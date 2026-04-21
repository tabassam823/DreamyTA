Quantum annealing: an
overview
royalsocietypublishing.org/journal/rsta

Atanu Rajak1 , Sei Suzuki2 , Amit Dutta3 and
Bikas K. Chakrabarti4,5

Review

1 Department of Physics, Presidency University, Kolkata 700073, India

Cite this article: Rajak A, Suzuki S, Dutta A,
Chakrabarti BK. 2022 Quantum annealing: an
overview. Phil. Trans. R. Soc. A 381: 20210417.
https://doi.org/10.1098/rsta.2021.0417

Moroyama, Saitama 350-0495, Japan
3 Indian Institute of Technology Kanpur, Kanpur 208016, India
4 Saha Institute of Nuclear Physics, 1/AF Bidhannagar,
Kolkata 700064, India
5 Indian Statistical Institute, 203 B. T. Road, Kolkata 700108, India

Received: 4 July 2022
Accepted: 22 August 2022
One contribution of 12 to a theme issue
‘Quantum annealing and computation:
challenges and perspectives’.
Subject Areas:
quantum physics, statistical physics,
quantum computing
Keywords:
quantum tunnelling, transverse Ising models,
quantum spin glass, p-spin models,
decoherence, non-deterministic
polynomial-time (NP)-complete and NP-hard
problems
Author for correspondence:
Atanu Rajak
e-mail: atanu.physics@presiuniv.ac.in

2 Department of Liberal Arts, Saitama Medical University,

AR, 0000-0002-0371-1153; SS, 0000-0002-3235-9910
In this review, after providing the basic physical
concept behind quantum annealing (or adiabatic
quantum computation), we present an overview
of some recent theoretical as well as experimental
developments pointing to the issues which are still
debated. With a brief discussion on the fundamental
ideas of continuous and discontinuous quantum
phase transitions, we discuss the Kibble–Zurek scaling
of defect generation following a ramping of a
quantum many body system across a quantum
critical point. In the process, we discuss associated
models, both pure and disordered, and shed light
on implementations and some recent applications
of the quantum annealing protocols. Furthermore,
we discuss the effect of environmental coupling on
quantum annealing. Some possible ways to speed
up the annealing protocol in closed systems are
elaborated upon: we especially focus on the recipes
to avoid discontinuous quantum phase transitions
occurring in some models where energy gaps vanish
exponentially with the system size.
This article is part of the theme issue ‘Quantum
annealing and computation: challenges and
perspectives’.

1. Introduction
Following the recent technological advance in
manipulation of a quantum state, the notion of quantum
computation and simulation which initially stemmed
2022 The Author(s) Published by the Royal Society. All rights reserved.
Downloaded from http://royalsocietypublishing.org/rsta/article-pdf/doi/10.1098/rsta.2021.0417/1326707/rsta.2021.0417.pdf
by guest
on 21 April 2026

(1.1)

where A(t) and B(t) are the scheduling function satisfying A(ti )  B(ti ) at the initial time ti and
A(tf )  B(tf ) at the final time tf so that H(t) interpolates between HD at t = ti and HP at t = tf .
The initial state at t = ti is set at the ground state of HD ≈ H(ti )/A(ti ). If the change in H(t) with
t is ‘sufficiently’ small, the spin state evolves adiabatically (i.e. stays in the ground state of the
instantaneous Hamiltonian) and arrives at the ground state of HP at t = tf which we seek. This
constitutes the basic notion of the QA, also known as the adiabatic quantum computation [4–10].
Throughout this paper, we shall employ QA scheme using the transverse Ising Hamiltonian (if not
otherwise mentioned). To illustrate, we consider the following Hamiltonian with ferromagnetic
nearest-neighbour interactions in one dimension:


z
σjz σj+1
−Γ
σjx ,
(1.2)
H = −J
j

j

where J denotes the strength of the interaction and Γ is the strength of the non-commuting


z . The transverse field Γ is annealed
transverse field. Here HD = − j σjx and HP = − j σjz σj+1
to reach the ground state of HP from the ground state of HD .
The success of QA is determined by how slowly the Hamiltonian changes with time.
According to the adiabatic theorem of quantum mechanics, the criterion of the adiabatic time
evolution is given by [11]


max |1(t)|(dH(t)/dt)|g(t)|
 1,
(1.3)
min[(t)]2
where |g(t) and |1(t) are the instantaneous ground and first-excited states at time t, respectively,
and (t) denotes the instantaneous energy gap above |g(t). The min and max functions are taken
with respect to the variable t. Thus, roughly speaking, QA works better for larger (t) [12].
As a classical counterpart to QA, simulated annealing (SA) is a known method of computation
for optimization problems [13]. In this method, we prepare the Gibbs–Boltzmann distribution of
HP at sufficiently high temperature by means of the Monte Carlo method and literally anneal the
system down to zero temperature. If annealing is sufficiently slow, then we are expected to arrive
at the ground state of HP with high probability. SA uses the thermal fluctuation for optimization,
which induces the thermal (Arhenius) jump from a local energy minimum to another separated by
an energy barrier. The escape rate from a local minimum over the energy barrier with height h is
given by e−h/kB T , where kB and T denote the Boltzmann constant and the temperature. Assuming
Downloaded from http://royalsocietypublishing.org/rsta/article-pdf/doi/10.1098/rsta.2021.0417/1326707/rsta.2021.0417.pdf
by guest
on 21 April 2026

...............................................................

H(t) = A(t)HD + B(t)HP ,

2

royalsocietypublishing.org/journal/rsta Phil. Trans. R. Soc. A 381: 20210417

from pure theoretical concepts has now spread to flourish an industry with an immense
possibility of technological applications. In particular, studies of quantum annealing (QA) have
gained a tremendous momentum since programmable QA machines, dubbed as quantum
annealers, with more than thousands of qubits realized and commercialized. In this review,
having provided an overview of QA protocol, we discuss some recent theoretical and
experimental developments of the QA exploiting the advantage of using quantum tunnelling
in finding the minimum of a classical energy function.
QA is usually aimed at seeking the ground state of a generic Ising model, which may contain
random biases and/or random many-body interactions [1–3]. Many optimization problems
including the travelling salesman problem, job scheduling problem, knapsack problem, and so
on, are shown to reduce to this problem. Therefore, the application of QA extends from physics
to our daily life. This broadness of application is another reason why QA has attracted much
attention in industry. Now, let us consider an Ising model denoted by the Hamiltonian HP , where
the subscript P stands for the problem Hamiltonian. We assume that HP is a classical many-body
Ising Hamiltonian described in terms of the z components of the Pauli operator {σjz }. We further
introduce a driver Hamiltonian HD which is not commutative with HP and has the trivial ground

state. A simple choice for HD is the transverse field: HD = − j σjx , so that HD does not commute
with HP . The total Hamiltonian of QA is given as

QA
w
spin configuration

Figure 1. Schematic picture of the thermal fluctuation and quantum tunnelling in a system with local energy minima separated
by an energy barrier with the height h and the width w.

that h is proportional to the system size N, this suggests that an exponentially long time in N is
necessary to reach the global energy minimum by SA.
In contrast to SA, quantum tunnelling induces an escape from a local minimum through an
energy barrier,
as shown schematically in figure 1. The tunnelling probability is approximately
√
given by e− hw/g [14,15], where g denotes the strength of quantum fluctuation, which corresponds
to the transverse field Γ in transverse Ising models. Therefore, assuming the height h ∼ O(N)
and the width w < O(N1/2 ), the time necessary to escape from a local minimum due to quantum
tunnelling is subexponential in N. For such a system, quantum tunnelling helps the system to
equilibrate even though the system is glassy, i.e. non-ergodic in the absence of the quantum
fluctuation, leading to a potential advantage of QA over SA in glassy systems. This role of
quantum tunnelling was first discussed by Ray et al. in 1989 [16] (see discussions in [17] in this
regard) in the context of the restoration of the replica symmetry or ergodicity due to quantum
fluctuation in the quantum version of the Sherrington–Kirkpatrick model [18], which is detailed
in the next section. Although the existence of an energy landscape with thin and high barriers in
specific models is still an issue of debate, it must be a foundation for the speedup of QA over SA
[17,19]. In addition, several numerical and experimental studies have provided evidence for such
an advantage of QA over SA in some specific models, as shown in §§1b(i) and 2. We show a brief
time-line for the development of QA in figure 2.
The review is organized in the following fashion: having discussed the basic idea behind the
QA scheme and the results for various models in the context of annealing and defect generation
especially for annealing across a quantum critical point in §1, we move to discuss various
implementations of annealing protocols in §2. In §3, we probe how does coupling to an external
environment influence the QA process. In §4, we again refer to the closed systems and discuss
possible ways to speed QA processes, especially in the context of avoiding discontinuous phase
transitions. Some recent applications are discussed in §5.

(a) Quantum phase transition and quantum annealing
The minimum gap min[(t)] appearing in equation (1.3) often decreases with increasing the
number of spins. In general, the energy gap vanishes at a quantum phase transition (QPT) because
a QPT separates disordered and ordered phases and the ground state is degenerate at a transition.
Let us consider the transverse Ising Hamiltonian introduced in equation (1.2). The initial state, for
Γ  J, is given by the ground state of the transverse field, in which all spins are aligned along the
x-axis of spin. This is a disordered state where the ground-state averaged magnetization in the
z-direction of spin is zero, i.e. σiz  = 0. The targeted ground state of the Ising Hamiltonian for
Γ = 0, however, is an ordered state in the sense that it has a fixed magnetization +1 or −1 for each
σjz . This implies that the system encounters a QPT during QA. Indeed, the model in equation (1.2)
Downloaded from http://royalsocietypublishing.org/rsta/article-pdf/doi/10.1098/rsta.2021.0417/1326707/rsta.2021.0417.pdf
by guest
on 21 April 2026

...............................................................

h

3

royalsocietypublishing.org/journal/rsta Phil. Trans. R. Soc. A 381: 20210417

energy

SA

1989

Ray et al. [16] proposed
that quantum fluctuations
could help explore the
rugged (free) energy
landscapes of the
Sherrington–Kirkpatrick
spin glasses and search
the ground state(s) by
escaping from local
minima (having tall but
thin barriers) using
tunnelling.

1991

1994

Finnila et al. [1]
reported a successful
computational search
of the minima (ground
state) of a
multidimensional
energy landscape (in
the context of large
molecules) using
quantum annealing.

Farhi et al. [3] proposed the
methodology of quantum
adiabatic computation in the
context of NP-hard problems.
Brooke et al. [85]
reported their first
experimental
demonstration of
quantum annealing
and its advantages
in LiHoYF Ising
glass magnets.

1998

1999

2000

Kadowaki &
Nishimori [2]
first formulated and
numerically
demonstrated clearly
the computational
advantages in Ising
glass-like mixed
magnetic models.

Santoro et al.
[79] reported on
the study of
quantum
annealing in
Ising spin
glasses and showed
that the residual energy
decreases faster with a
larger power (than in
the classical case) of
the inverse annealing
time.

2002

2011

Johnson et al. [88]
reported on the
remarkable
development and
functioning of a
Josephson-JunctionCoupled circuit
quantum Ising spin glass
annealing machine, built
and later marketed by DWave Systems.

Figure 2. A brief time-line for the development of quantum annealing. (Online version in colour.)

has QPTs at Γ /J = ±1. The finite size scaling of the energy gap at QPT depends on the character
of the associated QPT, and the latter is determined by the property of the Ising Hamiltonian.
The character of a conventional continuous QPT is specified by critical exponents [20–23].
The size scaling of the energy gap at a quantum critical point is given as c ∼ L−z where L
denotes the linear size of the system and the exponent z, known as the dynamical exponent,
characterizes the associated quantum critical point (QCP). Therefore, the time for QA to work
scales polynomially with the system size. However, apart from this simple situation, the
polynomial scaling of the energy gap at QPT is not always true. In fact, a discontinuous QPT
usually gives rise to an exponential scaling with the system size. This can be understood
phenomenologically as follows. Consider a quantum many-body system and focus on the two
lowest energy levels. We assume that higher energy levels are highly separated from them. The
effective Hamiltonian is then written as


εA 
,
H=
 εB
where εA and εB correspond to the energies of the two local minima, and  denotes the
tunnelling energy between these two states. Figure 3 shows the energy levels of this Hamiltonian
schematically. The discontinuous QPT corresponds to the change of the lowest energy level
between A and B. The transition takes place where the bare energies εA and εB of two levels
are degenerate. The energy gap at the transition is given by the twice of the tunnelling energy
, and  is given by an exponential of the Hamming distance between the states A and B. Note
that the Hamming distance is the number of sites at which the spin orientation along the z-axis is
different. Usually this distance increases linearly with the system size. Therefore, the energy gap
at a transition decays exponentially with the system size. Since the discontinuous QPT hinders
QA, several ways to avoid the discontinuous QPT have been proposed. We will mention some of
them in §4.
Downloaded from http://royalsocietypublishing.org/rsta/article-pdf/doi/10.1098/rsta.2021.0417/1326707/rsta.2021.0417.pdf
by guest
on 21 April 2026

4
...............................................................

1981

Wu et al. [84]
reported supporting
evidence for rapid
decrease in
characteristic
relaxation times to
reach the ground
state in LiHoYF
dipolar (Ising) glass
due to the effective
quantum tunnelling in
the system.

royalsocietypublishing.org/journal/rsta Phil. Trans. R. Soc. A 381: 20210417

Chakrabarti [47]
introduced the
transverse field Ising
spin glass model and
reported the first
study of the quantum
phase transition
behaviour of the
Mattis (unfrustrated)
and the Edwards–
Anderson (frustrated)
Ising Spin glass
models in transverse
field.

A

(1)

(3)

5

B
B

(1)

A

(2)

(3)

B

A
B

A

Figure 3. Schematic picture for an interchange of two energy levels. εA and εB corresponds to the energies of the two local
minima. (1), (2) and (3) show the situations with εA  εB , εA = εB , and εA  εB , respectively. In the case (2) with εA = εB ,
the energy gap is given by the twice of the tunnelling energy  between the states A and B.

QA across a QPT is closely related to the Kibble–Zurek mechanism of defect generation
following an annealing across a QCP [24–30]. The system starting from the initial disordered
ground state evolves adiabatically as far as the characteristic time of the instantaneous ground
state (i.e. the inverse of the gap) is shorter than the annealing speed. However, on approaching a
QPT, the characteristic time grows and hence the dynamics becomes non-adiabatic in the vicinity
of the QCP. The state of the system after the passage through the QCP is no longer the ground
state, rather a state with topological defects. The residual energy density, εres , i.e. the excess energy
over the expected final ground state at the end of the QA is a monotonically decreasing function of
the annealing duration τ . In case of a linear annealing through a conventional continuous QPT in
a d-dimensional many-body system with the critical exponent ν for the correlation length and the
dynamical exponent z, Kibble–Zurek scaling of the residual energy is given by εres ∼ τ −dν/(zν+1)
as far as the system after annealing is in a gapped phase. The scaling of the residual energy
density is modified from the Kibble–Zurek scaling for other unconventional continuous QPTs or
discontinuous QPTs and when the annealing protocol involves a nonlinear variation of the tuning
parameter [30–32]. The scaling of the residual energy together with the scaling of the energy gap
at QPT is an important measure that characterizes the property of QA [33,34].

(b) Transverse Ising models
Assuming the transverse field Hamiltonian as HD , the total Hamiltonian of QA forms the
transverse Ising models (TIMs). We briefly review properties of some representative TIMs in this
subsection [24–27].

(i) Pure and disordered transverse Ising chain
As the simplest case, we first consider the pure ferromagnetic one-dimensional TIM (1dTIM)
given by equation (1.2). There are two phases of the ground state in this model separated by
a quantum phase transition at Γ /J = 1. The ground state is disordered for Γ /J > 1, while it is
ferromagnetically ordered for Γ /J < 1. At the critical point Γ /J = 1, the energy gap above the
ground level vanishes as the system size L → ∞. The scaling of the energy gap with the linear
size L at the critical point is given by  ∼ L−1 . Critical exponents of the correlation length and the
dynamical exponent are ν = 1 and z = 1, respectively.
Downloaded from http://royalsocietypublishing.org/rsta/article-pdf/doi/10.1098/rsta.2021.0417/1326707/rsta.2021.0417.pdf
by guest
on 21 April 2026

