General parameter-shift rules for quantum gradients
David Wierichs1,2 , Josh Izaac1 , Cody Wang3 , and Cedric Yen-Yu Lin3
1 Xanadu, Toronto, ON, M5G 2C8, Canada
2 Institute for Theoretical Physics, University of Cologne, Germany

arXiv:2107.12390v3 [quant-ph] 22 Mar 2022

3 AWS Quantum Technologies, Seattle, Washington 98170, USA

Variational quantum algorithms are ubiquitous in applications of noisy intermediatescale quantum computers. Due to the structure of conventional parametrized quantum
gates, the evaluated functions typically are finite Fourier series of the input parameters. In
this work, we use this fact to derive new, general parameter-shift rules for single-parameter
gates, and provide closed-form expressions to
apply them. These rules are then extended
to multi-parameter quantum gates by combining them with the stochastic parameter-shift
rule. We perform a systematic analysis of
quantum resource requirements for each rule,
and show that a reduction in resources is possible for higher-order derivatives. Using the example of the quantum approximate optimization algorithm, we show that the generalized
parameter-shift rule can reduce the number of
circuit evaluations significantly when computing derivatives with respect to parameters that
feed into many gates. Our approach additionally reproduces reconstructions of the evaluated function up to a chosen order, leading to
known generalizations of the Rotosolve optimizer and new extensions of the quantum analytic descent optimization algorithm.

1 Introduction
With the advent of accessible, near-term quantum
hardware, the ability to rapidly test and prototype
quantum algorithms has never been as approachable
[1, 2, 3, 4]. However, many of the canonical quantum algorithms developed over the last three decades
remain unreachable in practice — requiring a large
number of error corrected qubits and significant circuit depth. As a result, a new class of quantum algorithms — variational quantum algorithms (VQAs)
[5, 6] — have come to shape the noisy intermediatescale quantum (NISQ) era. First rising to prominence with the introduction of the variational quantum eigensolver (VQE) [7], they have evolved to cover
topics such as optimization [8], quantum chemistry
[9, 10, 11, 12, 13], integer factorization [14], compilation [15], quantum control [16], matrix diagonalizaDavid Wierichs: wierichs@thp.uni-koeln.de

tion [17, 18], and variational quantum machine learning [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31].
These algorithms have a common structure: a
parametrized circuit is executed and a cost function is composed from expectation values measured
in the resulting state. A classical optimization routine is then used to optimize the circuit parameters
by minimizing said cost function. Initially, gradientfree optimization methods, such as Nelder-Mead and
COBYLA, were common. However, gradient-based
optimization provides significant advantages, from
convergence guarantees [32] to the availability of
workhorse algorithms (e.g., stochastic gradient descent) and software tooling developed for machine
learning [33, 34, 35, 36, 37].
The so-called parameter-shift rule [16, 23, 38, 39]
can be used to estimate the gradient for these optimization techniques, without additional hardware
requirements and — in contrast to naı̈ve numerical methods — without bias; the cost function is
evaluated at two shifted parameter positions, and
the rescaled difference of the results forms an unbiased estimate of the derivative. However, this twoterm parameter-shift rule is restricted to gates with
two distinct eigenvalues, potentially requiring expensive decompositions in order to compute hardwarecompatible quantum gradients [40]. While various extensions to the shift rule have been discovered, they
remain restricted to gates with a particular number
of distinct eigenvalues [10, 41].
In this manuscript, we use the observation that the
restriction of a variational cost function to a single
parameter is a finite Fourier series [42, 43, 44, 45];
as a result, the restricted cost function can be reconstructed from circuit evaluations at shifted positions
using a discrete Fourier transform (DFT). By analytically computing the derivatives of the Fourier series,
we extract general parameter-shift rules for arbitrary
quantum gates and provide closed-form expressions
to apply them. In the specific case of unitaries with
equidistant eigenvalues, the general parameter-shift
rule recovers known parameter-shift rules from the
literature, including the original two-term parametershift rule. We then generalize our approach in two
steps: first from equidistant to arbitrary eigenvalues
of the quantum gate, and from there — by making use
of stochastic parameter shifts — to more complicated
unitaries like multi-parameter gates. This enables us

Accepted in Quantum 2022-03-18, click title to verify. Published under CC-BY 4.0.

1

Figure 1: Overview of existing and new parameter-shift rules
for first-order univariate derivatives as Venn diagram on the
space of quantum gates. Each rule produces the analytic
derivative for a set of gates, with more general rules reproducing the more specific ones. For gates of the form
U (x) = exp(ixG) the rules are deterministic (left) whereas
more involved gates of the form UF = exp(i(xG + F )) require stochastic evaluations of shifted values (right). See
Sec. 2.2 for a summary of previously known shift rules. The
fermionic four-term shift rule in Ref. [41] covers the same
gates as the shown four-term rule (purple).

to cover all practically relevant quantum gates. An
overview of the existing parameter-shift rules and our
new results is shown in Fig. 1.
Afterwards, we perform an extensive resource analysis to compare the computational expenses required
by both the general shift rule presented here, and
decomposition-based approaches. In particular, we
note that evaluating the cost of gradient recipes by
comparing the number of unique executed circuits
leads to fundamentally different conclusions on the
optimal differentiation technique than when comparing the total number of measurements.
Our analysis not only is fruitful for understanding
the structure of variational cost functions, but also
has several practical advantages. Firstly, second-order
derivatives (such as the Hessian [46] and the FubiniStudy metric tensor [47, 48]) can be computed with
fewer evaluations compared to naı̈vely iterating the
two-term parameter-shift rule. We also show, using
the example of the quantum approximate optimization
algorithm (QAOA), that the generalized parametershift rule can reduce the number of quantum circuit
evaluations required for ansätze with repeated parameters.
Finally, we generalize the quantum analytic descent
(QAD) algorithm [49] using the reconstruction of variational cost functions discussed here. We also reproduce the known generalizations of Rotosolve [50, 51]
from single Pauli rotations to groups of rotations controlled by the same parameter [42, 45]; reconstruct-

ing functions with arbitrary spectrum extends this algorithm even further. Furthermore, the cost reduction for the gradient we present in the context of
QAOA applies to Rotosolve as well. Similarly, future improvements that reduce the cost for gradient
computations might improve the efficiency of these
model-based algorithms, based on the analysis presented here.
This manuscript is structured as follows. In Sec. 2,
we lay out the setting for our results by deriving the
general functional form for variational cost functions,
followed by a survey of existing parameter-shift rules.
In Sec. 3 we show how to fully reconstruct univariate variational cost functions from a finite number of
evaluations assuming an equidistant frequency spectrum, and derive parameter-shift rules for arbitraryorder univariate derivatives, including a generalization of the stochastic parameter-shift rule. In Sec. 4
we demonstrate how to compute second-order derivatives, in particular the Hessian and the metric tensor, more cheaply compared to existing methods. In
Sec. 5 we discuss applications, applying the new generalized parameter-shift rules to QAOA, and using
the full univariate reconstruction to extend existing
model-based optimization methods. We end the main
text in Sec. 6 with a discussion of our work and potential future directions. Finally, in the appendix we
summarize some technical derivations (App. A), and
extend the results to more general frequency spectra
(App. B). The general stochastic parameter-shift rule
and details on quantum analytic descent can be found
in Apps. C and D.
Related work: In Ref. [42], the functions of VQAs
were considered as Fourier series and parameter-shift
rules were derived. Regarding the shift rules, the authors of Ref. [42] consider integer eigenvalues and derive a rule with 2R + 1 evaluations for equidistant
eigenvalues. In particular, the two-term and fourterm shift rules are reviewed and formulated as special cases with fewer evaluations than the general result presented there. In contrast, our work results in
the exact generalization of those shift rules, which requires 2R evaluations. Remarkably, Refs. [42, 45] also
propose a generalized Rotosolve algorithm prior to its
eponymous paper.
In addition, during the final stages of preparation
of this work, a related work considering algebraic extensions of the parameter-shift rule appeared online
[52]. The general description of quantum expectation values in Sec. 2.1 of the present work, along
with its initial consequences in Sec. 3.1, are shown
in Sec. II A of this preprint. We present a simpler
derivation and further explore the implications this
description has. The generalization of the parametershift rule in Ref. [52] is obtained by decomposing the
gate generator using Cartan subalgebras, which can
yield fewer shifted evaluations than decompositions
of the gate itself. In particular, decompositions into

Accepted in Quantum 2022-03-18, click title to verify. Published under CC-BY 4.0.

2

non-commuting terms, which do not lead to a gate decomposition into native quantum gates directly, can
be used in this approach.
At a similar time, yet another work appeared
[53], presenting a derivation similar to Sec. 2.1 and
parameter-shift rules for the first order derivative.
These rules are based on the ideas discussed here in
Secs. 3.1 and 3.2.

2 Background
We start by deriving the form of a VQA cost function
of a single parameter for a general single-parameter
quantum gate. Then we review known parametershift rules and briefly discuss resource measures to
compare these gradient recipes.

stead; a common example for this is
G=

P
X

±Pk

(4)

k=1

for commuting Pauli words Pk (Pk Pk0 = Pk0 Pk ),
which yields the frequencies [P] and thus R = P.
In the following, we implicitly assume a mapping
between the two indices j, k ∈ [d] and the frequency
index ` ∈ [R] such that c` = c`(j,k) is well-defined2 .
We can then write the expectation value as a trigonometric polynomial (a finite-term Fourier series):
E(x) = a0 +

R
X

c` eiΩ` x +

`=1

= a0 +

R
X

R
X

c` e−iΩ` x

(5)

