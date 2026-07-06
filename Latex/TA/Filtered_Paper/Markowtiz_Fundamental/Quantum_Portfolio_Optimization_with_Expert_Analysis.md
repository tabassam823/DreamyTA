Quantum Portfolio Optimization with Expert Analysis
Evaluation
Nouhaila Innan1,2 , Ayesha Saleem1,2 , Alberto Marchisio1,2 , and Muhammad Shafique1,2
1

arXiv:2507.20532v1 [quant-ph] 28 Jul 2025

2

eBRAIN Lab, Division of Engineering, New York University Abu Dhabi (NYUAD), Abu Dhabi, UAE
Center for Quantum and Topological Systems (CQTS), NYUAD Research Institute, NYUAD, Abu Dhabi, UAE
nouhaila.innan@nyu.edu, as17815@nyu.edu, alberto.marchisio@nyu.edu, muhammad.shafique@nyu.edu

Abstract—Quantum algorithms have gained increasing attention for
addressing complex combinatorial problems in finance, notably portfolio
optimization. This study systematically benchmarks two prominent
variational quantum approaches, Variational Quantum Eigensolver (VQE)
and Quantum Approximate Optimization Algorithm (QAOA), under
diverse experimental settings, including different asset universes, ansatz
architectures, and circuit depths. Although both methods demonstrate
effective cost function minimization, the resulting portfolios often violate
essential financial criteria, such as adequate diversification and realistic
risk exposure. To bridge the gap between computational optimization
and practical viability, we introduce an Expert Analysis Evaluation
framework in which financial professionals assess the economic soundness
and the market feasibility of quantum-optimized portfolios. Our results
highlight a critical disparity between algorithmic performance and
financial applicability, emphasizing the necessity of incorporating expert
judgment into quantum-assisted decision-making pipelines.
Index Terms—Quantum Computing, Portfolio Optimization, Quantum
Finance

I. I NTRODUCTION
In today’s rapidly evolving financial landscape, the optimization
of investment portfolios plays a crucial role in informed decisionmaking for both institutional and individual investors. Balancing risk
and return under various constraints, such as budget, diversification,
and investor preferences, requires sophisticated techniques that can
navigate high-dimensional, nonlinear, and discrete solution spaces.
Traditional methods in quantitative finance have made significant
progress in addressing this challenge [1]. However, the rise of Quantum
Computing (QC) presents a new computational paradigm that offers
promising solutions to complex financial problems [2]–[9], particularly
in portfolio optimization [10], [11].
According to Markowitz’s seminal work on portfolio theory [12],
portfolio construction involves selecting an asset allocation that
balances expected return against risk, subject to constraints such as risk
tolerance and budget. Combinatorial portfolio selection, a core part
of this stage, is an NP-hard binary optimization problem [13] where
one must choose k assets from a pool of n, leading to an exponential
growth in the number of potential combinations. This complexity
is further compounded by practical constraints, including sector
diversification, investor preferences, and legal or ethical exclusions.
While classical solvers can tackle such problems effectively on small
scales, they become computationally intensive as the portfolio size
increases. QC emerges as a compelling alternative, offering potentially
superior scalability and performance [14], [15]. In particular, the Quantum Approximate Optimization Algorithm (QAOA) and Sampling
Variational Quantum Eigensolver (SamplingVQE) have been explored
as quantum solutions to Quadratic Unconstrained Binary Optimization
(QUBO)-encoded portfolio selection problems [16].
However, algorithmic solutions, especially those grounded in
quantum optimization, face important limitations. Despite achieving
high-quality convergence and favorable performance metrics, such
algorithms do not inherently incorporate critical real-world considera-

