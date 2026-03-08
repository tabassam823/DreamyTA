# Entropi Von Neumann: Fondasi Informasi Kuantum

Dokumen ini menjelaskan konsep **Entropi Von Neumann**, derivasi matematisnya, sejarah, serta aplikasinya dalam mekanika statistik dan teori informasi kuantum.

## 1. Sejarah dan Motivasi

Entropi Von Neumann diperkenalkan oleh **John von Neumann** pada tahun 1927. Motivasi utamanya adalah memperluas konsep entropi Gibbs/Boltzmann dari mekanika statistik klasik ke dalam kerangka mekanika kuantum yang baru lahir saat itu.

Von Neumann menyadari bahwa keadaan kuantum tidak selalu berupa "state murni" ($\psi$), melainkan sering kali merupakan "campuran statistik" (*mixed state*) dari berbagai keadaan akibat interaksi dengan lingkungan. Untuk mendeskripsikan ketidakpastian dalam sistem kuantum ini, ia merumuskan operator densitas ($ho$) dan entropi yang bersesuaian dengannya.

## 2. Definisi Matematis

Dalam mekanika kuantum, keadaan sistem dideskripsikan oleh **matriks densitas** $ho$, yang harus memenuhi syarat $\text{Tr}(ho) = 1$ dan $ho \ge 0$ (positif semidefinit).

**Entropi Von Neumann ($S$)** didefinisikan sebagai:

$$S(\rho) = -	\text{Tr}(\rho \ln \rho)$$

Jika kita melakukan dekomposisi spektral pada $ho$ sedemikian sehingga $ho = \sum_i \lambda_i |i \rangle\langle i|$, di mana $\lambda_i$ adalah nilai eigen (eigenvalues) dari $ho$, maka rumus di atas dapat ditulis sebagai:

$$S(
ho) = -\sum_i \lambda_i \ln \lambda_i$$

### Catatan Matematis:
1.  **Satuan:** Jika menggunakan $\ln$ (logaritma natural), satuannya adalah *nats*. Jika menggunakan $\log_2$, satuannya adalah *bits*.
2.  **State Murni:** Untuk state murni $ho = |\psi \rangle\langle \psi|$, nilai eigennya adalah $\{1, 0, 0, ...\}$. Maka $S(ho) = -(1 \ln 1 + 0) = 0$. Artinya, tidak ada ketidakpastian informasi dalam state murni.
3.  **Maximally Mixed State:** Untuk sistem dengan dimensi $d$, entropi maksimum adalah $S_{max} = \ln d$, yang terjadi ketika $ho = \frac{1}{d} \mathbb{I}$.

## 3. Sifat-Sifat Penting

Sebagai mahasiswa fisika dan matematika, Anda harus memperhatikan sifat-Sifat berikut:

*   **Invariansi Uniter:** $S(Uho U^\dagger) = S(ho)$. Entropi tidak berubah di bawah evolusi waktu uniter.
*   **Kecekungan (Concavity):** $S(\sum_i p_i ho_i) \ge \sum_i p_i S(ho_i)$. Mencampur state meningkatkan entropi (ketidakpastian).
*   **Subadditivitas:** Untuk sistem komposit $AB$, $S(ho_{AB}) \le S(ho_A) + S(ho_B)$. Kesamaan berlaku jika dan hanya jika $ho_{AB} = ho_A \otimes ho_B$ (tidak ada korelasi).
*   **Araki-Lieb Inequality:** $|S(ho_A) - S(ho_B)| \le S(ho_{AB})$. Ini adalah konsekuensi dari *entanglement* yang tidak ada dalam fisika klasik.

## 4. Aplikasi: Quantum Mutual Information (QMI)

Salah satu aplikasi paling krusial dari Entropi Von Neumann adalah untuk mengukur korelasi total antara dua bagian sistem ($A$ dan $B$).

$$I(A:B) = S(\rho_A) + S(\rho_B) - S(\rho_{AB})$$

Dalam konteks **Model Ising**, jika kita ingin mencari parameter interaksi $J_{ij}$ antara spin $i$ dan $j$:
1.  Kita menghitung matriks densitas terreduksi $ho_{ij}$ dari *ground state* Hamiltonian.
2.  Kita hitung $S(ho_i)$, $S(ho_j)$, dan $S(ho_{yij})$.
3.  Nilai $I(i:j)$ mencerminkan seberapa kuat "jejak" interaksi $J_{ij}$ tertanam dalam struktur informasi state tersebut.

## 5. Hubungan dengan Termodinamika

Dalam mekanika statistik kuantum, untuk ansambel kanonik pada suhu $T$, matriks densitasnya adalah:
$$\rho = \frac{e^{-\beta H}}{Z}$$
di mana $\beta = 1/k_BT$ dan $Z = 	ext{Tr}(e^{-\beta H})$ adalah fungsi partisi.

Jika kita substitusikan $ho$ ini ke dalam rumus Von Neumann:
$$S = -	\text{Tr} \left( \frac{e^{-\beta H}}{Z} \ln \frac{e^{-\beta H}}{Z} \right)$$
$$S = \frac{\langle E \rangle}{k_B T} + \ln Z$$

Dari sini kita mendapatkan hubungan energi bebas Helmholtz: $F = \langle E \rangle - TS$, yang menghubungkan informasi kuantum langsung dengan hukum termodinamika klasik.

## 6. Kesimpulan

Entropi Von Neumann adalah jembatan antara **Aljabar Linear**, **Teori Peluang**, dan **Fisika Statistik**. Ia bukan sekadar angka, melainkan ukuran fundamental dari "kemurnian" sebuah state kuantum dan kunci untuk memahami bagaimana sistem kuantum menyimpan serta membagikan informasi melalui interaksi Hamiltonian.