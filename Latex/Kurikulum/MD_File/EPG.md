# Catatan Riset: Exact Potential Game (EPG) dalam Optimasi Portofolio

## 1. Urgensi Eksplorasi & Fondasi Teoretis

Dalam domain *Econophysics*, integrasi antara teori permainan dan mekanika statistik memberikan kerangka kerja yang kuat untuk memahami dinamika kolektif pasar. Penggunaan *Exact Potential Game* (EPG) bukan sekadar pilihan matematis, melainkan kebutuhan fundamental untuk merepresentasikan perilaku agen rasional ke dalam lanskap energi fisik. Dengan memetakan utilitas marginal agen ke dalam perubahan fungsi potensial global, kita dapat memastikan bahwa pencarian titik kesetimbangan pasar (*Nash Equilibrium*) setara dengan pencarian status energi terendah (*ground state*) dalam sistem fisik seperti model Ising.

Formalisme ini menjadi "jembatan logika" yang memungkinkan penggunaan algoritma kuantum seperti *Variational Quantum Eigensolver* (VQE) atau QAOA dalam domain ekonomi. Tanpa struktur EPG, tidak ada jaminan bahwa solusi optimal yang ditemukan oleh komputer kuantum secara fisik akan konsisten dengan insentif individual para pemain di pasar. Oleh karena itu, EPG bertindak sebagai protokol sinkronisasi yang menyelaraskan tujuan mikro (maksimalisasi keuntungan agen) dengan stabilitas makro (efisiensi portofolio sistemik).

### Aksioma & Intuisi EPG
Sistem pemilihan aset diklasifikasikan sebagai *Exact Potential Game* jika terdapat fungsi skalar global $\Phi(\mathbf{x})$ yang menangkap dampak perubahan strategi individu terhadap utilitas sistem secara presisi. Secara intuitif, bayangkan sebuah sistem partikel di mana setiap partikel (aset) berusaha menempati posisi energi terendah; dalam EPG, "keinginan" setiap partikel untuk berpindah posisi selalu sejalan dengan penurunan energi total sistem. Aksioma dasar EPG didefinisikan melalui relasi selisih utilitas marginal pemain $i$ dengan selisih nilai potensial global sebagai berikut (Monderer & Shapley, 1996):
$$\Phi(x_i, \mathbf{x}_{-i}) - \Phi(x'_i, \mathbf{x}_{-i}) = u_i(x_i, \mathbf{x}_{-i}) - u_i(x'_i, \mathbf{x}_{-i})$$

Di mana:
- $x_i$ adalah strategi aktif pemain $i$ (misal: "Masuk" ke portofolio, $x_i=1$).
- $x'_i$ adalah strategi alternatif (misal: "Keluar", $x_i=0$).
- $\mathbf{x}_{-i}$ merepresentasikan vektor strategi seluruh pemain selain $i$.
- $u_i$ adalah fungsi utilitas individual yang ingin dimaksimalkan oleh pemain $i$.

Identitas pada Persamaan (1) menjamin bahwa setiap peningkatan utilitas individu yang dilakukan secara otonom oleh seorang agen akan secara otomatis meningkatkan nilai fungsi potensial global $\Phi(\mathbf{x})$. Dalam konteks Hamiltonian Ising, ini berarti setiap penurunan energi lokal pada *spin* tertentu akan membawa sistem secara keseluruhan menuju konfigurasi *ground state* yang stabil.

## 2. Reduksionisme: Kasus Minimal 2-Pemain

Untuk memahami mekanisme EPG, mari kita tinjau sistem minimal yang terdiri dari dua aset (Pemain 1 dan Pemain 2). Dalam skenario ini, setiap pemain harus memutuskan apakah akan "Masuk" ($x_i = 1$) atau "Keluar" ($x_i = 0$) dari portofolio. Keputusan ini tidak diambil secara terisolasi; utilitas yang diperoleh Pemain 1 sangat bergantung pada apakah Pemain 2 juga memilih untuk masuk, terutama karena adanya korelasi risiko $\sigma_{12}$ yang membebani kedua belah pihak secara simetris.

