# Transformasi Game Theory ke Ising: Derivasi Parameter Bias ($h_i$)

Dokumen ini membedah proses transformasi strategis dari perilaku pelaku pasar menuju parameter fisik dalam Hamiltonian Ising, membangun jembatan antara teori permainan dan mekanika kuantum.

## 1. Urgensi Eksplorasi: Mengapa Game Theory?
Model Markowitz konvensional seringkali gagal menangkap "jiwa" pasar karena menganggap aset sebagai entitas pasif. Dalam realitasnya, harga saham bergerak bukan hanya karena statistik internal, melainkan karena interaksi strategis antar pemain. Memahami bagaimana "insentif" diubah menjadi "medan magnet" ($h_i$) adalah kunci untuk membuat VQE yang adaptif terhadap kondisi pasar yang dinamis.

---

## 2. Aksioma & Intuisi: Hierarki Logika Teori Permainan
Kita membangun alur berpikir dari model yang paling kaku (ideal) ke yang paling realistis (data pasar).

1. **Aksioma Utilitas:** Sistem bertindak untuk memaksimalkan angka kepuasan (Return).
2. **Zero-Sum Game:** Model konflik murni ($A + B = 0$).
3. **Non Zero-Sum Game:** Model realitas pasar di mana keuntungan bersama dimungkinkan ($A + B \neq 0$).
4. **MSNE (Mixed Strategy Nash Equilibrium):** Penggunaan probabilitas dalam strategi karena ketidakpastian masa depan.

---

## 3. Reduksionisme: Kasus Minimal 2 Aset (Bimatrix)
Mari kita bedah interaksi antara Saham $i$ dan Saham $j$. Setiap aset memiliki dua strategi: Naik ($+1$) atau Turun ($-1$).

### A. Matriks Payoff Saham $i$ ($V_i$)
Status Saham $i$ ditentukan oleh responnya terhadap kondisi Saham $j$.

| $i \setminus j$ | Naik ($+1$) | Turun ($-1$) |
| :--- | :--- | :--- |
| **Naik ($+1$)** | $R_{UU}$ | $R_{UD}$ |
| **Turun ($-1$)** | $R_{DU}$ | $R_{DD}$ |

> **Visualisasi: Operasi Matriks Payoff**
> Secara linear, return Saham $i$ dapat direpresentasikan dalam matriks $2 \times 2$:
> $$ V_i = \begin{pmatrix} R_{UU} & R_{UD} \\ R_{DU} & R_{DD} \end{pmatrix} $$
> Di mana $R_{xy}$ adalah hasil (outcome) historis bagi Saham $i$ saat ia berada di kondisi $x$ dan pasangannya di kondisi $y$.

---

## 4. Jembatan Formalisme & Logika: Dari Frekuensi ke Probabilitas
Dalam realitas pasar, kita tidak tahu strategi lawan secara pasti, maka kita menggunakan frekuensi kejadian masa lalu sebagai proksi probabilitas.

### A. Definisi Probabilitas Gabungan
Misalkan $n_{xy}$ adalah jumlah hari di mana kondisi $(x,y)$ terjadi dalam total $N$ observasi:
$$ P(x,y) = \frac{n_{xy}}{N} \qquad (1) $$

> **Visualisasi (1): Matriks Probabilitas**
> Kita mendistribusikan frekuensi kejadian ke dalam matriks probabilitas:
> $$ \mathbf{P} = \frac{1}{N} \begin{pmatrix} n_{UU} & n_{UD} \\ n_{DU} & n_{DD} \end{pmatrix} $$
> Syarat normalisasi: $\sum_{x,y} P(x,y) = 1$.

---

## 5. Derivasi Matematis: Mencari Parameter $h_i$
Kita akan membedah turunan matematisnya secara runut. Semua variabel berada di ranah bilangan real ($\mathbb{R}$), memastikan Hamiltonian bersifat Hermitian sebelum dieksekusi oleh sirkuit kuantum.

### A. Definisi Variabel dan Domain
- $s_i, s_j \in \{+1, -1\}$: Variabel keputusan (spin) diskret.
- $V(s_i, s_j) \in \mathbb{R}$: Fungsi *payoff* (imbal hasil) dalam angka real.
- $P(s_j) \in [0, 1]$: Probabilitas state saham $j$, di mana $\sum P(s_j) = 1$.
- $E[i|s_i] \in \mathbb{R}$: *Expected Value* marginal untuk state tertentu.
- $h_i \in \mathbb{R}$: Parameter medan lokal atau bias linear yang dicari.

### B. Langkah 1: Mencari Nilai Harapan (Expected Value)
Nilai harapan dari sebuah variabel acak adalah jumlah hasil dikalikan probabilitasnya. Jika kita mengunci saham $i$ pada posisi Naik ($s_i = +1$):
$$ E[i|+] = \sum_{s_j \in \{+1, -1\}} P(s_j) \cdot V(+1, s_j) \qquad (2) $$
$$ E[i|+] = P(j+) V(+,+) + P(j-) V(+,-) $$

