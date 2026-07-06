Entanglement Induced Barren Plateaus
Carlos Ortiz Marrero,1 Mária Kieferová,2 and Nathan Wiebe3
Data Sciences and Analytics Group, Pacific Northwest National Laboratory, Richland, WA 99354 ∗
2
Centre for Quantum Computation and Communication Technology,
Centre for Quantum Software and Information, University of Technology Sydney, NSW 2007, Australia†
3
Department of Computer Science, University of Toronto, ON M5S 1A1, Canada‡
(Dated: March 11, 2021)

arXiv:2010.15968v2 [quant-ph] 10 Mar 2021

1

We argue that an excess in entanglement between the visible and hidden units in a Quantum
Neural Network can hinder learning. In particular, we show that quantum neural networks that
satisfy a volume-law in the entanglement entropy will give rise to models not suitable for learning
with high probability. Using arguments from quantum thermodynamics, we then show that this
volume law is typical and that there exists a barren plateau in the optimization landscape due to
entanglement. More precisely, we show that for any bounded objective function on the visible layers,
the Lipshitz constants of the expectation value of that objective function will scale inversely with the
dimension of the hidden-subsystem with high probability. We show how this can cause both gradient
descent and gradient-free methods to fail. We note that similar problems can happen with quantum
Boltzmann machines, although stronger assumptions on the coupling between the hidden/visible
subspaces are necessary. We highlight how pretraining such generative models may provide a way to
navigate these barren plateaus.

I.

INTRODUCTION

In recent years the prospects of quantum machine learning (QML) and quantum deep neural network have gained
notoriety in the scientific community. QML builds on the
success of traditional machine learning and the potential for quantum speedup. The QML field has enjoyed
increased attention for quantum algorithms for principal component analysis [1], support vector machines [2],
kernel methods [3, 4], and quantum neural networks
(QNN) [3, 5–8] but experiences setbacks in the form of
dequantization techniques [9–11].
A key part of a successful quantum machine learning
algorithm is an efficient training algorithm. In recent
years, several barren plateau results [12–16] put limitations on the gradient-based training of QNNs. Our result
complements the growing literature on barren plateaus
in quantum computing. McClean et al. [12] first showed
that unitary quantum neural networks generically suffer
from vanishing gradients exponentially in the number of
qubits. This issue stems from the concentration of measure [17, 18] and was subsequently demonstrated for other
QNNs [13, 14]. Another type of a barren plateau emerges
from hardware noise in the system [15]. The key observation that we put forward in this work is that barren
plateaus can occur because of an excess of entanglement
in deep quantum models.
In this paper, we prove that entanglement between
visible and hidden units hinders the learning process.
Inclusion of hidden units is essential in traditional machine
learning. Without them, the expressive power of neural
networks would be severely limited and deep learning

∗ carlos.ortizmarrero@pnnl.gov
† maria.kieferova@uts.edu.au
‡ nwiebe@cs.toronto.edu

all but impossible. In spite of this, there has been very
little attention paid to the effect of hidden units on the
training of QNNs. Surely, the expressive power of hidden
units would translate to the quantum world? Numerical
experiments seem to contradict this intuition. A small
scale numerical study [19] showed that the inclusion of
hidden units to quantum Boltzmann machines did not
lead to a higher quality of reproduction. While this could
be explained due to the small size of the QNN and simple
data, in our work we show that quantum Boltzmann
machines do not benefit from a large number of hidden
units.
We build intuition from exploring the statistical relationship between a random state and maximally entangled
states in a bipartite quantum system. A classic thermalization result [20] shows that for a random initial state,
the state on the visible units is with high probability
exponentially close to a maximally mixed state. However,
if the state is chosen from a k-design, its distance to a
maximally mixed state is bounded by a polynomial in
k [21]. We show that it is very difficult to escape from
this state because the gradients will be exponentially
small. As such, for a wide array of QNNs, randomness
and entanglement hinder the training.
This surplus of entanglement to some extent defeats
the purpose of deep learning by causing information to be
non-locally stored in the correlations between the layers
rather than in the layers themselves. As a result, when
one tries to remove the hidden units, as is customary in
deep learning, we find that the resulting state is close to
the maximally mixed state. Indeed, we show that such
situations are generic as well and that gradient descent
methods are unlikely to allow the user to escape from
such a plateau at low cost. This observation holds for
both "feedforward" QNNs as well as Boltzmann machines
and suggests that if quantum effects are to be used to
improve classical models then they must be used surgically.

2


























hidden














 ...











...

U (θ1 )
U (θ2 )

II.

...

U (θ3 )

...

U (θ4 )

...

U (θ6 )
U (θ5 )

THE IMPACT OF ENTANGLEMENT ON
DEEP MODELS

...

U (θ7 )

...

U (θ9 )
U (θ8 )

U (θ10 )

...
...
...
...



visible

U (θn−3 )
U (θn−1 )

...
...

U (θn−2 )

U (θn )

(a)
hidden

visible

(b)