...............................................................

2

royalsocietypublishing.org/journal/rsta Phil. Trans. R. Soc. A 381: 20210417

energy

(2)

j

j

where Jj is a random ferromagnetic coupling and hi is a random transverse field obeying
distributions πJ (J) and πh (h), respectively. The phase transition of this model happens
when [log J]av = log Γ + [log h]av , where [· · · ]av denotes the random average. The ground
state is ferromagnetically ordered for Γ < exp([log J]av − [log h]av ), and disordered for Γ >
exp([log J]av − [log h]av ) [36–39]. The phase transition is characterized by the infinite randomness
fixed point, where the dimensionless parameter appearing in √the distribution of the energy gap
√
 is (− log )/ L, implying that the energy gap scales as e−C L , where C is a positive constant.
Therefore, even though the ground state of this model with Γ = 0 is trivial, the dynamics of QA to
this state across the quantum phase transition is highly non-trivial. The size scaling of the typical
gap suggests that the time to arrive at the target state by QA scales as subexponential with L. In
connection to the Kibble–Zurek scaling, Dziarmaga and Caneva et al. reported that the density of
kinks produced after QA scales as
1
(1.6)
[ρkink ]av ∼
log2 ατ
with an O(1) constant α [40,41]. Thus, the defect density decays in a logarithmically slow
fashion with the annealing time τ which we reiterate makes QA difficult. However, it has been
reported that SA for the one-dimensional disordered Ising model (i.e. equation (1.5) with Γ = 0)
yields [ρkink ]av ∼ 1/ log α τ , where α is a constant, which decays slower than equation (1.6) [42].
Therefore, this model reveals an evident advantage of QA over SA.

(ii) Pure transverse Ising model in higher dimensions
The two-dimensional TIM (2dTIM) may be the simplest model next to 1dTIM, though unlike
the 1d case, the 2d model is not integrable. The equilibrium properties of the 2dTIM have been
studied numerically and some thermodynamic properties including the character of quantum
and thermal phase transitions are available. Recently Schmitt et al. carried out a numerical study
of QA in 2dTIM in the context of the Kibble–Zurek scaling using state-of-the-art numerical
methods [43]. Their results are consistent with the Kibble–Zurek prediction. Study of out-ofequilibrium dynamics of a two-dimensional quantum system will be a direction of study in the
near future.
The situation becomes simpler in the infinite dimension. The pure TIM in the infinite
dimension is written as

J  z z
σj σk − Γ
σjx ,
(1.7)
H=−
N
j<k

j

where N denotes the number of spins. Note that each spin interacts with all the other spins with

an equal strength. Defining the total spin operator as S = (1/2) N
j=1 σ j , this Hamiltonian can be
Downloaded from http://royalsocietypublishing.org/rsta/article-pdf/doi/10.1098/rsta.2021.0417/1326707/rsta.2021.0417.pdf
by guest
on 21 April 2026

...............................................................

in the thermodynamic limit L → ∞. We recall that the residual energy is defined as the excess
energy that is the difference of the energy expectation value of H(t = 0) with respect to the evolved
state at t = 0 from the ground energy of H(t = 0). According to the Kibble–Zurek scaling with
ν = z = 1, one has εres ∼ τ −1/2 consistent with equation (1.4).
The disordered version of 1dTIM is given by


z
Jj σjz σj+1
−Γ
hj σjx ,
(1.5)
H=−

6

royalsocietypublishing.org/journal/rsta Phil. Trans. R. Soc. A 381: 20210417

The scaling of the defect density following a QA of the pure 1dTIM was solved exactly by
Dziarmaga [35]. Let us assume Γ = −tJ/τ with the parameter τ which denotes the inverse of
the annealing speed. Using the periodic boundary condition in equation (1.2), and applying
the Jordan–Wigner transformation followed by the Fourier transformation, the quantum time
evolution of the spin state is reduced to decoupled Landau–Zener models of two-level systems
for each momentum mode [22,23]. When the time t is varied from −∞ to 0, with the initial state
chosen to be the ground state of the initial Hamiltonian, the residual energy per spin at the final
time t = 0 is found to be of the form
1
1
(1.4)
εres = 
π 2Jτ/h̄

arranged into
J
J 2
Sz − 2Γ Sx + .
(1.8)
N
2
In the thermodynamic limit, this model undergoes a continuous QPT at Γ = J. The energy gap
above the ground state behaves as [(Γ − J)Γ ]1/2 for Γ ≥ J and the size scaling of the energy gap
at Γ = 1 is c ∼ N−1/3 [44]. Introducing the effective dimension deff so that the system size N is
tied to the linear size L by Ldeff = N, one has relations between critical exponents as zν = 1/2 and
z/deff = 1/3. Then, assuming z = 1 as in pure TIMs with finite dimension, one obtains ν = 1/2 and
deff = 3. Caneva et al. studied QA of the present model and obtained εres ∼ τ −1/3 . This scaling is
inconsistent with the Kibble–Zurek scaling, since the latter predicts τ −1 . Acevedo et al. revealed
that there is an anomaly in the transition amplitude between the ground and excited states in the
present model [45]. Therefore, the naive phenomenological argument to derive the Kibble–Zurek
scaling does not apply to the system in infinite dimension. We shall also discuss an extension of
the Hamiltonian (1.7) to the p-body interacting model in §4 and argue that the QA does not work
in this model with odd p.

7

H = −2

jk

j

where jk stands for nearest-neighbour pairs and Jjk are independent random variables. The
order parameter of a spin glass is defined in terms of the spin overlap between different replicas.
Supposing that σjα,a denotes the spin operator for a replicated system labelled by a, the overlap

z,1 z,2
operator between replicas a = 1 and a = 2 is defined by R1,2 = (1/N) N
i=1 σj σj . The order
parameter is then given by q = [R1,2 ]av . The spin glass order is characterized by q > 0 with zero

z
magnetization m = 0, where the magnetization is defined by m = [(1/N) N
i=1 σj ]av . This means
that the spin configuration is spatially random but frozen. Rieger et al. [48] and Guo et al. [49]
investigated the character of QPTs of this model with the Gaussian distribution of Jjk with zero
mean and unit variance in square and cubic lattices, respectively, by means of the quantum Monte
Carlo (QMC) simulation. Singh & Young [50] studied the ±J model, where Jkj takes +1 or −1 with
equal probability for dimensions up to d = 8 using the linked cluster expansion to determine
the location of the QCP. Subsequently, QPTs of these models were reconsidered by Miyazaki &
Nishimori [51] and by Matoz-Fernandez & Romá [52] using the real-space renormalization group
and the QMC with parallel-tempering, respectively. They concluded that the QPTs in transverse
Ising spin glasses in two and three dimensions were compatible with the infinite randomness
fixed point with the critical exponents ν and ψ, where ψ specifies the activation type of size
scaling of the energy gap as [log ]av ∼ Nψ/d [53–57]. The estimated exponents for the Gaussian
model were ν ≈ 1.2 and ψ ≈ 0.44 in two dimensions [51,52] and ν ≈ 0.94 in three dimensions [51].
The Hamiltonian of the transverse Ising spin glass in infinite dimension, i.e. the quantum
Sherrington–Kirkpatrick (SK) model, is written as [16]
N


1
Jjk σjz σkz − Γ
σjx .
H = −√
N 1≤j<k≤N
j=1

(1.10)

The classical SK model in the absence of the transverse field unveiled the existence of the socalled replica symmetry breaking (RSB) in the spin glass phase [58,59], where the overlap R1,2
has a dispersed continuous distribution in the thermodynamic limit. Ray et al. [16] conjectured
on the basis of the QMC simulation the collapse of a continuous distribution for the classical SK
model into a delta function in the presence of any amount of the transverse field, which paved
the way for using quantum tunnelling in finding the global minimum or ground state of the SK
spin glass model. In the classical model, due to random interactions between spins at different
Downloaded from http://royalsocietypublishing.org/rsta/article-pdf/doi/10.1098/rsta.2021.0417/1326707/rsta.2021.0417.pdf
by guest
on 21 April 2026

...............................................................

The Hamiltonian of the Edwards–Anderson [46] version of the transverse Ising spin glass,
introduced by Chakrabarti in 1981 [47], is written as


Jjk σjz σkz − Γ
σjx ,
(1.9)
H=−

royalsocietypublishing.org/journal/rsta Phil. Trans. R. Soc. A 381: 20210417

(iii) Transverse Ising spin glass

The satisfiability problem is known as one of the basic combinatorial optimization problems
in computer science. Given the number of bits and constraints among bits, the problem is
to determine whether the bit configuration satisfying all the constraints exists or not. In the
Downloaded from http://royalsocietypublishing.org/rsta/article-pdf/doi/10.1098/rsta.2021.0417/1326707/rsta.2021.0417.pdf
by guest
on 21 April 2026

...............................................................

(c) Transverse Ising model for satisfiability

8

royalsocietypublishing.org/journal/rsta Phil. Trans. R. Soc. A 381: 20210417

lattice sites, such systems have many local minima in free energy which are separated by large
energy barriers of order O(N), where N is the system size [59]. This induces non-ergodicity in the
system and eventually breaks the replica symmetry of the system. As a result, finding the ground
state or global minimum of such systems is a very hard problem; for the SK spin glass model,
it turns out to be NP (non-deterministic polynomial-time) hard. The system indeed gets trapped
into one of the local minima inside the spin glass phase, due to the highly rugged nature of freeenergy landscape. This leads to a broad order parameter distribution in the spin glass phase [58].
In addition to a peak value of the order parameter distribution, it is extended up to the zero value
of the order parameter even in the thermodynamic limit.
It seems that the scenario may change drastically when a transverse field is applied on the
SK spin glass [16]. The presence of quantum fluctuations induces ergodicity in the system, since
quantum tunnelling becomes possible between the local minima separated by tall and narrow
free-energy barriers. This indicates the restoration of RSB for the quantum SK spin glass model.
As a result, the order parameter distribution should be sharply peaked at a point for the quantum
SK model in the thermodynamic limit. This ergodic behaviour of the quantum SK model is
responsible for the advantage in quantum annealing in comparison with SA.
This conjecture was criticized by Young [60] by solving numerically the effective onedimensional model to which the quantum SK model can be mapped in the N → ∞ limit; this
work predicted that the replica symmetric solution is unstable down to zero temperature. On
the contrary, Mukherjee et al. [61] explored the behaviour of the order parameter distribution
of the quantum SK model in the spin glass phase using the Monte Carlo technique for the
effective Suzuki–Trotter Hamiltonian at finite temperatures (see equation (2.1) discussed later)
and the exact diagonalization method at zero temperature. It has been found that there exists
a low temperature regime in the spin glass phase, where the order parameter distribution
becomes peaked around its most probable value in the thermodynamic limit, thus suggesting
the ergodic behaviour. On the other hand, the order parameter distribution remains Parisi type
in high temperature regime, which indicates the non-ergodic behaviour of the system in this
part of the spin glass phase. These two regions of the spin glass phase are separated by a
boundary connecting the zero temperature-zero transverse field point and the quantum-classical
crossover point on the phase boundary [61,62]. In addition, quantum annealing has also been
investigated for the quantum SK model using Suzuki–Trotter Hamiltonian dynamics in both the
ergodic and non-ergodic regimes. The average annealing time was estimated, when both the
temperature and the transverse-field were annealed down to some fixed low values, starting
from the paramagnetic phase. It was found that the average annealing time is independent
of the system size when the annealing is performed through the ergodic (quantum fluctuation
dominated) region, whereas it grows strongly with the system size when the annealing is carried
out through the non-ergodic (classical fluctuation dominated) region. This suggests that quantum
annealing has the potential to detect whether a phase is ergodic or non-ergodic. Also, the average
annealing time to approach a same ground state is small for annealing through the ergodic regime
compared with that through the non-ergodic regime. The QA for SK spin glass is also studied by
tuning both transverse and longitudinal fields, and it has been shown that this protocol exhibits
some effectiveness compared with the QA by varying the transverse field only [63].
Recently, Leschke et al. [64] proved rigorously non-zero variance of the overlap in the
thermodynamic limit of the quantum SK model at sufficiently low temperature with a small but
finite transverse field. Their study reveals a dispersed distribution of the overlap, therefore the
existence of RSB. However the controversy about the continuous distribution of the overlap in
the quantum SK model is still an open problem [65].

M


(σizm + σjzm + σkzm − 1)2 − Γ

m=1

N


σjx .

(1.11)

j=1

If one arrives at the exact ground state for Γ = 0, by annealing the field Γ , then one can solve the
Exact Cover. However, the Exact Cover is an NP-complete problem which no known algorithm
can solve in a time polynomial in N. Young et al. [66] studied equation (1.11) by means of the
QMC method. They found that some instances of the model show a discontinuous first-order
QPT with an exponentially small energy gap and the fraction of such instances grows toward
unity with increasing N. Jörg et al. [67] also reported occurrence of a first-order QPT in the random
3-XORSAT problem, which is another variant of the 3-SAT.

2. Implementation of quantum annealing
Implementing QA is a challenging task, since one needs to evolve a many-spin state under a
quantum many-body Hamiltonian. In this section, we review results from numerical simulation
using real-time dynamics as well as Monte Carlo dynamics, and from quantum simulations using
hardware.

(a) Results from numerical simulation for real-time dynamics
The real-time evolution of a quantum system governed by the Schrödinger equation can be
computed in general by solving a linear differential equation. However, since the number of
unknown functions of time increases as 2N with the number of spins, the system size acceptable
to a conventional computer is limited to N ∼ O(10). Kadowaki & Nishimori [2] reported in the
seminal paper that QA yields better solutions than the classical SA on the basis of their simulation
for eight spin systems of a frustrated model and the SK model. Farhi et al. [3] reported the
numerical result for the Exact Cover problem with the number of spins up to 20. The numerical
result suggested a quadratic scaling of the runtime in QA with respect to the number of spins.
However, this scaling should turn into an exponential one for larger size as shown by the QMC
study for the energy gap [66].
Restricted to systems in one dimension, there are efficient methods of numerical simulation for
real-time evolution. In the case of 1dTIMs without the longitudinal field, irrespective of disorder,
the Schrödinger equation of the spin state reduces to the Bogoliubov–de Gennes equation of
2N unknown functions of time through the Jordan–Wigner’s fermionization and the Bogoliubov
transformation [68]. Generic 1dTIMs with longitudinal fields cannot be mapped to free fermion
models. However, time evolution of generic 1dTIMs can be simulated using the time-dependent
density matrix renormalization group (tDMRG) proposed by White & Feiguin [69] or the time
evolving block decimation (TEBD) by Vidal [70]. In addition, the infinite system of 1dTIMs with
no disorder can be simulated using an infinite method of TEBD (iTEBD) [71]. These methods serve
the study of QA in 1dTIM with a uniform or disordered longitudinal field [72,73].

Downloaded from http://royalsocietypublishing.org/rsta/article-pdf/doi/10.1098/rsta.2021.0417/1326707/rsta.2021.0417.pdf
by guest
on 21 April 2026

...............................................................

H=

9

royalsocietypublishing.org/journal/rsta Phil. Trans. R. Soc. A 381: 20210417

case of 3-satisfiability problems, or 3-SATs in short, each constraint involves three bits drawn
randomly. Using the spin language, a constraint for three spins Si , Sj and Sk taking the
values ±1 can be represented as (Si + Sj + Sk − 1)2 , for instance. This vanishes and is called
satisfied when two of the three spins are +1 and the other spin is −1, otherwise it gives
a non-zero and positive value. The Exact Cover, a variant of the 3-SAT, consists of M such
constraints for N spins, and thus the corresponding quantum model that needs to be annealed is
given by

S1,3
S1,2
S1,1 S2,1 S3,1

SN,1

1dTIM
spatial direction
2d Ising model

Figure 4. Schematic picture of the Suzuki–Trotter mapping. A 1dTIM is mapped to a two-dimensional classical Ising model on
the square lattice. The additional dimension corresponds to the time. Sj,m denotes an Ising-spin variable at spatial site j and
temporal site m. (Online version in colour.)

