# Bagian 0: awal mula

Shapley dan Monderer adalah matematikawan murni yang menemukan **hukum/aturan baku** tentang _Potential Game_ (bahwa selisih utilitas individu harus sama dengan selisih fungsi global). Persamaan $u_i$ yang spesifik berisi $\mu$ (_return_) dan $\sigma$ (kovariansi) itu **dirumuskan oleh para peneliti keuangan kuantitatif di era modern** (seperti penulis pada jurnal _Multi-portfolio Optimization_ yang Anda unggah).

Para peneliti modern tersebut mengambil **Fungsi Global Markowitz**, lalu bekerja **mundur (reverse-engineering)** menggunakan hukum Shapley untuk menemukan "seperti apa bentuk matriks _payoff_ individunya agar sah disebut _Potential Game_?".

Untuk memahami dari mana persamaan $u_i$ itu berasal, mari kita bongkar menggunakan **Matriks Payoff Normal-Form** untuk 2 Saham (Saham 1 dan Saham 2). Ini adalah cara paling fundamental dalam _Game Theory_ untuk menurunkan sebuah persamaan utilitas.

---

### 1. Konstruksi Matriks Payoff (Kasus 2 Saham)

Bayangkan Saham 1 dan Saham 2 adalah dua pemain yang sedang bermain _game_. Masing-masing punya 2 strategi: $x \in \{0, 1\}$ ($0$ = Keluar, $1$ = Masuk).

Kita susun matriks _payoff_ $2 \times 2$. Nilai di dalam sel adalah $(u_1, u_2)$, yaitu keuntungan yang didapat (Saham 1, Saham 2).

| **Saham 1 \ Saham 2**  | **Keluar ($x_2$​=0)**                      | **Masuk ($x_2$​=1)**                       |
| ---------------------- | ------------------------------------------ | ------------------------------------------ |
| **Keluar ($x_1 = 0$)** | $(0, 0)$                                   | $(0, \mu_2 - \frac{\gamma}{2}\sigma_{22})$ |
| **Masuk ($x_1 = 1$)**  | $(\mu_1 - \frac{\gamma}{2}\sigma_{11}, 0)$ | $(P_{11}, P_{22})$                         |

**Mari kita bedah sel-sel di atas dari kacamata Saham 1:**

- **Baris Pertama ($x_1 = 0$):** Jika Saham 1 memilih "Keluar", utilitasnya PASTI $0$. Ia tidak peduli apa yang dilakukan Saham 2.
    
- **Kiri Bawah ($x_1 = 1, x_2 = 0$):** Saham 1 "Masuk", tapi Saham 2 "Keluar". Saham 1 menjadi pemain tunggal di portofolio. Maka, imbalannya murni _return_ miliknya dikurangi risiko mandirinya: $\mu_1 - \frac{\gamma}{2}\sigma_{11}$.
    
- **Kanan Bawah ($x_1 = 1, x_2 = 1$):** Keduanya "Masuk". Di sinilah interaksi terjadi. Saham 1 mendapatkan imbalan mandirinya, TETAPI harus dikurangi **penalti interaksi** (kovariansi) karena Saham 2 ikut masuk. Maka imbalan Saham 1 ($P_{11}$) di sel ini didefinisikan sebagai:
    
    $$P_{11} = \mu_1 - \frac{\gamma}{2}\sigma_{11} - \gamma\sigma_{12}$$
    

### 2. Mengubah Matriks Menjadi Persamaan Aljabar

Dalam _Game Theory_, sebuah matriks diskrit dapat diubah menjadi persamaan fungsi kontinu/aljabar dengan menggunakan variabel indikator (dalam hal ini $x_1$ dan $x_2$).

Mari kita rumuskan utilitas Saham 1 ($u_1$) berdasarkan matriks di atas:

**Langkah A: Sakelar Utama (Variabel $x_1$)**

Karena _payoff_ Saham 1 selalu $0$ jika ia memilih $x_1 = 0$, maka seluruh fungsi utilitasnya harus dikalikan dengan $x_1$.

$$u_1(x_1, x_2) = x_1 \times [ \text{Skenario jika ia Masuk} ]$$

**Langkah B: Interpolasi Linear (Variabel $x_2$)**

Sekarang kita lihat "Skenario jika ia Masuk" (Baris kedua matriks).

- Jika $x_2 = 0$, nilainya adalah: $\mu_1 - \frac{\gamma}{2}\sigma_{11}$
    
- Jika $x_2 = 1$, nilainya berkurang sebesar $\gamma\sigma_{12}$.
    

Karena variabel $x_2$ bersifat biner $\{0,1\}$, kita bisa menuliskannya sebagai pengurangan linear yang diaktifkan oleh $x_2$:

$$[ \text{Skenario jika ia Masuk} ] = \left( \mu_1 - \frac{\gamma}{2}\sigma_{11} \right) - (\gamma\sigma_{12})x_2$$

**Langkah C: Persamaan Final untuk 2 Saham**

Gabungkan Langkah A dan Langkah B:

$$u_1(x_1, x_2) = x_1 \left( \mu_1 - \frac{\gamma}{2}\sigma_{11} - \gamma\sigma_{12}x_2 \right)$$

### 3. Generalisasi ke $N$ Saham (Mendapatkan Persamaan Akhir)

Persamaan yang baru saja kita turunkan adalah untuk 2 saham. Bagaimana jika ada 4 saham (A, B, C, D) seperti yang Anda tanyakan sebelumnya?

Jika Saham A masuk ($x_A = 1$), ia tidak hanya melihat Saham B, tetapi juga melihat C dan D. Setiap saham lain yang ikut masuk akan memberikan potongan penalti secara independen.

Matriksnya menjadi matriks $N$-dimensi, namun logika interpolasinya tetap sama. Suku pengurangnya (penalti interaksi) ditambahkan sebanyak jumlah saham lain yang masuk.