tions such as economic volatility, geopolitical risks, or investor-specific
preferences [17]. These factors can drastically alter the viability of a
given portfolio, regardless of its algorithmically measured performance.
Quantum models typically rely on historical pricing data, which,
although informative, cannot fully capture the complexities of evolving
market dynamics or align with the subjective expectations of investors.
To address this gap, we propose an Expert Analysis Framework as
a complementary post-processing stage. This framework incorporates
human financial expertise to review the top-ranked quantum-optimized
portfolios. The goal is to ensure that selected portfolios are both
statistically sound and economically interpretable, as well as practically
feasible and aligned with real-world conditions. By integrating human
judgment into the quantum pipeline, we enhance the quality and
trustworthiness of the final portfolio decisions beyond what traditional
loss functions can deliver alone. Our novel contribution lies in
the integration of quantum optimization algorithms with expertdriven validation, bridging computational efficiency and financial
interpretability through:
• A comparative analysis of different quantum circuit architectures,
depths, and qubit counts across two quantum optimization
algorithms (QAOA and VQE).
• Evaluation using real-world financial datasets, relying on actual 2025 historical market data while studying diverse asset
selections.
• Development of an expert-guided evaluation framework to assess
the practical validity and interpretability of the resulting quantumgenerated portfolios.
II. BACKGROUND AND R ELATED W ORK
Portfolio optimization has become a representative use case for
evaluating quantum algorithms on real-world combinatorial problems.
In particular, its formulation as a Quadratic Unconstrained Binary
Optimization (QUBO) problem makes it compatible with quantum
annealing and gate-based approaches. Prior studies have explored the
performance of quantum algorithms on this problem class, analyzing
scalability, solution quality, and robustness using both synthetic and
historical financial datasets. Comparative investigations have also examined the effectiveness of heuristic, hybrid, and variational methods
in handling domain-specific constraints [16], [18]–[20]. Building on
these efforts, our work examines how quantum algorithms behave in
realistic financial settings. We focus on practical limitations that persist
despite algorithmic improvements and introduce a complementary
framework that integrates expert evaluation into the quantum decisionmaking process.
SamplingVQE [21], [22]. In the Noisy Intermediate-Scale Quantum
(NISQ) era, QC has introduced new algorithmic frameworks for
addressing discrete optimization problems. Among the most actively
studied are Variational Quantum Algorithms (VQAs), which use
hybrid quantum-classical routines to optimize parameterized quan-

tum circuits. Two notable VQAs applicable to binary optimization
problems, especially portfolio selection, are the QAOA [23] and the
SamplingVQE [21], [22].
QAOA is specifically designed to solve combinatorial optimization
problems by encoding a classical cost function into a parameterized
quantum circuit. It alternates between two Hamiltonians: the cost
Hamiltonian HC , which encodes the problem objective (e.g., a QUBO
formulation), and the mixer Hamiltonian HM , which introduces state
transitions. The circuit applies alternating layers of these Hamiltonians,
parameterized by angles γ and β, starting from an initial state. These
parameters are optimized using classical routines to minimize the
expectation value of HC . QAOA has been shown to approximate
classical solutions with bounded-depth circuits and is considered
well-suited for problems with binary constraints.
SamplingVQE, originally developed for estimating molecular
ground-state energies in quantum chemistry, has been adapted to
optimization tasks by expressing the objective function as a Hamiltonian and minimizing its expectation value over a parameterized
quantum state. The algorithm constructs a variational circuit U (θ) with
trainable parameters, acting on an initial state, and evaluates the cost
via repeated quantum measurements. Unlike QAOA, SamplingVQE
offers greater flexibility in circuit design through custom ansatz and
can be more easily integrated with classical preprocessing techniques.
Both QAOA and SamplingVQE have been applied to portfolio
optimization due to their compatibility with binary decision variables
and constraint encoding. Prior studies have demonstrated their
feasibility on simulators and early-stage quantum hardware [16],
yielding near-optimal solutions under realistic constraints in small
problem instances.
III. M ETHODOLOGY
The methodological pipeline begins with the mathematical formulation of the portfolio selection problem as a QUBO instance,
proceeds through quantum optimization using variational algorithms,
and concludes with an expert evaluation stage to ensure the financial
soundness of the resulting portfolios. The entire process is represented
in Fig. 1.
Mean -Variance Portfolio
Optimization Problem

Comparative Analysis

Objective (Loss)
Function
Convergence
QUBO
Formulation

Run Quantum
Algorithm

Cross Ansatz Performance
Comparison on
Expressibility,
Convergence, and Stability
Exploring the Impact of
Ansatz Complexity on
Optimization Convergence

Optimal Solution
QUBO Mapping
to Hamiltonian

Feasibility and Practicality
of Portfolio Allocations
Expert Analysis

Fig. 1: Overview of the proposed methodology combining QUBO-based
quantum optimization with expert-guided evaluation.

A. QUBO-based Portfolio Optimization
The portfolio optimization problem can be formulated as a binary
quadratic model. The objective is to select B assets out of n available
options to minimize risk and maximize expected return. This leads to
the following constrained problem: minx∈{0,1}n q x⊤ Σx − µ⊤ x
subject to 1⊤ x = B, where x ∈ {0, 1}n denotes the binary selection
vector (i.e., xi = 1 indicates selection of asset i), µ ∈ Rn is the
vector of expected returns, Σ ∈ Rn×n is the covariance matrix of