(b) Results from numerical simulation for Monte Carlo dynamics
A d-dimensional TIM in finite temperature (denoted by β −1 ) with spin-spin coupling Jjk and
transverse field Γ can be mapped to a (d + 1)-dimensional classical Ising model by the Suzuki–
Trotter mapping [74,75]. The resulting Hamiltonian Heff is given by
Heff = −

M 

Jjk
m=1 j<k

M

βΓ  
1
log coth
Sj,m Sj,m+1 ,
2β
M
N

Sj,m Sk,m −

M

(2.1)

j=1 m=1

where β is the inverse temperature, M is the Trotter number, Sj,m denotes the spin variable
with the spatial site j and temporal site m taking values ±1, and we defined the sign of Jjk
according to equation (1.9). In figure 4, we schematically illustrate the mapping of 1dTIM into
a (1 + 1)-dimensional classical Ising model. One can simulate in principle any TIM in and out of
equilibrium using this effective Hamiltonian and the Monte Carlo method. This method is called
the QMC method. Although the number β/M controls the accuracy of QMC, the cluster-update
method invented by Swendsen and Wang along the temporal direction enables to have β/M → 0
[76,77]. QMC is known to give rise to the sign problem and fail when the model involves the
frustration. However, QMC for TIM is free from the sign problem. Therefore, QMC is a powerful
method of classical computation in simulating TIM.
QA can be implemented in QMC by regarding the Monte Carlo step as time. The dynamics
realized by QMC is not the quantum dynamics governed by the Schrödinger equation but the
stochastic one. However, QA with QMC serves the purpose of solving an optimization problem
using a classical computer [78]. Several works have shown so far that QA with QMC works in
variety of optimization problems, such as two-dimensional Ising spin glass [79,80], travelling
salesman problem [81] and 3-SATs [82]. Figure 5 shows comparison between QA by QMC and SA
in the two-dimensional spin glass model [83]. This result implies outperformance of QA over SA.
Although an opposite result has been reported for harder 3-SAT problems [82], numerical studies
using QMC suggest that there are problems for which QA is potentially advantageous over SA
due to the restoration of ergodicity by quantum fluctuation [16].

(c) Results from quantum simulation using hardware
The most efficient way to perform QA is to use a quantum magnetic material which realizes
a TIM with a temporally controllable transverse field. LiHox Y1−x F4 is a material that models a
disordered Ising model and it also realizes a disordered TIM by application of the magnetic field
Downloaded from http://royalsocietypublishing.org/rsta/article-pdf/doi/10.1098/rsta.2021.0417/1326707/rsta.2021.0417.pdf
by guest
on 21 April 2026

...............................................................

spatial direction

10

royalsocietypublishing.org/journal/rsta Phil. Trans. R. Soc. A 381: 20210417

temporal direction

S1,M

11

(ln W)–2

0.01
QA
(ln W)–3
0.001
100

1000
10 000
Monte Carlo step

100 000

Figure 5. Comparison of the residual energy between QA by QMC and SA for the two-dimensional spin glass model with
99 × 99 spins with random coupling Jjk from the uniform distribution between −2 and 2. The cluster-flip algorithm in the
imaginary-time direction was used in QMC. SA was started from the initial temperature T = 5.0, while QA was from Γ = 5.0
with T = 0.01. The average was taken over 100 runs for a single instance in SA, and for 16 instances in QA. The decay of the
residual energy in SA is well fitted by (log τ )−2 . As for QA, it is approximated by (log τ )−3 , except for long annealing time
where the decay rate is smaller. (Adapted from [83].) (Online version in colour.)

perpendicular to the easy axis of magnetization [84]. Brooke et al. investigated two protocols, QA
and thermal annealing (TA), using this material with x = 0.44. In QA, the transverse field Γ was
strengthened at high temperature, the system was cooled, and then Γ is weakened to Γf at low
temperature. On the other hand, in TA, the temperature was lowered with keeping Γ = 0, and
then Γ was raised to Γf . In both protocols, the initial and final sets of Γ and temperature were
the same and the durations were the same as well. The ground state at Γf as the target state is a
glassy ferromagnetic state. Brooke et al. [85] reported that the state after QA is much closer to an
equilibrium state than the state after TA. This result implies that QA brings the state to the target
faster than TA. Quite recently Säubert et al., studied QA and TA of the same material and detailed
the dynamical behaviour of the energy landscape during QA. They showed that the transverse
field applied in QA induced random longitudinal fields, implying that the energy landscape of
the problem Hamiltonian HP evolved as QA proceeded [86]. This evolving landscape may be an
issue of future work related to QA.
Progress in Rydberg atom experiments enables to use Rydberg atoms as a quantum simulator.
Keesling et al. performed a quantum simulation of a sort of QA using an array of 51
Rydberg aroms. In this simulation, the system is described by the many-body Hamiltonian



H = (Ω/2) i (|gi ri | + h.c.) −  i ni + j<k Vjk nj nk , where |gj  and |rj  denote the ground and
the excited Rydberg states, respectively, of atoms, nj = |rj rj |, and Vjk is the van der Waars
interaction with the strength which decays as 1/|j − k|6 . The model exhibits a QPT, achieved by
tuning the parameter , belonging to the same universality class as that of 1dTIM . Keesling et al.
[87] observed that the Kibble–Zurek scaling for the kink density arising due to the sweeping of
the parameter , turns out to be the very same as that in 1dTIM.
In order to apply QA as a computation to an optimization problem in practice, spin–
spin interactions and longitudinal fields in addition to the transverse field need to be locally
controllable. A Canadian venture company, D-Wave Systems, has developed a quantum
annealing machine named as a quantum annealer, which consists of programmable coupled
superconducting flux qubits and performs QA to various Ising models [88]. The number of qubits
in the latest machine is beyond 5000. This is 100 times larger than the number of qubits in the
current gate-based quantum computer. Denchev et al. [89] benchmarked D-Wave 2X using 100
instances of the weak-strong cluster model with up to 945 spins. Qubits in D-Wave 2X form
the so-called chimera graph with unit cells consisting of eight qubits. In the weak-strong cluster
Downloaded from http://royalsocietypublishing.org/rsta/article-pdf/doi/10.1098/rsta.2021.0417/1326707/rsta.2021.0417.pdf
by guest
on 21 April 2026

...............................................................

SA

royalsocietypublishing.org/journal/rsta Phil. Trans. R. Soc. A 381: 20210417

residual energy per spin

0.1

296

489

681

945

85th
75th
50th

1014

12

1010

1010

QMC
108

108

SA
106

106

104

D-Wave annealing time (s)

1012

104

D-Wave
102
100

200

300

400

500

600

700

800

900

102
1000

problem size (bits)

Figure 6. Comparison of the time to reach the ground state with 99% success probability as a function of the problem size in
D-Wave 2X, SA and QMC. The runtime in SA and QMC is defined by nsweeps NTupdate , where nsweeps is the number of sweeps (one
sweep attempts to update all spins). Tupdate is the single-spin update time for SA and the update time of a spin-cluster along
the temporal direction. It is set as Tupdate = 1/5 ns for SA and 10 × 870 ns for QMC. Data for 50th, 75th and 85th percentile
taken from a set of 100 instances are shown. The error bars represent 95% confidence interval from bootstrapping. (Adapted
from [89]). (Online version in colour.)

model, there are all-all ferromagnetic couplings inside the cell, and half of the spins in a cell
ferromagnatically couple with those in neighbouring cells. In addition, weak longitudinal fields
are applied to spins in a randomly chosen cell, while strong fields anti-parallel to the weak ones
are applied to spins in the other cells. Figure 6 shows the time to reach the ground state with
99% success probability. For D-Wave, this time is defined by 20 µs [log(1 − 0.99)/ log(1 − p)] for
an instance, where the annealing time is fixed at 20 µs and p denotes the success probability to
obtain the ground state estimated from many runs. As for SA and QMC, it is the runtime on a
single processor. Regarding the median from 100 instances, D-Wave 2X is 108 and 107 times faster
than SA and QMC, respectively.

Boixo et al. [90] tested D-Wave’s quantum annealer to a spin glass model HP = − jk Jjk σjz σkz ,
where Jjk is chosen randomly from J = ±1, with N = 108 spins and reported that the results of the
quantum annealer correlated well with those obtained by QA with QMC. Figure 7 shows the
comparison of the histogram of the success probability between D-Wave’s quantum annealer
(DW) and QA with QMC (named as Simulated QA). The bimodal distribution which is common
in D-Wave and QMC could be evidence that the system embedded in D-Wave’s quantum annealer
was a quantum system. However, Shin et al. [91] reported that the classical spin vector model
along with the Monte Carlo dynamics, named as the spin vector Monte Carlo (SVMC) model,
provided as strong correlation with D-Wave’s data as QMC. The classical spin vector model is
represented by the Hamiltonian

H(t) = −A(t)

N

j=1

cos θj − B(t)



Jjk sin θj sin θk ,

(2.2)

jk

Downloaded from http://royalsocietypublishing.org/rsta/article-pdf/doi/10.1098/rsta.2021.0417/1326707/rsta.2021.0417.pdf
by guest
on 21 April 2026

...............................................................

1012

180

royalsocietypublishing.org/journal/rsta Phil. Trans. R. Soc. A 381: 20210417

QMC and SA single-core annealing time (s)

1014

(a) 500

(b) 500
DW
no. of instances

300
200

200
100

100

0

300

0.2

0.4

0.6

0.8

success probability

1.0

0

0.2

0.4

0.6

0.8

1.0

success probability

Figure 7. Comparison of the histogram of the probability of finding the ground state between D-Wave One and QA with QMC
(simulated QA) over 1000 instances of the spin glass model with N = 108 spins. (Adapted from [90]). (Online version in colour.)

where θj denotes the angle of the unit vector at site j in the xz plane. These works have raised a
problem to identify the model of D-Wave’s quantum annealer [92]. Bando et al. [93] studied the
Kibble–Zurek scaling in 1dTIM using D-Wave 2000Q and found that the kink density defined by

−α
z z
n = (1/2N) N
j=1 (1 − σj σj+1 ) = εres /2 scaled with the annealing time ta as n ∼ ta with α ≈ 0.20
by the device at NASA and α ≈ 0.34 by the one at D-Wave Systems. As mentioned in §1b(i),
−1/2
the scaling of the kink density is predicted as n ∼ ta
for an isolated system belonging to onedimensional Ising universality class. The authors in [93] compared numerical simulations for
1dTIM with coupling to an environment and for SVMC with the experiment, and concluded
that the quantum model agreed better with the experiment. Recently, King et al. [73] studied QA
of 1dTIM using D-Wave 2000Q, focusing on shorter annealing times than those in the previous
works. For short annealing times, the system in the device is less affected by environment, as
we shall discuss in the next section. Comparing analytic and numerical computation for the
Schrödinger dynamics of the isolated 1dTIM, the QMC simulation, and the SVMC simulation
with the experiment by D-Wave 2000Q, King et al. reported that only the Schrödinger dynamics
of the isolated 1dTIM with a small amount of disorder can explain all the experimental results
[73]. Also, in [94], a fully connected Sherrington–Kirkpatrick model with random couplings was
programmed using D-Wave TwoTM annealer, where optimal parameter setting allowed better
performance of the quantum annealer when compared with those obtained using optimized SA
algorithms.

3. Effects of environment on QA
Although QA is ideally performed in an isolated system, any real system is always coupled to
an environment and hence susceptible to decoherence. In fact, the system in D-Wave’s device
is believed to be affected considerably by an environment when the annealing time is longer
than a few microseconds. Therefore, it is very important to study an effect of environment
in QA.
There is a variety of models representing an environment. Caldeira & Leggett [95], in their
seminal work analysed the dynamics of flux state in a SQUID and constructed a simple model of
a two-level system coupled to a boson bath, where bosons are attributed to the electro-magnetic
field coming from the fluctuating current. Leggett et al. [96] elaborated on the single-spin model
coupled to a boson bath. Thus, considering QA performed with superconducting flux qubits,
the model which includes the effect of an environment should be an extension of the Caldeira–
Leggett model to many spins. The Hamiltonian is written as H(t) = HS (t) + HB + Hint , where the
system Hamiltonian HS (t) is given by equation (1.1). The bath is represented by the collection of
Downloaded from http://royalsocietypublishing.org/rsta/article-pdf/doi/10.1098/rsta.2021.0417/1326707/rsta.2021.0417.pdf
by guest
on 21 April 2026

...............................................................

no. of instances

400

royalsocietypublishing.org/journal/rsta Phil. Trans. R. Soc. A 381: 20210417

400

13
SQA

where ωa is the frequency of the harmonic oscillator of mode a. Hint represents the interaction
between the system and the bath, and is written as
Hint =

N

(σjx Qxj + σjz Qzj )

(3.2)

j=1

 γ
γ
γ
where Qj (γ = x, z) is the bath operators given by Qj = a λa (b†j,a + bj,a ). The spectral density
 γ 2
of the boson bath is assumed as Jγ (ω) = a (λa ) δ(ω − ωa ) = ηγ ωs e−ω/ωc , where ηγ denotes the
coupling strength of the system–bath interaction and ωc is the energy cutoff of the bath spectrum.
The Ohmic bath refers to s = 1, while the super-Ohmic and sub-Ohmic baths refer to s > 1 and
s < 1, respectively.
Let us now study the time evolution assuming that the state of the composite system is
described by the density operator ρ(t) at the instant t. The initial state is assumed to be a direct
product state of the form ρ(0) = |ψ(0)ψ(0)| ⊗ e−HB /T /ZB , where |ψ(0) denotes a state vector
of the system, T is the temperature and ZB is the partition function of the bath. Since we are
interested in the behaviour of the system, we consider the reduced density operator describing
the system, ρS (t) = TrB ρ(t), where TrB stands for the trace with respect to the bosonic degrees of
freedom.
Amin explored the success probability of QA for a range of annealing time ta obtained by
solving numerically the quantum Redfield master equation for an instance of 16 spins of the
random Ising model in a random longitudinal field with non-zero ηz and ηx = 0 [97]. The
obtained success probability is a non-monotonic function of ta . For short ta , the spin system is
not influenced by the bath and hence the success probability increases with increasing ta . In a
middle range of ta , the thermal environment disturbs the system’s adiabatic evolution more for
longer ta , hence leading to decreasing success probability. For very long ta , finally, the system
evolves keeping the thermal equilibrium with the bath until it is frozen near the end of QA. The
freezing happens because HS (ta ) and Hint are commutable when ηx = 0 and hence the relaxation
time diverges as t → ta . Thus the success probability in this regime goes to the probability of the
ground state at the thermal distribution as ta → ∞.
QA of 1dTIM in the presence of an environment has attracted a lot of attention in the context
of the Kibble–Zurek scaling. Assuming ηz = 0, namely, the boson bath coupled to σ x , 1dTIM with
coupling to the boson bath is mapped to a non-interacting fermion model with a fermion–boson
coupling through the Jordan–Wigner transformation. Then the problem is significantly tractable,
compared with the situation with ηz = 0. Patané et al. [98] studied the density of excitation
following QA using the Keldish technique. Based on the ansatz that the density of excitation E is
given by the sum of the coherent part Ecoh and the incoherent part Einc due to the environment,
Patané et al. [99] obtained Einc ∼ ηx T4 τ for the Ohmic bath with temperature T when QA ends
near the quantum critical point. The incoherent part increases with τ in contrast to the coherent
part, hence its scaling is called the anti-Kibble–Zurek scaling. Nalbach et al. studied the model

with the spatially correlated bath where all spins are coupled to a single bath, i.e. Hint = Qx j σjx


