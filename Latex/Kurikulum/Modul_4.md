# Modul 4: Pemetaan Hamiltonian Ising (Fondasi Fisika Statistik)

Modul ini bertujuan untuk memberikan pemahaman mendalam mengenai transformasi masalah optimasi portofolio diskret ke dalam formalisme mekanika statistik melalui model *Ising Hamiltonian*. Mahasiswa akan mempelajari bagaimana "insentif" finansial dan "risiko" pasar dipetakan menjadi interaksi fisik antar *spin* yang dapat diproses oleh algoritma kuantum.

## 1. Urgensi & Konteks Fisika
Dalam paradigma komputasi kuantum variabel diskret, penyelesaian masalah optimasi dilakukan dengan mencari konfigurasi *ground state* (energi terendah) dari sebuah sistem fisik. Konsep ini secara langsung berkorespondensi dengan prinsip minimalisasi fungsi biaya (*cost function*) dalam Teori Portofolio Modern. Dengan memetakan aset menjadi variabel *spin* biner, kita dapat memanfaatkan fenomena *quantum tunneling* dan prinsip variasi untuk menembus lanskap energi yang kompleks dan menemukan solusi optimal yang sulit dicapai oleh algoritma klasik.

Pemetaan ini sangat krusial karena ia menjembatani dunia ekonomi yang abstrak dengan hukum fisik yang rigid. Hamiltonian Ising bukan sekadar representasi matematis, melainkan sebuah model "energi pasar" di mana setiap konfigurasi portofolio memiliki bobot energi tertentu. Melalui pendekatan ini, pemilihan aset tidak lagi dipandang sebagai proses seleksi statistik semata, melainkan sebagai proses relaksasi sistem banyak-partikel (*many-body system*) menuju kesetimbangan termodinamika pada suhu nol.

## 2. Formalisme Matematis & Algoritma
Proses transformasi dimulai dengan mengubah variabel keputusan portofolio $x_i \in \{0, 1\}$ (di mana $x_i=1$ berarti aset dipilih) menjadi variabel *spin* Pauli-$Z$ melalui pemetaan $x_i = \frac{1 - z_i}{2}$. Transformasi ini mengubah domain $\{0, 1\}$ menjadi $\{1, -1\}$, yang merupakan nilai eigen dari operator $\hat{\sigma}^z$. Hamiltonian total $H$ dibangun dengan menggabungkan fungsi objektif Markowitz yang telah dimodifikasi (menggunakan *Normalized Mutual Information*) dengan suku penalti *Lagrange* untuk memaksakan batasan jumlah aset $K$.

### A. Derivasi Parameter Hamiltoniann
Hamiltonian Ising secara umum dinyatakan sebagai:
$$ H = \sum_{i} h_i \hat{\sigma}_i^z + \sum_{i < j} J_{ij} \hat{\sigma}_i^z \hat{\sigma}_j^z \qquad (1) $$
Melalui substitusi variabel ke dalam fungsi objektif $O(x) = \gamma \sum \tilde{\sigma}_{ij} x_i x_j - \sum \tilde{\mu}_i x_i + \lambda (\sum x_i - K)^2$, kita memperoleh parameter kopling $J_{ij}$ dan bias lokal $h_i$ sebagai berikut:
$$ J_{ij} = \frac{\gamma \tilde{\sigma}_{ij} + 2\lambda}{4} \qquad (2) $$
$$ h_i = -0.5 \left[ \frac{\gamma}{2} \tilde{\sigma}_{ii} - \tilde{\mu}_i + \lambda(1 - 2K) \right] - \sum_{j \neq i} J_{ij} \qquad (3) $$
Di mana $\gamma$ adalah koefisien *risk aversion*, $\lambda$ adalah parameter penalti *Lagrange*, dan $\tilde{\sigma}$ adalah matriks kovariansi yang telah disesuaikan dengan metrik non-linier.

### B. Penanganan Kendala (Constraint Handling)
Batasan jumlah aset atau *cardinality constraint* ($\sum x_i = K$) diintegrasikan menggunakan metode *Lagrange Multiplier* dalam bentuk sumur potensial kuadratik $P(x) = \lambda (\sum x_i - K)^2$. Penggunaan bentuk kuadratik (L2-norm) memastikan bahwa setiap deviasi dari target $K$, baik kelebihan maupun kekurangan aset, akan diberikan hukuman berupa kenaikan energi sistem. Dalam perspektif fisik, ini menciptakan "sumur energi" yang memaksa *bitstring* hasil pengukuran untuk selalu memiliki bobot Hamming yang sesuai dengan target $K$.

## 3. Implementasi Teknis (Code Breakdown)
Pada implementasi kode di `GT_Ising_SBR.ipynb`, proses ini dieksekusi melalui fungsi `build_hamiltonian_total`. Fungsi ini menerima input berupa vektor $h\_total$ dan matriks $J\_total$ yang telah dihitung berdasarkan data pasar historis. Algoritma kemudian membangun operator Hamiltonian menggunakan *library* `PennyLane` dengan merepresentasikan setiap suku sebagai produk tensor dari matriks Pauli-$Z$.

```python
def build_hamiltonian_total(h_total, J_total, n_assets):
    coeffs = []
    obs    = []
    # Suku Bias Lokal (h_i)
    for i in range(n_assets):
        if abs(h_total[i]) > 1e-10:
            coeffs.append(float(h_total[i]))
            obs.append(qml.PauliZ(i))
    # Suku Interaksi (J_ij)
    for i in range(n_assets):
        for j in range(i + 1, n_assets):
            if abs(J_total[i, j]) > 1e-10:
                coeffs.append(float(J_total[i, j]))
                obs.append(qml.PauliZ(i) @ qml.PauliZ(j))
    return qml.Hamiltonian(coeffs, obs)
```
Proses ini secara efektif mengonversi data finansial mentah menjadi instruksi operasional untuk perangkat keras kuantum, di mana nilai $h_i$ menentukan rotasi individual qubit dan $J_{ij}$ menentukan kekuatan *entanglement* antar qubit.

## 4. Analisis Konvergensi & Hasil
Keberhasilan pemetaan ini sangat bergantung pada pemilihan nilai parameter penalti $\lambda$. Jika $\lambda$ terlalu kecil, sistem mungkin akan memprioritaskan minimalisasi risiko dan maksimalisasi *return* hingga melanggar batasan $K$. Sebaliknya, jika $\lambda$ terlalu besar, gradien energi akan menjadi terlalu curam, yang dapat menyebabkan algoritma optimasi (seperti SPSA) terjebak dalam minimum lokal atau gagal mencapai konvergensi yang stabil.

Mahasiswa diharapkan melakukan eksperimen dengan mengubah rasio antara $\gamma$ dan $\lambda$ untuk mengamati perubahan pada lanskap energi sistem. Stabilitas solusi dapat diverifikasi melalui grafik riwayat energi, di mana konvergensi yang baik ditandai dengan penurunan energi secara asimtotik menuju nilai minimum yang konsisten dengan solusi *Nash Equilibrium* klasik yang diperoleh melalui *Sequential Best Response* (SBR).
