# Modern Portfolio Theory (MPT) Markowitz: Pendekatan Ekonofisika Kuantum

Catatan ini merangkum metodologi optimasi portofolio berdasarkan Modern Portfolio Theory (MPT) dari Harry Markowitz yang diintegrasikan dengan *Quantum Game Theory* dan algoritma *Variational Quantum Eigensolver* (VQE), sebagaimana dijelaskan dalam `Latex/PakGagus_Presentasi4/one_by_one.ipynb`.

## 1. Parameter Dasar Markowitz

Dalam model ini, pergerakan harga saham didiskritisasi menjadi dua state kuantum:
- **Naik ($|0\rangle$)**: Jika *Daily Log Return* ($R_t$) > 0.
- **Turun ($|1\rangle$)**: Jika $R_t \le 0$.

### Risk Aversion Endogen ($\lambda_{market}$)
Alih-alih menggunakan angka statis, kecenderungan penghindaran risiko (risk aversion) dihitung secara dinamis berdasarkan kondisi pasar agregat:

$$ \lambda_{market} = \frac{1}{1 + e^{\left(\frac{\mu_{avg}}{\sigma_{avg}}\right)}} $$

Dimana:
- $\mu_{avg}$: Rata-rata return seluruh aset dalam portofolio.
- $\sigma_{avg}$: Rata-rata volatilitas (standar deviasi) seluruh aset.

## 2. Konstruksi Matriks Payoff (Utilitas Markowitz)

Nilai *Payoff* dalam interaksi antar saham (Leader-Follower) ditentukan oleh fungsi utilitas Markowitz. Untuk setiap aset $k$ pada kombinasi state $|ij\rangle$:

$$ U_k^{(ij)} = (1 - \lambda_{market}) \cdot \mu_{k}^{(ij)} - \lambda_{market} \cdot \sigma_{k}^{(ij)} $$

- **$\mu_{k}^{(ij)}$**: Rata-rata return harian aset $k$ HANYA pada hari-hari di mana state $|ij
angle$ terjadi.
- **$\sigma_{k}^{(ij)}$**: Standar deviasi return harian aset $k$ pada hari-hari tersebut.

Matriks ini merepresentasikan "keuntungan psikologis" investor berdasarkan trade-off antara return dan risiko pada kondisi spesifik.

## 3. Pemetaan ke Formalisme Kuantum

### Fungsi Gelombang ($|\psi\rangle$)
Probabilitas empiris ($P_{ij}$) dari kemunculan state bersama (misal: Saham A naik dan Saham B turun) diubah menjadi amplitudo probabilitas kuantum ($a_{ij}$):

$$ a_{ij} = \sqrt{P_{ij}} $$
$$ |\psi \rangle = a_{00} |00 \rangle + a_{01} |01\rangle + a_{10} |10\rangle + a_{11} |11\rangle $$

### Matriks Densitas dan Entropi Von Neumann
Untuk mengukur interaksi non-linear antar aset, digunakan **Quantum Mutual Information (QMI)** yang diekstrak dari **Von Neumann Entropy**:

1. **Matriks Densitas**: $\rho = |\psi\rangle\langle\psi|$
2. **Entropi**: $S(\sigma) = -\text{Tr}(\sigma \ln \sigma)$
3. **[[QMI]] ($J_{LF}$)**: $I(L : F) = S(\rho_L) + S(\rho_F) - S(\rho_{LF})$

## 4. Ising Hamiltonian dan Optimasi

Model MPT ini kemudian dipetakan ke dalam model **Ising Hamiltonian** untuk dicari solusi optimalnya (Ground State):

$$ H = - \sum_{i} h_i \sigma_i^z - \sum_{i<j} J_{ij} \sigma_i^z \sigma_j^z $$

### Parameter Hamiltonian:
- **Bias ($h_i$)**: Merepresentasikan kecenderungan intrinsik aset $i$ untuk naik atau turun berdasarkan utilitas Markowitz-nya sendiri.
  $$ h_i = \frac{\text{Expected Payoff Up} -	\text{Expected Payoff Down}}{2} $$
- **Interaksi ($J_{ij}$)**: Merepresentasikan kekuatan korelasi/keterikatan (entanglement) antar aset yang diambil dari nilai QMI.

### Optimasi VQE:
- **Ansatz**: `EfficientSU2` digunakan untuk mengeksplorasi ruang pencarian portofolio secara efisien.
- **Optimizer**: `SPSA` (Simultaneous Perturbation Stochastic Approximation) digunakan untuk meminimalkan energi Hamiltonian (mencari risiko terendah dengan utilitas tertinggi).
- **Constraint**: Penalti ditambahkan untuk memaksa sistem memilih jumlah aset tertentu ($K$) dalam portofolio.

---
*Catatan ini disusun berdasarkan simulasi data historis (BBCA, TPIA, ASII, TLKM) periode 2021-2026.*