and HB = a h̄ωz b†a ba with Qx = a λa (b†a + ba ). In this situation, the correlation length is the
largest of the Kibble–Zurek length scale ξKZ ∼ τ 1/2 and the thermal length scale ξT ∼ T−1 . When
1  ξT < ξKZ , the thermal effect comes into play in the density of excitation. Thus, it is suggested
√
that E ∼ ηx T(τ T2 ) ∼ ηx T3 τ for τ  T  1 in this model. Nalbach et al. [100] proposed this scaling
relation and confirmed using the dissipative Landau–Zener theory for the two-level system. Dutta
et al. studied 1dTIM in the presence of a spatially homogeneous Gaussian white noise on the
transverse field, instead of considering the coupling to a boson bath. This stochastic perturbation
yields an effective dynamics of the noise-averaged density operator for an open quantum system.
Downloaded from http://royalsocietypublishing.org/rsta/article-pdf/doi/10.1098/rsta.2021.0417/1326707/rsta.2021.0417.pdf
by guest
on 21 April 2026

...............................................................

j,a

14

royalsocietypublishing.org/journal/rsta Phil. Trans. R. Soc. A 381: 20210417

harmonic oscillators. Hence the bath Hamiltonian HB is given, using the boson operators bj,a and
b†j,a for site j and mode a, by

h̄ωa b†j,a bj,a ,
(3.1)
HB =

4. Avoiding first-order phase transitions: closed systems
As discussed in §1a, it has been generally observed (with a few exceptions) that the minimum
energy gap decreases exponentially with the system size for a first-order phase transition, whereas
it shows a polynomial decrement in system size for a second-order phase transition. Therefore,
the order of phase transitions is an important factor in determining the efficiency of the quantum
annealing algorithm.

(a) Quantum ferromagnetic model
We consider here a ferromagnetic p-spin model in the transverse field. The Hamiltonian for such
a system is given by
1  z
σi
N
N

H = −N

i=1

p

−Γ

N


σix ,

(4.1)

i=1

where σiz and σix are usual Pauli matrices at the lattice site i, Γ is the magnetic field in transverse
direction and N is the number of spins and p is an integer. These type of models were initially
introduced in the context of spin glasses. The ground state of the classical model at zero
Downloaded from http://royalsocietypublishing.org/rsta/article-pdf/doi/10.1098/rsta.2021.0417/1326707/rsta.2021.0417.pdf
by guest
on 21 April 2026

...............................................................

pure and disordered systems with O(102 ) spins [111,112] or an infinite translationally invariant
system [113]. Using the infinite-system method, Oshiyama found modified Kibble–Zurek scaling
in 1dTIM coupled to the bath at zero temperature [112]. Oshiyama et al. also studied QA of 1dTIM
with the bath at finite temperatures. In the thermal environment at finite temperature T, the
infinitely slow QA (ta → ∞) can be regarded as the quasi-static and isothermal process, hence
the final energy should be identical to the thermal average of B(ta )HP at T. When ta is sufficiently
long but finite, the energy of the system has an excess from the thermal average. Oshiyama et al.
−1/3
[113] found and numerically confirmed that this excess energy scales with ta as ta , for the linear
annealing protocol.

15

royalsocietypublishing.org/journal/rsta Phil. Trans. R. Soc. A 381: 20210417

Then the noise-averaged density of excitation has an incoherent part which scales as Einc ∼ η̃x τ ,
where η̃x is the strength of the noise [101]. Weinberg et al. studied a similar model but with a
spatially uncorrelated and temporally correlated noise. The numerical result showed the same
scaling as ref. [101]. Weinberg et al. [102] also performed quantum simulation for 2dTIM using
D-Wave 2000Q and obtained scaling for the residual energy εres ∼ aτ −α + bτ β with α ≈ 0.74 and
β ≈ 0.456. The first term is consistent with the Kibble–Zurek scaling for 2dTIM with the exponent
dν/(zν + 1) ≈ 0.77, where d = 2, z = 1 and ν ≈ 0.63 [103]. Note that the scaling of the second term
corresponding to the incoherent part is different from that in 1dTIM, implying that Einc ∼ τ
is specific to 1dTIM. The anti-Kibble Zurek mechanism in the presence of a non-thermal bath
has also been discussed in the framework of the Lindblad formalism in [104–108].
The Kibble–Zurek and anti-Kibble–Zurek scalings imply the existence of a global or local
minimum of the density of excitation. Based on the numerical study using the Redfield master
equation in the momentum space for 1dTIM with the boson bath, equations (3.1) and (3.2) with
Qzj = 0, Arceci et al. [109] identified the region in the T − ηx -plane where there exists the local
or global minimum of the density of defects after QA. Interestingly, a global minimum of the
density of defects appears in the digitized QA, in which the time-evolution operator inducing
QA is split into slices with a finite time width and further split into those involving only HD and
those involving only HP [110], suggesting that the decomposition of the time-evolution operator
has an influence as a decoherence on the dynamics of a closed system.
Many studies of 1dTIM with a boson bath focusing on the Kibble–Zurek physics have assumed
Qzj = 0, namely, coupling between the system operators σjx and bosons. However, in experimental
systems such as those made of coupled superconducting flux qubits, coupling between σjz and
QzJ is rather important [96]. Recently, Suzuki et al. developed new matrix-product-state-based

methods for 1dTIM with a boson bath with Hint = j Qzj σjz , which enables the simulation of finite

1.8

1.2
1.0
T
0.8
0.6
ferromagnet
0.4
0.2
0

0.2

0.4

0.6

0.8

1.0

1.2

1.4

G

Figure 8. Phase diagram of the ferromagnetic p-spin model in the T − Γ plane for different values of p. The ferromagnetic
and quantum paramagnetic phases are separated by first-order phase transitions. (Adapted from [114]). (Online version in
colour.)

temperature with Γ = 0 corresponds to all spins aligned in the same direction. For even p, all
the spins in up or down states are valid ground states, whereas odd p has a unique ground
state when all the spins are in up states. Therefore, for simplicity, we will concentrate here on
the odd p cases. For p = 2, the Hamiltonian in equation (4.1) reduces to an infinite-range Ising
model which can be mapped to the usual mean field Curie-Weiss model exhibiting continuous
phase transitions. On the other hand, for p > 2, both classical and quantum phase transitions of
the system are discontinuous.
Using Suzuki-Trotter formalism and ‘static’ approximation, the phase diagram of the p-spin
ferromagnetic model can be found in Γ − T plane for different values of p (see figure 8) [114].
In the limit of p → ∞, using perturbation theory, the minimum energy gap of the system can be
calculated as min = 2N2−N/2 [114]. This indicates that the energy gap between the ground and
excited states closes exponentially fast with the system size at the transition point. For a general
p, an explicit form of the energy gap is not available so that one can comment about its scaling
with the system size; however, the same scaling can be inferred from numerical calculations.
The energy gap of the system can be calculated numerically using two complementary
methods as a function of the transverse-field Γ [114]. Using these numerical methods, we can
find the transition point Γc where the energy gap shows a minima that scales with the system
size. In the present case, the energy spectrum of the system has been studied for 3 ≤ p ≤ 31.
The Hamiltonian in equation (4.1) is represented by a sparse matrix of dimension 2N . For such
systems, the Lanczos method provides nearly exact extreme eigenvalues of the Hamiltonian for
the system size N ≤ 21. From the results of the Lanczos method for N ≤ 21, it has been found
that the transition happens between two states with the maximum possible angular momentum
l = N/2. The efficiency of the numerical simulation can be improved by exploiting the fact that
the total angular momentum L2 commutes with the Hamiltonian H in equation (4.1) (where L is
the total angular momentum of N spins). Therefore the transition occurs mainly in the subspace
of dimension 2l + 1 = N + 1. In this subspace, the Hamiltonian assumes a tri-diagonal form and
the resulting tri-diagonal matrix can be diagonalized efficiently for a system with size N ∼ 100 in
just a few seconds. The energy gap has been shown in figure 9a as a function of Γ for p = 3 and
Downloaded from http://royalsocietypublishing.org/rsta/article-pdf/doi/10.1098/rsta.2021.0417/1326707/rsta.2021.0417.pdf
by guest
on 21 April 2026

...............................................................

paramagnet

1.4

royalsocietypublishing.org/journal/rsta Phil. Trans. R. Soc. A 381: 20210417

1.6

16

p = Infinity
p=3
p=5
p=9
p = 15
p = 25

(a) 6

(b)

0.01

p=3

'min/N

'min

3
2
1

0

N = 10
N = 20
N = 30
N = 60
N = 90
N = 120
N = 150

1 × 10–6
1 × 10–8
p=3
p=5
p=7
p = 11
p = 15
p = 21
p = 31
2-N/2

1 × 10–10
1 × 10–12

0.5

1.0

1.5

2.0

1 × 10–14

0

20

40

60

80

100

120

140

N

G

Figure 9. (a) Variation of the energy gap as a function of Γ for p = 3 computed using an exact diagonalization method as
described in the text. The gap vanishes exponentially fast with the system size N near the critical point Γc (the black vertical
line). It also shrinks near the critical regime as N increases. (b) Minimum energy gap as a function of N for a few values of p
on a semi-log scale. It shows an exponential fall of the minimum gap with N for all values of p according to the scaling relation
min ∝ N2−Nα . (Adapted from [114]). (Online version in colour.)

different N. The gap becomes minimum at the critical value of Γ that agrees with the analytically
predicted value. One can observe that the region where the gap closes gets narrower as the value
of N is increased. The minimum energy gap min is further plotted as a function of N for different
values of p to find its dependence on N (figure 9b). It has been found that the minimum energy gap
decays exponentially as min ∝ N2−Nα for p ≥ 3. The minimum energy gap closes exponentially
fast as expected for the first-order phase transition. The value of exponent α can be computed
numerically from figure 9b. These exponents are also calculated analytically using an instantonic
approach. A comparison of values of α for different values of p is given in table 1 of [114].
Owing to an exponential decay of energy gap with the system size, the running time increases
exponentially for the case of a first-order phase transition, and thus reduces the efficiency of the
QA process. Therefore, it is an important issue to investigate whether one can avoid the firstorder phase transitions in the annealing path to solve the optimization problem efficiently
using QA algorithm. Below we discuss various methods to speed up a quantum annealing
process.

(b) Application of antiferromagnetic fluctuations
In the context of speed-up of QA, Seki & Nishimori [115] in 2012 proposed a method to overcome
issues related to the first-order phase transitions, by studying quantum annealing in the presence
of antiferromagnetic fluctuations in addition to the transverse-field term. They applied the
method to the infinite-range ferromagnetic p-spin model (see equation (4.1)) and showed that
there exists a quantum path that avoids the first-order transitions for some intermediate values of
p. The Hamiltonian for p-spin is given by
1  z
σi
N
N

H0 = −N

p

.

(4.2)

i=1

This is indeed the classical counterpart of the Hamiltonian as in equation (4.1) with zero
transverse field. Here H0 is the target Hamiltonian HP , whose ground state is the optimal solution
of the problem. The QA for this model is studied before with the transverse-field as a driver
Hamiltonian HD , which takes an exponentially long time to reach the ground state of the target
Hamiltonian due to the presence of a quantum first-order phase transition during the time
Downloaded from http://royalsocietypublishing.org/rsta/article-pdf/doi/10.1098/rsta.2021.0417/1326707/rsta.2021.0417.pdf
by guest
on 21 April 2026

...............................................................

0.0001

4

royalsocietypublishing.org/journal/rsta Phil. Trans. R. Soc. A 381: 20210417

5

17

1

(a)

(b)

0

1

18

mx 0.5
p=3
p=5
p = 11
p = 21

–0.4
0.2

0.4

0.6
s

0.8

1.0

0

0.2

0.4

0.6

0.8

1.0

s

Figure 10. (a) Free energy of the system with the Hamiltonian in equation (4.3), as a function of s for some values of p with
λ = 0.3. The free energy of the QP phase, equation (A 9), is represented by the dash-dotted line in light green. The thin solid
line with blue colour represents the free energy of the ferromagnetic phase (F), equation (A 10), and the thick solid line with
red colour is for the QP2 phase, equation (A 11). The lower limit of the QP2 domain (s = 1/(3 − 2λ)) is denoted by the vertical
dashed line. Although it is hard to see in this present scale, all the data for finite p studied here have lower values than that of
fQP2 in the QP2 regime. (b) Magnetization mx versus s for λ = 0.3 and the same values of p as in the case of free energies. The
vertical dashed line is the same as shown in panel (a). The solid line in red exhibits the x-component of magnetization of the
QP2 phase. The magnetization decreases to zero as s is increased with a jump at the boundary of the QP2 domain for p ≥ 5.
(Adapted from [115]). (Online version in colour.)

evolution. The ferromagnetic p-spin model reduces to the Grover problem when p → ∞ and there
is no known algorithm that can solve the problem efficiently in a polynomial time.
We discuss here how the inclusion of an antiferromagnetic fluctuation term can improve the
performance of QA of the model when both the transverse-field term and the antiferromagnetic
term are tuned. The total Hamiltonian of the problem is then given by
(4.3)
H(s, λ) = s{λH0 + (1 − λ)V̂AF } + (1 − s)VTF ,
N x 2
where VAF = +N((1/N) i=1 σi ) is an antiferromagnetic interaction term, whereas VTF is the
conventional transverse-field term. The parameters s and λ are functions of time, assumed to lie
between 0 and 1, which are chosen appropriately for a QA process. The initial Hamiltonian is
defined by s = 0 and an arbitrary λ, and the final one is given by s = λ = 1.

(i) Numerical results
We now focus on analysing the phase diagram of the model on the s − λ plane for finite values
of p, using the saddle point method and the static approximation, as elaborated in appendix A.
The method we adopt to construct the phase diagram is as follows. The self-consistent equations
(A 6) and (A 7) are initially solved numerically for a particular value of p and a set of values of s
and λ to find out the corresponding free energy. By comparing these free energies and all possible
solutions, the stable phases of the system are identified with the smallest value of free energy. The
variation of free energy with s for some values of p and λ = 0.3 is shown in figure 10. It can be seen
that the free energies for different values of p lie below fQP2 in the QP2 regime and, therefore, the
QP2 phase is not a stable phase. As we vary λ, the system undergoes a quantum phase transition
from the QP phase for small s to the Ferromagnetic (F) phase for large s.
To determine the type of phase transitions, i.e. first or second order, the magnetization mx is
numerically calculated as a function of s for the same parameter values as in the case of free
energy. We observe a change in mx around s = 0.4167 and mx decreases continuously to zero
from its unit value for p ≥ 5. Equivalently, it indicates that mz increases continuously from zero
to a finite value as we increase s for p ≥ 5. This identifies that for p ≥ 5 there exists a secondorder phase transition at the boundary of QP and QP2 phases. An interesting scenario arises for
some parameter values (e.g. λ = 0.3, p = 11) where the magnetization shows a jump within the
Downloaded from http://royalsocietypublishing.org/rsta/article-pdf/doi/10.1098/rsta.2021.0417/1326707/rsta.2021.0417.pdf
by guest
on 21 April 2026

...............................................................

f –0.2

royalsocietypublishing.org/journal/rsta Phil. Trans. R. Soc. A 381: 20210417

p=3
p=5
p = 11
p = 21

(a)

(b)

1.0

0.8
F

F

0.6

0.6

0.6

0.4

0.4

0.4

s
0.2
0

QP
0.2 0.4 0.6 0.8
l

1.0

0.2

QP

0.2

QP

0

0.2 0.4 0.6 0.8 1.0

0

0.2 0.4 0.6 0.8 1.0

Figure 11. Phase diagrams on the s-λ plane for the system with Hamiltonian in equation (4.3) for p = 3 (a), p = 5 (b) and
p = 11 (c). The boundary of the QP2 domain (s = 1/(3 − 2λ)), where a transition occurs between the QP and F phases, is
represented by the dash-dotted line. The red lines are for the first-order transitions and the light green lines represent the
second-order transitions. For p = 5 and 11, the magnetization shows sudden jumps on the dashed blue line (F-F boundary)
within the F phase. (Adapted from [115]). (Online version in colour.)

