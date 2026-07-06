One-dimensional long-range Ising model: two (almost) equivalent approximations
Valerio Pagni,1 Guido Giachetti,2 Andrea Trombettoni,3, 4, 5 and Nicolò Defenu1, 6

arXiv:2510.02458v2 [cond-mat.stat-mech] 20 Dec 2025

1

Institut für Theoretische Physik, ETH Zürich, Wolfgang-Pauli-Str. 27, 8093 Zürich, Switzerland
2
Laboratoire de Physique de l’École Normale Supérieure, CNRS, ENS & PSL
University, Sorbonne Université, Université Paris Cité, 75005 Paris, France
3
Dipartimento di Fisica, Università di Trieste, Strada Costiera 11, I-34151 Trieste, Italy
4
SISSA and INFN Sezione di Trieste, Via Bonomea 265, I-34136 Trieste, Italy
5
CNR-IOM DEMOCRITOS Simulation Center, Via Bonomea 265, I-34136 Trieste, Italy
6
CNR-INO, Area Science Park, Basovizza, 34149 Trieste, Italy

We investigate the critical behavior of the one-dimensional Ising model with long-range interactions using the functional renormalization group in the local potential approximation (LPA), and
compare our findings with Dyson’s hierarchical model (DHM). While the DHM lacks translational
invariance, it admits a field-theoretical description closely resembling the LPA, up to minor but
nontrivial differences. After reviewing the real-space renormalization group approach to the DHM,
we demonstrate a remarkable agreement in the critical exponent ν between the two methods across
the entire range of power-law decays 1/2 < σ < 1. We further benchmark our results against Monte
Carlo simulations and analytical expansions near the upper boundary of the nontrivial regime, σ <
∼ 1.
I.

INTRODUCTION

Long-range interacting systems have emerged as a central theme in modern many-body physics, exhibiting a
rich variety of collective phenomena that challenge and
extend the standard paradigms established for shortrange systems [1]. These include the breakdown of locality, violations of conventional scaling laws, and the
emergence of novel universality classes. Such systems
naturally arise in numerous physical contexts, including
trapped ion chains [2], dipolar gases [3], Rydberg atom
arrays [4], and cavity QED setups [5]. Moreover, recent
progress in quantum information and nonequilibrium dynamics has further highlighted the role of long-range interactions in phenomena such as dynamical phase transitions, thermalization and equilibration, and information
spreading beyond the light-cone limit, see Refs. [1, 6] for
a review. These developments have renewed interest in
understanding the critical behavior of long-range models,
both at and out of equilibrium, and in developing robust
theoretical tools to describe them.
Among the various models used to investigate longrange critical phenomena, a particularly influential and
extensively studied example is the one-dimensional longrange Ising
P(1D LRI) model, defined by the Hamiltonian
H = − 21 i̸=j Jij si sj with spin variables si = ±1 and
couplings decaying algebraically as
Jij =

J
,
|i − j|1+σ

(J > 0)

(1)

where σ > 0 ensures a well-defined thermodynamics [7].
Unlike its short-range counterpart in d = 1, the 1D LRI
model exhibits a finite-temperature phase transition for
certain values of σ. In fact, the long-range nature of
the couplings suppresses the strong fluctuations typical of
low-dimensional systems, allowing for spontaneous symmetry breaking. This was first rigorously established by
Dyson in Ref. [8] for all σ ∈ (0, 1), through the introduction of Dyson’s hierarchical model (DHM) as a tractable

lower bound. For σ > 1 there is no transition [9]. The
marginal case σ = 1, corresponding to interactions decaying as 1/r2 , remained unresolved in Dyson’s original
analysis. It was later shown by Fröhlich and Spencer [10]
that this case features a Berezinskii–Kosterlitz–Thouless
(BKT)-like transition, characterized by an essential singularity in the free energy. Notably, however, this transition includes a discontinuity in the magnetization – anticipated by Thouless in Ref. [11], see also [12] – which
distinguishes it from the standard BKT transition in the
two-dimensional XY model. The strong interest in the
Ising model with 1/r2 interactions was the result of its
equivalence to the Kondo problem, established by Anderson, Yuval and Hamann in a series of papers [13–15],
which also contain an early version of the renormalization group (RG) later developed by Wilson [16]. Their
methods were extended by Cardy [17] to encompass general discrete spin chains with 1/r2 interactions, including
Potts and Ashkin–Teller models.
The main interest of this work is the critical behavior of the 1D LRI with 0 < σ < 1. This is related
to the quantum criticality of the spin-boson model [18]
– via an imaginary time path integral approach analogous to [13–15] – where the power-law exponent of the
spectral function of the bosonic bath corresponds to σ
in the classical 1D LRI model. Despite the absence of
an exact solution for the partition function, the critical
physics of the 1D LRI with power law exponent σ has
been investigated through various powerful techniques,
such as Monte Carlo (MC) simulations [19–22], RG approaches [23, 24], and, recently, conformal field theory
(CFT) methods [25, 26].
In this work, we adopt the RG framework, which has
played a central role in the study of long-range critical
systems [27, 28]. Our goal is twofold. First, to compute
the critical exponent ν within a functional renormalization group (FRG) approach [29–32] – notice, indeed, that
one expects that the critical exponent η has a trivial dependence on σ [28] and therefore the main critical ex-

2
ponents are determined once the non-trivial dependence
of ν has been worked out. Second, to explore the connection between the FRG analysis of the 1D LRI model
and the real-space RG treatment of Dyson’s hierarchical model, which is a well-developed tool [33, 34], even
from a mathematically rigorous point of view [35–37].
Although the DHM is not translationally invariant and
is often regarded as a toy model, we argue that it admits
an effective description that closely mirrors the local potential approximation (LPA) of the FRG.
The structure of the paper is as follows. After a brief
reminder in Sec. II of results on critical properties of longrange systems useful for the rest of the paper, in Sec. III
we introduce the FRG formalism and present a nonperturbative estimate of the critical exponent ν = ν(σ),
which, to our knowledge, has not been explicitly computed for the 1D LRI model in this context. In Sec. IV,
we argue for a field-theoretical formulation of the DHM
and show how it is closely related to the FRG in the
LPA. We then review the calculation of ν in the DHM
by means of real-space RG and compare it with the FRG
results. In Sec. V, we benchmark our findings against
Monte Carlo simulations and analytical expansions near
the σ → 1 and σ → 1/2 limits. Our conclusions and
outlook are presented in Sec. VI.

II.

REMINDER ON CRITICAL PROPERTIES
OF LONG-RANGE SYSTEMS

In this section, we briefly review results on the characterization of critical behavior of long-range systems [1, 7]
and discuss the case with spatial dimension d = 1, which
presents some peculiarities.
Focusing on the regime σ > 0, where interactions decay more rapidly than 1/rd , we distinguish between three
scenarios. In the interval σ ∈ (0, σmf ) the critical behavior is essentially mean-field and governed by the Gaussian fixed point, very similar to how mean-field theory
provides the correct exponents above the upper critical
dimension in short-range systems. Distinctive long-range
features emerge for σ ∈ (σmf , σ∗ ), where the critical exponents depend continuously on the range parameter σ.
In this intermediate regime – the focus of this work –
the critical fixed points are interacting ones, meaning
that the role of fluctuations becomes crucial. Finally,
for σ ∈ (σ∗ , ∞) the critical behavior crosses over to the
short-range universality class, as the long-range interaction becomes irrelevant. While σmf = d/2 for classical LR O(n) models [1, 7], the exact value of σ∗ has
long remained controversial in d > 1 [38]. Today, the
most widely accepted scenario, proposed by Sak [28], is
that σ∗ = 2 − ηSR , where ηSR is the anomalous dimension of the model with short-range interactions, while for
the long-range model η(σ) = 2 − σ [22, 39, 40]. Critical properties of d-dimensional long-range systems have
been studied by a variety of methods, including Monte
Carlo [22, 41–43], RG approaches [23, 24, 27, 28, 39]

