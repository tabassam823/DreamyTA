Quantum Econophysics
Esteban Guevara Hidalgo†‡

arXiv:physics/0609245v3 [physics.soc-ph] 8 Dec 2016

†

Departamento de Fı́sica, Escuela Politécnica Nacional, Quito, Ecuador
‡
SIÓN, Autopista General Rumiñahui, Urbanización Edén del Valle,
Sector 5, Calle 1 y Calle A # 79, Quito, Ecuador

The relationships between game theory and quantum mechanics let us propose certain quantization relationships through which we could describe and understand not only quantum but also
classical, evolutionary and the biological systems that were described before through the replicator
dynamics. Quantum mechanics could be used to explain more correctly biological and economical
processes and even it could encloses theories like games and evolutionary dynamics. This could
make quantum mechanics a more general theory that we had thought.
Although both systems analyzed are described through two apparently different theories (quantum mechanics and game theory) it is shown that both systems are analogous and thus exactly
equivalents. So, we can take some concepts and definitions from quantum mechanics and physics for
the best understanding of the behavior of economics and biology. Also, we could maybe understand
nature like a game in where its players compete for a common welfare and the equilibrium of the
system that they are members.
PACS numbers: 03.65.-w, 02.50.Le, 03.67.-a, 89.65.Gh

I.

INTRODUCTION

Could it have an relationship between quantum mechanics and game theories? An actual relationship between these theories that describe two apparently different systems would let us explain biological and economical processes through quantum mechanics, quantum information theory and statistical physics.
We also could try to find a method which let us make
quantum a classical system in order to analyze it from
a absolutely different perspective and under a physical
equilibrium principle which would have to be exactly
equivalent to the defined classically in economics or biology. Physics tries to describe approximately nature
which is the most perfect system. The equilibrium notion
in a physical system is the central cause for this perfection. We could make use of this physical equilibrium to
its application in conflictive systems like economics.
The present work analyze the relationships between
quantum mechanics and game theory and proposes
through certain quantization relationships a quantum understanding of classical systems.
II.

THE VON NEUMANN EQUATION & THE
STATISTICAL MIXTURE OF STATES

An ensemble is a collection of identically prepared
physical systems. When each member of the ensemble is
characterized by the same state vector |Ψ(t)i it is called
pure ensemble. If each member has a probability pi of being in the state |Ψi (t)i we have a mixed ensemble. Each
member of a mixed ensemble is a pure state and its evolution is given by Schrödinger equation. To describe correctly a statistical mixture of states it is necessary the

introduction of the density operator
ρ(t) =

n
X

pi |Ψi (t)i hΨi (t)|

(1)

i=1

which contains all the physically significant information
we can obtain about the ensemble in question. Any two
ensembles that produce the same density operator are
physically indistinguishable. The density operator can
be represented in matrix form. A pure state is specified
by pi = 1 for some |Ψi (t)i , i = 1, ..., n and the matrix
which represents it has all its elements equal to zero except one 1 on the diagonal. The diagonal elements ρnn
of the density operator ρ(t) represents the average probability of finding the system in the state |ni and its sum
is equal to 1. The non-diagonal elements ρnp expresses
the interference effects between the states |ni and |pi
which can appear when the state |Ψi i is a coherent linear superposition of these states. Suppose we make a
measurement on a mixed ensemble of some observable
A. The ensemble average of A is defined by the average
of the expected values measured in each member of the
ensemble described by |Ψi (t)i and with probability pi , it
means hAiρ = p1 hAi1 + p2 hAi2 + ... + pn hAin and can
be calculated by using
hAi = T r {ρ(t)A} .

(2)

The time evolution of the density operator is given by
the von Neumann equation
i~

i
dρ h
= Ĥ, ρ
dt

(3)

which is only a generalization of the Schrödinger equation
and the quantum analogue of Liouville’s theorem.

2
III.

THE REPLICATOR DYNAMICS & EGT

Game theory [1–3] is the study of decision making of
competing agents in some conflict situation. It has been
applied to solve many problems in economics, social sciences, biology and engineering. The central equilibrium
concept in game theory is the Nash Equilibrium which is
expressed through the following condition
E(p, p) ≥ E(r, p).

Evolutionary game theory [4–6] has been applied to the
solution of games from a different perspective. Through
the replicator dynamics it is possible to solve not only
evolutionary but also classical games. That is why EGT
has been considered like a generalization of classical game
theory. Evolutionary game theory does not rely on rational assumptions but on the idea that the Darwinian process of natural selection [7] drives organisms towards the
optimization of reproductive success [8]. Instead of working out the optimal strategy, the different phenotypes in
a population are associated with the basic strategies that
are shaped by trial and error by a process of natural selection or learning.
The model used in EGT is the following: Each agent
in a n-player game where the ith player has as strategy
space Si is modelled by a population of players which
have to be partitioned into groups. Individuals in the
same group would all play the same strategy. Randomly
we make play the members of the subpopulations against
each other. The subpopulations that perform the best
will grow and those that do not will shrink and eventually will vanish. The process of natural selection assures
survival of the best players at the expense of the others.
The natural selection process that determines how populations playing specific strategies evolve is known as the
replicator dynamics [5, 6, 9, 10]