ferromagnetic phase. This suggests the existence of first-order transition within the F phase and
the energy gap at the transition point decreases exponentially with the system size. Nevertheless,
this peculiar behaviour does not appear for smaller values of λ for any non-zero p, except p = 3.
Therefore, for smaller λ, there exists only a second order transition when one increases s from zero
to a value near unity.
Using these results, phase diagrams of the system for p = 3, 5 and 11 are drawn on the
s − λ plane (figure 11). We can see that a boundary of second-order transitions between F
and QP phases exists for small λ and p ≥ 5. As a consequence, there are possibilities to find
a path to reach the F phase from the QP phase by avoiding a first-order transition provided
the first-order F-F boundary does not reach the λ = 0 axis, that occurs probably in the limit
of p → ∞ [115].
Let us now focus on analysing the behaviour of the energy gap across the phase transition
points of the system. The energy gap of the system is calculated numerically using perturbation
theory as described in [114]. The variation of energy gap with s for λ = 0.3 and p = 11 is shown
in figure 12. If the range of s where the energy gap has minimum value is zoomed, it can be seen
that the gap shows wiggly behaviour throughout the range. This behaviour starts at s ≃ 0.4184
for λ = 0.3, which indeed corresponds to the second-order transition point between the QP and
F phases. The wiggly behaviour ends at s ≃ 0.4676 for λ = 0.3, which corresponds to the firstorder transition point at the F-F boundary. The dashed vertical lines in figure 12 indicate two
transition points that are evaluated analytically using equations (A 6) and (A 7). The analytical
results show nearly a good agreement with the numerical results in the interval where the gap is
very small. It has been found that the rightmost local minimum of the energy gap in figure 12
corresponding to the F-F boundary shows a different scaling relation with the system size N
compared with the other local minima. The rightmost minimum energy gap decays exponentially
with the system size, which is expected from discontinuous behaviour of the magnetization
in figure 10 at the F-F boundary implying the first-order transition. Although, for the present
case, the above mentioned energy gap is not a global minimum, this will affect the efficiency
of QA for larger systems where the rightmost gap can become a global minimum since the
other local minima decay polynomially with the system sizes (see figs. 6 and 7 of [115] for
details).
These analytical and numerical results suggest that it is possible to increase the efficiency of
QA by choosing a path around λ = 0.1, which avoids first-order transition to reach the F phase
from the QP phase. For this process, s is the tuning parameter and the value p needs to be chosen
within the range 5 ≤ p ≤ 21 achieving maximum efficiency.
Downloaded from http://royalsocietypublishing.org/rsta/article-pdf/doi/10.1098/rsta.2021.0417/1326707/rsta.2021.0417.pdf
by guest
on 21 April 2026

...............................................................

0.8
F

19

1.0

royalsocietypublishing.org/journal/rsta Phil. Trans. R. Soc. A 381: 20210417

0.8

(c)

1.0

(b)

0.39

energy gap
0.42
s

0.45

0.48

1.0 u10–2

1.0 u10–4

40

80
N

120

160

Figure 12. (a) Energy gap as a function of s for p = 11 and λ = 0.3. The positions of minima of the energy gap are shown by the
vertical dashed lines at the QP2 domain with s ≃ 0.4167 and the F-F boundary at s ≃ 0.4701. (b) The rightmost local minimum
of the energy gap with the system size N for p = 11 and λ = 0.3 on a semi-log scale. The energy gap closes exponentially fast
with N. (Adapted from [115]). (Online version in colour.)

(c) Inhomogeneous transverse field driving
In §4b, we have discussed a method to speed up a QA process in the presence of the first-order
phase transitions by adding an antiferromagnetic fluctuation term. Here we consider a relatively
simpler approach of inhomogeneous driving of the transverse field to overcome the issue of the
first-order phase transitions. In this case, the strength of transverse field is turned off sequentially
from one site to the next according to the annealing schedule. Using both analytical and numerical
calculations, it has been shown that inhomogeneous driving can completely remove QPTs from
the annealing path and thus, it speeds up the annealing process exponentially [116,117].
The total Hamiltonian for the inhomogeneous driving is given by
H(s, τ ) = sH0 −

N(1−τ
)

σix ,

(4.4)

i=1

where H0 is the Hamiltonian for p-spin model in equation (4.2). The parameters s and τ both
are time-dependent, where s = τ = 0 at t = 0 and s = τ = 1 at t = t0 . This shows that the initial
Hamiltonian has only a transverse field and the final one has only a p-spin interacting term with
the Hamiltonian H0 . Both the initial and final Hamiltonians are in agreement with the traditional
QA protocol.
We note that the transverse field in equation (4.4) is applied only to N(1 − τ ) spins, where τ
increases from 0 to 1 as time proceeds from 0 to ta . This indicates that the transverse field is turned
off at neighbouring sites one by one as time increases, starting from site i = N to ending with site
i = 1 at τ = 1. This is the process of how the transverse field is driven inhomogeneously. It can
be noted that the parameter τ can have only discrete values for a finite N, since the upper limit
N(1 − τ ) in equation (4.4) should be an integer.

(i) Results
Using Trotter decomposition and the static approximation in Hamiltonian (4.4), the free energy
of the system can be calculated analytically for both finite and zero temperatures (see appendix
B). By minimizing the zero-temperature free energy with respect to magnetization m produces a
ground-state phase diagram, as depicted in figure 13.
For a fixed value of p, a line of the first-order phase transitions that originated from a point on
the s-axis terminates before approaching any point of the τ -axis. Remarkably, all these lines for
different values of p end before they reach one of the axes, τ = 1 or s = 0. Therefore, there exists
a path starting from s = τ = 0 to s = τ = 1 that does not encounter any kind of phase transitions.
This leads to an exponential speedup of QA, since the energy gap always remains finite even for
Downloaded from http://royalsocietypublishing.org/rsta/article-pdf/doi/10.1098/rsta.2021.0417/1326707/rsta.2021.0417.pdf
by guest
on 21 April 2026

...............................................................

0.5

0
0.36

20

1.0

N = 20
N = 80
N = 140

royalsocietypublishing.org/journal/rsta Phil. Trans. R. Soc. A 381: 20210417

energy gap

(a) 1.0

1.0

21

0.6
t
0.4

0.2

0

0.2

0.4

0.6

0.8

1.0

s

Figure 13. Phase diagram of the p-spin ferromagnetic model under an inhomogeneous field. All the lines represent the firstorder phase transitions for different values of p, which are extended up to the middle of the phase diagram from the axis τ = 0
corresponding to the homogeneous model. (Adapted from [116]). (Online version in colour.)

a system with large size. The positions of the critical points on the τ − s plane where the firstorder transitions terminate for different p values are calculated analytically by using the standard
Landau theory of phase transitions (see equation (B 3)). In this calculation, it has been considered
that the coefficients of the expansion of the free energy (B 2) around its minimum at m = mc vanish
to third order [118].
To strengthen the above conclusion, the energy gap of the system has been calculated both
analytically and numerically. Since our system is mean-field-type, the semi-classical treatment
can be applied to evaluate the energy gap [119,120]. In this context, the parametrization of a path
τ = sr is considered to connect s = τ = 0 and s = τ = 1 with a parameter r that determines the shape
of the path. Figure 14a,b exhibits two energy gap candidates, a1 and b , for the system with p = 3
along the paths τ = s, that does not encounter phase transitions, and τ = s2.366 , that just touches
the critical point where the first-order line ends. The smaller one between these two candidates is
the actual energy gap of the system.
As shown in figure 14a, b is found to be the smaller one and it monotonically increases with
s. On the other hand, as expected, the energy gap a1 vanishes at the critical point sc ≈ 0.52 in
figure 14b. To investigate the effect of finite-size systems, the energy gap is calculated by a direct
numerical diagonalization method along the τ = s path. The result is shown in figure 14c, which
shows a very good agreement with the asymptotic behaviour in the N → ∞ limit as observed in
b of figure 14a. As seen in figure (14c), the energy gap becomes minimum when the transverse
field is turned off at the first site as shown by the arrows, thus implying the location of the
minimum gap at s = 0 in the N → ∞ limit. It is important to note that the energy gap becomes
minimum near the origin τ = s = 0, when the annealing path (τ = s) does not encounter any
transitions (figure 14a,c), whereas the minimum of the gap occurs at the critical point when such a
transition exists along the path (figure 14b). In addition, a series of paths is considered to examine
the inhomogeneous driving protocol, and it is found that the minimum energy gap shows an
exponential decrement with the system sizes when the paths cross the first-order transitions (for
details, refer to the discussion around eqn (12) of [117]).
Downloaded from http://royalsocietypublishing.org/rsta/article-pdf/doi/10.1098/rsta.2021.0417/1326707/rsta.2021.0417.pdf
by guest
on 21 April 2026

...............................................................

0.8

royalsocietypublishing.org/journal/rsta Phil. Trans. R. Soc. A 381: 20210417

p=3
p=4
p=5
p=6
p=7
p=8
p=9

(b)

3
2

5

'a
'b1

6

4
3
2
1

1
0.2

0.4

0.6

0.8

1.0

0

5
4

22

N=5
N = 10
N = 100

3
2
1

0.2

s

0.4

0.6
s

0.8

1.0

0

0.2

0.4

0.6

0.8

1.0

s

Figure 14. Plots of two types of energy gap a1 and b for p = 3 as functions of s with (a) τ = s (i.e. away from the transition
line) and (b) τ = s2.366 (i.e. just touches the critical point). The final energy gap is defined by the smaller of these two gaps.
(c) The energy gap for different system sizes with τ = s computed by direct numerical diagonalization. The location of the
minimum energy gap is shown by an arrow for each N. (Adapted from [117]). (Online version in colour.)

The problem that we discussed so far, for inhomogeneous driving, considers ideal situations,
i.e. zero temperature and a complete turning off of the transverse field at each site. This
problem also has been studied at finite temperature and zero temperature with different types
of inhomogenity. It has already been studied that the first-order transitions that exist under
homogeneous driving at zero temperature can be circumvented by inhomogeneous driving
with complete turning off the transverse field at each site. For non-ideal situations, with a
finite temperature or a non-zero value of the final transverse field, one cannot avoid new
first-order transition lines like the ideal case. Nevertheless, it has been observed that the new
first-order transitions are weaker than the original one, since the free energy barrier between two
arbitrary local minima is smaller than the original homogeneous case. This leads to an increase
in the quantum tunnelling rate. Therefore one can infer that the inhomogeneous driving of the
transverse field has the potential to provide a better performance in quantum annealing. In
addition, Matsuura et al. [121] studied analytically the p-body ferromagnetic infinite-range Ising
model in transverse-field using a mean-field analysis and demonstrated that for p ≥ 3, where the
phase transition is of first order, Quantum Annealing Correction softens the closing of the gap for
small energy penalty values and prevents its closure for sufficiently large energy penalty values,
thereby providing from excitations that occur near the quantum critical point. It also has been
shown analytically that nested quantum annealing correction can suppress errors effectively in
Ising models with infinite-range interactions and their analysis revealed that the nesting structure
can significantly weaken or remove the first-order phase transitions, where the energy gap closes
exponentially [122].

(d) Suppression of Griffiths singularities
In a recent work by Knysh et al. [123], it has been shown that a QA process can be accelerated
using an embedded spin chain system with random interactions. A randomly interacting spin
chain exhibits Griffiths–McCoy singularities [124,125], since different parts of the system cannot
reach criticality simultaneously for random fluctuations. This leads to the diverging dynamical
exponent z and a stretched exponential scaling of the energy gap [36]. Therefore, the presence of
Griffiths singularities increases the annealing time for such systems.
On the other hand, quantum annealing has been studied for an embedded spin chain problem,
where logical qubits were replaced by ferromagnetic Ising spin chains [123]. For this study, an
ansatz is considered to find a balanced choice of coupling parameters based on renormalization
group intuition for the better performance of QA. This results in an exponential improvement
of annealing time, which is also confirmed numerically. It indicates that this protocol prevents to
Downloaded from http://royalsocietypublishing.org/rsta/article-pdf/doi/10.1098/rsta.2021.0417/1326707/rsta.2021.0417.pdf
by guest
on 21 April 2026

...............................................................

4

0

(c)
6

energy gap

5

'a
'b1

royalsocietypublishing.org/journal/rsta Phil. Trans. R. Soc. A 381: 20210417

energy gap

6

energy gap

(a)

occur randomly oriented domains in the system by ensuring a simultaneous criticality of spatially
separated regions.

(a) Quantum annealing versus semi-classical annealing
Starchl & Ritsch [17] have used the idea of quantum tunnelling to show the success of QA over
semi-classical annealing for an interacting bosonic model in the presence of cavity modes. The
model that is considered for this study is described by a tight binding Bose–Hubbard lattice model
with four sites, which are filled by two interacting bosons. The tunable non-local interactions are
introduced in the model via collective light scattering to two independent cavity modes. The
Hamiltonian for such a system is given by
H=J



(b†k bk+1 + h.c.) +

kPBC

U
nk (nk − 1) − (a†1 a1 + a†2 a2 ) + J̃ M̂1 (a1 + a†1 ) + M̂2 (a2 + a†2 ) ,
2
k

(5.1)
where bk and b†k are bosonic annihilation and creation operators, respectively. The photonic
annihilation operators a1 and a2 are associated with two independent cavity modes. The
interactions between the bosons and cavity field modes are represented by the fourth term
of equation (5.1), where M̂1 and M̂2 are called effective scattering operators. Using meanfield approximation of the field operators, the Hamiltonian in equation (5.1) can be written in
semi-classical form
Hsc =

J̃2
κ 2 + 2

2M̂1 M̂1  − ÎM̂1 2 + 2M̂2 M̂2  − ÎM̂2 2 ,

(5.2)

where κ determines the strength of cavity loss and I denotes the identity operator. Both the
Hamiltonians in equations (5.1) and (5.2) with periodic boundary conditions are translationally
invariant and thus provide approximately degenerate ground states. In order to create an unique
target ground state for the annealing process, a certain amount of impurity of strength V is added
in the Hamiltonian.
The dynamics of the system is started with
√ the ground state at zero pump J̃ = 0, and the pump
strength is increased linearly towards J̃ = 5, following an adiabatic schedule: J̃ ≈ t/tf , where tf is
the final time. The results of the study of annealing for this system are summarized in figure 15.
It shows the density plot of the fidelity on U − V plane after an adiabatic sweep using both the
semi-classical (5.1) and the full quantum (5.2) Hamiltonian. In this case, the fidelity is calculated
as the overlap between the final state after an adiabatic sweep and the desired target state. By
comparing two density plots for both semi-classical and quantum cases, i.e. when the dynamics
is driven by the semi-classical Hamiltonian and the full quantum Hamiltonian, respectively, one
can identify a clear quantum improvement in the success rate. It is observed that the semi-classical
approximation provides a reliably correct solution for small onsite interaction strength. For this
scenario, one can see a sudden fall of the success rate, when the interaction strength is increased.
If the repulsive interaction is further increased, the gap between the final ground state energy
and the first excitation becomes very small and the classical model effectively never succeeds. On
the other hand, the adiabatic evolution with full quantum Hamiltonian (5.1) provides an almost
correct solution with 99% probability, even for higher U values, as shown in figure 15b. Therefore,
for this system, a large parameter region is found where quantum annealing is highly successful,
whereas the semi-classical approach largely fails. In addition, for the quantum scenario, a direct
Downloaded from http://royalsocietypublishing.org/rsta/article-pdf/doi/10.1098/rsta.2021.0417/1326707/rsta.2021.0417.pdf
by guest
on 21 April 2026

...............................................................

In this section, we discuss some recent results on QA of a interacting bosonic system coupled
with cavity field modes for both classical and quantum limits of the system. In addition, we will
mention the recent development of QA in the context of parallel computation, and its effectiveness
compared with the existing methods.

royalsocietypublishing.org/journal/rsta Phil. Trans. R. Soc. A 381: 20210417

5. Application

23

(a)

(b)

fidelity ‘phase’ diagram semi-classical model
1.0

3.00

1.000
0.998

2.50

2.50

2.25

0.996

2.25

0.6

V

V
2.00

2.00

0.994

0.4
1.75

1.75

1.50

0.2

1.25

0.992

1.50
1.25

0.25 0.50 0.75 1.00 1.25 1.50 1.75 2.00
U

0.990
0.25 0.50 0.75 1.00 1.25 1.50 1.75 2.00
U

Figure 15. Colour density plot of the fidelity calculated as the overlap between the final state after an adiabatic evolution
using (a) the Hamiltonian with semi-classical mean-field approximation and as well as (b) for the full quantum Hamiltonian,
and the desired target
√ state on the U − V plane. Here the parameter values are: tf = 1000. For (a)  = −1, J̃ = 1 and for
(b)  = −5, J̃ = 5. (Adapted from [17]). (Online version in colour.)

