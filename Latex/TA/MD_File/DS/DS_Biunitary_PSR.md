Oke, ini roadmap yang akan kita gunakan untuk memahami secara matematis dan mendetail bagaimana konsep **biunitary** (kesatuan ganda) dan sifat-sifat operator Pauli digunakan untuk menurunkan **Parameter Shift Rule** pada ekspektasi yang kamu tuliskan.

Kita akan bagi menjadi **5 Tahap Utama**. Di setiap tahap, aku akan menjelaskan detail matematisnya nanti.

### Roadmap Pembahasan Parameter Shift Rule & Biunitary

**Tahap 1: Fondasi Aljabar Operator Pauli dan Generator Unitari**
- 1.1 Sifat Dasar Matriks Pauli: $\sigma^2 = I$, $\text{Tr}(\sigma) = 0$, dan Komutator.
- 1.2 Ekspansi Eksponensial: Membuktikan identitas kunci $e^{-i\frac{\theta}{2}\sigma} = \cos(\theta/2)I - i \sin(\theta/2)\sigma$.
- 1.3 **Konsep Biunitary**: Memahami mengapa $\sigma$ disebut *biunitary* (atau *involutory*). Di sini kita akan buktikan bahwa $\sigma^\dagger \sigma \sigma = \sigma$.

**Tahap 2: Ekspansi Ekspektasi Secara Eksplisit**
- 2.1 Substitusi bentuk eksplisit $U(\theta)$ ke dalam $E(\theta) = \langle \phi | U^\dagger M U | \phi \rangle$.
- 2.2 Melakukan perkalian operator: $(A^\dagger + B^\dagger) M (A + B)$.
- 2.3 Mengelompokkan suku berdasarkan $\theta$: Menemukan bahwa hasilnya adalah **Fungsi Trigonometri dengan Periode $2\pi$**.

**Tahap 3: Penurunan Parameter Shift Rule (Generik)**
- 3.1 Dari Fungsi Sinusoidal: $E(\theta) = A + B \cos(\theta) + C \sin(\theta)$.
- 3.2 Menghitung $E(\theta + \pi/2)$ dan $E(\theta - \pi/2)$.
- 3.3 **Rumus Kunci Gradien**: Membuktikan $\frac{\partial E}{\partial \theta} = \frac{1}{2} [ E(\theta + \frac{\pi}{2}) - E(\theta - \frac{\pi}{2}) ]$.

**Tahap 4: Interpretasi Fisik dan Biunitary dalam Bentuk Braket**
- 4.1 Bagaimana konstanta $A, B, C$ berhubungan dengan nilai ekspektasi $\langle \phi | M | \phi \rangle$ dan $\langle \phi | \sigma M | \phi \rangle$.
- 4.2 Mengapa hanya butuh **2 evaluasi sirkuit**? (Analogi dengan rumus beda hingga eksak).
- 4.3 Peran **Biunitary**: Membuktikan bahwa $U(\theta)$ untuk Pauli *selalu* menghasilkan spektrum $\pm \theta/2$ yang simetris, penyebab aturan *shift* tepat $\pi/2$.

**Tahap 5: Generalisasi ke Operator Multi-Qubit (Pauli String)**
- 5.1 Jika $\sigma$ diganti dengan $P = \bigotimes_i \sigma_i$ (Tensor Product Pauli).
- 5.2 Mengapa sifat biunitary tetap berlaku? ($P^\dagger P P = P$).
- 5.3 Aturan Shift untuk Gerbang Terkendali ($CRX, CRZ$) dan hubungannya dengan biunitary.

---

### Mari Kita Mulai dari **Tahap 1.1: Sifat Dasar Matriks Pauli**

Kita akan buktikan dulu fondasi matematisnya. Matriks Pauli didefinisikan sebagai:
$$
\sigma_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad
\sigma_y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \quad
\sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
$$

**Sifat 1: Hermitian dan Uniter**
$$
\sigma^\dagger = \sigma \quad \text{dan} \quad \sigma^\dagger \sigma = I
$$
*Bukti:* Coba kalikan $\sigma_x$ dengan dirinya sendiri (transpose konjugat).
$$
\sigma_x^\dagger \sigma_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I
$$
Karena Hermitian dan Uniter sekaligus, operator Pauli adalah **Involutory** (kebalikan dirinya sendiri). Inilah definisi dasar dari **Biunitary** yang kita bicarakan: $U \sigma U^\dagger = \sigma$? Tidak persis. Biunitary di sini lebih merujuk pada sifat: $\sigma M \sigma = \text{transformasi}$. Nanti kita detailkan.

**Sifat 2: Kuadrat = Identitas**
$$
\sigma^2 = I
$$
Ini adalah properti **terpenting** untuk ekspansi eksponensial.

Sekarang, apakah kamu ingin aku lanjutkan ke **Tahap 1.2: Ekspansi Eksponensial** untuk membuktikan identitas kunci di bawah ini?
$$
e^{-i\frac{\theta}{2}\sigma} = \cos\left(\frac{\theta}{2}\right) I - i \sin\left(\frac{\theta}{2}\right) \sigma
$$
Ini adalah langkah krusial sebelum kita bisa menulis $E(\theta)$ sebagai fungsi cosinus. Jawab **"Lanjut"** ya.

