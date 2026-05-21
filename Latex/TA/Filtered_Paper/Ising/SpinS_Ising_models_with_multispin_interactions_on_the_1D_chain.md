Spin-S Ising models with multispin interactions on the one-dimensional chain and
two-dimensional square lattice
Kohei Suzuki

arXiv:2410.14360v3 [cond-mat.stat-mech] 16 Feb 2025

Jij Inc., Bunkyo-ku, Tokyo 113-0031, Japan
We study spin-S Ising models with p-spin interactions on the one-dimensional chain and the twodimensional square lattice. Here, S denotes the magnitude of the spin and p represents the number
of spins involved in each interaction. The analysis is performed for S = 1/2, 1, 3/2, 2 and p = 3, 4, 5.
For the one-dimensional model, we formulate transfer matrices and numerically diagonalize them
to analyze the temperature dependence of the free energy and spin-spin correlations. In the case
of S = 1/2, the free energy does not depend on p, and the spin-spin correlations are uniformly
enhanced across all temperature scales as p increases. In contrast, for S ≥ 1, the free energy varies
with p, and the spin-spin correlations are significantly enhanced at lower temperatures as p increases.
For the two-dimensional model, by using multicanonical simulations, we analyze physical quantities
such as an order parameter, internal energy, and specific heat. In addition, we define and examine
an order parameter to distinguish ordered and disordered phases. It is found that a first-order phase
transition occurs at finite temperatures for all S and p ≥ 3, and increasing p strengthens its nature.
We present S and p dependence of the transition temperature and latent heat, and discuss effects
of higher-order interactions on the nature of phase transitions.

I.

INTRODUCTION

The Ising model, a representative example of classical
spin systems, and its variations have been extensively
studied for a long time since it was discussed by Lenz
[1] and Ising [2]. In the field of statistical physics, the
two-dimensional Ising model [3] is one of the most wellknown models to be analyzed exactly and exhibit a phase
transition at finite temperatures. In these models, two
spins interact with each other through two-body interactions. In terms of interactions, the Ising model can be
extended by introducing p-body interactions with p ≥ 3.
Systems with such higher-order interactions have been
studied for a long time because of their intriguing properties. For one-dimensional systems, although there are
no phase transitions at finite temperatures, some studies have been conducted on the relation with satisfiability problems [4], the free energy and spin correlations
[5, 6], and the correspondence with two-dimensional systems under an external magnetic field [6].
Regarding two-dimensional systems, they exhibit
phase transitions at finite temperatures and have attracted significant interest owing to their remarkable features. For instance, the eight-vertex model [7, 8] is known
to be mapped onto the square-lattice Ising model with
two- and four-body interactions [9, 10]. On the triangular lattice, an Ising model with three-body interactions
has been solved by Baxter and Wu [11–13]. While the
transition temperature of this system is the same as that
of the conventional square-lattice Ising model, its universality class corresponds to that of the four-state Potts
model [14].
Furthermore, an Ising model with p-body interactions
in one direction and two-body interactions in the other
on the rectangular lattice [15, 16] has been extensively
studied. Analysis utilizing self-duality reveals that the
transition temperature is identical to that of the square-

lattice Ising model, independent of p. For p = 3, the
phase transition is second-order and its universality class
belongs to that of four-state Potts model, and for p ≥ 4,
the transition becomes first-order. As a further extension, an Ising model with p-body interactions in both
directions on a square lattice is a natural extension of
two-body interactions in the Ising model. This model is
also self-dual and the transition temperature is expected
to be the same as that of the p = 2 case [17].
All the studies mentioned so far have focused on S =
1/2 spin systems. One can extend the Ising model by
considering general spin S. In general, such large spins
can emerge as effective degrees of freedom through interactions. From an application perspective, combinatorial
optimization problems can be mapped onto Ising models [18], and spin-S Ising models naturally correspond
to integer programming problems. In the case of usual
two-body interactions, these types of models are known
as Blume-Capel models [19, 20], which have been studied from the perspective of the tricritical point arising
from the competition between uniaxial anisotropy and
two-body interactions.
So far we have mentioned two types of extension to
the conventional Ising model: introducing p-spin interactions and considering spin-S systems. While these extensions have been studied individually, there are few studies
on models that incorporate both extensions. The physical properties of such systems are quite interesting and
these systems correspond to integer programming problems with higher-order terms in the context of mathematical optimization [18]. Thus, it is important to understand their basic properties for practical applications.
In this paper, we investigate two fundamental spin-S
Ising models with p-spin interactions, varying both S and
p up to S = 2 and p = 5 to explore how these changes affect the properties of the system. The first one is defined
on a one-dimensional chain, where we can define transfer matrices and obtain numerically exact results. The

2
second one is on a two-dimensional square lattice, which
shows phase transitions at finite temperatures and can
be analyzed using classical Monte Carlo simulations.
This paper is organized as follows. In Sec. II, we analyze the model on the one-dimensional chain. We define
a transfer matrix and perform numerical analysis to investigate the free energy and spin-spin correlations. In
Sec. III, we examine the two-dimensional square lattice
model. We employ the multicanonical [21–23] and the
Wang-Landau methods [24, 25], examining the nature of
phase transition through the typical physical quantities,
such as an order parameter, internal energy, and specific
heat. Finally, in Sec. IV, we summarize our results.
II.

ONE-DIMENSIONAL SYSTEMS

It is well-known that one-dimensional classical spin
systems with only finite-range interactions do not exhibit phase transitions at finite temperatures. The model
analyzed here does not show a phase transition either.
However, the behavior of certain physical quantities on p
remains interesting. In this section, we analyze the onedimensional spin-S Ising model with p-spin interactions.
We investigate the temperature dependence of the free
energy and the spin correlation functions. The former is
a fundamental physical quantity because it contains all
the thermodynamic information of the system, while the
latter reflects the magnetic properties of the system. By
analyzing these quantities, we aim to clarify the effects
of the number of spins involved in the interactions, p, on
the system.
This section is organized as follows: First, we define
the one-dimensional spin-S Ising model with p-spin interactions. Next, we introduce the transfer matrix to
calculate the free energy and spin correlation functions.
Finally, by numerically diagonalizing the transfer matrix,
we examine the effects of p on the free energy and on the
correlation length of the spin correlation functions.

FIG. 1. The schematic picture for the spin-S Ising model
with p-spin interactions on the one-dimensional chain for p =
3. Gray circles represent the spins.

