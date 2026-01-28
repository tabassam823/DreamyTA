---
marp: true
theme: default
paginate: true
backgroundColor: #fbfbfb
header: 'Quantum Bayesian Game Theory'
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
# Quantum Bayesian Game Theory (QBGT)
## Penyatuan Dua Dunia

**Solusi Akhir**
*Menghadapi Ketidakpastian dengan Strategi Kuantum*

---

## 1. Latar Belakang
### Mengapa Harus Digabung?

Kita sudah belajar dua hal:
1.  **Bayesian Game:** Bagus untuk memodelkan **ketidakpastian** (Contoh: Pasar mungkin Bull/Bear), tapi solusinya seringkali konservatif atau sub-optimal secara klasik.
2.  **Quantum (EWL) Game:** Bagus untuk **memperluas strategi** dan menciptakan korelasi (entanglement) antar aset, tapi biasanya diasumsikan aturannya fix.

> **QBGT (Quantum Bayesian Game Theory)** menggabungkan keduanya:
> Kita bermain di **Sirkuit Kuantum** (EWL), tetapi **Papan Skor-nya (Payoff)** berubah-ubah tergantung kocokan dadu "Nature" (Bayesian).

---

## 2. Aturan & Konsep Dasar

Dalam QBGT, permainan menjadi lebih dinamis:

1.  **Nature (Alam):** Memilih kondisi permainan ($	heta$).
    - Kondisi 1: Pasar Naik (Bullish)
    - Kondisi 2: Pasar Turun (Bearish)
2.  **Pemain (Investor):** Tidak tahu kondisi mana yang terpilih.
3.  **Strategi:** Pemain harus menyiapkan **Satu Sirkuit Kuantum ($→	heta$)** yang sama.
4.  **Tujuan:** Sirkuit tersebut harus memberikan hasil kemenangan rata-rata (Expected Utility) tertinggi, tidak peduli kondisi mana yang sebenarnya terjadi.

---

## 3. Konsep Main: "Satu Kunci untuk Semua Pintu"

Bayangkan Anda harus membuat satu kunci duplikat.
- Pintu A butuh kunci gerigi atas.
- Pintu B butuh kunci gerigi bawah.
- Anda tidak tahu pintu mana yang akan Anda temui.

**Solusi Klasik:** Buat kunci rata-rata (biasanya gagal di kedua pintu).
**Solusi Kuantum:** Buat "Kunci Superposisi" yang keadaan spin-nya bisa beradaptasi atau meminimalkan energi kesalahan di kedua skenario sekaligus melalui interferensi.

---

## 4. Formalisme Matematika

Inti dari QBGT adalah **Penggabungan Operator Hamiltonian**.

Alih-alih menghitung skor secara terpisah, kita membuat satu **Operator Raksasa** yang mewakili rata-rata alam semesta.

$$ \hat{H}_{QBG} = \sum_{\theta ∈ Θ} P(\theta) · \hat{H}_{\theta} $$

Untuk kasus kita (Bull vs Bear):
$$ \hat{H}_{QBG} = q · \hat{H}_{Bull} + (1-q) · \hat{H}_{Bear} $$

Dimana:
- $\hat{H}_{Bull}$: Operator energi yang "senang" kalau kita beli saham saat Bull.
- $\hat{H}_{Bear}$: Operator energi yang "marah" (penalti) kalau kita beli saham saat Bear.

---

## 5. Penurunan Analisis Numerik (Studi Kasus)

Mari kita lihat bagaimana operator ini terbentuk secara numerik.

**Misalkan kita punya 1 Aset (Qubit tunggal):**
- $\hat{Z}$ adalah operator Pauli Z (Nilai eigen +1 atau -1).
- Saat diukur, $\hat{Z} ⁺0⁻ = ⁺0⁻$ (Spin Up/Tidak Beli) dan $\hat{Z} ⁺1⁻ = -⁺1⁻$ (Spin Down/Beli).

**Skenario Bull ($q=0.6$):** Untung besar jika beli.
Operator Energi: $\hat{H}_{Bull} = -10 · \hat{Z}$ (Minus artinya energi rendah/bagus).

**Skenario Bear ($1-q=0.4$):** Rugi besar jika beli.
Operator Energi: $\hat{H}_{Bear} = +20 · \hat{Z}$ (Plus artinya energi tinggi/buruk).

---

## 5. Penurunan Analisis Numerik (Lanj.)

Kita gabungkan kedua realitas tersebut menjadi satu operator tunggal.

$$ \hat{H}_{QBG} = (0.6 · \hat{H}_{Bull}) + (0.4 · \hat{H}_{Bear}) $$
$$ \hat{H}_{QBG} = (0.6 · -10 · \hat{Z}) + (0.4 · 20 · \hat{Z}) $$
$$ \hat{H}_{QBG} = (-6 · \hat{Z}) + (8 · \hat{Z}) $$
$$ \hat{H}_{QBG} = +2 · \hat{Z} $$

**Interpretasi:**
Hasil akhirnya adalah $+2 · \hat{Z}$.
Karena koefisiennya positif (+2), maka untuk meminimalkan energi, sistem akan cenderung ke state $⁺0⁻$ (Tidak Beli).

---
**Artinya:**
Meskipun peluang Bull lebih besar (60%), risiko kerugian di Bear (20) sangat besar sehingga secara rata-rata (Bayesian), keputusan kuantum yang paling "aman" adalah tidak membeli.

---

## 6. Hubungan dengan Riset Kita (VQE)

Dalam riset "Optimasi Portofolio", kita tidak menghitung ini secara manual untuk 1 aset.

Kita punya:
1.  **Puluhan Aset ($N$):** Membentuk matriks $2^N 	imes 2^N$.
2.  **Korelasi Antar Aset:** Suku $\hat{Z}_i · \hat{Z}_j$ yang menangkap hubungan saham A dan B.

Kita menggunakan algoritma **VQE (Variational Quantum Eigensolver)** untuk mencari Ground State (keadaan energi terendah) dari operator $\hat{H}_{QBG}$ tersebut.

Hasil ground state itulah yang menjadi **Portofolio Optimal** kita.

---

<!-- _class: invert -->
# Terima Kasih
## Inilah Akhir dari Teori Dasar
### Selanjutnya: Implementasi Kodingan (Notebook)
