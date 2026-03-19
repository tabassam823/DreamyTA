# Penurunan Formal Model Markowitz-Ising Berbasis Strategic Game Theory dan Quantum Information

Dokumen ini menyajikan derivasi matematis lengkap untuk mentransformasikan masalah optimasi portofolio Markowitz ke dalam Hamiltonian *Ising*. Kita melakukan *upgrade* pada parameter biaya menggunakan probabilitas strategi biner dan *Quantum Mutual Information* (QMI). Analisis ini ditujukan untuk audiens dengan latar belakang matematika dan fisika yang memerlukan pembuktian rigoritas tinggi.

---

## 1. Dinamika Portofolio dan Fungsi Objektif Markowitz
Risiko portofolio didefinisikan sebagai varians dari imbal hasil gabungan $\sigma_p^2$. Untuk sistem dengan $N$ aset, variansnya adalah:
$$\sigma_p^2 = \text{Var}\left( \sum_{i=1}^N x_i r_i \right) = \sum_{i=1}^N \sum_{j=1}^N x_i x_j \sigma_{ij} \quad (1)$$
Di mana $x_i \in \{0, 1\}$ adalah variabel keputusan biner. Fungsi objektif Markowitz bertujuan meminimalkan risiko sekaligus memaksimalkan imbal hasil $\mu$ dengan parameter *risk aversion* $\lambda$:
$$\min \mathcal{L}_{pure} = \sum_{i,j} \sigma_{ij} x_i x_j - \lambda \sum_i \mu_i x_i \quad (2)$$

## 2. Transformasi ke Quadratic Unconstrained Binary Optimization (QUBO)
Untuk mencapai bentuk QUBO standar, kita memanfaatkan properti **idempotensi** variabel biner, di mana $x_i^2 = x_i$. Suku diagonal ($i=j$) pada persamaan (1) dapat digabungkan dengan suku imbal hasil:
$$\mathcal{L}_{pure} = \sum_i (\sigma_i^2 - \lambda \mu_i) x_i + \sum_{i<j} 2\sigma_{ij} x_i x_j \quad (3)$$
Dalam format QUBO: $\mathcal{L}_{pure} = \sum_i Q_{ii} x_i + \sum_{i<j} Q_{ij} x_i x_j$.

## 3. Refinisi Parameter Strategis via Regime-Conditioned Utility
Kita melakukan *upgrade* pada $Q_{ii}$ menggunakan dekomposisi strategi biner *Up/Down* selama rentang waktu $T$.

### 3.1 Konstruksi Payoff Strategi Individual ($Q_{ii}$)
Utilitas aset $i$ dikondisikan pada strategi harian $s \in \{u, d\}$ (di mana $u: C_t > O_t$). Kita mendefinisikan utilitas *risk-adjusted* kondisional $V_{i,s} = \mu_{i,s} - \lambda \sigma_{i,s}^2$. Parameter diagonal final adalah ekspektasi dari utilitas tersebut:
$$Q_{ii} = - \mathbb{E}[V_i] = - \sum_{s \in \{u,d\}} P(S_i = s) (\mu_{i,s} - \lambda \sigma_{i,s}^2) \quad (4)$$

### 3.2 Interaksi Informasi Non-Linear via Matriks Densitas
Untuk $Q_{ij}$, kita mengintegrasikan QMI untuk menangkap korelasi non-linear. Secara ontologis, kita mengonstruksi matriks densitas diagonal pada ruang Hilbert $\mathcal{H}_i \otimes \mathcal{H}_j$:
$$\rho_{ij} = \sum_{a,b \in \{u,d\}} P(a, b) |a,b\rangle\langle a,b| \quad (5)$$
Karena $\rho_{ij}$ diagonal, entropi von Neumann $S(\rho)$ tereduksi menjadi entropi Shannon. QMI didefinisikan sebagai $I(i:j) = S(\rho_i) + S(\rho_j) - S(\rho_{ij})$. Parameter interaksi diredefinisi menjadi:
$$Q_{ij} = 2 \cdot \text{Cov}(i, j) \cdot [1 + \xi I(i:j)] \quad (6)$$
**Catatan Simetri:** Karena $\text{Cov}(i,j) = \text{Cov}(j,i)$ dan $I(i:j) = I(j:i)$, maka $Q_{ij} = Q_{ji}$ terjamin secara matematis. 
**Kalibrasi $\xi$:** Parameter $\xi \geq 0$ bertindak sebagai koefisien kalibrasi informasi. Dalam praktik, $\xi$ harus dipilih sedemikian rupa agar matriks $Q$ tetap *positive semi-definite* (PSD) untuk menjamin masalah optimasi yang *well-posed*.

