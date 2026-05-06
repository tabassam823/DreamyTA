PHYSICAL REVIEW A 98, 032309 (2018)

Quantum circuit learning
K. Mitarai,1,* M. Negoro,1,2 M. Kitagawa,1,3 and K. Fujii2,4,†
1

Graduate School of Engineering Science, Osaka University, 1-3 Machikaneyama, Toyonaka, Osaka 560-8531, Japan
2
JST, PRESTO, 4-1-8 Honcho, Kawaguchi, Saitama 332-0012, Japan
3
Quantum Information and Quantum Biology Division, Institute for Open and Transdisciplinary Research Initiatives, Osaka University,
Osaka 560-8531, Japan
4
Graduate School of Science, Kyoto University, Yoshida-Ushinomiya-cho, Sakyo-ku, Kyoto 606-8302, Japan
(Received 12 January 2018; published 10 September 2018)
We propose a classical-quantum hybrid algorithm for machine learning on near-term quantum processors,
which we call quantum circuit learning. A quantum circuit driven by our framework learns a given task by
tuning parameters implemented on it. The iterative optimization of the parameters allows us to circumvent the
high-depth circuit. Theoretical investigation shows that a quantum circuit can approximate nonlinear functions,
which is further confirmed by numerical simulations. Hybridizing a low-depth quantum circuit and a classical
computer for machine learning, the proposed framework paves the way toward applications of near-term quantum
devices for quantum machine learning.
DOI: 10.1103/PhysRevA.98.032309
I. INTRODUCTION

In recent years, machine learning has acquired much attention in a wide range of areas including the field of quantum
physics [1–5]. Since quantum information processing is expected to bring us exponential speedups on some problems
[6,7], the usual machine learning tasks might be improved
when carried out on a quantum computer. Also, for the
purpose of learning a complex quantum system, it is natural
to utilize a quantum system as our computational resource. A
variety of machine learning algorithms for quantum computers have been proposed [8–11], since the Harrow-HassidimLloyd (HHL) algorithm [12] enabled us to perform basic
matrix operations on a quantum computer. These HHL-based
algorithms have the quantum phase estimation algorithm [7]
at their heart, which requires a high-depth quantum circuit.
To circumvent a high-depth quantum circuit, which is still a
long-term goal on the hardware side, classical-quantum hybrid algorithms consisting of a relatively low-depth quantum
circuit such as the quantum variational eigensolver [13,14]
(QVE) and quantum approximate optimization algorithm [15–
17] (QAOA) have been suggested. In these methods, a problem is encoded in an Hermitian matrix A. Its expectation
value A with respect to an ansatz state |ψ (θ ) is iteratively
optimized by tuning the parameter θ. The central idea of
hybrid algorithms is dividing the problem into two parts, each
of which can be performed easily on a classical and a quantum
computer.
In this paper, we present a new hybrid framework, which
we call quantum circuit learning (QCL), for machine learning
with a low-depth quantum circuit. In QCL, we provide input
data to a quantum circuit and iteratively tune the circuit parameters so that the optimized circuit gives the desired output.

*
†

mitarai@qc.ee.es.osaka-u.ac.jp
fujii.keisuke.2s@kyoto-u.ac.jp

2469-9926/2018/98(3)/032309(6)

A gradient-based systematic optimization of parameters is
introduced for the tuning just like the backpropagation method
[18] utilized in feedforward neural networks. We theoretically
show that a quantum circuit driven by the QCL framework
can approximate any analytical function, if the circuit has a
sufficient number of qubits. The ability of the QCL framework
to learn nonlinear functions and perform a simple classification task is demonstrated by numerical simulations. Also,
we show by simulation that a six-qubit circuit is capable of
fitting the dynamics of 3 spins of a 10-spin system with a fully
connected Ising Hamiltonian. We stress here that the proposed
framework is easily realizable on near-term devices.

II. QUANTUM CIRCUIT LEARNING
A. Algorithm

Our QCL framework aims to perform supervised or unsupervised learning tasks [18]. In supervised learning, an
algorithm is provided with a set of input {x i } and corresponding teacher data {f (x i )}. The algorithm learns to output
yi = y(x i , θ ) that is close to the teacher f (x i ), by tuning
θ . The output and the teacher can be vector-valued. QCL
assigns the calculation of the output yi to a quantum circuit
and the update of the parameter θ to a classical computer. The
objective of learning is to minimize a cost function, which is a
measure of how close the teacher and the output
 are, by tuning
