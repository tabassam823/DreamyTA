# Risk Aversion Endogen: Pendekatan Sigmoid dan Saturasi Informasi

Dokumen ini menjelaskan mekanisme penentuan parameter trade-off $\lambda$ secara otomatis (endogen) menggunakan fungsi aktivasi sigmoid, menghubungkan rasio *Signal-to-Noise* dengan nafsu investasi.

## 1. Urgensi: Mengapa Sigmoid?
Dalam model Markowitz statis, $\lambda$ (bobot return) seringkali dipilih secara subjektif (misal $\lambda=0.5$). Namun, pasar yang riil bersifat dinamis. Kita membutuhkan fungsi yang bisa mengubah rasio performa aset ($\mu/\sigma$) menjadi bobot keputusan yang halus namun memiliki batas yang jelas. Fungsi Sigmoid adalah kandidat sempurna karena ia memetakan input tak terbatas menjadi output dalam rentang $(0, 1)$.

---

## 2. Aksioma & Intuisi: Psikologi Keputusan
Ada tiga aksioma dasar yang melandasi penggunaan fungsi ini:
1.  **Aksioma Signal-to-Noise:** Investor tidak melihat keuntungan ($\mu$) secara terisolasi, melainkan selalu membandingkannya dengan derau/risiko ($\sigma$). Rasio $\mu/\sigma$ adalah penggerak utama keputusan.
2.  **Aksioma Saturasi:** Nafsu terhadap keuntungan tidak tumbuh linear tanpa batas. Ada titik di mana tambahan keuntungan tidak lagi menambah "nafsu" secara signifikan (titik jenuh/saturasi).
3.  **Aksioma Batas:** Parameter $\lambda$ harus berada di antara 0 (fokus total pada risiko) dan 1 (fokus total pada return).

---

## 3. Reduksionisme: Kasus Minimal ($\mu = \sigma$)
Mari kita lihat apa yang terjadi jika risiko suatu aset tepat sama dengan keuntungan yang diharapkan.

### A. Kondisi Seimbang
Jika $\mu = \sigma$, maka rasio $\mu/\sigma = 1$.
$$ \lambda = \frac{1}{1 + e^{-1}} \qquad (1) $$

> **Visualisasi (1): Jembatan Logika**
> Secara numerik:
> $$ \lambda \approx \frac{1}{1 + 0.367} \approx 0.731 $$
> Karena $\mu/\sigma$ positif dan cukup kuat, sistem "condong" untuk mengejar return ($\lambda > 0.5$). Sebaliknya, jika $\mu = 0$ (tidak ada return), maka $\lambda = 0.5$ (netral).

---

## 4. Jembatan Logika: Formalisme Fungsi Aktivasi
Dalam *Machine Learning*, sigmoid digunakan sebagai gerbang (*gate*). Dalam VQE Portofolio, $\lambda$ adalah gerbang yang menentukan seberapa besar "angin return" boleh meniup partikel kita keluar dari "lembah risiko".

### A. Persamaan Umum
$$ \lambda(\mu, \sigma) = \frac{1}{1 + e^{-(\mu/\sigma)}} \qquad (2) $$

---

## 5. Derivasi & Indeks Persamaan
Mari kita turunkan bagaimana perubahan kecil pada risiko ($\Delta \sigma$) memengaruhi selera investasi kita.

### A. Sensitivitas Selera terhadap Risiko
Turunan $\lambda$ terhadap $\sigma$ menunjukkan seberapa cepat selera kita berubah saat pasar mulai bergejolak:
$$ \frac{\partial \lambda}{\partial \sigma} = \frac{e^{-(\mu/\sigma)} \cdot (-\mu/\sigma^2)}{(1 + e^{-(\mu/\sigma)})^2} \qquad (3) $$

> **Visualisasi (3): Perhitungan Linear**
> Kita sederhanakan menggunakan properti turunan sigmoid $f'(x) = f(x)(1-f(x))$:
> $$ \frac{\partial \lambda}{\partial \sigma} = \lambda(1-\lambda) \cdot \left(\frac{\mu}{\sigma^2}\right) $$
> Misalkan pada titik netral $\lambda = 0.5$ dan $\mu/\sigma^2 = 2$:
> $$ \frac{\partial \lambda}{\partial \sigma} = (0.5)(0.5) \cdot 2 = 0.5 $$
> Ini menunjukkan bahwa pada kondisi netral, perubahan volatilitas memiliki dampak 50% terhadap pergeseran selera investasi kita.

---

## 6. Verifikasi & Parameter: Batas Ekstrem
Kita uji model ini pada tiga kondisi pasar yang berbeda:

| Kondisi Pasar | Rasio $\mu/\sigma$ | Nilai $\lambda$ | Perilaku VQE |
| :--- | :--- | :--- | :--- |
| **Pasar Euphoria** | $\mu \gg \sigma$ | $\lambda \to 1$ | Memilih aset return tertinggi, abaikan risiko. |
| **Pasar Netral** | $\mu = 0$ | $\lambda = 0.5$ | Keseimbangan antara keamanan dan cuan. |
| **Pasar Panic** | $\mu \ll 0$ | $\lambda \to 0$ | Memilih aset paling aman (varians terendah). |

> **Visualisasi (6): Contoh Perhitungan**
> Jika pasar sedang jatuh ($\mu = -10, \sigma = 2$):
> $$ \text{Rasio} = -5 \implies \lambda = \frac{1}{1 + e^5} \approx \frac{1}{1 + 148} \approx 0.006 $$
> Nilai $\lambda \approx 0$ ini akan membuat Hamiltonian VQE didominasi oleh suku risiko $x^T \Sigma x$.

---

## 7. Physical Insight: Efek "Termostat" Kuantum
Bayangkan $\lambda$ sebagai sebuah **termostat** otomatis.
1. Saat pasar "panas" (return tinggi), termostat membuka katup return lebar-lebar ($\lambda \uparrow$).
2. Saat pasar "dingin" (risiko tinggi), termostat menutup katup return dan menyalakan mode aman ($\lambda \downarrow$).

**Hubungan dengan Ising Hamiltonian:**
Parameter $\lambda$ endogen ini secara otomatis mengatur ulang kekuatan **Field Lokal ($h_i$)** terhadap **Kopling ($J_{ij}$)**. Tanpa campur tangan manusia, sirkuit kuantum Anda akan menyesuaikan "arah ukurannya" sendiri sesuai dengan iklim data yang masuk.

---

## 8. Kesimpulan
Dengan menggunakan fungsi sigmoid:
- Kita menghindari bias subjektif dalam memilih $\lambda$.
- Kita memberikan sifat **non-linear** yang lebih mirip dengan perilaku asli manusia.
- Kita memastikan bahwa sistem kuantum selalu memiliki skala energi yang konsisten.
