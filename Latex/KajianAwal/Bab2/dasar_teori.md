# Dasar Teori: Deep Learning-Based BSDE Solver for Libor Market Model

Berikut adalah rangkuman dasar teori yang dibahas dalam paper **"Deep Learning-Based BSDE Solver for Libor Market Model with Application to Bermudan Swaption Pricing and Hedging"**:

1.  **Libor Market Model (LMM) / BGM Model**
    *   Model struktur berjangka tingkat bunga yang digunakan secara luas untuk memberi harga derivatif tingkat bunga.
    *   > "The Libor Market Model, also known as the BGM Model, is a term structure model of interest rates. It is widely used to price interest rate derivatives, especially Bermudan swaptions, and other exotic Libor callable derivatives."
    *   > "LMM postulates dynamical propagation of the forward Libor rates, which are the floating rates to index the interest rate swap funding legs."

2.  **Heath, Jarrow, and Morton (HJM) Model**
    *   LMM merupakan perluasan dari model HJM yang menggunakan input pasar secara langsung.
    *   > "As an extension of the Heath, Jarrow, and Morton (HJM) [4] model on continuous forward rates, the LMM takes market observables as direct inputs to the model."

3.  **Monte Carlo Simulation**
    *   Metode numerik standar yang digunakan dalam LMM untuk menghitung harga derivatif, meskipun memiliki tantangan dalam menghitung "Greeks" (sensitivitas).
    *   > "For numerical implementation purposes, Monte Carlo simulation is used for Libor Market Model to compute the prices of derivatives."
    *   > "The standard Monte Carlo method for American swaption pricing more or less uses regression to estimate the expected value by a linear combination of basis functions..."

4.  **Backward Stochastic Differential Equations (BSDEs)**
    *   Pendekatan matematis yang menghubungkan persamaan diferensial parsial (PDE) non-linear dengan persamaan diferensial stokastik mundur, memungkinkan penyelesaian masalah dimensi tinggi.
    *   > "Most recently, groups of computational mathematics researchers... proposed new algorithms to solve nonlinear parabolic partial differential equations (PDEs) based on formulation of equivalent backward stochastic differential equations (BSDEs) in high dimension"

5.  **Generalized Feynman-Kac Theorems**
    *   Teorema yang menjadi landasan teoritis penghubung antara PDE dan BSDE.
    *   > "Theoretically, this approach is founded on the amazing generalized Feynman-Kac theorems (see works by Pardoux and Peng [13][14])."

6.  **Deep Neural Networks (DNN)**
    *   Digunakan untuk mengaproksimasi fungsi gradien atau kebijakan dalam penyelesaian BSDE, mengatasi "Curse of Dimensionality".
    *   > "For European style options the feedforward deep neural networks (DNN) show not only feasibility but also efficiency in obtaining both prices and numerical Greeks."
    *   > "The third step borrows ideas and tools from the most recent amazing developments in machine learning, reinforcement learning, and deep neural networks (DNN) learning."

7.  **Stochastic Optimal Control**
    *   Teori yang memiliki koneksi mendalam dengan teori BSDE/FBSDE dan digunakan dalam formulasi masalah penetapan harga.
    *   > "The second step in the new approach utilizes the deep connection between the BSDE/FBSDE theories and the stochastic optimal control theories"

8.  **Bellman Dynamic Programming Principle**
    *   Prinsip yang digunakan untuk menangani keputusan latihan awal (early exercise) pada opsi tipe Bermudan.
    *   > "A general guideline is the famous Bellman dynamic programming principle to make this type of optimal decision."
    *   > "When option price is projected backwards, it is easy to make an early exercise decision of Bermudan swaption following the same Bellman dynamic programming principle."

# Dasar Teori: Feedback-driven quantum reservoir computing for time-series analysis

Berikut adalah rangkuman dasar teori yang dibahas dalam paper **"Feedback-driven quantum reservoir computing for time-series analysis"**:

1.  **Quantum Reservoir Computing (QRC)**
    *   Paradigma komputasi yang menjanjikan yang memanfaatkan sistem kuantum sebagai sumber daya untuk pemrosesan informasi non-linear.
    *   > "Quantum reservoir computing (QRC) is a highly promising computational paradigm that leverages quantum systems as a computational resource for nonlinear information processing."

2.  **Fading-memory Property**
    *   Sifat penting dalam reservoir computing di mana dependensi temporal dipetakan, dan pengaruh input lama semakin berkurang dibandingkan input baru.
    *   > "Particularly focusing on temporal information processing, the fading-memory property emerges as a crucial aspect of the reservoir computing framework."
    *   > "This property dictates that when the reservoir projects input data onto the feature space, the temporal dependencies between different inputs are faithfully mapped within that internal space, and the influences of earlier inputs, being less significant than more recent ones, gradually diminish"

