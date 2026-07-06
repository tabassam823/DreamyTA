# Deep Dive: Dari Classical Bayesian Game ke Quantum EWL Framework

Dokumen ini memberikan penjelasan mendalam mengenai transisi teoritis dari **Game Theory Klasik** menuju **Quantum Bayesian Game Theory** menggunakan skema **EWL (Eisert-Wilkens-Lewenstein)**. Penjelasan ini disusun berdasarkan alur logika pada diagram arsitektur sistem (`mermaid_graph-1.png`).

---

## 1. Landasan Teori: Classical Bayesian Game Theory
*(Merujuk pada Fase 1 & 2 Diagram: Input & Pembentukan Model)*

### 1.1. Definisi dan Konsep Dasar
Dalam Game Theory standar, diasumsikan bahwa semua pemain memiliki informasi sempurna (*complete information*) mengenai aturan permainan dan fungsi payoff lawan. Namun, di pasar keuangan nyata, ketidakpastian adalah hal yang mutlak.

**Bayesian Game Theory** (diperkenalkan oleh John Harsanyi) menangani situasi **informasi tidak lengkap** (*incomplete information*), di mana setidaknya satu pemain tidak mengetahui "tipe" dari pemain lain atau kondisi lingkungan ("Nature").

Dalam konteks arsitektur kita:
*   **Pemain Utama**: Investor/Algoritma Portofolio.
*   **Lawan (Nature)**: Pasar Saham.
*   **Tipe (Types)**: Kondisi Pasar (misal: *Bullish*, *Bearish*, atau *Sideways*).
*   **Ketidakpastian**: Investor tidak tahu pasti tipe pasar saat ini, tetapi memiliki keyakinan awal (*prior belief*) berupa probabilitas (misal: 60% Bull, 40% Bear).

### 1.2. Transformasi Harsanyi
Untuk menyelesaikan permainan ini, kita menggunakan **Transformasi Harsanyi**, yang mengubah permainan informasi tidak lengkap menjadi permainan informasi tidak sempurna namun lengkap (*complete but imperfect information*).

1.  **Nature Move**: "Alam" memilih tipe pasar (Bull/Bear) berdasarkan probabilitas tertentu.
2.  **Player Move**: Investor memilih strategi alokasi aset.
3.  **Payoff**: Bergantung pada strategi investor DAN tipe pasar yang dipilih Nature.

Matriks Payoff menjadi **Matriks Payoff Terupdate** (lihat diagram Fase 2), di mana nilai ekspektasi payoff adalah rata-rata terbobot:
$$ \mathbb{E}[\text{Payoff}] = \sum_{t \in \text{Types}} P(t) \cdot u(\text{Strategi}, t) $$

---

## 2. Jembatan Kuantum: Skema EWL (Eisert-Wilkens-Lewenstein)
*(Merujuk pada Fase 1: Quantum Mechanics & EWL Scheme)*

### 2.1. Mengapa Perlu Kuantum?
Dalam permainan klasik, pemain terbatas pada strategi murni (pilih A atau B) atau strategi campuran (probabilitas klasik pilih A atau B).
Skema **EWL** memperkenalkan properti mekanika kuantum:
*   **Superposisi**: Strategi bukan lagi pilihan biner, tetapi kombinasi linier dari basis strategi.
*   **Entanglement**: Memungkinkan korelasi non-lokal antar pemain (atau antar aset dalam portofolio) yang lebih kuat daripada korelasi klasik.
*   **Interferensi**: Amplitudo probabilitas dapat saling menguatkan atau meniadakan, memungkinkan solusi yang tidak terjangkau secara klasik (Pareto Optimal).

### 2.2. Protokol Standar EWL
Protokol EWL beroperasi dalam 3 tahap utama yang dipetakan ke sirkuit kuantum:

1.  **Entangling Operator ($\hat{J}$)**:
Mempersiapkan state awal yang terbelit.
    $$ |\psi_{ent}\rangle = \hat{J} |00\dots0\rangle $$
    Biasanya, $\hat{J} = \exp(i \frac{\gamma}{2} \sigma_x^{\otimes n})$ untuk menciptakan korelasi maksimal.

2.  **Strategy Operator ($\hat{U}$)**:
Pemain menerapkan strategi mereka melalui operator uniter lokal. Dalam konteks portofolio, parameter rotasi ($\theta, \phi$) merepresentasikan bobot alokasi aset.
    $$ |\psi_{strat}\rangle = (\hat{U}_1 \otimes \hat{U}_2 \otimes \dots) |\psi_{ent}\rangle $$

