Chemical Physics Letters 621 (2015) 102–108

Contents lists available at ScienceDirect

Chemical Physics Letters
journal homepage: www.elsevier.com/locate/cplett

Relationship between coupling constants in Heisenberg exchange
Hamiltonian and Ising model
Sambhu N. Datta ∗ , Shekhar Hansda
Department of Chemistry, Indian Institute of Technology Bombay, Powai, Mumbai 400076, India

a r t i c l e

i n f o

a b s t r a c t

Article history:
Received 3 November 2014
In ﬁnal form 2 January 2015
Available online 7 January 2015

We show that the coupling constant involved in the Heisenberg exchange Hamiltonian is related to the
coupling constant calculated in the Ising model by a simple expression of the form J(Hei) = J(Ising)/N
where N is the average number of equivalent magnetic sites per cell taken for calculation. This relation
is demonstrated by DFT calculations on the crystallographic geometry of MnSb alloy in different magnetic phases, and on the optimized geometries of polymers of meta-xylylene and the silicon substituted
counterparts.
© 2015 Elsevier B.V. All rights reserved.

1. Introduction
It is well-known that the Heisenberg exchange Hamiltonian
serves as the effective spin Hamiltonian for ferromagnetic (FM)
and antiferromagnetic (AFM) solids, though in practice the Hamiltonian in Ising approximation is often used for calculations and
to obtain qualitative theoretical guidance [1–3]. It is desirable to
have a clearly deﬁned relationship between the coupling constants
in Heisenberg Hamiltonian and those calculated from Ising Hamiltonian, and whenever possible, compare these with the coupling
constants that can be estimated from experiment. This question is
addressed here. A relationship is obtained, and it is illustrated by
exemplary calculations on three systems.
2. Theoretical background
The treatment of ferromagnetism in solids in the absence of
an external magnetic ﬁeld is generally based on the Heisenberg
effective spin Hamiltonian,
site axis



H Hei = E0 − 2

j

ε

JεH S j • S
.
j+n

ε

(1)

In the above JεH is the exchange coupling constant in Heisenberg
model between the neighbouring magnetic sites joined by the unit
vector 
nε along the crystal axis ε, and Sj is the operator for the
spin angular momentum at site j. The Ising model, often applied to

∗ Corresponding author.
E-mail address: sndatta@chem.iitb.ac.in (S.N. Datta).
http://dx.doi.org/10.1016/j.cplett.2015.01.001
0009-2614/© 2015 Elsevier B.V. All rights reserved.

metallic or alloy systems [4], relies on a special case of Heisenberg
spin exchange in Eq. (1), with all spins considered as directed along
a speciﬁc (z) axis:
Ising

H Ising = E0

axis
site 


−2

j

JεI (Sj )z (Sj+nε )z .

(2)

ε

Here JεI is the magnetic exchange coupling constant in Ising model
between neighbouring sites along crystal axis ε, and (Sj )z is the
operator for the z-component of spin angular momentum. The
coupling constant JεI involves the interaction only between the zcomponents of spin, and therefore, differs from JεH that is used
in the general exchange Hamiltonian with Si ·Sj term. Ising model
has often been used for periodic systems to investigate qualitative
trends in properties [4].
2.1. Coupling constants
Let us write the number of sites as Nsite = Nuc Nmag where Nuc is
the number of unit cells per unit volume and Nmag is the number of
‘equivalent’ magnetic sites per unit cell. The ‘equivalent’ magnetic
sites are sites of same type of atoms in same chemical environment
and carrying the same spin, but they may appear at different relative topological positions in the repeating unit as illustrated by
Figure 1.
The total spin operators are given by
S total =

site

j

Sj,

S tot,z =

site

j

S jz .

(3)

S.N. Datta, S. Hansda / Chemical Physics Letters 621 (2015) 102–108

103

Figure 1. (a) Elementary unit cell for MnSb (Nmag = 2); (b) the supercell for MnSb (Nmag = 4); (c) unit cell for silicon substituted 1-D meta-xylylene polymer (Nmag = 2) and (d)
unit cell for 1-D meta-xylylene polymer (Nmag = 2). Atoms are coloured as follows: Mn (dark blue), Sb (light green), C (red), Si (purple), and H (green).

