Achieving High-Quality Portfolio Optimization with the Variational Quantum
Eigensolver
Anbang Wang,1 Zhonggang Lv,1 Zhenyuan Ma,1 Dunbo Cai,1 and Zhihong Zhang1, ∗

arXiv:2508.18625v1 [quant-ph] 26 Aug 2025

1

Future Science and Technology Research Lab, China Mobile (Suzhou)
Software Technology Company Limited, Suzhou 215163, China

Portfolio optimization is a fundamental problem in finance that aims to determine the optimal allocation of assets within a portfolio to maximize returns while minimizing risk. It can be formulated
as a Quadratic Unconstrained Binary Optimization (QUBO) problem, which is NP-hard. Quantum
computing offers the potential to solve such problems more efficiently than classical methods. In
this work, we employ the Variational Quantum Eigensolver (VQE) to address the portfolio optimization problem. To increase the likelihood of converging to high-quality solutions, we propose
using the Weighted Conditional Value-at-Risk (WCVaR) as the cost function and the Covariance
Matrix Adaptation Evolution Strategy (CMA-ES) as the optimizer. Our experiments are conducted
using the classical simulations on the Wuyue QuantumAI platform. The results demonstrate that
the combination of WCVaR and CMA-ES leads to improved performance in solving the portfolio
optimization problem.

I.

INTRODUCTION

Portfolio optimization is a fundamental problem in finance that seeks to allocate capital across various assets.
It plays a crucial role in modern investment management
by helping investors construct efficient portfolios and
make informed decisions in complex financial markets.
This problem can be formulated as a Quadratic Unconstrained Binary Optimization problem, which is NP-hard
and thus computationally intractable on classical computers for large instances. Quantum computing offers the
potential to solve such QUBO problems more efficiently,
paving the way for significant advancements in portfolio optimization. Among the quantum algorithms, the
Variational Quantum Eigensolver [1, 2] and the Quantum
Approximate Optimization Algorithm (QAOA) [3, 4] are
two promising candidates particularly well-suited for execution on Noisy Intermediate-Scale Quantum (NISQ)
devices [5].
However, solving the QUBO problem differs significantly from finding the ground state of a typical chemical
Hamiltonian. This is because the Ising Hamiltonian corresponding to a QUBO problem consists of terms that all
commute with each other, resulting in a ground state (if
non-degenerate) that is one of the computational basis
states. Using the traditional expectation value of energy
as the cost function is therefore not ideal. To address
this challenge, Barkoutsos et al. [6] proposed using Conditional Value-at-Risk (CVaR)—a metric widely used in
finance [7]—as the cost function. The CVaR cost function aligns well with the practical objectives of portfolio
optimization and enhances the performance and robustness of VQE and QAOA. In this paper, we introduce
a novel Weighted CVaR cost function that incorporates
weights based on the energy of each sampled outcome.
We also propose using the Covariance Matrix Adapta-

∗ zhangzhihong@cmss.chinamobile.com

tion Evolution Strategy [8] as the optimizer to mitigate
the impact of potentially non-smooth or ill-conditioned
objective functions on convergence. Our experiments,
conducted using classical simulations of the VQE algorithm for portfolio optimization on the Wuyue QuantumAI platform, demonstrate that the combination of the
WCVaR cost function and the CMA-ES optimizer leads
to a significant improvement in performance.
The remainder of this paper is organized as follows:
Section II provides a brief introduction to the background, including how to model the portfolio optimization problem using a dataset of historical closing prices,
convert it into a QUBO problem, and solve it using the
VQE algorithm. Section III describes the detailed implementation of our VQE approach. Section IV presents
the results obtained from numerical calculation. Finally,
Section V concludes the paper.

II.

BACKGROUND

Portfolio optimization is a fundamental problem in finance that aims to determine the optimal allocation of
assets within a portfolio to maximize returns while minimizing risk. Modern Portfolio Theory (MPT), introduced by Harry Markowitz in 1952 [9], is a widely accepted framework for portfolio optimization. It addresses
the trade-off between risk and return through meanvariance analysis, emphasizing diversification to achieve
efficient portfolios. In this section, we demonstrate how
to formulate the portfolio optimization problem given
market data and how to reduce it to the QUBO problem and the corresponding Ising model.

