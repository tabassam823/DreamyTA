import numpy as np
import pandas as pd
import os
from compute_endogenous_lambda import compute_endogenous_lambda
from find_nash_sbr import find_nash_sbr
from brute_force_validator import run_brute_force_window
from build_hamiltonian_total import build_hamiltonian_total
from find_optimal_lr_spsa import find_optimal_lr_spsa
from run_vqe_adaptive import run_vqe_adaptive
from calc_simple_return import calculate_simple_return
from calc_log_return import calculate_log_return
from calc_expected_returns import calculate_expected_simple_return, calculate_expected_log_return_with_drag
from calc_expected_returns import calculate_expected_simple_return, calculate_expected_log_return_with_drag

def run_strategy_step(lookback_data, tickers, curr_date, K=2, penalty_A=5.0,
                      max_depth=6, maxiter=100,
                      max_total_iter=500, batch_size=10,
                      conv_window=4, conv_tol=1e-3,
                      use_warm_start=True,
                      file_config=None):
    """
    Eksekusi satu periode pembelajaran dengan pencatatan tanggal.
    """
    if file_config is None:
        file_config = {
            'metrics': 'metrik_return_dan_lambda.csv',
            'bias_h': 'bias_h_total.csv',
            'interaksi_J': 'interaksi_J_total.csv',
            'pencarian_lr': 'hasil_pencarian_lr.csv',
            'parameter_pendamping': 'parameter_pendamping.csv'
        }
    
    n_assets = len(tickers)
    # ... rest of calculations ...
    # Simple Return dihitung manual via fungsi baru
    simple_rets = calculate_simple_return(lookback_data)
    # Log Return dihitung manual via fungsi baru
    log_rets  = calculate_log_return(lookback_data)
    
    binary_st = (log_rets <= 0).astype(int)   # 1 = turun, 0 = naik

    # --- PERHITUNGAN EXPECTED RETURN (Rumus Volatility Drag) ---
    mu_R_daily = calculate_expected_simple_return(simple_rets)
    # Variance log return sebagai dasar volatility drag
    var_r_daily = log_rets.var() 
    mu_r_daily = calculate_expected_log_return_with_drag(mu_R_daily, var_r_daily)

    # Menggunakan return periode (126 hari)
    mu_simple_period = mu_R_daily.values * 126
    mu_log_period = mu_r_daily.values * 126
    
    sigma_log = log_rets.std().values
    sigma_period_log = sigma_log * np.sqrt(126)
    
    # Matriks kovariansi tetap berbasis log return
    sigma_period_matrix = log_rets.cov().values * 126

    # gamma disini mewakili degree of risk-aversion, menggunakan mu_log_period (dengan drag) dan sigma_period_log
    gamma = compute_endogenous_lambda(mu_log_period, sigma_period_log)
    lam = penalty_A # penalty lambda untuk pembatas kardinalitas
    metrics_df = pd.DataFrame({
        'Date': [curr_date.date()] * n_assets,
        'Ticker': tickers,
        'Mu_Simple_Period': mu_simple_period,
        'Mu_Log_Period': mu_log_period,
        'Sigma_Log': sigma_log,
        'Sigma_Period_Log': sigma_period_log,
        'Lambda_RiskAversion': [gamma] * n_assets
    })
    
    metrics_df.to_csv(file_config['metrics'], mode='a', header=not os.path.exists(file_config['metrics']), index=False)

    # --- KONSTRUKSI MATRIKS Q (QUBO) TERPISAH ---
    # 1. Komponen Objektif (Return & Risk)
    Q_diag_obj = np.zeros(n_assets)
    Q_off_obj  = np.zeros((n_assets, n_assets))
    K_sq = K**2
    
    for i in range(n_assets):
        Q_diag_obj[i] = (gamma * sigma_period_matrix[i, i]) / (2.0 * K_sq) - (mu_simple_period[i] / K)
        for j in range(i + 1, n_assets):
            Q_val = (gamma * sigma_period_matrix[i, j]) / (2.0 * K_sq)
            Q_off_obj[i, j] = Q_val
            Q_off_obj[j, i] = Q_val

    # 2. Komponen Pinalti (Constraint)
    Q_diag_pen = np.zeros(n_assets)
    Q_off_pen  = np.zeros((n_assets, n_assets))
    for i in range(n_assets):
        Q_diag_pen[i] = (1.0 - 2.0 * K)
        for j in range(i + 1, n_assets):
            Q_off_pen[i, j] = 1.0
            Q_off_pen[j, i] = 1.0

    # --- KONSTRUKSI PARAMETER ISING TERPISAH ---
    # Fungsi pembantu untuk konversi Q ke h, J, C
    def qubo_to_ising(Q_diag, Q_off, constant=0.0):
        h = np.zeros(n_assets)
        J = np.zeros((n_assets, n_assets))
        for i in range(n_assets):
            sum_Q_ij_half = 0.0
            for j in range(n_assets):
                if i != j:
                    sum_Q_ij_half += Q_off[i, j] / 2.0
                    if i < j:
                        J[i, j] = Q_off[i, j] / 2.0
                        J[j, i] = Q_off[i, j] / 2.0
            h[i] = -((Q_diag[i] / 2.0) + sum_Q_ij_half)
        
        sum_Q_ii_half = np.sum(Q_diag) / 2.0
        sum_Q_ij_half_total = 0.0
        for i in range(n_assets):
            for j in range(i + 1, n_assets):
                sum_Q_ij_half_total += Q_off[i, j] / 2.0
        C = sum_Q_ii_half + sum_Q_ij_half_total + constant
        return h, J, C

    h_obj, J_obj, C_obj = qubo_to_ising(Q_diag_obj, Q_off_obj, 0.0)
    h_pen, J_pen, C_pen = qubo_to_ising(Q_diag_pen, Q_off_pen, float(K_sq))

    # --- EKSPOR BIAS & INTERAKSI TERPISAH ---
    h_df = pd.DataFrame({
        'Date': [curr_date.date()] * n_assets, 
        'Ticker': tickers, 
        'Bias_h_Obj': h_obj, 
        'Bias_h_Pen': h_pen
    })
    h_df.to_csv(file_config['bias_h'], mode='a', header=not os.path.exists(file_config['bias_h']), index=False)
    
    J_list = []
    for i in range(n_assets):
        for j in range(i + 1, n_assets):
            J_list.append({
                'Date': curr_date.date(), 
                'Ticker_i': tickers[i], 
                'Ticker_j': tickers[j], 
                'Interaction_J_Obj': J_obj[i, j],
                'Interaction_J_Pen': J_pen[i, j]
            })
    J_df = pd.DataFrame(J_list)
    J_df.to_csv(file_config['interaksi_J'], mode='a', header=not os.path.exists(file_config['interaksi_J']), index=False)

    # --- EKSPOR KONSTANTA C ISING TERPISAH ---
    c_df = pd.DataFrame({
        'Date': [curr_date.date()],
        'C_Obj': [C_obj],
        'C_Pen': [C_pen],
        'Penalty_A_Target': [penalty_A]
    })
    c_df.to_csv(file_config['parameter_pendamping'], mode='a', header=not os.path.exists(file_config['parameter_pendamping']), index=False)
    
    # Membangun Hamiltonian terpisah (Diperlukan untuk VQE & LR Finder)
    H_obj = build_hamiltonian_total(h_obj, J_obj, n_assets, offset=C_obj)
    H_pen = build_hamiltonian_total(h_pen, J_pen, n_assets, offset=C_pen)
    
    # [Tugas 4] Pencarian Nash Equilibrium (Hanya jika Warm-Start aktif)
    if use_warm_start:
        ne_bitstring, ne_utility = find_nash_sbr(mu_simple_period, sigma_period_matrix, gamma, curr_date, N=n_assets, K=K, history_file=file_config.get('nash_history', 'riwayat_nash_sbr.csv'))
        print(f"    [Nash Eq] Warm-start aktif. Bitstring: {ne_bitstring} | Utility: {ne_utility:.6f}")
        vqe_init_bs = ne_bitstring
    else:
        ne_bitstring, ne_utility = "N/A", 0.0
        vqe_init_bs = "0" * n_assets # Mulai dari |0...0>
        print("    [VQE] Warm-start dinonaktifkan. Memulai dari $|0...0\\rangle$")

    # [Validasi] Jalankan Brute Force Validation per window
    # Menggunakan Hamiltonian gabungan (Total) untuk pembanding energi VQE
    h_total = h_obj + penalty_A * h_pen
    J_total = J_obj + penalty_A * J_pen
    C_total = C_obj + penalty_A * C_pen
    
    print(f"    [Brute Force] Validasi global minimum untuk window {curr_date.date()}...")
    bf_bs, bf_e = run_brute_force_window(curr_date, n_assets, h_total, J_total, C_total, K, file_config)
    print(f"    [Brute Force] Global Min: {bf_bs} | Energy: {bf_e:.6f}")

    # [LR Finder] Menggunakan H gabungan dengan pinalti target bulan ini
    H_target = H_obj + penalty_A * H_pen
    print("    [LR Finder] Mencari Learning Rate optimal...")
    best_a, test_a_values, final_energies = find_optimal_lr_spsa(H_target, n_assets, curr_date, ne_bitstring=vqe_init_bs, K=K, test_iters=30, file_config=file_config)
    print(f"    [LR Finder] Base Learning Rate terpilih: {best_a:.4f}")

    # Optimasi VQE dengan Penalty Annealing
    selected_indices, depth_used, energy_final, best_history, best_ent_hist, best_gvar_hist, depth_energies, winning_probs, best_params = run_vqe_adaptive(
        H_obj, H_pen, n_assets, curr_date, ne_bitstring=vqe_init_bs, K=K, target_penalty=penalty_A,
        max_depth=max_depth, maxiter=maxiter,
        max_total_iter=max_total_iter, batch_size=batch_size,
        conv_window=conv_window, conv_tol=conv_tol, 
        best_a_base=best_a, file_config=file_config
    )

    lr_data = (test_a_values, final_energies, best_a)
    return selected_indices, depth_used, energy_final, best_history, best_ent_hist, best_gvar_hist, depth_energies, lr_data, ne_bitstring, ne_utility, winning_probs, best_params