3.  **Feedback-driven QRC Framework**
    *   Metodologi yang diusulkan menggunakan pengukuran proyektif pada semua qubit dan mengumpan balik hasilnya ke reservoir untuk memulihkan memori input sebelumnya.
    *   > "To address this issue, we propose the feedback-driven QRC framework. This methodology employs projective measurements on all qubits for unrestricted access to the quantum state, with the measurement outcomes subsequently fed back into the reservoir to restore the memory of prior inputs."

4.  **Measurement Back-action**
    *   Gangguan pada keadaan kuantum akibat pengukuran, yang biasanya menghapus memori input temporal dalam pendekatan QRC konvensional.
    *   > "Conventional QRC architectures rely on quantum measurements to extract information from the quantum reservoir. However, these measurements inevitably induce measurement back-action, leading to the destruction of the quantum state of the reservoir."
    *   > "As a result, the memories of previous inputs encoded within the quantum reservoir are completely erased."

5.  **Edge of Chaos**
    *   Fase transisi antara dinamika stabil dan tidak stabil di mana kinerja memori dan kemampuan komputasi reservoir menjadi maksimal.
    *   > "Previous investigations have demonstrated that computational capabilities tend to be maximized when the reservoir part resides proximate to the boundary separating a stable and an unstable dynamical regimes, commonly referred to as the edge of chaos"
    *   > "Notably, analysis of measurement trajectories reveal three distinct phases depending on the feedback strength, with the memory performance maximized at the edge of chaos."

6.  **Echo State Network (ESN)**
    *   Kerangka kerja reservoir computing klasik yang mapan, digunakan sebagai pembanding untuk mengevaluasi kinerja QRC.
    *   > "ESN is a well-established framework in classical reservoir computing [16, 17, 19]."

# Dasar Teori: Important Quantum Gates for Quantum Algorithms of Travelling Salesman Problem

Berikut adalah rangkuman dasar teori yang dibahas dalam paper **"Important Quantum Gates for Quantum Algorithms of Travelling Salesman Problem"**:

1.  **Travelling Salesman Problem (TSP)**
    *   Masalah optimasi klasik untuk menemukan rute terpendek yang mengunjungi setiap kota tepat satu kali dan kembali ke asal. Masalah ini diklasifikasikan sebagai NP-hard.
    *   > "Essentially, the TSP seeks to identify a route that visits N number of cities exactly once and returning to city of origin with the least amount of resources used"
    *   > "For this reason, TSP is classified as an NP-hard problem"

2.  **Quantum Approximate Optimization Algorithm (QAOA)**
    *   Algoritma kuantum hibrida yang beroperasi berdasarkan prinsip adiabatik, dirancang untuk menyelesaikan masalah optimasi kombinatorial di era NISQ.
    *   > "QAOA is closely related with the adiabatic quantum computing (AQC), which operates based on the adiabatic principle"
    *   > "QAOA is chosen as a way to solve TSP because, its performance has been proven to achieve the approximation ratio of at least 0.6924 on 3-regular graphs"

3.  **State Initialization (W State vs Hadamard)**
    *   Inisialisasi state sangat penting. Metode standar (Hadamard) menciptakan superposisi seragam yang mencakup solusi tidak valid. Penggunaan state W diusulkan karena hanya memiliki satu bit '1' per N qubit, mengurangi ruang pencarian solusi tidak valid secara drastis.
    *   > "The standard technique to prepare initial state is by applying a series of Hadamard gates to all qubits that put all qubit states in an equal superposition."
    *   > "This improvement is attributed to the W state’s unique property of assigning precisely a single bit ’1’ for every N bits."
    *   > "By utilising the W state as the initial state, we can reduce the initial complexity of the proposed algorithm from 2^N to N."

4.  **B(1/k) Gates for W State**
    *   Gerbang kuantum baru yang diusulkan untuk menghasilkan state W secara efisien.
    *   > "This paper proposes B(1/k) gates as important gates to generate W state for the quantum approximate optimization algorithm (QAOA)"
    *   > "It is quite clear to construct a W state. We require (N − 1) operations of B(1/k) and 2 × (N − 1) total operations of controlled-G(1/k) and upside down CNOT."

5.  **Cost & Mixer Hamiltonians**
    *   Dua komponen utama lapisan QAOA. Cost Hamiltonian merepresentasikan fungsi objektif masalah, sementara Mixer Hamiltonian membantu eksplorasi ruang solusi yang layak.
    *   > "The general structure of QAOA consists of two Hamiltonian operators, i.e., the cost Hamiltonian and the mixer Hamiltonian."
    *   > "The mixer Hamiltonian maps the algorithm to achieve feasible solutions."

