www.nature.com/scientificreports

OPEN

Multiclass portfolio optimization
via variational quantum
Eigensolver with Dicke state ansatz
J. V. S. Scursulim, Gabriel M. Langeloh, Victor L. Beltran & Samuraí Brito
Combinatorial optimization is a fundamental challenge in various domains, with portfolio optimization
standing out as a key application in finance. Despite numerous quantum algorithmic approaches
proposed for this problem, most overlook a critical feature of realistic portfolios: diversification.
In this work, we introduce a novel quantum framework for multiclass portfolio optimization that
explicitly incorporates diversification by leveraging multiple parametrized Dicke states, simultaneously
initialized to encode the diversification constraints, as an ansatz of the Variational Quantum
Eigensolver. A key strength of this ansatz is that it initializes the quantum system in a superposition
of only feasible states, inherently satisfying the constraints. This significantly reduces the search
space and eliminates the need for penalty terms. In addition, we also analyze the impact of different
classical optimizers in this hybrid quantum-classical approach. Our findings demonstrate that, when
combined with the CMA-ES optimizer, the Dicke state ansatz achieves superior performance in terms
of convergence rate, approximation ratio, and measurement probability. These results underscore
the potential of this method to solve practical, diversification-aware portfolio optimization problems
relevant to the financial sector.
Quantum Computing (QC) represents a groundbreaking technology poised to solve problems that lie beyond
the capabilities of classical computers. It operates by manipulating quantum systems and harnessing unique
properties such as superposition, interference, and entanglement. This approach enables the execution of
advanced algorithms designed to address complex challenges with remarkable efficiency. The potential of
quantum computing spans multiple fields, promising significant impacts across industries and scientific
disciplines; some of them include: quantum chemistry and material science1–3, machine learning4–9, finance10–17,
and optimization18–24.
Optimization plays a fundamental role across various domains, with classic examples including the traveling
salesman problem25, vehicle routing26, bin packing27, and portfolio optimization28-the central focus of this
article. These problems are traditionally tackled using classical techniques such as mixed-integer programming29,
approximation algorithms and metaheuristics30, and neural networks31,32. However, due to their computational
complexity, these methods tend to have limitations in either their running time or solution quality as the number
of variables increases.
Portfolio optimization exemplifies this challenge, especially in multiclass scenarios that require allocation
across diverse asset categories (e.g., equities, bonds, commodities). While classical approaches like the
Markowitz mean-variance model33 perform well for small-scale instances, multiclass formulations introduce
combinatorial and equality constraints that lead to mixed-integer quadratic programs (MIQPs), which are hard
to solve optimally, particularly in real-time or resource-limited settings.
In response to these limitations, Variational Quantum Algorithms (VQAs)34,35 have emerged as promising
tools for near-term quantum advantage. Designed for Noisy Intermediate-Scale Quantum (NISQ) devices, VQAs,
especially the Variational Quantum Eigensolver (VQE)36, have demonstrated potential in solving combinatorial
problems by mapping them to Ising Hamiltonians and approximating the ground state via parameterized
quantum circuits. The effectiveness of this approach heavily depends on the choice of ansatz, particularly when
handling complex constraints such as those in multiclass portfolio optimization.
To that end, this paper proposes the use of a Dicke state-based ansatz within the VQE framework to
efficiently handle multiclass portfolio optimization, incorporating a realistic feature in this problem related
to diversification of the investment. Our contributions are threefold: (i) Modeling advantage - we formulate a
multiclass portfolio optimization problem suitable for quantum encoding by introducing a parameterized Dickestate ansatz, in which diversification constraints are inherently satisfied through state preparation, eliminating
Instituto de Ciência e Tecnologia Itaú, São Paulo, Brazil. email: jose.scursulim@itau-unibanco.com.br;
samurai.brito@itau-unibanco.com.br

Scientific Reports |

(2026) 16:6208

| https://doi.org/10.1038/s41598-026-36333-4

1

www.nature.com/scientificreports/
the need for penalty calibration; (ii) Search-space advantage - by employing the Dicke state within the VQE
framework, we drastically reduce the effective search space, restricting the sampling and optimization to the
feasible manifold, which improves sample efficiency and convergence stability; and (iii) Empirical advantage in our simulations, the Dicke ansatz combined with CMA-ES achieved higher approximation ratios and more
frequent identification of the global optimum than standard ansatzes at comparable parameter counts. We make
no claim of asymptotic quantum speedup but demonstrate meaningful structural and practical improvements
within the variational paradigm.
This paper is organized as follows: the first section introduces the problem of multiclass portfolio
optimization. Subsequently, we provide an overview of VQE and the standard ansatz. We then describe the
problem formulation, the Dicke state ansatz, and the methodology employed. Finally, we present the numerical
results, empirical findings, and discussions. The paper concludes with a summary of the main contributions and
outlines directions for future research in quantum finance.

Multiclass portfolio optimization

In practical financial scenarios, optimizing solely for return and risk is insufficient. A realistic and robust
portfolio must also incorporate diversification constraints. This involves not only selecting a larger number of
assets, but also ensuring representation across different asset classes, such as stocks, bonds, and other financial
instruments (see Fig.1).
Diversification reduces exposure to specific market segments, enhances portfolio resilience, and aligns with
best practices in risk management. In its classical form, the objective is to select a subset of assets that minimizes
portfolio risk while maximizing expected return, under a given level of risk aversion33, as formulated below
min

x ∈ {0,1}n

qxT Σx − (1 − q)xT µ + rf ,

s.t. Ax = b.

(1)

