import pandas as pd
import numpy as np
from compute_metrics import compute_metrics
from compute_beta import compute_beta

def generate_report(results, data_clean, benchmark_data, benchmark_rets, tickers, config, report_filename):
    """
    Menghitung metrik kinerja dan menulis laporan ke file txt.
    """
    initial_capital = config['initial_capital']
    benchmark_ticker = config['benchmark_ticker']
    start_idx = results['start_idx']
    
    # Perhitungan Nilai IHSG untuk Metrik
    benchmark_prices = benchmark_data.reindex(data_clean.index).ffill().bfill()
    start_benchmark_price = benchmark_prices.loc[data_clean.index[start_idx]]
    value_benchmark_idx = initial_capital * (benchmark_prices.iloc[start_idx:] / start_benchmark_price)

    # Hitung Metrik Utama
    tr_vqe, sr_vqe, mdd_vqe = compute_metrics(results['value_vqe'][start_idx-1:], initial_capital, "Quantum VQE")
    tr_nash, sr_nash, mdd_nash = compute_metrics(results['value_nash'][start_idx-1:], initial_capital, "Nash Equilibrium")
    tr_bench, sr_bench, mdd_bench = compute_metrics(results['value_bench'][start_idx-1:], initial_capital, "Equal Weight")
    tr_ihsg, sr_ihsg, mdd_ihsg = compute_metrics(value_benchmark_idx.values.flatten(), initial_capital, f"Indeks ({benchmark_ticker})")

    # Hitung Beta terhadap IHSG
    bt_dates = data_clean.index[start_idx:]
    vqe_rets = pd.Series(results['value_vqe'][start_idx:], index=bt_dates).pct_change().dropna()
    vqe_beta = compute_beta(vqe_rets, benchmark_rets.reindex(vqe_rets.index).fillna(0))

    nash_rets = pd.Series(results['value_nash'][start_idx:], index=bt_dates).pct_change().dropna()
    nash_beta = compute_beta(nash_rets, benchmark_rets.reindex(nash_rets.index).fillna(0))

    bench_rets = pd.Series(results['value_bench'][start_idx:], index=bt_dates).pct_change().dropna()
    bench_beta = compute_beta(bench_rets, benchmark_rets.reindex(bench_rets.index).fillna(0))

    ihsg_rets = value_benchmark_idx.pct_change().dropna()
    ihsg_beta = compute_beta(ihsg_rets, benchmark_rets.reindex(ihsg_rets.index).fillna(0))

    # Tampilkan Laporan di Terminal
    print("\n" + "="*40)
    print("           METRIK KINERJA AKHIR")
    print("="*40)
    print(f"STRATEGI NASH EQUILIBRIUM (KLASIK):")
    print(f"  Return : {tr_nash:.2f}% | Sharpe: {sr_nash:.4f}")
    print(f"  Beta   : {nash_beta:.4f} | MDD   : {mdd_nash:.2f}%")
    print("-" * 35)
    print(f"STRATEGI QUANTUM VQE:")
    print(f"  Return : {tr_vqe:.2f}% | Sharpe: {sr_vqe:.4f}")
    print(f"  Beta   : {vqe_beta:.4f} | MDD   : {mdd_vqe:.2f}%")
    print("-" * 35)
    print(f"STRATEGI EQUAL WEIGHT (BENCHMARK):")
    print(f"  Return : {tr_bench:.2f}% | Sharpe: {sr_bench:.4f}")
    print(f"  Beta   : {bench_beta:.4f} | MDD   : {mdd_bench:.2f}%")
    print("-" * 35)
    print(f"INDEKS PASAR ({benchmark_ticker}):")
    print(f"  Return : {tr_ihsg:.2f}% | Sharpe: {sr_ihsg:.4f}")
    print(f"  Beta   : {ihsg_beta:.4f} | MDD   : {mdd_ihsg:.2f}%")
    print("="*40 + "\n")

    # Simpan Laporan ke File
    with open(report_filename, "w") as f:
        f.write("LAPORAN STRATEGI GAME THEORY DAN VQE\n")
        f.write(f"Urutan Ticker: {tickers}\n")
        f.write("="*45 + "\n")
        
        f.write("1. METRIK STRATEGI NASH EQUILIBRIUM (KLASIK):\n")
        f.write(f"   Return: {tr_nash:.2f}% | Sharpe: {sr_nash:.4f} | Beta: {nash_beta:.4f} | MDD: {mdd_nash:.2f}%\n")
        f.write("-" * 45 + "\n")
        
        f.write("2. METRIK STRATEGI QUANTUM VQE:\n")
        f.write(f"   Return: {tr_vqe:.2f}% | Sharpe: {sr_vqe:.4f} | Beta: {vqe_beta:.4f} | MDD: {mdd_vqe:.2f}%\n")
        f.write("-" * 45 + "\n")
        
        f.write("3. METRIK STRATEGI EQUAL WEIGHT:\n")
        f.write(f"   Return: {tr_bench:.2f}% | Sharpe: {sr_bench:.4f} | Beta: {bench_beta:.4f} | MDD: {mdd_bench:.2f}%\n")
        f.write("-" * 45 + "\n")
        
        f.write(f"4. METRIK INDEKS PASAR ({benchmark_ticker}):\n")
        f.write(f"   Return: {tr_ihsg:.2f}% | Sharpe: {sr_ihsg:.4f} | Beta: {ihsg_beta:.4f} | MDD: {mdd_ihsg:.2f}%\n\n")
        
        for log in results['detail_logs']: f.write(log + "\n")
    
    return value_benchmark_idx
