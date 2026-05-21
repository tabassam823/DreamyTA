# Analisis Kuantitatif Finansial: *Simple Return* dan *Log Return*

## 1. Pengenalan Data Finansial
Analisis kuantitatif dalam bidang keuangan dimulai dengan pemahaman mendalam terhadap struktur data harga aset. Data utama yang sering digunakan adalah harga aset pada waktu tertentu, yang dilambangkan sebagai $P_t$ untuk harga pada waktu $t$ (hari ini) dan $P_{t-1}$ untuk harga pada periode sebelumnya (kemarin). Harga aset merupakan variabel acak yang fluktuasinya mencerminkan dinamika pasar serta ekspektasi investor terhadap nilai intrinsik aset tersebut di masa depan.

Dalam konteks *Quantitative Finance*, perubahan harga tidak hanya dilihat sebagai nilai absolut, melainkan lebih sering diukur dalam bentuk imbal hasil (*returns*). Penggunaan imbal hasil memberikan keuntungan statistis dibandingkan harga mentah, karena imbal hasil cenderung memiliki sifat stasioner yang lebih baik. Hal ini sangat krusial saat melakukan pemodelan risiko atau optimasi portofolio guna memastikan bahwa model yang dikembangkan memiliki landasan teoretis yang kuat dan reliabel.

## 2. Karakteristik *Simple Return* dan *Log Return*
Imbal hasil dapat dipresentasikan dalam dua format utama, yaitu *simple return* dan *log return*. *Simple return* ($R_t$) didefinisikan sebagai perubahan persentase harga relatif terhadap harga awal, yang secara matematis dirumuskan sebagai berikut:
$$\begin{equation}
R_t = \frac{P_t - P_{t-1}}{P_{t-1}} = \frac{P_t}{P_{t-1}} - 1
\end{equation}$$
Sebaliknya, *log return* ($r_t$) menggunakan logaritma natural dari rasio harga untuk menangkap efek *compounding* secara kontinu. Hubungan antara kedua jenis imbal hasil ini dapat dinyatakan dalam persamaan berikut:
$$\begin{equation}
r_t = \ln\left(\frac{P_t}{P_{t-1}}\right) = \ln(1 + R_t)
\end{equation}$$

Terdapat perbedaan mendasar pada rentang nilai (*range*) antara keduanya yang memengaruhi interpretasi ekonomi. *Simple return* memiliki batas bawah di $-1$ (atau $-100\%$), yang merepresentasikan kondisi ketika harga aset jatuh hingga nol atau bangkrut, namun tidak memiliki batas atas. Di sisi lain, *log return* memiliki rentang dari $(-\infty, \infty)$, di mana penurunan harga hingga mendekati nol akan menghasilkan nilai $r_t$ yang mendekati $-\infty$. Sifat simetri pada *log return* ini sering kali lebih disukai dalam pemodelan stokastik karena menyederhanakan agregasi temporal imbal hasil melalui penjumlahan linear.

## 3. Optimasi Portofolio dan Aproksimasi *Return*
Dalam menyusun portofolio investasi, seorang investor harus menentukan bobot aset ($w_i$) sedemikian rupa sehingga memaksimalkan ekspektasi imbal hasil portofolio ($R_p$). Imbal hasil portofolio dalam bentuk *simple return* bersifat linear, yakni $R_p = \sum_{i=1}^n w_i R_i$. Namun, permasalahan muncul ketika kita mencoba menghitung imbal hasil logaritmik dari sebuah portofolio secara langsung dari *log return* aset individualnya. Secara teoritis, *log return* portofolio yang sebenarnya (*true log return*) didefinisikan sebagai:
$$\begin{equation}
r_{true} = \ln(1 + R_p) = \ln\left(1 + \sum_{i=1}^n w_i R_i\right)
\end{equation}$$

Sering kali dalam proses komputasi atau pengkodean, praktisi menggunakan aproksimasi *log return* portofolio ($\hat{r}_p$) yang merupakan penjumlahan terbobot dari *log return* masing-masing aset, yaitu $\hat{r}_p = \sum w_i r_i$. Pendekatan ini secara intuitif tampak benar, namun secara matematis tidak identik dengan $r_{true}$. Ketidaksamaan ini berasal dari sifat non-linear fungsi logaritma, sehingga $\ln(1 + \sum w_i R_i) \neq \sum w_i \ln(1 + R_i)$. Oleh karena itu, penting untuk memahami besarnya bias atau galat (*error*) yang muncul akibat penggunaan aproksimasi tersebut dalam analisis risiko.

