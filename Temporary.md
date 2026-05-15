### 1. Definisi Grup Uniter $\mathcal{U}(N)$

Grup uniter berderajat $N$, dinotasikan sebagai $\mathcal{U}(N)$, adalah himpunan semua matriks kompleks berdimensi $N \times N$ yang memenuhi properti uniter. Dalam komputasi kuantum untuk sistem $n$-qubit, dimensi grup ini direpresentasikan sebagai $N = 2^n$.

Kondisi matematis pembentuk $\mathcal{U}(N)$:

$$\mathcal{U}(N) = \{ U \in \mathbb{C}^{N \times N} \mid U^\dagger U = U U^\dagger = I_N \}$$

_Definisi Simbol:_

- $U$: Operator evolusi kuantum (berasosiasi dengan sirkuit ansatz).
    
- $U^\dagger$: Transpos konjugat kompleks dari $U$.
    
- $I_N$: Matriks identitas berdimensi $N \times N$.
    

Properti grup $\mathcal{U}(N)$:

1. **Ketertutupan (_Closure_):** Untuk setiap $U_1, U_2 \in \mathcal{U}(N)$, produk matriks $U_1 U_2 \in \mathcal{U}(N)$.
    
2. **Invers:** Setiap $U \in \mathcal{U}(N)$ memiliki invers unik $U^{-1} = U^\dagger \in \mathcal{U}(N)$.
    
3. **Preservasi Norma:** Transformasi uniter mempertahankan perkalian dalam (_inner product_) vektor, menjamin total probabilitas kuantum selalu 1 ($|\langle\psi|U^\dagger U|\psi\rangle| = 1$).
    

### 2. Definisi Ukuran Haar (Haar Measure) $dU$

Grup uniter $\mathcal{U}(N)$ secara topologis merupakan manifold kontinu dan kompak (grup Lie). Ukuran Haar, dinotasikan dengan diferensial $dU$, adalah ukuran probabilitas invarian yang unik pada grup ruang ini.

Sifat fundamental Ukuran Haar (Invariansi Translasi):

Untuk setiap matriks uniter konstan $V \in \mathcal{U}(N)$ dan fungsi terintegralkan $f(U)$:

$$\int_{\mathcal{U}(N)} f(U) dU = \int_{\mathcal{U}(N)} f(VU) dU = \int_{\mathcal{U}(N)} f(UV) dU$$

Kondisi Normalisasi (Probabilitas Total):

$$\int_{\mathcal{U}(N)} 1 dU = 1$$

### 3. Lema Integrasi Ukuran Haar (Weingarten Calculus)

Evaluasi kuantitas mekanika kuantum pada distribusi uniter acak bergantung pada momen integrasi elemen matriks.

**A. Momen Orde Pertama (Haar 1-Design):**

Ekspektasi nilai elemen matriks tunggal berpusat pada nol:

$$\int_{\mathcal{U}(N)} U_{ij} U^*_{kl} dU = \frac{1}{N} \delta_{ik} \delta_{jl}$$

Bentuk operator (_trace_):

$$\int_{\mathcal{U}(N)} U A U^\dagger dU = \frac{\text{Tr}[A]}{N} I$$

**B. Momen Orde Kedua (Haar 2-Design):**

Formulasi ekspansi polinomial orde dua berdasar fungsi Weingarten:

$$\int_{\mathcal{U}(N)} U A U^\dagger B U C U^\dagger dU = \frac{\text{Tr}[A]\text{Tr}[C]}{N^2-1} B + \frac{\text{Tr}[AC]}{N^2-1} \text{Tr}[B] I - \frac{\text{Tr}[AC]\text{Tr}[B]}{N(N^2-1)} I - \frac{\text{Tr}[A]\text{Tr}[C]}{N(N^2-1)} B$$

Untuk kasus spesifik penyederhanaan operator komutator pada kuadrat nilai ekspektasi (digunakan pada tahap 5):

$$\int_{\mathcal{U}(N)} |\text{Tr}[A U B U^\dagger]|^2 dU = \frac{\text{Tr}[A^2]\text{Tr}[B^2] + |\text{Tr}[A]|^2|\text{Tr}[B]|^2 - \frac{1}{N}(\text{Tr}[A^2]|\text{Tr}[B]|^2 + \text{Tr}[B^2]|\text{Tr}[A]|^2)}{N^2-1}$$

