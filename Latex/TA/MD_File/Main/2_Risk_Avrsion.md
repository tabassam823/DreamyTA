# Teori *Volatility Drag* dan *Risk Aversion* Endogen

## 1. Hubungan Ekspektasi Imbal Hasil dan Volatilitas
Dalam analisis portofolio dinamis, hubungan antara *simple return* ($R$) dan *log return* ($r$) tidak hanya bersifat logaritmik, tetapi juga melibatkan komponen volatilitas yang signifikan. Secara teoretis, ekspektasi dari imbal hasil logaritmik dapat diaproksimasi melalui ekspansi Taylor orde kedua sebagai berikut:
$$\begin{split}
\ln(1+x) &= x-\frac{x^2}{2}+\frac{x^3}{3}-\frac{x^4}{4} \dots \\
\ln(1+R) &= R-\frac{R^2}{2}+\frac{R^3}{3}-\frac{R^4}{4} \dots \\
&\approx R-\frac{R^2}{2}
\end{split}$$
sehingga bentuk ekspektasi dari imbal hasil logaritmik secara eksplisit adalah
$$\begin{split}
E[r] &= E[\ln(1+R)] \\
&\approx E\left[ R - \frac{1}{2}R^2 \right] \\
&= E[R] - \frac{1}{2}E[R^2]
\end{split}$$
Untuk menjabarkan $E[R^2]$, kita menggunakan definisi varians variabel acak:
$$\begin{split}
Var(R) &= E[(R - E[R])^2] \\
&= E[R^2 - 2R E[R] + (E[R])^2] \\
&= E[R^2] - 2(E[R])^2 + (E[R])^2 \\
&= E[R^2] - (E[R])^2
\end{split}$$
Sehingga diperoleh hubungan $E[R^2] = Var(R) + (E[R])^2$. Substitusi kembali ke dalam persamaan (1) menghasilkan:
$$\begin{equation}
\mu_r = \mu_R - \frac{1}{2}(\sigma_R^2 + \mu_R^2)
\end{equation}$$
Pada kondisi pasar di mana rata-rata imbal hasil harian mendekati nol ($\mu_R \approx 0$), maka suku $\mu_R^2$ menjadi tidak signifikan dan dapat diabaikan, sehingga:
$$\begin{equation}
\mu_r \approx \mu_R - \frac{1}{2}\sigma_R^2
\end{equation}$$

## 2. Konsep *Volatility Drag*
Suku $\frac{1}{2}\sigma_R^2$ dalam persamaan (3) dikenal sebagai *volatility drag*. Fenomena ini menjelaskan bagaimana fluktuasi harga dapat "mengikis" imbal hasil geometrik atau logaritmik suatu aset meskipun rata-rata imbal hasil aritmatiknya tetap positif. Sebagai ilustrasi teknis, jika sebuah aset mengalami penurunan $50\%$ kemudian diikuti kenaikan $50\%$, nilai aset tersebut tidak kembali ke titik awal (100 -> 50 -> 75). Selisih sebesar $25\%$ tersebut merupakan representasi nyata dari *volatility drag*.

Analisis sensitivitas terhadap imbal hasil logaritmik menunjukkan bagaimana perubahan parameter input memengaruhi $\mu_r$. Turunan parsial terhadap $\mu_R$ dan $\sigma_R$ adalah sebagai berikut:
- Efek imbal hasil aritmatik: 
$$\begin{split}
\frac{\partial \mu_r}{\partial \mu_R} &= \frac{\partial}{\partial \mu_R} \left(\mu_R - \frac{1}{2} \sigma_R^2\right) \\
&= 1
\end{split}$$
- Efek volatilitas: 
$$\begin{split}
\frac{\partial \mu_r}{\partial \sigma_R} &= \frac{\partial}{\partial \sigma_R} \left(\mu_R - \frac{1}{2}\sigma_R^2 \right) \\
&= -\frac{2\sigma_R}{2} \\
&= -\sigma_R
\end{split}$$

Perubahan total pada imbal hasil logaritmik dapat dirumuskan melalui diferensial total:
$$\begin{equation}
d\mu_r = 1 \cdot d\mu_R - \sigma_R \cdot d\sigma_R
\end{equation}$$
Persamaan ini menegaskan bahwa setiap peningkatan volatilitas akan memberikan dampak negatif linear terhadap ekspektasi imbal hasil logaritmik, yang memperkuat urgensi manajemen risiko dalam optimasi portofolio.

## 3. Analisis Rasio dan Sensitivitas Risiko
Perbedaan antara penggunaan *simple return* dan *log return* terlihat jelas saat kita meninjau rasio imbal hasil terhadap risiko ($z$). 
1. Jika menggunakan *simple return*: $$z_{simple} = \frac{\mu_R}{\sigma_R}$$
2. Jika menggunakan *log return*: 
$$\begin{split}
z_{log} &= \frac{\mu_r}{\sigma_r} \\
&\approx \frac{\mu_R - \frac{1}{2}\sigma_R^2}{\sigma_R} \\
&= \frac{\mu_R}{\sigma_R} - \frac{1}{2}\sigma_R
\end{split}$$

Secara matematis, $z_{log}$ akan selalu lebih kecil daripada $z_{simple}$ karena adanya faktor pengurangan volatilitas. Walupun expected return memunculkan nilai nol, nilai dari $z_{log}$ tidak akan ikut bernilai nol sehingga akan pengaruh volatilitasnya. Hal ini menunjukkan bahwa penggunaan *log return* memberikan penilaian risiko yang lebih konservatif dan realistis.

Selanjutnya, jika kita meninjau parameter sensitivitas $\lambda$ (yang sering dikaitkan dengan fungsi penalti risiko), perbandingannya adalah sebagai berikut:
- $\lambda_{simp} = e^{-\frac{\mu_R}{\sigma_R}}$
- $\lambda_{log} = \exp\left(-\frac{\mu_r}{\sigma_r}\right) \approx \exp\left(-\frac{\mu_R - \frac{1}{2}\sigma_R^2}{\sigma_R}\right) = \exp\left(-\frac{\mu_R}{\sigma_R} + \frac{1}{2}\sigma_R\right)$

Melalui manipulasi aljabar, diperoleh hubungan:
$$\begin{equation}
\lambda_{log} = \lambda_{simp} \cdot e^{\frac{1}{2}\sigma_R}
\end{equation}$$
Karena $e^{\frac{1}{2}\sigma_R} > 1$, maka $\lambda_{log} > \lambda_{simp}$. Hal ini membuktikan bahwa metrik yang berbasis pada *log return* secara implisit telah mengintegrasikan faktor volatilitas ke dalam perhitungan sensitivitasnya, sementara metrik berbasis *simple return* cenderung mengabaikan dinamika internal dari fluktuasi harga aset tersebut.