θ . As an example, the quadratic cost L = i f (x i ) − yi 2
is often used in regression problems. On the other hand, in
unsupervised learning (e.g., clustering), only input data are
provided, and some objective cost function that does not
involve the teacher is minimized.
Here we summarize the QCL algorithm on an N -qubit
circuit:
(1) Encode input data {x i } into some quantum state
|ψin (x i ) by applying a unitary input gate U (x i ) to initialized
qubits |0.

032309-1

©2018 American Physical Society

K. MITARAI, M. NEGORO, M. KITAGAWA, AND K. FUJII

PHYSICAL REVIEW A 98, 032309 (2018)

(2) Apply a θ -parameterized unitary U (θ ) to the input state and generate an output state |ψout (x i , θ ) =
U (θ ) |ψin (x i ).
(3) Measure the expectation values of some chosen observables. Specifically, we use a subset of Pauli operators
{Bj } ⊂ {I, X, Y, Z}⊗N . Using some output function F , output
yi = y(x i , θ ) is defined to be y(x i , θ ) ≡ F ({Bj (x i , θ )}).
(4) Minimize the cost function L(f (x i ), y(x i , θ )) of the
teacher f (x i ) and the output yi , by tuning the circuit parameters θ iteratively.
(5) Evaluate the performance by checking the cost function with respect to a data set that is taken independently from
the training one.
B. Relation with the existing algorithms

Minimization of the quadratic cost can be performed using
a high-depth quantum circuit with HHL-based algorithms. For
example, Ref. [19] shows a detailed procedure. This matrix
inversion approach is similar to the quantum support vector
machine [10]. As opposed to this, QCL applied to a regression
problem minimizes the cost by iterative optimization, successfully circumventing a high-depth circuit.
Quantum reservoir computing (QRC) [20] shares a similar
idea, in the sense that it passes the central optimization procedure to a classical computer. There, output is defined to be
y(x i ) ≡ w · B, where B is a set of observables taken from
quantum many-body dynamics driven with a fixed Hamiltonian, and w is the weight vector, which is tuned on a classical
device to minimize the cost function. The idea stems from
a so-called echo-state network approach [21]. If one views
QRC as a quantum version of the echo-state network, QCL,
which tunes the whole network, can be regarded as a quantum
counterpart of a basic neural network. In the QVE/QAOA,
the famous hybrid quantum algorithms, the weighted sum of
measured expectation values w fixed · B(θ ) is minimized by
tuning the parameter θ. There, an input x of a problem, such as
the geometry of a molecule or topology of a graph, is encoded
to the weight vector wfixed as wfixed (x). This procedure corresponds to a special case of QCL where we do not use the input
unitary U (x), and a cost function L = wfixed · B is utilized.
Figure 1 summarizes a comparison of the QVE/QAOA, QRC,
and presented QCL frameworks.
C. Ability to approximate a function

First, we consider the case where input data are onedimensional, for simplicity. It is straightforward to generalize
the following argument for higher-dimensional inputs.
Let x and ρin (x) = |ψin (x) ψin (x)| be an input datum and a corresponding density operator of the input
state. ρin (x) can be expanded by a set of Pauli operators
⊗N
{P
with ak (x) as coefficients, ρin (x) =
k } = {I, X, Y, Z}
k ak (x)Pk . A parametrized unitary transformation U (θ )
acting on ρin (x) creates the output state, which can also be
expanded by
{Pk } with {bk (x, θ )}. Now let uij (θ ) be such that
bm (x, θ ) = k umk (θ )ak (x). bm is the expectation value of
the Pauli observable itself, and therefore, the output is a linear
combination of input coefficient functions ak under unitarity
constraints imposed on {uij }.

Classical counterpart

Hybrid algorithms

Simulated annealing

QVE / QAOA
:
to be minimized via

Echo-State Network

QRC

: to be minimized via
Neural Network

QCL

: to be minimized via