FIG. 1. Examples of QNNs. (a) A quantum unitary network
characterized by a circuit with parameterized unitaries Uj =
e−iθj Hj where θj are the parameters we aim to learn and
Hj Hamiltonians that specify the QNN. The output is then
U (θ1 , . . . , θn ) |ψ0 i where |ψ0 i can be taken to be |0 . . . 0i for
generative learning. In this model, visible units correspond
to the qubits on which we evaluate the objective function,
in this case the last two registers. The remaining qubits
are called hidden units. (b) Quantum Boltzmann machines
defined on a graph. Each edge and each vertex correspond
to a weight on a local Hamiltonian corresponding to the pair
of qubits or a single qubit. The top layer of units (circles)
corresponds to visible units and the bottom layer (rectangles)
are hidden units.
QBMs models data as a thermal state
P
−
θi Hi
e−H(θ)
:= Tree− Pi i θi Hi . Without loss of generality, we will
Z(θ)
)
(
take Tr(H) = 0 for all quantum Boltzmann machines. The
aim when training a quantum Boltzmann machine is to learn
a vector θ such that for a training objective function given
by Oobj that acts on the visible subsystem, we maximize
Tr(Oobj Trh (e−H(θ) /Z(θ)).

Furthermore, our work establishes a link between the
thermalization literature and quantum machine learning
that has been hitherto absent from the literature.
We focus on two types of QNNs depicted in Figure 1,
feed-forward unitary quantum neural networks inspired
by QAOA, and Quantum Boltzmann machines [8, 19, 22].
Quantum Boltzmann machines can also be trained
generatively [19], meaning that rather than optimizing
a training objective function that is a linear function
of the density operator such as Tr(OObj Trh (e−H /Z)),
we aim to optimize a non-linear function of the density operator such as the quantum relative entropy, i.e.
S(ρtrain ||ρ(θ)) = Tr(ρtrain log(ρtrain )−ρtrain log(ρ(θ))), by
generating a quantum state ρ(θ) using the Boltzmann
machine that optimizes this divergence with the training
density operator.

The central question our work is to understand how
the entanglement in the neural network affects the visible units. Instead of providing speedup, entanglement
between visible and hidden units causes thermalization
on the visible subsystem. Thus, the inclusion of entanglement between the hidden and visible layers of a QNN
can be, unless carefully controlled, harmful to the neural
network model.
The relationship between the representational power of
a neural network and the degree of entanglement between
the visible and hidden systems was first discussed in [23];
however, here we re-examine this question and arrive at a
different conclusion. Specifically, we conclude that large
amounts of entanglement (as quantified by a volume law)
can be catastrophic for the model; whereas an area law
scaling for the entanglement entropy between the hidden
and visible can often be tolerated.
To see this, we need to make a few formal definitions.
Let S ⊂ CDv Dh ×Dv Dh be a family of parameterized density operators where Dv = 2nv is the dimension of the
nv -qubit visible subspace and Dh = 2nh the dimension
of the hidden subspace. For each ρ ∈ S, the qubits can
be uniquely assigned
to the vertices of a graph G on a
S
vertex set Vh Vv where Vv consists of log2 (Dv ) = nv
and Vh of log2 (Dh ) = nh qubits. We then will define
(j)
nv to be the number of vertices in Vv that are at least
graph distance j away from the vertices in Vh and define
(j)
nh to be the analogous number for the vertices in Vh .
We then say that S satisfies an area law if for all ρ ∈ S,
(1)
S(Trh (ρ)) ∈ Θ(nv ) similarly we say that S satisfies a
volume law if |S(Trh (ρ)) − log(Dv )| ∈ Θ(Dv /Dh ) where
S is the von Neumann entropy. With these definitions in
place we can concisely claim our result.
Proposition 1. Let S be a family of density operators
with visible dimension Dv and hidden dimension Dh ≥ Dv
(1)
(1)
with nv and nh qubits in the first visible and hidden
layers respectively. We then have that for any operator on
the visible sub-system Oobj and ρ ∈ S ⊂ CDv Dh ×Dv Dh ,
|Tr((Oobj ⊗ I)(ρ − I/(Dv Dh )))|

(1)

q


(1)
is in O kOObj k∞ log(Dv ) − nv
if S satisfies an area


p
law and is in O kOObj k∞ (Dv /Dh ) if S satisfies a
volume law.
Proof. The proof follows from standard inequalities for
the quantum relative entropy
1
kTrh (ρ) − I/Dv k21 ≤ S(Trh (ρ)||I/Dv )
2
= −S(Trh (ρ)) + log(Dv ).

(2)

3
much more common. This intuition can be made rigorous
by making appropriate assumptions about the interactions between the visible and hidden layers in the model.
In particular, we assume that the quantum states on the
joint system of the QNN approximate a Haar-random
state. In practice, this assumption is too strong as Haar
random states typically require exponentially long quantum circuits to generate them. Instead, we focus on
ensembles generated by unitary 2-designs, which model
the states generated by random sequences of universal
gates [25].

hidden

boundary
visible

FIG. 2. For an area law, the entanglement entropy scales as the
number of qubits on the boundary (in the dashed rectangle).

Then from the von-Neumann trace inequality we have
|Tr((OObj ⊗ I)(ρ − I/D))| ≤ kOObj k∞ kTrh (ρ) − I/Dv k1
p
≤ kOObj k∞ 2(log(Dv ) − S(Trh (ρ)))
(3)
(1)

If ρ satisfied an area-law scaling then S(Trh (ρ)) ∈ Θ(nv ).
From which the claimed result for the area law scaling
immediately follows. If instead we assume that ρ obeys
a volume-law then |S(Trh (ρ)) − log(Dv )| ∈ Θ(Dv /Dh ) =
Θ(2nv −nh )
This shows that if our quantum neural network outputs
states that satisfy a volume law then asymptotically the
predictions of the neural network would be no better than
random guessing. In contrast, quantum neural networks
will not necessarily observe this problem if the entanglement entropy is characteristic of an area-law scaling unless
the number of hidden units in the first layer becomes much
larger than the number of visible units. We, therefore, see
that uncontrolled entanglement, such as that yielded by
volume laws, can be catastrophic for deep quantum neural
networks (i.e. for Dh  Dv ) but the comparably limited
entanglement yielded by area laws may be more desirable.
This means that when designing neural networks, it is
vital to aim for sub-volume-law scaling. However, such
states often have concise representations using matrix
product states [24] and so might be no more performant
than classical neural networks. Nonetheless, we show
in III that such sub-volume law scalings are not typical
and that almost all quantum neural networks within the
ensembles we consider obey volume law scalings.
III.

TYPICALITY OF VOLUME-LAW SCALING

While area laws occur for certain systems, such as
ground states of gapped translationally invariant Hamiltonians on lattices, we expect volume law scalings to be

Proposition 2. Let U ∈ CDv Dh ×Dv Dh be drawn from a
unitary 2-design and let H = U † SU for some diagonal
matrix S ∈ CD×D . If either ρ = U |0ih0| U † (unitary
network) or ρ = e−H /Tr(e−H ) (Boltzmann machine) then
any bounded operator Oobj ∈ CDv ⊗Dv acting on the visible
subspace we have that,
!
r
Dv
|Tr ((Oobj ⊗ I)(ρ − I/D)))| ∈ O kOobj k∞
Dh
with high probability over U .
Proof. Let us first examine the case of ρ = U † |0ih0| U .
We then have that if we take the expectation value over
U drawn from a 2-design then
| E(Tr((Oobj ⊗ I)(U † |0ih0| U − I/D))|
≤ kOobj k∞ EkTrh (U † |0ih0| U − I/D)k1
q
≤ kOobj k∞ Dv EkTrh (U † |0ih0| U − I/D)k22

(4)

Since the partial trace of a density operator is a density
operator, it follows that the argument is positive definite
and in turn that the result can be written as
p
kOobj k∞ E(Tr((ρ − I/D) ⊗ (ρ − I/D))(Fvv0 ⊗ I), (5)

where Fvv0 is the flip or swap operator that swaps the
two visible subsystems.
Since the result is quadratic in the probability distribution we have from the definition of a unitary 2-design
that
E(Tr((ρ − I/D) ⊗ (ρ − I/D))
= EHaar (Tr((ρ − I/D) ⊗ (ρ − I/D))

(6)

where EHaar is the Haar expectation value. The result
then follows immediately from invoking Theorem 2 from
the result of Popescu et al [20] that
p
kOobj k∞ E(Tr((ρ − I/D) ⊗ (ρ − I/D))(Fvv0 ⊗ I)
!
r
Dv
∈ O kOobj k∞
.
(7)
Dh
Next let us assume that ρ = e−H /Tr(e−H ). We have
from the definition of H and the previous result that for

4
any eigenvector |ji of H
|Tr ((Oobj ⊗ I)(|jihj| − I/D)))| ∈ O kOobj k∞

A.

r

Dv
Dh

!

(8)
P
P
Since ρ = j |jihj| e−hj|H|ji /Tr(e−H ) := j EH (|jihj|)
the required result immediately follows by interchanging
the order of the expectation values over the mixed state
and over the unitary 2-design. These results also hold with
high probability as a consequence of Markov’s inequality.

This shows that for both the Boltzmann machine, as
well as unitary quantum networks, any observable measured on the visible layers will be indistinguishable, in
expectation, to the maximally mixed state with high probability. In other words, rather than strengthening the
analogous classical model the presence of entanglement
actually weakens them as the dimension of the hidden
subsystem grows relative to the visible subsystem. For
deep networks, we anticipate that there will be many more
hidden neurons than visible neurons and hence generically
entanglement is a bane not a boon for deep QNNs.
There are a number of caveats to this analysis. First,
we assume that the states in question are typical of a unitary 2-design. This assumption may not be appropriate
if a structured ansatz is used or if the used circuits are
shallow. The next assumption is that the observable is
supported on the visible system only. The final, potential,
caveat is that gradient-based optimizers may allow us to
train our way out of these typical points and thereby find
a way to productively leverage quantum effects. While the
first two caveats do speak to ways to escape this apparent no-go result, the ubiquity of “entanglement induced
barren plateaus” will make the third option fail with high
probability.

IV.

ENTANGLEMENT INDUCED BARREN
PLATEAUS

Our arguments for why gradient descent will fail to
improve the quality of a training objective function due
to entanglement between the visible and hidden layers
follows from similar reasoning to that employed in Proposition 2. However, the specific arguments require slightly
more nuanced assumptions since we need to worry about
how perturbations to the model parameters impact the
resulting state. Such assumptions are also made, for example, in the original McClean et al. work that identified
Barren plateaus for unitary networks [12]. Further, while
we were able to directly employ existing results from the
literature of thermalization to prove Proposition 2, the
necessary conditions do not hold for the gradients operator. We state the main results below and provide an
explicit proof in Appendices A and B

Plateaus for Unitary networks

We will first consider the case of unitary networks of
the form
U (θ1 , . . . , θn ) := e−iHn θn . . . e−iH1 θ1 .

(9)

We consider the case where one of the parameters is shifted
by a constant amount δk and argue about the maximum
possible shift in the expectation of an observable that is
supported only on the visible subsystem.
A major challenge to analyzing what happens when
shifting parameters of a unitary network is that such
networks are so complicated that the impact of this perturbation is difficult to measure. An example of such an
effect can be seen in the Loschmidt echo, which shows
exponential sensitivity to perturbations in the parameters of complex quantum dynamics [26, 27]. Our solution, similar to that taken in [12], is to assume that the
dynamics scrambles the states so much that almost all
Qk
subsequences of the product j=1 e−iHj θj form a unitary
2-design. This assumption is reasonable for a sufficiently
deep random circuit [28–30]. We then see that the value
of the objective function is Lipshitz continuous with a
constant that scales inversely with the hidden-dimension
Dh = 2nh . This shows that the plateau exists both for
gradient descent as well as gradient-free methods 1 . A
formal statement of this intuition and the result is given
below.
Theorem 3 (Gradient in unitary networks). Assume
that ρ(θ) is drawn from a unitary 2-design where ρ(θ) is
generated through a unitary ansatz of the form
ρ(θ) =

N
Y

j=1

e−iHj θj |0ih0|

1
Y

eiHj θj

j=N

that acts on a Hilbert space that is the product of a hidden
and visible space of dimensions Dh and Dv respectively.
Qk
Q1
Further, Hk (θ) = j=1 e−iHj θj Hk j=k eiHj θj for each
k obeys E(Hk (θ)ρ(θ)) = E(Hk (θ)) E(ρ(θ)). We then have
that
E(|Trv (Oobj Trh (ρ(θ)))|)
is a Lipshitz continuous function of θ with constant Λ
obeying
!
r
Dv
Λ ∈ O kOobj k∞ kHk k∞
.
Dh
The proof of the theorem follows by using the unitary
invariance of the trace norm and Hadamard’s lemma to

1 The work of McClean et al [12] can also be seen to implicitly

imply barren plateaus for gradient-free methods.

5
rewrite the difference between the perturbed exponential
and the original exponential as a commutator series of
Hk (θ) and ρ(θ). Then by using the triangle inequality, the
Cauchy-Schwarz inequality as well as the independence
assumptions made above to arrive at the result. An
explicit proof is given in Appendix A.
B.

Plateaus for Boltzmann Machines

Next, we will turn our attention to Boltzmann machines. We show that parameterized Hamiltonians drawn
from a unitary ensemble also experience an entanglement
induced barren plateau. The nature of this plateau, however, differs from that of the unitary network’s plateau in
that the plateau occurs under reasonable assumptions if
Tr(hh )2 /Tr(h2h ) ∈ o(Dh ) as we see below.
Theorem 4 (Gradient for Boltzmann machines). Assume
H ∈ CD×D is a random Hermitian matrix drawn from
an ensemble in the following manner: a diagonal matrix
with eigenvalues Ej ∈ R chosen according
to a probabilP
ity Pr(Ej ) such that maxk E( D12 ( j6=k (Ej − Ek )−1 )2 ) ∈
O(Γ2 ) and then is conjugated with a unitary drawn from a
distribution that is a unitary 2-design. Let us then define
for fixed Hermitian Hk ∈ CD×D that can be written for
Hermitian hv , hh as Hk = hv ⊗ hh and

the hidden layers reverting the model to a shallow one.
With these observations, the results then follow from the
use of standard inequalities and the Haar expectation
value of random states given, for example, in [31]. The
result holds with high probability as a consequence of the
Markov inequality.
In particular, we find that the gradient of the objective
function with respect to terms that non-trivially act on
the hidden layers are exponentially small in the number of hidden qubits since without loss of generality we
may take Tr(hh ) = 0 for all such terms. In contrast,
the gradient with respect to the visible Hamiltonian coefficients need not be exponentially small in the number
of hidden qubits. Indeed, if we have a k-local random
Hamiltonian where each Hamiltonian coefficient is chosen
independently from a distribution that is independent of
1−k
D then Γ ∈ O(log(D)
) thus for any k ≥ 2 the gradient
may only be polynomially small.
A side effect of these observations is that they explain,
in part, the observations in [19] that the number of hidden
units included in the model did not increase the performance of Quantum Boltzmann Machines. This can now
be understood from the fact that the Gibbs states for
typical Hamiltonians generate thermal states that are
close to the maximally mixed state. Thus, the inclusion
of hidden units typically will not be expected to increase
the performance of quantum Boltzmann machines.

ρ(θk ) := e−(H+θk Hk ) /Tr(e−(H+θHθ ) ).
Finally, let Oobj ∈ CDv ×Dv be a Hermitian matrix then

V.

HAAR RANDOM UNITARIES

In the previous sections, we assumed that the eigenbasis
the neural networks scramble at least as effectively as a
unitary 2-design. However, if we assume that in the case
is a differentiable function that obeys
of the unitary networks the gate sequence is Haar–random
s
! or in the case of the Boltzmann machine that the basis is

2
∂κ
Dv
Tr(hh )
+1
, Haar–random, then the type of concentration that we see
∈ O kOobj k∞ ΓkHk k∞
∂θk θk =0
Dh Dv Tr(h2h )
can be radically improved. Specifically, Levy’s lemma [20]
can be used in place of Markov’s inequality to show that
with high probability over the ensemble.
the vast majority of randomly selected networks will have
vanishing gradients. In particular,
The proof of Theorem 4 can be found in The Appendix B. The sketch of the proof is relatively simple.
Lemma 5 (Levy). Given a function f : Sd 7→ R defined
We use the assumption that the eigenvectors are taken
on the d-dimensional hypersphere Sd and a point φ ∈ Sd
to be columns of matrices drawn from a unitary 2-design
chosen uniformly at random,
and then use perturbation theory to argue about the per

turbed H. The use of perturbation theory introduces the
−C(d + 1)2
Prob[|f (φ) − E(f )| ≥ ] ≤ 2 exp
,
parameter Γ that characterizes the inverse minimal gap.
η2
We then take the partial trace of the resulting perturbed
eigenvectors to show that if the reduced density matrix
where η is the Lipshitz constant of f and C ∈ Θ(1).
over the hidden units of the perturbation Hamiltonian
Hk has zero trace then the partial trace over the hidden
This result ends up allowing us to use an even tighter
layers of each eigenvector remains the maximally mixed
concentration result for the systems than what is possible
state as per Proposition 2. This partial trace assumpusing Markov’s inequality because it shows that a large detion is needed because if bias terms were added to the
viation from the Haar expectation is exponentially small.
hidden units then one could disentangle them from the
This further means that a substantial deviation from the
visible units in the ground state through the perturbation.
results stated above is in fact exponentially smaller than
While such a perturbation may save the predictive power
what would be expected if we only had a 2-design condiof the Boltzmann machine, it would effectively eliminate
tion. If unitary k-designs are used in place of 2-designs
κ := Tr((Oobj ⊗ Ih )(ρ(θk )))

6
then it should be noted that it is possible to interpolate
between these two results [21], however, the bounds that
arise from using this result under the assumption that we
only have a 2-design is not superior to our Markov-based
analysis.

VI.

NUMERICAL RESULTS

We ran a series of numerical experiments summarized
in Figure 3 and 4 to demonstrate that our asymptotic
results apply to small-sized quantum networks.
We constructed our ansatz using the terms of a random
two-local Hamiltonian model on n-qubits. Let σaj =
I ⊗j−1 ⊗ σa ⊗ I ⊗n−j for a ∈ {x, y, z} and define
Ĥ =

XX
i

a

Jai σai +

XXX
i<j

a

i,j i j
Ja,b
σa σb

In Figure 3b, we generated a fixed thermal state e−Ĥ /Z
with onsite coefficients drawn from a normal distribution
with mean 0, variance 0.01, i.e. N (0, 0.01) and N (0, 1)
for the offsite coefficients. We then proceeded to estimate
the gradient vector of the Fidelity, F , between our model
and this fixed state using finite differences. We generated
1000 instances of our Unitary model by initializing all the
coefficients with samples from N (0, 1). The figure shows
a decrease in the variance ∞-norm of the gradient vector
on a semilog scale.
In Figure 3c, we estimated the gradient vector of the
trace distance, T , between our model and its perturbation for each parameter using finite differences. The
onsite coefficients where drawn from N (0, 0.01) and the
offsite coefficients from N (0, 1). Moreover, normalized
the Hamiltonian by its operator norm.

(10)

b

i,j
where we refer to Jai as the onsite coefficients and Ja,b
as the offsite coefficients of our model. For the Unitary
model, we exhaustively sampled from the individual terms
in equations (10) to construct the individual unitaries.
For the Boltzmann model, we used Ĥ as our Hamiltonian.
In Figure 3a and Figure 4, we compared the trace
distance scaling of the maximally mixed state and three
models: the gaussian unitary ensemble model, the unitary
QNN, and the Quantum Boltzmann Machine. In Figure
3a, we see that for an increasing number of hidden units
these models will produce states close to the maximally
mixed state. This result can be understood in the context
of Section III. Figure 4 highlights this effect on the data
histograms: as we increase the number of hidden units,
we see the trace distance concentrating around zero.
In Figure 3b, we performed a similar analysis on the
gradients of the unitary QNN. We observed an overall
decrease in ∞-norm of the gradient vector as we increasing
the size of the hidden units. We also calculated the
exponential rate of decay using least square fitting. This
overall decay is predicted in Theorem 3 as we increase
the number of hidden units.
The Boltzmann Machine results are summarized in
Figure 3c. In order to observe gradient decay in our
experiments, we need to amplify the effect of the offsite terms in relation to the onsite terms to encourage
a volume-law scaling. The emergence of these volume
laws can be understood from perturbation theory since
the leading order shift in an
P eigenvector |ni with eigenvalue En is proportional to j6=n |jihj| Hk |ni /(En − Ej ).
This shows that if we take |ni to be an eigenstate of the
1-body terms in the Hamiltonian then the entanglement
generated by Hk is suppressed by the energy gaps between
these states. We, therefore, choose these magnitudes to be
small so that significant entanglement can be introduced
in the eigenstates despite the small values of D that can
be explored on a classical computer. This phenomenon is
predicted in Theorem 4.

VII.

CONCLUSION

We showed that for Haar-random pure states and thermal states of random Hamiltonians, the gradient of an
observable objective function will be vanishing exponentially with the number of hidden units. This shows that
common types of QNNs are not only generically difficult
to train via local optimization methods but also that
adding hidden units will not always increase the power
of QNNs. Indeed, asymptotically we see that unless the
states generated satisfy an area law such hidden neurons
will likely be harmful.
One can prevent these entanglement induced barren
plateaus by violating any of the assumptions in our proofs.
The first is to choose an atypical initial state which has
been already explored in [32]. Next, one could try to
depart from the use of gradient-based optimization to
train such quantum models. However, it is unlikely that
without knowledge of the global properties of the training
objective function that such methods would succeed in
light of Proposition 2. Lastly, one can train models using
an objective function that does not correspond to an
observable and is independent of the density operator.
Of the three approaches, it is this last approach that we
advocate greater attention be paid to in quantum machine
learning. One tactic that can be used to circumvent our
pessimistic results is to begin a discriminative learning
task by first training generatively according to a quantity
such as the quantum relative entropy [8, 19] which is nonlinear in the quantum state ρ. We will show in subsequent
work that this quantum generative pre-training approach
can be used to successfully train both Boltzmann machines
and unitary networks and thereby mitigate some of the
challenges identified here for training deep QNNs.
As a final point, it is important to recognize that while
entanglement is a powerful tool to add to our models,
it must be used like a scalpel and not a sledgehammer.
Quantum properties such as entanglement may be harmful
if not surgically deployed and judicially used. Understanding the role that such quantum effects have on a model

7

(a)

(b)

(c)

FIG. 3. (a) Log-Log plot showing the of trace distance data in relation to the bound. The blue and orange marked values
1
correspond to the estimated maximum peak of the data histograms
p where Dv = 2 = 2. The green marked values correspond
to the bounds we obtain after substituting in E[T (ρ, I/D)] ≤ 1/2 Dv /Dh . (b-c) Semi-log plot highlighting the decay in the
variance of the ∞-norm of the gradient vector over an ensemble of initialized models. The dashed blue represents the average of
1000 model instances. The dash green line represents is the best fit obtained from least squares. (b) Gradient estimates for the
Unitary Model. (c) Gradient estimates for the normalized Quantum Boltzmann Machine.

(a) Real-Time Gaussian Unitary ensemble

(b) Unitary Model

(c) Normalized Boltzmann Machine

FIG. 4. Computed the trace distance between the reduce density of our models and the maximally mixed state for 1000 instances.
The models considered have only one visible unit i.e. Dv = 21 = 2. (a) Empirical trace distance distribution of a real-time
evolution (t = 10) of Hamiltonians drawn from the Gaussian Unitary Ensemble (GUE). (b) Empirical trace distance distribution
of the unitary model. All coefficients are drawn from a uniform distribution over [0, 1). (c) Empirical trace distance distribution
i,j
of the quantum Boltzmann machine. The on-set coefficients, Jai , are drawn N (0, 0.01). The off-set coefficients, Ja,b
, are drawn
from N (0, 1). Moreover, the Hamiltonian is normalized by its operator norm.

is very likely necessary [33] if we are to build quantum
models that can successfully leverage quantum effects.

ACKNOWLEDGMENTS

We thank Michael Bremner, Jarrod McClean and
Alessandro Rogero for helpful discussions and feedback.
Mária Kieferová acknowledges funding from ARC Centre
of Excellence for Quantum Computation and Communication Technology (CQC2T), project number CE170100012.

[1] Seth Lloyd, Masoud Mohseni, and Patrick Rebentrost.
Quantum principal component analysis. Nature Physics,

Support for C. Ortiz Marrero and Nathan Wiebe for
the numerical studies was provided by the Laboratory
Directed Research and Development Program at Pacific
Northwest National Laboratory, a multi-program national
laboratory operated by Battelle for the U.S. Department
of Energy, Release No. PNNL-SA-157287 and the theoretical work on this project by NW was supported by the U.S.
Department of Energy, Office of Science, National Quantum Information Science Research Centers, Co-Design
Center for Quantum Advantage under contract number
DE-SC0012704. Additional logistical support for Nathan
Wiebe was provided by the Google Research Award.

10(9):631–633, 2014.

8
[2] Patrick Rebentrost, Masoud Mohseni, and Seth Lloyd.
Quantum support vector machine for big data classification. Physical review letters, 113(13):130503, 2014.
[3] Maria Schuld and Nathan Killoran. Quantum machine
learning in feature hilbert spaces. Physical review letters,
122(4):040504, 2019.
[4] Vojtěch Havlíček, Antonio D Córcoles, Kristan Temme,
Aram W Harrow, Abhinav Kandala, Jerry M Chow, and
Jay M Gambetta. Supervised learning with quantumenhanced feature spaces. Nature, 567(7747):209–212,
2019.
[5] Maria Schuld, Ilya Sinayskiy, and Francesco Petruccione.
The quest for a quantum neural network. Quantum Information Processing, 13(11):2567–2586, 2014.
[6] Nathan Wiebe, Ashish Kapoor, and Krysta M Svore.
Quantum deep learning. Quantum Information & Computation, 16(7-8):541–587, 2016.
[7] Edward Farhi and Hartmut Neven. Classification with
quantum neural networks on near term processors. arXiv
preprint arXiv:1802.06002, 2018.
[8] Nathan Wiebe and Leonard Wossnig. Generative training
of quantum boltzmann machines with hidden units. arXiv
preprint arXiv:1905.09902, 2019.
[9] Ewin Tang. A quantum-inspired classical algorithm for
recommendation systems. In Proceedings of the 51st Annual ACM SIGACT Symposium on Theory of Computing,
pages 217–228, 2019.
[10] Ewin Tang. Quantum-inspired classical algorithms for
principal component analysis and supervised clustering.
arXiv preprint arXiv:1811.00414, 2018.
[11] András Gilyén, Seth Lloyd, and Ewin Tang. Quantuminspired low-rank stochastic regression with logarithmic dependence on the dimension. arXiv preprint
arXiv:1811.04909, 2018.
[12] Jarrod R McClean, Sergio Boixo, Vadim N Smelyanskiy,
Ryan Babbush, and Hartmut Neven. Barren plateaus
in quantum neural network training landscapes. Nature
communications, 9(1):1–6, 2018.
[13] M Cerezo, Akira Sone, Tyler Volkoff, Lukasz Cincio, and
Patrick J Coles. Cost-function-dependent barren plateaus
in shallow quantum neural networks. arXiv preprint
arXiv:2001.00550, 2020.
[14] Kunal Sharma, M Cerezo, Lukasz Cincio, and Patrick J
Coles. Trainability of dissipative perceptron-based quantum neural networks. arXiv preprint arXiv:2005.12458,
2020.
[15] Samson Wang, Enrico Fontana, M Cerezo, Kunal Sharma,
Akira Sone, Lukasz Cincio, and Patrick J Coles. Noiseinduced barren plateaus in variational quantum algorithms. arXiv preprint arXiv:2007.14384, 2020.
[16] Zoë Holmes, Andrew Arrasmith, Bin Yan, Patrick J Coles,
Andreas Albrecht, and Andrew T Sornborger. Barren
plateaus preclude learning scramblers. arXiv preprint
arXiv:2009.14808, 2020.
[17] Michael J. Bremner, Caterina Mora, and Andreas Winter.
Are random pure states useful for quantum computation?

Phys. Rev. Lett., 102:190502, May 2009.
[18] D. Gross, S. T. Flammia, and J. Eisert. Most quantum
states are too entangled to be useful as computational
resources. Phys. Rev. Lett., 102:190501, May 2009.
[19] Mária Kieferová and Nathan Wiebe. Tomography and
generative training with quantum boltzmann machines.
Physical Review A, 96(6):062327, 2017.
[20] Sandu Popescu, Anthony J Short, and Andreas Winter.
Entanglement and the foundations of statistical mechanics.
Nature Physics, 2(11):754–758, 2006.
[21] Richard A Low. Large deviation bounds for k-designs.
Proceedings of the Royal Society A: Mathematical, Physical and Engineering Sciences, 465(2111):3289–3308, 2009.
[22] Mohammad H Amin, Evgeny Andriyash, Jason Rolfe,
Bohdan Kulchytskyy, and Roger Melko. Quantum boltzmann machine. Physical Review X, 8(2):021050, 2018.
[23] Sankar Das Sarma, Dong-Ling Deng, and Lu-Ming Duan.
Machine learning meets quantum physics. arXiv preprint
arXiv:1903.03516, 2019.
[24] Jens Eisert, Marcus Cramer, and Martin B Plenio. Colloquium: Area laws for the entanglement entropy. Reviews
of Modern Physics, 82(1):277, 2010.
[25] Aram W Harrow and Richard A Low. Random quantum
circuits are approximate 2-designs. Communications in
Mathematical Physics, 291(1):257–302, 2009.
[26] Fritz Haake. Quantum signatures of chaos. In Quantum Coherence in Mesoscopic Systems, pages 583–595.
Springer, 1991.
[27] Bin Yan, Lukasz Cincio, and Wojciech H Zurek. Information scrambling and loschmidt echo. Physical Review
Letters, 124(16):160603, 2020.
[28] Richard Cleve, Debbie Leung, Li Liu, and Chunhao Wang.
Near-linear constructions of exact unitary 2-designs. arXiv
preprint arXiv:1501.04592, 2015.
[29] Jonas Haferkamp, Dominik Hangleiter, Adam Bouland,
Bill Fefferman, Jens Eisert, and Juani Bermejo-Vega.
Closing gaps of a quantum advantage with short-time
hamiltonian dynamics. arXiv preprint arXiv:1908.08069,
2019.
[30] Aram Harrow and Saeed Mehraban. Approximate unitary t-designs by short random quantum circuits using
nearest-neighbor and long-range gates. arXiv preprint
arXiv:1809.06957, 2018.
[31] Ryan Babbush, Jarrod McClean, Dave Wecker, Alán
Aspuru-Guzik, and Nathan Wiebe. Chemical basis of
trotter-suzuki errors in quantum chemistry simulation.
Physical Review A, 91(2):022311, 2015.
[32] Edward Grant, Leonard Wossnig, Mateusz Ostaszewski,
and Marcello Benedetti. An initialization strategy for
addressing barren plateaus in parametrized quantum circuits. Quantum, 3:214, 2019.
[33] Nathan Wiebe. Key questions for the quantum machine learner to ask themselves. New Journal of Physics,
22(9):091001, 2020.

Appendix A: Proof of Unitary Network Gradient

Here we provided a complete proof of Theorem 3.
Theorem 3 (Gradient in unitary networks). Assume that ρ(θ) is drawn from a unitary 2-design where ρ(θ) is generated

9
through a unitary ansatz of the form
ρ(θ) =

N
Y

e−iHj θj |0ih0|

j=1

1
Y

eiHj θj

j=N

that acts on a Hilbert space that is the product of a hidden and visible space of dimensions Dh and Dv respectively.
Qk
Q1
Further, Hk (θ) = j=1 e−iHj θj Hk j=k eiHj θj for each k obeys E(Hk (θ)ρ(θ)) = E(Hk (θ)) E(ρ(θ)). We then have that
E(|Trv (Oobj Trh (ρ(θ)))|)

is a Lipshitz continuous function of θ with constant Λ obeying
Λ ∈ O kOobj k∞ kHk k∞

r

Dv
Dh

!

.

Proof. First using the definition that


ρ(θ + δk ) := 

k
Y

e−iHj θj e−iHk δk

j=1

Y

j>k





e−iHj θj  ρ0 × 

k
Y

e−iHj θj e−iHk δk

j=1

Y

j>k

†

e−iHj θj 

(A1)

we then wish to analyze the distribution over θ of |Trv (Oobj Trh (ρ(θ) − ρ(θ + δk )))| , under the assumption that the
unitaries satisfy a 2-design condition.
Using Hadamard’s Lemma we can express the distance between the difference between the expectation values is








Trv Oobj Trh ρ(θ) − 

k
Y

j=1

e−iHj θj e−iHk |δk |

1
Y

j=k





eiHj θj  ρ(θ) 

k
Y

e−iHj θj e−iHk |δk |

j=1





:= Trv Oobj Trh ρ(θ) − e−iHk (θ)|δk | ρ(θ)eiHk (θ)|δk |
= Trv

1
Y

j=k

Oobj

† 

eiHj θj  

q
∞ Tr (Adq
X
h
−iHk (θ) (ρ(θ)))|δk |
q=1

q!

!

(A2)

Next, making the assumption that Hk (θ) and ρ(θ) are uncorrelated we can further simplify this result. Our exposition
will now follow that of Popescu, Short and Winter [20]; which we modify to deal with to show that a concentration of
measure exists for the commutators of Hk (θ) and ρ(θ).
We will now work under the assumption that the expectation values are independent. We further denote the
expectation value over the Hamiltonian as EH and the expectation value over the state as Eφ . If this independence
assumption holds then we need to argue about the magnitude of terms of the form Eφ (Trv (Trh (Hk (θ)ρ(θ))2 )). We can
estimate this by introducing two copies of the quantum state and linking both terms through the use of a flip operator
Fvv0 such that
X
Fvv0 =
|v 0 ihv| ⊗ |vihv 0 | .
(A3)
vv 0

In the following, we will use this notation primed indices to refer to the visible and hidden subsystems of the first and
second copies respectively.
The commutators in general consist of many different products of Hk and the state operator. Below we argue about
their form in generality. Let us assume that p1 , p2 , q1 , q2 are positive integers. We then wish to compute the product
of traces of of the form Trh (Hk (θ)p1 ρHk (θ)p2 Trh (Hk (θ)q1 ρHk (θ)q2 ). By applying the flip operator and taking the
quantum state ρ(θ) to be |φihφ|
Eφ (Trh (Hk (θ)p1 )ρHk (θ)p2 Trh (Hk (θ)q1 ρHk (θ)q2 ))
= Trvv0 (Eφ ((Trh (Hkp1 (θ)ρ(θ)Hkp2 (θ)) ⊗ Trh (Hkq1 (θ)ρ(θ)Hkq2 (θ)))Fvv0 ))
= Trvv0 Trhh0 (Eφ ((Trh (Hkp1 (θ)ρ(θ)Hkp2 (θ)) ⊗ Trh (Hkq1 (θ)ρ(θ)Hkq2 (θ)))(Fvv0 ⊗ I)))
= Tr(Eφ ((|φihφ| ⊗ |φihφ|)(Hkp1 (θ) ⊗ Hkq1 (θ))(Fvv0 ⊗ I)(Hkp2 (θ) ⊗ Hkq2 (θ)))).

(A4)

10
The next step in this is to recognize that the above tensor products if |φihφ| are a symmetric quantum state.
Therefore if we express the state as the sum of its anti-symmetric component and its symmetric component then the
anti-symmetric component must be zero [20]. We then see from the fact that ρ(θ) is assumed to be drawn from a
unitary 2-design that the expectation value is unitarily invariant and we can then follow the arguments laid out in [20]
that
Eφ (Trh (Hk (θ)p1 )ρHk (θ)p2 Trh (Hk (θ)q1 ρHk (θ)q2 ))
 sym 
2D2
Π
=
(Hkp1 (θ) ⊗ Hkq1 (θ))
Tr Eφ
D(D + 1)
D2
!!
× (Fvv0 ⊗ I)(Hkp2 (θ) ⊗ Hkq2 (θ))

(A5)

Next, if we define the flip operator on the dilated space including the hidden and visible units to be Frr0 = Fvv0 ⊗ Fhh0
then we can express Πsym = 21 (I + Frr0 ). Finally using the properties of the flip operator we find that we can write
Trv (Eφ (Trh (Hk (θ)p1 )ρHk (θ)p2 Trh (Hk (θ)q1 ρHk (θ)q2 )))
 p1

(Hk (θ) ⊗ Hkq1 (θ))(Fvv0 ⊗ I)(Hkp2 (θ) ⊗ Hkq2 (θ))
D2
=
Tr
D(D + 1)
D2


p
(Fvv0 ⊗ Fhh0 )(Hk 1 (θ) ⊗ Hkq1 (θ))(Fvv0 ⊗ I)(Hkp2 (θ) ⊗ Hkq2 (θ))
D2
Tr
+
D(D + 1)
D2


p
q
p
(Hk 1 (θ) ⊗ Hk1 (θ))(Fvv0 ⊗ I)(Hk 2 (θ) ⊗ Hkq2 (θ))
D2
=
Tr
D(D + 1)
D2


q
p
(Hk1 (θ) ⊗ Hk 1 (θ))(I ⊗ Fhh0 )(Hkp2 (θ) ⊗ Hkq2 (θ))
D2
+
Tr
D(D + 1)
D2
!
!
(Fvv0 ⊗ I)(Hkp1 +p2 (θ) ⊗ Hkq1 +q2 (θ))
(I ⊗ Fhh0 )(Hkq1 +p2 (θ) ⊗ Hkp1 +q2 (θ))
D2
D2
=
Tr
+
Tr
D(D + 1)
D2
D(D + 1)
D2
!
!
Trh (Hkp1 +p2 (θ))Trh (Hkq1 +q2 (θ))
Trv (Hkq1 +p2 (θ))Trv (Hkp1 +q2 (θ))
D2
D2
=
Trv
+
Trh
D(D + 1)
D2
D(D + 1)
D2
(A6)
We, therefore, have from the triangle inequality that
!
p1 +p2
q1 +q2
2
Tr
(H
(θ))Tr
(H
(θ))
D
h
h
k
k
Trv (Eφ (Trh (Hk (θ)p1 )ρHk (θ)p2 Trh (Hk (θ)q1 ρHk (θ)q2 ))) −
Trv
D(D + 1)
D2
!
p1 +p2 +q1 +q2
Trv (Hkq1 +p2 (θ))Trv (Hkp1 +q2 (θ))
Tr(|Hkq1 +q2 (θ)|)kTrv (Hk (θ)q1 +q2 )k∞
kHk k∞
. (A7)
≤ Trh
≤
≤
D2
D2
Dh
Here the last inequality follows from the fact that the Schatten infinity-norm is unitarily invariant and thus
kHk (θ)k∞ = kHk k∞ .
Next let us consider the expectation value for one of the terms in the expansion
E(kTrh (Adq−iHk (θ) (ρ(θ)))k1 )
p
≤ E( Dv kTrh (Adq−iHk (θ) (ρ(θ)))k2 )
q
≤ Dv E(kTrh (AdqHk (θ) (ρ(θ)))k22 )

(A8)

Every term in AdqHk (θ) (ρ(θ)) consists of q Hk (θ) and further 2q−1 terms have positive coefficient and 2q−1 terms
have negative coefficient. The proof of this fact is inductive. For q = 1,
AdHk (θ) (ρ(θ)) = Hk (θ)ρ(θ) − ρ(θ)Hk (θ),

(A9)

11
which demonstrates the base case of q = 1. Now assume that the claim is valid for q = p we then have that
p
p
Adp+1
Hk (θ) (ρ(θ)) = Hk (θ)AdHk (θ) (ρ(θ)) − AdHk (θ) (ρ(θ))Hk (θ)

(A10)

The induction step immediately follows from this observation and it is clear that the claim is valid for all q.
Now if we expand (Trh (AdqHk (θ) (ρ(θ))))2 using the linearity of the partial-trace operation we find that each term is
of the form Trh (Hkp1 (θ)ρ(θ)Hkp2 (θ))Trh (Hkq1 (θ)ρ(θ)Hkq2 (θ))where p1 + p2 = q = q1 + q2 . The expression in (A7) then
2

D
shows us that we can replace each term with D(D+1)
Trv

(Trh (Hkq (θ)))2
D2
q−1

while incurring a small error. Importantly,

this value is independent of p1 , p2 , q1 , q2 . Thus since there are 2
such terms with negative coefficient and 2q−1
with positive coefficient for each of the partial traces there are similarly 22q−1 terms with negative coefficient in the
expansion and 22q−1 with positive coefficient. Ergo, the sums over all such terms present in the adjoint is zero up to
the small error terms given in (A7). Thus we have that,
r
q
Dv
q
q
2
Dv E(kTrh (AdHk (θ) (ρ(θ))k2 ) ≤ (2kHk k∞ )
(A11)
Dh
Next from (A10) we have that

E Trv

Oobj

q
∞ Tr (Adq
X
h
−iHk (θ) (ρ(θ)))|δk |

q!

q=1

≤ kOObj k∞

∞
X

E

!

Trh (Adq−iHk (θ) (ρ(θ)))|δk |q

!

q!
1
v

u
∞ u
X
Trh (Adq−iHk (θ) (ρ(θ)))|δk |q
u

tDv E
≤ kOObj k∞
q!
q=1
q=1

r

Dv
≤ |δk |kOobj k∞ kHk k∞ e2kHk k∞ |δk |
,
Dh
!
r
Dv
∈ O |δk |kOObj k∞ kHk k∞
Dh

2

2




(A12)

where we have used the assumption that kHk k∞ |δk | ∈ O(1). From this our claim about the Lipshitz constant
immediately follows from the definition of Lipshitz continuity and from (A2).
Appendix B: Proof of Quantum Boltzmann Machine Gradient

Here we provide a complete proof for the gradient of a quantum Boltzmann machine. We can always assume that
the Hamiltonian is traceless. Indeed, for any Hamiltonian H 0 with a non-zero trace, we can introduce a Hamiltonian
H = H 0 − α1 such that Tr(H) = 0 and H leads to the same thermal state
0

ρthermal =

0

0

e−Ht
e−H t+α1t
eαt e−H t
e−H t
=
=
=
.
0
0
Tr(e−Ht )
Tr(e−H t+α1t )
eαt Tr(e−H t )
Tr(e−H 0 t )

(B1)

Theorem 4 (Gradient for Boltzmann machines). Assume H ∈ CD×D is a random Hermitian matrix drawn from an
ensemble in the following
P manner: a diagonal matrix with eigenvalues Ej ∈ R chosen according to a probability Pr(Ej )
such that maxk E( D12 ( j6=k (Ej − Ek )−1 )2 ) ∈ O(Γ2 ) and then is conjugated with a unitary drawn from a distribution
that is a unitary 2-design. Let us then define for fixed Hermitian Hk ∈ CD×D that can be written for Hermitian hv , hh
as Hk = hv ⊗ hh and
ρ(θk ) := e−(H+θk Hk ) /Tr(e−(H+θHθ ) ).
Finally, let Oobj ∈ CDv ×Dv be a Hermitian matrix then
κ := Tr((Oobj ⊗ Ih )(ρ(θk )))

12
is a differentiable function that obeys
∂κ
∈ O kOobj k∞ ΓkHk k∞
∂θk θk =0

s

Dv
Dh



Tr(hh )2
+1
Dv Tr(h2h )

!

,

with high probability over the ensemble.
Proof. First note that if we begin with an observable Oobj acting on the visible subspace then the difference between
the observable for ρ(θ) = e−(H+θk Hk ) /Z(θk ) and ρ(0) := ρ
E(|Tr((Oobj ⊗ Ih )ρ(θk )) − Tr((Oobj ⊗ Ih )ρ)|) ≤ kOObj k∞ E(kTrh (ρ(θk ) − ρ)k1 )
q
≤ kOObj k∞ Dv E(kTrh (ρ(θk ) − ρ)k22 ).

(B2)

Therefore just like the unitary network case, we will now focus our attention to bounding the expectation value of
the difference between the density operators. The main difference here is that the density operators are defined via
imaginary time-evolution rather than real time.
From Taylor’s theorem, we have that if the Hamiltonian H + sHk has no level crossings on the interval s ∈ [0, θk ]
then to order O(θk2 ) the eigenvectors of H + θk Hk can be identified using perturbation theory. In particular, for
any p ∈ {0, . . . , D − 1} let |pi be an eigenvector of H with eigenvalue Ep then the eigenvector |n0 i of H + θk that
corresponds to the eigenvector |ni of H can be expressed as
|n0 i = |ni + θk

X |ji hj| Hk |ni

j6=n

En − Ej

+ O(θk2 )

(B3)

This implies that


Trh (|n0 ihn0 | − |nihn|) = Trh θk

X |ji hj| Hk |nihn|

j6=n

En − Ej

+



|nihn| Hk |jihj| 
+ O(θk2 )
En − Ej

(B4)

P
(`)
(`)
Next let us write for any ` ∈ {0, . . . , D − 1} the eigenvector |`i = pq αpq |pqi, where αpq is a complex number and
|pqi := |piv ⊗ |qih for some appropriate basis for the visible and hidden subsystems. The expectation value over the
state vectors can then be thought of as an average of these coefficients.
There are many choices that can be made for the eigenbasis that we further exploit the fact that Hk := hv ⊗ hh to
choose the bases of the visible and hidden subsystems to diagonialze hv and hh . Thus we can state hv ⊗hh |pqi := λpq |pqi
for λpq ∈ R.
With these choices in place we can write


!
(j) ∗(j) (n) ∗(n)
X |ji hj| Hk |nihn|
X
X αpq
α
α
α
vw
rs
tu
=
Trh 
Trh
|pqihrs| Hk |tuihvw|
En − Ej
En − Ej
pqrstuvw
j6=n
j6=n
!
(j) ∗(j) (n) ∗(n)
X
X αpq
αrs αrs αvw λrs
|pqihvw|
=
Trh
En − Ej
pqrsvw
j6=n
!
(j) ∗(j) (n) ∗(n)
X X αpq
αrs αrs αvq λrs
=
|pihv|
(B5)
En − Ej
pqrsv
j6=n



Trh (|n0 ihn0 | − |nihn|)2 = 
=

X

j,j 0 6=n

X

j6=n

(j) ∗(j) (n) ∗(n)
(n) ∗(n) (j) ∗(j)
X (αpq
αrs αrs αvq + αpq αrs αrs αvq )λrs

pqrsv

En − Ej

!2

|pihv|  + O(θk4 )

(j) ∗(j) (n) ∗(n)
(n) ∗(n) (j) ∗(j)
(j) ∗(j) (n) ∗(n)
(n) ∗(n) (j) ∗(j)
X (αpq
αrs αrs αvq + αpq αrs αrs αvq )(αvq0 αr0 s0 αr0 s0 αv0 q0 + αvq0 αr0 s0 αr0 s0 αv0 q0 )λrs λr0 s0

pqrsv
q 0 r 0 s0 v 0

(En − Ej )(En − Ej 0 )

|pihv 0 | + O(θk4 )
(B6)

13
There are a total of 8 terms that arise when we expand the above products. Let us consider the first case which
emerges in the expectation value of the trace of the previous result. Here we will invoke the fact that the eigenvectors
are sampled from a unitary 2-design, which means that any quantity that is at most quadratic in the probability will
have an expectation value that coincides with the Haar average. A final point to note, is that as a consequence of
unitary invariance and the discussion contained in [31, Appendix A], the expectation value of the product of any two
terms is zero unless all of their indices match. Further, up to relative errors that are O(1/D), the expectation values of
the coefficients are independent of each other. This implies that if Tr(hh ) = 0 then


(j) ∗(j) (n) ∗(n) (j) ∗(j) (n) ∗(n)
X
X
0
0
α
α
α
α
α
α
α
α
λ
λ
pq rs
rs vq
rs r s 

vq 0 r 0 s0 r 0 s0 pq 0
E

0)
(E
−
E
)(E
−
E
n
j
n
j
0
pqrsv
j,j 6=n

q 0 r 0 s0 v 0

0

(j) 2
(n)
(j )
(n)
X X E(|αpq
| ) E(|αpq |2 ) E(|αpq0 |2 ) E(|αpq0 |2 )λpq λpq0

=O

(En − Ej )(En − Ej 0 )

j,j 0 6=n pqq 0

0

(j) 2
(n)
(n)
(j )
X X E(|αpq
| ) E(|αpq |2 ) E(|αvq |2 ) E(|αpq |2 )λ2pq

+

(En − Ej )(En − Ej 0 )

j,j 0 6=n pqv

+

(En − Ej )(En − Ej 0 )
!2

j,j 0 6=n pq

1
=O
D4
1
=O
D4
=O

0

(n) 4
(j)
(j )
X X E(|αpq
| ) E(|αpq |2 ) E(|αpq |2 )λ2pq

Dv
D3

X

1
En − Ej

X

1
En − Ej

j6=n

!!

!!

(Tr(h2v )(Tr(hh ))2 + (Dv + 1)Tr(Hk2 )

!2

!

!

!

Tr(hh )2
2
+ Dv Tr(Hk )
Tr(h2h )
j6=n
!2 
!

X
Tr(hh )2
1
2
+ 1 kHk k∞
En − Ej
Dv Tr(h2h )


(B7)

j6=n

Now under the assumption that


E

X

j6=n

1
En − Ej

!2 


 ∈ O Γ2 D 2 ,

it follows that this term is asymptotically bounded above by O(Γ2 kHk k2∞ /Dh ). It is straight forward to verify that
the same bound holds for all remaining 4 products in the expansion.
It then follows from (B2) and (B7) that
E(|Tr((Oobj ⊗ Ih )ρ(θk )) − Tr((Oobj ⊗ Ih )ρ)|)
θk
s

!
Dv
Tr(hh )2
∈ O kOobj k∞ ΓkHk k∞
+1
Dh Dv Tr(h2h )

|∂θk (E(|Tr((Oobj ⊗ Ih )ρ(θk ))))| = lim

θk →0

(B8)

The claim that this bound on the derivative holds with high probability over the ensemble is then a direct consequence
of Markov’s inequality.