ΩS is the set of possible values for spin variables. For
example, Ω1/2 = {−1, +1} for S = 1/2, and Ω1 =
{−1, 0, +1} for S = 1. This normalization restricts the
values of the spins to −1 ≤ si ≤ +1, which leads to
−JN ≤ Echain (s) ≤ JN ensuring comparable energy
scales for different p and S. To simplify some of the calculations, we restrict N to be a multiple of p, i.e., it is
assumed that N = pM with M being a non-negative
integer, which does not affect the results in the thermodynamic limit (N → ∞).
B.

Transfer matrix

Next, we introduce the transfer matrix to calculate the
partition function. Let us start by rewriting Eq. (1) using
the assumption that N is a multiple of p: N = pM . By
dividing Eq. (1) into terms for each p, we get
Echain (s) = −J

p
M X
X

Model

The one-dimensional spin-S Ising model with p-spin
interactions is defined by
Echain (s) = −J

N p−1
X
Y

si+j .

(1)

i=1 j=0

Here, N represents the system size and si denotes the
spin variable at the site i. We assume a ferromagnetic
interaction J > 0, and impose the periodic boundary
conditions: si+N = si for i = 1, 2, . . . , N . The schematic
illustration for the p = 3 model is shown in Fig. 1. The
values of si are normalized by the magnitude of the spin
S as follows:


−S −S + 1
S
,
,...,
.
(2)
si ∈ ΩS , ΩS =
S
S
S

spi+j .

(3)

i=1 k=1 j=−p+k

This allows us to express the partition function as
X
Z=
exp [−βEchain (s)]
s

=

M
XY


exp βJ

s i=1

A.

k−1
Y

p
X

k−1
Y


spi+j  ,

(4)

k=1 j=−p+k

P
with
β = 1/TPbeing inverse temperature. Here s =
P P
s1
s2 , . . . ,
sN represents the summation over all
spin variables. One can carry out the summation over
the spin variables with indices that are multiples of p:


p
M
k−1
X XY
X
Y
Z=
exp βJ
spi+j 
s\sp sp i=1

=

M
XY
X
s\sp i=1 spi ∈ΩS

k=1 j=−p+k


exp βJ

p
X

k−1
Y


spi+j  ,

(5)

k=1 j=−p+k

P
P P
P
where
s2p · · ·
sM p represents the sumsp =
sp
mation over the spin P
variables with indices that are
multiples of p, and
s\sp represents the summation
over
the
remaining
spin variables.
The term
P
spi ∈ΩS exp(· · · ) depends on the 2p − 2 spin variables:

3
spi−p+1 , spi−p , . . . , spi−1 and spi+1 , spi+2 , . . . , spi+p−1 .
This term can be considered as a matrix element of the
transfer matrix T̂ . We introduce its element as
T̂(spi−p+1 ,...,spi−1 ),(spi+1 ,...,spi+p−1 )


p
k−1
X
Y
X
exp βJ
spi+j  .
=
spi ∈ΩS

(a)

(b)

(c)

(d)

(6)

k=1 j=−p+k

The partition function can be expressed in terms of this
transfer matrix as follows:
Z=

M
XY

T̂(spi−p+1 ,...,spi−1 ),(spi+1 ,...,spi+p−1 )

s\sp i=1

=

X

=

X

···

s1

X

M
T̂(s
1 ,...,sp−1 ),(spM +1 ,...,spM +p−1 )

sp−1

···

s1

X

M
T̂(s
1 ,...,sp−1 ),(s1 ,...,sp−1 )

sp−1

= Tr[T̂

M

].

(7)

Note that we use the relations si+N = si for i =
1, 2, . . . , N and N = pM . As an example, we present
the transfer matrix for S = 1/2 and p = 2. The matrix
elements are given by
T̂(s2i−1 ),(s2i+1 )
X
=
exp (βJ(s2i−1 s2i + s2i s2i+1 ))
s2i ∈{−1,+1}

= 2 cosh(βJ(s2i−1 + s2i+1 )),

(8)

and the transfer matrix is


T̂(+1),(+1) T̂(+1),(−1)
T̂ =
T̂(−1),(+1) T̂(−1),(−1)


cosh(2βJ)
1
=2
.
1
cosh(2βJ)

(9)

p−1

λM
i .

(10)

i=1

C.

Free energy

Now, we calculate the free energy and examine its dependence on p. The free energy per spin can be obtained
from the partition function as follows:
1

fp (T ) = −T lim

N →∞ N

log Z

1
log λM
1
N →∞ N

= −T lim

1

= −T log λ1p ,

where log Z represents the natural logarithm of Z and
T is the temperature. Note that we set the Boltzmann
constant kB as 1. The free energy can be determined by
finding the largest eigenvalue λ1 of the transfer matrix
T̂ . For S = 1/2, the largest eigenvalue for any p can be
calculated analytically [6] as
p

λ1 = [2 cosh(βJ)] .

(12)

Thus, the free energy for S = 1/2 is

The transfer matrix introduced here is a real square matrix of size (2S + 1)(p−1) × (2S + 1)(p−1) . Denoting its
eigenvalues by λ1 ≥ λ2 ≥ · · · λ(2S+1)p−1 , the partition
function can finally be expressed as:
h
i (2S+1)
X
M
Z = Tr T̂
=

FIG. 2. Temperature T dependence of the free energy per
site fp (T ) for (a) S = 1/2, (b) S = 1, (c) S = 3/2, and (d)
S = 2. In the case of S = 1/2, the free energy takes the form
fp (T ) = −T log [2 cosh (βJ)], which is independent of p.

(11)

fp (T ) = −T log [2 cosh (βJ)] ,

(13)

which is equal to that of the conventional onedimensional Ising model and independent of p.
In contrast, for S ≥ 1, the free energy depends on p.
Since it is difficult to calculate analytically for S ≥ 1,
we confirm this by numerically diagonalizing the transfer
matrix. The results are shown in Fig. 2. For S = 1/2,
one can see that the free energy actually does not change
with p [Fig. 2(a)], while for S ≥ 1, the free energy increases as p increases [Figs. 2(b)-2(d)] especially for the
intermediate temperature range. For low temperatures,
the influence of p is small, and the free energy converges
to −1, reflecting the fact that the ground state energy
per site is −1 for any p.
In the case of S = 1/2, since the product of any number
of spins only takes the values −1 or +1, eliminating p
dependence,
Q this product can be regarded as a new spin
variable: i si ∈ {−1, +1}. As a result, the free energy
becomes independent of p. By using this property, one
can directly calculate the free energy for S = 1/2 without
defining the transfer matrix. For S ≥ 1, this property
does not hold and the free energy depends on p.

