FUNDAMENTALS OF QUANTUM
MUTUAL ENTROPY AND CAPACITY

arXiv:quant-ph/9806042v2 14 Jun 1998

Masanori Ohya
Department of Information Sciences
Science University of Tokyo
Noda City, Chiba 278-8510, Japan

1

Introduction

The study of mutual entropy (information) and capacity in classical system
was extensively done after Shannon by several authors like Kolmogorov [12]
and Gelfand [7]. In quantum systems, there have been several definitions of
the mutual entropy for classical input and quantum output [5, 8, 9, 14]. In
1983, the author defined [21] the fully quantum mechanical mutual entropy
by means of the relative entropy of Umegaki [35], and he extended it [23] to
general quantum systems by the relative entropy of Araki [3] and Uhlmann
[34]. When the author introduced the quantum mutual entropy, he did not
indicate that it contains other definitions of the mutual entropy including
classical one, so that there exist several misunderstandings for the use of
the mutual entropy (information) to compute the capacity of quantum channels. Therefore in this note we point out that our quantum mutual entropy
generalizes others and where the misuse occurs.

2

Mutual Entropy

The quantum mutual entropy was introduced in [21] for a quantum input
and quantum output, namely, for a purely quantum channel, and it was generalized for a general quantum system described by C*-algebraic terminology
[23]. We here review the mutual entropy in usual quantum system described
by a Hilbert space.
Let H be a Hilbert space for an input space, B(H) be the set of all
bounded linear operators on H and S(H) be the set of all density operators
∼
on H. An output space is described by another Hilbert space H , but often
1

∼

H = H. A channel from the input system to the output system is a mapping
∼
Λ* from S(H) to S(H) [20]. A channel Λ* is said to be completely positive
if the dual map Λ satisfies the following condition: Σnk,j=1 A∗k Λ(Bk∗ Bj )Aj ≥ 0
∼

for any n ∈N and any Aj ∈ B(H), Bj ∈ B(H). This condition is not strong
at all because almost all physical transformations satisfy it [10, 23].
An input state ρ ∈ S(H) is sent to the output system through a channel
∼
Λ*, so that the output state is written as ρ≡ Λ∗ ρ. Then it is important to
ask how much information of ρ is correctly sent to the output state Λ∗ ρ. This
amount of information transmitted from input to output is expressed by the
mutual entropy.
In order to define the mutual entropy, we first mention the entropy of a
quantum state introduced by von Neumann [19]. For a state ρ, there exists
a unique spectral decomposition
ρ = Σk λk Pk ,

(2.1)

where λk is an eigenvalue of ρ and Pk is the associated projection for each
λk . The projection Pk is not one-dimensional when λk is degenerated, so that
the spectral decomposition can be further decomposed into one-dimensional
projections. Such a decomposition is called a Schatten decomposition [33],
namely,
ρ = Σk λk Ek ,

(2.2)

where Ek is the one-dimensional projection associated with λk and the degenerated eigenvalue λk repeats dimPk times; for instance, if the eigenvalue
λ1 has the degeneracy 3, then λ1 = λ2 = λ3 < λ4 . This Schatten decomposition is not unique unless every eigenvalue is non-degenerated. Then the
entropy (von Neumann entropy) S (ρ) of a state ρ is defined by
S (ρ) = −trρ log ρ,

(2.3)

which equals to the Shannon entropy of the probability distribution {λk } :
X
S (ρ) = −
λk log λk .
(2.4)
k

The quantum mutual entropy was introduced on the basis of the above
von Neumann entropy for purely quantum communication processes. The
2

mutual entropy depends on an input state ρ and a channel Λ∗ , so it is denoted
by I (ρ; Λ∗ ), which should satisfy the following conditions:
(1) The quantum mutual entropy is well-matched to the von Neumann
entropy. Furthermore, if a channel is trivial, i.e., Λ∗ = identity map, then
the mutual entropy equals to the von Neumann entropy: I (ρ; id) = S (ρ).
(2) When the system is classical, the quantum mutual entropy reduces to
classical one.
(3) Shannon’s fundamental inequality [32] 0≤ I (ρ; Λ∗ ) ≤ S (ρ) is held.
Before mentioning the quantum mutual entropy,
 we briefly review the
