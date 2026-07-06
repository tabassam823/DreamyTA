PAPER • OPEN ACCESS

You may also like

Analogies between phase transitions in potential
games and quantum phase transitions

- Permeability heterogeneity and bulk linear
elasticity of displaced clay suspensions
determine interfacial pattern morphologies
in Hele–Shaw experiments
Vaibhav Raj Singh Parmar and Ranjini
Bandyopadhyay

To cite this article: Archan Mukhopadhyay et al 2025 New J. Phys. 27 123901

- Towards Markov-state holography
Xizhu Zhao, Dmitrii E Makarov and Aljaž
Godec

View the article online for updates and enhancements.

- High-harmonic spectroscopy of mobility
edges in one-dimensional quasicrystals
H K Avetissian, B R Avchyan, A Brown et
al.

This content was downloaded from IP address 103.159.199.165 on 20/01/2026 at 09:51

New J. Phys. 27 (2025) 123901

https://doi.org/10.1088/1367-2630/ae2356

PAPER

OPEN ACCESS

Analogies between phase transitions in potential games and
quantum phase transitions

RECEIVED

31 July 2025
REVISED

16 November 2025
ACCEPTED FOR PUBLICATION

24 November 2025
PUBLISHED

11 December 2025

Original Content from
this work may be used
under the terms of the
Creative Commons
Attribution 4.0 licence.
Any further distribution
of this work must
maintain attribution to
the author(s) and the title
of the work, journal
citation and DOI.

Archan Mukhopadhyay1,5, Tanay Saha2,5, Saikat Sur3,5,∗ and Sagar Chakraborty4
1

Department of Physics, M. S. Ramaiah University of Applied Sciences, Bengaluru 560058, India
Department of Mathematics, Simon Fraser University, Burnaby BC V5A 1S6, Canada
3
Optics & Quantum Information Group, The Institute of Mathematical Sciences, HBNI, CIT Campus, Taramani, Chennai 600113,
India
4
Department of Physics, Indian Institute of Technology Kanpur, Kanpur, Uttar Pradesh 208016, India
5
Contributed equally.
∗
Author to whom any correspondence should be addressed.
2

E-mail: archanmukhopadhyay.pi.ns@msruas.ac.in, tanay_saha@sfu.ca, saikats@imsc.res.in and sagarc@iitk.ac.in
Keywords: game theory, quantum games, statistical mechanics

Abstract
Potential games at population level has a very natural analogy with statistical mechanical systems.
Here we show that there are clear analogies between quantum phase transitions at zero temperature and phase transitions in potential games being played by fully rational players. Such phase
transitions are brought about by tuning parameters which change the payoff matrix either directly (as in classical games) or indirectly through continuous change in strategies (as in quantum
games). The phase transitions take the system from one Nash equilibrium to another; these Nash
equilibria (NE) are, in a sense, refined as only the ones that correspond to global maxima of the
potential are selected in the thermodynamic limit (infinite number of players). We observe that the
types of the phase transitions depend on the states involved in the transition process: while transitions involving two symmetric NE are discontinuous, the transitions between a symmetric and an
antisymmetric NE are continuous.

1. Introduction
The famous exclamatory remark (in German) of von Neumann to Morgenstern [1]—the two pioneers of
game theory—‘Ja hat denn das niemand gesehen?’ (Google’s English translation: ‘Yes, did not anyone see
that?’) is a lingering testimony of fascinating hidden analogies between thermodynamics and game theory; after all, the thermodynamical concepts of heat and temperature laid the foundations of axiomatic
treatment [2] of utility and rationality, and thence, the game theory.
Such analogies have only flourished over the years: another important idea—phase transition
(either equilibrium or non-equilibrium)—in thermodynamics and statistical mechanics has been wellexplored [3–9] in both classical and evolutionary games. It is not surprising that various collective configurations of a population of players playing games would show up as parameters of the strategic interaction between players change. For example, noise is realistically present in every real system—while
temperature characterizes it in thermodynamic system, intensity of rationality does so in game theoretic
system; the less rational a player, the more seemingly random choice of strategy is by the player. Thus,
as varying temperature leads to some common phase transitions (like liquid to gas and paramagnet to
ferromagnet) in nature, varying intensity of rationality may lead to a phase where the entire population
collectively plays a Nash equilibrium (NE) strategy—a strategy that when deviated from unilaterally does
not fetch any benefit to the deviating player.
This paper looks to add a new chapter to such analogies. A highly fertile field of research in physics is that of quantum phase transition [10–16], theoretically realized at zero temperature. Naturally,
one should look for an analogy of such phase transitions in the context of games in the limit of fully
rational (‘zero-temperature’) players. To this end, it is pragmatic to follow the mathematical scheme used
© 2025 The Author(s). Published by IOP Publishing Ltd on behalf of the Institute of Physics and Deutsche Physikalische Gesellschaft

New J. Phys. 27 (2025) 123901

A Mukhopadhyay et al

in physics: the language of Hamiltonian and partition function. This is best realized in potential games,
where a single global function captures the incentives of all players-much like a conservative potential in
physics-making them particularly amenable to tools from statistical mechanics.
The concept of potential games originated with the seminal work of Monderer and Shapley [17].
They demonstrated that multi-agent interactions can be characterized by a single potential function
that encapsulates the collective incentives of all players. In such games, when any player does unilateral
strategy-change improving their individual payoff, it results in an equivalent corresponding change in the
potential function, thereby linking individual rationality with the global dynamics of the system. This
property makes potential games particularly useful across economics, computer science, and engineering, where systems of self-interested agents tend to converge naturally to stable equilibria (Nash equilibria (NE)) without requiring centralized coordination [18–21]. In contrast, the literature on quantum
potential games remains at a very nascent stage compared to that of classical potential games or general
quantum games. A limited number of studies in quantum game theory have highlighted the applicability of these hybrid frameworks for distributed decision-making in engineered and quantum-enabled
systems [22, 23]. Thus, needless to say, quantum potential games may represent a promising intersection of classical game-theoretic structures and quantum strategy spaces, offering new modeling tools for
analyzing equilibrium behavior in emerging quantum technologies.
The paper is organized as follows: in section 2, we introduce the Hamiltonian and the partition function formalism of potential games. Section 3 analyzes the corresponding phase transition behavior. In
section 4, we extend the framework to quantum potential games and examine their phase transition
characteristics, while section 5 discusses possible indicators of quantum-like phase transitions. Finally,
section 6 presents the overall discussion and conclusions.

2. Hamiltonian formalism of potential games
In the context of one-shot two-player bimatrix game, a potential game [17, 24–26] is the one where a
unique (up to an additive constant) global potential V matrix exists such that
Vkj − Vij = ПAkj − ПAij ,
Vil − Vij = ПBil − ПBij ;

(1)

where ПA and ПB are the payoff matrices of player A and player B, respectively. The subscripts in the
equation above refer to the elements of the corresponding matrix: e.g. ПAkj is the payoff of player A when
she plays action sk (out of, say, nA possible actions available in her strategy set SA ) against action sj
(out of, say, nB possible actions available to her in her strategy set SB ). Ergo, i, k ∈ {1, 2, · · · , nA } and
j, l ∈ {1, 2, · · · , nB }. Thus notationally, Vil = V(si , sl ). In the paper, we shall stick with SA = SB = S =⇒
nA = nB = n. Such a potential approach simplifies the analysis of the equilibrium: the strategy profile
for which Vij achieves its maximum (with respect to single player deviations) is a preferred rational
outcome—an NE; if the maximum is global then the corresponding NE strategy profile may aptly be
called the most probable one—justification of this terminology may be sought in the methodology of statistical mechanics elaborated below. Interestingly, for 2 × 2 games, the global maximum corresponds to
the risk-dominant NE [27–29].
Interestingly, the long-established correspondence [3, 8] between the potential in a game-theoretic
problem and the Hamiltonian in a many-body system permits us to construct a common viewpoint to
observe the ground state or equilibrium property of a system and its variation with system parameters.
Allowing Greek superscripts to tag locations (nodes) of agents on a graph, the Hamiltonian of a manyagent interaction may simply be defined as
H=

X

V (sµ , sν ) Gµν ,

sµ , sν ∈ S;

(2)

⟨µν⟩

where adjacency matrix, Gµν = 1 if the agents/players, indexed by µ and ν, interact; otherwise, Gµν = 0.
The notation ⟨µν⟩ mean that µ and ν interact. Viewing the system as a statistical mechanical one, when
the system size is large, at equilibrium, one may also define a partition function [30, 31]:
Z (K) =

sn X
sn
X
s1 =s1 s2 =s1

2

···

sn
X
sN =s1

 
H
.
exp
K

(3)