and conformal bootstrap [40, 44–46]; see further references in [1, 7, 38]. Peculiar behavior may arise in twodimensional O(2) symmetric models [47–51], which is yet
the subject of active research.
In d = 1, the values 0 < σ < 1/2 identify the region
where critical exponents are exactly given by mean-field
theory, e.g. ν(σ) = 1/σ for the 1D LRI model (notice
that this region for long-range bond-percolation in d = 1
is 0 < σ < 1/3 [52]). On the other hand, the non-meanfield region extends only across 1/2 < σ < σ∗ = 1, as
anticipated by the foregoing summary of results about
the 1D LRI model. In fact, this agrees with [28], as
formally we have ηSR (d = 1) = 1, due to the fact that
in one dimension the short-range model has only a zerotemperature transition, where the two-point correlator
decays as a power-law with vanishing exponent, i.e. it is
constant.
The lack of a finite-temperature transition in the shortrange Ising chain carries interesting consequences. In the
absence of a short-range universality class, the usual picture consisting in the crossover from a line of long-range
fixed points to the short-range regime, see e.g. [40], becomes more involved. The crucial observation is that in
the region around σ∗ = 1 the most suitable degrees of
freedom are not the original spins, but the domain walls,
or kinks, introduced in [13–15] for σ = 1, and used in
the RG analysis of [23] for σ <
∼ 1, which considers a diluted gas of alternating kinks. As an extension of this
approach, and based on the infrared duality of [40] for
d > 1, Refs. [25, 26] provide a weakly-coupled field theory
for the 1D LRI model below σ = 1. Contrary to higher
dimensional LRI models, their theory is written in terms
of a compact free field with negative scaling dimension,
perturbed by vertex operators with the alternating-kink
constraint, which is enforced via an algebra of Pauli matrices. Thus, we expect that the peculiar character of the
one-dimensional problem close to the short-range limit is
going to also affect the following analyses – based on the
RG.

III.

LOCAL POTENTIAL APPROXIMATION

A.

Functional renormalization group in the LPA

In the first part of this article, we study the critical
physics of the 1D LRI model in the regime σ ∈ (1/2, 1)
by means of a functional renormalization group (FRG)
approach based on the effective average action. The latter is a modification of the generating functional Γ[ϕ] of
one-particle irreducible vertex functions (see e.g. [53]),
or the Legendre transform of the generating functional
of connected correlation functions. Such modification involves considering an external momentum scale k ≥ 0,
and adding a scale-dependent mass term to the bare action Sbare [ϕ] describing the field theory, so that the effective action reads Γk [ϕ], as it carries a k-dependence.
The mass term dependent on k is included to regular-

3
ize infrared modes with momentum scale q ≪ k. To
achieve that, a regulator function Rk (q) with appropriate features has to be specified. In particular, we want to
choose Rk so that at the microscopic scale k = Λ one retrieves the action Sbare [ϕ] = Γk=Λ [ϕ], while at the largest
scales k → 0 the full generating functional is approached,
that is Γk→0 [ϕ] → Γ[ϕ].
Within this setup it is possible to write the functional
and non-perturbative RG equation
Z
1
∂t Γk [ϕ] =
tr [Gk (q) ∂t Rk (q)] ,
(2)
2 q
R
proposed by Wetterich and Morris [29, 54], where q =
R
dq/(2π) and t = log(k/Λ). Denoting the second func(2)
tional derivative (Hessian) of the action by Γk , the fielddependent propagator Gk = Gk [ϕ] reads

−1
(2)
Gk [ϕ] = Γk [ϕ] + Rk
.

(3)

More details are found in [30–32] and references therein.
While there is no general solution to the equation (2),
it is possible to consider a truncated form of the action, so
that it becomes possible to project the RG onto functions
– rather than functionals – and obtain simpler differential
equations. A standard ansatz chosen for Γk is the local
potential approximation (LPA), which for the long-range
Ising model in one spatial dimension is
Z ∞
n
o
Γk [ϕ] =
dx ϕ(x)(−∆)σ/2 ϕ(x) + Vk (ϕ(x)) , (4)
−∞

where Vk (ϕ) is a local function of the field called effective
potential, and (−∆)σ/2 is the fractional Laplacian [55].
For an infinite homogeneous chain we equivalently use
the momentum-space variant of the gradient term:
Z ∞
Z ∞
dq σ
q ϕ(q)ϕ(−q) =
dx ϕ(x)(−∆)σ/2 ϕ(x), (5)
−∞
−∞ 2π
whence it becomes clear that long-range interactions are
described by a continuous field theory with non-analytic
momentum dependence. Note that q σ ≡ |q|σ .
It is crucial to note that the k-dependence of the LPA
ansatz (4) lies entirely in the effective potential Vk (ϕ).
In other words, the gradient term (5) is not subject to
any renormalization. The assumption that the theory is
given by (4) is certainly an approximation, so we cannot expect it to capture exactly the critical behavior of
the model. In fact, the LPA is the leading order of the
so-called derivative expansion, which would in principle
enable a systematic improvement of numerical results by
the inclusion of higher-order derivative interactions.
For long-range theories, however, the next to leading
order improvement of the LPA does not come from a
renormalization of the gradient term as in short-range
models. In fact, it has been shown [39] that no anomalous
scaling of the non-analytic term is generated by the FRG

if a (field-independent) wavefunction renormalization Zk
is introduced in front of the q σ term. This also agrees
with [56], where a similar result is shown for Wilson’s RG
to all orders of perturbation theory. On the other hand,
the short-range analytic term of the form q 2 ϕ(q)ϕ(−q)
is always generated under RG [56] together with other,
sub-leading, non-analytic terms [57]. We are neglecting
this term in the present analysis. In dimension d > 1
its influence becomes noticeable only very close to σ =
σ∗ [58].

B.

RG flow and fixed points

As previously discussed, we can now use the general
RG equation to deduce the flow of the effective potential.
Evaluating Eq. (2) at a constant field configuration, the
gradient term disappears, leading to
Z
1
∂t Rk (q)
∂t Vk (ϕ) =
.
(6)
σ
2 q q + Rk (q) + Vk′′ (ϕ)
Let us now consider the regulator [39]
Rk (q) = (k σ − q σ ) θ(k σ − q σ )

(7)

generalizing the standard Litim cutoff used for shortrange systems. We employ this regulator because it satisfies an optimization criterion for the LPA [59–61], thereby
minimizing systematic errors in the computation of critical exponents [32]. For example, the critical exponents
found with the Litim regulator are more accurate [62]
than those obtained with a power-law cutoff [63, 64].
Most importantly for our purposes, this optimized choice
is structurally closest to the recursion relations of the
DHM, allowing for the direct comparison performed in
Sec. IV C. The investigation of different regulator choices
and their impact on the specific numerical values of critical exponents is deferred to future studies. Focusing here
on the optimized Litim cutoff, the flow equation Eq. (6)
reads
∂t Vk (ϕ) =

σ
k 1+σ
.
σ
2π k + Vk′′ (ϕ)

(8)

The properties of criticality are captured by certain fixed
points of the RG flow. At such fixed points we expect scale-invariant solutions of Eq. (8). We therefore
turn (8) into the following autonomous differential equation (meaning that the scale k does not appear explicitly
in the equation):
∂t Ṽk (φ) = −Ṽk (φ) +

1−σ
σ
1
φṼk′ (φ) +
, (9)
2
2π 1 + Ṽk′′ (φ)

where we have used the dimensionless variables
x̃ = kx,

σ−1

φ(x̃) = k 2 ϕ(x),

Ṽk = k −1 Vk .

(10)

4
Setting the left-hand side of (9) to zero yields the fixedpoint equation. This is now an ordinary differential equation whose solutions Ṽ∗ (φ) can be studied by means of
a shooting method known as spikeplot [39, 65, 66] or
via pseudospectral approaches [67, 68]. Both the Gaussian and the interacting (Wilson-Fisher) fixed points are
found without the need of any Taylor expansion of the
effective potential.

0.6
0.5
0.4

C.

1
ν

Linearization around the fixed point

Once the scaling solution Ṽ∗ (φ) has been obtained, our
objective is to study the neighborhood of the interacting
fixed point in order to obtain the critical exponent in the
regime 1/2 < σ < 1. One of the exponents, namely the
anomalous dimension η = 2 − σ, is already determined
thanks to the analysis of [39], which holds in our case
as well. We are therefore interested in determining ν, so
that the remaining exponents can be retrieved by the use
of scaling laws, such as γ = ν(2 − η) = νσ.
The linearization around the fixed point Ṽ∗ (φ) leads
to the determination of RG eigenvalues [16], the largest
of which (typically known as thermal eigenvalue) corresponds to the inverse of ν: ymax ≡ yt = ν −1 . The FRG
approach allows us to obtain the spectrum of eigenvalues
functionally, without resorting to truncations of Taylor
series. We write the ansatz
Ṽk (φ) = Ṽ∗ (φ) + εe−yn t un (φ),

