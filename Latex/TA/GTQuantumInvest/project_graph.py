import marimo

__generated_with = "0.23.5"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import os
    import re

    return mo, os, re


@app.cell
def _(mo, os, re):
    # Fungsi untuk mencari file apa saja yang di-import oleh sebuah file
    def scan_dependencies(file_path, project_files):
        found_deps = set()
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                # Mencari pola 'import nama_file' atau 'from nama_file import ...'
                for other_file in project_files:
                    module_name = other_file.replace('.py', '')
                    # Regex untuk memastikan kita tidak salah mencocokkan kata di dalam string
                    pattern = rf'\b(import|from)\s+{module_name}\b'
                    if re.search(pattern, content):
                        found_deps.add(other_file)
        except:
            pass
        return found_deps

    def draw_project_map():
        root = os.getcwd()
        # Filter: Hanya ambil file .py, abaikan project_graph.py dan main_N...py
        all_py_files = [
            f for f in os.listdir(root) 
            if f.endswith('.py') 
            and f != 'project_graph.py'
            and not re.match(r'main_N\d+\.py', f)
        ]

        mermaid_lines = ["graph TD"]

        # Tambahkan gaya visual yang lebih kaya
        mermaid_lines.append("    classDef core fill:#FF9800,stroke:#E65100,stroke-width:2px,color:white;")
        mermaid_lines.append("    classDef strategy fill:#2196F3,stroke:#0D47A1,stroke-width:2px,color:white;")
        mermaid_lines.append("    classDef engine fill:#4CAF50,stroke:#1B5E20,stroke-width:2px,color:white;")
        mermaid_lines.append("    classDef math fill:#9C27B0,stroke:#4A148C,stroke-width:1px,color:white;")

        # Kategorisasi File
        categories = {
            'core': ['main.py', 'config.py', 'backtest_runner.py', 'report_generator.py', 'plot_generator.py', 'data_downloader.py'],
            'strategy': ['run_strategy_step.py', 'rebalance_portfolio.py'],
            'engine': ['run_vqe_adaptive.py', 'find_nash_sbr.py', 'brute_force_validator.py', 'find_optimal_lr_spsa.py', 'run_spsa_test.py'],
            'math': [f for f in all_py_files if f.startswith(('calc_', 'compute_', 'build_'))]
        }

        def get_style(filename):
            for cat, files in categories.items():
                if filename in files:
                    return f":::{cat}"
            return ""

        has_connections = False
        seen_edges = set()

        for file in all_py_files:
            deps = scan_dependencies(os.path.join(root, file), all_py_files)

            # Styling node berdasarkan kategori
            style = get_style(file)
            mermaid_lines.append(f'    {file.replace(".", "_")}["{file}"]{style}')

            for dep in deps:
                if file != dep:
                    src = file.replace(".", "_")
                    dst = dep.replace(".", "_")
                    edge = (src, dst)
                    if edge not in seen_edges:
                        mermaid_lines.append(f"    {src} --> {dst}")
                        seen_edges.add(edge)
                        has_connections = True
        if not has_connections:
            return mo.md("### ⚠️ Tidak ditemukan hubungan import antar file.\nPastikan file Anda menggunakan `import nama_file_lain`.")

        return mo.vstack([
            mo.md("# 🗺️ Peta Hubungan Kode Proyekmu"),
            mo.md("Garis panah menunjukkan file mana yang 'memanggil' file lainnya."),
            mo.mermaid("\n".join(mermaid_lines))
        ])

    draw_project_map()
    return


if __name__ == "__main__":
    app.run()
