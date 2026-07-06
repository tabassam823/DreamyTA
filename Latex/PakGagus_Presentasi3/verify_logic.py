
import pennylane as qml
from scipy import linalg as la
from itertools import combinations
import numpy as np
import pandas as pd

# === Helper Functions (Pasted from update) ===

def compute_endogenous_lambda(log_returns, tickers):
    """λ_market = σ_avg / (μ_avg + σ_avg), annualized"""
    mu_annual = log_returns[tickers].mean() * 252
    sigma_annual = log_returns[tickers].std() * np.sqrt(252)
    mu_avg = abs(mu_annual).mean()
    sigma_avg = sigma_annual.mean()
    if np.isnan(mu_avg) or np.isnan(sigma_avg) or (mu_avg + sigma_avg) == 0:
        return 0.5 
    return sigma_avg / (mu_avg + sigma_avg)

def compute_markowitz_payoff_matrix(log_returns, binary_states, asset_a, asset_b, lambda_risk):
    state_A = binary_states[asset_a].values
    state_B = binary_states[asset_b].values
    ret_A = log_returns[asset_a].values
    ret_B = log_returns[asset_b].values
    
    payoff_A = np.zeros((2, 2))
    payoff_B = np.zeros((2, 2))
    counts = np.zeros((2, 2))
    
    for t in range(len(state_A)):
        i, j = int(state_A[t]), int(state_B[t])
        counts[i, j] += 1
        u_A = (1 - lambda_risk) * (ret_A[t] * 252) - lambda_risk * abs(ret_A[t] * 252)
        u_B = (1 - lambda_risk) * (ret_B[t] * 252) - lambda_risk * abs(ret_B[t] * 252)
        
        payoff_A[i, j] += u_A
        payoff_B[i, j] += u_B
    
    for i in range(2):
        for j in range(2):
            if counts[i, j] > 0:
                payoff_A[i, j] /= counts[i, j]
                payoff_B[i, j] /= counts[i, j]
    
    return payoff_A, payoff_B

def classify_game_type(payoff_A, payoff_B):
    coord_A = (payoff_A[0, 0] > payoff_A[1, 0]) and (payoff_A[1, 1] > payoff_A[0, 1])
    coord_B = (payoff_B[0, 0] > payoff_B[0, 1]) and (payoff_B[1, 1] > payoff_B[1, 0])
    
    if coord_A and coord_B:
        return "Coordination Game"
    elif (not coord_A) and (not coord_B):
        return "Anti-Coordination Game"
    else:
        return "Mixed Strategy Game"

def compute_bias_hi(all_payoffs, tickers):
    n_assets = len(tickers)
    h = np.zeros(n_assets)
    for i in range(n_assets):
        payoff_sum = 0
        count = 0
        for (a, b), (pA, pB) in all_payoffs.items():
            if a == i:
                payoff_sum += (pA[1, 0] + pA[1, 1]) - (pA[0, 0] + pA[0, 1])
                count += 1
            elif b == i:
                payoff_sum += (pB[0, 1] + pB[1, 1]) - (pB[0, 0] + pB[1, 0])
                count += 1
        if count > 0:
            h[i] = payoff_sum / count
    return h

def compute_qmi_jij(binary_states, asset_a, asset_b, alpha=1.0):
    state_A = binary_states[asset_a].values
    state_B = binary_states[asset_b].values
    N = len(state_A)
    
    n_ij = np.zeros((2, 2))
    for t in range(N):
        n_ij[int(state_A[t]), int(state_B[t])] += 1
    prob_joint = (n_ij + alpha) / (N + 4 * alpha)
    
    rho_LF = np.diag(prob_joint.flatten())
    rho_L = np.diag(prob_joint.sum(axis=1))
    rho_F = np.diag(prob_joint.sum(axis=0))
    
    def von_neumann_entropy(rho):
        eigenvalues = np.real(la.eigvalsh(rho))
        eigenvalues = eigenvalues[eigenvalues > 1e-12]
        return -np.sum(eigenvalues * np.log(eigenvalues))
    
    S_LF = von_neumann_entropy(rho_LF)
    S_L = von_neumann_entropy(rho_L)
    S_F = von_neumann_entropy(rho_F)
    
    qmi = S_L + S_F - S_LF
    return qmi

def build_hamiltonian(h, J, n_assets, K=2, penalty_A=10.0):
    coeffs = []
    obs = []
    
    for i in range(n_assets):
        if abs(h[i]) > 1e-10:
            coeffs.append(float(h[i]))
            obs.append(qml.PauliZ(i))
    
    for i in range(n_assets):
        for j in range(i + 1, n_assets):
            if abs(J[i, j]) > 1e-10:
                coeffs.append(float(J[i, j]))
                obs.append(qml.PauliZ(i) @ qml.PauliZ(j))
    
    N_half_minus_K = n_assets / 2.0 - K
    const_val = penalty_A * (N_half_minus_K**2 + n_assets / 4.0)
    coeffs.append(float(const_val))
    obs.append(qml.Identity(0))
    
    for i in range(n_assets):
        coeff = -penalty_A * N_half_minus_K
        coeffs.append(float(coeff))
        obs.append(qml.PauliZ(i))
    
    for i in range(n_assets):
        for j in range(i + 1, n_assets):
            coeffs.append(float(penalty_A * 0.5))
            obs.append(qml.PauliZ(i) @ qml.PauliZ(j))
    
    H = qml.Hamiltonian(coeffs, obs)
    return H

