Eur. Phys. J. C
(2025) 85:705
https://doi.org/10.1140/epjc/s10052-025-14322-7

Regular Article - Computing, Software and Data Science

Exploring new variational quantum circuit ansatzes for solving
SU(2) matrix models
Harriet L. Daoa
Singapore, Republic of Singapore

Received: 17 March 2025 / Accepted: 15 May 2025
© The Author(s) 2025

Abstract In this work, we explored and experimented with
new forms of parameterized quantum circuits to be used as
variational ansatzes for solving the bosonic and supersymmetric SU (2) matrix models at different couplings using the
variational quantum Eigensolver (VQE) algorithm. Working
with IBM Qiskit quantum computing platform, we show
that two types of quantum circuits named TwoLocal and
EvolvedOperatorAnsatz can outperform the popular
EfficientSU2 circuits which have been routinely used
in the recent quantum physics literature to run VQE. With
their more customizable constructions that allow for more
flexibility beyond choosing the types of parameterized rotation gates, both types of new circuit ansatzes used in this
work have led to performances that are either better than
or at least comparable to EfficientSU2 in the setting
of SU (2) matrix models. In particular, in the strong coupling regime of the bosonic model, both TwoLocal and
EvolvedOperatorAnsatz circuits provided a better
approximation to the exact ground state, while in the supersymmetric model, shallow EvolvedOperatorAnsatz
circuits, with a small number of parameters, attained a
comparable or even better performance compared to the
much deeper EfficientSU2 circuits with around 8
to 9 times more parameters. The results of this work
demonstrate conclusively the potential of TwoLocal and
EvolvedOperatorAnsatz quantum circuits as efficient
new types of variational ansatzes that should be considered
more frequently in future VQE studies of quantum physics
systems.

Contents
1 Introduction . . . . . . . . . . . . . . . . . . . . . .
a e-mail: espoirdujour1162@gmail.com (corresponding author)

0123456789().: V,-vol

2 Matrix models . . . . . . . . . . . . . . . . . . . . .
2.1 Bosonic matrix models . . . . . . . . . . . . . .
2.2 Supersymmetric matrix models . . . . . . . . . .
3 Variational quantum eigensolver (VQE) . . . . . . . .
3.1 Quantum circuit ansatzes . . . . . . . . . . . . .
3.1.1 EfficientSU2 circuits . . . . . . . . .
3.1.2 TwoLocal circuits . . . . . . . . . . . . .
3.1.3 EvolvedOperatorAnsatz circuits . .
3.2 The estimator module . . . . . . . . . . . . . . .
3.3 Optimizers . . . . . . . . . . . . . . . . . . . . .
3.3.1 Optimizer basics . . . . . . . . . . . . . .
3.3.2 Optimizer selection . . . . . . . . . . . . .
3.4 Overview of VQE experiments . . . . . . . . . .
4  = 2 bosonic model . . . . . . . . . . . . . . . . .
4.1 EfficientSU2 & TwoLocal . . . . . . . . .
4.2 EvolvedOperatorAnsatz . . . . . . . . . .
4.3 Comparison of all quantum circuits . . . . . . . .
5  = 4 bosonic model . . . . . . . . . . . . . . . . .
5.1 EfficientSU2 & TwoLocal . . . . . . . . .
5.2 EvolvedOperatorAnsatz . . . . . . . . . .
5.3 Comparison of all quantum circuits . . . . . . . .
6  = 2 supersymmetric model . . . . . . . . . . . . .
6.1 EvolvedOperatorAnsatz . . . . . . . . . .
6.2 Comparison of all quantum circuits . . . . . . . .
7 Summary and concluding remarks . . . . . . . . . . .
A  = 2 bosonic SU (2) model: full results . . . . . . .
A.1 EfficientSU2 & TwoLocal . . . . . . . . .
A.2 EvolvedOperatorAnsatz . . . . . . . . . .
B  = 4 bosonic SU (2) model: Full results . . . . . . .
B.1 EfficientSU2 & TwoLocal . . . . . . . . .
B.2 EvolvedOperatorAnsatz . . . . . . . . . .
C  = 2 supersymmetric SU (2) model: Full results . . .
D TwoLocal versus EfficientSU2 . . . . . . . . .
D.1  = 2 bosonic SU (2) model . . . . . . . . . . .
D.2  = 4 bosonic SU (2) model . . . . . . . . . . .
References . . . . . . . . . . . . . . . . . . . . . . . . .

123

705

Page 2 of 80

1 Introduction
In recent years, there has been a steadily growing interest in
the problem of quantum simulation of different systems in
high energy physics, especially with the increasingly more
accessible quantum computing resources (either in the form
of actual quantum computers or quantum simulators) offered
by various industrial quantum computing platforms such as
IBM-Qiskit [1] and Google-Cirq [2], among others. An
important class of examples include the simulation of φ 4
scalar quantum field theory following the seminal works [3],
[4,5], which opened up new directions that have been investigated in more recent works such as [6,7]. The 2021 Snowmass review [8] provides an extensive overview on the topics
of quantum simulation for quantum field theories. Some other
interesting examples discuss the quantum simulation of dark
energy and dark matter [9], the simulation of different types
of black holes [10,11], the simulation of matrix models [12]
and quantum field theories with holographic duals [13,14],
the simulation of superconformal quantum mechanics [15]
on quantum computers.
Among the growing literature of quantum simulation of
high energy physics, the work [16] that explored three different approaches involving quantum computing, deep learning
and Lattice Monte Carlo to solve the bosonic and minimally
supersymmetric SU (2) matrix models is of particular interest to us. In the quantum computing approach, the authors
of [16] reported promising results obtained by using a type
of IBM Qiskit quantum circuits called EfficientSU2
[17], involving parameterized rotation RY and RY R Z gates,
as variational ansatzes to run the variational quantum eigensolver (VQE) algorithm [18–21] in order to estimate the
ground state energies of the truncated SU (2) matrix models at certain Fock space cutoff  at four different coupling
values. While the energies calculated by VQE showed a good
agreement with the exact ground state energies, the authors
of [16] stated that the variational forms of their quantum
circuit ansatzes were not specifically optimized for the problem of matrix models, which subsequently might have led to
the larger observed deviation from the exact energies at the
strong coupling compared to the weak coupling regime.
Inspired by [16] and the need to identify some better
forms of variational quantum circuits that perform well in
the strong as well as the weak coupling regimes within the
setting of matrix models, we aim to explore and experiment
with additional types of IBM Qiskit quantum circuits in
this work. Compared to [16] in which the ansatzes were
fixed to be of only two possible forms (EfficientSU2
[22] with either RY or RY R Z parameterized gates), here,
we adopt a more ansatz-centric standpoint. In particular, we
constructed and experimented with multiple variants of new
types of quantum circuit ansatzes called TwoLocal [23] and
EvolvedOperatorAnsatz [24] from IBM Qiskit,

123

Eur. Phys. J. C

(2025) 85:705

in addition to using multiple variants of EfficientSU2
beyond those already introduced in [16]. For the bosonic
SU (2) matrix model at Fock space cutoffs  = 2 and  = 4
at four coupling values λ = 0.2, 0.5, 1.0, 2.0, we consistently obtained better performances from TwoLocal and
EvolvedOperatorAnsatz compared to Efficient
SU2. When using the results reported in [16], which use
deeper versions of EfficientSU2 circuits (than the ones
in ours), as benchmarks, our best results always turned out
to be closer to the exact energy values than those reported
in [16]. In the supersymmetric case, working only with shallow EvolvedOperatorAnsatz circuits at a small number of parameters, we obtained results that outperformed
those reported in [16] for λ = 0.5 and λ = 2.0, while
for λ = 0.2 and λ = 1.0, our results were quite close
to but not as good as those of [16], which were obtained
using much deeper EfficientSU2 circuits with 8-9 times
larger in terms of the numbers of parameters. With these
results, we highlight the promising potential of TwoLocal
and EvolvedOperatorAnsatz quantum circuits as new
types of variational ansatzes that should be considered more
often in future quantum simulation research.
This rest of this paper is organized as follows.
• Section 2 collects some brief and relevant facts about the
SU (2) bosonic (Sect. 2.1) and supersymmetric matrix
models (Sect. 2.2).
• Section 3 summarizes the basics of VQE and describes
in detail the three components that are essential to VQE.
In particular, Sect. 3.2 describes the estimator used to
simulate the quantum measurements of the Hamiltonian
expectation values. Section 3.1 discusses in detail the
three types of variational quantum circuit ansatzes used
to run VQE algorithm for all the experiments in this work.
These include EfficientSU2 in 3.1.1, TwoLocal in
3.1.2 and EvolvedOperatorAnsatz in 3.1.3. Section 3.3 describes the basics of various types of classical
optimizers (Sect. 3.3.1) and the VQE experiments used
to select the optimizers that would be used throughout
this work (Sect. 3.3.2). An overview of the whole section
is presented in Sect. 3.4.
• Section 4 presents the main results of applying the
quantum circuit ansatzes introduced in Sect. 3.1 to
the SU (2) bosonic matrix model at Fock space cutoff
 = 2. Within this section, we first present the results
obtained by using TwoLocal and EfficientSU2
in Sect. 4.1, followed by the results obtained by using
EvolvedOperatorAnsatz in Sect. 4.2, followed by
a comparison of the results in this work with those
reported in [16] in Sect. 4.3.
• Section 5 presents the results for the case of SU (2)
bosonic matrix model at Fock cutoff  = 4. This follows
the same structure as Sect. 4 in which the VQE results

Eur. Phys. J. C

(2025) 85:705

obtained by EfficientSU2 and TwoLocal ansatzes
are first presented in 5.1, followed by the results obtained
by using EvolvedOperatorAnsatz in Sect. 5.2, followed by a comparison of all types of ansatzes including
the results of [16] in Sect. 5.3.
• Section 6 presents the results for the case of supersymmetric SU (2) matrix model at Fock cutoff  = 2. The
VQE results obtained by using EvolvedOperator
Ansatz are presented in 6.1 followed by a comparison
of these results against those from [16] in Sect. 6.2
• Section 7 closes the paper with a summary and some
concluding remarks.
• The Appendices A, B, C contain the supplementary material consisting of the convergence curves and the full
results from all VQE experiments corresponding to the
three truncated SU (2) matrix models (bosonic  = 2 in
Sect. A.1, A.2,  = 4 in Sects. B.1, B.2 and supersymmetric  = 2 in Section C). The Appendix D
includes the convergence curve plots showing the direct
comparisons between the performances of TwoLocal
and EfficientSU2 circuits, variant by variant, for the
cases of bosonic SU (2) models at Fock space cutoffs
 = 2 (D.1) and  = 4 (D.2).
The Python codes used to construct the quantum circuits and
carry out the VQE experiments for this work can be found at
the GitHub repository: https://github.com/lorrespz/matrix_
model_quantum_computing_vqe.
We make use of standard Python libraries like numpy,
pandas, matplotlib in addition to the specialized
Qiskit libraries qiskit, qiskit_aer, qiskit_
algorithms.

2 Matrix models
Matrix models occupy an important place in string theory, since they are the results of the dimensional reduction
of super Yang-Mills (SYM) theory from higher spacetime
dimensions down to just the time dimension [25]. Given the
essential role of strongly-coupled SU (N ) SYM theory (in the
large N limit) as the dual of a weakly coupled supergravity
theory in the celebrated AdS/CFT correspondence, various
tests of AdS/CFT have been carried out using different versions of SYM, including versions in which the SYM theories
are dimensionally reduced to some supersymmetric matrix
models. Some notable examples of these tests includes the
Monte-Carlo simulation of quantum black holes using matrix
model as done in the works [26,27] (see also the work [28] in
which the authors study the thermodynamics of BMN supersymmetric matrix model at strong t’Hooft coupling using the
gravity dual).

Page 3 of 80

705

In this section, we only briefly summarize some pertinent facts about matrix models with the practical aim being
the derivation of the Hamiltonian to be used in the VQE
algorithm. A longer and more detailed discussion of SU (N )
matrix models can be found in [16,25].
2.1 Bosonic matrix models
The Hamiltonian of a bosonic SU (N ) matrix model in the
operator formalism is given by


1 2 m 2 2 g2
(1)
P̂I −
X̂ I + [ X̂ I , X̂ J ]2 ,
Ĥ = Tr
2
2
4
where I = 1, . . . , D labels the number of matrices. The
momentum P̂I and position X̂ I operators can be written
in terms of the (N 2 − 1) SU (N ) generators τα (with α =
1, . . . , N 2 − 1 labeling the adjoint representation of SU (N ))
as
P̂I =

2 −1
N

PIα τα , X̂ I =

α=1

2 −1
N

X̂ αI τα .

(2)

α=1

The SU (N ) generators τα , normalized as Tr(τα τb ) = δαβ ,
obey the commutation relations
[τα , τb ] = f αβγ τγ ,

(3)

where f αβγ are the structure constants of SU (N ) group. The
canonical commutation relation of the Hamiltonian (1) is


(4)
X̂ I α , P̂Jβ = iδ I J δαβ .
Note that the Hamiltonian (1) and the canonical commutation
relation (4) are invariant under the SU (N ) transformations
X̂ I →

X̂ I

−1

,

P̂I →

P̂I

−1

.

(5)

Using (2), the Hamiltonian (1) can be written as

 1
m2 2
2
Ĥ =
P̂ +
X̂
2 Iα
2 Iα
α,I
⎛
⎞2
g 2  ⎝
β
+
f αβγ X̂ αI X̂ J ⎠ .
4
γ ,I,J

(6)

α,β

in which the total number of (bosonic) degrees of freedom is
D × (N 2 − 1). To use quantum computing, the Hamitonian
of the system of interest must be a finite-dimensional matrix
of even dimensions. For this purpose, one often uses the discrete Fock space representation involving the creation and
annihilation operators in terms of which the Hamiltonian is
written. So, by using the definition of the creation and annihilation operators in terms of the position and momentum
operators
â †I α =

m
i P̂I α
X̂ I α − √ , â I α =
2
2m

m
i P̂I α
X̂ I α + √ ,
2
2m

(7)

123

705

Page 4 of 80

Eur. Phys. J. C

and the number operator n̂ I α = â †I α â I α , the Hamiltonian (6)
can be written as


1
g2 
n̂ I α +
Ĥ = m
+
2
16m 2
α,I
γ ,I,J
⎛
⎞2

×⎝
f αβγ (â I α + â †I α )(â Jβ + â †Jβ )⎠ .
(8)
α,β

For each (I, α) mode, the Fock vacuum |0 I α satisfies
â I α |0 I α = 0

(9)

and the excited states |n I α are created by applying the creation operator â †I α on the vacuum state |0 I α
1
|n I α = √ (â †I α )n |0 I α
n!

(10)

The Fock vacuum of the matrix model is the tensor product of each individual I α mode |0 = ⊗ I α |0 I α . Next, we
must truncate the system to retain excitations only up to a
certain cutoff  so that the system can be simulated on a
quantum computer. This leads to the following definition of
the truncated creation, annihilation and number operators
†
=
âtruncated

âtruncated =
n̂ truncated =

−2


√

n=0
−2


√

n=0
−1


n + 1|n + 1n|,
n + 1|nn + 1|,

n|nn|

(11)

n=0

In this work, as in the quantum computation part of [16], the
choice of N = 2 and D = 2 is made, which leads to the
group being SU (2) with D × (N 2 − 1) = 6 bosonic degrees
of freedom. The Fock space cutoff  is taken to be  = 2 and
 = 4. The first case leads to a 26 = 64-dimensional Hilbert
space while the second case leads to a 46 = 212 = 4096dimensional Hilbert space. The matrix representation for the
âi annihilation operator for the case of  = 2 and  = 4 is:
 
01
 = 2 : âi = 12 ⊗ . . . ⊗ 12 ⊗
⊗ 12 ⊗ . . . ⊗ 12






00
(i − 1) times

(6−i)times

⎛
⎞
0 1 √0 0
⎜0 0 2 0 ⎟
√ ⎟
 = 4 : âi = 14 ⊗ . . . ⊗ 14 ⊗ ⎜


 ⎝0 0 0
3⎠
(i − 1) times
00 0 0
⊗ 14 ⊗ . . . ⊗ 14




(12)

2.2 Supersymmetric matrix models
The supersymmetric matrix model of interest to us is the
mass-deformed version of the one originating from the
dimensional reduction of the minimal 3D SU (N ) SYM theory [16,25], with the following Hamiltonian

g
1 2 g2
P̂ − [ X̂ I , X̂ J ]2 + ψ̄ I [ X̂ I , ψ]
H = Tr
2 I
4
2

2
3i
μ 2
− μψ̄ψ +
(14)
X̂ − (N 2 − 1)μ ,
4
2 I
where, as in the bosonic case, I = 1, . . . , D labels the number of matrices. I is the D-dimensional gamma matrices
and ψ is a two-component Majorana fermion, which can be
written as
 
ζ
.
(15)
ψ=
iζ †
In Eq. (14), μ is the mass term that is added to the massless
theory resulting from the dimensional reduction of the 3D
minimal SYM, and the presence of the term −(N 2 − 1)μ
forces the ground state energy to be exactly zero.
When N = 2, the minimal SU (2) BMN supersymmetric
matrix model has 6 bosonic degrees of freedom ( X̂ I α where
I = 1, 2 and α = 1, 2, 3) and 3 fermionic degrees
of freedom

ζα , which obey the anticommutation relation ζα† , ζβ = δαβ .
The Hamiltonian for this case is [16]

1
2
2
2
2
P̂1α
+ P̂2α
+ μ2 X̂ 1α
+ μ2 X̂ 2α
+ 3μ ζ̂α† ζ̂α ,
H =
2
α


2
2
− 2g 2
+g 2
X̂ 1α
X̂ 2β
X̂ 1α X̂ 1β X̂ 2α X̂ 2β ,
α=β

α<β


ig 
+√
αβγ −( X̂ 1α + i X̂ 2α )ζ̂β† ζ̂γ†
2 α,β,γ



+ − X̂ 1α + i X̂ 2α ζ̂β ζ̂γ − 3μ .

(16)

The fermion operators ζα obey the anticommutation relation ζα , ζβ = δαβ . With the Fock space cutoff chosen to
be  = 2, the fermion operators are constructed using the
Jordan-Wigner transformation involving Pauli spin matrices
as follows
 
00
⊗ 12 ⊗ . . . ⊗ 12 .
(17)
ζα = σ z ⊗ . . . ⊗ σ z ⊗



10
α−1times

(13)

(6−i)times

where 12 and 14 are the 2 × 2 and 4 × 4 identity matrix,
respectively.

123

(2025) 85:705

In this case, the fermionic Hilbert space sector has dimension
23 . Together with the bosonic sector, which has dimension
26 = 64, the total Hilbert space has dimension 29 = 512.
The 3 fermionic operators have to be tensored with 164 - the
64 × 64 identity matrix. The bosonic operators are the same
as defined in Eq. (12), except that they are now tensored with
18 (8 × 8 identity matrix). Explicitly, for the fermionic part,

Eur. Phys. J. C

(2025) 85:705

Page 5 of 80

705

Fig. 1 The main components
of VQE: a quantum circuit
ansatz, a quantum device (or a
simulator) to estimate the
expectation value of the
Hamiltonian, and a classical
optimizer

the three annihilation operators are defined as follows
 
01
⊗ 12 ⊗ 12 ,
(18)
c1 = 164 ⊗
00
 
01
c2 = 164 ⊗ σz ⊗
⊗ 12 ,
(19)
00
 
01
c3 = 164 ⊗ σz ⊗ σz ⊗
.
(20)
00
Note that for the truncated supersymmetric SU (2) model
considered here, the ground state energy is close to, but no
longer exactly zero.

3 Variational quantum eigensolver (VQE)
Variational quantum eigensolver (VQE) is a popular classicalquantum hybrid algorithm used to estimate the ground state
energy of a Hamiltonian system using some form of parameterized quantum circuits as a variational ansatz. Many examples of VQE have been discussed in great detail in the literature [19–21]. Here, for the sake of self-containedness, we
will briefly recap some details.
Denoting the parameterized quantum circuit by a unitary
operator Û (θ) acting on a collection of qubits initialized to
zero1
|0 = |0 ⊗ · · · ⊗ |0




(21)

n Q times

