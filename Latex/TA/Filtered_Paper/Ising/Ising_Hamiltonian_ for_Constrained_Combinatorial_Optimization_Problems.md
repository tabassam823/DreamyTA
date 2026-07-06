Ising Hamiltonians for Constrained Combinatorial Optimization Problems and the
Metropolis-Hastings Warm-Starting Algorithm
Hui-Min Li,1 Jin-Min Liang,1 Zhi-Xi Wang,1, ∗ and Shao-Ming Fei1, †

arXiv:2307.08980v1 [quant-ph] 18 Jul 2023

1 School of Mathematical Sciences, Capital Normal University, 100048, Beijing, China

Quantum approximate optimization algorithm (QAOA) is a promising variational quantum algorithm for
combinatorial optimization problems. However, the implementation of QAOA is limited due to the requirement
that the problems be mapped to Ising Hamiltonians and the nonconvex optimization landscapes. Although
the Ising Hamiltonians for many NP hard problems have been obtained, a general method to obtain the Ising
Hamiltonians for constrained combinatorial optimization problems (CCOPs) has not yet been investigated. In
this paper, a general method is introduced to obtain the Ising Hamiltonians for CCOPs and the MetropolisHastings warm-starting algorithm for QAOA is presented which can provably converge to the global optimal
solutions. The effectiveness of this method is demonstrated by tackling the minimum weight vertex cover
(MWVC) problem, the minimum vertex cover (MVC) problem, and the maximal independent set problem as
examples. The Ising Hamiltonian for the MWVC problem is obtained first time by using this method. The
advantages of the Metropolis-Hastings warm-starting algorithm presented here is numerically analyzed through
solving 30 randomly generated MVC cases with 1-depth QAOA.

∗ wangzhx@cnu.edu.cn
† feishm@cnu.edu.cn

2
I.

INTRODUCTION

Recently, there is immense interest in solving combinatorial optimization problems by using quantum algorithms, such as
quantum adiabatic algorithms [1–3], digitized adiabatic quantum computation [4, 5], quantum approximate optimization algorithm (QAOA) [6–8], and variational quantum eigensolver (VQE) [9, 10]. However, these quantum algorithms usually require
that the classical combinatorial optimization problems be mapped to Ising Hamiltonians whose ground states encode the solutions to these problems. Although the Ising Hamiltonians for many NP hard problems have been obtained in [11], a general
method to obtain the Ising Hamiltonians for constrained combinatorial optimization problems (CCOPs) has not yet been investigated.
In particular, the QAOA was originally proposed to find the approximate solutions to combinatorial optimization problems by
Farhi et al. in 2014 [6]. It is a promising approach for near-term noisy intermediate-scale quantum (NISQ) devices [12] which
are lack of error corrections and have imperfect gate implementations. In QAOA, the approximate solution to a combinatorial
optimization problem can be encoded as an ansatz wave function with 2p angle parameters (p is the depth of the algorithm). This
wave function can encode the exact solution when p → ∞ according to the adiabatic theorem [13]. Since each gate operation
involves a certain amount of noise and QAOA is an hybrid quantum-classical algorithm which requires an outer loop classical
optimization to assign angle parameters, it becomes more challenging to apply QAOA with high-depth. To reduce the circuit
depth in QAOA is of importance and interesting. There are different methods for such proposal, such as introducing digitized
counterdiabatic technique [14, 15] into QAOA.
Here, we focus on improving the performance of original QAOA with low-depth. While low-depth QAOA may achieve
promising results for some problems [7], the optimization landscapes would become more nonconvex so that it tends to obtain
the local optimal solutions which plagues QAOA [16, 17]. Recently, the warm-starting algorithms [17–19] have been proposed
to tackle this issue. Especially, the classical Metropolis-Hastings algorithm has been utilized as a warm-start for VQE to avoid
the local minima convergence, due to its provable ergodicity and suitability for unnormalized probability distributions [17].
Moreover, for an ergodic, discrete-time Markov chain, the number of epochs required to reach a certain threshold of convergence
is analytically bounded by


2
1
√
τ ≤ 2 ln
,
(1)
Φ
αMC π ∗
where αMC = |S − π| is the distance between the Markov chain’s sampled distribution S and the true stationary distribution π,
π ∗ is the probability of the least likely (maximum energy) state of π, and Φ is the conductance of the Markov process [17, 20].
In other words, only a minimal increase of classical overhead is required to avoid the local minima convergence for QAOA with
no increase in the complexity of quantum circuit and the quantum overhead.
In this paper, we introduce a general method to obtain the Ising Hamiltonians for CCOPs and demonstrate its effectiveness in
dealing with the minimum weight vertex cover (MWVC) problem, the minimum vertex cover (MVC) problem and the maximal
independent set (MIS) problem as examples. We emphasize that the Ising Hamiltonian for the MWVC problem is obtained first
time through our method, and the obtained Ising Hamiltonians for the other two examples are in consistent with that discussed in
[11]. Moreover, we focus on the Metropolis-Hastings warm-starting algorithm for 1-depth QAOA. We first provide the analytic
form of the loss function for 1-depth QAOA applied to combinatorial optimization problems and then modify the proposal
distribution used in [17] to present the warm-starting algorithm discussed in this paper. The presented warm-starting algorithm
here is completely classical due to the analytic loss function, implying that the quantum overhead has been extensively reduced
with only a minimal increase of classical overhead.
The paper is structured as follows. In Sec. II, we introduce the method to obtain the Ising Hamiltonians for CCOPs and
demonstrate its effectiveness by using the MWVC, MVC and MIS problems as examples. In Sec. III, we briefly review QAOA
and provide the analytic form of the loss function for 1-depth QAOA applied to combinatorial optimization problems. Besides,
we also present the Metropolis-Hastings warm-starting algorithm for QAOA. In Sec. IV, we numerically illustrate the validity
of our approach by applying the QAOA to MWVC cases with different sizes and demonstrate the advantages of the MetropolisHastings warm-starting algorithm by using 30 randomly generated MVC cases. We discuss our results and conclude in Sec. V.
II.

THE ISING HAMILTONIANS FOR CCOPS

In this section, we study the Ising Hamiltonians for CCOPs, for which the constraint and the target function can be considered
as combinatorial optimization problems Pa and Pb , respectively. We assume that Pa and Pb are both minimization problems. This
assumption is general since maximization problems can be easily transformed to minimization problems. Thus, a CCOP can be
considered to find the optimal solution to the problem Pb in the constrained search space given by the optimal solutions of the
problem Pa .
The Ising Hamiltonians for combinatorial optimization problems without constraints can be easily obtained. Denote the Ising
Hamiltonians Ha and Hb for the problems Pa and Pb , respectively. Sequentially, the solution to the CCOP can be encoded

3
to the eigenstate corresponding to the minimum eigenvalue of Hb under the constraint that this eigenstate is the ground state
of Ha . Here, Ha and Hb can be considered to be positive semidefinite due to the fact that Ha and Hb are both diagonal in
the computational basis. Let v0 <v1 < · · · · · · <vna −1 and w0 <w1 < · · · · · · <wnb −1 denote the different eigenvalues of Ha and Hb ,
′
′
respectively. If v0 <0, one can set Ha = Ha − v0 I. Ha is obviously positive semidefinite. It can also be considered as the Ising
′
Hamiltonian for the problem Pa since it keeps the sorting position of the corresponding eigenvalues. Similarly, one can set Hb if
w0 <0. Below we always assume that Ha and Hb are both positive semidefinite.
We take the Ising Hamiltonian H prob for the CCOP to be the linear combination of Ha and Hb ,
H prob = aHa + bHb ,
(i)

