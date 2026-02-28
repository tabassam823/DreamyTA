# Pengali Lagrange (Lagrange Multiplier)

## 1. Sejarah Singkat
Metode ini dinamai dari **Joseph-Louis Lagrange**, seorang matematikawan Italia-Prancis yang memperkenalkannya dalam karyanya yang monumental, *Mécanique Analytique* (1788). Lagrange mencari cara untuk menyelesaikan masalah optimasi yang dibatasi oleh kendala tertentu (*constrained optimization*). Metode ini kemudian menjadi landasan bagi mekanika analitik (Lagrangian Mechanics) dan digunakan secara luas di berbagai bidang mulai dari ekonomi, teknik, hingga fisika kuantum.

## 2. Detail Matematis Penurunan

### A. Optimasi Multivariabel (Kasus Sederhana)
Misalkan kita ingin mencari nilai ekstrem (maksimum atau minimum) dari sebuah fungsi objektif $f(x, y)$ yang tunduk pada sebuah kendala $g(x, y) = c$.

Secara geometris, titik ekstrem terjadi ketika kurva level dari $f$ bersinggungan dengan kurva kendala $g = c$. Pada titik singgung ini, vektor gradien dari kedua fungsi tersebut haruslah sejajar:
$$
\nabla f = \lambda \nabla g$$
Di mana $\lambda$ adalah konstanta yang disebut **Pengali Lagrange**.

Untuk menyelesaikannya, kita definisikan fungsi baru yang disebut **Lagrangian ($L$)**:
$$L(x, y, \lambda) = f(x, y) - \lambda (g(x, y) - c)$$

Titik stasioner dicari dengan menetapkan seluruh turunan parsial ke nol:
1. $\frac{\partial L}{\partial x} = 0 \implies \frac{\partial f}{\partial x} = \lambda \frac{\partial g}{\partial x}$
2. $\frac{\partial L}{\partial y} = 0 \implies \frac{\partial f}{\partial y} = \lambda \frac{\partial g}{\partial y}$
3. $\frac{\partial L}{\partial \lambda} = 0 \implies g(x, y) = c$ (Mengembalikan kendala asal)

### B. Ekstensi ke Ruang Fungsional (Kalkulus Variasi)
Dalam mekanika kuantum, variabel kita bukan lagi titik $(x, y)$, melainkan sebuah fungsi $\psi$. Kita ingin mencari fungsi yang meminimalkan fungsional energi $E[\psi]$ dengan kendala normalisasi.

$$L[\psi, \lambda] = \langle \psi | \hat{H} | \psi 
\rangle - \lambda (\langle \psi | \psi 
\rangle - 1)$$

Variasi terhadap $\langle \psi |$ memberikan:
$$\delta L = \langle \delta \psi | \hat{H} | \psi 
\rangle - \lambda \langle \delta \psi | \psi 
\rangle = 0$$
$$\langle \delta \psi | (\hat{H} | \psi 
\rangle - \lambda | \psi 
\rangle) = 0$$

Karena $\delta \psi$ adalah sembarang, maka bagian dalam kurung harus nol:
$$\hat{H}|\psi
\rangle = \lambda|\psi
\rangle$$
Persamaan ini menunjukkan bahwa **Pengali Lagrange ($\lambda$) dalam mekanika kuantum adalah Nilai Eigen Energi ($E$)**.

## 3. Aplikasi pada Prinsip Variasional
Sebagaimana dijelaskan pada `notes/Variational_Principle.md`, pengali Lagrange adalah alat yang mengubah masalah optimasi terkendala menjadi masalah optimasi tak terkendala.

1. **Normalisasi:** Memastikan bahwa probabilitas total tetap 1 saat kita memvariasikan fungsi gelombang untuk mencari ground state.
2. **Interpretasi Fisik:** $\lambda$ bukan sekadar parameter bantuan, melainkan representasi energi sistem pada state tersebut.

## 4. Hubungan dengan Penalty Constraint (QUBO/VQE)
Dalam riset Anda mengenai optimasi portofolio (@Latex/PakHeru_Presentasi4/Rencana_Penjelasan_VQE.md), Anda menemui suku penalti $P(\sum x_i - B)^2$.

Ada hubungan erat antara Pengali Lagrange dan Suku Penalti:
- **Pengali Lagrange ($\lambda$):** Memberikan solusi eksak untuk kendala *hard constraint* dalam ranah kontinu.
- **Suku Penalti ($P$):** Sering digunakan dalam komputasi biner (QUBO) untuk "memaksa" sistem kuantum agar tetap berada dalam ruang solusi yang valid. Jika $P 	o \infty$, maka solusi QUBO akan mendekati solusi yang diberikan oleh pengali Lagrange formal.

Suku penalti biner sebenarnya adalah pendekatan dari metode pengali Lagrange yang diaplikasikan pada ruang biner diskrit agar dapat dieksekusi oleh mesin VQE atau Ising Solver.
