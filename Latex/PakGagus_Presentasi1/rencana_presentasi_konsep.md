# Rencana Presentasi: Konsep Fundamental Optimisasi Portofolio Kuantum
**Fokus:** Penjelasan Mendalam Konsep Teknis (QUBO, Ansatz, Cost Functions, Optimizers)
**Target Audiens:** Mahasiswa S1/Akademisi yang ingin memahami "How it works"
**Format:** LaTeX Beamer

---

## Bagian 1: Pendahuluan & Formulasi Masalah

### Slide 1: Judul
- **Judul:** Bedah Konsep: Algoritma VQE untuk Optimisasi Portofolio
- **Sub-judul:** Dari Model Matematis hingga Implementasi Sirkuit Kuantum
- **Presenter:** [Nama Anda]
- **Tujuan:** Menjelaskan mekanisme di balik layar: QUBO, Ansatz, WCVaR, dan CMA-ES.

### Slide 2: Model Matematika Portofolio (Modern Portfolio Theory)
- **Konsep:** Bagaimana masalah keuangan ditulis dalam matematika?
- **Poin Kunci:**
    1.  **Return ($\mu$):** Keuntungan rata-rata (Linear). Ingin dimaksimalkan.
    2.  **Risiko ($\sigma$):** Matriks kovariansi antar aset (Kuadratik). Ingin diminimalkan.
    3.  **Persamaan Gabungan:** $C' = -\lambda(\text{Return}) + (1-\lambda)(\text{Risiko})$.
- **Saran Gambar:** Grafik **Efficient Frontier**. Kurva melengkung yang menunjukkan *trade-off* di mana sumbu X adalah Risiko dan sumbu Y adalah Return. Titik-titik di bawah kurva adalah portofolio yang tidak efisien.
    - *Solusi:* Gunakan Skrip Python 1 di Lampiran.

### Slide 3: QUBO (Quadratic Unconstrained Binary Optimization)
- **Konsep:** Jembatan antara Matematika Keuangan dan Fisika Kuantum.
- **Poin Kunci:**
    - **Quadratic:** Karena adanya interaksi risiko antar saham ($\sigma_{ij} x_i x_j$).
    - **Binary:** Variabel keputusan 0 (Tidak Beli) atau 1 (Beli).
    - **Unconstrained:** Batasan "Budget" diubah menjadi **Penalti**.
    - **NP-Hard:** Kompleksitas meningkat eksponensial, sulit bagi komputer klasik.
- **Saran Gambar:** Visualisasi **Sumur Penalti (Penalty Well)**. Grafik parabola sederhana $y = (x - target)^2$.
    - *Solusi:* Gunakan Skrip Python 2 di Lampiran.

### Slide 4: Implementasi Fisika (Mapping ke Hamiltonian)
- **Konsep:** Bagaimana menerjemahkan bit (0/1) menjadi bahasa kuantum (Spin/Qubit).
- **Poin Kunci:**
    1.  **Transformasi Variabel:** $x_i \in \{0,1\} \to s_i \in \{+1,-1\} \to \hat{Z}_i$.
    2.  **Hamiltonian Ising:** $\hat{H} = -\sum h_i \hat{Z}_i - \sum J_{ij} \hat{Z}_i \hat{Z}_j$.
    3.  **Interpretasi Fisik:**
        - $h_i$ (Medan Magnet Lokal) $\approx$ Return Saham.
        - $J_{ij}$ (Interaksi Spin) $\approx$ Risiko/Kovariansi.
    4.  **Tujuan:** Mencari Energi Minimum $\equiv$ Profit Maksimum.

---

## Bagian 2: Komponen Sirkuit Kuantum (The Quantum Part)

### Slide 5: Konsep VQE & Ansatz
- **Konsep:** *Variational Quantum Eigensolver* sebagai algoritma hibrida.
- **Poin Kunci:**
    - **VQE:** Mencari energi terendah (*ground state*) secara iteratif.
    - **Ansatz:** "Tebakan Awal" fungsi gelombang $|\psi(\theta)\rangle$.
    - **Parameter $\theta$:** Knob yang diputar-putar oleh komputer klasik untuk mencari bentuk gelombang terbaik.

### Slide 6: Two-Local Ansatz (Struktur Standar)
- **Konsep:** Desain sirkuit yang umum digunakan di era NISQ.
- **Poin Kunci:**
    - **Struktur:** Berlapis (*Layered*).
    - **Komponen:**
        - Rotasi Single Qubit ($R_y, R_z$): Eksplorasi superposisi.
        - Entanglement ($CNOT$): Mensimulasikan korelasi/interaksi antar aset.
    - **Karakteristik:** Sederhana, mudah diimplementasikan, tapi mungkin kurang ekspresif.
- **Saran Gambar:** Diagram sirkuit `Two-Local`. (Anda sudah memiliki gambar ini: `Gambar_1a.png`)

