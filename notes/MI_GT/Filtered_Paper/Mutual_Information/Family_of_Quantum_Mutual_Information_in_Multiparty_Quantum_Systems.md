Family of Quantum Mutual Information in Multiparty Quantum Systems
Asutosh Kumar∗

arXiv:2407.16365v3 [quant-ph] 2 Sep 2024

Department of Physics, Gaya College, Rampur, Gaya 823001, India and
P.G. Department of Physics, Magadh University, Bodh Gaya 824234, India
The characterization of information within a multiparty system is both significant and complex.
This paper presents the concept of generalized conditional mutual information, along with a family of multiparty quantum mutual information measures. We provide interpretations and delineate
the properties of these concepts, while also pointing out certain unresolved issues. The generalized
conditional mutual information serves to encapsulate the interdependencies and correlations among
various components of a multiparty quantum system. Additionally, various formulations of multiparty quantum mutual information contribute to a deeper comprehension of classical, quantum,
and total correlations. These insights have the potential to propel fundamental research in the field
of quantum information theory.

I.

INTRODUCTION

In our information-driven universe, information is the
cornerstone of communication, computation, and knowledge. Shannon in 1948 introduced the concept of mutual
information which provided a framework for quantifying the amount of information shared between two systems, revolutionizing classical information theory. Classical mutual information I(X : Y ) = H(X) + H(Y ) −
H(X, Y ), where H(X) is the Shannon entropy, measures
the amount of information obtained about one random
variable through another random variable. It quantifies
the reduction in uncertainty about one variable given
knowledge of the other. In classical information theory [1], mutual information has diverse applications in
data compression, error correction, and channel capacity,
making it a fundamental tool in communication systems
and coding theory.
This concept has now transcended into the quantum
domain, playing a crucial role in quantum information
theory [2–4] in particular. Quantum mutual information
(QMI) is a generalization of classical mutual information
to quantum systems. The QMI of a bipartite quantum
state ρAB given by I(A : B) = S(ρA ) + S(ρB ) − S(ρAB ),
where S(ρ) is the von Neumann entropy, quantifies the
total correlation [5, 6], both classical and quantum, between subsystems A and B. It serves as a measure of correlation beyond entanglement. QMI is essential in multiple areas of quantum information processing like quantum communication, quantum computing, and quantum
cryptography [2–4]. It is especially important in quantifying quantum channel capacities [7, 8]. In quantum
machine learning [9, 10], it quantifies the information
exchanged between various representations of quantum
datasets. It is also significant as a probe for many-body
localization [11], and in quantifying quantum objectivity
[12].
Understanding various correlations [13–16] in systems
involving more than two parties becomes increasingly im-

∗ asutoshk.phys@gmail.com

portant. In classical information theory, mutual information between multiple random variables can be straightforwardly extended. In the quantum realm, however,
correlations are more complex due to the exotic quantum phenomena such as nonlocality, superposition and
measurement problem. Multiparty quantum mutual information (MQMI) extends the concept of bipartite QMI
to systems with multiple parties, offering insights into
the intricate correlations that arise in quantum states.
It seeks to quantify the total correlations among several
subsystems within a quantum state, and has implications
for understanding and leveraging the correlations in multiparty quantum systems. Mutual information and related measures [5, 6, 17–23] are famed measures of multipartite information and correlation. The journey of
mutual information from classical to quantum domains
underscores its profound elegance and significance. As
quantum technologies continue to advance, the significance of mutual information in both the realms becomes
increasingly evident. The two main contributions of this
paper are:
1. Concept of generalized conditional mutual information which is an extension of the conditional entropy
S(A|B) = S(ρAB ) − S(ρB ) and conditional mutual information I(A : B|C) = S(ρAC ) + S(ρBC ) − S(ρC ) −
S(ρABC ). This quantity can encapsulate every possible
interdependency and correlation of any subsystem of a
multiparty system.
2. Introduction of a family of multiparty quantum mutual information. There are at least n − 1 MQMI for an
n (≥ 2)-party quantum system. Moreover, any positive
linear combination of these MQMIs is another MQMI.
Some linear combinations of these MQMIs can yield negative values.
It is evident that multiple expressions of MQMI arise
due to different ways of defining and quantifying correlations in complex quantum systems. Each expression
may capture unique aspects of these correlations, leading
to diverse applications and insights. A straightforward
consequence of multiple expressions of MQMI would be
enhanced understanding of classical, quantum and total
correlations. By providing a multifaceted understanding
of correlations in multiparty quantum systems, multiple

2
expressions of MQMI can drive fundamental research in
quantum information theory. By providing different perspectives on correlations and their operational interpretations, we can explore new theoretical models and deepen
our understanding of quantum systems.
This paper is organised as follows. In Sec. II, we consider the preliminaries such as notation and definitions.
The notion of generalized conditional mutual information
which is the generalization of conditional entropy and
conditional mutual information to multiparty systems is
introduced in Sec. III. In Sec. IV, we introduce a family
of multiparty quantum mutual information and provide
their interpretations and properties. We also speculate
them to be secrecy monotones which are useful in cryptography. Finally, we conclude and discuss some unresolved issues in Sec. V.

II.
A.

SETUP

Preliminaries

We consider a multiparty quantum system
X1 X2 · · · Xn represented by finite dimensional density matrix ρX1 X2 ···Xn ∈ H1d1 ⊗ H2d2 ⊗ · · · ⊗ Hndn . The
reduced density matrix of subsystem X is obtained
by partial tracing over the remaining subsystems X:
ρX = trX (ρXX ). The von Neumann entropy (in bits)
given by
S(ρ) := −tr(ρ log2 ρ) = −

X

