SCIENCE CHINA
Information Sciences

. RESEARCH PAPER .

August 2025, Vol. 68, Iss. 8, 180504:1–180504:11
https://doi.org/10.1007/s11432-024-4185-1

Special Topic: Quantum Information

Variational quantum eigensolver with linear depth
problem-inspired ansatz for solving portfolio
optimization in finance
Shengbin WANG1,2 , Peng WANG2 , Guihui LI3 , Shubin ZHAO1 , Dongyi ZHAO1 ,
Jing WANG1 , Yuan FANG1 , Menghan DOU1 , Yongjian GU4 ,
Yu-Chun WU2,5,6* & Guo-Ping GUO1,2,5,6*
1
Origin Quantum Computing Company Limited, Hefei 230026, China
Laboratory of Quantum Information, University of Science and Technology of China, Hefei 230026, China
3
Intelligent Information Sensing and Processing Lab, College of Electronic Engineering, Ocean University of China,
Qingdao 266000, China
4
College of Physics and Optoelectronic Engineering, Ocean University of China, Qingdao 266100, China
5
Institute of Artificial Intelligence, Hefei Comprehensive National Science Center, Hefei 230088, China
6
Anhui Province Key Laboratory of Quantum Network, University of Science and Technology of China,
Hefei 230026, China
2

Received 18 March 2024/Revised 30 May 2024/Accepted 10 September 2024/Published online 3 July 2025
Abstract Great efforts have been dedicated in recent years to exploring practical applications for noisy intermediate-scale
quantum (NISQ) computers, which is a fundamental and challenging problem in quantum computing. As one of the most
promising methods, the variational quantum eigensolver (VQE) has been extensively studied. In this paper, VQE is applied
to solve portfolio optimization problems in finance by designing two hardware-efficient Dicke state ansatzes that reach a
2
maximum of 2n two-qubit gate depth and n4 parameters, with n being the number of qubits used. Both ansatzes are
partitioning-friendly, allowing for the proposal of a highly scalable quantum/classical hybrid distributed computing (HDC)
scheme. Combining simultaneous sampling, problem-specific measurement error mitigation, and fragment reuse techniques,
we successfully implement the HDC experiments with up to 55 qubits on our superconducting quantum computer “Wu
Kong”. The simulation and experimental results illustrate that the restricted expressibility of the ansatzes, induced by the
small number of parameters and limited entanglement, is advantageous for solving classical optimization problems with the
cost function of the conditional value-at-risk (CVaR) for the NISQ era and beyond. Furthermore, the HDC scheme shows
great potential for achieving quantum advantage in the NISQ era. We hope that the heuristic idea presented in this paper
can motivate fruitful investigations in current and future quantum computing paradigms.
Keywords variational quantum eigensolver, hardware-efficient Dicke state ansatz, quantum/classical hybrid distributed
computing, fragment reuse technique, portfolio optimization
Citation Wang S B, Wang P, Li G H, et al. Variational quantum eigensolver with linear depth problem-inspired ansatz for
solving portfolio optimization in finance. Sci China Inf Sci, 2025, 68(8): 180504, https://doi.org/10.1007/s11432-024-4185-1

1

Introduction

Quantum computing can provide astonishing speedups in certain applications, such as simulating quantum systems [1], factoring numbers [2], searching unstructured databases [3], and solving linear systems
of equations [4], compared to its classical counterpart. These advantages arise from the peculiar properties of quantum entanglement, superposition, and interference. Mixed blessings, these properties also
seriously impede the design and manufacture of large-scale fault-tolerant quantum computers that can
fully realize the speedup potential of quantum computing [5]. Whereupon, the currently available noisy
intermediate-scale quantum (NISQ) computer, with no more than hundreds of noisy qubits, short coherence time, and limited connectivity, is the only quantum platform available to us in the coming few years,
and possibly even longer [6,7]. The widely held focus is on finding the “killer apps” for NISQ computers,
which is a notoriously difficult problem [8, 9].
* Corresponding author (email: wuyuchun@ustc.edu.cn, gpguo@ustc.edu.cn)
© Science China Press 2025

info.scichina.com

link.springer.com

Wang S B, et al.

Sci China Inf Sci

August 2025, Vol. 68, Iss. 8, 180504:2

