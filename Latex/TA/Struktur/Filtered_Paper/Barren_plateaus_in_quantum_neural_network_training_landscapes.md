ARTICLE
DOI: 10.1038/s41467-018-07090-4

OPEN

Barren plateaus in quantum neural network training
landscapes

1234567890():,;

Jarrod R. McClean1, Sergio Boixo

1, Vadim N. Smelyanskiy1, Ryan Babbush1 & Hartmut Neven1

Many experimental proposals for noisy intermediate scale quantum devices involve training a
parameterized quantum circuit with a classical optimization loop. Such hybrid quantumclassical algorithms are popular for applications in quantum simulation, optimization, and
machine learning. Due to its simplicity and hardware efﬁciency, random circuits are often
proposed as initial guesses for exploring the space of quantum states. We show that the
exponential dimension of Hilbert space and the gradient estimation complexity make this
choice unsuitable for hybrid quantum-classical algorithms run on more than a few qubits.
Speciﬁcally, we show that for a wide class of reasonable parameterized quantum circuits, the
probability that the gradient along any reasonable direction is non-zero to some ﬁxed precision is exponentially small as a function of the number of qubits. We argue that this is
related to the 2-design characteristic of random circuits, and that solutions to this problem
must be studied.

1 Google Inc., 340 Main Street, Venice, CA 90291, USA. Correspondence and requests for materials should be addressed to

J.R.M. (email: jmcclean@google.com) or to S.B. (email: boixo@google.com) or to V.N.S. (email: smelyan@google.com)
NATURE COMMUNICATIONS | (2018)9:4812 | DOI: 10.1038/s41467-018-07090-4 | www.nature.com/naturecommunications

1

ARTICLE

NATURE COMMUNICATIONS | DOI: 10.1038/s41467-018-07090-4

R

apid developments in quantum hardware have motivated
advances in algorithms to run in the so-called noisy
intermediate scale quantum (NISQ) regime1. Many of the
most promising application-oriented approaches are hybrid
quantum–classical algorithms that rely on optimization of a
parameterized quantum circuit2–8. The resilience of these
approaches to certain types of errors and high ﬂexibility with
respect to coherence time and gate requirements make them
especially attractive for NISQ implementations3,9–11.
The ﬁrst implementation of such algorithms was developed in
the context of quantum simulation with the variational quantum
eigensolver2,3. This algorithm has been successfully demonstrated
on a number of experimental setups with extensions to excited
states and other forms of incoherent error mitigation2,9,12–16.
Since then, the quantum approximate optimization algorithm was
developed in a similar context to address hard optimization
problems5,17–19. This algorithm has also been demonstrated on
quantum devices20. These approaches have even been extended to
both quantum machine learning and error correction6,7,20–23.
While the precise formulation of these methods and their
domains of applicability differ considerably, they typically tend to
rely upon the optimization of some parameterized unitary circuit
with respect to an objective function that is typically a simple sum
of Pauli operators or ﬁdelity with respect to some state. This
framework is reminiscent of the methodology of classical neural
networks23,24. As with any non-linear optimization, the choice of
both the parameterization and the initial state is important. In
quantum simulation, there is often a choice inspired by physical
domain knowledge3,17,25–29. However, in all domains of applicability, there have been implementations that utilize parametrized
random circuits of varying depth7,13,21,23,30. Within quantum
simulation that approach has been referred to as a “hardware
efﬁcient ansatz”13. This is in contrast to the previous proposals,
such as the variational quantum eigensolver2,3,9, which used
parametrized structured circuits inspired by the problem at hand,
such as unitary coupled cluster.
When little structure is known about the problem, or constraints
of the existing quantum hardware may prevent utilizing that
structure, choosing a random implementable circuit seems to provide an unbiased choice. One might also expect, based on recent
experimental designs for “quantum supremacy”, that random
quantum circuits are a powerful tool for such a task31. Also, despite
concerns about gradient-based methods in classical deep neural
networks32–34, they are successful24, even if using random

f (x )



<f >

