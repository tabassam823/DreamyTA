Symplectic invariants, entropic measures and correlations
of Gaussian states
Alessio Serafini, Fabrizio Illuminati and Silvio De Siena

arXiv:quant-ph/0307073v4 16 Dec 2003

Dipartimento di Fisica “E. R. Caianiello”, Università di Salerno, INFM UdR Salerno,
INFN Sez. Napoli, Gruppo Collegato di Salerno, Via S. Allende, 84081 Baronissi (SA), Italy
We present a derivation of the Von Neumann entropy and mutual information of arbitrary two–mode Gaussian states, based on
the explicit determination of the symplectic eigenvalues of a generic covariance matrix. The key role of the symplectic invariants
in such a determination is pointed out. We show that the Von Neumann entropy depends on two symplectic invariants, while
the purity (or the linear entropy) is determined by only one invariant, so that the two quantities provide two different hierarchies
of mixed Gaussian states. A comparison between mutual information and entanglement of formation for symmetric states is
considered, remarking the crucial role of the symplectic eigenvalues in qualifying and quantifying the correlations present in a
generic state.
December 12, 2003

1

Introduction

state ̺ can be characterized either by the Von Neumann entropy SV (̺) or by the linear entropy SL (̺). Such quantities are defined as follows for continuous variable systems:

Quantum information with continuous variable systems is
rapidly developing and appears to yield very promising
perspectives concerning both experimental realizations and
general theoretical insights. In such a context, Gaussian
states play a prominent role, both in view of their conceptual importance and for their relevance in experimental applications, and have attracted most of the attention of the
researchers in the field [1]. They are the easiest states that
can be created and controlled in the laboratory [2], and have
been successfully exploited in quantum cryptography [3]
and quantum teleportation protocols [4]. Moreover, they
are possible candidates for continuous variable quantum
computation processing [5, 1].
In particular, two–mode Gaussian states aroused great
interest in later years, being the simplest prototype of a
continuous variable bipartite system. As for the theory,
the qualitative characterization of the entanglement of two–
mode Gaussian states has been fully developed by determining the necessary and sufficient criteria for their separability [6, 7]. A computable quantitative characterization
of entanglement for such states is available as well, being
provided by negativity [8] and, in the symmetric instance,
by the entanglement of formation [9, 10].
Due to the interaction with the environment, any pure
quantum state involved in some quantum information process evolves into a mixed state. Therefore, another property
of crucial interest in Quantum Information Theory is quantifying the degree of mixedness of a quantum state. Let
us briefly recall that the degree of mixedness of a quantum

SV (̺) ≡

SL (̺) ≡

− Tr (̺ ln ̺) ,

1 − Tr (̺2 ) ≡ 1 − µ(̺) ,

(1)
(2)

where µ ≡ Tr (̺2 ) denotes the purity of the state ̺. The
linear entropy of an arbitrary n–mode Gaussian state can be
easily computed, whereas the evaluation of the Von Neumann entropy requires, in general, a more involved technical procedure. Making use of the Von Neumann entropy is however preferable, as it allows for a finer and
more precise characterization of mixedness and correlations for multi-mode Gaussian states. In fact, the Von
Neumann entropy is additive on tensor product states, unlike the linear entropy. Moreover, we will show that for
two–mode Gaussian states the Von Neumann entropy depends on two symplectic invariants, while the linear entropy in completely determined by only one invariant. Finally, the knowledge of the Von Neumann entropy of a
generic two–mode state allows to obtain the mutual information I(̺) ≡ SV (̺1 ) + SV (̺2 ) − SV (̺) (here ̺i is the
reduced density matrix of subsystem i), which quantifies
the total amount of correlations (quantum plus classical)
contained in a state [11].
The Von Neumann entropy of a n–mode Gaussian state
has been determined in some remarkable works on the capacity of Gaussian channels by Holevo et al. [12]. In this
letter we elucidate the mathematical structure introduced
by these Authors, recasting it in a form that is conceptually simple and physically useful for applications and for
1

where Ω is the usual symplectic form




ω 0
0 1
Ω≡
, ω≡
.
0 ω
−1 0

