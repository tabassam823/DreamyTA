import numpy as np
from itertools import combinations
from quantum_finance import compute_endogenous_lambda, calc_payoff, calc_qmi, build_hamiltonian
from vqe_solver import run_vqe_spsa_pennylane

def run_strategy_step(lookback_data, tickers, K=2, penalty_A=5.0, depth=1, maxiter=100):
    log_rets = np.log(lookback_data / lookback_data.shift(1)).dropna()
    binary_sts = (log_rets <= 0).astype(int)
    
    lam = compute_endogenous_lambda(log_rets, tickers)
    
    all_payoffs = {}
    pairs = list(combinations(range(len(tickers)), 2))
    
    for idx_a, idx_b in pairs:
        a, b = tickers[idx_a], tickers[idx_b]
        pA, pB = calc_payoff(log_rets[a].values, log_rets[b].values, 
                             binary_sts[a].values, binary_sts[b].values, lam)
        all_payoffs[(idx_a, idx_b)] = (pA, pB)
        
    n_assets = len(tickers)
    h = np.zeros(n_assets)
    for i in range(n_assets):
        payoff_sum, count = 0, 0
        for (a, b), (pA, pB) in all_payoffs.items():
            if a == i:
                payoff_sum += (pA[1, 0] + pA[1, 1]) - (pA[0, 0] + pA[0, 1])
                count += 1
            elif b == i:
                payoff_sum += (pB[0, 1] + pB[1, 1]) - (pB[0, 0] + pB[1, 0])
                count += 1
        if count > 0: h[i] = payoff_sum / count

    J = np.zeros((len(tickers), len(tickers)))
    for i in range(len(tickers)):
        for j in range(i + 1, len(tickers)):
            qmi = calc_qmi(binary_sts[tickers[i]].values, binary_sts[tickers[j]].values)
            J[i, j] = qmi
            J[j, i] = qmi

    H = build_hamiltonian(h, J, n_assets, K, penalty_A)
    selected_indices = run_vqe_spsa_pennylane(H, n_assets, K, depth, maxiter)
    
    return selected_indices
