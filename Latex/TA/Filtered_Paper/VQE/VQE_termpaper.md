Variational Principle 2.0: The
Variational Quantum Eigensolver
Term Paper
Authors: Anaya Dixit 23PH10020, Anu Kumari 23PH10008, Shradha
23PH10039
Date: November 28, 2025

Abstract
This term paper reviews the limitations of classical variational methods in quantum
chemistry and many-body physics, including exponential scaling of memory, runtime, and limited ansatz expressiveness. It introduces basic concepts of quantum
computing—qubits, superposition, entanglement, parameterised quantum circuits,
and measurement—as a foundation for quantum-enhanced variational algorithms.
The focus is on Variational Quantum Algorithms (VQAs), particularly VQE and
QAOA, explaining their hybrid quantum-classical workflow. Key challenges on
NISQ devices, such as the trade-off between hardware-efficient and chemistryinspired ansätze, barren plateaus, measurement overhead, adaptive ansatz design,
and gradient estimation, are discussed. Current research addressing these issues,
including adaptive and hardware-aware ansätze, error mitigation, measurement reduction, and gradient-efficient optimisation, is reviewed, giving a concise overview
of state-of-the-art methods for practical quantum simulations.

Keywords: Variational Quantum Algorithms, VQE, QAOA, NISQ, Hardware-efficient
ansätze, Chemistry-based ansätze, Barren plateaus, Measurement overhead, Adaptive
ansatz, Gradient-efficient optimisation, Quantum simulation, Hybrid quantum-classical
algorithms

1

Introduction

The variational principle is a unifying concept in physics, connecting classical mechanics,
classical field theory, quantum mechanics, and quantum field theory. Instead of writing
down equations of motion directly, we define a quantity called the action and require that
the physical motion makes this action stationary, usually a minimum. Historically, this
idea originates from Euler, Lagrange, and Hamilton in the 18th–19th centuries and was
later extended to quantum theory by Dirac and Feynman [1, 2]. The principle provides a
single framework that underlies particle dynamics, field theory, and many-body systems,
offering both conceptual unification and practical approximation methods.
1

In classical mechanics, Hamilton’s principle states that the path taken by a system
between two fixed endpoints in time renders the action
Z tf
L(q, q̇, t) dt
(1)
S[q] =
ti

stationary under small variations of the path q(t). This condition, δS = 0, leads to the
Euler–Lagrange equations:
 
d ∂L
∂L
−
= 0,
(2)
dt ∂ q̇
∂q
which are equivalent to Newton’s laws but expressed in a coordinate-independent and
more general form [3]. The variational principle naturally incorporates constraints, generalised coordinates, and symmetries, with Noether’s theorem linking symmetries of the
action to conserved quantities such as energy and momentum.
In quantum mechanics, the classical picture is generalised via Feynman’s path integral
formulation, where all paths contribute to the quantum amplitude, weighted by a phase
factor eiS/ℏ . Paths near the classical stationary path interfere constructively, while those
far from it cancel largely destructively, reproducing classical mechanics in the limit ℏ →
0 [2]. This demonstrates how the variational idea bridges classical and quantum regimes,
providing a unifying perspective on physical laws.

2

Variational Principle in Quantum Mechanics

In wave mechanics, variational ideas appear as the Rayleigh–Ritz method. For a timeindependent Hamiltonian Ĥ, the ground-state energy E0 satisfies
E0 ≤

⟨ψtrial |Ĥ|ψtrial ⟩
,
⟨ψtrial |ψtrial ⟩

(3)

for any normalised trial wavefunction ψtrial . This allows us to choose a parameterised
family of wavefunctions and minimise the energy expectation to approximate the groundstate energy and wavefunction. The method is widely applied in atomic, molecular, and
many-body systems where exact solutions of the Schrödinger equation are not feasible.
The variational principle also extends to time-dependent quantum systems through
the Dirac–Frenkel time-dependent variational principle (TDVP). A state |ψ(t)⟩ within a
restricted variational manifold satisfies
Z
d
S = dt ⟨ψ(t)|iℏ − Ĥ|ψ(t)⟩,
δS = 0,
(4)
dt
which leads to effective equations of motion for the variational parameters. Modern
variational quantum algorithms such as the Variational Quantum Eigensolver (VQE)
and related methods leverage this principle to approximate ground states and simulate
dynamics on quantum computers [4, 5].
Overall, the power of variational principles lies in their ability to unify classical and
quantum mechanics, provide systematic approximation schemes, incorporate symmetries
and conservation laws, and bridge between classical paths and quantum wavefunctions or
states. This conceptual foundation directly motivates the design of Variational Quantum
Algorithms.
2

3

