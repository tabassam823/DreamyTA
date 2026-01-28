# Slide Deck: Dari Teori Permainan Klasik ke Quantum Bayesian Games (EWL Scheme)

**Target Audience:** Mahasiswa tingkat akhir yang telah menempuh mata kuliah Game Theory, Group Theory, dan Fisika Kuantum Dasar.
**Tujuan:** Menjelaskan konstruksi model hibrida "Quantum Bayesian Game" untuk optimasi portofolio.

---

## Slide 1: Judul & Konteks
**Judul:** Quantum Bayesian Game Theory: Mengintegrasikan Ketidakpastian Pasar ke dalam Skema EWL
**Sub-judul:** Sebuah Pendekatan Hibrida Menggunakan Variational Quantum Eigensolver (VQE)

**Nareasi Pembuka:**
"Selamat pagi rekan-rekan. Kita semua sudah memahami bagaimana Keseimbangan Nash bekerja dalam sistem klasik, dan kita baru saja mengeksplorasi bagaimana mekanika kuantum memodifikasi probabilitas. Hari ini, kita akan menggabungkan keduanya. Kita akan melihat bagaimana 'ketidakpastian informasi' dalam Game Theory dapat diselesaikan menggunakan 'superposisi' dalam Fisika Kuantum, menggunakan bahasa Teori Grup $SU(2)$."

---

## Slide 2: Agenda & Peta Jalan
1.  **Masalah Klasik:** Keterbatasan Game Theory pada Informasi Tidak Lengkap.
2.  **Solusi Klasik:** Transformasi Harsanyi (Bayesian Game).
3.  **Upgrade Kuantum:** Skema Eisert-Wilkens-Lewenstein (EWL).
4.  **Integrasi Novel:** Membangun *Bayesian Weighted Hamiltonian*.
5.  **Eksekusi:** Algoritma VQE sebagai Solver.

---

## Slide 3: Masalah Dunia Nyata: Investor vs "Nature"
**Poin Utama:**
*   Dalam Game Theory standar, kita berasumsi *Complete Information*.
*   Di pasar saham, Investor (Player A) tidak tahu "kartu" apa yang dipegang Pasar (Player B / "Nature").
*   Apakah pasar sedang *Bullish*? Atau *Bearish*?
*   Ini adalah masalah **Incomplete Information**.

**Koneksi Teori:**
*   *Game Theory*: Kita tidak bisa langsung mencari Nash Equilibrium jika matriks payoff-nya sendiri tidak pasti.

---

## Slide 4: Solusi Klasik: Bayesian Game & Harsanyi
**Poin Utama:**
*   **John Harsanyi** memperkenalkan cara mengubah *Incomplete* menjadi *Imperfect but Complete Information*.
*   Kita menganggap "Nature" bergerak duluan dengan probabilitas tertentu (Prior Belief).
    *   $P(\text{Bull}) = 60%$
    *   $P(\text{Bear}) = 40%$
*   **Matriks Payoff Efektif:** Bukan lagi nilai tunggal, melainkan Ekspektasi Terbobot.
    $$ \mathbb{E}[U] = \sum_{t \in Types} P(t) \cdot U(s, t) $$

**Visualisasi:**
*   Diagram pohon keputusan: Nature bercabang ke Bull/Bear -> Player memilih strategi -> Payoff dihitung rata-rata.

---

