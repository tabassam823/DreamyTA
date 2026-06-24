You may also like

PAPER • OPEN ACCESS

Noise resilience of variational quantum compiling
To cite this article: Kunal Sharma et al 2020 New J. Phys. 22 043006

View the article online for updates and enhancements.

- Variational quantum compiling with double
Q-learning
Zhimin He, Lvzhou Li, Shenggen Zheng et
al.
- Efficient and practical quantum compiler
towards multi-qubit systems with deep
reinforcement learning
Qiuhao Chen, Yuxuan Du, Yuliang Jiao et
al.
- Time-optimal holonomic quantum gates on
Rydberg atoms
Jia-Qi Li, Hong-Xuan Li, Pei-Yao Song et
al.

This content was downloaded from IP address 103.94.191.173 on 23/06/2026 at 08:38

New J. Phys. 22 (2020) 043006

https://doi.org/10.1088/1367-2630/ab784c

PAPER

Noise resilience of variational quantum compiling
OPEN ACCESS

Kunal Sharma1,2 , Sumeet Khatri2, M Cerezo1,3
RECEIVED

1 October 2019

1
2

REVISED

20 January 2020
ACCEPTED FOR PUBLICATION

3

Theoretical Division, Los Alamos National Laboratory, Los Alamos, NM 87545, United States of America
Hearne Institute for Theoretical Physics and Department of Physics and Astronomy, Louisiana State University, Baton Rouge, LA United
States of America
Center for Nonlinear Studies, Los Alamos National Laboratory, Los Alamos, NM, United States of America

20 February 2020

E-mail: kunals2693@gmail.com

PUBLISHED

Keywords: noise, resilience, variational, algorithms, quantum

7 April 2020

and Patrick J Coles1

Original content from this
work may be used under
the terms of the Creative
Commons Attribution 4.0
licence.

Abstract
Variational hybrid quantum-classical algorithms (VHQCAs) are near-term algorithms that leverage
classical optimization to minimize a cost function, which is efﬁciently evaluated on a quantum
Any further distribution of computer. Recently VHQCAs have been proposed for quantum compiling, where a target unitary U is
this work must maintain
attribution to the
compiled into a short-depth gate sequence V. In this work, we report on a surprising form of noise
author(s) and the title of
resilience
for these algorithms. Namely, we ﬁnd one often learns the correct gate sequence V (i.e. the
the work, journal citation
and DOI.
correct variational parameters) despite various sources of incoherent noise acting during the costevaluation circuit. Our main results are rigorous theorems stating that the optimal variational
parameters are unaffected by a broad class of noise models, such as measurement noise, gate noise,
and Pauli channel noise. Furthermore, our numerical implementations on IBM’s noisy simulator
demonstrate resilience when compiling the quantum Fourier transform, Toffoli gate, and W-state
preparation. Hence, variational quantum compiling, due to its robustness, could be practically useful
for noisy intermediate-scale quantum devices. Finally, we speculate that this noise resilience may be a
general phenomenon that applies to other VHQCAs such as the variational quantum eigensolver.

1. Introduction
Obtaining accurate answers from near-term quantum computers is a challenge with major scientiﬁc and
technological implications. In these so-called noisy intermediate-scale quantum (NISQ) computers [1], errors
arise, for example, due to decoherence processes, gate noise, and measurement noise. Clearly, error mitigation
techniques will be necessary to make use of NISQ devices. Several promising error mitigation strategies have
recently emerged, including zero-noise extrapolation [2], quasi-probability decomposition [2], post-selection
[3, 4], noise-aware compiling [5], and machine learning for circuit-depth compression [6]. Let us consider two
other strategies for error mitigation in what follows.
Hybridizing a quantum algorithm by pushing some of the complexity onto a classical computer allows one
to only run a portion of the computation on the (error-prone) quantum computer. Excellent examples of this
strategy are variational hybrid quantum-classical algorithms (VHQCAs) [7]. VHQCAs only employ a quantum
computer to evaluate a cost function that depends on the parameters of a quantum gate sequence and then
leverage a classical optimization routine to minimize the cost and hence train the parameters. The most famous
VHQCA is the variational quantum eigensolver (VQE) [8], where the cost function is the energy for some
Hamiltonian and hence the goal is to prepare the ground state. VHQCAs have been proposed for many other
applications [9–22].
Another strategy for error mitigation is to ﬁnd quantum circuits or quantum algorithms that are inherently
noise resilient. Circuits for quantum error correction [23, 24], of course, have this property of inherent noise
resilience, and in fact, such circuits are resilient to all types of noise on a subset of the qubits. More generally, one
could ask whether a circuit is resilient to a particular kind of noise process. Hence, for every circuit, which aims
to compute some quantity, one could ask what noise models do not affect the output of the circuit.

© 2020 The Author(s). Published by IOP Publishing Ltd on behalf of the Institute of Physics and Deutsche Physikalische Gesellschaft

New J. Phys. 22 (2020) 043006

K Sharma et al

The two strategies just mentioned have an interesting intersection: researchers have observed that some
VHQCAs have some inherent noise resilience. McClean et al [7] noted that coherent errors (e.g., systematic gate
biases) can lead to a situation where the formal unitary V (a) speciﬁed by the parameters a is different from the
~
actual unitary that is physically implemented V (a). This error is correctable if there exists a vector b such that
~
one can physically implement the unitary V (a + b ) within one’s ansatz, with the condition that
~
V (a + b ) = V (a). If this condition is satisﬁed, then one could still physically achieve the minimum value of
the cost function, where the minimum value would be associated with different parameters than one would have
in the noiseless case. We refer to this kind of noise resilience as Cost Value Resilience, since the value of the cost
function at the global minimum is unaffected by the noise. Cost Value Resilience is important, e.g. if one is
interested in estimating the ground state energy of a Hamiltonian with VQE.
In this work, we report on a different kind of noise resilience for VHQCAs. Instead of considering Cost Value
Resilience, we consider the case where the optimal parameters are noise resilient, which we call Optimal
Parameter Resilience. While Cost Value Resilience is related to coherent noise, we ﬁnd that Optimal Parameter
Resilience holds for certain kinds of incoherent noise, such as decoherence processes and readout errors. For
certain applications, obtaining the correct optimal parameters is more important than obtaining the correct
value of the cost function.
Quantum compiling [25–27] is one of these applications. Compiling refers to transforming a high-level
algorithm into a low-level machine code. For quantum compiling, it is crucial to do this transformation
optimally, i.e. to keep the low-level code as short as possible, since errors accumulate with circuit depth.
VHQCAs offer a promising framework for (optimal) quantum compiling. Three recent works introduced
VHQCAs for quantum compiling, henceforth referred to as variational quantum compiling (VQC) [19–21]. In
VQC one trains the parameters a of a short-depth gate sequence V (a) such that it is close to a target unitary U.
Here, some distance measure between V (a) and U serves as the cost function and is efﬁciently evaluated on a
quantum computer, while a classical optimizer adjusts the parameters a to minimize the cost. VQC could be an
important tool for NISQ computing since it could optimally shrink the depth of quantum circuits. However, a
potential issue is that one needs to put the target unitary U on the NISQ device, and hence the target itself is noisy
or defective. Furthermore, there are noise sources in other parts of the cost-evaluation circuit. All of these may
lead to a defective optimal V (a), with the noise effectively compiled into V (a).
Addressing these concerns, our main results are rigorous theorems stating that many different types of noise
during cost evaluation do not affect the optimal V (a). For example, we show that VQC is resilient to
measurement noise (readout error). We also show resilience to incoherent gate noise and decoherence
processes, such as Pauli channels and non-unital Pauli channels, acting at speciﬁc times during the costevaluation circuit. In addition to these analytical results, we implement VQC on IBM’s noisy quantum simulator
[28] (which simulates their quantum hardware) for several quantum gates: quantum Fourier transform, Toffoli,
and W-state preparation. In each case, we observed signiﬁcant noise resilience (even more resilience than what is
explained by our theorems) such that we effectively learned the true optimal values of a despite the noise.
Finally, we speculate that the resilience phenomenon that we demonstrate for VQC may be more general,
potentially applying to other VHQCAs. For example, we discuss the potential for seeing this resilience for VQE,
and as a warm-up for the reader, we give a simple example in the next section where VQE exhibits Optimal
Parameter Resilience. We also establish in the Discussion section that VQC is a special case of VQE, and hence
our main results can be viewed as being relevant to VQE.

2. Warm-up: simple VQE example
Here we show that VQE [8] exhibits Optimal Parameter Resilience (OPR) to uncorrelated measurement noise
for a special class of Hamiltonians. VQE may exhibit OPR more generally, although the proof would certainly be
more involved. Hence we consider here this special case for illustration and leave the more general case for
future work.
Consider a Hamiltonian that is a sum of local Pauli operators
n

H = - å c ( j ) s (wj () j ) ,

(1)

j=1

where s(wj)( j) = Uw( j()j) s(z j) (Uw( j()j) )† is a local operator on qubit j that is unitarily equivalent to the Pauli z operator
s(z j) . Physically, this Hamiltonian arises for a system of n non-interacting spin-1/2 particles in a non-uniform
(i.e. j-dependent) magnetic ﬁeld. Without loss of generality, one can take the c ( j) coefﬁcients to be non-negative
(i.e. absorb any negativity into the deﬁnition of the Pauli operator). The ground state ∣y0ñ of H has a tensor
product form: ∣y0ñ = ⨂nj = 1∣w ( j )+ñ, where ∣w ( j )+ñ is the eigenvector of s(wj)( j) with the +1 eigenvalue.
2

New J. Phys. 22 (2020) 043006

K Sharma et al

