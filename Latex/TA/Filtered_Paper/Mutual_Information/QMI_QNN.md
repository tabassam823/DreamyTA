Quantum Information Processing (2024) 23:57
https://doi.org/10.1007/s11128-023-04253-1

Estimating quantum mutual information through a
quantum neural network
Myeongjin Shin1 · Junseo Lee2,3 · Kabgyun Jeong4,5
Received: 3 July 2023 / Accepted: 29 December 2023 / Published online: 9 February 2024
© The Author(s) 2024

Abstract
We propose a method of quantum machine learning called quantum mutual information neural estimation (QMINE) for estimating von Neumann entropy and quantum
mutual information, which are fundamental properties in quantum information theory.
The QMINE proposed here basically utilizes a technique of quantum neural networks
(QNNs), to minimize a loss function that determines the von Neumann entropy, and
thus quantum mutual information, which is believed more powerful to process quantum
datasets than conventional neural networks due to quantum superposition and entanglement. To create a precise loss function, we propose a quantum Donsker-Varadhan
representation (QDVR), which is a quantum analog of the classical Donsker-Varadhan
representation. By exploiting a parameter shift rule on parameterized quantum circuits, we can efficiently implement and optimize the QNN and estimate the quantum
entropies using the QMINE technique. Furthermore, numerical observations support
our predictions of QDVR and demonstrate the good performance of QMINE.
Keywords Quantum mutual information · Donsker-Varadhan representation ·
Quantum neural network · Parameterized quantum circuits

B Kabgyun Jeong

kgjeong6@snu.ac.kr
Myeongjin Shin
hanwoolmj@kaist.ac.kr
Junseo Lee
js_lee@norma.co.kr

1

School of Computing, Korea Advanced Institute of Science and Technology (KAIST), Daejeon
34141, Korea

2

School of Electrical and Electronic Engineering, Yonsei University, Seoul 03722, Korea

3

Quantum Security R&D, Norma Inc., Seoul 04799, Korea

4

Research Institute of Mathematics, Seoul National University, Seoul 08826, Korea

5

School of Computational Sciences, Korea Institute for Advanced Study, Seoul 02455, Korea

123

57

Page 2 of 16

M. Shin et al.

1 Introduction
The concept of quantum mutual information (QMI) in quantum information theory
quantifies the amount of information shared between two quantum systems. This
extends the classical notion of mutual information to the quantum regime [1–3]. This
information measure is fundamental, because it determines the quantum correlation or
entanglement between two quantum systems. The information obtained from quantum
mutual information can be applied to various fields of quantum information processing
such as quantum computation, quantum cryptography, and quantum communication
[2, 3] (particularly in quantum channel capacity problems [4, 5]). They also play a
crucial role in quantum machine learning [6, 7], where they measure the information
shared between different representations of quantum datasets. Moreover, the gathered information can be used to enhance the efficiency and effectiveness of quantum
algorithms in processing quantum data.
Quantum mutual information is expressed as the sum of von Neumann entropies,
denoted by S(ρ) = −Tr(ρ ln ρ) for a quantum state ρ, making the determination of
the von Neumann entropy [8] essential for calculating quantum mutual information.
In recent years, the estimation of the von Neumann entropy has garnered significant
attention in the field of quantum information theory. Various methods have been proposed to estimate von Neumann entropy, including those exploiting quantum state
tomography [9], Monte Carlo sampling [10], and entanglement entropy [11–18]. Several studies [16–18] have utilized quantum query models for entropy estimation and
have demonstrated promising quantum speedups. Specifically, Wang et al. [16] proposed that the von Neumann entropy can be estimated with an accuracy of ε by using
2
O( rε2 ) queries. However, these query model-based algorithms have practical limitations because a quantum circuit that generates the quantum state must be prepared, and
the effectiveness of constructing a quantum query model for the input state remains
an open question [15]. Thus, we focused on estimating the von Neumann entropy of
an unknown quantum state using only identical copies of the state. To the best of our
knowledge, no existing quantum algorithms estimate the von Neumann entropy using
O(poly(r ), poly( 1ε )) copies of the quantum state, where r represents the rank of the
state.
A mutual information neural estimation (MINE) method is a novel technique that
utilizes neural networks to calculate the classical mutual information between two
random variables. More precisely, this method optimizes a neural network to estimate
mutual information by minimizing the loss function. The loss function is based on the
Donsker-Varadhan representation [19] that provides a lower bound for the well-known
Kullback–Leibler (KL) divergence.
Quantum neural networks (QNNs) [20, 21], which are among the most powerful
quantum machine learning methods, serve as quantum counterparts to conventional
neural networks, and offer several advantages. One notable advantage is the ability to
use a quantum state as an input, which is particularly advantageous when calculating
quantum mutual information or the von Neumann entropy. We identified two types of
QNNs in the literature [20, 22] that possess a neural network structure and leverage
quantum advantages accompanied by well-defined training procedures. In this study,

