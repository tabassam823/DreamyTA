Quantum Approximate Optimization
Algorithm for Portfolio Selection:
A Comparative Study with Classical
Markowitz Optimization
Gabriel Padilla
Universidad de los Andes
November 19, 2025
Abstract
Portfolio optimization is a fundamental problem in quantitative finance and is traditionally addressed using the classical Markowitz mean–variance model. Although
this approach has proven effective, the inclusion of discrete constraints such as cardinality limits or binary asset selection introduces significant computational complexity, motivating the exploration of QUBO-based formulations and variational
quantum algorithms.
In this work, we formulate a small-scale portfolio selection instance as a QUBO
model, which is mapped to an Ising Hamiltonian and solved using the Quantum Approximate Optimization Algorithm (QAOA). We implement QAOA on a quantum
simulator and compare its performance with a classical solver for the same QUBO
problem. Markowitz is used only as a conceptual framework that motivates the
problem formulation, but not as a numerical baseline, since the classical continuous
model is not directly comparable with the discrete version used here.
The main contribution of this study is a detailed educational explanation of
QAOA, its components, the circuit structure, and the variational scheme, together
with an applied demonstration in a financial context. Rather than claiming quantum advantage, the focus is on understanding the algorithm’s behavior in realistic
small-scale instances. Finally, we discuss whether, as quantum technology advances,
QAOA could provide practical benefits in portfolio optimization or whether classical
methods will remain sufficient in practice.

1

1

Introduction

1.1

Context and Motivation

Portfolio optimization plays a fundamental role in traditional and quantitative finance,
providing a structured way to allocate capital, balance risk tolerance against expected
return, and build diversified investment strategies. The Markowitz mean–variance model
currently dominates the classical formulation due to its analytical clarity and practical relevance. However, when additional constraints such as cardinality limits, discrete
selection rules, or budget requirements are introduced, the problem becomes combinatorial and, in many cases, NP-hard. These discrete extensions challenge the scalability
of classical methods and motivate the search for alternatives within new computational
paradigms.
Recent advances in quantum computing have sparked significant interest in quantum
algorithms for combinatorial optimization problems. In particular, hybrid variational
algorithms, such as the Variational Quantum Eigensolver (VQE) and the Quantum Approximate Optimization Algorithm (QAOA), have emerged as promising candidates for
near-term quantum devices. QAOA, as proposed by Farhi, Goldstone, and Gutmann
in A Quantum Approximate Optimization Algorithm (MIT, 2014; arXiv:1411.4028), is
specifically designed to approximate solutions to discrete optimization problems and is
naturally expressed in terms of QUBO formulations and Ising Hamiltonians. This makes
it conceptually aligned with portfolio optimization when modeled as a binary problem in
which each variable indicates whether an asset is included or excluded from the portfolio.
Given the combinatorial structure of asset selection under constraints and the possibility of mapping QUBO formulations to quantum Hamiltonians, QAOA provides an
attractive framework for exploring quantum approaches to financial optimization. Although current quantum hardware is far from offering a practical advantage, small-scale
simulations allow the internal workings of the algorithm to be studied and its potential
future impact on financial applications to be assessed.

1.2

Objective and Scope of this Work

This work studies a simplified version of the portfolio optimization problem, in which asset
selection is represented by a binary vector. Each decision variable indicates whether an
asset is included in the portfolio, subject to basic constraints such as cardinality limits or
a simplified budget rule. This formulation naturally leads to a QUBO model that can be
directly mapped to an Ising Hamiltonian, enabling its implementation through QAOA.
The first objective of this study is to provide a clear and detailed exposition of the
Quantum Approximate Optimization Algorithm, covering the construction of the cost
Hamiltonian, the mixer Hamiltonian, the circuit architecture, and the hybrid quantum–classical optimization loop. This educational presentation constitutes a central
contribution of the work, in line with the academic interest in understanding QAOA
beyond its current practical performance.
2

