import warnings
import pandas as pd

# Import modul inti
from data_downloader import download_market_data
from backtest_runner import run_backtest
from report_generator import generate_report
from plot_generator import plot_all

# Import konfigurasi terpusat
from config import get_config, clean_workspace

warnings.filterwarnings('ignore')

# 1. Tentukan Aset (Tickers)
tickers = ['BBCA.JK', 'ADRO.JK']
N = len(tickers)

# 0. Bersihkan Workspace
clean_workspace(N)

# 2. Ambil Konfigurasi
config = get_config(tickers)

suffix = f"_N{N}"
filenames = {
    'daily_prices_csv': f'harga_harian_saham{suffix}.csv',
    'report_txt': f'laporan_backtest{suffix}.txt',
    'circuit_png': f'rangkaian_kuantum{suffix}.png',
    'convergence_png': f'grafik_konvergensi_detail{suffix}.png',
    'backtest_vqe_png': f'hasil_backtest_vqe{suffix}.png',
    'backtest_nash_png': f'hasil_backtest_nash{suffix}.png',
    'depth_png': f'grafik_depth_per_window{suffix}.png'
}

# 3. Eksekusi Pipeline
data_clean, benchmark_data, benchmark_rets = download_market_data(
    config['tickers'], config['benchmark_ticker'], 
    config['start_date'], config['end_date'], config['start_bt_date']
)
data_clean.to_csv(filenames['daily_prices_csv'])
print(f"Data harga harian telah diekspor ke '{filenames['daily_prices_csv']}'.")

results = run_backtest(data_clean, config['tickers'], config)

value_benchmark_idx = generate_report(
    results, data_clean, benchmark_data, benchmark_rets, 
    config['tickers'], config, filenames['report_txt']
)

plot_all(results, data_clean, value_benchmark_idx, config, filenames)

print(f"\nSeluruh proses N={N} selesai.")