explicit experimental schemes. To do so, we provide a
thorough and detailed analysis of the basics of the symplectic framework restricting to the two–mode case, presenting a simple and transparent procedure to evaluate the
Von Neumann entropy and the mutual information of two–
mode Gaussian states. Our approach is based on the explicit determination of the global symplectic invariants.
The methodology we introduce naturally highlights the role
played by the symplectic eigenvalues in characterizing the
correlations encoded in multipartite systems.

2

Inequality (6) is a useful way to express the Heisenberg
uncertainty principle.
In the following, we will make use of the Wigner quasi–
probability representation W (xi , pi ), defined as the Fourier
transform of the symmetrically ordered characteristic function [13]. In the Wigner phase space picture, the tensor
product H = H1 ⊗ H2 of the Hilbert spaces Hi ’s of the
two modes results in the direct sum Γ = Γ1 ⊕ Γ2 of the related phase spaces Γi ’s. As a consequence of the Stone-Von
Neumann theorem, a symplectic transformation acting on
the global phase space Γ corresponds to a unitary operator
acting on H [14]. In what follows we will refer to a transformation Sl = S1 ⊕ S2 , with each Si ∈ Sp(2,R) acting on
Γi , as to a “local symplectic operation”. The corresponding
unitary transformation is the “local unitary transformation”
Ul = U1 ⊗ U2 , with each Ui acting on Hi . Inequality (6) is
then a constraint on the Sp(2,R) ⊕ Sp(2,R) invariants [6]

Two–mode Gaussian states

Let us consider a two–mode continuous variable system,
described by the Hilbert space H = H1 ⊗H2 resulting from
the tensor product of the Fock spaces Hk ’s. We will call ak
the annihilation operator
acting on the space Hk .√Likewise,
√
x̂k = (ak + a†k )/ 2 and p̂k = −i(ak − a†k )/ 2 are the
quadrature phase operators of the mode k, the corresponding phase space variables being xk and pk . The set of Gaussian states is, by definition, the set of states with Gaussian
characteristic functions and quasi–probability distributions.
Therefore, a Gaussian state is completely characterized by
its first and second statistical moments, that is, respectively,
by the vector of mean values X̄ ≡ (hx̂1 i, hp̂1 i, hx̂2 i, hp̂2 i)
and by the covariance matrix σ
σij ≡

1
hx̂i x̂j + x̂j x̂i i − hx̂i ihx̂j i .
2

Det α + Det β + 2 Det γ ≤

(3)

1

W (X) =

−1

T

e− 2 Xσ X
√
,
π Det σ

(8)

where X stands for the vector (x1 , p1 , x2 , p2 ) ∈ Γ. In
general, the Wigner function transforms as a scalar under
symplectic operations, while the covariance matrix σ transforms according to
σ → S T σS ,

S ∈ Sp(4,R) .

As it is well known, for any covariance matrix σ there exists a local canonical operation Sl = S1 ⊕ S2 which brings
σ in the “standard form” σ sf [7]

(5)



a
 0
T
Sl σSl = σ sf ≡ 
 c1
0

The privileged role played by δ and ǫ in characterizing the
action of global symplectic operations on σ will become
clear in the following.
Positivity of ̺ and the commutation relations for quadrature phase operators impose the following constraint ensuring that σ be a bona fide covariance matrix [6]
i
σ+ Ω≥0,
2

1
+ 4 Det σ .
4

The Wigner function of a Gaussian state, written in terms
of the phase space quadrature variables, reads

First moments will be unimportant to our aims, and we will
set them to zero (as it is always possible by means of a
local unitary transformation) without any loss of generality
for our results. For simplicity, in what follows σ will refer
both to the Gaussian state and to its covariance matrix. It is
convenient to express σ in terms of the three 2 × 2 matrices
α, β, γ


α γ
σ≡
.
(4)
γT β
Let us define two further submatrices of σ




σ22 σ24
σ11 σ13
.
, ǫ=
δ=
σ42 σ44
σ31 σ33

(7)

0
a
0
c2

c1
0
b
0


0
c2 
 ,
0 
b

(9)