connection is found between atom-field entanglement in the dynamics and a high probability to
find the correct solution at the end of the annealing process.

(b) Parallel quantum annealing
There are a few recent studies on QA in the context of parallel quantum computation [126–128].
Recently, Pelofske et al. [128] proposed a method named as parallel quantum annealing that
has the potential to solve many independent problems on a quantum annealer during the same
annealing process. The authors applied their proposed method of parallel quantum annealing
on both D-Wave 2000Q at Los Alamos National Laboratory (referred to as D-W 2000Q) and the
newer D-Wave Advantage_System 1.1 (referred to as D-W Advantage). The results of parallel
quantum annealing have been compared with those found from sequential quantum annealing,
i.e. when the same problems are solved sequentially on a D-Wave machine. It has been observed
that, although there is a slight decrement in the accuracy of the solution for simultaneously solved
problems, parallel quantum annealing can provide a considerable speedup of up to two orders of
magnitude [128].

6. Summary and outlook
We have provided an overview of recent developments of QA that is based on the possible
advantage of using quantum tunnelling. When the energy landscape of an Ising Hamiltonian,
where the corresponding ground state is the target state of an optimization problem, consists
of high but thin barriers surrounding local minima, quantum tunnelling has an advantage over
thermal fluctuation in overcoming barriers and thus getting the system equilibrated. This nature
of quantum tunnelling provides a foundation which asserts that QA can outperform SA in a
glassy system with a rugged energy landscape. Indeed, we have focused on analytical and
numerical evidence that QA yields a better solution than SA in several glassy systems. The
question of the restoration of ergodicity due to quantum tunnelling in the quantum SK model
is still unresolved. Nevertheless, recent studies do indicate the possibility of the existence of an
ergodic phase, at least in a low temperature region [62,64]: this is expected to lead to a remarkable
possibility of the success of the annealing scheme in those systems [61].
We have also discussed QPTs in connection with QA. Generally speaking, a QPT hinders the
adiabatic time evolution underlying QA, since the energy gap above the ground state closes at a
Downloaded from http://royalsocietypublishing.org/rsta/article-pdf/doi/10.1098/rsta.2021.0417/1326707/rsta.2021.0417.pdf
by guest
on 21 April 2026

...............................................................

2.75
0.8

royalsocietypublishing.org/journal/rsta Phil. Trans. R. Soc. A 381: 20210417

2.75

24

fidelity ‘phase’ diagram full quantum model
3.00

papers.

Authors’ contributions. A.R.: formal analysis, investigation, resources, writing—review and editing; S.S.: formal
analysis, investigation, resources, writing—review and editing; A.D.: conceptualization, resources, writing—
review and editing; B.K.C.: conceptualization, resources, writing—review and editing.
All authors gave final approval for publication and agreed to be held accountable for the work performed
therein.
Conflict of interest declaration. We declare we have no competing interests.
Funding. A.R. acknowledges UGC, India for Start-up Research grant no. F. 30-509/2020(BSR). The work of S.S.
was supported by JSPS KAKENHI grant no. 22K03455. A.D. acknowledges support from SPARC program,
MHRD, India and SERB, DST, New Delhi, India. B.K.C. is grateful to the Indian National Science Academy
for their Senior Scientist Research Grant.
Acknowledgements. We acknowledge our collaborations with Gabriel Aeppli, Arunava Chakrabarti, Arnab Das,
Uma Divakaran, Jun-ichi Inoue, Sudip Mukherjee, Hidetoshi Nishimori, Masato Okada, Purusattam Ray,
Downloaded from http://royalsocietypublishing.org/rsta/article-pdf/doi/10.1098/rsta.2021.0417/1326707/rsta.2021.0417.pdf
by guest
on 21 April 2026

...............................................................

Data accessibility. The article has no additional data over those given in different figures taken from published

25

royalsocietypublishing.org/journal/rsta Phil. Trans. R. Soc. A 381: 20210417

QPT; this leads to inevitable generation of defects and excess energy in the final evolved state. In
this context, it is worth noting that the short-cut to adiabaticity [129] or counter-diabatic driving
protocols [130] have been proposed as a method to realize the adiabatic time evolution with a
finite time, providing a possible route to avoid a continuous QPT in the process of annealing. On
the contrary, a discontinuous QPT involves an exponentially fast closure of the energy gap with
the system size. Therefore, it is desirable and at the same time far more challenging to circumvent
a discontinuous QPT for the success of QA. We have reviewed methods using additional
antiferromagnetic interactions [123] or inhomogeneous transverse fields [116,117] proposed for
avoiding discontinuous QPTs that would lead to acceleration of QA. Random interactions in
spin chain systems induce Griffiths singularities that eventually increase the annealing time for
such systems. These singularities can be suppressed for the embedded spin chain problem, where
ferromagnetic Ising spin chains are used as logical qubits. It has been shown that the performance
of QA for such embedded systems improves exponentially in the context of annealing time [123].
To be precise, the performance advantage of QA is still model specific and a generic prescription
has not been known for discontinuous phase transitions involved by practical optimization
problems. In the cases of spin glass models, however, major advantages of the standard QA
have now even been established using QMC simulation [79] and hardware implementations
[85,131,132].
The idea of quantum tunnelling has been further used by Starchl & Ritsch [17] to establish the
superiority of QA over semi-classical annealing for a realistic system of interacting bosons in the
presence of cavity modes. Using numerical results, it has been shown that there exists a large
parameter regime where the QA provides a better performance than semi-classical annealing.
In addition, we have noted the recent development of parallel quantum computation using
an annealing algorithm [128]. The idea of parallel QA is to solve many independent problems
on a quantum annealer during the same annealing schedule. The authors have checked their
method of parallel QA on D-wave quantum machines and indicated the effectiveness of the
same [128].
Finally, in recent years the progress in developing hardware that performs QA using physical
qubits has gained a tremendous momentum. So far, devices with more than 5000 qubits have been
made available, and employed to study a wide gamut of fields that include condensed matter
systems in and out of equilibrium [93,131,133–135], high-energy physics [136–138], quantum
chemistry [139] and biology [140,141]. Application to various optimization problems has been
developing as well. We reviewed some of the experimental studies using QA hardware. From the
viewpoint of application as well as gaining theoretical rigour, decoherence inherent in a device
coupled to an environment is a fundamental issue of interest. We have briefly reviewed the effects
of thermal and non-thermal environments on QA. In order to perform QA ideally, coupling to
an environment leading to decoherence should be reduced. However, environment-assisted QAs
have been proposed for specific situations [142–144]. Utilizing specially engineered environments
to accelerate QA would be an important direction of future study.

Using the Suzuki–Trotter formula, the partition function for the Hamiltonian in equation (4.3) can
be written as
Z = lim ZM
M→∞

= lim Tr e−(β/M)sλH0 e−(β/M){s(1−λ)VAFF +(1−s)VTF }
M→∞

= lim

M→∞


{σiz }

⎛

⎡

βsλN
{σiz }| ⎝exp ⎣
M

⎡
βs(1 − λ)N
× exp ⎣−
M

1  z
σi
N

1  x
σi
N
N

i=1

N

p

M

⎤
⎦

i=1
2

⎤⎞M
N
β(1 − s)  x ⎦⎠
+
σi
|{σiz },
M

(A 1)

i=1


where {σ z } denotes the summation over all spin configurations in the z basis, and |{σiz } ≡
i
N
z
z
z
z
i=1 |σi . The state |σi  is the eigenstate of σi , having the eigenvalue σi (= ±1). Similar notations
will be used for the x basis.
Following the saddle point method in the limit N → ∞ and static approximation
(i.e. neglecting the imaginary-time dependence of the partition function in equation (A 1)
[114,115,145]), the partition function of the system can be written as

(A 2)
Z = dmz dmx exp[−Nβf (β, s, λ; mz , mx )],
where f (β, s, λ; mz , mx ) is the pseudo free energy defined as follows:
f (β, s, λ; mz , mx ) = (p − 1)sλ(mz )p − s(1 − λ)(mx )2


2 
2
1
− ln 2 cosh β psλ(mz )p−1 + 1 − s − 2s(1 − λ)mx .
β

(A 3)

The saddle point equations are thus
psλ(mz )p−1

2

2
psλ(mz )p−1 + 1 − s − 2s(1 − λ)mx


2 
2
× tanh β psλ(mz )p−1 + 1 − s − 2s(1 − λ)mx ,

(A 4)

1 − s − 2s(1 − λ)mx
mx = 
2 
2
psλ(mz )p−1 + 1 − s − 2s(1 − λ)mx


2 
2
× tanh β psλ(mz )p−1 + 1 − s − 2s(1 − λ)mx .

(A 5)

mz = 

and

To examine quantum phase transitions of the model, we consider low-temperature limits of
the above self-consistent equations. For a finite value of the square root in equations (A 4) and
Downloaded from http://royalsocietypublishing.org/rsta/article-pdf/doi/10.1098/rsta.2021.0417/1326707/rsta.2021.0417.pdf
by guest
on 21 April 2026

...............................................................

Appendix A. Static approximation and low-temperature limit

26

royalsocietypublishing.org/journal/rsta Phil. Trans. R. Soc. A 381: 20210417

Thomas F. Rosenbaum, Diptiman Sen, Parongama Sen, Robin B. Stinchcombe, Ryo Tamura and Shu Tanaka
on this development. A.D. acknowledges Souvik Bandyopadhyay and Sourav Bhattacharjee for comments.
We are grateful to the anonymous referees for their useful comments and important suggestions.
Disclaimer. This review is limited by our personal knowledge and also by the size limit (which we have already
crossed). We do not claim any completeness of discussions on even some important contributions in this
incredibly active field of research.

(A 5), the hyperbolic tangent tends to unity in the limit of β → ∞. Then the equations are given as
(A 6)

and
1 − s − 2s(1 − λ)mx
mx = 
2 
2 .
psλ(mz )p−1 + 1 − s − 2s(1 − λ)mx

(A 7)

In that case, the pseudo free energy (A 3) becomes


2 
2
psλ(mz )p−1 + 1 − s − 2s(1 − λ)mx . (A 8)
f (s, λ; mz , mx ) = (p − 1)sλ(mz )p − s(1 − λ)(mx )2 −
Equations (A 6) and (A 7) provide a ferromagnetic (F) solution with mz > 0 and a quantum
paramagnetic (QP) solution for mz = 0 and mx = 0. Using these properties of a quantum
paramagnetic phase, the regions of QP phases can be found on the s − λ plane. It appears that
there exists two types of QP phases in this problem and we call them QP and QP2 phases to
distinguish them from each other.
The regions of the different phases in terms of system parameters can be calculated using the
above conditions of those phases in equations (A 6) and (A 7). It has been found that the QP phase
exists in the region 0 ≤ s < 1/(3 − 2λ), and its free energy is given by
fQP (s, λ) = −sλ + 2s − 1,

(A 9)

which is independent of p. The free energy of the F phase cannot be calculated analytically for a
general p from equations (A 6) and (A 7). However, in the limit of p → ∞, the free energy of the F
phase is given as
fF (s, λ)|p→∞ = −sλ.

(A 10)

The free energy of the QP2 phase is given by
fQP2 (s, λ) = −

(1 − s)2
,
4s(1 − λ)

(A 11)

with the domain of applicability restricted by 1/(3 − 2λ) ≤ s < 1.

Appendix B. Inhomogeneous driving of the transverse field
(a) Free energy and first-order transitions
By applying Trotter decomposition and the static approximation on the Hamiltonian in equation
(4.4), the resulting free energy at finite temperature is given by [116]



p
p−1
2
f (m; s, τ ) = (1 − τ ) (p − 1)sm − T log 2 cosh β (spm ) + 1
+ τ {(p − 1)smp − T log 2 cosh(βspmp−1 )},

(B 1)

where m is the magnetization of the system along the z-axis. In the limit of zero temperature, the
free energy takes the form



(B 2)
f0 (m; s, τ ) = (1 − τ ) (p − 1)smp − (spmp−1 )2 + 1 + τ {(p − 1)smp − spmp−1 }.
For the calculation of zero-temperature free energy, it has been assumed that m ≥ 0.
Downloaded from http://royalsocietypublishing.org/rsta/article-pdf/doi/10.1098/rsta.2021.0417/1326707/rsta.2021.0417.pdf
by guest
on 21 April 2026

...............................................................

mz = 
2 
2
psλ(mz )p−1 + 1 − s − 2s(1 − λ)mx

27

royalsocietypublishing.org/journal/rsta Phil. Trans. R. Soc. A 381: 20210417

psλ(mz )p−1

Using the standard Landau theory of phase transitions, the locations of the critical points sc , τc
(figure 13) where the first-order transition lines terminate for different p, can be found as



1
27(p − 1)/4(p − 2)3

and sc =

1

p−1 
pmc
1 − m1c 2 /m1c

,

(B 3)

(p − 2)/(3(p − 1)) and mc = τc + (1 − τc )m1c .

(b) Semi-classical theory of energy gap
One can rewrite the Hamiltonian (4.4) in terms of two macroscopic spin operators (for details, see
[116,117]),
1
Sz,x
1 = 2

r
N(1−s
)

σiz,x

and Sz,x
2 =

i=1

as


H(s, τ ) = −sN

2 z
S + Sz2
N 1

1
2

N


σiz,x

(B 4)

i=N(1−sr )+1

p

− 2Sx1 .

(B 5)

These giant operators can be considered as classical vectors for sufficiently large N, and the
quantum fluctuations are subsequently applied around the classically stable directions through
an expansion of the Holstein–Primakoff transformation to the quadratic order in terms of boson
operators, as done in [119,120]. The result is given as

δ 
1 −  2 − 1 + a1 ã†1 ã1 + a2 ã†2 ã2 + b b† b,
(B 6)
H(s, τ ) = Ne + γ +
2
where ã1 and ã2 are bosonic annihilation operators, and e is the energy per spin of the classical
ground-state. The parameters a1 , a2 and b represent quantum fluctuations, where

a1 = δ 1 −  2 and a2 = δ.
(B 7)
Because a2 ≥ a1 , the minimum energy gap of the system is the smaller of a1 and b :
⎫
⎬
 = min(a1 , b )

and
a1 = δ 1 −  2 , b = 2sp{τ + (1 − τ ) cos θ0 }p−1 ,⎭

(B 8)

where
θ0 = arg min{−s[τ + (1 − τ ) cos θ]p − (1 − τ ) sin θ}
θ

2γ
=− ,
δ
1
γ = − sp(p − 1)(1 − τ ) sin2 θ0 {τ + (1 − τ ) cos θ0 }p−2 ,
2
and

δ = b cos θ0 + 2 sin θ0 + 2γ .

(B 9)

References
1. Finnila AB, Gomez MA, Sebenik C, Stenson C, Doll JD. 1994 Quantum annealing: a
new method for minimizing multidimensional functions. Chem. Phys. Lett. 219, 343–348.
(doi:10.1016/0009-2614(94)00117-0)
2. Kadowaki T, Nishimori H. 1998 Quantum annealing in the transverse Ising model. Phys. Rev.
E 58, 5355–5363. (doi:10.1103/PhysRevE.58.5355)
3. Farhi E, Goldstone J, Gutmann S, Lapan J, Lundgren A, Preda D. 2001 A quantum adiabatic
evolution algorithm applied to random instances of an NP-complete problem. Science 292,
472–475. (doi:10.1126/science.1057726)
Downloaded from http://royalsocietypublishing.org/rsta/article-pdf/doi/10.1098/rsta.2021.0417/1326707/rsta.2021.0417.pdf
by guest
on 21 April 2026

...............................................................

where m1c =

1+



royalsocietypublishing.org/journal/rsta Phil. Trans. R. Soc. A 381: 20210417

τc =

28

...............................................................

Downloaded from http://royalsocietypublishing.org/rsta/article-pdf/doi/10.1098/rsta.2021.0417/1326707/rsta.2021.0417.pdf
by guest
on 21 April 2026

29