Bottlenecks and Limitations of the Classical Variational Method

The classical variational method is a cornerstone of quantum chemistry and many-body
physics. It approximates ground-state energies by choosing a tractable trial wavefunction
⃗ and minimising the energy expectation value
|ψT (θ)⟩
⃗ = ⟨ψT (θ)|
⃗ H |ψT (θ)⟩
⃗ .
E(θ)

(5)

While conceptually powerful, the method becomes intractable when applied to strongly
correlated or large quantum systems [6]. Three major limitations arise: exponential memory requirements, exponentially expensive expectation-value evaluation, and restricted
ansatz expressiveness [5].

3.1

Exponential Memory Scaling

A general quantum state of N qubits requires storing 2N complex amplitudes:
|Ψ⟩ =

N −1
2X

ci |i⟩ .

(6)

i=0

This memory requirement becomes prohibitive beyond roughly 45–50 qubits on classical
hardware [7].
In quantum chemistry, the Full Configuration Interaction (FCI) method scales combinatorially:
 
M
dim(FCI) ∼
,
(7)
Ne
where M is the number of spin-orbitals and Ne the number of electrons. Such scaling
quickly renders classical methods unusable for realistic systems [6].

3.2

Exponential Runtime for Energy Evaluation

Even approximated ansätze require expensive computation of Hamiltonian expectation
values [6]. Methods such as Coupled Cluster Singles and Doubles (CCSD) scale as O(N 6 ),
while CCSD(T) scales as O(N 7 ) and fail in strongly correlated regimes (e.g., stretched
bonds, transition-metal complexes).

3.3

Limited Expressiveness of Classical Ansätze

Classical wavefunction families must remain computationally tractable, resulting in models that impose strong restrictions on entanglement:
• Hartree–Fock: no entanglement.
• CISD: truncated excitations only.
• CCSD(T): perturbative triples; fails under strong correlation.
• Tensor networks: limited by area-law entanglement.
Quantum systems, however, can exhibit volume-law entanglement, which classical ansätze
cannot efficiently represent [5].
These limitations motivate the need for quantum-enhanced variational methods.
3

4

Introduction to Quantum Computing

Quantum computing provides a fundamentally different mechanism for storing and processing information [7]. Instead of representing the wavefunction explicitly, quantum
hardware physically encodes it using the amplitudes of qubit states.

4.1

Qubits and Superposition

A qubit exists in a superposition of basis states:
|α|2 + |β|2 = 1.

|ψ⟩ = α |0⟩ + β |1⟩ ,

(8)

For N qubits, a quantum device naturally represents a state vector in a 2N -dimensional
Hilbert space.

4.2

Entanglement

Entanglement is a uniquely quantum resource in which subsystems cannot be described
independently. An example Bell state is:
|00⟩ + |11⟩
√
.
(9)
2
Entanglement enables efficient representation of correlated many-body states that are
intractable classically [5].
|Φ+ ⟩ =

4.3

Unitary Gates and Parameterised Circuits

Quantum algorithms are constructed from unitary operations. Parameterised quantum
circuits (PQCs) take the form:
⃗ = U (θ)
⃗ |0⟩⊗N .
|ψ(θ)⟩

(10)

These circuits serve as variational ansätze in VQAs [4, 8].

Figure 1: Quantum Gates [9].

4.4

Measurement and Hamiltonian Decomposition

Quantum observables are measured by decomposing the Hamiltonian into Pauli strings:
X
H=
ci P i ,
(11)
i

and estimating each term individually by repeated sampling [5].
4

4.5

Quantum Hardware (NISQ)

Current Noisy Intermediate-Scale Quantum (NISQ) devices provide:
• tens to hundreds of qubits,
• coherence times on the order of microseconds–milliseconds,
• gate errors in the range 10−3 to 10−2 .
Despite their limitations, NISQ devices can execute shallow variational circuits effectively [7].

5

Variational Quantum Algorithms (VQAs) and How
They Solve These Problems

Variational Quantum Algorithms constitute one of the most promising strategies for
utilising Noisy Intermediate-Scale Quantum (NISQ) devices. They combine quantum
state preparation with classical optimisation to solve classically intractable problems.
Among the earliest and most influential examples are the Variational Quantum Eigensolver (VQE) [4] for estimating ground-state energies of quantum systems, and the Quantum Approximate Optimisation Algorithm (QAOA) [10] for combinatorial optimisation.

5.1

The Variational Quantum Eigensolver (VQE)