asset returns, q > 0 is the risk-aversion parameter, and B is the total
number of assets to be selected.
Assuming all assets have equal unit price and the full budget must be
used, the constraint 1⊤ x = B can be incorporated into the objective
2
via a penalty term: minx∈{0,1}n q x⊤ Σx − µ⊤ x + α 1⊤ x − B ,
where α > 0 controls
of
2
Pn the strength
Pnthe penalty.
P Expanding
xi − B =
xi + 2 i<j xi xj −
the penalty term:
i=1
i=1
P
2
2B n
i=1 xi + B .
Using the identity x2i = xi for binary variables, the full objective
becomes a QUBO problem of the form: minx∈{0,1}n x⊤ Qx + c,
where Q is the QUBO matrix with entries:
(
q Σij + α,
if i ̸= j,
Qij =
q Σii − µi + α(1 − 2B), if i = j,
and c = αB 2 is a constant offset that can be ignored during
optimization.
B. Quantum Algorithm Implementation
To solve the formulated QUBO problem, we employ QAOA and
SamplingVQE. In both approaches, the QUBO objective function
x⊤ Qx is mapped to a cost Hamiltonian HC acting on n qubits. This
i
is done using the standard transformation xi = 1−Z
, where Zi is
2
the Pauli-Z operator on qubit i.
Applying
the cost Hamiltonian takes the form:
P this substitution,
P
HC =
h
Z
+
J
Z
i
i
ij
i Zj + const, where the coefficients
i
i<j
hi and Jij are derived from the QUBO matrix Q by applying the
mapping to each quadratic term Qij xi xj .
QAOA prepares a parameterized quantum state by alternating
between evolution under
Pthe cost Hamiltonian HC and a mixing
Hamiltonian HM =
i Xi , where Xi is the Pauli-X operator. A p-layer QAOA circuit generates the state:
Q
P |ψ(γ, β)⟩ =
p
−iβl HM −iγl HC
√1
e
e
|ψ
⟩,
where
|ψ
⟩
=
0
0
l=1
z∈{0,1}n |z⟩ is
2n
the uniform superposition over all bitstrings. The variational parameters γ, β ∈ Rp are optimized to minimize the expectation value:
C(γ, β) = ⟨ψ(γ, β)|HC |ψ(γ, β)⟩.
SamplingVQE uses a general parameterized circuit U (θ) to prepare
a trial state: |ψ(θ)⟩ = U (θ)|0⟩⊗n , and estimates P
the objective function by sampling measurement outcomes: C(θ) = z∈{0,1}n Pθ (z) ·
Cost(z), where Pθ (z) is the probability of observing bitstring z, with
z ∈ {0, 1}n representing a candidate solution x, and Cost(z) = z ⊤ Qz
is the QUBO cost evaluated classically. The circuit parameters θ are
updated using a classical optimizer to minimize C(θ).
For SamplingVQE, we evaluate several ansatz circuits provided in
Qiskit: TwoLocal (with Rx, Ry, and Cz gates), EfficientSU2,
PauliTwoDesign, and RealAmplitudes. These differ in circuit
depth, entanglement structure, and gate composition, which affects
their expressibility and optimization performance [22].
C. Optimization Evaluation and Convergence Analysis
To evaluate optimization performance, each ansatz is tested across
multiple random seeds and circuit depths. This variation captures
the effects of stochasticity in parameter initialization. Convergence
behavior is assessed using the cost difference between successive
iterations: ∆Ct = C(θ t ) − C(θ t−1 ), which serves as an indicator of
optimization stability and convergence rate. The evolution of the cost
function C(θ t ) over iterations is used to characterize the optimization
landscape for each ansatz.
D. Expert Analysis Framework
Although quantum algorithms produce portfolios optimized under
historical data, they do not account for evolving real-world conditions
such as geopolitical instability or market-specific risks. To assess the

practical viability of the solutions, we incorporate an expert evaluation
phase. In our methodology, domain experts assess the top-ranked
quantum-generated portfolios for feasibility in terms of liquidity,
sector diversification, and investor suitability. This ensures that the
final selection not only satisfies mathematical criteria but also aligns
with current market dynamics and investment policy constraints. In
this way, expert insight complements quantum outputs with contextual
financial reasoning.
First, we analyze algorithmic portfolio
stock
 return by calculating

Pi,end −Pi,start
price return of each asset i using Ri =
where
×
100,
Pi,start
Pi,end is the stock price of the asset at the end of the time period
and Pi,start is the stock price of the asset at the beginning of the time
period, and then we calculate the average stock return of thePportfolio
of n assets using the following: Average Return (%) = n1 n
i=1 Ri .
Finally, we evaluate the market feasibility of algorithm-generated
portfolios by testing them on stock returns from a “future” time
period that follows the original set of months used by the system.

Among the 4-asset configuration, Microsoft achieves the highest
return (7.23%), while Apple experienced the steepest decline (15.97%). Tesla also posted a loss and is typically associated with
high volatility. Google showed a small gain (0.15%) with relatively
low risk. These characteristics suggest that Microsoft and Google are
better suited for inclusion in risk-neutral portfolios.
In the broader 10-asset configuration, Coca Cola outperforms all
other assets with a 14.11% gain, providing valuable exposure to the
consumer sector. Goldman Sachs and Morgan Stanley show stable
returns, making them attractive for financial diversification. Although
Amazon and NVIDIA had slight losses, their inclusion can help spread
risk across sectors.
Portfolio construction requires balancing two key factors: return
potential and diversification. A well-diversified portfolio reduces
correlation risk, preventing concentrated losses in a single sector.
Assets with stable or modest positive returns are especially appealing
for risk-neutral investors, as they imply lower volatility and more
consistent future performance.

IV. R ESULTS AND D ISCUSSION

TABLE I: 6-month return for each asset.

A. Experimental Setup
As presented in Fig. 2, our experiments are conducted on two
problem sizes involving 4 and 10 assets, corresponding to quantum
circuits with 4 and 10 qubits, respectively. Historical financial data
is collected from Yahoo Finance [24], covering the six-month period
from December 2024 to May 2025. The selected assets are as follows:
for the 4-asset portfolio, Apple (AAPL), Google (GOOG), Microsoft
(MSFT), and Tesla (TSLA); and for the 10-asset portfolio, the same
four assets plus Amazon (AMZN), NVIDIA (NVDA), Goldman Sachs
(GS), Morgan Stanley (MS), Nike (NKE), and Coca Cola (KO).
QAOA is implemented using its built-in alternating operator ansatz. SamplingVQE is evaluated using four ansatz architectures: TwoLocal (configured with Rx, Ry, and Cz gates),
EfficientSU2, PauliTwoDesign, and RealAmplitudes.
All circuits are configured with full entanglement to increase expressibility. To analyze the impact of circuit complexity, each configuration
qiskit-finance
qiskit_finance.data_providers

Stock Price Data
4 Assets

10 Assets

qiskit_aer.primitives
qiskit.circuit.library

TwoLocal

qiskit_algorithms.optimizers

EfficientSU2

qiskit_finance.applications.optimization

RealAmplitudes

qiskit_algorithms

PauliTwoDesign

qiskit_optimization.algorithms
qiskit_algorithms.utils

QAOA

qiskit.result

SamplingVQE

Depth
2

4

6

8

10

Shots = 1024
Optimizer = COBYLA
MinimumEigenOptimizer

Fig. 2: Experimental setup of our methodology.

is executed across five circuit depths: 2, 4, 6, 8, and 10 layers.
Every experiment is repeated using five different random seeds. The
number of measurement shots is fixed at 1024, and all simulations
are performed using the QASM simulator [25].
The QUBO penalty parameter α is set to n/2 for each instance,
where n is the number of assets (and thus qubits). The risk-aversion
parameter is fixed at q = 0.5, corresponding to a moderate investor
profile balancing risk and return.
B. Asset Allocation and Diversification Trends
Before analyzing the portfolios generated by quantum algorithms,
it is important to evaluate the underlying assets in terms of recent
performance and their role in diversification. Table I summarizes the
6-month returns for each asset from December 2024 to May 2025.

Ticker

Stock Price
(2 Dec 2024)

Stock Price
(30 May 2025)

6-Month Return
(%)

AAPL
GOOG
MSFT
TSLA
AMZN
NVDA
GS
MS
NKE
KO

239.013428
172.380157
429.329376
357.089996
210.710007
138.598068
595.771423
129.127823
78.172211
62.737671

200.850006
172.642487
460.359985
346.459991
205.009995
135.120621
600.450012
128.029999
60.189999
71.590988

-15.9670619
0.152181089
7.22769294
-2.976842006
-2.705145371
-2.509015494
0.785299331
-0.85018393
-23.00333043
14.11164434

C. Convergence Analysis by Ansatz and Depth
By varying the ansatz architecture and increasing circuit depth, we
assess convergence efficiency and stability under different problem
sizes.
1) 4-Asset Configuration
For the 4-asset configuration, as shown in Fig. 3, the loss exhibits
an overall downward trend across all ansatz architectures. However, a
closer analysis reveals notable fluctuations at different circuit depths.
Among all architectures, QAOA exhibits the most instability, with
pronounced variance across depths and inconsistent convergence
behavior. In contrast, RealAmplitudes, TwoLocal, EfficientSU2, and
PauliTwoDesign exhibit smoother and more stable convergence, with
only occasional minor fluctuations that do not significantly impact
the overall downward trend.
Notably, PauliTwoDesign shows clear improvement with increasing
circuit depth, converging from approximately −0.85 at depth = 2
to around −1.0 at depth = 10. RealAmplitudes emerges as the
most efficient, consistently reaching convergence in fewer than 100
evaluations across all depths. Additionally, with increasing depth,
all ansatz architectures require more evaluations to converge. This
suggests that early convergence in shallower circuits may reflect
premature minimization due to insufficient expressibility, rather than
true optimization.
2) 10-Asset Configuration
As shown in Fig. 4, QAOA continues to exhibit high variance
in the 10-asset setup, particularly at lower depths. However, its
performance gradually improves with increased depth, evolving
from values near −2.0 to more stable convergence below −2.0 at

