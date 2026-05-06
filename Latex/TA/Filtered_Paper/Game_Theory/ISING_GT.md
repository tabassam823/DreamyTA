Noname manuscript No.
(will be inserted by the editor)

Quantum Nash equilibrium in the thermodynamic limit
Shubhayan Sarkar · Colin Benjamin

arXiv:1806.07343v3 [quant-ph] 7 Mar 2019

Received: date / Accepted: date

Abstract The quantum Nash equilibrium in the thermodynamic limit is studied for games like quantum Prisoner’s dilemma and quantum game of Chicken.
A phase transition is seen in both games as function of the entanglement in
the game. We observe that for maximal entanglement irrespective of the classical payoffs, majority of players choose quantum strategy over defect in the
thermodynamic limit.
Keywords Quantum games · Hawk-Dove game · Nash equilibrium
PACS 02.50.Le,01.80.+b,03.65.Ud,03.67.Ac

1 Introduction
Quantum game theory is an important extension of classical game theory to
the quantum regime. The classical games might be quantized by superposing initial states, entanglement between players or superposition of strategies,
for a brief account see [1]. The outcomes of a quantum game is well known
for two player case however, we want to investigate the scenario when the
number of players goes to infinity, i.e., the thermodynamic limit. In recent
times, there have been attempts to extend the two player classical games to
the thermodynamic limit by connecting it to the Ising model [2, 3, 4]. We do a
similar analysis and connect two player quantum games to the 1D Ising model
in the thermodynamic limit to figure out the strategy chosen by majority of
Shubhayan Sarkar
School of Physical Sciences, National Institute of Science Education & Research, HBNI,
Jatni-752050, India
Colin Benjamin
School of Physical Sciences, National Institute of Science Education & Research, HBNI,
Jatni-752050, India
E-mail: colin.nano@gmail.com

2

Shubhayan Sarkar, Colin Benjamin

the population and try to predict the Nash equilibrium when the choices are
entangled.
We approach the problem similar to as done in Refs. [3, 4], where players are
equivalent to sites and spins at each site represent the strategies of the players.
From a game theoretic perspective, Magnetisation is defined as the difference
between the average number of players opting for strategy s1 over s2 . We
first understand the connections between two player games and two spin Ising
Hamiltonian and then extend it to the thermodynamic limit. We then quantize
the Prisoner’s dilemma and game of Chicken using the Eisert’s scheme [5]. We
find the payoffs corresponding to the Quantum strategy (Quantum strategy
will be explicitly defined in section III). We then extend these games to the
thermodynamic limit by considering classical strategies (cooperation or defection) against the Quantum strategy. We see that for all the games considered,
Quantum and Cooperation are equiprobable strategies. However, we note an
intereseting feature that when the entanglement between the players becomes
maximum, then the majority of players would always choose the Quantum
strategy and won’t defect irrespective of the game’s payoffs. We also see how
quantum Nash equilibrium changes when the entanglement in the system is
varied.
This paper is organised as follows- In section IA, we review the 1-D Ising
model and the connection of two spin Ising Hamiltonian to the payoffs of a
general two player classical game as in Ref. [6]. We then extend it to the thermodynamic limit using the approach of Ref. [3, 4] for a classical game. Next,
we quantize the Prisoner’s dilemma game using Eisert’s scheme [5] and then
make the connection for the thermodynamic limit of quantum games, where
entanglement plays a non-trivial role. We then calculate the Nash equilibrium
in the thermodynamic limit for the quantum Prisoner’s dilemma. In section
III, we again quantize the game of Chicken using Eisert’s scheme and predict
the Nash equilibrium in the thermodynamic limit. We plot the probability of
choosing one strategy over other versus the entangling factor γ, and observe
the phase transitions as we vary the parameters. Interestingly we find that in
both games for maximal entanglement, the majority of individuals always opt
for the quantum strategy.

1.1 Classical game theory and 1D Ising model
In the 1D Ising model [7], the spins are put on a 1D line and are in either of
the two states +1 (↑) or −1 (↓). The interaction is restricted between nearest
neighbors only. The Hamiltonian of the 1D Ising system is given asH = −J

N
X
k=1

σk σk+1 − h

N
X

σk ,

(1)

k=1

where J denotes the spin-spin coupling, h is the external magnetic field and
the spins are denoted by σ’s. Using the above Hamiltonian Eq. (1), the Mag-

