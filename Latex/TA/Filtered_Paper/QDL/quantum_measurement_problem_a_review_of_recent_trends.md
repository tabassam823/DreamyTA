Philosophical Magazine

ISSN: 1478-6435 (Print) 1478-6443 (Online) Journal homepage: www.tandfonline.com/journals/tphm20

The quantum measurement problem: a review of
recent trends
Anderson A. Tomaz, Rafael S. Mattos & Mario Barbatti
To cite this article: Anderson A. Tomaz, Rafael S. Mattos & Mario Barbatti (26 Dec 2025): The
quantum measurement problem: a review of recent trends, Philosophical Magazine, DOI:
10.1080/14786435.2025.2601922
To link to this article: https://doi.org/10.1080/14786435.2025.2601922

Published online: 26 Dec 2025.

Submit your article to this journal

Article views: 2020

View related articles

View Crossmark data

Citing articles: 4 View citing articles

Full Terms & Conditions of access and use can be found at
https://www.tandfonline.com/action/journalInformation?journalCode=tphm20

PHILOSOPHICAL MAGAZINE
https://doi.org/10.1080/14786435.2025.2601922

The quantum measurement problem: a review of recent
trends
Anderson A. Tomaza, Rafael S. Mattosa and Mario Barbattia,b
a

Aix Marseille University, CNRS, ICR, Marseille, France; bInstitut Universitaire de France, Paris, France
ABSTRACT

ARTICLE HISTORY

Left on its own, a quantum state evolves deterministically under the
Schrödinger
equation,
forming
superpositions.
Upon
measurement, however, a stochastic process governed by the
Born rule collapses it to a single outcome. This dual evolution of
quantum states – the core of the Measurement Problem – has
puzzled physicists and philosophers for nearly a century. Yet,
amid the cacophony of competing interpretations, the problem
today is not as impenetrable as it once seemed. This paper
reviews the current status of the Measurement Problem,
distinguishing between what is well understood and what
remains unresolved. We examine key theoretical approaches,
including decoherence, many-worlds interpretation, objective
collapse theories, hidden-variable theories, dualistic approaches,
deterministic models, and epistemic interpretations. To make
these discussions accessible to a broader audience, we also
reference curated online resources that provide high-quality
introductions to central concepts.

Received 8 August 2025
Accepted 1 December 2025
KEYWORDS

Decoherence; measurement
problem; quantum state
collapse; interpretations of
quantum mechanics

1. Introduction
Quantum mechanics, as we learn in college, posits that an isolated system evolves unita­
rily and deterministically following the Schrödinger equation. When we measure the
system, the Born rule determines the output probabilities. The quantum state collapses
in a non-unitary, stochastic way, so the same outcome is obtained if the measurement
is repeated. Despite its awkward double rule of evolution, this seemingly simple frame­
work enabled comprehension of nature and technological advances to a level that our
species has never seen before.
Nevertheless, let us ask what ‘measure the system’ means. We will not find an answer
in the standard formulation of quantum mechanics. This innocent question unravels a
disturbing thread of conceptual problems, which are surprisingly difficult to address
experimentally and may have dramatic philosophical consequences for our conception
of the world.
The Measurement Problem has been haunting physicists and philosophers of science
for almost as long as the century since quantum mechanics was proposed. We can take as
CONTACT Anderson A. Tomaz
anderson.alves-tomaz@univ-amu.fr; Mario Barbatti
mario.barbatti@univ-amu.fr
Aix Marseille University, CNRS, ICR, Av. Esc. Normandie Niemen, Marseille 13397, Cedex 20, France
© 2025 Informa UK Limited, trading as Taylor & Francis Group

2

A. A. TOMAZ ET AL.

an anecdotal example the World Science Festival held in the first semester of 2024, a
science popularization event hosted by Brian Greene. Greene asked three quantum
mechanics specialists about the Measurement Problem and got three entirely distinct
answers. The entry Interpretations of Quantum Mechanics in Wikipedia contains thir­
teen distinct classes of theories and interpretations, and it does not even account for
some recent proposals.
The cacophony of proposed solutions to the Measurement Problem – including voices
from parts of the physics community that question whether the problem even exists – is
disturbing. It hurts our conception of science as delivering a consistent description of
reality. Why, after a century of quantum mechanics, do we still have no consensus on
its most fundamental process? What do we truly understand about the Measurement
Problem?
Any newcomer trying to get an answer to these questions faces a formidable challenge:
the Measurement Problem research is spread throughout countless isolated sub-commu­
nities. These groups do not talk to each other, making it exceptionally difficult to build an
overview of what’s going on. The large number of single-author papers doesn’t help
either. These papers raise hypotheses and propose theories and tests. However, most
don’t resonate within a mature community and only add to the cacophony.
As newcomers to the field ourselves – we just published our first contribution recently
[1] – we felt firsthand all these issues. We tackled this challenge with extensive reading,
discussion, and consultation with specialists on specific topics. We explored all corners of
the field rather than focussing on a single subfield. This review arose naturally. We aim to
deliver a broad overview of the several competing research lines. We don’t aim for a com­
prehensive survey (which would not be possible within the reasonable limits of a paper)
but rather to illuminate the central questions currently being discussed, allowing curious
non-specialists to start exploring the literature on their own. In doing so, we hope to
show that the Measurement Problem is not as bleak as it seems, although there is still
much to be uncovered.
Given the Measurement Problem’s central role, it is unsurprising that several other
reviews have been recently published to explore its unresolved aspects from different per­
spectives. Hance and Hossenfelder [2] critically assess whether the problem is fundamen­
tal or an artefact of our theoretical framework. In a synthetic review, they identify five
requirements that any satisfactory solution to the problem must satisfy and analyze
several proposed solutions. Müller [3] followed a different path. Instead of focussing
on the proposed solutions, he approaches the Measurement Problem from a formal
logic perspective. He decomposes it into six independent problems, which should be
investigated separately. Meanwhile, Freire Jr. [4] delivers a historical account, linking
the foundations of quantum mechanics to current scientific and technological advances.
Surveys dedicated to objective collapse theories are numerous. Bassi, Dorato, and
Ulbricht [5] present an in-depth analysis of objective collapse models from theoretical,
experimental, and philosophical perspectives. Carlesso et al. [6] further explore experimen­
tal tests beyond interferometric setups, while Donadi and Bassi [7] review gravity-induced
collapse models. These studies update the comprehensive review by Bassi and collaborators
from 2013 [8] and build on the foundational report on dynamical reduction models by
Ghirardi and Bassi [9], which remains a central reference in the field.

PHILOSOPHICAL MAGAZINE

3

Each of these works is worth the attention of readers interested in the status of foun­
dational discussions of quantum mechanics. Nevertheless, none delivers a broad cover­
age of the Measurement Problem; that’s precisely what we missed when we started our
journey. Addressing this gap, our review organises the various proposed solutions into
a structured overview, offering a broad reference point for both specialists and
newcomers.
Our work also brings a distinct perspective by examining the Measurement Problem
through the chemistry lens (since two authors, RSM and MB, are theoretical chemists).
Historically, chemists have treated quantum mechanics pragmatically, using it as a tool
rather than engaging with its foundational questions. However, recent advances in
quantum materials [10, 11], quantum dots for imaging and drug delivery [12], ultrafast
spectroscopy [13], and quantum computing [14, 15] have brought the Measurement
Problem into sharper focus at the chemistry labs. These fields increasingly rely on
quantum coherence, entanglement, and decoherence – concepts central to quantum
measurement theory [16, 17]. As chemists push the boundaries of quantum state
control, they may need to reconsider long-standing assumptions about wave function
collapse, observer effects, and the role of decoherence in chemical processes.
Despite being unconventional in scientific papers, we extensively referred to nonpeer-reviewed web resources, including books, essays, and videos. These resources
offer a plain language introduction and analysis free from intimidating technicalities.
They naturally don’t replace technical literature, but should not be neglected as relevant
entry points to the subject.

2. Quantum state description and evolution
This section briefly introduces basic quantum mechanics concepts, focussing on the
elements most relevant to the following discussions. For in-depth treatments, we refer
the reader to standard textbooks [18, 19]. Concise and accessible overviews can be
found in Refs. [20, 21].
Quantum mechanics encodes all information about a physical system in the quantum
state |c〉, a complex-valued unit vector in the Hilbert space H. In a finite Hilbert space, all
unit vectors are possible physical states of the system.
Consider, for example, the ammonia molecule NH3 (Figure 1). Its more stable geome­
try resembles a pyramid, with the three hydrogen atoms forming a triangular basis and
the nitrogen atom lying above or below it. Thus, ignoring molecular vibrations and
rotations, the nuclear quantum state of ammonia |c〉 has two components,

Figure 1. The ammonia (NH3 ) molecule serves as an example of a two-state quantum system. Its equi­
librium geometry is pyramidal, with the nitrogen atom lying above or below the hydrogen plane.
These two geometric configurations, labelled |up〉 and |down〉, may form a quantum superposition.

4

A. A. TOMAZ ET AL.

corresponding to pyramids up and down [22, Chapters 8 & 9]. Let’s name them |up〉 and
|down〉 states, respectively, meaning we will treat NH3 as a quantum bit (or a qubit).
In this example, the general quantum state |c〉 is a two-dimensional vector (see Figure
2(a)) written as
|c〉 = Cu |up〉 + Cd |down〉,

(1)

where Cu and Cd are complex-valued coefficients (or amplitudes) with |Cu |2 + |Cd |2 = 1.
Equation (1) trivially generalises to any number of dimensions as
􏽘
|c〉 =
Cn |fn 〉.
(2)
n

�

For a continuous basis, it becomes |c〉 = dsf(s)|s〉, and the amplitudes are called wave
functions.
So far, our example has been restricted to unit vectors, also known as pure states.
Nonetheless, the usual situation is imperfect knowledge, where we only know that the
system is in one of several possible pure states |ci 〉, each occurring with probability pi .
In this case, it is more appropriate to describe the system using a density operator
􏽘
r;
pi |ci 〉〈ci |,
(3)
i

Figure 2. Schematic representation of the quantum description of a two-state system, such as the NH3
molecule in Figure 1. (a) The quantum state |c〉 encapsulates all the system’s information and exists as
a vector in Hilbert space (illustrated here as a dashed circle plus the central dot). (b) Once a basis is
selected, |c〉 is expressed in terms of its basis components, with complex-valued amplitudes Ci . The
Hamiltonian operator Ĥ governs the state’s deterministic evolution via the Schrödinger equation. (c)
Upon measurement, the state |c〉 collapses to one of the basis vectors, with the probability of each
outcome given by |Ci |2 according to the Born rule.

PHILOSOPHICAL MAGAZINE

5

which captures statistical uncertainty over an ensemble of pure states. Densities are oper­
ators with unit trace and satisfy 〈a|r |a〉 ≥ 0 for any normalised state |a〉, regardless of the
chosen basis. A density operator represents a pure state if Tr(r2 ) = 1; otherwise, the state
is mixed.
For a composite system consisting of two subsystems A and B with Hilbert spaces HA
and HB , the total Hilbert space is the tensor product
H = HA ⊗ HB .

(4)

A pure state of the total system is a unit vector in H. It is called separable if it can be
written as
|c〉 = |ak 〉 ⊗ |bk 〉;

(5)

otherwise, it is said to be entangled. |ai 〉 and |bi 〉 are normalised, not necessarily orthog­
onal, states of the two systems. A general pure state can be expressed as a superposition of
product basis states:
􏽘
|c〉 =
Cij |ai 〉 ⊗ |bj 〉.
(6)
i,j

For mixed states, a density operator ρ is said to be separable if it can be written as
􏽘
(B)
r=
pk r(A)
(7)
k ⊗ rk ,
k

􏽐
(B)
where each r(A)
k pk = 1.
k and rk are density operators on HA and HB , and pk ≥ 0,
Otherwise, ρ is entangled.
The generalisation to more than two subsystems is straightforward.
The state vector is a dynamical quantity that evolves unitarily according to
|c(t)〉 = U(t, t0 ) |c(t0 )〉, which implies it satisfies the Schrödinger equation:
i h−

d
|c(t)〉 = Ĥ|c(t)〉,
dt

(8)

where Ĥ is the Hamiltonian operator (see Figure 2(b)). Equivalently, the density operator
r(t) evolves according to the von Neumann equation:
i h−

􏼃
dr(t) 􏼂
= Ĥ, r(t) ,
dt

(9)

