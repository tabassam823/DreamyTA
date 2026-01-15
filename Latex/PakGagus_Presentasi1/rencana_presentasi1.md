# Rencana Presentasi: Optimisasi Portofolio Menggunakan Algoritma Quantum VQE
**Target Audiens:** Mahasiswa S1 Semester Akhir (Fisika/Komputasi/Keuangan)
**Format:** LaTeX Beamer

---

## Bagian 1: Pendahuluan (Introduction)

### Slide 1: Judul
- **Judul:** Optimisasi Portofolio Berkualitas Tinggi dengan Variational Quantum Eigensolver (VQE)
- **Sub-judul:** Pendekatan Hibrida Menggunakan Weighted CVaR dan CMA-ES
- **Presenter:** [Nama Anda]
- **Institusi:** [Nama Institusi]
- **Gambar:** Ilustrasi artistik yang menggabungkan grafik saham dengan simbol sirkuit kuantum atau bola Bloch.

### Slide 2: Latar Belakang Masalah (Introduction 1.1)
- **Poin Utama:**
    - **Optimisasi Portofolio:** Masalah fundamental keuangan (alokasi modal untuk maksimalkan untung, minimalkan risiko).
    - **Formulasi QUBO:** Masalah diterjemahkan ke model *Quadratic Unconstrained Binary Optimization*.
    - **Tantangan:** Masalah ini termasuk kategori *NP-hard*. Komputer klasik kesulitan seiring bertambahnya jumlah aset.
    - **Solusi Kuantum:** Menawarkan potensi efisiensi komputasi untuk menyelesaikan masalah kompleks ini.
- **Saran Gambar:** Diagram alur sederhana: `Data Saham -> Rumus Matematika (QUBO) -> Tembok Penghalang (NP-hard) -> Solusi (Komputer Kuantum)`.

### Slide 3: Perangkat Komputasi Era NISQ (Introduction 1.2)
- **Poin Utama:**
    - **Algoritma Kandidat:** VQE (*Variational Quantum Eigensolver*) dan QAOA.
    - **Sifat Algoritma:** Hibrida (Kerjasama CPU Klasik dan QPU Kuantum).
        - QPU: Hitung energi sistem yang rumit.
        - CPU: Optimasi parameter.
    - **Era NISQ:** Perangkat kuantum saat ini masih "bising" (*noisy*) dan terbatas, namun VQE dinilai cukup tangguh (*robust*) untuk era ini.

### Slide 4: Tantangan Teknis VQE pada Keuangan (Introduction 1.3)
- **Poin Utama:**
    - **Kimia vs. Keuangan:** VQE awalnya untuk kimia (molekul kompleks). Masalah keuangan lebih sederhana (Hamiltonian komutatif).
    - **Ground State:** Solusi keuangan berupa *Computational Basis State* (deretan biner 0 dan 1, misal: Beli/Tidak).
    - **Masalah Nilai Ekspektasi:** Menggunakan rata-rata energi biasa kurang efektif karena bisa mengaburkan solusi optimal yang spesifik.

### Slide 5: Solusi yang Diusulkan (Introduction 1.4)
- **Poin Utama:**
    - **Fungsi Biaya Baru:** Mengganti rata-rata standar dengan **CVaR** (*Conditional Value-at-Risk*) -> Fokus pada ekor distribusi energi terendah.
    - **Inovasi:** Mengembangkan **Weighted CVaR (WCVaR)** (Memberi bobot prioritas pada solusi terbaik).
    - **Pengoptimasi:** Menggunakan **CMA-ES** (*Covariance Matrix Adaptation Evolution Strategy*) yang bebas turunan (*derivative-free*) untuk menangani lanskap energi yang kasar.

---

## Bagian 2: Landasan Teori (Background)

### Slide 6: Prapemrosesan Data Saham (Background 2.1)
- **Poin Utama:**
    - **Input:** Matriks harga aset ($P$) sepanjang waktu ($M$).
    - **Transformasi:** 
        1.  Hitung *Return* harian ($r_{ki}$). 
        2.  Hitung Ekspektasi Return ($\mu_i$) $\rightarrow$ Keuntungan.
        3.  Hitung Matriks Kovariansi ($\sigma_{ij}$) $\rightarrow$ Risiko.
- **Saran Gambar:** Tabel ilustrasi perubahan dari "Harga Rupiah" menjadi "Persentase Return" lalu menjadi vektor Mean dan matriks Kovariansi.

### Slide 7: Model Matematika Portofolio (Background 2.2 & 2.3)
- **Poin Utama:**
    - **Tujuan 1:** Maksimalkan Keuntungan ($C_1$).
    - **Tujuan 2:** Minimalkan Risiko ($C_2$).
    - **Kendala:** Total investasi tidak boleh melebihi Modal ($B$).
    - **Fungsi Gabungan:** $C' = -\lambda C_1 + (1-\lambda)C_2$.
        - $\lambda$: Faktor pengatur selera risiko investor (0 sampai 1).
- **Saran Gambar:** Grafik *Efficient Frontier* (Kurva Pareto) yang menunjukkan *trade-off* antara Risiko (sumbu X) dan Keuntungan (sumbu Y).

### Slide 8: Formulasi QUBO & Penalti (Background 2.4 & 2.5)
- **Poin Utama:**
    - **Variabel Biner:** $x_i \in \{0, 1\}$ (0 = Jangan Beli, 1 = Beli).
    - **Constraint:** Harus memilih tepat $N/2$ aset.
    - **Metode Penalti:** Menambahkan suku kuadratik $( \sum x_i - N/2 )^2$ ke fungsi tujuan.
        - Jika melanggar aturan jumlah aset, energi (biaya) melonjak tinggi.
    - **Analogi Fisika:** Mirip energi potensial pegas ($U \sim kx^2$). Memaksa sistem ke posisi setimbang.