VQE was introduced as a hybrid quantum-classical algorithm for computing molecular
energies and general Hamiltonian eigenvalues. The VQE has the notable property of
running on any quantum device, making it a candidate for evaluating the performance of
early quantum computers. Moreover, the algorithm is designed to leverage the strengths
of a given architecture. That is, if some gates or quantum operations may be performed
with higher fidelity, then the algorithm can leverage these strengths in the design of the
quantum hardware ansatz [4, 8].
The method starts by selecting a parameterised quantum circuit (ansatz) that prepares
a trial quantum state,
⃗ = U (θ)
⃗ |0⟩ ,
|ψ(θ)⟩
(12)
and evaluates its energy expectation with respect to the target Hamiltonian H. The
classical computer then optimises the parameters to minimise the energy, using the variational principle which guarantees:
⃗ = ⟨ψ(θ)|
⃗ H |ψ(θ)⟩
⃗ ≥ E0 ,
E(θ)

(13)

where E0 is the true ground-state energy [5,6]. This makes VQE particularly suitable for
quantum chemistry, where classical computational cost scales exponentially with system
size.

5

Figure 2: VQE Pipeline [11].

5.2

General Variational Formulation

The VQE energy functional is a special case of the broader VQA framework:
⃗ = ⟨ψ(θ)|
⃗ H |ψ(θ)⟩
⃗ .
min E(θ)
θ⃗

(14)

Any VQA consists of a parameterised quantum circuit whose parameters are iteratively
tuned through feedback from classical computation [6].
Algorithm 1 Variational Quantum Eigensolver (VQE)
Require: Hamiltonian H, ansatz U (θ), classical optimizer O
Ensure: Approximate ground-state energy E ∗
1: Initialize parameters θ
2: repeat
3:
Prepare trial state |ψ(θ)⟩ = U (θ) |0⟩
4:
Estimate energy E(θ) = ⟨ψ(θ)| H |ψ(θ)⟩
via repeated measurements

5:
Update parameters θ ← O θ, ∇θ E
6: until convergence
7: return E ∗ = E(θ)

5.3

Hybrid Quantum–Classical Loop

The workflow for VQE and most VQAs follows a common iterative structure:
⃗
1. A classical optimiser proposes a new set of parameters θ.
⃗ |0⟩.
2. The quantum processor prepares the state U (θ)
3. Measurements are performed to estimate the expectation value ⟨H⟩ (decomposed
into Pauli strings).
4. The classical optimiser updates θ⃗ according to the measured energy landscape.
6

This hybrid loop leverages the strengths of both systems: quantum processors represent complex many-body states, while classical optimisers handle noisy, high-dimensional
parameter landscapes [4, 8].

5.4

How VQAs Overcome Classical Bottlenecks

1. Exponential Memory An N -qubit quantum device implicitly encodes 2N complex
amplitudes, removing the need for classical storage of exponentially large vectors [7].
2. Exponential Runtime Instead of explicitly summing over all basis states, expectation values are obtained through repeated sampling on quantum hardware, providing
⃗ [5].
an efficient estimate of E(θ)
3. Expressive Ansätze Quantum circuits can generate entangled states beyond classical reach. Common choices include:
• Hardware-efficient ansätze (optimised for native gates and connectivity) [8],
• Unitary Coupled Cluster (UCC) for quantum chemistry [4],
• ADAPT-VQE, which grows the ansatz adaptively operator-by-operator [6],
• QAOA layers for discrete optimisation [10].

6

Challenges and Current Research

Variational Quantum Algorithms (VQAs), including VQE and QAOA, are promising
methods for leveraging NISQ devices to tackle classically intractable problems. However, their performance is limited by hardware constraints, ansatz design, measurement
overhead, and classical optimisation challenges [4–8, 12].

6.1

Tension Between Hardware-Efficient and Chemistry-Motivated
Ansätze

Hardware-efficient ansätze are shallow and compatible with NISQ devices but often fail
to capture complex electronic correlations, causing systematic energy errors [4, 5, 8].
Chemistry-inspired ansätze, like UCC, achieve high accuracy but require deep circuits
that exacerbate decoherence [4, 5]. Hybrid strategies, such as ADAPT-VQE, iteratively
build ansätze by adding only energetically relevant operators, balancing depth and expressivity [5, 6]. Hardware-efficient ansätze can also be modified to incorporate problemspecific features [8].

6.2

Mitigating Barren Plateaus

Barren plateaus, where gradients vanish exponentially with system size, hinder effective
optimisation [5,6]. They are worsened by highly expressive or random circuits. Mitigation
strategies include symmetry-preserving ansätze, local operator restrictions, and layerwise
training [6]. Initialization heuristics and cost-function design tailored to the problem also
help maintain nonzero gradients [6].
7

6.3

Reducing Measurement Overhead