Maka, untuk pemain $i$, fungsi pengurangnya dijumlahkan terhadap semua pemain $j$ lainnya:

$$u_i(x_i, \mathbf{x}_{-i}) = x_i \left( \mu_i - \frac{\gamma}{2}\sigma_{ii} - \gamma \sum_{j \neq i} \sigma_{ij}x_j \right)$$

---

**Kesimpulan:**

Persamaan tersebut bukanlah hasil sihir matematis yang tiba-tiba muncul. Persamaan itu adalah **terjemahan aljabar langsung dari Matriks Payoff Game Theory** di mana "Penalti Kovariansi" diletakkan pada sel ketika dua pemain saling bertemu (memilih strategi yang sama-sama aktif). Para peneliti merancang matriks ini sedemikian rupa agar ketika dihitung menggunakan Teorema Monderer-Shapley, hasilnya persis kembali menjadi fungsi Markowitz/Hamiltonian Ising.

Apakah transisi dari Matriks Payoff 2x2 ke persamaan aljabar di atas cukup mudah diikuti? Apakah Anda ingin saya membuatkan skrip Python (Qiskit) sederhana untuk membuktikan bahwa Hamiltonian ini benar-benar bisa mencari 2 saham optimal?
# Bagian 1: Dari Data Finansial Menuju Multi-Agent Game

## 1. Ekstraksi Data Finansial (Variabel Dasar)

Misalkan kita memiliki sebuah semesta pasar yang terdiri dari $N$ aset. Kita mengambil data deret waktu harga penutupan (_closing price_) dari aset-aset tersebut selama rentang waktu $T$. Dari data mentah ini, kita menghitung dua parameter fundamental:

- **Ekspektasi Return ($\mu_i$):** Nilai rata-rata keuntungan historis untuk setiap aset $i$.
    
- **Matriks Kovariansi ($\Sigma$):** Matriks berukuran $N \times N$ di mana elemen $\sigma_{ij}$ merepresentasikan kovariansi antara aset $i$ dan aset $j$. Jika $i = j$, maka $\sigma_{ii}$ adalah varians (risiko bawaan) dari aset $i$.
    

Kita juga menetapkan parameter $\gamma$ (gamma) sebagai tingkat penghindaran risiko (_risk aversion_). Semakin tinggi $\gamma$, semakin kita membenci risiko.

## 2. Definisi Permainan (_Game Structure_)

Sekarang kita mentransformasikan pasar ini menjadi sebuah permainan terdesentralisasi:

- **Pemain (_Players_):** Setiap aset $i \in \{1, 2, \dots, N\}$ bertindak sebagai pemain individual.
    
- **Ruang Strategi (_Strategy Space_):** Setiap aset $i$ memiliki dua pilihan aksi biner, yang direpresentasikan dengan variabel $x_i \in \{0, 1\}$.
    
    - $x_i = 1$: Aset memutuskan untuk "masuk" ke dalam portofolio.
        
    - $x_i = 0$: Aset memutuskan untuk "keluar" atau tidak berpartisipasi.
        
- **Profil Strategi:** Vektor $\mathbf{x} = (x_1, x_2, \dots, x_N)$ adalah konfigurasi portofolio secara keseluruhan. Pilihan strategi dari _semua pemain lain_ selain $i$ dilambangkan dengan $\mathbf{x}_{-i}$.
    

## 3. Fungsi Utilitas/Payoff Individual ($u_i$)

Ini adalah bagian paling krusial dalam _Game Theory_. Kita harus merumuskan apa yang didapatkan oleh aset $i$ jika ia memutuskan untuk bergabung ke dalam portofolio ($x_i = 1$), dengan mempertimbangkan siapa saja aset lain yang sudah ada di dalam ($\mathbf{x}_{-i}$).

Fungsi _payoff_ untuk pemain $i$, disimbolkan dengan $u_i(x_i, \mathbf{x}_{-i})$, didefinisikan sebagai berikut:

$$u_i(x_i, \mathbf{x}_{-i}) = x_i \left( \mu_i - \frac{\gamma}{2} \sigma_{ii} - \gamma \sum_{j \neq i} \sigma_{ij} x_j \right)$$

**Mari kita bedah anatomi fungsi _payoff_ ini:**

1. **Suku $x_i$ (Sakelar / _Toggle_):** Jika aset $i$ memilih keluar ($x_i = 0$), _payoff_-nya adalah $0$. Ia tidak mendapatkan _return_ dan tidak menanggung risiko. Jika ia masuk ($x_i = 1$), _payoff_-nya adalah nilai di dalam kurung.
    
2. **Suku $\mu_i$ (Keuntungan Mandiri):** Ini adalah imbalan dasar (_standalone reward_) yang didapat aset $i$ karena ia memiliki _return_ positif.
    
3. **Suku $\frac{\gamma}{2} \sigma_{ii}$ (Penalti Risiko Mandiri):** Ini adalah penalti yang langsung memotong _payoff_ karena aset $i$ itu sendiri memiliki fluktuasi (varians).
    
4. **Suku $\gamma \sum_{j \neq i} \sigma_{ij} x_j$ (Penalti Interaksi / Kopling):** Ini adalah esensi dari permainan! Aset $i$ akan mendapatkan pengurangan _payoff_ tambahan yang proporsional dengan kovariansi ($\sigma_{ij}$) terhadap setiap aset $j$ yang _juga_ memutuskan masuk ke portofolio ($x_j = 1$). Jika aset $i$ dan $j$ bergerak searah (korelasi positif), keberadaan aset $j$ merugikan aset $i$ dalam konteks diversifikasi.

Jika $i = A$, maka $\mathbf{x}_{-A} = (x_B, x_C, x_D)$.

Suku $\sum_{j \neq A}$ berarti kita menjumlahkan interaksi A dengan B, C, dan D sekaligus di dalam satu persamaan.