- **Saran Gambar:** Grafik parabola ("sumur energi") yang menggambarkan bagaimana solusi di luar target $N/2$ memiliki energi yang sangat tinggi.

### Slide 9: Implementasi VQE (Background 2.6 & 2.7)
- **Poin Utama:**
    - **Mapping ke Fisika:** Variabel biner ($x_i$) diubah ke variabel Spin ($s_i$) lalu ke Operator Pauli-Z ($\hat{Z}_i$).
    - **Hamiltonian:** $\hat{H} = -\sum h_i \hat{Z}_i - \sum J_{ij} \hat{Z}_i \hat{Z}_j$.
        - $h_i$: Mewakili Return saham.
        - $J_{ij}$: Mewakili Risiko/Kovariansi antar saham.
    - **Minimisasi Energi:** Mencari energi terendah ($\min \langle H \rangle$) sama dengan mencari profit maksimal.

### Slide 10: Conditional Value-at-Risk (CVaR) (Background 2.8)
- **Poin Utama:**
    - **Kelemahan Rata-rata:** Rata-rata energi sering menyesatkan jika solusi optimal jarang muncul.
    - **Konsep CVaR:** Hanya menghitung rata-rata dari $\alpha\%$ sampel terbaik (energi terendah).
    - **Parameter $\alpha$:** Mengatur keseimbangan antara eksplorasi dan stabilitas.

---

## Bagian 3: Desain Algoritma (Design)

### Slide 11: Inovasi Weighted CVaR (WCVaR) (Design 3.1)
- **Poin Utama:**
    - **Masalah CVaR Biasa:** Memberi bobot sama rata pada semua sampel terbaik (Top $\alpha$).
    - **Solusi WCVaR:** Memberi bobot berbeda ($w_k$) berdasarkan peringkat.
    - **Mekanisme:** Solusi ranking 1 diberi bobot jauh lebih besar daripada ranking 10.
    - **Tujuan:** Memberi sinyal lebih kuat ke optimizer untuk mengejar solusi elite.
- **Saran Gambar:** Grafik perbandingan bobot: Garis datar (CVaR biasa) vs Kurva meluruh eksponensial (WCVaR).

### Slide 12: Optimizer CMA-ES (Design 3.2)
- **Poin Utama:**
    - **Tantangan:** Fungsi biaya WCVaR menghasilkan lanskap yang kasar (*non-smooth*) dan berisik.
    - **Mengapa CMA-ES?**
        - Algoritma Evolusioner (berbasis populasi).
        - Tidak butuh turunan (*derivative-free*).
        - Tangguh terhadap *local minima*.
    - **Perbandingan:** Diadu melawan COBYLA (standar industri).

### Slide 13: Desain Sirkuit Kuantum (Ansatz) (Design 3.3 & 3.4)
- **Poin Utama:**
    - **Ansatz:** Bentuk rangkaian gerbang kuantum untuk fungsi gelombang coba-coba.
    - **Desain 1: Two-Local:** Standar. Lapisan rotasi ($R_y, R_z$) + Entanglement ($CNOT$).
    - **Desain 2: Block Ansatz:** Menggunakan modul blok fungsional untuk korelasi yang lebih dalam.
- **Saran Gambar:** Dua diagram sirkuit berdampingan. Kiri: Two-local (lapis demi lapis). Kanan: Block Ansatz (modul kotak besar).

---

## Bagian 4: Hasil Numerik (Results)

### Slide 14: Setup Eksperimen (Results 4.1)
- **Poin Utama:**
    - **Data:** 12 Aset (6 Saham China, 6 Saham AS) tahun 2024.
    - **Alasan 12 Aset:** Cukup kompleks untuk bukti konsep, bisa diverifikasi *brute force*.
    - **Metode Penilaian:** *Top-10 Hit Rate*.
        - Sukses jika solusi benar (Ground State) masuk dalam 10 tebakan teratas algoritma.

### Slide 15: Hasil Performa (Results 4.2)
- **Poin Utama:**
    - **WCVaR vs CVaR:** WCVaR jauh lebih stabil dan unggul di berbagai nilai $\alpha$. CVaR standar sangat sensitif (hanya bagus di $\alpha$ kecil).
    - **CMA-ES vs COBYLA:** CMA-ES konvergen lebih cepat dan mencapai sukses rate lebih tinggi.
    - **Ansatz:** Tidak ada perbedaan signifikan antara *Two-Local* dan *Block Ansatz*.
- **Saran Gambar:** Grafik garis performa (sumbu X: Iterasi, sumbu Y: Probability Success). Tunjukkan garis CMA-ES+WCVaR berada paling atas.

### Slide 16: Evaluasi Pembobotan (Appendix & Results)
- **Poin Utama:**
    - Menguji 4 varian bobot.
    - **Terburuk:** Berbasis Energi (tidak stabil).
    - **Terbaik:** *Piecewise Exponential* (W4) dan *Rank-based* (W3).
    - **Rekomendasi:** *Rank-based* (W3) karena sederhana namun sangat efektif.

---

## Bagian 5: Kesimpulan

### Slide 17: Kesimpulan Akhir
- **Poin Utama:**
    - Sinergi **WCVaR** (fungsi biaya) dan **CMA-ES** (optimizer) adalah kunci keberhasilan.
    - Pendekatan ini mengatasi masalah jebakan minima lokal dan lanskap energi kasar.
    - Metode ini menjanjikan untuk optimisasi portofolio di era komputer kuantum NISQ.

### Slide 18: Penutup
- **Terima Kasih**
- **Sesi Tanya Jawab (Q&A)**