λi log2 λi ,

(1)

i

P
where λi ≥ 0 and i λi = 1, is the quantum counterpart of Shannon entropy. Shannon entropy is the average
information content of a probability distribution. The
von Neumann entropy satisfies the inequalities [24, 25]:
S(ρX ) − S(ρY ) ≤ S(ρXY ) ≤ S(ρX ) + S(ρY ) ≤ S(ρXZ ) +
S(ρY Z ) and S(ρY ) + S(ρXY Z ) ≤ S(ρXY ) + S(ρY Z ). We
denote the von Neumann entropy of subsystem Xi Xj as
S(ρXi Xj ) ≡ S(Xi Xj ) ≡ Sij , and so on. S(ρ) = 0 for a
pure quantum state. Another important entropy for our
purpose is quantum relative entropy (QRE) which measures the closeness of two density matrices. It is defined
as
D(τ ||σ) := tr(τ log2 τ ) − tr(τ log2 σ),

(2)

if supp(τ ) ⊆ supp(σ), and infinity otherwise. The support
of a Hermitian matrix is the Hilbert space spanned by
its eigenvectors with nonzero eigenvalues [2]. The QRE
is monotonic under partial trace, completely-positive
and trace-preserving (CPTP) maps, and positive maps
[25, 26]. Let X = {X1 , X2 , · · · , Xn }, [n] = {1, 2, · · · , n},
and 1 = 1 such that S(1) = 0 and for any system X,
ρX 1 = ρX = 1ρX . [One can alternatively consider
1 = diag{1, 1, · · · , 1} with the requirement that its dimension is self-adjusting!]

B.

Correlations and Monotones

Let us consider a function f (ρX1 ···Xn ) defined on
ρX1 ···Xn and mention below some plausible and useful
properties.
(P1) Symmetry: f (ρX1 ···Xn ) is symmetric under the interchange of any two parties Xj and Xk .
(P2) Semipositivity: f (ρX1 ···Xn ) ≥ 0.
(P3) Vanishing on product states: f (ρX1 ⊗· · ·⊗ρXn ) = 0.
(P4) Monotonicity under some local operations [local
(completely) positive maps].
(P5) Monotonicity under classical communications (public announcement or communication over phone).
(P6) Additivity: f (ρ ⊗ σ) = f (ρ) + f (σ) and f (ρ⊗n ) =
nf (ρ).
(P7) Continuity: f (ρ) is a continuous (smooth) function
of its argument ρ.
If f satisfies (P2) semipositivity and (P3) vanishing on
product density matrices, it is a measure of the amount of
correlation between the parties. A nonnegative correlation function that observes (P4) monotonicity under local
operations and (P5) monotonicity under classical communications is called a monotone. A secrecy monotone,
in addition to (P2–P5), satisfies (P6) additivity and (P7)
continuity. If the secrecy monotone is expected to measure the amount of information (secrecy) shared by the
communicating parties {X1 , X2 , · · · , Xn } with the hostile party Eve, then the following properties are natural
[27, 28]:
(P8) Monotonicity under local operations by Eve.
(P9) Monotonicity under classical (public) communication by Eve.
Whether the information in question is correlation,
monotone or secrecy monotone should be clear from its
properties and the context.

III.

GENERALIZED CONDITIONAL MUTUAL
INFORMATION

In this section, we introduce the notion of generalized conditional mutual information (GCMI). It is the
multiparty extension of conditional entropy S(A|B) =
S(AB) − S(B) and conditional mutual information I(A :
B|C) = S(AC) + S(BC) − S(C) − S(ABC). It can encompass every possible interdependency or correlation
(interaction information) of any subsystem of a multiparty system. We define the GCMI as the information
contained in subsystems Xk1 Xk2 · · · Xkm of a multiparty
system X1 X2 · · · Xn (n ≥ m) but not in Y , where Y
(acting as a single system) is either 1 or one or more
remaining subsystems,
I(Xk1 : Xk2 : · · · : Xkm |Y ) := −S(Y )
m
X
X
+
(−1)j+1
S(Xk1 Xk2 · · · Xkj Y ).
j=1

k1 <···<kj ∈[m]

(3)

3
A few remarkable points about I(Xk1 : Xk2 : · · · :
Xkm |Y ) are as follows.
1. I(Xk1 : Xk2 |Y ) ≥ 0. This follows from the strong
subadditivity of von Neumann entropy.
2. I(Xk1 Xk2 · · · Xkm |1) = S(Xk1 Xk2 · · · Xkm ).
3. I(X1 : X2 : · · · : Xn |1) is the information (correlation)
common to subsystems X1 , X2 , · · · , and Xn .
4. It can assume negative values [29–33].
In the above, I(X|1) ≡ I(X), I(X1 : X2 : X3 |1) ≡
I(X1 : X2 : X3 ), and so on. In multiparty systems, however, we prefer to keep the notation I(X|1) rather than
I(X) to remind us the fact that either I(X) ≡ I(X|1) =
−S(1) + S(X) is analogous to conditional information or
I(X) is not a multiparty (total) correlation.
The nontriviality in characterization of information
and correlations begins to emerge with three-party system onwards. We illustrate the idea of GCMI using
the tripartite system ABC represented by density matrix ρABC [see Fig. 1(b)].
1. Information in A is [a + ab + ac + abc] = S(ρA ) ≡
I(A|1).
2. Information in A but neither in B nor in C (i.e., information strictly contained in A) is [a] = −S(ρBC ) +
S(ρABC ) ≡ I(A|BC).
3. Information in A (and possibly in B) but not in C is
[a + ab] = −S(ρC ) + S(ρAC ) ≡ I(A|C).
4. Information common to A and B (and possibly in C)
is [ab + abc] = S(ρA ) + S(ρB ) − S(ρAB ) ≡ I(A : B|1).
5. Information common to A and B but not in C is [ab] =
−S(ρC ) + S(ρAC ) + S(ρBC ) − S(ρABC ) ≡ I(A : B|C).
6. Information common to A, B and C is [abc] = S(ρA )+
S(ρB )+S(ρC )−S(ρAB )−S(ρAC )−S(ρBC )+S(ρABC ) ≡
I(A : B : C|1).
7. Information in ABC (as a single system) is S(ρABC ) ≡
I(ABC|1).
Indeed, there are several possibilities. Different arrangements or configurations of subsystems yield, in general,
different values of information or correlation.
8. Three-party total correlations amongst A, B and C
are given by

