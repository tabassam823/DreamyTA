Physica A 389 (2010) 481–489

Contents lists available at ScienceDirect

Physica A
journal homepage: www.elsevier.com/locate/physa

Ising model versus normal form game
Serge Galam a , Bernard Walliser b,∗
a

Centre de Recherche en Épistémologie Appliquée, École Polytechnique, CNRS UMR 7656, France

b

Paris School of Economics, ENS-EHESS-ENPC, CNRS UMR 8545, France

article

info

Article history:
Received 20 February 2009
Received in revised form 6 August 2009
Available online 23 September 2009
Keywords:
Econophysics
Ising model
Sociophysics
2 × 2 game

abstract
The 2-spin Ising model in statistical mechanics and the 2 × 2 normal form game in game
theory are compared. All configurations allowed by the second are recovered by the first
when the only concern is about Nash equilibria. But it holds no longer when Pareto optimum considerations are introduced as in the prisoner’s dilemma. This gap can nevertheless
be filled by adding a new coupling term to the Ising model, even if that term has up to now
no physical meaning. An individual complete bilinear objective function is thus found to be
sufficient to reproduce all possible configurations of a 2 × 2 game. Using this one-to-one
mapping new perspectives for future research in both fields can be envisioned.
© 2009 Elsevier B.V. All rights reserved.

1. Introduction
For two decades, statistical mechanics has been more and more used to study economic systems [1–3] as well as financial
ones [4]. A well-known example is the application of statistical mechanics to minority games on the basis of some financial
problems [5]. Such a transfer is generally grounded on a raw analogy, both fields sharing the existence of numerous entities
which are able to be in specific states and interact among themselves. Each entity is governed by the optimization of an
objective function depending on the states of all of them. The process leads to an overall equilibrium state. However, even
if the formal frame is rather similar, the interpretation underlying the maximization process is very different. While spins
are inert objects which obey objective laws, human beings follow an intentional behavior. Hence, the analogy is not really
substantial, but may nevertheless be valid at a formal level.
In this paper, two standard models of each discipline are compared, the Ising model at zero temperature for statistical
mechanics and the normal form with Nash equilibrium for game theory. When both models are restricted to two entities and
two state variables, a detailed comparison becomes possible. While in statistical mechanics the individual objective function
is an explicit truncated bilinear function in both entities, in game theory it is a quite general function with no specification.
On this basis, the possible configurations of equilibrium states are computed in each case and systematically compared.
It appears that any configuration happening in the first case appears as well in the second. However, when one introduces
Pareto optimum considerations as in the prisoner’s dilemma, this is no more true. However, the prisoner’s dilemma missing
configuration can be recovered by adding an additive new term to the Ising objective function. This additional term makes
the associated bilinear function complete. It is a linear term which at present has no physical meaning. Nevertheless, an
individual bilinear objective function which is complete is sufficient to reproduce all possible configurations of game theory.
The remainder of the paper is organized as follows. The second section recalls the frameworks used in statistical
mechanics and in game theory and compares their respective assumptions. The third section analyzes the configurations
of equilibrium states obtained in games when using the restrictive individual objective function of the Ising model. The
fourth section shows that the missing configuration can be recovered by considering a complete individual bilinear objective
function, but can no longer be obtained from a collective objective function. Some perspectives for new research in both
fields using our mapping are discussed in the last section.

∗ Corresponding author. Tel.: +33 1 45 35 43 06.
E-mail addresses: serge.galam@polytechnique.edu (S. Galam), walliser@mail.enpc.fr (B. Walliser).
0378-4371/$ – see front matter © 2009 Elsevier B.V. All rights reserved.
doi:10.1016/j.physa.2009.09.029

482

S. Galam, B. Walliser / Physica A 389 (2010) 481–489

2. Basic frameworks
2.1. Ising model
In statistical mechanics, the Ising model is most used. Rather powerful to study magnetic systems, it was proven
successful in describing a huge spectrum of different problems in other fields of physics. Numerous applications have been
also achieved outside physics in particular in sociophysics [6,7].
The Ising model considers a group of N two-state variables called spins, where each spin i = 1, . . . , N, takes values
denoted si = ±1. These spins interact by pairs {i, j} via two exchange constants Jij and Jji whose effect is to produce
respectively a local field hj−→i = Jij sj from spin j on spin i and a local field hi−→j = Jji si from spin i on spin j. These fields
couple linearly with their associated spins giving rise to the two individual energies:
Ei = −hj−→i si = −Jij sj si
Ej = −hi−→j sj = −Jji si sj
which are both bilinear functions of the spins.
The minus sign remembers that the energy is ultimately minimized. A positive coupling Jij  0 corresponds to a
ferromagnetic system and yields: si = sj . A negative coupling Jij ≺ 0 corresponds to a antiferromagnetic system and favors:
si = −sj . The absence of coupling Jij = 0 makes both values of si and sj independent one from the other.
Then, considering one spin si, all its interactions with the other (N − 1) spins add up to result in a net local field:
Vi =