Objective Function Value

Objective Function Value

1.5
1.0
0.5
0.0

(a)

1.5
1.0
0.5
0.0

(b)
(b)

-0.5

-0.5

-1.0

-1.0

0

50

100

150

250

200

350

300

400

0

100

200

0.5
0.0

(c)

-0.5
-1.0

Objective Function Value

1.0

1.0
0.5
0.0

(d)

-0.5

100

200

300

Number of Iterations

400

0

500

500

1.0
0.5
0.0

(e)

-0.5
-1.0

-1.0

0

400

1.5

1.5
Objective Function Value

Objective Function Value

1.5

300

Number of Iterations

Number of Iterations

100

200

300

Number of Iterations

400

0

500

100

200

300

Number of Iterations

400

500

Fig. 3: Loss convergence curves for a 4-asset configuration across different circuit depths. (a) Circuit Depth = 2, (b) Circuit Depth = 4, (c) Circuit Depth = 6,
(d) Circuit Depth = 8, (e) Circuit Depth = 10.
10

8
6
4
2

(a)

0
-2

8
6
4
2

(b)

0
-2

100

200

300

Number of Iterations
12
10

Objective Function Value

12
10
8
6
4
2

(c)

0
-2

400

500

0

100

200

100

200

300

Number of Iterations