A
a

A

I(A|BC)

B
ab
I(A:B|C)

a
I(A|B)

ab
I(A:B)

b
I(B|A)

b
I(B|AC)

ac
I(A:C|B)
abc
I(A:B:C)
bc
I(B:C|A)

C

B

(a)

c
I(C|AB)

(b)

FIG. 1. (a) Two-variable and (b) three-variable Venn diagrams with possible intersecting regions and generalized conditional mutual information. Here S(X) ≡ I(X|1) is the information content of subsystem X, the information contained
in subsystem X but not in subsystem Y is given by the conditional entropy S(X|Y ) = S(XY ) − S(Y ) = S(X) − I(X :
Y ) ≡ I(X|Y ), and I(X : Y ) is the information between X
and Y .

IV.

FAMILY OF MQMI

The bipartite QMI I(A : B) = S(A) + S(B) − S(AB)
is the measure of total correlation (classical and quantum) between subsystems A and B [5, 6], satisfies the
Araki-Lieb inequality I(A : B) ≤ 2 min{S(ρA ), S(ρB )}
[24], is invariant under local unitary operations, and is
nonincreasing under tracing out a subsystem. Here we
introduce a family of entropic functions constructed on
ρX1 ···Xn , and show below that they serve as n-party quantum mutual information.

A.

Definition

We define the k th (1 ≤ k ≤ n) multiparty quantum
mutual information on ρX1 ···Xn as
(n)

Mk (X1 : X2 : · · · : Xn )


X
n−1
:=
S(Xj1 · · · Xjk ) −
S(X1 · · · Xn ).
k−1

T3 (A : B : C) = S(ρA ) + S(ρB ) + S(ρC ) − S(ρABC )
j1 <···<jk ∈[n]
=D(ρABC ∥ ρA ⊗ ρB ⊗ ρC )
(4)
=I(A : BC) + I(B : C)
=I(A : B|C) + I(A : C|B) + I(B : C|A) + 2I(A : B : C|1), The superscript “n” in M (n) denotes the number of subk
systems (single or composite)
separated by colons, and

n−1
the
coefficients
for
given
n constitute the nth -row
and
k−1
of the Pascal’s triangle. We posit a few remarks here.
First, the choice of definition in Eq.(4) is motivated by
S3 (A : B : C) = S(ρAB ) + S(ρAC ) + S(ρBC ) − 2S(ρABC ) the fact that the two well-established MQMI [22, 27] in
=I(A : BC) + I(B : C|A)
the literature are members of this family. Second, this
multiparty quantum mutual information contains all two
=I(A : B|C) + I(A : C|B) + I(B : C|A) + I(A : B : C|1)
and more parties interactions, as described in [22], and
=S(ρABC ) − I(A|BC) − I(B|AC) − I(C|AB).
not just the n-party interaction I(X1 : X2 : · · · : Xn |1).
(2)
Third, M1 (X : Y ) = I(X : Y ) = I(X : Y |1).
For p + q = n, one can consider p-party versus q-party

4
partitions of X such that

MQMIs [22, 27] are:
(n)

Mp(n) + Mq(n) =

X



I ρk : ρk .(5)

kk∈{p|q partitions of X }

Tn (X1 : X2 : · · · : Xn ) ≡ M1 (X1 : X2 : · · · : Xn )
n
X
=
S(ρXk ) − S(ρX1 ···Xn )
(7)
k=1

=D(ρX1 ···Xn ∥ ρX1 ⊗ · · · ⊗ ρXn )
(n)

See Appendix A for more relations between Mk .

=

The existence of several expressions for multiparty
quantum mutual information can have profound consequences and diverse applications in quantum information
theory and technology. As research in this area continues
to evolve, the insights gained from multiple MQMI measures will be instrumental in unlocking the full potential
of quantum information science. The following observations, for instance, merit attention.
(n)
1. Mk are independent multiparty quantum mutual information. As these yield distinct values for an arbitrary
state, the parties must make a priori choice about which
multiparty correlation they want to consider. This a priori choice should be obvious (self-revealing) once their
interpretations are known.
2. To maximize their correlation, parties should con(n)
sider the quantity Mk where k = n/2 (for even n) or
(n)
k = (n ± 1)/2 (for odd n). For minimal correlation, M1
(n)
and Mn−1 are good candidates.
3. Corresponding to this family of multiparty quantum
mutual information, one can introduce a family of multiparty quantum discord. Discord is the difference between
unmeasured total correlation and measured total correlation present in a quantum state.
4. Information deviation due to a map or channel Φ (this
may include noise) acting on a multiparty quantum state
(n)
ρ is |Q(Φ(ρ)) − Q(ρ)|, where Q is either Mk , M (n) ,
C (n) , or generalized conditional mutual information.
5. Suppose the eavesdropper E interacts with the system
ρAB . Then, the desirable condition for the secure secret
sharing of information between A and B is that the sum
of correlations of E with A and B should be minimal
(refer to Fig. 1(b) with E in place of C). That is,