New J. Phys. 27 (2025) 123901

A Mukhopadhyay et al

This parameter K— a measure of deviation from full rationality [8, 27]—can be understood as an
analogy of the temperature of a thermodynamic system. We note that while writing the partition function, we take Gµν = 1 ∀µ, ∀ν ̸= µ, to envisage an equilibrium canonical ensemble corresponding to a
population (of a large size N) where
 every player interacts with every other player through a binary
interactions—there are always N2 pairwise interactions. Effectively, we consider N2 pairwise interactions among N individuals, where each interaction is modeled as a two-player, n-strategy game. As evident from equation (3), the number of players N does not explicitly enter the payoff matrix, although it
implicitly affects the partition function via the multiplicity of microstates. One may consider every possible assignment of strategies to players as a probable microstate of the ensemble. One may note that
the form of our derived partition function aligns with the Gibbs distribution in the equilibrium state,
provided we assume the Glauber dynamics (smoothened best response or Logit, in the game theory parlance) as the microscopic update rule for the macroscopic system [3].
In passing, we remark that while the conventional formulation of the partition function includes a
negative sign in the argument of exponential (that is, −H/K), adopting a positive sign (see equation (3))
leaves the underlying physics unchanged and can be interpreted as corresponding to a negative temperature or negative potential energy. This convention reflects our system’s evolution toward a state of maximum potential (or payoff), consistent with the maximization framework of evolutionary game theory
and in agreement with earlier studies [32–34].

3. Phase transitions
Due to the presence of the exponential function, all nN summands in the partition function will contribute to the sum when noise K is non-zero; in the limit of zero noise or K → 0, the system can only be
found at the highest potential. Thus, any shift from the microstate corresponding to the argmax set of
the potential is qualitatively equivalent to a phase transition in the system. As the potential is uniquely
mapped to the payoff (see equation (1)), the collective payoff of the system can be treated as an order
parameter for such phase transitions. The quantitative effect of such phase transitions will be reflected
either in the discontinuous change of the internal energy or its derivative at the critical point. The equivalent of the internal energy of the system are given as
⟨E⟩ = −K2

∂
ln Z (K) .
∂K

(4)

The following two subsections analyze the case of two-player two-strategy symmetric game. Such
games are known to be potential games. The payoff elements and potential matrix are described in
equations (7) and (8).
3.1. Ferromagnetic-to-ferromagnetic phase transition
Example of a phase would be where every individual plays the same strategy (symmetric equilibrium) in
the zero noise limit; it is analogous to the ferromagnetic phase in magnetic systems. In figure 1 we depict
these phases, respectively phase I and III, corresponding to two possible maximum potential elements,
VCC and VDD respectively. Without any loss of generality, let Vmm and Vm′ m ′ ′ (where (m ′ , m ′ ′ ) ̸= (m, m))
be the largest and the second largest elements, respectively, in the potential matrix. The population state
corresponding to the second highest energy configuration is always the case where (N − 1) players play
the strategy m and only one plays m′ (see appendix A). In the limit of small noise (almost rational players), the partition function in equation (3) turns out to be
1 N
1
1 N−1
Z (K) = e K ( 2 )Vmm + Ne K (N−1)Vmm′ e K ( 2 )Vmm + · · ·
h
i
N 1
N−1
= e( 2 ) K Vmm 1 + Ne− K ∆ + · · · ,

(5)

where, ∆ ≡ Vmm − Vmm′ is the energy gap between the top two most probable states and we assume that
∆ > 0 (non-degenerate eigenstates). Therefore, using equation (4)
 
N
N (N − 1) ∆
,
⟨E⟩ =
(6)
Vmm − (N−1)∆
2
e K +N
in the limit K → 0.
A phase transition due to tuning of parameters, other than the temperature-like K, while the system
stays in a symmetric equilibrium is most simply comprehended in the context of two-player two-strategy
3

New J. Phys. 27 (2025) 123901

A Mukhopadhyay et al

