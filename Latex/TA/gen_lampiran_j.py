import pandas as pd
import numpy as np

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
        line = " & ".join([f"{v:.4f}" if isinstance(v, (float, np.float64)) else str(v) for v in row]) + " \\\\"
        latex.append(line)
    
    if longtable:
        latex.append("\\end{longtable}")
        latex.append("\\end{footnotesize}")
    
    return "\n".join(latex)

# 1. Daily Prices
df_prices = pd.read_csv("GTQuantumInvest/Hasil_N4_GT/harga_harian_saham_N4.csv")
# Reorder to match: Date, BBCA, ADRO, SMGR, TLKM
df_prices = df_prices[['Date', 'BBCA.JK', 'ADRO.JK', 'SMGR.JK', 'TLKM.JK']]
df_prices.columns = ['Tanggal', 'BBCA', 'ADRO', 'SMGR', 'TLKM']

# 2. Returns
df_rets = pd.DataFrame()
df_rets['Tanggal'] = df_prices['Tanggal']
for ticker in ['BBCA', 'ADRO', 'SMGR', 'TLKM']:
    p = df_prices[ticker]
    simple = p.pct_change()
    log = np.log(p / p.shift(1))
    df_rets[f'{ticker}_Simple'] = simple
    df_rets[f'{ticker}_Log'] = log

df_rets_clean = df_rets.dropna().reset_index(drop=True)

# 3. Expected Returns & Variance
df_metrics = pd.read_csv("GTQuantumInvest/Hasil_N4_GT/metrik_return_dan_lambda_N4.csv")
# Tickers: BBCA, ADRO, SMGR, TLKM
# Period index 1 to 36
dates = df_metrics['Date'].unique()
summary_metrics = []
for i, date in enumerate(dates, 1):
    row = {'P': i}
    for ticker in ['BBCA.JK', 'ADRO.JK', 'SMGR.JK', 'TLKM.JK']:
        t_clean = ticker.split('.')[0]
        m = df_metrics[(df_metrics['Date'] == date) & (df_metrics['Ticker'] == ticker)].iloc[0]
        row[f'{t_clean}_mu_s'] = m['Mu_Simple_Period']
        row[f'{t_clean}_mu_l'] = m['Mu_Log_Period']
        row[f'{t_clean}_var_l'] = m['Sigma_Period_Log']**2
    summary_metrics.append(row)
df_sum_metrics = pd.DataFrame(summary_metrics)

# 4. Covariance (Approximate from window logic)
# We need to compute covariance for each window (126 days ending at date)
# Let's compute it from df_rets_all
df_prices_all = pd.read_csv("GTQuantumInvest/Hasil_N4_GT/harga_harian_saham_N4.csv")
df_prices_all.set_index('Date', inplace=True)
df_prices_all = df_prices_all[['BBCA.JK', 'ADRO.JK', 'SMGR.JK', 'TLKM.JK']]
df_log_rets_all = np.log(df_prices_all / df_prices_all.shift(1)).dropna()

cov_data = []
for i, date in enumerate(dates, 1):
    # Find index of date
    idx = df_log_rets_all.index.get_loc(date)
    # Window of 126 days ending at idx
    window = df_log_rets_all.iloc[max(0, idx-125):idx+1]
    cov_matrix = window.cov() * 126 # Scale to window size
    
    row = {'P': i}
    # Pairs: BBCA-ADRO, BBCA-SMGR, BBCA-TLKM, ADRO-SMGR, ADRO-TLKM, SMGR-TLKM
    # Note: Lampiran-J old format: BBCA-BBCA, BBCA-SMGR, BBCA-TLKM, ADRO-SMGR, ADRO-TLKM, SMGR-TLKM
    # Wait, the old format had BBCA-BBCA? That's variance.
    # Let's stick to the old header names but use the right pairs.
    row['BBCA-BBCA'] = cov_matrix.loc['BBCA.JK', 'BBCA.JK']
    row['BBCA-SMGR'] = cov_matrix.loc['BBCA.JK', 'SMGR.JK']
    row['BBCA-TLKM'] = cov_matrix.loc['BBCA.JK', 'TLKM.JK']
    row['ADRO-SMGR'] = cov_matrix.loc['ADRO.JK', 'SMGR.JK']
    row['ADRO-TLKM'] = cov_matrix.loc['ADRO.JK', 'TLKM.JK']
    row['SMGR-TLKM'] = cov_matrix.loc['SMGR.JK', 'TLKM.JK']
    cov_data.append(row)
df_cov = pd.DataFrame(cov_data)

# Print to files
with open("tmp_j_prices.tex", "w") as f:
    f.write(format_latex(df_prices, "Data Harga Harian Saham Gabungan (BBCA, ADRO, SMGR, TLKM)", "tab:daily_prices_merged"))