A.

Portfolio Optimization

The market data is represented as a matrix P of size
M × N , where N is the number of assets, M is the

2
number of time periods, and each entry of the matrix
Pki denotes the price of asset Ai at time point tk . Let
T = (t1 , t2 , . . . , tM )T be the vector of time points. We
define the return of asset Ai at time moment tk as
Pki − Pk−1,i
.
Pk−1,i

rki =

(1)

M

1 X
rki ,
M

(2)

k=1

M

1 X
σij =
(rki − µi )(rkj − µj ).
M −1

Quadratic Unconstrained Binary Optimization

QUBO is a combinatorial optimization problem which
can be formulated as follows:
X
X
Q(x) =
qij xi xj +
qi xi + c,
(8)
i<j

Using these returns, we compute the expected return of
asset Ai and the covariance between asset Ai and Aj as
µi =

B.

(3)

k=1

Suppose we have a total budget B that we wish to allocate among N assets in the portfolio. Let bi be the
portion of the budget allocated to asset Ai . These allocations must satisfy the following constraint:
X
bi ≤ B.
(4)

where the variables xi are binary, and parameters qij , qi
and c are real numbers.
In general, the total budget B and the individual investment amounts bi are real numbers. Discretizing them
into binary variables can significantly increase the number of variables in the QUBO formulation. To avoid this
overhead, we assume that the total budget B is an integer
and that each individual allocation bi is represented by
a binary variable indicating whether asset Ai is selected.
Without loss of generality, we set B = N/2. In the following, we use xi ∈ {0, 1} to represent the binary decision
variable corresponding to asset Ai , ensuring consistency
with the notation used in the QUBO problem (8). Our
goal then becomes minimizing the objective function
C ′ (x) = −λC1 (x) + (1 − λ)C2 (x)

i

Portfolio optimization involves two primary objectives:
maximizing return and minimizing risk. The expected
return, computed from historical market data, serves as
a reasonable estimate for future performance. Therefore,
the first objective function to maximize is the expected
return, given by:
C1 (b) =

N
X

µi bi ,

(5)

i=1

where b = (b1 , b2 , . . . , bN )T is the vector of investment
allocations. The risk of the portfolio is typically measured by its volatility, which is the square root of the
portfolio variance. Hence, the second objective function
to minimize is the portfolio variance:
X
C2 (b) =
σij bi bj .
(6)

N
X

xi = N/2.

(7)

Our aim is to minimize the combined objective function
C ′ (b) subject to the constraint (4).

(10)

i=1

The constraint in Eq. (10) can be incorporated into the
objective function using a penalty method. Specifically,
PN
we add a penalty term of the form p( i=1 xi − N/2)2 ,
where p > 0 is a sufficiently large penalty coefficient. The
resulting final objective function to minimize is:
C(x) = −λC1 (x) + (1 − λ)C2 (x) + p(

N
X

xi −

i=1

N 2
)
2
(11)

= −λ

N
X

µi xi + (1 − λ)

i=1

The portfolio optimization problem is inherently a
multi-objective optimization problem, involving two objective functions and one constraint. To solve such a
problem, one seeks the Pareto front—also known as the
efficient frontier in finance—which consists of solutions
that cannot be improved in one objective without worsening the other. A common approach to finding the Pareto
front is the scalarization method using linear weighting.
In this method, the two objectives are combined into a
single objective function by introducing a weighting factor λ:

(9)

subject to the constraint

ij

C ′ (b) = −λC1 (b) + (1 − λ)C2 (b).

i

N
X

N
X

σij xi xj

i=1 j=i+1

N
X
N
+ p(
xi − ) 2 .
2
i=1

C.

(12)

Variational Quantum Eigensolver

The QUBO problem is mathematically equivalent to
the Ising model. To transform the problem, we introduce
a spin vector s, where each element is defined as si =
1 − 2xi , mapping the binary variables xi ∈ {0, 1} to spins
{1, −1}. The objective function in Eq. (12) can then be
rewritten in the (classical) Ising form:
X
X
E(s) = −
hi si −
Jij si sj ,
(13)
i=1

i<j