Variational quantum algorithms (VQAs) [10], developed for efficient implementation on both quantum
and classical computers in a hybrid manner, significantly enhance the prospect of practical applications
that may offer quantum advantages in the NISQ era. The prominent algorithms are the variational
quantum eigensolver (VQE) [11] and the quantum approximate optimization algorithm (QAOA) [12]. In
recent years, significant efforts, particularly in the fields of quantum chemistry, quantum machine learning,
and combinatorial optimization [10, 13–25], have been made with VQAs to advance the practicality of
NISQ computers. For combinatorial optimization, which has already been extensively applied in many
areas of business and science, the studies in the quantum computing field mainly focus on maximum
cut, number partitioning, and portfolio optimization, etc. [23, 24, 26–31]. Compared to QAOA, which
encodes the total energy of the problem through the cost Hamiltonian that requires to be translated into
a unitary operator, resulting in a much deeper quantum circuit, VQE with the unique quantum part,
i.e., the ansatz, and classically optimized expectation of the total energy is more appealing. This comes
from the consensus that NISQ computers are limited to executing lower-depth circuits and hence should
focus on handling the classically intractable parts of the computation process as efficiently as possible.
The ansatz, a structurally parameterized quantum circuit (PQC) U (θ) with parameters θ, is the key
ingredient of the VQE algorithms. The trial quantum states |ψ(θ)i prepared by the ansatz are subsequently iteratively sampled and optimized to classically evaluate the minimum energy of the Hamiltonian
H of the problem, i.e., minθ hψ(θ)|H|ψ(θ)i, along with the corresponding eigenstate, upon the corresponding parameters θ [32, 33]. In other words, as the unique quantum part, ansatz determines the
output fidelity of NISQ computers and the potential advantage that the VQE algorithms can achieve.
Unsuitable ansatz deployed for specific problems trivially leads to bad performance. There are two main
categories of ansatzes in the context of this paper: hardware-efficient (HE) ansatz and problem-inspired
ansatz [10, 18]. The versatility of HE ansatz which is designed based on considering the restrictive conditions of NISQ computers can mitigate the effect of hardware noise to some extent. That is, HE ansatz is
problem-agnostic and can be a circuit with very low depth, even a product state composed of one layer
of single-qubit gates. These advantages have garnered much attention, resulting in a flurry of promising
results on solving small-scale problems of interest [11, 13, 27], and the current combinatorial optimization
investments are mainly focusing on this type of ansatz. However, for most of the underlying problems,
the problem-agnostic nature of this type of ansatz may lead to undesired issues such as barren plateau
(BP), local minima, and poor expressibility [34–37], particularly when the number of required qubits to
span the search space becomes slightly larger. In contrast, a problem-inspired ansatz has access to some
prior knowledge of the problem, which can span a more accurate search space. Hence the issues of BP
and local minima can be largely alleviated [38]. Unfortunately, this type of ansatz, e.g., the extensively
researched unitary coupled cluster (UCC) ansatz and heuristic ansatz in quantum chemistry [10,39], typically results in dense entanglement among qubits and leads to much deeper circuits, which is prohibitive
for the current NISQ computers to execute efficiently even on solving small-scale problems.
Clearly, viable ansatzes for efficiently solving problems of interest on NISQ computers should possess
both hardware-efficient and problem-inspired properties simultaneously. That is, this type of ansatzes
must be a shallow circuit with nearest-neighbor coupling which unfolds a feasible search subspace that
encompasses the optimal solution (or the near-optimal solutions) while avoiding, if possible, the generation
of irrelevant, even distant, states. In consequence, the key question at present turns to whether such a
viable ansatz can be devised, at least for solving specific problems. Besides, another issue that arises is
how to mitigate the errors induced by the width (number of qubits) of the ansatz when solving larger-scale
problems.
In this paper, we address these questions by introducing two ansatzes that can efficiently prepare
arbitrary Dicke states [40], which are well-suited for NISQ computers. Both ansatzes are not only useful
for solving portfolio optimization problems in finance [41,42] but also for other combinatorial optimization
problems [23]. Our ansatzes are unified frameworks that span the feasible subspace and have a linear
circuit depth with a constant factor of at most 2 on CNOT gates, which are applied only between adjacent
qubits. The worst-case asymptotic complexity on parameters θ is squared with a factor not exceeding 41 .
The above achievements make our ansatzes the most advanced methods for preparing Dicke states that
can be executed on NISQ computers with linear-nearest-neighbor coupling currently and answer the first
question in the affirmative. Nevertheless, to guarantee that NISQ computers can be deployed to efficiently
solve some larger-scale problems, addressing the second issue is an equally crucial task. Fortunately, the
building blocks of our ansatzes construct quantum circuits using a staircase structure, similar to the
structure of the Matrix product state, that is more convenient for us to embed circuit cutting [43, 44] or

Wang S B, et al.

Sci China Inf Sci

August 2025, Vol. 68, Iss. 8, 180504:3

qubit reuse [45] techniques, or their combination, to improve the performance of NISQ computers in terms
of circuit width dimension. Further progress has been achieved by proposing a quantum/classical hybrid
distributed computing (HDC) scheme. This scheme splits classically the ansatz into several subcircuits
with a staircase structure first, and then partitions (cuts) each subcircuit into applicable fragments using
the circuit cutting technique or executes each subcircuit directly using the qubit reuse technique. In the
circuit cutting case, the total number of qubits required to be cut in each circuit is greatly reduced. The
X, Y , and Z “measure-and-prepare” channels are eliminated based on the symmetry of Dicke states.
Compared to the common circuit cutting technique, our scheme exponentially reduces the sampling
complexity. We also significantly reduce the number of submissions of the circuits to the hardware. This
preserves completely the advantage of NISQ computers in solving portfolio optimization, not only in the
scenarios of selecting a small number of assets. In the qubit reuse case, the number of qubits used to
execute each circuit can be reduced to merely 2. We provide detailed comparisons of our scheme to the
commonly used ansatzes through complexity analysis, numerical simulations, and hardware experiments,
verifying the superiority of our methods over the state-of-the-art ones.
The paper is organized as follows. In Section 2, an overview of the binary integer portfolio optimization
problem is provided. The design inspiration, theoretical insights, single-layer structure rationality, detailed optimal circuit, and complexity comparisons of the proposed ansatzes are introduced in Section 3.
In Section 4, we provide the numerical simulations and hardware experiments of the proposed algorithms,
as well as the quantum/classical hybrid distributed computing scheme, simultaneous sampling method,
problem-specific measurement error mitigation, and fragment reuse technique. Finally, we conclude our
work and discuss some interesting problems in Section 5.

2

Portfolio optimization

As one of the most common optimization problems in finance, portfolio optimization involves selecting
from an asset pool a set of optimally allocated assets that achieve the expected return with minimum
financial risk, or maximize the expected return for a given level of risk [41,42]. In this paper, we focus on
binary integer portfolio optimization based on mean-variance analysis (modern portfolio theory) because
its binary variable representation aligns with the prevalent two-level quantum computers. The risk-return
optimization can be modeled as
minx qxT Ax − µT x,

(1)

s.t. ξ = ΠT x,

where x = (x1 , x2 , . . . , xn )T with xi ∈ {0, 1} represents the asset selection vector, i.e., the ith asset is
selected when boolean variable xi = 1 or not when xi = 0. A is the n × n real covariance matrix between
assets. The risk level q > 0 represents the investor’s risk tolerance, and the vector µ contains the expected
returns of the assets. The constraint is given by ξ = ΠT x, where ξ is the budget and Π is the asset price
vector, which can be simplified to the all-ones vector, 1, in the present scenario.
There are two ways to map the problem to a quadratic unconstrained binary optimization (QUBO) form
suitable for quantum computing [46]. The general way is known as the soft constraint form, which encodes
the constraint to a penalty, (ξ − 1T x)2 , absorbed into the cost function with a penalty scaling coefficient.
That is, by transforming variable xi ∈ {0, 1} to zi ∈ {−1, +1} based on the relation zi = 1 − 2xi , the
binary model is converted to a spin model:
( 
2 )
1 T
′ T
′T
′
minz q z Az − µ z + β ξ + 1 z
,
(2)
2
soft