(11)

where ε ≪ 1, and yn is the n-th eigenvalue with eigenfunction un . Substituting (11) into (9) while keeping only
linear terms in ε leads to
(yn − 1)un (φ) +

1−σ ′
σ
u′′n (φ)
φun (φ) =
. (12)
2
2π [1 + Ṽ∗′′ (φ)]2

Solving this linear differential equation yields the values
of yt = ν −1 shown as red dots in Fig. 1 for the whole
range σ ∈ (0.5, 1). In Fig. 1 we also report other estimates of ν −1 that will be discussed in the forthcoming
sections.
Close to the mean-field limit σ = 1/2, where the relation ν = 1/σ holds [27], we obtain indeed values close
to ν −1 = 0.5. On the other hand, we note that the exponent ν diverges in the proximity of σ = 1, so that
ν −1 → 0 for σ → 1− , as it should. This is analogous to
the short-range XY model, in which case the approach to
the BKT transition as d → 2 from above is accompanied
by a similar behavior of ν. We observe that near σ = 1
the LPA results are well fitted by ν −1 ≈ C(1 − σ)γ with
C ≈ 4.0
p and γ ≈ 0.9, to be compared with the result
ν −1 = 2(1 − σ) of [23, 25].
IV.

HIERARCHICAL MODEL

In this section, we focus on a lattice system different from the 1D LRI model. The microscopic vari-

LPA
DHM
Effective dimension
p
2(1 − σ)

0.3
0.2

CFT perturbative
-expansion
Three-loop PB
MC Tomita
MC Uzelac

0.1
0.0

0.5

0.6

0.7

0.8

0.9

1.0

σ
FIG. 1. Inverse of the critical exponent ν of the 1D LRI model
in the region 1/2 < σ < 1. The red dots are the results coming
from a non-perturbative FRG calculation at the LPA level,
described in Sec. III. The blue crosses represent the estimates
obtained from the DHM via a real-space RG, see Sec. IV.
The green triangles at σ = 0.5, σ ≈ 0.65 and σ = 0.875 are
obtained via the effective dimension approach, Eq. (47). The
dotted line is the two-loop ϵ expansion (44) of [27], while the
pink stars are the three-loop Padé-Borel resummed exponents
of [69]. The black dashed and olive dash-dotted lines are the
results coming from expansions around σ = 1, respectively
from [23] and [25]. More details about these are provided in
Sec. V. A detailed comparison of LPA and DHM results is
presented in Fig. 5. Finally, Monte Carlo points are taken
from Refs. [21] and [20].

ables are still Ising spins si ∈ {−1, +1} along a onedimensional chain, but the hierarchical model introduced
by Dyson (DHM) in [8] is most naturally described in
terms of block-spin variables. The hierarchical nature
of the model is captured by a label p ∈ {0, 1, . . . , N }
which we refer to as level. The number N of levels is a
positive integer. At the lowest level p = 0, the blockspin variables are exactly the same as the original spins
{si }, and we have 2N ≡ L of them. At level p = 1, we
join adjacent variables into two-spin blocks, resulting in
2N /2 = 2N −1 block-spins. At the higher levels, we join
again two adjacent blocks to form bigger ones. In general,
r ∈ {1, 2, . . . , 2N −p } identifies a specific block, once p has
been fixed. Of course, the last level p = N corresponds
to having all the original Ising spins {si } grouped into a
single block variable. Fig. 2 provides a visual summary of
the above description. Mathematically, this whole procedure is encoded by defining the block-spin variables as

5
where the triangle inequality is replaced by the condition
dij ≤ max{dik , dkj }. As a result, the matrix elements
Aij in Eq. (15) are

p=N

h
1

2

3

4

5

6

7

Aij =

8

N
X

p=dij

FIG. 2. Schematic representation of the hierarchical structure
of interactions in the DHM with N = 3 levels and L = 8 sites.
The weakest interaction corresponds to the top-level p = N .
A possible external field h couples linearly to the spins si at
the sites i ∈ {1, . . . , 8}.

the following sums
p

Sp,r =

2 r
X

si .

(13)

i=1+2p (r−1)

It is evident that the recursive property Sp−1,2r−1 +
Sp−1,2r = Sp,r , which enables us to pass from level p − 1
to level p, must hold. Moreover, according to the description above, it is also true that each variable Sp,r1 is
equivalent to any other Sp,r2 at the same level. This is
related to the very large symmetry group of the DHM,
which has order 2L−1 and is ultimately responsible for
the abundance of exact results about it [34].
The idea behind the DHM is to emulate the long-range
interactions of the form |i − j|−(1+σ) si sj in the 1D LRI
model. In order to obtain two-body interactions si sj it
is sufficient to square the variables Sp,r defined in (13).
This generates interactions between any two spins si and
sj contained in the r-th block at level p. However, interblock interactions are absent. To capture the decay of
interactions with distance, the intensity of the coupling
is suppressed as the block size increases with the level p,
2
by 2−p(1+σ) . In fact, the Hamiltonian
by multiplying Sp,r
of the DHM reads [8, 34]
HN = −

N
X

J

N −p
2X

2p(1+σ) r=1
p=1

(Sp,r )2 ,

(14)

with some constant J. The two main goals of this section
– i.e. the comparison with the 1D LRI model and the
renormalization of the DHM – are achieved by rewriting
the Hamiltonian (14) in terms of an ultrametric distance
and in a recursive fashion, respectively.
Let us begin with the first task. In order to construct
a fully-connected Ising-like Hamiltonian [70]
X
HN = −J
Aij si sj , i, j ∈ {1, . . . , L = 2N }, (15)
ij

we have to evaluate the cumulative interaction between
spins si and sj across all hierarchical levels. One starts
from p = dij , the first level at which the sites i and
j belong to the same block. The function dij satisfies
the property of a distance in an ultrametric space [71],

1
2−[dij −1]α − 2−N α
=
,
2pα
2α − 1

(16)

where we are using the notation α = 1 + σ for brevity.
It is worth noting that the L × L matrix A with entries
given by (16) possesses the block-hierarchical structure
shown in Fig. 3(a).
This contrasts with the 1D LRI model, cf. Fig. 3(b),
where the interactions (1) depend directly on the Euclidean distance and no tree hierarchy is present. In the
thermodynamic limit N, L → ∞ the correction 2−N α
in (16) becomes negligible and Aij ∼ 2−dij α . Comparing with (1), the correspondence 2dij ≈ |i − j| between
hierarchical and Euclidean distance may be drawn [70].
We remark in passing that the field of p-adic numbers,
which can be represented as infinite paths in a rooted
tree (in our case a 2-adic tree), plays an important role
in the rigorous RG-based formulation of quantum field
theory, see e.g. [72, 73].
Moreover, in (15) we include the constant term corresponding to the level p = 0 of the microscopic spins
(S0,i = si ) via the diagonal elements with dii = 0. In the
matrix plot of Fig. 3(a), these are visualized as bright
spots along the diagonal, as opposed to Fig. 3(b), where
Jii = 0 for the 1D LRI model. One can check that the inclusion of the level p = 0 ensures the matrix A is positive
definite, a property we will exploit in Sec. IV B, where
we also motivate the inclusion of this term – originally
absent from the Hamiltonian (14).
Finally, we turn to the recursive form of the Hamiltonian (14). In analogy with Ref. [22], we write
right
left
HN = HN
−1 + HN −1 −

J
S2 ,
2N (1+σ) N,1

(17)

which is just the expression of the possibility of joining
two (N − 1)-level models and adding interactions at the
top level (in fact, SN,1 = s1 + · · · + sL ) in order to obleft
tain an N -level DHM. More precisely, HN
−1 involves the
right
spins at sites {1, . . . , L/2}, while HN −1 refers to the sites
{L/2 + 1, . . . , L}.
The self-similar nature of hierarchical tree structures
can be used to derive exact RG equations in several
different context, from critical phenomena [33] to polymers [74], information transitions [75] and approximated
ones for quantum phase transitions [76]. Before proceeding to discuss the renormalization of the classical DHM,
we remark that the model displays a phase transition
for all values of α ∈ (1, 2) – or σ ∈ (0, 1) – like the 1D
LRI model [8]. The case σ = 1 is more delicate, because
the 1D LRI model has a phase transition with BKT features [10, 11], while the DHM does not [8]. Nonetheless,
a slight modification of the decay of the interaction in
Eq. (14) – namely replacing the factor 2−p(1+σ) = 2−2p

6
(a)

