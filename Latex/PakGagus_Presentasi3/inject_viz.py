import json

file_path = '/home/tabassam/Documents/DreamyTA/Latex/PakGagus_Presentasi3/kombinasi_4.ipynb'

with open(file_path, 'r') as f:
    data = json.load(f)

for cell in data['cells']:
    if cell['cell_type'] == 'code':
        # Check if this is the correct cell
        if any('# 5. Eksekusi HE-VQE dengan SPSA' in line for line in cell['source']):
            print("Found target cell.")
            new_source = []
            inserted = False
            for line in cell['source']:
                new_source.append(line)
                # Insert after printing initial cost
                if 'print(f"Initial cost: {initial_cost:.6f}")' in line:
                    new_source.append("\n")
                    new_source.append("# Visualisasi Sirkuit (Added)\n")
                    new_source.append("print(\"\\nGenerating circuit image...\")\n")
                    new_source.append("try:\n")
                    new_source.append("    fig, ax = qml.draw_mpl(vqe_circuit, decimals=2)(initial_params)\n")
                    new_source.append("    plt.title(f\"Hardware-Efficient Ansatz (HE-VQE)\\n{n_qubits} Qubits, Depth={depth}\", fontsize=14)\n")
                    new_source.append("    plt.show()\n")
                    new_source.append("except Exception as e:\n")
                    new_source.append("    print(f\"  WARNING: Failed to generate circuit image: {e}\")\n")
                    new_source.append("\n")
                    inserted = True
            
            if inserted:
                cell['source'] = new_source
                print("Injected visualization code.")
            else:
                print("WARNING: Could not find insertion point in target cell.")
            break

with open(file_path, 'w') as f:
    json.dump(data, f, indent=1)

print("Saved updated notebook.")