def solve_vqe(H, n_qubits, K=2, depth=2, maxiter=100, n_shots=4096, seed=42):
    dev = qml.device("default.qubit", wires=n_qubits)
    
    @qml.qnode(dev)
    def cost_circuit(params):
        weights = params.reshape((depth + 1, n_qubits, 2))
        for layer in range(depth + 1):
            for q in range(n_qubits):
                qml.RY(weights[layer, q, 0], wires=q)
                qml.RZ(weights[layer, q, 1], wires=q)
            if layer < depth:
                for q in range(n_qubits):
                    qml.CNOT(wires=[q, (q + 1) % n_qubits])
        return qml.expval(H)

    rng = np.random.default_rng(seed)
    n_params = n_qubits * 2 * (depth + 1)
    params = rng.uniform(0, 2 * np.pi, n_params)
    
    initial_cost = float(cost_circuit(params))
    # Adapted SPSA from notebook
    a = 0.1 * max(1.0, abs(initial_cost))
    c = 0.10
    A = maxiter * 0.1
    alpha = 0.602
    gamma = 0.101
    
    for k in range(maxiter):
        a_k = a / (A + k + 1) ** alpha
        c_k = c / (k + 1) ** gamma
        
        delta = 2 * rng.integers(0, 2, size=n_params) - 1
        
        cost_plus = float(cost_circuit(params + c_k * delta))
        cost_minus = float(cost_circuit(params - c_k * delta))
        
        grad = (cost_plus - cost_minus) / (2 * c_k * delta)
        
        params = params - a_k * grad

    dev_sample = qml.device("default.qubit", wires=n_qubits, shots=n_shots)
    
    @qml.qnode(dev_sample)
    def sample_circuit(params):
        weights = params.reshape((depth + 1, n_qubits, 2))
        for layer in range(depth + 1):
            for q in range(n_qubits):
                qml.RY(weights[layer, q, 0], wires=q)
                qml.RZ(weights[layer, q, 1], wires=q)
            if layer < depth:
                for q in range(n_qubits):
                    qml.CNOT(wires=[q, (q + 1) % n_qubits])
        return qml.probs(wires=range(n_qubits))

    probs = sample_circuit(params)
    
    best_bitstring = None
    best_prob = -1.0
    
    for i, p in enumerate(probs):
        bitstring = format(i, f'0{n_qubits}b')
        if bitstring.count('1') == K:
            if p > best_prob:
                best_prob = p
                best_bitstring = bitstring
                
    if best_bitstring is None:
        best_bitstring = "0011"

    selected_indices = [i for i, bit in enumerate(best_bitstring) if bit == '1']
    return selected_indices

def run_strategy_step(lookback_data, tickers, K=2, penalty_A=10.0):
    log_rets = np.log(lookback_data / lookback_data.shift(1)).dropna()
    binary_sts = (log_rets <= 0).astype(int)
    
    lam = compute_endogenous_lambda(log_rets, tickers)
    
    all_payoffs = {}
    game_counts = {"Coordination": 0, "Anti-Coordination": 0, "Mixed": 0}
    
    pairs = list(combinations(range(len(tickers)), 2))
    for idx_a, idx_b in pairs:
        a, b = tickers[idx_a], tickers[idx_b]
        pA, pB = compute_markowitz_payoff_matrix(log_rets, binary_sts, a, b, lam)
        all_payoffs[(idx_a, idx_b)] = (pA, pB)
        
        gtype = classify_game_type(pA, pB)
        if "Coordination" in gtype and "Anti" not in gtype:
            game_counts["Coordination"] += 1
        elif "Anti-Coordination" in gtype:
            game_counts["Anti-Coordination"] += 1
        else:
            game_counts["Mixed"] += 1
            
    dominant = max(game_counts, key=game_counts.get)
    print(f"  [{lookback_data.index[-1]}] Market Phase: {dominant} (λ={lam:.4f})")
    print(f"  Game Counts: {game_counts}")
        
    h = compute_bias_hi(all_payoffs, tickers)
    
    J = np.zeros((len(tickers), len(tickers)))
    for i in range(len(tickers)):
        for j in range(i + 1, len(tickers)):
            qmi = compute_qmi_jij(binary_sts, tickers[i], tickers[j])
            J[i, j] = qmi
            J[j, i] = qmi
            
    H = build_hamiltonian(h, J, n_assets=len(tickers), K=K, penalty_A=penalty_A)
    selected_indices = solve_vqe(H, n_qubits=len(tickers), K=K, maxiter=20) # Short iter for test
    
    return selected_indices

# === Test Execution ===
if __name__ == "__main__":
    print("Generating synthetic data...")
    dates = pd.date_range(start="2023-01-01", periods=100, freq='D')
    tickers = ['A', 'B', 'C', 'D']
    data = pd.DataFrame(np.random.randn(100, 4) * 0.01 + 1.0005, index=dates, columns=tickers)
    data = data.cumprod()
    
    print("Running strategy step...")
    selected = run_strategy_step(data, tickers, K=2)
    print(f"Selected indices: {selected}")
    print(f"Selected tickers: {[tickers[i] for i in selected]}")