Quantum Nash equilibrium in the thermodynamic limit

3

netisation can be derived[7] assinh(βh)
m= q
.
sinh2 (βh) + e−4βJ

(2)

A two spin 1D Ising Hamiltonian and the payoff matrix for a two player game
can be mapped as was shown in Ref. [6, 3]. A general two player game has a
payoff matrix given by

s1 s2
(3)
U =  s1 a, a0 b, b0  ,
s2 c, c0 d, d0
where U (si , sj ) is the payoff function and a, b, c, d are the row player’s payoffs
while a0 , b0 , c0 , d0 are the column player’s payoffs. The strategies adopted by
the two players are denoted as s1 and s2 . To extend a two player game to a
N-player game, i.e., the thermodynamic limit we proceed by first defining the
two player Ising game matrix corresponding to a two player game, as in Eq. 3.
For a full derivation of Ising game matrix from a two spin Ising model, see
Refs. [3, 4, 6] It is then straightforward to calculate the magnetization of the N
player game, i.e., the difference between number of players opting for strategy
s1 over s2 using Eq. 2.
To map the two player game to the Ising game matrix we proceed as followsa factor λ is added to the s1 column and µ to the s2 column in Eq. 3. Thus,
we have

s1
s2
(4)
U =  s1 a + λ b + µ  .
s2 c + λ d + µ
As shown in Ref. [6, 3], the Nash equilibrium remains invariant under such a
change to the payoffs. To show this we used the fixed point analysis of game
theory. Since the Nash equilibrium corresponds to a fixed point, we show that
the fixed point corresponding to the game Eq. (3) and the transformed game
Eq. (4) are the same, see appendix of Ref. [3] for a detailed explanation of the
invariance of Nash equilibrium fixed point. The Ising game matrix [3, 4, 6] is
defined as

s2 = +1 s2 = −1
 s1 = +1 J + h −J + h  .
(5)
s1 = −1 −J − h J − h
where s1 , s2 denotes the spin at a particular site. The players in game theory are represented by the site and the strategies are represented by spins
in the Ising model (see Refs. [3, 6] for a detailed derivation). Choosing the
b+d
transformations as λ = − a+c
2 and µ = − 2 in Eq. (4), the elements of Ising
game matrix Eq. (5) can be mapped directly to the transformed payoff matrix
Eq. (3). Thus, we get the values of J, h which define the N-player game in
terms of the row player payoff’s of the two player game asJ=

a−c+d−b
a−c+b−d
, h=
.
4
4

4

Shubhayan Sarkar, Colin Benjamin

The Magnetization which gives the difference between the average number of
players opting for strategy s1 over s2 , from Eq. (2) can be written in terms of
the payoff matrix elements Eq. (3) asm= q

sinh(β a−c+b−d
)
4

.

(6)

sinh2 (β a−c+b−d
) + e−β(a−c+d−b)
4

Eq. (6) defines the connection between the payoffs from a classical two player
game with the magnetization of the N-player game, i.e., the thermodynamic
limit. To summarize the methodology, we first map the general two-player
game payoff matrix Eq. (3) to the 2-site Ising game matrix Eq. (5) by adding
payoff factors-λ and µ to the columns of Eq.(3). The addition of factors helps
to make a one-to-one correspondence between two site Ising game matrix and
payoffs of a two player game. Further, under such transformations the Nash
equilibrium remains invariant, see Appendix of Ref. [3]. Equating the Ising
game matrix to the transformed payoff matrix Eq. (4) we find the parameters
of 1-D Ising model (J and h) in terms of game payoffs. The 2-site Ising game
matrix is just a subset of the N-site Ising model, which for N → ∞ gives the
thermodynamic limit (from statistical physics). Thus, the magnetization of the
Ising model in the thermodynamic limit is now expressed in terms of the game
payoffs which is effectively the difference in the fraction of players choosing
one strategy over other. Thus, we can get the distribution of strategies in the
thermodynamic limit by mapping the two-player payoff matrix to the 2-site
Ising model. An account of infinite player games has also been attempted in
Ref. [8] to study Nash equilibrium using a different approach, but unlike this
work which focuses on quantum games, it is classical and further it does not
deal with the question on how cooperation arises in the infinite player case.
When temperature in Ising system increases, i.e., β = kB1T decreases, the
spins become more disordered. Similarly, decreasing β in game theory relates
to increasing the randomness in choices for individual players. Now to connect quantum game theory to the 1D Ising model so as to find the quantum
Nash equilibrium in the thermodynamic limit we consider first the Prisoner’s
dilemma. We first quantize the classical two player Prisoner’s dilemma incorporating entanglement and then model the mapping to a N-player quantum
prisoners dilemma by taking recourse to the Ising game matrix as shown in
Eqs. 5 and then similarly calculating the magnetization of the N-player quantum prisoner’s dilemma, see Eq. 6.