400

500

400

500

10

8
6
4
2

(d)

0
-2

0

300

Number of Iterations

Objective Function Value

0

Objective Function Value

Objective Function Value

Objective Function Value

10

0

100

200

300

Number of Iterations

400

500

8
6
4
2

(e)

0
-2

0

100

200

300

Number of Iterations

400

500

Fig. 4: Loss convergence curves for a 10-asset configuration across different circuit depths. (a) Circuit Depth = 2, (b) Circuit Depth = 4, (c) Circuit Depth = 6,
(d) Circuit Depth = 8, (e) Circuit Depth = 10.

depth = 10. Other ansatz architectures perform more consistently.
PauliTwoDesign maintains convergence near −2.0 across all depths,
while RealAmplitudes, TwoLocal, and EfficientSU2 converge more
modestly, typically between −0.5 and −1.0.
Interestingly, the variance of convergence changes noticeably with
depth. For TwoLocal, PauliTwoDesign, and RealAmplitudes, the
spread of objective values narrows at greater depths, indicating more
stable convergence. In contrast, QAOA shows increasing variance,
suggesting sensitivity to circuit depth and parameter initialization.
D. Portfolio Output Analysis

1) 4-Asset Configuration
This configuration includes firms that, while covering different subsectors, are primarily technology-oriented, introducing considerable
correlation risk. As a result, optimal portfolios in this setting must
strike a balance between return potential and volatility. As shown
TABLE II: Assets selected for 4 assets configuration.
Ansatz/Model
Real Amplitudes
PauliTwoDesign
TwoLocal

While convergence results provide insight into an algorithm’s
optimization behavior, they do not guarantee the generation of
financially viable portfolios. To address this limitation, we analyze
the most frequently sampled bitstrings, each representing a candidate
portfolio, using probability histograms. These visualizations reveal
which portfolios each ansatz tends to favor and how likely they are
to be observed under repeated sampling.

EfficientSU2
QAOA

Portfolio (Depth = 2)
[GOOG, MSFT]
[GOOG, TSLA]
Fluctuating, Multiple bitstrings
at the same probability
[MSFT, TSLA]
[GOOG, MSFT]
Fluctuating, Multiple bitstrings
at the same probability

Portfolio (Depth = 10)
[AAPL, TSLA]
[GOOG, TSLA]
Fluctuating, Multiple bitstrings
at the same probability
Fluctuating, Multiple bitstrings
at the same probability
Fluctuating, Multiple bitstrings
at the same probability

in Fig. 5 and Table II, many anstaz architectures produce multiple
high-probability bitstrings, reflecting selection uncertainty driven by
strong asset correlations. At circuit depth 2, both Real Amplitudes

0.12

0.12

0.08
0.06
0.04

0.08
0.06
0.04

0.02

0.02

0.00

0.00

1

10

01

0
01

01

10

11
00

0

1
10

0

0
11

11

01

00

10

Bitstring (Portfolio Conﬁguration)

0.10

(b)

0.10

00

01

10

Probability

(a)

Probability

Probability

0.10

00

(c)

0.08
0.06
0.04
0.02
0.00

00

10

11

01

11

00

10

10

01

01

01

10

11

01

10

00

11

00

01

10

01

Bitstring (Portfolio Conﬁguration)

01

01

10

01

10

10

11
00

10

00
11

01
00

1

1
10

