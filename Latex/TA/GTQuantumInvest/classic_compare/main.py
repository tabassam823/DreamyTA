import os
import sys
import pandas as pd
import numpy as np
import warnings

# Tambahkan parent directory ke sys.path untuk import modul existing
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_downloader import download_market_data
from config import get_config
from markowitz_optimizer import solve_markowitz
from calc_simple_return import calculate_simple_return
from calc_log_return import calculate_log_return
from calc_expected_returns import calculate_expected_simple_return, calculate_expected_log_return_with_drag
from compute_endogenous_lambda import compute_endogenous_lambda
from rebalance_portfolio import rebalance_portfolio

warnings.filterwarnings('ignore')

def run_classic_backtest(n_assets):
    # 1. Ambil Tickers secara dinamis dari file main_NX.py yang bersangkutan
    # agar sinkronisasi aset 100% akurat
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location("main_module", f"../main_N{n_assets}.py")
        main_mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(main_mod)
        tickers = main_mod.tickers
        print(f"Menggunakan Tickers dari main_N{n_assets}.py: {tickers}")
    except Exception as e:
        print(f"Peringatan: Gagal mengambil tickers dari main_N{n_assets}.py ({e})")
        # Fallback ke daftar blue chip aman
        all_tickers = ['BBCA.JK', 'TLKM.JK', 'SMGR.JK', 'BMRI.JK', 'KLBF.JK', 'ASII.JK', 
                       'UNTR.JK', 'ICBP.JK', 'AMRT.JK', 'ADRO.JK', 'TPIA.JK', 'BBRI.JK']
        tickers = all_tickers[:n_assets]
        print(f"Menggunakan Fallback Tickers: {tickers}")

    config = get_config(tickers)
    
    K = config['K']
    lookback_days = config['lookback_days']
    rebalance_days = config['rebalance_days']
    initial_capital = config['initial_capital']
    start_bt_date = pd.to_datetime(config['start_bt_date'])

    # 2. Download Data
    data_clean, benchmark_data, benchmark_rets = download_market_data(
        config['tickers'], config['benchmark_ticker'], 
        config['start_date'], config['end_date'], config['start_bt_date']
    )

    start_idx = np.searchsorted(data_clean.index, start_bt_date)
    rebalance_indices = range(start_idx, len(data_clean), rebalance_days)

    value_classic = [initial_capital] * start_idx
    holdings_classic = np.zeros(n_assets)
    cash_classic = initial_capital
    
    results_log = []

    print(f"\n--- Memulai Classic Markowitz Backtest (N={n_assets}) ---")

    for i, curr_idx in enumerate(rebalance_indices):
        curr_date = data_clean.index[curr_idx]
        train_start = max(0, curr_idx - lookback_days)
        train_data = data_clean.iloc[train_start:curr_idx]
        next_idx = (rebalance_indices[i + 1] if i + 1 < len(rebalance_indices) else len(data_clean))

        # --- HITUNG METRIK (Sama dengan Quantum) ---
        simple_rets = calculate_simple_return(train_data)
        log_rets = calculate_log_return(train_data)
        
        mu_R_daily = calculate_expected_simple_return(simple_rets)
        var_r_daily = log_rets.var() 
        mu_r_daily = calculate_expected_log_return_with_drag(mu_R_daily, var_r_daily)

        mu_simple_period = mu_R_daily.values * 126
        sigma_log = log_rets.std().values
        sigma_period_log = sigma_log * np.sqrt(126)
        sigma_period_matrix = log_rets.cov().values * 126

        gamma = compute_endogenous_lambda(mu_r_daily.values * 126, sigma_period_log)

        # --- OPTIMASI CLASSIC ---
        selected_indices, weights = solve_markowitz(mu_simple_period, sigma_period_matrix, gamma, K)
        selected_names = [tickers[idx] for idx in selected_indices]
        
        print(f"[{curr_date.date()}] Classic Terpilih: {selected_names}")

        # Rebalancing (Equal weight di antara K terpilih untuk pembanding fair)
        target_w = np.zeros(n_assets)
        for idx in selected_indices: target_w[idx] = 1.0 / K
        
        current_prices = data_clean.iloc[curr_idx].values
        cash_classic, holdings_classic = rebalance_portfolio(cash_classic, holdings_classic, target_w, current_prices, n_assets)

        for d in range(curr_idx, next_idx):
            prices = data_clean.iloc[d].values
            value_classic.append(cash_classic + np.sum(holdings_classic * prices))
            
        results_log.append({
            'Date': curr_date.date(),
            'Selected': selected_names,
            'Equity': value_classic[-1]
        })

    # Simpan hasil
    output_dir = f"Hasil_Classic_Compare"
    if not os.path.exists(output_dir): os.makedirs(output_dir)
    
    df_res = pd.DataFrame(results_log)
    df_res.to_csv(f"{output_dir}/hasil_classic_N{n_assets}.csv", index=False)
    
    # Simpan seluruh history equity untuk plotting gabungan nantinya
    equity_df = pd.DataFrame({'Date': data_clean.index[:len(value_classic)], 'Equity': value_classic})
    equity_df.to_csv(f"{output_dir}/equity_history_classic_N{n_assets}.csv", index=False)

    print(f"Selesai N={n_assets}. Hasil disimpan di {output_dir}/")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
        run_classic_backtest(n)
    else:
        for n in [2, 4, 6, 8, 10, 12]:
            run_classic_backtest(n)
