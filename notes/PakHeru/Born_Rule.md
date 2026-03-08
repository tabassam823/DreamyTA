# Aturan Born: Jembatan Amplitudo ke Probabilitas

Aturan Born (*Born Rule*) adalah postulat dalam mekanika kuantum yang menghubungkan deskripsi matematis abstrak dari sebuah sistem (state vector) dengan hasil pengamatan eksperimental yang nyata. Tanpa aturan ini, kita tidak memiliki cara untuk menginterpretasikan apa arti fisik dari sebuah qubit.

---

## 1. Postulat Dasar: State dalam Ruang Hilbert
Sesuai dengan aksioma mekanika kuantum, sebuah sistem fisik didefinisikan secara lengkap oleh sebuah **vektor keadaan** $|\psi\rangle$ dalam ruang Hilbert kompleks $\mathcal{H}$.

**Konvensi Normalisasi:**
Agar interpretasi probabilitas bersifat konsisten, vektor $|\psi\rangle$ harus ternormalisasi:
$$ \langle \psi | \psi \rangle = 1 $$

**Filosofi:**
Vektor $|\psi\rangle$ itu sendiri bukanlah entitas yang dapat diamati secara langsung. Ia adalah "gudang potensi" yang menyimpan informasi tentang semua kemungkinan hasil pengukuran. Perubahan $|\psi\rangle$ bersifat deterministik (Persamaan Schrödinger), namun pengukurannya bersifat probabilistik.

---

## 2. Jembatan 1: Pengukuran sebagai Proyeksi
Dalam mekanika kuantum, setiap instrumen pengukuran mendefinisikan sebuah **basis ortonormal** $\{|n\rangle\}$ dalam ruang Hilbert. Mengukur sistem berarti "memaksa" sistem untuk memilih salah satu dari state basis tersebut.

**Alat (Projector Operator):**
Untuk setiap hasil pengukuran $n$, terdapat operator proyeksi $\hat{P}_n$:
$$ \hat{P}_n = |n\rangle\langle n | $$
Operator ini berfungsi untuk menyaring komponen dari $|\psi\rangle$ yang sejajar dengan hasil $n$.

---

## 3. Postulat Born: Definisi Probabilitas
Aturan Born (dinamai dari Max Born, 1926) menyatakan bahwa probabilitas $P(n)$ untuk mendapatkan hasil $n$ saat mengukur $|\psi\rangle$ adalah kuadrat dari magnitudo amplitudo probabilitasnya.

**Persamaan Utama:**
$$ P(n) = | \langle n | \psi \rangle |^2 = \langle \psi | \hat{P}_n | \psi \rangle $$

**Jembatan Gagasan:**
1.  **Amplitudo ($\langle n | \psi \rangle$):** Merupakan angka kompleks yang menunjukkan "seberapa banyak" komponen $|n\rangle$ di dalam $|\psi\rangle$.
2.  **Probabilitas ($P(n)$):** Merupakan angka riil non-negatif yang menunjukkan peluang kemunculan hasil tersebut.
3.  **Kekekalan Probabilitas:** Karena $\langle \psi | \psi \rangle = 1$ dan $\{|n\rangle\}$ adalah basis lengkap ($\sum \hat{P}_n = I$), maka $\sum P(n) = 1$.

---

## 4. Jembatan 2: Nilai Ekspektasi dan Statistik Pengukuran
Untuk menghubungkan probabilitas individu dengan nilai rata-rata yang kita cari dalam optimasi (VQE), kita memerlukan konsep **Nilai Ekspektasi**.

**Derivasi Runtut:**
Jika kita mengukur observabel $\hat{A}$ yang memiliki nilai eigen $a_n$ untuk state basis $|n\rangle$, maka rata-rata hasil pengukurannya adalah:
$$ \langle \hat{A} \rangle = \sum_n a_n P(n) $$
$$ \langle \hat{A} \rangle = \sum_n a_n \langle \psi | n \rangle \langle n | \psi \rangle = \langle \psi | \left( \sum_n a_n |n\rangle\langle n| \right) | \psi \rangle $$
$$ \langle \hat{A} \rangle = \langle \psi | \hat{A} | \psi \rangle $$

**Filosofi Jembatan:**
Nilai ekspektasi adalah "rata-rata tertimbang" dari semua kemungkinan hasil berdasarkan Aturan Born. Dalam VQE, kita tidak mencari probabilitas satu per satu, melainkan langsung mengestimasi $\langle \hat{H} \rangle$ melalui statistik sampling.

---

## 5. Jembatan 3: Implementasi pada Komputer Kuantum (Digital)
Pada komputer kuantum, pengukuran dilakukan pada **Basis Komputasi** (Z-basis).

**Mekanisme Sampling:**
Untuk sistem $N$-qubit, basis pengukurannya adalah bitstring biner $x \in \{0, 1\}^N$.
1.  State akhir sirkuit adalah $|\psi(\theta^*)\rangle$.
2.  Aturan Born memberikan probabilitas setiap portfolio: $P(x) = |\langle x | \psi(\theta^*) \rangle|^2$.
3.  Hardware melakukan **shot-based measurement**: Menjalankan sirkuit $M$ kali.
4.  Frekuensi relatif $\frac{\text{counts}(x)}{M}$ akan konvergen ke probabilitas Born $P(x)$ saat $M \to \infty$.

---

## 6. Ringkasan Aksioma Born
1.  **Positifitas:** $P(n) \ge 0$.
2.  **Linearitas:** Operator proyeksi bekerja secara linear pada ruang Hilbert.
3.  **Collapse (Reduksi Wavefunction):** Setelah pengukuran menghasilkan $n$, state sistem seketika berubah menjadi $|n\rangle$. Ini adalah alasan mengapa kita memerlukan banyak "shots" untuk merekonstruksi distribusi probabilitas.

**Kesimpulan:**
Aturan Born adalah jembatan terakhir yang mengubah **amplitudo kuantum yang tak terlihat** menjadi **distribusi data yang teramati**. Dalam konteks Markowitz, aturan inilah yang memungkinkan kita memilih aset investasi berdasarkan bitstring yang memiliki probabilitas tertinggi di akhir algoritma VQE.
