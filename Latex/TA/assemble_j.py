with open("tmp_j_prices.tex", "r") as f: prices = f.read()
with open("tmp_j_rets.tex", "r") as f: rets = f.read()
with open("tmp_j_sum_metrics.tex", "r") as f: metrics = f.read()
with open("tmp_j_cov.tex", "r") as f: cov = f.read()

latex = f"""\\chapter{{Data Harga Harian Saham}}
\\label{{appendix:daily_prices}}

Lampiran ini menyajikan dataset \\textit{{adjusted closing price}} atau harga penutupan aset yang disesuaikan untuk empat aset utama (BBCA, ADRO, SMGR, TLKM) yang digunakan selama periode simulasi.

{prices}

{rets}

{metrics}

{cov}
"""
with open("Contents/Lampiran/Lampiran-J.tex", "w") as f:
    f.write(latex)