2 Prisoner’s dilemma
In the classical Prisoners dilemma game, police interrogate two suspects separately. Each suspect can either cooperate with the other and not admit the
crime (C) or defect against the other(D) implicating him in the crime. The
payoff matrix is constructed by taking the matrix elements from Eq. (3) as
a = r, d = p, b = s and c = t, with the condition t > r > p > s. The reward

Quantum Nash equilibrium in the thermodynamic limit

5

is given by r, temptation is t, s is sucker’s payoff and the punishment is given
by p. Thus, the classical payoff matrix is given by
C D
U =  C r, r s, t  .
D t, s p, p


(7)

Independent of the strategy opted by the fellow suspect, one can always stay
safe by defecting. Thus, the Nash equilibrium in classical Prisoner’s dilemma
is always defection.

2.1 Quantum game theory and 1D Ising model
The classical Prisoner’s dilemma game was quantized by Eisert, et. al., in
Ref. [5]. We explain their procedure by representing the convicts as qubits
and their strategies as the state of those qubits. The cooperation strategy is
represented as |0i while defection is represented as |1i. To choose a particular
strategy the operator O(θ, φ) is applied on the initial state where,
 iφ

e cos(θ/2) sin(θ/2)
O(θ, φ) =
.
− sin(θ/2) e−iφ cos(θ/2)

(8)

The operator L̂ entangles the choices
cos(γ/2)
0
0
i sin(γ/2)


0
cos(γ/2) −i sin(γ/2)
0
,
L̂ = 


0
−i sin(γ/2) cos(γ/2)
0
i sin(γ/2)
0
0
cos(γ/2)


with γ being a measure of the entanglement in the game. γ = 0 implies no
entanglement while γ = π/2 implies maximal entanglement. The initial state
|00i on being acted by L̂ gives- |ψk i = cos(γ/2)|00i + i sin(γ/2)|11i, the
subscript k indicates the site index and the final state after the action of
the disentangling operator L̂† and the unitary operators O’s representing the
strategies is|χk i = L̂† O(θ1 , φ1 ) ⊗ O(θ2 , φ2 )L̂|00i.

(9)

The classical prisoner’s dilemma payoffs are given by Eq. (7). The payoffs for
qubits A and B are then calculated using the template of classical prisoner’s
dilemma as$A = r|h00|χk i|2 + t|h10|χk i|2 + s|h01|χk i|2 + p|h11|χk i|2 ,
$B = r|h00|χk i|2 + s|h10|χk i|2 + t|h01|χk i|2 + p|h11|χk i|2 .
(10)

6

Shubhayan Sarkar, Colin Benjamin

Inclusion of quantum strategy via Q = iZ = O(0, π/2) leads to a new payoff
matrix:


C
D
Q
 C r, r
s, t α1, α1 
,
(11)
U =
 D t, s
p, p α2, α3 
Q α1, α1 α3, α2 r, r
where C = I and D = X and α1 = r cos2 (γ) + p sin2 (γ), α2 = s cos2 (γ) +
t sin2 (γ), and α3 = t cos2 (γ) + s sin2 (γ). When γ = π/2, |ψk > is a maximally
entangled state and the payoff matrix becomes taking- r = 3, t = 5, s = 0 and
p = 1:


C D Q
 C 3, 3 0, 5 1, 1 

(12)
U =
 D 5, 0 1, 1 0, 5  .