where β is the penalty scaling coefficient. The problem described by (2) can be easily translated into
a diagonal Hamiltonian, whose ground state encodes the optimal solution of the optimization problem
i
(1) by replacing zi with σZ
. Finally, the HE ansatz-based VQE algorithm can be applied to estimate
the ground state. However, the landscape spanned by (2) with the HE ansatz is too large and flat
and contains too many local minima, which impact severely the optimization of the parameters and,
consequently, hinder the convergence of the solution for solving larger-scale problems.
Contrastingly, the hard constraint form encodes the constraint directly into the structure of the
problem-inspired ansatz. That is, any vector x that does not conform to the constraint ξ = 1T x is

Wang S B, et al.

Figure 1

Sci China Inf Sci

August 2025, Vol. 68, Iss. 8, 180504:4

Illustrative staircase-structure circuit for preparing state |W5 i.

excluded from the space spanned by the ansatz. Eq. (2) is reduced to
minz q ′ z T Az − µ′T z.

(3)

The elimination of the penalty term simplifies the evaluation of minθ hψ(θ)|H|ψ(θ)i on a much smaller
landscape.

3

Variational Dicke state ansatz

An ansatz is a dynamic quantum state preparation circuit that depends on some parameters optimized
through the minimization or maximization of a problem’s cost function. The form of the ansatz determines
the form of the cost Hamiltonian and the training behavior of the parameters. In this section, two
universal ansatzes for preparing arbitrary Dicke states |Dkn i with variable amplitudes as a function of the
parameters θ are presented. In the present scenario, a Dicke state |Dkn i is a superposition state composed
of all n-qubit basis states |ii with Hamming weight HW (i) = k [47, 48],
X
|Dkn i =
ai |ii,
(4)
i∈{0,1}n ,HW (i)=k

where ai is the amplitude of basis state |ii. For instance, |D23 i with equal amplitude is |D23 i = √13 (|011i +
|101i + |110i). In portfolio optimization, n denotes the number of assets that the asset pool can provide
and k ∈ [1, n − 1] is the number of assets selected from the asset pool which is equivalent to the budget
ξ [42]. A Dicke state encodes the constraint in (1), thus the QUBO takes the form expressed in (3).
This leads to a precise search space and a more regular cost function landscape, which is beneficial for
alleviating the issues of BP and local minima [38]. The applications of Dicke states also involve quantum
game [49], quantum metrology [50], and quantum networks [51].
Both ansatzes are inspired by the fundamental observation that all the useful information is implicitly
stored in the unitary Un , composed of the building blocks “Controlled-Ry and CNOT” shown in the
dashed box of Figure 1 for preparing W state [52]. Hence, we can easily extract the target states by
preparing a linear combination of the appropriate columns of Un , somewhat similar to the idea of the
linear combination of unitaries (LCU)-based quantum state preparation algorithms [53,54]. In this paper,
we refer to the circuit structure similar to the one in the dashed box as the ‘staircase structure’, denoted
as Un , which is the critical circuit structure of our ansatzes. We analyze the theoretical support for both
ansatzes based on this observation, see Appendix A for details. For an arbitrary basis state of |Dkn i,
there always exists a basis state with reverse symmetry to it, e.g., 11000 with 00011, 01010 with itself.
Therefore, the qubit at the top can be regarded as either the lowest qubit or the highest qubit. In the
following context, we fix the top qubit to be the highest qubit.
For combinatorial optimization problems, the solution is a single vector (binary string) that is fundamentally different from the ground state composed of multiple vectors for chemical systems. Therefore,
the extra degrees of freedom, which should be preserved in solving certain chemistry problems, can be
removed in combinatorial optimization scenarios. Then based on the observation of W state, we construct the staircase unitary Un using the simplified “A” gates [39] which is composed of multiple “CNOT,

Wang S B, et al.

Sci China Inf Sci

August 2025, Vol. 68, Iss. 8, 180504:5

Figure 2 Illustrations of (a) CCC ansatz and (b) CC ansatz for preparing |D25 i. For CCC ansatz, a 3C block is indicated in the
dashed box. For CC ansatz, the inoperative controlled-Ry in the dashed box is shown for structure completeness. The variational
parameters of Ry gates are omitted for brevity.

Controlled-Ry , CNOT” (3C) blocks, see Figure 2(a) for an example. Unexpectedly, the unitary contains all the information about Dicke states |Dkn i, which are distributed across different columns, see
Appendix A for detailed analysis. Motivated by this observation, the first ansatz is constructed with k
layers of staircases. Each layer is composed of (n − k − ⌊i/2⌋) 3C blocks, hence is called CCC ansatz,
starting with an NOT(X) gate deployed at the ith qubit where i equals 2k − 1,
 2k −n3,. . . , 1, when
k ⩽ ⌊n/2⌋, see Figure 2(a). For the cases of k > ⌊n/2⌋, we use the equivalence nk = n−k
to simplify
n
the circuit design, i.e., using the circuit for preparing |Dn−k
i followed by the unitary ⊗nj=1 Xj to prepare
|Dkn i. At last, we optimize each 3C block to its optimal circuit that contains only 2 CNOT gates to
reduce the circuit depth further, see Appendix B for detailed analysis.
The second ansatz proposed here is inspired directly by the circuit for preparing W state [52], the
n-qubit case of which is defined as
1
|Wn i = √ (|100 · · · 0i + |010 · · · 0i + · · · + |000 · · · 1i).
(5)
n