## 4. Formalisme Potential Game: Bukti Eksistensi Nash Equilibrium
Kita membuktikan bahwa sistem ini adalah **Exact Potential Game**. Untuk pemain $i$, kita definisikan fungsi utilitas individu $V_i$ sebagai kontribusi negatifnya terhadap biaya total:
$$V_i(x_i, x_{-i}) = -(Q_{ii} x_i + \sum_{j \neq i} Q_{ij} x_i x_j) \quad (7)$$
Definisikan fungsi potensial global $\Phi(x) = -\mathcal{L}_{total}(x)$. Perubahan utilitas pemain $i$ saat beralih strategi $x_i \to x_i'$ adalah:
$$\Delta V_i = V_i(x_i', x_{-i}) - V_i(x_i, x_{-i})$$
Dengan mensubstitusi persamaan (7) dan memanfaatkan simetri $Q_{ij} = Q_{ji}$, diperoleh:
$$\Delta V_i = (Q_{ii} + \sum_{j \neq i} Q_{ij} x_j)(x_i - x_i') = \Phi(x_i', x_{-i}) - \Phi(x_i, x_{-i})$$
Hal ini membuktikan bahwa setiap penurunan energi Hamiltonian berkorespondensi tepat dengan peningkatan utilitas strategis, sehingga *ground state* sistem adalah *Pure Strategy Nash Equilibrium* (PSNE).

## 5. Penurunan Penalti Batasan Portofolio (Kardinalitas)
Untuk memastikan $\sum x_i = K$, kita tambahkan penalti kuadratik $P(x) = A(\sum x_i - K)^2$. Ekspansi binomialnya adalah:
$$P(x) = A \left( (\sum x_i)^2 - 2K \sum x_i + K^2 \right)$$
Menggunakan properti $x_i^2 = x_i$, suku $(\sum x_i)^2$ menjadi $\sum x_i + 2 \sum_{i<j} x_i x_j$. Substitusi menghasilkan bentuk QUBO penalti:
$$H_{pen} = \sum_i A(1 - 2K) x_i + \sum_{i<j} 2A x_i x_j \quad (8)$$

## 6. Pemetaan ke Hamiltonian Ising via Transformasi Affine
Kita memetakan variabel biner $x_i \in \{0, 1\}$ ke operator *spin* $\hat{Z}_i \in \{1, -1\}$ melalui transformasi $x_i = \frac{1 - \hat{Z}_i}{2}$. Substitusi ke dalam Hamiltonian total $H = H_{pure} + H_{pen}$ menghasilkan:
$$\hat{H}_{final} = \sum_{i<j} J_{ij} \hat{Z}_i \hat{Z}_j + \sum_i h_i \hat{Z}_i + C \quad (9)$$
**Catatan:** Suku konstan $C$ diabaikan dalam proses optimasi karena tidak mempengaruhi letak konfigurasi energi terendah (*ground state*).

### 6.1 Formulasi Parameter Akhir
Melalui ekspansi aljabar yang teliti, diperoleh koefisien Hamiltonian sebagai berikut:
1.  **Kopling Interaksi ($J_{ij}$):** Menentukan keterikatan antar aset.
    $$J_{ij} = \frac{Q_{ij} + 2A}{4} \quad (10)$$
2.  **Medan Lokal ($h_i$):** Menentukan kecenderungan intrinsik pemilihan aset.
    $$h_i = -\frac{1}{2} Q_{ii} - \sum_{j \neq i} \frac{1}{4} Q_{ij} - A(K - \frac{N}{2}) \quad (11)$$

## 7. Kesimpulan
Model ini berhasil menyatukan teori portofolio klasik, *Game Theory*, dan *Quantum Information* ke dalam satu operator energi tunggal. Dengan jaminan sifat *potential game*, algoritma VQE dipastikan dapat mencari konfigurasi portofolio yang tidak hanya meminimalkan risiko kovarians, tetapi juga mengoptimalkan aliran informasi strategis antar aset.
