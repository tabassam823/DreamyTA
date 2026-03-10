# Suku Pertama & Kedua Model Markowitz: Risiko dan Return

Dokumen ini menjelaskan asal-usul matematis dari dua pilar utama portofolio: risiko ($x^T \Sigma x$) dan expected return ($\lambda \mu^T x$).

---

## 1. Filosofi: Mengapa Risiko Bersifat Kuadratik?
Dalam statistik, risiko diukur sebagai **varians** ($\sigma^2$), yaitu kuadrat dari deviasi standar. Mengapa kuadrat? Karena kita ingin menghukum penyimpangan (baik positif maupun negatif) secara proporsional terhadap besarnya penyimpangan tersebut. Dalam portofolio, risiko bukan sekadar jumlahan risiko aset tunggal, melainkan interaksi antar aset.

---

## 2. Reduksionisme: Kasus 2 Aset ($N=2$)
Mari kita bedah jumlahan risiko untuk dua aset dengan bobot investasi $x_1$ dan $x_2$.

### A. Ekspansi Aljabar
Risiko total portofolio adalah varians dari jumlahan variabel acak:
$$ \text{Var}(x_1 R_1 + x_2 R_2) = x_1^2 \sigma_1^2 + x_2^2 \sigma_2^2 + 2x_1 x_2 \sigma_{12} \qquad (1) $$

> **Visualisasi (1): Jembatan Logika**
> Suku $2x_1 x_2 \sigma_{12}$ adalah **interaksi**. Jika $\sigma_{12}$ negatif, maka risiko total berkurang (diversifikasi). Inilah alasan mengapa kita tidak bisa hanya menjumlahkan varians masing-masing aset. Penurunan rumusnya bisa dilihat di [[suku_pertama_kedua_pers1]]

---

## 3. Jembatan Logika: Representasi Matriks Risiko
Persamaan (1) dapat ditulis secara elegan dalam bentuk matriks $x^T \Sigma x$.

### A. Konstruksi Matriks Kovarians ($\Sigma$)
Matriks $\Sigma$ menampung seluruh informasi risiko:
$$ \Sigma = \begin{pmatrix} \sigma_1^2 & \sigma_{12} \\ \sigma_{21} & \sigma_2^2 \end{pmatrix} \qquad (2) $$

> **Visualisasi (2): Operasi Matriks**
> Mari kita lakukan perkalian $x^T \Sigma x$:
> $$ 
\begin{split}
x^T \Sigma x &= \begin{pmatrix} x_1 & x_2 \end{pmatrix} \begin{pmatrix} \sigma_1^2 & \sigma_{12} \\ \sigma_{21} & \sigma_2^2 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} \\\\
&= \begin{pmatrix} x_1 & x_2 \end{pmatrix} \begin{pmatrix} \sigma_1^2 x_1 + \sigma_{12} x_2 \\ \sigma_{21} x_1 + \sigma_2^2 x_2 \end{pmatrix} \\\\
&= x_1(\sigma_1^2 x_1 + \sigma_{12} x_2) + x_2(\sigma_{21} x_1 + \sigma_2^2 x_2) \\\\
&= \sigma_1^2 x_1^2 + \sigma_2^2 x_2^2 + 2\sigma_{12} x_1 x_2
\end{split}
$$
> Hasil ini tepat sama dengan persamaan (1). Bentuk ini disebut **Quadratic Form**.

---

## 4. Prinsip Diagonalisasi: Mencari "Aset Murni"
Diagonalisasi adalah proses memutar sistem koordinat kita untuk menemukan arah risiko yang independen.

### A. Dekomposisi Spektral
Karena $\Sigma$ adalah matriks simetris, dia bisa didiagonalisasi menjadi:
$$ \Sigma = V D V^T \qquad (3) $$

> **Visualisasi (3): Transformasi Koordinat**
> Jika kita definisikan variabel baru $y = V^T x$, maka risiko menjadi:
> $$ x^T \Sigma x = (V^T x)^T D (V^T x) = y^T D y = \lambda_1 y_1^2 + \lambda_2 y_2^2 \qquad (4) $$
> 
> > Dalam koordinat $y$, tidak ada lagi interaksi. Kita telah mengubah portofolio kompleks menjadi kombinasi linear dari "aset murni" yang tidak saling berkorelasi.

---

## 5. Suku Kedua: Return sebagai Proyeksi Linear ($\lambda \mu^T x$)
Berbeda dengan risiko yang bersifat kuadratik (luasan), keuntungan yang diharapkan (*expected return*) bersifat linear.

### A. Filosofi Return
Return portofolio adalah jumlahan bobot aset dikali rata-rata return masing-masing aset ($\mu_i$). Secara matematis:
$$ E[R_p] = \sum_{i=1}^N \mu_i x_i \qquad (5) $$

> **Visualisasi (5): Operasi Matriks**
> Ini adalah **Dot Product** antara vektor return $\mu$ dan vektor posisi $x$:
> $$ \mu^T x = \begin{pmatrix} \mu_1 & \mu_2 & \dots & \mu_N \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ \dots \\ x_N \end{pmatrix} = \mu_1 x_1 + \mu_2 x_2 + \dots + \mu_N x_N \qquad (6) $$

### B. Peran Parameter Risk Aversion ($\lambda$)
Dalam fungsi objektif $E = x^T \Sigma x - \lambda \mu^T x$, parameter $\lambda$ bertindak sebagai "tali penarik".
- Jika **$\lambda$ kecil**: Anda sangat takut risiko. VQE akan fokus meminimalkan $x^T \Sigma x$.
- Jika **$\lambda$ besar**: Anda haus keuntungan. VQE akan fokus memaksimalkan $\mu^T x$.

---

## 6. Jembatan Logika: Mengapa Linear vs Kuadrat?
- **Risiko ($x^T \Sigma x$):** Bersifat kuadratik karena ia mewakili energi yang terdistribusi di seluruh dimensi interaksi (seperti energi potensial pegas).
- **Return ($\lambda \mu^T x$):** Bersifat linear karena ia mewakili proyeksi satu dimensi ke arah "keuntungan" (seperti gaya gravitasi yang menarik ke satu arah).

---

## 7. Physical Insight: Gaya dalam Lanskap Energi
Bayangkan portofolio Anda sebagai partikel di sebuah bukit:
1. **Risiko** adalah kecuraman bukit di segala arah (permukaan kuadratik). Partikel ingin diam di lembah agar aman.
2. **Return** adalah gaya angin yang meniup partikel ke arah puncak tertentu (vektor $\mu$).
3. **Optimasi VQE** adalah mencari titik keseimbangan di mana partikel tersebut berhenti: tidak terlalu tinggi agar tidak jatuh (risiko rendah), tapi cukup jauh tertiup angin agar mendapat untung (return tinggi).

---

## 8. Kesimpulan untuk VQE
Dalam Hamiltonian Ising:
1. Suku risiko $\Sigma_{ij}$ menyumbang pada **Kopling $J_{ij}$** (karena bersifat $x_i x_j$).
2. Suku return $\mu_i$ menyumbang pada **Field Lokal $h_i$** (karena bersifat linear $x_i$).

VQE mencari *ground state* dari sistem yang "ditiup angin return" dan "ditekan oleh lembah risiko" secara bersamaan.
