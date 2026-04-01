# Prinsip Variasional (Variational Principle)

## 1. Sejarah Singkat
Prinsip Variasional, khususnya dalam mekanika kuantum, berakar dari kebutuhan untuk memecahkan persamaan Schrödinger pada sistem kompleks yang tidak memiliki solusi analitik eksak. Secara historis, metode ini dikembangkan melalui pendekatan **Rayleigh-Ritz**. Lord Rayleigh menggunakan prinsip ini untuk mempelajari teori suara dan getaran, sementara Walther Ritz memformalkannya sebagai metode numerik untuk mencari nilai eigen dari operator diferensial. Dalam konteks kimia dan fisika kuantum, prinsip ini menjadi fondasi bagi hampir semua metode aproksimasi, termasuk teori fungsional kerapatan (DFT) dan *Variational Quantum Eigensolver* (VQE).

## 2. Fondasi: Kalkulus Variasi dan Fungsional Energi
Secara matematis, prinsip ini bekerja pada sebuah **Fungsional**, yaitu objek yang memetakan sebuah fungsi ke sebuah bilangan real. Dalam mekanika kuantum, energi adalah fungsional dari fungsi gelombang, $E[\psi]$.

Kalkulus variasi mencari fungsi $\psi$ yang membuat fungsional tersebut stasioner (turunannya nol, $\delta E = 0$). Untuk memastikan fungsi gelombang tetap ternormalisasi ($\langle \psi | \psi \rangle = 1$), kita menggunakan teknik **[[Lagrange_Multiplier]]** ($\lambda$):
$$\delta \left( \langle \psi | \hat{H} | \psi \rangle - \lambda (\langle \psi | \psi \rangle - 1) \right) = 0$$

Jika kita variasikan terhadap $\langle \psi |$, kita mendapatkan:
$$\hat{H}|\psi\rangle - \lambda|\psi\rangle = 0 \implies \hat{H}|\psi\rangle = \lambda|\psi\rangle$$
Di sini, pengali Lagrange $\lambda$ secara fisik identik dengan **Energi (E)**. Ini membuktikan bahwa mencari titik stasioner dari fungsional energi adalah ekuivalen dengan menyelesaikan persamaan nilai eigen Schrödinger.

## 3. Konsep Pengali Lagrange (Lagrange Multiplier)
Dalam konteks prinsip variasional, pengali Lagrange adalah teknik matematis untuk menemukan titik ekstrem dari sebuah fungsional yang memiliki kendala (*constraints*). Dalam mekanika kuantum, kendala utamanya adalah **Normalisasi**:
$$\langle \psi | \psi \rangle = 1$$

Teknik ini memungkinkan kita untuk menggabungkan fungsional energi dan kendala normalisasi ke dalam satu fungsional baru:
$$\mathcal{L}[\psi, \lambda] = \langle \psi | \hat{H} | \psi \rangle - \lambda (\langle \psi | \psi \rangle - 1)$$

Di sini, $\lambda$ adalah pengali Lagrange. Dengan mencari $\delta \mathcal{L} = 0$, kita secara otomatis menjamin bahwa solusi yang ditemukan meminimalkan energi sekaligus memenuhi syarat normalisasi. Seperti yang ditunjukkan pada bagian sebelumnya, $\lambda$ ini akhirnya terbukti secara matematis sebagai nilai eigen energi $E$.

## 4. Detail Matematis Penurunan Rumus (Metode Rayleigh-Ritz)
Prinsip Variasional mempostulatkan bahwa nilai ekspektasi energi dari sembarang fungsi gelombang percobaan (*trial wavefunction*) $|\psi_{trial}\rangle$ akan selalu merupakan batas atas bagi energi keadaan dasar sejati ($E_0$) dari sebuah sistem.

### Derivasi:
Diberikan sebuah Hamiltonian $\hat{H}$ yang independen terhadap waktu, dengan kumpulan state eigen $|n\rangle$ dan nilai eigen $E_n$ sedemikian rupa sehingga:
$$\hat{H}|n
\rangle = E_n|n
\rangle$$
Asumsikan state eigen diurutkan berdasarkan energinya: $E_0 \leq E_1 \leq E_2 \leq \dots$