This is actually the most trivial case of selecting 1 asset out of n, n1 . The preparation procedure of W
state can be represented as |Wn i = Un (NOT1 ⊗ In−1 )|0n i, where NOT1 ⊗ In−1 represents the NOT gate
operating on the highest qubit in the first time step, see Figure 1, and Un is the n-qubit unitary operator
composed by the following “Controlled-Ry , CNOT” (2C) blocks, hence is called CC ansatz, shown in the
dashed box. The fact we found is that W state can be regarded as being extracted from the column 2n−1
of the unitary Un as |10n−1 i = NOT1 ⊗ In−1 |0n i.
Based on generalization and summarization, CC ansatz can be alternatively constructed in three steps
when k ⩽ n/2. The first step is to deploy unitary X{k mod 2} ⊗ [(I ⊗ X)⊗⌊k/2⌋ ] ⊗ In−k from top to bottom
in the first time step, see Figure 2(b) for the example of preparing |D25 i. The subscript {k mod 2} means
the first X operates only when k is odd. Then append a staircase composed of multiple 2C blocks for
each X gate except the one operating on the highest qubit (if exists). Each staircase starts from the
corresponding X gate and stops at the lowest qubit. At last append Un to complete the ansatz. The
number of staircase layers is reduced to ⌊k/2⌋ + 1 for preparing |Dkn i, whereas the prepared state with
k ∈ [3, n − 3] contains non-target basis states. Same as the method used in extending to cases with larger
n
k in CCC ansatz, state |Dkn i with k > n/2 in CC ansatz is prepared by |Dn−k
i. Each 2C block is also
optimized to 2 CNOT gates, see Appendix B for the two compile methods provided.
Although the state prepared by CC ansatz is not a precise Dicke state |Dkn i and contains non-negligible
non-targets when k belongs to [3, n − 3], the number of layers of the staircase is reduced by almost half,
making it more preferable for executing on NISQ computers. We also propose a symmetric space partition
scheme that utilizes the reverse symmetry property of the basis states of the Dicke state to alleviate the
impact of the extra basis states and preserve the target basis states as much as possible. See Appendix G
for analysis and numerical illustrations.
The two ansatzes both reach a linear complexity of two-qubit gate depth with a staircase structure,
and nk − 3k 2 /2 and n(k + 1)/2 − k 2/4 parameters, respectively, see Appendix C for the evaluation of the
complexity. The comparison with the latest schemes for preparing Dicke states is presented in Table 1.
Concretely, to prepare the small scale Dicke state |D28 i, the number of CNOT gates required based on
the 5 methods are 44, 27, 31, 22, and 25, respectively. Our ansatzes achieve the minimum CNOT counts
with linear-nearest-neighbor coupling which is more friendly for the current NISQ computers. Compared
to the previous circuits, the present ansatzes are much more regular and simple. It is also worth noting

Wang S B, et al.
Table 1

Sci China Inf Sci

August 2025, Vol. 68, Iss. 8, 180504:6

Comparison of Dicke state preparation schemes.

Method

Depth of CNOTs

Number of CNOTs

Number of θs

Topology

Mukherjee et al. [47]

O(nk)

–

all-to-all

Bärtschi et al. [48]

O(klog n
k)
p
O(k n
k)

5nk − 5k2
O(nk)

–

all-to-all

O(nk)

–

CCC ansatz

2(n − k)a)

2nk − 3k2

nk − 3k2

CC ansatz
a) By default, k ⩽ n
2.

Grid
2

2
2
n(k+1)
nk − k2
− k4
2
n
n
The complexity of preparing |Dn−k i is equal to that of preparing |Dk i.

2n

LNNb)
LNN

b) Linear-nearest-neighbor connectivity.

that we can easily prepare a subspace of arbitrary |Dkn i by combining fewer columns. In this manner, a
much smaller and more accurate search space can be spanned when some prior knowledge of the solution
is presented. Otherwise, we can still split the Dicke state into multiple subspaces and search them one
by one to alleviate the issues of the BP and local minima [55, 56].
As can be seen, the ansatzes are designed by reducing the parameters and quantum gates to a minimum
for improving their ability of executing on NISQ computers, while the expressibility is restricted, but the
BP problem is also suppressed [37]. Intuitively for classical optimization problems in the NISQ era,
the BP problem appears to be more important than expressibility. In addition, a local cost function
can perform better than a global one [34, 37]. Here we use the conditional value-at-risk (CVaR) [27]
as the cost function. CVaR with a small confidence level α ∈ (0, 1] can be regarded as a local cost
function. Additionally, the space spanned by the proposed ansatzes always contains the ground states
for all cases. Therefore, the negative impacts of restricted expressibility of the proposed ansatzes can
be greatly mitigated. We found numerically that deploying multiple layers of the staircase unitary Un
composed of 3C blocks, which always prepares a precise Dicke state, really does not observably improve
the performance for small confidence levels, see Appendix H for the demonstrations. Therefore, in
combinatorial optimization problems, it is reasonable for us to focus on the single layered Un with CVaR,
which is more amenable to the current NISQ devices.

4

Numerical simulations and experiments

In this section, we perform the numerical simulations and hardware experiments to verify the effectiveness
of our proposals.
4.1

Numerical simulations

We performed extensive noise-free numerical simulations by pyQPanda [57]. Specifically, the COBYLA
optimization algorithm is utilized. Simulation results show that we cannot expect to get the optimal
solution in just one calculation when the problem has a little larger asset pool, especially for HE ansatz
that spans an exponentially large search space, in the present shallow ansatz scenario. Therefore, it is
more intuitive to statistically analyze and compare the overall performance of these ansatzes. However,
the variance is a little larger due to the lower expressibility. In the following, we analyze numerically the
time consumption and the probabilities of obtaining the optimal and feasible solutions for the linearly
entangled HE ansatz and our proposed CCC and CC ansatzes with respect to different numbers of assets
and budgets.
Figure 3 provides a sketch of the average time and probabilities of the three ansatzes with the number
of assets n ranging in [4, 20] and confidence level α ∈ {1, 0.5, 0.25, 0.1}. The asset data is produced
using qiskit finance.data providers [58]. The maximum number of iterations is set to 500. The number
of budgets k is fixed at 2, and the risk level q is set to 0.5. To illustrate the statistical behaviors of the
time consumption and the probabilities, we initialize the parameters θ with a random seed 1231 and
the asset pool 20 times with random seeds starting from 1000. To guarantee shallow property, viable
execution time, and essential expressibility of the HE ansatz, the number of layers is set to be logarithmic
in n. For consistency, the seeds used for the random initialization of the 20 asset portfolios are the
same for each ansatz. To obtain results with the same precision, the number of samples of different
confidence levels α should be 1/α times of that of the cases where α = 1. That is to say, the ability of
always obtaining the optimal solution in most small α instances is achieved by appropriately increasing
the sampling complexity. Due to the sampling taking much longer than classical post-processing, we

