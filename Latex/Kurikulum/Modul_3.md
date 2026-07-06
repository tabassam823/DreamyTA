# Modul 3: Game Theory & Nash Equilibrium (SBR)

## 1. Landasan Ekonofisika: Portofolio sebagai *Exact Potential Game*

Pendekatan *Econophysics* memandang pasar finansial sebagai sistem kompleks yang terdiri dari banyak agen yang saling berinteraksi secara strategis. Dalam konteks optimasi portofolio, setiap aset dapat dianggap sebagai agen otonom yang "memutuskan" untuk berpartisipasi atau tidak dalam keranjang investasi guna memaksimalkan utilitas kolektif. Representasi ini memungkinkan transformasi masalah optimasi terpusat menjadi *Exact Potential Game* (EPG), di mana dinamika pencarian solusi optimal setara dengan proses pencarian titik kesetimbangan *Nash Equilibrium* (NE) dalam teori permainan.

Dalam kerangka kerja EPG, interaksi antara dua aset (pemain) dapat direpresentasikan melalui matriks *payoff* yang menunjukkan kontribusi bersama terhadap fungsi potensial global. Setiap pemain berusaha meningkatkan utilitasnya, yang dalam kasus ini direpresentasikan oleh kombinasi imbal hasil individu ($V_i$) dan sinergi interaksi ($W_{ij}$). Matriks berikut mengilustrasikan struktur insentif strategis antara dua aset $i$ dan $j$ dalam skenario inklusi portofolio:

| Aset $i$ \ Aset $j$ | $x_j = 1$ (*In*) | $x_j = 0$ (*Out*) |
| :--- | :---: | :---: |
| **$x_i = 1$ (*In*)** | $V_i + V_j + W_{ij}$ | $V_i$ |
| **$x_i = 0$ (*Out*)** | $V_j$ | $0$ |

**Tabel 1.** Matriks *Payoff* Strategis Dua Aset dalam Pemilihan Portofolio.

Struktur matriks pada Tabel 1 menunjukkan bahwa keuntungan bagi aset $i$ untuk bergabung dalam portofolio sangat bergantung pada status aset $j$. Jika aset $j$ sudah terpilih ($x_j = 1$), maka insentif bagi aset $i$ untuk ikut bergabung adalah sebesar $V_i + W_{ij}$. Keberadaan suku interaksi $W_{ij}$, yang diekstraksi dari korelasi historis melalui *Inverse Ising Problem*, menjadi faktor penentu apakah aset-aset tersebut akan membentuk kelompok kooperatif atau justru saling meniadakan dalam struktur energi sistem.

## 2. Penurunan Matematis Fungsi Potensial Markowitz

Masalah pemilihan portofolio diskret didefinisikan pada semesta aset $N$ dengan keputusan investasi yang direpresentasikan oleh profil strategi biner $\mathbf{x} \in \{0, 1\}^N$. Setiap elemen $x_i = 1$ menunjukkan inklusi aset $i$ dalam portofolio, sementara $x_i = 0$ menunjukkan eksklusi. Tujuan utama optimasi adalah meminimalkan fungsi Lagrangian Markowitz $\mathcal{L}(\mathbf{x})$, yang merupakan jumlahan dari risiko varians sistemik $\mathbf{x}^T \mathbf{\Sigma} \mathbf{x}$ dan ekspektasi imbal hasil $\boldsymbol{\mu}^T \mathbf{x}$ yang dikontrol oleh pengali Lagrange $\lambda \in \mathbb{R}^+$. Persamaan dasar Lagrangian tersebut dinyatakan sebagai berikut:

$$ \min_{\mathbf{x} \in \mathbb{B}^N} \mathcal{L}(\mathbf{x}) = \sum_{i=1}^N \sum_{j=1}^N \sigma_{ij} x_i x_j - \lambda \sum_{i=1}^N \mu_i x_i \qquad (1) $$

Parameter $\lambda$ dalam persamaan (1) merepresentasikan *trade-off* antara risiko dan *return*, di mana nilai optimalnya ditentukan oleh toleransi risiko investor pada kurva *efficient frontier*. Untuk menyelaraskan model ini dengan kerangka kerja teori permainan, dilakukan penskalaan Lagrangian dengan konstanta penghindaran risiko (*risk aversion*) $-\gamma/2$. Melalui substitusi hubungan analitis $\lambda = 2/\gamma$, fungsi objektif tersebut ditransformasikan ke dalam representasi fungsi potensial global $\Phi(\mathbf{x})$ sebagai berikut:

$$
\begin{aligned}
\Phi(\mathbf{x}) &= -\frac{\gamma}{2} \mathcal{L}(\mathbf{x}) \\
&= \sum_{i=1}^N \mu_i x_i - \frac{\gamma}{2} \sum_{i=1}^N \sum_{j=1}^N \sigma_{ij} x_i x_j
\end{aligned} \qquad (2)
$$

Sifat *Exact* dari permainan ini dibuktikan melalui analisis perubahan potensial global $\Delta \Phi_i$ akibat perubahan strategi unilateral oleh satu pemain $i$. Jika kita meninjau selisih nilai potensial antara kondisi aset $i$ bergabung ($x_i=1$) dan tidak bergabung ($x_i=0$) dengan asumsi strategi aset lainnya ($\mathbf{x}_{-i}$) tetap, maka didapatkan relasi utilitas marginal sebagai berikut:

$$ \Delta \Phi_i = \Phi(1, \mathbf{x}_{-i}) - \Phi(0, \mathbf{x}_{-i}) = \left( \mu_i - \frac{\gamma}{2} \sigma_{ii} \right) - \gamma \sum_{j \neq i} \sigma_{ij} x_j \qquad (3) $$

Persamaan (3) secara eksplisit menunjukkan bahwa setiap perubahan utilitas marginal pemain $i$ tercermin tepat dalam perubahan fungsi potensial global. Hal ini memberikan jembatan fisik yang fundamental di mana maksimisasi fungsi potensial $\Phi$ ekuivalen dengan minimalisasi energi Hamiltonian Ising $H$, sesuai dengan relasi $H = -\Phi$. Dengan demikian, pencarian titik *Nash Equilibrium* dalam sistem multi-agen ini secara matematis identik dengan pencarian status *ground state* pada sistem fisik yang memiliki interaksi dua-tubuh (*two-body interaction*).

## 3. Algoritma Sequential Best Response (SBR)

### 3.1 Urgensi & Konteks Fisika
Algoritma *Sequential Best Response* (SBR) bertindak sebagai jembatan metodologis antara perilaku belajar agen ekonomi dan optimasi lokal dalam fisika statistik. Dalam domain ekonomi, SBR merepresentasikan proses desentralisasi di mana setiap agen secara bergantian memperbaiki posisinya berdasarkan informasi lokal yang tersedia. Secara fisik, proses ini identik dengan teknik *Single-Spin Flip* pada simulasi model Ising di suhu nol ($T=0$), di mana sistem bergerak menuruni lembah energi hingga mencapai titik stasioner yang stabil.

Keunggulan utama SBR dalam kerangka kerja EPG adalah kepastian konvergensi menuju *Nash Equilibrium*. Karena setiap langkah individu dijamin meningkatkan fungsi potensial global (atau menurunkan energi sistem), algoritma ini pasti akan berhenti pada konfigurasi di mana tidak ada lagi agen yang dapat meningkatkan utilitasnya secara unilateral. Fenomena ini memastikan bahwa solusi yang ditemukan melalui proses desentralisasi ini memiliki validitas teoretis yang kuat sebagai titik ekuilibrium pasar.

### 3.2 Implementasi Teknis & Pseudocode
Dalam implementasi praktis pada file `GT_Ising_SBR.ipynb`, algoritma SBR diterjemahkan ke dalam fungsi `find_nash_sbr`. Fungsi ini menggunakan mekanisme pertukaran aset (*swap*) yang sangat efisien untuk menangani batasan kardinalitas $K$ secara eksplisit. Alur algoritma tersebut dirancang untuk melakukan eksplorasi pada ruang strategi yang terbatas tanpa perlu melakukan pemindaian menyeluruh (*brute-force*), sehingga sangat skalabel untuk semesta aset yang besar.

Berikut adalah *pseudocode* dari algoritma SBR yang diimplementasikan dalam sistem *Ising-SBR*:

---
**Algoritma 1: Sequential Best Response (SBR) untuk Pencarian Nash Equilibrium**
1.  **Input:** Bias medan lokal $h$, matriks interaksi $J$, jumlah aset $N$, target jumlah aset $K$.
2.  **Inisialisasi:** 
    *   Tentukan set pilihan awal $S \leftarrow \{1, \dots, K\}$.
    *   Hitung energi awal $E \leftarrow \text{get\_energy}(S, h, J)$.
3.  **Iterasi (Maksimum *max_iters*):**
    *   $S_{out} \leftarrow \{1, \dots, N\} \setminus S$ (Aset di luar portofolio).
    *   $best\_swap \leftarrow \text{None}$, $min\_E \leftarrow E$.
    *   **Untuk setiap** $i \in S$ dan **setiap** $j \in S_{out}$:
        *   Konstruksi kandidat baru $S' \leftarrow (S \setminus \{i\}) \cup \{j\}$.
        *   Hitung energi kandidat $E' \leftarrow \text{get\_energy}(S', h, J)$.
        *   **Jika** $E' < min\_E$:
            *   $min\_E \leftarrow E'$, $best\_swap \leftarrow (i, j)$.
    *   **Jika** $best\_swap$ ditemukan:
        *   Lakukan pembaruan: $S \leftarrow (S \setminus \{i\}) \cup \{j\}$ dan $E \leftarrow min\_E$.
    *   **Lainnya:**
        *   **Berhenti** (Konvergensi tercapai).
4.  **Output:** Profil strategi optimal $\mathbf{x}$ (bitstring) dan energi minimum $E$.
---

Analisis terhadap keluaran fungsi `find_nash_sbr` memberikan wawasan kritis mengenai lanskap solusi portofolio. Meskipun SBR dijamin konvergen, sifatnya yang "serakah" (*greedy*) membuat algoritma ini rentan terjebak dalam *local minima* atau kesetimbangan *Nash* lokal pada sistem dengan korelasi aset yang kompleks. Oleh karena itu, hasil dari SBR sering kali digunakan sebagai *Warm-Start* untuk algoritma kuantum yang lebih lanjut guna mengeksplorasi ruang pencarian secara lebih global.

---
*Modul ini disusun untuk memberikan landasan teoretis sebelum memasuki pemetaan Hamiltonian Ising yang lebih kompleks.*