Secondly, we develop a small-scale portfolio optimization instance and solve it using
QAOA on a quantum simulator. We then compare the resulting bitstrings and solution quality with a classical solver applied to the same QUBO model. The reference to
Markowitz is used only as historical and conceptual motivation in portfolio theory, but not
as a numerical baseline, since the classical continuous model is not directly comparable
with the discrete formulation used in this work. The comparison seeks to contextualize
the behavior of QAOA against classical methods capable of solving the same discrete
problem.
Finally, we pose an open question: as both quantum hardware and variational techniques evolve, is it reasonable to expect QAOA to offer practical benefits in portfolio
optimization, or will classical methods continue to dominate due to their maturity, stability, and efficiency? This reflection points to broader implications of using quantum
algorithms in financial decision-making in real-world settings.

2

Background

2.1

Classical Portfolio Optimization (Markowitz)

The classical portfolio theory proposed by Markowitz establishes a quantitative framework for allocating capital among assets, seeking a balance between expected return and
risk. Let w ∈ Rn be the portfolio weight vector, µ ∈ Rn the vector of expected returns,
and Σ ∈ Rn×n the risk covariance matrix. The typical problem consists of maximizing a
risk–return trade-off, for example:
max µ⊤ w − λ w⊤ Σw,
w

where λ > 0 controls risk aversion.
In the classical approach, the weights wi are continuous and represent fractions of
capital invested. However, when realistic constraints such as cardinality limits, subset selection of assets, or binary include/exclude decisions are introduced, the problem becomes
discrete and, in general, NP-hard. These discrete variants can be naturally formulated
as QUBO problems, which connects them with quantum optimization approaches.

2.2

QUBO and Ising Formulation

In a QUBO problem, decisions are modeled by binary variables xi ∈ {0, 1} that typically
represent whether an asset is selected. The objective function takes the quadratic form:
min

x∈{0,1}n

x⊤ Qx,

where Q is a real matrix encoding individual contributions, interactions, and penalty
terms.

3

To implement this formulation on quantum hardware, the binary variables are transformed into spins using the mapping:
xi =

1 − si
,
2

si ∈ {−1, +1},

which yields an equivalent Ising model. The associated cost Hamiltonian is expressed as:
HC =

X

hi Zi +

X

i

Jij Zi Zj ,

i<j

where Zi are Pauli-Z operators and the coefficients hi , Jij originate from the matrix Q.
Minimizing the energy of this Hamiltonian is equivalent to solving the original QUBO
problem, making this representation the natural basis for variational quantum algorithms
such as QAOA.

2.3

The Quantum Approximate Optimization Algorithm (QAOA)

The Quantum Approximate Optimization Algorithm (QAOA), introduced by Farhi et
al., is a hybrid quantum–classical algorithm designed to approximate solutions of combinatorial problems represented as Ising Hamiltonians. For a cost Hamiltonian HC , QAOA
constructs a parameterized quantum circuit based on two core elements:
• Cost Hamiltonian HC , which encodes the problem.
P
• Mixer Hamiltonian HM = i Xi , where Xi are Pauli-X operators.
The algorithm starts from the uniform superposition state:
|ψ0 ⟩ = |+⟩⊗n ,
and applies p alternating layers of unitaries derived from both Hamiltonians. The resulting state has the form:
|ψ(γ, β)⟩ = UM (βp ) UC (γp ) · · · UM (β1 ) UC (γ1 ) |ψ0 ⟩,
where
UC (γ) = e−iγHC ,

UM (β) = e−iβHM .

The parameter vector (γ, β) is optimized through a hybrid loop:
1. A classical optimizer proposes initial values for (γ, β).
2. The QAOA circuit is executed on a simulator or quantum device.
3. The expectation value ⟨HC ⟩ is measured.
4. The optimizer updates the parameters to reduce the Hamiltonian energy.
4

Physically, QAOA alternates evolution under the problem Hamiltonian (which drives
the state toward low-energy configurations) and the mixer Hamiltonian (which promotes
exploration of the solution space). For larger depth p, the algorithm can better approximate the optimal solution, although in real hardware this increases sensitivity to noise.
QAOA has been canonically applied to problems such as Max-Cut and other standard
QUBO problems, making it a natural candidate for discrete portfolio optimization formulated as an Ising Hamiltonian. In this work, QAOA is used both as an applied financial
demonstration and as a pedagogical tool to understand variational quantum algorithms.