4

(a)

(b)

(c)

(d)

FIG. 3. Temperature T dependence of the spin-spin correlation length ξp (T ) for (a) S = 1/2, (b) S = 1, (c) S = 3/2,
and (d) S = 2. In the case of S = 1/2, the correlation length
takes the form ξp (T ) = −p/[2 log tanh(βJ)].

D.

Spin-spin correlations

The spin correlation function reflects the magnetic
properties of the system. Since the model analyzed here
does not show a phase transition, the spin correlation
function exhibits exponential decay at finite temperatures for any S and p. However, by comparing the correlation length, we can investigate the effects of the number
of spins involved in the interactions, p, on the magnetic
properties of the system. The spin correlation function
is defined as follows:
1 X
si sj exp [−βEchain (s)] .
(14)
⟨si sj ⟩ =
Z s
From the symmetry of the system discussed in Ref. [6],
⟨si sj ⟩ for any S and p takes zero if the distance between
two spins is not a multiple of p:
⟨si sj ⟩ = 0,

|j − i| =
̸ mp,

(15)

Here, a only depends on the temperature, and ξp (T ) is
the correlation length. It is well known that the correlation length can be expressed using the largest and second largest eigenvalues of the transfer matrix. Since the
transfer matrix in Eq. (6) connects spins separated by a
distance of p, the spin-spin correlation function takes the
following form:
⟨si sj ⟩ = a

λ2
λ1

 |i−j|
p
.

(b)

(c)

(d)

FIG. 4. Temperature T dependence of the ratio of correlation
lengths rp (T ) for (a) S = 1/2, (b) S = 1, (c) S = 3/2,
and (d) S = 2. In the case of S = 1/2, the ratio takes
the form rp (T ) = p/2. The dashed lines indicate the value
corresponding to Sp.

From Eqs. (16) and (17), the correlation length can be
obtained using the largest eigenvalue λ1 and the second
largest eigenvalue λ2 :
ξp (T ) = −

(17)

p
.
log λλ21

(18)

Now, let us discuss the results. Figure 3 shows the
temperature dependence of ξp (T ). One can see that the
correlation length increases for any S as p increases. This
is because increasing p extends the range of the interaction, making it easier for spins to align. To make it easier
to see the effects of adjusting p, we define the ratio of correlation lengths as
rp (T ) =

where m is a non-negative integer. On the other hand, if
the distance between the spins is a multiple of p, ⟨si sj ⟩
decays exponentially as follows:


|j − i|
⟨si sj ⟩ = a exp −
, |j − i| = mp.
(16)
ξp (T )



(a)

ξp (T )
.
ξp=2 (T )

(19)

This ratio represents the magnification of ξp (T ) compared to the correlation length for p = 2. The temperature dependence of rp (T ) is shown in Fig. 4. For
S = 1/2, rp does not depend on the temperature and
takes a constant value: rp = Sp = p2 . This can be analytically calculated and the correlation length is given by
ξp = −p/[2 log tanh(βJ)] [6], confirming that rp = p/2.
In contrast, for S ≥ 1, rp depends on the temperature.
However, at low temperatures, rp shows a similar behavior and converges to rp = Sp at zero temperature.
Furthermore, for larger S and p, rp reaches the maximum value at low temperatures. We conclude that the
number of spins involved in the interaction p enhances
the magnetic properties of the system mostly in the low
temperature region and the correlation length takes the
simple form ξp (T ) ≃ Sp × ξp=2 (T ) around zero temperature.

5
III.

(a)

TWO-DIMENSIONAL SYSTEMS

(b)

(c)

(d)

6
5

Unlike the one-dimensional model analyzed previously
[Eq. (1)], two-dimensional classical spin systems exhibit
phase transitions at finite temperatures. In this section,
we explore how the number of interacting spins, p, influences the nature of phase transitions. In the following, we
first introduce the spin-S Ising model with p-spin interactions on the two-dimensional square lattice. We analyze
the models for S = 1/2, 1, 3/2, 3 and p = 3, 4, 5 as in
the one-dimensional models. Next, an order parameter
is introduced to distinguish between the ordered and disordered phases. We then briefly explain the numerical
methods used to analyze the model. Finally, we discuss
the results and the nature of the phase transitions.

A.

Model and order parameter

We start by introducing the spin-S Ising model with
p-spin interactions on the two-dimensional square lattice.
The model is described by
!
p−1
p−1
L
L X
Y
Y
X
six ,iy +k +
six +k,iy .
Esq (s) = −J
ix =1 iy =1

k=0

k=0

(20)
Here, L represents the length of a side of the square lattice, and p ≥ 2 is the number of interacting spins. To suppress finite size effects, we restrict L to be a multiple of p,
i.e. L = pM with M being a non-negative integer. This
restriction does not affect thermodynamic-limit results
and simplifies their estimation. six ,iy denotes the spin
variable at the coordinate (ix , iy ) and these spins are normalized to take values in ΩS . See Eq. (2) for details. The
periodic boundary conditions are imposed to the system
and the spin variables satisfy six +L,iy = six ,iy +L = six ,iy
for ix , iy = 1, 2, . . . , L. J > 0 is the magnitude of the
interactions and we set J = 1 as an energy unit. Under
these conditions, the energy range of Esq (s) for any p
and S is −2L2 ≤ Esq (s) ≤ 2L2 and the energy scales are
comparable for different p and S. Note that Esq (s) for
p = 2 and S = 1/2 corresponds to the conventional Ising
model on the square lattice.
Next, we define an order parameter to determine
whether the system is in an ordered phase or not. The
PL PL
magnetization m = ix =1 iy =1 six ,iy /L2 is commonly
used to distinguish the magnetic phases for conventional
Ising models. Since the spin-inversion symmetry does not
break and the magnetization m takes always zero for the
finite size systems, the squared magnetization m2 is also
used for finite-size numerical calculations.
For our models, it is true that the expectation value
of the squared magnetization ⟨m2 ⟩ takes non-zero values
in the ordered phase. Let us confirm this for the p = 3
model as an example. Considering the ground states,
the spin configurations for p = 3 are 16-fold degener-

