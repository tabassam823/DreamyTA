Sample-efficient learning of quantum many-body systems
Anurag
Anshu∗

Srinivasan
Arunachalam†

Tomotaka
Kuwahara‡

Mehdi
Soleimanifar§

arXiv:2004.07266v1 [quant-ph] 15 Apr 2020

April 17, 2020

Abstract
We study the problem of learning the Hamiltonian of a quantum many-body system given
samples from its Gibbs (thermal) state. The classical analog of this problem, known as learning
graphical models or Boltzmann machines, is a well-studied question in machine learning and
statistics. In this work, we give the first sample-efficient algorithm for the quantum Hamiltonian
learning problem. In particular, we prove that polynomially many samples in the number of
particles (qudits) are necessary and sufficient for learning the parameters of a spatially local
Hamiltonian in `2 -norm.
Our main contribution is in establishing the strong convexity of the log-partition function of
quantum many-body systems, which along with the maximum entropy estimation yields our
sample-efficient algorithm. Classically, the strong convexity for partition functions follows from
the Markov property of Gibbs distributions. This is, however, known to be violated in its exact
form in the quantum case. We introduce several new ideas to obtain an unconditional result
that avoids relying on the Markov property of quantum systems, at the cost of a slightly weaker
bound. In particular, we prove a lower bound on the variance of quasi-local operators with
respect to the Gibbs state, which might be of independent interest. Our work paves the way
toward a more rigorous application of machine learning techniques to quantum many-body
problems.

∗

Institute for Quantum Computing and Department of Combinatorics and Optimization, University of Waterloo,
Canada and Perimeter Institute for Theoretical Physics, Canada. aanshu@uwaterloo.ca
†
IBM Research. Srinivasan.Arunachalam@ibm.com
‡
Mathematical Science Team, RIKEN Center for Advanced Intelligence Project (AIP), Japan and Interdisciplinary
Theoretical & Mathematical Sciences Program (iTHEMS) RIKEN, Japan. tomotaka.kuwahara@riken.jp
§
Center for Theoretical Physics, MIT. mehdis@mit.edu

Contents
1

Introduction

1

2

Main result

3

3

Proof overview
3.1 Maximum entropy estimation and sufficient statistics . . . . . . . . . . . . . . . . . .
3.2 Strong convexity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.3 Strong convexity of log-partition function: Review of the classical case . . . . . . . .
3.4 Strong convexity of log-partition function: Proof of the quantum case . . . . . . . . .

4
4
5
7
8

4

Further discussions
11
4.1 Connection to previous work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
4.2 Open questions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11

5

Preliminaries
5.1 Some mathematical facts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.2 Local Hamiltonians and quantum Gibbs states . . . . . . . . . . . . . . . . . . . . . .
5.3 Quantum belief propagation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.4 Change in the spectrum after applying local operators . . . . . . . . . . . . . . . . . .
5.5 Local reduction of global operators . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.6 Stochastic convex optimization applied to Hamiltonian learning . . . . . . . . . . . .

12
12
13
15
16
17
18

6

Strong convexity of log Zβ (λ)

20

7

Lower bound on the variance of quasi-local operators
7.1 Warm-up: Variance at infinite temperature . . . . . . . . . . . . . . . . . . . . . . . .
7.2 Variance at finite temperature . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.3 Some key quantities in the proof and proof sketch . . . . . . . . . . . . . . . . . . . .
7.4 Reducing the global problem to a local problem . . . . . . . . . . . . . . . . . . . . .
7.5 Variance of operators with small support: finite temperature to infinite temperature
7.6 Invariance under local unitaries . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.7 Proof of the Theorem 33 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.8 Proof of Claims 37 and 38 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

23
24
27
28
29
31
32
33
35

References

40

A Proof of Fact 12

44

B Fourier transform of tanh(βω/2)/(βω/2)

45

C Derivation of the sub-exponential concentration

47

f
D Quasi-locality of W

51

E Proof of Lemma 34

53

F Proof of Theorem 3

57

1

Introduction

The success of machine learning algorithms in analyzing high-dimensional data, has resulted in
a surge of interest in applying these algorithms to study quantum many-body systems whose description requires dealing with an exponentially large state space. One important problem in this
direction is the quantum Hamiltonian learning problem, which has been the focus of many recent theoretical and experimental works [BAL19, BGP+ 20, WGFC14b, WGFC14a, EHF19, WPS+ 17]. Here,
one would like to learn the underlying Hamiltonian of a quantum system given multiple identical copies of its Gibbs (thermal) state. The classical analog of this problem is a central problem in
machine learning and modern statistical inference, known as learning graphical models or Boltzmann
machines (aka Ising models). Classically, understanding the learnability of Boltzmann machines
was initiated by the works of Hinton and others in the 80s [AHS85, HS+ 86]. In the past few years,
there has been renewed interest in this subject and has seen significant progress resulting in efficient
provable learning algorithms for graphical models with optimal sample and time complexity especially for sparse and bounded-degree graphs [Bre15, KM17, VMLC16, HKM17, RWL+ 10]. Thus far,
a rigorous analysis of the quantum Hamiltonian learning problem with guaranteed sample complexity has been lacking. The main contribution of this work is to provide the first sample-efficient
algorithm for this task.
We now introduce the quantum Hamiltonian learning problem. Consider a κ-local Hamiltonian H acting on n qudits. In general, we can parameterize H by
H(µ) =

m
X

µ` E`

`=1

where µ` ∈ R and the operators E` are Hermitian and {E` } forms an orthogonal basis for the space
of operators. For instance in the case of qubits, E` are tensor product of at most κ Pauli operators
that act non-trivially only on spatially contiguous qubits. We let the vector µ = (µ1 , . . . , µm )> be the
vector of interaction coefficients. In our setup, without loss of generality we assume the Hamiltonian
is traceless, i.e., for the identity operator E` = 1, the coefficient µ` = 0. At a inverse-temperature β,
the qudits are in the Gibbs state defined as
ρβ (µ) =

e−βH(µ)
.
tr[e−βH(µ) ]

In the learning problem, we are given multiple copies of ρβ (µ) and can perform arbitrary local
measurements on them. In particular, we can obtain all the κ-local marginals of ρβ (µ) denoted by
e` = tr[ρβ (µ)E` ] for ` ∈ [m].
The goal is to learn the coefficients µ` of the Hamiltonian H using the result of these measurements.
We call this the Hamiltonian Learning Problem. Before stating our main results, we provide further
motivations for looking at this problem.
Physics perspective. Quantum many-body systems consist of many quantum particles (qudits)
that locally interact with each other. The interactions between these particles are described by the
Hamiltonian of the system. Even though the interactions in the Hamiltonian are local, the state
of the whole system can be highly entangled. This is not only true at low temperatures when the
1

system is in the lowest energy eigenstate of its Hamiltonian (the ground state), but remains true
even at finite temperatures when the state is a mixture of different eigenstates of the Hamiltonian
known as the Gibbs or thermal state.
While the underlying fundamental interactions in these systems are long known to be given by
Coulomb forces between electrons and nuclei, they are too complicated to be grasped in entirety.
Physicists are primarily interested in “effective interactions” that, if accurately chalked out, can
be used to describe a variety of properties of the system. How can such effective interactions be
learned in a system as complicated as, for example, the high temperature superconductor? Algorithms for Hamiltonian learning can directly address this problem and provide a suitable approximation to the effective interactions.
Verification of quantum devices. The size of the available quantum computers is increasing and
they are becoming capable of running more intricate quantum algorithms or preparing highly entangled states over larger number of qubits. Due to the noise in these devices, a major challenge
that accompanies the scalable development of quantum devices is to efficiently certify their functionality. In recent times, one widely used subroutine in quantum algorithms is quantum Gibbs
sampling. Preparing and measuring the Gibbs state of a given Hamiltonian is used in quantum
algorithms for solving semi-definite programs [BS17, AGGW20, BKL+ 17, AG18, BKF19], quantum
simulated annealing [Mon15b, HW20], metropolis sampling [TOV+ 11], quantum machine learning [WKS14], or quantum simulations at finite temperature [MST+ 20]. Given near term quantum
devices will be noisy, an important problem when implementing these quantum subroutines is to
certify the performance of the quantum Gibbs samplers and to calibrate them. More specifically, it
would be ideal to have a classical algorithm that given samples from the output of a Gibbs sampler
determines if the correct Hamiltonian has been implemented.
Quantum machine learning for quantum data. A popular family of models for describing classical distributions are graphical models or Markov random fields. These models naturally encode the
causal structure between random variables and have found widespread applications in various
areas such as social networks, computer vision, signal processing, and statistics (see [RWL+ 10]
for a survey). A simple and extremely well-studied example of such a family is the classical Ising
model (also known as the Boltzmann machine) defined over a graph whose vertices correspond to
the random variables xi . A natural distribution that one can associate to this model is
X

X
1
Pr[X = x] = exp
Jij xi xj +
hi xi
(1)
Z
i∼j

i

where Jij , hi ∈ R are real coefficients and the normalization factor Z is called the partition function.
This distribution in Eq. (1) is also known as the Gibbs distribution. There is a rich body of work on
learnability of Ising models given samples from the Gibbs distribution. Remarkably, a sequence
of works concluded in showing a classical efficient algorithm with a running time quadratic in the
number of vertices that outputs estimates of the coefficients Jij and hi [Bre15, KM17, VMLC16].
Similar results have been also proved for more general graphical models.
Considering these achievements in learning theory and the broad practical application of machine learning algorithms, there has been a rising interest in connecting these techniques to problems in quantum computing and many-body physics. This along with other related problems is
loosely referred to as quantum machine learning. Is there a natural problem that we can rigorously
2

establish such a connection for it? Thus far, almost-all the proposals we are aware of in this direction are mostly based on heuristic grounds. One proposal that stands out due to its similarity to the
classical case is the problem of learning quantum Ising model (aka quantum Boltzmann machine)
or more generally the Hamiltonian Learning Problem.
In this paper, we rigorously show that by applying tools from statistics and machine
learning such as maximum entropy estimation, one can get a sample complexity for the
Hamiltonian Learning Problem that is polynomial in the number of qudits. To the best of our knowledge, this is the first such result that unconditionally obtains a non-trivial sample complexity. We
believe our work opens the doors to further study of this problem using insight from machine
learning and optimization theory.

2

Main result

Motivated by these applications, we now formally define the Hamiltonian learning problem.
Pm
Problem 1 (Hamiltonian learning problem). Consider a κ-local Hamiltonian H(µ) =
`=1 µ` E`
that acts on n qudits and consists of m local terms such that max`∈[m] |µ` | ≤ 1. In the
Hamiltonian Learning Problem, we are given N copies of the Gibbs state of this Hamiltonian
ρβ (µ) =

e−βH(µ)
tr[e−βH(µ) ]

at a fixed inverse-temperature β. Our goal is to obtain an estimate µ̂ = (µ̂1 , . . . , µ̂m ) of the coefficients µk
such that with probability at least 1 − δ,
||µ − µ̂||2 ≤ ε,
where ||µ − µ̂||2 =

Pm

2
`=1 |µ` − µ̂` |

1

2

is the `2 -norm of the difference of µ and µ̂.

Our main result is a sample-efficient algorithm for the Hamiltonian Learning Problem.
Theorem 2 (Sample-efficient Hamiltonian learning). The Hamiltonian Learning Problem 1 can be
solved using
!
c
m
eO(β )
N =O
· m3 · log
(2)
β c̃ ε2
δ
copies of the Gibbs state ρβ (µ) = e−βH(µ) /tr[e−βH(µ) ], where c, c̃ ≥ 1 are constants that depend on the
geometry of the Hamiltonian.
As far as we are aware, our work is the first to establish unconditional and rigorous upper
bounds on the sample complexity of the Hamiltonian Learning Problem. For spatially local Hamiltonians the number of interaction terms m scales as O(n). Hence, our result in Theorem 2 implies
a sample complexity polynomial in the number of qudits.
The number of samples in (2) increases as β → ∞ or β → 0. As the temperature increases
(β → 0), the Gibbs state approaches the maximally mixed state independent of the choice of
parameters µ. At low temperatures (β → ∞), the Gibbs state is in the vicinity of the ground space,
3

which for instance, could be a product state |0i⊗n for the various choices of µ. In either cases, more
sample are required to distinguish the parameters µ.
√
To complement our upper bound, we also obtain a Ω( m) lower bound for the
Hamiltonian Learning Problem with `2 norm using a simple reduction to the state discrimination
problem. The proof appears in Appendix F. Hence, our upper bound in Theorem 2 is tight up to
polynomial factors.
Theorem 3. The number of copies N of the Gibbs state needed to solve the Hamiltonian Learning Problem
and outputs a µ̂ satisfying kµ̂ − µk2 ≤ ε with probability 1 − δ is lower bounded by
 √m + log(1 − δ) 
N ≥Ω
.
βε

3

Proof overview

In order to prove our main result, we introduce several new ideas. In this section, we provide a
sketch of the main ingredients in our proof.

3.1

Maximum entropy estimation and sufficient statistics

In statistical learning theory, a conventional method for obtaining the parameters of a probability
distribution from data relies on the concepts of sufficient statistics and the maximum entropy estimation. Suppose p(x; µ) is a family of probability distributions parameterized by µ that we want to
learn. This family could for instance be various normal distributions with different mean or variance. Let X1 , . . . , Xm ∼ p(x; µ) be m samples from a distribution in this family. A sufficient statistic
is a function T of these samples T (X1 , . . . , Xm ) such that conditioned on that, the original date set
X1 , . . . , Xm does not depend on the parameter µ. For example, the sample mean and variance are
well known sufficient statistic functions.
After obtaining the sufficient statistic of a given data set given classical samples, there is a natural algorithm for estimating the parameter µ: among all the distributions that match the observed
statistic T (X) find the one that maximizes the Shannon entropy. Intuitively, this provides us with
the least biased estimate given the current samples [Jay57a, Jay82]. This algorithm, which is closely
related to the maximum likelihood estimation, is commonly used for analyzing the sample complexity of classical statistical problems.
Our first observation when addressing the Hamiltonian Learning Problem is that this method can
be naturally extended to the quantum problem [Jay57b]. Indeed, the maximum entropy principle
has already appeared in other quantum algorithms such as [BKL+ 17]. More formally, we first show
that the marginals tr[E` ρ] for ` ∈ [m] form a sufficient statistic for the Hamiltonian Learning Problem.
Proposition 4 (Matching local marginals implies global equivalence). Consider the following two
Gibbs states
P

P

e−β ` µ` E`
P
ρβ (µ) =
,
tr[e−β ` µ` E` ]

e−β ` λ` E`
P
ρβ (λ) =
tr[e−β ` λ` E` ]

(3)

such that tr[ρβ (λ)E` ] = tr[ρβ (µ)E` ] for all ` ∈ [m], i.e. all the κ-local marginals of ρβ (λ) match that
of ρβ (µ). Then, we have ρβ (λ) = ρβ (µ), which in turns implies λ` = µ` for ` ∈ [m].
4

Similar to the classical case discussed above, one implication of Proposition 4 is a method for
learning the Hamiltonian H: first measure all the κ-local marginals of the Gibbs state e` , then
among all the states of the form (3), find the one that matches those marginals. Finding such a
state can be naturally formulated in terms of an optimization problem known as the maximum
entropy problem:
max S(σ)
σ

s.t. tr[σE` ] = e` ,
σ > 0,

∀` ∈ [m]

(4)

tr[σ] = 1.

where S(σ) = −tr[σ log σ] is the von Neumann entropy of the state σ. The optimal solution of this
program is a quantum state with a familiar structure [Jay57b]. Namely, it is a Gibbs state ρ(λ) for
some set of coefficients λ = (λ1 , . . . , λm ). The coefficients λ are the Lagrange multipliers corresponding to the dual of this program. Indeed, we can write the dual program of Eq. (4) as follows:
µ = arg min log Zβ (λ) + β ·
λ=(λ1 ,...,λm )

m
X

λ` e` ,

(5)

`=1

P

where Zβ (λ) = tr e−β· ` λ` E` is the partition function at inverse-temperature β. In principle, according to the result of Proposition 4, we could solve the Hamiltonian Learning Problem by finding
the optimal solution of the dual program in (5). Of course, the issue with this approach is that
since we have access to limited number of samples of the original Gibbs state ρβ (µ), instead of the
exact marginals e` , we can only approximately estimate the e` s. We denote these estimates by ê` .
This means instead of solving the dual program (5), we solve its empirical version

µ̂ = arg min
λ=(λ1 ,...,λm )

log Zβ (λ) + β ·

m
X

λ` ê` .

(6)

`=1

The main technical problem that we address in this work is analyzing the robustness of the
programs (4) and (5) to the statistical error in the marginals as appears in (6). This is an instance
of a stochastic optimization which is a well-studied problem in optimization. In the next section, we
review the ingredients from convex optimization that we need in our analysis.

3.2

Strong convexity

One approach to incorporate the effect of the statistical errors in the marginals e` into the estimates for µ` is to use Proposition 4. It is not hard to extend this proposition to show that
if a Gibbs states ρβ (λ) approximately matches the marginals of ρβ (µ) up to some error ε, then
||ρβ (µ) − ρβ (λ)||21 ≤ O(mε) (see Section 5.2 for more details). This bound, however, is not strong
enough for our purposes. This is because if we try to turn this bound to a one on the coefficients µ` of the Hamiltonian, we need to bound || log ρβ (µ) − log ρβ (λ)||. Unfortunately, the function
log(x) does not have a bounded gradient (i.e., it is not Lipschitz) over its domain and in general
|| log ρβ (µ) − log ρβ (λ)|| can be exponentially worse than ||ρβ (µ) − ρβ (λ)||1 . In order to overcome
the non-Lipschitz nature of the logarithmic function and bound || log ρβ (µ) − log ρβ (λ)||, we prove
a property of the dual objective function (5) known as the strong convexity, which we define now.

5

Definition 5. Consider a convex function f : Rm 7→ R with gradient ∇f (x) and Hessian ∇2 f (x) at a
point x.1 This function f is said to be α-strongly convex in its domain if it is differentiable and for all x, y,
1
f (y) ≥ f (x) + ∇f (x)> (y − x) + α||y − x||22 ,
2
or equivalently if its Hessian satisfies
∇2 f (x)  α1.2
P
2
In other words, for any vector v ∈ Rm , it holds that i,j vi vj ∂x∂i ∂xj f (x) ≥ α||v||22 .

(7)

Roughly speaking, strong convexity puts a limit on how slow a convex function f (x) changes.3
This is particularly useful because given two points x, y and an upper bound on |f (y) − f (x)| and
∇f (x)> (y − x), it allows us to infer an upper bound on ||y − x||2 .
For our application, we think of f as being log Zβ (·). Then the difference |f (y) − f (x)| is the
difference between the optimal solution of the original program in Eq. (5) and that of its empirical
version in Eq. (6) which includes the statistical error. We apply this framework to our optimization
(6) in two steps:
1) Proving the strong convexity of the objective function: This is equivalent to showing that the
log-partition function (aka the free energy) is strongly convex, i.e., ∇2 log Zβ (λ)  α1 for some
positive coefficient α. In particular, this means that the optimization (6) is a convex program.
This result is the main technical contribution of our work and is stated in the following theorem:
P
Theorem 6 (Informal: strong convexity of log-partition function). Let H = m
`=1 µ` E` be a κlocal Hamiltonian over a finite dimensional lattice with ||µ|| ≤ 1. For a given inverse-temperature β, there
are constants c, c0 > 3 depending on the geometric properties of the lattice such that
0

c

∇2 log Zβ (µ)  e−O(β )

βc
· 1,
m
c

(8)
c0

