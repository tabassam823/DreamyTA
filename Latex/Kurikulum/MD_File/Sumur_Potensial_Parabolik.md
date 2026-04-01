# Analogi Sumur Potensial Parabolik: Memenjarakan State dalam Kendala

## 1. Urgency Eksplorasi
Mengapa kita butuh "Sumur Potensial"? Dalam optimasi portofolio kuantum, kita tidak hanya mencari risiko terendah, tetapi risiko terendah *pada jumlah aset tertentu*. Tanpa mekanisme pengunci ini, Hamiltonian akan "bocor" ke solusi trivial (seperti tidak memilih aset sama sekali untuk menihilkan risiko). Kita perlu menciptakan gaya pemulih (*restoring force*) yang secara otomatis menarik sistem kembali ke target $K$.

## 2. Aksioma & Intuisi: Osilator Harmonik
Dalam fisika klasik dan kuantum, cara paling stabil untuk menjaga partikel tetap di satu titik adalah dengan menempatkannya dalam **Sumur Potensial Parabolik**.
- **Analogi Mangkuk:** Bayangkan sebuah kelereng di dasar mangkuk parabola. Dasar mangkuk adalah target kita ($x = K$). 
- Jika kelereng bergeser ke kanan ($x > K$) atau ke kiri ($x < K$), bentuk parabola menciptakan gaya gravitasi yang menariknya kembali ke dasar.
- Dalam kuantum, ini direpresentasikan oleh Hamiltonian Osilator Harmonik Sederhana (QHO): $\hat{H} = \frac{\hat{p}^2}{2m} + \frac{1}{2}m\omega^2\hat{x}^2$.

## 3. Jembatan Logika: Pelanggaran Kendala sebagai "Displacement"
Dalam masalah pemilihan aset, kita mendefinisikan "jarak" dari idealitas sebagai selisih antara jumlah aset yang dipilih ($\sum x_i$) dengan target $K$.
- Jika kita menganggap $\sum x_i$ sebagai operator posisi $\hat{X}$.
- Maka, pelanggaran kendala adalah perpindahan $\Delta \hat{X} = (\hat{X} - K)$.
- Untuk mendapatkan energi yang selalu positif (hukuman), kita menguadratkan perpindahan tersebut, persis seperti energi potensial pegas $V(x) = \frac{1}{2}k\Delta x^2$.

## 4. Reduksionisme (Kasus Minimal: 1-Qubit)
Misalkan kita ingin qubit $x_1$ bernilai 1. Target $K=1$.
Suku penaltinya: $P(x) = A(x_1 - 1)^2$.
- Jika $x_1 = 1$, maka $P(1) = A(1-1)^2 = 0$.
- Jika $x_1 = 0$, maka $P(0) = A(0-1)^2 = A$.
Energi sistem naik sebesar $A$ jika kendala dilanggar.
/
## 5. Derivasi "Scratchpad" & Indeks Persamaan
Mari kita bangun Hamiltonian Penalti ($H_P$) dari operator jumlah aset $\hat{N}$.

Definisikan operator jumlah aset sebagai jumlahan operator okupansi:
$$ \hat{N} = \sum_{i=1}^n \hat{n}_i \qquad (1) $$
Di mana $\hat{n}_i$ adalah operator bilangan (eigenvalue 0 atau 1).

Untuk memenjarakan sistem pada nilai $\hat{N} = K$, kita konstruksi sumur potensial di sekitar $K$:
$$ H_P = A (\hat{N} - K\hat{I})^2 \qquad (2) $$
Di mana $A$ adalah konstanta kekakuan (*stiffness*) sumur, setara dengan $\frac{1}{2}m\omega^2$ pada osilator fisik.

## 6. Visualisasi Perhitungan (Blok `>`)
Mari kita ekspansi Persamaan (2) untuk kasus pemilihan $K=1$ dari $n=2$ aset ($x_1, x_2$):
> $$ H_P = A (\hat{n}_1 + \hat{n}_2 - 1)^2 $$
> $$ H_P = A [ (\hat{n}_1 + \hat{n}_2)^2 - 2(1)(\hat{n}_1 + \hat{n}_2) + 1^2 ] $$
> $$ H_P = A [ (\hat{n}_1^2 + \hat{n}_2^2 + 2\hat{n}_1\hat{n}_2) - 2\hat{n}_1 - 2\hat{n}_2 + 1 ] $$
>
> Mengingat sifat operator biner $\hat{n}_i^2 = \hat{n}_i$:
> $$ H_P = A [ (\hat{n}_1 + \hat{n}_2 + 2\hat{n}_1\hat{n}_2) - 2\hat{n}_1 - 2\hat{n}_2 + 1 ] $$
> $$ H_P = A [ 2\hat{n}_1\hat{n}_2 - \hat{n}_1 - \hat{n}_2 + 1 ] $$

## 7. Verifikasi & Parameter
Uji tingkat energi untuk konfigurasi state $|x_1 x_2\rangle$ dengan $K=1, A=10$:
- $|00\rangle \rightarrow \hat{N}=0 \rightarrow E = 10(0-1)^2 = 10$ (High Energy/Dihukum)
- **$|01\rangle \rightarrow \hat{N}=1 \rightarrow E = 10(1-1)^2 = 0$ (Ground State/Optimal)**
- **$|10\rangle \rightarrow \hat{N}=1 \rightarrow E = 10(1-1)^2 = 0$ (Ground State/Optimal)**
- $|11\rangle \rightarrow \hat{N}=2 \rightarrow E = 10(2-1)^2 = 10$ (High Energy/Dihukum)

## 8. Analogi "Physical Insight": Pegas Kaku
Parameter $A$ menentukan seberapa "keras" pegas yang mengikat kendala kita. 
- Jika $A$ kecil, pegas lembek; sistem mungkin berani melanggar kendala sedikit demi mendapatkan return yang sangat besar (energi risiko rendah).
- Jika $A$ besar, pegas sangat kaku; sistem tidak akan berani keluar dari dasar sumur $K$ karena kenaikan energi penaltinya akan sangat masif.

## 9. Visualisasi Mentah
Bayangkan permukaan energi Hamiltonian sebagai sebuah lembah curam berbentuk huruf "U" (parabola) yang memanjang di atas ruang Hilbert. Dasar lembah tersebut tepat memotong titik-titik kombinasi aset yang berjumlah $K$. VQE akan bertindak seperti partikel yang kehilangan energi (melalui optimasi parameter) hingga akhirnya "terperosok" dan berhenti di dasar lembah tersebut.