4
3
2
1
1

0.0
(e)

2

3

4

5

6

1

2

3

0.2

4

5

6

1

3

4

5

6

1

0.6

0.4
(f)

2

(g)

2

3

0.8

4

5

6

1.0

(h)

FIG. 5. Typical ground-state spin configurations (a)–(d) and
their Fourier intensities I(qx , qy ) (e)–(h) for S = 1/2, p = 3,
and L = 6. The configurations and their Fourier intensities
correspond to (a) and (e), (b) and (f), (c) and (g), and (d)
and (h), respectively.

2

ate. In general, the ground state is 2(p−1) -fold degenerate if L is a multiple of p. We show typical ground
states for L = 6 in Figs. 5(a)-5(d). In addition, there
are eight similar ground states obtained by using translational symmetry from the configuration in Fig. 5(b)
and two similar ground states each from Figs. 5(c) and
5(d), resulting in a total of 16 states. One can easily
confirm that the squared magnetization for each state is
⟨m2 ⟩ = 1 for Fig. 5(a), ⟨m2 ⟩ = 1/81 for Fig. 5(b), and
⟨m2 ⟩ = 1/9 for Figs. 5(c) and 5(d). Since each of the 16
states appears randomly in the ground state, the expectation value of the squared magnetization is calculated
as ⟨m2 ⟩ = (1 + 9/81 + 6/9)/16 = 1/9, and from similar
calculations, one can obtain ⟨m⟩ = 0 in the ground state.
Although the squared magnetization m2 takes nonzero
values at low temperatures, there are more relevant order parameters for the systems with p ≥ 3.
To define more relevant order parameters, we here consider the Fourier intensity:
2

L
L
1 X X
I(qx , qy ) = 2
si ,i ei(qx ix +qy iy ) .
L i =1 i =1 x y
x

(21)

y

Here, qx , qy = 0, 2π/L, . . . , 2π(L − 1)/L is the wave number and i represents the imaginary unit. The squared
magnetization corresponds to I(0, 0) and the Fourier intensity I(qx , qy ) introduced here can be regarded as a
generalization of the order parameter for classical spin
systems. Figures 5(e)-5(h) show I(qx , qy ) for the configurations shown in Figs. 5(a)-5(d). The configurations
and their Fourier intensities correspond to Figs. 5(a)
and 5(e), 5(b) and 5(f), 5(c) and 5(g), and 5(d) and 5(h)
respectively. Although there are 16 states in the ground

6
state, the Fourier intensities are translation invariant and
there are only four types as shown in Figs. 5(e)-5(h). One
can see that I(qx , qy ) takes nonzero values in the case that
(qx , qy ) ∈ {0, 2π/3, 4π/3} × {0, 2π/3, 4π/3}. The sum of
these Fourier intensities takes 1 in the ground state for
p = 3. Generalizing these arguments, we define the order
parameter for p ≥ 3 as
X X
I(qx , qy ),
(22)
O=
qx ∈Qp qy ∈Qp

where

Qp =


2nπ
n = 0, 1, . . . , p − 1 .
p

(23)

One can easily calculate the canonical expectation values
of O [Eq. (25)] in the ground state and high temperature
limit:
lim ⟨O⟩ = 1,

T →0

lim ⟨O⟩ =

T →∞

p2
.
L2

(24)

Note that in the thermodynamic limit (L → ∞), ⟨O⟩ becomes zero at high temperatures. We use the order parameter O defined in Eq. (22) to distinguish the ordered
and disordered phases. ⟨O⟩ ∼ 1 at finite temperatures
indicates that the system is in the ordered phase.
B.

Methods

As will be discussed later, the model analyzed here
exhibits a first-order phase transition. Conventional
classical Monte Carlo simulations such as the Metropolis method [26, 27] and the heat bath method [28] often struggle with such transitions since the systems get
trapped in metastable states which is typical of firstorder phase transitions. Cluster update methods such as
the Swendsen-Wang algorithm [29] and Wolff algorithm
[30] are known to be powerful computational methods for
the standard two-dimensional Ising models. These techniques overcome critical slowing down associated with
second-order phase transitions. However, it is difficult
to directly apply these methods to systems with higherorder interactions. One method that has overcome these
difficulties is the self-learning Monte Carlo method [31],
which has indeed been applied to Ising models with
higher-order interactions, in which the system exhibits
second-order phase transitions.
In this paper, we employ the multicanonical method
[21–23] and the Wang-Landau method [24, 25], which are
particularly effective for systems undergoing first-order
phase transitions. These methods sample states by performing a random walk in the energy space, effectively
avoiding traps in metastable states. Our analysis proceeded as follows. Initially, we utilized the Wang-Landau
method to estimate the density of states D(E) with E
being the energy of the system. We updated
√ the modification factor f (see Ref. [24] for details) to f when the

minimum value of the energy histogram reached 95% of
−8
its average, continuing until f reached e10 ≃ 1 + 10−8 .
The energy range was divided into up to 16 segments,
and Wang-Landau calculations for each energy segment
were carried out in parallel. Single-threaded calculations
were also performed using the symmetry of the system
without dividing the energy range. In this case, all negative energies that appeared during the simulation were
treated as positive energies and occurrences of the state
with E = 0 were counted twice. From these treatments
we have obtained D(E) with E ≥ 0 approximately twice
as fast. Finally, the density of states in the negative
energy range was determined so that D(−E) = D(E).
This method has the advantage that the boundary effects do not appear near E = 0, compared to the method
in which the simulation is limited to the region with positive or negative energy range. Note, however, that this
method loses its advantages if parallel calculations are
performed by dividing the energy range. If the energy
range is divided, the boundary effects may appear at the
joints of the energy segments.
After estimating D(E), we performed the multicanonical simulations and improved the estimated D(E). During each sweep of the simulations, we also stored the
order parameter O(E) [Eq. (22)] every time a state was
updated. To reduce computation time, instead of recalculating the order parameter every time, the order
parameter is calculated by updating its difference. The
number of sweeps conducted was 108 for the models with
S = 1/2 and 1, and 109 for those with S = 3/2 and
2. All calculations were performed five times for system
sizes up to L2 = 60 × 60.
C.

Results

