PHYSICAL REVIEW RESEARCH 7, 013221 (2025)

Enhanced natural parameterized quantum circuit
Yuquan Chen,1,2,* Yanjun Hou,1,2,* Zeyuan Wang ,3 Tianyun Wang,1,2 Ze Wu,1,2,†
Zhaokai Li ,1,2,4,‡ and Xinhua Peng 1,2,4,§
1

CAS Key Laboratory of Microscale Magnetic Resonance and School of Physical Sciences,
University of Science and Technology of China, Hefei 230026, China
2
CAS Center for Excellence in Quantum Information and Quantum Physics,
University of Science and Technology of China, Hefei 230026, China
3
Department of Physics, University of Michigan, Ann Arbor, Michigan 48109, USA
4
Hefei National Laboratory, University of Science and Technology of China, Hefei 230088, China
(Received 29 April 2024; accepted 8 January 2025; published 27 February 2025)
The classical-quantum interface for loading classical data into quantum systems is an indispensable component of quantum information processing, and the parameterized quantum circuit (PQC) represents significant
methodology in this area. However, a challenge in designing parameterized quantum circuits that can fully utilize
limited qubit resources while accurately representing classical data remains. To address this issue, we propose
the enhanced natural parameterized quantum circuit (ENPQC), which achieves the maximum parameter capacity
of quantum systems and preserves the local structure of the original dataset. To make the encoding circuits
more experiment friendly, we further provide two near-optimal circuits that achieve near-maximum capacity and
are comparable in complexity to the existing PQCs. We numerically show that the ENPQC overwhelms other
encoding methods for multiple datasets, demonstrating its potential for machine learning tasks. Furthermore,
we experimentally validate our scheme by demonstrating a three-class classification task on an NMR platform,
which achieves over 97% accuracy. This work provides a powerful tool for the classical-quantum interface,
paving the way for quantum big data processing during the noisy intermediate-scale quantum era.
DOI: 10.1103/PhysRevResearch.7.013221

I. INTRODUCTION

Quantum computing and quantum information provide a
tremendous opportunity to revolutionize the way we deal
with big data [1,2] due to their exponential acceleration
capability and their enhanced data encryption and security
mechanisms [3,4]. In order to leverage the superiority of
quantum technologies for classical tasks, a crucial prerequisite is determining how to efficiently load classical data
into quantum systems [5]. A good classical-quantum interface
can efficiently encode more classical data into a quantum device by consuming fewer quantum resources, including fewer
qubits and shorter control sequences. Moreover, the encoded
quantum states should reflect the topological relationships of
the original data, which has a great impact on the functionality
and accuracy of subsequent quantum data processing tasks
[6,7].

*

These authors contributed equally to this work.
Contact author: wuze@ustc.edu.cn
‡
Contact author: zkli@ustc.edu.cn
§
Contact author: xhpeng@ustc.edu.cn
†

Published by the American Physical Society under the terms of the
Creative Commons Attribution 4.0 International license. Further
distribution of this work must maintain attribution to the author(s)
and the published article’s title, journal citation, and DOI.
2643-1564/2025/7(1)/013221(8)

In the early stages, classical data were directly mapped
to the state vector of qubits and loaded into a quantum device through quantum state preparation [8–14]. This encoding
strategy encompasses various schemes such as basis encoding
[7], amplitude/phase encoding [15–18], and quantum random
access memory [19]. Since the classical data are directly
stored in explicit quantum entities, such as polarizations and
phases, the encoding scheme has clear physical meaning
[20–22]. However, the biggest drawback is that the preparation of general quantum states with high fidelity is always a
challenge task, especially in cases involving a large number
of qubits [9,13]. Therefore, the classical-quantum interface
based on state preparation gradually becomes inadequate for
the task of loading large datasets to quantum devices, particularly as we enter the noisy intermediate-scale quantum (NISQ)
era [23–26].
In recent years, heuristic encoding strategies based on
parameterized quantum circuits (PQCs) have garnered increasing attention [27,28]. As depicted in Fig. 1(a), by
encoding the classical data x into the rotation angles θ of the
single-qubit gates, the PQC-based interface can circumvent
the requirement for preparing target states and load the dataset
with high efficiency [6,29,30]. In general, the encoded states
at the end of the PQC will contain the information about x in
an abstract and nonlinear manner. A novel encoding scheme
known as the natural parameterized quantum circuit (NPQC)
has been proposed [31]. Within this framework, the distance
measure between the classical input data is maintained in the

013221-1

Published by the American Physical Society

YUQUAN CHEN et al.

PHYSICAL REVIEW RESEARCH 7, 013221 (2025)

the implementation of permutations is not straightforward in
practical experiments, we further propose specific entangling
structures containing only CNOT gates which can achieve the
capacity near maximum value. Based on the nuclear magnetic
resonance (NMR) quantum platform, we then experimentally
demonstrate our encoding scheme in a three-class classification task and achieve 97% classification accuracy on the
test set. Our work develops a PQC-based encoding strategy with high efficiency, good interpretability, and maximum
capacity, which provides a superior classical-quantum interface for quantum machine learning and quantum big data
processing.

II. ENHANCED NPQC SCHEME

FIG. 1. PQC-based classical-quantum interfaces and the comparison of two NPQC encoding schemes. (a) A schematic diagram
illustrating the loading of classical data x into a quantum system
using a general PQC. Here, θi denotes the rotation angles of the
single-qubit gates, and Uent is the entangling gate. (b) An example
of the original NPQC encoding scheme, which enables the loading
of at most 20 classical parameters into a four-qubit system. (c) Our
proposed ENPQC encoding scheme for a four-qubit system. The general permutation Uπ is employed as the entangling gate Uent , and its
permutation relation is depicted at the bottom. The encoding scheme
reaches the maximum parameter capacity (the degree of freedom of
the four-qubit pure state).

