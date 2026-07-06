import os
import re
import base64
import requests # Pastikan library requests tersedia

def scan_dependencies(file_path, project_files):
    found_deps = set()
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            for other_file in project_files:
                module_name = other_file.replace('.py', '')
                pattern = rf'\b(import|from)\s+{module_name}\b'
                if re.search(pattern, content):
                    found_deps.add(other_file)
    except:
        pass
    return found_deps

def generate_mermaid():
    root = os.getcwd()
    all_py_files = [
        f for f in os.listdir(root) 
        if f.endswith('.py') 
        and f not in ['project_graph.py', 'export_graph.py']
        and not re.match(r'main_N\d+\.py', f)
    ]

    mermaid_lines = ["graph TD"]
    mermaid_lines.append("    classDef core fill:#FF9800,stroke:#E65100,stroke-width:2px,color:white;")
    mermaid_lines.append("    classDef strategy fill:#2196F3,stroke:#0D47A1,stroke-width:2px,color:white;")
    mermaid_lines.append("    classDef engine fill:#4CAF50,stroke:#1B5E20,stroke-width:2px,color:white;")
    mermaid_lines.append("    classDef math fill:#9C27B0,stroke:#4A148C,stroke-width:1px,color:white;")

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

    seen_edges = set()
    for file in all_py_files:
        style = get_style(file)
        mermaid_lines.append(f'    {file.replace(".", "_")}["{file}"]{style}')
        deps = scan_dependencies(os.path.join(root, file), all_py_files)
        for dep in deps:
            if file != dep:
                src = file.replace(".", "_")
                dst = dep.replace(".", "_")
                if (src, dst) not in seen_edges:
                    mermaid_lines.append(f"    {src} --> {dst}")
                    seen_edges.add((src, dst))
    
    return "\n".join(mermaid_lines)

def export_png(mermaid_text, output_file="project_graph.png"):
    print("Mengonversi Mermaid ke PNG via mermaid.ink...")
    # Encode ke base64
    graphbytes = mermaid_text.encode("ascii")
    base64_bytes = base64.b64encode(graphbytes)
    base64_string = base64_bytes.decode("ascii")
    
    url = "https://mermaid.ink/img/" + base64_string
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(output_file, "wb") as f:
                f.write(response.content)
            print(f"Berhasil! Gambar disimpan sebagai: {output_file}")
        else:
            print(f"Gagal mengunduh gambar. Status code: {response.status_code}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    mermaid_str = generate_mermaid()
    export_png(mermaid_str)