Q 1, 1 5, 0 3, 3
As we can clearly see that there are two optimal strategies, i.e., both players
can choose to cooperate or the quantum strategy. However, the new Nash
equilibrium is the quantum strategy. Thus, if the players choose the quantum
strategy then they will be at equilibrium with the maximum benefit shared
between both the players.
Now to extend the above two player game to the infinite player limit or
the thermodynamic limit, we proceed as follows. Similar to the extension of
classical games to the thermodynamic limit wherein the strategies or choices
of the players are represented by the spins in the Ising model, herein each site
plays the role of a spin in the classical Ising model, see Fig. 1. However, to
incorporate entanglement each site contains an entangled pair and a two player
quantum game is played at each site. A site interacts via classical coupling
factor J with its neighboring site. h the external magnetic field which tends
to align the spins in a particular direction in the classical Ising model, herein
plays the role of an external parameter which tends to make the sites behave
similar to each other in the N-site quantum game. A schematic diagram is
shown in Fig. 1. To map the payoffs from the two player quantum prisoner’s
dilemma at a single site to the Ising game matrix (5) we have each player in
a game to have access to either classical or quantum strategy, see Eq. (8). We
investigate the behavior of the N-site population for classical versus quantum
strategy played at each site. The magnetization for the N-site population is
then calculated as before from Eqs. (5,6). Thus we break the payoff matrix (12)
in to two separate 2 × 2 blocks: one for Quantum versus Cooperation and the
other block for Quantum versus Defect.

2.2 Quantum versus Cooperation
As discussed in section 2.1 we calculate the magnetization in a scenario when
Alice and Bob have access to only quantum (Q = iZ) and cooperation (C = I)

Quantum Nash equilibrium in the thermodynamic limit

7

Fig. 1: Representation of Ising model and its extension to quantum game
theory. The sites are represented by the site index k. The blue dashed line
represents classical coupling J between sites while in each site an entangled
state is present on whose two qubits the quantum game is played.

strategy. The payoff matrix for the row player then from Eq. (12) is

C
Q
U = C
r
r cos2 (γ) + p sin2 (γ)  .
2
2
Q r cos (γ) + p sin (γ)
r


(13)

We see that when γ = 0, the quantum strategy reduces to the cooperation
strategy in the quantum Prisoner’s dilemma. As we can see from the payoff matrix, there are two Nash equilibriums- both the players can choose to cooperate
or choose quantum. Transforming the matrix (13) using the method explained
r+r cos2 (γ)+p sin2 (γ)
in section 1.1, we get the transformations as- λ = − a+c
2 =−
2
2

2

r+r cos (γ)+p sin (γ)
and µ = − b+d
. The transformed payoff matrix is then2 =−
2



C

Q



2
2

sin2 (γ)
sin2 (γ) 
U =  C r−r cos (γ)−p
− r−r cos (γ)−p
.
2 2
22
r−r cos (γ)
r−r cos (γ)
Q
−
2
2
2

2

sin (γ)
When compared to the Ising game matrix Eq. (5), we get J+h = r−r cos (γ)−p
2
2

2

sin (γ)
and J −h = r−r cos (γ)−p
. Solving these simultaneous equations, we have
2
2

2

sin (γ)
J = r−r cos (γ)−p
and h = 0. The magnetization which is the difference
2
between the number of sites wherein quantum wins versus the number of sites

8

Shubhayan Sarkar, Colin Benjamin

wherein cooperation wins then is given bym= q

sinh(βh)

= 0.

(14)

sinh2 (βh) + e−4βJ

For quantum Prisoner’s dilemma in the thermodynamic limit there is no
unique Nash equilibrium wherein the sites can choose between cooperation
and quantum strategy. The sites are equally divided between where cooperation wins or quantum strategy wins.
2.3 Quantum versus Defect
Following on from the discussion in section 2.1, we calculate the magnetization
in a scenario when Alice and Bob have access to only quantum (Q = iZ) or
defect (D = X) strategies. The payoff matrix is given by

Q
D
(15)
U = Q
r
t sin2 (γ) + s cos2 (γ)  .
2
2
D t cos (γ) + s sin (γ)
p
In this case the Nash equilibrium will change with γ. For example, when γ = 0,
the Nash equilibrium is to defect. However, when γ = π/2 the Nash equilibrium
is the quantum strategy. Transforming the matrix using the method, explained
r+t cos2 (γ)+s sin2 (γ)
in section 1.1, we get the transformations as- λ = − a+c
2 =−
2
2

2

p+t sin (γ)+s cos (γ)
and µ = − b+d
. Thus, the transformed payoff matrix is2 =−
2


Q
D
2

sin2 (γ)
t sin2 (γ)+s cos2 (γ)−p 
U =  Q r−t cos (γ)−s
.
2
2
2
2
t sin2 (γ)+s cos2 (γ)−p
r−t cos (γ)−s sin (γ)
−
D−
2
2
2

