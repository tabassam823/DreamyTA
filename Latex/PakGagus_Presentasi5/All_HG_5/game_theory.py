# game_theory.py
import numpy as np

def compute_endogenous_lambda(log_returns, tickers):
    """
    Menghitung parameter risk-aversion lambda secara endogen berdasarkan
    Sharpe Ratio rata-rata lintas aset, menggunakan fungsi sigmoid/logistik.
    """
    mu_annual    = log_returns[tickers].mean() * 252
    sigma_annual = log_returns[tickers].std()  * np.sqrt(252)
    mu_avg    = abs(mu_annual).mean()
    sigma_avg = sigma_annual.mean()
    if np.isnan(mu_avg) or np.isnan(sigma_avg) or (mu_avg + sigma_avg) == 0:
        return 0.5
    Z = mu_avg / sigma_avg   # Sharpe Ratio agregat
    return 1.0 / (1.0 + np.exp(Z))

def calc_payoff(ret_A, ret_B, st_A, st_B, lam):
    """
    Menghitung matriks payoff 2x2 untuk pasangan aset (A, B).
    
    Utilitas setiap hari: u_i(t) = (1-lam)*r_i(t)*252 - lam*|r_i(t)*252|
    Payoff dirata-ratakan per konfigurasi biner (s_A, s_B).
    """
    pA     = np.zeros((2, 2))
    pB     = np.zeros((2, 2))
    counts = np.zeros((2, 2))

    for t in range(len(st_A)):
        s, r  = int(st_A[t]), int(st_B[t])
        u_A   = (1 - lam) * (ret_A[t] * 252) - lam * abs(ret_A[t] * 252)
        u_B   = (1 - lam) * (ret_B[t] * 252) - lam * abs(ret_B[t] * 252)
        counts[s, r] += 1
        pA[s, r]     += u_A
        pB[s, r]     += u_B

    for s in range(2):
        for r in range(2):
            if counts[s, r] > 0:
                pA[s, r] /= counts[s, r]
                pB[s, r] /= counts[s, r]
    return pA, pB


def compute_bias_GT(pA, pB):
    """
    Menghitung bias lokal h_i^GT berdasarkan selisih expected payoff:
        h_A^GT = (E[pA | s_A=+1] - E[pA | s_A=-1]) / 2
        h_B^GT = (E[pB | s_B=+1] - E[pB | s_B=-1]) / 2

    Sesuai bab10.tex §3 (Pencarian Bias Lokal melalui Game Theory).
    s=+1 (naik)  → baris/kolom indeks 0  (state biner 0 ≡ |0⟩)
    s=-1 (turun) → baris/kolom indeks 1  (state biner 1 ≡ |1⟩)

    E[pA | s_A=+1] = rata-rata baris 0 → (pA[0,0] + pA[0,1]) / 2
    E[pA | s_A=-1] = rata-rata baris 1 → (pA[1,0] + pA[1,1]) / 2
    """
    E_A_up   = (pA[0, 0] + pA[0, 1]) / 2.0
    E_A_down = (pA[1, 0] + pA[1, 1]) / 2.0
    h_A_GT   = (E_A_up - E_A_down) / 2.0

    E_B_up   = (pB[0, 0] + pB[1, 0]) / 2.0
    E_B_down = (pB[0, 1] + pB[1, 1]) / 2.0
    h_B_GT   = (E_B_up - E_B_down) / 2.0

    return h_A_GT, h_B_GT
