# =============================================================================
# nash_equilibrium.py — Pencarian Nash Equilibrium via Best Response Dynamics
# =============================================================================
# Modul ini mengimplementasikan:
#   1. Evaluasi Fungsi Potensial Φ(x) (Eq. 18 + penalty)
#   2. Algoritma Best Response Dynamics (Rencana §6)

import numpy as np


def potential_function(x, strategic_returns, risk_matrix_amp, cov_diag,
                       gamma, lambda_pen, K):
    """
    Menghitung Fungsi Potensial Φ(x) dengan suku penalti kardinalitas.

    Sesuai kombinasi_GT_to_Ising.md Eq. (18) + Eq. (21):
        Φ(x) = Σ μ̃ᵢ xᵢ - (γ/2) Σᵢⱼ σ̃ᵢⱼ xᵢ xⱼ - λ(Σxᵢ - K)²

    Catatan: suku diagonal σ_{ii} menggunakan varians standar (bukan
    yang diamplifikasi) sesuai Eq. (18).

    Parameters
    ----------
    x : np.ndarray
        Vektor strategi biner (panjang N).
    strategic_returns : np.ndarray
        Vektor μ̃ (panjang N).
    risk_matrix_amp : np.ndarray
        Matriks kovariansi yang diamplifikasi σ̃ (N×N).
    cov_diag : np.ndarray
        Vektor diagonal kovariansi standar σ_{ii} (panjang N).
    gamma : float
        Risk-aversion parameter.
    lambda_pen : float
        Pengali Lagrange.
    K : int
        Target kardinalitas.

    Returns
    -------
    float
        Nilai fungsi potensial Φ(x).
    """
    N = len(x)

    # Return term: Σ μ̃ᵢ xᵢ
    return_term = np.dot(strategic_returns, x)

    # Risk term: (γ/2) Σᵢⱼ σ̃ᵢⱼ xᵢ xⱼ
    # Menggunakan diagonal standar dan off-diagonal yang diamplifikasi
    risk_term = 0.0
    for i in range(N):
        risk_term += cov_diag[i] * x[i] * x[i]   # σ_{ii} x_i²
        for j in range(i + 1, N):
            risk_term += 2.0 * risk_matrix_amp[i, j] * x[i] * x[j]
    risk_term *= gamma / 2.0

    # Penalty term: λ(Σxᵢ - K)²
    penalty_term = lambda_pen * (np.sum(x) - K) ** 2

    return return_term - risk_term - penalty_term


def best_response_dynamics(N, strategic_returns, risk_matrix_amp, cov_diag,
                            gamma, lambda_pen, K, max_iter=100,
                            n_restarts=10, seed=42):
    """
    Pencarian Nash Equilibrium menggunakan Best Response Dynamics.

    Sesuai pseudocode Rencana_kombinasi.md §6:
        1. Inisialisasi x secara acak
        2. Iterasi: untuk setiap pemain i, evaluasi Φ(x|xᵢ=0) vs Φ(x|xᵢ=1)
        3. Pilih strategi yang memaksimalkan Φ
        4. Ulangi hingga konvergen (tidak ada perubahan)

    Multiple restarts digunakan untuk menghindari minimum lokal.

    Parameters
    ----------
    N : int
        Jumlah aset.
    strategic_returns : np.ndarray
        Vektor μ̃.
    risk_matrix_amp : np.ndarray
        Matriks σ̃.
    cov_diag : np.ndarray
        Vektor σ_{ii}.
    gamma : float
        Risk-aversion.
    lambda_pen : float
        Pengali Lagrange.
    K : int
        Target kardinalitas.
    max_iter : int
        Iterasi maksimum per restart.
    n_restarts : int
        Jumlah restart acak.
    seed : int
        Random seed.

    Returns
    -------
    x_nash : np.ndarray
        Profil strategi Nash Equilibrium (vektor biner).
    phi_nash : float
        Nilai fungsi potensial pada NE.
    """
    rng = np.random.default_rng(seed)
    best_x = None
    best_phi = -np.inf

    for restart in range(n_restarts):
        # Inisialisasi acak
        x = rng.integers(0, 2, size=N).astype(float)

        for iteration in range(max_iter):
            changed = False

            for i in range(N):
                # Evaluasi utilitas jika x_i = 0
                x_test_0 = x.copy()
                x_test_0[i] = 0.0
                phi_0 = potential_function(x_test_0, strategic_returns,
                                           risk_matrix_amp, cov_diag,
                                           gamma, lambda_pen, K)

                # Evaluasi utilitas jika x_i = 1
                x_test_1 = x.copy()
                x_test_1[i] = 1.0
                phi_1 = potential_function(x_test_1, strategic_returns,
                                           risk_matrix_amp, cov_diag,
                                           gamma, lambda_pen, K)

                # Best response
                if phi_1 > phi_0 and x[i] == 0:
                    x[i] = 1.0
                    changed = True
                elif phi_0 > phi_1 and x[i] == 1:
                    x[i] = 0.0
                    changed = True

            # Konvergensi: tidak ada perubahan
            if not changed:
                break

        phi_current = potential_function(x, strategic_returns,
                                          risk_matrix_amp, cov_diag,
                                          gamma, lambda_pen, K)

        if phi_current > best_phi:
            best_phi = phi_current
            best_x = x.copy()

    x_nash = best_x
    phi_nash = best_phi

    # Konversi ke bitstring dan indeks terpilih
    bitstring = ''.join([str(int(b)) for b in x_nash])
    selected = [i for i in range(N) if x_nash[i] == 1]

    print(f"[Nash EQ] Nash Equilibrium: |{bitstring}⟩")
    print(f"[Nash EQ] Φ(x_nash) = {phi_nash:.6f}")
    print(f"[Nash EQ] Aset terpilih: indeks {selected}")

    return x_nash, phi_nash
