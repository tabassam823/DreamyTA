import yfinance as yf
import pandas as pd

def download_market_data(tickers, benchmark_ticker, start_date, end_date, start_bt_date):
    """
    Mengunduh data saham dan benchmark, melakukan pembersihan dasar,
    dan mengekspor data harga harian.
    """
    print("Mengunduh data saham...")
    data = yf.download(tickers, start=start_date, end=end_date, progress=False)['Close']
    data = data.dropna()
    data_clean = data.sort_index()

    print(f"Mengunduh data indeks pembanding ({benchmark_ticker})...")
    # Mengunduh benchmark mulai dari tanggal backtest agar rets bisa dihitung dengan benar
    benchmark_data = yf.download(benchmark_ticker, start=start_bt_date, end=end_date, progress=False)['Close']
    benchmark_data = benchmark_data.dropna()
    benchmark_rets = benchmark_data.pct_change().dropna()

    print(f"Data Berhasil Diunduh. Total hari observasi: {len(data_clean)}")
    
    return data_clean, benchmark_data, benchmark_rets