2

sin (γ)
When compared to the Ising game matrix Eq. (5), we get J+h = r−t cos (γ)−s
2
2

2

cos (γ)
. Solving these simultaneous equations, we have
and J −h = p−t sin (γ)−s
2
r−p+(s−t) cos(2γ)
r+p−t−s
J =
and
h
=
and the magnetization for the N-site
4
4
quantum prisoner’s dilemma as in Fig. 1 is, using Eq. (6)-

sinh(βh)
m= q
sinh2 (βh) + e−4βJ
sinh(β r+(s−t) cos(2γ)−p
)
4
= q
.
−β(r+p−t−s)
sinh2 (β r+(s−t) cos(2γ)−p
)
+
e
4
The magnetization from Eq. (16) for γ = 0 becomessinh(β r+s−t−p
)
4
,
m= q
−β(r+p−t−s)
sinh2 (β r+s−t−p
)
+
e
4

(16)

Quantum Nash equilibrium in the thermodynamic limit

9

Fig. 2: Magnetization versus γ for quantum prisoner’s dilemma taking r = 3,
t = 5, p = 1 and s = 0 when players have access to quantum and defect
−1
strategy. A phase transition occurs at γ = cos 2 2/5 = .579 rad.

which is same as derived in Ref. [3] for classical Prisoner’s dilemma. We see
that a phase transition for quantum Prisoner’s dilemma occurs whensinh(β

r + (s − t) cos(2γ) − p
) = 0,
4

=⇒ r + (s − t) cos(2γ) − p = 0 =⇒ cos(2γ) =

r−p
.
t−s
(17)

For r = 3, t = 5, p = 1 and s = 0, the phase transition from Eq. (17) should
−1
occur at γ = cos (3−1)/(5−0)
= .579 rad as shown in Fig. 2. Also, it is quite
2
interesting to note that from the magnetization in Eq. (16) for γ = π/2, the
magnetization is always positive independent of payoffs of the payoff matrix
Eq. (7) as for Prisoner’s dilemma r > p. This implies that whatever is the value
of reward, temptation or punishment, at a majority of the sites the quantum
strategy wins. As we can see from Fig. 2, when β increases or the temperature
decreases, the number of players choosing quantum strategy increases in the
region where magnetization is positive. However, in the regime where the magnetization is negative, the number of defectors increases when β increases. The
population tends to become unbiased towards both the choices when β tends
to 0 even when there is a unique Nash equilibrium in the two player case. Comparing with the classical Prisoner’s dilemma [3] in the thermodynamic limit,
we see that there is phase transition in the quantum case. This is interesting
as in the thermodynamic limit for the classical Prisoner’s dilemma majority
were always defecting. However, we see here that for maximum entanglement,
the defectors are always in a minority.

10

Shubhayan Sarkar, Colin Benjamin

3 Game of chicken
The game of “Chicken” refers to a situation where two players drive their
bikes toward each other, each can either swerve or go straight[9]. If the player
swerves but the opponent doesn’t, he can be called a coward or ”Chicken”.
The payoff matrix for the game of chicken with a = −s, b = r, c = −r and
d = 0 from Eq. (3) is given as

straight swerve
(18)
U =  straight −s, −s r, −r  ,
swerve −r, r
0, 0
where “r” denotes reputation while “s” denotes the injury cost with the condition s > r > 0. If one player drives straight and other swerves, the one who
swerves looses reputation, while other gains in reputation. However, a crash
occurs injuring both if both drive straight at each other. There are two pure
strategy Nash equilibriums (straight, swerve) and (swerve, straight) giving
payoff r to one player and -r to other. There is a mixed strategy Nash equilibrium also which is given by (σ, σ), where [σ = p.straight+(1 − p).swerve] with
p = rs (p being the probability to choose straight).
Taking the classical payoff matrix as in Eq. (18), we calculate the quantum
payoff’s via the scheme as done in section 2.1. If both the players move straight,
then it brings a higher loss to both the players. Thus straight strategy can
be taken equivalent to defection and swerve as cooperation. We thus have
the classical strategies represented via the unitary matrices as- swerve= I,
straight= X while the quantum strategy is Q = iZ. The full payoff matrix
including both classical and the quantum strategies is therefore

swerve straight Q
 swerve 0, 0
−r, r α1, α1 

(19)
U =
 straight r, −r −s, −s α2, α3  ,