`=1

a` cos(Ω` x) + b` sin(Ω` x),

(6)

`=1

2.1 Cost functions arising from quantum gates
Let us first consider the expectation value for a general gate U (x) = exp(ixG), defined by a Hermitian
generator G and parametrized by a single parameter
x. Let |ψi denote the quantum state that U is applied
to, and B the measured observable1 . The eigenvalues
of U (x) are given by {exp(iωj x)}j∈[d] with real-valued
{ωj }j∈[d] where we denote [d] := {1, . . . , d} and have
sorted the ωj to be non-decreasing. Thus, we have:
E(x) := hψ| U † (x)BU (x) |ψi

(1)

2.2 Known parameter-shift rules

d
X

=

ψj eiωj x bjk ψk eiωk x

(2)

j,k=1
d h
X

=

ψj bjk ψk ei(ωk −ωj )x

(3)

j,k=1
j<k

+ ψj bjk ψk ei(ωk −ωj )x
+

with frequencies given by the differences {Ω` }, where
we definedP
c` =: 21 (a` − ib` ) ∀` ∈ [R] with a` , b` ∈ R,
and a0 := j |ψj |2 bjj ∈ R.
Since E(x) is a finite-term Fourier series, the coefficients {a` } and {b` } can be obtained from a finite number of evaluations of E(x) through a discrete
Fourier transform. This observation (and variations
thereof in Sec. 3) forms the core of this work: we can
obtain the full functional form of E(x) from a finite
number of evaluations of E(x), from which we can
compute arbitrary order derivatives.

d
X

i

|ψj |2 bjj ,

j=1

where we have expanded B and |ψi in the eigenbasis
of U , denoted by bjk and ψj , respectively.
We can collect the x-independent part into coefficients cjk := ψj bjk ψk and introduce the R unique positive differences {Ω` }`∈[R] := {ωk − ωj |j, k ∈ [d], ωk >
ωj }. Note that the differences are not necessarily equidistant, and that for r = {ωj }j∈[d] unique
eigenvalues of the gate generator, there are at most
unique differences. However, many quanR ≤ r(r−1)
2
tum gates will yield R ≤ r equidistant differences in-

Parameter-shift rules relate derivatives of a quantum
function to evaluations of the function itself at different points. In this subsection, we survey known
parameter-shift rules in the literature.
For functions of the form (6) with a single frequency
Ω1 = Ω (i.e., G has two eigenvalues), the derivative
can be computed via the parameter-shift rule [16, 23,
38]
E 0 (0) =

Ω
[E(x1 ) − E(−x1 )],
2 sin(Ωx1 )

(7)

where x1 is a freely chosen shift angle from (0, π) 3 .
This rule was generalized to gates with eigenvalues {−1, 0, 1}, which leads to R = 2 frequencies,
in Refs. [41, 10] in two distinct ways. The rule in
Ref. [10] is an immediate generalization of the one
above:
E 0 (0) = y1 [E(x1 ) − E(−x1 )]

(8)

− y2 [E(x2 ) − E(−x2 )],
2 That is, `(j, k) = `(j 0 , k 0 ) ⇔ ω

k − ωj = ωk0 − ωj 0 .

1 Here we consider any pure state in the Hilbert space; in the

3 The position 0 for the derivative is chosen for convenience

context of VQAs, |ψi is the state prepared by the subcircuit
prior to U (x). Similarly, B includes the subcircuit following up
on U (x).

but the rule can be applied at any position. To see this, note
that shifting the argument of E does not change its functional
form.

Accepted in Quantum 2022-03-18, click title to verify. Published under CC-BY 4.0.

3

with freely chosen shift angles x1,2 and corresponding
coefficients y1,2 , requiring four evaluations to obtain
E 0 (0). A particularly symmetric choice of shift
angles
√
2±1
√
is x1,2 = π/2 ∓ π/4 with coefficients y1,2 = 2 2 . In
contrast, the rule in Ref. [41] makes use of an auxiliary
gate to implement slightly altered circuits, leading to
a structurally different rule:
E 0 (0) =

1 +
−
−
+
[E − E−
+ E+
− E−
],
4 +

(9)

α
where E±
is the measured energy when replacing the
gate U (x) in question by U (x ± π/2) exp(∓αi π4 P0 )
and P0 is the projector onto the zero-eigenspace of
the generator of U . Remarkably, this structure allows
a reduction of the number of distinct circuit evaluations to two if the circuit and the Hamiltonian are
real-valued, which is often the case for simulations of
fermionic systems and forms a unique feature of this
approach. This second rule is preferable whenever this
condition is fulfilled, the auxiliary gates exp(±i π4 P0 )
are available, and simultaneously the number of distinct circuits is the relevant resource measure.
Furthermore, the two-term parameter-shift rule
Eq. (7) was generalized to gates with the more complicated gate structure UF (x) = exp(i(xG + F )) via
the stochastic parameter-shift rule [39]
Z 1
Ω
E 0 (x0 ) =
[E+ (t) − E− (t)]dt. (10)
2 sin(Ωx1 ) 0

Here, E± (t) is the energy measured in the state prepared by a modified circuit that splits UF (x0 ) into
UF (tx0 ) and UF ((1 − t)x0 ), and interleaves these two
gates with UF =0 (±x1 ). See Sec. 3.6 and App. C for
details. The first-order parameter-shift rules summarized here and their relationship to each other is also
visualized in Fig. 1.
A parameter-shift rule for higher-order derivatives
based on repeatedly applying the original rule has
been proposed in Ref. [46]. The shift can be chosen smartly so that two function evaluations suffice
to obtain the second-order derivative:
E 00 (0) =

1
[E(π) − E(0)],
2

(11)

which like Eq. (7) is valid for single-frequency gates.
Various expressions to compute combinations of
derivatives with few evaluations were explored in
Ref. [54].

2.3 Resource measures for shift rules
While the original parameter-shift rule Eq. (7) provides a unique, unbiased method to estimate the
derivative E 0 (0) via evaluations of E if it contains
a single frequency, we will need to compare different
shift rules for the general case. To this end, we consider two resource measures. Firstly, the number of
distinct circuits that need to be evaluated to obtain all

terms of a shift rule, Neval . This is a meaningful quantity on both, simulators that readily produce many
measurement samples after executing each unique circuit once, as well as quantum hardware devices that
are available via cloud services. In the latter case,
quantum hardware devices are typically billed and
queued per unique circuit, and as a result Neval often
dictates both the financial and time cost. Note that
overhead due to circuit compilation and optimization
scale with this quantity as well.
Secondly, we consider the overall number N of measurements — or shots — irrespective of the number
of unique circuits they are distributed across. To this
end, we approximate the physical (one-shot) variance
σ 2 of the cost function E to be constant across its domain4 . For an arbitrary quantity ∆ computed from
M values of E via a shift rule,
∆=

M
X

yµ E(xµ ),

(12)

µ

we obtain the variance for the estimate of ∆ as
ε2 =

M
X
µ

|yµ |2

σ2
,
Nµ

(13)

where Nµ expresses the number of shots used to measure E(xµ ). For a total budget of N shots, the optimal shot allocation is Nµ = N |yµ |/kyk1 such that
N=

σ 2 kyk21
.
ε2

(14)

This can be understood as the number of shots needed
to compute ∆ to a tolerable standard deviation ε.
The number of shots N is a meaningful quantity for
simulators whose runtime scales primarily with the
number of requested samples (e.g., Amazon Braket’s
TN1 tensor network simulator [1]), and for actual
quantum devices when artificial resource measures
like pricing per unique circuit and queueing time do
not play a role.
In this work we will mostly use Neval to compare
the requirements of different parameter-shift rules as
it is more accessible, does not rely on the assumption
of constant physical variance like N does, and the
coefficients y to estimate N are simply not known
analytically in most general cases. For the case of
equidistant frequencies and shift angles as discussed
in Sec. 3.4 we will additionally compare the number
of shots N in Sec. 3.5.

3 Univariate cost functions
In this section we study how a quantum cost function, which in general depends on multiple parameters, varies if only one of these parameters is changed.
4 As it is impossible in general to compute σ 2 analytically, we
are forced to make this potentially very rough approximation.

Accepted in Quantum 2022-03-18, click title to verify. Published under CC-BY 4.0.

4

The results of this section will be sufficient to evaluate
the gradient as well as the diagonal of the Hessian of a
quantum function. We restrict ourselves to functions
that can be written as the expectation value of an observable with respect to a state that is prepared using
a unitary U (x) = exp(ixG) — capturing the full dependence on x. That is, all parameters but x are fixed
and the operations they control are considered as part
of the prepared state and the observable. As shown in
Sec. 2.1, this yields a trigonometric polynomial, i.e.,

E(x) = a0 +

R
X

a` cos(Ω` x) + b` sin(Ω` x).

(15)

`=1

In the following, we will assume the frequencies to be
equidistant, i.e., Ω` = `Ω, and generalize to arbitrary
frequencies in App. B. While it is easy to construct
gate sequences that do not lead to equidistant frequencies, many conventional gates and layers of gates
do yield such a regular spectrum. The equidistant
frequency case has two major advantages over the
general case: we can derive closed-form parametershift rules (Sec. 3.4); and the number of circuits required for the parameter-shift rule scales much better
(Sec. 3.5).
Without loss of generality, we further restrict the
frequencies to integer values, i.e., Ω` = `. For Ω 6=
1, we may rescale the function argument to achieve
Ω` = ` and once we reconstruct the rescaled function,
the original function is available, too.

3.1 Determining the full dependence on x
As we have seen, the functional form of E(x) is known
exactly. We can thus determine the function by computing the 2R + 1 coefficients {a` } and {b` }. This is
the well-studied problem of trigonometric interpolation (see e.g., [55, Chapter X]).
To determine E(x) completely, we can simply evaluate it at 2R + 1 distinct points xµ ∈ [−π, π). We
obtain a set of 2R + 1 equations

E(xµ ) = a0 +

R
X

3.2 Determining the odd part of E(x)
It is often the case in applications that we only need
to determine the odd part of E,
1
(E(x) − E(−x))
2
R
X
=
b` sin(`x).

Eodd (x) =

(16)
(17)

`=1

For example, calculating odd-order derivatives of
E(x) at x = 0 only requires knowledge of Eodd (x),
since those derivatives of the even part vanish. Note
that the reference point with respect to which Eodd is
odd may be chosen arbitrarily, and does not have to
be 0.
The coefficients in Eodd can be determined by evaluating Eodd at R distinct points xµ with 0 < xµ < π.
This gives us a system of R equations

Eodd (xµ ) =

R
X

b` sin(`xµ ),

µ ∈ [R]

(18)

`=1

which we can use to solve for the R coefficients {b` }.
Using Eq. (16) we see that each evaluation of Eodd
can be done with two evaluations of E(x). Thus, the
odd part of E can be completely determined with 2R
evaluations of E, saving one evaluation compared to
the general case. Note however that the saved E(0)
evaluation is evaluated regardless in many applications, and may be used to recover the full reconstruction — so, in effect, this saving does not have a significant impact5 .

3.3 Determining the even part of E(x)
We might similarly want to obtain the even part of
E,
1
(E(x) + E(−x))
2
R
X
= a0 +
a` cos(`x),

Eeven (x) =

(19)
(20)

`=1

a` cos(`xµ ) + b` sin(`xµ ), µ ∈ [2R]0

`=1

where we denote [2R]0 := {0, 1, . . . , 2R}. We can then
solve these linear equations for {a` } and {b` }; this process is in fact a nonuniform discrete Fourier transform
(DFT).
2πµ
, µ = −R, . . . , R,
A reasonable choice is xµ = 2R+1
in which case the transform is the usual (uniform)
DFT. For this choice, an explicit reconstruction for E
follows directly from [55, Chapter X]; we reproduce it
in App. A.1.1.

which can be used to compute even-order derivatives
of E.
Determining Eeven (x) requires R + 1 evaluations of
Eeven , which leads to 2R + 1 evaluations of E for arbitrary frequencies. However, in the case where Ω` are
integers, R + 1 evaluations of Eeven can be obtained
5 If E(0) is available, we can recover the full function, allowing us to, for example, evaluate its second derivative E 00 (0)
“for free”. However, in practice many more repetitions may be
needed for reasonable accuracy. This fact was already noted in
[46] for the R = 1 case.

Accepted in Quantum 2022-03-18, click title to verify. Published under CC-BY 4.0.

5

with 2R evaluations of E(x) by using periodicity:
Eeven (0) = E(0)
1
Eeven (xµ ) = (E(xµ ) + E(−xµ )),
2
0 < xµ < π, µ ∈ [R − 1]

(21)

Eeven (π) = E(π).

(23)

(22)

Thus, in this case 2R evaluations of E(x) suffice to
determine its even part, saving one evaluation over
the general case. In contrast to the odd part, this
saving genuinely reduces the required computations as
E(0) is also used in the cheaper computation of {a` };
therefore, if E(0) is already known, we only require
2R − 1 new evaluations.
We note that even though both the odd and the
even part of E(x) require 2R evaluations, the full
function can be obtained at the price of 2R + 1 evaluations.

3.4 Explicit parameter-shift formulas
Consider again the task of determining Eodd (Eeven )
based on its value at the shifted points {xµ } with
µ ∈ [R] (µ ∈ [R]0 ). This can be done by linearly combining elementary functions that vanish on all but one
of the {xµ }, i.e., kernel functions, using the evaluation E(xµ ) as coefficients. If we restrict ourselves to
µ
evenly spaced points xµ = 2µ−1
2R π (xµ = R π), we can
choose these functions to be Dirichlet kernels. In addition to a straightforward reconstruction of the odd
(even) function this delivers the general parametershift rules, which we derive in App. A.1:

E 0 (0) =

2R
X


E

µ=1

E 00 (0) = −E(0)

2µ − 1
π
2R



(−1)µ−1
,
4R sin2 2µ−1
4R π

(24)

2R−1
X  µπ  (−1)µ−1
2R2 + 1

E
+
µπ .
6
R 2 sin2 2R
µ=1

(25)
We remark that derivatives of higher order can be
obtained in an analogous manner, and with the same
function evaluations for all odd (even) orders. Furthermore, this result reduces to the known two-term
(Eq. (7)) and four-term (Eq. (8)) parameter-shift rules
for R = 1 and R = 2, respectively, as well as the
second-order derivative for R = 1 (Eq. (11)).
We again note that the formulas above use different evaluation points for the first and second derivatives (2R evaluations for each derivative). Closedform parameter-shift rules that use 2R + 1 shared
points can be obtained by differentiating the reconstruction formula Eq. (57).

3.5 Resource comparison
As any unitary may be compiled from (single-qubit)
Pauli rotations, which satisfy the original parameter-

shift rule, and CNOT gates, an alternative approach
to compute E 0 (0) is to decompose U (x) into such
gates and combine the derivatives based on the elementary gates. As rotation gates about any multiqubit Pauli word satisfy the original parameter-shift
rule as well, a more coarse-grained decomposition
might be possible and yield fewer evaluations for this
approach.
For instance, for the MaxCut QAOA ansatz6 on a
graph G = (V, E) with vertices V and edges E, one of
the operations is to evolve under the problem Hamiltonian:


X
x
Za Zb 
(26)
UP (x) ∝ exp −i
2
(a,b)∈E

 x
Y
(27)
=
exp −i Za Zb .
2
(a,b)∈E

Eq. (26) treats UP (x) as a single operation with at
most M = |E| frequencies 1, . . . , R ≤ M , and we can
apply the generalized parameter-shift rules of this section. Alternatively, we could decompose UP (x) with
Eq. (27), apply the two-term parameter-shift rule to
each RZZ rotation, and sum up the contributions using the chain rule.
3.5.1

Number of unique circuits

If there are P gates that depend on x in the decomposition, this approach requires 2P unique circuit evaluations; as a result, the general parameter-shift rule
is cheaper if R < P. The evaluations used in the
decomposition-based approach cannot be expressed
by E directly because the parameter is shifted only
in one of the P gates per evaluation, which makes the
general parameter-shift rule more convenient and may
reduce compilation overhead for quantum hardware,
and the number of operations on simulators.
In order to compute E 00 (0) via the decomposition,
we need to obtain and sum the full Hessian of all
elementary gates that depend on x (see App. A.4.2),
which requires 2P 2 −P+1 evaluations, including E(0),
and thus is significantly more expensive than the 2R
evaluations for the general parameter-shift rule.
While the derivatives can be calculated from the
functional form of Eodd or Eeven , the converse is not
true for R > 1, i.e., the full functional dependence
on x cannot be extracted from the first and second
derivative alone. Therefore, the decomposition-based
approach would demand a full multivariate reconstruction for all P parametrized elementary gates to
obtain this dependence, requiring O(2P ) evaluations.
The approach shown here allows us to compute the
dependence in 2R + 1 evaluations and thus is the only
method for which the univariate reconstruction is viable.
6 A more detailed description of the QAOA ansatz can be
found in Sec. 5.1.

Accepted in Quantum 2022-03-18, click title to verify. Published under CC-BY 4.0.

6

3.5.2

Number of shots

For equidistant evaluation points, we explicitly know
the coefficients of the first and second-order shift rule
given in Eqs. (24, 25), and thus can compare the variance of the derivatives in the context and under the
assumptions of Sec. 2.3.
The coefficients satisfy (see App. A.4.1)
−1

2R 
X
2µ − 1
2
π
=R
4R sin
4R
µ=1
2R−1
 µπ −1
X 
2R2 + 1
= R2 .
+
2 sin2
6
2R
µ=1

This means that the variance-minimizing shot allocation requires a shot budget of
σ 2 R2
(28)
ε2
σ 2 R4
NgenPS, 2 =
(29)
ε2
using the generalized parameter-shift rule for the first
and second derivative, respectively.
Assuming integer-valued frequencies in the cost
function typically means, in the decomposition-based
approach, that x enters the elementary gates without
any additional prefactors7 . Thus, optimally all evaluations for the first-order derivative rule are performed
with the same portion of shots; whereas the secondorder derivative requires an adapted shot allocation
which, in particular, measures E(0) with high precision as it enters E 00 (0) with the prefactor P/2. This
yields (see App. A.4.2)
NgenPS, 1 =

σ2 P 2
(30)
ε2
σ2 P 4
Ndecomp, 2 =
.
(31)
ε2
Comparing with NgenPS, 1 and NgenPS, 2 above, we see
that the shot budgets are equal at P = R. That is,
for both the first and second derivative, the general
parameter-shift rule does not show lower shot requirements in general, in contrast to the previous analysis
that showed a significantly smaller number of unique
circuits for the second derivative. This shows that
the comparison of recipes for gradients and higherorder derivatives crucially depends on the chosen resource measure. In specific cases we may be able to
give tighter upper bounds on R so that R < P (see
Sec. 5.1) and the general shift rule becomes favourable
regarding the shot count as well.
Ndecomp, 1 =

assume the frequencies to be equidistant but address
arbitrary spectra directly. Additionally we make the
reference point x0 at which the derivative is computed
explicit.
In Ref. [39], the authors derive the stochastic
parameter-shift rule for gates of the form
UF (x) = exp(i(xG + F ))

(32)

where G is a Hermitian operator with eigenvalues ±1
(so that G2 = 1), e.g., a Pauli word. F is any other
Hermitian operator, which may not necessarily commute with G8 . Key to the derivation of the stochastic
rule is an identity relating the derivative of the quantum channel UF (x)[ρ] = UF† (x)ρUF (x) to the derivative of the generator channel G(x)[ρ] = i[(xG + F ), ρ].
We may extend this directly to the general parametershift rule for the case when G2 = 1 is no longer satisfied (see App. C for the derivation):

E 0 (x0 ) =

Z 1X
R

yµ [Eµ (x0 , t) − E−µ (x0 , t)]dt

0 µ=1

(33)
E±µ (x0 , t) := hBiUF (tx0 )U (±xµ )UF ((1−t)x0 )|ψi .
The integration is implemented in practice by sampling values for t for each measurement of Eµ (x0 , t)
and E−µ (x0 , t).
The stochastic parameter-shift rule in combination
with the generalized shift rule in Eq. (24) allows for
the differentiation of any unitary with equidistant frequencies. As F in UF (x) above is allowed to contain terms that depend on other variational parameters, this includes multi-parameter gates in particular.
Furthermore, combining Eq. (33) with the generalized
shift rule for arbitrary frequencies in Eq. (90) allows
us to compute the derivative of any quantum gate as
long as the frequencies of UF =0 (x) are known. We
thus obtain an improved rule for UF 6=0 (x) over the
original stochastic shift rule whenever the generalized
shift rule is beneficial for U (x) = UF =0 (x), compared
to the decomposition-based approach.

4 Second-order derivatives

Next, we will apply the stochastic parameter-shift rule
to our general shift rule. For this section we do not

As noted in Sec. 3.3, higher-order derivatives of univariate functions are easily computed using the even
or odd part of the function. In the following sections, we will extend our discussion to multivariate
functions E(x), where derivatives may be taken with
respect to different variables. Each single parameter
dependence is assumed to be of the form Eq. (5), with
equidistant (and by rescaling integer-valued) frequen(k)
cies {Ω` }`∈[Rk ] = [Rk ] for the kth parameter. We

7 Of course, one can construct less efficient decompositions
that do not satisfy this rule of thumb.

8 If GF = F G, the exponential may be split into exp(ixG)
and exp(iF ) and we are back at the situation exp(ixG).

3.6 General stochastic parameter-shift rule

Accepted in Quantum 2022-03-18, click title to verify. Published under CC-BY 4.0.

7

may collect the numbers of frequencies in a vector
(R)k = Rk . It will again be useful in the following to
make the reference point x0 , at which these derivatives are computed, explicit.

4.1 Diagonal shift rule for the Hessian
Here we show how to compute the Hessian H of a
multivariate function E(x) at some reference point x0
using the Fourier series representation of E. We allow for single-parameter gates U (x) = exp(ixG) with
equidistant frequencies and will use fewer evaluations
of E than known schemes. An indication that this
may be possible for gates with two eigenvalues was
made in [54, Eq. (37)].
First, for the kth diagonal entry Hkk = ∂k2 E(x0 ) of
the Hessian, we previously noted in Sec. 3.3 that 2Rk
evaluations are sufficient as it is the second derivative
of a univariate restriction of E. Recall that one of
the 2Rk evaluations is E(x0 ); we can reuse this evaluation
Pnfor all diagonal entries of H, and thus require
1 + k=1 (2Rk − 1) = 2kRk1 − n + 1 evaluations for
the full diagonal. Further, if we compute the Hessian
diagonal (∇ 2 E)k := ∂k2 E in addition to the gradient,
we may reuse the 2kRk1 evaluations computed for the
gradient, only requiring a single additional function
value, namely E(x0 ). In this case, we do not make
use of the periodicity E(x0 + πv k ) = E(x0 − πv k ),
where v k is the kth canonical basis vector, because
this shift is not used in the gradient evaluation (see
Sec. 3.2).
Next, for an off-diagonal entry Hkm = ∂k ∂m E(x0 ),
consider the univariate trigonometric function that
shifts the two parameters xk and xm simultaneously:
E (km) (x) := E(x0 + xv k,m ),

(34)

where we abbreviated v k,m := v k + v m . We show
in App. A.2 that E (km) again is a Fourier series of x
with Rkm = Rk + Rm equidistant frequencies. This
00
means that we can compute E (km) (0) via Eq. (25)
with R = Rkm , using 2Rkm − 1 evaluations of E (as
we may reuse E(x0 ) from the diagonal computation).
Note that
d2 (km)
E
(x)
= Hkk + Hmm + 2Hkm ,
dx2
x=0

(35)

and that we have already computed the diagonal entries. We thus may obtain Hkm via the diagonal
parameter-shift rule

1  (km) 00
Hkm =
E
(0) − Hkk − Hmm .
(36)
2
In Fig. 2, we visually compare the computation of
Hkm via the diagonal shift rule to the chained application of univariate parameter-shift rules for xk and
xm .
As an example, consider the case when Rk = Rm =
1 (e.g., where all parametrized gates are of the form

Figure 2: Visual representation of two approaches to compute
a Hessian entry Hkm at the position x0 (red cross). The
parameters xk and xm lie on the coordinate axes and the
heatmap displays the cost function E(x). We may either
combine the general shift rule for xk and xm (grey triangles)
00
or compute the univariate derivative E (km) (0) and extract
Hkm via Eq. (36) (green circles).

exp(ixk Gk /2) with G2k = 1). By setting R = 2 in
00
Eq. (25), we obtain the explicit formula for E (km) (0),
00
3
1
E (km) (0) = − E(x0 ) − E(x0 + πv k,m )
(37)
2
2 



π
π
+ E x0 + v k,m + E x0 − v k,m
2
2

which can be combined with Eq. (36) to give an explicit formula for the Hessian. This formula (for Rk =
Rm = 1) was already discovered in [54, Eq. (37)].
The computation of Hkm along the main diagonal
in the xk -xm -plane can be modified by making use of
the second diagonal as well: define v k,m := v k − v m
and E

(km)

(x) := E(x0 + xv k,m ), and compute

d2 (km)
E
(x)
= Hkk + Hmm − 2Hkm ,
(38)
dx2
x=0


00
1
(km) 00
Hkm =
E (km) (0) − E
(0) .
4
This means we can replace the dependence on the diagonal elements Hkk and Hmm by another univariate
second-order derivative on the second diagonal. We
will not analyze the resources required by this method
in detail but note that for many applications it forms
a compromise between the two approaches shown in
Fig. 2.
We note that an idea similar to the ones presented
here can be used for higher-order derivatives, but possibly requires more than one additional univariate reconstruction per derivative.

Accepted in Quantum 2022-03-18, click title to verify. Published under CC-BY 4.0.

8

4.2 Resource comparison
For the Hessian computation, we will again look at
the number of unique circuit evaluations Neval and
the number of shots N , as introduced in Sec. 2.3.
4.2.1

Number of unique circuits

In Tab. 1, we summarize the number of distinct circuit
evaluations required to compute several combinations
of derivatives of E(x), either by decomposing the gate
or by using the general parameter-shift rule together
with the diagonal shift rule for the Hessian. We also
include the generalized case of non-equidistant frequencies covered in App. B.2 for completeness. To
obtain the cost for the repeated general shift rule,
i.e., without the diagonal shift rule for the Hessian
or decomposition, simply replace P by R in the left
column.
For equidistant frequencies, the diagonal shift rule
for Hkm requires 2(Rk + Rm ) − 1 evaluations, assuming the diagonal and thus E(x0 ) to be known
already. Like the gradient, Hkm may instead be computed by decomposing Uk (xk ) and Um (xm ) into Pk
and Pm elementary gates, respectively, and repeating the parameter-shift rule twice [46, 56]. All combinations of parameter shifts are required, leading
to 4Pk Pm evaluations. Finally, as a third option,
one may repeat the general parameter-shift rule in
Eq. (24) twice, leading to 4Rk Rm evaluations9 .
The repeated general shift rule requires strictly
more circuit evaluations than the diagonal shift rule,
since
1
2kRk21 − kRk1 + 1 > 2nkRk1 − (n2 + n − 2).
2
(39)
Similar to the discussion for the scaling of gradient
computations, the optimal approach depends on Rk,m
and Pk,m , but P and R often have a linear relation
so that the diagonal shift rule will be significantly
cheaper for many cost functions than decomposing
the unitaries.
4.2.2

App. A.5 for the three presented approaches, and we
conclude the number of shots required to achieve a
norm of ε to be
i2

σ2 h √
2
2
n
+
1
+
n
−
2
kRk
+
kRk
2
1
2ε2
(40)
i
2 h √
2

σ
2 − 1 kRk22 + kRk21
(41)
NgenPS = 2
2ε
i2

σ2 h √
Ndecomp = 2
2 − 1 kPk22 + kPk21
(42)
2ε
Ndiag =

In general, the diagonal shift rule for the Hessian is
significantly less efficient than the repeated execution
of the general parameter-shift rule if the shot count is
the relevant resource measure. This is in sharp contrast to the number of unique circuits, which is strictly
smaller for the diagonal shift rule. We note that the
two resource measures yield incompatible recommendations for the computation of the Hessian. The overhead of the diagonal shift rule reduces to a (to leading
order in n) constant prefactor if Rk = R for all k ∈ [n]:
in this case, we know kRk1 = n = kRk22 and therefore
√
2n + n + 1 − 2
Ndiag
√
=
−→ 2.
(43)
n→∞
NgenPS
n+ 2−1

4.3 Metric tensor
The Fubini-Study metric tensor F is the natural metric on the manifold of (parametrized) quantum states,
and the key ingredient in quantum natural gradient
descent [48]. The component of the metric belonging
to the parameters xk and xm can be written as
Fkm (x0 ) =Re{h∂k ψ(x)|∂m ψ(x)i}

(44)
x=x0

− h∂k ψ(x)|ψ(x)i hψ(x)|∂m ψ(x)i

,
x=x0

or, alternatively, as a Hessian [46]:
1
Fkm (x0 ) = − ∂k ∂m |hψ(x)|ψ(x0 )i|2
2
x=x0
=: ∂k ∂m f (x0 ).
(45)

Number of shots

Next we compare the numbers of measurements required to reach a precision ε. While the approach
via repeated shift rules uses distinct circuit evaluations for each Hessian entry, the diagonal shift rule in
Eq. (36) reuses entries of the Hessian and thus correlates the optimal shot allocations and the statistical
errors of the Hessian entries. We therefore consider
an error measure on the full Hessian matrix instead
of a single entry, namely the root mean square of the
Frobenius norm of the difference between the true and
the estimated Hessian. This norm is computed in
9 These 4R R
k m shifted evaluations are not simultaneous
shifts in both directions of the form Eq. (34).

It follows that we can compute the metric using the
same method as for the Hessian, with f (x) as the cost
function. We know the value of f without shift as
1
1
f (x0 ) = − |hψ(x0 )|ψ(x0 )i|2 = − .
2
2

(46)

The values with shifted argument can be calculated as
the probability of the zero bitstring 0 when measuring
the state V † (x)V (x0 ) |0i in the computational basis,
which requires circuits with up to doubled depth compared to the original circuit V (x). Alternatively, we
may use a Hadamard test to implement f , requiring an auxiliary qubit, two operations controlled by
that qubit as well as a measurement on it, but only

Accepted in Quantum 2022-03-18, click title to verify. Published under CC-BY 4.0.

9

Quantity
E(x0 )
∂k E(x0 )
∇E(x0 )
∂k2 E(x0 )
∇ 2 E(x0 )
∂k ∂m E(x0 )

Decomposition
1
2Pk
2kPk1
2Pk2 − Pk + 1
2kPk22 − kPk1 + 1
4Pk Pm

Gen. shift rule, equidistant
1
2Rk
2kRk1
2Rk
2kRk1 − n + 1
2(Rk + Rm ) − 1(∗)

∇⊗2 E(x0 )

2kPk21 − kPk1 + 1

2nkRk1 − 21 (n2 + n − 2)

∂k E(x0 ) & ∂k2 E(x0 )
∇E(x0 ) & ∇ 2 E(x0 )

2Pk2 + 1
2kPk22 + 1

2Rk + 1
2kRk1 + 1

∇E(x0 ) & ∇⊗2 E(x0 )

2kPk21 + 1

2nkRk1 − 21 (n2 − n − 2)

Gen. shift rule
1
2Rk
2kRk1
2Rk + 1
2kRk1 + 1
4Rk Rm + 2Rk + 2Rm − 4(∗)

2 kRk21 − kRk22 + nkRk1
−2n(n − 1) + 1
2Rk + 1
2kRk1 + 1

2 kRk21 − kRk22 + nkRk1
−2n(n − 1) + 1

Table 1: Number of distinct circuit evaluations Neval for measuring combinations of derivatives of a parametrized expectation
value function E at parameter position x0 . The compared approaches include decomposition of the unitaries together with the
original parameter-shift rule (left), and the generalized parameter-shift rule Eq. (24) together with the diagonal shift rule for
the Hessian in Eq. (36). The requirements for the latter differ significantly for equidistant (center ) and arbitrary frequencies
(right, see App. B.2). A third approach is to repeat the general parameter-shift rule, the cost of which can be read off by
replacing P by R in the left column. Here, n is the number of parameters in the circuit, Pk is the number of elementary
gates with two eigenvalues in the decomposition of the kth parametrized unitary, and Rk denotes the number of frequencies
2
for the kth parameter. The asterisk (∗) indicates that the derivatives ∂k2 E and ∂m
E need to be known in order to obtain the
mixed derivative at the shown price (see main text). The evaluation numbers take savings into account that are based on
using evaluated energies for multiple derivative quantities; hence, they are not additive in general.

halved depth on average (see App. A.3). With either of these methods, the terms for the shift rule in
Eq. (36) and thus the metric tensor can be computed
via the parameter-shift rule.
The metric can also be computed analytically without parameter shifts via a linear combination of unitaries (LCU) [57, 58], which also employs Hadamard
tests. As it uses the generator as an operation in the
circuit, any non-unitary generator needs to be decomposed into Pauli words for this method to be available
on quantum hardware, similar to a gate decomposition. Afterwards, this method uses one circuit evaluation per pair of Pauli words from the kth and mth
generator to compute the entry Fkm . A modification
of all approaches that use a Hadamard test is possible
by replacing it with projective measurements [56].
Metric entries that belong to operations that commute within the circuit 10 can be computed block-wise
without any auxiliary qubits, additional operations or
deeper circuits [48]. For a given block, we execute the
subcircuit V1 prior to the group of mutually commuting gates and measure the covariance matrix of the
generators {Gk } of these gates:

and {Gk } of the block, the covariance matrix can typically be measured with only a few unique circuit evaluations11 , making this method the best choice for the
block-diagonal. One may then either use the result
as an approximation to the full metric tensor, or use
one of the other methods to compute the off-blockdiagonal entries; the approximation has been shown
to work well for some circuit structures [48], but not
for others [59]. The methods to obtain the metric
tensor and their resource requirements are shown in
Tab. 2.
Since we run a different circuit for the metric tensor
than for the cost function itself, the 2Rk − 1 evaluations at shifted positions needed for the kth diagonal
entry cannot reuse any prior circuit evaluations, as is
the case for the cost function Hessian. Consequentially, the natural gradient of a (single term) expectation value function E,
∇n E(x) := F −1 (x)∇E(x),

(48)

By grouping the measurement bases of all {Gk Gm }

with ∇E referring to the Euclidean gradient, requires
more circuit evaluations than its Hessian and gradient
together.
However, the utility of the metric tensor becomes
apparent upon observing that it depends solely on the
ansatz, and not the observable being measured. This

10 For example, operations on distinct wires commute in general but not necessarily within the circuit if entangling operations are carried out between them.

11 For a layer of simultaneous single-qubit rotations on all
N qubits, even a single measurement basis is sufficient for the
corresponding N × N block.

Fkm = h0| V1† Gk Gm V1 |0i

(47)

− h0| V1† Gk V1 |0i h0| V1† Gm V1 |0i .

Accepted in Quantum 2022-03-18, click title to verify. Published under CC-BY 4.0.

10

Parameter shift rule
Overlap
Hadamard
0
1
X
X
∼ 43 DV
∼ 32 DV
2DV
∼ DV

Aux. qubits
off-block-diag.
Depth (avg)
Depth (max)
Neval (Fkk )
Neval (Fkm )
Neval (F)

(
2Rk − 1
2R
( k
2(Rk + Rm ) − 1
2(2Rk Rm + Rk + Rm − 2)
(
2nkRk1 − 21 (n2 + n)

2 kRk21 − kRk22 + n(kRk1 − n + 1)

1
2

LCU

Covariance

1
X
∼ 23 DV
∼ DV

0
2
3 DV

DV

Qk ≤ 12 (Pk2 − Pk )

P k ≤ Pk

Pk Pm

P km ≤ Pk Pm


kPk21 − kPk22 + kQk1

—

Table 2: Quantum hardware-ready methods to compute the Fubini-Study metric tensor and their resource requirements. The
cost function f (x) (see Eq. (45)) for the parameter-shift rule can be implemented with increased depth by applying the adjoint
of the original circuit to directly realize the overlap (left) or with an auxiliary qubit and Hadamard tests (center left, App. A.3).
The LCU method (center right) is based on Hadamard tests as well and both these methods can spare the auxiliary qubit
and instead employ projective measurements [56]. The cheapest method is via measurements of the covariance of generators
(right) but it can only be used for the block-diagonal of the tensor, i.e., not for all Fkm . We denote the depth of the original
circuit V by DV and the number of Pauli words in the decomposition of Gk and its square with Pk and Qk , respectively.
The Pk Pauli words of Gk can be grouped into P k groups of pairwise commuting words; the number of groups of pairwise
commuting Pauli words in the product Gk Gm similarly is P km . For the covariance-based approach, we overestimate the
number of required circuits, as typically many of the measurement bases of the entries in the same block will be compatible.
The number of unique circuits to be evaluated for a diagonal element Fkk , an off-diagonal element Fkm , and the full tensor
F is given in terms of the number of frequencies Rk and of Qk , Pk P k and P km . The entries for Neval in the first and second
row of the braces refer to equidistant (main text) and arbitrary frequencies (see App. B.2), respectively.

means that if a cost function has multiple terms, like
in VQEs, the metric only needs to be computed once
per epoch, rather than once per term, as is the case
of the cost function Hessian. Therefore, an epoch of
quantum natural gradient descent can be cheaper for
such cost functions than an epoch of optimizers using the Hessian of the cost function. In addition, the
block-diagonal of the metric tensor can be obtained
with few circuit evaluations per block for conventional
gates without any further requirements and with reduced average circuit depth.

5 Applications
In this section, we will present QAOA as concrete application for our general parameter-shift rule, which
reduces the required resources significantly when computing derivatives. Afterwards, we use the approach
of trigonometric interpolation to generalize the Rotosolve algorithm. This makes it applicable to arbitrary
quantum gates with equidistant frequencies, which reproduces the results in Refs. [42, 45], and extends
them further to more general frequency spectra. In
addition, we make quantum analytic descent (QAD)
available for arbitrary quantum gates with equidistant frequencies, which previously required a higherdimensional Fourier reconstruction and thus was infeasible.

5.1 QAOA and Hamiltonian time evolution
In Eq. (24) we presented a generalized parameter-shift
rule that makes use of 2R function evaluations for R
frequencies in E. A particular example for singleparameter unitaries with many frequencies are layers
of single- or two-qubit rotation gates, as can be found
e.g., in QAOA circuits or digitized Hamiltonian time
evolution algorithms.
The quantum approximate optimization algorithm
(QAOA) was first proposed in 2014 by Farhi, Goldstone and Gutmann to solve classical combinatorial
optimization problems on near-term quantum devices
[8]. Since then, it has been investigated analytically
[60, 61, 62], numerically [63, 64], and on quantum
computers [65, 66].
In general, given a problem Hamiltonian HP that
encodes the solution to the problem of interest onto
N qubits, QAOA applies two types of layers alternat⊗N
ingly to an initial state |+i :
VQAOA (x) =

1
Y

UM (x2j )UP (x2j−1 ),

(49)

j=p

where p is the number of blocks which determines
the depth of the circuit, UM (x) = exp (−ixHM ) with
PN
HM =
k=1 Xk is the so-called mixing layer, and
UP (x) = exp(−ixHP ) is the time evolution under HP .
The parameters x can then be optimized to try to

Accepted in Quantum 2022-03-18, click title to verify. Published under CC-BY 4.0.

11

minimize the objective function
⊗N

E(x) = h+|

†
VQAOA
(x)HP VQAOA (x) |+i

⊗N

. (50)

Here we focus on the layer UP , and we look at the
example of MaxCut in particular. The corresponding problem Hamiltonian for an unweighted graph
G = (V, E) with N vertices V and M edges E reads
HP =

X 1
(1 − Za Zb ),
2

(51)

(a,b)∈E

and UP correspondingly contains M two-qubit PauliZ rotations RZZ .
We note that HM has eigenvalues −N, −N +
2, · · · , N , which means the corresponding frequencies (differences of eigenvalues) are 2, · · · , 2N . Thus,
treating UM (x2j ) as a single operation, Eq. (6) implies
that E(x) can be considered an N -order trigonometric polynomial in x2j , and the parameter-shift rules
we derive in Sec. 3 will apply with R = N . Similarly,
HP has corresponding frequencies in the set [M ], and
it will obey the parameter-shift rule for R = M , although we may be able to give better upper bounds
λ for R. Thus the unique positive differences {Ω` }
for those layers, i.e., the frequencies of E(x) with respect to the parameter {x2j−1 }j∈[p] , take integer values within the interval [0, λ] as well. We may therefore
use Eq. (24), with the knowledge that R ≤ λ ≤ M .
Note that knowing all frequencies of E(x) requires
knowledge of the full spectrum of HP — and in particular of λ — which in turn is the solution of MaxCut
itself. As a consequence, the motivation for performing QAOA becomes obsolete. Therefore, in general
we cannot assume to know {Ω` } (or even R), but instead require upper bounds ϕ(G) ≥ MaxCut(G) = λ
which can be used to bound the largest frequency, and
thus the number of frequencies R and subsequently
the number of terms in the parameter-shift rule. It
is noteworthy that even if the largest frequency λ is
known exactly via a tight bound — which restricts
the Fourier spectrum to the integers [λ] — not all integers smaller than λ need to be present in the set of
frequencies {Ω` }, so that the estimate for R may be
too large12 .
One way to obtain an upper bound uses analytic
results based on the Laplacian of the graph of interest [67, 68], for which automatic bound generating programs exist [69]. An alternative approach uses
semi-definite programs (SDPs) that solve relaxations
of the MaxCut problem, the most prominent being
the Goemans-Williamson (GW) algorithm [70] and
recent extensions thereof that provide tighter upper
bounds [71, 72]. The largest eigenvalue is guaranteed
to be within ∼ 0.878 of these SDP upper bounds.
12 A simple example for this is the case of 2k-regular graphs;
here, HP only has even eigenvalues, and therefore all frequencies are even as well. Given an upper bound ϕ, we thus know
the number of frequencies to satisfy R ≤ ϕ/2.

To demonstrate the above strategy, we summarize
the number of evaluations required for the gradient
and Hessian of an n-parameter QAOA circuit on N
qubits for MaxCut in Tab. 3, comparing the approach via decomposing the circuit, to the one detailed above based on ϕ and the improved Hessian
measurement scheme in Sec. 4.1. Here, we take into
account that half of the layers are of the form UP ,
and the other half are mixing layers with R = N frequencies. We systematically observe the number of
evaluations for the gradient to be cut in half, and the
those for the gradient and Hessian together to scale
with halved order in N (and k, for regular graphs).
In addition, we display the numbers of circuit evaluations from Tab. 3 together with SDP-based bounds
for λ and the true minimal number of evaluations required for the parameter-shift rule in Fig. 3. For this,
we sampled random unweighted graphs of the corresponding type and size and ran the GW algorithm
as well as an improvement thereof to obtain tighter
bounds [71]. On one hand we observe the advantage of the generalized parameter-shift rule and the
cheaper Hessian method that can be read off already
from the scalings in Tab. 3. On the other hand, we
find both SDP-based upper bounds to provide an exact estimate of the largest eigenvalue in the N ≤ 20
regime, as can be seen from the cut values obtained
from the GW algorithm that coincide with the upper bound. In cases in which the frequencies {Ω` }
occupy all integers in [R], this leads to an exact estimate of R and the evaluations in the shift rule. For
all graph types but complete graphs, the SDP-based
upper bounds yield a better estimate for the number
of terms than the respective analytic bound ϕ, which
improves the generalized shift rule further.
In summary, we find the generalized parametershift rule to offer a constant prefactor improvement
when computing the gradient and an improvement
of at least O(N ) when computing both the gradient
and the Hessian. For certain graph types, knowledge
about the structure of the spectrum and tight analytic bounds provide this advantage already, whereas
for other graph types the SDP-based bounds reduce
the evaluation numbers significantly.

5.2 Rotosolve
The Rotosolve algorithm is a coordinate descent algorithm for minimizing quantum cost functions. It
has been independently discovered multiple times
[42, 45, 51, 50], with [50] giving the algorithm its name
but only (along with [51]) considering parametrized
Pauli rotations, and [42, 45] covering other unitaries
with integer-valued generator eigenvalues.
The Rotosolve algorithm optimizes the rotation angles sequentially: for one variational parameter xk at
a time, the cost function is reconstructed as a function
of that parameter using 2Rk +1 evaluations, the mini-

Accepted in Quantum 2022-03-18, click title to verify. Published under CC-BY 4.0.

12

General

Decomposition-based
∇E
∇E&∇⊗2 E
(M + N )n
O(n2 (M + N )2 )

Complete

1
2
2 n(N + N )

O(n2 N 4 )

2k-regular
(2k+1)-regular

(k + 1)nN
2k+3
2 nN

O(k 2 n2 N 2 )
O(k 2 n2 N 2 )

Graph type

Bound ϕ
jϕk
N2
4

kN
2k+1
2 N

n

Gen. shift rule
∇E
∇E&∇⊗2 E
2
n(ϕ +
j
k N )  O(n (ϕ + N ))
N2
+N
4
k+2
2 nN
2k+3
2 nN

O(n2 N 2 )

O(kn2 N )
O(kn2 N )

Table 3: Evaluation numbers for the gradient, or both the gradient and the Hessian, for QAOA circuits for MaxCut on
several types of graphs. Each graph has N vertices and a graph type-specific number M of edges, and the (even) number
of parameters is denoted as n. For K-regular graphs, we know M = min{(N 2 − N )/2, KN/2}, and the latter value is used
in the displayed evaluation costs; if the former value forms the minimum, the graph is in fact complete. The left column is
based on decomposing the circuit, applying the conventional two-term parameter-shift rule per elementary gate and iterating
it for the Hessian. The right column employs the generalized parameter-shift rule Eq. (24) combined with an upper bound ϕ
for the largest eigenvalue λ of the problem Hamiltonian, as well as the reduced number of evaluations for Hessian off-diagonal
terms from Sec. 4.1. The bound ϕ for complete graphs can be found in Ref. [67].

mum of the reconstruction is calculated, and then the
parameter is updated to the minimizing angle. For
the case of Pauli rotation gates this minimum can be
found via a closed-form expression. Recent studies
have shown such coordinate descent methods to work
well on many tasks [73, 50, 45, 74], although there are
limited cases where these methods fail [75].
While Rotosolve is not gradient-based, our cost reduction for the gradient presented in Sec. 5.1 stems
from a cost reduction for function reconstruction, and
hence is applicable to Rotosolve as well.
As shown in Sec. 3.1, the univariate objective
function can also be fully reconstructed if the
parametrized unitaries are more complicated than
Pauli rotations, using the function value itself and
the evaluations from the generalized parameter-shift
rule. Since the generalized parameter-shift rule also
applies for non-equidistant frequencies (see App. B),
the reconstruction works in the same way for arbitrary single-parameter gates. This extends our generalization of Rotosolve beyond the previously known
integer-frequency case [42, 45], although the number of frequencies—and thus the cost—for the reconstruction are typically significantly increased for noninteger frequencies. While the minimizing angle might
not be straightforward to express in a closed form as it
is the case for a single frequency, the one-dimensional
minimization can efficiently be carried out numerically to high precision, via grid search or semi-definite
programming [76, Chapter 4.2].

5.3 Quantum analytic descent
Quantum analytic descent (QAD) [49] also approaches the optimization problem in VQAs via
trigonometric interpolation. In contrast to Rotosolve, it considers a model of all parameters simultaneously and includes second-order derivatives, but
this model only is a local approximation of the full
cost function. Additionally, QAD has been developed
for circuits that exclusively contain Pauli rotations as

parametrized gates.
The algorithm evaluates the cost function E at
2n2 + n + 1 points around a reference point x0 , and
then constructs a trigonometric model of the form13
h
x
Ê(x0 + x) = A(x) E (A) + 2E (B) · tan
2
x 2
+ 2E (C) · tan
(52)
2
x
 x i
+4 tan
· E (D) · tan
,
2
2

Q
Here, we introduced A(x) := k cos2 x2k and the
element-wise square of a vector v, (v 2 )k := vk2 as for
the Hessian diagonal. The coefficients E (A/B/C/D)
are derived from the circuit evaluations, taking the
form of a scalar, two vectors and an upper triangular
matrix. More precisely, the expansion basis is chosen
such that E (B) = ∇E(x0 ), E (C) = ∇ 2 E(x0 ), and
E (D) is the strictly upper triangular part of the Hessian. Note that for this model 2n2 + n + 1 evaluations
are used to obtain n2 /2 + 3n/2 + 1 parameters. In the
presence of statistical noise from these evaluations, it
turns out that building the model to a desired precision and inferring modelled gradients close to the
reference point x0 has resource requirements similar
to measuring the gradient directly [49].
This model coincides with E(x) at x0 up to second
order, and in the vicinity its error scales with the third
order of the largest parameter deviation [49]. After
the construction phase, the model cost is minimized in
an inner optimization loop, which only requires classical operations. For an implementation and demonstration of the optimization, we also refer the reader
to [77] and [78].
In the light of the parameter-shift rules and reconstruction methods, we propose three (alternative)
modifications of QAD. The first change is to reduce
the required number of evaluations. As the coeffi13 We slightly modify the trigonometric basis functions from
Ref. [49] to have leading order coefficients 1.

Accepted in Quantum 2022-03-18, click title to verify. Published under CC-BY 4.0.

13

Known spectrum
Upper bound
SDP upper bound

Evaluations

∇E&∇⊗2 E

∇E

105

102

103

4 × 102
3 × 102
2 × 102

104

102

103
105

4 × 102
3 × 102

104

2 × 102
102

103
105

Evaluations

Evaluations

Evaluations

103

Decomposition
GW upper bound
GW lower bound

102

103

10

20

Number of vertices N

10

20

Number of vertices N

Figure 3: Evaluation numbers Neval for the gradient (left)
or both the gradient and the Hessian (right) for n = 6 parameter QAOA circuits for MaxCut on graphs of several
types and sizes. Using numerical upper bounds together with
our new parameter-shift rule (GW – purple triangles and its
generalization – dashed turquoise) reduces the resource requirements for both quantities significantly, compared to the
previously available decomposition-based method (solid orange). The rows correspond to the various considered graph
types (top to bottom): complete, 5-regular, 6-regular and
(up to) 4N randomly sampled edges. The requirements for
the decomposition-based approach and the analytic upper
bound (dotted blue) correspond to the results in the left and
right column of Tab. 3, respectively. The numerical upper
bounds both use the minimized objective value of SDPs for
relaxations of MaxCut to obtain the bound ϕ, which depends on the graph instance. The GW-based lower bound
(pink triangles) is obtained by randomly mapping the output
state of the GW algorithm to 10 valid cuts and choosing the
one with the largest cut value. Note that K-regular graphs
are only defined for N > K and N K mod 2 = 0 and that
graphs with κN sampled edges are complete for N ≤ 2κ + 1,
leading to a change in the qualitative behaviour in the last
row at N = 2κ + 2 = 10.

cients E (A/B/C/D) consist of the gradient and Hessian, they allow us to exploit the reduced resource
requirements presented in Tab. 1 14 . In the case originally considered by the authors, i.e., for Pauli rotations only, this reduces the number of evaluations
from 2n2 + n + 1 to (3n2 + n)/2 + 1.
A second, alternative modification of QAD is to
keep all evaluations as originally proposed to obtain
the full second-order terms, i.e., we may combine the
shift angles for each pair of parameters, and use them
for coefficients of additional higher-order terms. This
extended model (see App. D.1) has the form
x 2
(53)
E̊(x0 + x) = Ê(x0 + x) + 4A(x) tan
2

x
 x  2
+ E (G) · tan
,
· E (F ) · tan
2
2
where E (F ) is symmetric with zeros on its diagonal
and E (G) is a strictly upper triangular matrix. This
extended model has 2n2 +1 degrees of freedom, which
matches the number of evaluations exactly.
While the QAD model reconstructs the univariate
restrictions of E to the coordinate axes correctly, the
extended model E̊ does so for the bivariate restrictions to the plane spanned by any pair of coordinate
axes. It remains to investigate whether and for which
applications the extension yields a better optimization
behaviour; for functions in which pairs of parameters
yield a good local approximation of the landscape, it
might provide an improvement.
The third modification we consider is to generalize
the previous, extended QAD model to general singleparameter quantum gates. This can be done via a full
trigonometric interpolation to second order, which is
detailed in App. D.2, exactly reconstructing the energy function when restricted to any coordinate plane
at the price of 2(kRk21 −kRk22 +kRk1 )+1 evaluations.
Using toy model circuits and Hamiltonians, we
demonstrate the qualitative difference between the
QAD model, its extension E̊, and the generalization
to multiple frequencies in Fig. 4.

6 Discussion
In this work, we derive interpolation rules to exactly
express quantum functions E(x) as a linear combination of evaluations E(xµ ), assuming E(x) derives from
parametrized gates of the form U (x) = exp(ixG). Our
method relies on the observation that E(x) can be
expressed as trigonometric polynomial in x, characterized by a set of R frequencies that correspond to
distinct differences in the eigenvalues of G. This observation allows us to derive our results using trigonometric interpolation methods.
14 In addition, we may skip the n evaluations with shift angle π proposed in Ref. [49], and instead measure the Hessian
diagonal as discussed in Sec. 4.1.

Accepted in Quantum 2022-03-18, click title to verify. Published under CC-BY 4.0.

14

=

=

=

Figure 4: The QAD model (left), its extension E̊, see Eq. (53), that includes full second-order terms (center left), and the
second-order trigonometric interpolation model (center right), as well as the original expectation value E (right). The original
function is generated from toy Hamiltonians in a two-parameter example circuit, with one frequency (top) and two frequencies
(bottom) per parameter. The QAD model produces a local approximation to E that deviates away from x0 at a slow rate for
R = 1 but faster for R = 2. The extension E̊ reuses evaluations made for the Hessian to capture the full bivariate dependence
for a single frequency but is not apt to model multiple frequencies either. Finally, the trigonometric interpolation generalizes
E̊. This means it coincides with E̊ for R = 1, but also reproduces the full bivariate function for R > 1.

In addition to a full reconstruction of E(x), the
presented approach offers parameter-shift rules for
derivatives of arbitrary order and recipes to evaluate multivariate derivatives more cheaply. Using the
concept of the stochastic parameter-shift rule, quantum gates of the form UF (x) = exp(i(xG + F )) can
be differentiated as well.
Nevertheless, much remains unknown about the
practicality of our new parameter-shift rules. For the
common case that we have R equidistant frequencies,
Sec. 3.5 shows that the scaling of the required resources is similar between naı̈vely applying our generalized parameter-shift rules, and applying parametershift rules to a decomposition of U (x). This holds for
the first derivative and also for the required shot budget when computing the second derivative, whereas
the number of unique circuits is significantly smaller
for the new, generalized shift rule.
Our observations lead to several open questions:
In which situations can we obtain better bounds
on the number of frequencies? We investigated an
example for QAOA in Sec. 5.1, but are there other
examples?
P
• For general G (e.g., G =
j cj Pj with real cj and
Pauli words Pj ), the frequencies will not be equidistant, and in fact R may scale quadratically in the
size of U . Naı̈vely applied, our method would then
scale poorly compared to decomposing G. Can we

apply an approximate or stochastic parameter-shift
rule with a better scaling?

•

Would it ever make sense to truncate these
parameter-shift rules to keep only terms corresponding to smaller frequencies? This is inspired
by the idea of using low-pass filters to smooth out
rapid changes of a signal.

•

Our work on function reconstruction extends QAD
to all gates with equidistant frequencies. Similarly,
it allows Rotosolve, which has been shown to work
remarkably well on some applications, to be used
on all quantum gates with arbitrary frequencies. Is
there a classification of problems on which these
model-based algorithms work well? And can we
reduce the optimization cost based on the above
ideas?

•

More generally, can we apply the machinery of
Fourier analysis more broadly, e.g., to improve optimization methods in the presence of noise?

•

We hope that this work serves as an impetus for future
work that will further apply signal processing methods to the burgeoning field of variational quantum
computing.

Accepted in Quantum 2022-03-18, click title to verify. Published under CC-BY 4.0.

15

Acknowledgements
We would like to thank Nathan Killoran, Maria
Schuld, Matthew Beach, and Eric Kessler for helpful comments on the manuscript, as well as Christian
Gogolin and Gian-Luca Anselmetti for valuable discussions.

Code availability
The scripts used to create the data and plots for
Figs. 3 and 4 can be found at [79].

References
[1] Amazon Web Services.
“Amazon Braket”.
url: aws.amazon.com/braket/.
[2] J.M. Arrazola, V. Bergholm, K. Brádler, T.R.
Bromley, M.J. Collins, I. Dhand, A. Fumagalli,
T. Gerrits, A. Goussev, L.G. Helt, J. Hundal, T. Isacsson, R.B. Israel, J. Izaac, S. Jahangiri, R. Janik, N. Killoran, S.P. Kumar,
J. Lavoie, A.E. Lita, D.H. Mahler, M. Menotti,
B. Morrison, S.W. Nam, L. Neuhaus, H.Y.
Qi, N. Quesada, A. Repingon, K.K. Sabapathy, M. Schuld, D. Su, J. Swinarton, A. Száva,
K. Tan, P. Tan, V.D. Vaidya, Z. Vernon, Z. Zabaneh, and Y. Zhang. “Quantum circuits with
many photons on a programmable nanophotonic
chip”. Nature 591, 54–60 (2021).
[3] IBM Corporation.
“IBM Quantum”.
url: quantum-computing.ibm.com/.
[4] Microsoft.
“Azure
Quantum”.
url: azure.microsoft.com/../quantum/.
[5] Marcello Benedetti, Erika Lloyd, Stefan Sack,
and Mattia Fiorentini. “Parameterized quantum
circuits as machine learning models”. Quantum
Science and Technology 4, 043001 (2019).
[6] Marco Cerezo, Andrew Arrasmith, Ryan Babbush, Simon C. Benjamin, Suguru Endo, Keisuke
Fujii, Jarrod R. McClean, Kosuke Mitarai, Xiao
Yuan, Lukasz Cincio, and Patrick J. Coles. “Variational quantum algorithms”. Nature Reviews
Physics 3, 625–644 (2021).
[7] Alberto Peruzzo, Jarrod McClean, Peter Shadbolt, Man-Hong Yung, Xiao-Qi Zhou, Peter J. Love, Alán Aspuru-Guzik, and Jeremy L.
O’Brien. “A variational eigenvalue solver on a
photonic quantum processor”. Nature Communications 5, 4213 (2014).
[8] Edward Farhi, Jeffrey Goldstone, and Sam Gutmann. “A quantum approximate optimization
algorithm” (2014). arXiv:1411.4028.

[9] Tyson Jones, Suguru Endo, Sam McArdle, Xiao
Yuan, and Simon C. Benjamin. “Variational
quantum algorithms for discovering Hamiltonian
spectra”. Phys. Rev. A 99, 062304 (2019).
[10] Gian-Luca R Anselmetti, David Wierichs, Christian Gogolin, and Robert M Parrish. “Local,
expressive, quantum-number-preserving VQE
ansätze for fermionic systems”. New Journal of
Physics 23, 113010 (2021).
[11] Harper R. Grimsley, Sophia E. Economou, Edwin
Barnes, and Nicholas J. Mayhall. “An adaptive
variational algorithm for exact molecular simulations on a quantum computer”. Nature communications 10, 1–9 (2019).
[12] Ken M. Nakanishi, Kosuke Mitarai, and Keisuke
Fujii. “Subspace-search variational quantum
eigensolver for excited states”. Phys. Rev. Research 1, 033062 (2019).
[13] Alain Delgado, Juan Miguel Arrazola, Soran Jahangiri, Zeyue Niu, Josh Izaac, Chase Roberts,
and Nathan Killoran. “Variational quantum algorithm for molecular geometry optimization”.
Phys. Rev. A 104, 052402 (2021).
[14] Eric Anschuetz, Jonathan Olson, Alán AspuruGuzik, and Yudong Cao. “Variational quantum factoring”. In International Workshop on
Quantum Technology and Optimization Problems. Pages 74–85. Springer (2019).
[15] Sumeet Khatri, Ryan LaRose, Alexander
Poremba, Lukasz Cincio, Andrew T. Sornborger,
and Patrick J. Coles. “Quantum-assisted quantum compiling”. Quantum 3, 140 (2019).
[16] Jun Li, Xiaodong Yang, Xinhua Peng, and
Chang-Pu Sun. “Hybrid quantum-classical approach to quantum optimal control”. Phys. Rev.
Lett. 118, 150503 (2017).
[17] Ryan LaRose, Arkin Tikku, Étude O’Neel-Judy,
Lukasz Cincio, and Patrick J. Coles. “Variational
quantum state diagonalization”. npj Quantum
Information 5, 1–10 (2019).
[18] Benjamin Commeau, Marco Cerezo, Zoë Holmes,
Lukasz Cincio, Patrick J. Coles, and Andrew Sornborger. “Variational Hamiltonian diagonalization for dynamical quantum simulation” (2020). arXiv:2009.02559.
[19] Jonathan Romero, Jonathan P. Olson, and Alan
Aspuru-Guzik. “Quantum autoencoders for efficient compression of quantum data”. Quantum
Science and Technology 2, 045001 (2017).
[20] Guillaume Verdon, Michael Broughton, and Jacob Biamonte. “A quantum algorithm to train
neural networks using low-depth circuits” (2017).
arXiv:1712.05304.

Accepted in Quantum 2022-03-18, click title to verify. Published under CC-BY 4.0.

16

[21] Edward Farhi and Hartmut Neven. “Classification with quantum neural networks on near term
processors” (2018). arXiv:1802.06002.
[22] Maria Schuld and Nathan Killoran. “Quantum machine learning in feature Hilbert spaces”.
Phys. Rev. Lett. 122, 040504 (2019).
[23] Kosuke Mitarai, Makoto Negoro, Masahiro Kitagawa, and Keisuke Fujii. “Quantum circuit learning”. Phys. Rev. A 98, 032309 (2018).
[24] Maria Schuld, Alex Bocharov, Krysta M. Svore,
and Nathan Wiebe. “Circuit-centric quantum
classifiers”. Phys. Rev. A 101, 032308 (2020).
[25] Edward Grant, Marcello Benedetti, Shuxiang
Cao, Andrew Hallam, Joshua Lockhart, Vid Stojevic, Andrew G. Green, and Simone Severini.
“Hierarchical quantum classifiers”. npj Quantum
Information 4, 1–8 (2018).
[26] Jin-Guo Liu and Lei Wang. “Differentiable learning of quantum circuit Born machines”. Phys.
Rev. A 98, 062324 (2018).
[27] Vojtěch Havlı́ček, Antonio D. Córcoles, Kristan
Temme, Aram W. Harrow, Abhinav Kandala,
Jerry M. Chow, and Jay M. Gambetta. “Supervised learning with quantum-enhanced feature
spaces”. Nature 567, 209–212 (2019).
[28] Hongxiang Chen, Leonard Wossnig, Simone Severini, Hartmut Neven, and Masoud Mohseni.
“Universal discriminative quantum neural networks”. Quantum Machine Intelligence 3, 1–
11 (2021).
[29] Nathan Killoran,
Thomas R. Bromley,
Juan Miguel Arrazola, Maria Schuld, Nicolás
Quesada, and Seth Lloyd. “Continuous-variable
quantum neural networks”. Phys. Rev. Research
1, 033063 (2019).
[30] Gregory R. Steinbrecher, Jonathan P. Olson,
Dirk Englund, and Jacques Carolan. “Quantum
optical neural networks”. npj Quantum Information 5, 1–9 (2019).
[31] Andrea Mari, Thomas R. Bromley, Josh Izaac,
Maria Schuld, and Nathan Killoran. “Transfer
learning in hybrid classical-quantum neural networks”. Quantum 4, 340 (2020).
[32] Ryan Sweke, Frederik Wilde, Johannes Meyer,
Maria Schuld, Paul K. Faehrmann, Barthélémy
Meynard-Piganeau, and Jens Eisert. “Stochastic gradient descent for hybrid quantum-classical
optimization”. Quantum 4, 314 (2020).
[33] Martı́n Abadi, Paul Barham, Jianmin Chen,
Zhifeng Chen, Andy Davis, Jeffrey Dean,
Matthieu Devin, Sanjay Ghemawat, Geoffrey Irving, Michael Isard, Manjunath Kudlur,
Josh Levenberg, Rajat Monga, Sherry Moore,
Derek G. Murray, Benoit Steiner, Paul Tucker,

Vijay Vasudevan, Pete Warden, Martin Wicke,
Yuan Yu, and Xiaoqiang Zheng.
“TensorFlow: a system for large-scale machine learning”. In OSDI. Volume 16, pages 265–283.
Berkeley, CA, USA (2016). USENIX Association.
url: dl.acm.org/..3026877.3026899.
[34] Adam Paszke, Sam Gross, Soumith Chintala,
Gregory Chanan, Edward Yang, Zachary DeVito, Zeming Lin, Alban Desmaison, Luca
Antiga, and Adam Lerer.
“Automatic
differentiation in PyTorch”.
NIPS 2017
Workshop Autodiff
(2017).
url: openreview.net/forum?id=BJJsrmfCZ.
[35] Dougal Maclaurin, David Duvenaud, and
Ryan P. Adams. “Autograd: Effortless gradients
in NumPy”. In ICML 2015 AutoML Workshop.
(2015). url: indico.ijclab.in2p3.fr/..
[36] Atılım Güneş Baydin, Barak A. Pearlmutter,
Alexey Andreyevich Radul, and Jeffrey Mark
Siskind.
“Automatic differentiation in machine learning: a survey”. Journal of Machine Learning Research 18, 1–153 (2018).
url: http://jmlr.org/papers/v18/17-468.html.
[37] Ville Bergholm, Josh Izaac, Maria Schuld, Christian Gogolin, M. Sohaib Alam, Shahnawaz
Ahmed, Juan Miguel Arrazola, Carsten Blank,
Alain Delgado, Soran Jahangiri, Keri McKiernan, Johannes Jakob Meyer, Zeyue Niu, Antal
Száva, and Nathan Killoran. “PennyLane: Automatic differentiation of hybrid quantum-classical
computations” (2020). arXiv:1811.04968.
[38] Maria Schuld, Ville Bergholm, Christian
Gogolin, Josh Izaac, and Nathan Killoran.
“Evaluating analytic gradients on quantum
hardware”. Phys. Rev. A 99, 032331 (2019).
[39] Leonardo Banchi and Gavin E. Crooks. “Measuring analytic gradients of general quantum evolution with the stochastic parameter shift rule”.
Quantum 5, 386 (2021).
[40] Gavin E. Crooks. “Gradients of parameterized
quantum gates using the parameter-shift rule and
gate decomposition” (2019). arXiv:1905.13311.
[41] Jakob S. Kottmann, Abhinav Anand, and Alán
Aspuru-Guzik. “A feasible approach for automatically differentiable unitary coupled-cluster
on quantum computers”. Chemical Science 12,
3497–3508 (2021).
[42] Javier Gil Vidal and Dirk Oliver Theis. “Calculus on parameterized quantum circuits” (2018).
arXiv:1812.06323.
[43] Francisco Javier Gil Vidal and Dirk Oliver Theis.
“Input redundancy for parameterized quantum
circuits”. Frontiers in Physics 8, 297 (2020).
[44] Maria Schuld, Ryan Sweke, and Johannes Jakob
Meyer. “Effect of data encoding on the expressive

Accepted in Quantum 2022-03-18, click title to verify. Published under CC-BY 4.0.

17

power of variational quantum-machine-learning
models”. Phys. Rev. A 103, 032430 (2021).
[45] Ken M. Nakanishi, Keisuke Fujii, and Synge
Todo. “Sequential minimal optimization for
quantum-classical hybrid algorithms”. Phys.
Rev. Research 2, 043158 (2020).

[59] David Wierichs, Christian Gogolin, and Michael
Kastoryano. “Avoiding local minima in variational quantum eigensolvers with the natural
gradient optimizer”. Phys. Rev. Research 2,
043246 (2020).

[46] Andrea Mari, Thomas R. Bromley, and Nathan
Killoran. “Estimating the gradient and higherorder derivatives on quantum hardware”. Phys.
Rev. A 103, 012405 (2021).

[60] Mauro E. S. Morales, Jacob D. Biamonte,
and Zoltán Zimborás. “On the universality
of the quantum approximate optimization algorithm”. Quantum Information Processing 19, 1–
26 (2020).

[47] Johannes Jakob Meyer. “Fisher information in
noisy intermediate-scale quantum applications”.
Quantum 5, 539 (2021).

[61] Seth Lloyd.
“Quantum approximate optimization is computationally universal” (2018).
arXiv:1812.11075.

[48] James Stokes, Josh Izaac, Nathan Killoran, and
Giuseppe Carleo. “Quantum natural gradient”.
Quantum 4, 269 (2020).

[62] Matthew B. Hastings. “Classical and quantum bounded depth approximation algorithms” (2019). arXiv:1905.07047.

[49] Bálint Koczor and Simon C. Benjamin. “Quantum analytic descent” (2020). arXiv:2008.13774.

[63] Zhihui Wang, Stuart Hadfield, Zhang Jiang, and
Eleanor G. Rieffel. “Quantum approximate optimization algorithm for MaxCut: A fermionic
view”. Phys. Rev. A 97, 022304 (2018).

[50] Mateusz Ostaszewski, Edward Grant, and Marcello Benedetti. “Structure optimization for parameterized quantum circuits”. Quantum 5,
391 (2021).
[51] Robert M. Parrish, Joseph T. Iosue, Asier Ozaeta, and Peter L. McMahon. “A Jacobi diagonalization and Anderson acceleration algorithm for
variational quantum algorithm parameter optimization” (2019). arXiv:1904.03206.
[52] Artur F. Izmaylov, Robert A. Lang, and TzuChing Yen. “Analytic gradients in variational
quantum algorithms: Algebraic extensions of the
parameter-shift rule to general unitary transformations”. Phys. Rev. A 104, 062443 (2021).
[53] Oleksandr Kyriienko and Vincent E. Elfving. “Generalized quantum circuit differentiation
rules”. Phys. Rev. A 104, 052417 (2021).
[54] Thomas Hubregtsen, Frederik Wilde, Shozab
Qasim, and Jens Eisert. “Single-component
gradient rules for variational quantum algorithms” (2021). arXiv:2106.01388v1.
[55] Antoni Zygmund. “Trigonometric series, Volume
II”. Cambridge University Press (1988).
[56] Kosuke Mitarai and Keisuke Fujii. “Methodology for replacing indirect measurements with
direct measurements”. Phys. Rev. Research 1,
013006 (2019).
[57] Sam McArdle, Tyson Jones, Suguru Endo, Ying
Li, Simon C. Benjamin, and Xiao Yuan. “Variational ansatz-based quantum simulation of imaginary time evolution”. npj Quantum Information
5 (2019).
[58] Ying Li and Simon C. Benjamin. “Efficient
variational quantum simulator incorporating active error minimization”. Phys. Rev. X 7,
021050 (2017).

[64] Wen Wei Ho and Timothy H. Hsieh. “Efficient variational simulation of non-trivial quantum states”. SciPost Phys 6, 29 (2019).
[65] Leo Zhou, Sheng-Tao Wang, Soonwon Choi,
Hannes Pichler, and Mikhail D. Lukin. “Quantum approximate optimization algorithm: Performance, mechanism, and implementation on
near-term devices”.
Phys. Rev. X 10,
021067 (2020).
[66] Matthew P. Harrigan, Kevin J. Sung, Matthew
Neeley, Kevin J. Satzinger, Frank Arute, Kunal Arya, Juan Atalaya, Joseph C. Bardin, Rami
Barends, Sergio Boixo, et al. “Quantum approximate optimization of non-planar graph problems
on a planar superconducting processor”. Nature
Physics 17, 332–336 (2021).
[67] Charles Delorme and Svatopluk Poljak. “The
performance of an eigenvalue bound on the MaxCut problem in some classes of graphs”. Discrete
Mathematics 111, 145–156 (1993).
[68] William N. Anderson Jr. and Thomas D. Morley.
“Eigenvalues of the Laplacian of a graph”. Linear
and Multilinear Algebra 18, 141–145 (1985).
[69] Vladimir Brankov, Pierre Hansen, and Dragan
Stevanović. “Automated conjectures on upper
bounds for the largest Laplacian eigenvalue of
graphs”. Linear Algebra and its Applications
414, 407–424 (2006).
[70] Michel X. Goemans and David P. Williamson.
“Improved approximation algorithms for Maximum Cut and satisfiability problems using
semidefinite programming”.
J. ACM 42,
1115–1145 (1995).

Accepted in Quantum 2022-03-18, click title to verify. Published under CC-BY 4.0.

18

[71] Miguel F. Anjos and Henry Wolkowicz. “Geometry of semidefinite MaxCut relaxations via matrix ranks”. Journal of Combinatorial Optimization 6, 237–270 (2002).
[72] Liu Hongwei, Sanyang Liu, and Fengmin Xu. “A
tight semidefinite relaxation of the MaxCut problem”. J. Comb. Optim. 7, 237–245 (2003).
[73] Andrea Skolik, Jarrod R. McClean, Masoud
Mohseni, Patrick van der Smagt, and Martin
Leib. “Layerwise learning for quantum neural
networks”. Quantum Machine Intelligence 3, 1–
11 (2021).
[74] Marcello Benedetti, Mattia Fiorentini, and
Michael Lubasch. “Hardware-efficient variational
quantum algorithms for time evolution”. Phys.
Rev. Research 3, 033083 (2021).
[75] Ernesto Campos, Aly Nasrallah, and Jacob Biamonte. “Abrupt transitions in variational quantum circuit training”.
Phys. Rev. A 103,
032607 (2021).
[76] Aharon Ben-Tal and Arkadi Nemirovski. “Lectures on modern convex optimization: Analysis, algorithms, and engineering applications”.
SIAM (2001).
[77] Elies Gil-Fuster and David Wierichs. “Quantum analytic descent (demo)”.
url: pennylane.ai/qml/demos/.. (accessed: 2022-01-23).
[78] Bálint
Koczor
(2021).
code: balintkoczor/quantum-analytic-descent.
[79] David
Wierichs,
Josh
Izaac,
Cody
Wang, and Cedric Yen-Yu Lin (2022).
code: dwierichs/General-Parameter-Shift-Rules.
[80] Leonard Benjamin William Jolley. “Summation
of series”. Dover Publications (1961).
[81] falagar. “Prove that

n−1
P
k=1

(n−1)(2n−1)
”.
tan2 kπ
2n =
3

url: math.stackexchange.com/q/2343.
cessed: 2022-01-23).

(ac-

Consider the Dirichlet kernel
R

X
1
2
+
cos(`x)
2R + 1 2R + 1
`=1

sin 2R+1
2 x

=
(2R + 1) sin 12 x

D(x) =

(54)
(55)

where the limit x → 0 is taken when evaluating D(0).
The functions D(x−xµ ) are linear combinations of the
basis functions {sin(`x)}`∈[R] , {cos(`x)}`∈[R]0 , and
they satisfy D(xµ0 − xµ ) = δµµ0 . Therefore it is evident that
R
X

E(x) =

E(xµ )D(x − xµ )

(56)

µ=−R

 R
X
sin 2R+1
(−1)µ
2 x

 . (57)
E (xµ )
x−xµ
2R + 1
sin

=

µ=−R

2

As an example, for R = 1 (e.g., when the generator
G satisfies G2 = 1) we have the formula

sin 23 x
E(− 32 π)
E(x) =
−
(58)
3
sin( x2 + π3 )

E( 23 π)
E(0)
−
.
+
sin( x2 ) sin( x2 − π3 )
Derivatives of E(x) can be straightforwardly extracted from this full reconstruction.
A.1.2

Odd kernels

We now consider the case of determining Eodd given
its value at evenly spaced points {xµ = 2µ−1
2R π}µ∈[R]
15
. Consider the modified Dirichlet kernel :
R−1

D∗ (x) =

1
1
1 X
cos(`x)
+
cos(Rx) +
2R 2R
R