(b)
7

7

d1,7

1

2

3

4

1

2

5
3

6
4

7
5

dE
1,7

d2,7

1 d1,2 2

8
6

7

1

8

2
1

3

4
2

5
3

6
4

7

E

1 d1,2 2

8
5

dE
2,7

6

7

8

1

1

1

1

2

2

2

2

3

3

3

3

4

4

4

4

5

5

5

5

6

6

6

6

7

7

7

7

8

8

8

8

1

2

3

4

5

6

7

8

1

2

3

4

5

6

7

8

FIG. 3. One-dimensional chains of L = 8 Ising spins with either (a) hierarchical or (b) long-range interactions. (a) The
interaction matrix elements (16) of the hierarchical model exhibit ultrametric structure, since they depend on the distance
dij , measuring the depth of the lowest common ancestor of two ‘leaves’ (spins). Arranging distances as a triangle (shown for
sites 1, 2 and 7), the ultrametric inequality forces an isosceles configuration with a short base. (b) The intensity of matrix
elements (1) in the 1D LRI decays as a power law Jij ∼ |i − j|−(1+σ) of the Euclidean distance dE
ij = |i − j|. Contrary to (a),
Euclidean distances form a generic scalene triangle, for which the usual triangle inequality holds. In these figures, lighter colors
correspond to larger numerical values of the matrix elements, while the dark diagonal spots in (b) correspond to Jii = 0.

by 2−2p log(p) – does yield a BKT-like transition and the
Thouless effect [12]. We leave a more careful study of
this variation of the DHM to future investigations.
A.

Real-space renormalization

as a Gaussian integral over an auxiliary variable ϕ, so
that
Z ∞
2
1
ZN (β, h) = √
dϕ e−ϕ ×
π −∞
√
X
right
left
×
e−β[HN −1 (h)+HN −1 (h)]+2 AN ϕSN,1 .
(19)
{si }

For later convenience, we add to the Hamiltonian HN
an external field term of the form −hSN,1 , such that each
individual spin si interacts linearly with the field h. Even
so, the recursive property (17) holds unchanged.
Hence, using (17) and taking into account the possibility of external fields, the partition function satisfies
X
right
left
2
ZN (β, h) =
e−β[HN −1 (h)+HN −1 (h)] eAN SN,1
(18)

Redefining
the external field as h 7→ ĥN = h +
√
2 AN ϕβ −1 , the partition function reduces to the one
of a system with N − 1 levels and an external field ĥN ,
i.e.
Z ∞
2
1
ZN (β, h) = √
dϕ e−ϕ ZN −1 (β, ĥN )2 .
(20)
π −∞

where AN ≡ 2−N (1+σ) βJ. A Hubbard-Stratonovich
transformation enables us to recast the last exponential

In summary, we effectively removed the weakest link in
Fig. 2, in order to decouple the left and right chains, by

{si }

7
modifying the external field h 7→ ĥN (ϕ) in the HubbardStratonovich representation.
Since the recursive equation (20) is true at each level,
N can be replaced by p ∈ {1, . . . , N }. Moreover, reading (20) from right to left, we can interpret it as a blockspin transformation in the RG sense [77], with length
scale factor ℓ = 2. Even after one RG step – as we
have anticipated – the form of the Hamiltonian stays unchanged: Possible nonlocal interactions are not generated
by the RG due to the hierarchical structure of the system. This already suggests a deep similarity with the
LPA discussed in Sec. III. √
−1/2
Introducing P̃p (βAp x/ 2) = Zp−1 (β, x)2 , one obtains

2
Z ∞
1+σ
1
−(φ−y)2
2
dφ e
P̃p+1 (2
y) = √
P̃p (φ) , (21)
π −∞
after the change of variable from ϕ to φ = ϕ + y, with
√
−1/2
y = βAp h/ 2. This RG equation can be taken as the
starting point for the analysis of the fixed points of the
DHM.
An alternative route to the RG procedure [33, 34] is
to introduce the following probability measure for a spin
variable s
P0 (s) =

1
[δ(s − 1) + δ(s + 1)]
2

ZN (β, h) =

X

e−βHN =

√
1+σ
2
Pp+1 ( Cs) = 2 2 e−βCs

−∞

dy Pp (s + y)Pp (s − y),

(24)
where C = 21−σ . In passing we note that the RG transformation involves a rescaling of the spin by a factor
1−σ
proportional to ℓ− 2 , with ℓ = 2. Comparing that to
d−2+η
the conventional rescaling ℓ− 2 in d = 1, we obtain
η = 2 − σ, which is the same as the Sak relation [28] for
long-range models, including the 1D LRI model.
Eq. (24) contains the same information as (21), which
now can be interpreted [33] as the RG equation for the
Hubbard-Stratonovich dual P̃p of the spin measure Pp :
P̃p (φ) =

Z ∞

2

ZN =

=

Z
Z

e−βHN

L
Y

P (si )dsi

i=1
P

eβJ

ij Aij si sj

L
Y

2

e−βJsi P (si )dsi ,

(26)

i=1

where the last line includes the p = 0 level and therefore
features the Hamiltonian (15) written in terms of the
ultrametric matrix Aij , which is positive definite. Due
to the latter property, we can again use the HubbardStratonovich transformation from the spins {si } to the
field variables {ϕi }, obtaining
ZN ∝

Z

e−

−1
ij ϕi Aij ϕj

P

L
Y

P̃ (ϕi )dϕi ,

(27)

i=1

where P̃ is given by (25). Now, we separate off the diagonal contribution from the bilinear term
2
A−1
ij = Kij + m δij ,

V (ϕi ) = m2 ϕ2i − log P̃ (ϕi ).

#

(23)
and to derive an effective RG equation for this quantity.
In particular, the probability Pp (s) after p steps of renormalization evolves according to [33, 34]
Z ∞

P
As discussed earlier, the p = 0 term −J i s2i is added
to the Hamiltonian of the DHM. This is achieved while
keeping the partition function invariant, that is

(28)

and we define a local potential

P0 (si )dsi e−βHN ,

i=1

{si }

A local potential field theory for the DHM

(22)

so that the partition function reads
Z "Y
L

B.

(29)

R
eff
Therefore, the partition function ZN = dL ϕ e−HN [ϕ]
can be written in terms of the effective Hamiltonian
X
X
eff
HN
[ϕ] =
ϕi Kij ϕj +
V (ϕi ).
(30)
i̸=j

i

In this form, we can notice that the DHM renormalizes in exactly the same way as the LPA (4): The gradient term remains untouched, while the local potential
term flows under RG as a consequence of Eq. (21). In
the DHM this occurs by construction, while the absence
of renormalization of the gradient term in the LPA in
momentum-space RG is considered a truncation of the
full theory. Hence, we suggest that the latter truncation
in the field-theoretical framework corresponds to approximating the 1D LRI model on the lattice by the DHM
(with the same σ).
In order to make the analogy even tighter, we now show
that the gradient term in (30) mimics the non-analytic
momentum dependence q σ appearing in (4). In fact, the
eigenvalues of A = (Aij ) read

√

ds e−βJs +2 βJsφ Pp (s).

(25)

−∞

λk =

N
−k
X
j=0

Indeed, as discussed further in the next section, P̃ (ϕ)
can be interpreted as the probability distribution of the
variables ϕi , conjugate to the spin variables si .

2−jσ =

2σ − 2−(N −k)σ
2σ − 1

(31)

for k ∈ {0, . . . , N }. Their corresponding multiplicities
are given by 2k−1 for k > 0, with the largest eigenvalue

8

−1
ωk = λ−1
k − λ0 ,

qkσ
,
1 − (qk /2)σ

ω(q) = cσ q σ
DHM dispersion

0.08

0.06

0.04

0.02

0.00
0.00

0.05

0.10

0.15

0.20

q
FIG. 4. Comparison between the long-range dispersion
ω(q) = cσ q σ and its hierarchical counterpart ωk from Eq. (33).
For this plot σ = 0.5 and N = 20 have been chosen.

(32)

with the same degeneracy as the λk . It is now useful to
define the pseudo-momentum qk ≡ 2−(N −k) , with 0 <
qk ≤ 1, such that
ωk = ω(qk ) = cσ

0.10

ω(q)

