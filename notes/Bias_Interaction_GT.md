# Analisis Game Theory: Pairwise Stackelberg 4 Agen ke Ising Hamiltonian
## 1. Struktur Permainan (Pairwise Sequential)

Dalam sistem 4 agen $\{A, B, C, D\}$, kita meninjau interaksi sebagai kumpulan permainan dua pemain. Untuk setiap pasang agen $(i, j)$, terdapat dua skenario:
1.  Agen $i$ sebagai Leader dan Agen $j$ sebagai Follower ($i_L, j_F$).
2.  Agen $j$ sebagai Leader dan Agen $i$ sebagai Follower ($j_L, i_F$).

Total terdapat $P(4,2) = 12$ interaksi dalam sistem jika semua agen saling berinteraksi secara bergantian.

## 2. Pembentukan Matriks Payoff Per Pasangan

Misalkan untuk pasangan Agen $i$ dan $j$, fungsi utilitas masing-masing adalah:
*   $U_i(s_i, s_j) = \alpha_{ij} s_i + \gamma_{ij} s_i s_j$
*   $U_j(s_i, s_j) = \alpha_{ji} s_j + \gamma_{ji} s_i s_j$

**Definisi Variabel ($\alpha_{ij}, \gamma_{ij} \in \mathbb{R}$):**
1.  **$\alpha_{ij}$ (Intrinsic Utility):** Bilangan riil yang merepresentasikan kecenderungan mandiri agen $i$ saat berinteraksi dengan $j$. Ini adalah bobot linear yang menentukan seberapa kuat preferensi pribadi agen tanpa pengaruh pihak lain.
2.  **$\gamma_{ij}$ (Interaction Utility):** Bilangan riil yang merepresentasikan kekuatan korelasi. Jika positif, agen mendapat utilitas tambahan saat strateginya sama ($s_i = s_j$). Jika negatif, agen mendapat utilitas saat strateginya berbeda ($s_i \neq s_j$).

Dalam skema **Stackelberg ($i_L, j_F$)**:
1.  **Follower ($j$):** Memilih $s_j$ untuk memaksimalkan $U_j$ setelah melihat $s_i$.
2.  **Leader ($i$):** Memilih $s_i$ dengan mengantisipasi respon optimal $s_j^*(s_i)$.

### Matriks Payoff Biner ($s \in \{+1, -1\}$):
| Strategi ($s_i, s_j$) | Payoff Agen $i$              | Payoff Agen $j$              |
| :-------------------- | :--------------------------- | :--------------------------- |
| (+1, +1)              | $\alpha_{ij} + \gamma_{ij}$  | $\alpha_{ji} + \gamma_{ji}$  |
| (+1, -1)              | $\alpha_{ij} - \gamma_{ij}$  | $-\alpha_{ji} - \gamma_{ji}$ |
| (-1, +1)              | $-\alpha_{ij} - \gamma_{ij}$ | $\alpha_{ji} - \gamma_{ji}$  |
| (-1, -1)              | $-\alpha_{ij} + \gamma_{ij}$ | $-\alpha_{ji} + \gamma_{ji}$ |

| Strategi ($s_i, s_j$) | $+1$                                                      | $-1$                         |
| :-------------------- | :-------------------------------------------------------- | :--------------------------- |
| $+1$                  | $\alpha_{ij} + \gamma_{ij}$  $\alpha_{ji} + \gamma_{ji}$  | $\alpha_{ij} - \gamma_{ij}$  $-\alpha_{ji} - \gamma_{ji}$  |
| $-1$                  | $-\alpha_{ij} - \gamma_{ij}$  $\alpha_{ji} - \gamma_{ji}$ | $-\alpha_{ij} + \gamma_{ij}$  $-\alpha_{ji} + \gamma_{ji}$ |