## 4. Analisis Galat dan Pembuktian Matematis
Untuk membuktikan hubungan antara $r_{true}$ dan $\hat{r}_p$, kita dapat menggunakan deret Taylor orde kedua untuk fungsi $\ln(1+x) \approx x - \frac{x^2}{2}$. Pertama, kita ekspansi *log return* portofolio aproksimasi ($\hat{r}_p$) sebagai berikut:
$$\begin{equation}
\hat{r}_p = \sum w_i \ln(1 + R_i) \approx \sum w_i \left( R_i - \frac{R_i^2}{2} \right) = \sum w_i R_i - \frac{1}{2} \sum w_i R_i^2
\end{equation}$$
Selanjutnya, kita ekspansi *log return* portofolio yang sebenarnya ($r_{true}$) dengan cara yang sama:
$$\begin{equation}
r_{true} = \ln(1 + R_p) \approx R_p - \frac{R_p^2}{2} = \left( \sum w_i R_i \right) - \frac{1}{2} \left( \sum w_i R_i \right)^2
\end{equation}$$

Selisih antara nilai sebenarnya dan aproksimasi (galat) dapat dihitung dengan mengurangkan persamaan (4) dari persamaan (5):
$$\begin{split}
Error &= r_{true} - \hat{r}_p \\
&\approx \left[ \sum w_i R_i - \frac{1}{2} \left( \sum w_i R_i \right)^2 \right] - \left[ \sum w_i R_i - \frac{1}{2} \sum w_i R_i^2 \right] \\
&\approx \frac{1}{2} \left[ \sum w_i R_i^2 - \left( \sum w_i R_i \right)^2 \right]
\end{split}$$
Karena ekspresi di dalam kurung siku tersebut merupakan definisi dari varians ($\sigma^2$) dalam konteks rata-rata terbobot, maka didapatkan hubungan:
$$\begin{equation}
r_{true} \approx \hat{r}_p + \frac{1}{2} Var(R)
\end{equation}$$
Hasil ini menunjukkan bahwa penggunaan *log return* dalam optimasi Markowitz (yang berfokus pada ekspektasi imbal hasil) akan menghasilkan bias sebesar setengah dari variansnya. Oleh karena itu, dalam fungsi biaya Markowitz, *expected return* ($\mu$) wajib dihitung menggunakan *simple return* agar tidak terjadi *underestimation* terhadap kinerja portofolio yang sebenarnya.

## 5. Formalisme Kovariansi dalam Analisis Risiko
Kovariansi merupakan metrik krusial untuk mengukur derajat pergerakan bersama antara dua variabel acak, dalam hal ini adalah imbal hasil dari dua aset yang berbeda. Secara matematis, kovariansi antara variabel $X$ dan $Y$ didefinisikan sebagai ekspektasi dari perkalian deviasi masing-masing variabel terhadap rata-ratanya:
$$\begin{split}
Cov(X, Y) &= E[(X - \mu_X)(Y - \mu_Y)] \\
&= E[XY - X\mu_Y - Y\mu_X + \mu_X\mu_Y] \\
&= E[XY] - \mu_Y E[X] - \mu_X E[Y] + \mu_X\mu_Y \\
&= E[XY] - E[X]E[Y]
\end{split}$$
Persamaan di atas sering disebut sebagai rumus komputasi kovariansi. Dalam praktiknya, kovariansi sampel dihitung menggunakan rata-rata aritmatik dari data historis aset:
$$\begin{equation}
\sigma_{XY} = \frac{1}{n} \sum_{i=1}^n (X_i - \bar{X})(Y_i - \bar{Y})
\end{equation}$$