3
where hi and Jij are real coefficients derived from the
QUBO objective function (12). The corresponding quantum Ising Hamiltonian is obtained by replacing the classical spin variables si with Pauli operators Ẑi :
X
X
Ĥ = −
hi Ẑi −
Jij Ẑi Ẑj .
(14)
i=1

i<j

Like QUBO, the (classical) Ising model is generally
NP-hard and therefore cannot be solved efficiently in
the worst case. However, if we can find the ground
state of the corresponding quantum Ising Hamiltonian,
we can determine the ground state of the classical Ising
model—thereby solving the original QUBO problem.
Finding the ground state of a general quantum system
is known to be QMA-complete, which is considered the
quantum analog of NP-completeness. In principle, even
quantum computers are not expected to solve such problems efficiently in general. Nevertheless, several heuristic
quantum algorithms have been proposed that may offer
advantages for certain problem instances. These include
VQE, QAOA, and quantum annealing [10]. In this work,
we focus on the VQE algorithm.
VQE is is a hybrid quantum-classical algorithm. In this
approach, a quantum computer is used to prepare a quantum state and measure the expectation value of a given
Hamiltonian, while a classical computer performs an optimization to minimize this expectation value. Given a
Hamiltonian Ĥ, and a parameterized trial wave function
(known as an ansatz) ψ(θ), the VQE algorithm seeks the
optimal parameter vector θm that minimizes the energy
expectation value (the cost function), or Rayleigh quotient:
E(θ) =

⟨ψ(θ)|Ĥ|ψ(θ)⟩
.
⟨ψ(θ)|ψ(θ)⟩

(15)

If we assume the state is normalized, the denominator
vanishes.
The VQE algorithm was originally proposed and is
widely used to solve problems in physics and chemistry.
The Ising Hamiltonian represents a special case, as its
eigenstates are the computational basis states. Let the
eigensystem of the Ising Hamiltonian be defined by
Ĥ|n⟩ = En |n⟩,

(16)

where the eigenstates are ordered in ascending order of
energy„ i.e., |1⟩ denotes the ground state with energy E1 .
For a given parameter θ ∗ , the variational wave function
can be expanded in this eigenbasis as
X
|ψ(θ ∗ )⟩ =
cn (θ ∗ )|n⟩,
(17)
n

and the corresponding energy expectation value is
X
E(θ ∗ ) =
|cn (θ ∗ )|2 En .
(18)
n

We already know that the ground state is |1⟩, with
ground state energy E1 . This state can, in principle,
be reached in the expansion (17) by setting c1 (θ ∗ ) = 1
and all other coefficients ci (θ ∗ ) = 0. However, it is generally difficult to design an ansatz capable of collapsing
exactly to a specific computational basis state. Consequently, minimizing the energy expectation value (15)
may not be an effective strategy for guiding the VQE
algorithm toward the true ground state. Instead, the
Conditional Value at Risk (CVaR) has been proposed as
a more suitable cost function [6]. Suppose we prepare a
parameterized trial wave function ψ(θ) and measure it in
the computational basis, obtaining a set of bitstrings xk .
We then compute the energy of each measured bitstring
as Ek = ⟨xk |Ĥ|xk ⟩. This process is repeated K times,
yielding a set of sampled energies. These energies are
sorted in ascending order to form the ordered sample set
E = (E(1) , E(2) , . . . , E(K) ), where E(k) denotes the k-th
smallest value. For a given confidence level α ∈ (0, 1],
CVaR is defined as the average of the smallest ⌈αK⌉ energies:
⌈αK⌉

CVaRα (E) =

X

Ek .

(19)

k=1

When α = 1, CVaR1 reduces to the mean of the sampled
energies
K

Ē =

1 X
Ek ,
K

(20)

k=1

which approximates the standard energy expectation
value (15). When α is sufficiently small such that
⌈αK⌉ = 1, CVaRα becomes the minimum observed energy. If the variational ansatz has non-zero overlap with
the true ground state for all parameter values, this minimum can, in principle, converge to the ground state energy. However, for very small α, the cost function becomes non-smooth, making it difficult for classical optimizers to navigate the landscape effectively. Therefore, a
moderate value of α is typically chosen to balance exploration of low-energy states with optimization stability.
III.

DESIGN OF OUR VQE ALGORITHM

