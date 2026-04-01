# Teorema Rayleigh-Ritz: Fondasi Matematis Prinsip Variasi

Dokumen ini menjelaskan bagaimana masalah mencari solusi persamaan Schrodinger diubah menjadi masalah optimasi fungsional menggunakan Kalkulus Variasi.

## 1. Filosofi: Kecenderungan Alam Meminimalkan Energi
Dalam fisika, sistem selalu cenderung menuju kondisi dengan energi terendah (*Ground State*). **Prinsip Variasi** adalah alat matematika yang memungkinkan kita "menebak" kondisi tersebut dengan jaminan bahwa tebakan kita tidak akan pernah lebih rendah dari kenyataan alam semesta.

---

## 2. Kalkulus Variasi: Mencari Titik Stasioner Energi
Bayangkan energi sistem bukan sebagai angka, melainkan sebagai sebuah **fungsional** $E[\psi]$ yang bergantung pada bentuk fungsi gelombang (atau state) $|\psi\rangle$.

### A. Definisi Fungsional Energi
Energi rata-rata dari sebuah sistem didefinisikan sebagai hasil bagi Rayleigh:
$$ E(\psi) = \frac{\langle \psi | \hat{H} | \psi \rangle}{\langle \psi | \psi \rangle} \qquad (1) $$

> **Visualisasi (1): Jembatan Logika**
> Mengapa kita membagi dengan $\langle \psi | \psi \rangle$? Karena kita ingin memastikan nilai energi tidak bergantung pada "panjang" vektor $|\psi\rangle$ (normalisasi). 
> Jika $|\psi\rangle$ sudah ternormalisasi ($\langle \psi | \psi \rangle = 1$), maka $E(\psi) = \langle \psi | \hat{H} | \psi \rangle$.

### B. Variasi Fungsional ($\delta E = 0$)
Untuk mencari energi minimum, kita lakukan variasi kecil terhadap $|\psi\rangle$ dan menetapkan perubahannya menjadi nol.
$$ \delta E = \delta \left[ \frac{\langle \psi | \hat{H} | \psi \rangle}{\langle \psi | \psi \rangle} \right] = 0 \qquad (2) $$

> **Visualisasi (2): Perhitungan Linear (Uraian Variasi)**
> Menggunakan aturan hasil bagi $(u/v)' = (u'v - uv')/v^2$:
> $$ \delta E = \frac{\delta \langle \psi | \hat{H} | \psi \rangle \cdot \langle \psi | \psi \rangle - \langle \psi | \hat{H} | \psi \rangle \cdot \delta \langle \psi | \psi \rangle}{(\langle \psi | \psi \rangle)^2} = 0 $$
> Agar hasil bagi ini nol, maka pembilangnya harus nol:
> $$ \delta \langle \psi | \hat{H} | \psi \rangle \cdot \langle \psi | \psi \rangle = \langle \psi | \hat{H} | \psi \rangle \cdot \delta \langle \psi | \psi \rangle \qquad (3) $$

---

## 3. Jembatan Logika: Menuju Persamaan Nilai Eigen
Jika kita uraikan variasi pada persamaan (3) terhadap bra $\langle \psi |$:
$$ \langle \delta \psi | \hat{H} | \psi \rangle \cdot \langle \psi | \psi \rangle = \langle \psi | \hat{H} | \psi \rangle \cdot \langle \delta \psi | \psi \rangle $$
Pindahkan suku $\langle \psi | \psi \rangle$ ke bawah:
$$ \langle \delta \psi | \hat{H} | \psi \rangle = \left( \frac{\langle \psi | \hat{H} | \psi \rangle}{\langle \psi | \psi \rangle} \right) \langle \delta \psi | \psi \rangle \qquad (4) $$

Karena suku dalam kurung adalah $E$, maka:
$$ \langle \delta \psi | ( \hat{H} | \psi \rangle - E | \psi \rangle ) = 0 $$
Karena variasi $\langle \delta \psi |$ bersifat sembarang, maka bagian dalam kurung harus nol:
$$ \hat{H} | \psi \rangle = E | \psi \rangle \qquad (5) $$

**Kesimpulan Jembatan:** Mencari titik stasioner dari fungsional energi $E(\psi)$ identik dengan menyelesaikan persamaan nilai eigen Schrodinger.

---

## 4. Reduksionisme: Pembuktian $E(\psi) \ge E_0$
Sekarang kita buktikan bahwa tebakan apa pun ($|\psi\rangle$) selalu memberikan energi di atas atau sama dengan ground state ($E_0$).

### A. Ekspansi dalam Basis Eigen
Misalkan $\{|v_n\rangle\}$ adalah set vektor eigen dari $\hat{H}$ dengan energi $E_0 \le E_1 \le E_2 \dots$. Sembarang state $|\psi\rangle$ dapat ditulis sebagai:
$$ |\psi\rangle = \sum_n c_n |v_n\rangle \qquad (6) $$

> **Visualisasi (6): Operasi Matriks**
> Secara linear, $|\psi\rangle$ adalah jumlahan berbobot dari state-state murni (basis eigen):
> $$ |\psi\rangle = c_0 |v_0\rangle + c_1 |v_1\rangle + \dots = \begin{pmatrix} c_0 \\ c_1 \\ \vdots \end{pmatrix} $$

### B. Substitusi ke Rayleigh Quotient
$$ E(\psi) = \frac{\sum_n |c_n|^2 E_n}{\sum_n |c_n|^2} \qquad (7) $$

> **Visualisasi (7): Perhitungan Linear**
> Karena $E_n \ge E_0$ untuk semua $n$, maka:
> $$ \sum_n |c_n|^2 E_n \ge \sum_n |c_n|^2 E_0 = E_0 \sum_n |c_n|^2 $$
> Masukkan kembali ke pembilang persamaan (7):
> $$ E(\psi) \ge \frac{E_0 \sum_n |c_n|^2}{\sum_n |c_n|^2} = E_0 \qquad (8) $$

---

## 5. Verifikasi & Parameter: Batas Bawah
| Kondisi $\psi\rangle$              | Nilai $E(\psi)$   | Interpretasi Fisik                                 |
| :--------------------------------- | :---------------- | -------------------------------------------------- |
| **$\psi\rangle =v_0\rangle$**      | $E(\psi) = E_0$   | Tebakan tepat mengenai ground state.               |
| **$\psi\rangle \perp v_0\rangle$** | $E(\psi) \ge E_1$ | Tebakan tidak mengandung komponen ground state.    |
| **Sembarang $\psi\rangle$**        | $E(\psi) > E_0$   | Tebakan mengandung "pengotor" dari state eksitasi. |

---

## 6. Physical Insight: "Nature's Compass"
Prinsip variasi bertindak sebagai **kompas** bagi algoritma VQE.
1. Kita membuat sirkuit parametrik $|\psi(\theta)\rangle$.
2. Kita menghitung energi $E(\theta)$ menggunakan QPU.
3. Kita tahu dengan pasti bahwa semakin kecil $E(\theta)$, semakin dekat kita dengan solusi ekonomi optimal ($E_0$).

**Mengapa ini penting untuk portofolio?**
Karena kita tidak bisa mendiagonalkan matriks kovarians yang sangat besar, kita menggunakan Prinsip Variasi untuk "meraba" dasar lembah energi. Kita tidak perlu tahu di mana dasarnya, kita hanya perlu terus bergerak "ke bawah" sesuai petunjuk Teorema Rayleigh-Ritz.
