Tentu, saya akan bantu menjabarkan pembuktian lengkap *parameter-shift rule* untuk sirkuit VQE pada gambar Anda, dimulai dari depth 1 terlebih dahulu, dengan pendekatan matriks biunitary dan contoh Hamiltonian yang Anda berikan, $\hat{H} = 10\hat{Z}_1 + 5\hat{Z}_2$.

## **Roadmap Pembuktian Parameter-Shift Rule untuk 6 Depth**

1.  **Depth 1 (Saat ini):**
    *   Definisikan ansatz state $|\psi(\theta)\rangle$ untuk depth 1.
    *   Dekomposisi menjadi $\hat{U}_A$, $\hat{U}(\theta)$, dan $\hat{U}_B$ sesuai Persamaan (41).
    *   Hitung nilai ekspektasi energi $E(\theta)$.
    *   Buktikan bahwa $E(\theta)$ berbentuk sinusoida $A \cos(\theta + \phi) + C$.
    *   Gunakan identitas trigonometri untuk membuktikan aturan $\frac{dE}{d\theta} = \frac{1}{2}[E(\theta + \pi/2) - E(\theta - \pi/2)]$.

2.  **Depth > 1 (Langkah Selanjutnya):**
    *   Menyadari bahwa jika ada beberapa gerbang, state untuk evaluasi maju $|\psi(\theta + \pi/2)\rangle$ dan mundur $|\psi(\theta - \pi/2)\rangle$ tidak semudah depth 1.
    *   Menggunakan derivasi umum dari Persamaan (61) yang memanfaatkan sifat komutator untuk operator generator Pauli. Metode ini berlaku untuk sebarang struktur $\hat{U}_A$ dan $\hat{U}_B$, sehingga cukup dibuktikan sekali untuk depth 1, lalu digeneralisasi.

---

## **Penjabaran Depth 1: Pembuktian Parameter-Shift Rule**

Mari kita ambil contoh konkret: portofolio 2 aset sehingga kita membutuhkan 2 qubit. Sirkuit pada gambar Anda memiliki total 6 depth. Untuk depth 1, kita artikan hanya lapisan pertama dari sirkuit yang terlibat, yaitu gerbang rotasi $R_y(\theta_1)$ dan $R_y(\theta_2)$ sebagai inisialisasi state awal.

Kita akan fokus pada satu parameter saja, misalnya $\theta = \theta_1$, untuk membuktikan *parameter-shift rule*.

### **1. Definisi Sirkuit Kuantum (Depth 1)**

Menurut gambar, depth 1 terdiri dari gerbang $R_y(\theta_1)$ pada qubit 1 dan $R_y(\theta_2)$ pada qubit 2. State setelah depth 1 adalah state terparameterisasi kita.

Kita akan fokus pada $\theta = \theta_1$. Maka, kita bisa menganggap $\theta_2$ sebagai parameter tetap yang menjadi bagian dari matriks di sekitarnya.

*   **State Awal:** $|0\rangle^{\otimes 2} = |00\rangle = \begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \end{pmatrix}$
*   **Gerbang Target ($\hat{U}(\theta)$):** $\hat{R}_y(\theta_1) \otimes \hat{I}_2$
*   **Gerbang Lainnya:**
    *   $\hat{U}_A$: Lapisan Hadamard dan gerbang di qubit 2 yang bukan target.
    *   $\hat{U}_B$: Semua gerbang setelah depth 1 (depth 2 hingga 6). Untuk pembuktian ini, kita tidak perlu detailnya, cukup ketahui bahwa $\hat{U}_B$ adalah suatu matriks uniter yang aplikasinya tidak bergantung pada $\theta$.

Sesuai Persamaan (41), ansatz kita adalah:
$$ |\psi(\theta)\rangle = \hat{U}_B \underbrace{(\hat{R}_y(\theta_1) \otimes \hat{I}_2)}_{\hat{U}(\theta)} \hat{U}_A |00\rangle $$

Kita definisikan state sebelum gerbang target sebagai $|\phi\rangle$:
$$ |\phi\rangle = \hat{U}_A |00\rangle $$