FIG. 1. Comparison of the QVE/QAOA, QRC, and presented
QCL frameworks. In the QVE, the output of the quantum circuit
is directly minimized. The QRC and QCL both optimize the output
to the teacher f (x). QRC optimization is done by tuning the linear
weight w, as opposed to the QCL approach, which tunes the circuit
parameter θ.

When the teacher f (x) is an analytical function, we can
show, at least in principle, that QCL is able to approximate
it by considering a simple case with an input state created
by single-qubit rotations. The tensor product structure of the
quantum system plays an important role in this analysis. Let
us consider a state of N qubits:

1 
[I
+
xX
+
1 − x 2 Zi ].
i
2N i=1
N

ρin (x) =

(1)

This state can be generated for any x ∈ [−1, 1] with single
−1
Y
qubit rotations, namely, N
x), where RiY (φ) is
i=1 Ri (sin
the rotation of the ith qubit around the y axis with angle φ.
The state given by Eq. (1) has higher-order terms up to the N th
with respect to x. Thus an arbitrary unitary transformation on
this state can provide us with an arbitrary N th-order polynomial
√ as the expectation value of an observable. Terms like
x 1 − x 2 in Eq. (1) can enhance its ability to approximate
a function.
An important note regarding the example given above is
that the highest-order term x N is hidden in an observable
X⊗N . To extract x N from Eq. (1), one needs to transfer the
nonlocal observable X⊗N to a single-qubit observable using
an entangling gate such as the controlled-NOT gate. Entangling
nonlocal operations are the key ingredients of nonlinearity of
an output.
The above argument can readily be generalized to multidimensional inputs. Assume that we are given, with
d-dimensional data, x = {x1 , x2 , .., xd } and want higher
terms up to the nk th (k = 1, . . . , 
d ) for each datum,
then encode this datum in an N = k nk -qubit
√ quantum
nk
1 d
state as ρin (x) = 2N k=1 ( i=1 [I + xk Xi + 1 − xk2 Zi ]).
These input states automatically have an exponentially large
number of independent functions as coefficients set to the
number of qubits. The tensor product structure of the quantum
system readily “calculates” a product such as x1 x2 .
The unitarity condition of uij may have the effect of
eliminating the overfitting problem, which is crucial for its
performance in machine learning or in regression methods.

032309-2

QUANTUM CIRCUIT LEARNING

PHYSICAL REVIEW A 98, 032309 (2018)

One way to handle it in classical machine learning methods
is to add a regularization term to the cost function. For
example, ridge regression adds the regularization
term w2

to the quadratic cost function. Overall, L = i f (x i ) − w ·
φ(x i )2 + w2 is minimized. The weight vector w corresponds to the matrix element uij in QCL. The norm of the
row vector ui , however, is restricted to unity by the unitarity
condition, which prevents overfitting, from the unitarity of
quantum dynamics. Simple examples of this are given in the
Appendix.

FIG. 2. Quantum circuit used in numerical simulations. The parameters θ of single-qubit arbitrary unitaries U (θj(i ) ) are optimized to
minimize the cost function. D denotes the depth of the circuit.

D. Possible quantum advantages

We have shown in the above discussion that approximation of any analytical function is possible with the use of
nonlinearity created by the tensor product. In fact, nonlinear
basis functions are crucial for many methods utilized in classical machine learning. They require a large number of basis
functions to create a complex model that makes predictions
with a high precision. However, the computational cost of
learning increases with respect to an increasing number of
basis functions. To avoid this problem, the so-called kerneltrick method, which circumvents the direct use of a large
number of them, is utilized [18]. In contrast, QCL directly
utilizes the exponential number of functions with respect to
the number of qubits to model the teacher, which is basically
intractable on classical computers. This is a possible quantum
advantage of our framework, which was not obvious from
previous approaches like the QVE and QAOA.
Moreover, let us now argue about the potential power of
QCL representing complex functions. Suppose we want to
learn the output of QCL that is allowed to use unlimited resources in the learning process, via classical neural networks.
Then it has to learn the relation between inputs and outputs
of a quantum circuit, which, in general, includes universal
quantum cellular automata [22,23]. This certainly could not
be achieved using a polynomial-sized classical computational
resource to the number of qubits used for QCL. This implies
that QCL has the potential power to represent more complex
functions than the classical counterpart. Further investigations
are needed, including of the learning costs and which actual
learning problem enjoys such an advantage.
E. Optimization procedure

In the QVE [13], it has been suggested to use gradient-free
methods like Nelder-Mead. However, gradient-based methods
are generally more preferred when the parameter space becomes large. In neural networks, the backpropagation method
[18], which is basically gradient descent, is utilized in the
learning procedure.
To calculate the gradient of the expectation value of an
observable with respect to a circuit parameter θ , suppose the
unitary U (θ ) consists of a chain of unitary transformations
l
j =1 Uj (θj ) on a state ρin and we measure an observable
B. For convenience, we use the notation Uj :k = Uj . . . Uk .
†
Then B(θ ) is given as B(θ ) = Tr(BUl:1 ρin Ul:1 ). We assume that Uj is generated by a Pauli product Pj , that is,
Uj (θ ) = exp(−iθj Pj /2). The gradient is calculated to be
†
†
∂B
= − 2i Tr(BUl:j [Pj , Uj −1:1 ρin Uj −1:1 ]Ul:j ). While we can∂θj

not evaluate the commutator directly, the following property
of the commutator for an arbitrary operator ρ enables us to
compute the gradient on a quantum circuit:



 
π
π
π
† π
†
ρUj
−Uj −
ρUj −
.
[Pj , ρ] = i Uj
2
2
2
2
(2)
The gradient can be evaluated by



∂B
π
1
† π
†
ρj Uj
Ul:j +1
= Tr BUl:j +1 Uj
∂θj
2
2
2



1
π
π
†
†
− Tr BUl:j +1 Uj −
ρj Uj −
Ul:j +1 ,
2
2
2
(3)
†

where ρj = Uj :1 ρin Uj :1 . Just by inserting ±π/2 rotation generated by Pj and measuring the respective expectation values
B±
j , we can evaluate the exact gradient of an observable B,
B+ −B−

via ∂B
= j 2 j . A similar method is used by Li et al. [24]
∂θj
in their research on control pulse optimization with a target
quantum system.
III. NUMERICAL SIMULATIONS

We demonstrate the performance of the QCL framework
on several prototypical machine learning tasks by numerically simulating a quantum circuit in the form of Fig. 2
with N = 6 and D = 6. U (θj(i) ) in Fig. 2 is an arbitrary
rotation of a single qubit. We use the decomposition U (θj(i) ) =
RjX (θj(i)1 )RjZ (θj(i)2 )RjX (θj(i)3 ). H is the Hamiltonian of a fully
connected transverse Ising model:
N

N

j −1

aj Xj +

H =
j =1

Jj k Zj Zk .

(4)

j =1 k=1

The coefficients aj and Jj k are taken randomly from a uniform
distribution on [−1, 1]. The evolution time T is fixed to 10.
The results shown throughout this section are generated by
the Hamiltonian with the same coefficients. Here we note
that we have checked that similar results can be achieved
with different Hamiltonians. The dynamics under this form
of Hamiltonian can generate a highly entangled state and
is, in general for a large number of qubits, not efficiently
simulatable on a classical computer. Equation (4) is the basic
form of interaction in trapped ions or superconducting qubits,

032309-3

K. MITARAI, M. NEGORO, M. KITAGAWA, AND K. FUJII
(a)

(b)

(c)

(d)

PHYSICAL REVIEW A 98, 032309 (2018)

FIG. 4. Demonstration of a simple nonlinear classification task.
(a) Teacher data. Blue dots indicate class 0; red dots, class 1. (b)
Optimized output from the first qubit (after softmax transformation).
The threshold for classification is 0.5; less than 0.5 and greater
than 0.5 indicate that the point is classified as class 0 and class 1,
respectively.

FIG. 3. Demonstration of QCL performance to represent functions. “Initial” indicates the output of the quantum circuit with
randomly chosen θ ; “final,” the output from the optimized quantum
circuit. Fitting of (a) x 2 , (b) ex , (c) sin x, and (d) |x|.

which makes the time evolution easily implementable experimentally. θ is initialized with random numbers uniformly
distributed on [0, 2π ]. In all numerical simulations, outputs
are taken from Z expectation values. To emulate a sampling,
we added small Gaussian
noise with standard deviation σ
√
determined by σ = 2/Ns (Z2 − 1)/4, where Ns and Z
are the number of samples and a calculated expectation value,
to Z [25].
First, we perform the fitting of f (x) = x 2 , ex , sin x, |x| as
a demonstration of the representability of nonlinear functions
[18]. We use the normal quadratic loss for the cost function.
The number of teacher samples is 100. The output is taken
from the Z expectation value of the first qubit as shown in
Fig. 2. In this simulation, we allow the output to be multiplied
by a constant a which is initialized to unity. This constant a
and θ are simultaneously optimized.
 The input state ρin (x) is
prepared by applying Uin (x) = j RjZ (cos−1 x 2 )RjY (sin−1 x)
to initialized qubits |0. This unitary creates a state similar to
Eq. (1).
Results are shown in Fig. 3. All of the functions are well
approximated by a quantum circuit driven by the presented
QCL framework. To approximate highly nonlinear functions
such as sin x or a nonanalytical function |x|, QCL has brought
out the high-order terms which are initially hidden in nonlocal
operators. The result of fitting |x| [Fig. 3(d)] is relatively
poor because of its nonanalytical characteristics. A possible
solution for this is to employ different functions as the input
functions, such as Legendre polynomials. Although the choice
of input functions affects the performance of QCL, the result
shows that QCL with simple input has the ability to output a
wide variety of functions.
As the second demonstration, the classification problem,
which is an important family of tasks in machine learning,

is performed. Figure 4(a) shows the training data set; blue
and red points indicate classes 0 and 1, respectively. Here we
train the quantum circuit to classify based on each training
input data points x i = (xi,0 , xi,1 ). We define the teacher f (x i )
for each input x i to be the two-dimensional vector (1, 0)
for class 0 and (0, 1) for class 1. The number of teacher
samples is 200 (100 for class 0 and 100 for class 1). The
output is taken from the expectation value of the Pauli Z
operator of the first two qubits, and they are transformed
by the softmax function F. For the d-dimensional vector
q, the softmax function returns the d-dimensional 
vector
F(q ), with its kth element being Fk (q ) = eqk / i eqi .
Thus the output yi = (yi,0 , yi,1 ) is defined by yi =
F(Z1 (x i , θ ), Z2 (x i , θ )). For
 cost function, we
 the
use the cross-entropy L = i k∈{0,1} (f (x i ))k log yik .
The
is prepared by applying Uin (x) =
 Zinput−1 state
−1
2
Y
R
(cos
x
xi,j mod 2 ) to initialized
j j
i,j mod 2 )Rj (sin
qubits |0. j mod 2 is the remainder of j divided by 2. In this
task, the multiplication constant a is fixed to unity.
Learned output is shown in Fig. 4(b). We see that QCL
works as well for the nonlinear classification task. The same
task can be classically performed using, for example, the
kernel-trick support vector machine. The kernel-trick approach discards the direct use of a large number of basis
functions with respect to the number of qubits, as opposed
to the QCL approach, which utilizes an exponentially large
number of basis functions under certain constraints. In this
sense, QCL can benefit from the use of a quantum computer.
Finally, we demonstrate the ability of QCL to perform
a fitting task of quantum many-body dynamics. Simulation
of the dynamics of a 10-spin system under the fully connected transverse Ising Hamiltonian, Eq. (4), is performed
in advance to generate teacher data. Coefficients aj and Jj k
are taken from a uniform distribution on [−1, 1], independently of the coefficients of the Hamiltonian in the circuit.
The dynamics started from the initialized state |0⊗10 . The
transient at the beginning of evolution is discarded for the
duration Ttransient = 300. For practical use, one can employ
the dynamics obtained experimentally from a quantum system
with an unknown Hamiltonian as teacher data. The learned
dynamics is of Z expectation values of three spins during
t ∈ [Ttransient , Ttransient + 8]. This span of t is mapped on x ∈
[−1, 1] uniformly by t = 4(x + 1) + Ttransient to be properly

032309-4

QUANTUM CIRCUIT LEARNING

PHYSICAL REVIEW A 98, 032309 (2018)
(a)

(b)

(c)

(d)

FIG. 5. Demonstration of fitting quantum many-body dynamics.
The partial dynamics of the 10-spin system can be well approximated
by a six-qubit circuit.

introduced to the input gate. Outputs are taken from the Z
expectation values of the first, second, and third qubits in the
circuit. The quadratic cost function is employed. The number
of teacher samples is 100 for each. The multiplication constant
a is fixed to unity.
The result is shown in Fig. 5. It is notable that the three
observables of a complex 10-spin system can be well fitted,
simultaneously, using the three observables of a tuned sixqubit circuit. Although the task performed here is not what
is commonly referred to as a quantum simulation, we believe
that we provide an alternative way to learn a quantum manybody dynamics with a near-term quantum computer. It may
also be possible to extract partial information from the system
Hamiltonian by taking the derivative of the output with respect
to x, which can readily be performed using the same method
for calculating a gradient.
IV. CONCLUSION

We have presented a machine learning framework on nearterm realizable quantum computers. Our method fully employs the exponentially large space of a quantum system, by
mixing simply injected nonlinear functions with a low-depth
circuit to approximate a complex nonlinear function. Numerical results have shown the ability to represent a function, to
classify, and to fit a relatively large quantum system. Also,
theoretical investigation has shown QCL’s ability to provide
us a means for dealing with high-dimensional regression or
classification tasks, which has been unpractical on classical
computers.
Note added. Recently, we have become aware of related
works [26–34].

ACKNOWLEDGMENTS

K.M. and M.N. are supported by JST PRESTO JPMJPR1666. K.M., M.N., and M.K. are supported by JST
CREST JPMJCR1672. K.F. is supported by KAKENHI No.
16H02211, JST PRESTO JPMJPR1668, JST ERATO JPMJER1601, and JST CREST JPMJCR1673.

FIG. 6. A simple example of the avoidance of the overfitting
resulting from unitarity. (a), (c) Fitting result of noise-added sin x
and x 2 using QCL. (b), (d) Fitting result of noise-added sin x and x 2
using the classical regression with same basis functions as used in
QCL.

APPENDIX: UNITARITY AVOIDS OVERFITTING

In this Appendix, we demonstrate a simple example that
supports our claim in the text that the unitarity of the transformation has the effect of eliminating overfittings. We perform
a one-dimensional fitting task with a small training data set
to see the avoidance of overfitting. To observe the unitarity
effect, we fix the multiplication constant a to unity. For
simplicity, here we use a three-qubit circuit inthe same form
as in the text, with D = 3 and using Uin = i RiY (sin x) as
the input gate. In this case, the set of basis functions that QCL
utilizes is {x, x 2 , x 3 , (1 − x 2 )1/2 , 1 − x 2 , (1 − x 2 )3/2 , x(1 −
x 2 )1/2 , x 2 (1 − x 2 )1/2 , x(1 − x 2 )}. Therefore for comparison,
we run a simple classical linear regression program using the
same basis function set.
Figures 6(a) and 6(b) show the result of the task of fitting
data points of 0.5 sin x, with Gaussian noise of standard
deviation 0.05 added, using QCL and classical regression,
respectively. The result shows that, probably due to the
unitarity of the transformation, QCL accepts some errors
in the final output, as opposed to the classical regression,
which does not accept any errors in the final output; that is, it
overfits. As opposed to the w = 1 constraint on QCL, the
classical algorithm in this case output a weight vector with
w ≈ 134. Figures 6(c) and 6(d) show the the result of the
task to fit data points of x 2 , with Gaussian noise of standard
deviation 0.05 added, using QCL and classical regression,
respectively. Again, the same observation can be made. The
weight vector obtained by the classical algorithm exhibits
w ≈ 15 800 in this case.

032309-5

K. MITARAI, M. NEGORO, M. KITAGAWA, AND K. FUJII

PHYSICAL REVIEW A 98, 032309 (2018)

[1] G. Carleo and M. Troyer, Science 355, 602 (2017).
[2] M. Rupp, A. Tkatchenko, K.-R. Müller, and O. A. von
Lilienfeld, Phys. Rev. Lett. 108, 058301 (2012).
[3] P. Broecker, J. Carrasquilla, R. G. Melko, and S. Trebst, Sci.
Rep. 7, 8823 (2017).
[4] R. Ramakrishnan, P. O. Dral, M. Rupp, and O. A. von
Lilienfeld, J. Chem. Theory Comput. 11, 2087
(2015).
[5] M. August and X. Ni, Phys. Rev. A 95, 012335 (2017).
[6] P. W. Shor, SIAM J. Comput. 26, 1484 (1997).
[7] M. A. Nielsen and I. L. Chuang, Quantum Computation
and Quantum Information (Cambridge University Press, Cambridge, UK, 2010).
[8] I. Kerenidis and A. Prakash, arXiv:1704.04992.
[9] N. Wiebe, D. Braun, and S. Lloyd, Phys. Rev. Lett. 109, 050505
(2012).
[10] P. Rebentrost, M. Mohseni, and S. Lloyd, Phys. Rev. Lett. 113,
130503 (2014).
[11] Y. Cao, G. G. Guerreschi, and A. Aspuru-Guzik,
arXiv:1711.11240.
[12] A. W. Harrow, A. Hassidim, and S. Lloyd, Phys. Rev. Lett. 103,
150502 (2009).
[13] A. Peruzzo, J. McClean, P. Shadbolt, M. Yung, X. Zhou, P. J.
Love, A. Aspuru-Guzik, and J. L. O’Brien, Nat. Commun. 5,
4213 (2014).
[14] A. Kandala, A. Mezzacapo, K. Temme, M. Takita, M. Brink, J.
M. Chow, and J. M. Gambetta, Nature 549, 242 (2017).
[15] E. Farhi, J. Goldstone, and S. Gutmann, arXiv:1411.4028.
[16] E. Farhi and A. W. Harrow, arXiv:1602.07674.
[17] J. S. Otterbach, R. Manenti, N. Alidoust, A. Bestwick, M.
Block, B. Bloom, S. Caldwell, N. Didier, E. S. Fried, S. Hong,
P. Karalekas, C. B. Osborn, A. Papageorge, E. C. Peterson,
G. Prawiroatmodjo, N. Rubin, C. A. Ryan, D. Scarabelli, M.
Scheer, E. A. Sete, P. Sivarajah, R. S. Smith, A. Staley, N.

Tezak, W. J. Zeng, A. Hudson, B. R. Johnson, M. Reagor, M. P.
da Silva, and C. Rigetti, arXiv:1712.05771.
[18] C. M. Bishop, Pattern Recognition and Machine Learning
(Springer, New York, 2006).
[19] M. Schuld, I. Sinayskiy, and F. Petruccione, Phys. Rev. A 94,
022342 (2016).
[20] K. Fujii and K. Nakajima, Phys. Rev. Appl. 8, 024030 (2017).
[21] H. Jaeger and H. Haas, Science 304, 78 (2004).
[22] R. Raussendorf, Phys. Rev. A 72, 022301 (2005).
[23] D. Janzing and P. Wocjan, Quantum Info. Process. 4, 129
(2005).
[24] J. Li, X. Yang, X. Peng, and C.-P. Sun, Phys. Rev. Lett. 118,
150503 (2017).
[25] The simulation is carried out using the Python library QuTip
[35]. We use the BFGS method [36] provided in the SciPy
optimization library for optimization of parameters.
[26] L. Cincio, Y. Subasi, A. T. Sornborger, and P. J. Coles,
arXiv:1803.04114.
[27] E. Farhi and H. Neven, arXiv:1802.06002.
[28] M. Benedetti, D. Garcia-Pintos, Y. Nam, and A. Perdomo-Ortiz,
arXiv:1801.07686.
[29] M. Schuld and N. Killoran, arXiv:1803.07128.
[30] W. Huggins, P. Patel, K. B. Whaley, and E. M. Stoudenmire,
arXiv:1803.11537.
[31] J.-G. Liu and L. Wang, arXiv:1804.04168.
[32] M. Schuld, A. Bocharov, K. Svore, and N. Wiebe,
arXiv:1804.00633.
[33] M. Fanizza, A. Mari, and V. Giovannetti, arXiv:1805.03477.
[34] M. Benedetti, E. Grant, L. Wossnig, and S. Severini,
arXiv:1806.00463.
[35] J. Johansson, P. Nation, and F. Nori, Comput. Phys. Commun.
184, 1234 (2013).
[36] J. Nocedal and S. Wright, Numerical Optimization (Springer,
New York, 2006).

032309-6