λ0 being non-degenerate. This expression is compatible
with the spectrum of Ref. [71], where the level p = 0 was
however not included in the coupling matrix. The eigenvectors v k , though known [70, 71], do not correspond to
plane waves, as the DHM does not exhibit translational
invariance. First, both v 0 and v 1 contain 2N non-zero
components. While v 0 – up to normalization factors –
is the constant vector (1, 1, . . . , 1), the first half of v 1 is
filled with −1 and its second half with +1. Then, in general the k-th eigenspace is spanned by the mutually or(m)
thogonal eigenvectors v k , with m ∈ {1, . . . , 2k−1 } and
constructed as follows. The only nonzero elements of the
(1)
vector v k are the first 2N −k+1 ones: The first half of
them are all equal to −1, the second half are all +1.
(2)
Next, v k contains the same elements, but shifted: The
first 2N −k+1 ones are now zeros, but the second batch of
(1)
2N −k+1 elements are filled exactly as for v k . Iterating
this procedure yields all the other eigenvectors.
Knowing the spectrum of the adjacency matrix A, the
2
eigenvalues of K are then given by λ−1
k − m . Since we
interpret the first term in the effective Hamiltonian H eff
as a gradient term, we select a value of m2 such that the
zero mode (k = 0) has zero energy, i.e. m2 = λ−1
0 . We
conclude that the spectrum of the gradient term is

(33)

in the following discussion we are going to find out that
the values of the exponent ν for the LPA and the DHM
are numerically very close; in fact, they are almost equal
within our current choice of the regulator, see Eq. (7).

up to terms that vanish in the thermodynamic limit N →
∞. The prefactor is cσ = 2−σ (1 − 2−σ ). In a continuous
representation we can write the dispersion
C.

ω(q) =

N
−1
X
k=0

ω(qk )θ(q − qk )θ(qk+1 − q),

Exponent ν and comparison with the LPA

(34)

where q ∈ (0, 1]. In the thermodynamic limit, for sufficiently small values of qk , we observe that ω(q) ∼ cσ q σ ,
as visualized in Fig. 4. Hence, we have shown that
the hierarchical model produces a ‘wedding cake’ version of the dispersion appearing in (5). Using the symbol ⌊−∆⌋σ/2 to denote a hierarchical Laplacian whose
pseudo-momentum space representation is given by ω(q)
in Eq. (34), we compactly write the effective theory as
Z ∞
n
o
H eff [ϕ] =
dx ϕ(x)⌊−∆⌋σ/2 ϕ(x) + V (ϕ(x)) ,
−∞

(35)
after considering a suitable continuum limit. The analogy
with (4) is now complete.
Nevertheless, we expect that the hierarchical gradient
term alters the specific form of the fixed point theory
and also the values of the critical exponents. However,

In this part we review very briefly the procedure outlined in [33] to obtain the critical exponents of the DHM.
A convenient way of studying the RG equation (21) starting from the initial condition P̃0 (ϕ) – obtained from (22)
and (25), and dependent on the temperature β −1 – is to
expand the dual spin measure P̃p (ϕ) as a series of Hermite polynomials Hk (aϕ), where a = [1 − 2−(1+σ) ]1/2 .
This choice is prompted by the special property
Z ∞

2
k
dξ
√ e−(ξ−ϕ) Hk (aξ) = (1 − a2 ) 2 Hk
π
−∞



aϕ
√
1 − a2



.

(36)

Therefore, at each step p one can write

(p)

(p)

P̃p (ϕ) = B0 + B0

∞
X

k=1

(p)

Bk 2k(1+σ) H2k (aϕ).

(37)

9
Projecting the RG equation (21) onto the coefficients
(p)
Bk of this expansion yields the recursion relations [33]
(p+1)

= µ B0 B0 ,

k(1+σ)

(p+1)
(p)
µBk
= 2Bk +

B0
2

(p)

(p)

(38a)
∞
X

(p)

(p)

Tkk′ k′′ Bk′ Bk′′ (38b)

k′ ,k′′ =1

µ=1+

0.4

y 0.3
0.2

for all k ≥ 1, where we have defined
∞
X

0.5

0.1

(p)

(p)

22k (2k)! Bk Bk

(39)

0.0

LPA FRG
DHM

k=1