(i)

(2)

(i)

where a ∈ R and b ∈ R. Denote |x1 ⟩ , |x2 ⟩ , · · · |xli ⟩ the orthogonal eigenstates corresponding to the eigenvalue wi of Hb . It
n
o
(0)
(0)
(n −1)
(n −1)
is easy to see that |x1 ⟩ , · · · |xl0 ⟩ , · · · , |x1 b ⟩ , · · · |xln b−1 ⟩ also forms the eigenstate space for Ha and H prob . Thus, we can
b
define
(i)

(i)

(i)

(i)

ei ≡ min{λ j | Ha |x j ⟩ = λ j |x j ⟩}.

(3)

j

For the convenience of illustration, we assume that the solution to the CCOP is unique. Setting o ≡ min{ j | e j = v0 }, we have
j

T heorem 1. Let Ha and Hb be the Ising Hamiltonians for the optimization problems Pa and Pb , respectively. Assume that the
upper bound U of wo − wi and the lower bound L of ei − v0 (or ei − eo ), i < o, can be obtained from the eigenspectrum analysis
of Ha and Hb . The Ising Hamiltonian H prob for the CCOP has the following form,
H prob = aHa + bHb ,

(4)

where a > 0, b > 0 and a > bU/L.
Proo f . By the definitions of wi , ei and o, we have
(i)

i f i < o and j = 1, · · · , li ,

(5)

(o)

existing k ∈ (1, · · · , lo ),
i f i > o.

(6)
(7)

λ j ≥ ei > v0 ,
λk = v0 ,
wi > wo ,

The inequality (5) indicates that the target state which encodes the solution to the CCOP is not one of the eigenstates correspond(o)
ing to the eigenvalue wi (i < o) of Hb , since they are not the ground states of Ha . Thus, it can be seen that the target state is |xk ⟩
with the help of equality (6) and inequality (7).
(o)
(o)
In order for that H prob is the Hamiltonian for the CCOP, |xk ⟩ needs to be the unique ground state of H prob . Since H prob |xk ⟩ =
(o)

(i)

(i)

(i)

(av0 + bwo ) |xk ⟩ and H prob |x j ⟩ = (aλ j + bwi ) |x j ⟩, it implies that
(i)

av0 + bwo <aλ j + bwi ,

(8)

where j = 1, · · · , li for i = 0, · · · , o − 1, o + 1, · · · , nb − 1 and j = 1, · · · , k − 1, k + 1, · · · , li for i = o.
(o)
For i = o, the inequality (8) is satisfied for any a > 0, since λ j > eo = v0 for j = 1, · · · , k − 1, k + 1, · · · , lo . When i > o, from
(i)

the inequality (7) and that λ j ≥ v0 the (8) holds for any a > 0 and b > 0. When i < o, (8) can be written as
a>b

wo − wi
ei − v0

(9)

(i)

by using the inequality (5), namely, λ j ≥ ei . Therefore, we obtain a > 0, b > 0 and a > bU/L. □
We illustrate the effectiveness of our theorem by typical problems below.
A.

THE ISING HAMILTONIAN FOR THE MVC PROBLEM

Let G = (V, E) be an undirected graph, where V is a set of vertices and E a set of edges, the edge is covered by a vertex set
S ⊆ V when this edge has at least one of its endpoint in S. The MVC problem is to find such a vertex set S with the smallest
number of vertices under the constraint that every edge of E must be covered. The constraint of the MVC problem can be
considered as the optimization problem Pa that searches for the vertex set with the smallest uncovered edges, and the target

4
function of the MVC problem can be considered as the optimization problem Pb that targets to find the vertex set with smallest
vertices. We denote the number of the vertices (edges) by n (m).
Let the binary bit zi denotes the ith vertex of G. zi is identified with spin down −1 when zi is included in the vertex set S,
n−1 1
otherwise, spin up +1. Similar to the idea introduced in [21], we can use Cv (z) = ∑i=0
2 (1 − zi ) to count the number of vertices
in S. The corresponding Ising Hamiltonian Hb has the form,
n−1

Hb = ∑ (1 − σi z )/2,

(10)

i=0

where σi z denotes that the standard Pauli operator Z acts on the ith spin.
With respect to the problem Pa , the edge < i, j > formed by the vertices zi and z j is not covered by S only when zi = +1 and
z j = +1. Inspired by the idea in [21], the quantity
Ce (z) = ∑ (zi z j + zi + z j + 1) /4

(11)

<i, j>

can be used to count the number of edges which are uncovered by the set S. Thus, the corresponding Ising Hamiltonian Ha is of
the form,
Ha = ∑ (σi z σ j z + σi z + σ j z + I) /4.

(12)

<i, j>

From the derivations in Appendix A, in this case we have
wo − wi = o − i, ei − ei+1 ≥ 1

(13)

eo−1 − eo ≥ 1,
eo−2 − eo = eo−2 − eo−1 + eo−1 − eo ≥ 2,
··· ,
ei − eo ≥ o − i,

(14)

for i < o. From ei − ei+1 ≥ 1, we have

where i < o. Thus, H prob = aHa + bHb can be considered as the Ising Hamiltonian for the MVC problem with a > 0, b > 0 and
o−i
a > o−i
b, namely, a > b > 0.
The Ising Hamiltonian for the MVC problem can be simplified as


a z z n−1
b a
H prob = ∑ σi σ j + ∑ − + di σiz ,
2 4
<i, j> 4
i=0

(15)

where a > b > 0, di denotes the degree of the ith vertex, and the global phase item has been discarded.

B.

The ISING HAMILTONIAN FOR THE MWVC PROBLEM

An important generalized version of the MVC problem is the MWVC problem, which targets to find such a vertex cover
S ⊆ V of minimum total weight under the same constraint as the MVC problem. Different from the graph discussed in Sec. II A,
the ith vertex of G related to the MWVC problem is associated with a weight αi . The MWVC problem is NP-hard and more
complicated than the MVC problem [22, 23].
The constraint in the MWVC problem can be considered as the optimization problem Pa discussed in Sec. II A, and the target
function can be considered as the optimization problem Pb that targets to find the vertex set with minimum total weight. Similar
to the discussion in Sec. II A, the Hamiltonians Ha and Hb for the problems Pa and Pb can be expressed as
Ha = ∑ (σi z σ j z + σi z + σ j z + I) /4,
<i, j>
n−1

αi
(1 − σi z ).
2
i=0

Hb = ∑

(16)

5
It is straightforward to verify that
n−1

n−1

wo − wi ≤ wnb −1 − w0 = ∑ αi − 0 = ∑ αi ,
i=0

i=0

(17)

ei − eo ≥ 1
for i < o. Therefore, we obtain the Ising Hamiltonian for the MWVC problem,


a
a z z n−1
b
H prob = ∑ σi σ j + ∑ − αi + di σi z ,
2
4
<i, j> 4
i=0

(18)


n−1
αi b > 0, and the global phase item has been discarded.
where a > ∑i=0
C.

THE ISING HAMILTONIAN FOR THE MIS PROBLEM