Now suppose there is measurement noise in the cost-evaluation circuit. In the ideal case, one measures áH ñ =
( j)
( j)
( j)
( j)
å j c ( j) ás w ( j) ñ = å j c ( j) áUw ( j) s(z j) (Uw ( j) )†ñ by applying (Uw ( j) )† on the jth qubit and measuring it on the standard
basis to estimate ás(wj)( j) ñ. Then, by performing classical post-processing we compute the weighted sum in áH ñ.
( j)
( j)
However, with measurement noise, the s(z j) operator gets replaced by s
- p10( j ) )∣0ñá0∣ - ( p11( j ) - p01
)∣1ñá1∣.
z( j ) = ( p00
( j)
Here, pkl is the probability to obtain the k outcome when feeding in the ∣l ñ state on the jth qubit. Hence, instead of
measuring ás(wj)( j) ñ, one measures á s
w( j()j) = Uw( j()j) s
z( j) (Uw( j()j) )†. In other words, the Hamiltonian H gets
w( j()j) ñ with s
replaced by an effective Hamiltonian:

n

~
H = -å c ( j) 
sw( j()j ) .

(2)

j=1

~
The ground state of H is a tensor product of one-qubit states that are the eigenvectors of s
w( j()j) with the
( j)
( j)
( j)
( j)
largest eigenvalue. Suppose we assume that p00 + p11 > p01 + p10 for all j, which means that the probability
of getting the correct outcome is greater than the probability for getting the wrong outcome. With this
assumption, the largest eigenvalue of s
z( j) is associated with the ∣0ñ state, and hence the largest eigenvalue of
( j)
s
w ( j) is associated with ∣w ( j )+ñ. Therefore, despite the measurement noise, one still ﬁnds that the ground state is
∣y0ñ = ⨂nj = 1∣w ( j )+ñ. This implies that one would still learn the correct optimal parameters of the statepreparation circuit if one implemented VQE for this Hamiltonian.

3. Background: variational quantum compiling
Let us now move on to variational quantum compiling (VQC). VQC was ﬁrst introduced in [19], under the
name of quantum-assisted quantum compiling (QAQC). Two later works further investigated VQC [20, 21]
with slightly different approaches. Since we are attempting to unite these works [19–21] under one umbrella, we
are proposing the name VQC (instead of QAQC) as a unifying term.
There are two overarching approaches to VQC. One is to compile the full unitary matrix U by considering
the action of U on all input states (or an informationally complete set of states) [19, 21]. The other is to compile
only a particular column of the matrix U by considering the action of U on a ﬁxed input state [19, 20]. The
beneﬁt of the ﬁrst approach is that it is fully general, applying even when one does not know what the input state
to U will be (for example, if U occurs in the middle of one’s quantum algorithm). The beneﬁt of the second
approach is that, when the input state is known, it could lead to a shorter-depth compilation since it does not
require compilation of the entire unitary matrix.
3.1. Full unitary matrix compiling
Full unitary matrix compiling (FUMC) was treated in detail in [19]. This work introduced cost functions based
on the entanglement ﬁdelity and proposed quantum circuits to quantify the cost based on the overlap between
maximally entangled states. A slightly different but equivalent approach was employed in [21]. We focus on the
approach of [19] in what follows.
Two cost functions were considered in [19]. One cost function CHST quantiﬁes the Hilbert–Schmidt inner
product between the target unitary U and the trainable gate sequence V, as follows:
CHST = 1 - FHST,

with FHST = ∣ Tr(V †U )∣2 d 2,

(3)

n

where d=2 is the Hilbert-space dimension and n is the number of qubits that U acts on, and where we write V
instead of V (a) for simplicity. The circuit for computing CHST is called the Hilbert–Schmidt Test (HST) and is
shown in ﬁgure 1(a). First, one prepares a maximally entangled state ∣FñAB by acting with a depth-two circuit E,
then one applies U followed by V † on half of this maximally entangled state. Finally one measures the overlap
with the original maximally entangled state ∣FñAB by applying E † and quantifying the probability of the all-zeros
measurement outcome. One can verify that this probability is equal to FHST = ∣ Tr (V †U )∣2 d 2. This cost
function is operationally meaningful since it is equivalent to the average ﬁdelity F (U , V ) = ò ∣ áy∣V †U ∣yñ ∣2 dy
between states acted upon by U versus those acted upon by V, as follows [29, 30]:
d+1
(1 - F (U , V )).
d
Note that CHST is faithful in that CHST = 0 iff V=U (up to a global phase).
An alternative cost function [19] is given by
CHST =

CLHST = 1 - FLHST,

3

with FLHST =

1 n ( j)
åF ,
n j = 1 LHST

(4)

(5)

New J. Phys. 22 (2020) 043006

K Sharma et al

Figure 1. Circuits for cost evaluation in full unitary matrix compiling. (a) The Hilbert–Schmidt test (HST). An entangling gate E,
consisting of Hadamards and CNOTs, prepares a maximally entangled state between systems A and B. Then a target unitary U is
applied on A, which is followed by a trainable unitary V † . Finally, a measurement in the Bell basis is performed by applying the adjoint
of E, followed by a standard basis measurement. This circuit computes the Hilbert–Schmidt inner product between U and V, as the
probability to obtain the measurement outcome in which all 2n qubits are in the ∣0ñ state is FHST = (1 22n)∣ Tr (V †U )∣2 . (b) The local
Hilbert–Schmidt test (LHST), which is same as the HST circuit, except the disentangling gate E † is applied only on one Aj Bj pair of
qubits (depicted here for the A1 B1 pair) and subsequently, the same two qubits are measured in the standard basis. The probability for
( j)
the outcome associated with the ∣00ñ state is FLHST
in (5).

( j)
where FLHST
is the probability of the 00 measurement outcome in the local Hilbert–Schmidt test (LHST), which
is the circuit shown in ﬁgure 1(b). Note that FHST is the entanglement ﬁdelity for the quantum channel deﬁned
( j)
by V †U . On the other hand, FLHST
is the entanglement ﬁdelity for the quantum channel obtained from feeding
†
into V U the maximally mixed state on Aj and then tracing over Aj , where Aj consists of all qubits in A other
than Aj. As shown in [19]

CLHST  CHST  nCLHST,

(6)

which implies that CLHST is also a faithful cost function, i.e. CLHST = 0 iff V=U (up to a global phase).
The overall cost function proposed by [19] was a convex combination of CHST and CLHST :
C (q) = qCHST + (1 - q) CLHST.

(7)

Here, q is a free parameter with 0  q  1. The deﬁnition of C(q) was motivated in [19] by the fact that CHST has
a direct operational meaning (equation (4)) but it becomes difﬁcult to train for large n due to a vanishing gradient
[31], whereas CLHST is trainable but does not have a direct operational meaning. Hence one can take a weighted
average of these two functions, where for small n one can choose q » 1, while for large n one can choose q≈0.
3.2. Compiling with a ﬁxed input state
Fixed input state compiling (FISC) of a unitary matrix was introduced in [20, 19] and treated in signiﬁcant detail
in [20]. In this case, the goal is to train a gate sequence V so that it has the same effect as a target unitary U when
acting on a given input state ∣y0ñ. For simplicity and due to its technological relevance, we will consider the case
where ∣y0ñ = ∣0ñ is the all-zero state, so that we are interested in training V to satisfy (up to a global phase):
U ∣0ñ = V ∣0ñ ,

or equivalently

W ∣0ñ = ∣0ñ ,

(8)

with W = V †U . To quantify how far W ∣0ñ is from the state ∣0ñ, one can deﬁne the cost function
CLET = 1 - G LET,

where GLET is the ﬁdelity F (r, s ) = (Tr [

rs

(9)

r ])2 between these two states:

G LET = F (∣0ñá0∣ , W ∣0ñá0∣W †) = ∣ á0∣W ∣0ñ ∣2 = Tr [P0 W ∣0ñá0∣W †] ,

(10)

with P0 = ∣0ñá0∣ the projector onto the all-zero state. We employed the LET subscript here since we refer to the
circuit used to quantify (9) and (10) as the Loschmidt echo test (LET), shown in ﬁgure 2(a). The Loschmidt echo
[32] refers to a forward and backward time evolution with the intent of recovering the initial state. This is
analogous to the circuit in ﬁgure 2(a) where one ﬁrst evolves forward with U and then attempts to undo that
evolution with V †, to recover the initial state ∣0ñ. Hence the probability of the all-zero measurement outcome in
ﬁgure 2(a) is precisely GLET .
One can see that compiling with a ﬁxed input state leads to more freedom and hence more solutions than full
unitary matrix compiling. Note that CHST = 0 iff W = e if where f is a global phase factor. On the other hand,
CLET = 0 iff ∣ á0∣W ∣z ñ ∣ = ∣ áz∣W ∣0ñ ∣ = dz , 0 for all bit strings z . Hence, for W that achieve CLET = 0 , the
(n − 1)×(n − 1) unitary principal submatrix of W with matrix elements áz∣W ∣z ¢ñ (such that z , z ¢ ¹ 0 )
remains completely arbitrary. This degeneracy of optima can simplify the optimization of V as any of these
optima will lead to CLET = 0 .
4

New J. Phys. 22 (2020) 043006

K Sharma et al

Figure 2. Circuits for cost evaluation in compiling with a ﬁxed input state. (a) The Loschmidt echo test (LET). In this circuit, the
probability of obtaining the measurement outcome in which all n qubits are in the ∣0ñ state is GLET = ∣ á0∣V †U ∣0ñ ∣2 . (b) The local
Loschmidt echo test (LLET), which is the same as the LET but only the Aj qubit is measured. The probability that this qubit is in the ∣0ñ
( j)
state is GLLET
in (12).

Analogous to the LHST cost for full unitary matrix compiling, one can deﬁne a cost function for ﬁxed input
state compiling that involves local observables:
CLLET = 1 - G LLET = 1 -

1 n
å G ( j) ,
n j = 1 LLET

with

A

( j)
G LLET
= Tr [(P0 j Ä  A j ) W ∣0ñá0∣W †].

(11)

A

Here, P0 j is the projector onto the zero state on the Aj qubit, and  Aj denotes the identity on all qubits except Aj
and n is the number of qubits. We call the circuit used to compute CLLET the local Loschmidt echo test (LLET),
and this circuit is shown in ﬁgure 2(b). Note that
A

( j)
G LLET
= Tr A j [P0 j r ( j ) ] = á0∣r ( j ) ∣0ñ = F (∣0ñá0∣ , r ( j )) ,

(12)

( j)
where r( j) = Tr Aj [W ∣0ñá0∣W †]. Hence GLLET
corresponds to the probability of the zero outcome for the circuit
in ﬁgure 2(b). With a proof similar to that of (6) one can show that

CLLET  CLET  nCLLET,

(13)

and hence CLLET = 0 iff CLET = 0 . Furthermore, one can deﬁne an overall cost function analogous to
C(q) in (7)
C ¢ (q) = qCLET + (1 - q) CLLET,

(14)

which again is motivated by the fact that CLET has a direct operational meaning but is difﬁcult to train for large n,
whereas the opposite is true for CLLET . Hence one can take q » 1 for small n and q≈0 for large n.

4. Noise processes
In this work, we consider three different types of noise [33, 34]: (1) decoherence noise, (2) gate noise, and (3)
measurement noise. We now discuss how we mathematically model these three types of noise.
Let us start with decoherence. Physical models of decoherence often refer to T1 and T2 processes, which
respectively pertain to thermal relaxation (energy dissipation) and dephasing (loss of phase coherence). These
processes are typically modeled as local quantum channels acting independently on individual qubits. However,
mathematically it is easier to deal with classes of quantum channels that act globally on sets of qubits (which can
contain the independent local channels as a special case). In what follows, we deﬁne three types of global
quantum channels: depolarizing noise, Pauli noise, and non-unital Pauli noise. It is worth noting that Pauli
noise includes T2 processes as a special case (i.e. the dephasing channel is a Pauli channel), and non-unital Pauli
noise includes T1 processes as a special case (i.e. the amplitude damping channel is a non-unital Pauli channel).
Consider the following precise deﬁnitions.
Deﬁnition 1. We deﬁne depolarizing noise (DN) as a completely positive trace-preserving (CPTP) map that
maps an n-qubit state ρ to the state pr + (1 - p )  (2n).
Deﬁnition 2. We deﬁne Pauli Noise (PN) as a CPTP map  whose superoperator is diagonal in the Pauli basis.
In other words, its action on a Pauli operator X l Z k := X l1 Z k1 Ä ... Ä X ln Z kn is given by  (X l Z k ) = clk X l Z k ,
where c 00 = 1. Furthermore, we assume that clk  0 for all l and k , where l1, K, l n, k1, K, k n Î {0, 1}.
Deﬁnition 3. We deﬁne non-unital Pauli noise (NUPN) as a CPTP map NU whose action on the identity is
NU () =  + å (l, k ) ¹ (0, 0) dlk X l Z k , and whose action on all other Pauli operators X l Z k with (l , k ) ¹ (0, 0) is
given by NU (X l Z k ) = clk X l Z k . Furthermore, we assume that clk  0 for all l and k .
5

New J. Phys. 22 (2020) 043006

K Sharma et al

Next, we consider gate noise. While gate noise can involve coherent errors such as systematic gate bias, such
errors are hardware-speciﬁc, and hence we focus on incoherent gate noise. We consider a simple model for gate
noise in which every time a gate is implemented, a Pauli channel acts both before and after this gate.
Furthermore, for generality, we allow these Pauli channels to act globally on all qubits, which serves as a model
for cross-talk (where gates affect qubits on which they are intended to act trivially).
Deﬁnition 4. We deﬁne Pauli gate noise (PGN) as a simple noise model in which all gates are preceded and
followed by global Pauli channels. In other words, for a gate G , instead of its action on a state ρ being GrG†, we
model its action as ¢ (G  (r ) G†) where  and ¢ are Pauli channels. Note that these Pauli channels act on all
qubits, including qubits on which G acts trivially.
Finally, we consider measurement noise, also known as readout error. For a single qubit, we model
measurement noise as a classical bit-ﬂip channel, where feeding in the standard basis state ∣l ñ leads to the k
outcome with probability pkl. We allow for asymmetry in that one can have p01 ¹ p10, which is an important
generality, e.g. when T1 noise occurs during the measurement process. For multiple qubits, our measurement
noise model is a tensor product of the aforementioned bit-ﬂip channels, corresponding to uncorrelated
measurement noise.
Deﬁnition 5. We deﬁne measurement noise (MN) as a modiﬁcation of the standard-basis POVM elements,
which are {P0 = ∣0ñá0∣, P1 = ∣1ñá1∣} for a noiseless single qubit. With measurement noise, this POVM gets
replaced by {P0, P1}, with P0 = p00∣0ñá0∣ + p01∣1ñá1∣ and P1 = p10∣0ñá0∣ + p11∣1ñá1∣, where p00 + p10 = 1,
p01 + p11 = 1, and pkl is the probability of getting the k outcome given the l input. Furthermore we assume that
pkk > pkl for l ¹ k . Hence, for an n -qubit standard-basis measurement with measurement noise, we write the
POVM element associated with the bit string z = (z1, ¼, z n) as
n

Pz = ⨂ ( pz(jj0) ∣0ñá0∣ + pz(jj1) ∣1ñá1∣) ,

(15)

j=1

with å z j pz(j j0) = 1 and å z j pz(j j1) = 1, and we assume that pz(j jz)j > pz(j jl) for l ¹ z j .

5. Main results
Before proceeding to the main results we ﬁrst deﬁne two versions of optimal parameter resilience (OPR), i.e. of
learning the correct gate sequence V despite various sources of noise, which we refer to as strong-OPR and
weak-OPR.
Deﬁnition 6. Let d be the set of d ´ d unitary matrices. Let CQC (V ) be a cost function of V with V Î d , and
QC (V ) denote the noisy
suppose that CQC (V ) can be evaluated using a quantum circuit denoted QC. Let C
version of CQC (V ), i.e. the corresponding function whenever the circuit QC is run in the presence of some noise
~opt
QC (V ), i.e.
process  . Let  dopt and  d respectively denote the sets of unitaries that optimize CQC (V ) and C
 opt
d = {V ¢ Î d : C QC (V ¢) = min C QC (V )} ,

(16)

~opt
QC (V ¢) = min C
QC (V )}.
 d = {V ¢ Î d : C

(17)

V Î d

V Î d

~opt
We say that CQC (V ) exhibits strong-OPR to  if  d =  dopt . We say that CQC (V ) exhibits weak-OPR to 
opt
~
if  d Í  dopt .

5.1. Noise resilience of full unitary matrix compiling
Let us begin with full unitary matrix compiling (FUMC). Figure 3 shows the two noise models that we will
consider for FUMC. As shown in this ﬁgure, τ1 and τ2 are respectively deﬁned as the times just before and just
after the application of V †U . We note that the noise models considered in ﬁgure 3 capture fairly well the physical
noise that is present in, e.g. superconducting-qubit quantum computers, with the exception that only
depolarizing noise is allowed during the action of V †U . We make this simpliﬁcation for ease of analysis,
although our numerics in section 6 relax this assumption.
Consider the following deﬁnition for the noise model depicted in ﬁgure 3(a).
Deﬁnition 7. We deﬁne noise Model 1 to be the following noise process during the HST circuit: (1) global
depolarizing noise acting continuously throughout the circuit, (2) global Pauli noise at times t1 and t2, (3) global
depolarizing noise on system A acting continuously in between t1 and t2, (4) global non-unital Pauli noise on
6

New J. Phys. 22 (2020) 043006

K Sharma et al

Figure 3. Schematic diagram of: (a) Noise Model 1 of deﬁnition 7, and (b) Noise Model 2 of deﬁnition 8. The following acronyms are
employed: depolarizing noise (DN), Pauli gate noise (PGN), Pauli noise (PN), non-unital Pauli noise (NUPN), and measurement
noise (MN). Red dashed boxes indicate the time period and the qubits on which the noise process acts. Time τ1 (τ2) corresponds to the
time immediately before (after) the action of the unitary V †U . While both panels show the HST, these noise models are also applicable
to the LHST, provided one replaces E † with (E ( j) )†.

system B acting continuously in between t1 and t2, (5) Pauli gate noise during E and E †, and (6) measurement
noise. We also use the term Noise Model 1 when the same noise model acts during the LHST circuit, provided
one replaces E † with (E ( j))†.
We now state our ﬁrst main result. The proof of this result is given in appendix D, with some useful
preliminaries and lemmas given in appendices A–C.
Theorem 1. The cost functions CHST and CLHST exhibit strong-OPR to Noise Model 1 in deﬁnition 7.
Note that this theorem also implies that C (q ) = qCHST + (1 - q ) CLHST exhibits strong-OPR to Noise
~opt
Model 1, for all values of q. This is because the set  dopt =  d deﬁned in (16) and (17) is the same for CHST and
CLHST functions. Hence this same set is optimal for C(q).
Consider the implications of theorem 1. First, this theorem implies that FUMC is resilient to the
measurement noise model in deﬁnition 5. Second, FUMC is completely resilient to Pauli gate noise during the
entangling and disentangling gates, E and E †. Note that this Pauli gate noise is global and hence accounts for
cross talk. Third, FUMC is resilient to global depolarizing noise acting continuously throughout the circuit, as
well as global Pauli noise acting at the speciﬁc times τ1 and τ2. Fourth, FUMC is resilient to depolarizing noise
acting on system A and non-unital Pauli noise acting on system B, provided that each of these process act
(possibly continuously) during the time interval between τ1 and τ2. We emphasize that Pauli noise includes
dephasing channels (T2 noise) as a special case, while non-unital Pauli noise includes the depashing channel
(T1 noise) as a special case. Importantly, theorem 1 states that FUMC is resilient to the general case where all of
these noise processes occur together.
We now state our second main result (proven in appendix E), which deals with the noise model in
ﬁgure 3(b).
Deﬁnition 8. We deﬁne Noise Model 2 to be the following noise process during the HST circuit: (1) global
depolarizing noise acting continuously throughout the circuit, (2) global Pauli noise at times t1 and t2, (3) global
non-unital Pauli noise on system A at time t1, (4) global depolarizing noise on system A acting continuously in
between t1 and t2, (5) global Pauli noise on system B acting continuously in between t1 and t2, (6) Pauli gate
noise during E and E †, and (7) measurement noise. We also use the term Noise Model 2 when the same noise
model acts during the LHST circuit, provided one replaces E † with (E ( j))†.
Theorem 2. The cost functions CHST and CLHST exhibit strong-OPR to Noise Model 2 in deﬁnition 8.
The implications of theorem 2 are similar to those of theorem 1. The main difference is that theorem 2 allows
for non-unital Pauli noise on system A at time τ1, at the expense of only allowing Pauli noise to act continuously
on system B between τ1 and τ2. The other aspects of the noise models treated by these two theorems are identical.
The above two theorems immediately imply several corollaries below. These corollaries establish resilience
to noise models that are different and in some cases more general than the noise models previously considered,
at the expense of possibly specializing the form of the unitary W = V †U . See appendix G for the proofs of all
corollaries.

7

New J. Phys. 22 (2020) 043006

K Sharma et al

Corollary 1. The cost functions CHST and CLHST exhibit strong-OPR to a noise model that includes the
following: (1) all noise processes in Noise Model 1, as well as (2) a noise process during the implementation of
 = k ◦  ◦ 1 =  † ◦  (i.e. in the time interval between t1 and t2) in which global Pauli channels
{1A , K,  kA} act on system A, such that the overall channel on A is  kA ◦ k  ◦ 1A ◦ 1, provided that the
following condition is satisﬁed:
 A)(·).
