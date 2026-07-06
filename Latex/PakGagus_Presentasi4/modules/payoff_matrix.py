
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from itertools import combinations

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
    """Calculate Markowitz payoff matrix 2x2 for a pair of assets."""
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
        # Utility = (1-λ)µ - λσ
        # Using daily return as proxy for mu (scaled) and abs(return) for risk
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
    """Classify game type based on payoff structure."""
    # Coordination: (0,0) > (1,0) and (1,1) > (0,1) for A, etc.
    # Nash Equilibrium check essentially
    coord_A = (payoff_A[0, 0] > payoff_A[1, 0]) and (payoff_A[1, 1] > payoff_A[0, 1])
    coord_B = (payoff_B[0, 0] > payoff_B[0, 1]) and (payoff_B[1, 1] > payoff_B[1, 0])
    
    if coord_A and coord_B:
        return "Coordination Game"
    elif (not coord_A) and (not coord_B):
        return "Anti-Coordination Game"
    else:
        return "Mixed Strategy Game"

def generate_payoff_visualizations(all_payoffs, output_dir="generated_images"):
    """Generates heatmaps for payoff matrices."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    for (a_idx, b_idx), (pA, pB) in all_payoffs.items():
        # Create a combined heatmap or side-by-side
        fig, axes = plt.subplots(1, 2, figsize=(10, 4))
        
        sns.heatmap(pA, annot=True, cmap="RdBu", center=0, ax=axes[0])
        axes[0].set_title(f"Payoff Matrix Asset {a_idx}")
        axes[0].set_xlabel("Asset B State")
        axes[0].set_ylabel("Asset A State")
        axes[0].set_xticklabels(["Up", "Down"]) # 0=Up, 1=Down
        axes[0].set_yticklabels(["Up", "Down"])
        
        sns.heatmap(pB, annot=True, cmap="RdBu", center=0, ax=axes[1])
        axes[1].set_title(f"Payoff Matrix Asset {b_idx}")
        axes[1].set_xlabel("Asset B State")
        axes[1].set_ylabel("Asset A State")
        
        plt.suptitle(f"Payoff Matrices: {a_idx} vs {b_idx}")
        plt.tight_layout()
        plt.savefig(f"{output_dir}/payoff_matrix_{a_idx}_{b_idx}.png")
        plt.close()
    
    print(f"Payoff visualizations saved to {output_dir}")

def run_payoff_analysis(log_returns, binary_states, tickers):
    lam = compute_endogenous_lambda(log_returns, tickers)
    print(f"Computed Endogenous Lambda: {lam:.4f}")
    
    all_payoffs = {}
    game_counts = {"Coordination": 0, "Anti-Coordination": 0, "Mixed": 0}
    
    pairs = list(combinations(range(len(tickers)), 2))
    
    for idx_a, idx_b in pairs:
        a, b = tickers[idx_a], tickers[idx_b]
        pA, pB = compute_markowitz_payoff_matrix(log_returns, binary_states, a, b, lam)
        all_payoffs[(idx_a, idx_b)] = (pA, pB) # Storing by index for easier matrix indexing later
        all_payoffs[(tickers[idx_a], tickers[idx_b])] = (pA, pB) # Also store by ticker name if needed

        gtype = classify_game_type(pA, pB)
        print(f"Pair {a} vs {b}: {gtype}")
        
        if "Coordination" in gtype and "Anti" not in gtype:
            game_counts["Coordination"] += 1
        elif "Anti-Coordination" in gtype:
            game_counts["Anti-Coordination"] += 1
        else:
            game_counts["Mixed"] += 1
            
    return all_payoffs, game_counts, lam

if __name__ == "__main__":
    # Test execution
    import data_analysis # Import local module
    
    TICKERS = ['BBCA.JK', 'ASII.JK', 'TLKM.JK', 'TPIA.JK']
    START_DATE = "2025-01-06"
    END_DATE = "2026-01-06"
    OUTPUT_DIR = "generated_images"
    
    data = data_analysis.download_data(TICKERS, START_DATE, END_DATE)
    log_returns = data_analysis.calculate_log_returns(data)
    binary_states = (log_returns <= 0).astype(int)
    
    all_payoffs, game_counts, lam = run_payoff_analysis(log_returns, binary_states, TICKERS)
    
    # Filter keys to only pass index-based keys to visualization to avoid duplicates
    index_payoffs = {k: v for k, v in all_payoffs.items() if isinstance(k[0], int)}
    generate_payoff_visualizations(index_payoffs, OUTPUT_DIR)
