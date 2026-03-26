# =============================================================================
# hamiltonian.py — Konstruksi QUBO & Hamiltonian Ising
# =============================================================================
# Modul ini mengimplementasikan:
#   1. Pembentukan matriks QUBO dari parameter potensial (Eq. 24-25)
#   2. Pemetaan QUBO → Ising (J_ij, h_i) (Eq. 27-29)
#   3. Konstruksi operator Hamiltonian PennyLane (Eq. 30)
#   4. Brute force ground state search (untuk validasi N kecil)

import numpy as np
import pennylane as qml
from itertools import product


def build_qubo_matrix(strategic_returns, cov_diag, risk_matrix_amp,
                      gamma, lambda_pen, K, N):
    """
    Membangun matriks QUBO total Q^{total} yang menggabungkan
    biaya murni (pure cost) dan suku penalti kardinalitas.

    Sesuai kombinasi_GT_to_Ising.md Eq. (24)-(25):
        Q_{ii}^{total} = (γ/2)σ_{ii} - μ̃_i + λ(1 - 2K)
        Q_{ij}^{total} = γ σ̃_{ij} + 2λ     (untuk i ≠ j)

    Parameters
    ----------
    strategic_returns : np.ndarray
        Vektor μ̃ (panjang N).
    cov_diag : np.ndarray
        Vektor diagonal kovariansi σ_{ii} (panjang N).
    risk_matrix_amp : np.ndarray
        Matriks kovariansi yang diamplifikasi σ̃ (N×N).
    gamma : float
        Risk-aversion parameter.
    lambda_pen : float
        Pengali Lagrange untuk penalti kardinalitas.
    K : int
        Target kardinalitas.
    N : int
        Jumlah aset.

    Returns
    -------
    np.ndarray
        Matriks QUBO Q^{total} (N×N).
    """
    Q = np.zeros((N, N))

    # Elemen diagonal: Eq. (24)
    for i in range(N):
        Q[i, i] = (gamma / 2.0) * cov_diag[i] - strategic_returns[i] \
                   + lambda_pen * (1 - 2 * K)

    # Elemen off-diagonal: Eq. (25)
    for i in range(N):
        for j in range(i + 1, N):
            q_ij = gamma * risk_matrix_amp[i, j] + 2 * lambda_pen
            Q[i, j] = q_ij
            Q[j, i] = q_ij

    print(f"[Hamiltonian] Matriks QUBO total Q ({N}×{N}) berhasil dibangun.")
    return Q


def qubo_to_ising(Q, N):
    """
    Memetakan matriks QUBO ke parameter Ising (J_ij, h_i).

    Sesuai kombinasi_GT_to_Ising.md Eq. (27)-(29):
        J_{ij} = Q_{ij}^{total} / 4
        h_i    = -Q_{ii}^{total}/2 - Σ_{j≠i} Q_{ij}^{total}/4

    Parameters
    ----------
    Q : np.ndarray
        Matriks QUBO total (N×N).
    N : int
        Jumlah aset.

    Returns
    -------
    h : np.ndarray
        Vektor medan lokal (panjang N).
    J : np.ndarray
        Matriks kopling (N×N, upper triangular).
    """
    J = np.zeros((N, N))
    h = np.zeros(N)

    # Kopling: Eq. (27)
    for i in range(N):
        for j in range(i + 1, N):
            J[i, j] = Q[i, j] / 4.0
            J[j, i] = J[i, j]

    # Medan lokal: Eq. (28)-(29)
    for i in range(N):
        sum_Qij = 0.0
        for j in range(N):
            if j != i:
                sum_Qij += Q[i, j] / 4.0
        h[i] = -Q[i, i] / 2.0 - sum_Qij

    print(f"[Hamiltonian] Parameter Ising:")
    print(f"  h (medan lokal) = {h}")
    print(f"  J (kopling) diagonal-atas =")
    for i in range(N):
        for j in range(i + 1, N):
            print(f"    J[{i},{j}] = {J[i, j]:.6f}")

    return h, J


def build_pennylane_hamiltonian(h, J, n_qubits):
    """
    Membangun operator Hamiltonian PennyLane dari parameter Ising.

    Sesuai kombinasi_GT_to_Ising.md Eq. (30):
        Ĥ_Ising = Σ_{i<j} J_{ij} (Ẑ_i ⊗ Ẑ_j) + Σ_i h_i Ẑ_i

    Parameters
    ----------
    h : np.ndarray
        Vektor medan lokal.
    J : np.ndarray
        Matriks kopling.
    n_qubits : int
        Jumlah qubit.

    Returns
    -------
    qml.Hamiltonian
        Operator Hamiltonian PennyLane.
    """
    coeffs = []
    obs = []

    # Suku linear: h_i Z_i
    for i in range(n_qubits):
        if abs(h[i]) > 1e-10:
            coeffs.append(float(h[i]))
            obs.append(qml.PauliZ(i))

    # Suku kuadratik: J_ij Z_i Z_j
    for i in range(n_qubits):
        for j in range(i + 1, n_qubits):
            if abs(J[i, j]) > 1e-10:
                coeffs.append(float(J[i, j]))
                obs.append(qml.PauliZ(i) @ qml.PauliZ(j))

    # Fallback agar Hamiltonian tidak kosong
    if len(coeffs) == 0:
        coeffs.append(0.0)
        obs.append(qml.Identity(0))

    H = qml.Hamiltonian(coeffs, obs)
    print(f"[Hamiltonian] PennyLane Hamiltonian: {len(coeffs)} terms.")
    return H


def brute_force_ising(h, J, N, K=None):
    """
    Pencarian ground state secara brute force (exhaustive enumeration).
    Digunakan untuk validasi pada N kecil.

    Menghitung energi Ising:
        E(s) = Σ_i h_i s_i + Σ_{i<j} J_{ij} s_i s_j

    di mana s_i ∈ {+1, -1}, dengan konvensi:
        x_i = 0 → s_i = +1 (qubit |0⟩)
        x_i = 1 → s_i = -1 (qubit |1⟩)

    Parameters
    ----------
    h : np.ndarray
        Vektor medan lokal.
    J : np.ndarray
        Matriks kopling.
    N : int
        Jumlah aset.
    K : int, optional
        Jika diberikan, hanya evaluasi state dengan tepat K qubit bernilai 1.

    Returns
    -------
    best_bitstring : str
        Bitstring optimal (dalam representasi biner x ∈ {0,1}).
    best_energy : float
        Energi minimum.
    all_energies : dict
        Mapping {bitstring: energy} untuk semua konfigurasi.
    """
    best_energy = np.inf
    best_bitstring = None
    all_energies = {}

    for bits in product([0, 1], repeat=N):
        bitstring = ''.join(map(str, bits))

        # Kendala kardinalitas (jika ada)
        if K is not None and sum(bits) != K:
            continue

        # Konversi ke spin: x=0 → s=+1, x=1 → s=-1
        spins = np.array([1 - 2 * b for b in bits], dtype=float)

        # Hitung energi Ising
        energy = 0.0
        for i in range(N):
            energy += h[i] * spins[i]
        for i in range(N):
            for j in range(i + 1, N):
                energy += J[i, j] * spins[i] * spins[j]

        all_energies[bitstring] = energy

        if energy < best_energy:
            best_energy = energy
            best_bitstring = bitstring

    print(f"[Hamiltonian] Brute Force Ground State: |{best_bitstring}⟩, "
          f"E = {best_energy:.6f}")
    return best_bitstring, best_energy, all_energies