3

QAOA Applied to Portfolio Optimization

3.1

Problem Instance and Encoding

For this study, we consider a small instance of the discrete portfolio optimization problem
consisting of n = 6 assets. The expected returns µi and covariance matrix Σij were
generated synthetically to capture realistic correlations between assets, while maintaining
a manageable size that allows efficient simulation of QAOA.
Each asset is represented by a binary variable:
xi ∈ {0, 1},
where xi = 1 indicates that asset i is selected in the portfolio. This representation allows
writing a quadratic objective function combining return and risk:
Cost(x) = −

n
X

µi xi + λ

i=1

n X
n
X

Σij xi xj + penalties,

i=1 j=1

where the parameter λ regulates the trade-off between expected return and portfolio
variance.
The penalties included in the QUBO allow enforcing constraints such as:
• Cardinality constraint: restrict the number of selected assets.
• Budget constraints: control the maximum portfolio size.
• Penalty for violations: incorporate additional quadratic terms when a constraint
is not satisfied.
To implement this model in a quantum circuit, the binary variable is mapped to a
spin using the standard transformation:
xi =

1 − Zi
,
2

5

where Zi is the Pauli-Z operator acting on qubit i. Substituting this relation into the
cost function and expanding the quadratic terms, we obtain the cost Hamiltonian:
HC =

n
X

hi Zi +

i=1

X

Jij Zi Zj + constant,

i<j

which constitutes the direct input for the QAOA algorithm.

3.2

QAOA Circuit Design

Since each binary variable is represented by one qubit, the instance requires n = 6 qubits.
The corresponding cost Hamiltonian is:
HC =

6
X

hi Zi +

X

i=1

Jij Zi Zj .

i<j

The mixer Hamiltonian used is the standard one:
HM =

6
X

Xi ,

i=1

where Xi denotes the Pauli-X operator.
We build QAOA circuits with depths p = 1 and p = 2, each having 2p variational
parameters (γ1 , . . . , γp , β1 , . . . , βp ). The state prepared by the algorithm is:
|ψ(γ, β)⟩ = UM (βp ) UC (γp ) · · · UM (β1 ) UC (γ1 ) |+⟩⊗6 ,
with the parameterized unitaries:
UC (γ) = e−iγHC ,

UM (β) = e−iβHM .

For each set of parameters, the circuit is executed on a Qiskit simulator using 1024
shots, which yields stable measurement distributions over computational basis states.

6

Figure 1: Conceptual diagram of the QAOA circuit with depth p. The initial state is
|+⟩⊗n , followed by p alternating layers of evolution under HC and HM , and ending with
measurements in the computational basis.

3.3

Classical Reference

To evaluate the quantum performance, we use as baseline a classical QUBO solver,
capable of solving the same discrete model implemented for QAOA. This enables direct
comparison of:
• the optimal bitstring found by the classical method,
• its energy (QUBO cost),
• and the quality of the approximate solutions obtained by QAOA.
The continuous classical Markowitz model is mentioned only as theoretical motivation
in portfolio formulation. It is not used as a numerical baseline, since it operates on
continuous weights and is not comparable with the binary formulation employed in this
study.
Since the instance involves only six assets, no quantum advantage is expected. The
purpose of this section is to analyze QAOA’s ability to approximate minima of the corresponding Ising Hamiltonian and to demonstrate its use in a discrete financial optimization
problem.
7

4

Numerical Experiments and Results

In this section, we present the numerical implementation of the Quantum Approximate
Optimization Algorithm (QAOA) applied to a discrete portfolio optimization instance.
All experiments were carried out in Python using Qiskit within a custom virtual environment (“Quantum QAOA Env”). The complete code is available in the linked GitHub
repository. To document the process, we include below several screenshots of the executed
code.

4.1

Experimental Setup

The experiment considers a discrete portfolio selection problem with n = 6 assets. The
expected returns µi and the covariance matrix Σij were synthetically generated to create
a controlled and reproducible environment. Each decision variable is binary:
xi ∈ {0, 1},
indicating whether asset i is included in the portfolio.
The QUBO cost function used is:
Cost(x) = −

