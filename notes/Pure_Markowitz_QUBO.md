# Eksplorasi Modular: Penurunan Markowitz ke Ising Hamiltonian

Dokumen ini menyajikan derivasi bertahap model portofolio Markowitz, dimulai dari formulasi unconstrained (tanpa kendala) hingga penambahan suku penalti batasan pada level Hamiltonian Ising.

## 1. Urgensi Eksplorasi
Mengapa memisahkan objektif murni dari suku penalti? Secara numerik, pemisahan ini memungkinkan kita untuk menganalisis "lanskap energi alami" dari risiko dan return sebelum dipaksa oleh batasan (constraint). Hal ini krusial untuk mendiagnosis apakah kegagalan konvergensi VQE disebabkan oleh parameter ekonomi ($\lambda, \mu, \sigma$) atau oleh kerasnya batasan penalti ($A$).

## 2. Aksioma & Intuisi
Kita memandang pemilihan aset sebagai sistem partikel biner. Setiap aset $i$ memiliki dua keadaan: $|1\rangle$ (dibeli) dan $|0\rangle$ (dihindari).
- **Risiko ($\Sigma$):** Bertindak sebagai energi interaksi antar partikel. Jika dua aset berkorelasi positif, sistem akan "panas" (energi tinggi) jika keduanya dipilih bersamaan.
- **Return ($\mu$):** Bertindak sebagai medan eksternal yang menarik partikel ke keadaan energi rendah (menguntungkan).

## 3. Reduksionisme (Kasus Minimal: 2 Aset)
Sebelum generalisasi $N$-aset, mari bedah sistem 2-aset tanpa penalti:
$$ \mathcal{L}_{pure} = \sigma_1^2 x_1 + \sigma_2^2 x_2 + 2\sigma_{12}x_1 x_2 - \lambda(\mu_1 x_1 + \mu_2 x_2) \qquad (1) $$
Jika $x_1=1, x_2=0$, maka $E = \sigma_1^2 - \lambda \mu_1$. Kita mencari kombinasi $x_i$ yang menghasilkan nilai $E$ terkecil.

## 4. Jembatan Formalisme & Logika
Kita menggunakan transformasi variabel biner ke spin:
$$ x_i \to s_i \in \{1, -1\} \implies x_i = \frac{1 - s_i}{2} \qquad (2) $$
Logikanya: 
- Jika $s_i = 1$ (spin up), maka $x_i = 0$.
- Jika $s_i = -1$ (spin down), maka $x_i = 1$.

## 5. Derivasi "Scratchpad": Objektif Murni
### Fase 1: Transformasi QUBO Murni
Model Markowitz murni dalam variabel $x_i$:
$$ \mathcal{L}_{pure}(x) = \sum_{i} (\sigma_i^2 - \lambda \mu_i) x_i + \sum_{i < j} 2\sigma_{ij} x_i x_j \qquad (3) $$
Kita definisikan koefisien QUBO murni:
- $Q_{ii} = \sigma_i^2 - \lambda \mu_i$
- $Q_{ij} = \sigma_{ij}$

### Fase 2: Transformasi ke Ising Murni
Substitusi $x_i = \frac{1-s_i}{2}$ ke persamaan (3):
$$ H_{pure} = \sum_i Q_{ii} \frac{1-s_i}{2} + \sum_{i<j} 2Q_{ij} \left(\frac{1-s_i}{2}\right)\left(\frac{1-s_j}{2}\right) \qquad (4) $$
Ekspansi aljabar:
$$ H_{pure} = \sum_i \frac{Q_{ii}}{2} - \sum_i \frac{Q_{ii}}{2} s_i + \sum_{i<j} \frac{Q_{ij}}{2} (1 - s_i - s_j + s_i s_j) \qquad (5) $$
Kumpulkan suku-suku berdasarkan orde spin:
- **Suku Interaksi ($J_{ij}$):** $J_{ij}^{pure} = \frac{Q_{ij}}{2}$
- **Suku Medan ($h_i$):** $h_i^{pure} = -\frac{Q_{ii}}{2} - \sum_{j \neq i} \frac{Q_{ij}}{2}$
- **Konstanta ($C$):** $C^{pure} = \sum_i \frac{Q_{ii}}{2} + \sum_{i<j} \frac{Q_{ij}}{2}$