The spin state vectors |{mi } where mi varies over all possible eigenvalues of (Si )z for every site i form a complete basis set for the
2
common eigenstates of Stotal
and Stot,z . We note

S tot,z |{mi } = M|{mi },

M=

site


nearest neighbours along each direction ε, we get from the Ising
Hamiltonian
Ising

EFM = E0

− Nsite S 2

axis


zε JεI ,

ε

mj

(4)

j

where ε is a running index and the AFM spin arrangement is present
along the speciﬁc axis ε .
The energy per cell is written as Ec = E/Nuc such that

and

2
{mi }|Stotal
|{mi } = Smax (S + 1) + M 2 −

(6)

ε
= EFM + 2Nsite S 2 zε JεI  .
EAFM

site


m2j ,

Smax = Nsite S.

(5)

j

For the FM state, mj = S for every site j so that M = Smax = Nsite S,
2
 = Smax (Smax + 1). This also yields the spin per cell
and Stotal
Smax /Nuc = Nmag S so that S2 cell = Nmag S(Nmag S + 1). For any AFM conﬁguration, however, M = 0 that can correspond to any Stotal (Stotal = 0,
2S, 4S, . . ., Smax ). For any particular AFM arrangement with mj
alternatively varying as S and −S along a particular crystal axis
ε while maintaining FM arrangement along all other crystal axes,

2
m2 = Smax S so that Stotal
 = Smax , and similarly S2 cell = Nmag S.
j j
These results are exact.
The total (space-spin) electronic Hamiltonian Hel can be used
to calculate the energy of any state with a particular spin conﬁguration under Born–Oppenheimer approximation. This energy can
be equated to the energy of a spin Hamiltonian. As there are zε

Ising

Ec,FM = Ec,0 − Nmag S 2

axis


zε JεI ,

ε
Ec,AFM = Ec,FM + 2Nmag S 2 zε JεI  .

(7)

ε

This gives
2zε JεI =

ε
− Ec,FM
Ec,AFM

Nmag S 2

(8)

for each crystal axis ε.
There arises a problem in the calculation of the Heisenberg coupling constant JεH . The spin state M = Smax is necessarily a pure spin
state representing Stotal = Smax , that is, the FM ground state conﬁguration is indeed the exact ground state conﬁguration of the FM solid.
As far as an explicit quantum mechanical calculation is concerned,
the calculated solution for M = 0 is in general a mixture of states with
different values of Stotal as observed earlier after Eq. (5). Anderson
showed that the true AFM ground state in any solid is a harmonic

104

S.N. Datta, S. Hansda / Chemical Physics Letters 621 (2015) 102–108

oscillator state involving different sublattices. Spins of the two
sublattices are in opposite directions. One cannot deﬁne the spin
direction of any sublattice on an average basis [5]. As a speciﬁc spin
arrangement cannot represent the AFM ground state, the Heisenberg coupling constant cannot be directly calculated from it. Klein
et al. have discussed the limitations of the spin wave approach [6].
2.2. Broken symmetry
Any unrestricted self-consistent-ﬁeld (SCF) calculation
(Hartree–Fock or Kohn–Sham) on a speciﬁc AFM conﬁguration in Ising model is in principle comparable to the ‘broken
symmetry’ calculations in quantum chemistry on the less-thanhighest-spin states of a polyradical. Two issues are involved here.
First, there is selective localization of down spin on speciﬁc sites
2
[7]. The resulting solution is an eigenstate of Sz , but not of Stotal
.
Second, the problem is more intrinsic. For example, one needs a
two-determinant conﬁguration to describe an open-shell singlet
diradical. The unrestricted procedure gives a solution for Sz = 0 with
both spatial and spin symmetries broken and S2  ≈ 1. To calculate
the singlet–triplet energy gap for a diradical, the DFT broken
symmetry (BS) methodology was developed by Noodleman [8,9].
The Heisenberg spin Hamiltonian for a diradical
H = −2J H S1 · S2

(9)
2JH .

gives a singlet–triplet energy difference of
For an intramolecular ferromagnetic interaction, JH > 0, and for an antiferromagnetic coupling, JH < 0. Noodleman derived the relation [8,9]
JN =

EBS − ET

(10)

2
1 + Sab

