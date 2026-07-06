import numpy as np
import pandas as pd
from itertools import combinations
from quantum_finance import compute_endogenous_lambda, calc_payoff, calc_qmi, build_hamiltonian
from vqe_solver import run_vqe_spsa_pennylane

def run_strategy_step(lookback_data, tickers, K=2, penalty_A=5.0, depth=1, maxiter=100, curr_date=None, is_first_decision=False):
    log_rets = np.log(lookback_data / lookback_data.shift(1)).dropna()
    binary_sts = (log_rets <= 0).astype(int)
    
    lam, mu_annual, sigma_annual, mu_avg, sigma_avg = compute_endogenous_lambda(log_rets, tickers)
    
    if curr_date is not None:
        pd.DataFrame([{
            'Date': curr_date, 'Lambda': lam,
            'Mu_Avg': mu_avg, 'Sigma_Avg': sigma_avg
        }]).to_csv('lambda_history.csv', mode='w' if is_first_decision else 'a', header=is_first_decision, index=False)
        
        asset_stats = []
        for t in tickers:
            asset_stats.append({
                'Date': curr_date, 'Asset': t,
                'Mu_Annual': mu_annual[t], 'Sigma_Annual': sigma_annual[t]
            })
        pd.DataFrame(asset_stats).to_csv('asset_stats_history.csv', mode='w' if is_first_decision else 'a', header=is_first_decision, index=False)
    
    all_payoffs = {}
    pairs = list(combinations(range(len(tickers)), 2))
    
    for idx_a, idx_b in pairs:
        a, b = tickers[idx_a], tickers[idx_b]
        pA, pB = calc_payoff(log_rets[a].values, log_rets[b].values, 
                             binary_sts[a].values, binary_sts[b].values, lam)
        all_payoffs[(idx_a, idx_b)] = (pA, pB)
        
    if curr_date is not None:
        payoff_records = []
        for (idx_a, idx_b), (pA, pB) in all_payoffs.items():
            payoff_records.append({
                'Date': curr_date, 'Asset_A': tickers[idx_a], 'Asset_B': tickers[idx_b],
                'pA_00': pA[0,0], 'pA_01': pA[0,1], 'pA_10': pA[1,0], 'pA_11': pA[1,1],
                'pB_00': pB[0,0], 'pB_01': pB[0,1], 'pB_10': pB[1,0], 'pB_11': pB[1,1]
            })
        pd.DataFrame(payoff_records).to_csv('payoff_history.csv', mode='w' if is_first_decision else 'a', header=is_first_decision, index=False)
        
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

    if curr_date is not None:
        h_records = [{'Date': curr_date, 'Asset': tickers[i], 'h_value': h[i]} for i in range(n_assets)]
        pd.DataFrame(h_records).to_csv('h_history.csv', mode='w' if is_first_decision else 'a', header=is_first_decision, index=False)

    J = np.zeros((len(tickers), len(tickers)))
    rho_records = []
    svn_records = []
    prob_joint_records = []
    
    for i in range(len(tickers)):
        for j in range(i + 1, len(tickers)):
            qmi, rho_L, rho_F, rho_LF, sL, sF, sLF, prob_joint = calc_qmi(binary_sts[tickers[i]].values, binary_sts[tickers[j]].values)
            J[i, j] = qmi
            J[j, i] = qmi
            
            if curr_date is not None:
                rho_records.append({
                    'Date': curr_date, 'Asset_A': tickers[i], 'Asset_B': tickers[j],
                    'rho_L_0': float(np.real(rho_L[0,0])), 'rho_L_1': float(np.real(rho_L[1,1])),
                    'rho_F_0': float(np.real(rho_F[0,0])), 'rho_F_1': float(np.real(rho_F[1,1])),
                    'rho_LF_00': float(np.real(rho_LF[0,0])), 'rho_LF_01': float(np.real(rho_LF[1,1])),
                    'rho_LF_10': float(np.real(rho_LF[2,2])), 'rho_LF_11': float(np.real(rho_LF[3,3]))
                })
                
                svn_records.append({
                    'Date': curr_date, 'Asset_A': tickers[i], 'Asset_B': tickers[j],
                    'svn_rho_L': float(sL), 'svn_rho_F': float(sF), 'svn_rho_LF': float(sLF)
                })
                
                prob_joint_records.append({
                    'Date': curr_date, 'Asset_A': tickers[i], 'Asset_B': tickers[j],
                    'prob_00': float(np.real(prob_joint[0,0])), 'prob_01': float(np.real(prob_joint[0,1])),
                    'prob_10': float(np.real(prob_joint[1,0])), 'prob_11': float(np.real(prob_joint[1,1]))
                })

    if curr_date is not None:
        pd.DataFrame(rho_records).to_csv('rho_history.csv', mode='w' if is_first_decision else 'a', header=is_first_decision, index=False)
        pd.DataFrame(svn_records).to_csv('svn_history.csv', mode='w' if is_first_decision else 'a', header=is_first_decision, index=False)
        pd.DataFrame(prob_joint_records).to_csv('prob_joint_history.csv', mode='w' if is_first_decision else 'a', header=is_first_decision, index=False)

    if curr_date is not None:
        qmi_records = []
        for i in range(len(tickers)):
            for j in range(i + 1, len(tickers)):
                qmi_records.append({'Date': curr_date, 'Asset_A': tickers[i], 'Asset_B': tickers[j], 'QMI': J[i,j], 'J_value': J[i,j]})
        pd.DataFrame(qmi_records).to_csv('qmi_history.csv', mode='w' if is_first_decision else 'a', header=is_first_decision, index=False)
        pd.DataFrame(qmi_records).drop(columns=['QMI']).to_csv('J_history.csv', mode='w' if is_first_decision else 'a', header=is_first_decision, index=False)

    H = build_hamiltonian(h, J, n_assets, K, penalty_A)
    
    if curr_date is not None:
        hamiltonian_records = []
        for coeff, term in zip(H.coeffs, H.ops):
            hamiltonian_records.append({'Date': curr_date, 'Coefficient': float(coeff), 'Term': term.name if hasattr(term, 'name') else str(term)})
        pd.DataFrame(hamiltonian_records).to_csv('hamiltonian_history.csv', mode='w' if is_first_decision else 'a', header=is_first_decision, index=False)

    selected_indices = run_vqe_spsa_pennylane(H, n_assets, K, depth, maxiter, export_convergence=is_first_decision)
    
    return selected_indices
