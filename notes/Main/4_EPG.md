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
