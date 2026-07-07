# Desain *Ansatz* dalam *Variational Quantum Eigensolver* (VQE)

## 1. Pengantar *Variational Quantum Ansatz*
Dalam algoritma kuantum hibrida seperti VQE, *ansatz* didefinisikan sebagai sirkuit kuantum berparameter yang berfungsi untuk mempersiapkan *trial state* atau keadaan coba $|\psi(\boldsymbol{\theta})\rangle$. Tujuan utama dari penggunaan *ansatz* adalah untuk menjelajahi ruang Hilbert secara efisien guna menemukan keadaan dasar (*ground state*) dari Hamiltonian sistem yang merepresentasikan fungsi biaya portofolio. Pemilihan struktur *ansatz* sangat krusial karena ia menentukan jangkauan solusi yang dapat dicapai serta kompleksitas komputasi yang diperlukan dalam proses optimasi parameter klasik.

Konsep *ansatz* dalam komputasi kuantum analog dengan arsitektur jaringan saraf pada *machine learning* klasik. Sebuah *ansatz* yang baik harus memiliki kemampuan ekspresivitas yang tinggi untuk mencakup solusi optimal, namun tetap memiliki jumlah parameter yang terkendali agar tidak terjebak dalam fenomena *barren plateaus* (gradien yang hilang). Dalam konteks optimasi portofolio, *ansatz* dirancang untuk memetakan interaksi antar aset finansial ke dalam interaksi antar qubit melalui gerbang-gerbang logika kuantum yang dapat dikontrol.

## 2. Struktur Sirkuit *Hardware-Efficient*
Salah satu desain *ansatz* yang paling populer pada era *Noisy Intermediate-Scale Quantum* (NISQ) adalah *Hardware-Efficient Ansatz* (HEA). HEA dirancang dengan memanfaatkan gerbang kuantum asli (*native gates*) yang tersedia pada perangkat keras tertentu untuk meminimalkan *noise* dan kesalahan koherensi. Struktur sirkuit ini biasanya terdiri dari lapisan-lapisan gerbang rotasi satu qubit (seperti $R_y$ atau $R_z$) yang diikuti oleh lapisan gerbang *entanglement* dua qubit. Formulasi matematis dari operator unitari berparameter $U(\boldsymbol{\theta})$ pada HEA dapat dinyatakan sebagai:
$$\begin{equation}
U(\boldsymbol{\theta}) = \prod_{l=1}^L \left[ U_{ent} \cdot \left( \bigotimes_{i=1}^n R_{y}(\theta_{i,l}) \right) \right]
\end{equation}$$
di mana $L$ adalah jumlah lapisan (*depth*) dan $U_{ent}$ adalah operator tautan.

Penggunaan gerbang rotasi $R_y(\theta)$ sangat umum dalam masalah optimasi karena ia mampu memutar status qubit pada bidang nyata dalam bola Bloch, yang mempermudah interpretasi bobot portofolio. Penambahan kedalaman sirkuit $L$ akan meningkatkan fleksibilitas *ansatz* dalam merepresentasikan fungsi gelombang yang kompleks, namun juga meningkatkan risiko kesalahan sistemik akibat dekoherensi. Oleh karena itu, optimasi desain HEA memerlukan keseimbangan yang tepat antara kedalaman sirkuit dan fidelitas hasil pengukuran yang dihasilkan oleh detektor kuantum.

## 3. Peran *Entanglement* dalam Ruang Pencarian
*Entanglement* atau keterpautan kuantum merupakan fitur fundamental yang memungkinkan *ansatz* untuk menangkap korelasi non-klasik antar variabel aset. Dalam sirkuit kuantum, *entanglement* biasanya diimplementasikan menggunakan gerbang CNOT atau gerbang CZ yang menghubungkan pasangan-pasangan qubit. Dengan adanya lapisan *entanglement*, perubahan pada satu parameter rotasi dapat memengaruhi probabilitas status qubit lainnya secara kolektif. Hal ini secara langsung merepresentasikan interaksi antar aset dalam matriks kovariansi yang telah didefinisikan pada model Markowitz.