(59)

sin(Rx)

2R tan 21 x

(60)

`=1

=

where we again assume the limit x → 0 is taken when
evaluating D∗ (0). This kernel satisfies the relations
D∗ (xµ0 − xµ ) = δµµ0 ,

D∗ (xµ0 + xµ ) = 0,

(61)

∗

A Technical derivations
A.1 Derivation of explicit parameter-shift rules
Here we derive the trigonometric interpolation via
Dirichlet kernels.
A.1.1

Full reconstruction

We start out by exactly determining E(x) given its
2µ
value at points {xµ = 2R+1
π}, µ ∈ {−R, · · · , R}.
This is a well-known problem [55, Chapter X]; we reproduce the result below for completeness.

but unfortunately, D (x) is a linear combination of
cosines, not sines; it’s an even function, not an odd
function. We therefore instead consider the linear
combinations
D̃µ (x) := D∗ (x − xµ ) − D∗ (x + xµ )

(62)

sin(R(x − xµ ))
sin(R(x + xµ ))
−

1
2R tan 2 (x − xµ )
2R tan 12 (x + xµ )
"
#
R−1
X
1
1
= cos(xµ )
sin(Rx) +
sin(`x) .
R
2
=

`=1

15 Unlike Sec. A.1.1, we are not aware of a prior reference
for the derivations for this subsection (reconstructing the odd
part) and the next (reconstructing the even part).

Accepted in Quantum 2022-03-18, click title to verify. Published under CC-BY 4.0.

19

Similarly to D∗ , this kernel satisfies D̃µ (xµ0 ) = δµµ0
but it’s a linear combination of the odd basis functions
sin(`x), ` ∈ [R]. Following from these two properties,
we know that
Eodd (x) =

R
X

Eodd (xµ )D̃µ (x)

(63)

and if we take the limit x → 0:
D∗ 00 (0) = −

2R2 + 1
.
6

(67)

This yields the explicit parameter-shift rule for the
second derivative:

µ=1

=

R
X
Eodd (xµ )
µ=1

2R

"

sin(R(x + xµ ))
sin(R(x − xµ ))
−

×
1
tan 2 (x − xµ )
tan 12 (x + xµ )

#

and we thus can reconstruct Eodd with the R evaluations Eodd (xµ ).
We also can extract from here a closed-form formula
for the derivative at x = 0, as it only depends on the
odd part of E. We arrive at the general parametershift rule:
0

E (0) =

R
X

(−1)R−1
2R2 + 1
+ Eeven (π)
6
2
R−1
 µπ  (−1)µ−1
X

+
Eeven
(68)
µπ .
R sin2 2R
µ=1

E 00 (0) = −Eeven (0)

Again, derivatives of E of higher even order can be
computed in a similar
manner, using the same evalu
ations Eeven µπ
R .

A.2 Hessian parameter-shift rule
Here we consider the spectrum of the function

Eodd (xµ )D̃µ0 (0)

(64)

E (km) (x) := E(x0 + xv k,m ),

µ=1
R
X

sin(Rxµ )
(65)
2R
sin2 ( 12 xµ )
µ=1


R
X
(−1)µ−1
2µ − 1
.
π
=
Eodd
2R
2R sin2 2µ−1
4R π
µ=1
=

Eodd (xµ )

with v k,m = v k + v m . Without loss of generality,
we assume Uk to act first within the circuit and set
x0 = 0. As for the univariate case in Sec. 2.1, we may
explicitly write the cost function as
†
E (km) (x) = hψ| Uk† (x)V † Um
(x)BUm (x)V Uk (x) |ψi

Similarly, as the higher-order derivatives of D̃µ can
be computed analytically, we may obtain derivatives
of E of higher odd orders.
A.1.3

=

d
X

ψj1 vj2 j1 bj2 j3 vj3 j4 ψj4

(70)

j1 ,...j4 =1

 
 
(m)
(m)
(k)
(k)
x ,
× exp i ωj4 − ωj1 + ωj3 − ωj2

Even kernels

Next we reconstruct the even part Eeven again using
the kernel D∗ (x) from above but choosing the R + 1
points xµ = µπ/R for µ ∈ [R]0 . As the spacing between these points is the same as between the previous
{xµ }, we again have D∗ (xµ0 −xµ ) = δµµ0 ; but note we
cannot directly use D∗ (x − xµ ) as our kernel because
D∗ (x − xµ ) is an even function in x − xµ but not in
x. Instead we take the even linear combination

∗

if µ = 0
D (x)
∗
∗
D̂µ (x) := D (x − xµ ) + D (x + xµ ) if 0 < µ < R

 ∗
D (x − π)
if µ = R .
Then the D̂µ are even functions and satisfy D̂µ (xµ0 ) =
δµµ0 , leading to
Eeven (x) =

(69)

R
X

Eeven (xµ )D̂µ (x).

where ω (k,m) are the eigenvalues of the generators of
Uk and Um , respectively, and we denoted the entries
of matrices by lowercase letters as before. We may
read off the occuring frequencies in this Fourier series in terms of the unique positive differences Ω(k,m) ,
(k)
(m)
leading to δΩl1 l2 = ±Ωl1 ± Ωl2 . We again only
collect the positive values as they come in pairs16 .
In case of integer-valued frequencies, there are
Rkm = Rk + Rm such positive frequencies, namely
all integers in [Rk + Rm ]. For arbitrary frequencies, all {δΩ} might be unique and we obtain up to
Rkm = 2Rk Rm + Rk + Rm frequencies. Rescaling the
smallest frequency enforces a small degree of redundancy so that Rkm = 2Rk Rm + Rk + Rm − 2 is always
achievable; for some scenarios specific rescaling factors might drastically reduce Rkm 17 .

(66)

µ=0

The second derivative of D∗ is


sin(Rx) 1 − 2R2 sin2 ( 12 x)
cos(Rx)
∗ 00

D (x) =
−
1
2 1
4R tan( 2 x) sin ( 2 x)
2 sin2 12 x

16 That is, for any δΩ, we also have −δΩ in the Fourier series,
and the representation as real-valued function subsums the two
frequencies.
17 Recall that we used rescaling for the equidistant frequency
case to arrive at integer-valued {Ω}, which in turn made the
significant reduction above possible.

Accepted in Quantum 2022-03-18, click title to verify. Published under CC-BY 4.0.

20

|+i
|0i

U1

X

•

X

•

Uk−1

Uk (x)

Uk

Um (x)

X

•

X

•

Uk−1

Uk (x)

Uk

Um (x)

analysis, we approximate the single-shot variance σ 2
to be constant as detailed in the main text.

H

A.4.1
|+i
|0i

U1

S†

Figure 5: Circuits for the Hadamard tests to measure the
overlap in Eq. (71), adapted from [57, Fig. 5]. The basis rotation in the last operation on the auxiliary qubit determines
whether the real (top) or the imaginary (bottom) part of
hψ(x0 + xv k,m )|ψ(x0 )i is calculated. All unitaries without
argument are understood as Uj = Uj ((x0 )j ).

Norm for general parameter-shift rule

For the case of equidistant shift angles, we can compute the norm of the coefficient vector y (1,2) in the
parameter-shift rules in Eqs. (24,25) explicitly, in order to estimate the required shot budget for the obtained derivative. For the first order, we note that the
evaluations of E come in pairs, with the same coefficient up to a relative sign. This yields (recalling that
xµ = 2µ−1
4R π):
R

ky (1) k1 =

A.3 Hadamard tests for the metric tensor
In order to compute the metric tensor as the Hessian
of the overlap f (x) = − 12 |hψ(x)|ψ(x0 )i|2 , we need to
evaluate it at shifted positions x = x0 + xv k,m . This
can be done by executing the circuit V (x0 ) and the
adjoint circuit V † (x) at the shifted position, and returning the probability to measure the 0 bitstring in
the computational basis. As all operations after the
latter of the two parametrized gates of interest cancel between the two circuits, those operations can be
spared, but the maximal depth is (almost) the doubled depth of V .
Alternatively, we may use a Hadamard test as
derived in the appendix of Ref. [57].
There,
it was designed to realize the derivative overlaps
Re{h∂k ψ(x)|∂m ψ(x)i} for the metric tensor directly,
assuming the generator to be a Pauli word and therefore unitary. However, it can also be used to calculate
the real or imaginary part of
hψ(x)|ψ(x0 )i = h0| U1† ((x0 )1 ) · · · Uk† ((x0 )k + x)
†
†
· · · Um−1
((x0 )m−1 )Um
(x)Um−1 ((x0 )m−1 )

· · · U1 ((x0 )1 ) |0i .

(71)

by measuring the auxiliary qubit in the Z or Y basis.
The corresponding circuit is shown in Fig. 5.
While the original proposal has to split up the generators into Pauli words and implement one circuit
per combination of Pauli words from xk and xm , the
number of circuits here is dictated by the number of
evaluations in the parameter-shift rule. In order to
measure f (x), the real and the imaginary part both
have to be measured, doubling the number of circuits.

1 X
1
= R,
2R µ=1 sin2 (xµ )

which follows from sin−2 (xµ ) = cot2 (xµ ) + 1 and [80,
Formula (445)]:
R
X

cot2 (xµ ) = 2R2 − R.

The `1 -norm of the coefficients in parameter-shift
rules dictates the number of shots required to reach
certain precision (see Sec. 2.3). Here, we explicitly compute this norm for both the general and
decomposition-based parameter-shift rule for the firstand second-order univariate derivative. For the entire