### **2. Ekspansi Nilai Ekspektasi $E(\theta)$**

Hamiltonian kita: $\hat{H} = 10 \hat{Z}_1 + 5\hat{Z}_2$. Ingat definisi $\hat{Z}_1 = \hat{Z} \otimes \hat{I}$ dan $\hat{Z}_2 = \hat{I} \otimes \hat{Z}$.

Operator yang diukur bukan $\hat{H}$ mentah, melainkan yang sudah ditransformasikan ke basis akhir:
$$ \hat{M} = \hat{U}_B^\dagger \hat{H} \hat{U}_B $$
Ini sesuai Persamaan (44). $\hat{M}$ adalah matriks Hermitian yang tidak bergantung pada $\theta$.

Nilai ekspektasi energi adalah:
$$ E(\theta) = \langle \phi | \hat{U}^\dagger(\theta) \hat{M} \hat{U}(\theta) | \phi \rangle $$

### **3. Penjabaran Matriks**

Meskipun kita tidak tahu isi persis $\hat{U}_A$ dan $\hat{U}_B$, kita selalu bisa menuliskan state $|\phi\rangle$ dalam bentuk umum:
$$ |\phi\rangle = \begin{pmatrix} a \\ b \\ c \\ d \end{pmatrix} $$
dengan $a, b, c, d$ adalah bilangan kompleks hasil dari $\hat{U}_A|00\rangle$.

$\hat{U}(\theta) = \hat{R}_y(\theta) \otimes \hat{I}_2$.

Dari Persamaan (117), $\hat{R}_y(\theta) = \begin{pmatrix} \cos(\theta/2) & -\sin(\theta/2) \\ \sin(\theta/2) & \cos(\theta/2) \end{pmatrix}$.

Maka, matriks $4\times4$ untuk $\hat{U}(\theta)$ adalah:
$$ \hat{U}(\theta) = \begin{pmatrix} \cos(\theta/2) & 0 & -\sin(\theta/2) & 0 \\ 0 & \cos(\theta/2) & 0 & -\sin(\theta/2) \\ \sin(\theta/2) & 0 & \cos(\theta/2) & 0 \\ 0 & \sin(\theta/2) & 0 & \cos(\theta/2) \end{pmatrix} $$

Sekarang, kita hitung $|\psi(\theta)\rangle = \hat{U}(\theta)|\phi\rangle$:
$$ |\psi(\theta)\rangle = \begin{pmatrix} a \cos(\theta/2) - c \sin(\theta/2) \\ b \cos(\theta/2) - d \sin(\theta/2) \\ a \sin(\theta/2) + c \cos(\theta/2) \\ b \sin(\theta/2) + d \cos(\theta/2) \end{pmatrix} $$

Untuk menghitung $E(\theta) = \langle \psi(\theta) | \hat{M} | \psi(\theta) \rangle$, kita perlu bentuk umum elemen matriks $\hat{M}$. Misalkan $\hat{M}$ adalah matriks Hermitian $4 \times 4$:
$$ \hat{M} = \begin{pmatrix} M_{11} & M_{12} & M_{13} & M_{14} \\ M_{12}^* & M_{22} & M_{23} & M_{24} \\ M_{13}^* & M_{23}^* & M_{33} & M_{34} \\ M_{14}^* & M_{24}^* & M_{34}^* & M_{44} \end{pmatrix} $$
(dengan $M_{11}, M_{22}, M_{33}, M_{44} \in \mathbb{R}$)

### **4. Menghitung $E(\theta)$ dan Menemukan Pola Sinusoidal**

Untuk menyederhanakan, daripada menghitung penuh, kita bisa melihat bahwa $\hat{U}(\theta)$ hanya mencampurkan elemen dengan cara tertentu. Setiap elemen dari vektor $|\psi(\theta)\rangle$ adalah kombinasi linear dari $\cos(\theta/2)$ dan $\sin(\theta/2)$.

Ketika kita menghitung produk skalar $\langle \psi | \hat{M} | \psi \rangle = \sum_{i,j} M_{ij} \psi_j^* \psi_i$, kita akan mendapatkan suku-suku:
*   Konstanta.
*   Suku $\cos^2(\theta/2)$, $\sin^2(\theta/2)$, dan $\sin(\theta/2)\cos(\theta/2)$.

