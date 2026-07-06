import numpy as np
import pandas as pd

def perform_backtest(data_clean, tickers, start_idx, rebalance_days, lookback_days, K, initial_capital, run_strategy_step_fn, strategy_kwargs):
    rebalance_indices = list(range(start_idx, len(data_clean), rebalance_days))

    value_vqe = [initial_capital] * start_idx
    value_bench = [initial_capital] * start_idx
    value_assets = {t: [initial_capital] * start_idx for t in tickers}

    holdings_vqe, holdings_bench = np.zeros(len(tickers)), np.zeros(len(tickers))
    cash_vqe, cash_bench = initial_capital, initial_capital
    cash_assets = {t: initial_capital for t in tickers}
    holdings_assets = {t: 0.0 for t in tickers}

    def rebalance_portfolio(current_cash, current_holdings, target_weights, prices):
        total_value = current_cash + np.sum(current_holdings * prices)
        target_values = total_value * target_weights
        
        new_holdings = current_holdings.copy()
        new_cash = current_cash
        
        for j in range(len(tickers)):
            c_val = current_holdings[j] * prices[j]
            if c_val > target_values[j]:
                sell_val = c_val - target_values[j]
                shares_sold = sell_val / prices[j]
                new_cash += sell_val
                new_holdings[j] -= shares_sold
        
        for j in range(len(tickers)):
            c_val = new_holdings[j] * prices[j]
            if c_val < target_values[j]:
                buy_val = target_values[j] - c_val
                if new_cash < buy_val: buy_val = new_cash
                shares_bought = buy_val / prices[j]
                new_cash -= buy_val
                new_holdings[j] += shares_bought
                
        return new_cash, new_holdings

    for i, curr_idx in enumerate(rebalance_indices):
        curr_date = data_clean.index[curr_idx]
        train_start_idx = max(0, curr_idx - lookback_days)
        train_data = data_clean.iloc[train_start_idx:curr_idx]
        
        next_idx = rebalance_indices[i+1] if i+1 < len(rebalance_indices) else len(data_clean)
        
        selected_indices = run_strategy_step_fn(train_data, tickers, curr_date=curr_date.date(), is_first_decision=(i == 0), **strategy_kwargs)
        print(f"[{curr_date.date()}] VQE Terpilih: {[tickers[idx] for idx in selected_indices]}")
        
        target_w_vqe = np.zeros(len(tickers))
        if len(selected_indices) > 0:
            weight = 1.0 / len(selected_indices)
            for idx in selected_indices:
                target_w_vqe[idx] = weight
                
        target_w_bench = np.full(len(tickers), 1.0 / len(tickers))
        
        current_prices = data_clean.iloc[curr_idx].values
        
        cash_vqe, holdings_vqe = rebalance_portfolio(cash_vqe, holdings_vqe, target_w_vqe, current_prices)
        if i == 0:
            cash_bench, holdings_bench = rebalance_portfolio(cash_bench, holdings_bench, target_w_bench, current_prices)
        
        if i == 0:
            for j, t in enumerate(tickers):
                target_w_indiv = np.zeros(len(tickers))
                target_w_indiv[j] = 1.0
                c_t, h_t = rebalance_portfolio(cash_assets[t], np.zeros(len(tickers)), target_w_indiv, current_prices)
                cash_assets[t] = c_t
                holdings_assets[t] = h_t[j]

        start_d = curr_idx if i == 0 else curr_idx + 1
        for d in range(start_d, next_idx):
            prices = data_clean.iloc[d].values
            
            value_vqe.append(cash_vqe + np.sum(holdings_vqe * prices))
            value_bench.append(cash_bench + np.sum(holdings_bench * prices))
            
            for j, t in enumerate(tickers):
                value_assets[t].append(cash_assets[t] + holdings_assets[t] * prices[j])

    return value_vqe, value_bench, value_assets
