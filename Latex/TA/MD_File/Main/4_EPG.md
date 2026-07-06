# Formulasi *Equality Penalty Gradient* (EPG)

## 1. Pendekatan *Penalty Method* dalam Optimasi Terkendala
Dalam masalah optimasi Markowitz, terdapat kendala utama bahwa total bobot aset dalam portofolio harus sama dengan satu, yakni $\sum w_i = 1$. Untuk menyelesaikan masalah ini secara numerik tanpa menggunakan *Lagrange Multiplier* yang kompleks, kita dapat menggunakan pendekatan *Penalty Method*. Metode ini bekerja dengan cara menambahkan suku penalti ke dalam fungsi biaya (*cost function*) asli, yang akan memberikan nilai besar jika kendala tersebut dilanggar.

Fungsi biaya yang telah dimodifikasi dengan suku penalti didefinisikan sebagai:
$$\begin{equation}
L(\mathbf{w}, \lambda) = f(\mathbf{w}) + \frac{\lambda}{2} \left( \sum_{i=1}^n w_i - 1 \right)^2
\end{equation}$$
di mana $f(\mathbf{w}) = \frac{1}{2} \mathbf{w}^T \Sigma \mathbf{w} - q \mathbf{w}^T \mathbf{\mu}$ adalah fungsi biaya Markowitz asli, dan $\lambda$ adalah parameter penalti. Jika $\lambda$ bernilai sangat besar, maka algoritma optimasi akan dipaksa untuk mencari nilai $\mathbf{w}$ yang membuat $\sum w_i \approx 1$ guna meminimalkan nilai $L$.

## 2. Derivasi Gradien untuk *Equality Penalty*
Untuk mengupdate bobot menggunakan algoritma berbasis gradien seperti *Gradient Descent*, kita perlu menurunkan fungsi biaya $L$ terhadap setiap komponen bobot $w_k$. Gradien total terdiri dari gradien fungsi asli dan gradien dari suku penalti:
$$\begin{equation}
\nabla L(\mathbf{w}, \lambda) = \nabla f(\mathbf{w}) + \nabla \text{Penalty}
\end{equation}$$

Penurunan suku penalti terhadap $w_k$ dilakukan sebagai berikut:
$$\begin{split}
\frac{\partial}{\partial w_k} \left[ \frac{\lambda}{2} \left( \sum_{i=1}^n w_i - 1 \right)^2 \right] &= \lambda \left( \sum_{i=1}^n w_i - 1 \right) \cdot \frac{\partial}{\partial w_k} \left( \sum_{i=1}^n w_i - 1 \right) \\
&= \lambda \left( \sum_{i=1}^n w_i - 1 \right) \cdot 1
\end{split}$$
Sehingga, gradien total untuk setiap elemen $w_k$ adalah:
$$\begin{equation}
\frac{\partial L}{\partial w_k} = \left( \sum_{j=1}^n \sigma_{kj} w_j - q \mu_k \right) + \lambda \left( \sum_{i=1}^n w_i - 1 \right)
\end{equation}$$

## 3. Implementasi Numerik dan Dinamika Parameter
Dalam implementasi praktis, parameter penalti $\lambda$ sering kali ditingkatkan secara bertahap selama proses iterasi untuk memastikan konvergensi yang stabil. Jika $\lambda$ terlalu kecil di awal, kendala mungkin tidak terpenuhi dengan presisi tinggi; sebaliknya, jika $\lambda$ terlalu besar secara instan, permukaan fungsi biaya menjadi sangat curam sehingga menyebabkan ketidakstabilan numerik (*oscillation*).

Penggunaan *Equality Penalty Gradient* (EPG) memungkinkan kita untuk mengubah masalah optimasi terkendala (*constrained optimization*) menjadi masalah optimasi tanpa kendala (*unconstrained optimization*). Hal ini sangat menguntungkan saat kita menggunakan algoritma kuantum seperti VQE (*Variational Quantum Eigensolver*) atau optimasi stokastik seperti SPSA, di mana penanganan kendala secara eksplisit sering kali sulit dilakukan pada tingkat sirkuit kuantum.

## 4. Analisis Konvergensi
Efektivitas dari metode EPG dapat diukur melalui *residual error* dari kendala, yaitu $\epsilon = |1 - \sum w_i|$. Selama proses optimasi, gradien penalti akan terus mendorong vektor bobot menuju bidang hiper (*hyperplane*) $\sum w_i = 1$. Pada titik optimal, gradien dari fungsi tujuan dan gradien dari suku penalti akan saling meniadakan dalam arah yang tegak lurus terhadap permukaan kendala.

Hasil akhir dari pendekatan ini adalah vektor bobot $\mathbf{w}^*$ yang tidak hanya meminimalkan risiko portofolio untuk tingkat imbal hasil tertentu, tetapi juga secara otomatis memenuhi batasan anggaran investasi. Integrasi antara formulasi Markowitz dan teknik EPG ini membentuk kerangka kerja yang kuat untuk analisis portofolio modern yang efisien dan adaptif terhadap berbagai jenis arsitektur komputasi.

## 5. Penuruna rumus
$$\Phi(\vec{x}) = \sum_{l=1}^N \mu_l \frac{x_l}{k} - \frac{\gamma}{2}\sum_{i=1}^N\sum_{j=1}^N \sigma_{ij} \frac{x_i}{k} \frac{x_j}{k}$$
suku 1:
$$\sum_{l=1}^N \mu_l \frac{x_l}{k} = \mu_i \frac{x_i}{k} + \sum_{l=1}^N \mu_l \frac{x_l}{k}$$
suku 2:
$$\sum_{i=1}^N\sum_{j=1}^N \sigma_{ij} \frac{x_i}{k} \frac{x_j}{k} = \sigma_i^2 \frac{x_i^2}{k^2} + \sum_{j\ne i}\sigma_{ij} \frac{x_ix_j}{k^2} + \sum_{l\ne i} \sigma_{li} \frac{x_l x_i}{k^2} + \sum_{l\ne i}\sum_{j\ne i} \sigma_{kj}\frac{x_k x_k}{k^2}$$

