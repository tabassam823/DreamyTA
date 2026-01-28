# Rencana Presentasi 2: Eksplorasi Model Game Theory Kuantum

## 1. Pendahuluan
Dokumen ini berisi rencana materi untuk presentasi kedua, yang berfokus pada variasi model Game Theory yang dapat diselesaikan menggunakan metode matematika fisika kuantum. Fokus utama adalah membandingkan berbagai skema kuantisasi dan aplikasinya, termasuk Marinatto-Weber, EWS, EWL, dan pendekatan Bayesian.

## 2. Model Game Theory

### A. Model Marinatto-Weber
*   **Sumber**:
    *   `notes/Marinatto_Weber.pdf` (Penjelasan Konseptual).
    *   `paper/On_Correlated Equilibria_in_Marinatto–Weber_ Type_Quantum_Games.pdf` (Analisis Hubungan dengan Correlated Equilibria - P. Frackiewicz, 2020).
*   **Deskripsi Model**:
    *   Merupakan skema kuantisasi yang lebih "straightforward" dibandingkan EWL.
    *   **Mekanisme**:
        *   **State Awal**: Dimulai dengan state basis (misal $|\psi_{in}\rangle = |CC\rangle$).
        *   **Strategi**: Pemain menggunakan **operator permutasi** (seperti Identitas $I$ atau Pauli-X $\sigma_x$ untuk membalik state) yang bekerja pada ruang Hilbert masing-masing.
        *   **Payoff**: Dihitung melalui nilai ekspektasi (Trace) dari operator densitas akhir terhadap operator payoff.
*   **Temuan Penting**:
    *   Terdapat hubungan erat antara **Correlated Equilibria** (klasik) dan **Nash Equilibria** dalam skema MW.
    *   Penggunaan state terbelit (entangled) dalam skema MW memungkinkan pemain mencapai hasil yang setara dengan *correlated equilibrium* klasik (yang biasanya butuh mediator/komunikasi), tanpa komunikasi klasik.
*   **Status**: *Drafted* (Analisis sumber selesai).

