Evolutionary potential games on lattices
György Szabóa , István Borsosa
a Institute for Technical Physics and Materials Science, Centre for Energy Research, Hungarian Academy of Sciences,

arXiv:1508.03147v2 [physics.soc-ph] 29 Mar 2016

P.O. Box 49, H-1525 Budapest, Hungary

Abstract
Game theory provides a general mathematical background to study the effect of pair interactions and
evolutionary rules on the macroscopic behavior of multi-player games where players with a finite number
of strategies may represent a wide scale of biological objects, human individuals, or even their associations.
In these systems the interactions are characterized by matrices that can be decomposed into elementary
matrices (games) and classified into four types. The concept of decomposition helps the identification of
potential games and also the evaluation of the potential that plays a crucial role in the determination of
the preferred Nash equilibrium, and defines the Boltzmann distribution towards which these systems evolve
for suitable types of dynamical rules. This survey draws parallel between the potential games and the
kinetic Ising type models which are investigated for a wide scale of connectivity structures. We discuss
briefly the applicability of the tools and concepts of statistical physics and thermodynamics. Additionally
the general features of ordering phenomena, phase transitions and slow relaxations are outlined and applied
to evolutionary games. The discussion extends to games with three or more strategies. Finally we discuss
what happens when the system is weakly driven out of the ”equilibrium state” by adding non-potential
components representing games of cyclic dominance.

Contents
1 INTRODUCTION

2

2 BRIEF SURVEY OF GAMES
2.1 Players, strategies, payoffs, and potential . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2 Two-player games . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.3 Flow graphs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.4 General features of the potential . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

3
3
5
8
9

3 DECOMPOSITION OF TWO-PLAYER GAMES
3.1 Decomposition of symmetric matrix games . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.2 Decomposition of two-strategy bi-matrix games . . . . . . . . . . . . . . . . . . . . . . . . . .
3.3 Properties of two-player two-strategy games . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.4 Fraternal collaboration versus individualism . . . . . . . . . . . . . . . . . . . . . . . . . . . .

10
11
16
18
20

4 MULTI-PLAYER POTENTIAL GAMES
22
4.1 Pure Nash equilibia in multi-player games . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
5 EVOLUTIONARY POTENTIAL GAMES
5.1 Evolutionary rules leading to Boltzmann distribution . . . . . . . . . . . . . . . . . . . . . . .
5.2 Statistical physics and thermodynamics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.3 Consequences of the extremum principles . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

26
26
28
29

Email addresses: szabo@mfa.kfki.hu (György Szabó), borsos@mfa.kfki.hu (István Borsos)
Preprint submitted to Journal of LATEX Templates

March 30, 2016

6 ISING MODELS
32
6.1 Systems equivalent to Ising models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
6.2 Potts models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
7 FEATURES OF ISING MODELS
7.1 Spontaneous symmetry breaking . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.2 Mean-field theory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.3 Series expansions and duality . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.4 Critical phase transitions on lattices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.5 Ordering in other relatives of the Ising model . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.6 Critical phase transitions on networks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.7 Long-range interactions on lattices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.8 Sublattice ordered structures on lattices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.9 Frustration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.10 Effects of randomness . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

36
36
38
39
41
46
47
50
51
53
54

8 ORDERING PROCESSES
8.1 Evolution in the limit K → 0 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8.2 Interfacial phenomena and rearrangement through nucleation . . . . . . . . . . . . . . . . . .
8.3 Interfacial phenomena in three- and n-state systems . . . . . . . . . . . . . . . . . . . . . . .
8.4 Slow relaxation in random systems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

56
57
58
59
62

9 DEVIATIONS FROM THERMODYNAMICAL EQUILIBRIUM
63
9.1 Effects of matching pennies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
9.2 Effects of rock-paper-scissors game . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
10 CONCLUSIONS AND OUTLOOK

68

Acknowledgements

69

References

69

1. INTRODUCTION
Most games can be considered as simplified real-life situations in which the number of players as well as
their options is limited. The simplest case is represented by two-player non-cooperative games where the
intelligent and selfish players wish to maximize their own payoff that is quantified by a real number and
depending on their simultaneous choices while their utilities are quantified by two payoff matrices [1].
The original concept and application of payoff matrices have been extended basically within the framework of evolutionary game theory [2, 3, 4, 5, 6, 7, 8, 9, 10]. In biological systems the payoff matrices
characterize the resultant fitness (more precisely, the capability to create offspring) for the interacting pair
of species (representing the strategies for this terminology) and serve as a fundamental quantity in the
population dynamics developed in the spirit of the Darwinian selection [11, 12, 13, 14]. In human systems,
however, the imitation of the more successful player can control the time-dependent frequency of players
following a given strategy, in close analogy to biological systems [15, 16, 17, 18, 19].
The first systematic investigations of evolutionary games were performed in well-mixed population of
players for a wide scale of games and strategies. A progressively expanding research area was initiated by
Nowak and May [20] who introduced a model where the players are distributed on a square lattice and
their incomes come from one-shot games with their neighbors. In this cellular automaton type model the
players changed their strategy simultaneously (in discrete time steps) by imitating the strategy of the most
successful neighbor. The numerical investigations of these deterministic models [21] have demonstrated the
advantage of spatial structures for short-range interactions in the maintenance of cooperation among selfish
2

players for the prisoner’s dilemma. Since that time numerous followers have clarified relevant effects and
phenomena supporting the maintenance of cooperative behaviors in real-life situations described by different
versions of social dilemmas as surveyed by Nowak [8], Sigmund [9], Szabó and Fáth [22], Allen and Nowak
[23].
The systematic investigations involve systems where the authors studied the effects of different sets of
strategies, the connectivity structures described by lattices or graphs, and a wide scale of possible evolutionary rules including co-evolutionary games where all the relevant ingredients of the model are allowed to
evolve together with the strategy distribution [24]. Up to now most of the relevant two-person games are
studied within the framework of evolutionary games. New features can be investigated via versions of group
interactions that cannot be decomposed into the sum of pair interactions [25, 26].
Within this wide scale of systems less efforts are focused on the potential games [27], which are related
intimately to the statistical physics [28]. For a more detailed exposition of potential games see the relevant
chapter in the book by Sandholm [10]. The decomposition of the matrix games into the linear combination
of elementary games was discussed previously by Candogan et al. [29], Hwang and Rey-Bellet [30]. The
latter approach allows us to identify different types of pair interactions and also to determine the existence
of potential as well as to evaluate it if it exists [31]. Very recently Cheng [32] has suggested another method
for the evaluation of the potential. The applications and perspectives of potential games within the economy
are reviewed by Mallozzi [33].
In this review we survey briefly the fundamental concepts and background material necessary for understanding the recent and future developments in the research of evolutionary potential games. Due to the
wide scale of research fields involved and the limited length of this article we cannot give a comprehensive
picture. Instead of mathematical rigorousness we use a concise style with an effort to give a wide picture of
the set of phenomena and relationships that are already studied in the fields of statistical physics.
The structure of this review is as follows. The next four Sections summarize the basic concepts and
methods of traditional and evolutionary game theory including the general features of potential games and
the way of the evaluation of potential. Subsequently we discuss the intimate relationship between multiagent evolutionary potential games and Ising type models. Afterwards we briefly survey the phenomena (e.g.,
order-disorder phase transitions) explored by the application of the Ising type models. In Sec. 8 we describe
briefly the ordering processes characterizing the ways how the systems tend towards the final stationary
ordered structure at low noise levels. Section 9 is addressed to discuss what happens when the system
behavior deviates from the thermodynamical equilibrium due to the presence of non-potential components
representing cyclic dominance in the payoff matrices. Finally we outline some challenging questions for the
continuation of research in the near future.
2. BRIEF SURVEY OF GAMES
First we give a concise and tutorial description of the basic definitions and concepts of normal games we
use throughout this work. The reader can find further details of the traditional game theory in standard
textbooks like Fudenberg and Tirole [34], Gibbons [35], Hofbauer and Sigmund [5], Weibull [36], Samuelson
[37], Gintis [6], Cressman [7], Sandholm [10], Sigmund [9] that provide a more general outline of a wider
scale of games and illustrate their application in biology, economics, and behavioral sciences.
2.1. Players, strategies, payoffs, and potential
The normal game is an abstract formulation of a decision situation where each of N players must
choose simultaneously (and independent of each other) one of their own possible options to receive payoffs
dependent on the choices of all of them. Each intelligent and selfish (rational) player wishes to maximize
her own payoff with the assumption that the co-players are also intelligent. In other words, the players
are capable of deducing the best possible way of playing the game and they can handle the problem of the
common knowledge implying the fact that all players know that the others wish to maximize their own
utility, and all players know that all the others know that all of them wish to maximize their own payoff,
etc.
3

In multi-player games the players will be denoted by x = 1, . . . , N . Each player x can choose a pure
strategy sx from her set of strategies indexed by an integer, sx ∈ {1, 2, . . . , nx } where nx denotes the number
of strategies of player x. The choices of all the players are defined by the strategy profile s = (s1 , . . . , sN )
determining their payoff. In this notation each player x receives a payoff ux (s) = ux (s1 , . . . , sN ) quantifying
her utility. The above strategies are pure strategies. In many games (e.g., poker, matching pennies, or
rock-scissors-paper game) the players can also play mixed strategies where they select one of their pure
strategies with a given probability in each decision instance. Henceforth our discussion is limited to the
cases where the players are constrained to use pure strategies.
In the above games each of the N players wishes to optimize her own payoff regardless of the others,
which is complicated by the fact that, in general, none of the players can achieve her maximum payoff
because of the counter-interest of the others. Despite it, the players can be satisfied if they choose a strategy
profile s∗ = (s∗1 , . . . , s∗N ), called Nash equilibrium, that satisfies the following conditions:
∀ x, ∀ sx 6= s∗x :

ux (s∗x , s∗−x ) ≥ ux (sx , s∗−x ).

(1)

where s−x = (s1 , . . . , sx−1 , ss+1 , . . . , sN ) denotes the strategy profile of the co-players. If the inequality is
strict then s∗ is called a strict Nash equilibrium. For the Nash equilibrium the players do not have unilateral
incentive to choose another strategy. In other words, each player is satisfied with her own choice, because
there is no way to receive a higher payoff for the given choices of the others. Nash’s theorem [38, 39] states
that in normal games there exists at least one Nash equilibrium, possibly involving mixed strategies.
For most of the cases the game has more than one Nash equilibrium. In these situations we need
additional criteria for the strategy selection. For example we can choose those Nash equilibria that provides
the higher sum of the individual utilities. Another way of selection, based on the consideration of risk
dominance, was introduced by Harsanyi and Selten [40]. The latter method suggests choosing the strategy
that yields higher expected payoff against an opponent playing a mixed strategy when all feasible strategies
are chosen with equal probability. These additional criteria may give contradictory advices for some games.
Some of the games have attracted huge attention due to their curiosity and the high frequency we face
them day by day. The best known example is the prisoner’s dilemma representing a real-life situation when
the two players have only two options, called cooperation and defection, and the game has only one Nash
equilibrium, the mutual defection, while the mutual cooperation would result in a higher payoff for both
players (hence the dilemma). The analysis of similar situations attracted progressive activity in different
fields of science, including biology, economics, social sciences, and physics [8, 9, 22].
In normal games each player has her own utility function ux (s) to consider. For the potential games we
can introduce a single function V (s), called potential, that involves the strategic incentives of all players
in the following way suggested by Monderer and Shapley [27]. Namely, the difference of the potential
V (s) = V (s1 , s2 , . . . , sN ), when player x modifies her strategy (from sx to s′x ), is equal to the utility
function difference for the given player, that is,
ux (s′x ; s−x ) − ux (sx ; s−x ) = V (s′x ; s−x ) − V (sx ; s−x )

(2)

for ∀ x, ∀ sx , s′x , and ∀ s−x . This means that the potential is constructed from the payoff variations of those
players changing their strategies. Evidently, the existence of a potential for a normal game is strongly
limited by the above conditions. In other words, Eq. (2) gives strict constraints for the possible values
of payoffs. The difficulties can be well illustrated by introducing a dynamical graph [41] where each node
represents a strategy profile s and the edges denote transitions between two strategy profiles when only a
single player modifies her strategy. The sum of the given individual payoff differences is zero along all loops
of this dynamical graph for potential games.
Notice that if only one player modifies her strategy along a loop, e.g., sx (1) → sx (2) → . . . → sx (k) →
sx (1)) (while s−x is quenched) then the sum of the payoff variation:
k
X
i=1

[ux (sx (i + 1); s−x ) − ux (sx (i); s−x )] = 0
4

(3)

because in this sum all payoff components appear twice with opposite signs as sx (k + 1) equals sx (1).
Monderer and Shapley [27] have proved that a normal game admits a potential if and only if over any fouredge loops of the dynamical graph the sum of the changes in the deviator’s payoffs equals zero. Analogously
to the potential energy in physical systems the potential is unique also here up to addition of a constant.
In the literature of game theory one can find a wide range of examples satisfying the conditions of potential
games from genetic competition [42, 4] to congestion game on network [43, 44, 45, 46] or oligopoly games
[47].
The existence of the potential simplifies the analysis. For example, the strategy profile where V (s)
achieves its maximum is a preferred (pure) Nash equilibrium that plays a distinguished role in evolutionary
game theory like the ground state in physical systems.
If the edges of the above mentioned dynamical graph are directed (called flow graph henceforth) by
pointing towards the higher potential value, then the nodes (strategy profiles) with only incoming edges are
Nash equilibria. Similar flow graphs can be derived for the so-called ordinal potential games where a weaker
condition should be satisfied. Namely, if
ux (s′x ; s−x ) − ux (sx ; s−x ) > 0

(4)

V (s′x ; s−x ) − V (sx ; s−x ) > 0 .

(5)

then
Evidently, the existence of a potential prohibits the presence of directed loops here. The advantage of the
latter feature will be demonstrated later. In the literature of game theory one can find other classes of
potential games, that we will not discuss here. For example, besides the exact and ordinal potential games
mentioned above, Monderer and Shapley [27] have introduced the weighted and generalized ordinal potential
games; Voorneveld [48] has studied the best-response potential games; and Morris and Ui [49] investigated
the robust sets of equilibria for the generalized potentials.
The most relevant application of potential games was discovered by Blume [28, 50], who proved that for
a certain set of evolutionary rules the system evolves into a Boltzmann-Gibbs ensemble and the stationary
state can be well investigated by the tools of statistical physics. This feature justifies the importance of the
preferred Nash equilibrium.
Henceforth our analysis will be focused on those multi-player games where the players are allowed to use
only pure strategies and the interaction is composed of two-player games surveyed in the following section.
2.2. Two-player games
For a two-player game with players x and y the payoffs are defined by payoff tables and we can apply the
terminology of matrices. In many cases the strategy labels i and j (i = 1, 2, . . . , nx and j = 1, 2, . . . , ny ) are
sufficient to identify the pure strategies selected by players x and y. For the expression of payoffs, however,
it is convenient to denote the strategies of player x by (nx -dimensional) unit vectors, as
 
 
 
0
0
1
 ... 
1
0

 
 
sx = sx1 = 
(6)
 ...  , sx2 =  ...  , . . . , sxnx =  0  ,
0
0
1
and similar expressions define the strategies of player y. For this notation the payoffs of player x and y can
be expressed by the following matrix products as
ux (sx , sy ) =
uy (sx , sy ) =

sx · Asy ,

(7)
T

sy · Bsx = sx · B sy ,

T
where the matrix elements Aij and Bij define the payoffs of players x and y (we used the relation Bij
= Bji ).
Here P
we have to mention that the above expressions define the average payoffs
for
mixed
strategies,
e.g.,
P
sx = i ρi sxi , when player x uses her ith strategy with a probability ρi ( i ρi = 1). The latter notation

5

is useful for games having mixed Nash equilibrium. If the players are different (like in male-female, youngold, buyer-seller, sender-receiver interactions) then the so-called asymmetric two-player normal games are
specified by two payoff matrices (A and B) and it is customary to use its bi-matrix form, G = (A, BT ),
where the payoffs are given as


