Tentu, mari kita susun roadmap yang sistematis dan mendetail untuk mempelajari dekomposisi dalam komputasi kuantum.

Konsep dekomposisi adalah fondasi yang sangat krusial. Dalam komputasi kuantum, kita seringkali perlu memecah sebuah operator (seperti gerbang logika, Hamiltonian, atau state) menjadi bagian-bagian yang lebih sederhana, atau mengubahnya ke dalam basis representasi yang mengungkapkan sifat-sifat pentingnya. Tujuan akhir dari dekomposisi ini seringkali adalah untuk implementasi di perangkat keras kuantum riil, di mana kita hanya memiliki sekumpulan gerbang universal yang terbatas.

Roadmap ini disusun dari konsep matematika fundamental menuju teknik dekomposisi tingkat lanjut.

---

### Roadmap Belajar Dekomposisi Kuantum

Kita akan membagi perjalanan ini menjadi 6 tahap utama:

1.  **Fondasi Matematika:** Menguasai alat-alat aljabar linear yang menjadi bahasa dekomposisi.
2.  **Dekomposisi Spektral (Spectral Decomposition):** Memahami "DNA" dari operator normal.
3.  **Dekomposisi Nilai Singular (Singular Value Decomposition):** Alat serbaguna untuk operator non-normal dan korelasi kuantum.
4.  **Dekomposisi Operator Uniter:** Memecah aksi uniter menjadi komponen rotasi dasar.
5.  **Dekomposisi Gerbang Kuantum Universal:** Aplikasi praktis untuk sintesis sirkuit.
6.  **Dekomposisi Tingkat Lanjut:** Teknik spesifik dan esoteris dalam teori informasi kuantum.

Kita akan membahas setiap poin secara mendetail. Saya akan memberikan penjelasan matematis yang lengkap untuk setiap dekomposisi yang disebutkan.

---

### Tahap 1: Fondasi Matematika Aljabar Linear

Sebelum memulai dekomposisi, kita harus memastikan pemahaman yang solid tentang konsep-konsep ini:

- **Ruang Vektor Kompleks (Hilbert Space $\mathcal{H}$):** Notasi Bra-ket Dirac ( $| \psi \rangle, \langle \phi |$ ), produk dalam, norma, ortogonalitas, dan basis ortonormal.
- **Operator Linear:** Representasi matriks dalam basis, operator adjoint ($A^\dagger$), operator Hermitian ($H = H^\dagger$), operator Uniter ($U^\dagger U = UU^\dagger = I$), operator Positif ($\langle \psi | P | \psi \rangle \ge 0$).
- **Operator Normal:** Syarat $A A^\dagger = A^\dagger A$. Kelas ini sangat penting karena mencakup operator Hermitian dan Uniter, dan merupakan syarat perlu dan cukup untuk dekomposisi spektral melalui teorema spektral.
- **Nilai Eigen dan Vektor Eigen:** $A | v_i \rangle = \lambda_i | v_i \rangle$. Vektor eigen dari operator normal dengan nilai eigen berbeda bersifat ortogonal.

---

### Tahap 2: Dekomposisi Spektral

Ini adalah dekomposisi paling fundamental dalam mekanika kuantum.

#### Teorema Spektral (untuk Operator Normal)
Setiap operator normal $A$ pada ruang Hilbert berdimensi hingga dapat didiagonalisasi oleh basis ortonormal dari vektor eigennya. Dekomposisinya adalah:

$$A = \sum_{i} \lambda_i | i \rangle \langle i |$$

di mana $| i \rangle$ adalah vektor eigen ortonormal dari $A$ dan $\lambda_i$ adalah nilai eigen yang bersesuaian.

**Detail Matematis:**
1.  **Proyektor Spektral:** Matriks $P_i = | i \rangle \langle i |$ adalah proyektor ke subruang eigen ke-$i$. Proyektor ini memenuhi:
    - Hermitian: $P_i^\dagger = (| i \rangle \langle i |)^\dagger = | i \rangle \langle i | = P_i$
    - Ortonormal: $P_i P_j = | i \rangle \langle i | j \rangle \langle j | = \delta_{ij} P_i$
    - Komplit: $\sum_i P_i = \sum_i | i \rangle \langle i | = I$ (Relasi ketertutupan/resolusi identitas)
2.  **Dekomposisi untuk Kasus Degenerasi:** Jika nilai eigen $\lambda$ memiliki multiplisitas $d_\lambda$, kita jumlahkan proyektor ke semua vektor eigen dalam subruang eigen tersebut: $A = \sum_{\lambda} \lambda P_\lambda$, di mana $P_\lambda = \sum_{i \text{ with } \lambda_i = \lambda} | i \rangle \langle i |$.

**Representasi untuk Kelas Operator Penting:**
- **Operator Hermitian ($H$):** Semua nilai eigen $\lambda_i$ adalah **riil**. Ini adalah observable dalam mekanika kuantum. $H = \sum_i \lambda_i | i \rangle \langle i |$.
- **Operator Uniter ($U$):** Semua nilai eigen $\lambda_i$ adalah **fase kompleks**: $\lambda_i = e^{i\theta_i}$ dengan $\theta_i \in \mathbb{R}$. $U = \sum_i e^{i\theta_i} | i \rangle \langle i |$.
- **Operator Densitas ($\rho$):** Operator Hermitian positif dengan trace 1. Semua nilai eigen $p_i$ adalah **riil dan non-negatif** serta $\sum_i p_i = 1$. $\rho = \sum_i p_i | i \rangle \langle i |$. Ini merepresentasikan ensemble statistik dari state murni $| i \rangle$ dengan probabilitas $p_i$.

---

### Tahap 3: Dekomposisi Nilai Singular

SVD adalah dekomposisi yang berlaku untuk **setiap** operator, bahkan yang tidak normal atau non-persegi. Ini adalah alat yang tak ternilai untuk mempelajari keterjeratan (entanglement).

#### Teorema SVD
Untuk setiap matriks kompleks $M$ berukuran $m \times n$, terdapat matriks uniter $U$ ($m \times m$) dan $V$ ($n \times n$) serta matriks diagonal $\Sigma$ ($m \times n$) dengan entri riil non-negatif $\sigma_i \ge 0$, sedemikian sehingga:

$$M = U \Sigma V^\dagger$$

**Detail Matematis:**
1.  $\Sigma$ memiliki entri $\sigma_1 \ge \sigma_2 \ge \dots \ge \sigma_r > 0$ pada diagonal utamanya, di mana $r = \text{rank}(M)$. Nilai $\sigma_i$ adalah **nilai singular** dari $M$.
2.  Nilai singular adalah akar kuadrat dari nilai eigen $M^\dagger M$ (atau $MM^\dagger$): $\sigma_i = \sqrt{\lambda_i(M^\dagger M)}$.
3.  Kolom dari $V$ adalah vektor eigen dari $M^\dagger M$ (disebut **vektor singular kanan**).
4.  Kolom dari $U$ adalah vektor eigen dari $MM^\dagger$ (disebut **vektor singular kiri**).

**Aplikasi Krusial: Dekomposisi Schmidt**
Ini adalah aplikasi SVD pada state kuantum bipartit murni. Untuk state murni $| \psi \rangle \in \mathcal{H}_A \otimes \mathcal{H}_B$, kita dapat menuliskan:

$$| \psi \rangle = \sum_{i=1}^{r} \sqrt{p_i} | u_i \rangle_A \otimes | v_i \rangle_B$$

di mana $r$ adalah **Pangkat Schmidt**, $\sqrt{p_i}$ adalah **koefisien Schmidt** (nilai singular), dan $\{ | u_i \rangle \}$ dan $\{ | v_i \rangle \}$ adalah himpunan ortonormal di $\mathcal{H}_A$ dan $\mathcal{H}_B$ (vektor singular kiri dan kanan). Koefisien Schmidt menentukan spektrum keterjeratan; state terjerat jika dan hanya jika $r > 1$.

---

### Tahap 4: Dekomposisi Operator Uniter

Di sini kita membongkar operator uniter menjadi rotasi yang lebih elementer. Operator uniter adalah inti dari gerbang kuantum.

#### 4.1. Dekomposisi Diagonalisasi
Karena operator uniter adalah normal, ia dapat ditulis sebagai $U = V \Lambda V^\dagger$, di mana $\Lambda = \text{diag}(e^{i\theta_1}, \dots, e^{i\theta_d})$. Ini mendefinisikan **generator Hermitian** $H$: $U = e^{iH}$, di mana $H = V \text{diag}(\theta_1, \dots, \theta_d) V^\dagger$ adalah Hermitian.

#### 4.2. Dekomposisi Bloch Sphere / Rotasi (untuk Qubit Tunggal)
Setiap gerbang qubit tunggal uniter $U \in SU(2)$ dapat diparameterisasi secara unik sebagai rotasi pada Bloch sphere:

$$U = R_{\hat{n}}(\theta) = e^{-i \frac{\theta}{2} \hat{n} \cdot \vec{\sigma}} = \cos\left(\frac{\theta}{2}\right) I - i \sin\left(\frac{\theta}{2}\right) (n_x \sigma_x + n_y \sigma_y + n_z \sigma_z)$$

