import json

notebook_path = '/home/tabassam/Documents/DreamyTA/Replication/Hardware_efficient/HE_VQE_Replication.ipynb'

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Translations map (index -> new source lines)
# Only map markdown cells
translations = {
    0: [
        "# Replikasi VQE Efisien Perangkat Keras\n",
        "## Kandala et al., Nature 549, 242-246 (2017)\n",
        "\n",
        "Notebook ini mereplikasi hasil utama dari makalah penting tentang **Hardware-Efficient Variational Quantum Eigensolver (HE-VQE)** untuk estimasi energi keadaan dasar molekul.\n",
        "\n",
        "### Kontribusi Utama Makalah:\n",
        "1. **Ansatz Efisien Perangkat Keras**: Sirkuit kedalaman rendah dengan rotasi Euler (RZ-RX-RZ) dan entanglement CNOT\n",
        "2. **Pengoptimal SPSA**: Optimasi bebas gradien hanya dengan 2 pengukuran per iterasi\n",
        "3. **Simulasi Molekuler**: Energi keadaan dasar H₂, LiH, BeH₂\n",
        "\n",
        "### Kriteria Penerimaan:\n",
        "- **H₂**: Mencapai akurasi kimia (error < 1.6 mHa) pada kesetimbangan dengan kedalaman d=1\n",
        "- **LiH**: Mereproduksi fitur \"kink\" pada ~2.5 Å dengan d=1"
    ],
    1: [
        "---\n",
        "## 1. Pengaturan & Impor"
    ],
    3: [
        "---\n",
        "## 2. Ansatz Efisien Perangkat Keras\n",
        "\n",
        "Struktur ansatz mengikuti **Gambar 1c** dari makalah:\n",
        "\n",
        "$$|\\psi(\\theta)\\rangle = U_{\\text{ENT}} \\cdot U_{\\text{rot}}^{(d)} \\cdots U_{\\text{ENT}} \\cdot U_{\\text{rot}}^{(1)} \\cdot U_{\\text{rot}}^{(0)} |0\\rangle$$\n",
        "\n",
        "Di mana:\n",
        "- **Lapisan Rotasi** $U_{\\text{rot}}$: $R_Z(\\alpha) \\cdot R_X(\\beta) \\cdot R_Z(\\gamma)$ pada setiap qubit (dekomposisi Euler)\n",
        "- **Lapisan Entangler** $U_{\\text{ENT}}$: Gerbang CNOT dengan topologi linear atau bintang"
    ],
    5: [
        "---\n",
        "## 3. Hamiltonian Molekuler (H₂)\n",
        "\n",
        "Hamiltonian dibangun menggunakan **Parity Mapping** (Binary Tree Encoding) dan direduksi dari 4 menjadi 2 qubit melalui **Z₂ symmetry tapering**.\n",
        "\n",
        "Untuk H₂ pada kesetimbangan (0.74 Å):\n",
        "\n",
        "$$H = h_0 I + h_1 Z_0 + h_2 Z_1 + h_3 Z_0 Z_1 + h_4 X_0 X_1$$\n",
        "\n",
        "Suku $X_0 X_1$ sangat penting untuk entanglement!"
    ],
    7: [
        "---\n",
        "## 4. Pengoptimal SPSA\n",
        "\n",
        "**Simultaneous Perturbation Stochastic Approximation** memperkirakan gradien hanya dengan menggunakan **2 evaluasi fungsi** per iterasi:\n",
        "\n",
        "$$\\hat{g}_k = \\frac{f(\\theta + c_k \\Delta) - f(\\theta - c_k \\Delta)}{2 c_k} \\cdot \\Delta^{-1}$$\n",
        "\n",
        "Di mana $\\Delta$ adalah vektor perturbasi acak $\\pm 1$.\n",
        "\n",
        "Ini sangat penting untuk perangkat keras kuantum di mana setiap evaluasi fungsi memerlukan banyak `shot`!"
    ],
    9: [
        "---\n",
        "## 5. Eksekusi VQE\n",
        "\n",
        "Sekarang kita jalankan algoritma VQE lengkap:\n",
        "1. Inisialisasi parameter acak\n",
        "2. Ukur ekspektasi energi $\\langle \\psi(\\theta) | H | \\psi(\\theta) \\rangle$\n",
        "3. Perbarui parameter dengan SPSA\n",
        "4. Ulangi sampai konvergensi"
    ],
    12: [
        "---\n",
        "## 6. Kriteria Penerimaan #1: Akurasi Kimia H₂\n",
        "\n",
        "**Tes**: Mencapai error < 1.6 mHa pada panjang ikatan kesetimbangan (0.74 Å) dengan kedalaman d=1."
    ],
    14: [
        "---\n",
        "## 7. Kurva Disosiasi H₂\n",
        "\n",
        "Pindai jarak ikatan dari 0.3 hingga 2.5 Å dan bandingkan VQE dengan diagonalisasi eksak."
    ],
    17: [
        "---\n",
        "## 8. Kesimpulan\n",
        "\n",
        "Notebook ini mendemonstrasikan pendekatan **VQE Efisien Perangkat Keras** dari Kandala et al. (2017):\n",
        "\n",
        "### Temuan Utama:\n",
        "1. **Ansatz kedalaman rendah** (d=1) dapat mencapai akurasi kimia untuk H₂ pada kesetimbangan\n",
        "2. **Pengoptimal SPSA** efisien dengan hanya 2 pengukuran per iterasi\n",
        "3. **Pemetaan paritas + tapering** mengurangi H₂ dari 4 menjadi 2 qubit\n",
        "\n",
        "### Sorotan Implementasi:\n",
        "- `he_ansatz.py`: Rotasi Euler (RZ-RX-RZ) + entanglement CNOT\n",
        "- `molecular_hamiltonians.py`: H₂/LiH/BeH₂ dengan pemetaan paritas\n",
        "- `spsa_optimizer.py`: Aproksimasi gradien 2-pengukuran\n",
        "- `vqe_runner.py`: Loop VQE penuh dengan dukungan noise shot\n",
        "\n",
        "### Referensi:\n",
        "- Kandala, A. et al. \"Hardware-efficient variational quantum eigensolver for small molecules and quantum magnets.\" *Nature* **549**, 242-246 (2017)"
    ]
}

# Apply translations
for idx, new_source in translations.items():
    if idx < len(nb['cells']):
        if nb['cells'][idx]['cell_type'] == 'markdown':
            nb['cells'][idx]['source'] = new_source
        else:
            print(f"Warning: Cell {idx} is not markdown, skipping.")
    else:
        print(f"Warning: Cell index {idx} out of range.")

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=4)

print("Translation complete.")
