from qiskit.quantum_info import SparsePauliOp
import numpy as np

def build_hamiltonian(mu, sigma, risk_aversion=0.5, penalty=1.0):
    """
    Constructs the Ising Hamiltonian for the Portfolio Optimization problem.
    
    Args:
        mu (numpy.ndarray): Expected return vector of size N.
        sigma (numpy.ndarray): Covariance matrix of size NxN.
        risk_aversion (float): Risk aversion parameter (lambda).
        penalty (float): Penalty coefficient for the budget constraint.
        
    Returns:
        SparsePauliOp: The Ising Hamiltonian.
    """
    N = len(mu)
    # The budget B is fixed to N/2 as per the paper context
    B = N / 2
    
    # We will build the Hamiltonian as a list of (pauli_string, coeff)
    # and then sum them up into a SparsePauliOp.
    # Alternatively, and more efficiently, we can sum SparsePauliOp objects directly.
    
    # Initialize an empty Hamiltonian
    H = SparsePauliOp(['I' * N], coeffs=[0.0])
    
    # ---------------------------------------------------------
    # 1. Term: -lambda * sum(mu_i * x_i)
    # Mapping: x_i -> (I - Z_i) / 2
    # So: -lambda * mu_i * (I - Z_i)/2 = (-lambda * mu_i / 2) * I - (-lambda * mu_i / 2) * Z_i
    #                                  = (-lambda * mu_i / 2) * I + (lambda * mu_i / 2) * Z_i
    # ---------------------------------------------------------
    
    for i in range(N):
        # Construct Z_i operator
        # SparsePauliOp.from_list([("II...Z...II", 1)]) where Z is at index i
        # Qiskit uses little-endian (qubit 0 is rightmost), but usually for simple sums it doesn't matter 
        # as long as we are consistent. Let's use the standard index i from left to right for string construction 
        # or just use the position in the list.
        # String representation: "I" * (N - 1 - i) + "Z" + "I" * i (if 0 is rightmost)
        # Let's stick to Qiskit's standard: "Z" at index i implies the i-th qubit.
        
        op_zi = SparsePauliOp.from_sparse_list([("Z", [i], 1.0)], num_qubits=N)
        op_id = SparsePauliOp(['I' * N], coeffs=[1.0])
        
        # Coeffs for this term
        c_linear = -risk_aversion * mu[i]
        
        # x_i = 0.5 * (I - Z_i)
        term = c_linear * 0.5 * (op_id - op_zi)
        H += term

    # ---------------------------------------------------------
    # 2. Term: (1 - lambda) * sum_{i < j} (sigma_ij * x_i * x_j)
    # Mapping: x_i * x_j -> 0.25 * (I - Z_i) * (I - Z_j)
    #                     = 0.25 * (I - Z_i - Z_j + Z_i Z_j)
    # ---------------------------------------------------------
    
    for i in range(N):
        for j in range(i + 1, N):
            op_zi = SparsePauliOp.from_sparse_list([("Z", [i], 1.0)], num_qubits=N)
            op_zj = SparsePauliOp.from_sparse_list([("Z", [j], 1.0)], num_qubits=N)
            op_zizj = op_zi @ op_zj # Tensor product / composition
            op_id = SparsePauliOp(['I' * N], coeffs=[1.0])
            
            # Coeff for this term
            c_quad = (1 - risk_aversion) * sigma[i, j]
            
            # x_i * x_j term expansion
            # 0.25 * (I - Z_i - Z_j + Z_i*Z_j)
            term = c_quad * 0.25 * (op_id - op_zi - op_zj + op_zizj)
            H += term

    # ---------------------------------------------------------
    # 3. Term: p * (sum(x_i) - B)^2
    # Expansion: p * [ (sum x_i)^2 - 2B * sum x_i + B^2 ]
    # (sum x_i)^2 = sum (x_i^2) + 2 * sum_{i<j} (x_i * x_j)
    # Since x_i is binary, x_i^2 = x_i.
    # So: (sum x_i)^2 = sum x_i + 2 * sum_{i<j} x_i x_j
    # 
    # Full Penalty Term:
    # p * [ sum x_i + 2 * sum_{i<j} x_i x_j - 2B * sum x_i + B^2 ]
    # = p * [ (1 - 2B) * sum x_i + 2 * sum_{i<j} x_i x_j + B^2 ]
    # ---------------------------------------------------------
    
    # 3a. Constant part: p * B^2
    H += SparsePauliOp(['I' * N], coeffs=[penalty * (B**2)])
    
    # 3b. Linear part: p * (1 - 2B) * sum(x_i)
    coeff_linear_penalty = penalty * (1 - 2 * B)
    for i in range(N):
        op_zi = SparsePauliOp.from_sparse_list([("Z", [i], 1.0)], num_qubits=N)
        op_id = SparsePauliOp(['I' * N], coeffs=[1.0])
        
        # x_i = 0.5 * (I - Z_i)
        term = coeff_linear_penalty * 0.5 * (op_id - op_zi)
        H += term
        
    # 3c. Quadratic part: p * 2 * sum_{i<j} (x_i * x_j)
    # = 2p * sum_{i<j} (x_i * x_j)
    coeff_quad_penalty = 2 * penalty
    for i in range(N):
        for j in range(i + 1, N):
            op_zi = SparsePauliOp.from_sparse_list([("Z", [i], 1.0)], num_qubits=N)
            op_zj = SparsePauliOp.from_sparse_list([("Z", [j], 1.0)], num_qubits=N)
            op_zizj = op_zi @ op_zj
            op_id = SparsePauliOp(['I' * N], coeffs=[1.0])
            
            # x_i * x_j = 0.25 * (I - Z_i - Z_j + Z_i*Z_j)
            term = coeff_quad_penalty * 0.25 * (op_id - op_zi - op_zj + op_zizj)
            H += term

    # Simplify the Hamiltonian to combine like terms
    H = H.simplify()
    return H

