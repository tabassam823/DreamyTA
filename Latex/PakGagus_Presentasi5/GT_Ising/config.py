# =============================================================================
# Konfigurasi GT-Ising-VQE
# =============================================================================
tickers = ['DUK', 'MSFT', 'CVX', 'TSLA']
N       = len(tickers)       # Jumlah aset kandidat
K       = 2                  # Jumlah aset target portofolio
penalty_A = 5.0              # Pengali Lagrange (A) untuk H_penalty (lambda)
max_depth = 4                # Kedalaman maksimum ansatz (adaptive)
maxiter   = 100              # Iterasi SPSA per depth-level

# Parameter Kalender
initial_capital = 100_000_000.0
lookback_days  = 126   # ~6 bulan perdagangan
rebalance_days = 21   # ~1 bulan perdagangan