initialization33,35. However, in the quantum case one must
remember that the estimation of even a single gradient component
will scale as O(1/εα) for some small power α36 as opposed to
classical implementations where the same is achieved in O(log(1/ε))
time, where ε is the desired accuracy in the gradient that is inevitably tied to its magnitude.
We will present results related to random quantum circuits in
the context of the exponential dimension of Hilbert space and
gradient-based hybrid quantum–classical algorithms. A cartoon
depiction of this is given in Fig. 1. We show that for a large class
of random circuits, the average value of the gradient of the
objective function is zero, and the probability that any given
instance of such a random circuit deviates from this average value
by a small constant ε is exponentially small in the number of
qubits. This can be understood in the geometric context of concentration of measure37–39 for high-dimensional spaces. When
the measure of the space concentrates in this way, the value of any
reasonably smooth function will tend towards its average with
exponential probability, a fact made formal by Levy’s lemma40. In
our context, this means that the gradient is zero over vast reaches
of quantum space. The region where the gradient is zero does not
correspond to local minima of interest, but rather an exponentially large plateau of states that have exponentially small deviations in the objective value from the average of the totally mixed
state. We argue that the depth of circuits which achieve these
undesirable properties are modest, requiring only O(n1/d) depth
circuits on a d dimensional array, and numerically evaluate the
constant factors one expects to encounter for small instances of
this kind. While our results highlight the importance of avoiding
random initialization in parametric circuit approaches, they do
not discount the value of random quantum circuits in other
applications such as information security or demonstrations of
quantum supremacy. We close with an outlook on how this result
should shape strategies in ansatz design for scaling to larger
experiments.
Results
Gradient concentration in random circuits. We will discuss
random parameterized quantum circuits (RPQCs)
UðθÞ ¼ Uðθ1 ; :::; θL Þ ¼

L
Y

Ul ðθl ÞWl ;

ð1Þ

l¼1

where Ul(θl) = exp(−iθlVl), Vl is a Hermitian operator, and Wl is
a generic unitary operator that does not depend on any angle θl.
Circuits of this form are a natural choice due to a straightforward
evaluation of the gradient with respect to most objective functions
and have been introduced in a number of contexts already26,41.
Consider an objective function E(θ) expressed as the expectation
value over some Hermitian operator H,
EðθÞ ¼ h0jUðθÞy HUðθÞj0i:

ð2Þ

U(θ)

x
Fig. 1 Cartoon of concentration of quantum observables. The sphere depicts
the phenomenon of concentration of measure in quantum space: the
fraction of states that fall outside a ﬁxed angular distance from zero along
any coordinate decreases exponentially in the number of qubits40. This
implies a ﬂat plateau where observables concentrate on their average over
Hilbert space and the gradient is exponentially small. The fact that only an
exponentially small fraction of states fall outside of this band means that
searches resembling random walks will have an exponentially small
probability of exiting this “barren plateau”
2

When the RPQCs are parameterized in this way, the gradient
of the objective function takes a simple form:
D  h
i  E
∂EðθÞ


¼ i 0Uy Vk ; Uþy HUþ U 0 ;
∂k E 
ð3Þ
∂θk
Qk1
Ul ðθl ÞWl ,
where Qwe introduce the notations U  l¼0
L
Uþ  l¼k Ul ðθl ÞWl , and henceforth drop the subscript k from
Vk → V for ease of exposition. Finally, we will deﬁne our RPQCs U
(θ) to have the property that for any gradient direction ∂kE
deﬁned above, the circuit implementing U(θ) is sufﬁciently
random such that either U−, U+, or both match the Haar

NATURE COMMUNICATIONS | (2018)9:4812 | DOI: 10.1038/s41467-018-07090-4 | www.nature.com/naturecommunications

ARTICLE

NATURE COMMUNICATIONS | DOI: 10.1038/s41467-018-07090-4

distribution up to the second moment, and the circuits U− and
U+ are independent.
Our results make use of properties of the Haar measure on the
unitary group dμHaar(U) ≡ dμ(U), which is the unique left- and
right-invariant measure such that
Z
Z
Z
dμðUÞf ðUÞ ¼ dμðUÞf ðVUÞ ¼ dμðUÞf ðUVÞ; ð4Þ

uniformly in the D = 2n − 1 dimensional hypersphere. The
derivative with respect to the parameters θ is Lipschitz
continuous with some parameter η that depends on the operator
H. Levy’s lemma then implies that the variance of measurements
will decrease exponentially in the number of qubits. This intuition
may be made more precise through explicit calculation of the
variance, which is done in more detail in the Methods. The result
to ﬁrst order is