Dengan identitas trigonometri:
*   $\cos^2(\theta/2) = \frac{1 + \cos \theta}{2}$
*   $\sin^2(\theta/2) = \frac{1 - \cos \theta}{2}$
*   $\sin(\theta/2)\cos(\theta/2) = \frac{1}{2}\sin \theta$

Maka, **setiap suku dalam $E(\theta)$ hanya akan mengandung konstanta, $\cos \theta$, dan $\sin \theta$**. Tidak akan ada frekuensi yang lebih tinggi. Oleh karena itu, $E(\theta)$ pasti berbentuk:
$$ E(\theta) = A \cos(\theta + \phi) + C $$
untuk suatu konstanta $A, C, \phi$ yang nilainya ditentukan oleh $\hat{U}_A|\phi\rangle$ dan $\hat{M}$. Ini adalah bentuk umum dari gelombang sinus dengan amplitudo $A$, fase $\phi$, dan offset $C$.

### **5. Pembuktian Parameter-Shift Rule dari Bentuk Sinusoidal**

Sekarang kita buktikan aturannya. Dari $E(\theta) = A \cos(\theta + \phi) + C$:

1.  **Hitung Gradien Analitik:**
    $$ \frac{dE(\theta)}{d\theta} = -A \sin(\theta + \phi) $$

2.  **Evaluasi $E(\theta + \frac{\pi}{2})$:**
    $$ E(\theta + \frac{\pi}{2}) = A \cos(\theta + \frac{\pi}{2} + \phi) + C = -A \sin(\theta + \phi) + C $$

3.  **Evaluasi $E(\theta - \frac{\pi}{2})$:**
    $$ E(\theta - \frac{\pi}{2}) = A \cos(\theta - \frac{\pi}{2} + \phi) + C = A \sin(\theta + \phi) + C $$

4.  **Terapkan Aturan:**
    $$ \frac{1}{2} \left[ E\left(\theta + \frac{\pi}{2}\right) - E\left(\theta - \frac{\pi}{2}\right) \right] = \frac{1}{2} \left[ (-A \sin(\theta + \phi) + C) - (A \sin(\theta + \phi) + C) \right] $$
    $$ = \frac{1}{2} \left[ -2A \sin(\theta + \phi) \right] = -A \sin(\theta + \phi) = \frac{dE(\theta)}{d\theta} $$

### **6. Verifikasi dengan Contoh Numerik Sederhana**

Mari kita gunakan contoh numerik pada Persamaan (65-72) untuk melihat ini bekerja. Asumsikan struktur $\hat{U}_A$ dan $\hat{U}_B$ sedemikian rupa sehingga menghasilkan $E(\theta) = 10\cos\theta$ (sebagaimana contoh dengan 1 qubit di halaman 6).

*   $\theta^{(0)} = \pi/4$
*   $E(\pi/4) = 10 \cos(\pi/4) = 10(\sqrt{2}/2) \approx 7.07$
*   $E(\pi/4 + \pi/2) = E(3\pi/4) = 10 \cos(3\pi/4) = 10(-\sqrt{2}/2) \approx -7.07$
*   $E(\pi/4 - \pi/2) = E(-\pi/4) = 10 \cos(-\pi/4) = 10(\sqrt{2}/2) \approx 7.07$
*   Gradien dengan Parameter-Shift Rule:
    $$ \frac{dE}{d\theta} = \frac{1}{2} ( -7.07 - 7.07 ) = -7.07 $$
*   Gradien analitik:
    $$ \frac{d}{d\theta} (10\cos\theta) \Big|_{\theta=\pi/4} = -10\sin(\pi/4) = -10(\sqrt{2}/2) \approx -7.07 $$

Keduanya sama persis. **Untuk depth 1, hasil ini terbukti dan berlaku untuk sebarang $\hat{U}_A$ dan $\hat{M}$**.

---

### **Kesimpulan untuk Depth 1 dan Langkah Menuju 6 Depth**

