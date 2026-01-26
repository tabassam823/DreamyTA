import yfinance as yf
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def prepare_data():
    # Define assets as specified in the paper (N=12)
    us_equities = ["AAPL", "MSFT", "GOOGL", "AMZN", "NVDA", "JPM"]
    china_a_shares = [
        "600519.SS", "601398.SS", "600036.SS", 
        "601857.SS", "600276.SS", "601318.SS"
    ]
    assets = us_equities + china_a_shares
    
    # Timeframe: Jan 1, 2024 to Dec 31, 2024
    start_date = "2024-01-01"
    end_date = "2024-12-31"
    
    print(f"Fetching data for {len(assets)} assets from {start_date} to {end_date}...")
    
    # Download data
    data_raw = yf.download(assets, start=start_date, end=end_date)
    
    if 'Adj Close' in data_raw.columns.levels[0]:
        data = data_raw['Adj Close']
    else:
        data = data_raw['Close']
    
    # Reorder columns to match the defined assets list order
    data = data[assets]
    
    # Calculate daily returns (Eq 1: percentage change)
    # r_ki = (P_ki - P_k-1,i) / P_k-1,i
    returns = data.pct_change()
    
    # Handle missing data: Drop NaNs (first row will always be NaN)
    # and any days where data might be missing for some assets due to different market holidays
    returns = returns.dropna()
    
    # Calculate Expected Return Vector (mu) - Eq 2
    mu = returns.mean().values
    
    # Calculate Covariance Matrix (sigma) - Eq 3
    # Note: numpy.cov expects variables in rows, so we transpose
    sigma = returns.cov().values
    
    # Output results in copy-pasteable format
    print("\n" + "="*50)
    print("EXPECTED RETURN VECTOR (mu)")
    print("="*50)
    print(repr(mu))
    
    print("\n" + "="*50)
    print("COVARIANCE MATRIX (sigma)")
    print("="*50)
    # Using numpy array2string for better formatting if needed, but repr is good for copy-paste
    print(repr(sigma))
    
    # Verification: Assets List
    print("\n" + "="*50)
    print("ASSETS ORDER")
    print("="*50)
    print(assets)

    # Visualization of Correlation Matrix
    correlation_matrix = returns.corr()
    plt.figure(figsize=(12, 10))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title("Asset Correlation Matrix (2024)")
    plt.tight_layout()
    plt.savefig("asset_correlation.png")
    print("\nCorrelation matrix saved to 'asset_correlation.png'")

if __name__ == "__main__":
    prepare_data()