Sembarang fungsi gelombang percobaan $|\psi_{trial}\rangle$ dapat diekspansikan sebagai kombinasi linier dari state-state eigen tersebut (karena mereka membentuk basis ortonormal yang lengkap):
$$|\psi_{trial} \rangle = \sum_n c_n |n
\rangle$$

Nilai ekspektasi energi untuk $|\psi_{trial}\rangle$ didefinisikan sebagai:
$$\langle E 
\rangle = \frac{\langle \psi_{trial} | \hat{H} | \psi_{trial} 
\rangle}{\langle \psi_{trial} | \psi_{trial} 
\rangle}$$

Substitusikan ekspansi kombinasi linier ke dalam pembilang:
$$\langle \psi_{trial} | \hat{H} | \psi_{trial} 
\rangle = \sum_m \sum_n c_m^* c_n \langle m | \hat{H} | n 
\rangle = \sum_m \sum_n c_m^* c_n E_n \delta_{mn} = \sum_n |c_n|^2 E_n$$

Karena $E_n \geq E_0$ untuk semua $n$, maka:
$$\sum_n |c_n|^2 E_n \geq E_0 \sum_n |c_n|^2$$

Karena $\sum_n |c_n|^2 = \langle \psi_{trial} | \psi_{trial} \rangle$, maka kita mendapatkan ketidaksamaan fundamental:
$$\frac{\langle \psi_{trial} | \hat{H} | \psi_{trial} 
\rangle}{\langle \psi_{trial} | \psi_{trial} 
\rangle} \geq E_0$$

Artinya, dengan meminimalisasi nilai ekspektasi energi melalui parameter-parameter dalam $|\psi_{trial} \rangle$, kita akan mendekati nilai energi ground state yang sebenarnya.

## 5. Aplikasi Umum
Dalam komputasi klasik, prinsip ini digunakan untuk:
- **Aproksimasi Ground State:** Mencari energi terendah dari sistem seperti atom Helium atau osilator harmonik yang kompleks.
- **Metode Hartree-Fock:** Menggunakan fungsi gelombang berupa determinan Slater dan memvariasikan orbital untuk meminimalkan energi total sistem elektron.
- **Stabilitas Sistem:** Memastikan bahwa sistem fisik berada pada titik energi minimum (kesetimbangan).

## 6. Aplikasi Khusus pada VQE (Variational Quantum Eigensolver)

VQE adalah algoritma *hybrid* quantum-klasik yang menerapkan prinsip variasional secara langsung untuk mencari energi terendah dari sebuah Hamiltonian (misalnya Ising Hamiltonian dalam optimasi portofolio atau Hamiltonian molekuler dalam kimia).

### Mekanisme VQE:
1. **Ansatz (Parameterized Quantum Circuit):** Kita menyiapkan fungsi gelombang percobaan $|\psi(\theta)\rangle$ menggunakan sirkuit kuantum terparameterisasi.
   $$|\psi(\theta)
\rangle = \hat{U}(\theta)|0
\rangle$$
2. **Evaluasi Quantum:** Komputer kuantum digunakan untuk mengukur nilai ekspektasi energi $E(	\theta) = \langle \psi(	\theta) | \hat{H} | \psi(	\theta) \rangle$. Karena sirkuit kuantum bersifat uniter, state $|\psi(	\theta)\rangle$ sudah otomatis ternormalisasi.
3. **Optimasi Klasik:** Nilai $E(	\theta)$ dikirim ke optimizer klasik (seperti SPSA atau COBYLA) untuk memperbarui parameter $\theta$ guna meminimalkan $E(	\theta)$.
4. **Iterasi:** Proses berulang hingga konvergensi tercapai ($\Delta E \approx 0$).

### Interpretasi dalam Optimasi Portofolio:
Dalam konteks ekonomi (seperti pada @Latex/PakHeru_Presentasi4/Rencana_Penjelasan_VQE.md), *Ground State* yang ditemukan melalui prinsip variasional ini mewakili **Market Regime Optimal** atau konfigurasi portofolio dengan risiko minimum dan return tertentu yang telah dipetakan ke dalam Ising Hamiltonian. VQE tidak memprediksi masa depan, melainkan mengidentifikasi kondisi ekuilibrium yang paling stabil/menguntungkan dalam "permainan" pasar tersebut.