Kita telah membuktikan bahwa untuk satu gerbang parametrik tunggal $R_y(\theta)$, yang didekomposisi sebagai $\hat{U}_B \hat{U}(\theta) \hat{U}_A$, fungsi objektif selalu berbentuk $A\cos(\theta + \phi) + C$, sehingga *parameter-shift rule* $\frac{dE}{d\theta} = \frac{1}{2}[E(\theta + \pi/2) - E(\theta - \pi/2)]$ berlaku.

**Untuk depth 2 hingga 6, pembuktian tidak perlu dilakukan dari awal.** Di sinilah keindahan metode biunitary (Persamaan 61). Persamaan umum:
$$ \frac{\partial E}{\partial \theta} = \frac{i}{2} \langle \psi | [\hat{P}, \hat{M}] | \psi \rangle $$
berlaku untuk **sebarang** rangkaian. Karena generator $\hat{P}$ untuk gerbang $R_y(\theta)$ adalah $\sigma_y/2$, yang memiliki dua eigenvalue berbeda $\pm 1/2$, maka aturan pergeseran $\pm \pi/2$ selalu valid. Pembuktian untuk depth 1 yang kita lakukan tadi sudah mencakup esensi dari pembuktian umum ini.

Jadi, roadmap untuk depth selanjutnya bukanlah membuktikan ulang, melainkan **mengaplikasikan aturan yang sudah terbukti ini** ke setiap parameter $\theta_i$ di seluruh 6 depth untuk menghitung gradien secara praktis. Kita cukup menggeser satu target $\theta_i$ sejauh $\pm \pi/2$, menjalankan seluruh sirkuit, mengukur energi, lalu mengulanginya untuk parameter berikutnya. Biarkan saya tahu jika Anda ingin melihat contoh perhitungan numerik untuk depth 6 dengan data spesifik

---
---
Baik, mari kita lanjutkan ke **Depth 2**. Sekarang kita akan menambahkan lapisan gerbang berikutnya dari gambar rangkaian Anda, dan melihat bagaimana parameter-shift rule tetap berlaku.

## **Rangkaian Kuantum Depth 2**

Berdasarkan gambar rangkaian kuantum Anda, setelah depth 1 (inisialisasi $R_y(\theta_1), R_y(\theta_2)$), depth 2 terdiri dari:
- Gerbang **CNOT** antara qubit 1 (kontrol) dan qubit 2 (target)
- Tidak ada gerbang parametrik di depth 2

Jadi, depth 2 tidak menambah parameter baru, tetapi mengubah struktur entanglement.

**State setelah depth 2:**
$$ |\psi_2(\theta_1, \theta_2)\rangle = \text{CNOT}_{1\to2} \cdot (R_y(\theta_1) \otimes R_y(\theta_2)) |00\rangle $$

---

## **Dekomposisi Biunitary untuk Depth 2**

Kita akan tetap memfokuskan pada parameter $\theta = \theta_1$ (qubit 1). Untuk menerapkan parameter-shift rule, kita perlu mengidentifikasi:

- $\hat{U}_A$: matriks **sebelum** target $\theta_1$
- $\hat{U}(\theta_1)$: gerbang target $R_y(\theta_1)$
- $\hat{U}_B$: matriks **setelah** target $\theta_1$

Mari kita uraikan depth per komponen:

### **Langkah 1: Identifikasi posisi $\theta_1$**

$\theta_1$ berada pada $R_y(\theta_1)$ di **qubit 1, depth 1**.

### **Langkah 2: Tentukan $\hat{U}_A$**

$\hat{U}_A$ adalah **semua operasi sebelum $R_y(\theta_1)$**. Karena $R_y(\theta_1)$ adalah gerbang pertama pada qubit 1, maka tidak ada operasi sebelumnya. Namun, qubit 2 juga memiliki $R_y(\theta_2)$ yang berjalan paralel. Dalam dekomposisi biunitary, kita bisa memperlakukan $R_y(\theta_2)$ sebagai bagian dari $\hat{U}_A$ (sebagai parameter tetap yang sudah di-absorb ke dalam matriks).