where a, b, c1 , c2 are determined by the four local symplectic invariants Det σ = (ab − c21 )(ab − c22 ), Det α = a2 ,
Det β = b2 , and Det γ = c1 c2 . Therefore, the coefficients
of the standard form corresponding to any covariance matrix are unique (up to a common sign flip of the ci ’s).

(6)
2

3

Determination of the Von Neumann
entropy

first moments, this amounts to determine the most general
parametrization of the covariance matrix, which is provided
by the following lemma.

To proceed, let us first note that the purity µ (and therefore
the linear entropy SL ) of a Gaussian state can be easily
computed. In fact, the trace of a product of operators corresponds to the integral of the product of their Wigner representations (when existing) over the whole phase space.
Using the Wigner representation W of ̺ and taking into account the proper normalization factors, for a n–mode Gaussian state we get
Z
π
1
µ= n
.
(10)
W 2 dn x dn p = √
2 R2n
2n Det σ

Lemma 1 An arbitrary two–mode covariance matrix σ can
be written as
(15)
σ = AT ν n∓ A ,
where ν n∓ = ν n− −1/2 ⊕ ν n+ −1/2 is the covariance matrix of a tensor product of single–mode thermal states with
average photon number n̄∓ ≡ n∓ − 1/2 in the two modes

∞

k=0



n̄
1 + n̄

k

|kihk| ,

(11)

1
1
,
= √
2n̄ + 1
2 Det σ

(17)

a two–mode squeezing Stm (r) = diag( er , e−r , e−r , er )
and a local squeezing Sloc (r1 , r2 ) = Ssm (r1 , 0) ⊕
Ssm (r2 , 0), resulting from the direct product of two single–
mode squeezing operators with null phase. Note that
Stm (r) = Sloc (r, −r), so that the only global (nonlocal)
operations in the decomposition of Eq. (17) are the two rotations. We note that an equivalent decomposition has been
recently demonstrated for generic multimode pure Gaussian states [16]: the authors have shown that for any decomposition of a multimode pure Gaussian state with respect to
a bipartite division of the modes, the state can always be
expressed as a product state involving entangled two-mode
squeezed states and single-mode local states at each side.

(12)

and Ssm (r, ϕ) = exp( 12 r e−i2ϕ a2 − 21 r ei2ϕ a†2 ) is the
single–mode squeezing operator. Being unitary, the latter does not affect the values of the traces in Eqns. (1)–
(2), computed on the diagonal density matrix νn̄ given by
Eq. (12). One has then
µ(̺) =

A = Sloc (r1 , r2 )R(ξ)Stm (r)R(η)Sl

is a symplectic operation belonging to Sp(4,R) . Transformation A is made up by a local operation Sl , two rotations
R(φ), with


cos φ
0
− sin φ
0
 0
cos φ
0
− sin φ 
 , (18)
R(φ) = 

 sin φ
0
cos φ
0
0
sin φ
0
cos φ

where ν n̄ is a thermal state of mean photon number n̄
1 X
ν n̄ =
1 + n̄

(16)

while

Eq. (10) implies that a Gaussian state σ is pure if and only
if Det σ = 1/22n .
For single–mode systems, the Von Neumann entropy can
be easily computed as well. Neglecting first moments, any
single–mode Gaussian state ̺ can in fact be written as
†
̺ = Ssm (r, ϕ)ν n̄ Ssm
(r, ϕ) ,

ν n∓ = diag(n− , n− , n+ , n+ ) ,

(13)


n̄ + 1
+ ln(n̄ + 1)
SV (̺) = n̄ ln
n̄




1−µ
2µ
1+µ
=
− ln
. (14)
ln
2µ
1−µ
1+µ


Proof.
In order to prove the statement expressed
by Eq. (15), we consider the equivalent expression
A−1T σA−1 = ν n∓ and show that it is realized by some
A, n− , n+ for any given σ.
First, we choose Sl to bring σ to its standard form, given
by Eq. (9). We then apply to σ sf the rotated two–mode
squeezing R(η)−1 Stm (r)−1 , taking the covariance matrix
to the form


s 0 0 0
 0 m 0 c 


 0 0 s 0 ,
