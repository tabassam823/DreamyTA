import os
import pandas as pd
import matplotlib.pyplot as plt

def render_raw_prices_only():
    quantum_parent_dir = "../Hasil_GT" 
    output_plot_dir = "Grafik_Harga_Saham_Raw"
    
    if not os.path.exists(output_plot_dir):
        os.makedirs(output_plot_dir)

    print(f"\n--- Merender Grafik Harga Saham Asli (Raw Prices) ---")

    for n in [2, 4, 6, 8, 10, 12]:
        quantum_folder = f"{quantum_parent_dir}/Hasil_N{n}_GT"
        price_file = f"{quantum_folder}/harga_harian_saham_N{n}.csv"
        
        if os.path.exists(price_file):
            print(f"[N={n}] Memproses data harga...")
            
            df_prices = pd.read_csv(price_file)
            if 'Date' not in df_prices.columns:
                df_prices = df_prices.rename(columns={df_prices.columns[0]: 'Date'})
            df_prices['Date'] = pd.to_datetime(df_prices['Date'])
            
            # Kita potong mulai dari 2021 untuk konsistensi dengan grafik lainnya
            df_prices_bt = df_prices[df_prices['Date'] >= '2021-01-01'].copy()
            
            plt.figure(figsize=(14, 6))
            
            tickers = [c for c in df_prices_bt.columns if c != 'Date']
            colormap = plt.get_cmap('tab20')
            
            for idx, t in enumerate(tickers):
                # Plot harga asli tanpa normalisasi
                plt.plot(df_prices_bt['Date'], df_prices_bt[t], color=colormap(idx % 20), 
                         linewidth=1.5, label=t)
            
            plt.title(f'Pergerakan Harga Saham Individual (Raw Price) - N={n}', fontsize=14, fontweight='bold')
            plt.ylabel('Harga (IDR)', fontsize=12)
            plt.xlabel('Tanggal', fontsize=12)
            
            # Atur legend agar rapi di bawah atau samping jika terlalu banyak
            plt.legend(loc='upper left', fontsize=10, ncol=4 if n > 4 else 2)
            plt.grid(True, which='both', linestyle=':', alpha=0.5)

            plt.tight_layout()
            
            plot_path = f"{output_plot_dir}/pergerakan_harga_asli_N{n}.png"
            plt.savefig(plot_path, dpi=150)
            plt.close()
            print(f"      => Grafik berhasil disimpan: {plot_path}")
        else:
            print(f"[N={n}] File harga harian tidak ditemukan di {price_file}")

    print(f"\nProses selesai. Silakan cek folder '{output_plot_dir}' untuk melihat hasilnya.")

if __name__ == "__main__":
    render_raw_prices_only()