Sebaliknya, untuk posisi Turun ($s_i = -1$):
$$ E[i|-] = \sum_{s_j \in \{+1, -1\}} P(s_j) \cdot V(-1, s_j) \qquad (3) $$
$$ E[i|-] = P(j+) V(-,+) + P(j-) V(-,-) $$

> **Visualisasi (2-3): Perhitungan Linear**
> Secara operasional, ini adalah perkalian baris matriks probabilitas dengan matriks return:
> $$ E[i|s_i] = \begin{pmatrix} P_{j+} & P_{j-} \end{pmatrix} \begin{pmatrix} V(s_i, +) \\ V(s_i, -) \end{pmatrix} $$

### C. Langkah 2: Pemetaan Ekonomi ke Hamiltonian Ising ($h_i$)
Dalam Model Ising, kontribusi energi linear dari satu spin adalah $H_{lokal}(s_i) = -h_i s_i$. Kita harus menyelaraskan dua dunia ini:
- **Game Theory:** Memaksimalkan Payoff ($E$).
- **Fisika:** Meminimalkan Energi ($H$).
- **Aksioma Pemetaan:** $H \equiv -E$.

> **Visualisasi (C): Konsistensi Energi**
> 1. Jika $s_i = +1$, maka $H = -h_i$. Ini harus ekuivalen dengan $-E[i|+]$.
> 2. Jika $s_i = -1$, maka $H = +h_i$. Ini harus ekuivalen dengan $-E[i|-]$.

### D. Solusi Aljabar untuk $h_i$
Kita hitung selisih energi ($\Delta H$) antara kedua state:
$$ \Delta H = H(-1) - H(+1) = (+h_i) - (-h_i) = 2h_i $$
Di sisi lain, selisih ini harus sama dengan minus selisih ekspektasi payoff:
$$ \Delta H = -E[i|-] - (-E[i|+]) = E[i|+] - E[i|-] $$
Sehingga kita mendapatkan rumus final:
$$ h_i = \frac{E[i|+] - E[i|-]}{2} \qquad (4) $$

---

## 6. Visualisasi Perhitungan (Blok `>`)
> **Eksekusi Numerik (Data 20 Hari):**
> 1. Probabilitas: $P_{j+} = 0.5, P_{j-} = 0.5$.
> 2. Payoff: $V(+,+) = 0.02, V(+,-) = 0.01, V(-,+) = -0.01, V(-,-) = -0.02$.
> 3. Hitung Ekspektasi:
>    - $E[i|+] = (0.5 \times 0.02) + (0.5 \times 0.01) = 0.015$
>    - $E[i|-] = (0.5 \times -0.01) + (0.5 \times -0.02) = -0.015$
> 4. Hitung Bias:
>    - $h_i = (0.015 - (-0.015)) / 2 = 0.015$
> **Interpretation:** Nilai $h_i = 0.015$ menunjukkan "gradien keuntungan" per satu unit perubahan spin.

---

## 7. Kesimpulan untuk Analisis Matematis
- **Faktor Normalisasi (1/2):** Muncul karena variabel $s_i$ memiliki rentang 2 unit (dari -1 ke +1). Pembagian dengan 2 memastikan $h_i$ merepresentasikan *slope* energi per unit pergerakan state.
- **Validitas Transformasi:** Ini adalah transformasi *affine* murni. Selama matriks payoff berisi bilangan real, $h_i$ dipastikan skalar real, menjamin operator Hamiltonian bersifat Hermitian (syarat mutlak mekanika kuantum).

---

## 8. Verifikasi & Parameter: Dampak Payoff
| Kondisi Payoff  | Makna Strategis | Nilai $h_i$ | Efek Fisik pada Qubit |
| :-------------- | :-------------- | :---------- | :-------------------- |
| $E[i+] > E[i-]$ | Strategis naik. | $h_i > 0$   | Tarikan ke state $|1\rangle$ (Buy). |
| $E[i+] < E[i-]$ | Strategis turun.| $h_i < 0$   | Tolakan ke state $|0\rangle$ (Avoid).|
| $E[i+] = E[i-]$ | Netral.         | $h_i = 0$   | Tidak ada tekanan lokal. |

---

## 9. Physical Insight: Gaya Pasang Surut (Tidal Forces)
Parameter $h_i$ bukan sekadar angka statistik; ia adalah **medan magnet eksternal** yang menangkap tarikan strategis dari aset lain bahkan sebelum interaksi langsung ($J_{ij}$) terjadi. Ini memungkinkan VQE untuk mencari portfolio yang memiliki "ketahanan strategis" paling kuat.
