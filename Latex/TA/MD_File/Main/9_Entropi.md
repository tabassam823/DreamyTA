## Penurunan Rumus
$$\langle \phi | \psi \rangle = \begin{pmatrix} \alpha_{\phi}^* & \beta_{\phi}^* \end{pmatrix} \begin{pmatrix} \alpha_{\psi} \\ \beta_{\psi} \end{pmatrix}$$

## Outer product
$$|\psi \rangle \langle\psi| = \begin{pmatrix} \alpha \\ \beta \end{pmatrix} \begin{pmatrix} \alpha^* & \beta^* \end{pmatrix} $$
dengan matriks densitas
$$\begin{split}
\rho &= |\psi \rangle \langle\psi| \\
&= \begin{pmatrix} \alpha \\ \beta \end{pmatrix} \begin{pmatrix} \alpha^* & \beta^* \end{pmatrix} \\
&= \begin{pmatrix} |\alpha|^2 & \alpha \beta^* \\\beta\alpha^* & |\beta|^2 \end{pmatrix}
\end{split}$$

dimana $|\alpha|^2 + |\beta|^2 = 1$ merupakan syarat normalisasi dalam probabilitas klasik dan $\alpha \beta^* ; \beta \alpha^*$ merupakan koherensi kuantum dimana ia menyimpan inforamsi tentang fasa kuantum dan sifat superposisi.

matriks tersebut dapat dibagi menjadi 2 yaitu
1. pure state sebagai probabilitas klasik dalam jumlahan matriks diagonal 
2. mixed state dengan rumus $\rho = \sum_i p_i |\psi \rangle \langle\psi|$ dimana $p_i$ merupakan pure state
## Penggabungan sistem dengan tensor produk
$$|00\rangle = |0\rangle_A \otimes |0\rangle_B = \begin{pmatrix} 1 \\ 0 \end{pmatrix} \otimes \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \end{pmatrix}$$
### Keadaan terpisah
misal $|\psi\rangle = \frac{1}{\sqrt{2}} \left(|0\rangle + |1\rangle \right)$ 
atur qubit A di state $|0\rangle$ secara pasti dan qubit B dalam keadaan superposisi
$$\begin{split}
|\psi\rangle_{AB} &= |0\rangle_A \otimes \left(\frac{1}{\sqrt2} |0\rangle_B \otimes \frac{1}{\sqrt2} |1\rangle_B \right) \\
&= \frac{1}{\sqrt2} |00\rangle \frac{1}{\sqrt2} |01\rangle
\end{split}$$

### Keadaan terikat
$$
|\Phi^+\rangle_{AB} = \frac{1}{\sqrt2} |00\rangle \frac{1}{\sqrt2} |11\rangle
$$
keadaan tersebut tidak akan bisa dijadikan format matematis $\text{qubit}_A \otimes \text{qubit}_B$ .

## Partial Trace
misal
$$\begin{split}
\text{indeks} \quad 0 &= |00\rangle \\
\text{indeks} \quad 1 &= |01\rangle \\
\text{indeks} \quad 2 &= |10\rangle \\
\text{indeks} \quad 3 &= |11\rangle
\end{split}$$
dengan contoh notasi $\rho[2,2] = |10\rangle \langle10|$ 

jika ingin tahu peluang qubiit A bernilai 0 (elemen [0,0] dari $\rho_A$), maka harus menjumlahkan dua skenario dari matriks gabungan:
$$\rho_A[0,0] = \rho[0,0] + \rho[1,1]$$
Langkah A:
1. saat qubit A = 0 dan qubit B = 0 $\to \rho[0,0] = |00\rangle \langle00|$
2. saat qubit B = 0 dan qubit B = 1 $\to \rho[1,1] = |01\rangle \langle01|$
tiddak peduli qubit B nilainya apa, jika qubit A = 0, kita bisa jumlahkan peluanya.

Langkah B:
1. saat qubit A = 1 dan qubit B = 0 $\to \rho[2,2] = |10\rangle \langle10|$
2. saat qubit B = 1 dan qubit B = 1 $\to \rho[3,3] = |11\rangle \langle11|$

Langkah C:
1. $\rho_A[0,1] = \rho[0,2] + \rho[1,3]$
2. $\rho_A[1,0] = \rho[2,0] + \rho[3,1]$
pada poin 1, qubit A berubah dari 0 menjadi 1, qubit B tetap 0 sehingga 


---
---
# Entropi shannon
$$
H = - \sum_i p_i \log_2 (p_i)
$$
dengan $p_i$ sebagai *pure state* dan dengan hubungan 
$$
\rho = \sum_i p_i |\psi\rangle \langle \psi|
$$
dimana $\rho$ adalah *mixed state* pada sistem kuantum. Melalui dekomposisi spektral, operator densitas $\rho$ dapat dinyatakan dalam basis ortonormal $\{|e_j\rangle\}$ dengan *eigenvalues* $\lambda_j$ sebagai berikut:
$$\begin{split}
\rho &= \sum_j \lambda_j |e_j\rangle \langle e_j| \\
\log_2(\rho) &= \sum_j \log_2 (\lambda_j) |e_j\rangle \langle e_j|
\end{split}$$

Perkalian antara operator $\rho$ dan $\log_2(\rho)$ memanfaatkan sifat ortonormalitas basis $\langle e_j | e_k \rangle = \delta_{jk}$, sehingga:
$$\begin{split}
\rho \log_2(\rho) &= \left(\sum_j \lambda_j |e_j\rangle \langle e_j|\right) \left( \sum_k \log_2 (\lambda_k) |e_k\rangle \langle e_k|\right) \\
&= \sum_j \sum_k \lambda_j \log_2(\lambda_k) |e_j\rangle \langle e_j | e_k\rangle \langle e_k| \\
&= \sum_j \sum_k \lambda_j \log_2(\lambda_k) |e_j\rangle \delta_{jk} \langle e_k| \\
&= \sum_j \lambda_j \log_2(\lambda_j) |e_j\rangle \langle e_j| \quad (1)
\end{split}$$

Langkah selanjutnya adalah menerapkan operasi *trace* ($\text{Tr}$) pada persamaan (1) untuk mendapatkan jumlahan skalar dari elemen diagonalnya:
$$\begin{split}
\text{Tr}(\rho \log_2(\rho)) &= \text{Tr} \left( \sum_j \lambda_j \log_2(\lambda_j) |e_j\rangle \langle e_j| \right) \\
&= \sum_k \langle e_k | \left( \sum_j \lambda_j \log_2(\lambda_j) |e_j\rangle \langle e_j| \right) |e_k\rangle \\
&= \sum_k \sum_j \lambda_j \log_2(\lambda_j) \langle e_k | e_j \rangle \langle e_j | e_k \rangle \\
&= \sum_j \lambda_j \log_2(\lambda_j) \delta_{kj} \delta_{jk} \\
&= \sum_j \lambda_j \log_2(\lambda_j) \quad (2)
\end{split}$$

Berdasarkan definisi entropi sebagai ukuran ketidakteraturan atau hilangnya informasi, maka didapatkan entropi *Von Neumann* ($S$) dengan mengalikan hasil *trace* tersebut dengan tanda negatif:
$$
S(\rho) = -\text{Tr}(\rho \log_2(\rho)) = -\sum_j \lambda_j \log_2 (\lambda_j) \quad (3)
$$
Persamaan (3) menunjukkan bahwa entropi *Von Neumann* merupakan generalisasi dari entropi *Shannon* ke dalam ranah mekanika kuantum, di mana probabilitas klasik digantikan oleh *eigenvalues* dari matriks densitas.