# Struktur Presentasi Tugas Akhir (PPT)
**Judul:** Integrasi Exact Potential Game dan Variational Quantum Eigensolver untuk Optimasi Portofolio Hibrida

## Distribusi Slide (Total Estimasi: 30-33 Slide)

### I. Pendahuluan (Bab 1.1 - 1.5) (9 Slide)
1. **Slide 1: Judul dan Identitas**
   - Judul Penelitian, Nama Peneliti, Pembimbing.
2. **Slide 2: 1.1 Latar Belakang - Limitasi Model Markowitz**
   - Kegagalan asumsi distribusi normal dan ketergantungan non-linear.
3. **Slide 3: 1.1 Latar Belakang - Pendekatan Ekonofisika**
   - Pemetaan pasar ke sistem energi Hamiltonian Ising.
4. **Slide 4: 1.1 Latar Belakang - Integrasi Teori Permainan**
   - Pemanfaatan Exact Potential Game (EPG) untuk dinamika strategis.
5. **Slide 5: 1.1 Latar Belakang - Strategi Warm-Start**
   - Mengatasi Barren Plateaus melalui inisialisasi Nash Equilibrium.
6. **Slide 6: 1.1 Latar Belakang - VQE dan Optimasi SPSA**
   - Algoritma hibrida dan efisiensi estimasi gradien stokastik.
7. **Slide 7: 1.2 Rumusan Masalah**
   - Tiga pertanyaan kunci terkait EPG, Warm-start, dan performa VQE.
8. **Slide 8: 1.3 Tujuan Penelitian**
   - Target analisis formulasi, evaluasi efisiensi, dan pengujian kapabilitas.
9. **Slide 9: 1.4 Batasan Masalah**
   - N=2/N=4, EPG, SBR, dan framework PennyLane.
10. **Slide 10: 1.5 Manfaat Penelitian**
    - Kontribusi metode optimasi tangguh dan literatur komputasi kuantum.

### II. Landasan Teori (Bab 2.1 - 2.8) (8 Slide)
11. **Slide 11: Bab 2.1 - Dinamika Pasar Finansial**
    - Evolusi uang, Inflasi sebagai entropi ekonomi, dan prinsip Investasi.
12. **Slide 12: Bab 2.2 - Representasi Data Finansial**
    - Analisis Fundamental, Teknikal (SnR), dan Kuantitatif (Log-Return).
13. **Slide 13: Bab 2.3 - Teori Permainan dan EPG**
    - Ekuilibrium Nash, koordinasi Stag Hunt, dan formalisme fungsi potensial global.
    - Lampiran A
14. **Slide 14: Bab 2.4 - Hamiltonian Ising**
    - Sejarah model Ising, representasi aset sebagai *spin*, dan pemetaan QUBO ke Pauli-Z.
15. **Slide 15: Bab 2.5 - Fondasi Komputer Kuantum**
    - Sistem Qubit (Bola Bloch), Gerbang Kuantum (Rotasi dan CNOT), dan PQC.
16. **Slide 16: Bab 2.6 - Optimasi Parameter Klasik**
    - Parameter Shift Rule, Gradient Descent, dan efisiensi algoritma SPSA.
17. **Slide 17: Bab 2.7 - Algoritma VQE**
    - Prinsip Variasional (Rayleigh-Ritz), Ansatz EfficientSU2, dan siklus hibrida.
18. **Slide 18: Bab 2.8 - Validasi Barren Plateau**
    - Fenomena dataran tandus dan diagnostik menggunakan Entropi Von Neumann.

### III. Metodologi (3 Slide)
19. **Slide 19: Alur Metodologi Hibrida**
    - Diagram alir: Data -> EPG (PSNE) -> Hamiltonian (QUBO) -> VQE.
20. **Slide 20: Formulasi Hamiltonian Ising Spesifik**
    - Parameter $h_i$ (bias) dan $J_{ij}$ (kopling) dengan suku penalti budget $A$.
21. **Slide 21: Konfigurasi Sirkuit dan Optimizer**
    - Setting PennyLane, hyperparameter SPSA, dan kedalaman ansatz.

### IV. Hasil dan Pembahasan (6 Slide)
22. **Slide 22: Strategi Warm-Start dan Nash Equilibrium**
    - Perbandingan inisialisasi parameter (Random vs Nash).
23. **Slide 23: Analisis Konvergensi Energi**
    - Grafik konvergensi GT-VQE vs VQE Murni.
24. **Slide 24: Dinamika Internal (Entropy Analysis)**
    - Evolusi Entropi Von Neumann dan fenomena collapsing state.
25. **Slide 25: Hasil Backtesting Portofolio (N=2 dan N=4)**
    - Metrik finansial: Sharpe Ratio unggulan 1,0107.
26. **Slide 26: Analisis Jendela Waktu Ekstrem**
    - Agilitas rebalancing saat volatilitas pasar tinggi.
27. **Slide 27: Perbandingan Efisiensi Kedalaman Sirkuit**
    - Pengaruh jumlah layer terhadap akurasi dan noise.

### V. Penutup (2 Slide)
28. **Slide 28: Kesimpulan**
    - Ringkasan temuan utama menjawab rumusan masalah.
29. **Slide 29: Saran dan Penutup**
    - Pengembangan lanjut dan sesi tanya jawab.
