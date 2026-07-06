import numpy as np
import pandas as pd
from run_strategy_step import run_strategy_step
from rebalance_portfolio import rebalance_portfolio

def run_backtest(data_clean, tickers, config):
    """
    Menjalankan simulasi backtest berdasarkan data historis dan konfigurasi.
    """
    N = len(tickers)
    K = config['K']
    penalty_A = config['penalty_A']
    max_depth = config['max_depth']
    maxiter = config['maxiter']
    max_total_iter = config.get('max_total_iter', 500)
    batch_size = config.get('batch_size', 10)
    conv_window = config.get('conv_window', 4)
    conv_tol = config.get('conv_tol', 1e-3)
    use_warm_start = config.get('use_warm_start', True)
    initial_capital = config['initial_capital']
    lookback_days = config['lookback_days']
    rebalance_days = config['rebalance_days']
    start_bt_date = pd.to_datetime(config['start_bt_date'])

    start_idx = np.searchsorted(data_clean.index, start_bt_date)
    rebalance_indices = range(start_idx, len(data_clean), rebalance_days)

    value_vqe = [initial_capital] * start_idx
    value_bench = [initial_capital] * start_idx
    value_nash = [initial_capital] * start_idx
    value_assets = {t: [initial_capital] * start_idx for t in tickers}

    holdings_vqe, holdings_bench, holdings_nash = np.zeros(N), np.zeros(N), np.zeros(N)
    cash_vqe, cash_bench, cash_nash = initial_capital, initial_capital, initial_capital
    cash_assets = {t: initial_capital for t in tickers}
    holdings_assets = {t: 0.0 for t in tickers}

    detail_logs = []
    depths_history = []
    rebalance_dates = []
    window_analysis_history = [] # Menyimpan semua data untuk plotting per window

    print(f"\n--- Memulai Backtest dari {data_clean.index[start_idx].date()} hingga {data_clean.index[-1].date()} ---")

    for i, curr_idx in enumerate(rebalance_indices):
        curr_date = data_clean.index[curr_idx]
        train_start = max(0, curr_idx - lookback_days)
        train_data = data_clean.iloc[train_start:curr_idx]
        next_idx = (rebalance_indices[i + 1] if i + 1 < len(rebalance_indices) else len(data_clean))

        # Strategi Step
        selected_indices, depth_used, energy_final, best_history, best_ent_hist, best_gvar_hist, depth_energies, lr_data, ne_bs, ne_utility, winning_probs, best_params = run_strategy_step(
            train_data, tickers, curr_date, K=K, penalty_A=penalty_A, max_depth=max_depth, maxiter=maxiter,
            max_total_iter=max_total_iter, batch_size=batch_size,
            conv_window=conv_window, conv_tol=conv_tol,
            use_warm_start=use_warm_start,
            file_config=config.get('files')
        )
        
        depths_history.append(depth_used)
        rebalance_dates.append(curr_date.date())
        
        # Simpan semua detail untuk plotting nanti
        window_analysis_history.append({
            'date': curr_date.date(),
            'best_history': best_history,
            'best_ent_hist': best_ent_hist,
            'best_gvar_hist': best_gvar_hist,
            'depth_energies': depth_energies,
            'lr_data': lr_data,
            'winning_probs': winning_probs,
            'ne_bs': ne_bs,
            'best_params': best_params,
            'best_depth': depth_used,
            'K': K,
            'use_warm_start': use_warm_start
        })
        
        selected_names = [tickers[idx] for idx in selected_indices]
        vqe_details = "".join([f"    [Depth {d}] Konvergen dalam {iters} iterasi | E = {en:.6f}\n" for d, en, iters in depth_energies])
        
        print(f"[{curr_date.date()}] VQE Terpilih: {selected_names} | Depth: {depth_used} | E_min: {energy_final:.6f}")

        log_entry = (f"[{curr_date.date()}]\n"
                     f"  - Nash Eq: {ne_bs} | Utility: {ne_utility:.6f}\n"
                     f"  - LR: {lr_data[2]:.4f}\n"
                     f"  - Detail:\n{vqe_details}"
                     f"  - Terpilih: {selected_names} | Depth: {depth_used} | E_min: {energy_final:.6f}\n" + "-"*40)
        detail_logs.append(log_entry)

        # Rebalancing VQE
        target_w_vqe = np.zeros(N)
        if len(selected_indices) > 0:
            w = 1.0 / len(selected_indices)
            for idx in selected_indices: target_w_vqe[idx] = w

        # Rebalancing Nash
        target_w_nash = np.zeros(N)
        nash_indices = [j for j, bit in enumerate(ne_bs) if bit == '1']
        if len(nash_indices) > 0:
            w_n = 1.0 / len(nash_indices)
            for idx in nash_indices: target_w_nash[idx] = w_n

        target_w_bench = np.full(N, 1.0 / N)
        current_prices = data_clean.iloc[curr_idx].values

        cash_vqe, holdings_vqe = rebalance_portfolio(cash_vqe, holdings_vqe, target_w_vqe, current_prices, N)
        cash_nash, holdings_nash = rebalance_portfolio(cash_nash, holdings_nash, target_w_nash, current_prices, N)

        if i == 0:
            cash_bench, holdings_bench = rebalance_portfolio(cash_bench, holdings_bench, target_w_bench, current_prices, N)
            for j, t in enumerate(tickers):
                target_w_indiv = np.zeros(N)
                target_w_indiv[j] = 1.0
                c_t, h_t = rebalance_portfolio(cash_assets[t], np.zeros(N), target_w_indiv, current_prices, N)
                cash_assets[t], holdings_assets[t] = c_t, h_t[j]

        for d in range(curr_idx, next_idx):
            prices = data_clean.iloc[d].values
            value_vqe.append(cash_vqe + np.sum(holdings_vqe * prices))
            value_nash.append(cash_nash + np.sum(holdings_nash * prices))
            value_bench.append(cash_bench + np.sum(holdings_bench * prices))
            for j, t in enumerate(tickers):
                value_assets[t].append(cash_assets[t] + holdings_assets[t] * prices[j])

    # --- EKSPOR HASIL EKUITAS KE CSV (Untuk Perbandingan) ---
    suffix = f"_N{N}"
    equity_df = pd.DataFrame({
        'Date': data_clean.index[:len(value_vqe)],
        'VQE': value_vqe,
        'Nash': value_nash,
        'Benchmark': value_bench
    })
    # Gunakan folder files config jika ada, atau default suffix
    equity_csv_path = config.get('files', {}).get('equity_history', f'hasil_ekuitas_backtest{suffix}.csv')
    equity_df.to_csv(equity_csv_path, index=False)

    return {
        'value_vqe': value_vqe,
        'value_nash': value_nash,
        'value_bench': value_bench,
        'value_assets': value_assets,
        'depths_history': depths_history,
        'rebalance_dates': rebalance_dates,
        'detail_logs': detail_logs,
        'window_analysis_history': window_analysis_history,
        'start_idx': start_idx
    }