indeks l tidak dimasukkan karena tidak dimasukkan ke dalam persamaan sehingga 
$$\begin{split}
\Phi(\vec{x}) &= \sum_{l=1}^N \mu_l \frac{x_l}{k} - \frac{\gamma}{2}\sum_{i=1}^N\sum_{j=1}^N \sigma_{ij} \frac{x_i x_j}{k^2} \\
&= \mu_i \frac{x_i}{k} + \frac{\gamma}{2}\left(\sigma_i^2 \frac{x_i^2}{k^2} + \sum_{j\ne i}\sigma_{ij} \frac{x_ix_j}{k^2} + \sum_{l\ne i} \sigma_{li} \frac{x_l x_i}{k^2} \right) \\
&= \mu_i \frac{x_i}{k} + \frac{\gamma}{2}\left(\sigma_i^2 \frac{x_i^2}{k^2} + 2\sum_{j\lt i}\sigma_{ij}\frac{x_ix_j}{k^2} \right) \\
&= \mu_i \frac{x_i}{k} + \frac{\gamma}{2}\sigma_i^2 \frac{x_i^2}{k^2} + \gamma \sum_{j\lt i}\sigma_{ij}\frac{x_ix_j}{k^2}
\end{split}$$
karena $x_i^2 = x_i$, maka
$$\begin{split}
\Phi(\vec{x}) &= \mu_i \frac{x_i}{k} + \frac{\gamma}{2}\sigma_i^2 \frac{x_i}{k^2} + \gamma \sum_{j\lt i}\sigma_{ij}\frac{x_ix_j}{k^2} \\
&= x_i\left(\frac{\mu_i }{k} + \frac{\gamma}{2}\frac{\sigma_i^2}{k^2} + \gamma \sum_{j\lt i}\sigma_{ij}\frac{x_j}{k^2} \right)
\end{split}$$
sehingga
$$
\Delta \Phi(\vec{x}) = \Phi(x_i, \vec{x}_{-i}) - \Phi(x_i^{\prime}, \vec{x}_{-i}) 
$$
sehingga nash equilibrium akan didapat jika dan hana jika tidak ada satupun aseet yang memiliki $\Delta u_i \gt 0$   
$$\begin{split}
\Delta \Phi(\vec{x}) &= \Phi(1, \vec{x}_{-i}) - \Phi(0, \vec{x}_{-i}) \\
&= \frac{\mu_i }{k} + \frac{\gamma}{2}\frac{\sigma_i^2}{k^2} + \gamma \sum_{j\lt i}\sigma_{ij}\frac{x_j}{k^2}
\end{split}$$

dengan deviasi menjadi $i'$
$$
\Delta u_i = (1-2x_i)M_i
$$
# Contoh perhitungan
misal $\gamma=1 , \quad \mu_1=12, \quad \mu_2=11, \quad \mu_3=8, \quad \sigma_11=10, \quad \sigma_22=10, \quad \sigma_33=10, \quad \sigma_12=\sigma_21=8, \quad \sigma_13=\sigma_31=2, \quad \sigma_23=\sigma_32=-2$, maka 
$$
\begin{split}
\text{aset 1:} \quad M_1 &= 12 - \frac{1}{2}(10) - (8x_2 + 2x_3) = 7 - 8x_2 - 2x_3 \\
\text{aset 3:} \quad M_2 &= 11 - \frac{1}{2}(10) - (8x_1 - 2x_3) = 6 - 8x_2 + 2x_3 \\
\text{aset 3:} \quad M_3 &= 8 - \frac{1}{2}(10) - (2x_1 - 2x_2) = 3 - 2x_1 + 2x_2 \\
\end{split}
$$
maka pada iterasi 0: $\vec{x} = (0,0,0)$ 
$$
\begin{split}
M_1 &= 7 - 0 - 0 = 7 \\
M_2 &= 6 - 0 - 0 = 6 \\
M_3 &= 3 - 0 + 0 = 3 \\
\end{split}
$$
karena 7 adalah angka paling tinggi, maka ubah keputusannya menjadi 1. sehingga pada iterasi 1: $\vec{x}=(1,0,0)$
$$
\begin{split}
M_1 &= 7 - 0 - 0 = 7  \to \Delta\mu_1 = -7\\
M_2 &= 6 - 8 - 0 = -2 \\
M_3 &= 3 - 2 + 0 = 1 \\
\end{split}
$$
iterasi tersebut menunjukkan aset 1 akan rugi jika dijual (tahan strategi), aset 2 akan rugi jika dibeli (tahan strategi), dan aset 3 akan untuk jika dibeli (maka ganti strategi). sehingga iterasi 3 menjadi $\vec{x} = (1,0,1)$
$$
\begin{split}
M_1 &= 7 - 0 - 2 = 5  \to \Delta\mu_1 = -5\\
M_2 &= 6 - 8 + 2 = 0 \\
M_3 &= 3 - 2 + 0 = 1  \to \Delta\mu_3 = -1\\
\end{split}
$$
iterasi terakhir ini menunjukkan nash equilibrium karena tidak ada deviasi yang lebih dari 0.