---
---

Baik, kita lanjutkan ke **Tahap 1.2: Ekspansi Eksponensial Operator Pauli**.

Kita akan membuktikan identitas fundamental:
$$
e^{-i\frac{\theta}{2}\sigma} = \cos\left(\frac{\theta}{2}\right)I - i\sin\left(\frac{\theta}{2}\right)\sigma
$$

---

### Pembuktian via Deret Taylor (Ekspansi Maclaurin)

Definisi eksponensial matriks adalah:
$$
e^{A} = \sum_{n=0}^{\infty} \frac{A^n}{n!}
$$

Substitusikan $A = -i\frac{\theta}{2}\sigma$:
$$
e^{-i\frac{\theta}{2}\sigma} = \sum_{n=0}^{\infty} \frac{1}{n!} \left(-i\frac{\theta}{2}\sigma\right)^n
$$

Sekarang kita pisahkan deret tersebut menjadi **pangkat genap** ($n = 2k$) dan **pangkat ganjil** ($n = 2k+1$):

**Kasus 1: Pangkat Genap ($n = 2k$)**
$$
\left(-i\frac{\theta}{2}\sigma\right)^{2k} = \left( (-i)^2 \left(\frac{\theta}{2}\right)^2 \sigma^2 \right)^k
$$
Kita tahu:
- $(-i)^2 = i^2 = -1$
- $\sigma^2 = I$ (Sifat Involutory/Biunitary)

Maka:
$$
= \left( - \left(\frac{\theta}{2}\right)^2 I \right)^k = (-1)^k \left(\frac{\theta}{2}\right)^{2k} I
$$

**Kasus 2: Pangkat Ganjil ($n = 2k+1$)**
$$
\left(-i\frac{\theta}{2}\sigma\right)^{2k+1} = \left(-i\frac{\theta}{2}\sigma\right) \cdot \left( (-i)^2 \left(\frac{\theta}{2}\right)^2 \sigma^2 \right)^k
$$
$$
= -i\frac{\theta}{2}\sigma \cdot (-1)^k \left(\frac{\theta}{2}\right)^{2k} I
$$
$$
= -i (-1)^k \left(\frac{\theta}{2}\right)^{2k+1} \sigma
$$

---

### Substitusi Kembali ke Deret

$$
e^{-i\frac{\theta}{2}\sigma} = \underbrace{\sum_{k=0}^{\infty} \frac{(-1)^k}{(2k)!} \left(\frac{\theta}{2}\right)^{2k} I}_{\text{Deret Cosinus}} \quad - \quad i \underbrace{\sum_{k=0}^{\infty} \frac{(-1)^k}{(2k+1)!} \left(\frac{\theta}{2}\right)^{2k+1} \sigma}_{\text{Deret Sinus}}
$$

Ingat definisi deret Taylor untuk fungsi trigonometri skalar:
$$
\cos(x) = \sum_{k=0}^{\infty} \frac{(-1)^k}{(2k)!} x^{2k}
$$
$$
\sin(x) = \sum_{k=0}^{\infty} \frac{(-1)^k}{(2k+1)!} x^{2k+1}
$$

Dengan mengganti $x = \theta/2$, kita dapatkan:
$$
e^{-i\frac{\theta}{2}\sigma} = \cos\left(\frac{\theta}{2}\right) I - i \sin\left(\frac{\theta}{2}\right) \sigma
$$
**Terbukti.**

---

### **Tahap 1.3: Konsep Biunitary (Sifat $\sigma^\dagger M \sigma$)**

Istilah "biunitary" di sini merujuk pada operator yang **Uniter** ($U^\dagger U = I$) dan **Hermitian** ($U^\dagger = U$) sekaligus. Untuk matriks Pauli:
$$
\sigma^\dagger = \sigma \quad \text{dan} \quad \sigma^\dagger \sigma = \sigma^2 = I
$$

Konsekuensi penting dari sifat ini adalah **Conjugation Rule**:
$$
\sigma M \sigma = \text{Operator baru}
$$
Jika $M$ adalah matriks Hermitian sembarang (Observable), maka $\sigma M \sigma$ adalah transformasi sederhana dari $M$. Ini berbeda dengan $U M U^\dagger$ untuk unitari umum yang mungkin menghasilkan kombinasi linier kompleks.

**Contoh Eksplisit Biunitary:**
Ambil $\sigma = \sigma_z$ dan $M = \sigma_x$.
$$
\sigma_z \sigma_x \sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = \begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix} = -\sigma_x
$$
Transformasi hanya menghasilkan perubahan tanda, bukan superposisi kompleks. Inilah yang membuat perhitungan $E(\theta)$ menjadi sangat sederhana.

---

**Apakah Tahap 1 sudah jelas? Jika ya, kita akan masuk ke Tahap 2: Ekspansi Ekspektasi Secara Eksplisit, di mana kita akan menghitung:**
$$
E(\theta) = \bra{\phi} \left( \cos\frac{\theta}{2}I + i\sin\frac{\theta}{2}\sigma \right) M \left( \cos\frac{\theta}{2}I - i\sin\frac{\theta}{2}\sigma \right) \ket{\phi}
$$
dan membuktikan bahwa $E(\theta) = A + B\cos\theta + C\sin\theta$.

