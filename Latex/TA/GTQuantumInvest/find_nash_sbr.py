import numpy as np
import pandas as pd
import os

def find_nash_sbr(mu, sigma_matrix, gamma, curr_date, N=4, K=2, max_iters=100, history_file='riwayat_nash_sbr.csv'):
    """
    Pencarian Nash Equilibrium menggunakan Sequential Best Response (SBR)
    dalam Exact Potential Game.
    
    Potensial (Utilitas Portofolio):
    Phi = (1/K) * mu^T * x - (gamma / (2 * K^2)) * x^T * sigma * x
    
    Dalam Potential Game, Nash Equilibrium adalah local maximum dari fungsi potensial.
    Karena ada batasan sum(x) = K, kita menggunakan swap moves untuk mencari NE.
    """
    # Inisialisasi: pilih K aset pertama
    current_selection = set(range(K))
    history = []
    
    def calculate_potential(selection):
        x = np.zeros(N)
        for idx in selection: x[idx] = 1
        
        # 1. Komponen Return: (1/K) * sum(mu_i * x_i)
        ret = np.sum(mu[list(selection)]) / K
        
        # 2. Komponen Risiko: (gamma / (2 * K^2)) * sum(sigma_ij * x_i * x_j)
        # x^T * Sigma * x untuk subset selection
        if len(selection) > 0:
            sub_sigma = sigma_matrix[np.ix_(list(selection), list(selection))]
            risk = np.sum(sub_sigma) * (gamma / (2.0 * K**2))
        else:
            risk = 0.0
            
        return ret - risk

    current_phi = calculate_potential(current_selection)
    
    history.append({
        'Date': curr_date.date(),
        'Iteration': 0,
        'Bitstring': "".join(str(int(i in current_selection)) for i in range(N)),
        'Utility': current_phi,
        'Swap': 'Initial'
    })
    
    for iteration in range(1, max_iters + 1):
        improved = False
        out_portfolio = set(range(N)) - current_selection
        
        best_swap = None
        max_phi = current_phi
        
        # SBR/Local Search: Coba tukar satu aset di dalam dengan satu aset di luar
        # Mencari swap yang meningkatkan fungsi potensial paling besar
        for i in current_selection:
            for j in out_portfolio:
                new_selection = (current_selection - {i}) | {j}
                new_phi = calculate_potential(new_selection)
                
                if new_phi > max_phi:
                    max_phi = new_phi
                    best_swap = (i, j)
        
        if best_swap:
            i, j = best_swap
            current_selection = (current_selection - {i}) | {j}
            current_phi = max_phi
            improved = True
            history.append({
                'Date': curr_date.date(),
                'Iteration': iteration,
                'Bitstring': "".join(str(int(idx in current_selection)) for idx in range(N)),
                'Utility': current_phi,
                'Swap': f"{i}<->{j}"
            })
        
        if not improved:
            break
            
    # --- EKSPOR RIWAYAT NASH SBR ---
    df_history = pd.DataFrame(history)
    if not os.path.exists(history_file):
        df_history.to_csv(history_file, index=False)
    else:
        df_history.to_csv(history_file, mode='a', header=False, index=False)

    final_x = np.zeros(N, dtype=int)
    for idx in current_selection: final_x[idx] = 1
    # Kembalikan bitstring dan utilitas akhir (sebagai potensial)
    return "".join(str(bit) for bit in final_x), current_phi
