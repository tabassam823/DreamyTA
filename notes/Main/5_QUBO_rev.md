# Formulasi *Quadratic Unconstrained Binary Optimization* (QUBO) - Revisi Derivasi

## 1. Pendekatan Diskritisasi dalam Optimasi Kuantum
Dalam arsitektur komputasi kuantum seperti *Quantum Annealing* (QA) atau *Quantum Approximate Optimization Algorithm* (QAOA), masalah optimasi harus dipetakan ke dalam variabel biner. Transformasi dari variabel kontinu $w_i \in [0, 1]$ ke dalam variabel biner $x_i \in \{0, 1\}$ memungkinkan representasi masalah finansial pada perangkat keras kuantum.

Untuk portofolio dengan pembobotan diskrit (di mana setiap aset memiliki porsi $1/k$ dari total modal), kita dapat menggunakan variabel biner $x_i$ untuk menyatakan pemilihan aset ke-$i$. Dalam model ini, kendala anggaran terpenuhi jika $\sum_{i=1}^N x_i = k$.

## 2. Formulasi Fungsi Energi Markowitz
Fungsi biaya Markowitz yang memadukan risiko (varians) dan ekspektasi imbal hasil (*return*) dinyatakan sebagai:
$$\begin{equation}
E(\vec{x}) = \frac{\gamma}{2k^2} \sum_{i=1}^N \sum_{j=1}^N \sigma_{ij} x_i x_j - \frac{1}{k} \sum_{i=1}^N \mu_i x_i
\end{equation}$$
di mana $\gamma$ adalah parameter *risk aversion*, $\sigma_{ij}$ adalah elemen matriks kovariansi, dan $\mu_i$ adalah ekspektasi imbal hasil aset $i$.

## 3. Penalti Kendala Kuadratik
Agar solusi biner mematuhi kendala anggaran $\sum x_i = k$, kita mengintegrasikan suku penalti kuadratik $P(\vec{x})$. Penggunaan penalti kuadratik menjamin bahwa setiap deviasi dari target $k$ akan meningkatkan energi sistem secara signifikan (positif):
$$\begin{equation}
P(\vec{x}) = A \left( \sum_{i=1}^N x_i - k \right)^2
\end{equation}$$
Ekspansi dari suku penalti ini memberikan:
$$\begin{equation}
P(\vec{x}) = A \left[ \sum_{i=1}^N x_i^2 + \sum_{i \ne j} x_i x_j - 2k \sum_{i=1}^N x_i + k^2 \right]
\end{equation}$$
Mengingat $x_i \in \{0, 1\}$, maka berlaku identitas $x_i^2 = x_i$. Persamaan (3) dapat disederhanakan menjadi:
$$\begin{equation}
P(\vec{x}) = A \left[ \sum_{i \ne j} x_i x_j + (1-2k) \sum_{i=1}^N x_i + k^2 \right]
\end{equation}$$

## 4. Penurunan Hamiltonian Total (Format QUBO)
Hamiltonian total $H_{total}(\vec{x}) = E(\vec{x}) + P(\vec{x})$ diperoleh dengan menggabungkan persamaan (1) dan (4). Kita mendefinisikan koefisien linear ($Q_{ii}$) dan kuadratik ($Q_{ij}$) sebagai berikut:

$$\begin{equation}
H_{total}(\vec{x}) = \sum_{i=1}^N Q_{ii} x_i + \sum_{i < j} Q_{ij} x_i x_j + C_{offset}
\end{equation}$$

Di mana:
- $Q_{ii} = \frac{\gamma \sigma_{ii}}{2k^2} - \frac{\mu_i}{k} + A(1-2k)$
- $Q_{ij} = \frac{\gamma \sigma_{ij}}{k^2} + 2A$ (untuk $i \ne j$, karena $\sigma_{ij} = \sigma_{ji}$)
- $C_{offset} = Ak^2$

## 5. Pemetaan ke Model Ising (Hamiltonian Kuantum)
Untuk mengimplementasikannya pada sistem spin kuantum, kita melakukan transformasi variabel biner $x_i$ ke variabel spin $s_i \in \{-1, 1\}$ menggunakan relasi $x_i = \frac{s_i+1}{2}$. Substitusi ini mengubah fungsi biaya menjadi Hamiltonian Ising:

$$\begin{equation}
\hat{\mathcal{H}} = \sum_{i=1}^N h_i \hat{Z}_i + \sum_{i < j} J_{ij} \hat{Z}_i \hat{Z}_j + C
\end{equation}$$

Secara aljabar, parameter fisik Hamiltonian tersebut adalah:
- **Bias Lokal ($h_i$):** $h_i = \frac{1}{2} Q_{ii} + \sum_{j \ne i} \frac{1}{4} Q_{ij}$
- **Kopling Interaksi ($J_{ij}$):** $J_{ij} = \frac{1}{4} Q_{ij}$
- **Konstanta Pergeseran Energi ($C$):** $C = \sum_{i=1}^N \frac{Q_{ii}}{2} + \sum_{i < j} \frac{Q_{ij}}{4} + C_{offset}$

