# Rangkuman dan Analisis Paper: Game-Theoretic Optimal Portfolios

## 1. Pendahuluan
Paper ini membangun landasan matematis untuk model investasi kompetitif menggunakan notasi vektor dan teori probabilitas. Parameter dasar yang didefinisikan meliputi:

*   **Vektor Saham ($X$):** Merepresentasikan kondisi pasar, di mana $X = (X_{1}, ..., X_{m})$ adalah vektor nilai kembalian (*return*) per unit investasi pada saham ke-$i$, dengan asumsi $X_i \ge 0$.
*   **Distribusi Bersama ($F(x)$):** Vektor $X$ diasumsikan ditarik dari fungsi distribusi $F(x)$ yang diketahui, yang mencerminkan sifat stokastik pasar dan korelasi antar aset.
*   **Vektor Portofolio ($b$):** Variabel keputusan investor $b = (b_{1}, ..., b_{m})$, di mana $b_i$ adalah proporsi kekayaan yang dialokasikan pada saham ke-$i$. Syarat $b_i \ge 0$ dan $\sum b_i = 1$ menunjukkan pelarangan *short selling* dan alokasi modal penuh.
*   **Modal Acak ($S$):** Payoff strategi didefinisikan sebagai hasil perkalian titik $S = b^t X$.

Selanjutnya, diperkenalkan konsep *Two-Person Zero-Sum Game* di mana tujuan investor adalah mengalahkan lawan. Fungsi *payoff* permainan didefinisikan sebagai ekspektasi dari fungsi $\phi$ terhadap rasio kekayaan kedua pemain, $E\phi(S_1/S_2)$, di mana $\phi$ adalah fungsi non-decreasing.

Hipotesis utama yang diajukan adalah bahwa **Portofolio Log-Optimal ($b^*$)**, yaitu portofolio yang memaksimalkan $E[\ln(b^t X)]$, merupakan solusi universal untuk berbagai jenis fungsi payoff kompetitif tersebut.

Persamaan (1.1) mendefinisikan ruang strategi permainan yang melibatkan dua tahap keputusan:
1.  **Randomisasi Awal:** Pemain memilih distribusi $G_i(w)$ untuk menukar modal awal (1 unit) menjadi variabel acak $W_i$ yang "adil" (syarat $E[W_i] \le 1$ dan $W_i \ge 0$).
2.  **Alokasi Portofolio:** Modal hasil randomisasi ($W_i$) kemudian dialokasikan ke pasar menggunakan vektor portofolio $b_i$.

Tujuan permainan didefinisikan sebagai masalah Minimax untuk mencari Nilai Permainan ($v$). Penulis juga mendemonstrasikan universalitas model ini dengan menunjukkan bahwa berbagai tujuan investasi—seperti memaksimumkan probabilitas menang ($P(S_1 > S_2)$), ekspektasi rasio, hingga fungsi logaritmik—dapat direpresentasikan sebagai bentuk khusus dari $E \phi(S_1 / S_2)$.

## 2. Strategi Optimal Murni pada Permainan Primitif ($\phi$-Game)
Bagian ini menganalisis "Permainan Primitif", yaitu kondisi teoretis di mana belum ada pasar saham dan pemain hanya memilih variabel acak "adil" $W$. Tujuannya adalah memaksimalkan $E~\phi(W_{1}/W_{2})$.

Fokus utama analisis adalah menentukan kondisi di mana strategi terbaik adalah **tidak melakukan randomisasi** (strategi murni $W=1$). Menggunakan konsep *Saddlepoint* (Titik Pelana), **Teorema 1** menyatakan bahwa strategi optimal murni $W_{1}^{*} = W_{2}^{*} = 1$ tercapai jika dan hanya jika:
1.  Turunan pertama $\phi'(1)$ ada dan bernilai $\ge 0$.
2.  Fungsi $\phi$ memenuhi pertidaksamaan kelengkungan tertentu yang mengindikasikan sifat konkaf (cekung) di sekitar titik 1.

Secara implisit, teorema ini menyatakan bahwa jika fungsi kepuasan ($\phi$) bersifat cekung (mencerminkan penghindaran risiko, seperti fungsi logaritma), maka strategi terbaik adalah mempertahankan modal tanpa melakukan perjudian tambahan ($W=1$).