Given a graph G = (V, E), the MIS problem targets at finding an independent set S ⊆ V with the largest number of vertices,
where the independent set refers to the set with no edges between vertices.
The constraint of the MIS problem can be considered as the optimization problem Pa that searches for the vertex set S with
smallest edges, and the target function can be regarded as the optimization problem Pb that targets to find the vertex set S with
smallest vertices, where S denotes the vertex set V − S. The Hamiltonians Ha and Hb for the problems Pa and Pb can be easily
derived,
Ha = ∑ (σi z σ j z − σi z − σ j z + I) /4,
<i, j>

(19)

n−1

Hb = nI − ∑ (1 − σi z )/2.
i=0

For the MIS problem we still have the conclusions wo − wi = o − i and ei − eo ≥ o − i for i < o. The proof is similar to that given
in Appendix A.
Therefore, the Ising Hamiltonian for the MIS problem can be simplified as

n−1 
b a
a
− di σi z ,
H prob = ∑ σiz σ zj + ∑
(20)
4
<i, j> 4
i=0 2
where a > b > 0, and the global phase item has been discarded.
III.

STANDARD QAOA AND THE METROPOLIS-HASTINGS WARM-STARTING ALGORITHM

The longitudinal field Ising Hamiltonian has the form,
n−1

H prob (σ ) = − ∑ Ji j σiz σ zj − ∑ hi σiz ,
<i, j>

(21)

i=0

where < i, j > stands for the interaction between the ith and jth spins with strength Ji j , and hi represents the longitudinal
magnetic field acting on the ith spin. This Hamiltonian can be used to deal with the general combinatorial optimization problems.
A.

STANDARD QAOA

QAOA aims to find the ground state of the Hamiltonian (21) by minimizing the loss function
Fp (⃗γ, ⃗β ) = ⟨H prob ⟩ = ⟨⃗γ, ⃗β |H prob |⃗γ, ⃗β ⟩,

(22)

where ⃗γ = (γ1 , γ2 , · · · , γ p ), ⃗β = (β1 , β2 , · · · , β p ) and |⃗γ, ⃗β ⟩ is the p-depth QAOA ansatz wave function [6, 7],
|⃗γ, ⃗β ⟩ = e−iβ p Hx e−iγ p Hprob (· · · )e−iβ1 Hx e−iγ1 Hprob |+⟩⊗n ,

(23)

6
√
.
with Hx = ∑i σix and |+⟩ = |0⟩+|1⟩
2
T heorem 2. For the cases of Ji j = J, the analytic expression of F1 has the form,

F1 (γ1 , β1 )
n
J
= − ∑ sin (4β1 ) cos (2hi γ1 ) sin (−2Jγ1 ) cosdi −1 (2Jγ1 )
2 <i, j>
+ sin (4β1 ) cos (2h j γ1 ) sin (−2Jγ1 ) cosd j −1 (2Jγ1 )
+ sin2 (2β1 ) sin (2hi γ1 ) sin (2h j γ1 )
h
i
cosdi +d j −2 fi j −2 (2Jγ1 ) 1 + cos fi j (4Jγ1 )
+ sin2 (2β1 ) cos (2hi γ1 ) cos (2h j γ1 )
h
io
cosdi +d j −2 fi j −2 (2Jγ1 ) 1 − cos fi j (4Jγ1 )
n−1

+ ∑ hi sin 2β1 sin (2hi γ1 ) cosdi (2Jγ1 ),

(24)

i=0

where fi j is the number of spins that interact with both the ith and the jth spins.
The proof of Theorem 2 is given in Appendix B by using the Pauli Solver algorithm [24]. Notice that this Theorem is a special
case of the work in [25]. However, the proof of Theorem 2 in this paper adopts the Pauli Solver algorithm which only utilizes the
commutation relations of the Pauli matrices. The relevant calculation can be easily computed in a classical computer by realizing
symbolized multiplication rules for Pauli matrices. The angles (⃗γ, ⃗β ) can be restricted to the compact set [0, 2π] p × [0, π] p when
Ji j ∈ Z and hi ∈ Z [6]. In principle the analytic form of the loss function for QAOA with any depth can be obtained in a similar
way.
B.

QAOA WITH THE METROPOLIS-HASTINGS WARM-STARTING ALGORITHM

Inspired by the application of classic Metropolis-Hastings techniques to VQE [17], we present the Metropolis-Hastings warmstarting algorithm for QAOA in this section. The Metropolis-Hastings method has particularly useful advantages on sampling
in high-dimensional spaces. Its provable ergodicity guarantees that all samples of the distributions are eventually sampled in a
statistically representative way, regardless of which initial angle parameter is chosen [20, 26, 27].
The QAOA with Metropolis-Hastings warm-starting algorithm contains two parts: (i) choosing the optimal parameters
(⃗γ ∗ , ⃗β ∗ ) from Algorithm 1 (see below) as the initial parameters for standard QAOA; (ii) completing the optimization with a
closing sequence of standard QAOA epochs.
Before presenting the Metropolis-Hastings warm-starting algorithm for QAOA with any depth p, we first define the Boltzmann
distribution


P(⃗γ a , ⃗β a ) ∝ exp −αFp (⃗γ a , ⃗β a ) ,
(25)
where α > 0. From (25), we can see that the probability of the parameter sample increases exponentially with the decrease of
the corresponding loss function. To avoid a gradient of zero that causes the parameters to stop updating during the Metropolis⃗ ′ to be of the following form,
Hastings warm-starting process, we select the candidate parameter γ⃗ ′ and β
γ ′i = γi − η∂γi Fp (⃗γ, ⃗β ) + ξ Θt ,
β ′ = βi − η∂ Fp (⃗γ, ⃗β ) + ξ Θt ,
i

βi

(26)
(27)

where xi denotes the ith component of ⃗x, and we have added a normally distributed random noise term Θr ∼ N (0, 1) with scale
parameter ξ (see Algorithm 1 for more detail). The analytic gradient of the loss function can be easily computed classically by
assuming that the analytic expression for Fp can be computed. Thus the proposal distribution can be defined as
p

′
′
′
′
G(⃗γ , ⃗β |⃗γ, ⃗β ) = ∏ g(γi |γi )g(βi |βi ),

i=1

where


′
′
g(γi |γi ) = pdf N (η∂γi Fp , ξ 2 ) (γi − γi ),


′
′
g(βi |βi ) = pdf N (η∂βi Fp , ξ 2 ) (βi − βi ).

(28)