$$u_A(x_A, \mathbf{x}_{-A}) = x_A \left( \mu_A - \frac{\gamma}{2} \sigma_{AA} - \gamma \mathbf{( \sigma_{AB} x_B + \sigma_{AC} x_C + \sigma_{AD} x_D )} \right)$$

Jika $i = B$, maka $\mathbf{x}_{-B} = (x_A, x_C, x_D)$.

$$u_B(x_B, \mathbf{x}_{-B}) = x_B \left( \mu_B - \frac{\gamma}{2} \sigma_{BB} - \gamma \mathbf{( \sigma_{BA} x_A + \sigma_{BC} x_C + \sigma_{BD} x_D )} \right)$$

Jika $i = C$, maka $\mathbf{x}_{-C} = (x_A, x_B, x_D)$.

$$u_C(x_C, \mathbf{x}_{-C}) = x_C \left( \mu_C - \frac{\gamma}{2} \sigma_{CC} - \gamma \mathbf{( \sigma_{CA} x_A + \sigma_{CB} x_B + \sigma_{CD} x_D )} \right)$$

Jika $i = D$, maka $\mathbf{x}_{-D} = (x_A, x_B, x_C)$.

$$u_D(x_D, \mathbf{x}_{-D}) = x_D \left( \mu_D - \frac{\gamma}{2} \sigma_{DD} - \gamma \mathbf{( \sigma_{DA} x_A + \sigma_{DB} x_B + \sigma_{DC} x_C )} \right)$$

---
### 1. Mengapa $\sigma_{ii}$ tidak memakai notasi $\sum$?

Fungsi $u_i$ yang kita bahas di Bagian 1 adalah fungsi utilitas untuk **satu pemain tunggal** (aset $i$).

Karena kita sedang melihat dari kacamata egosentris aset $i$ semata, maka risiko mandirinya hanya ada satu nilai, yaitu varians dari dirinya sendiri ($\sigma_{ii}$). Ia tidak perlu dijumlahkan dengan varians aset lain dalam fungsi _payoff_ pribadinya.

Sebaliknya, notasi $\sum_{j \neq i}$ muncul pada suku kovariansi ($\sigma_{ij}$) karena aset $i$ harus menghitung total "gesekan" atau interaksi dengan _semua_ aset lain ($j$) yang saat itu sedang berada di dalam portofolio ($x_j = 1$).

### 2. Dari mana datangnya pembagi 2 ($\frac{\gamma}{2}$)?

Ini adalah bagian yang paling elegan dari sintesis _Potential Game_. Angka 2 ini bukanlah sekadar tebakan, melainkan hasil mutlak dari penurunan **Fungsi Objektif Global Markowitz** yang memiliki bentuk kuadratik.

Mari kita buktikan. Fungsi utilitas portofolio Markowitz global secara standar ditulis sebagai Ekspektasi Return dikurangi Penalti Risiko:

$$\Phi(\mathbf{x}) = \sum_{i=1}^N \mu_i x_i - \frac{\gamma}{2} \sum_{i=1}^N \sum_{j=1}^N \sigma_{ij} x_i x_j$$

_(Catatan: Penulisan $\frac{1}{2}$ di depan risiko portofolio adalah konvensi matematis yang standar agar saat diturunkan/diferensiasi, angka 2 dari pangkat kuadrat akan saling menghilangkan)._

Sekarang, mari kita bedah suku risiko kuadratik ganda di atas ($\sum \sum$):

$$\sum_{i=1}^N \sum_{j=1}^N \sigma_{ij} x_i x_j = \underbrace{\sum_{i=1}^N \sigma_{ii} x_i^2}_{\text{Suku Diagonal}} + \underbrace{\sum_{i \neq j} \sigma_{ij} x_i x_j}_{\text{Suku Off-Diagonal}}$$

Di sinilah **sifat biner dari strategi** memainkan peran ajaib. Karena strategi $x_i \in \{0, 1\}$, maka secara matematis $x_i^2 = x_i$ (seperti properti idempotensi yang dibahas di _main.pdf_).

Selain itu, matriks kovariansi bersifat simetris ($\sigma_{ij} = \sigma_{ji}$), sehingga suku _off-diagonal_ dapat disederhanakan dengan mengalikan 2:

$$\sum_{i=1}^N \sum_{j=1}^N \sigma_{ij} x_i x_j = \sum_{i=1}^N \sigma_{ii} x_i + 2 \sum_{i < j} \sigma_{ij} x_i x_j$$

Jika kita masukkan kembali angka pengali $\left(-\frac{\gamma}{2}\right)$ dari fungsi Markowitz awal ke dalam hasil ekspansi di atas, kita mendapatkan:

$$-\frac{\gamma}{2} \left[ \sum_{i=1}^N \sigma_{ii} x_i + 2 \sum_{i < j} \sigma_{ij} x_i x_j \right] = \mathbf{- \frac{\gamma}{2} \sum_{i=1}^N \sigma_{ii} x_i - \gamma \sum_{i < j} \sigma_{ij} x_i x_j}$$

### Kesimpulan Pembuktian (Syarat _Exact Potential Game_)

Dalam teori _Potential Game_, perubahan _payoff_ seorang pemain ($\Delta u_i$) saat ia mengubah strateginya harus sama persis dengan perubahan pada Fungsi Potensial global ($\Delta \Phi$).

Jika pemain $i$ mengubah strateginya dari $x_i = 0$ menjadi $x_i = 1$, kita bisa melihat kontribusi persis yang ia berikan ke fungsi global $\Phi$:

- Ia menambahkan _return_: $+\mu_i$
    
- Ia menambahkan varians (yang masih mengandung pembagi 2 dari ekspansi kita tadi): $-\frac{\gamma}{2} \sigma_{ii}$
    
