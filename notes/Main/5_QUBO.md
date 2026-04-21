# Formulasi *Quadratic Unconstrained Binary Optimization* (QUBO)

## 1. Pendekatan Diskritisasi dalam Optimasi Kuantum
Dalam arsitektur komputasi kuantum tertentu, seperti *Quantum Annealing* (QA) atau algoritma *Quantum Approximate Optimization Algorithm* (QAOA), masalah optimasi harus direpresentasikan dalam bentuk variabel biner. Transformasi dari variabel kontinu (bobot portofolio $w_i$) menjadi variabel diskrit atau biner merupakan langkah krusial. Format yang paling umum digunakan adalah QUBO (*Quadratic Unconstrained Binary Optimization*), di mana fungsi tujuan dinyatakan sebagai bentuk kuadratik dari variabel biner $x_i \in \{0, 1\}$.

Untuk merepresentasikan bobot kontinu $w_i \in [0, 1]$ ke dalam bentuk biner, kita menggunakan skema ekspansi biner dengan presisi $K$:
$$\begin{equation}
w_i = \sum_{k=1}^K 2^{-k} x_{i,k}
\end{equation}$$
di mana $x_{i,k}$ adalah variabel biner yang merepresentasikan bit ke-$k$ dari aset ke-$i$. Dengan menggunakan diskritisasi ini, masalah optimasi portofolio yang tadinya kontinu kini dapat dipetakan ke dalam ruang pencarian diskrit yang sesuai dengan kapabilitas perangkat keras kuantum.

## 2. Formulasi Fungsi Energi QUBO
Fungsi biaya Markowitz yang telah dimodifikasi (termasuk suku penalti kendala) harus disusun ulang ke dalam bentuk matriks QUBO. Secara umum, fungsi energi QUBO didefinisikan sebagai:
$$\begin{equation}
H(\mathbf{x}) = \sum_{i} Q_{ii} x_i + \sum_{i < j} Q_{ij} x_i x_j = \mathbf{x}^T \mathbf{Q} \mathbf{x}
\end{equation}$$
Dalam konteks portofolio, fungsi tujuan mencakup tiga komponen utama: minimisasi varians, maksimisasi imbal hasil, dan penalti pelanggaran kendala anggaran. Substitusi persamaan (1) ke dalam fungsi biaya Markowitz menghasilkan suku-suku linear dan kuadratik terhadap variabel biner $x_{i,k}$.

Matriks $\mathbf{Q}$ dibangun dengan menggabungkan koefisien-koefisien dari interaksi antar qubit. Suku diagonal $Q_{ii}$ merepresentasikan bias atau energi individual qubit, sedangkan suku non-diagonal $Q_{ij}$ merepresentasikan kekuatan kopling (*coupling strength*) antar qubit. Dalam sistem fisik kuantum, representasi ini setara dengan model Ising melalui transformasi variabel $x_i = (1 - z_i)/2$ di mana $z_i \in \{1, -1\}$.

## 3. Penanganan Kendala dalam Format QUBO
Salah satu tantangan dalam QUBO adalah memastikan bahwa solusi biner yang dihasilkan tetap mematuhi kendala $\sum w_i = 1$. Kendala ini diintegrasikan ke dalam fungsi energi menggunakan suku penalti kuadratik yang serupa dengan metode EPG:
$$\begin{equation}
P(\mathbf{x}) = \lambda \left( \sum_{i=1}^n \sum_{k=1}^K 2^{-k} x_{i,k} - 1 \right)^2
\end{equation}$$
Ketika persamaan (3) diekspansi, ia akan menghasilkan suku-suku linear $\propto x_{i,k}$ dan suku-suku kuadratik $\propto x_{i,k}x_{j,l}$. Suku-suku inilah yang kemudian ditambahkan ke dalam matriks $\mathbf{Q}$ utama. Nilai parameter penalti $\lambda$ harus dipilih secara hati-hati; jika terlalu kecil, solusi optimal mungkin tidak memenuhi kendala, namun jika terlalu besar, ia dapat menutupi struktur energi dari fungsi tujuan asli (varians dan imbal hasil).

## 4. Keunggulan dan Limitasi Representasi QUBO
Representasi QUBO memungkinkan masalah optimasi portofolio diselesaikan menggunakan algoritma hibrida klasik-kuantum. Dengan memetakan masalah ke dalam Hamiltonian sistem kuantum, kita dapat memanfaatkan fenomena *quantum tunneling* untuk melewati barier energi lokal dan menemukan solusi optimal global pada permukaan fungsi biaya yang kompleks.