Secara matematis, status kuantum portofolio setelah melalui lapisan *entanglement* tidak dapat lagi dipisahkan menjadi produk dari status individual masing-masing qubit. Hal ini memberikan keunggulan dalam menavigasi ruang pencarian yang sangat luas dibandingkan dengan metode pengambilan sampel klasik. Strategi penyusunan gerbang *entanglement*—apakah menggunakan skema *linear entanglement*, *full entanglement*, atau *circular entanglement*—akan sangat memengaruhi kecepatan konvergensi algoritma VQE dalam meminimalkan energi Hamiltonian portofolio:
$$\begin{equation}
E(\boldsymbol{\theta}) = \langle \psi(\boldsymbol{\theta}) | H | \psi(\boldsymbol{\theta}) \rangle
\end{equation}$$

## 4. Optimasi Parameter dan Pengukuran Energi
Langkah terakhir dalam implementasi *ansatz* adalah pengukuran nilai ekspektasi energi dari Hamiltonian $H$ yang telah dipetakan dari masalah QUBO. Nilai $E(\boldsymbol{\theta})$ yang diperoleh dari komputer kuantum kemudian dikirimkan kembali ke pengoptimal klasik (seperti SPSA atau GD) untuk memperbarui vektor parameter $\boldsymbol{\theta}$. Proses ini dilakukan secara berulang-ulang hingga nilai energi mencapai titik minimum global yang merepresentasikan alokasi bobot portofolio paling efisien. Vektor parameter optimal $\boldsymbol{\theta}^*$ kemudian didekodekan kembali menjadi bobot portofolio $w_i$ melalui proses diskritisasi biner yang telah dibahas sebelumnya.

Keberhasilan VQE sangat bergantung pada kemampuan *ansatz* untuk meminimalkan *approximation error*. Jika *ansatz* terlalu sederhana, ia mungkin tidak mampu mencapai *ground state* yang sebenarnya, sehingga menghasilkan solusi sub-optimal. Sebaliknya, *ansatz* yang terlalu kompleks akan sulit dilatih oleh pengoptimal klasik akibat lanskap energi yang terlalu bergejolak. Dengan demikian, pengembangan desain *ansatz* yang adaptif dan terinspirasi oleh struktur masalah finansial (*problem-inspired ansatz*) menjadi fokus penelitian utama untuk mencapai *quantum advantage* dalam bidang ekonomi fisik dan keuangan kuantum.

## 5. Penurunan Rumus
sesuai konvensi yang ada, bentuk matriks dari rotasi ry dan rz adalah
$$
R_y(\theta) = \begin{pmatrix} \cos(\theta/2) & -\sin(\theta/2) \\ \sin(\theta/2) & \cos(\theta/2) \end{pmatrix} \quad R_z(\theta) = \begin{pmatrix} e^{-i\theta/2} & 0 \\ 0 & e^{i\theta/2} \end{pmatrix}
$$

untuk gerbang entanglement CNOT adalah
$$
CNOT = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix}
$$

untuk gerbang entanglement CZ adalah
$$
CZ = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & -1 \end{pmatrix}
$$

