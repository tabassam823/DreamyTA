# Jawaban Soal 2a dan 2b: Generator Grup SO(4)

## 2a. Generator SO(4) dalam Representasi Matriks

Grup $SO(4)$ adalah grup rotasi dalam ruang 4-dimensi. Jumlah generator untuk $SO(n)$ adalah $n(n-1)/2$. Untuk $n=4$, terdapat $4(3)/2 = 6$ generator.

Generator $J_{ij}$ didefinisikan sebagai matriks yang menghasilkan rotasi di bidang $(i,j)$. Matriks-matriks ini bersifat anti-simetris ($J_{ij} = -J_{ji}$). Dalam representasi matriks $4 	imes 4$, komponen $(k,l)$ dari generator $J_{ij}$ diberikan oleh:
$$(J_{ij})_{kl} = -i (\delta_{ik} \delta_{jl} - \delta_{il} \delta_{jk})$$

Berikut adalah 6 generator $SO(4)$ menggunakan `pmatrix`:

### Rotasi yang melibatkan sumbu 1, 2, dan 3 (Subgrup SO(3))
$$
J_{12} = \begin{pmatrix} 0 & -i & 0 & 0 \\ i & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}, \quad
J_{23} = \begin{pmatrix} 0 & 0 & 0 & 0 \\ 0 & 0 & -i & 0 \\ 0 & i & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}, \quad
J_{31} = \begin{pmatrix} 0 & 0 & i & 0 \\ 0 & 0 & 0 & 0 \\ -i & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}
$$

### Rotasi yang melibatkan sumbu ke-4
$$
J_{14} = \begin{pmatrix} 0 & 0 & 0 & -i \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ i & 0 & 0 & 0 \end{pmatrix}, \quad
J_{24} = \begin{pmatrix} 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & -i \\ 0 & 0 & 0 & 0 \\ 0 & i & 0 & 0 \end{pmatrix}, \quad
J_{34} = \begin{pmatrix} 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & -i \\ 0 & 0 & i & 0 \end{pmatrix}
$$

---

## 2b. Generator SO(4) dalam Notasi Operator Diferensial

Dalam mekanika kuantum dan teori medan, generator rotasi sering dinyatakan sebagai operator momentum sudut yang bekerja pada ruang fungsi (koordinat). 

Untuk koordinat $x_1, x_2, x_3, x_4$, operator diferensial untuk generator $J_{ij}$ didefinisikan sebagai:
$$\hat{J}_{ij} = -i \left( x_i \frac{\partial}{\partial x_j} - x_j \frac{\partial}{\partial x_i} \right)$$

Secara eksplisit, keenam generator tersebut adalah:

1.  **Bidang (1,2):** $\hat{J}_{12} = -i \left( x_1 \partial_2 - x_2 \partial_1 \right)$
2.  **Bidang (2,3):** $\hat{J}_{23} = -i \left( x_2 \partial_3 - x_3 \partial_2 \right)$
3.  **Bidang (3,1):** $\hat{J}_{31} = -i \left( x_3 \partial_1 - x_1 \partial_3 \right)$
4.  **Bidang (1,4):** $\hat{J}_{14} = -i \left( x_1 \partial_4 - x_4 \partial_1 \right)$
5.  **Bidang (2,4):** $\hat{J}_{24} = -i \left( x_2 \partial_4 - x_4 \partial_2 \right)$
6.  **Bidang (3,4):** $\hat{J}_{34} = -i \left( x_3 \partial_4 - x_4 \partial_3 \right)$

Di sini $\partial_i$ merupakan notasi singkat untuk $\frac{\partial}{\partial x_i}$. Operator-operator ini memenuhi aljabar Lie yang sama dengan representasi matriksnya.

---

## 2c. 4 Contoh Elemen Grup SO(4)

Elemen grup $SO(4)$ adalah matriks $4 \times 4$ riil yang bersifat ortogonal ($R^T R = I$) dan memiliki determinan $+1$. Elemen-elemen ini merepresentasikan rotasi di ruang 4D.

Berikut adalah 4 contoh elemen grup $SO(4)$:

### 1. Rotasi pada Bidang (1,2)
Matriks ini memutar koordinat di bidang $x_1-x_2$ dengan sudut $\theta$:
$$R_{12}(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta & 0 & 0 \\ \sin\theta & \cos\theta & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$$

### 2. Rotasi pada Bidang (3,4)
Matriks ini memutar koordinat di bidang $x_3-x_4$ dengan sudut $\phi$:
$$R_{34}(\phi) = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & \cos\phi & -\sin\phi \\ 0 & 0 & \sin\phi & \cos\phi \end{pmatrix}$$

### 3. Rotasi Isotropik (Double Rotation)
$SO(4)$ memungkinkan rotasi simultan pada dua bidang yang saling tegak lurus (misalnya bidang 1-2 dan 3-4). Jika sudutnya sama ($\theta$), ini disebut rotasi isoklinik:
$$R_{double}(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta & 0 & 0 \\ \sin\theta & \cos\theta & 0 & 0 \\ 0 & 0 & \cos\theta & -\sin\theta \\ 0 & 0 & \sin\theta & \cos\theta \end{pmatrix}$$

### 4. Rotasi pada Bidang (2,3)
Contoh rotasi yang menghubungkan koordinat "dalam" subgrup $SO(3)$ pertama dengan sumbu lainnya:
$$R_{23}(\alpha) = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & \cos\alpha & -\sin\alpha & 0 \\ 0 & \sin\alpha & \cos\alpha & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$$

**Sifat Umum:** Semua matriks di atas memenuhi $R^T R = I$ dan $\det(R) = 1$. Sebagai contoh, untuk $R_{12}(\theta)$, determinannya adalah $(\cos^2\theta + \sin^2\theta) \cdot 1 \cdot 1 = 1$.

