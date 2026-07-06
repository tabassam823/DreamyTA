import os
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import numpy as np

def render_slsqp_minimal():
    classic_dir = "Hasil_Classic_Compare"
    quantum_parent_dir = "../Hasil_GT" 
    output_plot_dir = "Grafik_SLSQP_Only"
    initial_capital = 100_000_000.0
    
    if not os.path.exists(output_plot_dir):
        os.makedirs(output_plot_dir)

    print(f"\n--- Merender Grafik SLSQP vs Benchmark & Indeks ---")

    for n in [2, 4, 6, 8, 10, 12]:
        classic_file = f"{classic_dir}/equity_history_classic_N{n}.csv"
        quantum_file = f"{quantum_parent_dir}/Hasil_N{n}_GT/hasil_ekuitas_backtest_N{n}.csv"
        
        if os.path.exists(classic_file) and os.path.exists(quantum_file):
            print(f"[N={n}] Mengolah data...")
            df_classic = pd.read_csv(classic_file)
            df_quantum = pd.read_csv(quantum_file)
            
            df_classic['Date'] = pd.to_datetime(df_classic['Date'])
            df_quantum['Date'] = pd.to_datetime(df_quantum['Date'])
            
            # Mempertahankan data dari tahun 2020 (masa lookback) agar garis mendatar terlihat
            # Samakan start date untuk Benchmark (Equal Weight) dengan SLSQP jika ada sedikit perbedaan
            start_date_classic = df_classic['Date'].min()
            df_quantum = df_quantum[df_quantum['Date'] >= start_date_classic].copy()
            
            # Buat garis Equal Weight mendatar pada nilai modal awal sebelum Januari 2021
            mask_lookback = df_quantum['Date'] < pd.to_datetime('2021-01-01')
            df_quantum.loc[mask_lookback, 'Benchmark'] = initial_capital
            
            # Ambil rentang tanggal untuk download indeks
            start_date = df_classic['Date'].min()
            end_date = df_classic['Date'].max()
            
            # Download data IHSG (^JKSE) sebagai pembanding
            try:
                print(f"      > Mengambil data IHSG untuk N={n}...")
                ihsg = yf.download("^JKSE", start=start_date, end=end_date, progress=False)['Close']
                
                # Filter indeks IHSG untuk mencari nilai acuan pada awal Januari 2021
                ihsg_start_bt_date = pd.to_datetime('2021-01-01')
                # Mencari nilai IHSG pada hari pertama trading setelah atau pada 2021-01-01
                ihsg_base_idx = ihsg.index[ihsg.index >= ihsg_start_bt_date].min()
                
                if pd.isna(ihsg_base_idx):
                    # Fallback jika tidak ada data setelah 2021
                    ihsg_base_val = ihsg.iloc[0]
                else:
                    ihsg_base_val = ihsg.loc[ihsg_base_idx]
                
                # Normalisasi IHSG ke modal awal berdasarkan nilai di awal 2021
                ihsg_norm = (ihsg / ihsg_base_val) * initial_capital
                
                # Buat garis IHSG mendatar pada nilai modal awal sebelum Januari 2021
                mask_ihsg_lookback = ihsg_norm.index < ihsg_start_bt_date
                ihsg_norm.loc[mask_ihsg_lookback] = initial_capital

            except Exception as e:
                print(f"      ! Gagal mengambil data IHSG: {e}")
                ihsg_norm = None

            plt.figure(figsize=(12, 6))
            
            # 1. Garis SLSQP (Markowitz Klasik) - Hijau Tebal
            plt.plot(df_classic['Date'], df_classic['Equity'], 
                     label='Optimasi SLSQP (Classic Markowitz)', 
                     color='forestgreen', linewidth=3)
            
            # 2. Garis Equal Weight (Benchmark) - Abu-abu Titik-titik
            plt.plot(df_quantum['Date'], df_quantum['Benchmark'], 
                     label='Equal Weight (Benchmark)', 
                     color='gray', linestyle=':', alpha=0.8, linewidth=2)
            
            # 3. Garis Indeks IHSG - Magenta Putus-putus
            if ihsg_norm is not None:
                plt.plot(ihsg_norm.index, ihsg_norm.values, 
                         label='Indeks IHSG (^JKSE)', 
                         color='magenta', linestyle='--', alpha=0.7, linewidth=2)

            plt.title('Perbandingan Pertumbuhan Ekuitas: SLSQP vs Benchmarks', fontsize=14)
            plt.ylabel('Total Ekuitas (Rupiah)', fontsize=12)
            plt.xlabel('Tanggal', fontsize=12)
            plt.legend(loc='upper left', frameon=True, shadow=True)
            plt.grid(True, linestyle='--', alpha=0.5)
            
            plt.tight_layout()
            plot_path = f"{output_plot_dir}/slsqp_vs_benchmarks_N{n}.png"
            plt.savefig(plot_path, dpi=150)
            plt.close()
            print(f"      => Grafik disimpan di: {plot_path}")
        else:
            print(f"[N={n}] Data tidak lengkap. Pastikan simulasi klasik dan quantum sudah dijalankan.")

if __name__ == "__main__":
    render_slsqp_minimal()