Karena operator Pauli-Z ($\hat{Z}_i$) adalah operator *self-adjoint* dan seluruh parameter ($h_i, J_{ij}, C$) bernilai riil, maka Hamiltonian $\hat{\mathcal{H}}$ dijamin bersifat **Hermit** ($\hat{\mathcal{H}} = \hat{\mathcal{H}}^\dagger$). Hal ini memastikan bahwa seluruh nilai eigen yang dihasilkan (tingkat energi sistem) bersifat riil, yang merupakan syarat fundamental bagi observabel fisik dalam mekanika kuantum.

## 6. Analisis Rigoritas dan Pembuktian Sifat Hermit
Untuk membuktikan bahwa Hamiltonian $\hat{\mathcal{H}}$ bersifat Hermit, kita harus menunjukkan bahwa $\hat{\mathcal{H}}^\dagger = \hat{\mathcal{H}}$.

### 6.1. Pembuktian Formal Aljabar
Hamiltonian Ising kita didefinisikan sebagai:
$$\hat{\mathcal{H}} = \sum_{i=1}^N h_i \hat{Z}_i + \sum_{i < j} J_{ij} \hat{Z}_i \hat{Z}_j + C \hat{I}$$
Operasi *adjoint* ($\dagger$) pada Hamiltonian ini adalah:
$$\hat{\mathcal{H}}^\dagger = \left( \sum_{i} h_i \hat{Z}_i \right)^\dagger + \left( \sum_{i < j} J_{ij} \hat{Z}_i \hat{Z}_j \right)^\dagger + (C \hat{I})^\dagger$$
Menggunakan sifat linearitas dan distributif adjoint:
$$\hat{\mathcal{H}}^\dagger = \sum_{i} h_i^* \hat{Z}_i^\dagger + \sum_{i < j} J_{ij}^* (\hat{Z}_i \hat{Z}_j)^\dagger + C^* \hat{I}^\dagger$$
Diketahui bahwa:
1. Suku parameter finansial ($h_i, J_{ij}, C$) adalah bilangan riil, sehingga $h_i^* = h_i$, $J_{ij}^* = J_{ij}$, dan $C^* = C$.
2. Operator Pauli-Z bersifat Hermit: $\hat{Z}_i^\dagger = \hat{Z}_i$.
3. Operator identitas bersifat Hermit: $\hat{I}^\dagger = \hat{I}$.
4. Untuk operator yang saling komut (seperti $\hat{Z}_i$ dan $\hat{Z}_j$ pada situs berbeda), berlaku $(\hat{Z}_i \hat{Z}_j)^\dagger = \hat{Z}_j^\dagger \hat{Z}_i^\dagger = \hat{Z}_j \hat{Z}_i = \hat{Z}_i \hat{Z}_j$.

Substitusi kembali ke persamaan memberikan:
$$\hat{\mathcal{H}}^\dagger = \sum_{i} h_i \hat{Z}_i + \sum_{i < j} J_{ij} \hat{Z}_i \hat{Z}_j + C \hat{I} = \hat{\mathcal{H}} \quad \square$$

### 6.2. Contoh Kasus: Hamiltonian 2-Qubit
Sebagai ilustrasi fungsional, tinjau portofolio dengan 2 aset. Hamiltoniannya (tanpa konstanta $C$) adalah:
$$\hat{\mathcal{H}}_{2q} = h_1 \hat{Z}_1 + h_2 \hat{Z}_2 + J_{12} \hat{Z}_1 \hat{Z}_2$$
Dalam representasi matriks (produk Kronecker):
- $\hat{Z}_1 = \sigma_z \otimes I = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \otimes \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = \text{diag}(1, 1, -1, -1)$
- $\hat{Z}_2 = I \otimes \sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} \otimes \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = \text{diag}(1, -1, 1, -1)$
- $\hat{Z}_1 \hat{Z}_2 = \sigma_z \otimes \sigma_z = \text{diag}(1, -1, -1, 1)$

Ketiga matriks di atas adalah matriks diagonal riil. Karena $h_1, h_2, J_{12} \in \mathbb{R}$, maka $\hat{\mathcal{H}}_{2q}$ akan menjadi matriks diagonal riil:
$$\hat{\mathcal{H}}_{2q} = \begin{pmatrix} h_1+h_2+J_{12} & 0 & 0 & 0 \\ 0 & h_1-h_2-J_{12} & 0 & 0 \\ 0 & 0 & -h_1+h_2-J_{12} & 0 \\ 0 & 0 & 0 & -h_1-h_2+J_{12} \end{pmatrix}$$
Matriks diagonal riil selalu memenuhi $M^\dagger = M$, sehingga terbukti secara representatif bahwa Hamiltonian yang kita susun adalah **Hermit**. Hal ini menjamin bahwa saat kita melakukan optimasi dengan algoritma seperti VQE, energi ekspektasi $\langle \psi | \hat{\mathcal{H}} | \psi \rangle$ akan selalu berupa bilangan riil yang dapat diminimalkan.
