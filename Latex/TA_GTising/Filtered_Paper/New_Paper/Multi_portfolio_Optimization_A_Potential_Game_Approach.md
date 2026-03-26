Multi-portfolio Optimization: A Potential
Game Approach
Yang Yang1 , Francisco Rubio1 , Gesualdo Scutari2 , and Daniel Palomar1
1

Department of Electronic and Computer Engineering
The Hong Kong University of Science and Technology
{yangyang,eerubio,palomar}@ust.hk
2
Department of Electrical Engineering
State University of New York (SUNY) at Buﬀalo
gesualdo@buffalo.edu

Abstract. Trades from separately managed accounts are usually pooled
together for execution and the transaction cost for a given account may
depend on the overall level of trading. Multi-portfolio optimization is a
technique for combing multiple accounts at the same time, considering
their joint eﬀects while adhering to account-speciﬁc constraints. In this
paper, we model multi-portfolio optimization as a game problem and
adopt as a desirable objective the concept of Nash Equilibrium (NE). By
formulating the game problem as a potential game, we are able to provide
a complete characterization of NE and derive iterative algorithms with
a distributed nature and satisfactory convergence property.

1

Introduction

In a couple of ground-breaking articles [1,2] laying down the foundations of
modern portfolio theory, Markowitz introduced half a century ago a fundamental framework for solving the canonical problem of how an individual account
allocates wealth across a portfolio of risky assets by optimizing the associated
risk-return tradeoﬀ. Since then, numerous generalizations, such as limitations
on transaction costs and other portfolio characteristics, have been proposed in
order to eﬀectively model realistic operating conditions underlying the practice
of mean-variance optimization of single portfolio.
In a practical framework, trades of diverse clients are usually pooled and executed simultaneously for the sake of eﬃciency. But trading one account raises the
marginal transaction costs for other accounts, so a particularly relevant problem is that of realistically modeling the trading costs incurred when rebalancing
multiple accounts, and more speciﬁcally their market impact cost. Indeed, in the
multi-portfolio rebalancing problem, the market impact cost associated with a
given account depends on the overall level of trading of all accounts and not
just on its speciﬁc trading requirements. As a consequence, the actual market
impact cost of trading multiple accounts is typically larger than the sum of the
estimated market impact costs of trading each account separately.
R. Jain and R. Kannan (Eds.): GameNets 2011, LNICST 75, pp. 182–189, 2012.
c Institute for Computer Sciences, Social Informatics and Telecommunications Engineering 2012


Multi-portfolio Optimization

183

To the best of our knowledge, O’Cinneide and his collaborators [5] are the
ﬁrst to introduce the simultaneous rebalancing of multiple accounts into a multiportfolio optimization problem. Their approach is based on the maximization of
the total welfare over all accounts, namely the Pareto optimal solution to the
well-known “social planner” problem. Another methodology frequently used is
known as the Nash Equilibrium (NE) approach [4,7]. In NE approach, rather
than colluding to maximize total welfare, each account optimizes its own welfare, under the assumption that the trade decisions of other accounts have been
made and are ﬁxed. A NE is achieved when no account has an incentive to unilaterally deviate from it. Although this has been done in [7], the authors do not
provide any characterizations of the NE. Besides, each account is only subject
to short-selling constraint, which is hardly enough to model various complicated
regulations in practice.
One common shortcoming of [5,7] is that an all-at-once approach is used to
generate optimal trades for all accounts simultaneously. Compared with centralized approach, distributed algorithms are more suitable for implementation,
especially when the number of accounts is large. During each iteration, accounts
are rebalanced independently but taking into account the market impact of the
desired trades of other accounts.
In this paper, the multi-portfolio optimization problem is modeled as a game
problem and NE is adopted as the desirable objective. We ﬁrst consider a Nash
Equilibrium Problem where one player’s feasible strategy set is independent of
other players. We then generalize the problem by incorporating global constraints
imposed on all accounts, which may arise due to practical considerations such
as transaction size constraint over multiple accounts. In both cases, we give a
complete characterizations of the NE and derive iterative algorithms that can
be implemented in a distributed manner.