### Fase 3: Penambahan Suku Penalti ($H_{final} = H_{pure} + H_{pen}$)
Batasan jumlah aset $K$ dinyatakan sebagai $P(x) = A (\sum x_i - K)^2$.
Transformasi ke spin:
$$ \sum x_i = \frac{N}{2} - \frac{1}{2} \sum s_i $$
Maka penalti dalam bentuk spin:
$$ H_{pen} = A \left( \left(\frac{N}{2} - K\right) - \frac{1}{2} \sum s_i \right)^2 \qquad (6) $$
Misalkan $K' = \frac{N}{2} - K$, maka:
$$ H_{pen} = A \left( K'^2 - K' \sum s_i + \frac{1}{4} (\sum s_i)^2 \right) \qquad (7) $$
Gunakan identitas $(\sum s_i)^2 = N + 2 \sum_{i<j} s_i s_j$:
> **Derivasi Identitas:**
> Ekspansi kuadrat dari jumlahan spin adalah $(\sum_i s_i)(\sum_j s_j) = \sum_i s_i^2 + \sum_{i \neq j} s_i s_j$. 
> Karena $s_i \in \{1, -1\}$, maka $s_i^2 = 1$ untuk setiap $i$, sehingga $\sum_{i=1}^N s_i^2 = N$. 
> Suku off-diagonal $\sum_{i \neq j} s_i s_j$ mengandung pasangan $(i,j)$ dan $(j,i)$ yang identik secara nilai, sehingga dapat ditulis sebagai $2 \sum_{i<j} s_i s_j$.
> Maka, $(\sum s_i)^2 = N + 2 \sum_{i<j} s_i s_j$.
$$ H_{pen} = \sum_{i<j} \frac{A}{2} s_i s_j - \sum_i (A K') s_i + A(K'^2 + \frac{N}{4}) \qquad (8) $$

## 6. Visualisasi Perhitungan (Struktur Matriks)
Gabungan parameter Hamiltonian total $H = \sum J_{ij} s_i s_j + \sum h_i s_i$ didekomposisi menjadi kontribusi fundamental (ekonomi/strategis) dan kontribusi batasan (penalti):

> **1. Matriks Interaksi ($J_{ij}$):**
> $$ J_{ij}^{total} = J_{ij}^{pure} + J_{ij}^{pen} = \frac{\sigma_{ij}}{2} + \frac{A}{2} $$
> Secara fisik, ini adalah superposisi antara kovarians pasar dan tekanan penalti yang mencegah pemilihan aset berlebih secara kolektif.

> **2. Vektor Medan Lokal ($h_i$):**
> $$ h_i^{total} = h_i^{pure} + h_i^{pen} $$
> Di mana komponen murni ($h_i^{pure}$) merepresentasikan bias intrinsik aset:
> $$ h_i^{pure} = -\frac{\sigma_i^2 - \lambda \mu_i}{2} - \sum_{j \neq i} \frac{\sigma_{ij}}{2} $$
> *(Catatan: Suku $h_i^{pure}$ ini merupakan titik masuk untuk integrasi model Game Theory [[GT_to_h]] sebagai proksi marginal payoff).*
> 
> Dan komponen penalti ($h_i^{pen}$) memastikan kepatuhan terhadap batasan jumlah aset $K$:
> $$ h_i^{pen} = -A \left(\frac{N}{2} - K\right) $$

## 7. Verifikasi & Parameter
Mari uji batas untuk $N=2$ dan $K=1$ ($K' = 0$):
- Suku interaksi $J_{12}$ akan didominasi oleh $A/2$. Jika $A$ besar, $J_{12} \gg 0$, memaksa $s_1 s_2 = -1$ (satu spin up, satu spin down), yang berarti tepat 1 aset terpilih.
- Jika $\lambda$ sangat besar, $h_i$ akan didominasi oleh $\lambda \mu_i/2$ (positif), menarik spin ke $s_i = -1$ (beli).

## 8. Analogi "Physical Insight"
Pemodelan ini setara dengan **Antiferromagnetic Ising Model** di bawah medan magnet eksternal. Suku penalti $A$ memaksa sistem untuk memiliki jumlah spin "up" dan "down" yang spesifik, mirip dengan *constraint* pada sistem magnetik yang terkurung secara geometris (*geometric frustration*).

## 9. Visualisasi Mentah
Bayangkan sebuah hiperkubus $N$-dimensi. 
1. Tanpa $A$: Titik minimum berada di pojok yang memiliki return tertinggi.
2. Dengan $A$: Pojok-pojok yang tidak memenuhi $\sum x_i = K$ ditarik ke atas (energi sangat tinggi), menyisakan lembah energi hanya pada bidang potong (*hyperplane*) yang valid.
