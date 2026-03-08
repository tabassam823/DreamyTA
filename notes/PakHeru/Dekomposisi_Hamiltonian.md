# Dekomposisi Hamiltonian: Dari Matriks Global ke String Pauli

Dokumen ini menjelaskan mengapa dan bagaimana sebuah operator Hamiltonian $\hat{H}$ yang kompleks didekomposisi menjadi suku-suku dasar (Pauli strings) yang dapat diukur oleh komputer kuantum. Penjelasan ini disusun secara fundamental, menghubungkan aksioma mekanika kuantum dengan implementasi algoritma VQE.

---

## 1. Postulat Dasar: Observabel dan Hermitisitas
Dalam mekanika kuantum, setiap properti fisik yang dapat diukur (seperti total energi sistem) direpresentasikan oleh sebuah **operator linear Hermitian** $\hat{H}$ yang bekerja pada ruang Hilbert $\mathcal{H}$.

**Aksioma & Konvensi:**
1.  **Nilai Eigen Riil:** Karena energi adalah kuantitas fisik yang teramati, maka Hamiltonian $\hat{H}$ harus bersifat Hermitian ($\hat{H} = \hat{H}^\dagger$). Sifat ini menjamin bahwa semua nilai eigen (energi yang mungkin diukur) adalah bilangan riil.
2.  **Representasi Matriks:** Untuk sistem $n$-qubit, $\hat{H}$ direpresentasikan sebagai matriks kompleks berukuran $2^n \times 2^n$.

**Masalah Filosofis:**
Komputer kuantum tidak dapat "membaca" atau memproses matriks $2^n \times 2^n$ secara utuh (yang tumbuh secara eksponensial terhadap jumlah qubit). Komputer kuantum hanya dapat melakukan pengukuran pada basis tertentu (biasanya basis komputasi Z). Oleh karena itu, kita memerlukan **jembatan** untuk memecah informasi global ini menjadi potongan-potongan informasi lokal yang dapat diukur.

---

## 2. Jembatan 1: Basis Pauli sebagai "Atom" Operator
Untuk sistem 1-qubit ($2 \times 2$), terdapat empat matriks dasar yang membentuk basis ortogonal lengkap bagi ruang matriks Hermitian. Matriks ini disebut **Matriks Pauli**:

$$ \sigma_0 = I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}, \sigma_1 = X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \sigma_2 = Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \sigma_3 = Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} $$

**Konvensi Dekomposisi:**
Setiap matriks Hermitian $M_{2 \times 2}$ dapat dinyatakan secara unik sebagai kombinasi linear dari basis Pauli dengan koefisien riil $c_i$:
$$ M = c_0 I + c_1 X + c_2 Y + c_3 Z $$
Ini adalah jembatan pertama: mengubah matriks abstrak menjadi bobot dari empat "atom" informasi.

---

## 3. Jembatan 2: Produk Tensor untuk Sistem Banyak-Tubuh (Many-Body)
Untuk memperluas basis Pauli ke sistem $n$-qubit, kita menggunakan operasi **Produk Tensor ($\otimes$)**.

**Postulat Komposisi:**
Ruang Hilbert dari sistem gabungan adalah produk tensor dari ruang Hilbert masing-masing komponen. Maka, basis untuk sistem $n$-qubit adalah himpunan **Pauli Strings**:
$$ \mathcal{P}_n = \{ \sigma_{i_1} \otimes \sigma_{i_2} \otimes \dots \otimes \sigma_{i_n} \} $$
di mana $i_k \in \{0, 1, 2, 3\}$.

**Karakteristik Jembatan:**
- Terdapat $4^n$ kombinasi Pauli String yang mungkin.
- Setiap Pauli String $P_k$ bersifat Unitari dan Hermitian ($P_k^2 = I$).
- Pauli Strings membentuk basis ortogonal di bawah **Inner Product Hilbert-Schmidt**: $\langle A, B \rangle = \text{Tr}(A^\dagger B)$.

---

## 4. Mekanisme Dekomposisi: Proyeksi Operator
Diberikan Hamiltonian $\hat{H}$ yang kompleks, kita ingin mencari koefisien $c_k$ sehingga:
$$ \hat{H} = \sum_{k=1}^{4^n} c_k P_k $$

**Prosedur Matematika (Proyeksi):**
Karena sifat ortogonalitas basis Pauli, koefisien $c_k$ dapat dihitung dengan memproyeksikan $\hat{H}$ ke setiap basis $P_k$ menggunakan jejak matriks (trace):
$$ c_k = \frac{1}{2^n} \text{Tr}(P_k \hat{H}) $$

**Filosofi Praktis:**
Dalam masalah optimasi (seperti Markowitz), kita tidak mulai dari matriks penuh lalu mendekomposisinya. Sebaliknya, kita **membangun** $\hat{H}$ langsung dari variabel biner yang sudah ditransformasikan ke operator $Z$ (Ising model). Ini secara otomatis menghasilkan Hamiltonian yang sudah terdekomposisi.

---

## 5. Jembatan 3: Linearitas Nilai Ekspektasi
Mengapa dekomposisi ini menjadi "jantung" dari algoritma VQE? Jawabannya terletak pada sifat **Linearitas Operator**.

**Aksioma Pengukuran:**
Nilai rata-rata (ekspektasi) energi sistem pada state $|\psi\rangle$ adalah:
$$ \langle E \rangle = \langle \psi | \hat{H} | \psi \rangle $$

Menggunakan hasil dekomposisi:
$$ \langle E \rangle = \langle \psi | \left( \sum_k c_k P_k \right) | \psi \rangle $$
Berdasarkan sifat linearitas:
$$ \langle E \rangle = \sum_k c_k \langle \psi | P_k | \psi \rangle $$

**Konsekuensi Logis:**
1. Kita tidak perlu mengukur $\hat{H}$ secara utuh (yang mustahil).
2. Kita mengukur setiap Pauli String $P_k$ secara terpisah pada perangkat kuantum.
3. Kita menjumlahkan hasilnya secara klasik menggunakan komputer biasa untuk mendapatkan total energi.

---

## 6. Aplikasi pada Model Markowitz-Ising
Dalam Portofolio Markowitz, dekomposisi ini menjadi sangat efisien karena Hamiltonian Ising hanya menggunakan dua jenis Pauli String:

1.  **Suku Linear ($h_i \hat{Z}_i$):** Mengukur kecenderungan aset tunggal terhadap risiko/return.
    - $P_k = I \otimes \dots \otimes Z \otimes \dots \otimes I$
2.  **Suku Interaksi ($J_{ij} \hat{Z}_i \hat{Z}_j$):** Mengukur korelasi (kovarians) antar dua aset.
    - $P_k = I \otimes \dots \otimes Z \otimes \dots \otimes Z \otimes \dots \otimes I$

**Kesimpulan:**
Dekomposisi Hamiltonian adalah proses mengubah **operator energi global** yang tidak terjangkau menjadi **kombinasi informasi lokal** yang dapat dibaca oleh qubit. Tanpa dekomposisi ini, prinsip variasi (Rayleigh-Ritz) tidak akan pernah bisa diimplementasikan pada hardware kuantum era NISQ.
