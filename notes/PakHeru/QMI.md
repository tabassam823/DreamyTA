# Quantum Mutual Information (QMI) & Ekstraksi Parameter Interaksi

Dokumen ini menjelaskan bagaimana korelasi informasi dalam ruang Hilbert digunakan untuk merekonstruksi parameter fisik dalam model Ising Hamiltonian.

## 1. Konvensi Dasar: Makna Vektor State
Sebelum memahami interaksi, kita harus sepakat pada representasi matematis dari status qubit tunggal.

### A. Basis Komputasi (Reduksionisme 1-Qubit)
Status sistem diwakili oleh vektor kolom dalam ruang kompleks $\mathbb{C}^2$.
- **Status $|0\rangle$ (Ground/Spin Up):**
  $$ |0\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix} $$
- **Status $|1\rangle$ (Excited/Spin Down):**
  $$ |1\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix} $$

**Insight Fisik:** Angka "1" di baris pertama $|0\rangle$ berarti probabilitas menemukan sistem di state 0 adalah $|1|^2 = 100\%$.

---

## 2. Sistem Komposit: Ruang Hilbert 2-Qubit
Saat kita memiliki dua aset atau dua spin ($i$ dan $j$), ruang statusnya membesar melalui operasi **Tensor Product** ($\otimes$).

### A. Konstruksi Basis Rangkap Dua
Ada 4 kombinasi kemungkinan status untuk 2 qubit (dimensi $2^2 = 4$):
1. $|00\rangle = [1, 0, 0, 0]^T$
2. $|01\rangle = [0, 1, 0, 0]^T$
3. $|10\rangle = [0, 0, 1, 0]^T$
4. $|11\rangle = [0, 0, 0, 1]^T$

Setiap state umum $|\psi\rangle_{ij}$ adalah superposisi dari keempat basis ini:
$$ |\psi\rangle_{ij} = \sum_{a,b \in \{0,1\}} \alpha_{ab} |ab\rangle \qquad (1) $$

> **Visualisasi (1):** Secara linear, ini adalah penjumlahan vektor kolom:
>  $$ 
\begin{split}
 |\psi\rangle_{ij} &= \alpha_{00} |00\rangle + \alpha_{01} |01\rangle + \alpha_{10} |10\rangle + \alpha_{11} |11\rangle \\\\
 
 |\psi\rangle_{ij} &= \alpha_{00} \begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \end{pmatrix} + \alpha_{01} \begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \end{pmatrix} + \alpha_{10} \begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \end{pmatrix} + \alpha_{11} \begin{pmatrix} 0 \\ 0 \\ 0 \\ 1 \end{pmatrix} = \begin{pmatrix} \alpha_{00} \\ \alpha_{01} \\ \alpha_{10} \\ \alpha_{11} \end{pmatrix} 
 \end{split} $$
> Di mana $\alpha_{ab}$ adalah amplitudo probabilitas kompleks.

---

## 3. Matriks Densitas: Jembatan ke Informasi Statistik

### A. Keadaan Murni (*Pure State*)
Didefinisikan sebagai *outer product* dari state (1):
$$ \rho_{ij} = |\psi\rangle\langle\psi| \qquad (2) $$

> **Visualisasi (2):** Ini adalah perkalian matriks $(4 \times 1)$ dengan $(1 \times 4)$:
> $$ \rho_{ij} = \begin{pmatrix} \alpha_{00} \\ \alpha_{01} \\ \alpha_{10} \\ \alpha_{11} \end{pmatrix} \begin{pmatrix} \alpha_{00}^* & \alpha_{01}^* & \alpha_{10}^* & \alpha_{11}^* \end{pmatrix} = \begin{pmatrix} \alpha_{00}\alpha_{00}^* & \alpha_{00}\alpha_{01}^* & \alpha_{00}\alpha_{10}^* & \alpha_{00}\alpha_{11}^* \\ \alpha_{01}\alpha_{00}^* & \alpha_{01}\alpha_{01}^* & \alpha_{01}\alpha_{10}^* & \alpha_{01}\alpha_{11}^* \\ \alpha_{10}\alpha_{00}^* & \alpha_{10}\alpha_{01}^* & \alpha_{10}\alpha_{10}^* & \alpha_{10}\alpha_{11}^* \\ \alpha_{11}\alpha_{00}^* & \alpha_{11}\alpha_{01}^* & \alpha_{11}\alpha_{10}^* & \alpha_{11}\alpha_{11}^* \end{pmatrix} $$

