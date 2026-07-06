# Penurunan Model Hamiltonian Ising dari Data Finansial dan Game Theory

Dokumen ini merinci prosedur matematis untuk mentransformasikan data pergerakan harga aset finansial menjadi model *Hamiltonian Ising* melalui kerangka kerja *Potential Game* dan *Inverse Ising Problem*.

## 1. Representasi Pergerakan Harga ke dalam Variabel Spin
Langkah pertama dalam *Econophysics* adalah memetakan perilaku pasar yang diskret ke dalam sistem fisik. Arah pergerakan harga harian saham $i$ didefinisikan sebagai variabel *spin* Ising $s_i$:

$$s_i = \begin{cases} +1, & \text{jika harga naik (Up)} \\ -1, & \text{jika harga turun (Down)} \end{cases}$$ (1)

Untuk empat buah saham $A$, $B$, $C$, dan $D$, terdapat enam kemungkinan kombinasi pasangan. Kita buat tabel kontingensinya satu per satu:

### Tabel 1: Pasangan A-B
| A \ B | Up (+1) | Down (-1) |
| :--- | :---: | :---: |
| **Up (+1)** | $p_{AB}$ | $q_{AB}$ |
| **Down (-1)** | $r_{AB}$ | $s_{AB}$ |

### Tabel 2: Pasangan A-C
| A \ C | Up (+1) | Down (-1) |
| :--- | :---: | :---: |
| **Up (+1)** | $p_{AC}$ | $q_{AC}$ |
| **Down (-1)** | $r_{AC}$ | $s_{AC}$ |

### Tabel 3: Pasangan A-D
| A \ D | Up (+1) | Down (-1) |
| :--- | :---: | :---: |
| **Up (+1)** | $p_{AD}$ | $q_{AD}$ |
| **Down (-1)** | $r_{AD}$ | $s_{AD}$ |

### Tabel 4: Pasangan B-C
| B \ C | Up (+1) | Down (-1) |
| :--- | :---: | :---: |
| **Up (+1)** | $p_{BC}$ | $q_{BC}$ |
| **Down (-1)** | $r_{BC}$ | $s_{BC}$ |

### Tabel 5: Pasangan B-D
| B \ D | Up (+1) | Down (-1) |
| :--- | :---: | :---: |
| **Up (+1)** | $p_{BD}$ | $q_{BD}$ |
| **Down (-1)** | $r_{BD}$ | $s_{BD}$ |

### Tabel 6: Pasangan C-D
| C \ D         | Up (+1)  | Down (-1) |
| :------------ | :------: | :-------: |
| **Up (+1)**   | $p_{CD}$ | $q_{CD}$  |
| **Down (-1)** | $r_{CD}$ | $s_{CD}$  |

| Up \ Down |                A                 |                B                 |                C                 |                D                 |
| :-------- | :------------------------------: | :------------------------------: | :------------------------------: | :------------------------------: |
| **A**     | $p_{A\uparrow}, p_{A\downarrow}$ | $p_{A\uparrow}, p_{B\downarrow}$ | $p_{A\uparrow}, p_{C\downarrow}$ | $p_{A\uparrow}, p_{D\downarrow}$ |
| **B**     | $p_{B\uparrow}, p_{A\downarrow}$ | $p_{B\uparrow}, p_{B\downarrow}$ | $p_{B\uparrow}, p_{C\downarrow}$ | $p_{B\uparrow}, p_{D\downarrow}$ |
| **C**     | $p_{C\uparrow}, p_{A\downarrow}$ | $p_{C\uparrow}, p_{B\downarrow}$ | $p_{C\uparrow}, p_{C\downarrow}$ | $p_{C\uparrow}, p_{D\downarrow}$ |
| **D**     | $p_{D\uparrow}, p_{A\downarrow}$ | $p_{D\uparrow}, p_{B\downarrow}$ | $p_{D\uparrow}, p_{C\downarrow}$ | $p_{D\uparrow}, p_{D\downarrow}$ |

