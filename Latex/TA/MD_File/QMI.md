# Quantum Mutual Information (QMI) & Ekstraksi Parameter Interaksi

Dokumen ini menjelaskan bagaimana korelasi informasi dalam ruang Hilbert digunakan untuk merekonstruksi parameter fisik dalam model *Ising Hamiltonian*—dengan pembedahan eksplisit mengenai apa yang sebenarnya dihitung (informasi klasik vs. kuantum sejati) dan framing yang jujur mengenai validitas *ansatz* ini.

## 1. Konvensi Dasar: Makna Vektor State
Sebelum memahami interaksi, kita harus sepakat pada representasi matematis dari status *qubit* tunggal.

### A. Basis Komputasi (Reduksionisme 1-Qubit)
Status sistem diwakili oleh vektor kolom dalam ruang kompleks $\mathbb{C}^2$.
- **Status $|0\rangle$ (Ground/Spin Up):**
  $$ |0\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix} $$
- **Status $|1\rangle$ (Excited/Spin Down):**
  $$ |1\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix} $$

**Insight Fisik:** Angka "1" di baris pertama $|0\rangle$ berarti probabilitas menemukan sistem di *state* 0 adalah $|1|^2 = 100\%$. Representasi ini bukan fisika murni—ini adalah *embedding* data keuangan ke dalam bahasa mekanika kuantum, yang memberi kita akses ke alat matematika yang kaya.

---

## 2. Sistem Komposit: Ruang Hilbert 2-Qubit
Saat kita memiliki dua aset atau dua *spin* ($i$ dan $j$), ruang statusnya membesar melalui operasi ***Tensor Product*** ($\otimes$).

### A. Konstruksi Basis Rangkap Dua
Ada 4 kombinasi kemungkinan status untuk 2 *qubit* (dimensi $2^2 = 4$):
1. $|00\rangle = [1, 0, 0, 0]^T$
2. $|01\rangle = [0, 1, 0, 0]^T$
3. $|10\rangle = [0, 0, 1, 0]^T$
4. $|11\rangle = [0, 0, 0, 1]^T$

Setiap *state* umum $|\psi\rangle_{ij}$ adalah superposisi dari keempat basis ini:
$$ |\psi\rangle_{ij} = \sum_{a,b \in \{0,1\}} \alpha_{ab} |ab\rangle \qquad (1) $$

> **Visualisasi (1):** Secara linear, ini adalah penjumlahan vektor kolom:
>  $$ 
\begin{split}
 |\psi\rangle_{ij} &= \alpha_{00} |00\rangle + \alpha_{01} |01\rangle + \alpha_{10} |10\rangle + \alpha_{11} |11\rangle \\\\
 
 |\psi\rangle_{ij} &= \alpha_{00} \begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \end{pmatrix} + \alpha_{01} \begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \end{pmatrix} + \alpha_{10} \begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \end{pmatrix} + \alpha_{11} \begin{pmatrix} 0 \\ 0 \\ 0 \\ 1 \end{pmatrix} = \begin{pmatrix} \alpha_{00} \\ \alpha_{01} \\ \alpha_{10} \\ \alpha_{11} \end{pmatrix} 
 \end{split} $$
> Di mana $\alpha_{ab}$ adalah amplitudo probabilitas kompleks.

---

## 3. Matriks Densitas: Jembatan ke Informasi Statistik

### A. Keadaan Murni (*Pure State*)
*Pure state* adalah *state* yang sepenuhnya diketahui: tidak ada ketidakpastian klasik. Didefinisikan sebagai *outer product* dari *state* (1):
$$ \rho_{ij}^{(pure)} = |\psi\rangle\langle\psi| \qquad (2) $$

> **Visualisasi (2):** Ini adalah perkalian matriks $(4 \times 1)$ dengan $(1 \times 4)$:
> $$ \rho_{ij} = \begin{pmatrix} \alpha_{00} \\ \alpha_{01} \\ \alpha_{10} \\ \alpha_{11} \end{pmatrix} \begin{pmatrix} \alpha_{00}^* & \alpha_{01}^* & \alpha_{10}^* & \alpha_{11}^* \end{pmatrix} = \begin{pmatrix} \alpha_{00}\alpha_{00}^* & \alpha_{00}\alpha_{01}^* & \alpha_{00}\alpha_{10}^* & \alpha_{00}\alpha_{11}^* \\ \alpha_{01}\alpha_{00}^* & \alpha_{01}\alpha_{01}^* & \alpha_{01}\alpha_{10}^* & \alpha_{01}\alpha_{11}^* \\ \alpha_{10}\alpha_{00}^* & \alpha_{10}\alpha_{01}^* & \alpha_{10}\alpha_{10}^* & \alpha_{10}\alpha_{11}^* \\ \alpha_{11}\alpha_{00}^* & \alpha_{11}\alpha_{01}^* & \alpha_{11}\alpha_{10}^* & \alpha_{11}\alpha_{11}^* \end{pmatrix} $$