lalu 
$$
\begin{align}
U_{1q}(\theta) &= R_z(\theta_{1z}) R_y(\theta_{1y}) \\
&= \begin{pmatrix} e^{-i\theta_{1z}/2} & 0 \\ 0 & e^{i\theta_{1z}/2} \end{pmatrix} \begin{pmatrix} \cos(\theta_{1y}/2) & -\sin(\theta_{1y}/2) \\ \sin(\theta_{1y}/2) & \cos(\theta_{1y}/2) \end{pmatrix} \\
&= \begin{pmatrix} e^{-i\theta_{1z}/2} \cos(\theta_{1y}/2) & -e^{-i\theta_{1z}/2} \sin(\theta_{1y}/2) \\ e^{i\theta_{1z}/2} \sin(\theta_{1y}/2) & e^{i\theta_{1z}/2} \cos(\theta_{1y}/2) \end{pmatrix}
\end{align}
$$
sehingga untuk 2 qubit
lalu 
$$
\begin{align}
U_{q}(\theta) &= [R_z(\theta_{1z}) R_y(\theta_{1y})] \otimes [R_z(\theta_{2z}) R_y(\theta_{2y})]\\
&= \begin{pmatrix} e^{-i\theta_{1z}/2} \cos(\theta_{1y}/2) & -e^{-i\theta_{1z}/2} \sin(\theta_{1y}/2) \\ e^{i\theta_{1z}/2} \sin(\theta_{1y}/2) & e^{i\theta_{1z}/2} \cos(\theta_{1y}/2) \end{pmatrix} \otimes \begin{pmatrix} e^{-i\theta_{2z}/2} \cos(\theta_{2y}/2) & -e^{-i\theta_{2z}/2} \sin(\theta_{2y}/2) \\ e^{i\theta_{2z}/2} \sin(\theta_{2y}/2) & e^{i\theta_{2z}/2} \cos(\theta_{2y}/2) \end{pmatrix} \\
&= \begin{pmatrix} e^{-i(\theta_{1z}+\theta_{2z})/2} c_1c_2 & e^{-i(\theta_{1z}+\theta_{2z})/2} c_1s_2 & e^{-i(\theta_{1z}+\theta_{2z})/2} s_1c_2 & e^{-i(\theta_{1z}+\theta_{2z})/2}  s_1s_2  \\ e^{-i\theta_{1z}/2}e^{i\theta_{2z}/2} c_1s_2& e^{-i\theta_{1z}/2}e^{i\theta_{2z}/2}  c_1c_2& e^{-i\theta_{1z}/2}e^{i\theta_{2z}/2}  s_1s_2& e^{-i\theta_{1z}/2}e^{i\theta_{2z}/2}  s_1c_2  \\ e^{i\theta_{1z}/2}e^{-i\theta_{2z}/2} s_1c_2& e^{i\theta_{1z}/2}e^{-i\theta_{2z}/2} s_1s_2& e^{i\theta_{1z}/2}e^{-i\theta_{2z}/2} c_1c_2& e^{i\theta_{1z}/2}e^{-i\theta_{2z}/2}  c_1s_2  \\ e^{i(\theta_{1z}+\theta_{2z})/2}  s_1s_2& e^{i(\theta_{1z}+\theta_{2z})/2}  s_1c_2& e^{i(\theta_{1z}+\theta_{2z})/2}  c_1s_2& e^{i(\theta_{1z}+\theta_{2z})/2} c_1c_2 \end{pmatrix} \end{align}
$$

dengan

$$ c_i=\cos\frac{\theta_{iy}}2,\qquad s_i=\sin\frac{\theta_{iy}}2.  
$$

---

## Saran untuk penulisan skripsi

Saya justru **tidak menyarankan** menuliskan matriks (4\times4) penuh kecuali memang diperlukan. Dalam konteks ansatz VQE atau PQC, biasanya cukup dituliskan

# [  
U_q(\theta)

U_{1q}(\theta_1)\otimes U_{1q}(\theta_2),  
]

kemudian dijelaskan bahwa karena tensor product dua matriks (2\times2) menghasilkan matriks (4\times4), operator tersebut bekerja pada ruang Hilbert dua qubit berdimensi empat. Bentuk eksplisit matriks penuh umumnya hanya memperpanjang naskah tanpa memberikan wawasan tambahan, kecuali Anda memang akan menggunakan elemen-elemennya untuk penurunan matematis berikutnya.
sedangkan untuk entanglement layer 
$$
U_{ent} = CNOT_{(N-1,0)} \prod_{q=0}^{N-2} CNOT_{(q,q+1)}
$$

untuk sistem 2 qubit
$$
U_{ent} = CNOT_{(1,0)} \cdot CNOT_{(0,1)}
$$
di mana
$$
CNOT_{(1,0)} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \end{pmatrix} \quad CNOT_{(0,1)} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix}
$$

sehingga totalnya;
$$
U_{ent} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \end{pmatrix} \cdot \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 1 & 0 & 0 \end{pmatrix}
$$