( kA ◦  k  ◦  1A ◦ 1)(·) = ( k ◦  k - 1  ◦ 1 ◦ 

(18)

 is also a Pauli channel, and the channels  ,  †, and  correspond to conjugating the state by the unitaries
Here 
†
U , V , and W , respectively.
A

The condition in (18) implies that the overall channel consisting of global Pauli channels acting on system A
during the implementation of  is mathematically equivalent (although physically inequivalent) to a Pauli
channel followed by  . Therefore, corollary 1 follows from theorem 1.
Consider the following implications of corollary 1. Unitaries corresponding to the Clifford group necessarily
satisfy the condition in (18), as shown in appendix A. Therefore, corollary 2 below holds for any Clifford unitary
W. Moreover, tensor-product unitaries satisfy this same condition provided that the noise is local depolarizing
noise, and hence corollary 3 below also follows from corollary 1.
Corollary 2. Let the W = V †U gate sequence have the form W = W2A W1A with W1A composed only of Clifford gates.
Then the cost functions CHST and CLHST exhibit strong-OPR to a noise model that includes the following: (1) all noise
processes in Noise Model1, as well as (2) a noise process during the implementation of  1A = 1, k ◦  ◦ 1,1, in
which global Pauli channels {1A , K,  kA} act on system A, such that the overall channel on A
is  kA ◦ 1, k  ◦ 1A ◦ 1,1.
Corollary 3. Let the W = V †U gate sequence have the form W = W2A W1A with W1A = W1A ¢ Ä W1A  being a tensor
product, i.e. W is a tensor product up to a particular time. Then the cost functions CHST and CLHST exhibit strong-OPR
to a noise model that includes the following: (1) all noise processes in Noise Model 1, as well as (2) a noise process during the
A¢
A
implementations of  1A ¢ =  1,Ak¢ ◦  ◦  1,1
and  1A  =  1,Al ◦  ◦  1,1
in which local depolarizing channels
A¢
A¢
A
A
{1,1, K, 1, k} and {1,1, K, 1, l } act on subsystems A¢ and A, respectively, such that the overall channel on A=
A¢
A¢
A
A
A¢A is (1,Ak¢ ◦  1,Ak¢ ... 1,1
◦  1,1
) Ä (1,Al ◦  1,Al ... 1,1
◦  1,1
).
The following corollary follows from theorem 2 and is analogous to corollary 1.
Corollary 4. The cost functions CHST and CLHST exhibit strong-OPR to the following noise model: (1) all noise
processes in Noise Model 2, as well as (2) a noise process during the implementation of
 = k ◦  ◦ 1 =  † ◦  (i.e. in the time interval between t1 and t2) in which global non-unital Pauli
A
A
A
A
, K,  NU,
channels { NU,1
k} act on system A such that the overall channel on A is  NU, k ◦ k  ◦  NU,1 ◦ 1,
provided that the following condition is satisﬁed:
A
A
A
( NU,
k ◦  k  ◦  NU,1◦1)(·) = ( k ◦ k - 1  1◦ NU)(·) ,

(19)

 NU is also a non-unital Pauli channel.
where 
A

Finally, we present a simple corollary of theorem 1 based on the ricochet property of the standard Bell state.
Note that the noise model in the following corollary is fairly simple but nonetheless physically distinct from
those considered in ﬁgure 3, since it allows for global non-unital Pauli noise to occur during the implementation
of W.
Corollary 5. The cost functions CHST exhibits strong-OPR to the following noise model: (1) global depolarizing noise
acting continuously throughout the circuit, (2) global non-unital Pauli noise on system A at a ﬁxed time in between t1
and t2.
5.2. Noise resilience of ﬁxed input state compiling
Let us now consider ﬁxed input state compiling (FISC). Recall that the cost-evaluation circuits, shown in
ﬁgure 2, have less structure than the circuits in ﬁgure 1. As a result, the noise model that we consider in the FISC
case is simpler than the previously considered noise models. In particular, we deﬁne the following noise model,
which is depicted in ﬁgure 4. Note that, in this context, τ1 is deﬁned as the time just before the application of
V †U , and there is no need to consider a noisy quantum channel occurring after V †U since the measurement
occurs immediately after V †U .
8

New J. Phys. 22 (2020) 043006

K Sharma et al

Figure 4. Schematic diagram of Noise Model 3 of deﬁnition 9 for: (a) the LET circuit, and (b) the LLET circuit. Global depolarizing
noise (DN) acts continuously throughout the circuit, global Pauli noise (PN) acts at time τ1, and measurement noise (MN) occurs
during readout.

Deﬁnition 9. We deﬁne Noise Model 3 to be the following noise process during the LET or the LLET: (1) global
depolarizing noise acting continuously throughout the circuit, (2) global Pauli noise acting at time t1, and (3)
measurement noise.
We now state our main result for FISC, which is proven in appendix F.
Theorem 3. The cost functions CLET and CLLET exhibit weak-OPR, as deﬁned in deﬁnition 6, to Noise Model 3 in
deﬁnition 9.
This theorem implies that FISC is resilient to the measurement noise model in deﬁnition 5. Furthermore, it
is resilient to Pauli noise acting at τ1 and global depolarizing noise acting continuously throughout the circuit.
We remark that while FUMC exhibits strong-OPR for the noise models considered (see the previous
section), here FISC exhibits weak-OPR instead. The latter arises from the fact that the optimal set of unitaries
 dopt for FISC can be highly degenerate (i.e. can contain many unitaries) and the presence of noise could in
general break such degeneracy. The ‘weak’ term in weak-OPR is simply the fact that the number of global optima
is possibly reduced by noise, not that the noise resilience itself is weak. Hence, weak-OPR should still be viewed
as noise resilience, since the global optima in the presence of noise correspond to global optima in the noiseless
case. This implies that training in the presence of noise will lead one to ﬁnd the correct optimal parameters
for V (a).
Under certain conditions, theorem 3 implies that C ¢ (q ) deﬁned in (14) will also exhibit weak-OPR to Noise
opt
opt
Model 3. Let  d,
LET and  d, LLET denote the sets of unitaries that optimize CLET and CLLET , respectively. In the
~opt
opt
opt
absence of noise we have  dopt
, LET =  d , LLET , while in the presence of noise, theorem 3 implies  d , LET Í  d , LET
opt
opt
~opt
~
~
and  d, LLET Í  dopt
, LLET . Hence, if  d , LET Ç  d , LLET ¹ Æ, then for any value of q, C ¢ (q ) = qCLET + (1 - q ) CLLET
will also exhibit weak-OPR to Noise Model 3, where the unitaries that optimize C ¢ (q ) in the noisy case belong
~opt
~opt
to  d, LET Ç  d, LLET .
Theorem 3 implies the following corollaries, which establish resilience to noise models that go beyond Noise
Model3 at the expense of specializing the form of W. Note that these corollaries are analogous to Corollaries 1–3,
and corollary 6 implies Corollaries 7 and 8. See appendix G for the proofs.
Corollary 6. The cost functions CLET and CLLET exhibit weak-OPR to a noise model that includes the following: (1) all
noise processes in Noise Model 3, as well as (2) a noise process during the implementation of  = k ◦  ◦ 1 =
 † ◦  in which global Pauli channels {1, K, k} act, such that the overall channel is k ◦ k  ◦ 1 ◦ 1,
provided that the following condition is satisﬁed:
)(·) ,
(k ◦  k  ◦ 1 ◦ 1)(·) = ( k ◦  k - 1  ◦ 1 ◦ 

(20)

 is also a Pauli channel.
where 

Corollary 7. Let the W = V †U gate sequence have the form W = W2A W1A with W1A composed only of Clifford gates.
Then the cost functions CLET and CLLET exhibit weak-OPR to a noise model that includes the following: (1) all noise
processes in Noise Model 3, as well as (2) a noise process during the implementation of  1A = 1, k ◦  ◦ 1,1, in
which global Pauli channels {1A , K,  kA} act on system A, such that the overall channel on A
is  kA ◦ 1, k  ◦ 1A◦1,1.

9

New J. Phys. 22 (2020) 043006

K Sharma et al

Figure 5. Quantum circuits for: (a) Toffoli Gate, (b) three-qubit quantum Fourier transform, and (c) three-qubit W-state preparation.
m
Here, Rm stands for the controlled phase gate with a phase shift of f = e 2p i 2 , and Vk (bk ) is given by (21). For the three-qubit
W-state preparation circuit we have b1 = (2arccos( 1 3 ), 0, 0) and b 2 = (p 2, 0, 0).

Figure 6. (a) The dressed CNOT is composed of a CNOT preceded and followed by single-qubit gates Vk (ak ), where Vk (ak ) is given
by(21). (b) Two layers of the alternating-pair ansatz in the case of four qubits. Each layer is composed of dressed CNOTs acting on
alternating pairs of neighboring qubits. (c) Schematic representation of the target-inspired ansatz. In this approach, the gate sequence
of dressed CNOTs is obtained from the gate sequence of the target unitary U.

Corollary 8. Let the W = V †U gate sequence have the form W = W2A W1A with W1A = W1A ¢ Ä W1A  being a tensor
product, i.e. W is a tensor product up to a particular time. Then the cost functions CLET and CLLET exhibit weak-OPR
to a noise model that includes the following: (1) all noise processes in Noise Model 3, as well as (2) a noise process
A¢
A
during the implementations of  1A ¢ =  1,Ak¢ ◦  ◦  1,1
and  1A  =  1,Al ◦  ◦  1,1
in which local
A¢
A¢
A
A
depolarizing channels {1,1, K, 1, k} and {1,1, K, 1, l } act on subsystems A¢ and A , respectively, such that the
A¢
A¢
A
A
overall channel on A = A¢A is (1,Ak¢ ◦  1,Ak¢ ... 1,1
◦  1,1
) Ä (1,Al ◦  1,Al ... 1,1
◦  1,1
).

6. Implementations
In this section, we present the results of implementing VQC on the following three-qubit unitaries: the Toffoli
gate, the three-qubit quantum Fourier transform (QFT), and a W-state preparation circuit. Each of these
unitaries is of interest, e.g. the Toffoli gate when combined with the Hadamard gate provides a universal gate set
for quantum computing [35], the QFT is a subroutine in Shor’s algorithm [36], and W-state preparation is useful
for the quantum approximate optimization algorithm [37, 9]. Figure 5 shows gate sequences corresponding to
these unitaries obtained from the literature. The Toffoli gate in ﬁgure 5(a) is decomposed into a gate sequence
that contains nine one-qubit gates and six CNOTs [38]. For the QFT we employ its textbook circuit [33] in
ﬁgure 5(b), while the circuit for W-state preparation in ﬁgure 5(c) was derived from [39, 40].
Our VQC implementations were performed using IBM’s noisy quantum simulator [28] with a noise model
built from the reported noise parameters and connectivity of IBM’s 14-qubit Melbourne quantum computer
[41]. We remark that for VQC, we must have a target unitary U that is written as a gate sequence in the native gate
language and the native connectivity of the hardware. IBM’s simulator for the Melbourne device has a square
lattice connectivity and native gate alphabet of CNOTs, arbitrary rotation around Z and p 2 rotation around X.
Hence, transforming the gate sequences in ﬁgure 5 for the native device will typically add an overhead of
additional gates. Therefore, the target gate sequences in our implementations actually correspond to IBM’s
compilation (with this overhead included) of the circuits in ﬁgure 5.
In IBM’s noise model [28, 42], one-qubit gate errors are modeled as a single-qubit depolarizing error
followed by a thermal relaxation error, where thermal relaxation refers to both T1 and T2 channels. Similarly,
two-qubit gate errors consist of a two-qubit depolarizing error followed by single-qubit thermal relaxation
errors on each qubit. Finally, the noise model includes single-qubit readout errors.
We employ two different ansatzes, shown in ﬁgure 6, and (as described below) we employ gradient-based
optimization algorithms to train the gate sequence V (a). In ﬁgures 7–8, we plot the results of implementing
VQC with IBM’s noisy simulator for the three-qubit gates in ﬁgure 5. In each plot, we show the value of the noisy
cost functions versus the number of iterations of the optimization algorithm. Additionally, we plot the
corresponding value of the noiseless cost functions evaluated for the variational parameters a obtained from the
10

New J. Phys. 22 (2020) 043006

K Sharma et al

Figure 7. VQC implementations for the Toffoli gate (top) and three-qubit QFT (bottom). The ansatz for V (a) is: (a) one layer of the
alternating-pair ansatz, (b) two layers of the alternating-pair ansatz, (c) the target-inspired ansatz. The blue and green curves
LHST obtained by training V (a) in the presence of noise. The green and pink curves
HST and C
respectively plot the values of C
respectively plot the values of CHST and CLHST evaluated at the variational parameters a obtained from the noisy optimization of
V (a) . Curves are plotted as a function of the number of iterations in the gradient-descent algorithm, and the y-axis is in log-scale. The
blue and red dashed lines in (a) and (b) correspond to the minimum value of CHST and CLHST , respectively, determined by optimizing
V (a) in a noise-free environment. Top: in both (a) and (b), the green and pink curves converge to the dashed blue and red lines,
respectively. Bottom: While in (a) the green and pink curves converge to the dashed lines, in (b) the termination condition for the
optimization algorithm was reached before the pink curve could achieve convergence. The number of shots per iteration was
N=50 000 for (a) and (b). For (c) we employed the iCANS optimizer [44], where the total number of shots was 1.4 ´ 107 and the
minimum number of shots per iteration was initially Nmin = 2. The thick dashed vertical line in (c) indicates the point where we set
Nmin = 250 , which helped to further reduce the cost function.

Figure 8. VQC implementations for the three-qubit W-state preparation circuit for (a) the FUMC approach, and (b) the FISC
approach. The trainable gate sequence V (a) is given by the target-inspired ansatz. In the left (right) panel the blue and green curves
LET ) and C
LLET ) obtained by noisy training of V (a) . Similarly, in the left (right) panel
LHST (C
HST (C
plot respectively the values of C
LET ) and CLHST (C
LLET ) evaluated at the variational parameters a
the green and pink curves give respectively the values of CHST (C
obtained from the noisy optimization of V (a) . Curves are plotted as a function of the number of gradient-descent iterations, with the
y-axis in log-scale. Via noisy training, the noiseless cost functions go down to ~10-4 . Initially we set Nmin = 2, and the thick dashed
vertical lines shows the point where we increased this value to Nmin = 250. Increasing the minimum number of shots iCANS employs
to compute each partial derivative leads to smaller cost function values in both cases.

noisy optimization. These results allow us to verify if the parameters obtained from the noisy optimization are
indeed minimizing the noiseless cost functions. Before discussing the results, we ﬁrst give details for our ansatzes
and optimization methods.
6.1. Ansatzes and optimization methods
As previously mentioned, to implement VQC we consider two ansatzes for the trainable unitary V (a). The
building block of our ansatzes is a dressed CNOT gate, which is a two-qubit gate composed of a CNOT preceded
11

New J. Phys. 22 (2020) 043006

K Sharma et al

and followed by single-qubit gates Vk (ak ) acting on each qubit, as shown in ﬁgure 6(a). Each single-qubit gate
Vk (ak ) is decomposed (up to a global phase) into three elementary rotations parameterized by three angles in the
vector ak = (ak,1, ak,2, ak,3) as
Vk (ak) = e-iak,3sz 2e-iak,2sy 2e-iak,1sz 2.

(21)

Let us now introduce our ansatzes. We note that our two ansatzes are fairly similar to the ones introduced in
[19]. In our ﬁrst ansatz, each layer is composed of n dressed CNOTs, where n is the number of qubits (in the
special case of n = 2 each layer consists of one dressed CNOT), with the precise structure deﬁned as follows.
Deﬁnition 10. We deﬁne the alternating-pair ansatz as a layered ansatz in which each layer consists of
(parameterized) dressed CNOT gates acting on alternating pairs of neighboring qubits as illustrated in
ﬁgure 6(b).
We remark that it is useful to distinguish between a complete ansatz, in which an exact compilation for U is
contained inside the ansatz, versus an incomplete ansatz, where exact compilation is not possible. In general, a
small number of layers can lead to an incomplete ansatz, where one can only reach approximate compilation.
Hence, increasing the number of layers l could allow one to obtain better compilations of U. Note however that
while a large number of layers can achieve a complete ansatz, it can also be harder to train and can lead to a
longer-depth circuit.
The alternating-pair ansatz may not lead to the optimal depth compilation for U, particularly in the
complete ansatz case. Our second ansatz attempts to ﬁx the issue of introducing unnecessary depth by having a
structure that depends on U.
Deﬁnition 11. We construct the target-inspired ansatz by taking the gate sequence for the target unitary U ,
expanding this gate sequence into single-qubit gates and CNOTs, removing all single-qubit gates that precede or
follow a CNOT, and replacing each remaining CNOT in the gate sequence with a (parameterized) dressed
CNOT. Finally, each remaining single-qubit gate is replaced by a parametrized single-qubit gate.
As schematically depicted in ﬁgure 6(c), each layer is now composed of one dressed CNOT. This ansatz will
always be complete since its structure is inspired by U. While this ansatz is not useful to compress the number of
CNOTs in V (a), it is useful as a proof-of-concept to demonstrate OPR for complete ansatzes. We remark that a
simple modiﬁcation of this ansatz, where the placements of the dressed CNOTs are optimized over instead of
ﬁxed, would actually be useful for circuit-depth compression. Furthermore, we have implemented this dressed
CNOT placement optimization, and we ﬁnd that we obtain similar noise resilience results as those for the targetinspired ansatz.
Let us now discuss the optimization methods. As previously mentioned, the trainable gate sequence V (a) is
a function of a set of parameters a corresponding to the collection of the internal gate angles in each dressed
CNOT. To optimize these parameters, we employ a gradient-descent approach. This approach exploits the fact
that the gradient with respect to a of CHST , CLHST , CLET , and CLLET can be computed by using the circuits for
HST, LHST, LET, and LLET, respectively [43, 19]. We remark that we used different gradient-based approaches
for the shallow and deep ansatz cases, since the latter requires a more sophisticated and efﬁcient optimizer.
Speciﬁcally, for the shallow ansatz cases where there are few parameters, we employ the simple gradientbased approach outlined in [19, appendix 4] . In this approach, the number of shots N per iteration is ﬁxed. (We
choose N=50 000.) On the other hand, for deep ansatzes with larger numbers of parameters, we employ a
more sophisticated gradient-based approach that improves efﬁciency by reducing the number of shots required
[44]. This approach is the individual coupled adaptive number of shots (iCANS) algorithm of [44], which is a
measurement-frugal method that often outperforms other optimizers in the presence of noise. The iCANS
optimizer frugally adjusts the number of shots both for a given iteration and for a given partial derivative in a
stochastic gradient descent. When employing iCANS, one sets as input: (1) the total number of shots employed
during the optimization, and (2) the minimum number of shots (denoted Nmin) employed to estimate the
gradient for a given iteration. We set the latter to initially be Nmin=2 and then later increase this to Nmin=250,
which empirically leads to good convergence.
6.2. Toffoli gate
The top panels in ﬁgure 7 show results of implementing VQC for the Toffoli gate. Figure 7 (top, a) corresponds
to V (a) being given by a single layer of the alternating-pair ansatz of deﬁnition 10. Here, the noisy cost
LHST (blue and red curve, respectively) tend to decrease as the number of iterations
HST and C
functions C
HST
increases and converge to non-zero values. We remark that the number of iterations can be different for C
12

New J. Phys. 22 (2020) 043006

K Sharma et al

LHST since the termination condition of the optimization algorithm can be reached for a different number
and C
of iterations.
Figure 7 (top, a) also depicts the cost functions CHST and CLHST evaluated for the variational parameters a
obtained from the noisy optimization (green and pink curve, respectively). These curves show that as the
number of iterations increases, both CHST and CLHST tend to decrease too, indicating that the noisy training is
indirectly training the noiseless cost functions, i.e. the adjustments to the parameters a made by noisy training are
reducing the noiseless cost functions. Note that CHST and CLHST do not converge to zero since a single layer of
three dressed CNOTs forms an incomplete ansatz for the Toffoli gate.
In order to determine if the algorithm is reaching the minimum value achievable with just one layer, we have
also implemented VQC to compile the Toffoli gate in a noise-free simulation. The minimum values achieved for
CHST and CLHST are shown as a blue and red dashed curve, respectively. Surprisingly, the cost functions
evaluated with the parameters from the noisy training (green and pink curves) converge to the dashed lines. This
suggests that the optimal parameters are noise resilient since noisy training reaches the minimum value obtained
by noise-free training. As a caveat, however, we note that it is not clear whether the minima reached are global or
local optima.
Figure 7 (top, b) plots the VQC results for Toffoli with V (a) given by two layers of the alternating-pair
ansatz. In this case, CHST and CLHST converge to values which are smaller than the ones obtained in the one-layer
case. The latter indicates that two layers allow for a more complete compilation of the Toffoli gate, albeit it
appears that the ansatz is not yet complete. Note that both the decomposition of the Toffoli gate in ﬁgure 5, as
well as two layers of the alternating-pair ansatz, consist of six CNOTs. However, the placement of the dressed
CNOTs does not seem to be optimal. Finally, let us remark that the green and pink curves converge to the dashed
blue and red lines, respectively. Hence, this once again shows that the optimal parameters are noise resilient.
Similar to the previous case, it is not clear whether the minima reached are global or local minima.
Figure 7 (top, c) shows results for the target-inspired ansatz of deﬁnition 11. As the number of iterations
increases, all curves tend to decrease, with the green and pink curves converging to values of the order of 10−4.
We remark that we have veriﬁed that W = V †U »  for the parameters obtained. In this case, we do not plot
dashed blue and red curves since the ansatz is complete and the minimum of the noiseless cost functions is zero.
These results indicate that optimizing V (a) in the presence of noise yields the correct variational
parameters a, which minimize the noiseless cost function. Hence, both CHST and CLHST appear to exhibit OPR
for the realistic noise model considered.

6.3. Quantum Fourier transform
We now discuss the VQC results for the three-qubit QFT. Figure 7 shows the results for V (a) consisting of: a
single layer of the alternating-pair ansatz of deﬁnition 10 (bottom, a), two layers of the alternating-pair ansatz
(bottom, b), and the target-inspired ansatz of deﬁnition 11 (bottom, c). As shown in these plots, most of the
results for QFT are similar to the results for the Toffoli gate. In all cases the noiseless cost functions tended to
decrease with iterations, indicating that noisy training indirectly trains the noiseless costs.
For the one-layer case of ﬁgure 7 (bottom, a) the green and pink curves (noiseless cost functions evaluated at
the parameters obtained from noisy training) converge to the value obtained by training in a noise-free
environment (dashed curve). Here, the non-zero value of the dashed curve indicates that a one-layer ansatz is
incomplete. This is in contrast to ﬁgure 7 (bottom, b), where the dashed red line of CLHST is of the order of 10−4,
implying that the ansatz is complete. Once again, in ﬁgure 7 (bottom, b), the green and pink curves
approximately converge to the dashed lines (noiseless training), indicating noise resilience. Finally, ﬁgure 7
(bottom, c), shows that that both CHST and CLHST appear to exhibit OPR, as we can indirectly train the
parameters in V (a) in the presence of noise.

6.4. W-state preparation
Finally, we discuss the results of implementing of VQC for both FUMC and FISC of a W-state preparation
circuit. We remark here that we did not perform FISC for the Toffoli gate and the QFT since those unitaries act
trivially on the ∣0ñ state. Moreover, we are only interested in comparing the FUMC and the FISC approach with a
complete ansatz, meaning that we only considered the target-inspired ansatz of deﬁnition 11.
As shown in ﬁgure 8, all cost functions CHST , CLHST , CLET , and CLLET can be optimized indirectly via noisy
training of V (a). Both for FUMC and FISC the cost functions go down to ~10-4 , while for FUMC one can even
reach values of ~10-5 when employing the LHST. Hence, our numerics indicate that CHST , CLHST , CLET , and
CLLET appear to exhibit OPR to IBM’s realistic noise model.
13

New J. Phys. 22 (2020) 043006

K Sharma et al

7. Discussion
7.1. VQC in the NISQ era
Our analytical and numerical results suggest that variational quantum compiling (VQC) could be a useful tool
for near-term noisy quantum computing. While there are several intended uses for VQC [19], the main purpose
is for circuit-depth compression of quantum algorithms. This depth compression arises because VQC could
achieve optimal compiling, whereas classical methods for quantum compiling either scale exponentially (if they
are aiming at optimal compiling) or are sub-optimal when they are restricted to local (instead of global)
compiling of the circuit.
Suppose one is able to achieve depth compression with VQC. This implies that the target unitary U has a
longer depth than the trained gate sequence V (a). Prior to our work, one may have been concerned that this
depth compression might not reduce noise, because perhaps the noise occurring during U is somehow compiled
into the gate sequence V (a). However, our work shows that this is not the case. Despite various sources of
incoherent noise (e.g. see the noise model in ﬁgure 3), we ﬁnd that one learns the correct optimal parameters a
for V (a). This means that, after performing VQC, if one was to implement the gate sequence V (a) instead of
U, then one should see that V (a) really does achieve less noise than U, since the depth of V (a) is shorter.
7.2. Summary of results
In this work, we treated two different forms of VQC: Full Unitary Matrix Compiling (FUMC) and Fixed Input
State Compiling (FISC). Our main analytical results were stated in theorems 1–3. We found that both FUMC
and FISC are resilient to measurement noise. In addition, they are both resilient to global depolarizing noise
acting continuously throughout the circuit and global Pauli noise occurring just prior to the implementation
of W = V †U .
For FUMC, we were able to prove resilience to additional sources of noise, such as Pauli gate noise during the
entangling and disentangling gates as well as non-unital Pauli noise occurring at particular times in the circuit.
The fact that our noise resilience results are more extensive for FUMC than for FISC may simply be due to the
fact that the cost-evaluation circuit for FUMC is more complicated than that for FISC. Hence it is possible that
this additional resilience is needed to make the two approaches have similar levels of noise resilience.
Alternatively, it could be possible that either FUMC or FISC is more noise resilient than the other, although this
remains to be established. (Note that our numerics did not see a signiﬁcant difference in the noise resilience of
FUMC versus FISC.)
In addition, Corollaries 1–8 stated resilience results for noise models that go beyond the noise models
considered in theorems 1–3, at the expense of possibly specializing the form of the unitary W = V †U (for
example, to Clifford unitaries or tensor-product unitaries). In particular, these corollaries considered noise that
occurs during the implementation of W, which is certainly practically relevant.
Our numerical results were presented in ﬁgures 7–8. Generally speaking, these numerics agreed with our
theoretical expectations and hinted at resilience beyond what is stated in our theorems, which we discuss in the
next subsection. We emphasize that our implementations employed the noise model of IBM’s 14-qubit
Melbourne device, and hence this shows that VQC exhibits resilience for currently available hardware.
7.3. Noise resilience beyond our theorems
There are two senses in which VQC might exhibit resilience beyond the results stated in our theorems. The ﬁrst
sense is that VQC may be resilient to more general noise models than the ones we considered. The second sense
is that VQC may be resilient even for the incomplete ansatz case, on which we elaborate below. Both of these
possibilities appear to be supported by our numerical implementations.
For evidence supporting the idea that VQC may be resilient to more general noise models, consider the
following. The noise model associated with IBM’s 14-qubit Melbourne device is more general than the noise
models depicted in ﬁgures 3 and 4, and the unitaries we considered in ﬁgure 5 do not fall into the special cases
(e.g. Clifford or tensor product) treated by Corollaries 1–8. For example, IBM’s noise model has non-unital
Pauli noise associated with each gate and hence occurring throughout the implementation of W = V †U . Thus,
our theorems and corollaries do not cover all of noise processes occurring in IBM’s noise model. Despite this, we
were able to reduce the noiseless cost (via noisy training) to ~10-4 for the Toffoli gate (ﬁgure 7 (top, c)) and QFT
(ﬁgure 7 (bottom, c)), and to ~10-5 for W state preparation (ﬁgure 8).
Naturally, our theorems and corollaries have a bias towards noise models that are mathematically easy to
work with, such as Pauli noise or depolarizing noise, since this makes it easier to formulate proofs. It is therefore
important for future work to attempt to show resilience beyond these noise models.
As noted above, VQC may also have resilience beyond the complete ansatz case. Recall that we say an ansatz
for V (a) is complete (incomplete) if it contains (does not contain) an exact compilation of U. Our theorems and
corollaries are restricted to the complete ansatz case, whereas our numerics in ﬁgure 7 also consider the
14

New J. Phys. 22 (2020) 043006

K Sharma et al

incomplete ansatz case. Interestingly, ﬁgure 7 showed that typically one can obtain the same value for the
noiseless cost with either noisy or noiseless training. This surprising result suggests that perhaps the optimal
values for a may be resilient to noise even for the incomplete ansatz case, and future work should investigate this
possibility.
In addition, it will be important to investigate the effect of noise on the parameter landscape and parameter
trainability(e.g. [45]). Our work indicates that the global optimum of VQC may not change with noise, but does
not address the difﬁculty of ﬁnding this optimum.
7.4. Coherent versus incoherent noise
In the Introduction, we emphasized the distinction between OPR and cost value resilience [7]. The latter is
relevant to coherent noise, whereas OPR is relevant to incoherent noise. Intuitively, we anticipate that coherent
noise (e.g. systematic gate biases) in VQC will often shift the location of the global minimum in parameter space,
and hence we expect coherent noise to have a non-trivial effect on the optimal parameters in VQC. Because of
this intuition, we have focused our paper and our deﬁnition of OPR solely on incoherent noise. We remark that
our deﬁnition of OPR, which is stated in terms of unitaries (rather than parameters), would need to be modiﬁed
if one is interested in studying parameter resilience for coherent noise. However, as noted, we do not anticipate
resilience to coherent noise to hold. We also remark that other strategies exist to correct coherent noise [46].
Nevertheless, an interesting question for future work will be see whether OPR holds partially whenever both
coherent and incoherent noise are present. In addition, it will be interesting to combine the ideas of OPR and
cost value resilience into a single framework.
7.5. Noise resilience of VQE
Finally, let us consider VHQCAs more generally. In particular, let us revisit the variational quantum eigensolver
(VQE) that we discussed in section 2. As we now show, VQC is a special case of VQE. This idea was noted for
FISC in [20]. However, the argument is more subtle for the FUMC case.
The key observation is that the various cost functions can be rewritten as the expectation values for some
effective Hamiltonians:
CLET = áy (a)∣HLET∣y (a)ñ ,
CHST = ác (a)∣HHST∣c (a)ñ ,

CLLET = áy (a)∣HLLET∣y (a)ñ ,
CLHST = ác (a)∣HLHST∣c (a)ñ.

(22)

Here ∣y (a)ñ Î A and ∣c (a)ñ Î AB are n-qubit and 2n -qubit states, respectively, given by
∣y (a)ñ = V (a)∣0ñ ,

∣c (a)ñ = (V (a) Ä B)∣Fñ ,

(23)

where X denotes the Hilbert space of system X, and ∣Fñ = E∣0ñ is the standard maximally entangled state on
AB. We remark that ∣c (a)ñ is simply the Choi state associated with V (a).
For the cost functions associated with FISC, the effective Hamiltonians are given by
HLET =  A - U ∣0ñá0∣U †,

HLLET =  A -

1 n
A
U (P0 j Ä  A j) U †,
å
n j=1

(24)

A

where P0 j is the projector onto the zero state of Aj. For the cost functions associated with FUMC, the effective
Hamiltonians are given by
HHST =  AB - (U Ä B)∣FñáF∣(U † Ä B) ,
1
HLHST =  AB - å nj = 1 (U Ä B)(∣F( j )ñáF( j ) ∣ Ä  A j B j)(U † Ä B) ,
n

(25)

where ∣F( j)ñ is the standard maximally entangled state on Aj Bj . With these Hamiltonians, one can verify that the
expressions in (22) are equal to the original cost function deﬁnitions in section 3. Hence, we have just shown that
VQC is a special case of VQE, where the goal is to prepare the ground state of one of the Hamiltonians in (24)
or (25).
The fact that VQC is a special case of VQE implies that, for speciﬁc Hamiltonians, VQE is noise resilient.
Namely, we have shown that VQE exhibits OPR when the Hamiltonian has the form in either (24) or (25). This
naturally points to the question of whether VQE is resilient more generally. It is therefore a very interesting
direction for future research to extend our noise resilience to Hamiltonians other than the ones we considered.

8. Conclusions
In this work, we discovered a novel kind of noise resilience for variational hybrid quantum-classical algorithms
(VHQCAs). We introduced the idea of optimal parameter resilience (OPR), where the variational parameters
corresponding to the global optimum are unaffected by various types of incoherent noise. We showed that
15

New J. Phys. 22 (2020) 043006

K Sharma et al

variational quantum compiling (VQC) exhibits OPR. This paves the way for VQC to be used in the era of noisy
intermediate-scale quantum computing as a tool for circuit-depth compression. Important future research
directions include: (1) extending our theorems to show resilience to more general noise models than the ones we
considered (which our numerics suggest may be possible), (2) exploring noise resilience for the incomplete
ansatz case (which our numerics indicate may also be resilient), (3) analyzing approximate noise resilience, (4)
studying the effect of noise on the parameter training process, and (5) generalizing our resilience results to other
Hamiltonians for the variational quantum eigensolver and exploring resilience for other VHQCAs (for example,
some evidence of noise resilience was recently reported in [47]).

Acknowledgments
We thank Lukasz Cincio and Mark M Wilde for helpful discussions. KS acknowledges support from the US
Department of Energy (DOE) through a quantum computing program sponsored by the LANL Information
Science & Technology Institute. SK acknowledges support from the National Science Foundation and the
National Science and Engineering Research Council of Canada Postgraduate Scholarship. MC was supported by
the Center for Nonlinear Studies at Los Alamos National Laboratory (LANL). PJC acknowledges support from
the LANL ASC Beyond Moore’s Law project. MC and PJC also acknowledge support from the LDRD program at
LANL. This work was also supported by the US DOE, Ofﬁce of Science, Ofﬁce of Advanced Scientiﬁc
Computing Research.

Appendix A. Preliminaries
The main goal of the appendix is to provide the proofs of theorems 1–3 and Corollaries 1–8. For these proofs, we
will need to ﬁrst review some deﬁnitions and properties. We point readers to [33, 34] for additional background.
Pauli Basis. In our proofs, we will work in the Pauli product basis, involving a tensor product of one-qubit
Pauli operators. This is a natural basis to choose, given the qubit structure of quantum computers. Let
X l := s lx1 Ä s lx2 Ä  Ä s lxn,

Z k := s kz1 Ä s kz 2 Ä  Ä s kz n,

(A1)

where l1, l2, ¼, l n Î {0, 1}, k1, k2, ¼, k n Î {0, 1}, l = (l1, K, l n), and k = (k1, K k n). The following properties
are satisﬁed by the Pauli operators:
X l1 X l 2 = X l1Å l 2 ,

Z k1 Z k 2 = Z k1Å k 2,

X l Z k = ( - 1)l·k Z kX l ,

Tr[X l Z k ] = 2ndl , 0, dk, 0,

(A2)

which follow from the properties of the single-qubit Pauli operators.
Pauli group. The Pauli group of n qubits is n :={1, i} ´ {I , sx , sy , sz}Än .
Clifford group. The Clifford group on n qubits is the set of unitaries that normalize the Pauli group, i.e.
n :={U : U n U † Î n}.

Maximally entangled states. In what follows, we consider the following maximally entangled states
∣F+ñáF+∣ = ∣f+ñáf+∣Än, where ∣f+ñ = (∣0, 0ñ + ∣1, 1ñ) 2 . The aforementioned tensor product of
maximally entangled states can be written in the Pauli basis as follows:
1
1
∣F+ñáF+∣AB = 2n å XAl Z Ak Ä XBl ZBk = 2n å Z Ak XAl Ä ZBk XBl .
2 l,k
2 l,k

(A3)

(A4)

All-zero state. Noting that ∣0ñá0∣ = ( + sz ) 2, then in the Pauli basis the all-zero state ∣0ñá0∣ = ∣0ñá0∣Än is
1
1
∣0ñá0∣ = n ( + sz )Än = n å Z l .
(A5)
2
2 l
Pauli channels. A Pauli noise channel corresponds to the action of random Pauli operators on a quantum
state ρ according to a probability distribution. Let  A denote an n-qubit Pauli channel acting on system A=A1,
...An. Then the action of  A on the state ρ is given by
 A(r ) = å plA, k XAl Z Ak r (XAl Z Ak )† ,

(A6)

l,k

where 0  plA, k  1, and ål, kplA, k = 1. Using the properties in (A2), we ﬁnd that
 A(XAa Z Ab ) = å plA, k XAl Z Ak XAa Z Ab Z Ak XAl = å ( - 1)a·k ( - 1)b·l plA, k XAa Z Ab = paA, b XAa Z Ab ,
l,k

(A7)

l,k

where paA, b :=ål, k (-1)a·k (-1)b·l plA, k and -1  paA, b  1 for all a, b Î {0, 1} n. Similarly, the action of a global
Pauli channel  AB acting on systems A = A1  An and B = B1  Bn , respectively, is deﬁned as
16

New J. Phys. 22 (2020) 043006

K Sharma et al

 AB (X Aa1 Z Ab1 Ä XBa 2 ZBb2) = paAB
X Aa1 Z Ab1 Ä XBa 2 ZBb2.
1, a 2, b1, b 2

(A8)

Non-unital Pauli noise channels. The action of a non-unital Pauli channel NU on an n-qubit Pauli
operators is
 NU(X aZ b) = c a, bX aZ b

" a ¹ 0, b ¹ 0,

(A9)

å

(A10)

 NU(X 0Z 0) =  NU() =  +

d a, bX aZ b.

(a, b ) ¹ (0, 0)

We now prove the following lemma based on Clifford unitaries and Pauli channels.
Lemma 1. Let W be a Clifford unitary and let  be a Pauli channel. Then for any state ρ, the following holds:
( ◦ )(r ) = ( ◦  )(r ) ,

(A11)

⎛
⎞
◦ (r ) = W ⎜⎜å pl , k X l Z krZ kX l ⎟⎟ W † = å pl , k (WX lZ kW †)(WrW †)(WZ kX l W †)
⎝ l,k
⎠
l,k

(A12)

where  is another Pauli channel.
Proof. From (A6) it follows that

= å pl , k X m (l , k ) Z n (l , k ) WrW †Z n (l , k ) X m (l , k )

(A13)

l,k

= ( ◦  )(r ).

(A14)

The third equality follows from the deﬁnition of a Clifford unitary (A3), while the last equality follows from
(A6).

,

Appendix B. Noisy entangling and disentangling gates in FUMC
For the proofs given in appendices D–G, we will make use of some properties of the noisy versions of entangling
E and disentangling E † gates that appear in FUMC. Hence, it is helpful to ﬁrst state these properties in this
appendix. Recall that, for Pauli gate noise acting during E or E †, we assume that global Pauli channels act before
and after each Hadamard, as well as before and after each CNOT. This noise model incorporates the case when
there could be correlated Pauli noise acting on different qubits during E and E †. We note that the noisy
entangling gate is the same for both the HST and the LHST.
Let E=E AB denote the ideal entangling gate, which can be split into a tensor product of two qubit
entangling gates E Aj Bj as
n

E AB = E A1 B1 Ä E A2 B2 Ä  Ä E An Bn = ⨂ E A j B j.

(B1)

j=1

Moreover, each E Aj Bj consists of a Hadamard gate acting on Aj followed by a CNOT gate acting on both Aj and Bj.
In the quantum channel notation we write this as  Aj Bj =  XAj Bj ◦ ( Aj Ä  Bj), where  Aj are the quantum
channels that implement the Hadamard gates and  XAj Bj are the quantum channels that implement the CNOTs.
AB
The noisy version of AB , which we denote by  , is
n

n

j=1

j=1

AB
A j Bj
A j Ä  B j ) ◦  AB ,
 := ⨂ AB
◦ ⨂  AB
j ◦ X
j ◦ (
j

(B2)

AB
AB
where  AB
j ,  j , and  j are 2n -qubit global Pauli channels for all i Î {1 ,..., n}, as deﬁned in (A8). Since both
Hadamard and CNOT gates are Clifford unitaries, by using lemma 1 we ﬁnd that
n

n

j=1

j=1

AB
AB
 := AB ◦ ⨂  X j j ◦ ⨂ ( A j Ä  B j) ,

(B3)

where AB is another Pauli channel.
AB
We now apply  on the all-zeros state ∣0, 0ñá0, 0∣AB . Consider the following chain of equalities:
⎛
⎞
1
AB
AB 1
a b
a b
 (∣0 , 0ñá0 , 0∣AB ) =  ⎜⎜ 2n å Z Aa Ä ZBb⎟⎟ = 2n å maAB
, a, b, b X A Z A Ä XB ZB ,
2 a, b
⎝ 2 a, b
⎠

17

(B4)

New J. Phys. 22 (2020) 043006

K Sharma et al

where we used (A5), (A8), and the following identities for all jä{1, Kn}:
a

b

a

b

AB

a

a

AB

a

( A j Ä  B j)(Z Ajj Ä Z B jj ) = X Ajj Ä Z B jj , ( X j j)(X Ajj Ä B)
b

b

b

= X Ajj Ä X B jj , ( X j j)( A j Ä Z B jj ) = Z Ajj Ä Z B jj .

(B5)

The noisy disentangling channel for the HST is given by the adjoint of the noisy entangling channel, as
deﬁned in (B2). On the other hand, since in the LHST only two qubits Aj Bj are measured for a given run of the
experiment, the disentangling channel is applied only on the Aj Bj pair. However, we assume that global Pauli
channels act on 2n qubits before and after the Hadamard and CNOT gate. For each jä{1, K, n}, the
disentangling channel is given by the adjoint of the following channel:
AB
A j Bj
 ¢j := AB
Ä  A j B j) ◦ Q jAB ◦ ( A j Ä  B j Ä  A j B j) ◦  AB
j ◦ ( X
j ,

AB

j j
= AB
Ä  A j B j ) ◦ ( A j Ä  B j Ä  A j B j ) ,
j ◦ ( X

(B6)

(B7)

AB
AB
AB
where  AB
j ,  j ,  j , and j are 2n -qubit global Pauli channels, as deﬁned in (A8), and we used lemma 1.
We remark that the Pauli channels are deﬁned with a j subscript in (B7) to emphasize that for different runs of
the experiment the Pauli channels that act could be different.
From arguments similar to those used to derive (B4), we ﬁnd that
1

AB
1
a j bj
a j bj
 ¢j (∣0, 0ñá0, 0∣A j B j Ä  A j B j) = 2 å m aAB
, a , b , b ( X A j Z A j Ä X B j Z B j Ä  A j B j) .
2 a j, bj = 0 j j j j

(B8)

Appendix C. Measurement noise in FUMC
For the proofs given in appendices D–G, we will make use of some properties of measurement noise in FUMC.
Hence, it is helpful to ﬁrst state these properties in this appendix.
Let P0 denote the POVM element associated with getting the all-zeros outcome in the noiseless HST, which
n
can be expressed as P0 :=∣0ñá0∣ = ⨂2j =
1∣0ñá0∣. We consider the measurement noise as follows. For each qubit j,
( j)
( j)
where jä{1, K, 2n}, the ideal projector ∣0ñá0∣ gets replaced by p00
∣0ñá0∣ + p01
∣1ñá1∣. Moreover, we assume
( j)
( j)
that for all j the following strict inequality holds: p00 > p01 .
Let P0 denote the noisy POVM element. Then the following equalities hold:
n

n

j=1

j=1

Aj
Aj
Bj
Bj
P0 = ⨂ ( p00
∣0ñá0∣A j + p01
∣1ñá1∣A j ) Ä ⨂ ( p00
∣0ñá0∣B j + p01
∣1ñá1∣B j )

=å p A (a ) p B (b)∣a , bñáa , b∣AB ,

(C1)
(C2)

a, b

with p A (a ) = ( p01A1 )a1  ( p01An )an ( p00A1 )1 - a1  ( p00An )1 - an and p B (b ) = ( p01B1 )b1  ( p01Bn )bn ( p00B1 )1 - b1  ( p00Bn )1 - bn .
C.1. Effective noisy measurement operator for the HST
In the noiseless HST, the measurement is preceded by the disentangling unitary (E AB )†, where E AB is deﬁned in
(B1). In the Heisenberg picture, this corresponds to the evolution of the measurement operator with respect to
the unitary E AB. We now derive the effective noisy POVM element as the evolution of P0 under the noisy
AB
entangling channel  (deﬁned in section B).
Using (A5), ∣a, bñáa, b∣AB can be expressed as follows:
⎛ 1
⎞
∣a , bñáa , b∣AB = (XAa Ä XBb) ⎜ 2n ål , k Z Al Ä ZBk⎟(XAa Ä XBb)
⎝2
⎠
1
= 2n ål , k ( - 1)a·l ( - 1)b·k Z Al Ä ZBk ,
2

(C3)

where we used the properties of the Pauli operators as deﬁned in (A2). Then, from (B4) and the linearity of
quantum channels, it follows that
1
AB
l k
a·l
b·k l k
 (∣a , bñáa , b∣AB ) = 2n å mlAB
(C4)
, l , k, k ( - 1) ( - 1) X A Z A Ä XB ZB .
2 l,k

18

New J. Phys. 22 (2020) 043006

K Sharma et al

Therefore, from (C2) and (C4) it follows that
1
AB
aA, b Z Ab XAa Ä ZBb XBa ,
 (P0) = 2n å maAB
, a , b, b p
2 a, b

(C5)

where paA, b = ål, k (-1)a·l (-1)b·k p A (l ) p B (k ), and p A (l ) and p B (k ) are probability distributions as in (C2).
C.2. Effective noisy measurement operator for the LHST
In the LHST, a noisy measurement on two qubits Aj Bj is preceded by the disentangling unitary (E Aj Bj )† acting on
the same two qubits. Similar to section C.1, we now derive the effective POVM element as the evolution of the
( j)
operator Q00
(deﬁned below) under the adjoint of the noisy disentangling channel, as deﬁned in (B7). The noisy
POVM for the qubits Aj Bj is given by
~( j )
Q00 =

1

å p A (a¢) p B (b¢)∣a¢, b¢ñáa¢, b¢∣A B ,
j

j

j

j

(C6)

a ¢ , b ¢= 0

which follows from (C2). Moreover, the overall noisy POVM for the LHST is deﬁned as
1 n ~( j )
~
Q 00 = å Q00 Ä  A j B j.
n j=1

By using arguments similar to those used in (C3), (C4), and (C5), we ﬁnd that
AB ~( j )
1
 A j Z Abj X Aaj Ä Z Bbjj X Bajj Ä  A j B j ,
 ¢j (Q00 Ä  A j B j) = 2 å m aAB
,a ,b ,b p
2 a j, bj j j j j a j, bj

(C7)

(C8)

A
where  ¢j is given by (B7) and paj,jbj = å1a ¢ , b ¢= 0(-1)aj·a ¢ (-1)bj·b ¢p Aj (a ¢) p Bj (b¢).
Therefore, the overall effective noisy POVM for the LHST is deﬁned as

AB

1 1 n 1
AB ~
 A j Z Abj X Aaj Ä Z Bbjj X Bajj Ä  A j B j.
 ¢ (Q 00) = 2 å å m aAB
,a ,b ,b p
2 n j = 1a j, bj = 0 j j j j a j, bj

(C9)

Appendix D. Proof of theorem 1
Before providing a proof of theorem 1, we prove the following lemma.
Lemma 2. Let CQC (V ) be a cost function of V with V Î d , and d the set of d ´ d unitary matrices. Additionally
suppose that CQC (V ) can be evaluated using a quantum circuit denoted QC as follows:
C QC (V ) := Tr[LV (r )] ,

(D1)

where r is a quantum state, L denotes a POVM element and V denotes the noisy unital quantum channel describing
QC (V ) exhibits
the evolution of the state throughout the computation, which depends on the unitary V . Then C
strong-OPR to a noise model composed of V and a global depolarizing channels acting continuously throughout the
computation.
Proof. Without loss of generality let us decompose V as k noisy unital quantum channels: V =  Vk ◦ ¼ ◦ 1V .
In the presence of global depolarizing noise acting throughout the computation, the cost function can now be
expressed as
QC (V ) = Tr [L( k + 1 ◦  Vk ◦ ¼ ◦  2 ◦ 1V ◦ 1)(r )] ,
C

(D2)

where we have interleaved the channels  Vi with global depolarizing channels  i . From deﬁnition 1 and from
the fact that  Vi () =  , it follows that
QC (V ) = Tr [L( k + 1◦ Vk ◦ ¼ ◦  2 ◦ 1V ◦1)(r)] = p Tr [L( Vk ◦ ¼  V2 ◦ 1V )(r)] + (1 - p ) Tr [L] 2n
C
(D3)

= pCQC (V ) + (1 - p ) 2n ,

(D4)

where p = pk + 1 ¼ p1. Let  dopt denote the sets of unitaries that optimize CQC (V ) i.e.
 opt
d = {V ¢ Î d : C QC (V ¢) = min C QC (V )}.
V Î d

(D5)



Then, from (D4) we have that any unitary in  opt
d will also optimize C QC (V ). Hence C QC (V ) exhibits strongOPR to a noise model composed of V and a global depolarizing channels acting throughout the
computation.
,
19

New J. Phys. 22 (2020) 043006

K Sharma et al

By means of lemma 2 we know that if we show that a quantity exhibits OPR to a noise model  which does
not include global depolarizing noise acting continuously throughout the computation, then said quantity will
also exhibit OPR if we include global depolarizing noise to  .
We now provide a proof for theorem 1.
Theorem 1. The cost functions CHST and CLHST exhibit strong-OPR to Noise Model 1 in deﬁnition 7.
Proof. We begin by breaking up the HST circuit into three time intervals. In the ﬁrst time interval, the noisy
AB
entangling channel  is applied. In the second time interval, the quantum channel  † ◦  implements the
AB
unitaries U and V †. Finally, in the third time interval ( )† is applied. We assume that the global depolarizing
noise occurs on systems AB during all three time intervals and the global depolarizing noise occurs on system A
 AB
during the implementation of  † ◦  . Moreover, suppose that two different global Pauli channels  AB and 
act at times τ1 and τ2, respectively, and global non-unital Pauli channels act continuously on system B in between
τ1 and τ2.
Let r(0) denotes the initial state of the HST circuit and is given by r(0) = ∣0, 0ñá0, 0∣AB . At τ1 the state is
AB
AB
r (1) =  AB ( AB
◦  k ...  AB
◦ 1 (r (0))) ,
p(1,1)
p(1, k)

(D6)

where we have broken up the τ1 into k time increments and  k ◦ ... 1 is the channel that implements the
AB
AB
noisy entangling channel  , as deﬁned in (B2). Moreover, each  i is followed by a global depolarizing
channel  AB
, where p(r , s ) denotes the depolarizing probability for the sth time increment of the rth time
p(1, i )
AB

AB

interval. Then r(1) reduces to

AB
AB
AB
r (1) =  AB ( AB
◦  k ...  2 ( p(1,1) 1 (r (0)) + (1 - p(1,1) )  22n)
p(1, k)

(D7)

⎤
⎡ 1
AB
= p(1)  AB◦ (r (0)) + (1 - p(1) )  d = p(1) ⎢ 2n å b aAB, b XAa Z Ab Ä XBa ZBb⎥ + (1 - p(1) )  22n ,
⎥⎦
⎢⎣ 2 a, b

(D8)

where p(1) = p(1,1) ... p(1, k ) . The second equality follows from lemma 2 as  consists of only unitary and Pauli
AB
channels, and thus each  i is a unital channel, where iä{1, K, k}. The last equality follows from (B4) and
AB
AB
(A8), where b aAB
, b = ma, a, b, b qa, a, b, b .
Similarly, the state at τ2 is given by
AB

B
B
(1)
AB
A
 AB ( AB(2,l) ◦  A(2,l) ◦ (l Ä  NU,
r (2) = 
l) ...  p(2,1) ◦  s (2,1) ◦(1 Ä  NU,1)(r )).
p
s

(D9)

B
We ﬁrst ﬁnd the action of the channel 1 Ä  NU,1
on r(1) . Consider that

⎡
⎤
⎛
⎞
1
B
⎢ p(1) ⎜ å b aAB, b XAa Z Ab Ä XBa ZBb⎟ + AB⎥

Ä

(
)
1
NU,1
⎜
⎟
⎢⎣
⎥⎦
22n
⎝(a, b) ¹ (0, 0)
⎠

(D10)

⎡
⎤
⎛
⎞
1
= 2n ⎢ p(1) ⎜⎜ å b aAB, b ca(1, b) W1 XAa Z Ab W1† Ä XBa ZBb⎟⎟ + AB + å dg(1, h) A Ä XBg ZBh⎥ ,
⎥⎦
2 ⎢⎣
⎝(a, b) ¹ (0, 0)
⎠
(g , h ) ¹ (0, 0)

(D11)

B
(1 Ä  NU,1
)(r (1)) =

where we used the deﬁnition of a non-unital Pauli channel from (A9) and (A10). We note that the terms that are
independent of Wi do not affect the global optima. Therefore, the only relevant term in (D9) is
r (2) =

m
⎞
p(2) s (2) p(1)  AB ⎛
⎜⎜ å b aAB, b (  ca(i,)b) WXAa Z Ab W † Ä XBa ZBb⎟⎟ ,

2
n
2
⎝(a, b) ¹ (0, 0)
⎠
i=1

(D12)

where p(2) = p(2,1) ... p(2, l ) and s (2) = s (2,1) ... s (2, l ) , and where we have used (A9) and lemma 2.
Finally, the relevant term after the action of the noisy disentangling channel is
AB
AB
AB
r (3) =  AB
◦( m )†...  AB
◦(1 )† (r (2)) = p(3) ( )† (r (2)) + (1 - p(3) )  22n ,
p(3,1)
p(3, m)

(D13)

where p(3) = p(3, m) ... p(3,1) . The last equality follows from the fact that the channel ( )† consists of unitary
AB
channels and Pauli channels, and thus each ( i )† is a unital channel. Therefore, the term that decides the global
optima in the HST is given by
AB

m
⎛
⎞
AB
 AB ⎜ å b aAB, b (  c (i ) ) WXAa Z Ab W † Ä XBa ZBb⎟ ,
s (3) = ( )† ◦ 
⎜
⎟
a, b
⎝(a, b) ¹ (0, 0)
⎠
i=1

20

(D14)

New J. Phys. 22 (2020) 043006

K Sharma et al

where we have omitted the scaling factors. Let FHST (V ) µ f (V ) := Tr [P0 s (3) ]. Then
⎡
m
⎞⎤
⎛
 AB ◦  AB)(P0) ⎜ å b aAB, b (  c (i ) ) WXAa Z Ab W † Ä XBa ZBb⎟ ⎥
f (V ) = Tr⎢(
⎟⎥
⎜
a, b
⎢⎣
⎠⎦
⎝(a, b) ¹ (0, 0)
i=1

(D15)

⎡
⎤
⎢
⎥


= Tr ⎢ å kaAB, a, b, b Z Ab X Aa WXAa Z Ab W † Ä ZBb XBa XBa ZBb⎥
⎢(a, b) ¹ (0, 0)
⎥
⎣ a, b
⎦

(D16)

⎡
⎤
= TrA⎢ å kaAB, a, b, b Z Ab XAa WXAa Z Ab W †⎥.
⎢⎣(a, b) ¹ (0, 0)
⎥⎦

(D17)

~ AB p A q AB b AB (m c (i) ). The
The second equality follows from (C5), where we set kaAB
:=(1 22n) m
i = 1 a, b
, a, b, b
a, a, b, b a, b a, a, b, b a, b
opt
last equality follows from (A2). Let  d denote the sets of unitaries that optimize FHST (V ) (and hence
CHST (V )) such that
†
if
 opt
d = {V ¢ Î d : W = (V ¢) U = e  ,

for some f Î [0, 2p ]}.

(D18)

We remark that this set of unitaries also optimizes FLHST (V ) (and hence CLHST (V )). Then, for V ¢ Î d we ﬁnd
f (V ¢) = å (a, b) ¹ (0, 0) kaAB
, a, b, b . Let
T (V ):=

å

kaAB, a, b, b XAa Z Ab W † Ä ∣a , bñ ,

(a, b ) ¹ (0, 0)

S (V ):=

å

kaAB¢ , a ¢ , b ¢ , b ¢ W †X Aa ¢ Z Ab ¢ Ä ∣a ¢ , b¢ñ.

(D19)

(a ¢ , b ¢) ¹ (0, 0)

Consider the following inequality:
f (V ) = ∣ á S (V ) , T (V )ñ ∣ 

Tr (S (V )†S (V )) Tr (T (V )†T (V )) =

å

kaAB, a, b, b ,

(D20)

(a, b ) ¹ (0, 0)

where we used the Cauchy–Schwarz inequality. Moreover, note that the inequality in (D20) is saturated for any
AB
matrix V ¢ Î d if we assume that the coefﬁcients kaAB
, a, b, b characterizing the noise satisfy ka, a, b, b  0 . Therefore,
~opt
the set of unitaries that optimize FHST (V ) (and hence CHST (V )) is  d =  opt
d . According to deﬁnition 6, the
latter means that CHST exhibits strong-OPR to Noise Model 1 in deﬁnition 7.
We now show that the cost function CLHST exhibits strong-OPR to Noise Model 1. The LHST corresponds
to the optimization of the following function:
⎡
m
⎞⎤
~ ⎛⎜
 AB ◦  ¢ AB)(Q
FLHST (V ) µ g (V ) = Tr⎢(
b aAB, b (  ca(i,)b) WXAa Z Ab W † Ä XBa ZBb⎟⎟ ⎥ ,
00) ⎜
å
⎢⎣
⎝(a, b) ¹ (0, 0)
⎠ ⎥⎦
i=1

(D21)

where we replaced the disentangling and measurement channels in (D15) with (C9). Consider the following:
⎡⎛
⎞
1 1 n 1 ~ AB
bj¢ a j¢
bj¢ a j¢
Aj
⎟


g (V ) = Tr ⎢⎜⎜ 2 å å m
p
q
Z
X
Z
X

Ä
Ä
A j B j⎟
Bj Bj
⎢ 2 n j = 1a ¢, b ¢= 0 a j¢, a j¢, bj¢, bj¢ a j¢, bj¢ a j¢, a j¢, bj¢, bj¢ A j A j
⎠
⎣⎝
j j
m
⎛
⎞⎤
´ ⎜⎜ å b aAB, b (  ca(i,)b) WXAa Z Ab W † Ä XBa ZBb⎟⎟ ⎥
⎠ ⎥⎦
⎝(a, b) ¹ (0, 0)
i=1

(D22)
⎡n
⎤
1
b¢ a ¢
b¢ a ¢ a b
a b
= Tr ⎢å å
x (aj,)a ¢, b, b ¢ (Z Ajj X Ajj Ä  A j) WXAa Z Ab W † Ä Z Bjj X B jj X B jj Z B jj X B jj Z B jj ⎥
å
j
j
⎢⎣ j = 1(a, b) ¹ (0, 0) a ¢, b ¢= 0
⎥⎦
j j

(D23)

⎡n
⎤
1
b¢ a ¢
b¢ a ¢ a b
a b
= TrA⎢å å
x (aj,)a ¢, b, b ¢ (Z Ajj X Ajj Ä  A j) WXAa Z Ab W † Ä Tr B j (Z Bjj X B jj X B jj Z B jj ) Tr B j (X B jj Z B jj ) ⎥
å
j
j
⎢⎣ j = 1(a, b) ¹ (0, 0) a ¢, b ¢= 0
⎥⎦
j j
(D24)
⎡n
⎤
b
a
a
b
= TrA⎢å å x (ajj,)a j, bj, bj (Z Ajj X Ajj Ä  A j)(W (X Ajj Z Ajj Ä  A j) W †) ⎥
⎢⎣ j = 1(a j, bj ) ¹ (0,0)
⎥⎦
n

å

å

j = 1(a j , b j ) ¹ (0,0)

x (ajj,)a j, bj, bj ,

(D25)

(D26)

21

New J. Phys. 22 (2020) 043006

K Sharma et al

where in (D24) we have split TrB into a contribution from qubit Bj and a contribution on all qubits except Bj, and
A
~ A, B
where x (aj,)a ¢, b, b¢ = (1 4n) m
p j q
b AB ( m c (i) ). The ﬁrst equality is derived from (C9), while the
a j¢, a j¢, bj¢ bj¢ a j¢, bj¢ a j¢, a j¢, bj¢, bj¢ a, b i = 1 a, b
j
j
inequality follows from the arguments similar to (D20).
Here we remark that the inequality (D26) is saturated for any unitary matrix in the set of unitaries that
optimize FHST (V ) (and hence CLHST (V )) given by (D18). Hence, CLHST exhibits strong-OPR to Noise Model 1
in deﬁnition 7 if we assume that the coefﬁcients x (ajj,)aj, bj, bj characterizing the noise satisfy x (ajj,)aj, bj, bj  0.
,

Appendix E. Proof of theorem 2
Theorem 2. The cost functions CHST and CLHST exhibit strong-OPR to Noise Model 2 in deﬁnition 8.
Proof. We break up the HST circuit into three time intervals similar to section D. We again assume that the
global depolarizing noise occurs on system AB during all three time intervals and the global depolarizing noise
occurs on system A during the implementation of  † ◦  . Moreover, suppose that a global Pauli channel  AB
A
 AB acts
followed by a global non-unital Pauli channel  NU
acts at time τ1. Furthermore, a global pauli channel 
at time τ2, while a global Pauli channel acts continuously on the system B in between τ1 and τ2.
The state at τ1 is given by
A
A
◦  AB◦ (r (0)) + (1 - p(1) )  NU
( 22n)
r (1) = p(1)  NU
AB

(E1)

⎡ 1
⎤
1
1
a b
a b⎥
aAB
= p(1) ⎢ 2n å b
å dg ,hXAg ZAh Ä B.
, b X A Z A Ä XB ZB + 2n  + 2n
⎢⎣ 2 (a, b) ¹ (0, 0)
⎥⎦
2
2 (g , h) ¹ (0, 0)

(E2)

The ﬁrst equality follows from arguments similar to those used to derive (D6)–(D8). The last equality follows
AB
AB
aAB
from (B4), (A9), and (A10), where b
, b = ma, a, b, b qa, a, b, b ca, b .
At τ2 the state is
 ( AB(2,l) ◦ A(2,l) ◦(l Ä 
 l )...  AB(2,1) ◦  A(2,1) ◦(1 Ä 
1 )(r (1))).
r (2) = 
p
s
p
s
B

AB

B

(E3)

The term that depends on W in (E3) is given by
r (2) =

⎡
⎤
l
1  AB ⎢ (2) (2) (1)
AB
g h
(i )
a b
† Ä XaZb +
† Ä  ⎥,


(
)

p
s
p
b
p
WX
Z
W
d
WX
Z
W
B
å a, b  a, b
å g ,h A A
A A
B B
⎢⎣
⎥⎦
22n
(a, b ) ¹ (0, 0)
(g , h ) ¹ (0, 0)
i
(E4)

where we used the deﬁnition of Pauli channels from (A6) and (A8). By omitting the scaling factors, the relevant
term after t3 is given by

(

AB
a b
a b
†
 AB p(2) s (2) p(1) å
 AB l  (i )
r (3) = ( )† ◦ 
(a, b ) ¹ (0, 0) ba, b ( i pa, b ) WXA Z A W Ä XB ZB

)

AB
g h
†
 AB å
+ ( )† ◦ 
(g , h ) ¹ (0, 0) d g , hWXA Z A W Ä B .

(

)

(E5)

Let FHST (V ) µ f (V ) := Tr [P0 r (3) ]. Then
⎡  AB  AB 
⎤
l  (i )
aAB
f (V ) = Tr⎢⎣(
◦  )(P0) p(2) s (2) p(1) å(a, b) ¹ (0, 0) b
) WXAa Z Ab W † Ä XBa ZBb ⎥⎦
, b ( i p
a, b

(

)

g h
⎤
†
 AB ◦  AB)(P0) å
+ Tr⎡⎣(
(g , h ) ¹ (0, 0) d g , hWXA Z A W Ä B ⎦.

(

)

(E6)

Moreover, for simplicity we denote
⎡
l
⎛
⎞⎤
 AB ◦  AB)(P0) ⎜ å b
aAB
a(i, )b ) WXAa Z Ab W † Ä XBa ZBb⎟⎟ ⎥ ,
f1 (V ) := Tr⎢(
, b ( p
⎜
⎢⎣
⎝(a, b) ¹ (0, 0)
⎠ ⎥⎦
i

(E7)

⎡
⎛
⎞⎤
 AB ◦  AB)(P0) ⎜ å d g , hWX g Z Ah W † Ä B⎟ ⎥.
f2 (V ) := Tr⎢(
A
⎜
⎟⎥
⎢⎣
⎝(g , h) ¹ (0, 0)
⎠⎦

(E8)

22

New J. Phys. 22 (2020) 043006

K Sharma et al

Let us focus on f1 (V ) and f2 (V ) individually. Consider the following:
⎡
⎤
⎢
⎥
b¢ a¢
b¢ a¢ a b
AB
a b
†
f1 (V ) = Tr ⎢ å Ja, a ¢ , b, b ¢ Z A X A WXA Z A W Ä ZB XB XB ZB ⎥
⎢(a, b) ¹ (0, 0)
⎥
⎣ a¢,b¢
⎦
⎡
⎤
= Tr ⎢ å JaAB, a, b, b Z Ab XAa WXAa Z Ab W †⎥
⎢⎣(a, b) ¹ (0, 0)
⎥⎦

å



JaAB, a, b, b.

(E9)

(a, b ) ¹ (0, 0)

A
2n ~ AB

 AB ( l p (i) ). The
a ¢ , b ¢ qaAB
b
The ﬁrst equality follows from (C5), where JaAB
, a ¢ , b, b ¢ = (1 / 2 ) ma ¢ , a ¢ , b ¢ , b ¢ p
¢ , a ¢ , b ¢ , b ¢ a, b i a, b
inequality follows from the arguments similar to (D20). Here, the last inequality in (E9) is saturated for any
matrix V in the set  dopt of unitaries that optimize FHST (V ) (and hence CLHST (V )) given by (D18).
On the other hand

⎡
⎤
⎢
⎥
b¢ a¢
g h
a¢ b¢
†
f2 (V ) = Tr ⎢ å V AB
g , a ¢ , h, b ¢ Z A X A WXA Z A W Ä ZB XB ⎥
⎢(g , h) ¹ (0, 0)
⎥
⎣ a¢,b¢
⎦

(E10)

⎡
⎤
⎢
⎥
b¢ a¢
g h
a¢ b¢
†
= TrA⎢ å V AB
g , a ¢ , h, b ¢ Z A X A WXA Z A W Ä TrB (ZB XB ) ⎥
⎢(g , h) ¹ (0, 0)
⎥
⎣ a¢,b¢
⎦
=

å

(g , h ) ¹ (0, 0)

(E11)

g h
V AB
g , 0, h, 0 TrA (XA Z A ) = 0.

(E12)

A
~ AB

 AB ( l p (i) ). From the last equality it follows that f (V )
a ¢ , b ¢ qaAB
d b
where V gAB, a ¢ , h, b ¢ = (1 22n) m
a¢,a¢,b¢,b¢ p
2
¢ , a ¢ , b ¢ , b ¢ g , h a, b i a, b
is independent of W (and hence of V ) and thus does not affect the global optima. Therefore, from (E9) it follows
opt
HST (V )) is ~
that the set of unitaries that optimize FHST (V ) (and hence C
 d =  dopt . From deﬁnition 6 this
implies that CHST exhibits strong-OPR to Noise Model 2 in deﬁnition 8 if we assume that the coefﬁcients JaAB
, a, b, b
characterizing the noise satisfy JaAB
.

0
, a, b, b
We now show that the cost function CLHST exhibits strong-OPR to Noise Model 2. In particular, in the LHST
we want to optimize the following function:

FLHST (V ) µ g (V )
⎡  AB  ¢ AB ~
⎤
l  (i )
aAB
=Tr⎢⎣(
◦  )(Q 00) p(2) s (2) p(1) å(a, b) ¹ (0, 0) b
) WXAa Z Ab W † Ä XBa ZBb ⎥⎦
, b ( i p
a, b
~
g h
⎤
†
 AB ◦  ¢ AB)(Q
+ Tr⎡⎣(
00) å(g , h ) ¹ (0, 0) d g , hWXA Z A W Ä B ⎦ ,

(

)

(

)

(E13)

where we replaced the disentangling and measurement channels in (E6) with (C9). We now break up g(V ) into
two different functions.
⎡
l
⎞⎤
~ ⎛⎜
 AB ◦  ¢ AB)(Q
aAB
a(i, )b ) WXAa Z Ab W † Ä XBa ZBb⎟⎟ ⎥ ,
g1 (V ) := Tr⎢(
b
00) ⎜
å
, b ( p
⎢⎣
⎝(a, b) ¹ (0, 0)
⎠ ⎥⎦
i

(E14)

⎡
⎛
⎞⎤
~ ⎜
 AB ◦  ¢ AB)(Q
g2 (V ) := Tr⎢(
d g , hWXAg Z Ah W † Ä B⎟⎟ ⎥.
00) ⎜
å
⎢⎣
⎝(g , h) ¹ (0, 0)
⎠ ⎥⎦

(E15)

By using arguments similar to those used to derive equations (E10)–(E12) and from (C9), it follows that g2 (V ) is
independent of W (and hence of V ). Therefore, to prove the noise resilience of the LHST, we focus only on
g1 (V ). We then get:
⎡n
⎤
1
b¢ a ¢
b¢ a ¢ a b
a b
g1 (V ) = Tr ⎢å å
t (aj,)a ¢, b, b ¢ (Z Ajj X Ajj Ä  A j) WXAa Z Ab W † Ä Z Bjj X B jj X B jj Z B jj X B jj Z B jj ⎥ ,
å
j
j
⎢⎣ j = 1(a, b) ¹ (0, 0) a ¢, b ¢= 0
⎥⎦
j j

(E16)

~ AB

a, b (l p (i) ). We note that (E16) is similar to (D23). Therefore,
a ¢ ,jb ¢ qaAB
where t(aj,)a ¢, b, b¢ = (1 4n) m
b
a j¢, a j¢, bj¢, bj¢ p
i a, b
j¢, a j¢, bj¢, bj¢
j
j
from the proof in section D it follows that
A

AB

23

New J. Phys. 22 (2020) 043006

K Sharma et al
n

g1 (V )  å

å

j = 1(a j , b j ) ¹ (0,0)

t (ajj,)a j, bj, bj ,

(E17)

where the inequality is saturated for unitaries V ¢ in the set  dopt of unitaries that optimize FLHST (V ) (and hence
CLHST (V )) given by (D18). This further implies that
~opt
g (V )  g (V ¢) , for all V ¢ Î  opt
(E18)
d = d .
Thus CLHST exhibits strong-OPR to Noise Model 2 if we assume that the coefﬁcients t (ajj,)aj, bj, bj characterizing the
noise satisfy t (ajj,)aj, bj, bj  0.

,

Appendix F. Proof of theorem 3
Theorem 3. The cost functions CLET and CLLET exhibit weak-OPR, as deﬁned in deﬁnition 6, to Noise Model 3 in
deﬁnition 9.
Proof. Let us remark that in order to show weak-OPR to Noise Model 3 we just need to consider Pauli noise
acting at τ1 and measurement noise, since noise resilience to global depolarizing noise follows from lemma 2.
We ﬁrst consider the CLET cost function. From equations (A5) and (A6) we get that the action of the Pauli
channel acting at time τ1 is given by
 (∣0ñá0∣) = å ql , kX l Z k∣0ñá0∣Z kX l = å ql ∣lñál∣ ,
l,k

(F1)

l

where ql = åk ql, k . Similarly, we can express the noisy measurement POVM from deﬁnition 5 as
n

( j)
( j)
P0 = ⨂ ( p00
∣0ñá0∣ + p01
∣1ñá1∣) = å pi ∣iñái∣ ,
j=1

(F2)

i

with i = i1 i2 ¼ in a bit string and pi = p0(i11) p0(i22) ¼ p0(inn). For the present noise model we are interested in
determining the optimum of the function
LET (V ) = Tr [P0 ( ◦ )(∣0ñá0∣)] ,
G

with  =  † ◦  the channel that implements U followed by

(F3)

V †. Then, by means of (F1) and (F2) we ﬁnd

⎡⎛
⎞⎤
⎞⎛
LET (V ) = Tr ⎢⎜å p ∣iñái∣⎟ ⎜å q W ∣lñál∣W †⎟ ⎥ = å p q wil ,
G
i
l
i l
⎢⎣⎝ i
⎠ ⎥⎦
⎠⎝ l
i, l

(F4)

where wil = ∣ ái∣W ∣l ñ ∣2 are the matrix elements of a doubly stochastic matrix such that å i wil = ål wil = 1.
Let us now denote by q the vector with elements qi ordered in decreasing order. Similarly, we denote by p
the vector with elements pl ordered in decreasing order. Additionally, let {∣qr ñ} and {∣ ps ñ} be the basis in which
q and p are ordered, respectively, i.e.
 (∣0ñá0∣) = å qr∣qr ñáqr ∣ ,

and

P0 = å ps∣ ps ñá ps ∣.

r

(F5)

s

Then, from the permutation inequality (or the rearrangement inequality) [48] we have
LET (V ) = å p q wil  p · q.
G
i l

(F6)

i, l

The inequality in (F6) is saturated for matrices W Î  , where  is the subset of the Permutation Group which
maps {∣ ps ñ} to {∣qr ñ}. We remark here that if the vector q (or p) has components of equal magnitude, then the
set  is degenerate. Moreover, note that
p0  pi ,

and

q 0  qi ,

" i ¹ 0,

(F7)

where the second inequality follows from deﬁnition 2, while the ﬁrst inequality always holds since
( j)
( j)
( j)
" j.
p0 = nj = 1 p00
, and since we have assumed that p00
> p01
opt
We now recall that  d denotes the set of unitaries that optimize CLET (V ) and CLLET (V ), i.e. " V ¢ Î  opt
d
we have W ¢∣0ñ = (V ¢)†U ∣0ñ = ∣0ñ (up to a global phase), which entails wi¢0 = w0¢i = di, 0 , and hence
equation (F4) becomes
LET (V ¢) = p q + å p q wil¢ .
G
(F8)
0 0

i, l ¹ 0

i l

Since p0  pi and q0  qi " i then the ﬁrst term in (F8) corresponds to the ﬁrst term in the summation
p · q = år qr pr. Hence, in order to saturate (F6) we now need that W ¢ Î  , i.e. the (n - 1) ´ (n - 1)
principal submatrix of W ¢ with matrix elements áz∣W ¢∣z ¢ñ (such that z , z ¢ ¹ 0 ) must map {∣ ps ñ} to {∣qr ñ}
24

New J. Phys. 22 (2020) 043006

K Sharma et al

(where s ¹ 0 and r ¹ 0). Combining this result with (F6) we have that for any matrix V in d (the set of d × d
unitary matrices)
LET (V )  p · q = G
LET (V ¢) ,
G

(F9)

~opt
where V ¢ Î  d and where
~opt
 d = {V ¢ Î d : W = (V ¢)†U Î }.
(F10)
~opt
opt
opt
Evidently, not all matrices in  d are in  , which then entails that  d Í  d , and further means that CLET
exhibits weak-OPR to Noise Model 3 according to deﬁnition 6.
Let us now consider the noise resilience of LLET to Noise Model 3 of deﬁnition 9. We are now interested in
the optimum of
n

LLET (V ) = 1 å Tr [( p( j ) ∣0ñá0∣ + p( j ) ∣1ñá1∣) Ä  A j)(◦)(∣0ñá0∣)]
G
00
01
n j=1
=

⎤
⎡
1 n
( j)
( j)
∣0ñá0∣ + p01
∣1ñá1∣) Ä  A j)(å ql W ∣lñál∣W †) ⎥.
Tr ⎢( p00
å
n j=1 ⎣
⎦
l

(F11)

(F12)

For any matrix V ¢ Î  dopt we have W ¢∣0ñ = (V ¢)†U ∣0ñ = ∣0ñ (up to global phase) and
ål ql W ¢∣l ñál∣(W ¢)† = q0∣0ñá0∣ + ål ¹ 0ql W ¢∣l ñál∣(W ¢)†, which leads to
n
n
⎡
⎞⎤
⎛
LLET (V ¢) = 1 å p( j ) q + 1 å Tr ⎢( p( j ) ∣0ñá0∣ + p( j ) ∣1ñá1∣) Ä  A j)) ⎜å q W ¢∣lñál∣(W ¢)†⎟ ⎥.
G
0
l
01
n j = 1 00
n j = 1 ⎢⎣ 00
⎠ ⎥⎦
⎝l ¹ 0