n
n
X
X
dxi
=
aij xj −
akl xk xl  xi .
dt
j=1

The bonestone of EGT is the concept of evolutionary
stable strategy (ESS) [4, 11] that is a strengthened notion
of Nash equilibrium. It satisfies the following conditions
E(p, p) > E(r, p),
If E(p, p) = E(r, p) then E(p, r) > E(r, r),

(4)

Players are in equilibrium if a change in strategies by any
one of them (p → r) would lead that player to earn less
than if he remained with his current strategy (p).

dxi
= [fi (x) − hf (x)i] xi ,
dt



frequency. The stable fixed points of the replicator dynamics are Nash equilibria [2]. If a population reaches a
state which is a Nash equilibrium, it will remain there.

(7)

where p is the strategy played by the vast majority of
the population, and r is the strategy of a mutant present
in small frequency. Both p and r can be pure or mixed.
An ESS is described as a strategy which has the property that if all the members of a population adopt it, no
mutant strategy could invade the population under the
influence of natural selection. If a few individuals which
play a different strategy are introduced into a population in an ESS, the evolutionary selection process would
eventually eliminate the invaders.

IV.

RELATIONSHIPS BETWEEN QUANTUM
MECHANICS & GAME THEORY

A physical or a socioeconomical system (described
through quantum mechanics or game theory) is composed by n members (particles, subsystems, players,
states, etc.). Each member is described by a state or a
strategy which has assigned a determined probability (xi
or ρij ). The quantum mechanical system is described by
the density operator ρ whose elements represent the system average probability of being in a determined state. In
evolutionary game theory the system is defined through
a relative frequencies vector x whose elements can represent the frequency of players playing a determined strategy. The evolution of the density operator is described
by the von Neumann equation which is a generalization
of the Schrödinger equation. While the evolution of the
relative frequencies is described through the replicator
dynamics (5).

(5)
(6)

k,l=1

The element xi of the vector x is the probability of playing certain strategy or the relative frequency of individuals using that strategy. The fitness function fi =
P
n
how successful each subpopulation
j=1 aij xj specifies
Pn
is, hf (x)i = k,l=1 akl xk xl is the average fitness of the
population, and aij are the elements of the payoff matrix A. The replicator dynamics rewards strategies that
outperform the average by increasing their frequency, and
penalizes poorly performing strategies by decreasing their

It is important to note that the replicator dynamics
is a vectorial differential equation while von Neumann
equation can be represented in matrix form. If we would
like to compare both systems the first we would have
to do is to try to compare their evolution equations by
trying to find a matrix representation of the replicator
dynamics [12]
dX
= G + GT ,
dt

(8)

where the matrix X has as elements
1/2

xij = (xi xj )

(9)

3
The next table shows some specific resemblances between quantum statistical mechanics and evolutionary
game theory [13].

and

1
G + GT ij =
2
+
−

n
X

aik xk xij

k=1
n
X

1
2

Table 1
Quantum Statistical Mechanics

Evolutionary Game Theory

n system members

n population members

ajk xk xji

k=1
n
X

Each member in the state |Ψk i Each member plays strategy si

|Ψk i with
Ppk → ρij
ρ,
ihρii = i1
dρ
i~ dt = Ĥ, ρ
S = −T r {ρ ln ρ}

(10)

akl xk xl xij

k,l=1


are the elements of the matrix G + GT .

Although equation (8) is the matrix representation of
the replicator dynamics from which we could compare
and find a relationship with the von Neumann equation,
we can moreover find a Lax representation of the replicator dynamics by calling

In table 2 we show the properties of the matrixes ρ and
X.
Table 2
Density Operator Relative freq. Matrix

n

1X
(G1 )ij =
aik xk xij ,
2

ρ is Hermitian
T rρ(t) = 1
ρ2 (t) ⩽ ρ(t)
T rρ2 (t) ⩽ 1

(11)

k=1
n

1X
ajk xk xji ,
(G2 )ij =
2
(G3 )ij =

(12)

k=1
n
X

(13)

akl xk xl xij

k,l=1

the elements of the matrixes G1 , G2 and G3 that compose
by adding the matrix G + GT . The matrixes G1 , G2
and G3 can be also factorized in function of the matrixes
Q and X
G1 = QX,
G2 = XQ,
G3 = 2XQX,

(14)
(15)
(16)