7
Here, we emphasize that the warm-starting algorithm presented here is completely classical, as a result of the analytic expression
for loss function. Hence, it is more efficient than the warm-starting algorithm introduced in [17].
To illustrate the reasonability and effectiveness of the proposal distribution (28), we note that the Markov chain with this
⃗ ′ ,⃗γ, ⃗β ,
proposal distribution is strongly irreducible, since for all γ⃗ ′ , β
⃗ ′ |⃗γ, ⃗β )
G(γ⃗ ′ , β
−(γi − γ ′i − η∂γi Fp )2 − (βi − βi′ − η∂βi Fp )2
1
exp[
]>0
2
2ξ 2
i=1 2πξ
p

=∏

is satisfied for proper ξ . The proof is similar to that given in [17]. Thus, the resulting Markov chain is provably ergodic, implying
that the parameters near the global minima can be necessarily sampled after some epoches. When Fp has analytic expressions,
the calculation error of the numerical gradient descent considered in [17] can be removed, which gives rise to the proposal
distribution presented here.
Note that the resulting Markov chain is still provably ergodic and can also effectively sample the parameters near the global
minima when the loss function is numerically calculated with small estimation error. Therefore, the proposal distribution (28) is
still suitable for QAOA with any depth even the analytic loss function cannot be computed. When the loss function has analytic
expressions, the warm-starting algorithm presented is completely classical, namely, this algorithm does not involve any quantum
overhead. Nevertheless, each iteration of the warm-starting algorithm uses the same amount of quantum resources as that used
in each iteration of the standard QAOA when the loss function is numerically estimated.
Algorithm 1: The Metropolis-Hastings warm-starting algorithm
Input

: (⃗γ 0 , ⃗β 0 ): the initial parameters;

P(⃗γ, ⃗β ): the Boltzmann distribution used in the Metropolis-Hastings process;
Tmax : the maximum number of Markovian epochs;
⃗ ′ |⃗γ, ⃗β ): the proposal distribution in the Metropolis-Hastings process;
G(γ⃗ ′ , β
η: the learning rate in gradient descent;
ξ : the scale parameter of noise added in gradient descent;
Output: (⃗γ ∗ , ⃗β ∗ ): the parameters corresponding to the minimal value of the loss function during the Markovian epochs;
1 set t = 0, ⃗
γ

∗ =⃗
γ 0 , ⃗β ∗ = ⃗β 0 ;

2 while t < T do
3

4
5
6
7
8
9
10
11
12
13
14
15
16

generate a noise term Θt from the normal distribution N (0, 1);
⃗′
// the ith components of proposal candidate parameters γ⃗ ′ and β
γ ′i = γit − η∂γi Fp + ξ Θt ;
βi′ = βit − η∂βi Fp + ξ Θt ;


⃗ ′ )G(⃗γ t ,⃗β t |γ⃗ ′ ,β
⃗ ′)
P(γ⃗ ′ ,β
compute the accept rate: A = min 1,
;
t ⃗t
⃗′ ⃗ ′ t ⃗ t
P(⃗γ ,β )G(γ ,β |⃗γ ,β )

generate a sample u from uniform distribution U(0, 1);
if u ≤ A then
γit+1 = γ ′i ;
βit+1 = βi′ ;
if P(⃗γ t+1 , ⃗β t+1 ) > P(⃗γ ∗ , ⃗β ∗ ) then
⃗γ ∗ = ⃗γ t+1 , ⃗β ∗ = ⃗β t+1 ;
else
⃗γ t+1 = ⃗γ t ;
⃗β t+1 = ⃗β t ;
t = t + 1;

IV.

EXPERIMENTAL SECTION

In this section, the standard QAOA was applied on the MWVC cases to numerically demonstrate the validity and effectiveness
of Theorem 1. Besides, the behavior of the 1-depth QAOA was also compared with and without the Metropolis-Hastings warmstarting algorithm by using 30 randomly generated MVC cases.

8
A.

THE PERFORMANCE OF QAOA ON THE MWVC CASES

The performance of QAOA implemented on the MWVC cases was analyzed with different sizes based on the Ising Hamiltonians obtained through Theorem 1. The number of the MWVC cases for each size was selected to be 10 and the cases were
generated from the graphs which were all randomly drawn from Erdös-Rényi ensemble with edge probability 0.5. In order to
avoid slow convergence caused by overlarge loss function value, we randomly generate numbers from 0 to 3 per size as the
weight values of vertices. This process of randomly generating weights was general since the solution to the MWVC problem
was the same when the weight values were all multiplied by a positive number. Here, 20 initial angle parameters were selected, which were randomly generated from [−π, π] p × [−π, π] p and the QAOA was executed, respectively, to get the optimal
approximate solution. b = 0.5 and a = (∑n−1
i=0 αi )b + 0.1 was chosen for the Ising Hamiltonian to the MWVC cases.
Brute-force strategy was adopted to obtain the exact solutions for the MWVC cases and the correct solution probability for
each size of the MWVC cases was then computed by executing standard QAOA. Here, the correct solution probability for each
size refers to the average correct solution probability for 10 MWVC cases with the same size. As shown in Figure 1, the correct
solution probabilities all raise with the increase of depth. Correspondingly, the loss function values all decrease with the increase
of depth (see Figure 2). Moreover, it could be observed that the correct solution probabilities decrease with the increase of the
problem size at the same depth which also conforms to the search space characteristics of QAOA.
1
Size = 2
Size = 3
Size = 4
Size = 5
Size = 6
Size = 7
Size = 8

Correct solution probability

0.8

0.6

0.4

0.2

0
1

2

3

4

5

6

Depth

FIG. 1. Correct solution probabilities obtained by implementing standard QAOA on the MWVC cases with different sizes. For the sizes argued
here, the correct solution probabilities all raise with the increase of depth.

-2.1

-1.8

Loss Value

-1.5

-1.2

-0.9
Depth = 1
Depth = 3
Depth = 3
Depth = 4
Depth = 5
Depth = 6

-0.6

-0.3

0
2

3

4

5

6

7

8

Size of MWVC

FIG. 2. The loss function values obtained by implementing standard QAOA on the MWVC cases with different sizes. The solid blue line
represents the loss function values at the exact solutions. For the sizes argued here, the loss function values all decrease with the increase of
depth.

B.

THE PERFORMANCE OF THE METROPOLIS-HASTINGS WARM-START IMPLEMENTED TO QAOA

In this section, the performance of the Metropolis-Hastings warm-starting algorithm was demonstrated by analyzing the
average loss function values of QAOA with and without warm-start for 30 MVC cases.

9
To select the cases for which the 1-depth QAOA tends to obtain the local optimal solutions with high probabilities, we first
analyze the performance of 1-depth QAOA without warm-start on the graphs randomly generated from Erdös-Rényi ensemble
with different edge probabilities, respectively. The number of the MVC cases for each edge probability was selected to be 20.
From Figure 3, it could be observed that the average probability that 1-depth QAOA without warm-start converges to the local
minima was larger than 50% when the graphs were generated from Erdös-Rényi ensemble with edge probability ≥ 0.6. Here, the
global minima was considered as the minima obtained by executing 1-depth QAOA with 20 initial angle parameters randomly
generated from [0, 2π] p × [0, π] p , respectively. Moreover, it could be easily verified that the number of non-isotropic graphs
was small when the ratio of the number of edges to the number of vertices was too large or too small. Thus, we consider the
MVC cases generated from 30 graphs with ten vertices which were randomly drawn from the Erdös-Rényi ensemble with edge
probability= 0.6.
In order to show the relation between the initial angle parameters and converging to the global minima, we randomly choose
10 initial angle parameters from [0, 2π] p × [0, π] p to execute QAOA with and without Metropolis-Hastings warm-start algorithm,
respectively. Here, we set a = 2 and b = 1 for the Ising Hamiltonian to the MVC cases. The maximum number of MetropolisHastings epochs Tmax , the parameter α in the Equation (25), the parameter ξ in (26) and (27), and the learning rate η were
chosen to be 600, 0.5, 0.4, and 0.1, respectively. For the 30 MVC cases considered here, the mean of the loss function value
samples for the 10 initial angle parameters is shown in Figure 4(a) and the variance is shown in Figure 4(b).
From Figure 4, we see that whether the QAOA without the Metropolis-Hastings warm-start could reach the global minima
depends highly on the selection of the initial angle parameters and was irrelevant to the number of optimization iterations.
Sequentially, we need to execute the standard QAOA multiple times with different initial angle parameters to get the global
optimal results which leads to much quantum overhead.
However, for the QAOA with the Metropolis-Hastings warm-start, it could be seen that the influence of initial angel parameters
on the converging results was subtle (see Figures 4(b) and 5). In order words, it could always reach the global minima for any
randomly generated angle parameters even with low optimization iterations. Therefore, it could dramatically reduce the quantum
overhead with the help of Metropolis-Hastings warm-starting algorithm since this warm-starting algorithm was completely
classical.
The probability of obtaining local minima

0.8
0.7
0.6
0.5
0.4
0.3
0.2
0.1
0
0

0.1

0.2

0.3

0.4

0.5

0.6

0.7

0.8

0.9

1

The probability of generating edges

FIG. 3. The probabilities of obtaining the local minima when implementing 1-depth QAOA without warm-start on the MVC cases randomly
generated from Erdös-Rényi ensemble with different edge probabilities. The probability of being trapped in local minima is large than 50%
when the edge probability ≥ 0.6.

V.

CONCLUSION

We have provided a general method to obtain the Ising Hamiltonians for the CCOPs. In order to show the effectiveness of
our method, we have derived the Ising Hamiltonians for the MWVC, MVC and MIS problems. The Ising Hamiltonians for the
MVC and MIS problems obtained through our method have the same form as that discussed in [11], while the Ising Hamiltonian
for the MWVC problem, which is more complicated than the MVC problem, is obtained first time.
We have also applied QAOA to the MWVC cases with different sizes to show the validity and effectiveness of our method
numerically. The numerical experiments show that the correct solution probabilities all raise with the increase of depth for the
sizes considered in this paper. Correspondingly, the values of loss function all decrease with the increase of the depth. Moreover,
it is observed that the correct solution probability decreases with the increase of the problem size for the same depth, which also
conforms to the search space characteristics of QAOA.
For the longitudinal field Ising Hamiltonians, which can be used to describe general combinatorial optimization problems as
well as other problems such as many-body quantum system problems [5], we have provided the analytic form of the loss function

-12
-11
-10
-9
-8
-7
-6
-5
-4
-3
-2
-1
0
1
2
3
4

60

8
7
6
5
4
3
2
1
0

55
50

Variance of Loss Value

Average Loss Value

10

45
40
35
30

0

3

6

9

25

12

15

18

21

24

27

30

70

80

90

100

Optimization Iterations

20
15
10
5

0

10

20

30

40

50

60

70

80

90

100

0
0

Optimization Iterations

10

20

30

40

50

60

Optimization Iterations

(a)

(b)

FIG. 4. The mean and variance of loss function value of 30 MVC cases for 10 randomly generated initial angle parameters. The solid lines
show the numerical results of 1-depth QAOA with warm-start, while the dotted lines represent the numerical results of 1-depth QAOA without
warm-start. The numerical results of 1-depth QAOA with and without warm-start for one MVC case adopt the same color. a) The relation
between the average loss function value and the optimization iterations for QAOA with and without Metropolis-Hastings warm-start. b) The
relation between the variance of loss function value samples and the optimization iterations for QAOA with and without Metropolis-Hastings
warm-start.