0 c 0 n

Eq. (14), first achieved in Ref. [15], shows that for single–
mode Gaussian states the Von Neumann entropy is a monotonically increasing function of the linear entropy, so that
SV and SL yield the same characterization of mixedness.
In fact, both SV and SL are fully determined by the same
symplectic invariant Det σ. As we will now see, this is no
longer true for two–mode Gaussian states.
To find an expression for the Von Neumann entropy of
a generic Gaussian state of a two–mode system, we must
find a general expression for the state analogous to that provided by Eq. (11) for a single–mode system. Neglecting

which is convenient, due to the invariance of the submatrix
δ = diag(s, s), see Eqns. (5), under two–mode rotations
of the form Eq. (18). The second rotation R(ξ)−1 leaves
3

δ unchanged and can be chosen to make c null, yielding a
state of the form


s 0 0 0
 0 m′ 0 0 


 0 0 s 0 ,
0 0 0 n′

The solution of the system yields
s
p
∆(σ) ∓ ∆(σ)2 − 4 Det σ
.
n∓ (σ) =
2
Note that Ineq. (6) is equivalent to

1
,
(22)
2
whereas the necessary and sufficient criterion for a state to
be pure reads n− = n+ = 1/2 (one can easily show that it
is equivalent to Det σ = 1/16).
Knowledge of the symplectic eigenvalues and of the associated mean thermal photon numbers allows finally to determine the Von Neumann entropy SV (σ) of an arbitrary
two–mode Gaussian state σ. We have:
Proposition 1. The Von Neumann entropy SV (σ) of an arbitrary two–mode Gaussian state σ equals the one of the
tensor product of thermal states ν n∓ , associated to σ via
the correspondence established by Eq. (15), and its expression reads
n∓ ≥

which can be finally put in the desired form ν n− −1/2 ⊕
ν n+ −1/2 by means of the local squeezing Sloc (r1 , r2 ). 
Lemma 1 introduces an equivalence relation on the set
of Gaussian states, associating to any Gaussian state σ a
product of thermal states ν n∓ , by means of the correspondence defined by Eq. (15). The quantities n∓ are known
as the symplectic eigenvalues of σ, while transformation A
performs a symplectic diagonalization [12, 8, 17]. We note
that the decomposition of the symplectic operation A given
by Eq. (17) is the particular two–mode case of the general
decomposition of a symplectic operation [18].
Let us now focus on the quantity
∆(σ) = Det α + Det β + 2 Det γ ,

(19)

SV (σ) = f [n− (σ)] + f [n+ (σ)] ,

where α, β, and γ are defined as in Eq. (4). We have:
Lemma 2. ∆(σ) is invariant under the action of the symplectic transformation A defined by Eq. (15).
Proof. ∆(σ) is clearly invariant under local operations,
such as Sl , Sloc and Stm . As for the non local rotations
which enter in the definition of A, let us notice that they act
on covariance matrices of the following form


u 0 j 0
 0 v 0 k 

σ̃ = 
 j 0 w 0 ,
0 k 0 z

1
1
1
1
f (x) ≡ (x + ) ln(x + ) − (x − ) ln(x − ) . (24)
2
2
2
2
Proof. The symplectic operation A described by Eq. (17)
corresponds to a unitary transformation in the Hilbert space
H which cannot affect the value of the trace appearing in
the definition of SV , according to Eq. (1). Therefore, exploiting Eq. (14) and the additivity of the Von Neumann
entropy for tensor product states, one obtains Eq. (23). 
We have shown that the Von Neumann entropy of a two–
mode Gaussian state σ depends on the two invariants ∆(σ)
and Det σ, whereas the purity of σ is completely determined by Det σ alone, just as in the single–mode case.
This implies that the hierarchy of mixedness established by
the Von Neumann entropy on the set of Gaussian states differs, in the two–mode case, from that induced by the linear entropy. States may exist with a given linear entropy,
i.e. with a given Det σ, but with different Von Neumann
entropies, i.e. with different ∆(σ)’s. The Von Neumann
entropy thus provides a richer characterization of the state’s
lack of information.

