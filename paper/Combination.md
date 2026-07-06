# 1. Finance and Portofolio Optimization
## <u>Modern Portofolio Theory (Markowitz Model)</u>
Model Markowitz, atau *Mean-Variance Model*, adalah fondasi dari teori portofolio modern yang mengkuantifikasi hubungan antara risiko dan imbal hasil.
* **Konsep Utama**: Menggunakan varians (atau standar deviasi) sebagai ukuran risiko dan rata-rata historis sebagai ekspektasi imbal hasil. 
* **Efficient Frontier**: Menghasilkan set portofolio optimal di mana tidak ada portofolio lain yang memberikan imbal hasil lebih tinggi untuk tingkat risiko yang sama.
* **Formulasi Matematis**: Merupakan masalah *quadratic programming* yang bertujuan meminimalkan varians portofolio:
  $$\min \sigma_P^2 = \sum_{j=1}^N \sum_{i=1}^N w_i w_j \text{Cov}_{i,j}$$
  dengan kendala: $\sum w_i R_i = C$, $\sum w_i = 1$, dan $w_i \ge 0$.
* **Keterbatasan**: Sangat bergantung pada akurasi data input, mengasumsikan distribusi return normal (stasioneritas), dan memperlakukan fluktuasi positif (keuntungan) sama dengan fluktuasi negatif (kerugian).

## <u>Value at Risk (VaR) & Conditional Value at Risk (CVaR)</u>
* **Value at Risk (VaR)**: Diperkenalkan oleh JP Morgan (1994), VaR adalah ukuran risiko sintetis yang mengestimasi kerugian maksimum yang mungkin terjadi pada aset atau portofolio dalam periode waktu tertentu dengan tingkat kepercayaan tertentu.
    * **Kelemahan**: VaR tidak memenuhi prinsip *subadditivity*, sehingga tidak dianggap sebagai ukuran risiko yang koheren (artinya, diversifikasi mungkin tidak terlihat mengurangi risiko secara matematis).
* **Conditional Value at Risk (CVaR)**: Diperkenalkan oleh Rockafellar dan Uryasev (2000) untuk mengatasi kelemahan VaR. CVaR (atau *Expected Shortfall*) mengukur nilai rata-rata (ekspektasi) dari kerugian yang melebihi ambang batas VaR.
    * **Kelebihan**: Merupakan ukuran risiko yang koheren dan memungkinkan optimasi portofolio menggunakan pemrograman linear (*linear programming*), yang seringkali lebih efisien daripada pemrograman kuadratik.
* **Formulasi Model CVaR**:
  Bertujuan untuk meminimalkan ekspektasi kerugian ekor (*tail loss*):
  $$\min \text{CVaR}_\alpha = \text{VaR} + \frac{1}{m\alpha} \sum_{t=1}^m d_t$$
  di mana $d_t$ adalah deviasi di bawah VaR: $d_t = \max(\text{VaR} - \sum_{i=1}^N R_{it} w_i, 0)$.
## <u>Merton Model</u>
Diperkenalkan oleh Robert C. Merton (1969), ini adalah model optimasi portofolio waktu kontinu (*continuous-time*) di mana investor memutuskan alokasi antara aset berisiko dan bebas risiko untuk memaksimalkan utilitas konsumsi inter-temporal.
*   **Dinamis vs Statis**: Berbeda dengan Markowitz yang statis (satu periode), Model Merton memungkinkan penyesuaian portofolio secara aktif (*rebalancing*) merespons perubahan kondisi pasar dan volatilitas.
*   **Asumsi**: Harga aset mengikuti *Geometric Brownian Motion* (GBM), perdagangan kontinu tanpa biaya transaksi, dan tidak ada risiko gagal bayar (*default*).
*   **Solusi**: Masalah ini diselesaikan menggunakan persamaan Hamilton–Jacobi–Bellman (HJB) untuk menemukan strategi konsumsi dan investasi optimal.