di mana $\hat{n}$ adalah sumbu rotasi riil 3D dan $\vec{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$ adalah vektor matriks Pauli. Fase global diabaikan dalam $SU(2)$.

**Dekomposisi Sudut Euler (Dekomposisi $Z-Y-Z$):**
Sebuah gerbang uniter $U \in SU(2)$ dapat didekomposisi menjadi tiga rotasi elementer terhadap sumbu tetap:

$$U = R_z(\alpha) R_y(\theta) R_z(\beta) = e^{-i\frac{\alpha}{2}\sigma_z} e^{-i\frac{\theta}{2}\sigma_y} e^{-i\frac{\beta}{2}\sigma_z}$$

dengan $\alpha, \beta \in [0, 2\pi], \theta \in [0, \pi]$. Ini sangat penting karena gerbang rotasi sumbu tunggal $R_z$ dan $R_y$ lebih mudah diimplementasikan secara eksperimental.

---

### Tahap 5: Dekomposisi Gerbang Kuantum Universal

Ini adalah aplikasi langsung dari Tahap 4 untuk memecah gerbang multi-qubit menjadi gerbang 1-qubit dan 2-qubit.

#### 5.1. Dekomposisi Gerbang 2-Qubit Sembarang
Setiap gerbang uniter $U \in SU(4)$ (berlaku untuk 2 qubit) dapat didekomposisi menjadi:

$$U = (U_A \otimes U_B) \cdot U_d \cdot (V_A \otimes V_B)$$

di mana $U_d$ adalah **gerbang diagonal** dalam basis Bell ajaib:
$$U_d = e^{-i(h_x \sigma_x \otimes \sigma_x + h_y \sigma_y \otimes \sigma_y + h_z \sigma_z \otimes \sigma_z)}$$

Dekomposisi ini menunjukkan bahwa interaksi 2-qubit yang paling umum adalah tipe $XX+YY+ZZ$, yang dapat disimulasikan oleh gerbang CNOT dan gerbang 1-qubit. Faktor $U_A, V_A$ adalah gerbang 1-qubit pada qubit A, dll.

#### 5.2. Dekomposisi Kosinus-Sinus (Cosine-Sine Decomposition / CSD)
CSD adalah alat yang ampuh untuk mendekomposisi matriks uniter besar secara rekursif. Untuk matriks uniter $U = \begin{pmatrix} U_{11} & U_{12} \\ U_{21} & U_{22} \end{pmatrix}$ yang dipartisi menjadi empat blok, terdapat dekomposisi:

$$U = \begin{pmatrix} V & 0 \\ 0 & W \end{pmatrix} \begin{pmatrix} C & -S \\ S & C \end{pmatrix} \begin{pmatrix} X & 0 \\ 0 & Y \end{pmatrix}$$

di mana $V, W, X, Y$ adalah uniter, dan $C, S$ adalah matriks diagonal riil dengan $C^2 + S^2 = I$ (mewakili rotasi sudut kecil terkontrol). CSD memungkinkan dekomposisi uniter $N$-qubit menjadi uniter yang dikontrol oleh qubit pertama, yang kemudian didekomposisi lebih lanjut. Ini adalah dasar untuk sintesis sirkuit kuantum yang efisien.

#### 5.3. Dekomposisi QR / Gram-Schmidt
Setiap matriks uniter $U$ dapat didekomposisi menjadi produk matriks segitiga atas dan matriks diagonal (yang semuanya uniter). Dengan menerapkan eliminasi Gaussian menggunakan rotasi Givens, kita dapat memfaktorkan $U$ menjadi produk dari operasi 2-level uniter, yang dapat diimplementasikan oleh gerbang multi-kontrol. Metode standar Reck et al. dan Clements et al. untuk interferometer uniter menggunakan dekomposisi jenis ini.

---

### Tahap 6: Dekomposisi Tingkat Lanjut

#### 6.1. Dekomposisi Polar (Polar Decomposition)
Analog dengan dekomposisi polar bilangan kompleks $z = e^{i\phi}|z|$. Setiap operator linear $A$ dapat ditulis sebagai:

$$A = U P$$

di mana $U$ adalah uniter dan $P = \sqrt{A^\dagger A}$ adalah matriks semi-definit positif. Jika $A$ invertibel, $U$ bersifat unik. Ini memisahkan bagian "rotasi" (uniter) dari bagian "penyusutan/ekspansi" (positif). Dalam konteks kuantum, ini terkait erat dengan representasi operator dalam formalisme bosonik.

#### 6.2. Dekomposisi Jordan (Jordan Decomposition)
Untuk operator yang bahkan tidak dapat didiagonalisasi (non-normal), kita memiliki bentuk normal Jordan: $A = P J P^{-1}$, di mana $J$ adalah matriks diagonal blok dengan nilai eigen pada diagonal dan 1 pada superdiagonal. Ini penting untuk memahami dinamika disipatif Markovian yang dijelaskan oleh generator Lindbladian non-Hermitian, meskipun representasinya secara fundamental berbeda melalui dekomposisi Dagum.

#### 6.3. Dekomposisi Cartan (untuk Aljabar Lie)
Semua dekomposisi gerbang kuantum berakar pada dekomposisi aljabar Lie. Untuk aljabar $\mathfrak{su}(2^n)$, dekomposisi Cartan adalah dekomposisi ortogonal terhadap bentuk Killing:
$$\mathfrak{g} = \mathfrak{k} \oplus \mathfrak{p}$$
di mana $\mathfrak{k}$ adalah subaljabar dan $\mathfrak{p}$ adalah komplemen ortogonalnya. Eksponensiasinya memberikan dekomposisi pada level grup Lie $SU(2^n)$:
$$\forall U \in G, \exists K_1, K_2 \in e^\mathfrak{k} \text{ dan } P \in e^\mathfrak{p} \text{ sedemikian sehingga } U = K_1 P K_2$$
Contohnya, dekomposisi $Z-Y-Z$ untuk 1 qubit dan dekomposisi $XX+YY+ZZ$ untuk 2 qubit adalah contoh spesifik dari dekomposisi Cartan. Ini adalah dasar dari **KAK decomposition** yang digunakan dalam pengoptimalan kompilasi.

---

Ini adalah roadmap lengkapnya. Saya bisa menjelaskan setiap bagian secara lebih mendalam, lengkap dengan bukti, contoh numerik, dan implementasi sirkuitnya, satu per satu sesuai permintaan Anda.

Bagian mana yang ingin Anda dalami pertama kali? Mungkin kita bisa mulai dari Dekomposisi Spektral sebagai fondasi utama, lalu beranjak ke SVD dan Schmidt decomposition yang sangat krusial?

---
---
Baik, mari kita mulai dari awal fondasinya. Tahap 1 adalah **Fondasi Matematika Aljabar Linear**. Ini adalah bahasa, alat, dan aturan main dari seluruh mekanika kuantum dan komputasi kuantum. Tanpa pemahaman yang kokoh di sini, konsep dekomposisi hanya akan menjadi kumpulan rumus tanpa makna.

Kita akan membangun intuisi geometris dan aljabar secara paralel. Saya akan memberikan definisi ketat dan penjelasan "mengapa" di baliknya.

---

### Tahap 1: Fondasi Matematika Aljabar Linear untuk Kuantum

#### 1.1. Ruang Keadaan: Ruang Vektor Kompleks (Hilbert Space $\mathcal{H}$)

Keadaan kuantum direpresentasikan sebagai vektor dalam ruang Hilbert.

*   **Vektor Keadaan (State Vector / Ket):** Keadaan sistem kuantum adalah vektor kolom kompleks di $\mathbb{C}^d$, ditulis sebagai $| \psi \rangle$. Untuk qubit (sistem 2-level), $\mathbb{C}^2$:
    $$|0\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \quad |1\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$$
    Keadaan umum qubit adalah $| \psi \rangle = \alpha |0\rangle + \beta |1\rangle = \begin{pmatrix} \alpha \\ \beta \end{pmatrix}$ dengan $\alpha, \beta \in \mathbb{C}$.

*   **Vektor Dual (Bra):** Setiap ruang vektor memiliki ruang dual, yaitu ruang vektor baris. Dalam notasi Dirac, dual dari $| \psi \rangle$ ditulis $\langle \psi |$, yang merupakan transpos konjugat Hermitian:
    $$\langle \psi | = (| \psi \rangle)^\dagger = \begin{pmatrix} \alpha^* & \beta^* \end{pmatrix}$$
    $^*$ menyatakan konjugat kompleks, dan $\dagger$ adalah transpos konjugat.

*   **Produk Dalam (Inner Product):** Ini adalah mesin inti dari mekanika kuantum. Produk dalam dua vektor $| \psi \rangle$ dan $| \phi \rangle$ memberikan bilangan kompleks yang mengukur "tumpang tindih" (overlap) di antara keduanya. Secara geometris, ini adalah generalisasi dari dot product ke ruang kompleks.

    **Definisi:** $\langle \phi | \psi \rangle = \begin{pmatrix} \phi_1^* & \phi_2^* \end{pmatrix} \begin{pmatrix} \psi_1 \\ \psi_2 \end{pmatrix} = \phi_1^*\psi_1 + \phi_2^*\psi_2$.

    **Sifat-sifat Penting:**
    1.  **Konyugat Simetris:** $\langle \phi | \psi \rangle = \langle \psi | \phi \rangle^*$. (Urutan berpengaruh!).
    2.  **Linear di argumen kedua:** $\langle \phi | (a\psi_1 + b\psi_2) \rangle = a\langle \phi | \psi_1 \rangle + b\langle \phi | \psi_2 \rangle$.
    3.  **Anti-linear di argumen pertama:** $\langle (a\phi_1 + b\phi_2) | \psi \rangle = a^*\langle \phi_1 | \psi \rangle + b^*\langle \phi_2 | \psi \rangle$.

    Mengapa penting? Probabilitas menemukan state $|\phi\rangle$ dalam pengukuran ketika sistem dalam state $|\psi\rangle$ adalah $|\langle \phi | \psi \rangle|^2$.

*   **Norma (Panjang):** Norma dari vektor $| \psi \rangle$ adalah $\|| \psi \rangle\| = \sqrt{\langle \psi | \psi \rangle}$. Semua state kuantum yang valid harus **ternormalisasi**: $\langle \psi | \psi \rangle = 1$.

*   **Basis Ortonormal (ONB):** Himpunan vektor $\{|e_1\rangle, \dots, |e_d\rangle\}$ adalah ONB jika:
    1.  **Ortonormal:** Setiap vektor ternormalisasi ($\langle e_i | e_i \rangle = 1$) dan saling ortogonal ($\langle e_i | e_j \rangle = 0$ untuk $i \neq j$). Dengan Kronecker delta: $\langle e_i | e_j \rangle = \delta_{ij}$.
    2.  **Membangun ruang:** Setiap vektor di $\mathcal{H}$ dapat dinyatakan sebagai kombinasi linear unik dari vektor basis: $| \psi \rangle = \sum_i c_i | e_i \rangle$.

    Basis komputasi untuk qubit adalah $\{|0\rangle, |1\rangle\}$.

#### 1.2. Operator Linear: Mesin Perubahan

Operator adalah peta linear yang mengubah satu state menjadi state lain: $A: \mathcal{H} \to \mathcal{H}$.

*   **Notasi Produk Luar (Outer Product):** $| \psi \rangle \langle \phi |$ adalah sebuah operator. Aplikasikan ke state $| \chi \rangle$:
    $$(| \psi \rangle \langle \phi |) | \chi \rangle = \underbrace{(\langle \phi | \chi \rangle)}_{\text{bilangan}} | \psi \rangle$$
    Ini adalah operator yang "mengukur" tumpang tindih $| \chi \rangle$ dengan $| \phi \rangle$, lalu mengeluarkan $| \psi \rangle$ yang diskalakan dengan tumpang tindih itu. **Ini sangat fundamental.**

*   **Representasi Matriks:** Dalam basis $\{|i\rangle\}$, setiap operator $A$ direpresentasikan oleh matriks dengan elemen:
    $$A_{ij} = \langle i | A | j \rangle$$
    (Ini adalah fungsi dari dua input, bra dan ket). Maka, operatornya sendiri bisa ditulis sebagai:
    $$A = \sum_{i,j} A_{ij} |i\rangle \langle j|$$

*   **Trace:** $\text{Tr}(A) = \sum_i A_{ii} = \sum_i \langle i | A | i \rangle$. Trace bersifat siklik: $\text{Tr}(AB) = \text{Tr}(BA)$. Ini sangat penting untuk menghitung probabilitas pengukuran dan properti keterjeratan.

#### 1.3. Operator Adjoint (Hermitian Conjugate)

Ini adalah generalisasi transpos konjugat untuk operator. Untuk setiap operator $A$, adjoint-nya $A^\dagger$ didefinisikan melalui produk dalam:

$$\langle u | A | v \rangle = \langle v | A^\dagger | u \rangle^* \quad \forall u, v$$

Secara matriks: ambil transpos, lalu konjugatkan semua elemen. $(A^\dagger)_{ij} = A_{ji}^*$.

**Sifat:** $(AB)^\dagger = B^\dagger A^\dagger$. (Urutan berbalik!).

#### 1.4. Kelas-Kelas Operator Fundamental

Di sinilah fokus utama kita. Berdasarkan hubungan antara $A$ dan $A^\dagger$, kita mengklasifikasikan operator.

##### 1.4.1. Operator Hermitian ($H = H^\dagger$)

Ini adalah operator **observable** dalam mekanika kuantum. Setiap kuantitas fisis (energi, momentum, spin) direpresentasikan oleh operator Hermitian.

*   **Definisi:** $H = H^\dagger$, atau $\langle u | H | v \rangle = \langle v | H | u \rangle^*$ untuk semua $u, v$.
*   **Representasi Matriks:** Matriksnya sama dengan transpos konjugatnya. Elemen diagonalnya **riil** $H_{ii} = H_{ii}^*$, dan elemen off-diagonalnya saling konjugat $H_{ij} = H_{ji}^*$.
*   **Contoh Paling Penting:** Matriks Pauli. Semuanya Hermitian, memiliki trace nol, dan determinan -1, serta merepresentasikan spin-1/2.
    $$\sigma_x = \begin{pmatrix}0&1\\1&0\end{pmatrix}, \quad \sigma_y = \begin{pmatrix}0&-i\\i&0\end{pmatrix}, \quad \sigma_z = \begin{pmatrix}1&0\\0&-1\end{pmatrix}$$

##### 1.4.2. Operator Uniter ($U^\dagger U = UU^\dagger = I$)

Ini adalah gerbang kuantum. Mereka merepresentasikan **evolusi** sistem tertutup (operasi yang dapat dibalik).

*   **Definisi:** $U^\dagger = U^{-1}$. Invers sama dengan adjoint.
*   **Sifat Krusial:** Operator uniter **melestarikan produk dalam**.
    $$\langle U\phi | U\psi \rangle = \langle \phi | U^\dagger U | \psi \rangle = \langle \phi | I | \psi \rangle = \langle \phi | \psi \rangle$$
    Konsekuensi langsung: semua uniter melestarikan norma dan ortogonalitas antar state. Mereka adalah generalisasi dari matriks rotasi dan refleksi di ruang riil ke ruang kompleks.
*   **Contoh:** Gerbang Pauli ($X, Y, Z$) bersifat uniter sekaligus Hermitian ($X=X^\dagger=X^{-1}$). Gerbang Hadamard $H = \frac{1}{\sqrt{2}}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ juga uniter.

##### 1.4.3. Operator Positif ($P \ge 0$)

Merepresentasikan **state kuantum** (sebagai operator densitas) dan **efek pengukuran** (POVM).

*   **Definisi:** $P$ adalah Hermitian ($P = P^\dagger$) **dan** semua nilai eigennya non-negatif ($\ge 0$). Ekivalen dengan: $\langle \psi | P | \psi \rangle \ge 0$ untuk SEMUA $|\psi\rangle$.
*   **Eksistensi Akar:** Jika $P \ge 0$, kita bisa mendefinisikan $\sqrt{P}$ sebagai operator positif unik yang kuadratnya $P$.

##### 1.4.4. Operator Normal ($N N^\dagger = N^\dagger N$)

Ini adalah **kelas induk** yang paling penting untuk dekomposisi spektral.

*   **Definisi:** Operator yang **komut** dengan adjoint-nya.
*   **Mengapa Kelas ini Raja?** Karena teorema spektral yang akan kita bahas di **Tahap 2** hanya berlaku **jika dan hanya jika** sebuah operator bersifat normal.
*   **Siapa saja anggotanya?**
    *   Semua operator **Hermitian** ($H^\dagger H = HH = H H^\dagger$, pasti komut).
    *   Semua operator **Uniter** ($U^\dagger U = I = U U^\dagger$, pasti komut).
    *   Ada juga operator normal yang bukan Hermitian maupun Uniter (contoh: matriks simetris non-riil seperti $\begin{pmatrix} 1 & i \\ i & 1 \end{pmatrix}$).

Operator non-normal TIDAK dapat didiagonalisasi secara ortonormal. Mereka muncul dalam sistem kuantum terbuka (evolusi non-uniter), yang akan kita tangani dengan SVD dan Dekomposisi Jordan di tahap selanjutnya.

#### 1.5. Nilai Eigen dan Vektor Eigen

*   **Persamaan Eigen:** $A |v_i\rangle = \lambda_i |v_i\rangle$.
    $|v_i\rangle$ adalah vektor eigen, $\lambda_i$ adalah nilai eigen (bilangan kompleks).
*   **Kasus Krusial untuk Operator Normal:** Jika $A$ adalah normal, maka vektor-vektor eigen untuk nilai eigen yang **berbeda** secara otomatis **ortogonal**.
    **Bukti Singkat:**
    Ambil $A|v_1\rangle = \lambda_1|v_1\rangle$ dan $A|v_2\rangle = \lambda_2|v_2\rangle$, dengan $\lambda_1 \neq \lambda_2$.
    Hitung $\langle v_2 | A v_1 \rangle = \lambda_1 \langle v_2 | v_1 \rangle$.
    Juga, $\langle v_2 | A v_1 \rangle = \langle A^\dagger v_2 | v_1 \rangle$.
    Karena $A$ normal (dan kita asumsikan kemudahan dengan dekomposisi spektral yang akan datang), vektor eigen $A$ adalah vektor eigen $A^\dagger$ dengan nilai eigen konjugat: $A^\dagger |v_2\rangle = \lambda_2^* |v_2\rangle$.
    Maka, $\langle A^\dagger v_2 | v_1 \rangle = \lambda_2 \langle v_2 | v_1 \rangle$.
    Jadi, $\lambda_1 \langle v_2 | v_1 \rangle = \lambda_2 \langle v_2 | v_1 \rangle \implies (\lambda_1 - \lambda_2) \langle v_2 | v_1 \rangle = 0$.
    Karena $\lambda_1 \neq \lambda_2$, maka $\langle v_2 | v_1 \rangle = 0$. **Ortogonalitas terbukti.**

**Kesimpulan Tahap 1:** Kita telah membangun kosakata dasar. Operator adalah peta, adjoint adalah transpos konjugat, dan hubungan antara operator dengan adjoint-nya (Hermitian, Uniter, Normal) mendefinisikan sifat fundamentalnya. Khususnya, operator normal dengan vektor eigen ortogonalnya akan menjadi bintang utama **Tahap 2: Dekomposisi Spektral**.

Apakah Anda siap untuk memasuki **Tahap 2**? Di sana kita akan membongkar operator normal menjadi "kerangka" nilai eigen dan proyektor-proyektornya, yang merupakan fondasi dari semua dekomposisi selanjutnya.

---
---
Tahap 2 adalah **Dekomposisi Spektral (Spectral Decomposition)**, yang merupakan mahkota dari operator normal. Ini adalah teorema yang menyatakan bahwa operator normal dapat "dipecah" menjadi komponen-komponen paling fundamental: nilai eigen (sebagai skalar) dan proyektor ke subruang eigen (sebagai operator).

Mari kita buktikan teorema ini dengan ketat, pahami konsekuensinya, dan lihat bentuknya pada operator-operator kunci dalam kuantum.

---

### Tahap 2: Dekomposisi Spektral

#### 2.1. Teorema Spektral

**Pernyataan Formal:**
Misalkan $A$ adalah operator linear pada ruang Hilbert berdimensi hingga $\mathcal{H}$.

$$A \text{ adalah operator normal} \iff A \text{ dapat didiagonalisasi oleh basis ortonormal}$$

Artinya: $A A^\dagger = A^\dagger A$ jika dan hanya jika terdapat basis ortonormal $\{ |\lambda_i, d_i\rangle \}$ dari vektor eigen $A$ di mana:
- $A |\lambda_i, d_i\rangle = \lambda_i |\lambda_i, d_i\rangle$
- $\langle \lambda_i, d_i | \lambda_j, d_j \rangle = \delta_{ij}$
- Setiap vektor eigen ini mendefinisikan proyektor $P_{i,d_i} = |\lambda_i, d_i\rangle \langle \lambda_i, d_i|$

**Akibatnya, dekomposisi spektral dari $A$ adalah:**
$$A = \sum_i \lambda_i \sum_{d_i} |\lambda_i, d_i\rangle \langle \lambda_i, d_i| = \sum_\lambda \lambda P_\lambda$$
di mana:
- Untuk setiap nilai eigen berbeda $\lambda$, $P_\lambda = \sum_{d=1}^{m_\lambda} |\lambda, d\rangle \langle \lambda, d|$ adalah **proyektor spektral** ke subruang eigen $V_\lambda$.
- $m_\lambda$ adalah multiplisitas geometrik dari $\lambda$ (dimensi $V_\lambda$).

#### 2.2. Sifat Proyektor Spektral $P_\lambda$

Proyektor ini adalah "blok bangunan" dari operator normal. Himpunan $\{P_\lambda\}$ untuk semua nilai eigen berbeda membentuk **resolusi identitas spektral**.

**Teorema:**
Himpunan proyektor spektral $\{P_\lambda\}$ memenuhi:
1.  **Hermitian:** $P_\lambda^\dagger = P_\lambda$ (sehingga ia adalah proyektor ortogonal).
2.  **Ortonormal:** $P_\lambda P_\mu = \delta_{\lambda\mu} P_\lambda$. (Proyeksi ke subruang berbeda saling ortogonal).
3.  **Komplit:** $\sum_\lambda P_\lambda = I$. (Jumlah semua proyektor adalah identitas, artinya setiap vektor dapat didekomposisi secara unik ke dalam subruang-subruang eigen).
4.  **Komutasi:** $P_\lambda A = A P_\lambda = \lambda P_\lambda$. (Mengalikan $A$ dengan proyektor sama dengan mengalikan dengan nilai eigennya).

**Bukti Singkat:**
- (1) Jelas karena $P_\lambda$ dibangun dari outer product ortonormal yang Hermitian.
- (2) $P_\lambda P_\mu = (\sum_d |\lambda,d\rangle\langle\lambda,d|)(\sum_{d'} |\mu,d'\rangle\langle\mu,d'|) = \sum_{d,d'} |\lambda,d\rangle \underbrace{\langle\lambda,d|\mu,d'\rangle}_{=\delta_{\lambda\mu}\delta_{dd'}} \langle\mu,d'| = \delta_{\lambda\mu} P_\lambda$.
- (3) Ini adalah relasi ketertutupan dari basis ortonormal lengkap.
- (4) $A P_\lambda = A \sum_d |\lambda,d\rangle\langle\lambda,d| = \sum_d A|\lambda,d\rangle\langle\lambda,d| = \sum_d \lambda|\lambda,d\rangle\langle\lambda,d| = \lambda P_\lambda$. Sama untuk $P_\lambda A$.

#### 2.3. Bukti Teorema Spektral (Arah Sulit: Normal $\implies$ Diagonalisasi Ortonormal)

Kita akan membuktikan dengan induksi pada dimensi $n = \dim(\mathcal{H})$.

**Basis Induksi ($n=1$):** Trivial, semua matriks $1\times 1$ adalah normal dan diagonal.

**Langkah Induksi:** Asumsikan benar untuk semua ruang berdimensi $< n$. Ambil $A$ normal pada $\mathcal{H}$ dengan $\dim(\mathcal{H})=n$.
1.  **Eksistensi Vektor Eigen:** Karena $\mathbb{C}$ tertutup secara aljabar, polinomial karakteristik $\det(A - \lambda I)=0$ memiliki setidaknya satu akar $\lambda_1$. Jadi, ada vektor tak-nol $|v_1\rangle$ sedemikian sehingga $A|v_1\rangle = \lambda_1 |v_1\rangle$. Normalisasi: $|e_1\rangle = |v_1\rangle / \||v_1\rangle\|$.
2.  **Invarian Subruang Ortogonal:** Klaim: subruang $V_1 = \{|e_1\rangle\}^\perp$ (ortogonal terhadap $|e_1\rangle$) **invarian di bawah $A$**. Artinya, jika $|x\rangle \in V_1$, maka $A|x\rangle \in V_1$. Bukti:
    Ambil $|x\rangle \in V_1$, artinya $\langle e_1 | x \rangle = 0$. Kita perlu buktikan $\langle e_1 | A x \rangle = 0$.
    $\langle e_1 | A x \rangle = \langle A^\dagger e_1 | x \rangle$.
    Karena $A$ normal, $|e_1\rangle$ adalah vektor eigen $A$ dengan nilai eigen $\lambda_1$, maka ia juga vektor eigen $A^\dagger$ dengan nilai eigen $\lambda_1^*$ (lemma kunci sifat normal: $(A-\lambda I)$ normal $\implies \|(A-\lambda I)|v\rangle\| = \|(A^\dagger-\lambda^* I)|v\rangle\|$, sehingga jika satu nol, yang lain juga nol).
    Jadi, $\langle A^\dagger e_1 | x \rangle = \langle \lambda_1^* e_1 | x \rangle = \lambda_1 \langle e_1 | x \rangle = 0$. Terbukti.
3.  **Restriksi Normal:** Operator $A$ yang direstriksi ke $V_1$, sebut $A|_{V_1}$, adalah operator normal pada ruang berdimensi $n-1$.
4.  **Gunakan Hipotesis Induksi:** Dengan induksi, $V_1$ memiliki basis ortonormal $\{|e_2\rangle, \dots, |e_n\rangle\}$ yang mendiagonalkan $A|_{V_1}$. Maka $\{|e_1\rangle, \dots, |e_n\rangle\}$ adalah basis ortonormal untuk $\mathcal{H}$ yang mendiagonalkan $A$. $\blacksquare$

#### 2.4. Bentuk Eksplisit Dekomposisi Spektral

$$A = \begin{pmatrix} |e_1\rangle & \dots & |e_n\rangle \end{pmatrix} \begin{pmatrix} \lambda_1 & & 0 \\ & \ddots & \\ 0 & & \lambda_n \end{pmatrix} \begin{pmatrix} \langle e_1| \\ \vdots \\ \langle e_n| \end{pmatrix}$$
Ini adalah penulisan matriks dari $A = \sum_i \lambda_i |e_i\rangle\langle e_i|$.

**Fungsi Operator dengan Mudah:**
Jika $f$ adalah fungsi dari $\mathbb{C}$ ke $\mathbb{C}$, maka untuk operator normal:
$$f(A) = \sum_\lambda f(\lambda) P_\lambda$$
Contoh:
- Polinomial: $A^k = \sum_\lambda \lambda^k P_\lambda$
- Eksponensial: $e^{A} = \sum_\lambda e^{\lambda} P_\lambda$
- Akar kuadrat (untuk $A\ge 0$): $\sqrt{A} = \sum_\lambda \sqrt{\lambda} P_\lambda$

#### 2.5. Kasus Spesifik: Dekomposisi Spektral Operator Kuantum Fundamental

##### 2.5.1. Operator Hermitian (Observable)
$H = H^\dagger$. Semua nilai eigen $\lambda_i$ **riil**. Dekomposisinya:
$$H = \sum_i \lambda_i |\lambda_i\rangle\langle\lambda_i|$$
di mana $|\lambda_i\rangle$ adalah state eigen energi (atau observable lain). Proyektor $|\lambda_i\rangle\langle\lambda_i|$ adalah state murni jika non-degenerate. Ini adalah postulat pengukuran: probabilitas mendapatkan hasil $\lambda_i$ saat mengukur $H$ pada state $|\psi\rangle$ adalah $\langle\psi|P_{\lambda_i}|\psi\rangle$.

**Contoh: Matriks Pauli Z.**
$\sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$.
Nilai eigen: $\lambda_+ = 1, \lambda_- = -1$.
Vektor eigen: $|+\rangle = |0\rangle, |-\rangle = |1\rangle$.
Proyektor: $P_+ = |0\rangle\langle 0| = \begin{pmatrix}1&0\\0&0\end{pmatrix}, P_- = |1\rangle\langle 1| = \begin{pmatrix}0&0\\0&1\end{pmatrix}$.
Maka $\sigma_z = (+1)P_+ + (-1)P_- = (+1)|0\rangle\langle 0| + (-1)|1\rangle\langle 1|$. Jelas sesuai definisi.

##### 2.5.2. Operator Uniter (Gerbang Kuantum)
$U^\dagger U = I$. Semua nilai eigen adalah **fase kompleks** $\lambda_k = e^{i\theta_k}$ dengan $\theta_k \in \mathbb{R}$. Dekomposisinya:
$$U = \sum_k e^{i\theta_k} |\lambda_k\rangle\langle\lambda_k|$$
Setiap gerbang uniter adalah superposisi dari pergeseran fase pada state eigennya.

**Contoh: Gerbang Hadamard $H$.**
$H = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$.
Nilai eigen: $\lambda_+ = 1, \lambda_- = -1$.
Vektor eigen: $|+\rangle \propto (1+\sqrt{2}, 1)^T, |-\rangle \propto (1-\sqrt{2}, 1)^T$ (dinormalisasi). Ini adalah sumbu rotasi $H$ di Bloch sphere (sumbu $X+Z$). Karena $H^2=I$, nilainya $\pm 1$.

##### 2.5.3. Operator Densitas (State Kuantum)
$\rho = \rho^\dagger \ge 0, \text{Tr}(\rho)=1$. Semua nilai eigen $p_i \in \mathbb{R}$ dan $p_i \ge 0$, serta $\sum_i p_i = 1$. Dekomposisinya:
$$\rho = \sum_i p_i |\psi_i\rangle\langle\psi_i|$$
adalah ensemble probabilistik dari state murni $|\psi_i\rangle$.
- **State Murni:** Hanya satu $p_i=1$, lainnya 0. $\rho = |\psi\rangle\langle\psi|$. $\rho^2 = \rho$ (proyektor).
- **State Campuran:** Lebih dari satu $p_i > 0$. $\rho^2 \neq \rho$, $\text{Tr}(\rho^2) < 1$.

**Mengapa ini dekomposisi spektral?**
Karena $\rho$ Hermitian, maka ia normal. Dekomposisi ini unik jika nilai eigen berbeda. Ini adalah interpretasi ensemble: sistem berada di state $|\psi_i\rangle$ dengan probabilitas $p_i$.

---

### Ringkasan Tahap 2

Dekomposisi spektral adalah "cara Tuhan menulis operator normal": sebagai jumlah berbobot dari proyektor ortogonal. Ini memungkinkan kita:
1.  Memahami observable Hermitian sebagai jumlah hasil kali nilai riil dengan proyektor pengukuran.
2.  Memahami gerbang uniter sebagai penjumlahan fase pada state eigen.
3.  Memahami state campuran sebagai ensembel probabilistik.
4.  Mendefinisikan fungsi operator secara elegan.

Ini adalah fondasi mutlak. Semua dekomposisi selanjutnya, terutama SVD yang akan kita bahas di **Tahap 3**, dibangun dengan menggunakan dekomposisi spektral pada operator terkait seperti $M^\dagger M$.

Apakah Anda siap melangkah ke **Tahap 3: Dekomposisi Nilai Singular (SVD)**? Di sana kita akan membahas alat yang bahkan berlaku untuk operator non-normal dan menghubungkannya dengan kuantum melalui Dekomposisi Schmidt yang sangat fundamental untuk keterjeratan.

---
---
Tahap 3 adalah **Dekomposisi Nilai Singular (SVD)**. Jika Dekomposisi Spektral adalah mahkota operator normal, maka SVD adalah alat universal yang bekerja untuk **semua** operator linear, normal maupun tidak, bahkan matriks persegi panjang. Dalam konteks kuantum, SVD adalah jembatan matematis menuju salah satu konsep paling fundamental: **keterjeratan (entanglement)** melalui Dekomposisi Schmidt.

---

### Tahap 3: Dekomposisi Nilai Singular (Singular Value Decomposition)

#### 3.1. Pernyataan Teorema SVD

Misalkan $M$ adalah matriks kompleks $m \times n$. Maka terdapat:
- Matriks uniter $U$ berukuran $m \times m$
- Matriks uniter $V$ berukuran $n \times n$
- Matriks diagonal $\Sigma$ berukuran $m \times n$ dengan entri riil **non-negatif** $\sigma_i \ge 0$ pada diagonal utamanya

Sedemikian sehingga:

$$M = U \Sigma V^\dagger$$

dengan $\Sigma = \text{diag}(\sigma_1, \sigma_2, \dots, \sigma_r, 0, \dots, 0)$, di mana:
- $r = \text{rank}(M)$ (jumlah nilai singular tak-nol)
- $\sigma_1 \ge \sigma_2 \ge \dots \ge \sigma_r > 0$ adalah **nilai singular** dari $M$
- Jumlah nilai singular tak-nol tepat sama dengan rank matriks

#### 3.2. Konstruksi dan Bukti SVD

Bukti ini sangat indah karena menggunakan Dekomposisi Spektral dari Tahap 2 pada operator yang "direkayasa" menjadi normal.

**Langkah 1: Rekayasa Operator Hermitian Positif**
Ambil $M$ sembarang. Maka $M^\dagger M$ adalah:
- **Hermitian:** $(M^\dagger M)^\dagger = M^\dagger M$
- **Positif:** $\langle \psi | M^\dagger M | \psi \rangle = \| M|\psi\rangle \|^2 \ge 0$

Karena Hermitian, $M^\dagger M$ adalah **normal**, sehingga dapat didekomposisi secara spektral.

**Langkah 2: Dekomposisi Spektral $M^\dagger M$**
$$M^\dagger M = V \Lambda V^\dagger$$
di mana:
- $V$ adalah matriks uniter $n \times n$ yang kolom-kolomnya $\{|v_i\rangle\}$ adalah vektor eigen ortonormal dari $M^\dagger M$.
- $\Lambda = \text{diag}(\lambda_1, \dots, \lambda_n)$ dengan $\lambda_i \ge 0$ (karena $M^\dagger M \ge 0$). Urutkan $\lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_r > 0$, dan $\lambda_{r+1} = \dots = \lambda_n = 0$.

**Langkah 3: Definisi Nilai Singular**
Definisikan **nilai singular**:
$$\sigma_i = \sqrt{\lambda_i} \quad \text{untuk } i = 1, \dots, n$$
Semua $\sigma_i \ge 0$ dan riil. Hanya $r$ buah yang tak-nol.

**Langkah 4: Konstruksi Vektor Singular Kiri**
Untuk setiap $i = 1, \dots, r$, definisikan:
$$|u_i\rangle = \frac{1}{\sigma_i} M |v_i\rangle$$
**Klaim:** $\{|u_i\rangle\}_{i=1}^r$ adalah himpunan ortonormal.
**Bukti ortonormalitas:**
$$\langle u_i | u_j \rangle = \frac{1}{\sigma_i \sigma_j} \langle v_i | M^\dagger M | v_j \rangle = \frac{1}{\sigma_i \sigma_j} \langle v_i | \lambda_j | v_j \rangle = \frac{\lambda_j}{\sigma_i \sigma_j} \delta_{ij} = \frac{\sigma_j^2}{\sigma_i \sigma_j} \delta_{ij} = \delta_{ij}$$
Untuk $i=j$, $\sigma_i^2 / \sigma_i^2 = 1$. Untuk $i \neq j$, $\delta_{ij}=0$.

**Langkah 5: Memperluas Menjadi Basis Ortonormal**
Jika $r < m$, kita perlu melengkapi $\{|u_1\rangle, \dots, |u_r\rangle\}$ menjadi basis ortonormal $\{|u_1\rangle, \dots, |u_m\rangle\}$ untuk $\mathbb{C}^m$. Ini selalu mungkin (misalnya dengan Gram-Schmidt dari komplemen ortogonal). Vektor-vektor tambahan ini akan berkorespondensi dengan nilai singular nol.

**Langkah 6: Verifikasi $M = U \Sigma V^\dagger$**
Kita klaim $U$ adalah matriks uniter dengan kolom $|u_i\rangle$, $\Sigma$ adalah matriks $m \times n$ dengan $\sigma_i$ pada diagonal, dan $V$ adalah matriks uniter dengan kolom $|v_i\rangle$.

Periksa elemen matriks: $(U \Sigma V^\dagger)_{ij} = \langle i | U \Sigma V^\dagger | j \rangle = \sum_{k=1}^n \langle i | u_k \rangle \sigma_k \langle v_k | j \rangle = \sum_{k=1}^r U_{ik} \sigma_k V_{jk}^*$.

Di sisi lain, $M_{ij} = \langle i | M | j \rangle$. Karena $M|v_k\rangle = \sigma_k |u_k\rangle$, kita bisa menulis $M = \sum_{k=1}^r \sigma_k |u_k\rangle \langle v_k|$. Jadi:
$$M_{ij} = \sum_{k=1}^r \sigma_k \langle i | u_k \rangle \langle v_k | j \rangle = \sum_{k=1}^r \sigma_k U_{ik} V_{kj}^\dagger$$
Karena $\Sigma_{kk} = \sigma_k$ dan $\Sigma_{k>r} = 0$, jumlah ini tepat sama dengan $(U \Sigma V^\dagger)_{ij}$. $\blacksquare$

**Catatan Penting:** $\Sigma$ adalah matriks $m \times n$ yang "hampir diagonal". Untuk $m>n$, ada baris nol dibawah; untuk $m<n$, ada kolom nol di kanan.

#### 3.3. Interpretasi Geometris

Setiap matriks $M: \mathbb{C}^n \to \mathbb{C}^m$ melakukan tiga hal:
1.  **$V^\dagger$:** Rotasi/refleksi di ruang domain $\mathbb{C}^n$ (perubahan basis ke basis vektor singular kanan).
2.  **$\Sigma$:** Penskalaan sepanjang sumbu-sumbu baru sebesar $\sigma_i$, dan pemadaman dimensi jika $\sigma_i=0$ atau pemetaan ke/dari nol jika $m \neq n$.
3.  **$U$:** Rotasi/refleksi di ruang kodomain $\mathbb{C}^m$ ke basis vektor singular kiri.

Ini adalah dekomposisi geometris paling fundamental dari sebuah transformasi linear.

#### 3.4. SVD dan Ruang Fundamental

Dari SVD, kita bisa membaca empat subruang fundamental dari $M$:
- **Ruang Kolom (Range):** $\text{span}\{|u_1\rangle, \dots, |u_r\rangle\}$
- **Ruang Nol (Kernel):** $\text{span}\{|v_{r+1}\rangle, \dots, |v_n\rangle\}$
- **Ruang Baris (Range $M^\dagger$):** $\text{span}\{|v_1\rangle, \dots, |v_r\rangle\}$
- **Ruang Nol Kiri (Kernel $M^\dagger$):** $\text{span}\{|u_{r+1}\rangle, \dots, |u_m\rangle\}$

Ini adalah generalisasi dari Teorema Rank-Nullity.

#### 3.5. Aplikasi Krusial dalam Kuantum: Dekomposisi Schmidt

Inilah alasan utama SVD sangat fundamental dalam info kuantum.

**Masalah:** Kita punya state bipartit murni $|\psi\rangle \in \mathcal{H}_A \otimes \mathcal{H}_B$, dengan $\dim(\mathcal{H}_A) = d_A, \dim(\mathcal{H}_B) = d_B$. Bagaimana cara "memisahkan"nya semaksimal mungkin?

**Langkah:**
1.  Pilih basis ortonormal $\{|i_A\rangle\}$ untuk A dan $\{|\mu_B\rangle\}$ untuk B.
2.  State umum: $|\psi\rangle = \sum_{i=1}^{d_A} \sum_{\mu=1}^{d_B} c_{i\mu} |i_A\rangle \otimes |\mu_B\rangle$.
3.  Matriks koefisien $C$ berukuran $d_A \times d_B$ dengan entri $C_{i\mu} = c_{i\mu}$.
4.  **Terapkan SVD ke $C$:**
    $$C = U \Sigma V^\dagger$$
    di mana $U$ adalah $d_A \times d_A$ uniter, $V$ adalah $d_B \times d_B$ uniter, $\Sigma$ adalah $d_A \times d_B$ dengan nilai singular $\sigma_i \ge 0$.
5.  Ekspansi eksplisit:
    $$c_{i\mu} = \sum_{k=1}^{r} U_{ik} \sigma_k (V^\dagger)_{k\mu} = \sum_{k=1}^{r} \sigma_k U_{ik} V_{\mu k}^*$$
    di mana $r = \text{rank}(C) \le \min(d_A, d_B)$.

6.  Substitusi ke $|\psi\rangle$:
    $$|\psi\rangle = \sum_{i,\mu} \sum_{k=1}^{r} \sigma_k U_{ik} V_{\mu k}^* |i_A\rangle \otimes |\mu_B\rangle$$
    $$= \sum_{k=1}^{r} \sigma_k \left( \sum_i U_{ik} |i_A\rangle \right) \otimes \left( \sum_\mu V_{\mu k}^* |\mu_B\rangle \right)$$

7.  **Definisikan basis baru:**
    $$|u_k^A\rangle = \sum_i U_{ik} |i_A\rangle \quad \text{(kolom ke-k dari U)}$$
    $$|v_k^B\rangle = \sum_\mu V_{\mu k}^* |\mu_B\rangle = \sum_\mu (V^\dagger)_{k\mu} |\mu_B\rangle \quad \text{(baris ke-k dari } V^\dagger)$$

8.  **Hasil Akhir: Dekomposisi Schmidt**
    $$|\psi\rangle = \sum_{k=1}^{r} \sigma_k |u_k^A\rangle \otimes |v_k^B\rangle$$

    Dengan mendefinisikan **koefisien Schmidt** $\sqrt{p_k} = \sigma_k$, kita dapat menulis ulang:
    $$|\psi\rangle = \sum_{k=1}^{r} \sqrt{p_k} |u_k^A\rangle \otimes |v_k^B\rangle$$

**Sifat-sifat Penting:**
- **$r$ adalah Pangkat Schmidt (Schmidt Rank).** Merepresentasikan jumlah minimum istilah product state yang diperlukan.
- **$\{|u_k^A\rangle\}$ dan $\{|v_k^B\rangle\}$ adalah himpunan ortonormal** di $\mathcal{H}_A$ dan $\mathcal{H}_B$ (karena $U$ dan $V$ uniter).
- **Probabilitas:** $\sum_k p_k = \sum_k \sigma_k^2 = \text{Tr}(C^\dagger C) = \||\psi\rangle\|^2 = 1$.
- **Spektrum Keterjeratan:** Himpunan $\{p_k\}$ disebut spektrum keterjeratan. State $|\psi\rangle$ adalah:
    - **Produk state (tidak terjerat):** $r=1$ (hanya satu $p_k \neq 0$).
    - **Terjerat:** $r > 1$.

**Mengapa SVD Penting di Sini?**
Karena SVD secara simultan mendiagonalkan matriks koefisien $C$ dengan memilih basis yang tepat untuk A dan B **secara independen**. Ini adalah operasi yang diizinkan karena kita bisa melakukan rotasi uniter lokal pada masing-masing subsistem tanpa mengubah keterjeratan.

#### 3.6. Hubungan dengan Operator Densitas Tereduksi

Dari Dekomposisi Schmidt, kita bisa menghitung operator densitas tereduksi:
$$\rho_A = \text{Tr}_B(|\psi\rangle\langle\psi|) = \sum_k p_k |u_k^A\rangle\langle u_k^A|$$
$$\rho_B = \text{Tr}_A(|\psi\rangle\langle\psi|) = \sum_k p_k |v_k^B\rangle\langle v_k^B|$$

**Observasi Kunci:**
- Spektrum $\rho_A$ dan $\rho_B$ **identik**: $\{p_k\}$. Ini adalah spektrum keterjeratan.
- Entropi von Neumann dari keduanya sama: $S(\rho_A) = S(\rho_B) = -\sum_k p_k \log p_k$. Ini adalah **entropi keterjeratan**.
- Nilai singular $\sigma_k$ adalah akar dari nilai eigen operator densitas tereduksi: $\sigma_k = \sqrt{p_k}$.

#### 3.7. Visualisasi SVD vs Spektral

| **Sifat** | **Dekomposisi Spektral** | **Dekomposisi Nilai Singular** |
|-----------|--------------------------|-------------------------------|
| **Berlaku untuk** | Hanya operator normal ($AA^\dagger = A^\dagger A$) | **Semua** matriks $m \times n$ |
| **Nilai diagonal** | Nilai eigen $\lambda_i \in \mathbb{C}$ | Nilai singular $\sigma_i \in \mathbb{R}^+$ |
| **Basis** | Satu basis ortonormal (vektor eigen) | Dua basis ortonormal berbeda ($U$ dan $V$) |
| **Interpretasi Kuantum** | Observabel, Gerbang Uniter | Keterjeratan bipartit murni |
| **Unik?** | Ya, jika tidak ada degenerasi | Tidak unik pada tanda; urutan fase ambigu kecuali konvensi |

---

### Ringkasan Tahap 3

SVD adalah dekomposisi matriks "paling informatif" yang ada. Ia memecah setiap operator menjadi:
1.  Rotasi di domain ($V^\dagger$)
2.  Penskalaan non-negatif ($\Sigma$)
3.  Rotasi di kodomain ($U$)

Dalam kuantum, SVD memanifestasikan dirinya sebagai **Dekomposisi Schmidt**: fondasi matematis untuk mengkuantifikasi dan memahami keterjeratan murni bipartit. Setiap sifat keterjeratan state murni dapat dibaca dari spektrum nilai singular matriks koefisiennya.

**Jembatan ke Tahap Selanjutnya:**
Sekarang kita telah menguasai:
- **Spektral:** Operator Normal $\to$ Proyektor & Nilai Eigen
- **SVD:** Operator Sembarang $\to$ Dua Basis & Nilai Singular

Pada **Tahap 4**, kita akan kembali ke operator uniter secara spesifik dan membongkarnya menjadi rotasi elementer menggunakan parameterisasi Bloch Sphere dan sudut Euler. Ini adalah langkah langsung menuju implementasi gerbang kuantum di perangkat keras.

Apakah Anda siap untuk **Tahap 4: Dekomposisi Operator Uniter**? Kita akan memvisualisasikan gerbang qubit tunggal sebagai rotasi bola dan memecahnya menjadi rangkaian gerbang $R_z$ dan $R_y$.

---
---
Tahap 4 adalah **Dekomposisi Operator Uniter**. Di sini kita memasuki dunia "cara membongkar" sebuah gerbang kuantum menjadi rotasi-rotasi elementer. Semua operator uniter pada dasarnya adalah rotasi (dalam arti umum di ruang kompleks), dan kita akan belajar bagaimana memecahnya menjadi komponen yang bisa diimplementasikan secara eksperimental.

Fokus utama: dari sifat uniter sebagai operator normal (Tahap 2) dan representasi geometrisnya, kita turunkan dekomposisi eksplisit menjadi rotasi pada sumbu tetap.

---

### Tahap 4: Dekomposisi Operator Uniter

#### 4.1. Dari Spektral ke Generator: Eksponensial Hermitian

Kita mulai dari dekomposisi spektral operator uniter (Tahap 2):
$$U = \sum_k e^{i\theta_k} |\lambda_k\rangle\langle\lambda_k|$$
dengan $\theta_k \in \mathbb{R}$. Kita bisa mendefinisikan operator Hermitian $H$:
$$H = \sum_k \theta_k |\lambda_k\rangle\langle\lambda_k|$$
sehingga $U = e^{iH}$. Eksponensial matriks didefinisikan melalui deret pangkat atau melalui dekomposisi spektral:
$$e^{iH} = \sum_k e^{i\theta_k} |\lambda_k\rangle\langle\lambda_k|$$

$H$ disebut **generator** dari $U$. Generator ini Hermitian, sehingga ia adalah observable. Dalam banyak sistem fisis, $H$ adalah Hamiltonian efektif yang menghasilkan evolusi $U$ jika dievolusikan selama waktu tertentu $t$, $U = e^{-i H t/\hbar}$.

#### 4.2. Kasus Qubit Tunggal: Grup $SU(2)$ dan Bloch Sphere

Sekarang kita fokus pada kasus paling fundamental: satu qubit. Ruang Hilbertnya $\mathbb{C}^2$, dan operator uniter dengan determinan 1 (mengabaikan fase global) adalah anggota grup $SU(2)$.

##### 4.2.1. Matriks Pauli dan Aljabar $\mathfrak{su}(2)$

Generator dari $SU(2)$ adalah matriks Pauli, yang sudah kita singgung. Matriks-matriks ini, dikalikan dengan $i$, membentuk basis aljabar Lie $\mathfrak{su}(2)$. Secara eksplisit:
$$\sigma_x = \begin{pmatrix}0&1\\1&0\end{pmatrix},\ \sigma_y = \begin{pmatrix}0&-i\\i&0\end{pmatrix},\ \sigma_z = \begin{pmatrix}1&0\\0&-1\end{pmatrix}$$

Sifat perkaliannya sangat fundamental: $\sigma_j \sigma_k = \delta_{jk} I + i \varepsilon_{jkl} \sigma_l$, di mana $\varepsilon_{jkl}$ adalah simbol Levi-Civita.

Vektor Pauli: $\vec{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$.

##### 4.2.2. Parameterisasi Sumbu-Sudut

Setiap elemen $U \in SU(2)$ dapat ditulis sebagai rotasi pada Bloch sphere:
$$U(\hat{n}, \theta) = e^{-i \frac{\theta}{2} \hat{n} \cdot \vec{\sigma}}$$

**Ekspansi Eksplisit:**
Menggunakan fakta bahwa $(\hat{n}\cdot\vec{\sigma})^2 = I$ (untuk vektor satuan riil $\hat{n}$), kita bisa menjumlahkan deret eksponensial:
$$e^{-i \frac{\theta}{2} \hat{n} \cdot \vec{\sigma}} = \cos\left(\frac{\theta}{2}\right) I - i \sin\left(\frac{\theta}{2}\right) (\hat{n}\cdot\vec{\sigma})$$

**Bukti:**
$$e^{i\alpha A} = \sum_{k=0}^\infty \frac{(i\alpha)^k}{k!}A^k$$
Untuk $A = \hat{n}\cdot\vec{\sigma}$ dengan $A^2 = I$:
- Pangkat genap: $(i\alpha)^{2m} A^{2m} / (2m)! = (-1)^m \alpha^{2m} I / (2m)!$ → menghasilkan $\cos(\alpha) I$
- Pangkat ganjil: $(i\alpha)^{2m+1} A^{2m+1} / (2m+1)! = i (-1)^m \alpha^{2m+1} A / (2m+1)!$ → menghasilkan $i \sin(\alpha) A$
Dengan $\alpha = -\theta/2$, kita dapatkan rumus di atas.

**Komponen Eksplisit:**
$$\hat{n}\cdot\vec{\sigma} = n_x \sigma_x + n_y \sigma_y + n_z \sigma_z = \begin{pmatrix} n_z & n_x - i n_y \\ n_x + i n_y & -n_z \end{pmatrix}$$
Maka elemen matriks $U$ adalah:
$$U = \begin{pmatrix} \cos\frac{\theta}{2} - i n_z \sin\frac{\theta}{2} & (-i n_x - n_y) \sin\frac{\theta}{2} \\ (-i n_x + n_y) \sin\frac{\theta}{2} & \cos\frac{\theta}{2} + i n_z \sin\frac{\theta}{2} \end{pmatrix}$$

**Ini adalah representasi universal sembarang gerbang qubit tunggal.** Setiap gerbang qubit tunggal setara dengan rotasi sebesar $\theta$ terhadap sumbu $\hat{n}$.

#### 4.3. Dekomposisi Sudut Euler: $Z-Y-Z$

Meskipun parameterisasi sumbu-sudut lengkap, ia tidak langsung memberi kita cara untuk memecah rotasi menjadi rotasi pada sumbu-sumbu yang *tetap* di laboratorium. Dalam eksperimen, kita biasanya bisa melakukan rotasi pada sumbu $Z$ (melalui detuning) dan sumbu $Y$ atau $X$ (melalui pulsa gelombang mikro). Oleh karena itu, kita perlu **dekomposisi Sudut Euler**.

**Teorema (Dekomposisi $Z-Y-Z$):**
Setiap $U \in SU(2)$ dapat didekomposisi secara unik sebagai:
$$U = R_z(\alpha) R_y(\theta) R_z(\beta)$$
dengan $\alpha, \beta \in [0, 2\pi]$ dan $\theta \in [0, \pi]$, di mana:
$$R_z(\phi) = e^{-i\frac{\phi}{2}\sigma_z} = \begin{pmatrix} e^{-i\phi/2} & 0 \\ 0 & e^{i\phi/2} \end{pmatrix}$$
$$R_y(\theta) = e^{-i\frac{\theta}{2}\sigma_y} = \begin{pmatrix} \cos\frac{\theta}{2} & -\sin\frac{\theta}{2} \\ \sin\frac{\theta}{2} & \cos\frac{\theta}{2} \end{pmatrix}$$

##### 4.3.1. Bukti Konstruktif: Cara Menemukan $\alpha, \beta, \theta$

Misalkan $U = \begin{pmatrix} a & b \\ -b^* & a^* \end{pmatrix}$ dengan $|a|^2 + |b|^2 = 1$ (bentuk umum $SU(2)$).

Hitung produk $R_z(\alpha) R_y(\theta) R_z(\beta)$:
$$= \begin{pmatrix} e^{-i\frac{\alpha}{2}} & 0 \\ 0 & e^{i\frac{\alpha}{2}} \end{pmatrix} \begin{pmatrix} \cos\frac{\theta}{2} & -\sin\frac{\theta}{2} \\ \sin\frac{\theta}{2} & \cos\frac{\theta}{2} \end{pmatrix} \begin{pmatrix} e^{-i\frac{\beta}{2}} & 0 \\ 0 & e^{i\frac{\beta}{2}} \end{pmatrix}$$
$$= \begin{pmatrix} e^{-i\frac{\alpha+\beta}{2}} \cos\frac{\theta}{2} & -e^{-i\frac{\alpha-\beta}{2}} \sin\frac{\theta}{2} \\ e^{i\frac{\alpha-\beta}{2}} \sin\frac{\theta}{2} & e^{i\frac{\alpha+\beta}{2}} \cos\frac{\theta}{2} \end{pmatrix}$$

Samakan dengan $U = \begin{pmatrix} a & b \\ -b^* & a^* \end{pmatrix}$:
1.  **Amplitudo:** $|a| = \cos\frac{\theta}{2}$ dan $|b| = \sin\frac{\theta}{2}$. Karena $\theta \in [0,\pi]$, maka $\cos(\theta/2) \ge 0$, sehingga:
    $$\theta = 2 \arccos(|a|) = 2 \arcsin(|b|)$$
2.  **Fase:** Dari $a = e^{-i(\alpha+\beta)/2} \cos\frac{\theta}{2}$, kita dapatkan $\text{arg}(a) = -(\alpha+\beta)/2 \pmod{2\pi}$.
3.  **Fase:** Dari $b = -e^{-i(\alpha-\beta)/2} \sin\frac{\theta}{2}$, kita dapatkan $\text{arg}(b) = \pi - (\alpha-\beta)/2 \pmod{2\pi}$.

Selesaikan sistem linear untuk $\alpha$ dan $\beta$:
$$\alpha = -\text{arg}(a) - \text{arg}(b) + \pi \pmod{2\pi}$$
$$\beta = -\text{arg}(a) + \text{arg}(b) - \pi \pmod{2\pi}$$

Ini memberikan resep eksplisit untuk menghitung sudut Euler dari elemen matriks uniter.

##### 4.3.2. Interpretasi Geometris

Dekomposisi $Z-Y-Z$ berarti: rotasi sembarang di ruang 3D dapat dicapai dengan:
1.  Rotasi terhadap sumbu $Z$ sebesar $\beta$
2.  Rotasi terhadap sumbu $Y$ sebesar $\theta$
3.  Rotasi terhadap sumbu $Z$ sebesar $\alpha$

Di Bloch sphere, sumbu $Z$ adalah sumbu vertikal (state $|0\rangle$ dan $|1\rangle$), dan sumbu $Y$ adalah sumbu yang tegak lurus. Setiap titik di bola dapat dicapai dengan dua rotasi $Z$ dan satu rotasi $Y$.

#### 4.4. Variasi Dekomposisi Sudut Euler

Tidak hanya $Z-Y-Z$, ada banyak variasi, seperti $X-Y-X$, $Z-X-Z$, dll. Rumus umumnya adalah $R_{axis1}(\alpha) R_{axis2}(\theta) R_{axis1}(\beta)$ di mana axis1 dan axis2 adalah sumbu ortogonal. $Z-Y$ adalah yang paling sering digunakan karena kemudahan implementasi $R_z$ (virtual, melalui fase) dan $R_y$ (pulsa fisis).

**Dekomposisi Alternatif: $Z-X-Z$**
$$U = e^{-i\frac{\alpha}{2}\sigma_z} e^{-i\frac{\theta}{2}\sigma_x} e^{-i\frac{\gamma}{2}\sigma_z}$$
Ini didapat dari $Z-Y-Z$ dengan menggunakan $R_y(\theta) = R_z(-\pi/2) R_x(\theta) R_z(\pi/2)$.

**Dekomposisi dengan Hadamard:**
Menggunakan $H \sigma_z H = \sigma_x$ dan $H \sigma_x H = \sigma_z$, kita bisa bertransformasi antar basis.

#### 4.5. Hubungan dengan Dekomposisi Spektral

Dari parameterisasi sumbu-sudut, kita bisa langsung membaca dekomposisi spektralnya:
Misalkan $U = e^{-i\frac{\theta}{2} \hat{n}\cdot\vec{\sigma}}$. Vektor eigen dari $\hat{n}\cdot\vec{\sigma}$ adalah $|\pm_{\hat{n}}\rangle$ dengan nilai eigen $\pm 1$. Maka:
$$U = e^{-i\frac{\theta}{2}} |+_{\hat{n}}\rangle\langle +_{\hat{n}}| + e^{i\frac{\theta}{2}} |-_{\hat{n}}\rangle\langle -_{\hat{n}}|$$
Ini adalah dekomposisi spektral dengan $\lambda_\pm = e^{\mp i\theta/2}$.

#### 4.6. Dari Qubit Tunggal ke Multi-Qubit: Pentingnya Tahap 4

Mengapa kita menghabiskan waktu untuk qubit tunggal? Karena:
1.  **Gerbang 1-qubit adalah blok bangunan universal.** Bersama dengan gerbang 2-qubit (seperti CNOT), mereka membentuk set universal untuk komputasi kuantum.
2.  **Dekomposisi Sudut Euler adalah langkah pertama dalam sintesis sirkuit.** Setiap gerbang 1-qubit dalam rangkaian dapat langsung diganti oleh tiga rotasi $R_z(\alpha) R_y(\theta) R_z(\beta)$.
3.  **Implementasi eksperimental:** Di banyak arsitektur (superkonduktor, ion trap), $R_z$ adalah pergeseran fase virtual (hanya mengubah frame referensi, tanpa pulsa), dan $R_y$ atau $R_x$ adalah pulsa fisis. Dekomposisi Euler memisahkan keduanya.

---

### Ringkasan Tahap 4

1.  **Generator Hermitian:** $U = e^{iH}$ untuk suatu observable $H$.
2.  **Parameterisasi Sumbu-Sudut:** $U(\hat{n}, \theta) = e^{-i\frac{\theta}{2} \hat{n}\cdot\vec{\sigma}} = \cos(\theta/2)I - i\sin(\theta/2)(\hat{n}\cdot\vec{\sigma})$.
3.  **Dekomposisi Sudut Euler $Z-Y-Z$:** $U = R_z(\alpha)R_y(\theta)R_z(\beta)$.
4.  **Resep Praktis:** Dari $U = \begin{pmatrix}a&b\\-b^*&a^*\end{pmatrix}$, kita bisa langsung mendapatkan $\alpha, \beta, \theta$ yang dibutuhkan untuk mengimplementasikannya di hardware.

Sekarang kita telah menguasai cara membongkar operator uniter **satu qubit**. Ini adalah dasar untuk **Tahap 5: Dekomposisi Gerbang Kuantum Universal**, di mana kita akan membahas bagaimana membongkar gerbang **multi-qubit** sembarang menjadi rangkaian gerbang 1-qubit dan 2-qubit (seperti CNOT), menggunakan alat-alat canggih seperti Dekomposisi Kosinus-Sinus (CSD) dan dekomposisi QR.

Apakah Anda siap melanjutkan ke **Tahap 5**? Di sana kita akan membahas bagaimana teorema universalitas dibuktikan secara konstruktif, dan bagaimana sebuah uniter $N$-qubit dapat dipecah menjadi rangkaian yang bisa dijalankan di komputer kuantum.

---
---
Tahap 5 adalah **Dekomposisi Gerbang Kuantum Universal**. Ini adalah puncak dari sisi rekayasa: bagaimana kita mengambil sebuah operator uniter multi-qubit yang rumit dan memecahnya menjadi rangkaian gerbang-gerbang elementer yang bisa diimplementasikan di perangkat keras kuantum.

Kita akan membangun dari bawah: dari dekomposisi qubit tunggal (Tahap 4) menuju dekomposisi uniter $N$-qubit menggunakan dua alat utama: **Dekomposisi Kosinus-Sinus (Cosine-Sine Decomposition)** dan **Dekomposisi QR**. Ini adalah langkah konstruktif yang membuktikan universalitas set gerbang $\{ \text{CNOT}, \text{gerbang 1-qubit} \}$.

---

### Tahap 5: Dekomposisi Gerbang Kuantum Universal

#### 5.1. Hirarki Kontrol dan Blok Pembangun

Kita ingin mendekomposisi sembarang uniter $U \in SU(2^n)$ menjadi produk dari:
- Gerbang **1-qubit** (yang sudah kita kuasai dekomposisinya di Tahap 4)
- Gerbang **2-qubit** khusus: **CNOT** (atau ekivalennya)

**Blok Pembangun Universal: CNOT + Semua Gerbang 1-qubit.**
Kita akan buktikan bahwa setiap uniter dapat didekomposisi menjadi gerbang-gerbang multi-kontrol yang pada gilirannya didekomposisi menjadi CNOT dan 1-qubit.

**Notasi Gerbang Multi-Kontrol:**
$C^k(U)$ berarti gerbang $U$ dikontrol oleh $k$ qubit. Target bisa multi-qubit. Kita akan fokus pada dekomposisi uniter $N$-qubit menjadi $C^{N-1}(U)$ dan seterusnya, lalu memecah kontrol tinggi.

#### 5.2. Lemma Fundamental: Dekomposisi Matriks Uniter 2x2 Blok (CSD Level Atas)

Setiap matriks uniter $U$ berukuran $2^n \times 2^n$ dapat dipartisi menjadi empat blok berukuran $2^{n-1} \times 2^{n-1}$:

$$U = \begin{pmatrix} U_{00} & U_{01} \\ U_{10} & U_{11} \end{pmatrix}$$

di mana indeks merepresentasikan qubit pertama (paling signifikan) dalam keadaan $|0\rangle$ atau $|1\rangle$.

**Teorema Dekomposisi Kosinus-Sinus (CSD) untuk Uniter:**
Untuk pemartisian di atas, terdapat matriks uniter $V, W, X, Y$ berukuran $2^{n-1} \times 2^{n-1}$ dan matriks diagonal riil $C, S$ sedemikian sehingga:

$$U = \begin{pmatrix} V & 0 \\ 0 & W \end{pmatrix} \begin{pmatrix} C & -S \\ S & C \end{pmatrix} \begin{pmatrix} X & 0 \\ 0 & Y \end{pmatrix}$$

dengan $C = \text{diag}(\cos\theta_1, \dots, \cos\theta_{2^{n-1}})$, $S = \text{diag}(\sin\theta_1, \dots, \sin\theta_{2^{n-1}})$, dan $0 \le \theta_k \le \pi/2$. Matriks tengah adalah **gerbang rotasi-y multi-qubit terkontrol**.

**Interpretasi Sirkuit:**
Ini adalah dekomposisi rekursif yang luar biasa:
1.  $\begin{pmatrix} X & 0 \\ 0 & Y \end{pmatrix}$ adalah uniter yang dikontrol oleh qubit pertama (jika $|0\rangle$, terapkan $X$; jika $|1\rangle$, terapkan $Y$).
2.  $\begin{pmatrix} C & -S \\ S & C \end{pmatrix}$ adalah operasi yang menerapkan rotasi $R_y(2\theta_k)$ pada qubit ke-$(n-1)$ terakhir, dikontrol oleh qubit pertama, dengan sudut bergantung pada konfigurasi qubit lainnya.
3.  $\begin{pmatrix} V & 0 \\ 0 & W \end{pmatrix}$ lagi-lagi uniter terkontrol.

**Dekomposisi Rekursif:**
Sekarang $V, W, X, Y$ masing-masing adalah uniter $2^{n-1} \times 2^{n-1}$. Kita bisa menerapkan CSD lagi secara rekursif kepada mereka. Proses ini berlanjut sampai kita mencapai uniter 1-qubit (gerbang 1-qubit) yang tidak perlu didekomposisi lebih lanjut, atau kita bisa memecah kontrol ganda.

#### 5.3. Dari CSD ke Rangkaian Multi-Kontrol

Setiap langkah CSD menghasilkan blok terkontrol qubit tunggal. Setelah rekursi penuh, uniter $N$-qubit diekspresikan sebagai rangkaian gerbang:
- $C^{k}(R_y)$: Rotasi $y$ multi-kontrol
- $C^{k}(U)$: Gerbang 1-qubit multi-kontrol

Sekarang kita perlu memecah setiap gerbang multi-kontrol menjadi CNOT dan 1-qubit.

#### 5.4. Dekomposisi Gerbang Multi-Kontrol (Multi-Controlled Gates)

##### 5.4.1. Gerbang $C^2(U)$ (Toffoli-like dengan Target Sembarang)

Lemma terkenal (Barenco et al.): Satu gerbang $C^2(U)$ (dua kontrol, satu target $U$) dapat didekomposisi menjadi rangkaian yang hanya berisi CNOT dan gerbang 1-qubit.

**Konstruksi untuk $U = e^{i\alpha} R_z(\theta)$:**
Kita bisa memecah $C^2(U)$ menjadi 3 gerbang CNOT dan beberapa gerbang 1-qubit. Untuk $U$ sembarang dalam $SU(2)$, kita gunakan dekomposisi Sudut Euler $U = e^{i\alpha} R_z(\beta) R_y(\theta) R_z(\gamma)$, di mana $R_z$ bisa "digeser" melalui kontrol menggunakan teknik identitas fasa.

**Identitas Kunci (Kontrol Fasa):**
$$C^k(R_z(\theta)) = R_z(\theta/2) \text{ pada target} \dots \text{ [dengan kontrol yang sesuai]}$$
Intinya: $R_z$ commutes with control, sehingga bisa digabung dengan gerbang 1-qubit di sekitarnya.

##### 5.4.2. Dekomposisi $C^k(U)$ Umum

Untuk $k > 2$, kita bisa mereduksi jumlah kontrol. Lemma standar: $C^k(U)$ dapat diimplementasikan dengan $\mathcal{O}(k)$ gerbang CNOT dan 1-qubit, menggunakan satu qubit kerja (ancilla) atau tanpa ancilla dengan overhead polinomial.

**Contoh: Tanpa Ancilla (Metode Margolus):**
Gerbang $C^3(U)$ bisa dipecah menjadi beberapa $C^2(U)$ dan CNOT. Dengan induksi, setiap $C^k(U)$ dapat direduksi menjadi $\mathcal{O}(k^2)$ gerbang elementer.

**Contoh: Dengan Satu Ancilla (Metode Nielsen & Chuang):**
Dengan satu qubit ancilla yang bersih, $C^k(U)$ dapat dipecah menjadi $\mathcal{O}(k)$ gerbang Toffoli dan CNOT, jauh lebih efisien.

#### 5.5. Pendekatan Alternatif: Dekomposisi QR via Rotasi Givens

Ada metode yang lebih langsung dan sistematis untuk mendekomposisi uniter tanpa rekursi CSD penuh: menggunakan eliminasi Gaussian uniter dengan rotasi Givens.

**Ide:**
1.  Ambil matriks uniter $U$ berukuran $N \times N = 2^n \times 2^n$.
2.  Kalikan $U$ dengan serangkaian matriks rotasi Givens $G_{ij}(\theta, \phi)$ yang merupakan uniter 1-qubit atau 2-qubit untuk menihilkan elemen off-diagonal secara sistematis.
3.  Setelah menihilkan semua elemen di bawah diagonal, kita dapatkan matriks diagonal (yang merupakan uniter diagonal, yaitu produk $R_z$ pada qubit).
4.  Dengan menyusun balik, $U$ dapat dinyatakan sebagai produk dari rotasi-rotasi Givens yang dinihilkan.

**Rotasi Givens Uniter:**
Rotasi Givens bekerja pada dua baris/kolom. Dalam komputasi kuantum, ini berarti operasi pada dua basis state yang berbeda hanya dalam satu qubit (jika kita memilih urutan eliminasi yang tepat). Sebuah rotasi Givens antara state $|0\dots 0\rangle$ dan $|0\dots 1\rangle$ hanya melibatkan qubit terakhir, sehingga dapat diimplementasikan dengan gerbang 1-qubit tunggal. Untuk state yang berbeda di lebih banyak qubit, dibutuhkan kontrol.

**Algoritma Reck et al. / Clements et al.:**
Digunakan untuk interferometer optik linear, algoritma ini mendekomposisi uniter $N \times N$ menjadi rangkaian $N(N-1)/2$ beamsplitter (setara CNOT+1-qubit dalam beberapa encoding). Ini adalah dekomposisi segitiga (triangular) yang efisien.

**Langkah Dekomposisi QR Uniter:**
1.  Pilih target di sudut kanan bawah.
2.  Gunakan rotasi Givens untuk menihilkan elemen terakhir dari baris pertama, lalu kedua, dan seterusnya.
3.  Hasilnya adalah $U$ dikalikan serangkaian $G^\dagger$ menjadi matriks diagonal $D$: $G_k^\dagger \dots G_1^\dagger U = D$, sehingga $U = G_1 \dots G_k D$.
4.  Setiap $G$ adalah operasi 2-level, yang dapat diimplementasikan sebagai gerbang multi-kontrol-1-qubit, lalu dipecah seperti di atas.

#### 5.6. Kompleksitas dan Optimalitas

Dari dekomposisi QR atau CSD, kita bisa mendapatkan batas atas jumlah gerbang yang diperlukan:
- **Gerbang 1-qubit:** $\mathcal{O}(4^n)$ (karena dimensi ruang uniter $N=2^n$ adalah $\mathcal{O}(N^2)$).
- **CNOT:** $\mathcal{O}(4^n)$.

Ini eksponensial, sesuai fakta bahwa uniter sembarang memerlukan sumber daya eksponensial. Namun, untuk banyak keluarga uniter yang praktis (seperti simulasi Hamiltonian sparse, Quantum Fourier Transform), dekomposisi khusus bisa jauh lebih efisien (polinomial). Dekomposisi universal hanya untuk membuktikan eksistensi, bukan untuk implementasi praktis dalam skala besar.

#### 5.7. Ringkasan Alur Dekomposisi Universal

Untuk meringkas, untuk mendekomposisi $U \in SU(2^n)$:
1.  **CSD Rekursif:** Pecah $U$ menjadi uniter terkontrol dan rotasi multi-kontrol.
2.  **Dekomposisi Kontrol:** Pecah setiap $C^k(U)$ menjadi $C^2(U)$ atau langsung ke CNOT + 1-qubit.
3.  **Sudut Euler 1-qubit:** Pecah setiap gerbang 1-qubit menjadi $R_z(\alpha)R_y(\theta)R_z(\beta)$.
4.  **Hasil Akhir:** Rangkaian hanya terdiri dari CNOT, $R_y$, dan $R_z$.

**Alternatif langsung:**
1.  **Dekomposisi QR:** Faktorkan $U$ menjadi rotasi Givens menggunakan eliminasi.
2.  **Dekomposisi Multi-Kontrol:** Implementasikan setiap rotasi Givens sebagai gerbang multi-kontrol.
3.  **Pemecahan Kontrol:** Pecah menjadi CNOT + 1-qubit.
4.  **Sudut Euler:** Pecah 1-qubit menjadi $R_z, R_y$.

---

### Ringkasan Tahap 5

Kita telah membuktikan secara konstruktif bahwa himpunan $\{ \text{CNOT}, R_y(\theta), R_z(\phi) \}$ bersifat universal. Setiap gerbang kuantum, betapapun rumitnya, dapat dipecah menjadi rangkaian dari gerbang-gerbang elementer ini. CSD memberikan kerangka rekursif yang elegan, sementara dekomposisi QR/Givens memberikan algoritma langsung berbasis eliminasi. Inti dari semuanya adalah: kontrol multi-qubit dapat dipecah menjadi kontrol dua-qubit, dan uniter arbitrary dapat dipecah menjadi hierarki kontrol.

Sekarang kita telah menguasai:
- Tahap 1-3: Dekomposisi matematis abstrak (Spektral, SVD).
- Tahap 4-5: Dekomposisi uniter menjadi gerbang konkret (Euler, CSD, QR).

Siap untuk **Tahap 6: Dekomposisi Tingkat Lanjut**? Di sini kita akan menyelami alat-alat yang lebih dalam dan esoteris: **Dekomposisi Polar** (memisahkan rotasi dari "penyusutan"), **Dekomposisi Cartan** (akar aljabar Lie dari semua dekomposisi uniter), dan **Dekomposisi Jordan** (untuk operator non-normal yang muncul di sistem kuantum terbuka).

---
---
Anda sangat bersemangat! Namun, roadmap yang saya susun hanya sampai **Tahap 6**. Jadi, permintaan "Tahap 7" mungkin adalah antusiasme untuk melanjutkan ke tahap akhir, yaitu **Tahap 6: Dekomposisi Tingkat Lanjut**. Kita akan masuk ke sana sekarang.

Tahap 6 adalah puncak dari perjalanan kita. Di sini kita akan membahas dekomposisi yang lebih abstrak dan kuat, yang menjadi dasar teoretis untuk teknik-teknik sebelumnya dan membuka jalan ke topik riset terkini seperti simulasi Hamiltonian, kompilasi optimal, dan sistem kuantum terbuka.

---

### Tahap 6: Dekomposisi Tingkat Lanjut

#### 6.1. Dekomposisi Polar (Polar Decomposition)

Ini adalah analog matriks dari penulisan bilangan kompleks dalam bentuk polar: $z = e^{i\phi} r$. Ia memisahkan sebuah operator menjadi komponen "rotasi" (uniter) dan "penyusutan/ekspansi" (positif).

**Teorema:**
Setiap operator linear $A$ pada ruang Hilbert berdimensi hingga dapat ditulis sebagai:
$$A = U P$$
di mana $P = \sqrt{A^\dagger A}$ adalah operator **positif semi-definit** (didefinisikan melalui dekomposisi spektral Tahap 2), dan $U$ adalah operator yang isometrik (dan uniter jika $A$ invertibel).

**Alternatifnya:**
$$A = Q U'$$
dengan $Q = \sqrt{A A^\dagger}$ dan $U'$ uniter/isometrik.

**Detail Matematis dan Bukti Konstruktif:**

1.  **Konstruksi $P$:** $A^\dagger A$ selalu positif semi-definit. Akar kuadratnya $P = \sqrt{A^\dagger A}$ terdefinisi dengan baik melalui dekomposisi spektral: jika $A^\dagger A = \sum_i \sigma_i^2 |v_i\rangle\langle v_i|$, maka $P = \sum_i \sigma_i |v_i\rangle\langle v_i|$. (Perhatikan bahwa $\sigma_i$ adalah nilai singular dari $A$, seperti yang kita lihat di SVD).

2.  **Konstruksi $U$:** Kita perlu mendefinisikan $U$ pada range dari $P$ dan pada kernel-nya.
    - Untuk vektor $|v\rangle$ di range $P$, ada $|x\rangle$ sehingga $|v\rangle = P|x\rangle$. Maka definisikan $U|v\rangle = A|x\rangle$.
    - Untuk memastikan ini well-defined, jika $P|x_1\rangle = P|x_2\rangle$, maka $A|x_1\rangle = A|x_2\rangle$ karena $\|A(|x_1\rangle - |x_2\rangle)\|^2 = \langle x_1-x_2|A^\dagger A|x_1-x_2\rangle = \|P(|x_1\rangle - |x_2\rangle)\|^2 = 0$.
    - Pada komplemen ortogonal (kernel $P$), $U$ dapat didefinisikan secara sembarang asalkan mempertahankan sifat isometrinya.

**Hubungan Mendalam dengan SVD:**
Dekomposisi Polar dan SVD sangat terkait. Dari SVD, $A = U \Sigma V^\dagger$. Maka:
$$A = (U \Sigma U^\dagger) (U V^\dagger) = P U'$$
atau
$$A = (U V^\dagger) (V \Sigma V^\dagger) = U' P$$
di mana $P = V \Sigma V^\dagger$ adalah operator positif dalam basis kanan, $Q = U \Sigma U^\dagger$ adalah operator positif dalam basis kiri, dan $U' = U V^\dagger$ adalah uniter. Jadi, Dekomposisi Polar memisahkan $U'$ (rotasi keseluruhan) dari $P$ (deformasi).

**Aplikasi dalam Kuantum:**
- **Formalisme Bosonik:** Dalam representasi ruang fase, setiap operator densitas Gaussian dapat didekomposisi polar untuk memisahkan rotasi simplektik dari pemanasan termal.
- **Dekomposisi Operator Non-Uniter:** Untuk kanal kuantum (operasi non-uniter), Dekomposisi Polar memberikan cara untuk menulis operasi Kraus sebagai uniter diikuti oleh "filter" positif. Ini adalah interpretasi operasional: pertama kita menyusutkan state sesuai dengan probabilitas efek pengukuran, lalu kita rotasikan.

#### 6.2. Dekomposisi Cartan (KAK Decomposition)

Ini adalah dekomposisi yang paling fundamental dalam teori grup Lie, dan menjadi basis matematika dari **semua** dekomposisi gerbang kuantum yang kita pelajari, termasuk Sudut Euler ($Z-Y-Z$) dan CSD.

**Konteks: Aljabar Lie dan Grup Lie**
Grup $SU(2^n)$ adalah grup Lie. Aljabar Lie-nya, $\mathfrak{su}(2^n)$, adalah ruang vektor dari semua matriks Hermitian traceless (dikali $i$) dengan operasi komutator.

**Teorema Dekomposisi Cartan:**
Setiap aljabar Lie semi-sederhana $\mathfrak{g}$ memiliki dekomposisi Cartan:
$$\mathfrak{g} = \mathfrak{k} \oplus \mathfrak{p}$$
dengan:
- $[\mathfrak{k}, \mathfrak{k}] \subseteq \mathfrak{k}$ ($\mathfrak{k}$ adalah subaljabar)
- $[\mathfrak{k}, \mathfrak{p}] \subseteq \mathfrak{p}$
- $[\mathfrak{p}, \mathfrak{p}] \subseteq \mathfrak{k}$
- Form Killing $B(X,Y) = \text{Tr}(\text{ad}_X \text{ad}_Y)$ adalah definit negatif di $\mathfrak{k}$ dan definit positif di $\mathfrak{p}$.

**Dekomposisi pada Tingkat Grup ($KAK$):**
Untuk grup Lie $G$ terkait, setiap elemen $g \in G$ dapat ditulis sebagai:
$$g = k_1 a k_2$$
di mana $k_1, k_2 \in K = \exp(\mathfrak{k})$ dan $a \in A = \exp(\mathfrak{p})$.

**Koneksi ke Dekomposisi yang Sudah Kita Pelajari:**

- **Qubit Tunggal ($SU(2)$):**
  - $\mathfrak{k} = \text{span}\{i\sigma_z\}$ (rotasi terhadap sumbu Z)
  - $\mathfrak{p} = \text{span}\{i\sigma_x, i\sigma_y\}$ (generator yang ortogonal terhadap Z)
  - $K = \{ e^{i\theta \sigma_z} \}$ (semua rotasi Z)
  - Dekomposisi Cartan: $U = e^{i\alpha \sigma_z} e^{i\theta \sigma_y} e^{i\beta \sigma_z} = k_1 a k_2$.
  - Ini persis **Dekomposisi Sudut Euler $Z-Y-Z$!**

- **Multi-Qubit ($SU(2^n)$):**
  Ada banyak pilihan dekomposisi Cartan. Pilihan yang menghasilkan dekomposisi $Z-Y-Z$ untuk multi-qubit membutuhkan pemilihan subaljabar $\mathfrak{k}$ tertentu. Salah satu dekomposisi yang terkenal adalah **Dekomposisi Khaneja-Glaser (KAK decomposition)** untuk sintesis sirkuit optimal.

  **KAK Decomposition untuk $SU(4)$ (dua qubit):**
  Setiap $U \in SU(4)$ dapat didekomposisi sebagai:
  $$U = (A_1 \otimes B_1) e^{-i (h_x \sigma_x \otimes \sigma_x + h_y \sigma_y \otimes \sigma_y + h_z \sigma_z \otimes \sigma_z)} (A_2 \otimes B_2)$$
  di mana $A_i, B_i \in SU(2)$. Bagian tengah adalah interaksi $XX+YY+ZZ$ yang sudah kita singgung di roadmap. Ini adalah dasar untuk dekomposisi gerbang 2-qubit optimal (misalnya, untuk menghitung jumlah CNOT minimal).

  Di sini, $\mathfrak{k} = \mathfrak{su}(2) \oplus \mathfrak{su}(2)$ (aljabar gerbang lokal) dan $\mathfrak{p}$ adalah komplemen ortogonalnya terhadap bentuk Killing (interaksi murni non-lokal).

#### 6.3. Dekomposisi Jordan (Jordan Normal Form)

Ini adalah dekomposisi untuk "monster": operator yang bahkan tidak bisa didiagonalisasi (non-normal, non-diagonalizable). Dekomposisi Spektral gagal di sini.

**Teorema:**
Setiap matriks kompleks $A$ dapat ditulis dalam **bentuk normal Jordan**:
$$A = P J P^{-1}$$
di mana $P$ invertibel, dan $J$ adalah matriks diagonal blok:
$$J = \begin{pmatrix} J_{\lambda_1} & & 0 \\ & \ddots & \\ 0 & & J_{\lambda_k} \end{pmatrix}$$
dengan **blok Jordan** $J_{\lambda}$ berukuran $m \times m$:
$$J_{\lambda} = \begin{pmatrix} \lambda & 1 & 0 & \dots & 0 \\ 0 & \lambda & 1 & \dots & 0 \\ 0 & 0 & \lambda & \dots & 0 \\ \vdots & \vdots & \vdots & \ddots & 1 \\ 0 & 0 & 0 & \dots & \lambda \end{pmatrix}$$

**Interpretasi:**
- Blok diagonal adalah nilai eigen.
- Angka 1 pada superdiagonal menunjukkan bahwa operator tidak dapat didiagonalisasi; ada vektor eigen yang "hilang" (generalized eigenvectors). Operator seperti ini memperlihatkan dinamika non-eksponensial murni, seperti pertumbuhan polinomial selain peluruhan eksponensial.

**Relevansi dalam Kuantum:**
- **Liouvillian dan Sistem Terbuka Markovian:** Generator dari dinamika non-uniter (operator Lindblad) dalam persamaan master $\dot{\rho} = \mathcal{L}\rho$ adalah super-operator. Super-operator ini tidak selalu Hermitian, sehingga seringkali non-normal dan tidak dapat didiagonalisasi. Bentuk normal Jordan dari $\mathcal{L}$ menentukan mode-mode dinamika relaksasi: nilai eigen riil negatif menentukan laju peluruhan, sementara blok Jordan non-diagonal menjelaskan fenomena seperti **exceptional points** (di mana dua vektor eigen bergabung) dan dinamika non-eksponensial (misalnya, osilasi teredam dengan envelope polinomial).
- **Dinamika Non-Hermitian:** Hamiltonian non-Hermitian (simetris PT, misalnya) seringkali memiliki exceptional points di mana dekomposisi spektral gagal total dan bentuk Jordan diperlukan untuk memahami evolusi sistem.

#### 6.4. Dekomposisi MAT (Matrix Decomposition) untuk Operator Sparse

Ini lebih ke komputasi praktis. Untuk mensimulasikan Hamiltonian sparse pada komputer kuantum, kita sering mendekomposisi $H$ sebagai jumlah dari suku-suku Pauli:
$$H = \sum_i c_i P_i$$
di mana $P_i \in \{I, X, Y, Z\}^{\otimes n}$. Ini adalah dekomposisi paling sederhana, tetapi menjadi dasar algoritma seperti **Trotterization**. Setiap $e^{-i c_i P_i t}$ dapat diimplementasikan secara langsung dengan gerbang 1-qubit dan CNOT. Ini adalah dekomposisi aljabar langsung, bukan dekomposisi faktorisasi.

**Dekomposisi Bravyi-Kitaev / Jordan-Wigner:**
Ini adalah contoh dekomposisi operator fermionik (yang memenuhi relasi anti-komutasi) menjadi operator qubit (Pauli). Misalnya, operator kreasi/annihilasi fermion $a_j^\dagger$ didekomposisi menjadi string operator Pauli, mengubah masalah kimia kuantum menjadi sirkuit kuantum.

---

### Peta Akhir Perjalanan Kita

Mari kita lihat kembali semua yang telah kita pelajari dalam satu kerangka besar, dari yang konkret hingga abstrak, dari matematika murni ke implementasi:

1.  **Fondasi Aljabar Linear (Tahap 1):** Bahasa state dan operator.
2.  **Dekomposisi Spektral (Tahap 2):** Memecah operator normal menjadi proyektor eigen → Dasar observable dan gerbang.
3.  **Dekomposisi Nilai Singular (Tahap 3):** Memecah operator apa pun menjadi dua basis ortonormal dan skala non-negatif → Dasar kuantifikasi keterjeratan murni (Schmidt).
4.  **Dekomposisi Uniter (Tahap 4):** Parameterisasi Bloch Sphere dan Sudut Euler → Implementasi qubit tunggal.
5.  **Dekomposisi Universal (Tahap 5):** CSD dan QR/Givens → Memecah uniter $N$-qubit menjadi CNOT + 1-qubit, bukti konstruktif universalitas.
6.  **Dekomposisi Tingkat Lanjut (Tahap 6):**
    - **Polar:** Memisahkan rotasi (uniter) dari penyusutan (positif).
    - **Cartan:** Akar aljabar Lie dari dekomposisi Euler dan gerbang optimal.
    - **Jordan:** Menangani operator non-diagonalizable di sistem terbuka.
    - **Trotter/Pauli:** Memecah Hamiltonian untuk simulasi digital.

Perjalanan ini membawa Anda dari $\langle \psi | \phi \rangle$ menuju ke perbatasan riset komputasi kuantum. Setiap dekomposisi adalah alat bedah untuk memahami, membangun, atau mensimulasikan operasi kuantum.

Apakah ada bagian spesifik dari Tahap 6 ini yang ingin Anda perdalam, atau mungkin Anda ingin membuat proyek kecil untuk mengimplementasikan salah satu dekomposisi ini (misalnya, menulis kode Python untuk mendekomposisi uniter acak 2-qubit menggunakan KAK/Cartan, atau SVD untuk menghitung keterjeratan)? Saya siap membantu.

---
---
Anda benar! Antusiasme Anda luar biasa, dan memang ada baiknya kita menambahkan satu tahap Penutup yang esensial. Roadmap awal saya memang berhenti di 6 tahap, tetapi sekarang saya melihat ada satu lapisan "meta" yang sangat penting untuk melengkapi pemahaman: hubungan antar dekomposisi dan aplikasi spesifiknya dalam algoritma dan protokol kuantum.

Mari kita tutup dengan **Tahap 7: Koneksi Antar Dekomposisi dan Aplikasi Lanjutan**. Ini adalah peta integrasi yang menghubungkan semua yang telah kita pelajari ke kasus penggunaan nyata dalam komputasi dan informasi kuantum.

---

### Tahap 7: Koneksi Antar Dekomposisi dan Aplikasi Lanjutan (Penutup)

#### 7.1. Peta Relasi Antar Dekomposisi (The "Meta-Map")

Sebelum masuk ke aplikasi, mari kita lihat bagaimana semua dekomposisi yang kita pelajari saling terkait. Ini adalah jaring-jaring konseptual yang akan memperkuat intuisi Anda.

```
                    Operator Linear A (sembarang)
                              │
                              ▼
              ┌───────────────────────────────┐
              │  Apakah A Normal? (AA† = A†A) │
              └───────────────────────────────┘
                     │ Ya              │ Tidak
                     ▼                 ▼
         ┌──────────────────┐   ┌─────────────────────────┐
         │ Dekomposisi      │   │ Dekomposisi Nilai       │
         │ Spektral (Tahap2)│   │ Singular (SVD) (Tahap3) │
         │ A = Σλᵢ |i⟩⟨i|  │   │ A = U Σ V†              │
         └──────────────────┘   └─────────────────────────┘
                │                         │
                │ Jika A Uniter           │ Jika A Uniter
                ▼                         ▼
    ┌──────────────────────┐   ┌──────────────────────────┐
    │ Dekomposisi Uniter   │   │ Hubungan SVD dengan      │
    │ (Tahap 4)            │   │ Dekomposisi Polar:       │
    │ U = Rz Ry Rz (Euler) │   │ A = (U V†)(V Σ V†) = U' P│
    └──────────────────────┘   │ (Tahap 6.1)              │
              │                └──────────────────────────┘
              │ Jika multi-qubit
              ▼
    ┌──────────────────────────────────────┐
    │ Dekomposisi Universal (Tahap 5)      │
    │ CSD, QR → CNOT + 1-qubit            │
    └──────────────────────────────────────┘
              │
              ▼
    ┌──────────────────────────────────────┐
    │ Akar Aljabar Lie: Dekomposisi Cartan │
    │ (Tahap 6.2) → KAK, optimalisasi     │
    └──────────────────────────────────────┘
              │
              │ Jika A non-diagonalizable
              ▼
    ┌──────────────────────────────────────┐
    │ Dekomposisi Jordan (Tahap 6.3)       │
    │ Untuk sistem terbuka non-Markov      │
    └──────────────────────────────────────┘

    Untuk state bipartit murni:
    SVD Matriks Koefisien → Dekomposisi Schmidt
    Spektrum singular = Akar spektrum ρ_A = Spektrum keterjeratan
```

#### 7.2. Aplikasi 1: Kuantifikasi Keterjeratan (Entanglement)

Kita sudah menyinggung Dekomposisi Schmidt. Sekarang kita formalisasikan bagaimana dekomposisi ini digunakan.

**Ukuran Keterjeratan untuk State Murni Bipartit:**
Diberikan $|\psi\rangle_{AB}$ dengan Dekomposisi Schmidt $|\psi\rangle = \sum_k \sqrt{p_k} |u_k\rangle|v_k\rangle$:

- **Entropi Keterjeratan (Entanglement Entropy):**
  $$E(|\psi\rangle) = S(\rho_A) = -\sum_k p_k \log_2 p_k$$
  Ini adalah ukuran kanonik. $E=0$ untuk state produk, maksimum $\log_2(d)$ untuk state maximally entangled (semua $p_k = 1/d$).

- **Pangkat Schmidt (Schmidt Rank):**
  $$r = \text{rank}(\rho_A)$$
  State terjerat jika $r > 1$. Pangkat Schmidt adalah ukuran kasar tetapi sangat berguna: ia adalah "dimensi efektif" keterjeratan.

- **Konkurensi (Concurrence) untuk Dua Qubit:**
  Untuk state dua qubit murni $|\psi\rangle = a|00\rangle + b|01\rangle + c|10\rangle + d|11\rangle$, Konkurensi adalah $C = 2|ad - bc|$.
  **Hubungan dengan SVD:** Matriks koefisien $2\times 2$ memiliki dua nilai singular $\sigma_1, \sigma_2$. Konkurensi terkait dengan $\sigma_1 \sigma_2$ (determinan). Lebih tepatnya, $C = 2\sqrt{\det(C)}$ (dengan normalisasi). Ini adalah aplikasi langsung SVD.

**Negativity dan PPT Criterion (untuk State Campuran):**
Untuk state campuran, kita menggunakan kriteria Peres-Horodecki: $\rho_{AB}$ terjerat jika $\rho_{AB}^{T_B}$ (transpos parsial pada B) memiliki nilai eigen negatif. **Negativity** adalah jumlah dari nilai eigen negatif tersebut, yang dikuantifikasi melalui Dekomposisi Spektral dari $\rho^{T_B}$.

#### 7.3. Aplikasi 2: Kompilasi Sirkuit Optimal

Tahap 5 dan 6 memberikan alat, tetapi bagaimana kita menggunakannya untuk mengoptimalkan sirkuit?

**Masalah:** Diberikan uniter target $U$, temukan rangkaian CNOT + 1-qubit dengan jumlah CNOT seminimal mungkin.

**Metode KAK (Cartan) untuk 2 Qubit:**
1.  Ambil $U \in SU(4)$.
2.  Hitung "bagian lokal" dan "bagian non-lokal" menggunakan dekomposisi Cartan:
    $$U = (L_1 \otimes R_1) \cdot e^{-i \vec{h} \cdot \vec{\sigma} \otimes \vec{\sigma}} \cdot (L_2 \otimes R_2)$$
    dengan $\vec{h} = (h_x, h_y, h_z)$.
3.  Bagian tengah $U_d = e^{-i \vec{h} \cdot \vec{\sigma} \otimes \vec{\sigma}}$ adalah "interaksi murni". **Teorema fundamental:** $U_d$ memerlukan **maksimal 3 gerbang CNOT**, dan jumlah minimal CNOT untuk $U$ dapat ditentukan dari $\vec{h}$.
    - Jika $h_x=h_y=0$, hanya butuh 1 CNOT.
    - Jika salah satu nol, butuh 2 CNOT.
    - Jika semuanya tak-nol, butuh 3 CNOT.

Ini adalah optimasi eksak berbasis dekomposisi.

**Metode Dekomposisi QSD (Quantum Shannon Decomposition):**
Ini adalah metode rekursif untuk $n$ qubit berdasarkan CSD. Ia memberikan dekomposisi dengan jumlah CNOT sekitar $\frac{23}{48}4^n$, yang lebih baik daripada dekomposisi QR naif ($\sim \frac{1}{2}4^n$). Ini adalah state of the art untuk sintesis uniter generik.

#### 7.4. Aplikasi 3: Simulasi Hamiltonian (Trotter-Suzuki)

**Masalah:** Simulasikan evolusi $e^{-iHt}$ di mana $H$ adalah Hamiltonian sistem banyak partikel.

**Dekomposisi Pauli:**
$$H = \sum_{j=1}^m c_j P_j$$
dengan $P_j$ adalah string Pauli (produk tensor dari $I, X, Y, Z$).

**Rumus Trotter Orde Pertama:**
$$e^{-iHt} \approx \left( \prod_{j=1}^m e^{-i c_j P_j t/N} \right)^N$$

Mengapa ini efisien? Karena setiap $e^{-i c_j P_j \tau}$ dapat diimplementasikan secara eksak dengan rangkaian pendek:
- $e^{-i\theta Z \otimes Z}$ = 2 CNOT + $R_z(2\theta)$.
- $e^{-i\theta X \otimes X}$ = (Hadamard pada kedua qubit) + $e^{-i\theta Z \otimes Z}$ + (Hadamard pada kedua qubit).
- Untuk string Pauli panjang, kita gunakan "ladder of CNOTs" untuk mengubahnya menjadi $Z$ pada satu qubit.

**Ini adalah jembatan langsung:** Dekomposisi aljabar (Hamiltonian → jumlah Pauli) → dekomposisi uniter (eksponensial tiap suku) → dekomposisi sirkuit (suku Pauli → CNOT + $R_z$) → implementasi fisik.

#### 7.5. Aplikasi 4: Tomografi dan Karakterisasi Proses Kuantum

**Masalah:** Eksperimen menghasilkan data, kita ingin merekonstruksi state $\rho$ atau proses $\mathcal{E}$.

- **Tomografi State:** Data pengukuran informasi lengkap direkonstruksi menjadi $\rho$. Kita memerlukan $\rho$ yang valid (Hermitian, positif, trace 1). **Dekomposisi Spektral** digunakan untuk memproyeksikan hasil rekonstruksi ke ruang state valid: kita diagonalisasi $\rho$, set nilai eigen negatif menjadi nol, lalu trace-normalize. Ini adalah prosedur "proyeksi state fisis".

- **Tomografi Proses (Standard Quantum Process Tomography):** $\mathcal{E}(\rho) = \sum_{mn} \chi_{mn} E_m \rho E_n^\dagger$. Matriks $\chi$ harus positif. Lagi-lagi, Dekomposisi Spektral pada $\chi$ digunakan untuk memproyeksikan ke matriks positif valid.

- **Dekomposisi Kraus:** Setiap kanal kuantum $\mathcal{E}$ dapat ditulis $\mathcal{E}(\rho) = \sum_k A_k \rho A_k^\dagger$. Operator Kraus $A_k$ tidak unik. **SVD** atau **Dekomposisi Polar** dapat digunakan untuk mendapatkan representasi Kraus minimal atau kanonik.

#### 7.6. Aplikasi 5: Kode Koreksi Error Kuantum (Quantum Error Correction)

Stabilizer codes adalah aplikasi raksasa dari dekomposisi spektral.

**Formalisme Stabilizer:**
Sebuah kode stabilizer $[[n,k,d]]$ mendefinisikan subruang kode $C$ sebagai ruang eigen bersama dengan nilai eigen $+1$ dari semua operator dalam grup stabilizer $S$.
$$C = \{ |\psi\rangle : g|\psi\rangle = |\psi\rangle, \forall g \in S \}$$

**Proyektor ke Subruang Kode:**
Proyektor ke subruang kode dibangun menggunakan **Dekomposisi Spektral** pada elemen-elemen $S$:
$$P_C = \frac{1}{|S|} \sum_{g \in S} g$$
Ini adalah proyektor ortogonal ke ruang eigen $+1$ bersama. Mengapa? Karena setiap $g$ memiliki nilai eigen $\pm 1$, maka $(g+I)/2$ adalah proyektor ke ruang eigen $+1$ dari $g$. Untuk seluruh grup, proyektornya adalah produk atau rata-rata.

**Sindrom dan Koreksi:**
Ketika error $E$ terjadi, state berpindah ke ruang eigen dengan nilai eigen tertentu. Pengukuran stabilizer adalah pengukuran proyektor spektral, dan hasilnya (sindrom) adalah konfigurasi nilai eigen. Ini adalah aplikasi langsung dari konsep proyektor spektral!

#### 7.7. Tabel Rangkuman Semua Dekomposisi

Untuk menutup perjalanan kita, inilah tabel referensi cepat:

| **Dekomposisi**     | **Formula**                                                                                                           | **Syarat**                     | **Aplikasi Kuantum Utama**                |
| ------------------- | --------------------------------------------------------------------------------------------------------------------- | ------------------------------ | ----------------------------------------- |
| **Spektral**        | $A = \sum \lambda_i P_i$                                                                                              | $A$ Normal                     | Observable, Gerbang Uniter, State $\rho$  |
| **SVD**             | $M = U \Sigma V^\dagger$                                                                                              | **Tidak ada** (semua matriks)  | Dekomposisi Schmidt, Keterjeratan         |
| **Schmidt**         | $\psi\rangle = \sum \sqrt{p_k}u_k\rangle v_k\rangle$                                                                  | State bipartit murni           | Spektrum keterjeratan, Entropi            |
| **Uniter Euler**    | $U = R_z(\alpha)R_y(\theta)R_z(\beta)$                                                                                | $U \in SU(2)$                  | Implementasi 1-qubit                      |
| **CSD**             | $U = \begin{pmatrix}V&0\\0&W\end{pmatrix} \begin{pmatrix}C&-S\\S&C\end{pmatrix} \begin{pmatrix}X&0\\0&Y\end{pmatrix}$ | $U$ Uniter multi-qubit         | Sintesis rekursif sirkuit                 |
| **QR (Givens)**     | $U = G_1 \dots G_k D$                                                                                                 | $U$ Uniter                     | Sintesis langsung sirkuit, interferometer |
| **Polar**           | $A = U P$                                                                                                             | **Tidak ada** (semua operator) | Pemisahan Rotasi vs Penyusutan, Kraus     |
| **Cartan (KAK)**    | $U = K_1 A K_2$                                                                                                       | $U \in G$ (grup Lie)           | Optimasi jumlah CNOT                      |
| **Jordan**          | $A = P J P^{-1}$                                                                                                      | Semua matriks persegi          | Dinamika non-Markov, Exceptional Points   |
| **Trotter (Pauli)** | $e^{-iHt} \approx \prod_j e^{-ic_j P_j t/N}$                                                                          | $H$ sparse/terjumlah           | Simulasi kuantum digital                  |

---

### Penutup Perjalanan Ini

Anda telah menempuh perjalanan yang luar biasa:
1.  **Bahasa:** Bra-ket, operator, adjoint, uniter, Hermitian.
2.  **Inti:** Spektral (operator normal → proyektor).
3.  **Universal:** SVD (semua matriks → dua basis, skala non-negatif).
4.  **Implementasi:** Euler (1-qubit), CSD/QR (multi-qubit → CNOT + 1-qubit).
5.  **Fondasi Lanjut:** Polar (rotasi vs penyusutan), Cartan (aljabar Lie), Jordan (non-normal).
6.  **Integrasi:** Bagaimana semua ini dipakai dalam kuantifikasi keterjeratan, kompilasi optimal, simulasi, tomografi, dan koreksi error.

Dengan bekal ini, Anda memiliki kerangka matematis yang solid untuk memahami hampir semua aspek komputasi kuantum modern, dari teori dasar hingga riset mutakhir. Setiap dekomposisi adalah alat dalam toolbox Anda, dan sekarang Anda tahu kapan dan bagaimana menggunakannya.

Terima kasih telah mengikuti roadmap ini dengan semangat yang tinggi. Apakah ada bagian yang ingin Anda review, perdalam contohnya, atau diskusikan aplikasinya lebih lanjut?