In this subsection, we explain simulation results for
the spin-S Ising model with p-body interactions on a
square lattice [Eq. (20)] with S = 1/2, 1, 3/2, 2 and
p = 3, 4, 5. First, the temperature dependence of the
order parameter [Eq. (22)] and internal energy will be
shown. Next, by examining the energy distribution near
the transition point, we confirm that the system shows
a first-order phase transition. We then extrapolate the
latent heat and transition temperature associated with
the first-order transition in the thermodynamic limit. Finally, to verify the accuracy of the transition temperature
by a different method, we calculate the Binder ratio of
the order parameter for p = 3 by the conventional Monte
Carlo simulations with single spin flips.
We begin by presenting the results for the order parameter O(T ), which is defined as the expectation value
of O [Eq. (22)]:
P
D(E)O(E)e−βE
O(T ) := ⟨O⟩ = EP
.
(25)
−βE
E D(E)e
Here, O(E) is the order parameter corresponding to the
energy E and obtained through multicanonical simula-

7
(a)

(b)

(c)

(a)

(b)

(c)

(d)

(e)

(f)

(d)

(e)

(f)

(g)

(h)

(i)

(g)

(h)

(i)

(j)

(k)

(l)

(j)

(k)

(l)

FIG. 6. Temperature T dependence of the order parameter
O(T ) for (a) S = 1/2, p = 3, (b) S = 1/2, p = 4, (c) S =
1/2, p = 5, (d) S = 1, p = 3, (e) S = 1, p = 4, (f) S = 1, p = 5,
(g) S = 3/2, p = 3, (h) S = 3/2, p = 4, (i) S = 3/2, p = 5,
(j) S = 2, p = 3, (k) S = 2, p = 4, and (l) S = 2, p = 5.
Average values from five independent runs are shown here.
The maximum standard deviation is ∼ 10−5 and too small to
be visible on the graph for all results.

tions. D(E) is the density of states and β = 1/T is the
inverse temperature. We show temperature dependence
of O(T ) for S = 1/2, 1, 3/2, 2 and p = 3, 4, 5 in Fig. 6.
One can see that for all p and S, the order parameter
O(T ) approaches zero at high temperatures and 1 at low
temperatures. Additionally, in the intermediate temperature range, O(T ) changes abruptly from zero to a positive value. These tendencies become more pronounced
as the system size L2 increases. In the thermodynamic
limit, O(T ) is expected to jump from zero to a positive
value, suggesting that the system undergoes a first-order
phase transition. One can also see that the jump in the
order parameter at the transition point tends to increase
with the rise in S and p.
The estimated transition temperatures for p = 3, 4, 5
are Tc ∼ 2.3 for S = 1/2, Tc ∼ 1.6 for S = 1, Tc ∼ 1.4 for
S = 3/2, and Tc ∼ 1.2 for S = 2. The transition temperature decreases as the magnitude of the spin increases.
This tendency aligns with the behavior for p = 2 models,

FIG. 7. Temperature T dependence of the internal energy
u(T ) for (a) S = 1/2, p = 3, (b) S = 1/2, p = 4, (c) S =
1/2, p = 5, (d) S = 1, p = 3, (e) S = 1, p = 4, (f) S = 1, p = 5,
(g) S = 3/2, p = 3, (h) S = 3/2, p = 4, (i) S = 3/2, p = 5,
(j) S = 2, p = 3, (k) S = 2, p = 4, and (l) S = 2, p = 5.
Average values from five independent runs are shown here.
The maximum standard deviation is ∼ 10−4 and too small to
be visible on the graph for all results.

where the temperature of second-order phase transition
is Tc = 2.269... [3] for S = 1/2, Tc ≃ 1.68 − 1.71 [32–36]
for S = 1, Tc ≃ 1.46 [33] for S = 3/2, and Tc ≃ 1.32−1.69
[37–40] for S = 2, indicating a consistent decrease as S
increases.
Next, we show results of the internal energy density
defined by
P
D(E)Ee−βE
⟨E⟩
1
.
(26)
u(T ) := 2 = 2 PE
−βE
L
L
E D(E)e
Since the spin variables are normalized to take values
from −1 to 1 [Eq. (2)], the energy density in the ground
state is −2 for all p and S. The temperature dependence
of the internal energy u(T ) for S = 1/2, 1, 3/2, 2 and p =
3, 4, 5 is shown in Fig. 7, and indeed, it converges to −2 at
low temperatures. The important thing is that u(T ) also
changes abruptly at finite temperatures, and this change
occurs at the same temperature ranges predicted by the
order parameter as shown in Fig. 6. Additionally, the

8
(a)

3 2.280 42
4 2.286 44
5 2.306 40

(b)

(a)

(b)

(c)

(d)

(d)

(e)

(f)

(g)

(h)

(i)

(j)

(k)

(l)

3 1.670 42
4 1.694 44
5 1.735 40

(c)

3 1.401 42
4 1.404 44
5 1.424 40

3 1.252 42
4 1.238 44
5 1.243 40

FIG. 8. Energy E dependence of canonical energy distribution P (E, T ) near the transition temperature for (a) S = 1/2,
(b) S = 1, (c) S = 3/2, and (d) S = 2. The distribution
is normalized for its maximum value to be 1. The data are
obtained from single multicanonical simulation.

abrupt changes in u(T ) become more pronounced as the
system size increases, and its change increases with p and
S. These results indicate that the system exhibits the
first-order phase transition, consistent with the results
from the order parameter. The results also suggest that
increasing p and S results in larger latent heat.
To more directly confirm that the system undergoes
a first-order transition, we examine the canonical energy
distribution P (E, T ), which is defined as follows:
P (E, T ) := D(E)e−βE .

(27)

The energy dependence of P (E, T ) near the transition
temperature is shown in Fig. 8. Note that P (E, T ) is
normalized for its maximum value to be 1. For all values
of p and S, the energy distributions exhibit double-peak
structures, showing a characteristic feature of first-order
phase transitions [41]. Furthermore, the energy gap between two peaks widens as p and S increase, reflecting
an increase in latent heat for first-order phase transitions.
These results are consistent with those of the order parameter and the internal energy.
So far, we have discussed the finite-size results. We
then estimate physical quantities in the thermodynamic
limit from these results. We start by discussing the transition temperature. For this purpose, we define finite-size
“transition temperature” as the temperature which gives
the maximum value of the specific heat:
Tc (L) := arg max c(T ).

(28)

T

