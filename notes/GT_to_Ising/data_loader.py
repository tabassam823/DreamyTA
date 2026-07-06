# =============================================================================
# data_loader.py — Pra-pemrosesan Data Finansial
# =============================================================================
# Modul ini menangani:
#   1. Download data historis harga aset dari yfinance
#   2. Perhitungan log returns harian
#   3. Binarisasi state {u, d} berdasarkan threshold nol
#   4. Perhitungan parameter risk-aversion gamma endogen (sigmoid)

import yfinance as yf
import numpy as np
import pandas as pd
import warnings

warnings.filterwarnings('ignore')


def download_data(tickers, start, end):
    """
    Mengunduh data historis harga penutupan (Close) dari yfinance.

    Parameters
    ----------
    tickers : list[str]
        Daftar simbol ticker aset.
    start : str
        Tanggal awal (format 'YYYY-MM-DD').
    end : str
        Tanggal akhir (format 'YYYY-MM-DD').

    Returns
    -------
    pd.DataFrame
        DataFrame harga penutupan harian, terurut berdasarkan tanggal.
    """
    data = yf.download(tickers, start=start, end=end, progress=False)['Close']
    data = data.dropna().sort_index()
    print(f"[Data Loader] Data berhasil diunduh: {len(data)} hari observasi, "
          f"{len(tickers)} aset.")
    return data


def compute_log_returns(prices):
    """
    Menghitung log returns harian:  R_{i,t} = ln(P_{i,t} / P_{i,t-1})

    Parameters
    ----------
    prices : pd.DataFrame
        Harga penutupan harian.

    Returns
    -------
    pd.DataFrame
        Log returns harian (baris pertama di-drop karena NaN).
    """
    log_rets = np.log(prices / prices.shift(1)).dropna()
    return log_rets


def binarize_states(log_returns):
    """
    Pemetaan imbal hasil ke state biner {u, d}:
        S_{i,t} = 0 (up)   jika R_{i,t} > 0
        S_{i,t} = 1 (down) jika R_{i,t} <= 0

    Sesuai Rencana §A.3 dan kombinasi_GT_to_Ising.md §4.1.

    Parameters
    ----------
    log_returns : pd.DataFrame
        Log returns harian.

    Returns
    -------
    pd.DataFrame
        Binary states (0 = up, 1 = down).
    """
    binary_st = (log_returns <= 0).astype(int)
    return binary_st


def compute_endogenous_gamma(log_returns, tickers):
    """
    Menghitung parameter risk-aversion gamma secara endogen melalui
    fungsi sigmoid berdasarkan rata-rata Sharpe Ratio lintas aset.

    Sesuai kombinasi_GT_to_Ising.md Eq. (2):
        gamma = 1 / (1 + exp(-(mu/sigma)))

    di mana mu dan sigma diannualisasi (×252 dan ×sqrt(252)).

    Parameters
    ----------
    log_returns : pd.DataFrame
        Log returns harian.
    tickers : list[str]
        Daftar ticker untuk subset kolom.

    Returns
    -------
    float
        Nilai gamma endogen dalam rentang (0, 1).
    """
    mu_annual    = log_returns[tickers].mean() * 252
    sigma_annual = log_returns[tickers].std() * np.sqrt(252)

    mu_avg    = abs(mu_annual).mean()
    sigma_avg = sigma_annual.mean()

    if np.isnan(mu_avg) or np.isnan(sigma_avg) or (mu_avg + sigma_avg) == 0:
        return 0.5

    Z = mu_avg / sigma_avg   # Sharpe Ratio agregat
    gamma = 1.0 / (1.0 + np.exp(-Z))

    print(f"[Data Loader] Gamma endogen = {gamma:.4f} "
          f"(Sharpe agregat Z = {Z:.4f})")
    return gamma


def compute_covariance_matrix(log_returns, tickers):
    """
    Menghitung matriks kovariansi standar dari log returns.

    Parameters
    ----------
    log_returns : pd.DataFrame
        Log returns harian.
    tickers : list[str]
        Daftar ticker.

    Returns
    -------
    np.ndarray
        Matriks kovariansi (N×N).
    """
    cov = log_returns[tickers].cov().values
    return cov