classical mutual entropy [6]. Let (Ω, F ) , Ω, F be an input and output

measurable spaces, respectively, and P (Ω) , P Ω are the corresponding sets
of all probability measures (states)
on Ω and Ω , respectively. A channel Λ∗ is

a mapping from P (Ω) to P Ω and its dual Λ is a map from the set B (Ω) of

all Baire measurable functions on Ω to B Ω . For an input state µ ∈ P (Ω) ,
the output state µ = Λ∗ µ and the joint state (probability measure) Φ is given
by
Z

Λ (1Q ) dµ, Q ∈ F , Q ∈ F,
(2.5)
Φ Q× Q =
Q



1 (ω ∈ Q)
. The
0 (ω ∈
/ Q)
classical entropy, relative entropy and mutual entropy are defined as follows:
( n
)
X
S (µ) = sup −
µ (Ak ) log µ (Ak ) ; {Ak } ∈ P (Ω) ,
(2.6)

where 1Q is the characteristic function on Ω : 1Q (ω) =

k=1

S (µ, ν) = sup

( n
X
k=1

)
µ (Ak )
µ (Ak ) log
; {Ak } ∈ P (Ω) ,
ν (Ak )

I (µ; Λ∗) = S (Φ, µ ⊗ Λ∗ µ) ,

(2.7)
(2.8)

where P (Ω) is the set of all finite partitions on Ω, that is, {Ak } ∈ P (Ω) iff
Ak ∈ F with Ak ∩ Aj = ∅ (k 6= j)and ∪nk=1 Ak = Ω.
The quantum mutual entropy is defined as follows: In order to define the
quantum mutual entropy, we need the quantum relative entropy and the joint
state (it is called ”compound state” in the sequel) describing the correlation
between an input state ρ and the output state Λ∗ ρ through a channel Λ∗ .

3