where
Q is a diagonal matrix and has as elements qii =
1 Pn
2
k=1 aik xk . By using the fact that X = X we can
2
write the equation (8) like
dX
= QXX + XXQ − 2XQX
dt

(17)

and finally, by grouping into commutators and defining
Λ = [Q, X]
dX
= [Λ, X] .
dt
The matrix Λ has as elements
" n
!
X
1
(Λ)ij =
aik xk xij − xji
2
k=1

si P→ xi
X,
i xi = 1
dX
dt = [Λ, X]
P
H = − i xi ln xi

(18)

n
X

k=1

ajk xk

!#

.

This matrix commutative form of the replicator dynamics (18) follows the same dynamic as the von Neumann
equation (3) and the properties of their correspondent elements (matrixes) are similar, being the properties corresponding to our quantum system more general than the
properties of the classical system.

X is Hermitian
T rX = 1
X 2= X
T rX 2 (t) = 1

Although both systems are different, both are analogous and thus exactly equivalents.
V.

QUANTUM REPLICATOR DYNAMICS &
THE QUANTIZATION RELATIONSHIPS

The resemblances between both systems and the similarity in the properties of their corresponding elements
let us to define and propose the next quantization relationships
xi →

n
X

hi |Ψk i pk hΨk |i i = ρii ,

k=1

(xi xj )1/2 →

n
X

hi |Ψk i pk hΨk |j i = ρij .

(19)

k=1

A population will be represented by a quantum system
in which each subpopulation playing strategy si will be
represented by a pure ensemble in the state |Ψk (t)i and
with probability pk . The probability xi of playing strategy si or the relative frequency of the individuals using
strategy si in that population will be represented as the
probability ρii of finding each pure ensemble in the state
|ii [12].
Through these quantization relationships the replicator dynamics (in matrix commutative form) (18) takes
the form of the equation of evolution of mixed states (3).
And also
X −→ ρ,
i
Λ −→ − Ĥ,
~

(20)
(21)

4
where Ĥ is the Hamiltonian of the physical system.
The equation of evolution of mixed states from quantum statistical mechanics (3) is the quantum analogue
of the replicator dynamics in matrix commutative form
(18).

the pair (A, B) and it is defined by
X
pij log2 pij
H(A, B) ≡ −
while
H(A) = −

X

pij log2

GAMES THROUGH STATISTICAL
MECHANICS & QIT

H(B) = −

X

pij log2

Entropy is the central concept of information theories
[16, 17]. The Shannon entropy expresses the average information we expect to gain on performing a probabilistic
experiment of a random variable A which takes the values ai with the respective probabilities pi . It also can
be seen as a measure of uncertainty before we learn the
value of A. We define the Shannon entropy of a random
variable A by
H(A) ≡ H(p1 , ..., pn ) ≡ −

n
X

pi log2 pi .

(22)

i=1

The entropy of a random variable is completely determined by the probabilities of the different possible values that the random variable takes. Due to the fact that
p =P
(p1 , ..., pn ) is a probability distribution, it must satn
isfy i=1 pi = 1 and 0 ≤ p1 , ..., pn ≤ 1. The Shannon entropy of the probability distribution associated with the
source gives the minimal number of bits that are needed
in order to store the information produced by a source, in
the sense that the produced string can later be recovered.
The von Neumann entropy [16, 17] is the quantum analogue of Shannon’s entropy but it appeared 21 years before and generalizes Boltzmann’s expression. Entropy
in quantum information theory plays prominent roles in
many contexts, e.g., in studies of the classical capacity
of a quantum channel [18, 19] and the compressibility of
a quantum source [20, 21]. Quantum information theory
appears to be the basis for a proper understanding of the
emerging fields of quantum computation [22, 23], quantum communication [24, 25], and quantum cryptography
[26, 27].

X

(24)

pij ,

(25)

where pij is the joint probability to find A in state ai and
B in state bj .
The conditional entropy H(A | B) is a measure of how
uncertain we are about the value of A, given that we
know the value of B. The entropy of A conditional on
knowing that B takes the value bj is defined by
H(A | B) ≡ H(A, B) − H(B),
X
pij log2 pi|j ,
H(A | B) ≡ −

(26)

i,j

p

where pi|j = P ijpij is the conditional probability that A
i
is in state ai given that B is in state bj .
The mutual or correlation entropy H(A : B) measures
how much information A and B have in common. The
mutual or correlation entropy H(A : B) is defined by
H(A : B) ≡ H(A) + H(B) − H(A, B),
X
pij log2 pi:j ,
H(A : B) ≡ −

(27)

i,j

P

pij

P

pij

is the mutual probability. The
where pi:j = i pij j
mutual or correlation entropy also can be expressed
through the conditional entropy via
H(A : B) = H(A) − H(A | B),
H(A : B) = H(B) − H(B | A).

(28)
(29)