- Ia menambahkan kovariansi dengan aset lain (di mana angka 2 sudah habis dicoret oleh pembagi 2): $-\gamma \sum_{j \neq i} \sigma_{ij} x_j$
    

Itulah mengapa fungsi utilitas parsialnya berbentuk:

$$u_i = x_i \left( \mu_i - \frac{\gamma}{2} \sigma_{ii} - \gamma \sum_{j \neq i} \sigma_{ij} x_j \right)$$

Pembagi 2 pada $\sigma_{ii}$ tersisa karena ia berasal dari diagonal matriks yang tidak dikalikan 2 saat kita membongkar bentuk kuadratiknya. Penurunan ini mengonfirmasi bahwa permainan yang kita susun benar-benar merupakan _Exact Potential Game_ yang selaras dengan Hamiltonian kuadratik (QUBO/Ising).

---

# Bagian 2
### 1. Definisi _Exact Potential Game_

Sebuah permainan multi-agen disebut sebagai **Exact Potential Game** (Monderer & Shapley, 1996) jika terdapat sebuah fungsi skalar global $\Phi(\mathbf{x})$ yang disebut Fungsi Potensial, di mana perubahan utilitas satu pemain akibat perubahan strateginya secara sepihak, sama persis dengan perubahan pada nilai Fungsi Potensial tersebut.

Secara matematis, jika aset $i$ mengubah strateginya dari $x_i$ menjadi $x_i'$, sementara strategi aset lain ($\mathbf{x}_{-i}$) tetap, maka syarat mutlaknya adalah:

$$u_i(x_i', \mathbf{x}_{-i}) - u_i(x_i, \mathbf{x}_{-i}) = \Phi(x_i', \mathbf{x}_{-i}) - \Phi(x_i, \mathbf{x}_{-i})$$

### 2. Menghitung Perubahan Utilitas Individu ($\Delta u_i$)

Mari kita hitung selisih utilitas ($\Delta u_i$) jika aset $i$ memutuskan untuk mengubah statusnya dari "di luar portofolio" ($x_i = 0$) menjadi "masuk ke dalam portofolio" ($x_i = 1$).

Berdasarkan fungsi utilitas $u_i$ yang kita rumuskan di Bagian 1:

- Jika $x_i = 1$: $u_i(1, \mathbf{x}_{-i}) = \mu_i - \frac{\gamma}{2} \sigma_{ii} - \gamma \sum_{j \neq i} \sigma_{ij} x_j$
    
- Jika $x_i = 0$: $u_i(0, \mathbf{x}_{-i}) = 0$
    

Maka, perubahan utilitas individunya adalah:

$$\Delta u_i = \mu_i - \frac{\gamma}{2} \sigma_{ii} - \gamma \sum_{j \neq i} \sigma_{ij} x_j$$

### 3. Mengonstruksi Fungsi Potensial Global ($\Phi$)

Sekarang, kita asumsikan bahwa Fungsi Potensial global $\Phi(\mathbf{x})$ untuk permainan ini adalah persamaan objektif portofolio Markowitz standar (Return - Risiko):

$$\Phi(\mathbf{x}) = \sum_{k=1}^N \mu_k x_k - \frac{\gamma}{2} \sum_{k=1}^N \sum_{l=1}^N \sigma_{kl} x_k x_l$$

Untuk membuktikan syarat _Potential Game_, kita harus mencari tahu seberapa besar nilai $\Phi(\mathbf{x})$ berubah jika hanya variabel $x_i$ yang berubah dari $0$ menjadi $1$. Untuk melakukan ini, kita pisahkan semua suku di dalam $\Phi(\mathbf{x})$ yang **mengandung $x_i$**. Suku-suku yang tidak mengandung $x_i$ akan saling menghilangkan saat kita mencari selisihnya ($\Delta \Phi$).

Mari kita ekstrak suku-suku yang melibatkan $x_i$ dari fungsi $\Phi(\mathbf{x})$:

1. Dari suku _Return_: $\mu_i x_i$
    
2. Dari suku Risiko (saat $k=i$ dan $l=i$): $-\frac{\gamma}{2} \sigma_{ii} x_i^2$
    
3. Dari suku Risiko interaksi (saat $k=i$ dan $l=j$, atau $k=j$ dan $l=i$):
    
    $$-\frac{\gamma}{2} \sum_{j \neq i} \sigma_{ij} x_i x_j - \frac{\gamma}{2} \sum_{j \neq i} \sigma_{ji} x_j x_i$$
    

Karena matriks kovariansi simetris ($\sigma_{ij} = \sigma_{ji}$), kedua suku interaksi tersebut dapat dijumlahkan menjadi:

$$-\gamma \sum_{j \neq i} \sigma_{ij} x_i x_j$$

Jadi, bagian dari $\Phi(\mathbf{x})$ yang bergantung pada $x_i$ adalah:

$$\Phi_{dependen}(x_i) = \mu_i x_i - \frac{\gamma}{2} \sigma_{ii} x_i^2 - \gamma \sum_{j \neq i} \sigma_{ij} x_i x_j$$

### 4. Pembuktian Final ($\Delta u_i = \Delta \Phi$)

Ingat sifat variabel biner (_idempotensi_): karena $x_i \in \{0, 1\}$, maka $x_i^2 = x_i$. Kita substitusikan ini ke persamaan di atas:

$$\Phi_{dependen}(x_i) = \mu_i x_i - \frac{\gamma}{2} \sigma_{ii} x_i - \gamma \sum_{j \neq i} \sigma_{ij} x_i x_j$$

$$\Phi_{dependen}(x_i) = x_i \left( \mu_i - \frac{\gamma}{2} \sigma_{ii} - \gamma \sum_{j \neq i} \sigma_{ij} x_j \right)$$

Sekarang kita hitung perubahan Fungsi Potensial ($\Delta \Phi$) saat $x_i$ berubah dari $0$ ke $1$:

- Saat $x_i = 1$: $\Phi_{dependen}(1) = \mu_i - \frac{\gamma}{2} \sigma_{ii} - \gamma \sum_{j \neq i} \sigma_{ij} x_j$
    
- Saat $x_i = 0$: $\Phi_{dependen}(0) = 0$
    

Maka:

$$\Delta \Phi = \mu_i - \frac{\gamma}{2} \sigma_{ii} - \gamma \sum_{j \neq i} \sigma_{ij} x_j$$

**KESIMPULAN BAGIAN 2:**

Perhatikan bahwa hasil $\Delta \Phi$ di atas **sama persis** dengan $\Delta u_i$ yang kita hitung di langkah 2.

$$\Delta u_i = \Delta \Phi$$

Hal ini membuktikan secara sah bahwa permainan pemilihan aset ini adalah sebuah _Exact Potential Game_. Lebih jauh lagi, ini membuktikan bahwa mengejar _Nash Equilibrium_ dari utilitas individu ($u_i$) secara matematis ekuivalen dengan memaksimalkan Fungsi Markowitz global ($\Phi$). Bentuk persamaan Fungsi Potensial ini sudah berbentuk _Quadratic Unconstrained Binary Optimization_ (QUBO).

---

# Bagian 3: Pemetaan QUBO ke Hamiltonian Ising (VQE Input)

#### 1. Membalikkan Objektif (Maksimasi ke Minimasi)

Dalam _Game Theory_ dan portofolio Markowitz, tujuan kita adalah **memaksimalkan** Fungsi Potensial $\Phi(\mathbf{x})$ (memaksimalkan _return_, meminimalkan risiko).

Namun, dalam fisika kuantum, sebuah sistem alamiah selalu mencari keadaan dengan energi terendah (_Ground State_). Oleh karena itu, kita harus mendefinisikan **Hamiltonian Energi ($H$)** sebagai **negatif dari Fungsi Potensial**.

$$H(\mathbf{x}) = -\Phi(\mathbf{x})$$

Berdasarkan Fungsi Potensial yang kita dapatkan di Bagian 2, bentuk fungsi energi (QUBO) kita menjadi:

$$H(\mathbf{x}) = \sum_{i=1}^N \left( \frac{\gamma}{2} \sigma_{ii} - \mu_i \right) x_i + \gamma \sum_{i < j} \sigma_{ij} x_i x_j$$

Untuk menyederhanakan perhitungan, mari kita definisikan ulang koefisien linier dan kuadratiknya:

- **Koefisien Linier ($C_i$):** $C_i = \frac{\gamma}{2} \sigma_{ii} - \mu_i$
    
- **Koefisien Kuadratik ($Q_{ij}$):** $Q_{ij} = \gamma \sigma_{ij}$
    

Sehingga QUBO kita berbentuk:

$$H(\mathbf{x}) = \sum_{i} C_i x_i + \sum_{i < j} Q_{ij} x_i x_j$$

#### 2. Transformasi _Affine_ (Dari Variabel Biner ke Spin)

Algoritma VQE bekerja pada qubit yang direpresentasikan oleh operator Spin/Matriks Pauli-Z ($\hat{Z}$). Nilai eigen dari $\hat{Z}$ adalah $+1$ (spin up / state $|0\rangle$) dan $-1$ (spin down / state $|1\rangle$).

Kita harus memetakan variabel keputusan portofolio $x_i \in \{0, 1\}$ menjadi variabel spin $s_i \in \{-1, 1\}$. Transformasi standar yang digunakan adalah:

$$x_i = \frac{1 + s_i}{2}$$

_(Cek logika: Jika spin $s_i = 1$, maka $x_i = 1$ (aset dipilih). Jika spin $s_i = -1$, maka $x_i = 0$ (aset tidak dipilih))._

#### 3. Substitusi dan Ekspansi ke Model Ising

Sekarang kita substitusikan $x_i$ dengan $s_i$ ke dalam persamaan $H(\mathbf{x})$:

**Ekspansi Suku Linier:**

$$\sum_i C_i \left( \frac{1 + s_i}{2} \right) = \sum_i \frac{C_i}{2} s_i + \sum_i \frac{C_i}{2}$$

**Ekspansi Suku Kuadratik:**

$$\sum_{i < j} Q_{ij} \left( \frac{1 + s_i}{2} \right) \left( \frac{1 + s_j}{2} \right) = \sum_{i < j} \frac{Q_{ij}}{4} (1 + s_i + s_j + s_i s_j)$$

$$= \sum_{i < j} \frac{Q_{ij}}{4} s_i s_j + \sum_{i < j} \frac{Q_{ij}}{4} s_i + \sum_{i < j} \frac{Q_{ij}}{4} s_j + \sum_{i < j} \frac{Q_{ij}}{4}$$

Perhatikan bahwa suku $\sum_{i < j} \frac{Q_{ij}}{4} (s_i + s_j)$ bisa dikumpulkan menjadi satu penjumlahan terhadap indeks $i$ tunggal. Untuk setiap $i$, nilai $s_i$ akan dikalikan dengan semua interaksinya dengan $j$. Ini menjadi:

$$\sum_i \left( \sum_{j \neq i} \frac{Q_{ij}}{4} \right) s_i$$

#### 4. Pengelompokan menjadi Hamiltonian Ising Final

Model Ising standar memiliki format Hamiltonian sebagai berikut:

$$H(\mathbf{s}) = \sum_{i < j} J_{ij} s_i s_j + \sum_i h_i s_i + E_{offset}$$

Dengan mengumpulkan hasil ekspansi di Langkah 3, kita dapat mendefinisikan parameter kuantum dari data finansial kita:

**A. Kekuatan Kopling ($J_{ij}$) - _Interaksi Antar Qubit_:**