In this section, we detail the design of our VQE algorithm.
A.

Weighted CvaR

In Reference [6], the authors demonstrate that using the CVaR cost function leads to faster convergence
and better solutions for the combinatorial optimization
problems they tested, including portfolio optimization.
Standard CVaR assumes that all outcomes within the

4
worst α-fraction (e.g., the most extreme losses) contribute equally to the average, assigning them uniform
weights. However, in practice, greater concern is often
placed on the most extreme outcomes within this tail.
To better reflect this preference, a weighted sum may be
more appropriate. To enhance performance, we propose
using a weighted CVaR as the cost function, where the
weights are determined by the (relative or absolute) values of the energies within the tail. The WCVaR cost
function is defined as:
⌈αK⌉

WCVaRα (E) =

X

wk Ek ,

(21)

RY and RZ gates as our first circuit structure. Specifically, we use the two-local ansatz with RY and RZ gates
for the single-qubit rotation layers. Additionally, motivated by the work of [11], we design a second ansatz—the
block ansatz—based on a general two-qubit building
block. This block contains two CNOT gates and can implement arbitrary controlled-unitary operations [12]. In
both ansatzes, entanglement is introduced through pairwise connections between adjacent qubits. The circuit
diagrams for these two ansatzes are shown in Figure 1.
（ a）

Block

k=1

where wk denotes the weight assigned to the k-th smallest
energy E(k) in the ordered sample set, and the weights
satisfy the normalization condition:
⌈αK⌉

X

wk = 1.

(22)

Block

(b)

k=1

The choice of weight plays a central role in WCVaR. We
use the piecewise exponential weighting function with the
details given in appendix A.
B.

Covariance Matrix Adaptation Evolution
Strategy

While the mean sampled energy (15) can be a poor
cost function for VQE, both CVaR (19) and weighted
CVaR (21) offer significant improvements by focusing
optimization on low-energy states. However, these cost
functions are typically non-smooth and noisy, which can
hinder gradient-based optimizers and make it difficult
to locate the minimum reliably. To address this challenge, we employ the Covariance Matrix Adaptation Evolution Strategy, a popular derivative-free optimization
algorithm known for its effectiveness on nonlinear, nonconvex, and noisy problems [8]. The core idea of CMAES is to iteratively improve a population of candidate solutions using an evolutionary strategy, gradually adapting the search distribution to converge toward the global
optimum. Since CMA-ES does not require gradient information and is robust to noise, it is well-suited for optimizing the VQE cost function.
For benchmarking purposes, we also use the COBYLA
optimizer, which has been reported as one of the most
stable optimizers for VQE in Reference [2].
C.

VQE ansatz

Reference [2] reports that the Pauli two-design ansatz
performs best among the architectures evaluated. However, its use of random single-qubit rotation gates makes
it difficult to reproduce and unsuitable for reliable benchmarking. Therefore, we adopt the two-local ansatz with

FIG. 1. The ansztzes for the VQE algorithm in this work.
(a) A three-layer two-local ansatz. We use RY and RZ gates
for the single-qubit rotation layers. Pairwise CNOT gates are
used between layers. (b) A two-layer block ansatz. Each block
contains two CNOT gates. This quantum circuit diagram was
plotted using Qiskit [13].

D.

Wuyue platform

We implemented our VQE algorithm using the Wuyue
QuantumAI computing framework, a cloud-based platform [14] for quantum computing. This framework offers a diverse set of modularized ansatz choices, enabling
rapid prototyping and testing of variational quantum
circuits. Furthermore, its high-performance statevector
simulator, capable of emulating circuits with up to 30
qubits, was employed to obtain benchmark results without quantum noise.

IV.

NUMERICAL RESULTS

We constructed a 12-stock portfolio comprising 6 Chinese A-shares and 6 U.S. equities to enable a cross-market
optimization analysis. The A-share constituents were
selected to represent diverse sectors, including financial
services, consumer staples, technology, and energy. In
contrast, the U.S. holdings are primarily large-cap technology companies and other sector leaders. This compo-