### B. Model EWS (Eisert-Wilkens-Schmitz)
*   **Sumber**: `notes/EWS_Model.pdf` (Catatan/Foto Papan Tulis).
*   **Deskripsi Model**:
    *   Merupakan protokol yang dirancang untuk menyelesaikan dilema klasik (seperti Prisoner's Dilemma) menggunakan hukum mekanika kuantum.
    *   **Mekanisme**:
        1.  **Persiapan**: State awal $|CC\rangle$.
        2.  **Entanglement**: Operator $J$ mengikat state pemain (analoginya seperti menghubungkan koin dengan "benang gaib").
        3.  **Strategi**: Pemain menggunakan operator uniter $U(\theta, \phi)$ pada qubit mereka.
            *   Strategi tidak lagi biner (0/1) tapi kontinu pada **Bola Bloch**.
            *   Parameter $\theta$ dan $\phi$ memungkinkan strategi "campuran" kuantum (misal: "sedikit curang").
        4.  **Un-entanglement & Pengukuran**: Operator $J^\dagger$ melepaskan ikatan sebelum pengukuran final.
*   **Karakteristik**:
    *   Memperluas ruang strategi dari diskrit ke kontinu.
    *   Memungkinkan solusi Pareto optimal yang tidak ada di klasik.

### C. Model EWL (Eisert-Wilkens-Lewenstein)
*   **Sumber**:
    *   `paper/Quantum_Game_Theory/A_New_Quantization_Scheme for_Classica_Games.pdf` (Dmitry Kravchenko - Generalisasi EWL).
    *   `paper/Quantum_Game_Theory/Eisert_Wilkens_Lewenstein_scheme.pdf` (Kameshwari & Balakrishnan - Modified EWL, Decoherence, & Memory).
*   **Deskripsi Model**:
    *   Skema kuantisasi standar dan paling fundamental dalam Game Theory Kuantum.
    *   **Protokol Dasar**:
        1.  Referee menyiapkan sistem multipartite dalam state terbelit (entangled).
        2.  Sistem didistribusikan ke pemain.
        3.  Pemain menerapkan operasi uniter lokal.
        4.  Referee melakukan operasi invers/lanjutan dan pengukuran.
    *   **Pengembangan**:
        *   **Modified EWL**: Menghapus syarat bahwa game klasik harus menjadi subset dari game kuantum, memungkinkan penggunaan operator entangling yang lebih luas.
        *   **Generalisasi**: Perluasan skema untuk game dengan $N$ pemain dan $M$ strategi (bukan hanya 2x2).
        *   **Faktor Realistik**: Studi mengenai pengaruh **Decoherence** (noise) yang menurunkan payoff dan **Memory** yang dapat menaikkan payoff kembali.

### D. Model Bayesian Quantum Game
*   **Sumber Utama**: 
    *   *Judul*: "Characterizing the Nash equilibria of a three-player Bayesian quantum game"
    *   *Penulis*: Neal Solmeyer, Ricky Dixon, Radhakrishnan Balu (Quantum Information Processing, 2017).
    *   *File*: `paper/Bayesian/Characterizing_the_Nash_equilibria_of_a_three_player_Bayesian_quantum_game.pdf`

*   **Intisari Model**:
    1.  **Konsep Dasar**:
        *   Menggabungkan **Game Theory dengan informasi tidak lengkap (Bayesian Game)** ke dalam kerangka kuantum.
        *   Studi kasus menggunakan **Prisoner's Dilemma (PD)** dengan **tiga pemain**.
    
    2.  **Struktur Permainan**:
        *   **Pemain**: Terdapat tiga pemain. Pemain pertama menghadapi ketidakpastian mengenai "tipe" dari lawannya (Pemain 2).
        *   **Ketidakpastian (Bayesian Nature)**: Dikodekan dalam probabilitas klasik $p$ dan $1-p$ (atau amplitudo fungsi gelombang) bahwa Pemain 2 adalah tipe tertentu.
        *   **Formalisme**: Menggunakan skema **EWL (Eisert-Wilkens-Lewenstein)**. Qubit merepresentasikan state pemain, gate kuantum (uniter) sebagai strategi, dan entanglement sebagai mediator komunikasi.

    3.  **Temuan Utama**:
        *   Identifikasi kelas **Nash Equilibria (NE)** yang memiliki struktur kaya, dikarakterisasi oleh hubungan fase pada strategi pemain.
        *   **Keunggulan Kuantum**: Payoff pada NE dalam versi kuantum dapat melebihi versi klasik (mencapai Pareto optimality yang tidak mungkin di klasik).
        *   Struktur NE ini memungkinkan wasit untuk mengatur aturan permainan guna mendorong pemain menuju hasil kesetimbangan tertentu.

### E. Model Quantum Barro-Gordon
*   **Sumber**:
    *   *Judul*: "Quantum Barro-Gordon Game in Monetary Economics"
    *   *Penulis*: Ali Hussein Samadi, Afshin Montakhab, Hussein Marzban, Sakine Owjimehr (arXiv:1708.05689, 2017).
    *   *File*: `paper/Quantum_Barro-Gordon_Game_in_Monetary_Economics.pdf`
*   **Deskripsi Model**:
    *   **Konteks Aplikasi**: Menerapkan Game Theory Kuantum pada **Ekonomi Moneter**, spesifiknya pada masalah **Inkonsistensi Waktu (Time Inconsistency)**.
    *   **Masalah Klasik**: *Time Inconsistency* muncul ketika pembuat kebijakan "lemah" tergiur untuk menetapkan inflasi tinggi ketika publik mengharapkan inflasi rendah, demi meningkatkan output jangka pendek. Hal ini menyebabkan bias inflasi.
    *   **Skema Kuantisasi**: Menggunakan pendekatan **Marinatto-Weber (MW)** (bukan EWL).
*   **Temuan Utama**:
    *   Kuantisasi permainan dapat **menghilangkan masalah inkonsistensi waktu**.
    *   Ditemukan **Nash Equilibrium** yang konsisten terhadap waktu (time-consistent) di mana publik mengharapkan inflasi rendah dan pembuat kebijakan menepatinya, sebuah hasil yang sulit dicapai secara stabil dalam model klasik tanpa mekanisme komitmen eksternal.
    *   Menunjukkan potensi aplikasi riil Game Theory Kuantum dalam **Ekonofisika** (Econophysics).

## 3. Formulasi Matematis & Premi Dasar

Bagian ini menguraikan struktur matematis dan asumsi dasar yang membangun setiap model permainan.

### A. Marinatto-Weber (MW)
*   **Premi Dasar**: Permainan dimainkan dengan menerapkan operator klasik (atau probabilitas penerapannya) pada ruang Hilbert bersama yang statis. State awal memuat korelasi (entanglement) yang bertindak sebagai sumber koordinasi tanpa komunikasi.
*   **Formulasi**:
    *   **State Awal**: $|\Psi_{in}\rangle = \sum_{i,j} \alpha_{ij} |ij\rangle$ (State terbelit dalam $\mathcal{H}_A \otimes \mathcal{H}_B$).
    *   **Strategi**: Pemain $k$ memilih operator identitas $I$ atau inversi $\sigma_x$ (atau permutasi $V_k$ untuk dimensi $N$).
        *   State Akhir: $|\Psi_{fin}\rangle = (\hat{O}_A \otimes \hat{O}_B) |\Psi_{in}\rangle$.
    *   **Payoff**: Nilai ekspektasi dari operator payoff $M_i$.
        $$ \$(\hat{A}, \hat{B}) = \text{Tr}( |\Psi_{fin}\rangle\langle\Psi_{fin}| \cdot M_i ) $$
        dimana $M_i = \sum_{j,k} u_i(s_j, s_k) |jk\rangle\langle jk|$.

### B. Eisert-Wilkens-Lewenstein (EWL)
*   **Premi Dasar**: Permainan terjadi di "domain kuantum" yang diakses melalui operator entanglement $J$ dan diakhiri dengan disentanglement $J^\dagger$. Strategi pemain adalah rotasi lokal qubit yang memanfaatkan superposisi dan interferensi amplitudo.
*   **Formulasi**:
    *   **State Awal**: $|\psi_0\rangle = |00\rangle$.
    *   **Protokol**:
        1.  **Entangling**: $|\psi_{ent}\rangle = \hat{J} |00\rangle$, biasanya $\hat{J} = \exp(i \frac{\gamma}{2} \sigma_x \otimes \sigma_x)$.
        2.  **Strategi**: $|\psi_{strat}\rangle = (\hat{U}_A \otimes \hat{U}_B) |\psi_{ent}\rangle$, dengan $\hat{U} \in SU(2)$.
        3.  **Disentangling**: $|\psi_{fin}\rangle = \hat{J}^\dagger |\psi_{strat}\rangle$.
    *   **Payoff**: Probabilitas pengukuran state basis dikalikan matriks payoff klasik.
        $$ \$ = \sum_{s \in \{00, 01, 10, 11\}} P(s) \cdot u(s) = \sum_{s} |\langle s | \psi_{fin} \rangle|^2 \cdot u(s) $$

### C. Bayesian Quantum Game
*   **Premi Dasar**: Memperluas EWL ke kondisi informasi tidak lengkap. Payoff bergantung pada "tipe" pemain yang ditentukan oleh alam (Nature) dengan probabilitas tertentu. Kuantisasi memungkinkan korelasi non-lokal (seperti ketidaksetaraan Bell) yang tidak bisa dicapai klasik.
*   **Formulasi**:
    *   **Struktur Payoff**: Rata-rata terbobot dari payoff permainan kuantum untuk setiap tipe.
        $$ \$_{Bayes} = \sum_{t \in Tipe} p(t) \cdot \$_{Quantum}(\text{Strategi}, t) $$
    *   **Kondisi Konsistensi**: Ekspektasi nilai harus memenuhi kondisi *no-signaling* (persamaan 2 dalam paper referensi), memastikan bahwa statistik "saran" (entanglement) satu pemain tidak bergantung pada tipe pemain lain secara instan.

### D. Quantum Barro-Gordon
*   **Premi Dasar**: Aplikasi skema MW pada fungsi utilitas makroekonomi. Masalah *Time Inconsistency* diatasi karena entanglement mengubah struktur payoff sehingga strategi "janji palsu" (cheating) tidak lagi menjadi dominan atau menguntungkan.
*   **Formulasi**:
    *   **Fungsi Utilitas (Klasik)**:
        *   Policy Maker: $U^{pol} = \theta b (\pi - \pi^e) - \frac{a \pi^2}{2}$
        *   Public: $U^{pub} = - (\pi - \pi^e)^2$
    *   **Kuantisasi**:
        *   Strategi $\pi$ (inflasi) dan $\pi^e$ (ekspektasi) dipetakan ke operator Hilbert space (misal $|0\rangle \to$ inflasi rendah, $|1\rangle \to$ inflasi tinggi).
        *   Payoff Kuantum:
            $$ \langle U^{pol} \rangle_Q = \text{Tr}(\rho_{fin} \cdot \hat{H}_{pol}) $$
        dimana $\hat{H}_{pol}$ adalah operator Hamiltonian yang dikonstruksi dari fungsi utilitas klasik.

## 4. Contoh Kasus Implementasi (Alice & Bob)

Untuk memperjelas perbedaan mekanisme, berikut adalah ilustrasi kasus penggunaan karakter standar "Alice" dan "Bob".

### A. Kasus Marinatto-Weber: "Koin Terbelit"
*   **Skenario**: Alice dan Bob bermain Prisoner's Dilemma. Alih-alih memilih kartu tertutup, mereka diberi masing-masing satu koin dari pasangan koin yang sudah disiapkan wasit dalam keadaan terbelit (entangled).
*   **Aksi**:
    *   Alice memilih untuk membiarkan koinnya (Identitas, $I$) atau membaliknya (Flip, $\sigma_x$).
    *   Bob melakukan hal yang sama pada koinnya.
*   **Hasil**: Karena koin terbelit, jika Alice membalik koinnya, koin Bob mungkin ikut berubah statusnya relatif terhadap pengukuran akhir.
*   **Poin Kunci**: Mereka bisa mencapai kesepakatan (kooperasi) seolah-olah mereka telah berunding sebelumnya, meskipun mereka berada di ruang terpisah. Ini disebut *Correlated Equilibrium*.

### B. Kasus EWL: "Strategi Ajaib"
*   **Skenario**: Alice dan Bob bermain Prisoner's Dilemma, tetapi kali ini mereka diberi "Bola Kuantum" (Qubit).
*   **Aksi**:
    *   Bob (pemain klasik) hanya bisa memutar bola ke "Atas" (Kooperasi) atau "Bawah" (Khianat).
    *   Alice (pemain kuantum) bisa memutar bola ke arah "Samping" (Superposisi/Fase $i\sigma_y$).
*   **Hasil**: Strategi Alice yang "tegak lurus" terhadap dimensi klasik membuat pilihan Bob tidak relevan. Alice bisa memanipulasi hasil akhir sehingga ia selalu menang atau memaksa hasil Pareto Optimal (Kooperasi-Kooperasi) tanpa takut dikhianati.
*   **Poin Kunci**: Strategi kuantum mengalahkan strategi klasik.

### C. Kasus Bayesian: "Bob yang Misterius"
*   **Skenario**: Alice bermain melawan Bob. Namun, Alice tidak tahu apakah Bob sedang dalam *mood* "Kooperatif" (Tipe 1) atau "Kompetitif" (Tipe 2).
*   **Aksi**:
    *   Alice harus memilih satu strategi rotasi uniter $U_A$ yang bekerja baik untuk kedua kemungkinan tipe Bob.
    *   Bob memilih strategi berdasarkan tipe aslinya.
*   **Hasil**: Dengan memanfaatkan entanglement, Alice bisa memilih strategi yang memanfaatkan korelasi non-lokal. Payoff Alice menjadi rata-rata terbobot yang lebih tinggi daripada jika ia hanya menebak tipe Bob secara klasik.
*   **Poin Kunci**: Entanglement bertindak sebagai "saran rahasia" yang valid untuk kedua tipe Bob.

### D. Kasus Barro-Gordon: "Bank vs Publik"
*   **Skenario**:
    *   **Alice (Bank Sentral)**: Ingin inflasi rendah (janji), tapi tergiur menaikkan inflasi diam-diam (selingkuh) demi profit jangka pendek.
    *   **Bob (Publik)**: Mencoba menebak langkah Alice.
*   **Masalah Klasik**: Alice berjanji inflasi rendah ($0$), Bob percaya ($0$). Tapi Alice lalu curang ($1$) untuk untung. Bob kapok, besoknya Bob selalu tebak tinggi ($1$), Alice terpaksa tinggi ($1$). Keduanya rugi.
*   **Solusi Kuantum**:
    *   Alice dan Bob bermain menggunakan qubit terbelit.
    *   Struktur payoff kuantum (via MW scheme) mengubah matriks insentif.
    *   Keadaan di mana Alice curang tidak lagi memberikan keuntungan maksimal karena adanya korelasi kuantum yang "menghukum" strategi campuran/curang.
    *   **Hasil**: Alice konsisten menepati janji inflasi rendah, dan Bob percaya. Ekuilibrium tercapai di (Rendah, Rendah).

## 5. Rencana Analisis Selanjutnya

### Perbandingan Komparatif (Tabel)

| Fitur                  | Marinatto-Weber (MW)                               | EWL / EWS                                | Bayesian Quantum                      | Barro-Gordon (Quantum)                             |
| :--------------------- | :------------------------------------------------- | :--------------------------------------- | :------------------------------------ | :------------------------------------------------- |
| **Basis Strategi**     | Probabilitas Klasik pada State Kuantum / Permutasi | Operator Uniter (Rotasi di Bola Bloch)   | Uniter + Probabilitas Tipe (Bayesian) | Probabilitas Klasik pada State Kuantum (MW Scheme) |
| **Peran Entanglement** | Korelasi (mirip Correlated Eq.)                    | Interferensi & Superposisi Strategi      | Encoding Informasi & Strategi         | Resolusi Inkonsistensi Kebijakan                   |
| **Ruang Strategi**     | Diskrit (Permutasi)                                | Kontinu (Parameter Sudut $\theta, \phi$) | Kontinu + Ketidakpastian Tipe         | Diskrit (Kebijakan Inflasi Rendah/Tinggi)          |
| **Kompleksitas**       | Rendah (Straightforward)                           | Tinggi (Manipulasi Fase)                 | Sangat Tinggi (3 Pemain + Tipe)       | Menengah (Aplikasi Ekonomi)                        |

### Langkah Berikutnya
1. Menyusun slide presentasi berdasarkan struktur ini.
2. Memvalidasi detail matematis dari "Modified EWL" untuk melihat apakah relevan dengan kasus sederhana.
3. Simulasi numerik sederhana untuk membandingkan payoff MW vs EWL (jika waktu memungkinkan).