6.  **Ising Hamiltonian for TSP**
    *   Formulasi masalah TSP ke dalam model Ising menggunakan variabel spin Pauli-Z agar dapat diselesaikan dengan komputer kuantum.
    *   > "QAOA has been heavily studied to solve another optimization problem, e.g., the Max-cut problem for its simplicity and its connection to the Ising Model"
    *   > "To construct the complete Ising Hamiltonian for the complete cost function, we can substitute xi,j using spin variable σz_{i,j}."

# Dasar Teori: Linking quantum discord with Bayesian game theory

Berikut adalah rangkuman dasar teori yang dibahas dalam paper **"Linking quantum discord with Bayesian game theory"**:

1.  **Quantum Discord**
    *   Ukuran korelasi kuantum yang melampaui keterikatan (entanglement), mampu menangkap korelasi kuantum lokal bahkan dalam keadaan terpisah (separable). Discord lebih tahan terhadap gangguan eksternal dibandingkan bentuk korelasi kuantum lainnya.
    *   > "Quantum discord allows quantum correlations to be revealed which exist when the state may be unentangled."
    *   > "An added benefit of quantum discord is due to its relative robustness against external perturbations and noise compared to other forms of quantum correlation"

2.  **Quantum Discord Witness**
    *   Metode eksperimental untuk mendeteksi discord kuantum tanpa memerlukan tomografi keadaan penuh, menggunakan kombinasi non-linear fungsi korelasi.
    *   > "A recently proposed quantum discord witness offers an experimentally accessible set-up which allows the quantum discord to be witnessed through a non-linear combination of correlation functions."
    *   > "Therefore this motivates a clear need to design an experimentally friendly witness of quantum discord which allows for clear quantification of quantum effects"

3.  **Bayesian Game Theory**
    *   Kerangka kerja teori permainan di mana pemain memiliki ketidakpastian tentang jenis permainan yang mereka mainkan, memungkinkan pemodelan interaksi dengan informasi yang tidak lengkap.
    *   > "The advent of Bayesian game theory yields a general mechanism to model how parties interact and formulate decisions when there is uncertainty in what type of situation they are in."
    *   > "This results in the Bayesian nature of these games as each player has to assign a prior belief about what type of player the other player is"

4.  **CHSH Inequality & Game**
    *   Eksperimen terkenal untuk membedakan korelasi kuantum non-lokal dari korelasi klasik. Dalam konteks teori permainan, ini dapat dipetakan menjadi permainan kooperatif.
    *   > "The CHSH inequality is built from a linear combination of correlation functions in a bipartite system."
    *   > "Interestingly, the experimental set-up can be mapped to Bayesian game theory allowing for an extended generalisation of the proposed witness."

5.  **Link between Expected Payoff and Discord Witness**
    *   Paper ini menunjukkan hubungan langsung antara hasil yang diharapkan (expected payoff) dalam permainan Bayesian dan saksi discord kuantum melalui permainan CHSH.
    *   > "Subsequently, it is shown that there is a direct link between the expected payoff in Bayesian game theory and the previously proposed quantum discord witness by uniting these two concepts through the established CHSH game."
    *   > "By now combining and rearranging (12) and (14), it is clear there is a direct link between Bayesian game theory and witnessing quantum discord"

6.  **Quantum Advantage**
    *   Penggunaan sumber daya kuantum (seperti discord atau entanglement) dalam teori permainan untuk mencapai hasil yang lebih baik daripada strategi klasik terbaik.
    *   > "The main resource for quantum advantage is due to quantum entanglement and non-locality as these offer clear advantage over using classical physics."
    *   > "Given the practical link between Bayesian game theory and useful implementable algorithms, it is expected this link could be exploited but must be rigorously demonstrated."

# Dasar Teori: Qualitative financial modelling in fractal dimensions

Berikut adalah rangkuman dasar teori yang dibahas dalam paper **"Qualitative financial modelling in fractal dimensions"**:

1.  **Black-Scholes Equation (BSE)**
    *   Persamaan diferensial parsial fundamental untuk menilai derivatif finansial, namun memiliki batasan yang ketat dan tidak selalu sesuai dengan masalah ekonomi riil.
    *   > "The Black-Scholes equation is one of the most important partial differential equations governing the value of financial derivatives in financial markets."
    *   > "However, the Black-Scholes model requires severe constraints, assumptions, and conditions to be applied to real-life financial and economic problems."