30
-9
-8

QAOA with Metropolis-Hastings warm-start
1

Average Loss Value

-7

Standard QAOA

27
1

Average variance of Loss Value

Standard QAOA

-6
-5
-4
-3
-2
-1

1

QAOA with Metropolis-Hastings warm-start
1

24
21
18
15
3.5
3
2.5
2
1.5
1
0.5
0

12
9
6

0

3

1

0

0

2

4

6

8

10

12

14

16

18

20

Optimization Iterations
0

10

20

30

40

50

60

70

80

90

100

0

10

Optimization Iterations

(a)

20

30

40

50

60

70

80

90

100

Optimization Iterations

(b)

FIG. 5. The average mean and variance of loss function value for 30 MVC cases. a) The relation between the average loss function value
and the optimization iterations for QAOA with and without Metropolis-Hastings. b) The relation between the variance of loss function value
samples and the optimization iterations for QAOA with and without Metropolis-Hastings warm-start.

for 1-depth QAOA. Theoretically, the analytic form of the loss function for QAOA with any depth implemented on longitudinal
field Ising Hamiltonians can be obtained by using the Pauli Solver algorithm [24]. Thus, the analytic form of gradient can be
obtained classically, leading to more efficient execution of optimization iterations.
Based on the analytic form of the loss function, we have presented the Metropolis-Hastings warm-starting algorithm for
QAOA to obtain the global, rather than local, minima which does not depend on the choice of the initial angle parameters. This
warm-starting algorithm is especially efficient for low-depth QAOA as the optimization landscapes become more nonconvex
with low-depth.
We emphasize that the warm-starting algorithm discussed here is completely classical, implying that the quantum overhead
has been extensively reduced, only with a minimal increase of classical overhead. We have also numerically analyzed the
performance of the Metropolis-Hastings warm-starting algorithm for QAOA with depth p = 1. The numerical experiments show
that it can always reach the global minima for any randomly generated angle parameters even with low optimization iterations,
while whether the QAOA without the Metropolis-Hastings warm-start can reach global minima depends highly on the selection
of initial angle parameters, which can not be improved by increasing the number of optimization iterations.

ACKNOWLEDGMENTS

This work was supported by the NSFC (grant nos. 12075159 and 12171044), Beijing Natural Science Foundation (Z190005),
and Academician Innovation Platform of Hainan Province.

11
Appendix A: Proof of (13) in Sec. II A

It is straightforward to see that the eigenvalues of Hb are given by 0, 1, · · · , n. Thus, the conclusion that wo − wi = o − i is
obvious. Here, we focus on the proof of ei − ei+1 ≥ 1 for i < o below.
Without loss of generality, we assume
(i)

(i)

Ha |x p ⟩ = ei |x p ⟩ ,
where p ∈ (1, · · · , li ). Since σ z |0⟩ = +1 |0⟩ and σ z |1⟩ = −1 |1⟩, the jth quantum bit state |0⟩ indicates that the jth vertex of
G is not included in the vertex set S, while the quantum bit state |1⟩ indicates that the jth vertex of G is included in S. From
ei > v0 = 0, one has that there exists at least one edge, denoted as < k, l >, which is not covered by the vertex set S corresponding
(i)
(i)
to quantum state |x p ⟩. Thus, the kth and lth quantum bit states of |x p ⟩ are both |0⟩.
(i)

Next, we set |y⟩ = |x p ⟩ except for that the kth quantum bit of |y⟩ is flipped to |1⟩. The vertex set generated by |y⟩ is denoted
as Sy and the number of edges uncovered by Sy is denoted as λy . We can see that the number of vertices included in Sy is i + 1 and
λy ≤ ei − 1. In other words, we have Hb |y⟩ = (i + 1) |y⟩ = wi+1 |y⟩ and Ha |y⟩ = λy |y⟩, where λy ≤ ei − 1. By the definition 3,
we obtained that ei+1 ≤ λy ≤ ei − 1, namely, ei − ei+1 ≥ 1.

Appendix B: Proof of Theorem 2

