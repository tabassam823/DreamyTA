# Penurunan Konsep: Dari TwoLocal ke EfficientSU2

Dokumen ini menjelaskan bagaimana arsitektur umum **TwoLocal** dispesialisasi menjadi ansatz **EfficientSU2** melalui pemilihan blok rotasi dan pola keterbelitan tertentu.

## 1. Definisi Umum TwoLocal
Dalam Qiskit, `TwoLocal` adalah sebuah *template* sirkuit parameterisasi yang bergantian antara layer rotasi satu-qubit ($L$) dan layer keterbelitan dua-qubit ($W$). Secara matematis, sirkuit dengan kedalaman $d$ (*reps*) didefinisikan sebagai:

$$U(	\theta) = L_d(	\theta_d) \prod_{i=0}^{d-1} [W_i L_i(	\theta_i)]$$

Di mana:
- $L_i$: Operator uniter yang terdiri dari gerbang rotasi lokal (tensor product of single-qubit gates).
- $W_i$: Operator keterbelitan (entanglement) yang menghubungkan antar qubit.
- $d$: Jumlah repetisi blok.

## 2. Spesialisasi Menuju EfficientSU2
`EfficientSU2` adalah instansiasi dari `TwoLocal` dengan batasan (constraint) pada jenis gerbang yang digunakan untuk mengoptimalkan performa pada hardware NISQ.

### A. Blok Rotasi ($L_i$)
Pada `TwoLocal` umum, blok rotasi bisa berupa kombinasi gerbang apa pun (misal $RX, RY, RZ$). Namun, `EfficientSU2` secara spesifik memilih grup $SU(2)$ (Special Unitary group of degree 2). 

Setiap elemen dalam $SU(2)$ dapat direpresentasikan pada bola Bloch. Untuk mencapai cakupan yang efisien, `EfficientSU2` menggunakan urutan gerbang $R_y$ dan $R_z$:

$$L_i(	\theta_i) = \bigotimes_{j=0}^{n-1} \text{Rot}_{SU(2)}(	\theta_{i,j})$$

Secara matematis, blok rotasi untuk satu qubit $j$ pada layer $i$ dijabarkan menjadi:
$$\text{Rot}_{SU(2)}(	\theta_{i,j}) = R_z(	\theta_{i,j,2}) \cdot R_y(	\theta_{i,j,1})$$

*Catatan: Kombinasi $R_z R_y$ (atau $R_y R_z$) dipilih karena mampu menjangkau seluruh permukaan bola Bloch dengan jumlah parameter minimum (2 parameter per qubit per layer).*

### B. Blok Keterbelitan ($W_i$)
Pada `TwoLocal`, blok keterbelitan bisa berupa gerbang terkontrol apa pun. Pada `EfficientSU2`, standar yang digunakan adalah gerbang **CNOT (CX)** yang bersifat non-parameterisasi:

$$W_i = 	\text{Entangler}(P)$$

Di mana $P$ adalah pola konektivitas (Linear, Circular, atau Full). Misalnya, untuk pola **Linear**:
$$W = \prod_{j=0}^{n-2} CX_{j, j+1}$$

## 3. Penurunan Bentuk Umum ke Bentuk Khusus
Jika kita substitusikan komponen di atas ke dalam persamaan umum `TwoLocal`:

1.  **Substitusi Operator Rotasi**:
    Ganti $L_i(	\theta_i)$ dengan $\bigotimes_{j=0}^{n-1} R_z(	\theta_{i,j,2}) R_y(	\theta_{i,j,1})$.
2.  **Substitusi Operator Keterbelitan**:
    Ganti $W_i$ dengan urutan gerbang $CX$.

Maka, bentuk eksplisit dari **EfficientSU2** adalah:

$$|\psi(	\theta) \rangle = \underbrace{\left[ \bigotimes_{j=0}^{n-1} R_z(	\theta_{d,j,2}) R_y(	\theta_{d,j,1}) \right]}_{\text{Final Rotation Layer}} \prod_{i=0}^{d-1} \left[ \underbrace{W_{CX}}_{\text{Entanglement}} \underbrace{\bigotimes_{j=0}^{n-1} R_z(	\theta_{i,j,2}) R_y(	\theta_{i,j,1})}_{\text{Rotation Layer } i} \right] |0 \rangle^{\otimes n}$$

## 4. Perbandingan Parameterisasi
Perbedaan utama dalam perhitungan jumlah parameter dapat diturunkan sebagai berikut:

*   **TwoLocal Umum**: 
    $$\text{Params} = n \times (\text{jumlah jenis gerbang rotasi} \times (d + 1))$$
*   **EfficientSU2**:
    Karena menggunakan 2 jenis gerbang ($R_y, R_z$), maka:
    $$\text{Params}_{SU2} = n \times 2 \times (d + 1)$$

## 5. Kesimpulan Representasi
`EfficientSU2` adalah **TwoLocal** yang "disederhanakan" untuk kebutuhan universalitas rotasi pada satu qubit namun tetap efisien dalam jumlah gerbang. Ia mengambil struktur modular `TwoLocal` dan mengisinya dengan:
1.  **Rotations**: `['ry', 'rz']` (Membentuk grup $SU(2)$).
2.  **Entanglement**: `cx` (Standard hardware gate).

Hal ini menjadikannya sangat "efficient" karena meminimalkan kedalaman sirkuit sambil tetap mempertahankan kemampuan untuk merepresentasikan state quantum kompleks di ruang Hilbert.