2.  **Fractal Dimensions**
    *   Parameter yang menunjukkan kompleksitas kurva dan mengukur tingkat self-similarity dan iregularitas objek fraktal, digunakan untuk menganalisis data finansial.
    *   > "A fractal is an object characterized by self-similarity and irregularity."
    *   > "The fractal dimension offers an exceptional way of understanding and characterizing patterns that are frequently found in nature, and it is seriously considered in merely all fields of sciences and engineering."

3.  **Fractional Black-Scholes Models**
    *   Model yang memperluas Black-Scholes dengan menggabungkan turunan fraksional untuk mengatasi efek non-lokal dan memori panjang yang sering terlihat di pasar keuangan.
    *   > "These fractional models are expected since the Black-Scholes equation is derived using Ito's lemma from stochastic calculus, where fractional derivatives play a leading role."
    *   > "A new fractional parameter is introduced in this model, which is advantageous as it helps to describe the option market's behavior. Unlike many other stochastic volatility models, the fractional model provides a natural extension to the classical Black-Scholes model."

4.  **Hurst Exponent**
    *   Parameter fraktal yang sering digunakan dalam analisis keuangan untuk mempelajari efek memori panjang dalam seri waktu (time series) harga saham, berkorelasi dengan dimensi fraktal.
    *   > "fractal dimension is correlated with the Hurst exponent (a fractal parameter of an economic process), which is frequently used in financial analysis to study long-memory effects in a series of stock prices."
    *   > "The Hurst exponent is also considered a major parameter, and a method to extract realized Hurst exponents from log-prices was proposed by Garcin (2020)."

5.  **Fractal Market Hypothesis (FMH)**
    *   Hipotesis alternatif untuk Efficient Market Hypothesis, yang menyatakan bahwa pasar keuangan memiliki struktur fraktal dan menunjukkan pola self-similar.
    *   > "The efficient market hypothesis (EMH) is not a convincing model of financial markets; it has been replaced by the fractal market hypothesis (FMH) as a more general alternative tool to study financial markets"
    *   > "The Fractal Market Hypothesis ... offers a plausible explanation of various market inefficiencies and confirms the fact that “only balance of long-term and short-term players on the market can assure the market effectiveness.”"

6.  **Conformable Derivatives**
    *   Jenis turunan fraksional lokal yang diperkenalkan untuk menyederhanakan persamaan dinamis dan dapat menambahkan parameter tambahan tanpa mengubah sifat fisik sistem.
    *   > "In fact, conformable derivatives are local operators that modify the basic integer-order derivatives"
    *   > "This definition is motivating when compared to the fractional derivative, since it reduces the complexity of the dynamical equations of the system under study."

7.  **Power-laws in Financial Markets**
    *   Sifat umum dalam data keuangan seperti volatilitas, pengembalian, dan volume transaksi, menunjukkan perilaku yang tidak tergantung skala dan sering dikaitkan dengan struktur fraktal.
    *   > "In our analysis, we consider power-laws properties for volatility, interest rated, and dividend payout, which emerge in several empirical regularities in quantitative finance and economics."
    *   > "These power-law findings are ubiquitous and important, since information arising from estimate prices with tail-risk sensitivity are particularly critical for applied economists and finance researchers"

# Dasar Teori: Quantum-enhanced Markov chain Monte Carlo

Berikut adalah rangkuman dasar teori yang dibahas dalam paper **"Quantum-enhanced Markov chain Monte Carlo"**:

1.  **Markov Chain Monte Carlo (MCMC)**
    *   Teknik algoritmik populer untuk mengambil sampel dari distribusi probabilitas, terutama distribusi Boltzmann model Ising klasik.
    *   > "Markov chain Monte Carlo (MCMC) is the most popular algorithmic technique for sampling from the Boltzmann distribution μ of Ising models in all of the afore-mentioned applications."
    *   > "It approaches the problem indirectly, without ever computing μ(s) and in turn the partition function Z"

2.  **Classical Ising Models & Boltzmann Distribution**
    *   Model fisik yang terdiri dari variabel spin dengan energi yang terkait, sering digunakan untuk memodelkan sistem dengan lanskap energi yang kompleks (spin glasses), di mana distribusi Boltzmann menggambarkan probabilitas konfigurasinya.
    *   > "A classical Ising model consists of n variables ($1,..., Sn) = s called spins that can take values sj = ±1 independently"
    *   > "and a corresponding Boltzmann probability μ(s) = e-E(s)/T, where the partition function Z = Σe-E(s)/T ensures normalization."