123

Estimating quantum mutual information...

Page 3 of 16

57

we employed a parameterized quantum circuit [22], which is known for its quantum
advantages, despite the presence of the barren plateau problem, which requires further
investigation [23].
As a quantum analog of MINE, we propose a quantum mutual information neural
estimation (QMINE), which is a method for determining the von Neumann entropy and
quantum mutual information through a quantum neural network technique. Similar to
the classical case, QMINE uses a quantum neural network to minimize the loss function
that evaluates the von Neumann entropy. To generate a loss function that estimates
the von Neumann entropy, we present the quantum Donsker-Varadhan representation
(QDVR), which is a quantum version of the Donsker-Varadhan representation. QMINE
offers the potential for a quantum advantage in estimating the von Neumann entropy
facilitated by QDVR. By converting the problem of von Neumann entropy estimation
into a quantum machine learning regime, QMINE opens new possibilities. There is
also the potential to estimate von Neumann entropy using only O(poly(r ), poly( 1ε ))
copies of the quantum state. However, we acknowledge that further investigation is
required owing to the challenging and well-known barren plateau problem, as well as
the need for efficient quantum training methods.
The remainder of this paper is organized as follows. In Sect. 2, we briefly introduce
the basic notions of quantum mutual information, MINE, and parame- trized quantum
circuits. In Sect. 3, we generalize the Donsker-Varadhan representation to a QDVR,
which is the main component of QMINE. We also propose an estimation method for
von Neumann entropy using quantum neural networks in Sect. 4. This implies that
it is possible to efficiently obtain the quantum mutual information, and its numerical
simulations under the framework of QMINE in Sect. 5. Finally, a discussion and
remarks are presented in Sect. 6, and open questions and possibilities are raised for
future research.
Note on concurrent work. The independent and concurrent work [24] appeared
on the arXiv a few days after our preprint was uploaded. It introduced a method for
estimating von Neumann entropy reminiscent of ours, with Rényi entropy, measured
relative (Rényi) entropy, and fidelity. Our work focused on estimating von Neumann
entropy with low copy complexity. We reduced the domain in the variation formula but
Ref. [24] did not. We believe that limiting the trace and rank in the variation formula
is crucial for effective estimation.

2 Preliminaries
2.1 Quantum mutual information and von Neumann entropy
Quantum mutual information, also known as von Neumann mutual information, quantifies the relationship between two quantum states. This can be calculated by using the
formula (See Fig. 1):
 


 
I (A : B) = S ρ A + S ρ B − S ρ AB .

(1)

123

57

Page 4 of 16

M. Shin et al.

Fig. 1 Schematic diagram for
the quantum mutual
information, I (A : B), between
two quantum states ρ A and ρ B

Here, S(ρ) represents the von Neumann entropy [8] of quantum state ρ in a ddimensional Hilbert space, given by S (ρ) = −Tr (ρ log ρ). Therefore, estimating
the von Neumann entropy enables the estimation of the quantum mutual information.
The von Neumann entropy, which is an extension of the Shannon entropy [25] to
the quantum domain, can be estimated using quantum circuits and measurements. It
is defined as the entropy of the density matrix associated with a quantum state, where
the density matrix is a positive semi-definite matrix that represents the state. To estimate the von Neumann entropy, measurements can be performed on multiple copies
of the quantum state and the outcomes of these measurements can be utilized. The
most straightforward approach is to directly estimate the density matrix and calculate the entropy using its definition. However, estimating the von Neumann entropy
can be challenging, particularly for large quantum systems, owing to the difficulty
in accurately estimating the density matrix. Furthermore, the estimation accuracy is
influenced by the number of measurements conducted and the quality of the quantum hardware employed. However, ongoing research is focused on developing more
efficient and precise methods for estimating the von Neumann entropy.
Several methods have been employed to estimate von Neumann entropy, particularly those utilizing the quantum query model [15, 17, 18]. In the quantum query
model, if the quantum circuit U produces a quantum state ρ, it utilizes unitary gates
such as U , U † , and CU (controlled-U ). However, the quantum circuit must be known
to use the query model. The effectiveness of constructing a quantum query model for
a given input state remains uncertain [15], prompting us to explore the von Neumann
entropy estimation without relying on the quantum query model. In the absence of a
query model, our approach solely exploits identical copies of quantum states. Previous studies, such as Acharya et al. [13] employed O(d 2 ) copies of the quantum
 state