(73)

µ=1

A derivation for Eq. (73) can be adapted from
Ref. [81], which we present below for completeness:
−i(−1)µ = exp(i2Rxµ )

2R
= cos(xµ ) + i sin(xµ )

2R 
X
2R
2R−r
r
=
(cos(xµ ))
(i sin(xµ ))
r
r=0

R 
X
2R
2R−2r
2r
⇒ 0=
(cos(xµ ))
(i sin(xµ ))
2r
r=0

R 
R−r
X
2R 
− cot2 (xµ )
=
2r
r=0
Here we have applied the binomial theorem, extracted
the real part, and divided by (i sin(xµ ))2R (note that
0 < xµ < π/2). From the last equation above, we
see that cot2 (xµ ) is a root of the function g(χ) =
PR 2R
R−r
for all µ ∈ [R]. As g is a polynor=0 2r (−χ)
mial of degree R, we thus know all its roots and may
use the simplest of Vieta’s formulas:
R
X
µ=1

A.4 Coefficient norms for univariate derivatives via equidistant shifts

(72)

τµ = −

gR−1
gR

(74)

with roots {τµ }µ of g, and gj the jth order Taylor
coefficient of g. Plugging in the known roots and coefficients we get

Accepted in Quantum 2022-03-18, click title to verify. Published under CC-BY 4.0.

