# Teori Portofolio Modern: Optimasi *Mean-Variance* Markowitz

## 1. Landasan Teori Portofolio
Teori Portofolio Modern (MPT) yang diperkenalkan oleh Harry Markowitz merupakan tonggak utama dalam analisis investasi kuantitatif. Prinsip utama dari teori ini adalah diversifikasi, di mana risiko suatu portofolio tidak hanya ditentukan oleh risiko individual aset, tetapi juga oleh interaksi atau korelasi antar aset tersebut. Melalui pemilihan bobot aset yang tepat, investor dapat meminimalkan risiko untuk tingkat imbal hasil tertentu, atau sebaliknya, memaksimalkan imbal hasil untuk tingkat risiko tertentu.

Dalam kerangka Markowitz, karakteristik portofolio didefinisikan oleh dua parameter statistik utama: ekspektasi imbal hasil portofolio ($E[R_p]$) dan varians portofolio ($\sigma_p^2$). Imbal hasil portofolio merupakan kombinasi linear dari imbal hasil masing-masing aset terhadap bobot investasinya ($w_i$), yang secara matematis dirumuskan sebagai:
$$\begin{equation}
E[R_p] = \sum_{i=1}^n w_i E[R_i] = \mathbf{w}^T \mathbf{\mu}
\end{equation}$$
di mana $\mathbf{w}$ adalah vektor bobot dan $\mathbf{\mu}$ adalah vektor ekspektasi imbal hasil aset individual.

## 2. Formulasi Risiko dan Matriks Kovariansi
Risiko dalam teori Markowitz diukur melalui varians dari imbal hasil portofolio. Berbeda dengan imbal hasil, perhitungan varians portofolio melibatkan matriks kovariansi ($\Sigma$) untuk menangkap efek korelasi antar aset. Formulasi kuadratik untuk varians portofolio adalah:
$$\begin{equation}
\sigma_p^2 = \sum_{i=1}^n \sum_{j=1}^n w_i w_j \sigma_{ij} = \mathbf{w}^T \Sigma \mathbf{w}
\end{equation}$$
Persamaan di atas menunjukkan bahwa risiko portofolio sangat bergantung pada elemen non-diagonal dari matriks $\Sigma$. Jika korelasi antar aset rendah atau negatif, maka varians total portofolio dapat ditekan secara signifikan melalui mekanisme diversifikasi. Hal inilah yang mendasari penggunaan matriks kovariansi sebagai parameter input utama dalam pemodelan risiko kuantum maupun klasik.

## 3. Optimasi dan Fungsi Utilitas
Tujuan utama dari investor adalah menemukan alokasi bobot optimal $\mathbf{w}$ yang menyeimbangkan antara imbal hasil dan risiko. Hal ini sering kali direpresentasikan melalui fungsi utilitas ($U$) yang ingin dimaksimalkan oleh investor:
$$\begin{equation}
U = E[R_p] - \frac{1}{2} A \sigma_p^2
\end{equation}$$
di mana $A$ adalah koefisien *risk aversion* (penghindaran risiko) dari investor. Secara umum, permasalahan optimasi Markowitz dapat disusun sebagai minimisasi fungsi biaya kuadratik dengan kendala (*constraints*) tertentu:
$$\begin{equation}
\min_{\mathbf{w}} \left( \frac{1}{2} \mathbf{w}^T \Sigma \mathbf{w} - q \mathbf{w}^T \mathbf{\mu} \right)
\end{equation}$$
dengan kendala utama bahwa total bobot investasi harus sama dengan satu:
$$\begin{equation}
\sum_{i=1}^n w_i = \mathbf{w}^T \mathbf{1} = 1
\end{equation}$$
Parameter $q$ pada persamaan (4) merupakan faktor toleransi risiko. Jika $q=0$, investor hanya berfokus pada minimisasi risiko (*minimum variance portfolio*), sedangkan peningkatan nilai $q$ akan menggeser fokus investor menuju pencapaian imbal hasil yang lebih tinggi.

## 4. Interpretasi Biner dan Seleksi Aset
Selain dalam domain kontinu, bobot portofolio $w_i$ sering kali diinterpretasikan sebagai variabel keputusan biner $x_i \in \{0, 1\}$ dalam konteks seleksi aset (*asset selection*). Dalam skema ini, variabel $x_i$ merepresentasikan keputusan diskrit investor: $x_i = 1$ berarti aset $i$ dipilih untuk dibeli atau disertakan dalam portofolio, sedangkan $x_i = 0$ berarti aset tersebut diabaikan. Transformasi ini mengubah masalah optimasi dari domain kalkulus kontinu menjadi masalah optimasi kombinatorial (*combinatorial optimization*).

Interpretasi biner ini sangat relevan dalam pemodelan sistem kuantum karena variabel $x_i$ dapat dipetakan langsung ke dalam status qubit dalam basis komputasi $|0\rangle$ dan $|1\rangle$. Pada kasus khusus di mana setiap aset yang dipilih memiliki bobot yang sama ($w_i = x_i / K$), masalah Markowitz dapat disederhanakan menjadi pencarian kombinasi aset terbaik yang meminimalkan risiko bersama. Pendekatan ini menjadi dasar fundamental bagi pemetaan masalah keuangan ke dalam format QUBO, di mana setiap keputusan "beli" atau "tidak beli" direpresentasikan oleh dinamika energi pada perangkat keras kuantum.