Elemen matriks ini didefinisikan sebagai:
$$ \rho_{ab,cd} = \langle ab | \rho_{ij} | cd \rangle = \alpha_{ab} \alpha_{cd}^* \qquad (3) $$

> **Visualisasi (3):** Indeks $ab,cd$ merujuk pada baris dan kolom. 
> Contoh: elemen baris ke-1 kolom ke-2 ($\rho_{00,01}$) didapat dari $\alpha_{00}$ (baris) dikali $\alpha_{01}^*$ (kolom).

### B. Keadaan Campuran (*Mixed State*)
Jika sistem memiliki ketidakpastian klasik (noise/suhu), kita menggunakan rata-rata statistik:
$$ \rho_{ij} = \sum_k p_k |\psi_k\rangle\langle\psi_k| \qquad (4) $$

> **Visualisasi (4):** Secara matriks, ini adalah jumlahan berbobot elemen-per-elemen:
> $$ \rho_{ij} = \sum_k p_k \begin{pmatrix} \rho_{00,00}^{(k)} & \rho_{00,01}^{(k)} & \rho_{00,10}^{(k)} & \rho_{00,11}^{(k)} \\ \rho_{01,00}^{(k)} & \rho_{01,01}^{(k)} & \rho_{01,10}^{(k)} & \rho_{01,11}^{(k)} \\ \rho_{10,00}^{(k)} & \rho_{10,01}^{(k)} & \rho_{10,10}^{(k)} & \rho_{10,11}^{(k)} \\ \rho_{11,00}^{(k)} & \rho_{11,01}^{(k)} & \rho_{11,10}^{(k)} & \rho_{11,11}^{(k)} \end{pmatrix} $$
> Di mana $\sum p_k = 1$ memastikan normalisasi probabilitas tetap terjaga setelah jumlahan.

**Verifikasi Parameter:** Matriks $\rho$ wajib memenuhi:
1. **Hermitian:** $\rho = \rho^\dagger$ (Matriks simetris terhadap diagonal dan elemen konjugat kompleksnya).
2. **Trace = 1:** Total probabilitas (diagonal utama) harus 100%.
$$ \text{Tr}(\rho) = \sum_{a,b} \rho_{ab,ab} = 1 \qquad (5) $$

> **Visualisasi (5):** Jumlahan elemen diagonal pada matriks (2) atau (4):
> $$ \text{Tr}(\rho) = \rho_{00,00} + \rho_{01,01} + \rho_{10,10} + \rho_{11,11} = 1 $$

---

## 4. Jembatan Logika: Partial Trace & Informasi Lokal
Untuk mendapatkan status lokal qubit $i$, kita harus melakukan *trace-out* terhadap qubit $j$.

**Filosofi:** Kita menjumlahkan semua kemungkinan status qubit $j$ untuk melihat perilaku rata-rata qubit $i$.
$$ \rho_i = \text{Tr}_j(\rho_{ij}) = \sum_{b \in \{0,1\}} \langle b |_j \rho_{ij} | b \rangle_j \qquad (6) $$

> **Visualisasi (6):** Partisi matriks $\rho_{ij}$ menjadi blok $2 \times 2$:
> $$ \rho_{ij} = \begin{pmatrix} \mathbf{M_{00}} & \mathbf{M_{01}} \\ \mathbf{M_{10}} & \mathbf{M_{11}} \end{pmatrix} = \begin{pmatrix} \begin{pmatrix} \rho_{00,00} & \rho_{00,01} \\ \rho_{01,00} & \rho_{01,01} \end{pmatrix} & \begin{pmatrix} \rho_{00,10} & \rho_{00,11} \\ \rho_{01,10} & \rho_{01,11} \end{pmatrix} \\ \begin{pmatrix} \rho_{10,00} & \rho_{10,01} \\ \rho_{11,00} & \rho_{11,01} \end{pmatrix} & \begin{pmatrix} \rho_{10,10} & \rho_{10,11} \\ \rho_{11,10} & \rho_{11,11} \end{pmatrix} \end{pmatrix} $$
> Operasi $\text{Tr}_j$ (trace-out qubit kedua) setara dengan mengambil Trace dari setiap blok $\mathbf{M_{ac}}$ secara independen.