and the combinatorial tensor
(
′
′′ 
2l l! 2kl 2kl , if |k ′ − k ′′ | ≤ k ≤ k ′ + k ′′ ,
Tkk′ k′′ =
0,
otherwise,
(40)
with l = −k + k ′ + k ′′ . When the temperature is tuned to
its critical value β = βc , entering the initial condition P̃0
(p=0)
and thus the coefficients {Bk
}, one is able to reach a
fixed point characterized by {Bk∗ } and µ∗ , which is the
(p)
obvious notation for (39) with Bk → Bk∗ . The fixed
point can be found with very high accuracy and with
a truncated series (37), which typically need not include
much more than 10 terms [33]. The rigorous construction
of this interacting fixed point, along with further aspects
of the RG flow of Dyson-type hierarchical models, is explored in [35–37].
Once the fixed point is known, it is possible to linearize
(p)
(p)
around it. One defines δBk = Bk − Bk∗ and finds
(p+1)

δBk

=

∞
X

(p)

Vkk′ δBk ,

∆y 10
ymean

−4

10−5

0.6

0.7

0.8

0.9

1.0

σ
FIG. 5. In the upper panel we show the thermal eigenvalue
y = ν −1 obtained as solution of (12) in the LPA and (43) for
the DHM. The points overlap almost exactly, as in Fig. 1.
Their relative difference, where ∆y = yLPA − yDHM and
ymean = (yLPA + yDHM )/2, is shown in the lower panel. The
error is peaked in the region of large σ, but it stays below
10−3 throughout the interval 1/2 < σ < 1.

(41)

k′ =1

where the stability matrix is given by
P∞


2 δkk′ + k′′ =1 Tkk′ k′′ Bk∗′′
∗ ∗ 2k′
′
−
B
B
2
(2k
)!
.
Vkk′ = ∗
′
k k
µ
2k(1+σ)
(42)
The critical exponent ν is obtained from the largest eigenvalue λ1 of the stability matrix,
ν −1 = log λ1 / log 2,

(43)

under the requirement that there is only one unstable
direction, and therefore all the other eigenvalues with
m ̸= 1 obey |ym | < 1.
We have carried out the calculation of the exponent ν
for the DHM, and our results are shown as blue crosses
in Fig. 1. One sees that ν −1 → 1/2 for σ → 1/2 and
ν −1 → 0 for σ → 1− , as for the LPA results. Near σ = 1
one has for the DHM results ν −1 ≈ C(1−σ)γ with C ≈ 4.0
and γ ≈ 0.9, again as for the LPA results.
Remarkably, the values of ν −1 (σ) overlap almost perfectly with the corresponding ones obtained via the FRG
at the LPA level, as described in Sec. III. Their relative

difference is always below 10−3 and actually mostly below 10−4 in the entire σ range, see Fig. 5.
The similarity between these two values comes as a
surprise if one considers that the forms of the gradient
terms in Eqs. (4) and (35) is different. In fact, the similarity only occurs for the present choice of the regulator (7), which is a long-range generalization of the optimized Litim regulator [59, 60]. It was already noted
in [78] that the LPA of a short-range scalar theory in
three dimensions reproduces, up to small numerical values, the exponent of a hierarchical model with rescaling
factor ℓ1/3 , provided that the optimized regulator [59, 60]
is used. Here, we demonstrate that this property extends
over the entire σ range and in d = 1.
At an even earlier stage, it was discovered by Felder
in [79] that the ℓ → 1 limit of the RG recusion relations
of the DHM is mathematically equal to the LPA in the
exact RG formulation of Wilson and Polchinski. In turn,
the latter is equivalent [80] via a change of variables to the
LPA in the Wetterich formulation – the one that we have
used in Sec. III – upon choosing the optimized regulator
proposed by Litim [59, 60].

10
Due to the fact that variations in the scale factor ℓ may
change the universality class of the model, the natural
formulation with blocks of size ℓ = 2 in the DHM is
not mathematically equivalent to the LPA. However, the
effect of such variation of ℓ in the critical exponents is
minimal [34]. This underlies the discrepancy observed in
Fig. 5.
For completeness, we also report in Fig. 6 a comprehensive picture of the first few RG eigenvalues, where y1 =
ν −1 and ω = −y2 is the so-called ‘correction-to-scaling’
exponent. In the region 0 < σ ≤ 1/2 the Gaussian fixed
point dictates the universal properties of the system and
the eigenvalues are given by yn = n(σ − 1) + 1 [33]. As
we cross σ = 1/2 towards larger values, as in Fig. 5,
the Gaussian fixed point exchanges stability with the interacting one, whose RG eigenvalues are computed via
FRG (filled circles) or the method of [33] (crosses). Not
only the thermal eigenvalue y1 , but also the eigenvalues
yn>1 corresponding to irrelevant perturbations exhibit
the LPA-DHM correspondence described previously. The
discrepancy between the two methods is quantitatively
comparable to that for y1 .

0.5

yn

0.0

−0.5
−1.0
−1.5
−2.0

y1
y2
y3

0.0

0.2

0.4

0.6

0.8

1.0

σ
FIG. 6. First three RG eigenvalues y1 , y2 , y3 computed by
means of the FRG of Sec. III (filled circles) or the RG for the
DHM of Sec. IV C (crosses). We find close agreement between
the latter methods around the interacting fixed-point, while
the eigenvalues are exact (solid lines) for the Gaussian region
0 < σ < 1/2.

An interesting open question concerns the critical exponents of the theory (35) studied by means of the FRG
with an appropriate generalization of the regulator (7)
where q σ would be replaced by ω(q). In that case, on the
basis of the previous discussion, we expect to find exactly
the same critical exponents as those of the DHM.

V.

COMPARISON WITH OTHER METHODS

In this section, we compare our numerical estimates
with known analytical and numerical results for the Ising
model. For the sake of the following comparisons, the
LPA and DHM are effectively equivalent, and we will
refer mostly to the LPA of Sec. III.
In Ref. [27] the second-order ϵ-expansion around the
mean-field threshold d = 2σ was reported.
ν −1 =

σ
ϵ
ϵ2
= σ − − A(σ) + O(ϵ3 ),
γ
3
9

(44)

where ϵ = 2σ−d = 2σ−1, A(σ) = ψ(1)−2ψ(σ/2)+ψ(σ),
and ψ(·) is the digamma function. In Fig. 1 Eq. (44) is
shown as the dotted black line and closely follows the
LPA estimates in the region σ ∈ (0.5, 0.55), while departing for σ >
∼ 0.6.
A more thorough weak-coupling expansion was carried
out for long-range models in [69, 81]. This work provides
three-loop estimates of the critical exponents in the ϵexpansion. In order to obtain accurate results, one additionally needs to perform a Padé-Borel resummation of
the three-loop series. The results are plotted in Fig. 1
as pink stars. At σ = 0.6, these higher-order corrections
realign the perturbative results with the LPA, while at
σ = 0.7 and 0.8, the exponent ν −1 becomes compatible
with [21] and larger than the LPA one.
In the strong-coupling limit σ → 1 the LPA reproduces the expected divergence of the correlation length
exponent, but cannot capture the exact slope, which was
obtained in the perturbative RG approach of Kosterlitz [23]. Indeed, the alternating domain walls are appropriate weakly coupled degrees of freedom in the region close to σ = 1, see the end of Sec. I as well as
Ref. [15]. Within the domain wall formulation, one obtains η(σ) = 2 − σ and
p
ν(σ)−1 = 2(1 − σ) + O(1 − σ),
(45)
which is the solid line of Fig. 1. Recently, Ref. [25] improved the result in Eq. (45), giving for the √
scaling dimension of the dual of the ϕ2 field ∆ϵ = 1 − 2δ + δ/4,
with δ = 1 − σ. Using the relation between ν and ∆ϵ
with d = 1 in the results of [25] then gives
ν(σ)−1 =

p

2(1 − σ) −

1−σ
+ O((1 − σ)3/2 ).
4

(46)

While the correction of [25] moves the curve of ν −1 (the
dashed line in Fig. 1) closer to the LPA estimate, the
slope of the two curves are still different at σ → 1− .
One reason for the slope discrepancy may be the missing
short-range term q 2 in the our LPA ansatz (4). At larger
dimensions, which also include quantum 1D LRI model,
the FRG reproduces correctly both the weak and strong
coupling limits close to σ = σmf and σ = σ∗ , see Fig. (3a)
of [82]. As anticipated in the Introduction, we see that
∗
the topological effects at σ <
∼ σ = 1 become particularly

11
strong, so that both the LPA (4) and the hierarchical
approximation become unsatisfactory. The improvement
of our theoretical description in this sense – as well as
the possibility of dealing with the field theory of [25, 26]
within FRG – is deferred to future work.
Consistently with the previous analysis, the comparison between the MC estimate of the critical exponents
and the LPA results strongly depends on the σ region,
see Fig. 1. The MC results of Ref. [20] (orange squares)
approach the estimate in Eq. (46) for σ >
∼ 0.8, while for
σ <
0.8
they
become
compatible
with
the
LPA predic∼
tion (small red circles). Furthermore, we have included a
comparison with Ref. [21], whose MC points (empty blue
circles) are systematically higher than those of Ref. [20],
but remain overall consistent with the previous analysis
due to the larger error bars. The comparison with [20]
and [21] shows that the LPA yields accurate results in a
large σ interval, except in the vicinity of σ = 1.
A mapping was conjectured between the critical exponents value of the long-range model and those of
the corresponding local model in an effective dimension
Deff [83]. This mapping has been shown to be remarkably
useful in the past [22, 39] and, although not supported
beyond the LPA level [39, 44], it produces accurate estimates, within 5%, when applied to the exact values in
d = 2 [58]. In the current d = 1 case, one finds
νLR (σ) = Deff νSR (Deff ),

(47)

with σ = (2 − ηSR (Deff ))/Deff . Then, we can take Deff ∈
{2, 3, 4}, ηSR (Deff ) ∈ {1/4, ηCB , 0}, and νSR (Deff ) ∈
{1, νCB , 1/2}, where the three-dimensional exponents
ηCB and νCB are the recent conformal bootstrap values
taken from [84]. The corresponding points are shown as
green triangles in Fig. 1. Overall, the results of the effective dimension approach overshoot the MC results by
Ref. [20]. This is most likely the result of the approximate nature of the effective dimension approach.
In summary, the LPA study produces a critical exponent ν −1 (σ) well in agreement with the perturbative
curve as σ → σmf = 1/2, while it remains consistently
below the strong coupling expansion as σ → σ∗ = 1.
Based on the comparison with MC data and the effective
dimension mapping, the accuracy of the LPA estimates is
accurate up to σ ≈ 0.8. Moreover, since the perturbative
expansions and (almost) all Monte Carlo data points lie
above our LPA/DHM curve, we may conclude that the
exponent ν −1 of the DHM appears to be a lower bound
for the exponent ν −1 of the 1D LRI model, in qualitative
agreement with the general strategy of using the DHM
to prove bounds for the 1D LRI.

VI.

CONCLUSIONS

In this work, we analyzed the critical behavior of the
one-dimensional long-range Ising (1D LRI) model by employing two complementary non-perturbative methods:

the functional renormalization group (FRG) in the local potential approximation (LPA), and real-space renormalization of Dyson’s hierarchical model (DHM). Despite their conceptual differences — the LPA being a
momentum-space continuum approach and the DHM a
discrete, non-translationally invariant lattice model —
we have shown that their predictions for the critical exponent ν are nearly indistinguishable across the entire
long-range interacting regime 1/2 < σ < 1.
We have argued that this remarkable agreement arises
from a deeper structural analogy between the two formulations. In particular, both frameworks retain a fixed
gradient term and renormalize only the local potential,
with the DHM providing a constructive realization of this
truncation. Furthermore, the use of the optimized Litim
regulator (7) in the LPA enhances this correspondence
by mirroring the features of the hierarchical RG transformation.
Comparisons with perturbative expansions near σ =
1/2 and recent conformal field theory (CFT) results near
σ = 1 provide a consistent validation of the LPA and
DHM approximations, while also delineating their limitations. Our analysis underscores the difficulty of accurately capturing BKT-like transitions and topological phenomena as σ approaches 1, where both approximations begin to falter (despite having the correct feature ν −1 for σ → 1− ), primarily due to their neglect
of short-range operators and topological defects. Nevertheless, Monte Carlo simulations indicate that the LPA
retains quantitative reliability across a broad intermediate regime, extending up to σ ≈ 0.8. Taken together,
these findings yield a well-defined curve for the critical
exponent ν in the classical Ising model in d = 1. For
σ<
∼ 0.8, the Ising curve closely follows the LPA predic<
tion, while in the range 0.8 <
∼ σ ∼ 1, it is rather close
to the CFT estimate given in Eq. (46) and consistently
above LPA results.
Looking forward, several interesting directions emerge.
First, it would be desirable to improve upon the LPA by
incorporating the effects of short-range analytic terms
and testing the robustness of the observed equivalence
beyond leading-order truncations. Additionally, adapting the FRG framework to study the effective DHM field
theory – with its hierarchical Laplacian dispersion ω(q)
– may allow for a direct and controlled comparison with
numerical RG flows. From a broader perspective, the
methods and analogies presented here may inform the
treatment of more complex systems exhibiting long-range
interactions, including quantum spin chains and out-ofequilibrium models [6, 85].
Finally, the close correspondence between the DHM
and the LPA offers not only computational advantages
but also conceptual clarity in the understanding of longrange critical phenomena, suggesting that hierarchical
models may serve as effective surrogates for more realistic systems in suitable regimes.
Note added. During the completion of this work, we
became aware of a related preprint [86], analyzing the

12
1D LRI model via real-space RG, and reporting finitetemperature phases for the ferromagnetic and spin-glass
regimes but no ordered phase in the antiferromagnetic
case.

[1] N. Defenu, T. Donner, T. Macrı̀, G. Pagano, S. Ruffo,
and A. Trombettoni, Long-range interacting quantum
systems, Reviews of Modern Physics 95, 035002 (2023).
[2] J. W. Britton, B. C. Sawyer, A. C. Keith, C.-C. J.
Wang, J. K. Freericks, H. Uys, M. J. Biercuk, and J. J.
Bollinger, Engineered two-dimensional Ising interactions
in a trapped-ion quantum simulator with hundreds of
spins, Nature 484, 489 (2012).
[3] T. Lahaye, C. Menotti, L. Santos, M. Lewenstein, and
T. Pfau, The physics of dipolar bosonic quantum gases,
Reports on Progress in Physics 72, 126401 (2009).
[4] A. Browaeys and T. Lahaye, Many-body physics with
individually controlled Rydberg atoms, Nature Physics
16, 132 (2020).
[5] H. Ritsch, P. Domokos, F. Brennecke, and T. Esslinger,
Cold atoms in cavity-generated dynamical optical potentials, Reviews of Modern Physics 85, 553 (2013).
[6] N. Defenu, A. Lerose, and S. Pappalardi, Out-ofequilibrium dynamics of quantum many-body systems
with long-range interactions, Physics Reports 1074, 1
(2024).
[7] A. Campa, T. Dauxois, and S. Ruffo, Statistical mechanics and dynamics of solvable models with long-range interactions, Physics Reports 480, 57 (2009).
[8] F. J. Dyson, Existence of a phase-transition in a onedimensional Ising ferromagnet, Commun. Math. Phys.
12, 91 (1969).
[9] D. Ruelle, Statistical mechanics of a one-dimensional lattice gas, Communications in Mathematical Physics 9, 267
(1968).
[10] J. Fröhlich and T. Spencer, The phase transition in the
one-dimensional Ising model with 1/rˆ2 interaction energy, Commun. Math. Phys. 84, 87 (1982).
[11] D. Thouless, Long-range order in one-dimensional Ising
systems, Physical Review 187, 732 (1969).
[12] F. J. Dyson, An Ising ferromagnet with discontinuous
long-range order, Comm. Math. Phys. 21, 269 (1971).
[13] G. Yuval and P. Anderson, Exact results for the Kondo
problem: One-body theory and extension to finite temperature, Physical Review B 1, 1522 (1970).
[14] P. W. Anderson, G. Yuval, and D. Hamann, Exact results in the Kondo problem. II. Scaling theory, qualitatively correct solution, and some new results on onedimensional classical statistical models, Physical Review
B 1, 4464 (1970).

ACKNOWLEDGMENTS

GG acknowledges the support of the MSCA Grant
101152898 (DREAMS). This research was funded by
the Swiss National Science Foundation (SNSF) grant
numbers 200021–207537 and 200021–236722, by the
Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) under Germany’s Excellence Strategy
EXC2181/1-390900948 (the Heidelberg STRUCTURES
Excellence Cluster) and by the European Union under
GA No. 101077500–QLRNet. Partial support by grant
NSF PHY-230935 to the Kavli Institute for Theoretical
Physics (KITP) is also acknowledged.

