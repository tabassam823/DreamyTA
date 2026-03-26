import numpy as np

def compute_endogenous_lambda(log_returns, tickers):
    mu_annual    = log_returns[tickers].mean() * 252
    sigma_annual = log_returns[tickers].std()  * np.sqrt(252)
    mu_avg    = abs(mu_annual).mean()
    sigma_avg = sigma_annual.mean()
    if np.isnan(mu_avg) or np.isnan(sigma_avg) or (mu_avg + sigma_avg) == 0:
        return 0.5
    Z = mu_avg / sigma_avg
    return 1.0 / (1.0 + np.exp(Z))

def compute_strategic_returns(log_rets, binary_st, tickers):
    n_assets = len(tickers)
    total_days = len(log_rets)
    mu_tilde = np.zeros(n_assets)
    
    grouped = log_rets.groupby([binary_st[t] for t in tickers])
    for state, group in grouped:
        P_s = len(group) / total_days
        R_bar_s = group[tickers].mean().values
        mu_tilde += P_s * R_bar_s
        
    return mu_tilde

def calc_shannon_entropy(st_A):
    p1 = np.mean(st_A)
    p0 = 1.0 - p1
    H = 0.0
    if p0 > 0: H -= p0 * np.log2(p0)
    if p1 > 0: H -= p1 * np.log2(p1)
    return H

def calc_classical_mutual_information(st_A, st_B):
    n_ij = np.zeros((2, 2))
    for t in range(len(st_A)):
        n_ij[int(st_A[t]), int(st_B[t])] += 1
    
    prob_joint = n_ij / len(st_A)
    prob_A = prob_joint.sum(axis=1)
    prob_B = prob_joint.sum(axis=0)
    
    I_MI = 0.0
    for i in range(2):
        for j in range(2):
            if prob_joint[i, j] > 0:
                I_MI += prob_joint[i, j] * np.log2(prob_joint[i, j] / (prob_A[i] * prob_B[j]))
    return max(I_MI, 0.0)

def calc_NMI(st_A, st_B):
    I_AB = calc_classical_mutual_information(st_A, st_B)
    H_A = calc_shannon_entropy(st_A)
    H_B = calc_shannon_entropy(st_B)
    if H_A == 0 or H_B == 0:
        return 0.0
    return I_AB / np.sqrt(H_A * H_B)