for any f(U) and V∈U(N), where the integration domain will be
implied to be U(N) when not explicitly listed. While this property
is valuable for proofs, quantum circuits that exactly achieve this
invariance generically require exponential resources. This motivates the concept of unitary t-designs42–44, which satisfy the
above properties for restricted classes of f(U), often requiring only
modest polynomial resources. Suppose {pi, Vi} is an ensemble of
unitary operators, with unitary Vi being sampled with probability
pi. The ensemble {pi, Vi} is a t-design if
Z
X
pi Vit ρðViy Þt ¼ dμðUÞU t ρðU y Þt :
ð5Þ

D
8
2 E
Trðρ2 Þ
y
>

Tr
V;
u
Hu
>
2n
ð2 1Þ
>
>
U
<
D
E þ
Var½∂k E   Tr2nðH 2 Þ Tr V; uρuy 2
> ð2 1Þ
>
U
>
>
: 1
2
2
TrðH ÞTrðρ ÞTrðV 2 Þ
2ð3n1Þ

UðNÞ

i

This deﬁnition is equivalent to the property that if f(U) is a
polynomial of at most degree t in the matrix elements of U and at
most degree t in the matrix elements of U*, then averaging over
the t-design {pi, Vi} will yield the same result as averaging over the
unitary group with the respect to the Haar measure.
The average value of the gradient is a concept that requires
additional speciﬁcation because, for a given point, the gradient
can only be deﬁned in terms of the circuit that led to that point.
We will use a practical deﬁnition that leads to the value we are
interested in, namely
Z
ð6Þ
h∂k Ei ¼ dUpðUÞ∂k h0jUðθÞy HUðθÞj0i;
where p(U) is the probability distribution function of U. A review
on the properties of products of independent random matrices
can be found in ref.45. The assumptions of independence and at
least one of U− or U+ forming a 1-design in our RPQCs implies
that 〈∂kE〉 = 0, as shown in the Methods.
Levy’s lemma informs our intuition about the the expected
variance of this quantity through simple geometric arguments. In
particular, Haar random unitaries on n qubits will output states

a

ð7Þ

where the notation hf ðuÞiUx indicates the average with u drawn
from p(Ux), and the ﬁrst case corresponds to U− being a 2-design
and not U+, the second to U+ being a 2-design but not U−, and
the third to both U+ and U− being 2-designs. We emphasize the
fact that this variance depends at most on polynomials of degree 2
in U and polynomials of degree 2 in U*. Whereas a unitary 2design will exhibit the correct variance43,46, a unitary 1-design
will exhibit the correct average value, but not necessarily the
variance. As a result, if a circuit is of sufﬁcient depth that for any
∂kE, either U− or U+ forms a 2-design, then with high probability
one will produce an ansatz state on a barren plateau of the
quantum landscape, with no interesting search directions in sight.
From these results, it is clear that only either U+ or U− needs
to be sufﬁciently random to poison the gradient for the remainder
of the circuit. For example, while it is somewhat unintuitive, even
the ﬁrst element of a circuit, k = 1, will have a vanishing gradient
due to the circuit following it, U+. Additionally, we see that there
is no detailed dependence on the structure of Vk, other than the
rate at which they help randomize the circuit, determining at
what depth one expects to ﬁnd an approximate 2-design.
Numerical simulations. The previous section shows that for
reasonable classes of RPQCs at a sufﬁcient number of qubits and
depth, one will end up on a barren plateau. Here we verify this
result for even modest depth one-dimensional (1D) random
circuits with numerical simulations. This helps to clarify the rate
of concentration for realistic circuits and shows the transition as

b

Ul (l)

Wl

⎢0〉

RY ( 4 )

RP1,1 (1,1)

⎢0〉

RY ( 4 )

RP1,2 (1,2)

⎢0〉

RY ( 4 )

RP1,3 (1,3)

⎢0〉

RY ( 4 )

RP1,4 (1,4)

⎢0〉

RY ( 4 )

RP1,5 (1,5)

Fig. 2 Structure of quantum circuits. a The generic subunit of circuits we study in this work, with a parameterized component Ul(θl) and
  non-parameterized
unit Wl for each layer l. b Example schematic of the 1D random circuits used in our numerical experiments. The circuit begins with RY 4π gates applied to all
qubits followed by a speciﬁed number of layers of randomly chosen Pauli rotations applied to each qubit and then a 1D ladder of controlled Z gates. The
 
initial RY 4π gates are not repeated in each layer. The indices i and j in θi,j index the layer and qubit, respectively. For each layer and qub it Pi,j ∈ {X, Y, Z}
and θi,j∈[0,2π) are sampled independently
NATURE COMMUNICATIONS | (2018)9:4812 | DOI: 10.1038/s41467-018-07090-4 | www.nature.com/naturecommunications