where n Q is the number of qubits, the expectation value of
an observable, such as a Hamiltonian Ĥ , can be measured in
terms of a trial wavefunction (θ) given by (θ) = Û (θ) |0
as
 


 
(22)
(θ  Ĥ  (θ)
Using VQE, the ground state energy of the Hamiltonian Ĥ is
estimated using (22) by means of a quantum computer (or a
suitable quantum simulator) and is optimized with a classical
optimizer. A schematic of the different components of VQE
is shown in Fig. 1.
In Eq. (22), θ are the parameters to be varied so that the
algorithm returns an upper bound estimate E VQE on the exact
1 Some other initializations are possible other than zero.

ground state energy E 0 :



(θ)| Ĥ |(θ)
 .
E 0 ≤ E VQE = 
(θ)|(θ)

(23)

In order to carry out the estimation involving quantum circuits of the form (22), the Hamiltonian has to be written as
a sum of the tensor products of Pauli operators, (also called
Pauli strings) of the form Q 1 ⊗ Q 2 ⊗ . . . ⊗ Q n Q where
Q i ∈ (I2 , X, Y, Z ). If fermionic operators are present, these
can be converted to Pauli string operators using the JordanWigner transformation [29].
Throughout this work, we perform all VQE experiments
exclusively using Qiskit, an IBM quantum computing
platform with an extensive suite of libraries for quantum circuits, algorithms, simulators and even access to real quantum hardware (quantum computers with hundreds of qubits)
hosted on their cloud servers [1]. We recall that our settings
of interest for all VQE experiments are the following Hamiltonians representing the truncated SU (2) matrix models.
• Bosonic SU(2) model truncated at Fock cutoff  = 2:
This leads to a model with 6 bosonic modes with 26 = 64
states and a 64 × 64-dimensional Hamiltonian – corresponding to 6-qubit circuits used in VQE.
• Bosonic SU(2) model truncated at Fock cutoff  = 4:
This leads to a model with 6 bosonic modes with 46 =
212 = 4096 states and a 4096×4096-dimensional Hamiltonian – corresponding to 12-qubit circuits used in VQE.
• Supersymmetric SU(2) model truncated at Fock cutoff
 = 2: This leads to a model with 6 bosonic modes
+ 3 fermionic modes with 29 = 512 states and a 512 ×
512-dimensional Hamiltonian – corresponding to 9-qubit
circuits used in VQE.
For each of the three cases above, we will look at four different couplings λ = 0.2, 0.5, 1.0, 2.0 where λ = g 2 N ,
with g is the actual coupling appearing the in Eqs. (1), (14),
and N = 2 corresponding to SU (2) group of the matrix
model. This leads to four different Hamiltonians per case. In
total, there are twelve Hamiltonians Hλ including 8 bosonic
=2,4
Hamiltonians Hλ=0.2,0.5,1.0,2.0
and 4 supersymmetric Hamil-

(S) =2
tonians Hλ=0.2,0.5,1.0,2.0
.
While it is desirable to study more complex matrix models
such as SU (2) at higher Fock space cutoff , or matrix mod-

123

705

Page 6 of 80

els with a larger group SU (N ) where N > 2, we note that
such models are drastically more computationally demanding. In general, the number of states for a bosonic SU (N )
matrix model (with N 2 −1 generators) with d bosonic matri2
ces truncated at Fock cutoff  is d(N −1) . Concretely speaking, when N = 3, for the SU (3) matrix model with 8 SU (3)
generators τα (α = 1, . . . , 8), the smallest number of bosonic
matrices is d = 2, corresponding to 16 modes X I α (with
I = 1, 2). At the lowest Fock cutoff of  = 2, the total
number of modes is 216 = 65, 536 states. At this level,
without access to an actual quantum hardware hosted on a
large server, a modern laptop2 operating a Qiskit simulator cannot handle this, simply because it will run out of
memory before long. The situation only gets worse: at cutoff
 = 4, the number of states in the SU (3) matrix model is
416 = 232 = 4.3 × 109 . When N = 4, for SU (4) matrix
models, with 15 SU (4) generators τα with α = 1, . . . , 15,
the smallest number of bosonic matrices is d = 2, corresponding to 30 modes X I α (I = 1, 2), and at Fock cutoff
 = 2, the number of states is 230 = 1.07 × 109 . Even
for the SU (2) models with only 3 generators and 6 bosonic
modes at the very least, at Fock space cutoff  = 8, the number of states is still 86 = 218 = 262, 144, which cannot be
handled by a modern laptop. The complications arising from
the resource intensive nature of the computation with larger
and more complex matrix models were also noted in [16] in
which the authors chose alternative approaches (rather than
quantum computing), such as deep learning involving a classical neural network and lattice Monte Carlo simulation, to
deal with SU (3) matrix models.
In the subsequent sections, we will describe in detail the
various components that are integral to the practical implementation of the VQE algorithm in Qiskit.
3.1 Quantum circuit ansatzes
The first crucial component of VQE that we will focus on
is the quantum circuit ansatzes composed of parameterized
gates whose parameters can be varied to obtain certain optimized expectation value of the specific Hamiltonian of interest. The main challenge involving quantum circuit ansatzes
in VQE is the limited overlap of these ansatzes with the
actual quantum states in the corresponding Hilbert space
under study, which makes the optimization process rather difficult. A good choice of quantum circuit ansatzes is hence of
paramount importance to the overall success of VQE experiments. Two main different approaches exist with respect to
the selection of quantum circuit ansatzes, one involving the
use of generic, untailored ansatzes chosen for their hardware
efficiency for all problem settings, and another involving the
2 Such as one with 16–64 Gb RAM (at the time of writing this article).

123

Eur. Phys. J. C

(2025) 85:705

use of tailored ansatzes constructed specifically for the particular problem setting of interest. In this work, we will explore
both approaches in the context of SU (2) matrix model.
One of the building blocks of a quantum circuit ansatz is
parameterized rotation gates like R X , RY , and R Z given by
⎞
⎛


cos θ2 −i sin θ2
θ
⎠,
R X (θ ) = exp −i X = ⎝
2
−i sin θ2 cos θ2
⎛
⎞


cos θ2 − sin θ2
θ
⎠,
RY (θ ) = exp −i Y = ⎝
2
θ
θ
sin 2 cos 2


⎛
⎞


exp −i θ2
0
θ
⎠
R Z (θ ) = exp −i Z = ⎝
  , (24)
2
0
exp i θ2
where X, Y, Z are the Pauli matrices.
Another essential building block comprises the so-called
entanglement gates that act on multiple qubits and are used
to entangle qubits in the quantum circuits. The most common
of such gates are the controlled type of gates, for example
the 2-qubit Controlled-X (C X ) gate (also known as CNOT
gate)
⎛
⎞
1000
⎜0 1 0 0⎟
⎟
C X (q0 , q1 ) = |00| ⊗ 12 + |11| ⊗ X = ⎜
⎝0 0 0 1⎠ ,
0010
(25)
where 12 is the 2D identity matrix, and |0 = (1, 0),
|1 = (0, 1) denote the single qubit state. The parameterized version of the C X gate, the C R X (θ ) gate given by
C R X (θ, q0 , q1 ) = |00| ⊗ 12 + |11| ⊗ R X (θ )
⎛
⎞
10
0
0
⎜0 1
0
0 ⎟
⎟,
=⎜
θ
⎝0 0 cos
−i sin θ ⎠
2

0 0 −i sin θ2

cos θ2

(26)

2

is also another popular choice. Other choices include R X X
(a parameterized 2-qubit X ⊗ X rotation gate) given by


θ
R X X (θ ) = exp −i X ⊗ X ,
(27)
2
RCC X gate (a parameterized simplified Toffoli gate), and
RC3X gate (a parameterized simplified 3-controlled Toffoli
gate). Using some combinations of these gates, we would
describe in detail, in subsequent sections, the types of quantum circuits that will be used as variational ansatzes for
running all the experiments in this work. All these circuits
are implemented in the Qiskit quantum circuit library
qiskit.circuit.library.3
3 https://docs.quantum.ibm.com/api/qiskit/circuit_library.

Eur. Phys. J. C

(2025) 85:705

Page 7 of 80

705

Table 1 Details of the eight variants of EfficientSU2 ansatzes used throughout this work. d is the depth of the circuit, and n Q is the number
of qubits in the circuit
EfficientSU2 circuits

Parameters

Rotation block
(parameterized)

Entanglement pattern
(unparameterized)

effsu2_Ry_c (Fig. 2a)

(d + 1) × n Q

RY

Circular

effsu2_Rz_c (Fig. 2b)

(d + 1) × n Q

RZ

Circular

effsu2_RyRz_c (Fig. 2c)

2(d + 1) × n Q

RY and R Z

Circular

effsu2_RyY_c (Fig. 2d)

(d + 1) × n Q

RY and Y

Circular

effsu2_Ry_f (Fig. 2e)

(d + 1) × n Q

RY

Full

effsu2_Rz_f (Fig. 2f)

(d + 1) × n Q

RZ

Full

effsu2_RyRz_f (Fig. 2g)

2(d + 1) × n Q

RY and R Z

Full

effsu2_RyY_f (Fig. 2h)

(d + 1) × n Q

RY and Y

Full

3.1.1 EfficientSU2 circuits
Qiskit EfficientSU2 circuits [22] are hardware efficient quantum circuits that consist of a rotation building
block with the default choice being a combination of RY
and R Z gates, and an entanglement block with the default
choice being C X gates. This is the predominant type of circuits used for many recent works in the literature dealing
with VQE using Qiskit platform [9–11,16]. In our experiments, we will vary the rotation block and the scheme of
the entanglement block (which can be either ‘circular’ or
‘full’ among other choices). This leads to the eight different
EfficientSU2 ansatzes listed in Table 1, which are categorized into eight variants with four different types of rotation
blocks and 2 different schemes of entanglement arrangement.
The four types of gates in the rotation blocks are RY , R Z ,
RY R Z , RY Y , while the two entanglement schemes are either
‘circular’, in which the any qubit in the circuit is entangled
with its next nearest neighbor and the last qubit is entangled
with the first one, or ‘full’ in which every qubit in the circuit
is entangled with every other qubits in the circuit (using only
C X gates). Note that in the work [16] the authors employed
2 variants of EfficientSU2, one consisting of solely RY
gates in the rotation block and the other consisting of RY R Z
gates in the rotation block, with the full entanglement scheme
for both variants.
The number of parameters of the EfficientSU2 quantum circuits are the same as the number of parameterized
gates in the rotation blocks. This amounts to (d + 1) × n Q
parameters where d is the depth of the circuit (the number
of repetitions that the basic building block of the circuit is
repeated) and n Q is the number of qubits, for variational
forms involving a single type of rotation gates (either RY or

R Z or RY Y since Y gate is not parameterized) or 2(d+1)×n Q
for variational forms involving two types of rotation gates
(RY R Z ). Given these number of parameters, the scaling property of EfficientSU2 for all the 8 variants considered in
this work is linear in both the circuit depth d and number of
qubits n Q . The variant with the most number of parameters
is effsu2_RyRz_c and effsu2_RyRz_f with RY R Z
gates in the rotation part.
3.1.2 TwoLocal circuits
TwoLocal circuits [23] have similar structure to, but more
general than, EfficientSU2 in the sense that they still
consist of a rotation block followed by an entanglement
block, but there is more freedom in choosing the type of
gates in the entanglement block. In particular, we are not
limited to the unparameterized C X but have access to more
general gates such as the parameterized C R X , R X X , RC2X
and RC3X gates for entangling the qubits. Analogous to
the EfficientSU2 case above, we use the eight variants
of TwoLocal quantum circuits with the same four types
of rotation blocks (consisting of either RY , R Z , RY R Z or
RY Y ) and two entanglement schemes (‘circular’ or ‘full’),
but these TwoLocal circuits employ the parameterized
C R X gates in the entanglement block (see Table 2). This
increases the number of parameters in TwoLocal quantum
circuits but also enhance their expressivity compared to their
EfficientSU2 counterparts.
In particular, the number of parameters in this type of
quantum circuits are the sum of the number of parameterized
rotation gates and entanglement gates. A circular entanglement pattern leads to an additional n Q number of parameters
per circuit depth d, while a full entanglement pattern leads

123

705

Page 8 of 80

Fig. 2 The eight variants of
EfficientSU2 ansatzes used
throughout this work. Note that
for demonstration purpose, we
choose the number of qubits to
be 6 in the figures above but the
actual numbers of qubits are
either 6 or 12 depending on the
Hamiltonian under study. (a)
effsu2_Ry_c: RY gates and
circular entanglement pattern.
(b) effsu2_Rz_c: R Z gates
and circular entanglement
pattern. (c) effsu2_RyRz_c:
RY R Z gates and circular
entanglement pattern. (d)
effsu2_RyY_c: RY Y gates
and circular entanglement
pattern. (e) effsu2_Ry_f: RY
gates and full entanglement
pattern. (f) effsu2_Rz_f: RY
gates and full entanglement
pattern. (g) effsu2_RyRz_f:
RY R Z gates and full
entanglement pattern. (h)
effsu2_RyY_f: RY Y gates
and full entanglement pattern

123

Eur. Phys. J. C

(2025) 85:705

Eur. Phys. J. C

(2025) 85:705

Page 9 of 80

705

Table 2 Details of the eight variants of TwoLocal ansatzes used throughout this work. d is the circuit depth, n Q is the number of qubit in the
circuit
TwoLocal circuits

Parameters

Rotation block
(parameterized)

Entanglement block
(parameterized)

tl_Ry_c (Fig. 3a)

(2d + 1)n Q

RY

C R X , circular

tl_Rz_c (Fig. 3b)

(2d + 1)n Q

RZ

C R X , circular

tl_RyRz_c (Fig. 3c)

(3d + 2)n Q

RY and R Z

C R X , circular

tl_RyY_c (Fig. 3d)

(2d + 1)n Q


1 2
1
d nQ +
d + 1 nQ
2
2


1
1 2
d nQ +
d + 1 nQ
2
2


1 2
3
d nQ +
d + 2 nQ
2
2


1 2
1
d nQ +
d + 1 nQ
2
2

RY and Y

C R X , circular

RY

C R X , full

RZ

C R X , full

RY and R Z

C R X , full

RY and Y

C R X , full

tl_Ry_f (Fig. 3e)
tl_Rz_f (Fig. 3f)
tl_RyRz_f (Fig. 3g)
tl_RyY_f (Fig. 3h)



n
Q −1

to an additional

= 21 n Q (n Q − 1) parameters4 per

k

k=1

circuit depth d. Together with the parameters from the rotation gates, which can be either (d + 1)n Q for a single type
of rotation gates or 2(d + 1)n Q for a double type of rotation gates, the total number of parameters can be moderately
large. For example, the variants tl_Ry_c and tl_Ry_f at
depth d have the following total number of parameters
tl_Ry_c : (d + 1)n Q + d n Q = (2d + 1) n Q ,
⎛
⎞
n Q −1

tl_Ry_f : (d + 1)n Q + d ⎝
k⎠
k=1

1
= (d + 1)n Q + d n Q (n Q − 1)
2
4 Let’s consider the term

 nQ


k

k=1

n Q

k=1 k:

!
"
= 1 + 2 + · · · + n Q = n Q − (n Q − 1)

(28)

!
"
!
"
+ n Q − (n Q − 2) + · · · + n Q − (n Q − 0)
!
"
= (n Q + · · · + n Q ) − (n Q − 1) + (n Q − 2) + · · · + 1 + 0



n Q times

⎛

⎞

n Q −1

k⎠
= n 2Q − ⎝
k=1

which means
n 2Q =

 nQ

k=1

⎛
k +⎝

n Q −1


k=1

⎞

⎛

k⎠ = 2 ⎝

n Q −1


k=1

⎞
k⎠ + n Q

⎛
⇒ ⎝

n Q −1



⎞
k⎠

1
= d n 2Q +
2




1
d + 1 nQ .
2

(30)

The exact number of parameters for each of the eight variants of TwoLocal quantum circuits are listed in Table
2. Given these number of parameters, the scaling property
of TwoLocal quantum circuits for the four variants with
circular entanglement pattern is linear in both the circuit
depth d and number of qubits n Q , while the scaling property of TwoLocal circuits with full entanglement pattern
is quadratic in the number of qubits n Q but is still linear in
d, the circuit depth. Compared with EfficientSU2 circuits with the same d and n Q , TwoLocal circuits with the
circular entanglement pattern can be approximately 1.25–
1.5 times larger (when the rotation block is RY R Z ) or 1.5–2
times larger (when the rotation block is RY , R Z , RY Y ), while
TwoLocal circuits with the full entanglement pattern can
be several times larger in terms of the number of parameters,
depending on the number of qubits n Q present. Among the
TwoLocal variants, those with the full entanglement pattern scale much faster than those with the circular pattern. The
variant with the most number of parameters is tl_RyRz_f
with RY R Z rotation gates and full entanglement. For illustration, we plot the number of parameters for tl_Ry_c,
tl_Ry_f, tl_RyRz_c, and tl_RyRz_f as functions of
the circuit depth d and number of qubits n Q in Fig. 4. In terms
of n Q , both tl_RyRz_f and tl_Ry_f scale quadratically,
while tl_Ry_c and tl_RyRz_c scale linearly. In terms o
f d, all circuits scale linearly. As functions of either n Q or
d, tl_RyRz_f scales the fastest, followed by tl_Ry_f,
tl_RyRz_c and tl_Ry_c.

k=1

(29)
=

1
n Q (n Q − 1) .
2

123

705

Page 10 of 80

Eur. Phys. J. C

(2025) 85:705

Fig. 3 The eight variants of
TwoLocal ansatzes (with
C R X gate in the entanglement
block) used throughout this
work. Note that for
demonstration purpose, we
choose the number of qubits to
be 6 in the figures above but the
actual numbers of qubits are
either 6 or 12 depending on the
Hamiltonian under study. (a)
tl_Ry_c: RY gates and
circular entanglement pattern.
(b) tl_Rz_c: R Z gates and
circular entanglement pattern.
(c) tl_RyRz_c: RY R Z gates
and circular entanglement
pattern. (d) tl_RyY_c: RY Y
gates and circular entanglement
pattern. (e) tl_Ry_f: RY gates
and full entanglement pattern.
(f) tl_Rz_f: RY gates and full
entanglement pattern. (g)
tl_RyRz_f: RY R Z gates and
full entanglement pattern. (h)
tl_RyY_f: RY Y gates and full
entanglement pattern

3.1.3 EvolvedOperatorAnsatz circuits
Unlike EfficientSU2 and TwoLocal quantum circuits
described in the previous sections that are built from parameterized rotation and parameterized/unparameterized controlled type of gates and can serve as generic ansatzes
for any VQE problem, EvolvedOperatorAnsatz [24],

123

as constructed and used in this work, are quantum circuits tailored to the specific task at hand. In general,
EvolvedOperatorAnsatz quantum circuits can be
written as
⎛
⎞
NO
d
#
#


⎝ exp −iθi,r Oi ⎠
(31)
r =1

i=1

Eur. Phys. J. C

(2025) 85:705

Page 11 of 80

705

Fig. 4 Scaling properties of TwoLocal quantum circuits tl_Ry_c,
tl_Ry_f, tl_RyRz_c, and tl_RyRz_f as a function of the number of qubits n Q in the range of [6,50] (top figure) at fixed circuit depth
d = 1, and as function of the circuit depth d in the range of [1,20] when
the number of qubits is fixed at n Q = 12 (bottom figure). As functions
of n Q , TwoLocal variants with the full entanglement pattern have a
quadratic scaling while TwoLocal variants with the circular entanglement pattern have a linear scaling. As function of the circuit depth d,

all TwoLocal variants have a linear scaling property. In the top figure,
the two quadratic curves n 2Q and 0.5n 2Q are included to compare with
the quadratic scaling properties of tl_Ry_f and tl_RyRz_f, which
are shown to be faster than 0.5n 2Q but much slower than n 2Q . Furthermore, note that the scaling properties of tl_RyY_c and tl_Rz_c are
the same as tl_Ry_c, while the scaling properties of tl_RyY_f and
tl_Rz_f are the same as tl_Ry_f

where Oi is a set of N O operators [O1 , . . . , O N O ], d is the
depth of the circuit. The exp term in Eq. 31 is handled using
first order Trotterization5 .
As written in Eq. (31), the number of parameters of the
EvolvedOperatorAnsatz circuit is not dependent on

the number of qubits n Q , and thus this type of circuit only
scales linearly with increasing d but does not scale with
increasing n Q , which can be a plus point when n Q is large. In
principle, the operators Oi can be chosen randomly, in which
case EvolvedOperatorAnsatz can serve as variational
ansatzes for any general problem. However, the ‘tailoredness’ of this type of circuits (as used this work) has to do
with the fact that the set of operators Oi chosen for each of
the cases under study is unique and pertinent only to that
case. As such, the exact form of this type of quantum circuit
ansatzes will be described in detail in Sects. 4.2, 5.2, and 6.1
for the  = 2,  = 4 SU (2) bosonic model and  = 2
supersymmetric SU (2) model, respectively.
Comparison with ADAPT-VQE algorithm: While the
tailoredness of the EvolvedOperatorAnsatz circuits
might be reminiscent of the ansatz used in ADAPT-VQE
method, conceptually these are two completely different

5 Trotterization is the process in which a term like U (t) exp(−i H t)
representing the evolution operator of a Hamiltonian H can be approximated to order n as

U (t) ≈

n #
k
#

exp (−i Hi t/n)

j=1 i=1

if H can be written as the sum
H=

k


Hi

i=1

where the Hi ’s do not necessarily commute. Naturally, the larger n is,
the better approximation that one gets for U (t).

123

705

Page 12 of 80

things. It is therefore useful to clarify this point in detail
for the benefit of the reader. ADAPT-VQE, as introduced
in the work [30] in the context of quantum chemistry and
customized in other works such as [31] in the context of a
(1+1)-dimensional gauge theory, constructs a tailored trial
wavefunction by relying on a predefined operator pool from
which to iteratively adjust the trial wavefunction until convergence is reached. The operator pool contains a selection of
various operators that are related to the Hamiltonian H under
study. In the case of [30], this pool includes single and double excitation operators. With ADAPT-VQE algorithm, the
number of operators that are used to act on the wavefunction
is continuously and incrementally adjusted during the algorithm run time – by selecting one at a time6 an operator Ok
whose expectation value [H, Ok ] is the largest – to obtain
an increasingly improved circuit ansatz. On the other hand,
in this work, EvolvedOperatorAnsatz is a choice of
circuit ansatz whose construction starts by defining a set of
operators that are completely fixed during the entire run of
the VQE algorithm. There is no adjustment of the operators
in the ansatz during the VQE run, in direct contrast to the
case of ADAPT-VQE.
3.2 The estimator module

Once a quantum circuit ansatz (θ) = U (θ)|0
has been
chosen, the second crucial task of VQE is the computation
of the expectation value of the Hamiltonian (θ)H |(θ).
This task can be carried out on actual quantum computer
hardware, or on a quantum simulator. While the eventual goal
is to run the VQE algorithms on actual quantum computers,
here – as in the case of [16], we work with a Qiskit simulator due to the time constraint imposed on the free access to
the quantum hardware. The simulator that we use to compute
the expectation value of the Hamiltonian is the Estimator
module [33] provided by qiskit_aer [34].7 Estimator
can be coded in either a noiseless or noisy setting.

6 See also [32] for a variant of ADAPT-VQE that allows for multiple

operators to be added iteratively instead of a single operator at each
iteration.
7 Note that the versions of Qiskit and Qiskit Aer used in this work

are 1.3.0 and 0.15, respectively, while the Qiskit and Aer versions
used in [16] were 0.26.2 and 0.8.2, respectively [17]. There are significant differences in the module organizations between these Qiskit
versions. One of these differences is the deprecation of the module
opflow that was heavily used in the VQE codes of [16] which allows
the Hamiltonian to be declared as a MatrixOp without the need to
convert it explicitly to Pauli string operator form [17]. In later versions
of Qiskit (starting from 0.28) and in our codes, the starting point
of all VQE runs are the Hamiltonians written in the forms of Pauli
string operators. A simple example of how to run VQE (using the latest
Qiskit version at the time of this writing) can be found in the tutorial
[35].

123

Eur. Phys. J. C

(2025) 85:705

• In the noiseless setting, depending on the
‘approximation’ parameter (either True or False)
and the number of shots (either None or int), it
is a state vector simulator which either returns the
exact expectation value (approximation = True,
shots = None) or the expectation value with sampling noise (approximation = False, shots =
int) [33]. In this work, we choose the latter setting with
shots=1024. The larger the the number of shots, the
smaller the difference will be between the actual value
and that of a VQE simulation.
• In the noisy setting, various available and realistic noise
models can be added to the Estimator. These noise
models can either be custom built from scratch by
adding to the quantum circuit ansatzes several types of
preexisting quantum errors defined in Qiskit which
include depolarizing quantum error channel, amplitude/phase damping errors, coherent/mixed unitary error,
readout errors and thermal relaxation errors among
others [36], or built based on the properties and the
noise profiles of real quantum IBM devices such as
the 127-qubit ibm_brussels, ibm_brisbane or
ibm_strasbourg among others.8 In the presence of
noise, there exist several error mitigation techniques
[37], such as TREX (Twirled readout extinction) [38],
ZNE (Zero-noise extrapolation), PEA (Probabilistic error
amplification) [39] and PEC (Probabilistic error cancellation), that can be coded into the Estimator module [40]. It is expected that in the noisy setting, even
with the use of the few error mitigation techniques mentioned above, the results of the VQE experiments will be
worse compared to those run in the noiseless setting. In
particular, the run time of each experiment will be significantly longer before convergence is reached and the
values obtained at convergence will not be as close to
the actual values as in the noiseless case. In worst case
scenarios, convergence might not be reached at all.
Due to the nature of this work being an exploration of many
different types of quantum circuit ansatzes, thus a proof-ofconcept of sort, which requires relatively fast running times
(in the order of several hours at most per experiment) in order
to quickly establish the most efficient ansatzes, we defer the
use of noisy setting for the Estimator (together with some
error mitigation techniques listed above) to future works in
which a single type, rather than multiple types, of quantum
circuit ansatzes are studied.

8 The list of active IBM quantum computers can be found at https://

quantum.ibm.com/services/resources, while the list of retired IBM
quantum devices can be found at https://docs.quantum.ibm.com/
guides/retired-qpus.

Eur. Phys. J. C

(2025) 85:705

Page 13 of 80

independently from the set {−1, 1}. The update rule for
SPSA is the same as Eq. (32), but with the derivative
∇ L(θk ) replaced by f (θk ) given in Eq.(33)

3.3 Optimizers
3.3.1 Optimizer basics
Optimizers are a crucial component in the VQE algorithm
since they perform the essential task of updating the parameters θ of the quantum circuit ansatzes subjected to a loss
 9 to be minimized. The process of
or objective function L(θ)
parameter update can be either gradient-based, in which the
first derivative or the gradient of L(θ), ∇ L(θ) is utilized and
needs to be known in exact form, or gradient-free, in which
∇ L(θ) is either unnecessary or only needs to be known in
approximated forms. The most basic type of gradient-based
parameter update is a process known as gradient descent
given by the following equation
θk+1 = θk − α∇ L(θk )

(32)

in which θk are the parameters at the k th iteration, and α,
the learning rate, is a hyperparameter chosen by the user.
Too small α leads to a slow convergence while too large
α leads to oscillations and overshooting which might prevent convergence [41]. While gradient-based optimizers are
the cornerstone of modern classical machine and deep learning involving artificial neural networks, gradient-free optimizers are popular choices for quantum computing problem
settings [42,43]. Gradient-free optimizers are more flexible
than gradient-based in the sense that they can perform well
 is complicated, non-smooth or nonin situations where L(θ)
differentiable. Although the overall efficiency of the VQE
algorithm depends greatly on the choices of both quantum
circuit ansatzes and optimizers, the convergence quality is
almost entirely controlled by the type of optimizers used,
given that using the same quantum circuit ansatz with different optimizers lead to different converged results. In this
section, we considered the following six optimizers.10
1. SPSA (stochastic perturbation simultaneous approximation) [46] is a gradient-free stochastic optimization algorithm that performs parameter updates by approximating
the gradient of the loss function ∇ L(θk ) at iteration k by
a function g(θk ) obtained by [42]
 k ) − L(θk − ck 
 k)
