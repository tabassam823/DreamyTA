import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')

from config import *
from data_loader import download_data
from math_helpers import compute_endogenous_lambda, compute_strategic_returns, calc_NMI
from hamiltonian import build_hamiltonian_total
from nash_equilibrium import find_nash_equilibrium
from vqe_optimizer import run_vqe_adaptive

def rebalance_portfolio(current_cash, current_holdings, target_weights, prices):
    total_value    = current_cash + np.sum(current_holdings * prices)
    target_values  = total_value * target_weights
    new_holdings   = current_holdings.copy()
    new_cash       = current_cash

    for j in range(N):
        c_val = new_holdings[j] * prices[j]
        if c_val > target_values[j]:
            sell_val        = c_val - target_values[j]
            new_cash       += sell_val
            new_holdings[j] -= sell_val / prices[j]

    for j in range(N):
        c_val = new_holdings[j] * prices[j]
        if c_val < target_values[j]:
            buy_val       = min(target_values[j] - c_val, new_cash)
            new_cash     -= buy_val
            new_holdings[j] += buy_val / prices[j]

    return new_cash, new_holdings

def run_strategy_step(lookback_data, tickers, K, penalty_A, max_depth, maxiter):
    n_assets = len(tickers)
    log_rets  = np.log(lookback_data / lookback_data.shift(1)).dropna()
    binary_st = (log_rets <= 0).astype(int)

    gamma = compute_endogenous_lambda(log_rets, tickers)
    lam = penalty_A
    
    mu = log_rets.mean().values
    mu_tilde = compute_strategic_returns(log_rets, binary_st, tickers)
    cov_emp = log_rets.cov().values
    sigma_tilde = np.zeros((n_assets, n_assets))
    
    for i in range(n_assets):
        for j in range(n_assets):
            if i == j:
                sigma_tilde[i, i] = cov_emp[i, i]
            else:
                nmi_val = calc_NMI(binary_st[tickers[i]].values, binary_st[tickers[j]].values)
                sigma_tilde[i, j] = cov_emp[i, j] * (1.0 + nmi_val)

    h_total = np.zeros(n_assets)
    J_total = np.zeros((n_assets, n_assets))

    for i in range(n_assets):
        for j in range(i + 1, n_assets):
            J_val = (gamma * sigma_tilde[i, j] + 2 * lam) / 4.0
            J_total[i, j] = J_val
            J_total[j, i] = J_val
            
    for i in range(n_assets):
        sum_J_ij = 0.0
        for j in range(n_assets):
            if i != j:
                sum_J_ij += (gamma * sigma_tilde[i, j] + 2 * lam) / 4.0
        h_total[i] = -0.5 * ((gamma / 2.0) * sigma_tilde[i, i] - mu_tilde[i] + lam * (1.0 - 2.0 * K)) - sum_J_ij

    ne_bitstring, ne_energy, all_ne_energies = find_nash_equilibrium(h_total, J_total, N=n_assets, K=K)
    print(f"    [Nash Eq] Bitstring: {ne_bitstring} | Energy: {ne_energy:.6f}")

    H = build_hamiltonian_total(h_total, J_total, n_assets)
    
    selected_indices, depth_used, energy_final, best_history, energies_per_depth = run_vqe_adaptive(
        H, n_assets, ne_bitstring=ne_bitstring, K=K, max_depth=max_depth, maxiter=maxiter
    )

    debug_data = {
        'mu': mu,
        'mu_tilde': mu_tilde,
        'sigma': cov_emp,
        'sigma_tilde': sigma_tilde,
        'all_ne_energies': all_ne_energies,
        'spsa_history': best_history,
        'energies_per_depth': energies_per_depth
    }

    return selected_indices, depth_used, energy_final, debug_data