3

ARTICLE

NATURE COMMUNICATIONS | DOI: 10.1038/s41467-018-07090-4

100

Slope = –0.685

10–1

10–1

10–2

10–2

( 1, 1E ) variance

( 1, 1E ) variance

10–3
10–4
10–5
10–6

10–4
10–5

10–7

10–6

10–8

10–7
5

10

15
n Qubits

20

25

Fig. 3 Exponential decay of variance. The sample variance of the gradient
of


the energy for the ﬁrst circuit component of a two-local Pauli term ∂θ1;1 E
plotted as a function of the number of qubits on a semi-log plot. As
predicted, an exponential decay is observed as a function of the number of
qubits, n, for both the expected value and its spread. The slope of the ﬁt line
is indicative of the rate of exponential decay as determined by the operator

the circuit grows in length from a single layer to a circuit
demonstrating statistics analogous to a 2-design.
The circuits and objective functions used in our numerical
experiments begin with a layer of RY(π/4) = exp(−iπ/8 Y) gates to
prevent X, Y, or Z from being an especially preferential direction
with respect to gradients. Then, the circuit proceeds by a number
of layers. Each layer consists of a parallel application of single
qubit rotations to all qubits, given by RP(θ) where P∈{X, Y, Z} is
chosen with uniform probability and θ∈[0, 2π) is also chosen
uniformly. This layer is followed by a layer of 1D nearest
neighbor controlled phase gates, as in Fig. 2. Thus, the number of
angles is the number of qubits times the number of layers.
The objective operator H is chosen to be a single Pauli ZZ
operator acting on the ﬁrst and second qubits, H = Z1Z2. The
gradient is evaluated with respect to the ﬁrst parameter, θ1,1. This
simple choice helps to extract the exponential scaling. As complex
objectives can be written as sums of these operators, the results
for large objectives can be inferred from these numbers.
Moreover, it is clear that for any polynomial sum of these
operators, the exponential decay of the signal in the gradient will
not be circumvented.
From Fig. 3 we see that for a single 2-local Pauli term, both the
expected value of the gradient and its spread decay exponentially
as a function of the number of qubits even when the number of
layers is a modest linear function. Empirically for our linear
connectivity, we see that value is about 10n where n is the number
of qubits, following the expected scaling of O(n1/d) where d is the
dimension of the connectivity. For empirical reference, the
expected gate depth in a chemistry ansatz such as unitary coupled
cluster is at least O(n3), meaning that if the initial parameters
were randomized, this effect could be expected on less than 10
orbitals, a truly small problem in chemical terms. We also observe
in Fig. 4 that as the number of layers increases, there is a
transition to a 2-design where the variance converges. This leads
4

10–3

0

100

200
300
L layers

400

500

Fig. 4 Convergence to 2-design limit. Here we show the sample variance of
the gradient of the
 energy for the ﬁrst circuit component of a two-local
Pauli term ∂θ1;1 E plotted as a function of the number of layers, L, in a 1D
quantum circuit. The different lines correspond to all even numbers of
qubits between 2 and 24, with 2 qubits being the top line, and the rest
being ordered by qubit number. The dotted black lines depict the 2-design
asymptotes for this Hamiltonian as determined by our analytic results. This
shows the convergence of the second moment as a function of the number
of layers to a ﬁxed value determined by the number of qubits

to a distinct plateau as the circuit length increases, where the
height of the plateau is determined by the number of qubits. An
additional example with an objective function deﬁned by
projection on a target state is provided as Supplementary
Figures 1 and 2, showing the rapid decay of variance and similar
plateaus as a function of circuit length. These results substantiate
our conclusion that gradients in modest-sized random circuits
tend to vanish without additional mitigating steps.
Contrast with gradients in classical deep networks. Finally, we
contrast our results with the vanishing (and exploding) gradient
problem of classical deep neural networks32–34,47. At least two
key differences are present in the quantum case: (i) the different
scaling of the vanishing gradient and (ii) the complexity of
computing expected values.
The gradient in a classical deep neural network can vanish
exponentially in the number of layers32,33, while in a quantum
circuit the gradient may vanish exponentially in the number of
qubits, as shown above. In the classical case, the gradient for a
weight in a neuron depends on the sum of all the paths
connecting that neuron to the output, and when the weights are
initialized with random values the paths have random signs
which cancels the signal32. The number of paths is exponential in
the number of layers. In the quantum case, the number of paths is
exponential in the number of gates, and also have random
signs31. The gradient saturates to an exponential in the number of
qubits because the output state is normalized.
The estimation of the gradient for each training batch for a
classical neural network is limited by machine precision and
scales with O(log(1/ε)). Even if the gradient is small, as long as it
is consistent enough between batches, the method may eventually

