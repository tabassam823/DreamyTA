import numpy as np
import cma
from qiskit.primitives import StatevectorSampler
from qiskit.quantum_info import Statevector

# Import our previous modules
from build_hamiltonian import build_hamiltonian
from build_ansatz import get_ansatz

def get_diagonal_hamiltonian(hamiltonian):
    """
    Extracts the diagonal of the Hamiltonian matrix efficiently.
    Since H is an Ising Hamiltonian, it is diagonal in the Z-basis.
    """
    # For N=12, 2^12 = 4096 is small enough to store the full diagonal.
    # We can get it by summing the diagonals of each Pauli term.
    
    num_qubits = hamiltonian.num_qubits
    dim = 2**num_qubits
    diagonal = np.zeros(dim, dtype=complex)
    
    for pauli, coeff in zip(hamiltonian.paulis, hamiltonian.coeffs):
        # Convert Pauli string to diagonal Z-vector
        # 'I' -> 1, 'Z' -> -1
        # The diagonal is the tensor product of these values.
        
        # We can construct the diagonal for this term efficiently
        term_diag = np.ones(1, dtype=complex)
        
        # Iterate through the pauli string (reversed because qiskit is little-endian)
        # However, SparsePauliOp is usually stored such that index 0 is the rightmost in string but 
        # let's rely on the label.
        # String 'Z...Z' corresponds to qubits N-1 ... 0
        
        # A safer way using Qiskit's built-in functionality if available, 
        # or just manual tensor product.
        
        # Let's iterate from qubit 0 to N-1
        # Qiskit Pauli string index 0 is the rightmost char (qubit 0).
        
        p_str = pauli.to_label()
        
        # We build from qubit 0 (last char) up to N-1 (first char)
        current_diag = np.array([1])
        
        for char in reversed(p_str):
            if char == 'I':
                op = np.array([1, 1])
            elif char == 'Z':
                op = np.array([1, -1])
            else:
                raise ValueError("Hamiltonian must be Ising (I/Z only).")
            
            # Tensor product: new = op (tensor) current
            # But numpy kronecker is A (tensor) B. 
            # If we want qubit N-1 (tensor) ... (tensor) qubit 0
            # We are building from 0 up. So next qubit is to the left (A).
            current_diag = np.kron(op, current_diag)
            
        diagonal += coeff * current_diag
        
    return np.real(diagonal)

def bitstring_to_int(bitstring):
    """Converts a bitstring '101...' to integer."""
    return int(bitstring, 2)

def cost_function(parameters, ansatz, diagonal_energies, sampler, shots=1000):
    """
    WCVaR Cost Function using Rank-Based Exponential Weighting.
    """
    # 1. Bind parameters
    # ansatz.assign_parameters(parameters) is deprecated/slow in loop
    # We use the sampler's binding mechanism
    
    # 2. Measure (Simulate)
    # Using StatevectorSampler for simulation
    # Primitive V2 run() takes a list of pubs (Primitive Unified Blocs)
    # Each pub is (circuit, parameter_values)
    job = sampler.run([(ansatz, parameters)], shots=shots)
    result = job.result()
    
    # Get counts/bitstrings from the first (and only) pub result
    data = result[0].data
    # bitstrings = data.meas.get_bitstrings() # This gives list of all shots
    # Alternatively, get counts directly if supported, but Sampler V2 returns bitstrings/counts
    
    counts = data.meas.get_counts()
    
    # 3. Process Data
    # Expand to list of energies
    sampled_energies = []
    
    for bitstring, count in counts.items():
        # Calculate Energy
        # Map bitstring to index: '0...0' -> 0, '0...1' -> 1
        # Note: Qiskit bitstrings are usually Little Endian in print? 
        # No, Qiskit '01' means q1=0, q0=1 usually.
        # Our diagonal construction was [qN-1 ... q0].
        # So '0...1' (q0=1) should map to index 1.
        
        idx = int(bitstring, 2)
        energy = diagonal_energies[idx]
        
        sampled_energies.extend([energy] * count)
        
    # 4. Sort Energies
    sampled_energies.sort()
    K = len(sampled_energies) # Should be shots
    
    # 5. Weighting (WCVaR)
    # Constants from instruction
    alpha = 0.25
    beta = 1.0
    
    # Cutoff index
    cutoff = int(np.ceil(alpha * K))
    tail_energies = sampled_energies[:cutoff]
    
    # Weights: w_k = exp(-beta * k) for k = 1 to cutoff
    # Note: k is 1-based rank
    ks = np.arange(1, cutoff + 1)
    weights = np.exp(-beta * ks)
    
    # Normalize weights
    weights /= np.sum(weights)
    
    # Weighted Sum
    wcvar = np.sum(weights * tail_energies)
    
    return wcvar