∆(σ̃) = Tr (δǫ) .
Such an expression is manifestly invariant under the action
of identical rotations R(φ) on the submatrices δ and γ, see
Eqns. (5) and (18). 
The quantity Det σ is obviously invariant as well under
the action of A since, for any symplectic transformation S,
one has Det S = 1. Exploiting the invariance of Det σ
and ∆(σ) one can determine the symplectic eigenvalues
n∓ which characterize a generic Gaussian state σ, according to Eq. (15)
=

(23)

with n∓ given by Eqns. (21) and

for which one has

Det σ

(21)

4

Det ν n∓ = n2− n2+ ,

Symplectic eigenvalues, mutual information and correlations

The mutual information I(σ) of a Gaussian state σ is defined as

(20)
∆(σ) = ∆(ν n∓ ) = n2− + n2+ .

I(σ) = SV (σ 1 ) + SV (σ 2 ) − SV (σ) ,
4

(25)

where σ i stands for the reduced single–mode state obtained
by tracing over subsystem j 6= i. Knowledge of SV (σ)
leads to the following:
Proposition 2. The mutual information I(σ) of an arbitrary two–mode Gaussian state is

symmetric states. Even the quantification of quantum correlation provided by negativity [8], which is computable
also for non symmetric states, reduces for a two–mode
Gaussian state σ to a simple function of ñ− (σ).
The dependence of entanglement on the eigenvalue
ñ− (σ) is due to the fact that the biggest eigenvalue of
the partially transposed covariance matrix σ̃ can be easily shown to fulfill Ineq. (22). Thus ñ− (σ) alone can be
responsible of the violation of the PPT (‘positivity of the
partial transpose’) criterion for separability [6], which can
be recast as
1
ñ− (σ) ≥ .
(29)
2
All the quantification of entanglement for two–mode Gaussian states available at present just quantify the violation of
this inequality.
We have extensively shown how both quantum and classical correlations of a Gaussian state are encoded in symplectic spectra of the global, reduced and partially transposed covariance matrices of the state.

I(σ) = f (a) + f (b) − f [n− (σ)] − f [n+ (σ)] , (26)
√
√
where a = Det α , b = Det β , and f(x) is the same
as in Eq. (24).
Proof. Let us consider the reduction of σ to its standard
form σ sf , defined by Eq. (9). The matrix elements a and
b of σ sf are easily recovered from a generic σ, because
Det α = a2 and Det β = b2 are Sp(2,R) ⊕ Sp(2,R) invariant. Notice that, since either SV (σ) or the quantities
SV (σ i )’s are invariant under local unitary operations, one
has I(σ) = I(σ sf ). Partial tracing of σ sf over subsystem
i yields σ 1 = diag(a, a) and σ 2 = diag(b, b), so that,
finally, Eq. (14) and Proposition 1 lead to Eq. (26). 
Notice that a and b constitute the symplectic spectra of, respectively, σ 1 and σ 2 . Eq. (26) emphasizes the relevant
role played by the symplectic eigenvalues n∓ (σ sf ) in determining the total amount of correlations contained in a
quantum state of a continuous variable system, in striking
analogy to the role played by the symplectic eigenvalues of
the partial transpose of σ sf in characterizing the amount of
quantum correlations [9, 10].
To better clarify this point, let us consider a symmetric
state σ sym , i.e. a state whose standard form fulfills a = b,
so that its mutual information reads, according to Eq. (26)

5

In conclusion, we have characterized mixedness and total
correlations of two–mode Gaussian states by deriving their
Von Neumann entropy and mutual information. Comparing
these quantities with the entanglement of formation of symmetric states shows that a crucial information about quantum and classical correlations lies in the symplectic eigenvalues of the covariance matrix and of its partial transpose.
The problem is still left open of determining a fully satisfactory quantification of the purely quantum correlations in
a general two–mode Gaussian state.