where x is a binary decision vector such that an entry equal to 1 indicates the inclusion of a corresponding
asset in the portfolio, Σ is the covariance matrix of asset returns, capturing the portfolio’s overall risk, while
µ represents the expected return vector. The parameter rf denotes the risk-free rate, such as the return of US
Treasury bonds. The matrix Am×n encodes the linear constraints that govern portfolio selection, where m is the
number of constraint equations and typically corresponds to the number of asset classes or diversification. In the
example of Fig. 1, aij = 1 whenever asset j belongs to class i and aij = 0 otherwise. To simplify and reduce the
number of experimental parameters, we set q = 0.5.
This formulation enables the inclusion of constraints that promote diversification, by limiting or enforcing
the number of assets selected within each predefined class. Such constraints are essential for constructing welldiversified portfolios, which are less exposed to specific sector or asset risks, and thus more resilient to market
fluctuations.

Fig. 1. Illustrative example of a multiclass portfolio optimization problem with a predefined asset class
allocation to ensure diversification aiming the reduction of market risk. The total number of assets considered
is 820, distributed as follows: 500 stocks, 200 cryptocurrencies, 30 commodities, 10 ETFs, 60 REITs and 20
Bonds. For each class there are Cn,k possible portfolios, where n represents the total number of assets in the
class and k is the predefined number of assets to be selected. The goal of this portfolio optimization is to find
the best set of assets that will produce a portfolio that satisfies the constraints maximizing the return and
minimizing the risk.

Scientific Reports |

(2026) 16:6208

| https://doi.org/10.1038/s41598-026-36333-4

2

www.nature.com/scientificreports/

Variational quantum algorithms and ansatz

The primary VQAs for combinatorial optimization are VQE36 and the Quantum Approximate Optimization
Algorithm (QAOA)37. In this work, we focus only on VQE in the context of multiclass portfolio optimization (see
Fig.2). Both approaches utilize a parameterized quantum circuit, commonly referred to as an ansatz, together
with a classical optimization routine. Their objective is to minimize the expectation value of the problem
Hamiltonian (H) which encodes the specific combinatorial optimization problem to be solved, as showed in the
equation below:
⃗
⃗
min ⟨ψ(θ)|H|ψ(
θ)⟩.
(2)

⃗ ∈ Rn
θ

The expectation value defined in equation (2) is lower bounded by the minimum eigenvalue of the Hamiltonian
H, known as the energy of the ground state E0 . The primary goal of this approach is to identify an appropriate
ansatz along with an optimal set of parameters θ⃗∗ , such that the expected value computed ⟨ψ(θ⃗∗ )|H|ψ(θ⃗∗ )⟩
is equal or close to E0 . Quantum mechanics guarantees the existence of this lower bound38, although its exact
value is generally unknown beforehand. Thus, the variational method provides a practical way to approximate
both the ground-state wavefunction and its corresponding energy.
The main difference between VQE and QAOA is that the latter is a special case of the former, once the QAOA
ansatz has a well-defined structure based on the adiabatic theorem38, which, in general, leads to deeper quantum
circuits. There is a trade-off between these algorithms, VQE offers a shallow quantum circuit with a higher
number of parameters, meanwhile QAOA offers a deeper ansatz with 2p parameters, where p represents the
number of layers, so in some cases QAOA could solve a problem using fewer parameters but at the cost of using
a deeper circuit. In any case, both have the potential to extract useful results from NISQ devices.
Some key challenges in applying VQE to practical scenarios are identifying the optimal ansatz, determining
efficient parameter initialization methods, and selecting the most suitable classical optimizer. In this study, we
systematically explored various ansatzes to determine the most suitable configuration for our specific problem.
The investigated ansatzes can be categorized into three distinct types: (i) simple Ry rotation gates, (ii) the
extensively studied TwoLocal ansatz along with its variants13, and (iii) the parameterized Dicke state. A detailed
schematic representation of each ansatz is provided in Fig.3.
The TwoLocal ansatz is a widely employed variational quantum circuit used in VQE. It consists of two
types of parameterized quantum gates arranged in alternating layers: single-qubit rotation gates, such as Rx ,
Ry , or Rz , and two-qubit entanglement gates, such as CNOT. The structure typically begins with rotation gates
applied individually to each qubit, followed by layers of entangling gates that couple pairs of qubits, fostering
quantum correlations essential for capturing complex solution spaces. This alternating pattern of rotations
and entanglement can be repeated multiple times to increase the ansatz’s expressivity. Due to its flexibility and
relative simplicity, the two-local ansatz has proven effective in approximating solutions for various optimization
problems on current NISQ devices.

Portfolio optimization and Dicke state

