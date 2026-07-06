# Rencana Presentasi: Strategi Investasi Kompetitif dan Portofolio Log-Optimal

**Target Audiens:** Mahasiswa Matematika Tingkat Akhir  
**Format:** LaTeX Beamer  
**Sumber Referensi:** `hasil_gemini_adv_formal.md`

---

## Struktur Slide dan Konten

### Slide 1: Judul Presentasi
- **Judul Utama:** Strategi Investasi Kompetitif: Pendekatan Game Theory dan Portofolio Log-Optimal
- **Subjudul:** Analisis Matematis Berdasarkan Permainan $\phi$ (*The $\phi$-Game*)

### Slide 2: Pendahuluan - Model Pasar Saham
- **Definisi Pasar:** Vektor $X = (X_1, \dots, X_m)$ di mana $X_i \ge 0$ adalah *return* (nilai kembalian) per unit modal.
- **Definisi Portofolio:** Vektor $b = (b_1, \dots, b_m)$ dengan kendala:
  - $b_i \ge 0$ (tanpa *short selling*).
  - $\sum b_i = 1$ (modal penuh).
- **Modal Akhir ($S$):** Variabel acak $S = b^t X$.
- **Konteks:** $X$ ditarik dari distribusi bersama $F(x)$ yang diketahui.

### Slide 3: Kerangka Game Theory (*Zero-Sum*)
- **Pemain:** Dua investor (Pemain 1 vs Pemain 2).
- **Tujuan:** Memaksimalkan ekspektasi fungsi imbal hasil $E\phi(S_1/S_2)$.
  - Menang ditentukan oleh rasio kekayaan $S_1/S_2$.
  - $\phi(t)$ adalah fungsi monoton naik (*non-decreasing*).
- **Hipotesis:** Keberadaan strategi universal **Portofolio Log-Optimal ($b^*$)** yang *robust*.

### Slide 4: Formalisasi Strategi Permainan
- **Ruang Strategi Dua Tahap:**
  1. **Randomisasi Awal ($W$):** Memilih variabel acak adil (*Fair Random Variable*) dengan $W \ge 0$ dan $E[W] \le 1$.
  2. **Alokasi Aset ($b$):** Memilih portofolio saham.
- **Persamaan Payoff (1.1):**
  $$E \phi\left(\frac{W_{1}b_{1}^{\prime}X}{W_{2}b_{2}^{\prime}X}\right)$$
- **Masalah Minimax:** Mencari titik pelana ($v$) keseimbangan strategi.

### Slide 5: Permainan Primitif ($\phi$-Game) - Bagian 1
- **Definisi:** Permainan murni pemilihan distribusi probabilitas tanpa pasar saham.
- **Masalah:** Memilih $W_1, W_2$ untuk memaksimumkan $E\phi(W_1/W_2)$.
- **Pertanyaan Kunci:** Kapan strategi optimal adalah strategi murni ($W=1$, tanpa judi)?

### Slide 6: Permainan Primitif - Teorema 1
- **Syarat Strategi Murni:** Optimal pada $W_1^* = W_2^* = 1$ jika dan hanya jika fungsi $\phi$ bersifat konkaf (cekung) di sekitar 1.
- **Ketidaksamaan Diferensial:**
  $$(\frac{t-1}{t})\phi'(1) \le \phi(t)-\phi(1) \le (t-1)\phi'(1)$$
- **Interpretasi:** Untuk fungsi utilitas yang menghindari risiko (seperti logaritma atau pangkat $0 \le \alpha \le 1$), "diam" lebih baik daripada taruhan adil.

### Slide 7: Keluarga Konveks (*Convex Families*)
- **Definisi:** Himpunan variabel acak $\mathcal{S}$ di mana campuran linear $\lambda S_1 + (1-\lambda)S_2$ tetap berada dalam himpunan.
- **Contoh:** Portofolio standar, portofolio dengan kendala linear, dan strategi sekuensial.
- **Relevansi:** Memungkinkan penggunaan teorema titik tetap dan minimax.

### Slide 8: Teorema 2 - Ekuivalensi Fundamental
- **Pernyataan:** Untuk keluarga konveks, sifat **Log-Optimal** ekuivalen dengan **Dominasi Linear**.
  $$E \ln(S/S^*) \le 0 \iff E(S/S^*) \le 1$$
- **Bukti (Sketsa):**
  - Linear $\to$ Log: Ketidaksamaan Jensen.
  - Log $\to$ Linear: Metode variasi (perturbasi) dan kontradiksi.
- **Implikasi:** Masalah optimasi logaritma dapat diselesaikan/diverifikasi lewat pertidaksamaan linear.

### Slide 9: Teorema 3 - Pemisahan Variabel (*Separation Theorem*)
- **Konteks:** Permainan Pasar Saham Penuh.
- **Teorema:** Strategi optimal terfaktor menjadi dua komponen independen:
  1. **Komponen Judi ($W^*$):** Solusi dari permainan primitif (bergantung pada $\phi$).
  2. **Komponen Investasi ($b^*$):** Selalu Portofolio Log-Optimal (Universal, tidak bergantung $\phi$).
- **Mekanisme Bukti:** Substitusi variabel $Z = (W_2 S_2)/S^*$ mereduksi masalah kembali ke permainan primitif.

### Slide 10: Permainan Multi-tahap (*Multistage*)
- **Model:** Investasi berulang selama $n$ periode dengan *compounding* dan *rebalancing*.
- **Teorema 4 (Strategi Myopic):**
  - Strategi terbaik adalah memaksimalkan $E[\ln S]$ pada tiap langkah secara independen (*greedy*).
  - Tidak perlu mengorbankan keuntungan hari ini demi masa depan.
- **Dasar:** Sifat aditif fungsi logaritma: $\ln(\prod X_i) = \sum \ln X_i$.

### Slide 11: Randomisasi Posterior (Observasi Modal) - Bagian 1
- **Skenario:** Pemain dapat mengamati rasio modal $S_1/S_2$ di tengah permainan.
- **Isu Psikologis:** Apakah pemain yang tertinggal harus mengubah strategi menjadi lebih agresif (*Jockeying for position*)?
- **Intuisi Judi Biasa:** Pada judi murni, yang kalah memang harus mengambil risiko ekstrem ("All-in").

### Slide 12: Randomisasi Posterior - Teorema 5
- **Hasil Kontraintuitif di Pasar Saham:**
  - Strategi optimal tetaplah **Log-Optimal ($b^*$)** dengan randomisasi awal standar ($W^*$).
  - Strategi "Buta" (*Unconditional*) sudah cukup untuk mencapai minimax.
- **Alasan Matematis:**
  - $S^*$ memiliki sifat dominasi linear ($E[S_{lawan}/S^*] \le 1$).
  - Segala penyimpangan lawan dari $S^*$ secara statistik merugikan mereka sendiri, sehingga kita tidak perlu bermanuver.

### Slide 13: Kesimpulan
- **Penyatuan Teori:** Portofolio Log-Optimal adalah solusi universal untuk berbagai tujuan investasi ($\phi$) dalam kerangka kompetitif.
- **Sifat:** Memiliki properti *Fair Reach* dan stabilitas jangka panjang.
- **Implikasi Praktis:** Investor dapat fokus memaksimalkan pertumbuhan logaritmik portofolio sendiri tanpa perlu bereaksi berlebihan terhadap pergerakan modal pesaing.
