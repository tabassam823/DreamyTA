import numpy as np
import pandas as pd
import os
from itertools import product

def brute_force_optimization(n_assets, h, J, C_Ising, K=2):
    """
    Mengecek semua kemungkinan 2^N bitstring untuk menemukan energi terendah secara mutlak.
    """
    best_energy = float('inf')
    best_bitstring = None
    
    # Generate semua kemungkinan bitstring (0 dan 1) untuk N aset
    all_combinations = list(product([0, 1], repeat=n_assets))
    
    results = []

    for bit_tuple in all_combinations:
        x = np.array(bit_tuple)
        # Transformasi ke Spin (Z) -> x=0 -> Z=1, x=1 -> Z=-1
        Z = 1 - 2 * x
        
        # Hitung Energi: E = sum(h_i * Z_i) + sum(J_ij * Z_i * Z_j) + C_Ising
        energy_ising = 0
        # Suku Bias
        for i in range(n_assets):
            energy_ising += h[i] * Z[i]
        
        # Suku Interaksi
        for i in range(n_assets):
            for j in range(i + 1, n_assets):
                energy_ising += J[i, j] * Z[i] * Z[j]
        
        # Tambahkan Konstanta
        total_energy = energy_ising + C_Ising
        
        bit_str = "".join(map(str, bit_tuple))
        results.append({'bitstring': bit_str, 'energy': total_energy, 'valid': (sum(x) == K)})
        
        if total_energy < best_energy:
            best_energy = total_energy
            best_bitstring = bit_str
            
    return best_bitstring, best_energy, pd.DataFrame(results)

def run_brute_force_window(curr_date, n_assets, h, J, C_Ising, K, file_config):
    """Menjalankan validasi brute force untuk satu window tertentu dan mengekspor hasilnya."""
    best_bs, best_e, full_results = brute_force_optimization(n_assets, h, J, C_Ising, K=K)
    
    # Tambahkan kolom Tanggal
    full_results.insert(0, 'Date', curr_date.date())
    
    # Simpan hasil (append)
    file_path = file_config.get('brute_force', 'hasil_brute_force_validation.csv')
    full_results.to_csv(file_path, mode='a', header=not os.path.exists(file_path), index=False)
    
    return best_bs, best_e

if __name__ == "__main__":
    validate_last_window()