encoded quantum states. The input data can be transformed
into a higher-dimensional space, where they become linearly
separable, consistent with the widely utilized Gaussian kernel function in machine learning applications. Therefore, the
NPQC serves as a classical-quantum interface with both high
encoding efficiency and good interpretability.
However, compared to other encoding schemes, the original NPQCs do not exhibit a clear advantage in parameter
capacity, which denotes the amount of data that can be independently loaded and is upper bounded by the degree of
freedom (DOF) of the quantum device’s pure state [32–36].
Improving the encoding capacity could help us fully utilize
the Hilbert space of quantum devices and effectively reduce
the width and depth of the encoding circuits [35], which is
of great significance for NISQ data processing tasks. For the
NPQC scheme, the encoding capacity is closely related to the
properties of entangling gates in the circuit [31], but it is still
an open question whether and how the maximum encoding
capacity can be achieved.
In this work, we demonstrate in both theory and experiment
an enhanced classical-quantum interface based on an ansatz
that achieves the maximum encoding capacity. First, we theoretically prove that designing special permutations as the
entangling gates allows for achieving the maximum encoding capacity of 2N+1 − 2 in N-qubit PQCs. Considering that

In PQC-based classical-quantum interfaces [29,30], the
quantum circuit architecture comprises layers that include
single-qubit rotations denoted by (Rx , Ry , Rz ), along with an
entangling gate designated as Uent . The classical input data x
are mapped to the rotation angles of these qubits through a linear transformation represented by θ = θ r + cx; this encoding
process is illustrated in Fig. 1(a). Here, x represents a classical
feature vector, θ r represents the reference parameters, and c
is a scaling coefficient. In this way, one not only can load
the classical information into the qubits but can also define
a kernel function that connects the original data space with
the Hilbert space of the quantum state. Specifically, under the
condition ||cx||  1, the fidelity between two encoded states
simplifies into a form resembling a weighted Gaussian kernel
function [37], signifying the PQC as the corresponding feature
mapping:
c2

|ψ (θ i )|ψ (θ j )|2 ≈ e− 4 (xi −x j ) F (θr )(xi −x j ) .
T

(1)

Here, F (θ r ) is the quantum Fisher information matrix, defined
as Fi j (θ) = 4[∂i ψ|∂ j ψ − ∂i ψ|ψψ|∂ j ψ], with |∂i ψ =
∂|ψ (θ)/∂θi [38,39]. Furthermore, if F (θ r ) = 1 for a certain
circuit, the inner product of two encoded states corresponds
to the standard Gaussian kernel that is commonly utilized in
various machine learning applications. This variant of PQC,
called the natural PQC, has a Euclidean quantum geometry at
the reference parameter θ r , facilitating faster training of variational quantum algorithms and enhancing quantum metrology
applications [31].
The number of noncorrelated classical parameters embedded in the quantum state is limited by the DOF of the quantum
system. Here, the effective quantum dimension GC (θ) =
rank[F (θ)] is defined to measure the parameter capacity of
a given N-qubit circuit [32]. As for the NPQC structure that
maintains the condition F (θ r ) = 1, we can gradually increase
the number of circuit layers until the parameter capacity is
saturated. At this point, the maximum value of GC (θ r ), denoted as CN , can be defined as the structure’s NPQC capacity.
For example, as depicted in Fig. 1(b), the original NPQC
architecture tends to be sparse, and in most layers only N/2
qubits are utilized. The maximal capacity of the NPQC is
N (2N/2 + 1) [31], indicating that the number of independent
parameters will not increase with the addition of extra layers.

013221-2

ENHANCED NATURAL PARAMETERIZED QUANTUM …

PHYSICAL REVIEW RESEARCH 7, 013221 (2025)

A. Analytical solution for PQC design

Here, we introduce the enhanced NPQC (ENPQC), which
aims to maximize the parameter capacity up to the full
DOF of the N-qubit pure state (2N+1 − 2) while maintaining the Euclidean quantum geometry, i.e., F (θ r ) = 1. As
illustrated in Fig. 1(c), the ENPQC consists of single-qubit
rotations and an entangling gate per layer, with the encoded

