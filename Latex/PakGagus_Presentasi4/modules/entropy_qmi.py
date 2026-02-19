
import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt
import seaborn as sns
import os

def compute_qmi_jij(binary_states, asset_a, asset_b, alpha=1.0):
    """Calculate Quantum Mutual Information (QMI) as J_ij."""
    state_A = binary_states[asset_a].values
    state_B = binary_states[asset_b].values
    N = len(state_A)
    
    n_ij = np.zeros((2, 2))
    for t in range(N):
        n_ij[int(state_A[t]), int(state_B[t])] += 1
    
    # Regularization with alpha
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

def compute_all_qmi(binary_states, tickers):
    """Computes QMI matrix for all pairs."""
    n_assets = len(tickers)
    J = np.zeros((n_assets, n_assets))
    
    for i in range(n_assets):
        for j in range(i + 1, n_assets):
            qmi = compute_qmi_jij(binary_states, tickers[i], tickers[j])
            J[i, j] = qmi
            J[j, i] = qmi # Symmetric
            
    return J

# generate illustration
def generate_qmi_visualization(J, tickers, output_dir="generated_images"):
    """Generates heatmap for QMI Matrix."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    plt.figure(figsize=(8, 6))
    sns.heatmap(J, annot=True, xticklabels=tickers, yticklabels=tickers, cmap="viridis")
    plt.title("Quantum Mutual Information (J Matrix)")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/qmi_heatmap.png")
    plt.close()
    print(f"QMI visualization saved to {output_dir}")

if __name__ == "__main__":
    import data_analysis
    
    TICKERS = ['BBCA.JK', 'ASII.JK', 'TLKM.JK', 'TPIA.JK']
    START_DATE = "2025-01-06"
    END_DATE = "2026-01-06"
    OUTPUT_DIR = "generated_images"

    data = data_analysis.download_data(TICKERS, START_DATE, END_DATE)
    log_returns = data_analysis.calculate_log_returns(data)
    binary_states = (log_returns <= 0).astype(int)
    
    J = compute_all_qmi(binary_states, TICKERS)
    generate_qmi_visualization(J, TICKERS, OUTPUT_DIR)