We prove the Theorem 2 by using the Pauli Solver algorithm introduced in [24]. It is straightforward to get that
F1 (γ1 , β1 )
= ⟨+|⊗n eiγ1 Hprob eiβ1 Hx (H prob )e−iβ1 Hx e−iγ1 Hprob |+⟩⊗n
= −J ∑ ⟨+|⊗n eiγ1 Hprob eiβ1 Hx (Zu Zv ) e−iβ1 Hx e−iγ1 Hprob |+⟩⊗n
<u,v>

n−1

− ∑ hu ⟨+|⊗n eiγ1 Hprob eiβ1 Hx (Zu ) e−iβ1 Hx e−iγ1 Hprob |+⟩⊗n
u=0

n−1

= −J ∑ ⟨Zu Zv ⟩ − ∑ hu ⟨Zu ⟩,
<u,v>

(B1)

u=0

where Zu = σuz . Let Quv = eiγ1 Hprob eiβ1 Hx Zu Zv e−iβ1 Hx e−iγ1 Hprob and Qu = eiγ1 Hprob eiβ1 Hx Zu e−iβ1 Hx e−iγ1 Hprob . In order to solve
⟨Zu Zv ⟩ and ⟨Zu ⟩ through the Pauli Solver algorithm, we first write
n−1

Quv = a0 I + ∑

∑

alσ σl + ∑

∑

alkσ λ σl λk + . . . ,

∑

blσ σl + ∑

∑

blkσ λ σl λk + . . . ,

l=0 σ =X,Y,Z

l̸=k σ ,λ =X,Y,Z

n−1

Qu = b0 I + ∑

l=0 σ =X,Y,Z

(B2)

l̸=k σ ,λ =X,Y,Z

where aα ∈ R, bα ∈ R and X{Y, Z}i represents the Pauli matrix X{Y, Z} acting on the ith spin. Using ⟨+| I |+⟩ = ⟨+| X |+⟩ = 1
and ⟨+|Y |+⟩ = ⟨+|Z |+⟩ = 0, we have
⟨Zu Zv ⟩ = ⟨γ1 , β1 | Zu Zv |γ1 , β1 ⟩ = ⟨+|⊗n Quv |+⟩⊗n
n−1

= a0 + ∑ alX + ∑ alkXX + · · · ,
l=0

l̸=k

⟨Zu ⟩ = ⟨γ1 , β1 | Zu |γ1 , β1 ⟩ = ⟨+|⊗n Qu |+⟩⊗n
n−1

= b0 + ∑ blX + ∑ blkXX + · · · .
l=0

l̸=k

(B3)

12
To prove Theorem 2, we first introduce the following relations:
σu ∏ eiJγ1 Zu Zk = ∏ e−iJγ1 Zu Zk σu ,

(B4)

σu Zv eiJγ1 Zu Zv = e−iJγ1 Zu Zv σu Zv ,

(B5)

<u,k>

<u,k>

σu σv e
σu Zv

iJγ1 Zu Zv
iJγ1 Zu Zl

=e
=

∏

e

∏

eiJγ1 Z j Zv =

∏

eiJγ1 Zu Zl =

∏

eiJγ1 Z j Zv =

<u,l>,l̸=v

σu Zv

−iJγ1 Zu Zl

(B6)

∏

e

σu Zv ,

(B7)

∏

eiJγ1 Z j Zv σu Zv ,

(B8)

∏

e−iJγ1 Zu Zl σu Zv ,

(B9)

∏

e−iJγ1 Z j Zv σu Zv ,

(B10)

< j,v>, j̸=u

<u,l>,l̸=v

σu σv

σu σv ,

<u,l>,l̸=v

< j,v>, j̸=u

σu σv

iJγ1 Zu Zv

<u,l>,l̸=v

< j,v>, j̸=u

< j,v>, j̸=u

where σu denotes the Pauli operators X or Y acting on the uth spin. These relations can be proved straightforwardly by using the
properties of Pauli matrices X, Y and Z. Here, we prove (B10) as an example. Since [X, Z] = −[Z, X], [Y, Z] = −[Z,Y ], we have
σu σv eiJγ1 Z j Zv = σu σv (cos (Jγ1 ) + i sin (Jγ1 )Z j Zv )
= (cos (Jγ1 ) − i sin (Jγ1 )Z j Zv ) σu σv
= e−iJγ1 Z j Zv σu σv ,

(B11)

where j ̸= u. Thus (B10) is proved by repeating the process (B11) for different j.
−iβ1 Xl and Z e−iβ1 Xu = eiβ1 Xu Z , we have
Now we prove the Theorem 2 by computing ⟨Zu ⟩ and ⟨Zu Zv ⟩. Since e−iβ1 Hx = ∏n−1
u
u
l=0 e
eiβ1 Hx Zu e−iβ1 Hx = e2iβ1 Xu Zu
= sin (2β1 )Yu + cos (2β1 )Zu .

(B12)

Since Zu in the second term commutes with e−iγ1 Hprob , it does not contribute to ⟨Zu ⟩.
For Yu in the first term in (B12), it is straightforward to verify that
n−1

n−1

l=0

l=0

∏ e−iγ1 hl Zl (Yu ) ∏ eiγ1 hl Zl = e−iγ1 hu Zu (Yu ) eiγ1 hu Zu
= e−2iγ1 hu Zu (Yu )
= sin (−2hu γ1 )Xu + cos (2hu γ1 )Yu .

(B13)

With the help of (B4), we have

∏ e−iJγ1 Z j Zk (σu ) ∏ eiJγ1 Z j Zk

< j,k>

< j,k>

−iJγ1 Zu Zk

= ∏ e
<u,k>

(σu ) ∏ eiJγ1 Zu Zk
<u,k>

−2iJγ1 Zu Zk

= ∏ e

(σu ) .

(B14)

<u,k>

Since

∏ e−2iJγ Z Z (Xu ) = ∏ [cos (2Jγ1 ) − i sin (2Jγ1 )Zu Zk ] (Xu ) ,
1 u k

<u,k>

(B15)

<u,k>

the only term which contributes to the expectation value ⟨Zu ⟩ is cosdu (2Jγ1 )Xu in the expanded right hand side.
Similarly, since

∏ e−2iJγ Z Z (Yu ) = ∏ [cos (2Jγ1 ) − i sin (2Jγ1 )Zu Zk ] (Yu ) ,
1 u k

<u,k>

(B16)

<u,k>

the right hand side of (B16) does not contribute to ⟨Zu ⟩. Thus, we have
⟨+|⊗n eiγ1 Hprob Yu e−iγ1 Hprob |+⟩⊗n = sin(−2hu γ1 ) cosdu (2Jγ1 ).

(B17)

13
Combining (B17) and (B12), we have
⟨Zu ⟩ = ⟨+|⊗n eiγ1 Hprob eiβ1 Hx Zu e−iβ1 Hx e−iγ1 Hprob |+⟩⊗n
= sin(2β1 ) sin(−2hu γ1 ) cosdu (2Jγ1 ).

(B18)

Corresponding to (B12), we have
eiβ1 Hx Zu Zv e−iβ1 Hx = e2iβ1 Xu e2iβ1 Xv Zu Zv
1
= sin2 (2β1 )YuYv + sin (4β1 )(Yu Zv + ZuYv )
2
+ cos2 (2β1 )Zu Zv ,

(B19)