royalsocietypublishing.org/journal/rsta Phil. Trans. R. Soc. A 381: 20210417

4. Santoro GE, Tosatti E. 2006 Optimization using quantum mechanics: quantum annealing
through adiabatic evolution. J. Phys. A. Math. Gen. 39, R393–R431. (doi:10.1088/03054470/39/36/R01)
5. Das A, Chakrabarti BK. 2008 Colloquium: quantum annealing and analog quantum
computation. Rev. Mod. Phys. 80, 1061–1081. (doi:10.1103/RevModPhys.80.1061)
6. Morita S, Nishimori H. 2008 Mathematical foundation of quantum annealing. J. Math. Phys.
49, 125210. (doi:10.1063/1.2995837)
7. Tanaka S, Tamura R, Chakrabarti BK. 2017 Quantum spin glasses, annealing and computation.
Cambridge, UK: Cambridge University Press.
8. Albash T, Lidar DA. 2018 Adiabatic quantum computation. Rev. Mod. Phys. 90, 015002.
(doi:10.1103/RevModPhys.90.015002)
9. Hauke P, Katzgraber HG, Lechner W, Nishimori H, Oliver WD. 2020 Perspectives of
quantum annealing: methods and implementations. Rep. Prog. Phys. 83, 054401. (doi:10.1088/
1361-6633/ab85b8)
10. Das A, Chakrabarti BK, Stinchcombe RB. 2005 Quantum annealing in a kinetically
constrained system. Phys. Rev. E 72, 026701. (doi:10.1103/PhysRevE.72.026701)
11. Messiah A. 1961 Quantum mechanics. Amsterdam, The Netherlands: North Holland.
12. Suzuki S, Okada M. 2005 Residual energies after slow quantum annealing. J. Phys. Soc. Jpn.
74, 1649–1652. (doi:10.1143/JPSJ.74.1649)
13. Kirkpatrick S, Gelatt Jr CD, Vecchi MP. 1983 Optimization by simulated annealing. Science
220, 671–680. (doi:10.1126/science.220.4598.671)
14. Shankar R. 2012 Principles of quantum mechanics. Berlin, Germany: Springer.
15. Mukherjee S, Chakrabarti BK. 2015 Multivariable optimization: quantum annealing and
computation. Eur. Phys. J. ST 224, 17–24. (doi:10.1140/epjst/e2015-02339-y)
16. Ray P, Chakrabarti BK, Chakrabarti A. 1989 Sherrington-Kirkpatrick model in a transverse
field: absence of replica symmetry breaking due to quantum fluctuations. Phys. Rev. B 39,
11 828–11 832. (doi:10.1103/PhysRevB.39.11828)
17. Starchl EA, Ritsch H. 2022 Unraveling the origin of higher success probabilities in quantum
annealing versus semi-classical annealing. J. Phys. B: At. Mol. Opt. Phys. 55, 025501.
(doi:10.1088/1361-6455/ac489a)
18. Sherrington D, Kirkpatrick S. 1975 Solvable model of a spin-glass. Phys. Rev. Lett. 35,
1792–1796. (doi:10.1103/PhysRevLett.35.1792)
19. Yaacoby R, Schaar N, Kellerhals L, Raz O, Hermelin D, Pugatch R. 2022 Comparison between
a quantum annealer and a classical approximation algorithm for computing the ground state
of an Ising spin glass. Phys. Rev. E 105, 035305. (doi:10.1103/PhysRevE.105.035305)
20. Sondhi SL, Girvin SM, Carini JP, Shahar D. 1997 Continuous quantum phase transitions. Rev.
Mod. Phys. 69, 315–333. (doi:10.1103/RevModPhys.69.315)
21. Sachdev S. 1999 Quantum phase transitions. Cambridge, UK: Cambridge University Press.
22. Suzuki S, Inoue J-I, Chakrabarti BK. 2012 Quantum Ising phases and transitions in transverse
Ising models, vol. 862. Berlin, Germany: Springer.
23. Dutta A, Aeppli G, Chakrabarti BK, Divakaran U, Rosenbaum TF, Sen D. 2015 Quantum
phase transitions in transverse field spin models: from statistical physics to quantum information.
Cambridge, UK: Cambridge University Press.
24. Kibble TWB. 1976 Topology of cosmic domains and strings. J. Phys. A. Math. Gen. 9,
1387–1398. (doi:10.1088/0305-4470/9/8/029)
25. Zurek WH. 1985 Cosmological experiments in superfluid helium? Nature 317, 505–508.
(doi:10.1038/317505a0)
26. Zurek WH, Dorner U, Zoller P. 2005 Dynamics of a quantum phase transition. Phys. Rev. Lett.
95, 105701. (doi:10.1103/PhysRevLett.95.105701)
27. Polkovnikov A. 2005 Universal adiabatic dynamics in the vicinity of a quantum critical point.
Phys. Rev. B 72, 161201. (doi:10.1103/PhysRevB.72.161201)
28. Damski B. 2005 The simplest quantum model supporting the Kibble–Zurek mechanism of
topological defect production: Landau-Zener transitions from a new perspective. Phys. Rev.
Lett. 95, 035701. (doi:10.1103/PhysRevLett.95.035701)
29. Mukherjee V, Divakaran U, Dutta A, Sen D. 2007 Quenching dynamics of a quantum XY
spin-12 chain in a transverse field. Phys. Rev. B 76, 174303. (doi:10.1103/PhysRevB.76.174303)

...............................................................

Downloaded from http://royalsocietypublishing.org/rsta/article-pdf/doi/10.1098/rsta.2021.0417/1326707/rsta.2021.0417.pdf
by guest
on 21 April 2026

30

royalsocietypublishing.org/journal/rsta Phil. Trans. R. Soc. A 381: 20210417

30. Sen D, Sengupta K, Mondal S. 2008 Defect production in nonlinear quench across a quantum
critical point. Phys. Rev. Lett. 101, 016806. (doi:10.1103/PhysRevLett.101.016806)
31. Barankov R, Polkovnikov A. 2008 Optimal nonlinear passage through a quantum critical
point. Phys. Rev. Lett. 101, 076801. (doi:10.1103/PhysRevLett.101.076801)
32. Mukherjee V, Dutta A. 2010 Adiabatic multicritical quantum quenches: continuously
varying exponents depending on the direction of quenching. Europhys. Lett. 92, 37004.
(doi:10.1209/0295-5075/92/37004)
33. Dziarmaga J. 2010 Dynamics of a quantum phase transition and relaxation to a steady state.
Adv. Phys. 59, 1063–1189. (doi:10.1080/00018732.2010.514702)
34. Polkovnikov A, Sengupta K, Silva A, Vengalattore M. 2011 Colloquium: nonequilibrium
dynamics of closed interacting quantum systems. Rev. Mod. Phys. 83, 863–883.
(doi:10.1103/RevModPhys.83.863)
35. Dziarmaga J. 2005 Dynamics of a quantum phase transition: exact solution of the quantum
Ising model. Phys. Rev. Lett. 95, 245701. (doi:10.1103/PhysRevLett.95.245701)
36. Fisher DS. 1992 Random transverse field Ising spin chains. Phys. Rev. Lett. 69, 534–537.
(doi:10.1103/PhysRevLett.69.534)
37. Fisher DS. 1995 Critical behavior of random transverse-field Ising spin chains. Phys. Rev. B
51, 6411–6461. (doi:10.1103/PhysRevB.51.6411)
38. Young AP, Rieger H. 1996 Numerical study of the random transverse-field Ising spin chain.
Phys. Rev. B 53, 8486–8498. (doi:10.1103/PhysRevB.53.8486)
39. Fisher DS, Young AP. 1998 Distributions of gaps and end-to-end correlations in
random transverse-field Ising spin chains. Phys. Rev. B 58, 9131–9141. (doi:10.1103/Phys
RevB.58.9131)
40. Dziarmaga J. 2006 Dynamics of a quantum phase transition in the random Ising model:
logarithmic dependence of the defect density on the transition rate. Phys. Rev. B 74, 064416.
(doi:10.1103/PhysRevB.74.064416)
41. Caneva T, Fazio R, Santoro GE. 2007 Adiabatic quantum dynamics of a random Ising chain
across its quantum critical point. Phys. Rev. B 76, 144427. (doi:10.1103/PhysRevB.76.144427)
42. Suzuki S. 2009 Cooling dynamics of pure and random Ising chains. J. Stat. Mech. Theory Exp.
2009, P03032. (doi:10.1088/1742-5468/2009/03/P03032)
43. Schmitt M, Rams MM, Dziarmaga J, Heyl M, Zurek WH. 2022 Quantum phase transition
dynamics in the two-dimensional transverse-field Ising model. Sci. Adv. 8, eabl6850.
(doi:10.1126/sciadv.abl6850)
44. Botet R, Jullien R. 1983 Large-size critical behavior of infinitely coordinated systems. Phys.
Rev. B 28, 3955–3967. (doi:10.1103/PhysRevB.28.3955)
45. Acevedo OL, Quiroga L, Rodríguez FJ, Johnson NF. 2014 New dynamical scaling
universality for quantum networks across adiabatic quantum phase transitions. Phys. Rev.
Lett. 112, 030403. (doi:10.1103/PhysRevLett.112.030403)
46. Edwards SF, Anderson PW. 1975 Theory of spin glasses. J. Phys. F: Met. Phys. 5, 965–974.
(doi:10.1088/0305-4608/5/5/017)
47. Chakrabarti BK. 1981 Critical behavior of the Ising spin-glass models in a transverse field.
Phys. Rev. B 24, 4062–4064. (doi:10.1103/PhysRevB.24.4062)
48. Rieger H, Young AP. 1994 Zero-temperature quantum phase transition of a two-dimensional
Ising spin glass. Phys. Rev. Lett. 72, 4141–4144. (doi:10.1103/PhysRevLett.72.4141)
49. Guo M, Bhatt RN, Huse DA. 1994 Quantum critical behavior of a three-dimensional Ising
spin glass in a transverse magnetic field. Phys. Rev. Lett. 72, 4137–4140. (doi:10.1103/
PhysRevLett.72.4137)
50. Singh RRP, Young AP. 2017 Critical and Griffiths-McCoy singularities in quantum Ising
spin glasses on d-dimensional hypercubic lattices: a series expansion study. Phys. Rev. E 96,
022139. (doi:10.1103/PhysRevE.96.022139)
51. Miyazaki R, Nishimori H. 2013 Real-space renormalization-group approach to the
random transverse-field Ising model in finite dimensions. Phys. Rev. E 87, 032154.
(doi:10.1103/PhysRevE.87.032154)
52. Matoz-Fernandez DA, Romá F. 2016 Unconventional critical activated scaling of twodimensional quantum spin glasses. Phys. Rev. B 94, 024201. (doi:10.1103/PhysRevB.
94.024201)

...............................................................

Downloaded from http://royalsocietypublishing.org/rsta/article-pdf/doi/10.1098/rsta.2021.0417/1326707/rsta.2021.0417.pdf
by guest
on 21 April 2026

31

royalsocietypublishing.org/journal/rsta Phil. Trans. R. Soc. A 381: 20210417

