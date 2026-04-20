# Algoritma *Simultaneous Perturbation Stochastic Approximation* (SPSA)

## 1. Pendekatan Optimasi Bebas Gradien (*Gradient-Free*)
Dalam optimasi portofolio menggunakan komputer kuantum, salah satu tantangan utama adalah adanya *noise* hasil pengukuran (*shot noise*) yang menyebabkan permukaan fungsi biaya menjadi tidak mulus. Algoritma *Gradient Descent* standar sering kali gagal dalam kondisi ini karena memerlukan perhitungan turunan parsial yang presisi. Sebagai solusinya, digunakan algoritma *Simultaneous Perturbation Stochastic Approximation* (SPSA). SPSA adalah algoritma optimasi stokastik yang tidak memerlukan informasi gradien analitik, melainkan melakukan estimasi gradien berdasarkan dua evaluasi fungsi biaya pada setiap iterasi.

Keunggulan utama SPSA dibandingkan metode *finite difference* konvensional adalah efisiensi komputasinya. Jika masalah optimasi melibatkan $p$ variabel, metode *finite difference* membutuhkan $2p$ evaluasi fungsi untuk mengestimasi gradien. Sebaliknya, SPSA hanya membutuhkan 2 evaluasi fungsi tanpa memedulikan besarnya dimensi $p$. Hal ini membuat SPSA menjadi pilihan utama dalam algoritma hibrida klasik-kuantum seperti VQE (*Variational Quantum Eigensolver*), di mana evaluasi sirkuit kuantum merupakan proses yang memakan waktu dan sumber daya.

## 2. Estimasi Gradien Stokastik
Inti dari SPSA adalah teknik perturbasi simultan, di mana seluruh komponen vektor parameter $\theta$ diubah secara bersamaan melalui vektor acak $\Delta$. Estimasi gradien pada iterasi ke-$k$, dilambangkan sebagai $\hat{g}_k(\theta_k)$, dihitung melalui rumus berikut:
$$\begin{equation}
\hat{g}_k(\theta_k) = \frac{y(\theta_k + c_k \Delta_k) - y(\theta_k - c_k \Delta_k)}{2 c_k \Delta_k}
\end{equation}$$
di mana $y(\cdot)$ adalah nilai fungsi biaya yang terukur (mungkin mengandung noise), $c_k$ adalah skala perturbasi, dan $\Delta_k$ adalah vektor acak yang biasanya mengikuti distribusi Bernoulli ($\pm 1$).

Untuk setiap elemen ke-$i$ dari vektor gradien, formulasinya adalah:
$$\begin{equation}
\hat{g}_{ki}(\theta_k) = \frac{y(\theta_k + c_k \Delta_k) - y(\theta_k - c_k \Delta_k)}{2 c_k \Delta_{ki}}
\end{equation}$$
Karena pembilang pada persamaan (2) sama untuk seluruh komponen $i=1, 2, \dots, p$, maka efisiensi komputasi yang tinggi dapat tercapai. Secara teoretis, dalam kondisi *noise* yang bersifat *zero-mean*, estimasi gradien stokastik ini akan konvergen ke gradien asli seiring dengan bertambahnya jumlah iterasi.

## 3. Aturan Pembaruan dan Barisan *Gain*
SPSA memperbarui vektor parameter menggunakan aturan yang serupa dengan *Gradient Descent*, namun dengan menggunakan estimasi gradien stokastik dan barisan langkah yang meluruh (*decaying step sizes*). Aturan pembaruan parameternya adalah:
$$\begin{equation}
\theta_{k+1} = \theta_k - a_k \hat{g}_k(\theta_k)
\end{equation}$$
Keberhasilan konvergensi SPSA sangat bergantung pada pemilihan barisan *gain* $a_k$ (untuk langkah pembaruan) dan $c_k$ (untuk skala perturbasi). Barisan ini didefinisikan sebagai berikut:
$$\begin{equation}
a_k = \frac{a}{(k + 1 + A)^\alpha}, \quad c_k = \frac{c}{(k + 1)^\gamma}
\end{equation}$$

Parameter $a, c, A, \alpha,$ dan $\gamma$ adalah konstanta non-negatif yang menentukan dinamika optimasi:
- $A$ adalah konstanta stabilitas yang mencegah langkah terlalu besar pada iterasi awal.
- $\alpha$ dan $\gamma$ mengontrol kecepatan peluruhan; nilai standar yang sering digunakan adalah $\alpha = 0.602$ dan $\gamma = 0.101$ untuk memastikan konvergensi asimtotik yang optimal.
- $a$ dan $c$ dipilih berdasarkan magnitudo fungsi biaya dan sensitivitas parameter terhadap perubahan energi.