Here, the specific heat is defined as the derivative of the
internal energy density and can be calculated by
2

c(T ) :=

∂
1 ⟨E 2 ⟩ − ⟨E⟩
u(T ) = 2
.
∂T
L
T2

(29)

FIG. 9. Temperature T dependence of the specific heat per
system size c(T ) for (a) S = 1/2, p = 3, (b) S = 1/2, p = 4,
(c) S = 1/2, p = 5, (d) S = 1, p = 3, (e) S = 1, p = 4, (f)
S = 1, p = 5, (g) S = 3/2, p = 3, (h) S = 3/2, p = 4, (i)
S = 3/2, p = 5, (j) S = 2, p = 3, (k) S = 2, p = 4, and (l)
S = 2, p = 5. Average values from five independent runs are
shown here. The maximum standard deviation is ∼ 10−3 and
too small to be visible on the graph for all results.

In finite-size numerical calculations for a system undergoing a first-order transition, the specific heat tends to
diverge as the system size L increases near the transition
temperature because the internal energy tends to jump
but does not do so exactly at the transition point. The
temperature dependence of the specific heat is shown in
Fig. 9. One can see that c(T ) actually tends to diverge
near the transition temperature as the system size increases. Tc (L) defined in Eq. (28) represents the temperature at which this divergence tendency is observed.
This quantity behaves as follows with increasing system
size:
Tc (L) =

a
+ Tc (∞).
L2

(30)

Here, a is a constant value and Tc (∞) is the estimated
transition temperature in the thermodynamic limit.
The inverse system size 1/L2 dependence of Tc (L) is
shown in Fig. 10. The solid and dashed lines represent the fits by Eq. (30). It can be seen that Tc (L)

9
(a)

(b)

(a)

1.603(2)

1.6659(1)
1.6869(1)
1.7194(3)

2.2696(1)
2.2690(1)
2.2692(1)

(b)

1.128(5)

1.041(8)

(c)

(d)

1.416(2)

0.695(3)

0.919(2)

(c)

(d)

1.752(3)

1.780(2)

1.532(1)

1.555(1)

1.3986(1)
1.3989(1)
1.4133(1)

1.2500(1)
1.2343(1)
1.2360(1)

1.005(1)
0.990(2)

FIG. 10. Inverse system size dependence of finite-size “transition temperatures” Tc (L) for (a) S = 1/2, (b) S = 1, (c)
S = 3/2, and (d) S = 2. Average values from five independent runs are shown here. The maximum standard deviation is ∼ 10−4 and too small to be visible in the plotted data. The solid and dashed lines represent the fits by
Tc (L) = a/L2 + Tc (∞). Fitting was performed using five
data points in the range of L = 30 to 60.

FIG. 11. Inverse system size dependence of the latent heat
∆Q(L) for (a) S = 1/2, (b) S = 1, (c) S = 3/2, and (d)
S = 2. Average values from five independent runs are shown
here. The maximum standard deviation is ∼ 10−3 and too
small to be visible in the plotted data. The solid and dashed
lines represent the fits by ∆Q(L) = a/L2 + ∆Q(∞). Fitting
was performed using five data points in the range of L = 30
to 60.

follows the form given in Eq. (30) for larger L and the
fitting errors are very small. For S = 1/2, the transition temperatures for p = 3, 4, 5 take almost the same
values:√ Tc (∞) ≃ 2.269. This value is very close to
2/ log( 2 + 1) = 2.269185..., which is the exact transition temperature for p = 2. The fact that the transition temperature for S = 1/2 takes the same value for
all p is consistent with the analytical results obtained
using self-duality [17]. In contrast, for S = 1, the transition temperatures for p = 3, 4, 5 are different and increase with increasing p. Interestingly, for S = 3/2, the
transition temperatures for p = 3 and 4 take almost the
same values: Tc (∞) ≃ 1.398. From the finite-size numerical calculations, it is, however, difficult to determine
whether this close similarity is merely coincidental or if
the transition temperatures are exactly the same for some
theoretical reasons. The case of S = 2 shows no simple
correlation between transition temperatures and p.
Then we discuss the latent heat in the thermodynamic
limit characteristic of first-order phase transitions. We
denote the energies that correspond to the two peaks of
P (E, Tc (L)) as E− (L) and E+ (L). Note that E− (L) <
E+ (L). Using both energies, we define finite size “latent
heat” as

Here, a is a constant and ∆Q(∞) can be considered as
the latent heat in the thermodynamic limit. Figure 11
shows the inverse system size dependence of ∆Q(L). One
can see that ∆Q(L) behaves as Eq. (32) for large L and
the fitting errors are small. The overall trend is that the
latent heat increases with p for each S. This indicates
that the system exhibits a stronger first-order transition
as p increases. It is also consistent with the results of the
order parameter and internal energy.
To confirm that the systems show first-order transitions at the temperatures obtained here, we calculate the
following Binder cumulant:

∆Q(L) := E+ (L) − E− (L).

(31)

Similar to Tc (L), this quantity behaves as follows with
increasing system size:
∆Q(L) =

a
+ ∆Q(∞).
L2

(32)

U (T ) := 1 −

⟨O2 ⟩
3 ⟨O⟩

2.

(33)

It is known that the Binder cumulants for different system sizes intersect at the transition temperature for sufficiently large system sizes [42–44]. We here employed a
Monte Carlo simulation with single-spin flips to perform
the calculations, ensuring consistency in our results obtained by the multicanonical simulations. This method
requires a large number of sweeps to converge and is difficult to carry out for the models for p ≥ 4, whereas the
p = 3 models converge with a relatively small number
of sweeps ∼ 104 . Figure 12 shows U (T ) near the transition temperature for p = 3 and S = 1/2, 1, 3/2, 2. The
Metropolis update [26, 27] is used for S = 1/2 and the
Suwa-Todo method [45] for S ≥ 1. The number of sweeps
is up to 5 × 104 and the number of samples is 105 for all
data. It is evident that U (T ) intersects at the estimated
transition temperature for all S, which is consistent with

10
(a)

(b)

1.6659

2.2692

(d)

(c)

1.3986

1.2500

FIG. 12. Temperature T dependence of the Binder cumulant U (T ) near the transition temperature for p = 3 and (a)
S = 1/2, (b) S = 1, (c) S = 3/2, and (d) S = 2. The
dashed vertical lines represent the estimated transition points
obtained from Eq. (30).

