GAMES AND ECONOMIC BEHAVIOR 14, 124–143 (1996)
ARTICLE NO. 0044

Potential Games
Dov Monderer∗
Faculty of Industrial Engineering and Management, The Technion, Haifa 32000, Israel

and
Lloyd S. Shapley
Department of Economics and Department of Mathematics, University of California,
Los Angeles, California 90024
Received January 19, 1994

We define and discuss several notions of potential functions for games in strategic form.
We characterize games that have a potential function, and we present a variety of applications. Journal of Economic Literature Classification Numbers: C72, C73. © 1996 Academic
Press, Inc.

1. INTRODUCTION
Consider a symmetric oligopoly Cournot competition with linear cost functions ci (qi ) = cqi , 1 ≤ i ≤ n. The inverse demand function, F(Q), Q > 0, is a
positive function (no monotonicity, continuity, or differentiability assumptions
n
as
on F are needed). The profit function of Firm i is defined on R++
Pn

5i (q1 , q2 , . . . , qn ) = F(Q)qi − cqi ,

where Q = j=1 q j .
n
−→ R:
Define a function P: R++
P(q1 , q2 , . . . , qn ) = q1 q2 · · · qn (F(Q) − c).
n−1
For every Firm i, and for every q−i ∈ R++
,

5i (qi , q−i ) − 5i (xi , q−i ) > 0,

iff

P(qi , q−i ) − P(xi , q−i ) > 0,
∀qi , xi ∈ R++ .
(1.1)

∗ First version: December 1988. Financial support from the Fund for the Promotion of Research at
the Technion is gratefully acknowledged by the first author. E-mail: dov@techunix.technion.ac.il.

124
0899-8256/96 $18.00
Copyright © 1996 by Academic Press, Inc.
All rights of reproduction in any form reserved.

125

POTENTIAL GAMES

A function P satisfying (1.1) is called an ordinal potential, and a game that possesses an ordinal potential is called an ordinal potential game. Clearly, the purestrategy equilibrium set of the Cournot game coincides with the pure-strategy
equilibrium set of the game in which every firm’s profit is given by P. A condition
stronger than (1.1) is required if we are interested in mixed strategies.
Consider a quasi-Cournot competition1 with a linear inverse demand function
F(Q) = a − bQ, a, b > 0, and arbitrary differentiable cost functions ci (qi ),
1 ≤ i ≤ n. Define a function P ∗ ((q1 , q2 , . . . , qn )) as
P ∗ ((q1 , q2 , . . . , qn )) = a

n
X

qj − b

n
X

j=1

−

n
X

q j2 − b

j=1

X

qi q j

1≤i< j≤n

c j (q j ).

(1.2)

j=1

It can be verified that For every Firm i, and for every q−i ∈ R+n−1 ,
5i (qi , q−i ) − 5i (xi , q−i ) = P ∗ (qi , q−i ) − P ∗ (xi , q−i ),

∀qi , xi ∈ R+ . (1.3)

A function P ∗ satisfying (1.3) will be called a potential function.2,3 The equalities (1.3) imply that the mixed-strategy equilibrium set of the quasi-Cournot
game coincides with the mixed-strategy equilibrium set of the game obtained
by replacing every payoff function by P ∗ . In particular, firms that are jointly
trying to maximize the potential function P ∗ (or the ordinal potential P) end up
in an equilibrium.4 We will prove that there exists at most one potential function
(up to an additive constant). This raises the natural question about the economic
content (or interpretation) of P ∗ : What do the firms try to jointly maximize?
1 Negative prices are possible in this game, though the prices in any nondegenerate equilibrium will
be positive.
2 In physics, P ∗ is a potential function for (5 , 5 , . . . , 5 ) if
1
2
n

∂5i
∂ P∗
=
∂qi
∂qi

for every 1 ≤ i ≤ n.

If the profits functions are continuously differentiable then this condition is equivalent to (1.3).
3 Slade (1993) proved the existence of a function P ∗ satisfying (1.3) for the quasi-Cournot game.
She called this function a fictitious objective function.
4 Every q ∗ that maximizes P ∗ is a pure-strategy equilibrium, but there may be pure-strategy equilibrium profiles that are just “local” maximum points, and there may be mixed-strategy equilibrium
profiles as well. Therefore, the argmax set of the potential can be used as a refinement tool for potential
games (this issue is discussed in Section 5). Neyman (1991) showed that if the potential function is
concave and continuously differentiable, then every mixed-strategy equilibrium profile is pure and
must maximize the potential function. Neyman’s result is related by Shin and Williamson (1994) to
the concept of “simple equilibrium outcome” in Bayesian games.

126

MONDERER AND SHAPLEY