=

n−1
X

(8)

I(Xk : Xk+1 · · · Xn )

k=1
n
X

X

j=2

k1 <···kj ∈[n]

(j − 1)

(9)

I(Xk1 : · · · : Xkj |Xkj+1 · · · Xkn ),
(10)

and
(n)

Sn (X1 : X2 : · · · : Xn ) ≡ Mn−1 (X1 : X2 : · · · : Xn )
n
X
=
S(ρX1 ···Xk−1 Xk+1 ···Xn ) − (n − 1)S(ρX1 ···Xn ) (11)
k=1

=I(X1 : X2 · · · Xn ) +

n−1
X

I(Xk : Xk+1 · · · Xn |X1 · · · Xk−1 )

k=2

(12)
=

n
X

X

I(Xk1 : · · · : Xkj |Xkj+1 · · · Xkn ) (13)

j=2 k1 <···kj ∈[n]

=S(ρX1 ···Xn ) −

n
X

I(Xk |Xk ).

(14)

k=1

Both Tn and Sn measure both the classical and the
quantum correlations. Tn and Sn are referred to as
“total correlation” [5, 17] and “dual total correlation”
[18, 19] respectively, quantum secrecy monotones [27],
and multiparty quantum mutual information [22] from
the information-theoretic point of view.
(n)
We further find that Mk , for fixed k (1 ≤ k < n),
is nondecreasing under discarding of any one party or
grouping together any two parties (see Appendix B).
That is,
(n)

(n−1)

Mk (X1 : · · · : Xn ) ≥ Mk

(X1 : · · · : Xn−1 ),

I(A : E|B) + I(B : E|A) + I(A : B : E)

(16)

(3)

=M2 (A : B : E) − I(A : B|E)
=I(AB : E) → 0.

(15)

(n)
(n−1)
Mk (X1 : · · · : Xn ) ≥ Mk
(X1 : · · · : Xn−1 Xn ).

(6)
B.

A more stringent condition would be that each of I(A :
E|B), I(B : E|A), and I(A : B : E) is either zero or
tends to zero.
P
(n)
(n)
6. Mk together with k ck Mk can be used to distinguish quantum states.
The various equivalent expressions of two eminent

Interpretations
(n)

Interpretations of Tn = M1 .– From Eq.(8), Tn
is interpreted as the minimal relative entropy between
ρX1 ···Xn and a product density matrix σX1 ⊗ · · · ⊗ σXn
(the minimum being attained when σXk = ρXk ). From
Eq.(9), Tn is the sum of decorrelation costs when the parties decorrelate themselves locally one by one from the
rest using I(Xk : Xk+1 · · · Xn ) bits of randomness [5].

5
From Eq.(10), Tn is the sum of (j − 1)-times all (j ≥ 2)party interactions.
(n)
Interpretations of Sn = Mn−1 .– Sn like Tn , from
Eq.(12), can be interpreted as the sum of decorrelation costs when the parties decorrelate themselves
locally one by one from the rest using I(Xk :
Xk+1 · · · Xn |X1 · · · Xk−1 ) bits of randomness. Sn , using
Eq.(13), is the sum of all interactions of two and more
parties only once [22]. Equivalently, from Eq.(14), it is
the entropy of the whole system less the sum of information in nonintersecting regions.
(n)
Nevertheless, while all Mk can be viewed as the sum
of two and more parties interactions, not all of them
have straightforward physical or operational meaning like
(n)
(n)
M1 and Mn−1 . Therefore, any operational interpretation of these mutual information would be appreciated.
(n)

(n)

(n)

M (n) (X1 : X2 : · · · : Xn )
n
X
(n)
=
λk Mk (X1 : X2 : · · · : Xn ),

TABLE I. Values of multiparty quantum mutual in(n)
formation Mk
and common information C (n) of generalized Greenberger-Horne-Zeilinger
states |gGHZn ⟩ =
√
√
p |0⟩⊗n + eiϕ 1 − p |1⟩⊗n , Dicke states |Dnr ⟩ =
P
q1
P[|0⟩⊗n−r |1⟩⊗r ], three-qutrit totally antisymmetric
(nr) P
state |ψas ⟩ = √16 (|123⟩ − |132⟩ + |231⟩ − |213⟩ + |312⟩ − |321⟩),
four-qubit cluster state |C4 ⟩ = 12 (|0000⟩ + |0011⟩ + |1100⟩ −
|1111⟩), and |HS4 ⟩ = √16 (|0011⟩+|1100⟩+ω(|1010⟩+|0101⟩)+
ω 2 (|1001⟩+|0110⟩)). Here h(p) := −p log2 p−(1−p) log2 (1−p)
2πi
is the binary entropy, ω = e 3 , and “×” stands for not appli(n)
cable. Note that C
can be negative and C (n=odd) vanishes
for pure states.

Properties

P
where λk ≥ 0 and
k λk = 1. We conjecture below
(n)
(n)
that Mk and M
are plausible candiadtes for secrecy
monotones. Another important linear combination of
(n)
Mk is
C (n) (X1 : X2 : · · · : Xn )
n
X
(n)
=
(−1)k+1 Mk (X1 : X2 : · · · : Xn ),

(18)

k=1

=I(X1 : X2 : · · · : Xn |1).
C (n) is the information (correlation) common to all Xk s.
It can, however, be negative (see Table I). Moreover, it
vanishes identically for pure odd-party quantum states:
X
X
(n)
(n)
C (n=odd) =
Mk −
Mk = 0.
(19)
k=odd

k=even
(n)

(n)