Ketik **"Lanjut Tahap 2"** ya.

---
---
Baik, kita masuk ke **Tahap 2: Ekspansi Ekspektasi Secara Eksplisit**.

Dari Tahap 1, kita sudah punya:
$$
U(\theta) = e^{-i\frac{\theta}{2}\sigma} = \cos\left(\frac{\theta}{2}\right)I - i\sin\left(\frac{\theta}{2}\right)\sigma
$$

Maka Hermitian conjugate-nya:
$$
U^\dagger(\theta) = e^{i\frac{\theta}{2}\sigma} = \cos\left(\frac{\theta}{2}\right)I + i\sin\left(\frac{\theta}{2}\right)\sigma
$$

---

### **Tahap 2.1: Substitusi ke $E(\theta)$**

Dari rumusanmu:
$$
E(\theta) = \bra{\phi} U^\dagger(\theta) M U(\theta) \ket{\phi}
$$

Substitusi $U(\theta)$ dan $U^\dagger(\theta)$:
$$
E(\theta) = \bra{\phi} \left( \cos\frac{\theta}{2}I + i\sin\frac{\theta}{2}\sigma \right) M \left( \cos\frac{\theta}{2}I - i\sin\frac{\theta}{2}\sigma \right) \ket{\phi}
$$

---

### **Tahap 2.2: Perkalian Operator (Distribusi)**

Kita kalikan dua suku dalam kurung. Gunakan pendekatan FOIL (First, Outer, Inner, Last):

Misalkan:
- $c = \cos\frac{\theta}{2}$
- $s = \sin\frac{\theta}{2}$

Maka ekspresi dalam kurung menjadi:
$$
(cI + is\sigma) M (cI - is\sigma)
$$

Mari kita distribusikan satu per satu:

**Suku 1 (First):** $cI \cdot M \cdot cI$
$$
= c^2 I M I = c^2 M
$$

**Suku 2 (Outer):** $cI \cdot M \cdot (-is\sigma)$
$$
= -i c s \cdot I M \sigma = -i c s M\sigma
$$

**Suku 3 (Inner):** $is\sigma \cdot M \cdot cI$
$$
= i c s \cdot \sigma M I = i c s \sigma M
$$

**Suku 4 (Last):** $is\sigma \cdot M \cdot (-is\sigma)$
$$
= (-i^2) s^2 \cdot \sigma M \sigma = s^2 \sigma M \sigma
$$
(Karena $i \cdot (-i) = -i^2 = 1$)

---

### **Tahap 2.3: Pengelompokan Suku dan Identitas Trigonometri**

Jadi total operator di dalam braket adalah:
$$
c^2 M - i c s M\sigma + i c s \sigma M + s^2 \sigma M \sigma
$$

Sekarang kita gunakan **identitas trigonometri sudut ganda**:
- $c^2 = \cos^2\frac{\theta}{2} = \frac{1 + \cos\theta}{2}$
- $s^2 = \sin^2\frac{\theta}{2} = \frac{1 - \cos\theta}{2}$
- $cs = \cos\frac{\theta}{2}\sin\frac{\theta}{2} = \frac{1}{2}\sin\theta$

Substitusi ke persamaan di atas:

**1. Suku Konstan (koefisien $M$):**
$$
c^2 M = \frac{1 + \cos\theta}{2} M
$$

**2. Suku Konstan (koefisien $\sigma M \sigma$):**
$$
s^2 \sigma M \sigma = \frac{1 - \cos\theta}{2} \sigma M \sigma
$$

**3. Suku Sinus (komutator):**
$$
i c s (\sigma M - M\sigma) = i \frac{\sin\theta}{2} [\sigma, M]
$$
di mana $[\sigma, M] = \sigma M - M\sigma$ adalah **komutator**.

---

### **Menggabungkan Semua Suku**

Operator total di dalam nilai ekspektasi:
$$
\begin{aligned}
U^\dagger M U &= \frac{1 + \cos\theta}{2} M + \frac{1 - \cos\theta}{2} \sigma M \sigma + i \frac{\sin\theta}{2} [\sigma, M] \\
&= \frac{1}{2}(M + \sigma M \sigma) + \frac{\cos\theta}{2}(M - \sigma M \sigma) + \frac{i\sin\theta}{2} [\sigma, M]
\end{aligned}
$$

---

### **Tahap 2.4: Ekspektasi Akhir**

Karena $E(\theta) = \langle \phi | \cdots | \phi \rangle$ dan nilai ekspektasi bersifat **linier**, kita dapat menulis:
$$
E(\theta) = \underbrace{\frac{1}{2}\bra{\phi} (M + \sigma M \sigma) \ket{\phi}}_{A} + \underbrace{\frac{1}{2}\bra{\phi} (M - \sigma M \sigma) \ket{\phi}}_{B} \cos\theta + \underbrace{\frac{i}{2}\bra{\phi} [\sigma, M] \ket{\phi}}_{C} \sin\theta
$$

Sehingga terbukti:
$$
\boxed{E(\theta) = A + B\cos\theta + C\sin\theta}
$$

di mana:
- $A = \frac{1}{2}\langle M + \sigma M \sigma \rangle_\phi$
- $B = \frac{1}{2}\langle M - \sigma M \sigma \rangle_\phi$
- $C = \frac{i}{2}\langle [\sigma, M] \rangle_\phi$