Q
α1, α1 α3, α2 0, 0
where α1 = −s sin2 (γ), α2 = r cos(2γ) and α3 = −r cos(2γ). Now, we try to
figure out what happens in the infinite player limit or the thermodynamic limit
of quantum game of Chicken. To do this we break the quantum payoff matrix
into two 2 × 2 blocks. This is what we do below, we first consider Quantum
vs. Swerve and then Quantum vs. Straight.
3.1 Quantum versus Swerve
As discussed in section 2.1 we calculate the magnetization in a scenario when
the qubits at a particular site are acted on by only quantum (Q = iZ) or
swerve (I) strategies. The payoff matrix is then given from Eq. (19) for only
row player as

swerve
Q
U =  swerve
(20)
0
−s sin2 (γ)  .
2
Q −s sin (γ)
0

Quantum Nash equilibrium in the thermodynamic limit

11

As we can see from the payoff matrix, there are two Nash equilibriums- both
choosing swerve or both choosing quantum. To go to the thermodynamic limit
of the two player quantum game of chicken we follow the same procedure as
was done for two player quantum prisoner’s dilemma. First transforming the
s sin2 (γ)
s sin2 (γ)
and µ = − b+d
,
matrix as given above using λ = − a+c
2 =
2
2 =
2
to map it to the Ising game matrix (5), we have

swerve
Q
2
2


U =  swerve s sin2 (γ) − s sin2 (γ)  .
2
2
Q − s sin2 (γ) s sin2 (γ)
2

When compared to the Ising game matrix Eq. (5), we get J + h = s sin2 (γ) and
2

2

(γ)
J − h = s sin2 (γ) . Solving these simultaneous equations, we have J = −s sin
2
and h = 0. From Ising model, the magnetization is-

m= q

sinh(βh)

= 0, as h = 0.

(21)

sinh2 (βh) + e−4βJ

Thus, the net magnetization vanishes in other words it is independent of
r, s, t, p, i.e., the number of players choosing straight is exactly same as the
number of players playing quantum in the thermodynamic limit. Finally, we
see that when γ = 0, the quantum strategy Q reduces to the swerve or cooperation strategy in the classical game of chicken.
3.2 Quantum versus Straight
As discussed in section 2.1 we calculate the magnetization in a scenario when
the qubits at a particular site are acted only by quantum (Q = iZ) or straight
(= X) strategies. The payoff matrix is given by

Q
straight
U =
(22)
Q
0
−r cos(2γ)  .
straight r cos(2γ)
−s
The Nash equilibrium in this case changes with γ. For γ < π/4, there are
three Nash equilibria- (Quantum, Straight), (Straight, Quantum) and (σ, σ),
where σ = p × quantum + (1 − p) × straight, with p = s−r cos(2γ)
. However, for
s
γ > π/4, there is only one Nash equilibrium- both players choosing Quantum.
s+r cos(2γ)
Transforming the matrix (22) as given above using λ = − a+c
2 =
2
r cos(2γ)
and µ = − b+d
=
−
,
to
map
it
into
the
Ising
game
matrix
and
thus
2
2
calculate the Nash equilibrium in the thermodynamic limit, we have for the
transformed payoff matrix

Q
straight
s−r cos(2γ) 
U =
.
Q
− r cos(2γ)
2
2
r cos(2γ)
s−r cos(2γ)
straight
−
2
2

12

Shubhayan Sarkar, Colin Benjamin

Magnetisation
1.0
0.8
0.6

β=1

0.4

β=1.5
β=2

0.2

0.5

1.0

1.5

γ

-0.2
Fig. 3: Magnetization versus γ for quantum game of Chicken with r = s = 4
for different β 0 s when players have access to quantum and straight strategy.
For maximum entanglement i.e., γ = π/2, the magnetization is always positive
irrespective of the values for s, r and β.

When compared to the Ising game matrix Eq. (5), we get J + h = − r cos(2γ)
2
and J −h = r cos(2γ)−s
.
Solving
these
simultaneous
equations,
we
have
J
=
− 4s
2
s−2r cos(2γ)
and h =
. Thus, the magnetization in the thermodynamic limit is4
m= q

sinh(β s−2r cos(2γ)
)
4
=q
.
βs
sinh2 (βh) + e−4βJ
sinh2 (β s−2r cos(2γ)
)
+
e
4
sinh(βh)

(23)

The magnetization from Eq. (23) for γ = 0 is thenm= q

