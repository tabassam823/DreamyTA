---
marp: true
theme: default
paginate: true
backgroundColor: #fbfbfb
header: 'Pengantar Teori Permainan Bayesian'
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
  }

---

<!-- _class: lead -->
# Pengantar Bayesian Game Theory
## Mengambil Keputusan di Bawah Ketidakpastian

**Untuk Mahasiswa Baru**
*Dari Intuisi ke Analisis Numerik*

---

## 1. Latar Belakang
### Mengapa Game Theory "Klasik" Tidak Cukup?

Dalam **Game Theory Klasik (Nash Equilibrium)**, kita berasumsi:
1. Semua pemain tahu aturan main.
2. Semua pemain tahu *payoff* (imbalan) satu sama lain.
3. **Perfect Information:** Kita tahu siapa lawan kita dan apa motivasinya.

> **Tapi di Dunia Nyata...**
> - Saat main Poker, kita tidak tahu kartu lawan.
> - Saat lelang, kita tidak tahu budget lawan.
> - Saat investasi, kita tidak tahu apakah pasar akan **Naik (Bull)** atau **Hancur (Bear)**.

Inilah **Incomplete Information Game**. John Harsanyi (Nobel Prize 1994) memecahkan masalah ini dengan **Bayesian Game**.

---

## 2. Aturan & Konsep Dasar

Bayesian Game mengubah "Ketidaktahuan" menjadi "Probabilitas".

### Komponen Utama:
1. **Players (Pemain):** Para pengambil keputusan (Contoh: Anda vs Pasar).
2. **Actions (Aksi):** Pilihan yang tersedia (Contoh: Beli / Jual).
3. **Types ($\theta$):** Informasi rahasia yang dimiliki pemain.
   - *Contoh:* Lawan Anda mungkin bertipe "Agresif" atau "Pasif".
4. **Beliefs (Keyakinan/Probabilitas $p$):** 
   - Karena tidak tahu tipe lawan secara pasti, kita menebak menggunakan probabilitas.
   - "Saya yakin 70% dia menggertak, 30% dia punya kartu bagus."

---

## 3. Konsep Main: "Nature" sebagai Wasit

Bagaimana cara memodelkan ketidaktahuan? Kita perkenalkan pemain fiktif bernama **"Nature"** (Alam).

**Alur Permainan:**
1. **Nature** mengocok dadu untuk menentukan "Tipe" dari setiap pemain (atau kondisi dunia).
2. Pemain mengetahui tipenya sendiri, tapi **tidak tahu** tipe lawannya.
3. Pemain hanya mengetahui **distribusi probabilitas** (Prior Belief) dari tipe lawan.
4. Pemain memilih strategi untuk memaksimumkan **Expected Payoff** (rata-rata imbalan).

---

## 4. Formalisme Matematika (Definisi 7.1)

**Definisi 7.1:** Bayesian game $n$-pemain $BG := (\Omega, \Theta, \rho, A, u)$ terdiri dari:
1. **$\Omega$ (States):** Himpunan kondisi dunia.
   > *Bahasa Awam: Apakah cuaca "Hujan" atau "Cerah"? Apakah pasar "Bull" atau "Bear"?*
2. **$\Theta$ (Types):** Tipe privat pemain ($\Theta = \prod \Theta_i$).
   > *Bahasa Awam: Kartu rahasia yang kita pegang (misal: "Saya tipe Pengambil Risiko").*
3. **$\rho$ (Prior):** Distribusi probabilitas bersama $\rho \in \Delta(\Theta \times \Omega)$.
   > *Bahasa Awam: Tebakan awal kita (misal: "70% kemungkinan lawan menggertak").*
   
---
1. **$A$ (Actions):** Profil aksi. Strategi murni adalah peta $\hat{a}_i: \Theta_i \to A_i$.
   > *Bahasa Awam: Rencana lengkap ("Jika saya tipe A, saya akan Lari; jika tipe B, saya Lawan").*
2. **$u$ (Payoff):** Fungsi utilitas $u_i: \Omega \times \Theta_i \times A \to \mathbb{R}$.

---

## 4. Formalisme Matematika (Fungsi Payoff)

Bagaimana cara menghitung untung jika kita tidak yakin?

**Bayesian Payoff Function (Persamaan 7.2):**
$$ \hat{u}_i(\hat{a}) := \sum_{(\theta, \omega) \in \Theta \times \Omega} \rho(\omega|\theta_i)u_i(\omega, \theta_i, \hat{a}(\theta)) $$