The joint entropy would equal the sum of each of A’s
and B’s entropies only in the case that there are no correlations between A’s and B’s states. In that case, the
mutual entropy or information vanishes and we could not
make any predictions about A just from knowing something about B.
The relative entropy H(p k q) measures the closeness
of two probability distributions, p and q, defined over the
same random variable A. We define the relative entropy
of p with respect to q by
X
X
pi log2 qi ,
pi log2 pi −
H(p k q) ≡
i

i

Suppose A and B are two random variables. The joint
entropy H(A, B) measures our total uncertainty about

pij ,

i

i,j

There exists a strong relationship between game theories, statistical mechanics and information theory. The
bonds between these theories are the density operator
and entropy [14, 15]. From the density operator we can
construct and understand the statistical behavior about
our system by using the statistical mechanics. Also we
can develop the system in function of its accessible information and analyze it through information theories
under a criterion of maximum or minimum entropy.

X
j

i,j

VI.

(23)

i,j

H(p k q) ≡ −H(A) −

X
i

pi log2 qi .

(30)

5
The relative entropy is non-negative, H(p k q) ≥ 0, with
equality if and only if p = q. The classical relative entropy of two probability distributions is related to the
probability of distinguishing the two distributions after a
large but finite number of independent samples (Sanov’s
theorem) [28].
By analogy with the Shannon entropies it is possible
to define conditional, mutual and relative quantum entropies. Quantum entropies also satisfies many other interesting properties that do not satisfy their classical analogues. For example, the conditional entropy can be negative and its negativity always indicates that two systems
are entangled and indeed, how negative the conditional
entropy is provides a lower bound on how entangled the
two systems are [29].
By other hand, in statistical mechanics entropy can
be regarded as a quantitative measure of disorder. It
takes its maximum possible value in a completely random ensemble in which all quantum mechanical states
are equally likely and is equal to zero in the case of a pure
ensemble which has a maximum amount of order because
all members are characterized by the same quantum mechanical state ket.
From both possible points of view and analysis (statistical mechanics or information theories) of the same
system its entropy is exactly the same. Lets consider
a system composed by N members, players, strategies,
states, etc. This system is described completely through
certain density operator ρ, its evolution equation (the
von Neumann equation) and its entropy. Classically, the
system is described through the matrix of relative frequencies X, the replicator dynamics and the Shannon
entropy. For the quantum case we define the von Neumann entropy as

In a far from equilibrium system the von Neumann
vary in time until it reaches its maximum value. When
the dynamics is chaotic the variation with time of the
physical entropy goes through three successive, roughly
separated stages [30]. In the first one, S(t) is dependent
on the details of the dynamical system and of the initial
distribution, and no generic statement can be made. In
the second stage, S(t) is a linear increasing function of
time ( dS
dt = const.). In the third stage, S(t) tends asymptotically towards the constant value which characterizes
equilibrium ( dS
dt = 0). With the purpose of calculating
the time evolution of entropy we approximate the logarithm of ρ by series ln ρ = (ρ− I)− 21 (ρ− I)2 + 31 (ρ− I)3 ...
[15]
dS(t)
11 P dρii
=
dt
6 i dt
P dρji
−6 ρij
dt
i,j
9 P
dρki
+
ρ ρ
2 i,j,k ij jk dt
dρli
4 P
ρ ρ ρ
+ ζ.
−
3 i,j,k,l ij jk kl dt

(34)

In general entropy can be maximized subject to different constrains. In each case the result is the condition the
system must follow to maximize its entropy. Generally,
this condition is a probability distribution function. We
can obtain the density operator from the study of an ensemble in thermal equilibrium. Nature tends to maximize
entropy subject to the constraint that the ensemble average of the Hamiltonian has a certain prescribed value.
We will maximize S by requiring that
X
δρii (ln ρii + 1) = 0
(35)
δS = −
i

S = −T r {ρ ln ρ}

(31)

and for the classical case
H =−

X

xii ln xii

(32)

i

i=1

which is the Shannon entropy over the relative frequencies vector x (the diagonal elements of X).
We can describe the evolution of the entropy of our
classical system H(t) by supposing that the vector of relative frequencies x(t) evolves in time following the replicator dynamics [15]
n
o
dH
= T r U (H̃ − X) ,
dt

subject to the constrains δT r (ρ) = 0 and δ hEi = 0. By
using Lagrange multipliers
X
δρii (ln ρii + βEi + γ + 1) = 0
(36)
and the normalization condition T r(ρ) = 1 we find that
e−βEi
ρii = P −βEk
ke

which is the condition that the density operator and its
elements must satisfy to our system tends to maximize
its entropy S. If we maximize S without the internal
energy constrain δ hEi = 0 we obtain

(33)

where H̃ is a diagonal matrix whose trace is equal
to the Shannon entropy i.e. H = T rH̃ and Ui =
[fi (x) − hf (x)i].

(37)