Namun, terdapat limitasi pada jumlah qubit yang tersedia pada perangkat keras saat ini. Penggunaan presisi $K$ yang tinggi untuk meningkatkan akurasi bobot $w_i$ akan meningkatkan jumlah variabel biner secara eksponensial ($n \times K$ qubit). Oleh karena itu, pemilihan tingkat diskritisasi harus menyeimbangkan antara resolusi bobot yang diinginkan dan sumber daya komputasi kuantum yang tersedia. Integrasi QUBO ini menjadi jembatan utama antara teori keuangan klasik dan implementasi pada era *Noisy Intermediate-Scale Quantum* (NISQ).

## 5. penurunan rumus
dari maksimasi kembali ke minimasi karena agen cenderung mencari payoff tinggi, sedangkan ising mencari energi terendah
$$E(\vec{x}) = \Phi(\vec{x})$$
sehingga
$$\begin{split}
E(\vec{x}) &= \frac{\gamma}{2}\sum_{i=1}^N\sum_{j=1}^N \sigma_{ij} \frac{x_i x_j}{k^2} -\sum_{i=1}^N \mu_i \frac{x_i}{k} \\
&= \frac{\gamma}{2}\left(\sum_{i=1}^N\sigma_i^2 \frac{x_i^2}{k^2} + \sum_{i\ne j}\sigma_{ij} \frac{x_ix_j}{k^2}\right) -\sum_{i=1}^N \mu_i \frac{x_i}{k} \\
&= \frac{\gamma}{2}\sum_{i=1}^N\sigma_i^2 \frac{x_i^2}{k^2} + \frac{\gamma}{2}\sum_{i\ne j}\sigma_{ij} \frac{x_ix_j}{k^2} - \sum_{i=1}^N \mu_i \frac{x_i}{k}
\end{split}$$

$$
\boxed{E(\vec{x}) = \frac{\gamma}{2k^2}\begin{pmatrix} x_1 & x_2 & \dots & x_n\end{pmatrix} \begin{pmatrix}\sigma_{11} & 0 & \dots & 0 \\ 0 & \sigma_{22} & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \dots & \sigma_{nn} \end{pmatrix} \begin{pmatrix}x_1 \\ x_2 \\ \vdots \\ x_n\end{pmatrix} + \frac{\gamma}{2k^2}\begin{pmatrix} x_1 & x_2 & \dots & x_n\end{pmatrix} \begin{pmatrix}0 & \sigma_{12} & \dots & \sigma_{1n} \\ \sigma_{21} & 0 & \dots & \sigma_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ \sigma_{n1} & \sigma_{n2} & \dots & 0 \end{pmatrix} \begin{pmatrix}x_1 \\ x_2 \\ \vdots \\ x_n\end{pmatrix} - \frac{1}{k}\begin{pmatrix} \mu_1 & \mu_2 & \dots & \mu_n\end{pmatrix} \begin{pmatrix}x_1 \\ x_2 \\ \vdots \\ x_n\end{pmatrix}}
$$

masukkan aplikasi penalti agar sistem meloloskan $\sum_i^N x_i=k$ dan memberi penalti untuk jumlahan yang tidak mengikuti aturan
$$\begin{split}
P(\vec{x}) &= A\left( \sum_i^N x_i-k \right) \\ 
P(\vec{x}) &= A \sum_i^N x_i-Ak \\
\end{split}$$
$$
\boxed{P(\vec{x}) = \begin{pmatrix} x_1 & x_2 & \dots & x_n\end{pmatrix} \begin{pmatrix}A \\ A \\ \vdots \\ A \end{pmatrix} - Ak}
$$

sehingga
$$\begin{split}
E_{total}(\vec{x}) &= E(\vec{x}) + P(\vec{x})\\
&= \frac{\gamma}{2}\sum_{i=1}^N\sigma_i^2 \frac{x_i^2}{k^2} + \frac{\gamma}{2}\sum_{i\ne j}\sigma_{ij} \frac{x_ix_j}{k^2} - \sum_{i=1}^N \mu_i \frac{x_i}{k} + A \sum_i^N x_i-Ak \\
&= \dots \\
&= \sum_{i=1}^N \left(\frac{\gamma\sigma_i^2}{2k^2}-\frac{\mu_i}{k}+A\right)x_i + \sum_{i\ne j}\left(\frac{\gamma \sigma_{ij}}{2k^2} \right) x_ix_j -Ak \\
\end{split}$$