by taking into the the fact that Zu Zv e−iβ1 Xu e−iβ1 Xv = eiβ1 Xu eiβ1 Xv Zu Zv . The term Zu Zv commutes with e(−iγ1 Hprob ) and thus does
not contribute to ⟨Zu Zv ⟩.
For the term YuYv in (B19), it is straightforward to verify that
n−1

n−1

l=0

l=0
−iγ1 hu Zu −iγ1 hv Zv

∏ e−iγ1 hl Zl (YuYv ) ∏ eiγ1 hl Zl
=e

(YuYv ) eiγ1 hv Zu eiγ1 hu Zv

e

= e−2iγ1 hu Zu e−2iγ1 hv Zv (YuYv )
= sin(2hu γ1 ) sin(2hv γ1 )Xu Xv
+ cos(2hu γ1 ) sin(−2hv γ1 )Yu Xv
+ sin(−2hu γ1 ) cos(2hv γ1 )XuYv
+ cos(2hu γ1 ) cos(2hv γ1 )YuYv ,

(B20)

by using the fact Y j eiγ1 h j Z j = e−iγ1 h j Z j Y j .
Similarly, for the terms Yu Zv and ZuYv in (B19), we have
n−1

n−1

∏ e−iγ1 hl Zl (Yu Zv ) ∏ eiγ1 hl Zl

l=0

l=0
−iγ1 hu Zu −iγ1 hv Zv

=e

e

(Yu Zv ) eiγ1 hu Zu eiγ1 hv Zv

= e−2iγ1 hu Zu (Yu Zv )
= sin(−2hu γ1 )Xu Zv + cos(2hu γ1 )Yu Zv ,
n−1

(B21)

n−1

∏ e−iγ1 hl Zl (ZuYv ) ∏ eiγ1 hl Zl

l=0

=e

l=0
−iγ1 hu Zu −iγ1 hu Zv

e

(ZuYv ) eiγ1 hu Zu eiγ1 hv Zv

= e−2iγ1 hv Zv (ZuYv )
= sin(−2hv γ1 )Zu Xv + cos(2hv γ1 )ZuYv .

(B22)

With respect to the term Xu Zv in (B21), by using (B5), (B7) and (B8) we obtain

∏ e−iJγ1 Z j Zk (Xu Zv ) ∏ eiJγ1 Z j Zk

< j,k>

=e

< j,k>

−iJγ1 Zu Zv

∏

∏

e−iJγ1 Zu Zl

∏

e−iJγ1 Z j Zv (Xu Zv )

<u,l>,l̸=v

< j,v>, j̸=u

iJγ1 Z j Zv

iJγ1 Zu Zl iJγ1 Zu Zv

e

< j,v>, j̸=u

= e−2iJγ1 Zu Zv

∏

e

e

<u,l>,l̸=v

∏

e−2iJγ1 Zu Zl (Xu Zv )

<u,l>,l̸=v

= [cos(2Jγ1 ) − i sin(2Jγ1 )Zu Zv ]

∏

<u,l>,l̸=v

[cos(2Jγ1 ) − i sin(2Jγ1 )Zu Zl ] (Xu Zv ) ,

(B23)

14
Expanding the product on the right hand side above gives rise to the sum of tensor products of Pauli operators. Clearly, no term
contributes to the expectation value ⟨Zu Zv ⟩, namely,
⟨+|⊗n ∏ e−iJγ1 Z j Zk (Xu Zv ) ∏ eiJγ1 Z j Zk |+⟩⊗n = 0.

(B24)

⟨+|⊗n ∏ e−iJγ1 Z j Zk (Zu Xv ) ∏ eiJγ1 Z j Zk |+⟩⊗n = 0.

(B25)

< j,k>

< j,k>

This implies by symmetry that

< j,k>

< j,k>

Concerning the term Yu Xv in (B20), we have from (B6), (B9) and (B10),

∏ e−iJγ1 Z j Zk (Yu Xv ) ∏ eiJγ1 Z j Zk

< j,k>

< j,k>

−iJγ1 Zu Zv

=e

∏

=

e−iJγ1 Z j Zv (Yu Xv )

∏

<u,l>,l̸=v

< j,v>, j̸=u

iJγ1 Z j Zv

iJγ1 Zu Zl iJγ1 Zu Zv

∏

e

∏

e−2iJγ1 Zu Zl

<u,l>,l̸=v

< j,v>, j̸=u

∏

[cos(2Jγ1 − i sin(2Jγ1 ))Zu Zl ]

∏

[cos(2Jγ1 − i sin(2Jγ1 ))Z j Zv ] (Yu Xv ) .

< j,v>, j̸=u

=

e−iJγ1 Zu Zl
e

∏

e

<u,l>,l̸=v

e−2iJγ1 Z j Zv (Yu Xv )

∏

<u,l>,l̸=v

(B26)

< j,v>, j̸=u

Expanding the product on the right hand side above, one has the sum of tensor products of Pauli operators. Thus, we see that no
terms contribute to the expectation value ⟨Zu Zv ⟩, namely,
⟨+|⊗n ∏ e−iJγ1 Z j Zk (Yu Xv ) ∏ eiJγ1 Z j Zk |+⟩⊗n = 0.

(B27)

⟨+|⊗n ∏ e−iJγ1 Z j Zk (XuYv ) ∏ eiJγ1 Z j Zk |+⟩⊗n = 0.

(B28)

< j,k>

< j,k>

By symmetry, this implies that

< j,k>

< j,k>

Therefore, we have
⟨+|⊗n ∏ e−iJγ1 Z j Zk (Yu Zv ) ∏ eiJγ1 Z j Zk |+⟩⊗n
< j,k>

< j,k>

du −1

= sin(−2Jγ1 ) cos
⊗n

⟨+|

∏e

−iJγ1 Z j Zk

< j,k>

(2Jγ1 ),

(B29)
iJγ1 Z j Zk

(ZuYv ) ∏ e

⊗n

|+⟩

< j,k>

= sin(−2Jγ1 ) cosdv −1 (2Jγ1 ),
⊗n

⟨+|

∏e

< j,k>

=

−iJγ1 Z j Zk

(YuYv ) ∏ e

(B30)
iJγ1 Z j Zk

⊗n

|+⟩

< j,k>


1
cos(du +dv −2 f −2) (2Jγ1 ) 1 − cos f (4Jγ1 ) .
2

(B31)

15
From (B6), (B9) and (B10) we have for the term Xu Xv ,

∏ e−iJγ1 Z j Zk (Xu Xv ) ∏ eiJγ1 Z j Zk
< j,k>

< j,k>

−iJγ1 Zu Zv

=e

∏

e−iJγ1 Zu Zl

<u,l>,l̸=v

eiJγ1 Z j Zv

∏

< j,v>, j̸=u

=
=

−2iJγ1 Zu Zl

∏

e−iJγ1 Z j Zv (Xu Xv )

< j,v>, j̸=u

∏

eiJγ1 Zu Zl eiJγ1 Zu Zv

∏

e−2iJγ1 Z j Zv (Xu Xv )

<u,l>,l̸=v

∏

e

<u,l>,l̸=v

< j,v>, j̸=u

∏

[cos(2Jγ1 ) − i sin(2Jγ1 )Zu Zl ]

∏

[cos(2Jγ1 ) − i sin(2Jγ1 )Z j Zv ] (Xu Xv ) .

<u,l>,l̸=v