Parameter ini berasal mutlak dari suku kuadratik $s_i s_j$.

$$J_{ij} = \frac{Q_{ij}}{4} \implies \mathbf{J_{ij} = \frac{\gamma}{4} \sigma_{ij}}$$

_Interpretasi:_ Jika dua aset berkorelasi positif ($\sigma_{ij} > 0$), maka $J_{ij} > 0$ (Kopling Antiferomagnetik). Sistem energi tidak menyukai dua aset ini dipilih bersamaan ($s_i=1, s_j=1$), karena akan menaikkan energi. Ini adalah wujud alamiah dari **diversifikasi portofolio**.

**B. Medan Magnet Lokal ($h_i$) - _Bias Individu Qubit_:**

Parameter ini adalah gabungan dari suku linier dan limpahan dari suku kuadratik.

$$h_i = \frac{C_i}{2} + \sum_{j \neq i} \frac{Q_{ij}}{4}$$

Substitusi kembali $C_i$ dan $Q_{ij}$:

$$\mathbf{h_i = \frac{1}{2} \left( \frac{\gamma}{2} \sigma_{ii} - \mu_i \right) + \frac{\gamma}{4} \sum_{j \neq i} \sigma_{ij}}$$

_Interpretasi:_ Ini adalah "medan" yang mendorong sebuah aset untuk masuk atau keluar secara individu. _Return_ tinggi ($\mu_i$) akan membuat $h_i$ semakin negatif, mendorong spin $s_i$ menuju $+1$ (masuk portofolio) untuk meminimalkan energi Hamiltonian.

**C. Energi Offset ($E_{offset}$):**

$$E_{offset} = \sum_i \frac{C_i}{2} + \sum_{i < j} \frac{Q_{ij}}{4}$$

_Interpretasi:_ Konstanta ini **dapat diabaikan** (dibuang) saat dimasukkan ke dalam VQE karena konstanta hanya menggeser spektrum energi secara vertikal, namun tidak mengubah konfigurasi _Ground State_ (konfigurasi aset optimal) itu sendiri.

#### 5. Formulasi Operator Kuantum (VQE Input)

Langkah terakhir, setelah kita mendapatkan nilai skalar matriks $J_{ij}$ dan vektor $h_i$, kita mengubah variabel spin $s$ menjadi operator Pauli-Z ($\hat{Z}$) untuk algoritma VQE.

Hamiltonian kuantum final ($\hat{H}$) yang siap Anda kompilasi (misalnya menggunakan Qiskit atau Pennylane) adalah:

$$\hat{H} = \sum_{i < j} J_{ij} (\hat{Z}_i \otimes \hat{Z}_j) + \sum_{i=1}^N h_i \hat{Z}_i$$

---

**Kesimpulan Bagian 3:**

Sampai di sini, Anda telah berhasil mendaratkan konsep data mentah (Saham) $\rightarrow$ _Game Theory_ (Agen Biner) $\rightarrow$ QUBO (Energi Klasik) $\rightarrow$ **Hamiltonian Kuantum ($\hat{H}$)**.

Bentuk $\hat{H}$ inilah yang akan Anda masukkan ke dalam VQE. Seperti yang kita diskusikan sebelumnya, Anda bisa menjalankan _solver_ Ising klasik (seperti _Simulated Annealing_) pada persamaan $\hat{H}$ ini untuk mendapatkan _Nash Equilibrium_ sebagai "Kunci Jawaban" _quality check_ sebelum menjalankan sirkuit parametrik VQE.

Apakah penurunan matematis ini sudah cukup jelas untuk diimplementasikan ke dalam _code_ (Python/Qiskit) nantinya?

---
---
Mari kita bedah detail matematis dari implementasi suku penalti ini. Proses ini akan memastikan bahwa model VQE kita hanya akan memilih tepat $K$ saham (misalnya, $K=2$) dari total $N$ saham yang tersedia.

Untuk **Bagian 1** ini, kita akan fokus pada **Formulasi Penalti dan Ekspansinya di Domain QUBO (Variabel Biner)** sebelum nanti kita ubah ke bentuk Spin/Ising.

---

# Bagian 4: Formulasi dan Ekspansi Suku Penalti (Domain Biner/QUBO)

#### 1. Mendefinisikan Batasan (Constraint)

Tujuan kita adalah memilih tepat $K$ aset dari semesta $N$ aset. Ingat kembali bahwa variabel keputusan kita adalah $x_i \in \{0, 1\}$.

Secara matematis, batasan ini ditulis sebagai persamaan linear sederhana:

$$\sum_{i=1}^N x_i = K$$

#### 2. Mengubah Batasan Menjadi Fungsi Energi (Penalti)

Dalam kerangka optimasi tanpa kendala (_Unconstrained Optimization_) seperti QUBO atau Ising, kita tidak bisa memberikan aturan baku ("harus $K$"). Sebagai gantinya, kita mengubah persamaan di atas menjadi **fungsi kerugian kuadratik**.

Jika jumlah aset yang dipilih tidak sama dengan $K$, sistem harus menerima tambahan energi positif yang sangat besar. Fungsi penalti $P(\mathbf{x})$ didefinisikan sebagai:

$$P(\mathbf{x}) = \lambda \left( \sum_{i=1}^N x_i - K \right)^2$$

**Catatan tentang $\lambda$ (Faktor Penalti):**

$\lambda$ adalah sebuah skalar positif yang nilainya harus jauh lebih besar ($\lambda \gg 0$) dibandingkan nilai energi dari objektif utama (matriks kovariansi dan _return_). Hal ini memastikan bahwa melanggar batasan akan selalu menghasilkan energi yang lebih buruk (lebih tinggi) daripada mematuhi batasan, seburuk apa pun kombinasi _return-risk_ saham yang dipilih.

#### 3. Ekspansi Aljabar Fungsi Penalti

