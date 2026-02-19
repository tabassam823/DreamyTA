
import sys
import os
import pandas as pd
import numpy as np
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings("ignore")

# Ensure modules are importable
sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))

import modules.data_analysis as da
import modules.payoff_matrix as pm
import modules.entropy_qmi as eq
import modules.hamiltonian as ham
import modules.vqe_optimization as vqe
# import modules.vqe_adam as vqe_adam
import modules.backtest as bt

def run_analysis_pipeline(window_data:np.array, tickers:list[str], K:int=2):
    """
    Runs the full quantum-classical pipeline on a slice of data.
    Returns the selected indices (optimal assets).
    """
    if len(window_data) < 20:
        return [] # Not enough data
        
    try:
        # 1. Stats & Preprocessing
        log_returns = da.calculate_log_returns(window_data)
        binary_states = (log_returns <= 0).astype(int)
        
        # 2. Payoff Matrix
        all_payoffs, _, lam = pm.run_payoff_analysis(log_returns, binary_states, tickers)
        
        # 3. Hamiltonian Params
        J = eq.compute_all_qmi(binary_states, tickers)
        h = ham.compute_bias_hi(all_payoffs, tickers)
        
        # 4. Hamiltonian Construction
        H = ham.build_hamiltonian(h, J, len(tickers), K=K)
        
        # 5. VQE Optimization (SPSA)
        # Using SPSA as requested
        params, _ = vqe.run_vqe_spsa(H, n_qubits=len(tickers), K=K, maxiter=100)
        # params, _ = vqe_adam.run_vqe_adam(H, n_qubits=len(tickers), K=K, maxiter=50, stepsize=0.1)
        selected_indices, _, _ = vqe.sample_results(params, len(tickers), K=K)
        # selected_indices, _, _ = vqe_adam.sample_results(params, len(tickers), K=K)
        return selected_indices
        
    except Exception as e:
        print(f"Error in pipeline: {e}")
        return []