> **Penjelasan Sehari-hari:**
> Kita tidak bisa menghitung keuntungan pasti. Rumus ini menghitung **Rata-rata Tertimbang (Expected Value)**.
>
> *"Saya menjumlahkan semua kemungkinan hasil, dikalikan dengan seberapa yakin saya hal itu akan terjadi."*

---

## 4. Formalisme Matematika (Equilibrium)

**Definisi 7.3 (Bayesian Nash Equilibrium):**
Profil strategi $\hat{a}^* \in \hat{A}$ adalah equilibrium jika untuk setiap pemain $i$:
$$ \hat{u}_i(\hat{a}^*) \ge \hat{u}_i(\hat{a}^*_{-i}, \hat{a}_i) \quad (7.4) $$

> **Penjelasan Sehari-hari (Kondisi Anti-Penyesalan):**
> Mengingat apa yang saya tahu (tipe saya) dan tebakan saya tentang Anda, **ini adalah langkah terbaik saya**. Saya tidak akan mengubah strategi ini karena pilihan lain memberikan hasil lebih buruk.

**Teorema 7.5:**
> *Every Bayesian game has at least one Bayesian Nash equilibrium...*
> **Artinya:** Selalu ada "cara main terbaik" (rasional) dalam situasi ketidakpastian, tidak peduli seberapa rumit situasinya.

---

## 4. Dinamika Belief (Evolusi Keyakinan)

Dalam game berulang, kita menggunakan **Bayes' Rule** untuk mengupdate keyakinan berdasarkan sejarah ($h_{t-1}$).

**Logika Update (Chain Store Paradox):**
1. **Prior ($q$):** "Saya rasa 50% dia Monopolis Lemah."
2. **Observasi:** Dia **Melawan (Fight)** penantang sebelumnya.
3. **Posterior ($q_t$):**
   $$ q_{baru} = \frac{P(\text{Dia Melawan} | \text{Dia Kuat}) \cdot q_{lama}}{P(\text{Dia Melawan})} $$
   *"Dia berani melawan? Kemungkinan dia 'Lemah' turun drastis!"*

> **Inti:** Pemain cerdas selalu merevisi strategi mereka berdasarkan data terbaru.

---

## 5. Penurunan Analisis Numerik (Studi Kasus)

Mari kita sederhanakan untuk kasus **Investor vs Pasar**.

**Skenario:**
- **Pemain:** Investor.
- **Lawan (Nature):** Pasar (Bisa **Bullish** atau **Bearish**).
- **Aksi Investor:** Investasi ($I$) atau Tahan Uang ($W$).
- **Belief (Keyakinan):** Investor yakin 60% Pasar Bullish ($q=0.6$), 40% Pasar Bearish ($1-q=0.4$). 

---

## 5. Penurunan Analisis Numerik (Lanj.)

**Matriks Payoff (Imbalan) Investor:**

| Kondisi Pasar | Investasi ($I$) | Tahan Uang ($W$) |
| :--- | :---: | :---: |
| **Bullish** ($\theta_1$) | +100 Juta | 0 |
| **Bearish** ($\theta_2$) | -50 Juta | 0 |


**Tujuan:** Menghitung **Expected Utility (EU)** untuk menentukan aksi terbaik.

---

## 5. Penurunan Analisis Numerik (Perhitungan)

Kita gunakan rata-rata tertimbang (Weighted Average):

**1. Jika Memilih Investasi ($I$):**
$$ EU(I) = (P_{Bull} \times \$_{Bull}) + (P_{Bear} \times \$_{Bear}) $$
$$ EU(I) = (0.6 \times 100) + (0.4 \times -50) $$
$$ EU(I) = 60 - 20 = \mathbf{+40} $$

**2. Jika Memilih Tahan Uang ($W$):**
$$ EU(W) = (0.6 \times 0) + (0.4 \times 0) = \mathbf{0} $$

**Kesimpulan:** Strategi terbaik adalah **Investasi** karena $EU(I) > EU(W)$.

---

## 6. Hubungan dengan Riset Kita (Preview)

Di tingkat lanjut, kita menghadapi masalah dimana menghitung manual terlalu sulit karena variabelnya ribuan.

Oleh karena itu kita menggunakan **Quantum Computing (VQE)** untuk mencari solusi optimalnya secara otomatis.

Rumus Hamiltonian yang kita gunakan nanti:
$$ \hat{H}_{QBG} = q \cdot \hat{H}_{Bull} + (1-q) \cdot \hat{H}_{Bear} $$

Ini persis sama dengan logika:
$$ \text{Total} = (0.6 \times \text{Kondisi Bagus}) + (0.4 \times \text{Kondisi Buruk}) $$

---

<!-- _class: invert -->
