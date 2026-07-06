# data_loader.py
import yfinance as yf

def download_data(tickers, start_date, end_date):
    """Download daily close data for tickers."""
    data = yf.download(tickers, start=start_date, end=end_date, progress=False)['Close']
    data = data.dropna()
    data_clean = data.sort_index()
    print(f"Data Berhasil Diunduh. Total hari observasi: {len(data_clean)}")
    return data_clean
