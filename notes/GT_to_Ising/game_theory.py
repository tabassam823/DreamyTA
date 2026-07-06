# =============================================================================
# game_theory.py — Analisis Game Theory & Classical Mutual Information
# =============================================================================
# Modul ini mengimplementasikan:
#   1. Distribusi probabilitas microstate P(s₁, s₂, ..., sₙ)
#   2. Strategic return μ̃ᵢ (Eq. 13)
#   3. Shannon Entropy & Classical Mutual Information (Eq. 15)
#   4. Normalized Mutual Information (NMI)
#   5. Risk matrix amplification σ̃ᵢⱼ (Eq. 16-17)

import numpy as np
from itertools import product


def compute_marginal_probabilities(binary_states, tickers):
    """
    Menghitung probabilitas marginal P(Sᵢ = s) untuk setiap aset.

    Sesuai kombinasi_GT_to_Ising.md §4.1:
        P(Sᵢ = s) = (1/T) Σ I(S_{i,t} = s)

    Parameters
    ----------
    binary_states : pd.DataFrame
        State biner (0=up, 1=down) per aset per hari.
    tickers : list[str]
        Daftar simbol aset.

    Returns
    -------
    dict
        {ticker: np.array([P(up), P(down)])}
    """
    T = len(binary_states)
    marginals = {}
    for ticker in tickers:
        counts = np.bincount(binary_states[ticker].values, minlength=2)
        marginals[ticker] = counts / T
    return marginals


def compute_strategic_return(log_returns, binary_states, tickers):
    """
    Menghitung strategic return μ̃ᵢ untuk setiap aset.

    Sesuai kombinasi_GT_to_Ising.md Eq. (13):
        μ̃ᵢ = Σ_{s∈{u,d}} P(Sᵢ=s) × μ_{i,s}

    di mana μ_{i,s} adalah conditional expected return saat state s.

    Parameters
    ----------
    log_returns : pd.DataFrame
        Log returns harian.
    binary_states : pd.DataFrame
        Binary states (0=up, 1=down).
    tickers : list[str]
        Daftar ticker.

    Returns
    -------
    np.ndarray
        Vektor strategic returns μ̃ (panjang N).
    """
    N = len(tickers)
    mu_tilde = np.zeros(N)

    for i, ticker in enumerate(tickers):
        states = binary_states[ticker].values
        returns = log_returns[ticker].values
        T = len(states)

        for s in [0, 1]:  # 0=up, 1=down
            mask = (states == s)
            count_s = mask.sum()
            P_s = count_s / T
            if count_s > 0:
                mu_s = returns[mask].mean()
            else:
                mu_s = 0.0
            mu_tilde[i] += P_s * mu_s

    print(f"[Game Theory] Strategic returns μ̃ = {mu_tilde}")
    return mu_tilde


def compute_joint_probability(binary_states, ticker_i, ticker_j):
    """
    Menghitung distribusi probabilitas bersama P(Sᵢ=s, Sⱼ=s')
    untuk pasangan aset (i, j).

    Sesuai kombinasi_GT_to_Ising.md Eq. (14):
        P(Sᵢ=s, Sⱼ=s') = (1/T) Σ I(S_{i,t}=s) · I(S_{j,t}=s')

    Parameters
    ----------
    binary_states : pd.DataFrame
        Binary states.
    ticker_i, ticker_j : str
        Simbol aset pasangan.

    Returns
    -------
    np.ndarray
        Matriks probabilitas bersama 2×2.
    """
    T = len(binary_states)
    joint = np.zeros((2, 2))
    si = binary_states[ticker_i].values
    sj = binary_states[ticker_j].values

    for t in range(T):
        joint[si[t], sj[t]] += 1

    return joint / T


def compute_shannon_entropy(probs):
    """
    Menghitung Shannon entropy:  H(X) = -Σ p(x) log₂ p(x)

    Parameters
    ----------
    probs : np.ndarray
        Vektor probabilitas (1-D).

    Returns
    -------
    float
        Nilai entropy dalam bits.
    """
    probs = probs[probs > 1e-12]
    return -np.sum(probs * np.log2(probs))