1
ρ, where d denotes the dimension, whereas Wang et al. [15] used O ε5 λ2 copies
of ρ, where λ represents the lower bound on all nonzero eigenvalues. To the best of
our knowledge, no existing algorithm provides a high-accuracy estimation of the von
Neumann entropy by using only O(poly(r )) copies of ρ with rank r .
2.2 Mutual information neural estimator
The mutual information neural estimator (MINE) [26] is a method for estimating the
mutual information of two random variables by using neural networks. This approach
involves selecting functions Tθ : X × Y → R that are parameterized by neural
networks with the parameter θ ∈ Θ. Considering n samples, we define the empirical
(n)
(n)
(n)
joint and product probability distributions as p X Y and p X × pY , respectively. The

123

Estimating quantum mutual information...

Page 5 of 16

57

MINE strategy is given by:
 


I (X
: Y )n = sup E p X Y [Tθ ] − log E p X × pY e Tθ ,
θ∈Θ

(2)

where E is the expected value. Additionally, the Donsker-Varadhan representation is
defined as follows: For any probability distribution functions p and q,
D K L ( p||q) =

  
sup E p [T ] − log Eq e T ,

T :Ω→R

(3)

where we take the supremum over all the functions T .
Using the Donsker-Varadhan representation [27], it can be proven that I (X : Y ) ≥

I (X : Y )n and MINE are strongly consistent, meaning that there exists a positive
integer
N and a choice of neural network parameters θ ∈ Θ such that for all n ≥ N ,




