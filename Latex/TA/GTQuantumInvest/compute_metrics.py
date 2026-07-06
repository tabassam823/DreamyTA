import numpy as np

def compute_metrics(value_series, initial_capital, label=""):
    vals   = np.array(value_series)
    rets   = np.diff(vals) / vals[:-1]

    total_return = (vals[-1] - initial_capital) / initial_capital * 100.0

    if len(rets) > 0 and rets.std() > 1e-12:
        sharpe = (rets.mean() / rets.std()) * np.sqrt(252)
    else:
        sharpe = 0.0

    peak = np.maximum.accumulate(vals)
    dd   = (peak - vals) / peak
    mdd  = dd.max() * 100.0

    print(f"\n{'='*50}")
    print(f"  Metrik Kinerja: {label}")
    print(f"{'='*50}")
    print(f"  Total Return   : {total_return:+.2f}%")
    print(f"  Sharpe Ratio   : {sharpe:.4f}")
    print(f"  Max Drawdown   : {mdd:.2f}%")
    print(f"{'='*50}")
    return total_return, sharpe, mdd

def calculate_entanglement_entropy(psi):
    """
    Menghitung Entanglement Entropy (Von Neumann) dari statevector N-qubit.
    Menggunakan partial trace terhadap semua qubit kecuali qubit 0.
    """
    # 1. Konversi ke numpy array complex
    psi = np.array(psi, dtype=complex)
    dim = len(psi)
    n_qubits = int(np.round(np.log2(dim)))

    # 2. Partial Trace untuk mendapatkan Reduced Density Matrix rho_A (Qubit 0)
    # Reshape psi menjadi (dim_A, dim_B) di mana dim_A = 2 (qubit pertama)
    # dim_B = 2^(N-1) (sisa qubit lainnya)
    psi_reshaped = psi.reshape(2, 2**(n_qubits - 1))
    
    # rho_A = psi * psi_dagger (Matrix Multiplication)
    rho_A = np.dot(psi_reshaped, psi_reshaped.conj().T)

    # 3. Hitung Eigenvalues dari rho_A (matriks 2x2)
    eigvals = np.linalg.eigvalsh(rho_A)

    # 4. Bersihkan nilai negatif sangat kecil akibat floating point error
    eigvals = eigvals[eigvals > 1e-12]

    # 5. Von Neumann Entropy: S = -sum(p * log2(p))
    if len(eigvals) == 0:
        return 0.0
        
    return -np.sum(eigvals * np.log2(eigvals))