01

00

11

01

Bitstring (Portfolio Conﬁguration)

3.5

1.0
0.5

2.5
2.0
1.5
1.0
0.5

1.5
1.0
0.5

01
01
01
01
01
10
01
01
00
11
10
01
01
01
01
01
01
01
01
01
10
10
01
01
00
11
01
10
11
00
10
01
01
01
10
10
01
10
10
10
01
01
10
01
01
01
10

01
01
01
00
01
10
10
01
01
01
01
01
01
01
01
10
01
10
01
10

01
10
01

11

10
01

00
11
10

01

01
01
0
11

10
01

10
0

01
01

10
10
10

10

10
10

10
10

01
01
01
01
10

11
00
10
10
01
10
10
10
10
10
11
00
10
01
10
01
10
01
01
01
10
10
01
10
01
10
00
11
01
10
01
10
01
10

01
10

01

01

01

01
10

01
0

01

11

01
01
10

01
10
0

Bitstring (Portfolio Conﬁguration)

2.0

0.0

0.0

0.0

(c)

2.5

10

2.0
1.5

3.0

(b)

3.0

Probability (10^3)

(a)

2.5

Probability (10^3)

Probability (10^3)

Fig. 5: Probability histograms for a 4-asset configuration across different circuit depths. (a) Circuit Depth = 2, (b) Circuit Depth = 6, (c) Circuit Depth = 10.

Bitstring (Portfolio Conﬁguration)

Bitstring (Portfolio Conﬁguration)

Fig. 6: Probability histograms for a 10-asset configuration across different circuit depths. (a) Circuit Depth = 2, (b) Circuit Depth = 6, (c) Circuit Depth = 10.

and EfficientSU2 identify the [GOOG, MSFT] portfolio, arguably the
most balanced and financially sound pair based on historical returns.
However, this pattern does not persist at greater depths. Notably, at
depth 10, Real Amplitudes selects a risk-heavy portfolio including
Apple and Tesla, despite their underperformance in the observed
period.
These results suggest that increasing circuit complexity does not
necessarily yield better portfolio quality in small, highly correlated
asset sets. Instead, deeper circuits may introduce instability or reduce
interpretability.
2) 10-Asset Configuration
The 10-asset setup across a broader range of industries offers greater
opportunities for effective diversification. In this context, an ideal
portfolio balances sectoral exposure while maximizing risk-adjusted
returns. As illustrated in Fig. 6 and Table III, several depth-2 portfolios
TABLE III: Assets selected for 10 assets configuration.
Ansatz/Model

Portfolio (Depth = 2)

Portfolio (Depth = 10)

Real Amplitudes
PauliTwoDesign
TwoLocal
EfficientSU2

[GOOG, MSFT, NVDA, GS, NKE]
[GOOG, MSFT, AMZN, GS, NKE]
[GOOG, MSFT, NVDA, GS, NKE]
[GOOG, MSFT, NVDA, GS, NKE]
Fluctuating, Multiple bitstrings
at the same probability

[AAPL, MSFT, AMZN, MS, KO]
[AAPL, TSLA, NVDA, MS, KO]
[GOOG, AMZN, NVDA, GS, KO]
[GOOG, AMZN, NVDA, GS, KO]

QAOA

[AAPL, TSLA, NVDA, GS, KO]

include Nike, which posts the steepest decline among all assets. In
contrast, portfolios generated at depth 10 tend to align more closely
with sound financial principles. Coca Cola consistently appears across
different ansatz architectures and is often selected alongside Amazon,
NVIDIA, or Google to enhance diversification and reduce volatility.
Despite this trend, some architectures, such as Real Amplitudes,
PauliTwoDesign, and QAOA, continue to select Apple or Tesla at
depth 10, even though both assets experience significant losses. These
choices potentially weaken portfolio quality and underscore the risk of
relying solely on convergence metrics. The most balanced outputs are
obtained from TwoLocal and EfficientSU2 at depth 10. These circuits
consistently generate diversified portfolios that include Google, Coca
Cola, Goldman Sachs, and either Amazon or NVIDIA, combining
strong sectoral coverage with reasonable return expectations.
These findings emphasize that deeper circuits tend to produce more
viable portfolios in larger, more diverse asset sets. However, good
convergence alone does not ensure financial suitability. These results
highlight the need for interpretability and domain expertise when
applying quantum algorithms to portfolio optimization.

E. Expert Evaluation of Portfolio Quality
To assess the real-world viability of the quantum-generated portfolios, we compare their composition and short-term future returns using
our expert analysis. Table IV reports the individual asset returns during
June 2025, the month immediately following the original six-month
evaluation period, while Table V summarizes the average returns
for each generated portfolio during that period, calculated using our
framework.
TABLE IV: Stock returns for each asset in June 2025 (2 June to 20 June),
following the 6-month evaluation period.
Ticker