L(θk + ck 
k ,

f (θk ) =
2ck

(33)

 k is a random
where ck is a small positive scaling factor, 
perturbation vector (at iteration k) whose entries are drawn
9 For VQE, L(θ)
 is the ground state expectation value of the Hamilto-




nian: L(θ) = (θ)|H
|(θ) .

10 The full list of optimizers can be found at [44] and a useful tutorial

exploring optimization loops from IBM is at [45].

705

θk+1 = θk − α f (θk ) .

(34)

2. COBYLA (constrained optimization by linear approximation) [47] is a gradient-free optimization algorithm that
performs parameter updates by utilizing a linear approximation of the loss function L(θ) as well as all constraints
in the neighborhood of the current point, within a specified
trust region, to determine the next point. At each iteration,
the algorithm solves a linear programming problem inside
a trust region whose radius decreases as certain convergence criterion is reached. An important point to note is
that COBYLA treats simple bounds as constraints, which
might lead to bound violations.
3. NELDER-MEAD [48] is a gradient-free optimization
algorithm and simplex-based direct search method. Given
the loss function L(θ), this algorithm starts with a set of,
say (n +1) points θinitial = (θ0 , . . . , θn ) ∈ Rn that are supposedly the vertices of a simplex S in Rn , and calculates
the loss function value L(θinitial ) at these vertices. Next, a
sequence of transformations is applied to S with the aim
of decreasing L(θ) until the simplex S is sufficiently small
or a convergence criterion is reached.
4. L_BFGS_B is the limited-memory (subject to bounds)
version of BFGS (Broyden–Fletcher–Goldfarb–Shanno),
a gradient-based optimization algorithm, which uses the
Hessian matrix H of the loss function to compute the
direction nk
nk = Hk−1 ∇ L(θk )

(35)

to perform a line search on {θk + ηk nk |ηk ∈ R} to find an
optimal update ηk . Once this is found, the new parameter
θk+1 is updated to
θk+1 = θk + ηk nk .

(36)

With the updated parameter θk+1 , one can calculate the
change in the gradient Dk = ∇ L(θk+1 ) − ∇ L(θk ) and
use that to update the Hessian:
Hk+1 = Hk +

Dk DkT
nk DkT nk

−

Hk nk nkT Hk
nkT Hk nk

.

(37)

5. SLSQP (sequential least squares programming) [49]
is a gradient-based optimization based on sequential
quadratic programming (SQP) which involves the construction of a Lagrangian L from the loss function L(θ)

123

705

Page 14 of 80

Eur. Phys. J. C

and the equality and inequality constraints h i (θ), gi (θ)
 μ)
