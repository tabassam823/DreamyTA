misal $$u = \begin{pmatrix}u_{11} & u_{12} \\ u_{21} & u_{22}\end{pmatrix}$$ dengan 
1. normalisasi kolom 1: $|u_{11}|^2 + |u_{21}|^2 = 1$
2. normalisasi kolom 2: $|u_{12}|^2 + |u_{22}|^2 = 1$
3. ortogonlitas $u_{11}^* u_{12} + u_{11}^* u_{22} = 0$
	1. $\ket{\psi} = u_{11} \ket{0} + u_{21} \ket{1}$
	2. $\ket{\phi} = u_{12} \ket{0} + u_{21} \ket{1}$
	3. $\langle \psi | \phi \rangle = \begin{pmatrix} u_{11}^* & u_{21}^* \end{pmatrix} \begin{pmatrix} u_{12} \\ u_{22} \end{pmatrix}$  
	4. $U_{22} = \frac{u_{11}^* u_{12}^*}{u_{21}^*}$ substitusi ke (1) dengan manipulasi $|u_{11}| = \cos{\theta}$, maka $|u_{21}| = \sin{\theta}$ 
	5. $$|u_{12}|^2 + \left| \frac{u_{11}^* u_{12}^*}{u_{21}^*} \right|^2 = 1$$
	6. $$|u_{12}|^2 + \left( 1 + \frac{|u_{11}|^2}{|u_{21}|^2} \right) = 1$$
	7. $$|u_{12}|^2 + \left(\frac{|u_{21}|^2 +|u_{11}|^2}{|u_{21}|^2} \right) = 1$$
	8. $$|u_{12}|^2 + \left(\frac{1}{|u_{21}|^2} \right) = 1$$
	9. $$|u_{12}|^2 = |u_{21}|^2 $$
5. $u_{22} =\frac{\cos{\theta} \sin{\theta}}{\sin{\theta}} = \cos{\theta}$
6. manipulasi fase kompleks
	1. $u_{11} = \cos{\theta} e^{i\gamma_1}$
	2. $u_{21} = \sin{\theta} e^{i\gamma_2}$
	3. $u_{12} = \sin{\theta} e^{i\gamma_3}$
	4. $u_{22} = \cos{\theta} e^{i\gamma_4}$
7. masuk ke pers (3) 
$$
\begin{split}
\left( \cos{\theta} e^{-i\gamma_1} \right) \left(\sin{\theta} e^{i\gamma_3}\right) + \left(\sin{\theta} e^{-i\gamma_2} \right) \left(\cos{\theta} e^{i\gamma_4}\right) &= 0 \\
\cos{\theta} \sin{\theta} e^{i(\gamma_3 - \gamma_1)} + \cos{\theta} \sin{\theta} e^{i (\gamma_4 - \gamma_2)} &= 0 \\
e^{i(\gamma_3 - \gamma_1)} + e^{i (\gamma_4 - \gamma_2)} &= 0 \\
e^{i(\gamma_3 - \gamma_1)} &= -e^{i (\gamma_4 - \gamma_2)}
\end{split}$$
karena $e^{i\pi} = -1$, maka 
$$\begin{split}
e^{i(\gamma_3 - \gamma_1)} &= e^{i(\gamma_3 - \gamma_1 - \pi)} \\
i(\gamma_4 - \gamma_2) &= \gamma_3 - \gamma_1 - \pi
\end{split}$$
karena $\gamma_1 = \gamma_4 = \alpha$, maka
$$\begin{split}
\alpha - \gamma_2 &= \gamma_3 - \alpha - \pi \\
\gamma_2 + \gamma_3 &= 2\alpha + \pi
\end{split}$$
sehingga dapat diambil
$$\begin{split}
\gamma_3 &= \alpha + \phi \\
\gamma_2 &= \alpha - \phi + \pi
\end{split}$$dimana $\phi$ digunakan sebagai rotasi fasa baru. 
8. dengan mensubstitusi fasa rotasi tersebut ke persamaan awal menjadi
	1. $$u_{11} = \cos{\theta} e^{i\alpha}$$
	2. $$\begin{split} u_{12} &= \sin{\theta} e^{i\gamma_2} e^{i(\alpha_1 \phi)} \\ &= e^{i\alpha} e^{i\phi} \sin{\theta}  \end{split}$$
	3. $$\begin{split}u_{21} &= \sin{\theta} e^{i(\alpha - \phi + \pi)} \\ &= - e^{i\alpha} e^{-i\phi} \sin{\theta} \end{split}$$
	4. $$u_{22} = \cos{\theta} e^{i\gamma_4} $$
