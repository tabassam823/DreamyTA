# Bab 2: Tinjauan Pustaka dan Dasar Teori

Bab ini menguraikan landasan teori yang mendasari penelitian tesis, mengintegrasikan konsep-konsep dari Fisika Murni (Kuantum dan Statistik) dengan aplikasinya dalam Ekonomi dan Teori Permainan. Struktur bab ini disusun berdasarkan relevansi dengan mata kuliah yang telah ditempuh serta literatur terkini yang dikaji.

## 2.1 Formalisme Mekanika Kuantum untuk Pemodelan Informasi
Sub-bab ini membangun fondasi matematis yang diperlukan untuk Teori Permainan Kuantum dan Komputasi Kuantum, memperdalam konsep yang telah dipelajari dalam mata kuliah **Fisika Kuantum** dan **Fisika Matematika**.

### 2.1.1 Ruang Hilbert dan Operator
Menjelaskan representasi state kuantum dalam ruang Hilbert, notasi Dirac (bra-ket), dan operator Hermisian. Ini adalah perluasan langsung dari materi aljabar linear di **Fisika Matematika II/III**.
*   *Relevansi Paper:* ==Marinatto-Weber== approach dalam *==Quantum Barro-Gordon Game==* membutuhkan pemahaman mendalam tentang operator densitas dan trace parsial.
*   *Konsep Kunci:* ==Superposisi, Qubit vs Qutrit== (seperti dibahas dalam paper *Quantum inspired qubit qutrit neural networks*), dan Matriks Densitas.

### 2.1.2 Keterikatan (Entanglement) dan Quantum Discord
Membahas korelasi non-klasik yang menjadi sumber keunggulan kuantum (quantum advantage).
*   *Relevansi Paper:* Paper *Linking quantum discord with ==Bayesian game theory==* menekankan bahwa ==*Quantum Discord*== lebih relevan daripada entanglement semata dalam sistem yang noisy atau terpisah.
*   *Hubungan Mata Kuliah:* Pendalaman dari konsep spin dan sistem banyak partikel di **Fisika Kuantum** dan **Fisika Zat Padat**.

### 2.1.3 Interferensi Kuantum dalam Probabilitas
Menjelaskan bagaimana amplitudo probabilitas kompleks menghasilkan interferensi (konstruktif/destruktif) yang menyimpang dari probabilitas klasik.
*   *Relevansi Paper:* Dasar utama dari paper *Quantum-like influence diagrams*, yang memodelkan "irasionalitas" pengambilan keputusan manusia menggunakan efek interferensi ini.

## 2.2 Fisika Statistik dan Sistem Kompleks
Sub-bab ini menghubungkan termodinamika dan mekanika statistik dengan fenomena ekonomi, memanfaatkan dasar dari mata kuliah **Fisika Statistik** dan **Termodinamika**.

### 2.2.1 Model Ising dan Distribusi Boltzmann
Model interaksi spin klasik yang dipetakan ke dalam masalah optimasi dan pengambilan keputusan.
*   *Relevansi Paper:* Paper *Quantum-enhanced Markov chain Monte Carlo* dan *Important Quantum Gates for... TSP* menggunakan ==Hamiltonan Ising== untuk memodelkan fungsi biaya (cost function) dalam masalah optimasi.
*   *Hubungan Mata Kuliah:* Aplikasi langsung dari ensemble kanonik dan fungsi partisi yang dipelajari di **Fisika Statistik**.

### 2.2.2 Proses Stokastik dan Gerak Brown
Dasar bagi pemodelan fluktuasi harga aset yang bersifat acak.
*   *Relevansi Paper:* Paper *Qualitative financial modelling in fractal dimensions* dan *Deep Learning-Based BSDE* menggunakan variasi dari ==Gerak Brown Geometris== dan proses difusi.
*   *Hubungan Mata Kuliah:* Terkait erat dengan **Fisika Modern** (fenomena difusi) dan **Matematika Finansial**.

### 2.2.3 Fraktal dan Analisis Runtun Waktu (Time Series)
Menggunakan ==konsep dimensi fraktal== untuk menganalisis kekasaran (rugosity) pasar yang tidak dapat dijelaskan oleh model Gaussian biasa.
*   *Relevansi Paper:* *Qualitative financial modelling in fractal dimensions* membahas Hurst Exponent dan Fractal Market Hypothesis sebagai alternatif Efficient Market Hypothesis.

## 2.3 Metode Komputasi dan Numerik
Menjabarkan teknik simulasi yang digunakan untuk menyelesaikan persamaan kompleks yang tidak memiliki solusi analitik, sesuai dengan kompetensi dari **Fisika Komputasi** dan **Pengantar Fisika Komputasi**.

### 2.3.1 Metode Monte Carlo dan Rantai Markov (MCMC)
Teknik sampling untuk menyelesaikan integral dimensi tinggi atau masalah optimasi.
*   *Relevansi Paper:* Digunakan secara luas dalam ==*Libor Market Model*== untuk pricing derivatif dan dipercepat menggunakan algoritma kuantum dalam paper *Quantum-enhanced Markov chain Monte Carlo*.

### 2.3.2 Persamaan Diferensial Stokastik Mundur (BSDE)
Metode matematika lanjut untuk pricing opsi yang melibatkan penyelesaian persamaan diferensial parsial non-linear.
*   *Relevansi Paper:* Fokus utama paper *Deep Learning-Based ==BSDE== Solver*, yang menggabungkan *Deep Learning* (Neural Networks) untuk mengatasi =="curse of dimensionality"==.
*   *Hubungan Mata Kuliah:* Aplikasi lanjut dari **Fisika Matematika** (Persamaan Diferensial Parsial).

### 2.3.3 Algoritma Optimasi Kuantum (QAOA)
Algoritma hibrida klasik-kuantum untuk masalah optimasi kombinatorial.
*   *Relevansi Paper:* Dijelaskan dalam *Important Quantum Gates for Quantum Algorithms of TSP*.

## 2.4 Ekonofisika dan Teori Permainan
Sintesis dari konsep fisika yang diterapkan pada masalah ekonomi, sesuai dengan minat spesifik tesis dan mata kuliah **Matematika Finansial**.

### 2.4.1 ==Model Black-Scholes== dan Derivatif Finansial
Teori standar penentuan harga opsi dan keterbatasannya.
*   *Relevansi Paper:* Menjadi basis pembanding untuk model-model baru seperti *Fractional Black-Scholes* dan *Libor Market Model*.

### 2.4.2 Teori Permainan Klasik vs Kuantum
Membandingkan Nash Equilibrium klasik dengan hasil yang diperoleh melalui strategi kuantum (misalnya, penggunaan superposisi strategi).
*   *Relevansi Paper:* Paper *Quantum Barro-Gordon Game* menunjukkan bagaimana strategi kuantum dapat menyelesaikan masalah "Time Inconsistency" dan inflasi yang tidak dapat diselesaikan secara klasik. Paper *Linking quantum discord with ==Bayesian game theory==* menghubungkan teori permainan dengan korelasi kuantum.

### 2.4.3 Arbitrase Statistik dan Kointegrasi
Strategi trading yang memanfaatkan sifat ==*mean-reverting*== dari spread harga saham.
*   *Relevansi Paper:* *Statistical Arbitrage for Multiple Co-integrated Stocks* menggunakan proses ==Ornstein-Uhlenbeck== (mirip pegas teredam di **Mekanika**) untuk memodelkan spread.