NATURE COMMUNICATIONS | (2018)9:4812 | DOI: 10.1038/s41467-018-07090-4 | www.nature.com/naturecommunications

ARTICLE

NATURE COMMUNICATIONS | DOI: 10.1038/s41467-018-07090-4

succeed. On a quantum device, the cost of estimating the gradient
scales as O(1/εα)36. For any number of measurements much lower
than 1/||g||α, where ||g|| is the norm of the gradient, a gradientbased optimization will result in a random walk. By concentration
of measure, a random walk will have exponentially small
probability of exiting the barren plateau. As a result, gradient
descent without some additional strategy cannot circumvent this
challenge on a quantum device in polynomial time.
Discussion
We have seen both analytically and numerically that for a wide
class of random quantum circuits, the expected values of observables concentrate to their averages over Hilbert space and gradients concentrate to zero. This represents an interesting
statement about the geometry of quantum circuits and landscapes
related to hybrid quantum–classical algorithms. More practically,
it means that randomly initialized circuits of sufﬁcient depth will
ﬁnd relatively little utility in hybrid quantum–classical
algorithms.
Historically, vanishing gradients may have played a role in the
early winter of deep neural networks32,34,47. However, multiple
techniques have been proposed to mitigate this problem24,35,48,49,
and the amount of training data and computational power
available has grown substantially. One approach to avoid these
landscapes in the quantum setting is to use structured initial
guesses, such as those adopted in quantum simulation. Another
possibility is to use pre-training segment by segment, which was
an early success in the classical setting48,50. These or other
alternatives must be studied if these ansatze are to be successful
beyond a few qubits.
Methods
We explicitly show the expectation value of the gradient is 0 and that under our
assumptions the variance decays exponentially in the number of qubits. By our
deﬁnition of RPQCs, we have that for any speciﬁed direction ∂kE, both U− and U+
are independently distributed and either U− or U+ match the Haar distribution up
to at least the second moment (they are a 2-design). The assumption of independence is equivalent to
R
R
pðUÞ ¼ dUþ pðUþ Þ dU pðU Þ
ð8Þ
´ δðUþ U  UÞ;

U+ is at least a 1-design,
n R  h
io
R
h∂k Ei ¼ i dU pðU ÞTr ρ dμ Uþ V; Uþy HUþ
R
¼ i TrH
dU pðU ÞTr ρ ½V; I 
N

ð13Þ

¼ 0:
An advantage of the explicit polynomial formulas are that they allow an analytic
calculation of the variance as well, which allows precise speciﬁcation of the coefﬁcient in Levy’s lemma. In cases where the integrals depend on up to two powers of
elements of U and U*, one may make use of the elementwise formula51
R

dμðUÞUi1 j1 Ui2 j2 Ui′ j′ Ui′ j′ ¼
1 1

δi i′ δi i′ δj j′ δj j′ þδi i′ δi i′ δj j′ δj j′
1 1

2 2

2 2

1 1

2 2

1 2

N 2 1

2 1

1 2

2 1

δi i′ δi i′ δj j′ δj j′ þδi i′ δi i′ δj j′ δj j′

:

ð14Þ

2 1
1 2 2 1 1 1 2 2
 1 1 2 2 1 2 NðN
2 1Þ

The variance of the gradient is deﬁned by
Var½∂k E ¼ hð∂k EÞ2 i;

ð15Þ

as we have seen above that 〈∂kE〉 = 0. Through use of the above formula for
integration up to the second moment of the Haar distribution, one may evaluate
this expression in 3 separate cases. For simplicity and relevance, we evaluate them
in the asymptotic case including only the dominant contribution as determined by
the inverse dimension.
In the case where U− is a 2-design but not U+,
Var½∂k E 



2Trðρ2 Þ
Trðρ2 Þ
Tr Hu2 V 2  ðHu VÞ2 U ¼  2n
Tr ½V; Hu 2 U ;
2
þ
þ
N 1
2 1

