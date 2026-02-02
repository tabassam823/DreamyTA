# Rencana Presentasi: Hardware-Efficient Variational Quantum Eigensolver
**Tujuan:** Menjelaskan simulasi struktur elektronik pada komputer kuantum superkonduktor menggunakan pendekatan yang efisien secara perangkat keras.

---

## Bagian 1: Pendahuluan & Motivasi

### Slide 1: Judul & Identitas
*   **Visual:** Judul Paper ("Hardware-efficient Variational Quantum Eigensolver for Small Molecules and Quantum Magnets"), Nama Penulis (Tim IBM Quantum), dan Gambar Chip Kuantum (Figur 1B).
*   **Narasi/Poin Bicara:**
    1.  Selamat pagi/siang. Hari ini kita akan membahas terobosan penting dalam simulasi kimia kuantum pada perangkat NISQ (*Noisy Intermediate-Scale Quantum*).
    2.  Fokus utama kita adalah bagaimana menyelesaikan masalah struktur elektronik molekul yang kompleks (hingga BeH2) menggunakan hardware yang memiliki keterbatasan (noise dan koherensi pendek).
    3.  Kunci keberhasilannya adalah strategi "Hardware-Efficient Ansatz".

### Slide 2: Masalah Utama - Struktur Elektronik
*   **Visual:** Ilustrasi molekul sederhana, elektron yang mengelilingi inti, dan persamaan Schrödinger ($H \ket{Ψ} = E \ket{Ψ}$).
*   **Narasi/Poin Bicara:**
    1.  **Apa masalahnya?** Kita ingin mencari energi keadaan dasar (*ground state energy*) dari sebuah molekul. Sifat kimia material bergantung pada bagaimana elektron-elektron (fermion) berinteraksi.
    2.  **Tantangan Klasik:** Simulasi fermion pada komputer klasik berskala secara **eksponensial**. Menambah satu elektron menambah beban komputasi berkali-kali lipat.
    3.  **Tembok Penghalang:** Metode statistik klasik (Monte Carlo) gagal karena *Fermionic Sign Problem*.

### Slide 3: Mengapa Komputer Kuantum? & Tantangannya
*   **Visual:** Grafik perbandingan kompleksitas Klasik vs Kuantum, dan diagram skematik *Quantum Phase Estimation* (QPE) dengan tanda silang merah atau peringatan.
*   **Narasi/Poin Bicara:**
    1.  Komputer kuantum secara alami cocok untuk mensimulasikan sistem kuantum (seperti kata Feynman).
    2.  **Pendekatan Buku Teks (QPE):** Secara teori, *Quantum Phase Estimation* (QPE) bisa memberikan hasil eksak.
    3.  **Realita:** QPE membutuhkan sirkuit yang sangat panjang. Hardware saat ini memiliki waktu koherensi pendek (qubit cepat error). Sebelum QPE selesai, informasi sudah hilang.
    4.  **Solusi:** Kita butuh algoritma yang "tahan banting" dan sirkuit yang pendek.

---

## Bagian 2: Metodologi (Solusi)

### Slide 4: Solusi Hibrida - VQE (Variational Quantum Eigensolver)
*   **Visual:** Diagram lingkaran (Loop) antara CPU Klasik dan QPU (Quantum Processing Unit).
*   **Narasi/Poin Bicara:**
    1.  Paper ini menggunakan **VQE**. Ini adalah algoritma hibrida.
    2.  **Pembagian Tugas:**
        *   **Kuantum:** Menyiapkan keadaan gelombang (*trial state*) yang rumit dan mengukur energinya.
        *   **Klasik:** Menerima data energi, lalu menghitung parameter baru untuk menurunkan energi tersebut.
    3.  **Prinsip Variasional:** Energi rata-rata dari tebakan kita akan selalu $≥$ Energi Ground State asli. Jadi, kita cukup memutar parameter sampai energinya paling rendah (minimum).

### Slide 5: Masalah pada Ansatz Standar (UCC)
*   **Visual:** Rumus kompleks *Unitary Coupled Cluster* (UCC) dan ilustrasi sirkuit yang sangat dalam/panjang.
*   **Narasi/Poin Bicara:**
    1.  Bagaimana cara kita menebak fungsi gelombang awal? Standar kimia adalah UCC (*Unitary Coupled Cluster*).
    2.  **Masalah UCC:** Sangat akurat tapi sangat mahal. Jumlah gerbang (gates) meledak secara polinomial.
    3.  **Isu Teknis:** Membutuhkan "Trotterisasi" (pemotongan langkah waktu) yang membuat sirkuit jadi sangat dalam $
ightarrow$ kena noise $
ightarrow$ hasil hancur.
    4.  Oleh karena itu, penulis **tidak** menggunakan UCC.

### Slide 6: Inovasi Utama - Hardware-Efficient Ansatz
*   **Visual:** Diagram sirkuit dari Paper (Panel C) yang menunjukkan pola berulang: Rotasi - Entangler - Rotasi.
*   **Narasi/Poin Bicara:**
    1.  **Ide Inti:** Jangan memaksakan rumus kimia ke hardware. Sebaliknya, buatlah tebakan (*ansatz*) yang disesuaikan dengan kemampuan hardware.
    2.  **Desain Sirkuit:** Gunakan gerbang yang tersedia secara "alami" di perangkat IBM:
        *   Rotasi Euler Single-Qubit (untuk kontrol).
        *   Entangler Drift Hamiltonian (interaksi alami antar qubit).
    3.  **Keuntungan:** Sirkuit menjadi pendek (*shallow depth*), meminimalkan akumulasi error sebelum pengukuran.

---

## Bagian 3: Implementasi Eksperimental