X

µ i xi + λ

i

X

Σij xi xj + penalty terms,

i,j

where λ controls the risk–return trade-off, and the penalty terms enforce cardinality or
portfolio size constraints. This QUBO is directly transformed into the cost Hamiltonian
HC using the standard mapping xi = (1 − Zi )/2.
The QAOA implementation includes:
• Cost Hamiltonian HC derived from the QUBO.
P
• Mixer Hamiltonian HM = i Xi .
• Initial state ψ0 = +⊗6 .
• Evaluated depths: p = 1 and p = 2.
• Classical optimizer: COBYLA, with a fixed iteration limit.
• Backend: qiskit aer simulator (statevector).

4.2

Results

For each method (QAOA with p = 1, QAOA with p = 2, and the classical exact QUBO
solution), we recorded:
• The obtained bitstring (asset selection),
8

Figure 2: Python code for constructing the QAOA circuit.
• The expected return

P

i µ i xi ,

• The variance x⊤ Σx,
• The QUBO cost value.
The results obtained in the implementation are shown in Table 1.
Method
QAOA (p = 1)
QAOA (p = 2)
Classical (exact QUBO)

Bitstring

Expected Return

Variance

QUBO Cost

101010
011100
100011

0.25
0.35
0.28

0.137
0.198
0.144

-17.740
-17.630
-17.745

Table 1: Comparison between QAOA (p = 1 and p = 2) and the exact classical QUBO
solver.

9

Figure 3: Output of the table generated in Python.

4.3

Discussion of Results

The results show that QAOA can effectively approximate the optimal solution of the
QUBO model. The exact classical solver achieves a minimum cost of −17.745, while
QAOA obtains:
• −17.740 for p = 1 (very close to optimal),
• −17.630 for p = 2 (slightly worse due to the non-convex landscape).
This behavior is characteristic of variational algorithms: increasing the circuit depth
(p = 2) expands the search space but also introduces a more complex optimization surface,
which is susceptible to local minima when using a classical optimizer.
We also observe that different bitstrings may have very similar costs, reflecting the
nearly degenerate structure of the Hamiltonian energy landscape. This is common in
discrete financial problems where many portfolios exhibit similar risk–return profiles.
Overall, the experiments indicate that:
1. QAOA can recover near-optimal QUBO solutions for small instances.
2. Larger p does not guarantee better performance due to the non-convex nature of
the variational problem.
3. A classical QUBO solver provides an appropriate and directly comparable reference.
These results reinforce the pedagogical value of applying QAOA to a realistic financial
problem and open the door to research on scalability, noise, and hybrid optimization on
next-generation quantum hardware.

5

Discussion and Outlook

5.1

Interpretation of Results

The experiments show that QAOA can effectively approximate the optimal solution of
the QUBO model for small portfolio optimization instances. In particular, for n = 6
assets, QAOA with p = 1 achieves a cost value almost identical to that obtained by
the exact classical solver, while p = 2 shows a slight degradation associated with the
non-convex nature of the optimization landscape. This suggests that, in simple discrete
10

settings, variational circuits can capture the structure of the Hamiltonian even with
limited circuit depth.
However, it is important to contextualize these results. The algorithm was executed
on a classical quantum simulator, where the computational cost grows exponentially
with the number of qubits. For this reason, although QAOA performs correctly on small
instances, classical simulation clearly shows that there is currently no practical advantage
over classical methods. The objective of this work is exploratory and pedagogical rather
than performance-driven.
Several limitations inherent to the variational approach must also be highlighted:
• Limited scalability. Modeling realistic portfolios with tens or hundreds of assets
would require a prohibitive number of qubits.
• Noisy NISQ hardware. Current quantum devices suffer from decoherence, gate
errors, and limited circuit depth, which restrict QAOA’s effectiveness even for modest values of p.
• Difficult optimization landscape. The parameter space (γ, β) contains multiple
local minima, which complicates convergence of the classical optimizer.
Together, these points indicate that QAOA is a powerful framework for understanding
how financial problems can be mapped to quantum Hamiltonians and how variational
optimization behaves, but it is still far from replacing classical methods in practical
scenarios.