if __name__ == "__main__":
    data_clean = download_data(tickers)
    
    start_bt_date    = pd.to_datetime('2021-01-04')
    start_idx        = np.searchsorted(data_clean.index, start_bt_date)
    rebalance_indices = range(start_idx, len(data_clean), rebalance_days)

    print(f"\n--- Memulai Backtest UNTUK WINDOW PERTAMA SAJA ---")
    
    curr_idx = rebalance_indices[0]
    curr_date = data_clean.index[curr_idx]
    train_start = max(0, curr_idx - lookback_days)
    train_data = data_clean.iloc[train_start:curr_idx]
    next_idx = rebalance_indices[1] if len(rebalance_indices) > 1 else len(data_clean)
    
    print(f"Training Window: {data_clean.index[train_start].date()} -> {curr_date.date()}")
    print(f"Testing Window:  {curr_date.date()} -> {data_clean.index[next_idx-1].date()}")

    # --- Optimasi VQE ---
    selected_indices, depth_used, energy_final, debug_data = run_strategy_step(
        train_data, tickers, K=K, penalty_A=penalty_A,
        max_depth=max_depth, maxiter=maxiter
    )
    selected_names = [tickers[idx] for idx in selected_indices]
    print(f"[{curr_date.date()}] VQE Terpilih: {selected_names} | Depth: {depth_used} | E_min: {energy_final:.6f}")

    # =========================================================================
    # EXTRACTION OF DEBUG DATA TO CSV & PLOTS
    # =========================================================================
    # 1. Save mu and mu_tilde
    df_mu = pd.DataFrame({'Asset': tickers, 'mu': debug_data['mu'], 'mu_tilde': debug_data['mu_tilde']})
    df_mu.to_csv('window_1_mu.csv', index=False)
    print("Disimpan: window_1_mu.csv")

    # 2. Save sigma
    df_sigma = pd.DataFrame(debug_data['sigma'], index=tickers, columns=tickers)
    df_sigma.to_csv('window_1_sigma.csv')
    print("Disimpan: window_1_sigma.csv")

    # 3. Save sigma_tilde
    df_sigmat = pd.DataFrame(debug_data['sigma_tilde'], index=tickers, columns=tickers)
    df_sigmat.to_csv('window_1_sigma_tilde.csv')
    print("Disimpan: window_1_sigma_tilde.csv")

    # 4. Save & Plot Nash Equilibrium Energies
    ne_series = pd.Series(debug_data['all_ne_energies'])
    ne_series.to_csv('window_1_nash_equilibrium.csv', header=['Energy'])
    
    plt.figure(figsize=(8, 5))
    ne_series.sort_values().plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title("Nash Equilibrium Energies for Feasible Bitstrings")
    plt.ylabel("Classical Ising Energy")
    plt.xlabel("Portfolio Bitstring (N=4, K=2)")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('window_1_nash_equilibrium.png', dpi=150)
    plt.close()
    print("Disimpan: window_1_nash_equilibrium.png")

    # 5. Save & Plot SPSA Iteration History
    spsa_series = pd.Series(debug_data['spsa_history'], name='Energy')
    spsa_series.index.name = 'Batch_Iteration'
    spsa_series.to_csv('window_1_spsa_history.csv')
    
    plt.figure(figsize=(8, 5))
    plt.plot(spsa_series.index, spsa_series.values, color='purple', linewidth=2)
    plt.title(f"VQE SPSA Convergence (Depth={depth_used})")
    plt.ylabel("Energy")
    plt.xlabel("Batch Iteration")
    plt.grid(linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('window_1_spsa_history.png', dpi=150)
    plt.close()
    print("Disimpan: window_1_spsa_history.png")

    # 6. Save & Plot Energies per Depth
    depth_series = pd.Series(debug_data['energies_per_depth'], name='Energy')
    depth_series.index.name = 'Depth'
    depth_series.to_csv('window_1_depth_energies.csv')
    
    plt.figure(figsize=(8, 5))
    plt.plot(depth_series.index, depth_series.values, marker='o', color='green', linewidth=2, markersize=8)
    plt.title("VQE Minimum Energy vs. Ansatz Depth")
    plt.ylabel("Converged Energy")
    plt.xlabel("Layer Depth")
    plt.xticks(depth_series.index)
    plt.grid(linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('window_1_depth_energies.png', dpi=150)
    plt.close()
    print("Disimpan: window_1_depth_energies.png")

    # =========================================================================
    # CORE STRATEGY PLOT
    # =========================================================================
    target_w_vqe = np.zeros(N)
    if len(selected_indices) > 0:
        w = 1.0 / len(selected_indices)
        for idx in selected_indices:
            target_w_vqe[idx] = w

    target_w_bench = np.full(N, 1.0 / N)
    current_prices = data_clean.iloc[curr_idx].values

    cash_vqe, holdings_vqe = rebalance_portfolio(initial_capital, np.zeros(N), target_w_vqe, current_prices)
    cash_bench, holdings_bench = rebalance_portfolio(initial_capital, np.zeros(N), target_w_bench, current_prices)
    
    cash_assets = {t: initial_capital for t in tickers}
    holdings_assets = {t: 0.0 for t in tickers}
    for j, t in enumerate(tickers):
        tw = np.zeros(N); tw[j] = 1.0
        c, h = rebalance_portfolio(initial_capital, np.zeros(N), tw, current_prices)
        cash_assets[t], holdings_assets[t] = c, h[j]

    dates_window = data_clean.index[curr_idx:next_idx]
    records = []
    
    for d in range(curr_idx, next_idx):
        prices = data_clean.iloc[d].values
        val_vqe = cash_vqe + np.sum(holdings_vqe * prices)
        val_bench = cash_bench + np.sum(holdings_bench * prices)
        
        row = {'Date': data_clean.index[d], 'VQE': val_vqe, 'Benchmark': val_bench}
        for j, t in enumerate(tickers):
            row[t] = cash_assets[t] + holdings_assets[t] * prices[j]
        records.append(row)

    df_results = pd.DataFrame(records).set_index('Date')

    plt.figure(figsize=(10, 6))
    plt.plot(df_results.index, df_results['VQE'], label=f'Quantum Exact Potential Game VQE (K={K})', linewidth=2.5, color='blue')
    plt.plot(df_results.index, df_results['Benchmark'], label='Buy & Hold Benchmark (Equal Weight)', linewidth=2.5, color='black', linestyle='--')
    
    colors = ['red', 'green', 'orange', 'purple']
    for j, t in enumerate(tickers):
        plt.plot(df_results.index, df_results[t], label=f'Buy & Hold {t}', color=colors[j], alpha=0.6)

    plt.title(f'Kinerja Portofolio Kuantum - Window Pertama\n({dates_window[0].date()} hingga {dates_window[-1].date()})')
    plt.ylabel('Ekuitas Portofolio (Rupiah)')
    plt.xlabel('Tanggal')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.savefig('window_1_result.png', dpi=150)
    plt.close()