9. sehingga matriks uniter menjadi $$\begin{split}U &= e^{i\alpha} \\ &= \begin{pmatrix}\cos{\theta} & e^{i\phi} \sin{\phi} \\ -e^{i\phi} \sin{\theta} &\cos{\theta} \end{pmatrix} \end{split} $$ untuk kasus determinan 1 (setelah fase global keluar)

---
---
matriks pauli
$$
\sigma_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \quad \sigma_y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} \quad \sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} 
$$
dengan sifat
1. Hermitian $\to x^\dagger = x$
2. Uniter $\to x^\dagger x = I$
3. Trace $\to Tr(x) = 0$
4. Determinant $\to det(x) = -1$

---
$$
\begin{split}
    e^{i \theta \alpha} &= \sum_{n=0}^\infty \frac{(i \theta \alpha)^n}{n!} \\
    &= I + i \theta \alpha - \frac{\theta^2}{2!} \alpha^2 - i \frac{\theta^3}{3!} \alpha^3 + \dots \\
	&= \sum_{n=0}^\infty \frac{(i \theta )^n \hat{p}^n}{n!}
\end{split}
$$
dengan pemisahan ganjil dan genap
$$
\begin{split} 
   e^{i \theta \hat{p}} &= \sum_{k=0}^\infty \frac{(i \theta)^{2k} \hat{p}^{2k}}{(2k)!} + \sum_{k=0}^\infty \frac{(i \theta)^{2k+1} \hat{p}^{2k+1}}{(2k+1)!} \\
   &= \sum_{k=0}^\infty \frac{(i \theta)^{2k} I}{(2k)!} + \sum_{k=0}^\infty \frac{(i \theta)^{2k+1} \hat{p}}{(2k+1)!} \\
    &= \left( \sum_{k=0}^\infty \frac{(-1)^{k} \theta^{2k}}{(2k)!} \right) I + i \left( \sum_{k=0}^\infty \frac{(-1)^{k} \theta^{2k+1}}{(2k+1)!} \right) \hat{p}\\
    &= \cos{\theta} I + i \sin{\theta} \hat{p} \\
	&= \begin{pmatrix} \cos{\theta} & \sin{\theta} \\ \sin{\theta} & \cos{\theta} \end{pmatrix}
\end{split}
$$
untuk $\hat{p} = \sigma_z$

dalam komputasi kuantum, gerbang rotasi didefinisikan sebagai
$$
\begin{split}
    R_z (\theta) &= e^{-i \theta \sigma_z} = \begin{pmatrix}
\cos \theta & -\sin \theta \\
\sin \theta & \cos \theta
\end{pmatrix} \\
	R_y (\theta) &= e^{-i \theta \sigma_y} = \begin{pmatrix}
\cos \theta & -\sin \theta \\
\sin \theta & \cos \theta
\end{pmatrix} \\
	R_x (\theta) &= e^{-i \theta \sigma_x} = \begin{pmatrix}
\cos \theta & -\sin \theta \\
\sin \theta & \cos \theta
\end{pmatrix}
\end{split}
$$
koefisien $\frac{1}{2}$ lahir dari vektor ortogonal di ruang kuantum 2D yang direpresentasikan oleh vektor anti paralel ($180^\circ$) di ruang nyata 3D.