sinh(β s−2r
4 )

,

βs
sinh2 (β s−2r
4 )+e

which is the same as derived in Ref. [3]. The phase transition for the quantum
game of chicken occurs whensinh(β

s − 2r cos(2γ)
) = 0 =⇒ s − 2r cos(2γ) = 0
4
s
=⇒ cos(2γ) = .
2r

(24)

For r = s = 4, the phase transition from Eq. (24) should occur at γ =
cos−1 (1)/(2)
= π/6 as shown in Fig. 3. It is to be noted from the magnetization,
2
see Eq. (24) for γ > π/4, the magnetization is always positive independent of
payoffs of the payoff matrix Eq. (18) as for game of chicken s > r > 0. This

Quantum Nash equilibrium in the thermodynamic limit

13

implies that independent of the reputation or injury cost, the majority of the
population would always choose the quantum strategy. When fluctuation in
choices become maximum or β = 0, the players become unbiased towards
quantum or straight even when a unique Nash equilibrium exists in the two
player game.
4 Conclusions
The aim in this work was to figure out the quantum Nash equilibrium in the
thermodynamic limit. In the thermodynamic limit we see that, the quantum
and cooperation strategy are equally probable. However, when the players
have access to defection and quantum strategy, a phase transition occurs when
the entanglement between players increases in favor of the quantum strategy.
Further, when the entanglement is maximum then irrespective of payoffs, the
majority always choose the quantum strategy and don’t defect. Even in game of
“Chicken”, the majority of players would always choose the quantum strategy
over defection when the entanglement is maximum. Thus, we can conclude that
when the players have access to quantum strategy, defection in a population
reduces. Further to point out the generality of our approach, instead of the
quantization scheme of Eisert, et. al, see Ref. [6], we could have chosen any
quantization procedure of the two-player game and our approach could be
used to extend the quantized game to the thermodynamic limit. An account
of different quantization schemes of classical games can be found in Ref. [10].
5 Acknowledgments
This work was supported by the grant “Non-local correlations in nanoscale systems: Role of decoherence, interactions, disorder and pairing symmetry” from
SCIENCE & ENGINEERING RESEARCH BOARD, New Delhi, Government
of India, Grant No. EMR/20l5/001836, Principal Investigator: Dr. Colin Benjamin, National Institute of Science Education and Research, Bhubaneswar,
India. CB thanks Condensed matter and Statistical Physics section of the Abdus Salam ICTP, Trieste, Italy for funding a research visit during which a part
of this work was completed.
6 Author’s contributions
C.B. conceived the proposal, S.S. did the calculations on the advice of C.B.,
C.B. and S.S. analyzed the results and wrote the paper. Both authors reviewed
the manuscript.
7 Conflicts of Interest
The authors have no potential financial or non-financial conflicts of interest.

14

Shubhayan Sarkar, Colin Benjamin

8 Data Availability Statement
All data generated or analysed during this study are included in this manuscript.

References
1. J. O. Grabbe, An Introduction to Quantum Game Theory, arXiv:quant-ph/0506219
2. C. Adami and A. Hintze, Thermodynamics of Evolutionary Games,
arXiv:1706.03058v1 (2017).
3. S. Sarkar and C. Benjamin, Emergence of Cooperation in the thermodynamic limit,
arXiv:1803.10083 (2018).
4. S. Sarkar and C. Benjamin, Triggers for cooperative behavior in the thermodynamic
limit: a case study in Public goods game, arXiv:1804.06465 (2018).
5. J. Eisert, M. Wilkens, and M. Lewenstein, Quantum Games and Quantum Strategies,
Phys. Rev. Lett. 83, 3077 (1999).
6. S. Galam and B. Walliser, Ising model versus normal form game, Physica A: Statistical
Mechanics and its Applications, 389, 3 (2010).
7. Web article ”http://www.nyu.edu/classes/tuckerman/
stat.mech/lectures/lecture 26/node2.html”
8. Hannu Salonen, On the existence of Nash equilibria in large games, Int. J. Game
Theory (2010) 39: 351.
9. Game Theory in Action: An Introduction to Classical and Evolutionary Models,
Stephen Schecter and Herbert Gintis, Princeton Univ. Press (2016).
10. Faisal Shah Khan, et. al., Quantum games: a review of the history, current state, and
interpretation, Quantum Inf Process (2018) 17: 309.