| Up \ Down |                A                 |                B                 |                C                 |                D                 |
| :-------- | :------------------------------: | :------------------------------: | :------------------------------: | :------------------------------: |
| **A**     | $\mu_{A\uparrow}, \mu_{A\downarrow}$ | $\mu_{A\uparrow}, \mu_{B\downarrow}$ | $\mu_{A\uparrow}, \mu_{C\downarrow}$ | $\mu_{A\uparrow}, \mu_{D\downarrow}$ |
| **B**     | $\mu_{B\uparrow}, \mu_{A\downarrow}$ | $\mu_{B\uparrow}, \mu_{B\downarrow}$ | $\mu_{B\uparrow}, \mu_{C\downarrow}$ | $\mu_{B\uparrow}, \mu_{D\downarrow}$ |
| **C**     | $\mu_{C\uparrow}, \mu_{A\downarrow}$ | $\mu_{C\uparrow}, \mu_{B\downarrow}$ | $\mu_{C\uparrow}, \mu_{C\downarrow}$ | $\mu_{C\uparrow}, \mu_{D\downarrow}$ |
| **D**     | $\mu_{D\uparrow}, \mu_{A\downarrow}$ | $\mu_{D\uparrow}, \mu_{B\downarrow}$ | $\mu_{D\uparrow}, \mu_{C\downarrow}$ | $\mu_{D\uparrow}, \mu_{D\downarrow}$ |

### Kalkulasi Nilai Harapan Kondisional (Expected Return)
Setelah frekuensi ditentukan, kita hitung total imbal hasil (*return*) untuk setiap kuadran. Untuk pasangan aset $i$ dan $j$ (di mana $i, j \in \{A, B, C, D\}$):

- **Kondisi Up-Up ($V_{uu, ij}$):**
$$V_{uu, ij} = \sum_{k=1}^{p_{ij}} (R_{i,k} + R_{j,k})$$

- **Kondisi Up-Down ($V_{ud, ij}$):**
$$V_{ud, ij} = \sum_{k=1}^{q_{ij}} (R_{i,k} + R_{j,k})$$

- **Kondisi Down-Up ($V_{du, ij}$):**
$$V_{du, ij} = \sum_{k=1}^{r_{ij}} (R_{i,k} + R_{j,k})$$

- **Kondisi Down-Down ($V_{dd, ij}$):**
$$V_{dd, ij} = \sum_{k=1}^{s_{ij}} (R_{i,k} + R_{j,k})$$

Rumus di atas berlaku untuk keenam pasangan aset: **AB, AC, AD, BC, BD, dan CD**. Penjumlahan dilakukan pada hari-hari ($k$) di mana kedua saham tersebut memenuhi kondisi pergerakan pada sel tabel kontingensi masing-masing.

## 2. Ekstraksi Parameter Hamiltonian (Inverse Ising Problem)
Kita asumsikan sistem pergerakan harga dapat direpresentasikan oleh fungsi *return* kondisional $V(s_A, s_B)$ yang mengikuti bentuk umum Hamiltonian Ising dua-bodi:

$$V(s_A, s_B) = C + h_A s_A + h_B s_B + J_{AB} s_A s_B$$ (2)

Di mana:
- $C$: Konstanta *baseline return* pasar.
- $h_i$: Medan lokal (*local field*) yang merepresentasikan momentum intrinsik saham $i$.
- $J_{AB}$: Parameter interaksi (*coupling*) yang merepresentasikan korelasi atau sinergi antar saham.

Berdasarkan data historis, kita menghitung total *return* gabungan untuk setiap kuadran: $V_{uu}, V_{ud}, V_{du}, V_{dd}$. Hal ini menghasilkan sistem persamaan linier berikut:

$$\begin{aligned} V(+1, +1) &= C + h_A + h_B + J_{AB} = V_{uu} \\ V(+1, -1) &= C + h_A - h_B - J_{AB} = V_{ud} \\ V(-1, +1) &= C - h_A + h_B - J_{AB} = V_{du} \\ V(-1, -1) &= C - h_A - h_B + J_{AB} = V_{dd} \end{aligned}$$ (3)

Dengan menggunakan aljabar linier untuk setiap tabel, kita mendapatkan solusi unik untuk setiap parameter:

### A. Rumus 6 Interaksi (Coupling $J_{ij}$)
Suku interaksi ini menangkap kekuatan korelasi antar saham.
1. $J_{AB} = \frac{1}{4}(V_{uu, AB} - V_{ud, AB} - V_{du, AB} + V_{dd, AB})$
2. $J_{AC} = \frac{1}{4}(V_{uu, AC} - V_{ud, AC} - V_{du, AC} + V_{dd, AC})$
3. $J_{AD} = \frac{1}{4}(V_{uu, AD} - V_{ud, AD} - V_{du, AD} + V_{dd, AD})$
4. $J_{BC} = \frac{1}{4}(V_{uu, BC} - V_{ud, BC} - V_{du, BC} + V_{dd, BC})$
5. $J_{BD} = \frac{1}{4}(V_{uu, BD} - V_{ud, BD} - V_{du, BD} + V_{dd, BD})$
6. $J_{CD} = \frac{1}{4}(V_{uu, CD} - V_{ud, CD} - V_{du, CD} + V_{dd, CD})$

