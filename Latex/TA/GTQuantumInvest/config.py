import os

# =============================================================================
# 0. Daftar File untuk Pembersihan (Workspace Cleaning)
# =============================================================================
def clean_workspace(N=None):
    """Menghapus file intermediate lama agar tidak terjadi duplikasi data."""
    suffix = f"_N{N}" if N is not None else ""
    files_to_clean = [
        f'metrik_return_dan_lambda{suffix}.csv', 
        f'bias_h_total{suffix}.csv', 
        f'interaksi_J_total{suffix}.csv',
        f'konstanta_C_total{suffix}.csv', 
        f'riwayat_nash_sbr{suffix}.csv', 
        f'hasil_pencarian_lr{suffix}.csv', 
        f'hasil_depth_vs_energi{suffix}.csv', 
        f'riwayat_iterasi_vqe{suffix}.csv', 
        f'theta_final_all_depths{suffix}.csv',
        f'parameter_pendamping{suffix}.csv',
        f'hasil_brute_force_validation{suffix}.csv'
    ]
    for f in files_to_clean:
        if os.path.exists(f):
            try:
                os.remove(f)
            except:
                pass

# =============================================================================
# 1. Konfigurasi Global (Hyperparameters)
# =============================================================================
def get_config(tickers):
    """
    Menghasilkan dictionary konfigurasi berdasarkan daftar tickers.
    Semua parameter di sini akan seragam untuk seluruh file main_N.py.
    """
    N = len(tickers)
    # Kedalaman sirkuit adaptif: 4 + N, tapi dibatasi maksimal 12 untuk N besar agar efisien
    max_depth_val = min(12, 4 + N)
    
    import numpy as np
    suffix = f"_N{N}"
    return {
        'tickers': tickers,
        'N': N,
        'K': N // 2,                 
        'penalty_A': 5.0, 
        'max_depth': max_depth_val,          
        'maxiter': 100 + (20 * N),    

        'max_total_iter': 400 + (100 * N), 
        'batch_size': 10,            
        'conv_window': 5,            
        'conv_tol': 1e-5,            
        'initial_capital': 100_000_000.0,
        'lookback_days': 126,        
        'rebalance_days': 21,        
        'benchmark_ticker': '^JKSE',
        'start_date': "2020-06-01",
        'end_date': "2024-01-01",
        'start_bt_date': '2021-01-04',
        'use_warm_start': False,

        # --- File Outputs Terlokalisasi (Agar Bisa Paralel) ---
        'files': {
            'metrics': f'metrik_return_dan_lambda{suffix}.csv',
            'bias_h': f'bias_h_total{suffix}.csv',
            'interaksi_J': f'interaksi_J_total{suffix}.csv',
            'nash_history': f'riwayat_nash_sbr{suffix}.csv',
            'pencarian_lr': f'hasil_pencarian_lr{suffix}.csv',
            'depth_vs_energi': f'hasil_depth_vs_energi{suffix}.csv',
            'riwayat_iterasi': f'riwayat_iterasi_vqe{suffix}.csv',
            'theta_final': f'theta_final_all_depths{suffix}.csv',
            'parameter_pendamping': f'parameter_pendamping{suffix}.csv',
            'brute_force': f'hasil_brute_force_validation{suffix}.csv',
            'equity_history': f'hasil_ekuitas_backtest{suffix}.csv'
        }
    }

