# Ising Hamiltonian: Sejarah, Konsep, dan Aplikasi

Dokumen ini memberikan penjelasan mendalam tentang Model Ising, fungsi Hamiltonian-nya, serta bagaimana parameter bias ($h_i$) dan interaksi ($J_{ij}$) membentuk dinamika sistem.

## 1. Sejarah Model Ising

Model Ising dinamai dari fisikawan **Ernst Ising**, yang mempublikasikan solusinya untuk model satu dimensi (1D) pada tahun 1925 dalam tesis doktoralnya. Namun, konsep aslinya diusulkan oleh pembimbingnya, **Wilhelm Lenz**, pada tahun 1920 sebagai cara untuk memahami feromagnetisme (sifat magnet permanen) dalam material.

*   **1925 (Ising):** Membuktikan bahwa dalam 1D, tidak terjadi transisi fase (perubahan dari tidak magnetik menjadi magnetik) pada suhu di atas nol. Hal ini sempat membuatnya berpikir model ini tidak berguna untuk menjelaskan feromagnetisme.
*   **1944 (Lars Onsager):** Memberikan solusi matematis yang sangat kompleks untuk model 2D, yang membuktikan adanya transisi fase. Penemuan ini merupakan tonggak sejarah dalam fisika statistik.
*   **Era Modern:** Model Ising kini melampaui fisika dan digunakan dalam ilmu saraf, biologi, sosial, hingga optimasi komputer (Quantum Annealing).

## 2. Konsep Dasar Hamiltonian

Dalam fisika, **Hamiltonian ($H$)** adalah operator atau fungsi yang menyatakan **energi total** dari suatu sistem. Dalam Model Ising, kita bekerja dengan variabel diskrit yang disebut **spin** ($s_i$), yang hanya bisa bernilai $+1$ (atas) atau $-1$ (bawah).

Bentuk umum Ising Hamiltonian adalah:

$$H(\mathbf{s}) = - \sum_{\langle i,j 
\rangle} J_{ij} s_i s_j - \sum_{i} h_i s_i$$

### Komponen Parameter:

#### A. Parameter Interaksi ($J_{ij}$)
Ini adalah kekuatan kopling antara dua spin pada lokasi $i$ dan $j$.
*   **Feromagnetik ($J_{ij} > 0$):** Sistem lebih menyukai spin yang searah (keduanya $+1$ atau keduanya $-1$) karena ini menurunkan energi total.
*   **Anti-feromagnetik ($J_{ij} < 0$):** Sistem lebih menyukai spin yang berlawanan arah (satu $+1$, satu $-1$) untuk mencapai energi rendah.
*   **Frustrasi:** Terjadi jika konfigurasi interaksi membuat sistem tidak bisa memuaskan semua pasangan $J_{ij}$ sekaligus.

#### B. Parameter Bias / Lapangan Eksternal ($h_i$)
Ini merepresentasikan pengaruh eksternal pada masing-masing spin secara individu.
*   Jika $h_i > 0$, spin $s_i$ cenderung menjadi $+1$ untuk meminimalkan energi.
*   Jika $h_i < 0$, spin $s_i$ cenderung menjadi $-1$.
*   Dalam konteks optimasi, $h_i$ sering disebut sebagai **bias** atau **local field**.

## 3. Cara Kerja dan Mekanika Statistik

Tujuan dari sistem ini biasanya adalah menemukan konfigurasi $\mathbf{s} = \{s_1, s_2, ..., s_n\}$ yang menghasilkan **Ground State** (energi terendah).

1.  **Energi vs Probabilitas:** Menurut distribusi Boltzmann, konfigurasi dengan energi rendah ($H$ kecil) memiliki probabilitas kemunculan yang lebih tinggi pada suhu rendah.
2.  **Transisi Fase:** Pada suhu tinggi, kekacauan termal mendominasi. Namun di bawah suhu kritis ($T_c$), interaksi $J_{ij}$ cukup kuat untuk memaksa spin-spin tersebut berbaris secara kolektif, menciptakan magnetisasi makroskopis.

## 4. Penggunaan dan Aplikasi Detail

### A. Optimasi Kombinatorial (QUBO)
Banyak masalah sulit dalam matematika (seperti *[[Traveling Salesman Problem]]* atau *Graph Partitioning*) dapat dipetakan ke dalam Ising Hamiltonian. Model ini dikenal sebagai **QUBO** (*Quadratic Unconstrained Binary Optimization*) jika variabelnya diubah dari $s \in \{1, -1\}$ menjadi $x \in \{0, 1\}$.
*   Mencari solusi terbaik = Mencari konfigurasi spin dengan energi terendah.

### B. Quantum Annealing & Komputasi Kuantum
Komputer kuantum seperti **D-Wave** menggunakan prinsip Ising Hamiltonian. Mereka menyiapkan sistem dalam keadaan kuantum, lalu secara perlahan mengubah Hamiltonian hingga mencapai Ground State dari masalah yang ingin dipecahkan.
*   $J_{ij}$ diprogram sebagai koneksi antar qubit.
*   $h_i$ diprogram sebagai bias pada masing-masing qubit.

### C. Ilmu Saraf (Neural Networks)
Model **Hopfield Network** adalah bentuk langsung dari Model Ising. Memori disimpan dalam pola interaksi $J_{ij}$. Ketika diberikan input yang tidak lengkap, jaringan akan "meluncur" ke lembah energi terendah yang merepresentasikan memori yang tersimpan.

### D. Sosiologi dan Ekonomi
Digunakan untuk memodelkan dinamika opini di mana $J_{ij}$ mewakili pengaruh antar individu dan $h_i$ mewakili opini pribadi atau pengaruh media luar.

## 5. Ringkasan
Model Ising adalah jembatan antara dunia fisik dan dunia komputasi. Melalui parameter **bias ($h_i$)** dan **interaksi ($J_{ij}$)**, kita dapat merumuskan sistem kompleks yang mampu belajar, mengingat, dan memecahkan masalah optimasi yang sangat berat melalui minimalisasi energi Hamiltonian.