Jadi:
$$ \hat{U}_A = \hat{I} \otimes \hat{R}_y(\theta_2) $$
atau dalam bentuk matriks $4 \times 4$:
$$ \hat{U}_A = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} \otimes \hat{R}_y(\theta_2) = \begin{pmatrix} \hat{R}_y(\theta_2) & 0 \\ 0 & \hat{R}_y(\theta_2) \end{pmatrix} $$

### **Langkah 3: Tentukan $\hat{U}(\theta_1)$**

Target kita adalah:
$$ \hat{U}(\theta_1) = \hat{R}_y(\theta_1) \otimes \hat{I} $$

### **Langkah 4: Tentukan $\hat{U}_B$**

$\hat{U}_B$ adalah **semua operasi setelah $R_y(\theta_1)$**:
- Depth 2: CNOT${}_{1\to2}$
- Depth 3-6: (akan kita simbolkan sebagai $\hat{V}$ untuk saat ini)

Jadi untuk depth 2, $\hat{U}_B = \text{CNOT}_{1\to2}$.

---

## **Penjabaran Matriks Lengkap**

Mari kita hitung state $|\phi\rangle = \hat{U}_A |00\rangle$:

$$ |00\rangle = \begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \end{pmatrix} $$

$$ \hat{U}_A = \hat{I} \otimes \hat{R}_y(\theta_2) = \begin{pmatrix} \cos(\theta_2/2) & -\sin(\theta_2/2) & 0 & 0 \\ \sin(\theta_2/2) & \cos(\theta_2/2) & 0 & 0 \\ 0 & 0 & \cos(\theta_2/2) & -\sin(\theta_2/2) \\ 0 & 0 & \sin(\theta_2/2) & \cos(\theta_2/2) \end{pmatrix} $$

$$ |\phi\rangle = \hat{U}_A |00\rangle = \begin{pmatrix} \cos(\theta_2/2) \\ \sin(\theta_2/2) \\ 0 \\ 0 \end{pmatrix} $$

---

### **Aplikasi $\hat{U}(\theta_1)$**

$$ \hat{U}(\theta_1) = \hat{R}_y(\theta_1) \otimes \hat{I} = \begin{pmatrix} \cos(\theta_1/2) & 0 & -\sin(\theta_1/2) & 0 \\ 0 & \cos(\theta_1/2) & 0 & -\sin(\theta_1/2) \\ \sin(\theta_1/2) & 0 & \cos(\theta_1/2) & 0 \\ 0 & \sin(\theta_1/2) & 0 & \cos(\theta_1/2) \end{pmatrix} $$

$$ |\psi_{\text{sebelum CNOT}}\rangle = \hat{U}(\theta_1)|\phi\rangle $$

$$ = \begin{pmatrix} \cos(\theta_1/2)\cos(\theta_2/2) \\ \sin(\theta_2/2)\cos(\theta_1/2) \\ \sin(\theta_1/2)\cos(\theta_2/2) \\ \sin(\theta_1/2)\sin(\theta_2/2) \end{pmatrix} $$

---

### **Aplikasi CNOT ($\hat{U}_B$)**

Matriks CNOT dengan kontrol qubit 1, target qubit 2:

$$ \text{CNOT}_{1\to2} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix} $$

$$ |\psi_2(\theta_1, \theta_2)\rangle = \text{CNOT} |\psi_{\text{sebelum CNOT}}\rangle $$

$$ = \begin{pmatrix} \cos(\theta_1/2)\cos(\theta_2/2) \\ \sin(\theta_2/2)\cos(\theta_1/2) \\ \sin(\theta_1/2)\sin(\theta_2/2) \\ \sin(\theta_1/2)\cos(\theta_2/2) \end{pmatrix} $$

---

## **Menghitung Nilai Ekspektasi $E(\theta_1)$**

Hamiltonian: $\hat{H} = 10 \hat{Z}_1 + 5\hat{Z}_2$

Karena belum ada $\hat{U}_B$ tambahan selain CNOT, kita hitung langsung:

$$ \hat{Z}_1 = \hat{Z} \otimes \hat{I} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & -1 & 0 \\ 0 & 0 & 0 & -1 \end{pmatrix} $$