### Slide 7: Block Ansatz (Struktur Modular)
- **Konsep:** Desain alternatif berbasis blok fungsional.
- **Poin Kunci:**
    - **Struktur:** Modular (*Block-based*).
    - **Mekanisme:** Qubit diproses secara intensif dalam satu blok sebelum lanjut ke blok lain.
    - **Kelebihan:** Menciptakan korelasi yang lebih dalam (*deeper entanglement*) dan operasi *controlled-unitary* yang fleksibel.
- **Saran Gambar:** Diagram sirkuit `Block Ansatz`. (Anda sudah memiliki gambar ini: `Gambar_1b.png`)

---

## Bagian 3: Fungsi Biaya (Cost Function) - Inovasi Utama

### Slide 8: Evolusi Fungsi Biaya: Dari Rata-rata ke CVaR
- **Konsep:** Mengapa "Rata-rata Energi" itu buruk untuk optimisasi.
- **Poin Kunci:**
    - **Expectation Value (Mean):** Merata-rata seluruh hasil sampling. Solusi bagus sering tertutup oleh solusi buruk.
    - **CVaR (Conditional Value-at-Risk):** Hanya mengambil rata-rata dari **Ekor Distribusi** ($\alpha\%$ terendah).
    - **Logika:** Fokus hanya pada kandidat solusi terbaik, abaikan sampah.
- **Saran Gambar:** Histogram distribusi energi. Tunjukkan area $\alpha$ di ujung kiri (energi rendah) yang diambil untuk perhitungan.

### Slide 9: Weighted CVaR (WCVaR)
- **Konsep:** Penyempurnaan CVaR (Inovasi Paper).
- **Poin Kunci:**
    - **Masalah CVaR:** Memberi bobot SAMA pada Juara 1 dan Juara Terakhir dalam daftar top $\alpha$.
    - **Solusi WCVaR:** Memberi bobot BERBEDA berdasarkan **Ranking**.
    - **Rumus Bobot:** $w_k = \exp(-\beta k)$ (Meluruh secara eksponensial).
    - **Efek:** Memberi sinyal sangat kuat ke optimizer jika menemukan solusi ranking 1.
- **Saran Gambar:** Grafik perbandingan **Kurva Bobot**. Garis lurus (CVaR) vs Kurva meluruh (WCVaR).
    - *Solusi:* Gunakan Skrip Python 3 di Lampiran.

---

## Bagian 4: Pengoptimasi Klasik (The Classical Optimizer)

### Slide 10: COBYLA vs CMA-ES
- **Konsep:** Perbandingan mekanisme kerja optimizer.
- **Poin Kunci:**
    - **COBYLA:** Pendekatan linear, single agent. Mudah terjebak lokal minima.
    - **CMA-ES:** Populasi banyak agen, evolusioner. Mampu beradaptasi dengan landscape kasar (WCVaR).
- **Saran Gambar:** Ilustrasi **Populasi CMA-ES**. Menunjukkan sebaran titik (generasi awal) yang perlahan mengerucut ke satu titik tengah (generasi akhir) di atas peta kontur.
    - *Solusi:* Gunakan Skrip Python 4 di Lampiran.

---

## Bagian 5: Kesimpulan Integrasi

### Slide 11: The Big Picture (Integrasi Sistem)
- **Konsep:** Bagaimana semua komponen bekerja sama.
- **Alur Kerja:**
    1.  **QUBO:** Masalah Keuangan $\rightarrow$ Fisika.
    2.  **Ansatz:** Membentuk kandidat solusi.
    3.  **WCVaR:** Menilai kualitas solusi.
    4.  **CMA-ES:** Mengarahkan pencarian.
- **Saran Gambar:** Diagram Alur Kerja (Flowchart).
    - *Solusi:* Gunakan kode **TikZ** di Lampiran untuk digenerate langsung di LaTeX.

### Slide 12: Sesi Diskusi
- Ruang untuk pertanyaan mendalam.

---

# Lampiran: Panduan Generasi Gambar (Python & TikZ)

Berikut adalah kode yang bisa Anda jalankan (di Jupyter Notebook atau Python script) untuk menghasilkan gambar PNG berkualitas tinggi untuk slide presentasi Anda.

### 1. Skrip Python: Efficient Frontier (Slide 3)
```python
import numpy as np
import matplotlib.pyplot as plt

# Dummy Data
np.random.seed(42)
returns = np.random.normal(0.1, 0.2, 500)
risks = np.random.normal(0.15, 0.05, 500)

plt.figure(figsize=(6, 4))
plt.scatter(risks, returns, c='lightgray', label='Portofolio Tidak Efisien')
# Pareto Front (Simple approximation for visual)
sorted_indices = np.argsort(risks)
pareto_risks = risks[sorted_indices]
pareto_returns = np.maximum.accumulate(returns[sorted_indices])
plt.plot(pareto_risks, pareto_returns, 'r-', linewidth=3, label='Efficient Frontier')

plt.title('Konsep Efficient Frontier')
plt.xlabel('Risiko ($\sigma$)')
plt.ylabel('Return ($\mu$)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.savefig('slide3_efficient_frontier.png', dpi=300)
plt.show()
```

