# Algoritma *Simultaneous Perturbation Stochastic Approximation* (SPSA)

## 1. Pendekatan Optimasi Bebas Gradien (*Gradient-Free*)
Dalam optimasi portofolio menggunakan komputer kuantum, salah satu tantangan utama adalah adanya *noise* hasil pengukuran (*shot noise*) yang menyebabkan permukaan fungsi biaya menjadi tidak mulus. Algoritma *Gradient Descent* standar sering kali gagal dalam kondisi ini karena memerlukan perhitungan turunan parsial yang presisi. Sebagai solusinya, digunakan algoritma *Simultaneous Perturbation Stochastic Approximation* (SPSA). SPSA adalah algoritma optimasi stokastik yang tidak memerlukan informasi gradien analitik, melainkan melakukan estimasi gradien berdasarkan dua evaluasi fungsi biaya pada setiap iterasi.

Keunggulan utama SPSA dibandingkan metode *finite difference* konvensional adalah efisiensi komputasinya. Jika masalah optimasi melibatkan $p$ variabel, metode *finite difference* membutuhkan $2p$ evaluasi fungsi untuk mengestimasi gradien. Sebaliknya, SPSA hanya membutuhkan 2 evaluasi fungsi tanpa memedulikan besarnya dimensi $p$. Hal ini membuat SPSA menjadi pilihan utama dalam algoritma hibrida klasik-kuantum seperti VQE (*Variational Quantum Eigensolver*), di mana evaluasi sirkuit kuantum merupakan proses yang memakan waktu dan sumber daya.

## 2. Vektor Gangguan dan Distribusi Rademacher
Inti dari SPSA adalah teknik perturbasi simultan, di mana seluruh komponen vektor parameter $\theta$ diubah secara bersamaan melalui vektor acak $\Delta_k$. Vektor acak ini wajib mengikuti **Distribusi Rademacher** (distribusi Bernoulli simetris $\pm 1$) agar estimasi gradien bersifat tidak bias.

### 2.1 Sifat Matematis Distribusi Rademacher
Vektor $\Delta_k = (\Delta_{k,1}, \Delta_{k,2}, \dots, \Delta_{k,p})^T$ harus memenuhi karakteristik berikut:
1.  **Simetri**: $\mathbb{E}[\Delta_{k,i}] = 0$, artinya peluang munculnya $+1$ dan $-1$ adalah sama (0.5).
2.  **Independensi**: Setiap komponen $\Delta_{k,i}$ bersifat saling bebas (*independent and identically distributed*).
3.  **Invers**: Karena $\Delta_{k,i} \in \{+1, -1\}$, maka berlaku $\Delta_{k,i}^{-1} = \Delta_{k,i}$.
4.  **Perkalian Silang**: $\mathbb{E}[\Delta_{k,i} \Delta_{k,j}] = \delta_{ij}$, di mana nilainya 1 jika $i=j$ dan 0 jika $i \neq j$.

## 3. Estimasi Gradien Stokastik
Estimasi gradien pada iterasi ke-$k$, dilambangkan sebagai $\hat{g}_k(\theta_k)$, dihitung melalui rumus berikut:
$$\begin{equation}
\hat{g}_k(\theta_k) = \frac{y(\theta_k + c_k \Delta_k) - y(\theta_k - c_k \Delta_k)}{2 c_k} \Delta_k^{-1}
\end{equation}$$
di mana $y(\cdot)$ adalah nilai fungsi biaya (energi) yang terukur, $c_k$ adalah skala perturbasi, dan $\Delta_k$ adalah vektor Rademacher.

Untuk setiap elemen ke-$i$ dari vektor gradien, karena $\Delta_{ki}^{-1} = \Delta_{ki}$, formulasinya menjadi:
$$\begin{equation}
\hat{g}_{ki}(\theta_k) = \frac{y(\theta_k + c_k \Delta_k) - y(\theta_k - c_k \Delta_k)}{2 c_k \Delta_{ki}}
\end{equation}$$
Karena pembilang pada persamaan (2) sama untuk seluruh komponen $i=1, 2, \dots, p$, maka efisiensi komputasi yang tinggi dapat tercapai.

## 4. Aturan Pembaruan dan Barisan *Gain*
SPSA memperbarui vektor parameter menggunakan aturan yang serupa dengan *Gradient Descent*, namun dengan menggunakan estimasi gradien stokastik dan barisan langkah yang meluruh (*decaying step sizes*). Aturan pembaruan parameternya adalah:
$$\begin{equation}
\theta_{k+1} = \theta_k - a_k \hat{g}_k(\theta_k)
\end{equation}$$
Keberhasilan konvergensi SPSA sangat bergantung pada pemilihan barisan *gain* $a_k$ (untuk langkah pembaruan) dan $c_k$ (untuk skala perturbasi):
$$\begin{equation}
a_k = \frac{a}{(k + 1 + A)^\alpha}, \quad c_k = \frac{c}{(k + 1)^\gamma}
\end{equation}$$
Parameter standar yang sering digunakan adalah $\alpha = 0.602$ dan $\gamma = 0.101$ untuk memastikan konvergensi asimtotik yang optimal.

