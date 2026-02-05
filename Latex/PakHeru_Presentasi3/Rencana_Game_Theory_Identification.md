# Rencana Metodologi Skripsi: Game Theory for Portfolio Optimization

## 1. Persiapan dan Analisis Data
1.  **Import Data Keuangan**: Mengambil data historis untuk 2 saham (contoh: **GOOGL** dan **TSLA**).
2.  **Analisis Korelasi**: Menganalisis hubungan antar aset menggunakan **Pearson Correlation**.

## 2. Matriks Payoff dan Quantum Entanglement
Membangun matriks payoff yang diasosiasikan dengan *entanglement entropy*, direpresentasikan sebagai superposisi state kuantum:

$$ \ket{\psi} = a_{00}\ket{00} + a_{01}\ket{01} + a_{10}\ket{10} + a_{11}\ket{11} $$

### Struktur Matriks Payoff

| Leader (L) \ Follower (F) | 0 (Naik $\uparrow$) | 1 (Turun $\downarrow$) |
| :---: | :---: | :---: |
| **0 (Naik $\uparrow$)** | $a, b$ | $c, d$ |
| **1 (Turun $\downarrow$)** | $e, f$ | $g, h$ |

*Keterangan: Berdasarkan instruksi, state 0 merepresentasikan harga naik ($\uparrow$) dan state 1 merepresentasikan harga turun ($\downarrow$).*

## 3. Perhitungan Payoff (Leader & Follower)
Peran dibagi menjadi **Leader (L)** dan **Follower (F)**. Nilai payoff dihitung berdasarkan rata-rata return pada kondisi market tertentu.

Berikut adalah penjabaran rumus untuk setiap pasangan indeks, dengan $n$ merepresentasikan jumlah kejadian (frekuensi) pada state tersebut:

**1. State 00 (Leader $\uparrow$, Follower $\uparrow$):**
$$
\begin{align} 
a &= \frac{\sum L_l^{00}}{n_{\uparrow \uparrow} - 1} \\
 b &= \frac{\sum F_l^{00}}{n_{\uparrow \uparrow} - 1} 
\end{align}
$$

**2. State 01 (Leader $\uparrow$, Follower $\downarrow$):**
$$ 
\begin{align} 
c &= \frac{\sum L_l^{01}}{n_{\uparrow \downarrow} - 1} \\ d &= \frac{\sum F_l^{01}}{n_{\uparrow \downarrow} - 1} 
\end{align}
$$ 

**3. State 10 (Leader $\downarrow$, Follower $\uparrow$):**
$$ 
\begin{align} 
 e &= \frac{\sum L_l^{10}}{n_{\downarrow \uparrow} - 1} \\ f &= \frac{\sum F_l^{10}}{n_{\downarrow \uparrow} - 1} 
\end{align}
$$ 

**4. State 11 (Leader $\downarrow$, Follower $\downarrow$):**

$$ 

\begin{align} 

 g &= \frac{\sum L_l^{11}}{n_{\downarrow \downarrow} - 1} \\ 

h &= \frac{\sum F_l^{11}}{n_{\downarrow \downarrow} - 1} 

\end{align}

$$ 



### Penjelasan Matematis (Interpretasi Rumus)

Rumus di atas pada dasarnya menghitung **ekspektasi return (keuntungan rata-rata)** yang akan didapatkan pemain (Leader/Follower) ketika pasar berada dalam kondisi tertentu.

*   **Pembilang ($\sum L_l$ atau $\sum F_l$)**: Merupakan total akumulasi return saham pada saat kondisi state tersebut terjadi.