ρii =

1
N

(38)

which is the β → 0 limit (“high - temperature limit”) in
equation (37) in where a canonical ensemble becomes a

6
completely random ensemble in which all energy eigenstates are equally populated. In the opposite low - temperature limit β → ∞ tell us that a canonical ensemble
becomes a pure ensemble where only the ground state is
populated. The parameter β is related to the “temperature” τ as follows
β=

1
.
τ

(39)

By replacing ρii obtained in the equation (37) in the von
Neumann entropy we can
it in function of the
P rewrite
−βEk
, β and hEi through
partition function Z =
ke
the next equation
S = ln Z + β hEi .

(40)

From the partition function we can know some parameters that define the system like
1 ∂Z
∂ ln Z
=−
,
Z ∂β
∂β
∂ hEi
1 ∂S
=−
=−
.
∂β
β ∂β

hEi = −

(41)

∆E 2

(42)

We can also analyze the variation of entropy with respect
to the average energy of the system
1
∂S
= ,
∂ hEi
τ
∂2S
1 ∂τ
2 = − τ 2 ∂ hEi
∂ hEi

(43)
(44)

and with respect to the parameter β
∂S
= −β ∆E 2 ,
∂β
∂ hEi
∂ 2 hEi
∂2S
=
.
+
β
∂β
∂β 2
∂β 2
VII.

(45)
(46)

FROM CLASSICAL TO QUANTUM

The resemblances between both systems (described
through quantum mechanics and EGT) apparently different but analogous and thus exactly equivalents and
the similarity in the properties of their corresponding
elements let us to define and propose the quantization
relationships like in section 5.
It is important to note that equation (18) is nonlinear while its quantum analogue is linear. This means
that the quantization eliminates the nonlinearities. Also
through this quantization the classical system that were
described through a diagonal matrix X can be now described through a density operator which not neccesarily
must describe a pure state, i.e. its non diagonal elements
can be different from zero representing a mixed state due
to the coherence between quantum states that were not
present through a classical analysis.

Through the relationships between both systems we
could describe classical, evolutionary, quantum and also
the biological systems that were described before through
evolutionary dynamics with the replicator dynamics. We
could explain through quantum mechanics biological and
economical processes being a much more general theory
that we had thought. It could even encloses theories like
games and evolutionary dynamics.
Problems in economy and finance have attracted the
interest of statistical physicists. Kobelev et al [31] used
methods of statistical physics of open systems for describing the time dependence of economic characteristics
(income, profit, cost, supply, currency, etc.) and their
correlations with each other. Antoniou et al [32] introduced a new approach for the presentation of economic
systems with a small number of components as a statistical system described by density functions and entropy. This analysis is based on a Lorenz diagram and
its interpolation by a continuos function. Conservation
of entropy in time may indicate the absence of macroscopic changes in redistribution of resources. Assuming
the absence of macro-changes in economic systems and
in related additional expenses of resources, we may consider the entropy as an indicator of efficiency of the resources distribution. Statistical physicists are also extremely interested in economic fluctuations [33] in order
to help our world financial system avoid “economic earthquakes”. Also it is suggested that in the field of turbulence, we may find some crossover with certain aspects of
financial markets. Statistical mechanics and economics
study big ensembles: collections of atoms or economic
agents, respectively. The fundamental law of equilibrium
statistical mechanics is the Boltzmann-Gibbs law, which
states that the probability distribution of energy E is
P (E) = Ce−E/T , where T is the temperature, and C is a
normalizing constant. The main ingredient that is essential for the derivation of the Boltzmann-Gibbs law is the
conservation of energy. Thus, one may generalize that
any conserved quantity in a big statistical system should
have an exponential probability distribution in equilibrium [34]. In a closed economic system, money is conserved. Thus, by analogy with energy, the equilibrium
probability distribution of money must follow the exponential Boltzmann-Gibbs law characterized by an effective temperature equal to the average amount of money
per economic agent. Drăgulescu and Yakovenko demonstrated how the Boltzmann-Gibbs distribution emerges
in computer simulations of economic models. They considered a thermal machine, in which the difference of temperature allows one to extract a monetary profit. They
also discussed the role of debt, and models with broken
time-reversal symmetry for which the Boltzmann-Gibbs
law does not hold. Recently the insurance market, which
is one of the important branches of economy, have attracted the attention of physicists [35]. The maximum
entropy principle is used for pricing the insurance. Darooneh obtained the price density based on this principle,