(F13)

On the other hand, for any unitary matrix V Î d
LLET (V ) = 1 å nj = 1 Tr [( p( j ) ∣0ñá0∣ + p( j ) ∣1ñá1∣) Ä  A j ) q W ∣0ñá0∣W †]
G
0
00
01
n
1
( j)
( j)
+ å nj = 1 Tr ⎡⎣( p00
∣0ñá0∣ + p01
∣1ñá1∣) Ä  A j)(ål ¹ 0 ql W ∣lñál∣W †) ⎤⎦
n
1
( j)
( j)
( j)
 å nj = 1 Tr [ p00
∣0ñá0∣ + p01
∣1ñá1∣) Ä  A j)(ål ¹ 0 ql W ∣lñál∣W †) ⎤⎦
q0 W ∣0ñá0∣W †] + Tr ⎡⎣( p00
n
1
1
( j)
( j)
( j)
= å nj = 1 p00
∣0ñá0∣ + p01
∣1ñá1∣) Ä  A j)(ål ¹ 0 ql W ∣lñál∣W †) ⎤⎦ ,
q0 + å nj = 1 Tr ⎡⎣( p00
n
n
(F14)

(

)

( j)
( j)
where the inequality follows from the fact that p00
, and hence
> p01
( j)
( j)
( j)
( j)
( j)
( p00
∣0ñá0∣ + p01
∣1ñá1∣) Ä  A j  ( p00
∣0ñá0∣ + p00
∣1ñá1∣) Ä  A j  p00
.

(F15)

We can then simplify equation (F14) as
n
n
n
LLET (V )  1 å p( j ) q + 1 å å q p ( j ) w kl = 1 å p( j ) q + å q p˜ w kl ,
G
n j = 1 00 0
n j = 1l ¹ 0, k ¹ 0 l k
n j = 1 00 0 l ¹ 0, k ¹ 0 l k

(F16)

( j)
( j)
where we have pk( j) = p00
if kj=0, and pk( j) = p01
if kj=1. On the the other hand, in the second equality of
1 n
j
(
)
(F16) we have deﬁned p˜k = n å j = 1 pk . Finally, the following inequality follows again from the rearrangement
inequality
n

LLET (V )  1 å p( j ) q + å q  p˜  ,
G
n j = 1 00 0 l ¹ 0, k ¹ 0 l k

(F17)

which is saturated for matrices W Î ¢, where ¢ is a subset of the Permutation Group such that
ål ¹ 0, k ¹ 0ql p˜k wkl = ål ¹ 0, k ¹ 0ql p˜k. Here q and p̃ are vectors with components ql and p˜k in decreasing order,
respectively. Hence, we can deﬁne the set of matrices which saturate (F17) as
~opt
 d = {V ¢ Î d : W = (V ¢)†U Î ¢}.
(F18)
While any matrix in  dopt saturates the inequality in (F14), only a subset will also saturate (F17). Hence,
~opt
 d Í  dopt , and CLLET exhibits weak-OPR to Noise Model 3 according to deﬁnition 6.

,

Appendix G. Proof of corollaries 1–8
Corollary 1. The cost functions CHST and CLHST exhibit strong-OPR to a noise model that includes the following: (1)
all noise processes in Noise Model 1, as well as (2) a noise process during the implementation of
25

New J. Phys. 22 (2020) 043006

K Sharma et al

 = k ◦  ◦ 1 =  †◦ (i.e. in the time interval between t1 and t2) in which global Pauli channels {1A , K,
 kA} act on system A, such that the overall channel on A is  kA ◦ k  ◦ 1A ◦ 1, provided that the following
condition is satisﬁed:
 A)(·).
