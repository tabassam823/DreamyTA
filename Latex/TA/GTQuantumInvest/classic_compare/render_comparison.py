import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def render_all_comparisons():
    # Folder tempat hasil tersimpan
    classic_dir = "Hasil_Classic_Compare"
    # Mengambil hasil Warm-Start (GT) sebagai pembanding utama
    quantum_parent_dir = "../Hasil_GT" 
    output_plot_dir = "Grafik_Perbandingan"
    initial_capital = 100_000_000.0
    
    if not os.path.exists(output_plot_dir):
        os.makedirs(output_plot_dir)

    print(f"\n--- Memulai Perenderan Grafik Perbandingan (Quantum VQE vs Classic Markowitz) ---")

    for n in [2, 4, 6, 8, 10, 12]:
        classic_file = f"{classic_dir}/equity_history_classic_N{n}.csv"
        quantum_folder = f"{quantum_parent_dir}/Hasil_N{n}_GT"
        quantum_file = f"{quantum_folder}/hasil_ekuitas_backtest_N{n}.csv"
        price_file = f"{quantum_folder}/harga_harian_saham_N{n}.csv"
        
        if os.path.exists(classic_file) and os.path.exists(quantum_file):
            print(f"[N={n}] Memproses data...")
            df_classic = pd.read_csv(classic_file)
            df_quantum = pd.read_csv(quantum_file)
            
            # Konversi tanggal
            df_classic['Date'] = pd.to_datetime(df_classic['Date'])
            df_quantum['Date'] = pd.to_datetime(df_quantum['Date'])
            
            # Buat Subplot 2 Baris: Atas untuk Ekuitas, Bawah untuk Harga Saham
            fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 12), sharex=True, gridspec_kw={'height_ratios': [1.5, 1]})
            
            # --- PANEL 1: EKUITAS STRATEGI ---
            # Hitung persentase pertumbuhan
            pct_vqe = (df_quantum['VQE'] - df_quantum['VQE'].iloc[0]) / df_quantum['VQE'].iloc[0] * 100
            pct_bench = (df_quantum['Benchmark'] - df_quantum['Benchmark'].iloc[0]) / df_quantum['Benchmark'].iloc[0] * 100
            pct_nash = (df_quantum['Nash'] - df_quantum['Nash'].iloc[0]) / df_quantum['Nash'].iloc[0] * 100

            # 1. Plot Quantum VQE (Biru)
            ax1.plot(df_quantum['Date'], pct_vqe, label=r'Quantum VQE ($\mathit{Warm-Start}$)', 
                     color='blue', linewidth=3)
            
            # (Garis Classic Markowitz dihapus sesuai permintaan)
            
            # 3. Plot Benchmark (Hitam Titik-titik)
            ax1.plot(df_quantum['Date'], pct_bench, label=r'$\mathit{Benchmark}$ ($\mathit{Equal \ Weight}$)', 
                     color='black', alpha=0.6, linestyle=':')
            
            # 4. Plot Nash Equilibrium (Oranye)
            ax1.plot(df_quantum['Date'], pct_nash, label=r'$\mathit{Nash \ Equilibrium}$ (Klasik)', 
                     color='orange', alpha=0.8)

            ax1.set_title(f'Persentase Pertumbuhan Portofolio (N={n})', fontsize=14, fontweight='bold')
            ax1.set_ylabel('Persentase Pertumbuhan Modal (%)', fontsize=12)
            ax1.legend(loc='upper left', fontsize=15)
            ax1.grid(True, which='both', linestyle='--', alpha=0.4)

            # --- PANEL 2: HARGA SAHAM ASLI (TANPA NORMALISASI) ---
            if os.path.exists(price_file):
                df_prices = pd.read_csv(price_file)
                if 'Date' not in df_prices.columns:
                    df_prices = df_prices.rename(columns={df_prices.columns[0]: 'Date'})
                df_prices['Date'] = pd.to_datetime(df_prices['Date'])
                
                # Filter agar tanggal sesuai dengan backtest
                start_bt_date = df_quantum['Date'].iloc[0]
                df_prices_bt = df_prices[df_prices['Date'] >= start_bt_date].copy()
                
                tickers = [c for c in df_prices_bt.columns if c != 'Date']
                colormap = plt.get_cmap('tab20')
                
                for idx, t in enumerate(tickers):
                    # Plot harga asli
                    ax2.plot(df_prices_bt['Date'], df_prices_bt[t], color=colormap(idx % 20), 
                             linewidth=1.5, label=t)
                
                ax2.set_title(f'Pergerakan Harga Saham Individual (Raw Price)', fontsize=12, fontweight='bold')
                ax2.set_ylabel('Harga (IDR)', fontsize=12)
                ax2.legend(loc='upper left', fontsize=13.5, ncol=4 if n > 4 else 2)
                ax2.grid(True, which='both', linestyle=':', alpha=0.5)

            plt.xlabel('Tanggal', fontsize=12)
            plt.tight_layout()
            
            plot_path = f"{output_plot_dir}/perbandingan_VQE_vs_Classic_N{n}.png"
            plt.savefig(plot_path, dpi=150)
            plt.close()
            print(f"      => Grafik berhasil disimpan: {plot_path}")
        else:
            if not os.path.exists(classic_file):
                print(f"[N={n}] Data Klasik tidak ditemukan di {classic_file}")
            if not os.path.exists(quantum_file):
                print(f"[N={n}] Data Quantum tidak ditemukan di {quantum_file}")


    print(f"\nProses selesai. Silakan cek folder '{output_plot_dir}' untuk melihat hasilnya.")

if __name__ == "__main__":
    render_all_comparisons()