N
X

Jij sj ,

with Jii = 0.

j =1

At this stage, in order to satisfy the principle of equality of action and reaction which holds true for most physical
applications, the exchange couplings are taken symmetric: Jij = Jji .
In addition, spins can be coupled linearly to a local field h̃i , which may vary from spin to spin like in the random field
model. It is independent of the spin states. A uniform field h can also be applied to the system. It couples linearly and
simultaneously to every spin. These coupling terms write respectively h̃i si and hsi . Both h̃i and h can be positive, negative or
null. In physics, discriminating between h̃i and h originated from the different experimental schemes which produce them
respectively. On a more formal point of view, they can be combined within one single local variable: hi = h̃i + h.
The total local field becomes:
Vi =

N
X

Jij sj + hi

j =1

and the associated individual energy:
Ei = −

N
X

Jij si sj − hi si .

j =1

It is worth to note that a self-coupling term with i = j may be included in Ei . However since si si = 1, it contributes a
constant Jii to Ei , which therefore does not influence the equilibrium state. In the special case where Vi = 0, the associated
spin si is said to be ‘‘frustrated’’ since neither si = +1 nor si = −1 can minimize Ei = 0. It makes a spin flip cost no energy.
The total energy of the N-spin system is then obtained by adding all individual energies Ei which defines the Hamiltonian
under two equivalent forms:

H =−

X

Jij si sj −

hi,ji

X

hi s i

(1)

X

(2)

i
N

H0 = −

1X
2 i ,j = 1

Jij si sj −

hi s i

i

where hi, ji means all distinct pairs of interacting spins and 1/2 corrects the double counting of each pair. In other
circumstances, the system may stabilize into some limit cycle.

The Hamiltonian measures the energy of a peculiar configuration {s1 , s2 , . . . , sN } given the external parameters Jij , hi .
It is sufficient to describe the equilibrium properties of the system.
Observe that minimizing the Hamiltonian with respect to the states {si } is identical to minimizing each {Ei } with respect
to si . However, it should be emphasized that this feature is a direct result of the assumption of symmetric couplings (Jij = Jji ).
Indeed, the term Jij may be virtually asymmetric (Jij 6= Jji ). In that case, the energy function cannot characterize uniquely the
system since then the asymmetric part waves out in summing both terms Jij si sj and Jji sj si in H due to the commutation of si
and sj resulting in one average coupling term (Jij + Jji )/2 which is symmetric. Therefore, for asymmetric couplings, a purely
dynamical analysis is required making the solving of the problem much more difficult.

S. Galam, B. Walliser / Physica A 389 (2010) 481–489

483

Observe moreover that, on purely formal grounds, hi can be taken as positive without restriction. Exchanging the sign of
si preserves the value of Ei if changing altogether the signs of Jij and hi .
At this stage, to make the comparison to game theory straightforward, we restrict the approach to two spins: N = 2,
even if the physical interpretation is dubious. The local fields becomes:
V1 = J21 s2 + h1

and

V2 = J12 s1 + h2 .

(3)

The individual energies follow:
E1 = −J21 s1 s2 − h1 s1

and V2 = −J12 s1 s2 − h2 s2 .

(4)

Finally, the Hamiltonian reduces to:
1

H10 ,2 = − (J12 + J21 )s1 s2 − h1 s1 − h2 s2 .

(5)

2