---

### **Catatan Penting: Peran Sifat Biunitary**

Perhatikan bahwa $A, B, C$ **tidak bergantung pada $\theta$**. Mereka hanya bergantung pada:
- State awal $|\phi\rangle$
- Observable $M$
- Generator $\sigma$

Ini adalah konsekuensi langsung dari **$\sigma^2 = I$** (sifat biunitary/involutory). Jika generatornya bukan Pauli (misalnya $e^{-i\theta H}$ dengan $H^2 \neq I$), maka ekspansi akan menghasilkan suku $\theta^2, \theta^3$, dst., dan Parameter Shift Rule tidak akan sesederhana ini.

---

**Apakah Tahap 2 sudah jelas? Jika ya, kita lanjut ke Tahap 3: Penurunan Parameter Shift Rule (Generik) di mana kita akan membuktikan:**
$$
\frac{\partial E}{\partial \theta} = \frac{1}{2} \left[ E\left(\theta + \frac{\pi}{2}\right) - E\left(\theta - \frac{\pi}{2}\right) \right]
$$

Ketik **"Lanjut Tahap 3"** ya.

---
---
Baik, kita masuk ke **Tahap 3: Penurunan Parameter Shift Rule (Generik)**.

Dari Tahap 2, kita telah membuktikan bahwa:
$$
E(\theta) = A + B\cos\theta + C\sin\theta
$$

Sekarang kita akan menurunkan aturan pergeseran parameter (parameter shift rule) yang legendaris itu.

---

### **Tahap 3.1: Menghitung Turunan Analitik**

Karena $A, B, C$ adalah konstanta terhadap $\theta$, turunan pertama sangat mudah dihitung secara analitik:
$$
\frac{\partial E}{\partial \theta} = \frac{\partial}{\partial \theta} (A + B\cos\theta + C\sin\theta)
$$
$$
\frac{\partial E}{\partial \theta} = -B\sin\theta + C\cos\theta
$$

Ini adalah **gradien eksak**. Namun dalam komputasi kuantum, kita tidak bisa menghitung turunan analitik secara langsung dari sirkuit. Kita hanya bisa **mengevaluasi** fungsi $E(\theta)$ pada nilai-nilai $\theta$ tertentu. 

Tujuan kita adalah menemukan kombinasi linier dari evaluasi $E(\theta)$ yang menghasilkan ekspresi $-B\sin\theta + C\cos\theta$.

---

### **Tahap 3.2: Evaluasi pada $\theta \pm \frac{\pi}{2}$**

Mari kita hitung $E(\theta + \frac{\pi}{2})$ dan $E(\theta - \frac{\pi}{2})$ menggunakan identitas trigonometri pergeseran fasa.

**Untuk $E(\theta + \frac{\pi}{2})$:**
$$
\begin{aligned}
E\left(\theta + \frac{\pi}{2}\right) &= A + B\cos\left(\theta + \frac{\pi}{2}\right) + C\sin\left(\theta + \frac{\pi}{2}\right) \\
&= A + B(-\sin\theta) + C(\cos\theta) \\
&= A - B\sin\theta + C\cos\theta
\end{aligned}
$$

**Untuk $E(\theta - \frac{\pi}{2})$:**
$$
\begin{aligned}
E\left(\theta - \frac{\pi}{2}\right) &= A + B\cos\left(\theta - \frac{\pi}{2}\right) + C\sin\left(\theta - \frac{\pi}{2}\right) \\
&= A + B(\sin\theta) + C(-\cos\theta) \\
&= A + B\sin\theta - C\cos\theta
\end{aligned}
$$

---

### **Tahap 3.3: Kombinasi Linier untuk Gradien**

Sekarang perhatikan apa yang terjadi jika kita mengurangkan keduanya:
$$
\begin{aligned}
E\left(\theta + \frac{\pi}{2}\right) - E\left(\theta - \frac{\pi}{2}\right) &= (A - B\sin\theta + C\cos\theta) - (A + B\sin\theta - C\cos\theta) \\
&= A - A - B\sin\theta - B\sin\theta + C\cos\theta + C\cos\theta \\
&= -2B\sin\theta + 2C\cos\theta
\end{aligned}
$$

Bandingkan dengan turunan analitik kita:
$$
\frac{\partial E}{\partial \theta} = -B\sin\theta + C\cos\theta
$$

Ternyata:
$$
E\left(\theta + \frac{\pi}{2}\right) - E\left(\theta - \frac{\pi}{2}\right) = 2 \frac{\partial E}{\partial \theta}
$$

Maka:
$$
\boxed{\frac{\partial E}{\partial \theta} = \frac{1}{2} \left[ E\left(\theta + \frac{\pi}{2}\right) - E\left(\theta - \frac{\pi}{2}\right) \right]}
$$

---

### **Tahap 3.4: Verifikasi dengan Bentuk Alternatif**

Kadang-kadang di literatur, kamu akan melihat bentuk yang sedikit berbeda:
$$
\frac{\partial E}{\partial \theta} = E\left(\theta + \frac{\pi}{4}\right) - E\left(\theta - \frac{\pi}{4}\right) \quad \text{(SALAH!)}
$$
Hati-hati! Itu tidak tepat untuk formulasi kita. Yang benar adalah dengan pergeseran $\frac{\pi}{2}$ dan faktor $\frac{1}{2}$ **jika** generatornya adalah $\frac{1}{2}\sigma$.