7
applied it to multi agents model of insurance market and
derived the utility function. The main assumption in his
work is the correspondence between the concept of the
equilibrium in physics and economics. He proved that
economic equilibrium can be viewed as an asymptotic
approximation to physical equilibrium and some difficulties with mechanical picture of the equilibrium may
be improved by considering the statistical description of
it. TopsØe [36] also has suggested that thermodynamical
equilibrium equals game theoretical equilibrium. Quantum games have proposed a new point of view for the
solution of the classical problems and dilemmas in game
theory. Quantum games are more efficient than classical games and provide a saturated upper bound for this
efficiency [37–42].
Nature may be playing quantum survival games at the
molecular level [43, 44]. It could lead us to describe
many of the life processes through quantum mechanics
like Gogonea and Merz [45] who indicated that games are
being played at the quantum mechanical level in protein
folding. Gafiychuk and Prykarpatsky [46] applied the
replicator equations written in the form of nonlinear von
Neumann equations to the study of the general properties
of the quasispecies dynamical system from the standpoint
of its evolution and stability. They developed a mathematical model of a naturally fitted coevolving ecosystem
and a theoretical study a self-organization problem of
an ensemble of interacting species. The genetic code is
the relationship between the sequence of the bases in the
DNA and the sequence of amino acids in proteins. Recent
work [47] about evolvability of the genetic code suggests
that the code is shaped by natural selection. DNA is
a nonlinear dynamical system and its evolution is a sequence of chemical reactions. An abstract DNA-type system is defined by a set of nonlinear kinetic equations with
polynomial nonlinearities that admit soliton solutions associated with helical geometry. Aerts and Czachor [48]
shown that the set of these equations allows for two different Lax representations: They can be written as von Neumann type nonlinear systems and they can be regarded
as a compatibility condition for a Darboux-covariant Lax
pair. Organisms whose DNA evolves in a chaotic way
would be eliminated by natural selection. They also explained why non-Kolmogorovian probability models occurring in soliton kinetics are naturally associated with
chemical reactions. Patel [49, 50] suggested quantum dynamics played a role in the DNA replication and the optimization criteria involved in genetic information processing. He considers the criteria involved as a task similar
to an unsorted assembly operation where the Grover’s
database search algorithm fruitfully applies; given the
different optimal solutions for classical and quantum dynamics. Turner and Chao [51] studied the evolution of
competitive interactions among viruses in an RNA phage,
and found that the fitness of the phage generates a payoff
matrix conforming to the two-person prisoner’s dilemma
game. Bacterial infections by viruses have been presented

as classical game-like situations where nature prefers the
dominant strategies. Azhar Iqbal [42] showed results in
which quantum mechanics has strong and important roles
in selection of stable solutions in a system of interacting entities. These entities can do quantum actions on
quantum states. It may simply consists of a collection
of molecules and the stability of solutions or equilibria
can be affected by quantum interactions which provides
a new approach towards theories of rise of complexity in
groups of quantum interacting entities. Neuroeconomics
[52, 53] may provide an alternative to the classical Cartesian model of the brain and behavior [54] through a rich
dialogue between theoretical neurobiology and quantum
logic [55, 56].
The results shown in this study on the relationships between quantum mechanics and game theories are a reason
of the applicability of physics in economics and biology.
Both systems described through two apparently different
theories are analogous and thus exactly equivalents. So,
we can take some concepts and definitions from quantum mechanics and physics for the best understanding of
the behavior of economics and biology. Also, we could
maybe understand nature like a game in where its players compete for a common welfare and the equilibrium of
the system that they are members.

VIII.

ON A QUANTUM UNDERSTANDING OF
CLASSICAL SYSTEMS

If our systems are analogous and thus exactly equivalents, our physical equilibrium (maximum entropy)
should be also exactly equivalent to our socieconomical
equilibrium. If in an isolated system each of its accessible states do not have the same probability, the system
is not in equilibrium. The system will vary and will evolution in time until it reaches the equilibrium state in
where the probability of finding the system in each of
the accessible states is the same. The system will find
its more probable configuration in which the number of
accessible states is maximum and equally probable. The
whole system will vary and rearrange its state and the
states of its ensembles with the purpose of maximize its
entropy and reach its maximum entropy state. We could
say that the purpose and maximum payoff of a physical
system is its maximum entropy state. The system and
its members will vary and rearrange themselves to reach
the best possible state for each of them which is also the
best possible state for the whole system.
This can be seen like a microscopical cooperation between quantum objects to improve their states with the
purpose of reaching or maintaining the equilibrium of the
system. All the members of our quantum system will play
a game in which its maximum payoff is the equilibrium of
the system. The members of the system act as a whole
besides individuals like they obey a rule in where they