3.  **Quantum-enhanced MCMC Algorithm**
    *   Algoritma hibrida yang menggunakan komputer kuantum untuk mengusulkan pergerakan (moves) dalam rantai Markov dan komputer klasik untuk menerima atau menolaknya, bertujuan untuk konvergensi yang lebih cepat.
    *   > "Here we introduce a quantum algorithm to sample from distributions that pose a bottleneck in several applications, which we implement on a superconducting quantum processor."
    *   > "The algorithm performs Markov chain Monte Carlo (MCMC), a popular iterative sampling technique, to sample from the Boltzmann distribution of classical Ising models."

4.  **Detailed Balance Condition**
    *   Kondisi yang harus dipenuhi oleh probabilitas transisi dalam rantai Markov untuk memastikan bahwa proses konvergen ke distribusi target yang diinginkan.
    *   > "Sufficient conditions for such convergence are that the Markov chain be irreducible and aperiodic (technical requirements that will always be met here [11]), and satisfy the detailed balance condition"
    *   > "P(s'|s) μ(s) = P(s|s') μ(s')"

5.  **Metropolis-Hastings (M-H) Acceptance**
    *   Probabilitas penerimaan yang umum digunakan dalam MCMC untuk memutuskan apakah usulan pergerakan (proposal) harus diterima atau ditolak, berdasarkan rasio probabilitas distribusi.
    *   > "One of the most popular is the Metropolis-Hastings (M-H) acceptance probability [13, 14]: A(s'|s) = min (1, Q(s|s') μ(s') / Q(s'|s) μ(s))"

6.  **Spin Glasses & Rugged Energy Landscapes**
    *   Model Ising klasik yang ditandai dengan lanskap energi yang "kasar" (rugged) dengan banyak minimum lokal, menjadi tantangan signifikan bagi algoritma MCMC klasik.
    *   > "Eq. (1) typically defines a rugged energy landscape for such instances, informally termed spin glasses"
    *   > "spin glasses at low T present a formidable challenge for all of these approaches, manifesting in long autocorrelation, slow convergence, and ultimately long MCMC running times."

7.  **Quantum Speedup & Convergence**
    *   Algoritma MCMC yang ditingkatkan secara kuantum menunjukkan konvergensi yang lebih cepat (dalam jumlah iterasi yang lebih sedikit) dibandingkan alternatif klasik, terutama pada masalah spin glass yang relevan.
    *   > "We find that this quantum algorithm converges in fewer iterations than common classical MCMC alternatives on relevant problem instances, both in simulations and experiments."
    *   > "It therefore opens a new path for quantum computers to solve useful not merely difficult-problems in the near term."

# Dasar Teori: Quantum Barro-Gordon Game in Monetary Economics

Berikut adalah rangkuman dasar teori yang dibahas dalam paper **"Quantum Barro-Gordon Game in Monetary Economics"**:

1.  **Classical Game Theory**
    *   Kerangka matematis untuk menganalisis situasi di mana hasil dari tindakan satu agen memengaruhi agen lain, dengan aplikasi luas di berbagai bidang ilmu.
    *   > "Classical game theory addresses decision problems in multi-agent environment where one rational agent's decision affects other agents' payoffs."
    *   > "Game theory has widespread application in economic, social and biological sciences."

2.  **Barro-Gordon Game**
    *   Model klasik dalam ekonomi moneter yang menggambarkan masalah ketidakonsistenan waktu dalam kebijakan moneter, sering mengarah pada bias inflasi.
    *   > "In this paper, we consider a quantum version of the classical Barro-Gordon game which captures the problem of time inconsistency in monetary economics."
    *   > "The classical Barro-Gordon game captures the essence of this type of time-inconsistency in the context of decisions (strategy) that a policy maker must make and the expectations that the public can have."

3.  **Time Inconsistency**
    *   Fenomena di mana kebijakan yang optimal di suatu waktu menjadi tidak optimal ketika waktu tersebut tiba, seringkali karena godaan pembuat kebijakan untuk mengeksploitasi ekspektasi publik.
    *   > "Such time inconsistency refers to the temptation of weak policy maker to implement high inflation when the public expects low inflation."
    *   > "The inconsistency arises when the public punishes the weak policy maker in the next cycle."

4.  **Quantum Game Theory**
    *   Versi kuantum dari teori permainan klasik yang menggabungkan prinsip-prinsip mekanika kuantum (seperti superposisi dan keterikatan) untuk menganalisis interaksi strategis, berpotensi menghilangkan dilema klasik.
    *   > "In recent years quantum versions of classical games have been proposed and studied."
    *   > "It is the purely quantum mechanical concept of superposition (of strategies) which provides the key ingredient in our approach to game theory here."

5.  **Marinatto-Weber (MW) Approach**
    *   Skema umum untuk kuantisasi permainan yang didasarkan pada pendekatan ruang Hilbert, digunakan dalam penelitian ini untuk mengkuantisasi permainan Barro-Gordon.
    *   > "Marinatto and Weber (MW) [12] offered a more general scheme for quantization of games based on Hilbert space approach."
    *   > "We therefore use the MW method to quantize the game between weak policy maker and the public."

