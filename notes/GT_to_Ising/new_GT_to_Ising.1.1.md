# Derivasi Formal: Transformasi Markowitz-Ising Berbasis Strategi Biner, Game Theory, dan Informasi Kuantum

Dokumen ini menyajikan kerangka kerja matematis formal untuk mentransformasikan masalah optimasi portofolio (seleksi $K=2$ dari $N=4$ saham) ke dalam model *Ising*. Pendekatan ini merupakan *upgrade* struktural terhadap model Markowitz konvensional dengan mengintegrasikan dinamika strategi biner (*Up/Down*) dan *Quantum Mutual Information* (QMI). Melalui derivasi ini, sistem portofolio dipandang sebagai *Exact Potential Game* yang titik keseimbangannya berhimpit dengan *ground state* Hamiltonian fisik.

## 1. Konstruksi Ruang Strategi dan Isomorfisma Klasikal-ke-Kuantum
Dalam analisis ini, setiap aset $i \in \{A, B, C, D\}$ didefinisikan sebagai pemain yang mengadopsi strategi biner pada setiap waktu $t$: *Up* ($S_u$) jika $C_t > O_t$ dan *Down* ($S_d$) jika $C_t \leq O_t$. Perilaku stokastik aset selama rentang waktu $T$ diringkas dalam distribusi probabilitas marginal $P(S_i)$.

### 1.1 Justifikasi Ontologis Matriks Densitas Diagonal
Untuk menjembatani data klasikal dengan formalisme kuantum, kita mengonstruksi matriks densitas $\rho_{ij}$ pada ruang Hilbert $\mathcal{H}_i \otimes \mathcal{H}_j$ menggunakan distribusi probabilitas bersama $P(S_i, S_j)$:
$$\rho_{ij} = \sum_{s_i, s_j \in \{u,d\}} P(S_i=s_i, S_j=s_j) |s_i, s_j\rangle\langle s_i, s_j| \quad (1)$$
Karena $\rho_{ij}$ bersifat diagonal, entropi von Neumann $S(\rho) = -\text{Tr}(\rho \ln \rho)$ secara matematis ekuivalen dengan entropi Shannon $H(S)$. Penggunaan istilah *Quantum Mutual Information* (QMI) di sini didefinisikan sebagai:
$$I(i:j) = S(\rho_i) + S(\rho_j) - S(\rho_{ij}) \quad (2)$$
Nilai ini menangkap seluruh spektrum korelasi (linear dan non-linear) antar strategi aset yang nantinya dipetakan langsung ke operator Pauli-Z.

## 2. Refinisi Utilitas Markowitz melalui Strategic Risk Attribution
Optimasi biaya Markowitz $\min \mathcal{L} = x^T Q x$ diredefinisi dengan memasukkan ekspektasi utilitas yang dikondisikan pada strategi biner. Pendekatan ini menangkap non-stasioneritas data finansial melalui dekomposisi regime.

1.  **Dekomposisi Utilitas Mandiri ($Q_{ii}$):**
    $$Q_{ii} = \sum_{s \in \{u,d\}} P(S_i = s) \left( \sigma_{i,s}^2 - \lambda \mu_{i,s} \right) \quad (3)$$
    Di mana $\mu_{i,s}$ dan $\sigma_{i,s}^2$ adalah *conditional expected return* dan *variance* aset $i$ pada regime strategi $s$.
2.  **Interaksi Strategis dan Diversifikasi ($Q_{ij}$):**
    $$Q_{ij} = 2 \cdot \text{Cov}(i, j) \cdot \left[ 1 + \xi I(i:j) \right] \quad (4)$$
    Parameter $\xi$ berfungsi sebagai *scaling factor* untuk interaksi informasi, di mana QMI memberikan penalti tambahan pada pasangan aset yang memiliki keterikatan strategis yang kuat (mengurangi risiko sistemik).

## 3. Formalisme Potential Game: Bukti Kestabilan Sistem
Sistem ini diklaim sebagai *Exact Potential Game*. Sebuah permainan dikatakan memiliki fungsi potensial $\Phi(x)$ jika perubahan utilitas setiap pemain saat berpindah strategi ekuivalen dengan perubahan pada $\Phi(x)$.

**Bukti Formal:**
Misalkan fungsi biaya total adalah $f(x) = \sum Q_{ii} x_i + \sum Q_{ij} x_i x_j$. Kita mendefinisikan fungsi potensial $\Phi(x) = -f(x)$. Untuk setiap pemain $i$, jika ia mengubah keputusannya dari $x_i$ ke $x_i'$, maka:
$$\Delta V_i = V_i(x_i', x_{-i}) - V_i(x_i, x_{-i}) = \Phi(x_i', x_{-i}) - \Phi(x_i, x_{-i}) \quad (5)$$
Karena $Q$ simetris ($Q_{ij} = Q_{ji}$), kondisi ini terpenuhi secara identik. Konsekuensi matematisnya adalah setiap *Pure Strategy Nash Equilibrium* (PSNE) dari sistem ini berkorespondensi langsung dengan titik ekstrim (minimum/maximum) dari fungsi biaya. Dalam konteks optimasi kuantum, mencari *ground state* Hamiltonian Ising setara dengan mencari *Nash Equilibrium* yang paling stabil.

## 4. Transformasi Hamiltonian Ising dan Optimasi VQE
Untuk mengimplementasikan seleksi tepat 2 dari 4 saham, kita menyertakan kendala kardinalitas melalui penalti kuadratik $A(\sum x_i - 2)^2$. Transformasi variabel biner $x_i \mapsto \frac{1 - \hat{Z}_i}{2}$ menghasilkan Hamiltonian target:
$$\hat{H}_{final} = \sum_{i<j} J_{ij}^{total} \hat{Z}_i \hat{Z}_j + \sum_i h_i^{total} \hat{Z}_i \quad (6)$$

Dengan parameter fisik yang diturunkan secara presisi:
- **Kopling Interaksi ($J_{ij}^{total}$):** $\frac{1}{2}(Q_{ij} + A)$
- **Medan Lokal ($h_i^{total}$):** $-\frac{1}{2}Q_{ii} - \sum_{j \neq i} \frac{1}{2}Q_{ij} - A K'$, di mana $K' = K - N/2 = 0$.

## 5. Kesimpulan dan Implikasi Teknis
Melalui integrasi *Game Theory* dan *Quantum Information*, model ini tidak hanya mengoptimalkan portofolio berdasarkan statistik orde kedua, tetapi juga berdasarkan struktur informasi strategis antar aset. Keberadaan fungsi potensial menjamin konvergensi algoritma VQE pada solusi yang stabil secara ekonomi. Penggunaan probabilitas strategi *Up/Down* memberikan dimensi temporal yang lebih kaya, memungkinkan investor untuk memahami dinamika "alasan" di balik seleksi aset dalam rentang waktu $T$.