**Interpretasi Strategi Finansial:**
*   **$s_i = +1$ (Bullish):** Merepresentasikan ekspektasi harga naik atau munculnya *candle* hijau (Up).
*   **$s_i = -1$ (Bearish):** Merepresentasikan ekspektasi harga turun atau munculnya *candle* merah (Down).

## 3. Estimasi Payoff dengan Laplace Smoothing

Sebelum melakukan ekstraksi parameter, kita harus mengisi nilai dalam matriks payoff berdasarkan data historis. Untuk menghindari bias akibat data yang jarang muncul (sparse data), kita menggunakan **Laplace Smoothing**.

Misalkan $L$ adalah payoff Leader dan $F$ adalah payoff Follower, dengan $n_{ij}$ adalah jumlah kejadian strategi $(i, j)$ muncul dalam data. Nilai sel matriks ($a, b, c, \dots$) dihitung sebagai berikut:

$$
\begin{align}
    a &= \frac{\sum L^{00}}{n_{00} + 1}, \quad b = \frac{\sum F^{00}}{n_{00} + 1} \\
    c &= \frac{\sum L^{01}}{n_{01} + 1}, \quad d = \frac{\sum F^{01}}{n_{01} + 1} \\
    e &= \frac{\sum L^{10}}{n_{10} + 1}, \quad f = \frac{\sum F^{10}}{n_{10} + 1} \\
    g &= \frac{\sum L^{11}}{n_{11} + 1}, \quad h = \frac{\sum F^{11}}{n_{11} + 1}
\end{align}
$$

**Tujuan:** Menstabilkan nilai payoff agar perhitungan bias ($h_i$) dan interaksi ($J_{ij}$) tidak meledak atau error saat menghadapi data yang terbatas.

## 4. Akumulasi Menjadi Total Hamiltonian

Untuk mendapatkan model Ising tunggal bagi seluruh 4 agen, kita menjumlahkan seluruh utilitas dari 12 permainan tersebut (atau subset yang ditentukan) ke dalam satu fungsi biaya total $E$:

$$E = - \sum_{i} \sum_{j \neq i} U_{i,j}(s_i, s_j)$$

Di mana $U_{i,j}$ adalah utilitas agen $i$ ketika berinteraksi dengan agen $j$.

## 4. Mendapatkan Nilai Bias ($h_i$) dan Interaksi ($J_{ij}$)

Setelah menjumlahkan seluruh fungsi utilitas, kita kelompokkan suku-sukunya untuk dicocokkan dengan bentuk Ising:
$$H = - \sum_{i} h_i s_i - \sum_{i<j} J_{ij} s_i s_j$$

### A. Parameter Bias ($h_i$)
Bias agen $i$ adalah akumulasi dari kecenderungan internalnya di semua permainan di mana dia terlibat (baik sebagai Leader maupun Follower).

$$h_i = \sum_{j \neq i} (\text{Koefisien } s_i \text{ saat } i \text{ jadi Leader}) + \sum_{j \neq i} (\text{Koefisien } s_i \text{ saat } i \text{ jadi Follower})$$

Secara matematis:
$$h_i = \sum_{j \neq i} \alpha_{ij}$$

### B. Parameter Interaksi ($J_{ij}$)
Interaksi antara agen $i$ dan $j$ adalah gabungan dari pengaruh timbal balik kedua agen tersebut. Karena Ising Hamiltonian bersifat simetris ($J_{ij} = J_{ji}$), maka nilai $J_{ij}$ adalah total kekuatan hubungan dari kedua arah.

$$J_{ij} = \gamma_{ij} + \gamma_{ji}$$

*   **Jika $J_{ij} > 0$:** Kedua agen secara total memiliki insentif untuk berkoordinasi (strategi sama).
*   **Jika $J_{ij} < 0$:** Terdapat konflik kepentingan yang kuat (strategi berlawanan).

## 5. Metode Perhitungan Marginal

Dalam praktik teknis, jika kita sudah memiliki tabel matriks payoff, nilai $h_i$ dan $J_{ij}$ dapat diekstraksi menggunakan selisih marginal:

### A. Ekstraksi Bias ($h_i$)
Bias adalah setengah dari selisih utilitas saat agen $i$ memilih strategi $+1$ dibandingkan $-1$ (kondisi agen lain dianggap konstan):
$$h_i = \frac{U_i(s_i = +1) - U_i(s_i = -1)}{2}$$

### B. Ekstraksi Interaksi ($J_{ij}$)
Interaksi diperoleh dari selisih marginal utilitas yang melibatkan hubungan dua agen:
$$J_{ij} = \frac{[U_{total}(+1, +1) + U_{total}(-1, -1)] - [U_{total}(+1, -1) + U_{total}(-1, +1)]}{4}$$
*(Pembagi 4 digunakan untuk menormalisasi perubahan tanda pada kedua variabel biner).*

## 6. Pendekatan Kuantum: QMI & Von Neumann Entropy

Untuk mendapatkan parameter interaksi ($J_{ij}$) yang lebih akurat dalam sistem yang kompleks (seperti pasar saham), kita dapat menggunakan kerangka **Teori Informasi Kuantum**. Pendekatan ini melampaui statistik linear klasik.

### A. Matriks Densitas ($\rho$) dan Entropi
Dalam **Quantum Econophysics**, probabilitas strategi agen direpresentasikan oleh matriks densitas $\rho$. Ketidakpastian informasi dalam sistem diukur dengan **Entropi Von Neumann**:
$$S(\rho) = -\text{Tr}(\rho \ln \rho)$$

### B. Quantum Mutual Information (QMI)
Hubungan antar agen diukur melalui QMI ($I$), yang menangkap korelasi total (klasik + kuantum) antara dua agen $i$ dan $j$:
$$I(i:j) = S(\rho_i) + S(\rho_j) - S(\rho_{ij})$$

### C. Ekstraksi $J_{ij}$ dari QMI
Dalam model Hamiltonian Learning, nilai interaksi $J_{ij}$ berbanding lurus dengan kekuatan informasi yang dibagikan (QMI). Semakin tinggi QMI antara dua agen, semakin kuat interaksi $J_{ij}$ dalam model Ising kita. Ini memungkinkan kita untuk:
1.  **Mendeteksi Herding:** Mengidentifikasi kapan agen-agen mulai meniru satu sama lain secara massal (QMI melonjak).
2.  **Korelasi Non-Linear:** Menangkap hubungan tersembunyi antar emiten saham yang tidak terdeteksi oleh korelasi Pearson biasa.

## 7. Contoh Kasus 4 Agen (A, B, C, D)

Jika kita asumsikan interaksi homogen di mana setiap Leader mendapat keuntungan $+2$ dari kesesuaian strategi ($\gamma_L = 2$) dan Follower mendapat $+1$ ($\gamma_F = 1$), serta setiap agen punya preferensi pribadi $\alpha = 0.5$:

1.  **Bias ($h_A$):**
    $h_A = \alpha_{AB} + \alpha_{AC} + \alpha_{AD} + \alpha_{BA} + \alpha_{CA} + \alpha_{DA}$
    Jika semua $\alpha = 0.5$, maka $h_A = 6 \times 0.5 = 3.0$.

2.  **Interaksi ($J_{AB}$):**
    $J_{AB} = \gamma_{AB} (\text{A as L}) + \gamma_{BA} (\text{B as L})$
    Jika $\gamma_L = 2$ dan $\gamma_F = 1$ (dari sisi lawan), maka $J_{AB} = 2 + 1 = 3.0$.

## 6. Kesimpulan
Dalam skema Pairwise Stackelberg, $h_i$ mencerminkan **agregat egoisme/preferensi pribadi** agen di seluruh sesi permainan, sedangkan $J_{ij}$ mencerminkan **akumulasi pengaruh timbal balik** (pengaruh Leader terhadap Follower ditambah pengaruh Follower terhadap Leader).