where Sab is the overlap integral between the two magnetically
active orbitals a and b, and EBS and ET are the energies of the broken symmetry state and the triplet state, respectively. The coupling
constant JN gives a fair estimate of JH in the two-electron-in-twoorbital model when Sab is small. Real molecules, however, deviate
from the two-electron-two-orbital model, and for them the spin
polarization treatment led to two different formulae valid in the
limits of weak [10,11] and strong [12,13] overlap. For a general system, however, a single expression was formulated by Yamaguchi
et al. [14–16],
JY =

2 S2
Nmag

.

(12)

As JY is an estimate of the Heisenberg coupling constant, the latter
is related to the normally calculated Ising model coupling constant
in (8) by
JεH =

JεI
.
Nmag

zJ̄

=

2S(S + 1)
3

(14)

that equals 0.5 for S = 1/2. This expression is often used by experimentalists. Here z is the total number of nearest neighbours, and J̄
is the average of coupling constants of the Heisenberg Hamiltonian.
Also, the EPR g factor (spectroscopic splitting factor) is taken to be 2.
Somewhat better statistical treatments by Rushbrooke and Wood
give the ratio 0.28 for simple cubic lattice and a slightly larger value
for fcc and bcc lattices [20]. If we retain the value 0.28 for monoclinic
cells, we get
J̄ =

5.36kB TC
.
2zS(S + 1)

(15)

Replacing gS (=2S) by nB , the number of ferromagnetic magnons
per site, the average coupling constant can be estimated from the
ferromagnetic transition temperature by
J̄est =

10.72kB TC
.
znB (nB + 1)

(16)

This expression gives a standpoint for comparing the calculated
numbers with the observed transition temperature and saturation
magnetic moment that provides nB .

(11)

where EBS and EHS are energies, and S2 BS and S2 HS are the
expectation values of the square of total spin angular momentum
operator, for broken-symmetry (BS) and high-spin (HS) solutions,
respectively. The JY is an estimate of JH . At each limit of Sab , the
Yamaguchi expression reduces to the corresponding limiting form.
the
S2 
values
per
cell,
that
is,
Considering
2
S FM = Nmag S(Nmag S + 1) and S2 AFM = Nmag S, one obtains
ε
− Ec,FM
Ec,AFM

kB TC

3. Test cases

(EBS − EHS )
S 2 HS − S 2 BS

2zε JεY =

limitations of computational resources, serious quantum mechanical calculations on the magnetic properties of periodic systems
have been done within the last two decades. For instance, Dovesi
et al. reported UHF calculations on KMF3 (M = Mn, Fe, Co and Ni)
in 1997 [17]. Second, almost all reported calculations have been
made on the ‘single site model’, that is, the repeating units have
been selected such that Nmag = 1. A relationship between the coupling constants was not explicitly sought. Towler et al. calculated
the Ising exchange parameters for MnO and NiO using single site
model in 1994 and obtained the AFM–FM energy difference that led
to a good estimate of Néel temperature [18]. Jacobson et al. directly
calculated the Heisenberg coupling constants for the same systems
in 2013 by considering a progressively large cell in real space, and
found good agreement with a variety of experimental results [19].
Experimental results such as the ferromagnetic transition temperature (TC ) and saturation magnetization can be correlated with
the Heisenberg coupling constant. The molecular ﬁeld theory gives
the ratio

(13)

It equals the usually calculated coupling constant in Ising model
only when Nmag = 1.
Though the two models are about 90 years old, relationship (13)
remained largely unnoticed because of two reasons. First, due to

There have been excellent discussions on the magnetic properties of inorganic solids such as KMF3 systems (with M = Mn, Fe,
Co, and Ni) [17], MnO and NiO [18,19]. The studies in Refs. [17,18]
involved Nmag = 1, while in Ref. [19] the convergence of the Heisenberg exchange parameters were explicitly studied for different
cut-offs in real space.
In this work we investigate three systems, all having two equivalent magnetic sites per repeating unit. The ﬁrst one is MnSb, a
purely inorganic solid [Figure 1(a) and (b)]. The second one is Sisubstituted poly-meta-xylylene with silicon atoms as radical sites
[Figure 1(c)]. The third is a purely organic polymer of meta-xylylene
[Figure 1(d)].
3.1. Alloy MnSb
The alloy MnSb has NiAs type structure (space group P63 /mmc)
and hcp lattice with a = 4.285 Å and c = 6.113 Å [21]. For MnSb, nB
is known (nB = 3.5) [22]. There are in average six Mn atoms and six
Sb atoms per unit cell. For computational purposes one can utilize
the elementary unit cell that is shown in Figure 2. The elementary unit cell has in average two MnSb pairs. Three phases, namely,
ferromagnetic (FM), antiferromagnetic along z-axis (AFM1) and

