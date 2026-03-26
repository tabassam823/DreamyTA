# =============================================================================
# vqe_optimizer.py — VQE dengan Adaptive Layer Selection (EfficientSU2 + SPSA)
# =============================================================================
# Modul ini mengimplementasikan:
#   1. Ansatz EfficientSU2 (RY-RZ + CNOT ring)
#   2. Optimizer SPSA dengan adaptive convergence detection
#   3. Adaptive layer selection (depth incremental)
#
# Sesuai referensi All_HG.py §7 dan Rencana §E.

import numpy as np
import pennylane as qml


def run_vqe_adaptive(H, n_qubits, K=2, max_depth=4,
                     maxiter=100, max_total_iter=2000,
                     batch_size=25, conv_window=4, conv_tol=1e-4,
                     seed=42):
    """
    Menjalankan VQE dengan dua mekanisme adaptif:

    (A) Adaptive SPSA Iterations (konvergensi otomatis):
        - SPSA dijalankan dalam batch kecil (batch_size iterasi per batch).
        - Konvergensi terdeteksi jika relative change energi pada jendela
          conv_window batch terakhir di bawah conv_tol.
        - Berhenti otomatis saat konvergen atau max_total_iter tercapai.

    (B) Adaptive Layer Selection:
        - Mulai dari depth=1; setelah SPSA konvergen, evaluasi E_L.
        - Tambah layer jika E_L < E_{L-1} (penurunan energi signifikan).
        - Berhenti jika energi tidak turun atau max_depth tercapai.

    Ansatz: EfficientSU(2) → lapisan RY-RZ dengan entanglement CNOT ring.
    Optimizer: SPSA (a=0.1, c=0.1, alpha=0.602, gamma=0.101).

    Parameters
    ----------
    H : qml.Hamiltonian
        Operator Hamiltonian Ising.
    n_qubits : int
        Jumlah qubit (= jumlah aset).
    K : int
        Target kardinalitas portofolio.
    max_depth : int
        Kedalaman maksimum ansatz.
    maxiter : int
        Iterasi minimum SPSA sebelum cek konvergensi.
    max_total_iter : int
        Batas atas total iterasi SPSA per depth.
    batch_size : int
        Ukuran batch SPSA (iterasi per evaluasi konvergensi).
    conv_window : int
        Jumlah batch untuk sliding window konvergensi.
    conv_tol : float
        Toleransi relative change untuk konvergensi.
    seed : int
        Random seed.

    Returns
    -------
    selected_indices : list[int]
        Indeks aset yang terpilih (K aset dengan qubit=1).
    best_depth : int
        Kedalaman ansatz optimal.
    best_energy : float
        Energi minimum yang ditemukan.
    best_history : list[float]
        Riwayat energi per batch (untuk convergence plot).
    best_probs : np.ndarray
        Distribusi probabilitas state pada depth optimal.
    """
    dev = qml.device("default.qubit", wires=n_qubits)
    rng = np.random.default_rng(seed)

    def make_circuit(depth):
        """Membuat cost circuit dan probability circuit untuk depth tertentu."""

        @qml.qnode(dev)
        def cost_circuit(params):
            w = params.reshape((depth + 1, n_qubits, 2))
            for layer in range(depth + 1):
                for q in range(n_qubits):
                    qml.RY(w[layer, q, 0], wires=q)
                    qml.RZ(w[layer, q, 1], wires=q)
                if layer < depth:
                    for q in range(n_qubits - 1):
                        qml.CNOT(wires=[q, q + 1])
                    qml.CNOT(wires=[n_qubits - 1, 0])
            return qml.expval(H)

        @qml.qnode(dev)
        def prob_circuit(params):
            w = params.reshape((depth + 1, n_qubits, 2))
            for layer in range(depth + 1):
                for q in range(n_qubits):
                    qml.RY(w[layer, q, 0], wires=q)
                    qml.RZ(w[layer, q, 1], wires=q)
                if layer < depth:
                    for q in range(n_qubits - 1):
                        qml.CNOT(wires=[q, q + 1])
                    qml.CNOT(wires=[n_qubits - 1, 0])
            return qml.probs(wires=range(n_qubits))

        return cost_circuit, prob_circuit

    def run_spsa(cost_circuit, n_params, init_params=None):
        """
        Menjalankan SPSA dengan adaptive convergence detection.

        Returns
        -------
        params : np.ndarray
            Parameter optimal.
        final_energy : float
            Energi terakhir.
        energy_history : list[float]
            Riwayat energi per batch.
        total_iters : int
            Total iterasi yang dijalankan.
        """
        a, c = 0.1, 0.1
        A_coeff = maxiter * 0.1
        alpha_exp = 0.602
        gamma_exp = 0.101

        if init_params is not None:
            params = init_params.copy()
        else:
            params = rng.uniform(0, 2 * np.pi, n_params)

        energy_history = []
        total_iters = 0

        while total_iters < max_total_iter:
            # --- Satu batch SPSA ---
            for _ in range(batch_size):
                k = total_iters
                a_k = a / (A_coeff + k + 1) ** alpha_exp
                c_k = c / (k + 1) ** gamma_exp
                delta = 2 * rng.integers(0, 2, size=n_params) - 1

                cost_plus = float(cost_circuit(params + c_k * delta))
                cost_minus = float(cost_circuit(params - c_k * delta))
                grad = (cost_plus - cost_minus) / (2 * c_k * delta)
                params = params - a_k * grad
                total_iters += 1

            # --- Evaluasi energi setelah batch ---
            current_energy = float(cost_circuit(params))
            energy_history.append(current_energy)

            # --- Cek konvergensi ---
            if total_iters >= maxiter and len(energy_history) >= conv_window:
                E_old = energy_history[-conv_window]
                E_now = energy_history[-1]
                rel_change = abs(E_old - E_now) / (abs(E_old) + 1e-12)
                if rel_change < conv_tol:
                    break

        return params, energy_history[-1], energy_history, total_iters

    # --- Adaptive Layer Loop ---
    best_energy = np.inf
    best_params = None
    best_depth = 1
    best_history = []

    print(f"[VQE] Memulai VQE adaptive (max_depth={max_depth}, "
          f"maxiter={maxiter}, batch={batch_size})...")

    for depth in range(1, max_depth + 1):
        n_params = n_qubits * 2 * (depth + 1)
        cost_fn, prob_fn = make_circuit(depth)

        # Warm-start dari depth sebelumnya
        if best_params is not None and len(best_params) < n_params:
            init_p = np.concatenate([
                best_params,
                rng.uniform(0, 2 * np.pi, n_params - len(best_params))
            ])
        else:
            init_p = None

        params, energy, e_hist, n_iters = run_spsa(
            cost_fn, n_params, init_params=init_p
        )

        print(f"  [Depth {depth}] Konvergen dalam {n_iters} iterasi "
              f"| E = {energy:.6f}")

        if energy < best_energy:
            best_energy = energy
            best_params = params
            best_depth = depth
            best_history = e_hist
        else:
            # Energi tidak turun → berhenti menambah layer
            print(f"  [Depth {depth}] Energi tidak menurun, berhenti.")
            break

    # --- Evaluasi probabilitas pada depth terbaik ---
    _, prob_fn = make_circuit(best_depth)
    best_probs = prob_fn(best_params)

    # --- Pilih bitstring dengan tepat K qubit = 1 ---
    sorted_indices = np.argsort(best_probs)[::-1]
    best_bitstring = None
    for idx in sorted_indices:
        bs = format(idx, f'0{n_qubits}b')
        if bs.count('1') == K:
            best_bitstring = bs
            break

    if best_bitstring is None:
        # Fallback: pilih K qubit dengan probabilitas tertinggi
        bs_list = list('0' * n_qubits)
        top_k = np.argsort(best_probs)[-K:]
        for idx in top_k:
            bs_list[idx] = '1'
        best_bitstring = ''.join(bs_list)

    selected_indices = [i for i, bit in enumerate(best_bitstring)
                        if bit == '1']

    print(f"[VQE] Ground State: |{best_bitstring}⟩, E = {best_energy:.6f}")
    print(f"[VQE] Depth optimal: {best_depth}")
    print(f"[VQE] Aset terpilih: indeks {selected_indices}")

    return selected_indices, best_depth, best_energy, best_history, best_probs