T
T
)
(A11 , B11
)
···
(A1ny , B1n
y


..
..
..
(8)
G=
.
.
.
.
T
T
(Anx 1 , Bnx 1 ) · · · (Anx ny , Bnx ny )

For identical players the game is symmetric (A = B and nx = ny = n) and the game is well described by
a single payoff matrix. An additional symmetry occurs in the partnership games [5, 51] (or ”games with
common interests” [27]) when the players share the utility equally, that is, if A = AT .
For the two-player potential games we can introduce a potential matrix


V11 · · · V1ny

..  .
..
V =  ...
(9)
.
. 
Vnx 1 · · · Vnx ny

where the matrix components can also be expressed via the use of a matrix product, namely,
Vij = sxi · Vsyj ,

(10)

that satisfies the conditions
Vkj − Vij
Vil − Vij

= Akj − Aij ,

= Bil − Bij ,

(11)

where i, k = 1, . . . , nx and j, l = 1, . . . , ny .
In order to visualize the relevance of the above constraints we introduce now the dynamical graph
representation of games where each possible strategy profile is denoted by a node arranged in the same way
as in the bi-matrix formalism [see Eq. (8)].
Figure 1 illustrates the dynamical graph for a two-player 3×3 game where the edges of the graph connect
those pairs of strategy profiles where only one of the players changes her strategy. This arrangement of nodes
resembles a 3 × 3 square lattice with periodic boundary conditions. The payoff pairs and the elements of
the potential matrix are indicated within the boxes representing strategy profiles. Notice, that the nodes of
a column (or row) form a complete subgraph for any finite number of strategies. Along these edges we will
consider the payoff variation of only that player who modifies her strategy.
The existence of potential implies that the summarized potential variation (or payoff variation of the
active player) between any two strategy profiles [e.g. along a given series of unilateral strategy changes
from (sxi , syj ) to (sxk , syl )] is independent of the path connecting the initial and final strategy profiles. In
other words, the sum of potential variation is zero along each loop of the dynamical graph. More precisely,
according to Kirchhoff’s laws we should take into consideration only the independent loops, their number is
the difference of the number of edges of the whole dynamical graph and those of its spanning tree [52, 53].
For the 3 × 3 games the dynamical graph has 9 nodes and 18 edges as plotted in Fig. 1 while the spanning
tree has only 8 edges, e.g., those forming a shape of ∃. The number of independent loops is 10 and the
corresponding loops can be constructed by adding edges to the spanning tree consecutively. It is convenient
to select the shortest loop containing the new edge. In the present case, however, the number of non-trivial
independent loops is only 4 because along the three-edge loops (within a column or row) the conditions are
satisfied as it is demonstrated by Eq. (3).
Accordingly, in the present case there are only four independent (internal) four-edge loops that can be
selected as denoted by dashed (red) circles in Fig. 1. Kirchhoff’s law ensures that the conditions of the
existence of potential are satisfied for all the possible loops if it is satisfied for each independent four-edge
loop.
6

A11 ,B11
V11

A12 ,B21
V12

A13 ,B31
V13

A21 ,B12
V21

A22 ,B22
V22

A23 ,B32
V23

A31 ,B13
V31

A32 ,B23
V32

A33 ,B33
V33

Figure 1: (Color online) Dynamical graph with payoff pairs and potential values for a two-player 3 × 3 game. Dashed (red)
circles indicate a possible choice of the four independent four-edge loops to be considered for the existence of potential according
to Kirchhoff’s law.

For general treatment it is useful to discuss in detail the 2 × 2 sub-games where player x can use her
strategy i or j (1 ≤ i < j ≤ nx ) while player y is restricted to select either her kth or lth strategy
(1 ≤ k < l ≤ ny ). The relevant payoff variations for this sub-game are illustrated in Fig. 2. A potential
(i,k)
Aik ,Bki

Bli-Bki

Aik-Ajk

(j,k)
Ajk ,Bkj

(i,l)
Ail ,Bli

Ajl-Ail

Bkj-Blj

(j,l)
Ajl ,Blj

Figure 2: Payoff variations of the active player for a 2 × 2 sub-games along the directed four-edge loops of the dynamical graph.
Within the boxes the upper parameters refer to the strategy profile and the corresponding payoffs are denoted in lower row.

exists if the sums of the payoff variations of the active player along these four-edge loops become zero, that
is,
Bli − Bki + Ajl − Ail + Bkj − Blj + Aik − Ajk = 0
(12)
for all possible 2 × 2 sub-games [27]. Conversely, all the sub-games of a potential game are potential games,
too.
For a two-player game with nx and ny strategies we can distinguish nx (nx − 1)ny (ny − 1)/4 two-strategy
sub-games whereas the number of independent four-edge loops is significantly less, i.e. (nx − 1)(ny − 1),
according to the Kirchhoff laws discussed above. The number of independent and relevant four-edge loops of
the dynamical graph is reduced drastically for the symmetric matrix games. The reduction of the number of
the relevant four-edge loops is related to the equivalence of payoff variations along the loops (i, k) → (i, l) →
(j, l) → (j, k) → (i, k) and (k, i) → (l, i) → (l, j) → (k, j) → (k, i) if A = B. As a result, if condition (12) is
7

satisfied along a loop, then it is satisfied also for its counter-loop.
Additionally, if A = B, then we can distinguish three types of four-edge loops. In the first case, both
players can choose the same two strategies (e.g., i = k and j = l) and then Eq. (12) is always satisfied.
That means that all the symmetric 2 × 2 games (and sub-games) are potential games. Section 3.3 is devoted
to discuss the consequences of this inherent feature.
In the second case the players have a common strategy and their second strategies are distinct. For
example, the upper right loop, indicated by the (red) dashed circle in Fig. 1 represents such a situation
when Eq. (12) becomes
A12 − A21 + A23 − A32 + A31 − A13 = 0 .
(13)
Due to the above-mentioned symmetries this is the only criterion for the existence of potential in the set of
symmetric 3 × 3 matrix games.
The third type of the four-edge loops can appear only for n ≥ 4 because here the players use different
strategy pairs. For example, along the loop (1, 3) → (1, 4) → (2, 4) → (2, 3) → (1, 3) in a four-strategy game
Eq. (12) obeys the following form:
A13 − A31 + A24 − A42 + A32 − A23 + A41 − A41 = 0 .

(14)

The structure of Eqs. (13) and (14) implies a relationship between the existence of potential and the absence
of cyclic components of the basis games (see Sect. 3.1).
In summary, for an n × n matrix game, Kirchhoff’s laws give (n − 1)2 conditions to be satisfied by the
payoff matrix elements (Aij and Bij ) for the potential games. If A = B then the number of independent
conditions is reduced to (n − 1)(n − 2)/2 in agreement with the fact that each symmetric 2 × 2 matrix game
is a potential game and for the symmetric 3 × 3 potential games the nine payoff parameter Aij must satisfy
only one simple linear relation given by (13).
2.3. Flow graphs
The flow graph is the directed version of the dynamical graph where each node represents a strategy
profile and the directed edges connect those strategy pairs which differ in only one of the player’s strategies.
The arrows on these edges point towards the strategy profile resulting in higher income for the player
modifying her strategy unilaterally. Notice that here the (bold) arrows differ from those we used in Fig. 2.
This approach limits the analysis to those cases where the preferences of these unilateral changes are defined.
Some of the properties of potential games are straightforward consequences of well-known results of the
theory of graphs, especially of directed graphs [54]. The flow graphs are simple directed graphs that have
neither parallel edges nor self-loops. Additionally, the flow graph of a potential game is free of directed loops
as mentioned before.
Figure 3 represents a flow graph for a three-strategy game. Due to the intimate relationship between the
dynamical graphs and flow graphs here we use the same arrangement of strategy profiles as in Fig. 1. We
emphasize, however, that for larger number of strategies (nx , ny ≥ 3) the structure resembling the square
lattice with periodic boundary conditions is preserved whereas the graph should be extended by additional
directed edges connecting any pairs located within the same column or row. Remarkably, directed loops
cannot occur within one row (and column) of the flow graph of a matrix game because of the conditions
defined by Eq. (3). Furthermore, within each of these directed subgraphs there exists only one strategy
providing the best income for the given player. As a strict Nash equilibrium is an optimal choice for both
players, therefore the latter fact explains why the number of strict (pure) Nash equilibria is limited by
min (nx , ny ).
Figure 3 shows the flow graph of a three-strategy game having only one strict Nash equilibrium that
can be found by starting the search for any strategy profile and allowing the players to choose unilaterally
a better strategy from their own point of view. After some steps the walk in this directed graph ends in a
Nash equilibrium represented by a node without outgoing edges. Evidently, a similar flow graph holds for
games where the payoffs are modified by smaller components that are not capable of reversing the directions
of arrows.
8

(1,1)

(1,2)

(1,3)

(2,1)

(2,2)

(2,3)

(3,1)

(3,2)

(3,3)

Figure 3: Flow graph for a three-strategy matrix game. Labels of vertices/boxes refer to the strategy profiles and the directed
edges indicate the preferred strategy change for one of the players.

In the textbook of game theory the reader can find different methods for the determination of Nash
equilibria. One of the standard methods is based on the iterated elimination of the strictly dominated
strategies. In the notation of Sect. 2.1, strategy sx of player x is strictly dominated by strategy s′x if
ux (sx , s−x ) < ux (s′x , s−x ) ∀s−x . Such a dominance can be easily recognized in a flow graph. For example,
Fig. 3 represents a game where strategy 3 is dominated by strategy 2 as the arrows connecting the nodes of
the second and third columns are pointed to left. Notice, that for this special case strategy 1 dominates the
other strategies for both players.
As rational players do not play dominated strategies, these strategies can be eliminated. Once we
have eliminated a dominated strategy it can happen that another strategy for one of the players becomes
a dominated strategy. For the games illustrated in Fig. 3 only the (1, 1) strategy profile survives after
repeating this procedure.
The above method will not eliminate rows and columns including a strict Nash equilibrium. The iterated
elimination of dominated strategies simplifies the game and shrinks the flow graph. In many cases the
simplified model may be equivalent to a well-known game (e.g., coordination game).
The number of Nash equilibria is a fundamental question in the theory of games. In the literature of
graph theory [55, 54] the reader can find the discussion of finite directed acyclic graphs, i.e. finite directed
graphs that have no directed loops. Such graphs always have at least one node without outgoing edges,
otherwise a directed walk of arbitrary length could be constructed in the finite graph, as we could always
leave any vertices of the loop, and by the finiteness of the graph the walk would contain a cycle, contradicting
the assumption of acyclicity.
The latter statement specifies the Nash theorem for the case of potential games. Namely, at least one
strict pure Nash equilibrium exists for the potential games. By reversing the direction of the edges, a similar
argument shows, that a finite acyclic directed graph also has at least one node without incoming edges. The
corresponding node is represented by the strategy profile (3, 3) in Fig. 3.
Remarkably, the determination of flow graph for any matrix game can help us find the Nash equilibria as
we only need to identify the strategy profiles without outgoing edge(s). In the rest of this work we discuss
more complex flow graphs corresponding to multi-player games where many Nash equilibria can exist.
2.4. General features of the potential
The linear relationship between the individual payoff variation and potential variation implies general
features. First we emphasize that a game as well as its potential is not influenced if all payoff elements
(including Aij , Bij , and Vij ) are increased with a constant value because the player decisions depend only
on the payoff differences.
9

If a bi-matrix game G = (A, BT ) has a potential V then the game G′ = (αA, αBT ) also has a potential
given as V′ = αV. If α > 0 then the multiplication of the payoff elements can be interpreted as a choice
of new unit. For negative α, however, the game and its Nash equilibria can change drastically, whereas the
existence of potential remains valid.
In addition, if we have two potential games, G = (A, BT ) and G′ = (A′ , B′T ), with potentials V and V′
then the game obtained by the linear combination of payoffs G⋆ = αG + βG′ = (αA + βA′ , αBT + βB′T )
is also a potential game with V⋆ = αV + βV′ .
One can easily check that for symmetric matrix games (A = B) the potential is a symmetric matrix,
i.e., V = VT . This feature is the direct consequence of the fact that players exchange their payoff if
they exchange their strategies. An additional symmetry occurs for the partnership games (A = B and
A = AT ) when V = A. For such situations the players share their income equally, resembling the fraternal
or egalitarian behavior [27, 5, 51]. In that case, the individual and common interests coincide and many
intriguing events (e.g., social dilemmas) are dropped.
Within matrix games we can distinguish games with self- and cross-dependent payoffs [31]. For the crossdependent payoffs the income of each player depends only on the co-player’s strategy, that is the columns
of the payoff matrices are composed of uniform values (γj and δi for j = 1, . . . , ny and i = 1, . . . , nx ) as:




γ1 · · · γny
δ1 · · · δnx


..  .
..  ,
(15)
B = B(cr) =  ... . . .
A = A(cr) =  ... . . .
. 
. 
γ1

δ1

· · · γny

· · · δnx

In these cases the unilateral strategy changes are not motivated by receiving a higher individual payoff
and the corresponding potential is constant (i.e., we can choose V(cr) = 0). On the contrary, for the
self-dependent payoffs the rows of the payoff matrices are constant, namely,




γ1 · · · γ1
δ1 · · · δ1
 .
.
.. 
.. 
..
..
A = A(s) =  ..
B = B(s) =  ..
,
(16)
.
.
.
. ,
δny · · · δny
γnx · · · γnx

and the components of the potential matrix obey the following form:
(s)

Vij = γi + δj ,

(17)

V(s) = A + BT .

(18)

or in matrix notation
The linear relationship between the potential and the payoffs offers the possible use of decomposition
when the matrix games are composed of elementary games reflecting basic symmetries as detailed in the
next section.
3. DECOMPOSITION OF TWO-PLAYER GAMES
In the literature of game theory the concept of decomposition is used in different ways. For most of the
cases the games with many payoff parameters are built from simpler games characterized by a significantly
less number of parameters [see the works by Szép and Forgó [56], Kleinberg and Weiss [57], Sandholm
[51], and Candogan et al. [29]]. This gives us a deeper insight into the general properties of interactions
described by the tools of game theory. Relationship between payoffs, potential, flow graphs, and other types
of interactions are discussed in the papers by Candogan et al. [29, 58], Hwang and Rey-Bellet [30] who used
a different terminology. Now we follow the concept introduced recently in the papers by Szabó et al. [31, 59],
which is based on the introduction of orthogonal elementary basis games representing proper features, e.g.,
games with self- or cross-dependent payoffs. Our analysis will be focused on those decompositions that help
us identify the components prohibiting the existence of potential. This way of decomposition is consistent
with the stability analysis based on the systematic investigations of two-strategy sub-games [60, 61].
10

3.1. Decomposition of symmetric matrix games
Symmetric matrix games are defined by the Aij elements of the payoff matrices (B = A and nx = ny =
n). In the spirit of decomposition, the payoff matrix is a linear combination of four matrices:










0 0
0 0
0 1
1 0
A11 A12
(19)
+ A22
+ A21
+ A12
A=
= A11
0 1
1 0
0 0
0 0
A21 A22
with the suitable coefficients. For a linear arrangement of the matrix components the above four matrices
form a set of orthogonal ”basis vectors” that are called basis matrices or basis games henceforth. We can
choose, however, another set of orthogonal basis matrices representing fundamentally different games that
involve the relevant symmetries. For example, a new set of orthogonal basis matrices can be defined as








1 1
1 −1
1
1
1 −1
f (1) =
, f (2) =
, f (3) =
, f (4) =
.
(20)
1 1
1 −1
−1 −1
−1
1
These basis games were used in many examples studied previously [see e.g. [28, 10]]. The orthogonality is
defined by introducing the scalar product of two n × n matrices as
A·B= B·A=

n
X

Aij Bij ,

(21)

i,j=1

that is zero if A and B are orthogonal to each other. Notice that the basis games given by Eqs. (19) and
(20) form two sets of orthogonal basis matrices as f (m) · f (m′ ) = 0 if m 6= m′ (m, m′ = 1, . . . , n2 ) and
otherwise f (m) · f (m) = N (m) > 0.
Using the orthogonal basis matrices one can express any n × n payoff matrix as
2

A=

n
X

α(m)f (m) ,

(22)

m=1

where the coefficients α(m) are given by the expression
n

α(m) =

X
1
1
Ajk fjk (m).
A · f (m) =
N (m)
N (m)

(23)

j,k=1

The first basis matrix f (1) given by (20) defines a game with constant payoffs. In fact this is the irrelevant
component of the game that does not influence the decision of selfish players and α(1) [defined by Eq. (22)]
is equal to the average value of Aij . The linear combinations of the first and second components (e.g.,
A = A(cr) = α(1)f (1) + α(2)f (2)) describe all games with cross-dependent payoffs. Similarly, the matrix
A = A(s) = α(1)f (1) + α(3)f (3) corresponds to a game with self-dependent payoffs.
In game theory f (4) represents the coordination game when players are enforced to choose the same
strategy. At the same time, the game with payoff matrix A = −f (4) is an anti-coordination game where
the best results can be achieved by the players if they choose opposite strategies. Thus the sign of α(4)
defines whether coordination or anti-coordination type interaction is built into the game and its strength is
measured by |α(4)|.
In the light of the above results, a symmetric two-strategy game is composed of three types of components
representing the self-dependent and cross-dependent payoffs, and the coordination type interaction. Due to
the general features discussed in Sec. 2.4 only two of these components contribute to the potential matrix
that obeys the following form:
V = α(3)[f (3) + f T (3)] + α(4)f (4)
(24)
omitting the arbitrary constant [proportional to f (1)].
The mentioned general features are preserved when the number of strategies is increased, whereas a
fundamentally new type of interaction emerges if n > 2 (or even if B 6= A). This type of interaction
represents the cyclic dominance that prevents the existence of potential.
11

For the illustration what happens for n > 2, we briefly discuss now a possible decomposition of the
symmetric 3 × 3 matrix games. A more detailed analysis is available in a recent paper by Szabó et al. [31]
who suggested the introduction of a set basis matrices representing the two-dimensional Fourier components
of A. Instead of it, now we use another notation based on the dyadic products [59]. In this notation the
basis matrices g(m) (m = 1, . . . , 9) are expressed with the help of dyadic products e(k) ⊗ e(l) (k, l = 1, 2, 3)
of the following three three-dimensional orthogonal basis vectors
 




1
−1
1
e(1) =  1  , e(2) =  −1  , e(3) =  −1  .
(25)
1
2
0

The relationship between the matrix label m and the vector labels k and l is given by the following definitions:


1 1 1
g(1) = e(1) ⊗ e(1) =  1 1 1  ,
(26)
1 1 1


−1 −1 2
g(2) = e(1) ⊗ e(2) =  −1 −1 2  ,
(27)
−1 −1 2


1 −1 0
g(3) = e(1) ⊗ e(3) =  1 −1 0  ,
(28)
1 −1 0


−1 −1 −1
g(4) = e(2) ⊗ e(1) =  −1 −1 −1  ,
(29)
2
2
2


1
1
1
g(5) = e(3) ⊗ e(1) =  −1 −1 −1  ,
(30)
0
0
0


1
1 −2
g(6) = e(2) ⊗ e(2) =  1
1 −2  ,
(31)
−2 −2
4


1 −1 0
(32)
1 0,
g(7) = e(3) ⊗ e(3) =  −1
0
0 0


−1
0
1
1
g(8) =
[e(2) ⊗ e(3) + e(3) ⊗ e(2)] =  0
1 −1  ,
(33)
2
1 −1
0


0
1 −1
1
g(9) =
[e(2) ⊗ e(3) − e(3) ⊗ e(2)] =  −1
0
1.
(34)
2
1 −1
0
Accordingly, the 3 × 3 payoff matrix is expressed by the linear combinations of these g(m)s as
A=

9
X

β(m)g(m) ,

(35)

m=1

where the coefficients β(m) are given by the expression
3

β(m) =

X
1
1
A · g(m) =
Ajk gjk (m),
N (m)
N (m)
j,k=1

12

(36)

and the normalization factors are defined as above, that is, N (m) = g(m) · g(m) .
The present set of basis vectors reflects similar features and symmetries we found for the 2 × 2 payoff
matrices. Namely, the first component g(1) defines a constant (or average) contribution to the payoffs and
for later convenience its contribution will be denoted for n > 2 as
A(av) = β(1)g(1)

(37)

where g(1) denotes the all-ones matrix and
β(1) =

n
1 X
Aij .
n2 i,j=1

(38)

The linear combination of the first three terms [A(cr) = β(1)g(1) + β(2)g(2) + β(3)g(3)] spans the whole
set of symmetric 3 × 3 games with cross-dependent payoffs. On the other hand, the self-dependent payoff
component of a game A can be given as A(s) = β(1)g(1) + β(4)g(4) + β(5)g(5) where values of β(1), β(4),
and β(5) are given by Eqs. (36). Straightforward calculations yield that these portions of payoffs obey a
simple form:


γ1 γ1 γ1
A(s) =  γ2 γ2 γ2  ,
(39)
γ3 γ3 γ3
where γi is equal to the average values of payoffs in the ith (i = 1, 2 and 3) row of A, that is,
3

γi =

1X
Aij .
3 j=1

(40)

The values of γi are equivalent to the average income of player x when she chooses her ith strategy, while
her co-player follows a mixed strategy by choosing the three options with equal probabilities. For games
with more than one Nash equilibria the concept of risk dominance, suggested by Harsanyi and Selten [40],
gives us an additional criterion to select one of them. The risk dominance dictates to choose those strategies
that provide the highest γi value. Accordingly, A(s) quantifies the risk dominance, too. Figure 3 illustrates
the flow graph of A(s) for γ1 > γ2 > γ3 . For games A(s) a potential exists with a potential matrix
V(s) = A(s) + A(s)T as it is detailed in Sect. 2.4.
Evidently, one can perform a similar calculation for the evaluation of the component A(cr) = β(1)g(1) +
P
(cr)
β(2)g(2) + β(3)g(3) with cross-dependent payoffs that can be expressed as Aij = 3i=1 Aij /3. These terms
do not contribute to the potential matrix (V(cr) = 0).
The component g(7) [see (32)] corresponds to an elementary coordination type game where the players
achieve the best if both choose either the first or the second strategy simultaneously. Due to its relevance
this payoff matrix is denoted henceforth as d(1, 2). Additionally, we can introduce further elementary
coordination games d(p, q) defined as

1, if i = j = p,



 1, if i = j = q,
dij (p, q) = −1, if i = p and j = q,
(41)


−1,
if
i
=
q
and
j
=
p,


0, otherwise,

even for n > 3 when 1 ≤ p < q ≤ n that describes similar relationship between the strategies p and q (for
simplicity the n-dependence is not denoted). Notice that d(1, 3) can be obtained from d(1, 2) by exchanging
the second and third rows and columns simultaneously. Although the matrices d(1, 2), d(1, 3), and d(2, 3)
are not orthogonal to each other, these basis games span the three-dimensional subspaces of the coordination

13

type interactions defined as A(coord) = β(6)g(6) + β(7)g(7) + β(8)g(8). Applying the expressions (35) and
(36) one can easily check that, for example,


1
0 −1
1
d(1, 3) =  0
(42)
0
0  = [g(6) + g(7) − 2g(8)] .
4
−1
0
1

The anti-coordination type interactions between any strategy pairs (p < q) are also located along the
half-lines (βd(p, q) with β < 0) in the space of A(coord) . For example, the game with a payoff matrix
A(coord) = −g(7) corresponds to a situation where the players have two equivalent Nash equilibria, namely
the strategy pairs (1, 2) and (2, 1).
The coordination type games include curious cases when the game has three equivalent Nash equilibria.
For instance, the strategy pairs (1, 1), (2, 2), and (3, 3) are equivalent Nash equilibria in a game defined as
A = d(1, 2) + d(1, 3) + d(2, 3). If one exchanges the first and second rows and columns simultaneously in
the latter payoff matrix, then the resultant game is also a coordination type game with three equivalent
Nash equilibria: (1, 2), (2, 1), and (3, 3).
Notice that A(coord)T = A(coord) indicating the coincidence of individual and common interests within
this type of games and the existence of a potential matrix that is identical to the symmetric payoff matrix
[V(coord) = A(coord) ].
The last component (g(9) = A(rps) ) represents the well investigated rock-paper-scissors game that has
only one mixed Nash equilibrium when the three strategies are selected with the same probability. The
rock-paper-scissors games exemplify those systems from ecology to non-equilibrium physics, where three
states (strategies or species) cyclically dominate each other [62, 4, 63, 64, 65].
The rock-paper-scissors basis game (g(9)) has no potential because of the existence of directed loops in
the flow graph shown in Fig. 4. For the illustration of the three-fold symmetries within this flow graph, here
the strategy profiles (nodes) are rearranged. This flow graph illustrates clearly the presence of a directed
six-edge loop along the hexagonal periphery where the thick directed edges represent the ”best response”.
Besides it, this flow graph contains six directed four-edge loops [ see e.g., the loop (1, 2) → (1, 3) → (2, 3) →
(1,2)

(3,2)

(1,1)

(1,3)

(2,2)

(2,3)

(3,3)

(3,1)

(2,1)

Figure 4: Flow graph of the rock-scissors-paper game. Thick edges represent the best responses.

(2, 2) → (1, 2)].
As potential exists for all the linear combinations of the first eight basis games, therefore the absence of
the rock-paper-scissors component (β(9) = 0 ) can be interpreted as a necessary condition for the existence
of potential. The latter condition, more precisely the mathematical expression of A·A(rps) = 0, is equivalent
to (13) we derived previously with the application of the Kirchhoff laws.
14

The payoff matrix g(9) = A(rps) can be considered as the adjacency matrix of a simple directed graph
(shown in Fig. 5) that illustrates graphically the cyclic dominance among the three strategies represented
by the nodes of this dominance graph. In order to avoid confusion with the dynamical and flow graphs here

1

3

2

Figure 5: The adjacency matrix of this three-node directed graph is equivalent to payoff matrix of the rock-paper-scissors game.
The directed three-edge loop refers to cyclic dominance among the three strategies denoted by labeled black bullets.

we used a third way for the graphical illustration of a simple directed graph. The conventions of the arrow
directions in the flow and dominance graphs become identical if the adjacency matrix elements of a directed
graph are defined as Aij = −Aji = 1 if there is a directed link from the strategy (node) j to i and otherwise
Aij = 0. In words, the dominance graph in Fig. 5 corresponds to a game where strategy 1 dominates 2, 2
dominates 3, and 3 dominates 1. This direction convention ensures that the arrows will show the direction
of probability current in evolutionary systems discussed later.
It is noteworthy, that the cyclic dominance graph is analogous to the cyclic food web used in ecological
models to describe the predation-prey relationship. The adjacency matrix of the tree-like dominance graph
(trophic food web) can be related to some anti-symmetric components in the sub-space of games with the
self- and cross-dependent payoffs.
Evidently, one can choose another set of basis matrices with features suitable for the problems to be
studied. For example we can separate the symmetric and anti-symmetric parts of the self- and crossdependent payoffs which allow the analysis of the zero-sum components or the strength of social dilemmas.
Most of the general properties of the symmetric three-strategy games are preserved for n > 3. The
decomposition of a symmetric matrix game into elementary components becomes impressive for n = 2k (k is
an integer) when the columns of the Walsh-Hadamard matrices [66] are used as basis vectors in the dyadic
decomposition [59]. For this choice both the basis vectors and the derived basis matrices are composed
of only +1s and −1s that simplify the calculations [for an example see Eq. (20)]. These calculations have
confirmed the relevance of the mentioned four types of interactions for n = 4 [59]. Similar results are
concluded by Candogan et al. [29], Hwang and Rey-Bellet [30] who studied the decomposition of n-strategy
games without introducing a definite set of basis games.
According to the analyses mentioned, the games with self-dependent payoffs are spanned by n dyadic
products, as e(1) ⊗ e(j) for j = 1, . . . , n, of an orthogonal set of basis vectors (e(1), . . . , e(n)) when the
first one is composed of only +1s, that is, ei (1) = 1 for i = 1, . . . , n. In this notation the basis games with
cross-dependent payoffs are given as e(j) ⊗ e(1). The all-ones matrix (g(1) = e(1) ⊗ e(1)) belongs to both
types and plays the role of irrelevant term. Its coefficient β(1) quantifies the average payoff. The direct
pair interactions are missing within their unified parameter space spanned by the (2n − 1) orthogonal basis
matrices that may even be divided into the sum of symmetric (e(1) ⊗ e(j) + e(j) ⊗ e(1)) and anti-symmetric
(e(1) ⊗ e(j) − e(j) ⊗ e(1)) basis matrices. Thus the unified parameter space of A(cr) and A(s) can also be
spanned by the mentioned n symmetric and (n − 1) anti-symmetric basis games.
The rest of the symmetric parameter space of games is equivalent to the linear combinations of the
additional symmetric basis matrices defined by the dyadic products as e(k) ⊗ e(j) + e(j) ⊗ e(k) if 1 < k ≤
j ≤ n. Hwang and Rey-Bellet [30] have shown that this set of games (denoted as A(coord) ) are also spanned
by the n(n − 1)/2 d(p, q) matrices defined by Eq. (41) (for 1 ≤ p < q ≤ n). Notice that all the mentioned
basis matrices of A(coord) are orthogonal to both A(s) and A(cr) because the sums of the matrix elements
are zero in the rows and columns separately. The number of these orthogonal basis games, as well as the
number of the independent d(p, q) matrices, is n(n − 1)/2.
The rest of the anti-symmetric parameter space of the payoff matrix is spanned by the orthogonal basis
15

matrices e(k) ⊗ e(j) − e(j) ⊗ e(k) where 1 < k < j ≤ n. The number of these orthogonal basis games is
(n − 1)(n − 2)/2 and their linear combinations are also denoted by A(cycl) because of the presence of cyclic
dominance.
Calculations [59] for n = 4 have indicated that A(cycl) is spanned by three orthogonal basis games
defined by the adjacency matrices of the four-edge directed graphs plotted in Fig. 6. Additionally, A(cycl)

(a)

(b)

1

4

2

(c)

1

4

2

3

1

4

2

3

3

Figure 6: The adjacency matrices of these four-edge directed graphs are orthogonal to each other and represent the three cyclic
basis games for n = 4.

contains games where the cyclic dominance is limited to three strategies as in the rock-paper-scissors game.
For example, the sum of these three cyclic orthogonal basis games is equivalent to a rock-paper-scissors
type sub-game (with strategies 2, 3, and 4). The knowledge of these three cyclic basis games simplifies the
identification of potential games, because it is enough to check whether the scalar products of A by the
three cyclic basis games become zero simultaneously, or not. Potential exists if all these scalar products are
zero.
For n > 4, however, determining the existence of potential becomes difficult because of the large number
of the possible four-edge and three-edge loops illustrated in Fig. 7. It is emphasized, that the orthogonality

(a)

(b)

1
n

j

1
n

2
i

2

k

i
l

j

k
Figure 7: Directed graphs with n nodes and a single three- (a) or four-edge (b) directed loop.

between A and the adjacency matrices of these types of the directed graphs reproduces the same conditions
for the existence of potential that we have derived in Sec. 2.2. The application of the Kirchhoff laws gives
us a method to select (n − 1)(n − 2)/2 independent loops to be checked.
In sum, the payoff matrix of a two-player symmetric game can be decomposed into the sum of four
classes of payoff matrices representing the self-dependent, the cross-dependent, the coordination, and the
cyclic dominance type interactions. More precisely,
A = A(s) + A(cr) − A(av) + A(coord) + A(cycl) ,

(43)

that takes into consideration that A(av) is involved in A(s) and A(cr) . Potential exists if A(cycl) = 0 and the
potential matrix can be given as
V = A(s) + A(s)T + A(coord) .
(44)
3.2. Decomposition of two-strategy bi-matrix games
The decomposition of the bi-matrix games requires the straightforward extension of the scalar product
of two bi-matrix games analogously to the traditional scalar product of two vectors. As the bi-matrix game
16

G is described by the elements of two matrices (A and B), therefore the scalar product of the games G and
G′ (determined by (A′ and B′ )) is defined as
G · G′ =

n
X

′
[Aij A′ij + Bij Bij
].

(45)

i,j=1

The decomposition of the two-strategy games becomes impressive if we use the following orthogonal basis
games:


( 1, 1) ( 1, 1)
f ′ (1) =
(46)
( 1, 1) ( 1, 1)


( 1, 1) (−1, 1)
f ′ (2) =
(47)
( 1, −1) (−1, −1)


( 1, 1) ( 1, −1)
f ′ (3) =
(48)
(−1, 1) (−1, −1)


( 1, 1) (−1, −1)
f ′ (4) =
(49)
(−1, −1) ( 1, 1)


( 1, −1) ( 1, −1)
f ′ (5) =
(50)
( 1, −1) ( 1, −1)


( 1, −1) (−1, −1)
f ′ (6) =
(51)
( 1, 1) (−1, 1)


( 1, −1) ( 1, 1)
f ′ (7) =
(52)
(−1, −1) (−1, 1)


( 1, −1) (−1, 1)
f ′ (8) =
(53)
(−1, 1) ( 1, −1)
that are composed of +1s and −1s. Using these orthogonal basis games, all the two-strategy bi-matrix
games can be given as
8
X
G=
α′ (m)f ′ (m)
(54)
m=1

′

where the coefficients α (n) are expressed as before, i.e.,
α′ (m) =

1
G · f ′ (m).
8

(55)

Notice that the first four basis games span the parameter space of the symmetric games when B = A,
that have been discussed previously. In other words, f ′ (1), . . . , f ′ (4) denote the bi-matrix version of the
symmetric two-strategy orthogonal basis games given by Eqs. (20).
The linear combinations of the additional second four basis games describe the anti-symmetric games
where B = −A. The resulting four basis games [f ′ (5), . . . , f ′ (8)] are obtained from the first four ones by
reversing the sign of payoffs received by the second player. All these basis games represent some properties.
For example, the coefficient of f ′ (5) quantifies the difference in the average payoffs between the players x
and y.
The games with self-dependent payoffs are given as
G(s) = α′ (1)f ′ (1) + α′ (3)f ′ (3) + α′ (5)f ′ (5) + α′ (7)f ′ (7),

(56)

and the resultant payoff matrices A(s) and B(s) are composed of uniform rows with payoff parameters
(s)
(s)
representing averages values as for the symmetric games (e.g., Aij = (Ai1 +Ai2 )/2 and Bij = (Bi1 +Bi2 )/2).
17

Similar expressions define the components with cross-dependent payoffs:
G(cr) = α′ (1)f ′ (1) + α′ (2)f ′ (2) + α′ (5)f ′ (5) + α′ (6)f ′ (6).

(57)

The basis game f ′ (4) defines the symmetric coordination type interaction with payoffs A(coord) =
B(coord) = α′ (4)f (4) where f (4) is defined by Eq. (20).
The bi-matrix game f ′ (8) is equivalent to the matching pennies game, which is a well-known zero-sum
game where the first player wins a payoff unit from the co-player if they both choose the same strategy. For
opposite choices the second player wins 1 from the first player. This game has a mixed Nash equilibrium,
where the players choose their strategy at random.
The flow graph of the matching pennies game (see Fig. 8) illustrates the appearance of a directed loop
because for each strategy profile the unsatisfied player can increase her own payoff by 2 by reversing her
strategy. As a result, if in an iterated game the randomly selected player is allowed to modify her own

Figure 8: For the matching pennies game one of the players always wishes to reverse her strategy in a way maintaining cyclic
strategy modifications.

strategy unilaterally then the actual strategy profile will evolve cyclically. Such situations were reported
previously by van Valen [67, 68] who suggested the concept of Red Queen mechanism to explain biological
evolution via a constant arm race between co-evolving species. The interactions between buyers and sellers
[69], property owners and criminals [70], or conformists and rebels [71] exhibit similar features. For very
recent investigations of the Red Queen mechanism at the level of population dynamics we suggest reading
the papers by Sardanyés and Solé [72] and Juul et al. [73]. The cyclic variation in the strategy profiles has
been observed by Xu et al. [74] in human experiments.
Evidently, potential does not exist for the matching pennies game and also for those two-strategy bimatrix games that include this component. It is needless to emphasize that the bi-matrix game G = G(pot)
is a potential game, if α′ (8) = G · g(8) = 0, and the latter existence criterion for the potential is equivalent
mathematically to Eq. (12) for the particular case when i = k = 1 and j = l = 2.
For the rest of (seven) basis games the potential of a non-symmetric bi-matrix game can be easily
determined. According to this calculation, the potential matrix V(bmg) can be built up only from three
components as
V(bmg) = α′ (3)[f (3) + f T (3)] + α′ (4)f (4) + α′ (7)[f (3) − f T (3)].
(58)
It is worth mentioning that the game G = G(pot) + α′ (8)f ′ (8) can even be an ordinal potential game with
the potential of G(pot) [given by Eqs. (58)] if |α′ (8)| does not exceed a threshold value dependent on the
payoff differences in G(pot) , more precisely, if the contributions of the matching pennies game cannot reverse
the arrow directions in the flow graph that ensures the existence of at least one pure Nash equilibrium.
Conversely, if the cyclic component dominates the system behavior, then the game has only a mixed Nash
equilibrium until G(pot) is weak enough to reverse the flow direction along at least one edge in the flow
graph.

3.3. Properties of two-player two-strategy games
In the previous sections we have shown a general method to evaluate the potential matrix in the absence
of cyclic (or matching pennies) components. This method is based on the concept of decomposition and
18

exploited the symmetries simplifying the calculations. Now we introduce another method and notation to
discuss the general properties of the two-player two-strategy games.
For a deeper discussion of the symmetric two-strategy games (A = B) we use the traditional notation
introduced for the investigation of social dilemmas [75, 76, 9] where the strategies are called defection and
cooperation (in short sx1 , sy1 = D and sx2 , sy2 = C). Within this terminology both players receive P (punishment) or R (reward) for mutual defection or cooperation meanwhile the defector receives T (temptation)
and her cooperative co-player gets S (sucker’s payoff) if they choose opposite strategies. For the case of
prisoner’s dilemma (S < P < R < T ) both selfish players are enforced to choose defection (this is the pure
Nash equilibrium) because the cooperation is a dominated strategy, that is, the players receive higher payoff
when choosing D irrespectively of the co-players decision. The curiosity of the prisoner’s dilemma game is
that the players’ rational (selfish) choices yield a suboptimal outcome.
There are two other (weaker) social dilemmas, namely the hawk-dove [3] (called also snowdrift [77] or
chicken [78]) game (with a payoff rank of P < S < R < T ) and the stag hunt game (S < P < T < R). Most
of the previous analyses are performed when setting P = 0 and R = 1 without loss of generality.
In the terminology of social dilemmas the bi-matrix of the symmetric two-strategy game is usually given
as


(0, 0) (T, S)
G = G(sd) =
.
(59)
(S, T ) (1, 1)
For these payoff parameters the three social dilemmas are positioned on the S − T plane as illustrated in
Fig. 9 where four regions are distinguished.
S
H

HD

SH

PD

1

0

-1

0

1

2

T

Figure 9: (Color online) Four types of symmetric two-strategy games can be distinguished as a function of T and S for the
notation of social dilemmas when the black and white bullets represent D and C strategies. The four segments are characteristic
to games abbreviated as: H = harmony; HD = hawk-dove; SH = stag hunt; and PD = prisoner’s dilemma. The pure Nash
equilibria are represented by nodes without outgoing edges in the flow graphs.

Within each region the two-person game can be characterized by the same flow graph denoted. It is
emphasized that these notations of strategies and payoffs are related to the case of the prisoner’s dilemma
game. For other types of games one can find more suitable names for the strategies and payoffs, e.g., for the
hawk-dove game the players are to choose between the aggressive and peaceful (conflict avoiding) behaviors
and the resultant payoff can be well described by using the terms of equal share of benefit, exploitation, and
cost of injury. Anyway, the hawk-dove game has an additional mixed Nash equilibrium when the players
choose one of their two strategies with a probability dependent on the payoffs.
19

The absence of additional types of flow graphs is related to the symmetries that prescribe equivalent
payoff variations for the active player deviating from the (D, D) or (C, C) strategy profiles. Due to these
symmetries all the symmetric two-strategy games are potential games and the potential matrix is formally
given by Eq. (24) with the decomposition of the payoff matrix


0 T
(sd)
A=A
=
(60)
S 1
into the sum of four components [as defined by Eqs.(22) and (20)] with coefficients
α(1) =

S−T −1
T −S−1
1−T −S
T +S+1
, α(2) =
, α(3) =
, α(4) =
.
4
4
4
4

According to Eq. (24) the potential obeys the following form:




1 −1
2
0
(sd)
V
= α(4)
+ α(3)
.
−1
1
0 −2

(61)

(62)

This expression will be used in Sec. 6.1 to illuminate the relationship between the Ising models and the multiagent evolutionary games, if the interaction is defined by symmetric two-strategy games. It is emphasized,
however, that the above potential matrix can be expressed by an even simpler expression,


0
S
V(sd) =
,
(63)
S 1−T +S
that is obtained from (62) by adding a suitable constant to Vij s. The second version of the potential can
be evaluated by using a simple algorithm. First we choose V11 = A11 , subsequently V12 = V21 = A21 , and
finally V22 = V12 + A22 − A12 in the spirit of Eqs. (2). This method can be adopted for larger number of
strategies if the existence of potential is already justified. The resultant potential matrices are convenient
when deriving phase diagrams for some types of multi-agent evolutionary games.
It is worth mentioning that the values of the potential are equal for the two pure Nash equilibria [(C, D)
and (D, C)] within the region of the hawk-dove game (see Fig. 9). On the contrary, the potential values
differ between the (D, D) and (C, C) Nash equilibria within the region of stag hunt games. To be more
quantitative, (C, C) is the preferred Nash equilibrium if S > (T −1) when T < 1 and the strategy pair (D, D)
is preferred if S < min [(T − 1), 0]. The location of the preferred Nash equilibria is illustrated graphically in
the next section (see Fig. 10) where it is contrasted with the case of collaborating players.
Within the region of the hawk-dove (or anti-coordination) games the equivalence between (C, D) and
(D, C) Nash equilibria is evidently broken if A 6= B. For these bi-matrix games the potential (58) obeys
the form:






1 −1
2
0
0
2
V(bmg) = α′ (4)
+ α′ (3)
+ α′ (7)
,
(64)
−1
1
0 −2
−2
0
that we use later when drawing a parallel between the multi-agent evolutionary games and Ising models.
Now we emphasize that the first components in Eqs. (62) and (64) measure the strength of coordination
type interaction, the second ones quantify the potential difference between the (1, 1) and (2, 2) strategy pairs
whereas the third term distinguishes the potential value between the states (1, 2) and (2, 1).
3.4. Fraternal collaboration versus individualism
In traditional game theory [1] the formation of coalition is permitted for the so-called cooperative games.
Some of the essential elements of the games are dropped if the players are allowed to agree in how they wish
to increase the sum of their income for two-player potential games. On the other hand, such situations can
occur frequently in our everyday life. Thus we analyze now what happens if fraternal players try to maximize
their total income shared equally. The results can serve as a reference when comparing actions motivated by
individual or common interest. For this goal we introduce a reevaluated payoff matrix, A(fr) = (A + AT )/2,
20

defining the individual payoffs for symmetric games with n strategies. For these games the individual and
common interests coincide and the preferred Nash equilibrium may differ from those proposed for a potential
game A.
The equal share of payoffs eliminates the anti-symmetric components of A and the corresponding potential matrix is given as V(fr) = A(fr) . In the two-strategy social dilemma notation discussed above


0
(T + S)/2
(fr)
(fr)
V
=A
=
(65)
(T + S)/2
1
which predicts two distinct regions on the T − S plane when considering the preferred Nash equilibrium
that may be either (C, C) (if (T + S) < 2) or the (C, D) or (D, C) strategy profiles (if (T + S) > 2). The
latter results differ strikingly from those we obtained above as it is illustrated in Fig. 10. The differences in
the location of the maximum matrix elements of V [see Eq. (63)] and V(fr) imply social dilemmas for the
two-strategy games.

S

S
(D,C)
or
(C,D)

1

(C,C)

(D,C)
or
(C,D)

1

0

0

(C,C)
(D,D)

-1
0

1

2

-1

T

0

1

2

T

Figure 10: Preferred Nash equilibria for selfish (left) and fraternal (right) players. Dash-dotted lines divide the S − T plane
into four regions nominated in Fig. 9

A similar comparison can be performed for other potential games even for n > 2. In that case we use
the notation of Eq. (43) when potential exists if A(cycl) = 0 and the resulting potential matrix is determined
by only two components (A(s) and A(coord) ) as expressed in (44). For these games the effective payoff and
potential matrices for fraternal players involve the contribution of A(cr) , too, as
1
V(fr) = A(fr) = A(coord) − A(av) + [A(s) + A(s)T + A(cr) + A(cr)T ].
2

(66)

We face ”social dilemma” if the preferred Nash equilibria are distinct, that is, when (i, j) 6= (i′ , j ′ ) where
(fr)
(fr)
max [Vkl ] = Vij and max [Vkl ] = Vi′ j ′ . The conflicting situations involve cases when the selfishness results
in lower payoffs for both players (as it happens for the prisoner’s dilemma) or also those ones when the loss
of the sucker exceeds the extra profit of the winner. The discrepancy between the individual and common
interests can be quantified by
V − V(fr) =

1 (s)
[A + A(s)T − A(cr) − A(cr)T ]
2

(67)

depending only on the self- and cross-dependent components. More precisely, V − V(fr) is the potential of
the antisymmetric portion of the self- and cross-dependent payoff components defined as (A(s) + A(cr) −
A(s)T − A(cr)T )/2 = A − AT . Accordingly, no dilemmas arise if A(s) = A(cr)T . In the light of this result
for a symmetric n-strategy potential game we have (n − 1) independent parameters to control the absence
or presence of the social dilemma in the above sense.
The social dilemmas and their consequences are preserved for spatial multi-agent evolutionary games with
equivalent players if logit rules control the strategy updates as it is demonstrated by Szabó and Szolnoki
[79] who studied cases of non-equal sharing for n = 2.
21

4. MULTI-PLAYER POTENTIAL GAMES
Up to this point we have discussed only two-player games. Evidently the sum or any linear combinations
of independent two-player potential games are also potential games as the original conditions (2) are satisfied.
This situation remains valid even for the cases when some of the players participate in more than one potential
games using the same strategies in each action. Remarkably, if a player uses two (or more) strategies against
her co-players then she can be considered as two (or more) players. In many biological and economical
systems the strategy represents the type of species or behavior that is the same for all the interactions for
a given individual. For human systems, however, one can assume that the players use different strategies
in the games they participate. Furthermore, human players can use mixed (stochastic) strategies in the
repeated games.
Henceforth we assume that the players use pure strategies expressed by unit vectors [see Eq. (6)] for
each player x = 1, . . . , N where N denotes the number of players. In the present game theoretical models
the players wish to maximize their own payoff by consecutive strategy refreshments disregarding the payoff
variation for all the other co-players. If the players play two-person potential games with a subset of the
other players, then their individual motivation can be well quantified by the variation of potential
X
sx · V(x, y)sy
(68)
U (s) =
hx,yi

where the summation runs over all interacting pairs (denoted as hx, yi) defined by the edges of the connectivity graph where each node represents a player.
In real social systems the pair potential may be different for all interacting pairs as indicated by the
expression V(x, y). In most of the cases, however, we assume that the players are equivalent and the games
are uniform. For the latter discussions the arguments of the potential matrix V are omitted. Many relevant
features of spatial evolutionary games can be investigated where the equivalent players are located on the sites
of lattice with periodic boundary conditions. The investigation of these systems can be efficiently supported
by the methods developed for studying models of solid state physics where all the relevant symmetries are
satisfied.
The latter simplifications exclude the analysis of systems with players interacting via non-symmetric
games. At the same time, the systematic investigation of the multi-agent systems with non-symmetric
games can be performed on bipartite networks that give us a convenient connectivity structure. For these
multi-agent systems we distinguish two types of players (e.g. males and females, buyers and sellers, etc.)
who are distributed on a bipartite graph providing that each player plays games with players of opposite
type. For these systems the connectivity network is divided into two subgraphs with sites x ∈ X and y ∈ Y .
The bipartite connectivity graph ensures that players at sites x ∈ X interact exclusively with those at sites
y ∈ Y , and vice versa.
Such a situation can even be realized in lattice systems. For example, if the players are located at the
sites of a square lattice, then the sites are divided into two equivalent sublattices corresponding to the white
and dark squares of the chessboard. These systems will be discussed later in Sec. 6.1 and 9.1.
The first investigations of the multi-agent evolutionary games were performed for well-mixed populations
corresponding to a complete connectivity graph where interactions exist between all the possible pairs. Since
the pioneering work of Nowak and May [20, 21] the games are studied progressively on different lattices.
For these spatial systems the sites are equivalent if periodic boundary conditions are applied for a finite
square box of L × L = N sites and the interactions are restricted to the same size of neighborhood for each
player (e.g., nearest or nearest and next-nearest neighbors). The main advantage of the lattice structured
population is based on the translation symmetry providing good conditions for studying the consequences
of some characteristic features in the structure of neighborhood.
For real social systems, however, the irregular networks give a more adequate background for the investigation of multi-agent systems. This is the reason why the analysis of lattice systems was extended to different
graphs representing diluted lattices [80, 81], real social networks [82] random graphs [83, 84, 85, 86, 87] including different small-world [88, 89] and scale-free networks [90, 91].
22

4.1. Pure Nash equilibia in multi-player games
In this section we briefly survey the relevant variations in the number of Nash equilibria when an N player game on a lattice (or network) is built from pair interactions between the neighbors. Regardless of the
connectivity structure, the multi-agent systems have 2N microscopic states (s) if all the pair interactions are
characterized by a 2 × 2 game. Furthermore, if the possible transitions between two microscopic states are
limited to those s → s′ where only one player modifies her strategy (e.g., sx → s′x ) then the dynamical graph
can be represented by an N -dimensional hypercube [41, 92]. Such a dynamical graph is shown (for N = 4) in
Fig. 11 where the nodes and edges of the four-dimensional hypercube are projected onto a two-dimensional
plane from a suitable direction in such a way that the number of players playing the first strategy differs by
1 from level to level. Notice that the parallel edges represent strategy changes for the same player while the

Figure 11: The flow graph in a four player potential game if the potential is composed of two-player coordination games when
players benefit from choosing the same strategy.

strategy profiles are different on the neighborhood. If the strategy profile evolves along the directed edges
then the system evolves into one of the two Nash equilibria. Such a behavior occurs when randomly chosen
players are allowed to increase their income by choosing another strategy in the knowledge of their other
possible payoff(s). The iteration of this process ends in one of the Nash equilibria that are absorbing points.
Evidently the final state depends on the initial state. The latter method can be considered as a way to find
pure Nash equilibria [93, 44, 94, 29].
This method can be utilized for all the potential (and ordinal potential) games to find pure Nash equilibria due to the absence of directed loops in their flow graph. The N -player systems have only one Nash
equilibrium if the interaction is composed of pair interactions belonging uniformly to either the harmony or
prisoner’s dilemma games.
In the example illustrated in Fig. 11 there are only two Nash equilibria and each has a basin of attraction
in the space of strategy profiles. A similar behavior occurs for larger number of players if all the possible
pairs interact via a coordination game.
More sophisticated processes occur in a spatial system where the players are located on a square lattice
and play stag hunt games with their four nearest neighbors. In that case if we allow a randomly chosen
player to increase her payoff by choosing the opposite strategy then the iteration of these steps drives the
system into the homogeneous D state (sx = D ∀x) if the sufficiently large system is started from a random
initial strategy profile for S < T − 1 and T < 1 (see the left plots in Fig. 12). This is the preferred Nash
equilibrium where U (s) reaches its maximum. This system, however, has many other Nash equilibria that
may be achieved by the application of the above evolutionary dynamics if we choose different initial states as
it is illustrated in Fig. 12. The reader can easily check that in the homogeneous C state (sx = C ∀x) nobody
can benefit from changing her strategy unilaterally. This feature implies that the latter Nash equilibrium
has a finite basin of attraction if the formation of a D − D pair on two neighboring sites is not favored
23

Figure 12: Final spatial distributions of strategies (Nash equilibria) (lower snapshots) if the evolution is started from three
different initial states (upper snapshots) when the players play stag hunt games (T = 0.5, S=-0.6) with the four neighbors on
the square lattice. In the left case the system is started from a random initial state where D and C strategies are present with
the same probability. In the initial state of the middle case Ds are created randomly with a probability of 0.02 . For the right
case the latter initial state is modified by adding two rectangular blocks of Ds.

either. Consequently, the second Nash equilibrium can be achieved from such a random initial state where
the ratio of D and C strategies is small and typically only isolated D strategies or small cluster of Ds are
present in the sea of Cs. Such a situation is illustrated by the middle pair of snapshots of Fig. 12.
Despite the small ratio of D strategies, larger clusters of Ds may also appear in the random initial state,
particularly if the system is sufficiently large [for a more quantitative analysis we suggest consulting surveys
of percolation theory [95, 96]]. If the size of a rectangular cluster of Ds exceeds a threshold value, then this
colony can remain alive or it can even expand if this process is supported by the presence of solitary Ds
along the periphery as demonstrated in the plots at the right of Fig. 12. Consequently, the selected Nash
equilibrium depends on the initial state and also on the random strategy refreshment of players.
Similar phenomena can be observed for the spatial stag hunt games if S > T − 1. The only difference
is that the roles of the D and C strategies are exchanged in the evolutionary processes. On the contrary, a
basically different behavior occurs along the boundary S = T − 1 separating the above discussed regions of
parameters where the homogeneous states form a frozen poly-domain structure as demonstrated in Fig. 13.
As this is the typical behavior in the whole region of the hawk-dove games, we will not discuss the resulting

Figure 13: Typical distribution of D and C strategies on a square lattice in a Nash equilibrium occurring in the stag hunt
region for S = −0.5 and T = 0.5.

processes separately.
Within the region of hawk-dove games (T > 1 and S > 0) the lattice system has two equivalent sublattice
24

ordered states where the potential reaches its maximum. The analysis of these states requires the introduction of two sublattices (X and Y ) as described above. In the first ordered structure the sites of sublattice
X are occupied by Ds, and Cs are in the other sublattice. For the second ordered structure the sublattice
occupancies are reversed. These long range ordered structures are equivalent (because of the translation
symmetry) and can be observed in finite systems if the linear size L is even for periodic boundary conditions.
If such a system is started from a random initial strategy distribution, then the random strategy update
of players favoring the increase of their own payoff results in a frozen poly-domain structure as illustrated
in Fig. 14. Similar patterns are reported by Sysi-Aho et al. [97], who studied additionally the cases where
second neighbor interactions are also taken into consideration.

Figure 14: Typical strategy distributions on a 50 × 50 box of sites for Nash equilibria in a HD game on a square lattice for
nearest neighbor interactions if S = 0.2 (left panel) and S = 0.4 (right panel) for T = 1.3.

In the frozen poly-domain structures both types of ordered strategy arrangements are recognizable within
the domains. Notice the absence of point defects inside the ordered spatial regions where the players are
satisfied and will not modify their strategy. The opposite ordered structures are separated by boundary
layers. The average composition of these boundary layers, however, depends on the sign of S − T + 1 as
demonstrated by two opposite examples in Fig. 14.
Evidently, the above-mentioned difference in the boundary layers vanishes if S − T + 1 = 0 because the
interface becomes a mixture of two types illustrated in Fig. 14. In this special case there are many players
along the interfaces who have the same payoff for the opposite strategies. If we additionally allow these
players also to modify their strategy, then these additional stochastic events in the strategy update yield
a domain growing process that drives the system into one of the homogeneous sublattice ordered strategy
arrangements. This evolutionary process is demonstrated in Fig. 15 where the time is measured in the unit
of Monte Carlo steps (MCS) [within one MCS each player receives a chance once on the average to change
her strategy].

Figure 15: Three snapshots at times t = 10, 40, and 160 MCS (from left to right) illustrating the evolution of strategy
distribution on a 80 × 80 box of a larger system for S = 0.4 and T = 1.4.

Finally we mention that the latter additional options result in a similar domain growing process in the
stag hunt region, too, if S − T + 1 = 0. These ordering processes will be discussed later when studying
25

the consequences of a more general class of stochastic evolutionary rules. Finally we mention that similar
phenomena occur on bipartite networks.
5. EVOLUTIONARY POTENTIAL GAMES
Evolutionary games are devoted to explore the consequences of different evolutionary rules defining the
ways how individuals can modify their own strategies in order to have a higher payoff. The first efforts were
mainly focused on the maintenance of cooperative behavior in the social dilemmas where the results strongly
depend on the set of strategies, the connectivity structure of players, and the dynamical rules that may
involve variations in all ingredients of the mathematical models (including the current strategy, interaction
or learning networks, dynamical rules, personal features, and their combinations). As mentioned in the
Introduction the concept of evolutionary games was originally suggested and applied by Maynard Smith
and Price [11], Maynard Smith [3], Axelrod and Hamilton [15], Axelrod [16], Hofbauer and Sigmund [4] to
provide a mathematical background for the description of the Darwinian evolution for biological and social
systems. This is the reason why most of the investigations during the last decades used dynamical rules
based on the adoption/imitation of the more successful strategy (or biological species). As a result different
dynamical rules are introduced and studied systematically for a wide scale of conditions [for a survey see
[8, 22, 98]].
For example, in lattice systems the ”imitating the best” rule [20] dictates the deterministic adoption
of that player’s strategy who received the higher payoff in the neighborhood; the ”imitating the better”
rules allow to adopt any better strategy from the local neighborhood with a probability dependent on the
neighbors’s payoff [99, 18]. Besides it there are other imitation rules [introduced and studied e.g., by Nowak
et al. [80]; Szabó and Tőke [100]; Alonso-Sanz et al. [101]; Masuda and Aihara [84]; Ohtsuki and Nowak
[102], Wild et al. [103]; Wu et al. [104]; and many others] when the players can adopt the strategy even from
a worse neighbor though the more successful strategies continue to be preferred.
For all types of imitation rules the system has absorbing states because this rule cannot recreate a
strategy that has become extinct previously. For example, if one of the homogeneous states is approached
then the system remains there forever. On the contrary, the introduction of mutation [see [105], [106], and
[107]] is capable of reviving strategies that have vanished previously.
For the rules based on fictitious game (as detailed in the Section 4.1) each player is capable of determining
her own payoff for her strategies with an assumption that their co-player will not change their strategies. For
the ”best response” version of these rules the player chooses those strategies that provide the highest payoff
under the mentioned conditions. If more than one ”best response” exists, then the player selects one of them
at random. The smoothed versions of this rule allow the player to select all her possible strategies with a
probability dependent on the payoff variation. The concept of potential games becomes fruitful for those
special versions of these dynamical rules which drive the system into the so-called Gibbs state characterized
by the Boltzmann distribution [for an English translation of Boltzmann’s original work see [108]]. For these
special cases we can utilize the enormous amount of results obtained in statistical and solid state physics to
explain phenomena emerging in social and biological systems, too.
Evidently, the latter evolutionary processes based on fictitious games are relevant in human systems.
Similar situations can occur in biological systems if the species creates a large number of mutants with a
survival probability dependent on the neighborhood. We have to emphasize, however, that the quantitative
analysis of the social and biological systems requires relevant extensions of the possible rules opening new
challenges for both the non-equilibrium statistical physics and super-statistics.
5.1. Evolutionary rules leading to Boltzmann distribution
In the field of game theory Blume [28] described first that for the application of the so-called loglinear or logit evolutionary rules the potential games evolve into the Gibbs state assuring the validity of
the direct application of the concepts and tools of equilibrium statistical physics. The basic idea, as an
efficient Monte Carlo algorithm to determine average values for the Boltzmann distribution in many particle
system, however, was developed by a group conducted by Metropolis at Los Alamos in the 1950s. They
26

recognized that instead of evaluating the Boltzmann factor for a randomly chosen microscopic state it is
more efficient to use a Markov chain algorithm in which a state will be chosen with a probability defined by
the Boltzmann distribution. Nowadays this method is named importance sampling. A similar evolutionary
rule was suggested by Glauber [109] who wished to study time-dependent processes for the Ising model
whose dynamics is not prescribed by the quantum mechanics. Since that time several other algorithms
were suggested and used widely for the investigation of equilibrium and non-equilibrium phenomena in
many-particle systems.
Now we describe the above-mentioned rules in historical order by using the terminology of evolutionary
game theory. The system is started from an arbitrary (typically random) initial state and during the
evolution the following elementary steps are repeated. A randomly chosen player x can modify her strategy
sx to s′x chosen at random from her options with a probability w(sx → s′x ) dependent on the payoff variation
∆u = ux (s′x , s−x ) − ux (sx , s−x ) = V (s′x , s−x ) − V (sx , s−x ).
For the Metropolis algorithm the player always adopts the new strategy s′x if it is worthy (∆u > 0). For
the opposite cases the player accepts the strategy s′x with a probability decreasing exponentially with the
possible loss, that is,

1 for ∆u ≥ 0 ,
(M)
′
w (sx → sx ) =
(69)
e∆u/K for ∆u < 0
where K denotes the magnitude of noise (or temperature in physical systems). Notice that this rule agrees
with those we used in Sec. 4.1 if K → 0.
For the Glauber dynamics
1
.
(70)
w(G) (s → s′x ) =
1 + e−∆u/K
This evolutionary rule is convenient for the analytical calculation as demonstrated in [22].
The transition rate for the logit rule [28, 110] is defined as
w

(log)

′
eu(sx ,s−x )/K
′
(sx → sx ) = λx P
′′
eu(sx ,s−x )/K
s′′
x

.

(71)

where the summation runs over all the possible strategies of the player x and 0 < λx ≤ 1. The choice of
λx = 1 provides the most efficient algorithm in the Monte Carlo simulations.
The most relevant common feature of the above dynamical rules is that they all drive the potential games
into the Gibbs state where the probability p(s) of a strategy profile s is given by the Boltzmann distribution
as
1
p(s) = eU(s)/K
(72)
Z
where
X
Z=
eU(s)/K .
(73)
s

The normalization factor Z is called the partition function and plays a crucial role in statistical physics
because the partial derivatives of ln (Z) reproduce relevant thermodynamical quantities. For example, the
average value of the potential can be given as
U=

∂ ln (Z)
.
∂(1/K)

(74)

The relevance of these features is enhanced by the exact solutions obtained by Eggarter [111], Baxter
[112], Yang [113] for several connectivity structures.
In addition, the conditions of detailed balance are also satisfied between all the possible forward-backward
transition pairs. As a result, for the Boltzmann distribution the transition sx → s′x and its backward version
(s′x → sx ) appear with the same frequency, i.e.,
′

w(sx → s′x , s−x )eU(s)/K = w(s′x → sx , s−x )eU(s )/K
27

(75)

for ∀ x, ∀ sx , s′x , and ∀ s−x . These conditions are satisfied if
′
w(sx → s′x , s−x )
= e[U(s )−U(s)]/K .
w(s′x → sx , s−x )

(76)

Due to this relationship the final stationary state (the Boltzmann distribution) and also the satisfaction of
detailed balance remain unchanged if the transition rates w(sx → s′x ) and w(s′x → sx ) are multiplied by the
same coefficient that can be varied from pair to pair of strategy profiles involved [see λx in Eq. (71)].
For all the above dynamical rules only one player has modified her strategy in the consecutive elementary
steps. For the Kawasaki dynamics [114] a randomly chosen player x exchanges strategy with one of her
neighbors with a probability dependent on their summarized payoff variation that is not affected by the
interaction between them. The payoff variation arising from the rest of interactions can be built up from
two consecutive individual strategy changes as before. Consequently, the summarized payoff variation is
identical to the potential variation ∆U = U (sx , sy , s−x,y ) − U (sy , sx , s−x,y ) and the transition rate can be
given by the following expression:
1
(77)
w(K) (s → s′x ) =
1 + e−∆U/K
used in many solid state applications when studying diffusion or transport in systems where the number of
particles (strategies) is conserved. For the two-strategy systems the corresponding dynamical graph is given
by the nodes of an N -dimensional hypercube and the edges are defined by those diagonals of faces where
two neighboring players exchange their different strategies with each other.
5.2. Statistical physics and thermodynamics
For the microscopic description of a multi-agent system we should define the individual strategy for all
participants, which requires a huge amount of data. At the same time, for the macroscopic description
of the same system we use only a few parameters, e.g. average portion of a strategy, average payoff and
noise level, as it happens in the thermodynamic description of a gas when using the concept of pressure,
temperature, and density, without any knowledge about the position and velocity of atoms contained in the
gas. Statistical physics gives a general framework to describe the relationships between the macroscopic
(thermodynamic) quantities that are influenced by the microscopic interactions.
The fundamental assumption of the equal a priori probability of the accessible microscopic states serves
a basis for the statistical description. According to this approach, those macroscopic states can be observed
in the stationary state that are realized by the largest number of microscopic states. Due to the law of
large numbers the latter approach defines well the macroscopic state in the limit N → ∞ as detailed in the
textbooks of statistical physics [see e.g. [115, 116]] based on early works by Boltzmann [117], Gibbs [118]
and Szilárd [119].
Now we briefly survey the relevant mathematical background following a modern formalism suggested
by Jaynes [120] and using the terminology of evolutionary game theory [28, 121, 122] as before. Within this
framework the system is described by the p(s) probability distribution of the microscopic states s and the
problem of prediction becomes equivalent to the maximization of Shannon entropy [123]
X
S =−
p(s) ln p(s)
(78)
s

under several constraints. The crucial problem of extending the maximum entropy principle to non-physical
systems lies in the adequate choice of constraints. This approach is used successfully in the analysis of
complex [124] and chaotic systems.
In the present case p(s) is normalized, that is,
X
p(s) = 1
(79)
s

28

and we can fix the average value of the potential as
X
p(s)U (s) = U .

(80)

s

Using the standard method the extremum under the above constraints can be evaluated by solving the
following set of equations:
"
#
X
X
∂
S + λ1
p(s) + λ2
p(s)U (s) = 0
(81)
∂p(s)
s
s
where the Lagrange multipliers λ1 and λ2 are determined by taking into consideration the conditions (79)
and (80). Straightforward calculations yield that the optimal probability distribution becomes equivalent to
the Boltzmann distribution for λ2 = 1/K [see (72) and (73)] and for a suitable choice of the average value
of the potential (U) depending on K (strictly) monotonously.
In the real utilization of the above extremum principle, it is more convenient to perform a Legendre
transform [125, 126, 127]. Using the analogy of the Helmholtz free energy in thermodynamics, we introduce
now a thermodynamic potential
Φ = U + KS
(82)

that has a maximum in the equilibrium state for a fixed K characterizing the temperature in statistical
mechanics or noise level in evolutionary potential games in the sense defined by the logit dynamical rules
[see e.g., (71)].
Notice that for spatial systems with short range interactions both the entropy S and the average value
of potential (as well as Φ) are proportional to the system size N and are considered as extensive quantities
in the thermodynamical descriptions.
Counterexamples are systems with long-range interactions or systems on some types of small-world
networks where we cannot apply the traditional methods directly. In the wide field of statistical physics
there are some new directions and approaches to describe the macroscopic behavior of the mentioned systems
when considering complex [124], or other dynamical systems [128, 129], and those non-equilibrium systems
that behave like the superpositions of the Boltzmann distributions [130, 131]. Surveying the latter directions
goes beyond the scope of the present work, our attention will be focused on the description of phenomena
occurring in large spatial systems.
In the following sections we will draw a parallel between the kinetic Ising/Potts models and social systems
for a particular evolutionary rule. In fact, for both types of these systems the applicability of thermodynamics
is limited to the thermostatics. According to quantum mechanics each microscopic state of the Ising type
systems is an eigenstate and remains unchanged forever. The time-dependence in the kinetic Ising model
is introduced by assuming a uniform interaction between the spins and a heat reservoir characterized by
the temperature K. Under these conditions the total energy of the Ising system fluctuates and the first
and second laws of thermodynamics become meaningless. The failure of the third law of thermodynamics
is related to the high degeneracy of the ground state as discussed later for several cases.
In social and biological systems the application of a similar stochastic evolutionary rule is justified by
its mathematical simplicity and the analogies we can exploit in the interpretation of the phenomena. In
these systems the value of K can characterize: (i) the fluctuation of payoffs; (ii) the errors made by players
during their decision process; and (iii) the magnitude of risk the player accepts in the hope of finding a
better (long-term) solution. In social systems the value of K can be even considered as a personal feature
and also the subject of the coevolutionary process. The first simulations in such coevolutionary models have
indicated the homogenization of K for the coexistence of strategies within the prisoners dilemma region if
both the strategy and K adoption are controlled by pairwise imitation rule [132]. Similar results for Glauber
type rules would increase the relevance of thermostatics for these systems.
5.3. Consequences of the extremum principles
The principle of the maximum entropy serves as a mathematical background describing the intimate
relationship between statistical mechanics/physics and thermodynamics. This principle explains the laws
29

of thermodynamics as well as the relevance of the Boltzmann distribution and connects the meaning of the
Lagrange multipliers and the intensive quantities of thermodynamics. The Boltzmann distribution itself
implies several general relationships among the first and second partial derivatives of the thermodynamic
potentials [125, 133, 134] or the partition function as illustrated by Eq. (74). Examples are the Gibbs-Duhem
relations and the Gibbs’ phase rule. This knowledge is summarized in equation of states quantifying the
relations among the intensive and extensive thermodynamical quantities for macroscopic systems composed
of different atoms, ions, and molecules.
The simplicity of the linear response theory and the fluctuation-dissipation theorem are also direct
consequences of the Boltzmann distribution [135] where the effect of a small perturbation obeys a simple
expression in linear approximation.
In addition to the general thermodynamical relationships, the extremum principles can also be used
to evaluate the thermodynamical quantities in the knowledge of the microscopic interactions. We briefly
survey now the essence of the cluster variation methods providing a general framework for the traditional
mean-field and pair approximations in the approximative description of the lattice systems. For the sake of
simplicity our description is focused on systems with interactions between the equivalent neighboring players
located on the sites of a lattice. Within this approach the translation invariant microscopic states can be
described by configuration probabilities on a small cluster of neighboring sites. For example, p1 (s1 ) defines
the probability of the strategy s1 at each site of the lattice while p2 (s1 , s2 ) describes the probability of finding
s1 and s2 strategies on two neighboring sites. For rotational invariant arrangement of strategies (e.g., on
square lattices where the horizontal or vertical directions are equivalent) we can assume that p2 (s1 , s2 ) is
independent of both the position and direction of the pair. These quantities are normalized, that is,
X
p1 (s1 ) = 1 ,
s1

X

p2 (s1 , s2 ) = 1 ,

(83)

s1 ,s2

and satisfy the compatibility conditions:
X
X
p2 (s2 , s1 ) = p1 (s1 ) .
p2 (s1 , s2 ) =
s2

(84)

s2

Evidently, one can use larger clusters of n sites to describe the stationary state in this system and the
corresponding quantities satisfy similar compatibility conditions. The larger the cluster we study, the more
accurate is the approximate solution [136, 137].
With the application of Bayes’ theorem we can build up the configuration probabilities for a large cluster
as a product of configuration probabilities of smaller clusters as detailed in the paper by Gutowitz et al.
[138]. This approach allows us to derive adequate approximations for some other quantities, e.g., correlation
function and correlation length [22]. Furthermore, the application of Bayes’ theorem plays a fundamental
role within the dynamical cluster techniques (developed to study stationary states in non-equilibrium lattice
systems) when a set of coupled differential equations is derived by taking into consideration the contribution
of all the elementary steps [139]. In comparison to the dynamical cluster techniques the so-called cluster
variation method provides a more convenient way to evaluate the configuration probabilities. With the use
of these quantities one can express both the entropy and the average value of the potential for a given lattice
structure. For example, on a d-dimensional cubic lattice the value of U is expressed as
X
(85)
Vs1 s2 p2 (s1 , s2 ) ,
U = Nd
s1 ,s2

while the entropy can be approximated at the level of pair approximation [140, 141] as
X
X
S ≃ S (2p) = −N d
p1 (s1 ) ln p1 (s1 ) .
p2 (s1 , s2 ) ln p2 (s1 , s2 ) + N (2d − 1)
s1

s1 ,s2

30

(86)

When using larger cluster sizes one can give better approximations for the entropy [142, 143], while expression (85) remains unchanged for the case of pair interactions. For the cluster variation methods the
thermodynamic potential [e.g., Φ as defined by (82)] is expressed as a function of configuration probabilities and its maximum value is determined by varying these parameters. The standard calculation may be
simplified by considering only the independent parameters of the configuration probabilities. For example,
if only two strategies are allowed, s1 , s2 = 1, 2, then the one- and two-site configuration probabilities can be
expressed with only two parameters as
p1 (1) = c ,
p1 (2) = 1 − c ,
p2 (1, 1) = q ,
p2 (1, 2) = c − q ,
p2 (2, 1) = c − q ,

(87)

p2 (2, 2) = 1 − 2c + q

where c can be interpreted as the portion (or density) of strategy 1 in the whole system and c − q describes
the density of domain walls separating homogeneous territories. In that case the equilibrium values of c and
q are given by the solution of the following equations:

and

∂Φ(c, q)
= 0,
∂c

(88)

∂Φ(c, q)
= 0,
∂q

(89)

where Φ(c, q) = U(c, q) + KS(c, q) is obtained by substituting Eqs. (87) into (86) and (85). In general,
Eqs. (88) and (89) have more than one possible solutions (0 ≤ p2 (s2 , s2 ) ≤ 1). In the latter case the real
solution is the one where Φ(c, q) reaches its maximum.
Thus the cluster variation method gives us a unique way to evaluate the equilibrium value of c and q
together with all the related quantities as a function of K. Besides it, one can derive approximate phase
diagrams if the actual model has several solutions with different symmetries, as it happens frequently in solid
state systems [examples and further references are given in [144, 145]]. In evolutionary games on lattices
the average total payoff can be given as
X
(90)
As1 s2 p2 (s1 , s2 ) ,
A = Nd
s1 ,s2

in the knowledge of the payoff matrix A and the nearest neighbor strategy configuration probabilities. Apart
from the symmetric case A = AT , the quantity A has no analogous concept in solid state physics because
it may contain terms neglected in the evaluation of the pair potential V. At the same time, this quantity
plays a key role in the investigation of social dilemmas.
It is worth mentioning that the cluster variation method at the level of pair approximation reproduces
the exact result for the one-dimensional systems with nearest neighbor interactions. For these systems the
probability distribution of strategies can be given by the Bayesian formula as
p(s) = p2 (s1 , s2 )

x=N
Y−1

p2 (sx , sx+1 )
,
p1 (sx )
s ,x=2

(91)

x

that satisfies the compatibility conditions, that is, any pair configuration probability can be reproduced by
summing over the rest of sites, and the resultant entropy becomes equivalent to (86) for d = 1 in the limit
N → ∞.
31

Equations from (83) to (91) give a mathematical basis for the use of the cluster variation method at the
level of two-site approximations. This calculation becomes simpler at the level of one-site approximation
(that is equivalent to the traditional mean-field approximation), when we have only one parameter (c) to
be determined according to (88). The corresponding expressions for U and S can be derived with the
assumption p2 (s1 , s2 ) = p1 (s1 )p1 (s2 ) that simplifies the entropy as
X
p1 (s1 ) ln p1 (s1 ) .
(92)
S ≃ S (1p) = −N
s1

It is emphasized that the one-site approximation ignores the role of the topological features of the connectivity structure. More precisely, only the number of co-players is involved in U. This approach may give an
adequate description of phenomena for those (homogeneous) connectivity structures where the number of
neighbors is large enough. For the square lattice the results of the one- and two-site approximations will be
contrasted with Onsager’s exact result in the following section.
The generalization of the cluster variation method for larger number of strategies and/or for larger size of
clusters is straightforward. When increasing these parameters one can study a rich variety of sophisticated
phenomena although the calculations become more complex and time-consuming. At the same time we
can reduce the number of independent parameters by taking into consideration the additional symmetries.
From this point of view the use of the corresponding three- and four-site approximations is advantageous
on triangular and square lattices.
Finally we mention that the pair approximation can be applied successfully on Bethe lattices where this
approach gives a more accurate prediction as illustrated by Vukov et al. [86] who compared the analytical
approximate results with Monte Carlo simulations performed on a locally similar random regular graph for
large sizes.
In the above description we have assumed the equivalence between both the players and their location.
There exist, however, several spatial structures (e.g. non-Bravais lattices) or games (e.g., matching pennies)
where we should distinguish the sites and/or players. The cluster variation method may be extended to
these cases by introducing the configuration probabilities on several types of one-, two-, or n-site clusters
by considering also the sublattice structure.
6. ISING MODELS
The investigation and application of the Ising type models have a long history as surveyed by Brush
[146], Niss [147, 148, 149], Sornette [150]. The original idea was first described by Lenz [151] as a simple
model to study the ferromagnetism. The one-dimensional version of this lattice model was studied by Ising
[152], who was the PhD student of Lenz. Unfortunately, the one-dimensional model is not suitable to describe
the ferromagnetic-paramagnetic transition observed in magnetic material when increasing the temperature
[153, 154] because the domain walls, that can be considered as point defects in the one-dimensional systems,
prevent the formation of long range order [115].
The existence of the phase transition was shown by Peierls [155] using an argument later improved
by Griffiths [156]. The approximate methods (like mean-field approximation [157] and pair approximation
[140]) have confirmed the presence of a continuous phase transition. The exact solution in the absence of
external magnetic field on the square lattice with nearest neighbor interactions was obtained by Onsager
[158]. In the following decades this magnetic model was extensively investigated on different lattice structures
assuming ferromagnetic or anti-ferromagnetic interactions. Due to its simplicity and the knowledge of the
exact solution the model was frequently used to check the accuracy of different approximation techniques
[159]. Since that time the Ising models have been fundamental mathematical models in statistical physics
representing a robust universality class of critical phase transitions [116, 160, 161, 162].
The original Ising model can be directly applied to explain the magnetic behavior only for a few materials.
On the other hand, the equivalent lattice gas models are widely used to derive theoretical phase diagrams for
alloys [163], metal-hydrogen systems [164], solid electrolytes [165], intercalation [166] or non-stoichiometric
compounds [167], etc. The analogy to the Ising models is due to the fact that in all these models only two
32

states of the lattice sites are distinguished. For example, in the Cu-Au alloys either Cu or Au atoms can be
at one site x; in the palladium-hydrogen systems an interstitial void x of the metal matrix can be empty or
occupied by a H atom; in the superionic conductor AgI, iodide ions form a rigid body-centered cubic lattice
and the smaller mobile silver ions can be present or missing in a tetrahedral void represented by the site x.
The total energy of these systems can be built up from pair interactions between the neighboring sites in
the knowledge of the physical properties.
The flexible interpretation of the Ising model implies its applicability to many other systems involving
high-energy physics [for a survey see the review by Pelissetto and Vicari [168]] and social models with
players located on a network [169, 170]. The latter situation occurs when the connected individuals can
choose between two options, e.g., using meter or yard as unit of length; following drive left or drive right
rule in traffic; using Windows or Linux operating systems, etc. All these examples represent the so-called
coordination game and are analogous to ferromagnetic systems [169, 171, 172, 173, 174, 175, 176].
6.1. Systems equivalent to Ising models
In the magnetic Ising model the spin variables σx = +1, −1 refer to upward and downward magnetic
moments at site x of a network. The strength of the spin-spin interaction between the neighboring sites x
and y is denoted by Jxy and we can assume the presence of a site-dependent external magnetic field hx . For
any microscopic state σ = (σ1 , . . . , σN ) the Hamiltonian (or potential energy) function of this multi-spin
system is given as
X
X
Jxy σx σy −
hx σx
(93)
H(σ) = −
x

hx,yi

where the summation runs over all nearest neighbor pairs (denoted by hx, yi as it is done for the multi-player
games). For ferromagnetic interactions the so-called coupling constants are positive (Jxy > 0) and the system
achieves one of the ordered ground states with minimal energy in the ferromagnetic phase (σx = +1 at each
site if hx > 0 or σx = −1 if hx < 0. A similar optimal strategy distribution occurs in a multi-agent system
with coordination type pair interactions if one of the two strategies is preferred by suitable self-dependent
payoffs.
In order to clarify the relationship between the Ising models and the multi-agent, two-strategy, potential
games first the site energies are shared among the pair interactions as
X
hx =
h′x (y ′ ),
(94)
y′

where the summation runs over y ′ which are the interacting neighbors of x. In that case the Hamiltonian is
composed of pair interactions involving the corresponding contributions of the site energies from both sites
in the following way
X
Hxy (σx , σy )
(95)
H(σ) =
hx,yi

where
Hxy (σx , σy ) = −Jxy σx σy − h′x (y)σx − h′y (x)σy

(96)

that may also be written as
Hxy (σx , σy ) = −Jxy σx σy −

h′x (y) + h′y (x)
h′x (y) − h′y (x)
(σx + σy ) −
(σx − σy ).
2
2

(97)

The latter form of the pair interactions is convenient for the comparison with the potential of a nonsymmetric
2 × 2 game given by Eq. (64) because the first term is analogous to the coordination type interaction as the
four possible values of the product σx σy define a matrix equivalent to f (4). Similarly, in matrix notation
the second (third) term of (97) becomes equivalent to the second (third) term of the expression (64) with
a suitable choice of the coefficients. Using this analogy a multi-agent, two-strategy, potential game can
be mapped onto an Ising model on the same network with an adequate choice of the parameters Jxy and
33

h′x (x′ ) whereas the local site energy is defined by (94). More than one game can be mapped onto the same
generalized Ising model by varying the game parameters under the conditions of (94).
In a human system it is natural to assume distinct payoffs for each pair, therefore in the corresponding
Ising models both the coupling constants Jxy and the local magnetic fields hx can be considered as random
parameters. The resulting random Ising models or spin glasses will be discussed briefly in Sec. 7.10.
The traditional Ising model was introduced to study solid state phenomena where the interacting particles
are identical and the applied magnetic field is homogeneous, consequently Jxy = J and hx = h, and the
connectivity network is a translation invariant lattice where each site has z neighbors. Similar conditions can
be satisfied for multi-agent evolutionary games with equivalent interactions between the players residing on
the sites of the same lattice. In that case the local site energy is shared equally among the z pair interactions
becoming
h
(98)
Hxy (σx , σy ) = −Jσx σy − (σx + σy ).
z
For the quantitative relationship now we compare −Hxy with the pair potential (62) obtained in the notation
(59) of social dilemmas. Drawing a parallel between these two systems, the σx = +1 (σx = −1) spin state
corresponds to the strategy sx = D (sx = C). For this convention one can deduce the following relationship
between the parameters of the Ising model and social systems:
J=

1−T −S
4

and

h
T −1−S
=
,
z
4

(99)

that is, the Ising type spin-spin interaction is analogous to the coordination game whereas the magnetic
field plays the role of the driving force validating the risk dominance.
These linear relations determine the values of J and h as a function of the payoff parameters T and S.
Figure 16 shows the orthogonal Descartes coordinate axes for the h/z and J (denoted by red dashed and
blue dotted lines) on the S − T plane we used in Sect. 3.3 for the classification of games according to the
flow graphs and Nash equilibria. Now the S − T (or h − J) plane is divided into three regions with respect
S

-J

-h/z

1

0

-1
0

1

2

T

Figure 16: (Color online) Mapping the Ising parameters J and h onto the S − T plane of payoffs in the notation of social
dilemmas defined by Eq. (59).

to the thermodynamically stable states of the Ising model in the low noise limit. Within the white territory
a ferromagnetic, i.e., homogeneous spin down (σx = −1), is stabilized that refers to uniform cooperation
in games (where T < 1 and S > T − 1) involving the harmony games and the upper half of the stag hunt
games. The opposite ferromagnetic state (σx = +1 or sx = D) occurs within the dark region (S < 0 and
T > S + 1) representing the second half of the stag-hunt games and the prisoner’s dilemmas.
Within the third region (T > 1 and S > 0) an anti-ferromagnetic spin arrangement is realized when
the neighboring spins point to opposite directions. On the square lattice the up and down spins form a
34

chessboard like pattern which we used in Fig. 16 for the illustration of this spatial structure. This antiferromagnetic spin arrangement is twofold degenerated as the simultaneous reversal of all spins does not
affect the total energy (93) even in the presence of h. On the other hand, the application of a magnetic field
h influences the local stability of spin states and this is the reason why a ferromagnetic phase is stabilized
if |h| exceeds a threshold value when J < 0, as it is also discussed for games [79]. These thermodynamically
stable (ordered) states are realized by the logit rules in the limit K → 0 and coincide with the preferred
pure Nash equilibria determined by the strategy pair (i, j) for which Vij is maximal.
In the present system the highest average (total) income can be achieved by uniform cooperation if
2R > T + S, otherwise the sublattice ordered arrangement of the C and D strategies provides the highest
total payoff. Despite this total payoff optimum the system falls into the state of ”tragedy of the community”
within the dark territory indicated in Fig. 16. In the zero noise limit the latter structure occurs for h < 0,
except the sublattice ordered region where the sufficiently strong repulsive interactions prevent the formation
of a homogeneous state. In some sense the negative magnetic field can be interpreted as a force driving the
social system into the state of the tragedy of the community.
Notice furthermore that the case of J = (1−S −T )/4 = 0 refers to the absence of interactions between the
neighboring spins. In such situations the independent spin reversals are controlled only by the magnetic field
h and the system is equivalent to the collection of non-interacting spins that can be described analytically
when considering only a single spin. The corresponding games are called ”equal-gains-from-switching” [177]
or ”dummy” games [45] in the literature. The donation game [9] represents one of the well investigated
examples.
The analytical study of the anti-ferromagnetic spin arrangements requires the division of the lattice into
two sublattices (x ∈ X and y ∈ Y ) in a way discussed in Sec. 4. Additionally, the concept of the Ising
model was extended by introducing staggered magnetic fields that are uniform within a sublattice. Thus,
hx = h + hs and hy = h − hs where hs defines the strength of the staggered magnetic fields. Now the pair
interaction
hs
h
(100)
Hxy (σx , σy ) = −Jσx σy − (σx + σy ) − (σx − σy ).
z
z
has a third term quantifying the effect of the staggered magnetic field that favors one of the sublattice
ordered spin arrangements. The Ising model with staggered magnetic field is equivalent to an evolutionary
potential game on the same bipartite network. Comparison of the matrix notation of Eq. (100) with the
2 × 2 potential matrix (64) explains that the staggered magnetic field
hs
= α′ (7),
z

(101)

where z denotes the number of neighbors in the translation invariant connectivity structure.
The introduction and application of the staggered magnetic field have no practical importance in the
investigation of the magnetic materials. This quantity becomes relevant from theoretical point of view when
justifying the equivalence of order-disorder transitions observed for the ferromagnetic and anti-ferromagnetic
Ising models when varying the temperature. To be more precise, the effect of hs on the ferromagnetic state
(J > 0 and h = 0) is equivalent to the effect of h on the anti-ferromagnetic state.
Finally we mention that the sublattice-dependent local site energy plays an important role in those lattice
gas models where two types of sites are distinguished. For example, in the crystals of Pd-H system [164],
CaF2 [165], and alkali-fullerides [145] the mobile atoms/ions can stay both in the tetrahedral and octahedral
sites of the face-centered cubic lattice formed by the rigid components.
6.2. Potts models
The two-state Ising model without magnetic field was extended by Potts [178] who introduced a lattice
model with n (n ≥ 3) equivalent states at each site. Previously Ashkin and Teller [179] studied a particular
four-component version of the Ising model on a square lattice. The lattice model with n states for a common
interaction energy between the different local states was also suggested by Kihara et al. [180]. The name of
Potts model was proposed by Domb [181] and used worldwide since that time. For a comprehensive survey
of the early results we can suggest consulting the review by Wu [182].
35

In the terminology of game theory the Potts models correspond to multi-agent games with symmetric
n-strategy pair interactions where the payoff matrix and potential are given by n × n unit matrices, that is,
both the payoffs and potential matrices V can be expressed by Kronecker’s delta as
Aij = Bij = Vij (x, y) = Jδij ,

(102)

where i, j = 1, . . . , n. For J > 0 this pair interaction is equivalent to a generalized coordination game with
n equivalent Nash equilibria when the players choose the same option. This game involves all the d(p, q)
[1 ≤ p < q ≤ n; see Eq. (41)] coordination type interactions with the same strength.
In the literature of physics the Potts model is extended by introducing an external magnetic field (h > 0)
or a self-dependent component preferring one of the strategies. The presence of this term suppresses the
critical transition in a way as it occurs in the Ising model.
The main features of the corresponding ferromagnetic Potts model are well described in the field of
statistical physics. This set of models is used for the classification of the universal behaviors appearing in the
order-disorder transitions when the temperature (noise) is increased. Due to its simplicity the investigation
of the Potts model played an important role in the exploration of the critical phase transitions and it became
a key model when testing different methods and approaches. It turned out that the critical behavior of the
Potts model is richer and more general than that of the Ising model.
Originally the Potts model was considered as the simplest mathematical model exhibiting an orderdisorder phase transition for n > 2 while its kinetic versions allow the investigations of the time-dependent
ordering processes. In the light of the robustness and universality of critical phase transitions it was later
realized that in many substances the phase transitions can be interpreted by the application of various
Potts models. For example, three-fold degenerated ordered structures can be formed by atoms adsorbed on
single crystal surfaces (for 1/3 coverage) [183, 184] or by mobile ions in layered solid electrolytes (e.g. silver
β-alumina) [185]. A large variety of the experimental realizations of the two-dimensional, n = 4 Potts model
was discussed by Domany et al. [186].
In Sect. 7.8 we will discuss briefly a lattice gas model for illustrating the emergence of equivalent ordered
structures on a square lattice. The general and universal properties of the order-disorder phase transitions
for the n-state Potts model will be detailed in Sec. 7.4 while the most relevant features of the ordering
process are surveyed briefly in Sec. 8.
7. FEATURES OF ISING MODELS
Despite its simplicity the Ising model can be used to demonstrate a surprisingly wide range of phenomena
including different types of ordered structures in the stationary state when varying the range and strength
of interactions on lattices or graphs. Besides it, the kinetic Ising model is capable of illustrating a large
number of dynamical processes how they evolve towards the final stationary state. Now we briefly survey
the most relevant phenomena that can help us understand the behavior of the more general evolutionary
games on graphs.
7.1. Spontaneous symmetry breaking
In the absence of a magnetic field h the ferromagnetic Ising model with nearest neighbor interactions
on the square or cubic lattices has two equivalent ordered states that appear with the same probability
according to the Boltzmann distribution (72). Similarly, the Boltzmann distribution predicts the presence
of the two equivalent anti-ferromagnetic ordered structures with the same probability even in the presence
of a magnetic field if its strength does not exceed a threshold value. On the contrary, in the practice we see
only one of the ordered structures in sufficiently large systems.
To resolve the above discrepancy Fig. 17 shows a typical time-dependence of the frequency of C strategy
as a function of time in one of the two sublattices of a small square lattice for the hawk-dove region at a
low noise level when the sublattice ordered strategy arrangements are favored. Figure 17 illustrates that
the system alternates between two ”ordered” states and the transition time is significantly shorter than
the average residence time (tr ) the system stays in the vicinity of one of the ordered states. The value
36

1

ρC,X(t)

0.8
0.6
0.4
0.2
0

0

40000

80000 120000 160000 200000

time [MCS]
Figure 17: Time-dependence of the C strategy frequency in the sublattice X for the hawk-dove game on square lattice with
nearest neighbor interactions. The fluctuations are smoothed by averaging over 100 MCS. The Monte Carlo simulation is
performed for T = 1.5, R = 1, S = 0.5, P = 0, K = 0.5, and L = 10.

tr [MCS]

of the average residence time can be estimated by counting the state reversals during a sufficiently long
Monte Carlo simulation that gives tav ≃ 3 × 104 MCS for the parameters used for results plotted in Fig. 17.
Figure 18 shows that tav increases exponentially with the linear size for the values of payoffs and noise level
given in the caption of Fig. 17. Consequently, for sufficiently large sizes we may find the system staying in
one of the macroscopic states during the whole sampling time that may exceed many years or even the age
of the Universe. The selection of one of the ”stationary” states depends on the initial conditions and the
sequence of random numbers used in the simulation. Although the average residence time depends on other
10

8

10

7

10

6

10

5

10

4

10

3

10

2

0

5

10

15

20

L
Figure 18: MC data for the size dependence of the average reversal time obtained on a square lattice for T = 1.5, R = 1,
S = 0.5, P = 0, and K = 0.5.

parameters (payoffs and noise) the spontaneous symmetry breaking described above remains valid for other
values as well as for many other systems in the limit N → ∞. This feature is contrary to the prediction of
the Boltzmann distribution suggesting the presence of both types of ordered microscopic states with equal
probability. In other words, the infinite system is nonergodic because the time and ensemble averages would
give different results below the critical transition point for h = 0. An identical behavior occurs for the
anti-ferromagnetic lattice models (for hs = 0) as well as for the Potts models. This feature has rigorously
been studied for a long time in the theory of stochastic phenomena [187].
It is emphasized that the above mentioned discrepancy vanishes if the equivalence of the ordered struc37

tures is broken by applying h 6= 0 for the ferromagnetic Ising models. In that case it is convenient to consider
the zero-field magnetization as an average value in the limit h → +0. A similar trick can be applied for the
anti-ferromagnetic Ising model (hs → +0) and also for the Potts models.
7.2. Mean-field theory
In most of the cases the mean-field theory gives an adequate qualitative prediction about the system
behavior. Bragg and Williams [157] suggested expressing the contribution of interactions via the introduction
of an effective magnetic field hef f characteristic to the average magnetization (m = hσx i) in translation
invariant systems. For a d-dimensional hyper-cubic lattice
hef f = zJm

(103)

where z = 2d is the number of interacting neighbors.
In the presence of a magnetic field h + hef f the average magnetization for a single spin is determined by
the Boltzmann distribution as
m = tanh [(h + hef f )/K] = tanh [(h + 2dJm)/K] .

(104)

1

1

0.5

0.5

0

0

m

m

This implicit equation has a trivial solution m = 0 if h = 0. This (paramagnetic) solution is the only solution
above a critical noise level (K > Kc = 2dJ). In the opposite cases (K < Kc ) two additional equivalent
(symmetric) solutions are found as illustrated on the left plot of Fig. 19. Both solutions tend towards a

-0.5
-1

-0.5

0

0.5

-1

1

K/2dJ

0

0.5

1

K/2dJ

Figure 19: (Color online) Prediction of mean-field theory for the magnetization m vs. K/2dJ for the Ising model at h = 0
(left) and h = 0.01 (right). Solid (dashed) lines denote attractor (repellor) solutions. Colored regions refer to three basins of
attraction.

homogeneous state (m(K) = ±1) and m2 (K) vanishes linearly when K → Kc from below. More precisely,
m(K) ≃

3(Kc − K) 1/2
Kc

(105)

in the close vicinity of Kc .
In the presence of an external magnetic field (h > 0) the typical solutions are illustrated in the right plot
of Fig. 19. Notice that Eq. (104) has also three solutions at low values for K while in the opposite limit the
solution becomes unique. Contrary to the zero-field case now there is a solution that varies smoothly when
K is increased from zero to ∞.
It is emphasized that the thermodynamically stable solution is distinguished by the extremum principle at
the level of one site approximation. In that case the one-site probabilities are expressed as p1 (+1) = (1+m)/2
and p1 (−1) = (1 − m)/2 and from the resulting thermodynamical potential Φ(m) Eq. (104) can be deduced
by the extremum condition ∂Φ(m)/∂m = 0. Direct comparison of the values of Φ(m) for the different
solutions justifies the preference of the upper (thicker solid) curve in the right plot of Fig. 19.
38

The dynamical mean-field equation can also be used to determine the dynamical stability of the above
solutions. The corresponding equation of motion summarizes the contributions of spin reversals for the
Glauber type evolutionary rules, that is,
∂m
1
1
1+m
1−m
=−
+
.
∂t
2 1 + e(4dJm+2h)/K
2 1 + e−(4dJm+2h)/K

(106)

Evidently, in the stationary state this equation becomes equivalent to Eq. (104). At the same time Eq. (106)
allows us to determine the basin of attractor for each solution as denoted in Fig. 19 by different colors.
Namely, if the system is started from a state with a magnetization m(0) then m(t) evolves vertically towards
the corresponding attractor. For high noise levels the system always develops into the only stationary
solution. For h = 0 and below the critical noise level (K < Kc ), however, the final state depends on
the initial state, that is, if m(t = 0) > 0 then the system develops towards the positive m(K) stationary
solution. For K < Kc the trivial solution m = 0 is a separatrix. In the presence of an external field
the separatrix is distorted as illustrated in Fig. 19. Consequently, when varying the initial magnetization
the dynamical mean-field theory allows the system to remain in both ferromagnetic states contrary to the
extremum principle favoring only one showing continuous variation in m(K).
Thermodynamically unstable (or meta-stable) states can be observed very frequently in the nature.
For example, after a suitable variation of temperature (or other thermodynamical quantities) materials
can evolve into (or remain in) a meta-stable phase like the supercooled liquids and gases. The disordered
phase in alloys (cooled down fast from a high temperature) remains present for a long time despite the
fact that phase segregation is favored thermodynamically at low temperatures (e.g., Cu-Au alloys) [163].
The magnetic hysteresis represents another example where the reversal of a weak magnetic field is not
accompanied directly by the reversal of m. Similar phenomena are present in biological and social systems
when varying the payoff parameters or dynamical rules in time [188, 189, 190].
In the light of the above phenomena the results of the mean-field approach can be interpreted as a
message that the mean-field conditions do not support the system to achieve the thermodynamically stable
state. Such a situation can occur in a social system where the players select z co-players at random from
the whole population and determine their strategies in the spirit of the Glauber dynamics. Later we will
show that for short-range interactions the system can evolve into the thermodynamically stable state due
to the enhanced role of fluctuations.
In fact, the main shortage of the mean-field theory is related to neglecting the fluctuations. This is not
dangerous when there are a large number of neighbors (here for z = 2d ≫ 1) and the law of the large
numbers ensures small variance in hef f . This is the reason why mean-field type behavior is expected in
many spatial multi-player systems if the spatial dimension d exceeds a critical value, that is, if d > dc .
In a low-dimensional system the fluctuations affect significantly the system behavior. Due to this effect
the prediction of mean-field theory is wrong in the one-dimensional systems (with short-range interaction)
that do not have long-range ordered arrangements at finite temperatures. Otherwise the mean-field theory
also gives a qualitatively good picture about the phase transitions in more complicated systems.
7.3. Series expansions and duality
The prediction of mean-field theory can be improved by the application of low and high noise series
expansions allowing us to extract additional properties of the Ising model. Now we study the traditional
ferromagnetic Ising model without magnetic field (hx = 0) on a square lattice with uniform interactions
Jxy = J between the nearest neighbors in order to illustrate the duality that is an inherent symmetry of
this system.
In the low noise limit (K → 0) the partition function [see Eq. (73)] can be approximated by summing
the contribution of those states that are present with the highest probabilities for a finite N as
Z = e2N J/K [1 + N e−4·2J/K + 2N e−6·2J/K + · · ·] .

(107)

Here the first term gives the contribution of the ordered ’up spins’ state (σx = +1); the second one comes from
states where only a single spin is reversed inside the ordered arrangement, and the third term summarizes
39

the contribution of states where only two nearest-neighboring spins are flipped. The argument of the
corresponding exponential functions reflects the interfacial energy of the island of spins reversed.
Similar expressions can be evaluated for other lattices even in the presence of a homogeneous magnetic field. The resulting expression can be used to derive analytical approximations for thermodynamical
quantities (e.g. magnetization, energy, specific heat) in the low noise/temperature limit.
The high noise series expansion is based on the following transformation suggested by van der Waerden
[191]. Accordingly, the contribution of a spin-pair to the Boltzmann factor is divided into two parts as
J

e K σx σy = cosh (J/K)[1 + σx σy tanh (J/K)]

(108)

where the second term goes to zero if K → ∞. Using this expression the partition function obeys the
following form:
X Y J
X Y
[1 + σx σy tanh (J/K)]
(109)
e K σx σy = [cosh (J/K)]2N
Z=
σ hx,yi

σ hx,yi

where the product runs over all possible nearest neighbors. The product can be expanded out into 22N terms,
where most of them [e.g. σx σy tanh (J/K) or (σx σy )(σx′ σy′ ) tanh2 (J/K)] have vanishing contribution to
the partition function after the sum is over the spin configurations. Exceptions are those products of spin
pairs where each σx has an exponent of 2 or 4 when their value is one for all the 2N spin configurations.
The latter constellations of different pairs have a general geometrical feature, namely, the connected σx σy
nearest neighbors form a closed loop (or collection of loops) as illustrated in Fig. 20.

Figure 20: (Color online) Leading pairs of contributions to the partition function for the low and high-noise series expansions
on the square lattice. For the low noise case (left) islands of down spins are indicated by open bullets in the sea of up spins
(closed bullets) while thick (red) edges denote spin-pairs contributing to the interfacial energy. In the high noise limit (right)
thick (blue) edges denote loops of neighboring spin-pairs giving non-zero contribution when summing over the spins.

As a result, the leading contribution to the partition function can be written as
Z = 2N [cosh (J/K)]2N [1 + N [tanh (J/K)]4 + 2N [tanh (J/K)]6 + · · ·] .

(110)

Comparing the expressions between the rectangular brackets in Eqs. (107) and (110) indicates their similarity
that remains valid for arbitrary high order of the approximations as justified by combinatorial methods
detailed in the reviews by Wannier [192], Newell and Montroll [159], and Domb [193]. This feature serves
as a basis for the so-called duality transformation mapping the low-noise behavior at J/K onto a high noise
Ising system with J/K ′ on the square lattice if
e−2J/K = tanh (J/K ′ ) .
40

(111)

′

This formula reflects that the square lattice Ising model is self-dual, that is e−2J/K = tanh (J/K). In short,
the dual of the dual is the original system. This symmetry was exploited by Kramers and Wannier [194] in
the first exact evaluation of the critical temperature.
Before going to the discussion of the critical transition we briefly mention several properties related to
the high-noise series expansions or duality. First we emphasize that the concept of duality remains valid for
other two-dimensional lattices. That means, for example, that the low-noise behavior on a triangular lattice
can be mapped into the high noise behavior on the honeycomb lattice as detailed in the above mentioned
reviews. Notice furthermore that both the high- and low-noise series expansions can be performed when the
coupling constant depends on x therefore it involves the possibility that the low noise behavior of an Ising
model with inhomogeneous coupling constant can be mapped onto another inhomogeneous Ising model at
high noises (disregarding the irrelevant prefactors in Eqs. (107) and (110)) [195].
Notice furthermore, that the high-noise series expansion reflects the relevance of loops formed by interacting spin pair throughout the connectivity structure. So this approach indicates directly the absence of
corrections for the loop-free networks, namely, on the one-dimensional lattice with open boundary or on the
tree-like structures including Cayley trees. As a result, the partition function of the Ising model on loop-free
networks can be given as
Z = 2N [cosh (J/K)]Nl
(112)
where Nl is the number of links (connected spin pairs) in the given structure. For example, Nl = N − 1
for the one-dimensional lattice where the vanishing correction ([2 sinh J/K]N ) of the periodic boundary
condition can also be evaluated as it comes from the only loop containing all the sites/edges. Notice that
Nl = N − 1 for all the tree-like structure (independent of the degree distribution).
7.4. Critical phase transitions on lattices
In the quantitative analysis of the critical phase transition(s) from the disordered state to the ordered
one, several quantities play fundamental roles [196, 162]. For example, in a ferromagnetic system the average
magnetization m is defined as
1 X
hσx ih→+0
(113)
m=
N x

where the sum runs over all sites x of the lattice. In general m is considered to be an order parameter where
h· · ·ih→+0 denotes long-time average in the stationary state in the presence of an external magnetic field
with strength h → +0. For any finite value of h the probability of the states of disfavored magnetization
is suppressed in the Boltzmann distribution in the limit N → ∞. Using this approach we can avoid the
difficulties related to the nonergodicity mentioned above.
In the equivalent evolutionary potential games the above order parameter can also be used for the
quantitative analysis of the ordering by substituting σx = +1 (σx = −1) if sx = D (sx = C).
For the analysis of an anti-ferromagnetic system the lattice sites are divided into two disjoint sublattices
(x ∈ X and y ∈ Y ) as discussed in Sec. 4. This anti-ferromagnetic system can be transformed into a
ferromagnetic model by substituting J → −J and σy → −σy ∀y ∈ Y . This transformation is accompanied
by a transfer of the homogeneous magnetic field h into a staggered magnetic field hs and vice versa. In the
absence of magnetic fields this transformation explains the equivalence of the corresponding order-disorder
transitions.
For these sublattice ordered spatial structures the anti-ferromagnetic order parameter is usually defined
as


X
2 X
hσx ihs →+0 −
(114)
hσy ihs →+0 
m=
N
x∈X

y∈Y

where the averages are evaluated in the limit hs → +0. Henceforth we will not denote these assumptions.
In Fig. 21 Monte Carlo data of the order parameter are indicated by symbols when varying the noise level
(temperature) for an evolutionary social dilemma game with nearest neighbor interactions on the square
lattice. Data obtained for Glauber dynamics at parameters T = 1.5 and S = 0.5 are identical to the case
41

1.0
0.8

m

0.6
0.4
0.2
0.0
0.0

0.2

0.4

0.6

0.8

K
Figure 21: (Color online) Monte Carlo results for the order parameter m as a function of noise for evolutionary potential games
with Glauber dynamics on square lattice at several values of payoff parameters: in the notation of social dilemmas: T = 1.5,
S = 0.5 (boxes); T = 1.4, S = 0.3 (diamonds); T = 0.5, S = −0.49 (open circles); and T = 0.5, S = −0.499 (closed circles).
The exact solution for the corresponding Ising model is denoted by a solid line. Dotted (blue) and dashed (red) lines illustrate
the prediction of the cluster variation method for the levels of one- and two-site approximations.

of an anti-ferromagnetic Ising model without the external magnetic fields (h = hs = 0) for which the exact
solution was obtained by Onsager [158] as
1

√ Kc −4 8
,
m = 1 − [sinh (ln(1 + 2) )]
K

(115)

√
where Kc = 2J/ ln (1 + 2). The results illustrate clearly how the system undergoes an order-disorder
transition at a critical noise level. As mentioned above, this value of Kc can also be evaluated from the
duality relation by substituting K = K ′ = Kc into (111). For low noises (K < Kc ) the order parameter
varies from 1 monotonously and continuously to zero when approaching the critical point and remains m = 0
if K > Kc . Similar transition can be observed for other evolutionary games (where T −1 = S) corresponding
to the zero-field Ising model. More precisely, the m(K/Kc ) functions coincide and Kc is proportional to
|T − 1 + S|.
It is well known that for the anti-ferromagnetic Ising model the main features of the critical transition
remain unchanged in the presence of an external magnetic field h whereas the critical noise level decreases
as illustrated by data obtained for T = 1.4 and S = 0.3. This behavior is related to the fact that h does not
influence the total energy of the two equivalent ordered spin arrangements. Similar effects can be observed
for the ferromagnetic Ising model when a staggered magnetic field (hs ) is switched on for h = 0 due to
the above-mentioned intimate relationship between the ferromagnetic and anti-ferromagnetic Ising models.
On the contrary, the application of h to the ferromagnetic systems smoothed the abrupt variation of the
order parameter as illustrated by open and closed circles in Fig. 21. These Monte Carlo data show how the
magnetization tends towards the exact solution if the corresponding magnetic field goes to zero. Notice,
furthermore, that m remains positive for arbitrary noise levels while m → 0 if K → ∞. In addition, the
symmetries prescribe that m(−h) = −m(h). Evidently, similar behavior occurs for the anti-ferromagnetic
system in the presence of a staggered field.
Notice the excellent coincidence between the analytical and numerical results we have obtained for
T = 1.5 and S = 0.5 while Monte Carlo data (with m < 0.5) are missing in the close vicinity of the critical
point. The latter deficiency is a direct consequence of the technical difficulties related to the general features
of this type of critical transitions. Namely, the average value of the order parameter vanishes algebraically,
more precisely,
m ∝ (Kc − K)β ,
(116)
42

with β = 1/8 if K → Kc from below for all the cases (T > 1 and S > 0) when the chessboard-like ordered
strategy arrangement transforms into a disordered (m = 0) state as illustrated in Fig. 22. In the absence of
1.0

m

0.5

0.2

0.1
0.0001

0.001

0.01

0.1

1.0

Kc-K
Figure 22: Log-log plot of the order parameter as a function of Kc − K for results plotted in Fig. 21.

the exact two-dimensional solution for h 6= 0 the latter universal feature was suggested by Griffiths [197] and
justified by Rapaport and Domb [198] who used approximation methods in the investigation of the transition
from the disordered (paramagnetic) state into the anti-ferromagnetic structure in the presence of a magnetic
field. The exploration of this universal behavior in the critical phase transitions was also motivated by the
experiments. In fact, the first critical exponent (or divergency) was observed when measuring the specific
heat as a function of temperature in the absence of magnetic field. Within the context of thermodynamics
the different versions of the specific heat are described as the second partial derivative of the suitable
thermodynamic potential and denoted as
ch ∝ |Kc − K|α ,

(117)

where the index h refers to fixed magnetic field for the anti-ferromagnetic systems. For the ferromagnetic
system h = 0 is required otherwise the external field h suppresses the divergence of ch in parallel with the
elimination of the power law behavior in the magnetization as shown in Fig. 21. Accordingly, instead of the
power law divergency, one can observe a peak in the K-dependence of the specific heat at the vicinity of
Kc and the height of this peak decreases if h is increased. Evidently, the internal symmetries of the Ising
model imply that the application of a staggered magnetic field (hs ) results in similar consequences for the
transitions from anti-ferromagnetic to paramagnetic phase.
In agreement with the features mentioned above and with the fluctuation dissipation theorem [see [199]
with further references therein] the magnetization depends sensitively on the external magnetic field at the
critical point (K = Kc ), namely,
m ∝ |h|1/δ .
(118)

In the understanding of the universal features of the critical behaviors, the analysis of the correlation
functions played crucial roles. The general versions of correlation functions are defined in the translation
invariant stationary states as
(j)

(j)

′
′
(i)
′
g (i,j) (x, t) = hn(i)
y (t )nx+y (t + t )i − hny (τ )ihnx+y (t + t )i

(119)

where i and j denote strategy labels (i, j = 1, . . . , n), h· · ·i refers to averaging over all sites y and time t′ .
Notice that here we use the vector notation of sites in the argument of the correlation functions although in
(i)
many numerical analyses x refers to horizontal (or vertical) spatial distances. nx is the extended definition
of the occupation variable at time t and site x, namely,

1 for sx = i ,
n(i)
(t)
=
.
(120)
x
0 otherwise
43

For sublattice ordered structures it is convenient to prescribe that x ∈ X and y ∈ Y . For short range
interactions the one-time correlation function decreases exponentially with the horizontal or vertical distance
as
−|x|
g (i,j) (x, 0) ≃ e ξij
(121)
if |x| → ∞. The one-site correlation function shows similar behavior, namely,
−t

g (i,j) (0, t) ≃ e τij

(122)

if t ≫ 1. Both the correlation time τij and the correlation length ξij depend on the noise level K as well
as on the potential parameters. In the Ising model for h = 0 we can omit the indices (i and j) and the
corresponding quantities diverge as
ξ ∝ |(Kc − K)|−ν⊥
(123)
and
τ ∝ |(Kc − K)|−νk

(124)

with ν⊥ = νk = 1 when approaching the critical point. We note that νk characterizes the so-called critical
slowing down in the time-dependence of correlations. Beside it, the intensity of the fluctuation of order
parameter given as
#2
"
E
D X
X
(125)
χm = N h
σx i −
σx
x

x

also diverges. More precisely,

χm ∝ |(Kc − K)|−γ .

(126)

In the stationary state at the critical point the correlation function decreases algebraically, that is,
g(x, 0) ∝ |x|2−d−η⊥ .

(127)

All these features jointly cause serious technical difficulties in Monte Carlo simulations if one wishes to
determine the order parameter with a reliable accuracy in the close vicinity of the critical point, because
both the system size and sampling time should be chosen to be significantly larger than the correlation
length and time.
In fact the exponents introduced above are not independent. One of the main results of the statistical
physics in the 20th century is the explanation of the universal behaviors in the critical phase transitions.
Using the scaling hypothesis and the renormalization-group techniques, introduced by Kadanoff [200] and
Wilson [201], relations have been explored between the above defined critical exponents. One form of this
idea assumes that the singular part of the thermodynamic potential Φ(K, h) in the close vicinity of the
critical point Kc is a generalized homogeneous function of ε = |K − Kc |/Kc and h, e.g.,
Φs (λah h, λaε ε) = λΦs (h, ε)

(128)

as surveyed briefly by Stanley [202]. This concept implies that two parameters (ah and aε ) determine the
values of critical exponents. The validity of the scaling hypothesis is confirmed by numerous experiments
and theoretical calculations by observing data collapse when a thermodynamic quantity of two variables
(e.g. m(h, K − Kc )) forms a single curve, if we use suitable scales in a two-dimensional plot. The latter
feature reflects a universal behavior and is valid in the close vicinity of the critical point for the systems
belonging to the Ising universality class.
The concepts of renormalization group techniques helped us understand the phenomena and relevant
conditions resulting in the universal behaviors (for a brief survey of the essence and history of this approach
see the review by Fischer [203]). This approach distinguishes relevant (e.g., spatial dimension d, number
n of possible states, and additional symmetries) and irrelevant (lattice structure) quantities and gives an
adequate description and explanation of the universal behavior at the critical point (and also in its close
vicinity). These investigations have justified that the diverging quantities tend asymptotically towards a
44

exponent
α
β
γ
δ
η
ν⊥

d=2
0(log)
1/8
7/4
15
1/4
1

d=3
0.110(1)
0.34265(3)
1.2372(5)
4.789(2)
0.0364(5)
0.6301(4)

d=4(MF)
0
1/2
1
3
0
1/2

Table 1: Critical exponents of the d-dimensional Ising model.

power law behavior characterized by the same exponent on both sides of the critical point. For example,
when approaching the critical point ξ ≃ C1 (Kc − K)γ if K < Kc and ξ ≃ C2 (K − Kc )γ if K > Kc (C1 6= C2 ).
This is the reason why we used the same notation for the exponents below and above the transition point.
The renormalization group techniques have confirmed quantitatively the universal scaling hypothesis
between an upper and lower spatial dimension d. The predictions of the scaling hypothesis are simple
consequences of the properties (128) preserved by the Legendre transform of Φ(K, h) and its derivatives.
Since the critical exponents are directly related to ah and aε , one can derive scaling laws by eliminating
these variables. Using this method three scaling laws can be derived:
α + 2β + γ

= 2,

(129)

α + β(δ + 1) = 2 ,
(2 − η⊥ )ν⊥ = γ .

(130)
(131)

which are independent of the spatial dimension d, whereas the fourth, so-called hyper scaling law, indicates
directly the relevance of the spatial dimension as
2 − α = dν⊥ .

(132)

Due to these relations only two of the six static exponents are independent. For the practical identification
of this class of universal behavior in any models one needs to check the values of only two static exponents.
For the systems belonging to the Ising universality class, the values of most relevant exponents as a
function of the spatial dimension d are summarized in Table 1. The reader can find a comprehensive list
of the theoretical and experimental results in the review by Pelissetto and Vicari [168] and in the book
by Ódor [204]. The one-dimensional results are missing here due to the absence of the critical transition.
For d ≥ 4 the critical behavior and exponents are well described by mean-field theory. Furthermore, the
two-dimensional results are extracted from the exact results and the value of α = 0 refers to logarithmic
divergence (ch ∝ − log ε) in the specific heat.
Finally we emphasize that a similar universal critical behavior can even occur in other non-equilibrium
models where the probability distribution of the microscopic states differs from the Boltzmann distribution.
For example, Pérez et al. [205] have reported this type of universal critical transition in an Ising model,
where the spins are reversed simultaneously as in the stochastic cellular automata surveyed by Wolfram
[206].
The critical phenomena have also been explored for the Potts models on different lattices and graphs.
Most of our knowledge comes from a wide scale of analytical (approximation) methods or numerical techniques and are justified by experiments. As it is known, the mean-field description gives a qualitatively
correct picture of the phase transition in the Ising model. Kihara et al. [180] found that the mean-field
approach predicts first-order phase transition for all n > 2. Subsequently, the more sophisticated methods
have clarified that the order-disorder transitions are of first-order for n > 4 at d = 2; n ≥ 3 at d = 3; and
n > 2 at d = 4 in homogeneous spatial systems [182].
Contrary to the mean-field prediction, the order-disorder transitions are continuous for all the twodimensional lattices if n = 2, 3, or 4. These critical transitions exhibit power law behavior in several
45

exponent
α
β
γ
δ
η
ν⊥

n=2
0(log)
1/8
7/4
15
1/4
1

n=3
1/3
1/9
13/9
14
4/15
5/6

n=4
2/3
1/12
7/6
15
1/2
2/3

Table 2: Critical exponents vs. n for the two-dimensional Potts models.

quantities in the close vicinity of the transition point as detailed above. The corresponding critical exponents
are listed in Table 2 where the values in column n = 2 are equivalent to the critical exponents of Ising model
given also in Table 1. Evidently, the listed values of the critical exponents satisfy the relations expressed by
(129)-(132) as these are derived from general scaling laws.
It is emphasized that the above robust behavior occurs in homogeneous spatial systems where n individual
strategies or degenerated ground states can be distinguished. Deviations from these universal behaviors
appear when the spatial systems become inhomogeneous or the connections between the players are described
by different graphs [207].
7.5. Ordering in other relatives of the Ising model
The decomposition of payoff matrices for n strategies has highlighted the relevance of those basis games,
denoted as d(p, q), that possess Ising type interactions between the pth and qth strategies. These models
have not yet been investigated systematically. The Monte Carlo simulations on a square lattice with logit
dynamics indicate an Ising type ordering process when increasing the noise level K as it is illustrated in
Fig. 23 for three values of n. For all the three interactions d(1, 2) the system prefers the homogeneous
sx = 1 or sx = 2 state in the low noise limit and (ρ1 − ρ2 ) → 0 if K approaches Kc from below. The
preferences of the strategies 1 and 2 can be observed for K > Kc because of the formation of their cluster
when ρ1 = ρ2 > ρn (for n > 2). However, in the limit K → ∞ the fluctuations suppress these correlations
and all the n strategies are present with the same probability (1/n).

strategy frequency

1

n=2
n=3

0.8

n=4

0.6
0.4
0.2
0
0

0.5

1

1.5

2

2.5

K
Figure 23: (Color online) Strategy frequencies as a function of K for spatial evolutionary games if the interaction is defined by
d(1, 2) [see Eq. (41)]. The Monte Carlo data of the 1st (2nd) strategies are indicated by closed (open) symbols for n = 2 (red
◦), n = 3 (△), and n = 4 (blue boxes). The frequencies of the third and fourth strategies for (n = 4) are indicated by (blue)
pluses and crosses while the symbol ▽ shows the frequency of the third strategy for n = 3.

The first numerical investigations [31, 59, 208] support the theoretical expectations predicting Ising type
critical transitions at Kc (n) for n = 3 and 4. The preliminary Monte Carlo results show that Kc (n) decreases
46

if n is increased and the phase transition becomes a first order one if n exceeds a threshold value.
In the above-mentioned systems the critical phase transitions are smoothed if the interaction is perturbed
by switching on a self-dependent component or an additional coordination type interaction that can prefer
the first (or the second) strategy. The ρi (K) functions in Fig. 24 are obtained for an interaction that results
in the dominance of strategy 1 in the low noise limit. In this plot we were able to illustrate the Monte Carlo
data by lines due to the absence of the fluctuation enhancement in the region of smooth transition.

strategy frequency

1
0.8

1

0.6
0.4

2
3

0.2
0
0

0.5

1

1.5

2

2.5

3

K
Figure 24: Strategy frequencies vs. noise level K if the interaction is given by A = d(1, 2) + 0.1 · d(1, 3) in the three-strategy
multi-agent evolutionary potential game.

As mentioned previously, the symmetric potential matrix can possess two equivalent preferred Nash
equilibria [(p, q) or (q, p) if max(Vij ) = Vpq = Vqp ] even for n > 2. On the square lattice these interactions
yield two equivalent sublattice ordered strategy arrangements when the players select strategies p and q
in the sublattices X and Y or conversely if K → 0. When increasing the noise level K these systems
exhibit an order-disorder phase transition at Kc . The strategy frequencies in the sublattices show a similar
K-dependence plotted in Fig. 23. Contrary to the case of equivalent homogeneous ordered states, the equivalence between the sublattice ordered strategy distribution is not destroyed if the interaction is perturbed
weakly because their effects are identical on both sublattices. Consequently, the Ising type sublattice ordering takes place in a wide region of the payoff parameters. The latter phenomenon is resembling the effect
of the external magnetic field h on the anti-ferromagnetic ordering if its value does not exceed a threshold
value (see Figs. 16 and 21).
7.6. Critical phase transitions on networks
The investigation of the Ising model on different networks also has a long history as detailed in the
review by Dorogovtsev et al. [207]. First we discuss the simplest cases where the players are distributed on
a Cayley tree or Bethe lattice that is considered as an infinite Cayley tree without its periphery. Despite the
strong relationship between these connectivity structures, the Ising model exhibits fundamentally different
behaviors on them as it was emphasized in early works of Eggarter [111], Müller-Hartmann and Zittartz
[209], Wang and Wu [210].
The first important difference is due to the fact that a relevant portion of the nodes of the Cayley tree
belongs to the periphery (the leaf nodes in graph theory terminology) where the players have only one
neighbor and the presence of this boundary affects the macroscopic behavior significantly, due to the large
number of these sites. On the other hand, this feature is utilized in the determination of the exact solution
[111, 112, 211]. The absence of the ordered states on the Cayley tree for any finite values of K is related
to the fact that when removing a single edge this structure is divided into two independent parts where
opposite ordered structure can be formed. Due to this feature, arbitrary deviation in the magnetization can
be achieved by generating a single point defect that is always present at finite K in the sufficiently large
47

systems. A similar reason explains the absence of ordered strategy arrangements (and phase transition) in
the one-dimensional lattice where one of the long-range ordered phases occurs only for K = 0.
Müller-Hartmann and Zittartz [209] have shown that the thermodynamic potential (free energy) on the
Cayley tree becomes a nonanalytic function of the magnetic field h below a critical temperature KBP given
by the pair approximation applied by Bethe [140] and Peierls [155]. More precisely, the leading part of the
nonanalytic behavior is proportional to hκ where the exponent κ increases monotonously from 1 to ∞ as the
temperature goes from 0 to KBP . This phenomenon is accompanied by a diverging magnetic susceptibility
below the transition point. Mélin et al. [212] have shown that this unusual behavior may be related to the
large number of metastable states that are stable with respect to single-spin flips.
The use of Bethe lattice eliminates the boundary layer and assumes translation invariance (i.e. the
equivalence of sites). Using this assumption we can derive analytical results that predict mean-field type
order-disorder phase transition if K is increased. Due to the absence of loops in this structure the two-site
cluster variation method (called also Bethe-Peierls or pair approximation) reproduces the exact result as
indicated in Fig. 25 where the MC data are obtained on a random regular graph for large sizes as the MC
simulations cannot be performed on an infinitely large Bethe lattice. In network analysis [213, 214] and
1.0
0.8

m

0.6
0.4
0.2
0.0
0.0

0.2

0.4

0.6

0.8

K
Figure 25: Order parameter m as a function of noise K for evolutionary hawk-dove game with Glauber dynamics at payoff
parameters T = 1.5, S = 0.5 if the players are located on a random regular graph of degree 4. Xs indicate MC data for
N = 2 × 106 . The solid line denotes the prediction of the two-site cluster variation method for the Bethe lattice and the
Onsager results (on square lattice) are illustrated by dotted line.

graph theory [55] it is well known that the average length of the shortest loops for the random regular
graphs increases with ln N . Consequently, this approach can give an adequate description of the system
behavior for those cases where the sparse and long loops of the connectivity structure do not modify the
behavior relevantly. This approach is capable of explaining more striking differences in those phenomena
where a random regular graph is substituted for the square lattice in a three-strategy evolutionary game
[215].
In the last decades the statistical analysis of different networks initiated the reinvestigation of traditional
lattice models on a wide scale of complex networks. Most of these networks are claimed to provide a better
description of the connections that have emerged in social interactions, neural systems, communication,
transportation, etc. Some of these network models are capable of describing a continuous transition from
a spatial lattice to random or random regular graphs, while others create novel features not involved in
the traditional concept of lattices. Now we briefly outline what happens to the Ising and Potts models on
several types of networks.
The so-called small-world effect takes place in networks where the average shortest distance between two
nodes is proportional to ln N . The Bethe lattices, Cayley trees, and random regular graphs possess this
feature. Watts and Strogatz [216] proposed a way of building the small-world effect into spatial lattices. In
the first model they considered a one-dimensional chain (ring) with first- and second-neighbor interactions.
48

exponent
α
β
γ
δ

υ>5
1st order
1/2
1
3

υ=5
0(log)
1/2⋆
1
3⋆

3<υ<5
(5 − υ)/(υ − 3)
1/(υ − 3)
1
υ−2

Table 3: Critical exponents vs. υ for the Ising models on scale-free graphs. ⋆ refers to logarithmic corrections described in
[222, 223].

The small world feature is achieved by removing qN connections from the lattice and connecting one of their
end points to another site chosen at random (0 < q ≪ 1). This method does not modify the average number
of neighbors though it destroys the regularity. At the same time, it can be applied for any d-dimensional
lattices. The number of neighbors is conserved at each site by the method proposed by Newman and Watts
[217] where connections are interchanged between pairs of connected sites selected randomly. Soon after the
network models had been published, different phenomena were investigated on the resultant structures.
Studying the one-dimensional Ising model with the above rewired lattices or with a lattice obtained by
adding a portion q of new links, Barrat and Weigt [218] and Gitterman [219] have observed the appearance
of ordered structure at finite noise levels (K < Kc (q)) in sufficiently large systems. It is found that Kc
increases monotonously with q and Kc ∝ −z/ log (q) for low values of q where z (z ≥ 4) is the number of
neighbors in the starting one-dimensional chain. They also reported a mean-field type phase transition at
Kc .
These types of small-world structures were reinvestigated by Herrero [220] and Chatterjee and Sen [221]
when the initial structure was a square (d = 2) or cubic (d = 3) lattice. Their analyses have confirmed the
presence of the ordered state at low temperatures in agreement with the expectation. The increase of Kc
was similar to those found for the one-dimensional cases, that is, δKc ∝ 1/ log (q) and the phase transitions
were of mean-field type.
Up to now we have studied the Ising models on regular or quasi-homogeneous networks where the
degrees of nodes were close to their average value. Fundamentally different behaviors were reported by
Dorogovtsev et al. [222] and Leone et al. [223] who studied the Ising model on random graphs with a degree
distribution having a fat tail. Most of these investigations are performed on networks having a power-law
degree distribution p(z) ∝ z −υ for large number (z) of neighbors. Using different approaches these authors
studied the general features of the ferromagnetic phase transitions for different values of υ. The analyses
showed mean-field type phase transitions when υ > 5. These approaches indicated non-trivial critical
exponents for 3 ≤ υ ≤ 5 as listed in Table 3. Note that behavior of the fluctuation is not affected by the
value of υ within this region, while α, β, and γ depend on υ in a way that breaks the scaling relations (129)
and (130).
For υ ≤ 3 the role of the high degree nodes (hubs) becomes relevant in the limit N → ∞ and the system
stays in a ferromagnetic state for arbitrary noise level K. Within this range of υ, however, a size effect
can be observed because the value of N limits the maximum of z, too. As a result, for most of these finite
systems the Ising model exhibits an order-disorder transition at Kc ∝ ln (N ) according to the theoretical
investigations mentioned above, in agreement with the results of Monte Carlo simulations [224]. Many
realistic networks and network models belong to this class, therefore the latter feature governs the behavior
in both biological and social systems.
In the above small-world networks the additional random links can be interpreted as a way of introducing
long-range interactions. Similarly to the Lévy flights, the strength of long-range interactions can be weakened
by creating the additional links with a probability p(l) ∝ l−∆ where l is the Euclidean distance between
the sites to be connected and ∆ > 0. The behavior of the resulting system is similar to those obtained by
introducing long-range interactions, as discussed in the following section.
Fundamentally different behaviors were reported by Gefen et al. [225, 226] who studied the Ising and
Potts models on several fractal lattices discussed by Mandelbrot [227]. In the 80s the analysis was extended
49

by Bhanot et al. [228], d’Auriac and Rammal [229], Bonnier et al. [230], Monceau et al. [231]. Some of
the fractal lattices were generated by an algorithm producing a Sierpinski carpet. For example, a large
hypercube of a d-dimensional lattice with ñk̃d sites is divided into ñd equal hypercubes and (ñd − m̃) of
them are removed. The same process is repeated for the rest of the smaller hypercubes. After the k̃th
segmentation steps we get a fractal lattice characterized by a fractal dimension df = ln (m̃)/ ln (ñ) that can
be tuned from 0 to d. The resultant self-similar structures made these types of models attractive for the
application of renormalization group techniques and other exact methods. A series of investigations have
clarified that the behavior of the Ising model on these lattices depends not only on the fractal dimensions,
but is also affected significantly by other topological features like the order of ramification and lacunarity
[225, 232].
The order of ramification R measures the number of links to be cut in order to isolate an arbitrarily large
portion of the network. If R is finite then the ferromagnetic ordering is missing at finite noise levels. Notice
that this criterion is the generalized version of those we used above for explaining the absence of ordering
in the one-dimensional lattice and Cayley trees. Among the fractal lattices the quasi-linear structures
(generated similarly to the Koch-curve) [233] and some versions of the Sierpinski gasket [234] represent
networks on which the Ising model has no long-range order (and phase transition) at finite noise level K.
On the contrary, phase transition occurs if R = ∞ in the limit N → ∞. The first papers [234] indicated
clearly that some critical exponents depend also on the lacunarity Λ [235], which quantifies the deviation
from the translation invariance. For the above mentioned Sierpinski carpets the lacunarity Λ measures how
the removed small boxes are distributed. At high lacunarity the removed boxes form a large hole, while at
low lacunarities these boxes are distributed ”homogeneously”.
The critical exponents of the resultant phase transition are studied quantitatively only on a few fractal
lattices. For example, Monceau et al. [231] and Carmona et al. [232] studied the critical behavior on the
above mentioned Sierpinski carpet for d = 2, ñ = 3, m̃ = 8 where df = ln (8)/ ln (3) = 1.8927 . . .. Despite the
technical difficulties their results are consistent with the suggestion of Wu and Hu [236] stating the existence
of a weaker universality class. Accordingly, the static exponents may vary with the geometrical parameters
of the fractal (e.g., df and lacunarity) and the relations between the critical exponents (129)-(132) are valid
if df is substituted for d in (132). In a subsequent paper Monceau and Hsiao [237] studied the critical
behavior on fractals sharing the same fractal dimension but having different lacunarities. It was found that
the long-range order at the critical point decays faster when the lacunarity is increased for a given df .
At the end of this section it is worth mentioning that most of the above discussions are based dominantly
on approximate results supported by numerical simulations. Very recently, however, Dembo and Montanari
[238], Montanari et al. [239], and Dembo et al. [240] have performed a more rigorous mathematical analysis
of the Ising and Potts models on locally tree-like structures and their results support the picture sketched
above.
7.7. Long-range interactions on lattices
In ionic compounds the Coulomb interaction plays a crucial role in the formation of the microscopic
arrangements of ions even in the cases when screening complicates the analysis in the presence of opposite
charges [165]. For the ferromagnetic materials the dipole-dipole interaction is responsible for the emergence
of a proper magnetic domain structure that results in an almost zero remanence magnetization in the soft
magnets [153]. In solid solutions the interaction between two large interstitial atoms is mediated by the
lattice distortion and it can be well approximated by a suitable long-range interaction. This interaction
drives the segregation process. In social and biological systems the diffusion of opinion or chemical products
can also mediate a similar long-range interaction. For the investigation of these type of interactions, the
formalism of the Ising model provides a good mathematical background, although huge technical difficulties
arise from the large number of interactions to be considered in the real phenomena. In short, the analysis
of the Ising and Potts models with long-range interactions on lattices is recently at a beginning stage.
There are, however, several results that are worthy of a brief outline. In many cases the coupling constant
Jxy between the sites x and y is expressed by an algebraic function Jxy = 1/|x − y|d+∆ where |x − y| is
the Euclidean distance on the d-dimensional lattice and ∆ quantifies the type of long-range interactions.
50

Assuming a ferromagnetic interaction, the total effect (sum) of the coupling constants Jxy over the whole
system helps preserve the ferromagnetic state. This quantity as well as the total energy, however, diverges
if ∆ ≤ 0 as
Z ∞
X
X
1
1
Jxy =
≃ a(d)
dr
(133)
d+∆
1+∆
|x − y|
r
1
y,y6=x

y,y6=x

d−1

where a(d)r
refers to the surface of a d-dimensional sphere of radius r. Consequently, the ferromagnetic
state is stabilized if ∆ ≤ 0. Since the early work of Ruelle [241] the systematic analysis of the Ising and
Potts models has clarified what happens for ∆ > 0.
Ruelle [241] proved rigorously the absence of long-range order in the one-dimensional Ising ferromagnetic
model if ∆ > 1. On the other hand, Dyson [242] proved the existence of a phase transition in these systems
if 0 < ∆ < 1. For ∆ = 1 the existence of phase transition was justified later by Dyson [243] and by
Imbrie and Newman [244] who described an intermediate phase where the two-point correlation function
exhibits power law decay with a K-dependent exponent below Kc . Using the renormalization group approach
Fisher et al. [245] have shown that the one-dimensional Ising model exhibits mean-field-like behavior for
0 < ∆ < 0.5 while non-trivial (∆-dependent) exponents are found for 0.5 < ∆ < 1. For higher dimensions
the analyses were focused on two regions of ∆ where mean-field or ∆-dependent exponents are predicted by
the renormalization group techniques.
7.8. Sublattice ordered structures on lattices
If the range of interactions exceeds the nearest neighbors on a lattice then we may face a wide variety of
sublattice ordered states in the low noise limit. The extensive investigations of these systems were unavoidable in solid state physics where the effects of the second- and third-neighbor interactions with different
strengths are studied in many materials. For example, the adequate description of the oxygen ordering in
the Cu-O layer of the super-conducting YBa2 Cu3 O7−δ compounds required to take into consideration four
terms of interactions [246].
The introduction of the additional second- and third-neighbor interactions (denoted as J2 and J3 ) does
not cause qualitatively different behaviors if all the coupling constants favor the ferromagnetic structure, that
is, if J1 , J2 , J3 > 0. The presence of the additional terms increases the value of Kc . Fundamentally different
consequences occur, however, if the additional interactions do not support the formation of the ordered
arrangement dictated by the first-neighbor interactions. In the latter cases numerous types of ordered
structure may emerge. For the illustration of these phenomena we study now a simple model investigated
in detail first by Binder and Landau [247] and recently by Yin and Landau [248] and de Queiroz [249].
Consider an Ising model on the square lattice with equivalent anti-ferromagnetic interactions (J1 =
J2 = −1) between the first and second-neighbors for the presence of a magnetic field h. One can assume
that all the possible ordered structures can be built up by tiling, that is, by repeating one of the 2 × 2
patterns shown in Fig. 26. The resulting long-range ordered arrangements can be well described by a four-

Figure 26: All the possible spin arrangements within a 2 × 2 cluster of sites that are used for generating four-sublattice ordered
arrangements on a square lattice.

sublattice description defining the average magnetization for each sublattice. Notice that patterns within
the second, third and fifth column of Fig. 26 can be transformed into each other by a rotation of 90◦ and the
51

corresponding ordered structures have the same potential (or energy) in the macroscopic system. All these
three types of ordered structures are fourfold degenerated and involve the possibility that the corresponding
order-disorder transitions belong to the Potts model universality class for n = 4 and d = 2.
Contrary to the naive expectations, simulations have indicated a more complex behavior both in the
spatial patterns and in the phase transitions. Figure 27 illustrates four snapshots when increasing h. All these
simulations are performed at a low noise level in order to keep the strip like anti-ferromagnetic arrangement
(see the bottom right plot in Fig. 27) almost free of point defects. The applied magnetic fields are selected
according to the phase diagram reported by Yin and Landau [248] and represent different phases. Besides
these four phases there exists a disordered (paramagnetic) spin arrangements stabilized for sufficiently high
noise level (K > Kc (h)) or high fields |h| > 8.

h=6.0

h=4.1

h=3.9

h=0.0

Figure 27: Ordered and partially ordered spin arrangements in the kinetic Ising model on the square lattice when the first- and
second-neighbor anti-ferromagnetic coupling constants are equivalent and K = 0.3 · |J| for different external magnetic fields
(h) indicated by figures inside the (50 × 50) snapshots.

The fourfold degenerated strip-line anti-ferromagnetic structure undergoes a phase transition to the
paramagnetic phase at Kc (h = 0) = 2.08. This curious phase transition will be discussed later. In the zero
noise limit this ordered structure is stable as long as |h| < 4. For 4 < |h| < 6 a partially ordered structure,
called row-shifted (2×2) phase, can be observed in the low noise limit. The corresponding spin arrangements
can be constructed from the completely ordered pattern built up from one of the (2 × 2) blocks of the second
columns in Fig. 26 that consist of ferromagnetic and anti-ferromagnetic rows (columns) alternately. For the
present interactions the total energy (or potential) is not changed if the anti-ferromagnetic rows are shifted
horizontally at random. In the resultant partially ordered phase the entropy remains finite in the limit
K → 0. Due to the symmetries the equivalent column-shifted states can be constructed in a similar way.
Thus within a region of h dependent on the temperature this system has two equivalent sets of partially
ordered structures. Within this region one can observe a spontaneous symmetry breaking that is analogous
to the formation of ferromagnetic or anti-ferromagnetic structures if the system is started from an ordered
structure at a low noise level. This process is driven by the increase of entropy while the coexistence of the
domains of row- and column-shifted phases is prevented by the positive interfacial energy.
Between the strip-line and row-shifted structures, it has been possible to distinguish two additional
phases by [248] in the phase diagram at low noises. The upper-right snapshot of Fig. 26 illustrates the spin
arrangement in the paramagnetic phase with short-range correlations resembling all the above mentioned
52

ordered phases. The appearance of the disordered (paramagnetic) phase is common at low noises in the
phase diagrams between basically different ordered phases. In the present model, however, another type
of structure (see the left-bottom snapshot in Fig. 26) is observed. The latter phase can be considered as
a poly-domain pattern of the strip-line phases where the presence of interfaces is stabilized as it occurs in
water-oil emulsions or other self-assembling systems [250, 251]. Remarkably, the distinction of this phase
required sophisticated techniques.
Recently different methods have been applied by Yin and Landau [248] and de Queiroz [249] for the
classification of the phase transitions in the present model. According to these investigations, the phase
transitions from the ordered or partially ordered structure into the disordered one are continuous but not
universal. Both transitions exhibit power law behavior with exponents dependent on the magnetic field. In
other words, these transitions do not belong to the above mentioned universality classes of the Ising and
Potts models.
The above features are not unique. Similar phenomena can be observed for the present model when
varying the ratio J2 /J1 or when additional interactions are switched on [252]. In the paper by Dublenych
[253] the reader can find dozens of patterns that can be used for building up long-range ordered structures of
the Ising model on triangular lattices, if first- and second-neighbor interactions are taken into consideration.
Evidently, analogous phenomena are expected in lattices for higher dimensions if the range of interactions
is increased and also in evolutionary potential games when the number of strategies exceeds 2.
7.9. Frustration
In the previous section we have faced situations when the ground state was infinitely degenerated (see
the upper-left snapshot of Fig. 26). Such a situation becomes natural on lattices where three spins (players)
interact with each other via equivalent anti-ferromagnetic pair interactions (anti-coordination games) as
denoted on the left panel of Fig. 28 [254]. This phenomenon was first described by Wannier [255] who studied
the anti-ferromagnetic Ising model on a triangular lattice. In fact, for the anti-ferromagnetic interactions,
the basic reason is related to the presence of loops with an odd number of edges. Such topological situation
occurs on many other lattices with a finite clustering coefficient (e.g., square lattice with the first- and
second-neighbor interactions), in some curious lattice structures [e.g., the Cairo pentagonal lattice studied
by Rojas et al. [256]] that includes five-edge loops.
On the contrary in social networks the length of loops may be either odd or even, consequently, the
frustration is unavoidable on these structures for the anti-coordination games.

?

?

Figure 28: Two typical topological conditions yielding frustration. The left panel shows three players with two strategies
(closed and empty bullets) located on a triangle for pairwise anti-coordination games denoted by double lines. The question
mark refers to the equivalence between the two strategies for the third player. The right panel shows four players on a square
network who play pairwise coordination (simple edge) or anti-coordination (double edge) game with each other as denoted.
For the given three-player strategy profile the fourth player has two equivalent strategies.

The other source of frustration is related those models where the coupling constants are chosen to be
+J or −J at random as it is illustrated in the right panel of Fig. 28. Some consequences of the frustration
are well illustrated in Fig. 29 where one can observe six different domains representing the chessboard and
anti-chessboard arrangements of two of three strategies on the square lattice for games equivalent to the
repulsive three-state Potts model. Berker and Kadanoff [257] have shown that the typical size of these
53

Figure 29: (Color online) Typical snapshot for the repulsive three-state Potts model on the square lattice at low noise levels.

domains (or the correlation length) increases algebraically when the noise level K is decreased. Similar
features were reported previously by Wannier [255] for the Ising model on a triangular lattice.
A direct consequence of the frustration can be the high level of degeneracy of states having maximal
potential. If the number of these degenerate states increases with N exponentially then the specific entropy
remains finite in the zero noise limit, contrary to the third law of thermodynamics. This discrepancy
vanishes if the games are not equivalent, as it occurs in social systems. On the contrary, if we study a
system with many edges of small potential differences in the dynamical graph, then the systems may reach
the thermodynamically stable state faster.
7.10. Effects of randomness
For many multi-agent systems we cannot assume equivalent games representing the interactions among
the participants. In Sec. 6.1 it is shown that if the interactions are limited to symmetric 2 × 2 games then
the potential of this multi-agent system can be mapped onto an Ising model where the values of Jxy and
hx vary within a wide range. The effects of these types of randomness have been studied for four decades
and the results are documented in the literature of spin glasses. The experimental investigations of these
systems were first motivated by the unusual magnetic behavior of some metal alloys (e.g. AuFe and CuMn)
[258]. From a theoretical point of view these phenomena demanded the development of new concepts and
approaches. Comprehensive descriptions of the models, methods, phenomena, and perspectives are given
in the books by Mézard et al. [259] and by Stein and Newman [260]. For most of the investigations the
effects of randomness (occurring in Jxy and hx ) are considered separately. Exceptions are represented by
the one-dimensional random Ising models [261]. Recent trends in the research of evolutionary game theory
offer further possibilities for the introduction of randomness via the consideration of personal features and
the wide scale of connectivity structures. Here we survey only a few phenomena that seem to be important
for information processing [262], decision theory [263], social [260] and biological [264] systems.
Spin glasses are systems combining quenched randomness and frustration. For the Ising type spin glasses
the parameters Jxy and hx are random variables and are characterized by some probability distribution
functions. The accurate mathematical form of the probability distribution of the Jxy values is not important
in general. For technical reasons the Gaussian distribution is chosen with a mean value of zero (denoted as
2
iiJ = 1 where hh· · ·iiJ refers to averaging over all pairs). An alternative approach was
hhJxy iiJ = 0 and hhJxy
suggested by Domany [265] for the so-called ±J model where Jxy = J (Jxy = −J) is chosen at random with
a probability p (1 − p). Here we remind the reader that hhJxy iiJ > 0 does not guarantee the ferromagnetic
order in the low noise limit in the absence of magnetic field (hx = 0). When investigating the ±J model on
a square lattice Domany [265] has explained the existence of the ferromagnetic order in the low noise limit
if p > pc (pc ≃ 0.83 on the square lattice). It was found that the percolation of unfrustrated squares was
responsible for the ferromagnetic state and the critical point (pc ) is associated with the adequate percolation
threshold value.
54

The spin glass model was introduced and studied by Edwards and Anderson [266] for a uniform Gaussian
2
distribution (hhJxy iiJ = 0 and hhJxy
iiJ = 1). In agreement with the experimental results this model has
indicated the presence of a ”spin glass” phase at low noise levels (K < Ksg ). The main characteristic of
the spin glass phase is the existence of a large number of free-energy valleys that are inaccessible from each
other in the limit N → ∞. Within the spin-glass phase the average magnetization is zero and there are
ferromagnetic domains with different sizes and orientations. During the evolution the system remains in the
vicinity of one of the given free-energy valleys similarly to the ferromagnetic phase where only two (ordered)
microscopic states are distinguished. For the quantification of the remanence of these spin arrangements
Edwards and Anderson [266] have introduced an order parameter which is similar to the one-site two-time
(2)
(1)
correlation function characterizing the coincidence of the ”average” spin directions hσx i and hσx i in the
vicinity of times t1 and t2 which are far from each other. If the system remains in the same free-energy valley
(1)
(2)
then hσx i = hσx i = hσx i and the spin glass phase can be characterized by the so-called Edwards-Anderson
order parameter:
1 X
qEA =
hhσx i2 i J .
(134)
N x
At high temperatures qEA = 0 because each spin can flip into the opposite state within a short time.
qEA = 1 refers to frozen patterns at K = 0. Deviations from qEA = 1 arise from thermal fluctuations and
frustration.
A more detailed insight into the nature of spin glasses is provided by considering an exactly solvable model
introduced by Sherrington and Kirkpatrick [267]. It is an Ising model on a complete network (interactions
exist between all spin pairs), therefore this model could be well investigated by the mean-field theory using
the replica trick. For the analytical analysis of this model, [267] [268] have justified the phase transition at
Kc = 1 from the paramagnetic state to the spin glass phase when decreasing the temperature and explained
the magnetic behavior observed in experiments.
In order to study the inherent relationship between two glassy states Parisi [269] has suggested using a
more complicated order parameter:
1 X
hσx iα hσx iβ .
(135)
qαβ =
N x

that quantifies the average overlapping between two frozen spin patterns α and β for a given randomness in
Jxy . Assuming that the state α takes place with a probability W α for a given randomness, Parisi [269, 270]
introduced a probability distribution of overlap values as
X
P (q) =
W α W β δ(q − qαβ ).
(136)
α,β

It is generally assumed that qαα is independent of α in the limit N → ∞. In that case, qαα = qEA and P (q)
exhibits two Dirac-delta peaks at ±qEA , referring to the global spin reversal symmetry of the Ising model.
For the Sherrington-Kirkpatrick model, Parisi [270, 271] has shown the hierarchical (tree-like) structure in
the overlapping qαβ for a given randomness in Jxy and discussed the general features of P (q) when averaging
over the randomness in Jxy . It was found that hhP (q)iiJ > 0 if −qEA < q < qEA .
For more realistic spin glass models with short range interactions, basically different results have been
reported by Newman and Stein [272], Middleton [273], Billoire et al. [274] who studied the averaged overlap
probability distribution. The differences are related to the number of energy valleys, the consequences of
spatial structure and the absence/presence of frustration. At the same time these investigations raised many
new questions. For a brief survey of the differences and recent achievements we suggest reading the recent
reviews by Newman and Stein [275] and by Read [276].
The effect of random-field hx on the thermodynamical behaviors of the d-dimensional ferromagnetic Ising
model was investigated by Imry and Ma [277], Villain [278], Imbrie [279], using different approaches. In
these investigations Jxy = J, hhx i = 0, and hh2x i = h2R are chosen where the mean variance hR measures the
randomness. The complexity of questions related to the existence of ferromagnetic phase in the low noise
limit is well reflected by the facts that the initial studies lead to controversial results. The systematic Monte
55

Carlo calculations [280, 281, 282, 283] have indicated the ferromagnetic phase in the presence of a weak
randomness at low temperatures if d ≥ 2, otherwise there is no average magnetization in the presence of a
random field. In other words, the paramagnetic to ferromagnetic critical phase transition can occur if hR
does not exceed a threshold value dependent on the lattice structures. Very recently Shrivastav et al. [284]
have investigated the morphological properties of the spin arrangement in the two- and three-dimensional
systems in the low noise limit and reported power law behaviors in the correlation functions. In that case
the paramagnetic phase possesses spin glass order qEA > 0, that increases when decreasing the temperature,
although the system has only one paramagnetic state.
Finishing this section we emphasize that the evolutionary potential games describing biological and
social systems demand the systematic investigation of the effects of additional randomness that can occur
in the connectivity structure, the local dynamical rules, and even in the number of strategies. On the other
hand, the characteristic features of the spin glasses may be suppressed when slow variation is allowed in the
parameters characterizing the randomness.
8. ORDERING PROCESSES
A typical two-dimensional ordering process in the Ising model from the random initial distribution
towards the equilibrium state was illustrated previously in Fig. 15. This process can be observed for a fixed
noise level below its critical value Kc and it has some universal features. Namely, two equivalent types
of ordered strategy arrangements form a domain structure that is topologically similar to the cases where
islands are in lakes located within larger islands located in larger lakes etc. for the infinitely large systems.
This pattern can be characterized by the average distance l(t) between two neighboring domain walls (along
the horizontal or vertical cross-sections) that give a time dependent contribution to the equilibrium average
potential. Namely, after a√relaxation time, Ueq − U (t) = α/l(t) where α depends on the pair potential and
noise level K, and l(t) ∝ t as long as l(t) < L.
Figure 30 shows two typical Monte Carlo results obtained when the system with hawk-dove parameters
is started from a random initial state on a square lattice and the time-dependence of the average potential
[U (t)] is recorded during the evolution for two noise levels. Despite the large system size (L = 4000) the
1

Ueq-U(t)

0.1

0.01

0.001
1

10

100

1000

10000

100000

time [MCS]
Figure 30: Log-log plot of averaged Ueq − U (t) vs. time for K = 0.1 (squares) and K = 0.34 (diamonds) at T = 1.5 and
S = 0.2. The dashed line shows the slope (-1/2) characterizing the theoretical prediction.

functions U (t) are decorated by fluctuations with an amplitude increasing with time. These undesired
fluctuations are suppressed by averaging U (t) (at t = ti ≃ 2i/2 ) over time intervals 0.8ti < t < 1.2ti for the
clear illustration of the asymptotic behavior mentioned. Notice, that it takes a longer time to achieve the
asymptotic behavior when K approaches the critical point due to the critical slowing down as indicated by
diamonds in Fig. 30.
56

Different approaches have been developed to describe the above-mentioned time-dependent processes
that remain valid also for the homogeneous three-dimensional systems. All the relevant features are well
investigated by continuum description in terms of coarse-grained order parameter field [for detailed discussion
we suggest consulting the reviews by Hohenberg and Halperin [285], Langer [286], and Bray [287]]. For this
approach the systems are described by a scalar order parameter Φ dependent on time and continuous space
that can be considered as average magnetization (or strategy density) over a small region.
Additionally, the motion of interfaces can be described by geometrical approaches for both the two- and
three-dimensional systems as it is detailed by Brakke [288], Brower et al. [289], and Goldstein and Petrich
[290] (with further references therein). For these differential geometric descriptions the two-dimensional
system is characterized by a set of closed curves representing the interfaces in the corresponding two-color
map. The evolution of these curves is determined by a differential equation taking into consideration the
average velocity of the interface depending on its local curvature, direction, and additional symmetries
coming from the microscopic dynamical rules. For example, the reduction of the length of interfaces via the
so-called curvature driven interface evolution (for a very recent geometrical survey see the work by Garcke
[291]) can explain different domain growing phenomena (l ∝ tα with α = 1/2, 1/3, or 1/4). Additionally,
these approaches can describe a wide variety of interfacial instabilities occurring in solid state systems. On
the other hand, the applicability of this method is limited to systems possessing one type of interfaces.
In comparison to the spatial systems the final ordered strategy arrangement is formed significantly faster
on small-world connectivity structures due to the absence of large distances. For the demonstration of this
phenomenon we have performed MC simulations for an evolutionary hawk-dove game on a random bipartite
regular graph with a degree of 4. The system started from a random initial state and the order parameter,
the average payoff and potential were recorded after each MC steps performed at a noise level below its
critical value. During the first steps the sharp increase of potential (see Fig. 31) refers to the formation of
ordered microdomains. Within this period the sublattice order parameter remains zero because of the large

U(t)/N

4.0

3.0

2.0
0

50

100

150

time [MCS]
Figure 31: Average potential as a function of time during the sublattice ordering process on bipartite random regular graph
for a hawk-dove game at T = 1.5, S = 0.5, K = 0.5, and N = 4 ∗ 106 . MC data of four independent runs are illustrated with
different types of lines.

number of microdomains of two types. The number of domains decreases gradually and after some time the
size of the largest domains becomes comparable to the diameter of the given graph (∝ ln N ). Thereafter,
the largest domain conquers the system. The parallel curves in Fig. 31 refer to similar scenarios and the
randomness influences dominantly the time when ruling domain emerges. Evidently, on smaller systems
the above behavior is disturbed by the stochastic events occurring both in the generation of the random
networks and in the evolution of strategy distribution.
8.1. Evolution in the limit K → 0
The pattern evolution in the Ising model on different lattices and graphs has been studied for several
years in the zero noise limit [292]. This particular case exhibits some curiosity.
57

For example, in the one-dimensional Ising model the long-range order can also be formed in the system
if it is started from a random initial state while the evolution is controlled by the Glauber dynamics in the
limit K → 0 for h = 0. In that case the system becomes equivalent to the one-dimensional voter model
[293, 187] and the interfaces (separating the opposite domains) move randomly. If two interfaces collide
then both are annihilated. Finally the system evolves into one of the homogeneous states with a probability
dependent on the initial magnetization. The average domain size increases in time as l(t) ∝ t1/2 [294].
In general, the l(t) ∝ t1/2 scaling law is valid for the two- and three-dimensional lattices, too. However,
in several trials the system evolves into a frozen state [295, 296] and these events modify the long-time
behavior. The bottom snapshots in Fig. 12 show an example when rectangular boxes of the preferred phases
are frozen into the opposite phase if the system is started form a random state being close to the ordered
opposite structure. The application of the periodic boundary conditions may also result in frozen patterns
in the finite systems. Spirin et al. [296] have reported that for about one third of the trials in the twodimensional lattice the system evolves into a poly-domain state where all the interfaces are horizontal (or
vertical). For most of the cases only two strips are formed. It is reported furthermore that the number of
frozen states is larger for d = 3.
Recently Biswas and Sen [292] have studied the Ising system on a random network created from the
one-dimensional lattice by adding new links into the connectivity structure. As a result the lattice sites
have different degrees and for some constellations these irregularities were capable of blocking the domain
growing processes, independently of the details of the generation of random networks. On the other hand,
the freezing disappears in the limit N → ∞ for densely connected networks [297].
The appearance of frozen patterns is expected for the n-strategy games (or Potts models) and also for
systems where the number of neighbors is increased.
8.2. Interfacial phenomena and rearrangement through nucleation
Many relevant phenomena for the ordering or reordering processes can be well interpreted by considering
microscopically the evolution of an interface separating two ordered phases for the two-dimensional ferromagnetic Ising model. Figure 32 shows a horizontal interface between the up- and down-spin ordered phases
that remains stable at K = 0 even in the presence of a weak magnetic field. Due to the rare stochastic
events at low noise levels, one of the spins may reverse along the interface as denoted by the middle panel
in Fig. 32. The ferromagnetic nearest neighbor interactions enforce this spin to flip back, which represents
the typical behavior. Sometimes, however, before the reconstruction of the smooth interface one of the
neighboring spins may also reverse thus forming a two-spin cluster.
The appearance of a two-spin cluster along this interface results in a new situation when the spins at
sites x and y in Fig. 32 have similar environments, namely, there are two up-spins and two down-spins in
their neighborhood and the preferred spin reversal is determined by the magnetic field. As a result this
two-spin cluster can be considered as a nucleon from which the expansion (or growing) of the preferred state
can start. The direction of the motion of steps and also its average velocity can be quantified by comparing
the probabilities of spin reversals at sites x and y in the third panel of Fig. 32. The quantitative analysis
justifies that the average vertical velocity is proportional to the magnetic field (if |h| ≪ 1). Throughout

x y

Figure 32: Consecutive steps in the evolution of a horizontal interface separating two ordered strategy arrangements on a
square lattice.

these consecutive elementary steps the system will evolve into the thermodynamically stable ferromagnetic
state if 0 < K < Kc .
58

The average vertical velocity of the above horizontal interface depends on two factors: the average
horizontal velocity of the steps and the frequency of these steps along the interface. The second quantity
depends on time and also on the nucleation rate characterizing the probability of the appearance of a
sufficiently large nucleon. If the nucleation rate is low, then the interfaces are composed of large horizontal
and vertical segments, otherwise the domain pattern is almost isotropic.
Similar phenomena can be observed along the interfaces separating the equivalent anti-ferromagnetic
domains. In that case the presence of the homogeneous external field h modifies the interface as it is
illustrated in the snapshots of Figs. 14, whereas the the average velocity of the interface is zero. At the
same time, the application of a staggered magnetic field prefers one of the ordered spin arrangements to the
opposite one and results in an average velocity proportional to hs (if hs ≪ 1).
In the above process the appearance and expansion of the one-dimensional preferred nucleons play
the crucial role in the evolution towards the final stationary state. Similar mechanism can be observed
in d-dimensional lattices when the appearance of sufficiently large islands of the preferred ordered phase
is necessary to initiate the transition from an ordered phase to the thermodynamically stable final spin
arrangement. That happens when we wish to reverse the direction of magnetization by the application of
an external magnetic field. In thermodynamical systems, the formation of the sufficiently large nucleon of
the preferred phase is supported by a suitable series of stochastic elementary steps that may occur rarely.
Sooner or later, however, some sufficiently large nucleons appear and catalyze the transition towards the
stable phase via a domain growing process. The resident time in the meta-stable state(s) may be extremely
long, especially at low noise levels. These phenomena are well investigated in a wide scale of physical systems
and exploited in many products of high technology.
In two-strategy evolutionary potential games the growth of the C domains on a square lattice can be
characterized by the average velocity v of the moving step shown in Fig. 32. If logit rule controls the
evolution then
eux (C)/K
euy (D)/K
v = u (C)/K
−
.
(137)
e x
+ eux (D)/K
euy (C)/K + euy (D)/K
Due to the similar strategy arrangements in the neighborhood the denominators are equal and
v=

e2(1+S)/K − e2T )/K
e2(1+S)/K + e2T )/K