R
X

(−1)R−1 2R
2
cot (xµ ) = −

R 2R
(−1)
0
µ=1
2

= 2R2 − R.


(75)
(76)
21

For the second order we may repeat the above
computation
small
modifications18 , arriving at

PR−1with
2R
g(χ) = r=0 2r+1 (−χ)R−r and therefore at
2R
(2)
ky 1 k =

2R

(−1)R−1 3
+1 1
+ + (R − 1) −

6
2
(−1)R 2R
1

2

= R2 .
A.4.2



(77)

Norm for decomposition

P

X
1
[E (k) (x1 ) − E (k) (−x1 )], (78)
2 sin(x1 )
k=1

where E (k) denotes the cost function based on the
decomposition, in which only the parameter of the kth
elementary gate is set to the shifted angle x1 and to
0 in all other gates. To maximize sin(x1 ), we choose
x1 = π/2, and as a reuslt all 2P coefficients have
magnitude 1/2, and therefore
(1)

ky decomp k1 = P.

P
X
1
2 sin2 (x1 ) k,m=1

(80)

k<m


E (km) (x1 , x1 ) − E (km) (−x1 , x1 )
− E (km) (x1 , −x1 ) + E (km) (−x1 , −x1 )

Similar to the previous section, we compute the coefficient norms for three methods to compute the Hessian for equidistant frequencies and shifts: We may
use the diagonal shift rule in Eq. (36), repeat the
general parameter-shift rule, or decompose the circuit
and repeat the original parameter-shift rule. For the
first approach, the diagonal entries of the Hessian—
and thus the shifted evaluations for those entries—are
reused to compute the off-diagonal ones, whereas the
shifted evaluations for the repeated shift rule are distinct for all Hessian entries. This difference makes
the cost comparison for a single Hessian entry difficult. We therefore consider the root mean square of
the Frobenius norm of the difference between the true
and the estimated Hessian as quality measure. The
matrix of expected deviations is given by the standard
deviations σkm so that we need to compute
v
v
uX
u X
u n 2 X 2
u n
2
t
σkm = t
σk +
2σkm .
(82)
ε=
k,m=1