Jika matrik $A$ dan $B$ adalah _traceless_ ($\text{Tr}[A] = \text{Tr}[B] = 0$), rumusan tereduksi menjadi:

$$\int_{\mathcal{U}(N)} |\text{Tr}[A U B U^\dagger]|^2 dU = \frac{\text{Tr}[A^2]\text{Tr}[B^2]}{N^2-1}$$

---

### 4. Kontribusi Prinsip pada Penurunan Rumus Tahap 5 dan 6

Sirkuit ansatz VQE (Tahap 4) parametrik $|\psi(\theta)\rangle$ berkedalaman tinggi ($d \to \infty$) secara matematis berevolusi membentuk **Unitary 2-Design**, di mana distribusi matriks dari operator parametrik mengaproksimasi momen orde pertama dan kedua dari ukuran Haar secara eksak.

**A. Kontribusi pada Fenomena Barren Plateau (Tahap 5):**

Definisi variansi gradien:

$$\text{Var}_\theta[\partial_k E(\theta)] = \mathbb{E}_\theta[(\partial_k E(\theta))^2]$$

Turunan analitik kuadrat fungsi biaya memuat operator $U_L$ dan $U_R$. Berkat sifat invarian translasi ukuran Haar, ekspektasi parameter disubstitusi menjadi integral probabilitas atas $\mathcal{U}(N)$ untuk $U_L$ dan $U_R$.

Aplikasi Lema Haar Orde-2 (dengan operator Pauli/Generator $V_k$ yang _traceless_ $\text{Tr}[V_k] = 0$):

$$\mathbb{E}_\theta[(\partial_k E(\theta))^2] = \int_{\mathcal{U}(N)} \left(-\frac{i}{2}\text{Tr}[H U_R [V_k, U_L|0\rangle\langle0|U_L^\dagger] U_R^\dagger]\right)^2 dU_R dU_L$$

Substitusi Lema 3B mengeliminasi dependensi lokal parameter, menghasilkan batas komputasi analitik:

$$\text{Var}_\theta[\partial_k E(\theta)] \approx \frac{\text{Tr}[H^2]\text{Tr}[V_k^2]}{2(N^2-1)} \propto \frac{1}{N^2} = \frac{1}{(2^n)^2}$$

Sifat manifold $\mathcal{U}(N)$ memaksa probabilitas pemusatan vektor konsentrasi (_concentration of measure_) secara eksponensial dekat ke nilai ekspektasi (0), meratakan ruang parameter optimasi SPSA.

**B. Kontribusi pada Entropi Von Neumann (Tahap 6):**

Ketergantungan $\rho_A(\theta)$ dikalkulasi rata-ratanya menggunakan integrasi terhadap statevector acak-Haar ($|\psi\rangle = U|0\rangle$ dengan $U \sim \text{Haar}$).

Aplikasi Lema Haar 1-Design pada matriks densitas global:

$$\mathbb{E}_{U \sim \text{Haar}}[|\psi\rangle\langle\psi|] = \int_{\mathcal{U}(N)} U |0\rangle\langle0| U^\dagger dU = \frac{\text{Tr}[|0\rangle\langle0|]}{N} I_{AB} = \frac{I_{AB}}{d_A d_B}$$

Konsekuensi asimtotik Page's Theorem (yang diturunkan langsung dari metrik geometris $\mathcal{U}(N)$) mengekstrak volume sub-ruang subsistem A, yang terbukti mendominasi matriks campuran:

$$\mathbb{E}_{U \sim \text{Haar}}[S(\rho_A)] = \sum_{j=d_B+1}^{d_A d_B} \frac{1}{j} - \frac{d_A - 1}{2 d_B}$$

Untuk $d_B \gg d_A$, deret Taylor proyektif mereduksi ekspresi ke:

$$\mathbb{E}[S(\rho_A)] \to \log_2(d_A)$$

Integrasi probabilitas pada grup $\mathcal{U}(N)$ merasionalisasi bahwa mayoritas keadaan di ruang Hilbert besar adalah **teralitkan secara maksimal**, menjadikan entropi sebagai fungsi indikator geometris langsung atas kejenuhan (Barren Plateau) yang dialami oleh ansatz.