A finite partition of Ω in classical case corresponds to an orthogonal decomposition {Ek } of the identity operator I of H in quantum case because the
set of all orthogonal projections is considered to make an event system in a
quantum system. It is known [28] that the following equality holds
)
(
X
trρEk log trρEk ; {Ek } = −trρ log ρ,
sup −
k

and the supremum is attained when {Ek } is a Schatten decomposition of ρ.
Therefore the Schatten decomposition is used to define the compound state
and the quantum mutual entropy.
The compound state σE (corresponding to joint state in CS) of ρ and Λ∗ ρ
was introduced in [21, 22], which is given by
X
σE =
λk Ek ⊗ Λ∗ Ek ,
(2.9)
k

where E stands for a Schatten decomposition {Ek } of ρ, so that the compound state depends on how we decompose the state ρ into basic states
(elementary events), in other words, how to see the input state.
The relative entropy for two states ρ and σ is defined by Umegaki [35]
and Lindblad [15], which is written as

S (ρ, σ) =



trρ (log ρ − log σ) (when ranρ ⊂ ranσ)
∞
(otherwise)

(2.10)

Then we can define the mutual entropy by means of the compound state
and the relative entropy [21], that is,
I (ρ; Λ∗ ) = sup {S (σE , ρ ⊗ Λ∗ ρ) ; E = {Ek }} ,

(2.11)

where the supremum is taken over all Schatten decompositions because this
decomposition is not unique generally. Some computations reduce it to the
following form:
)
(
X
λk S (Λ∗ Ek , Λ∗ ρ) ; E = {Ek } .
(2.12)
I (ρ; Λ∗ ) = sup
k

This mutual entropy satisfies all conditions (1)∼(3) mentioned above.
4

When the input system is classical, an input state ρ is given by a probability distribution or a probability measure, in either case, the Schatten
decomposition of ρ is unique, namely, for the case of probability distribution
; ρ = {λk } ,
X
ρ=
λk δk ,
(2.13)
k

where δk is the delta measure, that is,

1(k=j)

δk (j) = δk,j = {0(k6=j) , ∀j.

(2.14)

Therefore for any channel Λ∗ , the mutual entropy becomes
X
λk S (Λ∗ δk , Λ∗ ρ) ,
I (ρ; Λ∗ ) =

(2.15)

k

which equals to the following usual expression of Shannon when the minus
is well-defined:
X
(2.16)
λk S (Λ∗ δk ) .
I (ρ; Λ∗ ) = S (Λ∗ ρ) −
k

The above equality has been taken as the definition of the mutual entropy
for a classical-quantum channel [4, 5, 8, 9, 14].
Note that the definition (2.12) of the mutual entropy is written as
(
)
X
X
I (ρ; Λ∗ ) = sup
λk S (Λ∗ ρk , Λ∗ ρ) ; ρ =
λk ρk ∈ Fo (ρ) ,
k

k

where Fo (ρ) is the set of all orthogonal finite decompositions of ρ. Here
ρk is orthogonal to ρj (denoted by ρk ⊥ ρj ) means that the range of ρk is
orthogonal to that of ρj. The equality is easily proved as follows: Put
(
)
X
X
∗
∗
∗
If (ρ; Λ ) = sup
λk S (Λ ρk , Λ ρ) ; ρ =
λk ρk ∈ Fo (ρ) .
k

k

The inequality I (ρ; Λ∗ ) ≤ If (ρ; Λ∗ ) is obvious. Let us prove the converse.
Each ρk in an orthogonal decomposition
ρ is further decomposed into
P (k)of (k)
one dimensional projections; ρk =
j µj Ej , a Schatten decomposition
of ρk . From the following equalities of the relative entropy [3, 28]: (1)
5

S (aρ, bσ) = aS (ρ, σ) − a log ab , for any positive number a, b; (2) ρ1 ⊥ ρ2
=⇒ S (ρ1 + ρ2 , σ) = S (ρ1 , σ) + S (ρ2 , σ), we have 
P
P
P
(k)
(k)
(k)
∗
∗
∗ (k)
∗
k λk S (Λ ρk , Λ ρ) =
k,j λk µj S Λ Ej , Λ ρ +
k,j λk µj log µj


P
(k)
(k)
≤ k,j λk µj S Λ∗ Ej , Λ∗ρ ,
which implies the converse inequality I (ρ; Λ∗ ) ≥ If (ρ; Λ∗ ) because
P
(k) (k)
is a Schatten decomposition of ρ. Thus I (ρ; Λ∗ ) = If (ρ; Λ∗ ) .
k,j λk µj Ej
More general formulation of the mutual entropy for general quantum systems was done [23, 10] in C*dynamical system by using Araki’s or Uhlmann’s
relative entropy [3, 34, 28]. This general mutual entropy contains all other
cases including measure theoretic definition of Gelfand and Yaglom [7].
The mutual entropy is a measure for not only information transmission
but also description of state change, so that this quantity can be applied to
several topics [1, 2, 16, 18, 23, 24, 27, 31].

3

Communication Processes

We discuss communication processes in this section[6, 9, 28]. Let A = {a1, a2, ·
·, an } be a set of certain alphabets and Ω be the infinite direct product of A :
Ω = AZ ≡ Π∞
−∞ A calling a message space. In order to send a information
written by an element of this message space to a receiver, we often need to
transfer the message into a proper form for a communication channel. This
change of a message is called a coding. Precisely, a coding is a measurable
one to one map ξ from Ω to a proper space X . For instance, we have the
following codings: (1) When a message is expressed by binary symbol 0 and
1, such a coding is a map from Ω to {0, 1}N . (2) A message expressed by 0,1
sequence in (1) is represented by an electric signal. (3) Instead of an electric
signal, we use optical signal. Coding is a combination of several maps like
the above (1) and (2), (3). One of main targets of the coding theory is to find
the most efficient coding and also decoding for information transmission.
Let (Ω, FΩ , P (Ω)) be an input probability space and X be the coded
input space. This space X may be a classical object or a quantum object.
For instance, X is a Hilbert space H of a quantum system, then the coded
input system is described by (B(H), S(H))of Sec.2.
An output system is similarly described as the input system: The coded
∼
∼
output space is denoted by X and the decoded output space is Ω made by
6

∼

another alphabets. An transmission (map) from X to X is described by a
channel reflecting all properties of a physical device, which is denoted by
∼

γ here. With a decoding ξ, the whole information transmission process is
written as
∼
ξ

γ

∼

ξ

∼

Ω −→ X −→X −→Ω .

(3.1)

That is, a message ω ∈ Ω is coded to ξ (ω) and it is sent to the output system
through a channel γ, then the output coded message becomes γ ◦ ξ (ω) and
∼

it is decoded to ξ ◦γ ◦ ξ (ω) at a receiver.
This transmission process is mathematically set as follows: M messages
are sent to a receiver and the kth message ω (k) occurs with the probability λk . Then the occurrence
probability of each message in the sequence

ω (1) , ω (2) , · · ·, ω (M ) of M messages is denoted by ρ = {λk } , which is a state
in a classical system. If ξ is a classical coding, then ξ (ω) is a classical object
such as an electric pulse. If ξ is a quantum coding, then ξ (ω) is a quantum
object (state) such as a coherent state. Here we consider such a quantum

(k)
coding, that is, ξ ω (k) is a quantum state, and we denote
ξ
ω
by σk .

Thus the coded state for the sequence ω (1) , ω (2) , · · ·, ω (M ) is written as
X
σ=
λk σk .
(3.2)
k

This state is transmitted through a channel γ. This channel is expressed by
a completely positive mapping Γ∗ , in the sense of Sec.1, from the state space
∼
∼
of X to that of X , hence the output coded quantum state σ is Γ∗ σ. Since
the information transmission process can be understood as a process of state
∼
∼
(probability) change, when Ω and Ω are classical and X and X are quantum,
the process (3.1) is written as
Ξ∗

Γ∗

∼

∼∗

Ξ

∼

P (Ω) −→ S (H) −→ S( H) −→ P (Ω),

(3.3)
∼

∼∗

where Ξ∗ (resp.Ξ ) is the channel corresponding to the coding ξ (resp. ξ ) and
∼
∼
S (H) (resp.S( H) ) is the set of all density operators (states) on H (resp.H
).
We have to be care to study the objects in the above transmission process
(3.1) or (3.3). Namely, we have to make clear which object is going to study.
For instance, if we want to know the information capacity of a quantum
7

channel γ(= Γ∗ ), then we have to take X so as to describe a quantum system
like a Hilbert space and we need to start the study from a quantum state in
quantum space X not from a classical state associated to a message. If we like
to know the capacity of the whole process including a coding and a decoding,
∼

∼∗

which means the capacity of a channel ξ ◦γ ◦ ξ(=Ξ ◦ Γ∗ ◦ Ξ∗ ), then we have
to start from a classical state. In any case, when we concern the capacity of
channel, we have only to take the supremum of the mutual entropy I (ρ; Λ∗ )
over a quantum or classical state ρ in a proper set determined by what we
like to study with a channel Λ∗ . We explain this more precisely in the next
section.

4

Channel Capacity

We discuss two types of channel capacity in communication processes, namely,
the capacity of a quantum channel Γ∗ and that of a classical (classical∼∗

quantum-classical) channel Ξ ◦ Γ∗ ◦ Ξ∗ .
(1) Capacity of quantum channel: The capacity of a quantum channel is
the ability of information transmission of the channel itself, so that it does
not depend on how to code a message being treated as a classical object and
we have to start from an arbitrary quantum state and find the supremum of
the mutual entropy. One often makes a mistake in this point. For example,
one starts from the coding of a message and compute the supremum of the
mutual entropy and he says that the supremum is the capacity of a quantum
channel, which is not correct. Even when his coding is a quantum coding
and he sends the coded message to a receiver through a quantum channel, if
he starts from a classical state, then his capacity is not the capacity of the
quantum channel itself. In his case, usual Shannon’s theory is applied because
he can easily compute the conditional distribution by a usual (classical) way.
His supremum is the capacity of a classical-quantum-classical channel, and
it is in the second category discussed below.
The capacity of a quantum channel Γ∗ is defined as follows: Let S0 (⊂
S(H)) be the set of all states prepared for expression of information. Then
the capacity of the channel Γ∗ with respect to S0 is defined by
C S0 (Γ∗ ) = sup{I (ρ; Γ∗ ) ; ρ ∈ S0 }.

(4.1)

Here I (ρ; Γ∗ ) is the mutual entropy given in (2.11) or (2.12) with Λ∗ = Γ∗ .
8

When S0 = S(H) , C S(H) (Γ∗ ) is denoted by C (Γ∗ ) for simplicity. In [29, 17],
we also considered the pseudo-quantum capacity Cp (Γ∗ ) defined by (4.1)
with the pseudo-mutual entropy Ip (ρ; Γ∗ ) where the supremum is taken over
all finite decompositions instead of all orthogonal pure decompositions:
)
(
X
X
λk ρk , finite decomposition .
λk S (Γ∗ ρk , Γ∗ ρ) ; ρ =
Ip (ρ; Γ∗ ) = sup
k

k

(4.2)
However the pseudo-mutual entropy is not well-matched to the conditions
explained in Sec.2, and it is difficult to be computed numerically [30]. From
the monotonicity of the mutual entropy [28], we have
0 ≤ C S0 (Γ∗ ) ≤ CpS0 (Γ∗ ) ≤ sup {S(ρ); ρ ∈ S0 } .
(2) Capacity of classical-quantum-classical channel: The capacity of C-Q∼∗

C channel Ξ ◦ Γ∗ ◦Ξ∗ is the capacity of the information transmission process
starting from the coding of messages, therefore it can be considered as the
capacity including a coding (and a decoding). As is discussed in Sec.3, an
input state ρ is the probability distribution {λk } of messages, and its Schatten
decomposition is unique as (2.13), so the mutual entropy is written by (2.15):


∼∗

∗

∗

I ρ; Ξ ◦ Γ ◦ Ξ



=

X
k

∼∗

∼∗
∗
∗
∗
∗
λk S Ξ ◦ Γ ◦ Ξ δk , Ξ ◦ Γ ◦ Ξ ρ .

(4.3)

If the coding Ξ∗ is a quantum coding, then Ξ∗ δk is expressed by a quantum
state. Let denote the coded quantum state by σk and put σ = Ξ∗ ρ =
P
k λk σk . Then the above mutual entropy is written as

∼∗
 X
 ∼∗
∼∗
(4.4)
λk S Ξ ◦ Γ∗ σk , Ξ ◦ Γ∗ σ .
I ρ; Ξ ◦ Γ∗ ◦ Ξ∗ =
k

This is the expression of the mutual entropy of the whole information transmission process starting from a coding of classical messages. Hence the capacity of C-Q-C channel is
∼∗

 ∼∗

C P0 Ξ ◦ Γ∗ ◦ Ξ∗ = sup{I ρ; Ξ ◦ Γ∗ ◦ Ξ∗ ; ρ ∈ P0 },
(4.5)

where P0 (⊂ P (Ω)) is the set of all probability distributions prepared for
input (a-priori) states (distributions or probability measures). Moreover the
9

capacity for coding is found by taking the supremum of the mutual entropy
(4.4) over all probability distributions and all codings Ξ∗ :
∼∗

 ∼∗

P0
∗
∗
∗
Cc Ξ ◦ Γ = sup{I ρ; Ξ ◦ Γ ◦ Ξ ; ρ ∈ P0 , Ξ∗ }.
(4.6)
The last capacity is for both coding and decoding and it is given by

 ∼∗
∼∗
P0
( Γ∗ ) = sup{I ρ; Ξ ◦ Γ∗ ◦ Ξ∗ ; ρ ∈ P0 , Ξ∗ , Ξ }.
Ccd

(4.7)

P0
These capacities CcP0 , Ccd
do not measure the ability of the quantum channel
∗
Γ itself, but measure
of Γ∗ through the coding and decoding.
P the ability
∗
Remark that k λk S(Γ σk ) is finite, then (4.4) becomes
 ∼∗

X
∼∗
∼∗
∗
∗
λk S(Ξ ◦Γ∗ σk ).
(4.8)
I ρ; Ξ ◦ Γ ◦ Ξ = S(Ξ ◦Γ∗ σ) −
k

Further, if ρ is a probability measure having a density function
f (λ) and each
R
λ corresponds to a quantum coded state σ(λ), then σ = f (λ) σ(λ)dλ and
Z

 ∼∗
∼∗
∼∗
∗
∗
∗
I ρ; Ξ ◦ Γ ◦ Ξ = S(Ξ ◦Γ σ) − f (λ)S(Ξ ◦Γ∗ σ(λ))dλ,

(4.9)

which is less than

∗

S(Γ σ) −

Z

f (λ)S(Γ∗ σ(λ))dλ.

The above bound is called Holevo bound, and it is computed in several
cases[29, 36].
P0
satisfy the following inequalities
The above three capacities C P0 , CcP0 , Ccd


∼∗
∼∗
P0
( Γ∗ ) ≤ sup {S(ρ); ρ ∈ Po }
0 ≤ C P0 Ξ ◦ Γ∗ ◦ Ξ∗ ≤ CcP0 Ξ ◦ Γ∗ ≤ Ccd

where S(ρ) is not the von Neumann entropy but the Shannon entropy: P
λk log λk .
The capacities (4.1), (4.6),(4.7) and (4.8) are generally different. Some
misunderstandings occur due to forgetting which channel is considered. That
is, we have to make clear what kind of the ability, the capacity of a quantum
channel itself or that of a classical-quantum(-classical ) channel or that of a
coding free, is considered.

10

References
[1] L. Accardi, M. Ohya and H .Suyari, Computation of Mutual Entropy in
Quantum Markov Chains, Open Systems and Information Dynamics, 2,
No.3, 337-354, 1994.
[2] S. Akashi, The asymptotic behavior of ε-entropy of a compact positive
operator, J.Math.Anal.Appl., 153, 250-257, 1990.
[3] H. Araki, Relative entropy for states of von Neumann algebras, Publ.
RIMS Kyoto Univ., 11, 809–833, 1976.
[4] V.P. Belavkin, Conditional entropy and capacity of quantum channels,
in Proc. of VIII-th Conference on Coding Theory and Information Transmission, 15-19, Moscow-Kuibishev, 1982.
[5] V.P. Belavkin and P.L. Stratonovich,Optimization of processing of quantum signals according to an information Criterion, Radio Eng. Electron.
Phys., 18, 9, 1839-1844, 1973.
[6] P. Billingsley, “Ergodic Theory and Information”, Wiley, NY.,1965.
[7] I.M. Gelfand and A.M. Yaglom, Calculation of the amount of information about a random function contained in another such function, Amer.
Math. Soc. Transl., 12, 199-246, 1959.
[8] A.S. Holevo, Some estimates for the amount of information transmittable by a quantum communication channel (in Russian), Problemy
Peredachi Informacii, 9, 3-11, 1973
[9] R.S.Ingarden, Quantum information theory, Rep. Math. Phys., 10, 4373, 1976.
[10] R.S. Ingarden, A. Kossakowski and M.Ohya, “Information Dynamics
and Open Systems”, Kluwer Academic Publishers, 1997.
[11] K. Inoue, M. Ohya and H. Suyari, Characterization of quantum teleportation processes by nonlinear quantum channel and quantum mutual
entropy, to appear in Physica D.
[12] A.N. Kolmogorov, Theory of transmission of information, Amer. Math.
Soc. Translation, Ser.2, 33, 291–321, 1963.
11

[13] S. Kullback and R. Leibler, On information and sufficiency, Ann. Math.
Stat., 22, 79–86, 1951.
[14] L.B. Levitin, Physical information theory for 30 years: basic concepts
and results, Springer Lect. Note in Phys., 378, 101-110, 1991.
[15] G. Lindblad, Entropy, information and quantum measurements, Commun. Math. Phys., 33, 111-119, 1973.
[16] T. Matsuoka and M. Ohya, Fractal dimensions of states and its application to Ising model, Rep. Math. Phys., 36, 365–379, 1995.
[17] N. Muraki, M. Ohya and D. Petz, Note on entropy of general quantum
systems, Open Systems and Information Dynamics, 1, No.1, 43–56,
1992.
[18] N. Muraki and M. Ohya, Entropy functionals of Kolmogorov Sinai type
and their limit theorems, Letters in Mathematical Physics, 36, 327-375,
1996.
[19] J.von Neumann, “Die Mathematischen Grundlagen der Quantenmechanik”, Springer-Berlin, 1932.
[20] M. Ohya, Quantum ergodic channels in operator algebras, J. Math.
Anal. Appl. 84, 318-327, 1981.
[21] M. Ohya, On compound state and mutual information in quantum information theory, IEEE Trans. Information Theory, 29, 770-777, 1983.
[22] M. Ohya, Note on quantum probability, L. Nuovo Cimento, 38, 402–406,
1983.
[23] M. Ohya, Some aspects of quantum information theory and their applications to irreversible processes, Rep. Math. Phys., 27, 19–47, 1989.
[24] M. Ohya, Fractal dimensions of states, Quantum Probability and Related Topics, 6, World Scientific, Singapore, 1991.
[25] M. Ohya, State change, complexity and fractal in quantum systems,
Quantum Communications and Measurement, 309–320, 1995.

12

[26] M. Ohya, Complexity and fractal dimensions for quantum states, Open
Systems and Information Dynamics, 4, No.1, 141-157.
[27] M. Ohya, Complexities and their applications to characterization of
chaos, International J. Theor. Phys, 37, No.1, 495-506.
[28] M. Ohya and D. Petz, “Quantum Entropy and Its Use”, Springer, 1993.
[29] M. Ohya, D. Petz and N. Watanabe, On capacities of quantum channels,
Probability and Mathematical Statistics, 17, 179-196, 1997.
[30] M. Ohya, D. Petz and N. Watanabe, Numerical computation of quantum
capacity, International J. Theor. Phys., 37, No.1, 507-510.
[31] M. Ohya and N. Watanabe, On mathematical treatment of FredkinToffoli-Milburn gate, to appear in Physica D.
[32] C.E. Shannon, Mathematical theory of communication, Bell System
Tech. J. 27, 379–423, 1948.
[33] R. Schatten, “Norm Ideals of Completely Continuous Operators”,
Springer-Verlag, 1970.
[34] A. Uhlmann, Relative entropy and the Wigner-Yanase-Dyson-Lieb concavity in interpolation theory, Commun. Math. Phys., 54, 21–32, 1977.
[35] H. Umegaki, Conditional expectations in an operator algebra IV (entropy and information), Kodai Math. Sem. Rep., 14, 59–85, 1962.
[36] H.P. Yuen and M. Ozawa, Ultimate information carrying limit of qunatum systems, Phys. Rev. Lett., 70, 363-366, 1993.

13