3.  **Disentangling Operator ($\hat{J}^\dagger$)**:
Operasi invers untuk mengembalikan basis sebelum pengukuran.
    $$ |\psi_{fin}\rangle = \hat{J}^\dagger |\psi_{strat}\rangle $$

---

## 3. Integrasi: Quantum Bayesian Game Model
*(Merujuk pada Fase 2: Integrasi ke Bayesian Weighted Hamiltonian)*

Ini adalah inti dari inovasi model yang diajukan. Kita menggabungkan ketidakpastian tipe pasar (Bayesian) dengan kekuatan komputasi operasional EWL.

### 3.1. Mapping "Nature" ke Operator Kuantum
Alih-alih menyelesaikan satu permainan kuantum tunggal, kita menganggap bahwa sistem berada dalam superposisi dari berbagai "permainan" yang mungkin terjadi (Bull atau Bear).

Dalam diagram, ini direpresentasikan oleh node **Bayesian Weighted Hamiltonian**.

Konstruksinya adalah sebagai berikut:
1.  Kita mendefinisikan **Hamiltonian Pasar Bull** ($H_{bull}$) dan **Hamiltonian Pasar Bear** ($H_{bear}$) berdasarkan matriks payoff masing-masing kondisi. Hamiltonian ini dikonstruksi dari operator Pauli yang sesuai dengan skema EWL.
2.  Kita menggunakan probabilitas Bayesian ($p_{bull}, p_{bear}$) dari analisis data (Sentiment/Statistik) sebagai bobot.

### 3.2. Bayesian Weighted Hamiltonian
Hamiltonian total sistem ($H_{total}$) yang akan dipecahkan oleh VQE bukan lagi Hamiltonian statis tunggal, melainkan ekspektasi terbobot:

$$ H_{total} = p_{bull} \cdot H_{bull} + p_{bear} \cdot H_{bear} $$

Ini berarti:
*   Jika pasar sangat mungkin Bull ($p_{bull} \to 1$), sistem akan berkonvergensi ke strategi optimal untuk pasar Bull.
*   Jika pasar tidak pasti ($p \approx 0.5$), sistem akan mencari strategi "titik tengah" (Robust Optimization) yang paling aman untuk kedua kondisi.

---

## 4. Eksekusi: Variational Quantum Eigensolver (VQE)
*(Merujuk pada Fase 3: Eksekusi VQE)*

Setelah model matematika terbentuk dalam $H_{total}$, kita masuk ke eksekusi komputasi.

### 4.1. Sirkuit Kuantum EWL sebagai Ansatz
Dalam VQE, sirkuit kuantum EWL bertindak sebagai **Ansatz** (tebakan struktur sirkuit). Parameter strategi pemain ($\theta$) menjadi parameter variasi yang akan dioptimalkan.

*   **Input**: State $|0\rangle$.
*   **Proses**: Entanglement $\to$ Rotasi Parameter ($\theta$) $\to$ Disentanglement.
*   **Output**: State $|̂\psi(\theta)\rangle$.

### 4.2. Pengukuran Energi (Cost Function)
Kita mengukur nilai ekspektasi energi dari Hamiltonian Bayesian terhadap state yang dihasilkan sirkuit:

$$ \langle E \rangle = \langle \psi(\theta) | H_{total} | \psi(\theta) \rangle $$

Nilai ini merepresentasikan **Negatif dari Ekspektasi Return Portofolio** (atau ukuran risiko yang ingin diminimalkan).

### 4.3. Loop Optimasi Hibrida
Sesuai diagram:
1.  **Quantum**: Menghitung $\langle E \rangle$.
2.  **Klasik (Bayesian Optimization/CMA-ES)**: Menerima nilai cost, lalu memperbarui parameter $\theta$ untuk mencari nilai minimum.
3.  **Iterasi**: Berulang hingga konvergen ($\theta_{optimal}$). 

## Kesimpulan
Model ini menawarkan pendekatan novel di mana:
1.  **Bayesian Game** menangani ketidakpastian eksternal (Kondisi Pasar).
2.  **EWL Scheme** menangani korelasi internal antar aset (Entanglement).
3.  **VQE** bertindak sebagai "solver" untuk mencari Keseimbangan Nash (Nash Equilibrium) atau solusi Pareto Optimal dari permainan kompleks ini secara efisien.
