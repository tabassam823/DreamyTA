# config.py
# =============================================================================
# Konfigurasi
# =============================================================================
tickers = ['DUK', 'MSFT', 'CVX', 'TSLA']
N       = len(tickers)       # Jumlah aset kandidat
K       = 2                  # Jumlah aset target portofolio
penalty_A = 5.0              # Pengali Lagrange (A) untuk H_penalty
max_depth = 4                # Kedalaman maksimum ansatz (adaptive)
maxiter   = 100              # Iterasi SPSA per depth-level

# Parameter Kalender
initial_capital = 100_000_000.0
lookback_days  = 63   # ~3 bulan perdagangan
rebalance_days = 21   # ~1 bulan perdagangan

start_date = "2020-09-01"
end_date = "2024-01-01"
start_bt_date = '2021-01-04'