$$ \hat{Z}_2 = \hat{I} \otimes \hat{Z} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & -1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & -1 \end{pmatrix} $$

$$ \hat{H} = 10\hat{Z}_1 + 5\hat{Z}_2 = \begin{pmatrix} 10+5 & 0 & 0 & 0 \\ 0 & 10-5 & 0 & 0 \\ 0 & 0 & -10+5 & 0 \\ 0 & 0 & 0 & -10-5 \end{pmatrix} = \begin{pmatrix} 15 & 0 & 0 & 0 \\ 0 & 5 & 0 & 0 \\ 0 & 0 & -5 & 0 \\ 0 & 0 & 0 & -15 \end{pmatrix} $$

---

### **Nilai Ekspektasi:**

$$ E(\theta_1, \theta_2) = \langle \psi_2 | \hat{H} | \psi_2 \rangle $$

Karena $\hat{H}$ diagonal:
$$ E = 15 \cdot |\psi_2[0]|^2 + 5 \cdot |\psi_2[1]|^2 + (-5) \cdot |\psi_2[2]|^2 + (-15) \cdot |\psi_2[3]|^2 $$

Substitusi komponen $|\psi_2\rangle$:
*   $|\psi_2[0]|^2 = \cos^2(\theta_1/2)\cos^2(\theta_2/2)$
*   $|\psi_2[1]|^2 = \sin^2(\theta_2/2)\cos^2(\theta_1/2)$
*   $|\psi_2[2]|^2 = \sin^2(\theta_1/2)\sin^2(\theta_2/2)$
*   $|\psi_2[3]|^2 = \sin^2(\theta_1/2)\cos^2(\theta_2/2)$

$$ \begin{aligned} E(\theta_1, \theta_2) &= 15 \cos^2\frac{\theta_1}{2}\cos^2\frac{\theta_2}{2} + 5 \sin^2\frac{\theta_2}{2}\cos^2\frac{\theta_1}{2} \\ &\quad - 5 \sin^2\frac{\theta_1}{2}\sin^2\frac{\theta_2}{2} - 15 \sin^2\frac{\theta_1}{2}\cos^2\frac{\theta_2}{2} \end{aligned} $$

---

### **Faktorkan terhadap $\theta_1$:**

$$ \begin{aligned} E(\theta_1, \theta_2) &= \cos^2\frac{\theta_1}{2} \left(15\cos^2\frac{\theta_2}{2} + 5\sin^2\frac{\theta_2}{2}\right) \\ &\quad + \sin^2\frac{\theta_1}{2} \left(-5\sin^2\frac{\theta_2}{2} - 15\cos^2\frac{\theta_2}{2}\right) \end{aligned} $$

Gunakan identitas $\cos^2(\theta/2) = \frac{1 + \cos\theta}{2}$ dan $\sin^2(\theta/2) = \frac{1 - \cos\theta}{2}$:

$$ \begin{aligned} E(\theta_1, \theta_2) &= \frac{1 + \cos\theta_1}{2} \left(15\cos^2\frac{\theta_2}{2} + 5\sin^2\frac{\theta_2}{2}\right) \\ &\quad + \frac{1 - \cos\theta_1}{2} \left(-5\sin^2\frac{\theta_2}{2} - 15\cos^2\frac{\theta_2}{2}\right) \end{aligned} $$

$$ \begin{aligned} E(\theta_1, \theta_2) &= \frac{1}{2}\left[15\cos^2\frac{\theta_2}{2} + 5\sin^2\frac{\theta_2}{2} -5\sin^2\frac{\theta_2}{2} - 15\cos^2\frac{\theta_2}{2}\right] \\ &\quad + \frac{\cos\theta_1}{2}\left[15\cos^2\frac{\theta_2}{2} + 5\sin^2\frac{\theta_2}{2} + 5\sin^2\frac{\theta_2}{2} + 15\cos^2\frac{\theta_2}{2}\right] \end{aligned} $$

$$ \begin{aligned} E(\theta_1, \theta_2) &= 0 + \cos\theta_1 \left(15\cos^2\frac{\theta_2}{2} + 5\sin^2\frac{\theta_2}{2}\right) \end{aligned} $$