> **⚠️ Peringatan Kritis — Masalah Pure State untuk Data Keuangan:**
> Jika kita menggunakan *encoder* $|\psi\rangle_{ij} = \sum_{a,b} \sqrt{P(a,b)} |ab\rangle$ untuk mengubah data *candlestick* menjadi *state* kuantum, maka $\rho_{ij}^{(pure)} = |\psi\rangle\langle\psi|$ adalah proyektor *rank-1*. Konsekuensinya fatal bagi QMI: karena ini *pure state*, **entropi sistem gabungan $S(\rho_{ij}) = 0$ selalu**. Maka QMI menjadi $I(i:j) = S(\rho_i) + S(\rho_j) - 0 = S(\rho_i) + S(\rho_j)$—yang hanya merupakan jumlah entropi marginal, bukan korelasi sejati antar aset. Korelasi aslinya (koherensi *off-diagonal*) justru hilang karena *pure state* dari data klasik tidak mengandung *entanglement* nyata.

### B. Keadaan Campuran (*Mixed State*) — Pilihan yang Tepat untuk Data Keuangan
Jika sistem memiliki ketidakpastian klasik (seperti *ensemble* historis data pasar), kita menggunakan *mixed state*. Untuk data *candlestick*, *mixed state* diagonal yang paling tepat adalah:
$$ \rho_{ij}^{(mixed)} = \sum_{a,b} P(a,b) |ab\rangle\langle ab| \qquad (3) $$

> **Visualisasi (3):** *Mixed state* diagonal ini berbentuk matriks diagonal berisi probabilitas:
> $$ \rho_{ij}^{(mixed)} = \begin{pmatrix} P(00) & 0 & 0 & 0 \\ 0 & P(01) & 0 & 0 \\ 0 & 0 & P(10) & 0 \\ 0 & 0 & 0 & P(11) \end{pmatrix} $$
> Ini jauh lebih bersih dan jujur. Tidak ada elemen *off-diagonal*—karena data historis kita memang klasik, tidak mengandung *superposisi* fisik.

> **Mengapa Ini Lebih Baik?**
> Dengan *mixed state* diagonal, $S(\rho_{ij})$ **tidak lagi nol**, dan QMI yang dihasilkan menjadi:
> $$ I(i:j) = S(\rho_i) + S(\rho_j) - S(\rho_{ij}) \neq 0 $$
> Yang secara matematis **persis ekuivalen** dengan *classical mutual information*:
> $$ I_{classical}(i:j) = \sum_{a,b} P(a,b) \log \frac{P(a,b)}{P(a)P(b)} $$
> Ini lebih jujur: kita mengakui bahwa yang kita hitung adalah informasi klasik yang di-*embed* ke dalam formalisme kuantum—bukan korelasi kuantum sejati (*entanglement*). Dan justru karena "jujur" ini, hasil numeriknya lebih andal dan interpretasinya lebih solid.

> **Visualisasi (Mixed vs. Pure State):** Secara intuitif, ini adalah perbedaan antara mendeskripsikan ensemble historis (mixed) vs. menciptakan *superposisi* fiktif dari data (pure). Analogi: membuat dadu berisi set probabilitas (mixed) vs. melempar dadu yang berada dalam superposisi (pure)—keduanya menggunakan bahasa kuantum, tapi hanya yang pertama yang terhubung ke realita data historis kita.

Elemen matriks (3) didefinisikan sebagai:
$$ \rho_{ab,ab} = P(a,b), \quad \rho_{ab,cd} = 0 \text{ untuk } (a,b) \neq (c,d) \qquad (4) $$

**Verifikasi Parameter:** Matriks $\rho^{(mixed)}$ wajib memenuhi:
1. **Hermitian:** $\rho = \rho^\dagger$ — terpenuhi karena elemen diagonal real.
2. **Trace = 1:** Total probabilitas harus 100%.
$$ \text{Tr}(\rho^{(mixed)}) = \sum_{a,b} P(a,b) = 1 \qquad (5) $$