( kA ◦  k  ◦  1A ◦ 1)(·) = ( k ◦  k - 1  ◦ 1 ◦ 

A

(G1)

is also a Pauli channel, and the channels  ,  †, and  correspond to conjugating the state by the unitaries

Here 
U , V †, and W , respectively.

Proof. This follows from the fact that the overall noisy channel acting during the implementation of  is
mathematically equivalent to a Pauli channel followed by the unitary  , as described in the condition (G1) and
by invoking theorem 1, which allows for Pauli channel noise at time τ1.,
Corollary 2. Let the W = V †U gate sequence have the form W = W2A W1A with W1A be composed only of Clifford
gates. Then the cost functions CHST and CLHST exhibit strong-OPR to a noise model that includes the following: (1)
all noise processes in Noise Model1, as well as (2) a noise process during the implementation of
 1A = 1, k ◦  ◦ 1,1, in which global Pauli channels {1A , K,  kA} act on system A, such that the overall
channel on A is  kA ◦ 1, k  ◦ 1A ◦ 1,1.
Proof. From lemma 1 it follows that Clifford unitaries satisfy the condition in (G1). Therefore, corollary 2 is a
special case of corollary 1.
,
Corollary 3. Let the W = V †U gate sequence have the form W = W2A W1A with W1A = W1A ¢ Ä W1A  being a tensor
product, i.e., W is a tensor product up to a particular time. Then the cost functions CHST and CLHST exhibit strongOPR to a noise model that includes the following: (1) all noise processes in Noise Model 1, as well as (2) a noise process
A¢
A
during the implementations of  1A ¢ =  1,Ak¢ ◦  ◦  1,1
and  1A  =  1,Al ◦  ◦  1,1
in which local
A¢
A¢
A
A
depolarizing channels {1,1, K, 1, k} and {1,1, K, 1, l } act on subsystems A¢ and A , respectively, such that the
A¢
A¢
A
A
overall channel on A¢A is (1,Ak¢ ◦  1,Ak¢ ... 1,1
◦  1,1
) Ä (1,Al ◦  1,Al ... 1,1
◦  1,1
).
Proof. Let ρ denote a quantum state. Consider the following chain of equalities:
( Ap ¢ Ä  qA)( A¢ Ä  A)(r ) = (A¢ Ä  qA)( p ( A¢ Ä  A(r )) + (1 - p ) p A¢ TrA¢(( A¢ Ä  A)(r ))
(G2)
= (A¢ Ä  qA)( p ( A¢ Ä  A(r )) + (1 - p ) p A¢ TrA¢((A¢ Ä  A)(r ))
(G3)

= (A¢ Ä  qA)( A¢ Ä  A)( pr + (1 - p ) p A¢ TrA¢(r ))

(G4)

= (A¢ Ä  qA)( A¢ Ä  A)( Ap ¢(r ))

(G5)

= ( A¢ Ä  A)( Ap ¢ Ä  qA)(r ) ,

(G6)

where p A ¢ is a maximally mixed state on system A¢. Therefore, the result follows by applying (G6) several times
and invoking corollary 1.

,

Corollary 4. The cost functions CHST and CLHST exhibit strong-OPR to the following noise model: (1) all noise processes
in Noise Model 2, as well as (2) a noise process during the implementation of  = k ◦  ◦ 1 =  †◦ (i.e. in the
A
A
, K,  NU,
time interval between t1 and t2) in which global non-unital Pauli channels { NU,1
k} act on system A such
A
A
that the overall channel on A is  NU, k ◦k  ◦  NU,1 ◦ 1, provided that the following condition is satisﬁed:
A
A

( NU,
k ◦  k  ◦  NU,1 ◦ 1)(·) = ( k ◦  k - 1  1◦  NU)(·) ,
A

(G7)

 NU is also a Pauli channel.
where 
A

Proof. This follows from the fact that the overall noisy channel acting during the implementation of  is
mathematically equivalent to a non-unital Pauli channel followed by the unitary  , as described in the
condition (G7) and by invoking theorem 2, which allows for non-unital Pauli noise at time τ1.,
Corollary 5. The cost functions CHST exhibits strong-OPR to the following noise model: (1) global depolarizing noise
acting continuously throughout the circuit, (2) global non-unital Pauli noise on system A at a ﬁxed time in between t1
and t2.

26

New J. Phys. 22 (2020) 043006

K Sharma et al

A
Proof. Let us decompose  as  = 2 ◦ 1 such that the non-unital Pauli channel  NU
acts at time t¢
A
between  1 and  2, with the overall channel between τ1 and τ2 given by 2 ◦  NU ◦ 1. The state at
time τ1 is

r (1) = p(1) ∣F+ñáF+∣ + (1 - p(1) )  d ,

(G8)

where p(1) = p(k,1)  p(1,1) corresponds to the continuous depolarizing channel as discussed in appendix D.
We break up the time interval in between t¢ and τ1 into l steps. The state at time t¢ is given by
A
l
1 (1)
AB
r (2) =  NU
◦ qAB
)
(2, l ) ◦ 1  ◦  (2,1) ◦ 1(r
q

(G9)

A
= NU
( p(1) q (2) 1(∣F+ñáF+∣) + (1 - p(1) q (2))  d )

(G10)

A
=p(1) q (2)  NU
(1(∣F+ñáF+∣)) + (1 - p(1) q (2))  d + (1 - p(1) q (2))

1
d g , hXAg Z Ah Ä B ,
å
d (g , h) ¹ (0, 0)

(G11)

where q(2) = q(2, k )  q(2,1) and 1 =  1l  11. Similarly, we break up the the time interval between τ2 and
t¢ into m steps. The term that depends on  at time τ2 is given by
A
s (2) = p(1) q (2) r (2) 2 ◦  NU
◦ 1(∣F+ñáF+∣) + r (2) (1 - p(1) q (2))


1
å dg ,hW2 XAg ZAh W2† Ä B. (G12)
d (g , h) ¹ (0, 0)

Let
FHST (V ) µ f (V ) := Tr[∣F+ñáF+∣ 
s (2)].

(G13)

Moreover, for simplicity we denote
A
f1 (V ) := Tr[∣F+ñáF+∣(2 ◦  NU
◦1)(∣F+ñáF+∣)] ,

(G14)

f2 (V ) := Tr[∣F+ñáF+∣(W2 XAg Z Ah W 2† Ä B)].

(G15)

A
f1 (V ) = Tr [∣F+ñáF+∣( 2A ◦  NU
)((A Ä (1T )B )(∣F+ñáF+∣AB ))]

(G16)

Consider the followings:
A
)(∣F+ñáF+∣)]
= Tr [(A Ä ( 1*)B )(∣F+ñáF+∣)( 2A ◦  NU

(G17)

A
= Tr [((1†) A Ä B)(∣F+ñáF+∣)( 2A ◦  NU
)(∣F+ñáF+∣)]

(G18)

A
= Tr [∣F+ñáF+∣( 1A ◦  2A ◦  NU
)(∣F+ñáF+∣)]

(G19)

 f1 (V ¢) ,
(G20)
opt
opt
where V ¢ Î  d , and where  d denote the sets of unitaries that optimize FHST (V ) (and hence CHST (V )) as

deﬁned in (D18). The ﬁrst and third equalities follow from the ricochet property. The last equality corresponds
to the case when there is non-unital Pauli noise at time τ1 and no other noise in the HST circuit, which is a special
case of theorem 2. Therefore, the inequality follows from theorem 2. Moreover, by using the arguments similar
to (E10)–(E12), we ﬁnd that f2 (V ) is independent of W. This completes the proof.
,

Corollary 6. The cost functions CLET and CLLET exhibit weak-OPR to a noise model that includes the following: (1)
all noise processes in Noise Model 3, as well as (2) a noise process during the implementation of
 = k ◦  ◦ 1 =  †◦ in which global Pauli channels {1, K, k} act, such that the overall channel is
k ◦ k  ◦ 1◦1, provided that the following condition is satisﬁed:
)(·).
(k ◦  k  ◦ 1 ◦ 1)(·) = ( k ◦  k - 1  ◦ 1 ◦ 

(G21)

 is also a Pauli channel.
where 

Proof. This follows from arguments similar to corollary 1 and by invoking theorem 3.

,

Corollary 7. Let the W = V †U gate sequence have the form W = W2A W1A with W1A be composed only of Clifford gates.
Then the cost functions CLET and CLLET exhibit weak-OPR to a noise model that includes the following: (1) all noise
processes in Noise Model 3, as well as (2) a noise process during the implementation of  1A = 1, k ◦  ◦ 1,1, in which
global Pauli channels {1A , K,  kA} act on system A, such that the overall channel on A is  kA ◦ 1, k  ◦ 1A ◦ 1,1.
Proof. This corollary is a special case of corollary 6, since lemma 1 implies that Clifford unitaries satisfy
(G21).

27

,

New J. Phys. 22 (2020) 043006

K Sharma et al

Corollary 8. Let the W = V †U gate sequence have the form W = W2A W1A with W1A = W1A ¢ Ä W1A  being a tensor
product, i.e. W is a tensor product up to a particular time. Then the cost functions CLET and CLLET exhibit weakOPR to a noise model that includes the following: (1) all noise processes in Noise Model 3, as well as (2) a noise process
A¢
A
during the implementations of  1A ¢ =  1,Ak¢ ◦  ◦  1,1
and  1A  =  1,Al ◦  ◦  1,1
in which local
A¢
A¢
A
A
depolarizing channels {1,1, K, 1, k} and {1,1, K, 1, l } act on subsystems A¢ and A ,respectively, such that the
A¢
A¢
A
A
overall channel on A¢A is (1,Ak¢ ◦  1,Ak¢ ... 1,1
◦  1,1
) Ä (1,Al ◦  1,Al ... 1,1
◦  1,1
).
Proof. This follows from arguments similar to the proof of corollary 3 and by invoking corollary 6.

,

ORCID iDs
Kunal Sharma https://orcid.org/0000-0003-3132-1088
M Cerezo https://orcid.org/0000-0002-2757-3170

References
[1] Preskill J 2018 Quantum computing in the NISQ era and beyond Quantum 2 79
[2] Temme K, Bravyi S and Gambetta J M 2017 Error mitigation for short-depth quantum circuits Phys. Rev. Lett. 119 180509
[3] Linke N M, Johri S, Figgatt C, Landsman K A, Matsuura A Y and Monroe C 2018 Measuring the renyi entropy of a two-site fermihubbard model on a trapped ion quantum computer Phys. Rev. A 98 052334
[4] Subaşı Y, Cincio L and Coles P J 2019 Entanglement spectroscopy with a depth-two quantum circuit J. Phys. A: Math. Theor. 52 044001
[5] Murali P, Baker J M, Javadi-Abhari A, Chong F T and Martonosi M 2019 Noise-adaptive compiler mappings for noisy intermediatescale quantum computers Proc. Twenty-Fourth Int. Conf. on Architectural Support for Programming Languages and Operating Systems
(New York: ACM) pp 1015–29
[6] Cincio L, Subaşı Y, Sornborger A T and Coles P J 2018 Learning the quantum algorithm for state overlap New J. Phys. 20 113022
[7] McClean J R, Romero J, Babbush R and Aspuru-Guzik A 2016 The theory of variational hybrid quantum–classical algorithms New J.
Phys. 18 023023
[8] Peruzzo A, McClean J, Shadbolt P, Yung M-H, Zhou X-Q, Love P J, Aspuru-Guzik A and O’Brien J L 2014 A variational eigenvalue
solver on a photonic quantum processor Nat. Commun. 5 4213
[9] Farhi E, Goldstone J and Gutmann S 2014 A quantum approximate optimization algorithm arXiv:1411.4028
[10] Johnson P D, Romero J, Olson J, Cao Y and Aspuru-Guzik A 2017 QVECTOR: an algorithm for device-tailored quantum error
correction arXiv:1711.02249
[11] Romero J, Olson J P and Aspuru-Guzik A 2017 Quantum autoencoders for efﬁcient compression of quantum data Quantum Sci.
Technol. 2 045001
[12] LaRose R, Tikku A, O’Neel-Judy É, Cincio L and Coles P J 2019 Variational quantum state diagonalization npj Quantum Inf. 5 8
[13] Arrasmith A, Cincio L, Sornborger A T, Zurek W H and Coles P J 2019 Variational consistent histories as a hybrid algorithm for
quantum foundations Nat. Commun. 10 3438
[14] Cerezo M, Poremba A, Cincio L and Coles P J 2019 Variational quantum ﬁdelity estimation arXiv:1906.09253
[15] Jones T, Endo S, McArdle S, Yuan X and Benjamin S C 2019 Variational quantum algorithms for discovering hamiltonian spectra Phys.
Rev. A 99 062304
[16] Yuan X, Endo S, Zhao Q, Benjamin S and Li Y 2019 Quantum 3 191
[17] Li Y and Benjamin S C 2017 Efﬁcient variational quantum simulator incorporating active error minimization Phys. Rev. X 7 021050
[18] Kokail C et al 2019 Self-verifying variational quantum simulation of lattice models Nature 569 355
[19] Khatri S, LaRose R, Poremba A, Cincio L, Sornborger A T and Coles P J 2019 Quantum-assisted quantum compiling Quantum 3 140
[20] Jones T and Benjamin S C 2018 Quantum compilation and circuit optimisation via energy dissipation arXiv:1811.03147
[21] Heya K, Suzuki Y, Nakamura Y and Fujii K 2018 Variational quantum gate optimization arXiv:1810.12745
[22] Carolan J et al 2020 Variational quantum unsampling on a quantum photonic processor Nat. Phys. 16 322–7
[23] Devitt S J, Munro W J and Nemoto K 2013 Quantum error correction for beginners Rep. Prog. Phys. 76 076001
[24] Fowler A G, Mariantoni M, Martinis J M and Cleland A N 2012 Surface codes: towards practical large-scale quantum computation
Phys. Rev. A 86 032324
[25] Chong F T, Franklin D and Martonosi M 2017 Programming languages and compiler design for realistic quantum hardware Nature
549 180
[26] Häner T, Steiger D S, Svore K and Troyer M 2018 A software methodology for compiling quantum programs Quantum Sci. Technol. 3
020501
[27] Venturelli D, Do M, Rieffel E and Frank J 2018 Compiling quantum circuits to realistic hardware architectures using temporal planners
Quantum Sci. Technol. 3 025004
[28] Cross A W, Bishop L S, Smolin J A and Gambetta J M 2017 Open quantum assembly language arXiv:1707.03429
[29] Horodecki M, Horodecki P and Horodecki R 1999 General teleportation channel, singlet fraction, and quasidistillation Phys. Rev. A
60 1888
[30] Nielsen M A 2002 A simple formula for the average gate ﬁdelity of a quantum dynamical operation Phys. Lett. A 303 249–52
[31] Cerezo M, Sone A, Volkoff T, Cincio L and Coles P J 2020 Cost-function-dependent barren plateaus in shallow quantum neural
networks arXiv:2001.00550
[32] Goussev A, Jalabert R A, Pastawski H M and Wisniacki D A 2012 Loschmidt echo Scholarpedia 7 11687
[33] Nielsen M A and Chuang I L 2010 Quantum Computation and Quantum Information (Cambridge: Cambridge University Press)
[34] Wilde M M 2017 Quantum Information Theory 2nd edn (Cambridge: Cambridge University Press)
[35] Shi Y 2003 Both toffoli and controlled-not need little help to do universal quantum computing Quantum Inf. Comput. 3 84–92
[36] Shor P 1997 Polynomial-time algorithms for prime factorization and discrete logarithms on a quantum computer SIAM J. Comput. 26
1484–509

28

New J. Phys. 22 (2020) 043006

K Sharma et al

[37] Wang Z, Rubin N C, Dominy J M and Rieffel E G 2020 Phys. Rev. A 101 012320
[38] Shende V V and Markov I L 2009 On the CNOT-cost of toffoli gates Quantum Inf. Comput. 9 0461–86
[39] Bärtschi A and Eidenbenz S 2019 Deterministic preparation of Dicke states Fundamentals of Computation Theory vol 11651 (Berlin:
Springer) (https://doi.org/10.1007/978-3-030-25027-0_9)
[40] Cruz D et al 2019 Efﬁcient quantum algorithms for ghz and w states, and implementation on the ibm quantum computer Adv.
Quantum Technol. 2 1900015
[41] Aleksandrowicz G et al 2019 Qiskit: An Open-source Framework for Quantum Computing
[42] Qiskit 2019 Qiskit/qiskit-tutorials
[43] Mitarai K, Negoro M, Kitagawa M and Fujii K 2018 Quantum circuit learning Phys. Rev. A 98 032309
[44] Kübler J M, Arrasmith A, Cincio L and Coles P J 2019 An adaptive optimizer for measurement-frugal variational algorithms
arXiv:1909.09083
[45] Gentini L, Cuccoli A, Pirandola S, Verrucchi P and Banchi L 2019 Noise-assisted variational hybrid quantum-classical optimization
arXiv:1912.06744
[46] Khodjasteh K and Viola L 2009 Dynamically error-corrected gates for universal quantum computation Phys. Rev. Lett. 102 080501
[47] Bravo-Prieto C, LaRose R, Cerezo M, Subaşı Y, Cincio L and Coles P J 2019 arXiv:1909.05820Variational quantum linear solver: a
hybrid algorithm for linear systems
[48] Hardy G H and Littlewood J E 1952 Karreman mathematics research collection Inequalities, Cambridge Mathematical Library ed
G Pólya et al (Cambridge: Cambridge University Press)

29