8
prefer the welfare of the collective over the welfare of the
individual. This equilibrium is represented in the maximum system entropy in where the system resources are
fairly distributed over its members. A system is stable
only if it maximizes the welfare of the collective above the
welfare of the individual. If it is maximized the welfare of
the individual above the welfare of the collective the system gets unstable and eventually it collapses (Collective
Welfare Principle [12, 13, 15]).
Fundamentally, we could distinguish three states in every system: minimum entropy, maximum entropy, and
when the system is tending to whatever of these two
states. The natural trend of a physical system is to the
maximum entropy state. The minimum entropy state is
a characteristic of a manipulated system i.e. externally
controlled or imposed. A system can be internally or externally manipulated or controlled with the purpose of
guide it to a state of maximum or minimum entropy depending of the ambitions of the members that compose
it or the people who control it.
There exists tacit rules inside a system. These rules do
not need to be specified or clarified and search the system
equilibrium under the collective welfare principle. The
other prohibitive and repressive rules are imposed over
the system when one or many of its members violate the
collective welfare principle and search to maximize its
individual welfare at the expense of the group. Then it
is necessary to establish regulations on the system to try
to reestablish the broken natural order.

to explain more correctly biological and economical processes and even encloses theories like games and evolutionary dynamics.
The quantum analogues of the relative frequencies matrix, the replicator dynamics and the Shannon entropy
are the density operator, the von Neumann equation
and the von Neumann entropy. Every game (classical,
evolutionary or quantum) can be described quantically
through these three elements.
The bonds between game theories, statistical mechanics and information theory are the density operator and
entropy. From the density operator we can construct and
obtain all the mechanical statistical information about
our system. Also we can develop the system in function
of its information and analyze it through information theories under a criterion of maximum or minimum entropy.
Although both systems analyzed are described through
two apparently different theories (quantum mechanics
and game theory) both are analogous and thus exactly
equivalents. So, we can take some concepts and definitions from quantum mechanics and physics for the best
understanding of the behavior of economics and biology.
Also, we could maybe understand nature like a game in
where its players compete for a common welfare and the
equilibrium of the system that they are members.

The relationships between game theory and quantum
mechanics let us propose certain quantization relationships through which we could describe and understand
not only classical and evolutionary systems but also the
biological systems that were described before through the
replicator dynamics. Quantum mechanics could be used

We could say that the purpose and maximum payoff of
a system is its maximum entropy state. The system and
its members will vary and rearrange themselves to reach
the best possible state for each of them which is also the
best possible state for the whole system. This can be
seen like a microscopical cooperation between quantum
objects to improve their states with the purpose of reaching or maintaining the equilibrium of the system. All the
members of our system will play a game in which its
maximum payoff is the equilibrium of the system. The
members of the system act as a whole besides individuals
like they obey a rule in where they prefer to work for the
welfare of the collective besides the individual welfare.

[1] J. von Neumann and O. Morgenstern,The Theory of
Games and Economic Behavior (Princeton University
Press, Princeton, 1947).
[2] R. B. Myerson, Game Theory: An Analysis of Conflict
(MIT Press, Cambridge, 1991).
[3] M. A. Nowak and K. Sigmund, Nature 398, 367 (1999).
[4] J. M. Smith, Evolution and The Theory of Games (Cambridge University Press, Cambridge, UK, 1982).
[5] J. Hofbauer and K. Sigmund, Evolutionary Games and
Replicator Dynamics (Cambridge University Press, Cambridge, UK, 1998).
[6] J. Weibul, Evolutionary Game Theory (MIT Press, Cambridge, MA, 1995).
[7] R. A. Fisher, The Genetic Theory of Natural Selection

(Oxford, Clarendon Press, 1930).
[8] P. Hammerstein and R. Selten, Game Theory and Evolutionary Biology (Handbook of Game Theory. Vol 2. Elsevier B.V., 1994).
[9] R. Cressman, The Stability Concept of Evolutionary
Game Theory: A Dynamic Approach (Springer-Verlag,
New York, 1992).
[10] P. D. Taylor and L. B. Jonker , Evolutionary stable strategies and game dynamics, Mathematical Biosciences 40,
145-156 (1978).
[11] J. M. Smith and G. R. Price, The logic of animal conflict,
Nature 246, 15 (1973).
[12] E. Guevara H., Quantum Replicator Dynamics, Physica
A 369/2, 393-407 (2006).

IX.

CONCLUSIONS