### 2. Skrip Python: Sumur Penalti (Slide 4)
```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 12, 400)
target = 6
penalty = 10 * (x - target)**2

plt.figure(figsize=(6, 4))
plt.plot(x, penalty, 'b-', linewidth=3)
plt.axvline(x=target, color='r', linestyle='--', label=f'Target (N/2 = {target})')
plt.text(target, 100, 'Solusi Valid\n(Energi Rendah)', ha='center', color='green')
plt.text(2, 200, 'Melanggar Aturan\n(Energi Tinggi)', ha='center', color='red')
plt.text(10, 200, 'Melanggar Aturan\n(Energi Tinggi)', ha='center', color='red')

plt.title('Konsep Sumur Penalti (Penalty Well)')
plt.xlabel('Jumlah Aset yang Dipilih')
plt.ylabel('Energi Penalti')
plt.ylim(0, 360)
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('slide4_penalty_well.png', dpi=300)
plt.show()
```

### 3. Skrip Python: Perbandingan Bobot WCVaR (Slide 9)
```python
import numpy as np
import matplotlib.pyplot as plt

k = np.arange(1, 21) # Ranking 1 sampai 20
cvar_weights = np.ones_like(k) # Bobot rata
wcvar_weights = np.exp(-0.3 * k) # Bobot eksponensial

plt.figure(figsize=(6, 4))
plt.plot(k, cvar_weights, 'b--', linewidth=2, label='CVaR Standar (Bobot Rata)')
plt.plot(k, wcvar_weights, 'r-', linewidth=3, marker='o', label='WCVaR (Bobot Eksponensial)')

plt.title('Perbandingan Pembobotan: CVaR vs WCVaR')
plt.xlabel('Ranking Solusi (1 = Terbaik)')
plt.ylabel('Besar Bobot ($w_k$)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('slide9_weights.png', dpi=300)
plt.show()
```

### 4. Skrip Python: Ilustrasi CMA-ES (Slide 10)
```python
import numpy as np
import matplotlib.pyplot as plt

# Buat fungsi kontur (Landscape)
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2  # Fungsi mangkok sederhana

plt.figure(figsize=(6, 5))
plt.contourf(X, Y, Z, levels=20, cmap='viridis', alpha=0.6)

# Generasi Awal (Tersebar)
gen1_x = np.random.uniform(-2.5, 2.5, 10)
gen1_y = np.random.uniform(-2.5, 2.5, 10)
plt.scatter(gen1_x, gen1_y, color='red', marker='x', s=50, label='Generasi Awal (Acak)')

# Generasi Akhir (Konvergen)
genN_x = np.random.normal(0, 0.2, 10)
genN_y = np.random.normal(0, 0.2, 10)
plt.scatter(genN_x, genN_y, color='white', edgecolors='black', s=80, label='Generasi Akhir (Konvergen)')

plt.title('Ilustrasi Kerja CMA-ES')
plt.legend()
plt.savefig('slide10_cmaes.png', dpi=300)
plt.show()
```

### 5. Kode TikZ: Big Picture Flowchart (Slide 11)
*Sisipkan kode ini langsung di dalam file `.tex` Anda pada slide yang sesuai. Pastikan paket `\usepackage{tikz}` sudah ada di preamble.*

```latex
\begin{tikzpicture}[node distance=1.5cm, auto]
    % Styles
    \tikzstyle{block} = [rectangle, draw, fill=blue!20, text width=5em, text centered, rounded corners, minimum height=3em]
    \tikzstyle{line} = [draw, -latex']
    \tikzstyle{cloud} = [draw, ellipse, fill=red!20, node distance=3cm, minimum height=2em]

    % Nodes
    \node [block] (qubo) {1. QUBO Formulation};
    \node [block, right of=qubo, node distance=3cm] (ansatz) {2. Quantum Circuit (Ansatz)};
    \node [block, right of=ansatz, node distance=3cm] (wcvar) {3. WCVaR Evaluation};
    \node [block, right of=wcvar, node distance=3cm] (cmaes) {4. CMA-ES Update};
    
    % Edges
    \path [line] (qubo) -- (ansatz);
    \path [line] (ansatz) -- (wcvar);
    \path [line] (wcvar) -- (cmaes);
    \path [line] (cmaes) |- (0,-1.5) -| (ansatz); % Loop feedback
    
    % Labels
    \node [below of=ansatz, node distance=2cm] (loop_label) {\textit{Loop Optimisasi}};
\end{tikzpicture}
```