Jembatan logika utama di sini adalah sifat simetri dari matriks kovariansi, di mana $\sigma_{12} = \sigma_{21}$. Simetri ini menjamin bahwa dampak marjinal Pemain 1 terhadap Pemain 2 sama persis dengan dampak marjinal Pemain 2 terhadap Pemain 1. Kesetaraan pengaruh timbal balik inilah yang memungkinkan terciptanya sebuah fungsi potensial global tunggal $\Phi(\mathbf{x})$ yang dapat mewakili seluruh "medan gaya" interaksi antar-agen dalam pasar.

### Matriks Payoff $(u_1, u_2)$
Struktur *payoff* di bawah ini menunjukkan bagaimana korelasi informasional mereduksi utilitas individual saat kedua aset dipilih secara simultan:

| Pemain 1 \ Pemain 2 | Keluar ($x_2 = 0$) | Masuk ($x_2 = 1$) |
| :--- | :--- | :--- |
| **Keluar ($x_1 = 0$)** | $(0, 0)$ | $(0, \mu_2 - \frac{\gamma}{2}\sigma_{22})$ |
| **Masuk ($x_1 = 1$)** | $(\mu_1 - \frac{\gamma}{2}\sigma_{11}, 0)$ | $(P_{11}, P_{22})$ |

> **Visualisasi Payoff $P_{11}$:**
> $P_{11} = \underbrace{\mu_1}_{\text{Profit}} - \underbrace{\frac{\gamma}{2} \sigma_{11}}_{\text{Self-Risk}} - \underbrace{\gamma \sigma_{12}}_{\text{Correlation Penalty}}$
>
> Penalti $\gamma \sigma_{12}$ muncul hanya jika kedua pemain memilih masuk ($x_1=1, x_2=1$), yang mencerminkan beban redundansi informasi dalam portofolio.

## 3. Derivasi "Scratchpad" & Formalisme Matematika

Untuk membuktikan bahwa model Markowitz adalah EPG, kita melakukan dekomposisi fungsi potensial global $\Phi(\mathbf{x})$ untuk mengisolasi kontribusi variabel keputusan $x_i$. Fungsi potensial awal didefinisikan sebagai fungsi utilitas total portofolio:

$$\Phi(\mathbf{x}) = \sum_{i=1}^N \mu_i x_i - \frac{\gamma}{2} \sum_{i=1}^N \sum_{j=1}^N \sigma_{ij} x_i x_j$$

Kita ekspansi suku sigma untuk memisahkan indeks $i$ yang sedang kita tinjau dari indeks lainnya $j \neq i$:

$$\Phi(\mathbf{x}) = \mu_i x_i - \frac{\gamma}{2} \left( \sigma_{ii} x_i^2 + 2 \sum_{j \neq i} \sigma_{ij} x_i x_j \right) + C_{-i}$$

Di mana $C_{-i}$ memuat seluruh komponen yang tidak mengandung variabel $x_i$. Mengingat properti peubah biner $x_i^2 = x_i$, kita dapat melakukan faktorisasi untuk mendapatkan relasi utilitas individual $u_i(x_i, \mathbf{x}_{-i})$ yang eksplisit:

$$\Phi(\mathbf{x}) = x_i \underbrace{\left( \mu_i - \frac{\gamma}{2} \sigma_{ii} - \gamma \sum_{j \neq i} \sigma_{ij} x_j \right)}_{u_i(x_i, \mathbf{x}_{-i})} + C_{-i}$$

> **Jembatan Logika Verifikasi:**
> Substitusikan nilai $x_i$:
> 1. Jika $x_i = 1 \implies \Phi(1, \mathbf{x}_{-i}) = u_i(1, \mathbf{x}_{-i}) + C_{-i}$
> 2. Jika $x_i = 0 \implies \Phi(0, \mathbf{x}_{-i}) = 0 + C_{-i}$
>
> Selisihnya: $\Phi(1, \mathbf{x}_{-i}) - \Phi(0, \mathbf{x}_{-i}) = u_i(1, \mathbf{x}_{-i})$, yang secara matematis membuktikan eksistensi fungsi potensial eksak sesuai definisi EPG.