To address portfolio optimization with quantum computing, first we need to convert Eq.(1) to a Quadratic
Unconstrained Binary Optimization (QUBO) problem39, then the QUBO is converted to an Ising model through
i ) 40
the change of variables xi = (1−z
2

Fig. 2. An illustrative example of a VQE routine, which is defined by a quantum state preparation conducted
on a quantum device or simulator, followed by an optimization process in a classical computer. In the quantum
routine, we start with a quantum state where all qubits are in state |0⟩, this initial state evolves according to
the unitary U (θ⃗i ), which defines ansatz structure and receives a set of parameters that will define the states
probability distribution extracted from a certain number of measurements. The classical routine is focused on
updating the set of parameters θ⃗i , in order to minimize the expectation value of the Hamiltonian that encodes
the optimization problem. This process is repeated until the maximum number of iterations or when other
stopping criteria are achieved.

Scientific Reports |

(2026) 16:6208

| https://doi.org/10.1038/s41598-026-36333-4

3

www.nature.com/scientificreports/

Fig. 3. Schematic representation of the ansatzes explored in this work: (a) and (b) depict the Dicke State, while
(c) and (d) illustrate the Ry and Two Local ansatz, respectively. In this example, the portfolio consists of 5
assets categorized into 2 classes-3 bonds and 2 stocks. The optimization goal is to select 2 bonds and 1 stock
to maximize returns and minimize risks. For a consistent comparison, the different ansatzes are configured to
have a comparable number of parameters, with the parameterized Dicke state serving as the reference.

min

x ∈ {0,1}n

qxT Σx − (1 − q)xT µ + rf + λ (Ax − b)2 .(3)

With that, the equality constraints become a penalty term in the objective function and its intensity is regulated
by the Lagrange multiplier λ. Using information about the structure of the optimization problem, it is possible
to encode constraint properties in the ansatz, which produces a quantum state that satisfies the constraints.
Therefore, we can remove the penalty term from equation 3 setting λ = 0 if the ansatz guarantees a feasible
solution.
To enhance the approach, we can leverage knowledge about the optimization problem structure to design
more efficient circuits. For example, let us consider a portfolio optimization problem with n variables and
constraints that specify the exact number of k assets that must be selected to minimize risk and maximize return.
In realistic scenarios, usually k ≪ n in order to obtain simpler and more explainable portfolios with an adequate
level of diversification without reducing potential returns. In this situation, feasible candidate solutions must
have a Hamming weight equal to k. The size of the set of feasible solutions is given by Cn,k = n!/k!(n − k)!.
Consequently, among all 2n quantum states, we eliminate those that do not meet the specified constraints. By
initializing the quantum state in a superposition that encompasses only feasible solutions, the search space is
effectively reduced from O(2n ) to O(nk ). Hence, the quantum state suitable for handling such constraints is
known as the Dicke state43, which is a quantum state related to a fundamental model of quantum optics that
describes the interaction between light and matter44. The general formula for a uniform distribution of quantum
states with n qubits and Hamming weight k is defined by45
|Dkn ⟩ = Cn,k

−1/2

∑
i

Pi |0⟩⊗ (n−k) ⊗ |1⟩⊗ k ,(4)

where Pi represents each possible permutation of a quantum state with n qubits with k qubits equal to |1⟩. There
are several different implementations of the Dicke state (see Table 1). The quantum state defined by Eq.(4), was
used as the initial state for QAOA in46–50, and in these references the authors tested a variety of mixers. Beyond
the scope of optimization, Dicke states are relevant to the following fields: quantum game theory51, quantum
networks52, quantum metrology53, quantum error correction54 and quantum storage55.
Beyond their broad applicability, Dicke states also serve as a foundation for our proposed ansatz in variational
quantum algorithms. In this study, we assume all-to-all qubit connectivity to emphasize the conceptual
contribution of the Dicke-state formulation and its ability to enforce diversification constraints without penalty
terms. Nevertheless, the approach is not limited to this topology. As shown in Table 1, existing Dicke-state
preparation circuits support all-to-all, grid, and linear-nearest-neighbor (LNN) architectures, with different
trade-offs in depth and two-qubit gate count. Hence, the framework is hardware-agnostic, as preparing each
class subspace only requires initializing a fixed-Hamming-weight superposition.
This ansatz fits perfectly with the portfolio optimization problem subject to a constraint of a fixed number
of products, since it creates a superposition in the space of feasible solutions. To address portfolio optimization
through VQE with the Dicke state ansatz, we use its parameterized version (see Fig.3b):
⃗ =
|Dkn (θ)⟩
Scientific Reports |

(2026) 16:6208

∑
i

⊗ (n−k)
⃗
Pi ai (θ)|0⟩
⊗ |1⟩⊗ k ,(5)

| https://doi.org/10.1038/s41598-026-36333-4

4

www.nature.com/scientificreports/

Method

Depth CNOTs

nCN OT s

np

Topology

41

O(nk)

5nk − 5k2

N/A

all-to-all

k(k+1)
kn −
2

all-to-all

N/A

all-to-all

N/A

grid

2
nk − 3k2

LNN

2
n(k+1)
− k4
2

LNN

Ours

O(nk)

5nk − 5k

42

O(k log n
k)

O(nk)

k)

O(nk)

√n

42

