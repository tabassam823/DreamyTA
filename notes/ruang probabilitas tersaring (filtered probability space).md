# Ruang Probabilitas Tersaring (Filtered Probability Space)

## Pendahuluan
Dalam matematika keuangan dan kalkulus stokastik, **Ruang Probabilitas Tersaring** (Filtered Probability Space) adalah konsep fundamental yang digunakan untuk memodelkan eksperimen acak di mana informasi terungkap seiring berjalannya waktu. Konsep ini sangat penting dalam pemodelan harga aset (seperti dalam *Libor Market Model* yang dibahas pada paper), karena memungkinkan kita untuk mendefinisikan bagaimana ketidakpastian berkurang atau bagaimana informasi bertambah dari waktu ke waktu.

## Definisi Formal
Sebuah ruang probabilitas tersaring biasanya dinotasikan sebagai tupel empat elemen:
$$(\Omega, \mathcal{F}, \mathbb{F}, P)$$

Di mana komponen-komponennya adalah sebagai berikut:

1.  **$\Omega$ (Ruang Sampel / Sample Space):**
    Himpunan dari semua kemungkinan hasil kejadian (outcome) yang bisa terjadi. Dalam konteks keuangan, ini bisa merepresentasikan semua kemungkinan jalur pergerakan harga pasar di masa depan.

2.  **$\mathcal{F}$ (Sigma-Aljabar / Sigma-Algebra):**
    Koleksi dari semua kejadian (subset dari $\Omega$) yang mungkin dapat kita beri nilai probabilitasnya. Ini merepresentasikan "total informasi" yang mungkin diketahui di akhir waktu.

3.  **$P$ (Ukuran Probabilitas / Probability Measure):**
    Fungsi yang memberikan nilai probabilitas (antara 0 dan 1) untuk setiap kejadian di dalam $\mathcal{F}$.

4.  **$\mathbb{F} = (\mathcal{F}_t)_{t \geq 0}$ (Filtrasi / Filtration):**
    Ini adalah elemen kunci yang membedakan konsep ini dari ruang probabilitas biasa. Filtrasi adalah keluarga sigma-aljabar yang "membesar" seiring waktu ($\mathcal{F}_s \subseteq \mathcal{F}_t \subseteq \mathcal{F}$ untuk $s \le t$).
    *   **Interpretasi:** $\mathcal{F}_t$ merepresentasikan informasi yang tersedia bagi pengamat pada waktu $t$.
    *   Sifat $\mathcal{F}_s \subseteq \mathcal{F}_t$ berarti kita tidak pernah "lupa"; informasi yang kita miliki di masa lalu ($s$) tetap menjadi bagian dari informasi yang kita miliki sekarang ($t$).

## Intuisi dalam Keuangan
Bayangkan Anda sedang mengamati harga saham.
*   Pada $t=0$ (hari ini), Anda hanya tahu harga hari ini. Anda tidak tahu harga besok. Ini adalah informasi $\mathcal{F}_0$.
*   Pada $t=1$ (besok), Anda akan melihat pergerakan harga baru. Sekarang Anda tahu harga hari ini DAN harga besok. Pengetahuan Anda bertambah. Ini adalah $\mathcal{F}_1$.
*   **Proses Teradaptasi (Adapted Process):** Sebuah proses stokastik (seperti harga saham $S_t$) dikatakan *teradaptasi* dengan filtrasi $\mathbb{F}$ jika nilai $S_t$ dapat diketahui sepenuhnya hanya dengan informasi yang ada pada waktu $t$ (yaitu $\mathcal{F}_t$). Kita tidak bisa menggunakan informasi masa depan untuk mengetahui harga sekarang.

## Relevansi dengan Paper (BSDE & LMM)
Dalam paper *"Deep Learning-Based BSDE Solver for Libor Market Model"*, konsep ini krusial karena:
1.  **Martingale:** Suku bunga Libor forward dimodelkan sebagai *martingale* di bawah ukuran probabilitas tertentu. Martingale didefinisikan secara ketat bergantung pada filtrasi (ekspektasi bersyarat terhadap informasi masa lalu).
2.  **BSDE (Backward Stochastic Differential Equations):** Paper ini menggunakan *Backward* SDE. Tidak seperti persamaan diferensial biasa yang bergerak dari $t=0$ ke depan, BSDE dipecahkan mundur dari waktu terminal $T$. Solusi BSDE haruslah proses yang **teradaptasi** (adapted) terhadap filtrasi $\mathbb{F}$. Artinya, meskipun kita menghitung mundur, solusi pada waktu $t$ tidak boleh "mengintip" informasi masa depan; ia harus konsisten dengan arus informasi yang wajar.

## Referensi
*   Shreve, S. E. (2004). *Stochastic Calculus for Finance II: Continuous-Time Models*. Springer. (Buku teks standar untuk matematika keuangan).
*   Investopedia/Financial Dictionary definitions on Stochastic Processes and Filtration.
*   *Filtered probability space*. Wikipedia. Diakses dari [en.wikipedia.org/wiki/Filtered_probability_space](https://en.wikipedia.org/wiki/Filtered_probability_space).
*   QuantStart. *Sigma-Algebras and Filtrations in Finance*. Diakses dari [quantstart.com](https://www.quantstart.com).
