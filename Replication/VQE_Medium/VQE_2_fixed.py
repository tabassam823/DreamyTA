import pennylane as qml
from pennylane import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Data Preparation
tickers = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA"] # 5 Assets
start_date = "2020-01-01"
end_date = "2021-01-01"

def get_data(tickers, start, end):
    # Fixed yfinance download to avoid errors if any
    data = yf.download(tickers, start=start, end=end, progress=False)
    
    # Handle MultiIndex columns (Price, Ticker)
    # Check if 'Adj Close' is in the top level (Price)
    if 'Adj Close' in data.columns.levels[0]:
        return data['Adj Close']
    elif 'Close' in data.columns.levels[0]:
        print("Warning: 'Adj Close' not found, using 'Close' prices.")
        return data['Close']
    else:
        # Fallback for flat index or other structures
        if 'Adj Close' in data.columns:
            return data['Adj Close']
        elif 'Close' in data.columns:
            return data['Close']
        else:
             raise ValueError(f"Could not find price data. Available columns: {data.columns}")

print("Fetching data...")
# Fetch data
df = get_data(tickers, start_date, end_date)
print(df.head())

# Calculate Daily Returns
returns = df.pct_change().dropna()

# Expected Return (Mean) and Covariance Matrix
mu = returns.mean().to_numpy()
sigma = returns.cov().to_numpy()

print("Expected Returns (mu):", mu)
print("Covariance Matrix (sigma):\n", sigma)

# Hamiltonian Construction
w = 0.5
B = 2
P = 10.0 # Penalty weight
N = len(tickers)

def build_hamiltonian(mu, sigma, w, B, P):
    # full_hamiltonian = qml.Hamiltonian([], []) # Initialize empty
    # PennyLane Hamiltonian initialization might behave differently in newer versions if empty.
    # We will accumulate terms in lists and create it at the end.
    coeffs = []
    ops = []
    
    # Linear terms (x_i)
    for i in range(N):
        coeff_x = -(1-w) * mu[i] + w * sigma[i,i] + P * (1 - 2*B)
        # x_i = 0.5 * I - 0.5 * Z_i
        # Term 1: 0.5 * coeff_x * I
        coeffs.append(0.5 * coeff_x)
        ops.append(qml.Identity(i))
        # Term 2: -0.5 * coeff_x * Z_i
        coeffs.append(-0.5 * coeff_x)
        ops.append(qml.PauliZ(i))

    # Quadratic terms (x_i x_j)
    for i in range(N):
        for j in range(i+1, N):
            coeff_xx = 2 * w * sigma[i,j] + 2 * P
            # x_i x_j = 0.25 (I - Z_i - Z_j + Z_i Z_j)
            
            # Term 1: 0.25 * coeff_xx * I (Global identity, can map to wire 0 or any)
            coeffs.append(0.25 * coeff_xx)
            ops.append(qml.Identity(0))
            
            # Term 2: -0.25 * coeff_xx * Z_i
            coeffs.append(-0.25 * coeff_xx)
            ops.append(qml.PauliZ(i))
            
            # Term 3: -0.25 * coeff_xx * Z_j
            coeffs.append(-0.25 * coeff_xx)
            ops.append(qml.PauliZ(j))
            
            # Term 4: 0.25 * coeff_xx * Z_i Z_j
            coeffs.append(0.25 * coeff_xx)
            ops.append(qml.PauliZ(i) @ qml.PauliZ(j))
            
    # Constant term from Penalty B^2 (P * B^2)
    coeffs.append(P * B**2)
    ops.append(qml.Identity(0))
    
    return qml.Hamiltonian(coeffs, ops)

print("Building Hamiltonian...")
H = build_hamiltonian(mu, sigma, w, B, P)
print("Hamiltonian defined with terms:", len(H.ops))

# VQE
dev = qml.device("default.qubit", wires=N)

# Define the ansatz
def ansatz(params, wires):
    qml.BasicEntanglerLayers(weights=params, wires=wires)

@qml.qnode(dev)
def cost_function(params):
    ansatz(params, wires=range(N))
    return qml.expval(H)

# Initialize parameter shapes
shape = qml.BasicEntanglerLayers.shape(n_layers=3, n_wires=N)
np.random.seed(0)
params = np.random.random(shape)

print("Starting Optimization...")
opt = qml.GradientDescentOptimizer(stepsize=0.1)
max_iterations = 20 # Reduced for quick check
costs = []

for i in range(max_iterations):
    params, cost = opt.step_and_cost(cost_function, params)
    costs.append(cost)
    if i % 5 == 0:
        print(f"Step {i}: Cost = {cost}")

print(f"Final Cost: {costs[-1]}")

# Results Analysis
@qml.qnode(dev)
def probability_circuit(params):
    ansatz(params, wires=range(N))
    return qml.probs(wires=range(N))

probs = probability_circuit(params)
max_prob_idx = np.argmax(probs)
binary_string = format(max_prob_idx, f'0{N}b')

print("Optimal State (Binary):", binary_string)
print("Selected Assets:", [tickers[i] for i, bit in enumerate(binary_string) if bit == '1'])
