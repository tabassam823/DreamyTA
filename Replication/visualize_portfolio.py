import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def visualize_portfolio():
    # =========================================================================
    # USER INPUT SECTION
    # =========================================================================
    
    # 1. Tickers (Fixed)
    tickers = [
        'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'NVDA', 'JPM', 
        '600519.SS', '601398.SS', '600036.SS', '601857.SS', '600276.SS', '601318.SS'
    ]
    
    # 2. Expected Returns (mu) - Values from Phase 1
    # Replace this array if you have new data
    mu = np.array([
        0.00129829, 0.00063003, 0.00142009, 0.00165567, 0.00458041,
        0.0014705, -0.00010674, 0.00170935, 0.00173847, 0.00130019,
        0.00036145, 0.00156579
    ])
    
    # 3. Optimal Bitstring
    # Paste the "Lowest Energy Bitstring" from the VQE output here
    # Example: "100110111000"
    optimal_bitstring = "100110111000" 
    
    # =========================================================================
    # PROCESSING
    # =========================================================================
    
    # Qiskit bitstrings are often printed little-endian (rightmost bit is qubit 0).
    # In our mapping, qubit i corresponds to asset i.
    # If the string is "qN...q0", we need to reverse it to get "q0...qN" 
    # to match the tickers list [Asset 0, Asset 1, ...].
    
    # Check mapping logic from previous phase:
    # Bitstring: 100110111000
    # Reversed:  000111011001
    # Indices:   012345678901
    # Selected: 3, 4, 5, 7, 8, 11
    
    # Reverse string to align with list index 0 -> N
    binary_selection = np.array([int(bit) for bit in optimal_bitstring[::-1]])
    
    print("Asset Allocation:")
    for i, ticker in enumerate(tickers):
        status = "SELECTED" if binary_selection[i] == 1 else "        "
        print(f"{i:2d} | {ticker:<12} | Exp Ret: {mu[i]:.6f} | {status}")

    # =========================================================================
    # VISUALIZATION
    # =========================================================================
    
    sns.set_theme(style="whitegrid")
    fig, ax1 = plt.subplots(figsize=(14, 8))
    
    # 1. Bar Chart: Binary Decision (Selected vs Not Selected)
    # Create colors: Green for Selected, Light Grey for Not Selected
    colors = ['#2ecc71' if x == 1 else '#bdc3c7' for x in binary_selection]
    
    # Plot bars
    bars = ax1.bar(tickers, binary_selection, color=colors, alpha=0.7, label='Portfolio Selection')
    
    # Customize Primary Axis (Selection)
    ax1.set_ylabel('Selection Status (Binary)', fontsize=14, fontweight='bold', color='#2c3e50')
    ax1.set_ylim(0, 1.2)
    ax1.set_yticks([0, 1])
    ax1.set_yticklabels(['Not Selected', 'Selected'], fontsize=12)
    ax1.tick_params(axis='x', rotation=45, labelsize=12)
    
    # Add labels on top of bars
    for bar, selected in zip(bars, binary_selection):
        height = bar.get_height()
        if selected:
            ax1.text(bar.get_x() + bar.get_width()/2., 1.02, 'IN', 
                     ha='center', va='bottom', fontsize=12, fontweight='bold', color='green')
    
    # 2. Line Plot: Expected Returns (Secondary Axis)
    ax2 = ax1.twinx()
    
    # Plot line/scatter
    ax2.plot(tickers, mu, color='#e74c3c', marker='o', linestyle='-', linewidth=2, markersize=8, label='Annualized Expected Return')
    
    # Highlight high-return points
    for i, val in enumerate(mu):
        ax2.annotate(f"{val:.4f}", (i, val), xytext=(0, 10), textcoords='offset points', 
                     ha='center', fontsize=9, color='#c0392b')

    # Customize Secondary Axis (Returns)
    ax2.set_ylabel('Daily Expected Return (mu)', fontsize=14, fontweight='bold', color='#e74c3c')
    ax2.grid(False) # Turn off grid for second axis to avoid clutter
    
    # Title and Layout
    plt.title('VQE Optimal Portfolio Allocation (WCVaR Optimized)\nBinary Selection vs Expected Return', fontsize=16, fontweight='bold', pad=20)
    
    # Legend
    # Combine legends from both axes
    lines, labels = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax2.legend(lines + lines2, labels + labels2, loc='upper left', fontsize=12)
    
    plt.tight_layout()
    
    # Save output
    output_filename = "vqe_optimal_portfolio.png"
    plt.savefig(output_filename, dpi=300)
    print(f"\nVisualization saved to: {output_filename}")

if __name__ == "__main__":
    visualize_portfolio()