ð16Þ

where Hu ¼ uy Hu and we have deﬁned the notation hf ðuÞiUx to mean the average
over u sampled from p(Ux). In the case where U+ is a 2-design but not U−,

2 E
2TrðH 2 Þ
TrðH 2 Þ D
Var½∂k E  2
Tr ρ2u V 2  ðρu VÞ2 U ¼  2n
Tr V; ρu
; ð17Þ

U
N 1
2 1
where ρu ¼ uρuy . Finally in the case where both U+ and U− are 2-designs
     
1
Var½∂k E  ð3n1Þ Tr H 2 Tr ρ2 Tr V 2 :
2

ð18Þ

In all cases, the exponential decay of the gradient as a function of the number of
qubits is evident.

Data availability

Data used to generate the above ﬁgures are available upon request from the
authors.

Received: 23 May 2018 Accepted: 9 October 2018

which allows us to rewrite the expression as
Z
Z
h
i
h∂k Ei ¼ i dU pðU ÞTr ρ ´ dUþ pðUþ Þ V; Uþy HUþ :

ð9Þ

References
We will utilize explicit integration over the unitary group with respect to the
Haar measure, which up to the ﬁrst moment can be expressed as51
Z

y
¼
dμðUÞ Uij Ukm

Z


dμðUÞUij Umk
¼

δim δjk
N

;

ð10Þ

where N is the dimension of the space, typically 2n for n qubits. Using this
expression, one may readily verify that
Z
TrO
M ¼ dμðUÞUOU y ¼
I;
ð11Þ
N
which we use in the following. Now, making use of the assumption that either U+
or U− matches the Haar measure up to the ﬁrst moment (it is a 1-design), we ﬁrst
examine the case where U− is at least a 1-design and ﬁnd that
n
h R
io
R
h∂k Ei ¼ i dμðU ÞTr ρ ´ V; dUþ pðUþ ÞUþy HUþ
nh R
io
;
ð12Þ
¼ Ni Tr V; dUþ pðUþ ÞUþy HUþ
¼0
where we have deﬁned ρ ¼ U j0ih0jUy and used the fact that the trace of a
commutator of trace class operators is zero. In the second case, where we assume

1.

Preskill, J. Quantum computing in the NISQ era and beyond. Quantum 2, 79
(2018).
2. Peruzzo, A. et al. A variational eigenvalue solver on a photonic quantum
processor. Nat. Commun. 5, 1 (2014).
3. McClean, J. R., Romero, J., Babbush, R. & Aspuru-Guzik, A. The theory of
variational hybrid quantum-classical algorithms. New J. Phys. 18, 023023
(2016).
4. Yung, M.-H. et al. From transistor to trappedion computers for quantum
chemistry. Sci. Rep. 4, 9 (2014).
5. Farhi, E. Goldstone, J. & Gutmann, S. A quantum approximate optimization
algorithm. Preprint at https://arxiv.org/abs/1411.4028 (2014).
6. Johnson, P. D., Romero, J., Olson, J., Cao, Y. & Aspuru-Guzik, A. QVECTOR:
an algorithm for device-tailored quantum error correction. Preprint at https://
arxiv.org/abs/1711.02249 (2017).
7. Cao, Y., Giacomo Guerreschi, G. & Aspuru-Guzik, A. Quantum neuron: an
elementary building block for machine learning on quantum computers.
Preprint at https://arxiv.org/abs/1711.11240 (2017).
8. Hempel, C. et al. Quantum chemistry calculations on a trappedion quantum
simulator. Phys. Rev. X 8, 031022 (2018).
9. O’alley, P. J. J. et al. Scalable quantum simulation of molecular energies. Phys.
Rev. X 6, 31007 (2016).
10. McClean, J. R., Schwartz, M. E., Carter, J. & de Jong, W. A. Hybrid quantumclassical hierarchy for mitigation of decoherence and determination of excited
states. Phys. Rev. A. 95, 42308 (2017).

NATURE COMMUNICATIONS | (2018)9:4812 | DOI: 10.1038/s41467-018-07090-4 | www.nature.com/naturecommunications

5

ARTICLE

NATURE COMMUNICATIONS | DOI: 10.1038/s41467-018-07090-4