i.e., for every vector v ∈ Rm we have v T · ∇2 log Zβ (µ) · v ≥ e−O(β ) βm · ||v||22 .
2) Bounding the error in estimating µ in terms of the error in estimating the marginals e` : In this
step we show that as long as the statistical error of the marginals is small, using the strong convexity property from step (1), we can still prove an upper bound on the difference between the
solutions of the convex programs (5), (6).
We discuss this in more details later in Section 5.6. The result can be stated as follows:
Theorem 7 (Error bound from strong convexity). Let δ, α > 0. Suppose the marginals e` are determined up to error δ, i.e., |e` − ê` | ≤ δ for all ` ∈ [m]. Additionally assume ∇2 log Zβ (λ)  α1 and
||λ|| ≤ 1. Then the optimal solution to the program (6) satisfies
√
2β mδ
||µ − µ̂||2 ≤
α
Combining Theorem 6 and Theorem 7, we obtain the main result of our paper. We now proceed
to sketch the proof of Theorem 6.
2

1

Recall that the entries of the Hessian matrix ∇2 f (x) are given by ∂x∂i ∂xj f (x)
2
By A  B we mean A − B is positive semidefinite.
3
This should not be confused with a related property called the smoothness which limits how fast the function grows.

6

3.3

Strong convexity of log-partition function: Review of the classical case

In order to better understand the motivation behind our quantum proof, it is insightful to start with
the classical Hamiltonian learning problem. This helps us better describe various subtleties and
what goes wrong when trying to adapt the classical techniques to the quantum case. We continue
using the quantum notation here,
P but the reader can replace the Hamiltonian H, for instance, with
the classical Ising model H = i∼j Jij xi xj (where xi ∈ {−1, 1} and Jij ∈ R).
The entries of the Hessian ∇2 log Zβ (µ) for classical Hamiltonians are given by
i
∂2 h
log Zβ (µ) = Cov[Ei , Ej ]
∂µi ∂µj

(9)

where Cov is the covariance function which is defined as Cov[Ei , Ej ] = hEi Ej i − hEi ihEj i with
the expectation taken with respect to the Gibbs distribution (i.e., hEi = tr[E · ρβ (µ)]). To prove the
strong convexity of the log-partition function at a constant β, using (9) it suffices to show that for
every vector v, we have
"m
#
m
X
X
X
∂2
(10)
vi vj
log Zβ (µ) = Var
v` E` ≥ Ω(1) ·
v`2 .
∂µi ∂µj
i,j

`=1

`=1

P
Although the operator ` v` E` is a local Hamiltonian,
note the mismatch between this operator
P
µ
and the original Hamiltonian in the Gibbs state m
`=1 ` E` . Also note that compared to the inequality (8), the inequality (10) claims a stronger lower bound of Ω(1).
P
2
Before proving Eq. (10), we remark that an upper bound of Var[ m
`=1 v` E` ] ≤ O(1)||v||2 is known
in literature, under various conditions like the decay of correlations both in classical and quantum
settings [Ara69, Gro79, PY95, Uel04, KGK+ 14, FU15]. This upper bound intuitively makes sense because the variance of the thermal state of a Hamiltonian and other local observables are expected to
be extensive, i.e., they scale with the number of particles (spins) or norm of the Hamiltonian, which
is replaced by ||v||22 in our setup. However, in the classical Hamiltonian learning problem, we are
interested in obtaining a lower bound on the variance. To this end, a crucial property of the (classical) Gibbs distributions that allows us to prove the inequality (10) is the conditional independence
or the Markov property of classical systems.
Definition 8 (Markov property). Suppose the interaction graph is decomposed into three disjoint regions
A, B, and C such that region B “shields” A from C, i.e., the vertices in region A are not connected to those
in C. Then, conditioned on the sites in region B, the distribution of sites in A is independent of those in C.
This is often conveniently expressed in terms of the conditional mutual information by I(A : C|B) = 0.
It is known by the virtue of the Hammersley-Clifford theorem [HC71] that the family of distributions with the Markov
P property coincides with the Gibbs distributions. Using this property, we
can lower bound Var [ m
`=1 v` E` ] in terms of variance of local terms E` by conditioning on a subset
of sites. To this end, we consider a partition of the interaction graph into two sets A and B. The
set B is chosen, suggestively, such that the vertices in A are not connected (via any edges) to each
other. We denote the spin configuration of sites in B collectively by sB . Then using the concavity
of the variance and the Markov property, we have

7

Var

"m
X
`=1

#
v` E`

"

(1)

≥ EsB Var

"m
X

=

v` E` sB

`=1


(2) X

##



EsB Var 

≥ Ω(1)

v` E` sB 

`:E` acts on x

x∈A
(3)


X

m
X

v`2 ,

(11)

`=1

where inequality (1) follows from the law of total variance, equality (2) can be justified as follows:
by construction, the local terms E` either completely lie inside region B or intersect with only
one of the sites in region A. In the former, the local conditional variance Var [E` |sB ] vanishes,
whereas in the latter, the interaction terms E` that act on different sites x ∈ A become uncorrelated
and the global variance decomposes into a sum of local variance. Finally, inequality (3) is derived
by noticing that at any constant inverse-temperature β, the local variance is lower bounded by
a constant that scales as e−O(β) . By carefully choosing the partitions A and B such that
P|A| =2
O(n), we can make sure that the variance in inequality (2) is a constant fraction of the m
`=1 v`
as in (11) (see [Mon15a, VMLC16]
 for details). This lower bound on variance results in a sample
complexity O eO(β) m(log m)ε−2 , which compared to our result in Theorem 2 is more efficient (by
only a polynomial factor in m).

3.4

Strong convexity of log-partition function: Proof of the quantum case

If we try to directly quantize the proof strategy of the classical case in the previous section, we
immediately face several issues. We now describe the challenges in obtaining a quantum proof
along with our techniques to overcome them.
3.4.1

Relating the Hessian to a variance

The first problem is that we cannot simply express the entries of the Hessian matrix ∇2 log Zβ (µ)
in terms of Cov[Ei , Ej ] as in (9). This expression in (9) only holds for Hamiltonians with commuting
terms, i.e., [Ei , Ej ] = 0 for all i, j ∈ [m]. The Hessian for the non-commuting Hamiltonians takes a
complicated form (see Lemma 29 for the full expression) that makes its analysis difficult. Our first
contribution is to recover a similar result to (10) in the quantum case by showing that, for every v,
we can still lower bound v > · ∇2 log Zβ (µ) · v by the variance of a suitably defined quasi-local operator.
We later define what we mean by “quasi-local” more formally (see Definition 14 in the body), but
for now one can assume such an operator is, up to some small error, sum of local terms.
Lemma 9 (A lower bound on ∇2 log Zβ (µ)
(µ)). For any vector v ∈ Rm , we define a quasi-local operator
P
m
f=
e
W
`=1 v` E` , where the operators Ẽ` are defined by
Z ∞
e` =
E
fβ (t) e−iHt E` eiHt dt.
(12)
−∞

8

π|t|/β

2
+1
Here fβ (t) = βπ
is defined such that fβ (t) scales as β1 e−π|t|/β for large t and fβ (t) ∝ log(1/t)
log eeπ|t|/β −1
for t → +0. We claim that

X

vi vj

i,j

3.4.2

∂2
f]
log Zβ (µ) ≥ β 2 Var[W
∂µi ∂µj

(13)

Lower bounding the variance

As a result of Lemma 9, we see
that from here onwards, it suffices to lower bound the variance of
f = Pm v` Ẽ` . One may expect the same strategy based on the Markov
the quasi-local operator W
`=1
property in (11) yields the desired lower bound. Unfortunately, it is known that a natural extension of this property to the quantum case, expressed in terms of the quantum conditional mutual
information (qCMI), does not hold. In particular, example Hamiltonians are constructed in [LP08]
such that for a tri-partition A, B, C as in Definition 8, their Gibbs states have non-zero qCMI, i.e.,
I(A : C|B) > 0. Nevertheless, it is conjectured that an approximate version of this property can
be recovered i.e., I(A : C|B) ≤ e−Ω(dist(A,C)) . In other words, the approximate property claims
that qCMI is exponentially small in the width of the shielding region B. Thus far, this conjecture
has been proved only at sufficiently high temperatures [KKB19] and on 1D chains [KB19]. Even
assuming this conjecture is true, we currently do not know how to recover the argument in (11).
We get back to this point in Section 4.2. Given this issue we ask,
Can we obtain an unconditional lower bound on the variance of a quasi-local observable at any
inverse-temperature β without assuming quantum conditional independence?
Our next contribution is to give an affirmative answer to this question. To achieve this, we modify
the classical strategy as explained below.
From global to
Plocal variance. One ingredient in the classical proof is to lower bound the global
variance Var[ ` v` E` ] by sum of local conditional variances Var[E` |sB ] as in (11). We prove a similar but slightly weaker result in the quantum regime. To simplify our discussion, let us ignore the
f = P v` Ẽ` is a quasi-local operator and view it as (strictly) local. Consider a special
fact that W
`
f is supported on a small number of sites. For instance,
case in which v is such that the operator W
f ] can be easily related to the
it could be that v1 > 0 while v2 , . . . , vm = 0. Then the variance Var[W
2
local variance Var[E1 ] and since E1 = 1, |tr[E1 ρβ ]| < 1, we get

f ] = v 2 · tr[E 2 ρβ ] − tr[E1 ρβ ]2 ≥ Ω(1) · v 2
Var[W
1
1
1
f]
We show that even in the general case, where v1 , . . . , vm are all non-zero, we can still relate Var[W
to the variance of a local operator supported on a constant region. Compared to the classical case
in (11), where the lower bound on Var[W ] includes a sum of O(m) local terms, our reduction to a
single local variance costs “an extra factor of m” in the strong convexity bound in Theorem 6.
Our reduction to local variance is based on the following observation. By applying Haarf except those that act on
random local unitaries, we can remove all the terms of the operator W
f(i) defined via
an arbitrary qudit at site i. We denote the remainder terms by W
f(i) = W
f − EU ∼Haar [U † W
f Ui ].
W
i
i
9

By using triangle inequality this relation implies
h
i
f 2 · Ui ρβ U † ] .
f ] ≥ 1 tr[W
f 2 ρβ ] − EU tr[W
Var[W
i
(i)
i
2

(14)

f 2 · Ui ρβ U † ]], this will allow us
Hence, if we could carefully analyze the effect of the term EUi [tr[W
i
f ] to the local variance tr[W
f 2 ρβ ]. We discuss this next.
to relate the global variance Var[W
(i)
Bounding the effect of local unitaries. While applying the above reduction helps us to go to
an easier local problem, we need to deal with the changes in the spectrum of the Gibbs state due
to applying the random local unitaries Ui . Could it be that the unitaries Ui severely change the
f and ρβ ? We show that this is not the case, relying on the facts: (1)
spectral relation between W
f and H that are energetically far away and (2) the
local unitaries cannot mix up subspaces of W
weight given by the Gibbs state ρβ to nearby subspaces of H are very similar at small β. Thus, (1)
allows us to focus the subspaces that are close in energy and (2) shows that similar weights of these
subspaces do not change the variance by much. In summary, we prove:
Proposition 10 (Invariance under local unitaries, informal). Let UX be a local unitary operator acting
on region X that has a constant size. There exists a constant c ≤ 1 such that
i 
c
h
f] .
f 2 · UX ρβ U † ≤ Var[W
(15)
tr W
X
When combined with (14), the inequality (15) implies the following loosely stated local lower
bound on the global variance:
 h
i 1
f ] ≥ tr W
f 2 ρβ c .
Var[W
(i)
f 2 ρβ ]. This can be done,
With this reduction, it remains to find a constant lower bound on tr[W
(i)
again, by applying a local unitary U . Roughly speaking, we use this unitary to perform a “change
of basis” that relates the local variance at finite temperature to its infinite-temperature version. The
spectrum of ρβ majorizes the maximally mixed state η. Hence, by applying a local unitary, we can
f 2 in the same order as that of ρβ such that when applied to both ρβ
rearrange the eigenvalues of W
(i)
2
†
f
f 2 η]. Formally, we show that
and η, we have tr[W U ρβ U ] ≥ tr[W
(i)

(i)

Proposition 11 (Lower bound on the local variance, informal). There exists a unitary U supported
on O(1) sites such that
h
i
h
i
f 2 U ρβ U † ≥ tr W
f2 η ,
tr W
(i)
(i)
where η is the maximally mixed state or the infinite temperature Gibbs state.
In summary, starting from (14) and following Proposition 10 and Proposition 11, the lower
bound on the global variance takes the following local form:
h
i  h
iO(1)
f 2 ρβ ≥ tr W
f2 η
tr W
.
(i)
h
i
f 2 η by a constant is now an easier task, which we explain in
Lower bounding the quantity tr W
(i)
more details later in Lemma 34 and Theorem 32.
10

4

Further discussions

4.1

Connection to previous work

A similar problem to Hamiltonian Learning Problem known as the shadow tomography has been
considered before [Aar18a, AR19, BKL+ 17] where instead of the coefficients µ` , we want to find
a state σ that approximately matches tr[E` σ] ≈ε tr[E` ρ] given multiple copies of an unknown
state ρ. It was shown poly(log m, log dn , 1/ε) copies of ρ are sufficient for tomography. The
Hamiltonian Learning Problem differs from the shadow tomography problem. Our goal is to estimate the Hamiltonian (i.e. the coefficients µ` ) within some given error bound. The shadow tomography protocol only concerns with estimating the marginals tr[E` ρ] up to a fixed error and by
itself does not imply a bound on the Hamiltonian. Moreover, since the Hamiltonians we consider
are spatially local, we only need to measure local observables E` . This means we do not need to
rely on the whole machinery of the shadow tomography which is applicable even when E` are
non-local. We instead use a variant of this method introduced in [HKP20] or other approaches
such as those in [CW20, BMBO19] to estimate tr[E` ρβ ].
There have been a number of proposals for the Hamiltonian Learning Problem in the past. In
[BAL19, EHF19, QR19] learning the Hamiltonian from local measurements is considered. Their
approach is based on setting up a linear system of equations whose constraints (i.e., the matrix of
coefficients) are determined from the measurement outcomes. The solution of these equations is
the parameter µk of the Hamiltonian. The sample complexity in this approach depends inverse
polynomially on the “spectral gap” of the matrix of coefficients which thus far has not been rigorously bounded. Another line of work considers learning the Hamiltonian using a trusted quantum simulator [WGFC14b, WGFC14a, VMN+ 19] which is analyzed using a combination of numerical evidence and heuristic arguments. Amin et al. [AAR+ 18b] quantized classical Boltzmann
machines and proposed a method to train and learn quantum Boltzmann machines using gradient descent.
As mentioned earlier, there has been a fruitful series of works on the classical analog of the
Hamiltonian Learning Problem (see e.g. [Bre15, KM17, VMLC16]). In our work, we assume it is a
priori known that the interaction graph of the Hamiltonian is spatially local. We then estimate
the parameters in `2 -norm using poly(n) samples which is polynomially tight even for classical
Hamiltonians. If we instead consider estimation in `∞ -norm, the classical algorithms can achieve a
stronger result. That is, given O(log n) samples, they succeed in efficiently learning the structure of
the underlying graph and its parameters in `∞ -norm. If we apply our current analysis to this setup,
we cannot improve our poly(n) sample complexity to O(log n). This is in part because the classical
results devise a more efficient convex program that learns the parameters node-wise (this relies on
the commutativity of the Hamiltonian terms), and partly because their required strong convexity
assumptions is based on the Markov property, none of which are known to be quantizable.

4.2

Open questions

In Section 3.1 we explained our approach to analyzing the Hamiltonian Learning Problem based on
reducing data to its sufficient statistics and using maximum entropy estimation. An issue with
this approach is the blowup in the computationally complexity. It is shown in [Mon15a] that this
approach basically requires approximating the partition function which is NP-hard. Ideally, one
would like to have an algorithm for the Hamiltonian Learning Problem that requires small number

11

of samples, but also has an efficient running time. Satisfying both these constraints for all inversetemperatures β even in the classical learning problems is quite challenge. It was only recently
that more efficient algorithms are devised for learning graphical models [KM17, VMLC16]. In
this work, we focus on the less demanding but still non-trivial question of bounding the sample
complexity and leave obtaining an efficient running time for future work. Below we mention some
of the open problems in this direction.
Our lower bound on the variance in Section 3.4.2 is obtained for any constant inversetemperature β. It is an interesting open question to improve this bound, ideally to a constant
independent of system size, assuming physically-motivated conditions such as the decay of correlations or the decay of conditional mutual information. Another approach might be to derive
such a bound at high temperatures where powerful tools such as cluster expansions are available
[KKB19]. We also expect our bounds can be improved for commuting Hamiltonians. Indeed, using structural results such as [BV03, AE11], one should be able to follow the same strategy as in
Section 3.3 to find a constant lower bound on the variance of commuting Hamiltonians.
There are recent results on efficiently computing the partition function of quantum many-body
systems under various assumptions [BG17, HMS19, KKB19]. We expect by combining these results
with our maximum entropy estimation algorithm in Section 3.1, one can obtain efficient classical algorithms for the Hamiltonian Learning Problem. Another approach might be to use calibrated
quantum computers (or Gibbs samplers) as in [BK16, BKL+ 17] to solve the maximum entropy optimization using multiplicative weight update method and learn the parameters of another quantum device.
Finally, an important future direction is to devise more refined objective functions for the
Hamiltonian Learning Problem that matches the performance of the learning algorithms for the classical problem as discussed in Section 4.1. Given the non-commutative nature of quantum Hamiltonians, this seems to require substantially new ideas and advances in characterizing the information
theoretic properties of the quantum Gibbs states.
Acknowledgements. We thank Aram Harrow, Yichen Huang, Rolando La Placa,
Sathyawageeswar Subramanian, John Wright, and Henry Yuen for helpful discussions. Part
of this work was done when SA and TK were visiting Perimeter Institute. SA was supported
in part by the Army Research Laboratory and the Army Research Office under grant number
W1975117. AA is supported by the Canadian Institute for Advanced Research, through funding
provided to the Institute for Quantum Computing by the Government of Canada and the Province
of Ontario. Perimeter Institute is also supported in part by the Government of Canada and the
Province of Ontario. TK was supported by the RIKEN Center for AIP and JSPS KAKENHI Grant
No. 18K13475. MS was supported by NSF grant CCF-1729369 and a Samsung Advanced Institute
of Technology Global Research Partnership.

5

Preliminaries

5.1

Some mathematical facts

Here we summarize some of the basic mathematical facts used in the proof. Let A, B be arbitrary
operator. The operator norm of A which
is its largest singular value is denoted by kAk. We also often
p
use the Frobenius norm kAkF := tr[A† A] and more generally the Hilbert-Schmidt inner product
12

between A, B defined by tr[A† B]. Additionally using Hölder’s inequality we have,
q
q
†
†
kABkF = tr(B AA B) ≤ kBk2 tr(AA† ) = kBk · kAkF .

(16)

We define the von Neumann entropy of a quantum state σ by S(σ) = −tr[σ log σ] and the relative
entropy between two states σ1 and σ2 by S(σ1 kσ2 ) = −tr[σ1 log σ2 ] − S(σ1 ).
The gradient of a real function f : Rm 7→ R is denoted by ∇f (x) and its Hessian (second deriva2
tive) matrix by ∇2 f (x). The entries of the Hessian matrix are given by ∂x∂i ∂xj f (x).
We write A  0 to represent a positive semi-definite (PSD) operator A, one such example of a PSD
operator is the Hessian matrix ∇2 f (x).
For convenience, we will also gather a collection of infinite sums over exponentials. For t > 0, let
Z ∞
Z
Z
 1 ∞ −y 1t
1 ∞ −x
Γ(t) :=
xt−1 e−x dx =
e d xt =
e
dy
t 0
t 0
0
be the gamma function. It holds that Γ(t) ≤ tt . This can be used to simplify several summations
that we encounter later. Finally, we collect a few useful summations that we use in our proofs in
the following fact. The proof is postponed until Appendix A.
Fact 12. Let a, c, p > 0 be reals and b be a positive integer. Then
P∞ −cj
c
≤ ec .
1)
j=0 e
2)

P∞

3)

P∞

5.2

p

b −cj ≤ 2 ·
j=0 j e
p
j=0



b+1
cp

c p
p
e−c(a+j) ≤ e− 2 a

 b+1
p

.


 1 
2 p
1
.
1 + p cp

Local Hamiltonians and quantum Gibbs states

Local Hamiltonians. In this work, we focus on Hamiltonians that are geometrically local. That
is, the interactions terms in the Hamiltonian act on a constant number of qudits that are in the
neighborhood of each other. To describe this notion more precisely, we consider a D-dimensional
lattice Λ ⊂ ZD that contains n sites with a d-dimensional qudit (spin) on each site. We denote the
dimension of the Hilbert space associated to the lattice Λ by DΛ . The Hamiltonian of this system is
X
H=
HX .
X⊂Λ

Each term HX acts only on the sites in X and X is restricted to be a connected set
P with respect
to Λ. We also define the Hamiltonian restricted to a region A ⊆ Λ by HA =
X⊆A HX . Let
B(r, i) := {j ∈ Λ|dist(i, j) ≤ r} denotes a ball (under the Manhattan distance in the lattice) of
size r centered at site i. For a given connected set X ∈ Λ, let diam(X) := max{dist(i, j) : i, j ∈ X}
denote the diameter of this set, X c := Λ \ X denote the complement of this set and ∂X denote its
boundary. Given two sets X, Y ∈ Λ, we define dist(X, Y ) := min (dist(i, j) : i ∈ X, j ∈ Y ).
In order describe our Hamiltonians, we consider an orthogonal Hermitian basis for the space
of operators acting on each qudit. For instance, for qubits this basis consists of the Pauli operators.
By decomposing each local term HX in terms of the tensor product of such basis operators, we find
the following canonical form for the Hamiltonian H:
13

Definition 13 (Canonical representation for κ-local Hamiltonians). A κ-local Hamiltonian H on a
lattice Λ is sum of m Hermitian operators E` each acting non-trivially on κ qudits. That is,
H=

m
X

µ` E` .

(17)

`=1

where µ` ∈ R and we assume ||E` || ≤ 1, tr[E`2 ] = DΛ , E`† = E` for ` ∈ [m], and
tr[Ek E` ] = 0