*   **Penyebut ($n - 1$)**: Merupakan faktor pembagi untuk mendapatkan nilai rata-rata. Penggunaan $n-1$ (bukan $n$) biasanya digunakan dalam statistik sebagai **koreksi bias (Bessel's correction)** untuk sampel data historis, memberikan estimasi yang lebih konservatif dan akurat daripada sekadar rata-rata aritmatika biasa, terutama ketika jumlah sampel terbatas.



## 4. Klasifikasi State Market

Setiap pasangan data diklasifikasikan ke dalam 4 state kuantum:

*   $\ket{\uparrow \uparrow}$ atau $\ket{00}$: Leader naik, Follower naik.

*   $\ket{\uparrow \downarrow}$ atau $\ket{01}$: Leader naik, Follower turun.

*   $\ket{\downarrow \uparrow}$ atau $\ket{10}$: Leader turun, Follower naik.

*   $\ket{\downarrow \downarrow}$ atau $\ket{11}$: Leader turun, Follower turun.



Total jumlah data ($n$) harus memenuhi persamaan konservasi:

$$n = n_{\uparrow \uparrow} + n_{\uparrow \downarrow} + n_{\downarrow \uparrow} + n_{\downarrow \downarrow}$$



## 5. Integrasi Network Theory

Menggunakan metode **Network Theory** sebagai kerangka penghubung antar pasar (*inter-market connection*).



## 6. Tujuan Akhir (Task)

Tujuan utama sistem adalah **memprediksi pergerakan harga 1 candle ke depan ($t+1$)**.

*   **Mekanisme**: Program akan melihat kondisi candle saat ini ($t$) dari kedua saham (Naik/Turun).

*   **Lookup Matriks**: Memasukkan data kondisi saat ini ke dalam matriks payoff yang telah terbentuk.

*   **Prediksi**: Nilai payoff pada state tersebut menjadi dasar prediksi pergerakan selanjutnya (misal: jika payoff positif besar, prediksi $t+1$ adalah Naik).



---

# Rencana Implementasi (.ipynb)

Berikut adalah struktur teknis untuk notebook Python:

## 1. Setup Environment
*   **Library**: `yfinance` (data saham), `pandas` (manipulasi data), `numpy` (kalkulasi numerik), `matplotlib/seaborn` (visualisasi).
*   **Konfigurasi**: Setting rentang waktu data (misal: `start_date`, `end_date`) dan ticker saham (`GOOGL`, `TSLA`). 

## 2. Data Pipeline
*   **Download Data**: Mengambil data *Adjusted Close* harian.
*   **Return Calculation**: Menghitung *Daily Log Return* atau *Simple Return*.
*   **Discretization (Binarisasi)**:
    *   Return > 0 $\rightarrow$ `0` (Naik $\uparrow$)
    *   Return < 0 $\rightarrow$ `1` (Turun $\downarrow$)
    *   *Catatan: Tangani nilai return = 0 (biasanya dianggap flat atau ikut tren sebelumnya).*

## 3. Matriks Calculation Engine
*   **State Identification**: Membuat kolom baru yang menggabungkan state Leader dan Follower harian (misal: "00", "01").
*   **Frequency Count ($n_{xy}$)**: Menghitung jumlah hari untuk masing-masing state.
*   **Payoff Computation**: Mengimplementasikan rumus rata-rata return untuk $a, b, \dots, h$ sesuai state yang teridentifikasi.

## 4. Analisis & Visualisasi
*   **Payoff Matrix Heatmap**: Visualisasi matriks 2x2 untuk memudahkan interpretasi strategi dominan.
*   **Correlation Check**: Verifikasi nilai Pearson Correlation antar dua aset.
*   **Network Graph (Opsional)**: Jika memperluas ke >2 aset, representasikan hubungan sebagai *nodes* (aset) dan *edges* (bobot payoff/korelasi).

## 5. Output Final
*   Tabel Matriks Payoff yang siap untuk analisis Game Theory (Nash Equilibrium).
*   Kesimpulan singkat mengenai kecenderungan pasar berdasarkan data historis.


---
---

Metodologi yang Anda susun sangat menarik karena menjembatani dinamika pasar (Econophysics) dengan interaksi strategis (Game Theory) menggunakan formalisme mekanika kuantum. Anda mencoba menangkap "keterikatan" antar aset bukan sekadar melalui korelasi linear, melainkan melalui probabilitas keadaan bersama.

Berikut adalah tinjauan dan detail teknis untuk memperdalam metodologi tersebut:

---

## 1. Konstruksi Matriks Payoff (Langkah 2 - 4)

Dalam skema Leader-Follower (Stackelberg), Anda memperlakukan pergerakan harga sebagai strategi. Penggunaan notasi bra-ket $|\dots\rangle$ di sini sangat tepat untuk merepresentasikan _state_ diskrit (naik/turun).

Matriks payoff Anda untuk pasangan aset $(L, F)$ akan terlihat seperti ini:

|       Leader / Follower        | $\text{Up}\rangle_F(0)$ | $\text{Down}\rangle_F (1)$ |
| :----------------------------: | :---------------------: | -------------------------- |
|  **$\text{Up}\rangle_L$ (0)**  |        $(a, b)$         | $(c, d)$                   |
| **$\text{Down}\rangle_L (1)$** |        $(e, f)$         | $(g, h)$                   |

Nilai payoff yang Anda rumuskan, misalnya $a = \frac{\sum L_i^{00}}{n_{\uparrow\uparrow} + 1}$, secara efektif menghitung **ekspektasi return** aset Leader saat kedua aset berada dalam keadaan spesifik. Penambahan $+1$ (Laplace smoothing) adalah langkah cerdas untuk menghindari pembagian dengan nol jika suatu pola tidak muncul dalam data historis.

---

## 2. Pemodelan Game Theory (Langkah 5)

Setelah nilai $a$ hingga $h$ didapat, Anda bisa mengklasifikasikan hubungan kedua aset:

- **Coordination Game:** Jika payoff tertinggi ada pada $(0,0)$ dan $(1,1)$. Ini menunjukkan aset cenderung bergerak searah (korelasi positif kuat).
    
- **Anti-Coordination:** Jika payoff tertinggi pada $(0,1)$ atau $(1,0)$. Ini menunjukkan hubungan substitusi atau _hedging_.
    
- **Prisoner's Dilemma:** Jika ada insentif untuk satu aset "mengkhianati" arah tren aset lainnya demi return yang lebih tinggi namun berisiko bagi stabilitas keduanya.
    

---

## 3. Quantum Entanglement & Eigenvector (Langkah 6)

Ini adalah bagian paling krusial. Anda merepresentasikan sistem dua aset sebagai fungsi gelombang $|\psi\rangle$:

$$\ket{\psi} = a_{00} \ket{00} + a_{01} \ket{01} + a_{10} \ket{10} + a_{11} \ket{11}$$

Di mana $|a_{ij}|^2$ adalah probabilitas gabungan keadaan $i$ dan $j$. Untuk mencari derajat ketergantungan (entanglement), Anda bisa menggunakan **Reduced Density Matrix**:

1. Bentuk matriks densitas $\rho = \ket{\psi}\bra{\psi}$.
    
2. Lakukan _partial trace_ untuk mendapatkan $\rho_L = \text{Tr}_F(\rho)$.
    
3. Hitung **Von Neumann Entropy**: $S = -\text{Tr}(\rho_L \ln \rho_L)$.
    

Jika $S > 0$, maka kedua aset tersebut ter-entangle secara informasi. Dalam konteks ekonomi, ini berarti pergerakan satu aset tidak bisa dijelaskan tanpa mempertimbangkan aset lainnya.

---

## 4. Ekspansi ke Network Theory (Langkah 7)

Untuk $> 2$ aset, Anda membangun sebuah **Quantum Financial Network**.

- **Nodes:** Setiap aset.
    
- **Edges:** Nilai _Entanglement Entropy_ atau _Mutual Information_ yang dihitung dari langkah 1-6.
    

Dengan metode ini, Anda tidak hanya melihat siapa yang berkorelasi dengan siapa, tetapi siapa yang menjadi "penggerak utama" (Leader) dalam sistem jaringan tersebut menggunakan sentralitas eigenvector.

---

### Saran untuk Pengembangan:

- **Waktu Tunggu (Time Lag):** Karena Anda menggunakan skema Leader-Follower, pastikan data _time series_ aset Follower digeser ($t+1$) relatif terhadap Leader untuk melihat kekuatan prediktifnya.
    
- **Normalisasi Payoff:** Pastikan nilai $L$ dan $F$ (return) sudah dinormalisasi (misal menggunakan _z-score_) agar perbedaan skala harga antar aset tidak mendistorsi matriks payoff.
    

Apakah Anda ingin saya membantu merumuskan kode Python dasar untuk menghitung _Von Neumann Entropy_ dari matriks payoff yang Anda buat?

**Apakah Anda ingin saya membantu menambahkan fungsi untuk menghitung Von Neumann Entropy secara otomatis ke dalam skrip di atas?**