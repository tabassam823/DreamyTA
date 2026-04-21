# Pengali Lagrange (Lagrange Multiplier) & Transformasi Suku Penalti

Dokumen ini menjelaskan bagaimana metode optimasi terkendala klasik menjadi fondasi untuk memaksakan batasan jumlah aset dalam model portofolio kuantum.

## 1. Filosofi: Optimasi di Bawah Tekanan
Optimasi tanpa batasan itu mudah (seperti bola yang menggelinding ke lembah terdalam). Namun, dalam ekonomi, kita memiliki keterbatasan (budget, jumlah aset). **Joseph-Louis Lagrange** memperkenalkan parameter bantuan $\lambda$ untuk memastikan solusi tetap berada di dalam "garis batas" yang ditentukan.

### A. Bentuk Umum Lagrangian
Misalkan kita ingin meminimalkan fungsi risiko $f(x)$ dengan kendala bahwa fungsi batasan $g(x)$ harus bernilai $K$.
$$ L(x, \lambda) = f(x) + \lambda \cdot (g(x) - K) \qquad (1) $$

> **Visualisasi (1): Jembatan Logika**
> Secara geometris, titik optimal terjadi ketika gradien fungsi objektif sejajar dengan gradien kendala:
> $$ \nabla f(x) = -\lambda \nabla g(x) $$
> Artinya, pada titik tersebut, "gaya" untuk menurunkan nilai $f$ tepat dilawan oleh "gaya" dari kendala $g$ yang menahan agar tidak keluar batas. Nilai $\lambda$ menentukan seberapa "kuat" kendala tersebut menekan fungsi objektif.

### B. Masalah Linearitas: Mengapa Persamaan (1) Gagal di Komputasi Kuantum?
Dalam kalkulus klasik, kita mencari *stationary point* dengan menurunkan terhadap $\lambda$ ($\frac{\partial L}{\partial \lambda} = 0$), yang secara otomatis memaksa $g(x) = K$. Namun, pada algoritma *unconstrained optimization* seperti VQE atau QAOA:
1. **Tidak ada derajat kebebasan $\lambda$:** Hardware kuantum hanya melakukan minimisasi terhadap variabel state $x$, bukan parameter pengali $\lambda$.
2. **Ketidakstabilan Energi:** Jika kita menggunakan suku linear $\lambda(g(x)-K)$, optimizer akan "menipu" sistem. Jika $\lambda$ positif, sistem akan membuat $g(x)$ sekecil mungkin (menuju $-\infty$) untuk menurunkan energi total. Jika $\lambda$ negatif, sistem akan membuat $g(x)$ sebesar mungkin.
3. **Kesimpulan:** Suku linear tidak memiliki "dasar" (minimum lokal) pada titik $g(x)=K$. Kita butuh bentuk fungsional yang menghukum deviasi di kedua arah (kelebihan maupun kekurangan).

---

## 2. Jembatan Logika: Dari Lagrange ke Suku Penalti (QUBO)
Dalam komputasi kuantum (VQE/Ising), variabel kita adalah biner $x \in \{0, 1\}$. Kita tidak bisa menggunakan turunan kontinu $\nabla L = 0$ secara langsung pada hardware. Oleh karena itu, kita mengubah "Gaya Lagrange" menjadi "Energi Penalti".

### A. Transformasi Sumur Potensial (L2-Norm)
Untuk memaksa sistem tetap pada $g(x) = K$ tanpa variabel $\lambda$, kita mengubah kendala menjadi **[[Sumur_Potensial_Parabolik]]**. Kita menggunakan bentuk kuadrat (L2-norm) agar setiap deviasi—baik positif maupun negatif—dikonversi menjadi kenaikan energi:
$$ E_{penalty} = A \cdot (g(x) - K)^2 \qquad (2) $$

**Jembatan Formalisme:**
Persamaan (2) adalah evolusi dari Persamaan (1) di mana kita mengganti pengali statis $\lambda$ dengan fungsi penalti dinamis yang besarnya proporsional terhadap kuadrat pelanggaran kendala. Dalam optimasi numerik, ini disebut sebagai *Soft Constraint*.

**Insight Fisik:** 
- Jika $g(x) - K = 0$, maka $E_{penalty} = 0$ (Sistem nyaman di dasar lembah).
- Jika $g(x) \neq K$, maka $(g(x) - K)^2$ selalu positif (baik kelebihan maupun kekurangan aset). Pengali $A$ (evolusi dari $\lambda$) akan memperbesar hukuman ini sehingga sistem "terpaksa" kembali ke kondisi $K$.