$$
\boxed{
\begin{split}
E_{total}(\vec{x}) =& \left[ \frac{\gamma}{2k^2}\begin{pmatrix} x_1 & x_2 & \dots & x_n\end{pmatrix} \begin{pmatrix}\sigma_{11} & 0 & \dots & 0 \\ 0 & \sigma_{22} & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \dots & \sigma_{nn} \end{pmatrix}  -\frac{1}{k} \begin{pmatrix} \mu_1 & \mu_2 & \dots & \mu_n \end{pmatrix} + A \right] \begin{pmatrix}x_1 \\ x_2 \\ \vdots \\ x_n\end{pmatrix} \\
&+ \begin{pmatrix} x_1 & x_2 & \dots & x_n \end{pmatrix} \left[ \frac{\gamma}{2k^2}\begin{pmatrix} 0 & \sigma_{12} & \dots & \sigma_{1n} \\ \sigma_{21} & 0 & \dots & \sigma_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ \sigma_{n1} & \sigma_{n2} & \dots & 0 \end{pmatrix}  \right] \begin{pmatrix}x_1 \\ x_2 \\ \vdots \\ x_n\end{pmatrix} \\
&-Ak
\end{split}
}$$

dengan melakukan transformasi affine $x_i = \frac{s_i+1}{2}$ ; 
$$\begin{split}
E_{total}(\vec{x}) &= \sum_{i=1}^N \left(\frac{\gamma \sigma_i^2}{2k^2}-\frac{\mu_i}{k}+A\right)\left(\frac{s_i+1}{2}\right) + \sum_{i\ne j}\left(\frac{\gamma \sigma_{ij}}{2k^2} \right) \left(\frac{s_i+1}{2}\right)\left(\frac{s_j+1}{2}\right) -Ak \\
&= \sum_{i=1}^N \left(\frac{\gamma \sigma_i^2}{4k^2}-\frac{\mu_i}{2k}+\frac{A}{2}\right)s_i + \sum_{i\ne j}\left(\frac{\gamma \sigma_{ij}}{8k^2} \right) \left(s_is_j + s_i + s_j + 1\right) -Ak \\
&= \sum_{i=1}^N \left(\frac{\gamma \sigma_i^2}{4k^2}-\frac{\mu_i}{2k}+\frac{A}{2}\right)s_i + \sum_{i\ne j}\left(\frac{\gamma \sigma_{ij}}{8k^2} \right)s_is_j + \sum_{i\ne j}\left(\frac{\gamma \sigma_{ij}}{8k^2} \right)s_i + \sum_{i\ne j}\left(\frac{\gamma \sigma_{ij}}{8k^2} \right)s_j + \sum_{i\ne j}\left(\frac{\gamma \sigma_{ij}}{8k^2} \right) -Ak \\
\end{split}$$

