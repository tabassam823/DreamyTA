import yfinance as yf

def load_data(tickers, start_date, end_date):
    """Mengunduh data observasi dari yfinance."""
    data = yf.download(tickers, start=start_date, end=end_date, progress=False)['Close']
    data = data.dropna()
    return data.sort_index()