Price (2 Jun 2025)

Price (20 Jun 2025)

June Return (%)

AAPL
GOOG
MSFT
TSLA
AMZN
NVDA
GS
MS
NKE
KO

201.70
170.17
461.97
342.69
206.65
137.37
598.72
128.40
61.57
71.49

201.00
167.73
477.40
322.16
209.69
143.85
640.80
132.71
59.79
68.84

-0.35
-1.43
3.34
-5.99
1.47
4.72
7.03
3.36
-2.89
-3.71

TABLE V: Average returns for selected portfolios in June 2025, based on
configurations generated during the 6-month period.
4-Asset

10-Asset

Portfolio

Return (%)

Portfolio

Return (%)

GOOG, MSFT
AAPL, TSLA
GOOG, TSLA
MSFT, TSLA

0.95
-3.17
-3.71
-1.33

GOOG, MSFT, KO, GS, AMZN
GOOG, MSFT, KO, GS, NVDA
GOOG, AMZN, NVDA, GS, KO
AAPL, TSLA, NVDA, MS, KO
AAPL, MSFT, AMZN, GS, KO

1.34
1.99
1.62
-0.39
0.34

In the 4-asset configuration, the only portfolio to generate a positive
return in June is [GOOG, MSFT], identified by Real Amplitudes and
EfficientSU2 at depth 2. All other combinations, particularly those
involving Tesla or Apple, underperform, an outcome that aligns with
prior expert observations about volatility and return consistency.
In contrast, the 10-asset portfolios show stronger overall performance, with four out of five configurations producing positive
returns. Notably, the highest-returning portfolio, [GOOG, MSFT, KO,
GS, NVDA], at 1.99%, is not generated by any circuit. However,
EfficientSU2 generates a similar composition with a 1.62% return,
indicating promising alignment with expert expectations.
From an expert perspective, this analysis supports three key insights:
•

Portfolios containing Microsoft, Google, and Goldman Sachs
consistently perform well, reinforcing their classification as stable,

lower-risk assets.
Deeper circuits (e.g., depth 10) in larger asset configurations
are more likely to yield viable portfolios, as they support better
diversification.
• Portfolios containing Tesla or Apple frequently underperform,
validating expert caution regarding volatility and recent performance trends.
•

While quantum circuits show clear promise in rapidly generating
competitive candidate portfolios, their inherently probabilistic nature
sometimes leads to inconsistencies with forward-looking financial
expectations. The ability to narrow the solution space is valuable, but
expert oversight remains essential for final portfolio selection. This
evaluation demonstrates the role of expert analysis as a critical filter,
one that ensures practical portfolio quality beyond convergence or
historical return metrics.
F. Discussion
This study addresses the portfolio optimization problem using real
financial data over a six-month period, evaluated across two asset
configurations using various architectures and depths. While the results
demonstrate clear algorithmic convergence, particularly as circuit depth
increases, this convergence does not consistently translate into the
generation of optimal portfolios.
Although the ansatz architectures exhibit strong scalability and
optimization behavior, the portfolios they produce often fail to
align with favorable future outcomes. This limitation highlights a
critical characteristic of current quantum approaches: they operate on
historical stock data alone and do not incorporate forward-looking
or external variables that influence asset performance. Moreover,
while simulator-based results demonstrate idealized performance, real
quantum hardware introduces additional complexity, such as noise
and decoherence, which may further affect output quality.
Despite this, QC provides a potential advantage by addressing the
NP-hard nature of the portfolio optimization problem. It enables
the efficient and scalable generation of candidate portfolios that
would otherwise be computationally intensive to explore classically.
Building upon this strength, our Expert Analysis framework serves
as a complementary layer, allowing further refinement and selection
of portfolios based on future expectations, real-time dynamics, and
investor-specific constraints.
The results show that quantum-generated portfolios benefit from
expert interpretation. Our framework offers a practical path forward,
in which quantum algorithms narrow the solution space while domain
knowledge ensures financial relevance. It also leaves room for future
enhancements that incorporate probabilistic forecasting, alternative
risk models, and behavioral or ethical investment preferences.
V. C ONCLUSION
This work presents a hybrid framework for quantum-enhanced
portfolio optimization, combining quantum computational scalability
with expert-informed evaluation. Our results demonstrate that quantum
circuits, particularly at higher depths, achieve strong convergence
across varying asset configurations and ansatz architectures. However,
convergence alone does not guarantee portfolio quality, as future
performance is shaped by dynamic and unmodeled external factors.
To bridge this gap, we introduce an Expert Analysis layer that
evaluates quantum-generated portfolios beyond historical data. This
component enhances interpretability and aligns portfolio selection with
financial context and investor needs. Our findings suggest that QC
holds strong potential for addressing complex financial optimization
tasks. However, to produce robust and viable outcomes, quantum