for k 6= `.

(18)

Since H is geometrically local, it holds that m = O(|Λ|) = O(n). As discussed earlier, we
extensively use the notion of quasi-local operators, which we now formally define.
Definition 14 (Quasi-local operators). An operator A is said to be (τ, a1 , a2 , ζ)-quasi-local if it can be
written as
A=

n
X

g` Ā`

`=1

with g` ≤ a1 · exp(−a2 `τ ),
!

Ā` =

X

aZ ,

|Z|=`

max
i∈Λ

X
Z:Z3i

kaZ k

≤ ζ,

(19)

where the sets Z ⊂ Λ are restricted to be balls.4
Although local operators are morally a special case of quasi-local operators (when τ = ∞), we
will reserve the above notation for operators with τ = O(1). A useful tool for analyzing quasilocality is the Lieb-Robinson bound, which shows a light-cone like behavior of the time evolution
operator.
Fact 15 (Lieb-Robinson bound [LR72], [NS09]). Let P, Q be operators supported on regions X, Y of
the D dimensional lattice Λ respectively. Let H be a (ζ, κ)-geometrically local Hamiltonian. There exist
constants vLR , f, c that only depend on ζ, κ and D such that


k[eiHt Ae−iHt , B]k ≤ f kAkkBk · min (|∂X|, |∂Y |) · min ec(vLR |t|−dist(X,Y )) , 1 .
Gibbs states. At an inverse-temperature β, a quantum many-body system with the Hamiltonian
H(µ) is in the Gibbs (thermal) state
ρβ (µ) =

e−βH(µ)
.
tr[e−βH(µ) ]

(20)

The partition function of this system is defined by Zβ (µ) = tr[e−βH(µ) ].
Remark 16. In our notation, we sometimes drop the dependency of the partition function or the Gibbs state
on µ. We also often simply use the term local Hamiltonian H or quasi-local operator A when referring to
Definition 13 and Definition 14.
4
The assumption that Z is a ball suffices for us. Our results on quasi-local operators also generalize to the case
where Z is an arbitrary regular shape, for example when the radii of the balls inscribing and inscribed by Z are of
constant proportion to each other.

14

As discussed earlier, local marginals of the Gibbs states can be used to uniquely specify them.
This provides us with “sufficient statistics” for learning the Hamiltonians from ρβ . More precisely,
we have:
Proposition 17 (Restatement of Proposition 4). Consider the following two Gibbs states
P

P

e−β ` µ` E`
P
ρβ (µ) =
,
tr[e−β ` µ` E` ]

e−β ` λ` E`
P
ρβ (λ) =
tr[e−β ` λ` E` ]

(21)

such that tr[ρβ (λ)Ej ] = tr[ρβ (µ)Ej ] for all j ∈ [m], i.e. all the κ-local marginals of ρβ (λ) match that of
ρβ (µ). Then, we have ρβ (λ) = ρβ (µ), which in turns implies λ` = µ` for ` ∈ [m].
Proof. We consider the relative entropy between ρβ (λ) and the Gibbs state ρβ (µ). We have
S (ρβ (µ)kρβ (λ)) = tr [ρβ (µ) (log ρβ (µ) − log ρβ (λ))]
#
"
X
= −S(ρβ (µ)) + β · tr ρβ (µ)
λ` E` + log Z(λ)

(22)

`

(1)

= −S(ρβ (µ)) + β

X

λ` tr[ρβ (λ)E` ] + log Z(λ)

(23)

`

= −S(ρβ (µ)) + S(ρβ (λ))

(2)

≥ 0,

(24)

where (1) follows because tr[ρβ (µ)E` ] = tr[ρβ (λ)E` ] for all ` ∈ [m] and (2) used the positivity of
relative entropy. Similarly, we can exchange the role of ρ(µ) and ρ(λ) in (24) and get
S (ρβ (λ)kρβ (µ)) = −S(ρβ (λ)) + S(ρβ (µ)) ≥ 0.

(25)

Combining these bounds imply S(ρβ (µ)) = S(ρβ (λ)) and hence from Eq. (24), we get
S(ρβ (µ)kρβ (λ)) = 0. It is known that the relative entropy of two distribution is zero only when
ρβ (µ) = ρβ (λ).PHence, we also have log ρβ (µ) = log ρβ (λ) or equivalently up to an additive term
P
m
m
`=1 µ` E` =
`=1 λ` E` . Since the operators E` form an orthogonal basis (see Eq. (18)), we see
that λ` = µ` for all ` ∈ [m].
t
u
Remark 18. When the marginals of the two Gibbs states only approximately match, i.e.,
|tr[ρβ (µ)E` ] − tr[ρβ (λ)E` ]| ≤ ε
for ` ∈ [m], then a similar argument to (24) shows that S(ρβ (µ)kρβ (λ)) ≤ O(mε). By applying Pinsker’s
inequality, we get ||ρβ (µ) − ρβ (λ)||21 ≤ O(mε).5

5.3

Quantum belief propagation

Earlier we saw that we could express the Gibbs state of a Hamiltonian H by Eq. (20). Suppose we
alter this Hamiltonian by adding a term V such that
H(s) = H + sV,
5

s ∈ [0, 1].

Pinsker’s inequality states that for two density matrices ρ, σ, we have kρ − σk21 ≤ 2 ln 2 · S(ρkσ).

15

(26)

How does the Gibbs state associated with this Hamiltonian change? If the new term V commutes
with the Hamiltonian H, i.e., [H, V ] = 0, then the derivative of the Gibbs state of H(s) is given by
d −βH(s)
β n −βH(s) o
e
= −βe−βH(s) V = −
e
,V ,
ds
2

(27)

where {e−βH(s) , V } = e−βH(s) V + V e−βH(s) denotes the anti-commutator. In the non-commuting
case though, finding this derivative is more complicated. The quantum belief propagation is a framework developed in [Has07, Kim17, KB19] for finding such derivatives in a way that reflects the
locality of the system.
Definition 19 (Quantum
P belief propagation operator). For every s ∈ [0, 1], β ∈ R, define H(s) =
H + sV where V = j,k Vj,k |jihk| is a Hermitian operator. Also let fβ (t) be a function whose Fourier
transform is
tanh(βω/2)
f˜β (ω) =
,
βω/2
1
i.e., fβ (t) = 2π

R

(28)

dω f˜β (ω)eiωt . The quantum belief propagation operator ΦH(s) (V ) is defined by
Z ∞
ΦH(s) (V ) =
dtfβ (t) e−iH(s)t V eiH(s)t .
−∞

P

j εj (s) |jihj|, we can write

X

|jihk| Vj,k f˜β (Ej (s) − Ek (s)).

Equivalently, in the energy basis of H(s) =
ΦH(s) (V ) =

j,k

(29)

Proposition 20 (cf. [Has07]). In the same setup as Definition 19, it holds that
o
d −βH(s)
β n −βH(s)
e
=−
e
, ΦH(s) (V ) .
ds
2

5.4

(30)

Change in the spectrum after applying local operators

H and P H be projection operators onto the eigenspaces of H whose enFor a Hamiltonian H, let P≤x
≥y
A , P A for the quasi-local operator
ergies are in ≤ x and ≥ y, respectively (we use similar notation P≤x
≥y
H |ψi = |ψi.
A). Consider a quantum state |ψi in the low-energy part of the spectrum such that P≤x
Suppose this states |ψi is perturbed by applying a local operator OX on a subset X ⊂ Λ of its qudits. Intuitively, we expect that the operator OX only affects the energy of |ψi up to O(|X|), i.e.,
H O |ψik ≈ 0 for y  x + |X|. A simple example is when |ψi is the eigenstate of a classical spin
kP≥y
X
system. By applying a local operation that flips the spins in a small region X, the energy changes
at most by O(|X|). The following lemma rigorously formulates the same classical intuition for
quantum Hamiltonians.

Lemma 21 (Theorem 2.1 of [AKL16]). Let H be an arbitrary κ-local operator such that
X
H=
hZ ,
|Z|≤κ

16

(31)

and each i ∈ Λ supports at most g terms hZ . Then, for an arbitrary operator OX which is supported on
H O P H is upper-bounded by
X ⊆ Λ, the operator norm of P≥y
X ≤x
H
H
kP≥y
OX P≤x
k ≤ kOX k · exp −


1
(y − x − 2g|X|) .
2gκ

(32)

In our analysis, we need an different version of this lemma for quasi-local operators instead of
κ-local operators. The new lemma will play a central role in lower-bounding the variance of quasilocal operators. The proof follows by the analysis of a certain moment function (as opposed to the
moment generating function in [AKL16]). Due to formal similarities between the proofs, we defer
the proof of the next lemma to Appendix C.
Lemma 22 (Variation of [AKL16] for quasi-local operators). Let A be a (τ, a1 , a2 , 1)-quasi-local operator, as given in Eq. (19), with τ ≤ 1. For an arbitrary operator OX supported on a subset X ⊆ Λ with
|X| = k0 and kOX k = 1, we have


A
A
kP≥x+y
OX P≤x
k ≤ c5 · k0 exp − (λ1 y/k0 )1/τ1 ,
(33)
2/τ

where τ1 := τ2 −1, c5 and λ1 are constants depending on a1 and a2 as c5 ∝ a2

5.5

−2/τ

and λ1 ∝ a2

respectively.

Local reduction of global operators

An important notion in our proofs will be a reduction of a global operator to a local one, which has
influence on a site i. Fix a subset Z ⊆ Λ and an operator O supported on Z. Define
O(i) := O − tri [O] ⊗

1i
d

(34)

where operator 1i is the identity operator on the ith site, d is the local dimension, tri is the partial
trace operation with respect to the site i. Note that O(i) removes all the terms in O that do not act on
the ith site. This can be explicitly seen by introducing a basis {EYα }α∈N,Y ∈Z of Hermitian operators,
where Y labels the support of EYα and α labels several possible operators on the same support.
We can assume that tr[(EYα )2 ] = 1, tri [EYα ] = 0 for every i ∈ Y , and the orthogonality condition
0
tr[EYα EYα 0 ] = 0 holds if α 6= α0 or Y 6= Y 0 . These conditions are satisfied by the appropriately
normalized Pauli operators. Expand
X
O=
gα,Y EYα .
α,Y

Then
O(i) =

X
α,Y

gα,Y EYα −

X
α,Y

gα,Y tri [EYα ] ⊗

1i
=
d

X

gα,Y EYα .

α,Y :Y 3i

Thus, O(i) is an operator derived from O, by removing all EYα which act as identity on i.

The
following claim shows that the Frobenius norm of a typical O(i) is not much small in comparison
to the Frobenius norm of O.
Claim 23. For every operator O and O(i) defined in Eq. (34), it holds that
max kO(i) k2F ≥
i∈Z

1 X
1
kO(i) k2F ≥
kOk2F ,
|Z|
|Z|
i∈Z

17

(35)

0

Proof. Using the identities tr[EYα EYα 0 ] = 0 and tr[(EYα )2 ] = 1, we have
X
X X
X
2
2
kOk2F =
gα,Y
≤
gα,Y
=
kO(i) k2F .
i∈Z α,Y :Y 3i

Y,α

i∈Z

t
u

This completes the proof.

5.6

Stochastic convex optimization applied to Hamiltonian learning

Suppose we want to solve the optimization
max f (x)

x∈Rm

for a function f : Rm → R which is of the form f (x) = Ey∼D [g(x, y)]. Here g(x, y) is some convex
function and the expectation Ey∼D is taken with respect to an unknown distribution D. Algorithms
for this maximization problem are based on obtaining i.i.d. samples y drawn from the distribution D.
In practice, we can only receive finite samples y1 , y2 , . . . , y` from such a distribution. Hence, instead
of the original optimization, we solve an empirical version
`

1X
g(x, yk ).
max
x∈Rm `
k=1

The natural question therefore is: How many samples ` do we need to guarantee the output of the
empirical optimization is close to the original solution? One answer to this problem relies on a
property of the objective function known as strong convexity.
Definition 24 (Restatement of Definition 5). Consider a convex function f : Rm 7→ R with gradient
∇f (x) and Hessian ∇2 f (x) at x. The function f is said to be α-strongly convex in its domain if it is
differentiable and for all x, y, and
1
f (y) ≥ f (x) + ∇f (x)> (y − x) + α||y − x||22 ,
2
or equivalently if its Hessian satisfies
∇2 f (x)  α1.
In other words, for any vector v ∈ Rm it holds that

(36)

2
∂2
i,j vi vj ∂xi ∂xj f (x) ≥ α||v||2 .

P

Next, we discuss how the framework of convex optimization and in particular strong convexity,
can be applied to the Hamiltonian Learning Problem. To this end, we define the following optimization problems.
Definition 25 (Optimization program for learning the Hamiltonian). We denote the objective function in the Hamiltonian Learning Problem and its approximate version (equations (5) and (6) in Section 3.1)
by L(λ) and L̂(λ) respectively, i.e.,
L(λ) = log Zβ (λ) + β ·

m
X

L̂(λ) = log Zβ (λ) + β ·

λ` e` ,

`=1

18

m
X
`=1

λk ê` ,

(37)

Pm

where the partition function is given by Zβ (λ) = tr e−β `=1 λ` E` . The parameters of the Hamiltonian
that we intend to learn are µ = arg minλ∈Rm :kλk≤1 L(λ). As before, we also define the empirical version of
this optimization by

µ̂ = arg min L̂(λ).

(38)

λ∈Rm :||λ||≤1

We prove later in Lemma 30 that log Zβ (λ) is a convex function in parameters λ and thus, the
optimization in (38) is a convex program whose solution can be in principle found. In this work,
we do not constraint ourselves with the running time of solving (38). We instead obtain sample
complexity bounds as formulated more formally in the next theorem.
Theorem 26 (Error in µ from error in marginals e` ). Let δ, α > 0. Suppose the marginals e` are
determined up to error δ, i.e., |e` − ê` | ≤ δ for all ` ∈ [m]. Additionally assume ∇2 log Z(λ)  α1 for
||λ|| ≤ 1. Then the optimal solution to the program (38) satisfies
√
2β mδ
||µ − µ̂||2 ≤
α
Proof. From the definition of µ̂ as the optimal solution of L̂ in (38), we see that L̂(µ̂) ≤ L̂(µ). Thus,
we get
log Zβ (µ̂) + β ·

m
X
`=1

µ̂` ê` ≤ log Zβ (µ) + β ·

m
X

µ` ê` .

`=1

or equivalently,
log Zβ (µ̂) ≤ log Zβ (µ) + β ·

m
X
`=1

(µ` − µ̂` )ê` .

(39)

∂
We show later in Lemma 29 that for every ` ∈ [m], we have ∂µ
log Zβ (µ) = −βe` .6 This along with
`
the assumption ∇2 log Z(µ)  α1 in the theorem statement, implies that for every µ0 with ||µ0 || ≤ 1
m
X
1
2
log Zβ (µ ) ≥ log Zβ (µ) − β ·
(µ0` − µ` )e` + α||µ0 − µ||2 .
2
0

`=1

Hence, by choosing µ0 = µ̂ and combining (40) and (39), we get
log Zβ (µ) − β ·

m
X
`=1

m

X
1
(µ̂` − µ` )e` + α||µ̂ − µ||22 ≤ log Zβ (µ) + β ·
(µ` − µ̂` )ê`
2
`=1

which further implies that
m

X
1
α||µ̂ − µ||22 ≤ β ·
(µ̂` − µ` )(e` − ê` ),
2
`=1

≤ β · ||µ̂ − µ||2 · ||ê − e||2 .
6

