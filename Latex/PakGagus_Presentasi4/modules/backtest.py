
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

def calculate_metrics(portfolio_values, benchmark_values=None):
    """Calculate key performance indicators."""
    returns = portfolio_values.pct_change().dropna()
    
    # Total Return
    total_return = (portfolio_values.iloc[-1] - portfolio_values.iloc[0]) / portfolio_values.iloc[0]
    
    # CAGR
    n_years = len(portfolio_values) / 252
    cagr = (portfolio_values.iloc[-1] / portfolio_values.iloc[0])**(1/n_years) - 1
    
    # Volatility (Annualized)
    volatility = returns.std() * np.sqrt(252)
    
    # Sharpe Ratio (assuming 0% risk free for simplicity or just excess return)
    sharpe_ratio = (returns.mean() * 252) / volatility if volatility != 0 else 0
    
    # Max Drawdown
    cumulative_returns = (1 + returns).cumprod()
    peak = cumulative_returns.cummax()
    drawdown = (cumulative_returns - peak) / peak
    max_drawdown = drawdown.min()
    
    metrics = {
        "Total Return": total_return,
        "CAGR": cagr,
        "Volatility": volatility,
        "Sharpe Ratio": sharpe_ratio,
        "Max Drawdown": max_drawdown
    }
    
    return metrics

def rebalance_portfolio(current_cash, current_holdings, target_weights, prices, transaction_cost=0.0025):
    """Rebalance portfolio to target weights."""
    total_value = current_cash + np.sum(current_holdings * prices)
    target_values = total_value * target_weights
    
    current_values = current_holdings * prices
    diff_values = target_values - current_values
    
    # Sell first
    sells = diff_values < 0
    sell_amounts = -diff_values[sells]
    sell_shares = sell_amounts / prices[sells]
    
    # Apply transaction cost to sells
    proceeds = np.sum(sell_shares * prices[sells] * (1 - transaction_cost))
    current_cash += proceeds
    current_holdings[sells] -= sell_shares
    
    # Buy second
    buys = diff_values > 0
    buy_amounts = diff_values[buys]
    
    # Check if we have enough cash (approximate, since costs reduce buying power)
    total_buy_needed = np.sum(buy_amounts)
    if total_buy_needed > current_cash:
        # Scale down buys if not enough cash (shouldn't happen if math is perfect, but costs...)
        scale_factor = current_cash / (total_buy_needed * (1 + transaction_cost))
        buy_amounts *= scale_factor
        
    buy_shares = buy_amounts / (prices[buys] * (1 + transaction_cost))
    cost = np.sum(buy_shares * prices[buys] * (1 + transaction_cost))
    
    current_cash -= cost
    current_holdings[buys] += buy_shares
    
    return current_cash, current_holdings

def run_backtest_simulation(price_data, initial_capital=100000000, transaction_cost=0.0014):
    """
    Simulates a strategy.
    Note: Real backtest needs strategy logic injected. 
    Here I'll implement a 'Framework' that accepts a `strategy_func` callback.
    """
    pass # Placeholder if needed, but defining class or simpler func below

class BacktestEngine:
    def __init__(self, price_data, initial_capital=100_000_000, transaction_cost=0.0014):
        self.prices = price_data
        self.initial_capital = initial_capital
        self.tc = transaction_cost
        self.cash = initial_capital
        self.holdings = np.zeros(len(price_data.columns))
        self.portfolio_history = []
        self.dates = []
        
    def step(self, date, target_weights):
        current_prices = self.prices.loc[date].values
        
        self.cash, self.holdings = rebalance_portfolio(
            self.cash, self.holdings, target_weights, current_prices, self.tc
        )
        
        total_val = self.cash + np.sum(self.holdings * current_prices)
        self.portfolio_history.append(total_val)
        self.dates.append(date)
        
    def get_results(self):
        df = pd.Series(self.portfolio_history, index=self.dates)
        return df

def generate_backtest_visualizations(portfolio_curve, benchmark_curve, output_dir="generated_images"):
    """Generates equity curve and drawdown plot."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 1. Equity Curve
    plt.figure(figsize=(10, 6))
    plt.plot(portfolio_curve.index, portfolio_curve.values, label="HE-VQE Portfolio", linewidth=2)
    if benchmark_curve is not None:
         plt.plot(benchmark_curve.index, benchmark_curve.values, label="Benchmark (Equal Weight)", linestyle='--', alpha=0.7)
    
    plt.title("Portfolio Performance vs Benchmark")
    plt.xlabel("Date")
    plt.ylabel("Portfolio Value (IDR)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/backtest_equity_curve.png")
    plt.close()
    
    # 2. Drawdown
    returns = portfolio_curve.pct_change().dropna()
    cum_ret = (1 + returns).cumprod()
    peak = cum_ret.cummax()
    drawdown = (cum_ret - peak) / peak
    
    plt.figure(figsize=(10, 4))
    plt.fill_between(drawdown.index, drawdown.values, color='red', alpha=0.3)
    plt.plot(drawdown.index, drawdown.values, color='red', linewidth=1)
    plt.title("Portfolio Drawdown")
    plt.ylabel("Drawdown %")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/backtest_drawdown.png")
    plt.close()
    
    print(f"Backtest visualizations saved to {output_dir}")

def comparison_table(metrics_port, metrics_bench, output_dir="generated_images"):
    """Generates comparison table image."""
    df = pd.DataFrame([metrics_port, metrics_bench], index=["HE-VQE", "Benchmark"]).round(4)
    
    fig, ax = plt.subplots(figsize=(8, 2))
    ax.axis('tight')
    ax.axis('off')
    table = ax.table(cellText=df.values, colLabels=df.columns, rowLabels=df.index, loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.3)
    plt.title("Performance Metrics Comparison")
    plt.savefig(f"{output_dir}/performance_comparison.png", bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    pass