5.2

Can QAOA Revolutionize Portfolio Optimization?

Looking forward, it is natural to ask whether variational algorithms like QAOA could
someday transform portfolio optimization. The answer depends on the evolution of quantum hardware and hybrid techniques.
On one hand, if quantum devices with more qubits, lower noise, and accessible circuit
depths become available, QAOA could operate on large-scale QUBO models that are
currently intractable for exact classical solvers. Moreover, the ability to naturally encode complex non-linear interactions could enable the integration of realistic constraints,
stochastic scenarios, advanced risk measures, or stress tests directly into the problem
Hamiltonian, extending beyond what is offered by mean–variance methods or mixedinteger programming.
On the other hand, classical methods are highly mature. Convex optimization techniques, Markowitz models, robust optimization, and mixed-integer solvers provide stable,
fast, and well-validated solutions in real-world applications. Even in discrete problems
with multiple constraints, classical algorithms remain highly efficient due to advances in
heuristics, decomposition, and global optimization.
In this context, the fundamental question is whether, once quantum hardware reaches
larger scale and lower noise, algorithms such as QAOA will be able to deliver a practical
11

advantage in speed, solution quality, or modeling expressiveness over these established
classical tools.
Open Question. Given the current state of quantum hardware and classical optimization techniques, an open question remains whether quantum variational algorithms like
QAOA will eventually provide a practical advantage in real-world portfolio optimization,
or whether classical methods will remain sufficient for most applications.

6

Conclusion

In this work, we explored the application of the Quantum Approximate Optimization
Algorithm (QAOA) to the discrete portfolio selection problem formulated as a QUBO
model. Through a practical implementation in Python/Qiskit, we demonstrated how to
map a financial optimization problem into an Ising Hamiltonian and how to execute the
hybrid quantum–classical variational loop to approximate its ground state.
The results show that QAOA can recover solutions close to the classical optimum for
small instances, confirming its conceptual validity as a variational technique. However,
they also highlight that current limitations in quantum hardware — restricted depth,
noise, and limited qubit counts, together with the difficulty of the parameter optimization
landscape — still prevent any practical advantage over established classical methods.
Nonetheless, the formulation of financial problems in terms of Hamiltonians opens
a promising research direction, with potential to incorporate complex constraints, nonlinear interactions, and stochastic scenarios directly into the problem structure. The
central question remains: if quantum hardware advances sufficiently, will variational algorithms like QAOA outperform classical methods for certain classes of combinatorial
financial problems?
This study contributes to this discussion by providing a pedagogical, transparent,
and reproducible demonstration of QAOA applied to finance, along with a conceptual
comparison with relevant classical approaches. It highlights both the current limits and
the future possibilities of quantum optimization in financial applications.

References
1. Farhi, E., Goldstone, J., & Gutmann, S. (2014). A Quantum Approximate Optimization Algorithm. arXiv:1411.4028. https://doi.org/10.48550/arXiv.1411.4028
2. IBM Quantum. (2023). Quantum Approximate Optimization Algorithm (QAOA)
Tutorial. IBM Quantum Documentation.
3. Markowitz, H. (1952). Portfolio selection. The Journal of Finance, 7(1), 77–91.
https://doi.org/10.2307/2975974

12

4. Schuld, M., & Petruccione, F. (2018). Supervised Learning with Quantum Computers. Springer.
5. Padilla, G. (2025). Quantum Approximate Optimization Algorithm for Portfolio
Selection – Code Repository. GitHub. https://github.com/gabrielpadilla24/
QuantumApproximateOptimizationAlgorithm

Statement on the Use of Artificial Intelligence
The entire methodological design, code implementation, QUBO formulation, Hamiltonian
construction, and execution of experiments were carried out by the author of this work.
Artificial intelligence tools (ChatGPT, OpenAI) were used solely to improve the structure
of the document, refine academic writing, and support conceptual organization. In no
case did AI generate original code or perform substantive technical development. All
technical, mathematical, and computational elements were designed and executed by the
author.

13

