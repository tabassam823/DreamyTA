# Parameter Shift Rule (PSR)

Parameter Shift Rule adalah teknik fundamental dalam komputasi kuantum variabel (Variational Quantum Circuits) untuk menghitung gradien eksak dari nilai ekspektasi terhadap parameter sirkuit. Berbeda dengan *finite difference* yang hanya memberikan estimasi, PSR memberikan nilai gradien yang analitik dan eksak.

## 1. Sejarah Singkat
Konsep Parameter Shift Rule pertama kali diperkenalkan ke komunitas Quantum Machine Learning oleh **Mitarai et al.** dalam makalah berjudul *"Quantum Circuit Learning"* pada tahun 2018. Tak lama kemudian, **Schuld et al.** memperluas dan menggeneralisasi metode ini dalam makalah *"Evaluating analytic gradients of quantum circuits on quantum hardware"*. 

Sebelum adanya PSR, peneliti sering menggunakan metode *finite difference* (seperti metode Euler) yang memiliki kelemahan pada hardware kuantum yang berisik karena ketidakstabilan numerik saat $\Delta \theta$ sangat kecil. PSR memecahkan masalah ini dengan menggunakan pergeseran parameter yang besar (misal $\pi/2$).

## 2. Definisi Matematis
Misalkan kita memiliki fungsi energi (nilai ekspektasi) $E(\theta)$:
$$E(\theta) = \langle \psi | U^\dagger(\theta) M U(\theta) | \psi \rangle$$

Di mana $U(\theta)$ adalah gerbang unitari yang dibangkitkan oleh operator Pauli $\sigma$ (seperti $X, Y, Z$):
$$U(\theta) = \exp\left(-i \frac{\theta}{2} \sigma\right)$$

Persamaan Parameter Shift Rule menyatakan bahwa turunan $E(\theta)$ terhadap $\theta$ adalah:
$$\frac{\partial E(\theta)}{\partial \theta} = \frac{1}{2} \left[ E\left(\theta + \frac{\pi}{2}\right) - E\left(\theta - \frac{\pi}{2}\right) \right]$$

## 3. Penurunan Rumus (Derivation)

Mari kita turunkan secara bertahap menggunakan sifat-sifat matriks Pauli.

### A. Turunan Langsung
Gunakan aturan perkalian (product rule) pada $E(\theta)$:
$$\frac{\partial E}{\partial \theta} = \langle \psi | \frac{\partial U^\dagger}{\partial \theta} M U | \psi \rangle + \langle \psi | U^\dagger M \frac{\partial U}{\partial \theta} | \psi \rangle$$

Karena $U(\theta) = e^{-i\frac{\theta}{2}\sigma}$, maka:
$$\frac{\partial U}{\partial \theta} = -\frac{i}{2}\sigma U(\theta), \quad \frac{\partial U^\dagger}{\partial \theta} = \frac{i}{2} U^\dagger(\theta) \sigma$$

Substitusikan ke persamaan turunan:
$$\frac{\partial E}{\partial \theta} = \langle \psi | \left(\frac{i}{2} U^\dagger \sigma\right) M U | \psi \rangle + \langle \psi | U^\dagger M \left(-\frac{i}{2} \sigma U\right) | \psi \rangle$$
$$\frac{\partial E}{\partial \theta} = \frac{i}{2} \langle \psi(\theta) | \sigma M - M \sigma | \psi(\theta) \rangle$$
$$\frac{\partial E}{\partial \theta} = \frac{i}{2} \langle \psi(\theta) | [\sigma, M] | \psi(\theta) \rangle \quad \dots (1)$$

### B. Ekspansi Pergeseran Parameter
Gunakan identitas Euler untuk operator Pauli ($\sigma^2 = I$):
$$U(s) = e^{-i\frac{s}{2}\sigma} = \cos\left(\frac{s}{2}\right) I - i \sin\left(\frac{s}{2}\right) \sigma$$

Evaluasi $E(\theta + s)$ di mana $s$ adalah pergeseran:
$$E(\theta + s) = \langle \psi(\theta) | U^\dagger(s) M U(s) | \psi(\theta) \rangle$$
`mengapa s hanya berpengaruh pada U saja dan tidak pada $\psi$`
$$E(\theta + s) = \langle \psi(\theta) | (\cos\frac{s}{2} I + i \sin\frac{s}{2} \sigma) M (\cos\frac{s}{2} I - i \sin\frac{s}{2} \sigma) | \psi(\theta) \rangle$$

Setelah melakukan ekspansi aljabar:
$$E(\theta + s) = \cos^2\frac{s}{2} \langle M \rangle + \sin^2\frac{s}{2} \langle \sigma M \sigma \rangle + \cos\frac{s}{2}\sin\frac{s}{2} \cdot i \langle [\sigma, M] \rangle$$

Dengan cara yang sama untuk $E(\theta - s)$:
$$E(\theta - s) = \cos^2\frac{s}{2} \langle M \rangle + \sin^2\frac{s}{2} \langle \sigma M \sigma \rangle - \cos\frac{s}{2}\sin\frac{s}{2} \cdot i \langle [\sigma, M] \rangle$$

### C. Finalisasi
Kurangi kedua persamaan tersebut:
$$E(\theta + s) - E(\theta - s) = 2 \cos\frac{s}{2} \sin\frac{s}{2} \cdot i \langle [\sigma, M] \rangle$$
Gunakan identitas trigonometri $2\sin A \cos A = \sin 2A$:
$$E(\theta + s) - E(\theta - s) = \sin(s) \cdot i \langle [\sigma, M] \rangle \quad \dots (2)$$

Bandingkan persamaan (2) with persamaan (1). Jika kita pilih $s = \pi/2$:
$$\sin(\pi/2) = 1$$
Maka:
$$E(\theta + \pi/2) - E(\theta - \pi/2) = i \langle [\sigma, M] \rangle$$

Karena dari persamaan (1) kita tahu $\frac{\partial E}{\partial \theta} = \frac{1}{2} \left( i \langle [\sigma, M] \rangle \right)$, maka terbukti bahwa:
$$\frac{\partial E}{\partial \theta} = \frac{1}{2} \left[ E\left(\theta + \frac{\pi}{2}\right) - E\left(\theta - \frac{\pi}{2}\right) \right]$$

## 4. Keunggulan PSR
1.  **Analitik**: Memberikan gradien yang benar-benar eksak, bukan pendekatan.
2.  **Noise Robust**: Karena pergeseran $s$ cukup besar ($\pi/2$), sinyal yang dihasilkan lebih kuat dibandingkan noise hardware, berbeda dengan *finite difference* yang butuh $s$ sangat kecil.
3.  **Implementasi Mudah**: Tidak memerlukan sirkuit tambahan atau tambahan qubit; cukup menjalankan sirkuit yang sama dengan parameter yang berbeda.