Mesin QUBO atau Ising hanya bisa menerima persamaan dalam bentuk polinomial derajat dua (maksimal perkalian dua variabel, $x_i x_j$). Oleh karena itu, kita harus mengekspansi (membongkar) bentuk kuadratik di atas.

Mari kita jabarkan kuadrat dari persamaan tersebut:

$$\left( \sum_{i=1}^N x_i - K \right)^2 = \left( \sum_{i=1}^N x_i \right)^2 - 2K \sum_{i=1}^N x_i + K^2$$

#### 4. Membongkar Suku "Kuadrat dari Penjumlahan"

Bagian yang paling menantang dari ekspansi di atas adalah suku $\left( \sum_{i=1}^N x_i \right)^2$. Jika kita mengkuadratkan sebuah penjumlahan panjang, hasilnya adalah jumlah dari kuadrat masing-masing elemen ditambah dua kali perkalian silang antar elemennya:

$$\left( \sum_{i=1}^N x_i \right)^2 = \sum_{i=1}^N x_i^2 + 2 \sum_{i < j} x_i x_j$$

Di sinilah **sifat idempotensi** (yang juga dibahas pada "main.pdf") dari variabel biner kembali menyelamatkan kita. Karena $x_i$ hanya bisa bernilai $0$ atau $1$, maka kuadrat dari nilai tersebut sama dengan nilai aslinya ($0^2 = 0$ dan $1^2 = 1$).

Maka, $x_i^2 = x_i$.

Substitusikan properti ini ke dalam persamaan:

$$\left( \sum_{i=1}^N x_i \right)^2 = \sum_{i=1}^N x_i + 2 \sum_{i < j} x_i x_j$$

#### 5. Menyusun Ulang Menjadi Bentuk Final QUBO Penalti

Sekarang, masukkan kembali hasil dari langkah 4 ke dalam ekspansi langkah 3:

$$P(\mathbf{x}) = \lambda \left[ \left( \sum_{i=1}^N x_i + 2 \sum_{i < j} x_i x_j \right) - 2K \sum_{i=1}^N x_i + K^2 \right]$$

Kita kelompokkan suku-suku yang memiliki variabel linier tunggal $\sum x_i$:

$$P(\mathbf{x}) = \lambda \left[ (1 - 2K) \sum_{i=1}^N x_i + 2 \sum_{i < j} x_i x_j + K^2 \right]$$

Lalu, kita distribusikan $\lambda$ ke masing-masing suku. Inilah **Bentuk Final Fungsi Penalti di Domain QUBO**:

$$P(\mathbf{x}) = \underbrace{\lambda (1 - 2K) \sum_{i=1}^N x_i}_{\text{Suku Linier}} + \underbrace{2\lambda \sum_{i < j} x_i x_j}_{\text{Suku Kuadratik (Interaksi)}} + \underbrace{\lambda K^2}_{\text{Konstanta}}$$

---

**Analisis Hasil Bagian 1:**

Dari persamaan final QUBO di atas, kita bisa melihat dengan sangat jelas "mekanika" penalti ini bekerja:

- **Suku Interaksi ($2\lambda x_i x_j$):** Ini adalah penalti yang sangat besar jika aset $i$ dan aset $j$ dihidupkan bersamaan. Nilainya selalu positif (menambah energi). Ini "menghukum" sistem jika terlalu banyak aset yang dipilih.
    
- **Suku Linier ($\lambda(1 - 2K)x_i$):** Karena $K$ biasanya bilangan bulat positif (misal $K=2$), maka $(1 - 2(2)) = -3$. Suku ini bernilai _negatif_, yang berarti ia "memberikan hadiah" (menurunkan energi) bagi setiap aset individu yang dihidupkan, sampai batas tertentu, untuk melawan hukuman dari suku interaksi. Tarik-menarik antara hadiah linier dan hukuman interaksi inilah yang membuat energi minimum _hanya_ tercapai ketika tepat $K$ aset menyala.
    

Jika bagian ekspansi QUBO ini sudah dapat dipahami sepenuhnya, kita bisa melanjutkan ke **Bagian 2: Transformasi Affine Suku Penalti dari Variabel Biner ($x$) menuju Variabel Spin Ising ($s$ atau $z$)**. Apakah Anda siap untuk melanjutkannya?

---
Mari kita lanjutkan ke **Bagian 2: Transformasi Affine Suku Penalti menuju Hamiltonian Ising**.

Pada tahap ini, kita akan mengubah persamaan fungsi penalti yang masih dalam format variabel biner / QUBO ($x_i \in \{0, 1\}$) menjadi format variabel spin kuantum / Ising ($s_i \in \{-1, 1\}$). Bentuk inilah yang nantinya bisa diterjemahkan menjadi operator Pauli-Z ($\hat{Z}$) untuk algoritma VQE.

---

# Bagian 5: Transformasi Affine dan Parameter Penalti Ising

#### 1. Persamaan Awal dan Aturan Transformasi

Mari kita ingat kembali bentuk final QUBO dari fungsi penalti yang kita dapatkan di Bagian 1:

$$P(\mathbf{x}) = \lambda (1 - 2K) \sum_{i=1}^N x_i + 2\lambda \sum_{i < j} x_i x_j + \lambda K^2$$

Aturan transformasi _affine_ standar dari variabel biner ke variabel spin adalah:

$$x_i = \frac{1 + s_i}{2}$$

Kita akan mensubstitusikan nilai $x_i$ ini ke dalam Suku Linier dan Suku Kuadratik secara terpisah agar tidak membingungkan.

#### 2. Ekspansi Suku Linier

Substitusikan ke dalam suku linier:

$$L_{pen} = \lambda (1 - 2K) \sum_{i=1}^N \left( \frac{1 + s_i}{2} \right)$$

