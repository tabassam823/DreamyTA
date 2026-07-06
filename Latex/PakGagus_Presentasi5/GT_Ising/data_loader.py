import yfinance as yf

def download_data(tickers, start_date="2020-09-01", end_date="2024-01-01"):
    print("Mendownload data historis...")
    data = yf.download(tickers, start=start_date, end=end_date, progress=False)['Close']
    data = data.dropna()
    data_clean = data.sort_index()
    print(f"Data Berhasil Diunduh. Total hari observasi: {len(data_clean)}")
    return data_clean
