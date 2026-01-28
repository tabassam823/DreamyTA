---
marp: true
theme: default
paginate: true
backgroundColor: #fbfbfb
header: 'Pengantar EWL Scheme'
footer: 'Materi Pengayaan Mahasiswa Baru | Lab Riset Operasi'
style: |
  section {
    font-family: 'Arial', sans-serif;
    justify-content: start;
  }
  h1 {
    color: #2c3e50;
  }
  h2 {
    color: #34495e;
    border-bottom: 2px solid #3498db;
    padding-bottom: 10px;
  }
  .highlight {
    color: #e74c3c;
    font-weight: bold;
  }
  .box {
    background-color: #ecf0f1;
    padding: 20px;
    border-radius: 5px;
    border-left: 5px solid #3498db;
  }
  table {
    margin-left: auto;
    margin-right: auto;
    border-collapse: collapse;
    width: 80%;
  }
  th, td {
    border: 1px solid #bdc3c7;
    padding: 10px;
    text-align: center;
  }

---

<!-- _class: lead -->
# Pengantar EWL Scheme
## Eisert-Wilkens-Lewenstein Protocol

**Jembatan Menuju Quantum Game Theory**
*Mengalahkan Dilema Klasik dengan Fisika Kuantum*

---

## 1. Latar Belakang
### Keterbatasan Game Theory Klasik

Dalam game klasik seperti **Prisoner's Dilemma**, pemain yang rasional seringkali terjebak dalam hasil yang buruk.

**Masalah:**
- Dua tahanan (Alice & Bob) diinterogasi terpisah.
- Jika keduanya kooperatif (diam), hukumannya ringan (3 tahun).
- Tapi karena takut dikhianati, logika rasional ("Nash Equilibrium") memaksa mereka saling berkhianat.
- **Hasil:** Keduanya dapat hukuman berat (5 tahun).

> **Pertanyaan:** Adakah cara agar mereka bisa bekerja sama *tanpa* berkomunikasi?
> **Jawabannya:** Ada, jika mereka punya "tali gaib" kuantum (Entanglement).

---

## 2. Aturan & Protokol EWL

Pada tahun 1999, Eisert, Wilkens, dan Lewenstein (EWL) membuat protokol untuk memainkan game ini di komputer kuantum.

**Alur Permainan (Sirkuit):**
1.  **State Awal:** Mulai dari state netral $\ket{00}$.
2.  **Entanglement ($\hat{J}$):** Operator yang membuat strategi Alice dan Bob saling terikat (berkorelasi kuat).
3.  **Strategi Pemain ($\hat{U}_A, \hat{U}_B$):** Alice dan Bob memutar qubit mereka masing-masing (memilih strategi).
4.  **Un-Entanglement ($\hat{J}^\dagger$):** Operator pembalik untuk membaca hasil interferensi.
5.  **Pengukuran:** Menentukan Payoff akhir.

---

## 3. Konsep Main: Ruang Strategi Baru

Di dunia klasik, strategi cuma ada dua: **0 (Diam)** atau **1 (Khianat)**.
Di dunia kuantum, strategi adalah **Rotasi Bola Bloch**.

### Keunggulan Kuantum:
1.  **Superposisi:**
    Pemain bisa memilih strategi "setengah diam, setengah khianat" secara bersamaan.
    $$ \ket{\psi} = \alpha\ket{0} + \beta\ket{1} $$
2.  **Entanglement:**
    Keputusan Alice seketika mempengaruhi probabilitas hasil Bob, dan sebaliknya. Ini "merusak" asumsi klasik bahwa keputusan dibuat terpisah.

---

## 4. Formalisme Matematika

State akhir ($\ket{\psi_f}$) dari permainan ditentukan oleh persamaan operator berikut:

$$ \ket{\psi_f} = \hat{J}^\dagger (\hat{U}_A \otimes \hat{U}_B) \hat{J} \ket{00} $$

Dimana operator Entanglement $\hat{J}$ biasanya didefinisikan sebagai:
$$ \hat{J} = \exp\left(i \frac{\gamma}{2} \hat{\sigma}_x \otimes \hat{\sigma}_x\right) $$

- Jika $\\gamma = 0$: Game kembali menjadi **Klasik**.
- Jika $\\gamma = \pi/2$: Game memiliki **Maximum Entanglement**.

Payoff dihitung dari probabilitas state akhir:
$$ \$ = \sum P_{ij} \cdot \text{Payoff}_{ij} = \sum |\braket{ij|\psi_f}|^2 \cdot \pi_{ij} $$

---

## 5. Penurunan Analisis Numerik (Studi Kasus)

Mari kita lihat bagaimana **Strategi Ajaib Kuantum** ($Q$) mengalahkan strategi klasik.

**Matriks Payoff Prisoner's Dilemma:**

| Alice \ Bob | Cooperate (C) | Defect (D) |
| :--- | :---: | :---: |
| **Cooperate (C)** | (3, 3) | (0, 5) |
| **Defect (D)** | (5, 0) | (1, 1) |

- **Klasik:** Nash Equilibrium adalah **(D, D)**. Poin = 1.
- **Kuantum:** Kita gunakan strategi "Miracle Move" ($Q = i\sigma_y$) untuk kedua pemain.

---

## 5. Penurunan Analisis Numerik (Lanj.)

Jika Alice dan Bob sama-sama menggunakan strategi Kuantum $Q$ pada entanglement maksimal:

**1. Operasi Matematis:**
Strategi $Q$ memutar fase qubit sedemikian rupa sehingga ketika operator $\hat{J}^\dagger$ diterapkan, amplitudo untuk state "Khianat" saling meniadakan (Interferensi Destruktif).

**2. Hasil State Akhir:**
Secara matematis, state akhirnya menjadi:
$$ \ket{\psi_f} = \ket{00} \quad (\text{Murni Cooperate}) $$

**3. Payoff Akhir:**
$$ \text{Payoff} = (100\% \times 3) = \mathbf{3} $$
---
**Kesimpulan:**
Tanpa komunikasi, strategi kuantum memaksa hasil (3,3) yang lebih tinggi daripada hasil rasional klasik (1,1).

---

## 6. Hubungan dengan Riset Kita

Kenapa kita pakai ini untuk saham?

1.  **Pasar sebagai Lawan:**
    Dalam riset kita, "Bob" adalah Pasar (Nature).
2.  **Menghindari Crash:**
    Sama seperti kita ingin menghindari hasil (1,1) di Prisoner's Dilemma, kita ingin menghindari kerugian saat pasar Crash.
3.  **Korelasi Aset:**
    Entanglement ($\\hat{J}$) kita gunakan untuk mengikat aset-aset dalam portofolio agar mereka bekerja sama menyeimbangkan risiko, jauh lebih baik daripada korelasi statistik biasa.

---

<!-- _class: invert -->
# Terima Kasih
## Lanjut ke Quantum Game Theory?