## 4. Ekuivalensi Nash Equilibrium & Ground State

Keunggulan utama dari formulasi *Exact Potential Game* adalah kepastian konvergensi menuju *Nash Equilibrium* (NE) melalui proses maksimisasi fungsi potensial $\Phi(\mathbf{x})$. Dalam representasi mekanika statistik, ekuilibrium NE ini bersesuaian tepat dengan status *ground state* (energi terendah) dari Hamiltonian Ising. Dengan memetakan utilitas ke dalam lanskap energi, kita dapat memandang dinamika pasar sebagai proses stokastik di mana sistem berusaha mencari konfigurasi partikel yang paling stabil secara termodinamika.

Penyelarasan ini memberikan landasan matematis yang kokoh bagi penggunaan algoritma kuantum, karena menjamin bahwa solusi optimal secara global (minimum energi) juga merupakan titik kesetimbangan strategis yang stabil bagi seluruh partisipan pasar. Setiap penurunan energi dalam sistem Ising ekuivalen dengan peningkatan utilitas agen menuju ekuilibrium yang stabil. Oleh karena itu, fenomena *herding* atau sinkronisasi keputusan investor dapat dianalisis secara fisik sebagai transisi fase dalam sistem magnetik sintetis.

> **Physical Insight:**
> Proses *Best Response Dynamics* di mana agen mengubah strategi untuk meningkatkan utilitasnya setara dengan proses *Single-Spin Flip* pada algoritma Monte Carlo yang menurunkan energi sistem. Jika sistem mencapai *ground state*, tidak ada agen yang dapat meningkatkan utilitasnya secara unilateral, yang merupakan definisi eksak dari *Pure Strategy Nash Equilibrium*.

## 5. Integrasi Parameter Strategis & Verifikasi

Utilitas individual pemain $i$ didefinisikan dengan mengintegrasikan parameter imbal hasil strategis $\tilde{\mu}_i$ dan risiko interaksi yang telah dimodifikasi oleh korelasi informasional. Formulasi ini mencakup ekspektasi keuntungan personal, risiko varians individual, serta penalti akibat redundansi informasi dengan aset lain dalam portofolio:

$$u_i(x_i, \mathbf{x}_{-i}) = x_i \left( \tilde{\mu}_i - \frac{\gamma}{2} \sigma_{ii} - \gamma \sum_{j \neq i} \tilde{\sigma}_{ij} x_j \right)$$

Di mana $\gamma$ merupakan koefisien penghindaran risiko yang mengatur bobot relatif antara keuntungan dan volatilitas. Penggunaan $\tilde{\sigma}_{ij}$ (misal: *Mutual Information* atau *Non-linear Correlation*) memungkinkan model untuk menangkap struktur ketergantungan yang lebih kompleks daripada sekadar korelasi Pearson standar.

### Tabel Verifikasi Dampak Parameter
Berikut adalah ringkasan dampak fisik dan strategis dari variasi parameter dalam EPG:

| Parameter | Perubahan | Dampak Fisik (Hamiltonian) | Dampak Strategis (Pasar) |
| :--- | :--- | :--- | :--- |
| $\tilde{\mu}_i \uparrow$ | Kenaikan Imbal Hasil | Medan magnet eksternal $h_i$ menguat | Agen lebih cenderung "Masuk" (dominasi keuntungan) |
| $\gamma \uparrow$ | Penghindaran Risiko | Kopling interaksi $J_{ij}$ menguat | Diversifikasi meningkat (agen menghindari redundansi) |
| $\tilde{\sigma}_{ij} \uparrow$ | Korelasi Tinggi | Energi sistem naik jika *spin* paralel | Terjadi penalti utilitas jika aset dipilih bersamaan |
| $N \uparrow$ | Jumlah Aset | Dimensi Hilbert space membesar | Kompleksitas pencarian ekuilibrium meningkat |