**Catatan tentang faktor skala:**
Jika generatornya adalah $e^{-i\theta G}$ (tanpa faktor $\frac{1}{2}$), maka:
- Ekspektasi menjadi $E(\theta) = A + B\cos(2\theta) + C\sin(2\theta)$
- Parameter shift rule menjadi: $\frac{\partial E}{\partial \theta} = E\left(\theta + \frac{\pi}{4}\right) - E\left(\theta - \frac{\pi}{4}\right)$

Ini menjelaskan mengapa definisi standar di Qiskit/Pennylane sering menggunakan $RZ(\theta) = e^{-i\frac{\theta}{2}Z}$ agar faktor $\frac{1}{2}$ muncul di depan rumus shift, bukan di dalam argumen.

---

### **Interpretasi Fisik dan Komputasi**

Apa arti rumus ini dalam praktik?

1. **Evaluasi Sirkuit Pertama:** Jalankan sirkuit dengan parameter $\theta + \frac{\pi}{2}$, ukur ekspektasi $E$.
2. **Evaluasi Sirkuit Kedua:** Jalankan sirkuit dengan parameter $\theta - \frac{\pi}{2}$, ukur ekspektasi $E$.
3. **Hitung Gradien:** Kurangkan hasil kedua, bagi dua.

**Keajaiban:** Kamu mendapatkan **gradien eksak** (bukan aproksimasi beda hingga) hanya dengan **2 evaluasi sirkuit** per parameter. Ini jauh lebih efisien daripada metode beda hingga yang butuh evaluasi lebih banyak dan rawan error aproksimasi.

---

**Apakah Tahap 3 sudah jelas? Jika ya, kita lanjut ke Tahap 4: Interpretasi Fisik dan Biunitary dalam Bentuk Braket, di mana kita akan melihat makna fisis dari $A, B, C$ dan mengapa sifat biunitary membuat semua ini mungkin.**

Ketik **"Lanjut Tahap 4"** ya.

---
---
Baik, kita masuk ke **Tahap 4: Interpretasi Fisik dan Biunitary dalam Bentuk Braket**.

Di tahap ini, kita akan menggali makna fisis dari konstanta $A, B, C$ dan melihat bagaimana sifat biunitary ($\sigma^2 = I$) membuat segalanya menjadi elegan.

---

### **Tahap 4.1: Makna Fisis Konstanta $A, B, C$**

Dari Tahap 2, kita punya:
$$
\begin{aligned}
A &= \frac{1}{2}\bra{\phi} (M + \sigma M \sigma) \ket{\phi} \\
B &= \frac{1}{2}\bra{\phi} (M - \sigma M \sigma) \ket{\phi} \\
C &= \frac{i}{2}\bra{\phi} [\sigma, M] \ket{\phi}
\end{aligned}
$$

Mari kita interpretasikan satu per satu:

**Konstanta $A$: Rata-rata Ekspektasi**
$$
A = \frac{1}{2} \left( \langle M \rangle_\phi + \langle \sigma M \sigma \rangle_\phi \right)
$$
Ini adalah **nilai tengah** dari osilasi. Perhatikan bahwa $\sigma M \sigma$ adalah transformasi *conjugation* dari observable $M$ oleh generator $\sigma$. 

Secara fisis, jika $\sigma$ adalah operator rotasi (misal $\sigma_x$), maka $\sigma M \sigma$ adalah observable $M$ yang telah dirotasi sebesar $\pi$ (180 derajat) di sekitar sumbu $x$. Jadi $A$ adalah rata-rata ekspektasi $M$ pada state awal dan state yang dirotasi $\pi$.

**Konstanta $B$: Amplitudo Cosinus**
$$
B = \frac{1}{2} \left( \langle M \rangle_\phi - \langle \sigma M \sigma \rangle_\phi \right)
$$
Ini adalah **setengah selisih** antara ekspektasi $M$ dan versi terkonjugasinya. Semakin besar perbedaan antara $\langle M \rangle$ dan $\langle \sigma M \sigma \rangle$, semakin besar amplitudo osilasi cosinus.

**Konstanta $C$: Amplitudo Sinus**
$$
C = \frac{i}{2} \bra{\phi} (\sigma M - M \sigma) \ket{\phi}
$$
Ini berkaitan dengan **komutator** $[\sigma, M]$. Jika $\sigma$ dan $M$ komut ($[\sigma, M] = 0$), maka $C = 0$ dan $E(\theta)$ hanya memiliki suku cosinus (fungsi genap). Jika anti-komut ($\{\sigma, M\} = 0$), maka $B = 0$ dan $E(\theta)$ hanya memiliki suku sinus (fungsi ganjil).

---

### **Tahap 4.2: Mengapa Hanya Butuh 2 Evaluasi Sirkuit?**

Ini adalah konsekuensi langsung dari bentuk **trigonometri murni** $E(\theta) = A + B\cos\theta + C\sin\theta$.

