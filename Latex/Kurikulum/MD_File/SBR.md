# Catatan Riset: Sequential Best Response (SBR) dalam Optimasi Portofolio

## 1. Urgensi Eksplorasi: Mengapa SBR?

Dalam sistem ekonomi yang kompleks, jarang sekali ditemukan otoritas pusat yang secara diktator mengatur seluruh strategi pemain secara simultan. Sebaliknya, pasar sering kali beroperasi melalui interaksi desentralisasi, di mana setiap agen membuat keputusan berdasarkan informasi yang tersedia secara lokal. *Sequential Best Response* (SBR) adalah algoritma paling fundamental yang memodelkan perilaku ini.

SBR bertindak sebagai "jembatan algoritma" antara ekonomi dan fisika. Dalam ekonomi, ia merepresentasikan proses belajar agen yang berusaha memperbaiki posisinya. Dalam fisika, SBR setara dengan teknik *Greedy Search* atau *Local Optimization* yang sangat efisien untuk sistem yang memiliki fungsi potensial. Keuntungan utama SBR dalam *Exact Potential Game* (EPG) adalah kepastian konvergensi: karena setiap langkah individu dijamin meningkatkan fungsi potensial global (atau menurunkan energi sistem), algoritma ini pasti akan berhenti pada titik stasioner yang merupakan *Nash Equilibrium*.

### Aksioma & Intuisi "Best Response"
Secara matematis, sebuah strategi $x_i^*$ disebut sebagai *Best Response* bagi pemain $i$ jika ia memaksimalkan utilitas pribadinya $u_i$ terhadap strategi pemain lain $\mathbf{x}_{-i}$ yang sedang tetap. Kita mendefinisikan operator *Best Response* $\mathcal{B}_i$ sebagai:

$$x_i^* = \arg \max_{x_i \in \{0, 1\}} u_i(x_i, \mathbf{x}_{-i})$$


Di mana $x_i \in \{0, 1\}$ adalah pilihan strategi biner pemain $i$. 

**Intuisi Fisika:**
Bayangkan setiap aset sebagai partikel dengan *spin* yang merespons medan magnet efektif. Medan magnet ini dihasilkan oleh interaksi dengan partikel tetangganya (aset lain dalam portofolio). SBR adalah proses di mana satu per satu partikel meninjau medan di sekitarnya dan memutar *spin*-nya ke arah yang meminimalkan energi lokal. Fenomena ini identik dengan algoritma *Single-Spin Flip* pada simulasi Ising model di suhu nol ($T=0$), di mana sistem hanya bergerak menuju konfigurasi energi yang lebih rendah.

## 3. Protokol Algoritma (Step-by-Step)

Algoritma SBR beroperasi dalam lingkungan diskret di mana setiap pemain secara bergantian meninjau keputusannya. Berikut adalah langkah-langkah formal implementasi SBR dalam optimasi portofolio:

1.  **Inisialisasi:** Tentukan profil strategi awal $\mathbf{x}^{(0)} = (x_1, x_2, \dots, x_N)$. Biasanya dimulai dari kondisi acak atau portofolio kosong ($x_i=0, \forall i$).
2.  **Iterasi Sekuensial:** Untuk setiap pemain $i$ dari $1$ sampai $N$:
    *   Amati keputusan pemain lain $\mathbf{x}_{-i}$ saat ini.
    *   Hitung utilitas marginal untuk dua opsi: $u_i(1, \mathbf{x}_{-i})$ dan $u_i(0, \mathbf{x}_{-i})$.
    *   Pilih strategi $x_i^{(t+1)}$ yang memberikan utilitas lebih tinggi (*Best Response*).
3.  **Evaluasi Konvergensi:** Periksa apakah ada pemain yang masih ingin mengubah strateginya setelah satu putaran penuh ($1 \dots N$). Jika tidak ada perubahan, sistem telah mencapai *Nash Equilibrium*.
4.  **Terminasi:** Hentikan algoritma jika kondisi stasioner tercapai.

> **Kriteria Konvergensi:** Dalam *Potential Game*, fungsi potensial $\Phi(\mathbf{x})$ memiliki nilai maksimum yang terbatas dan strategi bersifat biner (finit). Karena setiap langkah SBR pasti menaikkan $\Phi(\mathbf{x})$ atau setidaknya menjaganya tetap, algoritma ini tidak mungkin terjebak dalam *looping* tanpa henti dan dijamin akan konvergen ke titik stasioner (lokal atau global).

## 4. Jembatan Logika: SBR vs. Hamiltonian Ising

