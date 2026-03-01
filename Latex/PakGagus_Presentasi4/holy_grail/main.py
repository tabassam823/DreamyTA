import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
import os

from config import *
from data_loader import load_data
from strategy import run_strategy_step
from backtest import perform_backtest

warnings.filterwarnings('ignore')

def main():
    print("Starting Setup untuk Backtesting (2021-2023)...")
    
    data_clean = load_data(tickers, start_date, end_date)
    print(f"Data Berhasil Diunduh. Total hari observasi: {len(data_clean)}")
    
    start_bt_date = pd.to_datetime('2021-01-04')
    start_idx = np.searchsorted(data_clean.index, start_bt_date)
    
    print(f"\\n--- Memulai Backtest dari {data_clean.index[start_idx].date()} hingga {data_clean.index[-1].date()} ---")
    
    strategy_kwargs = {
        'K': K,
        'penalty_A': penalty_A,
        'depth': depth,
        'maxiter': maxiter
    }

    value_vqe, value_bench, value_assets = perform_backtest(
        data_clean=data_clean,
        tickers=tickers,
        start_idx=start_idx,
        rebalance_days=rebalance_days,
        lookback_days=lookback_days,
        K=K,
        initial_capital=initial_capital,
        run_strategy_step_fn=run_strategy_step,
        strategy_kwargs=strategy_kwargs
    )
    
    print("Backtesting Selesai.")
    
    plt.figure(figsize=(14, 7))
    plt.plot(data_clean.index[:len(value_vqe)], value_vqe, label='QBGT VQE SPSA (Rebalance K=2)', linewidth=2.5, color='blue')
    plt.plot(data_clean.index[:len(value_bench)], value_bench, label='Buy & Hold Benchmark (Equal 4 Aset)', linewidth=2.5, color='black', linestyle='--')
    
    colors = ['red', 'green', 'orange', 'purple']
    for j, t in enumerate(tickers):
        plt.plot(data_clean.index[:len(value_assets[t])], value_assets[t], label=f'Buy & Hold {t}', color=colors[j], alpha=0.6)

    plt.title('Simulasi Backtesting Kinerja Portofolio Ekonomi Kuantum (2021-2023)')
    plt.ylabel('Ekuitas Portofolio (Rupiah)')
    plt.xlabel('Tanggal')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend(loc='upper left')
    plt.tight_layout()
    
    # Save the output image
    plot_path = os.path.join(os.path.dirname(__file__), 'backtest_result.png')
    plt.savefig(plot_path)
    print(f"Plot visualisasi disimpan di: {plot_path}")

if __name__ == "__main__":
    main()