(138)

in the social dilemma notation. As a result, within the region of stag hunt game the condition v = 0 defines
a straight line (S = T − 1) on the T − S plane separating homogeneous cooperation (sx = C) and defection
(sx = D) regions in the low noise limit (in agreement with the phase diagram plotted in Fig. 16).
8.3. Interfacial phenomena in three- and n-state systems
During evolutionary processes the interfacial phenomena can play crucial roles in the n-strategy (n > 2)
systems, too. First we show what happens during the domain growth if the coordination type interaction
between strategies 1 and 2 is extended by additional (neutral) strategies. Figure 33 illustrates the formation
of two homogeneous domains (with strategy 1 and 2) if A = d(1, 2) [see the definition (41) at n = 5] if the
two dimensional system is started from a random initial for logit rule at a noise level (K = 0.4). For this
low noise level the strategies 3, 4, and 5 can occur very rarely inside the homogeneous domains. At the same
time the mentioned strategies will be selected dominantly by the players located along the interfaces where
the opposite effects of neighbors (with strategies 1 and 2) are balanced (see the sites x and y indicated in the
right plot of Fig. 32). In the present system the appearance of the additional strategies along the interfaces
does not modify the general features of domain growing process.
If the interactions are dominated by d(1, 2) then the equivalence between the strategies 1 and 2 is
evidently broken by the presence of self-dependent components and also by the additional coordination type
interactions. More precisely, the preference of strategy 1 (or 2) depends on the value of γ1 − γ2 and also on
the strengths of the components d(1, 3) and d(2, 3). The competition between these components may result
in different phase transitions as it is discussed by Vukov et al. [208] in a three-strategy evolutionary game.
59