[15] P. Anderson and G. Yuval, Some numerical results on the
Kondo problem and the inverse square one-dimensional
Ising model, Journal of Physics C: Solid State Physics 4,
607 (1971).
[16] K. G. Wilson and J. Kogut, The renormalization group
and the ϵ expansion, Physics reports 12, 75 (1974).
[17] J. L. Cardy, One-dimensional models with 1/r2 interactions, Journal of Physics A: Mathematical and General
14, 1407 (1981).
[18] A. J. Leggett, S. Chakravarty, A. T. Dorsey, M. P. Fisher,
A. Garg, and W. Zwerger, Dynamics of the dissipative two-state system, Reviews of Modern Physics 59,
1 (1987).
[19] E. Luijten and H. W. Blöte, Classical critical behavior
of spin models with long-range interactions, Physical Review B 56, 8945 (1997).
[20] K. Uzelac, Z. Glumac, and A. Aničić, Critical behavior of
the long-range Ising chain from the largest-cluster probability distribution, Physical Review E 63, 037101 (2001).
[21] Y. Tomita, Monte Carlo study of one-dimensional Ising
models with long-range interactions, Journal of the Physical Society of Japan 78, 014002 (2008).
[22] M. C. Angelini, G. Parisi, and F. Ricci-Tersenghi, Relations between short-range and long-range Ising models,
Physical Review E 89, 062120 (2014).
[23] J. Kosterlitz, Phase transitions in long-range ferromagnetic chains, Physical Review Letters 37, 1577 (1976).
[24] S. A. Cannas, One-dimensional Ising model with longrange interactions: A renormalization-group treatment,
Physical Review B 52, 3034 (1995).
[25] D. Benedetti, E. Lauria, D. Mazáč, and P. van Vliet,
One-Dimensional Ising Model with 1/r 1.99 Interaction,
Physical Review Letters 134, 201602 (2025).
[26] D. Benedetti, E. Lauria, D. Mazac, and P. van Vliet, A
strong-weak duality for the 1d long-range Ising model,
arXiv:2509.05250 (2025).
[27] M. E. Fisher, S.-k. Ma, and B. Nickel, Critical exponents
for long-range interactions, Physical Review Letters 29,
917 (1972).
[28] J. Sak, Recursion relations and fixed points for ferromagnets with long-range interactions, Physical Review B 8,
281 (1973).
[29] C. Wetterich, Exact evolution equation for the effective
potential, Phys. Lett. B 301, 90 (1993).
[30] N. Tetradis and C. Wetterich, Critical exponents from

13
the effective average action, Nuclear Physics B 422, 541
(1994).
[31] J. Berges, N. Tetradis, and C. Wetterich, Nonperturbative renormalization flow in quantum field theory and
statistical physics, Phys. Rept. 363, 223 (2002).
[32] N. Dupuis, L. Canet, A. Eichhorn, W. Metzner, J. M.
Pawlowski, M. Tissier, and N. Wschebor, The nonperturbative functional renormalization group and its applications, Phys. Rept. 910, 1 (2021).
[33] D. Kim and C. Thompson, Critical properties of Dyson’s
hierarchical model, Journal of Physics A: Mathematical
and General 10, 1579 (1977).
[34] Y. Meurice, Nonlinear aspects of the renormalization
group flows of Dyson’s hierarchical model, Journal
of Physics A: Mathematical and Theoretical 40, R39
(2007).
[35] P. M. Bleher and J. G. Sinai, Investigation of the critical point in models of the type of Dyson’s hierarchical
models, Communications in Mathematical Physics 33, 23
(1973).
[36] P. Bleher and Y. G. Sinai, Critical indices for Dyson’s
asymptotically-hierarchical models, Communications in
Mathematical Physics 45, 247 (1975).
[37] P. Bleher, Critical phenomena in the Dyson hierarchical model and renormalization group, arXiv:1010.5855
(2010).
[38] N. Defenu, A. Codello, S. Ruffo, and A. Trombettoni,
Criticality of spin systems with weak long-range interactions, Journal of Physics A: Mathematical and Theoretical 53, 143001 (2020).
[39] N. Defenu, A. Trombettoni, and A. Codello, Fixed-point
structure and effective fractional dimensionality for O(N )
models with long-range interactions, Physical Review E
92, 052113 (2015).
[40] C. Behan, L. Rastelli, S. Rychkov, and B. Zan, Longrange critical exponents near the short-range crossover,
Physical review letters 118, 241601 (2017).
[41] E. Luijten, Interaction range, universality and the upper
critical dimension, Ph.D. thesis (1997).
[42] K. Fukui and S. Todo, Order-N cluster Monte Carlo
method for spin systems with long-range interactions,
Journal of Computational Physics 228, 2629 (2009).
[43] T. Horita, H. Suwa, and S. Todo, Upper and lower critical
decay exponents of Ising ferromagnets with long-range
interaction, Physical Review E 95, 012143 (2017).
[44] C. Behan, L. Rastelli, S. Rychkov, and B. Zan, A scaling
theory for the long-range to short-range crossover and an
infrared duality, Journal of Physics A: Mathematical and
Theoretical 50, 354002 (2017).
[45] C. Behan, Bootstrapping the long-range ising model in
three dimensions, Journal of Physics A: Mathematical
and Theoretical 52, 075401 (2019).
[46] C. Behan, E. Lauria, M. Nocchi, and P. van Vliet, Analytic and numerical bootstrap for the long-range Ising
model, Journal of High Energy Physics 2024, 136 (2024).
[47] G. Giachetti, N. Defenu, S. Ruffo, and A. Trombettoni, Berezinskii-Kosterlitz-Thouless phase transitions
with long-range couplings, Phys. Rev. Lett. 127, 156801
(2021).
[48] G. Giachetti, A. Trombettoni, S. Ruffo, and N. Defenu, Berezinskii-Kosterlitz-Thouless transitions in classical and quantum long-range systems, Phys. Rev. B 106,
014106 (2022).
[49] G. Giachetti, N. Defenu, S. Ruffo, and A. Trombettoni,

