import numpy as np
import pandas as pd
from scipy.optimize import minimize

def solve_markowitz(mu, sigma_matrix, gamma, K):
    """
    Menyelesaikan optimasi Markowitz Klasik (Mean-Variance)
    Minimasi: 0.5 * gamma * w^T * Sigma * w - mu^T * w
    Subject to: sum(w) = 1, w_i >= 0
    Dan kita batasi hanya K aset yang terpilih (Long-only, Equal-weight di antara K aset)
    atau optimasi bobot kontinu.
    
    Namun untuk perbandingan yang 'fair' dengan VQE (yang mencari bitstring),
    kita bisa melakukan optimasi kontinu lalu mengambil K aset teratas,
    atau menggunakan optimasi integer/kardinalitas jika memungkinkan.
    
    Di sini kita gunakan pendekatan: Optimasi bobot kontinu (Long-only, sum=1),
    lalu pilih K aset dengan bobot tertinggi untuk disamakan dengan output diskrit VQE.
    """
    n = len(mu)
    
    def objective(w):
        return 0.5 * gamma * np.dot(w.T, np.dot(sigma_matrix, w)) - np.dot(mu.T, w)
    
    constraints = ({'type': 'eq', 'fun': lambda w: np.sum(w) - 1.0})
    bounds = [(0, 1) for _ in range(n)]
    
    # Inisialisasi bobot (equal weight)
    init_w = np.ones(n) / n
    
    res = minimize(objective, init_w, method='SLSQP', bounds=bounds, constraints=constraints)
    
    if not res.success:
        # Jika gagal, kembalikan equal weight sebagai fallback
        best_w = init_w
    else:
        best_w = res.x
        
    # Ambil K indeks dengan bobot terbesar
    selected_indices = np.argsort(best_w)[-K:]
    
    return sorted(list(selected_indices)), best_w
