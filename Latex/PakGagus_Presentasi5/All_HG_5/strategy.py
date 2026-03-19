# strategy.py
import numpy as np
from itertools import combinations

from game_theory import compute_endogenous_lambda, calc_payoff, compute_bias_GT
from quantum_info import calc_qmi, compute_coupling_QMI
from hamiltonian import build_hamiltonian_total
from vqe_solver import run_vqe_adaptive

def run_strategy_step(lookback_data, tickers, K=2, penalty_A=5.0,
                      max_depth=4, maxiter=100,
                      max_total_iter=2000, batch_size=25,
                      conv_window=4, conv_tol=1e-4):
    """
    Pipeline lengkap sesuai Bab-3.tex:
      1. Log return & binerisasi state
      2. Hitung lambda endogen
      3. Bangun payoff matrix → h_i^GT (Game Theory)
      4. Hitung QMI → J_ij^QMI (dengan scaling alpha = T_market)
      5. Hitung parameter penalti: h_i^pen dan J_ij^pen (bab10.tex §2)
      6. Susun parameter total: h_total, J_total
      7. Bangun Hamiltonian total
      8. Optimasi VQE adaptif (SPSA + adaptive layers)
    """
    n_assets = len(tickers)
    log_rets  = np.log(lookback_data / lookback_data.shift(1)).dropna()
    binary_st = (log_rets <= 0).astype(int)   # 1 = turun (|1⟩), 0 = naik (|0⟩)

    lam = compute_endogenous_lambda(log_rets, tickers)

    # ------------------------------------------------------------------
    # Step 3: Payoff Matrix dan Bias h_i^GT
    # ------------------------------------------------------------------
    all_payoffs = {}
    for idx_a, idx_b in combinations(range(n_assets), 2):
        a, b = tickers[idx_a], tickers[idx_b]
        pA, pB = calc_payoff(
            log_rets[a].values, log_rets[b].values,
            binary_st[a].values, binary_st[b].values, lam
        )
        all_payoffs[(idx_a, idx_b)] = (pA, pB)

    # Akumulasi h_GT per aset dari semua pair yang melibatkannya
    h_GT     = np.zeros(n_assets)
    h_counts = np.zeros(n_assets)
    for (idx_a, idx_b), (pA, pB) in all_payoffs.items():
        h_a, h_b = compute_bias_GT(pA, pB)
        h_GT[idx_a]     += h_a
        h_GT[idx_b]     += h_b
        h_counts[idx_a] += 1
        h_counts[idx_b] += 1

    for i in range(n_assets):
        if h_counts[i] > 0:
            h_GT[i] /= h_counts[i]

    # ------------------------------------------------------------------
    # Step 4: QMI & Kopling J_ij^QMI
    # ------------------------------------------------------------------
    # T_market = rata-rata varians log return (konvensi Econophysics, k_B=1)
    var_daily  = log_rets[tickers].var().values
    T_market   = var_daily.mean()
    if T_market < 1e-12:
        T_market = 1e-6

    J_QMI = np.zeros((n_assets, n_assets))
    for i in range(n_assets):
        for j in range(i + 1, n_assets):
            qmi_val  = calc_qmi(binary_st[tickers[i]].values,
                                binary_st[tickers[j]].values)
            # Korelasi empiris untuk menentukan tanda kopling
            rho_corr = np.corrcoef(log_rets[tickers[i]].values,
                                   log_rets[tickers[j]].values)[0, 1]
            j_val = compute_coupling_QMI(qmi_val, rho_corr, T_market)
            J_QMI[i, j] = j_val
            J_QMI[j, i] = j_val

    # ------------------------------------------------------------------
    # Step 5: Parameter Penalti (bab10.tex §2)
    #   K' = N/2 - K
    #   h_i^pen = -A * K'
    #   J_ij^pen = A / 2
    # ------------------------------------------------------------------
    K_prime   = (n_assets / 2.0) - K
    h_pen     = -penalty_A * K_prime           # Skalar (sama untuk semua i)
    J_pen_val =  penalty_A / 2.0              # Skalar (sama untuk semua i,j)

    h_pen_vec  = np.full(n_assets, h_pen)
    J_pen_mat  = np.zeros((n_assets, n_assets))
    for i in range(n_assets):
        for j in range(i + 1, n_assets):
            J_pen_mat[i, j] = J_pen_val
            J_pen_mat[j, i] = J_pen_val

    # ------------------------------------------------------------------
    # Step 6: Parameter Total
    # ------------------------------------------------------------------
    h_total = h_GT    + h_pen_vec
    J_total = J_QMI   + J_pen_mat

    # ------------------------------------------------------------------
    # Step 7 & 8: Bangun Hamiltonian & Optimasi VQE
    # ------------------------------------------------------------------
    H = build_hamiltonian_total(h_total, J_total, n_assets)
    selected_indices, depth_used, energy_final = run_vqe_adaptive(
        H, n_assets, K=K, max_depth=max_depth, maxiter=maxiter,
        max_total_iter=max_total_iter, batch_size=batch_size,
        conv_window=conv_window, conv_tol=conv_tol
    )

    return selected_indices, depth_used, energy_final
