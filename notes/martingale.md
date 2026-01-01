# Martingale dalam Matematika Keuangan

## Definisi Formal
Dalam teori probabilitas dan proses stokastik, **martingale** adalah model matematika untuk permainan yang adil ("fair game") di mana pengetahuan tentang masa lalu tidak membantu memprediksi kemenangan atau kerugian di masa depan.

Secara formal, sebuah proses stokastik diskrit $X_1, X_2, X_3, \dots$ disebut martingale terhadap filtrasi $\mathcal{F}_n$ (informasi yang tersedia hingga waktu $n$) jika memenuhi dua kondisi:
1.  **Nilai Ekspektasi Terbatas:** $E[|X_n|] < \infty$
2.  **Ekspektasi Bersyarat Konstan:** $E[X_{n+1} | \mathcal{F}_n] = X_n$

Artinya, ekspektasi (nilai harapan) dari nilai masa depan $X_{n+1}$, jika diketahui semua informasi saat ini ($X_1, \dots, X_n$), adalah sama dengan nilai saat ini $X_n$. Dalam waktu kontinu (seperti dalam Libor Market Model), definisi ini diperluas menjadi $E[X_t | \mathcal{F}_s] = X_s$ untuk semua $s \le t$.

## Intuisi dan Relevansi dalam Keuangan
Dalam konteks keuangan, konsep martingale sangat fundamental, terutama dalam penetapan harga derivatif (arbitrage-free pricing).

1.  **Tidak Ada Arbitrase (No-Arbitrage):** Teorema Fundamental Penetapan Harga Aset menyatakan bahwa pasar bebas arbitrase jika dan hanya jika terdapat suatu ukuran probabilitas ekuivalen (disebut *Risk-Neutral Measure* atau *Martingale Measure*) di mana harga aset yang didiskontokan adalah martingale.
2.  **Driftless Property:** Sebuah proses martingale tidak memiliki "drift" atau kecenderungan arah yang dapat diprediksi secara sistematis. Perubahan nilainya di masa depan sepenuhnya didorong oleh volatilitas acak. Ini terlihat pada persamaan diferensial stokastik (SDE) untuk martingale yang tidak memiliki suku $dt$, hanya suku $dW_t$ (Brownian motion):
    $$ dX_t = \sigma(t, X_t) dW_t $$
    Jika ada suku drift ($\mu dt$), proses tersebut bukan martingale (kecuali drift-nya nol).

## Hubungan dengan Paper (LMM)
Dalam paper *"Deep Learning-Based BSDE Solver for Libor Market Model"*, konsep martingale muncul secara spesifik dalam konteks perubahan ukuran (measure change):

*   **Ukuran Forward ($Q^{T_{n+1}}$):** Di bawah ukuran probabilitas ini, suku bunga Libor forward $L_n(t)$ adalah martingale. Ini berarti dinamikanya hanya memiliki komponen difusi (volatilitas) dan tanpa drift. Hal ini sangat menyederhanakan pemodelan karena kita bisa menulis $dL_n(t) = \sigma_n(\dots) dW^{(n+1)}(t)$.
*   **Ukuran Terminal ($Q^{T_N}$):** Ketika kita pindah ke ukuran ini untuk menyamakan kerangka kerja semua suku bunga, sifat martingale hilang untuk suku bunga selain yang terakhir. Muncul suku drift $\mu_n$ yang kompleks (lihat Sub-bab 2.1 dalam ringkasan paper). Memahami kapan sebuah proses adalah martingale dan kapan tidak adalah kunci untuk menurunkan persamaan dinamika yang benar.

## Referensi
*   Musiela, M., & Rutkowski, M. (2005). *Martingale Methods in Financial Modelling*. Springer.
*   Shreve, S. E. (2004). *Stochastic Calculus for Finance II: Continuous-Time Models*. Springer.
*   Investopedia. *Martingale*. Diakses dari [investopedia.com](https://www.investopedia.com/terms/m/martingale.asp).
*   Wikipedia. *Martingale (probability theory)*. Diakses dari [en.wikipedia.org/wiki/Martingale_(probability_theory)](https://en.wikipedia.org/wiki/Martingale_(probability_theory)).
