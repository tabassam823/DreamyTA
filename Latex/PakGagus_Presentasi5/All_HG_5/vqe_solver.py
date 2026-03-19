# vqe_solver.py
import numpy as np
import pennylane as qml

def run_vqe_adaptive(H, n_qubits, K=2, max_depth=4,
                     maxiter=100, max_total_iter=2000,
                     batch_size=25, conv_window=4, conv_tol=1e-4,
                     seed=42):
    """
    Menjalankan VQE dengan dua mekanisme adaptif:

    (A) Adaptive SPSA Iterations (konvergensi otomatis):
        - SPSA dijalankan dalam batch kecil (``batch_size`` iterasi per batch).
        - Setelah setiap batch, evaluasi energi disimpan ke ``energy_history``.
        - Konvergensi terdeteksi jika relative change energi pada jendela
          ``conv_window`` batch terakhir di bawah ``conv_tol``:
              |E_{t-w} - E_t| / (|E_{t-w}| + eps) < conv_tol
        - Berhenti otomatis saat konvergen atau ``max_total_iter`` tercapai.
        - ``maxiter`` hanya digunakan sebagai batas bawah (minimal iterasi
          awal sebelum cek konvergensi dimulai).

    (B) Adaptive Layer Selection (sesuai flowchart Bab-3.tex):
        - Mulai dari depth=1; setelah SPSA konvergen, evaluasi E_L.
        - Tambah layer jika E_L < E_{L-1} (penurunan energi signifikan).
        - Berhenti jika energi tidak turun atau ``max_depth`` tercapai.

    Ansatz: EfficientSU(2) manual → lapisan RY-RZ dengan entanglement CNOT ring.
    Optimizer: SPSA dengan parameter standar (a=0.1, c=0.1, alpha=0.602, gamma=0.101).
    """
    dev = qml.device("default.qubit", wires=n_qubits)
    rng = np.random.default_rng(seed)

    def make_circuit(depth):
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

        Iterasi dibagi menjadi batch kecil (``batch_size``). Setelah setiap
        batch selesai, energi dievaluasi dan disimpan ke ``energy_history``.
        Konvergensi dianggap tercapai apabila memenuhi SALAH SATU kondisi:
            (1) Total iterasi >= ``max_total_iter``, atau
            (2) Setelah minimal ``maxiter`` iterasi, relative energy change
                dalam jendela ``conv_window`` batch terakhir < ``conv_tol``:
                    |E_{hist[-w]} - E_{hist[-1]}| / (|E_{hist[-w]}| + 1e-12)
                    < conv_tol

        Return:
            params        (np.ndarray): Parameter optimal hasil SPSA
            final_energy  (float)     : Energi terakhir saat konvergen
            energy_history (list)     : Energi per-batch untuk diagnostik
            total_iters   (int)       : Total iterasi yang digunakan
        """
        a, c      = 0.1, 0.1
        A_coeff   = maxiter * 0.1    # A mengacu pada ``maxiter`` awal sebagai referensi skala
        alpha_exp = 0.602
        gamma_exp = 0.101

        if init_params is not None:
            params = init_params.copy()
        else:
            params = rng.uniform(0, 2 * np.pi, n_params)

        energy_history = []
        total_iters    = 0
        converged      = False

        while total_iters < max_total_iter:
            # --- Satu batch SPSA ---
            for _ in range(batch_size):
                k     = total_iters
                a_k   = a / (A_coeff + k + 1) ** alpha_exp
                c_k   = c / (k + 1)           ** gamma_exp
                delta = 2 * rng.integers(0, 2, size=n_params) - 1

                cost_plus  = float(cost_circuit(params + c_k * delta))
                cost_minus = float(cost_circuit(params - c_k * delta))
                grad       = (cost_plus - cost_minus) / (2 * c_k * delta)
                params     = params - a_k * grad
                total_iters += 1

            # --- Evaluasi energi setelah batch selesai ---
            current_energy = float(cost_circuit(params))
            energy_history.append(current_energy)

            # --- Cek konvergensi (hanya setelah minimal maxiter iterasi) ---
            if total_iters >= maxiter and len(energy_history) >= conv_window:
                E_old = energy_history[-conv_window]
                E_now = energy_history[-1]
                rel_change = abs(E_old - E_now) / (abs(E_old) + 1e-12)
                if rel_change < conv_tol:
                    converged = True
                    break

        return params, energy_history[-1], energy_history, total_iters

    # --- Adaptive Layer Loop ---
    best_energy    = np.inf
    best_params    = None
    best_depth     = 1
    best_history   = []

    for depth in range(1, max_depth + 1):
        n_params = n_qubits * 2 * (depth + 1)
        cost_fn, prob_fn = make_circuit(depth)

        # Inisialisasi: warm-start dari parameter depth sebelumnya jika ada
        if best_params is not None and len(best_params) < n_params:
            init_p = np.concatenate([
                best_params,
                rng.uniform(0, 2 * np.pi, n_params - len(best_params))
            ])
        else:
            init_p = None

        params, energy, e_hist, n_iters = run_spsa(cost_fn, n_params, init_params=init_p)

        print(f"    [Depth {depth}] Konvergen dalam {n_iters} iterasi | E = {energy:.6f}")

        if energy < best_energy:
            best_energy  = energy
            best_params  = params
            best_depth   = depth
            best_history = e_hist
        else:
            # Energi tidak turun → berhenti menambah layer
            break

    # Evaluasi probabilitas pada depth terbaik
    _, prob_fn = make_circuit(best_depth)
    probs = prob_fn(best_params)

    # Pilih bitstring dengan tepat K qubit = 1 dan probabilitas tertinggi
    sorted_indices = np.argsort(probs)[::-1]
    best_bitstring = None
    for idx in sorted_indices:
        bs = format(idx, f'0{n_qubits}b')
        if bs.count('1') == K:
            best_bitstring = bs
            break

    if best_bitstring is None:
        # Fallback: pilih K indeks dengan probabilitas tertinggi
        best_bitstring = '0' * n_qubits
        top_k = np.argsort(probs)[-K:]
        bs_list = list('0' * n_qubits)
        for idx in top_k:
            bs_list[idx] = '1'
        best_bitstring = ''.join(bs_list)

    selected_indices = [i for i, bit in enumerate(best_bitstring) if bit == '1']
    return selected_indices, best_depth, best_energy