6. For pure states, C (n) ≤ Mk = Mn−k . For mixed
states, we expect them to obey the inequality:


(n)
(n)
C (n) ≤ M1 ≈ Mn−1


(n)
(n)
(n)
< M2 ≈ Mn−2 < · · · < Mn/2 .
(20)
We also surmise that for k1 < k2 ≤ n/2 and c ≥ ck2 ,k1 =
k2 (kn )
2
,
k1 (kn )
1
(n)

Here we discuss a number of useful properties that
(n)
Mk satisfy.
(n)
1. Mk is invariant under local unitary operations because von Neumann entropy is invariant under unitary
operations.
(n)
(n)
2. M1 = Tn and Mn−1 = Sn satisfy the following properties [22, 27]: (P1–P9) above, (P10) Sn = Tn for pure
states, and (P11) Sn (ρX1 X2 ···Xn ) ≤ Tn (ρX1 X2 ···Xn ) +
2S(ρX1 X2 ···Xn ).

(17)

k=1

(n)

State
M1
M2
M3
M4
C (n)
|gGHZ2 ⟩ 2 h(p)
0
×
×
2 h(p)
|gGHZ3 ⟩ 3 h(p) 3 h(p)
0
×
0
|D31 ⟩ 2.75489 2.75489
0
×
0
|ψas ⟩ 4.75489 4.75489
0
×
0
|gGHZ4 ⟩ 4 h(p) 6 h(p)
4 h(p)
0
2 h(p)
|D41 ⟩ 3.24511
6
3.24511
0
0.490225
|D42 ⟩
4
7.50978
4
0
0.490225
|C4 ⟩
4
10
4
0
-2
|HS4 ⟩
4
10.75489
4
0
-2.75489
|gGHZ5 ⟩ 5 h(p) 10 h(p) 10 h(p) 5 h(p)
0
|D51 ⟩ 3.60964 9.70951 9.70951 3.60964
0
|D52 ⟩ 4.85475 12.95462 12.95462 4.85475
0

C.

(n)

3. Mn = 0 (as expected) because (X1 X2 · · · Xn ) as a
single system has no mutual information.
4. Suppose 1 ≤ p, q ≤ n−1 such that p ̸= q and p+q = n.
(n)
(n)
Then Mp = Mq for pure states and hence can be
called “dual” to each other. We envisage from Table I
(n)
that for pure states the profile of Mk versus k is analogous to a truncated Gaussian (a point or a straight line
being the particular case).
(n)
5. Mk satisfy (P1) symmetry, (P3) vanishing on product states, (P6) additivity and (P7) continuity. These
properties are also satisfied by any quantity which is a
(n)
linear combination of Mk . In particular,

(n)

cMk1 ≥ Mk2 .
(n)

(21)

7. Mk (X1 : X2 : · · · : Xn ) in Eq.(4) is semipositive.
Proof.
It is obvious for pure states because
S(X1 X2 · · · Xn ) vanishes identically. For mixed states,
(n)
(n)
(n)
the semipositivity of M1 , Mn−1 , and Mk=n/2 (for even
n) follows from Eqs.(8, 9), Eq.(12), and Eq.(5) respec(n)
tively. In general, Mk is semipositive because it is
(n)
nondecreasing under discarding a subsystem: Mk ≥

6
(n−1)

(k)

(n)

Mk
≥ · · · ≥ Mk = 0 [see Eq.(15)]. Mk can
also be shown nonnegative using the subadditivity and
the strong subadditivity of von Neumann entropy (see
Appendix C). The idea is to eliminate S(X1 X2 · · · Xn )
terms. This can be achieved by grouping together (repeatedly) two appropriate entropy terms of small number of parties to obtain an entropy term having greater
number of parties. One should, however, take care that
while grouping no entropy term, except S(X1 X2 · · · Xn ),
appears twice or more.
■
(n)
Thus, Mk in Eq.(4) and M (n) in Eq.(17) satisfy a
number of useful properties: symmetry, semipositivity,
vanishing on product states, additivity, and continuity.
Hence, they constitute a family of multiparty quantum
mutual information.

D.

Conjecture and Remark

Secrecy monotones quantify the amount of secret correlation shared by the parties of a multipartite system.
They are useful in the study of quantum (as well as clas(n)
(n)
sical) cryptography. M1 = Tn and Mn−1 = Sn satisfy
properties (P4, P5) and (P8, P9), and qualify for secrecy
monotones [27]. We speculate (see Appendix D for argu(n)
ment) that Mk (k = 2, 3, · · · , n−2) in Eq.(4) and M (n)
in Eq.(17) also meet the criteria (P4, P5) and (P8, P9)
for being considered as measures of secrecy monotone.
In addition to these n-party symmetric monotones, we
(m)
also have other monotones Mk
(1 ≤ k ≤ m < n) on
n-party quantum states ρX1 ···Xn which can be obtained

[1] T. Cover and J. Thomas, Elements of Information Theory (John Wiley & Sons, 1991).
[2] M. A. Nielsen and I. L. Chuang, Quantum Computation
and Quantum Information (Cambridge University Press,
2000).
[3] M. M. Wilde, Quantum Information Theory (Cambridge
University Press, 2013).
[4] J. Preskill, Lecture Notes for Physics 229: Quantum Information and Computation (CreateSpace Independent
Publishing Platform, 2015).
[5] B. Groisman, S. Popescu, and A. Winter, Quantum,
classical, and total amount of correlations in a quantum
state, Phys. Rev. A 72, 032317 (2005).
[6] N. Li and S. Luo, Total versus quantum corrrelations in
quantum states, Phys. Rev. A 76, 032327 (2007).
[7] C. H. Bennett and P. W. Shor, Quantum Channel Capacities, Science 303, 1784-1787 (2004).
[8] A. S. Holevo, Quantum channel capacities, Quantum
Electron. 50, 440 (2020).
[9] J. Biamonte, P. Wittek, N. Pancotti, P. Rebentrost, N.
Wiebe, and S. Lloyd, Quantum machine learning, Nature
549, 195-202 (2017).
[10] G. Carleo, I. Cirac, K. Cranmer, L. Daudet, M. Schuld,
N. Tishby, L. Vogt-Maranto, and L. Zdeborová, Machine
learning and the physical sciences, Rev. Mod. Phys. 91,