if __name__ == "__main__":
    # Real data from Phase 1
    N = 12
    mu = np.array([
        0.00129829, 0.00063003, 0.00142009, 0.00165567, 0.00458041,
        0.0014705, -0.00010674, 0.00170935, 0.00173847, 0.00130019,
        0.00036145, 0.00156579
    ])
    
    sigma = np.array([
        [1.93065254e-04, 8.06667321e-05, 8.67697331e-05, 8.14811864e-05, 1.14943731e-04, 3.14880919e-06, 3.34852086e-06, 1.50490305e-08, 1.78463544e-06, -4.26159620e-06, 2.48643108e-05, 2.09408214e-05],
        [8.06667321e-05, 1.52769153e-04, 1.22908368e-04, 1.47812317e-04, 1.84036012e-04, 2.90522192e-05, -2.45438019e-06, -1.91957115e-05, -7.39709853e-06, 9.48176167e-06, 6.50059737e-06, 6.73923882e-06],
        [8.67697331e-05, 1.22908368e-04, 3.02691633e-04, 1.63384728e-04, 1.77293621e-04, 3.60765336e-05, 3.58302022e-05, 7.69963292e-06, 3.61670055e-05, 5.51268604e-05, 2.80899835e-05, 5.20217182e-05],
        [8.14811864e-05, 1.47812317e-04, 1.63384728e-04, 3.03478746e-04, 2.47351255e-04, 6.09185345e-05, 4.25115695e-06, -1.50900366e-05, -1.30070811e-06, 2.50807932e-05, -9.15458602e-06, 1.73895365e-05],
        [1.14943731e-04, 1.84036012e-04, 1.77293621e-04, 2.47351255e-04, 1.05798856e-03, 4.11219245e-05, 4.41488486e-05, -1.56736230e-05, 2.02663425e-05, 9.39947198e-05, 6.88672246e-05, 6.60165422e-05],
        [3.14880919e-06, 2.90522192e-05, 3.60765336e-05, 6.09185345e-05, 4.11219245e-05, 2.12766228e-04, -1.27275706e-05, -7.30702607e-06, -1.48841441e-05, -9.23187646e-07, -2.27303193e-05, -2.20272177e-05],
        [3.34852086e-06, -2.45438019e-06, 3.58302022e-05, 4.25115695e-06, 4.41488486e-05, -1.27275706e-05, 2.83836809e-04, 4.24976797e-05, 1.43912160e-04, 7.75746777e-05, 1.73707021e-04, 2.05431126e-04],
        [1.50490305e-08, -1.91957115e-05, 7.69963292e-06, -1.50900366e-05, -1.56736230e-05, -7.30702607e-06, 4.24976797e-05, 1.51073599e-04, 9.93120476e-05, 1.02098869e-04, -1.09195027e-07, 6.73227594e-05],
        [1.78463544e-06, -7.39709853e-06, 3.61670055e-05, -1.30070811e-06, 2.02663425e-05, -1.48841441e-05, 1.43912160e-04, 9.93120476e-05, 2.26926540e-04, 1.21574865e-04, 1.08965226e-04, 2.10847667e-04],
        [-4.26159620e-06, 9.48176167e-06, 5.51268604e-05, 2.50807932e-05, 9.39947198e-05, -9.23187646e-07, 7.75746777e-05, 1.02098869e-04, 1.21574865e-04, 4.23158499e-04, 4.84957737e-05, 1.20344712e-04],
        [2.48643108e-05, 6.50059737e-06, 2.80899835e-05, -9.15458602e-06, 6.88672246e-05, -2.27303193e-05, 1.73707021e-04, -1.09195027e-07, 1.08965226e-04, 4.84957737e-05, 4.05630777e-04, 1.83171953e-04],
        [2.09408214e-05, 6.73923882e-06, 5.20217182e-05, 1.73895365e-05, 6.60165422e-05, -2.20272177e-05, 2.05431126e-04, 6.73227594e-05, 2.10847667e-04, 1.20344712e-04, 1.83171953e-04, 3.23460020e-04]
    ])
    
    print(f"Building Hamiltonian for N={N} assets with Budget B={N/2}...")
    
    # Build Hamiltonian using standard parameters
    hamiltonian = build_hamiltonian(mu, sigma, risk_aversion=0.5, penalty=1.0)
    
    print("\nHamiltonian Construction Complete.")
    print(f"Number of qubits: {hamiltonian.num_qubits}")
    print(f"Number of Pauli terms: {len(hamiltonian.paulis)}")
    
    # Verify complexity: Should be roughly N + N*(N-1)/2 + 1 terms (Linear + Quad + Const)
    # For N=12: 12 + 66 + 1 = 79 terms approximately (might be less due to cancellations or groupings)
    expected_terms_approx = N + (N * (N - 1) / 2) + 1
    print(f"Expected approx number of terms (N + NC2 + 1): {int(expected_terms_approx)}")
    
    # Print first few terms to check
    print("\nFirst 5 terms of the Hamiltonian:")
    print(hamiltonian[:5])