Wang S B, et al.

Sci China Inf Sci

August 2025, Vol. 68, Iss. 8, 180504:7

Figure 3 (Color online) Comparisons among the CCC, CC, and HE ansatzes, up to 20 assets. (a) The average time consumption;
(b) the average probability of obtaining the optimal solution; (c) the average probability of obtaining the feasible solutions. A
feasible solution is accepted when its expectation is not more than 0.75 times that of the optimal solution. The maximum and
minimum values at α = 0.1 are plotted as shadows. The others are not shown because they would override confusingly, disrupting
the display of average information.

Figure 4 (Color online) Comparisons of different number of budgets. (a) The average time consumption; (b) the average probability of obtaining the optimal solution; (c) the average probability of obtaining the feasible solutions.

roughly multiplied the numerical simulation time by 1/α to approximate the time consumption of each
instance. Even so, under the same experimental conditions, the number of iterations trends to reduce
with decreasing confidence level which results in only a slight difference in the consumed time for different
α.
As indicated in Figure 3(a), CCC and CC ansatzes always take time less than the logarithmic depth
HE ansatz. This benefits from the more targeted expressibility of our ansatzes. The Hamming weight of
the basis states prepared by our ansatzes is exactly the budget k (slightly more for CC ansatz), while the
HE ansatz outputs an exponential number of basis states that contain every possible budget belonging
to [0, n]. Then the search space spanned by our ansatze is much smaller, and the landscape is much more
regular, which promises the high efficiency of our ansatzes. In addition, to enhance the expressibility of
the HE ansatz by deploying poly(n) layers, the time consumption would increase rapidly.
Figure 3(b) demonstrates the probabilities of obtaining the optimal solutions of the three ansatzes. As
the number of assets n increases, the probabilities of obtaining the optimal solutions of CCC and CC
ansatzes are generally higher than that of the HE ansatz. Their performance improves as α decreases.
For example, for the HE ansatz, α = 0.5 consistantly outperforms α = 1, α = 0.25 becomes superior
to α = 0.5 when n = 8, and α = 0.1 surpasses α = 0.25 starting from n = 18. However, for the
proposed ansatzes, the upper bound is greatly improved. As shown in Figure 3(b), α = 0.5 does not
surpass α = 1 until n reaches approximately 10. Besides, the decreases in the cases corresponding to
α = 0.5, 0.25, 0.1 are relatively slower, suggesting that the proposed ansatzes exhibit high and stable
performance for larger-scale cases, even with large α. Conventionally, finding the optimal solution could
be an extremely hard task that implies finding a feasible solution by consuming affordable resources is
more realistic. As shown in Figure 3(c), compared to the probabilities of obtaining the optimal solution,
CCC and CC ansatzes can always find feasible solutions with much higher probabilities, especially for
larger n. We argue that it is more practical to find a feasible solution for optimization problems using
NISQ computers because the hardware noise and sampling error lead to the rapid convergence of the
algorithm to a local minimum that very likely corresponds to a feasible solution.
In the second simulation, we fix confidence level α at 0.5, the total number of assets at 12, and test the
performance of these ansatzes when the budgets range from 2 to 6. As shown in Figure 4, the performance
of the proposed ansatzes is always much better than the HE ansatz. In Figure 4(a), the time consumed

Wang S B, et al.

Sci China Inf Sci

August 2025, Vol. 68, Iss. 8, 180504:8

by the HE ansatz remains almost the same because the ansatz is the same one across different budgets,
while the time consumed by the proposed ansatzes gradually increases due to the expansion of the search
space. In Figure 4(b), the probability of obtaining the optimal solution of CC ansatz decreases much faster
than for CCC ansatz due to the introduction of extra non-target states. Compared to the probability
of obtaining the optimal solution, it is much easier for us to obtain a feasible solution, as depicted in
Figure 4(c).
4.2

Experiments on NISQ computer

The common fact is that, to achieve potential quantum advantages, the problem scale needs to be large
enough. That is to say, the hardware should be able to prepare a high precision superposition state
containing an exponential number of basis states with respect to a large number of qubits. However, the
current NISQ computers cannot easily process a large number of qubits, while retaining an exponential
number of basis states simultaneously. Inspired by the partitioning-friendly property of both ansatzes, the
highly scalable quantum/classical HDC scheme is proposed. Combining simultaneous sampling, problemspecific measurement error mitigation, and fragment reuse techniques, the HDC experiments of |D355 i and
|D612 i using 3 and 6 qubits, respectively, achieve success.
HDC scheme. The feasibility of the HDC scheme stems from the fact that we can find a combination
of a small number of columns of Un to construct a Dicke state ansatz, refer to Appendix A. Therefore, the
ansatz can be classically split into several subcircuits, each of which is synthesized using only one of these
columns, or a superposition of a few of these columns, if possible, followed by Un . Each subcircuit with
relatively sparse entanglement spans a smaller subspace that is more applicable for NISQ computers.
By careful design, the sparse staircase structure of the subcircuits offers us superior properties like a
minimal number of cut qubits and a correspondingly minimal number of observables of the “measureand-prepare” channels for utilizing the circuit cutting technique, refer to Appendix D for the detailed
analysis. Specifically, the total number of cut qubits for partitioning each subcircuit into p + 1 fragments
is just p and the “measure-and-prepare” channel only has the observables |0ih0| and |1ih1|, when a single
qubit is cut between the adjacent two fragments. Then the sampling complexity of each subcircuit for
evaluating the CVaR is O(1/(αǫ2 )) with the confidence level α ∈ (0, 1] and the accuracy ǫ. This is a
complexity that has no concern with the total number of cut qubits p. Hence, the subcircuits can be
cut into smaller fragments to more easily obtain the low-probability basis states. This is because the
basis states in a smaller fragment can be obtained with higher probabilities, leading to more accurate
results. Furthermore, the qubit reuse technique [45] can be applied to execute these subcircuits directly,
especially those with very few columns, refer to Figure E3 in Appendix E for an illustration. However,
the circuit cutting technique can mitigate the impact of errors more flexibly in the width dimension of
NISQ devices [43, 59].
Simultaneous sampling. The reduction of the “measure and prepare” channels eliminates the
redundant sampling complexity. The number of fragment submissions to the quantum computer is also
exponentially decreased to 2p+1 where p is the number of cut qubits. However, the observables |0ih0| and
|1ih1| can only be observed on matrix basis I, which results in the sequential sampling of the fragments,
refer to the end of Appendix D. Here we propose to simultaneously sample each fragment, which is
also advantageous for applying quantum error mitigation (QEM) [60–63]. In this case, all the 2p + 1
fragments are shot N times each. Then we perform sequential sampling of the measured results in a
classical manner.
Problem-specific measurement error mitigation. In general, the states prepared by probleminspired ansatzes are sparse ones, so the commonly laudable noise-resistance feature is no longer as
effective. Here, by combining the symmetry property of each fragment with measurement error mitigation
method [60, 62], we greatly improve the accuracy of the execution on NISQ hardwares. Specifically, we
found that each fragment can only output states with the same Hamming weight, which provides us
with a more accurate assignment matrix M by setting the columns with other Hamming weights to be
a standard basis with the element “1” on the main diagonal. Then after evaluating pmigit = M −1 pnoisy
where pnoisy is the vector of the measured probability and pmigit is the mitigated probability, we normalize
the probabilities of the states with the correct Hamming weight in pmigit to be the final output. Our
proposals mitigate the effects of noise perturbation and, as a result, improve the stability and convergence
speed of the optimization process.
Fragment reuse. In the optimization process, the change of each θ only influences the corresponding

