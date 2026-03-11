
---

## 2. Apa Arti $\text{sgn}(\rho_{ij})$ dan Cara Mendapatkannya?

### Maknanya

$\text{sgn}(\rho_{ij})$ adalah **fungsi tanda dari koefisien korelasi Pearson**, dan hanya mengambil tiga nilai:

$$\text{sgn}(\rho_{ij}) = \begin{cases} +1 & \text{jika } \rho_{ij} > 0 \quad \text{(dua aset cenderung bergerak searah)} \ -1 & \text{jika } \rho_{ij} < 0 \quad \text{(dua aset cenderung bergerak berlawanan)} \ 0 & \text{jika } \rho_{ij} = 0 \quad \text{(independen linear)} \end{cases}$$

Fungsinya dalam konteks Hamiltonian sangat spesifik: QMI selalu positif karena entropi tidak pernah negatif, sehingga QMI tidak bisa membedakan apakah dua aset bergerak _bersama_ atau _berlawanan_—ia hanya tahu "ada ketergantungan" tapi tidak tahu "arahnya." $\text{sgn}(\rho_{ij})$ hadir untuk menyuntikkan informasi arah ini ke dalam $J_{ij}$.

Efek fisiknya pada Hamiltonian adalah sebagai berikut. Bila $J_{ij} < 0$ (ferromagnetik), sistem energi rendah saat $s_i = s_j$—kedua aset cenderung sama-sama dipilih atau sama-sama dihindari. Bila $J_{ij} > 0$ (antiferromagnetik), sistem energi rendah saat $s_i \neq s_j$—satu aset dipilih dan yang lain dihindari, berguna untuk _hedging_.

### Cara Mendapatkannya

Secara praktis, prosesnya dua langkah:

**Langkah 1: Hitung korelasi Pearson dari data return harian**

$$\rho_{ij} = \frac{\sum_{t=1}^{T}(r_{i,t} - \bar{r}_i)(r_{j,t} - \bar{r}_j)}{\sqrt{\sum_t(r_{i,t}-\bar{r}_i)^2 \cdot \sum_t(r_{j,t}-\bar{r}_j)^2}}$$

Di mana $r_{i,t}$ adalah _return_ harian aset $i$ pada hari $t$. Ini menghasilkan nilai $\rho_{ij} \in [-1, +1]$.

**Langkah 2: Ambil hanya tandanya**

$$\text{sgn}(\rho_{ij}) = \frac{\rho_{ij}}{|\rho_{ij}|}$$

Atau dalam Python, cukup `np.sign(pearson_corr_matrix)`.

### Satu Catatan Penting

Ada celah yang perlu disadari: $\rho_{ij}$ hanya menangkap ketergantungan **linear**. Dua aset bisa memiliki $\rho_{ij} \approx 0$ tapi tetap memiliki $I(i:j)$ yang besar kalau ketergantungannya non-linear (misalnya, satu aset selalu bergerak besar saat yang lain stabil—hubungan yang tidak tertangkap korelasi Pearson). Dalam kasus seperti ini, $J_{ij} = \text{sgn}(\rho_{ij}) \cdot \sqrt{I(i:j)}$ akan menghasilkan nilai kecil padahal interaksi informasionalnya signifikan. Ini adalah salah satu kelemahan desain yang jujur perlu diakui dalam model ini.