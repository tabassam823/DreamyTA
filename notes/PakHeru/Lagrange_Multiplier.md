# Lagrange Multiplier dalam Markowitz QUBO

Dokumen ini menjelaskan konsep, fungsi, dan penurunan matematis dari Lagrange Multiplier ($A$) yang digunakan sebagai suku penalti dalam optimasi portofolio Markowitz berbasis QUBO.

## 1. Definisi: Mengapa $A$ disebut Bobot Penalti (Lagrange Multiplier)?

Dalam konteks **QUBO (Quadratic Unconstrained Binary Optimization)**, kata kuncinya adalah "*Unconstrained*" (Tanpa Kendala). Algoritma kuantum seperti QAOA atau mesin *annealing* hanya bisa meminimalkan fungsi energi tanpa batasan eksternal. 

Namun, dalam dunia nyata, kita memiliki batasan (seperti: "harus memilih tepat $K$ aset"). Untuk memasukkan batasan ini ke dalam fungsi yang "tanpa batasan", kita menggunakan **Metode Penalti**.

*   **$A$ sebagai Bobot Penalti**: Menentukan seberapa besar "hukuman" (peningkatan energi) yang diberikan jika solusi melanggar batasan.
*   **$A$ sebagai Lagrange Multiplier**: Secara fungsional bertindak seperti pengali $\lambda$ dalam kalkulus, yang menghubungkan fungsi objektif utama dengan fungsi kendala.

## 2. Hubungan dengan Metode Lagrange Standar

Suku penalti tersebut adalah adaptasi dari **Metode Lagrange Multiplier** untuk optimasi diskrit. Dalam optimasi kontinu standar:

$$\min f(x) \quad \text{dengan kendala} \quad g(x) = 0$$

Dirumuskan menjadi fungsi Lagrangian:
$$\mathcal{L}(x, \lambda) = f(x) + \lambda g(x)$$

Dalam QUBO, kita menggunakan variasi yang disebut **Penalty Method** (bagian dari *Augmented Lagrangian Method*). Perbedaannya, kita menguadratkan kendalanya: $A(g(x))^2$.

**Mengapa dikuadratkan?**
1.  **Selalu Positif**: Jika $g(x) \neq 0$ (baik positif atau negatif), nilai $(g(x))^2$ akan selalu positif, sehingga menambah energi (memberi penalti).
2.  **Kesesuaian QUBO**: Bentuk kuadrat memastikan hubungan antar variabel tetap dalam orde dua (kuadratik), yang merupakan syarat format QUBO.

## 3. Penurunan Rumus Penalti

Berikut adalah langkah transformasi dari kendala menjadi suku penalti:

1.  **Kendala Asli**: $\sum_{i=1}^N x_i = K$ (Jumlah aset yang dipilih harus sama dengan $K$).
2.  **Bentuk Normal Kendala**: $g(x) = \sum_{i=1}^N x_i - K = 0$.
3.  **Konstruksi Penalti Kuadratik**:
    Agar nilai minimum fungsi tepat berada di titik di mana $\sum x_i - K = 0$, kita kuadratkan selisihnya:
    $$ P(x) = A \cdot (g(x))^2 = A \left( \sum_{i=1}^N x_i - K \right)^2 $$

Jika $\sum x_i = K$, maka $(K - K)^2 = 0$ (Tanpa penalti). Jika terjadi pelanggaran, energi naik sebesar $A \times (\text{error})^2$.

## 4. Fungsi Umum Lagrange Multiplier

Fungsi utama Lagrange Multiplier ($A$) adalah sebagai **penyeimbang antara dua tujuan yang saling bertentangan**:

1.  **Optimalitas (Fungsi Objektif)**: Mencari nilai sekecil atau sebesar mungkin (misal: risiko terkecil atau keuntungan terbesar).
2.  **Validitas (Kendala)**: Memastikan solusi tersebut memenuhi syarat yang ditetapkan (misal: jumlah aset pas).

**Analogi Sederhana:**
Bayangkan Anda sedang berbelanja.
*   **Fungsi Objektif**: Membeli barang sebanyak mungkin (memuaskan keinginan).
*   **Kendala**: Uang di dompet terbatas.
*   **Lagrange Multiplier ($A$)**: Adalah "konsekuensi" jika Anda *over-budget*. Jika $A$ terlalu kecil, Anda mungkin nekat berutang (melanggar kendala). Jika $A$ sangat besar, Anda akan sangat hati-hati agar pengeluaran pas dengan dompet, meskipun keinginan belum sepenuhnya terpenuhi.

Dalam QUBO, nilai $A$ harus dipilih agar cukup besar sehingga kendala tidak dilanggar, tetapi tidak terlalu besar sehingga menutupi detail dari fungsi risiko dan return yang ingin kita optimalkan.

## 5. Strategi Menentukan Nilai $A$

Menentukan nilai $A$ yang tepat adalah salah satu tantangan utama dalam QUBO. Jika $A$ terlalu kecil, algoritma akan menghasilkan solusi yang melanggar batasan. Jika $A$ terlalu besar, "lanskap energi" menjadi terlalu curam sehingga sulit bagi algoritma untuk menemukan solusi optimal global.

Berikut adalah beberapa pendekatan untuk mendapatkan nilai $A$:

### A. Pendekatan Teoretis (Upper Bound)
Secara matematis, $A$ harus lebih besar daripada perubahan maksimum yang mungkin terjadi pada fungsi objektif utama (risiko dan return) jika satu variabel berubah.
$$ A > \max | \Delta (\text{Risiko} - \text{Return}) | $$
Tujuannya adalah memastikan bahwa keuntungan dari "curang" (melanggar batasan) tidak pernah lebih besar daripada kerugian akibat hukuman penalti.

### B. Rule of Thumb (Praktis)
Seringkali, praktisi menggunakan nilai $A$ yang setara atau sedikit lebih besar dari nilai koefisien terbesar dalam matriks kovarians atau return. 
- Jika $\Sigma_{ij}$ dan $\mu_i$ berada di rentang $[0, 1]$, nilai $A$ sering kali dimulai dari $1$ hingga $10$.

### C. Pencarian Grid (Grid Search / Hyperparameter Tuning)
Dalam pendekatan ini, $A$ diperlakukan seperti hyperparameter dalam machine learning:
1. Pilih serangkaian nilai (misal: $0.1, 1, 10, 100$).
2. Jalankan optimasi untuk setiap nilai.
3. Pilih nilai $A$ terkecil yang masih memberikan solusi valid (memenuhi $\sum x_i = K$).

### D. Penalti Dinamis (Annealing Schedule)
Beberapa algoritma memulai dengan nilai $A$ yang kecil agar sistem dapat mengeksplorasi ruang solusi secara bebas pada awal proses, kemudian secara bertahap meningkatkan $A$ untuk "memaksa" sistem masuk ke wilayah solusi yang valid di akhir proses.

### E. Normalisasi Fungsi Objektif
Agar pemilihan $A$ lebih konsisten, seringkali suku risiko dan return dinormalisasi terlebih dahulu ke rentang $[0, 1]$. Dengan demikian, nilai $A$ dapat ditentukan secara lebih intuitif (misal: $A=1.5$ pasti lebih dominan daripada fungsi objektif yang sudah dinormalisasi).