$$L_{pen} = \frac{\lambda (1 - 2K)}{2} \sum_{i=1}^N s_i + \frac{\lambda (1 - 2K) N}{2}$$

Perhatikan bahwa suku pertama adalah komponen _bias lokal/medan magnet_, sedangkan suku kedua adalah konstanta yang akan masuk ke _offset_ energi.

#### 3. Ekspansi Suku Kuadratik (Interaksi)

Substitusikan ke dalam suku interaksi antar variabel:

$$Q_{pen} = 2\lambda \sum_{i < j} \left( \frac{1 + s_i}{2} \right) \left( \frac{1 + s_j}{2} \right)$$

$$Q_{pen} = 2\lambda \sum_{i < j} \frac{1 + s_i + s_j + s_i s_j}{4}$$

$$Q_{pen} = \frac{\lambda}{2} \sum_{i < j} s_i s_j + \frac{\lambda}{2} \sum_{i < j} (s_i + s_j) + \frac{\lambda}{2} \sum_{i < j} 1$$

Di sini ada sebuah trik matematis atau properti penyederhanaan yang sangat penting. Pada suku $\sum_{i < j} (s_i + s_j)$, setiap variabel $s_i$ akan muncul tepat sebanyak $(N - 1)$ kali karena ia berpasangan dengan semua aset lainnya. Sehingga:

$$\sum_{i < j} (s_i + s_j) = (N - 1) \sum_{i=1}^N s_i$$

Sementara itu, suku $\sum_{i < j} 1$ adalah jumlah semua pasangan yang mungkin (kombinasi 2 dari $N$), yaitu $\frac{N(N - 1)}{2}$.

Masukkan kembali penyederhanaan ini:

$$Q_{pen} = \frac{\lambda}{2} \sum_{i < j} s_i s_j + \frac{\lambda (N - 1)}{2} \sum_{i=1}^N s_i + \frac{\lambda N(N - 1)}{4}$$

#### 4. Pengelompokan menjadi Parameter Ising Penalti

Sekarang kita jumlahkan kembali $L_{pen}$, $Q_{pen}$, dan konstanta awal $\lambda K^2$. Format Hamiltonian Ising adalah $H_{pen} = \sum_{i < j} J^{pen}_{ij} s_i s_j + \sum_i h^{pen}_i s_i + E^{pen}_{offset}$.

Mari kita ekstrak parameternya satu per satu:

**A. Kekuatan Kopling Penalti ($J^{pen}_{ij}$)**

Ini diambil murni dari koefisien di depan $s_i s_j$:

$$\mathbf{J^{pen}_{ij} = \frac{\lambda}{2}}$$

_Interpretasi:_ Perhatikan bahwa nilai kopling ini **sama untuk setiap pasangan aset** dan selalu bernilai positif. Ini memberikan dorongan tolakan (_antiferromagnetic_) yang seragam ke seluruh sistem agar spin tidak cenderung sejajar (tidak semuanya $+1$ atau $-1$).

**B. Medan Magnet Lokal Penalti ($h^{pen}_i$)**

Ini adalah gabungan dari koefisien linier di $L_{pen}$ dan limpahan linier dari $Q_{pen}$:

$$h^{pen}_i = \frac{\lambda (1 - 2K)}{2} + \frac{\lambda (N - 1)}{2}$$

Faktorkan $\frac{\lambda}{2}$:

$$h^{pen}_i = \frac{\lambda}{2} (1 - 2K + N - 1)$$

$$\mathbf{h^{pen}_i = \frac{\lambda}{2} (N - 2K)}$$

_Interpretasi:_ Ini adalah bagian yang paling elegan. Medan lokal penalti ini bergantung pada selisih antara jumlah total aset ($N$) dan dua kali lipat target aset ($2K$). Jika $N > 2K$ (misal pilih 2 dari 10 saham), maka $h^{pen}$ bernilai positif, yang secara alamiah "menekan" spin menuju $-1$ (keluar portofolio) agar tidak terlalu banyak saham yang terpilih.

**C. Energi Offset Penalti ($E^{pen}_{offset}$)**

Ini adalah kumpulan semua konstanta. Meskipun tidak dimasukkan ke dalam operator VQE, nilainya penting untuk mencocokkan total energi klasik dengan energi kuantum nantinya:

$$E^{pen}_{offset} = \frac{\lambda (1 - 2K) N}{2} + \frac{\lambda N(N - 1)}{4} + \lambda K^2$$

---

### Kesimpulan dan Integrasi Final

Dengan selesainya Bagian 2 ini, Anda telah memiliki kepingan _puzzle_ yang terakhir. Seperti yang kita diskusikan pada _prompt_ sebelumnya (dan yang tertulis di `main.pdf`), langkah terakhir sebelum masuk ke mesin VQE adalah **menjumlahkan parameter dari _Game Theory_ dengan parameter Penalti**:

1. **Operator Interaksi Total:**
    
    $$J^{total}_{ij} = J^{GT}_{ij} + J^{pen}_{ij} = \frac{\gamma}{4} \sigma_{ij} + \frac{\lambda}{2}$$
    
2. **Operator Medan Lokal Total:**
    
    $$h^{total}_i = h^{GT}_i + h^{pen}_i = \left[ \frac{1}{2} \left( \frac{\gamma}{2} \sigma_{ii} - \mu_i \right) + \frac{\gamma}{4} \sum_{j \neq i} \sigma_{ij} \right] + \frac{\lambda}{2} (N - 2K)$$
    

Hamiltonian Final Anda ($\hat{H}_{final}$) siap dikonstruksi menggunakan $J^{total}$ dan $h^{total}$ dan dijalankan di Qiskit atau VQE _solver_ lainnya!

Apakah konklusi matematis ini sudah menjawab kebutuhan Anda secara menyeluruh untuk mengawinkan _Game Theory_, objektif Markowitz, Penalti, dan VQE?