## Slide 5: Mengapa Pindah ke Kuantum? (Limitasi Klasik)
**Poin Utama:**
*   Dalam Game Theory Klasik, pemain sering terjebak dalam **Nash Equilibrium yang suboptimal** (Contoh: Prisoner's Dilemma).
*   Kita ingin mencapai **Pareto Optimality**.
*   **Pertanyaan:** Bisakah kita menggunakan properti kuantum (Entanglement & Superposisi) untuk "lolos" dari dilema klasik ini?

**Koneksi Fisika:**
*   Ingat *Bell's Inequality*? Korelasi kuantum bisa lebih kuat daripada korelasi klasik mana pun. Kita akan manfaatkan ini untuk koordinasi strategi tanpa komunikasi.

---

## Slide 6: Skema EWL (Eisert-Wilkens-Lewenstein)
**Poin Utama:**
*   EWL adalah protokol standar untuk "meng-kuantisasi" permainan klasik.
*   Memetakan strategi klasik ke dalam **Ruang Hilbert**.
*   Strategi bukan lagi {0, 1}, tapi rotasi kontinu dalam bola Bloch.

**Struktur Matematika (Group Theory):**
*   Qubit $\in \mathbb{C}^2$.
*   Strategi Pemain $\in SU(2)$ (Special Unitary Group, dimensi 2).
    $$ \hat{U}(\theta, \phi) = \begin{pmatrix} e^{-i\phi}\cos(\theta/2) & -e^{-i\phi}\sin(\theta/2) \\ e^{i\phi}\sin(\theta/2) & e^{i\phi}\cos(\theta/2) \end{pmatrix} $$

---

## Slide 7: Protokol EWL - Langkah 1: Entanglement
**Visualisasi:**
*   Dua qubit dimulai pada state $|00\rangle$.
*   Gerbang $\hat{J}$ diterapkan.

**Analisis Matematis:**
*   Operator Entangling $\hat{J}$ biasanya berkaitan dengan operator Pauli $\sigma_x \otimes \sigma_x$.
*   $$ |\psi_{ent}\rangle = \hat{J} |00\rangle = \frac{1}{\sqrt{2}} (|00\rangle + i|11\rangle) $$
*   **Penting:** Tanpa operator $\hat{J}$, permainan ini hanya permainan klasik yang dimainkan dengan koin mahal. Entanglement adalah kunci *Quantum Advantage*.

---

## Slide 8: Protokol EWL - Langkah 2 & 3: Strategi & Disentangling
**Langkah 2: Strategi Pemain ($\hat{U}_A \otimes \hat{U}_B$)
*   Pemain A (Investor) dan Pemain B (Pasar) merotasi qubit mereka secara lokal.
*   State menjadi: $|\psi_{strat}\rangle = (\hat{U}_A \otimes \hat{U}_B) |\psi_{ent}\rangle$.

**Langkah 3: Disentangling ($\hat{J}^\dagger$)
*   Pintu keluar kuantum. Kita harus membalikkan proses entanglement sebelum pengukuran agar interferensi terjadi dengan benar.
*   $$ |\psi_{fin}\rangle = \hat{J}^\dagger |\psi_{strat}\rangle $$
*   Proses ini memastikan bahwa jika kedua pemain main strategi klasik, hasilnya kembali ke payoff klasik (korespondensi).

---

## Slide 9: Inovasi Kita: Quantum Bayesian Game
**Transisi:**
"EWL standar itu bagus untuk permainan statis. Tapi bagaimana jika kita tidak tahu kita sedang main game yang mana (Bull atau Bear)? Di sinilah kita masukkan konsep Bayesian."

**Konsep:**
*   Kita tidak membuat satu sirkuit untuk Bull dan satu untuk Bear secara terpisah.
*   Kita mendefinisikan sistem kita berada dalam **Superposisi Probabilistik Klasik** dari kedua kondisi tersebut.

---

## Slide 10: Konstruksi Hamiltonian Terbobot (The Core)
**Matematika:**
*   Hamiltonian merepresentasikan "Energi" sistem. Dalam kasus kita, Energi = -Payoff (Kita ingin meminimalkan Energi = Memaksimalkan Payoff).
*   Kita bangun Hamiltonian untuk masing-masing kondisi pasar:
    *   $\\hat{H}_{Bull}$ (berbasis matriks payoff saat pasar naik).
    *   $\\hat{H}_{Bear}$ (berbasis matriks payoff saat pasar turun).
*   **Bayesian Weighted Hamiltonian:**
    $$ \hat{H}_{Total} = p_{Bull} \cdot \hat{H}_{Bull} + p_{Bear} \cdot \hat{H}_{Bear} $$
    *(dimana $p$ adalah probabilitas prior dari analisis sentimen/statistik)*

---

## Slide 11: Arsitektur Solusi: VQE sebagai Solver
**Masalah:** Mencari strategi optimal ($\\theta, \\phi$) yang meminimalkan ekspektasi energi $\\hat{H}_{Total}$.
**Solusi:** Variational Quantum Eigensolver (VQE).

**Mapping ke VQE:**
1.  **Ansatz (Tebakan Sirkuit):** Sirkuit EWL itu sendiri. Parameter $\\theta$ pada gate $\\hat{U}$ adalah variabel yang kita cari.
2.  **Objective Function:** Nilai ekspektasi Hamiltonian.
    $$ \langle E \rangle = \langle \psi(\theta) | \hat{H}_{Total} | \psi(\theta) \rangle $$

---

## Slide 12: Alur Eksekusi (The Hybrid Loop)
**Visualisasi Diagram Alir (Mermaid Graph Fase 3):**

1.  **QPU (Quantum Processor):**
    *   Siapkan state $|00\rangle$.
    *   Jalankan sirkuit EWL dengan parameter $\\theta_i$.
    *   Ukur ekspektasi energi $\\langle H_{Total} \rangle$.
2.  **CPU (Classical Optimizer):**
    *   Terima nilai energi.
    *   Apakah sudah minimum?
    *   Jika belum, gunakan algoritma optimasi (seperti SPSA atau CMA-ES) untuk mengupdate $\\theta_{i+1}$.
    *   Kirim $\\theta_{i+1}$ kembali ke QPU.

---

## Slide 13: Kesimpulan & Takeaways
1.  **Bayesian Game** memberikan kerangka kerja untuk menangani ketidakpastian eksternal ("Nature").
2.  **EWL Scheme** memberikan "ruang bermain" yang lebih luas (Hilbert Space) dibanding strategi klasik, memungkinkan solusi kooperatif/optimal baru.
3.  **VQE** adalah mesin pencari yang efisien untuk menemukan strategi ekuilibrium tersebut secara numerik.

**Closing:**
"Dengan model ini, kita tidak hanya menebak pasar. Kita mencari strategi kuantum yang paling 'robust' terhadap segala kemungkinan kondisi pasar."

---
**Diskusi & Tanya Jawab