---

## 3. Reduksionisme: Kasus Pemilihan $K=2$ Aset
Mari kita bedah aljabar suku penalti untuk memilih tepat **2 aset** dari total **3 aset** tersedia ($x_1, x_2, x_3$).

### A. Formulasi Penalti
Batasannya adalah $x_1 + x_2 + x_3 = 2$. Maka fungsional penaltinya:
$$ P(x) = A(x_1 + x_2 + x_3 - 2)^2 \qquad (3) $$

> **Visualisasi (3): Ekspansi Aljabar**
> Kita ekspansi persamaan (3) menggunakan identitas $(a+b+c-d)^2$:
> $$ P(x) = A \left[ (x_1^2 + x_2^2 + x_3^2) + 2(x_1x_2 + x_1x_3 + x_2x_3) - 2(2)(x_1 + x_2 + x_3) + 2^2 \right] $$
> Karena $x_i \in \{0, 1\}$, maka $x_i^2 = x_i$. Substitusi ini memberikan:
> $$ P(x) = A \left[ (x_1 + x_2 + x_3) + 2(x_1x_2 + x_1x_3 + x_2x_3) - 4(x_1 + x_2 + x_3) + 4 \right] $$
> $$ P(x) = A \left[ 2(x_1x_2 + x_1x_3 + x_2x_3) - 3(x_1 + x_2 + x_3) + 4 \right] \qquad (4) $$

---

## 4. Representasi Matriks: QUBO Form
Persamaan (4) dipetakan ke dalam format matriks $x^T Q x$ untuk diproses oleh Ising Solver.

### A. Pemetaan Elemen
Bentuk umum QUBO adalah $\sum_{i<j} Q_{ij} x_i x_j + \sum_i C_i x_i + \text{const}$.

> **Visualisasi (4): Operasi Matriks**
> Berdasarkan hasil ekspansi di persamaan (4):
> - **Suku Interaksi (Kopling):** Koefisien di depan $x_i x_j$ adalah $2A$.
> - **Suku Linear (Field):** Koefisien di depan $x_i$ tunggal adalah $-3A$.
> - **Konstanta (Energy Offset):** Nilai tanpa variabel adalah $4A$.
>
> $$ P(x) = A \begin{pmatrix} x_1 & x_2 & x_3 \end{pmatrix} \begin{pmatrix} -3 & 2 & 2 \\ 0 & -3 & 2 \\ 0 & 0 & -3 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} + 4A $$

---

## 5. Verifikasi Parameter: Apakah Batasan $K=2$ Terpenuhi?
Mari kita uji energi sistem untuk berbagai konfigurasi pemilihan aset (asumsi $A=1$):

| Konfigurasi $(x_1, x_2, x_3)$ | Jumlahan ($\sum x_i$) | Energi $P(x)$ (Substitusi ke pers. 3) | Status |
| :--- | :--- | :--- | :--- |
| $(0, 0, 0)$ | 0 | $1(0-2)^2 = 4$ | Dihukum Berat |
| $(1, 0, 0)$ | 1 | $1(1-2)^2 = 1$ | Dihukum |
| **$(1, 1, 0)$** | **2** | **$1(2-2)^2 = 0$** | **Optimal (Ground State)** |
| $(1, 1, 1)$ | 3 | $1(3-2)^2 = 1$ | Dihukum |

> **Cara Membaca Tabel:** Konfigurasi yang memenuhi syarat $K=2$ memiliki energi terendah (0). Inilah sebabnya VQE akan "jatuh" ke solusi ini selama proses optimasi.

---

## 6. Kesimpulan: Peran $A$ sebagai Pengali Lagrange "Kaku"
Dalam Hamiltonian Ising, parameter $A$ bukan sekadar angka acak. Dia adalah **stiffness** (kekakuan) dari kendala kita.
1. Jika **$A$ terlalu kecil**: Potensi keuntungan dari return mungkin lebih besar dari hukuman penalti, sehingga sistem memilih jumlah aset yang salah demi mengejar return.
2. Jika **$A$ terlalu besar**: Lembah energi menjadi terlalu curam, membuat optimizer (seperti SPSA) terjebak atau gagal konvergen karena gradien yang terlalu ekstrem.

**Physical Insight:** Bayangkan batasan sebagai sebuah sumur potensial. Parameter $A$ menentukan kedalaman dan kecuraman sumur tersebut. Untuk $K=2$, kita sedang mendesain sumur yang titik terdalamnya tepat berada pada kombinasi bitstring dengan bobot Hamming $= 2$.
