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

# 1. Bias H and C_Obj, Lambda
df_bias = pd.read_csv("GTQuantumInvest/Hasil_N4_GT/bias_h_total_N4.csv")
df_param = pd.read_csv("GTQuantumInvest/Hasil_N4_GT/parameter_pendamping_N4.csv")
df_metrics = pd.read_csv("GTQuantumInvest/Hasil_N4_GT/metrik_return_dan_lambda_N4.csv")

dates = df_bias['Date'].unique()

data_h = []
for i, d in enumerate(dates, 1):
    row = {'P': i, 'Tanggal': d}
    # get lambda
    lam = df_metrics[df_metrics['Date'] == d]['Lambda_RiskAversion'].iloc[0]
    row['$\\lambda$'] = lam
    
    # get h
    for t in ['BBCA.JK', 'ADRO.JK', 'SMGR.JK', 'TLKM.JK']:
        h_val = df_bias[(df_bias['Date'] == d) & (df_bias['Ticker'] == t)]['Bias_h_Obj'].sum() # assuming one row
        t_clean = t.split('.')[0]
        row[f'$h_{{obj}}$ ({t_clean[:2]})'] = h_val
        
    # get C_obj
    c_obj = df_param[df_param['Date'] == d]['C_Obj'].iloc[0]
    row['$C_{obj}$'] = c_obj
    data_h.append(row)

df_h = pd.DataFrame(data_h)
latex_h = format_latex(df_h, "Parameter Dinamis Portofolio N=4 ($\\lambda$, $h_{obj}$, $C_{obj}$)", "tab:unified_n4")

# 2. Interaksi J
df_j = pd.read_csv("GTQuantumInvest/Hasil_N4_GT/interaksi_J_total_N4.csv")
data_j = []
for i, d in enumerate(dates, 1):
    row = {'P': i, 'Tanggal': d}
    sub_j = df_j[df_j['Date'] == d]
    
    # Possible pairs
    pairs = [('BBCA.JK', 'TLKM.JK'), ('BBCA.JK', 'SMGR.JK'), ('BBCA.JK', 'ADRO.JK'),
             ('TLKM.JK', 'SMGR.JK'), ('TLKM.JK', 'ADRO.JK'), ('SMGR.JK', 'ADRO.JK')]
    
    for t1, t2 in pairs:
        # Note: could be in any order in Ticker_i, Ticker_j
        j_val_row = sub_j[((sub_j['Ticker_i'] == t1) & (sub_j['Ticker_j'] == t2)) | ((sub_j['Ticker_i'] == t2) & (sub_j['Ticker_j'] == t1))]
        j_val = j_val_row['Interaction_J_Obj'].sum() if not j_val_row.empty else 0.0
        # Format label like BC-TL
        lbl = f"{t1[:2]}-{t2[:2]}"
        row[lbl] = j_val
    data_j.append(row)

df_j_table = pd.DataFrame(data_j)
latex_j = format_latex(df_j_table, "Parameter Interaksi Hamiltonian $J$ N=4", "tab:interaction_j_n4")

# 3. SBR Iterations
df_sbr = pd.read_csv("GTQuantumInvest/Hasil_N4_GT/riwayat_nash_sbr_N4.csv")
# To avoid making it too long, we might just list the SBR iterations
# The CSV has Date, Iteration, Bitstring, Utility, Swap
# I will just format this directly
latex_sbr = format_latex(df_sbr, "Riwayat Iterasi Sequential Best Response (SBR) N=4", "tab:sbr_history_n4")

# 4. VQE Convergence
df_vqe = pd.read_csv("GTQuantumInvest/Hasil_N4_GT/hasil_depth_vs_energi_N4.csv")
# Group by Date, Depth, get Energy
# Pivot so Columns are Depth 1 to 8, Rows are Dates (or P)
df_vqe_pivot = df_vqe.pivot(index='Date', columns='Depth', values='Energy').reset_index()
# add P
df_vqe_pivot.insert(0, 'P', range(1, len(df_vqe_pivot) + 1))
df_vqe_pivot.columns = [str(c) if not isinstance(c, str) else c for c in df_vqe_pivot.columns]
# Rename column 1 to 8 as D1 to D8
df_vqe_pivot.rename(columns={str(d): f'D{d}' for d in range(1, 9)}, inplace=True)
latex_vqe = format_latex(df_vqe_pivot, "Perbandingan Energi Akhir VQE Berdasarkan Depth N=4", "tab:vqe_depth_n4")

# Assemble Lampiran-G
doc = f"""\\chapter{{Data Numerik Hasil Simulasi N=4}}
\\label{{appendix:numerical_data_n4}}

Lampiran ini menyajikan dataset numerik untuk simulasi dengan $N=4$ aset. Untuk data harga harian saham untuk periode simulasi, dapat merujuk pada Tabel \\ref{{tab:daily_prices_merged}} di Lampiran \\ref{{appendix:daily_prices}}.

\\section{{Parameter Dinamis Hamiltonian N=4}}

Berikut adalah parameter $h$ (bias), $C_{{obj}}$ (konstanta), dan parameter $\\lambda$ yang dihitung berdasarkan volatilitas per jendela. 

{latex_h}

Selanjutnya adalah parameter interaksi $J$ antar masing-masing aset pada setiap jendela waktu.

{latex_j}

\\section{{Riwayat Iterasi Sequential Best Response (SBR) N=4}}

Proses pencarian ekuilibrium menggunakan metode SBR dicatat pada tabel berikut. \textit{{Swap}} menunjukkan indeks bit yang ditukar, \textit{{Utility}} adalah nilai utilitas yang dicapai, dan \textit{{Bitstring}} merepresentasikan portofolio strategi.

{latex_sbr}

\\section{{Perbandingan Konvergensi VQE Berdasarkan Depth}}

Tabel berikut menunjukkan perbandingan energi akhir (konvergensi) yang berhasil dicapai oleh algoritma VQE pada berbagai kedalaman sirkuit (Depth 1 hingga 8) di setiap periode jendela waktu. 

{latex_vqe}
"""

with open("Contents/Lampiran/Lampiran-G.tex", "w") as f:
    f.write(doc)

print("Lampiran-G.tex berhasil dibuat.")