We do not have an answer to this question. However, it is clear that the mere
existence of a potential function helps us (and the players) to better analyze the
game.5
In this paper we will prove various properties of potential games, and we will
provide simple methods for detecting them and for computing their potential
functions.
To our knowledge, the first to use potential functions for games in strategic
form was Rosenthal (1973). Rosenthal defined the class of congestion games
and proved, by explicitly constructing a potential function, that every game in
this class possesses a pure-strategy equilibrium. The class of congestion games
is, on the one hand, narrow, but on the other hand, very important for economics.
Any game where a collection of homogeneous agents have to choose from a
finite set of alternatives, and where the payoff of a player depends on the number
of players choosing each alternative, is a congestion game. We will show that
the class of congestion games coincides (up to an isomorphism) with the class
of finite potential games.
Recently, much attention has been devoted to several notions of “myopic”
learning processes. We show that for generic finite games, the existence of an
ordinal potential is equivalent to the convergence to equilibrium of the learning
process defined by the one-sided better reply dynamic. The new learning literature raised a new interest in the Fictitious Play process in games in strategic
form defined by Brown (1951). It was studied for zero-sum games by Robinson
(1951) and for non-zero-sum games by Miyasawa (1961), Shapley (1964), Deschamps (1973), and lately by Krishna (1991), Milgrom and Roberts (1991), Sela
(1992), Fudenberg and Kreps (1993), Jordan (1993), Hofbauer (1994), Krishna
and Sjöström (1994), Fudenberg and Levine (1994), Monderer et al. (1994),
and others. In Monderer and Shapley (1996) we prove that the Fictitious Play
process converges to the equilibrium set in a class of games that contains the
finite (weighted) potential games. Milchtaich (1996) analyzed classes of games
related to congestion games. His work, as well as that of Blume (1993), indicates
that ordinal potential games are naturally related to the evolutionary learning as
well (see e.g., Crawford, 1991; Kandori and Rob, 1992; Young, 1993; Roth and
Erev, 1995; and the references listed therein).
As the potential function is uniquely defined up to an additive constant, the
argmax set of the potential function does not depend on a particular potential
function. Thus, for potential games this argmax set refines the equilibrium set,
at least technically. We show that this refinement concept accurately predicts the
experimental results obtained by Van Huyck et al. (1990). We do not attempt to
provide any explanation to this prediction power obtained (perhaps as a coinci-

5 A similar problem is discussed by Bergstrom and Varian (1985).

POTENTIAL GAMES

127

dence) in this case.6 A possible way of explaining this can be found in Blume
(1993). Blume discusses various stochastic strategy revision processes for players who have direct interaction only with small part of the population. He proves
for the log-linear strategy revision process that the strategies of the players in a
symmetric potential game converge to the argmax set of the potential.7
Hart and Mas-Colell (1989) have applied potential theory to cooperative
games. Except for the fact that we are all using potential theory our works are
not connected. Nevertheless, we will show in the last section that combining our
work with Hart and Mas-Colell’s yields a surprising application to value theory.8
The paper is organized as follows: In Section 2 we give the basic definitions
and provide several useful characterizations of finite potential and finite ordinal
potential games. An equivalence theorem between potential games and congestion games is given in Section 3. In Section 4 we discuss and characterize infinite
potential games. Section 5 is devoted to a discussion of the experimental results
of Van Huyck et al. In Section 6 we show an application of our theory to the
strategic approach to cooperative games.
2. POTENTIAL GAMES
Let 0(u 1 , u 2 , . . . , u n ) be a game in strategic form with a finite number of
players. The set of players is N = {1, 2, . . . , n}, the set of strategies of Player i
is Y i , and the payoff function of Player i is u i : Y → R, where Y = Y 1 × Y 2 ×
· · · × Y n is the set of strategy profiles, and R denotes the set of real numbers.
When no confusion may arise we denote 0(u 1 , u 2 , . . . , u n ) by 0. For S ⊆ N ,
−S denotes the complementary set of S, and Y S denotes the Cartesian product
×i∈S Y i . For singleton sets {i}, Y −{i} is denoted by Y −i . A function P: Y → R
is an ordinal potential for 0, if for every i ∈ N and for every y −i ∈ Y −i
u i (y −i , x) − u i (y −i , z) > 0 iff P(y −i , x) − P(y −i , z) > 0
for every x, z ∈ Y i .

(2.1)

0 is called an ordinal potential game if it admits an ordinal potential.
Let w = (wi )i∈N be a vector of positive numbers which will be called weights.
A function P: Y → R is a w-potential for 0 if for every i ∈ N and for every
y −i ∈ Y −i
¡
¢
u i (y −i , x) − u i (y −i , z) = wi P(y −i , x) − P(y −i , z)
for every x, z ∈ Y i .
(2.2)
0 is called a w-potential game if it admits a w-potential.
6 Crawford (1991) gave an evolutionary interpretation of these experiments’ results.
7 This argmax set is assumed to be a singleton.
8 Another application to cooperative games is discussed by Qin (1992).

128

MONDERER AND SHAPLEY

When we are not interested in particular weights w, we simply say that P is
a weighted potential and that 0 is a weighted potential game.9
A function P: Y → R is an exact potential (or, in short, a potential) for 0 if it
is a w-potential for 0 with wi = 1 for every i ∈ N . 0 is called an exact potential
game (or, in short, a potential game) if it admits a potential. For example, the
matrix P is a potential for the Prisoner’s Dilemma game G described below:
µ
¶
µ
¶
(1, 1) (9, 0)
4 3
G=
,
P=
.
(0, 9) (6, 6)
3 0
The next lemma characterizes the equilibrium set of ordinal potential games. Its
obvious proof will be omitted.
LEMMA 2.1. Let P be an ordinal potential function for 0(u 1 , u 2 , . . . , u n ).
Then the equilibrium set of 0(u 1 , u 2 , . . . , u n ) coincides with the equilibrium set
of 0(P, P, . . . , P). That is, y ∈ Y is an equilibrium point for 0 if and only if
for every i ∈ N

P(y) ≥ P(y −i , x)

for every x ∈ Y i .

Consequently, If P admits a maximal value10 in Y , then 0 possesses a (purestrategy) equilibrium.
COROLLARY 2.2. Every finite ordinal potential game possesses a pure-strategy
equilibrium.

