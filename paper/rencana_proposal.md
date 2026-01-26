# Rencana Proposal Skripsi
**Judul Tentatif:** Optimasi Portofolio Dua Aset Menggunakan *Quantum Game Theory* Skema Eisert-Wilkens-Lewenstein (EWL) Berbasis Algoritma VQE

---

# BAB 1: PENDAHULUAN

## 1.1 Latar Belakang
*   **Konteks Finansial:** Jelaskan pentingnya diversifikasi aset (Modern Portfolio Theory/Markowitz). Masalah timbul ketika pasar mengalami kondisi ekstrem (krisis), di mana aset-aset cenderung berkorelasi tinggi (jatuh bersamaan), mirip dengan fenomena "Dilema" dalam Game Theory.
*   **Keterbatasan Klasik:** Metode optimasi klasik sering terjebak di *local optima* atau gagal menangkap korelasi kompleks antar aset. Keseimbangan Nash klasik dalam *Prisoner's Dilemma* seringkali suboptimal.
*   **Solusi Kuantum:** Pengenalan *Quantum Computing* dan *Quantum Game Theory*. Bagaimana fenomena fisika seperti *Superposition* dan *Entanglement* dapat memberikan strategi baru yang tidak ada di dunia klasik.
*   **Fokus Penelitian:** Menggunakan skema EWL (Eisert-Wilkens-Lewenstein) untuk memodelkan interaksi dua aset, dan menyelesaikannya menggunakan algoritma hibrid klasik-kuantum VQE (*Variational Quantum Eigensolver*) untuk mencari alokasi optimal.

## 1.2 Rumusan Masalah
1.  Bagaimana memodelkan masalah pemilihan portofolio dua aset sebagai permainan kuantum menggunakan skema EWL?
2.  Bagaimana kinerja algoritma VQE dengan *Hardware Efficient Ansatz* dalam menemukan keseimbangan optimal (Nash Equilibrium) pada permainan tersebut?
3.  Apakah pendekatan *Quantum Game Theory* menghasilkan portofolio dengan *Trend Ratio* atau *Sharpe Ratio* yang lebih baik dibandingkan pendekatan *Game Theory* klasik?

## 1.3 Batasan Masalah
1.  **Objek:** Dibatasi pada portofolio yang terdiri dari 2 aset saham (studi kasus: saham berkapitalisasi besar di G7 atau LQ45).
2.  **Model Permainan:** Menggunakan skema kuantisasi EWL (*Eisert-Wilkens-Lewenstein*).
3.  **Algoritma:** Menggunakan VQE (*Variational Quantum Eigensolver*) dengan *optimizer* klasik COBYLA/SPSA.
4.  **Sirkuit:** Fokus pada *Hardware Efficient Ansatz* (RyRz) untuk 2 Qubit.
5.  **Simulasi:** Simulasi dilakukan menggunakan *framework* Qiskit atau Pennylane (belum pada perangkat keras kuantum riil/QPU).

## 1.4 Tujuan Penelitian
1.  Mengimplementasikan skema EWL pada sirkuit kuantum VQE untuk kasus optimasi portofolio.
2.  Membuktikan bahwa *entanglement* dapat memberikan solusi *Payoff* (keuntungan portofolio) yang lebih tinggi dibandingkan strategi klasik.
3.  Membandingkan metrik risiko dan pengembalian antara portofolio klasik dan kuantum.

## 1.5 Manfaat Penelitian
*   **Teoretis:** Memberikan bukti empiris penerapan *Quantum Game Theory* pada domain keuangan, khususnya *Asset Allocation* (bukan sekadar *Resource Allocation*).
*   **Praktis:** Menawarkan alternatif algoritma bagi manajer investasi untuk menghadapi kondisi pasar yang memiliki korelasi tinggi.

---

# BAB 2: TINJAUAN PUSTAKA

## 2.1 Teori Portofolio & Manajemen Risiko
*(Referensi: Combination.md Bab 1)*
*   **Modern Portfolio Theory (Markowitz):** Konsep *Efficient Frontier* dan *trade-off* Risk-Return.
> **Pelajari ini:**
> *   Apa itu *Efficient Frontier* dan mengapa investor rasional selalu memilih portofolio di garis ini?
> *   Bagaimana varians ($\sigma^2$) digunakan sebagai proksi risiko?
> *   **Referensi:** [[Combination.md > Modern Portofolio Theory (Markowitz Model)]]