def main():
    # Configuration
    TICKERS = ['BBCA.JK', 'ASII.JK', 'TLKM.JK', 'TPIA.JK']
    
    # User Request: 5 years, Jan 6 2021 - Jan 6 2026
    DATA_START = "2021-01-06"
    DATA_END = "2026-01-06"
    
    # Backtest settings
    LOOKBACK_MONTHS = 6 
    LOOKBACK_DAYS = int(LOOKBACK_MONTHS * 21) # approx trading days
    
    OUTPUT_DIR = "generated_images"
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    print(f"=== Downloading Data ({DATA_START} to {DATA_END}) ===")
    data = da.download_data(TICKERS, DATA_START, DATA_END)
    
    # Define Rebalance Schedule
    # Only rebalance where we have enough lookback data
    full_dates = data.index
    if len(full_dates) < LOOKBACK_DAYS:
        print("Not enough data for the requested lookback window.")
        return

    # Start backtest after lookback period
    backtest_start_date = full_dates[LOOKBACK_DAYS]
    print(f"Backtest Start Date (after lookback): {backtest_start_date.date()}")
    
    # Rebalance Monthly
    rebalance_dates = pd.date_range(start=backtest_start_date, end=DATA_END, freq='ME')
    
    # Portfolio Engines
    # We simulate starting with cash at the first rebalance date
    start_idx = data.index.get_loc(backtest_start_date) if backtest_start_date in data.index else data.index.searchsorted(backtest_start_date)
    
    # Ensure start_idx is valid
    if start_idx >= len(data):
        print("Start index out of bounds.")
        return
        
    simulation_data = data.iloc[start_idx:]
    engine_vqe = bt.BacktestEngine(simulation_data)
    engine_bench = bt.BacktestEngine(simulation_data)
    
    # Initial Weights (Equal Weight Benchmark)
    current_weights_bench = np.full(len(TICKERS), 1.0/len(TICKERS))
    
    # To track selections
    selection_log = []
    
    print(f"\n=== Starting Rolling Window Backtest ({len(rebalance_dates)} rebalance events) ===")
    
    # Helper to check if date is a rebalance date (or close to it)
    # Since rebalance_dates might not be trading days, we map to nearest valid logic or simply check monthly transition
    # Valid logic: iterate simulation days. If month changes or date > next_rebalance, rebalance.
    # Simpler: Iterate rebalance_dates, run pipeline, update target weights in engine.
    # The engine needs to step day-by-day to track value.
    
    # Let's verify how BacktestEngine works. It has .step(date, weights) -> rebalances only if called.
    # It also has .portfolio_history.
    # We should iterate DAILY through simulation_data. 
    # If today is a rebalance trigger, run pipeline.
    
    next_rebalance_idx = 0
    
    # Initial VQE Run for the first day
    print(f"Performing Initial Rebalance at {simulation_data.index[0].date()}...")
    lookback_slice = data.loc[:simulation_data.index[0]].iloc[-LOOKBACK_DAYS:]
    sel_indices = run_analysis_pipeline(lookback_slice, TICKERS)
    
    target_weights_vqe = np.zeros(len(TICKERS))
    if sel_indices:
        for i in sel_indices:
            target_weights_vqe[i] = 1.0 / len(sel_indices)
        print(f"Selected: {[TICKERS[i] for i in sel_indices]}")
        selection_log.append((simulation_data.index[0], [TICKERS[i] for i in sel_indices]))
    else:
        print("No selection (Fallback to cash/hold).")
    
    # Initialize Portfolios
    initial_prices = simulation_data.iloc[0].values
    engine_vqe.holdings = (engine_vqe.cash * target_weights_vqe) / initial_prices
    engine_vqe.cash = 0
    
    engine_bench.holdings = (engine_bench.cash * current_weights_bench) / initial_prices
    engine_bench.cash = 0
    
    # Loop
    for date in simulation_data.index:
        # Check if we need to rebalance (is today >= next scheduled rebalance?)
        if next_rebalance_idx < len(rebalance_dates) and date >= rebalance_dates[next_rebalance_idx]:
            print(f"Rebalancing at {date.date()}...")
            
            # Analyze Lookback Window
            # Window: [date - LOOKBACK_DAYS : date]
            # Use iloc for slicing robustly
            curr_loc = data.index.get_loc(date)
            window_data = data.iloc[max(0, curr_loc - LOOKBACK_DAYS) : curr_loc]
            
            sel_indices = run_analysis_pipeline(window_data, TICKERS)
            
            new_weights_vqe = np.zeros(len(TICKERS))
            if sel_indices:
                for i in sel_indices:
                    new_weights_vqe[i] = 1.0 / len(sel_indices)
                print(f"  Selected: {[TICKERS[i] for i in sel_indices]}")
                selection_log.append((date, [TICKERS[i] for i in sel_indices]))
            else:
                print("  Optimization failed or no selection. Holding position.")
                # We can choose to hold previous weights or go to cash. 
                # Let's hold previous weights (do nothing to weights, just rebalance to maintain them? or literally do nothing?)
                # Assuming 'step' rebalances to target. If we pass previous holdings as target...
                # Let's skip rebalancing call if failed, effectively holding assets.
                pass 
                
            # Execute Rebalance
            engine_vqe.step(date, new_weights_vqe)
            engine_bench.step(date, current_weights_bench)
            
            next_rebalance_idx += 1
            
        else:
            # Just record value
            val_vqe = engine_vqe.cash + np.sum(engine_vqe.holdings * data.loc[date].values)
            engine_vqe.portfolio_history.append(val_vqe)
            engine_vqe.dates.append(date)
            
            val_bench = engine_bench.cash + np.sum(engine_bench.holdings * data.loc[date].values)
            engine_bench.portfolio_history.append(val_bench)
            engine_bench.dates.append(date)

    # Results
    results_vqe = engine_vqe.get_results()
    results_bench = engine_bench.get_results()
    
    bt.generate_backtest_visualizations(results_vqe, results_bench, OUTPUT_DIR)
    
    metrics_vqe = bt.calculate_metrics(results_vqe)
    metrics_bench = bt.calculate_metrics(results_bench)
    
    bt.comparison_table(metrics_vqe, metrics_bench, OUTPUT_DIR)
    
    # Save Selection Log
    with open(f"{OUTPUT_DIR}/selection_log.txt", "w") as f:
        for d, assets in selection_log:
            f.write(f"{d.date()}: {assets}\n")
            
    print(f"\nBacktest Complete. Results saved to {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