6.  **Nash Equilibrium**
    *   Keadaan stabil dalam permainan di mana tidak ada pemain yang dapat memperoleh keuntungan dengan mengubah strategi mereka secara sepihak, asalkan strategi pemain lain tetap. Kuantisasi game Barro-Gordon dapat menghasilkan Nash equilibrium yang time-consistent.
    *   > "In this paper, by following Backus and Driffill [38] and Storger [39], we use a special version of BG game. This version is easier to convert to quantum game due to having a definitive payoff matrix."
    *   > "We first present a quantum version of the Barro-Gordon game. Next, we show that in a particular case of the quantum game, time-consistent Nash equilibrium could be achieved when public expects low inflation, thus resolving the game."

7.  **Inflationary Bias**
    *   Kecenderungan pembuat kebijakan untuk menghasilkan inflasi yang lebih tinggi dari yang diharapkan publik, seringkali karena kurangnya komitmen terhadap kebijakan yang telah diumumkan. Kuantisasi game dapat membantu mengatasi masalah ini.
    *   > "Therefore, we encounter an inflationary bias."
    *   > "The main idea is, when people expect low inflation, central bank finds the incentive for high inflation."

# Dasar Teori: Quantum inspired qubit qutrit neural networks for real time financial forecasting

Berikut adalah rangkuman dasar teori yang dibahas dalam paper **"Quantum inspired qubit qutrit neural networks for real time financial forecasting"**:

1.  **Quantum-inspired Neural Networks (QNNs)**
    *   Model machine learning yang memanfaatkan prinsip-prinsip mekanika kuantum seperti superposisi, keterikatan, dan interferensi untuk pemrosesan data.
    *   > "Quantum intelligence, situated at the intersection of quantum computing and AI, harnesses phenomena like superposition, entanglement, and interference to optimize and solve intricate prediction tasks"
    *   > "the proposed models underscore the transformative potential of quantum-inspired approaches, paving the way for their integration into computationally intensive fields."

2.  **Qubit-based Neural Networks (QQBNs)**
    *   Jaringan saraf kuantum yang menggunakan qubit (sistem kuantum dua tingkat) untuk merepresentasikan dan memproses informasi.
    *   > "This research investigates the performance and efficacy of machine learning models in stock prediction, comparing Artificial Neural Networks (ANNs), Quantum Qubit-based Neural Networks (QQBNs), and Quantum Qutrit-based Neural Networks (QQTNs)."
    *   > "Data representation in a quantum neural network (QNN) using qubits is a crucial step because unlike classical neural networks that operate on bits (0 or 1), QNNs leverage the principles of quantum mechanics."

3.  **Qutrit-based Neural Networks (QQTNs)**
    *   Jaringan saraf kuantum yang menggunakan qutrit (sistem kuantum tiga tingkat), menawarkan representasi data yang lebih kaya dan efisiensi komputasi yang lebih tinggi dibandingkan qubit atau model klasik.
    *   > "By achieving superior accuracy, efficiency, and adaptability, the proposed models underscore the transformative potential of quantum-inspired approaches"
    *   > "Qutrit-based neural network (QQTN) workflow leveraged a bespoke qutrit simulator built on top of QuTiP 4.7.3"

4.  **Data Encoding (Amplitude & Phase Encoding)**
    *   Teknik untuk mengonversi data klasik menjadi status kuantum. Amplitude encoding memetakan nilai data ke amplitudo keadaan, sedangkan phase encoding memetakan ke faktor fase.
    *   > "Amplitude encoding This technique assigns specific amplitudes to the |0) and (1) states based on the data value."
    *   > "Phase encoding Here, classical data values are encoded into the phase factors of a superposition state."

5.  **Parameterized Quantum Circuits (PQCs)**
    *   Sirkuit kuantum dengan gerbang kuantum yang dapat dilatih (trainable) (misalnya, gerbang rotasi) yang parameternya dioptimalkan secara iteratif.
    *   > "Parameterization introduces trainable elements within the QNN circuit, allowing iterative optimization of quantum gates."
    *   > "Examples include rotation gates (Rx, Ry, Rz), which adjust based on training feedback to enhance task performance."

6.  **Fidelity-based Loss Function**
    *   Fungsi biaya khusus yang digunakan dalam optimasi QNN, mengukur keselarasan antara keadaan keluaran jaringan dan keadaan target yang diinginkan.
    *   > "Both the QQBN and QQTN models were trained using a fidelity-based loss function defined as L(θ) = 1 - |〈target|ψoutput(θ)〉|^2"
    *   > "This loss encourages the model to generate quantum states that closely match the target output."