## 3. Keluarga Konveks (Convex Families)
Bagian ini menjembatani optimasi logaritmik dengan pertidaksamaan linear. Penulis membandingkan dua jenis portofolio:
*   $b^*$: Portofolio yang memaksimalkan pertumbuhan logaritmik ($E \ln (b'X)$).
*   $b^{**}$: Portofolio yang mendominasi secara linear, memenuhi $E(S/S^{**}) \le 1$.

Penulis menunjukkan bahwa $b^*$ dan $b^{**}$ adalah identik jika himpunan variabel acak yang tersedia membentuk **Keluarga Konveks**. Keluarga konveks didefinisikan sebagai himpunan di mana campuran linear dari dua anggota himpunan juga merupakan anggota himpunan tersebut ($\lambda S_1 + (1-\lambda)S_2 \in \mathcal{S}$). Berbagai jenis investasi, termasuk portofolio standar, portofolio dengan kendala (*constrained*), dan strategi sekuensial, terbukti memenuhi sifat konveksitas ini.

**Teorema 2** menjadi inti dari bagian ini, menyatakan ekuivalensi berikut untuk keluarga konveks:
$$E \ln(S/S^*) \le 0 \iff E(S/S^*) \le 1$$

Implikasi praktis dari teorema ini dirangkum dalam **Corollary 2** (Kondisi Kuhn-Tucker), yang memberikan metode verifikasi optimalitas portofolio:
1.  $E(X_i/S^*) \le 1$ untuk semua saham individu $i$.
2.  $b_i^* = 0$ jika $E(X_i/S^*) < 1$.
Kondisi ini menunjukkan bahwa portofolio optimal telah menyerap seluruh potensi keuntungan pasar ("alpha"), sehingga tidak ada saham individu yang secara rata-rata dapat mengalahkan kinerja relatif portofolio tersebut.

## 4. Permainan $\phi$ di Pasar Saham
Penulis menggabungkan hasil dari Teorema 1 dan Teorema 2 untuk membuktikan ketangguhan (*robustness*) portofolio Log-Optimal dalam konteks permainan pasar saham.

**Teorema 3 (Teorema Pemisahan)** menyatakan bahwa strategi optimal untuk permainan pasar saham terfaktor menjadi dua bagian independen:
1.  **Komponen Permainan ($W^*$):** Strategi randomisasi modal awal yang bergantung pada preferensi risiko ($\phi$), mengambil solusi dari Permainan Primitif.
2.  **Komponen Investasi ($b^*$):** Alokasi portofolio yang selalu berupa Portofolio Log-Optimal, independen terhadap bentuk fungsi $\phi$.

Pembuktian dilakukan menggunakan substitusi variabel $Z = (W_2 S_2)/S^*$. Karena $S^*$ memiliki sifat dominasi linear ($E[S/S^*] \le 1$), variabel $Z$ terbukti tetap merupakan variabel acak yang adil. Hal ini mereduksi masalah kompleks pasar saham kembali menjadi bentuk permainan primitif sederhana. Kesimpulannya, untuk memenangkan permainan, investor cukup menggunakan portofolio Log-Optimal untuk aspek investasi, dan hanya perlu menyesuaikan profil risiko pada level modal awal.

## 5. Permainan Pasar Bertahap (Multistage)
Analisis diperluas ke dimensi waktu ($n$ periode) dengan memperhitungkan bunga majemuk (*compounding*) dan realokasi aset. Strategi didefinisikan sebagai urutan keputusan investasi yang dapat bergantung pada sejarah pasar sebelumnya.

**Teorema 4** menunjukkan bahwa prinsip **Log-Optimal Myopic** (rabun jauh) adalah strategi terbaik. Pada setiap tahap $k$, investor cukup memaksimalkan ekspektasi logaritma kondisional saat itu ($E[\ln b_k' X_k | \text{Sejarah}]$). Hal ini dimungkinkan karena sifat aditif dari fungsi logaritma ($E \ln S_n = \sum E \ln S_k$), yang mengubah optimasi produk jangka panjang menjadi penjumlahan optimasi jangka pendek. Karena strategi sekuensial terbukti membentuk keluarga konveks, sifat dominasi linear tetap berlaku, menjamin optimalitas strategi ini dalam konteks permainan jangka panjang.

## 6. Contoh: Randomisasi Posterior Berdasarkan Modal Relatif
Bagian ini membahas skenario di mana pemain dapat mengamati modal lawan dan mengubah strategi di tengah permainan (*Posterior/Conditional Randomization*). Intuisi awal mungkin menyarankan bahwa pemain yang tertinggal harus mengambil risiko lebih besar ("judi nekat") untuk mengejar ketertinggalan.

Namun, **Teorema 5** membantah intuisi ini. Strategi optimal terbukti tetaplah strategi "buta" atau tanpa syarat (*unconditional*):
1.  Tetap memegang portofolio Log-Optimal ($b^*$).
2.  Tetap menggunakan strategi randomisasi awal ($W^*$) yang sama dengan permainan primitif.

Alasannya terletak pada konsep **"Jangkauan Adil" (*Fair Reach*)**. Karena portofolio Log-Optimal ($S^*$) mendominasi semua strategi lain secara rasio ($E[S/S^*] \le 1$), segala bentuk penyimpangan atau manuver berdasarkan posisi lawan tidak akan memberikan keuntungan statistik yang cukup untuk mengalahkan disiplin $S^*$. Upaya untuk melakukan randomisasi bersyarat terbukti tidak lebih baik daripada strategi minimax standar.

## 7. Kesimpulan
Makalah ini menyimpulkan bahwa portofolio yang memaksimalkan ekspektasi logaritma ($E \ln S$) memiliki properti optimalitas *game-theoretic* yang universal.

1.  **Universalitas:** Strategi ini optimal untuk satu periode maupun banyak periode, dan untuk berbagai fungsi tujuan ($\phi$) selama bersifat non-decreasing. Investor tidak perlu mengetahui horizon waktu atau fungsi utilitas lawan secara spesifik untuk memilih portofolio saham.
2.  **Pemisahan Keputusan:** Keputusan investasi (pilih $b^*$) terpisah sepenuhnya dari keputusan manajemen risiko (pilih $W^*$). Jika fungsi tujuan bersifat cekung (penghindaran risiko), randomisasi tidak diperlukan sama sekali.
3.  **Dominasi:** Keunggulan Log-Optimal didasarkan pada sifat dominasi rasionya ($E[S/S^*] \le 1$), yang menjamin bahwa kekayaan strategi lain tidak akan pernah secara sistematis melampaui kekayaan strategi Log-Optimal dalam jangka panjang.
