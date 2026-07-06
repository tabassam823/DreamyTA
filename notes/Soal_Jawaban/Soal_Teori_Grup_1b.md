# Jawaban Soal 1b: Contoh Elemen Grup SU(4)

Elemen grup $SU(4)$ adalah matriks uniter $4 	imes 4$ dengan determinan +1. Secara umum, elemen grup dapat dituliskan dalam bentuk eksponensial dari generatornya:
$$U = e^{i \alpha_a \lambda_a}$$
di mana $\lambda_a$ adalah generator $SU(4)$ (matriks Gell-Mann $4 	imes 4$) dan $\alpha_a$ adalah parameter riil.

Berikut adalah 3 contoh elemen grup $SU(4)$:

## Contoh 1: Rotasi dalam Subruang (1,2)
Menggunakan generator $\lambda_3$, kita dapat membentuk matriks diagonal yang melakukan pergeseran fasa berlawanan pada dua komponen pertama.
Misalkan $\alpha_3 = \pi/2$:
$$U_1 = \exp\left( i \frac{\pi}{2} \lambda_3 ight) = \begin{pmatrix} e^{i\pi/2} & 0 & 0 & 0 \ 0 & e^{-i\pi/2} & 0 & 0 \ 0 & 0 & 1 & 0 \ 0 & 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} i & 0 & 0 & 0 \ 0 & -i & 0 & 0 \ 0 & 0 & 1 & 0 \ 0 & 0 & 0 & 1 \end{pmatrix}$$
**Verifikasi:**
- $U_1^\dagger U_1 = 	ext{diag}(-i, i, 1, 1) 	ext{diag}(i, -i, 1, 1) = I$ (Uniter).
- $\det(U_1) = (i)(-i)(1)(1) = 1$ (Spesial).

## Contoh 2: Matriks Pencampuran (Mixing) pada Indeks 1 dan 2
Menggunakan generator $\lambda_1$ yang merepresentasikan rotasi (seperti matriks Pauli $\sigma_x$).
Misalkan $\alpha_1 = 	heta$:
$$U_2 = \exp(i 	heta \lambda_1) = \begin{pmatrix} \cos	heta & i\sin	heta & 0 & 0 \ i\sin	heta & \cos	heta & 0 & 0 \ 0 & 0 & 1 & 0 \ 0 & 0 & 0 & 1 \end{pmatrix}$$
Untuk $	heta = \pi/4$:
$$U_2 = \begin{pmatrix} 1/\sqrt{2} & i/\sqrt{2} & 0 & 0 \ i/\sqrt{2} & 1/\sqrt{2} & 0 & 0 \ 0 & 0 & 1 & 0 \ 0 & 0 & 0 & 1 \end{pmatrix}$$
**Verifikasi:**
- Matriks ini uniter dan memiliki determinan $\cos^2	heta - (i\sin	heta)^2 = \cos^2	heta + \sin^2	heta = 1$.

## Contoh 3: Elemen Diagonal Global (Menggunakan $\lambda_{15}$)
Generator $\lambda_{15}$ melibatkan semua dimensi. Misalkan kita mengambil parameter $\alpha_{15} = \phi \sqrt{6}$:
$$U_3 = \exp(i \phi \sqrt{6} \lambda_{15}) = \exp \left[ i \phi \begin{pmatrix} 1 & 0 & 0 & 0 \ 0 & 1 & 0 & 0 \ 0 & 0 & 1 & 0 \ 0 & 0 & 0 & -3 \end{pmatrix} ight] = \begin{pmatrix} e^{i\phi} & 0 & 0 & 0 \ 0 & e^{i\phi} & 0 & 0 \ 0 & 0 & e^{i\phi} & 0 \ 0 & 0 & 0 & e^{-3i\phi} \end{pmatrix}$$
**Verifikasi:**
- $U_3^\dagger U_3 = I$ karena setiap elemen diagonal adalah fasa murni.
- $\det(U_3) = e^{i\phi} \cdot e^{i\phi} \cdot e^{i\phi} \cdot e^{-3i\phi} = e^{i(3\phi - 3\phi)} = e^0 = 1$.
- Matriks ini memenuhi syarat $SU(4)$ untuk sembarang nilai $\phi$ riil.