L(θ, λ,
 = L(θ) +



 +
λi h i (θ)



i

μi gi (θ)

(38)

i

where λi and μi are the Lagrange multipliers associated
with h i and gi . The parameter update at iteration k th pro and μ.
cess not only involves θ but also λ

⎞ ⎛ ⎞
θk
θk+1
k , μ
k)
∇L(θk , λ
⎝λ
 k+1 ⎠ = ⎝ λ
k ⎠ −
2


∇ L(θk , λk , μ
k)
μ
 k+1
μ
k
⎛

(39)

where


∇L = ∇θ L, ∇λ L, ∇μ L .
6. ADAM (adaptive moment estimation) [50] is a gradientbased optimization algorithm that is very popular in
machine and deep learning involving classical neural networks. To perform a parameter update at step k, ADAM
uses the running estimates of the first and the second
moment of the gradient ∇ L(θk ) [42]
μ
 k+1 = β1 μ
 k + (1 − β1 )∇ L(θk )
σk+1 = β2 σk + (1 − β2 )∇ L(θk )  ∇ L(θk )

(40)

where μ
 k denotes the mean estimate and σk the variance,
β1 , β2 ∈ [0, 1) are the decay rates. The final parameter
update equation for ADAM is
θk+1 = θk − $

αμ
ˆ k+1

(41)

σˆ k+1 + 

where α is a positive scaling factor, and μ
ˆ and σˆ are the
scaled or corrected versions of μ
 and σ (due to the fact
that these estimates can be biased when the iteration k is
small)
μ
ˆ k =

μ
k
1 − β1k+1

,

σˆ k =

σk
1 − β2k+1

.

(42)

While gradient-based and gradient-free optimizers have their
own advantages as well as disadvantages, gradient-based
optimizers such as ADAM are directly impacted by the barren plateau phenomenon [51] in which the gradient ∇ L(θ) of
 vanishes exponentially in the number
the loss function L(θ)
of qubits. To a lesser extent, gradient-free optimizers such as
COBYLA have been shown to be affected [52] by this phenomenon but this is highly dependent on the specific setting
under study. A viable method to prevent the occurrence of
barren plateaus in VQE experiments utilizing gradient-based

123

(2025) 85:705

optimizers involves a special initialization of the parameters
as reported in [53]. The factors inducing the occurrences of
barren plateaus, ranging from the effects of the loss function, the form of the ansatzes, to the presence of noise, are
an active area of research whose results have been reported
in recent works such as [51,54–56]. Furthermore, depending
 and the structure
on the complexity of the cost function L(θ)
of quantum circuit ansatzes, multiple local minima might
exist and could cause the optimization to be stuck. This is a
prevalent problem that affects all types of optimizers, especially when the number of parameters to be optimized is high.
While these issues can negatively impact the training process
in VQE experiments generally, they are not of too much concern for us, since our VQE experiments involve a noiseless
quantum simulator as well as shallow quantum circuits with
small number of parameters, similar to the case in [16].
3.3.2 Optimizer selection
To make an informed choice of the eventual optimizers to
be used in our VQE experiments, we will perform several
experiments to check the performances of all six optimizers
using some of the ansatzes introduced in Sect. 3.1 within
the setting of the SU (2) matrix model. For these experiments, we use the 64 × 64 Hamiltonian at Fock cutoff  = 2
=2 with the exact ground
at weak coupling λ = 0.2, Hλ=0.2
state energy E exact = 3.14808, and four quantum circuit
ansatzes, effsu2_Ry_f, effsu2_RyRz_f, tl_Ry_f
and tl_RyRz_f. For each of the ansatzes, six VQE experiments will be run using the six optimizers SPSA, COBYLA,
NELDER-MEAD, L-BFGS-B, SLSQP, ADAM. Most of
these optimizers, except SPSA, automatically end the optimization process when convergence is reached. The results
are listed in Table 3 and the convergence curves are shown
in Fig. 5.
Using Table 3 and Fig. 5, the clear trends that emerged
from the VQE experiments involving the six optimizers are
the following.
• Three of the gradient-based optimizers (SLSQP, LBFGS-B, ADAM) performed extremely poorly in the
sense that no parameters update occurred and the optimization process was terminated after fewer than 40 iterations (corresponding to the fact that the convergence
curves were just short straight lines (colored pink, purple, orange) coinciding with one another in Fig. 6, which
is a zoomed in version of Fig. 5) showing only the first
45 iterations.
• The gradient-free optimizers SPSA, COBYLA,
NELDER-MEAD performed much better than the
gradient-based optimizers with convergences reached,
albeit at different values for different optimizers. Among
the three, NELDER-MEAD is the worst performer, with

Eur. Phys. J. C

(2025) 85:705

Page 15 of 80

705

=2 and six optimizers SPSA, COBYLA, NELDERTable 3 Results of the 24 VQE experiments involving the  = 2, λ = 0.2 Hamiltonian Hλ=0.2
MEAD, L-BFGS-B, SLSQP, ADAM with four ansatzes effsu2_Ry_f, effsu2_RyRz_f, tl_Ry_f and tl_RyRz_f

Ansatz

SPSA

COBYLA

NELDER-MEAD

SLSQP

L-BFGS-B

ADAM

effsu2_Ry_f

3.15449

3.15918

3.38867

6.08574

6.08574

6.08574

effsu2_RyRz_f

3.15020

3.16211

4.17441

6.03906

6.03906

6.03906

tl_Ry_f

3.14902

3.14785

3.22715

6.20488

6.20488

6.20488

tl_RyRz_f

3.15371

3.16211

5.24121

7.28477

7.28477

7.28477

convergence values far above the correct ones. COBYLA
and SPSA consistently yielded results at convergence that
are quite close to the exact values.
Based on the results shown in Table 3 and Figs. 5, 6, we select
SPSA and COBYLA for all the VQE experiments carried out
in the main part of this work.
3.4 Overview of VQE experiments
In this section, we provide an overview of all the VQE
experiments that will be carried out in this work. With
all the components for VQE in place as described in the
previous sections, we update Fig. 1 to reflect our specific
choices of these VQE components in Fig. 7. There are 12
Hamiltonians Hλ in total corresponding to the three truncated SU (2) models (bosonic at Fock cutoff  = 2, 4
and supersymmetric at Fock cutoff  = 2) at four different couplings λ = 0.2, 0.5, 1.0, 2.0. For quantum circuit
ansatzes, we work with the 8 variants of EfficientSU2
in Table 1, the 8 variants TwoLocal in Table 2 and the
various variants of EvolvedOperatorAnsatz whose
construction are described in detail in later sections. The
problem-agnostic, or generic, ansatzes EfficientSU2,
TwoLocal are used in the bosonic models only, while the
tailored EvolvedOperatorAnsatz circuits are used in
both the bosonic and supersymmetric models. Two optimizers are used throughout: COBYLA and SPSA. Given these
parameters, each VQE experiment is uniquely specified by
the tuple of choices denoted as (Hamiltonian, ansatz, optimizer)11 where the Hamiltonian choice includes either Hλ
11 For example,
=2 , effsu2_Ry_c, COBYLA) corresponds to the VQE
• (Hλ=0.2
experiment involving the bosonic  = 2 model at coupling λ = 0.2
with the EfficientSU2 ansatz variant effsu2_Ry_c and
(S)=2
COBYLA optimizer. (Hλ=0.5
, ev_op_Hp15, SPSA) refers to
the VQE experiment involving the supersymmetric  = 2 model
at coupling λ = 0.5 with the EvolvedOperatorAnsatz variant ev_op_Hp15 with SPSA optimizer.
(=4
• (Hλ
, EfficientSU2&TwoLocal, COBYLA/SPSA) refers
to the VQE experiments involving the bosonic  = 4 model
at all couplings λ = 0.2, 0.5, 1.0, 2.0 with all the variants of
EfficientSU2 and all the variants of TwoLocal with both
COBYLA and SPSA optimizers.

(S)

or Hλ
corresponding to the bosonic or supersymmetric
SU (2) model at Fock cutoff  and coupling λ.
The total numbers of VQE experiments for each truncated
SU (2) matrix model are listed below.
1. Bosonic SU (2) at  = 2: At each coupling λ, there are
16 EfficientSU2 and TwoLocal ansatzes, together
with 9 EvolvedOperatorAnsatz variants, for a total
of 25 ansatz variants. Together with the usage of two optimizers (COBYLA & SPSA), there are 50 VQE experiments per λ. With 4 values of λ, we have 200 VQE experiments in total.
2. Bosonic SU (2) at  = 4: At each coupling λ, there are
16 EfficientSU2 and TwoLocal ansatzes, together
with 8 EvolvedOperatorAnsatz variants, for a total
of 24 ansatz variants, which lead to 48 VQE experiments
using either COBYLA or SPSA optimizer. With 4 values
of λ, this leads to 192 experiments.
3. Supersymmetric SU (2) at  = 2: At each coupling
λ, there are 12 EvolvedOperatorAnsatz variants
(EfficientSU2 and TwoLocal ansatzes are not used)
which lead to 24 VQE experiments using either COBYLA
or SPSA optimizer. With 4 values of λ, this leads to 96
experiments.
In the following sections, we present and discuss in detail
the results obtained from running the VQE experiments
involving the three SU (2) matrix models (bosonic models
at  = 2,  = 4 and supersymmetric model at  = 2)
using three different types of ansatzes and two different
types of optimizers. For each SU (2) model at four different couplings λ = 0.2, 0.5, 1.0, 2.0, we will highlight the
best results for each type of ansatzes and compare these best
results among one another, as well as among those reported
from [16] in order to benchmark the performances of our proposed ansatzes against the EfficientSU2 ansatzes used
in [16]. The full results for all experiments, together with the
(=4

• (Hλ
, EvolvedOperatorAnsatz, COBYLA/SPSA) refers
to the VQE experiments involving the bosonic  = 4 model
at all couplings λ = 0.2, 0.5, 1.0, 2.0 with all the variants of
EvolvedOperatorAnsatz with both COBYLA and SPSA
optimizers.

123

705

Page 16 of 80

Fig. 5 Convergence curves
from the VQE experiments
involving the SU (2) matrix
model at Fock cutoff  = 2 at
coupling λ = 0.2, using six
different optimizers SPSA,
COBYLA, NELDER-MEAD,
L-BFGS-B, SLSQP, ADAM for
four ansatzes: Clockwise from
left: effsu2_Ry_f,
effsu2_RyRz_f, tl_Ry_f
and tl_RyRz_f

Fig. 6 A zoomed-in version of
Fig. 5 showing only the first 45
iterations of the VQE
experiments. The convergence
curves of the gradient-based
optimizers SLSQP, L-BFGS-B,
ADAM are just straight lines
exactly coinciding with one
other, hence only the purple line
is visible in all 4 plots

123

Eur. Phys. J. C

(2025) 85:705

Eur. Phys. J. C

(2025) 85:705

Page 17 of 80

705

Fig. 7 The main components of VQE as selected in this work:
three types of quantum circuit ansatzes which include 8 variants
of EfficientSU2, 8 variants of TwoLocal for the bosonic
SU (2) model experiments and an unfixed number of variants of
EvolvedOperatorAnsatz depending on the SU (2) model, a quantum simulator called Estimator (state vector simulator with sam-

pling) to estimate the expectation value of the Hamiltonian, and two
different classical optimizers (COBYLA and SPSA). There are four
different Hamiltonians Hλ for each of the three SU (2) models, corresponding to the four couplings λ = 0.2, 0.5, 1.0, 2.0, for a total of 12
Hamiltonians

corresponding convergence curves for the energy of each of
the ansatzes will be included as supplementary materials in
the Appendix, since the these are not necessary for the qualitative discussion in the main text. Due to the presence of
numerous Tables and Figures, we summarize the structure of
our results in Table 4.

operators IXXIXX, XIXXIX, XXIXXI accounting for the
interaction part (the off-diagonal components) in the  = 2
Hamiltonian increase in values from −0.05 to −0.5.
The exact energies at the four couplings, obtained by diagonalization, are
=2
= 3.14808,
E λ=0.2

=2
= 3.69722,
E λ=1.0

=2
E λ=0.5
= 3.36254,
=2
E λ=2.0
= 4.26795.

(44)

4  = 2 bosonic model
4.1 EfficientSU2 & TwoLocal
The Hamiltonian for the SU (2) bosonic matrix model at  =
2 cutoff is a 26 ×26 or 64×64 matrix that can be expressed as a
sum of 10 Pauli string operators whose coefficients change at
different couplings λ. The list of the 10 Pauli string operators
and their coefficients are shown in Table 5.
The exact form of the Hamiltonian Hλ=2 at any of the
four couplings λ can be read off from the correct λ column
=2
of Table 5. For example, at λ = 0.2, the Hamiltonian Hλ=0.2
is
=2
Hλ=0.2
= 6.15IIIIII − 0.5 (IIIIIZ + IIIIZI + IIIZII

+IIZIII + ZIIIII + IZIIII)
− 0.05 (IXXIXX + XIXXIX + XXIXXI) . (43)
Going from the weak coupling regime at λ = 0.2, 0.5 to the
strong coupling regime at λ = 1.0, 2.0, the first 7 rows of
Table 5 corresponding to the diagonal operators of the  = 2
Hamiltonian do not change their coefficients, while the three

The 16 variants of the depth-1 (d = 1) EfficientSU2 and
TwoLocal quantum circuits used in this problem, implemented with n Q = 6 qubits, have the exact forms as those
shown in Figs. 2 and 3. Depending on the rotation gates and
the entanglement pattern, the numbers of parameters due to
these structures are
⎧
⎪
⎨(d + 1)n Q = 12, (RY , R Z , RY Y )
Rotation :
⎪
⎩
2(d + 1)n Q = 24, (RY R Z )
⎧
⎪
(circular)
⎨n Q = 6
Q −1
Entanglement : n 
⎪
k = 21 n Q (n Q − 1) = 15 (full)
⎩
k=1

Table 6 recaps the structure of all 16 ansatz variants and lists
their numbers of parameters. Variant-wise, EfficientSU2

123

705

Page 18 of 80

Eur. Phys. J. C

Table 4 An overview of the tables and figures containing the
main results for all VQE experiments run in this work for
the three types of quantum circuit ansatzes (EfficientSU2,
TwoLocal, EvolvedOperatorAnsatz) at 4 different couplings
λ = 0.2, 0.5, 1.0, 2.0 for the cases of  = 2,  = 4 bosonic and
 = 2 supersymmetric SU (2) matrix model. For each of the three
SU (2) models, the main results include a summary table listing only
the best result from each type of optimizers for each type of ansatzes
(EfficientSU2/TwoLocal are counted together), the plots showSU (2) Model

Ansatz

=2
(Bosonic)
Section 4

=2
(BMN)
Section 6

Table 5 The 10 Pauli string
operators forming the SU (2)
matrix model Hamiltonians at
four couplings
λ = 0.2, 0.5, 1.0, 2.0

123

Supplementary results

Table 21 Table 22 Table 23 Table 24
(F-S)
(F-S)
(F-S)
(F-S)
Fig. 16 Fig. 17 Fig. 18 Fig. 19
(CC)
(CC)
(CC)
(CC)

Table 7
Fig. 8

Table 9
Fig. 11

EvolvedOperator
Table 8

=4
(Bosonic)
Section 5

ing the comparisons of all variants within the ansatz type considered,
and a table containing best overall results for all ansatzes (including
the ones reported in [16]). The supplementary results for each model
include the four tables (labeled F-S for Full-Supplementary) listing the
full results for all ansatz variants at each coupling λ, and the convergence curve plots (labeled CC for Convergence Curves) of all variants.
All tables with the F-S label and figures with the CC label are supplementary material included in the Appendix

Main results

EfficientSU2
Table 1
TwoLocal
Table 2

Table 25 Table 26 Table 27 Table 28
(F-S)
(F-S)
(F-S)
(F-S)

Best overall results:
Table 10

Table 13
Fig. 13

EfficientSU2
Table 1
TwoLocal
Table 2

Fig. 20 (CC), Fig. 21 (CC)

Table 29 Table 30 Table 31 Table 32
(F-S)
(F-S)
(F-S)
(F-S)
Fig. 22 Fig. 23 Fig. 24 Fig. 25
(CC)
(CC)
(CC)
(CC)

Table 15
Fig. 14

EvolvedOperator
Table 14

(2025) 85:705

Best overall results:
Table 16

Table 33 Table 33 Table 35 Table 36
(F-S)
(F-S)
(F-S)
(F-S)
Fig. 26 (CC)

Table 19
Fig. 15

Table 37 Table 38 Table 39 Table 40
(F-S)
(F-S)
(F-S)
(F-S)

Best overall results:
Table 20

Fig. 27, Figs.28, 29, 30, 31 (CC)

EvolvedOperator
Table 18

Operator

λ = 0.2

λ = 0.5

λ = 1.0

λ = 2.0

IIIIII

6.15

6.375

6.75

7.5

IIIIIZ

−0.5

−0.5

−0.5

−0.5

IIIIZI

−0.5

−0.5

−0.5

−0.5

IIIZII

−0.5

−0.5

−0.5

−0.5

IIZIII

−0.5

−0.5

−0.5

−0.5

ZIIIII

−0.5

−0.5

−0.5

−0.5

IZIIII

−0.5

−0.5

−0.5

−0.5

IXXIXX

−0.05

−0.125

−0.25

−0.5

XIXXIX

−0.05

−0.125

−0.25

−0.5

XXIXXI

−0.05

−0.125

−0.25

−0.5

Eur. Phys. J. C

(2025) 85:705

circuits have the same parameters for both full and circular
entanglement patterns, since the entanglement part of these
circuits does not include any parameterized gates. On the
other hand, variant-wise, TwoLocal circuits whose entanglement part includes the parameterized C R X gate have
more parameters for the full entanglement than for the circular entanglement. The circuit with the largest number of
parameters is tl_RyRz_f.
The best results obtained by running the VQE experiments
COBYLA/SP
(Hλ=2 , EfficientSU2&TwoLocal,
SA) using the eight variants of EfficientSU2 and eight
variants of TwoLocal quantum circuits with COBYLA and
SPSA optimizers are summarized in Table 7, in which the
column ‘COBYLA’ lists the best performing ansatz, with its
associated energy, obtained with COBYLA optimizer, the
‘SPSA’ column lists the best ansatz and its associated energy
obtained using SPSA optimizer. The column ‘Full results’
lists the supplementary Tables/Figures (in the appendix) containing the full energy results for all 16 ansatzes together
with their convergence curves. The performances of all
EfficientSU2 and TwoLocal ansatzes for all four coupling values are shown in Fig. 8.
The main observations regarding the results are noted
below. Of particular importance for the analyses of the results
are the details concerning the best type of ansatzes, the overlap of the ansatzes with the true wavefunction and the performances of TwoLocal versus those of EfficientSU2.
1. Best ansatzes: For the set of VQE experiments (Hλ=2 ,
EfficientSU2&TwoLocal,
COBYLA/SPSA),
the best ansatz type is always TwoLocal, obtained
with COBYLA optimizer. At weak coupling (λ = 0.2),
TwoLocal ansatzes with full entanglement, tl_Ry_f,
perform best, while at stronger couplings (λ = 0.5, 1.0,
2.0), TwoLocal ansatzes with circular entanglement,
tl_Ry_c, perform best (Table 7). It is interesting to note
that EfficientSU2/TwoLocal variants with RY R Z
rotation block perform poorly compared to those with
RY , R Z , RY Y rotation block (see Fig. 8). Furthermore,
different optimizers yield different results for the same
quantum circuit ansatz used as obvious from Fig. 8, where
different data points corresponding to either COBYLA or
SPSA are observed for the same ansatz.
2. Overlaps with the exact ground state:
• At λ = 0.2 (see Fig. 8, first row, left subfigure), there
is a close overlap of the majority of ansatzes with
the exact energy such as effsu2_Rz_f, tl_Ry_c,
tl_RyY_c, tl_Ry_f, tl_Rz_f, tl_RyY_f
(using SPSA), and tl_Ry_c, tl_Ry_f, tl_RyY_f
(using COBYLA).
• At λ = 0.5 (see Fig. 8, first row, right subfigure), there
is no overlap between any ansatz using SPSA opti-

Page 19 of 80

705

mizer, but some close overlap for several ansatzes such
as tl_Ry_c, tl_RyY_c, tl_Ry_f, tl_RyY_f
using COBYLA optimizer.
• At λ = 1.0, 2.0 (Fig. 8, second row, left and right
subfigures), with either optimizer, all ansatzes yielded
values far above the correct energy value. This trend
of the results obtained at weak couplings being more
accurate than those at strong couplings is indicative of the fact that the problem-agnostic, generic
EfficientSU2 and TwoLocal quantum circuit
ansatzes used have more overlap with the actual wavefunction at weak couplings than those at strong couplings. This observation was already made in the work
[16].
3. Effect of circuit depths: For the λ = 2.0 case, since there
is no overlap of the depth-1 circuits used with the exact
ground state wavefunction, we performed some additional
VQE experiments involving deeper versions of the 16
ansatzes to determine whether more parameters would
lead to better performance. Our results, plotted in Fig.
9 indicate that increasing the depths of the circuits does
not lead to better results, as we obtained mostly similar or worse results with the depth-2 and depth-3 versions of all 16 circuits. Each subfigure of Fig. 9 shows
the results of the VQE experiments involving a particular
combination of ansatzes and optimizer, clockwise from
the top left, we have the 8 variants of depth-1, depth2, depth-3 EfficientSU2 used with COBYLA optimizer, followed by the same EfficientSU2 circuits
used with SPSA optimizer, followed by the 8 variants of
depth-1, depth-2, depth-3 TwoLocal used with SPSA
optimizer, followed by the same TwoLocal circuits used
with COBYLA optimizer. In each of the subfigures, the
green line denoting the depth-1 circuits are almost always
closer to the exact energy than the blue and cyan lines
denoting depth-2 and depth-3 circuits.
4. TwoLocal versus EfficientSU2: Out of 64 comparisons made between the 8 variants of EfficientSU2
and the corresponding 8 variants of TwoLocal using 2
different optimizers at 4 different couplings, TwoLocal
quantum circuit ansatzes almost always outperform or at
least are on par with EfficientSU2 ansatzes of the
same variant, using either COBYLA or SPSA. This is evident from the convergence curve plots of Figs. 32, 33, 34,
35, 36, 37, 38, 39 in Sect. D.1 of the appendix, in which the
orange curve representing TwoLocal ansatzes always
converge at the same values as or at lower values than the
blue curve representing EfficientSU2 ansatzes. The
faster convergence and better performance of TwoLocal
ansatzes compared to their EfficientSU2 counterparts can probably be attributed to the fact that the lat-

123

705

Page 20 of 80

Eur. Phys. J. C

Table 6 VQE experiments
(Hλ=2 , EfficientSU2&
TwoLocal, COBYLA/SPSA):
The list of the 8 variants of
EfficientSU2 and 8 variants
of TwoLocal detailing their
structures and number of
parameters

Ansatz

Rotation block

effsu2_Ry_c
effsu2_Rz_c
effsu2_RyY_c
effsu2_RyRz_c

(2025) 85:705

Entanglement pattern

Number of parameters

RY
RZ
RY Y
RY R Z

circular

12
12
12
24

effsu2_Ry_f
effsu2_Rz_f
effsu2_RyY_f
effsu2_RyRz_f

RY
RZ
RY Y
RY R Z

full

12
12
12
24

tl_Ry_c
tl_Rz_c
tl_RyY_c
tl_RyRz_c

RY
RZ
RY Y
RY R Z

circular

18
18
18
30

tl_Ry_f
tl_Rz_f
tl_RyY_f
tl_RyRz_f

RY
RZ
RY Y
RY R Z

full

27
27
27
39

Table 7 VQE experiments (Hλ=2 , EfficientSU2&TwoLocal,
COBYLA/SPSA): summary of the best results for each of the optimizer
at the four couplings λ. See main text for the description of the columns.

The best results are noted in bold. (F-S) denotes Full-Supplementary,
and CC denotes ‘Convergence Curves’. Tables with the label (F-S) and
figures with the label (CC) can be found in Sect. A.1 in the appendix

Coupling

Exact

COBYLA

SPSA

Full results

λ = 0.2

3.14808

3.14844
tl_Ry_f

3.14941
tl_Ry_c

Table 21 (F-S)
Fig. 16(CC)

λ = 0.5

3.36254

3.36475
tl_Ry_c

3.37207
tl_Ry_c

Table 22(F-S)
Fig. 17(CC)

λ = 1.0

3.69722

3.7373
tl_Ry_c

3.74316
effsu2_Ry_f

Table 23(F-S)
Fig. 18(CC)

λ = 2.0

4.26795

4.41895
tl_Ry_c

4.48535
tl_Ry_c

Table 24(F-S)
Fig. 19(CC)

ter contain the parameterized entanglement block that
enhances their expressivity while the former do not.
5. A peculiar trend to note is that circuits involving R Z
in the rotation blocks of either type (EfficientSU2
or TwoLocal) have flat convergence curve with almost
no variations (using COBYLA) or very few oscillations
(using SPSA) in values. This form of ansatz is almost
impervious to the variational process (especially using
COBYLA). Furthermore, at all couplings, the convergence curves are identical for EfficientSU2 and
TwoLocal circuits involving R Z rotation block (as evident from the complete overlap of these curves in Figs.
32, 33, 34, 35, 36, 37, 38, 39 in Sect. D.1).

Operator12 quantum circuits listed in Table 8. Out of these
eight ansatzes, only three quantum circuits (shown in Fig.10)
are unique, with the rest being the deeper versions of these.
In particular,
• ev_op_r uses three random Pauli string operators ZZIIII, IZIIZI, IXIXIX as building blocks. These operators
are random in the sense that they are not related to the
operators listed in Table 5 that make up the SU (2)  = 2
Hamiltonian.
• ev_op_H uses the 9 Pauli string operators listed in Table
5 as building blocks - These 9 operators make up almost
the entirety of the SU (2)  = 2 Hamiltonian matrix.
In selecting the operators for this ansatz, we could also
include the identity operator IIIIII, but that makes no difference in the VQE algorithm since the identity operator
cannot be parameterized.

4.2 EvolvedOperatorAnsatz
For the case of SU (2) bosonic matrix model at Fock cutoff  = 2, we construct the nine tailored Evolved

123

12 We

use the shortened form EvolvedOperator to refer to
EvolvedOperatorAnsatz occasionally in this paper since the
meaning is clear with little chance of confusion.

Eur. Phys. J. C

(2025) 85:705

Page 21 of 80

705

Fig. 8 VQE experiments (Hλ=2 , EfficientSU2&TwoLocal,
COBYLA/SPSA) – clockwise from top left λ = 0.2, λ = 0.5, λ = 2.0,
λ = 1.0: comparison of the 8 variants of EfficientSU2 and 8 vari-

ants TwoLocal ansatzes at each λ. The data points in each of the 4
subfigures above are generated from the full results included in Tables
21, 22, 23, 24 found in the appendix (Sect. A.1)

• ev_op_Hp uses the 5 Pauli string operators IIIIIZ,
IIIZII, IXXIXX, IZIIII, XIXXIX as building blocks –
these 5 operators are a subset of the 9 operators used in
ev_op_H.

The best results obtained by running the VQE experiments
(Hλ=2 , EvolvedOperatorAnsatz, COBYLA/SPSA)
using the nine variants of EvolvedOperatorAnsatz
from Table 8 with COBYLA and SPSA optimizers are summarized in Table 9. Similar in structure to Table 7, the column ‘COBYLA’ lists the best performing ansatz obtained

All nine ansatzes with their structures and corresponding
numbers of parameters are listed in Table 8.

123

705

Page 22 of 80

Eur. Phys. J. C

EfficientSU2 circuits with SPSA optimizer, 8 variants of depth1, depth-2, depth-3 TwoLocal circuits with SPSA optimizer, same
TwoLocal circuits with COBYLA optimizer. A noticeable trend is
that deeper circuits have comparable or even worse performances compared to the depth-1 version

Fig. 9 Comparison of the energy results for the VQE experiments
=2 using depth-1, depth-2 and depth-3 EfficientSU2
involving Hλ=2.0
and TwoLocal quantum circuits, with COBYLA and SPSA optimizers. Clockwise from top left: 8 variants of depth-1, depth-2,
depth-3 EfficientSU2 circuits with COBYLA optimizer, same

Table 8 The list of all
EvolvedOperatorAnsatz
circuit variants used for the
VQE experiments (Hλ=2 ,
EvolvedOperatorAnsatz,
COBYLA & SPSA)

123

(2025) 85:705

Ansatz

Parameters

Operators

ev_op_r

3

ev_op_H

9

[ZZIIII, IZIIZI, IXIXIX]
⎛
⎞
IIIIIZ,
IIIIZI, IIIZII,
⎝ IIZIII, IXXIXX, IZIIII,⎠
XIXXIX, XXIXXI, ZIIIII

ev_op_Hp

5

[IIIIIZ, IIIZII, IXXIXX, IZIIII, XIXXIX]

ev_op_r3

9

Depth-3 version of ev_op_r

ev_op_H_2f

18

Depth-2 version of ev_op_H

ev_op_H_3f

27

Depth-3 version of ev_op_H

ev_op_Hp2

10

Depth-2 version of ev_op_Hp

ev_op_Hp3

15

Depth-3 version of ev_op_Hp

ev_op_Hp4

20

Depth-4 version of ev_op_Hp

Eur. Phys. J. C

(2025) 85:705

Page 23 of 80

705

Fig. 10 The three unique depth-1 EvolvedOperator quantum circuits from Table 8

when using COBYLA optimizer, the column ‘SPSA’ lists
the best ansatz obtained when using SPSA optimizer. The
last column lists the supplementary Tables containing the
full results (all of which can be found in the appendix, Sect.
A.2). Furthermore, Fig. 11 shows the performances of all
nine EvolvedOperatorAnsatz circuits at all four couplings.
• Best ansatzes: For the VQE experiments (Hλ=2 ,
EvolvedOperatorAnsatz, COBYLA & SPSA) at
all four couplings, conforming to expectations, the best
performing ansatzes are almost always those quantum
circuits comprising operators that are part of the  = 2
Hamiltonian (either the 9-operator or the 5-operator variants), and not the ones formed by random operators. The
only exception is the case of λ = 0.2, with the best
performing ansatz being ev_op_r3, the depth-3 version of ev_op_r (Fig. 10a) – the variant containing 3
random operators.13 At λ = 0.5 and λ = 2.0, the best
ansatz variant is ev_op_H_2f, the depth-2 version of
ev_op_H (Fig. 10c) containing 9 operators making up
13 At λ = 0.2, ev_op_r3 and ev_op_Hp4 obtained the same results

of 3.14844, but ev_op_r3 has only 9 parameters versus the 20 parameters of ev_op_Hp4, making it the better variant, since a more performing variant is always one with fewer parameters.

the SU (2) Hamiltonian. At λ = 1.0, the best variant
is ev_op_Hp4, the depth-4 version of ev_op_Hp containing 5 operators making up the Hamiltonian (Fig. 10b)
• Overlaps with the exact ground state:
– At λ = 0.2 (Fig. 11, first row, left subfigure), all
depth-1 unique circuits used with SPSA, together
with ev_op_Hp4 used with COBYLA, have good
overlaps with the exact wavefunction.
– At λ = 0.5 (Fig. 11, first row, right subfigure),
only ev_op_H_2f and ev_op_H_3f used with
COBYLA have some close overlaps with the exact
wavefunction.
– At λ = 1.0 (Fig. 11, second row, left subfigure), only
ev_op_Hp4 used with COBYLA has a relatively
close overlap with the ground state.
– At λ = 2.0 (Fig. 11, second row, right subfigure), several variants (including ev_op_H, ev_op_H_2f and
ev_op_H_3f used with either COBYLA or SPSA)
have relatively close overlaps with the exact ground
state.
– Despite the fact that none of the ansatzes have
truly good overlaps with the exact ground state at
strong couplings λ = 1.0, 2.0, these overlaps of
the EvolvedOperatorAnsatz circuits considered in this section with the ground state are still

123

705

Page 24 of 80

Eur. Phys. J. C

Table 9 VQE experiments (Hλ=2 , EvolvedOperatorAnsatz,
COBYLA/ SPSA): summary of the best results for each type of optimizers at the four couplings λ. See the main text for the description
of the columns. The best results are noted in bold. (F-S) denotes Full-

(2025) 85:705

Supplementary. Tables with the label (F-S) can be found in the appendix
(Sect. A.2). The convergence curves for this set of VQE experiments
are plotted in Fig. 20 for COBYLA optimizer and Fig. 21 for SPSA
optimizer (Sect. A.2)

Coupling

Exact

COBYLA

SPSA

Full results

λ = 0.2

3.14808

3.14844
ev_op_Hp4

3.14844
ev_op_r3

Table 25(F-S)

λ = 0.5

3.36254

3.36328
ev_op_H_2f

3.36719
ev_op_Hp3

Table 26(F-S)

λ = 1.0

3.69722

3.70508
ev_op_Hp4

3.72266
ev_op_Hp2

Table 27(F-S)

λ = 2.0

4.26795

4.28906
ev_op_H_2f

4.30664
ev_op_H_2f

Table 28(F-S)

significantly better than those of EfficientSU2
and TwoLocal ansatzes in the previous section,
as evident by comparing the top left and top right
subfigures in Fig. 11 with the corresponding ones
in Fig. 8. This is indicative of a better approximation to the true wavefunction using the tailored
EvolvedOperatorAnsatz circuits.
4.3 Comparison of all quantum circuits
In this section, we collect the best results obtained by running the VQE experiments with the three different types of
ansatzes and two different types of optimizers in Table 10.
For reference and later as benchmarks, we also include the
best results reported in [16], obtained by using the depth-3
EfficientSU2 quantum circuits with the rotation block
being RY (for all couplings) with different optimizers. As
the circuits of [16] are all depth 3 (d = 3), the numbers
of parameters are (d + 1)n Q = 24 for the RY variational
form and 2(d + 1)n Q = 48 for the RY R Z variational form.
Each entry in the first three rows of Table 10 is a tuple (E,
ansatz, number of parameters, optimizer) listing the energy
at convergence, the ansatz variant, the number of parameters
in the ansatz, and the optimizer used to obtain the result. The
entries in the second last row corresponding to the results of
[16] have a slightly different format, (E, number of parameters, optimizer), in which the ansatz is not listed, since the
authors of [16] exclusively used depth-3 EfficientSU2
circuits with RY rotation block for these experiments.
1. Within this work, among the three types of quantum
circuits used, the tailored EvolvedOperator circuits emerged as the best performing type of ansatzes
for all four couplings λ = 0.2, 0.5, 1.0, 2.0, followed
by the TwoLocal quantum circuits and finally by
EfficientSU2
quantum
circuits.
Among
EfficientSU2 and TwoLocal, an interesting trend
to note is the better performance of variants with circular

123

entanglement pattern compared to those with full entanglement pattern, as three out of four best variants of either
EfficientSU2 or TwoLocal have circular entanglement pattern.
2. Including the results of [16] as benchmarks (the second
last row of Table 10), EvolvedOperatorAnsatz circuits still emerged as the best performers. In particular, for the cases of λ = 0.2, 0.5, both TwoLocal and
EvolvedOperatorAnsatz variants yielded better
results than [16], while for the cases of λ = 1.0, 2.0, only
EvolvedOperatorAnsatz circuits achieved better
results than [16]. It is also noteworthy that in all four
instances, EvolvedOperatorAnsatz, with at most
20 parameters, outperformed EfficientSU2 with 24
parameters.

5  = 4 bosonic model
For the case of SU (2) bosonic matrix model at Fock cutoff
 = 4, the Hamiltonian is a 212 ×212 , or 4096×4096 matrix.
When expressed as a sum of Pauli operator strings, the final
expression contains 895 terms and can be downloaded as a
text file which is available at this GitHub link [57], since it
is too long to be included in full here. The exact energies by
diagonalization for the four Hamiltonians at different couplings are:
E λ=0.2 = 3.13406,

E λ=0.5 = 3.29894,

E λ=1.0 = 3.52625,

E λ=2.0 = 3.89548 .

(45)

In Table 11, we list the 40 largest operators (by absolute
values) and their coefficients for the  = 4 Hamiltonian at
four different couplings λ = 0.2, 0.5, 1.0, 2.0. These operators correspond to the vertical green lines in Fig. 12 which
shows graphically the magnitudes of the coefficients of all
895 operators for each of the 4 couplings. In Table 11, Group
(E), Group (G) and Group (C) operators, which are Pauli
strings made of the tensor products of the various combi-

Eur. Phys. J. C

(2025) 85:705

Page 25 of 80

705

Fig. 11 Bosonic SU (2) matrix model at Fock cutoff  = 2 at different couplings (clockwise from top left λ = 0.2, λ = 0.5, λ = 2.0,
λ = 1.0): comparison of all EvolvedOperatorAnsatz quantum

circuit ansatzes at each λ. The data points in the four subfigures above
are from the Tables 25, 26, 27, 28 in Sect. A.2 in the appendix

nations of the identity matrix and Pauli ‘Z’ matrix, account
partly for the diagonal components of the  = 4 Hamiltonian. The remaining operators, from Group (A) to Group
(K), which are Pauli strings made of tensor products of various combinations of the identity matrix with the Pauli ‘X’,
‘Y’ matrices, account partly for the interaction part, or the
off-diagonal components, of the  = 4 Hamiltonian.

this case are
Rotation :

⎧
⎪
⎨(d + 1)n Q = 24,

(RY , R Z , RY Y )

⎪
⎩

2(d + 1)n Q = 48, (RY R Z )
⎧
⎪
(circular)
⎨n Q = 12
n
−1
Q
Entanglement :

⎪
k = 21 n Q (n Q − 1) = 66 (full)
⎩
k=1

5.1 EfficientSU2 & TwoLocal
We use the same 8 variants of the depth-1 EfficientSU2
and 8 variants of the depth-1 TwoLocal quantum circuit
ansatzes as in the case of  = 2, but now each circuit consists
of n Q = 12 qubits instead of n Q = 6 qubits. The numbers
of parameters due to the rotation and entanglement parts for

Table 12 recaps the structure of the 16 ansatz variants and
lists their numbers of parameters. As already noted in the
case of  = 2, EfficientSU2 circuits have the same
parameters for both full and circular entanglement patterns
(variant-wise), since the entanglement part of these circuits
does not include any parameterized gates. On the other hand,
variant-wise, TwoLocal circuits whose entanglement part
includes the parameterized C R X gate have more parame-

123

705

Page 26 of 80

Eur. Phys. J. C

Table 10 VQE experiments involving  = 2 bosonic SU (2) matrix
model: Summary of the best results from each type of ansatzes
(EfficientSU2, TwoLocal, EvolvedOperatorAnsatz)
obtained from this work, as well as those reported in [16], at dif-

(2025) 85:705

ferent couplings λ for SU (2) matrix model at cutoff  = 2. The
absolute best results obtained from comparing all results in this table
are noted in bold

Ansatz type

λ = 0.2

λ = 0.5

λ = 1.0

λ = 2.0

EfficientSU2

3.14980
effsu2_Rz_c
(12 params)
COBYLA/SPSA

3.36963
effsu2_RyRz_c
(24 params)
COBYLA

3.74902
effsu2_Rz_c
(12 params)
COBYLA/SPSA

4.45508
effsu2_RyRz_f
(24 params)
COBYLA

TwoLocal

3.14844
tl_Ry_f
(27 params)
COBYLA

3.36475
tl_Ry_c
(18 params)
COBYLA

3.73730
tl_Ry_c
(18 params)
COBYLA

4.41895
tl_Ry_c
(18 params)
COBYLA

EvolvedOperator

3.14844
ev_op_r3
(9 params)
COBYLA

3.36328
ev_op_H_2f
(18 params)
COBYLA

3.70508
ev_op_Hp4
(20 params)
COBYLA

4.28906
ev_op_Hp_2f
(18 params)
COBYLA

Results from [16]
EfficientSU2
RY (depth 3)

3.14897
(24 params)
NELDER-MEAD

3.36675
(24 params)
SLSQP

3.71463
(24 params)
COBYLA

4.33636
(24 params)
SLSQP

Exact energy

3.14808

3.36254

3.69722

4.26795

ters for the full entanglement than for the circular entanglement. The circuit with the largest number of parameters is
tl_RyRz_f with 114 parameters.
The best results obtained by running the VQE experiments
(Hλ=4 , EfficientSU2&TwoLocal, COBYLA/SPSA)
using the 8 variants of EfficientSU2 and 8 variants
of TwoLocal quantum circuits with COBYLA and SPSA
optimizers are summarized in Table 13, in which the column ‘COBYLA’ lists the best performing ansatz (at each
coupling) together with the associated energy E obtained
by using COBYLA optimizer, the column ‘SPSA’ lists
the best ansatz with the associated E obtained by using
SPSA optimizer. The column ‘Full results’ lists the supplementary tables/figures (in the appendix) containing the full
energy results for all 16 ansatzes together with their convergence curves. The performances of all EfficientSU2 and
TwoLocal ansatzes for all four coupling values are shown
in Fig. 13.
The main observations regarding the results are noted
below. Trends concerning the best ansatzes, the overlap of the
ansatzes with the true wavefunction, and the performances of
TwoLocal versus those of EfficientSU2 are the most
important details to note.

• Best ansatzes: The best performing ansatz for 2 out of
4 couplings (λ = 0.2, 2.0) is the TwoLocal variant
tl_RyY_c involving the RY Y rotation block with circular entanglement . For λ = 1.0, the best performing
ansatz is the TwoLocal variant tl_Ry_c with RY rotation block with circular entanglement. For λ = 0.5, the

123

best performing ansatz is tl_RyY_f with RY Y rotation
block and full entanglement (see Table 13).
• Overlaps with the true wavefunction:
– At λ = 0.2 (Fig. 13, first row, left subfigure), using
SPSA, many variants from both EfficientSU2
such
as
effsu2_Ry_c,
effsu2_Rz_c,
effsu2_RyY_c, effsu2_RyY_f, effsu2_
Rz_f, and TwoLocal such as tl_Ry_c, tl_Rz_c,
tl_RyY_c, tl_Ry_f, tl_Rz_f, tl_RyY_f have
good overlaps with the exact ground state.
– At λ = 0.5 (Fig. 13, first row, right subfigure), only
a few TwoLocal variants such as tl_Ry_c (with
COBYLA), tl_Ry_f and tl_RyY_f (with SPSA)
have good overlaps with the ground state.
– At λ = 1.0 (Fig. 13, second row, left subfigure), more TwoLocal ansatzes have good overlaps with the ground state, including tl_Ry_c with
COBYLA, tl_RyRz_c with SPSA, tl_RyY_c
and tl_Ry_f with COBYLA.
– At λ = 2.0 (Fig. 13, second row, right subfigure), the
only variant with good overlap is tl_RyY_c with
SPSA.
• Optimizer performances: For weak couplings λ =
0.2, 0.5, a wide range of fluctuations in the obtained E
values can be observed for the 8 variants of
EfficientSU2 with both COBYLA and SPSA, while
the 8 variants of TwoLocal show a much smaller
range of fluctuation with SPSA (and to a smaller extent,
COBYLA). For λ = 1.0, wider range of fluctuations
across all variants of EfficientSU2 (and to a smaller

Eur. Phys. J. C

(2025) 85:705

Page 27 of 80

Table 11 The largest 40 operators by absolute values for the  = 4
Hamiltonian for 4 couplings λ = 0.2, 0.5, 1.0, 2.0. The dashed lines
‘—’ refer to the absence of a particular operator in the set under consideration. For example, the 31 operators in groups from (A) to (F) are
λ = 0.2

705

common to all couplings, while the operators in group (G) are common
only to λ = 0.2, 0.5 and λ = 1.0 Hamiltonians (not present in the
λ = 2.0 case). The operators in group (J) are only present in λ = 1.0
and λ = 2.0 cases, etc
λ = 0.5

λ = 1.0

λ = 2.0

Group

Operator
IIIXYYIIIXIX

− 0.0901

−0.2253

−0.4506

−0.9012

(A)

IIIXIXIIXXIX

−0.0901

−0.2253

−0.4506

−0.9012

(B)

(C)

(D)

(E)

(F)

(G)

IIIXIXIIYYIX

− 0.0901

−0.2253

−0.4506

−0.9012

IXIIIXIXIIXX

− 0.0901

−0.2253

−0.4506

−0.9012

IIXIIIXIIIII

0.0933

0.2333

0.4665

0.9330

IIIIXIXIIIII

0.0933

0.2333

0.4665

0.9330

XIIIIIIIXIII

0.0933

0.2333

0.4665

0.9330

IIIIXIIIXIII

0.0933

0.2333

0.4665

0.9330

XIIIIIIIIIXI

0.0933

0.2333

0.4665

0.9330

IIXIIIIIIIXI

0.0933

0.2333

0.4665

0.9330

ZZIIIIIIIIII

−0.1500

−0.3750

−0.7500

−1.5000
−1.5000

IIZZIIIIIIII

−0.1500

−0.3750

−0.7500

IIIIZZIIIIII

-0.1500

−0.3750

−0.7500

−1.5000

IIIIIIZZIIII

−0.1500

−0.3750

−0.7500

−1.5000

IIIIIIIIZZII

−0.1500

−0.3750

−0.7500

−1.5000

IIIIIIIIIIZZ

−0.1500

−0.3750

−0.7500

−1.5000

IXIXIIIXIXII

−0.1741

−0.4353

−0.8705

−1.7410

IXIIIXIXIIIX

−0.1741

−0.4353

−0.8705

−1.7410

IIIXIXIIIXIX

−0.1741

−0.4353

−0.8705

−1.7410

ZIIIIIIIIIII

−1.1500

−1.3750

−1.7500

−2.5000

IIZIIIIIIIII

−1.1500

−1.3750

−1.7500

−2.5000

IIIIZIIIIIII

−1.1500

−1.3750

−1.7500

−2.5000

IIIIIIZIIIII

−1.1500

-1.3750

−1.7500

−2.5000

IIIIIIIIZIII

−1.1500

−1.3750

−1.7500

−2.5000

IIIIIIIIIIZI

−1.1500

−1.3750

−1.7500

−2.5000

XIIIIIIIIIII

0.2898

0.7244

1.4489

2.8978

IIXIIIIIIIII

0.2898

0.7244

1.4489

2.8978

IIIIXIIIIIII

0.2898

0.7244

1.4489

2.8978

IIIIIIXIIIII

0.2898

0.7244

1.4489

2.8978

IIIIIIIIXIII

0.2898

0.7244

1.4489

2.8978

IIIIIIIIIIXI

0.2898

0.7244

1.4489

2.8978

IZIIIIIIIIII

−0.5000

−0.5000

−0.5000

—

IIIZIIIIIIII

−0.5000

−0.5000

−0.5000

—

IIIIIZIIIIII

−0.5000

−0.5000

−0.5000

—

IIIIIIIZIIII

−0.5000

−0.5000

−0.5000

—

IIIIIIIIIZII

−0.5000

−0.5000

−0.5000

—
—

IIIIIIIIIIIZ

−0.5000

−0.5000

−0.5000

(H)

XXIXIIIXIXII

−0.0901

−0.2253

—

—

(I)

IXIIYYIXIIIX

−0.0901

−0.2253

—

− 0.9012

(J)

(K)

IXIIIXIXIIYY

−0.0901

−0.2253

—

− 0.9012

IIXXIXIIIXIX

—

—

− 0.4506

− 0.9012

IIYYIXIIIXIX

—

—

− 0.4506

− 0.9012

IIIXXXIIIXIX

—

—

− 0.4506

− 0.9012

IXXXIIIXIXII

—

—

—

− 0.9012

YYIIIXIXIIIX

—

—

—

− 0.9012

IXIIXXIXIIIX

—

—

—

− 0.9012

IXIIIXYYIIIX

—

—

—

− 0.9012

123

705

Page 28 of 80

Eur. Phys. J. C

Fig. 12 Graphical representations of the set of 895 Pauli string operators forming the  = 4 Hamiltonian for four couplings λ = 0.2 (first
row, left subfigure), λ = 0.5 (first row, right subfigure), λ = 1.0 (second row, left subfigure) and λ = 2.0 (second row, right subfigure). The
x-axis labels the operator index (the order of appearance of the operator

Table 12 VQE experiments
(Hλ=4 , EfficientSU2&
TwoLocal, COBYLA/SPSA):
the list of the 8 variants of
EfficientSU2 and 8 variants
of TwoLocal detailing their
structures and number of
parameters

123

(2025) 85:705

in the sum forming the Hamiltonian whose full expression is available
at [57]) ranging from 1 to 895, the y axis labels the operator coefficient.
The green vertical lines in each subfigures correspond to the 40 largest
operators (at each of the coupling λ) listed in Table 11

Ansatz

Rotation block

Entanglement pattern

Number of parameters

effsu2_Ry_c
effsu2_Rz_c
effsu2_RyY_c
effsu2_RyRz_c

RY
RZ
RY Y
RY R Z

Circular

24
24
24
48

effsu2_Ry_f
effsu2_Rz_f
effsu2_RyY_f
effsu2_RyRz_f

RY
RZ
RY Y
RY R Z

Full

24
24
24
48

tl_Ry_c
tl_Rz_c
tl_RyY_c
tl_RyRz_c

RY
RZ
RY Y
RY R Z

Circular

36
36
36
60

tl_Ry_f
tl_Rz_f
tl_RyY_f
tl_RyRz_f

RY
RZ
RY Y
RY R Z

Full

90
90
90
114

Eur. Phys. J. C

(2025) 85:705

Page 29 of 80

Table 13 VQE experiments (Hλ=4 , EfficientSU2&TwoLocal,
COBYLA & SPSA): summary of the best results for each of the coupling λ. See main text for the description of the columns. For each
row corresponding to a coupling λ, the best result (which is closest to

705

the exact energy) is noted in bold. (F-S) denotes Full-Supplementary,
and CC denotes ‘Convergence Curves’. Tables with the label (F-S) and
Figures with the label (CC) can be found in Sect. B.1 in the appendix

Coupling

Exact

COBYLA

SPSA

Full results

λ = 0.2

3.13406

3.1791
effsu2_Rz_c

3.13679
tl_RyY_c

Table 29(F-S)
Fig.22(CC)

λ = 0.5

3.29894

3.27478
tl_RyY_c

3.30641
tl_RyY_f

Table 30(F-S)
Fig.23(CC)

λ = 1.0

3.52625

3.53869
tl_Ry_c

3.55374
tl_RyRz_c

Table 31(F-S)
Fig.24 (CC)

λ = 2.0

3.89548

4.16062
tl_RyY_f

3.94466
tl_RyY_c

Table 32(F-S)
Fig.25(CC)

Fig. 13 Bosonic SU (2) matrix model at Fock cutoff  = 4 at different couplings (clockwise from top left λ = 0.2, λ = 0.5, λ = 2.0,
λ = 1.0): comparison of all EfficientSU2/TwoLocal ansatzes at

each λ with the y-axis zoomed in to the vicinity of the exact energy
value. The data points for each λ from the figure above are from Tables
29, 30, 31 and 32 found in the Appendix

123

705

Page 30 of 80

extent, TwoLocal) are seen with either optimizer. For
λ = 2.0, COBYLA optimizer yields a large range of fluctuation across all 16 ansatzes while SPSA has a relatively
better performance (see Fig. 13).
• TwoLocal versus EfficientSU2: Similar to the
 = 2 case above, out of the 64 comparisons made
between the 8 variants of TwoLocal and the corresponding 8 variants of EfficientSU2 at 4 different
couplings using 2 different optimizers, TwoLocal circuits consistently outperform EfficientSU2 using
either optimizer for all couplings. This is evident from the
convergence curve plots in Figs. 40, 41, 42, 43, 44, 45, 46,
47 (included in Sect. D.2 of the appendix) in which the
orange curves representing TwoLocal ansatzes almost
always converge faster and at values below the blue
curves representing EfficientSU2 ansatzes. The only
few exceptions to this are:
– the λ = 0.2 case with SPSA involving circuits
tl_RyRz_f and effsu2_RyRz_f with RY R Z
rotation blocks and full entanglement pattern (see Fig.
41).
– the λ = 1.0 case (see Fig. 45) with SPSA involving circuits with RY rotation block with circular
entanglement (tl_Ry_c & effsu2_Ry_c), and
RY Y rotation block with full entanglement pattern
(tl_RyY_f & effsu2_RyY_f).
– the λ = 2.0 case with SPSA involving circuits
tl_Ry_f and effsu2_Ry_f with RY rotation
block with full entanglement (see Fig. 47).
The fact that all of the exceptions above occur with SPSA
optimizer, which has a fixed number of iterations, and
not COBYLA optimizer, which has a variable number
of iterations might indicate that the observed exceptions
above are attributable to the optimizer performance rather
than the actual ansatz performance.
• The same peculiar trend noted in the  = 2 case is
observed here: Circuits involving R Z in the rotation block
of either EfficientSU2 or TwoLocal are almost
impervious to the variational process (especially using
COBYLA), as their convergence curves are practically
straight lines which overlap completely for the two types
of circuits (as can be seen from the complete overlap of
these curves in Figs. 40, 41, 42, 43, 44, 45, 46, 47).
5.2 EvolvedOperatorAnsatz
To build the tailored EvolvedOperatorAnsatz quantum circuits for the SU (2) bosonic matrix model at Fock
cutoff  = 4, we use the same approach as the  = 2 case
in which the quantum circuits are created by selecting a subset of operators that form the Hamiltonian to be the building
blocks. However, unlike the  = 2 case where the Hamil-

123

Eur. Phys. J. C

(2025) 85:705

tonian is only a 64 × 64 matrix and can be expressed as
the sum of only 10 Pauli string operators in which 9 out
of these 10 operators can be picked to build the tailored
EvolvedOperatorAnsatz circuits, the  = 4 Hammiltonian is a 4096 × 4096 matrix and is the sum of 895
Pauli string operators. It is out of the question to use all 895
operators or even a much smaller number of 100 operators to
build the tailored circuit, due to the exponentially slow running time of the VQE algorithms when dealing with circuits
of that size. Because of this setback, we will work with various smaller subsets, containing N = 15, 20, 25, 30 operators
chosen by the largest absolute values of their coefficients.
For each set of N operators (where N = 15, 20, 25, 30),
we created two EvolvedOperatorAnsatz quantum circuits, a depth-1 version and a depth-2 version. This led to
the eight quantum circuit ansatzes which are listed in Table
14. Note that for each coupling λ, the content of the set
of N largest operators is different, i.e. the set of N = 15
operators at λ = 0.2 (weak coupling), consisting of operators from Group (E)+ Group (G) + half of Group (F) in
Table 11, is not the same as the set of N = 15 operators
at λ = 2.0 (strong coupling), consisting of operators from
Group (F) + Group (E) + Group (D) in Table 11. This leads
to EvolvedOperatorAnsatz quantum circuits having
different building blocks at each coupling λ, although they
may have the same name. The specific building blocks for
each variant of the EvolvedOperatorAnsatz quantum
circuits are listed in full in Table 14.
The best results for each type of optimizers for  =
4 SU (2) matrix model at all four couplings are summarized in Table 15, which has the same format as previous sections. The column ‘COBYLA’/‘SPSA’ lists the
best ansatz and associated energy result obtained with
COBYLA/SPSA for each coupling. The performances of
all EvolvedOperatorAnsatz variants are visually presented in Fig. 14.
Some observations regarding the best ansatzes and the
overlaps of the ansatzes with the true ground state are noted
below.
• Best ansatzes: Rather contrary to the expectation that
performance should improve as more operators (forming the Hamiltonian) are added in the circuits, the best
performing quantum circuits are not those with the largest
number of operators. As can be seen from Table 15, the
best ansatz at each coupling is never ev_op_Hp30 or
its depth-2 version ev_op_Hp30_2f, which have the
largest number of operators out of all variants considered.
Instead, the best performing variant for λ = 0.2, 0.5, 1.0
is the one with 25 operators (the second-largest number of
operators), ev_op_Hp25_2f and ev_op_Hp25. For
λ = 2.0, it is ev_op_Hp15_2f (with 15 operators).
• Overlaps of the ansatzes with the exact ground state:

Eur. Phys. J. C

(2025) 85:705

Table 14 The list of eight
EvolvedOperatorAnsatz
quantum circuits used for
running the VQE for  = 4
Hamiltonian. In the
‘Description’ column, the
building blocks of each variant
is listed in the notation of Table
11, i.e. (A),…, (G) refer to the
Group (A),…, (G) to which
certain types of Pauli string
operators are labeled. The
fractions before some groups
mean that only those fractions
specified (and not all operators
from the groups) are selected.
The full list of operators for
each N at each coupling can be
found in the Jupyter
notebook available at this
GitHub link [58]

Page 31 of 80

Ansatz

Parameters

705

Description
Largest 15 operators
λ = 0.2 : (E) + (G) + 21 (F)
excl. [IIIIIIXIIIII, IIIIIIIIXIII, IIIIIIIIIIXI] in (F)

ev_op_Hp15

15

λ = 0.5 : (E) + (F) + 21 (G)
excl. [IZIIIIIIIIII, IIIIIIIIIZII, IIIIIIIIIIIZ] in (G)
λ = 1.0 : (E) + (F) + (D)
λ = 2.0 : (E) + (F) + (D)
Largest 20 operators
λ = 0.2 : (E) + (F) + (G) + (2/3)(D)
excl. IXIXIIIXIXII in (D)

ev_op_Hp20

20

λ = 0.5 : (E) + (F) + (G) + (2/3)(D)
excl. IXIXIIIXIXII in (D)
λ = 1.0 : (E) + (F) + (D) + (5/6)(C)
excl. IIZZIIIIIIII in (C)
λ = 2.0 : (E) + (F) + (D) + (5/6)(C)
excl. ZZIIIIIIIIII in (C)
Largest 25 operators
λ = 0.2 : (E) + (F) + (G) + (D) + (2/3)(C)
excl. [IIIIIIZZIIII, IIIIIIIIZZII] in (C)

ev_op_Hp25

25

λ = 0.5 : (E) + (F) + (G) + (D) + (2/3)(C)
excl. [IIIIIIZZIIII, IIIIIIIIZZII] in (C)
λ = 1.0 : (E) + (F) + (C) + (D) + (2/3)(G)
excl. [IZIIIIIIIIII, IIIIIIIIIZII] in (G)
λ = 2.0 : (E) + (F) + (C) + (D) + (2/3)(B)
excl. [IIXIIIXIIIII, XIIIIIIIXIII] in (B)
Largest 30 operators
λ = 0.2 : (E) + (F) + (G) + (D) + (C) + (1/2)(B)
excl. [IIXIIIXIIIII, IIIIXIXIIIII, XIIIIIIIXIII] in (B)

ev_op_Hp30

30

λ = 0.5 : (E) + (F) + (G) + (D) + (C) + (1/2)(B)
excl. [IIXIIIXIIIII, IIIIXIXIIIII, XIIIIIIIXIII] in (B)
λ = 1.0 : (E) + (F) + (C) + (D) + (G) + (1/2)(B)
excl. [IIXIIIXIIIII, XIIIIIIIXIII, IIIIXIIIXIII] in (B)
λ = 2.0 : (E) + (F) + (C) + (D) + (B) + (3/4)(A)
excl. IIIXYYIIIXIX in (A)

ev_op_Hp15_2f

30

Depth-2 version of ev_op_Hp15

ev_op_Hp20_2f

40

Depth-2 version of ev_op_Hp20

ev_op_Hp25_2f

50

Depth-2 version of ev_op_Hp25

ev_op_Hp30_2f

60

Depth-2 version of ev_op_Hp30

123

705

Page 32 of 80

Eur. Phys. J. C

Table 15 VQE experiments (Hλ=4 , EvolvedOperatorAnsatz,
COBYLA & SPSA): summary of the best results for each of
the optimizer at four couplings λ. See main text for the description of the columns. The best results are noted in bold. (F-S)

(2025) 85:705

denotes Full-Supplementary. Tables with the label (F-S) can be
found in the appendix. The convergence curves of the energy for all
EvolvedOperatorAnsatz can be found in Fig. 26

Coupling

Exact

COBYLA

SPSA

Full results

λ = 0.2

3.13406

3.15952
ev_op_Hp15_2f

3.13421
ev_op_Hp25_2f

Table 33 (F-S)

λ = 0.5

3.29894

3.29968
ev_op_Hp25

3.29896
ev_op_Hp25_2f

Table 34 (F-S)

λ = 1.0

3.52625

3.53512
ev_op_Hp25

3.54551
ev_op_Hp30

Table 35 (F-S)

λ = 2.0

3.89548

4.16425
ev_op_Hp20

3.93348
ev_op_Hp15_2f

Table 36 (F-S)

Fig. 14 Bosonic SU (2) matrix model at Fock cutoff  = 4 at different couplings (clockwise from top left λ = 0.2, λ = 0.5, λ = 2.0,
λ = 1.0): comparison of all EvolvedOperatorAnsatz quantum

123

circuit ansatzes. The data points for the 4 subfigures above are from the
Tables 33, 34, 35, 36 in Sect. B.2 of the appendix

Eur. Phys. J. C

(2025) 85:705

– At λ = 0.2 (Fig. 14, first row, left subfigure),
using SPSA, ev_op_Hp25, ev_op_Hp30 and
ev_op_Hp25_2f show good overlaps with the
exact ground state.
– At λ = 0.5 (Fig. 14, first row, right subfigure), multiple variants show good overlaps with the ground state,
including
ev_op_Hp20,
ev_op_Hp30,
ev_op_Hp20_2f, ev_op_Hp25_2f with SPSA,
and
ev_op_Hp25,
ev_op_Hp15_2f,
ev_op_Hp25_2f using COBYLA.
– At λ = 1.0 (Fig. 14, second row, left subfigure), only
ev_op_Hp30 with SPSA and ev_op_Hp25 with
COBYLA show good overlaps with the ground state.
– At λ = 2.0 (Fig. 14, second row, right subfigure),
the only variant with a good overlap with the ground
state is ev_op_H15_2f with SPSA.
• Optimizer performances: for all couplings, it is evident
that SPSA optimizer yields a more stable and accurate performance for all quantum circuits compared to
COBYLA as can be seen from Fig. 14 in which the
purple line representing the results obtained with SPSA
are almost always closer to the exact energy line than
the green line representing the results obtained with
COBYLA.
5.3 Comparison of all quantum circuits
In this section, we collect the best results obtained by running
the experiments with the three different types of ansatzes and
two different types of optimizers for the case of  = 4 in
Table 16. As was done in the  = 2 case, we also included
the best results reported from the work [16] in the second
last row of Table 16. These results were obtained by using
the L-BFGS-B optimizer and the depth-3 EfficientSU2
quantum circuits with the rotation block being RY (for λ =
0.5, 1, 0, 2.0) and RY R Z for λ = 0.2. This means that the
number of parameters in these circuits are (d +1)n Q = 48 for
the RY variational form and 2(d + 1)n Q = 96 for the RY R Z
variational form. Each entry in the first three rows of Table
16 is a tuple (E, ansatz, number of parameters, optimizer)
listing the best energy at convergence, the best ansatz variant,
the number of parameters in the ansatz, and the optimizer
used to obtain the result. The entries in the second last row
corresponding to the results of [16] has a slightly different
format, (E, rotation block, number of parameters, optimizer),
in which rotation block type used in the EfficientSU2
ansatz is listed, since the authors of [16] exclusively used
EfficientSU2 and no other types of ansatzes.
• Within this work, for all four couplings λ = 0.2, 0.5, 1.0,
2.0, the best quantum circuit ansatz type is Evolved
Operator,
followed
by
TwoLocal
and

Page 33 of 80

705

EfficientSU2 (see the first three rows of Table 16).
Among EfficientSU2 and TwoLocal, an interesting trend to note is the better performance of variants with
circular entanglement pattern compared to those with full
entanglement pattern, as three out of four best variants
of either EfficientSU2 or TwoLocal have circular
entanglement pattern. This trend was already noted in the
case of bosonic SU (2) model at  = 2 in Sect. 4.3.
• Using as benchmarks the best results reported in the work
[16], our results are really competitive. In particular, for
the λ = 0.2, 05 cases, both TwoLocal (at 3.13679
& 3.30641 for λ = 0.2 and λ = 0.5, respectively)
and EvolvedOperatorAnsatz circuits (3.13421 &
3.29896, respectively) yield better results than [16]
(at 3.13705 & 3.30869, respectively). For the case of
λ = 1.0, only EvolvedOperatorAnsatz circuit (at
3.53512) yields a better result than [16] (at 3.54748).
For the case of λ = 2.0, our best result, which was
obtained by an EvolvedOperator ansatz at 3.93348
is the same as that obtained by [16], but our ansatz has
only 30 parameters in contrast to the 48 parameters of
the depth-3 EfficientSU2 circuit used by [16].

6  = 2 supersymmetric model
The Hamiltonian for the SU (2) supersymmetric matrix
model at Fock cutoff  = 2 is a 29 × 29 matrix with the
following exact energies obtained by diagonalization
E λ=0.2 = 0.003287,

E λ=0.5 = 0.01690,

E λ=1.0 = 0.04829,

E λ=2.0 = 0.08385 .

(46)

At each coupling λ, the 29 × 29 Hamiltonian can be written
as the sum of 25 Pauli string operators as shown in Table 17.
Operators in Group (A) are all those contributing to the diagonal elements of the Hamiltonian, and are the tensor products of the identity ‘I’ and Pauli ‘Z’ operators. Their values
remain unchanged as the coupling constant λ varies. Operators in Group (B) and (C) , which are the tensor products of
various combinations of the identity, Pauli ‘X’ and Pauli ‘Y’
operators, are those contributing to the interaction part, or the
off-diagonal components, of the Hamiltonian. Their values
steadily increase as the coupling constant λ varies from weak
(λ = 0.2) to strong (λ=2.0). At λ = 2.0, the values of these
off-diagonal operators reach the maximum values are equal
to those in Group (A).
From Table 17, the supersymmetric  = 2 Hamiltonian
at any of the four couplings λ can be read off using the corresponding column for λ. For example, the Hamiltonian at
λ = 0.5 reads

123

705

Page 34 of 80

Eur. Phys. J. C

Table 16 VQE experiments involving  = 4 bosonic SU (2)
matrix model: summary of the best results from the three
types of quantum circuit ansatzes (EfficientSU2, TwoLocal,
EvolvedOperatorAnsatz) from this work, as well as those

(2025) 85:705

reported in [16], at different couplings for SU (2) matrix model at cutoff
 = 4. The absolute best results obtained by comparing all ansatzes
from our work and those from [16] are noted in bold

Ansatz type

λ = 0.2

λ = 0.5

λ = 1.0

λ = 2.0

EfficientSU2

3.14605
effsu2_RyY_c
(24 params)
SPSA

3.44775
effsu2_Rz_c
(24 params)
COBYLA/SPSA

3.89550
effsu2_Rz_c
(24 params)
COBYLA/SPSA

4.20670
effsu2_Ry_f
(24 params)
SPSA

TwoLocal

3.13679
tl_RyY_c
(36 params)
SPSA

3.30641
tl_RyY_f
(90 params)
SPSA

3.53869
tl_Ry_c
(36 params)
COBYLA

3.94466
tl_RyY_c
(36 params)
SPSA

EvolvedOperator

3.13421
ev_op_Hp25_2f
(50 params)
SPSA

3.29896
ev_op_Hp25_2f
(50 params)
SPSA

3.53512
ev_op_Hp25
(25 params)
COBYLA

3.93348
ev_op_Hp15_2f
(30 params)
SPSA

Results from [16]
EfficientSU2
(depth-3)

3.13705
RY R Z
(96 params)
L-BFGS-B

3.30869
RY (48 params)
L-BFGS-B

3.54748
RY (48 params)
L-BFGS-B

3.93348
RY (48 params)
L-BFGS-B

Exact energy

3.13406

3.29894

3.52625

3.89548

Table 17 The 25 Pauli string operators, together with their coefficients at each coupling λ, making up the supersymmetric SU (2) matrix model at
=2
Group

(A)

(B)

(C)

123

Operator

λ = 0.2

λ = 0.5

λ = 1.0

λ = 2.0

IIIIIIIII

5.4

5.625

6.0

6.75

ZIIIIIIII

− 0.5

− 0.5

− 0.5

− 0.5

IZIIIIIII

− 0.5

− 0.5

− 0.5

− 0.5

IIZIIIIII

− 0.5

− 0.5

− 0.5

− 0.5

IIIZIIIII

− 0.5

− 0.5

− 0.5

− 0.5

IIIIZIIII

− 0.5

− 0.5

− 0.5

− 0.5

IIIIIZIII

− 0.5

− 0.5

− 0.5

− 0.5

IIIIIIZII

− 0.75

− 0.75

− 0.75

− 0.75

IIIIIIIZI

− 0.75

− 0.75

− 0.75

− 0.75

IIIIIIIIZ

− 0.75

− 0.75

− 0.75

− 0.75

XXIXXIIII

0.05

− 0.125

− 0.25

− 0.5

XIXXIXIII

0.05

− 0.125

− 0.25

− 0.5

IXXIXXIII

0.05

− 0.125

− 0.25

− 0.5

IIXIIIYXI

0.158

0.25

0.354

0.5

IIXIIIXYI

0.158

0.25

0.354

0.5

IIIIIXXXI

0.158

0.25

0.354

0.5

IIIXIYZY

0.158

0.25

0.354

0.5

XIIIIIIYX

0.158

0.25

0.354

0.5

XIIIIIIXY

0.158

0.25

0.354

0.5

IIIXIIIXX

0.158

0.25

0.354

0.5

IIIIIXYYI

− 0.158

− 0.25

− 0.354

− 0.5

IXIIIIYZX

− 0.158

− 0.25

− 0.354

− 0.5

IXIIIIXZY

− 0.158

− 0.25

− 0.354

− 0.5

IIIIXIXZX

− 0.158

− 0.25

− 0.354

− 0.5

IIIXIIIYY

− 0.158

− 0.25

− 0.354

− 0.5

Eur. Phys. J. C

(2025) 85:705

Page 35 of 80

(S)=2

Hλ=0.5

= −0.5 (IZIIIIIII + IIZIIIIII+ IIIZIIIII+ IIIIZIIII+ IIIIIZIII)
−0.75 (IIIIIIZII + IIIIIIIZI + IIIIIIIIZ)
−0.125 (XXIXXIIII + XIXXIXIII + IXXIXXIII)

+0.25 (IIXIIIYXI + IIXIIIXYI + IIIIIXXXI + IIIIXIYZY
+XIIIIIIYX+ XIIIIIIXY +IIIXIIIXX)
−0.25 (IIIIIXYYI + IXIIIIYZX+ IXIIIIXZY
+IIIIXIXZX + IIIXIIIYY)

(47)

6.1 EvolvedOperatorAnsatz
In this case, we work only with EvolvedOperator
Ansatz, as our goal is to keep the quantum circuit ansatzes
as shallow as possible. This is not achievable with either
EfficientSU2 or TwoLocal, since the depth-1 versions
of these circuits fail to yield results that are close enough to
the exact values, which can only be reached with much deeper
circuits of around 8-9 layers.
For the construction of the EvolvedOperatorAnsatz
circuits, we work with the largest 15, 20 and 24 operators
chosen from Table 17. This leads to the 12 ansatzes (listed
in Table 18) which include the depth-1 circuits ev_op_15,
ev_op_20, ev_op_H with 15, 20, and 24 building blocks,
respectively, together with their depth-2, depth-3, depth-4
versions. Since the supersymmetric  = 2 Hamiltonian
only contains 25 Pauli string operators, excluding the identity operator (which cannot be parameterized anyway), those
circuits whose building blocks use 24 operators (ev_op_H
and their higher-depth versions) practically contain the whole
 = 2 Hamiltonian. Although we have 12 ansatzes in total,
structurally, there are only three unique variants.
(S)=2
,
The best results of the VQE experiments (Hλ
EvolvedOperatorAnsatz, COBYLA & SPSA) are
summarized in Table 19. A comparison of the performances
of all 12 variants at four couplings can be found in Fig.
15. For all couplings, the best quantum circuit ansatz is
ev_op_Hp20 with 20 parameters.
We note the following observations regarding the best
ansatzes, the overlaps of the ansatzes with the exact ground
state, and the effect of increasing the depths of the ansatzes
on the convergence results.
• Best ansatzes: At all couplings, the best Evolved
OperatorAnsatz variant is ev_op_Hp20 with 20
parameters (see Table 19). Interestingly, circuits with 24
operators in their building blocks perform quite poorly
compared to those containing fewer operators. They are
in fact among the worst performers at all four couplings
(see also Figs. 27, 28, 29, 30, 31).
• Overlaps with the exact ground state:
– At λ = 0.2 (Fig. 15, first row, left subfigure), 4 variants from ev_op_Hp15 to ev_op_Hp20_2f as

705

well as ev_op_Hp15_3f , ev_op_Hp15_4f –
all with SPSA – show good overlaps with the exact
ground state.. With COBYLA, ev_op_Hp15_2f,
ev_op_H_2f,
ev_op_Hp15_3f, ev_op_Hp15_4f also show
good overlaps with the exact ground state..
– At λ = 0.5 (Fig. 15, first row, right subfigure)
ev_op_Hp20,
ev_op_Hp15_2f
and
ev_op_Hp20_2f – all with SPSA - show good
overlaps with the exact ground state..
– At λ = 1.0 (Fig. 15, second row, left subfigure), only
ev_op_Hp20 and ev_op_Hp20_2f - both with
SPSA – show good overlaps with the exact ground
state.
– At λ = 2.0 (Fig. 15, second row, right subfigure),
only ev_op_Hp20 with SPSA shows a good overlap
with the exact ground state.
• Effect of circuit depths: As supplementary material, the
full convergence curves at different couplings obtained
by running VQE algorithms using COBYLA for all
12 circuits are shown in Fig. 27, while the convergence curves obtained using SPSA are plotted separately
for circuits of different depths. Convergence curves of
depth-1 circuits (comprising ev_op_15, ev_op_20,
ev_op_H) using SPSA are plotted in Fig. 28. Convergence curves of depth-2 circuits (ev_op_15_2f,
ev_op_20_2f, ev_op_H_2f) are shown in Fig.
29, those of depth-3 circuits (ev_op_15_3f, ev_
op_20_3f, ev_op_H_3f) are shown in Fig. 30, and
those of depth-4 circuits (ev_op_15_4f, ev_op_20
_4f, ev_op_H_4f) are shown in Fig. 31. All the curves
are included in Sect. C in the appendix. Within the depth1 circuits comprising the three variants ev_op_Hp15,
ev_op_Hp20, ev_op_H, for both COBYLA and SPSA
optimizers, the order of best to worst performing, for all
four couplings, is ev_op_Hp20 → ev_op_Hp15 →
ev_op_H. As the depth of the circuits is increased from
1 to 4, a clear trend is the general decrease in performance of all variants compared to their shallower versions, which is evident in the convergence curves that end
in higher and higher values for the case of COBYLA optimizer in Fig. 27 and become more and more widespread
for the case of SPSA optimizer which can be seen in Figs.
28, 29, 30 and 31.
6.2 Comparison of all quantum circuits
In this section, we compare the best results obtained using
EvolvedOperatorAnsatz circuits with those obtained
in [16] using EfficientSU2 RY R Z circuits either with
depth-8 (2(d + 1)n Q = 18 × 9 = 162 parameters) or depth9 (2(d + 1)n Q = 20 × 9 = 180 parameters). The results are

123

705

Page 36 of 80

Eur. Phys. J. C

Table 18 Evolved
OperatorAnsatz quantum
circuits used to run VQE for the
case of SU (2) supersymmetric
model with  = 2

(2025) 85:705

Ansatz

Parameters

Operators

ev_op_Hp15

15

Largest 15 operators by absolute values


IIXIIIYXI, IIIXIIIXX, IIIXIIIYY
λ = 0.2: (A) +
IIXIIIXYI, IIIIIXXXI, IIIIIXYYI
λ = 0.5: Same as λ = 0.2
λ = 1.0: Same as λ = 0.2
λ = 2.0: Same as λ = 0.2

20

ev_op_Hp20

Largest 20 operators by absolute values
λ = 0.2: (A) + (C) (excl. XIIIIIIXY)
λ = 0.5: Same as λ = 0.2
λ = 1.0: Same as λ = 0.2
λ = 2.0: Same as λ = 0.2

ev_op_Hp

24

All operators in Table 17 except IIIIIIIII

ev_op_Hp15_2f

30

Depth-2 version of ev_op_Hp15

ev_op_Hp20_2f

40

Depth-2 version of ev_op_Hp20

ev_op_Hp_2f

48

Depth-2 version of ev_op_Hp

ev_op_Hp15_3f

45

Depth-3 version of ev_op_Hp15

ev_op_Hp20_3f

60

Depth-3 version of ev_op_Hp20

ev_op_Hp_3f

72

Depth-3 version of ev_op_Hp

ev_op_Hp15_4f

60

Depth-4 version of ev_op_Hp15

ev_op_Hp20_4f

80

Depth-4 version of ev_op_Hp20

ev_op_Hp_4f

96

Depth-4 version of ev_op_Hp

(S)=2

Table 19 VQE experiments (Hλ
, EvolvedOperatorAnsatz,
COBYLA & SPSA): summary of the best results for each type of optimizers for each of the four coupling λ. The best results are noted in

bold. (F-S) denotes full-supplementary. Tables with the label (F-S) can
be found in Sect. C in the appendix

Coupling

Exact

COBYLA

SPSA

Full results

λ = 0.2

0.003287

0.03099
ev_op_Hp_2f

0.01228
ev_op_Hp20

Table 37 (F-S)

λ = 0.5

0.01690

0.19482
ev_op_Hp15_2f

0.01953
ev_op_Hp20

Table 38 (F-S)

λ = 1.0

0.04829

0.39722
ev_op_Hp15_3f

0.10229
ev_op_Hp20

Table 39 (F-S)

λ = 2.0

0.08385

0.6250
ev_op_Hp20_3f

0.15918
ev_op_Hp20

Table 40 (F-S)

tabulated in Table 20, in which the first row contains the best
results from using EvolvedOperatorAnsatz while the
second row lists the results reported by [16]. Each entry in
the first row is a tuple (E, ansatz, depth, number of parameters, optimizer) corresponding to the best ansatz variant and
its characteristics. The entries in the second row have a similar format, (E, depth, number of parameters, optimizer), in
which the ansatz is not listed since it is always the variant of
EfficientSU2 with RY R Z rotation block and full entanglement pattern.
For λ = 0.2 and λ = 1.0, depth-8 and depth-9
EfficientSU2 ansatzes achieved slightly better results
than depth-1 ev_op_Hp20. For λ = 0.5 and λ = 2.0, the
same depth-1 ev_op_Hp20 ansatz outperformed the depth-

123

9 EfficientSU2 ansatz. The fact that ev_op_Hp20
with only 20 parameters can perform on par or better than
EfficientSU2 with 162 or 180 parameters is a very
promising result which shows the clear advantage of tailored
ansatzes over generic ones.

7 Summary and concluding remarks
In this work, we revisited the problem of solving for
the ground state energy of SU (2) matrix models (both
bosonic and supersymmetric) with variational quantum
eigensolver (VQE) algorithm involving variational quantum
circuit ansatzes using the IBM quantum computing plat-

Eur. Phys. J. C

(2025) 85:705

Page 37 of 80

705

Fig. 15 Supersymmetric SU (2) model at Fock cutoff  = 2 at different couplings (clockwise from top left λ = 0.2, λ = 0.5, λ = 2.0, λ = 1.0):
comparison of all EvolvedOperatorAnsatz quantum circuits. The data points in the subfigures above are from Tables 37, 38, 39, 40
Table 20 Comparison of the EvolvedOperatorAnsatz quantum circuits at different couplings for the supersymmetric SU (2) matrix model
at cutoff  = 2 with the results reported in [16]. The absolute best results are noted in bold
Ansatz type

λ = 0.2

λ = 0.5

λ = 1.0

λ = 2.0

EvolvedOperator

0.012277
ev_op_Hp20
depth-1
(20 params)
SPSA

0.01953
ev_op_Hp20
depth-1
(20 params)
SPSA

0.10229
ev_op_Hp20
depth-1
(20 params)
SPSA

0.15918
ev_op_Hp20
depth-1
(20 params)
SPSA

Results from [16]
EfficientSU2
RY R Z

0.010126
depth-8
(162 params)
SLSQP

0.02744
depth-9
(180 params)
SLSQP

0.07900
depth-9
(180 params)
SLSQP

0.17688
depth-9
(180 params)
SLSQP

Exact energy

0.003287

0.01690

0.04829

0.08385

123

705

Page 38 of 80

form Qiskit [1]. With the aim of exploring and identifying new variational ansatzes to extend the well-known
EfficientSU2 quantum circuits used in [16], we first
experimented with TwoLocal circuits – a more general
form of EfficientSU2 with the same underlying architecture, and later with EvolvedOperatorAnsatz – a
type of circuits with different architecture that we tailormade for each specific Hamiltonians of interest, in addition
to experimenting with more variants of EfficientSU2
beyond those used in [16]. We referred to both
EfficientSU2 and TwoLocal as generic ansatzes on
account of the fact that their structures, whose building
blocks consist of a rotation part and an entanglement part,
are essentially the same in all problem settings, while
EvolvedOperatorAnsatz had to be constructed by
choosing the suitable operators that go into each building
block.
• In total, for the cases of SU (2) bosonic matrix model at
Fock space cutoffs  = 2 and  = 4, we explored
eight different variants of EfficientSU2 that are
combinations of four possible choices of rotation block,
involving the parameterized RY , R Z , RY R Z , RY Y gates,
and two possible choices of entanglement arrangements
(full or circular) involving the unparameterized C X
gate (see Table 1 and Fig. 2). Corresponding to these
eight EfficientSU2 variants are the eight variants of
TwoLocal ansatzes with the same four combinations
of rotation gates and two possible entanglement arrangements involving the parameterized C R X gates (see Table
2 and Fig. 3). To keep the number of variational parameters small, all circuits used are depth-114 . Regarding the
EvolvedOperatorAnsatz, we created nine variants
for the bosonic SU (2) matrix model with Fock cutoff
 = 2 and eight variants for the  = 4 case. For  = 2,
the nine variants include one with random operators, one
with a full set of operators making up the Hamiltonian
(with the exception of the identity), and one with a partial set of operators making up the Hamiltonian, together
with their higher-depth versions (see Table 8 and Fig. 10).
For  = 4, the variants include circuits whose building
blocks are made from the 15, 20, 25, 30 operators with
largest coefficients by absolute values out of the 895 operators making up the full  = 4 Hamiltonian, together
with their higher depth versions (see Table 14).
With these different variants within each type of quantum
circuit ansatzes, for the  = 2 and  = 4 SU (2) cases,
we performed 32 VQE runs using EfficientSU2 and
TwoLocal at each coupling for a total of four differ14 Except the case of bosonic SU (2) model at  = 2, λ = 2.0 in which

we used deeper EfficientSU2 and TwoLocal circuits to evaluate
the effect of circuit depth on the results

123

Eur. Phys. J. C

(2025) 85:705

ent couplings λ = 0.2, 0.5, 1.0, 2.0 using two different optimizers: COBYLA and SPSA (see Figs. 8 and
13)15 . With EvolvedOperatorAnsatz, at each coupling, there were 18 VQE runs for the  = 2 case
(see Fig. 11), and 16 VQE runs for the  = 4 case16
(see Fig. 14). The obtained results show a consistent
trend for both  at all couplings: the best performing
quantum circuit ansatz type is always the tailor-made
EvolvedOperatorAnsatz, followed by the generic
TwoLocal ansatzes, followed by EfficientSU2 (as
documented in Tables 10 and 16). This is not surprising,
given the fact that EfficientSU2 is the least tailored
and least expressive ansatz type compared to the others.
In specifying the different variants of EfficientSU2,
our only choice lies in the selection of the gates in the rotation block, and the entanglement scheme. In specifying
the variants of TwoLocal quantum circuits, not only
do we have the same choices as the EfficientSU2
case, we also have an additional choice of parameterized gates for the entanglement block. On the other
hand, for the EvolvedOperatorAnsatz quantum
circuits, we moved away from the rigid structure of
‘rotation-entanglement’ blocks and had the freedom to
use entirely new building blocks made of Pauli string
operators, which can be selected to be those forming
the Hamiltonian of interest. When compared with the
results reported in [16], which were obtained using
the depth-3 EfficientSU2 circuits with either RY
or RY R Z rotation blocks and full entanglement pattern, our results are promising in the sense that while
EvolvedOperatorAnsatz always outperform the
results of [16], TwoLocal ansatzes also do better than
the results of [16] in some cases (see Tables 10 and 16).
• For the case of supersymmetric SU (2) model at Fock
space cutoff  = 2, we worked only with
EvolvedOperatorAnsatz variational quantum circuits and created twelve different ansatzes, three of which
are unique and made of building blocks with the largest
15, 20 and 24 operators chosen from the 25 operators
making up the  = 2 Hamiltonian (see Table 17). The
remaining ansatzes are the higher-depth (depth-2, depth3, depth-4) versions of these first three (see Table 18).
Using these 12 ansatzes, we performed 24 VQE runs
at each coupling using SPSA and COBYLA optimizers
(see Fig. 15), for the same four couplings of 0.2, 0.5,

15 In total, for the SU (2) bosonic matrix model, this resulted in 128

VQE experiments for  = 2 and 128 experiments for  = 4, using
EfficientSU2 and TwoLocal ansatze

SU (2) bosonic matrix model, there were
72 VQE runs for  = 2 and 64 VQE runs for  = 4 using
EvolvedOperatorAnsatz circuits.
16 All together, for the

Eur. Phys. J. C

(2025) 85:705

1.0 and 2.017 . The obtained results consistently show
the best variational quantum circuit ansatz as the depth1 circuit with 20 operators in its building blocks (see
Table 20). Higher-depth circuits actually recorded poorer
performances compared to their lower-depth counterparts. When using as benchmarks the results of [16],
which were obtained using deep EfficientSU2 circuits (either depth-8 or depth-9) with around 162 or 180
parameters, our best results obtained by using the shallow
20-parameter EvolvedOperatorAnsatz are really
competitive, given that for λ = 0.5 and λ = 2.0,
EvolvedOperatorAnsatz emerged as the best performer, while for λ = 0.2 and λ = 1.0,
EvolvedOperatorAnsatz obtained very close
results to the much deeper EfficientSU2 of [16].
This is again very promising in the sense that by using a
tailored architecture without involving either rotation or
entanglement building blocks, one can obtain comparably good or better results at a small fraction (around 1/8
or 1/9) of the number of parameters required when using
EfficientSU2.
Overall, the obtained results in this work suggest that given
their potential to outperform the well-known and routinely
used EfficientSU2 in the context of SU (2) matrix
model, TwoLocal and EvolvedOperatorAnsatz variational quantum circuits should be considered more often
in future quantum simulation studies involving VQE algorithm in high energy physics in general, either alongside or
as new alternatives to EfficientSU2. A class of interesting examples of these future studies involves the quantum
computing of Schwarzschild-de-Sitter black holes [10] or
the quantum computing of string theory black holes [11], all
of which employed EfficientSU2 circuits as variational
ansatzes. Another interesting class of examples involves the
benchmarking of VQE algorithm on different types of quantum computing hardware as done in [59] in which the authors
also employed EfficientSU2 quantum circuits (referred
to as the RY -CNOT ansatz).
Perhaps of more immediate relevance to this work is
the possibility of applying TwoLocal and Evolved
Operator to SU (N ) matrix models with N > 2. As previously discussed in Section 3, higher SU (N ) matrix models are much more computationally intensive than SU (2)
model due to the exponentially increasing size of the
Hilbert spaces of these models [60,61]. While it is possible to run VQE experiments involving SU (3) matrix
model with generic ansatzes like EfficientSU2 and
TwoLocal with the circular entanglement pattern which

Page 39 of 80

705

scale linearly 18 in the number of qubits, we note that,
to run just the simulator, this requires substantial computing resources typically possible only with an access to real
quantum hardware or a cloud computing platform. This is
where EvolvedOperatorAnsatz circuits might turn
out to be an especially good candidate for a trial wavefunction, since unlike TwoLocal and EfficientSU2,
they do not scale in the number of qubits (but depend
only on the number of operators used in their construction), potentially making it possible to tackle the problem without involving large computing powers. Furthermore, we note that a more streamlined method of constructing the tailored EvolvedOperatorAnsatz circuits would involve the ADAPT-VQE algorithm that implements the iterative adjustment process to fine tune the operators to be included in the final form of the ansatz. This
bypasses the need to manually construct different variants of
EvolvedOperatorAnsatz and could be more efficient
when dealing with more complex SU (N ) matrix models.
We hope to be able to return to these issues in future works.
Acknowledgements The author is an unaffiliated and independent
researcher. This work is possible thanks to the open-source IBM quantum computing platform Qiskit [1].
Data Availability Statement My manuscript has associated data in
a data repository. [Authors’ comment: The data can be found in the
GitHub
repository:
https://github.com/lorrespz/mat
rix_model_quantum_computing_vqe.]
Code Availability Statement My manuscript has associated code/
software in a data repository. [Authors’ comment: All codes can be
found in the GitHub repository: https://github.com/lorrespz/matrix_
model_quantum_computing_vqe.]
Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation,
distribution and reproduction in any medium or format, as long as you
give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes
were made. The images or other third party material in this article
are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not
included in the article’s Creative Commons licence and your intended
use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecomm
ons.org/licenses/by/4.0/.
Funded by SCOAP3 .

A  = 2 bosonic SU(2) model: full results
A.1 EfficientSU2 & TwoLocal
See Tables 21, 22, 23, 24 and Figs. 16, 17, 18, 19.

17 For the  = 2 SU (2) supersymmetric model, there were 96 VQE
runs in total

18 And TwoLocal variants with the full entanglement pattern which

scale quadratically.

123

705

Page 40 of 80

Table 21 Full results from the
VQE
experiments
 =2
Hλ=0.2 , EfficientSU2/
TwoLocal, COBYLA/SPSA).
The exact energy is
=2 = 3.14808. The best
E λ=0.2
result from each optimizer is
noted in bold

Table 22 Full results from the
=2 ,
VQE experiments (Hλ=0.5
EfficientSU2/TwoLocal,
COBYLA/SPSA). The exact
=2 = 3.36254.
energy is E λ=0.5
The best result from each
optimizer is noted in bold

123

Eur. Phys. J. C

(2025) 85:705

Ansatz

Energy (COBYLA)

Energy (SPSA)

effsu2_Ry_c

3.19141

3.15703

effsu2_Rz_c

3.14980

3.14980

effsu2_RyRz_c

3.15801

3.16816

effsu2_RyY_c

3.15977

3.16641

effsu2_Ry_f

3.15918

3.15332

effsu2_Rz_f

3.14980

3.14980

effsu2_RyRz_f

3.16211

3.15137

effsu2_RyY_f

3.15664

3.15137

tl_Ry_c

3.14863

3.14941

tl_Rz_c

3.14980

3.14980

tl_RyRz_c

3.15762

3.15645

tl_RyY_c

3.14863

3.14941

tl_Ry_f

3.14844

3.14980

tl_Rz_f

3.14980

3.14980

tl_RyRz_f

3.16992

3.15605

tl_RyY_f

3.14844

3.14980

Ansatz

Energy (COBYLA)

Energy (SPSA)

effsu2_Ry_c

3.37158

3.38623

effsu2_Rz_c

3.37451

3.37451

effsu2_RyRz_c

3.36963

4.41553

effsu2_RyY_c

3.39014

3.40088

effsu2_Ry_f

3.37549

3.37305

effsu2_Rz_f

3.37451

3.37451

effsu2_RyRz_f

3.40283

3.37646

effsu2_RyY_f

3.37549

3.37891

tl_Ry_c

3.36475

3.37207

tl_Rz_c

3.37451

3.37451

tl_RyRz_c

3.37012

3.37939

tl_RyY_c

3.36475

3.37207

tl_Ry_f

3.36523

3.37646

tl_Rz_f

3.37451

3.37451

tl_RyRz_f

3.39502

3.38379

tl_RyY_f

3.36523

3.37646

Eur. Phys. J. C

(2025) 85:705

Table 23 Full results from the
=2 ,
VQE experiments (Hλ=1.0
EfficientSU2/TwoLocal,
COBYLA/SPSA). The exact
=2 = 3.69722.
energy is E λ=1.0
The best result from each
optimizer is noted in bold

Table 24 Full results from the
=2 ,
VQE experiments (Hλ=2.0
EfficientSU2/TwoLocal,
COBYLA/SPSA). The exact
=2 = 4.26795.
energy is E λ=2.0
The best result from each
optimizer is noted in bold

Page 41 of 80

705

Ansatz

Energy (COBYLA)

Energy (SPSA)

effsu2_Ry_c

3.77051

3.76953

effsu2_Rz_c

3.74902

3.74902

effsu2_RyRz_c

3.78906

3.79199

effsu2_RyY_c

3.79297

3.77832

effsu2_Ry_f

3.80469

3.74316

effsu2_Rz_f

3.74902

3.74902

effsu2_RyRz_f

3.76465

3.75098

effsu2_RyY_f

3.75879

3.74902

tl_Ry_c

3.73730

3.75098

tl_Rz_c

3.74902

3.74902

tl_RyRz_c

3.74414

3.75293

tl_RyY_c

3.73730

3.75098

tl_Ry_f

3.74121

3.75195

tl_Rz_f

3.74902

3.74902

tl_RyRz_f

3.76953

3.74707

tl_RyY_f

3.74121

3.75195

Ansatz

Energy (COBYLA)

Energy (SPSA)

effsu2_Ry_c

5.61816

5.54297

effsu2_Rz_c

4.49805

4.49805

effsu2_RyRz_c

4.46973

4.49609

effsu2_RyY_c

4.88574

4.52148

effsu2_Ry_f

4.49121

4.51172

effsu2_Rz_f

4.49805

4.49805

effsu2_RyRz_f

4.45508

4.52051

effsu2_RyY_f

4.54004

4.50098

tl_Ry_c

4.41895

4.48535

tl_Rz_c

4.49805

4.49805

tl_RyRz_c

4.52441

4.50684

tl_RyY_c

4.41895

4.48535

tl_Ry_f

4.44922

4.51562

tl_Rz_f

4.49805

4.49805

tl_RyRz_f

4.48730

4.49121

tl_RyY_f

4.44922

4.51562

123

705

Page 42 of 80

Eur. Phys. J. C

(2025) 85:705

=2 . Clockwise from top left: (H =2 , EfficientSU2,
Fig. 16 Convergence curves of the energy for the VQE experiments involving Hλ=0.2
λ=0.2
=2 , TwoLocal, COBYLA), (H =2 , TwoLocal, SPSA), (H =2 , EfficientSU2, SPSA)
COBYLA), (Hλ=0.2
λ=0.2
λ=0.2

123

Eur. Phys. J. C

(2025) 85:705

Page 43 of 80

705

=2 . Clockwise from top left: (H =2 , EfficientSU2,
Fig. 17 Convergence curves of the energy for the VQE experiments involving Hλ=0.5
λ=0.5
=2 , TwoLocal, COBYLA), (H =2 , TwoLocal, SPSA), (H =2 , EfficientSU2, SPSA)
COBYLA), (Hλ=0.5
λ=0.5
λ=0.5

123

705

Page 44 of 80

Eur. Phys. J. C

(2025) 85:705

=2 . Clockwise from top left: (H =2 , EfficientSU2,
Fig. 18 Convergence curves of the energy for the VQE experiments involving Hλ=1.0
λ=1.0
=2 , TwoLocal, COBYLA), (H =2 , TwoLocal, SPSA), (H =2 , EfficientSU2, SPSA)
COBYLA), (Hλ=1.0
λ=1.0
λ=1.0

123

Eur. Phys. J. C

(2025) 85:705

Page 45 of 80

705

=2 . Clockwise from top left: (H =2 , EfficientSU2,
Fig. 19 Convergence curves of the energy for the VQE experiments involving Hλ=2.0
λ=2.0
=2 , TwoLocal, COBYLA), (H =2 , TwoLocal, SPSA), (H =2 , EfficientSU2, SPSA)
COBYLA), (Hλ=2.0
λ=2.0
λ=2.0

A.2 EvolvedOperatorAnsatz
See Tables 25, 26, 27, 28 and Figs. 20, 21.

123

705

Page 46 of 80

Table 25 Full results from the
=2 ,
VQE experiments (Hλ=0.2
EvolvedOperatorAnsatz,
COBYLA/SPSA). The exact
=2 = 3.14808.
energy is E λ=0.2
The best result from each
optimizer is noted in bold

Table 26 Full results from the
=2 ,
VQE experiments (Hλ=0.5
EvolvedOperatorAnsatz,
COBYLA/SPSA). The exact
=2 = 3.36254.
energy is E λ=0.5
The best result from each
optimizer is noted in bold

Table 27 Full results from the
=2 ,
VQE experiments (Hλ=1.0
EvolvedOperatorAnsatz,
COBYLA/SPSA). The exact
=2 = 3.69722.
energy is E λ=1.0
The best result from each
optimizer is noted in bold

Table 28 Full results from the
=2 ,
VQE experiments (Hλ=2.0
EvolvedOperatorAnsatz,
COBYLA/SPSA). The exact
=2 = 4.26795.
energy is E λ=2.0
The best result from each
optimizer is noted in bold

123

Eur. Phys. J. C

(2025) 85:705

Ansatz

Energy (COBYLA)

Energy (SPSA)

ev_op_r

3.14980

3.14863

ev_op_r3

3.15078

3.14844

ev_op_H

3.15000

3.14863

ev_op_H_2f

3.15000

3.15488

ev_op_H_3f

3.14883

3.15332

ev_op_Hp

3.15059

3.14980

ev_op_Hp2

3.15156

3.15156

ev_op_Hp3

3.14902

3.15254

ev_op_Hp4

3.14844

3.15273

Ansatz

Energy (COBYLA)

Energy (SPSA)

ev_op_r

3.37451

3.37158

ev_op_r3

3.37109

3.37305

ev_op_H

3.36572

3.37158

ev_op_H_2f

3.36328

3.37695

ev_op_H_3f

3.36426

3.37354

ev_op_Hp

3.37451

3.37451

ev_op_Hp3

3.36768

3.36719

ev_op_Hp4

3.37695

3.37109

Ansatz

Energy (COBYLA)

Energy (SPSA)

ev_op_r

3.74902

3.74902

ev_op_r3

3.74414

3.74512

ev_op_H

3.72656

3.72949

ev_op_H_2f

3.71484

3.73242

ev_op_H_3f

3.71387

3.72461

ev_op_Hp

3.74902

3.73828

ev_op_Hp2

3.73242

3.72266

ev_op_Hp3

3.71582

3.73242

ev_op_Hp4

3.70508

3.73926

Ansatz

Energy (COBYLA)

Energy (SPSA)

ev_op_r

4.49805

4.49805

ev_op_r3

4.48535

4.48926

ev_op_H

4.29297

4.31055

ev_op_H_2f

4.28906

4.30664

ev_op_H_3f

4.29102

4.30859

ev_op_Hp

4.44141

4.44141

ev_op_Hp2

4.39453

4.32227

ev_op_Hp3

4.29883

4.34766

ev_op_Hp4

4.28906

4.33008

Eur. Phys. J. C

(2025) 85:705

Page 47 of 80

705

Fig. 20 Convergence curves
from the VQE experiments
(Hλ=2 , EvolvedOperatorAnsatz,
COBYLA). From top to bottom:
λ = 0.2, 0.5, 1.0, 2.0

123

705

Page 48 of 80

Fig. 21 Convergence curves
from the VQE experiments
(Hλ=2 , EvolvedOperatorAnsatz,
SPSA). From top to bottom:
λ = 0.2, 0.5, 1.0, 2.0

123

Eur. Phys. J. C

(2025) 85:705

Eur. Phys. J. C

(2025) 85:705

Page 49 of 80

705

B  = 4 bosonic SU(2) model: Full results
B.1 EfficientSU2 & TwoLocal
See Tables 29, 30, 31, 32 and Figs. 22, 23, 24, 25.

Table 29 Full results of the
=4 ,
VQE experiments (Hλ=0.2
EfficientSU2&TwoLocal,
COBYLA/SPSA) involving the
SU (2) bosonic matrix model at
Fock cut-off  = 4 and
coupling λ = 0.2 using
EfficientSU2/TwoLocal
quantum circuit with SPSA &
COBYLA optimizers. The exact
=4 = 3.13406.
energy is E λ=0.2
The best result for each type of
optimizers is noted in bold

Table 30 Full results of the
=4 ,
VQE experiments (Hλ=0.5
EfficientSU2&TwoLocal,
COBYLA/SPSA) involving the
SU (2) bosonic matrix model at
Fock cut-off  = 4 and
coupling λ = 0.2 using
EfficientSU2/TwoLocal
quantum circuit with SPSA &
COBYLA optimizers. The exact
=4 = 3.29894.
energy is E λ=0.5
The best result for each type of
optimizers is noted in bold

Ansatz

Energy (COBYLA)

Energy (SPSA)

effsu2_Ry_c

3.34450

3.23204

effsu2_Rz_c

3.17910

3.17910

effsu2_RyRz_c

7.35898

4.89771

effsu2_RyY_c

4.93931

3.14605

effsu2_Ry_f

3.37026

3.19555

effsu2_Rz_f

3.17910

3.17910

effsu2_RyRz_f

9.85983

3.11959

effsu2_RyY_f

3.38528

4.24528

tl_Ry_c

3.18228

3.18339

tl_Rz_c

3.17910

3.17910

tl_RyRz_c

3.38940

3.62318

tl_RyY_c

3.21248

3.13679

tl_Ry_f

3.49465

3.16617

tl_Rz_f

3.17910

3.17910

tl_RyRz_f

4.07165

4.10208

tl_RyY_f

3.58869

3.14366

Ansatz

Energy (COBYLA)

Energy (SPSA)

effsu2_Ry_c

4.18830

3.61873

effsu2_Rz_c

3.44775

3.44775

effsu2_RyRz_c

7.68608

5.96494

effsu2_RyY_c

3.71764

3.66239

effsu2_Ry_f

3.95226

3.40536

effsu2_Rz_f

3.44775

3.44775

effsu2_RyRz_f

3.99438

4.53325

effsu2_RyY_f

3.58207

3.55380

tl_Ry_c

3.21974

3.49978

tl_Rz_c

3.44775

3.44775

tl_RyRz_c

3.60629

3.39842

tl_RyY_c

3.27478

3.38926

tl_Ry_f

3.53397

3.32111

tl_Rz_f

3.44775

3.44775

tl_RyRz_f

4.35256

3.50001

tl_RyY_f

3.47803

3.30641

123

705

Page 50 of 80

Table 31 Full results of the
=4 ,
VQE experiments (Hλ=1.0
EfficientSU2&TwoLocal,
COBYLA/SPSA) involving the
SU (2) bosonic matrix model at
Fock cut-off  = 4 and
coupling λ = 1.0 using
EfficientSU2/TwoLocal
quantum circuit with SPSA &
COBYLA optimizers. The exact
=4 = 3.52625.
energy is E λ=1.0
The best result for each type of
optimizers is noted in bold

Table 32 Full results of the
=4 ,
VQE experiments (Hλ=2.0
EfficientSU2&TwoLocal,
COBYLA/SPSA) involving the
SU (2) bosonic matrix model at
Fock cut-off  = 4 and
coupling λ = 2.0 using
EfficientSU2/TwoLocal
quantum circuit with SPSA &
COBYLA optimizers. The exact
=4 = 3.52625.
energy is E λ=2.0
The best result for each type of
optimizers is noted in bold

123

Eur. Phys. J. C

(2025) 85:705

Ansatz

Energy (COBYLA)

Energy (SPSA)

effsu2_Ry_c

5.64314

4.22957

effsu2_Rz_c

3.89550

3.89550

effsu2_RyRz_c

6.94346

8.01018

effsu2_RyY_c

6.65659

5.67670

effsu2_Ry_f

6.30709

4.19845

effsu2_Rz_f

3.89550

3.89550

effsu2_RyRz_f

6.11065

3.78857

effsu2_RyY_f

4.30899

4.10703

tl_Ry_c

3.53869

5.26669

tl_Rz_c

3.89550

3.89550

tl_RyRz_c

6.18099

3.55374

tl_RyY_c

4.96284

4.83891

tl_Ry_f

3.56694

3.75099

tl_Rz_f

3.89550

3.89550

tl_RyRz_f

4.60628

3.92772

tl_RyY_f

3.74414

4.97329

Ansatz

Energy (COBYLA)

Energy (SPSA)

effsu2_Ry_c

10.89956

6.92786

effsu2_Rz_c

4.79100

4.79100

effsu2_RyRz_c

11.05988

4.32874

effsu2_RyY_c

9.68253

4.94393

effsu2_Ry_f

8.01434

4.20670

effsu2_Rz_f

4.79100

4.79100

effsu2_RyRz_f

7.32845

5.87643

effsu2_RyY_f

7.79339

5.54155

tl_Ry_c

6.39657

5.45181

tl_Rz_c

4.79100

4.79100

tl_RyRz_c

7.28931

4.61735

tl_RyY_c

4.26378

3.94466

tl_Ry_f

4.29829

6.29251

tl_Rz_f

4.79100

4.79100

tl_RyRz_f

7.99626

5.42990

tl_RyY_f

4.16062

5.61301

Eur. Phys. J. C

(2025) 85:705

Page 51 of 80

705

=4 . Clockwise from top left: (H =4 , EfficientSU2,
Fig. 22 Convergence curves of the energy for the VQE experiments involving Hλ=0.2
λ=0.2
=4 , TwoLocal, COBYLA), (H =4 , TwoLocal, SPSA), (H =4 , EfficientSU2, SPSA)
COBYLA), (Hλ=0.2
λ=0.2
λ=0.2

B.2 EvolvedOperatorAnsatz
See Tables 33, 34, 35, 36 and Fig. 26.
Table 33 Results of the VQE
=4 ,
experiments (Hλ=0.2
EvolvedOperatorAnsatz
from Table 14, SPSA &
COBYA). The exact energy is
E = 3.13406. The best result
from each type of optimizers is
noted in bold

Ansatz

Energy (COBYLA)

Energy (SPSA)

ev_op_Hp15

3.27813

3.17320

ev_op_Hp20

3.18835

3.15612

ev_op_Hp25

3.17782

3.14337

ev_op_Hp30

3.21665

3.14084

ev_op_Hp15_2f

3.15952

3.15614

ev_op_Hp20_2f

3.23598

3.19462

ev_op_Hp25_2f

3.33135

3.13421

ev_op_Hp30_2f

3.47127

3.15462

123

705

Page 52 of 80

Eur. Phys. J. C

(2025) 85:705

=4 . Clockwise from top left: (H =4 , EfficientSU2,
Fig. 23 Convergence curves of the energy for the VQE experiments involving Hλ=0.5
λ=0.5
=4 , TwoLocal, COBYLA), (H =4 , TwoLocal, SPSA), (H =4 , EfficientSU2, SPSA)
COBYLA), (Hλ=0.5
λ=0.5
λ=0.5

Table 34 Full results of the
=4 ,
VQE experiments (Hλ=0.5
EvolvedOperatorAnsatz
from Table 14, SPSA &
COBYA). The exact energy is
E = 3.29894. The best result
from each type of optimizers is
noted in bold

123

Ansatz

Energy (COBYLA)

Energy (SPSA)

ev_op_Hp15

4.03464

3.41548

ev_op_Hp20

3.35601

3.30692

ev_op_Hp25

3.29968

3.42603

ev_op_Hp30

33.51242

3.30582

ev_op_Hp15_2f

3.30153

3.34375

ev_op_Hp20_2f

3.54492

3.30794

ev_op_Hp25_2f

3.30028

3.29896

ev_op_Hp30_2f

3.77042

3.33945

Eur. Phys. J. C

(2025) 85:705

Page 53 of 80

705

=4 . Clockwise from top left: (H =4 , EfficientSU2,
Fig. 24 Convergence curves of the energy for the VQE experiments involving Hλ=1.0
λ=1.0
=4 , TwoLocal, COBYLA), (H =4 , TwoLocal, SPSA), (H =4 , EfficientSU2, SPSA)
COBYLA), (Hλ=1.0
λ=1.0
λ=1.0

Table 35 Full results of the
=4 ,
VQE experiments (Hλ=1.0
EvolvedOperatorAnsatz
from Table 14, SPSA &
COBYA). The exact energy is
E = 3.52625. The best result
from each type of optimizers is
noted in bold

Ansatz

Energy (COBYLA)

Energy (SPSA)

ev_op_Hp15

3.62082

3.67193

ev_op_Hp20

3.84073

3.60327

ev_op_Hp25

3.53512

3.96745

ev_op_Hp30

3.77387

3.54551

ev_op_Hp15_2f

4.35314

3.71765

ev_op_Hp20_2f

3.75998

3.59577

ev_op_Hp25_2f

4.92616

3.68810

ev_op_Hp30_2f

4.75916

3.63468

123

705

Page 54 of 80

Eur. Phys. J. C

(2025) 85:705

=4 . Clockwise from top left: (H =4 , EfficientSU2,
Fig. 25 Convergence curves of the energy for the VQE experiments involving Hλ=2.0
λ=2.0
=4 , TwoLocal, COBYLA), (H =4 , TwoLocal, SPSA), (H =4 , EfficientSU2, SPSA)
COBYLA), (Hλ=2.0
λ=2.0
λ=2.0

Table 36 Results of the VQE
=4 ,
experiments (Hλ=2.0
EvolvedOperatorAnsatz
from Table 14, SPSA &
COBYA). The exact energy is
E = 3.89548. The best result
from each type of optimizers is
noted in bold

123

Ansatz

Energy (COBYLA)

Energy (SPSA)

ev_op_Hp15

4.86152

4.69522

ev_op_Hp20

4.16425

4.62906

ev_op_Hp25

6.16766

4.37152

ev_op_Hp30

4.88188

4.12944

ev_op_Hp15_2f

4.94432

3.93348

ev_op_Hp20_2f

4.93465

4.10240

ev_op_Hp25_2f

7.39414

4.51453

ev_op_Hp30_2f

6.01181

4.76864

Eur. Phys. J. C

(2025) 85:705

Page 55 of 80

705

=4
Fig. 26 Convergence curves of the energy for the VQE experiments (Hλ=0.2,0.5,1.0,2.0
, EvolvedOperatorAnsatz from Table 14, SPSA &
=4
COBYA). First column: (Hλ , EvolvedOperatorAnsatz, COBYA). Second column: (Hλ=4 , EvolvedOperatorAnsatz, SPSA)

123

705

Page 56 of 80

Eur. Phys. J. C

(2025) 85:705

C  = 2 supersymmetric SU(2) model: Full results
See Tables 37, 38, 39, 40 and Figs. 27, 28, 29, 30, 31.

Table 37 Full results of the
(S)=2
VQE experiments (Hλ=0.2 ,
EvolvedOperatorAnsatz,
COBYLA/SPSA). All
EvolvedOperatorAnsatz
variants are described in Table
18. The exact energy is
E = 0.003287. The best result
from each optimizer is noted in
bold

Table 38 Full results of the
(S)=2
VQE experiments (Hλ=0.5 ,
EvolvedOperatorAnsatz,
COBYLA/SPSA). All
EvolvedOperatorAnsatz
variants are described in Table
18. The exact energy is
E = 0.01690. The best result
from each optimizer is noted in
bold

Table 39 Full results of the
(S)=2
VQE experiments (Hλ=1.0
,
EvolvedOperatorAnsatz,
COBYLA/SPSA). All
EvolvedOperatorAnsatz
variants are described in Table
18. The exact energy is
E = 0.04829. The best result
from each optimizer is noted in
bold

123

Ansatz

Energy (COBYLA)

Energy (SPSA)

ev_op_Hp15

2.05509

0.09354

ev_op_Hp20

0.07807

0.01228

ev_op_H

2.14721

0.11827

ev_op_Hp15_2f

0.09291

0.09172

ev_op_Hp20_2f

0.07201

0.05251

ev_op_H_2f

0.03099

1.53414

ev_op_Hp15_3f

0.09358

0.09763

ev_op_Hp20_3f

0.16704

0.18184

ev_op_H_3f

2.20486

2.20766

ev_op_Hp15_4f

0.10025

0.13584

ev_op_Hp20_4f

0.57030

0.94922

ev_op_H_4f

3.28990

3.04627

Ansatz

Energy (COBYLA)

Energy (SPSA)

ev_op_Hp15

2.14404

0.22217

ev_op_Hp20

0.24023

0.01953

ev_op_H

2.36133

0.33105

ev_op_Hp15_2f

0.19482

0.23730

ev_op_Hp20_2f

0.22119

0.18799

ev_op_H_2f

0.39746

2.15186

ev_op_Hp15_3f

0.20605

0.26318

ev_op_Hp20_3f

1.22900

0.32031

ev_op_H_3f

2.87256

1.84668

ev_op_Hp15_4f

0.24854

0.26904

ev_op_Hp20_4f

1.33350

0.65479

ev_op_H_4f

3.59375

3.48535

Ansatz

Energy (COBYLA)

Energy (SPSA)

ev_op_Hp15

2.34535

0.47291

ev_op_Hp20

0.46279

0.10229

ev_op_H

2.69001

0.67807

ev_op_Hp15_2f

0.55453

0.44484

ev_op_Hp20_2f

0.40886

0.13280

ev_op_H_2f

0.64810

1.29156

ev_op_Hp15_3f

0.39722

0.50091

ev_op_Hp20_3f

2.34058

0.44396

ev_op_H_3f

3.73377

2.00362

ev_op_Hp15_4f

0.57642

0.55918

ev_op_Hp20_4f

3.24279

0.47511

ev_op_H_4f

3.34156

3.08163

Eur. Phys. J. C

(2025) 85:705

Table 40 Full results of the
(S)=2
VQE experiments (Hλ=2.0
,
EvolvedOperatorAnsatz,
COBYLA/SPSA). All
EvolvedOperatorAnsatz
variants are described in Table
18. The exact energy is
E = 0.08385. The best result
from each optimizer is noted in
bold

Page 57 of 80

705

Ansatz

Energy (COBYLA)

Energy (SPSA)

ev_op_Hp15

2.87744

0.87207

ev_op_Hp20

0.67041

0.15918

ev_op_H

3.51416

1.40527

ev_op_Hp15_2f

0.92383

0.88135

ev_op_Hp20_2f

3.04639

0.41748

ev_op_H_2f

3.05371

1.17822

ev_op_Hp15_3f

0.88379

0.90771

ev_op_Hp20_3f

0.62500

0.82568

ev_op_H_3f

3.80322

2.17969

ev_op_Hp15_4f

0.95947

0.93457

ev_op_Hp20_4f

2.89307

1.25342

ev_op_H_4f

2.73145

2.16602

123

705

Page 58 of 80

Eur. Phys. J. C

(S)=2

Fig. 27 VQE experiments (Hλ
, EvolvedOperatorAnsatz,
COBYLA): convergence curves of the energy values. Clockwise from
top left: λ = 0.2, 0.5, 2.0, 1.0. In all 4 subfigures, depth-4 circuits

123

(2025) 85:705

perform much worse than their lower depth versions, as is evident from
the corresponding convergence curves

Eur. Phys. J. C

(2025) 85:705

(S)=2

Fig. 28 VQE experiments (Hλ
, EvolvedOperatorAnsatz,
SPSA): convergence curves of the energy values. Only depth1 circuits from Table 18 are plotted. Clockwise from top left:
λ = 0.2, 0.5, 2.0, 1.0. In all 4 subfigures, ev_op_Hp20 is the best

Page 59 of 80

705

performing variant while ev_op_H is the worst performing variant,
as is evident from how close their corresponding convergence curves
are to the exact energy denoted by the horizontal black dashed line

123

705

Page 60 of 80

Eur. Phys. J. C

(S)=2

Fig. 29 VQE experiments (Hλ
, EvolvedOperatorAnsatz,
SPSA): convergence curves of the energy values. Only depth2 circuits from Table 18 are plotted. Clockwise from top left:
λ = 0.2, 0.5, 2.0, 1.0. In all 4 subfigures, ev_op_Hp20 is the best

123

(2025) 85:705

performing variant while ev_op_H is the worst performing variant,
as is evident from how close their corresponding convergence curves
are to the exact energy denoted by the horizontal black dashed line

Eur. Phys. J. C

(2025) 85:705

(S)=2

Fig. 30 VQE experiments (Hλ
, EvolvedOperatorAnsatz,
SPSA): convergence curves of the energy values. Only depth3 circuits from Table 18 are plotted. Clockwise from top left:
λ = 0.2, 0.5, 2.0, 1.0. In all 4 subfigures, ev_op_Hp20 is the best

Page 61 of 80

705

performing variant while ev_op_H is the worst performing variant,
as is evident from how close their corresponding convergence curves
are to the exact energy denoted by the horizontal black dashed line

123

705

Page 62 of 80

Eur. Phys. J. C

(S)=2

Fig. 31 VQE experiments (Hλ
, EvolvedOperatorAnsatz,
SPSA): convergence curves of the energy values. Only depth4 circuits from Table 18 are plotted. Clockwise from top left:
λ = 0.2, 0.5, 2.0, 1.0. In all 4 subfigures, ev_op_Hp20 is the best

D TwoLocal versus EfficientSU2
D.1  = 2 bosonic SU (2) model
See Figs. 32, 33, 35, 36, 37, 38 and 39.

123

(2025) 85:705

performing variant while ev_op_H is the worst performing variant,
as is evident from how close their corresponding convergence curves
are to the exact energy denoted by the horizontal black dashed line

Eur. Phys. J. C

(2025) 85:705

=2 , EfficientSU2&TwoLocal,
Fig. 32 VQE experiments (Hλ=0.2
COBYLA): Comparison of the performances of TwoLocal circuits
and EfficientSU2, variant by variant using COBYLA optimizer.
All 8 variants of TwoLocal outperform or are on par with the corresponding 8 variants of EfficientSU2, as is evident from the orange

Page 63 of 80

705

line representing the TwoLocal variant converges at a lower/the same
value than/as the blue line representing the EfficientSU2 variant.
Both TwoLocal & EfficientSU2 variants involving R Z rotation
block fail to be optimized with COBYLA as their convergence curves
are just straight lines (first row & third row, right subfigure)

123

705

Page 64 of 80

=2 , EfficientSU2&TwoLocal,
Fig. 33 VQE experiments (Hλ=0.2
SPSA): Comparison of the performances of TwoLocal circuits and
EfficientSU2, variant by variant using SPSA optimizer. All 8 variants of TwoLocal outperform or are on par with the corresponding 8
variants of EfficientSU2, as is evident from the orange line representing the TwoLocal variant converges at a lower/the same value

123

Eur. Phys. J. C

(2025) 85:705

than/as the blue line representing the EfficientSU2 variant. Both
TwoLocal & EfficientSU2 variants involving R Z rotation block
fail to be optimized with SPSA as their convergence curves are practically just straight lines coinciding with each other (first row & third
row, right subfigure)

Eur. Phys. J. C

(2025) 85:705

=2 , EfficientSU2&TwoLocal,
Fig. 34 VQE experiments (Hλ=0.5
COBYLA): Comparison of the performances of TwoLocal circuits
and EfficientSU2, variant by variant using COBYLA optimizer.
All 8 variants of TwoLocal outperform or are on par with the corresponding 8 variants of EfficientSU2, as is evident from the orange

Page 65 of 80

705

line representing the TwoLocal variant converges at a lower/the same
value than/as the blue line representing the EfficientSU2 variant.
Both TwoLocal & EfficientSU2 variants involving R Z rotation
block fail to be optimized with COBYLA as their convergence curves
are just straight lines (first row & third row, right subfigure)

123

705

Page 66 of 80

=2 , EfficientSU2&TwoLocal,
Fig. 35 VQE experiments (Hλ=0.5
SPSA): comparison of the performances of TwoLocal circuits and
EfficientSU2, variant by variant using SPSA optimizer. All 8 variants of TwoLocal outperform or are on par with the corresponding 8
variants of EfficientSU2, as is evident from the orange line representing the TwoLocal variant converges at a lower/the same value

123

Eur. Phys. J. C

(2025) 85:705

than/as the blue line representing the EfficientSU2 variant. Both
TwoLocal & EfficientSU2 variants involving R Z rotation block
fail to be optimized with SPSA as their convergence curves are practically just straight lines coinciding with each other (first row & third
row, right subfigure)

Eur. Phys. J. C

(2025) 85:705

=2 , EfficientSU2&TwoLocal,
Fig. 36 VQE experiments (Hλ=1.0
COBYLA): Comparison of the performances of TwoLocal circuits
and EfficientSU2, variant by variant using COBYLA optimizer.
All 8 variants of TwoLocal outperform or are on par with the corresponding 8 variants of EfficientSU2, as is evident from the orange

Page 67 of 80

705

line representing the TwoLocal variant converges at a lower/the same
value than/as the blue line representing the EfficientSU2 variant.
Both TwoLocal & EfficientSU2 variants involving R Z rotation
block fail to be optimized with COBYLA as their convergence curves
are just straight lines (first row & third row, right subfigure)

123

705

Page 68 of 80

=2 , EfficientSU2&TwoLocal,
Fig. 37 VQE experiments (Hλ=1.0
SPSA): Comparison of the performances of TwoLocal circuits and
EfficientSU2, variant by variant using SPSA optimizer. All 8 variants of TwoLocal outperform or are on par with the corresponding 8
variants of EfficientSU2, as is evident from the orange line representing the TwoLocal variant converges at a lower/the same value

123

Eur. Phys. J. C

(2025) 85:705

than/as the blue line representing the EfficientSU2 variant. Both
TwoLocal & EfficientSU2 variants involving R Z rotation block
fail to be optimized with SPSA as their convergence curves are practically just straight lines coinciding with each other (first row & third
row, right subfigure)

Eur. Phys. J. C

(2025) 85:705

=2 , EfficientSU2&TwoLocal,
Fig. 38 VQE experiments (Hλ=2.0
COBYLA): Comparison of the performances of TwoLocal circuits
and EfficientSU2, variant by variant using COBYLA optimizer.
All 8 variants of TwoLocal outperform or are on par with the corresponding 8 variants of EfficientSU2, as is evident from the orange

Page 69 of 80

705

line representing the TwoLocal variant converges at a lower/the same
value than/as the blue line representing the EfficientSU2 variant.
Both TwoLocal & EfficientSU2 variants involving R Z rotation
block fail to be optimized with COBYLA as their convergence curves
are just straight lines (first row & third row, right subfigure)

123

705

Page 70 of 80

=2 , EfficientSU2&TwoLocal,
Fig. 39 CVQE experiments (Hλ=2.0
SPSA): Comparison of the performances of TwoLocal circuits and
EfficientSU2, variant by variant using SPSA optimizer. All 8
variants of TwoLocal outperform or are on par with the corresponding
8 variants of EfficientSU2, as is evident from the orange line
representing the TwoLocal variant converges at a lower/the same

123

Eur. Phys. J. C

(2025) 85:705

value than/as the blue line representing the EfficientSU2 variant.
Both TwoLocal & EfficientSU2 variants involving R Z rotation
block fail to be optimized with SPSA as their convergence curves are
practically just straight lines coinciding with each other (first row &
third row, right subfigure)

Eur. Phys. J. C

(2025) 85:705

Page 71 of 80

705

D.2  = 4 bosonic SU (2) model
See Figs. 40, 41, 42, 43, 44, 45, 46 and 47.

=4 , EfficientSU2&
Fig. 40 VQE
experiments
(Hλ=0.2
TwoLocal, COBYLA): Comparison of the performances of
TwoLocal circuits and EfficientSU2, variant by variant using
COBYLA optimizer. Apart from tl_Ry_f (3rd row, left subfigure) and tl_RyY_f (4th row, right subfigure), the remaining 6
variants of TwoLocal outperform the corresponding 8 variants of

EfficientSU2, as is evident from the orange line representing
the TwoLocal variant converges at a lower value than the blue
line representing the EfficientSU2 variant. Both TwoLocal
& EfficientSU2 variants involving R Z rotation block fail to be
optimized with COBYLA as their convergence curves are just straight
lines coinciding with each other (1st row & 3rd row, right subfigure)

123

705

Page 72 of 80

=4 , EfficientSU2&TwoLocal,
Fig. 41 VQE experiments (Hλ=0.2
SPSA): Comparison of the performances of TwoLocal circuits
and EfficientSU2, variant by variant using COBYLA optimizer.
Apart from tl_RyRz_f (4th row, left subfigure), the remaining 7
variants of TwoLocal outperform the corresponding 8 variants of
EfficientSU2, as is evident from the orange line representing

123

Eur. Phys. J. C

(2025) 85:705

the TwoLocal variant converges at a lower value than the blue
line representing the EfficientSU2 variant. Both TwoLocal &
EfficientSU2 variants involving R Z rotation block fail to be optimized with COBYLA as their convergence curves are just straight lines
coinciding with each other (1st row & 3rd row, right subfigure)

Eur. Phys. J. C

(2025) 85:705

=4 , EfficientSU2&TwoLocal,
Fig. 42 VQE experiments (Hλ=0.5
COBYLA): Comparison of the performances of TwoLocal circuits
and EfficientSU2, variant by variant using COBYLA optimizer.
All 8 variants of TwoLocal outperform or are on par with the corresponding 8 variants of EfficientSU2, as is evident from the orange
line representing the TwoLocal variant converges at a lower/the same

Page 73 of 80

705

value than/as the blue line representing the EfficientSU2 variant.
Both TwoLocal & EfficientSU2 variants involving R Z rotation
block fail to be optimized with COBYLA as their convergence curves
are just straight lines coinciding with each other (1st row & 3rd row,
right subfigure)

123

705

Page 74 of 80

=4 , EfficientSU2&TwoLocal,
Fig. 43 VQE experiments (Hλ=0.5
SPSA): comparison of the performances of TwoLocal circuits and
EfficientSU2, variant by variant using SPSA optimizer. All 8 variants of TwoLocal outperform or are on par with the corresponding 8
variants of EfficientSU2, as is evident from the orange line representing the TwoLocal variant converges at a lower/the same value

123

Eur. Phys. J. C

(2025) 85:705

than/as the blue line representing the EfficientSU2 variant. Both
TwoLocal & EfficientSU2 variants involving R Z rotation block
fail to be optimized with SPSA as their convergence curves are just
straight lines coinciding with each other (1st row & 3rd row, right subfigure)

Eur. Phys. J. C

(2025) 85:705

=4 , EfficientSU2&TwoLocal,
Fig. 44 VQE experiments (Hλ=1.0
COBYLA): comparison of the performances of TwoLocal circuits
and EfficientSU2, variant by variant using COBYLA optimizer.
All 8 variants of TwoLocal outperform the corresponding 8 variants of EfficientSU2, as is evident from the orange line represent-

Page 75 of 80

705

ing the TwoLocal variant converges at a lower value than the blue
line representing the EfficientSU2 variant. Both TwoLocal &
EfficientSU2 variants involving R Z rotation block fail to be optimized with COBYLA as their convergence curves are just straight lines
coinciding with each other (1st row & 3rd row, right subfigure)

123

705

Page 76 of 80

=4 , EfficientSU2&TwoLocal,
Fig. 45 VQE experiments (Hλ=1.0
SPSA): comparison of the performances of TwoLocal circuits and
EfficientSU2, variant by variant using SPSA optimizer. Apart from
tl_Ry_c (first row, left subfigure) and tl_RyY_f (4th row, right
subfigure), the remaining 6 variants of TwoLocal outperform or are
on par with the corresponding 8 variants of EfficientSU2, as is

123

Eur. Phys. J. C

(2025) 85:705

evident from the orange line representing the TwoLocal variant converges at a lower/the same value than/as the blue line representing the
EfficientSU2 variant. Both TwoLocal & EfficientSU2 variants involving R Z rotation block fail to be optimized with SPSA as
their convergence curves are just straight lines coinciding with each
other (1st row & 3rd row, right subfigure)

Eur. Phys. J. C

(2025) 85:705

=4 , EfficientSU2&TwoLocal,
Fig. 46 VQE experiments (Hλ=2.0
COBYLA): comparison of the performances of TwoLocal circuits
and EfficientSU2, variant by variant using COBYLA optimizer.
All 8 variants of TwoLocal outperform or are on par with the corresponding 8 variants of EfficientSU2, as is evident from the orange
line representing the TwoLocal variant converges at a lower/the same

Page 77 of 80

705

value than/as the blue line representing the EfficientSU2 variant.
Both TwoLocal & EfficientSU2 variants involving R Z rotation
block fail to be optimized with COBYLA as their convergence curves
are just straight lines coinciding with each other (1st row & 3rd row,
right subfigure)

123

705

Page 78 of 80

=4 , EfficientSU2&TwoLocal,
Fig. 47 VQE experiments (Hλ=2.0
SPSA): comparison of the performances of TwoLocal circuits and
EfficientSU2, variant by variant using SPSA optimizer. Apart
from tl_Ry_f (3rd row, left subfigure), the remaining 7 variants of
TwoLocal outperform or are on par with the corresponding 8 variants
of EfficientSU2, as is evident from the orange line representing

123

Eur. Phys. J. C

(2025) 85:705

the TwoLocal variant converges at a lower/the same value than/as the
blue line representing the EfficientSU2 variant. Both TwoLocal
& EfficientSU2 variants involving R Z rotation block fail to be
optimized with SPSA as their convergence curves are just straight lines
coinciding with each other (1st row & 3rd row, right subfigure)

Eur. Phys. J. C

(2025) 85:705

References
1. M.D. Anis et al., Qiskit: an open-source framework for quantum
computing (2021). https://www.ibm.com/quantum/qiskit
2. Cirq Developers, Cirq (2021). https://github.com/quantumlib/
Cirq/graphs/contributors
3. S.P. Jordan, K. Lee, J. Preskill, Quantum algorithms for quantum
field theories. Science 336(6085), 1130–1133 (2012)
4. S.P. Jordan, K.S.M. Lee, J. Preskill, Quantum algorithms for
fermionic quantum field theories (2014). arXiv:1404.7115 [hepth, quant-ph]
5. S.P. Jordan, K. Lee, J. Preskill, Quantum computation of scattering
in scalar quantum field theories. Quantum Inf. Comput. 14, 1014–
1080 (2014). arXiv:1112.4833v2 [hep-th]
6. A. Hardy et al., Optimized Quantum Simulation Algorithms for
Scalar Quantum Field Theories. arXiv: 2407.13819v1 [quant-ph]
7. N.A. Zemlevskiy, Scalable Quantum Simulations of Scattering in
Scalar Field Theory on 120 Qubits. arXiv: 2411.02486 [quant-ph]
8. C.W. Bauer et al., Quantum Simulation for High Energy Physics,
Snowmass (2021). arXiv:2204.0338 [quant-ph]
9. A. Joseph, J.-P. Varela, M.P. Watts, T. White, Y. Feng, M. Hassan,
M. McGuigan, Quantum Computing for Inflationary, Dark Energy
and Dark matter Cosmology. arXiv:2105.13849
10. A. Joseph, T. White, V. Chandra, M. McGuigan, Quantum Computing of Schwarzschild-de Sitter Black Holes and Kantowski–Sachs
Cosmology. arXiv:2202.09906
11. V. Chandra, M. McGuigan, Quantum Computing for Rotating,
Charged and String Theory Black Holes. arXiv:2207.03085
12. H. Gharibyan, M.Hanada, M. Honda, J. Liu, Toward simulating
Superstring/M-theory on a quantum computer. arXiv:2011.06573
13. L. Garcia-Alvarez, I.L. Egusquiza, L. Lamata, A. del Campo,
J. Sonner, E. Solano, Digital Quantum Simulation of Minimal
AdS/CFT. arXiv:1607.08560v1
14. R. Babbush, D.W. Berry, H. Neven, Quantum simulation of the
Sachdev–Ye–Kitaev model by asymmetric qubitization. Phys. Rev.
A 99, 040301 (2019). arXiv:1806.02793v2 [quant-ph]
15. Y. Feng, M. McGuigan, T. White, Superconformal Quantum
Mechanics on a Quantum Computer. arXiv:2201.00805
16. E. Rinaldi, X. Han, M. Hassan, Y. Feng, F. Nori, M. McGuigan,
M. Hanada, Matrix-model simulations using quantum computing,
deep learning, and lattice Monte Carlo. PRX Quantum 3, 010324
(2022)
17. https://github.com/erinaldi/bmn2-qiskit/blob/main/notebooks/
QISKIT_bosonic_matrices_VQE.ipynb . https://github.com/
erinaldi/bmn2-qiskit/blob/main/notebooks/QISKIT_susy_
matrices_VQE.ipynb. Accessed Mar 2025
18. D. Wecker, M.B. Hastings, M. Troyer, Towards practical quantum variational algorithms. Phys. Rev. A 92, 042303 (2015).
arXiv:1507.08969v2 [quant-ph]
19. N. Moll, P. Barkoutsos, L.S. Bishop, J.M. Chow, A. Cross, D.J.
Egger, S. Filipp, A. Fuhrer, J.M. Gambetta, M. Ganzhorn, A. Kandala, A. Mezzacapo, P. Muller, W. Riess, G. Salis, J. Smolin, I. Tavernelli, K. Temme, Quantum optimization using variational algorithms on near-term quantum devices. Quantum Sci. Technol. 3,
030503 (2018)
20. M. Cerezo, A. Arrasmith, R. Babbush, S.C. Benjamin, S. Endo, K.
Fujii, J.R. McClean, K. Mitarai, X. Yuan, L. Cincio, P.J. Coles, Variational quantum algorithms. Nat. Rev. Phys. 3, 625–644 (2021).
arXiv:2012.09265v2 [quant-ph]
21. J. Tilly, H. Chen, S. Cao, D. Picozzi, K. Setia, Y. Li, E. Grant,
L. Wossnig, I. Rungger, G.H. Booth et al., The variational
quantum Eigensolver: a review of methods and best practices.
arXiv:2111.05176 [quant-ph]
22. Qiskit EfficientSU2 circuit. https://docs.quantum.ibm.
com/api/qiskit/qiskit.circuit.library.EfficientSU2

Page 79 of 80

705

23. Qiksit TwoLocal circuit. https://docs.quantum.ibm.com/api/
qiskit/qiskit.circuit.library.TwoLocal
24. Qiksit
EvolvedOperatorAnsatz
circuit:
https://
docs.quantum.ibm.com/api/qiskit/qiskit.circuit.library.
EvolvedOperatorAnsatz. See also https://docs.quantum.ibm.
com/api/qiskit/qiskit.circuit.library.evolved_operator_ansatz
25. N. Kim, J.-H. Park, Massive super Yang–Mills quantum mechanics:
classification and the relation to supermembrane. Nucl. Phys. B
759, 249–282 (2006). arXiv:hep-th/0607005
26. K.N. Anagnostopoulos, M. Hanada, J. Nishimura, S. Takeuchi,
Monte Carlo studies of supersymmetric matrix quantum mechanics
with sixteen supercharges at finite temperature. Phys. Rev. Lett.
100, 021601 (2008). arXiv:0707.4454
27. M. Hanada, Y. Hyakutake, G. Ishiki, J. Nishimura, Holographic
description of quantum black hole on a computer. Science
344(6186), 882–885. arXiv:1311.5607
28. M.S. Costa, L. Greenspan, J. Penedones, J. Santos, Thermodynamics of the BMN matrix model at strong coupling. J. High Energy
Phys. 2015, 69 (2015). arXiv:1411.5541
29. P. Jordan, E. Wigner, Über das Paulische Äquivalenzverbot. Z.
Phys. 47, 631–651 (1928)
30. H.R. Grimsley, S.E. Economou, E. Barnes, N.J. Mayhall, An
adaptive variational algorithm for exact molecular simulations on
a quantum computer. Nat. Commun. (2019). https://doi.org/10.
1038/s41467-019-10988-2. arXiv: 1812.11173
31. R.C. Farrell, M. Illa, A.N. Ciavarella, M.J. Savage, Scalable circuits for preparing ground states on digital quantum computers:
the Schwinger model vacuum on 100 qubits. PRX Quantum 5(2),
020315 (2024). arXiv:2308.04481
32. P.G. Anastasiou, Y. Chen, N.J. Mayhall, E. Barnes, S.E. Economou,
TETRIS-ADAPT-VQE: an adaptive algorithm that yields shallower, denser circuit Ansätze. Phys. Rev. Res. 6, 013254 (2024)
33. Qiskit Estimator from qiskit_aer, https://qiskitaer/stubs/qiskit_aer.primitives.Estimator.html#qiskit_aer.
primitives.Estimator. See also the source code at https://github.
com/Qiskit/qiskit-aer/blob/main/qiskit_aer/primitives/estimator.
py
34. Qiskit Ecosystem, Qiskit Aer 0.15.0. https://qiskit.github.io/
qiskit-aer/apidocs/aer.html
35. Qiskit VQE tutorial. https://qiskit-community.github.io/
qiskit-algorithms/tutorials/03_vqe_simulation_with_noise.html
36. Qiskit
NoiseModel,
https://qiskit.github.io/qiskit-aer/
apidocs/aer_noise.html.
https://qiskit.github.io/qiskit-aer/
stubs/qiskit_aer.noise.NoiseModel.html.
https://qiskit.github.
io/qiskit-aer/tutorials/3_building_noise_models.html
37. Qiskit error mitigation techniques https://docs.quantum.ibm.
com/guides/configure-error-mitigation.
https://docs.quantum.
ibm.com/guides/error-mitigation-and-suppression-techniques
38. E. van den Berg, Z.K. Minev, K. Temme, Model-free readouterror mitigation for quantum expectation values. Phys. Rev. A 105,
032620 (2022)
39. Y. Kim, A. Eddins, S. Anand, K.X. Wei, E. van den Berg, S. Rosenblatt, H. Nayfeh, Y. Wu, M. Zaletel, K. Temme, A. Kandala, Evidence for the utility of quantum computing before fault tolerance.
Nature 618, 500–505 (2023)
40. Qiskit error mitigation techniques with Estimator
tutorial.
https://learning.quantum.ibm.com/tutorial/
combine-error-mitigation-options-with-the-estimator-primitive
41. D. Wierichs, C. Gogolin, M. Kastoryano, Avoiding local minima
in variational quantum eigensolvers with the natural gradient optimizer. Phys. Rev. Res. 2, 043246 (2020)
42. M. Wiedmann, M. Hölle, M. Periyasamy, N. Meyer, C. Ufrecht, D.
D. Scherer, A. Plinge, C. Mutschler, An empirical comparison of
optimizers for quantum machine learning with SPSA-based gradients, in 2023 IEEE International Conference on Quantum Comput-

123

705

Page 80 of 80

ing and Engineering (QCE). https://doi.org/10.1109/QCE57702.
2023.00058. arXiv:2305.00224
43. A. Pellow-Jarman, I. Sinayskiy, A. Pillay, F. Petruccione, A comparison of various classical optimizers for a variational quantum linear solver. https://doi.org/10.1007/s11128-021-03140-x.
arXiv:2106.08682
44. Qiskit full list of optimizers. https://qiskit-community.github.
io/qiskit-algorithms/apidocs/qiskit_algorithms.optimizers.html
45. https://learning.quantum.ibm.com/course/
variational-algorithm-design/optimization-loops
46. J.C. Spall, An overview of the simultaneous perturbation method
for efficient optimization. Johns Hopkins APL Technical Digest,
vol. 19, no. 4, pp. 482-492. See also ‘SPSA algorithm’. https://
www.jhuapl.edu/SPSA/
47. M.J.D. Powell, A direct search optimization method that models the objective and constraint functions by linear interpolation,
in: Advances in Optimization and Numerical Analysis, pp. 51–67
(1994)
48. J.A. Nelder, R. Mead, A simplex method for function minimization.
Comput. J. 7(4), 308–313 (1965)
49. D. Kraft, A software package for sequential quadratic programming, Technical Report DFVLR-FB 88–28. Institut für Dynamik
der Flugsysteme, Oberpfaffenhofen (1988)
50. D.P. Kingma, J. Ba, Adam: a method for stochastic optimization.
arXiv:1412.6980
51. J.R. McClean, S. Boixo, V.N. Smelyan-skiy, R. Babbush, H. Neven,
Barren plateaus in quantum neural network training landscapes.
Nat. Commun. 9, 1 (2018)
52. A. Arrasmith, M. Cerezo, P. Czarnik, L. Cincio, P.J. Coles, Effect
of barren plateaus on gradient-free optimization. Quantum 5, 558
(2021). arXiv:2011.12245
53. E. Grant, L. Wossnig, M. Ostaszewski, M. Benedetti, An initialization strategy for addressing barren plateaus in parametrized quantum circuits. Quantum 3, 214 (2019). arXiv:1903.05076
54. S. Wang, E. Fontana, M. Cerezo, K. Sharma, A. Sone, L. Cincio,
P.J. Coles, Noise-induced barren plateaus in variational quantum
algorithms. Nat. Commun. 12, 6961 (2021). arXiv:2007.14384
55. M. Cerezo, A. Sone, T. Volkoff, L. Cincio, P.J. Coles, Cost function dependent barren plateaus in shallow parametrized quantum
circuits. Nat. Commun. 12, 1791 (2021). arXiv:2001.00550
56. J.C. Napp, Quantifying the barren plateau phenomenon for a model
of unstructured variational ansätze. arXiv:2203.06174

123

Eur. Phys. J. C

(2025) 85:705

57. Text files contanining the full expression for the  = 4 bosonic
SU (2) Hamiltonians containing 895 Pauli string operators at different couplings λ. λ = 0.2: https://github.com/lorrespz/matrix_
model_quantum_computing_vqe/blob/main/utility/pauliH_L4_
g0.2.txt λ = 0.5: https://github.com/lorrespz/matrix_model_
quantum_computing_vqe/blob/main/utility/pauliH_L4_g0.5.txt.
λ = 1.0: https://github.com/lorrespz/matrix_model_quantum_
computing_vqe/blob/main/utility/pauliH_L4_g1.0.txt. λ = 2.0:
https://github.com/lorrespz/matrix_model_quantum_computing_
vqe/blob/main/utility/pauliH_L4_g2.0.txt
58. Full list of operators used for 
=
4
EvolvedOperatorAnsatz
circuits
https://github.com/
lorrespz/matrix_model_quantum_computing_vqe/blob/main/
L%3D4_EvolvedOperator/ops_spectrum/L4_operator_spectrum.
ipynb
59. A. Bentellis, A. Matic-Flierl, C.B. Mendl, J.M. Lorenz, Benchmarking the Variational Quantum Eigensolver using different quantum hardware, in 2023 IEEE International Conference on Quantum
Computing and Engineering (QCE), Bellevue, pp. 518–523 (2023).
arXiv:2305.07092v1 [quant-ph]
60. https://github.com/qiskit-community/qiskit-community-tutorials/
blob/master/chemistry/adaptive_VQE.ipynb.
https://
qiskit-community.github.io/qiskit-algorithms/stubs/qiskit_
algorithms.AdaptVQE.html
61. Qiskit Ecosystem, Qiskit Algorithms 0.3.1. https://
qiskit-community.github.io/qiskit-algorithms/index.html