solutions must integrate domain expertise. The proposed framework
lays the foundation for future research into adaptive, expert-guided
quantum financial systems capable of responding to both market
fluctuations and individual investor preferences.
ACKNOWLEDGMENT
This work was supported in part by the NYUAD Center for
Quantum and Topological Systems (CQTS), funded by Tamkeen
under the NYUAD Research Institute grant CG008.
R EFERENCES
[1] A. Gunjan and S. Bhattacharyya, “A brief review of portfolio optimization
techniques,” Artificial Intelligence Review, 2023.
[2] D. Herman et al., “Quantum computing for finance,” Nature Reviews
Physics, vol. 5, no. 8, pp. 450–465, 2023.
[3] N. Innan et al., “Financial fraud detection using quantum graph neural
networks,” Quantum Machine Intelligence, vol. 6, no. 1, p. 7, 2024.
[4] N. Innan, M. A.-Z. Khan, and M. Bennai, “Financial fraud detection: a
comparative study of quantum machine learning models,” International
Journal of Quantum Information, vol. 22, no. 02, p. 2350044, 2024.
[5] S. Dutta et al., “QADQN: Quantum attention deep q-network for financial
market prediction,” in 2024 IEEE International Conference on Quantum
Computing and Engineering (QCE), vol. 2. IEEE, 2024, pp. 341–346.
[6] N. Innan et al., “LEP-QNN: Loan eligibility prediction using quantum
neural networks,” arXiv preprint arXiv:2412.03158, 2024.
[7] M. E. Alami et al., “Comparative performance analysis of quantum
machine learning architectures for credit card fraud detection,” arXiv
preprint arXiv:2412.19441, 2024.
[8] N. Innan et al., “QFNN-FFD: Quantum federated neural network for
financial fraud detection,” arXiv preprint arXiv:2404.02595, 2024.
[9] P. K. Choudhary et al., “HQNN-FSP: A hybrid classical-quantum neural
network for regression-based financial stock market prediction,” arXiv
preprint arXiv:2503.15403, 2025.
[10] P. Rebentrost and S. Lloyd, “Quantum computational finance: quantum
algorithm for portfolio optimization,” KI-Künstliche Intelligenz, pp. 1–12,
2024.
[11] K. Zaman et al., “PO-QA: A framework for portfolio optimization using
quantum algorithms,” in 2024 IEEE International Conference on Quantum
Computing and Engineering (QCE), vol. 1. IEEE, 2024, pp. 1397–1403.
[12] H. Markowitz, “Portfolio selection,” The Journal of Finance, vol. 7, no. 1,
pp. 77–91, 1952.
[13] Y. Chen et al., “Benchmarking of quantum and classical computing in
large-scale dynamic portfolio optimization under market frictions,” 2025.
[14] K. Zaman et al., “A survey on quantum machine learning: Current
trends, challenges, opportunities, and the road ahead,” arXiv preprint
arXiv:2310.10315, 2023.
[15] M. Kashif, A. Marchisio, and M. Shafique, “Computational advantage
in hybrid quantum neural networks: Myth or reality?” arXiv preprint
arXiv:2412.04991, 2024.
[16] F. Phillipson and H. S. Bhatia, “Portfolio optimisation using the dwave quantum annealer,” in International Conference on Computational
Science. Springer, 2021, pp. 45–59.
[17] J. Zhou, “Quantum finance: Exploring the implications of quantum
computing on financial models,” Computational Economics, 2025.
[18] M. Hodson, B. Ruck, H. Ong, D. Garvin, and S. Dulman, “Portfolio
rebalancing experiments using the quantum alternating operator ansatz,”
arXiv preprint arXiv:1911.05296, 2019.
[19] D. J. Egger et al., “Quantum computing for finance: State-of-the-art and
future prospects,” IEEE Transactions on Quantum Engineering, 2020.
[20] D. Milhomem and M. Dantas, “Analysis of new approaches used in
portfolio optimization: a systematic literature review,” Production, 2020.
[21] A. Peruzzo et al., “A variational eigenvalue solver on a quantum processor,”
Nature Communications, vol. 5, p. 4213, 2014.
[22] G. Buonaiuto et al., “Best practices for portfolio optimization by quantum
computing, experimented on real quantum devices,” Scientific Reports,
vol. 13, no. 1, p. 19434, 2023.
[23] E. Farhi, J. Goldstone, and S. Gutmann, “A quantum approximate
optimization algorithm,” arXiv preprint arXiv:1411.4028, 2014.
[24] R. Aroussi, “yfinance,” 2023, https://pypi.org/project/yfinance/.
[25] A. Javadi-Abhari et al., “Quantum computing with qiskit,” arXiv preprint
arXiv:2405.08810, 2024.