$$
\boxed{
\begin{split}
E_{total}(\vec{x}) =& \left[ \frac{\gamma}{2k^2}\begin{pmatrix} \frac{s_1+1}{2} & \frac{s_2+1}{2} & \dots & \frac{s_n+1}{2}\end{pmatrix} \begin{pmatrix}\sigma_{11} & 0 & \dots & 0 \\ 0 & \sigma_{22} & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \dots & \sigma_{nn} \end{pmatrix}  -\frac{1}{k} \begin{pmatrix} \mu_1 & \mu_2 & \dots & \mu_n \end{pmatrix} + A \right] \begin{pmatrix}\frac{s_1+1}{2} \\ \frac{s_2+1}{2} \\ \vdots \\ \frac{s_n+1}{2}\end{pmatrix} \\
&+ \begin{pmatrix} \frac{s_1+1}{2} & \frac{s_2+1}{2} & \dots & \frac{s_n+1}{2} \end{pmatrix} \left[ \frac{\gamma}{2k^2}\begin{pmatrix} 0 & \sigma_{12} & \dots & \sigma_{1n} \\ \sigma_{21} & 0 & \dots & \sigma_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ \sigma_{n1} & \sigma_{n2} & \dots & 0 \end{pmatrix}  \right] \begin{pmatrix}\frac{s_1+1}{2} \\ \frac{s_2+1}{2} \\ \vdots \\ \frac{s_n+1}{2}\end{pmatrix} \\
&-Ak \\
&= \left[\frac{\gamma}{8k^2}\begin{pmatrix} s_1+1 & s_2+1 & \dots & s_n+1\end{pmatrix} \begin{pmatrix} \sigma_{11} & 0 & \dots & 0 \\ 0 & \sigma_{22} & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \dots & \sigma_{nn} \end{pmatrix} - \frac{1}{2k} \begin{pmatrix} \mu_1 & \mu_2 & \dots \mu_n \end{pmatrix} + \frac{A}{2} \right] \begin{pmatrix} s_1+1 \\ s_2+1 \\ \vdots \\ s_n+1\end{pmatrix} \\ 
&+ \frac{\gamma}{8k^2}\begin{pmatrix} s_1+1 & s_2+1 & \dots & s_n+1\end{pmatrix} \begin{pmatrix} 0 & \sigma_{12} & \dots & \sigma_{1n} \\ \sigma_{21} & 0 & \dots & \sigma_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ \sigma_{n1} & \sigma_{n2} & \dots & 0 \end{pmatrix} \begin{pmatrix} s_1+1 \\ s_2+1 \\ \vdots \\ s_n+1\end{pmatrix} \\
&- \frac{Ak}{2}\\
&= \cdots \\
&= \left[\frac{\gamma}{4k^2} \begin{pmatrix}\sigma_{11} & 0 & \dots & 0 \\ 0 & \sigma_{22} & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \dots & \sigma_{nn}\end{pmatrix} - \frac{1}{2k} \begin{pmatrix}\mu_1 & \mu_2 & \dots & \mu_n\end{pmatrix} \right]\begin{pmatrix} s_1 \\ s_2 \\ \vdots \\ s_n\end{pmatrix} \\
&+ \frac{\gamma}{8k^2} \begin{pmatrix} s_1 & s_2 & \dots & s_n \end{pmatrix} \begin{pmatrix} 0 & \sigma_{12} & \dots & \sigma_{1n} \\ \sigma_{21} & 0 & \dots & \sigma_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ \sigma_{n1} & \sigma_{n2} & \dots & 0 \end{pmatrix} \begin{pmatrix} s_1 \\ s_2 \\ \vdots \\ s_n \end{pmatrix} \\
&+ \frac{\gamma}{8k^2} \begin{pmatrix} 0 & \sigma_{12} & \dots & \sigma_{1n} \\ \sigma_{21} & 0 & \dots & \sigma_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ \sigma_{n1} & \sigma_{n2} & \dots & 0 \end{pmatrix} \begin{pmatrix} s_1 \\ s_2 \\ \vdots \\ s_n \end{pmatrix} + \frac{\gamma}{8k^2} \begin{pmatrix} s_1 & s_2 & \dots & s_n \end{pmatrix} \begin{pmatrix} 0 & \sigma_{12} & \dots & \sigma_{1n} \\ \sigma_{21} & 0 & \dots & \sigma_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ \sigma_{n1} & \sigma_{n2} & \dots & 0 \end{pmatrix} \\
&+ \frac{\gamma}{8k^2} \begin{pmatrix} 0 & \sigma_{12} & \dots & \sigma_{1n} \\ \sigma_{21} & 0 & \dots & \sigma_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ \sigma_{n1} & \sigma_{n2} & \dots & 0 \end{pmatrix} - Ak
\end{split} 
}
$$

sehingga dapat didefinisikan
$$
h_i= \left(\frac{\gamma \sigma_i^2}{4k^2}-\frac{\mu_i}{2k}+A\right)
$$
dan
$$
J_{ij}= \frac{\gamma \sigma_{ij}}{8k^2} \quad \text{untuk } i \ne j
$$
dengan
$$
C = \sum_{i\ne j}\left(\frac{\gamma \sigma_{ij}}{8k^2} \right)s_i + \sum_{i\ne j}\left(\frac{\gamma \sigma_{ij}}{8k^2} \right)s_j + \sum_{i\ne j}\left(\frac{\gamma \sigma_{ij}}{8k^2} \right) -Ak
$$

maka model hamiltonian ising dapat dikonstruksi menjadi
$$
\hat{\mathcal{H}} = \sum_{i=1}^N h_i s_i + \sum_{i\ne j}J_{ij} s_i s_j + C
$$
atau jika dibentuk dalam bentuk pauli;
$$
\hat{\mathcal{H}} = \sum_{i=1}^N h_i \hat{Z}_i + \sum_{i\ne j}J_{ij} \hat{Z}_i \hat{Z}_j + C
$$