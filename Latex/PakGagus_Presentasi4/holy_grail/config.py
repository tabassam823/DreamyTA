# 1. Konfigurasi
tickers = ['BBCA.JK', 'ASII.JK', 'TLKM.JK', 'TPIA.JK']
K = 2
penalty_A = 5.0
depth = 1  # Kedalaman Ansatz EfficientSU2
maxiter = 100 # Iterasi SPSA

# Parameter Kalender
initial_capital = 100_000_000.0
lookback_days = 63 
rebalance_days = 21 
start_date = "2020-09-01"
end_date = "2024-01-01"
