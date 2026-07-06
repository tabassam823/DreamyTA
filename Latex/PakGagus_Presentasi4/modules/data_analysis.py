
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import os

def download_data(tickers, start_date, end_date):
    """Downloads historical data for given tickers."""
    print(f"Downloading data for: {tickers}...")
    data = yf.download(tickers, start=start_date, end=end_date, progress=False)['Close']
    data = data.dropna()
    return data

def calculate_log_returns(data):
    """Calculates log returns: R_t = ln(P_t / P_{t-1})."""
    log_returns = np.log(data / data.shift(1)).dropna()
    return log_returns

def calculate_statistics(log_returns):
    """Calculates mean, std dev, and % Up (binary state 0)."""
    binary_states = (log_returns <= 0).astype(int)
    stats = []
    
    for t in log_returns.columns:
        mu = log_returns[t].mean()
        sigma = log_returns[t].std()
        # In the notebook: |0> (Up) if R > 0, |1> (Down) if R <= 0
        # binary_states is 1 if R<=0 (Down), 0 if R>0 (Up)
        # So % Up is count of 0s / total
        up_pct = (binary_states[t] == 0).mean() * 100
        stats.append({
            "Ticker": t,
            "Mean (mu)": mu,
            "Std Dev (sigma)": sigma,
            "% Naik": up_pct
        })
    
    return pd.DataFrame(stats)

def generate_visualizations(data, stats_df, output_dir="generated_images"):
    """Generates and saves visualizations."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 1. Price History Plot
    plt.figure(figsize=(10, 6))
    for col in data.columns:
        plt.plot(data.index, data[col], label=col)
    plt.title("Historical Asset Prices")
    plt.xlabel("Date")
    plt.ylabel("Close Price (IDR)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/price_history.png")
    plt.close()

    # 2. Statistics Table Image
    fig, ax = plt.subplots(figsize=(8, 3))
    ax.axis('tight')
    ax.axis('off')
    table_data = stats_df.round(6).values
    column_labels = stats_df.columns
    table = ax.table(cellText=table_data, colLabels=column_labels, loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.2)
    plt.title("Asset Return Statistics")
    plt.savefig(f"{output_dir}/statistics_table.png", bbox_inches='tight')
    plt.close()
    
    print(f"Visualizations saved to {output_dir}")

if __name__ == "__main__":
    # Configuration from notebook
    TICKERS = ['BBCA.JK', 'ASII.JK', 'TLKM.JK', 'TPIA.JK']
    START_DATE = "2025-01-06"
    END_DATE = "2026-01-06"
    OUTPUT_DIR = "../generated_images" # Relative to modules/ dir if running from there, or adjust as needed. 
    # Better to use absolute path or handle relative path carefully.
    # Assuming execution from project root based on file creation path.
    OUTPUT_DIR = "generated_images"

    data = download_data(TICKERS, START_DATE, END_DATE)
    log_returns = calculate_log_returns(data)
    stats_df = calculate_statistics(log_returns)
    
    print("Statistics:")
    print(stats_df)
    
    generate_visualizations(data, stats_df, OUTPUT_DIR)