Untuk menghubungkan SBR dengan Hamiltonian Ising ($H$), kita perlu membuktikan bahwa setiap peningkatan utilitas marginal agen sebanding dengan penurunan energi Hamiltonian. Berdasarkan definisi Hamiltonian dalam mekanika statistik, $H(\mathbf{x}) = -\Phi(\mathbf{x})$.

Jika pemain $i$ beralih dari $x_i=0$ ke $x_i=1$ karena $u_i(1, \mathbf{x}_{-i}) > u_i(0, \mathbf{x}_{-i})$, maka:

$$\Delta u_i = u_i(1, \mathbf{x}_{-i}) - u_i(0, \mathbf{x}_{-i}) > 0$$

Mengingat sifat *Exact Potential Game*:
$$\Phi(1, \mathbf{x}_{-i}) - \Phi(0, \mathbf{x}_{-i}) = \Delta u_i > 0$$

Maka perubahan energi Hamiltoniannya adalah:
$$\Delta H = H(1, \mathbf{x}_{-i}) - H(0, \mathbf{x}_{-i}) = -[\Phi(1, \mathbf{x}_{-i}) - \Phi(0, \mathbf{x}_{-i})] = -\Delta u_i$$

Karena $\Delta u_i > 0$, maka $\Delta H < 0$. Ini membuktikan bahwa setiap kali agen di pasar merasa lebih diuntungkan, sistem secara fisik mendingin menuju energi yang lebih rendah.

> **Visualisasi Perhitungan (Blok `>`):**
> Misalkan sistem 2-aset dengan $\mu_1 = 0.5$, $\sigma_{11} = 0.2$, $\gamma = 1$, dan $x_2=0$.
> 1. Jika Pemain 1 di luar ($x_1=0$): $u_1 = 0$
> 2. Jika Pemain 1 masuk ($x_1=1$): $u_1 = 0.5 - \frac{1}{2}(0.2) = 0.4$
> $\implies \Delta u_1 = 0.4 \implies \Delta H = -0.4$. Energi turun 0.4 unit.

## 5. Analogi "Physical Insight" & Verifikasi

Meskipun SBR dijamin konvergen dalam *Potential Game*, algoritma ini bersifat "serakah" (*greedy*). SBR hanya bergerak ke arah yang memberikan peningkatan utilitas segera, yang secara fisik setara dengan mencari lembah energi terdekat.

### Fenomena Metastabilitas & Local Minima
Dalam lanskap energi yang kompleks (seperti portofolio dengan banyak aset berkorelasi negatif), SBR sangat rentan terjebak dalam *local minima* (atau *local Nash Equilibrium*). Titik ini adalah konfigurasi di mana tidak ada satu pun agen yang dapat meningkatkan utilitasnya dengan berpindah strategi secara unilateral, namun secara kolektif ada konfigurasi lain yang memiliki energi jauh lebih rendah (*Global Nash Equilibrium*).

Secara fisik, ini disebut sebagai kondisi **Metastabilitas**. Untuk keluar dari jebakan ini, sistem klasik biasanya memerlukan "panas" (seperti pada *Simulated Annealing*) agar dapat melompati penghalang energi. Di sinilah algoritma kuantum memberikan keunggulan melalui mekanisme *Quantum Tunneling*.

### Tabel Perbandingan: SBR vs. Algoritma Variasional Kuantum

| Fitur | Sequential Best Response (SBR) | Variational Quantum Eigensolver (VQE) |
| :--- | :--- | :--- |
| **Mekanisme** | Klasik, Sekuensial, Deterministik | Kuantum, Paralel, Probabilistik |
| **Eksplorasi** | Terjebak di *local minima* | Mampu menembus penghalang via *tunneling* |
| **Skalabilitas** | Efisien untuk $N$ kecil-menengah | Potensial untuk $N$ besar (eksponensial state) |
| **Output** | Satu titik *Nash Equilibrium* | Distribusi probabilitas *ground state* |
| **Analogi Fisik** | *Zero-temperature quench* | *Adiabatic/Variational cooling* |

### Verifikasi & Parameter
Untuk memastikan konvergensi SBR yang stabil, parameter berikut harus diperhatikan:
1.  **Urutan Pembaruan:** Meskipun konvergensi dijamin, urutan pemain ($1 \dots N$ vs acak) dapat mempengaruhi *Nash Equilibrium* mana yang dicapai jika terdapat banyak NE.
2.  **Kondisi Awal:** Memulai dari "Empty Portfolio" ($x=0$) cenderung menghasilkan solusi yang lebih konservatif dibandingkan memulai dari "Full Portfolio" ($x=1$).
3.  **Koefisien $\gamma$:** Semakin besar $\gamma$, semakin "kasar" lanskap energinya, meningkatkan kemungkinan terjebak di *local minima*.