the results obtained by the multicanonical simulations.

IV.

SUMMARY

We have analyzed the spin-S Ising models with p-spin
interactions on the one-dimensional chain and the twodimensional square lattice, varying both S and p up to
S = 2 and p = 5 to explore how these changes affect
the properties of the system. For the one-dimensional
model, we have calculated the free energy and the spinspin correlations by numerically diagonalizing the transfer matrix. It is found that the free energy decreases as p
increases for S ≥ 1, while the free energy is independent
of p for S = 1/2. Additionally, the spin-spin correlations
increase with p and this increase becomes significant in
the low-temperature region. The correlation length ξp
takes the form ξp ≃ Sp × ξp=2 for p ≥ 3 near zero temperature.
For the model on the two-dimensional square lattice,
we have investigated the nature of the phase transition.
By using the multicanonical methods, we have analyzed
basic physical quantities such as the order parameter,
internal energy, and heat capacity. It is found that a
first-order phase transition occurs for p ≥ 3. While it is
well known that S = 1/2 Ising-like models with higherorder interactions exhibit first-order transitions [16, 46–
51], we have shown that this also holds true for S ≥ 1.
Furthermore, analysis of the latent heat shows that increasing p or S leads to a stronger first-order transition,
with a corresponding increase in the latent heat. Regarding the transition temperature, our results suggest that
for S = 1/2, the transition temperature is independent

TABLE I. The transition temperatures Tc (∞) and the latent
heat ∆Q(∞) estimated from the scaling forms in Eqs. (30)
and (32), respectively. For comparison, the values for p = 2
are also shown.
S
p
Tc (∞)
∆Q(∞) Transition order
1/2 2
2.26918... [3]
Second
3
2.2696(1)
0.695(3)
First
4
2.2690(1)
1.041(8)
First
5
2.2692(1)
1.128(5)
First
1
2 1.68–1.71 [32–36]
Second
3
1.6659(1)
0.919(2)
First
4
1.6869(1)
1.416(2)
First
5
1.7194(3)
1.603(2)
First
3/2 2
1.46 [33]
Second
3
1.3986(1)
0.990(2)
First
4
1.3989(1)
1.532(1)
First
5
1.4133(1)
1.752(3)
First
2
2 1.32–1.69 [37–40]
Second
3
1.2500(1)
1.005(1)
First
4
1.2343(1)
1.555(1)
First
5
1.2360(1)
1.780(2)
First

√
of p and is close to Tc = 2/ log( 2 + 1), as previously
predicted using self-duality [17]. However, for S ≥ 1, the
relation between p and the transition temperature is not
simple. When p is fixed and S increases, the transition
temperature tends to decrease, and it is expected to converge to a finite value in the limit of infinite S → ∞. For
S = 3/2, the transition temperatures for p = 3 and 4 are
very close, with Tc ≃ 1.398. Whether this close similarity
is coincidental or has a theoretical background remains
an open question for future studies. We summarize the
transition temperatures and the latent heat obtained in
this paper in Table I, along with the results for p = 2 for
comparison. The results obtained in this paper are expected to deepen our understanding of the properties of
p-body interactions and serve as a foundation for various
future studies, including potential applications.
Finally, let us comment on future works. One interesting point is exploring Ising models with continuous spins,
obtained by S → ∞. While the transition temperature
decreases as the magnitude of spin S increases for fixed
p, the latent heat tends to increase, suggesting that the
first-order transition could become stronger. In addition
to the p-spin interaction Jp considered in this paper, introducing conventional two-body interactions J2 is also
interesting. It is expected that a system with sufficiently
large J2 shows a second-order phase transition, while for
sufficiently small J2 , the p-spin interactions become dominant and the system shows a first-order transition. As
J2 decreases from large values, there could appear a tricritical point, where the phase transition changes from
second order to first order. Analyzing this would also be
an interesting topic for future research.

11
ACKNOWLEDGEMENT

We would like to thank research members of Jij Inc.
for their helpful discussion and conversation.

[1] W. Lenz, Beitrag zum Verständnis der magnetischen Erscheinungen in festen Körpern, Z. Phys. 21, 613 (1920).
[2] E. Ising, Beitrag zur Theorie des Ferromagnetismus, Z.
Phys. 31, 253 (1925).
[3] L. Onsager, Crystal statistics. I. A two-dimensional
model with an order-disorder transition, Phys. Rev. 65,
117 (1944).
[4] Y. Fan, One-dimensional Ising model with k-spin interactions, Eur. J. Phys. 32, 1643 (2011).
[5] D. C. Mattis and R. Galler, Odd-spin-cluster interactions, Phys. Rev. B 27, 2894 (1983).
[6] L. Turban, One-dimensional Ising model with multispin
interactions, J. Phys. A: Math. Theor. 49, 355002 (2016).
[7] C. Fan and F. Y. Wu, General Lattice Model of Phase
Transitions, Phys. Rev. B 2, 723 (1970).
[8] R. J. Baxter, Eight-Vertex Model in Lattice Statistics,
Phys. Rev. Lett. 26, 832 (1971).
[9] F. W. Wu, Ising Model with Four-Spin Interactions,
Phys. Rev. B 4, 2312 (1971).
[10] L. P. Kadanoff and F. J. Wegner, Some Critical Properties of the Eight-Vertex Model, Phys. Rev. B 4, 3989
(1971).
[11] R. J. Baxter and F. Y. Wu, Exact Solution of an Ising
Model with Three-Spin Interactions on a Triangular Lattice, Phys. Rev. Lett. 31, 1294 (1973).
[12] R. J. Baxter and F. Y. Wu, Ising model on a triangular lattice with three-spin interactions. I. The eigenvalue
equation, Aust. J. Phys. 27, 357 (1974).
[13] R. J. Baxter, Ising model on a triangular lattice with
three-spin interactions. II. Free energy and correlation
length, Aust. J. Phys. 27, 369 (1974).
[14] R. B. Potts, Some generalized order-disorder transformations, Math. Proc. Camb. Philos. Soc. 48, 106–109
(1952).
[15] L. Turban, Self-dual anisotropic two-dimensional Ising
models with multispin interactions, J. Physique Lett. 43,
259 (1982).
[16] J. M. Debierre and L. Turban, Two-dimensional Ising
model with multispin interactions, J. Phys. A: Math.
Gen. 16, 3571 (1983).
[17] L. Turban, Self-dual two-dimensional Potts model with
multispin interactions, J. Phys. C: Solid State Phys. 15,
L227 (1982).
[18] A. Lucas, Ising formulations of many NP problems,
Front. Phys. 2 (2014).
[19] M. Blume, Theory of the first-order magnetic phase
change in UO2 , Phys. Rev. 141, 517 (1966).
[20] H. Capel, On the possibility of first-order phase transitions in Ising systems of triplet ions with zero-field splitting, Physica 32, 966 (1966).
[21] B. A. Berg and T. Neuhaus, Multicanonical algorithms
for first order phase transitions, Phys. Lett. B 267, 249
(1991).
[22] B. A. Berg and T. Neuhaus, Multicanonical ensemble: A
new approach to simulate first-order phase transitions,

