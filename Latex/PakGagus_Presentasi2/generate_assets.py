import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf
import pennylane as qml

# Konfigurasi sesuai VQE_2.ipynb
TICKERS = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA"]
START_DATE = "2020-01-01"
END_DATE = "2021-01-01"
W = 0.5
B = 2
P = 10.0
N_LAYERS = 3
MAX_ITERATIONS = 100
STEPSIZE = 0.1
SEED = 0

# 1. Visualisasi Risk vs Return (Konseptual)
def plot_risk_return():
    np.random.seed(42)
    returns = np.linspace(0.05, 0.25, 100)
    risks = 0.1 + 2 * (returns - 0.05)**2 + 0.02 * np.random.normal(0, 0.1, 100)
    
    plt.figure(figsize=(8, 6))
    plt.plot(risks, returns, 'b-', label='Efficient Frontier', linewidth=2)
    plt.scatter(risks + np.random.rand(100)*0.1, returns - np.random.rand(100)*0.05, c='gray', alpha=0.5, s=10, label='Feasible Portfolios')
    
    plt.title("Konsep: Risk vs Return (Efficient Frontier)")
    plt.xlabel("Risk (Standard Deviation)")
    plt.ylabel("Expected Return")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.savefig("risk_vs_return.png")
    print("Saved 'risk_vs_return.png'")
    plt.close()

# 2. Visualisasi Data (Covariance Matrix & Expected Returns)
def plot_data_visuals():
    print(f"Fetching data for {TICKERS}...")
    try:
        # Menggunakan auto_adjust=False agar sesuai dengan notebook jika memungkinkan
        data = yf.download(TICKERS, start=START_DATE, end=END_DATE, progress=False, auto_adjust=False)
        df = data['Adj Close']
    except Exception as e:
        print(f"Error fetching data: {e}. Generating dummy data.")
        dates = pd.date_range(start=START_DATE, end=END_DATE)
        df = pd.DataFrame(np.random.randn(len(dates), len(TICKERS)) * 0.01 + 1.0, index=dates, columns=TICKERS)

    returns = df.pct_change().dropna()
    mu = returns.mean().to_numpy()
    sigma = returns.cov().to_numpy()
    
    # Plot Expected Returns
    plt.figure(figsize=(8, 5))
    pd.Series(mu, index=TICKERS).plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title("Expected Daily Returns (Replikasi)")
    plt.ylabel("Mean Return")
    plt.xticks(rotation=0)
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.savefig("expected_returns.png")
    print("Saved 'expected_returns.png'")
    plt.close()
    
    # Plot Covariance Matrix
    plt.figure(figsize=(8, 6))
    plt.imshow(sigma, cmap='coolwarm', interpolation='nearest')
    plt.colorbar(label='Covariance')
    plt.xticks(range(len(TICKERS)), TICKERS)
    plt.yticks(range(len(TICKERS)), TICKERS)
    plt.title("Covariance Matrix Heatmap (Replikasi)")
    for i in range(len(TICKERS)):
        for j in range(len(TICKERS)):
            plt.text(j, i, f"{sigma[i, j]:.4f}", ha="center", va="center", color="black", fontsize=8)
    plt.savefig("covariance_matrix.png")
    print("Saved 'covariance_matrix.png'")
    plt.close()
    
    return mu, sigma

# 3. & 4. VQE Simulation for Convergence & Probabilities
def run_vqe_visuals(mu, sigma):
    N = len(TICKERS)
    coeffs, ops = [], []
    
    # Hamiltonian Construction sesuai logic notebook
    for i in range(N):
        coeff_x = -(1-W) * mu[i] + W * sigma[i,i] + P * (1 - 2*B)
        coeffs.extend([0.5 * coeff_x, -0.5 * coeff_x])
        ops.extend([qml.Identity(i), qml.PauliZ(i)])
        for j in range(i+1, N):
            coeff_xx = 2 * W * sigma[i,j] + 2 * P
            coeffs.extend([0.25*coeff_xx, -0.25*coeff_xx, -0.25*coeff_xx, 0.25*coeff_xx])
            ops.extend([qml.Identity(0), qml.PauliZ(i), qml.PauliZ(j), qml.PauliZ(i)@qml.PauliZ(j)])
    coeffs.append(P * B**2)
    ops.append(qml.Identity(0))
    H = qml.Hamiltonian(coeffs, ops)
    
    dev = qml.device("default.qubit", wires=N)
    def ansatz(params, wires):
        qml.BasicEntanglerLayers(weights=params, wires=wires)
        
    @qml.qnode(dev)
    def cost_function(params):
        ansatz(params, wires=range(N))
        return qml.expval(H)
    
    shape = qml.BasicEntanglerLayers.shape(n_layers=N_LAYERS, n_wires=N)
    np.random.seed(SEED)
    params = np.random.random(shape)
    opt = qml.GradientDescentOptimizer(stepsize=STEPSIZE)
    
    costs = []
    print(f"Running VQE optimization ({MAX_ITERATIONS} iterations)...")
    for i in range(MAX_ITERATIONS):
        params, cost = opt.step_and_cost(cost_function, params)
        costs.append(cost)
        if i % 20 == 0:
            print(f"Step {i}: Cost = {cost}")
            
    # Plot Convergence
    plt.figure(figsize=(8, 5))
    plt.plot(costs, 'b-')
    plt.title("VQE Optimization Convergence (Replikasi)")
    plt.xlabel("Iterations")
    plt.ylabel("Cost")
    plt.grid(True, alpha=0.3)
    plt.savefig("vqe_convergence.png")
    print("Saved 'vqe_convergence.png'")
    plt.close()
    
    # Plot Probabilities
    @qml.qnode(dev)
    def probability_circuit(params):
        ansatz(params, wires=range(N))
        return qml.probs(wires=range(N))
        
    probs = probability_circuit(params)
    
    plt.figure(figsize=(10, 5))
    plt.bar([format(i, f'0{N}b') for i in range(2**N)], probs, color='purple')
    plt.title("Final State Probabilities (Replikasi)")
    plt.xlabel("Portfolio State (Binary)")
    plt.ylabel("Probability")
    plt.xticks(rotation=90)
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig("probability_histogram.png")
    print("Saved 'probability_histogram.png'")
    plt.close()

if __name__ == "__main__":
    plot_risk_return()
    mu, sigma = plot_data_visuals()
    run_vqe_visuals(mu, sigma)
    print("\nAll assets generated successfully matching VQE_2.ipynb parameters!")