(79)

Due to all coefficients being equal, the optimal shot
allocation is N/(2P) for all terms.
For the second-order derivative, the full Hessian has
to be computed from the decomposition as described
in Ref. [46] and all elements have to be summed19 :
E 00 (0) =

1
1 P
(1)
= P 2 . (81)
ky decomp k1 = 2P(P − 1) + P +
2
2
2
Here the optimal shot allocation is to measure all
shifted terms with N/(2P 2 ) shots, and E(0) with
N/(2P) shots.

A.5 Coefficient norms for the Hessian

If we compute the first- and second-order derivatives
via a decomposition that contains P parametrized elementary gates, we need to apply the original two-term
parameter-shift rule to each of these gates separately.
For the first-order derivative, we simply sum all elementary derivatives. For integer-valued frequencies,
x typically feeds without prefactor into the gates in
the decomposition, so that the decomposition-based
shift rule reads
E 0 (0) =

1/2 for the off-diagonal terms, P coefficients of magnitude 1/2 for the E (k) (π) and one coefficient with
magnitude P/2 for E(0), summing to



A.5.1

k=1

where E (km) (x1 , x2 ) is defined analogously to E (k) but
the shift angles put into the kth and mth elementary gate may differ. Fixing the shift angle to π/2
again, we have 2P(P − 1) coefficients of magnitude
18 Recall that the angles differ between the two derivatives.
19 Here we do not anticipate the cheaper Hessian evaluation
from Sec. 4.1.