Figure 1. A schematic presentation of twelve ordinal game classes demarcated by the lines: S = 0, T = 0, S = 1, T = 1, and S = T.
On the basis of the strategies, corresponding to the highest potential element, there can be three distinct classes: the green region
(region (I) with the strategy profile (C, C), the red region (region II) with the strategy profiles (C, D) and (D, C), and cyan region
(region III) with the strategy profile (D, D) correspond to the highest potential (see [35] for detailed description of the game
classes).

symmetric games which are always potential games [17]. A 2 × 2 payoff bimatrix is commonly represented in the following form:

C
D

C

D

(R, R)
(T, S)

(S, T)
.
(P, P)

(7)

Here, the payoff elements R, S, T, and P, are popularly known as the Reward, Sucker’s payoff, Temptation, and Punishment, respectively [36]; and the actions/strategies C and D are termed
Cooperation and Defection, respectively. Therefore, R and P correspond to the payoffs for mutual
cooperation and mutual defection, respectively. Without any loss of generality, to make our analysis
tractable, we set R = 1 and P = 0—which amounts to performing a positive affine transformation on the
payoff elements [35]—for the classical games. The resulting payoff bimatrix corresponds to the following
potential matrix:



0
T−1
V=
.
T−1 T−S−1

(8)

Owing to the existence of a common Z2 symmetry, the corresponding partition function [31, 37,
38] is shown to be analogous to that of a long-ranged classical Ising model with N spins in a transverse magnetic field: the interaction strength J and the magnetic field strength h in the Ising model is
analogous to the payoff dependent functions (1 − S − T)/4 and (T − S − 1)/2, respectively, in the gametheoretic setup [3].
Even at zero noise, a ferromagnetic-to-ferromagnetic phase transition is clearly evident when the
potential maximum shifts between symmetric strategy profiles, such as moving from (D, D) to (C, C) or
vice-versa. A comparison of the four elements of the potential matrix reveals (D, D) is the most probable
NE when T ⩽ 1 and S > T − 1; and (C, C) is the most probable NE when T ⩽ 1 and S < T − 1. Thus,
as per figure 1, the phase transition is possible when parameters change to take one from cyan region
to green region across the line S = T − 1. In terms of the games, such transitions are possible either
4

New J. Phys. 27 (2025) 123901

A Mukhopadhyay et al

between a Prisoner’s Dilemma (PD) game and a Harmony game or between two appropriate coordination games.
A transition parameter for this case can be defined as λ ≡ V(D, D) − V(C, C) = T − S − 1. We note
that such transition parameters are defined so that the zero value of λ serves as a boundary between two
game classes (see figure 1), each characterized by a distinct set of NE. In the limit of zero noise and in
the thermodynamic limit, the energies of the system in these two ferromagnetic phases can be shown to
be of the following form:
⟨E⟩I = 0,
⟨E⟩III =

(9a)
2

N
(T − S − 1) .
2

(9b)

One may note that the energies of these two phases are continuous on the phase boundaries.
However, the same is not true for the first derivative of the energies:
δ

∂⟨E⟩I
∂⟨E⟩III
N2
∂⟨E⟩
≡
−
=
,
∂λ
∂λ λ=0+
∂λ λ=0−
2

(10)

showing a discontinuous jump in the derivative of average energy across the phase transition. It points
towards a very interesting result: ferromagnetic-to-ferromagnetic transitions are discontinuous transitions. For clarity, we have elaborated on test examples of this type of transition in appendix B.
3.2. Antiferromagnetic-to-ferromagnetic transition
A completely different kind of phase appears when there is a transition from the PD, Harmony Game
or coordination game to the anti-coordination game (S > 0 and T > 1), characterized by coexistence
of asymmetric NE and mixed NE. As per figure 1, we are talking about the transition between cyan or
green region and red region. This phase (in red region) reminds one of the antiferromagnetic phase (all
spins are not aligned in the same direction): the full population cannot play the same strategy in the
zero noise limit owing to the restrictions imposed by the Hamiltonian. Here, the maximum potential
element Vmm′ is asymmetric in the strategy, i.e. m ̸= m ′ . If α and (N − α) are the numbers of agents
with strategy sm and sm′ , respectively, then with
1
1
Vtot (α) = α (α − 1) Vmm + α (N − α) Vmm′ + (N − α) (N − α − 1) Vm′ m ′ ,
2
2
denoting the total energy of the system, the partition function of equation (3) becomes
h
i
Vtot (α)
Vtot (α±1)−Vtot (α)
K
Z (K) = e K
1+e
,

(11)

(12)

˜ = Vtot (α) − Vtot (α ± 1). Thus, for small noise, in this
for infinitesimal noise, up to first order in ∆
phase,
⟨E⟩ = Vtot (α) −

˜
∆
˜
∆

.

(13)

1+e K

An asymmetric strategy profile corresponding to the maximum potential matrix element means that
the potential is maximized in each binary interaction given the involved players play different strategies.
In a population as considered in our case, where the agents interact with each other in an unstructured geometry, the equilibrium state of the population has to be interpreted as a geometrically frustrated state [39–41]: many macroscopically equivalent degenerate microstates are possible. To give an
example, let us consider a population of three player interacting with each other through 2 × 2 anticoordination game; each pair of players should have opposite strategies to maximize the potential. But
the obvious indeterminacy of strategy of the third player—who is supposed to interact with both the
players simultaneously—gives rise to six-fold degenerate population states. The specific microstate realized at equilibrium starting from a non-equilibrium state depends on the underlying protocol of the
strategy-update-rule.
A caveat is worth pointing out: understanding the asymmetric NE at the population level in anticoordination games requires considering two populations with interspecific interactions. However, the
statistical mechanical setup we are interested in in this paper allows only for a single-population interpretation of the asymmetric NE. Therefore, it not surprising that in any game featuring asymmetric
potential maxima, particularly in set-ups involving more than two players, statistical mechanics tends
5

New J. Phys. 27 (2025) 123901

A Mukhopadhyay et al

Figure 2. Change in cooperator-fraction (xC ) during antiferromagnetic-to-ferromagnetic transition: subfigure (a) depicts the
transition from region I to region II whereas subfigure (b) depicts the same for region II to region III. Cyan, blue and black
curves, respectively, correspond to N = 5, N = 10, and N = 100 sizes of the population.

to favor a polymorphic population that somewhat aligns with the concept of mixed Nash Equilibrium
state, even if this does not directly correspond to the potential maxima present in a two-player scenario.
We remark that a polymorphic population means coexistence of individuals using different strategies
that persist stably over time. It is the population-level analogue of a mixed phase in physics—a dynamic
equilibrium between competing ‘species’ or ‘states’ (strategies). Such an equilibrium, corresponding to
maximization of Vtot (corresponding to the anti-coordination game; see equation (11)) with respect to x
(where x ≡ α/N be the fraction of agents playing sm ), is given by
x=

1
S + 2N
(T − S − 1)
.
S+T−1

(14)

Obviously, in the limit of infinite population, x = S/(S + T − 1), which interestingly, is the mixed
(symmetric) NE of the anti-coordination game [42]. This limit is understood as follows. Note first that
the mixed NE is obtained under maximization of Vtot , irrespective of population size, if we take selfinteraction into account, i.e. every player can also engage with itself—this technically means to replace
‘−1’ in equation (11) by ‘0’. Therefore, in the thermodynamic limit, i.e. large N, the contribution from
self-interaction becomes relatively negligible, allowing for the standard classical game theory outcome.
In the limit of zero noise and in the thermodynamic limit, the energy of the system in the antiferromagnetic phase is given by
2

⟨E⟩II =

N2 (T − 1)
.
2 (T + S − 1)

(15)

One can note that the energy of this phase is continuous on the phase boundaries with the other
two ferromagnetic phases. Interestingly, the same is true for the first derivative of the energies (see
appendix A):
∂⟨E⟩I
∂⟨E⟩II
−
= 0,
+
∂λ λ=0
∂λ λ=0−
∂⟨E⟩II
∂⟨E⟩III
−
= 0.
+
∂λ λ=0
∂λ λ=0−

(16)

Thus, we can see that both the antiferromagnetic-to-ferromagnetic phase transitions are continuous
transitions. We also note that in line with equation (14), the aforementioned phase transitions would
involve continuous change in cooperator-fraction which should depend on population size as well (see
figure 2).
We present the summary of both the ferromagnetic-to-ferromagnetic and antiferromagnetic-toferromagnetic phase transitions in 2 × 2 games in table 1 and also illustrate them on K–λ space in
figure 3 to highlight their striking visual resemblance with the quantum phase transitions found in true
quantum systems.
6

New J. Phys. 27 (2025) 123901

A Mukhopadhyay et al

Table 1. Characteristics of quantum-like phase transitions in 2 × 2 classical games. (The fidelity-like measure, f(λ), is described later in
section 5).

Phases involved

Shift in NE states

Transition parameter (λ)

δ |∂⟨E⟩/∂λ|

f(λ = 0)

Type of transition

Phase I and phase III
Phase II and phase III
Phase I and phase II

All C to all D
Mixed state to all D
All C to mixed state

T−S−1
S
T −1

N2
2

0
1
1 − 2N
1
1 − 2N

Discontinuous
Continuous
Continuous

0
0

Figure 3. Illustrating quantum-like phase transitions in 2 × 2 classical games: the density plots depict the first derivative of energy
with respect to the transition parameter on parameter space of noise strength (K) and transition parameter (λ). We have considered an all-to-all connected network of five players. (a), (b), and (c) depict transitions from region I to region II, region II to
region III, and region I to region III, respectively. The resemblance of these plots with quantum phase transition plots (see figure
1.2(b) in textbook [10] ) is intriguing.

4. Quantum potential games: phase transitions
We note that in a classical game to achieve the afore-discussed phase transitions, we had to tune the
payoff elements leading to change in the ordinal class of the games at the phase transitions. A somewhat different scenario is when one of the players has access to a continuous strategy set and is capable
of changing their strategy continuously to bring about phase transitions. One such kind of game with
continuous strategy space is a quantum game [43–48].
The extension of the one-shot game into the quantum domain may be done using many existing
protocols [43, 45, 49–52]. In our paper, we follow the Eisert–Wilkens–Lewenstein (EWL) protocol [45]
that maps the classical strategies into a continuum set of quantum strategies available to the players. This
extension helps us to arrive at the outcomes of the classical strategies C and D through manipulations
of Hilbert state vectors |0⟩ and |1⟩ respectively. Generally, the state of the quantum game is defined as
|ψ⟩ ≡ J(ε)|ab⟩ = J(ε)|a⟩A ⊗ |b⟩B where a, b ∈ {0, 1} and the unitary entangling operator
ε √
ε
J (ε) ≡ 1A ⊗ 1B cos + −1 DA ⊗ DB sin .
(17)
2
2
(A and B tags to the two players, Alice and Bob, respectively.) Here, ε stands for the parameter characterizing the entanglement between the qubits, 1 is the identity operator and D is the standard qubit
flip Y gate with a phase. The action of D on the states |0⟩ and |1⟩ takes it to its orthogonal counterpart −|1⟩ and |0⟩ respectively. The two-qubit entangling operator J(ε) acts on the joint Hilbert space
HA ⊗ HB . While operating it forms an entangled two-qubit state from the pure states |0⟩A and |0⟩B . The
entanglement parameter, ε ∈ [0, π/2], quantifies the entanglement of the initial states of the players.
Any quantum strategy is represented as a unitary operator belonging to a SU(2) group rotation and
is of the following form [53]


γ
U=
−δ ∗

δ
γ∗


(18)

with |γ|2 + |δ|2 = 1; the elements are complex numbers and the asterisk denotes the complex conjugate. From now on, we will use the superscript A or B depending on whether Alice or Bob has played
the strategy. In general, the initial game state is chosen as |ψinitial ⟩ ≡ J(ε)|00⟩. The simultaneous strategic
action by Alice and Bob leads to a new final state |ψfinal ⟩ = J† (ε)(UA ⊗ UB )J(ε)|00⟩. The payoff is given by
P P
$A ≡ a b Πab |⟨ab|ψfinal ⟩|2 which basically weight the payoffs with the likeliness of the basis states. The
extension from classical game to quantum game is justified as the following mapping holds: U as 1 and
7

New J. Phys. 27 (2025) 123901

A Mukhopadhyay et al

Figure 4. The actions of three quantum strategies Cooperation (C), Defection (D), Hadamard (H), and a generic strategy U(θ, ϕ)
on the state |0⟩ are depicted schematically on the Bloch sphere. All quantum strategies are 2 × 2 unitaries on the SU(2) Hilbert
space and their actions on a pure state are represented by rotations on the surface of the Bloch sphere.

D—respectively representing cooperation and defection actions—the payoff is identical to that of a classical game, as expected. To make the study analytically tractable we focus on the standard two-parameter
subspace of SU(2) where δ = δ ∗ = sin θ2 and γ = eiϕ cos θ2 ; θ ∈ [0, π] and ϕ ∈ [0, π/2].
There is no guarantee that the potential structure exists for all quantum games; not much work is
reported in the literature (cf in the context of evolutionary game dynamics [27, 54–57]). We restrict
our attention to potential games because they enable the application of statistical mechanical prescriptions within the framework of game theory. The general condition for potentiality in quantum games
is discussed in detail in appendix C (refer equation (C2)). We find (see appendix C) that one needs at
least two quantum strategies along with a classical one to get a non-trivial quantum potential game. We
prefer to choose the Hadamard gate H as it is one of the most well known quantum strategies studied
in the literature [58]. To this end, let us choose Cooperation (C); the well-known Hadamard strategy,
H ≡ (θ = π2 , ϕ = 0); and another quantum strategy, U whose θ and ϕ are such that we get a potential
game structure (refer appendix C):
sin ε =

tan θ/2
,
sin ϕ

∀ sin ε ̸= 0.

(19)

The solution to the above equation forms a continuous line effectively parametrized by a single
parameter belonging to SU(2) subspace. From the form of the above transcendental equation and the
allowed ranges of the trigonometric functions, it follows that the condition of potentiality imposes a
restriction on θ. Consequently, the maximum allowed range of θ is [0, π/2], which corresponds to the
case of maximal entanglement with ε = π/2. For non-maximal entanglement, the upper bound of θ
becomes strictly less than π/2. These strategies are pictorially shown in figure (4). The resulting 3 × 3
game, corresponding to the underlying classical game as defined in equation (7), possesses a potential
matrix V whose elements are given by:
T−R
1
, V22 = (P − 3R − S + 3T) ,
2  
4
 
θ
T−R
2
2 θ
V13 = V31 = (P − 2R + T) sin
, V23 = V32 =
+ (2P − R − S) sin
,
2
2
2



1
θ
V33 =
−2R − S + T + (S − T) cos θ + 2 cos4 R cos2 η + R cos2 ε + P sin2 ε sin2 η
2
2


η
2θ
+ sin
(P + S + T) + (−P + S + T) cos θ + 2 (2P − S − T) sin θ cos
,
2
2



θ
where η ≡ 2 sin−1 csc ε tan
.
2
V11 = 0,

V12 = V21 =

8

(20)

New J. Phys. 27 (2025) 123901

A Mukhopadhyay et al

Figure 5. The variation of potential matrix elements with the driving parameter for our quantum modified PD game with
R = 6, S = 1, T = 7, and P = 5. The black dashed line corresponds to the critical point, θc = 0.4467π.

Figure 6. This figure exhibits the fractions of players corresponding to strategies C, H, and U(θ) for a quantum modified potential
game. The underlying game is a quantum PD game with R = 6, S = 1, T = 7, and P = 5. Subplots (a), (b), and (c) correspond to
all-to-all network with five (N = 5), ten (N = 10), and hundred (N = 100) players respectively.

One can see that V 33 among the diagonal elements, and V 13 & V 23 among the off-diagonal elements
are functions of θ. Obviously, the necessary condition for C to be NE is V11 > V12 and V11 > V13 , i.e.
R > T and 2R > T + P,

(21)

respectively. It implies that C is never a NE if the underlying game is PD, where T > R > P > S.
Similarly, for H to be most probable NE, the potential element V 22 must be maximum. There exists
an upper bound of θ (say, θc ), beyond which V 23 exceeds V 22 . The expression for the upper bound of θ
follows from the condition V23 = V22 :
s
θc = 2 arcsin

P+T−R−S
.
4 (2P − R − S)

(22)

For a typical set of payoff elements R = 6, S = 1, T = 7, and P = 5, the critical value is θc ≈ 0.4467π.
For this case, the variation of potential matrix elements as a function of the transition parameter and for
maximal entanglement has been shown in figure 5. Henceforth, we consider the entanglement operator
to be a perfect entangler (ε = π/2) for all the cases discussed in this paper.
For the regime below the critical point, the state of the system at zero temperature consists solely
of players utilizing the strategy H. However, in the regime above the critical point, the population may
exhibit a mixture of the three strategies: C, H, and U. This regime corresponds to the antiferromagnetic
phase within the context of quantum potential games.
The maximum energy and the corresponding state of the population are determined by maximizing the total energy over all possible states. We present the state corresponding to the maximum energy
in figure 6 for a PD game. It can be noted that this state only corresponds to a fraction of H and U for
9

New J. Phys. 27 (2025) 123901

A Mukhopadhyay et al

Figure 7. Illustrating quantum-like phase transitions in quantum PD game: the density plot (subplot (a) depict the first derivative of energy with respect to the transition parameter on parameter space of noise strength (K) and transition parameter (θ).
We have considered an all-to-all connected network of five players and R = 6, S = 1, T = 7, and P = 5. The resemblance of this
plot with quantum phase transition plots (see figure 1.2(b) in textbook [10]) is intriguing. Subplot (b) and (c) depict the first
derivative of energy with respect to the transition parameter as a function of the transition parameter (θ) for K = 0 for N = 5 and
N = 100 players, respectively.

θ > θc . From our numerical calculations, we observe that the strategy fractions (figure 6) tend to become
continuous at the phase boundary as the system size increases.
Letting α to denote the number of players with strategy U at θ = θc+ , the expression for the energy at
θ = θc+ is given by the form:
⟨E⟩

=
+

θ=θc

 


α
N−α
V33 (θc ) +
V22 + α (N − α) V23 (θc ) .
2
2

(23)

On the other hand, the energy at θ = θc− is independent of θ,
⟨E⟩

=
−

θ=θc

 
N
V22 .
2

(24)

Therefore, the difference between the first derivatives of the energies of the two phases at the phase
boundary is given by the following expression:
∂⟨E⟩
∂⟨E⟩
∂⟨E⟩
δ
≡
−
=
∂θ
∂θ θ=θc+
∂θ θ=θc−

 
α ∂V33 (θc )
∂V23 (θc )
+ α (N − α)
.
2
∂θ
∂θ

(25)

Since both the potential elements V 33 and V 23 are smooth functions at the boundary, the discontinuity in the derivative of energy can appear if α is nonzero. Since from figure 6 we observe, as N
increases, the value of α limits to zero at the phase boundary from right, i.e. at θ = θc+ , the value of
the expression in equation (25) tends to zero in the thermodynamic limit. Here, we assume the system
size N to be large but not infinity. From this insight, we can conclude that the derivative of energy (and
hence the energy itself) with respect to θ in the thermodynamic limit are continuous functions at the
phase boundary (see figures 7(b) and (c)). Thereby, it also brings forth a continuous ferromagnetic-toantiferromagnetic phase transition in the context of quantum game.
Before proceeding further, we should point out that the entanglement operator employed herein is
not the most general form. As an illustration, the operator used in [45, 59] differs from ours by a negative sign in the exponential term (see equation (17)). A straightforward calculation with this entanglement operator reveals that the corresponding payoff remains unchanged, apart from a relative phase
factor in the final wavefunction. This implies that the physical results including the potentiality conditions (equation (19) and equation (C5)) are unaffected by this sign difference. More generally, the
entanglement operator can be expressed in terms of a pair of Cartan parameters [60–62], of which the
specific form used in our analysis arises as a special case. The analogues of equations (19) and (20)
can likewise be derived under this generalized framework. However, for the class of ‘perfect entanglers’
(operators that generate maximum entanglement from initially unentangled qubits), as considered in our
study, it can be shown that the final results remain invariant across all equivalent entanglement-operator
formulations, apart from possible differences in the relative phase factors of the final wavefunction.
10

New J. Phys. 27 (2025) 123901

A Mukhopadhyay et al

5. Hint of quantum-like phase transition
The resilience of the maximally probable NE near the zero temperature may be effectively characterized as the ratio of the potential difference (∆) between the top two probable states and the minimum
thermal fluctuation: ∆/K (recall that K is analogous to temperature in energy units). The higher this
ratio the more resilient the rationality is with respect to thermal fluctuations. This gap in potentials
between the top two most probable states is analogous to the energy gap of the lowest excitation above
the ground state in quantum many-body systems [10]. At the phase transition, the system is extremely
sensitive to the thermal fluctuations as this gap closes to zero. Even at an infinitesimal temperature, all
possible strategic interactions are present in any many-body systems.
The theory of quantum many-body systems deals with the nature of phases of interacting quantum
particles in their ground states. To delve into this, two different energy-scales are compared, namely, the
Planck energy, representing the typical energy of the Hamiltonian, and the thermal energy. Consider
a quantum Hamiltonian of a lattice-dependent model and a dimensionless coupling parameter in the
system. For an infinite lattice, this energy of the ground state can no longer behave as a smooth, analytic function of this parameter. This situation occurs when an excited level shifts into the ground state
and vice-versa causing a level-crossing at a specific value of the parameter. The signature of this transition is marked by the non-analyticity in the ground state energy. This kind of transitions are known
as quantum phase transitions. Unlike classical phase transitions, here temperature does not govern the
transition in the system.
The phase transition considered in this article is analogous to the above-mentioned quantum phase
transition. Our system is a all-to-all coupled lattice (note each lattice point represents each individual of
the population). The dimensionless parameter of phase transition depends on the system under study:
for the classical game it is payoff elements whereas for the quantum game it is the strategy parameter. In
line with expectation, we also observed discontinuous shift in internal energy at the critical point.
In the study of quantum phase transitions, researchers utilize a concept known as fidelity, which
serves as an information-theoretic measure to identify the ground state singularities linked to a quantum
phase transition. Fidelity is quantified as the overlap between the ground states of a specific Hamiltonian
evaluated at two different settings of the tuneable parameter (say, λ). Formally, fidelity for two ground
states |ψ0 (λ)⟩ and |ψ0 (λ + δλ)⟩ of a Hamiltonian H(λ) is defined as the overlap of states very close to
each other in the parameter space [63]:
F (λ) = lim |⟨ψ0 (λ) |ψ0 (λ + δλ)⟩|.
δλ→0

(26)

The above quantity is bounded from above by unity (corresponds to the case where the two states
are identical) and from below by zero (corresponds to the case where the two states are orthogonal).
The fidelity, F(λ), vanishes in the limit of the states becoming mutually orthogonal: it is generally the
case close to a quantum critical point [10, 63]. It is observed that the fidelity shows a sharp decay in
proximity to a critical point indicating a signature of phase transition [63–65].
To assess the population surrounding the critical point, in line with our agenda to digging up analogies with quantum phase transitions, we require a comparable metric. Using the transition parameter, λ,
we define a fidelity-like measure for our analysis as follows:
d (λ)
f (λ) = 1 − √ ,
2

(27)

where d(λ) denotes the normalized Euclidean distance between the population states corresponding to
the parameters λ and λ + δλ (δλ → 0). Any discontinuity observed in f(λ) would highlight the critical
point in the game-theoretic population akin to the behavior seen in quantum phase transitions within
many-body systems.
Let (xs1 (λ), xs2 (λ), · · · , xsn (λ)) represent the population state, where the fraction xsi (λ) denotes the
fraction of the population equipped with the strategy si at a given λ. The formula for d(λ) can then be
expressed as follows:
v
u n
uX
2
d (λ) = lim t
[xsi (λ + δλ) − xsi (λ)] .
(28)
δλ→0

i =1

√
The range of d(λ) is [0, 2]. It is worth considering the relevance of fidelity-like measures in gametheoretic contexts. Such measures, originally introduced in quantum and statistical physics to quantify
11

New J. Phys. 27 (2025) 123901

A Mukhopadhyay et al

Figure 8. Quantum-like phase transitions captured by fidelity-like measure. (a) and (b) correspond to the transitions between
phases I and II, and between phases II and III respectively in 2 × 2 classical game (refer equation (7)). (c) corresponds to the
phase transition in quantum PD game (R = 6, S = 1, T = 7, and P = 5; refer section 4). We have taken δλ = 10−7 and δθ =
π/10−6 in the classical and the quantum games, respectively.

the similarity between states under parametric variations, can offer valuable insight into the stability and
sensitivity of equilibria in evolutionary games. From the game-theoretic perspective, d(λ) denotes the
distance in the state space—represented by an (n − 1)-dimensional simplex—between two equilibrium
population states corresponding to infinitesimally close parameter values λ and λ + δλ. By construction,
an increase in this distance implies a decrease in the associated fidelity, and vice versa. In particular, a
fidelity value of unity (f = 1) indicates that the equilibrium (or ground) state remains invariant with
respect to small changes in the control parameter, reflecting local stability of the population configuration. Conversely, a fidelity approaching zero (f → 0) signifies that the two equilibrium states become
orthogonal, i.e. there is a complete reorganization of the population state distribution. This sharp drop
in fidelity can thus serve as a precursor or diagnostic indicator of a qualitative change in the behavior of
the system—analogous to a quantum or thermodynamic phase transition. In this sense, fidelity provides
a unified, geometry-based metric to quantify how sensitively an equilibrium responds to perturbations in
the underlying game parameters, bridging microscopic variations in payoffs with macroscopic structural
changes in the population dynamics.
It is clear that the phase transition between ferromagnetic phases retains a fidelity of 1, except at the
critical point, where the fidelity drops to zero. In contrast, during the transitions between antiferromagnetic and ferromagnetic phases, the fidelity varies continuously across the transition point in the thermodynamic limit. However, for finite populations, there is a discontinuity of 1/(2N) across the phase
boundaries. For more details, please refer to appendix D. For the case of continuous phase transition in
the quantum game, we plot the corresponding fidelity in figure 8(c) which substantiates our claim of the
phase transition.

6. Discussion and conclusions
This paper extends the efforts of interdisciplinary researchers in finding parallels between physics of
phase transitions and transitions in population states due to modifications in parameters of game played
between its individuals: although classical phase transitions already had known analogues in game theory [9, 66–68], curiously, the analogue of the quantum phase transition was missing in the game theory literature. In this paper, we comprehensively filled this lacuna using examples of both classical and
quantum games.
In a typical game theoretic setup, there is a trade off between the potential difference between the
energy levels (a function of the payoff matrix elements) and the noise parameter. If the players are so
rational that the dynamics is solely governed by the potential elements, the quantum-like phase transition occurs. This phenomenon is similar to the case of quantum phase transition where the characteristic energy scale of the thermal fluctuations above the ground state vanishes.
We have presented both continuous and discontinuous phase transitions, and also proposed an
analogue of fidelity measure used in quantum phase transitions in physics problems. One important
observation is that just alteration of NE is not enough for the kind of phase transitions we have discussed in this paper; rather, the statistical mechanical framework requires alteration of most probable
NE—something that can be located using potential matrix formulation—to result in the aforesaid phase
transitions.
12

New J. Phys. 27 (2025) 123901

A Mukhopadhyay et al

While ground-state fidelity has been generally used to detect quantum phase transitions [63], it often
fails to serve as a reliable marker, especially for systems with all-to-all connectivity, like the Lipkin–
Meshkov–Glick model [64, 69]. Generally in these systems, the phase transitions are driven by collective, mean-field-like behavior. As a result, the overlap between ground states does not show a sharp signature near critical points, especially in the thermodynamic limit. Numerical studies also reveal that
fidelity minima are often broad or absent due to finite-size effects, making the critical point difficult to
identify. Although fidelity shows promise in some short-range, a clear and general criterion for when
it acts as a proper signature for a transition is still lacking [65]. In view of these results in literature of
quantum many-body systems, one should also generalize our approach on systems where agents interact on short-ranged graphs to observe a closer similarity to quantum phase transitions in short-ranged
ordered lattices.
In the framework discussed in this paper, it is interesting to realize that entanglement effectively
functions as a shared non-classical correlation that facilitates coordinated strategic decision-making
among agents without the need for explicit communication. This correspondence between quantum
correlations and economic coordination mechanisms underscores the possibility that quantum gametheoretic models may naturally arise in financial and economic systems, particularly in environments
where strategic agents interact under conditions of limited or asymmetric information [70, 71].
The alteration of NE with the variation of game-theoretic parameters is not, by itself, a new observation [72, 73]; however, what is distinctive in our potential-based formulation lies in the physical interpretation it affords: firstly, we embed potential games within the conceptual and mathematical framework of statistical physics, thereby establishing a formal correspondence between microscopic interactions
(individual strategic behaviors) and macroscopic observables (aggregate system states). This mapping
allows us to treat the collective behavior of strategic agents analogously to that of particles in a thermodynamic ensemble, where the system tends toward configurations that maximize a scalar potential
analogous to free energy. Secondly, within this framework, a mere change in the Nash equilibrium does
not automatically imply a phase transition. Instead, a true transition occurs only when the maximumpotential state—the strategic configuration that globally maximizes the potential—undergoes a switch.
This phenomenon directly parallels a ground-state transition in a many-body physical system, where a
qualitative change in the dominant configuration marks a new phase. To further illustrate this correspondence, we explicitly note:
1. the temperature of the physical system maps onto the irrationality or noise parameter in game theory,
quantifying the degree of stochasticity or deviation from perfectly rational behavior in the
population;
2. the average potential of the game corresponds to the average energy (or free energy) of the physical
system, representing the expected payoff at the population level; and
3. a flip in the maximum-potential state mirrors a ground-state transition, signifying a macroscopic
reorganization of the system and, necessarily, a shift in the NE.
This analogy not only clarifies the nature of equilibrium transitions in evolutionary games but also
provides a principled way to classify them using tools and intuitions drawn from statistical mechanics.
The equilibrium population states of the system, as studied herein, can be obtained as the end results of Logit rule [74–76] (equivalent to Glauber dynamics in non-equilibrium statistical mechanics [8,
77, 78]). Thus, an immediate research avenue worth pursuing as an extension of our work is to investigate analogies between dynamical quantum phases [10, 63] and the non-equilibrium states of population
consisting of players playing strategic games. We envisage that such an equivalence would help in novel
characterization of the learning processes of agents though the concepts and measures used for characterizing various aspects of dynamical quantum phase transitions [79–81].
While our formulation and results retain complete generality and applicability for the class of twoplayer–two-strategy games, as the strategy space increases-leading to higher-dimensional games-the situation becomes more restrictive. In such cases, the existence of a potential function is no longer guaranteed. Payoff structure with a well-defined potential naturally becomes a necessary condition for extending our framework to these more complex systems. This distinction bears a close analogy with classical
physics: the dynamics of conservative force fields can be described within the framework of equilibrium
statistical mechanics, where a scalar potential (energy function) fully determines the system’s evolution and stationary states. In contrast, non-conservative or dissipative force fields lack such a potential
representation, and hence, no general statistical-mechanical formulation can be constructed for them.
Similarly, non-potential games do not admit a global potential, making them incompatible with the
equilibrium-based analytical tools employed in our study.
13

New J. Phys. 27 (2025) 123901

A Mukhopadhyay et al

A potential structure is not guaranteed even in quantum games involving more than three strategies.
Even within the framework of a three-strategy quantum game-particularly when two of the strategies
do not possess any classical analog-the system exhibits highly complex and nonlinear behavior. In such
cases, it becomes extremely difficult to predict the overall outcome if one replaces the Hadamard strategy
with any other quantum strategy. This difficulty arises due to the pronounced nonlinearities embedded
in the payoff landscape, which can lead to significant shifts in the phase transition points, alterations in
the corresponding sets of NE, and even changes in the nature of the phase transitions. Consequently,
the analytical characterization of such higher-dimensional or more generalized quantum strategic spaces
remains a formidable challenge. The system may exhibit entirely new regimes depending on the choice
of entanglement parameters and the specific form of the quantum strategies employed. Therefore,
any comprehensive or general statement about these extended scenarios would require a separate and
detailed investigation, which lies beyond the current scope of this work but represents an interesting direction for future research.

Data availability statement
All data that support the findings of this study are included within the article (and any supplementary
files).

Acknowledgments
AM acknowledges the support from Centre for Ecological Sciences, Indian Institute of Science,
Bengaluru, where part of this work was carried out and his stay there was supported by SERB (DST,
Govt. of India) through Project No. PDF/2023/001151. AM is currently employed with M S Ramaiah
University of Applied Sciences. SS acknowledges the support of the Department of Chemical &
Biological Physics and AMOS at the Weizmann Institute of Science, Israel, where a significant part of
the work was carried out.

Appendix A. Second highest energy configuration
Let us assume that V mm and Vm′ m ′ ′ be the largest and the second largest elements of the potential matrix. We consider following two cases separately:
Case 1: m ′ = m ′ ′ . The system, in its second maximum energy state, in principle, can have α players playing the strategy m and the rest (N − α) playing the strategy m′ . The value of α ranges between
1 ⩽ α ⩽ N. We now prove that α = 1 corresponds to the second maximum energy state in the thermodynamic limit. Let E(N1 , N2 ) denote the energy of the state where N 1 and N 2 agents are playing
the strategies m and m′ , respectively. Let us compare the energies of the states corresponding to α and
(α + 1). Mathematically, lets first examine the case for α = 0:
E (N, 0) − E (N − 1, 1) = (N − 1) (Vmm − Vmm′ ) > 0.

(A1)

Now we move to the generic case,



 
N−α
α
E (N − α, α) − E (N − α − 1, α + 1) =
Vmm +
Vm′ m ′ + α (N − α) Vmm′
2
2




N−α−1
α+1
−
Vmm +
Vm′ m ′ + (α + 1) (N − α − 1) Vmm′
2
2
= (N − α − 1) Vmm − (N − 2α − 1) Vmm′ > 0 ∀α.

(A2)

Therefore, by mathematical induction, it is evident that α = 1 corresponds to the second maximum
energy state in the thermodynamic limit.
Case 2: m ′ ̸= m ′ ′ . The system, in its second maximum energy state, in principle, can have α players
playing the strategy m′ , β players playing the strategy m′′ , and the rest (N − α − β) playing the strategy
m. The values of α and β range between 1 ⩽ α ⩽ N. Let E(N1 , N2 , N3 ) denote the energy of the state
where N 1 , N 2 , and N 3 agents are playing the strategies m, m′ , and m′ ′ , respectively. We prove now that
the case α = 1 corresponds to the second maximum energy state in the thermodynamic limit. Following
the same footsteps as used for the last case, we arrive at the following inequality:
E (N − α − β, α, β) − E (N − α − β − 1, α + 1, β) = (N − α − β − 1) (Vmm − Vmm′ ) > 0 ∀α, β.
14

(A3)

New J. Phys. 27 (2025) 123901

A Mukhopadhyay et al

From the above inequality, it can be concluded by mathematical induction that α = 1 and β = 0 (or,
α = 0 and β = 1, depending on the scenario) corresponds to the second maximum energy state in the
thermodynamic limit, i.e. the population state corresponding to the second highest energy configuration
is always the case where (N − 1) players play the strategy m and only one plays m′ (or, m′′ ).

Appendix B. Ferromagnetic to ferromagnetic transition: a case study
For a symmetric 2 × 2 classical game, consider a path in the (S, T)–plane that begins in the region
1 > T > S > 0 (refer to equation (7) and the subsequent discussion), passes exactly through the degenerate point (S = 0, T = 1), and then continues into the region T > 1 > 0 > S. The degenerate point acts
as a boundary between two game classes: the Harmony game (HG) and the Prisoner’s Dilemma (PD)
respectively. Before reaching the degenerate point, the game has a unique symmetric pure NE (C, C)
because T < 1 and S > 0. At the degenerate point, a player receives the same payoff from choosing C
or D, regardless of the opponent’s action. Consequently, every pure profile and every mixed profile is
a Nash equilibrium at this point.
Immediately after passing the point into the PD region-T > 1, S < 0 (for example, S = −0.5, T =
1.2)-the cooperative equilibrium is destroyed while the defection equilibrium appears, leaving (D, D)
as the unique symmetric pure NE. Thus, when the path crosses exactly through the degenerate point,
the equilibrium structure changes discontinuously. In practice, this means that at the moment of crossing, the players are indifferent, and arbitrarily small perturbations determine the equilibrium around the
degenerate point. In a population of N players, the equilibrium state therefore switches from all cooperation to all defection as the payoff parameters cross the degenerate point.
The same phenomenon can be interpreted using the potential function within the framework of
equilibrium statistical mechanics. The Hamiltonian in equation (2), corresponding to a many-agent allto-all interaction, can be expressed in terms of the strategy variables sµ and sν , which take the values 1
(for strategy C) and 2 (for strategy D), for a symmetric 2 × 2 classical game. The elements of the global
potential matrix in this case are computed using equation (1) as
V11 − V21 = 1 − T,
V22 − V12 = −S.
Owing to the gauge invariance of energy, one of the four elements can be set to zero without loss of
generality. We therefore set V11 = 0 to obtain equation (8).
In a population of N players, each can choose between two strategies, C or D, resulting in 2N possible configurations. If one of the diagonal elements of the potential matrix-say V mm (m ∈ {1, 2})-attains
the maximum value, then under the assumption of perfect rationality, all players will choose the strategy
corresponding to V mm , leading to the state of maximum potential. However, in the absence of perfect
rationality, other configurations with lower potential values may also coexist in the system. These configurations are captured by the terms appearing in the partition function (see equations (3) and (5)). The
partition function represents the total measure of how all possible strategy profiles are weighted according to their potential values at a given finite rationality. Intuitively, it quantifies the likelihood of the system settling into high-potential (more favorable) configurations as compared to low-potential ones.
For example, a configuration with the second-highest potential may consist of (N − 1) players
interacting through V mm , while one player deviates and interacts with the rest via the second-highest
potential element Vmm′ (m, m ′ ∈ {1, 2}). Therefore, in the limit of small noise (corresponding to
almost rational players), the partition function and the internal energy can be expanded as discussed
in equations (5) and (6).
To illustrate the transition between the two ordered collective states (a ferromagnetic-toferromagnetic transition), consider two sets of payoff parameters: one corresponding to the HG and the
other to the PD.
HG: For T = 0.7 and S = 0.5, the potential matrix becomes

V=


0
−0.3
.
−0.3 −0.8

The largest potential element is V11 = 0, corresponding to mutual cooperation. Hence, when all players
choose C, the total potential is maximized. Under perfect rationality, this fully cooperative configuration

15

New J. Phys. 27 (2025) 123901

A Mukhopadhyay et al

forms the stable equilibrium (NE) of the Harmony Game. In this scenario, in the presence of small
noise, using equations (3) and (5), the partition function can be written explicitly as


0.3 (N − 1)
Z (K) = 1 + N exp −
.
(B1)
K
Similarly, from equation (6), the internal energy can be expressed as
⟨E⟩ = −

0.3 N (N − 1)
i.
h
N + exp 0.3(NK−1)

(B2)

Obviously, for perfect rationality (K = 0), the total energy is
⟨E⟩ |K=0 = 0.

(B3)

PD: For T = 1.2 and S = −0.5, the potential matrix becomes


0 0.2
V=
.
0.2 0.7
Here, the largest potential element is V22 = 0.7, corresponding to mutual defection. Therefore, when
all players choose D, the total potential is maximized. This configuration represents the Nash equilibrium of the PD. Here, in the presence of small noise, from equations (3) and (5), the partition function
becomes
 



N
0.5 (N − 1)
Z (K) = exp
× 0.7 1 + N exp −
(B4)
,
2
K
and the corresponding internal energy is given by
 
N
0.5 N (N − 1)
i.
h
⟨E⟩ = 0.7
−
2
N + exp 0.5(N−1)

(B5)

K

Therefore, under perfect rationality, the energy of the system is
 
N
⟨E⟩ |K=0 = 0.7
.
2

(B6)

The transition from global cooperation to global defection as the parameters (T, S) are varied thus
represents a ferromagnetic-to-ferromagnetic transition between two ordered collective states, each characterized by full alignment of the players’ strategies and change in total energy of the system (zero
versus non-zero—as seen above in equations (B3) and (B6)). The point (S = 0, T = 1) on the line
T − S − 1 = 0 serves as the boundary connecting the two game classes—HG and PD—summarized in
table 1.

Appendix C. Three–strategy quantum potential game
A two-player three-strategy quantum game essentially allows the players to choose at least one pure
quantum strategy. By the word, pure, we denote all such quantum strategies that are not accessible in
a classical game setup. One knows that for a symmetric three-strategy classical game to be a potential game, the incentive of pairwise inter-strategy interactions is symmetric with respect to strategyinterchange among the players [3]. Thus, the condition of potentiality for such three-strategy symmetric
games (ПA = ПB = П) turns out to be as follows:
3
X

П (si , si+1 ) =

i =1

3
X

П (si+1 , si ) ,

(C1)

i =1

with s4 ≡ s1 .
This condition of potentiality should be sought for the quantum potential game. For such a game,
with three strategies s1 , s2 and s3 more appropriately denoted as U1 , U2 and U3 , respectively, the potential
the condition can be recast as:
X
X
Π (Ui , Ui+1 ) =
Π (Ui+1 , Ui )
(C2a)
i

i

16

New J. Phys. 27 (2025) 123901

A Mukhopadhyay et al

"
(S − T)

X

|ψ01 (Ui , Ui+1 ) |2 −

X

i

#
|ψ10 (Ui , Ui+1 ) |2 = 0,

(C2b)

i

The first equation is just a rewriting of equation (C1), whereas the second equation follows from the
fact that J(ϵ) is symmetric with respect to both the qubits.
The output state |ψfinal ⟩ = J† (ε)(UA ⊗ UB )J(ε)|00⟩ of the quantum game is described by the following
wavefunctions ψij (UA , UB ) = ⟨ij |ψfinal ⟩:
ε
ε
ψ00 (UA , UB ) = cos2 γA γB + sin2 γA∗ γB∗ ,
2
2
ε
ε
ψ01 (UA , UB ) = − cos2 γA δB − sin2 γA∗ δB
2
2
ε
ε
+ i cos sin (δA γB∗ − δA γB ) ,
2
2
ε
ε
ψ10 (UA , UB ) = − cos2 δA γB − sin2 δA γB∗
2
2
ε
ε
+ i cos sin (γA∗ δB − γA δB ) ,
2
2
ε
ε
ψ11 (UA , UB ) = δA δB − i cos sin (γA γB − γA∗ γB∗ ) .
2
2

(C3a)

(C3b)

(C3c)
(C3d)

We consider a game where both the players have access to a pure quantum strategy (say, U ≡
(γ(θ, ϕ), δ(θ))) along with the classical strategies, Cooperation (C) and Defection (D). In this case,
ψ01 (C, D) = 1,

(C4a)

ψ10 (C, D) = 0,

(C4b)

ε
ε
ψ01 (D, U) = i cos sin (γ ∗ − γ) ,
2
2
ε
ε
ψ10 (D, U) = − cos2 γ − sin2 γ ∗ ,
2
2
ψ01 (U, C) = 0,

(C4d)

ψ10 (U, C) = −δ.

(C4f )

(C4c)

(C4e)

Using equation (C4) in equation (C2), we find the following condition for potentiality to hold:
2

2

[ℜ (γ)] + [ℑ (γ)] cos 2ε + δ 2 = 1
=⇒ sin ε · ℑ (γ) = 0.

(C5)

This essentially implies that unless the initial state is unentangled or the quantum strategy is in ϕ = 0
subspace, the game is not potential. This is along the expected line as in the limit of zero entanglement
the payoffs can be uniquely mapped to a payoff corresponding to a classical mixed strategy, and such a
game is always potential.
Now we consider a game where both the players have assess to one classical strategy C, and two
quantum strategies: Hadamard gate H and U ≡ (γ(θ, ϕ), δ(θ)). In this case,
1
ψ01 (C, H) = − √
2
ψ10 (C, H) = 0,
δ∗
ε
δ
ε
ψ01 (H, U) = − √ cos2 − √ sin2
2
2
2
2
ε ∗
i
ε
+ √ cos sin (γ − γ) ,
2
2
2
γ
ε γ∗
ε
ψ10 (H, U) = − √ cos2 − √ sin2
2
2
2
2
i
ε
ε
+ √ cos sin (δ − δ ∗ ) ,
2
2
2

(C6a)

(C6b)

(C6c)

ε
ε
ψ01 (U, C) = i cos sin (δ − δ ∗ ) ,
2
2

(C6d)

ε
ε
− δ sin2 .
2
2

(C6e)

ψ10 (U, C) = −δ ∗ cos2
17

New J. Phys. 27 (2025) 123901

A Mukhopadhyay et al

Using equation (C6) in equation (C2), we find the following condition for potentiality to hold:
2

2

[ℜ (γ)] + [ℑ (γ)] cos 2ε + [ℑ (γ)] δ sin ε + δ 2 = 1
θ
=⇒ sin ε sin ϕ = tan .
2

(C7)

This is essentially equation (19) used in the main text. It means that in the set-up of two-player
game where each player’s strategy set is { C, H, U(θ, ϕ)}, the game will have a potential structure only
if the parameters in the third strategy U(θ, ϕ) satisfy this transcendental equation. For the case of
maximum entanglement (ε = π/2), the equation simply leads to sin ϕ = tan θ2 and thereby restricting
θ ∈ [0, π/2] (recall, ϕ ∈ [0, π/2]).

Appendix D. Fidelities
Although a straightforward matter, for the sake of completeness, we present here calculations of fidelities
as reported in table 1. In phase II, the equilibrium cooperator fraction is given by equation (14) where
we put T = 1 to get xC = 1 − 1/(2N). Therefore, from equation (27) and equation (28), we arrive at
q
f (λ)

T=1

= 1−
= 1−

2 

1
1 2
1 − 1 − 2N
+ 0 − 2N
√
2

1
.
2N

(D1)

which is continuous in the thermodynamic limit as it approaches 1—the value of fidelity deep inside any
single phase.
Similarly, the fidelity between phases II and III, is found by setting S = 0 in equation (14) to find
xC = 1/(2N) leading to
q
 
2
1
1 2
+ 1 − 1 − 2N
0 − 2N
√
f (λ)
= 1−
S=0
2
1
.
= 1−
2N

(D2)

Lastly, the fidelity between phases I and III, is
q
f (λ)

S=T−1

= 1−

2

2

(1 − 0) + (1 − 0)
√
=0
2

which is discontinuous at the boundary even as N → ∞.

ORCID iDs
Archan Mukhopadhyay  0000-0002-1449-3390
Saikat Sur  0000-0003-4824-6336
Sagar Chakraborty  0000-0001-7568-0598

References
[1] Rédei M (ed) 2005 John von Neumann: Selected Letters (American Mathematical Society)
[2] von Neumann J and Morgenstern O 1944 Theory of Games and Economic Behavior 1st edn (Princeton University Press)
[3] Szabó G and Borsos I 2016 Phys. Rep. 624 1–60
[4] Szabó G and Szolnoki A 2004 Chaos 14 121–31
[5] Scott A D, King D M, Ordway S W and Bahar S 2022 Chaos 32 122101
[6] Si T 2008 Game theory and topological phase transition (arXiv:cond-mat/0601014 [cond-mat.stat-mech])
[7] Imhof L A 2005 Ann. Appl. Probab. 15 1019–45
[8] Blume L E 1993 Games Econ. Behav. 5 387–424
[9] Tah R and Benjamin C 2024 (arXiv:2407.15801 [cond-mat.stat-mech])
[10] Sachdev S 2011 Quantum Phase Transitions (Cambridge University Press)
[11] Vojta M 2003 Rep. Prog. Phys. 66 2069
[12] Hertz J A 1976 Phys. Rev. B 14 1165–84
[13] Sondhi S L, Girvin S M, Carini J P and Shahar D 1997 Rev. Mod. Phys. 69 315–33
[14] Vojta M 2018 Rep. Prog. Phys. 81 064501
[15] Osborne T J and Nielsen M A 2002 Phys. Rev. A 66 032110

18

(D3)

New J. Phys. 27 (2025) 123901

A Mukhopadhyay et al

[16] Continentino M A 2017 Quantum Scaling in Many-Body Systems: An Approach to Quantum Phase Transitions (Cambridge
University Press)
[17] Monderer D and Shapley L S 1996 Games Econ. Behav. 14 124–43
[18] Dunkel J and Schulz A S 2006 On the complexity of pure-strategy nash equilibria in congestion and local-effect games Internet and
Network Economics ed P Spirakis, M Mavronicolas and S Kontogiannis (Springer) pp 62–73
[19] Marden J R, Arslan G and Shamma J S 2009 Trans. Sys. Man Cyber. B 39 1393–407
[20] Buzzi S and Zappone A 2011 Potential games for energy-efficient resource allocation in multipoint-to-multipoint CDMA wireless
data networks (arXiv:1105.2017 [cs.IT])
[21] Bichler M, Legacci D, Mertikopoulos P, Oberlechner M and Pradelski B 2025 Trans. Mach. Learn. Res. (available at: https://
openreview.net/forum?id = Is9APiPg4V)
[22] Lin W, Piliouras G, Sim R and Varvitsiotis A 2025 Quantum 9 1689
[23] Sanz-Martín L, Rivas G, Clavijo-Buriticá N, Herrera M and Parra-Domínguez J 2025 Quantum Inf. Process. 24 291
[24] Rosenthal R W 1973 Int. J. Game Theory 2 65–67
[25] Candogan O, Menache I, Ozdaglar A and Parrilo P A 2013 Math. Oper. Res. 38 474–96
[26] Sandholm W H 2001 J. Econ. Theory 97 81–108
[27] Sandholm W H 2010 Population Games and Evolutionary Dynamics (MIT Press)
[28] Young H P 1993 Econometrica 61 57–84 (available at: www.jstor.org/stable/2951778)
[29] Kandori M, Mailath G J and Rob R 1993 Econometrica 61 29
[30] Reif F 1965 Fundamentals of Statistical and Thermal Physics (McGraw Hill)
[31] Chowdhury D and Stauffer D 2000 Principles of Equilibrium Statistical Mechanics (Wiley)
[32] Ramsey N F 1956 Phys. Rev. 103 20–28
[33] Babajanyan S G, Allahverdyan A E and Cheong K H 2020 Phys. Rev. Res. 2 043055
[34] Asl M M and Sadeghi M 2025 A theoretical framework to explain non-nash equilibrium strategic behavior in experimental games
(arXiv:2501.11404 [physics.soc-ph])
[35] Pandit V, Mukhopadhyay A and Chakraborty S 2018 Chaos 28 033104
[36] Mukhopadhyay A, Sur S, Saha T, Sadhukhan S and Chakraborty S 2024 Physica A 637 129613
[37] Pathria R K and Beale P D 2021 Statistical Mechanics 4th edn (Academic)
[38] Huang K 1987 Statistical Mechanics 2nd edn (Wiley)
[39] Chalker J T 2009 Geometrically frustrated antiferromagnets: statistical mechanics and dynamics (arXiv:0901.3492)
[40] Ramirez A P and Syzranov S V 2025 Mater. Adv. 6 1213–29
[41] Greedan J E 2001 J. Mater. Chem. 11 37–53
[42] Huertas-Rosero A F 2004 A cartography for 2 × 2 symmetric games (arXiv:cs/0312005 [cs.GT])
[43] Meyer D A 1999 Phys. Rev. Lett. 82 1052–5
[44] Eisert J and Wilkens M 2000 J. Mod. Opt. 47 2543–56
[45] Eisert J, Wilkens M and Lewenstein M 1999 Phys. Rev. Lett. 83 3077
[46] Iqbal A and Toor A H 2001 Phys. Lett. A 280 249–56
[47] Flitney A and Abbott D 2002 Fluct. Noise Lett. 2 R175–87
[48] Taylor P D and Jonker L B 1978 Math. Biosci. 40 145–56
[49] Marinatto L and Weber T 2000 Phys. Lett. A 272 291–303
[50] Fra̧ckiewicz P 2013 J. Phys. A: Math. Theor. 46 275301
[51] Benjamin S C and Hayden P M 2001 Phys. Rev. A 64 030301
[52] Johnson N F 2001 Phys. Rev. A 63 020302
[53] Nielsen M A and Chuang I L 2000 Quantum Computation and Quantum Information (Cambridge University Press)
[54] Lin W, Piliouras G, Sim R and Varvitsiotis A 2023 Quantum potential games, replicator dynamics, and the separability problem
(arXiv:2302.04789 [cs.GT])
[55] Fudenberg D and Tirole J 1991 Game Theory (MIT Press)
[56] Weibull J W 1995 Evolutionary Game Theory (MIT Press)
[57] Hofbauer J and Sigmund K 1998 Evolutionary Games and Population Dynamics (Cambridge University Press)
[58] Einstein A, Podolsky B and Rosen P 1935 Phys. Rev. 47 777
[59] Eisert J, Wilkens M and Lewenstein M 2020 Phys. Rev. Lett. 124 139901
[60] Vijayakrishnan V and Balakrishnan S 2019 Quantum Inf. Process. 18 112
[61] Zhang J, Vala J, Sastry S and Whaley K B 2003 Phys. Rev. A 67 042313
[62] Rezakhani A T 2004 Phys. Rev. A 70 052313
[63] Dutta A, Aeppli G, Chakrabarti B K, Divakaran U, Rosenbaum T F and Sen D 2015 Quantum phase transitions in transverse field
spin models: from statistical physics to quantum information (arXiv:1012.0653 [cond-mat.stat-mech])
[64] Zanardi P and Paunković N 2006 Phys. Rev. E 74 031123
[65] Gu S 2010 Int. J. Mod. Phys. B 24 4371–458
[66] Du J, Li H, Xu X, Zhou X and Han R 2003 J. Phys. A: Math. Gen. 36 6551
[67] Cheng J, Mei W, Su W and Chen G 2023 Physica A 611 128447
[68] Miekisz J and Mohamadichamgavi J 2025 Phase transitions in the Prisoner’s dilemma game on the Barabási-Albert graph with
participation cost (arXiv:2505.23370 [q-bio.PE])
[69] Gu S, Kwok H, Ning W and Lin H 2008 Phys. Rev. B 77 245109
[70] Hanauske M, Kunz J, Bernius S and König W 2010 Physica A 389 5084–102
[71] Khan F S, Linke N M, Than A T and Baron D 2025 Quantum Econ. Finance 2 40–51
[72] Harsanyi J C 1973 Int. J. Game Theory 2 1–23
[73] Selten R 1975 Int. J. Game Theory 4 25–55
[74] Auletta V, Ferraioli D, Pasquale F and Persiano G 2011 (arXiv:1107.4537)
[75] Hwang S and Rey-Bellet L 2021 Games Econ. Behav. 126 355–73
[76] Lahkar R, Mukherjee S and Roy S 2023 Games Econ. Behav. 139 133–60
[77] Santis E D and Marinelli C 2007 (arXiv:math/0505608 [math.PR])
[78] Szabó G and Fáth G 2007 Phys. Rep. 446 97–216
[79] Heyl M 2018 Rep. Prog. Phys. 81 054001
[80] Zvyagin A A 2016 Low Temp. Phys. 42 971–94
[81] Van Damme M, Desaules J, Papić Z and Halimeh J C 2023 Phys. Rev. Res. 5 033090

19