Figure 33: (Color online) Two homogeneous domains of strategies 1 (white) and 2 (black) are growing in the two-dimensional
system if the interaction is defined by A = d(1, 2) for n = 5. During the evolutionary process the strategies i = 3, 4, and 5
(denoted by red, blue and green boxes) occur dominantly at the steps of interfaces separating the white and black territories.

For another example we mention the attractive n-state Potts model evolves towards one of the homogeneous ordered states throughout a domain growing process at low noise levels, if the system is started from
a random initial state.
A similar phenomenon can also be observed for some spatial coordination games [31]. The left snapshot
of Fig. 34 illustrates the spatial distribution of three strategies during the domain growing process in a
system where A = d(1, 2) + d(2, 3) + d(1, 3) for n = 3]. The right hand snapshot of Fig. 34 shows similar

Figure 34: (Color online) Typical strategy distributions on a square lattice for two types of the three-strategy coordination
games during the domain growing process after 500 MCS if the system is started from a random initial state and the evolution
is controlled by logit rule at low noise levels (K ≃ 0.5Kc ).

domain growing process in a system where the payoff matrix A′ is obtained from A by exchanging its first
and second rows. As discussed in Sec. 3.1 and [31] there are two other equivalent systems that can be
transformed into each other by exchanging two strategy labels in one of the sublattices. A similar symmetry
is behind the equivalence of the ferromagnetic and anti-ferromagnetic Ising model on bipartite graphs.
In two-dimensional spatial systems the geometrical features of these domain patterns differ significantly
from those occurring in the two-state systems, where the interfaces form closed loops typically in the infinitely
large systems (as mentioned in Sect. 8). For n = 3 one can distinguish three types of interfaces that can
form closed loops or represent a planar network with three-edge vertices.
In spite of the striking geometrical differences the average domain size increases with the square root of
time (l(t) ∝ t1/2 ) as reported by Grest et al. [298] and the geometrical features of these patterns become
60