def compute_mutual_information(binary_states, ticker_i, ticker_j):
    """
    Menghitung Classical Mutual Information (CMI) antar pasangan aset.

    Sesuai kombinasi_GT_to_Ising.md Eq. (15):
        I(i:j) = Σ_{s,s'} P(Sᵢ=s, Sⱼ=s') log₂ [P(s,s') / (P(s)·P(s'))]

    Parameters
    ----------
    binary_states : pd.DataFrame
        Binary states.
    ticker_i, ticker_j : str
        Simbol aset pasangan.

    Returns
    -------
    float
        Nilai mutual information I(i:j) ≥ 0 (bits).
    """
    P_joint = compute_joint_probability(binary_states, ticker_i, ticker_j)
    P_i = P_joint.sum(axis=1)   # Marginal Sᵢ
    P_j = P_joint.sum(axis=0)   # Marginal Sⱼ

    mi = 0.0
    for s in range(2):
        for s_prime in range(2):
            p_ss = P_joint[s, s_prime]
            if p_ss > 1e-12 and P_i[s] > 1e-12 and P_j[s_prime] > 1e-12:
                mi += p_ss * np.log2(p_ss / (P_i[s] * P_j[s_prime]))

    return max(mi, 0.0)


def compute_nmi_matrix(binary_states, tickers):
    """
    Menghitung matriks Normalized Mutual Information (NMI).

    NMI(i,j) = I(i:j) / sqrt(H(i) × H(j))

    Parameters
    ----------
    binary_states : pd.DataFrame
        Binary states.
    tickers : list[str]
        Daftar ticker.

    Returns
    -------
    np.ndarray
        Matriks NMI (N×N), simetris.
    """
    N = len(tickers)
    marginals = compute_marginal_probabilities(binary_states, tickers)
    nmi_mat = np.zeros((N, N))

    # Shannon entropy per aset
    H = np.array([compute_shannon_entropy(marginals[t]) for t in tickers])

    for i in range(N):
        for j in range(i + 1, N):
            mi = compute_mutual_information(binary_states, tickers[i], tickers[j])
            denom = np.sqrt(H[i] * H[j]) if (H[i] > 1e-12 and H[j] > 1e-12) else 1.0
            nmi_val = mi / denom
            nmi_mat[i, j] = nmi_val
            nmi_mat[j, i] = nmi_val

    print(f"[Game Theory] NMI Matrix:\n{np.array2string(nmi_mat, precision=4)}")
    return nmi_mat


def compute_xi_cmi(cov_matrix, nmi_matrix, N):
    """
    Menghitung koefisien penskalaan dimensional ξ^CMI.

    Sesuai kombinasi_GT_to_Ising.md Eq. (17):
        ξ^CMI = (Σ_{i<j} |σᵢⱼ|) / (Σ_{i<j} I(i:j))

    Di sini kita menggunakan NMI sebagai input (sudah ternormalisasi).

    Parameters
    ----------
    cov_matrix : np.ndarray
        Matriks kovariansi standar (N×N).
    nmi_matrix : np.ndarray
        Matriks NMI (N×N).
    N : int
        Jumlah aset.

    Returns
    -------
    float
        Nilai ξ^CMI untuk penskalaan.
    """
    sum_cov = 0.0
    sum_nmi = 0.0
    for i in range(N):
        for j in range(i + 1, N):
            sum_cov += abs(cov_matrix[i, j])
            sum_nmi += nmi_matrix[i, j]

    if sum_nmi < 1e-12:
        xi = 1.0
    else:
        xi = sum_cov / sum_nmi

    print(f"[Game Theory] ξ^CMI = {xi:.6f}")
    return xi


def amplify_risk_matrix(cov_matrix, nmi_matrix, xi, N):
    """
    Memodifikasi matriks kovariansi dengan amplifikasi informasional.

    Sesuai kombinasi_GT_to_Ising.md Eq. (16):
        σ̃ᵢⱼ = σᵢⱼ × [1 + ξ^CMI · NMI(i,j)]

    Elemen diagonal (varians) tetap tidak berubah.

    Parameters
    ----------
    cov_matrix : np.ndarray
        Matriks kovariansi standar (N×N).
    nmi_matrix : np.ndarray
        Matriks NMI (N×N).
    xi : float
        Koefisien penskalaan ξ^CMI.
    N : int
        Jumlah aset.

    Returns
    -------
    np.ndarray
        Matriks kovariansi yang telah diamplifikasi σ̃ (N×N).
    """
    sigma_tilde = cov_matrix.copy()
    for i in range(N):
        for j in range(N):
            if i != j:
                sigma_tilde[i, j] = cov_matrix[i, j] * (1.0 + xi * nmi_matrix[i, j])

    print(f"[Game Theory] Amplified risk matrix σ̃ (off-diagonal modified).")
    return sigma_tilde