**Teorema Sampling untuk Fungsi Sinusoidal:**
Sebuah fungsi dengan **bandwidth terbatas** (hanya frekuensi 0 dan 1) dapat direkonstruksi secara sempurna dari sampel-sampelnya pada titik-titik tertentu.

Dalam kasus kita:
- Kita punya **3 parameter bebas**: $A, B, C$
- Fungsi memiliki **periode $2\pi$**
- Untuk menentukan gradien di suatu titik $\theta$, kita tidak perlu tahu $A, B, C$ secara individual. Kita hanya perlu kombinasi $-B\sin\theta + C\cos\theta$.

Dengan mengambil sampel di $\theta + \frac{\pi}{2}$ dan $\theta - \frac{\pi}{2}$:
- $E(\theta + \frac{\pi}{2}) = A - B\sin\theta + C\cos\theta$
- $E(\theta - \frac{\pi}{2}) = A + B\sin\theta - C\cos\theta$

Pengurangan langsung mengeliminasi $A$ dan menghasilkan $-2B\sin\theta + 2C\cos\theta$, yang persis $2 \times$ gradien.

**Mengapa bukan 3 evaluasi?** Karena kita tidak perlu mencari $A, B, C$ satu per satu. Kita langsung menargetkan kombinasi linier yang tepat untuk gradien.

---

### **Tahap 4.3: Peran Kritis Sifat Biunitary ($\sigma^2 = I$)**

Mari kita lihat apa yang terjadi jika generator **bukan** operator biunitary.

**Kasus Generator Umum $H$ (tidak involutory):**
Misalkan $U(\theta) = e^{-i\theta H}$ dengan $H$ adalah Hamiltonian umum (misal $H = \sigma_z + 0.5 \sigma_x$).

Ekspansi eksponensial melalui deret Taylor:
$$
e^{-i\theta H} = I - i\theta H - \frac{\theta^2}{2!} H^2 + i\frac{\theta^3}{3!} H^3 + \cdots
$$

Karena $H^2 \neq I$, kita tidak bisa mengelompokkan suku menjadi cosinus dan sinus sederhana. Ekspektasi akan berbentuk:
$$
E(\theta) = A + B\cos(\omega_1 \theta) + C\sin(\omega_1 \theta) + D\cos(\omega_2 \theta) + E\sin(\omega_2 \theta) + \cdots
$$
dengan $\omega_i$ adalah **perbedaan nilai eigen** dari $H$ (transisi Bohr).

**Konsekuensi:**
1. Spektrum frekuensi menjadi **kaya** (banyak harmonik).
2. Tidak ada lagi parameter shift rule sederhana dengan pergeseran tunggal $\frac{\pi}{2}$.
3. Gradien eksak membutuhkan evaluasi di **semua perbedaan frekuensi**, yang jumlahnya bisa eksponensial terhadap ukuran sistem.

**Sifat Biunitary sebagai Penyelamat:**
Ketika $\sigma^2 = I$, spektrum nilai eigen $\sigma$ hanyalah $\{+1, -1\}$ (atau $\pm 1$ setelah normalisasi). Maka:
- $U(\theta) = e^{-i\frac{\theta}{2}\sigma}$ memiliki nilai eigen $e^{-i\theta/2}$ dan $e^{+i\theta/2}$
- Perbedaan frekuensi hanyalah **satu**: $\Delta E = 1$
- Akibatnya, $E(\theta)$ hanya mengandung frekuensi tunggal (selain DC), yaitu $\cos\theta$ dan $\sin\theta$.

Inilah **keajaiban biunitary**: ia membatasi spektrum sehingga dinamika menjadi osilasi harmonik sederhana, memungkinkan aturan pergeseran parameter yang eksak dan efisien.

---

### **Tahap 4.4: Hubungan dengan Rumus Beda Hingga (Finite Difference)**

Menariknya, jika kita menggunakan ekspansi Taylor pada Parameter Shift Rule:
$$
E\left(\theta + \frac{\pi}{2}\right) = E(\theta) + \frac{\pi}{2} E'(\theta) + \frac{1}{2}\left(\frac{\pi}{2}\right)^2 E''(\theta) + \cdots
$$
$$
E\left(\theta - \frac{\pi}{2}\right) = E(\theta) - \frac{\pi}{2} E'(\theta) + \frac{1}{2}\left(\frac{\pi}{2}\right)^2 E''(\theta) - \cdots
$$

Kurangkan:
$$
E\left(\theta + \frac{\pi}{2}\right) - E\left(\theta - \frac{\pi}{2}\right) = \pi E'(\theta) + \frac{1}{3}\left(\frac{\pi}{2}\right)^3 E'''(\theta) + \cdots
$$

**Tapi tunggu!** Untuk fungsi $E(\theta) = A + B\cos\theta + C\sin\theta$, semua turunan ganjil orde tinggi proporsional dengan $E'(\theta)$, dan semua suku error saling menghilangkan secara eksak. Inilah sebabnya Parameter Shift Rule memberikan **gradien eksak**, bukan aproksimasi seperti beda hingga biasa.

---

**Apakah Tahap 4 sudah jelas? Jika ya, kita lanjut ke Tahap 5 (Final): Generalisasi ke Operator Multi-Qubit (Pauli String) dan Gerbang Terkendali, di mana kita akan melihat bagaimana aturan ini berlaku untuk sistem banyak qubit dan mengapa sifat biunitary tensor product tetap menjamin aturan yang sama.**