5
the weighted CVaR (WCVaR) cost function shows
no significant dependence on α. At α = 1 or
α = 0.5, CVaR performs considerably worse than
WCVaR. However, when α = 0.25 or α = 0.1,
CVaR’s performance, although slightly inferior, becomes comparable to that of WCVaR. The property
that WCVaR’s performance does not depend on α
allows us to directly choose α = 1, thereby avoiding the impact of hyperparameter selection on the
efficiency of the VQE algorithm.

sition provides diversified exposure across market capitalizations, industries, and geographic regions. Daily
closing prices for the calendar year 2024 were obtained
using the Yahoo Finance API via the Python library yfinance [15, 16]. These price data were processed into daily
return series and used to compute the covariance matrix,
both of which serve as inputs for the subsequent portfolio
optimization. The dataset is available for download at:
https://github.com/lvzggg/portfolio_vqe.git.
1.0

96.0%

92.0%

= 1.0

89.0%

91.0%

= 0.5

• On average, the CMA-ES optimizer outperforms
the COBYLA optimizer. Further numerical analysis reveals that even with up to 300 iterations,
COBYLA still fails to achieve the performance level
attained by CMA-ES within just 100 iterations.
Therefore, we conclude that CMA-ES is superior
to COBYLA for this problem, and we restrict subsequent experiments to the CMA-ES optimizer.

0.8
0.6
0.4
0.2

7.0%

0.0
1.0 93.0%

Top-10 Hit Rate

0.8
0.6

8.0%

12.7%
2.0% 0.0%
0.0%

86.0%
75.0%

= 0.25

55.0%

5.0%

7.0%

98.0%
87.0%

0.7% 0.7%

95.0%

65.0%

8.7%

0.0%

= 0.1

74.0%
64.7%60.0%

• The COBYLA optimizer appears to be more compatible with the CVaR cost function, particularly
at α = 0.25, while the CMA-ES optimizer demonstrates greater compatibility with the WCVaR cost
function. This may suggest that the choices of optimizer, cost function, and even ansatz should be
considered holistically, as there is no single optimal
choice for any one aspect in isolation.

0.4
0.2

0.0%

CM
CM A+A
A+ 1+C
A V
CM 1+W aR
A
CM +A CVaR
A 2
CO +A2 +CVa
CO BYLA +WC R
BY +A Va
LA 1 R
CO +A1 +CVa
B
CO YLA +WC R
BY +A Va
LA 2+ R
+A CV
2+ aR
WC
Va
R
CM
A
+
CM A
A+ 1+C
A V
CM 1+W aR
A
CM +A CVaR
A 2
CO +A2 +CVa
B
Y
CO LA +WC R
BY +A Va
LA 1 R
CO +A1 +CVa
B
CO YLA +WC R
BY +A Va
LA 2+ R
+A CV
2+ aR
WC
Va
R

0.0

17.3%
10.0%
1.3%
0.0%

FIG. 2. Success rate during the optimization process for various combinations of ansatzes, optimizers, and cost functions.
A1 and A2 denote the two-local ansatz and the block ansatz,
respectively.

 & 0 $    $     & 9 D 5

   

   

 & 0 $    $     : & 9 D 5
 & 0 $    $     & 9 D 5

   

 & 0 $    $     : & 9 D 5

   

   
   

   