S.N. Datta, S. Hansda / Chemical Physics Letters 621 (2015) 102–108

105

Figure 2. Elementary unit cell of hexagonal symmetry, showing different magnetic phases FM and AFM1, and the supercell showing AFM2: blue circles denote spin up Mn,
red circles are for spin down Mn, and green circles stand for Sb. Each elementary cell contains in average 2 Mn atoms and 2 Sb atoms, and the corresponding supercell
contains 4 atoms of each type. This supercell is generated using the expansion matrix 200/010/001.

antiferromagnetic in xy plane (AFM2) are illustrated in the same
ﬁgure.
For calculations on periodic systems, the energy of FM and AFM1
phases can be obtained by taking the elementary unit cell illustrated in Figure 2 as the repeating unit. However, the energy of
the AFM2 phase has to be determined by considering the supercell
containing four Mn atoms as the repeating unit, and the energies
of FM and AFM1 phases can be recalculated for this supercell. The
supercell energy differences are to be divided by 2 to obtain the
energy differences per elementary unit cell.
From the Ising Hamiltonian in Eq. (2) we get the following values
for total energy per elementary cell

Ising



I
Ec,FM = Ec,0 − Nmag Sz2 zz JzI + zxy Jxy
Ising





I
Ec,AFM1 = Ec,0 − Nmag Sz2 −zz JzI + zxy Jxy
Ising



Ec,AFM2 = Ec,0 − Nmag Sz2 zz JzI −

zxy I
J
3 xy



nearest-neighbour Ising coupling constants. One obtains the
relations
(Ec,AFM1 − Ec,FM )
2zz JzI =
,
(18)
Nmag Sz2
(Ec,AFM2 − Ec,FM )
4
I
zxy Jxy
=
.
3
Nmag Sz2

For MnSb in FM, AFM1 and AFM2 phases, S = |Sz | = 2 for each
Mn atom. When we take the same periodicity into account, that
is, explicitly consider the difference in the number of nearestneighbour antiferromagnetic interactions in the two involved
phases, (number of antiferromagnetic interactions in AFM1 or
AFM2 phase plus number of ferromagnetic interactions in FM
phase), we must write
2zz JzY =

(17)



(Ec,AFM1 − Ec,FM )

4
Y
zxy Jxy
=
3

,
2 S2
Nmag
z
(Ec,AFM2 − Ec,FM )
2 S2
Nmag
z

(20)
.

Furthermore,
J̄Ising =

where Nmag = 2 for the elementary unit cell, and zz and zxy are
the numbers of nearest neighbour atoms along z-axis and in the
xy plane, respectively, for each magnetic site. For hcp lattice,
I are the corresponding
zz = 2 and zxy = 6. Furthermore, JzI and Jxy

(19)

J̄Hei