## <u>CCAPM & CRRA</u>
*   **CCAPM (Consumption Capital Asset Pricing Model)**: Model yang mengaitkan ketidakpastian pengembalian aset dengan konsumsi. Dalam literatur *multi-agent* (misalnya Tapiero, 2015), CCAPM sering diperluas menggunakan pendekatan *Game Theory*, di mana setiap agen dianggap bermain ("gaming the market") melawan agregat pasar atau agen lainnya, menciptakan keseimbangan harga konsumsi yang unik.
*   **CRRA (Constant Relative Risk Aversion)**: Kelas fungsi utilitas yang digunakan dalam Model Merton (dan varian *multi-agent*-nya) untuk menjamin *tractability* matematis.
    *   Bentuk umum: $U(c) = \frac{c^{1-\gamma}}{1-\gamma}$ (Power Utility) atau $U(c) = \ln(c)$ (Log Utility).
    *   Karakteristik: Penghindaran risiko relatif tetap konstan seiring perubahan kekayaan, memungkinkan ditemukannya solusi bentuk tertutup (*closed-form solution*) untuk alokasi portofolio optimal.

# 2. Quantum and Game Theory

## <u>Klasik to Quantum</u> 
Konsep ini menjembatani teori permainan klasik dengan mekanika kuantum, di mana strategi pemain diperluas dari pilihan deterministik atau probabilistik (mixed) menjadi operasi uniter pada sistem kuantum.

### Prisoner's Dilemma
Salah satu contoh paling terkenal dalam teori permainan non-kooperatif.
*   **Kasus Klasik**: Dua tahanan diinterogasi terpisah. Pilihan rasional (Nash Equilibrium) bagi keduanya adalah "mengaku" (*defect*), yang menghasilkan hukuman lebih berat (misal 4 tahun) dibandingkan jika keduanya "menyangkal" (*cooperate*) (2 tahun).
*   **Versi Kuantum**: Menggunakan skema EWL (Eisert-Wilkens-Lewenstein). Dengan memanfaatkan *quantum entanglement* maksimal ($\gamma = \pi/4$), pemain dapat mengakses strategi baru yang memungkinkan mereka lolos dari dilema dan mencapai hasil Pareto optimal (saling bekerja sama) secara rasional.

### Teknik Kuantisasi Permainan
Paper Kravchenko mengusulkan skema baru untuk mengkuantisasi permainan dengan jumlah pemain ($N$) dan pilihan strategi ($M$) yang sembarang, melampaui batasan biner skema EWL.
*   **Protokol**:
    1.  **Inisialisasi**: Sistem kuantum $N$-qudit disiapkan (tiap qudit memiliki $M$ level).
    2.  **Entangling**: Operator $\hat{J}$ diterapkan untuk menciptakan korelasi kuantum antar pemain.
    3.  **Strategi**: Pemain menerapkan operasi uniter lokal ($\hat{U}$) pada qudit mereka masing-masing.
    4.  **Disentangling & Pengukuran**: Operator $\hat{J}^\dagger$ diterapkan kembali, diikuti pengukuran untuk menentukan *payoff*.
*   **Backward Compatibility**: Operator $\hat{J}$ dirancang khusus agar jika pemain membatasi diri pada strategi klasik (matriks permutasi/shift), permainan kembali persis ke bentuk klasiknya.

### Permainan Voting
Aplikasi dari skema kuantisasi $N$-pemain pada masalah pemilihan sosial (misal: 3 pemilih, 4 kandidat).
*   **Masalah**: Dalam sistem klasik, pemungutan suara taktis atau egois (*selfish voting*) sering mengarah pada hasil yang kurang optimal bagi kesejahteraan bersama.
*   **Solusi Kuantum**: Simulasi menunjukkan bahwa strategi kuantum memungkinkan pemilih untuk keluar dari jebakan Nash equilibrium klasik yang buruk dan berevolusi menuju titik Pareto optimal, memberikan manfaat kolektif yang lebih besar.

### Pengantar Model Permainan Kompleks
Transisi dari "permainan matriks 2x2" sederhana ke "Games with Quantum Decisions" yang lebih kompleks.
*   **Skala**: Melibatkan banyak pemain (*multi-player*) dan banyak pilihan (*multi-choice*).
*   **Kompleksitas**: Mencari Nash Equilibrium di ruang strategi kuantum (yang kontinu dan berdimensi tinggi) jauh lebih sulit daripada kasus klasik. Namun, ruang strategi yang lebih luas ini membuka peluang solusi kooperatif yang tidak eksis di dunia klasik.