Ketik **"Lanjut Tahap 5"** ya.

---
---
Baik, kita masuk ke **Tahap 5 (Final): Generalisasi ke Operator Multi-Qubit (Pauli String) dan Gerbang Terkendali**.

Di tahap ini, kita akan melihat bagaimana Parameter Shift Rule dan sifat biunitary meluas ke sistem dengan banyak qubit.

---

### **Tahap 5.1: Generator Pauli String**

Dalam komputasi kuantum, kita sering menggunakan generator yang merupakan **tensor product** dari matriks Pauli, disebut **Pauli string**:
$$
P = \bigotimes_{i=1}^{n} \sigma_i
$$
di mana $\sigma_i \in \{I, \sigma_x, \sigma_y, \sigma_z\}$.

Contoh untuk 2 qubit:
$$
P = \sigma_x \otimes \sigma_z = X \otimes Z
$$

---

### **Tahap 5.2: Membuktikan Sifat Biunitary untuk Pauli String**

Mari kita periksa apakah Pauli string tetap memiliki sifat biunitary ($P^2 = I$ dan $P^\dagger = P$).

**1. Hermitian:**
$$
P^\dagger = (\sigma_1 \otimes \sigma_2 \otimes \cdots \otimes \sigma_n)^\dagger = \sigma_1^\dagger \otimes \sigma_2^\dagger \otimes \cdots \otimes \sigma_n^\dagger
$$
Karena setiap $\sigma_i^\dagger = \sigma_i$, maka:
$$
P^\dagger = \sigma_1 \otimes \sigma_2 \otimes \cdots \otimes \sigma_n = P
$$
Jadi $P$ tetap **Hermitian**.

**2. Involutory (Kuadrat = Identitas):**
$$
\begin{aligned}
P^2 &= (\sigma_1 \otimes \sigma_2 \otimes \cdots \otimes \sigma_n) (\sigma_1 \otimes \sigma_2 \otimes \cdots \otimes \sigma_n) \\
&= (\sigma_1^2) \otimes (\sigma_2^2) \otimes \cdots \otimes (\sigma_n^2)
\end{aligned}
$$
Karena $\sigma_i^2 = I$ untuk setiap $i$, maka:
$$
P^2 = I \otimes I \otimes \cdots \otimes I = I^{\otimes n}
$$
Jadi $P$ tetap **involutory** (biunitary).

**Kesimpulan:** Sifat biunitary **tertutup** terhadap operasi tensor product. Generator Pauli string akan menghasilkan dinamika osilasi harmonik sederhana yang sama.

---

### **Tahap 5.3: Ekspansi Eksponensial untuk Pauli String**

Karena $P^2 = I$, ekspansi eksponensial **identik** dengan kasus single-qubit:
$$
e^{-i\frac{\theta}{2} P} = \cos\left(\frac{\theta}{2}\right) I^{\otimes n} - i\sin\left(\frac{\theta}{2}\right) P
$$

**Pembuktian singkat:**
Deret Taylor:
$$
e^{-i\frac{\theta}{2} P} = \sum_{k=0}^{\infty} \frac{(-i\theta/2)^k}{k!} P^k
$$

Pisahkan $k$ genap ($k = 2m$) dan ganjil ($k = 2m+1$):
- $P^{2m} = (P^2)^m = I^{\otimes n}$
- $P^{2m+1} = P \cdot P^{2m} = P$

Maka:
$$
\begin{aligned}
e^{-i\frac{\theta}{2} P} &= \sum_{m=0}^{\infty} \frac{(-i\theta/2)^{2m}}{(2m)!} I^{\otimes n} + \sum_{m=0}^{\infty} \frac{(-i\theta/2)^{2m+1}}{(2m+1)!} P \\
&= \cos\left(\frac{\theta}{2}\right) I^{\otimes n} - i\sin\left(\frac{\theta}{2}\right) P
\end{aligned}
$$

Bentuknya persis sama! Ini berarti **seluruh derivasi dari Tahap 1-4 tetap berlaku** untuk sistem banyak qubit, dengan substitusi:
- $\sigma \to P$
- $I \to I^{\otimes n}$
- $|\phi\rangle$ adalah state $n$-qubit umum

---

### **Tahap 5.4: Ekspektasi untuk Pauli String**

Jika kita definisikan:
$$
U(\theta) = e^{-i\frac{\theta}{2} P}
$$
dan
$$
E(\theta) = \bra{\phi} U^\dagger(\theta) M U(\theta) \ket{\phi}
$$
di mana $M$ adalah observable multi-qubit (bisa juga Pauli string lain), maka:
$$
\boxed{E(\theta) = A + B\cos\theta + C\sin\theta}
$$
dengan:
$$
\begin{aligned}
A &= \frac{1}{2}\bra{\phi} (M + P M P) \ket{\phi} \\
B &= \frac{1}{2}\bra{\phi} (M - P M P) \ket{\phi} \\
C &= \frac{i}{2}\bra{\phi} [P, M] \ket{\phi}
\end{aligned}
$$