11. Wecker, D., Hastings, M. B. & Troyer, M. Progress towards practical quantum
variational algorithms. Phys. Rev. A 92, 42303 (2015).
12. Shen, Y. et al. Quantum implementation of unitary coupled cluster for
simulating molecular electronic structure. Phys. Rev. A 95, 020501(R)
(2017).
13. Kandala, A. et al. Hardware-efﬁcient quantum optimizer for small molecules
and quantum magnets. Nature 549, 242 (2017).
14. Colless, J. I. et al. Computation of molecular spectra on a quantum processor
with an error-resilient algorithm. Phys. Rev. X 8, 011021 (2018).
15. Santagati, R. et al. Witnessing eigenstates for quantum simulation of
hamiltonian spectra. Sci. Adv. 4, 1 (2018).
16. Dumitrescu, E. F. et al. Cloud quantum computing of an atomic nucleus. Phys.
Rev. Lett. 120, 210501 (2018).
17. Wecker, D., Hastings, M. B. & Troyer, M. Training a quantum optimizer.
Phys. Rev. A 94, 022309 (2016).
18. Wang, Z., Hadﬁeld, S., Jiang, Z. & Rieffel, E. G. Quantum approximate
optimization algorithm for maxcut: a fermionic view. Phys. Rev. A 97, 022304
(2018).
19. Moll, N. et al. Quantum optimization using variational algorithms on
nearterm quantum devices. Quantum Sci. Technol. 3, 030503 (2018).
20. Otterbach, J. S. et al. Unsupervised machine learning on a hybrid quantum
computer. Preprint at https://arxiv.org/abs/1712.05771v1 (2017).
21. Romero, J., Olson, J. P. & Aspuru-Guzik, A. Quantum autoencoders for
efﬁcient compression of quantum data. Quantum Sci. Technol. 2, 045001
(2017).
22. Biamonte, J. et al. Quantum machine learning. Nature 549, 195 (2017).
23. Farhi,E. & Neven, H. Classiﬁcation with quantum neural networks on near
term processors. Preprint at https://arxiv.org/abs/1802.06002 (2018).
24. LeCun, Y., Bengio, Y. & Hinton, G. Deep learning. Nature 521, 436 (2015).
25. McClean, J. R., Babbush, R., Love, P. J. & Aspuru-Guzik, A. Exploiting locality
in quantum computation for quantum chemistry. J. Phys. Chem. Lett. 5, 4368
(2014).
26. Romero, J. et al. Strategies for quantum computing molecular energies using
the unitary coupled cluster ansatz. Quant. Sci. Technol. 4, 1 (2018).
27. Babbush, R. et al. Low-depth quantum simulation of materials. Phys. Rev. X 8,
011044 (2018).
28. Rubin, N. C., Babbush, R. & McClean, J. Application of fermionic marginal
constraints to hybrid quantum algorithms. New J. Phys. 20, 053020 (2018).
29. Kivlichan, I. D. et al. Quantum simulation of electronic structure with linear
depth and connectivity. Phys. Rev. Lett. 120, 110501 (2018).
30. Farhi, E., Goldstone, J., Gutmann, S. & Neven, H. Quantum algorithms for
ﬁxed qubit architectures. Preprint at http://arxiv.org/abs/1703.06199 (2017).
31. Boixo, S. et al. Characterizing quantum supremacy in nearterm devices. Nat.
Phys. 14, 595 (2018).
32. Bradley, D. M. Learning in Modular Systems (Carnegie Mellon University,
Pittsburgh, 2010).
33. Glorot, X. & Bengio, Y. Understanding the difﬁculty of training deep
feedforward neural networks. In Proceedings of the Thirteenth International
Conference on Artiﬁcial Intelligence and Statistics, PMLR. AISTATS. (eds.)
Yee Whye Teh, Mike Titterington. 249–256 (2010)
34. Shalev-Shwartz, S., Shamir, O., & Shammah, S. Failures of gradient-based deep
learning. Preprint at https://arxiv.org/abs/1703.07950 (2017).
35. Ioffe S. & Szegedy, C. Batch normalization: accelerating deep network training
by reducing internal covariate shift. In Proceedings of the 32nd International
Conference on Machine Learning, PMLR. ICML. (eds.) Francis Bach, David
Blei. 448–456 (2015)
36. Knill, E., Ortiz, G. & Somma, R. D. Optimal quantum measurements of
expectation values of observables. Phys. Rev. A 75, 012328 (2007).
37. Popescu, S., Short, A. J. & Winter, A. Entanglement and the foundations of
statistical mechanics. Nat. Phys. 2, 754 (2006).
38. Bremner, M. J., Mora, C. & Winter, A. Are random pure states useful for
quantum computation? Phys. Rev. Lett. 102, 190502 (2009).
39. Gross, D., Flammia, S. T. & Eisert, J. Most quantum states are too entangled to
be useful as computational resources. Phys. Rev. Lett. 102, 190501 (2009).
40. Ledoux, M. The Concentration of Measure Phenomenon (American
Mathematical Society, Providence, 2005).
41. Guerreschi, G. G. & Smelyanskiy, M. Practical optimization for hybrid
quantum-classical algorithms. Preprint at https://arxiv.org/abs/1701.01450
(2017).

