
import pennylane as qml
import numpy as np
import matplotlib.pyplot as plt
import os

def compute_bias_hi(all_payoffs, tickers):
    """Calculate bias h_i from marginal payoff matrices."""
    n_assets = len(tickers)
    h = np.zeros(n_assets)
    # Map ticker to index
    ticker_to_idx = {t: i for i, t in enumerate(tickers)}
    
    for i in range(n_assets):
        payoff_sum = 0
        count = 0
        # Iterate over all pairs involving asset i
        for (key, (pA, pB)) in all_payoffs.items():
            # Handle both index-based and name-based keys
            if isinstance(key[0], int):
                idx_a, idx_b = key
            else:
                idx_a = ticker_to_idx[key[0]]
                idx_b = ticker_to_idx[key[1]]
                
            if idx_a == i:
                # i is Player A. Marginalize over B (columns).
                # Difference between State 1 (Down) and State 0 (Up)
                # Note: Payoff matrix indices: 0=Up, 1=Down.
                # Usually we want to minimize Cost. If Down (1) is bad (low utility), 
                # then (Utility(1) - Utility(0)) might be negative. 
                # Hamiltonian coeff usually corresponds to energy. Lower energy = better.
                # If we map x=1 to selected (or "Down" depending on mapping), we align signs.
                # In notebook: h_i ~ (E[U(1)] - E[U(0)]) 
                u_down = (pA[1, 0] + pA[1, 1]) / 2.0
                u_up = (pA[0, 0] + pA[0, 1]) / 2.0
                payoff_sum += (u_down - u_up)
                count += 1
            elif idx_b == i:
                # i is Player B. Marginalize over A (rows).
                u_down = (pB[0, 1] + pB[1, 1]) / 2.0
                u_up = (pB[0, 0] + pB[1, 0]) / 2.0
                payoff_sum += (u_down - u_up)
                count += 1
                
        if count > 0:
            h[i] = payoff_sum / count
            
    return h

def build_hamiltonian(h, J, n_assets, K=2, penalty_A=10.0):
    """Build total Hamiltonian = H_cost + H_constraint"""
    coeffs = []
    obs = []
    
    # H_cost terms: sum(h_i * Z_i) + sum(J_ij * Z_i * Z_j)
    # Note: signs depend on mapping. 
    # If h_i > 0 suggests "Down" state (1) has higher cost (lower utility), we want to avoid 1.
    # Pauli Z eigenvalues: |0> -> +1, |1> -> -1.
    # If we map x_i (0 or 1) to (I - Z_i)/2, then |1> corresponds to value 1.
    
    # Notebook implementation check:
    # It seems to just use h[i] direct coefficient for PauliZ.
    # Let's stick to notebook logic: coeffs.append(float(h[i]))
    
    for i in range(n_assets):
        if abs(h[i]) > 1e-10:
            coeffs.append(float(h[i]))
            obs.append(qml.PauliZ(i))
    
    for i in range(n_assets):
        for j in range(i + 1, n_assets):
            if abs(J[i, j]) > 1e-10:
                coeffs.append(float(J[i, j]))
                obs.append(qml.PauliZ(i) @ qml.PauliZ(j))
    
    # H_constraint terms: A(Sum((I-Zi)/2) - K)^2
    N_half_minus_K = n_assets / 2.0 - K
    const_val = penalty_A * (N_half_minus_K**2 + n_assets / 4.0)
    
    # Constant term (Identity)
    if abs(const_val) > 1e-10:
        coeffs.append(float(const_val))
        obs.append(qml.Identity(0))
    
    # Linear terms from constraint (-A * (N/2 - K) * Zi)
    for i in range(n_assets):
        coeff = -penalty_A * N_half_minus_K
        coeffs.append(float(coeff))
        obs.append(qml.PauliZ(i))
    
    # Quadratic terms from constraint (A/4 * ZiZj * 2 = A/2 * ZiZj)
    for i in range(n_assets):
        for j in range(i + 1, n_assets):
            coeffs.append(float(penalty_A * 0.5))
            obs.append(qml.PauliZ(i) @ qml.PauliZ(j))
    
    H = qml.Hamiltonian(coeffs, obs)
    return H

def generate_bias_visualization(h, tickers, output_dir="generated_images"):
    """Generates bar chart for bias h_i."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    plt.figure(figsize=(8, 5))
    plt.bar(tickers, h, color='skyblue')
    plt.title("Bias Terms (h_i) - Cost Sensitivity")
    plt.xlabel("Assets")
    plt.ylabel("Value")
    plt.axhline(0, color='black', linewidth=0.8)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/bias_terms.png")
    plt.close()
    print(f"Bias visualization saved to {output_dir}")

if __name__ == "__main__":
    # Test execution
    # This requires Data, Payoffs, and QMI
    import data_analysis
    import payoff_matrix
    import entropy_qmi
    
    TICKERS = ['BBCA.JK', 'ASII.JK', 'TLKM.JK', 'TPIA.JK']
    OUTPUT_DIR = "generated_images" # Test dir
    
    # Mock data flow for testing this module specifically would be complex without full run.
    # But let's assume imports and standard flow:
    data = data_analysis.download_data(TICKERS, "2025-01-01", "2025-01-10")
    log_returns = data_analysis.calculate_log_returns(data)
    binary_states = (log_returns <= 0).astype(int)
    all_payoffs, _, _ = payoff_matrix.run_payoff_analysis(log_returns, binary_states, TICKERS)
    
    h = compute_bias_hi(all_payoffs, TICKERS)
    generate_bias_visualization(h, TICKERS, OUTPUT_DIR)
    
    J = entropy_qmi.compute_all_qmi(binary_states, TICKERS)
    H = build_hamiltonian(h, J, len(TICKERS))
    print("Hamiltonian constructed:", H)