k<m

Hessian shift rule

The variance for a Hessian diagonal entry Hkk is
σ 2 Rk4 /Nkk if we use Nkk shots to estimate it (see
Eq. (29))20 . For an off-diagonal element Hkm computed via the diagonal shift rule in Eq. (36), the variance is


4
1 σ 2 (Rk + Rm )4
σ 2 Rk4
σ 2 Rm
2
σkm =
+
+
, (83)
4
Nkm
Nkk
Nmm
where we used that Rkm = Rk + Rm for equidistant
frequencies. Overall, this yields
n
X σ 2 (Rk + Rm )4
X
σ 2 Rk4 n + 1
2
+
(84)
ε =
Nkk
2
2Nkm
k=1

P

1 X (k)
+
[E (π) − E(0)]
2

k=1

k<m

If we allocate Ndiag shots optimally, that is Nkm is
proportional to the square root of the coefficient of
−1
Nkm
, we require
" n
#2
r
X 1
σ2 X 2 n + 1
2
√ (Rk + Rm )
Ndiag = 2
Rk
+
ε
2
2
k=1
k<m
i2

σ2 h √
= 2
(85)
n + 1 + n − 2 kRk22 + kRk21
2ε
shots to estimate H to a precision of ε.
20 Recall that σ 2 is the single-shot variance.

Accepted in Quantum 2022-03-18, click title to verify. Published under CC-BY 4.0.

22

A.5.2

Repeated general parameter-shift rule

Without the diagonal shift rule, we compute Hkm by
executing the univariate general parameter-shift rule
in Eq. (24) for xk and xm successively, i.e., we apply
the rule for xm to all terms from the rule for xk . This
leads to 4Rk Rm terms with their coefficients arising
from the first-order shift rule coefficients by multiplying them together:
ky (km) k1 =

Rk
Rm
X
X
1
1
1
2
2
4Rk Rm µ=1 sin (xµ ) 0 sin (xµ0 )
µ =1

= Rk Rm ,

(86)

where we used Eq. (72). Correspondingly, the variance for Hkm computed by this methods with an
2
optimal shot allocation of Nkm shots is σkm
=
2 2 2
σ Rk Rm /Nkm . The mean square of the Frobenius
norm then is
ε2 =

n
X
σ 2 R4

k

k=1

Nkk

+