by grouping together any two or more of the n-parties.
All these monotones, however, are not all linearly independent.

V.

CONCLUSIONS

In this study, we have conducted a comprehensive analysis of entropy-based information within multiparty systems. Firstly, we introduced the concept of generalized
conditional mutual information. Next, we presented a
family of multiparty quantum mutual information, which
is anticipated to significantly contribute to fundamental research in quantum information theory. This advancement is expected to enhance our comprehension
of classical, quantum, and total correlations, and consequences thereof. Notably, this framework includes the
two well-established multiparty quantum mutual information measures.
(n)
(n)
While various interpretations exist for M1 and Mn−1 ,
(n)
the interpretation of other measures Mk remains unclear. Therefore, some operational interpretations of
these mutual information measures would be beneficial. Additionally, we conjecture that the remaining
P
(n)
(n)
(n)
measures
=
k λk Mk , where λk ≥
P Mk and M
0 and
k λk = 1, will exhibit monotonicity under local
operations and classical communication, thereby qualifying as secrecy monotones. We also posit that our formalism will be instrumental in characterizing measures
of multiparty nonclassical correlations.

045002 (2019).
[11] G. D. Tomasi, S. Bera, J. H. Bardarson, and F. Pollmann,
Quantum Mutual Information as a Probe for Many-Body
Localization, Phys. Rev. Lett. 118, 016804 (2017).
[12] D. A. Chisholm, L. Innocenti, and G. M. Palma, Importance of using the averaged mutual information when
quantifying quantum objectivity, Phys. Rev. A 110,
012218 (2024).
[13] I. Bengtsson and K. Życzkowski, Geometry of Quantum States: An Introduction to Quantum Entanglement
(Cambridge University Press, 2006).
[14] R. Horodecki, P. Horodecki, M. Horodecki, and K.
Horodecki, Quantum entanglement, Rev. Mod. Phys. 81,
865 (2009).
[15] K. Modi, A. Brodutch, H. Cable, T. Paterek, and V.
Vedral, The classical-quantum boundary for correlations:
Discord and related measures, Rev. Mod. Phys. 84, 1655
(2012).
[16] A. Bera, T. Das, D. Sadhukhan, S. S. Roy, A. Sen(De),
and U. Sen, Quantum discord and its allies: a review of
recent progress, Rep. Prog. Phys. 81, 024001 (2018).
[17] S. Watanabe, Information theoretical analysis of multivariate correlation, IBM Journal of Research and Development 4(1), 66-81 (1960).

7
[18] T. S. Han, Linear dependence structure of the entropy
space, Inform. Contr. 29, 337-368 (1975).
[19] T. S. Han, Nonnegative Entropy Measures of Multivariate Symmetric Correlations, Inform. Contr. 36, 133-156
(1978).
[20] Z. Walczak, Total correlations and mutual information,
Phys. Lett. A 373, 1818-1822 (2009).
[21] G. L. Giorgi, B. Bellomo, F. Galve, and R. Zambrini,
Genuine quantum and classical correlations in multipartite systems, Phys. Rev. Lett. 107, 190501 (2011).
[22] A. Kumar, Multiparty quantum mutual information: An
alternative definition, Phys. Rev. A 96, 012332 (2017).
[23] Sk Sazim and P. Agrawal, Quantum mutual information
and quantumness vectors for multiqubit systems, Quantum Inf. Process. 19, 216 (2020).
[24] A. Wehrl, General properties of entropy, Rev. Mod. Phys.
50, 221 (1978).
[25] M. B. Ruskai, Inequalities for quantum entropy: A review
with conditions for equality, J. Math. Phys. 43, 4358-4375
(2002).
[26] A. M̈uller-Hermes and D. Reeb, Monotonicity of the
Quantum Relative Entropy Under Positive Maps, Ann.

Henri Poincaré 18, 1777-1788 (2017).
[27] N. J. Cerf, S. Massar, and S. Schneider, Multipartite classical and quantum secrecy monotones, Phys. Rev. A 66,
042309 (2002).
[28] M. Horodecki, P. Horodecki, and R. Horodecki, Limits
for Entanglement Measures, Phys. Rev. Lett. 84, 2014
(2000).
[29] N. J. Cerf and C. Adami, Negative entropy and information in quantum mechanics, Phys. Rev. Lett. 79, 51945197 (1997).
[30] M. Horodecki, J. Oppenheim, and A. Winter, Partial
quantum information, Nature 436, 673-676 (2005).
[31] M. Horodecki, J. Oppenheim, and A. Winter, Quantum State Merging and Negative Information, Commun.
Math. Phys. 269, 107-136 (2007).
[32] L. del Rio, J. Aberg, R. Renner, O. Dahlsten, and V.
Vedral, The thermodynamic meaning of negative entropy,
Nature 474, 61-63 (2011).
[33] G. Gour, M. M. Wilde, S. Brandsen, and I. J. Geng, Inevitability of knowing less than nothing, arXiv:2208.14424
[quant-ph].

(n)

Appendix A: Relations between Mk