(B32)

< j,v>, j̸=u

In this case, in order for that only operators I or X act on the uth and vth spins, an even number of spins are required to interact
both the uth and the vth spins. In other words, only the expanded terms (Zu Zl1 ) ∗ · · · ∗ (Zu Zl2 j ) ∗ (Zl1 Zv ) ∗ · · · ∗ (Zl2 j Zv ) ∗ (Xu Xv )
contribute to the expectation value ⟨Zu Zv ⟩, where j = 0, 1, · · · . Thus, we have
⟨+|⊗n ∏ e−iJγ1 Z j Zk (Xu Xv ) ∏ eiJγ1 Z j Zk |+⟩⊗n
< j,k>

< j,k>

 
 
f
f
=
cosdu +dv −2 (2Jγ1 ) +
cosdu +dv −2−4 (2Jγ1 ) sin4 (2Jγ1 ) + · · ·
0
2
 h
f
i f −i h
ii
f
cos2 (2Jγ1 )
sin2 (2Jγ1 )
= cosdu +dv −2−2 f (2Jγ1 ) ∑
i=0,2,··· i


1
= cosdu +dv −2 f −2 (2Jγ1 ) 1 + cos f (4Jγ1 ) .
2

(B33)

Accounting to that
f

 
f
1
∑ i a f −i bi = 2 ((a + b) f + (a − b) f ),
i=0,2,...
we get
1
sin(4β1 ) cos(2hu γ1 ) sin(−2Jγ1 ) cosdu −1 (2Jγ1 )
2
+ sin(4β1 ) cos(2hv γ1 ) sin(−2Jγ1 ) cosdv −1 (2Jγ1 )

⟨Zu Zv ⟩ =

+ sin2 (2β1 ) cos(2hu γ1 ) cos(2hv γ1 ) cos(du +dv −2 f −2) (2Jγ1 )

· 1 − cos f (4Jγ1 )
+ sin2 (2β1 ) sin(2hu γ1 ) sin(2hv γ1 ) cos(du +dv −2 f −2) (2Jγ1 )

· 1 + cos f (4Jγ1 ) .

(B34)

With all the above discussions, we complete the proof.

[1] A. Das and B. K. Chakrabarti, Colloquium: Quantum annealing and analog quantum computation, Rev. Mod. Phys. 80, 1061 (2008).
[2] E. Farhi, J. Goldstone, S. Gutmann, J. Lapan, A. Lundgren, and D. Preda, A Quantum Adiabatic Evolution Algorithm Applied to Random
Instances of an NP-Complete Problem, Science 292, 472 (2001).
[3] V. Mehta, F. Jin, H. De Raedt, and K. Michielsen, Quantum annealing with trigger Hamiltonians: Application to 2-satisfiability and
nonstoquastic problems, Phys. Rev. A 104, 032421 (2021).
[4] R. Barends, A. Shabani, L. Lamata, J. Kelly, A. Mezzacapo, U. L. Heras, R. Babbush, A. G. Fowler, B. Campbell, Y. Chen, et al.,
Digitized adiabatic quantum computing with a superconducting circuit, Nature 534, 222 (2016).
[5] P. Chandarana, N. N. Hegade, K. Paul, F. Albarrán-Arriagada, E. Solano, A. del Campo, and X. Chen, Digitized-counterdiabatic quantum
approximate optimization algorithm, Phys. Rev. Research 4, 013141 (2022).

16
[6] E. Farhi, J. Goldstone, and S. Gutmann, A Quantum Approximate Optimization Algorithm, arXiv:1411.4028 [quant- ph] (2014).
[7] J. Wurtz and P. Love, MaxCut quantum approximate optimization algorithm performance guarantees for p > 1, Phys. Rev. A 103, 042612
(2021).
[8] G. E. Crooks, Performance of the Quantum Approximate Optimization Algorithm on the Maximum Cut Problem, arXiv:1811.08419
[quant-ph] (2018).
[9] A. Peruzzo, J. McClean, P. Shadbolt, M.-H. Yung, X.-Q. Zhou, P. J. Love, A. Aspuru-Guzik, and J. L. O’Brien, A variational eigenvalue
solver on a photonic quantum processor, Nat Commun 5, 4213 (2014).
[10] M. Cerezo, A. Arrasmith, R. Babbush, S. C. Benjamin, S. En-do, K. Fujii, J. R. McClean, K. Mitarai, X. Yuan, L. Cincio, et al., Variational
Quantum Algorithms, Nat Rev Phys 3, 625(2021).
[11] A. Lucas, Ising formulations of many NP problems, Front. Physics 2, 5 (2014).
[12] J. Preskill, Quantum Computing in the NISQ era and beyond, Quantum 2, 79 (2018).
[13] E. Farhi, J. Goldstone, S. Gutmann, and M. Sipser, Quantum Computation by Adiabatic Evolution, arXiv:quant-ph/0001106 (2000).
[14] N. N. Hegade, X. Chen, and E. Solano, Digitized counterdiabatic quantum optimization, Phys. Rev. Research 4, L042030 (2022).
[15] N. N. Hegade, P. Chandarana, K. Paul, X. Chen, F. Albarrán-Arriagada, and E. Solano, Portfolio optimization with digitized counterdiabatic quantum algorithms, Phys. Rev. Research 4, 043204 (2022).
[16] J. Lee, A. B. Magann, H. A. Rabitz, and C. Arenz, Progress toward favorable landscapes in quantum combinatorial optimization, Phys.
Rev. A 104, 032401 (2021).
[17] T. L. Patti, O. Shehab, K. Najafi, and S. F. Yelin, Markov Chain Monte-Carlo Enhanced Variational Quantum Algorithms,arXiv:2112.02190 [quant-ph] (2021).
[18] D. J. Egger, J. Mareček, and S. Woerner, Warm-starting quantum optimization, Quantum 5, 479 (2021).
[19] D. Beaulieu and A. Pham, Max-cut Clustering Utilizing Warm-Start QAOA and IBM Runtime, arXiv:2108.13464 [quant-ph] (2021).
[20] R. Montenegro and P. Tetali, Mathematical Aspects of Mixing Times in Markov Chains, Found. Trends Theor. Comput. Sci. 1, 237–354
(2006).
[21] N. Thomas, Monte Carlo Search for Very Hard KSAT Realizations for Use in Quantum Annealing, arXiv:1412.5361v1 [cond-mat.statmech] (2014).
[22] M. R. Garey, A guide to the theory of np-completeness, Computers and intractability (1979).
[23] L. Wang, C.-M. Li, J. Zhou, B. Jin, and M. Yin, An Exact Algorithm for Minimum Weight Vertex Cover Problem in Large Graphs,
arXiv:1903.05948 [cs] (2019).
[24] S. Hadfield, Quantum Algorithms for Scientific Computing and Approximate Optimization, arXiv:1805.03265v1 [quant-ph] (2018).
[25] A. Ozaeta, W. van Dam and P. L. McMahon, Expectation Values from the Single-Layer Quantum Approximate Optimization Algorithm
on Ising Problems, arXiv:2012.03421 [quant-ph] (2021).
[26] F. Kemp, Probability for Statisticians, Journal of the Royal Statistical Society: Series D (The Statistician) 52, 249 (2003).
[27] D. Maslen, The eigenvalues of Kac’s master equation, Mathe- matische Zeitschrift 243, 291 (2003).