A path in Y is a sequence γ = (y0 , y1 , . . .) such that for every k ≥ 1 there
−i
i
, x) for some x 6= yk−1
exists a unique player, say Player i, such that yk = (yk−1
i
in Y . y0 is called the initial point of γ , and if γ is finite, then its last element
is called the terminal point of γ . γ = (y0 , y1 , . . .) is an improvement path with
respect to 0 if for all k ≥ 1 u i (yk ) > u i (yk−1 ), where i is the unique deviator
at step k. Hence, an improvement path is a path generated by myopic players. 0
has the finite improvement property (FIP) if every improvement path is finite.
LEMMA 2.3. Every finite ordinal potential game has the FIP.

Proof. For every improvement path γ = (y0 , y1 , y2 , . . .) we have by (2.1)
P(y0 ) < P(y1 ) < P(y2 ) < · · · .
As Y is a finite set, the sequence γ must be finite.
9 Using Blume’s (1993) terminology we can give an equivalent definition: 0 is a weighted potential

game if and only if there exists a payoff function which is strongly best-response equivalent to each
of the players’ payoff functions. Sela (1992) proved that if the two-person game (A, B) does not
have weakly dominated strategies, then it has a weighted potential if and only if it is better-response
equivalent in mixed strategies (see Monderer and Shapley (1996) for the precise definition) to a game
of the form (P, P). This result can be easily generalized to n-person games.
10 See footnote 4.

129

POTENTIAL GAMES

It is obvious that for finite games with the FIP, and in particular for finite
ordinal potential games, every maximal improvement path must terminate in an
equilibrium point. That is, the myopic learning process based on the one-sided
better reply dynamic converges to the equilibrium set. However we have obtained
a stronger learning result11 :
THEOREM 2.4 (Monderer and Shapley, 1996). Every finite weighted potential game has the Fictitious Play property.

It is interesting to note that having the FIP is not equivalent to having an
ordinal potential. A counterexample is the game G 1 described below. The rows
in G 1 are labeled by a and b, and the columns are labeled by c and d.
µ
¶
(1, 0) (2, 0)
.
G1 =
(2, 0) (0, 1)
The game G 1 has the FIP, but any ordinal potential P for G 1 must satisfy the
following impossible sequence of relations:
P(a, c) < P(b, c) < P(b, d) < P(a, d) = P(a, c).
A function P: Y → R is a generalized ordinal potential for 0 if for every i ∈ N
and for every y −i ∈ Y −i , and for every x, z ∈ Y i ,
u i (y −i , x) − u i (y −i , z) > 0

implies that

P(y −i , x) − P(y −i , z) > 0.
(2.3)

LEMMA 2.5. Let 0 be a finite game. Then, 0 has the FIP if and only if 0 has
a generalized ordinal potential.

Proof. Let 0 be a game with the FIP. Define a binary relation “>” on Y as
follows: x > y iff x 6= y and there exists a finite improvement path γ with an
initial point y and a terminal point x. The finite improvement property implies
that “>” is a transitive relation. Let Z ⊆ Y . We say that Z is represented if
there exists Q: Z → R such that for every x, y ∈ Z , x > y implies that
Q(x) > Q(y). Let Z be a maximal represented subset of Y . We proceed to
prove that Z = Y . Suppose x 6∈ Z . If x > z for every z ∈ Z , we extend
Q to Z ∪ {x} by defining Q(x) = 1 + maxz∈Z Q(z), thus contradicting the
maximality of Z . If z > x for every z ∈ Z , we extend Q to Z ∪ {x} by defining
Q(x) = minz∈Z Q(z) − 1, contradicting again the maximality of Z . Otherwise
we extend Q and contradict the maximality of Z by defining Q(x) = (a + b)/2,
11 Several notions of acyclicity are discussed in the recent learning literature. Most of them (unlike
the FIP) are related to the best-response dynamic. See, e.g., Young (1993). Other results relating the
fictitious play property with various types of improvement paths can be found in Monderer and Sela
(1992).

130

MONDERER AND SHAPLEY

where a = max{Q(z) : z ∈ Z ,
Hence Y is represented.12

x > z}, and b = min{Q(z) : z ∈ Z ,

z > x}.

COROLLARY 2.6. Let 0 be a finite game with the FIP. Suppose in addition
that for every i ∈ N and for every y −i ∈ Y −i

u i (y −i , x) 6= u i (y −i , z)

for every x 6= z ∈ Y i .

Then 0 has an ordinal potential.
Proof. Observe that the condition on 0 implies that every generalized ordinal
potential for 0 is an ordinal potential for 0. Hence, the proof follows from
Lemma 2.5.
Ordinal potential games have many ordinal potentials. For exact potential
games we have:
LEMMA 2.7. Let P1 and P2 be potentials for the game 0. Then there exists a
constant c such that

P1 (y) − P2 (y) = c

for every y ∈ Y .

Proof. Fix z ∈ Y . For all y ∈ Y define
H (y) =

n
X
£

¤
u i (ai−1 ) − u i (ai ) ,

i=1
−i
, z i ).
where a0 = y and for every 1 ≤ i ≤ n, ai = (ai−1
If P stands for either P1 or P2 , then by (2.1), H (y) = P(y) − P(z) for every
y ∈ Y . Therefore

P1 (y) − P2 (y) = c

for every y ∈ Y .

The next results characterize exact potential games in a way that resembles
the standard approach to potential functions in physics.
For a finite path γ = (y0 , y1 , . . . , y N ) and for a vector v = (v 1 , v 2 , . . . , v n )
of functions v i : Y → R, we define
I (γ , v) =

n
X
£

¤
v ik (yk ) − v ik (yk−1 ,

k=1
ik
).
where i k is the unique deviator at step k (i.e., ykik 6= yk−1
12 A constructive and more elegant proof of this result is given in Milchtaich (1996); he showed that
the function P that assigns to each y ∈ Y the number of strategy profiles that are connected to y by an
improvement path that terminates in y is a generalized ordinal potential for 0.

131

POTENTIAL GAMES

The path γ = (y0 , y1 , . . . , y N ) is closed if y0 = y N . It is a simple closed path
if in addition yl 6= yk for every 0 ≤ l 6= k ≤ N −1. The length of a simple closed
path is defined to be the number of distinct vertices in it. That is, the length of
γ = (y0 , y1 , . . . , y N ) is N .
THEOREM 2.8. Let 0 be a game in strategic form, as described at the beginning of this section. Then the following claims are equivalent:

(1) 0 is a potential game.
(2) I (γ , u) = 0 for every finite closed paths γ .
(3) I (γ , u) = 0 for every finite simple closed paths γ .
(4) I (γ , u) = 0 for every finite simple closed paths γ of length 4.
The proof of Theorem 2.8 is given in Appendix A.
A typical simple closed path, γ , of length 4 is described below. In this path,
i and j are the active players, a ∈ Y −{i, j} is a fixed strategy profile of the other
players, xi , yi ∈ Y i , and x j , yj ∈ Y j ,
A ←−−−− D

x
,
γ =
y

B −−−−→ C
where A = (xi , x j , a), B = (yi , x j , a), C = (yi , yj , a), and D = (xi , yj , a).
COROLLARY 2.9. 0 is a potential game if and only if for every i, j ∈ N , for
every a ∈ Y −{i, j} , and for every xi , yi ∈ Y i and x j , yj ∈ Y j ,

u i (B) − u i (A) + u j (C) − u j (B) + u i (D) − u i (C) + u j (A) − u j (D) = 0,
where the points A, B, C, and D are described above.
We end this section with an important remark concerning the mixed extension
of finite games.
LEMMA 2.10. Let 0 be a finite game. Then 0 is a w-potential game if and
only if the mixed extension of 0 is a w-potential game.

Proof. For i ∈ N let 1i be the set of mixed strategies of Player i and let U i
be the payoff function of player i in the mixed extension of 0. That is,
U i ( f ) = U i ( f 1, f 2, . . . , f n )
X
=
u i (y 1 , y 2 , . . . , y n ) f 1 (y 1 ) f 2 (y 2 ) . . . f n (y n ),

∀ f ∈ 1,

y∈Y

where 1 = ×i∈N 1i . Obviously, if P̄: 1 → R is a w-potential function for the
mixed extension of 0, then its restriction to Y yields a w-potential for 0. As for

132

MONDERER AND SHAPLEY

the converse, suppose P is a w-potential for 0, then it can be easily verified that
P̄ is a potential for the mixed extension of 0, where
X
P̄( f 1 , f 2 , . . . , f n ) =
P(y 1 , y 2 , . . . , y n ) f 1 (y 1 ) f 2 (y 2 ) . . . f n (y n ). (2.4)
y∈Y

An example to an ordinal potential game whose mixed extension is not an
ordinal potential game is given in Sela (1992).

3. CONGESTION GAMES
Congestion games were defined by Rosenthal (1973). They are derived from
congestion models that have been extensively discussed in the literature (see
e.g., Garcia and Zangwill, 1981). Consider an illustrative example:
c1 (1),c1 (2)

A −−−−−→ B



c (1),c (2)
c3 (1),c3 (2)y
y2 2
D −−−−−→ C
c4 (1),c4 (2)

In the congestion model described above, Driver a has to go from point A
to point C and Driver b has to go from point B to point D. AB is called road
segment 1, BC is called road segment 2, . . . etc. c j (1) denotes the payoff (e.g.,
the negative of the cost) for a single user of road segment j. c j (2) denotes the
payoff for each user of road segment j if both drivers use road segment j. The
drivers are therefore engaged in a game (the associated congestion game, C G)
whose strategic form is given below (The rows are labeled by {1, 2} and {3, 4},
and the columns are labeled by {1, 3} and {2, 4}:
¶
µ
(c1 (2) + c2 (1), c1 (2) + c3 (1)) (c2 (2) + c1 (1), c2 (2) + c4 (1))
.
CG =
(c3 (2) + c4 (1), c3 (2) + c1 (1)) (c4 (2) + c3 (1), c4 (2) + c2 (1))
By Corollary 2.9 the congestion game C G admits a potential. In particular
(and with no restrictions on the payoff c j (i)) it has a (pure-strategy) equilibrium.
For completeness we attach below a potential P for the congestion game. The
potential is computed by formula (3.2):
¶
µ
c1 (1) + c1 (2) + c2 (1) + c3 (1) c2 (1) + c2 (2) + c1 (1) + c4 (1)
.
P=
c3 (1) + c3 (2) + c4 (1) + c1 (1) c4 (1) + c4 (2) + c3 (1) + c2 (1)
A congestion model C(N , M, (6 i )i∈N , (c j ) j∈M ) is defined as follows. N denotes the set of players {1, 2, . . . , n} (e.g., drivers). M denotes the set of facilities

POTENTIAL GAMES

133

{1, 2, . . . , m} (e.g, road segments). For i ∈ N let 6 i be the set of strategies of
player i, where each Ai ∈ 6 i is a nonempty subset of facilities (e.g., a route).
For j ∈ M let c j ∈ R {1,2,...,n} denote the vector of payoffs, where c j (k) denotes
the payoff (e.g., the cost) to each user of facility j, if there are exactly k users.
The congestion game associated with the congestion model is the game in
strategic form with the set of players N , with the sets of strategies (6 i )i∈N , and
with payoff functions (v i )i∈N defined as follows:
Set 6 = ×i∈N 6 i . For all A ∈ 6 and for every j ∈ M let σ j (A) be the number
of users of facility j. That is,
σ j (A) = #{i ∈ N : j ∈ Ai },
where A = (A1 , A2 , . . . , An ).
Define v i : 6 → R by
v i (A) =

X

c j (σ j (A)).

(3.1)

j∈Ai

The following theorem can be deduced from Rosenthal (1973).
THEOREM 3.1. Every congestion game is a potential game.

Proof. Let 0 be the congestion game defined by the parameters N , M,
(6 i )i∈N , (c j ) j∈M .
For each A ∈ 6 define
!
Ãσ (A)
j
X
X
c j (l) .
(3.2)
P(A) =
n
j∈∪i=1
Ai

l=1

The proof that P is a potential for 0 can be deduced from Rosenthal (1973) or
directly using Corollary 2.9.
Let 01 and 02 be games in strategic form with the same set of players N . For
k = 1, 2 let (Yki )i∈N be the strategy sets in 0k , and let (u ik )i∈N be the payoff
functions in 0k . We say that 01 and 02 are isomorphic if there exist bijections
g i : Y1i → Y2i , i ∈ N , such that for every i ∈ N
u i1 (y 1 , y 2 , . . . , y n ) = u i2 (g 1 (y 1 ), g 2 (y 2 ), . . . , g n (y n ))
for every (y 1 , y 2 , . . . , y n ) ∈ Y1 ,
where Y1 = ×i∈N Y1i .
THEOREM 3.2. Every finite potential game is isomorphic to a congestion
game.

The proof, as well as several relevant discussions, is given in Appendix B.

134

MONDERER AND SHAPLEY

4. INFINITE POTENTIAL GAMES
Let 0 be a game in strategic form as described in Section 2. 0 is called a
bounded game if the payoff functions (u i )i∈N are bounded.
LEMMA 4.1. Every bounded potential game possesses an ε-equilibrium point
for every ε > 0.

Proof. Note that by (2.2) every potential P for 0 must be bounded. Let
ε > 0. There exists z ∈ Y satisfying
P(z) > sup P(y) − ε.
y∈Y

Obviously z is an ε-equilibrium point.
Recall the concept of a path from Section 2. Let ε > 0. A path γ = (y0 , y1 , . . .)
is an ε-improvement path with respect to 0 if for all k ≥ 1 u i (yk ) > u i (yk−1 )+ε,
where i is the unique deviator at step k. The game 0 has the approximate finite
improvement property (AFIP) if for every ε > 0 every ε-improvement path is
finite. The proof of the next lemma is obvious and will be omitted.
LEMMA 4.2. Every bounded potential game has the AFIP.

Note that for games with the AFIP, and in particular for bounded potential
games, every maximal ε-improvement path terminates in an ε-equilibrium point.
A game 0 is called a continuous game if the strategy sets are topological spaces
and the payoff functions are continuous with respect to the product topology.
Note that by (2.2), the potential of a continuous potential game is continuous.
Therefore we have:
LEMMA 4.3. Let 0 be a continuous potential game with compact strategy
sets. Then 0 possesses a pure-strategy equilibrium point.

We now proceed to deal with differentiable games. We assume that the strategy
sets under discussion are intervals of real numbers. We omit the obvious proof
of the next lemma.
LEMMA 4.4. Let 0 be a game in which the strategy sets are intervals of real
numbers. Suppose the payoff functions u i : Y i → R, i ∈ N , are continuously
differentiable, and let P: Y → R. Then P is a potential for 0 if and only if P is
continuously differentiable, and

∂P
∂u i
= i
i
∂y
∂y

for every i ∈ N .

The next theorem is well-known (and very useful).

135

POTENTIAL GAMES

THEOREM 4.5. Let 0 be a game in which the strategy sets are intervals of
real numbers. Suppose the payoff functions are twice continuously differentiable.
Then 0 is a potential game iff

∂ 2u j
∂ 2ui
= i j
i
j
∂y ∂y
∂y ∂y

for every i, j ∈ N .

(4.1)

Moreover, if the payoff functions satisfy (4.1) and z is an arbitrary (but fixed)
strategy profile in Y , then a potential for 0 is given by
X Z 1 ∂u i
(x(t))(x i )0 (t) dt,
(4.2)
P(y) =
i
∂
y
0
i∈N
where x: [0, 1] → Y is a piecewise continuously differentiable path in Y that
connects z to y (i.e., x(0) = z and x(1) = y).
Consider for example the quasi-Cournot game described in the Introduction.
It can be easily verified that (4.1) is satisfied (because ∂ 2 u i /∂ y i ∂ y j = a for
every i 6= j ∈ N ), and applying (4.2) yields the potential given in (1.2). Unlike
(weighted) potential games, ordinal potential games are not easily characterized.
We do not know of any useful characterization, analogous to the one given in
(4.1), for differentiable ordinal potential games.

5. THE POTENTIAL AS AN EQUILIBRIUM REFINEMENT TOOL
Let 0 be a potential game and let P be a potential for 0. The set of all strategy
profiles that maximize P is a subset of the equilibria set. By Lemma 2.7, this set
does not depend on a particular potential function.13 Thus, at least technically,
the potential defines a refinement concept.
Consider the version of the Stag Hunt game of Rouseau, as described in
Crawford (1991): There are n players. Player i chooses ei ∈ {1, 2, . . . , 7}. The
payoff 5i of Player i is
5i (e1 , e2 , . . . , en ) = a min(e1 , e2 , . . . , en ) − bei + c,
where a > b ≥ 0, and c is a constant that guarantees positive payoffs. Define a
potential function P as
P(e1 , e2 , . . . , en ) = a min(e1 , e2 , . . . , en ) − b

j
X

ej .

j=1
13 It can also be proved that for weighted potential games, the argmax set of a weighted potential
does not depend on a particular choice of a weighted potential (even though distinct weighted potentials
may be based on different sets of weights (i.e., neither vector of weights is a multiple by a scalar of the
other vector)).

136

MONDERER AND SHAPLEY

Note that if a < nb, then P is maximized at the profile e with ei = 1 for every
1 ≤ i ≤ n. If a > nb, then P is maximized at the strategy profile satisfying
ei = 7 for every i. Surprisingly, the equilibrium selection predicted by the argmax
set of the potential is the one that is supported by the experimental results of
Van Huyck et al. (1990). In Experiment A (using Crawford’s notation), a = 0.2,
b = 0.1, and 14 ≤ n ≤ 16. Thus a < nb. In Experiment B, b was switched
to 0, and therefore a > nb. In Experiments Cd and C f , a = nb. In this case,
every equilibrium profile maximizes the potential, and thus the potential cannot
be used for a prediction. Indeed, in Cd , the players were not using a particular
equilibrium profile. In Experiment C f , which was the same as Cd except for
the fact that the two players were fixed (and not randomly matched), players
tended to choose e1 = e2 = 7. This, to our opinion, reflects the principal that a
repetition is a substitute to cooperation in repeated games.
We do not attempt to explain the success of the argmax set of the potential
to predict behavior in the above potential game. It may be just a coincidence.14
We hope that further experiments will be conducted to test this new refinement
concept.
Van Huyck et al. (1991) conducted another set of experiments on average
opinion games. In this experiments the payoff function of Player i is given by
5i (e1 , e2 , . . . , en ) = α M − β(M − ei )2 + γ ,
where α, β, and γ are positive constants, and M = M(e1 , e2 , . . . , en ) is the
median of (e1 , e2 , . . . , en ).
It can be seen easily that this game does not have a weighted potential, and
thus we are unable to analyze their results via the potential approach. However,
if the
function M is replaced by the mean function, A(e1 , e2 , . . . , en ) =
Pmedian
n
ei , then by Theorem 4.5 the game does have a potential. The unique
1/n i=1
strategy profile that maximizes this potential is ei = 7 for every i. Unfortunately,
we do not know of any experiment conducted with the mean function A.

6. AN APPLICATION TO THE STRATEGIC APPROACH TO VALUE
THEORY
Let N = {1, 2, . . . , n} be the set of players. For each nonempty coalition
S ⊆ N we denote by G(S) the space of all cooperative games with transferable
utility on the set of players S. That is, v ∈ G(S) if and only if v is a real-valued
function defined on the set 2 S of subsets of S with v(∅) = 0. A solution is a
∪ S∈2 N R S such that ψ(v) ∈ R S whenever v ∈ G(S).
function ψ : ∪ S∈2 N G(S) →P
A solution ψ is efficient if i∈S ψv(i) = v(S) for every S ∈ 2 N and for every
v ∈ G(S).
14 See, however, the Introduction for references to a possible explanation suggested by Blume (1993).

137

POTENTIAL GAMES

For each solution ψ and for each c ∈ R N we will define a game in strategic
form 0(ψ, c, v) for every v ∈ G(N ) as follows:
The set of players is N . The set of strategies of player i is Y i = {0, 1}. Player
i can decide not to join the game (choosing 0) and to get a payoff ci , or to
participate in the game (choosing 1). Let S be the set of all players that choose 1.
Then each i ∈ S receives the payoff ψ(v S )(i), where v S ∈ G(S) is the restriction
of v to 2 S . More precisely, for ε ∈ Y = {0, 1} N denote S(ε) = {i ∈ N : εi = 1}.
Then the payoff function u i of player i is
½ i
if εi = 0
c,
i
u (ε) =
ψ(v S(ε) )(i),
if εi = 1.
The games 0(ψ, c, v) will be called the participation games. We now present
two characterizations (a local characterization and a global one) for the Shapley
value in terms of the strategic properties of the participation games.
THEOREM 6.1. Let ψ be an efficient solution on G = ∪ S∈2 N G(S), let c ∈ R N ,
and let v ∈ G(N ). Then ψ is the Shapley value on {v S : S ∈ 2 N } if and only
if 0 = 0(ψ, c, v) is a potential game.

Proof. Let i ∈ N . Then
u i (ε−i , 1) − u i (ε−i , 0) = ψ(v S∪{i} )(i) − ci

for all ε ∈ Y ,

(6.1)

where S = { j 6= i : ε j = 1}.
For S ⊆ N let ε S ∈ Y be defined as follows: εiS = 1 if i ∈ S, and εiS = 0 if
i 6∈ S.
From (6.1) we deduce that 0 is a potential game if and only if there exists
Q: Y → R such that
Q(ε S )− Q(ε S\{i} ) = ψ(v S∪{i} )(i)−ci

for every S ⊆ N and for every i ∈ S.
(6.2)
P
Set P(ε S ) = Q(ε S ) + i∈S ci , then Q satisfies (6.2) iff P satisfies
P(ε S )− P(ε S\{i} ) = ψ(v S∪{i} )(i)

for all S ⊆ N and for every i ∈ S. (6.3)

Thus, the proof follows from Theorem A in Hart and Mas-Colell (1989).
THEOREM 6.2. Let ψ be an efficient solution on G = ∪ S∈2 N G(S), and let
c ∈ R N . Then ψ is the Shapley value on G if and only if 0(ψ, c, v) is a potential
game for every v ∈ G(N ).

Proof. The proof follows from Theorem 6.1.
By Theorem 5.2 in Hart and Mas-Colell (1989) we can also prove the following
characterization of weighted Shapley values.

138

MONDERER AND SHAPLEY

THEOREM 6.3. Let ψ be an efficient solution on G = ∪ S∈2 N G(S), let c ∈ R N ,
let v ∈ G(N ), and let w be a vector of positive weights. Then ψ is the w-Shapley
value on {v S : S ∈ 2 N } if and only if 0 = 0(ψ, c, v) is a w-potential game.

Other results relating noncooperative potential games with cooperative solutions are discussed in Qin (1992).

APPENDIX A
Proof of Theorem 2.8. Obviously (2) H⇒ (3) H⇒ (4). We prove that (1)
⇐⇒ (2) and that (4) H⇒ (2).
(1) H⇒ (2) Suppose P is a potential for 0. Let γ = (y0 , y1 , . . . , y N ) be a
closed path. Then by (2.2)
I (γ , u) = I (γ , (P, P, . . . , P)) = P(y N ) − P(y0 ) = 0.
(2) H⇒ (1) Suppose I (γ , u) = 0 for every closed path γ . Fix z ∈ Y . Let
y ∈ Y . We claim that for every two paths γ1 and γ2 that connect z to y, I (γ1 , u) =
I (γ2 , u). Indeed, suppose γ1 = (z, y1 , . . . , y N ) and γ2 = (z, z 1 , . . . , z M ), where
y N = z M = y. Let µ be the closed path (γ1 , γ2−1 ). That is,
µ = (z, y1 , . . . , y N , z M−1 , z M−2 , . . . , z).
Then I (µ, u) = 0. Therefore I (γ1 , u) = I (γ2 , u). For every y ∈ Y choose a
path, say γ (y), connecting z to y. Define P(y) = I (γ (y), u) for all y ∈ Y . We
proceed to prove that P is a potential for 0. We have just proved that
P(y) = I (γ , u)

for every γ that connects z to y.

(A.1)

Let i ∈ N , let y −i ∈ Y −i , and let a 6= b ∈ Y i . Let γ = (z, y1 , . . . , (y −i , a)) be
a path connecting z to (y −i , a). Set µ = (z, y1 , . . . , (y −i , a), (y −i , b)). Then by
(A.1)
P(y −i , b) − P(y −i , a) = I (µ, u) − I (γ , u) = u i (y −i , b) − u i (y −i , a).
Therefore P is a potential for 0.
(4) H⇒ (2) Suppose I (γ , u) = 0 for every simple closed path γ of length 4.
We denote the length of a closed path γ = (y0 , y1 , . . . , y N ) l(γ ) (= N ).
Suppose that for some closed path, say γ , I (γ , u) 6= 0. Obviously N = l(γ ) ≥
5. Without loss of generality we may assume that I (µ, u) = 0 , whenever
l(µ) < N .
Suppose γ = (y0 , y1 , y2 , . . . , Y N ). Let i( j), 0 ≤ j ≤ N −1, be the unique de−i( j)
i( j)
, x(i( j))), where x(i( j)) 6= yj . Without
viator at step j. That is, yj+1 = (yj
loss of generality assume that i(0) = 1. Since i(0) = 1, and y N = y0 , there exists

139

POTENTIAL GAMES

1 ≤ j ≤ N − 1 such that i( j) = 1. If j = 1 or j = N − 1, we get a contradiction
to the minimality assumption about the length of γ in the following way: Assume
w.l.o.g. that i(1) = 1. Define µ = (y0 , y2 , . . . , y N ). Then, I (µ, u) = I (γ , u),
and l(µ) < N . Assume therefore that 2 ≤ j ≤ N − 2. We show that there exists
z j ∈ Y such that the path µ = (y0 , y1 , . . . , yj−1 , z j , yj+1 , . . . , y N ) satisfies
I (µ, u) = I (γ , u)

and

i( j − 1) = 1.

(A.2)

Indeed, define
−{i( j−1),1}

z j = (yj−1

i( j−1)

1
, yj−1 , yj+1
).

Then, by our assumption on closed paths of length 4,
I ((yj−1 , yj , yj+1 , z j ), u) = 0.
This implies (A.2).
Continuing recursively, we finally find a closed path τ of length N such that
I (τ, u) 6= 0, and i(0) = i(1) = 1, in contradiction to the minimality assumption
We conclude that I (γ , u) = 0 for every closed paths γ .

APPENDIX B
The payoff functions in the congestion game are given in (3.1). We need an
equivalent formulation in order to prove Theorem 3.2. For A = (A1 , A2 , . . . , An )
∈ 6 and for S ⊆ N we denote A(S) = ∪i∈S Ai , and we denote A(−S) = A(S c ),
where S c is the complementary set of S. For S = {i}, A(i) and A(−i) stand
M
for A({i})
Pand A(−{i}) respectively. For x ∈ R and for B ⊆ M we denote
x(B) = j∈B x( j).
LEMMA B.1. Suppose C is a congestion game as described in Section 3.
For every r ∈ N define the vector x r ∈ R M as

x r ( j) = c j (m)

for every j ∈ M.

Then for every i ∈ N and for every A ∈ 6
v i (A) = x 1 (A(i) ∩ A(−i)c )
¢
¡
+ x 2 ∪k6=i [A(i) ∩ A(k) ∩ A(−{i, k})c ]
+ · · · + x n (∩k∈N A(k)) .
Proof. The proof follows from (3.1).

(B.1)

140

MONDERER AND SHAPLEY

Proof of Theorem 3.2. Let 0 be a finite potential game as described in Section 2. The set of players is N = {1, 2, . . . , n}, the strategy sets are (Y i )i∈N , and
the payoff functions are (u i )i∈N . Let P be a potential for 0.
Let k(i) = #Y i be the number of strategies of player i, and assume
i
Y i = {a1i , a2i , . . . , ak(i)
}.
n
For i ∈ N , set K (i) = {1, 2, . . . , k(i)}, and set K = ×i=1
K (i).
We proceed to define an isomorphic congestion game. The facility set M is
defined to be the set of all ε = (ε 1 , ε2 , . . . , εn ), where for every i ∈ N εi is a
vector of 0’s and 1’s of length k(i). That is, εi ∈ {0, 1} K (i) . In other words,
n
M = ×i=1
{0, 1} K (i) .

The strategy sets (6 i )i∈N in the congestion games are defined as
6 i = {Ai1 , Ai2 , . . . , Aik(i) }

for every i ∈ N ,

Ali = {ε ∈ M : εli = 1}

for every l ∈ K (i).

where

We now define vectors (x r )r ∈N in R M such that the payoffs (v i )i∈N defined in
Lemma B.1 satisfy
v i (A1m 1 , A2m 2 , . . . , Anm n ) = u i (am1 1 , am2 2 , . . . , amn n ),
∀i ∈ N and ∀(m 1 , m 2 , . . . , m n ) ∈ K .
For 1 < r < n set x r = 0.
For r = n, x n is defined to be a solution of the following system of equations:
x n (A1m 1 ∩A2m 2 ∩· · ·∩Anm n ) = P(am1 1 , am2 2 , . . . , amn n ),

(m 1 , m 2 , . . . , m n ) ∈ K .
(B.2)
We have to show that a solution to (B.2) exists. For each m = (m 1 , m 2 , . . . , m n ) ∈
K let ε(m) ∈ M be defined as follows: εmi i = 1 for every i ∈ N , and εki = 0 for
every i ∈ N and for every k 6= m i in K (i). Set
M1 = {ε(m): m ∈ K }.
Note that for m 6= l ∈ K , ε(m) 6= ε(l). Therefore we can define x n as
½
P(am1 1 , am2 2 , . . . , amn n ),
if ε = ε(m) ∈ M1
n
x (ε) =
0,
if ε 6∈ M1 .

(B.3)

141

POTENTIAL GAMES

It can be verified easily that for every m ∈ K
A1m 1 ∩ A2m 2 ∩ · · · ∩ Anm n ∩ M1 = {ε(m)}.
Therefore x n satisfies (B.2).
We proceed to define x 1 . Note that by (2.2) for every i ∈ N and for every
−i
a ∈ Y −i , the expression u i (a −i , a i ) − P(a −i , a i ) does not depend on a i ∈ Y i .
That is,
u i (a −i , a i ) − P(a −i , a i ) = u i (a −i , bi ) − P(a −i , bi )

for every a i , bi ∈ Y i .

For every i ∈ N define Q −i : Y −i → R by
Q i (a −i ) = u i (a −i , a i ) − P(a −i , a i ),

(B.4)

where a i is arbitrarily chosen from Y i .
For each i ∈ N and for each m i = (m ik )k6=i ∈ K −i define ε(m i ) ∈ M as
εsi = 1 for every s ∈ K (i), and for every k, k 6= i, εsk = 0 iff s = m ik .
Set
M2 = {ε(m i ): m i ∈ K −i }.

(B.5)

Define x 1 as
(
x (ε) =
1

³
´
Q i (amk i )k6=i ,
k
0,

if ε ∈ M2 and ε = ε(m i )
if ε 6∈ M2 .

It can be verified that for every m = (m 1 , m 2 , . . . , m n ) ∈ K and for A =
(A1m 1 , A2m 2 , . . . , Anm n ) ∈ 6,
¢
¡
x 1 Aim i ∩ A(−i) = x 1 (ε(m i )) = u i (a) − P i (a)

for every i ∈ N , (B.6)

where m i = (m k )k6=i and a = (am1 1 , am2 2 , . . . , amn n ).
Combine (B.6), (B.2), and Lemma B.1 to get that for every i ∈ N ,
v i (A1m 1 , A2m 2 , . . . , Anm n ) = u i (am1 1 , am2 2 , . . . , amn n ),

∀(m 1 , m 2 , . . . , m n ) ∈ K .

We conclude this Appendix with a remark about the minimal number of facilities that are needed to represent potential games by congestion games.
n
, be fixed. Then the
Let the number of players, n, and the strategy sets, (Y i )i=1
dimension d of the linear space of all potential games with n players and with

142

MONDERER AND SHAPLEY

n
the strategy sets (Y i )i=1
is

d=

k
k
k
+
+ ··· +
+ k − 1,
k(1) k(2)
k(n)

where for every i ∈ N , k(i) = #Y i and k = k(1)k(2) · · · k(n).
Suppose we are looking for a fixed set of facilities M with m elements and
for fixed strategy sets (6 i )i∈N with #6 i = k(i) for every i ∈ N , such that each
potential game will be represented by a congestion game with n players, with
the facility set M, and with the strategy sets (6 i )i∈N . Then by Lemma B.1 each
such congestion game is uniquely defined by n vectors (x i )i∈N in R M . Suppose
also that we wish the representation operation to be linear, then we must have
µ
¶
k
k
k
1
+
+ ··· +
+k−1 .
(B.7)
m≥
n k(1) k(2)
k(n)
In the proof of Theorem 3.2, m = 2k(1)+k(2)+···+k(n) . However, instead of M we
could have defined our facility set to be either M1 or M2 ( the one with the greater
number of elements). Hence, the number of facilities m could be reduced to
¶
µ
k
k
k
+
+ ··· +
.
(B.8)
m = max k,
k(1) k(2)
k(n)
Comparing (B.7) to (B.8) indicates that it may be possible to improve upon our
result.

REFERENCES
Bergstrom, C., and Varian, H. R. (1985). “Two Remarks on Cournot Equilibria,” Econ. Lett. 19, 5–8.
Blume, L. E. (1993). “The Statistical Mechanics of Strategic Interaction,” Games Econ. Behav. 5,
387–424.
Brown, G. W. (1951). “Iterative Solution of Games by Fictitious Play,” in Activity Analysis of Production
and Allocation. New York: Wiley.
Crawford, V. P. (1991). “An Evolutionary Interpretation of Van Huyck, Battalio, and Beil’s Experimental
Results on Coordination,” Games Econ. Behav. 3, 25–59.
Deschamps, R. (1973). Ph.D. Thesis. University of Louvain.
Fudenberg, D., and Kreps, D. (1993). “Learning, Mixed Equilibria,” Games Econ. Behav. 5, 320–367.
Fudenberg, D., and Levine, D. K. (1994). “Consistency and Cautious Fictitious Play,” mimeo.
Garcia, C. B., and Zangwill, W. I. (1981). “Pathways to Solutions, Fixed Points, and Equilibria,” New
York: Prentice Hall.
Hart, S., and Mas-Colell, A. (1989). “Potential, Value, and Consistency,” Econometrica 57, 589–614.
Hofbauer, J. (1994). “Stability for the Best Response Dynamics,” mimeo.
Jordan, J. S. (1993). “Three Problems in Learning Mixed-Strategy Nash Equilibria,” Games Econ.
Behav. 5, 368–386.

POTENTIAL GAMES

143

Kandori, M., and Rob, R. (1992). “Evolution of Equilibria in the Long Run: A General Theory and
Applications,” mimeo.
Krishna, V. (1991). “Learning in Games with Strategic Complementarity,” mimeo.
Krishna, V., and Sjöström. (1994). “On the Rate of Convergence of Fictitious Play,” mimeo.
Milchtaich, I. (1996). “Congestion Games With Player–Specific Payoff Functions,” Games Econ.
Behav. 13, 111–124.
Milgrom, P., and Roberts, J. (1991). “Adaptive and Sophisticated Learning in Normal Form Games,”
Games Econ. Behav. 3, 82–100.
Miyasawa, K. (1961). “On the Convergence of the Learning Process in a 2 × 2 Non-zero-sum Two
Person Game,” Economic Research Program, Princeton University, Research Memorandum No. 33.
Monderer, D., and Sela, A. (1992). “Fictitious Play and No-Cycling Conditions,” mimeo.
Monderer, D., Samet, D., and Sela, A. (1994). “Belief Affirming in Learning Processes,” mimeo.
Monderer, D., and Shapley, L. S. (1996). “Fictitious Play Property for Games with Identical Interests,”
J. Econ. Theory 1, 258–265.
Neyman, A. (1991). “Correlated Equilibrium and Potential Games,” mimeo.
Qin, C-Z. (1992). “On a Potential Game for Endogenous Formation of Cooperation Structures,” mimeo.
Robinson, J. (1951). “An Iterative Method of Solving a Game,” Ann. Math. 54, 296–301.
Rosenthal, R. W. (1973). “A Class of Games Possessing Pure-Strategy Nash Equilibria,” Int. J. Game
Theory 2, 65–67.
Roth, A. E., and Erev, I. (1995). “Learning in Extensive-Form Games: Experimental Data and Simple
Dynamic Models in the Intermediate Term,” Games Econ. Behav. 8, 164–212.
Sela, A. (1992). “Learning Processes in Games,” M.Sc. Thesis. The Technion, Haifa, Israel. [In Hebrew].
Shapley, L. S. (1964). “Some Topics in Two-Person Games,” in Advances in Game Theory (M. Dresher,
L. S. Shapley, and A. W. Tucker, Eds.), pp. 1–28, Princeton, NJ: Princeton Univ. Press.
Shin, H. S., and Williamson, T. (1994). “How Much Common Belief Is Necessary for a Convention,”
mimeo.
Slade, M. E. (1993). “What Does an Oligopoly Maximize? J. Ind. Econ., forthcoming.
Van Huyck, J., Battalio, R., and Beil, R. (1990). “Tactic Coordination Games, Strategic Uncertainty,
and Coordination Failure,” Amer. Econ. Rev. 80, 234–248.
Van Huyck, J., Battalio, R., and Beil, R. (1991). “Strategic Uncertainty, Equilibrium Selection Principles, and Coordination Failure in Average Opinion Games,” Quart. J. Econ., 885–910.
Young, H. P. (1993). “The Evolution of Conventions,” Econometrica, 61, 57–84.