state represented as |ψ (θ) = L−1
l=0 Ul (θ)|0̄, where Ul (θ) =
N−1
(n)
(n)
)Ry (θl,y
) and N and L denote the number
Uent n=0 Rx (θl,x
of qubits and circuit layers, respectively. Throughout this
work, we adopt zero-based numbering and use little-endian
qubit ordering, with |n̄ (n = 0, 1, . . . , 2N − 1) representing
the computational basis states, where n̄ is the N-digit binary
representation of n.
Consider a scenario where the reference parameters θ r = 0
and the entanglement gate satisfies Uent |0̄ = |0̄, a property
commonly observed in an ansatz constructed from controlled
gates. Thus, the matrix element of F (θ r ) associated with the

(n)
and θl(n ,β) simplifies to
parameters θl,α




F(ll  ,nn ,αβ ) (0) = Re0̄|σ̂α(n) (Uent )l−l σ̂β(n ) |0̄.

(2)

For l = l  , the condition F(ll,nn ,αβ ) (0) = δnn δαβ ensures
that the diagonal elements of F (θ r ) are equal to 1. For
l = l  , using σx(n) |0̄ = |2n  and σy(n) |0̄ = i|2n , the offdiagonal elements with α = β result in F(ll  ,nn ,αβ ) (0) =

Re{±i2n |(Uent )l−l |2n }, which vanish if Uent is additionally
restricted to be real in the computational basis. Consequently,
the remaining matrix elements to evaluate are of the form


F(l=l  ,nn ,αα) (0) = 2n |(Uent )l−l |2n .

(3)

If Eq. (3) yields a nonzero result, it indicates interdependence
between the two parameters involved, leading to a mixing of
the information they encode; thus, one of the parameters must
be removed. This process facilitates the establishment of the
layout of parameterized gates in circuits.
Moving forward, we demonstrate in theory that by utilizing
the quantum state permutation as the entangling gate (Uent =
Uπ ) with a specific design, the parameter capacity of the
ENPQC can achieve the DOF of pure states. The details are as
follows. The operator Uπ acts on the 2N computational basis
states by applying a permutation π , such that Uπ |n̄ = |π (n).
Substituting this into Eq. (3) results in




F(l=l  ,nn ,αα) (0) = I[π l −l (2n ) = 2n ],

(4)

where I[X ] denotes the indicator function, which equals 1
if X is true and 0 otherwise. Since the permutation can be
expressed as a product of disjoint cyclic permutations (or
cycles), we divide π into three parts:
π = (0) ◦ [σ1 · · · σi · · · ] ◦ [ 1 · · · i · · · ],

(5)

where the cycle (0) arises from the condition Uent |0̄ = |0̄,
σi represents cycles containing at least one element that is
a power of 2, and i represents cycles that exclude powers
of 2. We define {ln }N−1
n=0 as a structural characteristic of the
permutation π , with its definition and connection to the circuit
layout formalized in Proposition 1.
Proposition 1. For a 2N -permutation π with π (0) = 0
and ln (n = 0, 1, . . . , N − 1) as the minimum positive integer

such that π −ln (2n ) is a power of 2, (a) ∀ 0 ⩽ n, n < N, 0 ⩽


l < ln , 0 ⩽ l  < ln , and π l −l (2n ) = 2n if and only if l = l 
and n = n , and (b) ∀ 0 ⩽ n < N, l ⩾ ln , ∃ 0 ⩽ n < N, 0 ⩽


l  < ln , such that π l −l (2n ) = 2n .

Proof. We consider the cycles containing 2n and 2n . Den
note the L cycle that includes 2 as σ p .



For part (a), if 2n is not in σ p , then clearly, π l −l (2n ) = 2n .

If 2n is in σ p , we consider two cases:

(1) When n = n , the equation σ pl −l (2n ) = 2n holds if and
only if l  − l = kL for some integer k. It holds only when l =
l  since L ⩾ ln and 0 ⩽ l, l  < ln .
(2) When n = n , the definition of ln implies that σ pK (2n ) =
n
2 requires K ⩾ ln or K ⩽ −ln , shown as follows:


·   2n 
  2n ).
