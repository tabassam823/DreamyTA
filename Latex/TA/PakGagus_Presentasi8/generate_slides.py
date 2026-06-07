import os
import subprocess

def generate_and_compile(n_value):
    gt_dir = f"../GTQuantumInvest/Hasil_N{n_value}_GT/Analisis_Window_N{n_value}"
    nogt_dir = f"../GTQuantumInvest/Hasil_N{n_value}_NoGT/Analisis_Window_N{n_value}"
    
    if not os.path.exists(gt_dir):
        print(f"Directory {gt_dir} not found.")
        return
    
    gt_files = set([f for f in os.listdir(gt_dir) if f.endswith("_window.png")])
    nogt_files = set([f for f in os.listdir(nogt_dir) if f.endswith("_window.png")])
    common_files = sorted(list(gt_files.intersection(nogt_files)))
    
    output_content = ""
    
    # Add Classic Comparison Slide (Slide 2, right after title)
    classic_comp_dir = "../GTQuantumInvest/classic_compare/Grafik_Perbandingan"
    classic_comp_file = f"perbandingan_VQE_vs_Classic_N{n_value}.png"
    if os.path.exists(os.path.join("PakGagus_Presentasi8", classic_comp_dir, classic_comp_file)) or os.path.exists(os.path.join(classic_comp_dir, classic_comp_file)):
        output_content += f"\\begin{{frame}}{{Perbandingan Kinerja Kumulatif: VQE vs Klasik (N={n_value})}}\n"
        output_content += "    \\begin{figure}\n"
        output_content += "        \\centering\n"
        output_content += f"        \\includegraphics[width=0.8\\textwidth]{{{classic_comp_dir}/{classic_comp_file}}}\n"
        output_content += f"        \\caption{{Perbandingan Pertumbuhan Modal Strategi VQE terhadap Tolok Ukur Klasik (N={n_value})}}\n"
        output_content += "    \\end{figure}\n"
        output_content += "\\end{frame}\n\n"

    for filename in common_files:
        date = filename.replace("_window.png", "")
        # Slide 1: Comparison Allocation
        output_content += f"\\begin{{frame}}{{Perbandingan Alokasi Portofolio N={n_value} - {date}}}\n"
        output_content += "    \\begin{figure}\n"
        output_content += "        \\centering\n"
        output_content += "        \\begin{subfigure}[b]{0.48\\textwidth}\n"
        output_content += "            \\centering\n"
        output_content += f"            \\includegraphics[width=\\textwidth]{{{gt_dir}/{filename}}}\n"
        output_content += "            \\caption{Dengan \\textit{Game Theory}}\n"
        output_content += "        \\end{subfigure}\n"
        output_content += "        \\hfill\n"
        output_content += "        \\begin{subfigure}[b]{0.48\\textwidth}\n"
        output_content += "            \\centering\n"
        output_content += f"            \\includegraphics[width=\\textwidth]{{{nogt_dir}/{filename}}}\n"
        output_content += "            \\caption{Tanpa \\textit{Game Theory}}\n"
        output_content += "        \\end{subfigure}\n"
        output_content += f"        \\caption{{Jendela Waktu {date}}}\n"
        output_content += "    \\end{figure}\n"
        output_content += "\\end{frame}\n\n"
        
        # Slide 2: Circuit Comparison (Side-by-Side) - Only for N <= 6
        circuit_file = f"{date}_circuit.png"
        gt_circ_path = os.path.join(gt_dir, circuit_file)
        nogt_circ_path = os.path.join(nogt_dir, circuit_file)
        
        if n_value <= 6 and (os.path.exists(gt_circ_path) or os.path.exists(nogt_circ_path)):
            output_content += f"\\begin{{frame}}{{Perbandingan Sirkuit Kuantum N={n_value} - {date}}}\n"
            output_content += "    \\begin{figure}\n"
            output_content += "        \\centering\n"
            output_content += "        \\begin{subfigure}[b]{0.48\\textwidth}\n"
            output_content += "            \\centering\n"
            output_content += f"            \\includegraphics[width=\\textwidth]{{{gt_dir}/{circuit_file}}}\n"
            output_content += "            \\caption{Sirkuit (GT)}\n"
            output_content += "        \\end{subfigure}\n"
            output_content += "        \\hfill\n"
            output_content += "        \\begin{subfigure}[b]{0.48\\textwidth}\n"
            output_content += "            \\centering\n"
            output_content += f"            \\includegraphics[width=\\textwidth]{{{nogt_dir}/{circuit_file}}}\n"
            output_content += "            \\caption{Sirkuit (No-GT)}\n"
            output_content += "        \\end{subfigure}\n"
            output_content += f"        \\caption{{Perbandingan Rangkaian Kuantum - {date}}}\n"
            output_content += "    \\end{figure}\n"
            output_content += "\\end{frame}\n\n"

    tex_path = f"Hasil_N{n_value}.tex"
    with open(tex_path, "w") as f:
        f.write(output_content)
    
    # Compile to PDF
    wrapper_content = f"""\\documentclass{{beamer}}
\\usepackage[utf8]{{inputenc}}
\\usepackage{{graphicx}}
\\usepackage{{subcaption}}
\\usepackage[bahasa]{{babel}}
\\captionsetup[subfigure]{{labelformat = simple, labelsep = none}}
\\renewcommand\\thesubfigure{{(\\alph{{subfigure}})\\hspace{{0.4em}}}}
\\title{{Perbandingan VQE dan GT-VQE Setiap Jendela Rebalance periode 2021-2023\\\\(Sistem N={n_value})}}
\\author{{}}
\\date{{}}
\\begin{{document}}
\\maketitle
\\input{{{tex_path}}}
\\end{{document}}
"""
    wrapper_name = f"temp_N{n_value}.tex"
    with open(wrapper_name, "w") as f:
        f.write(wrapper_content)
    
    print(f"Compiling N={n_value}...")
    subprocess.run(["pdflatex", "-interaction=nonstopmode", wrapper_name], stdout=subprocess.DEVNULL)
    if os.path.exists(f"temp_N{n_value}.pdf"):
        os.rename(f"temp_N{n_value}.pdf", f"Hasil_N{n_value}.pdf")
    
    # Cleanup temp
    for ext in ["aux", "log", "out", "snm", "toc", "nav", "tex"]:
        tmp = f"temp_N{n_value}.{ext}"
        if os.path.exists(tmp): os.remove(tmp)

if __name__ == "__main__":
    for n in [2, 4, 6, 8, 10, 12]:
        generate_and_compile(n)
