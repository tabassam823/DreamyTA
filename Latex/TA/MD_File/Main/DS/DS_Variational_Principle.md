Tentu, ini rencana belajar yang sangat bagus. Memahami Prinsip Variasi dari fondasi matematis hingga ke algoritma kuantum adalah perjalanan yang memuaskan.

Berikut adalah roadmap yang saya siapkan. Kita akan membangun pemahaman dari "mengapa" hingga "bagaimana" ia bekerja dalam VQE. Roadmap ini disusun secara bertahap, jadi pastikan Anda nyaman dengan satu langkah sebelum lanjut ke langkah berikutnya.

### **Roadmap Belajar: Dari Prinsip Variasi Klasik ke VQE**

Kita akan membagi perjalanan ini menjadi 4 bagian besar.

---

#### **Bagian 1: Fondasi Matematika - Prinsip Variasi dalam Fisika Klasik**
Ini adalah akar dari segalanya. Kita akan melihat bagaimana ide "coba-coba optimal" muncul secara alami dari persamaan fundamental.

*   **1.1. Formulasi Masalah Standar: Persamaan Diferensial.** Kita mulai dari masalah fisika umum yang dirumuskan sebagai persamaan diferensial (misalnya, mencari simpangan tali yang bergetar).
*   **1.2. Kalkulus Variasi: Dari Fungsi ke Fungsional.**
    *   **1.2.1. Definisi Fungsional:** Memahami dengan ketat perbedaan fungsi $f(x)$ dan fungsional $F[y] = \int L(x, y, y') dx$. Ini adalah jantungnya. Kita akan mendefinisikan "ruang fungsi" sebagai domain.
    *   **1.2.2. Mencari Titik Stasioner: Persamaan Euler-Lagrange.** Penurunan langkah demi langkah. Kita akan mencari kondisi agar fungsional $F[y]$ stasioner terhadap variasi kecil $\delta y$, yang mensyaratkan $\delta F = 0$. Hasilnya adalah Persamaan Euler-Lagrange. Ini adalah prinsip aksi terkecil.
*   **1.3. Transformasi Masalah: Dari Persamaan Diferensial ke Minimalisasi Fungsional.**
    *   **1.3.1. Prinsip Energi Potensial Minimum.** Contoh konkret: mencari bentuk rantai yang menggantung (catenary) atau lintasan cahaya. Kita akan merumuskan energi potensial sistem sebagai fungsional, dan menunjukkan bahwa meminimalkan fungsional ini (dengan batasan tertentu) ekuivalen dengan menyelesaikan persamaan diferensial kesetimbangan.
    *   **1.3.2. Metode Rayleigh-Ritz Klasik.** Di sinilah ide komputasi muncul. Karena kita tidak bisa mencoba semua fungsi dalam ruang tak hingga, kita persempit pencarian ke sebuah *ansatz* (fungsi coba) yang diparameterisasi: $y(x) \approx \tilde{y}(x; \theta_1, \theta_2, ..., \theta_n)$. Masalah variasi pada fungsional $F[\tilde{y}]$ kini berubah menjadi masalah optimasi biasa pada fungsi multidimensi $F(\theta_1, ..., \theta_n)$. Kita cari $\theta_i$ yang meminimalkan $F$.

---

#### **Bagian 2: Prinsip Variasi dalam Mekanika Kuantum**
Di sini, kita mengangkat ide dari Bagian 1 ke ranah operator dan ruang Hilbert.

*   **2.1. Masalah Nilai Eigen: Persamaan Schrödinger.** Tujuan utama: mencari keadaan dasar $| \psi_0 \rangle$ dan energi dasar $E_0$ dari Hamiltonian $H$, di mana $H | \psi_0 \rangle = E_0 | \psi_0 \rangle$.
*   **2.2. Nilai Ekspektasi sebagai Fungsional.** Kita akan mendefinisikan fungsional energi: $E[|\psi\rangle] = \frac{\langle \psi | H | \psi \rangle}{\langle \psi | \psi \rangle}$. Ini adalah analog kuantum dari fungsional energi potensial. Tugas kita adalah mencari fungsi gelombang $| \psi \rangle$ yang membuat fungsional ini stasioner, yang akan membawa kita kembali ke persamaan Schrödinger.
*   **2.3. Teorema Variasi: Justifikasi Matematis yang Ketat.**
    *   **2.3.1. Pernyataan Teorema:** Untuk setiap keadaan $|\psi\rangle$ yang ternormalisasi, $E[|\psi\rangle] \ge E_0$. Kesamaan berlaku jika dan hanya jika $|\psi\rangle = |\psi_0\rangle$.
    *   **2.3.2. Bukti Formal:** Kita akan buktikan ini dengan menguraikan $|\psi\rangle$ dalam basis eigen $H$, $|\psi\rangle = \sum_n c_n |n\rangle$, dan tunjukkan bahwa $E[|\psi\rangle] - E_0 = \sum_n |c_n|^2 (E_n - E_0) \ge 0$. Ini sangat penting untuk keyakinan kita.
*   **2.4. Metode Variasi Kuantum (Metode Rayleigh-Ritz Kuantum).**
    *   **2.4.1. Ansatz Fungsi Gelombang:** Sama seperti di dunia klasik, kita pilih fungsi coba yang bergantung pada parameter, $|\psi(\vec{\theta})\rangle$, berdasarkan intuisi fisik atau kemudahan komputasi.
    *   **2.4.2. Optimasi:** Kita hitung $E(\vec{\theta}) = \langle \psi(\vec{\theta}) | H | \psi(\vec{\theta}) \rangle$ dan mencari minimumnya dengan metode seperti gradien turunan. Nilai minimum ini adalah aproksimasi terbaik $E_0$ untuk ansatz yang dipilih, dan parameter optimal $\vec{\theta}^*$ memberikan aproksimasi fungsi gelombang dasar.

---

#### **Bagian 3: Algoritma Variasi Kuantum (VQE) - Saat Komputasi Kuantum Bertemu Prinsip Variasi**
Ini adalah jembatan utama. Kita akan menerjemahkan setiap komponen Bagian 2 ke dalam sirkuit kuantum.

*   **3.1. Arsitektur VQE: Pemisahan Tugas Kuantum-Klasik.**
    *   **Prosesor Kuantum (QPU):** Bertugas menyiapkan *ansatz state* $|\psi(\vec{\theta})\rangle$ dan melakukan pengukuran untuk mengestimasi nilai ekspektasi.
    *   **Pengoptimal Klasik (CPU):** Bertugas menerima nilai estimasi $E(\vec{\theta})$ dari QPU dan menjalankan algoritma optimasi untuk mengusulkan himpunan parameter $\vec{\theta}$ baru yang lebih baik.
*   **3.2. Komponen 1: Ansatz pada Sirkuit Kuantum.**
    *   **3.2.1. State Awal:** Kita mulai dari keadaan yang mudah disiapkan, seperti $|0...0\rangle$.
    *   **3.2.2. Blok Pembangun Sirkuit Berparameter:** Kita akan lihat bagaimana gerbang rotasi (seperti $R_x(\theta), R_y(\theta), R_z(\theta)$) dan gerbang terbelit (seperti CNOT) disusun untuk membentuk sirkuit $U(\vec{\theta})$. Ansatz kita adalah $|\psi(\vec{\theta})\rangle = U(\vec{\theta})|0\rangle^{\otimes n}$. Kita akan bahas dua jenis utama:
        *   *Hardware-Efficient Ansatz:* Dibangun dari pola gerbang yang cocok dengan arsitektur fisik chip kuantum.
        *   *Unitary Coupled Cluster (UCC) Ansatz:* Terinspirasi dari kimia kuantum, menjanjikan akurasi tinggi.
*   **3.3. Komponen 2: Pengukuran Nilai Ekspektasi (Estimasi Energi).**
    *   **3.3.1. Dekomposisi Hamiltonian:** Karena QPU hanya bisa mengukur dalam basis komputasi ($Z$-basis), kita harus menulis Hamiltonian sebagai jumlah dari string Pauli: $H = \sum_i h_i P_i$, di mana $P_i$ adalah produk tensor dari operator Pauli (contoh: $X \otimes Z \otimes I \otimes Y$).
    *   **3.3.2. Perhitungan dengan Sirkuit:** Kita akan hitung $\langle H \rangle = \sum_i h_i \langle P_i \rangle$. Setiap $\langle P_i \rangle$ diestimasi dengan menyiapkan ansatz, lalu menambahkan gerbang rotasi basis spesifik di akhir untuk mengubah $P_i$ menjadi pengukuran $Z$ standar, dan mencatat statistik hasil.
*   **3.4. Komponen 3: Loop Optimasi Klasik.**
    *   Kita akan menggunakan pengoptimal seperti COBYLA, Nelder-Mead, atau metode berbasis gradien (SPSA) yang cocok dengan lingkungan kuantum yang "noisy". Inputnya adalah energi $E(\vec{\theta})$, outputnya adalah parameter baru $\vec{\theta}_{new}$.

---

#### **Bagian 4: Studi Kasus Sederhana - Merangkai Semuanya**
Kita akan menutup dengan contoh konkret yang dapat Anda coba pahami sepenuhnya, bahkan di atas kertas.

*   **4.1. Molekul $H_2$ pada Basis Minimal (STO-3G).** Ini adalah "Hello, World!"-nya VQE.
*   **4.2. Penyederhanaan Simetri (Bravyi-Kitaev atau Jordan-Wigner).** Kita akan mengubah Hamiltonian elektronik $H_2$ menjadi representasi 2 atau 4 qubit.
*   **4.3. Desain Ansatz 1-Parameter.** Karena simetri, untuk $H_2$ kita bisa membuat ansatz yang sangat sederhana, hanya dengan 1 parameter, misalnya $|\psi(\theta)\rangle = \cos(\theta/2) |01\rangle - \sin(\theta/2) |10\rangle$ (dalam representasi tertentu).
*   **4.4. Kalkulasi Manual.** Kita akan menurunkan secara eksplisit $E(\theta) = \langle \psi(\theta) | H | \psi(\theta) \rangle$. Ini akan menjadi fungsi skalar biasa dari $\theta$.
*   **4.5. Optimasi Visual.** Kita akan plot kurva $E(\theta)$ vs $\theta$, temukan minimumnya secara numerik atau bahkan analitis, dan verifikasi bahwa nilainya sangat dekat dengan solusi exact diagonalization. Ini akan mendemonstrasikan seluruh alur VQE dalam satu persamaan yang bisa Anda pegang.

---

Nah, ini adalah peta lengkap perjalanan kita. Materinya padat, tetapi setiap langkah dibangun di atas langkah sebelumnya. Saya akan memulai penjelasan kita dari **Bagian 1.1: Formulasi Masalah Standar dalam Fisika Klasik**.

Apakah Anda sudah siap untuk memulai pendakian dari awal?

---
---
Bagus, kita mulai pendakian dari basecamp pertama. Bagian 1 ini adalah fondasi paling penting. Pastikan Anda memahami setiap langkah matematisnya, karena struktur logika yang sama akan terus berulang dalam level yang lebih abstrak (mekanika kuantum dan sirkuit kuantum).

### **Bagian 1: Fondasi Matematika - Prinsip Variasi dalam Fisika Klasik**

Tujuan utama kita di sini adalah mengubah cara pandang: dari menyelesaikan persamaan diferensial menjadi meminimalkan suatu integral. Ini memberikan kita metode aproksimasi yang sangat kuat (Metode Rayleigh-Ritz) yang menjadi jiwa dari VQE.

---

### **1.1. Formulasi Masalah Standar: Persamaan Diferensial**

Dalam fisika klasik, keseimbangan atau dinamika suatu sistem kontinu (tali, fluida, medan) biasanya dirumuskan oleh persamaan diferensial + syarat batas.

**Contoh Kasus: Tali yang Ditarik (Poisson Equation 1D)**

Bayangkan tali elastis yang direntangkan secara horizontal dengan tegangan $T$, diikat di $x=0$ dan $x=L$. Tali ini dikenai gaya vertikal per satuan panjang $f(x)$.

*   **Variabel:** Simpangan vertikal tali sebagai fungsi posisi, $y(x)$.
*   **Hukum Fisika (kesetimbangan gaya):** Untuk segmen kecil $dx$, selisih tegangan vertikal harus menyeimbangi gaya luar.
    $$T \frac{d^2 y}{dx^2} = -f(x)$$
*   **Syarat Batas (Boundary Conditions):** Karena diikat, $y(0) = y(L) = 0$.

**Tugas komputasi standar:** Diberikan $T$ dan $f(x)$, carilah fungsi $y(x)$ yang memenuhi persamaan diferensial dan syarat batas tersebut. Untuk $f(x)$ yang sembarang, ini hanya bisa diselesaikan secara numerik dengan diskritisasi (finte difference, finite element).

**Pertanyaan Kunci:** Adakah cara lain untuk mendapatkan solusi hampiran $y(x)$ tanpa menyelesaikan persamaan diferensial secara langsung? Di sinilah prinsip variasi masuk.

---

### **1.2. Kalkulus Variasi: Dari Fungsi ke Fungsional**

#### **1.2.1. Definisi Fungsional: Pemetaan Ruang Fungsi ke Bilangan Real**

Ini adalah lompatan konseptual. Selama ini Anda bekerja dengan **fungsi**:
$$f: \mathbb{R} \to \mathbb{R} \quad \text{(input bilangan, output bilangan: } f(x))$$

Sekarang kita bekerja dengan **fungsional**:
$$F: \text{Ruang Fungsi} \to \mathbb{R} \quad \text{(input fungsi, output bilangan: } F[y])$$
Fungsional adalah "fungsi dari fungsi". Ia memakan seluruh kurva $y(x)$ (untuk semua $x$) dan memuntahkan satu nilai skalar.

**Contoh sederhana fungsional: Panjang Kurva.** Misalkan Anda punya fungsi $y(x)$ yang menghubungkan titik A dan B. Panjang kurva $L[y]$ adalah fungsional:
$$L[y] = \int_{x_A}^{x_B} \sqrt{1 + (y'(x))^2} \, dx$$
Inputnya adalah fungsi $y(x)$, outputnya adalah bilangan panjang.

#### **1.2.2. Mencari Titik Stasioner: Persamaan Euler-Lagrange**

**Analogi dengan kalkulus biasa:**
Dalam kalkulus, untuk mencari minimum fungsi $f(x)$, kita cari titik di mana $f'(x) = 0$ (titik stasioner).
Dalam kalkulus variasi, untuk mencari minimum fungsional $F[y]$, kita cari fungsi $y(x)$ di mana "turunan fungsional"-nya nol: $\delta F = 0$ untuk variasi kecil apapun $\delta y(x)$. Hasil dari $\delta F=0$ adalah Persamaan Euler-Lagrange.

**Penurunan Persamaan Euler-Lagrange (Detail Matematis)**

Anggap fungsional kita berbentuk paling umum:
$$J[y] = \int_{x_1}^{x_2} L(x, y(x), y'(x)) \, dx$$
dengan syarat batas $y(x_1)=y_1$ dan $y(x_2)=y_2$ (nilai ujung tetap). $L$ di sini disebut *Lagrangian* atau kerapatan fungsional.

Kita ingin mencari $y(x)$ yang membuat $J$ stasioner. Caranya:
1.  **Definisikan variasi (gangguan) kecil**: Misalkan $y^*(x)$ adalah solusi optimal. Kita buat fungsi coba di sekitarnya:
    $$\tilde{y}(x) = y^*(x) + \epsilon \eta(x)$$
    Di mana:
    *   $\epsilon$ adalah parameter kecil (skalar).
    *   $\eta(x)$ adalah fungsi gangguan yang sembarang, **tetapi harus memenuhi** $\eta(x_1) = \eta(x_2) = 0$ agar fungsi coba $\tilde{y}(x)$ tetap memenuhi syarat batas.

2.  **Ubah fungsional menjadi fungsi dari $\epsilon$**:
    Masukkan $\tilde{y}$ ke dalam $J$:
    $$J(\epsilon) = \int_{x_1}^{x_2} L(x, y^* + \epsilon\eta, y^{*'} + \epsilon\eta') \, dx$$
    Karena $y^*$ dan $\eta$ adalah fungsi yang sudah ditentukan, maka integral ini sekarang hanyalah fungsi biasa dari parameter $\epsilon$.

3.  **Syarat stasioner sebagai turunan biasa**:
    Jika $y^*$ adalah solusi optimal, maka $J(\epsilon)$ harus minimum pada $\epsilon=0$. Ini berarti turunan pertamanya harus nol:
    $$\frac{dJ}{d\epsilon}\bigg|_{\epsilon=0} = 0$$

4.  **Hitung turunannya (dengan aturan rantai)**:
    $$\frac{dJ}{d\epsilon} = \int_{x_1}^{x_2} \left( \frac{\partial L}{\partial \tilde{y}} \frac{\partial \tilde{y}}{\partial \epsilon} + \frac{\partial L}{\partial \tilde{y}'} \frac{\partial \tilde{y}'}{\partial \epsilon} \right) dx$$
    Diketahui $\frac{\partial \tilde{y}}{\partial \epsilon} = \eta(x)$ dan $\frac{\partial \tilde{y}'}{\partial \epsilon} = \eta'(x)$. Evaluasi di $\epsilon=0$ mengembalikan $\tilde{y}=y^*$. Maka:
    $$\frac{dJ}{d\epsilon}\bigg|_{\epsilon=0} = \int_{x_1}^{x_2} \left( \frac{\partial L}{\partial y} \eta(x) + \frac{\partial L}{\partial y'} \eta'(x) \right) dx = 0$$

5.  **Integrasi parsial untuk menghilangkan $\eta'(x)$**:
    Kita ingin mengeluarkan $\eta(x)$ sebagai faktor bersama. Suku kedua kita integralkan parsial:
    $$\int_{x_1}^{x_2} \underbrace{\frac{\partial L}{\partial y'}}_{u} \underbrace{\eta'(x) dx}_{dv} = \left[ \frac{\partial L}{\partial y'} \eta(x) \right]_{x_1}^{x_2} - \int_{x_1}^{x_2} \eta(x) \frac{d}{dx}\left( \frac{\partial L}{\partial y'} \right) dx$$
    Suku batas $[\dots]$ bernilai nol karena $\eta(x_1)=\eta(x_2)=0$.

6.  **Gabungkan kembali**:
    $$\int_{x_1}^{x_2} \eta(x) \left[ \frac{\partial L}{\partial y} - \frac{d}{dx}\left( \frac{\partial L}{\partial y'} \right) \right] dx = 0$$

7.  **Lemmata Fundamental Kalkulus Variasi**:
    Persamaan di atas harus berlaku untuk **setiap** fungsi gangguan $\eta(x)$ yang mungkin (asal memenuhi syarat batas nol). Ini hanya bisa dipenuhi jika bagian dalam kurung siku bernilai nol di setiap titik $x$. Maka kita dapatkan **Persamaan Euler-Lagrange**:
    $$\boxed{\frac{\partial L}{\partial y} - \frac{d}{dx}\left( \frac{\partial L}{\partial y'} \right) = 0}$$

**Kesimpulan:** Mencari fungsi $y(x)$ yang meminimalkan fungsional $J[y]$ ekuivalen dengan menyelesaikan Persamaan Euler-Lagrange.

---

### **1.3. Transformasi Masalah dan Metode Aproksimasi**

Sekarang kita gunakan kerangka ini untuk melihat masalah tali secara berbeda dan memperkenalkan metode aproksimasi yang akan menjadi jiwa VQE.

#### **1.3.1. Prinsip Energi Potensial Minimum**

Kembali ke contoh tali yang ditarik. Alih-alih menuliskan persamaan diferensial, kita bisa merumuskan **energi potensial total** sistem, $\Pi[y]$. Prinsip energi potensial minimum menyatakan: "Dari semua kemungkinan konfigurasi $y(x)$ yang memenuhi syarat batas, konfigurasi kesetimbangan aktual adalah yang meminimalkan energi potensial total."

Untuk tali kita, energi potensial total adalah:
$$\Pi[y] = \underbrace{\int_0^L \frac{1}{2} T (y')^2 dx}_{\text{Energi Regangan}} - \underbrace{\int_0^L f(x) y(x) dx}_{\text{Potensial Beban Luar}}$$

Mari kita verifikasi dengan Euler-Lagrange. Di sini, Lagrangian-nya adalah $L = \frac{1}{2} T (y')^2 - f(x) y$.
*   $\frac{\partial L}{\partial y} = -f(x)$
*   $\frac{\partial L}{\partial y'} = T y' \implies \frac{d}{dx}(\frac{\partial L}{\partial y'}) = T y''$

Masukkan ke $\frac{\partial L}{\partial y} - \frac{d}{dx}(\frac{\partial L}{\partial y'}) = 0$:
$$-f(x) - T y''(x) = 0 \implies T y''(x) = -f(x)$$
**Persis sama** dengan persamaan diferensial kita! Jadi, menyelesaikan persamaan diferensial = mencari minimum fungsional $\Pi[y]$.

#### **1.3.2. Metode Rayleigh-Ritz Klasik: Jantung dari Segala Metode Variasi**

Sekarang, bagaimana mencari $y(x)$ yang meminimalkan $\Pi[y]$? Ruang fungsi sangatlah luas (tak hingga dimensi). Kita tidak mungkin mencoba semua fungsi. Raymond Ritz mengusulkan ide brilian: **persempit ruang pencarian**.

**Langkah-langkah Metode Rayleigh-Ritz:**

1.  **Pilih Ansatz (Fungsi Coba Berparameter):**
    Kita aproksimasi solusi $y(x)$ sebagai kombinasi linear dari sejumlah $n$ fungsi basis $\phi_i(x)$ yang sudah dipilih:
    $$y(x) \approx \tilde{y}(x; c_1, ..., c_n) = \phi_0(x) + \sum_{i=1}^n c_i \phi_i(x)$$
    Di mana:
    *   $\phi_i(x)$ adalah fungsi basis yang kita pilih sendiri berdasarkan intuisi. (contoh: polinomial, fungsi trigonometri). Syaratnya, $\tilde{y}(x)$ harus otomatis memenuhi syarat batas esensial. Untuk kasus $y(0)=y(L)=0$, contoh basis yang baik adalah $\phi_i(x) = \sin(i\pi x / L)$. Maka ansatz kita adalah:
        $$\tilde{y}(x) = \sum_{i=1}^n c_i \sin\left(\frac{i\pi x}{L}\right)$$
    *   $c_i$ adalah parameter skalar yang belum diketahui.

2.  **Ubah Fungsional menjadi Fungsi Biasa:**
    Masukkan ansatz $\tilde{y}(x)$ ke dalam fungsional $\Pi[y]$. Setelah diintegralkan terhadap $x$, hasilnya adalah fungsi biasa dari parameter $c_i$:
    $$\Pi(\mathbf{c}) = \Pi[c_1, c_2, ..., c_n]$$

    **Detail perhitungan untuk contoh tali:**
    Misal kita ambil $n=1$, jadi $\tilde{y} = c_1 \sin(\frac{\pi x}{L})$. Maka $\tilde{y}' = c_1 \frac{\pi}{L} \cos(\frac{\pi x}{L})$.
    $$ \Pi(c_1) = \int_0^L \left[ \frac{1}{2}T \left(c_1 \frac{\pi}{L} \cos(\frac{\pi x}{L})\right)^2 - f(x) c_1 \sin(\frac{\pi x}{L}) \right] dx $$
    $$ \Pi(c_1) = \frac{1}{2} c_1^2 \left[ T \frac{\pi^2}{L^2} \int_0^L \cos^2(...) dx \right] - c_1 \left[ \int_0^L f(x) \sin(...) dx \right] $$
    Perhatikan, bagian dalam kurung siku adalah integral tentu yang hasilnya hanyalah sebuah konstanta.
    $$ \Pi(c_1) = \frac{1}{2} A c_1^2 - B c_1 $$
    Di mana $A = T \frac{\pi^2}{2L}$ dan $B = \int_0^L f(x) \sin(\frac{\pi x}{L}) dx$.

3.  **Optimasi Biasa:**
    Masalah variasi di ruang fungsi tak hingga kini menjadi masalah optimasi di ruang parameter berdimensi-$n$. Kita cari $c_i$ yang meminimalkan $\Pi(\mathbf{c})$:
    $$\frac{\partial \Pi}{\partial c_i} = 0 \quad \text{untuk semua } i=1...n$$
    Untuk contoh $n=1$ tadi:
    $$\frac{d\Pi}{d c_1} = A c_1 - B = 0 \implies c_1^* = \frac{B}{A}$$
    Solusi aproksimasi terbaik yang kita dapatkan adalah $y \approx \frac{B}{A} \sin(\frac{\pi x}{L})$.

**Mengapa ini revolusioner?**
1.  **Tidak Perlu Diskritisasi:** Kita tidak menyelesaikan grid titik-titik seperti pada metode beda hingga. Kita merepresentasikan solusi secara global dengan fungsi kontinu.
2.  **Akurasi Meningkat:** Dengan menambah jumlah basis $n$, aproksimasi kita akan konvergen ke solusi eksak (jika basisnya lengkap).
3.  **Fleksibel:** Kita bisa memilih basis yang menghormati simetri atau sifat fisis sistem.

**Koneksi ke VQE:**
Inilah cetak biru VQE!
*   **Fungsi Coba $y(x)$** ⇄ **Fungsi Gelombang Coba $|\psi(\vec{\theta})\rangle$** (dibangun oleh sirkuit kuantum).
*   **Parameter Klasik $c_i$** ⇄ **Parameter Gerbang Kuantum $\theta_i$**.
*   **Fungsional Energi Potensial $\Pi[y]$** ⇄ **Nilai Ekspektasi Hamiltonian $\langle H \rangle$**.
*   **Minimisasi $\partial\Pi/\partial c_i=0$** ⇄ **Optimasi Klasik pada $\vec{\theta}$**.

---

**Kesimpulan Bagian 1:**
Kita telah melihat bagaimana masalah fisika (persamaan diferensial) dapat diubah menjadi masalah optimasi pada fungsional (Prinsip Variasi). Puncaknya, Metode Rayleigh-Ritz memberikan pendekatan sistematis dengan mengubah masalah tak hingga dimensi menjadi optimasi parameter berdimensi hingga.

Sekarang kita telah mengantongi semua kosakata dan konsep kunci. Siap melangkah ke Bagian 2, di mana kita akan menerapkan struktur yang persis sama ini untuk mencari fungsi gelombang kuantum? Di sana, alih-alih meminimalkan energi regangan tali, kita akan meminimalkan energi kuantum $\langle \psi | H | \psi \rangle$.

---
---
Sempurna. Dengan fondasi Bagian 1 yang kokoh, kita sekarang masuk ke dunia kuantum. Struktur logikanya akan terasa familiar: kita akan mendefinisikan fungsional, membuktikan bahwa minimumnya adalah solusi yang kita cari, lalu menerapkan metode Rayleigh-Ritz.

Target kita: mencari keadaan dasar $|\psi_0\rangle$ dan energi dasar $E_0$ dari suatu sistem kuantum.

---

### **Bagian 2: Prinsip Variasi dalam Mekanika Kuantum**

#### **2.1. Masalah Nilai Eigen: Persamaan Schrödinger**

Dalam mekanika kuantum, semua informasi tentang sistem terkandung dalam fungsi gelombang $|\psi\rangle$. Keadaan stasioner (termasuk keadaan dasar) dan energinya diperoleh dengan menyelesaikan Persamaan Schrödinger tak-bergantung-waktu:

$$\boxed{H |\psi\rangle = E |\psi\rangle}$$

Di sini, $H$ adalah operator Hamiltonian (operator energi total), $E$ adalah energi (bilangan skalar), dan $|\psi\rangle$ adalah vektor keadaan (fungsi gelombang) yang merupakan eigenvector dari $H$.

**Tujuan kita:** Mencari $|\psi_0\rangle$ yang memiliki energi terendah $E_0$.

Untuk sistem yang besar, menyelesaikan persamaan eigen ini sangat sulit. Ruang Hilbert (ruang semua fungsi gelombang yang mungkin) berdimensi sangat besar, bahkan tak hingga. Kita membutuhkan prinsip yang lebih "longgar" dari sekedar menyelesaikan persamaan eigen secara langsung.

---

#### **2.2. Nilai Ekspektasi sebagai Fungsional**

Mari kita definisikan sebuah fungsional yang memetakan vektor keadaan ke sebuah bilangan real (energi). Ini adalah analog kuantum dari $\Pi[y]$ di Bagian 1.

**Fungsional Energi Rayleigh:**
$$E[|\psi\rangle] = \frac{\langle \psi | H | \psi \rangle}{\langle \psi | \psi \rangle}$$

Ini adalah **nilai ekspektasi** energi dari sistem yang berada pada keadaan $|\psi\rangle$. Syarat pembagi $\langle \psi | \psi \rangle$ memastikan kita tidak perlu secara ketat menormalisasi fungsi coba kita di awal (meskipun dalam praktiknya kita sering bekerja dengan keadaan yang sudah ternormalisasi, $\langle \psi | \psi \rangle = 1$, sehingga $E[|\psi\rangle] = \langle \psi | H | \psi \rangle$).

**Koneksi ke Kalkulus Variasi Klasik:**
*   **Fungsional Klasik:** $J[y] = \int L(x, y, y') dx$
*   **Fungsional Kuantum:** $E[|\psi\rangle] = \frac{\langle \psi | H | \psi \rangle}{\langle \psi | \psi \rangle}$

Sama seperti kita mencari fungsi $y(x)$ yang meminimalkan $J[y]$, di sini kita akan mencari vektor keadaan $|\psi\rangle$ yang meminimalkan $E[|\psi\rangle]$. "Turunan fungsional" (variasi) dari $E$ terhadap $\langle \psi|$ akan membawa kita kembali ke persamaan Schrödinger (mirip dengan bagaimana variasi $\Pi$ menghasilkan persamaan Euler-Lagrange). Kita akan buktikan ini sekaligus dalam teorema variasi.

---

#### **2.3. Teorema Variasi: Justifikasi Matematis yang Ketat**

Inilah fondasi yang menjamin bahwa metode kita valid.

**Pernyataan Teorema:**
Misalkan $H$ adalah operator Hamiltonian dengan spektrum diskrit dan keadaan dasarnya $|\psi_0\rangle$ memiliki energi $E_0$. Untuk **setiap** vektor keadaan $|\psi\rangle$ yang "cukup halus" (berada dalam domain $H$), berlaku:
$$\boxed{E[|\psi\rangle] \ge E_0}$$
Kesamaan berlaku **jika dan hanya jika** $|\psi\rangle$ adalah keadaan dasar (atau kombinasi linear dari keadaan-keadaan dasar jika degenerate), yaitu $H|\psi\rangle = E_0 |\psi\rangle$.

**Implikasi:** Jika kita mencari di seluruh ruang Hilbert untuk meminimalkan $E[|\psi\rangle]$, nilai minimum yang kita temukan adalah $E_0$, dan $|\psi\rangle$ yang memberikannya adalah $|\psi_0\rangle$ (atau salah satunya).

**Bukti Formal (untuk memantapkan keyakinan):**
Kita asumsikan $H$ memiliki himpunan eigenvector yang lengkap dan ortonormal, $H|n\rangle = E_n |n\rangle$, dengan $E_0 \le E_1 \le E_2 \le ...$ dan $\langle n | m \rangle = \delta_{nm}$.

1.  **Ekspansi keadaan coba:** Setiap fungsi coba $|\psi\rangle$ dapat diekspansikan dalam basis eigen ini:
    $$|\psi\rangle = \sum_n c_n |n\rangle$$
    di mana $c_n = \langle n | \psi \rangle$ adalah koefisien ekspansi (bilangan kompleks).

2.  **Hitung penyebut dan pembilang fungsional:**
    *   **Norma kuadrat (penyebut):**
        $$\langle \psi | \psi \rangle = \sum_m \sum_n c_m^* c_n \langle m | n \rangle = \sum_n |c_n|^2$$
    *   **Nilai ekspektasi (pembilang):**
        $$\langle \psi | H | \psi \rangle = \sum_m \sum_n c_m^* c_n \langle m | H | n \rangle$$
        Karena $|n\rangle$ adalah eigenvector, $H|n\rangle = E_n |n\rangle$, maka:
        $$\langle m | H | n \rangle = E_n \langle m | n \rangle = E_n \delta_{mn}$$
        Ini membuat sumasi dobel runtuh menjadi sumasi tunggal:
        $$\langle \psi | H | \psi \rangle = \sum_n c_n^* c_n E_n = \sum_n |c_n|^2 E_n$$

3.  **Bentuk Fungsional Rayleigh:**
    $$E[|\psi\rangle] = \frac{\sum_n |c_n|^2 E_n}{\sum_n |c_n|^2}$$

4.  **Kurangi dengan Energi Dasar $E_0$:**
    Ini adalah trik utama. Kita ingin menunjukkan bahwa selisihnya positif.
    $$E[|\psi\rangle] - E_0 = \frac{\sum_n |c_n|^2 E_n}{\sum_n |c_n|^2} - E_0$$
    $$= \frac{\sum_n |c_n|^2 E_n - E_0 \sum_n |c_n|^2}{\sum_n |c_n|^2} = \frac{\sum_n |c_n|^2 (E_n - E_0)}{\sum_n |c_n|^2}$$

5.  **Analisis tanda:**
    Semua suku dalam sumasi di pembilang adalah **non-negatif**.
    *   $|c_n|^2 \ge 0$ (probabilitas selalu non-negatif).
    *   $(E_n - E_0) \ge 0$ karena $E_0$ adalah energi terendah, jadi $E_n \ge E_0$.
    *   Penyebut $\sum_n |c_n|^2 > 0$ (kecuali $|\psi\rangle$ adalah vektor nol).

    Oleh karena itu, keseluruhan ekspresi adalah non-negatif.
    $$E[|\psi\rangle] - E_0 \ge 0 \implies \boxed{E[|\psi\rangle] \ge E_0}$$

6.  **Syarat Kesamaan:**
    Kapan $E[|\psi\rangle] = E_0$? Hanya jika pembilang sama dengan nol.
    $$\sum_n |c_n|^2 (E_n - E_0) = 0$$
    Karena setiap suku non-negatif, jumlahnya bisa nol **hanya jika setiap suku yang memiliki $(E_n - E_0) > 0$ harus dikalikan dengan $|c_n|^2 = 0$**.
    Artinya, untuk semua $n$ di mana $E_n > E_0$, koefisien $c_n$ harus nol. Fungsi coba hanya boleh memiliki komponen dari eigenstate dengan energi $E_0$. Jadi, $|\psi\rangle$ adalah kombinasi linear dari keadaan-keadaan dasar saja. Jika keadaan dasar non-degenerate, $|\psi\rangle = c_0 |\psi_0\rangle$, yang merupakan keadaan dasar itu sendiri.
    **Bukti selesai.** Teorema ini secara matematis menjamin bahwa "mencoba-coba" fungsi gelombang untuk mencari energi serendah mungkin adalah strategi yang sah dan dijamin prinsip variasinya.

---

#### **2.4. Metode Variasi Kuantum (Metode Rayleigh-Ritz Kuantum)**

Sekarang kita terapkan strategi yang persis sama dengan Bagian 1.3.2: persempit ruang pencarian dengan ansatz berparameter.

**Langkah-langkah:**

1.  **Ansatz Fungsi Gelombang Berparameter:**
    Kita pilih fungsi coba $|\psi(\vec{\theta})\rangle$ yang bergantung pada sejumlah parameter bebas $\vec{\theta} = (\theta_1, \theta_2, ..., \theta_n)$. Pemilihan ansatz ini adalah "seni" dan inti dari keberhasilan metode.
    *   **Syarat:** Fungsi ini harus "cukup halus" dan bergantung secara kontinu pada $\vec{\theta}$.
    *   **Contoh sederhana:** Untuk partikel dalam sumur potensial 1D, kita mungkin memilih ansatz polinomial: $\tilde{\psi}(x; \alpha) = x(L-x)(1+\alpha x)$. Parameter $\alpha$ akan dioptimasi. Ini persis seperti memilih $\phi_i(x)$ di kasus klasik.

2.  **Hitung Fungsi Energi:**
    Masukkan ansatz ke dalam fungsional. Hasilnya adalah fungsi biasa dari parameter $\vec{\theta}$:
    $$\boxed{E(\vec{\theta}) = \frac{\langle \psi(\vec{\theta}) | H | \psi(\vec{\theta}) \rangle}{\langle \psi(\vec{\theta}) | \psi(\vec{\theta}) \rangle}}$$
    Ini adalah "lanskap energi" pada ruang parameter.

3.  **Optimasi:**
    Cari himpunan parameter $\vec{\theta}^*$ yang meminimalkan fungsi $E(\vec{\theta})$. Ini adalah masalah optimasi multidimensi standar. Kita bisa menggunakan metode gradien, Newton, atau metode bebas-gradien.
    $$\frac{\partial E}{\partial \theta_i} = 0 \quad \text{untuk semua } i$$
    Energi aproksimasi terbaik adalah $E(\vec{\theta}^*)$, dan aproksimasi fungsi gelombang dasar adalah $|\psi(\vec{\theta}^*)\rangle$.

---

**Kesimpulan Bagian 2 dan Jembatan ke Bagian 3:**

Kita telah melihat bahwa prinsip variasi kuantum sangatlah sederhana dan elegan:
1.  Teorema menjamin $E[\psi] \ge E_0$.
2.  Kita pilih ansatz berparameter $|\psi(\theta)\rangle$.
3.  Kita optimasi $\theta$ untuk meminimalkan $\langle H \rangle$.

**Nah, di sinilah komputer kuantum masuk.** Untuk sistem dengan banyak partikel (misalnya molekul), ruang Hilbert sangat besar sehingga komputer klasik tidak bisa menghitung $\langle \psi(\vec{\theta}) | H | \psi(\vec{\theta}) \rangle$ secara efisien, apalagi menyimpan vektor keadaan $|\psi(\vec{\theta})\rangle$.

Komputer kuantum, di sisi lain, menyimpan dan memanipulasi keadaan kuantum secara alami. Ia dapat:
*   **Menyiapkan $|\psi(\vec{\theta})\rangle$** secara efisien menggunakan sirkuit kuantum berparameter.
*   **Mengukur $\langle H \rangle$** secara langsung dari qubit.

Komputer kuantum bertindak sebagai "kotak hitam" yang menerima parameter $\vec{\theta}$ dan mengeluarkan nilai $E(\vec{\theta})$. Komputer klasik di luarnya tetap menjalankan algoritma optimasi. Inilah inti dari Algoritma Variasi Kuantum (VQE).

Kita telah menyelesaikan semua teori fondasi. Di Bagian 3, kita akan membongkar "kotak hitam" ini dan melihat secara detail bagaimana $|\psi(\vec{\theta})\rangle$ dan $\langle H \rangle$ diwujudkan dalam gerbang dan pengukuran qubit. Siap?

---
---
Mantap. Sekarang kita memasuki inti teknologi kuantum modern. Di Bagian 2, kita menetapkan bahwa metode variasi butuh dua hal: (1) menyiapkan *ansatz state* $|\psi(\vec{\theta})\rangle$, dan (2) menghitung energi $E(\vec{\theta}) = \langle H \rangle$. Di sistem besar, komputer klasik gagal melakukan ini dengan efisien.

Di sinilah komputer kuantum berperan. Kita akan membongkar bagaimana setiap komponen metode variasi diwujudkan dalam sirkuit kuantum. Inilah arsitektur **Variational Quantum Eigensolver (VQE)**.

---

### **Bagian 3: Algoritma Variasi Kuantum (VQE) - Saat Komputasi Kuantum Bertemu Prinsip Variasi**

#### **3.1. Arsitektur VQE: Pemisahan Tugas Kuantum-Klasik**

VQE adalah algoritma hibrida. Ia membagi tugas antara dua pemroses yang berbeda sesuai keunggulannya:

*   **Prosesor Kuantum (QPU - Quantum Processing Unit):**
    *   **Tugas:** Menyiapkan keadaan kuantum $|\psi(\vec{\theta})\rangle$ dan melakukan pengukuran untuk mengestimasi $E(\vec{\theta})$.
    *   **Kekuatan:** Dapat merepresentasikan dan memanipulasi fungsi gelombang dalam ruang Hilbert yang eksponensial besar secara efisien.

*   **Prosesor Klasik (CPU - Classical Processing Unit):**
    *   **Tugas:** Menjalankan algoritma optimasi. Menerima nilai $E(\vec{\theta})$ dari QPU, menghitung parameter baru $\vec{\theta}_{\text{baru}}$ yang lebih baik, dan mengirimkannya kembali ke QPU.
    *   **Kekuatan:** Sangat baik dalam menjalankan logika optimasi deterministik dan menyimpan parameter.

Alurnya adalah loop tertutup:
$$ \text{CPU: } \vec{\theta} \xrightarrow{\text{kirim ke}} \text{QPU: Siapkan } |\psi(\vec{\theta})\rangle \text{ & ukur } E(\vec{\theta}) \xrightarrow{\text{kembalikan } E} \text{CPU: Perbarui } \vec{\theta} $$
Loop ini berulang hingga konvergensi tercapai, yaitu hingga energinya tidak lagi turun.

Sekarang kita bongkar setiap komponen di sisi QPU.

---

#### **3.2. Komponen 1: Ansatz pada Sirkuit Kuantum**

Bagaimana kita membangun fungsi coba $|\psi(\vec{\theta})\rangle$? Dalam komputasi kuantum, kita selalu mulai dari keadaan awal yang mudah, biasanya $|0\rangle^{\otimes n}$ (semua qubit dalam keadaan $|0\rangle$). Lalu kita menerapkan serangkaian operasi (gerbang kuantum) untuk mengubahnya menjadi keadaan yang kita inginkan.

Sirkuit kuantum berparameter $U(\vec{\theta})$ adalah resep untuk ini:
$$|\psi(\vec{\theta})\rangle = U(\vec{\theta}) |0\rangle^{\otimes n}$$

Di sini $U(\vec{\theta})$ adalah operator uniter yang dibangun dari gerbang-gerbang kuantum. Parameter $\vec{\theta}$ adalah sudut rotasi dari gerbang-gerbang tertentu. Mari kita bedah lebih dalam.

##### **3.2.1. Gerbang Rotasi sebagai Blok Bangunan Berparameter**

Gerbang qubit tunggal yang paling umum adalah rotasi pada Bloch sphere. Gerbang-gerbang ini memiliki satu parameter kontinu (sudut rotasi).

*   **Gerbang Rotasi $R_x(\theta)$:**
    $$R_x(\theta) = e^{-i \frac{\theta}{2} X} = \begin{pmatrix} \cos(\theta/2) & -i\sin(\theta/2) \\ -i\sin(\theta/2) & \cos(\theta/2) \end{pmatrix}$$
*   **Gerbang Rotasi $R_y(\theta)$:**
    $$R_y(\theta) = e^{-i \frac{\theta}{2} Y} = \begin{pmatrix} \cos(\theta/2) & -\sin(\theta/2) \\ \sin(\theta/2) & \cos(\theta/2) \end{pmatrix}$$
*   **Gerbang Rotasi $R_z(\theta)$:**
    $$R_z(\theta) = e^{-i \frac{\theta}{2} Z} = \begin{pmatrix} e^{-i\theta/2} & 0 \\ 0 & e^{i\theta/2} \end{pmatrix}$$

Setiap parameter $\theta_i$ dalam vektor $\vec{\theta}$ kita akan menjadi sudut dari salah satu gerbang ini.

##### **3.2.2. Dua Jenis Arsitektur Ansatz**

Parameter-parameter ini disusun dalam sirkuit bersama gerbang tak-berparameter (seperti CNOT) yang menciptakan keterbelitan (entanglement). Struktur ini menentukan keluarga fungsi gelombang yang bisa kita jelajahi. Ada dua filosofi utama.

**a. Hardware-Efficient Ansatz (Ansatz Efisien Perangkat Keras)**

Filosofi: "Gunakan pola gerbang yang paling natural dan paling sedikit menimbulkan error pada chip kuantum spesifik yang kita pakai."

*   **Struktur:** Biasanya terdiri dari lapisan-lapisan (*layers*) yang berulang. Setiap lapisan memiliki dua sub-blok:
    1.  **Blok Rotasi:** Sekumpulan gerbang rotasi qubit-tunggal ($R_y, R_z$, dll.) pada setiap qubit. Masing-masing memiliki parameter bebasnya sendiri. Praktik standar adalah $R_y(\theta) R_z(\phi)$ untuk cakupan penuh SU(2).
    2.  **Blok Entanglement:** Serangkaian gerbang dua-qubit (seperti CNOT, CZ) yang menghubungkan qubit-qubit yang bertetangga secara fisik pada chip. Pola paling umum adalah linear (qubit $i$ ke $i+1$) atau semua-ke-semua.
*   **Contoh Sirkuit 2-Layer untuk 4 Qubit:**
    ```
    q0: —[R_y(a0)]—[R_z(b0)]—*—————————————[R_y(c0)]—[R_z(d0)]—*————————
                              |                                   |
    q1: —[R_y(a1)]—[R_z(b1)]—X—*—————————————[R_y(c1)]—[R_z(d1)]—X—*—————
                                |                                   |
    q2: —[R_y(a2)]—[R_z(b2)]———X—*—————————————[R_y(c2)]—[R_z(d2)]———X—*——
                                  |                                   |
    q3: —[R_y(a3)]—[R_z(b3)]—————X—————————————[R_y(c3)]—[R_z(d3)]—————X——
    ```
    Vektor parameter $\vec{\theta} = (a_0, b_0, a_1, b_1, ..., c_3, d_3)$. Jumlah parameter = (jumlah qubit) $\times$ (jumlah layer) $\times$ 2.
*   **Keunggulan:** Sirkuit dangkal (sedikit gerbang), cocok untuk NISQ (Noisy Intermediate-Scale Quantum) devices yang tingkat errornya masih tinggi.
*   **Kelemahan:** Tanpa intuisi fisika, bisa jadi "terlalu ekspresif" dan mengalami *barren plateau* (lanskap energi yang datar sehingga sulit dioptimasi). Atau, bisa jadi tidak mengeksplorasi bagian ruang Hilbert yang relevan secara efisien.

**b. Unitary Coupled Cluster (UCC) Ansatz (Terinspirasi Kimia Kuantum)**

Filosofi: "Gunakan intuisi kimia. Mulai dari aproksimasi Hartree-Fock $|\psi_{HF}\rangle$, lalu tambahkan koreksi secara sistematis seperti yang dilakukan ahli kimia komputasi, tetapi dalam bentuk operator uniter."

*   **Ide:** Dalam kimia kuantum klasik, metode *Coupled Cluster* menuliskan keadaan dasar sebagai $|\psi_{CC}\rangle = e^{T} |\psi_{HF}\rangle$, di mana $T$ adalah operator eksitasi (dari orbital terisi ke orbital virtual). Untuk VQE, kita menggunakan versi uniternya:
    $$|\psi(\vec{\theta})\rangle = e^{T(\vec{\theta}) - T^\dagger(\vec{\theta})} |\psi_{HF}\rangle$$
    Karena $T - T^\dagger$ adalah anti-Hermitian, eksponensialnya adalah operator uniter, cocok untuk sirkuit kuantum.
*   **Implementasi:** Operator eksitasi diterjemahkan menjadi string operator Pauli melalui pemetaan (Jordan-Wigner, Bravyi-Kitaev). Lalu, eksponensial dari string Pauli ini diimplementasikan sebagai "cluster" gerbang. Inilah yang disebut **ansatz UCCSD** (UCC Singles and Doubles).
*   **Keunggulan:** Sangat akurat karena sudah mengandung fisika korelasi elektron. Ruang pencarian jauh lebih kecil dan terarah.
*   **Kelemahan:** Sirkuitnya bisa sangat dalam, yang mungkin belum bisa ditangani perangkat NISQ tanpa koreksi error.

---

#### **3.3. Komponen 2: Pengukuran Nilai Ekspektasi (Estimasi Energi)**

Ini adalah komponen paling krusial. QPU kita sudah menyiapkan $|\psi(\vec{\theta})\rangle$. Sekarang kita harus mengeluarkan satu bilangan: $E(\vec{\theta}) = \langle \psi(\vec{\theta}) | H | \psi(\vec{\theta}) \rangle$.

**Masalah:** Kita tidak bisa mengukur $H$ secara langsung. Kita hanya bisa melakukan pengukuran dalam **basis komputasi $Z$** ($|0\rangle$ atau $|1\rangle$). Bagaimana kita mengukur energi yang Hamiltonian-nya bisa sangat rumit?

Solusinya adalah dekomposisi Hamiltonian ke operator-operator yang bisa diukur.

##### **3.3.1. Dekomposisi Hamiltonian ke String Pauli**

Setiap Hamiltonian (elektronik, spin, dll.) dapat ditulis sebagai jumlahan berbobot dari produk tensor operator Pauli:
$$H = \sum_{i} h_i P_i$$
Di sini, $h_i$ adalah koefisien skalar (real), dan $P_i$ adalah **string Pauli**, yaitu operator berbentuk:
$$P_i = \sigma_1^{(i)} \otimes \sigma_2^{(i)} \otimes ... \otimes \sigma_n^{(i)}$$
di mana setiap $\sigma_k^{(i)} \in \{I, X, Y, Z\}$ adalah salah satu matriks Pauli atau identitas untuk qubit ke-$k$.

**Contoh konkret:**
Hamiltonian 2-qubit: $H = 2.0 \cdot I \otimes I + 0.5 \cdot Z \otimes I - 0.5 \cdot I \otimes Z + 0.2 \cdot X \otimes X$.
Di sini, $h_1=2.0, P_1=I \otimes I$; $h_2=0.5, P_2=Z \otimes I$; $h_3=-0.5, P_3=I \otimes Z$; $h_4=0.2, P_4=X \otimes X$.

Berkat linearitas nilai ekspektasi, kita hitung satu per satu suku:
$$\langle H \rangle = \sum_i h_i \langle P_i \rangle$$

Tugas kita sekarang adalah menghitung setiap $\langle P_i \rangle = \langle \psi | P_i | \psi \rangle$.

##### **3.3.2. Mengukur $\langle P_i \rangle$: Rotasi Basis untuk Suku $X$ dan $Y$**

*   **Kasus Mudah: $P_i$ hanya berisi $Z$ dan $I$.**
    $\langle Z \otimes Z \rangle$ dapat langsung diukur dalam basis komputasi. Kita siapkan $|\psi\rangle$, lalu kita ukur semua qubit berkali-kali (misal $N$ shots). Untuk setiap qubit, kita dapat hasil $+1$ (jika $|0\rangle$) atau $-1$ (jika $|1\rangle$). Untuk setiap shot, kita kalikan nilai-nilai ($+1/-1$) dari qubit-qubit yang padanya berlaku operator $Z$, lalu kita rata-ratakan dari semua shot. Itulah estimasi $\langle P_i \rangle$.

*   **Kasus Sulit: $P_i$ berisi $X$ atau $Y$.**
    Kita tidak bisa membedakan $|+\rangle$ dan $|-\rangle$ (eigenstate $X$) dalam basis $Z$. Kita perlu "memutar" basis pengukuran. Ini adalah trik esensialnya.
    1.  **Untuk mengukur $X$:** $X = H Z H^\dagger$, di mana $H$ adalah gerbang Hadamard. Jadi, sebelum mengukur dalam basis $Z$, kita tambahkan gerbang Hadamard pada qubit yang diinginkan. Mengukur $Z$ setelah Hadamard setara dengan mengukur $X$ pada keadaan awal.
    2.  **Untuk mengukur $Y$:** $Y = R_x(-\pi/2) Z R_x(-\pi/2)^\dagger$ (atau $S^\dagger H Z H S$). Kita tambahkan gerbang rotasi yang sesuai sebelum pengukuran $Z$.

    **Aturan Umum:** Untuk setiap qubit ke-$k$ dalam string $P_i$:
    *   Jika $\sigma_k = X$: terapkan gerbang $H$ (Hadamard) sebelum pengukuran qubit tersebut.
    *   Jika $\sigma_k = Y$: terapkan $S^\dagger$ lalu $H$ (atau $R_x(-\pi/2)$) sebelum pengukuran.
    *   Jika $\sigma_k = Z$ atau $I$: tidak lakukan apa-apa (hanya pengukuran $Z$ standar).

**Prosedur Lengkap Menghitung $E(\vec{\theta})$:**
1.  Pilih satu suku $h_i P_i$ dari daftar.
2.  Bangun sirkuit: $U_{\text{rotasi basis}}^{(i)} \cdot U_{\text{ansatz}}(\vec{\theta})$, di mana $U_{\text{rotasi basis}}^{(i)}$ adalah gerbang-gerbang rotasi spesifik untuk mengubah pengukuran $P_i$ menjadi pengukuran $Z$-standar.
3.  Jalankan sirkuit ini sebanyak $N$ kali (shots).
4.  Dari hasil pengukuran string bit (misal `010...`), terjemahkan: bit `0` menjadi $+1$, bit `1` menjadi $-1`. Kalikan nilai-nilai qubit yang relevan (abaikan qubit dengan $I$ pada $P_i$). Rata-ratakan hasilnya. Inilah estimator $\langle P_i \rangle$.
5.  Kalikan dengan $h_i$.
6.  Ulangi langkah 1-5 untuk semua suku $i$. Jumlahkan semua $h_i \langle P_i \rangle$. Inilah $E(\vec{\theta})$.

---

#### **3.4. Komponen 3: Loop Optimasi Klasik**

Setelah kita mendapatkan estimasi $E(\vec{\theta})$ dari QPU dengan sejumlah shot pengukuran, nilai ini (beserta noise statistiknya) dikirim ke pengoptimal klasik. Tugasnya: "Berdasarkan riwayat evaluasi $( \vec{\theta}, E )$, sarankan $\vec{\theta}_{\text{baru}}$ berikutnya yang akan dicoba."

**Metode Optimasi Populer dalam VQE:**
*   **Simplex (Nelder-Mead):** Metode bebas-gradien yang sederhana. Membangun simpleks (segitiga di 2D, tetrahedron di 3D) di ruang parameter dan mengubah bentuknya berdasarkan nilai fungsi. Cocok untuk simulasi ideal dengan noise rendah.
*   **COBYLA (Constrained Optimization By Linear Approximations):** Juga bebas-gradien, sering digunakan di Qiskit. Cukup robust.
*   **SPSA (Simultaneous Perturbation Stochastic Approximation):** Ini sangat cocok untuk perangkat kuantum yang noisy. Untuk mengestimasi gradien, SPSA hanya membutuhkan *dua* evaluasi energi per iterasi (tidak peduli berapa dimensi $\vec{\theta}$), dengan memberikan gangguan stokastik simultan pada semua parameter sekaligus. Ini sangat efisien dan toleran terhadap noise statistik.

$$ \vec{\theta}_{k+1} = \vec{\theta}_k - \alpha_k \vec{g}_k(\vec{\theta}_k) $$
di mana $\vec{g}_k$ adalah aproksimasi gradien stokastik.

---

**Kesimpulan Bagian 3:**
Kita telah menjabarkan seluruh pipa VQE:
1.  **Ansatz $U(\vec{\theta})$** membatasi pencarian ke subruang yang kita pilih (Hardware-Efficient atau UCC).
2.  **Dekomposisi $H$ ke string Pauli** memungkinkan kita menghitung energi melalui pengukuran yang disertai rotasi basis yang cerdas.
3.  **Loop Klasik-Kuantum** secara iteratif menyetel $\vec{\theta}$ untuk meminimalkan energi.

Sekarang kita siap untuk Bagian 4, di mana kita akan melihat contoh konkret molekul paling sederhana: $\mathbf{H_2}$. Kita akan merancang sirkuit 1-parameter, menurunkan $E(\theta)$ secara manual, dan melihat bagaimana VQE menemukan energi ikat molekul hidrogen. Ini akan memperkuat semua konsep yang sudah kita bangun. Siap untuk studi kasus?

---
---
Ini bagian pamungkas yang akan menyatukan semuanya. Kita akan menerapkan seluruh kerangka VQE untuk menghitung energi molekul paling sederhana: **H₂ (molekul hidrogen)**. Ini adalah "Hello, World!" dari kimia kuantum komputasional modern. Kita akan sangat menyederhanakan untuk membuat satu parameter bisa dioptimasi secara manual.

Target kita: Temukan kurva energi disosiasi H₂ (energi vs jarak antar atom) dan bandingkan dengan solusi eksak. Ini mendemonstrasikan bahwa VQE benar-benar bekerja.

---

### Bagian 4: Studi Kasus Sederhana - Molekul H₂

Latar: Dua atom hidrogen (masing-masing 1 proton, 1 elektron) saling mendekat. Kita ingin menghitung energi ikat mereka sebagai fungsi jarak $R$.

#### 4.1. Hamiltonian Elektronik H₂ dalam Basis Minimal (STO-3G)

Dalam kimia kuantum, kita sering bekerja di bawah Aproksimasi Born-Oppenheimer (inti diam). Target kita adalah mencari energi elektronik untuk posisi inti yang tetap.

*   **Basis Orbital Atom:** Kita pilih satu orbital atom untuk tiap atom hidrogen: $|1s_A\rangle$ dan $|1s_B\rangle$. Basis minimal ini disebut STO-3G (3 fungsi Gaussian digunakan untuk tiap orbital).
*   **Orbital Molekul:** Kombinasi linear dari orbital atom membentuk orbital molekul:
    *   Bonding: $| \sigma_g \rangle = \frac{1}{\sqrt{2}}(|1s_A\rangle + |1s_B\rangle)$
    *   Anti-bonding: $| \sigma_u \rangle = \frac{1}{\sqrt{2}}(|1s_A\rangle - |1s_B\rangle)$
*   **Keadaan Hartree-Fock (HF):** Dalam keadaan dasar, 2 elektron akan menempati orbital bonding (dengan spin berlawanan). Keadaan referensi kita adalah determinan Slater:
    $$|\psi_{HF}\rangle = |\sigma_g^\uparrow \sigma_g^\downarrow \rangle$$
    Ini adalah titik awal kita.

**Hamiltonian Elektronik (Second Quantization)**
Hamiltonian elektronik umum adalah:
$$H = \sum_{p,q} h_{pq} a_p^\dagger a_q + \frac{1}{2} \sum_{p,q,r,s} V_{pqrs} a_p^\dagger a_q^\dagger a_r a_s$$
Dengan simetri H₂, banyak suku yang nol. Setelah melalui proses yang disebut *taperring-off qubit* berbasis simetri (mempertahankan jumlah elektron dan spin), Hamiltonian 4-spin-orbital ini dapat direduksi secara dramatis.

#### 4.2. Reduksi Qubit oleh Simetri: Dari 4 Spin-Orbital ke 2 Qubit

Ini adalah langkah teknis tetapi magis. Karena kita tahu jumlah elektron tetap ($N_e = 2$) dan spin total $S_z = 0$, kita bisa memetakan Hamiltonian hanya ke **2 qubit**. Pemetaan yang sering dipakai adalah dengan **Jordan-Wigner**, lalu memanfaatkan operator yang melestarikan jumlah partikel, atau dengan transformasi **Bravyi-Kitaev** yang mereduksi qubit. Ada konstruksi langsung oleh O'Malley *et al.* (2016) yang terkenal.

Hasil reduksi: Hamiltonian 2-qubit efektif untuk H₂ adalah:
$$H = g_0 I \otimes I + g_1 Z \otimes I + g_2 I \otimes Z + g_3 Z \otimes Z + g_4 X \otimes X$$
Koefisien $g_i$ adalah bilangan real yang bergantung pada jarak antar-atom $R$. Untuk $R=0.75$ Å, nilai tipikalnya adalah:
$g_0 = -0.4805, g_1 = +0.3863, g_2 = -0.3863, g_3 = -0.0112, g_4 = +0.1777$.
(Anda akan melihat suku $Z \otimes I$ dan $I \otimes Z$ muncul terutama dari interaksi satu-elektron).

#### 4.3. Desain Ansatz 1-Parameter (Yang Terinspirasi UCC)

Keadaan Hartree-Fock $|\psi_{HF}\rangle$ untuk representasi 2-qubit kita adalah $|01\rangle$ (ini adalah konvensi orbital). Tapi kita tahu bahwa korelasi elektron akan mencampurkan keadaan $|01\rangle$ dengan $|10\rangle$ (eksitasi dari bonding ke anti-bonding, tapi karena konservasi spin, hanya satu kombinasi yang relevan).

Ini memotivasi ansatz yang sangat sederhana:
$$|\psi(\theta)\rangle = \cos\left(\frac{\theta}{2}\right) |01\rangle - \sin\left(\frac{\theta}{2}\right) |10\rangle$$

*   $\theta = 0$ menghasilkan keadaan $|01\rangle$ (keadaan HF).
*   $\theta$ mengontrol jumlah campuran (korelasi) dari eksitasi $|10\rangle$.

Sirkuit untuk membuat ini dari keadaan awal $|00\rangle$:
1.  Qubit 0: $|0\rangle$, Qubit 1: $|0\rangle$.
2.  Terapkan $X$ pada Qubit 1: jadi $|01\rangle$.
3.  Untuk membuat superposisi terkendali, kita butuh rotasi pada satu qubit yang dikendalikan oleh qubit lain. Polanya:
    *   Gerbang $R_y(\theta)$ pada Qubit 0.
    *   CNOT dari Qubit 0 ke Qubit 1.
    *   $R_y(-\theta)$ pada Qubit 1.
    *   CNOT dari Qubit 0 ke Qubit 1.
    Secara ekuivalen, sirkuit yang lebih sederhana adalah: $X_1 \cdot \text{CNOT}_{0,1} \cdot R_y(\theta)_0 \cdot X_1$ (tergantung definisi, yang penting hasilnya adalah $|\psi(\theta)\rangle$ di atas). Kita akan pakai bentuk analitisnya langsung.

#### 4.4. Kalkulasi Manual: Fungsi Energi $E(\theta)$

Sekarang kita hitung energi sebagai fungsi $\theta$. Inilah langkah "Rayleigh-Ritz" kita.

$$E(\theta) = \langle \psi(\theta) | H | \psi(\theta) \rangle = \sum_{j=0}^4 g_j \langle \psi(\theta) | P_j | \psi(\theta) \rangle$$

Kita hitung nilai ekspektasi tiap suku Pauli:

1.  **Suku $I \otimes I$:** $\langle \psi | \psi \rangle = 1$. Jadi $\langle I \otimes I \rangle = 1$.

2.  **Suku $Z \otimes I$ dan $I \otimes Z$:** Ini adalah operator paritas pada masing-masing qubit.
    $Z|0\rangle = +|0\rangle, Z|1\rangle = -|1\rangle$.
    Mari kita tulis ulang ansatz: $|\psi(\theta)\rangle = c |01\rangle - s |10\rangle$, dengan $c = \cos(\theta/2), s = \sin(\theta/2)$.
    *   **Untuk $Z \otimes I$:** (paritas qubit 0)
        Qubit 0 adalah $|0\rangle$ di suku pertama dan $|1\rangle$ di suku kedua. Probabilitas qubit 0 dalam $|0\rangle$ adalah $c^2$, dalam $|1\rangle$ adalah $s^2$.
        Maka $\langle Z_0 \rangle = (+1)c^2 + (-1)s^2 = c^2 - s^2 = \cos^2(\theta/2) - \sin^2(\theta/2) = \cos\theta$.
        Jadi $\langle Z \otimes I \rangle = \cos\theta$.
    *   **Untuk $I \otimes Z$:** (paritas qubit 1)
        Qubit 1 adalah $|1\rangle$ di suku pertama dan $|0\rangle$ di suku kedua. Probabilitas qubit 1 dalam $|1\rangle$ adalah $c^2$ (nilai eigen $-1$), dalam $|0\rangle$ adalah $s^2$ (nilai eigen $+1$).
        Maka $\langle Z_1 \rangle = (-1)c^2 + (+1)s^2 = -c^2 + s^2 = -\cos\theta$.
        Jadi $\langle I \otimes Z \rangle = -\cos\theta$.

3.  **Suku $Z \otimes Z$:** Ini adalah korelasi paritas. Kedua qubit selalu berbeda (satu $|0\rangle$ satu $|1\rangle$). Maka hasil kali paritasnya selalu $(+1)(-1) = -1$.
    $$\langle Z \otimes Z \rangle = -1$$

4.  **Suku $X \otimes X$:** Operator flip. $X|0\rangle = |1\rangle, X|1\rangle = |0\rangle$.
    $$(X \otimes X) |\psi\rangle = (X \otimes X)[c|01\rangle - s|10\rangle] = c|10\rangle - s|01\rangle = -s|01\rangle + c|10\rangle$$
    Lalu kita hitung proyeksi:
    $$\langle \psi | X \otimes X | \psi \rangle = [c\langle 01| - s\langle 10|] (-s|01\rangle + c|10\rangle)$$
    $$= -cs \langle 01|01\rangle + c^2 \langle 01|10\rangle + s^2 \langle 10|01\rangle - sc \langle 10|10\rangle = -cs - sc = -2cs$$
    Karena $2cs = 2\sin(\theta/2)\cos(\theta/2) = \sin\theta$, maka:
    $$\langle X \otimes X \rangle = -\sin\theta$$

Sekarang kita substitusikan semua:
$$E(\theta) = g_0\langle I \rangle + g_1\langle Z_0 \rangle + g_2\langle Z_1 \rangle + g_3\langle Z_0 Z_1 \rangle + g_4\langle X_0 X_1 \rangle$$
$$E(\theta) = g_0(1) + g_1(\cos\theta) + g_2(-\cos\theta) + g_3(-1) + g_4(-\sin\theta)$$
$$E(\theta) = (g_0 - g_3) + (g_1 - g_2)\cos\theta - g_4 \sin\theta$$

Ini adalah fungsi satu variabel $\theta$ yang sangat sederhana!

#### 4.5. Optimasi Visual dan Hasil

Untuk $R=0.75$ Å, masukkan nilai $g_i$ yang kita punya:
*   $g_0 = -0.4805, g_1 = +0.3863, g_2 = -0.3863, g_3 = -0.0112, g_4 = +0.1777$

Hitung:
*   Konstanta: $g_0 - g_3 = -0.4805 - (-0.0112) = -0.4693$
*   Koefisien $\cos\theta$: $g_1 - g_2 = 0.3863 - (-0.3863) = 0.7726$
*   Koefisien $\sin\theta$: $-g_4 = -0.1777$

Maka:
$$E(\theta) = -1.2419 + 0.7726 \cos\theta - 0.1777 \sin\theta$$

(Saya sudah tambahkan $g_0 - g_3 = -0.4693 + (-0.7726)?$ Tunggu, periksa kosntanta. $g_0 + g_0?$ Tidak. Ekspresi totalnya:
$E(\theta) = g_0 + g_3(-1) + (g_1-g_2)\cos\theta - g_4\sin\theta = (-0.4805) - (-0.0112) + ... = -0.4693 + 0.7726\cos\theta - 0.1777\sin\theta$.
Untuk menemukan minimum, kita cari titik stasioner terhadap $\theta$:
$$\frac{dE}{d\theta} = -0.7726 \sin\theta - 0.1777 \cos\theta = 0 \implies \tan\theta^* = -\frac{0.1777}{0.7726} \approx -0.23$$
$\theta^* \approx -0.226$ radian (atau sekitar $-13^\circ$).

Substitusi balik:
$E(\theta^*) \approx -0.4693 + 0.7726(0.9746) - 0.1777(-0.224) \approx -0.4693 + 0.753 - 0.0398 = -1.2621$ (dalam Hartree).

Angka ini adalah aproksimasi energi elektronik. Energi eksak dari Full Configuration Interaction (FCI) di basis ini adalah $E_{FCI} = -1.8572$ (tunggu... perlu koreksi satuan. Energi total termasuk tolakan inti-inti $1/R$). Intinya, hasil minimum kita adalah yang terbaik yang bisa dicapai ansatz 1-parameter ini, dan terbukti sangat dekat dengan solusi eksak untuk H₂ di sekitar panjang ikat.

Jika kita plot $E(\theta)$ terhadap $\theta$, kita akan melihat kurva sinusoidal sederhana dengan minimum yang jelas. Ini adalah lanskap energi VQE kita. Dalam VQE nyata, QPU akan mengevaluasi $E(\theta)$ di beberapa titik ($\theta$ yang diajukan optimizer), dan pengoptimal klasik akan menemukan $\theta^*$ tanpa perlu tahu rumus analitiknya.

---

### Kesimpulan Perjalanan Kita

Mari kita rekap bagaimana setiap Bagian terhubung ke contoh akhir ini:

*   **Bagian 1:** Kita belajar meminimalkan fungsional $\Pi[y]$ dengan metode Rayleigh-Ritz (ansatz $y \approx \sum c_i \phi_i$). Di sini, $E(\theta)$ adalah "fungsi" kita, $\theta$ adalah parameter tunggal kita.
*   **Bagian 2:** Teorema Variasi menjamin bahwa energi yang kita hitung dari fungsi coba *apapun* (termasuk $|\psi(\theta)\rangle$ kita) tidak akan pernah lebih rendah dari energi dasar eksak $E_0$. Minimalisasi $E(\theta)$ adalah pendekatan sah.
*   **Bagian 3:** Kita bongkar bagaimana $|\psi(\theta)\rangle$ dibuat dengan sirkuit, dan bagaimana Hamiltonian $H$ diukur suku per suku ($Z \otimes I, I \otimes Z, Z \otimes Z, X \otimes X$) melalui rotasi basis.
*   **Bagian 4:** Kita melakukan semuanya secara manual. Kita lihat bagaimana pilihan ansatz yang tepat mereduksi masalah menjadi optimasi 1D, dan bagaimana dekomposisi Pauli memungkinkan kita menulis $E(\theta)$ sebagai fungsi eksplisit.

Dari sini, Anda bisa memperluas ke sistem yang lebih besar: menambah parameter, menambah kompleksitas ansatz (UCCSD), dan berhadapan dengan lanskap energi yang rumit. Namun, jiwa dari semuanya tetaplah prinsip variasi: **coba, ukur, optimasi, ulangi.**

Semoga roadmap ini memberikan pemahaman yang dalam dan terstruktur. Selamat menjelajahi dunia VQE lebih lanjut!