where [Ĥ, r] = Ĥ r − rĤ denotes the commutator.
Every measurable physical quantity (observable) is represented by a self-adjoint oper­
ator Ô = Ô† on H. The possible outcomes of a measurement of Ô are its eigenvalues
on [ R. For a non-degenerate spectrum, the probability of obtaining the outcome on at
measurement time t′ is (see Figure 2(c))
􏼌
􏼌2
P(on ) = 􏼌〈on | c(t ′ )〉􏼌 ,

(10)

where |on 〉 is the corresponding eigenstate. In terms of the density operator, this

6

A. A. TOMAZ ET AL.

probability becomes
􏼂
􏼃
P(on ) = Tr |on 〉〈on |r(t ′ ) .

(11)

This formulation corresponds to a projective measurement (also known as a projectionvalued measure, or PVM), where the outcome on is associated with the projection oper­
ator |on 〉〈on |. For more general types of quantum measurements – such as those involving
degenerate spectra or positive operator-valued measures (POVMs) – we refer the reader
to Ref. [21] for a pedagogical overview.
According to the standard postulates of quantum mechanics, after the measurement,
the system is left in the normalised eigenstate |on 〉 if on was measured. This state change
is referred to as quantum state collapse. In this discussion, we assumed that collapse is
instantaneous and occurs at t ′ . Standard quantum theory gives no clue as to whether
this is precise or not. Recent resonant inelastic X-ray scattering (RIXS) experiments
have suggested that state collapse occurs gradually over a finite time [23]. However,
this interpretation remains ambiguous, as the observed dynamics could also be
explained by progressive decoherence rather than a fundamental modification of
quantum measurement. We will return to when and how long it takes for collapse to
occur in discussing Objective Collapse Theories in Section 5.3. The implications of
an instantaneous collapse are explored in Section 5.7, in the context of quantum
field measurements.

3. The problems with quantum measurements
To summarise the description of the quantum state evolution discussed in the previous
section, standard quantum mechanics prescribes that a quantum state follows two types
of time evolution: Left on its own, it evolves with the Schrödinger equation, which is
unitary and deterministic [18, Ch 3, 19, Ch 1]. During a measurement, the system pro­
duces a classical outcome with probabilities given by the Born rule. In idealised cases, this
is often described by a non-unitary state update (the projection postulate), but more gen­
erally, a measurement is any transformation that extracts classical information from a
quantum system. These processes must be probabilistic and cannot allow communi­
cation between distant systems without a physical carrier.
There are different ways to scrutinise this description [3, 24, 25]. Here, we follow
Schlosshauer [26, Ch 2], who decomposed it into three problems: the problem of the pre­
ferred basis, the problem of the nonobservability of interference, and the problem of out­
comes. Each of these challenges arises naturally from the standard formulation of
quantum mechanics and highlights a gap in our understanding of what happens when
a quantum system is measured. Below, we define these problems in sequence.
The problem of the preferred basis. Suppose we have an apparatus to detect whether the
NH3 molecule is up or down. This apparatus is also modelled as a quantum system,
initially in a ‘ready’ state. If it measures the molecule up, its pointer moves to 1; if it
detects down, it moves to 0 (in the following, we will omit ⊗ for brevity):
|up〉|ready〉 → |up〉|1〉,
|down〉|ready〉 → |down〉|0〉.

(12)

PHILOSOPHICAL MAGAZINE

7

If the molecule is initially in the superposition
􏼁
1
|c〉 = √�� |up〉 + |down〉 ,
2

(13)

the measurement interaction leads to an entangled state:
􏼁
1
|c〉|ready〉 → √�� |up〉|1〉 + |down〉|0〉 .
2

(14)

This one-to-one correlation between system and apparatus defines the premeasurement
state in the von Neumann measurement scheme [26], where a collapse (or equivalent
mechanism) is needed to produce a definite outcome.
The same final state can be expressed in a different basis. Define (Figure 3):
􏼁
|+〉 = √1�2 |up〉 + |down〉 ,
􏼁
(15)
|− 〉 = √1�2 |up〉 − |down〉 ,
and
|A〉 = √1�2 (|1〉 + |0〉),
|B〉 = √1�2 (|1〉 − |0〉),

(16)

Then the same entangled state becomes
1
|F〉 = √�� (|+〉|A〉 + |− 〉|B〉).
2

(17)

Formally, both descriptions are equivalent. But in practise, the apparatus always pro­
duces outcomes on a specific basis – here, {|1〉, |0〉} – not in {|A〉, |B〉} or any other.
One might argue that the apparatus, by design, selects the measurement basis. But this
assumes what needs to be explained: how and why a particular basis emerges from the

Figure 3. The choice of basis to describe the quantum system is arbitrary in principle. The quantum
state |c〉 can be equally written in terms of the {|up〉, |down〉} or {|+〉, |− 〉} basis. In the premeasure­
ment entangled state, this basis ambiguity extends to the apparatus as well, although only the
system’s basis is illustrated here.

8

A. A. TOMAZ ET AL.

unitary quantum dynamics. After all, the entangled state can be expressed in many
incompatible bases, and the Schrödinger equation itself does not single out any of them.
This ambiguity – why a specific set of outcomes is realised when many are in principle
available – is the problem of the preferred basis, first formulated by Zurek [27].
The problem of the nonobservability of interference. Quantum mechanics predicts that
systems can exist in coherent superpositions, which should produce observable interfer­
ence effects. Indeed, such effects are routinely seen at microscopic scales – for instance, in
electron double-slit experiments [28] or the oscillations of generalised oscillator strengths
for symmetric molecules under electron impact [29]. More recently, Kanitz and
coworkers demonstrated interference patterns from helium and hydrogen atoms
transmitted through single-layer graphene, achieving diffraction with atoms at kiloelec­
tronvolt energies [30].
Nevertheless, interference is never observed in macroscopic objects: tables, measure­
ment devices, or Schrödinger’s cat do not display interference fringes. One might suspect
this absence is simply due to the extremely short de Broglie wavelengths of large systems,
making interference effects undetectable. However, this explanation is insufficient. Under
carefully controlled conditions, interference remains observable even for massive mol­
ecules with minuscule de Broglie wavelengths, as demonstrated by Talbot diffraction
experiments with molecules comprising up to 2000 atoms [31]. Thus, the absence of
interference in everyday situations cannot be entirely attributed to technical limitations.
The real puzzle is why coherence, though allowed in principle by the Schrödinger
equation, becomes unobservable in practise beyond microscopic scales. This discon­
nect defines the problem of the nonobservability of interference and points toward
the need for a dynamical mechanism that suppresses coherence in macroscopic
systems.
The problem of outcomes. Even after addressing the previous two issues – identifying
a preferred basis and suppressing interference – a fundamental question remains: Why
do measurements yield a single, definite outcome rather than a superposition of poss­
ible results? After decoherence, the total system (including apparatus and environ­
ment) is still described by an entangled quantum state encompassing all possible
outcomes (as shown in Equation (14). Yet we never observe such superpositions:
each measurement yields a unique result. Indeed, what would it even mean to
observe a superposition?
Standard quantum mechanics provides no mechanism for this selection. The Born
rule accurately predicts the statistical distribution of outcomes over many measurements.
Still, it does not explain why a particular result occurs or what selects it in an individual
run.
These three problems define the core of the Measurement Problem [26, Ch 2]. The
following section explores how decoherence addresses the first two problems, while a
dedicated discussion on the problem of outcomes follows in Section 5.

4. Decoherence
The problem of the nonobservability of interference is addressed by decoherence.
Decoherence disperses the quantum information about a system into correlations
with the surrounding environment, suppressing the observable effects of

PHILOSOPHICAL MAGAZINE

9

superposition [26, 32]. To have a feeling of how decoherence acts, suppose that our
|up〉 and |down〉 system can interact with an environment with only three states, |e0 〉,
|e1 〉, and |e2 〉. We initially prepare the system in a superposition of |up〉 and |down〉
and the environment in |e0 〉, such that the initial state of the system plus environ­
ment is
|C(t0 )〉 = (a|up〉 + b|down〉) ⊗ |e0 〉.

(18)

Because of the interaction between the system and its environment, the joint
quantum state becomes entangled:
|C(t1 )〉 = a|up〉|e1 〉 + b|down〉|e2 〉.

(19)

We can monitor the system’s evolution alone, averaging it over the environment
states. This is done by computing the reduced density matrix for the system. This
average is obtained by taking the trace over the environment’s states of the fulldensity operator:

rS = TrE [|C〉〈C|]
􏼢
􏼣
|a|2
ab∗ 〈e2 |e1 〉
=
ba∗ 〈e1 |e2 〉
|b|2

(20)

The diagonal terms |a|2 and |b|2 are the |up〉 and |down〉 populations. The off-diag­
onal terms are the coherences and are responsible for quantum interferences.
In general, the environmental states are not orthogonal, and the coherences are
non-null. However, as time passes, the environment states tend to become
effectively orthogonal because their dynamics are different when the environment
interacts with the system’s |up〉 and |down〉 geometries. Thus, the off-diagonal terms
tend to zero,
􏼔
􏼕
􏼔
􏼕
ab∗ 〈e2 |e1 〉 Decoherence |a|2
0
|a|2
− − − − −− →
,
(21)
rS =
ba∗ 〈e1 |e2 〉
0 |b|2
|b|2
because 〈e1 |e2 〉 dynamically becomes null. This process is called decoherence.
In formal terms, decoherence arises from the time propagation of the reduced density
matrix, which evolves with a master equation of the type [26, Ch 4].
􏼂
􏼃
drS (t)
= − ih− ĤS , rS (t) +
dt
􏽼�������􏽻􏽺�������􏽽
Unitary evolution

􏼂
􏼃
D̂ rS (t)
􏽼���􏽻􏽺���􏽽

,

(22)

Decoherence/dissipation

where ĤS is the system’s Hamiltonian, including the environment’s perturbation. D̂ is the
term responsible for decoherence to the environment.
Decoherence tends to be extremely fast when considering the environment as a multi­
dimensional system. For example, we can employ the Joos-Zeh model [33] to estimate
the decoherence time of the and |up|down superposition in ammonia gas. According
to this model, the coherence in Equation (21) decays exponentially,
􏼁
􏼁 t
rS up, down, t = rS up, down, 0 e− tD ,
(23)

10

A. A. TOMAZ ET AL.

with a decoherence time given as

tD =

1
.
1
3
8 N
2 a2 (Dx)2 (k T)2
(2
p
M)
B
2
3h− V

(24)

In this equation, N/V is the number density of the gas at temperature T. M is the mol­
ecular mass. a is the molecule’s size (the molecule is assumed to be a dielectric
sphere), and Dx is the displacement between the |up〉 and |down〉 geometries. Plugging
these quantities in Equation (24), we find that NH3 coherence disappears almost instan­
taneously within 10− 19 s under room temperature and pressure. Although the superposi­
tion persists in the combined system and environment, its effects become unobservable
due to dispersal in the gas.
Although decoherence often occurs in femtoseconds or even sub-femtoseconds,
specific molecular systems exhibit surprisingly long-lived coherence effects. For instance,
Kaufman et al. [34] demonstrated that electronic coherences could survive for hundreds
of femtoseconds in molecules with near parallel potential energy surfaces due to reduced
dephasing between branched wavepackets (see also Figure 4). Schultz et al. [16] compre­
hensively review cases where vibronic coupling and structured environments lead to long
coherence lifetimes, including examples from light-harvesting complexes in
photosynthesis.
Babcock et al. [35] reported superradiant effects in tryptophan networks extending
over microtubule-scale architectures, which require long-lived electronic coherence.
This is remarkable, since superradiance typically unfolds over hundreds of femtoseconds
[36]. For isolated tryptophan in aqueous solution, electronic decoherence occurs in less
than 100 fs [37], implying that the protein scaffold must be critical in preserving coher­
ence to allow superradiant emission. Babcock’s result has also attracted media attention
(see here and here) because it may support Hameroff-Penrose’s hypothesis on the
quantum origin of consciousness (see Section 5.6.2).

Figure 4. Schematic illustration of molecular evolution after photoexcitation. The nuclear wavepacket
initially relaxes in the excited state until reaching a degeneracy region with the ground state within a
time tN . There, coherence builds, but it is quickly counteracted by decoherence due to wavepacket
dephasing, disappearing within tD . Up to this point, the Schrödinger equation provides an impeccable
description of the phenomenon. If the molecule is measured at tC , it will either be in the ground (as
illustrated) or in the excited state, with statistics following the Born rule.

PHILOSOPHICAL MAGAZINE

11

These findings suggest that molecular architecture can sometimes counteract decoher­
ence, challenging the assumption that coherence always vanishes rapidly. Theory,
especially atomistic simulations [38], has still to catch up in this field.
In addition to suppressing quantum interferences, decoherence also addresses the
problem of the preferred basis. It leads to the selection of a stable outcome basis
through a process known as einselection, which drives the quantum state to the basis
least entangled with the environment (this basis is known as the pointer basis) [27].
This preferred basis depends on the Hamiltonian [39]. Assuming that the position oper­
ator commutes with the system-environment interaction Hamiltonian (usually the case),
decoherence tends to select the position eigenstates as the preferred basis as long as the
interaction Hamiltonian is more important for the dynamics than the system’s Hamil­
tonian. If both terms compete, the preferred basis is one close to coherent states,
which minimises the uncertainty in both position and momentum. If the system’s Ham­
iltonian dominates the dynamics, energy eigenstates are preferred as the basis.
For a molecule in a gas, Paz and Zurek’s analysis [39] implies that the outcome basis of
the environment selects for measuring nuclei is approximately position states. On the
other hand, energy states emerge as the preferred outcome basis for measuring electrons.
Thus, when we initially chose the {|up〉, |down〉} basis for describing the quantum state of
the ammonia molecule, we did it because it matched our classical intuition of nuclei cor­
responding to particles with defined positions. After discussing decoherence, we realise
that we may have developed such a classic intuition because the environment selects the
{|up〉, |down〉} basis and suppresses superposition effects, creating a world of particles
with well-defined positions.
Nevertheless, einselection may not be the last word in the preferred basis problem.
Adil and co-authors have recently shown that the preferred basis is not solely dictated
by the system-environment interaction, but also by the natural factorisation of the
global Hilbert space [40]. Different factorizations can lead to multiple coexisting sets
of pointer states, meaning classical behaviour emerges in different ways depending on
the structure of the Hamiltonian. These coexisting classical realms challenge the idea
that einselection always yields a single classical outcome. They may even reignite the pre­
ferred basis problem, but now at the level of Hamiltonian factorisation.
Decoherence explains why quantum superpositions become locally invisible; however,
it does not explain why multiple observers consistently agree on what they observe. Zurek
proposed that this consensus arises through Quantum Darwinism [41, 42], a process in
which the environment acts not as a sink of information but as a communication
channel. As the system interacts with its surroundings, information about its pointer
states – those least perturbed by decoherence – is redundantly imprinted across many
fragments of the environment. Different observers can then independently access these
fragments to infer the same system properties without disturbing them. Objectivity, in
this view, emerges as a Darwinian selection of information: only the most robust, redun­
dantly recorded observables survive to be classically shared.
Decoherence is part of the standard quantum mechanics toolkit. It is an experimen­
tally well-documented effect crucial for quantum mechanical applications, such as
quantum information [21]. Regardless of one’s preferred interpretation, the role of deco­
herence remains essential and cannot be ignored.

12

A. A. TOMAZ ET AL.

This dominant role of decoherence in the current understanding of quantum mech­
anical processes does not imply a consensus. Landsmann, for instance, characterises
decoherence as ‘an unmitigated disaster’ [43, Ch 11]. His core criticism is that decoher­
ence rigorously only occurs in an environment with infinite degrees of freedom after
infinite interaction time with the system. Kastner reinforces this criticism by noticing
that decoherence claims of describing irreversible processes suffer from similar concep­
tual problems already present in statistical mechanics when explaining the emergence of
irreversibility from reversible processes [44].

5. Facing the problem of outcomes
In the previous section, we saw that decoherence clarifies a significant portion of the
Measurement Problem. However, the problem of outcomes is still open: After the basis
is chosen and quantum superpositions are suppressed, the system remains in a
mixture of possible outcomes. Decoherence does not tell how and why only one of
these outcomes is measured. At this point, standard interpretation of quantum mech­
anics postulates an additional dynamic step, the collapse:
􏼔
􏼕
Collapse 1 0
−−−−−−−−−→ 0 0
􏼔
􏼕
􏼔
􏼕
ab∗ 〈e2 |e1 〉 Decoherence |a|2
0
|a|2
or
− − − − −− →
(25)
rS =
∗
|b|2
ba 〈e1 |e2 〉
0 |b|2
􏼔
􏼕
Collapse 0 0
−−−−−−−−−→ 0 1
We illustrate these different processes with an example of a photoexcited molecule under­
going internal conversion in Figure 4. Light initially promotes the molecule to an excited
electronic state. The nuclear wavepacket evolves on the potential energy surface of the
excited state until it reaches a region of degeneracy with the ground state potential
energy surface. There, quantum coherence builds between the two states, creating a state
superposition. The dephasing between the wavepacket components in each state counter­
acts, causing decoherence. All events up to this point, including decoherence, can be simu­
lated by propagating the Schrödinger equation for the molecule [45]. If the molecule is
measured, it will be found to be either in the ground or excited state. However, our simu­
lation can only tell the probabilities of these outputs.
Standard quantum mechanics assumes that a wave function collapse occurred. Never­
theless, the existence of collapse is far from consensual. It is regarded as a superfluous
hypothesis [46] in several quantum mechanical interpretations.
In the following subsections, we will dive into a few classes of potential solutions that
represent the current debate on the Measurement Problem, with little attention to phi­
losophical and historical aspects. More comprehensive approaches can be found in
Refs. [4, 43, Introduction & Ch 11, 47, 48].
Before that, we should clarify the concepts we are dealing with. In literature, decoher­
ence and collapse concepts are sometimes used interchangeably. We should avoid it, as
these phenomena may, in principle, be completely independent and occur on different
time scales.

PHILOSOPHICAL MAGAZINE

13

As stated in Equation (25), decoherence acts on the off-diagonal terms of the system’s
reduced density matrix. Collapse, however, zeroes all diagonal terms except one in the
entire density matrix – that is, the matrix describing the system, apparatus, and observer
collectively, which Equation (25) does not represent. We can be a bit more flexible with
this definition. In principle, a quantum theory including collapse could go as far as to
provide a diagonal density matrix. This means we would be left in a situation of statistical
uncertainty: the collapse occurred, but the theory only informed us of the probability of
each outcome. We could call such a case an epistemic collapse. If, however, the theory
zeroes the diagonal (except one) elements, then we would have an ontic collapse.
5.1. Many-worlds interpretation
The lack of information on the outcomes is not a problem for some interpretations. For
instance, the Many-Worlds Interpretation (or Relative State Interpretation or, still, Ever­
ettian Quantum Mechanics) proposes that the remaining outcomes after decoherence cor­
respond to independent universe branches [49]. Observers existing in each branch
perceive different outcomes because their quantum state, entangled with the molecular
quantum state, also branches. In one branch, the combined molecule-observer quantum
state may be |up〉|observer− sees− up〉 and in another, |down〉|observer− sees− down〉. No
observed branches with superpositions of both states exist because of decoherence
toward the environment (surrounding the system and the observer) suppressing them
[50]. Thus, the Many-Worlds Interpretation posits the existence of a single quantum uni­
verse composed of non-communicating classical branches.
For the Many-Worlds Interpretation, the quantum state |c〉 is a complete description
of reality (no hidden variables are required), exclusively evolving according to the Schrö­
dinger equation (collapse is only an illusion caused by the universe branching) [51, 52].
Thus, the Many-Worlds Interpretation is consistent with standard quantum mechanics
and requires no modification to the theory. However, it remains an interpretation rather
than a testable theory, since it currently makes no unique experimental predictions. A
significant challenge is the technical infeasibility of maintaining and measuring a
quantum system in a coherent superposition of orthogonal states, especially for large
systems. This difficulty explains why superpositions of macroscopic states cannot be
observed directly due to rapid decoherence. Susskind and Aaronson demonstrated this
limitation using methods from quantum computational complexity, naming it the
quantum-hard problem [53, 54].
A puzzling feature of the Many-Worlds Interpretation is understanding how the
deterministic branching relates to the wave function amplitudes and the Born rule.
Carroll and Sebens [55] propose that this relation is established after decoherence
occurs but before the measurement is registered. In this period, if the observer wants
to estimate which branch they are, their rational credence directly leads to the Born
rule. Thus, the probabilistic character of quantum mechanics would be a subjective
aspect arising from the observer’s self-locating uncertainty. Carroll and Sebens’ deri­
vation of the Born rule is only strictly valid if the ratios of branch amplitudes are the
square roots of rational numbers. However, they argue that the large number of branches
in practical situations always allows this condition to be approximately satisfied. This
approximation also enables experimental tests of their hypothesis by searching for

14

A. A. TOMAZ ET AL.

minor deviations from the Born rule. Kent [56] sharply questioned the conceptual and
mathematical soundness of Carroll and Sebens’ account, arguing that their notion of
self-locating uncertainty presupposes an objective and well-defined branching of the
wave function – something not provided by the Everettian framework itself.
Like Carroll and Sebens, Short [57] derives the Born rule in Many-Worlds Interpret­
ation based on estimating the probability of picking a random branch among many.
However, instead of relying on self-locating uncertainty, he does it by establishing
three axioms that the probability must satisfy: (1) the probability depends only on the
present state (regardless of how it was generated); (2) only branches with non-zero
amplitudes count as components of the many-world state; (3) probability cannot flow
between uncoupled worlds. Short then shows that the Born rule uniquely satisfies
these axioms.
The Many-Worlds Interpretation may seem exotic to non-specialists due to its
exuberant ontology. Despite this perception, it is a serious contender among the pro­
posed solutions to the Measurement Problem. It is a popular interpretation among phy­
sicists, with prominent supporters like Carroll [51, 52, 55], Tegmark [58], Zeh [46, 59,
60], and Deutsch – though their formulations vary in how explicitly Everettian they
are and in the extent of their commitment to the metaphysics of many worlds.
However, it also faces outstanding critics, like Penrose [61] and Albert. For Landsmann,
the Many-Worlds Interpretation would be ‘acceptable only if truly everything else has
failed’ [43, Ch 11].
5.2. Epistemic interpretations
Epistemic interpretations claim that a quantum state is no more than a mathematical tool
to predict outcomes. This stance is shared by interpretations such as the Relational
Interpretation [62–64], Quantum Information-Theoretic approaches [65], Quantum
Bayesianism [66], and Indivisible Stochastic Process Theory [67], which are discussed
next.
5.2.1. Relational interpretation
The Relational Interpretation of quantum mechanics (or relational quantum mechanics),
proposed by Rovelli, focuses on the interaction between systems, emphasising that prop­
erties are defined only in relation to such interactions [64]. Thus, the molecular geometry
may be well-defined for a nearby molecule in the environment acting as an observer
while remaining in superposition for another molecule that is too distant to interact
significantly.
Rovelli draws attention to the fact that this state dependence on a specific observer is
not new in physics. It is analogous, for instance, to the velocity dependence on the par­
ticular reference frame in which it is measured. The novelty in quantum mechanics is
that the non-commutative nature of quantum variables implies that not all properties
can be sharply defined simultaneously [64], limiting the completeness of information
derivable from a single interaction.
In the Relational Interpretation, the wave function is not ontologically real (see
Section 6 for discussion). Instead, it serves as a tool for predicting the probabilities of
interaction outcomes. Conceptual issues with measurement arise only when undue

PHILOSOPHICAL MAGAZINE

15

ontological weight is assigned to it. By treating the wave function purely as a predictive
instrument, measurement can be reframed as an ordinary interaction, resolving these
difficulties.
The Relational Interpretation is characterised by a sparse ontology [64], meaning that
properties are not defined between interactions. Nevertheless, it remains a realist
interpretation because it posits a physical world of interacting systems.
Giacomini, Castro-Ruiz, and Brukner have recently extended relational ideas
beyond Rovelli’s Relational Quantum Mechanics by incorporating Quantum Reference
Frames, QRF [68]. In their approach, a QRF is simply a quantum system elevated to the
role of a reference frame so that its degrees of freedom define the origin relative to
which one describes other systems. By extending canonical transformations to the
quantum domain, Giacomini et al. show how usual frame changes (translations, for
example) remain valid even if the reference frame itself is in a superposition or
entangled state. Their approach leads to the relativity of notions like superposition
and entanglement. If a given particle is in a spatial superposition from the lab’s view­
point, then from the particle’s viewpoint, the lab may itself appear in a corresponding
superposition.
This perspective may offer new insights into the Measurement Problem, particularly
in Wigner’s friend scenarios, where the possibility of conflicting accounts among obser­
vers becomes natural if each observer constitutes its own QRF [68, 69]. Section 5.3.2 dis­
cusses how Giacomini and Brukner use QRFs to challenge Penrose’s conjecture on
gravity-induced collapse [70].
5.2.2. Information-theoretic and QBism views
Another epistemic perspective comes from quantum information theory, which treats
quantum mechanics as an axiomatic framework akin to thermodynamics. Brukner and
Zeilinger [65] argue that quantum theory is fundamentally about information, not
underlying physical reality. Its postulates describe how information is processed, not
how systems evolve in space and time.
Recent experimental results reinforce this perspective. Spegel-Lexne and co-authors
demonstrated the equivalence of entropic uncertainty and wave-particle duality [71],
suggesting that quantum measurement can be understood through informational con­
straints rather than wave function collapse.
A more radical variant of this informational approach is Quantum Bayesianism, or
QBism [66]. QBism interprets the quantum state not as a system property but as a
tool that reflects an agent’s personal beliefs (or more precisely, doxastic states) about
the outcomes of their measurements. For instance, assigning the state |up to a molecule
expresses an agent’s expectation about what they will experience upon interacting with it,
not a claim about an objective feature of the molecule. When a measurement is made, the
quantum state is updated to reflect the agent’s new information, akin to a Bayesian
update of probabilities. From this perspective, collapse is not a physical transformation
but the agent updating their beliefs in response to their own experience, which is the
measurement outcome [66, 72].
Some no-go theorems are sometimes cited as challenging epistemic views, particularly
the Pusey-Barrett-Rudolph (PBR) theorem [73]. It shows that, under certain assump­
tions, quantum states cannot be interpreted merely as statistical knowledge about

16

A. A. TOMAZ ET AL.

underlying physical states – that is, hidden variables (see Section 5.4). Instead, the
quantum state must be part of physical reality. However, this conclusion applies only
to models that posit such hidden variables. Interpretations like QBism, which deny the
existence of underlying ontic states altogether, fall outside the scope of the theorem
[74, 75]. Rovelli has made similar clarifications for relational interpretations as well [76].
Another supposed challenge to QBism comes from Ozawa’s intersubjectivity theorem
[77, 78], which claims that two observers jointly measuring a system must agree on its
outcome. This has been interpreted as incompatible with QBism’s agent-centric frame­
work. However, Schack has recently argued that this conclusion is mistaken and that
QBism maintains consistency across observers without requiring objective outcomes
in the traditional sense [79].
A common misunderstanding is to conflate QBism with older subjectivist interpret­
ations, such as that of London and Bauer [80], who suggested that collapse results
from an observer becoming aware of an outcome. However, QBism takes a different
stance: the measurement outcome is not something the agent discovers; it is the
agent’s experience. No underlying real wave function remains untouched – it is a
theory about actions and consequences, not objective ontologies [81].
By rejecting objective quantum states, QBism sidesteps many interpretative para­
doxes, offering a consistent but radically subjective view in which quantum theory
serves as a decision-making tool for agents.
5.2.3. Indivisible stochastic process theory
Barandes has recently proposed the Indivisible Stochastic Process Theory, where classical
configurations of particles, fields, or qubits evolve via non-Markovian dynamics [67, 82].
In this type of dynamics, which recovers all results from conventional quantum mech­
anics, transition probabilities cannot be estimated at intermediate times. In Barandes’
approach, wave functions are considered predictive tools only, and the Hilbert space
of quantum mechanics is demoted to a convenient instrumentalist framework without
an ontological basis.
Barandes draws a historical analogy, comparing the transition from instrumentalist
frameworks in quantum mechanics to the Copernican revolution, where the instrumen­
tal Ptolemaic system of epicycles was replaced by a more fundamental description based
on forces. Similarly, he advocates for a clear physical picture to supersede the abstract
formalism of Hilbert space mechanics.
Unlike the Relational Interpretation (Section 5.2.1), the Indivisible Stochastic Process
formulation posits a non-perspectival, objective reality: each system has a definite
configuration that evolves stochastically in time. The ontology is well-defined at all
times: each system has a definite configuration, even between interactions. What is
sparse are the dynamical laws, since conditional probabilities connecting two moments
in time are generally defined only when the earlier time is either the initial time or a
special kind of interaction event (called a division event). This framework does not
assume divisibility or Markovianity.
By embedding quantum systems within generalised stochastic systems, the Indivisible
Stochastic Process formulation aligns with a realist philosophy, reinterpreting quantum
systems as governed by dynamic interactions without requiring measurement to be
treated as a distinct or special process.

PHILOSOPHICAL MAGAZINE

17

5.3. Objective collapse theories
5.3.1. Agnostic objective collapse
Opposed to Many-Worlds Interpretation and epistemic interpretations, objective collapse
theories consider that collapse is a physical process, and that standard quantum mech­
anics is still incomplete [5, 8]. Thus, these theories attempt to change the Schrödinger
equation to account for the collapse. This subsection deals with agnostic objective col­
lapse, that is, theories that do not attribute a cause to the collapse. In the following sub­
section, we will look at gravity-induced collapse.
Most objective collapse theories predict that a system in quantum superposition ran­
domly localises in one of the outcomes given enough time [8, 83–85]. The quantum state
is driven by a stochastic Schrödinger equation, such as the quantum-state diffusion
equation [86, 87]
􏽘
􏼁
􏼁2
i
h􏽘
d|c〉 = − − Ĥ|c〉 dt +
Ân − 〈An 〉 |c 〉dWn −
Ân − 〈An 〉 |c〉 dt.
2 n
h
n

(26)

In addition to the usual Hamiltonian term, the right-hand side contains two additional
terms that tend to localise the state in one of the eigenstates of the operators Ân , as illus­
trated in Figure 5 for Ân = Ĥ. The collapse is stochastic and controlled by a Wiener
process Wn (with 〈dWn 〉 = 0 and dWm dWn = dmn h dt), which, for the ensemble
density, the statistical distribution of outcomes follows the Born rule. A positive real con­
stant η sets the noise strength (diffusion rate), hence the collapse timescale. The equation
is nonlinear due to the 〈An 〉 = 〈c|Ân |c〉/〈c|c〉 terms. However, the evolution of the
ensemble density is linear thanks to the quadratic last term [88]. This linearity is required
to avoid superluminal information exchange.
Different objective collapse theories have been proposed, corresponding to specific
choices of operators Ân , including the Hamiltonian operator [89], position operators
(GRW after the initials of the authors [90]), density number operators (CSL for
Continuous Spontaneous Localization [84]), and mass density operators [91] (which
is discussed in Section 5.3.2). These specific models are thoroughly reviewed in Refs.
[5, 9].
No observers or interacting systems are required in Equation (26). The localisation
time depends on the size of the system. It may take billions of years for an isolated
ammonia molecule in superposition to collapse to |up〉 or |down〉. In a gas, however,
such localisation occurs nearly instantaneously.
5.3.2. Gravity-induced objective collapse
The highest stakes among the objective collapse theories are those proposing that gravity
is the cause of the collapse. Penrose [92], for instance, claims that distinct mass distri­
butions in superposition (mup for up or mdown for down in ammonia molecule) would
cause slightly different spacetime distortions. The instability associated with these super­
imposed distortions leads to the wave function collapse within a time
h−
tc =
(27)
ED

18

A. A. TOMAZ ET AL.

Figure 5. Example of application of the stochastic Schrödinger equation (Equation (26)) taking the
Hamiltonian of the one-dimensional harmonic oscillator for the operators Ân . The system is initially
􏽱�
􏽱�
􏽱�
in a superposition |c(0)〉 = 16 |1〉 + 23 |2〉 + 16 |3〉 of the ground and first two excited states. The
oscillator’s mass and angular frequency are equal to one atomic unit. η was arbitrarily chosen as
0.25 au. (a)–(c) Shows the population evolution in three realizations, each collapsing to a different
state. (d) The statistics over 10 thousand realizations show that the stochastic formulation recovers
the Born rule with 1/6, 2/3, and 1/6 probabilities for states 1, 2, and 3, respectively. (e) For the
employed parameters, the collapse occurs within a few femtoseconds. Simulations were performed
using the Skitten program developed in our group.

where ED is the Newtonian gravitational self-energy
􏽚
ED = 4pG d3 rd3 r′

􏼐

mup (r′ ) − mdown (r′ )

􏼑􏼐
􏼑
mup (r) − mdown (r)

|r − r′ |

,

(28)

and G is the gravitational constant. This collapse time can also be derived by computing
the difference between Newtonian free-fall accelerations in the space surrounding each
geometry [93]. A direct application of Equation (27) predicts it would take billions of
years to collapse the wave function of an isolated molecule, but only 10− 27 s to observe
collapse in a 10 kg body (Figure 6) [1].
The same collapse time arises from the Quantum Mechanics with Universal Density
Localization (QMUDL), the model Diósi proposed for the stochastic state evolution
[91]. In QMUDL, the Schrödinger equation is modified to

PHILOSOPHICAL MAGAZINE

19

Figure 6. Diósi-Penrose collapse time as a function of the total mass. The estimate was made for a
homogeneous carbon system. The collapse times for such a system with the masses of fullerene
C70 , a protein, an adenovirus, a grain of pollen, and a small dog are indicated. Figure reproduced
from Ref. [1].

􏽚
􏼁
i
d|c〉 = − Ĥ|c〉 dt + m̂(r) − 〈m̂(r)〉 dW(r) dr|c〉
h
􏼁
􏼁
􏽚􏽚
m̂(r) − 〈m̂(r)〉 m̂(r′ ) − 〈m̂(r′ )〉
kG
− −
dr dr′ |c〉 dt,
4h
|r − r′ |

(29)

where the scalar Wiener process is defined by 〈dW〉 = 0 and
dW(r) dW(r′ ) = kG dt/(2h− |r − r′ |). This equation is a particular case of Equation (26)
where the operators Ân are taken proportional to the mass density operator m̂. The
random noise is proportional to the ratio between the gravitational constant G and the
reduced Planck constant —. κ is an arbitrary dimensionless constant. Despite the distinct
and independent derivations, the collapse time (27) is generally called the Diósi-Penrose
Model.
The Diósi-Penrose model has attracted criticism on multiple fronts. Gao [94] raised
several issues on the Penrose conjecture. His main point is that Penrose’s argument by
analogy with the conventional quantum mechanical time-uncertainty principle is not rig­
orous enough. Moreover, he is also right to point out that although we commonly refer to
the Diósi-Penrose model, Diósi and Penrose theories are fundamentally distinct, arriving
at the same collapse time through independent, though conceptually related, arguments.
Diósi himself [95] notes their similarities and differences and suggests that further work
is needed to clarify whether the two frameworks are compatible.
Giacomini and Brukner [70] also challenged Penrose’s conjecture that quantum
superposition conflicts with Einstein’s equivalence principle. Using the Quantum Refer­
ence Frames (QRF) formalism (see also 5.2.1), they showed that it is possible to generalise
the principle (or, more precisely, always to make the metric field locally Minkowskian)
even in the presence of quantum superpositions of massive bodies.

20

A. A. TOMAZ ET AL.

Additionally, our atomistic simulations showed that the Diósi-Penrose collapse time
reaches a minimum value independent of superposition displacement and, in some
instances, can be surprisingly long [1]. Figurato et al. [96] have also independently con­
cluded that the model could have too long collapse times for macroscopic bodies. Beyond
these theoretical concerns, experimental tests have also challenged the model. Donadi et
al. [97] and Arnquist et al. [98] conducted underground experiments to test gravityrelated collapse mechanisms. Their results placed stringent constraints on the model’s
parameters (see Section 5.3.3).
Although all these points must be considered when assessing the validity of the DiósiPenrose model, none of them directly falsifies the model. And, as Thorne said, ‘Penrose
has a way of always being right, even when he does things in a strange way’ [99].
Oppenheim has recently proposed another hypothesis that attributes wave function
collapse to the influence of gravity. Indeed, his Postquantum Theory of Classical
Gravity does not focus on the Measurement Problem and has a more ambitious goal
of reconciling gravity and quantum mechanics [100]. Oppenheim’s central hypothesis
is that gravity is a classical field. To ensure classical gravity can interact coherently
with quantum matter fields, Oppenheim and colleagues developed a Classical
Quantum (CQ) Dynamics framework, which circumvents the usual obstacles encoun­
tered by semiclassical models, such as violation of the superposition principle due to non­
linearities in the equations of motion [100–102].
The CQ dynamics of the hybrid state r(z, t) (where z represents the classical phase
space coordinates) is expressed in terms of the general master equation [100]
􏼒
􏽯 􏼓
􏼃 􏽘 mn
∂r
i􏼂
1􏽮 †
L̂m L̂n , r
= − − Ĥ, r +
l L̂m rL̂†n −
+
h
2
∂t
m,n
􏽚
􏽘
􏼈
􏼉
􏼁
1 􏽘 mn
W mn z|z′ ; t L̂m rL̂†n −
W (z; t) L̂†n L̂m , r + ,
+ dz′
2 m,n
m,n

(30)

which can describe back reactions of quantum matter fields in classical (including grav­
itational) fields. This equation has completely positive dynamics (hence probabilities
remain positive), preserves the trace (probabilities are conserved), and is linear in the
density operator (superluminal signalling is avoided). In addition to the commutator
term responsible for the unitary evolution and the Lindbladian term [20] (proportional
to lmn ) causing decoherence, the integral term promotes jumps in the quantum and clas­
sical subsystems. The last term preserves the norm of the quantum state.
Like in modelling open quantum systems [103], Equation (30) is not directly solved
for ρ but rather through an ensemble of stochastic trajectories (unraveling procedure)
[104, 105]. In each trajectory, the quantum degrees of freedom undergo stochastic pro­
jection onto the eigenstates of the corresponding Lindblad operators, collapsing to a
definite outcome in a manner that statistically recovers the Born rule. These quantum
jumps induce corresponding phase space jumps in the classical degrees of freedom,
representing a backreaction of the quantum system on the classical one. In addition to
collapse, this equation also describes decoherence, leading to the suppression of
quantum coherence over time. Figure 7 illustrates the quantum and classical stochastic
jumps in a system composed of a qubit and a classical particle discussed in Ref. [104]

PHILOSOPHICAL MAGAZINE

21

Figure 7. Evolution of the quantum state population and classical phase space coordinates (q, p) in
the CQ dynamics (Equation (30) with diagonal Lindblad operators of a qubit interacting with a classical
􏽱�
􏽱�
particle [104]. The initial state is d(q)d(p)( 13 |0〉 + 23 |1〉). The figure shows two stochastic trajectories.
On the left, the interaction between the subsystems collapses the qubit to state 0, while on the right, it
collapses to state 1. Stochastic jumps in the classical phase space are also observed due to backreac­
tion. If many trajectories are computed, they will be distributed as 1/3 in 0 and 2/3 in 1. The trajec­
tories were propagated for 0.05 s, with a timestep of 2.5 × 10− 5 s. The jump rate was t = 0.01 s. The
other parameters are B = 1 J·s·m− 1 , m = 1 kg, and v = 1 s− 1 . Simulations were performed with the
program provided in Ref. [104].

Even though stochastic trajectories are introduced as a means to propagate the density
evolution (30), Oppenheim and co-authors assign them ontological significance [104]. A
stochastic trajectory represents the system collapsing to a specific state, just as it is also
done in the other objective collapse theories discussed above. Their theory implies that
collapse does not require measurement, as it occurs naturally due to interactions with
a classical field [104].
Gravity-induced wave function collapse may have profound implications for physics.
If any of these theories are confirmed, it would not only close the Measurement Problem
but also imply that gravity plays a unique role in nature, different from the other funda­
mental interactions. Moreover, it would also impact future efforts to reconcile general
gravity and quantum mechanics, moving toward what Penrose calls the gravitization
of quantum mechanics [106].
5.3.3. Experimental assessment of objective collapse theories
Experimental efforts to test objective collapse models, especially CSL, have gained
remarkable traction in recent years [6, 9, 98, 107, 108]. One of the most direct approaches
involves matter-wave interferometry with large molecules or nanoparticles, designed to

22

A. A. TOMAZ ET AL.

probe the persistence of quantum coherence at mesoscopic scales [1]. Gasbarri et al.
argue that the microgravity environment of space, with its long free-fall times and low
noise, offers a unique setting for such experiments, enabling both interferometric and
non-interferometric tests with unprecedented sensitivity to collapse effects [108].
Beyond interferometry, several non-interferometric techniques have been proposed to
test collapse models without requiring explicit superpositions. Carlesso et al. reviewed
platforms such as optomechanical resonators, ultra-cold atoms, and solid-state
systems, where collapse-induced noise may manifest as excess heating or anomalous
diffusion [6]. Other proposals investigate spontaneous X-ray emission from the
random motion of charged particles, a distinctive prediction of CSL. These diverse strat­
egies have steadily improved the empirical bounds on collapse parameters, ruling out
wide ranges of the originally proposed parameter space for both CSL and DiósiPenrose models.
Recent studies have expanded the scope of experimental constraints. Altamura et al.
analyzed data from the LISA Pathfinder mission and found that rotational degrees of
freedom could provide tighter bounds than translational motion in some scenarios
[107]. In a related direction, Howl, Penrose, and Fuentes proposed an experiment
using a Bose–Einstein condensate prepared in a spatial superposition to test gravitation­
ally induced collapse [93].
As discussed in Section 5.3.2, the Diósi-Penrose model ties collapse to gravitational
self-energy. Figurato et al. investigated whether the model predicts rapid enough collapse
for macroscopic systems and showed that it does not always do so across the entire par­
ameter range [96]. Meanwhile, an underground experiment at the Gran Sasso Laboratory
searched for spontaneous radiation arising from collapse-induced diffusion, placing
strong limits on the spatial resolution of mass density – enough to exclude the original
parameter-free version of the Diósi-Penrose proposal [97].
These efforts signal a shift in the status of objective collapse theories from speculative
constructs to empirically testable frameworks. Among them, CSL stands out for its tune­
able parameters and broad compatibility with experimental platforms, while the DiósiPenrose and Oppenheim models offer more rigid, gravity-motivated alternatives. For
example, Angeli et al. recently demonstrated that if gravity is both classical and local,
as in Oppenheim’s proposal (see Section 5.3.2), then it must induce diffusion in
quantum systems, a phenomenon potentially observable with large-scale mechanical
probes such as torsion pendulums [109].
Altogether, these developments underscore the increasing interconnection of collapse
models with experimental physics. Whether or not they ultimately capture physical
reality, they provide concrete benchmarks for testing the limits of quantum theory and
may yet point toward deeper structures beyond it.
Despite the increasing experimental scrutiny of objective-collapse models, the idea
that the Schrödinger equation may provide only an incomplete description of physical
evolution continues to inspire new proposals. A recent one by Dick reframes the
Measurement Problem as an interaction problem [110]. In this view, every inelastic
energy exchange between systems acts as a mutual observation, interrupting the
smooth Schrödinger evolution and producing definite outcomes. The wave function is
interpreted as an epistemic superposition of possible ontic outcomes – elastic channels
describing continuous evolution, inelastic ones involving discontinuous quantum

PHILOSOPHICAL MAGAZINE

23

jumps. Although this approach introduces no explicit modification of the Schrödinger
equation, it assumes that the equation captures only the evolution of relative probability
amplitudes, not the actual transitions that occur during energy exchange. In this sense,
Dick’s proposal can be regarded as a minimalist form of objective collapse, locating
the breakdown of unitarity within ordinary interactions rather than in new stochastic
dynamics.
5.4. Hidden-variables theories
5.4.1. Physical restrictions on hidden variables
Hidden variable theories (also known as ontic theories) explore the hypothesis that the
quantum state |c〉 may not be a complete description of the system and that a set of
additional (hidden) variables may contain further information (accessible or not)
[111]. The hidden variables discussion is where the Measurement Problem spills the
most on other fundamental questions of quantum mechanics, such as nonlocality in
entangled systems, the completeness of quantum mechanics, and the existence of prop­
erties independently of measurement.
Hidden variable theories are typically framed within the limits of two no-go theorems
and a few physically motivated restrictions. The theorems are the Bell and the KochenSpecker ones. Bell’s theorem states that no local hidden-variable theory can be entirely
compatible with quantum mechanics [112, Ch 2, 113]. Local in this context means
that ‘the result of a measurement on one system be unaffected by operations on a
distant system with which it has interacted in the past’ [112, Ch 2].
In turn, the Kochen-Specker theorem [113–115] states that any hidden variable theory
consistent with quantum mechanics must renounce either all observables having definite
values at all times or these values being independent of how they are measured. The
theorem is strictly valid for Hilbert spaces with dimension greater than two.
Finally, the physical restrictions are the non-signalling principle (imposing that non­
locality cannot be harvested to exchange superluminal information) and the statistical
independence (supposing that initial statistical setups can be completely uncorrelated;
see also Section 5.5).
The situation seems simple from there. For instance, the experimental violations of
Bell’s inequalities [116] – confirming the predictions of quantum mechanics – imply
that physical theories must either be non-local or not have properties defined at all
times. However, no-go theorems are as strong as their underlying hypotheses, often
deeply hidden in the deduction. The restrictions imposed by these theorems and physical
principles have been constantly challenged [117, 118] (except for the non-signalling prin­
ciple, which is likely the only consensual rule in the game). Relaxing statistical indepen­
dence (sometimes loosely called the free-will principle) in Bell’s theorem, for example,
may allow for building consistent local and realist theories. We will return to this
point in Section 5.5.
5.4.2. Bohmian mechanics
Most of the practical development in hidden-variable theories happens in the framework
of Bohmian Mechanics, which posits the existence of corpuscles moving in a non-New­
tonian way and guided by a wave function [119]. The corpuscle’s velocities are

24

A. A. TOMAZ ET AL.

determined by a velocity field (the de Broglie-Bohm Equation) dependent on the wave
function, which, in turn, follows the Schrödinger evolution. This deterministic time evol­
ution in Bohmian Mechanics automatically solves the problem of outcomes. Although
Bohmian Mechanics’ experimental predictions are equivalent to quantum mechanics
[120], it is not discarded that they could be experimentally tested [121]. A striking
example is the experiment by Sharoglazova et al. [122], who investigated the energyspeed relationship of wave-guided photons in a microcavity. They observed that for eva­
nescent states within a potential step, lower-energy particles exhibited higher speeds.
This result is in tension with standard Bohmian Mechanics, which predicts zero speed
for such particles.
Poirier has proposed an alternative theory that prescribes non-Newtonian trajectories
but entirely discards wave functions [123, 124]. In this case, the quantum system is
described by an ensemble of interacting deterministic real-valued trajectories with
well-defined positions and momenta. This type of theory inscribes itself into the tradition
of hydrodynamic interpretation of quantum mechanics, inaugurated by Madelung right
after Schrödinger’s original work [125, 126, p. 222]. In Madelung’s interpretation,
quantum mechanics is modelled as a quantum fluid [127], which can be understood
as many interacting classical worlds [128].
This picture of many interacting classical worlds has been the basis of molecular
dynamics simulations, where the nuclear wave function time evolution is commonly
approximated by interacting and non-interacting trajectories, depending on the
approach [129, 130]. Tully, who proposed surface hopping, the most popular method
for nonadiabatic molecular dynamics simulations, employed the Madelung Hydrodyn­
amic Interpretation to justify using mixed quantum-classical approximations [131].
These molecular dynamics simulations, however, adopt the trajectory approach pragma­
tically without any foundational claim.
5.5. Deterministic models
Bell’s theorem shows that no local hidden variable theories can reproduce all quantum
mechanical predictions [112]. Thus, the experimental violation of Bell’s inequalities
seemed to be the end of any local deterministic model. However, Bell’s theorem explicitly
requires the validity of the statistical independence assumption, which states that the
experimental settings are not influenced by any hidden factors determining the
system’s evolution. This section surveys two local deterministic models – Superdetermin­
ism and Retrocausality – built on the challenge to the statistical independence
assumption.
Superdeterminism posits that hidden correlations between measurement settings and
system properties predetermine quantum outcomes [132]. ’t Hooft proposed a concrete
realization of this idea in his Cellular Automaton Interpretation (CAI) [133]. In this
model, the universe is fundamentally described by a discrete, classical system evolving
in time, much like a computer program updating the values of a grid according to
fixed rules. These underlying configurations, called ontological states, evolve determinis­
tically and form the actual physical reality. The familiar quantum formalism emerges
only as a statistical approximation of our ignorance about the precise ontological state.
In this view, superpositions are not real: they are computational tools that summarise

PHILOSOPHICAL MAGAZINE

25

ensembles of possible classical states. ’t Hooft argues that violations of Bell inequalities do
not imply nonlocality, but instead reflect our mistaken identification of such statistical
templates with physical systems.
A recent proposal by Donadi and Hossenfelder [134] introduced a local, deterministic
model for wave function collapse that explicitly violates statistical independence while
reproducing standard quantum predictions. Their model suggests that all quantum
states, except measurement eigenstates, are unstable under hidden-variable perturbations
and deterministically collapse before reaching the detector. Unlike objective collapse
models (see Section 5.3), the collapse dynamics in the Donadi-Hossenfelder model are
entirely deterministic.
Cosmic Bell Experiments have provided stringent tests of the statistical independence
assumption in Bell’s theorem [116, 135]. These experiments avoid the possibility that
hidden variables could influence detector settings by randomly determining measure­
ment choices using distant astrophysical sources. By doing so, they attempt to close
the freedom-of-choice loophole, which is crucial for evaluating the plausibility of super­
deterministic explanations. In a landmark experiment, Rauch et al. [116] used high-red­
shift quasars – whose light originated billions of years ago – to set measurement
parameters in a Bell test. Their results remained consistent with standard quantum
mechanics, implying that superdeterministic correlations, if they exist, should date
back to the early universe. Similarly, Handsteiner et al. [135] employed light from
distant galaxies to eliminate potential local influences on detector choices. While these
results do not strictly rule out superdeterminism, it must account for cosmologicalscale correlations to remain viable, raising deep challenges for its plausibility.
Retrocausal Interpretations also challenge the statistical independence assumption,
but, even bolder than Superdeterminism, it assumes influence from future events.
Such interpretations propose that the Measurement Problem arises from assuming a
one-way flow of time. Models such as the Two-State Vector Formalism [136] describe
quantum systems by an initial state evolving forward in time and a final state evolving
backward from the measurement outcome. The interaction of these forward- and back­
ward-evolving states determines the probabilities of different results. The Pechukas’
forces [137], which are still the primary justification used today for momentum rescaling
along nonadiabatic coupling vectors in molecular dynamics [138], were derived from this
same type of forward and backward propagation to determine quantum transitions in
atomic collisions.
Retrocausality is still an active research field. Adlam [139] proposed that accepting
nonlocality and imposing relativistic constraints (such as the nonexistence of a preferred
reference frame) leads to retrocausality. Sutherland [140] derived the Born rule within a
retrocausal model. This is a significant result because it changes the status of the rule
from a postulate to a natural consequence of incorporating time-symmetric boundary
conditions in quantum mechanics. A notable development is the Fixed-Point Formu­
lation proposed by Ridley and Adlam, which presents an atemporal, all-at-once frame­
work for retrocausality and includes a full derivation of the Born rule [141, 142].
Another recent contribution is van der Pals’ retrocausal hidden-variable model [143],
which attributes the emergence of definite outcomes to resonance conditions between
advanced and retarded virtual photons. These photons arise from an underlying, timesymmetric periodic process occurring beneath the Heisenberg uncertainty threshold.

26

A. A. TOMAZ ET AL.

Both Superdeterminism and Retrocausality remain controversial and experimentally
unverified. Nevertheless, despite their speculative nature, these models provide a striking
contrast to interpretations that rely on wave function collapse, branching universes, or
fundamental randomness [144], keeping the possibility of a fully local and deterministic
resolution to the Measurement Problem open.
5.6. Dualist collapse hypotheses
5.6.1. Classical-apparatus inducing collapse
The core of the Copenhagen Interpretation of quantum mechanics, developed by Bohr
and Heisenberg, is the assumption that any experiment in physics must be described
in terms of classical physical concepts [43, Introduction]. When such an experiment
falls within the realm of quantum mechanics, the tension between the system’s
quantum description and the apparatus’s classical description is the crucial factor that
causes statistical uncertainty and ultimately selects a single output [145]. There is no
claim that the classical apparatus is not composed of quantum particles. It is just that
the description of the experiment is restricted to the use of classical terminology.
This quantum-classical duality, formulated as the Heisenberg Cut arbitrarily separ­
ating classical from quantum systems, still plays a role in a pragmatic definition of
measurement [146]. It is also at the basis of the asymptotic emergence hypothesis [147],
which poses that collapse is a unitary physical process. Asymptotic emergence
employs algebraic quantum theory to demonstrate that some phenomena forbidden in
the quantum limit (like collapse) are allowed in the classical limit due to some exponen­
tial sensitivity to perturbations in the Hamiltonian [147].
In a series of works [148, 149], Schonfeld has explored cloud chambers, Geiger coun­
ters, and Stern-Gerlach experiments for empirical tests of quantum measurement,
including possible deviations from the Born rule in detecting rare events. He challenges
the conventional view that measurement is an axiomatic feature of quantum mechanics,
proposing that measurement emerges phenomenologically from collective interactions
in quantum detection systems. He analyzed the detailed microstructure of real measure­
ment systems, using classical idealizations selectively where it seems mathematically or
intuitively reasonable.
Oppenheim’s Postquantum Theory provides another perspective for the classicalquantum duality [100], treating gravity as a classical entity interacting dynamically
with quantum systems, causing wave function collapse (see Section 5.3.2 for a detailed
discussion).
5.6.2. Mind-inducing collapse
A historically relevant but discredited hypothesis is that consciousness causes collapse.
Wigner advocated for it until he learned about Zeh’s work on what would come to be
known as decoherence [150]. We mainly mention this mind-matter duality here to dis­
entangle a few ideas that are sometimes mixed up.
First, there is the actual proposal that consciousness causes the collapse, which presup­
poses a matter-mind duality. The discomfort this hypothesis raises in our physical under­
standing of the world has never been better embodied than in Bell’s quip [151], ‘Was the
wave function of the world waiting to jump for thousands of millions of years until a

PHILOSOPHICAL MAGAZINE

27

single-celled living creature appeared? Or did it have to wait a little longer, for some
better qualified system … with a PhD?’
Then, there is an epistemic proposal where the mind does not objectively cause the
collapse. Instead, the apparent collapse is an illusion arising when the observer
becomes aware of the measurement outcome. We find such a perspective in London
and Bauer [80, p. 251] who, in 1939, attributed the essential role played by consciousness
to be ‘the increase of knowledge, acquired by the observation’.
Finally, Hameroff and Penrose [152] put forward precisely the opposite hypothesis:
collapse causes consciousness. (And quantum coherences in the microtubules mentioned
in Section 4 would be part of this process.) They argue that if consciousness cannot be
reduced to an algorithmic process, then its physical origin must be in the stochastic
nature of the wave function collapse, which, for Penrose, is an objective event, as dis­
cussed in Section 5.3.
5.7. Measurement in quantum field theory
Quantum field theory (QFT) poses specific challenges to the Measurement Problem that
are more daunting than in standard, non-relativistic quantum mechanics [153]. Because
QFT integrates quantum mechanics and special relativity, locality is a built-in concept.
This differs entirely from non-relativistic quantum mechanics, where locality is an
add-on assumption, like when Bell imposed it in deriving his theorem. Sorkin showed
that applying standard collapse rules to QFT can lead to superluminal information trans­
fer in scenarios he termed impossible measurements [154]. More recently, this issue has
been reframed as a violation of the broader no-signalling principle, which prohibits com­
munication without a physical carrier [155].
Figure 8 illustrates a version of Sorkin’s impossible measurement using our NH3 qubit.
Alice, Bob, and Charlie are ready to perform measurements on a molecule-field coupled
system at times tA (Alice), tB (Bob), and tC (Charlie). They are spaced to allow causal
effects between Bob and Alice and between Charlie and Bob, but not between Alice and
Charlie. In the relativity lingo, Alice and Charlie are spacelike separated.
Alice prepares a molecule in a |down〉 state and can choose whether to flip it to |up〉 at
time tA or not. The molecule is coupled to an electromagnetic field. The field state is | fu 〉

Figure 8. Impossible measurement in QFT adapted from Ref. [154] Charlie, at time tC , cannot know if
Alice flipped the molecule at tA or not. Could an instantaneous collapse of the electromagnetic field’s
state in Bob’s measurement at tB enable superluminal information transfer between Alice and Charlie?.

28

A. A. TOMAZ ET AL.

if the molecule is |up〉 and | fd 〉 if the molecule is |down〉. The field is initially | fd 〉 and,
after tA , it is updated according
√�� to Alice’s choice. At tB , Bob measures the field projected
on (|up〉| fu 〉 + |down〉| fd 〉)/ 2. Charlie, who, at time tC , has no direct information about
Alice’s choice, attempts to indirectly discover that by measuring the field at tC , which was
updated after Bob’s intervention. Sorkin argues that, in principle, Charlie’s measure­
ments on the field could reveal Alice’s choice, implying superluminal exchange. There­
fore, avoiding such impossible measurements would require nontrivial constraints on
which observables are consistent with causality.
Such imprecision in the description of the measurement in QFT has been character­
ised, with a flair to the dramatic, as ‘a major scandal in the foundations of quantum
physics’ [156]. Recently, Bostelmann, Fewster, and Ruep proposed that the situation is
naturally solved within algebraic QFT as long as probes and couplings are constrained
to be local [153, 157, 158].
This approach, originally developed as a general framework for describing measure­
ment in algebraic QFT, was not tailored to solve the Sorkin problem, but rather aims
to identify and localise induced system observables and to characterise state updates.
The application to the Sorkin scenario, as presented in [158], thus constitutes a nontrivial
test of the framework. Their analysis is valid for general fields and spacetime geometries,
making it a promising step toward a rigorous measurement theory in QFT.
A complementary approach is proposed by Polo-Gómez, Garay, and Martín-Martí­
nez, who develop a measurement theory for QFT based on spatially smeared particle
detector models – such as the Unruh-DeWitt detector – that interact locally and cov­
ariantly with quantum fields [159]. Their framework, applicable to general fields and
spacetime geometries, avoids problems such as Sorkin’s impossible measurements
and allows localised interactions without invoking instantaneous collapse. While Bos­
telmann et al. pursue a mathematically rigorous algebraic route, Polo-Gómez et al.
adopt a more operational strategy grounded in how detectors realistically interact
with quantum fields.
Other proposals inspired by quantum field theory and signal analysis take a different
route, using mathematical tools to reinterpret collapse as a statistical construction. For
instance, Morgan proposed a framework based on classical random fields and oper­
ator-algebraic methods to model quantum phenomena, offering an alternative strategy
that remains within a classical probabilistic setting [160]. In his work, these fields –
equipped with nontrivial correlation structures – are used to reproduce quantum stat­
istics and construct joint probabilities even for noncommuting observables. His emphasis
lies not on deriving definite outcomes from quantum theory, but on modelling the
empirical structure of datasets generated by repeated measurements. This approach
aims to preserve locality and realism, challenging standard assumptions about the neces­
sity of wave function collapse or quantization itself.

6. The ontological status of the wave function
One fundamental question underlying the Measurement Problem is whether the wave
function represents an actual physical object (Ψ-ontic) or is merely a mathematical
tool encoding information (Ψ-epistemic) [161]. The Many-Worlds Interpretation
(Section 5.1), Objective Collapse Theories (Section 5.3), and Hidden-Variable Theories

PHILOSOPHICAL MAGAZINE

29

(Section 5.4) align with the Ψ-ontic view, while epistemic interpretations (Section 5.2)
are, by definition, Ψ-epistemic.
A common argument for the Ψ-epistemic view is that the wave function evolves in an
abstract, high-dimensional configuration space, making it unlikely to correspond to any­
thing physically real [161]. However, such a criticism does not intimidate Ψ-ontic pro­
ponents, who argue that the wave function describes something fundamental about
reality, even if not in three-dimensional space [162, 163]. Wave function realism, for
example, holds that the wave function is a physical field existing in a high-dimensional
configuration space [164]. Carroll and Singh take this high-dimensional Ψ-ontic stand to
the extreme [52]. In an interpretation they call Mad-Dog Everettianism, they propose that
the only fundamental elements of reality are the Hilbert space, state vectors, and hamilto­
nians. Everything else – including space, time, and classical variables – emerges from these.
Other Ψ-ontic interpretations have been developed to avoid the conceptual challenges
of high-dimensional spaces. One approach is the multi-field interpretation, which states
that an N-body wave function is a multi-field that assigns properties to sets of N points in
the 3D space [165]. This is the view one of us adopted in an essay discussing the nature of
the molecular wave function [166]. Gao [167] proposed an alternative Ψ-ontic interpret­
ation in the 3D space that does not require multi-fields. In his view, the wave function
represents a random discontinuous motion (RDM) of particles in real space. The wave
function phase encodes momentum flow, giving it a concrete physical meaning. More­
over, RDM makes testable predictions, suggesting that collapse is an emergent effect of
underlying stochastic motion rather than a fundamental postulate. Whether this
model extends to relativistic quantum field theory remains an open question.
Spacetime state realism reinterprets quantum mechanics by assigning quantum states
to regions of spacetime rather than treating the wave function as an object in a highdimensional space [168]. This approach aligns more naturally with quantum field
theory, which assigns quantum states to localised spacetime regions. A similar shift in
emphasis to local quantities occurs in Density Functional Theory (DFT) [169], which,
rather than working with the entire many-body wave function, pragmatically describes
fermionic systems in terms of their density – a function of three spatial coordinates.
A different approach comes from the Nomological Interpretation, which suggests that
the wave function is not a physical object but a law of nature governing quantum behav­
iour [162]. This is a common stance in interpreting Bohmian Mechanics [119, 170].
The Berry phase, which may arise during the cyclic evolution of quantum systems
[171, 172], is a mathematical feature of the wave function that can be explored to
assess its ontological status. Such a phase can build, for instance, when the nuclear geo­
metry of a molecule evolves along a closed path encircling a conical intersection. (A
conical intersection is a molecular geometry at which two adiabatic electronic states
degenerate, forming a conical topology of the potential energy surfaces in nuclear coor­
dinate space [173].) Unlike dynamic phases, the Berry phase is tied to the wave function’s
geometric properties and may, in principle, manifest in observable interference effects.
Valahu et al. [174] claimed to have observed such geometric-phase interference in a
trapped-ion quantum simulator mimicking conical intersection dynamics, which
would strongly support the Ψ-ontic interpretation. However, it is unclear whether
such effects could be observed in actual molecules since their experiment could be con­
sidered more of a controlled simulation than a molecular measurement. Moreover, Min

30

A. A. TOMAZ ET AL.

et al. [175] and, more recently, Ibele et al. [176] have provided strong theoretical evidence
that the Berry phase originates from the Born-Oppenheimer approximation and disap­
pears in an exact electron-nuclear treatment, suggesting it may be an artefact rather than
a fundamental quantum property.
Although the wave function’s ontological nature remains unsettled, some recent exper­
iments may support wave function realism. In particular, Costello et al. [177] reconstructed
Bloch wave functions in GaAs semiconductors using angle-resolved photoemission data,
showing that wave functions can, in some contexts, be experimentally accessed rather
than only inferred. However, such reconstructions apply to quasiparticles and rely on a
specific preparation context, and do not settle the deeper question of whether the wave
function represents an element of reality. As Rovelli has emphasised [76], a wave function
may encode the full information needed to predict measurement outcomes relative to a
given observer, without implying a universally ontic status.

7. Through the forest of quantum foundations
It is easy to get lost in the Measurement Problem. The gargantuan amount of literature,
the innumerable distinct theories, the endless debates, and the entanglement between
physics, philosophy, and formal logic all lend anyone stepping into this field a feeling
analogous to being trapped in a dense tropical forest. This review aims to offer an
updated global map, which, although it cannot pinpoint the escape route, as it simply
doesn’t exist, will at least help us steer clear of dangerous cliffs.
Here, we provide a general overview of possible solutions to the Measurement Problem,
which remains an actively discussed topic among physicists and philosophers, as well as of
newly proposed theories that we consider particularly promising or disruptive. They fall into
five classes of explanations: Many-Worlds Interpretations, Epistemic Interpretations, Objec­
tive Collapse Theories, Hidden-Variable Theories, and Dualistic Collapse Hypotheses.
Today, the Measurement Problem is much less puzzling than it once was. Thanks to
the decoherence program, we understand how quantum interferences are suppressed and
how the environment selects the outcome basis. Nevertheless, we still lack a fundamental
explanation for why only a single outcome is observed in experiments, and we are still
taking the first steps toward a well-defined measurement theory in quantum field
theory. Indeed, given that QFT is likely the most successful physical theory ever devel­
oped, any satisfactory solution for the Measurement Problem must also be an acceptable
solution for measurement in QFT. Therefore, it is worrisome to note that researchers on
the Measurement Problem do not usually deal with QFT (and vice versa).
Most scientists who use quantum mechanics in their daily work focus on its practical
applications rather than its interpretation. Indeed, it makes no difference whether we inter­
pret the result of an experiment as the quantum state collapsing into a single branch or experi­
encing a branch that cuts off communication with all others. Such a subtle distinction belongs
to defining a preferred worldview. It is even less consequential than choosing between New­
tonian and Hamiltonian formulations of classical mechanics, which at least differ in their
practical use. The exception concerns objective collapse theories, which propose new
physics beyond conventional quantum mechanics. In any case, it makes sense to keep chal­
lenging all interpretations and theories to prune the weak and reach complete consistency on
the remaining, even if we never get a single consensual description of quantum mechanics.

PHILOSOPHICAL MAGAZINE

31

Acknowledgments
The authors gratefully acknowledge Stephen Adler, Jacob Barandes, Matteo Carlesso, John deBrota,
Lajos Diósi, Christopher Fewster, Nicolas Gisin, Peter Morgan, Tzula Propp, Michael Ridley, Roldão
da Rocha, Carlo Rovelli, Jonathan Schonfeld, Barbara Šoda, Niklas Sülzner, and Mark van der Pals
for their careful reading of the first version of the manuscript and for their thoughtful and precise
comments, which encouraged us and helped improve this challenging work.

Disclosure statement
No potential conflict of interest was reported by the author(s).

Funding
This work received support from the French government under the France 2030 investment plan
as part of the Initiative d’Excellence d’Aix-Marseille Université (A*MIDEX AMX-22-REAB-173
and AMX-22-IN1-48) and from the European Research Council (ERC) Advanced Grant
SubNano (grant agreement 832237).

References
[1] A.A. Tomaz, R.S. Mattos, and M. Barbatti, Gravitationally-induced wave function collapse
time for molecules, Phys. Chem. Chem. Phys. 26 (2024), pp. 20785–20798.
[2] J.R. Hance and S. Hossenfelder, What does it take to solve the measurement problem?. J.
Phys. Commun. 6 (2022), pp. 1–12.
[3] F.A. Muller, Six measurement problems of quantum mechanics, in Non-Reflexive Logics,
Non-Individuals, and the Philosophy of Quantum Mechanics: Essays in Honour of the
Philosophy of Décio Krause, J.R.B. Arenhart and R.W. Arroyo, eds., Springer
International Publishing, Cham, 2023, pp. 225–259.
[4] O. Freire Junior, From the interpretation of quantum mechanics to quantum technologies, in
Oxford Research Encyclopedias, Physics, 2024.
[5] A. Bassi, M. Dorato, and H. Ulbricht, Collapse models: A theoretical, experimental and phi­
losophical review. Entropy 25 (2023), p. 645.
[6] M. Carlesso, S. Donadi, L. Ferialdi, M. Paternostro, H. Ulbricht, and A. Bassi, Present status and
future challenges of non-interferometric tests of collapse models, Nat. Phys. 18 (2022), pp. 243–250.
[7] S. Donadi and A. Bassi, Seven nonstandard models coupling quantum matter and gravity.
AVS Quantum Sci. 4, 025601 (2022), pp. 1–15.
[8] A. Bassi, K. Lochan, S. Satin, T.P. Singh, and H. Ulbricht, Models of wave-function collapse,
underlying theories, and experimental tests, Rev. Mod. Phys. 85 (2013), pp. 471–527.
[9] A. Bassi and G. Ghirardi, Dynamical reduction models, Phys. Rep. 379 (2003), pp. 257–426.
[10] B. Keimer and J.E. Moore, The physics of quantum materials, Nat. Phys. 13 (2017), pp.
1045–1055.
[11] F. Campaioli, S. Gherardini, J.Q. Quach, M. Polini, and G.M. Andolina, Colloquium:
quantum batteries. Rev. Mod. Phys. 96, 031001 (2024), pp. 1–36.
[12] M.C. Biswas, M.T. Islam, P.K. Nandy, and M.M. Hossain, Graphene quantum dots (GQDs) for
bioimaging and drug delivery applications: A review, ACS Mater. Lett. 3 (2021), pp. 889–911.
[13] D. Zigmantas, T. Polívka, P. Persson, and V. Sundström, Ultrafast laser spectroscopy
uncovers mechanisms of light energy conversion in photosynthesis and sustainable energy
materials. Chem. Phys. Rev. 3, 041303 (2022), pp. 1–106.
[14] D. Claudino, The basics of quantum computing for chemists. Int. J. Quantum Chem. 122
(2022), p. e26990.
[15] S. McArdle, S. Endo, A. Aspuru-Guzik, S.C. Benjamin, and X. Yuan, Quantum compu­
tational chemistry, Rev. Mod. Phys. 92 (2020), p.015003.

32

A. A. TOMAZ ET AL.

[16] J.D. Schultz, J.L. Yuly, E.A. Arsenault, K. Parker, S.N. Chowdhury, R. Dani, S. Kundu, H.
Nuomin, Z. Zhang, J. Valdiviezo, P. Zhang, K. Orcutt, S.J. Jang, G.R. Fleming, N. Makri,
J.P. Ogilvie, M.J. Therien, M.R. Wasielewski, and D.N. Beratan, Coherence in chemistry:
foundations and frontiers, Chem. Rev. 124 (2024), pp. 11641–11766.
[17] G.D. Scholes, A. Olaya-Castro, S. Mukamel, A. Kirrander, K.K. Ni, G.J. Hedley, and N.L.
Frank, The quantum information science challenge for chemistry, J. Phys. Chem. Lett. 16
(2025), pp. 1376–1396.
[18] C. Cohen-Tannoudji, B. Diu, and F. Laloe, Quantum Mechanics, Vol. 1, Wiley-VCH, New
York, USA, 2020.
[19] J.J. Sakurai, Modern Quantum Mechanics, Addison-Wesley, Massachusetts, 1994.
[20] D. Manzano, A short introduction to the lindblad master equation. AIP Adv. 10 (2020), pp.
025106-1– 025106-15.
[21] W. Wu and G.D. Scholes, Foundations of quantum information for physical chemistry, J.
Phys. Chem. Lett. 15 (2024), pp. 4056–4069.
[22] R.P. Feynman, R. Leighton, and M. Sands, The Feynman Lectures on Physics, new millen­
nium edition ed., Vol. III, Basic Books, USA, 2011. Available at https://www.
feynmanlectures.caltech.edu/.
[23] N. Ignatova, V.V. Cruz, R.C. Couto, E. Ertan, A. Zimin, F.F. Guimarães, S. Polyutov, H.
Ågren, V. Kimberg, M. Odelius, and F. Gel’mukhanov, Gradual collapse of nuclear wave
functions regulated by frequency tuned x-ray scattering. Sci. Rep. 7: 43891 (2017), pp. 1–12.
[24] F. Laudisa, The information-theoretic view of quantum mechanics and the measurement pro­
blem(s), Eur. J. Phil. Sci. 13 (2023), pp. 1–26.
[25] T. Maudlin, Three measurement problems, Topoi 14 (1995), pp. 7–15.
[26] M. Schlosshauer, Decoherence and the Quantum-to-Classical Transition, Springer-Verlag,
Heidelberg, 2007.
[27] W.H. Zurek, Pointer basis of quantum apparatus: into what mixture does the wave packet
collapse? Phys. Rev. D 24 (1981), pp. 1516–1525.
[28] A. Tonomura, J. Endo, T. Matsuda, T. Kawasaki, and H. Ezawa, Demonstration of singleelectron buildup of an interference pattern, Am. J. Phys. 57 (1989), pp. 117–120.
[29] M. Barbatti, A.B. Rocha, and C.E. Bielschowsky, Young-type interference pattern in molecu­
lar inner-shell excitations by electron impact. Phys. Rev. A 72, 032711 (2005), pp. 032711-1–
032711-6.
[30] C. Kanitz, J. Bühler, V. Zobač, J.J. Robinson, T. Susi, M. Debiossac, and C. Brand,
Diffraction of helium and hydrogen atoms through single-layer graphene. Science 389
(2025), pp. 724–726. https://doi.org/doi:10.1126/science.adx5679.
[31] Y.Y. Fein, P. Geyer, P. Zwick, F. Kiałka, S. Pedalino, M. Mayor, S. Gerlich, and M. Arndt,
Quantum superposition of molecules beyond 25 kda, Nat. Phys. 15 (2019), pp. 1242–1245.
[32] P. Ball, Quantum common sense, Aeon Magazine (2017), Available at https://aeon.co/
essays/the-quantum-view-of-reality-might-not-be-so-weird-after-all.
[33] E. Joos and H.D. Zeh, The emergence of classical properties through interaction with the
environment, Z. Phys. B: Conden. Matter 59 (1985), pp. 223–243.
[34] B. Kaufman, P. Marquetand, T. Rozgonyi, and T. Weinacht, Long-lived electronic coherences
in molecules, Phys. Rev. Lett. 131 (2023), p. 263202.
[35] N.S. Babcock, G. Montes-Cabrera, K.E. Oberhofer, M. Chergui, G.L. Celardo, and P.
Kurian, Ultraviolet superradiance from mega-networks of tryptophan in biological architec­
tures, J. Phys. Chem. B 128 (2024), pp. 4035–4046.
[36] M. Gross and S. Haroche, Superradiance: an essay on the theory of collective spontaneous
emission, Phys. Rep. 93 (1982), pp. 301–396.
[37] A. Ajdarzadeh, C. Consani, O. Bräm, A. Tortschanoff, A. Cannizzo, and M. Chergui,
Ultraviolet transient absorption, transient grating and photon echo studies of aqueous trypto­
phan, Chem. Phys. 422 (2013), pp. 47–52.
[38] Y. Shu and D.G. Truhlar, Decoherence and its role in electronically nonadiabatic dynamics, J.
Chem. Theory Comput. 19 (2023), pp. 380–395.

PHILOSOPHICAL MAGAZINE

33

[39] J.P. Paz and W.H. Zurek, Quantum limit of decoherence: environment induced superselection
of energy eigenstates, Phys. Rev. Lett. 82 (1999), pp. 5181–5185.
[40] A. Adil, M.S. Rudolph, A. Arrasmith, Z. Holmes, A. Albrecht, and A. Sornborger, A search
for classical subsystems in quantum worlds, preprint (2024). Available at arXiv:2403.10895
[quant-ph].
[41] W.H. Zurek, Quantum darwinism, Nat. Phys. 5 (2009), pp. 181–188.
[42] W.H. Zurek, Emergence of the classical world from within our quantum universe, in From
Quantum to Classical: Essays in Honour of H.-Dieter Zeh, C. Kiefer, ed., Springer
International Publishing, Cham, 2022, pp. 23–44.
[43] K. Landsman, Foundations of Quantum Theory: From Classical Concepts to Operator
Algebras, Springer Cham, Netherlands, 2017.
[44] R.E. Kastner, ‘Einselection’ of pointer observables: the new H-theorem? Stud. History Phil.
Sci. Part B: Stud. History Phil. Mod. Phys. 48 (2014), pp. 56–58.
[45] G.A. Worth, Quantics: A general purpose package for quantum molecular dynamics simu­
lations, Comput. Phys. Commun. 248 (2020), p. 107040.
[46] H.D. Zeh, There are no quantum jumps, nor are there particles!, Phys. Lett. A 172 (1993), pp.
189–192.
[47] B. d’Espagnat, Veiled Reality – An Analysis of Present-Day Quantum Mechanical Concepts,
Westview Press, USA, 2003.
[48] D.Z. Albert, A Guess at the Riddle: Essays on the Physical Underpinnings of Quantum
Mechanics, Harvard University Press, 2023.
[49] D. Wallace, The Emergent Multiverse: Quantum Theory According to the Everett
Interpretation, Oxford University Press, Oxford, UK, 2012.
[50] W.H. Zurek, Probabilities from entanglement, born’s rule from envariance, Phys. Rev. A 71
(2005), p. 052105.
[51] S.M. Carroll and J. Lodman, Energy non-conservation in quantum mechanics. Found. Phys.
51, 83 (2021), pp. 1–11.
[52] S.M. Carroll and A. Singh, Mad-dog everettianism: quantum mechanics at its most minimal,
in What is Fundamental?, A. Aguirre, B. Foster, and Z. Merali, eds., Springer International
Publishing, Cham, 2019, pp. 95–104.
[53] S. Aaronson, Y. Atia, and L. Susskind, On the hardness of detecting macroscopic superposi­
tions, Preprint (2020). Available at arXiv:2009.07450 [quant-ph].
[54] L. Susskind, Computational complexity and black hole horizons. Fortschritte der Physik 64
(2016), pp. 24–43.
[55] S.M. Carroll and C.T. Sebens, Many worlds, the born rule, and self-locating uncertainty, in
Quantum Theory: A Two-Time Success Story, Springer, Milan, 2014, pp. 157–169.
[56] A. Kent, Does it make sense to speak of self-Locating uncertainty in the universal wave func­
tion? remarks on sebens and carroll, Found. Phys. 45 (2015), pp. 211–217.
[57] A.J. Short, Probability in many-worlds theories. Quantum 7, 971 (2023), pp. 1–10.
[58] M. Tegmark, Our Mathematical Universe: My Quest for the Ultimate Nature of Reality,
Alfred A. Knopf, New York, 2014.
[59] H.D. Zeh, On the interpretation of measurement in quantum theory, Found. Phys. 1 (1970),
pp. 69–76.
[60] P. Byrne, Searching for dieter zeh, in From Quantum to Classical: Essays in Honour of H.Dieter Zeh, C. Kiefer, ed., Springer International Publishing, Cham, 2022, pp. 289–305.
[61] R. Penrose, Fashion, Faith, and Fantasy in the New Physics of the Universe, Princeton
University Press, USA, 2016.
[62] C. Robson, Relational quantum mechanics and contextuality. Found. Phys. 54: 54 (2024),
pp. 1–22.
[63] C. Rovelli, Relational quantum mechanics, Int. J. Theor. Phys. 35 (1996), pp. 1637–1678.
[64] C. Rovelli, Space is blue and birds fly through it, Phil. Trans. R. Soc. A: Math. Phys. Eng. Sci.
376 (2018), p. 20170312.

34

A. A. TOMAZ ET AL.

[65] V. Brukner and A. Zeilinger, Information and fundamental elements of the structure of
quantum theory, in Time, Quantum and Information, L. Castell and O. Ischebeck, eds.,
Springer Berlin Heidelberg, Berlin, Heidelberg, 2003, pp. 323–354.
[66] C.A. Fuchs, N.D. Mermin, and R. Schack, An introduction to QBism with an application to
the locality of quantum mechanics, Am. J. Phys. 82 (2014), pp. 749–754.
[67] J.A. Barandes, The stochastic-quantum theorem, preprint (2023). Available at
arXiv:2309.03085 [quant-ph].
[68] F. Giacomini, E. Castro-Ruiz, and V. Brukner, Quantum mechanics and the covariance of
physical laws in quantum reference frames. Nat. Commun. 10: 494 (2019), pp. 1–13.
[69] A. Vanrietvelde, P.A. Hoehn, F. Giacomini, and E. Castro-Ruiz, A change of perspective:
switching quantum reference frames via a perspective-neutral framework. Quantum 4, 225
(2020), pp. 1–35.
[70] F. Giacomini and V. Brukner, Quantum superposition of spacetimes obeys einstein’s equiv­
alence principle. AVS Quantum Sci. 4, 015601 (2022), pp. 1–9.
[71] D. Spegel-Lexne, S. Gómez, J. Argillander, M. Pawłowski, P.R. Dieguez, A. Alarcón, and
G.B. Xavier, Experimental demonstration of the equivalence of entropic uncertainty with
wave-particle duality, Sci. Adv. 10 (2024), p. eadr2007.
[72] A. Franck, Miding Matter, Aeon Magazine (2017).
[73] M.F. Pusey, J. Barrett, and T. Rudolph, On the reality of the quantum state, Nat. Phys. 8
(2012), pp. 475–478.
[74] M.S. Leifer, Can the quantum state be interpreted statistically?, https://mattleifer.info/2011/
11/20/can-the-quantum-state-be-interpreted-statistically/ (2011). Accessed: 2025-04-18.
[75] M.S. Leifer, Is the quantum state real? An extended review of Ψ-ontology theorems, Quanta 3
(2014), pp. 67–155.
[76] C. Rovelli, Relational quantum mechanics, in The Stanford Encyclopedia of Philosophy, E.N.
Zalta and U. Nodelman, eds., Spring 2025 ed., Metaphysics Research Lab, Stanford
University, Stanford, USA, 2025.
[77] A. Khrennikov, Ozawa’s intersubjectivity theorem as objection to QBism individual agent
perspective. Int. J. Theor. Phys. 63, 23 (2024), pp. 1–9.
[78] A. Khrennikov, Relational quantum mechanics: Ozawa’s intersubjectivity theorem as justifi­
cation of the postulate on internally consistent descriptions. Found. Phys. 54: 29 (2024), pp.
1–12.
[79] R. Schack, When will two agents agree on a quantum measurement outcome? Intersubjective
agreement in QBism. International Journal of Theoretical Physics 63:254 (2024), pp. 1–9.
https://link.springer.com/article/10.1007/s10773-024-05790-w.
[80] F. London and E. Bauer, The theory of observation in quantum mechanics, in Quantum
Theory and Measurement, J.A. Wheeler and W.H. Zurek, eds., Princeton University
Press, USA, 1983, pp. 217–259.
[81] J.B. DeBrota, C.A. Fuchs, and R. Schack, Quantum dynamics happens only on paper:
Qbism’s account of decoherence, preprint (2024). Available at arXiv:2312.14112.
[82] J.A. Barandes, The stochastic-quantum correspondence. Philosophy of Physics 3 (2025), pp.
1–32. https://doi.org/10.31389/pop.186.
[83] S.L. Adler, Quantum theory as an emergent phenomenon: foundations and phenomenology.
J. Phys.: Conf. Ser. 361 (2012), pp. 1–8.
[84] G.C. Ghirardi, P. Pearle, and A. Rimini, Markov processes in hilbert space and continuous
spontaneous localization of systems of identical particles, Phys. Rev. A 42 (1990), pp. 78–89.
[85] L.E.F.F. Torres and S. Roche, A non-Hermitian loop for a quantum measurement. Journal of
Physics Communications 9 065001 (2025), pp. 1–9. https://doi.org/10.1088/2399-6528/
ade19b.
[86] S.L. Adler and A. Bassi, Collapse models with non-white noises, J. Phys. A: Math. Theor. 40
(2007), pp. 15083–15098.
[87] N. Gisin and I.C. Percival, The quantum-state diffusion model applied to open systems. J.
Phys. A: Math. Gen. 25 (1992), pp. 5677–5691.

PHILOSOPHICAL MAGAZINE

35

[88] N. Gisin, Stochastic quantum dynamics and relativity, Helv. Phys. Acta 62 (1989), pp.
363–371.
[89] R. Schack, T.A. Brun, and I.C. Percival, Quantum state diffusion, localization and compu­
tation, J. Phys. A: Math. Gen. 28 (1995), pp. 5401–5413.
[90] G.C. Ghirardi, A. Rimini, and T. Weber, Unified dynamics for microscopic and macroscopic
systems, Phys. Rev. D 34 (1986), pp. 470–491.
[91] L. Diósi, Models for universal reduction of macroscopic quantum fluctuations, Phys. Rev. A
40 (1989), pp. 1165–1174.
[92] R. Penrose, On Gravity’s role in quantum state reduction, Gen. Relativ. Gravit. 28 (1996), pp.
581–600.
[93] R. Howl, R. Penrose, and I. Fuentes, Exploring the unification of quantum theory and general
relativity with a Bose–Einstein condensate, New J. Phys. 21 (2019), p. 043047.
[94] S. Gao, Does gravity induce wavefunction collapse? An examination of penrose’s conjecture,
Stud. History Philos. Sci. Part B: Stud. History Philos. Mod. Phys. 44 (2013), pp. 148–151.
− of massive quantum superpo­
[95] L. Diósi, On the conjectured gravity-related collapse rate DE/h
sitions, AVS Quantum Sci. 4 (2022), p. 015605.
[96] L. Figurato, M. Dirindin, J. Luis Gaona-Reyes, M. Carlesso, A. Bassi, and S. Donadi, On the
effectiveness of the collapse in the Diósi–Penrose model, New J. Phys. 26 (2024), p. 113004.
[97] S. Donadi, K. Piscicchia, C. Curceanu, L. Diósi, M. Laubenstein, and A. Bassi, Underground
test of gravity-related wave function collapse, Nat. Phys. 17 (2021), pp. 74–78.
[98] I.J. Arnquist, F.T. Avignone, A.S. Barabash, C.J. Barton, K.H. Bhimani, E. Blalock, B. Bos,
M. Busch, M. Buuck, T.S. Caldwell, Y.D. Chan, C.D. Christofferson, P.H. Chu, M.L. Clark,
C. Cuesta, J.A. Detwiler, Y. Efremenko, H. Ejiri, S.R. Elliott, G.K. Giovanetti, M.P. Green, J.
Gruszko, I.S. Guinn, V.E. Guiseppe, C.R. Haufe, R. Henning, D. Hervas Aguilar, E.W.
Hoppe, A. Hostiuc, I. Kim, R.T. Kouzes, T.E. Lannen V, A. Li, A.M. Lopez, J.M. LópezCastaño, E.L. Martin, R.D. Martin, R. Massarczyk, S.J. Meijer, T.K. Oli, G. Othman, L.S.
Paudel, W. Pettus, A.W.P. Poon, D.C. Radford, A.L. Reine, K. Rielage, N.W. Ruof, D.
Tedeschi, R.L. Varner, S. Vasilyev, J.F. Wilkerson, C. Wiseman, W. Xu, C.H. Yu, and
B.X. Zhu, Search for spontaneous radiation from wave function collapse in the majorana
demonstrator, Phys. Rev. Lett. 129 (2022), p. 239902.
[99] K. Thorne, Black Holes & Time Warps: Einstein’s Outrageous Legacy (Commonwealth Fund
Book Program), WW Norton & Company, New York City, USA, 1995.
[100] J. Oppenheim, A postquantum theory of classical gravity? Phys. Rev. X13 (2023), p. 041040.
[101] J. Oppenheim, Is it time to rethink quantum gravity? Int. J. Mod. Phys. D 32 (2023), p.
2342024.
[102] S. Carlip, Is quantum gravity necessary? Classical Quantum Grav. 25 (2008), p. 154010.
[103] T.A. Brun, Continuous measurements, quantum trajectories, and decoherent histories, Phys.
Rev. A 61 (2000), p. 042107.
[104] J. Oppenheim, C. Sparaciari, B. Šoda, and Z. Weller-Davies, Objective trajectories in hybrid
classical-quantum dynamics. Quantum 7, 891 (2023), pp. 1–47.
[105] J. Oppenheim, C. Sparaciari, B. Šoda, and Z. Weller-Davies, Gravitationally induced deco­
herence vs space-time diffusion: testing the quantum nature of gravity. Nat. Commun. 14:
7910 (2023), pp. 1–24.
[106] R. Penrose, On the gravitization of quantum mechanics 1: quantum state reduction, Found.
Phys. 44 (2014), pp. 557–575.
[107] D.G.A. Altamura, A. Vinante, and M. Carlesso, Improved bounds on collapse models from
rotational noise of the laser interferometer space antenna pathfinder mission, Phys. Rev. A
111 (2025), pp. L020203.
[108] G. Gasbarri, A. Belenchia, M. Carlesso, S. Donadi, A. Bassi, R. Kaltenbaek, M. Paternostro, and
H. Ulbricht, Testing the foundation of quantum physics in space via interferometric and noninterferometric experiments with mesoscopic nanoparticles. Commun. Phys. 4, 155 (2021), pp.
1–13.

36

A. A. TOMAZ ET AL.

[109] O. Angeli, S. Donadi, G. Di Bartolomeo, J.L. Gaona-Reyes, A. Vinante, and A. Bassi,
Probing the quantum nature of gravity through classical diffusion, preprint (2025).
Available at arXiv:2501.13030.
[110] R. Dick, Back to bohr: quantum jumps in Schrödinger’s wave mechanics, Quantum Rep. 6
(2024), pp. 401–408.
[111] G. Ghirardi and R. Romano, Ontological models predictively inequivalent to quantum
theory, Phys. Rev. Lett. 110 (2013), p. 170404.
[112] J.S. Bell, Speakable and Unspeakable in Quantum Mechanics, 2nd ed., Cambridge University
Press, Cambridge, UK, 2004. Available at https://www.cambridge.org/9780521523387.
[113] N.D. Mermin, Hidden variables and the two theorems of john bell, Rev. Mod. Phys. 65
(1993), pp. 803–815.
[114] C. Held, The Kochen-Specker Theorem, The Stanford Encyclopedia of Philosophy (Fall 2022
Edition) (2022), Available at https://plato.stanford.edu/archives/fall2022/entries/kochenspecker/.
[115] S. Kochen and E.P. Specker, The problem of hidden variables in quantum mechanics, J.
Math. Mech. 17 (1967), pp. 59–87. Available at https://www.jstor.org/stable/24902153.
[116] D. Rauch, J. Handsteiner, A. Hochrainer, J. Gallicchio, A.S. Friedman, C. Leung, B. Liu, L.
Bulla, S. Ecker, F. Steinlechner, R. Ursin, B. Hu, D. Leon, C. Benn, A. Ghedina, M.
Cecconi, A.H. Guth, D.I. Kaiser, T. Scheidl, and A. Zeilinger, Cosmic bell test using
random measurement settings from high-redshift quasars. Phys. Rev. Lett. 121 (2018), pp.
080403-1–080403-9.
[117] D.H. Oaknin, Bypassing the Kochen–Specker theorem: an explicit non-Contextual statistical
model for the qutrit. Axioms 12, 90 (2023), pp. 1–11.
[118] K.W. Bong, A. Utreras-Alarcón, F. Ghafari, Y.C. Liang, N. Tischler, E.G. Cavalcanti, G.J.
Pryde, and H.M. Wiseman, A strong no-go theorem on the Wigner’s friend paradox, Nat.
Phys.16 (2020), pp. 1199–1205.
[119] D. Dürr and S. Teufel, Bohmian Mechanics, in Bohmian Mechanics: The Physics and
Mathematics of Quantum Theory, Springer Berlin Heidelberg, Berlin, Heidelberg, 2009,
pp. 145–171.
[120] S. Das, Detlef Dürr, arrival-time distributions, and spin in Bohmian mechanics: Personal
recollections and state-of-the-art, preprint (2023), Available at arXiv:2309.15815 [physics.h­
ist-ph].
[121] A. Valentini, Inflationary cosmology as a probe of primordial quantum mechanics, Phys. Rev.
D 82 (2010), p. 063513.
[122] V. Sharoglazova, M. Puplauskis, C. Mattschas, C. Toebes, and J. Klaers, Energy–speed
relationship of quantum particles challenges bohmian mechanics, Nature 643 (2025), pp.
67–72. Available at https://doi.org/10.1038/s41586-025-09099-4.
[123] B. Poirier, Bohmian mechanics without pilot waves, Chem. Phys. 370 (2010), pp. 4–14.
[124] B. Poirier and H.M. Tsai, Trajectory-based conservation laws for massive spin-zero relativis­
tic quantum particles in 1 + 1 spacetime, J. Phys.: Conf. Ser. 1612 (2020), p. 012022.
[125] E. Madelung, Quantentheorie in hydrodynamischer form, Z. Phys. 40 (1927), pp. 322–326.
[126] A. Messiah, Quantum Mechanics, Vol. I, North-Holland Publishing Company,
Netherlands, 1961.
[127] P. Holland, Computing the wavefunction from trajectories: particle and wave pictures in
quantum mechanics and their relation, Ann. Phys. 315 (2005), pp. 505–531.
[128] M.J.W. Hall, D.A. Deckert, and H.M. Wiseman, Quantum phenomena modeled by inter­
actions between many classical worlds, Phys. Rev. X 4 (2014), p. 041013.
[129] R. Crespo-Otero and M. Barbatti, Recent advances and perspectives on nonadiabatic mixed
quantum-Classical dynamics, Chem. Rev. 118 (2018), pp. 7026–7068.
[130] L.M. Ibele, E. Sangiogo Gil, E. Villaseco Arribas, and F. Agostini, Simulations of photoin­
duced processes with the exact factorisation: state of the art and perspectives. Phys. Chem.
Chem. Phys. 26 (2024), pp. 26693–26718.
[131] J.C. Tully, Mixed quantum-classical dynamics, Faraday Discuss. 110 (1998), pp. 407–419.

PHILOSOPHICAL MAGAZINE

37

[132] S. Hossenfelder and T. Palmer, Rethinking superdeterminism. Front. Phys. 8: 139 (2020), pp.
1–13.
[133] G. ’tHooft, The Cellular Automaton Interpretation of Quantum Mechanics, Springer,
Cham, 2016.
[134] S. Donadi and S. Hossenfelder, Toy model for local and deterministic wave-function collapse,
Phys. Rev. A 106 (2022), p. 022212.
[135] J. Handsteiner, A.S. Friedman, D. Rauch, J. Gallicchio, B. Liu, H. Hosp, J. Kofler, D. Bricher,
M. Fink, C. Leung, A. Mark, H.T. Nguyen, I. Sanders, F. Steinlechner, R. Ursin, S.
Wengerowsky, A.H. Guth, D.I. Kaiser, T. Scheidl, and A. Zeilinger, Cosmic bell test:
measurement settings from milky way stars, Phys. Rev. Lett. 118 (2017), p. 060401.
[136] Y. Aharonov, P.G. Bergmann, and J.L. Lebowitz, Time symmetry in the quantum process of
measurement, Phys. Rev. 134 (1964), pp. B1410–B1416.
[137] P. Pechukas, Time-dependent semiclassical scattering theory. II. Atomic collisions, Phys. Rev.
181 (1969), pp. 174–185.
[138] J.M. Toldo, R.S. Mattos, J. Pinheiro Max, S. Mukherjee, and M. Barbatti, Recommendations
for velocity adjustment in surface hopping, J. Chem. Theory Comput. 20 (2024), pp. 614–624.
[139] E. Adlam, Two roads to retrocausality. Synthese 200(5) (2022), pp. 422–444. https://doi.org/
10.1007/s11229-022-03919-0.
[140] R.I. Sutherland, Probabilities and certainties within a causally symmetric model. Found.
Phys. 52: 75 (2022), pp. 1–17.
[141] M. Ridley, Quantum probability from temporal structure, Quantum Rep. 5 (2023), pp. 496–509.
[142] M. Ridley and E. Adlam, Time and event symmetry in quantum mechanics. Quantum Stud.:
Math. Found. 12: 9 (2025), pp. 1–21.
[143] M.K. van der Pals, A note on a possible solution to the measurement problem, Int. J.
Quantum Found. 10 (2024), pp. 26–55. Available at https://ijqf.org/archives/7019.
[144] N. Gisin, Indeterminism in physics, classical Chaos and Bohmian mechanics: are real
numbers really real? Erkenntnis 86 (2021), pp. 1469–1481.
[145] G. Bacciagaluppi and E. Crull, Heisenberg (and Schrödinger, and Pauli) on hidden variables,
Stud. History Phil. Sci. Part B: Stud. History Phil. Mod. Phys. 40 (2009), pp. 374–382.
[146] D. Grimmer, The pragmatic QFT measurement problem and the need for a Heisenberg-like
cut in QFT. Synthese 202(4) (2023), pp. 1–45.
[147] N.P. Landsman, Spontaneous symmetry breaking in quantum systems: emergence or
reduction? Stud. History Philos. Sci. Part B: Stud. History Philos. Mod. Phys. 44 (2013),
pp. 379–394.
[148] J.F. Schonfeld, Measured distribution of cloud chamber tracks from radioactive decay: A new
empirical approach to investigating the quantum measurement problem, Open Phys. 20
(2022), pp. 40–48.
[149] J.F. Schonfeld, Does the Mott problem extend to Geiger counters?, Open Phys. 21 (2023), p.
20230125.
[150] J. Mehra and A. Wightman, The Collected Works of EP Wigner, vol. vi, p271 (1995).
[151] J. Bell, Against ‘measurement’, Phys. World 3 (1990), pp. 33–41.
[152] S. Hameroff and R. Penrose, Consciousness in the universe: A review of the ‘Orch OR’ theory,
Phys. Life Rev. 11 (2014), pp. 39–78.
[153] C.J. Fewster and R. Verch, Measurement in quantum field theory, perprint (2023). Available
at arXiv:2304.13356 [math-ph].
[154] R.D. Sorkin, Impossible measurements on quantum fields, preprint (1993). Available at
arXiv:gr-qc/9302018.
[155] N. Gisin and F. Del Santo, Towards a measurement theory in QFT: “impossible” quantum
measurements are possible but not ideal. Quantum 8, 1267 (2024), pp. 1–11.
[156] J. Earman and G. Valente, Relativistic causality in algebraic quantum field theory, Int. Stud.
Phil. Sci. 28 (2014), pp. 1–48.
[157] C.J. Fewster and R. Verch, Quantum fields and local measurements, Commun. Math. Phys.
378 (2020), pp. 851–889.

38

A. A. TOMAZ ET AL.

[158] H. Bostelmann, C.J. Fewster, and M.H. Ruep, Impossible measurements require impossible
apparatus, Phys. Rev. D 103 (2021), p. 025017.
[159] J. Polo-Gómez, L.J. Garay, and E. Martín-Martínez, A detector-based measurement theory
for quantum field theory, Phys. Rev. D 105 (2022), p. 065003.
[160] P. Morgan, The collapse of a quantum state as a joint probability construction*, J. Phys. A 55
(2022), p. 254006.
[161] M. Hubert, Is the statistical interpretation of quantum mechanics Ψ-ontic or Ψ-epistemic?.
Found. Phys. 53: 16 (2023), pp. 1–23.
[162] E.K. Chen, Realism about the wave function, Philos. Compass 14 (2019), p. e12611.
[163] A. Ney, Three arguments for wave function realism. Eur. J. Philos. Sci. 13: 50 (2023), pp. 1–
18.
[164] D.Z. Albert, Elementary quantum metaphysics, in Bohmian Mechanics and Quantum
Theory: An Appraisal, J.T. Cushing, A. Fine, and S. Goldstein, eds., Springer
Netherlands, Dordrecht, 1996, pp. 277–284.
[165] M. Hubert and D. Romano, The wave-function as a multi-field, Eur. J. Philos. Sci. 8 (2018),
pp. 521–537.
[166] M. Barbatti, We are not empty, Aeon Magazine (2023), Available at https://aeon.co/essays/
why-the-empty-atom-picture-misunderstands-quantum-theory.
[167] S. Gao, The Meaning of the Wave Function: In Search of the Ontology of Quantum
Mechanics, Cambridge University Press, Cambridge, UK, 2017.
[168] D. Wallace and C.G. Timpson, Quantum mechanics on spacetime I: spacetime state realism,
Br. J. Philos. Sci. 61 (2010), pp. 697–727.
[169] R.O. Jones, Density functional theory: its origins, rise to prominence, and future, Rev. Mod.
Phys. 87 (2015), pp. 897–923.
[170] S. Goldstein and S. Teufel, Quantum spacetime without observers: Ontological clarity and the
conceptual foundations of quantum gravity, in Physics Meets Philosophy at the Planck Scale:
Contemporary Theories in Quantum Gravity, C. Callender and N. Huggett, eds., Cambridge
University Press, Cambridge, UK, 2001, pp. 275–289.
[171] M.V. Berry, Quantal phase factors accompanying adiabatic changes, Proc. R. Soc. Lond. A.
Math. Phys. Sci. 392 (1984), pp. 45–57.
[172] D. Xiao, M.C. Chang, and Q. Niu, Berry phase effects on electronic properties, Rev. Mod.
Phys. 82 (2010), pp. 1959–2007.
[173] W. Domcke, D.R. Yarkony, and H. Köppel, Conical Intersections – Electronic Structure,
Dynamics and Spectroscopy, Advanced Series in Physical Chemistry, World Scientific,
Singapore, 2004.
[174] C.H. Valahu, V.C. Olaya-Agudelo, R.J. MacDonell, T. Navickas, A.D. Rao, M.J. Millican,
J.B. Pérez-Sánchez, J. Yuen-Zhou, M.J. Biercuk, C. Hempel, T.R. Tan, and I. Kassal,
Direct observation of geometric-phase interference in dynamics around a conical intersection,
Nat. Chem. 15 (2023), pp. 1503–1508.
[175] S.K. Min, A. Abedi, K.S. Kim, and E.K.U. Gross, Is the molecular Berry phase an artifact of
the Born-Oppenheimer approximation?. Phys. Rev. Lett. 113, 263004 (2014), pp. 2127–2143..
[176] L.M. Ibele, E. Sangiogo Gil, B.F.E. Curchod, and F. Agostini, On the nature of geometric and
topological phases in the presence of conical intersections, the Journal of Physical Chemistry
Letters¡/DIFdel¿J. Phys. Chem. Lett. 14 (2023), pp. 11625–11631.
[177] J.B. Costello, S.D. O’Hara, Q. Wu, D.C. Valovcin, L.N. Pfeiffer, K.W. West, and M.S.
Sherwin, Reconstruction of bloch wavefunctions of holes in a semiconductor, Nature 599
(2021), pp. 57–61.

