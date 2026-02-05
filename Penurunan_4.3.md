Penurunan dari persamaan **(4.3)** ke **(4.4)** didasarkan pada operasi matematika yang disebut **Partial Trace** (Jejak Parsial). Dalam mekanika kuantum, operasi ini digunakan untuk mencari kondisi satu bagian sistem (misalnya Leader) dengan cara mengabaikan atau "merata-ratakan" informasi dari bagian sistem lainnya (Follower).

Berikut adalah langkah-langkah penurunan berurutan dari dokumen Anda:

---

### 1. Menuliskan Matriks Densitas Gabungan (4.3)

Matriks densitas sistem gabungan $\rho_{sys}$ berukuran $4 \times 4$ karena merupakan hasil produk tensor dari dua sistem 2-dimensi ($2 \times 2 = 4$). Menggunakan indeks ganda $|ij\rangle \langle mn|$, strukturnya adalah:

$$\rho_{sys} = \begin{pmatrix}

\rho_{00,00} & \rho_{00,01} & \rho_{00,10} & \rho_{00,11} \\

\rho_{01,00} & \rho_{01,01} & \rho_{01,10} & \rho_{01,11} \\

\rho_{10,00} & \rho_{10,01} & \rho_{10,10} & \rho_{10,11} \\

\rho_{11,00} & \rho_{11,01} & \rho_{11,10} & \rho_{11,11}

\end{pmatrix}$$

### 2. Definisi Operasi Partial Trace

Untuk mendapatkan matriks densitas Leader ($\rho_L$), kita melakukan _trace_ terhadap derajat kebebasan Follower ($F$):

$$\rho_L = \text{Tr}_F(\rho_{sys})$$

Secara matematis, ini berarti kita menjumlahkan elemen-elemen di mana kondisi Follower pada sisi _ket_ dan _bra_ adalah sama ($|0\rangle \langle 0|$ dan $|1\rangle \langle 1|$).

### 3. Pemetaan Indeks ke Matriks $2 \times 2$

Matriks $\rho_L$ akan berukuran $2 \times 2$. Kita harus mengisi empat slot elemennya: $(\rho_L)_{00}, (\rho_L)_{01}, (\rho_L)_{10},$ dan $(\rho_L)_{11}$.

- **Elemen $(\rho_L)_{00}$ (Baris 0, Kolom 0):** Ambil semua elemen $\rho_{sys}$ di mana Leader berada di state 0 pada baris dan kolom, lalu jumlahkan semua kemungkinan Follower.
    
    $$(\rho_L)_{00} = \rho_{00,00} + \rho_{01,01}$$
    
- **Elemen $(\rho_L)_{01}$ (Baris 0, Kolom 1):** Ambil elemen di mana Leader baris = 0 dan Leader kolom = 1.
    
    $$(\rho_L)_{01} = \rho_{00,10} + \rho_{01,11}$$
    
- **Elemen $(\rho_L)_{10}$ (Baris 1, Kolom 0):** Ambil elemen di mana Leader baris = 1 dan Leader kolom = 0.
    
    $$(\rho_L)_{10} = \rho_{10,00} + \rho_{11,01}$$
    
- **Elemen $(\rho_L)_{11}$ (Baris 1, Kolom 1):** Ambil elemen di mana Leader baris = 1 dan Leader kolom = 1.
    
    $$(\rho_L)_{11} = \rho_{10,10} + \rho_{11,11}$$
    

### 4. Hasil Akhir (Persamaan 4.4)

Dengan menyusun kembali elemen-elemen di atas ke dalam bentuk matriks, kita memperoleh persamaan **(4.4)**:

$$\rho_L = \begin{pmatrix}

\rho_{00,00} + \rho_{01,01} & \rho_{00,10} + \rho_{01,11} \\

\rho_{10,00} + \rho_{11,01} & \rho_{10,10} + \rho_{11,11}

\end{pmatrix}$$

**Kesimpulan Logika:**

Persamaan 4.4 adalah "penyusutan" informasi. Kita menggabungkan baris 1&2 serta baris 3&4 dari matriks asli untuk menghilangkan detail tentang apa yang dilakukan Follower, sehingga kita hanya fokus pada probabilitas dan koherensi aset Leader saja.

---
---

Dalam persamaan **(4.3)**, $\bra{k}_F$ dan $\ket{k}_F$ berfungsi sebagai **operator proyeksi** yang digunakan untuk mengekstraksi informasi spesifik dari sistem gabungan.

Secara teknis, fungsi mereka dalam operasi **Partial Trace** adalah sebagai berikut:

### 1. Sebagai "Filter" Informasi

Dalam sistem dua aset (Leader dan Follower), matriks densitas $\rho_{sys}$ mengandung informasi tentang kedua aset tersebut secara terikat (_entangled_).

- $\ket{k}_F$ dan $\bra{k}_F$ bertindak sebagai alat untuk memilih atau "memfilter" keadaan aset Follower ($F$) pada basis $k$, di mana $k \in \{0, 1\}$.
    
- Operasi ini memungkinkan kita untuk melihat apa yang terjadi pada aset Leader ($L$) ketika kita "menghilangkan" detail dari aset Follower.
    

### 2. Mekanisme Penjumlahan (Tracing Out)

Persamaan **(4.3)** ditulis sebagai:

$$\rho_L = \sum_{k \in \{0,1\}_F} \bra{k}_F \rho_{sys} \ket{k}_F \tag{4.3}$$

Di sini, $\bra{k}$ dan $\ket{k}$ bekerja untuk melakukan perkalian titik (_inner product_) pada bagian Follower saja:

- Ketika $k=0$, kita mengambil semua bagian dari $\rho_{sys}$ yang berkaitan dengan Follower di keadaan $|0\rangle$.
    
- Ketika $k=1$, kita mengambil semua bagian yang berkaitan dengan Follower di keadaan $|1\rangle$.
    
- Penjumlahan ($\sum$) dari kedua hasil ini memastikan bahwa kita mendapatkan gambaran total statistik aset Leader tanpa mempedulikan apakah Follower naik atau turun.
    

### 3. Representasi Matematis (Sandwiching)

Dalam aljabar linear, mengapit sebuah matriks dengan Bra dan Ket seperti $\bra{k} \rho \ket{k}$ disebut sebagai "sandwiching".

- Secara fisik, ini mirip dengan mencari nilai rata-rata atau probabilitas dari operator densitas pada keadaan $k$.
    
- Karena $\rho_{sys}$ berada di ruang $\mathcal{H}_L \otimes \mathcal{H}_F$, mengalikan dengan basis Follower akan "melenyapkan" dimensi Follower dan menyisakan matriks yang hanya hidup di ruang Leader ($\mathcal{H}_L$).
    

**Analogi Sederhana:**

Jika $\rho_{sys}$ adalah buku yang berisi cerita tentang dua orang (Leader dan Follower), maka $\sum \bra{k}_F \dots \ket{k}_F$ adalah proses menyunting buku tersebut dengan cara menghapus semua dialog dan aksi milik Follower, sehingga pembaca hanya bisa melihat perkembangan karakter Leader saja.

Apakah Anda ingin saya menunjukkan bagaimana hasil "sandwiching" ini secara spesifik membentuk elemen-elemen angka dalam matriks $2 \times 2$ pada persamaan 4.4?