Self-consistent harmonic approximation in presence of
non-local couplings(a), EPL 133, 57004 (2021).
[50] G. Giachetti, N. Defenu, S. Ruffo, and A. Trombettoni,
Villain model with long-range couplings, Journal of High
Energy Physics 2023, 1 (2023).
[51] X. Tianning, Y. Dingyun, Z. Chao, F. Zhijie, and
D. Youjin, Two-dimensional XY Ferromagnet Induced by Long-range Interaction, Chin. Phys. Lett.
https://doi.org/10.1088/0256-307X/42/7/070002
(2025).
[52] G. Gori, M. Michelangeli, N. Defenu, and A. Trombettoni, One-dimensional long-range percolation: A numerical study, Physical Review E 96, 012108 (2017).
[53] D. J. Amit and V. Martin-Mayor, Field theory, the renormalization group, and critical phenomena: graphs to
computers (World Scientific Publishing Company, 2005).
[54] T. R. Morris, The exact renormalization group and approximate solutions, International Journal of Modern
Physics A 9, 2411 (1994).
[55] A. Lischke, G. Pang, M. Gulian, F. Song, C. Glusa,
X. Zheng, Z. Mao, W. Cai, M. M. Meerschaert,
M. Ainsworth, et al., What is the fractional Laplacian?
A comparative review with new results, Journal of Computational Physics 404, 109009 (2020).
[56] J. Honkonen and M. Y. Nalimov, Crossover between field
theories with short-range and long-range exchange or correlations, Journal of Physics A: Mathematical and General 22, 751 (1989).
[57] I. Balog, G. Tarjus, and M. Tissier, Critical behaviour
of the random-field Ising model with long-range interactions in one dimension, Journal of Statistical Mechanics:
Theory and Experiment 2014, P10017 (2014).
[58] A. Solfanelli and N. Defenu, Universality in long-range
interacting systems: The effective dimension approach,
Physical Review E 110, 044121 (2024).
[59] D. F. Litim, Optimization of the exact renormalization
group, Phys. Lett. B 486, 92 (2000).
[60] D. F. Litim, Optimized renormalization group flows,
Phys. Rev. D 64, 105007 (2001).
[61] I. Nándori, I. G. Márián, and V. Bacsó, Spontaneous
symmetry breaking and optimization of functional renormalization group, Physical Review D 89, 047701 (2014).
[62] N. Defenu and A. Codello, Scaling solutions in the derivative expansion, Physical Review D 98, 016013 (2018).
[63] T. R. Morris, Derivative expansion of the exact renormalization group, Physics Letters B 329, 241 (1994).
[64] T. R. Morris, The renormalization group and two dimensional multicritical effective scalar field theory, Physics
Letters B 345, 139 (1995).
[65] T. R. Morris, On truncations of the exact renormalization
group, Physics Letters B 334, 355 (1994).
[66] A. Codello, Scaling solutions in a continuous dimension,
Journal of Physics A: Mathematical and Theoretical 45,
465006 (2012).
[67] J. Borchardt and B. Knorr, Global solutions of functional
fixed point equations via pseudospectral methods, Physical Review D 91, 105011 (2015).
[68] F. Ihssen, V. Pagni, J. Marino, S. Diehl, and N. Defenu,
Nonperturbative treatment of a quenched Langevin field
theory, Physical Review B 112, 024306 (2025).
[69] D. Benedetti, R. Gurau, and S. Harribey, Addendum:
Long-range multi-scalar models at three loops (2020 J.
Phys. A: Math. Theor. 53 445008), Journal of Physics A:
Mathematical and Theoretical 58, 129401 (2025).

14
[70] L. Capizzi, G. Giachetti, A. Santini, and M. Collura,
Spreading of a local excitation in a quantum hierarchical
model, Physical Review B 106, 134210 (2022).
[71] E. Agliari and F. Tavani, The exact Laplacian spectrum
for the Dyson hierarchical network, Scientific reports 7,
39962 (2017).
[72] A. Abdesselam, A. Chandra, and G. Guadagni, Rigorous
quantum field theory functional integrals over the p-adics
I: anomalous dimensions, arXiv:1302.5971 (2013).
[73] A. Abdesselam, Towards three-dimensional conformal
probability, p-Adic Numbers, Ultrametric Analysis and
Applications 10, 233 (2018).
[74] B. Derrida and H. Spohn, Polymers on disordered trees,
spin glasses, and traveling waves, Journal of Statistical
Physics 51, 817 (1988).
[75] F. Gerbino, G. Giachetti, P. Le Doussal, and A. De Luca,
Measurement-induced phase transition in state estimation of chaotic systems and the directed polymer, Physical Review Research 7, 033105 (2025).
[76] C. Monthus, Dyson Hierarchical long-ranged quantum
spin-glass via real-space renormalization, Journal of
Statistical Mechanics: Theory and Experiment 2015,
P10024 (2015).
[77] L. P. Kadanoff, Scaling laws for Ising models near Tc ,
Physics Physique Fizika 2, 263 (1966).
[78] D. F. Litim, Towards functional flows for hierarchical
models, Physical Review D—Particles, Fields, Gravitation, and Cosmology 76, 105001 (2007).

[79] G. Felder, Renormalization group in the local potential
approximation, Commun. Math. Phys. 111, 101 (1987).
[80] T. R. Morris, Equivalence of local potential approximations, Journal of High Energy Physics 2005, 027 (2005).
[81] D. Benedetti, R. Gurau, S. Harribey, and K. Suzuki,
Long-range multi-scalar models at three loops, Journal
of Physics A: Mathematical and Theoretical 53, 445008
(2020).
[82] N. Defenu, A. Trombettoni, and S. Ruffo, Criticality
and phase diagram of quantum long-range O(N ) models, Physical Review B 96, 104432 (2017).
[83] R. Banos, L. Fernandez, V. Martin-Mayor, and A. Young,
Correspondence between long-range and short-range spin
glasses, Physical Review B—Condensed Matter and Materials Physics 86, 134416 (2012).
[84] C.-H. Chang, V. Dommes, R. S. Erramilli, A. Homrich,
P. Kravchuk, A. Liu, M. S. Mitchell, D. Poland, and
D. Simmons-Duffin, Bootstrapping the 3d Ising stress
tensor, Journal of High Energy Physics 2025, 1 (2025).
[85] P. Molignini and B. Chakrabarti, Unbounded entropy
production and violent fragmentation for repulsive-toattractive interaction quench in long-range interacting
systems, New Journal of Physics 26, 103030 (2024).
[86] E. Artun and A. N. Berker, Ferromagnetic and SpinGlass Finite-Temperature Order but no Antiferromagnetic Order in the d = 1 Ising Model with
Long-Range Power-Law Interactions, arXiv:2508.11168
https://doi.org/10.48550/arXiv.2508.11168 (2025).