# For returns, only show some columns if it's too wide, but old one had 9 columns.
# It uses \cmidrule so it's a bit special.
# I'll manually generate the returns table string.
def gen_rets_latex(df):
    cols = ['Tanggal', 'Simple', 'Log', 'Simple', 'Log', 'Simple', 'Log', 'Simple', 'Log']
    header1 = "Tanggal & \\multicolumn{2}{c}{BBCA} & \\multicolumn{2}{c}{ADRO} & \\multicolumn{2}{c}{SMGR} & \\multicolumn{2}{c}{TLKM} \\\\"
    header2 = "& Simple & Log & Simple & Log & Simple & Log & Simple & Log \\\\"
    
    latex = ["\\begin{footnotesize}", "\\begin{longtable}{lcccccccc}", 
             "\\caption{Data Simple Return dan Log Return Saham (BBCA, ADRO, SMGR, TLKM)} \\label{tab:daily_returns_merged} \\\\",
             "\\toprule", header1, "\\cmidrule(r){2-3} \\cmidrule(r){4-5} \\cmidrule(r){6-7} \\cmidrule(r){8-9}", header2, "\\midrule", "\\endfirsthead",
             "\\multicolumn{9}{c}{{\\bfseries Lanjutan Tabel \\thetable}} \\\\", "\\toprule", header1, 
             "\\cmidrule(r){2-3} \\cmidrule(r){4-5} \\cmidrule(r){6-7} \\cmidrule(r){8-9}", header2, "\\midrule", "\\endhead",
             "\\midrule", "\\multicolumn{9}{r}{{Bersambung...}} \\\\", "\\bottomrule", "\\endfoot", "\\bottomrule", "\\endlastfoot"]
    
    for i, row in df.iterrows():
        line = f"{row['Tanggal']} & {row['BBCA_Simple']:.5f} & {row['BBCA_Log']:.5f} & {row['ADRO_Simple']:.5f} & {row['ADRO_Log']:.5f} & {row['SMGR_Simple']:.5f} & {row['SMGR_Log']:.5f} & {row['TLKM_Simple']:.5f} & {row['TLKM_Log']:.5f} \\\\"
        latex.append(line)
    latex.append("\\end{longtable}\n\\end{footnotesize}")
    return "\n".join(latex)

with open("tmp_j_rets.tex", "w") as f:
    f.write(gen_rets_latex(df_rets_clean))

# For summary metrics
def gen_sum_metrics_latex(df):
    header1 = "P & \\multicolumn{3}{c}{BBCA} & \\multicolumn{3}{c}{ADRO} & \\multicolumn{3}{c}{SMGR} & \\multicolumn{3}{c}{TLKM} \\\\"
    header2 = "& $\\mu_s$ & $\\mu_l$ & $\\sigma_l^2$ & $\\mu_s$ & $\\mu_l$ & $\\sigma_l^2$ & $\\mu_s$ & $\\mu_l$ & $\\sigma_l^2$ & $\\mu_s$ & $\\mu_l$ & $\\sigma_l^2$ \\\\"
    
    latex = ["\\begin{footnotesize}", "\\begin{longtable}{lcccccccccccc}", 
             "\\caption{Ekspektasi Return dan Varians Log Return 36 Periode - Skala 126 Hari (BBCA, ADRO, SMGR, TLKM)} \\label{tab:expected_return_36} \\\\",
             "\\toprule", header1, "\\cmidrule(r){2-4} \\cmidrule(r){5-7} \\cmidrule(r){8-10} \\cmidrule(r){11-13}", header2, "\\midrule", "\\endfirsthead",
             "\\multicolumn{13}{c}{{\\bfseries Lanjutan Tabel \\thetable}} \\\\", "\\toprule", header1, 
             "\\cmidrule(r){2-4} \\cmidrule(r){5-7} \\cmidrule(r){8-10} \\cmidrule(r){11-13}", header2, "\\midrule", "\\endhead",
             "\\midrule", "\\multicolumn{13}{r}{{Bersambung...}} \\\\", "\\bottomrule", "\\endfoot", "\\bottomrule", "\\endlastfoot"]
    
    for i, row in df.iterrows():
        line = f"{int(row['P'])} & {row['BBCA_mu_s']:.3f} & {row['BBCA_mu_l']:.3f} & {row['BBCA_var_l']:.3f} & {row['ADRO_mu_s']:.3f} & {row['ADRO_mu_l']:.3f} & {row['ADRO_var_l']:.3f} & {row['SMGR_mu_s']:.3f} & {row['SMGR_mu_l']:.3f} & {row['SMGR_var_l']:.3f} & {row['TLKM_mu_s']:.3f} & {row['TLKM_mu_l']:.3f} & {row['TLKM_var_l']:.3f} \\\\"
        latex.append(line)
    latex.append("\\end{longtable}\n\\end{footnotesize}")
    return "\n".join(latex)

with open("tmp_j_sum_metrics.tex", "w") as f:
    f.write(gen_sum_metrics_latex(df_sum_metrics))

with open("tmp_j_cov.tex", "w") as f:
    f.write(format_latex(df_cov, "Kovarians Log Return 36 Periode - Skala 126 Hari", "tab:covariance_36"))

print("Selesai men-generate komponen Lampiran-J.")