2

Problem Formulation

Treating the market-impact in a single account optimization as if it is the only
account being traded underestimates the true trading cost of rebalancing each
account. Instead, the market-impact caused by all accounts being optimized simultaneously should be considered. Under this consideration, the utility function
for account n is deﬁned as [7]
1
1
un (wn , w−n ) = αTn wn − ρ · wnT Qwn − δ · wnT Ω
2

2

 N



wm

,

(1)

m=1

where for account n, αTn wnis the expected
return, ρwnT Qwn represents the


N
penalization for risk, δ·wnT Ω
m=1 wm is a nonlinear market-impact function
while aggregate eﬀects generated by other accounts are taken into account.
The maximization of account n’s utility function (1), however, is subject to
one or various kinds of constraints due to practical considerations. Some of them

184

Y. Yang et al.

include short-selling constraint, holding constraint, budget constraint and cardinality constraint. Since our discussion does not depend on the type of constraints,
we use a simple notation Kn to denote the set of account n’s feasible strategies.
We further assume that Kn is a non-empty, closed and convex set, and it is
independent of the other accounts’ strategies.
Given the utility fuction (1) and strategy set Kn , we formulate the system
design as a Nash Equilibrium Problem (NEP) using as desirable criterion the
concept of Nash Equilibrium (NE). Speciﬁcally, we consider a strategic noncooperative game in which the players are the accounts. Each player n competes
against the others by choosing a strategy wn that maximizes his own utility
function. In other words, given the strategy of other players, player n solves the
following optimization problem:

maximize un (wn , w−n )
wn
∀n.
(2)
subject to wn ∈ Kn
A NE is achieved when no player has an incentive to deviate unilaterally, which
is formally deﬁned as follows:
Deﬁnition 1. A (pure) strategy profile w = (wn )N
n=1 is a NE of NEP (2) if


) ≥ un (wn , w−n
), ∀wn ∈ Kn , ∀n,
un (wn , w−n
N

with w−n = (wm )m=1,m=n .

3

Potential Game and Its Characterizations

To deal with NEP (2), we use in this paper a framework given by potential game
theory [3,8], which allows us to infer the properties of NEP by solving a single
optimization problem.
To begin with, a potential game is formally deﬁned below.
Deﬁnition 2. A strategic game (2) is called an exact potential game if there
exists a function P : K → R such that for all n and (wn1 , w−n ), (wn2 , w−n ) ∈ K:
un (wn1 , w−n ) − un (wn2 , w−n ) = P(wn1 , w−n ) − P(wn2 , w−n ).

(3)

With the deﬁnition of potential game in (3), it is easy to see that the set of
NE for NEP (2) remains the same when all utility functions in (2) are replaced
with P(w). This implies that we can study the properties of NEs using a single
function that does not depend on the particular player. Furthermore, it is natural
to ask what is the relationship between NEs of NEP (2) and the maxima of P,
which can be obtained by solving:
maximize P(w)
w

subject to w ∈ K.

(4)

Multi-portfolio Optimization

185

Lemma 1. [8] Let NEP (2) be a potential game with potential function P. If
w is a maximum of P, then it is a NE of NEP (2). If K is a convex set with a
Cartesian structure, i.e., K = K1 × K2 × . . . × KN , and w is a NE of NEP (2),
then w is a maximum of P.
Recall that in Section 2, we have assumed that Kn is independent of other
players. Then Lemma 1 indicates that w is a NE of NEP (2) if and only if
it is a maximum of NLP (4). This provides us with new intuition to study the
potential game, which is the framework of standard optimization theory applied
to the potential function.
To make use of Lemma 1, we ﬁrst deﬁne a function θ1 (w) as
θ1 (w) 

1 T
w M1 w − α,
2
N

(5)
N

where M1  I ⊗ (ρQ + δΩ) + 2δ · S ⊗ Ω, α  (αn )n=1 , w  (wn )n=1 , and
⎡
⎤
0 1 ... 1
⎢1 0 ... 1⎥
⎢
⎥
S  ⎢ . . . . ⎥.
(6)
⎣ .. .. . . .. ⎦
1 1 ... 0
Using the deﬁnition of potential function, we can readily show that NEP (2) is
a potential game, as stated in the following theorem.
Theorem 1. [10] Suppose each player’s strategy set Kn is independent of other
players’ strategies and K has a Cartesian structure, NEP (2) is equivalent to the
following optimization problem:
maximize θ1 (w)
w

subject to w ∈ K.

(7)

The equivalence of NEP (2) and NLP (7) enables us to explore the existence
and uniqueness of NE of NEP (2) by considering NLP (7). The result is stated
in the following theorem.
Theorem 2. [10] Suppose each player’s strategy set Kn is independent of other
players’ strategies and K has a Cartesian structure, the Nash Equilibrium Problem (2) always has a unique NE.
We mention that the pareto-optimal solution of NEP (2), i.e., the optimal solution to the sum-utility maximization problem, can be interpreted as the NE of a
NEP with a modiﬁed objective function. Interested readers are referred to [10]
for details.
Given the existence and uniqueness of NE, a natural question is that is there
any algorithm that can be implmented in a distributed manner and has satisfactory convergence behavior? We consider best-response based iterative algorithms
with both sequential (Gauss-Seidel) and simultaneous (Jacobi) update, as described in Algorithm 1.

186

Y. Yang et al.

Algorithm 1. Iterative Best Response Algorithm
Data : Choose any wn0 ∈ Kn for all n = 1, 2, . . . , N , and set q = 0.
Step 1: If wq satisﬁes a suitable termination criterion: STOP.
Step 2: Sequentially or Simultaneously for n = 1, 2, . . . , N , update wnq+1 as follows:
Sequential (Gauss-Seidel) Update:
q+1
q
q
, wn , wn+1
, . . . , wN
).
wnq+1  arg minwn ∈Kn un (w1q+1 , . . . , wn−1
Simultaneous (Jacobi) Update:
q
q
q
, wn , wn+1
, . . . , wN
).
wnq+1  (1 − N1 )wnq + N1 · arg minwn ∈Kn ui (w1q , . . . , wn−1
Step 3: Set q ← q + 1; and go to Step 1.
∞

Theorem 3. [10] Any sequence {wq }q=0 generated by the sequential and simultaneous update of iterative best-response algorithm in Algorithm 1 converges to
the unique NE of NEP (2), for any given updating order of the users.

4

Generalized Nash Equilibrium Problem

In all previous developments we have assumed that one player’s strategy set is
independent of the rival players’ actions, but this is not always the case. There
are many applications of interest where the feasible sets naturally depend on
the variables of the player’s rivals. In this section, we consider the NEP (2)
with global constraints as in (8). This results in a generalized Nash Equilibrium
Problem (GNEP), which are formally described as follows:
⎫
maximize αTn wn − 12 ρwnT Qwn
⎪
⎪
wn
⎪

⎪
N 
⎪


⎪
subject to m=1 wn,i ≤ Ci , ∀i = 1, . . . , I
⎪
⎪
⎪
⎬
N 
|w
|
≤
U
,
∀l
=
1,
.
.
.
,
L
∀n,
(8)
m,j
l
j∈Jl
m=1
⎪
⎪
⎪
T



⎪
⎪
N
N
⎪
δΩ
⎪
m=1 wm
m=1 wm ≤ T
⎪
⎪
⎭
wn ∈ Kn
Note that we have preserved Kn to exclusively denote one player’s individual
constraints such as budget constraint. The ﬁrst and second global constraint in
(8) represents the transaction size constraint over multiple accounts and limitations on the amount invested over groups of assets with related characteristics,
respectively. In this formulation, we remove the market-impact function from
the objective and incorporate it as the third global constraint in (8).
We call a game problem with coupled constraint sets as deﬁned in (8) a
Generalized Nash-Equilibrium Problem (GNEP). To analyze the GNEP (8),
we can follow a similar approach as that in Section 3. After some elementary
algebra, it can be shown that GNEP (8) is a potential game with the following
constrained optimization problem:

Multi-portfolio Optimization

187

maximize αT w − 12 wT (I ⊗ ρQ) w
w

subject to w ∈ K1 × . . . × KN
g(w) ≤ 0,
where

⎡


N

n=1 |wn,i | − Ci

I

(9)
⎤

⎥
⎢
i=1
⎥
⎢ 

⎥
⎢
L
N 
⎥.
g(w)  ⎢
⎥
⎢
j∈Jl |wn,j | − Ul
n=1
l=1
⎥
⎢
⎦
⎣
T


N
N
δΩ
n=1 wn
n=1 wn − T,

(10)

We denote the feasible set of (9) as K  {w : w ∈ K1 × . . . × KN , g(w) ≤ 0}. It
is easy to see that NLP (9) is a strongly convex optimization problem, and it
has a unique maximum.
Note that in NLP (9), K does not have a Cartesian structure. The equivalence
between GNEP (8) and NLP (9) as indicated by Lemma 1 may not hold any more.
As shown in [9,6,8], a NE of GNEP (8) is not necessarily a maximum of NLP (9).
Nash Equilibriums of the GNEP (8) that are also maxima of NLP (9) are termed
as Variational Equilibriums (VE). In another word, GNEP (8) and NLP (9) are
equivalent in the sense of VE. From now on, we will focus on the VE of the GNEP
(8) and give detailed analysis on its existence, uniqueness and algorithms.
Theorem 4. [10] There always exists a unique variational equilibrium of GNEP
(8).
The potential game formulation of GNEP (8), i.e., NLP (9), not only serves as
a direct way to characterize the VE, but also provides us with some intuition to
devise distributed algorithms achieving the VE. First we derive a result that is
valid for all potential games.
Theorem 5. [10] Consider a Nash Equilibrium game where each players solves
the following convex optimization problem

maximize fn (wn , w−n )
wn
∀n
(11)
subject to wn ∈ Kn ,
with a concave potential function P(w). Now suppose a global convex constraint
g(w) ≤ 0 is imposed on all players, i.e., each player solves the following optimization problem
⎫
maximize fn (wn , w−n ) ⎪
⎬
wn
∀n.
(12)
subject to wn ∈ Kn
⎪
⎭
g(w) ≤ 0.
Then w is a Variational Equilibrium of GNEP (12) if and only if it is a Nash
Equilibrium of the following NEP

188

Y. Yang et al.

maximize fn (wn , w−n ) − λT · g(w)
wn

subject to wn ∈ Kn


∀n

(13)

with λ such that 0 ≤ λ⊥g(w ) ≤ 0.
Thanks to Theorem 5, we have transformed GNEP (12) with coupled strategy set
into NEP (13) with no coupling in strategy set. The transformation is beneﬁcial
because we can solve GNEP (12) in a distributed manner. Speciﬁcally, we can
design a double-loop algorithm, where in the outer loop, the price tuple λ is
updated by sub-gradient method, and in the inner loop, NEP (13) is solved
using Algorithm 1. We summarize this double-loop algorithm in Algorithm 2.
Algorithm 2. Sub-gradient Algorithm
Data: Choose any λ(0) ≥ 0, and set q = 0.
Step 1: If λ(q) satisﬁes a suitable termination

 criterion: STOP.

(q)
of NEP (13) using Algorithm 1.
Step 2: Compute the unique NE w λ




(q+1)
(q)
(q)

(q)
Step 3: λ
, where γ (q) is the q-th stepsize.
= λ −γ ·g w λ
Step 4: q ← q + 1; go to Step 1.

A common criterion for choosing the stepsize γ (q) in Algorithm is that γ (q)
must be square summable, but not absolute summable. The convergence property of Algorithm 2 is given by the following theorem.
Theorem 6. [10] Algorithm 2 solving GNEP (12) converges as long as Algorithm 1 solving NEP (11) converges.
Theorem 6 indicates that the introduction of global convex constraints does not
require stricter convergence conditions. For GNEP (8), as we have already proved
in Theorem 3 that Algorithm 1 always converges, we can therefore conclude that
Algorithm 2 can surely converge to the unique VE of GNEP (8).

5

Discussions and Conclusions

In Figure 1, we show the convergence of Algorithm 1 and Algorithm 2. From
Figure 1(a), the sequential update of best-response iterative algorithm converges
to the unique NE very fast. On the other hand, the convergence speed of the
simultaneous update of best-response iterative algorithm depends on N , the
number of accounts. When there are a large number of accounts, its convergence
speed is typically small.
Figure 1(b) shows that the outer-loop price tuple λ converges with a satisfactory convergence speed. As we have pointed out before, the convergence of
inner-loop best-response iterative algorithm guarantees the convergence of Algorithm 2.
In conclusion, we have modeled the multi-portfolio optimization problem as a
Nash Equilibrium problem and analyze it under the framework of potential game.

Multi-portfolio Optimization

189

1

1

10

10

Gauss−Seidel Update
Jacobi Update

0

10

0

10

−1

 λq − λ  2

 wq − w 2

10
−1

10

−2

10

−2

10

−3

10

−4

10
−3

10

−5

10
−4

10

−6

0

5

10

15
iteration

20

(a) Algorithm 1

25

30

10

0

5

10

15
iteration

20

25

30

(b) Algorithm 2

Fig. 1. Convergence Behavior of Algorithm 1 and Algorithm 2

Speciﬁcally, we consider both NEP with uncoupled strategy set and generalized
NEP with global constraints imposed on all players. We then give a complete
characterizations of NE of NEP and VE of GNEP. We further derive iterative
algorithms that can be implemented in a distributed manner and has satisfactory
convergence behavior.

References
1. Markovitz, H.: Portfolio selection. Journal of Finance 7(1), 77–91 (1952)
2. Markowitz, H.M.: Portfolio selection: Eﬃcient diversiﬁcation of investments. Wiley
(1959)
3. Monderer, D., Shapley, L.S.: Potential games. Games and Economic Behavior 14,
124–143 (1996)
4. Nash, J.: Non–cooperative games. Annals of Mathematics 54(2), 286–295 (1951)
5. O’Cinneide, C., Scherer, B., Xu, X.: Pooling trades in a quantitative investment
process. The Journal of Portfolio Management 32(4), 33–43 (2006)
6. Pang, J.S., Scutari, G., Palomar, D., Facchinei, F.: Design of cognitive radio
systems under temperature-interference constraints: A variational inequality approach. IEEE Transactions on Signal Processing 58(6), 3251–3271 (2010)
7. Savelsbergh, M.W.P., Stubbs, R.A., Vandenbussche, D.: Multiportfolio optimization: A natural next step. In: Guerard, J.B. (ed.) Handbook of Portfolio Construction, pp. 565–581. Springer, US (2010)
8. Scutari, G., Barbarossa, S., Palomar, D.: Potential games: A framework for vector
power control problems with coupled constraints. In: ICASSP 2006 Proceedings,
vol. 4 (2006)
9. Scutari, G., Facchinei, F., Pang, J.S., Palomar, D.P.: Monotone communication
games: Theory, algorithms, and models. Submitted to IEEE Transactions on nformation Theory (2010)
10. Yang, Y., Rubio, F., Scutari, G., Palomar, D.: Multi-portfolio optimization: A
potential game approach (2011) (in preparation)