7.  **Financial Forecasting Application**
    *   Penerapan QNN, khususnya QQTN, untuk prediksi pasar saham, menunjukkan keunggulan dalam akurasi, efisiensi, dan kemampuan beradaptasi.
    *   > "This research employs stock market prediction as an empirical testbed to examine the effectiveness and scalability of Qubit- and Qutrit-based quantum models."
    *   > "QQTN not only surpasses its classical and qubit-based counterparts in multiple quantitative and qualitative metrics but also achieves comparable performance with significantly reduced training times."

# Dasar Teori: Quantum-like influence diagrams for decision-making

Berikut adalah rangkuman dasar teori yang dibahas dalam paper **"Quantum-like influence diagrams for decision-making"**:

1.  **Quantum-like Bayesian Networks (QLBNs)**
    *   Perluasan dari Bayesian Network klasik yang menggunakan amplitudo probabilitas kompleks (seperti dalam mekanika kuantum) alih-alih probabilitas riil. Ini memungkinkan pemodelan efek interferensi kuantum.
    *   > "Moreira and Wichert (2014, 2016a) proposed a quantum-like Bayesian network which extends Bayesian networks by replacing probabilities by complex quantum probability amplitudes."
    *   > "The off-diagonal elements of this operator correspond to quantum interference effects that will enable deviations from normative probabilistic inferences which are obtained in traditional BNs."

2.  **Quantum Interference Effects**
    *   Efek non-linear yang muncul dalam QLBN karena superposisi keadaan, yang dapat memperkuat (konstruktif) atau memperlemah (destruktif) probabilitas klasik. Ini digunakan untuk memodelkan penyimpangan dari rasionalitas klasik.
    *   > "These quantum interference effects are the core of the QLBN and are the result of the interferences caused by the quantum wave function."
    *   > "Note that quantum interference effects are non-linear functions that can be mapped to the non-linear activation functions in neural networks"

3.  **Influence Diagrams**
    *   Model grafis probabilistik untuk pengambilan keputusan yang terdiri dari node variabel acak, node keputusan, dan node utilitas. Tujuannya adalah memilih keputusan yang memaksimalkan utilitas yang diharapkan (Maximum Expected Utility/MEU).
    *   > "Generally speaking, an “influence diagram”, I, is a compact graphical representation of a decision scenario."
    *   > "The goal of an influence graph is to make a decision D maximise the Expected Utility function U by taking into account probabilistic inferences performed in the Bayesian Network"

4.  **Quantum-like Influence Diagrams (QLIDs)**
    *   Pengembangan baru yang diusulkan dalam paper ini, menggabungkan QLBN dengan Influence Diagrams. Tujuannya adalah memodelkan keputusan manusia yang paradoks atau irasional dengan mempengaruhi probabilitas yang digunakan dalam perhitungan MEU melalui interferensi kuantum.
    *   > "We suggest extending the quantum-like Bayesian network formalism to incorporate the notion of maximum expected utility to model human paradoxical, sub-optimal and irrational decisions."
    *   > "Instead of proposing an alternative representation of the expected utility theory... we take advantage of the quantum interference terms produced in the quantum-like Bayesian Network to influence the probabilities used to compute the expected utility of some decision."

5.  **Bounded Rationality & Irrationality**
    *   Konsep bahwa pengambilan keputusan manusia dibatasi oleh sumber daya kognitif dan informasi, serta dapat menyimpang dari rasionalitas normatif (seperti dalam teori utilitas yang diharapkan). QLID mencoba menangkap spektrum ini.
    *   > "Bounded Rationality: Corresponds to the scenario where the decision-maker is bounded in terms of cognitive resources with limited information, time, and processing power."
    *   > "Irrationality: Corresponds to the bounded rational minds that are facing extremely high levels of uncertainty... leads to decisions with very poor performances in terms of an utility function."

6.  **Law of Balance**
    *   Metode untuk menentukan nilai parameter interferensi kuantum dalam QLBN agar fluktuasi probabilitas tetap seimbang dan tidak terlalu sensitif, menyerupai kekacauan deterministik.
    *   > "In Wichert and Moreira (2018), the authors proposed a balanced quantum-like Bayesian network in which the normalisation process occurs by taking dominant quantum interference waves and balancing them in such a way that, when Bayes normalisation is being applied upon probabilistic inferences, they cancel each other out."