Estimating Hamiltonian expectation values requires many Pauli measurements, which
scale poorly and are affected by noise [5,6]. Techniques like Pauli-term grouping, unitary
partitioning, classical shadows, and T-REx reduce measurements and correct errors [12].
Combining these with adaptive ansätze enables efficient classical optimisation [12].

6.4

Adaptive Ansatz Construction

Fixed ansätze may be too shallow or too deep for NISQ hardware [5, 6]. Adaptive approaches like ADAPT-VQE iteratively add only relevant operators, producing compact
circuits with high accuracy. Current research optimises operator pools and growth criteria
to improve scalability and hardware compatibility [6].

6.5

Efficient Gradient Estimation

Accurate gradients are essential for classical optimisation, but NISQ noise and finite sampling can make estimates imprecise [5]. Methods such as the parameter-shift rule, stochastic gradient descent, and variance-reduction improve noise resilience [5, 6, 12]. Problemspecific cost functions and sequential parameter updates further enhance convergence [6].

7

Conclusion

Variational Quantum Algorithms, particularly VQE, have revolutionised approaches to
classically intractable problems in quantum chemistry and many-body physics by combining parameterised quantum circuits with classical optimisation [4–6]. They overcome
exponential memory and runtime limitations while providing expressive ansätze capable
of capturing strong entanglement [4, 5, 8]. Advances such as adaptive ansätze, hardwareefficient designs, and improved measurement and gradient strategies have made VQE
feasible on NISQ devices [5, 6, 12]. This framework not only enables accurate groundstate approximations but also lays the groundwork for scalable quantum simulations,
potentially transforming molecular modelling, materials science, and optimisation, and
opening new avenues for practical quantum applications [4, 6, 8].

References
[1] Wikipedia contributors.
Variational principle — Wikipedia.
https://en.
wikipedia.org/wiki/Variational_principle, 2025. [Online; accessed 28-Nov2025].
[2] Richard P. Feynman and Albert R. Hibbs. Quantum Mechanics and Path Integrals.
McGraw-Hill, New York, 1st edition, 1965.
[3] Physics LibreTexts. Lagrangian and Hamiltonian Mechanics — Physics LibreTexts.
https://phys.libretexts.org/Bookshelves/Mechanics/Book%3A_
Classical_Mechanics_(LibreTexts), 2025. [Online; accessed 28-Nov-2025].

8

[4] Alberto Peruzzo, Jarrod McClean, Peter Shadbolt, Man-Hong Yung, Xiao-Qi Zhou,
Peter J. Love, Alán Aspuru-Guzik, and Jeremy L. O’Brien. A variational eigenvalue
solver on a photonic quantum processor. Nature Communications, 5, 2014.
[5] Jarrod R McClean, Jonathan Romero, Ryan Babbush, and Alán Aspuru-Guzik. The
theory of variational hybrid quantum-classical algorithms. New Journal of Physics,
18(2):023023, 2016.
[6] M. Cerezo, A. Arrasmith, R. Babbush, S.C. Benjamin, S. Endo, K. Fujii, J.R. McClean, K. Mitarai, X. Yuan, L. Cincio, and P.J. Coles. The theory and practice
of the variational quantum eigensolver: A review of formulations and applications.
Nature Reviews Physics, 3:625–644, 2021.
[7] John Preskill. Quantum computing in the nisq era and beyond. Quantum, 2:79,
2018.
[8] Abhinav Kandala, Antonio Mezzacapo, Kristan Temme, Maika Takita, Markus
Brink, Jerry M. Chow, and Jay M. Gambetta. Hardware-efficient variational quantum eigensolver for small molecules and quantum magnets. Nature, 549:242–246,
2017.
[9] IBM Quantum.
Bits, gates, and circuits — Utility-Scale Quantum
Computing Course.
https://quantum.cloud.ibm.com/learning/courses/
utility-scale-quantum-computing/bits-gates-and-circuits, 2024.
[10] Edward Farhi, Jeffrey Goldstone, and Sam Gutmann. A quantum approximate
optimization algorithm, 2014.
[11] J. Tilly, H. Chen, S. Cao, D. Picozzi, K. Setia, Y. Li, E. Grant, L. Wossnig, I. Rungger, G. H. Booth, and J. Tennyson. The Variational Quantum Eigensolver: a review
of methods and best practices. arXiv preprint, arXiv:2111.05176, 2021.
[12] M. Belaloui et al. Techniques for reducing measurement overhead in variational
quantum algorithms, 2025.
[13] Harsha Thapliyal et al. Recent advances in hardware-aware ansätze and adaptive
vqas, 2025.
[14] X. Wang et al. Layerwise optimization and gradient-efficient methods for vqas. IEEE
Transactions on Quantum Engineering, 4:1–12, 2023.

9

