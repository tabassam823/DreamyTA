# =============================================================================
# config.py — Konfigurasi Global Pipeline GT-Ising-VQE
# =============================================================================
# Parameter sistem untuk optimasi portofolio menggunakan
# Game Theory + Classical Mutual Information + VQE.

# --- Aset & Portofolio ---
TICKERS = ['DUK', 'MSFT', 'CVX', 'TSLA']
N = len(TICKERS)
K = 2                       # Target kardinalitas portofolio

# --- Data Historis ---
DATA_START = "2023-01-01"
DATA_END   = "2024-01-01"

# --- Parameter Risiko & Penalti ---
LAMBDA_PENALTY = 5.0        # Pengali Lagrange untuk kendala kardinalitas

# --- VQE / SPSA Parameters ---
MAX_DEPTH      = 4          # Kedalaman maksimum ansatz EfficientSU2
MAXITER        = 100        # Iterasi SPSA minimum sebelum cek konvergensi
MAX_TOTAL_ITER = 2000       # Batas atas total iterasi SPSA per depth
BATCH_SIZE     = 25         # Ukuran batch SPSA
CONV_WINDOW    = 4          # Jumlah batch untuk deteksi konvergensi
CONV_TOL       = 1e-4       # Toleransi relative change untuk konvergensi
SEED           = 42         # Random seed untuk reprodusibilitas

# --- Output ---
OUTPUT_DIR = "output"       # Direktori untuk CSV dan grafik