## 4. Relevansi dalam Optimasi Portofolio Kuantum
Dalam konteks riset ini, SPSA digunakan sebagai *classical optimizer* untuk melatih parameter sirkuit ansatz pada VQE. Ketika kita mencoba meminimalkan fungsi biaya Markowitz melalui representasi Hamiltonian, SPSA mampu menavigasi *loss landscape* yang kasar akibat keterbatasan jumlah *shots* pada perangkat kuantum. Sifat SPSA yang toleran terhadap noise memastikan bahwa proses pembaruan bobot portofolio tetap stabil meskipun data input memiliki variabilitas statistik yang tinggi.

Selain itu, karena SPSA hanya membutuhkan dua pengukuran energi per iterasi, ia secara drastis mengurangi total waktu eksekusi pada simulator maupun *Quantum Processing Unit* (QPU) nyata. Hal ini memungkinkan simulasi portofolio dengan jumlah aset yang lebih banyak tanpa terkendala oleh biaya komputasi yang membengkak secara linear terhadap jumlah aset. Dengan demikian, integrasi SPSA dalam kerangka kerja optimasi portofolio kuantum memberikan keseimbangan yang ideal antara akurasi hasil dan efisiensi operasional.

## 5. Penurunan Rumus

memanfaatkan distribusi bernoulli yang memiliki himpunan -1 dan 1 ke dalam persamaan parameter shift rule:
$$
\vec{\Delta}_k=(\vec{\Delta}_{k,1}, \vec{\Delta}_{k,2}, \dots, \vec{\Delta}_{k,D})^T
$$

dengan evaluasi maju
$$E_+=E(\theta_k + c_k \vec{\Delta}_k) \approx E(\theta_k) + c_k \sum_{j=1}^D \vec{\Delta}_j \frac{\partial E}{\partial \theta_j} + \frac{1}{2} c_k^2 \sum_{j=1}^D \vec{\Delta}_j^2 \frac{\partial^2 E}{\partial \theta_j^2} + \dots$$

dan evaluasi mundur
$$
E_-=E(\theta_k - c_k \vec{\Delta}_k) \approx E(\theta_k) - c_k \sum_{j=1}^D \vec{\Delta}_j \frac{\partial E}{\partial \theta_j} + \frac{1}{2} c_k^2 \sum_{j=1}^D \vec{\Delta}_j^2 \frac{\partial^2 E}{\partial \theta_j^2} - \dots$$

sehingga didapatkan:
$$
E_+ - E_-= 2 c_k \sum_{j=1}^D \vec{\Delta}_j \frac{\partial E}{\partial \theta_j} + O(c_k^3)
$$

dan dengan estimator sebagai rumus tebakan ($\hat{g}$):
$$
\begin{align}
\hat{g}_i &= \frac{E_+ - E_-}{2 c_i \vec{\Delta}_i}\\
&= \frac{2c_i\sum_{j=1}^D \vec{\Delta}_j \frac{\partial E}{\partial \theta_j}}{2 c_i\vec{\Delta}_i} \\
&= \frac{1}{\vec{\Delta}_i} \sum_{j=1}^D \vec{\Delta}_j \frac{\partial E}{\partial \theta_j} \\
&= \frac{\Delta_i}{\Delta_i} \frac{\partial E}{\partial \theta_i} + \sum_{i\ne j} \frac{\Delta_j}{\Delta_i} \frac{\partial E}{\partial \theta_j} \\
&= \frac{\partial E}{\partial \theta_i} + \sum_{i\ne j} \frac{\Delta_j}{\Delta_i} \frac{\partial E}{\partial \theta_j}\\
\end{align}
$$

karena distribusi bernouli $\in \{-1,1\}$ maka $E\left[\frac{\Delta_j}{\Delta_i}\right] = 0$ untuk $i \ne j$ dan $E\left[\frac{\Delta_i}{\Delta_i}\right] = 1$ sehingga:
$$
\begin{align}
E[\hat{g}_i] &= E\left[\frac{\partial E}{\partial \theta_i} + \sum_{i\ne j} \frac{\Delta_j}{\Delta_i} \frac{\partial E}{\partial \theta_j}\right] \\
&= \frac{\partial E}{\partial \theta_i} + \sum_{i\ne j} E\left[\frac{\Delta_j}{\Delta_i}\right] \frac{\partial E}{\partial \theta_j} \\
&= \frac{\partial E}{\partial \theta_i}
\end{align}
$$

Sehingga didapatkan:
$$
\begin{align}
\theta_{k+1} &= \theta_k - a_k \hat{g}_k(\theta_k) \\
&= \theta_k - a_k \frac{\partial E}{\partial \theta_k}
\end{align}
$$

Ini menunjukkan bahwa SPSA adalah algoritma *Gradient Descent* yang menggunakan estimasi gradien stokastik.