1 I
I
),
(J + 3Jxy
4 z

J̄Ising
= J̄ Y =
.
2

These are the working equations for the system under study.

(21)

106

S.N. Datta, S. Hansda / Chemical Physics Letters 621 (2015) 102–108

Table 1
Single point energies calculated for FM and AFM1 phases of the elementary unit cell from the crystallographic geometry of the MnSb alloy. All energy values are in atomic
units.

MnSb
B3LYP
B3PW
PBE0

Ec,FM (Sz per MnX)

Ec,AFM1 (Sz per MnX)

Ec,(AFM1−FM)

JzI (cm−1 ) Eq. (15)

−218.80951 (2.0070)
−219.10288 (2.0101)
−218.94131 (2.0146)

−218.79621 (0.0017)
−219.08845 (0.0015)
−218.92396 (0.0009)

0.01331
0.01442
0.01734

91.3
98.9
118.9

Table 2
Single point energies calculated for FM, AFM1 and AFM2 phases of the supercell from the crystallographic geometry of alloy MnSb. All energy values are in atomic units.
Phase

E (Sz per MnX)

E(AFM1−FM)

E(AFM2−FM)

JzI (cm−1 )

I
Jxy
(cm−1 )

J̄Ising (cm−1 )

B3LYP

FM
AFM1
AFM2

−437.61893 (2.0075)
−437.59177 (−0.0083)
−437.59562 (0.0000)

0.02716

0.02331

93.1

39.9

53.2

B3PW

FM
AFM1
AFM2

−438.20478 (2.0107)
−438.17552 (−0.0017)
−438.17955 (0.0000)

0.02926

0.02523

100.4

43.3

57.6

PBE0

FM
AFM1
AFM2

−437.88252 (2.0143)
−437.84788 (−0.0009)
−437.85389 (0.0000)

0.03464

0.02863

118.8

49.1

66.5

The ab-intio solid state computational code CRYSTAL09 [23,24]
is used for energy calculations by DFT methodology. Experimental lattice constants from Ref. [21] are adopted as input. Hybrid
functionals are known to provide better results for insulators and
semiconductors [25–28]. A possible problem with applicability
exists only for conductive materials. This has been discussed by
Franchini [29]. The ‘time-tested’ B3LYP functional generates relative energies close to the experimental values and good coupling
constants [30–33], and B3PW reproduces J near experimental value
[33,34]. PBE0 is known to produce band structure data comparable
to experiments [35].
We employ the pseudopotential basis sets for the atomic valence
states, namely (i) 3s, 3p, 4s and 3d orbitals of Mn, and (ii) 5s and
5p orbitals of Sb: Mn HAYWSC-411d311 heifets 2005 [33], and
Sb DURAND-21d1G causa 1991 [36]. The chosen Mn basis set with
B3LYP functional has produced good estimates of structural parameters and magnetic exchange coupling constants for LaMnO3 [33]
and ScMnO3 [37]. The basis set selected for Sb generally leads to
structural parameters close to the experimental ones [36]. Use of
the pseudopotentials allows the size of basis set to be reduced and
thereby save computational resources.
Total energy, Sz , and the charge and spin populations are determined in the following way. Single point calculations are done on
the elementary unit cells and the corresponding supercells. SPINLOCK keyword is used to maintain the difference between the
number of electrons with spins up and down to get the desired spin
states (such as Sz = 0, 1, . . ., 8). However, the spin state with Sz = 4
for the elementary unit cell and that with Sz = 8 for the supercell
come out to be most stable. To get the second antiferromagnetic
phase (AFM2) and the in-plane coupling constant, an expansion
matrix of 100/020/001 is used to generate the supercell. The spin
state 8 is employed for the ferromagnetic phase of this supercell.
Shrinking factor of 12 is used to obtain eigenvectors and eigenvalues. Tolerance parameters (TOLINTEG) have ﬁve integers T1 T2
T3 T4 T5 with default values 6 6 6 6 12 in CRYSTAL09. To get
greater accuracy in the coulomb and exchange integrals, tolerance
parameters 7 7 7 7 15 are used as recommended in Refs. [38,39].
Convergence is achieved with the help of ANDERSON procedure
[40]. The Fock-KS matrix mixing (FMIXING) (for two successive
cycles) is taken as 50%. For all the calculations, the starting electronic conﬁgurations have been taken as 4s2 3d5 for Mn and 5s2 5p3
for Sb.

Table 3
Average magnetic exchange coupling constant (in cm−1 ) calculated from the experimental transition temperature and nB of MnSb solid.
Rushbrooke–Wood coupling constant

B3LYP
B3PW
PBE0

J̄Ising a

J̄Hei b

J̄est c

53.2
57.6
66.5

26.6
28.8
33.2

28.4

a

Ising model calculation, Table 1.
Corrected for Heisenberg exchange by using Nmag = 2 in Eq. (13).
c
Heisenberg model, mean ﬁeld theory and statistical approximation, Eq. (16).

b

3.2. Polyradicals
The calculations on meta-xylylene polyradical chains and the
corresponding silicon substituted species are done using code
Gaussian 09 [41]. Optimization of molecular geometries and the
subsequent single point calculations on silicon substituted species
are performed using 6-311G(d,p) and 6-311++G(d,p) basis sets,
respectively, with B3LYP and B3LYP-D functionals. For metaxylylene polyradical chains the molecular geometry optimization
and subsequent single point calculations are done using 6-31G(d,p)
and 6-311G(d,p) basis sets, respectively, using B3LYP and M06-2X
functionals.
CRYSTAL09 code is used for calculations on the inﬁnitely long
one-dimensional polymers. The geometry of the unit cell is fully
optimized in both FM and AFM states while using B3LYP and B3LYPD functionals with TZVP basis sets for Si, C and H atoms [42]. The
M06-2X functional is not available in CRYSTAL09. For poly-metaxylylene and its silicon substituted form, we have used (i) SHRINK
factors 16 16 and 32 32, respectively, (ii) the SPINLOCK keyword,
and (iii) tolerance parameters (TOLINTEG) 7 7 7 7 14. Convergence
is achieved using LEVSHIFT option 1 0 along with 30% FMIXING.
4. Results and discussion
Single point calculations are done on the experimentally
reported crystal geometries. The input ﬁles and selected outputs
are included in Supporting Information. The energy differences and
calculated Ising model coupling constants are given in Table 1 (elementary unit cell) and Table 2 (supercell). The Ising model coupling

S.N. Datta, S. Hansda / Chemical Physics Letters 621 (2015) 102–108

107

Table 4
Calculated magnetic exchange coupling constants in cm−1 : The number of phenylene rings in the polymer is p. The J∞ is estimated by assuming an exponential behaviour.
Periodic calculations are done by using B3LYP and B3LYP-D functionals with TZVP basis set.
Si substituted poly-meta-xylylene

Poly-meta-xylylene

p

B3LYP/6-311++G(d,p)

B3LYP-D/6-311++G(d,p)

p

B3LYP/6-311G(d,p)

M06-2X/6-311G(d,p)

1
2
3
4
∞

243.0
178.4
166.5
122.1
76.7

243.0
178.4
169.7
122.1
85.6

2
3
4
∞

1682
572.8
464.7
453.0

1542
521.3
353.3
320.2

Periodic calculation

B3LYP/TZVP

B3LYP-D/TZVP

Periodic calculationa

B3LYP/TZVP

I

187.1
93.6

197.0
98.5

JI
JH

1077
538.5

J
JH

Data have been taken from Ref. [45].
a
M06-2X is not included in CRYSTAL09 code.

Figure 3. Exponential ﬁtting of decreasing J values with increase in chain length for (a) silicon substituted poly-meta-xylylene (rmsd 9.23 for B3LYP and 10.49 B3LYP-D) and
(b) poly-meta-xylylene (rmsd 45.5 for B3LYP and 0.16 M06-2X). The J value reaches a limiting value J∞ that compares with JH . The periodic calculation gives JI and relation
(13) using Nmag = 2 leads to JH .

constant along the c-axis (z-axis) that is obtained from the supercell calculation is almost equal to that from the calculation on the
I is obtained
elementary unit cell. The in-plane coupling constant Jxy
from Eq. (19). It is also positive, conﬁrming that MnSb is most stable
in the FM phase. The average J̄Ising is obtained from Eq. (21).
As the elementary unit cell in Figure 1 resembles the combination of two monoclinic cells, each having one MnSb pair in average,
we adopt the Rushbrooke–Wood expression (15) for this alloy. The
ferromagnetic transition temperature TC is 587 K for MnSb [43] so
that J̄est = 28.4 cm−1 in the Heisenberg model. In Table 3, coupling
constants from crystal geometries are compared with the coupling constant estimated from nB and TC . The calculated Heisenberg
coupling constants are in striking agreement with the estimated
value from Eq. (15), and vindicate the relationship between J̄Ising
and J̄Hei in Eq. (21).
We have also optimized the geometry of the elementary unit
cell and the supercell. The detailed results are not included in this
report and will be published elsewhere.
In meta-xylylene polyradicals and the silicon substituted forms,
the high-spin state is always the ground state. A decreasing trend in
J values with length is observed in both cases. This trend is shown in
Table 4. Matsuda et al. have shown that the decay of J in phenylene
chains is generally exponential in form [44]. An exponential decay
is illustrated in Figure 3 where a limiting value (J∞ ) is found from
the calculated JY values. We get J∞ (in cm−1 ) = 76.7 (B3LYP), 85.6
(B3LYP-D) for the silicon substituted polymer, and 453.0 (B3LYP),
320.2 (M06-2X) for the unsubstituted meta-xylylene polymer.
From periodic calculations we obtain JI (in cm−1 ) = 187.1
(B3LYP), 197.0 (B3LYP-D) for the silicon polymer, and 1077 (B3LYP),
1096 (B3LYP-D) for the unsubstituted meta-xylylene polymer.
Using Eq. (13), we get JH (in cm−1 ) = 93.5 (B3LYP), 98.5 (B3LYP-D)
for the silicon polymer, and 538.5 (B3LYP), 548 (B3LYP-D) for the

unsubstituted meta-xylylene polymer. Thus the limiting values (J∞ )
estimated from the Heisenberg coupling constants in Yamaguchi
expression are more or less equal to the JH values and not the JI
ones. The JH is exactly half of the JI that is directly obtained from
the results of periodic calculations. A somewhat negative deviation of J∞ from JH is evident. With increasing number of phenylene
rings p, the geometry of the polyradical progressively deviates from
the periodicity that is obtained by repeating the dimer unit. The
detailed results will be published elsewhere [45].
Because of the difference in composition, B3PW is expected to
yield the best J value, followed by B3LYP, (the former functional
containing an improved correlation part), and then the adjustableparameter-free PBE0. This has been precisely observed in our
calculation of Heisenberg coupling constant for MnSb. B3LYP is considered as time-tested for thermochemical calculations. For organic
molecules, M06-2X has a greater contribution from HF exchange,
and generally produces a better (and smaller) coupling constant
than B3LYP does. For polyradicals, the effect of the dispersive forces
can be quite signiﬁcant, as found from the periodic calculations on
the silicon-substituted polymer.
5. Conclusions
This study gives an insight into the relationship between the
coupling constant of Heisenberg exchange and that normally
calculated from Ising approximation. We ﬁnd relation (13) and
demonstrate it by sample calculations on MnSb. The two sets of
coupling constants are equal in the ‘single site model.’ Thus the
choice of the repeating unit becomes critical. This is also valid for
polyradicals. When two successive radical monomers are twisted
such that they are alternately periodic, the dimer is the repeating
unit and a sensible result evolves only after dividing Ising model

108

S.N. Datta, S. Hansda / Chemical Physics Letters 621 (2015) 102–108

coupling constant by 2. These and related issues will be discussed
in our future work.
Acknowledgments
We are grateful to Department of Science and Technology for
ﬁnancial support, and I.I.T. Bombay computer centre for their
facilities. S.H. acknowledges University Grants Commission for a
fellowship. We acknowledge A. K. Pal for supplying data on unsubstituted polyradicals.
Appendix A. Supplementary data
Supplementary data associated with this article can be found, in
the online version, at doi:10.1016/j.cplett.2015.01.001.
References
[1] Z.G. Soos, J. Chem. Phys. 43 (1965) 1121.
[2] J.F. Nagle, J.C. Bonner, J. Chem. Phys. 54 (1971) 729.
[3] M.E. Costas, Z. Wang, W.M. Gelbart, J. Chem. Phys. 96 (1992) 2228.
[4] O. Kahn, Molecular Magnetism, VCH Publishers, New York, 1993.
[5] P.W. Anderson, Phys. Rev. 86 (1952) 694.
[6] D.J. Klein, S.A. Alexander, W.A. Seitz, T.G. Schmalz, G.E. Hite, Theor. Chim. Acta
69 (1986) 393.
[7] F. Neese, Wiley Interdiscip. Rev. Comput. Mol. Sci. 2 (2012) 73.
[8] L. Noodleman, J. Chem. Phys. 74 (1981) 5737.
[9] L. Noodleman, E.J. Baerends, J. Am. Chem. Soc. 106 (1984) 2316.
[10] A.P. Ginsberg, J. Am. Chem. Soc. 102 (1980) 111.
[11] L. Noodleman, E.R. Davidson, Chem. Phys. 109 (1986) 131.
[12] A. Bencini, F. Totti, C.A. Daul, K. Doclo, P. Fantucci, V. Barone, Inorg. Chem. 36
(1997) 5022.
[13] E. Ruiz, J. Cano, S. Alvarez, P. Alemany, J. Comput. Chem. 20 (1999) 1391.
[14] K. Yamaguchi, H. Fukui, T. Fueno, Chem. Lett. 15 (1986) 625.
[15] K. Yamaguchi, Y. Takahara, T. Fueno, K. Nasu, Jpn. J. Appl. Phys. 26 (1987) L1362.

[16] K. Yamaguchi, F. Jensen, A. Dorigo, K.N. Houk, Chem. Phys. Lett. 149 (1988) 537.
[17] R. Dovesi, F. Freyria Fava, C. Roetti, V.R. Saunders, Faraday Discuss. 106 (1997)
173.
[18] M.D. Towler, N.L. Allan, N.M. Harrison, V.R. Saunders, W.C. Mackrodt, E. Aprà,
Phys. Rev. B 50 (1994) 5041.
[19] A. Jacobsson, B. Sanyal, M. Ležaić, S. Blügel, Phys. Rev. B 88 (2013) 134427.
[20] G.S. Rushbrooke, P.J. Wood, Mol. Phys. 1 (1958) 257.
[21] K. Elankumaran, G. Markandeyulu, K.V.S. Rama Rao, J. Phys. Soc. Jpn. 61 (1992)
1979.
[22] T. Okita, Y. Makino, J. Phys. Soc. Jpn. 25 (1968) 120.
[23] R. Dovesi, R. Orlando, B. Civalleri, V.R. Saunders, C.M. Zicovich-Wilson, Z. Kristallogr. 220 (2005) 571.
[24] R. Dovesi, et al., CRYSTAL09 User’s Manual, University of Torino, Torino, 2009.
[25] M. Causà, R. Dovesi, C. Pisani, R. Colle, A. Fortunelli, Phys. Rev. B 36 (1987) 891.
[26] M.D. Towler, A. Zupan, M. Causà, Comput. Phys. Commun. 98 (1996) 181.
[27] S. Piskunov, E. Heifets, R.I. Eglitis, G. Borstel, Comput. Mater. Sci. 29 (2004) 165.
[28] F. Corà, Mol. Phys. 103 (2005) 2483.
[29] C. Franchini, J. Phys. Condens. Matter 26 (2014) 253202.
[30] J. Muscat, A. Wander, N.M. Harrison, Chem. Phys. Lett. 342 (2001) 397.
[31] X. Feng, Phys. Rev. B 69 (2004) 155107.
[32] S. Tomić, B. Montanari, N.M. Harrison, Phys. E: Low-Dimens. Syst. Nanostruct.
40 (2008) 2125.
[33] R.A. Evarestov, E.A. Kotomin, Y.A. Mastrikov, D. Gryaznov, E. Heifets, J. Maier,
Phys. Rev. B 72 (2005) 214411.
[34] E. Heifets, E. Kotomin, V.A. Trepakov, J. Phys. Condens. Matter 18 (2006) 4845.
[35] J. Graciani, et al., J. Chem. Theory Comput. 7 (2010) 56.
[36] M. Causà, R. Dovesi, C. Roetti, Phys. Rev. B 43 (1991) 11937.
[37] T. Bredow, K. Jug, R.A. Evarestov, Phys. Status Sol. (B) 243 (2006) R10.
[38] C. Pisani, R. Dovesi, C. Roetti, Hartree-Fock Ab Initio Treatment of Crystalline
Systems, Springer, Berlin, 1988.
[39] V.R. Saunders, C. Freyria-Fava, R. Dovesi, L. Salasco, C. Roetti, Mol. Phys. 77
(1992) 629.
[40] D.G. Anderson, J. Assoc. Comput. Mach. 12 (1964) 547.
[41] M.J. Frisch, et al., Gaussian 09 Revision A.02, Gaussian Inc., Wallingford, CT,
2009.
[42] M.F. Peintinger, D.V. Oliveira, T. Bredow, J. Comput. Chem. 34 (2013) 451.
[43] C. Chen, et al., J. Appl. Phys. 89 (2001) 8035.
[44] S. Nishizawa, J. Hasegawa, K. Matsuda, J. Phys. Chem. C 117 (2013) 26280.
[45] S. Hansda, A.K. Pal, S.N. Datta, J. Phys. Chem. C (2015) (Manuscript submitted
for publication).