---

## **Hasil Akhir $E(\theta_1)$ untuk Depth 2**

$$ E(\theta_1) = \left(15\cos^2\frac{\theta_2}{2} + 5\sin^2\frac{\theta_2}{2}\right) \cos\theta_1 $$

Ini berbentuk **$A \cos\theta_1$** dengan:
$$ A = 15\cos^2\frac{\theta_2}{2} + 5\sin^2\frac{\theta_2}{2} $$

---

## **Pembuktian Parameter-Shift Rule**

Karena $E(\theta_1) = A \cos\theta_1$, maka:

1.  **Gradien analitik:**
    $$ \frac{\partial E}{\partial \theta_1} = -A \sin\theta_1 $$

2.  **Evaluasi maju ($\theta_1 + \pi/2$):**
    $$ E\left(\theta_1 + \frac{\pi}{2}\right) = A \cos\left(\theta_1 + \frac{\pi}{2}\right) = -A \sin\theta_1 $$

3.  **Evaluasi mundur ($\theta_1 - \pi/2$):**
    $$ E\left(\theta_1 - \frac{\pi}{2}\right) = A \cos\left(\theta_1 - \frac{\pi}{2}\right) = A \sin\theta_1 $$

4.  **Parameter-shift rule:**
    $$ \frac{1}{2}\left[ E\left(\theta_1 + \frac{\pi}{2}\right) - E\left(\theta_1 - \frac{\pi}{2}\right) \right] = \frac{1}{2} \left[ -A \sin\theta_1 - A \sin\theta_1 \right] = -A \sin\theta_1 $$

    $$ = \frac{\partial E}{\partial \theta_1} \quad \text{(Terbukti!)} $$

---

## **Verifikasi Numerik**

Ambil contoh $\theta_1 = \pi/4$ dan $\theta_2 = \pi/3$:

$$ \theta_2/2 = \pi/6 $$
$$ \cos(\pi/6) = \sqrt{3}/2 \approx 0.8660 $$
$$ \sin(\pi/6) = 0.5 $$

$$ A = 15(0.8660)^2 + 5(0.5)^2 = 15(0.75) + 5(0.25) = 11.25 + 1.25 = 12.5 $$

**Gradien analitik:**
$$ \frac{\partial E}{\partial \theta_1} = -12.5 \cdot \sin(\pi/4) = -12.5 \cdot 0.7071 = -8.8388 $$

**Parameter-shift:**
$$ E(\pi/4 + \pi/2) = E(3\pi/4) = 12.5 \cos(3\pi/4) = 12.5 \cdot (-0.7071) = -8.8388 $$
$$ E(\pi/4 - \pi/2) = E(-\pi/4) = 12.5 \cos(-\pi/4) = 12.5 \cdot 0.7071 = 8.8388 $$

$$ \frac{1}{2}[-8.8388 - 8.8388] = -8.8388 $$

**Sesuai!** ✓

---

## **Kesimpulan untuk Depth 2**

Meskipun kita menambahkan **CNOT** yang menciptakan entanglement, struktur sinusoidal $E(\theta_1)$ tetap terjaga karena CNOT adalah gerbang uniter yang **tidak bergantung pada $\theta_1$**. CNOT menjadi bagian dari $\hat{U}_B$ yang terserap ke dalam matriks $\hat{M} = \hat{U}_B^\dagger \hat{H} \hat{U}_B$, sehingga tidak mengubah sifat fundamental: **setiap parameter rotasi tunggal menghasilkan respons sinusoidal**.

Prinsip ini akan terus berlanjut untuk depth 3, 4, 5, dan 6. Setiap penambahan gerbang non-parametrik (CNOT, Hadamard, dll.) akan berakhir di $\hat{U}_A$ atau $\hat{U}_B$, tetap menjaga validitas parameter-shift rule. 

Apakah Anda ingin saya lanjutkan ke depth 3? Di depth 3, gambar Anda menunjukkan rotasi $R_y$ lagi yang menambah parameter $\theta_3$ dan $\theta_4$. Kita bisa melihat interaksi dua parameter parametrik yang dipisahkan oleh CNOT.

---
---