9
[13] E. Guevara H., The Why of the applicability of Statistical
Physics to Economics, physics/0609088.
[14] E. Guevara H., Introduction to the study of entropy in
Quantum Games, quant-ph/0604170.
[15] E. Guevara H., Quantum Games Entropy, Physica A (to
be published), quant-ph/0606045.
[16] J. von Neumann, Thermodynamik quantummechanischer
Gesamheiten, Gött. Nach. 1 273-291(1927).
[17] J. von Neumann, Mathematische Grundlagen der Quantenmechanik (Springer, Berlin, 1932).
[18] B. Schumacher and M. D. Westmoreland, Phys. Rev. A
56, 131 (1997).
[19] A. S. Holevo, IEEE Trans. Inf. Theory 44, 269 (1998).
[20] B. Schumacher, Phys. Rev. A 51, 2738 (1995).
[21] R. Jozsa and B. Schumacher, J. Mod. Opt. 41, 2343
(1994).
[22] C. H. Bennett and D. P. DiVincenzo, Nature 377, 389
(1995).
[23] D. P. DiVincenzo, Science 270, 255 (1995).
[24] C. H. Bennett and S. J. Wiesner, Phys. Rev. Lett. 69,
2881 (1992).
[25] C. H. Bennett et al., Phys. Rev. Lett. 70, 1895 (1993).
[26] A. Ekert, Nature 358, 14 (1992).
[27] C. H. Bennett, G. Brassard, and N. D. Mermin, Phys.
Rev. Lett. 68, 557 (1992).
[28] T. M. Cover and J. A. Thomas, Elements of Information
Theory (Wiley, New York, 1991).
[29] M. A. Nielsen and I. L. Chuang, Quantum Computation
and Quantum Information (Cambridge University Press,
Cambridge, 2000).
[30] M. Baranger, V. Latora and A. Rapisarda, Time evolution of thermodynamic entropy for conservative and dissipative chaotic maps, cond-mat/0007302.
[31] L.Ya. Kobelev, O.L. Kobeleva, Ya.L. Kobelev, Is it Possible to Describe Economical Phenomena by Methods of
Statistical Physics of Open Systems?, physics/0005010.
[32] I. Antoniou, V.V. Ivanov, Yu.L. Korolev, A.V. Kryanev,
V.V. Matokhin, Z. Suchanecki, Physica A 304, 525-534
(2002).
[33] H. Eugene Stanley, Exotic statistical physics: Applications to biology, medicine, and economics, Physica A
285, 1-17 (2000).
[34] A. Drăgulescu and V. M. Yakovenko, Statistical mechanics of money, Eur. Phys. J. B 17, 723-729 (2000).
[35] A. Darooneh, Entropy 8[1], 18-24 (2006).
[36] F. TopsØe, Information Theoretical Optimization Techniques, Kybernetika 15, 8-27 (1979). F. TopsØe, Game
theoretical equilibrium, maximum entropy and minimum
information discrimination, in Maximum Entropy and

Bayesian Methods (A. Mohammad-Djafari and G. Demoments (eds.), pp. 15-23, Kluwer, Dordrecht, 1993).
[37] D. A. Meyer, Phys. Rev. Lett. 82, 1052-1055 (1999).
[38] J. Eisert, M. Wilkens and M. Lewenstein, Phys. Rev.
Lett. 83, 3077 (1999).
[39] L. Marinatto and T. Weber, Phys. Lett. A 272, 291
(2000).
[40] A. P. Flitney and D. Abbott, Proc. R. Soc. (London) A
459, 2463-74 (2003).
[41] E. W. Piotrowski and J. Sladkowski, Int. J. Theor. Phys.
42, 1089 (2003).
[42] Azhar Iqbal, PhD thesis, Quaid-i-Azam University, 2004,
quant-ph/0503176.
[43] R. Dawkins, The Selfish Gene (Oxford University Press,
Oxford, 1976).
[44] R. Axelrod, The Evolution of Cooperation (Basic Books,
New York, 1984).
[45] V. Gogonea and K. M. Merz, Fully quantum mechanical description of proteins in solution – combining linear scaling quantum mechanical methodologies with the
Poisson-Boltzmann equation, J. Phys. Chem. A 103,
5171-5188 (1999).
[46] V. Gafiychuk and A. Prykarpatsky, J. Nonlin. Math
Phys. 11, 350 (2004).
[47] R. D. Knight, S.J. Freeland, and L.F. Landweber,
Rewiring the keyboard: evolvability of genetic code, Nature Reviews Genetics 2, 49, (2001).
[48] D. Aerts and M.Czachor, Abstract DNA-type systems,
q-bio.PE/0411031.
[49] A. Patel, Quantum algorithms and the genetic code, Pramana 56, 367-381, (2001).
[50] A. Patel, Testing Quantum Dynamics in Genetic Information Processing, Journal of Genetics 80, 39, (2001).
[51] P. E. Turner and L. Chao, Prisoner’s dilemma in an RNA
virus, Nature 398, 6726 (1999).
[52] P. W. Glimcher, Decisions, Decisions, Decisions: Choosing a Biological Science of Choice, Neuron 36, 323
(2002).
[53] P. W. Glimcher, Decisions, Uncertainty, and the Brain:
The Science of Neuroeconomics (MIT Press, Cambridge
2003).
[54] E. W. Piotrowski and J. Sladkowski, The next stage:
quantum game theory, quant-ph/0308027.
[55] E. W. Piotrowski and J. Sladkowski, Quantum
computer: an appliance for playing market games,
quant-ph/0305017.
[56] G. Collum, Systems of logical systems: Neuroscience and
quantum logic, Foundations of Science 7, 49 (2002).