### B. Rumus 4 Bias (Momentum Lokal $h_i$)
Parameter ini menunjukkan momentum intrinsik masing-masing saham.
1. $h_A = \frac{1}{4}(V_{uu, AB} + V_{ud, AB} - V_{du, AB} - V_{dd, AB})$
2. $h_B = \frac{1}{4}(V_{uu, AB} - V_{ud, AB} + V_{du, AB} - V_{dd, AB})$
3. $h_C = \frac{1}{4}(V_{uu, AC} - V_{ud, AC} + V_{du, AC} - V_{dd, AC})$
4. $h_D = \frac{1}{4}(V_{uu, AD} - V_{ud, AD} + V_{du, AD} - V_{dd, AD})$

*(Catatan: Rumus bias di atas menggunakan referensi pasangan tertentu, namun secara matematis akan menghasilkan nilai yang sama jika data pergerakan individu saham tetap konsisten di semua tabel).*

## 3. Jembatan Game Theory: Potential Game
Dalam *Game Theory*, setiap saham atau agen dianggap ingin memaksimalkan fungsi utilitas atau potensial ($\Phi$). Sebaliknya, dalam fisika statistik, sistem cenderung mencari energi terendah atau Hamiltonian ($H$) minimum. Hubungan ekuivalensi antara keduanya adalah:

$$H = -\Phi$$ (5)

Maka, Hamiltonian untuk prediksi pergerakan pasar adalah:
$$H_{\text{prediksi}} = -C - h_A s_A - h_B s_B - J_{AB} s_A s_B$$ (6)

## 4. Optimisasi Seleksi Portofolio (QUBO)
Setelah mendapatkan bobot interaksi ($W_{ij} \approx J_{ij}$) dan skor individu ($V_i \approx h_i$), tahap berikutnya adalah memilih $K$ aset terbaik dari $N$ kandidat. Kita beralih ke variabel biner $x_i \in \{0, 1\}$ (0: tidak dipilih, 1: dipilih).

### A. Fungsi Objektif
Tujuannya adalah memaksimalkan total skor dari aset yang dipilih:
$$H_{\text{obj}} = -\left( \sum_{i=1}^N V_i x_i + \sum_{i<j}^N W_{ij} x_i x_j \right)$$ (7)

### B. Suku Penalti (*Penalty Term*)
Untuk memaksa sistem memilih tepat $K$ aset, kita gunakan metode *Lagrange Multiplier* dalam bentuk penalti kuadratik dengan bobot denda $A$:
$$H_{\text{pen}} = A \left( \sum_{i=1}^N x_i - K \right)^2$$ (8)

Jika syarat $\sum x_i = K$ terpenuhi, maka $H_{\text{pen}} = 0$. Jika melanggar, energi akan melonjak naik, sehingga algoritma optimisasi (seperti *Quantum Annealing*) akan menghindarinya.

## 5. Transformasi ke Model Ising Global
Untuk mengeksekusi Hamiltonian pada *hardware* kuantum, kita harus mengembalikan variabel biner $x_i$ ke variabel spin $s_i$ menggunakan transformasi *affine*:

$$x_i = \frac{s_i + 1}{2}$$ (9)

### Ekspansi Suku Penalti
Sebagai contoh untuk $N=4$ dan $K=2$, ekspansi suku penalti $A(x_A + x_B + x_C + x_D - 2)^2$ dalam variabel spin akan menghasilkan:
1. **Konstanta**: $4A$.
2. **Suku Linear (Medan Lokal Baru)**: $-3A s_i$.
3. **Suku Kuadratik (Interaksi Baru)**: $+2A s_i s_j$.

### Hamiltonian Total
$$H_{\text{total}} = H_{\text{obj}} + H_{\text{pen}}$$ (10)

Hasil akhirnya adalah Hamiltonian dalam bentuk baku Ising yang siap dihitung:
$$H_{\text{Ising}} = \sum_i h'_i s_i + \sum_{i<j} J'_{ij} s_i s_j + \text{Konstanta}$$ (11)

Di mana $h'_i$ dan $J'_{ij}$ adalah hasil penggabungan parameter dari data historis (Stage 1) dan parameter penalti seleksi (Stage 2).