*   **Indikator Kinerja:** Penjelasan tentang *Sharpe Ratio* dan **Trend Ratio** (sebagai metrik yang lebih sensitif terhadap tren *uptrend* stabil).
> **Pelajari ini:**
> *   Kelemahan *Sharpe Ratio*: Mengapa ia "menghukum" volatilitas positif (kenaikan harga mendadak)?
> *   Kelebihan *Trend Ratio*: Bagaimana ia membedakan antara volatilitas "buruk" (turun) dan fluktuasi di sekitar tren naik?
> *   **Referensi:** [[Combination.md > Quantum Computing X Finance > Trend Ratio]]

*   **Risiko:** Definisi *Variance* dan *Value at Risk (VaR)*.
> **Pelajari ini:**
> *   Perbedaan VaR (kerugian maksimal pada tingkat kepercayaan tertentu) dan CVaR (rata-rata kerugian *melebihi* VaR).
> *   Mengapa CVaR lebih disukai dalam optimasi (sifat koheren)?
> *   **Referensi:** [[Combination.md > Value at Risk (VaR) & Conditional Value at Risk (CVaR)]]

## 2.2 Quantum Game Theory
*(Referensi: Combination.md Bab 2)*
*   **Game Theory Klasik:** Konsep dasar *Payoff Matrix*, *Zero-sum vs Non-zero-sum*, dan *Nash Equilibrium*.
> **Pelajari ini:**
> *   Cara membaca matriks Payoff 2x2.
> *   Apa itu *Nash Equilibrium*? (Kondisi di mana tidak ada pemain yang untung jika mengubah strategi sendirian).
> *   **Referensi:** [[Combination.md > Klasik to Quantum > Prisoner's Dilemma]]

*   **Prisoner's Dilemma:** Analogi kondisi pasar "Bearish" di mana kedua aset jatuh (Defect-Defect) sebagai dilema yang harus dipecahkan.
> **Pelajari ini:**
> *   Struktur matriks *Prisoner's Dilemma*: Kenapa (Defect, Defect) adalah Nash Equilibrium meskipun (Cooperate, Cooperate) lebih menguntungkan bersama?
> *   Bagaimana analogi ini berlaku untuk dua saham yang jatuh bersamaan saat krisis?
> *   **Referensi:** [[Combination.md > Klasik to Quantum > Prisoner's Dilemma]]

*   **Skema EWL:**
    *   Penjelasan matematis operator *Entangling* ($\hat{J}$) dan *Disentangling* ($\hat{J}^\dagger$).
    *   Pentingnya operator $J$ untuk mengakses strategi kuantum yang superior.
    *   Perbedaan dengan skema Marinatto-Weber (mengapa EWL dipilih: manipulasi entanglement eksplisit).
> **Pelajari ini:**
> *   Konsep kunci: Bagaimana operator $\hat{J}$ membuat strategi pemain saling terikat (entangled) sebelum mereka membuat keputusan?
> *   Mengapa ini memungkinkan pemain "lolos" dari dilema klasik?
> *   **Referensi:** [[Combination.md > Eisert Wilkens Lewenstein (EWL)]] dan [[Combination.md > Modified EWL]]

## 2.3 Variational Quantum Eigensolver (VQE)
*(Referensi: Combination.md Bab 3 & Rencana Penelitian)*
*   **Prinsip Kerja VQE:** Algoritma hibrid (Quantum Loop + Classical Optimizer).
> **Pelajari ini:**
> *   Konsep *Hybrid Algorithm*: Bagian mana yang dikerjakan QPU (Quantum Processing Unit) dan bagian mana yang dikerjakan CPU?
> *   Apa itu *Variational Principle*? (Nilai ekspektasi Hamiltonian tidak akan pernah lebih rendah dari energi *Ground State* sebenarnya).
> *   **Referensi:** [[Combination.md > VQE Ansatz]]

*   **Mapping Masalah:**
    *   Transformasi *Payoff Matrix* menjadi Operator **Hamiltonian** ($H$).
    *   Rumus: $H = - \text{Total Payoff}$ (Minimasi energi = Maksimasi profit).
> **Pelajari ini:**
> *   Cara mengubah matriks angka (Payoff) menjadi operator kuantum (Pauli Z, I, dll).
> *   Kenapa tanda negatif (-) penting? (Karena VQE mencari minimum, kita ingin maksimum).
> *   **Referensi:** [[Combination.md > Komentar & Analisis > Missing Link]]

*   **Ansatz (Parameterized Quantum Circuit):**
    *   Penjelasan *Hardware Efficient Ansatz* / *RyRz Ansatz* (Rotasi satu qubit + CNOT).
    *   Alasan pemilihan: Efisiensi kedalaman sirkuit untuk 2 qubit dibandingkan *Dicke States* yang kompleks.
> **Pelajari ini:**
> *   Apa itu parameter $\theta$ dalam sirkuit? (Ini adalah "tombol putar" yang akan diatur oleh optimizer).
> *   Bentuk visual sirkuit *RyRz* (Rotasi Y -> Rotasi Z -> CNOT).
> *   **Referensi:** [[Combination.md > Komentar & Analisis > VQE Ansatz]]

*   **Optimizer Klasik:** Penggunaan **COBYLA** (*Constrained Optimization by Linear Approximation*) untuk memperbarui parameter $\theta$.
> **Pelajari ini:**
> *   Mengapa COBYLA cocok untuk kuantum? (Hemat evaluasi, tahan terhadap noise/stokastik).
> *   **Referensi:** [[Combination.md > COBYLA]]

## 2.4 Penelitian Terdahulu (State of the Art)
*(Referensi: Combination.md Bab 4)*
*   **Quantum Computing in Finance:** Studi tentang EL-GNQTS (algoritma evolusioner terinspirasi kuantum) untuk portofolio global.
> **Pelajari ini:**
> *   Bagaimana algoritma evolusioner (EL-GNQTS) menggunakan konsep "entanglement" sebagai metafora pencarian lokal? (Bedakan dengan entanglement fisik di VQE).
> *   **Referensi:** [[Combination.md > Quantum Computing X Finance > EL-GNQTS]]

*   **Quantum Game Theory for Resources:** Studi tentang QC-PRAGM (alokasi sumber daya *cloud*).
> **Pelajari ini:**
> *   Contoh aplikasi Game Theory di bidang lain (Resource Allocation) untuk melihat pola pemodelan "Cost Function".
> *   **Referensi:** [[Combination.md > Game Theory X Quantum Computing > QC-PRAGM]]

*   **Posisi Penelitian (Gap Analysis):** Kebanyakan riset menggunakan VQE untuk optimasi kombinatorial langsung (QAOA like) atau Game Theory untuk alokasi *resource*. Penelitian ini mengisi celah penggunaan **EWL VQE secara spesifik untuk alokasi bobot aset**.
> **Pelajari ini:**
> *   Identifikasi "Sweet Spot": Gabungan unik antara EWL (Game Theory), VQE (Quantum Algo), dan Portfolio (Finance).
> *   **Referensi:** [[Combination.md > Komentar & Analisis > Posisi Penelitian]]

## 2.5 Kerangka Berpikir
1.  **Input:** Data Saham Historis (Harga Penutupan).
2.  **Pra-pemrosesan:** Hitung *Expected Return* dan *Covariance Matrix* -> Buat *Payoff Matrix*.
3.  **Kuantisasi:** Mapping *Payoff Matrix* -> Hamiltonian ($H$).
4.  **Proses VQE:**
    *   Inisialisasi Sirkuit EWL (Gate $J$, Gate Strategi $U(\theta)$).
    *   Ukur Ekspektasi Nilai $\langle \psi | H | \psi \rangle$.
    *   Optimasi Parameter $\theta$ (Strategi Pemain) via COBYLA.
5.  **Output:** Bobot portofolio optimal (Strategi Kuantum).
6.  **Evaluasi:** Bandingkan *Trend Ratio* hasil Kuantum vs Klasik.
> **Pelajari ini:**
> *   Pahami alur data: Data Mentah -> Matriks Klasik -> Operator Kuantum -> Sirkuit -> Hasil Optimasi.
> *   **Referensi:** [[bab3_metodologi.md > 3.1 Alur Penelitian]]

# BAB 3: METODOLOGI PENELITIAN

## 3.1 Alur Penelitian
Penelitian ini dilakukan dengan pendekatan eksperimental simulasi komputasi. Tahapan penelitian dibagi menjadi lima fase utama:
1.  **Pengumpulan Data:** Akuisisi data harga saham historis.
2.  **Pemodelan Game Theory Klasik:** Konstruksi matriks *Payoff* berdasarkan *return* dan risiko.
3.  **Kuantisasi (Encoding):** Transformasi masalah ke dalam bentuk Operator Hamiltonian.
4.  **Implementasi VQE:** Eksekusi algoritma kuantum variasional dengan skema EWL.
5.  **Evaluasi & Analisis:** Perbandingan kinerja portofolio kuantum vs klasik.
> **Pelajari ini:**
> *   Gambaran besar "Pipeline" sistem yang akan dibangun.
> *   **Referensi:** [[bab3_metodologi.md]]

## 3.2 Pengumpulan dan Pra-pemrosesan Data
*   **Objek:** Dua aset saham ($N=2$) dengan kapitalisasi pasar besar (Blue Chip) yang memiliki korelasi historis tinggi (misalnya: sektor perbankan atau teknologi).
*   **Sumber Data:** *Yahoo Finance* (menggunakan library Python `yfinance`).
*   **Periode:** Data harian (*Adjusted Close*) selama 5-10 tahun terakhir.
*   **Preprocessing:**
    *   Menghitung *Logarithmic Returns* harian: $R_t = \ln(P_t / P_{t-1})$.
    *   Menghitung *Expected Return* ($\mu$) dan Matriks Kovarians ($\Sigma$).
> **Pelajari ini:**
> *   Cara menggunakan library `yfinance` di Python.
> *   Rumus Log Return dan mengapa dipakai (stasioneritas).
> *   Cara menghitung matriks kovarians dengan `numpy` atau `pandas`.
> *   **Referensi:** Dokumentasi `yfinance` & `pandas`.

## 3.3 Konstruksi Model Permainan (Game Modeling)

### 3.3.1 Definisi Strategi
Setiap aset dianggap sebagai "Pemain".
*   **Strategi $C$ (Cooperate):** Alokasi bobot tinggi / Beli.
*   **Strategi $D$ (Defect):** Alokasi bobot rendah / Tahan (atau Jual).

### 3.3.2 Matriks Payoff ($M$)
Matriks *payoff* 2x2 dikonstruksi untuk merepresentasikan keuntungan portofolio pada berbagai kondisi kombinasi strategi.
$$
M = \begin{pmatrix}
(CC) & (CD) \\
(DC) & (DD)
\end{pmatrix}
$$
*   Nilai entri matriks dihitung berdasarkan fungsi utilitas Markowitz ($U = \mu_p - \frac{\lambda}{2}\sigma_p^2$) atau *Trend Ratio* untuk setiap kombinasi bobot.
> **Pelajari ini:**
> *   Bagaimana mengisi 4 sel matriks ini? (Hitung profit portofolio untuk 4 skenario bobot yang berbeda: misal (50%,50%), (100%,0%), (0%,100%), (0%,0%)).
> *   **Referensi:** [[bab3_metodologi.md > 3.3.2 Matriks Payoff]]

### 3.3.3 Pemetaan ke Hamiltonian ($H$)
Agar dapat diproses oleh VQE, matriks *payoff* klasik ($M$) dipetakan menjadi operator Hermitian (Hamiltonian). Karena VQE mencari energi minimum (Ground State), sedangkan tujuan investasi adalah maksimasi profit, maka Hamiltonian didefinisikan sebagai negasi dari Payoff:
$$ H = - \sum_{i,j \in \{0,1\}} M_{ij} |ij\rangle\langle ij| $$
Dalam bentuk *Pauli Strings* (untuk 2 Qubit), ini dapat didekomposisi menjadi:
$$ H = c_0 I + c_1 Z_0 + c_2 Z_1 + c_3 Z_0 Z_1 $$
Dimana $Z$ adalah Pauli-Z operator.
> **Pelajari ini:**
> *   Teknik *Ising Formulation*: Bagaimana mengubah masalah optimasi menjadi Hamiltonian fisik.
> *   Cara menghitung koefisien $c_0, c_1, c_2, c_3$ dari nilai matriks $M$.
> *   **Referensi:** [[Combination.md > Komentar & Analisis > Missing Link]]

## 3.4 Desain Sirkuit VQE (Skema EWL)

Simulasi dilakukan menggunakan kerangka kerja **Pennylane** atau **Qiskit**.

### 3.4.1 Inisialisasi State
Keadaan awal qubit dimulai dari $|00\rangle$.

### 3.4.2 Operator Entanglement ($\hat{J}$)
Sesuai skema EWL, operator ini menciptakan korelasi kuantum antar pemain sebelum strategi dipilih.
$$ \hat{J} = e^{-i \frac{\gamma}{2} \sigma_x \otimes \sigma_x} $$
Untuk $\gamma = \pi/2$, ini menciptakan *Maximal Entanglement*. Dalam sirkuit, ini diimplementasikan menggunakan kombinasi gerbang **CNOT** dan **Rotasi X ($R_x$)**.
> **Pelajari ini:**
> *   Bagaimana merangkai gate `Rxx` atau kombinasi `H + CNOT` di Qiskit/Pennylane untuk membuat sirkuit Bell State.
> *   **Referensi:** [[Combination.md > Eisert Wilkens Lewenstein (EWL)]]

### 3.4.3 Ansatz (Strategi Pemain)
Menggunakan **Hardware Efficient Ansatz** (atau *RyRz Ansatz*) untuk merepresentasikan strategi pemain yang akan dioptimasi.
*   Parameter: $\vec{\theta}$ (sudut rotasi).
*   Gerbang: Rotasi qubit tunggal ($R_y, R_z$) diikuti oleh *entangling layer* (CNOT) jika kedalaman sirkuit $>1$.
*   Bentuk Unitary: $U(\theta) = \prod_{l} U_{ent} \prod_{q} R_y(\theta_{l,q})$.
> **Pelajari ini:**
> *   Apa itu gate rotasi `Ry` dan `Rz`? (Rotasi di bola Bloch).
> *   Bagaimana `Ry(theta)` memetakan probabilitas strategi klasik ke amplitudo kuantum?
> *   **Referensi:** [[Combination.md > Komentar & Analisis > VQE Ansatz]]

### 3.4.4 Pengukuran (Cost Function)
Sirkuit diakhiri dengan operator *inverse entanglement* $\hat{J}^\dagger$. Nilai ekspektasi Hamiltonian dihitung:
$$ \mathcal{L}(\theta) = \langle \psi(\theta) | H | \psi(\theta) \rangle $$
Tujuan VQE adalah mencari $\theta^*$ yang meminimalkan $\mathcal{L}$.
> **Pelajari ini:**
> *   Apa arti $\langle H \rangle$? (Rata-rata hasil pengukuran energi).
> *   Kenapa kita perlu *inverse gate* ($\hat{J}^\dagger$) di akhir? (Untuk mengembalikan basis pengukuran ke basis komputasi standar jika perlu, atau sesuai protokol EWL).
> *   **Referensi:** [[Combination.md > Eisert Wilkens Lewenstein (EWL)]]

## 3.5 Optimasi Klasik
*   **Optimizer:** COBYLA (*Constrained Optimization by Linear Approximation*).
*   **Alasan:** Efisien untuk masalah dengan jumlah evaluasi fungsi terbatas dan tidak memerlukan perhitungan gradien (*gradient-free*), cocok untuk simulasi variasi stokastik pasar.
*   **Iterasi:** Parameter $\theta$ diperbarui berulang kali hingga nilai ekspektasi konvergen.
> **Pelajari ini:**
> *   Cara kerja *loop* VQE: Quantum (hitung energi) -> Klasik (ubah theta) -> Quantum (hitung lagi) -> ... -> Konvergen.
> *   **Referensi:** [[Combination.md > COBYLA]]

## 3.6 Evaluasi Kinerja (Metrics)
Bobot portofolio optimal yang dihasilkan oleh strategi kuantum akan dievaluasi dan dibandingkan dengan strategi klasik (*Mean-Variance* standar) menggunakan indikator:
1.  **Trend Ratio:** Mengukur kemiringan garis tren dibagi volatilitas deviasi (fokus utama penelitian).
2.  **Sharpe Ratio:** *Excess return* per unit varians.
3.  **Maximum Drawdown (MDD):** Risiko penurunan maksimum dari puncak ke lembah.
> **Pelajari ini:**
> *   Cara menghitung *Trend Ratio* dari data *time-series* harga portofolio.
> *   **Referensi:** [[Combination.md > Quantum Computing X Finance > Trend Ratio]]

$$ \begin{pmatrix} \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \end{pmatrix} \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \text{ ?}$$