1. The recurrence relation(s) for Tn and Sn are as follows:
Tn (X1 : X2 : · · · : Xn ) = Tn−1 (Xk1 : Xk2 : · · · : Xkn−1 ) + I(Xk1 · · · Xkn−1 : Xkn ),
Tn (X1 : X2 : · · · : Xn ) = Tn−1 (Xk1 Xk2 : Xk3 : · · · : Xkn ) + I(Xk1 : Xk2 ),

(A1)
(A2)

Sn (X1 : X2 : · · · : Xn ) = Sn−1 (Xk1 Xk2 : Xk3 : · · · : Xkn ) + I(Xk1 : Xk2 |Xk3 · · · Xkn ).

(A3)

and

where Xkj belongs to and exhaust the set X . It is evident that the recurrence relation is not unique. For the
choice of {Xkn−j = Xj+1 }n−1
j=0 , Eq.(A1) and Eq.(A2) separately yields Eq.(9), and Eq.(A3) yields Eq.(12).
(n )

(n )

2
2. Relations between Mk 1 and Mk+1
.

(n)

M2

+

(n)

X

I(Xj : Xk ) = (n − 1)M1 ,

(A4)

j<k∈[n]
(n)
(k + 1)Mk+1 +

X

X

(n)
I (Xj1 · · · Xjk : Xi ) = (n − k)Mk +

j1 <···<jk ∈[n] i(̸=j1 ̸=···̸=jk )
(n−1)

(n)

Mn−1 (X1 : · · · : Xn ) = Mn−2 (X1 : · · · : Xn−1 ) +

n−1
X



k
1−
n

 
n
(n)
M1 ,
k


SXk + SXn − SX1 ···Xn − SXk Xn .

(A5)

(A6)

k=1

Appendix B: Proof of Eqs.(15, 16)
(n)

Here we show that Mk , for fixed k (1 ≤ k < n), is nondecreasing under discarding of any one party or grouping
together any two parties. That is,
(n)

(n−1)

Mk (X1 : X2 : · · · : Xn ) ≥ Mk
(n)
Mk (X1 : X2 : · · · : Xn )

≥

(X1 : X2 : · · · : Xn−1 ),

(n−1)
Mk
(X1 : X2 : · · · : Xn−1 Xn ).

(B1)
(B2)

8
(n)

Above inequalities follow from the definition of Mk and the entropic inequalities S(X) + S(Y ) ≥ S(XY ) (subad(n)
ditivity) and S(XY ) + S(Y Z) ≥ S(Y ) + S(XY Z) (strong subadditivity), as shown below. First, we show that Mk
is nondecreasing under discarding a subsystem.
n
X

(n)

M1 (X1 : X2 : · · · : Xn ) =

Sk − S12···n

k=1
n−1
X

=

=
≥

(n)



k=1
(n−1)
M1
(X1 : X2 : · · · : Xn−1 ) + I(X1 X2 · · · Xn−1 : Xn |1)
(n−1)
(2)
M1
(X1 : X2 : · · · : Xn−1 ) + M1 (X1 X2 · · · Xn−1 : Xn ),
(n−1)
M1
(X1 : X2 : · · · : Xn−1 ),

=

X

M2 (X1 : X2 : · · · : Xn ) =

Sk − S12···(n−1) + S12···(n−1) + Sn − S12···n

Sjk − (n − 1)S12···n

j<k∈[n]

X

=

Sjk − (n − 2)S12···(n−1)

j<k∈[n−1]


+

n−1
X


Sjn + (n − 2)S12···(n−1) − (n − 1)S12···n 

j=1
(n−1)

≥ M2





(X1 : X2 : · · · : Xn−1 ) + 

Sj + S(n−1)n − S12···n 

n−2
X
j=1

≥
≥

(n)

M3 (X1 : X2 : · · · : Xn ) =

(n−1)
(n−1)
M2
(X1 : X2 : · · · : Xn−1 ) + M1
(X1 : X2 : · · · Xn−2 : Xn−1 Xn ),
(n−1)
M2
(X1 : X2 : · · · : Xn−1 ),

X
i<j<k∈[n]

X

=



n−1
S12···n
2


n−2
Sijk −
S12···(n−1)
2

Sijk −

i<j<k∈[n−1]







n
−
2
n
−
1
S12···(n−1) −
S12···n 
+
Sijn +
2
2
i<j∈[n−1]


n−1
n−2
X
X n−1
X
(n−1)
≥ M3
(X1 : X2 : · · · : Xn−1 ) + 
S1jn +
Sij − (n − 2)S12···n 
X



j=2
(n−1)

≥ M3

i=2 j=i+1

(X1 : X2 : · · · : Xn−1 ).

(n)

(n−1)

(n)

Similarly, one can show that Mk>3 (X1 : X2 : · · · : Xn ) ≥ Mk>3 (X1 : X2 : · · · : Xn−1 ). Next, we show that Mk
nondecreasing under grouping together two parties, specifically for n = 4.
(4)

M1 (X1 : X2 : X3 : X4 ) = (S1 + S2 + S3 + S4 ) − S1234
= (S1 + S2 + S34 − S1234 ) + (S3 + S4 − S34 )
(3)

(2)

= M1 (X1 : X2 : X3 X4 ) + M1 (X3 : X4 ),
(3)

≥ M1 (X1 : X2 : X3 X4 ),

is

9
(4)

M2 (X1 : X2 : X3 : X4 ) = S12 + S13 + S14 + S23 + S24 + S34 − 3S1234
= (S12 + S134 + S234 − 2S1234 )
+(S13 + S14 + S23 + S24 + S34 − S134 − S234 − S1234 )
(3)

