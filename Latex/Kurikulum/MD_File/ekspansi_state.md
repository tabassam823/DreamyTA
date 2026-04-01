# Ekspansi State dalam Basis Eigen: Mekanisme Konvergensi Kuantum

Dokumen ini menjelaskan mengapa kita dapat menguraikan sembarang state kuantum menjadi kombinasi dari state-state energi, dan bagaimana hal ini menjadi kunci bagi algoritma optimasi seperti VQE.

---

## 1. Postulat Dasar: Spektrum Operator Hermitian
Dalam mekanika kuantum, Hamiltonian $\hat{H}$ adalah operator linear Hermitian. Berdasarkan **Teorema Spektral** dalam aljabar linear:

**Aksioma & Konvensi:**
1.  **Eigensystem:** Terdapat sekumpulan nilai eigen riil $\{E_n\}$ dan vektor eigen $\{|v_n\rangle\}$ yang memenuhi persamaan:
    $$ \hat{H} |v_n\rangle = E_n |v_n\rangle $$
2.  **Ortonormalitas:** Vektor-vektor eigen ini bersifat ortonormal, yaitu $\langle v_m | v_n \rangle = \delta_{mn}$.
3.  **Kelengkapan (Completeness):** Vektor-vektor eigen $\{|v_n\rangle\}$ membentuk basis lengkap untuk ruang Hilbert $\mathcal{H}$.

**Filosofi:**
Basis eigen adalah "bahasa alami" dari Hamiltonian. Sama seperti warna putih yang dapat diuraikan menjadi spektrum warna pelangi, sebuah state kuantum abstrak $|\psi\rangle$ dapat diuraikan menjadi komponen-komponen energi yang menyusunnya.

---

## 2. Jembatan 1: Prinsip Superposisi dan Resolusi Identitas
Karena $\{|v_n\rangle\}$ adalah basis lengkap, kita dapat menyatakan sembarang state $|\psi\rangle$ sebagai kombinasi linear (superposisi) dari vektor-vektor eigen tersebut.

**Alat (Resolusi Identitas):**
Sebuah identitas operator $\hat{I}$ dapat dinyatakan sebagai jumlah dari semua operator proyeksi ke basis eigen:
$$ \hat{I} = \sum_n |v_n\rangle\langle v_n | $$

**Jembatan Gagasan:**
Dengan menyisipkan identitas ke dalam $|\psi\rangle$, kita memproyeksikan state tersebut ke seluruh spektrum Hamiltonian:
$$ |\psi\rangle = \hat{I} |\psi\rangle = \sum_n |v_n\rangle \langle v_n | \psi \rangle $$
$$ |\psi\rangle = \sum_n \alpha_n |v_n\rangle $$
di mana $\alpha_n = \langle v_n | \psi \rangle$ adalah **amplitudo probabilitas** sistem berada pada tingkat energi $E_n$.

---

## 3. Jembatan 2: Normalisasi dan Konservasi Probabilitas
Agar $|\psi\rangle$ merepresentasikan sistem fisik yang nyata, total probabilitas harus bernilai satu.

**Derivasi Runtut:**
$$ \langle \psi | \psi \rangle = \left( \sum_m \alpha_m^* \langle v_m | \right) \left( \sum_n \alpha_n |v_n\rangle \right) $$
Karena sifat ortonormalitas ($\langle v_m | v_n \rangle = \delta_{mn}$), maka:
$$ \sum_n |\alpha_n|^2 = 1 $$

**Jembatan Gagasan:**
Koefisien $|\alpha_n|^2$ (berdasarkan Aturan Born) menunjukkan bobot kontribusi setiap tingkat energi terhadap state total. Jika $|\alpha_0|^2$ besar, maka state tersebut sangat mirip dengan ground state.

---

## 4. Jembatan 3: Nilai Ekspektasi dalam Representasi Spektral
Bagaimana ekspansi ini membantu kita menghitung energi rata-rata?

**Derivasi Energi:**
$$ \langle E \rangle = \langle \psi | \hat{H} | \psi \rangle = \langle \psi | \hat{H} \left( \sum_n \alpha_n |v_n\rangle \right) $$
Karena $\hat{H} |v_n\rangle = E_n |v_n\rangle$:
$$ \langle E \rangle = \left( \sum_m \alpha_m^* \langle v_m | \right) \left( \sum_n \alpha_n E_n |v_n\rangle \right) $$
$$ \langle E \rangle = \sum_n E_n |\alpha_n|^2 $$

**Filosofi Jembatan:**
Energi yang kita ukur (nilai ekspektasi) adalah **rata-rata tertimbang** dari seluruh spektrum energi Hamiltonian, di mana bobotnya adalah probabilitas $|\alpha_n|^2$ dari ekspansi state kita.

---

## 5. Aplikasi pada VQE: Mekanisme Konvergensi
Dalam VQE, kita memiliki state parametrik $|\psi(\theta)\rangle$. Berarti amplitudo probabilitasnya juga bergantung pada parameter: $\alpha_n(\theta)$.

**Logika Optimasi:**
1.  **Keadaan Awal:** Saat $\theta$ acak, $|\psi(\theta)\rangle$ memiliki komponen di banyak tingkat energi (banyak $\alpha_n$ yang tidak nol). Energi $\langle E \rangle$ akan bernilai tinggi.
2.  **Proses Minimisasi:** Algoritma optimasi mengubah $\theta$ untuk menurunkan $\langle E \rangle$.
3.  **Filter Energi:** Secara matematis, proses ini "membuang" komponen state eksitasi ($n > 0$) dengan cara mengecilkan $|\alpha_n(\theta)|^2$ dan memperbesar $|\alpha_0(\theta)|^2$.

**Limit Konvergensi:**
$$ \lim_{\theta \to \theta^*} \alpha_n(\theta) = \begin{cases} 1 & \text{untuk } n=0 \\ 0 & \text{untuk } n \ne 0 \end{cases} $$
$$ \lim_{\theta \to \theta^*} \langle E \rangle = E_0 $$

---

## 6. Kesimpulan
Ekspansi state adalah alat yang memungkinkan kita melihat "jeroan" dari sirkuit kuantum. Ia membuktikan bahwa menurunkan nilai ekspektasi energi secara numerik setara dengan **menyelaraskan sirkuit kuantum** kita agar tepat berada pada basis eigen energi terendah (ground state). Tanpa konsep ekspansi ini, kita tidak akan memiliki justifikasi matematis mengapa VQE dapat menemukan solusi portfolio optimal.
