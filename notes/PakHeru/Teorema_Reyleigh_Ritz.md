# Teorema Rayleigh-Ritz: Fondasi Matematis Prinsip Variasi

Teorema Rayleigh-Ritz adalah pilar utama dalam analisis numerik dan mekanika kuantum yang memungkinkan kita untuk mengestimasi nilai eigen (terutama nilai eigen terkecil) dari sebuah operator tanpa harus melakukan diagonalisasi matriks secara langsung. Teorema ini menjadi alasan mengapa VQE (Variational Quantum Eigensolver) dapat bekerja.

---

## 1. Definisi Matematis dalam Aljabar Linear

Misalkan $A$ adalah sebuah matriks Hermitian (dalam kuantum, ini adalah Hamiltonian $\hat{H}$) berukuran $n \times n$. Karena $A$ Hermitian, maka:
1.  Semua nilai eigennya adalah riil: $\lambda_0 \le \lambda_1 \le \dots \le \lambda_{n-1}$.
2.  Vektor-vektor eigennya $\{|v_0\rangle, |v_1\rangle, \dots, |v_{n-1}\rangle\}$ membentuk basis ortonormal.

### Hasil Bagi Rayleigh (Rayleigh Quotient)
Untuk setiap vektor non-nol $|\psi\rangle \in \mathbb{C}^n$, Hasil Bagi Rayleigh didefinisikan sebagai:
$$ R(A, \psi) = \frac{\langle \psi | A | \psi \rangle}{\langle \psi | \psi \rangle} $$

**Pernyataan Teorema:**
Nilai dari $R(A, \psi)$ selalu berada di antara nilai eigen terkecil dan terbesar dari $A$:
$$ \lambda_{\min} \le \frac{\langle \psi | A | \psi \rangle}{\langle \psi | \psi \rangle} \le \lambda_{\max} $$

---

## 2. Pembuktian Formal (Derivasi Runtut)

Untuk memahami mengapa ini selalu benar, kita gunakan sifat basis dari vektor eigen.

### Langkah 1: Ekspansi Vektor Trial
Sembarang vektor $|\psi\rangle$ dapat dinyatakan sebagai kombinasi linear dari vektor eigen $|v_i\rangle$:
$$ |\psi\rangle = \sum_{i=0}^{n-1} c_i |v_i\rangle $$
di mana $c_i = \langle v_i | \psi \rangle$ adalah amplitudo probabilitas.

### Langkah 2: Hitung Produk Dalam (Normalisasi)
$$ \langle \psi | \psi \rangle = \left( \sum_j c_j^* \langle v_j | \right) \left( \sum_i c_i |v_i\rangle \right) = \sum_i |c_i|^2 $$
*(Karena $\langle v_j | v_i \rangle = \delta_{ji}$)*

### Langkah 3: Hitung Nilai Ekspektasi Pembilang
$$ \langle \psi | A | \psi \rangle = \langle \psi | \left( A \sum_i c_i |v_i\rangle \right) $$
Karena $A|v_i\rangle = \lambda_i |v_i\rangle$:
$$ \langle \psi | A | \psi \rangle = \left( \sum_j c_j^* \langle v_j | \right) \left( \sum_i c_i \lambda_i |v_i\rangle \right) = \sum_i \lambda_i |c_i|^2 $$

### Langkah 4: Substitusi ke Hasil Bagi Rayleigh
$$ R(A, \psi) = \frac{\sum_i \lambda_i |c_i|^2}{\sum_i |c_i|^2} $$

### Langkah 5: Pembuktian Batas Bawah ($\lambda_0$)
Karena $\lambda_0 \le \lambda_i$ untuk semua $i$, maka kita bisa mengganti setiap $\lambda_i$ dengan $\lambda_0$ dalam pembilang:
$$ \sum_i \lambda_i |c_i|^2 \ge \sum_i \lambda_0 |c_i|^2 = \lambda_0 \sum_i |c_i|^2 $$
Jika kita bagi kedua sisi dengan $\sum_i |c_i|^2$, kita mendapatkan:
$$ \frac{\langle \psi | A | \psi \rangle}{\langle \psi | \psi \rangle} \ge \lambda_0 $$

---

## 3. Interpretasi Fisika: Energi Ground State

Dalam mekanika kuantum, matriks $A$ adalah operator Hamiltonian $\hat{H}$ yang merepresentasikan total energi sistem. Nilai eigen terkecil $\lambda_0$ adalah energi **Ground State** ($E_0$).

Teorema ini memberitahu kita bahwa:
> "Jika kita menebak sembarang keadaan kuantum $|\psi\rangle$, energi rata-rata yang kita ukur tidak akan pernah lebih rendah dari energi ground state yang sebenarnya."

### Konsekuensi Logis:
1. Jika $E(\psi) = E_0$, maka $|\psi\rangle$ pastilah vektor eigen dari ground state (atau berada dalam subruang eigennya).
2. Semakin "pintar" kita memilih $|\psi\rangle$, semakin dekat kita dengan solusi eksak.

---

## 4. Hubungan dengan VQE (Variational Quantum Eigensolver)

VQE meminjam teorema ini untuk mengubah masalah fisika menjadi masalah optimasi komputer klasik:

1.  **Ansatz sebagai Parameterized Map:** Kita membuat sirkuit kuantum yang menghasilkan state $|\psi(\theta)\rangle$. $\theta$ adalah tuas yang kita putar untuk mengubah arah vektor dalam Hilbert space.
2.  **Cost Function:** Kita definisikan fungsi biaya $J(\theta) = \langle \psi(\theta) | \hat{H} | \psi(\theta) \rangle$.
3.  **Minimisasi:** Berdasarkan Teorema Rayleigh-Ritz, kita tahu bahwa nilai minimum global dari $J(\theta)$ adalah $E_0$.
4.  **Hardware-Efficient:** Kita tidak perlu mendiagonalisasi $\hat{H}$ (yang berukuran $2^n \times 2^n$). Kita hanya perlu "menembak" berbagai nilai $\theta$ dan membiarkan prinsip variasi menuntun kita ke dasar lembah energi.

---

## 5. Ringkasan Aksioma
1.  **Hermitisitas:** Hamiltonian harus bisa diukur (eigenvalues riil).
2.  **Kelengkapan Basis:** State apa pun bisa didekati oleh kombinasi state dasar.
3.  **Monotonisitas:** Energi rata-rata menurun seiring pendekatan trial state ke ground state.