Wang S B, et al.

Sci China Inf Sci

August 2025, Vol. 68, Iss. 8, 180504:9

Figure 5 (Color online) (a) Probability of obtaining the optimal solution in the first experiments, numerical versus hardware.
Appendix F shows the simulation and experiment setups, and qubit topology for both experiments. In this experiment, qubits 45,
46, 52 are used. It should be clarified that we did not perform experiments with qubits larger than 55. (b) The convergence curve
for case |D612 i. The blue dashed line shows the change of the CVaR expectation, and the green solid line represents the probability
of obtaining the optimal solution.

fragment, and the other fragments remain unchanged. Consequently, it is not necessary to repeatedly
execute all of the fragments. The previously measured results of the fragments can be reused later when
their θs have not changed. This fact is used to reduce the number of submissions to the quantum computer
and the introduced bias can improve the stability of the optimization process. Hence the trainability can
be improved as well.
Now, we present the experimental results. The first experiment executes the k = 3 case of CCC ansatz
with one column corresponding to one subcircuit on the NISQ computer to demonstrate the feasibility of
the proposed algorithms; CC ansatz has similar results. Each |D3n i ansatz is classically split into ⌊ n−1
2 ⌋
subcircuits. Each subcircuit is partitioned into ⌈ n−1
⌉
3-qubit
fragments.
For
the
specific
HDC
scheme
2
and complexity analysis, refer to Appendixes E and F. The asset pool is generated using random seed
1000. To improve the convergence speed, the confidence level α is initially set to a small value, as shown
in Table F1 of Appendix F, and is then increased to 1.0 gradually [64]. We also formalize the uniform
initialization of the states for all subcircuits.
In this scenario, SLSQP is employed, rather than COBYLA, because this experiment needs to handle
many small-size fragments, and SLSQP can take better advantage of the fragment reuse technique to
improve the stability of the optimization process (cost gradient). In addition, there are only 3 “1” elements
in each basis state, and their distribution is relatively dispersed. The gradient of the cost function is
easier to find. The experiments achieve the successful executions of the circuits with up to 55 qubits.
In fact we found that hardware experiments converge much faster than numerical simulations under the
same configuration in the early stage of the optimization process. This indicates that the perturbation
of the hardware noise is an inherent advantage for the CVaR cost function with a small α. However, the
discrepancy between the probabilities of obtaining the optimal solutions in both cases becomes larger with
respect to the number of assets, see Figure 5(a). This result stems from the fact that, as the value of α
increases in the optimization process, the number of basis states that could be sampled in the confidence
interval (0, α] becomes larger. The sampling accuracy is reduced due to the instability and noise of the
hardware. Hence the stability of the CVaR expectation gradually decreases in the subsequent stages of
the optimization process. The instability of the expectation disturbs the convergence process, leading
to fluctuations in the probability of obtaining the optimal solution. This instability also provides the
opportunity to surpass noiseless numerical simulations (as seen in the 55-asset experiment).
The second experiment searches for the optimal solution of case |D612 i. The ansatz is classically split
into 5 subcircuits. Each subcircuit is cut into two 6-qubit fragments and one 2-qubit 3C block. For the
specific HDC scheme and complexity analysis, refer to Appendixes E and F. At this time, the restricted
expressibility and complex structure of our ansatz severely impede its uniform initialization. To remedy
this issue, we coarsely fit the parameters
θ that can produce a relatively uniform output. The coarse
P
fitting is performed by minimizing i (p′i − p0 )2 where p′i corresponds to the probabilities of the sampled
states and p0 is the uniform probability. Additionally the parameters θ are also initialized randomly in
the interval [π/2, 3π/4].
Extensive numerical simulations showed that, in the most complicated scenario, COBYLA outperforms

Wang S B, et al.

Sci China Inf Sci

August 2025, Vol. 68, Iss. 8, 180504:10

SLSQP. As shown in Figure 4(b), when using COBYLA and setting α to 0.5, the average probability of
obtaining the optimal solution of |D612 i is about 45% (approaching the soft cap of 50% corresponding
to α = 0.5), while with the same configuration, SLSQP can only achieve 18%. This results from the
local minima problems caused by the considerable overlap of the basis states. Specifically, the asset pool
generated by the random seed 1000 also prevents SLSQP from converging to the optimal solution. The
present experimental scheme can only slightly improve the situation. In such a difficult instance, we
attempted to use COBYLA. In the primary stage of COBYLA, only one or two parameters are changed
in each iteration. So, we choose to repeatedly run the primary stage multiple times. The parameters
obtained from the previous run are used as the initial parameters of the next run. In consequence, the
fragment reuse technique can make the optimization process more stable. As shown in Figure 5(b), the
optimization process exhibits fluctuating convergence to the optimal solution. The COBYLA optimization algorithm and the learning rate adjustment made at the beginning of each run inherently lead to
fluctuations. Additionally, larger values of α exacerbate the impact of the instability and noise of the
hardware to the optimization process.