I(σ sym ) = 2f (a) − f [n− (σ sym )] − f [n+ (σ sym )] ,
(27)
p
(a ∓ c1 )(a ∓ c2 ).
with symplectic eigenvalues n∓ =
On the other hand, the symplectic eigenvalues of the
partially transposed covariance matrix σ̃ sym (obtained
from σ sym by switching
p the sign of c2 , see [6]) are
ñ∓ ≡ n∓ (σ̃ sym ) =
(a ∓ c1 )(a ± c2 ). In particular,
for
an
entangled
state,
the
smallest eigenvalue is ñ− =
p
(a − |c1 |)(a − |c2 |). 1
The symplectic eigenvalue ñ− encodes all the information
about the entanglement of the state, since the necessary and
sufficient criterion for entanglement reduces to ñ− < 1/2,
while the entanglement of formation EF (σ sym ) reads 2

Acknowledgements
Financial support from INFM, INFN, and MIUR under national project PRIN-COFIN 2002 is acknowledged.

References
[1] Quantum Information Theory with Continuous Variables, S. L. Braunstein and A. K. Pati Eds. (Kluwer,
Dordrecht, 2002).

EF (σ sym ) = max{0, g[ñ−]} ,
(28)


 1
 1
2
2
2
1
1
( −x)
( +x)
( −x)2
( +x)
− 2 2x ln 2 2x
with g(x) ≡ 2 2x ln 2 2x
(see [9] for details); it correctly reduces to I(σ)/2 for pure

[2] H. J. Kimble and D. F. Walls, J. Opt. Soc. Am. B 4,
10 (1987).

1 If σ is entangled, then Det γ < 0, see Ref. [6].
2E

F (̺) ≡ min{pi ,|ψi i}

Conclusions

P

pi E(|ψi ihψi |), where E(|ψihψ|) is the
entropy of entanglement of the pure state |ψi, defined as the Von Neumann
entropy of its reduced densityPmatrix, and the min is taken over all the
pure states realization of ̺ =
pi |ψi ihψi |.

[3] H. P. Yuen and A. Kim, Phys. Lett. A 241, 135 (1998);
F. Grosshans, G. Van Assche, J. Wenger, R. Brouri, N.
J. Cerf, and P. Grangier, Nature 421, 238 (2003).
5

[4] A. Furusawa, J. L. Sorensen, S. L. Braunstein, C. A.
Fuchs, H. J. Kimble, and E. S. Polzik, Science 282,
706 (1998); T. C. Zhang, K. W. Goh, C. W. Chou, P.
Lodahl, and H. J. Kimble, Phys. Rev. A 67, 033802
(2003).
[5] S. Lloyd and S. L. Braunstein, Phys. Rev. Lett. 82,
1784 (1999); T. C. Ralph, W. J. Munro, and G. J. Milburn, quant-ph/0110115 (2001).
[6] R. Simon, Phys. Rev. Lett. 84, 2726 (2000).
[7] L.-M. Duan, G. Giedke, J. I. Cirac, and P. Zoller,
Phys. Rev. Lett. 84, 2722 (2000).
[8] G. Vidal and R. F. Werner, Phys. Rev. A 65, 032314
(2001).
[9] G. Giedke, M. M. Wolf, O. Krüger, R. F. Werner, and
J. I. Cirac, Phys. Rev. Lett. 91 107901 (2003).
[10] M. M. Wolf, G. Giedke, O. Krüger, R. F. Werner, and
J. I. Cirac, quant–ph/0306177 (2003).
[11] L. Henderson and V. Vedral, J. Phys. A 34, 6899
(2001).
[12] A. S. Holevo, M. Sohma, and O. Hirota, Phys. Rev. A
59, 1820 (1999); A. S. Holevo and R. F. Werner, ibid.
63, 032312 (2001).
[13] See, e.g., S. M. Barnett and P. M. Radmore, Methods in Theoretical Quantum Optics (Clarendon Press,
Oxford, 1997).
[14] R. Simon, E. C. G. Sudarshan, and N. Mukunda,
Phys. Rev. A 36, 3868 (1987).
[15] G. S. Agarwal, Phys. Rev. A 3, 828 (1971).
[16] A. Botero and B. Reznik, Phys. Rev. A 67, 052311
(2003).
[17] J. Williamson, Am. J. Math. 58, 141 (1936).
[18] H. Huang and G. S. Agarwal, Phys. Rev. A 49, 52
(1994).

6