X 2σ 2 R2 R2
k

k<m

Nkm

m

(87)

and an optimal shot allocation across the entries of
the Hessian to achieve a precision of ε will require
" n
#2
σ2 X 2 X √
Rk +
2Rk Rm
NgenPS = 2
ε
k=1
k<m
i2

σ2 h √
= 2
2 − 1 kRk22 + kRk21
(88)
2ε
shots in total.
A.5.3

Decomposition and repeated original shift rule

For the third approach, we only require the observation that again all (unique) Hessian entries are estimated independently and that the coefficients arise
from all products of two coefficients from the separate
shift rules for xk and xm . This yields 4Pk Pm coefficients with magnitude 1/4, so that the calculation of
ε is the same as for the previous approach, replacing
R by P. The required shot budget for a precision of
ε is thus
i2

σ2 h √
Ndecomp = 2
2 − 1 kPk22 + kPk21
(89)
2ε

B Generalization to arbitrary spectra
Throughout this work, we mostly focused on cost
functions E with equidistant — and thus, by rescaling, integer-valued — frequencies {Ω` }. Here we will
discuss the generalization to arbitrary frequencies,
mostly considering the changed cost.

B.1 Univariate functions
The nonuniform DFT used to reconstruct the full
function E in Sec. 3.1, and its modifications for the

odd and even part in Secs. 3.2 and 3.3, can be used
straightforwardly for arbitrary frequencies. However, choosing equidistant shift angles {xµ } will no
longer make the DFT uniform, as was the case for
equidistant frequencies. Correspondingly, the explicit
parameter-shift rules for E 0 (0) and E 00 (0) in Eqs. (24,
25) do not apply and in general we do not know a
closed-form expression for the DFT or the parametershift rules. Symbolically, the parameter-shift rule
takes the form
E 0 (0) =

R
X

yµ(1) [E(xµ ) − E(−xµ )]

(90)

µ=1
(2)

E 00 (0) = y0 E(0) +

R
X

yµ(2) [E(xµ ) + E(−xµ )]. (91)

µ=1

Regarding the evaluation cost, the odd part and
thus odd-order derivatives can be obtained at the
same price of 2R evaluations of E as before, but the
even part might no longer be periodic in general; as a
consequence,
Eeven (π) =

1
(E(π) + E(−π)) 6= E(π)
2

(92)

actually may require two evaluations of E, leading to
2R + 1 evaluations overall. If the even part is periodic, which is equivalent to all involved frequencies
being commensurable, with some period T , evaluating
Eeven (T /2) allows to skip the additional evaluation.
When comparing to the first derivative based on a
decomposition into P parametrized elementary gates,
the break-even point for the number of unique circuits
remains at R = P as for equidistant frequencies, but
we note that e.g., a decomposition of the form
U (x) =

P
Y

Uk (βk x),

(93)

k=1

namely where x is rescaled individually in each elementary gate by some βk ∈ R, in general will result in
R = P 2 frequencies of E, making the decompositionbased parameter-shift rule beneficial. For the secondorder derivative, the number of evaluations 2R + 1
might be quadratic in P in the same way, but the decomposition requires 2P 2 − P + 1 as well, so that the
requirements are similar if R = P.
Regarding the required number of shots, we cannot make concrete statements for the general case as
we don’t have a closed-form expression for the coefficients y, but note that for the decomposition approach, rescaling factors like the {βk } in Eq. (93)
above have to be factored in via the chain rule, leading
to a modified shot requirement.
An example for unitaries with non-equidistant frequencies would be the QAOA layer that implements
the time evolution under the problem Hamiltonian
(see Eq. (26)) for MaxCut on weighted graphs with
non-integer weights.

Accepted in Quantum 2022-03-18, click title to verify. Published under CC-BY 4.0.

23

For the stochastic parameter-shift rule in Sec. 3.6
we did not restrict ourselves to equidistant frequencies
and derive it in App. C for general unitaries of the
form UF = exp(i(xG + F )) directly.

parameter-shift rule, the authors show21

Z 1
E 0 (x0 ) =
dt tr UF† (tx0 )B UF (tx0 )
0

h

× i G , UF (1 − t)x0 |ψihψ| UF† (1 − t)x0

B.2 Multivariate functions
While the univariate functions do not differ strongly
for equidistant and arbitrary frequencies in E and
mostly the expected relation between R and P
changes, the shift rule for the Hessian and the metric
tensor are affected heavily by generalizing the spectrum. First, the univariate restriction E (km) (x) in
Eq. (34) still can be used to compute the off-diagonal
entry Hkm of the Hessian but this may require up to
2Rkm + 1 = 4Rk Rm + 2Rk + 2Rm − 3 evaluations (see
App. A.2), in contrast to 2Rkm = 2(Rk + Rm ) in the
equidistant case. Compared to the resource requirements of the decomposition-based approach, 4Pk Pm ,
this makes our general parameter-shift rule more expensive if Rk & Pk .
As we use the same method to obtain the metric
tensor F, the number of evaluations grows in the same
manner, making the decomposition-based shift rule
more feasible for unitaries with non-equidistant frequencies. As f (x0 ) does not have to be evaluated,
an off-diagonal element Fkm requires one evaluation
fewer than Hkm , namely 4Rk Rm + 2Rk + 2Rm − 4.

where we again denoted the state prepared by the circuit before UF by |ψi and the observable transformed
by the circuit following UF by B. By using Eq. (95)
to express the commutator, we obtain

Z 1
X
0
E (x0 ) =
dt
yµ tr UF† (tx0 )B UF (tx0 ) (97)
0

µ

× U (xµ )UF (1 − t)x0 |ψihψ| UF†


In this section we describe a stochastic variant of
the general parameter-shift rule which follows immediately from combining the rule for single-parameter
gates in Eq. (90) with the result from Ref. [39].
First, note that any shift rule
E 0 (x0 ) =

X

yµ E(x0 + xµ ),

(94)

µ

X

yµ U (xµ )ρU † (xµ ),



(1 − t)x0 U (xµ ) .

UF,µ (x0 , t) := UF (tx0 )U (xµ )UF (1 − t)x0



(98)

and denote the cost function that uses UF,µ (x0 , t) instead of UF (x0 ) as
n
o
†
Eµ (x0 , t) := tr B UF,µ
(x0 , t) |ψihψ| UF,µ (x0 , t) .
Rewriting Eq. (97) then yields the generalized stochastic parameter-shift rule
Z 1 X
0
E (x0 ) =
dt
yµ Eµ (x0 , t).
(99)
µ

It can be implemented by sampling values for the
splitting time t, combining the shifted energies
Eµ (x0 , t) for each sampled t with the coefficients yµ ,
and averaging over the results.

D Details on QAD
In this section we provide details on the latter two
of the three modifications of the QAD algorithm discussed in Sec. 5.3.

D.1 Extended QAD model for Pauli rotations

with coefficients {yµ } and shift angles {xµ } for a unitary U (x) = exp(ixG), implies that we can implement
the commutator with G:
i[G, ρ] =

†



We abbreviate the interleaved unitaries

0

C General stochastic shift rule

(96)

i

(95)

µ

since the commutator between G and the Hamiltonian
directly expresses the derivative of the expectation
value E 0 (0) on the operator level, and shift rules hold
for arbitrary states.
Now consider the extension UF (x) = exp(i(xG +
F )) of the above unitary. In the original stochastic

The QAD model introduced in Ref. [49] contains
trigonometric functions up to second (leading) order.
The free parameters of the model cannot be extracted
with one function evaluation per degree of freedom,
because unlike standard monomials in a Taylor expansion, the trigonometric basis functions mix the orders
in the input parameters. This leads to the mismatch
of 2n2 + n + 1 (original QAD) or 3n2 /2 + n/2 + 1 (see
above) evaluations to obtain n2 /2+3n/2+1 model parameters. We note that the QAD model contains full
univariate reconstructions at optimal cost, extracting
21 To be precise, we here combine Eqs. (11-13) in Ref. [39]
into a general expression for E 0 .

Accepted in Quantum 2022-03-18, click title to verify. Published under CC-BY 4.0.

24

the 2n + 1 model parameters E (A) , E (B) and E (C)
from 2n + 1 function evaluations. The doubly shifted
evaluations, however, are used for the Hessian entry
only:
(D)

Ekm =


1  ++
+−
−+
−−
E
− Ekm
− Ekm
+ Ekm
,
4 km

(100)

±±
where Ekm
= E(x0 ± π2 v k ± π2 v m ) and we recall that
this QAD model is restricted to Pauli rotations only.
Let us now consider a slightly larger truncation of
the cost function than the one presented in App. A 2
in [49]:

E̊(x0 + x) = A(x) E (A)

x 2
x
+ 2E (C) · tan
+ 2E (B) · tan
2
x 2
x
(D)
+ 4 tan
E
tan
(101)
2
2x 
x
+ 4 tan
E (F ) tan2
2
2
 
 
2 x
(G)
2 x
+ 4 tan
E
tan
2
2
Q
with A(x) = k cos2 (xk /2). E (F ) and E (G) have zeros on their diagonals because there are no terms of
the form sin3 (xk /2) or sin4 (xk /2) in the cost function, and for E (G) we only require the strictly upper
triangular entries due to symmetry. The higher-order
terms contain at least three distinct variables xk , xl
and xm because all bivariate terms are captured in
the above truncation. Using
 π
 π
 1
π
and tan ±
A ± vk ± vm =
= ±1,
4
4
4
4

circuit to consist of Pauli rotation gates exclusively.
In the spirit of the generalized function reconstruction
and parameter-shift rule, we would like to relax this
assumption and generalize the QAD model. However,
there is no obvious unique way to do this, because the
correspondence between the gradient and E (B) and
between the Hessian and E (C,D) is not preserved for
multiple frequencies. Instead, the uni- and bivariate
Fourier coefficients of E form the model parameters
and the derivative quantities are contractions with the
frequencies thereof. There are multiple ways in which
we could generalize QAD to multiple frequencies.
The first way to generalize QAD is to compute the
gradient and Hessian with the generalized parametershift rule Eq. (24) and the shift rule for Hessian entries
Eq. (36) and to construct a single-frequency model as
in original QAD. Even though we know the original
energy function to contain multiple frequencies, this
would yield a local model with the correct secondorder expansion at x0 that exploits the evaluations
savings shown in this work. As QAD is supposed to
use the model only in the neighbourhood of x0 , this
might be sufficient for the optimization.
As a second generalization we propose a full
trigonometric interpolation of E up to second order,
similar to the univariate reconstruction in Sec. 3.1.
First we consider the univariate part of the model:
Start by evaluating E at positions shifted in the kth
coordinate by equidistant points and subtract E(x0 ),
Eµ(k) := E(x0 + xµ v k ) − E(x0 )
2µπ
, µ ∈ [2Rk ].
xµ :=
2Rk + 1

(B)

(F )

+ Ekm

Dµ(k) (x) =

1
2Rk + 1

1+2

Rk
X

!
cos(`(x − xµ ))

`=1

(C)

−+
+−
−−
++
Ekm
+ Ekm
+ Ekm
+ Ekm
= E (A) + 2Ek

(104)
sin 21 (2Rk + 1)(x − xµ )

=
(2Rk + 1) sin 12 (x − xµ )


(G)

(C)
+ 2Em
+ 4Ekm .
±±
This means that the 4 function evaluations Ekm
that
(D)
are used for Ekm in the original QAD can be recy(F )
(F )
(G)
cled to obtain the 3 parameters Ekm , Emk and Ekm .
The corresponding model is of the form Eq. (101)
and therefore includes all terms that depend on two
parameters only. Consequentially, the constructed
model exactly reproduces the cost function not only
on the coordinate axes but also on all coordinate
planes spanned by any two of the axes. The number of model parameters is 2n2 + 1, which matches
the total number of function evaluations.

D.2 Trigonometric interpolation for QAD
Both the original QAD algorithm, and the extension
introduced above, assume the parametrized quantum

(103)

Then consider the (shifted) Dirichlet kernels

we now can compute:
−+
+−
−−
++
Ekm
− Ekm
+ Ekm
− Ekm
= Ek

(102)

(105)

(k)

which satisfy Dµ (xµ0 ) = δµµ0 and are Fourier series with integer frequencies up to Rk . Therefore, the
function22
Ê (k) (x) =

2Rk
X

Eµ(k) Dµ(k) (x)

(106)

µ=1

coincides with E(x0 + xv k ) − E(x0 ) at 2Rk + 1 points
and is a trigonometric polynomial with the same Rk
frequencies.
22 One might be wondering why to subtract E(x ) just to add
0
it manually back into the reconstruction now. This is because
we need to avoid duplicating this term when adding up the
univariate and bivariate terms of all parameters later on.

Accepted in Quantum 2022-03-18, click title to verify. Published under CC-BY 4.0.

25

(km)

Similarly, the product kernels Dµµ0 (xk , xm ) =
(k)

(m)

Dµ (xk )Dµ0 (xm ) can be used to reconstruct the bivariate restriction of E to the xk −xm plane. For this,
evaluate the function at doubly shifted positions and
subtract both, E(x0 ) and the univariate parts:
(km)
Eµµ0 := E(x0 + xµ v k + xµ0 v m )

(107)

− Ê (k) (xµ ) − Ê (m) (xµ0 ) − E(x0 )

(108)

Then, the bivariate Fourier series
Ê (km) (xk , xm ) =

2RX
k ,2Rm

(km)

(km)

Eµµ0 Dµµ0 (xk , xm )

µ,µ0 =1

(109)
coincides with E(x0 + xk v k + xm v m ) − E(x0 ) −
Ê (k) (xk ) − Ê (m) (xm ) on the entire coordinate plane
spanned by v k and v m .
As we constructed the terms such that they do not
contain the respective lower order terms, we finally
can combine them to the full trigonometric interpolation:
Êinterp (x) = E(x0 ) +

n
X

Ê (k) (xk )

(110)

k=1

+

X

Ê (km) (xk , xm ).

k<m

This model has as many parameters as function evaluations, namely 2(kRk21 −kRk22 +kRk1 )+1, and therefore, the trigonometric interpolation is the generalization of the extended QAD model in App. D.1. Indeed,
for Rk = 1 for all k we get back 2(n2 − n + n) + 1 =
2n2 + 1 evaluations and model parameters.
We note that the trigonometric interpolation can
be implemented for non-equidistant evaluation points
in a similar manner and with the same number of
evaluations, although the elementary functions are no
longer Dirichlet kernels but take the form
D̊µ(k) (x) =

 2R

sin 12 x Yk sin 12 (x − xµ0 )

 . (111)
sin 12 xµ µ0 =1 sin 21 (xµ − xµ0 )

Accepted in Quantum 2022-03-18, click title to verify. Published under CC-BY 4.0.

26