def main():
    # ---------------------------------------------------------
    # 1. Setup Data & Hamiltonian
    # ---------------------------------------------------------
    print("Setting up Portfolio Optimization problem...")
    
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
    
    # Build Hamiltonian
    hamiltonian = build_hamiltonian(mu, sigma, risk_aversion=0.5, penalty=1.0)
    
    # Pre-compute Diagonal
    print("Pre-computing Hamiltonian diagonal (this may take a moment)...")
    diagonal_energies = get_diagonal_hamiltonian(hamiltonian)
    print("Diagonal computed.")
    
    # ---------------------------------------------------------
    # 2. Setup Ansatz
    # ---------------------------------------------------------
    ansatz = get_ansatz(num_qubits=N)
    ansatz.measure_all() # Ensure we measure all qubits
    
    # ---------------------------------------------------------
    # 3. Optimization with CMA-ES
    # ---------------------------------------------------------
    print("\nStarting CMA-ES Optimization (max 500 evals)...")
    
    # Initial parameters
    num_params = ansatz.num_parameters
    x0 = np.random.rand(num_params) * 2 * np.pi # Random start in [0, 2pi]
    sigma0 = 0.5 # Initial step size
    
    # Sampler
    sampler = StatevectorSampler()
    
    # Wrapper for CMA-ES
    # CMA-ES minimizes, so we return WCVaR directly
    def objective(x):
        return cost_function(x, ansatz, diagonal_energies, sampler, shots=1000)
    
    # Run Optimization
    # options={'maxfevals': 500, 'verbose': -9} to reduce noise if needed
    es = cma.fmin(objective, x0, sigma0, options={'maxfevals': 500, 'verb_disp': 50})
    
    best_params = es[0]
    best_wcvar = es[1]
    
    print("\n" + "="*50)
    print("OPTIMIZATION RESULTS")
    print("="*50)
    print(f"Best WCVaR: {best_wcvar}")
    
    # ---------------------------------------------------------
    # 4. Final Evaluation
    # ---------------------------------------------------------
    print("\nEvaluating Best Solution...")
    job = sampler.run([(ansatz, best_params)], shots=2000)
    result = job.result()
    counts = result[0].data.meas.get_counts()
    
    # Find most frequent bitstring
    best_bitstring = max(counts, key=counts.get)
    
    # Find lowest energy bitstring sampled
    min_energy = float('inf')
    best_energy_bitstring = ""
    
    for bs in counts:
        idx = int(bs, 2)
        en = diagonal_energies[idx]
        if en < min_energy:
            min_energy = en
            best_energy_bitstring = bs
            
    print(f"Most Frequent Bitstring: {best_bitstring}")
    print(f"Lowest Energy Bitstring: {best_energy_bitstring}")
    print(f"Minimum Energy: {min_energy}")
    
    # Interpret Portfolio
    # Bitstring '101...' means: q11 q10 ... q0
    # Asset order in Phase 1 was:
    assets = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'NVDA', 'JPM', '600519.SS', '601398.SS', '600036.SS', '601857.SS', '600276.SS', '601318.SS']
    
    # Reverse bitstring to match array order (q0 is first asset?)
    # Wait, usually q0 is the LEAST significant bit in integer conversion, but printed as Rightmost.
    # If we mapped x_i -> Z_i, then q_i corresponds to x_i.
    # Qiskit print "100" means q2=1, q1=0, q0=0.
    # So if string is "00...01" (q0=1), it means Asset 0 is selected.
    # The string is length N. Index i corresponds to q_i.
    # In the string representation, q0 is at index -1 (last).
    
    selected_assets = []
    # Iterate from right (q0) to left
    bs_reversed = best_energy_bitstring[::-1] # Now index 0 is q0
    
    print("\nSelected Portfolio (from Lowest Energy Sample):")
    for i, bit in enumerate(bs_reversed):
        if bit == '1':
            selected_assets.append(assets[i])
            
    print(selected_assets)
    print(f"Number of assets selected: {len(selected_assets)}")

if __name__ == "__main__":
    main()
