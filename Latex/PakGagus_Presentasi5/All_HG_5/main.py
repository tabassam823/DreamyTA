# main.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings

from config import *
from data_loader import download_data
from strategy import run_strategy_step
from metrics import compute_metrics

warnings.filterwarnings('ignore')

def rebalance_portfolio(current_cash, current_holdings, target_weights, prices, N):
    """Eksekusi rebalancing portofolio tanpa biaya transaksi."""
    total_value    = current_cash + np.sum(current_holdings * prices)
    target_values  = total_value * target_weights
    new_holdings   = current_holdings.copy()
    new_cash       = current_cash

    # Jual aset berlebih terlebih dahulu
    for j in range(N):
        c_val = new_holdings[j] * prices[j]
        if c_val > target_values[j]:
            sell_val        = c_val - target_values[j]
            new_cash       += sell_val
            new_holdings[j] -= sell_val / prices[j]

    # Kemudian beli aset yang kurang
    for j in range(N):
        c_val = new_holdings[j] * prices[j]
        if c_val < target_values[j]:
            buy_val       = min(target_values[j] - c_val, new_cash)
            new_cash     -= buy_val
            new_holdings[j] += buy_val / prices[j]

    return new_cash, new_holdings

def main():
    print("Starting Setup for Backtesting (2021-2023)...")

    data_clean = download_data(tickers, start_date, end_date)
    
    start_bt_dt       = pd.to_datetime(start_bt_date)
    start_idx         = np.searchsorted(data_clean.index, start_bt_dt)
    rebalance_indices = range(start_idx, len(data_clean), rebalance_days)

    # Tracking Array
    value_vqe   = [initial_capital] * start_idx
    value_bench = [initial_capital] * start_idx
    value_assets = {t: [initial_capital] * start_idx for t in tickers}

    holdings_vqe, holdings_bench = np.zeros(N), np.zeros(N)
    cash_vqe, cash_bench = initial_capital, initial_capital
    cash_assets    = {t: initial_capital for t in tickers}
    holdings_assets = {t: 0.0 for t in tickers}

    print(f"\n--- Memulai Backtest dari {data_clean.index[start_idx].date()} "
          f"hingga {data_clean.index[-1].date()} ---")

    for i, curr_idx in enumerate(rebalance_indices):
        curr_date      = data_clean.index[curr_idx]
        train_start    = max(0, curr_idx - lookback_days)
        train_data     = data_clean.iloc[train_start:curr_idx]

        next_idx = (rebalance_indices[i + 1]
                    if i + 1 < len(rebalance_indices)
                    else len(data_clean))

        # --- Alokasi VQE ---
        selected_indices, depth_used, energy_final = run_strategy_step(
            train_data, tickers, K=K, penalty_A=penalty_A,
            max_depth=max_depth, maxiter=maxiter
        )
        selected_names = [tickers[idx] for idx in selected_indices]
        print(f"[{curr_date.date()}] VQE Terpilih: {selected_names} "
              f"| Depth: {depth_used} | E_min: {energy_final:.6f}")

        target_w_vqe = np.zeros(N)
        if len(selected_indices) > 0:
            w = 1.0 / len(selected_indices)
            for idx in selected_indices:
                target_w_vqe[idx] = w

        # --- Benchmark: Buy & Hold Equal Weight ---
        target_w_bench = np.full(N, 1.0 / N)

        current_prices = data_clean.iloc[curr_idx].values

        # Rebalance VQE (setiap bulan)
        cash_vqe, holdings_vqe = rebalance_portfolio(
            cash_vqe, holdings_vqe, target_w_vqe, current_prices, N
        )

        # Benchmark & Single Asset: hanya di awal periode
        if i == 0:
            cash_bench, holdings_bench = rebalance_portfolio(
                cash_bench, holdings_bench, target_w_bench, current_prices, N
            )
            for j, t in enumerate(tickers):
                target_w_indiv = np.zeros(N)
                target_w_indiv[j] = 1.0
                c_t, h_t = rebalance_portfolio(
                    cash_assets[t], np.zeros(N), target_w_indiv, current_prices, N
                )
                cash_assets[t]    = c_t
                holdings_assets[t] = h_t[j]

        # --- Mark to Market ---
        start_d = curr_idx if i == 0 else curr_idx + 1
        for d in range(start_d, next_idx):
            prices = data_clean.iloc[d].values
            value_vqe.append(cash_vqe + np.sum(holdings_vqe * prices))
            value_bench.append(cash_bench + np.sum(holdings_bench * prices))
            for j, t in enumerate(tickers):
                value_assets[t].append(cash_assets[t] + holdings_assets[t] * prices[j])

    print("\nBacktesting Selesai.")

    # =============================================================================
    # Evaluasi Metrik Kinerja
    # =============================================================================
    tr_vqe,   sr_vqe,   mdd_vqe   = compute_metrics(value_vqe,   initial_capital, "QBGT VQE (Adaptive Layers)")
    tr_bench, sr_bench, mdd_bench = compute_metrics(value_bench, initial_capital, "Buy & Hold Equal Weight")
    for t in tickers:
        compute_metrics(value_assets[t], initial_capital, f"Buy & Hold {t}")

    # =============================================================================
    # Visualisasi Pertumbuhan Portofolio
    # =============================================================================
    plt.figure(figsize=(14, 7))

    dates = data_clean.index

    plt.plot(dates[:len(value_vqe)],   value_vqe,
             label=f'QBGT VQE SPSA Adaptive (K={K})',
             linewidth=2.5, color='blue')

    plt.plot(dates[:len(value_bench)], value_bench,
             label='Buy & Hold Benchmark (Equal Weight)',
             linewidth=2.5, color='black', linestyle='--')

    colors = ['red', 'green', 'orange', 'purple']
    for j, t in enumerate(tickers):
        plt.plot(dates[:len(value_assets[t])], value_assets[t],
                 label=f'Buy & Hold {t}', color=colors[j], alpha=0.6)

    plt.title(
        'Simulasi Backtesting Kinerja Portofolio Ekonomi Kuantum (2021–2023)\n'
        'Metodologi: Game Theory + QMI Hamiltonian + VQE Adaptive Layers'
    )
    plt.ylabel('Ekuitas Portofolio (Rupiah)')
    plt.xlabel('Tanggal')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.savefig('backtest_result.png', dpi=150)
    plt.show()
    print("\nGrafik disimpan sebagai backtest_result.png")

if __name__ == "__main__":
    main()