∂
In particular, see Eq. (44), where we showed ∂µ
log Zβ (µ) = −β · tr[E` ρβ (µ)] = −βe` .
`

19

(40)

Hence, we have
√
2β
2β mδ
||ê − e||2 ≤
.
α
α

||µ̂ − µ||2 ≤

t
u
Corollary 27 (Sample complexity from strong convexity). Under the same conditions as in Theorem 26, the number of copies of the Gibbs state ρβ that suffice to solve the Hamiltonian Learning Problem is
!
β 2 2O(κ)
m log m .
N =O
α 2 ε2
Proof. First observe that, using Theorem 26, as long as the error in estimating the marginals e` are
δ≤

αε
√ ,
2β m

(41)

we estimate the coefficients µ by µ̂ such that ||µ̂ − µ||2 ≤ ε. The marginals e` can be estimated in
various ways. One method considered in [CW20, BMBO19] is to group the operators E` into sets
of mutually commuting observables and simultaneously measure them at once. Alternatively, we
can use the recent procedure in [HKP20, Theorem 1] based on a variant of shadow tomography. In
either case, the number of copies of the state needed to find all the marginals with accuracy δ is
!
2O(κ)
N =O
log m ,
δ2
where recall that κ is the locality of the Hamiltonian. Plugging in Eq. (41) gives us the final bound
!
β 2 2O(κ)
N =O
m log m .
α 2 ε2
t
u

6

Strong convexity of log Zβ (λ)

We now state our main theorem which proves the strong convexity of the logarithm
P of the partition
function. Recall that for a vector λ = (λ1 , . . . , λm ) ∈ Rm , Hamiltonian H(λ) = i λi Ei where Ei
are tensor product of Pauli operators with weight at most κ and ρβ (λ) = Zβ1(λ) e−βH(λ) , we defined
the partition function as Zβ (λ) = tr(e−βH(λ) ). We now prove our main theorem for this section.
P
Theorem 28 (Restatement of Theorem 6: log Z(λ) is strongly convex). Let H = m
`=1 µ` E` be a
κ-local Hamiltonian over a finite dimensional lattice. For a given inverse-temperature β, there are constants
c, c0 > 3 depending on the geometric properties of the lattice such that
0

2

−O(β c )

∇ log Zβ (µ)  e

βc
·
· 1,
m
0

(42)
c

i.e., for every vector v ∈ Rm we have v T · ∇2 log Zβ (µ) · v ≥ β c e−O(β ) /m · ||v||22 .
20

The proof of Theorem 28 is divided into multiple lemmas that we state and prove both in this
and the following sections. We begin with finding an expression for the Hessian of log Zβ (λ).
P
Lemma 29. For every vector v ∈ Rm , define the local operator Wv = m
i=1 vi Ei (for notational convenience,
2
later on we stop subscripting W by v). The Hessian ∇ log Zβ (λ) satisfies
i

2
β 2 h
v > · ∇2 log Zβ (λ) · v =
tr Wv , ΦH(λ) (Wv ) ρβ (λ) − β 2 tr [Wv ρβ (λ)] ,
2

(43)

Proof. Since the terms in the Hamiltonian are non-commuting, we use Proposition 20 to find the
derivatives of log Zβ (λ). We get

o
∂
1
β n −βH(λ)
log Zβ (λ) =
tr −
e
, ΦH(λ) (Ej )
∂λj
Zβ (λ)
2


Z ∞
−β
−iH(λ)t
iH(λ)t
−βH(λ)
dtfβ (t)e
Ej e
=
tr e
Zβ (λ)
−∞
"
#
e−βH(λ)
= −β tr Ej
,
(44)
Zβ (λ)
where the second
R ∞ equality used the definition of the quantum belief propagation operator
ΦH(λ) (Ej ) = −∞ dtfβ (t) e−iH(λ)t Ej eiH(λ)t with fβ as given in Definition 19. The third equality used the fact that eiH(λ)t commutes with e−βH(λ) . Similarly, we have
"
!#
∂2
e−βH(λ)
∂
log Zβ (λ) = −β tr Ej ·
∂λk ∂λj
∂λk
Zβ (λ)
"
#


e−βH(λ)
1
∂  −βH(λ) 
∂
1
+ βtr Ej ·
= −β tr Ej ·
e
Zβ (λ)
·
Zβ (λ) ∂λk
Zβ (λ)
Zβ (λ) ∂λk


β2 
tr Ej · ρβ (λ), ΦH(λ) (Ek ) − β 2 tr[Ek ρβ (λ)] tr[Ej ρβ (λ)]
2

β 2 
=
tr Ej , ΦH(λ) (Ek ) · ρβ (λ) − β 2 tr[Ek ρβ (λ)] tr[Ej ρβ (λ)].
2
=

One can see from this equation that ∇2 log Zβ (H) is a symmetric real matrix, 7 and hence its eigenvectors have real entries. Finally, we get
X

v > · ∇2 log Zβ (λ) · v =
vj vk
=

j,k
β2

2

∂2
log Zβ (λ)
∂λk ∂λj

(45)

h
i
2
tr Wv , ΦH(λ) (Wv ) ρβ (λ) − βtr [Wv ρβ (λ)] .
t
u

7

The terms tr[Ek ρβ (λ)] and tr[Ej ρβ (λ)] are real, being expectations of Hermitian matrices.
Moreover,
E
is a Hermitian
operator,
being
an
anti-commutator
of
two
Hermitian
operators.
Hence
j , ΦH(λ) (Ek )

tr Ej , ΦH(λ) (Ek ) ρβ (λ) is real too.



21

The statement of Lemma 29 does not make it clear that the Hessian is a variance of a suitable
operator, or even is positive. The following lemma shows how to lower bound the Hessian by a
variance of a quasi-local operator. The intuition for the proof arises by writing the Hessian in a
manner that makes its positivity clear. This in particular, shows that log Zβ (µ) is a convex function
in parameters µ – we later improve this to being strongly convex.
P
Lemma 30 (A lower bound on ∇2 log Zβ (λ)
(λ)). For every v ∈ Rm and local operator Wv = i vi Ei ,
f such that
define another local operator W
Z ∞
f
fβ (t) e−iHt W eiHt dt,
(46)
Wv =
−∞

where
fβ (t) =

2
eπ|t|/β + 1
log π|t|/β
βπ
e
−1

(47)

4 −π|t|/β
e
for large t. We claim
is defined such that fβ (t) scales as βπ

i
h
i  h
i2
2
1 h
fv )2 ρβ (λ) − tr W
fv ρβ (λ)
tr Wv , ΦH(λ) (Wv ) ρβ (λ) − tr [Wv ρβ (λ)] ≥ tr (W
2

(48)

Remark 31. For the rest of the paper, we are going to fix an arbitrary v ∈ Rm , in order to avoid subscripting
f by v.
W, W
Proof of Lemma 30. Let us start by proving a simpler version of Eq. (48), where we only show
i
2
1 h
tr W, ΦH(λ) (W ) ρβ (λ) − tr [W ρβ (λ)] ≥ 0.
(49)
2
Since v is an arbitrary vector, this shows that, as expected, ∇2 log Zβ (λ) is a positive semidefinite
operator.
P
Consider the spectral decomposition of the Gibbs state ρβ (λ): ρβ (λ) =
j rj (λ)|jihj|. Then
observe that
i
2
1 h
tr W, ΦH(λ) (W ) ρβ (λ) − tr [W ρβ (λ)]
(50)
2

2
X
1X
=
rj (λ)hj|{W, ΦH (W )}|ji − 
rj (λ)Wj,j 
2
j
j

2
X

1X
rj (λ)Wj,j 
=
rj (λ) Wj,k hk|ΦH (W )|ji + hj|ΦH (W )|kiWk,j − 
2
j
j,k

2


X
X
(1) 1
=
rj (λ) Wj,k Wk,j f˜β (Ek − Ej ) + Wj,k Wk,j f˜β (Ej − Ek ) − 
rj (λ)Wj,j 
2
j
j,k

2
X
(2) X
=
rj (λ)|Wj,k |2 f˜β (|Ej − Ek |) − 
rj (λ)Wj,j  .
(51)
j,k

j

22

In equality (1), we use Definition 19 and in equality (2) we use the facts that W is Hermitian and
f˜β (t) = f˜β (−t). Since f˜β (0) = 1 and f˜β (t) > 0 for all t, it is now evident from last equation that

tr

1
{W, ΦH (W )}ρβ
2



2


− tr (W ρβ )2 ≥

X
j

rj (λ)|Wj,j |2 − 

X
j

rj (λ)Wj,j  ≥ 0.

f in (46). The function fβ (t) in (46) is chosen
We can improve this bound by using the operator W
˜
carefully such that its Fourier transform satisfies fβ (ω) = f˜β (|ω|). Then, we have that
Z ∞
X
f=
W
fβ (t) e−iHt W eiHt dt =
|jihk| Wj,k f˜β (|Ej − Ek |).
(52)
−∞

j,k

Similar to (51) we get
f 2 ρβ (λ)) − [tr(W
f ρβ (λ))]2 =
tr(W

X
j,k


2
X
rj (λ)|Wj,k |2 f˜β (|Ej − Ek |)2 − 
rj (λ)Wj,j 
j

2


≤

X
j,k

rj (λ)|Wj,k |2 f˜β (|Ej − Ek |) − 


= tr

{W, ΦH (W )}
2

X

rj (λ)Wj,j 

j



ρβ (λ) − [tr(W ρβ (λ))]2 ,

(53)

where the inequality is derived from f˜β (x)2 ≤ f˜β (x) for arbitrary −∞ < x < ∞. Thus, we get
m
X
i=1

∂
vi
∂λi

!2
f 2 ρβ (λ)) − tr(W
f ρβ (λ))2 .
log Zβ (λ) ≥ tr(W
t
u

7

Lower bound on the variance of quasi-local operators

In the previous section, we showed how to give a lower bound on the Hessian of the logarithm of
the partition
for a vector λ = (λ1 , . . . , λm ) ∈ Rm with kλk ≤ 1, Hamiltonian
P function. To be precise,
1
−βH(λ)
(where Zβ (λ) = tr(e−βH(λ) )), we showed in Lemma 30
H(λ) = i λi Ei and ρβ (λ) = Zβ (λ) e
f such that for every v, we have
how to carefully choose a local operator W

f ].
v > · ∇2 log Zβ (λ) · v ≥ β 2 Var[W

(54)

f with respect to ρβ (λ) can be bounded from
In this section, we further prove that the variance of W
below by a large enough quantity. Before looking at the highly non-trivial case of finite temperature, lets look at a simpler case of infinite temperature limit.

23

Theorem 32
Variance at finite temperature
Claims 37 and 38
Variance of locally rotated operator at finite temperature
Subsection 7.4, Equation (93)
Variance of operator with small support at finite temperature
Claim 36
Lemma 34
Variance of operator with small support at infinite temperature
Claim 44
Theorem 32
Variance of operator with small support at infinite temperature
Figure 1: Flow of the argument in the proof of Theorem 33.

7.1

Warm-up: Variance at infinite temperature

1Λ
. We have the
Consider the infinite temperature state (i.e., the maximally mixed state) η = D
Λ
following theorem, where we assume that the locality of W , namely κ = O(1).

f as defined in Lemma 30, we have
Theorem 32. For W
m

f )2 η] − tr[W
f η]2 ≥
tr[(W

X
Ω(1)
vi2 .
2
(β log(m) + 1)

(55)

i=1

f is replaced by W ,
The intuition behind the theorem is as follows. In the above statement, if W
then the lower bound is immediate (see Eq. (56) below). Similarly, if H and W were commuting,
f would be the same as W and the statement would follow. In order to show (55) for W
f in
then W
general, we expand it in the energy basis of the Hamiltonian and use the locality of W to bound
the contribution of cross terms (using Lemma 21). This accounts for the contributions arising due
to non-commutativity of W and H.
P
f η] = tr[W η] =
Proof of Theorem 32. Recall from Lemma 30 that W = i vi Ei . We first note that tr[W

24

f )2 k2 . To begin with, we observe
f )2 η] = 1 k(W
0. From the definition, we have tr[(W
F
DΛ
kW k2F = DΛ

m
X

vi2 ,

(56)

i=1

which holds since the basis Ei satisfies kEi k2F = DΛ and tr[Ei Ej ] = 0 if i 6= j. Define PsH as the
projection onto the energy range (s, s + 1] of H.
X
|jihj|.
(57)
PsH :=
j:Ej ∈(s,s+1]

Using the identity

H
f
s Ps = 1Λ and the definition of W , let us expand

P

kW k2F =
f k2F =
kW

∞
X
s,s0 =−∞
∞
X
s,s0 =−∞

kPsH0 W PsH k2F ,
Z ∞
−∞

2

dtPsH0 fβ (t)e−iHt W eiHt PsH

(58)
F
2

=

∞
X

X

s,s0 =−∞

j:Ej ∈(s,s+1]
k:Ek ∈(s,s+1]

Wj,k f˜β (|Ej − Ek |)PsH0 |jihk|PsH

.

(59)

F

By using the inequality
1
tanh(βω/2)
≥ β
,
f˜β (ω) =
βω/2
|ω| + 1
2

we have
2

X
j:Ej ∈(s,s+1]
k:Ek ∈(s,s+1]

Wj,k f˜β (|Ej − Ek |)PsH0 |jihk|PsH

X

=

F

X

j:Ej ∈(s,s+1] k:Ej ∈(s0 ,s0 +1]

[f˜β (|Ej − Ek |)]2 |Wj,k |2

1

X
X
|Wj,k |2 =
2
0 | + 1) + 1
(|s
−
s
j:Ej ∈(s,s+1] k:Ej ∈(s0 ,s0 +1]
2

≥ β

kPsH0 W PsH k2F

2
β
0
2 (|s − s | + 1) + 1

.

(60)

f k2 :
Plugging this lower bound in Eq. (59) gives the following lower bound for kW
F
f k2F ≥
kW

∞
X
s,s0 =−∞

∞
X

H
H
∞
X
kP(s
W P(s
k2
0 +s1 )/2
0 −s1 )/2 F
,
2 =
2
β
β
0
s0 =−∞ s1 =−∞
2 (|s − s | + 1) + 1
2 (|s1 | + 1) + 1

kPsH0 W PsH k2F

25

(61)

where we have introduced s0 = s + s0 , s1 = s − s0 . Let us consider the last expression for a fixed s0 ,
introducing a cut-off parameter s̄ which we fix eventually:
H
H
∞
X
kP(s
W P(s
k2
0 +s1 )/2
0 −s1 )/2 F

[ β2 (|s1 | + 1) + 1]2


X
1
H
H
k2 
W P(s
kP(s
≥ β
2 
0 −s1 )/2 F
0 +s1 )/2
|s1 |≤s̄
2 (s̄ + 1) + 1


∞
X
X
1
H
H
H
H
k2  .
W P(s
kP(s
= β
k2 −
W P(s
kP(s
2 
0 −s1 )/2 F
0 +s1 )/2
0 −s1 )/2 F
0 +s1 )/2
s1 =−∞
|s1 |>s̄
2 (s̄ + 1) + 1
s1 =−∞

(62)

By combining the inequalities (61) and (62), we obtain
f k2F ≥
kW

kW k2F

∞
X

1

X
H
H
kP(s
W P(s
k2 .

2
0 +s1 )/2
0 −s1 )/2 F
β
(s̄
+
1)
+
1
s0 =−∞ |s1 |>s̄
2

2 −
β
2 (s̄ + 1) + 1

(63)

H
H
Now, we will estimate the second term in (63). Since the subspaces P(s
and P(s
are
0 +s1 )/2
0 −s1 )/2
sufficiently far apart in energy, we can use the exponentialP
concentration on the spectrum [AKL16]
(as stated in Lemma 21) to obtain the following: for W = i vi Ei , we have
H
H
kP(s
W P(s
k≤
0 +s1 )/2
0 −s1 )/2

m
X
i=1

H
vi kP(s
E PH
k
0 +s1 )/2 i (s0 −s1 )/2

−λ(|s1 |−1−κ)

≤ Ce

m
X
i=1

(64)
−λ(|s1 |−1−κ)

|vi | ≤ Cme

max |vi |.
i

where we use the condition that Ei are tensor product of Pauli operators with weight at most κ,
and the parameters C and λ are O(1) constants (see Lemma 21 for their explicit forms). Then, the
second term in (63) can be upper-bounded by
∞
X

X

s0 =−∞ |s1 |>s̄
(1)

≤
(2)

≤

∞
X

H
H
kP(s
W P(s
k2
0 +s1 )/2
0 −s1 )/2 F

X

s0 =−∞ |s1 |>s̄
∞
X

X

|s1 |>s̄ s0 =−∞

H
H
H
kP(s
W P(s
k2 · kP(s
k2
0 +s1 )/2
0 −s1 )/2
0 +s1 )/2 F
H
kP(s
k2 · C 2 m2 e−2λ(|s1 |−1−κ) max vi2
0 +s1 )/2 F
i

= DΛ C 2 m2 e2λ(1+κ) max vi2
i

(3)

≤ DΛ max vi2
i

X
|s1 |≥s̄+1

C 2 m2 e2λ(κ+1)
λ

e−2λ|s1 |

C 2 m2 e2λ(κ+1) −2λs̄
e−2λs̄ ≤ DΛ
e
λ
(4)

26

!
X
i

vi2

,

(65)

where inequality (1) follows
Eq. (16), (2) follows from Eq. (64), (3) follows from Fact 12 and
Pfrom
2
2
(4) follows from maxi vi ≤ i vi . Therefore, by applying Eq. (56) and (65) to (63), we arrive at the
lower bound as
!
!
m
2 m2 e2λ(κ+1)
X
D
C
Λ
f k2F ≥
kW
vi2
1−
e−2λs̄ .
(66)
[β(s̄ + 1)/2 + 1]2
λ
i=1

Since λ, C, κ = O(1), by choosing s̄ = O(log(m)), we obtain the main inequality (55). This completes the proof. 
t
u

7.2

Variance at finite temperature

Next, we show how to prove a variance lower bound at finite temperature. This is achieved by
the following general theorem on the variance of arbitrary local operator, which will reduce the
problem to estimating a “variance-like” quantity at the infinite temperature case (observe the occurrence of the maximally mixed state η in the theorem below).
−βH

e
Theorem 33. Let β > 0, H be a κ-local Hamiltonian on the lattice Λ and ρβ = tr(e
−βH ) . Let A be a
(τ, a1 , a2 , 1)-quasi-local operator (see Eq. (19)) where a2 = O(1/β), a1 = O(1) are constants and Z are
restricted to be connected sets within Λ. Suppose tr[Aρβ ] = 0 and τ ≤ 1. We have
2

2

hA i = tr(A ρβ ) ≥



β Ω(1)

max tr[A2(i) η]
i∈Λ

.

We remark that the theorem statement above hides several terms that depend on the lattice,
such as the lattice dimension, the degree of the graph and the locality of Hamiltonian (which we
have fixed to be a constant). Additionally, the assumptions a2 = O(1/β), a1 = O(1) are made in
order to show that an operator A∗ to which we apply the theorem, satisfies the assumptions of the
theorem.8 Before proving the theorem, we first discuss how to use this theorem in order to prove
a lower bound on the Hessian of log Z(λ).
P
f be the operators defined in Lemma 30. In
For an arbitrary v ∈ Rm , let W = i vi Ei and W

f is a 1/D, O(1), O(1/β), c∗ β 2D+1 (maxi∈Λ |vi |) -quasi-local operator,
Appendix D we show that W
for c∗ = O(1). Thus, the following operator
A∗ =

β −2D−1
f − tr[ρβ W
f ]1),
(W
c∗ maxi∈Λ |vi |

is (O(1), O(1), O(1/β), 1)-quasi-local and satisfies tr[Aρβ ] = 0. We now apply Theorem 33 to the
operator A∗ to prove Theorem 28. We need to estimate maxi tr[A∗2
(i) η]. Consider
max tr[(A∗(i) )2 η] =
i

β −4D−2
c2∗ (maxi∈Λ |vi |)2



2
f
max tr[(W(i) ) η] .
i

The following lemma is shown in Appendix E.
8

We remark that we can also apply the theorem for other choices of a1 , a2 , with small modifications to the proof.

27

Lemma 34. It holds that
f(i) )2 η]) =
max(tr[(W
i∈Λ

Ω(1)
(β log(β) + 1)



2
max vi .
2D+2
i∈Λ

This implies
max tr[(A∗(i) )2 η] =
i

Ω(1)
β 4D+2 (β log(β) + 1)2D+2 (maxi∈Λ |vi |)



2
max vi =
2
i∈Λ

1
β Ω(1)

.

Using this lower bound in Theorem 33, we find
2 

2

4D+2 (max
i∈Λ |vi |)
∗ 2
∗ 2
f )2 i − hW
fi = β
h(W
h(A
)
i
−
(hA
i)
c2∗

2 
β Ω(1)
Ω(1)
∗ 2
max |vi | · max tr[(A(i) ) η]
=β
i

i∈Λ

= β Ω(1) ·


β

β O(1) 
2
1
· max |vi |
O(1)
i∈Λ


2
O(1)
e−β
O(1)
(1) Ω(1)
=β
· e−β
max |vi | ≥ β Ω(1) ·
i∈Λ
m

!
X

vi2

,

i

where we used β −O(1) ≥ e−β in (1). Putting together the bound above with Eq. (54), we find that
for every v ∈ Rm ,
m
−β O(1) X

f ] ≥ β Ω(1) · e
v > · ∇2 log Zβ (λ) · v ≥ β 2 Var[W
vi2 .
m
i=1

This establishes Theorem 28.

7.3

Some key quantities in the proof and proof sketch

We now prove Theorem 33. For notational simplicity, let
H 0 := H −

1
log Zβ ,
β

(67)

0

which allows us to write ρβ = e−βH . We will interchangeably use the frobenius norm to write
√
hA2 i = tr(A2 ρβ ) = kA ρβ kF . We now define the projection operator PγA as follows (see Figure 2):
PγA :=

X

Πω ,

(68)

ω∈[−γ,γ]

where Πω is the projector onto the eigenspace of A with eigenvalue ω. We then define δγ by
√
δγ := 1 − kPγA ρβ k2F .

28

(69)

Probability distribution

2
PA

hAi = 0

A

Figure 2: Plot of the probability distribution tr[Πω ρβ ], where Πω is the projector onto the eigenvectors of A with eigenvalue ω. It is assumed that tr[Aρβ ] = 0. For a γ to be chosen in the proof, PγA
is the projector onto the subspace of eigenvectors of A with eigenvalue between [−γ, γ]. A lower
bound on the variance of A follows if we can show that for a constant γ, the probability mass in
the colored range is small (see Equation 70).
Using δγ , observe that we can lower bound hA2 i as
X
X
X
hA2 i =
ω 2 hω|ρβ |ωi ≥
ω 2 hω|ρβ |ωi ≥ γ 2
hω|ρβ |ωi ≥ γ 2 δγ .
ω

|ω|≥γ

|ω|≥γ

(70)

A
Let QA
γ = 1 − Pγ , then observe that from Eq. (69) that

√
√
√
2
kPγA ρβ − ρβ k2F = kQA
γ ρβ kF = δγ .

(71)

The proof is divided into the following subsections, each of which may be of independent interest on its own.

7.4

Reducing the global problem to a local problem

A main challenge in bounding the variance of the operator A is that it is a global operator and
its properties may scale badly with the system size. But since it is a linear combination of local
operators, it is related to operators supported in a local region by a simple linear transform. To this
end, recall the definition of A(i) (the local operator which includes essentially the terms in A that
have support on the ith site) from the subsection 5.5. Using Haar random unitaries, we obtain the
integral representation of A(i) as
Z
1
A(i) = A − [tri (A)] ⊗ 1i = A − dµ(Ui )Ui† AUi ,
(72)
d
where µ(Ui ) is the Haar measure for unitary operator Ui which acts on the ith site. Since the A(i)
is obtained from a quasi-local A, it is quasi-local itself. Next claim will approximate A(i) by a local
operator.

29

Claim 35. For an integer R, let Xi be the radius-R ball around the site i, i.e., Xi = B(R, i). There exists
an operator AXi supported entirely on Xi , such that
1

τ
a2
4
τ
kA(i) − AXi k ≤ 2a1 ·
· e− 2 (R) .
2
a2 τ
Proof. Using the representation of A in Theorem 33 and the fact that local operators not containing i
in their support are removed, we can write


X
1
A(i) =
gk aZ − [tri (aZ )] ⊗ 1i ,
d
k,Z⊆Λ:
|Z|≤k,Z3i

Define
X

AXi =

k,Z⊆Xi :
|Z|≤k,Z3i



1
gk aZ − [tri (aZ )] ⊗ 1i .
d

be the desired approximations of A(i) by removing all operators that are not contained in Xi . Observe that
X
X
(1)
kA(i) − AXi k ≤ 2
gk kaZ k ≤ 2
gk kaZ k
k,Z⊆Λ:
Z6⊂Xi ,|Z|≤k,Z3i

(2)

≤2

k,Z⊆Λ:
diam(Z)≥R,|Z|≤k,Z3i

!
X

X

gk

Z:Z3i

k≥R

≤ 2ζa1

X
k≥R

e

−a2 kτ

kaZ k

(3)

≤ 2ζ

X

gk

k≥R

(4)

−1
≤ 2ζa1 · a2 τ ·

 2
2 τ − a2 (R)τ
·e 2
.
τ

(73)

For inequality (1), note that since Z 6⊂ Xi and Z 3 i, the diameter of Z (recall that Z is a ball)
must be larger than the radius of Xi , which is R. Inequality (2) holds since k ≥ |Z| ≥ diam(Z),
inequality (3) uses Definition 14 and inequality (4) uses Fact 12. Since ζ = 1 for the given A (see
the statement of Theorem 33), this completes the proof.
t
u
We now define i0 as

√
i0 := arg max kAi ηkF .

(74)

i

The set of unitaries Ui0 and the Haar measure µ(Ui0 ) are defined analogously. Plugging in

1
τ
1
2
8 · 4 τ · a1


R=
log 2
1
√
a2
τ τ · a τ kA
ηk
2

(i0 )

F

in Claim 35 we get
1
√
kA(i0 ) − AXi0 k ≤ kA(i0 ) ηkF
(75)
4
Substituting a2 = O(1/β), a1 = O(1), τ = O(1), we find that we can ensure the condition (75) for


Ω(1)
1
.
(76)
R = diam(Xi0 ) = β log
√
kA(i0 ) ηkF
30

7.5

Variance of operators with small support: finite temperature to infinite temperature

Having related A to the operator A(i0 ) (which is essentially supported on a small number of sites
in the lattice, up to a tail decaying sub-exponentially in the radius), we now argue that it is simpler
to bound the variance of A(i0 ) in terms of its variance at infinite temperature, as long as some local
rotations are allowed. In particular, we will show the existence of a unitary Ui0 for which we can
proceed in this fashion. The intuition here is that if rotations are allowed, then the eigenvectors of
AXi0 can be rearranged to yield largest possible variance with ρβ . This turns out to be larger than
the variance with η. To make this precise, we prove the following claim.
Claim 36. There exists UXi0 such that
1
√
√
√
†
kUX
A(i0 ) UXi0 ρβ kF ≥ kA(i0 ) ηkF − 2kAXi0 − A(i0 ) k ≥ kA(i0 ) ηkF ,
i0
2
where the second inequality uses Eq. (75).
Proof of Claim 36. Recall that the goal is to show the existence of a unitary UXi0 satisfying
√
√
†
kUX
A(i0 ) UXi0 ρβ kF ≥ kA(i0 ) ηkF − 2kAXi0 − A(i0 ) k.
i
0

(77)

We start from the following,

√
√
†
† 
A(i0 ) UXi0 ρβ kF = kUX
(A(i0 ) − AXi0 ) + AXi0 UXi0 ρβ kF
kUX
i0
i0
√
†
AXi0 UXi0 ρβ kF − kA(i0 ) − AXi0 k
≥ kUX
i
0

(78)

√
†
and lower-bound the norm of kUX
AXi0 UXi0 ρβ kF . For this, define
i
0

ρβ,X := trX c (ρβ ),

(79)

where trX c is the partial trace operation for the Hilbert space on X c . We define the spectral decomposition of AXi0 as
DXi

AXi0 =

X0
s=1

εs |εs ihεs |,

(80)

where εs is ordered as |ε1 | ≥ |ε2 | ≥ |ε3 | ≥ · · · and DXi0 is the dimension of the Hilbert space
on Xi0 . Additionally, define the spectral decomposition of ρβ,Xi0 as
DXi

ρβ,Xi0 =

X0
s=1

ps |µs ihµs |,

(81)

where ps is ordered as p1 ≥ p2 ≥ p3 ≥ · · · and |µs i is the sth eigenstate of ρβ,Xi0 . We now choose
the unitary operator UXi0 such that
UXi0 |µs i = |εs i

for s = 1, 2, . . . , DXi0
31

(82)

We then obtain
D Xi
†
UXi0 ρβ,Xi0 UX
=
i0

X0
s=1

ps |εs ihεs |.

(83)

This implies
√
†
†
kUX
AXi0 UXi0 ρβ k2F = tr[UX
A2Xi UXi0 ρβ ]
i
i
0

0

0

†
†
= tr[A2Xi UXi0 ρβ UX
] = trXi0 [A2Xi UXi0 ρβ,Xi0 UX
]
i0
i0
0
0
DXi

=

X0
s=1

ps ε2s ≥

1
DXi0

DXi

X0
s=1

√
ε2s = kAXi0 ηk2F ,

(84)

where the inequality
used the fact that ps , εs are given in descending order. Then, the minimization
P
problem of s ps εs for ps s with the constraint p1 ≥ p2 ≥ p3 ≥ · · · has a solution of p1 = p2 = · · · =
pDXi . Using the lower bound
0

√
√
√
kAXi0 ηkF = k(AXi0 − A(i0 ) + A(i0 ) ) ηkF ≥ kA(i0 ) ηkF − kAXi0 − A(i0 ) k,

(85)

we can reduce inequality (84) to
√
√
†
AXi0 UXi0 ρβ kF ≥ kA(i0 ) ηkF − kAXi0 − A(i0 ) k.
kUX
i
0

(86)

By combining the inequalities (78) and (86), we obtain
√
√
†
†
kUX
A(i0 ) UXi0 ρβ kF ≥ kUX
AXi0 UXi0 ρβ kF − kA(i0 ) − AXi0 k
i0
i0
√
†
AXi0 UXi0 ρβ kF − 2kA(i0 ) − AXi0 k
≥ kUX
i
0

t
u

which proves the claimed statement.

7.6

Invariance under local unitaries

Recall that we reduced the problem of variance of A to that of the operator A(i0 ) that is essentially supported on small number of sites. But in the process, we introduced several local unitaries
(c.f. previous subsections). In order to handle the action of these unitaries, we will use two claims
which show that local unitaries do not make much difference in the relative behavior of spectra of
A and H 0 . To elaborate, consider any local operator UX acting on constant number of sites X on
†
the state ρβ . It is expected that the quantum state UX
ρβ UX has “similar” spectral properties as ρβ .
So if the eigen-spectrum of the operator A is strongly concentrated for ρβ , one would expect this
†
behavior to hold even for UX
ρβ UX . We make this intuition rigorous in the following claim.
Claim 37. Let c1 , c2 , λ be universal constants. Let X ⊆ Λ. For every unitary UX supported on X, we have
2
 c2c+β
√
2
ρ
k
≤
exp
λ|X|
δγ
.
kQA
U
β F
γ X

32

(87)

Let us see a simple application of the claim. It allows us to control the variance of A even after
local operations are applied to it. More precisely,
√
√
√
kAUX ρβ k2F = kAPγA UX ρβ k2F + kA(1 − PγA )UX ρβ k2F
(88)
√
≤ γ 2 + kAk2 · k(1 − PγA )UX ρβ k2F .
O(1)/β

By Claim 37, the expression on the second line is upper bounded by γ 2 + kAk2 eO(1)|X| δγ
. This
√
upper bound on kAUX ρβ kF suffices to provide an inverse-polynomial lower bound on the variance
of A2 , since we can lower bound δγ for an appropriate choice of γ. However we now show how one
can polynomially improve upon this upper bound (thereby the lower bound on variance) using the
following claim. This claim, along the lines of Claim 37, also shows that local unitaries UX do not
change the desired expectation values.
Claim 38. Let X ⊆ Λ. For every unitary UX supported on X, we have9

1
2
√
AQA
· exp O(1) · |X| δγO(1)/β + O(1) · |X|6 · hA2 i.
γ UX ρβ F ≤
γ

(89)

Proof of both the Claims 37, 38 appear in Section 7.8. An immediate corollary of this claim is
the following, that improves upon Eq. (88).
Corollary 39. Let X be a subset of Λ of size |X| = O(1). For every unitary UX supported on X, we have
O(1)/β

eO(1)·|X| δγ
√
kAUX ρβ k2F ≤ γ 2 +
+ O(1)|X|6 hA2 i.
γ
√
Proof. Similar to Eq. (88), we upper bound kAUX ρβ k2F as
2
2
2
√
√
√
√
A
2
kAUX ρβ k2F = APγA UX ρβ F + AQA
γ UX ρβ F ≤ γ + AQγ UX ρβ F ,
A
since QA
γ = 1 − Pγ . By combining this with Claim 38, the corollary follows.

7.7

(90)

(91)
t
u

Proof of the Theorem 33

We are now ready to prove the main theorem statement. The main idea of the proof is the following:
if the spectrum of A is strongly concentrated for the Gibbs state ρβ , the concentration can be proven
to be protected to arbitrary local unitary operations (see Claims 37 and 38). On the other hand,
by choosing local unitary operations appropriately, we can relate the variance of the operator A
(rotated by certain local unitary Ui0 on the site i0 ) to the variance of the operator A(i0 ) and hence
give a good lower bound to the variance (see Claim 36). Combining the two results allows us to
lower bound the variance of A and hence prohibits the strong spectral concentration of the operator
A. We formally prove this now.
Proof. Let UXi0 be the unitary as chosen in Claim 36. Using Eq. (72), we obtain the following ex†
pression for UX
A(i0 ) UXi0
i
0

†
†
UX
A(i0 ) UXi0 = UX
AUXi0 −
i
i
0

9

0

Z

†
dµ(Ui0 )UX
Ui†0 AUi0 UXi0 .
i
0

Explicit O(1) constants that appear in this inequality are made clear in the proof.

33

(92)

Using triangle inequality, we have
√
√
†
†
kUX
A(i0 ) UXi0 ρβ kF ≤ kUX
AUXi0 ρβ kF +
i0
i0
√
= kAUXi0 ρβ kF +

Z

Z

√
†
Ui†0 AUi0 UXi0 ρβ kF
dµ(Ui0 )kUX
i
0

√
dµ(Ui0 )kAUi0 UXi0 ρβ kF

(93)

This implies
Z

2
√
dµ(Ui0 )kAUi0 UXi0 ρβ kF
Z
2
√
√
dµ(Ui0 )kAUi0 UXi0 ρβ kF .
≤ 2kAUXi0 ρβ k2F + 2


√
√
†
2
kUX
A
U
ρ
k
≤
kAUXi0 ρβ kF +
β F
(i0 ) Xi0
i
0

Now, we can use Corollary 39 to obtain the upper bound
O(1)/β

eO(1)|Xi0 | δγ
√
†
2
2
A
U
kUX
ρ
k
≤
4γ
+
β F
(i0 ) Xi0
i0
γ

+ O(1)|Xi0 |6 hA2 i.

(94)

Using Claim 36, we have
1
√
√
†
A(i0 ) UXi0 ρβ kF ≥ kA(i0 ) ηkF .
kUX
i0
2

(95)

Putting together the upper bound in Eq. (94) and the lower bound in Eq. (95), we have
O(1)/β

eO(1)|Xi0 | δγ
1
√
+ O(1)|Xi0 |6 hA2 i ≥ kA(i0 ) ηk2F .
γ
4
√
By choosing as γ 2 = kA(i0 ) ηk2F /32 =: γ02 , we obtain
4γ 2 +

(96)

O(1)/β

eO(1)|Xi0 | δγ0
γ0

+ O(1)|Xi0 |6 hA2 i ≥ γ02 .

(97)

This inequality implies that either
β·O(1)

δγ0 ≥ γ03 e−O(1)|Xi0 |
or
hA2 i ≥
Combining with Eq. (70), we conclude that

Ω(1)γ02
.
|Xi0 |6

n

β·O(1) Ω(1)γ 2 o
0
hA2 i ≥ min γ02 · γ03 e−O(1)|Xi0 |
,
.
|Xi0 |6
Eq. (76) ensures that
|Xi0 | = O(1)RD = β Ω(1) log
34



1
√

kA(i0 ) ηkF

Ω(1)

,

where we have used the assumption that lattice dimension D is O(1). Plugging in this expression
for |Xi0 | with the choice of γ0 , we find
√ Ω(1)
n
√ β·O(1) −βO(1)|Xi | Ω(1)kA(i0 ) ηkF o
2
2
0 ,
tr(A ρβ ) = hA i ≥ min kA(i0 ) ηkF
·e
|Xi0 |6
√ Ω(1) o
n
Ω(1)kA(i0 ) ηkF
√ β Ω(1)
≥ min kA(i0 ) ηkF , O(1)
β
log( kA 1√ηkF )O(1)
(i0 )
√
Ω(1)
n
√ β Ω(1) Ω(1)kA(i0 ) ηkF o
≥ min kA(i0 ) ηkF ,
β O(1)
√ β Ω(1)
≥ kA(i0 ) ηkF .
√
√
Since we chose i0 in Eq. (74) such that kA(i0 ) ηkF = maxi kA(i) ηkF , this proves the theorem. t
u

7.8

Proof of Claims 37 and 38

Proof of Claim 37. Recall that the goal is to show that for every X ⊆ Λ and arbitrary unitaries UX ,
c

2
√
2
λ|X| c2 +β
kQA
U
ρ
k
≤
c
e
δ
,
γ
1
X
β
γ
F

(98)

A
A
where QA
γ = 1 − Pγ and Pγ was defined in Eq. (68). To prove this inequality, we start from the
following expression:

√
2
kQA
γ UX ρβ kF =

X

H0 √
QA
ρβ
γ UX Pm

m∈Z

2

=
F

X

H
QA
γ UX Pm

0

√

ρβ

m∈Z

2

(99)

F

with
0

X

H
:=
Pm

j:Ej ∈(m,m+1]

|jihj|,

(100)

where
eigenvector of the Hamiltonian H 0 with Ej the corresponding eigenvalue. Note
P|ji is the
0
H = 1 and we have P H 0 = 0 for m ∈
that m∈Z Pm
/ [−kH 0 k, kH 0 k]. For some ∆ > 0 which we pick
m
2
H 0 √ρ
as a sum of the following quantities
later, we now decompose QA
β
γ UX Pm
F

H0

QA
γ UX Pm

√

ρβ

2

2

H0
H0
H0 √
= QA
ρβ ,
γ P>m+∆ + P<m−∆ + P[m−∆,m+∆] UX Pm
H0

F

(101)

F

where
0

H
:=
P>m+∆

X

0

H
Pm
0 ,

m0 >m+∆

0

H
:=
P<m+∆

0

X

H
Pm
0 ,

0

H
:=
P[m−∆,m+∆]

X

0

H
Pm
0 .

(102)

m−∆≤m0 ≤m+∆

m0 <m+∆

Summing over all m ∈ Z in Eq. (101) and using Eq. (99) followed by the triangle inequality gives
us the following inequality
√
2
kQA
γ UX ρβ kF
X
X
2
2

H0
H0 √
H0
H0
H0 √
≤2
QA
ρβ +2
QA
ρβ . (103)
γ P[m−∆,m+∆] UX Pm
γ P>m+∆ + P<m−∆ UX Pm
F
F
m∈Z
m∈Z
|
|
{z
}
{z
}
:=(1)

:=(2)

35

We first bound (1) in Eq. (103). Note that for every m,
0

H
H
QA
γ P[m−∆,m+∆] UX Pm

0

√

ρβ

2
F

H
≤ kPm

√

0

−βm

≤e

0

H
ρβ k2 · QA
γ P[m−∆,m+∆]
2

H0

QA
γ P[m−∆,m+∆]

F

2
F

(104)

,

where the first inequality used Eq. (16). The expression in the last line can be upper bounded as
h
i
2
−βm
A H0
H0
=
e
tr
Q
P
e−βm QA
P
γ [m−∆,m+∆]
γ [m−∆,m+∆]
F
h
i
H0
H0
≤ e−βm eβ(m+∆+1) tr QA
P
ρ
P
γ [m−∆,m+∆] β [m−∆,m+∆]
2
√
H0
= eβ(∆+1) QA
.
γ P[m−∆,m+∆] ρβ
F

where the inequality follows from
0

0

0

H
H
H
e−β(m+∆+1) P[m−∆,m+∆]
 P[m−∆,m+∆]
ρβ P[m−∆,m+∆]
.

Thus we conclude, from Equation 104, that
0

H
H
QA
γ P[m−∆,m+∆] UX Pm

0

√

2
√
H0
≤ eβ(∆+1) QA
γ P[m−∆,m+∆] ρβ
F
F
X
2
β(∆+1)
A H0 √
=e
Qγ Pm0 ρβ .
2

ρβ

F

m0 ∈[m−∆,m+∆]

So the first term (1) in Eq. (103) can be bounded by
X

0

H
H
QA
γ P[m−∆,m+∆] UX Pm

0

√

ρβ

m∈Z

2
F

≤ eβ(∆+1)
(1)

X

0

X

H
QA
γ Pm0

√

ρβ

m∈Z m0 ∈[m−∆,m+∆]

= eβ(∆+1) · 2∆

X

0

H
QA
γ Pm 0

m0

√

ρβ

2
F

2
F

2
√
β(∆+1)
δγ ,
= 2∆eβ(∆+1) QA
γ ρβ F = 2∆e

(105)

where Pin (1) we use the fact that each m0 appears 2∆ times in the summation
P
m∈Z
m0 ∈[m−∆,m+∆] .
We now move on to upper bound (2) in Eq. (103) as follows. We have
2

H0
H0
H0 √
QA
≤
ρβ
γ P>m+∆ + P<m−∆ UX Pm
F


H0
H0
H0
H0 √
P>m+∆
+ P<m−∆
UX Pm
· kPm
ρβ k2F ,

(106)

where we use kQA
γ k ≤ 1. Using Lemma 21, we obtain

H0
H0
H0
P>m+∆
+ P<m−∆
UX P m
≤ Ce−λ(∆−|X|) ,

(107)

where C and λ are universal constants. Plugging Eq. (107) into Eq. (106), we get
2

H0
H0
H0 √
H0 √
QA
ρβ
≤ Ce−λ(∆−|X|) kPm
ρβ k2F .
γ P>m+∆ + P<m−∆ UX Pm
F

36

(108)

With this, we can bound (2) in Eq. (103) by
X
m∈Z

X
2

H0
H0
H0 √
H0 √
QA
ρβ
≤
Ce−λ(∆−|X|) kPm
ρβ k2F = Ce−λ(∆−|X|) , (109)
γ P>m+∆ + P<m−∆ UX Pm
F

m∈Z

H 0 √ρ k2 = tr(ρ ) = 1. Putting together Eq. (105)
where the equality used the fact that m∈Z kPm
β F
β
and (109) into Eq. (103), we finally obtain the upper bound of

P

√
2
β(∆+1)
δγ + 2Ce−λ(∆−|X|) .
kQA
γ UX ρβ kF ≤ 4∆e

(110)

We let ∆ = cβ −1 log(1/δγ ), which gives
c2

√
2
λ|X| c2 +β
kQA
δγ
,
γ UX ρβ kF ≤ c1 e

(111)
t
u

for some universal constants c1 , c2 . This proves the claim statement.
We now proceed to prove Claim 38.
Proof of Claim 38. Recall that the aim is to prove that for every X ⊆ Λ and unitary UX we have
O(1)/β

eO(1)|X| δγ
2
√
ρ
≤
AQA
U
X
β
γ
F
γ

+

O(1)|X|5 2
hA i
γ5

We let c5 , λ1 , τ1 be O(1) constants as defined in Lemma 22 and c1 , c2 , λ = O(1) be constants given
by Claim 37. For the proof, we first decompose QA
γ as
QA
γ =

∞
X

PsA ,

A
A
PsA := P(sγ,(s+1)γ]
+ P[−(s+1)γ,−sγ)
,

(112)

s=1

P
A is defined as P A :=
where P[a,b]
a≤ω≤b Πω (where Πω is the subspace spanned by the eigenvec[a,b]
√
tors of A with eigenvalue ε). Using this notation, observe that kAQA
γ UX ρβ kF can bounded by
∞

∞

s=1

s=1
∞
X
2

X
X
2
2
2
2
√
√
√
AQA
APsA UX ρβ F ≤
APsA · PsA UX ρβ F
γ UX ρβ F =
2
√
(s + 1)2 PsA UX ρβ F ,

≤γ

(113)

s=1

√
where we use kAPsA k ≤ γ(s + 1) from the definition (112) of PsA . The norm PsA UX ρβ F is
bounded from above by
√
PsA UX ρβ F =

PsA UX

∞
X

√
PsA0 ρβ

s0 =0

F

≤

∞
X

√
PsA UX PsA0 ρβ F ,

(114)

s0 =0

P
A
where we use ∞
s0 =0 Ps0 = 1 in the first equation and in the second inequality we use the triangle
inequality for the Frobenius norm. Using Lemma 22 we additionally have
0

1/τ1

kPsA UX PsA0 k ≤ c5 |X|e−(λ1 γ|s−s |/|X|)
37

for every s, s0 ≥ 0,

(115)

where c5 , λ1 are as given in Lemma 22. Using this, we have
1/2
1/2
√
√
√
PsA UX P0A ρβ F = PsA UX P0A ρβ F · PsA UX P0A ρβ F

c2 1/2
(1)
√
1/2
c +β
· kPsA UX P0A ρβ kF
≤ 2c1 eλ|X| δγ 2



(2)

≤

λ|X|

2c1 e


(3)

≤

λ|X|

2c1 e

c2
c2 +β

1/2

c2
c2 +β

1/2 

1/τ1 1/2
·1
· c5 |X|e−(λ1 γ|s|/|X|)

δγ
δγ

· PsA UX P0A

1/2

√
1/2
· k ρβ kF

(116)



1/τ1 1/2
= (δγ0 )1/2 · c5 |X|e−(λ1 γ|s|/|X|)
,

(4)

c2
c2 +β

√
PsA UX P0A ρβ F
√

10 , inequality (2) uses Eq. (16), inequalwhere inequality (1) uses
≤ 2c1 δγ
ity (3) uses Eq. (115) and the fact that k ρβ kF = tr(ρβ ) = 1 and equality (4) defines δγ0 :=
c2
c +β

2c1 eλ|X| δγ 2

. Using Eq. (116), we obtain the following
∞

∞
X

X
√
√
√
PsA UX PsA0 · PsA0 ρβ F
PsA UX PsA0 ρβ F ≤ PsA UX P0A ρβ F +
s0 =1

s0 =0

1/τ1
1/2 1/2
≤ δ 0 γ c5 |X|1/2 e−(λ1 γs/|X|) /2
∞
X
0
1/τ1
√
+
c5 |X|e−(λ1 γ|s−s |/|X|)
PsA0 ρβ F ,
s0 =1

(117)

where the first term in the inequality was obtained from Eq. (116) and the second term was obtained
from Eq. (115).
We now upper bound the summation in the second term of Eq. (117) by using the Cauchy–
Schwarz inequality as follows:
∞
X

0

e−(λ1 γ|s−s |/|X|)

s0 =1
∞
X

=

0

1/τ1

√
PsA0 ρβ F

1/τ1 /2

e−(λ1 γ|s−s |/|X|)

s0 =1

≤
(1)

≤
10

∞
X

0

!1/2
−(λ1 γ|s−s0 |/|X|)1/τ1

e

s0 =1



4τ1 |X|
(2τ1 )τ1
λ1 γ

1/τ1 /2

· e−(λ1 γ|s−s |/|X|)
∞
X


√
PsA0 ρβ F
2
√
PsA0 ρβ F

−(λ1 γ|s−s0 |/|X|)1/τ1

e

!1/2

s0 =1

1/2
·

∞
X

!1/2
−(λ1 γ|s−s0 |/|X|)1/τ1
pA
s0 e

,

(118)

s0 =1

A
A
A
Since QA
γ ≤ 1 and P0 = Pγ = 1 − Qγ , we have

√
PsA UX P0A ρβ

F

A √
≤ QA
γ UX (1 − Qγ ) ρβ

F

√
≤ QA
γ UX ρβ

F

A√
+ QA
ρβ
γ UX Qγ

F

√
≤ QA
γ UX ρβ
c

c2
c +β

+δγ ≤ 2c1 eλ|X| δγ 2
F

2
√
A
λ|X| c2 +β
where the first inequality used PsA ≤ QA
δγ
from Claim 37.
γ and the last inequality used kQγ UX ρβ kF ≤ c1 e

38

,

P
2
√
A√
2
where ps0 := PsA0 ρβ F and we used Fact 12 in inequality (1). Note that ∞
s0 =1 ps0 = kQγ ρβ kF
A
A
because of P0A = P(0,γ]
+ P[−γ,0)
= PγA . We can obtain the following upper bound by combining
the equations Eq. (114), (117) and (118):
2
√
PsA UX ρβ F
∞
2
X
√
PsA UX PsA0 ρβ F
≤
s0 =0



1/τ1 /2

1/2 1/2

≤ δ 0 γ c5 |X|1/2 e−(λ1 γs/|X|)
≤



+

∞
X
s0 =1

0

c5 |X|e−(λ1 γ|s−s |/|X|)

1/τ1
1/2 1/2
δ 0 γ c5 |X|1/2 e−(λ1 γs/|X|) /2 + c5 |X|



4τ1 |X|
(2τ1 )τ1
λ1 γ
∞
X

8c2 τ1 |X|3
+ 5
(2τ1 )τ1 ·
}
λ1 γ
|

−(λ1 γs/|X|)1/τ1

≤ 2c5 δ 0 γ |X|e
{z
|

:=f1 (s)

1/τ1

2
√
PsA0 ρβ F
∞
X

1/2
·

!1/2
−(λ1 γ|s−s0 |/|X|)1/τ1
pA
s0 e

2

s0 =1

!
−(λ1 γ|s−s0 |/|X|)1/τ1

pA
s0 e

.

{z

}

s0 =1
:=f2 (s)

Recall that the goal of this claim was to upper bound Eq. (113), which we can rewrite now as
∞

∞

∞

s=1

s=1

s=1

X
X
X
2
2
√
√
2
AQA
(s + 1)2 PsA UX ρβ F ≤ γ 2
(s + 1)2 f1 (s) + γ 2
(s + 1)2 f2 (s). (119)
γ UX ρβ F ≤ γ
We bound each of these terms separately. In order to bound the first term observe that
γ2

∞
∞
X
X
1/τ1
(s + 1)2 f1 (s) = 2γ 2 c5 δγ0 |X|2
(s + 1)2 e−(λ1 γs/|X|)
s=1

s=1

(1)

2

0



≤ 2γ c5 δ γ |X| · 8τ1 ·

(3τ1 )τ1 |X|
λ1 γ

3
≤

16c5 δγ0 |X|4 τ1 (3τ1 )3τ1
,
λ31 γ

where inequality (1) uses Fact 12. We now bound the second term in Eq. (119) as follows
!
∞
∞
∞
2
3
X
X
X
τ1
2
2
2 8c5 τ1 |X|
2
A −(λ1 γ|s−s0 |/|X|)1/τ1
γ
(s + 1) f2 (s) = γ ·
(2τ1 )
(s + 1)
p s0 e
.
λ1 γ
0
s=1

s=1
s =1
∞
∞
τ1 X


2
3
X
8γc5 τ1 |X| (2τ1 )
2 −(λ1 γ|s−s0 |/|X|)1/τ1
pA
(s
+
1)
e
=
s0
λ1
s=1
s0 =1
∞
∞
τ1 X
X

2
3
8γc5 τ1 |X| (2τ1 )
0
1/τ1
A
0 2
ps0 (2s )
(1 + |s − s0 |)2 e−(λ1 γ|s−s |/|X|)
≤
λ1
s=1
s0 =1

 ∞
(1) 8γc2 τ |X|3 (2τ )τ1
(3τ1 )τ1 |X| 3 X A 0 2
1
5 1
≤
· 16τ1 ·
ps0 (2s ) ,
λ1
λ1 γ
s0 =1

(120)

39

where inequality (1) follows from Fact 12. Further upper bound this expression by simplifying the
pre-factors, we get
∞

∞
X

512c25 |X|6 τ12 (3τ1 )4τ1 X A 0 2
γ
(s + 1) f2 (s) ≤
ps0 (s )
λ41 γ 2
0
s=1
2

2

s =1
∞
2
6
2
4τ
X
1
512c5 |X| τ1 (3τ1 )
=
(γs0 )2 pA
s0
λ41
s0 =1
∞

512c25 |X|6 τ12 (3τ1 )4τ1 X
2
√
PsA0 (γs0 ) ρβ F
=
4
λ1
0

s =1
∞
2
6
2
4τ
(2) 512c |X| τ (3τ ) 1 X
1
5
1
≤
λ41
s0 =0

(121)

512c25 |X|6 τ12 (3τ1 )4τ1 2
2
√
PsA0 A ρβ F =
hA i,
λ41

In inequality (2), we used PsA0 (γs0 )  PsA0 from the definition (112) of PsA0 . By combining the above
inequalities altogether, we prove Eq. (89).
t
u

References
[Aar18a]

Scott Aaronson. Shadow tomography of quantum states. In STOC’18—Proceedings
of the 50th Annual ACM SIGACT Symposium on Theory of Computing, pages 325–338.
ACM, New York, 2018. 4.1

[AAR+ 18b] Mohammad H Amin, Evgeny Andriyash, Jason Rolfe, Bohdan Kulchytskyy, and
Roger Melko. Quantum boltzmann machine. Physical Review X, 8(2):021050, 2018.
4.1
[AE11]

Dorit Aharonov and Lior Eldar. On the complexity of commuting local Hamiltonians,
and tight conditions for topological order in such systems. In 2011 IEEE 52nd Annual
Symposium on Foundations of Computer Science—FOCS 2011, pages 334–343. IEEE Computer Soc., Los Alamitos, CA, 2011. 4.2

[AG18]

Joran van Apeldoorn and András Gilyén. Improvements in quantum SDP-solving
with applications. arXiv preprint arXiv:1804.05058, 2018. 1

[AGGW20] Joran van Apeldoorn, András Gilyén, Sander Gribling, and Ronald de Wolf. Quantum
SDP-solvers: Better upper and lower bounds. Quantum, 4:230, 2020. 1
[AHS85]

David H Ackley, Geoffrey E Hinton, and Terrence J Sejnowski. A learning algorithm
for boltzmann machines. Cognitive science, 9(1):147–169, 1985. 1

[AKL16]

Itai Arad, Tomotaka Kuwahara, and Zeph Landau. Connecting global and local energy distributions in quantum spin models on a lattice. Journal of Statistical Mechanics:
Theory and Experiment, 2016(3):033301, March 2016. 21, 5.4, 22, 7.1, C, C

[AR19]

Scott Aaronson and Guy N. Rothblum. Gentle measurement of quantum states and
differential privacy. In STOC’19—Proceedings of the 51st Annual ACM SIGACT Symposium on Theory of Computing, pages 322–333. ACM, New York, 2019. 4.1
40

[Ara69]

Huzihiro Araki. Gibbs states of a one dimensional quantum lattice. Communications in
Mathematical Physics, 14(2):120–157, Jun 1969. 3.3

[BAL19]

Eyal Bairey, Itai Arad, and Netanel H Lindner. Learning a local hamiltonian from
local measurements. Physical review letters, 122(2):020504, 2019. 1, 4.1

[BG17]

Sergey Bravyi and David Gosset. Polynomial-time classical simulation of quantum
ferromagnets. Physical Review Letters, 119(10):100503, 2017. 4.2

[BGP+ 20]

Eyal Bairey, Chu Guo, Dario Poletti, Netanel H Lindner, and Itai Arad. Learning the
dynamics of open quantum systems from their steady states. New Journal of Physics,
2020. 1

[BHV06]

S. Bravyi, M. B. Hastings, and F. Verstraete. Lieb-robinson bounds and the generation
of correlations and topological quantum order. Phys. Rev. Lett., 97:050401, Jul 2006. D

[BK16]

Fernando GSL Brandão and Michael J Kastoryano. Finite correlation length implies efficient preparation of quantum thermal states. Communications in Mathematical Physics,
pages 1–16, 2016. 4.2

[BKF19]

Fernando GS L Brandão, Richard Kueng, and Daniel Stilck França. Faster quantum
and classical SDP approximations for quadratic binary optimization. arXiv preprint
arXiv:1909.04613, 2019. 1

[BKL+ 17]

Fernando GSL Brandao, Amir Kalev, Tongyang Li, Cedric Yen-Yu Lin, Krysta M Svore,
and Xiaodi Wu. Exponential quantum speed-ups for semidefinite programming with
applications to quantum learning. arXiv preprint arXiv:1710.02581, 2017. 1, 3.1, 4.1, 4.2

[BMBO19]

Xavier Bonet-Monroig, Ryan Babbush, and Thomas E O’Brien. Nearly optimal
measurement scheduling for partial tomography of quantum states. arXiv preprint
arXiv:1908.05628, 2019. 4.1, 5.6

[Bre15]

Guy Bresler. Efficiently learning Ising models on arbitrary graphs [extended abstract].
In STOC’15—Proceedings of the 2015 ACM Symposium on Theory of Computing, pages
771–782. ACM, New York, 2015. 1, 1, 4.1

[BS17]

Fernando GSL Brandao and Krysta M Svore. Quantum speed-ups for solving semidefinite programs. In Foundations of Computer Science (FOCS), 2017 IEEE 58th Annual
Symposium on, pages 415–426. IEEE, 2017. 1

[BV03]

Sergey Bravyi and Mikhail Vyalyi. Commutative version of the k-local hamiltonian
problem and common eigenspace problem. arXiv preprint quant-ph/0308021, 2003. 4.2

[CW20]

Jordan Cotler and Frank Wilczek. Quantum overlapping tomography. Physical Review
Letters, 124(10):100401, 2020. 4.1, 5.6

[EHF19]

Tim J Evans, Robin Harper, and Steven T Flammia. Scalable bayesian hamiltonian
learning. arXiv preprint arXiv:1912.07636, 2019. 1, 4.1

[FU15]

Jürg Fröhlich and Daniel Ueltschi. Some properties of correlations of quantum lattice systems in thermal equilibrium. Journal of Mathematical Physics, 56(5):053302, 2015. 3.3
41

[Gro79]

Leonard Gross. Decay of correlations in classical lattice models at high temperature. Communications in Mathematical Physics, 68(1):9–27, Feb 1979. 3.3

[Has07]

Matthew B Hastings. Quantum belief propagation: An algorithm for thermal quantum systems. Physical Review B, 76(20):201102, 2007. 5.3, 20

[HC71]

J. M. Hammersley and P. E. Clifford. Markov field on finite graphs and lattices. 1971.
3.3

[HKK08]

Masahito Hayashi, Akinori Kawachi, and Hirotada Kobayashi. Quantum measurements for hidden subgroup problems with optimal sample complexity. Quantum Information and Computation, 8:0345–0358, 2008. F

[HKM17]

Linus Hamilton, Frederic Koehler, and Ankur Moitra. Information theoretic properties of markov random fields, and their algorithmic applications. In Advances in Neural
Information Processing Systems, pages 2463–2472, 2017. 1

[HKP20]

Hsin-Yuan Huang, Richard Kueng, and John Preskill. Predicting many properties of a
quantum system from very few measurements. arXiv preprint arXiv:2002.08953, 2020.
4.1, 5.6

[HMS19]

Aram Harrow, Saeed Mehraban, and Mehdi Soleimanifar. Classical algorithms, correlation decay, and complex zeros of partition functions of quantum many-body systems. arXiv preprint arXiv:1910.09071, 2019. 4.2

[HS+ 86]

Geoffrey E Hinton, Terrence J Sejnowski, et al. Learning and relearning in boltzmann
machines. Parallel distributed processing: Explorations in the microstructure of cognition,
1(282-317):2, 1986. 1

[HW12]

A. W. Harrow and A. Winter. How many copies are needed for state discrimination?
IEEE Transactions on Information Theory, 58(1):1–2, 2012. F

[HW20]

Aram W Harrow and Annie Y Wei. Adaptive quantum simulated annealing for
bayesian inference and estimating partition functions. In Proceedings of the Fourteenth
Annual ACM-SIAM Symposium on Discrete Algorithms, pages 193–212. SIAM, 2020. 1

[Jay57a]

Edwin T Jaynes. Information theory and statistical mechanics.
106(4):620, 1957. 3.1

[Jay57b]

Edwin T Jaynes. Information theory and statistical mechanics. ii. Physical review,
108(2):171, 1957. 3.1, 3.1

[Jay82]

Edwin T Jaynes. On the rationale of maximum-entropy methods. Proceedings of the
IEEE, 70(9):939–952, 1982. 3.1

[KB19]

Kohtaro Kato and Brandão, Fernando G. S. L. Quantum approximate Markov chains
are thermal. Comm. Math. Phys., 370(1):117–149, 2019. 3.4.2, 5.3

[KGK+ 14]

M. Kliesch, C. Gogolin, M. J. Kastoryano, A. Riera, and J. Eisert. Locality of Temperature.
Phys. Rev. X, 4:031019, Jul 2014. 3.3
42

Physical review,

[Kim17]

Isaac H Kim. Markovian matrix product density operators: Efficient computation of
global entropy. arXiv preprint arXiv:1709.07828, 2017. 5.3

[KKB19]

Tomotaka Kuwahara, Kohtaro Kato, and Fernando GSL Brandão. Clustering of conditional mutual information for quantum gibbs states above a threshold temperature.
arXiv preprint arXiv:1910.09425, 2019. 3.4.2, 4.2

[KM17]

Adam R. Klivans and Raghu Meka. Learning graphical models using multiplicative
weights. In 58th Annual IEEE Symposium on Foundations of Computer Science—FOCS
2017, pages 343–354. IEEE Computer Soc., Los Alamitos, CA, 2017. 1, 1, 4.1, 4.2

[KMS16]

Tomotaka Kuwahara, Takashi Mori, and Keiji Saito. Floquet-magnus theory and
generic transient dynamics in periodically driven many-body quantum systems. Annals of Physics, 367:96 – 124, 2016. C.3

[Kuw16]

Tomotaka Kuwahara. Asymptotic behavior of macroscopic observables in generic
spin systems. Journal of Statistical Mechanics: Theory and Experiment, 2016(5):053103,
2016. C

[LP08]

Matthew S Leifer and David Poulin. Quantum graphical models and belief propagation. Annals of Physics, 323(8):1899–1946, 2008. 3.4.2

[LR72]

Elliott H. Lieb and Derek W. Robinson. The finite group velocity of quantum spin
systems. Communications in Mathematical Physics, 28(3):251–257, 1972. 15

[Mon15a]

Andrea Montanari. Computational implications of reducing data to sufficient statistics. Electron. J. Stat., 9(2):2370–2390, 2015. 3.3, 4.2

[Mon15b]

Ashley Montanaro. Quantum speedup of monte carlo methods. Proceedings of the
Royal Society A: Mathematical, Physical and Engineering Sciences, 471(2181):20150301,
2015. 1

[MST+ 20]

Mario Motta, Chong Sun, Adrian TK Tan, Matthew J OâĂŹRourke, Erika Ye, Austin J
Minnich, Fernando GSL Brandão, and Garnet Kin-Lic Chan. Determining eigenstates
and thermal states on a quantum computer using quantum imaginary time evolution.
Nature Physics, 16(2):205–210, 2020. 1

[NS09]

Bruno Nachtergaele and Robert Sims. Locality estimates for quantum spin systems.
In Vladas Sidoravičius, editor, New Trends in Mathematical Physics, pages 591–614, Dordrecht, 2009. Springer Netherlands. 15

[PY95]

Yong Moon Park and Hyun Jae Yoo. Uniqueness and clustering properties of Gibbs states
for classical and quantum unbounded spin systems. Journal of Statistical Physics, 80(1):223–
271, Jul 1995. 3.3

[QR19]

Xiao-Liang Qi and Daniel Ranard. Determining a local Hamiltonian from a single
eigenstate. Quantum, 3:159, July 2019. 4.1

[RWL+ 10]

Pradeep Ravikumar, Martin J Wainwright, John D Lafferty, et al. High-dimensional
ising model selection using l1-regularized logistic regression. The Annals of Statistics,
38(3):1287–1319, 2010. 1, 1
43

[TOV+ 11]

Kristan Temme, Tobias J Osborne, Karl G Vollbrecht, David Poulin, and Frank Verstraete. Quantum metropolis sampling. Nature, 471(7336):87, 2011. 1

[Uel04]

Daniel Ueltschi. Cluster expansions and correlation functions. Moscow Mathematical Journal, 4(2):511–522, 2004. 3.3

[VMLC16]

Marc Vuffray, Sidhant Misra, Andrey Lokhov, and Michael Chertkov. Interaction
screening: Efficient and sample-optimal learning of ising models. In Advances in Neural Information Processing Systems, pages 2595–2603, 2016. 1, 1, 3.3, 4.1, 4.2

[VMN+ 19] Guillaume Verdon, Jacob Marks, Sasha Nanda, Stefan Leichenauer, and Jack Hidary.
Quantum hamiltonian-based models and the variational quantum thermalizer algorithm. arXiv preprint arXiv:1910.02071, 2019. 4.1
[WGFC14a] Nathan Wiebe, Christopher Granade, Christopher Ferrie, and David Cory. Quantum hamiltonian learning using imperfect quantum resources. Physical Review A,
89(4):042314, 2014. 1, 4.1
[WGFC14b] Nathan Wiebe, Christopher Granade, Christopher Ferrie, and David G Cory. Hamiltonian learning and certification using quantum resources. Physical review letters,
112(19):190501, 2014. 1, 4.1
[WKS14]

Nathan Wiebe, Ashish Kapoor, and Krysta M Svore. Quantum deep learning, 2014. 1

[WPS+ 17]

Jianwei Wang, Stefano Paesani, Raffaele Santagati, Sebastian Knauer, Antonio A Gentile, Nathan Wiebe, Maurangelo Petruzzella, John G O’Brien, Jeremy L. Rarity, Anthony Laing, et al. Experimental quantum hamiltonian learning. Nature Physics,
13(6):551–555, 2017. 1

A

Proof of Fact 12

Here we restate and prove the following fact.
Fact 40 (Restatement of Fact 12). Let a, c, p > 0 be reals and b be a positive integer. Then
P∞ −cj
c
1)
≤ ec .
j=0 e
2)

P∞

3)

P∞

p

b −cj ≤ 2 ·
j=0 j e
p

j=0



b+1
cp

c p
p
e−c(a+j) ≤ e− 2 a

 b+1
p

.


 1 
2 p
1
1 + p cp
.

Proof. The first summation follows from
∞
X
j=0

e−cj =

1
ec
ec
=
≤
.
1 − e−c
ec − 1
c

44

p
For the second sum, notice that the function tb e−ct achieves the maximum at t∗ =

∞
X

b −cj p

j e

j=0

∗ b −c(t∗ )p

∗

≤ t (t ) e

=

=

≤

b
cp

Z ∞

 1
b
cp

p

. Then

p

tb e−ct dt

+
0

 b+1
p

− pb

Z ∞

1

e−y

p
b+1

dy
b+1
(b + 1)c p 0
! b+1


p
b
1
b+1
+
Γ
b
b+1
p
e b+1 cp
pc p
! b+1

 b+1
 b+1

p
b+1 p
b
1
2
b+1 p
+ b+1
≤ ·
.
b
p
p
cp
e b+1 cp
pc p
e

+

For the third sum, we will use the identity
(a + j)p ≥ 2p−1 (ap + j p ) ≥

1 p
(a + j p ) .
2

This is clearly true if p ≥ 1. For p < 1, we use concavity. Now, consider the following chain of
inequalities and change of variables:
∞
X
j=0

c p

p

e−c(a+j) ≤ e− 2 a
≤e

− 2c ap

=e

− 2c ap

∞
X

c p

e− 2 `

`=0

Z ∞


1+

e

− 2c tp


dt

0
1

1+

2p

!

Z ∞

e

1

cp

−y p

dy

0

1

=e

− 2c ap

 !
c p
1
1+ 1Γ
≤ e− 2 a
p
pc p
2p

t
u

This completes the proof.

B

 1 !
2 p
1+ 1
.
pc p p
1

Fourier transform of tanh(βω/2)/(βω/2)

We here derive the Fourier transform of
tanh(βω/2)
f˜β (ω) =
,
βω/2
which is
fβ (t) :=

1
2π

Z ∞
−∞

45

eiωt f˜β (ω)dω.

Im(!)

Im(!)
Re(!)

Re(!)

(b) Integral path C − of ω for t < 0

(a) Integral path C + of ω for t > 0

Figure 3: Cauchy’s integral theorem for the calculation of the Fourier transform.
For the calculation of the Fourier transform, we first consider the case of t > 0. By defining C +
as a integral path as in Fig. 3 (a), we obtain
Z ∞
Z
1
1
eiωt f˜β (ω)dω =
eiωt f˜β (ω)dω
2π −∞
2π C +
∞
X
(122)
=i
Resω=iπ+2imπ [eiωt f˜β (ω)].
m=0

Note that the singular points of [eiωt f˜β (ω)] are given by βω = iπ(2m + 1) with m integers. We can
calculate the residue as
Resβω=iπ+2imπ [eiωt f˜β (ω)] =

4e−(2m+1)πt/β −i
βπ
2m + 1

(123)

We thus obtain
fβ (t) =

1
2π

Z ∞

∞

eiωt f˜β (ω)dω =

−∞

4 X e−(2m+1)πt/β
.
βπ
2m + 1

(124)

m=0

for t > 0.
We can perform the same calculation for t < 0. In this case, we define C − as a integral path as
in Fig. 3 (b), and obtain
Z
∞
X
1
iωt ˜
fβ (t) =
e fβ (ω)dω = −i
Resω=−iπ−2imπ [eiωt f˜β (ω)].
(125)
2π C −
m=0

By using
Resω=−iπ−2imπ [eiωt f˜β (ω)] =

4e(2m+1)πt/β
i
,
βπ
2m + 1

(126)

we have
1
fβ (t) =
2π

Z ∞

∞

eiωt f˜β (ω)dω =

−∞

4 X e(2m+1)πt/β
.
βπ
2m + 1
m=0

46

(127)

for t < 0. By combining the above expressions for fβ (t), we arrive at
∞

4 X e−(2m+1)π|t|/β
fβ (t) =
.
βπ
2m + 1

(128)

m=0

The summation is calculated as
Z ∞X
Z ∞
∞
∞
X
1
1
e−(2m+1)x
ex + 1
0
−(2m+1)x0
0
dx
=
=
e
dx =
log
0
0
2m + 1
2
ex − 1
ex − e−x
x
x
m=0

(129)

m=0

for x > 0, which yields
fβ (t) =
Since
log

2
eπ|t|/β + 1
.
log π|t|/β
βπ
e
−1

(130)

eπ|t|/β + 1
2
≤ π|t|/β
,
π|t|/β
e
−1
e
−1

fβ (t) shows an exponential decay in |t|.

C

Derivation of the sub-exponential concentration

Recall that the goal in this appendix is to prove the following lemma.
Lemma 41 (Restatement of Lemma 22). Let A be a (τ, a1 , a2 , 1)-quasi-local operator with τ < 1, as given
in Eq. (19). For an arbitrary operator OX supported on a subset X ⊆ Λ with |X| = k0 and kOX k = 1,
we have


A
A
kP≥x+y
OX P≤x
k ≤ c5 · k0 exp − (λ1 y/k0 )1/τ1 ,
(131)
where τ1 := τ2 − 1 and c5 and λ1 are constants which only depend on a1 and a2 . In particular, the a2
2/τ

dependence of c5 and λ1 is given by c5 ∝ a2

−2/τ

and λ1 ∝ a2

respectively.

Before proving this lemma, let us elaborate upon the method. Recall that
X
X
A
A
P≤x
=
Πω , P>y
=
Πω ,

(132)

ω>y

ω≤x

where Πω is the projector onto the eigenvalue ω eigenspace of A. One way to prove the upper bound
in the estimation of the norm (131) is to utilize the technique in Ref. [AKL16] (i.e., Lemma 21). The
argument proceeds by considering
A
A
A
A
kP≥x+y
OX P≤x
k = kP≥x+y
e−νA eνA OX e−νA eνA P≤x
k

A
A
≤ kP≥x+y
e−νA k · keνA OX e−νA k · keνA P≤x
k

≤ e−νx keνA OX e−νA k,

47

(133)

which reduces the problem to estimation of the norm keνA OX e−νA k. Additionally, by definition
of A in Theorem 33 we have
A=

n
X

g` Ā` ,

(134)

`=1

where Ā` is κ-local and g` is sub-exponentially decaying function for ` (as made precise in Eq. (19)),
namely g` = exp(−O(`1/D )). In this case, for ν = O(1), the norm of the imaginary time evolution
can be finitely bounded only in the case D = 1 [Kuw16]. That is, the norm keνA OX e−νA k diverges
to infinity for D ≥ 2. However, our main contribution in this section is that we are able to prove
the lemma statement without going through the inequalities in (133) (which in turn used earlier
results of [Kuw16, AKL16]). We now give more details.

C.1

Proof of Lemma 41

In order to estimate the norm, we need to take a different route from (133). Let I be any interval
of the real line and PIA be the projector onto the eigenspace of A with eigenvalues in I. Using the
operator inequality
A
A
P≥z
(A − ω1)m  (z − ω)m P≥x+y
,
we obtain
A
A
k(A − ω1)m OX PIA k ≥ kP≥z
(A − ω)m OX PIA k ≥ (z − ω)m kP≥z
OX PIA k,

(135)

hence
A
kP≥z
OX PIA k ≤

k(A − ω)m OX PIA k
.
(z − ω)m

(136)

Our strategy to establish Eq. (131) will be to expand
A
A
kP≥x+y
OX P≤x
k≤

∞
X
j=0

A
kP≥x+y
OX PIAj k,

(137)

for carefully chosen intervals Ij := (x − a1 (j + 1), x − a1 j] (the term a1 is as given in the statement
of Lemma 41). Towards this, let us fix an arbitrary ω, an interval I := (ω − a1 , ω] and prove an
A
upper bound on kP≥ω+θ
OX PIAj k (for all θ). We show the following claim.
Claim 42. There is a constant c6 such that
A
kP≥ω+θ
OX PIA k ≤

h
i
1
exp −[θ/(ec6 k0 )]1/τ1 + 1 .
τ

(138)

The claim is proved in subsection C.2. Let us use the claim to establish the lemma. In the
A
inequality (137), we need to estimate kP≥x+y
OX PIAj k with Ij := (x − (j + 1)a1 , x − ja1 ]. Setting
ω = x − ja1 and θ = y + ja1 in Claim 42, we have
( 
)

1
y + a1 j 1/τ1
A
A
kP≥x+y OX PIj k ≤ exp −
+1 .
(139)
τ
ec6 k0
48

In order to complete the bound on Equation 137, we need to take summation with respect to j. We
have
)
( 

1/τ1

1/τ1 
∞
∞
X
X
1 − 12 ec yk
y
+
a
j
ec6 k0 τ1
1
1
1/τ
A
A
1
6 0
,
+1 ≤ e
(4/τ )
exp −
kP≥x+y OX PIj k ≤
1+
τ
ec6 k0
τ
a1
j=0

j=0

(140)
where in last inequality we used Fact 12 (3) with c = (ec6 k0 /a1 )−1/τ1 , p = 1/τ1 and a = y/a1 . This
gives the form of (131) and completes the proof.

C.2

Proof of Claim 42

From Equation 136, it suffices to upper bound k(A − ω)m OX PIA k. Abbreviate Ã := A − ω1. Introduce the multi-commutator
adsÃ (OX ) := [Ã, . . . [Ã, [Ã, OX ]] . . .] .
|
{z
}
s times

Consider the following identity,
Ã

m

OX PIA =

m  
X
m
s=0

s

adsÃ (OX )Ãm−s PIA .

(141)

This shows that
kÃ

m

OX PIA k ≤

m  
m  
X
X
m m−s
m
m−s A
s
k adsÃ (OX )k,
PI k ≤
a
k adÃ (OX )k · kÃ
s 1
s
s=0

(142)

s=0

. The remaining task is to estimate the upper
where we use kÃm−s PIA k = k(A − ω)m−s PIA k ≤ am−s
1
s
s
bound of k adÃ (OX )k = k adA (OX )k. This is done in the following claim.
Claim 43. Let A be an operator that is given by the form (19). Then, for an arbitrary operator OX which is
supported on a subset X (|X| = k0 ), the norm of the multi-commutator adsA (OX ) is bounded from above by
(2a1 )s (2k0 )s es
k adsA (OX )k ≤
·



τ

2
a2 τ

 2s
τ

· (sτ1 )s

for s ≤ m,

where the constants a1 and a2 have been defined in Eq. (19), and Γ(·) is the gamma function.
By applying the inequality (143) to (142), we obtain
2s

m

kÃ



m  
X
τ
m m−s (2a1 )s (2k0 )s es
2
a1
·
· (sτ1 )s
τ
a2 τ
s
s=0

 2m
m  
m
X
τ
m
2
m (2ek0 )
≤
(2a1 )
·
· (mτ1 )m
s
τ
a2 τ
s=0

 2m
im
m
τ
2
1h
m (2ek0 )
= (4a1 )
·
· (mτ1 )m =
8ea1 k0 [2/(a2 τ )]2/τ mτ1 .
τ
a2 τ
τ

OX PIA k ≤

49

(143)

Therefore, setting z = ω + θ in the inequality (136), we obtain
kÃ
A
kP≥ω+θ
OX PIA k ≤



mO P Ak
τ1 m
1
X I
2/τ m
8ea1 k0 [2/(a2 τ )]
≤
θm
τ
θ
1
≤
τ



c6 k0 mτ1
θ

(144)

m
,

(145)

where c6 := 8ea1 [2/(a2 τ )]2/τ . Let us choose m = m̃ with m̃ the minimum integer such that
c6 k0 m̃τ1
≤ 1/e.
θ

(146)

The above condition is satisfied by m̃τ1 ≤ θ/(ec6 k0 ), which implies
j
k
m̃ = [θ/(ec6 k0 )]1/τ1 ,

(147)

where b·c is the floor function. From this choice, the claim concludes.

C.3

Proof of Claim 43

Recall that we need to show, for an arbitrary operator OX which is supported on k0 sites, the norm
of the multi-commutator adsA (OX ) is bounded by
(2a1 )s (2k0 )s es
k adsA (OX )k ≤
·



τ

2
a2 τ

 2s
τ

· (sτ1 )s

for s ≤ m.

We start from the following expansion:
X
adsA (OX ) =
gk1 gk2 · · · gks [Āks , [Āks−1 , · · · [Āk1 , OX ] · · · ].
k1 ,k2 ,...,ks

By using Lemma 3 in Ref. [KMS16] and setting ζ = 1 (see Definition 19) we obtain
k[[Āks , [Āks−1 , · · · [Āk1 , OX ] · · · ]k ≤ 2s k0 (k0 + k1 )(k0 + k1 + k2 ) · · · (k0 + k1 + k2 + · · · + ks−1 ).
(148)
Recall that we set kOX k = 1 and |X| = k0 . The norm of adsA (OX ) is bounded from above by
k adsA (OX )k
∞
X
≤
2s gk1 gk2 · · · gks k0 (k0 + k1 )(k0 + k1 + k2 ) · · · (k0 + k1 + k2 + · · · + ks−1 )
k1 ,k2 ,...,ks =1

=

X

X

K≥s k1 +k2 +...+ks =K
k1 ≥1,k2 ≥1,...,ks ≥1

2s gk1 gk2 · · · gks k0 (k0 + k1 )(k0 + k1 + k2 ) · · · (k0 + k1 + k2 + · · · + ks−1 ),
(149)

s
where the summation over K starts from s because each
Ps of {kj }j=1 is larger than 1. Now, using the
τ
expression log[gk /a1 ] = −a2 k for τ ≤ 1, we have j=1 log(gkj /a1 ) ≤ log(gk1 +k2 +···+ks /a1 ). This

50

P
follows from sj=1 kjτ ≥ (k1 + k2 + · · · + ks )τ . Thus, using k1 + k2 + · · · + ks = K, the summand
in the inequality (149) is upper-bounded by
gk1 gk2 · · · gks k0 (k0 + k1 )(k0 + k1 + k2 ) · · · (k0 + k1 + k2 + · · · + ks−1 ) ≤ as1 (gK /a1 )k0 (k0 + K)s−1 ,
(150)
where we use the inequality k1 + k2 + · · · + kj ≤ K for j = 1, 2, . . . , s − 1. By combining the two
inequalities (149) and (150), we obtain
X
X
(2a1 )s (gK /a1 )k0 (k0 + K)s−1
k adsA (OX )k ≤
K≥s k1 +k2 +...+ks =K
k1 ≥1,k2 ≥1,...,ks ≥1


s
≤
(2a1 )s (gK /a1 )k0 (k0 + K)s−1
K −s
K≥s
X K − 1
(2a1 )s (gK /a1 )k0 (k0 + K)s−1
=
s−1

(1) X



K≥s

(2)

≤ (2a1 )s (2k0 )s

X es K s
ss

(gK /a1 )(K)s−1

K≥s
s
s
s
(2a1 )s (2k0 )s es X 2s−1 −a2 K τ
(3) (2a1 ) (2k0 ) e X
2s−1 −a2 K τ
=
K
e
≤
K
e
ss
ss
K≥s
K≥0


 2s 
s
τ
2
2
(2a1 )s (2k0 )s es
·
=
· s τ −1 .
τ
a2 τ




n
where in (1),
denotes the multi-combination, namely m
= n+m−1
, in 2 we upper bound
n−1
 es K s
K−1
s−1 ≤ ss , k0 + K ≤ 2k0 K, in (3) we use the sub-exponential form of gK in Eq. (19) and in (4)
we use Fact 12. Since τ1 = τ2 − 1, this proves the statement.
(4) (2a )s (2k )s es
1
0
≤
·
s
s τ

D



2s
a2 τ

 2s
τ

f
Quasi-locality of W

f , where {τ, a1 , a2 , ζ} defined in
We here aim to obtain (τ, a1 , a2 , ζ)-quasi-locality of the operator W
Definition 14. In particular, we will show that




2D+1
τ, a1 , a2 , ζ = 1/D, O(1), O(1/β), O(β
) max vj
j∈Λ

f . Recall the definition of W
f:
suffices to prove the quasi-locality of W
Z ∞
f
W =
fβ (t) e−iHt W eiHt dt,
−∞

where
fβ (t) =

2
eπ|t|/β + 1
log π|t|/β
βπ
e
−1
51

and

X

W =

vi Ei .

i∈Λ

We write
f=
W

X

Z ∞
−∞

i

Abbreviate

fβ (t) e−iHt Ei eiHt dt.

vi

Ẽi (t) := e−iHt Ei eiHt

R∞
and recall that Ẽi = ∞ fβ (t)Ẽi (t). Moreover, (with some abuse of notation) let B(r, i) denote the
ball of radius r such that: the centre of B(r, i) coincides with the the center of the smallest ball
containing Ei . We assume that r ranges in the set {mi , mi + 1, . . . , ni }, where mi is the radius of
the smallest ball containing Ei and ni is the number such that B(ni , i) = Λ. Define
Ẽir (t) := trB(r,i)c [Ẽi (t)] ⊗

1B(r,i)c
,
tr[1B(r,i)c ]

Ẽi0 (t) = 0,

i.e., W̃ir (t) traces out all the qudits in Ẽi (t) that are at outside the B(r, i)-ball around Ẽir . From
[BHV06], we have
o
n
kẼi (t) − Ẽir (t)k ≤ kEi k min 1, c3 rD−1 e−c4 (r−vLR |t|)
which in particular implies
o
n
kẼir (t) − Ẽir−1 (t)k ≤ 2 min 1, c3 rD−1 e−c4 (r−vLR |t|) ,
where we use kEi k = 1, vLR is the Lieb-Robinson velocity (as defined in Fact 15) and c3 , c4 are constants. We note that the 2 min{1, ·} is derived from the trivial upper bound kẼir (t) − Ẽir+1 (t)k ≤ 2.
This allows us to write the following quasi-local expression:
ni 
X

Ẽi (t) =

r=mi


Ẽir (t) − Ẽir−1 (t) .

Using this, we can now write the quasi-local representation of Ẽi as follows.
Z ∞

Z ∞
fβ (t)Ẽi (t)dt =

−∞

fβ (t)
−∞

ni 
X
r=mi


Ẽir (t) − Ẽir−1 (t) .

To see that it is quasi-local, observe that the term with radius r has norm
Z ∞
fβ (t) Ẽir (t) − Ẽir−1 (t)
−∞

≤ c3 r

D−1 −c4 r

e

·

≤ 2c3 rD−1 e−c4 r
≤ 2c3 r

D−1

Z r/vLR

c4 vLR |t|−π|t|/β

e

−r/vLR
|c
e 4 vLR −π/β|r/vLR − 1

|c4 vLR − π/β|

dt +

+2

− min(πr/(βvLR ),c4 r)

(r/vLR )e

Z ∞

−π|t|/β

e

Z −r/vLR
dt +

r/vLR
−πr/(βv
LR )
e

π/β

+ 2(β/π)e−πr/(βvLR ) ,
52

−∞

e−π|t|/β dt

where we use (exy − 1)/x ≤ yexy for x ≥ 0 and y ≥ 0. Define
Z ∞


πr/(2βvLR )
fβ (t) Ẽir (t) − Ẽir−1 (t) .
aB(r,i) := e
−∞

Here, the operator aB(r,i) is supported on the subset B(r, i). Then, from |B(r, i)| = O(rD ), the
f is given as
quasi-local representation of W
f=
W

X
i∈Λ

ni
X

vi

e−πr/(2βvLR ) aB(r,i) =

r=mi

ni
X X

1

e−O(|B(r,i)| D ) vi aB(r,i) ,

i∈Λ r=mi

1

with e−O(|B(r,i)| D ) decaying sub-exponentially with rate τ = 1/D, for all i ∈ Λ. We also obtain the
parameter ζ in Eq. (19) by

X
X
X
X
vj kaB(r,j) k ≤
c5 rD
vj e−πr/(2βvLR ) ≤ max vj
c5 cB r2D e−πr/(2βvLR )
r,j:B(r,j)3i

r

j∈Λ

j:B(r,j)3i

r


≤ 2cB c5

2D + 1
π/(2βvLR )

2D+1 


max vj ,
j∈Λ

where we define cB such that |B(r, j)| ≤ cB rD and we used Fact 12 (2) with p = 1,
f is a
b = 2D and c = π/(2βvLR ). This completes
the representation and shows that W

2D+1
1/D, O(1), O(1/β), O(β
) (maxj∈Λ vj ) -quasi-local.

E

Proof of Lemma 34

f defined in Lemma 30 we have
Recall that the goal in this section is to prove that for W


Ω(1)
2
2
f
max vi ,
max tr[(W(i) ) η] =
i∈Λ
(β log(β) + 1)2D+2 i∈Λ
where η is the maximally mixed state. In this direction, we will now prove that
f(i) √ηkF ≥
max kW
i∈Λ

c7

max(|vi |),
(β log(β) + 1)D+1 i∈Λ

(151)

for a constant c7 = O(1). For convenience, let us define argmaxi∈Λ |vi | = i+ , or equivalently |vi+ | =
maxi∈Λ |vi |. We denote the ball region B(r, i+ ) by Br for the simplicity, where r is fixed later. Let
f [Br ] which is defined as follows:
us consider W
Z ∞
X
f [Br ] :=
W
fβ (t)e−iHt W [Br ]eiHt dt, W [Br ] :=
vi Ei .
(152)
−∞

i∈Br

f [Br ] is obtained from W [Br ] in an equivalent manner as W
f is obtained from W , the folSince W
lowing claim follows along the same lines as Theorem 32. We skip the very similar proof.

53

Claim 44. It holds that
f [Br ]k2F ≥
kW

X
DΛ
vi2 ,
c5 [β log(r) + 1]2
i∈Br

where c5 is a constant of O(1).
f [Br ] well approximates the property of W
f around the site i+ , as long
Since the new operator W
f [Br ](i ) and W
f(i ) are close to each other. The claim below
as r is sufficiently large, we expect that W
+
+
makes this intuition rigorous:
Claim 45. It holds that
f(i ) − W
f [Br ](i ) k ≤ c1 |vi |β D e−c2 r/β ,
kW
+
+
+

(153)

where c1 , c2 are constants of O(1).
f(i ) which are not included in the
This claim implies that the contribution of all the terms in W
+
Br ball around i+ decays exponentially with r. Hence,
f(i ) kF = kW
f(i ) − W
f [Br ](i ) + W
f [Br ](i ) kF ≥ kW
f [Br ](i ) kF − kW
f(i ) − W
f [Br ](i ) kF
kW
+
+
+
+
+
+
+
p
f
f
f
≥ kW [Br ](i+ ) kF − DΛ kW(i+ ) − W [Br ](i+ ) k
p
f [Br ](i ) kF − DΛ c1 |vi |β D e−c2 r/β , (154)
≥ kW
+
+

√
f(i ) − W
f [Br ](i ) k in the second inequality. Second,
f(i ) − W
f [Br ](i ) kF ≤ DΛ kW
where we use kW
+
+
+
+
f [Br ] by W
f [Br , Br0 ] which are supported on Br0 :
we consider the approximation of W
f [Br , Br0 ] := trB c (W
f [Br ]) ⊗
W
r0

1Brc0
c

d|Br0 |

.

(155)

f , we expect W
f [Br , Br0 ] ≈ W
f [Br ] for r0  r. This is shown in the
Because of the quasi-locality of W
following lemma:
f [Br , Br0 ] and W
f [Br ] is upper-bounded as
Claim 46. The norm difference between W
f [Br ] − W
f [Br , Br0 ]k ≤ c3 |vi |rD βe−c4 |r0 −r|/β
kW
+

(156)

f [Br ](i ) − W
f [Br , Br0 ](i ) k ≤ 2c3 |vi |rD βe−c4 |r0 −r|/β ,
kW
+
+
+

(157)

and

where c3 , c4 are constants of O(1).
The claim reduces the inequality (154) to
p
f(i ) kF ≥ kW
f [Br ](i ) kF − DΛ c1 |vi |β D e−c2 r/β
kW
+
+
+
p
p
f [Br , Br0 ](i ) kF − DΛ kW
f [Br ](i ) − W
f [Br , Br0 ](i ) k − DΛ c1 |vi |β D e−c2 r/β
≥ kW
+
+
+
+
p
p
D −c2 r/β
D
−c4 (r0 −r)/β
f
≥ kW [Br , Br0 ](i+ ) kF − DΛ c1 |vi+ |β e
− 2 DΛ c3 |vi+ |r βe
.
(158)
54

f [Br , Br0 ](i ) to that of W
f [Br , Br0 ] using Claim 23. By recalling that
Next, we relate the norm of W
+
f [Br , Br0 ](i ) is supported on Br0 , this gives
W
+
f(i ) [Br , Br0 ]kF ≥
kW
+

1 f
kW [Br , Br0 ]kF ,
|Br0 |

(159)

which reduces the inequality (158) to
p
p
1 f
0
kW [Br , Br0 ]kF − DΛ c1 |vi+ |β D e−c2 r/β − 2 DΛ c3 |vi+ |rD βe−c4 (r −r)/β
|Br0 |
p
p
1 f
0
≥
kW [Br ]kF − DΛ c1 |vi+ |β D e−c2 r/β − (2 + 1/|Br0 |) DΛ c3 |vi+ |rD βe−c4 (r −r)/β ,
|Br0 |
(160)

f(i ) kF ≥
kW
+

f [Br , Br0 ]kF . Finally, we use the lower
where in the second inequality we apply Claim
P 46 2to kW
bound given in Claim 44 and the inequality i∈Br vi ≥ vi2+ (since i+ ∈ Br ) to obtain
f [Br ]k2F ≥
kW

DΛ
v2 .
c5 [β log(r) + 1]2 i+

This reduces the inequality (160) to the following:
f(i ) kF
kW
|vi+ |
0
√+
≥
− c1 |vi+ |β D e−c2 r/β − 3c3 |vi+ |rD βe−c4 (r −r)/β ,
√
D
DΛ
c8 (r0 )
c5 [β log(r) + 1]
where we used |Br0 | ≤ c8 (r0 )D , for some constant c8 . By choosing r0 = 2r and r = O(1)·Dβ log(β)+
1, we have
f(i ) kF
kW
c7 |vi+ |
f(i ) √ηkF ≥
√+
= kW
,
+
DΛ
(β log(β) + 1)D+1

(161)

f(i) kF ≥ kW
f(i ) kF , we obtain the main
for some constant c7 . By using the inequality maxi∈Λ kW
+
statement. This completes the proof. 

E.1

Proof of Claims 45, 46

Proof of Claim 45. Recall that the goal is to prove
f(i ) − W
f [Br ](i ) k ≤ c1 |vi |β D e−c2 r/β
kW
+
+
+
f(i ) :
for constants c1 , c2 . We start from the integral representation of W
+
Z
f(i ) = W
f − µ(Ui )U † W
f Ui ,
W
+
+
i+
+

(162)

where µ(Ui+ ) is the Haar measure for unitary operator Ui+ which acts on the i+ th site. This yields
Z
c
f
f
f
f [B c ]Ui .
W(i+ ) − W [Br ](i+ ) = W [Br ] − µ(Ui+ )Ui†+ W
(163)
r
+
55

We thus obtain
f [Brc ]]k
f(i ) − W
f [Br ](i ) k ≤ sup k[Ui , W
kW
+
+
+
Ui +

≤

Z ∞
fβ (t)
−∞

X
j∈B c

|vj | sup k[Ui+ , e−iHt Ej eiHt ]kdt
U(i)

r
XZ ∞
fβ (t) min(e−c(dist(i+ ,j)−vLR t) , 1)dt,
≤ |vi+ |

j∈Brc

(164)

−∞

where we use |vj | ≤ |vi+ | and the Lieb-Robinson bound (Fact 15) for the last inequality. Because
the function fβ (t) decays as e−O(t/β) and dist(i+ , j) ≥ r for j ∈ Brc , we have
XZ ∞
(165)
fβ (t) min(e−c(dist(i+ ,j)−vLR t) , 1)dt ≤ c1 |vi+ |β D e−c2 r/β .
|vi+ |
−∞

j∈Brc

t
u

This completes the proof.
Proof of Claim 46. Recall that we wanted to show
f [Br ] − W
f [Br , Br0 ]k ≤ c3 |vi |rD βe−c4 |r0 −r|/β .
kW
+
f [Br , Br0 ]:
In order to prove this, we also utilize the integral representation of W
Z
f [Br , Br0 ] := µ(UB c )U † c W
f [Br ]UB c ,
W
B 0
r0
r0
r

f [Br ] − W
f [Br , Br0 ]k as
which yields an upper bound of kW
Z
f [Br ] − W
f [Br , Br0 ]k ≤ µ(UB c )k[W
f [Br ], UB c ]k.
kW
r0
r0

(166)

(167)

f [Br ] and the Lieb-Robinson bound (Fact 15), we obtain
From the definition (152) of W
Z ∞
Z
Z
X
f
c
c
c
fβ (t)
|vj | · k[e−iHt Ej eiHt , UBrc0 ]k
µ(UBr0 )k[W [Br ], UBr0 ]k ≤ µ(UBr0 )
−∞

≤ |vi+ |

Z ∞
fβ (t)
−∞

j∈Br

X

0

min(e−c(r −r−vLR t) , 1)dt

j∈Br

≤ c03 |vi+ | · |Br | · βe−c4 r/β ,

(168)

where ∂Brc0 is the surface region of Brc0 . Since |Br | ∝ rD , we obtain the main inequality (156). Now,
since
Z
f [Br ](i ) = W
f [Br ] − µ(Ui )U † W
f [Br ]Ui
W
+
+
i+
+
and
f [Br , Br0 ](i ) = W
f [Br , Br0 ] −
W
+

Z

f [Br , Br0 ]Ui ,
µ(Ui+ )Ui†+ W
+

we obtain the second inequality (157) due to
f [Br ](i ) − W
f [Br , Br0 ](i ) k ≤ 2kW
f [Br ] − W
f [Br , Br0 ]k.
kW
+
+
t
u

This completes the proof.
56

F

Proof of Theorem 3

For convenience of the reader, we restate the theorem here.
Theorem 47 (Restatement of Theorem 3). The number of copies N of the Gibbs state needed to solve the
Hamiltonian Learning Problem and outputs a µ̂ satisfying kµ̂ − µk2 ≤ ε with probability 1 − δ is lower
bounded by
 √m + log(1 − δ) 
N ≥Ω
.
βε
Proof. In order to prove the lower bound, we consider learning the parameters µ ∈ Rm of the
following class of one-local Hamiltonians on m qubits:
H(µ) =

m
X
i=1

Let Tm : {µ ∈ Rm
+ :
the following claim.

µi |1ih1|i .

2
2
m
i µi ≤ 100ε } be an orthant of the hypersphere of radius θ in R+ . We have

P

Claim 48. There exists a collection of 2m points in Tm , such that the `2 distance between each pair is ≥ ε.
Proof. Pick 2m points uniformly at random in Tm . By union bound, the probability that at least one
pair is at a distance of at most ε is at most (2m )2 times the probability that a fixed pair of points is at
a distance of at most ε. But the latter probability is upper bounded by the ratio between the volume
m
of a hypersphere of radius ε and the volume of Tm , which is (10ε)εm /2m = 51m . Since (2m )2 51m < 1,
the claim concludes.
t
u
Let these set of 2m points be S. For some temperature β > 0 and unknown µ ∈ S, suppose A
is an algorithm that is given N copies of ρβ (µ) and, with probability 1 − δ, outputs µ0 satisfying
kµ0 − µk2 ≤ ε. We now use A to assign the estimated µ̂ to exactly one of the parameters µ. Once the
learning algorithm obtains an output µ0 , we can find the closest point in S (in `2 distance) as our
estimate of µ, breaking ties arbitrarily. With probability 1 − δ, the closest µ ∈ S to µ0 is the correct
µ since by the construction of S, kµ0 − µk2 ≤ ε. Thus, the algorithm A can be used to solve the
problem of estimating the parameters µ themselves (not only approximating it). We furthermore
show that the number of samples required to estimate µ ∈ S is large using lower bounds in the
quantum state discrimination. We will directly use the lower bound from [HKK08] (as given in
[HW12]). Before we plug in their formula, we need to bound the maximum norm of ρβ (µ) for

57

µ ∈ S. That is,
m
O

e−βµi
1
max{2 kρβ (µ)k} = max 2
|0ih0|
+
|1ih1|
µ∈S
µ∈S
1 + e−βµi
1 + e−βµi
i=1
!
m
O
2
= max
µ∈S
1 + e−βµi
i=1
!
m
O
2eβµi
= max
µ∈S
eβµi + 1
i=1
!
m
O
2eβµi
≤ max
µ∈S
2
i=1
 Pm 
√ √Pm
√
2
i=1 µi ≤ eβ m·10ε ,
= max eβ i=1 µi ≤ eβ m
m

m

!

µ∈S

P
since i µ2i ≤ 100ε2 for all i ∈ S. Thus, the lower bound for state identification of {H(µ) : µ ∈ S}
in [HW12, Equation 2] (cf. [HKK08] for the original statement) implies that
 √m + log(1 − δ) 
log |S| + log(1 − δ)
m log 2 + log(1 − δ)
√
N≥
=
.
=O
log (maxµ∈S {2m kρ(µ)β k})
εβ
10 mβε
t
u

This establishes the lower bound.

58