> **Visualisasi (5):** Jumlahan semua elemen diagonal = 1, sesuai normalisasi probabilitas.

---

## 4. Jembatan Logika: Partial Trace & Informasi Lokal
Untuk mendapatkan status lokal *qubit* $i$, kita harus melakukan *trace-out* terhadap *qubit* $j$.

**Filosofi:** Kita menjumlahkan semua kemungkinan status *qubit* $j$ untuk melihat perilaku rata-rata *qubit* $i$.
$$ \rho_i = \text{Tr}_j(\rho_{ij}) = \sum_{b \in \{0,1\}} \langle b |_j \rho_{ij} | b \rangle_j \qquad (6) $$

> **Visualisasi (6):** Untuk *mixed state* diagonal (3), *partial trace* cukup menjumlahkan baris-baris yang memiliki qubit $i$ yang sama:
> $$ \rho_i = \begin{pmatrix} P(00) + P(01) & 0 \\ 0 & P(10) + P(11) \end{pmatrix} = \begin{pmatrix} P(i=0) & 0 \\ 0 & P(i=1) \end{pmatrix} $$
> Hasilnya adalah matriks densitas marginal untuk *qubit* $i$—juga diagonal, lebih intuitif.

**Reduksionisme (Langkah Aljabar):**

### A. Matriks Densitas Terreduksi $\rho_i$
Untuk *mixed state* diagonal:
$$ (\rho_i)_{ac} = \sum_{b \in \{0,1\}} \rho_{ab,cb} \qquad (7) $$

> **Visualisasi (7):**
> $$ \rho_i = \begin{pmatrix} P(00) + P(01) & 0 \\ 0 & P(10) + P(11) \end{pmatrix} = \begin{pmatrix} P(i{=}0) & 0 \\ 0 & P(i{=}1) \end{pmatrix} $$

### B. Matriks Densitas Terreduksi $\rho_j$
*Trace-out qubit* pertama ($\text{Tr}_i$):
$$ \rho_j = \sum_{a \in \{0,1\}} \rho_{ab,ad} \qquad (8) $$

> **Visualisasi (8):**
> $$ \rho_j = \begin{pmatrix} P(00) + P(10) & 0 \\ 0 & P(01) + P(11) \end{pmatrix} = \begin{pmatrix} P(j{=}0) & 0 \\ 0 & P(j{=}1) \end{pmatrix} $$

---

## 5. Menghitung Quantum Mutual Information (QMI)
Gunakan **Entropi Von Neumann ($S$)** pada hasil persamaan (3), (7), dan (8):
$$ S(\rho) = -\text{Tr}(\rho \ln \rho) \qquad (9) $$

> **Visualisasi (9):** Untuk matriks diagonal, cukup jumlahkan $-p \ln(p)$ untuk setiap elemen diagonal:
> $$ S(\rho_i) = -P(i{=}0) \ln P(i{=}0) - P(i{=}1) \ln P(i{=}1) $$
> $$ S(\rho_{ij}^{(mixed)}) = -\sum_{a,b} P(a,b) \ln P(a,b) $$
> Ini adalah **Shannon entropy** standar! Tidak ada ambiguitas numerik.

**Definisi QMI:**
$$ I(i:j) = S(\rho_i) + S(\rho_j) - S(\rho_{ij}) \qquad (10) $$

> **Visualisasi (10):** Ini adalah operasi skalar sederhana.
> Contoh: Jika $P(00) = P(11) = 0.45$ dan $P(01) = P(10) = 0.05$ (dua aset sangat berkorelasi positif):
> - $S(\rho_i) = S(\rho_j) \approx 0.69$ (mendekati $\ln 2$, karena masing-masing aset hampir 50-50 naik/turun)
> - $S(\rho_{ij}) = -2(0.45\ln 0.45) - 2(0.05 \ln 0.05) \approx 0.80$ (entropi sistem gabungan)
> - $I(i:j) = 0.69 + 0.69 - 0.80 = 0.58$ (informasi mutual yang cukup besar)
> Bandingkan jika kedua aset independen ($P(ab) = P(a)P(b)$): $I(i:j) = 0$ (tidak ada informasi bersama).

---

## 6. Mengapa QMI Menjadi Landasan Parameter $J_{ij}$? (Framing sebagai Ansatz)