**Reduksionisme (Langkah Aljabar):**

### A. Matriks Densitas Terreduksi $\rho_i$
$$ (\rho_i)_{ac} = \text{Tr}(\mathbf{M_{ac}}) = \sum_{b \in \{0,1\}} \rho_{ab,cb} \qquad (7) $$

> **Visualisasi (7):** Menggabungkan hasil trace blok menjadi matriks $2 \times 2$:
> $$ \rho_i = \begin{pmatrix} \text{Tr}(\mathbf{M_{00}}) & \text{Tr}(\mathbf{M_{01}}) \\ \text{Tr}(\mathbf{M_{10}}) & \text{Tr}(\mathbf{M_{11}}) \end{pmatrix} = \begin{pmatrix} (\rho_{00,00} + \rho_{01,01}) & (\rho_{00,10} + \rho_{01,11}) \\ (\rho_{10,00} + \rho_{11,01}) & (\rho_{10,10} + \rho_{11,11}) \end{pmatrix} $$

### B. Matriks Densitas Terreduksi $\rho_j$
Trace-out qubit pertama ($\text{Tr}_i$) setara dengan menjumlahkan blok diagonal secara matriks:
$$ \rho_j = \mathbf{M_{00}} + \mathbf{M_{11}} = \sum_{a \in \{0,1\}} \rho_{ab,ad} \qquad (8) $$

> **Visualisasi (8):** Penjumlahan langsung blok diagonal utama:
> $$ \rho_j = \begin{pmatrix} \rho_{00,00} & \rho_{00,01} \\ \rho_{01,00} & \rho_{01,01} \end{pmatrix} + \begin{pmatrix} \rho_{10,10} & \rho_{10,11} \\ \rho_{11,10} & \rho_{11,11} \end{pmatrix} = \begin{pmatrix} (\rho_{00,00} + \rho_{10,10}) & (\rho_{00,01} + \rho_{10,11}) \\ (\rho_{01,00} + \rho_{11,10}) & (\rho_{01,01} + \rho_{11,11}) \end{pmatrix} $$

---

## 5. Menghitung Quantum Mutual Information (QMI)
Gunakan **Entropi Von Neumann ($S$)** pada hasil persamaan (6), (7), dan (8):
$$ S(\rho) = -\text{Tr}(\rho \ln \rho) \qquad (9) $$

> **Visualisasi (9):** Secara praktis, kita mendiagonalkan matriks $\rho$ untuk mendapatkan nilai eigen $\lambda_k$. Lalu:
> $$ S(\rho) = -(\lambda_1 \ln \lambda_1 + \lambda_2 \ln \lambda_2 + \dots) $$
> Jika sistem murni, satu nilai eigen bernilai 1 dan sisanya 0, sehingga $S=0$.

**Definisi QMI:**
$$ I(i:j) = S(\rho_i) + S(\rho_j) - S(\rho_{ij}) \qquad (10) $$

> **Visualisasi (10):** Ini adalah operasi skalar sederhana (angka dikurangi angka).
> Contoh: Jika $S(\rho_i) = 0.69$, $S(\rho_j) = 0.69$, dan $S(\rho_{ij}) = 0$ (Pure State), maka $I(i:j) = 1.38$ (Korelasi maksimal/Bell state).

---

## 6. Mengapa QMI Menjadi Landasan Parameter $J_{ij}$?
Dalam *Inverse Ising Problem*, kita ingin mencari $J_{ij}$ yang paling cocok dengan data.

1. **Korelasi & Energi:** Berdasarkan statistik Boltzmann, korelasi antar aset dipicu oleh energi interaksi $J_{ij}$. QMI (10) mengukur **total korelasi** tersebut.
2. **Hubungan Analitik:** Pada suhu tinggi, $I(i:j) \approx \frac{1}{2}(J_{ij}/k_BT)^2$. Ini membuktikan bahwa $I(i:j)$ adalah proksi langsung dari kekuatan kopling fisik.
3. **Physical Insight:** $J_{ij}$ besar berarti qubit $i$ dan $j$ "berbagi" banyak informasi. QMI menghitung volume informasi yang dibagikan ini, sehingga memberikan nilai $J_{ij}$ yang lebih akurat daripada korelasi statistik klasik.