On this basis, the equilibrium state is obtained by a minimization of H 0 with respect to both {s1 , s2 } given {J12 , J21 , h1 , h2 }.
Hence −H 0 is a collective objective function which is maximized with respect to the two internal degrees of freedom {s1 , s2 }.
Remember that h1 and h2 can be taken positive without restriction.
In the case of symmetric exchange couplings (J12 = J21 ), the minimization of E1 with respect to s1 and E2 with respect to
s2 is precisely equivalent to the minimization of H with respect to {s1 , s2 }. The functions E1 and E2 are therefore individually
minimized, hence their opposite are individual objective functions which are maximized.
2.2. Game theory
In game theory, the standard ‘‘normal form’’ is most used. It applies to many economic applications as well as to
applications in other fields like political science or biology.
The framework considers a group of N players numerated with i = 1, . . . , N. Each player i chooses some action si in a
set Si ,which is defined on a nominal (discrete) scale rather than on a numerical one. The players interact globally through
their actions and reach some common consequences C for each issue (s1 , . . . , si , . . . , sN ). These consequences are assessed
by each player i thanks to a utility or payoff function Ui = Ui (C ) = Ui (s1 , . . . , si , . . . , sN ). Such a utility index is ordinal,
hence the utility function, otherwise of any form, is defined up to a monotone transformation. Finally, each player chooses
his action by maximizing his utility.
Since the maximization implemented by some player depends on what the other players do, an equilibrium notion has
to be defined in order to coordinate the players’ moves. A Nash equilibrium state is a stable state in a fixed environment,
provided that one player only is able to deviate from it at a time. Technically, a (pure) Nash equilibrium state is an ‘issue’ (or
‘state’ or ‘profile of actions’ (s∗1 , . . . , s∗i , . . . , s∗N ) where each action is a best response to the others’ equilibrium actions:
s∗i = arg max Ui (s∗1 , . . . , si , . . . , s∗N ).

(6)

si

In other terms, in an equilibrium state, no player has an incentive to deviate unilaterally from his action:
Ui (s∗1 , . . . , s∗i , . . . , s∗N ) ≥ Ui (s∗1 , . . . , si , . . . , s∗N ), ∀si .

(7)

A Nash equilibrium is strict if and only if the inequality is strict for each player. In fact, the equilibrium conditions state that
if the players are placed in an equilibrium state, they stay there. But they do not explain through what dynamical process
the players come to an equilibrium state.
The Nash equilibrium notion assumes that the players follow their own individual interests (embedded in their utility
function which gathers heterogeneous motivations). The Pareto optimum notion considers a collective point of view
(however based on the individual utility functions). It asserts that a state is a Pareto optimum if there exists no other available
state which is better for all players (and strictly better for one of them at least). Technically, it is defined in two steps. Firstly,
an issue (s1 , . . . , si , . . . , sN ) Pareto dominates another issue (s01 , . . . , s0i , . . . , s0N ) if it gives more utility to each player (and
strictly more to one of them)
Ui (s1 , . . . , si , . . . , sN ) ≥ Ui (s01 , . . . , s0i , . . . , s0N ),

∀i,

(8)

with one strict inequality. Secondly, a Pareto optimum is an issue which is not Pareto dominated by any other issue. However,
even if a collective order on global states is considered, no collective objective function is assumed to exist.
The game is now restricted to two players and two actions per player, i.e. a 2 × 2 game. It is usually represented by a
matrix where the lines represent the two actions s11 and s21 of the first player and the columns the two actions s12 and s22 of
the second player. At the intersection of an action for each player, the bi-matrix indicates first the utility of the first player,
then the utility of the second player:
s12
s11
s21

(U1 (s11 , s12 ), U2 (s11 , s12 ))
(U1 (s21 , s12 ), U2 (s21 , s12 ))

s22

(U1 (s11 , s22 ), U2 (s11 , s22 ))
(U1 (s21 , s22 ), U2 (s21 , s22 ))

484

S. Galam, B. Walliser / Physica A 389 (2010) 481–489

This bi-matrix has indeed quite a general form and can be written with 8 free parameters:

( a, a0 )
(c , c 0 )

(b, b0 )
(d, d0 )

Two classes of games are of special interest. The symmetric games are such that the two players play symmetric roles and
get symmetric utilities: a = a0 , b = c 0 , c = b0 , d = d0 . The zero-sum games are such that the utilities of the players are
opposite for each issue of the game: a = −a0 , b = −b0 , c = −c 0 , d = −d0 . In case of a symmetric game, it exists at least one
equilibrium state while in case of a zero-sum game, it exists at most one equilibrium state.
In the bi-matrix, the (pure) Nash equilibria are obtained as ‘wells’ of the best response arrows relating horizontal or vertical
issues in the matrix. The Pareto optima are obtained by eliminating all dominated issues. The two types of states need not to
coincide. For instance, consider the game with: a  c  d  b, c 0 = d0  a0  b0 . The best responses, the Nash equilibria (a
strict Nash equilibrium is denoted N while a large one is denoted N 0 ) and the Pareto optima (denoted P) are the following:
N =P

←−

↑
P

↓
N0

←→

Observe that the equilibrium states are unchanged under a monotone transformation of U1 and U2 . Especially, they are
not affected when adding to U1 (and U2 ) a constant in the first column and another in the second:

(a + λ, a0 + λ0 )
(c + λ, c 0 + λ0 )

(b + µ, b0 + µ0 )
(d + µ, d0 + µ0 )

Likely, the Pareto dominating issues are unchanged under a linear transformation of U1 and U2 . Especially, they are
unchanged when adding to U1 (and U2 ) a same constant in all issues:

(a + λ, a0 + λ0 )
(c + λ, c 0 + λ0 )

(b + λ, b0 + λ0 )
(d + λ, d0 + λ0 )

Note however that such transformations do not keep the symmetric or zero-sum character of the game.
2.3. Correspondence between the frames
The two frameworks appear quite similar in their structure: a spin is replaced by a player, the state si by an action si ,
the local energy −Ei by a utility function Ui , a physical equilibrium by a Nash equilibrium. But the Hamiltonian H has no
counterpart since no collective utility (linear or not) is defined. However, the physical structure is logically stronger than
the game structure since the state is quantified and the energy is more specific (truncated bilinear function of the variables).
The physical problem can be transformed into a game problem by constructing an equivalent normal form for a game.
The 2 × 2 matrix gives in each issue the energy of spins 1 and 2, the issues corresponding to the combinations of first and
second states for the spins. We thus get the ‘Ising game’ matrix which is comparable to the one obtained from game theory:
s12 = +1

(J12 + h1 , J21 + h2 )
(−J12 − h1 , −J21 + h2 )

s11 = +1
s21 = −1

s22 = −1

(−J12 + h1 , −J21 − h2 )
(J12 − h1 , J21 − h2 )

The same previous general form can be used, but it involves now only 4 free parameters since the off diagonal payoffs
depend on the diagonal payoffs in the following way:

(α, α 0 )
(−α, −δ 0 )

(−δ, −α 0 )
(δ, δ 0 )

with α = J12 + h1 , α 0 = J21 + h2 , δ = J12 − h1 and δ 0 = J21 − h2 . Note that the correspondence can be reversed since
J12 = (α + δ)/2, h1 = (α − δ)/2, J21 = (α 0 + δ 0 )/2, h2 = (α 0 − δ 0 )/2.
The Ising game is symmetric when α = α 0 and δ = δ 0 , which involves that: J12 = J21 and h1 = h2 . It is zero-sum when
α = δ = −α 0 = −δ 0 , which involves J12 = −J21 and h1 = h2 = 0.
If we are interested only in equilibrium states, it is always possible to change a usual game into an equivalent Ising game
by adding to the utilities some specific constants:

λ = −(a + c )/2,

µ = −(b + d)/2,

λ0 = −(a0 + c 0 )/2,

µ0 = −(b0 + d0 )/2.

The new utilities become related to the old ones as follows:

α = (a − c )/2,

δ = (d − b)/2,

α 0 = (a0 − c 0 )/2,

δ 0 = (d0 − b0 )/2.

S. Galam, B. Walliser / Physica A 389 (2010) 481–489

485

Moreover, the physical parameters can be directly related to the old utilities:
J12 = (a − b − c + d)/2,

h1 = (a + b − c − d),

J21 = (a0 − b0 − c 0 + d0 )/2,

h2 = (a0 + b0 − c 0 − d0 ).

However, if we are interested in Pareto optima, the same operation cannot be done since the constants generally differ
along lines and columns.
3. Comparison of equilibrium states
3.1. Taxonomy of 2 × 2 games
In general 2 × 2 games, we are looking for the different types of equilibrium configurations that may happen. For this,
it is enough to consider that the payoffs of a player are defined up to a monotone transformation, hence are defined on an
ordinal scale. Even more we have only to consider the relative position of the payoffs leading to the best responses. It means
that we have just to compare a to c and b to d. Such a reasoning concerns in fact the vertical arrows in the basic scheme. We
obtain only 9 combinations:
– 2 combinations A without ties and opposite moves: ↑↓ or ↓↑
– 2 combinations B without ties and parallel moves: ↑↑ or ↓↓
– 2 combinations C with one tie right: ↑l or ↓l
– 2 combinations D with one tie left: l↑ or l↓
– 1 combination E with two ties: ll
For two players, we obtain in principle 9 × 9 = 81 combinations. But a matrix obtained by exchanging lines or columns
gives the same equilibrium states since there is only a change of label of the actions. However, for some matrices, exchanging
lines or columns can lead to the same matrix. In fact, the exchange properties of the different combinations are the following:
– combinations A exchange themselves when exchanging lines and similarly when exchanging columns.
– combinations B exchange themselves when exchanging lines and are invariant when exchanging columns
– combinations C exchange themselves when changing lines and lead to configurations D when exchanging columns
– combinations D exchange themselves when changing lines and lead to configurations C when exchanging columns
– combination E is invariant when changing lines as well as when changing columns.
It is clear that only one of the two combinations B, C and D needs to be kept for each player since the other is obtained by
exchanging the lines (for player 1) and the columns (for player 2). Similarly, the unique combination E has to be kept. A first
problem happens however with configurations A. Keeping one combination for player 1 is enough when crossing with any
other combination for player 2. But when crossing one combination A for player 1 and one combination B for player 2 is not
enough since two different configurations are concretely produced. A second problem appears with configuration E. Since it
is completely symmetric, its adoption by player 1 gives the same configuration against the combinations C and D of player
2, hence one has to be deleted.
The following table makes precise the 15 different configurations that can be obtained:
A
A

−→
↑

[1]

↓

←−
B

B
N

←−

↑

[2]

−→

↓

N

←−

↑

[3]

C

↓

N

←−

↑

[5]

↓

←→

0

←−

N
N

←−

↑

[4]

↑

N

←−

↑

[6]

←−
C

D

E

D
0

←→

↑

[8]

N
N

↑

E
N

↓

0

↑

←−

←−
[7]

l

←→

N0

↓
N0

←→

N0

N0

←→

N0

↑

[9]

↑

↑

[13]

↑

←−

↑

[12]

←→

N0

←→
N

←→

←→

N0

←→

N0

N0

←→

↑

[10]

l

↑

[14]

l

←→

N0

N0

←→

N0

l

[15]

l

N0

←→

N0

←−
N0

←→

N0

l

[11]

↑

N0

←−

N0

The four configurations without ties are the basic ones and can each can be illustrated by a specific example:
– configuration 1 corresponds to the absence of a Nash equilibrium state. It is illustrated by ‘‘matching pennies’’ where
both players exhibit one of the two sides of a personal penny; the first wins if the two pennies are on the same side while
the second wins if they are on opposite sides

(1, −1)
(−1, 1)

(−1, 1)
(1, −1)

486

S. Galam, B. Walliser / Physica A 389 (2010) 481–489

– configuration 2 corresponds to two Nash equilibrium states. A first subcase happens when the two equilibria cannot be
compared: one is better for the first player and the other is better for the second player. It is illustrated by the ‘‘battle
of the sexes’’ where player 1 is the husband and player 2 the wife; for the husband, the first action consists in going to
boxing and the second to ballet; for the wife, the first action consists in going to ballet and the second to boxing; the utility
of preferred entertainment is 2 and the utility of being together to 4. A second subcase happens when one equilibrium
Pareto dominates the other. It is illustrated by the ‘‘stag hunt game’’ where for each player, the first action consists in
hunting a rabbit and the second a deer; the rabbit can be hunt alone and provides then a utility of 1; the deer can only be
hunt conjointly and provides a utility of 7 for each; if only one player hunts the deer, he will starve and his utility is −1.

(2, 2)
(4, 6)

(6, 4)
(0, 0)

(7, 7)
(1, −1)

(−1, 1)
(1, 1)

– configuration 4 corresponds to one Nash equilibrium obtained by dominant actions for each player. A first subcase
happens when the Nash equilibrium is not Pareto dominated by another issue. It is illustrated by the ‘‘lonely game’’
where each player buys a toy independently from the other’s action; the utility of the toy for each player is +1 and the
disutility of not buying is −1. A second subcase happens when the Nash equilibrium is Pareto dominated by another
issue. It is illustrated by the ‘‘prisoner’s dilemma’’ where for each player, the first action consists in defecting and the
second in cooperating; they get utility 2 if both defect, utility 4 if both cooperate, but if one cooperates without the other,
he receives 0 and the other receives 6; the only equilibrium state is the issue (2, 2); but the last is not a Pareto optimum
(contrary to all other three issues) since it is Pareto dominated by the opposite issue (4, 4)

(1, 1)
(−1, 1)

(1, −1)
(−1, −1)

(2, 2)
(0, 6)

(6, 0)
(4, 4)

3.2. Taxonomy of Ising games
The Nash equilibrium states can be computed and the configurations they determine depend only on the relation between
Jij and hi . The matrix defined by these parameters isolate 25 basic configurations. For each configuration, the scheme of best
responses in the 2 × 2 matrix is defined in the following table in which h1 and h2 are strictly positive:
J21 < −h2

−→

N

↓

[2]

↑

N

←−

J12 < −h1

0

←→

N

↓

[5]

↑

N

←−

[3]

N

[8]

←−

N0

←→

N0

←−

l

[10]

N0

←→

N

←−

↑

[6]

N0

←→

N0

N0

←−

l

[5]

↑

l

[11]

↑

l

[9]

N0

←−

N0

←−

N0

←−

−h1 < J12
J12 < h1

↑

−→

N

N0

←→

N0

N

←−

[3]

↑

↑

[9]

↑

↑

[4]

←−
↑

←−
N0

N0

←→

N0

N

←−

[8]

l

↑

[10]

l

↑

[6]

←−

−→

J12 > h1

↑

[1]

↓

N0

←→

↑

[8]

←−

↑

↑

↑

←−

−→
←−

←−
↓

N

N

←−

↑

[3]

←−

←−
↑

[1]

↓

l

↓

N0

↑

←−
[8]

l

↑

−→
←−

N

↑

[3]

↑

↑

−→

N

←−

↑

[7]

l

←→

N0

N

N

←−

↑

[5]

↓

←→

N0

←−

↑

−→

←→

←−
↓

J21 > h2

J21 = h2

←−
↓

−→

J12 = −h1

J12 = h1

−h2 < J21 < h2

J21 = −h2

←−
[5]

l

−→

N0

↑

←−

N

[2]

↓

−→

N

↑

The preceding table has to be completed by a table where h1 = 0, h2 > 0 (or symmetrically):
J21 < −h2
J12 < 0

J12 = 0

J12 > 0

−h2 < J21 < h2

J21 = −h2

−→

N

↓

[2]

↑

N

←−

0

←→

N

↓

[5]

↑

N

←−

←−
↓

[3]

N

←−

N

←→

N0

←−

l

[14]

l

N0

←→

N0

N

←−

↑

[5]

↓

←→

N0

N0

←→

N0

N0

←−

l

[12]

l

l

[14]

l

l

[13]

N0

←−

N0

←−

N0

←−

N

←→

N

←−

↑

[8]

↑

[3]

[1]

←−

↓

←−

↓

←−

[8]

N0

−→

←−
↓

−→

↑

J21 > h2

J21 = h2

←−

↑

l

↓

↑

↓

[1]

↑

−→
N

l

←−
[12]

l

−→
N

↑

←−
[2]

↓

−→

N

S. Galam, B. Walliser / Physica A 389 (2010) 481–489

487

Finally, a last table is obtained when h1 = h2 = 0:
J21 < 0
J12 < 0

J12 = 0

J12 > 0

J21 > 0

J21 = 0
0

−→

N

↓

[2]

↑

N0

←−

0

←→

N

↓

[12]

↑

N0

←→

←−
↓

−→

N0

N0

←→

N0

N0

l

[12]

l

l

[15]

l

l

N0

←−

N0

←→

N0

−→

N0

←→

↑

[12]

↓

←→

N0

↑

[1]

↓

←−

[1]

↑

−→

N0

↑

←−
[12]

l

−→

N0

←−
[2]

↓

−→

N0

Of course, many configurations appear twice by symmetry. But more important, all configurations appear as expected.
The first table gives configurations 1 to 11. The second table adds the configurations 12 to 14. The third table adds the
configuration 15.
Notice that the game may be symmetric only in configurations 2, 4, 7,11 and 15. It can be checked that it then admits at
least one equilibrium state. Likely, the game may be zero-sum only in configurations 1 and 15. It then admits either zero or
four Nash equilibrium states.
The games without ties can be obtained from Ising models for specific parameters:
– configuration 1 (no equilibrium state) is obtained when Jij Jji < 0 and |Jij | > |hi |. Especially, matching pennies is obtained
with J12 = 1, J21 = −1 and h1 = h2 = 0.
– configuration 2 (two strict equilibrium states) is obtained when Jij Jji > 0 and |Jij | > |hi |. Especially, the battle of sexes is
obtained with J12 = J21 = −2 and h1 = h2 = 1 and a general translation of utility of 3. The stag hunt game is obtained
with J12 = J21 = 2 and h1 = h2 = +1 and a general translation of utility of 4
– configuration 4 (one strict equilibrium state) is obtained when |Jij | < |hi |. Especially, the lonely game is obtained for
J12 = J21 = 0 and h1 = h2 = 1.
4. Extended framework
4.1. Missing configurations
In the preceding framework, only the point of view of Nash equilibrium states was considered. A Nash equilibrium
corresponds to a state where the players may stay, when they are constrained to strictly follow their own interest. But
the game theorists are interested in Pareto optima too (especially when they coincide with equilibrium states). The reason
is that an issue which is not Pareto optimal is not collectively satisfying since the players may move to a better issue for
both, however by coordinating their actions.
Consider an Ising game where the North-West issue (α, α 0 ) is an equilibrium and the South-West issue (δ, δ 0 ) is not. The
corresponding conditions are α  0, α 0  0 and δ ≺ 0, δ 0 ≺ 0. It follows immediately that the North-West issue (α, α 0 )
Pareto dominates the South-West one (δ, δ 0 ). The opposite dominance is not possible, hence some games which precisely
show such an opposite dominance cannot be represented by Ising games.
For instance, consider the ‘‘prisoner’s dilemma’’. The North-West issue (where both players defect) is the only equilibrium
state. The South-West issue (where both players cooperate) is better for both players to the opposite one. Hence, the
prisoner’s dilemma, with its specific structure of a unique Nash equilibrium Pareto dominated by a non-equilibrium issue,
cannot be written as an Ising game.
4.2. Enlarged framework
In order to recover the missing configuration within the Ising model and thus get a full matching of configurations, the
simplest way is to add to the local energy of each spin an ‘altruistic’ term ki sj , which depends exclusively on the other spin
state:

− Ei = −

X

Jij si sj − hi si − ki sj .

(9)

j

In fact, such an operation transforms, for player i, his initial payoff in a payoff where ki is added in the first column
and where ki is subtracted in the second column. Such an operation does not change the equilibrium states (even if it
changes the payoffs at equilibrium), but does change the Pareto states. The ‘extended Ising game’ writes now in the form of a

488

S. Galam, B. Walliser / Physica A 389 (2010) 481–489

general game:
s12 = +1

(J12 + h1 + k1 , J21 + h2 + k2 )
(−J12 − h1 + k1 , −J21 + h2 − k2 )

s11 = +1
s21

= −1

s22 = −1

(−J12 + h1 − k1 , −J21 − h2 + k2 )
(J12 − h1 − k1 , J21 − h2 − k2 )

This matrix is written under the form:

( a, a0 )
(c , c 0 )

0

(b, b )
0
(d, d )

with a = J12 + h1 + k1 , b = −J12 + h1 − k1 , c = −J12 − h1 + k1 and d = J12 − h1 − k1 for player 1 and similarly
for player 2. However, the coefficients of the first player still obey the constraint: a + b + c + d = 0 (and symmetrically
for the second). But this condition can always be reached from the original matrix by subtracting to the coefficients of the
first player a constant (a + b + c + d)/4 to all payoffs (without changing the equilibrium and Pareto states). The preceding
formulas can then be reversed (for the first player):
J12 = (a − b − c + d)/4 = (a − b − c + d)/4
h1 = (a + b − c − d)/4 = (a + b − c − d)/4
k1 = (a − b + c − d)/4 = (a − b + c − d)/4.
Hence, a complete bilinear function is sufficient to obtain all possible configurations.
For instance, the prisoner’s dilemma is obtained by setting J12 = J21 = 0, h1 = h2 = 1 and k1 = k2 = −2, and applying
a general payoff transformation of +3.
4.3. The ‘altruistic’ term
At this stage, two comments can be made about the ‘altruistic term’ added to the energy of each spin. First, this term has
no clear interpretation in statistical mechanics. Second, the completed energy cannot be deduced from a collective single
Hamiltonian.
If such an Hamiltonian existed, he would be obtained by ‘integrating’ the new energy of each spin Vi , obtained by dividing
−Ei by si :

∂H
= J12 s2 + h1 + k1 s2 /s1
∂ s1
∂H
V2 =
= J21 s1 + h2 + k2 s1 /s2 .
∂ s2
V1 =

(10)
(11)

But since the second derivatives ∂∂s ∂Hs and ∂∂s ∂Hs differ, the Hamiltonian does not exist.
1 2
2 1
Conversely, consider the Hamiltonian obtained by adding the energy of both spins.
2

2

H 0 = J12 s1 s2 + J21 s1 s2 + h1 s1 + h2 s2 + k1 s2 + k2 s1 .

(12)

It leads to individual spin energies which are not the good ones, but it allows to find the Pareto optimum in the prisoner’s
dilemma. Hence, the missing configuration, contrary to the other ones, cannot be obtained by minimizing a Hamiltonian.
5. Further extensions
Extension to continuous positions for each entity is usual in games as well as in statistical mechanics and their comparison
can be extended. But extension to N entities creates a further divergence between statistical mechanics and game theory.
In statistical mechanics, the energy of a spin is generally generated by summarizing its bilateral interactions with all other
spins. Multilateral interactions are possible in some cases, but are more difficult to handle mathematically. In economics,
the utility is directly defined on a multilateral basis, by a general dependence on all others’ actions. Again, it is not specified,
but only submitted to very general conditions. It follows that the additional term(s) needed to recover a general function
from a partial one will be intricate.
Two problems stay common to statistical mechanics and game theory. In both cases, the equilibrium state is defined
from outside (by the modeler) as a state which remains stable without perturbations from the environment. But the concrete
process leading to some well-defined equilibrium state is not formally described. Hence, the ‘implementation problem’ states
that the process leading to an equilibrium state has to be made explicit. Likely, the ‘selection problem’ states that the way one
equilibrium state is sorted out in case of multiplicity has to be made explicit, in relation with the preceding one. In physics,
a random selection is often assumed with equiprobability.

S. Galam, B. Walliser / Physica A 389 (2010) 481–489

489

In game theory, two justifications of an equilibrium notion were recently proposed and duly formalized [8]. The epistemic
justifications assume that the players are hyper-intelligent and are able to reach instantaneously an equilibrium state by
their sole reasoning. Moreover, the players select one equilibrium state through shared ‘conventions’, for instance focal
points (culturally induced). The evolutionist justifications assume that the players have a bounded rationality and follow a
sequential learning or evolution process leading asymptotically to an equilibrium state. In that case, an equilibrium state is
automatically selected at least probabilistically by the initial conditions and the history of the system.
In statistical mechanics, only the second option is open since the spins can hardly be assumed to hold beliefs and to
deliberate. Nevertheless the sociophysics approach has proven possible to substitute individuals to spins as long as the
assumptions made are formally equivalent. In fact, various schemes were proposed in order to describe the local dynamic
genesis of an equilibrium state, with more or less justifications. They allow the convergence towards an equilibrium state
by using the concept of spontaneous symmetry breaking.
Finally, statistical mechanics studies the system of spins even when the temperature differs from zero. A spin is
then in some state with a probability precisely defined which decreases with its energy and increases with the inverse
of the temperature. In game theory, the corresponding situation happens when a player chooses an action with a
probability generically defined which increases with its utility and depends on some parameter characterizing the
‘exploration–exploitation’ dilemma. The corresponding equilibrium states have to be further compared.
References
[1] M. Blume, The statistical mechanics of strategic interaction, Games and Economic Behavior 5 (1993) 387–424.
[2] A. Kirman, J.B. Zimmermann (Eds.), Economics with Heterogenous Interacting Agents, Springer, 2001.
[3] P. Bourgine, J.P. Nadal (Eds.), Cognitive Economics, Springer, 2004.
[4] H.S. Bhamra, Imitation in financial markets, International Journal of Theoretical and Applied Finance 3 (3) (2000) 473–478.
[5] A.C.C. Coolen, The Mathematical Theory of Minority Games: Statistical Mechanics of Interacting Agents, Oxford University Press, 2005.
[6] C. Castellano, S. Fortunato, V. Loreto, Statistical physics of modern dynamics, Reviews of Modern Physics 81 (2009) 591–646.
[7] S. Galam, Sociophysics: A review of Galam models, International Journal of Modern Physics C 19 (3) (2008) 409–440.
[8] B. Walliser, Justifications of game equilibrium notions, in: R. Arena, A. Festre (Eds.), Knowledge, Beliefs and Economics, Edward Elgar, 2006.

