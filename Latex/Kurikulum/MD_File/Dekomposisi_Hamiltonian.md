# Dekomposisi Hamiltonian: Dari Matriks Global ke String Pauli

Dokumen ini menjelaskan mengapa dan bagaimana sebuah operator Hamiltonian $\hat{H}$ yang kompleks didekomposisi menjadi suku-suku dasar (Pauli strings) yang dapat diukur oleh komputer kuantum.

## 1. Urgensi Eksplorasi: Masalah "Raksasa" di Ruang Hilbert
Sistem $n$-qubit memiliki ruang status sebesar $2^n \times 2^n$. Untuk 10 aset saja, matriks Hamiltonian berukuran $1024 \times 1024$. Komputer kuantum tidak dapat "membaca" atau memproses matriks sebesar ini secara utuh. Hardware kuantum hanya dapat melakukan pengukuran pada basis tertentu (biasanya basis Z). Kita butuh cara untuk memecah informasi global ini menjadi potongan-potongan lokal yang bisa diukur secara paralel.

---

## 2. Aksioma & Intuisi: Matriks Pauli sebagai "Atom" Informasi
Setiap matriks Hermitian (energi) dapat dibangun dari 4 "batu bata" dasar yang disebut **Matriks Pauli**:

$$ I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}, X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} $$

**Aksioma:** Matriks Pauli $\{I, X, Y, Z\}$ membentuk basis ortogonal yang lengkap bagi ruang matriks $2 \times 2$. Artinya, sembarang matriks energi 1-qubit pasti bisa dinyatakan sebagai kombinasi linear dari keempat matriks ini dengan koefisien riil.

---

## 3. Reduksionisme: Kasus Minimal (1-Qubit)
Mari kita bedah sebuah Hamiltonian 1-qubit umum $\hat{H}$:
$$ \hat{H} = c_0 I + c_x X + c_y Y + c_z Z \qquad (1) $$

### A. Mencari Koefisien (Proyeksi Trace)
Kita memproyeksikan $\hat{H}$ ke masing-masing basis Pauli menggunakan operasi **Trace** ($\text{Tr}$):
$$ c_k = \frac{1}{2} \text{Tr}(\sigma_k \hat{H}) \qquad (2) $$

> **Visualisasi (2): Perhitungan Matriks (Mencari $c_z$)**
> Misalkan kita punya Hamiltonian dengan energi state $|0\rangle$ sebesar 3 dan state $|1\rangle$ sebesar 1, maka $\hat{H} = \begin{pmatrix} 3 & 0 \\ 0 & 1 \end{pmatrix}$. Mari kita cari komponen $Z$:
> $$ 
\begin{split}
 c_z &= \frac{1}{2} \text{Tr} \left[ \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \begin{pmatrix} 3 & 0 \\ 0 & 1 \end{pmatrix} \right] \\\\
 c_z &= \frac{1}{2} \text{Tr} \begin{pmatrix} 3 & 0 \\ 0 & -1 \end{pmatrix} = \frac{1}{2} (3 + (-1)) = 1
 \end{split}
 $$
> Artinya, energi ini mengandung "gaya" sebesar $1$ unit ke arah sumbu Z.

---

## 4. Jembatan Formalisme & Logika: Banyak Qubit (Many-Body)
Untuk sistem $n$-qubit, kita menggunakan **Produk Tensor** ($\otimes$) untuk membangun basis yang lebih besar.

**Jembatan Logika:** Jika 1 qubit punya 4 basis, maka $n$ qubit punya $4^n$ kombinasi basis (Pauli Strings). Hamiltonian total didekomposisi menjadi jumlahan string:
$$ \hat{H} = \sum_{k=1}^{4^n} c_k P_k \qquad (3) $$
Di mana $P_k$ adalah string seperti $Z \otimes I \otimes X \otimes \dots$.

---

## 5. Derivasi "Scratchpad" & Indeks Persamaan: Linearitas Ekspektasi
Mengapa dekomposisi ini menjadi kunci VQE? Karena sifat linearitas operator dalam mekanika kuantum:
$$ \langle \hat{H} \rangle = \langle \psi | \left( \sum_k c_k P_k \right) | \psi \rangle = \sum_k c_k \langle \psi | P_k | \psi \rangle \qquad (4) $$

> **Visualisasi (4): Aliran Data**
> Bayangkan kita ingin mengukur energi total:
> 1. **Klasik:** Komputer menyimpan daftar koefisien $\{c_k\}$ (misal: $c_1=0.5, c_2=-1.2$).
> 2. **Kuantum:** Hardware mengukur rata-rata string $\langle P_k \rangle$ (misal: $\langle Z_1 Z_2 \rangle = 0.8$).
> 3. **Hasil:** Kita kalikan secara klasik $(0.5 \times 0.8 + \dots)$ untuk mendapatkan total energi.
>
> Ini memungkinkan kita menghitung energi raksasa hanya dengan melakukan banyak pengukuran kecil yang sederhana.

---

## 6. Verifikasi & Parameter: Portofolio Markowitz-Ising
Dalam masalah optimasi portofolio, dekomposisi ini sangat efisien karena Hamiltonian Ising hanya memiliki dua jenis "Lego":

| Jenis Suku | Komponen Fisik | Pauli String ($P_k$) | Makna Ekonomi |
| :--- | :--- | :--- | :--- |
| **Suku Linear** | $h_i \hat{Z}_i$ | $I \otimes \dots \otimes Z \otimes \dots \otimes I$ | Risiko/Return individu aset $i$. |
| **Suku Interaksi** | $J_{ij} \hat{Z}_i \hat{Z}_j$ | $I \otimes \dots \otimes Z \otimes \dots \otimes Z \otimes \dots \otimes I$ | Kovarians (hubungan gerak) aset $i$ dan $j$. |

---

## 7. Analogi "Physical Insight": Spektroskopi Operator
Bayangkan Hamiltonian sebagai **cahaya putih** yang misterius. 
- Dekomposisi Hamiltonian bertindak seperti **Prisma** yang memecah cahaya tersebut menjadi warna-warna dasar (Pauli Strings). 
- Komputer kuantum adalah **Detektor** yang hanya bisa melihat satu warna dalam satu waktu. 
- Dengan mengukur intensitas setiap warna dasar, kita bisa merekonstruksi spektrum energi total dari cahaya tersebut tanpa harus menelan seluruh matari pembentuknya.

---

## 8. Kesimpulan
Dekomposisi Hamiltonian mengubah masalah **eksponensial** (matriks raksasa) menjadi jumlahan **polinomial** dari pengukuran-pengukuran lokal yang praktis. Tanpa teknik ini, prinsip variasi (Rayleigh-Ritz) tidak akan pernah bisa diimplementasikan pada hardware kuantum era NISQ.