• The performance of the CVaR cost function improves as α decreases, whereas the performance of

   
   
   

      

   

 ( [ D F W  6 R O X W L R Q  3 U R E D E L O L W \

To evaluate the performance of the VQE algorithm,
we assessed its success rate over the course of the optimization. Specifically, in each iteration, the quantum
state output by VQE was projected onto the computational basis. The algorithm was deemed successful in that
iteration if the exact ground state (i.e., the optimal solution) was found among the top 10 states ranked by their
measurement probabilities. The overall performance was
then quantified as the total number of successful iterations.
The results are presented in Fig. 2, where the first 100
iterations are shown for the CMA-ES optimizer and the
first 150 iterations for the COBYLA optimizer. It is rare
for the VQE algorithm to find the optimal solution in
one iteration and then fail to find it in the subsequent
iteration. Therefore, Fig. 2 can also be interpreted as
a measure of convergence speed: a higher success rate
indicates faster convergence. There is no significant difference in performance between the two-local ansatz and
the block ansatz. However, both the choice of optimizer
and the cost function have a substantial impact on performance. The main findings are summarized as follows:

      

   

    

   

    

   

    
   
    
   

    

       

   
 

  

  

  

  

   

      

    
 

  

  

  

  

   

 , W H U D W L R Q V

FIG. 3. The probability of sampling the optimal solution for
various combinations of ansatzes, optimizers, and cost functions. A1 and A2 denote the two-local ansatz and the block
ansatz.

In Fig. 3, we present the probability of sampling the
optimal solution (i.e., the overlap between the VQE variational state and the ground state) as a function of the
number of iterations. For consistency with previous results, only the first 100 iterations are shown for the CMAES optimizer. The observed trends are consistent with
those in Fig. 2.

6
V.

CONCLUSIONS

In this work, we address the portfolio optimization
problem using the Variational Quantum Eigensolver
(VQE) algorithm. We employ a dataset comprising 12
stocks and implement the VQE algorithm on a classical
simulator on Wuyue QuautumAI platform. Our investigation focuses on the performance of VQE under various optimization configurations, particularly the interplay between ansatz design, cost functions, and classical
optimizers. Empirical evaluation demonstrates that the
choice of optimizer and cost function significantly impacts convergence behavior and solution quality. Simulation results indicate that, among the configurations
considered, the combination of the CMA-ES optimizer
and the Weighted Conditional Value-at-Risk (WCVaR)
cost function yields the best performance. We believe
these findings enhance our understanding of the role of
optimization in VQE-based portfolio optimization and
provide valuable guidance for future research.
ACKNOWLEDGMENTS

We acknowledge the support from Basic Research for
Application Program of China Mobile (No. R251166S).

parameter that controls the concentration of weights on
low-energy states.
The second variant is the rank-based exponential
weighting:
wk = exp (−βk) ,

where β is again an inverse temperature parameter. This
form assigns weights based solely on the rank k of the
energy value, independent of its absolute magnitude.
The third variant is a piecewise exponential weighting
function, designed to allow different decay rates across
segments of the ordered sample:


if k < N1 ,
exp (−β1 k)
wk = exp (−β2 (k − N1 )) · wN1 −1 if N1 ≤ k < N2 ,

exp (−β (k − N )) · w
if k ≥ N2 .
3
2
N2 −1
(A4)
Here, N1 and N2 (with N1 < N2 ) are positive integers defining the transition points between segments, and
β1 , β2 , β3 > 0 are positive decay parameters. The continuity of the weights at k = N1 and k = N2 is ensured by
multiplying the exponential in each subsequent segment
by the weight value at the end of the previous segment
(e.g., wN1 −1 and wN2 −1 ).

In this section, we describe the weighting schemes employed in the WCVaR cost function. We assume the sampled energies are sorted in ascending order, forming an
ordered set E = (E(1) , E(2) , . . . , E(K) ), where E(k) denotes the k-th smallest energy value. For brevity, we
present only the unnormalized weights.
The standard Conditional Value-at-Risk (CVaR) can
be viewed as a special case of WCVaR, where equal
weights are assigned to the ⌈αK⌉ smallest values in the
sample set, and zero weight to all others:
(
1 if k ≤ ⌈αK⌉
wk =
(A1)
0 otherwise
The exponential weighting function is well-known to
researchers in both physics and computer science, as it
arises naturally in Boltzmann’s law in statistical physics
and the softmax function in machine learning and optimization. In this work, we employ three distinct variants
of the exponential weighting function to explore their impact on the WCVaR cost function.
The first variant is the energy-based exponential
weighting:


wk = exp −β(E(k) − E0 ) ,
(A2)
where E0 = E(1) denotes the minimum energy value observed in the sample set, and β is an inverse temperature

 ) L Q D O  ( [ D F W  6 R O X W L R Q  3 U R E D E L O L W \

   

Appendix A: Weights in WCVaR cost function

(A3)

 & 0 $    $     : 
 & 0 $    $     : 

   

 & 0 $    $     : 
 & 0 $    $     : 

   
   
   
   
   
   
   
   

    

   

 

FIG. 4. Probability of sampling the optimal solution under
different weighting schemes. The blue solid line (W1), red
dashed line (W2), black dash-dotted line (W3), and green
dotted line (W4) denote the CVaR, energy-based exponential
weighting, rank-based exponential weighting, and piecewise
exponential weighting cost functions, respectively.

In Fig. 4, we present the probability of sampling the
optimal solution under four different weighting schemes.
CVaR performs well when α is small but poorly when α
is large. The energy-based exponential weighting scheme
yields the worst performance; therefore, its piecewise
variant is not considered further. In contrast, the rankbased exponential weighting performs well, particularly
when α is large. The piecewise exponential weighting
function outperforms the rank-based version, although

7
the improvement is not significant. Consequently, we
adopt the piecewise exponential weighting function in
the main part of this work. However, if minimizing the

number of hyperparameters is a priority, the rank-based
weighting function remains a viable and effective alternative.

[1] Peruzzo, A.; McClean, J.; Shadbolt, P.; Yung, M.H.;
Zhou, X.Q.; Love, P.J.; Aspuru-Guzik, A.; O’brien,
J.L. A variational eigenvalue solver on a photonic quantum processor. Nature communications 2014, 5, 4213.
https://doi.org/10.1038/ncomms5213.
[2] Buonaiuto, G.; Gargiulo, F.; De Pietro, G.; Esposito,
M.; Pota, M. Best practices for portfolio optimization
by quantum computing, e xperimented on real quantum
devices. Scientific Reports 2023, 13, 19434. Publisher:
Nature Publishing Group, https://doi.org/10.1038/
s41598-023-45392-w.
[3] Farhi, E.; Goldstone, J.; Gutmann, S. A Quantum Approximate Optimization Algorithm, 2014, [arXiv:quantph/1411.4028].
[4] Brandhofer, S.; Braun, D.; Dehn, V.; Hellstern, G.;
Hüls, M.; Ji, Y.; Polian, I.; Bhatia, A.S.; Wellens, T.
Benchmarking the performance of portfolio optimization
with QAOA. Quantum Information Processing 2022, 22.
https://doi.org/10.1007/s11128-022-03766-5.
[5] Preskill, J. Quantum Computing in the NISQ era and
beyond. Quantum 2018, 2, 79. https://doi.org/10.
22331/q-2018-08-06-79.
[6] Barkoutsos, P.K.; Nannicini, G.; Robert, A.; Tavernelli,
I.; Woerner, S. Improving Variational Quantum Optimization using CVaR. Quantum 2020, 4, 256. https:
//doi.org/10.22331/q-2020-04-20-256.
[7] Acerbi, C.; Tasche, D.
On the coherence of expected shortfall. Journal of Banking & Finance 2002,

26, 1487–1503. https://doi.org/https://doi.org/10.
1016/S0378-4266(02)00283-2.
[8] Hansen, N. The CMA Evolution Strategy: A Tutorial,
2023, [arXiv:cs.LG/1604.00772].
[9] Markowitz, H. Portfolio Selection. The Journal of Finance 1952, 7, 77–91. Publisher: [American Finance Association, Wiley], https://doi.org/10.2307/2975974.
[10] Johnson, M.W.; Amin, M.H.S.; Gildert, S.; Lanting, T.;
Hamze, F.; Dickson, N.; Harris, R.; Berkley, A.J.; Johansson, J.; Bunyk, P.; et al. Quantum annealing with
manufactured spins. Nature 2011, 473, 194–198. Publisher: Nature Publishing Group, https://doi.org/10.
1038/nature10012.
[11] Chivilikhin, D.; Samarin, A.; Ulyantsev, V.; Iorsh, I.;
Oganov, A.R.; Kyriienko, O. MoG-VQE: Multiobjective genetic variational quantum eigensolver, 2020,
[arXiv:quant-ph/2007.04424].
[12] Nielsen, M.A.; Chuang, I.L. Quantum Computation and
Quantum Information: 10th Anniversary Edition; Cambridge University Press, 2010.
[13] Qiskit: An Open-source Framework for Quantum Computing. https://qiskit.org. Accessed: 2025-08-14.
[14] WuYue. https://ecloud.10086.cn/portal/product/
WYQCLOUD. Accessed: 2025-08-14.
[15] Yahoo! Finance. https://finance.yahoo.com/. Accessed: 2025-08-14.
[16] yfinance 0.2.65. https://pypi.org/project/yfinance/.
Accessed: 2025-08-14.