σ p = (
  · ·
 · · · 
⩾ln

⩾ln



Given 0 ⩽ l < ln and 0 ⩽ l < ln , it follows that −ln < l  −


l < ln , so σ pl −l (2n ) = 2n .
For part (b), we consider two cases:
(1) If σ p contains only one power of 2, namely, 2n , then L =


ln . There exist n = n and l  = l mod L such that σ l −l (2n ) =
σ kL (2n ) = 2n , k ∈ Z.
(2) If σ p contains M powers of 2 where M ⩾ 2, we denote
them as 2n0 , 2n1 , . . . , 2nM−1 in the reverse order of appearance
in σ p , starting from 2n0 = 2n ,
nM−1
n0
σ p = (
· · 2n1 
 · · · 2  · · · 
 · 
 · ·· 2  ).
lnM−1

ln1

ln0

Thus, σ p is divided into M disjoint intervals, and σ p−l (2n ) must
be in one of them. Formally, we define
⎧
j = 0,
⎪
⎨0
j−1
Lj =
l
1
⩽ j < M,
i=0 ni
⎪
⎩
L
j = M.
For l ⩾ ln , there exists an integer 0 ⩽ q < M such that kL +
Lq ⩽ l < kL + Lq+1 for some k ∈ N. Consequently, there ex

ist n = nq and l  = (l − Lq ) mod L such that σ pl −l (2n ) = 2n .

(n)
Proposition 1 implies that if the parameters θl,α
with l < ln
are chosen to be independent for all n, then all other parameters become redundant in terms of those. Consequently,
the NPQC capacity CN depends on the sum of cycle lengths
having powers of 2: CN = 2 N−1
n=0 ln . The maximum value of
CN , which equals the DOF of N-qubit pure states 2(2N − 1), is
attained if all cycles in π except (0) contain powers of 2. This
implies that all i terms within Eq. (5) are empty. Therefore,
we have found a special class of entanglement gates Uπ for
NPQC and the corresponding circuit construction scheme.
Our ENPQC ansatz is given based on the following rules:
(1) Each layer of the ENPQC ansatz consists of singlequbit rotations {Rx , Ry } and an entangling gate Uπ , with at
most one set of {Rx , Ry } on each qubit per layer.
(2) There are ln layers of {Rx , Ry } on the nth qubit Qn .
When designing a circuit, we can first construct the permutation π , thereby obtaining {ln }N−1
n=0 , and then obtain the
corresponding circuit based on the above two rules. The
number of layers is clearly bounded by max ln N−1
n=0 , with
a minimum of (2N − 1)/N when CN equals the DOF,

013221-3

YUQUAN CHEN et al.

PHYSICAL REVIEW RESEARCH 7, 013221 (2025)

then
K
|2n−1  = |2m−1 ,
UCR

m ⩾ 1,

(7)

K+1 n−1
UCR
|2  = |2N−1 ,

m = 0,

(8)

and vice versa.
Building on this, it suffices to determine the smallest posK0
itive integer K0 such that πCR
(2N−1 ) yields a power of 2,
m0
denoted by 2 ; thus, lm0 = K0 . Assuming that m0 ⩾ 1 without loss of generality, we can deduce from Proposition 2 that
K0 N−2
|2  = |2m0 −1  and lm0 −1 = K0 . By analogy, we have
UCR
ln =

FIG. 2. Different types of entangling patterns and a comparison
of their NPQC capacities. The entangling patterns (a) CNOT ring UCR
and (b) CNOT shuffle UCS and (c) the general permutation Uπ serve as
Uent in Fig. 1(a) to form ENPQC. (d) Comparison of the N-qubit
NPQC capacity in ENPQC with the optimal solution Uπ (green
solid line, reaching pure-state degrees of freedom), CNOT ring (red
scattering), CNOT shuffle (blue scattering), and the original NPQC
(gray dashed line).

indicating that parameter gates are uniformly distributed
across all qubits. In Fig. 1(c), we provide an example of
a permutation that achieves the DOF while minimizing the
number of circuit layers, with {ln }(n = 0, 1, 2, 3) marked at
the bottom. Based on the permutation, we are able to derive
the corresponding quantum circuit, as shown in Fig. 1(c).
In Fig. 2(d), the NPQC capacity for various structures is
depicted in relation to the number of qubits N, ranging from
2 to 40. The green line signifies the maximum capacity of our
ENPQC, equivalent to the degree of freedom of N-qubit pure
states, and the dashed line represents parameter capacities of
the NPQC scheme raised in previous study.
B. Experiment-friendly near-optimal circuits

The implementation of general permutations in experiment
is sometimes challenging [40]; hence, finding some special
entangling structures that are experimentally feasible is important. One common strategy is to construct the entangling
gates using CNOT gates. Here, we first consider the CNOT ring
UCR structure. It involves a consecutive application of CNOT
gates among N adjacent qubit pairs when the last qubit is
treated as a neighbor to the first one, as shown in Fig. 2(a).
We identify a distinctive property of UCR that enables the
efficient computation of ln , as stated in Proposition 2, with
proofs provided in the Supplemental Material [41].
Proposition 2. For 1 ⩽ n < N, if there exist integers K >
0 and 0 ⩽ m < N such that
K
UCR
|2n  = |2m ,

(6)

K0
K0 + 1

n ⩽ m0 ,
n > m0 .

(9)

Hence, the NPQC capacity CN = 2[N (K0 + 1) − m0 − 1].
The encoding part in Fig. 3(a) depicts the three-qubit PQC
utilizing UCR , with K0 = 2 and m0 = 1. To determine K0
and m0 , we propose two numerical approaches. The first involves computing the matrix representation of UCR to derive
the permutation πCR , which incurs exponential computational
complexity. The second approach simulates the evolution
K0 N−1
UCR
|2  = |2m0 , where each application of UCR is expressed as a matrix-vector multiplication,
⎡  ⎤ ⎡
⎤
⎤⎡
0 1 1 · · · 1 QN−1
QN−1
⎢Q ⎥ ⎢1 1 0 · · · 0⎥⎢Q ⎥
⎢ N−2 ⎥ ⎢
⎥⎢ N−2 ⎥
⎢  ⎥ ⎢
⎥
⎥⎢
⎢QN−3 ⎥ = ⎢1 1 1 · · · 0⎥⎢QN−3 ⎥ mod 2, (10)
⎢
⎥ ⎢
⎥
⎥⎢
⎢ .. ⎥ ⎢ .. .. .. . .
.. ⎥⎢ ... ⎥
. . ⎦⎣
⎣ . ⎦ ⎣. . .
⎦
Q0

1

1

1

···

1

Q0

which reduces the scale from 2N to N. This makes it possible
to handle cases with a larger number of qubits N. In Fig. 2(b),
the red diamonds represent the NPQC capacity for the UCR
scenario, surpassing the original NPQC in most cases and
approaching the pure-state DOF in some instances.
To further improve the parameter capacity, we rearrange
the order of CNOT gates in the CNOT ring and construct the
entangling gate referred to as CNOT shuffle UCS , as depicted in
Fig. 2(b). To construct the associated mapping matrix of UCS ,
the process begins with an identity matrix, adding the jth row
to the kth row modulo 2 for each CNOT(Qj , Qk ) applied, where
row j corresponds to qubit Q j . As Proposition 2 is inapplicable in universal cases, each ln (n = 0, . . . , N − 1) must be
computed individually. Given the infeasibility of exhaustively
traversing all N! permutations for large N, hundreds of permutations are randomly sampled using Monte Carlo methods,
and the one yielding the largest CN is selected as the estimate
for the optimal N-qubit UCS . The results, depicted as blue dots
in Fig. 2(d), indicate that the DOF is achieved in most cases
simply by rearranging the elements in the CNOT ring. The
corresponding configurations are provided in Supplementary
Information [41].
The CNOT ring, due to its structure, requires that the CNOT
gates be executed sequentially. In contrast, the CNOT shuffle
may allow for parallel execution of certain quantum gates
depending on the arrangement of the CNOT gates. Notably,
the optimal permutation for UCS may not be unique, offering
additional flexibility for experimental implementation.

013221-4

ENHANCED NATURAL PARAMETERIZED QUANTUM …

PHYSICAL REVIEW RESEARCH 7, 013221 (2025)

as a three-qubit quantum processor. The Hamiltonian of the
NMR sample is

π
Ji j σ̂z(i) σ̂z( j) ,
π νi σ̂z(i) +
(11)
Hs =
2
i
ij
where the parameter νi denotes the chemical shift associated
with the ith spin and Ji j indicates the strength of the scalar
coupling between the ith and jth spins. Our experiments were
performed on a Bruker Avance III 400 MHz spectrometer at
room temperature. The system, initially in the thermal equilibrium state, is first prepared as a pseudopure state (PPS) ρ̂pps =
[(1 − )/8]1 + |000000| by using the selective-transition
approach [46] with a polarization of ≈ 10−5 prior to loading classical data. The experimental fidelity of ρ̂pps is about
99.29%.
The experimental process is illustrated in Fig. 3(a). We
utilize the CNOT ring as the entangling gate and employ
ENPQC to encode classical data {x1 , x2 , . . . , xn } into quantum
operations acting on ρ̂pps , resulting in encoded quantum states.
For an instance x from the wine dataset, it is transformed by
θ = θ r + cx and loaded into the ENPQC to obtain the encoded
state |ψ (θ). Next, we apply a unitary transformation Utrain ,
which is implemented by an NMR shaped pulse sequence
consisting of 2000 adjustable control fields Bi = (Bx(i) , By(i) )
over a duration of δt = 20 ms. The control Hamiltonian is


Bx(i) σ̂x( j) + By(i) σ̂y( j) ,
(12)
Hc (Bi ) = π
j

FIG. 3. Experimental demonstration of multiclass classification
tasks based on the ENPQC encoding scheme. (a) Schematic diagram
of the overall experimental process. The classical wine dataset is
divided into training, validation, and test sets in a 6:2:2 ratio. In the
three-qubit NMR quantum system, we utilize the ENPQC scheme
to encode classical data into quantum states and then determine the
final state after applying an operation with adjustable parameters
denoted as Utrain . By optimizing the parameters in Utrain , we achieve
three-class classification of the input data. (b) Iteration curves during
the training process. The two lines depict the accuracy of the classification for the training set and validation set at different epochs.
(c) Upon completion of training, the simulated reduced density matrices for different qubits in the final states are displayed on the Bloch
sphere. Red, green, and blue correspond to the three classes of the
input data.
III. EXPERIMENTAL DEMONSTRATION OF THE ENPQC

To demonstrate the experimental feasibility of the ENPQC
scheme, we employ this encoding method to perform a threeclass classification task on an NMR quantum system. The
classical dataset we use is the wine dataset [42,43], comprising 178 instances with chemical analyses for three wine
varieties, with each instance containing 13 distinct chemical
attributes. Our task involves classifying wine categories based
on these attributes. The dataset is split into training, validation,
and test sets in a 60:20:20 ratio. The NMR sample used in the
experiment is the iodotrifluoroethylene (C2 F3 I) dissolved in
D-chloroform [44,45], and we utilize three 19 F nuclear spins

and the total evolution operator of the system corresponding
to a single shaped pulse is 
given by Ut (Bi ) = exp{−i[Hs +
Hc (Bi )]δt}. Thus, Utrain = i Ut (Bi ). The encoded states
evolve under Utrain to the final states, where we measure each
qubit’s expectation value σx . The classification of the input
data is determined by the maximum measurement value of
σx  across the qubits. Specifically, let the classification result
given by the circuit for an input instance be k (k ∈ [0, 1, 2]);
we define k as follows:
 
(13)
k = arg maxi σx(i) i=0,1,2 .
Then we define the cost function as follows:
 2

n
1  1   (i)  (i)  2
Cost(x1 , . . . , xn ) =
y − σx j
,
n j=1 3 i=0 j

(14)

where i refers to the ith qubit, j indicates the jth instance
from the wine dataset, and y(i)
j is the class label for the
ith qubit of the jth instance. Minimizing this cost function
optimizes Utrain . We train the parameters B within Utrain using the simultaneous perturbation stochastic approximation
(SPSA) algorithm [47]. SPSA is an efficient optimization
technique that estimates gradients with two measurements
per iteration, independent of the parameter count, offering
robustness against noise and applicability in black-box scenarios without the need for analytical gradients. Based on
the measured expectation values σx  of each qubit, we
calculate the cost function using a classical computer and
iterate the parameters with SPSA. Training is conducted
with a minibatch size of 4 over 18 epochs [41,48,49].
After the cost function converges, we obtain the trained

013221-5

YUQUAN CHEN et al.

PHYSICAL REVIEW RESEARCH 7, 013221 (2025)

parameters B. Using these trained parameters, we can then
determine the accuracy of the circuit on the test set.
Figure 3(b) shows the relationship between the classification accuracy of the training set and the validation set, as
well as the corresponding loss with iterations of the epoch
during the process of training. The final obtained classification accuracies are 97.17% for the training set and 100%
for the validation and test sets. Upon completion of training,
the reduced density matrix of each qubit in its final state
is displayed on the Bloch sphere in Fig. 3(c). Red, green,
and blue represent the three classes of input data. In this
experiment, the role of Utrain can be considered a “global
rotation” operation that preserves the inner product between
any two encoded quantum states invariant. This implies that
the distance between final states and Utrain is unrelated. Consequently, the distances between final states are determined by
the encoding scheme used to map classical data into quantum
states. To achieve classification tasks, it is essential to distinguish different classes of classical input data as effectively
as possible through their corresponding quantum states. If
the encoded quantum states are particularly close together, it
becomes challenging to find observables suitable for distinguishing them. This means that the encoding schemes directly
influence the upper bound on classification accuracy. From
Fig. 3(c), it can be observed that our ENPQC scheme effectively maps different categories of data to distinct regions in
the state space.
IV. CONCLUSION AND DISCUSSION

In conclusion, we demonstrated in both theory and experiment an efficient classical-quantum interface by establishing
a PQC-based encoding framework termed enhanced natural
PQC. This encoding scheme maximizes the circuit’s parameter capacity to the degree of freedom of the pure state
and preserves the local structure of the original dataset.
Our work makes significant progress in addressing the crucial challenge of efficient classical-quantum data transfer
during the NISQ era and opens up new possibilities for efficient quantum information processing and quantum machine
learning.
To validate the effectiveness of our encoding method, we
compared ENPQC with other encoding schemes for quantum classification tasks. As shown by the numerical results
in Table I, the ENPQC scheme has significant advantages
over the previous amplitude encoding [16,50–52] and angle
encoding [18,53,54] methods in terms of qubit number or
encoding complexity. Furthermore, in pattern recognition
tasks such as the iris [55], wine [43], and breast cancer [56]
datasets, the quantum classification using the ENPQC encoding scheme achieves obviously better accuracy. However, for
image recognition tasks like handwritten digits [57] and the
Fashion-MNIST [58] dataset, the ENPQC scheme performs
on par with amplitude encoding and significantly outperforms
angle encoding [41]. Overall, the ENPQC encoding scheme
demonstrates clear superiority in terms of classification accuracy and resource consumption across various tasks [41].
Our scheme requires the use of permutation operations
Uπ as the entangling gates. Currently, how to efficiently

TABLE I. Comparison of quantum resource consumption and
classification accuracy (in percentage) of multiclass classification
tasks when using ENPQC with the full DOF, amplitude encoding,
and angle encoding. Here, M is the dimension of the classical data.
The simulation results for quantum classification tasks for various
datasets, including iris, wine, breast cancer, handwritten digits, and
Fashion-MNIST, are presented. The training and test sets are split
in an 8:2 ratio. The classical data are encoded into quantum states
using different methods and then classified using the support vector
machine (SVM).

Number of qubits
Iris (%)
Wine (%)
Breast cancer (%)
Handwritten digits (%)
Fashion-MNIST (%)

ENPQC

Amplitude

Angle

O(log M )
97.33
94.41
94.73
93.93
84.50

O(log M )
68.00
88.21
80.67
94.27
84.92

O(M )
96.67
92.71
92.61
48.69
11.39

implement specified permutation operations in a quantum system remains an open question. In Soeken et al.’s work [59],
a compilation algorithm for quantum state permutations into
elementary quantum gates was introduced. Compiling a specific permutation may result in an exponential gate complexity
[40]. It is worth noting that the ENPQC ansatz design is
related to only {lk }N−1
k=0 , which depend on the relative positions
of powers of 2 within the permutation cycles, regardless of
other elements. Therefore, we can regard {lk } as the structural
feature of the permutation π . This implies that different permutations with the same {lk } have equal impact in terms of
the design of encoding the circuit. Therefore, when designing
the ENPQC with maximum parameter capacity, we can first
construct {lk } such that all i terms within Eq. (5) are empty,
then obtain different permutations π corresponding to this
{lk }. The specific choice of which π to use will depend on
the physical platform employed. This flexibility facilitates the
implementation of ENPQC in various quantum systems.
ACKNOWLEDGMENTS

This work is supported by the Innovation Program
for Quantum Science and Technology (Grant No.
2021ZD0303205), the National Natural Science Foundation
of China (Grants No. 12261160569, No. 92165108, No.
12150014, and No. 11927811), the Anhui Initiative in
Quantum Information Technologies (Grant No. AHY050000),
the Anhui Provincial Natural Science Foundation (Grant No.
2108085J04), and the XPLORER Prize. We are grateful for
the meaningful discussions and valuable insights provided by
Professor H. Zhai and Dr. T. Haug.
DATA AVAILABILITY

Data generated and analyzed during the current study
are available from the corresponding author upon reasonable
request. All code used in this study is available from the
corresponding author upon request.

013221-6

ENHANCED NATURAL PARAMETERIZED QUANTUM …

PHYSICAL REVIEW RESEARCH 7, 013221 (2025)

[1] P. Rebentrost, M. Mohseni, and S. Lloyd, Quantum support
vector machine for big data classification, Phys. Rev. Lett. 113,
130503 (2014).
[2] S. S. Gill, A. Kumar, H. Singh, M. Singh, K. Kaur, M. Usman,
and R. Buyya, Quantum computing: A taxonomy, systematic
review and future directions, Software: Pract. Exper. 52, 66
(2022).
[3] T. Monz, D. Nigg, E. A. Martinez, M. F. Brandl, P. Schindler,
R. Rines, S. X. Wang, I. L. Chuang, and R. Blatt, Realization of
a scalable Shor algorithm, Science 351, 1068 (2016).
[4] J. A. Jones, M. Mosca, and R. H. Hansen, Implementation of
a quantum search algorithm on a quantum computer, Nature
(London) 393, 344 (1998).
[5] J. A. Cortese and T. M. Braje, Loading classical data into a
quantum computer, arXiv:1803.01958.
[6] F. Valdez and P. Melin, A review on quantum computing and
deep learning algorithms and their applications, Soft Comput.
27, 13217 (2023).
[7] M. Rath and H. Date, Quantum data encoding: A comparative
analysis of classical-to-quantum mapping techniques and their
impact on machine learning accuracy, EPJ Quantum Technol.
11, 72 (2024).
[8] J. C. Aulicino, T. Keen, and B. Peng, State preparation
and evolution in quantum computing: A perspective from
Hamiltonian moments, Int. J. Quantum Chem. 122, e26853
(2022).
[9] X.-M. Zhang, M.-H. Yung, and X. Yuan, Low-depth quantum
state preparation, Phys. Rev. Res. 3, 043200 (2021).
[10] V. Sood and R. P. Chauhan, Towards quantum state preparation
with materials science: An analytical review, Int. J. Quantum
Chem. 123, e27148 (2023).
[11] A. B. Magann, S. E. Economou, and C. Arenz, Randomized
adaptive quantum state preparation, Phys. Rev. Res. 5, 033227
(2023).
[12] I. F. Araujo, C. Blank, I. C. S. Araújo, and A. J. da Silva, Lowrank quantum state preparation, IEEE Trans. Comput.-Aided
Design Integr. Circuits Syst. 43, 161 (2024).
[13] X.-M. Zhang, T. Li, and X. Yuan, Quantum state preparation
with optimal circuit depth: Implementations and applications,
Phys. Rev. Lett. 129, 230504 (2022).
[14] I. F. Araujo, D. K. Park, T. B. Ludermir, W. R. Oliveira, F.
Petruccione, and A. J. da Silva, Configurable sublinear circuits
for quantum state preparation, Quantum Inf. Process. 22, 123
(2023).
[15] K. Nakaji, S. Uno, Y. Suzuki, R. Raymond, T. Onodera, T.
Tanaka, H. Tezuka, N. Mitsuda, and N. Yamamoto, Approximate amplitude encoding in shallow parameterized quantum
circuits and its application to financial market indicators, Phys.
Rev. Res. 4, 023136 (2022).
[16] M. Plesch and Č. Brukner, Quantum-state preparation with
universal gate decompositions, Phys. Rev. A 83, 032302 (2011).
[17] M. Schuld and F. Petruccione, Supervised Learning with Quantum Computers, Quantum Science and Technology, Vol. 17
(Springer, Cham, 2018).
[18] R. LaRose and B. Coyle, Robust data encodings for quantum
classifiers, Phys. Rev. A 102, 032420 (2020).
[19] V. Giovannetti, S. Lloyd, and L. Maccone, Quantum random
access memory, Phys. Rev. Lett. 100, 160501 (2008).

[20] S. Stenholm, Polarization coding of quantum information,
Opt. Commun. 123, 287 (1996).
[21] H. Mohammadbagherpoor, Y.-H. Oh, A. Singh, X. Yu,
and A. J. Rindos, Experimental challenges of implementing
quantum phase estimation algorithms on IBM quantum computer, arXiv:1903.07605.
[22] A. Saharia, R. K. Maddila, J. Ali, P. Yupapin, and G. Singh,
An elementary optical logic circuit for quantum computing: A
review, Opt. Quantum Electron. 51, 224 (2019).
[23] K. Bharti et al., Noisy intermediate-scale quantum algorithms,
Rev. Mod. Phys. 94, 015004 (2022).
[24] J. Preskill, Quantum computing in the NISQ era and beyond,
Quantum 2, 79 (2018).
[25] T. Haug, C. N. Self, and M. Kim, Quantum machine learning of
large datasets using randomized measurements, Mach. Learn.:
Sci. Technol. 4, 015005 (2023).
[26] D. Peral-García, J. Cruz-Benito, and F. J. García-Peñalvo, Systematic literature review: Quantum machine learning and its
applications, Comput. Sci. Rev. 51, 100619 (2024).
[27] G. Li, R. Ye, X. Zhao, and X. Wang, Concentration of data
encoding in parameterized quantum circuits, Advances in Neural Information Processing Systems, edited by S. Koyejo,
S. Mohamed, A. Agarwal, D. Belgrave, K. Cho, and A.
Oh (Curran Associates, Inc., Red Hook, 2022), Vol. 35,
pp. 19456–19469.
[28] M. C. Caro, E. Gil-Fuster, J. J. Meyer, J. Eisert, and R. Sweke,
Encoding-dependent generalization bounds for parametrized
quantum circuits, Quantum 5, 582 (2021).
[29] P. Nimbe, B. A. Weyori, and A. F. Adekoya, Models in quantum
computing: A systematic review, Quantum Inf. Process. 20, 80
(2021).
[30] D. Volya and P. Mishra, State preparation on quantum computers via quantum steering, IEEE Trans. Quantum Eng. 5,
3100714 (2024).
[31] T. Haug and M. S. Kim, Natural parametrized quantum circuit,
Phys. Rev. A 106, 052611 (2022).
[32] T. Haug, K. Bharti, and M. S. Kim, Capacity and quantum
geometry of parametrized quantum circuits, PRX Quantum 2,
040309 (2021).
[33] K. M. Barnes et al., Optimising the quantum/classical interface
for efficiency and portability with a multi-level hardware abstraction layer for quantum computers, EPJ Quantum Technol.
10, 36 (2023).
[34] S. Sim, P. D. Johnson, and A. Aspuru-Guzik, Expressibility
and entangling capability of parameterized quantum circuits for
hybrid quantum-classical algorithms, Adv. Quantum Technol.
2, 1900070 (2019).
[35] K. Nakaji and N. Yamamoto, Expressibility of the alternating layered ansatz for quantum computation, Quantum 5, 434
(2021).
[36] L. Funcke, T. Hartung, K. Jansen, S. Kühn, and P. Stornati, Dimensional expressivity analysis of parametric quantum circuits,
Quantum 5, 422 (2021).
[37] T. Haug and M. Kim, Optimal training of variational quantum
algorithms without barren plateaus, arXiv:2104.14543.
[38] J. Liu, H. Yuan, X.-M. Lu, and X. Wang, Quantum Fisher
information matrix and multiparameter estimation, J. Phys. A
53, 023001 (2020).

013221-7

YUQUAN CHEN et al.

PHYSICAL REVIEW RESEARCH 7, 013221 (2025)

[39] J. J. Meyer, Fisher information in noisy intermediate-scale
quantum applications, Quantum 5, 539 (2021).
[40] N. Schuch and J. Siewert, Programmable networks for quantum
algorithms, Phys. Rev. Lett. 91, 027902 (2003).
[41] See Supplemental Material at http://link.aps.org/supplemental/
10.1103/PhysRevResearch.7.013221 for theoretical derivation,
experimental details, and further discussion, which includes
Refs. [60,61].
[42] S. Aeberhard, D. Coomans, and O. Y. de Vel, Comparative
analysis of statistical pattern recognition methods in high dimensional settings, Pattern Recognit. 27, 1065 (1994).
[43] S. Aeberhard and M. Forina, Wine, UCI Machine Learning
Repository, 1991, https://doi.org/10.24432/C5PC7J.
[44] J. Li, R. Fan, H. Wang, B. Ye, B. Zeng, H. Zhai, X. Peng,
and J. Du, Measuring out-of-time-order correlators on a nuclear
magnetic resonance quantum simulator, Phys. Rev. X 7, 031011
(2017).
[45] X. Chen, Z. Wu, M. Jiang, X.-Y. Lü, X. Peng, and J. Du, Experimental quantum simulation of superradiant phase transition
beyond no-go theorem via antisqueezing, Nat. Commun. 12,
6281 (2021).
[46] X. Peng, X. Zhu, X. Fang, M. Feng, K. Gao, X. Yang, and M.
Liu, Preparation of pseudo-pure states by line-selective pulses
in nuclear magnetic resonance, Chem. Phys. Lett. 340, 509
(2001).
[47] J. C. Spall, An overview of the simultaneous perturbation
method for efficient optimization, Johns Hopkins APL Tech.
Dig. 19, 482 (1998).
[48] J. C. Spall, Implementation of the simultaneous perturbation
algorithm for stochastic optimization, IEEE Trans. Aerosp.
Electron. Syst. 34, 817 (1998).
[49] I. Goodfellow, Y. Bengio, and A. Courville, Deep Learning
(MIT Press, Cambridge, MA, 2016).
[50] V. V. Shende, S. S. Bullock, and I. L. Markov, Synthesis of
quantum logic circuits, in Proceedings of the 2005 Asia and
South Pacific Design Automation Conference, Shanghai, China
(Association for Computing Machinery, New York, NY, 2005),
pp. 272–275.

[51] M. Mottonen, J. J. Vartiainen, V. Bergholm, and M. M.
Salomaa, Transformation of quantum states using uniformly
controlled rotations, arXiv:quant-ph/0407010.
[52] X. Sun, G. Tian, S. Yang, P. Yuan, and S. Zhang, Asymptotically optimal circuit depth for quantum state preparation and
general unitary synthesis, IEEE Trans. Comput.-Aided Des.
Integr. Circuits Syst. 42, 3301 (2023).
[53] M. Weigold, J. Barzen, F. Leymann, and M. Salm, Data encoding patterns for quantum computing, in Proceedings of the 27th
Conference on Pattern Languages of Programs, PLoP ’20 (The
Hillside Group, 2022), pp. 1–11.
[54] F. Yan, A. M. Iliyasu, and S. E. Venegas-Andraca, A survey
of quantum image representations, Quantum Inf. Process. 15, 1
(2016).
[55] R. A. Fisher, Iris, UCI Machine Learning Repository, 1988,
https://doi.org/10.24432/C56C76.
[56] W. Wolberg, O. Mangasarian, N. Street, and W. Street, Breast
cancer Wisconsin (diagnostic), UCI Machine Learning Repository, 1995, https://doi.org/10.24432/C5DW2B.
[57] Y. Lecun, L. Bottou, Y. Bengio, and P. Haffner, Gradient-based
learning applied to document recognition, Proc. IEEE 86, 2278
(1998).
[58] H. Xiao, K. Rasul, and R. Vollgraf, Fashion-MNIST: A novel
image dataset for benchmarking machine learning algorithms,
arXiv:1708.07747.
[59] M. Soeken, F. Mozafari, B. Schmitt, and G. De Micheli, Compiling permutations for superconducting QPUs, in 2019 Design,
Automation & Test in Europe Conference & Exhibition (DATE)
(IEEE, Piscataway, NJ, 2019), pp. 1349–1354.
[60] F. Pedregosa, G. Varoquaux, A. Gramfort, V. Michel, B.
Thirion, O. Grisel, M. Blondel, P. Prettenhofer, R. Weiss, V.
Dubourg, J. Vanderplas, A. Passos, D. Cournapeau, M. Brucher,
M. Perrot, and E. Duchesnay, Scikit-learn: Machine learning in
Python, J. Mach. Learn. Res. 12, 2825 (2011).
[61] V. Havlíček, A. D. Córcoles, K. Temme, A. W. Harrow, A.
Kandala, J. M. Chow, and J. M. Gambetta, Supervised learning
with quantum-enhanced feature spaces, Nature (London) 567,
209 (2019).

013221-8