## <u>MW dan EWL Scheme</u>
Dalam teori permainan kuantum, terdapat dua skema kuantisasi utama yang digunakan secara luas untuk memperluas permainan klasik ke ranah kuantum: Skema Marinatto-Weber (MW) dan Skema Eisert-Wilkens-Lewenstein (EWL). Kedua skema ini memanfaatkan sifat mekanika kuantum, terutama *entanglement*, untuk memberikan keuntungan strategis yang tidak mungkin dicapai dalam permainan klasik.

## <u>Marinatto-Weber</u>
Skema ini merupakan salah satu dari dua metode kuantisasi yang tersedia. Dalam literatur, skema MW dikenal pendekatannya pada permainan statis dengan informasi lengkap. (Catatan: Dokumen referensi utama lebih berfokus pada EWL dan variannya, hanya menyebut MW sebagai alternatif standar).

## <u>Eisert Wilkens Lewenstein (EWL)</u>
Skema EWL adalah metode kuantisasi yang paling terkenal, diperkenalkan untuk menyelesaikan dilema dalam permainan klasik (seperti *Prisoner's Dilemma*) menggunakan sirkuit kuantum.
*   **Prinsip Dasar**: Permainan dimulai dengan keadaan awal yang dibuat *entangled* oleh arbiter menggunakan operator $J$. Pemain kemudian menerapkan strategi mereka berupa operator uniter lokal ($U \in SU(2)$), diikuti oleh operator *disentangling* $J^\dagger$ dan pengukuran.
*   **Syarat Klasik**: EWL mensyaratkan bahwa permainan klasik harus menjadi himpunan bagian (*subset*) dari versi kuantumnya.
*   **Keterbatasan**: Akibat syarat di atas, operator *entangling* $J$ terbatas hanya pada kelas *controlled unitary operators*. Hal ini dikritik karena membatasi eksplorasi penuh terhadap sifat kuantum permainan.

## <u>Modified EWL</u>
Diusulkan untuk mengatasi keterbatasan skema EWL orisinal dengan mencabut persyaratan bahwa permainan klasik harus menjadi subset.
*   **Fleksibilitas Operator**: Memungkinkan penggunaan operator *entangling* dua-qubit yang jauh lebih luas (sembarang $J \in SU(4)$), tidak terbatas pada *controlled unitaries*. Ini membuka peluang untuk menemukan *Nash Equilibrium* yang lebih superior.
*   **Decoherence & Memory**:
    *   **Decoherence (Noise)**: Interaksi dengan lingkungan yang menyebabkan hilangnya informasi kuantum, yang umumnya menurunkan *payoff* pemain.
    *   **Memory**: Pengetahuan pemain tentang strategi sukses masa lalu. Studi menunjukkan bahwa memori dapat mengkompensasi penurunan *payoff* akibat *decoherence*.
*   **Temuan**: Dengan memilih operator *entangling* yang tepat (misalnya dari kelas *Perfect Entanglers*), efek negatif dari *noise* dapat diminimalkan, dan dalam kondisi tertentu (interferensi konstruktif), *payoff* rata-rata justru dapat meningkat seiring bertambahnya *noise*.


# 3. VQE Ansatz
## <u>COBYLA</u>
*   **Definisi**: *Constrained Optimization by Linear Approximation* (COBYLA) adalah algoritma optimasi numerik iteratif yang digunakan dalam VQE untuk memperbarui parameter sirkuit kuantum.
*   **Karakteristik**: Tidak memerlukan gradien (*derivative-free*), membuatnya tangguh terhadap noise pada perangkat NISQ.
*   **Performa**: Dalam konteks optimasi portofolio dengan CVaR, COBYLA seringkali menunjukkan performa yang lebih stabil dibandingkan SLSQP pada skenario yang kompleks, terutama saat menangani ruang pencarian yang dibatasi oleh *ansatz* berbasis Dicke state.

## <u>Parameterized Quantum Circuit</u>
Parameterized Quantum Circuit (PQC) atau *ansatz* adalah komponen inti VQE yang menentukan ruang keadaan yang dapat dieksplorasi.
*   **Problem-Inspired Ansatz**: Dokumen ini memperkenalkan *CCC ansatz* dan *CC ansatz* yang dirancang khusus untuk masalah optimasi kombinatorial (seperti seleksi aset).
*   **Efisiensi Perangkat Keras**: Menggunakan struktur "staircase" dengan kedalaman linear ($2n$ gerak dua-qubit) dan konektivitas tetangga terdekat (*nearest-neighbor*), sangat cocok untuk komputer kuantum era NISQ (seperti chip "Wu Kong").
*   **Dicke States**: *Ansatz* ini secara efisien menyiapkan *Dicke states* $|D^n_k\rangle$, yang merupakan superposisi dari semua basis state $n$-qubit dengan *Hamming weight* $k$. Hal ini secara otomatis memenuhi kendala anggaran (memilih $k$ aset dari $n$ pilihan) tanpa memerlukan *penalty terms* yang memperumit lanskap biaya.

## <u>Bayesian Game Algorithm</u>
*   **Konsep Dasar**: Bayesian Game Algorithm digunakan untuk memodelkan interaksi antara agen investasi dalam kondisi informasi tidak lengkap (*incomplete information*). Dalam konteks portofolio, ini melibatkan deteksi perilaku investasi melalui *two-person non-cooperative Bayesian game*.
*   **Mekanisme**:
    *   **Bayesian Nash Equilibrium (BNE)**: Menentukan strategi optimal di mana setiap pemain memaksimalkan ekspektasi *payoff* berdasarkan kepercayaan (*belief*) mereka terhadap tipe lawan (misal: investor normal vs spekulan/malicious).
    *   **Probabilistic Monitoring**: Mengurangi kompleksitas komputasi dengan mengadopsi strategi pemantauan berbasis probabilitas untuk mengidentifikasi pola portofolio dan interaksi pasar.
*   **Integrasi**: Algoritma ini memungkinkan pembaruan *belief* secara dinamis menggunakan aturan Bayesian saat data pasar baru tersedia, membantu dalam memprediksi fluktuasi harga aset dan mengoptimalkan bobot portofolio berdasarkan perilaku agen lain di pasar.


# 4. Sweet Spot
## <u>Game Theory X Quantum Computing</u>
Penggunaan teori permainan untuk mengoptimalkan alokasi sumber daya dalam lingkungan *Quantum Cloud Computing* (QCC).
*   **QC-PRAGM (Quantum Circuit Partitioning Resource Allocation Game Model)**: Sebuah model permainan di mana klien (pemain) berusaha meminimalkan biaya penggunaan sumber daya, sementara penyedia *cloud* berusaha memaksimalkan utilitas sumber daya.
*   **Nash Equilibrium**: Model ini terbukti memiliki *Nash Equilibrium* yang unik, di mana alokasi sumber daya optimal tercapai dan biaya total sistem tidak melebihi 4/3 dari biaya optimal teoretis.
*   **Optimasi Komunikasi**: Pengembangan *QC-PRAGM++* mengintegrasikan optimasi partisi sirkuit untuk meminimalkan gerbang non-lokal (*remote gates*), sehingga mengurangi latensi komunikasi antar node kuantum dalam jaringan terdistribusi.

## <u>Quantum Computing X Finance</u>
Penerapan komputasi evolusioner terinspirasi kuantum untuk menyelesaikan masalah optimasi portofolio yang kompleks di pasar keuangan global.
*   **Trend Ratio (TR)**: Indikator kinerja baru yang mengukur *return* harian per unit risiko harian, di mana risiko didefinisikan sebagai deviasi dari garis tren *uptrend*. Ini lebih efektif daripada *Sharpe Ratio* dalam mengidentifikasi portofolio dengan pertumbuhan stabil.
*   **EL-GNQTS (Entanglement-enhanced Local Search based on GNQTS)**: Algoritma optimasi yang menggabungkan *Quantum-inspired Tabu Search* (QTS) dengan mekanisme pencarian lokal berbasis *entanglement*.
    *   **Mekanisme**: Menggunakan konsep *superposition* dan *quantum-not gate* untuk eksplorasi ruang solusi, serta *entanglement* untuk memodelkan hubungan ketergantungan antar saham (misal: substitusi aset yang berkorelasi) guna mempercepat konvergensi ke solusi Pareto optimal.
    *   **Hasil**: Terbukti unggul dalam membentuk portofolio global (G7 markets) yang memiliki risiko rendah dan *return* stabil dibandingkan metode klasik.

# 5. Komentar & Analisis Kesesuaian dengan Rencana Penelitian

Bagian ini memetakan rangkuman literatur di atas dengan *Research Roadmap* skripsi Anda (VQE + EWL untuk 2 Aset).

## <u>1. Relevansi Model EWL (Bab 2)</u>
*   **Status**: **Sangat Sesuai**.
*   **Analisis**: Rangkuman pada Bab 2 (EWL & Modified EWL) sudah memberikan dasar teori yang kuat untuk argumen Anda memilih EWL dibandingkan Marinatto-Weber.
*   **Poin Kunci untuk Skripsi**: Anda dapat mengutip bagian "Syarat Klasik" dan "Fleksibilitas Operator" di *Modified EWL* untuk menjustifikasi mengapa Anda menggunakan operator entanglement eksplisit ($\hat{J}$) dalam sirkuit VQE Anda. Ini mendukung hipotesis bahwa korelasi kuantum dapat menemukan solusi yang tidak terlihat oleh model klasik.

## <u>2. VQE Ansatz: Dicke States vs. RyRz (Bab 3)</u>
*   **Status**: **Perlu Penyesuaian Konteks**.
*   **Analisis**: Rangkuman Bab 3 saat ini membahas *Dicke State Ansatz* yang dirancang untuk memilih $k$ aset dari $N$ aset (skala besar).
*   **Catatan Kritis**: Untuk penelitian Anda yang berfokus pada **2 Aset (2 Qubit)**, *Dicke State* mungkin terlalu kompleks atau tidak perlu.
    *   **Saran**: Sesuai rencana Anda, gunakan **Hardware Efficient Ansatz** atau **RyRz Ansatz**. Ansatz ini lebih sederhana dan parameter rotasinya ($\theta$) dapat langsung dipetakan sebagai "Strategi Pemain" dalam protokol EWL.
    *   **Optimizer**: Penggunaan **COBYLA** yang dirangkum di Bab 3 sudah tepat dan sesuai dengan rencana Anda karena efisiensinya dalam optimasi bebas gradien (derivative-free).

## <u>3. Missing Link: Mapping Payoff ke Hamiltonian</u>
*   **Status**: **Belum Tercover Secara Eksplisit di Rangkuman**.
*   **Tindakan**: Dalam implementasi VQE nanti, Anda harus mendefinisikan *Cost Function* secara spesifik.
    *   Literatur *Trend Ratio* (Bab 4) membahas fungsi tujuan finansial.
    *   Tugas Anda adalah menerjemahkan matriks *Payoff* (Keuntungan/Risiko) menjadi Operator **Hamiltonian** ($H$).
    *   Rumus kuncinya: $H = - \text{Payoff Matrix}$ (karena VQE mencari energi minimum, sedangkan kita mencari profit maksimum).

## <u>4. Posisi Penelitian ("Sweet Spot")</u>
Penelitian Anda berada tepat di irisan Bab 4:
*   Anda menggunakan **Game Theory** (EWL dari Bab 2).
*   Dijalankan di atas **Quantum Computing** (VQE dari Bab 3).
*   Untuk menyelesaikan masalah **Finance** (Portfolio 2 Aset dari Bab 1).
*   **Kebaruan (Novelty)**: Kebanyakan paper (seperti QC-PRAGM) menggunakan game theory untuk *resource allocation*. Penelitian Anda menggunakan game theory untuk *asset allocation* itu sendiri, yang merupakan pendekatan unik (Quantum Game Theory for Portfolio Optimization).