7.  **Sure Thing Principle**
    *   Prinsip ekonomi klasik yang sering dilanggar dalam eksperimen pengambilan keputusan manusia (seperti Prisoner's Dilemma). Pelanggaran ini dapat dimodelkan menggunakan QLID.
    *   > "The Sure Thing Principle (Savage, 1954) is a fundamental principle in economics and probability theory... Several experiments have shown that people violate this principle in decisions under uncertainty"
    *   > "Table 4 shows that the quantum-like Bayesian network was able to accommodate the paradoxical outcomes found in different experiments of the literature with respect to the Prisoner’s dilemma game"

# Dasar Teori: Statistical Arbitrage for Multiple Co-integrated Stocks

Berikut adalah rangkuman dasar teori yang dibahas dalam paper **"Statistical Arbitrage for Multiple Co-integrated Stocks"**:

1.  **Statistical Arbitrage & Pairs Trading**
    *   Strategi perdagangan yang memanfaatkan hubungan kointegrasi antar aset. Ide dasarnya adalah bahwa selisih harga (spread) antara aset yang terkointegrasi bersifat *mean-reverting*. Trader dapat mengambil posisi *long* pada aset yang murah dan *short* pada aset yang mahal, mengharapkan konvergensi.
    *   > "Statistical arbitrage strategies involve trading among pairs of assets having co-integration. The essential idea is that a pair of co-integrated asset prices have a difference that is mean reverting."
    *   > "For a trader with the ability to sell short and utilise leverage, a possible strategy is to long the cheaper asset, short the expensive asset, and then wait for the spread to converge"

2.  **Co-integration Model with Factors**
    *   Model yang digunakan mempertimbangkan saham yang *return*-nya terkointegrasi dengan *return* dari sekumpulan faktor. *Spread* didefinisikan sebagai residual dari regresi *return* saham terhadap *return* faktor.
    *   > "The model considers stocks whose total returns have co-integration with the total returns of a set of factors."
    *   > "The spreads are defined as the residuals that are obtained after regressing the total returns of a stock onto the total returns of factors."

3.  **Eigenportfolios as Factors**
    *   Faktor-faktor yang digunakan adalah *eigenportfolio*, yaitu portofolio ortogonal yang dikonstruksi dari matriks korelasi *return* saham (menggunakan PCA). Ini efektif karena faktor-faktornya ortogonal.
    *   > "The factors that we utilise are eigenportfolios, which are the orthogonal portfolios constructed from the correlation matrix of stock returns."
    *   > "Eigenportfolios are an effective factor construction because they are orthogonal"

4.  **Ornstein-Uhlenbeck (OU) Process**
    *   Proses stokastik yang digunakan untuk memodelkan dinamika *spread* yang *mean-reverting*. Jika sebuah saham terkointegrasi dengan faktor, *spread*-nya diasumsikan mengikuti proses OU stasioner.
    *   > "If we know that a stock is co-integrated with these factors, then we can further specify Z_t^i to be a stationary Ornstein-Uhlenbeck process"
    *   > "These spreads form a stationary vector Ornstein-Uhlenbeck (O) process."

5.  **Stochastic Control & HJB Equation**
    *   Masalah pencarian portofolio optimal diformulasikan sebagai masalah kontrol stokastik untuk memaksimalkan utilitas (fungsi utilitas *power*). Solusinya diperoleh dengan memecahkan persamaan Hamilton-Jacobi-Bellman (HJB).
    *   > "The optimal portfolio is obtained from the solution to an HJB equation, which in the case of power utility function we are able to reduce to a system of ordinary differential equations (ODEs)"
    *   > "Optimal portfolio weights are found by solving a Hamilton–Jacobi–Bellman (HJB) partial differential equation"

6.  **Market Neutrality**
    *   Kendala penting dalam *statistical arbitrage* dengan model faktor untuk mengimunisasi portofolio dari fluktuasi pasar. Karena faktor (eigenportfolio) dianggap tidak dapat diperdagangkan (karena biaya transaksi tinggi), optimasi perlu dibatasi agar portofolio netral terhadap pasar.
    *   > "Market neutrality is important when doing statistical arbitrage with a factor model, as it immunises the portfolio against market fluctuations."
    *   > "However in our case, because the factors are not tradeable, the optimisation should be constrained in order to have a market-neutral portfolio."

7.  **Matrix Riccati Equation**
    *   Persamaan diferensial matriks non-linear yang muncul dalam solusi persamaan HJB. Analisis stabilitas jangka panjang dari persamaan ini penting untuk memastikan model bebas arbitrase dan solusi HJB konvergen ke *steady state*.
    *   > "reduce to a system of ordinary differential equations (ODEs) that includes a matrix Riccati equation and a pair of linear equations."
    *   > "We perform long-term stability analyses for these ODEs... finiteness of the ODEs... indicates that the model has an absence of arbitrage"