### Slide 7: Peta Jalan Eksperimen (Figur 1)
*   **Visual:** Figur 1 penuh dari paper (Panel A, B, C, D).
*   **Narasi/Poin Bicara:**
    1.  Mari lihat alur lengkapnya:
    2.  **Panel A (Kimia):** Kita mulai dari orbital elektron. Menggunakan *Parity Mapping* dan simetri untuk memadatkan masalah (misal: 8 orbital $\rightarrow$ 6 qubit).
    3.  **Panel B (Chip):** Dijalankan pada prosesor 6-qubit transmon yang terhubung lewat *waveguide resonators*.
    4.  **Panel C (Sirkuit):** Struktur berlapis (Depth $d$). Lapisan rotasi ($\theta$) diselingi lapisan entangler ($U_{ENT}$).
    5.  **Panel D (Fisik):** Diterjemahkan menjadi pulsa mikrogelombang (Cross-Resonance).

### Slide 8: Strategi Optimasi (SPSA)
*   **Visual:** Grafik konvergensi energi yang "bergerigi" lalu melandai (ilustrasi SPSA), dan rumus update parameter.
*   **Narasi/Poin Bicara:**
    1.  Tantangan pengukuran: Hasil kuantum itu probabilistik (ada noise/fluktuasi).
    2.  Jika menggunakan metode gradien biasa, kita butuh terlalu banyak pengukuran.
    3.  **Solusi: SPSA (Simultaneous Perturbation Stochastic Approximation).**
    4.  Hebatnya SPSA: Bisa mengestimasi arah perbaikan (gradien) hanya dengan **2 pengukuran**, tidak peduli apakah parameternya ada 10 atau 100. Ini sangat menghemat waktu.

---

## Bagian 4: Hasil & Diskusi

### Slide 9: Hasil Puncak - Molekul BeH2 (Figur 2)
*   **Visual:** Grafik Energi vs Iterasi untuk BeH2 (Figur 2 dari paper).
*   **Narasi/Poin Bicara:**
    1.  Ini adalah pembuktian konsep untuk molekul terbesar saat itu: **Berilium Dihidrida (BeH2)**.
    2.  Menggunakan **6 Qubit**. (Menggunakan aproksimasi *frozen core* untuk membuang elektron dalam).
    3.  Lihat grafiknya: Titik-titik energi turun seiring iterasi SPSA berjalan.
    4.  **Hasil:** Garis hijau (hasil akhir eksperimen) berhimpitan dengan garis hitam (teori). Akurasi kimia tercapai ($d=1$, 30 parameter).

### Slide 10: Kurva Energi Potensial (Figur 3)
*   **Visual:** Tiga grafik berdampingan: H2 (2 qubit), LiH (4 qubit), BeH2 (6 qubit).
*   **Narasi/Poin Bicara:**
    1.  Eksperimen diulang untuk berbagai jarak antar-atom (sumbu X) untuk melihat profil energi ikat.
    2.  **H2 & BeH2:** Hasil sangat akurat mengikuti garis teori.
    3.  **Kasus LiH (Tengah):** Ada penyimpangan di jarak 2.5 Angstrom.
    4.  **Mengapa menyimpang?** Bukan karena noise alat, tapi karena sirkuit $d=1$ terlalu sederhana (*underfitting*) untuk menangkap kompleksitas LiH di jarak tersebut. Jika kedalaman ($d$) ditambah, noise akan merusak hasil. Ini adalah *trade-off* klasik di era NISQ.

### Slide 11: Validasi Noise
*   **Visual:** Zoom-in pada salah satu grafik hasil yang menunjukkan area berwarna (shaded region).
*   **Narasi/Poin Bicara:**
    1.  Perhatikan area berwarna di grafik. Itu adalah hasil simulasi komputer klasik yang *sengaja* diberi noise.
    2.  Data eksperimen (titik-titik) jatuh tepat di dalam area prediksi tersebut.
    3.  **Artinya:** Penulis sangat memahami karakter error pada mesin mereka. Tidak ada "sihir", semua terukur secara fisika.

### Slide 12: Bonus - Magnetisme Kuantum (Figur 4)
*   **Visual:** Grafik Model Heisenberg Antiferomagnetik.
*   **Narasi/Poin Bicara:**
    1.  Metode ini tidak hanya untuk kimia. Mereka juga menguji model magnetisme (interaksi spin).
    2.  **Temuan Menarik:**
        *   Saat medan magnet luar kuat: Sirkuit tanpa entangler ($d=0$) justru menang.
        *   Saat interaksi antar-spin kuat ($J$ besar): Wajib pakai entangler ($d=2$).
    3.  Kesimpulan: Kompleksitas sirkuit harus disesuaikan dengan fisika masalahnya.

---

## Bagian 5: Kesimpulan

### Slide 13: Kesimpulan & Masa Depan
*   **Visual:** Poin-poin ringkasan dan ilustrasi visi masa depan (skalabilitas).
*   **Narasi/Poin Bicara:**
    1.  **Pencapaian:** Berhasil mensimulasikan molekul hingga BeH2 (6 qubit) tanpa memerlukan koherensi yang sempurna atau koreksi error (error correction).
    2.  **Kunci Sukses:** Kombinasi VQE + Hardware-Efficient Ansatz + Optimasi SPSA.
    3.  **Tantangan ke Depan:** Untuk molekul yang jauh lebih besar, kita tetap membutuhkan:
        *   Konektivitas qubit yang lebih baik.
        *   Waktu koherensi yang lebih panjang (agar bisa pakai $d$ yang lebih dalam).
    4.  Paper ini membuka jalan bahwa komputer kuantum jangka pendek (NISQ) bisa berguna untuk masalah sains nyata.

### Slide 14: Sesi Tanya Jawab
*   **Visual:** Teks "Terima Kasih" dan "Q&A".