5

Conclusion and discussion

In this paper, we have achieved the common portfolio optimizations using our superconducting computer
n
“Wu Kong” for up to 55 qubits (assets) in the case of |D3n i and 12 qubits in the case of |Dn/2
i. This
comes from trading expressibility for trainability by proposing two compact Dicke state ansatzes and
utilizing the CVaR cost function. Additionally, the proposed HDC scheme with simultaneous sampling,
problem-specific measurement error mitigation, and fragment reuse technique, is utilized. The proposed
ansatzes achieve the current lowest complexity in terms of circuit depth, two-qubit gates, and parameters,
compared to previous methods. The unified framework for preparing arbitrary Dicke states with a
staircase structure is well-suited for distributed quantum computing. Our proposals greatly improve the
execution precision in NISQ devices with little overhead.
It should be noted that we just applied the simplest quantum error mitigation method, i.e., quantum
measurement error mitigation. Other superior methods, such as zero-noise extrapolation and probabilistic
error cancellation [60], should be able to achieve significantly better results. Hence, as the performance of
NISQ computers improves, the methods we proposed have the potential to significantly accelerate certain
practical applications of variational quantum algorithms [10], such as in the fields of chemistry, biology,
and machine learning, in the near future, not limited to classical optimization problems.
The experimental results show that partitioning the search space into multiple small-enough subspaces
can alleviate the barren plateau problem. Nevertheless, to obtain potential quantum advantages, ergodically searching these subspaces may not be efficient in some cases. Additionally, the error-prone issue
of NISQ computers limits their capability further. In consequence, choosing the appropriate columns or
partial elements of these columns by consuming few resources to span a more accurate search subspace
becomes critical. However, it may be cumbersome due to its dependence on the correlation among the
assets and subspaces.
Acknowledgements

This work was supported by National Natural Science Foundation of China (Grant No. 12034018).

Supporting information Appendixes A–H. The supporting information is available online at info.scichina.com and link.
springer.com. The supporting materials are published as submitted, without typesetting or editing. The responsibility for scientific accuracy and content remains entirely with the authors.
References
1 Feynman R P. Simulating physics with computers. Int J Theor Phys, 1982, 21: 467–488
2 Shor P W. Algorithms for quantum computation: discrete logarithms and factoring. In: Proceedings of the 35th Annual
Symposium on Foundations of Computer Science, 1994. 124–134
3 Grover L K. Quantum mechanics helps in searching for a needle in a haystack. Phys Rev Lett, 1997, 79: 325–328
4 Harrow A W, Hassidim A, Lloyd S. Quantum algorithm for linear systems of equations. Phys Rev Lett, 2009, 103: 150502
5 Nielsen M A, Chuang I L. Quantum Computation and Quantum Information (10th Anniversary edition). Cambridge: Cambridge University Press, 2010
6 Preskill J. Quantum computing in the NISQ era and beyond. Quantum, 2018, 2: 79
7 Leymann F, Barzen J. The bitter truth about gate-based quantum algorithms in the NISQ era. Quantum Sci Technol, 2020,
5: 044007
8 Bharti K, Cervera-Lierta A, Kyaw T H, et al. Noisy intermediate-scale quantum algorithms. Rev Mod Phys, 2022, 94: 015004
9 Lau J W Z, Lim K H, Shrotriya H, et al. NISQ computing: where are we and where do we go? AAPPS Bull, 2022, 32: 27
10 Cerezo M, Arrasmith A, Babbush R, et al. Variational quantum algorithms. Nat Rev Phys, 2021, 3: 625–644
11 Peruzzo A, McClean J, Shadbolt P, et al. A variational eigenvalue solver on a photonic quantum processor. Nat Commun,
2014, 5: 4213
12 Farhi E, Goldstone J, Gutmann S. A quantum approximate optimization algorithm. 2014. ArXiv:1411.4028

Wang S B, et al.

13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64

Sci China Inf Sci

August 2025, Vol. 68, Iss. 8, 180504:11

