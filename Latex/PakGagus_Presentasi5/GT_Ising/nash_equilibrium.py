import numpy as np
from itertools import combinations

def find_nash_equilibrium(h, J, N=4, K=2):
    best_energy = np.inf
    best_bitstring = None
    all_energies = {}
    
    for combo in combinations(range(N), K):
        x = np.zeros(N, dtype=int)
        for idx in combo:
            x[idx] = 1
            
        Z = 1 - 2 * x 
        
        E = 0.0
        for i in range(N):
            E += h[i] * Z[i]
            for j in range(i + 1, N):
                E += J[i, j] * Z[i] * Z[j]
                
        bitstring = "".join(str(bit) for bit in x)
        all_energies[bitstring] = E
        
        if E < best_energy:
            best_energy = E
            best_bitstring = bitstring
            
    return best_bitstring, best_energy, all_energies