Dalam *Inverse Ising Problem*, kita ingin mencari $J_{ij}$ yang paling cocok dengan data. Perlu ditegaskan bahwa hubungan $J_{ij} \propto \sqrt{I(i:j)}$ merupakan sebuah ***ansatz* desain yang termotivasi**, bukan derivasi dari *first principles*. Berikut justifikasinya:

1. **Motivasi dari Limit Termal:** Dalam distribusi Boltzmann $P \propto e^{-\beta H}$, pada *high-temperature limit*, korelasi antar *spin* menjadi $I(i:j) \approx \frac{1}{2}(\beta J_{ij})^2$. Ini memberi hubungan $|J_{ij}| \approx \frac{1}{\beta}\sqrt{2I(i:j)}$. Namun, relasi ini hanya valid jika $\rho_{ij}$ berasal dari distribusi Boltzmann—bukan dari data *candlestick* historis seperti pada kita. Penggunaan relasi ini pada data klasik adalah ekstrapolasi.

2. **Validitas sebagai Ansatz:** Meskipun demikian, *ansatz* $J_{ij} \propto \sqrt{I(i:j)}$ memenuhi semua syarat fisikal yang diperlukan:
   - $J_{ij} = 0$ saat $I(i:j) = 0$ (tidak ada korelasi → tidak ada kopling).
   - $|J_{ij}|$ membesar secara monoton saat informasi bersama meningkat.
   - Skala $\kappa$ dapat dikalibrasi dari data pasar ($\kappa \approx \sqrt{2} k_B T$, $T \sim \sigma_{avg}$).

3. **Catatan Klasikal:** Karena kita menggunakan *mixed state* diagonal, QMI yang dihitung **persis ekuivalen** dengan *classical mutual information* Shannon. Ini berarti $J_{ij}$ yang kita gunakan bukan mengukur korelasi kuantum (entanglement), melainkan **ketergantungan statistik klasik** yang dikodekan ke dalam formalisme kuantum. Ini bukan kelemahan—justru ini adalah poin kejujuran yang membuat model kita lebih kokoh secara fundamental. Ada preseden dalam literatur *econophysics* (Mantegna & Stanley, 1999) untuk pendekatan ini.

4. **Penentuan Tanda:** QMI selalu positif, sehingga tidak membedakan *co-movement* (pergerakan searah, aset saling melengkapi) dari *anti-korelasi* (pergerakan berlawanan, berguna untuk *hedging*). Oleh karena itu, tanda $J_{ij}$ diperoleh dari koefisien korelasi Pearson $\rho_{ij}$ antara pengembalian (*return*) $r_i$ dan $r_j$:
   $$ \rho_{ij} = \frac{\sum_{t=1}^{T}(r_{i,t} - \bar{r}_i)(r_{j,t} - \bar{r}_j)}{\sqrt{\sum_t(r_{i,t}-\bar{r}_i)^2 \cdot \sum_t(r_{j,t}-\bar{r}_j)^2}} \qquad (11) $$
   Arah korelasi kemudian diekstrak menggunakan fungsi *signum*:
   $$ \text{sgn}(\rho_{ij}) = \frac{\rho_{ij}}{|\rho_{ij}|} \qquad (12) $$
   Fungsi tanda ini menentukan sifat fisik interaksi Ising: tanda negatif ($-1$) mengindikasikan interaksi *ferromagnetic* (*co-movement*), sedangkan tanda positif ($+1$) mengindikasikan interaksi *antiferromagnetic* (*hedging*).

> **Rumus Final dengan Koefisien Normalisasi:**
> $$ J_{ij} = \kappa \cdot \text{sgn}(\rho_{ij}) \sqrt{I(i:j)} \qquad (13) $$
> Di mana $\kappa \approx \sqrt{2} k_B T$ adalah koefisien konversi dari satuan informasi (*nats*) ke satuan energi (risiko), dan $T \sim \sigma_{avg}$ adalah "Suhu Pasar" yang diekstraksi dari volatilitas rata-rata historis.

> **Peringatan Kalibrasi Skala:**
> Nilai $I(i:j)$ (dalam *nats*) dan nilai penalti $A$ (dimensi risiko) memiliki domain numerik yang berbeda. Koefisien $\kappa$ harus dikalibrasi secara hati-hati agar $J_{ij}$ sepadan skalanya dengan $A/2$. Jika tidak, lanskap energi *Hamiltonian* akan terdistorsi: model akan mengabaikan optimasi portofolio demi kepatuhan batasan, atau sebaliknya.