Kandala A, Mezzacapo A, Temme K, et al. Hardware-efficient variational quantum eigensolver for small molecules and
quantum magnets. Nature, 2017, 549: 242–246
Moll N, Barkoutsos P, Bishop L S, et al. Quantum optimization using variational algorithms on near-term quantum devices.
Quantum Sci Technol, 2018, 3: 030503
McArdle S, Endo S, Aspuru-Guzik A, et al. Quantum computational chemistry. Rev Mod Phys, 2020, 92: 015003
Tilly J, Chen H, Cao S, et al. The variational quantum eigensolver: a review of methods and best practices. Phys Rep, 2022,
986: 1–128
O’Brien T E, Streif M, Rubin N C, et al. Efficient quantum computation of molecular forces and other energy gradients. Phys
Rev Res, 2022, 4: 043210
Fedorov D A, Peng B, Govind N, et al. VQE method: a short survey and recent developments. Mater Theor, 2022, 6: 2
Biamonte J, Wittek P, Pancotti N, et al. Quantum machine learning. Nature, 2017, 549: 195–202
Cong I, Choi S, Lukin M D. Quantum convolutional neural networks. Nat Phys, 2019, 15: 1273–1278
Li G, Zhao X, Wang X. Quantum self-attention neural networks for text classification. 2022. ArXiv:2205.05625
Lamata L. Quantum machine learning implementations: proposals and experiments. Adv Quantum Tech, 2023, 6: 2300059
Nannicini G. Performance of hybrid quantum-classical variational heuristics for combinatorial optimization. Phys Rev E,
2019, 99: 013304
Liu X, Angone A, Shaydulin R, et al. Layer VQE: a variational approach for combinatorial optimization on noisy quantum
computers. IEEE Trans Quantum Eng, 2022, 3: 1–20
Palackal L, Poggel B, Wulff M, et al. Quantum-assisted solution paths for the capacitated vehicle routing problem. 2023.
ArXiv:2304.09629
Wang Z, Hadfield S, Jiang Z, et al. Quantum approximate optimization algorithm for MaxCut: a fermionic view. Phys Rev
A, 2018, 97: 022304
Barkoutsos P K, Nannicini G, Robert A, et al. Improving variational quantum optimization using CVaR. Quantum, 2020, 4:
256
Yu Y, Cao C, Dewey C, et al. Quantum approximate optimization algorithm with adaptive bias fields. Phys Rev Res, 2022,
4: 023249
Amaro D, Modica C, Rosenkranz M, et al. Filtering variational quantum algorithms for combinatorial optimization. Quantum
Sci Technol, 2022, 7: 015021
Zhu L, Tang H L, Barron G S, et al. Adaptive quantum approximate optimization algorithm for solving combinatorial problems
on a quantum computer. Phys Rev Res, 2022, 4: 033029
Qu D, Matwiejew E, Wang K, et al. Experimental implementation of quantum-walk-based portfolio optimization. Quantum
Sci Technol, 2024, 9: 025014
Benedetti M, Lloyd E, Sack S, et al. Parameterized quantum circuits as machine learning models. Quantum Sci Technol,
2019, 4: 043001
Herasymenko Y, O’Brien T E. A diagrammatic approach to variational quantum ansatz construction. Quantum, 2021, 5: 596
Cerezo M, Sone A, Volkoff T, et al. Cost function dependent barren plateaus in shallow parametrized quantum circuits. Nat
Commun, 2021, 12: 1791
Marrero C O, Kieferová M, Wiebe N. Entanglement-induced barren plateaus. PRX Quantum, 2021, 2: 040316
Leone L, Oliviero S F E, Cincio L, et al. On the practical usefulness of the hardware efficient ansatz. 2022. ArXiv:2211.01477
Holmes Z, Sharma K, Cerezo M, et al. Connecting ansatz expressibility to gradient magnitudes and barren plateaus. PRX
Quantum, 2022, 3: 010313
Bharti K, Haug T. Iterative quantum-assisted eigensolver. Phys Rev A, 2021, 104: L050401
Gard B T, Zhu L, Barron G S, et al. Efficient symmetry-preserving state preparation circuits for the variational quantum
eigensolver algorithm. npj Quantum Inf, 2020, 6: 10
Dicke R H. Coherence in spontaneous radiation processes. Phys Rev, 1954, 93: 99–110
Orús R, Mugel S, Lizaso E. Quantum computing for finance: overview and prospects. Rev Phys, 2019, 4: 100028
Herman D, Googin C, Liu X, et al. A survey of quantum computing for finance. 2022. ArXiv:2201.02773
Peng T, Harrow A W, Ozols M, et al. Simulating large quantum circuits on a small quantum computer. Phys Rev Lett, 2020,
125: 150504
Ying C, Cheng B, Zhao Y, et al. Experimental simulation of larger quantum circuits with fewer superconducting qubits. Phys
Rev Lett, 2023, 130: 110601
Hua F, Jin Y, Chen Y, et al. Exploiting qubit reuse through mid-circuit measurement and reset. 2022. ArXiv:2211.01925
Hodson M, Ruck B, Ong H, et al. Portfolio rebalancing experiments using the quantum alternating operator ansatz. 2019.
ArXiv:1911.05296
Mukherjee C S, Maitra S, Gaurav V, et al. Preparing dicke states on a quantum computer. IEEE Trans Quantum Eng, 2020,
1: 1–17
Bärtschi A, Eidenbenz S. Short-depth circuits for dicke state preparation. In: Proceedings of IEEE International Conference
on Quantum Computing and Engineering, 2022. 87–96
Özdemir S K, Shimamura J, Imoto N. A necessary and sufficient condition to play games in quantum mechanical settings.
New J Phys, 2007, 9: 43
Pezzè L, Smerzi A, Oberthaler M K, et al. Quantum metrology with nonclassical states of atomic ensembles. Rev Mod Phys,
2018, 90: 035005
Miguel-Ramiro J, Dür W. Delocalized information in quantum networks. New J Phys, 2020, 22: 043011
Cruz D, Fournier R, Gremion F, et al. Efficient quantum algorithms for GHZ and W states, and implementation on the IBM
quantum computer. Adv Quantum Tech, 2019, 2: 1900015
Long G L. General quantum interference principle and duality computer. Commun Theor Phys, 2006, 45: 825–844
Wang S, Wang Z, Cui G, et al. Fast black-box quantum state preparation based on linear combination of unitaries. Quantum
Inf Process, 2021, 20: 270
Bittel L, Kliesch M. Training variational quantum algorithms is NP-hard. Phys Rev Lett, 2021, 127: 120502
Tüysüz C, Clemente G, Crippa A, et al. Classical splitting of parametrized quantum circuits. 2022. ArXiv:2206.09641
Dou M, Zou T, Fang Y, et al. QPanda: high-performance quantum computing framework for multiple application scenarios.
2022. ArXiv:2212.14201
Javadi-Abhari A, Treinish M, Krsulich K, et al. Quantum computing with Qiskit. 2024. ArXiv:2405.08810
Wang S, Fontana E, Cerezo M, et al. Noise-induced barren plateaus in variational quantum algorithms. Nat Commun, 2021,
12: 6961
Cai Z, Babbush R, Benjamin S C, et al. Quantum error mitigation. 2022. ArXiv:2210.00921
Bonet-Monroig X, Sagastizabal R, Singh M, et al. Low-cost error mitigation by symmetry verification. Phys Rev A, 2018, 98:
062339
Nation P D, Kang H, Sundaresan N, et al. Scalable mitigation of measurement errors on quantum computers. PRX Quantum,
2021, 2: 040326
Temme K, Bravyi S, Gambetta J M. Error mitigation for short-depth quantum circuits. Phys Rev Lett, 2017, 119: 180509
Kolotouros I, Wallden P. Evolving objective function for improved variational quantum optimization. Phys Rev Res, 2022, 4:
023225