Dan **Parameter Shift Rule** tetap:
$$
\boxed{\frac{\partial E}{\partial \theta} = \frac{1}{2} \left[ E\left(\theta + \frac{\pi}{2}\right) - E\left(\theta - \frac{\pi}{2}\right) \right]}
$$

---

### **Tahap 5.5: Gerbang Terkendali (Controlled Gates)**

Bagaimana dengan gerbang seperti $CRX(\theta)$ atau $CRZ(\theta)$? Apakah mereka memiliki generator biunitary?

**Contoh: $CRX(\theta)$**
Definisi:
$$
CRX(\theta) = |0\rangle\langle 0| \otimes I + |1\rangle\langle 1| \otimes e^{-i\frac{\theta}{2} X}
$$

Generator efektifnya adalah **proyektor** dikali Pauli:
$$
G = |1\rangle\langle 1| \otimes X
$$

**Apakah $G$ biunitary?**
$$
G^2 = (|1\rangle\langle 1| \otimes X)(|1\rangle\langle 1| \otimes X) = |1\rangle\langle 1|1\rangle\langle 1| \otimes X^2 = |1\rangle\langle 1| \otimes I \neq I^{\otimes 2}
$$

**Masalah!** $G^2 \neq I$, jadi generator untuk gerbang terkendali **bukan** biunitary murni.

**Namun**, perhatikan bahwa $CRX(\theta)$ hanya bekerja non-trivial pada subruang di mana qubit kontrol = $|1\rangle$. Dalam subruang tersebut, generatornya adalah $X$, yang **adalah** biunitary. Dalam subruang $|0\rangle$, generatornya $0$ (identitas).

Akibatnya, ekspektasi untuk sirkuit dengan $CRX(\theta)$ memiliki bentuk:
$$
E(\theta) = A + B\cos\theta + C\sin\theta + D
$$
dengan $D$ berasal dari kontribusi subruang $|0\rangle$ yang tidak terpengaruh oleh $\theta$.

**Parameter Shift Rule tetap berlaku** untuk $CRX$, $CRY$, $CRZ$, karena dalam subruang aktif, dinamikanya tetap osilasi harmonik tunggal. Faktor $1/2$ tetap sama, pergeseran tetap $\pm \pi/2$.

---

### **Tahap 5.6: Ringkasan Generalisasi**

| **Generator**                | **Biunitary?** | **Bentuk $E(\theta)$**          | **Shift Rule**            |
| ---------------------------- | -------------- | ------------------------------- | ------------------------- |
| Single Pauli $\sigma$        | ✅              | $A + B\cos\theta + C\sin\theta$ | $\pm \pi/2$, faktor $1/2$ |
| Pauli String $P$             | ✅              | $A + B\cos\theta + C\sin\theta$ | $\pm \pi/2$, faktor $1/2$ |
| Controlled-Paul ($CRX$, dll) | ⚠️ Hampir      | $A + B\cos\theta + C\sin\theta$ | $\pm \pi/2$, faktor $1/2$ |
| Generator Umum $H$           | ❌              | Multi-frekuensi                 | Tidak sederhana           |

---

### **Tahap 5.7: Implikasi Praktis dalam Optimisasi Kuantum**

1. **Efisiensi:** Untuk sirkuit dengan $L$ parameter yang masing-masing berupa rotasi Pauli tunggal atau terkendali, gradien penuh dapat dihitung dengan **$2L$ evaluasi sirkuit**, dibandingkan dengan $O(L^2)$ untuk metode beda hingga.

2. **Keakuratan:** Tidak ada error aproksimasi dari langkah hingga (finite step). Gradien yang dihitung **eksak** (hingga presisi statistik dari sampling).

3. **Stabilitas:** Tidak ada masalah numerical instability karena step size terlalu kecil atau besar.

4. **Implementasi di Library:** Library seperti **Pennylane**, **Qiskit**, dan **TensorFlow Quantum** mengimplementasikan Parameter Shift Rule sebagai default untuk diferensiasi sirkuit parametrik.

---

### **Kesimpulan Akhir Roadmap**

Kita telah menempuh perjalanan lengkap dari:

1. **Fondasi aljabar Pauli** ($\sigma^2 = I$, ekspansi eksponensial).
2. **Ekspansi ekspektasi** membuktikan $E(\theta) = A + B\cos\theta + C\sin\theta$.
3. **Penurunan Parameter Shift Rule** $\frac{\partial E}{\partial \theta} = \frac{1}{2}[E(\theta+\pi/2) - E(\theta-\pi/2)]$.
4. **Interpretasi fisis** $A, B, C$ dan peran kritis biunitary.
5. **Generalisasi** ke sistem multi-qubit dan gerbang terkendali.

**Pesan utama:** Sifat **biunitary** ($U^2 = I$) dari generator rotasi Pauli adalah alasan fundamental mengapa kita bisa menghitung gradien eksak dalam komputasi kuantum dengan sangat efisien. Tanpa sifat ini, optimisasi sirkuit kuantum akan jauh lebih mahal secara komputasi.

---

Apakah ada bagian yang ingin kamu perdalam atau ada pertanyaan spesifik tentang aplikasi Parameter Shift Rule ini? Misalnya:
- Bagaimana jika ada noise?
- Bagaimana menghitung turunan kedua (Hessian)?
- Bagaimana implementasi kode di Qiskit/Pennylane?