: Y )n  ≤ ε. By applying a gradient descent method on the neural
 I (X : Y ) − I (X



network Tθ to maximize E p X Y [Tθ ] − log E p X × pY e Tθ , we can obtain I (X
: Y )n
and estimate the mutual information I (X : Y ).
The MINE technique has found applications in various areas of artificial intelligence, such as feature selection, representation learning, and unsupervised learning,
using information-theoretic methods. Compared to previous approaches, it provides
more accurate and robust estimates of mutual information, leading to significant
advancements in the field of artificial intelligence (AI). It is important to recognize that
MINE is a relatively new and rapidly evolving field, with ongoing research focused
on enhancing and broadening its capabilities. Nonetheless, the MINE technique is
widely regarded as a valuable tool in AI and information theory, offering a powerful
and flexible approach for estimating the mutual information between variables.
2.3 Parametrized quantum circuits
Parameterized quantum circuits (PQCs) [22] are quantum circuits that incorporate
adjustable parameters, typically represented as real numbers. These parameters can be
fine-tuned to control the behavior of the quantum circuit, thereby providing increased
flexibility and optimization potential. Parameterized quantum circuits have extensive
applications in quantum machine learning and optimization algorithms, enabling computations that are challenging or even infeasible using classical methods.
By manipulating circuit parameters, one can efficiently learn and represent quantum
systems in a compact and adaptable manner. In quantum optimization, parameterized
quantum circuits play a crucial role in global minimum search. The objective function
can be represented as a measurement outcome of the quantum circuit. The quantum
circuit can harness superposition and entanglement to explore the search space more
effectively than classical optimization algorithms.
One of the core techniques used in quantum optimization procedures for parameterized quantum circuits is the parameter shift rule [28]. The parameter shift rule is

123

57

Page 6 of 16

M. Shin et al.

a powerful tool in quantum machine learning that enables efficient computation of
gradients with respect to the parameters of a quantum circuit.
The fundamental concept behind the parameter shift rule is to employ a quantum
circuit with adjustable parameters to perform the measurements. By utilizing the measurement outcome, it is possible to estimate the gradient of a cost function with respect
to the circuit parameters. This rule capitalizes on the notion that small variations in
the parameters of a quantum circuit can be used to calculate the derivative of the cost
function pertaining to these parameters.
The underlying principle involves the preparation of two identical copies of a quantum state, each with slightly different parameter values. By comparing these two
quantum states, it was possible to estimate the gradient. By using multiple samples
via measurement, the gradient can be estimated.
If a parameterized quantum circuit is represented as a sequence of unitary gates, it
is denoted as
N

Ui (θi ) U0 (x).

U (x; θ ) :=
i=1

The output of the circuit can then be observed using an observable Ô and the measurement outcome becomes a quantum circuit function. The quantum circuit function is
expressed in simplified form as f (x; θi ) = ψi |Ui† (θi ) Ôi+1 Ui (θi )|ψi  for each i. The
gradient of the quantum circuit function can then be calculated using the parameter
shift rule, as follows:

∇θi f (x; θi ) = c ψi |Ui† (θi + s) Ôi+1 Ui (θi + s)|ψi 

−ψi |Ui† (θi − s) Ôi+1 Ui (θi − s)|ψi  .

(4)

The parameter shift rule has been successfully employed in various quantum
machine learning algorithms, including quantum neural networks [20, 22] and quantum support vector machines [29, 30], for optimization and training purposes. It is
regarded as a valuable tool for developing efficient quantum machine learning algorithms, as it enables the efficient computation of gradients in quantum systems, which
is often a challenging task. It is important to note that the parameter shift rule is an
approximation, and its accuracy depends on factors such as the choice of parameters,
cost function, and the specific quantum circuit. Nevertheless, it has proven to be a
useful and efficient technique in the emerging field of quantum machine learning, and
our ongoing research focuses on enhancing and expanding its potential capabilities.

3 Quantum Donsker-Varadhan representation
The quantum Donsker-Varadhan representation is a mathematical framework that
enables quantum neural networks to estimate the von Neumann entropy. It is a quantum counterpart of the original Donsker-Varadhan representation, with the distinction

123

Estimating quantum mutual information...

Page 7 of 16

57

that QDVR focuses solely on the quantum entropy rather than on the relative entropy.
QDVR can be considered as a modified version of the Gibbs variational principle [31],
which restricts the domain to density matrices.
As mentioned previously, MINE [26] exploits the original Donsker-Varadhan representation to estimate classical mutual information using a (classical) neural network.
In the context of estimating mutual quantum information, it is natural to consider a
quantum version of the Donsker-Varadhan representation. Notably, we need only estimate the components of von Neumann entropy S(ρ A ), S(ρ B ), and S(ρ AB ) to determine
the quantum mutual information I (A : B). A variational formula for von Neumann
entropy exists as follows:
Theorem 1 (Gibbs Variational Principle [31]) Let f : H d×d → R be a function
defined on d-dimensional Hermitian matrices T and ρ be a density matrix. Then we
have


(5)
f (T ) = −Tr(ρT ) + log Tr(e T ) .
Thus, for d-dimensional Hermitian matrices T , the von Neumann entropy is given by:
S(ρ) = inf f (T ),
T

(6)

where the infimum is taken over all Hermitian T .
Our objective is to determine the Hermitian matrix T that maximizes
f (T ). We

parameterize T by using ti ∈ R and |ψi  ∈ Cd . We canexpress T= ri=1 ti |ψi  ψi |,
d
d
ti
which gives us f (T ) = − i=1
ti ψi | ρ |ψi  + log
i=1 e . To compute f (T ),
d . Achieving this with
we must measure the quantum state ρ using the basis {|ψi }i=1

an error smaller than ε requires O( σε2 ) samples of ρ, where σ := Var({ti }). However,
the number of required samples of ρ can become substantial because of the broad
domain of T , which encompasses all Hermitian matrices. Therefore, reducing the size
of this domain is imperative.
2

Lemma 1 For all Hermitian matrices T , the function f holds that
f (T ) = f (T + cI )

(7)

for a constant c.
Proof For any T ∈ H d×d , we have


f (T + cI ) = −Tr(ρ(T + cI )) + log Tr(e T +cI )


= −Tr(ρT ) − cTr(ρ) + log ec Tr(e T )


= −Tr(ρT ) − log Tr(e T )
= f (T ).

123

57

Page 8 of 16

M. Shin et al.

Thus, f (T ) = f (T + cI ) for a constant c.
Proposition 1 (Domain Reduction) Let f : H d×d → R be a function defined on
d-dimensional Hermitian matrices and let ρ be a density matrix. Then,
S(ρ) = inf f (T )
T

(8)

for d-dimensional ‘positive’ Hermitian matrices T .
Proof For any Hermitian matrix T ∈ H d×d , let c = max|ψi ∈Cd (− ψi | T |ψi ).
From Lemma 1, there exists a positive Hermitian matrix T0 = T + cI such that
f (T ) = f (T0 ). Therefore, we can reduce the domain of T to a positive Hermitian
matrix.
Now, we only need to search for the space of the positive Hermitian matrices to find
the optimal T . The computational complexity of copying ρ to calculate f (T ) depends
on T . To reduce this complexity, we need to specify and limit the trace of T .
Lemma 2 A positive Hermitian matrix T0 with rank r exists that satisfies Tr(T0 ) ≤
2r n + r log 1ε such that
|S(ρ) − f (T0 )| < ε,

(9)

where ρ is an r -rank density matrix.
Proof See the details of the proof in “Appendix A”.
Proposition 2 (Quantum Donsker-Varadhan Representation) Let f : H d×d → R be a
function defined on d-dimensional Hermitian matrices, and let ρ be an r -rank density
matrix.


(10)
g(T ) = −Tr (cρT ) + log Tr(ecT ) ,

where c ≥ 2r n + r log 1ε . Then,
|S(ρ) − inf(g(T ))| < ε

(11)

for any d-dimensional r -rank density matrix T .
Proof By using Lemmas 1 and 2, there exists an r -rank positive Hermitian matrix T0
with Tr(T0 ) = c such that |S(ρ) − f (T0 )| < ε. Thus, T1 = Tc0 is an r -rank density
matrix, and |S(ρ)−g(T1 )| < ε. From Theorem 1, S(ρ) ≤ g(T ) for all density matrices
T . Therefore, |S(ρ) − inf(g(T ))| ≤ |S(ρ) − g(T1 )| < ε. This completes the proof.
According to the quantum Donsker-Varadhan representation in Proposition 2, we
only need to search within the space of the density matrices. By calculating g(T )
2
with an error of ε, the complexity of copying ρ is O( εc2 ). Next, we plan to determine
the optimal density matrix T that minimizes g(T ). In the next section, we will use
quantum neural networks to determine the optimal T .

123

Estimating quantum mutual information...

Page 9 of 16

57

4 Von Neumann entropy estimation with quantum neural networks
We now explain the estimation of von Neumann entropy using quantum neural networks, specifically focusing on parameterized quantum circuits as an example. Our
approach is inspired by the work of Liu et al. [32], who utilized variational autoregressive networks and quantum circuits to address problems in quantum statistical
mechanics. To achieve this, specific values are assigned to the variables in T by defining
Cd . Additionally,
t as a set of real numbers, {ti |ti ∈ R} and |ψi  as complex vectors in 
let us assume that the rank of ρ is denoted by r , and we define T= ri=1 ti |ψi  ψi |.
r
Consequently,

r thect function g(T ) becomes g(T ) = −c i=1 ti ψi | ρ |ψi  +
i
log d − r + i=1 e . We can introduce a unitary operator U that transforms |ψi 
into |i, and represent this unitary operator using a set of parameters θ as U (θ ) as
follows:
g(T ) = −c

r


ti i| U (θ )ρU † (θ ) |i + log d − r +

i=1

r


ecti

.

(12)

i=1

By considering U (θ ) as a quantum neural network and ρ as its input, we can obtain
the network output by computing U (θ )ρU † (θ ). To accurately calculate g(T ) with
an error rate less than
to measure the output of the quantum neural
 ε, it is necessary

2
c2
i)
=
O
times.
network O Var(ct
ε2
ε2
Our objective was to optimize the parameters to determine the infimum of g(T ).
For example, let us consider a parameterized quantum circuit [22] with Pauli gates as
θi
k
a quantum neural network U (θ ) = i=1
U (θi ), where U (θi ) = e−i 2 Pi . By applying
the parameter shift rule [28], we observe that
∇θ g(t, θ ) =


π
π 
1 
g t, θ +
− g t, θ −
,
2
2
2

(13)

and
∂ g(t, θ )
cecti

= −c i| U (θ )ρU † (θ ) |i +
.
∂ti
d − r + ri=1 ecti

(14)

r
conditions ti ≥ 0 and
i=1 ti = 1, we choose ti =
To satisfy the
 2
i−1
2
cos ϕi . We can apply gradient descent to ϕ j and θi to optimize the
j=1 sin ϕ j
 2
quantum circuit. To calculate the gradient, we require O εc2 ×(#of parameters in QNN)
copies of ρ. Therefore, to obtain inf (g (T )) and estimate S (ρ) with an error of less
than ε, we require

 2
c
O
× (# of parameters in QNN) × (# of trainings in QNN)
ε2
 2
 

r
2
2 1
=O
n
n
+
log
n
params
train
ε2
ε

(15)

123

57

Page 10 of 16

M. Shin et al.

copies of ρ.
3
Analytic gradient measurements in convex loss functions require O( nε2 ) copies of ρ
to converge to a solution with O(ε) close to the optimum [33]. In general, situations that
involve parameterized quantum circuits may have nonconvex loss functions, but many
algorithms still utilize parameterized quantum circuits and achieve quantum speedups.
We anticipate that quantum speedup can be achieved by employing parameterized
quantum circuits with analytic gradient measurements in QMINE and estimating the
von Neumann entropy using O(poly(r )) copies of ρ. In future research, we will
investigate the relationships between n train and n params , and the performance of this
approach. The key point is to transform the quantum mutual information estimation
problem into a quantum neural network problem.

5 Numerical simulations
We demonstrated the performance of QMINE in estimating the quantum mutual information of random density matrices through numerical simulations of a quantum circuit.
Our goal is to show that QMINE can estimate quantum mutual information with low
error. We also analyze the rank and trainable parameters, and conducted simulations
to support the results on QDVR.
5.1 Rank analysis
Based on QDVR, we establish that if the rank of the density matrix ρ is r , then setting
the rank of the parameter matrix T to r is sufficient. Thus, we aim to determine the
optimal T that estimates the von Neumann entropy. To investigate the effect of rank,
we experimented with the rank of T by letting r = rank(ρ) and k = rank(T ). In this
analysis, we simulate the scenario with N = 5, D = 30, r = 8, and c ≤ 80, where
N is the number of qubits, D is the circuit depth, r is the rank of the density matrix,
c is calculated using QDVR (details are provided in “Appendix B”). Figure 2 shows
that when k ≥ r , the result of QMINE converges to the correct value, whereas when
k < r , it converges at a high error rate. This phenomenon has also been observed
in other cases. These results support the QDVR’s claim that the rank of the optimal
solution T is r . Because convergence is faster when k = r than when k > r , it is best
to use QMINE with k = r .
5.2 Number of trainable parameters on quantum circuit analysis
We analyzed the performance of QMINE by varying the depth of the quantum circuit. In our simulations, we used N = 5, D = 30, r = k = 8, and c ≤ 80. The
experimental results confirmed that as the depth of the circuit and the number of
parameters increased, the estimation accuracy of QMINE improved. Figure 3 illustrates the results, showing that a circuit depth of 20 achieved the best performance. It
converged rapidly with a lower error compared to a depth of 30, which converged at
a slower rate despite having a similar error. These findings emphasize the importance

123

Estimating quantum mutual information...

Page 11 of 16

57

Fig. 2 We compare the performance of different approaches. The green curve represents QMINE with the
exact rank, which exhibited the best performance. It converges rapidly with low error. However, the red
curve represents QMINE with a lower rank, which converges with a high error. Finally, the blue curve
represents QMINE with a higher rank, which converges with low error but at a slower pace (Color figure
online)

Fig. 3 The green line in the graph, representing a circuit depth of 20 with 400 parameters, exhibits the best
performance. It converges quickly with a low error-rate. However, the red line, representing a depth of 10
with 200 parameters, converges with a high error-rate. The blue line, corresponding to a depth of 30 with
600 parameters, achieves a low error but it takes a longer-time to converge (Color figure online)

of choosing an appropriate circuit depth (i.e., number of parameters) in QMINE. The
copy complexity is determined by the number of parameters (n params ) and the number
of training iterations (n train ). Therefore, when applying QMINE in various situations,
it is crucial to select the correct circuit depth. We plan to investigate this aspect in
future studies.

123

57

Page 12 of 16

M. Shin et al.

Fig. 4 Estimation result of the quantum mutual information of a random density matrix

5.3 Estimating quantum mutual information
We estimated the quantum mutual information of a random density matrix using
simulations with N = 4 qubits. For each tested random density matrix, we achieved
error rates ranging from 0.1% to 1%. Additional details can be found in “Appendix
B” (Fig. 4).

6 Conclusions
We have addressed the quantum Donsker-Varadhan representation, which is a mathematical framework for estimating von Neumann entropy. The QDVR allows us to find
the optimal T by searching only within the density matrices, resulting in low copy
complexity for calculations. By optimizing the quantum neural network using QDVR
and the parameter shift rule, we can estimate von Neumann entropy and subsequently

123

Estimating quantum mutual information...

Page 13 of 16

57

estimate the quantum
The number
of copies of ρ required is

 2  mutual information.
1
r
2
2
approximately O ε2 n + log ε n params · n train .
Through the numerical simulations, we demonstrated that the quantum mutual
information neural estimation (QMINE) performs well, and it aligns with the results
of quantum Donsker-Varadhan representation. The rank analysis supported the results
of QDVR, whereas the circuit depth analysis emphasized the importance of selecting
an appropriate circuit depth. In addition, we estimated the quantum mutual information
and achieved a low error rate. The key finding of this study is the conversion of the
quantum mutual information and von Neumann entropy estimation problem into a
quantum neural network problem. In future, we suggest investigating the specifics
of n params and n train pertaining to the quantum neural network problem. This will be
explored in future studies.
Acknowledgements This work was supported by the National Research Foundation of Korea (NRF)
through grants funded by the Ministry of Science and ICT (NRF-2022M3H3A1098237) and the Ministry of Education (NRF-2021R1I1A1A01042199). This work was partially supported by an Institute for
Information & Communications Technology Promotion (IITP) grant funded by the Korean government
(MSIP) (No. 2019-0-00003; Research and Development of Core Technologies for Programming, Running,
Implementing, and Validating of Fault-Tolerant Quantum Computing Systems).
Funding Open Access funding enabled and organized by Seoul National University.
Data availability Our manuscript has no associated data.

Declarations
Conflict of interest The authors have no conflicts to disclose.
Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which
permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give
appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence,
and indicate if changes were made. The images or other third party material in this article are included
in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If
material is not included in the article’s Creative Commons licence and your intended use is not permitted
by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the
copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.

Appendix A Proof of Lemma 2
Here, we provide an explicit proof of Lemma 2 and details of the numerical simulation
results.
r
r
i=1 pi |ψi ψi |, let us define T0 =
i=1 ti |ψi ψi | with ti =
 For given ρ =
pi
log( k ), if pi ≥ k;
and k = dε2 . Then, the bound on the value of |S (ρ) − f (T0 )|
0,
if pi < k
can be derived as:

123

57

Page 14 of 16

M. Shin et al.






|S (ρ) − f (T0 )| = S (ρ) + Tr (ρT0 ) − log Tr(e T0 ) 

⎛
⎞

  
p 

 pi 
 r
1
i
⎠
pi log
pi log
1+
− log ⎝
+
= 
pi
k
k 
 i=1
pi ≥k
pi <k
pi ≥k

⎛
⎞


  
 

 pi 

1
1


⎝
⎠
=
pi log
pi log
1+
− log
+
pi
k
k 
 pi <k
pi ≥k
pi <k
pi ≥k


  
 

1
1
pi log
pi log
+
= 
p
k
i
 pi <k
pi ≥k
⎞
⎛
 
 
 pi 

1
1
⎠
1+
− log
+ log
− log ⎝
k
k
k 
pi <k
pi ≥k

⎛
⎞








k
pi log
k+
pi ⎠
− log ⎝
= 
pi

 pi <k
pi <k
pi ≥k

⎛
⎞


  
 



1
1

⎝
⎠
=
pi log
pi log
+ log 1 +
+
(k − pi ) 
p
k
i

 pi <k
pi <k
pi <k

1
 
2
2ε 2 log d + log ε
ε
1
+ dk =
+
≤ 2dk log
k
d
d
< ε.

That is, |S(ρ) − f (T0 )| < ε. Finally, Tr (T0 ) is estimated as
 
1
≤
Tr (T0 ) =
log
log
k
k
pi ≥k
pi ≥k
 
 
1
1
= 2r log d + r log
≤ r log
k
ε
 
1
.
= 2r n + r log
ε


p 
i



This implies that there exists a positive Hermitian matrix T0 such that Tr(T0 ) =

O(r n+r log 1ε ) and |S (ρ) − f (T0 )| < ε.

Appendix B Details on numerical simulations
To support our observations, we explain the details of the numerical simulations for
estimating the quantum mutual information, which can be expressed as the sum of

123

Estimating quantum mutual information...
Table 1 Estimations of quantum
mutual information using the
QMINE method

Page 15 of 16

57

Rank

QMI

Estimation results

Error-rate (%)

1

1.8048002

1.7946120

0.565

2

1.7631968

1.7493981

0.783

4

1.3031208

1.2902124

0.991

8

0.8440226

0.8376048

0.760

16

0.4172888

0.4163618

0.222

von Neumann entropies as follows:
I (A : B) = S(ρ A ) + S(ρ B ) − S(ρ AB )


= S ρ A ⊗ ρ B − S(ρ AB ).
To obtain quantum mutual information, we adopted an alternative and simple strategy.
By exploiting QMINE (suggested in Sect. 4), we directly estimate S(ρ A ⊗ ρ B ) and
S(ρ AB ). That is, we address S(ρ A ⊗ ρ B ) rather than estimating S(ρ A ) or S(ρ B ). This
method reduces the number of resource copies required for simulations.
We used four-qubit for this simulation and the results of our experiment are summarized in Table 1. To show that QMINE can estimate the quantum mutual information
for various density matrices, we present the results of the estimation, where the rank
of ρ AB is different.

References
1. Jaeger, G.: Quantum Information: An Overview. Springer, New York (2007)
2. Nielsen, M.A., Chuang, I.L.: Quantum Computation and Quantum Information. Cambridge University
Press, Cambridge (2000)
3. Wilde, M.M.: Quantum Information Theory. Cambridge University Press, Cambridge (2017)
4. Bennett, C.H., Shor, P.W.: Quantum Channel Capacities. Science 303, 1784 (2004)
5. Holevo, A.S.: Quantum channel capacities. Quantum Electron. 50, 440 (2020)
6. Biamonte, J., Wittek, P., Pancotti, N., Rebentrost, P., Wiebe, N., Lloyd, S.: Quantum machine learning.
Nature 549, 195 (2017)
7. Carleo, G., Cirac, I., Cranmer, K., Daudet, L., Schuld, M., Tishby, N., Vogt-Maranto, L., Zdeborová,
L.: Machine learning and the physical sciences. Rev. Mod. Phys. 91, 045002 (2019)
8. Bengtsson, I., Życzkowski, K.: Geometry of quantum states: an introduction to quantum entanglement.
Cambridge University Press, Cambridge (2017)
9. O’Donnell R., Wright J.: Efficient quantum tomography. In: Proceeding of the 48th Annual ACM
Symposium on Theory of Computing, pp. 899–912 (2016)
10. Hastings, M.B., González, I., Kallin, A.B., Melko, R.G.: Measuring Renyi entanglement entropy in
quantum Monte Carlo simulations. Phys. Rev. Lett. 104, 157201 (2010)
11. Calabrese, P., Cardy, J., Doyon, B.: Entanglement entropy in extended quantum systems. J. Phys. A:
Math. Theor. 42, 500301 (2009)
12. Gur T., Hsieh M.-H., Subramanian S.: Sublinear quantum algorithms for estimating von Neumann
entropy. arXiv:2111.11139
13. Acharya, J., Issa, I., Shende, N.V., Wagner, A.B.: Estimating quantum entropy. IEEE J. Select. Areas
Inf. Theory 1, 454 (2020)
14. Tan, K.C., Volkoff, T.: Variational quantum algorithms to estimate rank, quantum entropies, fidelity,
and fisher information via purity minimization. Phys. Rev. Res. 3, 033251 (2021)

123

57

Page 16 of 16

M. Shin et al.

15. Wang Y., Zhao B., Wang X.: Quantum algorithms for estimating quantum entropies. arXiv:2203.02386
16. Wang Q., Guan J., Liu J., Zhang Z., Ying M.: New Quantum Algorithms for Computing Quantum
Entropies and Distances. arXiv:2203.13522
17. Gilyén A., Li T.: Distributional property testing in a quantum world. arXiv:1902.00814
18. Subramanian, S., Hsieh, M.-H.: Quantum algorithm for estimating α-Renyi entropies of quantum
states. Phys. Rev. A 104, 022428 (2021)
19. Von Neumann, J.: Mathematische grundlagen der quantenmechanik. Springer, New York (1996)
20. Beer, K., Bondarenko, D., Farrelly, T., Osborne, T.J., Salzmann, R., Scheiermann, D., Wolf, R.: Training
deep quantum neural networks. Nat. Commun. 11, 808 (2020)
21. Wan, K.H., Dahlsten, O., Kristjánsson, H., Gardner, R., Kim, M.S.: Quantum generalisation of feedforward neural networks. NPJ Quantum Inf. 3, 36 (2017)
22. Benedetti, M., Lloyd, E., Sack, S., Fiorentini, M.: Parameterized quantum circuits as machine learning
models. Quantum Sci. Technol. 4, 043001 (2019)
23. McClean, J.R., Boixo, S., Smelyanskiy, V.N., Babbush, R., Neven, H.: Barren plateaus in quantum
neural network training landscapes. Nat. Commun. 9, 4812 (2018)
24. Goldfeld Z., Patel D., Sreekumar S., Wilde M.: Quantum neural estimation of entropies.
arXiv:2307.01171
25. Shannon C.E.: A mathematical theory of communication. Bell Syst. Tech. J. 27, 379 & 623 (1948)
26. Belghazi M.I., Baratin A., Rajeswar S., Ozair S., Bengio Y., Courville A., Hjelm R.D., MINE: Mutual
Information Neural Estimation. arXiv:1801.04062
27. Donsker, M.D., Varadhan, S.R.S.: Asymptotic evaluation of certain Markov process expectations for
large time–III. Commun. Pure Appl. Math. 29, 389 (1976)
28. Mitarai, K., Negoro, M., Kitagawa, M., Fujii, K.: Quantum circuit learning. Phys. Rev. A 98, 032309
(2018)
29. Rebentrost, P., Mohseni, M., Lloyd, S.: Quantum support vector machine for big data classification.
Phys. Rev. Lett. 113, 130503 (2014)
30. Havlíček, V., Córcoles, A.D., Temme, K., Harrow, A.W., Kandala, A., Chow, J.M., Gambetta, J.M.:
Supervised learning with quantum-enhanced feature spaces. Nature 567, 209 (2019)
31. Huber A.: Variational Principles in Quantum Statistical Mechanics. Mathematical Methods in Solid
State and Superfluid Theory: Scottish Universities Summer School, pp. 364–392 (1968)
32. Liu, J.-G., Mao, L., Zhang, P., Wang, L.: Solving quantum statistical mechanics with variational
autoregressive networks and quantum circuits. Mach. Learn. Sci. Technol. 2, 025011 (2021)
33. Harrow, A.W., Napp, J.C.: Low-depth gradient measurements can improve convergence in variational
hybrid quantum-classical algorithms. Phys. Rev. Lett. 126, 140502 (2021)
Publisher’s Note Springer Nature remains neutral with regard to jurisdictional claims in published maps
and institutional affiliations.

123

