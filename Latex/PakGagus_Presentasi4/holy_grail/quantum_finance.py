import numpy as np
import scipy.linalg as la
import pennylane as qml
from itertools import combinations

def compute_endogenous_lambda(log_returns, tickers):
    mu_annual = log_returns[tickers].mean() * 252
    sigma_annual = log_returns[tickers].std() * np.sqrt(252)
    mu_avg = abs(mu_annual).mean()
    sigma_avg = sigma_annual.mean()
    if np.isnan(mu_avg) or np.isnan(sigma_avg) or (mu_avg + sigma_avg) == 0:
        return 0.5, mu_annual, sigma_annual, mu_avg, sigma_avg
    # Sigmoid / Logistic function based on Sharpe Ratio
    Z = mu_avg / sigma_avg
    lam = 1.0 / (1.0 + np.exp(Z))
    return lam, mu_annual, sigma_annual, mu_avg, sigma_avg

def calc_payoff(ret_A, ret_B, st_A, st_B, lam):
    pA, pB, counts = np.zeros((2, 2)), np.zeros((2, 2)), np.zeros((2, 2))
    for t in range(len(st_A)):
        i, j = int(st_A[t]), int(st_B[t])
        counts[i, j] += 1
        u_A = (1 - lam) * (ret_A[t] * 252) - lam * abs(ret_A[t] * 252)
        u_B = (1 - lam) * (ret_B[t] * 252) - lam * abs(ret_B[t] * 252)
        pA[i, j] += u_A
        pB[i, j] += u_B
    for i in range(2):
        for j in range(2):
            if counts[i, j] > 0:
                pA[i, j] /= counts[i, j]
                pB[i, j] /= counts[i, j]
    return pA, pB

def calc_qmi(st_A, st_B):
    n_ij = np.zeros((2, 2))
    for t in range(len(st_A)):
        n_ij[int(st_A[t]), int(st_B[t])] += 1
    prob_joint = (n_ij + 1.0) / (len(st_A) + 4.0)
    rho_LF = np.diag(prob_joint.flatten())
    rho_L = np.diag(prob_joint.sum(axis=1))
    rho_F = np.diag(prob_joint.sum(axis=0))
    def svn(rho):
        eig = np.real(la.eigvalsh(rho))
        eig = eig[eig > 1e-12]
        return -np.sum(eig * np.log(eig))
    
    sL, sF, sLF = svn(rho_L), svn(rho_F), svn(rho_LF)
    qmi = sL + sF - sLF
    return qmi, rho_L, rho_F, rho_LF, sL, sF, sLF, prob_joint

def build_hamiltonian(h, J, n_assets, K=2, penalty_A=5.0):
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
                
    coeffs.append(float(penalty_A))
    obs.append(qml.Identity(0)) 
    
    for pair in combinations(range(n_assets), 2):
        coeffs.append(float(penalty_A / 2))
        obs.append(qml.PauliZ(pair[0]) @ qml.PauliZ(pair[1]))
        
    return qml.Hamiltonian(coeffs, obs)