O(k

43

2(n − k)

2nk − 3k

2n

2
nk − k2

43

2

2

Table 1. A comparison between different implementations of the Dicke state circuit explored in the literature.
The circuits metrics considered are: the complexity of depths of CNOTs, the scaling of number of CNOTs
(nCN OT s ) and number of parameters np with n and k, and topology. These metrics are relevant for resources
optimization for Dicke state preparation on the current noisy quantum devices.

Scenario

na

nc

ns

Ansatz

np

nsearchspace

I

10

1

4

|D410 ⟩

30

210

II

25

5

5

|D15 ⟩⊗ 5

20

3125

9

|D25 ⟩⊗ 2 |D15 ⟩⊗2 |D35 ⟩

31

25000

III

25

5

Table 2. The table shows the different scenarios we use to evaluate the performance of parametrized Dicke
state in the context of multiclass portfolio optimization. Where na represents the number of assets (that define
the number of qubits used in the scenario), nc number of classes, ns amount of select assets, np number of
parameters of Dicke state ansatz. |Dkn ⟩ is a superposition of all states with n qubits and k qubits equal |1⟩. Each
state represents a class where n is the total number of assets available to choose and k is the number of assets
we must select from it. The parameter θ⃗ was omitted in the state for better visualization. The last column shows
the actual size of search space for each scenario.

⃗ represents amplitude probability as a function of the parameters θ⃗. A similar approach was presented
where ai (θ)
by43, which focused solely on the preparation of a single Dicke state, thus mimicking portfolio optimization
without diversification constraints. In this paper, we use the implementation given by41, creating a non-uniform
Dicke state parameterizing the circuit implementation and incorporating the multiclass optimization by
including multiple Dicke states representing the multiple classes. Each Dicke state represents a class with a set
of products (number of qubits n) and will encode the constraints of the exact number of assets which will be
selected by class (parameter k) (see Fig.3a). The equation below dictates the number of parameters np of a Dicke
state ansatz
np =

m
∑
i=1

ki ni −

ki (ki + 1)
(6)
2

where ki is the number of states |1⟩, that corresponds to the Hamming weight associated with the budget
constraint. Equation (6) was derived empirically, for further details see Suplementary Material.
For m = 1, we have a unique Dicke state ansatz with n qubits and Hamming weight k, but m > 1 implies a
tensor product of different Dicke states. The summation is over the number of classes represented by the number
of Dicke states in the tensor product of the initialization.

Results

We addressed the portfolio optimization problem using the SCIP optimizer, treating its solution as the benchmark
reference (see Supplementary Material). The running time was determined by averaging the results from 100
executions. This average running time served as the basis for comparing the performance of classical methods
with hybrid VQE routines. However, it is important to note that we did not expect that the VQE approach would
outperform the classical methods in terms of speed.
The experiments were performed in three different scenarios as described in Table 2. For Scenario I, we ran
the VQE algorithm for 20 different ansatzes (Dicke state, Ry , and 18 variations of Two Local). For Scenarios
II and III only the Dicke state was used. For all scenarios, we tested 5 classical optimizers with 1000 iterations,
100 randomly sampled initial points (ansatz parameters), 4096 shots per circuit, totalizing more than 60 billion
executions (≈ nansatz × noptimizers × nexecutions × nshots × niterations ). More details of the variations of
the two-local ansatz used here can be found in Supplementary Material. All data used in this work are publicly
available and were obtained using the Yahoo Finance API.
Scientific Reports |

(2026) 16:6208

| https://doi.org/10.1038/s41598-026-36333-4

5

www.nature.com/scientificreports/
We employ Scenario I to identify the most effective ansatz for multiclass portfolio optimization. Among
the 500 trials conducted per ansatz, the parametrized Dicke state emerged as the best performing approach,
regardless of the classical optimizer (see Fig.4). For this initial evaluation, we only verified that the optimal
solution consistently emerged as the state with the highest probability without considering the magnitude of
this probability. It is evident that the Dicke state has been the most effective ansatz so far. Because of that, we
only employ it for the other scenarios to assess its performance and evaluate the impact of classical optimizers.
From a theoretical standpoint, the improved optimization performance of the Dicke-state ansatz arises from
its structural design, which confines the variational search to the feasible subspace defined by the diversification
constraints. By preparing the quantum
∏ state as a tensor product of Dicke states, the search space is reduced
from the full 2n Hilbert space to i Cni ,ki a substantial reduction in realistic scenarios where ki ≪ ni . This
restriction removes infeasible configurations, concentrates the optimization on meaningful portfolio states, and
preserves the symmetry of fixed Hamming weight. Consequently, the optimizer operates on a smoother energy
landscape, improving convergence stability and accuracy relative to more general ansatzes.
Another challenge in the evaluation of hybrid algorithms is to measure the effect of the classical optimizer on
the solution. As mentioned before, we tested five different optimizers: CMA-ES56, COBYLA57, Random Sampler,
SPSA58 and QNSPSA59. The evaluation takes into account three different metrics: the approximation ratio, the
frequency with which the right answer appears in the 100 trials per optimizer, and the quality of the quantum
output for each trial (the probability of measuring the target state). The approximation ratio is defined as23,60–62
ar =

(

Emax − ⟨H⟩ψ(θ⃗∗ )
(Emax − E0 )

)

,(7)

where ⟨H⟩ψ(θ⃗∗ ) is the expected value of the problem Hamiltonian computed with the ansatz and the set of
parameters obtained at the end of optimization. E0 is the ground-state energy associated with the optimal
solution that was calculated by computing the lowest eigenvalue for the problem Hamiltonian. Emax represents
the highest Hamiltonian eigenvalue. The metric above measures how close or distant the solution is from the
optimal. For example, an approximation ratio equal to 1 means that the solution is equal to the optimal one.
When comparing the results of the experiments in different scenarios, it is clear that CMA-ES emerged as
the optimizer that exhibited the highest frequency of finding the target state with the highest probability among

Ds
Ry
TL1
TL2
TL3
TL4
TL5
TL6
TL7
TL8
TL9
TL10
TL11
TL12
TL13
TL14
TL15
TL16
TL17
TL18

Ds
Ry
TL1
TL2
TL3
TL4
TL5
TL6
TL7
TL8
TL9
TL10
TL11
TL12
TL13
TL14
TL15
TL16
TL17
TL18

0

Err
0.02
0.6
0.75
0.68
1.37
2.78
0.69
1.28
2.0
0.5
1.05
1.3
1.18
1.51
0.63
1.14
1.21
0.69
1.18
1.48

100


0.03
0.61
0.92
0.8
1.76
2.4
0.82
1.67
2.18
0.45
1.06
1.23
1.5
1.83
0.65
1.49
1.59
0.81
1.48
1.82

200

Fig. 4. Ansatz comparison results for Scenario I taking into account all optimizers. The histogram shows the
number of trials where each ansatz found the optimal solution as its most common output. Notably, out of the
20 ansatzes tested, the Dicke state demonstrated the best performance, independently of the classical optimizer.
Out of 500 runs, in more than 50%, the VQE-Dicke state found the optimal result as the one with the highest
probability. The inside table shows the absolute error (||Err||) and the standard deviation (σ) between the
expected value of the quantum solution and the target. Again, the VQE-Dicke state presented the best metrics.

Scientific Reports |

(2026) 16:6208

| https://doi.org/10.1038/s41598-026-36333-4

6

www.nature.com/scientificreports/
all the 100 trials (see Table 3). In terms of time, COBYLA was the fastest optimizer, followed by CMA-ES in
second place. QNSPSA, the second solver that demonstrated good performance in finding the global optimal,
was surprisingly costly in terms of time, resulting in the worst performance among all optimizers. This result
indicates the potential of using CMA-ES as a good choice for hybrid algorithms. More explorations must be
done, but, at least for these experiments, CMA-ES surpasses the other optimizers.
It is clear that the optimizers guide the distribution toward the right direction, this fact can be seen in Fig.5,
where we compare the approximation ratio distribution before and after the parameter optimization process. Note
that the values of the initial distribution are below ar = 0.9, but after optimization we can see a displacement to
the right, which means that optimization succeeded in obtaining a set of parameters which generates a quantum
state whose state distribution has a high probability of measuring a state with a high approximation ratio.
Note that even when the probability of measuring the target state is low (see probability of state of measure 0
in Fig. 6), ar ≳ 0.9 for most optimizers, see Fig. 5 (colored bars). This phenomenon is linked to Eq.(7), which,
from a quantum perspective, acts as a weighted average representing the expected value of the Hamiltonian.
This implies that the approximation ratio of the quantum output distribution is essentially a weighted sum of
the approximation ratios of individual states. As a result, when the system moves toward the optimal region
post-optimization, where most states in the distribution have lower energy, the approximation ratio generally
becomes higher.
The clarity of the results is enhanced upon examining Fig.6. After conducting 100 experimental runs, we
aggregated the data and analyzed the frequency of each bit string, arranging them in ascending order of energy.
For improved visualization, we retained only the top five bit strings, consolidating all others into a rest category.
It is evident that CMA-ES consistently exhibits the highest probability of sampling the optimal solution in
all scenarios and dominates the top five regions. QNSPSA, COBYLA, and SPSA show comparable behaviors,
ranking second. Although they are capable of achieving the optimal solution, in instances where they do not,
they frequently yield solutions that are close to the global optimum.
Despite the high performance of CMA-ES in all scenarios, the quality of the quantum output is not
consistent. To investigate why p(x∗ ) is widely distributed, we evaluated the impact of the number of iterations in
p(x∗ ). As can be seen in Fig.7 as the number of iterations increases, the average probability of finding the target
state also increases, achieving a more accurate result. The experiment was performed in scenario I and with
ninterations ≳ 1500 the solution reaches the optimal region (p(x∗ ) ≥ 0.95). The result strongly suggests that,
in addition to the capacity to find the target state, it is possible to improve the quality of the quantum output by
increasing the number of iterations.
It is important to mention that recent studies61,63,64 suggest the potential quantum advantage of variational
algorithms like VQE and QAOA arises when the number of function evaluations (ncalls ≡ nshots × niterations )
remains smaller than the size of the effective search space (nsearch ∏
space ). By applying the Dicke state ansatz in
n
our problem, we significantly reduce the search space from 2n by i c Cni ,ki ∼ O(nk ). However, for the set
of experiments provided here, ncalls ∼ 4.096.000 ≫ nsearch space as can be seen in the last column of Table 2.

Scenario

I

II

III

Optimizer

All

p(x∗ ) ≥ 0.95

Time (s)

CMA-ES

88

25

COBYLA

44

32

82.8 ± 0.6

QNSPSA

74

65

RS

27

0

SPSA

49

44

CMA-ES

98

97

COBYLA

49

35

QNSPSA

76

73

RS

6

0

SPSA

40

25

CMA-ES

70

1

COBYLA

21

5

QNSPSA

30

27

RS

0

0

SPSA

12

4

29 ± 4

601 ± 3

82.5 ± 0.7

154.5 ± 0.8
181 ± 4
43 ± 6

981 ± 9
202 ± 1
302 ± 6

335 ± 12
119 ± 21

1541 ± 20
376 ± 3

467 ± 17

Table 3. A summary of experiments results for each scenario considering only Dicke state ansatz. The column
All represents the frequency of the optimal global solution (x∗ ), among 100 experiments, counted if it appears
with highest probability. p(x∗ ) ≥ 0.95 filter only the quantum outputs which the probability of the optimal
state is greater than 0.95. As can be seen, by applying this filter the frequency in CMAES drastically reduces in
some scenarios (numbers indicated in Bold and Italic). The last column represents the average running time
and the standard deviation of each optimizer.

Scientific Reports |

(2026) 16:6208

| https://doi.org/10.1038/s41598-026-36333-4

7

www.nature.com/scientificreports/

(a) Scenario I (b) Scenario II (c) Scenario III

CMAES

100

COBYLA

0
100

SPSA

0
100

QNSPSA

0
100

RS

0
100

0

0.0

0.5 0.9 0.0

0.5 0.9 0.0
ar

0.5 0.9

Fig. 5. Plots (a), (b), and (c) compare the approximation ratio (ar ) distributions before (gray) and after
(colored) optimization for each scenario (columns) and optimizers (rows). The gray represent ar distributions
with the initial parameters, while the colored ones reflect optimized parameters, based on 100 experiments
per optimizer. A vertical black dashed line marks ar = 0.9. Across all optimizers and scenarios, the initial
distributions shift toward ar ≥ 0.9, indicating the positive impact of the hybrid approach and optimizers. In
Scenario I (blue) all the optimizers guide the solution to the optimal region.

Conclusion

In this work, we introduce an innovative approach to exploring multiclass portfolio optimization through a
parameterized version of multiple Dicke states within a VQE framework. We analyze three distinct scenarios
by varying the complexity of the search space and the number of parameters in the parameterized circuit. Our
comparative evaluation indicates that Dicke states outperform other ansatzes, making them a suitable choice for
this type of problem.
Furthermore, we examine the impact of various optimizers within this hybrid algorithm. Our results indicate
that CMA-ES outperforms other optimizers in both execution time and convergence to the optimal solution.
However, achieving higher-quality quantum outputs requires a larger number of iterations and tuning of the
optimizer parameters. Additionally, all optimizers tested here appear to find parameters that guide the quantum
distribution output toward regions close to the ground state. The Random Sampler was shown to be the worst
optimizer.
Another intriguing aspect we began to evaluate is the relationship between state fidelity and optimal
parameters, as discussed in the Supplementary Material. In future research, our aim is to address the open
questions highlighted here and to further investigate the use of the QAOA with Dicke states for multiclass
portfolio optimization. This will include exploring different mixer Hamiltonians.
All our results were obtained through simulations, as our primary objective was to gain a deeper understanding
of the algorithm’s potential for solving realistic portfolio optimization problems, encoding the diversification
constraints in the quantum state preparation.
Although the proposed Dicke-state framework achieved promising results, further investigation is needed
to evaluate its scalability and practical benefits in large-scale, real-world portfolio optimization. The potential
advantage of variational algorithms emerges when the number of function evaluations remains smaller than
the effective search space, motivating future studies combining the Dicke ansatz with CMA-ES and Conditional
Value at Risk (CVaR) to explore possible regimes of quantum advantage. While current simulations assume allScientific Reports |

(2026) 16:6208

| https://doi.org/10.1038/s41598-026-36333-4

8

www.nature.com/scientificreports/

(a) Scenario I (b) Scenario II (c) Scenario III
CMAES

1.0

0
1
2
3
res4t

0
2
5
7
1
res0t

0.0

0
1
2
4
res6t

0.5

COBYLA

1.0

0
2
3
11
2
res2t

0
2
7
15
3
res7t

SPSA

1.0

0
2
3
5
1
res1t

0.0

0
2
7
1
3475
rest

0.5

0
1
2
13
2
res3t

Probability

0.0

0
1
2
3
1
res3t

0.5

QNSPSA

1.0

0
1
2
3
1
res3t

0
1
2
7
1
res4t

0
1
2
3
1
res1t

2
7
15
29
3
res7t

48
56
10
1729
28
res9t

0.0

0
1
2
3
res4t

0.5

RS

1.0
0.5
0.0

Fig. 6. Plots (a), (b), and (c) display the sampling probabilities of each bit string, ordered from lower to higher
energy, aggregated over 100 runs. The target state is positioned at 0 based on this energy ordering. We present
the five best results from each optimizer across all scenarios, with the tick rest aggregating outcomes outside
the top five. Overall, CMA-ES and QNSPSA achieved the best performance, as they concentrate probability
distribution in the optimal region and assign the highest probability to the ground state.

to-all connectivity, the approach is hardware-agnostic and compatible with realistic 2D or sparse architectures,
offering structural efficiency by reducing the feasible subspace and eliminating penalty terms. Preliminary
hardware tests on IBM quantum devices can be seen in the Supplementary Material and confirm the expected
sensitivity to noise and circuit depth, reinforcing the focus on noiseless simulations to isolate algorithmic
behavior. Finally, quantum-optimized portfolios showed consistency with classical allocations in risk–return
balance and diversification quality, encouraging future work on explicit financial performance metrics.
Future research is also needed to test these findings on current quantum hardware, comparing the
effectiveness of Zero-Noise Extrapolation (ZNE), Probabilistic Error cancellation (PEC) and CVaR in mitigating
errors during the calculation of expectation values. Our goal was not to provide definitive proof of this impact,
but rather to test the viability of utilizing VQE in a more realistic financial scenario and open a new direction of
exploration that is encoding optimization constraints in state preparation. We believe that our findings represent
a significant step towards this objective.

Scientific Reports |

(2026) 16:6208

| https://doi.org/10.1038/s41598-026-36333-4

9

www.nature.com/scientificreports/

1.0

p(x*)

0.8
0.6
0.4
0.2
0.0

p = 0.5
p = 0.95

0

500

1000

1500

2000

2500

niterations
Fig. 7. The result expresses how the probability to achieve the target state evolve as we increase the number
of iterations in CMA-ES optimizer in scenario I. Each point in the curve represents 100 executions of VQEDicke with 4096 shots for a fixed number of iterations of CMA-ES. Note that each execution initializes a
random set of parameters for VQE. After each execution we extracted the probability of measuring the target
state and compute the average among all 100 runs. As the number of iterations increases, independently of
the parameters initialization, p(x∗ ) also increases. When niterations ≳ 1500, the points fluctuate around 0.95,
indicating convergence to the region where p(x∗ ) ≳ 0.95. These residual fluctuations arise from stochastic
optimizer initializations and finite-shot sampling, and occasional dips below 0.95 are therefore expected and
do not compromise the convergence trend.

Data availability

The datasets generated and/or analyzed during the current study are available in the Yahoo Finance and can be
downloaded using the following python library: yfinance. The period of the datasets considered in this work are:
2023-12-18 until 2024 12-16 and 2024-01-02 until 2025-01-02.

Code availability

The underlying code for this study is not publicly available but may be made available to qualified researchers
on reasonable request from the corresponding author.
Received: 17 September 2025; Accepted: 12 January 2026

References

1. McArdle, S., Endo, S., Aspuru-Guzik, A., Benjamin, S. C. & Yuan, X. Quantum computational chemistry. Rev. Mod. Phys. 92,
015003 (2020).
2. Bauer, B., Bravyi, S., Motta, M. & Chan, G.K.-L. Quantum algorithms for quantum chemistry and quantum materials science.
Chem. Rev. 120, 12685 (2020).
3. von Burg, V. et al. Quantum computing enhanced computational catalysis. Phys. Rev. Res. 3, 033055 (2021).
4. Biamonte, J. et al. Quantum machine learning. Nature 549, 195 (2017).
5. Liu, N. & Rebentrost, P. Quantum machine learning for quantum anomaly detection. Phys. Rev. A 97, 042315 (2018).
6. Schuld, M. & Killoran, N. Quantum machine learning in feature hilbert spaces. Phys. Rev. Lett. 122, 040504 (2019).
7. Cong, I., Choi, S. & Lukin, M. D. Quantum convolutional neural networks. Nat. Phys. 15, 1273 (2019).
8. Cerezo, M., Verdon, G., Huang, H.-Y., Cincio, L. & Coles, P. J. Challenges and opportunities in quantum machine learning. Nat.
Comput. Sci. 2, 567 (2022).
9. Jerbi, S., et al. Quantum machine learning beyond kernel methods. Nat. Commun. 14, 517 (2023)
10. Egger, D. J. et al. Quantum computing for finance: State-of-the-art and future prospects. IEEE Trans. Quantum Eng. 1, 1 (2020).
11. Ramos-Calderer, S. et al. Quantum unary approach to option pricing. Phys. Rev. A 103, 032414 (2021).
12. Mugel, S. et al. Dynamic portfolio optimization with real datasets using quantum processors and quantum-inspired tensor
networks. Phys. Rev. Res. 4, 013006 (2022).
13. Buonaiuto, G., Gargiulo, F., De Pietro, G., Esposito, M. & Pota, M. Best practices for portfolio optimization by quantum computing,
experimented on real quantum devices. Sci. Rep. 13, 19434 (2023).
14. Herman, D. et al. Quantum computing for finance. Nat. Rev. Phys. 5, 450 (2023).
15. Wilkens, S. & Moorhouse, J. Quantum computing for financial risk measurement. Quantum Inf. Process. 22, 51 (2023).
16. Naik, A. S., Yeniaras, E., Hellstern, G., Prasad, G. & Vishwakarma, S. K. L. P. From portfolio optimization to quantum blockchain
and security: A systematic review of quantum computing in finance. Financ. Innov. 11, 1 (2025).
17. Thakkar, S. et al. Improved financial forecasting via quantum machine learning. Quantum Mach. Intell. 6, 27 (2024).
18. Jarret, M. & Wan, K. Improved quantum backtracking algorithms using effective resistance estimates. Phys. Rev. A 97, 022337
(2018).
19. Campbell, E., Khurana, A. & Montanaro, A. Applying quantum algorithms to constraint satisfaction problems. Quantum 3, 167
(2019).
20. Montanaro, A. Quantum speedup of branch-and-bound algorithms. Phys. Rev. Res. 2, 013056 (2020).
21. Egger, D. J., Mareček, J. & Woerner, S. Warm-starting quantum optimization. Quantum 5, 479 (2021).
22. Magann, A. B., Rudinger, K. M., Grace, M. D. & Sarovar, M. Feedback-based quantum optimization. Phys. Rev. Lett. 129, 250502
(2022).

Scientific Reports |

(2026) 16:6208

| https://doi.org/10.1038/s41598-026-36333-4

10

www.nature.com/scientificreports/
23. Abbas, A., Ambainis, A., Augustino, B. et al. Challenges and opportunities in quantum optimization. Nat. Rev. Phys. 6, 718–735
(2024).
24. Finžgar, J. R., Kerschbaumer, A., Schuetz, M. J., Mendl, C. B. & Katzgraber, H. G. Quantum-informed recursive optimization
algorithms. PRX Quantum 5, 020327 (2024).
25. Jünger, M., Reinelt, G. & Rinaldi, G. The traveling salesman problem. Handbooks in operations research and management science 7,
225 (1995).
26. Toth, P., & Vigo, D. The vehicle routing problem (SIAM, 2002).
27. Martello, S., Pisinger, D. & Vigo, D. The three-dimensional bin packing problem. Oper. Res. 48, 256 (2000).
28. Mansini, R., ,odzimierz Ogryczak, W., Speranza, M. G., & E. T. A. of European Operational Research Societies, Linear and mixed
integer programming for portfolio optimization, Vol. 21 (Springer, 2015).
29. Jünger, M., et al. 50 Years of integer programming 1958-2008: From the early years to the state-of-the-art ( Springer Science &
Business Media, 2009)
30. Gonzalez, T. F. Handbook of approximation algorithms and metaheuristics ( Chapman and Hall/CRC, 2007).
31. Smith, K. A. Neural networks for combinatorial optimization: a review of more than a decade of research. INFORMS J. Comput.
11, 15 (1999).
32. Prates, M., Avelar, P. H., Lemos, H., Lamb, L. C. & Vardi, M. Y. Learning to solve np-complete problems: A graph neural network
for decision tsp. Proc. AAAI Conf. Artif. Intell. 33, 4731–4738 (2019).
33. Markowitz, H. M. Portfolio selection. J. Finance 7, 71 (1952).
34. Cerezo, M. et al. Variational quantum algorithms. Nat. Rev. Phys. 3, 625 (2021).
35. Preskill, J. Quantum computing in the nisq era and beyond. Quantum 2, 79 (2018).
36. Peruzzo, A., McClean, J., Shadbolt, P. et al. A variational eigenvalue solver on a photonic quantum processor. Nat. Commun. 5, 4213
(2014).
37. Farhi, E., Goldstone, J., & Gutmann, S. A quantum approximate optimization algorithm, arXiv preprint arXiv:1411.4028 (2014)
38. Griffiths, D. J., & Schroeter, D. F. Introduction to quantum mechanics (Cambridge university press, 2019).
39. Glover, F., Kochenberger, G., & Du, Y. Quantum bridge analytics i: a tutorial on formulating and using qubo models. 4or 17, 335
(2019).
40. Lucas, A. Ising formulations of many np problems. Front. Phys. 2, 5 (2014).
41. Mukherjee, C. S., Maitra, S., Gaurav, V. & Roy, D. Preparing dicke states on a quantum computer. IEEE Trans. Quantum Eng. 1, 1
(2020).
42. Bärtschi, A., & Eidenbenz, S. Short-depth circuits for dicke state preparation, in 2022 IEEE International Conference on Quantum
Computing and Engineering (QCE) 87–96 ( IEEE, 2022).
43. Wang, S., et al., Variational quantum eigensolver with linear depth problem-inspired ansatz for solving portfolio optimization in
finance, arXiv preprint arXiv:2403.04296 (2024)
44. Garraway, B. M. The dicke model in quantum optics: Dicke model revisited. Philos. Trans. R. Soc. A: Math. Phys. Eng. Sci. 369, 1137
(2011).
45. Bärtschi, A. & Eidenbenz, S. Deterministic preparation of dicke states. In: International Symposium on Fundamentals of
Computation Theory 126–139 (Springer, 2019).
46. Cook, J., Eidenbenz, S. & Bärtschi, A. The quantum alternating operator ansatz on maximum k-vertex cover. In: 2020 IEEE
International Conference on Quantum Computing and Engineering (QCE) 83–92 (IEEE, 2020).
47. Bärtschi, A. & Eidenbenz, S. Grover mixers for qaoa: Shifting complexity from mixer design to state preparation. In: 2020 IEEE
International Conference on Quantum Computing and Engineering (QCE) pp. 72–82 (IEEE, 2020).
48. Brandhofer, S. et al. Benchmarking the performance of portfolio optimization with qaoa. Quantum Inf. Process. 22, 25 (2022).
49. He, Z. et al. Alignment between initial state and mixer improves qaoa performance for constrained optimization. npj Quantum Inf.
9, 121 (2023).
50. Niroula, P. et al. Constrained quantum optimization for extractive summarization on a trapped-ion quantum computer. Sci. Rep.
12, 17171 (2022).
51. Özdemir, S. K., Shimamura, J. & Imoto, N. A necessary and sufficient condition to play games in quantum mechanical settings.
New J. Phys. 9, 43 (2007).
52. Prevedel, R. et al. Experimental realization of dicke states of up to six qubits for multiparty quantum networking. Phys. Rev. Lett.
103, 020503 (2009).
53. Tóth, G. Multipartite entanglement and high-precision metrology, Physical Review A—Atomic. Mol. Opt. Phys. 85, 022322 (2012).
54. Ouyang, Y. Permutation-invariant quantum coding for quantum deletion channels. In: 2021 IEEE International Symposium on
Information Theory (ISIT) 1499–1503 (IEEE, 2021).
55. Ouyang, Y. Quantum storage in quantum ferromagnets. Phys. Rev. B 103, 144417 (2021).
56. Grayver, A. V. & Kuvshinov, A. V. Exploring equivalence domain in nonlinear inverse problems using covariance matrix adaption
evolution strategy (cmaes) and random sampling. Geophys. J. Int. 205, 971 (2016).
57. Powell, M. J. A direct search optimization method that models the objective and constraint functions by linear interpolation (Springer,
1994)
58. Spall, J. C. An overview of the simultaneous perturbation method for efficient optimization. Johns Hopkins APL Tech. Dig. 19, 482
(1998).
59. Gacon, J., Zoufal, C., Carleo, G. & Woerner, S. Simultaneous perturbation stochastic approximation of the quantum fisher
information. Quantum 5, 567 (2021).
60. Shaydulin, R. & Alexeev, Y. Evaluating quantum approximate optimization algorithm: A case study, in 2019 tenth international
green and sustainable computing conference (IGSC) 1–6 (IEEE, 2019).
61. Zhou, L., Wang, S.-T., Choi, S., Pichler, H. & Lukin, M. D. Quantum approximate optimization algorithm: Performance,
mechanism, and implementation on near-term devices. Phys. Rev. X 10, 021067 (2020).
62. Herrman, R., Lotshaw, P. C., Ostrowski, J., Humble, T. S. & Siopsis, G. Multi-angle quantum approximate optimization algorithm.
Sci. Rep. 12, 6781 (2022).
63. Scriva, G., Astrakhantsev, N., Pilati, S. & Mazzola, G. Challenges of variational quantum optimization with measurement shot
noise. Phys. Rev. A 109, 032408 (2024).
64. Maurizio, A. & Mazzola, G. Quantum computing for genomics: conceptual challenges and practical perspectives. PRX Life 3.4,
047001 (2025).

Disclaimer

Any opinions, findings, conclusions, or recommendations expressed in this material are those of the authors
and do not necessarily reflect the views of Itaú-Unibanco and Institute of Science and Technology of Itaú. This
document is not and does not constitute or intend to constitute investment advice or any investment service. It
is not and should not be deemed to be an offer to purchase or sell, or a solicitation of an offer to purchase or sell,
or a recommendation to purchase or sell any securities or other financial instruments. In addition, all data used
in this study comply with the Brazilian General Data Protection Law.
Scientific Reports |

(2026) 16:6208

| https://doi.org/10.1038/s41598-026-36333-4

11

www.nature.com/scientificreports/

Author contributions

SB and JV conceived the project. SB, JV and GM developed the theoretical framework. JV, GM and VB performed the experiment and collected the data. JV and SB analyzed experimental data and prepared figures. All
authors contributed to writing the manuscript.

Funding

This research did not receive funding.

Declarations
Competing interests

The authors declare no competing interests.

Additional information

Supplementary Information The online version contains supplementary material available at ​h​t​t​p​s​:​/​/​d​oi​ ​.​o​r​g​/​1​
0​.​10​ ​3​8​/​s​4​1​5​9​8-​ ​0​2​6​-​3​6​3​3​3​-​4​​​​.​​
Correspondence and requests for materials should be addressed to J.V.S.S. or S.B.
Reprints and permissions information is available at www.nature.com/reprints.
Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and
institutional affiliations.
Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which
permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give
appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and
indicate if changes were made. The images or other third party material in this article are included in the article’s
Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included
in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or
exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy
of this licence, visit http://creativecommons.org/licenses/by/4.0/.
© The Author(s) 2026

Scientific Reports |

(2026) 16:6208

| https://doi.org/10.1038/s41598-026-36333-4

12