53. Motrunich O, Mau S-C, Huse DA, Fisher DS. 2000 Infinite-randomness quantum Ising critical
fixed points. Phys. Rev. B 61, 1160–1172. (doi:10.1103/PhysRevB.61.1160)
54. Karevski D, Lin Y-C, Rieger H, Kawashima N, Iglói F. 2001 Random quantum magnets with
broad disorder distribution. Eur. Phys. J. B 20, 267–276. (doi:10.1007/PL00011100)
55. Lin Y-C, Iglói F, Rieger H. 2007 Entanglement entropy at infinite-randomness fixed points in
higher dimensions. Phys. Rev. Lett. 99, 147202. (doi:10.1103/PhysRevLett.99.147202)
56. Iglói F, Monthus C. 2005 Strong disorder RG approach of random systems. Phys. Rep. 412,
277–431. (doi:10.1016/j.physrep.2005.02.006)
57. Iglói F, Monthus C. 2018 Strong disorder RG approach—a short review of recent
developments. Eur. Phys. J. B 91, 290. (doi:10.1140/epjb/e2018-90434-8)
58. Parisi G. 1980 The order parameter for spin glasses: a function on the interval 0-1. J. Phys. A.
Math. Gen. 13, 1101–1112. (doi:10.1088/0305-4470/13/3/042)
59. Binder K, Young AP. 1986 Spin glasses: experimental facts, theoretical concepts, and open
questions. Rev. Mod. Phys. 58, 801–976. (doi:10.1103/RevModPhys.58.801)
60. Young AP. 2017 Stability of the quantum Sherrington-Kirkpatrick spin glass model. Phys.
Rev. E 96, 032112. (doi:10.1103/PhysRevE.96.032112)
61. Mukherjee S, Rajak A, Chakrabarti BK. 2018 Possible ergodic-nonergodic regions in the
quantum Sherrington-Kirkpatrick spin glass model and quantum annealing. Phys. Rev. E
97, 022146. (doi:10.1103/PhysRevE.97.022146)
62. Mukherjee S, Rajak A, Chakrabarti BK. 2015 Classical-to-quantum crossover in the critical
behavior of the transverse-field Sherrington-Kirkpatrick spin glass model. Phys. Rev. E 92,
042107. (doi:10.1103/PhysRevE.92.042107)
63. Rajak A, Chakrabarti B. 2014 Quantum annealing search of Ising spin glass ground
state (s) with tunable transverse and longitudinal fields. Indian J. Phys. 88, 951–955.
(doi:10.1007/s12648-014-0483-9)
64. Leschke H, Manai C, Ruder R, Warzel S. 2021 Existence of replica-symmetry breaking in
quantum glasses. Phys. Rev. Lett. 127, 207204. (doi:10.1103/PhysRevLett.127.207204)
65. Schindler PM, Guaita T, Shi T, Demler E, Cirac I. 2022 A variational ansatz for the ground
state of the quantum Sherrington-Kirkpatrick model. Preprint (https://arxiv.org/abs/2204.
02923)
66. Young AP, Knysh S, Smelyanskiy VN. 2010 First-order phase transition in the quantum
adiabatic algorithm. Phys. Rev. Lett. 104, 020502. (doi:10.1103/PhysRevLett.104.020502)
67. Jörg T, Krzakala F, Semerjian G, Zamponi F. 2010 First-order transitions and the performance
of quantum algorithms in random optimization problems. Phys. Rev. Lett. 104, 207206.
68. Barouch E, McCoy BM, Dresden M. 1970 Statistical mechanics of the XY model. I. Phys. Rev.
A 2, 1075–1092. (doi:10.1103/PhysRevA.2.1075)
69. White SR, Feiguin AE. 2004 Real-time evolution using the density matrix renormalization
group. Phys. Rev. Lett. 93, 076401. (doi:10.1103/PhysRevLett.93.076401)
70. Vidal G. 2004 Efficient simulation of one-dimensional quantum many-body systems. Phys.
Rev. Lett. 93, 040502. (doi:10.1103/PhysRevLett.93.040502)
71. Orús R, Vidal G. 2008 Infinite time-evolving block decimation algorithm beyond unitary
evolution. Phys. Rev. B 78, 155117.
72. Pollmann F, Mukerjee S, Green AG, Moore JE. 2010 Dynamics after a sweep through a
quantum critical point. Phys. Rev. E 81, 020101. (doi:10.1103/PhysRevE.81.020101)
73. King AD et al. 2022 Coherent quantum annealing in a programmable 2000-qubit Ising chain.
Preprint (https://arxiv.org/abs/2202.05847).
74. Trotter HF. 1959 On the product of semi-groups of operators. Proc. Am. Math. Soc. 10, 545–551.
(doi:10.1090/S0002-9939-1959-0108732-6)
75. Suzuki M. 1986 Quantum statistical Monte Carlo methods and applications to spin systems.
J. Stat. Phys. 43, 883–909. (doi:10.1007/BF02628318)
76. Swendsen RH, Wang J-S. 1987 Nonuniversal critical dynamics in Monte Carlo simulations.
Phys. Rev. Lett. 58, 86–88. (doi:10.1103/PhysRevLett.58.86)
77. Nakamura T, Ito Y. 2003 A quantum Monte Carlo algorithm realizing an intrinsic relaxation.
J. Phys. Soc. Jpn. 72, 2405–2408. (doi:10.1143/JPSJ.72.2405)
78. Kadowaki T. 2002 Study of optimization problems by quantum annealing. arXiv: quantph/0205020. (doi:10.48550/ARXIV.QUANT-PH/0205020)

...............................................................

Downloaded from http://royalsocietypublishing.org/rsta/article-pdf/doi/10.1098/rsta.2021.0417/1326707/rsta.2021.0417.pdf
by guest
on 21 April 2026

32

royalsocietypublishing.org/journal/rsta Phil. Trans. R. Soc. A 381: 20210417

79. Santoro GE, Martonák R, Tosatti E, Car R. 2002 Theory of quantum annealing of an Ising spin
glass. Science 295, 2427–2430. (doi:10.1126/science.1068774)
80. Martoňák R, Santoro GE, Tosatti E. 2002 Quantum annealing by the path-integral Monte
Carlo method: the two-dimensional random Ising model. Phys. Rev. B 66, 094203.
81. Martoňák R, Santoro GE, Tosatti E. 2004 Quantum annealing of the traveling-salesman
problem. Phys. Rev. E 70, 057701.
82. Battaglia DA, Santoro GE, Tosatti E. 2005 Optimization by quantum annealing: lessons from
hard satisfiability problems. Phys. Rev. E 71, 066707. (doi:10.1103/PhysRevE.71.066707)
83. Suzuki S. 2011 Kibble–Zurek mechanism in simulated annealing and quantum annealing.
J. Phys.: Conf. Ser. 302, 012046.
84. Wu W, Ellman B, Rosenbaum T, Aeppli G, Reich D. 1991 From classical to quantum glass.
Phys. Rev. Lett. 67, 2076–2079. (doi:10.1103/PhysRevLett.67.2076)
85. Brooke J, Bitko D, Rosenbaum TF, Aeppli G. 1999 Quantum annealing of a disordered
magnet. Science 284, 779–781. (doi:10.1126/science.284.5415.779)
86. Säubert S, Sarkis CL, Ye F, Luke G, Ross KA. 2021 Microscopics of quantum annealing in the
disordered dipolar Ising ferromagnet LiHox Y1−x F4 . Preprint. (https://arxiv.org/abs/2105.
03408)
87. Keesling A et al. 2019 Quantum Kibble–Zurek mechanism and critical dynamics on a
programmable Rydberg simulator. Nature 568, 207–211. (doi:10.1038/s41586-019-1070-1)
88. Johnson MW et al. 2011 Quantum annealing with manufactured spins. Nature 473, 194–198.
(doi:10.1038/nature10012)
89. Denchev VS, Boixo S, Isakov SV, Ding N, Babbush R, Smelyanskiy V, Martinis J, Neven H.
2016 What is the computational value of finite-range tunneling? Phys. Rev. X 6, 031015.
90. Boixo S, Rønnow TF, Isakov SV, Wang Z, Wecker D, Lidar DA, Martinis JM, Troyer M. 2014
Evidence for quantum annealing with more than one hundred qubits. Nat. Phys. 10, 218–224.
(doi:10.1038/nphys2900)
91. Shin SW, Smith G, Smolin JA, Vazirani U. 2014 How ‘quantum’ is the D-Wave machine?
Preprint. (https://arxiv.org/abs/1401.7087)
92. Suzuki S, Das A. 2015 Quantum annealing: The fastest route to quantum computation? Eur.
Phys. J. Spec. Top. 10, 218.
93. Bando Y et al. 2020 Probing the universality of topological defect formation in a
quantum annealer: Kibble–Zurek mechanism and beyond. Phys. Rev. Res. 2, 033369.
(doi:10.1103/PhysRevResearch.2.033369)
94. Venturelli D, Mandrà S, Knysh S, O’Gorman B, Biswas R, Smelyanskiy V. 2015 Quantum
optimization of fully connected spin glasses. Phys. Rev. X 5, 031040.
95. Caldeira AO, Leggett AJ. 1983 Quantum tunnelling in a dissipative system. Ann. Phys. (NY)
149, 374–456. (doi:10.1016/0003-4916(83)90202-6)
96. Leggett AJ, Chakravarty S, Dorsey AT, Fisher MPA, Garg A, Zwerger W. 1987 Dynamics of
the dissipative two-state system. Rev. Mod. Phys. 59, 1–85. (doi:10.1103/RevModPhys.59.1)
97. Amin MH. 2015 Searching for quantum speedup in quasistatic quantum annealers. Phys. Rev.
A 92, 052323. (doi:10.1103/PhysRevA.92.052323)
98. Patanè D, Silva A, Amico L, Fazio R, Santoro GE. 2008 Adiabatic dynamics in open quantum
critical many-body systems. Phys. Rev. Lett. 101, 175701.
99. Patanè D, Amico L, Silva A, Fazio R, Santoro GE. 2009 Adiabatic dynamics of a quantum
critical system coupled to an environment: scaling and kinetic equation approaches. Phys.
Rev. B 80, 024302.
100. Nalbach P, Vishveshwara S, Clerk AA. 2015 Quantum Kibble–Zurek physics in the presence
of spatially correlated dissipation. Phys. Rev. B 92, 014306. (doi:10.1103/PhysRevB.92.014306)
101. Dutta A, Rahmani A, del Campo A. 2016 Anti-Kibble–Zurek behavior in crossing the
quantum critical point of a thermally isolated system driven by a noisy control field. Phys.
Rev. Lett. 117, 080402. (doi:10.1103/PhysRevLett.117.080402)
102. Weinberg P, Tylutki M, Rönkkö JM, Westerholm J, Åström JA, Manninen P, Törmä P, Sandvik
AW. 2020 Scaling and diabatic effects in quantum annealing with a D-Wave device. Phys. Rev.
Lett. 124, 090502. (doi:10.1103/PhysRevLett.124.090502)
103. Hasenbusch M, Pinn K, Vinti S. 1999 Critical exponents of the three-dimensional Ising
universality class from finite-size scaling with standard and improved actions. Phys. Rev.
B 59, 11 471–11 483. (doi:10.1103/PhysRevB.59.11471)

...............................................................

Downloaded from http://royalsocietypublishing.org/rsta/article-pdf/doi/10.1098/rsta.2021.0417/1326707/rsta.2021.0417.pdf
by guest
on 21 April 2026

33

royalsocietypublishing.org/journal/rsta Phil. Trans. R. Soc. A 381: 20210417

104. Karl M, Gasenzer T. 2017 Strongly anomalous non-thermal fixed point in a quenched twodimensional Bose gas. New J. Phys. 19, 093014. (doi:10.1088/1367-2630/aa7eeb)
105. Keck M, Montangero S, Santoro GE, Fazio R, Rossini D. 2017 Dissipation in adiabatic
quantum computers: lessons from an exactly solvable model. New J. Phys. 19, 113029.
(doi:10.1088/1367-2630/aa8cef)
106. Bandyopadhyay S, Bhattacharjee S, Dutta A. 2020 Dynamical generation of Majorana edge
correlations in a ramped Kitaev chain coupled to nonthermal dissipative channels. Phys. Rev.
B 101, 104307. (doi:10.1103/PhysRevB.101.104307)
107. Rossini D, Vicari E. 2020 Dynamic Kibble–Zurek scaling framework for open
dissipative many-body systems crossing quantum transitions. Phys. Rev. Res. 2, 023211.
(doi:10.1103/PhysRevResearch.2.023211)
108. Puebla R, Smirne A, Huelga SF, Plenio MB. 2020 Universal Anti-Kibble–Zurek scaling in
fully connected systems. Phys. Rev. Lett. 124, 230602. (doi:10.1103/PhysRevLett.124.230602)
109. Arceci L, Barbarino S, Rossini D, Santoro GE. 2018 Optimal working point in dissipative
quantum annealing. Phys. Rev. B 98, 064307. (doi:10.1103/PhysRevB.98.064307)
110. Mbeng GB, Arceci L, Santoro GE. 2019 Optimal working point in digitized quantum
annealing. Phys. Rev. B 100, 224201. (doi:10.1103/PhysRevB.100.224201)
111. Suzuki S, Oshiyama H, Shibata N. 2019 Quantum annealing of pure and random Ising chains
coupled to a Bosonic environment. J. Phys. Soc. Jpn. 88, 061003. (doi:10.7566/JPSJ.88.061003)
112. Oshiyama H, Shibata N, Suzuki S. 2020 Kibble–Zurek mechanism in a dissipative transverse
Ising chain. J. Phys. Soc. Jpn. 89, 104002. (doi:10.7566/JPSJ.89.104002)
113. Oshiyama H, Suzuki S, Shibata N. 2022 Classical simulation and theory of quantum
annealing in a thermal environment. Phys. Rev. Lett. 128, 170502. (doi:10.1103/Phys
RevLett.128.170502)
114. Jörg T, Krzakala F, Kurchan J, Maggs AC, Pujos J. 2010 Energy gaps in quantum first-order
mean-field-like transitions: the problems that quantum annealing cannot solve. Eurphys. Lett.
89, 40004.
115. Seki Y, Nishimori H. 2012 Quantum annealing with antiferromagnetic fluctuations. Phys.
Rev. E 85, 051112. (doi:10.1103/PhysRevE.85.051112)
116. Susa Y, Yamashiro Y, Yamamoto M, Nishimori H. 2018 Exponential speedup of quantum
annealing by inhomogeneous driving of the transverse field. J. Phys. Soc. Jpn. 87, 023002.
(doi:10.7566/JPSJ.87.023002)
117. Susa Y, Yamashiro Y, Yamamoto M, Hen I, Lidar DA, Nishimori H. 2018 Quantum annealing
of the p-spin model under inhomogeneous transverse field driving. Phys. Rev. A 98, 042326.
(doi:10.1103/PhysRevA.98.042326)
118. Nishimori H, Ortiz G. 2010 Elements of phase transitions and critical phenomena. Oxford, UK:
Oxford University Press.
119. Seoane B, Nishimori H. 2012 Many-body transverse interactions in the quantum annealing
of the p-spin ferromagnet. J. Phys. A. Math. Theor. 45, 435301. (doi:10.1088/1751-8113/
45/43/435301)
120. Filippone M, Dusuel S, Vidal J. 2011 Quantum phase transitions in fully connected
spin models: an entanglement perspective. Phys. Rev. A 83, 022327. (doi:10.1103/Phys
RevA.83.022327)
121. Matsuura S, Nishimori H, Albash T, Lidar DA. 2016 Mean field analysis of quantum
annealing correction. Phys. Rev. Lett. 116, 220501. (doi:10.1103/PhysRevLett.116.220501)
122. Matsuura S, Nishimori H, Vinci W, Lidar DA. 2019 Nested quantum annealing correction at
finite temperature: p-spin models. Phys. Rev. A 99, 062307. (doi:10.1103/PhysRevA.99.062307)
123. Knysh S, Plamadeala E, Venturelli D. 2020 Quantum annealing speedup of embedded
problems via suppression of Griffiths singularities. Phys. Rev. B 102, 220407.
(doi:10.1103/PhysRevB.102.220407)
124. Griffiths RB. 1969 Nonanalytic behavior above the critical point in a random Ising
ferromagnet. Phys. Rev. Lett. 23, 17–19. (doi:10.1103/PhysRevLett.23.17)
125. McCoy BM. 1969 Incompleteness of the critical exponent description for ferromagnetic
systems containing random impurities. Phys. Rev. Lett. 23, 383–386. (doi:10.1103/Phys
RevLett.23.383)
126. Jałowiecki K, Wieckowski A, Gawron P, Gardas B. 2020 Parallel in time dynamics with
quantum annealers. Sci. Rep. 10, 1.

...............................................................

Downloaded from http://royalsocietypublishing.org/rsta/article-pdf/doi/10.1098/rsta.2021.0417/1326707/rsta.2021.0417.pdf
by guest
on 21 April 2026

34

royalsocietypublishing.org/journal/rsta Phil. Trans. R. Soc. A 381: 20210417

127. Aadit N, Grimaldi A, Carpentieri M, Theogarajan L, Martinis JM, Finocchio G, Camsari KY.
2022 Massively parallel probabilistic computing with sparse Ising machines. Nat. Electron 5,
460–468.
128. Pelofske E, Hahn G, Djidjev HN. 2022 Parallel quantum annealing. Sci. Rep. 12, 1.
129. Guéry-Odelin D, Ruschhaupt A, Kiely A, Torrontegui E, Martínez-Garaot S, Muga JG. 2019
Shortcuts to adiabaticity: concepts, methods, and applications. Rev. Mod. Phys. 91, 045001.
130. Sels D, Polokovnikov A. 2017 Minimizing irreversible losses in quantum systems by local
counterdiabatic driving. Proc. Natl Acad. Sci. USA 114, E3909. (doi:10.1073/pnas.1619826114)
131. King AD et al. 2022 Quantum critical dynamics in a 5000-qubit programmable spin glass.
arXiv: 2207.13800. (doi:10.48550/arXiv.2207.13800)
132. Mohseni N, McMahon PL, Byrnes T. 2022 Ising machines as hardware solvers of
combinatorial optimization problems. Nat. Rev. Phys. 4, 363–379. (doi:10.1038/s42254022-00440-8)
133. Harris R et al. 2018 Phase transitions in a programmable quantum spin glass simulator.
Science 361, 162–165. (doi:10.1126/science.aat2025)
134. Kairys P, King AD, Ozfidan I, Boothby K, Raymond J, Banerjee A, Humble TS. 2020
Simulating the Shastry-Sutherland Ising model using quantum annealing. Phys. Rev. X
Quantum 1, 020320.
135. King AD, Batista CD, Raymond J, Lanting T, Ozfidan I, Poulin-Lamarre G, Zhang H, Amin
MH. 2021 Quantum annealing simulation of out-of-equilibrium magnetization in a spinchain compound. Phys. Rev. X Quantum 2, 030317.
136. Mott A, Job J, Vlimant J-R, Lidar D, Spiropulu M. 2017 Solving a Higgs optimization
problem with quantum annealing for machine learning. Nature 550, 375–379. (doi:10.1038/
nature24047)
137. Das S, Wildridge AJ, Vaidya SB, Jung A. 2019 Track clustering with a quantum annealer
for primary vertex reconstruction at hadron colliders. Preprint. (https://arxiv.org/abs/1903.
08879)
138. Abel S, Spannowsky M. 2021 Quantum-field-theoretic simulation platform for observing the
fate of the false vacuum. Phys. Rev. X Quantum 2, 010389.
139. Teplukhin A, Kendrick BK, Babikov D. 2019 Calculation of molecular vibrational spectra on
a quantum annealer. J. Chem. Theory Comput. 15, 4555–4563. (doi:10.1021/acs.jctc.9b00402)
140. Perdomo-Ortiz A, Dickson N, Drew-Brook M, Rose G, Aspuru-Guzik A. 2012 Finding
low-energy conformations of lattice protein models by quantum annealing. Sci. Rep. 2, 1.
(doi:10.1038/srep00571)
141. Dusko A, Delgado A, Saraiva A, Koiller B. 2018 Quantum annealing versus classical machine
learning applied to a simplified computational biology problem. NPJ Quantum Inf. 4, 1.
(doi:10.1038/s41534-017-0051-1)
142. Amin MHS, Love PJ, Truncik CJS. 2008 Thermally assisted adiabatic quantum computation.
Phys. Rev. Lett. 100, 060503. (doi:10.1103/PhysRevLett.100.060503)
143. Dickson NG et al. 2013 Thermally assisted quantum annealing of a 16-qubit problem. Nat.
Commun. 4, 1903. (doi:10.1038/ncomms2920)
144. Mishra A, Albash T, Lidar DA. 2018 Finite temperature quantum annealing solving
exponentially small gap problem with non-monotonic success probability. Nat. Commun. 9,
2917. (doi:10.1038/s41467-018-05239-9)
145. Bapst V, Semerjian G. 2012 On quantum mean-field models and their quantum annealing.
J. Stat. Mech.: Theory Exp. 2012, P06007. (doi:10.1088/1742-5468/2012/06/P06007)

