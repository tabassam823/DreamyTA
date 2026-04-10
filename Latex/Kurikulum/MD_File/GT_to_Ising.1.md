# Transformasi Model Ising: Dari Fisika Statistik hingga Teori Permainan dan Optimisasi Portofolio

Dokumen ini merangkum evolusi Model Ising, konsep *Potential Game*, dan panduan matematis lengkap untuk memetakan masalah pemilihan portofolio saham ke dalam arsitektur komputasi kuantum (QUBO/Ising).

---

## 1. Sejarah Singkat Model Ising dan Ekstensinya

Model Ising tidak lahir langsung sebagai alat optimisasi finansial. Ia berevolusi melintasi beberapa disiplin ilmu selama hampir satu abad:

* **Wilhelm Lenz & Ernst Ising (1920-1924):** Lenz menggagas model matematis sederhana untuk feromagnetisme di mana momen dipol atom (spin) hanya memiliki dua keadaan ($+1$ atau $-1$). Ising menyelesaikannya untuk 1-Dimensi, namun salah menyimpulkan bahwa model ini tidak memiliki transisi fase.
* **Lev Landau (1937):** Melalui Teori Ginzburg-Landau, ia membuktikan bahwa interaksi antar variabel (spin) muncul secara alami dari **ekspansi deret Taylor** terhadap energi bebas sistem ruang kontinu. Suku gradien $(\nabla \psi)^2$ adalah representasi makroskopis dari interaksi antar tetangga.
* **Lars Onsager (1944):** Membuktikan secara matematis bahwa Model Ising 2-Dimensi memiliki transisi fase, menjadikannya tonggak sejarah fisika statistik.
* **Richard Courant (1943) & Andrew Lucas (2014):** Courant memperkenalkan Metode Penalti (pengali Lagrange) untuk masalah optimisasi bersyarat. Lucas mempopulerkan kerangka kerja ini ke dalam mekanika kuantum dengan memetakan masalah NP-Hard ke format QUBO (*Quadratic Unconstrained Binary Optimization*), di mana Model Ising "dibajak" untuk menyelesaikan masalah kombinatorial dengan menambahkan **suku penalti kuadratik**.

---

## 2. Hubungan *Potential Game* dan Model Ising

Dalam Teori Permainan (*Game Theory*), sebuah *Potential Game* adalah sistem di mana insentif (perubahan *payoff*) dari semua pemain dapat dipetakan ke dalam satu fungsi global yang disebut **Fungsi Potensial ($\Phi$)**.

Pemain rasional selalu berusaha **memaksimalkan** Fungsi Potensial ($\Phi$). Sebaliknya, sistem fisika alamiah selalu berusaha **meminimalkan** Energi (Hamiltonian, $H$). Oleh karena itu, *Potential Game* dapat diterjemahkan secara langsung ke Model Ising dengan membalikkan tandanya:
$$H = -\Phi$$



Agar aturan sistem (seperti kuota atau batas anggaran) dipatuhi oleh pemain/algoritma, aturan tersebut harus dimasukkan sebagai **denda (penalti)** ke dalam fungsi utilitas sebelum diubah menjadi Hamiltonian.

---

## 3. Penurunan Matematis: Studi Kasus 4 Saham

**Tujuan:** Memilih tepat 2 saham optimal dari 4 pilihan saham (A, B, C, D) berdasarkan nilai individu ($V$) dan nilai sinergi/interaksi ($W$) yang diekstrak dari tabel kontingensi pergerakan harga.

### Langkah 1: Definisi Variabel dan Fungsi Objektif (QUBO)
Kita menggunakan variabel biner seleksi $x_i \in \{0, 1\}$. 
Kita merumuskan Hamiltonian Objektif ($H_{obj}$) untuk memaksimalkan *return*. Karena Hamiltonian mencari nilai minimum, kita menambahkan tanda minus.

$$H_{obj} = - \left( V_A x_A + V_B x_B + V_C x_C + V_D x_D + W_{AB} x_A x_B + W_{AC} x_A x_C + W_{AD} x_A x_D + W_{BC} x_B x_C + W_{BD} x_B x_D + W_{CD} x_C x_D \right)$$

### Langkah 2: Merumuskan Suku Penalti
Aturan portofolio mensyaratkan kita hanya boleh memilih tepat 2 saham.
$$\sum x_i = 2 \implies x_A + x_B + x_C + x_D - 2 = 0$$

Kita ubah menjadi suku penalti kuadratik dengan bobot denda $A$:
$$H_{pen} = A(x_A + x_B + x_C + x_D - 2)^2$$

### Langkah 3: Ekspansi Aljabar Suku Penalti
Di dalam QUBO, kuadrat dari variabel biner adalah variabel itu sendiri ($x_i^2 = x_i$). Kita jabarkan ekspansi kuadrat dari $H_{pen}$:
Misalkan $S = x_A + x_B + x_C + x_D$. Maka penalti adalah $A(S - 2)^2 = A(S^2 - 4S + 4)$.

* $S^2 = \sum x_i^2 + 2\sum_{i<j} x_i x_j = \sum x_i + 2\sum_{i<j} x_i x_j$
* $-4S = -4\sum x_i$

Gabungkan kembali ke dalam penalti:
$$H_{pen} = A \left( -3(x_A + x_B + x_C + x_D) + 2(x_A x_B + \dots + x_C x_D) + 4 \right)$$

### Langkah 4: Hamiltonian Total QUBO
Gabungkan $H_{obj}$ dan $H_{pen}$ yang sudah diekspansi. Kelompokkan berdasarkan variabel linear dan interaksi kuadratik:

$$H_{QUBO} = \sum_{i} (-V_i - 3A) x_i + \sum_{i<j} (-W_{ij} + 2A) x_i x_j + 4A$$



### Langkah 5: Transformasi Affine ke Model Ising
Untuk memproses matriks ini di *quantum annealer*, konversikan variabel QUBO ($x_i \in \{0, 1\}$) ke variabel Ising ($s_i \in \{-1, 1\}$) menggunakan substitusi:
$$x_i = \frac{s_i + 1}{2}$$

Substitusikan ke dalam $H_{QUBO}$ untuk mendapatkan bentuk akhir Ising:
$$H_{Ising} = \sum_{i} h_i s_i + \sum_{i < j} J_{ij} s_i s_j + C_{total}$$

*Keterangan:* Medan lokal ($h_i$) dan kekuatan interaksi ($J_{ij}$) yang baru akan secara otomatis mengandung kompensasi denda $A$, memaksa mesin mencari pasangan $s_i$ yang mematuhi aturan "hanya pilih 2".