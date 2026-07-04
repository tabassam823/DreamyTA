import pandas as pd

# Function to generate longtable
def format_latex(df, caption, label, longtable=True):
    cols = df.columns
    header = " & ".join([str(c) for c in cols]) + " \\\\"
    
    latex = []
    if longtable:
        latex.append("\\begin{footnotesize}")
        latex.append("\\begin{longtable}{" + "l" * len(cols) + "}")
        latex.append(f"\\caption{{{caption}}} \\label{{{label}}} \\\\")
        latex.append("\\toprule")
        latex.append(header)
        latex.append("\\midrule")
        latex.append("\\endfirsthead")
        latex.append("\\multicolumn{" + str(len(cols)) + "}{c}{{\\bfseries Lanjutan Tabel \\thetable}} \\\\")
        latex.append("\\toprule")
        latex.append(header)
        latex.append("\\midrule")
        latex.append("\\endhead")
        latex.append("\\midrule")
        latex.append("\\multicolumn{" + str(len(cols)) + "}{r}{{Bersambung...}} \\\\")
        latex.append("\\bottomrule")
        latex.append("\\endfoot")
        latex.append("\\bottomrule")
        latex.append("\\endlastfoot")
    
    for i, row in df.iterrows():
        line = " & ".join([f"{v:.4f}" if isinstance(v, (float)) else str(v) for v in row]) + " \\\\"
        latex.append(line)
    
    if longtable:
        latex.append("\\end{longtable}")
        latex.append("\\end{footnotesize}")
    
    return "\n".join(latex)

# 1. Bias H, J, C_Obj, Lambda
df_bias = pd.read_csv("GTQuantumInvest/Hasil_N2_GT/bias_h_total_N2.csv")
df_param = pd.read_csv("GTQuantumInvest/Hasil_N2_GT/parameter_pendamping_N2.csv")
df_metrics = pd.read_csv("GTQuantumInvest/Hasil_N2_GT/metrik_return_dan_lambda_N2.csv")
df_j = pd.read_csv("GTQuantumInvest/Hasil_N2_GT/interaksi_J_total_N2.csv")

dates = df_bias['Date'].unique()

data_unified = []
for i, d in enumerate(dates, 1):
    row = {'P': i}
    # get lambda
    lam = df_metrics[df_metrics['Date'] == d]['Lambda_RiskAversion'].iloc[0]
    row['$\\lambda$'] = lam
    
    # get h
    for t in ['BBCA.JK', 'ADRO.JK']:
        h_val = df_bias[(df_bias['Date'] == d) & (df_bias['Ticker'] == t)]['Bias_h_Obj'].sum()
        t_clean = t.split('.')[0]
        row[f'$h_{{obj}}$ ({t_clean})'] = h_val
        
    # get J (BC-AD)
    sub_j = df_j[df_j['Date'] == d]
    if not sub_j.empty:
        j_val = sub_j['Interaction_J_Obj'].sum()
    else:
        j_val = 0.0
    row['$J_{obj}$ (BC-AD)'] = j_val

    # get C_obj
    c_obj = df_param[df_param['Date'] == d]['C_Obj'].iloc[0]
    row['$C_{obj}$'] = c_obj
    
    data_unified.append(row)

df_unified = pd.DataFrame(data_unified)
latex_unified = format_latex(df_unified, "Parameter Dinamis Portofolio N=2 ($\\lambda$, $h_{obj}$, $J_{obj}$)", "tab:unified_n2")


# 2. SBR Iterations
df_sbr = pd.read_csv("GTQuantumInvest/Hasil_N2_GT/riwayat_nash_sbr_N2.csv")
latex_sbr = format_latex(df_sbr, "Riwayat Iterasi Sequential Best Response (SBR) N=2", "tab:sbr_history_n2")

# 3. VQE Convergence
df_vqe = pd.read_csv("GTQuantumInvest/Hasil_N2_GT/hasil_depth_vs_energi_N2.csv")
# Group by Date, Depth, get Energy
df_vqe_pivot = df_vqe.pivot(index='Date', columns='Depth', values='Energy').reset_index()
df_vqe_pivot.insert(0, 'P', range(1, len(df_vqe_pivot) + 1))
df_vqe_pivot.columns = [str(c) if not isinstance(c, str) else c for c in df_vqe_pivot.columns]
# Check max depth
depths = [col for col in df_vqe_pivot.columns if col not in ['P', 'Date']]
df_vqe_pivot.rename(columns={d: f'D{d}' for d in depths}, inplace=True)
latex_vqe = format_latex(df_vqe_pivot, "Perbandingan Energi Akhir VQE Berdasarkan Depth N=2", "tab:vqe_depth_n2")

# Assemble Lampiran-D
doc = f"""\\chapter{{Data Numerik Hasil Simulasi N=2}}
\\label{{appendix:numerical_data_n2}}

Lampiran ini menyajikan dataset numerik yang menjadi dasar analisis pada bab-bab sebelumnya untuk sistem dengan $N=2$ aset. Seluruh nilai numerik telah dibulatkan untuk kemudahan pembacaan tanpa mengurangi signifikansi teknis.

Data harga harian saham untuk periode simulasi ini dapat merujuk pada Tabel \\ref{{tab:daily_prices_merged}} di Lampiran \\ref{{appendix:daily_prices}}.

\\section{{Parameter Dinamis Hamiltonian N=2}}

Berikut adalah parameter $h$ (bias), interaksi $J$, $C_{{obj}}$ (konstanta), dan parameter $\\lambda$ yang dihitung berdasarkan volatilitas per jendela untuk N=2. Karena hanya terdapat dua aset, interaksi $J$ digabungkan ke dalam satu tabel yang sama.

{latex_unified}

\\section{{Riwayat Iterasi Sequential Best Response (SBR) N=2}}

Proses pencarian ekuilibrium menggunakan metode SBR dicatat pada tabel berikut. \\textit{{Swap}} menunjukkan indeks bit yang ditukar, \\textit{{Utility}} adalah nilai utilitas yang dicapai, dan \\textit{{Bitstring}} merepresentasikan portofolio strategi.

{latex_sbr}

\\section{{Perbandingan Konvergensi VQE Berdasarkan Depth N=2}}

Tabel berikut menunjukkan perbandingan energi akhir (konvergensi) yang berhasil dicapai oleh algoritma VQE pada berbagai kedalaman sirkuit di setiap periode jendela waktu. 

{latex_vqe}
"""

with open("Contents/Lampiran/Lampiran-D.tex", "w") as f:
    f.write(doc)

print("Lampiran-D.tex berhasil dibuat.")