similar on the scale of l(t) as it is observed for the Ising model and other field theoretical models surveyed
by Bray [287].
In the present system, the existence of the third strategy does not influence the behavior of interfaces if
the point defects are distributed sparsely. If the attractive Potts model includes a magnetic field favoring one
of the homogeneous states then one can observe the expansion of the favored domains along their interfaces
with an average velocity proportional to the magnetic field.
A similar behavior is expected for three-strategy potential games if the payoff matrix g(8) is weakly
disturbed by additional self-dependent components (39). In those cases the difference between the corresponding γi values will determine the direction (and also the average velocity) of invasions between two
”homogeneous” domains. For example, this mechanism results in the prevalence of strategy 1 in the final
stationary state if γ1 > γ2 , γ3 .
The right hand snapshot of Fig. 34 illustrates a system that is not yet studied systematically within the
framework of Potts models. In the latter evolutionary game one can observe a homogeneous domain formed
by strategy 3 and two equivalent chessboard like ordered strategy arrangements of the strategies 1 and 2. The
most striking feature of this game is related to an inherent symmetry that we have discussed previously when
justifying the equivalence of the ferromagnetic and anti-ferromagnetic Ising models on bipartite networks
(see Sec. 7.4). According to the generalization of the mentioned method, game g(8) on a bipartite network
becomes equivalent to those where the pair interactions are defined by g(6) if the players in sublattice Y
exchange the labels of their first and second strategies (1 ↔ 2). The latter transformation is equivalent to the
exchange of the first and second row of the payoff matrix. Due to the mentioned relation the three domains
are equivalent on the square lattice and after a domain growing process one of these ordered structures will
prevail in the finite systems. When increasing the noise level K this system undergoes an order-disorder
critical phase transition belonging to the universality class of the three-state Potts model.
One can generate two additional potential games with payoff matrices obtained from g(8) by exchanging
the labels 1 ↔ 3 or 2 ↔ 3 for the players staying in sublattice Y . The resulting games are similar to g(6).
These relatives of the Potts model can be constructed as suitable linear combinations of three elementary
games (g(6), g(7), and g(8) [31]. It turned out that the corresponding three-dimensional subset of games
can be considered as a generalization of the Potts model. Here we have to emphasize that the additional
self-dependent components are not capable of preferring one of the sublattice ordered two-strategy structures
to its anti-pattern.
The exploration of the three-strategy symmetric potential games is not complete. Even more complex
behavior is expected for n > 3 when the number of interfaces as well as the types of vertices increases with
n. The preliminary results have indicated the dominance of three-edge vertices that follows a complicated
transition/annihilation rule [299]. The consideration of nonsymmetric games will allow us to study the effect
of those types of self-dependent components that distinguish the chessboard and anti-chessboard arrangements of two strategies, as it is done when applying a staggered magnetic field to the anti-ferromagnetic
Ising model.
In the above-discussed models the average motion of the invasion fronts is driven by the increase of
individual payoffs that is quantified by the increase of U in the thermodynamic potential Φ (82) if K → 0.
In the maximization of Φ, however, the high entropy of the disordered phase, especially for a large number
of strategies, can become the leading term at sufficiently high values of K.
Figure 35 illustrates a domain growing process on a square lattice from one of the ordered phases (here
sx = 1) to the disordered strategy arrangement if the interaction is described by d(1, 2) for n = 50 at a noise
level K = 0.52 > Kc (50) = 0.512(2). The process begins with a nucleation procedure that is followed by the
expansion of the disordered territories where all the strategies are present with approximately equivalent
probabilities.
Here the evolution is also controlled by the logit rule, therefore we can estimate the average velocity v
of a step along the interfaces in the same way as it is described in Sec. 8.2. Neglecting the appearance of
strategy 2 the value of v can be approximated as
v≃

e2/K
e2/K + n − 2

−

61

n−2
.
e2/K + n − 2

(139)

Figure 35: (Color online) Three consecutive snapshots at times t = 200, 1000, and 3000 MCSs (from left to right) show a
domain growing process when the (white) homogeneous spatial strategy distribution (sx = 1) transforms into the disordered
phase composed of n = 50 strategies (distinguished by different gray scales).

Accordingly, the disordered phase expands at the expense of ordered phase if v < 0, that occurs if K >
2/ ln (n − 2) for sufficiently large values of n when the K-dependence of strategy frequencies exhibits a firstorder phase transition. The criterion v = 0 gives us an estimation for the critical point, Kc (n) = 2/ ln (n − 2),
that agrees very well with the Monte Carlo result given above for n = 50.
The latter result implies that the high-entropy phases can occur for any noise level if n is sufficiently
large. Here it is worth mentioning that similar arguments justify the stability of high-entropy alloys at room
temperatures. Recently the high-entropy alloys are studied progressively and considered to be a promising
family of materials with a wide scale of applications [300, 301, 302].
Anyway, the average velocity of an interface can be determined numerically if the Monte Carlo simulations
are started from artificial initial state where the competing phases are represented by two domains with equal
sizes. Using this method one can evaluate the phase boundaries in the phase diagrams more accurately
[303, 304], particularly if the first order transition is accompanied with a hysteresis [305] or sensitivity to
the initial state [306].
8.4. Slow relaxation in random systems
Up to now we have mainly discussed the stationary states of the systems (in the limit N → ∞). In
general, homogeneous systems evolve towards the stationary states exponentially if the state is weakly
perturbed. We have mentioned two exceptions when the homogeneous system reaches the final state more
slowly. In the first case the system evolves form a random initial state into one of the ordered arrangements
√
through a domain growing process and the average domain size (or correlation length) increases with t as
detailed above. The second case occurs at the critical point where system behavior is dominantly controlled
by the fluctuations and results in a power law decay in most of the quantities. Now we briefly discuss the
slow relaxation processes observed in the Griffiths phase of the random Ising systems.
The slow (nonanalytic) relaxation of the magnetization in the paramagnetic phase of a random ferromagnetic Ising model at h = 0 was reported by Griffiths [307] who studied a diluted Ising model on a lattice where
a portion of the lattice sites are not occupied by Ising spins [308]. Subsequent analyses have indicated the
presence of Griffiths phase in many other random Ising models between the paramagnetic and ferromagnetic
(or spin-glass) phases. According to the investigation of different models the one-site two-time correlation
function [defined in Sec. 8] is found to have a ”stretched-exponential” form, g(0, t) ≃ exp[−(t/τ )κ ] with
0 < κ < 1, depending on the spatial dimension and other details of the system [309, 310, 311, 312].
The related spatial patterns assume the existence of sparse and large ordered domains in the random
environment. The thermalization (spontaneous reversal) of these sparse domains is very slow because it
requires a long sequence of coherent flipping over a large volume. According to this picture the timedependence of magnetization (or any order parameter) can be approximated as
Z ∞
m(t) =
w(τ ) exp[−t/τ ] dτ
(140)
0

62

with a suitable choice of the weight function w(τ ). Noest [313, 314] has shown that if the relaxation time
increases exponentially with the size n of a compact cluster (τ ∼ exp[an]) and the probability of such clusters
decreases exponentially with n, then the leading term of the asymptotic behavior of m(t) can be estimated
as
m(t) ∼ t−θ
(141)

where θ (θ > 0) depends on a and on other parameters within the Griffiths phase. It is emphasized that
similar behavior is reported for several other systems, e.g., stochastic cellular automata [314] and contact
processes with quenched disorder in the environment [315]. Today the contact process [316] is considered as
the paradigm of systems where the extinction of a species/strategy exhibits a critical transition that belongs
to the directed percolation universality class [317]. For a survey of the main features of this critical transition
we suggest consulting the review by Hinrichsen [318]. In the latter system the quenched randomness modifies
also the system behavior at the critical point [319]. The presence of Griffiths phase and its consequences
are described by Muñoz et al. [320] for the contact process on complex networks.
The occurrence of the Griffiths phase in the contact process has implied algebraic extinction of a strategy
in many evolutionary games where the evolutionary rule is based on imitation in spatial systems with
quenched disorder [321]. In most of the evolutionary games with quenched randomness, however, the
appearance of Griffiths phase is not investigated although it can cause incorrect numerical data in the
vicinity of the critical point(s).
The above theoretical picture supposes that the relaxations of the domains are independent of each other
(i.e., the rare events are not organized hierarchically). This feature simplifies the numerical analysis of these
systems as the Monte Carlo simulations can be performed simultaneously on many ”small” systems. In the
opposite cases, when the models involve hierarchically constrained dynamical processes [309], more complex
finite-size analyses are required.
At the end of this section we underline the relevance of the Griffiths phase in the evolutionary games
modeling biological or social systems where the quenched randomness is assumed naturally [260]. For the
numerical analysis of these systems in the Griffiths phase we have no chance to achieve the final stationary
state due the the slow algebraic relaxation processes. It means, on the one hand, that in the Griffiths phase
the final stationary quantities should be determined by extrapolation of the asymptotic behavior. On the
other hand, for the interpretation of the experimental and numerical data we should consider the fact that
the system has not achieved its equilibrium state.
The Griffiths phase represents technical difficulties in numerical simulations that can be avoided by
introducing slow variation in the randomness that is also a natural ingredient of biological and social systems.
The relevant differences between the quenched and temporal randomness are detailed by [318] for the contact
process.
9. DEVIATIONS FROM THERMODYNAMICAL EQUILIBRIUM

In the absence of potential the existence of Boltzmann distribution becomes meaningless and we cannot
apply the results of equilibrium statistical physics and thermodynamics. Additionally, the validity of thermodynamics is dropped when applying an evolutionary rule that breaks the detailed balance and drives the
system far away from the Boltzmann distribution, as happens, for example, in the imitation-based dynamics
used frequently in many previous investigations. For some types of coevolutionary games the absence of
the fixed connectivity structure, the possible changes in personal features and spatial location raise many
additional questions whose analyses go beyond the scope of the present work.
In the following sections we discuss briefly some effects of the matching pennies and rock-paper-scissors
games that can be studied in multi-agent evolutionary games even for the application of logit rules. The
discussion of these games is unavoidable because of their important role in the subgames of any n × n matrix
games, which can affect the system’s behavior significantly.
9.1. Effects of matching pennies
The matching pennies game, defined by f ′ (8) in its bimatrix form (53), represents the simplest cyclic
interaction. For a two-player evolutionary game with logit rule the unsatisfied player reverses her strategy
63

with a high probability dependent on K, while the opposite transitions become rare. Thus this interaction
breaks the detailed balance and can be considered as a microscopic force inducing cyclic variations in
the systems. The effect of this interaction can be quantified by the probability current(s), measuring the
difference in the frequency of forward and backward transitions along the directed edges of the flow graph
(see Fig. 8). This current is uniform along the four edges in the stationary state of this stochastic process.
The induced circular probability current creates observable variations in the probability of the strategy
profiles. For the illustration of this phenomenon we discuss a system where a weak matching pennies
component is added to the payoff of a hawk-dove game. The variations in the probabilities are illustrated
in Fig. 36. In this figure the height of the dark columns denotes the probability of each strategy profile in

(0,0)

(0,1)

(1,0)

(1,1)

Figure 36: Probabilities of the four strategy profiles are proportional to the height of the dark (ε = 0) and white (ε = 0.1)
columns for a two-person hawk-dove game if it is extended by a matching pennies component with a strength of ε. The arrowed
gray circle denotes the probability current loop induced by the matching pennies game.

the stationary state when G = G(sd) as defined by (59). For the given parameters (T = 1.4, S = 0.3, and
K = 0.3) p(1, 1) < p(2, 2) whereas p(1, 2) = p(2, 1). If the latter game is modified by adding a weak matching
pennies component to the payoffs (quantitatively G = G(sd) + εG(mp) with ε = 0.1) then the appearance of
probability current is accompanied with a striking variation in the stationary state. The largest increase of
p(2, 1) can be interpreted as the consequence of a congestion phenomenon. Accordingly, for the maintenance
of the circular probability current, the lowest value of p(1,1) plays the role of a narrower bottleneck that
creates an increase in p(2, 1) to ensure uniform probability current through the four-edge loop. At the same
time the value of p(1, 2) is decreased, that is, the presence of the matching pennies component destroys the
equivalence of the two Nash equilibria.
In the multi-agent version of this evolutionary game on the square lattice, the above microscopic effect
occurs for each interacting neighbor and affects the macroscopic behavior. This extension of the models can
be performed for those lattices that can be divided into two sublattices (X and Y , where the two types of
players are located separately). As a result of this breaking of the original symmetry, one of the sublattice
ordered strategy arrangements can be preferred in the low noise limit. Evidently, the preference is reversed
with the sign of ε. Furthermore, the preference is also reversed if we consider the upper half part of the
hawk-dove game, where S > (T − 1) and p(2, 2) < p(1, 1), because here the strategy pair (2, 2) plays the
role of the narrower bottleneck in the circulation. In fact, the effect of the matching pennies component is
similar to the application of a suitable staggered magnetic field in the anti-ferromagnetic Ising model.
Along the line S = (T − 1) in the parameter space, the above effect does not work because here p(1, 1) =
p(2, 2). In these systems the presence of the matching pennies component does not destroy the universal
features of Ising type critical transition [322], whereas the value of Kc is reduced (proportionally to ε) if its
strength does not exceed a threshold value. In the latter case the pair interaction belongs to the classes of
ordinal potential games, because weak contribution of the matching pennies is not enough to change the
edge directions in the flow graph.
In non-equilibrium systems the breaking of detailed balance can be well quantified by evaluating the
entropy production I (for a survey see [41]). This quantity is constructed from the frequencies of the
64

forward and backward transitions between states s and s′ if these transitions are allowed by an elementary
step in both directions. Now the random consecutive elementary steps consist of single site strategy changes
from (sx , s−x ) to (s′x , s−x ) appearing with a frequency W (sx → s′x ) in the stationary state. The entropy
production summarizes the contributions of the forward and backward transitions for each possible transition
pair in the following way:
I=

1 X
W (sx → s′x )
.
[W (sx → s′x ) − W (s′x → sx )] ln
2 s ,s′
W (s′x → sx )

(142)

x x
s−x

Notice that this quantity is always positive (I > 0) except the case I = 0 when the conditions of detailed
balance are satisfied, i.e., if W (sx → s′x ) = W (s′x → sx ) ∀sx , s′x , s−x . Despite the large number of transitions
in lattice systems the entropy production can be well estimated by recognizing that the transition frequency
W (sx → s′x ) depends dominantly on the close neighborhood of player x, who modifies her strategy, if the
dynamics is controlled by short range interactions. Besides it we can exploit the translation invariance of
the lattice system. As a result the specific entropy production (I/N ) can be estimated by considering the
transition frequencies at any site x for all possible strategy configurations in its close neighborhood.
For example, during the Monte Carlo simulations on a square lattice one can determine the transition
frequencies sx → s′x for all the 24 = 16 possible strategy configurations of the four nearest neighbor sites and
also for the cases when 28 = 256 configurations are distinguished on the first- and second neighbor sites. In
this way we can deduce two approximate results for the specific entropy production (I/N ) and comparison
of them indicates the relevance of the second neighbors although they do not influence directly the transition
in the present models. Evidently, the larger the neighborhood, the more accurate is the present approach
(for a more detailed description of this approach see [92]).
Figure 37 shows the Monte Carlo results for the specific entropy production when varying the noise level
for different strengths of the matching pennies component. Here the closed symbols represent data obtained
when only the first neighbors are taken into consideration in the identification of s−x . Notice that the latter
approximate data are close to those we obtained when a larger neighborhood (the first and second neighbors
of player x) is used for the characterization of s−x . The small differences between the two sets of data
0.6
0.5

I/N

0.4
0.3
0.2
0.1
0
0

0.5

1.0

1.5

2.0

K
Figure 37: Specific entropy production as a function of K for evolutionary game with G = G(sd) + ǫG(mp) pair interactions
on the square lattice if T = 1.4, S = 0.3, and ǫ = 0.1 (open diamonds and bullets), 0.175 (open boxes and closed diamonds),
0.25 (open circles and closed boxes). The open symbols denote data obtained for the larger neighborhood.

justify the reliability of this approach. Notice furthermore another general feature: I/N vanishes in the
limit K → ∞ when only the randomness controls the players’ decisions.
Figure 37 illustrates that the force of ordering (strength of hawk-dove component) blocks the strategy
reversals and also the breaking of detailed balance in the low noise limit if ε is less than a threshold value,
more quantitatively, |ǫ| < |ǫth | where |ǫth | = 1/2 min(|T − 1|, |S|). In the opposite limit, the specific entropy
production diverges if K → 0 and we can observe a remarkably different behavior.
65

The divergency of I/N in the low noise limit is characteristic to systems where cyclic dominance controls
the system behavior and prevents the formation of ordered strategy arrangements. A similar divergency
occurs in systems where a finite portion of the transition pairs becomes unidirectional. If the evolution is
defined by only the matching pennies component in a spatial evolutionary game then the visual observation
indicates random strategy distribution on a square lattice. The quantitative analysis, however, has clearly
indicated weak correlations between the second and third neighbors [322] that evidently vanish in the high
noise limit.
9.2. Effects of rock-paper-scissors game
If the multi-agent evolutionary games are composed of equivalent players with three strategies, then the
rock-paper-scissors component is responsible for the deviation from the potential games. The rock-paperscissors game itself creates a weakly correlated random distribution of the three strategies on a square lattice
if a logit rule controls the evolution. The three strategies are present with the same probability (1/3) and the
numerical investigations indicate a weak spatial correlation that is similar to those found for the matching
pennies game. The latter analogy implies that the alternation of the three strategies on each site reflects
relevant breaking of the detailed balance, particularly in the limit K → 0 when I/N diverges.
Contrary to the two-strategy games with a matching pennies component, the presence of a weak rockpaper-scissors component can cause more relevant changes in the macroscopic behavior of the multi-agent
spatial three-strategy evolutionary games. To demonstrate this, we consider the three-state Potts model
on a square lattice if the uniform attractive pair interactions are modified by introducing a weak cyclic
dominance, i.e., G = G(Potts) + ǫG(rsp) where G(Potts) = d(1, 2) + d(2, 3) + d(1, 3). As mentioned before,
the n = 3 Potts model evolves into one of the three ordered states at low noises. In the presence of a
weak cyclic dominance, however, the domain growth is blocked by the formation of rotating spiral arms
as illustrated in Fig. 38. The spiral form of the rotating edges is a direct consequence of the fact that
the component ǫG(rsp) induces an average invasion velocity independent of the direction of the interface
and of the distance measured along the interface from the center of the given three-edge vortex (vortex
means rotating vertex). Due to the cyclic symmetry, all the three edges of a vortex (anti-vortex) rotate
clockwise (anti-clockwise). Sometimes the moving interfaces meet and may annihilate each other or create a
new vortex-anti-vortex pair. The latter processes are accompanied with a rearrangement of the connections
(represented by the interfaces) between the vortices and anti-vortices. Some geometrical features, namely,
the average curvature of interfaces, the average distance of vortices, the average length of interfaces between
a vortex and anti-vortex pair, were already investigated by Szolnoki and Szabó [323], Szolnoki et al. [324]
who found that the critical transition is suppressed in the presence of cyclic dominance and the correlation
length diverges as ξij ∝ 1/ǫ if ǫ → 0 at sufficiently low noise levels.

Figure 38: (Color online) Rotating spiral arms in the snapshots characteristic to the self-organizing pattern on the square
lattice where the pattern evolution is controlled by attractive (ferromagnetic) three-state Potts type interaction and a rockpaper-scissors component with a strength of ǫ = 0.1 for logit dynamics at a low noise level.

66

If the previous model is modified by additional potential game components that favor one of the homogeneous states, then a sufficiently weak cyclic component cannot prevent the formation of an ordered state
at low noises. In these cases the interaction itself might be considered as an ordinal potential game. A
further increase in the cyclic component, however, can maintain a self-organizing spatio-temporal pattern
(see Fig. 38) in which the portions of the three strategies are different. In the practice of evolutionary game
theory this mechanism is exploited when the undesired effect of social dilemma is reduced by introducing a
third strategy representing voluntarism [325], ”tit for tat” [326], or punishment [327].
It is emphasized that similar rotating spirals are observed in many other systems including BelousovZhabotinsky reaction [328, 329], excitable media (e.g. cardiac muscle [330], neural systems [331]), epidemiological models [332], and biological/ecological models [333, 334, 335]. The robustness of similar spatiotemporal patterns is also demonstrated by numerous three-strategy spatial evolutionary games (for a survey
see [22]). It is already well-known that the rock-paper-scissors type cyclic dominance helps the maintenance
of all the participating strategies/species [62] even for inhomogeneous invasion rates generating a non-trivial
reaction in the populations [336, 337]. The cyclic dominance can mediate positive or negative feedback
throughout the cyclic process that depends on the parity of the number of strategies within the cyclic game
[338, 339, 340]. The consequences of this parity effect can affect the behavior in many systems.
The presence of cyclic interactions is responsible for the survival of a large number of strategies and
the bio-diversity in biological systems [341, 22]. The investigations of predator-prey models with a large
number of species and with a complex structure of cyclic dominance indicate an extremely wide scale
of behaviors. In some systems the cyclic components can maintain different subsets of strategies, called
strategy associations, that are stabilized against the external invaders by suitable spatio-temporal patterns.
These strategy associations can survive simultaneously in a large spatial systems by forming large domains
[342, 343, 344, 345]. In these complex systems the cyclic dominance among the strategy associations can be
quantified by determining the average velocity of interfaces separating them [346, 347].
The analysis of the competition between strategy associations is generally based on models with random
sequential imitation type evolutionary rule that may even be applied simultaneously for several systems [348]
when the models become similar to stochastic cellular automata [349, 350]. The spatial rock-paper-scissor
game with a synchronized stochastic logit update [351] has demonstrated the appearance of chimera states
which have been intensively studied in the literature of coupled spatial oscillators [352, 353, 354, 355, 356].
For the repeated two-player rock-paper-scissors game the synchronized logit rule at low noises results in
cyclic choices [e.g. (1, 1) → (2, 2) → (3, 3) → (1, 1)] until the first mistake. Afterwards the (1, 2) → (3, 2) →
(3, 1) → (2, 1) → (2, 3) → (1, 3) → (1, 2) cycle is repeated in the absence of mistakes. Such cycles can also
occur in the spatial system as it is illustrated in Fig. 39. The numerical simulations indicate the formation

Figure 39: (Color online) Snapshot (left) of a chimera state on a square lattice where the evolution of a rock-paper-scissors
game is controlled by a low noise logit rule applied synchronously. The right hand plot illustrates how the spatial patterns
change cyclically.

of large domains in which the cyclic choices are stabilized by the neighborhoods suppressing the effect
67

of individual mistakes. In the snapshots one can distinguish nine types of domains representing different
phases of these cycles. Additionally the visualization of the pattern evolution indicates clearly the presence
of rotating spiral arms due to the cyclic dominance between the oscillating associations.
Finally we mention that the interfaces separating two strategy associations can serve as a location for
the emergence of a new strategy association with a proper spatio-temporal structure. Such phenomena were
reported in spatial evolutionary games with cyclic dominance between the strategies/species (for n ≤ 5)
where the evolutionary rule is based on imitation and site exchange of neighboring players [343] [346]. The
interfaces in Fig. 33 can also exemplify the appearance of a new phase that may play a crucial role in the
formation of multicellular living materials.
10. CONCLUSIONS AND OUTLOOK
We have reviewed our recent understanding of potential games representing an intimate relationship between physical systems and models applicable to study relevant phenomena in biological and social/economical
systems. The analogy becomes particularly important for those social and biological multi-agent systems
where the pair interactions can be well described by symmetric n × n potential games with logit rules when
the systems are driven into the Boltzmann distribution and the general laws of thermodynamics are valid.
The application of concepts and methods developed in statistical physics proved to be trivially beneficial
for the partnership games where the equivalent players share their income equally. It turned out, however,
that the analogies can be directly extended to the potential games representing a wider scale of games.
The evaluation of the potential is demonstrated if it exists. The largest component of the potential matrix
identifies the preferred Nash equilibrium (playing the role of ground state in physical systems) even for multiagent systems composed of uniform pair interactions. This feature implies a simple method for determining
the phase diagram at low noises. If the largest component of the potential matrix is located on the main
diagonal of the potential matrix then all the players prefer to choose the corresponding strategy independent
of the connectivity structure. In general, the latter systems show a thermodynamical behavior represented
by the Ising model in the presence of an external magnetic field, even for n > 2. As Ising type models have
already been investigated under a wide scale of different conditions (including symmetries, randomness,
networks, ordering processes) therefore many results of statistical physics can be directly adapted to explain
the phenomena in evolutionary games, as well. If the largest pair of the potential matrix components occurs
outside the main diagonal then the systems have two equivalent preferred Nash equilibria and become
similar to the anti-ferromagnetic Ising models. On bipartite graphs these systems exhibit an Ising type
order-disorder phase transition when the noise level is increased, otherwise the sublattice ordering can be
suppressed by frustration and/or randomness that may result in extremely slow relaxations towards the final
stationary state as discussed in the literature of spin glasses and Griffiths phases.
The classification of games into four classes of interactions has helped us conclude general features
characterizing the corresponding subset of games. Accordingly, the players are not interested in favoring
one of their strategies for games with cross-dependent payoffs, thus they choose strategies at random. For the
self-dependent payoffs the players’ behaviors can be considered separately from each other. Consequently,
all these multi-agent systems with equivalent players and interactions are well described by considering only
one player. It is found, furthermore, that the real pair interactions of potential games can be built up as a
linear combination of coordination type games between the possible strategy pairs.
It is shown that the presence of the elementary games with cyclic dominance prevents the existence
of potential. The consequences of the latter deviations are discussed for several examples challenging the
application of methods developed in the field of non-equilibrium statistical physics. In the light of these
results one can conclude that these terms of interactions result in self-organizations characterizing living
systems.
We have shown that some general questions of traditional game theory become particularly transparent
when using the tools of graph theory. Here we used graphs for three purposes. The dynamical graphs
visualize the strategy profiles (microscopic states) and the possible transitions between them if only unilateral
strategy changes are allowed in the system. Due to the simple structure of the dynamical graph (for the
68

symmetric games) we could determine the number of independent and relevant loops, along which the sum
of payoff variations should be zero for the potential games. The flow graph illustrates the preferred strategy
changes and simplifies the identification of the pure Nash equilibria (that always exist in potential games) as
nodes without outgoing edges. The dominance graph denotes graphically the payoff differences quantified by
the antisymmetric part of the payoff matrix. Using these concepts one can distinguish cyclic and hierarchical
dominance. In potential games the hierarchical dominance can be related to emergence of social dilemmas
occurring even for n > 2. It is hoped that further graph theoretical investigations can throw light on
additional relationships.
When writing this survey we faced challenging questions and interesting phenomena week by week. Some
of these problems have already been clarified during the preparation of this work while others remained in
the state of ”challenging questions”. Examples for the former problems are the decomposition of matrix
games, the identification of different classes of interactions, the relevance of cyclic dominance, the inherent
symmetries involved in the matrices, and a series of interesting phenomena. The list of the latter examples
is much longer and contains the identification of ordinal potential games, the elucidation of inherent symmetries in the classes of interactions, the systematic investigation of social dilemmas for potential games, the
relevance of high-entropy associations, the spontaneous formation of strategy associations in the presence
of cyclic games, the extension of relaxation process for quenched random interactions, the co-evolutionary
processes including the evolution of connectivity networks, payoffs, dynamical rules and emergence of new
strategies, etc. The study of these intriguing questions offers further promising challenges.
Acknowledgements
Discussions with Ben Allen, Kinga Bodó, Balázs Király, Martin Nowak, Attila Szolnoki, and Jeromos
Vukov are gratefully acknowledged. This work was supported by the John Templeton Foundation (FQEB
Grant #RFP-12-22) and the Hungarian National Research Fund (OTKA TK-101490).
References
References
[1] J. von Neumann, O. Morgenstern, Theory of Games and Economic Behaviour, Princeton University Press, Princeton,
1944.
[2] E. C. Zeeman, Population dynamics from game theory, in: Lecture Notes in Mathematics, Vol. 819, Springer, New York,
1980, pp. 471–497.
[3] J. Maynard Smith, Evolution and the Theory of Games, Cambridge University Press, Cambridge, UK, 1982.
[4] J. Hofbauer, K. Sigmund, The Theory of Evolution and Dynamical Systems, Cambridge University Press, Cambridge,
UK, 1988.
[5] J. Hofbauer, K. Sigmund, Evolutionary Games and Population Dynamics, Cambridge University Press, Cambridge, UK,
1998.
[6] H. Gintis, Game Theory Evolving, Princeton University Press, Princeton, 2000.
[7] R. Cressman, Evolutionary Dynamics and Extensive Form Games, MIT Press, Cambridge, MA, 2003.
[8] M. A. Nowak, Evolutionary Dynamics, Harvard University Press, Cambridge, MA, 2006.
[9] K. Sigmund, The Calculus of Selfishness, Princeton University Press, Princeton, NJ, 2010.
[10] W. H. Sandholm, Population Games and Evolutionary Dynamics, MIT University Press, Cambridge, MA, 2010.
[11] J. Maynard Smith, G. R. Price, The logic of animal conflict, Nature 246 (1973) 15–18.
[12] P. Taylor, L. Jonker, Evolutionary stable strategies and game dynamics, Math. Biosci. 40 (1978) 145–156.
[13] J. Hofbauer, P. Schuster, K. Sigmund, A note on evolutionary stable strategies and game dynamics, J. Theor. Biol. 81
(1979) 609–612.
[14] P. Schuster, K. Sigmund, Replicator dynamics, J. Theor. Biol. 100 (1983) 533–538.
[15] R. Axelrod, W. D. Hamilton, The evolution of cooperation, Science 211 (1981) 1390–1396.
[16] R. Axelrod, The Evolution of Cooperation, Basic Books, New York, 1984.
[17] D. Helbing, Interrelations between stochastic equations for systems with pair interactions, Physica A 181 (1992) 29–52.
[18] K. H. Schlag, Why imitate, and if so, how? A bounded rational approach to multi-armed bandits, J. Econ. Theory 78
(1998) 130–156.
[19] S. Hummert, K. Bohl, D. Basanta, A. Deutsch, S. Werner, G. Theissen, A. Schröter, S. Schuster, Evolutionary game
theory: cells as players, Mol. BioSyst. 10 (2014) 3044–3065.
[20] M. A. Nowak, R. M. May, Evolutionary games and spatial chaos, Nature 359 (1992) 826–829.

69

[21] M. A. Nowak, R. M. May, The spatial dilemmas of evolution, Int. J. Bifurcat. Chaos 3 (1993) 35–78.
[22] G. Szabó, G. Fáth, Evolutionary games on graphs, Phys. Rep. 446 (2007) 97–216.
[23] B. Allen, M. A. Nowak, Games on graphs, EMS Surv. Math. Sci. 1 (2014) 113–151.
[24] M. Perc, A. Szolnoki, Coevolutionary games – a mini review, BioSystems 99 (2010) 109–125.
[25] J. M. Pacheco, F. C. Santos, M. O. Souza, B. Skyrms, Evolutionary dynamics of collective action in n-person stag hunt
dilemmas, Proc. R. Soc. Lond. B 276 (2009) 315–321.
[26] M. Perc, J. Gómez-Gardeñes, A. Szolnoki, L. M. Florı́a and Y. Moreno, Evolutionary dynamics of group interactions on
structured populations: a review, J. R. Soc. Interface 10 (2013) 20120997.
[27] D. Monderer, L. S. Shapley, Potential games, Games Econ. Behav. 14 (1996) 124–143.
[28] L. E. Blume, The statistical mechanics of strategic interactions, Games Econ. Behav. 5 (1993) 387–424.
[29] O. Candogan, I. Menache, A. Ozdaglar, P. A. Parrilo, Flows and decomposition of games: Harmonic and potential
games, Math. Oper. Res. 36 (2011) 474–503.
[30] S.-H. Hwang, L. Rey-Bellet, Decompositions of two player games: potential, zero-sum, and stable games, E-print:
arXiv:1106.3552v2 (2011).
[31] G. Szabó, K. S. Bodó, B. Allen, M. A. Nowak, Fourier decomposition of payoff matrix for symmetric three-strategy
games, Phys. Rev. E 90 (2014) 042811.
[32] D. Cheng, On finite potential games, Automatica 50 (2014) 1793–1801.
[33] L. Mallozzi, An application of optimization theory to the study of equilibria for games: a survey, Cent. Eur. J. Oper.
Res. 21 (2013) 523–539.
[34] D. Fudenberg, J. Tirole, Game Theory, MIT Press, Cambridge, MA, 1991.
[35] R. Gibbons, Game Theory for Applied Economists, Princeton University Press, Princeton, NJ, 1992.
[36] J. W. Weibull, Evolutionary Game Theory, MIT Press, Cambridge, MA, 1995.
[37] L. Samuelson, Evolutionary Games and Equilibrium Selection, MIT Press, Cambridge, MA, 1997.
[38] J. Nash, Equilibrium points in n-person games, Proc. Natl. Acad. Sci. USA 36 (1950) 48–49.
[39] J. Nash, Non-cooperative games, Ann. Math. 54 (1951) 286–295.
[40] J. C. Harsanyi, R. Selten, A General Theory of Equilibrium Selection in Games, MIT Press, Cambridge, MA, 1988.
[41] J. Schnakenberg, Network theory of microscopic and macroscopic behavior of master equation systems, Rev. Mod. Phys.
48 (1976) 571–585.
[42] R. A. Fisher, The Genetical Theory of Natural Selection, Clarendon Press, Oxford, 1930.
[43] M. Beckmann, C. B. McGuire, Studies in the Economics of Transportation, Yale University Press, New Haven, 1956.
[44] R. W. Rosenthal, A class of games possessing pure-strategy Nash equilibria, Int. J. Game Theory 2 (1973) 65–67.
[45] G. Facchini, F. van Megen, P. Borm, S. Tijs, Congestion models and weighted Bayesian potential games, Theor. Decis.
42 (1997) 193–206.
[46] W. H. Sandholm, Potential games with continuous player sets, J Econ. Theor. 97 (2001) 80–108.
[47] M. E. Slade, What does an oligopoly maximize, J. Econ. Theory 42 (1994) 45–51.
[48] M. Voorneveld, Best response potential games, Econ. Lett. 66 (2000) 289–295.
[49] S. Morris, T. Ui, Generalized potential and robust sets of equilibria, J. Econ. Theor. 124 (2005) 45–78.
[50] L. E. Blume, The statistical-mechanics of best-response strategy revision, Games Econ. Behav. 11 (1995) 111–145.
[51] W. H. Sandholm, Decompositions and potentials for normal form games, Games Econ. Behav. 70 (2010) 446–456.
[52] G. Kirchhoff, Über die Auflösung der Gleichungen, auf welche man bei der Untersuchung der linearen Vertheilung
galvanisher Ströme gefürt wird, Ann. Phys. Chem. 72 (1847) 497–508.
[53] C. A. Desoer, E. S. Kuh, Basic Circuit Theory, MacGraw-Hill, 1969.
[54] F. Harary, R. Z. Norman, D. Cartwright, Structural Models: An Introduction to the Theory of Directed Graphs, Wiley,
New York, 1966.
[55] B. Bollobás, Modern Graph Theory, Springer, New York, 1998.
[56] J. Szép, F. Forgó, Introduction to Theory of Games, Akadémiai Kiadó, Budapest, 1985.
[57] N. L. Kleinberg, J. H. Weiss, The orthogonal decomposition of games and an averaging formula for the Shapley value,
Math. Oper. Res. 11 (1986) 117–124.
[58] O. Candogan, A. Ozdaglar, P. A. Parrilo, Dynamics in near-potential games, Games Econ. Behav. 82 (2013) 66–90.
[59] G. Szabó, K. S. Bodó, B. Allen, M. A. Nowak, Four classes of interactions for evolutionary games, Phys. Rev. E 92
(2015) 022820.
[60] C. Adami, J. Schossau, A. Hintze, Evolution and stability of altruist strategies in microbial games, Phys. Rev. E 85
(2012) 011914.
[61] P. Cui, Z.-X. Wu, Selfish punishment with avoiding mechanism can alleviate both first-order and second-order social
dilemma, J. Theor. Biol. 361 (2014) 111–123.
[62] R. M. May, W. J. Leonard, Nonlinear aspects of competition between three species, SIAM J. Appl. Math. 29 (1975)
243–253.
[63] K. Tainaka, Physics and ecology of rock-paper-scissors game, in: T. Marsland, I. Frank (Eds.), Lecture Notes in Computer
Science, volume 2063, Springer, Berlin, 2001, pp. 384–395.
[64] E. Frey, Evolutionary game theory: Theoretical concepts and applications to microbial communities, Physica A 389
(2010) 4265–4298.
[65] A. Szolnoki, M. Mobilia, L.-L. Jyian, B. Szczesny, A. M. Rucklidge, M. Perc, Cyclic dominance in evolutionary games:
a review, J. R. Soc. Interface 11 (2014) 20140735.
[66] N. Ahmed, K. R. Rao, Orthogonal transforms for digital signal processing, Springer-Verlag, Berlin, 1975.
[67] L. M. van Valen, A new evolutionary law, Evolutionary Theory 1 (1973) 1–30.

70

[68] L. M. van Valen, Evolution as a zero-sum game for energy, Evolutionary Theory 4 (1980) 289–300.
[69] D. Friedman, Evolutionary games in economics, Econometrica 59 (1991) 637–666.
[70] R. Cressman, W. G. Morrison, J.-F. Wen, On the evolutionary dynamics of crime, Can. J. Econ. 31 (1998) 1101–1117.
[71] Z. Cao, X. Yang, The fashion game: Network extension of matching pennies, Theor. Comp. Sci. 540-541 (2014) 169–181.
[72] J. Sardanyés, R. V. Solé, Red Queen coevolution on fitness landscapes, in: H. Richter, A. Engelbrecht (Eds.), Recent
Advances in the Theory and Application of Fitness Landscapes, Emergence, Complexity and Computation, Vol. 6,
Springer, Berlin, 2014, pp. 301–338.
[73] J. Juul, A. Kianercy, S. Bernhardsson, S. Pigolotti, Replicator dynamics with turnover of players, Phys. Rev. E 88 (2013)
022806.
[74] B. Xu, S. Wang, Z. Wang, Periodic frequencies of the cycles in 2x2 games: evidence from experimental economics, Eur.
Phys. J. B 87 (2014) 46.
[75] M. W. Macy, A. Flache, Learning dynamics in social dilemmas, Proc. Natl. Acad. Sci. USA 99 (2002) 7229–7236.
[76] F. C. Santos, J. M. Pacheco, T. Lenaerts, Evolutionary dynamics of social dilemmas in structured heterogeneous
populations, Proc. Natl. Acad. Sci. USA 103 (2006) 3490–3494.
[77] C. Hauert, M. Doebeli, Spatial structure often inhibits the evolution of cooperation in the snowdrift game, Nature 428
(2004) 643–646.
[78] P. Morris, Introduction to Game Theory, Springer-Verlag, Berlin, 1994.
[79] G. Szabó, A. Szolnoki, Selfishness, fraternity, and other-regarding preference in spatial evolutionary games, J. Theor.
Biol. 299 (2012) 81–87.
[80] M. A. Nowak, S. Bonhoeffer, R. M. May, More spatial games, Int. J. Bifurcat. Chaos 4 (1994) 33–56.
[81] M. H. Vainstein, J. J. Arenzon, Disordered environments in spatial games, Phys. Rev. E 64 (2001) 051905.
[82] P. Holme, A. Trusina, B. J. Kim, P. Minnhagen, Prisoner’s dilemma in real-world acquaintance networks: Spikes and
quasiequilibria induced by the interplay between structure and dynamics, Phys. Rev. E 68 (2003) 030901.
[83] B. J. Kim, A. Trusina, P. Holme, P. Minnhagen, J. S. Chung, M. Y. Choi, Dynamic instabilities induced by asymmetric
influence: Prisoner’s dilemma game in small-world networks, Phys. Rev. E 66 (2002) 021907.
[84] N. Masuda, K. Aihara, Spatial prisoner’s dilemma optimally played in small-world networks, Phys. Lett. A 313 (2003)
55–61.
[85] O. Durán, R. Mulet, Evolutionary prisoner’s dilemma in random graphs, Physica D 208 (2005) 257–265.
[86] J. Vukov, G. Szabó, A. Szolnoki, Cooperation in the noisy case: Prisoner’s dilemma game on two types of regular random
graphs, Phys. Rev. E 73 (2006) 067103.
[87] E. De Santis, C. Marinelli, A class of stochastic games with infinitely many interacting agents related to Glauber dynamics
on random graphs, J. Phys. A: Math. Theor. 49 (2007) 11777–11790.
[88] Z.-X. Wu, X.-J. Xu, Y. Chen, Y.-H. Wang, Spatial prisoner’s dilemma game with volunteering in Newman-Watts
small-world networks, Phys. Rev. E 71 (2005) 037103.
[89] M. Tomassini, L. Luthi, M. Giacobini, Hawks and doves games on small-world networks, Phys. Rev. E 73 (2006) 016132.
[90] F. C. Santos, J. M. Pacheco, Scale-free networks provide a unifying framework for the emergence of cooperation, Phys.
Rev. Lett. 95 (2005) 098104.
[91] F. C. Santos, J. F. Rodrigues, J. M. Pacheco, Graph topology plays a determinant role in the evolution of cooperation,
Proc. R. Soc. B 273 (2006) 51–55.
[92] G. Szabó, T. Tomé, I. Borsos, Probability currents and entropy productions in nonequilibrium lattice systems, Phys.
Rev. E 82 (2010) 011105.
[93] G. W. Brown, Iterative solution of games by fictious play, in: T. C. Koopmans (Ed.), Activity Analysis of Production
and Allocation, Wiley, New York, 1951, pp. 373–376.
[94] D. Monderer, L. S. Shapley, Fictious play property for games with identical interests, J. Econ. Theory 68 (1996) 258–265.
[95] J. W. Essam, Percolation theory, Rep. Progr. Phys. 43 (1980) 833–912.
[96] D. Stauffer, A. Aharony, Introduction to Percolation Theory, Taylor & Francis, London, 1992.
[97] M. Sysi-Aho, J. Saramäki, J. Kertész, K. Kaski, Spatial snowdrift game with myopic agents, Eur. Phys. J. B 44 (2005)
129–135.
[98] C. P. Roca, J. A. Cuesta, A. Sánchez, Evolutionary game theory: Temporal and spatial effects beyond replicator
dynamics, Phys. Life Rev. 6 (2009) 208–249.
[99] D. Helbing, Microscopic foundation of stochastic game dynamical equations, in: W. Leinfellner, E. Köhler (Eds.), Game
Theory, Experience, Rationality, Kluwer Academic, Dordrecht, 1998, pp. 211–224.
[100] G. Szabó, C. Tőke, Evolutionary prisoner’s dilemma game on a square lattice, Phys. Rev. E 58 (1998) 69–73.
[101] R. Alonso-Sanz, C. Martı́n, M. Martı́n, The effect of memory in the spatial continuous-valued prisoner’s dilemma, Int.
J. Bifurcat. Chaos 11 (2001) 2061–2083.
[102] H. Ohtsuki, M. A. Nowak, Evolutionary games on cycles, Proc. R. Soc. Lond. B 273 (2006) 2249–2256.
[103] G. Wild, A. Gardner, S. A. West, Adaptation and the evolution of parasite virulence in a connected world, Nature 459
(2009) 983–986.
[104] B. Wu, P. M. Altrock, L. Wang, A. Traulsen, Universality of weak selection, Phys. Rev. E 82 (2010) 046106.
[105] M. Willensdorfer, M. A. Nowak, Mutation in evolutionary games can increase average fitness at equilibrium, J. Theor.
Biol. 237 (2005) 355–362.
[106] T. Antal, M. A. Nowak, A. Traulsen, Strategy abundance in 2 × 2 games for arbitrary mutation rates, J. Theor. Biol.
257 (2009) 340–344.
[107] C. E. Tarnita, T. Antal, M. A. Nowak, Mutation-selection equilibrium in games with mixed strategies, J. Theor. Biol.
261 (2009) 50–57.

71

[108] K. Sharp, F. Matschinsky, Translation of Ludwig Boltzmanns paper on the relationship between the second fundamental
theorem of the mechanical theory of heat and probability calculations regarding the conditions for thermal equilibrium
Sitzungberichte der Kaiserlichen Akademie der Wissenschaften. Mathematisch-Naturwissen Classe. Abt. II, LXXVI 1877,
pp 373-435 (Wien. Ber. 1877, 76:373-435). Reprinted in Wiss. Abhandlungen, Vol. II, reprint 42, p. 164-223, Barth,
Leipzig, 1909, Entropy 17 (2015) 1971–2009.
[109] R. J. Glauber, Time-dependent statistics of the Ising model, J. Math. Phys 4 (1963) 294–307.
[110] D. Fudenberg, D. K. Levine, Learning in games: Where do we stand, European Economic Review 42 (1998) 631–639.
[111] T. P. Eggarter, Cayley trees, the Ising problem, and the thermodynamic limit, Phys. Rev. B 9 (1974) 2989.
[112] R. J. Baxter, Exactly solved models in statistical mechanics, Academic, London, 1982.
[113] Z. R. Yang, Solvable Ising model in Sierpinski carpets: The partition function, Phys. Rev. E 49 (1994) 2457–2457.
[114] K. Kawasaki, Diffusion constant near the critical point for time-dependent Ising models I, Phys. Rev. 145 (1966) 224–230.
[115] L. D. Landau, E. M. Lifshitz, Statistical Physics (third edition) Part 1, Butterworth-Heinemann, Oxford, 1980.
[116] K. Toda, R. Kubo, N. Saito, Statistical Physics I: Equilibrium Statistical Mechanics, Springer, Berlin, Heidelberg, 1991.
[117] L. Boltzmann, Über die Benziehung zwischen dem Zweiten Hauptsatze der mechanischen Wärmethorie und der
Wahrscheinlichkeitsrechnung resp. den Sätzen über das Wämegleichgewicht, Sitzunber. Kais. Akad. Wiss. Wien Math.
Naturwiss. Classe 76 (1877) 373–435.
[118] J. W. Gibbs, Elementary principles in statistical mechanics, Yale University Press, New Haven, 1902.
[119] L. Szilárd, Über die Entropieverminderung in einem thermodynamischen System bei Eingriffen intelligenter Wesen”
(On the reduction of entropy in a thermodynamic system by the intervention of intelligent beings, Z. Physik 53 (1929)
840–856.
[120] I. T. Jaynes, Information theory and statistical mechanics, Phys. Rev. 106 (1957) 620–628.
[121] L. E. Blume, How noise matters, Games Econ. Behav. 44 (2003) 251–271.
[122] M. H. Cohen, I. I. Eliazar, Econophysical visualization of Adam Smith’s invisible hand, Physica A 392 (2013) 813–822.
[123] C. E. Shannon, W. Weaver, Mathematical theory of communication, University of Illinois Press, Urbana, 1949.
[124] H. Haken, Information and Self-organization, Springer, Berlin, 1988.
[125] H. B. Callen, Thermodynamics, Wiley, New York, 1960.
[126] R. M. Alberty, Use of Legendre transform in chemical thermodynamics, Pure Appl. Chem. 73 (2001) 1349–1380.
[127] R. K. P. Zia, E. F. Redish, S. R. McKay, Making sense of the Legendre transform, Am. J. Phys. 77 (2009) 614–622.
[128] R. Graham, T. Tél, Existence of potential for dissipative dynamical systems, Phys. Rev. Lett. 52 (1984) 9–12.
[129] R. Graham, A. Hamm, T. Tél, Nonequilibrium potential for dynamical systems with fractal attractors or repellers, Phys.
Rev. Lett. 66 (1991) 3089–3092.
[130] C. Beck, E. D. G. Cohen, Superstatistics, Physica A 332 (2003) 267–275.
[131] R. Hanel, S. Thurner, M. Gell-Mann, Generalized entropies and the transformation group of superstatistics, PNAS 108
(2011) 6390–6394.
[132] G. Szabó, A. Szolnoki, J. Vukov, Selection of dynamical rules in spatial prisoner’s dilemma games, EPL 87 (2009) 18007.
[133] L. Tisza, Generalized thermodynamics, MIT Press, Cambridge, MA, 1966.
[134] H. B. Callen, Thermodynamics and an Introduction to Thermostatistics (2nd ed.), John Wiley & Sons, New York, 1985.
[135] R. Kubo, The fluctuation-dissipation theorem, Phys. Rep. 29 (1966) 255–280.
[136] T. Morita, Cluster variation method and Möbius inversion formula, J. Stat. Phys. 59 (1990) 819–825.
[137] D. Gratias, J. M. Sanchez, D. de Fontaine, Application of group theory to the calculation of the configurational entropy
in the cluster variation method, Physica 113 (1982) 315.
[138] H. A. Gutowitz, J. D. Victor, B. W. Knight, Local structure theory for cellular automata, Physica D 28 (1987) 18–48.
[139] R. Dickman, Driven lattice gas with repulsive interactions: Mean-field theory, Phys. Rev. A 41 (1990) 2192–2195.
[140] H. A. Bethe, Statistical theory of superlattices, Proc. R. Soc. (London) A 150 (1935) 552.
[141] R. Kikuchi, A theory of cooperative phenomena, Phys. Rev. 81 (1951) 988–1003.
[142] R. Kikuchi, S. Brush, Improvement of the cluster-variation method, J. Chem. Phys. 47 (1967) 195–203.
[143] T. Morita, General structure of the distribution functions for the Heisenberg model and the Ising model, J. Math. Phys.
13 (1972) 115–123.
[144] D. de Fontaine, Cluster variation and cluster statics, in: J. L. Morin-Lopez, J. M. Sanchez (Eds.), Theory and Applications
of the Cluster Variation and Path Probability Methods, Springer US, 1996, pp. 125–144.
[145] L. Udvardi, G. Szabó, Lattice-gas model for alkali-fullerides: face-centered-cubic structure, J. Phys.: Condens. Matter 8
(1996) 10959–10971.
[146] S. G. Brush, History of the Lenz-Ising model, Rev. Mod. Phys. 39 (1967) 883–893.
[147] M. Niss, History of the Lenz-Ising model 1920-1950: From ferromagnetic to cooperative phenomena, Arch. Hist. Exact
Sci. 59 (2005) 267–318.
[148] M. Niss, History of the Lenz-Ising model 1950-1965: From irrelevance to relevance, Arch. Hist. Exact Sci. 63 (2009)
243–287.
[149] M. Niss, History of the Lenz-Ising model 1965-1971: the role of simple model in understanding critical phenomena, Arch.
Hist. Exact Sci. 65 (2011) 625–658.
[150] D. Sornette, Physics and financial economics (1776-2014): puzzles, Ising and agent-based models, Rep. Prog. Phys. 77
(2014) 062001.
[151] W. Lenz, Beitrag zum Verständnis der magnetischen Erscheinungen in festen KörpernTheorie des Ferromagnetismus,
Physik. Z. 21 (1920) 613–615.
[152] E. Ising, Beitrag zur Theorie des Ferromagnetismus, Z. Physik 31 (1925) 253–258.
[153] R. M. Bozorth, Ferromagnetism, Van Nostrand, 1951.

72

[154] D. C. Mattis, Theory of magnetism, Harper and Row, 1965.
[155] R. E. Peierls, On Ising’s model of ferromagnetism, Proc. Camb. Phil. Soc. 32 (1936) 477–481.
[156] R. B. Griffiths, Peierls proof of spontaneous magnetization in a two-dimensional Ising ferromagnet, Phys. Rev. 136
(1964) 437–439.
[157] W. L. Bragg, E. J. Williams, The effect of the thermal agitation on atomic arrangement in alloys, Proc. R. Soc. (London)
A 145 (1934) 699.
[158] L. Onsager, Crystal statistics. I. a two-dimensional model with an order-disorder transition, Physical Review 65 (1944)
117–149.
[159] G. F. Newell, E. W. Montroll, On the theory of the Ising model of ferromagnetism, Rev. Mod. Phys. 25 (1953) 353–389.
[160] C. Domb, Ising model, in: C. Domb, M. S. Green (Eds.), Phase Transitions and Critical Phenomena, Vol. 3, Academic
Press, London, 1974, pp. 357–484.
[161] K. Kawasaki, Kinetics of Ising models, in: C. Domb, M. S. Green (Eds.), Phase Transitions and Critical Phenomena,
Vol. 2, Academic Press, London, 1972, pp. 443–501.
[162] H. E. Stanley, Introduction to Phase Transitions and Critical Phenomena, Clarendon Press, Oxford, 1971.
[163] C. Kittel, Introduction to Solid State Physics, John Wiley & Sons, Chichester, 2004.
[164] G. Alefeld, J. Völkl, Hydrogen in metals I: Basic properties, Topics in Applied Physics, Vol. 28, Springer-Verlag, Berlin,
1978.
[165] W. Dieterich, P. Fulde, I. Peschel, Superionic conductors, Adv. Phys. 29 (1980) 345.
[166] M. S. Dresselhaus, G. Dresselhaus, Intercalation compounds of graphite, Adv. Phys. 51 (2002).
[167] K. Kosuge, Chemistry of Non-stoichiometric Compounds, Oxford University Press, Oxford, 1994.
[168] A. Pelissetto, E. Vicari, Critical phenomena and renormalization group theory, Phys. Rep. 368 (2002) 549–727.
[169] S. Galam, Y. Gefen, Y. Shapir, Sociophysics: A mean behavior model for the process of strike, Math. J. Sociol. 9 (1982)
1–13.
[170] S. M. Krause, S. Bornholdt, Spin models as microfoundation of macroscopic market models, Physica A 392 (2013)
4048–4054.
[171] A. V. M. Herz, Collective phenomena in spatially extended evolutionary games, J. Theor. Biol. 169 (1994) 65–87.
[172] I. H. Lee, Á. Valentinyi, Interactive contagion, Rev. Econ. Stud. 67 (2000) 47–66.
[173] W. A. Brock, S. N. Durlauf, Discrete choice with social interactions, Rev. Econ. Stud. 68 (2001) 235–260.
[174] G. Weisbuch, D. Stauffer, ”antiferromagnetism” in social relations and Bonabeau model, Physica A 384 (2007) 542–548.
[175] S. Galam, B. Walliser, Ising model versus normal form game, Physica A 389 (2010) 481–489.
[176] S. Grauwin, D. Hunt, E. Bertin, P. Jensen, Effective free energy for individual dynamics, Adv. Complex Systems 14
(2011) 529–536.
[177] M. Nowak, K. Sigmund, The evolution of stochastic strategies in the prisoner’s dilemma, Acta Appl. Math. 20 (1990)
247–265.
[178] R. B. Potts, Some generalized order-disorder transitions, Math. Proc. Camb. Phil. Soc. 48 (1952) 106–109.
[179] J. Ashkin, E. Teller, Statistics of two-dimensional lattices with four components, Phys. Rev. 64 (1943) 178–184.
[180] T. Kihara, Y. Midzuno, T. Shizume, Statistics of two-dimensional lattices with many components, J. Phys. Soc. Jpn. 9
(1954) 681–687.
[181] C. Domb, Graph theory and embeddings, in: C. Domb, M. S. Green (Eds.), Phase Transitions and Critical Phenomena,
Vol. 3, Academic Press, London, 1974, pp. 1–95.
[182] F. Y. Wu, The Potts model, Rev. Mod. Phys. 54 (1982) 235–268.
[183] S. Alexander, Lattice gas transition of He on grafoil: A continuous transition with cubic terms, Phys. Lett. A 54 (1975)
353.
[184] E. Domany, E. K. Riedel, Phase transitions in two-dimensional systems, J. Appl. Phys. 49 (1978) 1315.
[185] J. F. Gouyet, B. Sapoval, P. Pfeuty, Antiferroelectric transition in β-alumina, a realization of the D = 2, s = 3 Potts
model?, J. Physique Lett. 41 (1980) L115–L117.
[186] E. Domany, M. Schick, J. S. Walker, R. B. Griffiths, Classification of continuous order-disorder transitions in adsorbed
monolayers, Phys. Rev. B 18 (1978) 2209.
[187] T. M. Liggett, Interacting Particle Systems, Springer, New York, 1985.
[188] W.-X. Wang, J. Lü, G. Chen, P. M. Hui, Phase transition and hysteresis loop in structured games with global updating,
Phys. Rev. E 77 (2008) 046109.
[189] D. H. Wolpert, M. Harré, E. Olbrich, N. Bertschinger, J. Jost, Hysteresis effects of changing parameters on noncooperative
games, Phys. Rev. E 85 (2012) 036102.
[190] D.-Y. Hua, Hysteresis behavior and nonequilibrium phase transition in a one-dimensional evolutionary game model,
Chin. Phys. B 22 (2013) 040512.
[191] B. L. van der Waerden, Die lange Reichweite der regelmassigen Atomanordnung in Mischkristallen, Z. Physik 118 (1941)
473–488.
[192] G. H. Wannier, The statistical problem in cooperative phenomena, Rev. Mod. Phys. 17 (1945) 50–60.
[193] C. Domb, On the theory of cooperative phenomena in crystals, Adv. Phys. 9 (1960) 149–244.
[194] H. A. Kramers, G. H. Wannier, Statistics of the two-dimensional ferromagnet. part 1, Phys. Rev. 60 (1941) 252–262.
[195] F. J. Wegner, Duality in generalized Ising models and phase transitions without local order parameter, J. Math. Phys.
12 (1971) 2259–2272.
[196] M. E. Fisher, The theory of equilibroum critical phenomena, Phys. Rep. 30 (1967) 616–730.
[197] R. B. Griffiths, Dependence of critical indices on a parameter, Phys. Rev. Lett. 24 (1970) 1479–1482.
[198] D. C. Rapaport, C. Domb, The smoothness postulate and the Ising antiferromagnet, J. Phys. C: Sol. St. Phys. 4 (1971)

73

2684–2694.
[199] U. M. B. Marconi, A. Puglisi, L. Rondoni, A. Vulpiani, Fluctuation-dissipation: Response theory in statistical physics,
Phys. Rep. 461 (2008) 111–195.
[200] L. P. Kadanoff, Static phenomena near critical points: Theory and experiments, Rev. Mod. Phys. 39 (1967) 395–431.
[201] K. G. Wilson, The renormalization group and critical phenomena, Rev. Mod. Phys. 55 (1983) 583–600.
[202] H. E. Stanley, Scaling, universality, and renormalization: thee pillars of modern critical phenomena, Rev. Mod. Phys.
71 (1999) S358–S366.
[203] M. E. Fischer, Renormalization group theory: Its basis and formulation in statistical physics, Rev. Mod. Phys. 70 (1998)
653–681.
[204] G. Ódor, Universality in Nonequilibrium Lattice Systems, World Scientific, Singapore, 2008.
[205] G. Pérez, F. Sastre, R. Medina, Critical exponents for the extended dynamical systems with simultaneous updating: the
case of ising model, Physica D 168-169 (2002) 318–324.
[206] S. Wolfram, Universality and complexity in cellular automata, Physica D 10 (1984) 1–35.
[207] S. N. Dorogovtsev, A. V. Goltsev, J. F. F. Mendes, Critical phenomena in complex networks, Rev. Mod. Phys. 80 (2008)
1275–1335.
[208] J. Vukov, L. Varga, B. Allen, M. A. Nowak, G. Szabó, Payoff components and their effects in a spatial three-strategy
evolutionary social dilemma, Phys. Rev. E 92 (2015) 012813.
[209] E. Müller-Hartmann, J. Zittartz, New type of phase transition, Phys. Rev. Lett. 33 (1974) 893.
[210] Y. K. Wang, F. Y. Wu, Multi-component spin model on a Cayley tree, J. Phys. A: Math. Gen. 9 (1976) 593.
[211] M. Ostilli, Cayley trees and Bethe lattices: A concise analysis for mathematicians and physicists, Physica A 391 (2012)
3417–3423.
[212] R. Mélin, J. C. A. d’Auriac, P. Chandra, B. Doucot, Glassy behavior in the ferromagnetic Ising model on a Cayley tree,
J. Phys. A: Math. Gen. 29 (1996) 6773–5804.
[213] R. Albert, A.-L. Barabási, Statistical mechanics of complex networks, Rev. Mod. Phys. 74 (2002) 47–97.
[214] M. E. J. Newman, The structure and function of complex networks, SIAM Review 45 (2003) 167–256.
[215] G. Szabó, C. Hauert, Evolutionary prisoner’s dilemma games with voluntary participation, Phys. Rev. E 66 (2002)
062903.
[216] D. J. Watts, S. H. Strogatz, Collective dynamics of ’small world’ networks, Nature 393 (1998) 440–442.
[217] M. E. J. Newman, D. J. Watts, Renormalization group analysis of the small-world network model, Phys. Lett. A 263
(1999) 341–346.
[218] A. Barrat, M. Weigt, On the properties of small-world network model, Eur. Phys. J. B: Math. Gen. 13 (2000) 547–560.
[219] M. Gitterman, Small-world phenomena in physics: the Ising model, J. Phys. A: Math. Gen. 33 (2000) 8373–8381.
[220] C. P. Herrero, Ising model in small-world networks, Phys. Rev. E 65 (2002) 066110.
[221] A. Chatterjee, P. Sen, Phase transitions in an Ising model on a Euclidean network, Phys. Rev. E 74 (2006) 036109.
[222] S. N. Dorogovtsev, A. V. Goltsev, J. F. F. Mendes, Ising model on networks with an arbitrary distribution of connections,
Phys. Rev. E 66 (2002) 016104.
[223] M. Leone, A. Vázquez, A. Vespignani, R. Zecchina, Ferromagnetic ordering in graphs with arbitrary degree distribution,
Eur. Phys. J. B 28 (2002) 191–197.
[224] A. Aleksiejuk, J. Holyst, D. Stauffer, Ferromagnetic phase transition in Barabási-Albert networks, Physica A 310 (2002)
260–266.
[225] Y. Gefen, B. B. Mandelbrot, A. Aharony, Critical phenomena on fractal lattices, Phys. Rev. Lett. 45 (1980) 855–858.
[226] Y. Gefen, Y. Meir, B. B. Mandelbrot, A. Aharony, Geometric interpretation of hypercubic lattices with noninteger
dimensionality by use of low lacunarity fractal lattices, Phys. Rev. Lett. 50 (1983) 145–148.
[227] B. B. Mandelbrot, Fractals: Form, Chance and Dimension, Freeman, San Francisco, 1977.
[228] G. Bhanot, H. Neuberger, J. A. Shapiro, Simulation of a critical Ising fractal, Phys. Rev. Lett. 53 (1984) 2277–2280.
[229] J. C. A. d’Auriac, R. Rammal, Critical behavior of the kinetic Ising model on a fractal lattice, J. Phys. A: Math. Gen.
19 (1986) L655–L661.
[230] B. Bonnier, Y. Leroyer, C. Meyers, Real-space renormalization-goup study of fractal Ising models, Phys. Rev. B 37
(1988) 5205–5210.
[231] P. Monceau, M. Perreau, F. Hébert, Magnetic critical behavior of the Ising model on fractal structures, Phys. Rev. B
58 (1998) 6386–6393.
[232] J. M. Carmona, U. M. B. Marconi, J. J. Ruiz-Lorenzo, A. Tarancón, Critical properties of the Ising model on Sierpinski
fractals: A finite-size scaling-analysis approach, Phys. Rev. B 58 (1998) 14387–14396.
[233] Y. Gefen, A. Aharony, B. B. Mandelbrot, Phase transitions on fractals: I. quasi-linear lattices, J. Phys. A: Math. Gen.
16 (1983) 1267–1278.
[234] Y. Gefen, A. Aharony, Y. Shapir, B. B. Mandelbrot, Phase transitions on fractals: II. Sierpinski gaskets, J. Phys. A:
Math. Gen. 17 (1984) 435–444.
[235] B. B. Mandelbrot, The Fractal Geometry of Nature, Freeman, New York, 1983.
[236] Y.-K. Wu, B. Hu, Phase transitions on complex Sierpinski carpets, Phys. Rev. A 35 (1987) 1404–1411.
[237] P. Monceau, P.-Y. Hsiao, Direct evidence for weak universality on fractal structures, Physica A 331 (2004) 1–9.
[238] A. Dembo, A. Montanari, Ising models on locally tree-like graphs, Ann. Appl. Prob. 20 (2010) 565–592.
[239] A. Montanari, E. Mossel, A. Sly, The weak limit of Ising models on locally tree-like graphs, Probab. Theory Relat. Fields
152 (2012) 31–51.
[240] A. Dembo, A. Montanari, N. Sun, Factor models on locally tree-like graphs, Ann. Prob. 41 (2013) 4162–4213.
[241] D. Ruelle, Statistical mechanics of a one-dimensional lattice gas, Commun. Math. Phys. 9 (1968) 267.

74

[242] F. J. Dyson, Existence of a phase-transition in a one-dimensional Ising ferromagnet, Commun. Math. Phys. 12 (1969)
91–107.
[243] F. J. Dyson, An Ising ferromagnet with discontinuous long-range order, Commun. Math. Phys. 21 (1971) 269–283.
[244] J. Z. Imbrie, C. M. Newman, An intermediate phase with slow decay of correlations in one-dimensional 1/|x − y| + 2
percolation, Ising Potts models, Commun. Math. Phys. 118 (1988) 303–336.
[245] M. E. Fisher, S. Ma, B. G. Nickel, Critical exponents for long-range interactions, Phys. Rev. Lett. 29 (1972) 917–920.
[246] L. T. Wille, Mean-field theory of oxygen-vacancy ordering in YBa2 Cu3 O7−δ , Phys. Rev. B. 40 (1989) 6931–6940.
[247] K. Binder, D. P. Landau, Phase diagrams and critical behavior in Ising square lattices with nearest- and next-nearestneighbor interactions, Phys. Rev. B 21 (1980) 1941–1962.
[248] J. Yin, D. P. Landau, Phase diagram and critical behavior of the square-lattice Ising model with competing nearestneighbor and next-nearest-neighbor interactions, Phys. Rev. E 80 (2009) 051117.
[249] S. L. A. de Queiroz, Scaling behavior of a square-lattice Ising model with competing interactions in a uniform field,
Phys. Rev. E 84 (2011) 031132.
[250] G. Gompper, M. Schick, Self-Assembling Amphiphilic Systems, Academic Press, London, 1994.
[251] J. R. Henriksen, M. C. Sabra, O. G. Mouritsen, Phase transitions and steady state microstructure in a two-temperature
lattice-gas with mobile active impurities, Phys. Rev. E 62 (2000) 7070–7076.
[252] J. Yin, D. P. Landau, Square lattice gases with two- and three-body interactions revisited: A row-shifted (2 × 2) phase,
Phys. Rev. E 81 (2010) 031121.
[253] Y. I. Dublenych, Ground states of the lattice-gas model on triangular lattice with nearest- and next-nearest-neighbor
pairwise interactions and with three-particle interaction: Ground states at boundaries of full-dimensional regions, Phys.
Rev. E 84 (2011) 061102.
[254] H. T. Diep, Frustrated spin systems, World Scientific, Singapore, 2004.
[255] G. H. Wannier, Antiferromagnetism. the triangular Ising net, Phys. Rev. 79 (1950) 357–364.
[256] M. Rojas, O. Rojas, S. M. de Souza, Frustrated Ising model on the Cairo pentagonal lattice, Phys. Rev. E 86 (2012)
051116.
[257] A. N. Berker, L. P. Kadanoff, Ground-state entropy and algebraic order at low temperatures, J. Phys. A: Math. Gen.
13 (1980) L259–L264.
[258] V. Cannella, J. A. Mydosh, Magnetic ordering in gold-iron alloys, Phys. Rev. B 6 (1972) 4220–4237.
[259] M. Mézard, G. Parisi, M. A. Virasoro, Spin Glass Theory and Beyond, World Scientific, Singapore, 1987.
[260] D. L. Stein, C. M. Newman, Spin Glasses and Complexity, Primers in Complex Systems, Princeton University Press,
Princeton, NY, 2013.
[261] J. M. Normand, M. L. Mehta, H. Orland, One-dimensional random Ising models, J. Phys. A: Math. Gen. 18 (1985)
621–639.
[262] H. Nishimori, Statistical Physics of Spin Glasses and Information Processing, Oxford University Press, Oxford, 2013.
[263] S. Galluccio, J.-P. Bouchaud, M. Potter, Rational decisions, random matrices and spin glasses, Physica A 259 (1998)
449–456.
[264] D. L. Stein, Spin Glasses and Biology, World Scientific, Singapore, 1992.
[265] E. Domany, Some results for the two-dimensional Ising model with competing interactions, J. Phys. C 12 (1979)
L119–L123.
[266] S. F. Edwards, P. W. Anderson, Theory of spin glasses, J. Phys. F: Metal Phys. 5 (1975) 965–974.
[267] D. Sherrington, S. Kirkpatrick, Solvable model of a spin-glass, Phys. Rev. Lett. 35 (1975) 1792–1796.
[268] D. J. Thouless, P. W. Anderson, R. G. Palmer, Solution of ’solvable model of a spin glass’, Phil. Mag. 35 (1977) 593–601.
[269] G. Parisi, Infinite number of order parameters for spin-glasses, Phys. Rev. Lett. 43 (1979) 1754–1756.
[270] G. Parisi, The order parameter for spin-glasses: A function on the interval 0-1, J. Phys. A: Math. Gen. 13 (1980)
1101–1112.
[271] G. Parisi, Order parameter for spin-glasses, Phys. Rev. Lett. 50 (1983) 1946–1948.
[272] C. M. Newman, D. L. Stein, Simplicity of state and overlap structure in finite volume realistic spin glasses, Phys. Rev.
E 57 (1998) 1356–1366.
[273] A. A. Middleton, Extracting thermodynamic behavior of spin glasses from overlap function, Phys. Rev. B 87 (2013)
220201(R).
[274] A. Billoire, A. Maiorano, E. Marinari, V. Martin-Mayor, D. Yllanes, Cumulative overlap distribution function in realistic
spin glasses, Phys. Rev. B 90 (2014) 094201.
[275] C. M. Newman, D. L. Stein, Distribution of pure states in short-range spin glasses, Int. J. Mod. Phys. B 24 (2010)
2091–2106.
[276] N. Read, Short-range Ising spin glasses: The metastate interpretation of replica symmetry breaking, Phys. Rev. E 90
(2014) 032142.
[277] Y. Imry, S. Ma, Random-field instability of the ordered state of continuous symmetry, Phys. Rev. Lett. 35 (1975)
1399–1401.
[278] J. Villain, Commensurate-incommensurate transition with frozen impurities, J. Phys. (Paris) Lett. 43 (1982) L–551–L558.
[279] J. Z. Imbrie, Lower critical dimension of the random-field Ising model, Phys. Rev. Lett. 53 (1984) 1747–1750.
[280] E. T. Gawlinski, K. Kaski, M. Grant, J. D. Gunton, Domain growth in the Ising model in a random magnetic field,
Phys. Rev. Lett. 53 (1984) 2266–2269.
[281] G. S. Grest, C. M. Soukoulis, K. Levin, Comparative Monte Carlo and mean-field studies of random-field Ising systems,
Phys. Rev. B 33 (1986) 7659–7674.
[282] N. D. Mackenzie, The 2d random-field Ising model – Monte Carlo simulations, J. Phys. C: Solid State Phys. 19 (1986)

75

563–567.
[283] C. Frontera, E. Vives, Numerical signs for a transition in the two-dimensional random field Ising model at t = 0, Phys.
Rev. E 59 (1999) R1295.
[284] G. P. Shrivastav, M. Kumar, V. Banerjee, S. Puri, Ground-state morphologies in the random-field Ising model: Scaling
properties and non-Porod behavior, Phys. Rev. E 90 (2014) 032140.
[285] P. C. Hohenberg, B. I. Halperin, Theory of dynamic critical phenomena, Rev. Mod. Phys. 49 (1977) 435–479.
[286] J. S. Langer, An introduction to the kinetics of first-order phase transition, in: C. Godreche (Ed.), Solids far from
equilibrium, Cambridge Univ. Press, Cambridge, 1992, p. 297.
[287] A. J. Bray, Theory of phase ordering kinetics, Adv. Phys. 43 (1994) 357–459.
[288] K. A. Brakke, The motion of a surface by its mean curvature, Princeton University, Princeton, 1978.
[289] R. C. Brower, D. A. Kessler, J. Koplik, H. Levine, Geometrical models of interface evolution, Phys. Rev. A 29 (1984)
1335–1342.
[290] R. E. Goldstein, D. M. Petrich, The Korteweg-de Vries hierarchy as dynamics of closed curves in the plane, Phys. Rev.
Lett. 67 (1991) 3203–3206.
[291] H. Garcke, Curvature driven interface evolution, Jahresber. Dtsch. Math. Ver. 115 (2013) 63–100.
[292] S. Biswas, P. Sen, Effect of the nature of randomness on quenching dynamics of the Ising model on complex networks,
Phys. Rev. E 84 (2011) 066107.
[293] P. Clifford, A. Sudbury, A model for spatial conflict, Biometrika 60 (1973) 581–588.
[294] M. Bramson, D. Griffeath, Clustering and dispersion rates for some interacting particle systems on z 1 , Ann. Probab. 8
(1980) 183–213.
[295] A. Lipowski, Anomalous phase-ordering kinetics in the Ising model, Physica A 268 (1999) 6–13.
[296] V. Spirin, P. L. Krapivsky, S. Redner, Fate of zero-temperature Ising ferromagnets, Phys. Rev. E 63 (2001) 036118.
[297] P. K. Das, P. Sen, Zero temperature dynamics of Ising model on a densely connected small world network, Eur. Phys.
J. B 47 (2005) 391–396.
[298] G. S. Grest, M. P. Anderson, D. J. Srolovitz, Domain-growth kinetics in for the Q-state Potts model in two and three
dimensions, Phys. Rev. B 38 (1988) 4752–4760.
[299] M. P. O. Loureiro, J. J. Arenzon, L. F. Cugliandolo, Geometrical properties of the Potts model during coarsening regime,
Phys. Rev. E 85 (2012) 021135.
[300] O. N. Senkov, G. B. Wilks, D. B. Miracle, C. P. Chuang, P. K. Liaw, Refractory high-entropy alloys, Intermetallics 18
(2010) 1758–1765.
[301] J.-W. Yeh, Alloy design strategies and future trends in high-entropy alloys, J. Metals 65 (2013) 1759–1771.
[302] R. Carroll, C. Li, C.-W. Tsai, J. Yeh, J. Antonaglis, B. A. W. Brinkman, M. LeBlanc, X. Xie, S. Chen, P. K. Liaw, K. A.
Dahmen, Experiments and model for serration statistics in low-entropy, medium-entropy, and high-entropy alloys, Sci.
Rep. 5 (2015) 16997.
[303] A. Szolnoki, G. Szabó, M. Perc, Phase diagrams for the spatial public goods game with pool punishment, Phys. Rev. E
83 (2011) 036101.
[304] A. Szolnoki, G. Szabó, L. Czakó, Competition of individual and institutional punishments spatial public goods games,
Phys. Rev. E 84 (2011) 046106.
[305] A. Hintze, C. Adami, Punishment in public goods games leads to metastable phase transitions and hysteresis, Phys.
Biol. 12 (2015) 046005.
[306] K. Shigaki, Z. Wang, J. Tanimot, E. Fukuda, Effects of initial fraction of cooperators on cooperative behavior in
evolutionary prisoner’s dilemma game, PLoS ONE 8 (2013) e76942.
[307] R. B. Griffiths, Nonanalytic behavior above the critical point in a random Ising ferromagnet, Phys. Rev. Lett. 23 (1969)
17–19.
[308] R. B. Griffiths, J. L. Lenowitz, Random spin systems: Some rigorous results, J. Math. Phys. 9 (1968) 1284–1292.
[309] R. G. Palmer, D. L. Stein, E. Abrahams, P. W. Anderson, Models of hierarchically constrained dynamics for glassy
relaxation, Phys. Rev. Lett. 53 (1984) 958–961.
[310] C. De Dominicis, H. Orland, F. Lainée, Stretched exponential relaxation in systems with random free energies, J.
Physique Lett. 46 (1985) L463–L466.
[311] M. Randeria, J. P. Sethna, R. G. Palmer, Low-frequency relaxation in Ising spin-glasses, Phys. Rev. Lett. 54 (1985)
1321–1324.
[312] A. J. Bray, The nature of the Griffiths phase, Phys. Rev. Lett. 59 (1987) 586–589.
[313] A. J. Noest, Power-law relaxation of spatially disordered stochastic cellular automata and directed percolation, Phys.
Rev. B 38 (1988) 2715–2720.
[314] A. J. Noest, New universality for spatially disordered cellular automata and directed percolation, Phys. Rev. Lett. 57
(1986) 90–93.
[315] A. G. Moreira, R. Dickman, Critical dynamics of the contact process with quenched disorder, Phys. Rev. E 54 (1996)
R3090.
[316] T. E. Harris, Contact interactions on a lattice, Ann. Prob. 2 (1974) 969–988.
[317] W. Kinzel, Phase transitions of cellular automata, Z. Phys. B 58 (1985) 229–244.
[318] H. Hinrichsen, Non-equilibrium critical phenomena and phase transitions into absorbing states, Adv. Phys. 49 (2000)
815–958.
[319] R. Dickman, A. G. Moreira, Violation of scaling in the contact process with quenched disorder, Phys. Rev. E 57 (1998)
1263–1268.
[320] M. A. Muñoz, R. Juhász, C. Castellano, G. Ódor, Griffiths phases on complex networks, Phys. Rev. Lett. 105 (2010)

76

128701.
[321] M. Droz, J. Szwabinski, G. Szabó, Motion of influential players can support cooperation in prisoner’s dilemma, Eur.
Phys. J. B 71 (2009) 579–585.
[322] G. Szabó, L. Varga, I. Borsos, Evolutionary matching-pennies game on bipartite regular networks, Phys. Rev. E 89
(2014) 042820.
[323] A. Szolnoki, G. Szabó, Vertex dynamics during domain growth in three-state models, Phys. Rev. E 70 (2004) 027101.
[324] A. Szolnoki, G. Szabó, M. Ravasz, Three-state Potts model in combination with the rock-scissors-paper game, Phys.
Rev. E 71 (2005) 027102.
[325] C. Hauert, S. De Monte, J. Hofbauer, K. Sigmund, Volunteering as Red Queen mechanism for cooperation in public
goods game, Science 296 (2002) 1129–1132.
[326] M. Nowak, K. Sigmund, Oscillation in the evolutionary reciprocity, J. Theor. Biol. 137 (1989) 21–26.
[327] E. Fehr, S. Gächter, Altruistic punishment in humans, Nature 415 (2002) 137–140.
[328] R. J. Field, R. M. Noyes, Oscillations in chemical systems. IV. Limit cycle behavior in a model of real chemical reaction,
J. Chem. Phys. 60 (1974) 1877–1884.
[329] K. Showalter, I. R. Epstein, From chemical systems to systems chemistry: Patterns in space and time, Chaos 25 (2015)
097613.
[330] N. Wiener, A. Rosenblueth, Conduction of impulses in cardiac muscle, Arc. Inst. Cardiol. (Mexico) 16 (1946) 205–265.
[331] H. Hempel, L. Schimansky-Geier, J. Garcia-Ojalvo, Noise-sustained pulsating patterns and global oscillations in subexitable media, Phys. Rev. Lett. 82 (1999) 3713–3716.
[332] W. O. Kermack, A. G. McKendrick, A contribution to the mathematical theory of epidemics, Proc. R. Soc. A 115 (1927)
700–721.
[333] R. Durrett, S. Levin, Allelopathy in spatial distributed populations, J. Theor. Biol. 185 (1997) 165–171.
[334] B. Kerr, M. A. Riley, M. W. Feldman, B. J. M. Bohannan, Local dispersal promotes biodiversity in a real-life game of
rock-paper-scissors, Nature 418 (2002) 171–174.
[335] E. Frey, T. Reichenbach, Bacterial games, in: H. Meyer-Ortmanns, S. Thurner (Eds.), Evolution: From the Planck
Epoch to Complex Multicellular Life, Springer Berlin Heidelberg, 2011, pp. 297–329.
[336] K. Tainaka, Paradoxial effect in a three-candidate voter model, Phys. Lett. A 176 (1993) 303–306.
[337] K. Tainaka, Indirect effect in cyclic voter models, Phys. Lett. A 207 (1995) 53–57.
[338] K. Tainaka, N. Araki, Press perturbation in lattice ecosystems: Parity law and optimum strategy, J. Theor. Biol. 197
(1999) 1–13.
[339] K. Sato, N. Yoshida, N. Konno, Parity law for population dynamics of n-species with cyclic advantage competition,
Appl. Math. Comp. 126 (2002) 255–270.
[340] G. Szabó, A. Szolnoki, G. A. Sznaider, Segregation process and phase transition in cyclic predator-prey models with
even number of species, Phys. Rev. E 76 (2007) 051921.
[341] R. M. May, Hypercycles spring to life, Nature 353 (1991) 607–608.
[342] G. Szabó, Competing associations in six-species predator-prey models, J. Phys. A: Math. Gen. 38 (2005) 6689–6702.
[343] P. Szabó, T. Czárán, G. Szabó, Competing associations in bacterial warfare with two toxins, J. Theor. Biol. 248 (2007)
736–744.
[344] G. Szabó, A. Szolnoki, I. Borsos, Self-organizing patterns maintained by competing associations in six-species predatorprey model, Phys. Rev. E 77 (2008) 041919.
[345] S. Rulands, T. Reichenbach, E. Frey, Threefold way to extinction in populations of cyclically competing species, J. Stat.
Mech. (2011) L01003.
[346] J. Vukov, A. Szolnoki, G. Szabó, Diverging fluctuations in a spatial five-species cyclic dominance game, Phys. Rev. E
88 (2013) 022123.
[347] A. Dobrinevski, M. Alava, T. Reichenbach, E. Frey, Mobility-dependent selection of competing strategy associations,
Phys. Rev. E 89 (2014) 012721.
[348] S. S. Wiltermuth, C. Heath, Synchrony and cooperation, Psychological Science 20 (2009) 1–5.
[349] S. Wolfram, Statistical mechanics of cellular automata, Rev. Mod. Phys. 55 (1983) 601–644.
[350] C. G. Langton, Studying artificial life with cellular automata, Physica D 22 (1986) 120–149.
[351] L. Varga, J. Vukov, G. Szabó, Self-organizing patterns in an evolutionary rock-paper-scissors game for stochastic synchronized strategy updates, Phys. Rev. E 90 (2014) 042920.
[352] D. M. Abrams, S. H. Strogatz, Chimera states for coupled oscillators, Phys. Rev. Lett. 93 (2004) 174102.
[353] D. Dudkowski, Y. Maistrenko, T. Kapitaniak, Different types of chimera states: An interplay between spatial and
dynamical chaos, Phys. Rev. E 90 (2014) 032920.
[354] M. S. Santos, J. D. S. Jr., A. M. Batista, I. L. Caldas, R. L. Viana, S. R. Lopes, Recurrence quantification analysis of
chimera states, Phys. Lett. A 379 (2015) 2188–2192.
[355] C. R. Laing, Chimera in networks with purely local coupling, Phys. Rev. E 92 (2015) 050904(R).
[356] J. Xie, E. Knobloch, H.-C. Kao, Twisted chimera states and multicore spiral chimera states on two-dimensional torus,
Phys. Rev. E 92 (2015) 042921.

77