## 5. Penurunan Rumus Matematis
Penurunan ini membuktikan bahwa SPSA adalah estimator tak bias dari gradien sesungguhnya. Misalkan kita melakukan ekspansi Taylor pada evaluasi maju ($E_+$) dan mundur ($E_-$):

$$E_+ = E(\theta_k + c_k \Delta_k) \approx E(\theta_k) + c_k \sum_{j=1}^p \Delta_j \frac{\partial E}{\partial \theta_j} + \frac{1}{2} c_k^2 \sum_{j=1}^p \Delta_j^2 \frac{\partial^2 E}{\partial \theta_j^2} + \dots$$
$$E_- = E(\theta_k - c_k \Delta_k) \approx E(\theta_k) - c_k \sum_{j=1}^p \Delta_j \frac{\partial E}{\partial \theta_j} + \frac{1}{2} c_k^2 \sum_{j=1}^p \Delta_j^2 \frac{\partial^2 E}{\partial \theta_j^2} - \dots$$

Selisih kedua evaluasi tersebut menghilangkan suku orde genap:
$$E_+ - E_- = 2 c_k \sum_{j=1}^p \Delta_j \frac{\partial E}{\partial \theta_j} + O(c_k^3)$$

Substitusi ke dalam rumus estimator $\hat{g}_i$:
$$\begin{align}
\hat{g}_i &= \frac{E_+ - E_-}{2 c_k \Delta_i} \approx \frac{2 c_k \sum_{j=1}^p \Delta_j \frac{\partial E}{\partial \theta_j}}{2 c_k \Delta_i} \\
&= \frac{1}{\Delta_i} \sum_{j=1}^p \Delta_j \frac{\partial E}{\partial \theta_j} = \frac{\Delta_i}{\Delta_i} \frac{\partial E}{\partial \theta_i} + \sum_{j \neq i} \frac{\Delta_j}{\Delta_i} \frac{\partial E}{\partial \theta_j}
\end{align}$$

Mengambil nilai harapan ($\mathbb{E}$) terhadap distribusi Rademacher:
$$\mathbb{E}[\hat{g}_i] = \frac{\partial E}{\partial \theta_i} + \sum_{j \neq i} \mathbb{E}\left[\frac{\Delta_j}{\Delta_i}\right] \frac{\partial E}{\partial \theta_j}$$
Karena $\mathbb{E}[\Delta_j/\Delta_i] = 0$ untuk $j \neq i$, maka didapatkan $\mathbb{E}[\hat{g}_i] = \frac{\partial E}{\partial \theta_i}$.

## 6. Contoh Numerik Implementasi
Berdasarkan visualisasi riset, misalkan kita memiliki Hamiltonian sederhana $H = 10 \hat{Z}_1 + 5 \hat{Z}_2$ dengan sirkuit ansatz $|\psi(\theta)\rangle = R_y(\theta_1)|0\rangle \otimes R_y(\theta_2)|0\rangle$.

1.  **Fungsi Energi**: $E(\theta_1, \theta_2) = 10 \cos(\theta_1) + 5 \cos(\theta_2)$.
2.  **Inisialisasi**: $\theta^{(0)} = (1.571, 1.571)$, $a_0 = 0.1, c_0 = 0.1$. Energi awal $E = 0$.
3.  **Perturbasi**: Pilih $\Delta_0 = (1, -1)^T$.
    - $\theta_+ = (1.671, 1.471) \implies E_+ = -0.499$
    - $\theta_- = (1.471, 1.671) \implies E_- = 0.499$
4.  **Estimasi Gradien**:
    - $\hat{g}_1 = \frac{-0.499 - 0.499}{2(0.1)(1)} = -4.99$
    - $\hat{g}_2 = \frac{-0.499 - 0.499}{2(0.1)(-1)} = 4.99$
5.  **Pembaruan Parameter**:
    $$\theta^{(1)} = \begin{pmatrix} 1.571 \\ 1.571 \end{pmatrix} - 0.1 \begin{pmatrix} -4.99 \\ 4.99 \end{pmatrix} = \begin{pmatrix} 2.070 \\ 1.072 \end{pmatrix}$$
6.  **Hasil**: Energi baru $E(2.070, 1.072) \approx -2.39$. Terbukti terjadi penurunan energi yang signifikan hanya dengan satu iterasi SPSA.