## 5. *Efficient Frontier* dan *Sharpe Ratio*
Hasil dari proses optimasi untuk berbagai tingkat toleransi risiko membentuk sebuah kurva yang dikenal sebagai *Efficient Frontier*. Kurva ini merepresentasikan sekumpulan portofolio optimal yang memberikan imbal hasil tertinggi untuk setiap tingkat risiko tertentu. Portofolio yang berada di bawah kurva ini dianggap tidak efisien karena terdapat alternatif lain yang memiliki risiko lebih rendah untuk imbal hasil yang sama.

Untuk mengukur performa relatif dari sebuah portofolio dibandingkan dengan aset bebas risiko (*risk-free asset*), digunakan metrik *Sharpe Ratio* ($S$):
$$\begin{equation}
S = \frac{R_p - R_f}{\sigma_p}
\end{equation}$$
Secara grafis, portofolio optimal yang paling efisien berada pada titik singgung (*tangency portfolio*) antara *Efficient Frontier* dan garis alokasi modal (*Capital Allocation Line*). Titik ini mewakili portofolio dengan *Sharpe Ratio* tertinggi, yang merupakan tujuan akhir dari banyak strategi manajemen aset modern.


## 6. Penurunan Rumus

$$
\mathcal{L}(\vec{\omega}) = \vec{\omega}^{T} \Sigma \vec{\omega} - \lambda(\mu^T\vec{\omega})
$$
$$
\boxed{\mathcal{L(\vec{\omega)}} = \begin{pmatrix}\omega_1 & \omega_2 & \dots & \omega_n\end{pmatrix} \begin{pmatrix}\sigma_{11} & \sigma_{12} & \dots & \sigma_{1n} \\ \sigma_{21} & \sigma_{22} & \dots & \sigma_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ \sigma_{n1} & \sigma_{n2} & \dots & \sigma_{nn}\end{pmatrix} \begin{pmatrix}\omega_1 \\ \omega_2 \\ \vdots \\ \omega_n\end{pmatrix} - \lambda \begin{pmatrix}\mu_1 & \mu_2 & \dots & \mu_n\end{pmatrix} \begin{pmatrix}\omega_1 \\ \omega_2 \\ \vdots \\ \omega_n\end{pmatrix}}
$$
$$\mathcal{L}(\vec{x}) = \frac{\vec{x}^T}{k}\Sigma \frac{\vec{x}^T}{k} - \lambda \left(\mu^T\frac{\vec{x}}{k}\right)$$

$$
\boxed{\mathcal{L(\vec{x})} = \frac{1}{k^2}\begin{pmatrix} x_1 & x_2 & \dots & x_n\end{pmatrix} \begin{pmatrix}\sigma_{11} & \sigma_{12} & \dots & \sigma_{1n} \\ \sigma_{21} & \sigma_{22} & \dots & \sigma_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ \sigma_{n1} & \sigma_{n2} & \dots & \sigma_{nn}\end{pmatrix} \begin{pmatrix}x_1 \\ x_2 \\ \vdots \\ x_n\end{pmatrix} - \frac{\lambda}{k} \begin{pmatrix}\mu_1 & \mu_2 & \dots & \mu_n\end{pmatrix} \begin{pmatrix}x_1 \\ x_2 \\ \vdots \\ x_n\end{pmatrix}}
$$
minimasi ke maksimasi
$$\begin{split}
U(\vec{x}) &= -\frac{1}{\lambda} \mathcal{L}(\vec{x}) \\
&= ... \\
&= \left(\sum_{i=1}^N \mu_i \frac{x_i}{k}\right) - \frac{1}{\lambda}\left(\sum_{i=1}^N\sum_{j=1}^N \sigma_{ij} x_i x_j\right)
\end{split}$$

$$
\boxed{U(\vec{x}) =  \frac{1}{k} \begin{pmatrix} \mu_1 & \mu_2 & \dots & \mu_n \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix} - \frac{1}{\lambda k^2} \begin{pmatrix} x_1 & x_2 & \dots & x_n \end{pmatrix} \begin{pmatrix} \sigma_{11} & \sigma_{12} & \dots & \sigma_{1n} \\ \sigma_{21} & \sigma_{22} & \dots & \sigma_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ \sigma_{n1} & \sigma_{n2} & \dots & \sigma_{nn} \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix}}
$$ 

risk tolerance berbanding terbalik dengan risk aversion $\frac{1}{\lambda} \propto \frac{\gamma}{2}$ 
$$
U(\vec{x}) = \left(\sum_{i=1}^N \mu_i \frac{x_i}{k}\right) - \frac{\gamma}{2}\left(\sum_{i=1}^N\sum_{j=1}^N \sigma_{ij} x_i x_j\right)
$$

$$
\boxed{U(\vec{x}) =  \frac{1}{k} \begin{pmatrix} \mu_1 & \mu_2 & \dots & \mu_n \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix} - \frac{\gamma}{2k^2} \begin{pmatrix} x_1 & x_2 & \dots & x_n \end{pmatrix} \begin{pmatrix} \sigma_{11} & \sigma_{12} & \dots & \sigma_{1n} \\ \sigma_{21} & \sigma_{22} & \dots & \sigma_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ \sigma_{n1} & \sigma_{n2} & \dots & \sigma_{nn} \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix}}
$$ 

fungsi potensial pada EPG