Aturan dasar kovariansi juga mencakup sifat bilinear yang sangat berguna dalam membedah interaksi antar aset dalam portofolio. Salah satu aturan yang paling sering digunakan adalah aturan penjumlahan:
$$\begin{split}
Cov(a+b, c+d) &= E[(a+b)(c+d)] - ((E[a+b])(E[c+d)]) \\
&= (E[ac+ad+bc+bd]) - (E[a]E[c] + E[[a]E[d] + E[b]E[c] + E[b]E[d]) \\
&= E[ac]+E[ad]+E[bc]+E[bd] - E[a]E[c] + E[a]E[d] + E[b]E[c] + E[b]E[d] \\
&= (E[ac]-E[a]E[c]) + (E[ad]-E[a]E[d]) + (E[bc]-E[b]E[c]) + (E[bd]-E[b]E[d]) \\
&= Cov(a,c) + Cov(a,d) + Cov(b,c) + Cov(b,d)
\end{split}$$
Serta aturan penskalaan linear terhadap konstanta $k$:
$$\begin{split}
Cov(kX, Y) &= kE[XY]-kE[X]E[Y] \\
&= k(E[XY]-E[X]E[Y]) \\
&= k \cdot Cov(X, Y)
\end{split}$$

## 6. Invariansi Kovariansi pada *Small Volatility*
Meskipun *expected return* harus menggunakan *simple return*, terdapat argumen kuat mengapa parameter kovariansi ($\sigma$) lebih baik dihitung menggunakan *log return*. Pada kondisi volatilitas rendah (*small volatility*), imbal hasil logaritmik merupakan aproksimasi dari imbal hasil sederhana dikurangi eror ($\epsilon$), 
$$\begin{split}
r_i &\approx R_i + \epsilon \\
E[r_i] &= E[R_i + \epsilon] \\
&= E[R_i] + \epsilon
\end{split}$$Sehingga deviasi logaritmiknya $\Delta_{log}$ adalah
$$\begin{split}
\Delta_{\sigma_{log}} &= r_i - E[r_i] \\
&= (r_i + \epsilon) - (E[R_i] + \epsilon) \\
&= R_i + \epsilon - E[R_i] - \epsilon \\
&= R_i - E[R_i]
\end{split}$$
Maka bisa disimpulkan bahwa $cov(r_i,r_j) \approx cov(R_i,R_j)$.

Jika kita meninjau kovariansi antara dua *log return* aset A dan B, kita mendapatkan ekspansi berikut:
$$\begin{split}
Cov(r_A, r_B) &\approx Cov(\ln(1-R_A), \ln(1-R_B)) \\
&\approx Cov\left(R_A - \frac{R_A^2}{2}, R_B - \frac{R_B^2}{2}\right)
\end{split}$$
Dengan menerapkan aturan bilinear pada persamaan (10), kita dapat menguraikan ekspresi tersebut menjadi:
$$\begin{equation}
Cov(r_A, r_B) \approx Cov(R_A, R_B) - \frac{1}{2} Cov(R_A, R_B^2) - \frac{1}{2} Cov(R_A^2, R_B) + \frac{1}{4} Cov(R_A^2, R_B^2)
\end{equation}$$
Analisis sensitivitas melalui orde magnitudo menunjukkan bahwa jika imbal hasil $R$ berada pada orde $10^{-2}$, maka $Cov(R_A, R_B)$ berada pada orde $10^{-4}$. Suku-suku berikutnya yang melibatkan $R^2$ akan berada pada orde $10^{-6}$ atau bahkan $10^{-8}$. Karena nilai suku-suku tersebut jauh lebih kecil dibandingkan suku utama, maka secara praktis dapat diabaikan.

## 7. Kesimpulan Teknis Pemilihan Parameter
Berdasarkan derivasi pada bagian sebelumnya, dapat disimpulkan bahwa pada kondisi pasar dengan volatilitas yang wajar, berlaku hubungan:
$$\begin{equation}
Cov(r_A, r_B) \approx Cov(R_A, R_B)
\end{equation}$$
Hal ini memberikan justifikasi matematis untuk menggunakan *log return* dalam menghitung matriks kovariansi. Penggunaan *log return* lebih diunggulkan dalam pemodelan risiko karena memiliki rentang $(-\infty, \infty)$ yang lebih sesuai dengan asumsi distribusi normal pada banyak model stokastik, serta memiliki sifat aditif secara temporal. Dengan demikian, konfigurasi optimal dalam optimasi Markowitz adalah menggunakan *simple return* untuk menghitung vektor ekspektasi imbal hasil ($\mu$) guna menghindari bias, dan menggunakan *log return* untuk membangun matriks kovariansi ($\Sigma$) demi stabilitas statistik.