Phys. Rev. Lett. 68, 9 (1992).
[23] B. A. Berg and T. Celik, New approach to spin-glass
simulations, Phys. Rev. Lett. 69, 2292 (1992).
[24] F. Wang and D. P. Landau, Efficient, Multiple-Range
Random Walk Algorithm to Calculate the Density of
States, Phys. Rev. Lett. 86, 2050 (2001).
[25] F. Wang and D. P. Landau, Determining the density of
states for classical statistical models: A random walk
algorithm to produce a flat histogram, Phys. Rev. E 64,
056101 (2001).
[26] N. Metropolis, A. W. Rosenbluth, M. N. Rosenbluth,
A. H. Teller, and E. Teller, Equation of State Calculations by Fast Computing Machines, J. Chem. Phys. 21,
1087 (1953).
[27] W. K. Hastings, Monte Carlo sampling methods using
Markov chains and their applications, Biometrika 57, 97
(1970).
[28] A. A. Barker, Monte Carlo calculations of the radial distribution functions for a proton-electron plasma, Aust. J.
Phys. 18, 119 (1965).
[29] R. H. Swendsen and J.-S. Wang, Nonuniversal critical
dynamics in Monte Carlo simulations, Phys. Rev. Lett.
58, 86 (1987).
[30] U. Wolff, Collective Monte Carlo Updating for Spin Systems, Phys. Rev. Lett. 62, 361 (1989).
[31] J. Liu, Y. Qi, Z. Y. Meng, and L. Fu, Self-learning Monte
Carlo method, Phys. Rev. B 95, 041101(R) (2017).
[32] P. D. Beale, Finite-size scaling study of the twodimensional Blume-Capel model, Phys. Rev. B 33, 1717
(1986).
[33] J. C. Xavier, F. C. Alcaraz, D. Penã Lara, and J. A. Plascak, Critical behavior of the spin- 23 blume-capel model in
two dimensions, Phys. Rev. B 57, 11575 (1998).
[34] C. J. Silva, A. A. Caparica, and J. A. Plascak, WangLandau Monte Carlo simulation of the Blume-Capel
model, Phys. Rev. E 73, 036702 (2006).
[35] A. Malakis, A. N. Berker, I. A. Hadjiagapiou, N. G. Fytas, and T. Papakonstantinou, Multicritical points and
crossover mediating the strong violation of universality:
Wang-Landau determinations in the random-bond d = 2
Blume-Capel model, Phys. Rev. E 81, 041113 (2010).
[36] P. Butera and M. Pernici, The Blume–Capel model for
spins S=1 and 3/2 in dimensions d=2 and 3, Physica A
507, 22 (2018).
[37] J. Tucker, Ising ferromagnet with biquadratic exchange
interaction and uniaxial anisotropy, J. Magn. Magn.
Mater. 71, 27 (1987).
[38] T. Kaneyoshi, J. Tucker, and M. Jaščur, Differential operator technique for higher spin problems, Physica A 186,
495 (1992).
[39] M. Jurčišin, A. Bobák, and M. Jaščur, Two-spin cluster
theory for the Blume-Capel model with arbitrary spin,
Physica A 224, 684 (1996).
[40] N. Hachem, A. Lafhal, H. Zahir, M. El Bouziani,
M. Madani, and A. Alrajhi, The spin-2 Blume-Capel

12
model by position space renormalization group, Superlattice. Microst. 111, 927 (2017).
[41] M. S. S. Challa, D. P. Landau, and K. Binder, Finitesize effects at temperature-driven first-order transitions,
Phys. Rev. B 34, 1841 (1986).
[42] K. Binder and D. P. Landau, Finite-size scaling at firstorder phase transitions, Phys. Rev. B 30, 1477 (1984).
[43] K. Binder, K. Vollmayr, H.-P. Deutsch, J. D. Reger,
M. Scheucher, and D. P. Landau, MONTE CARLO
METHODS FOR FIRST ORDER PHASE TRANSITIONS: SOME RECENT PROGRESS, Int. J. Mod.
Phys. C 03, 1025 (1992).
[44] C. L. Wang, J. C. Li, M. L. Zhao, M. I. Marqués,
C. Aragó, and J. A. Gonzalo, Monte Carlo Simulation
of First Order Phase Transitions, Ferroelectrics 401, 3
(2010).
[45] H. Suwa and S. Todo, Markov Chain Monte Carlo
Method without Detailed Balance, Phys. Rev. Lett. 105,
120603 (2010).

[46] H. Blöte, A. Compagner, P. Cornelissen, A. Hoogland,
F. Mallezie, and C. Vanderzande, Critical behaviour of
two Ising models with multispin interactions, Physica A
139, 395 (1986).
[47] J. R. Heringa, H. W. J. Blöte, and A. Hoogland, Phase
transitions in self-dual Ising models with multispin interactions and a field, Phys. Rev. Lett. 63, 1546 (1989).
[48] G.-M. Zhang and C.-Z. Yang, Monte Carlo Study of the
Order of the Phase Transition in Ising Systems with Multispin Interactions, Phys. Status Solidi B 175, 459 (1993).
[49] A. Barra, Notes on ferromagnetic p-spin and REM,
Math. Methods Appl. Sci. 32, 783 (2009).
[50] E. Jurčišinová and M. Jurčišin, Phase transitions of the
p-spin model on pure husimi lattices, Phys. Rev. E 88,
012140 (2013).
[51] E. Jurčišinová and M. Jurčišin, The first order phase
transitions in the multisite spin-1/2 model on a pure
husimi lattice, Physica A: Statistical Mechanics and its
Applications 415, 375 (2014).