≥ M2 (X1 : X2 : X3 X4 ) + (S1 + S2 + S34 − S1234 ),
(3)

(3)

= M2 (X1 : X2 : X3 X4 ) + M1 (X1 : X2 : X3 X4 ),
(3)

≥ M2 (X1 : X2 : X3 X4 ),
(4)

M3 (X1 : X2 : X3 : X4 ) = S123 + S124 + S134 + S234 − 3S1234
(3)

≥ 0 = M3 (X1 : X2 : X3 X4 ).
■
(n)

Appendix C: Semipositivity of Mk
(n)

Here we illustrate the nonnegativity of Mk

for n = 5.

(5)

= (S1 + S2 + S3 + S4 + S5 ) − S12345 ≥ S12345 − S12345 = 0.

(5)

= S12 + S13 + S14 + S15 + S23 + S24 + S25 + S34 + S35 + S45 − 4S12345
= (S12 + S34 ) + S15 + (S13 + S45 ) + S24 + (S14 + S23 ) + S25 + S35 − 4S12345
≥ (S1234 + S15 ) + (S1345 + S24 ) + (S1234 + S25 ) + S35 − 4S12345
≥ (S12345 + S1 ) + (S12345 + S4 ) + (S12345 + S2 ) + S35 − 4S12345
= (S1 + S2 + S4 ) + S35 − S12345
≥ (S124 + S35 ) − S12345
≥ S12345 − S12345 = 0.

(5)

= S123 + S124 + S125 + S134 + S135 + S145 + S234 + S235 + S245 + S345 − 6S12345
= (S123 + S145 ) + (S124 + S235 ) + (S135 + S234 ) + (S134 + S245 ) + (S125 + S345 ) − 6S12345
≥ (S1 + S12345 ) + (S2 + S12345 ) + (S3 + S12345 ) + (S4 + S12345 ) + (S5 + S12345 ) − 6S12345
= (S1 + S2 + S3 + S4 + S5 ) − S12345 ≥ 0.

(5)

= (S1234 + S1235 ) + (S1245 + S1345 ) + S2345 − 4S12345
≥ (S123 + S12345 ) + (S145 + S12345 ) + S2345 − 4S12345
≥ (S123 + S145 ) + S2345 − 2S12345
≥ (S1 + S12345 ) + S2345 − 2S12345
= (S1 + S2345 ) − S12345
≥ S12345 − S12345 = 0.

M1
M2

M3

M4

(n)

Alternatively, one can also endeavor to obtain a recurrence relation for Mk which expresses it as a positive sum
of bipartite mutual information I(A : B) and conditional mutual information I(A : B|C). Then, the semipositivity
(n)
of Mk is trivial. We, however, note that obtaining the recurrence relation is neither unique [see Eqs.(A1, A2, A3)]
nor easy. For example,
(n)

(n−1)

M2 (X1 : X2 : · · · : Xn ) = M2

(n−1)

(X1 : X2 : · · · : Xn−1 ) + M1
(X1 : X2 : · · · : Xn−1 )
Pn−1
+I(Xn : X2 · · · Xn−1 |X1 ) + j=2 I(Xn : X1 · · · Xj−1 Xj+1 · · · Xn−1 |Xj ).

(C1)
■

10
(n)

Appendix D: Argument for Secrecy Monotones of Mk
(n)

Our argument for the speculation that Mk meet the criteria of secrecy monotones is as follows. Consider a fiveparty quantum system X = {X1 , · · · , X5 }, for example. We know that the von Neumann entropy is invariant under
unitary transformations including the permutation or particle exchange operator. That is, S12345 = S13245 = S23145 ,
etc. Then
(5)

M2 (X1 : X2 : · · · : X5 ) = S12 + S13 + S14 + S15 + S23 + S24 + S25 + S34 + S35 + S45 − 4S12345
= (S12 + log2 (d3 d4 d5 ) − S12345 ) + (S13 + log2 (d2 d4 d5 ) − S13245 ) + · · ·
+ (S45 + log2 (d1 d2 d3 ) − S12345 ) + 6S12345 − log2 (d1 d2 d3 d4 d5 )6
=D(ρ12345 ||ρ12 ⊗ I345 ) + D(ρ13245 ||ρ13 ⊗ I245 ) + · · · + D(ρ12345 ||I123 ⊗ ρ45 ) + 6S12345 − log2 (d1 d2 d3 d4 d5 )6 ,
and
(5)

M3 (X1 : X2 : · · · : X5 ) = S123 + S124 + S125 + S134 + S135 + S145 + S234 + S235 + S245 + S345 − 6S12345
= (S123 + log2 (d4 d5 ) − S12345 ) + (S124 + log2 (d3 d5 ) − S12435 ) + · · ·
+ (S345 + log2 (d1 d2 ) − S12345 ) + 4S12345 − log2 (d1 d2 d3 d4 d5 )4
=D(ρ12345 ||ρ123 ⊗ I45 ) + D(ρ12435 ||ρ124 ⊗ I35 ) + · · · + D(ρ12345 ||I12 ⊗ ρ345 ) + 4S12345 − log2 (d1 d2 d3 d4 d5 )4 .
While D(ρAB ||ρA ⊗ ρB ) is always well-behaved, D(ρAB ||ρB ⊗ ρA ) is not in general due to the support condition.
Therefore, in the second steps above, the parties (subsystems) have been rearranged beforehand to resolve the support
condition of QRE. Note that the operations such as local quantum operations and local measurements and public
classical communication can be regarded as local positive maps [27]. Because D(ρ||σ) ≥ D(Φ(ρ)||Φ(σ)) for any local
(n)
positive map Φ, it implies that Mk are monotonic under local quantum operations and classical communications. ■