6

42. Renes, J. M., Blume-Kohout, R., Scott, A. J. & Caves, C. M. Symmetric
informationally complete quantum measurements. J. Math. Phys. 45, 2171
(2004).
43. Dankert, C., Cleve, R., Emerson, J. & Livine, E. Exact and approximate unitary
2-designs and their application to ﬁdelity estimation. Phys. Rev. A 80, 012304
(2009).
44. Harrow, A. W. & Low, R. A. Random quantum circuits are approximate 2designs. Commun. Math. Phys. 291, 257 (2009).
45. Ipsen, J. R. Products of independent Gaussian random matrices. Preprint at
https://arxiv.org/abs/1510.06128 (2015).
46. Roberts, D. A. & Yoshida, B. Chaos and complexity by design. J. High. Energy
Phys. 2017, 121 (2017).
47. Hochreiter, S., Bengio, Y., Frasconi, P. & Schmidhuber, J. Gradient ﬂow in
recurrent nets: the difﬁculty of learning long-term dependencies. A Field
Guide to Dynamical Recurrent Neural Networks, Chapter 14, (eds.) S. C.
Kremer and J. F. Kolen. (IEEE Press Piscataway, NJ 2001) https://www.
amazon.com/Field-Guide-Dynamical-Recurrent-Networks/dp/0780353692
48. Hinton, G. E., Osindero, S. & Teh, Y.-W. A fast learning algorithm for deep
belief nets. Neural Comput. 18, 1527 (2006).
49. He, K., Zhang, X., Ren, S. & J. Sun, J. Deep residual learning for image
recognition. In Proceedings of the IEEE conference on Computer Vision and
Pattern Recognition. (Eds.) Raman, B., Kumar, S., Roy, P.P., Sen, D., Las
Vegas, NV, United States, 770–778 (2016).
50. Bengio, Y., Lamblin, P., Popovici, D. & Larochelle, H. Greedy layer-wise
training of deep networks. Advances in Neural Information Processing
Systems 19 (NIPS'06). (eds.) B. Schölkopf, J. C. Platt, T. Hoffman. 53–160
(MIT Press, Canada 2007).
51. Puchałla, Z. & Miszczak, J. A. Symbolic integration with respect to the haar
measure on the unitary groups. Bull. Pol. Acad. Sci. Tech. Sci. 65, 21 (2017).

Acknowledgements
The authors thank Craig Gidney for helpful comments on the manuscript.

Author contributions
J.R.M., S.B., V.N.S, R.B., and H.N. contributed to the formulation of ideas, calculations,
and writing of the manuscript.

Additional information
Supplementary Information accompanies this paper at https://doi.org/10.1038/s41467018-07090-4.
Competing interests: The authors declare no competing interests.
Reprints and permission information is available online at http://npg.nature.com/
reprintsandpermissions/

Publisher’s note: Springer Nature remains neutral with regard to jurisdictional claims in
published maps and institutional afﬁliations.

Open Access This article is licensed under a Creative Commons
Attribution 4.0 International License, which permits use, sharing,
adaptation, distribution and reproduction in any medium or format, as long as you give
appropriate credit to the original author(s) and the source, provide a link to the Creative
Commons license, and indicate if changes were made. The images or other third party
material in this article are included in the article’s Creative Commons license, unless
indicated otherwise in a credit line to the material. If material is not included in the
article’s Creative Commons license and your intended use is not permitted by statutory
regulation or exceeds the permitted use, you will need to obtain permission directly from
the copyright holder. To view a copy of this license, visit http://creativecommons.org/
licenses/by/4.0/.
© The Author(s) 2018

NATURE COMMUNICATIONS | (2018)9:4812 | DOI: 10.1038/s41467-018-07090-4 | www.nature.com/naturecommunications

