import pandas as pd
import numpy as np
import sys
import os

# Add parent directory to sys.path
sys.path.append(os.path.abspath('GTQuantumInvest'))
from compute_metrics import compute_metrics

initial_capital = 100_000_000.0

for n in [2, 4]:
    file_path = f"GTQuantumInvest/classic_compare/Hasil_Classic_Compare/equity_history_classic_N{n}.csv"
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        print(f"\nProcessing N={n} from {file_path}")
        compute_metrics(df['Equity'], initial_capital, label=f"Classic SLSQP N={n}")
    else:
        print(f"File not found: {file_path}")
