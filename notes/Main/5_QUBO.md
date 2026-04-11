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
