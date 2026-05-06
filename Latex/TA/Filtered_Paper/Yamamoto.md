RESEARCH ARTICLE
www.advquantumtech.com

Coherent Ising Machines with Optical Error Correction
Circuits
Sam Reifenstein, Satoshi Kako, Farad Khoyratee, Timothée Leleu,
and Yoshihisa Yamamoto*
is expected to scale exponentially. A representative example of an NP-hard combinatorial optimization problem is the
non-planar Ising model.[1] Special-purpose
quantum hardware devices have been
developed for ﬁnding The solutions of
Ising problems more eﬃciently than
standard heuristic approaches. For example, quantum annealing (QA) devices
exploit the adiabatic evolution of purestate vectors using a time-dependent
Hamiltonian.[2,3] Another example is the
coherent Ising machine (CIM), which exploits the quantum-to-classical transition of
mixed-state density operators in a quantum
oscillator network.[4–7] Performance comparisons between QA devices and CIMs
for various Ising models incorporating
complete, dense, or sparse graphs have
been reported.[8] Theoretical performance
comparisons between ideal gate-model
quantum computers that implement either
Grover’s search algorithm or the adiabatic quantum computing algorithm and
CIMs have also been reported recently.[9]
Although CIMs featuring all-to-all coupling among spins are
highly eﬀective, their use of external ﬁeld-programmable gate
array (FPGA) circuits, analog-to-digital converters (ADCs), and
digital-to-analog converters (DACs) not only results in considerable energy dissipation but also introduces potential bottlenecks
for high-speed operation.
The standard linear coupling scheme used by CIMs has been
found to suﬀer from amplitude heterogeneity among the constituent quantum oscillators. Consequently, the Ising Hamiltonian is incorrectly mapped to the network loss, resulting in unsuccessful operation, particularly in frustrated spin systems.[10] A
novel error-correcting feedback scheme developed to resolve this
problem[11,12] increases the solution accuracy of CIMs to a level
comparable to that of state-of-the-art heuristics such as break-out
local search (BLS). [14] In this paper, we introduce a novel CIM
architecture in which error correction is implemented optically.
In the proposed architecture, computationally intensive matrixvector multiplication (MVM) and a nonlinear feedback function
are implemented using phase-sensitive (degenerate) optical parametric ampliﬁers, which are essentially equivalent to main-cavity
optical parametric oscillators (OPOs). This new CIM architecture can potentially be implemented monolithically in future
photonic integrated circuits using thin-ﬁlm LiNbO3 platforms.
LiNbO3 platforms.[15]

A coherent Ising machine (CIM) comprising a network of open-dissipative
quantum oscillators with optical error correction circuits is proposed. In the
proposed network, the squeezed/anti-squeezed vacuum states of the
constituent optical parametric oscillators establish quantum correlations
below the threshold through optical mutual coupling and collective symmetry
breaking is induced above the threshold as a decision-making process. This
initial search process is followed by a chaotic solution search step facilitated
by optical error correction feedback. The particular algorithm used by the
proposed network is derived from the truncated Wigner stochastic diﬀerential
equation. As an optical hardware technology, the proposed CIM has several
unique features, including programmable all-to-all Ising coupling in the
optical domain, directional coupling (Jij ≠ Jji )-induced chaotic behavior, and
the ability to operate at low power at room temperature. The proposed CIM is
evaluated in terms of its performance and how this scales at diﬀerent problem
sizes. It is shown that the various CIMs discussed in this paper are eﬀective at
solving many problem types, although the optimal algorithm depends on the
problem case. It is further shown that the proposed optical implementations
can be achieved with low energy consumption on thin-ﬁlm LiNbO3 platforms.

1. Introduction
Combinatorial optimization problems are ubiquitous in modern
science, engineering, medicine, and business. As such problems
are often NP-hard, their runtime on classical digital computers

S. Reifenstein, S. Kako, F. Khoyratee, Y. Yamamoto
PHI (Physics & Informatics) Laboratories
NTT Research Inc.
940 Stewart Drive, Sunnyvale, CA 94085, USA
E-mail: yoshihisa.yamamoto@ntt-research.com
T. Leleu
International Research Center for Neurointelligence
The University of Tokyo
7-3-1 Hongo Bunkyo-ku, Tokyo 113-0033, Japan
The ORCID identiﬁcation number(s) for the author(s) of this article
can be found under https://doi.org/10.1002/qute.202100077
© 2021 The Authors. Advanced Quantum Technologies published by
Wiley-VCH GmbH. This is an open access article under the terms of the
Creative Commons Attribution-NonCommercial-NoDerivs License,
which permits use and distribution in any medium, provided the original
work is properly cited, the use is non-commercial and no modiﬁcations
or adaptations are made.

DOI: 10.1002/qute.202100077

Adv. Quantum Technol. 2021, 4, 2100077

2100077 (1 of 21)

© 2021 The Authors. Advanced Quantum Technologies published by Wiley-VCH GmbH

www.advquantumtech.com

Figure 1. a) Vacuum and squeezed vacuum states. b) Coherent and squeezed coherent states. c) Conventional CIM with vacuum noise injected from
reservoirs and a modiﬁed CIM with suppressed reservoir noise.

Because of their simple and eﬃcient theoretical descriptions,
networks of open dissipative quantum oscillators with optical error correction circuits are promising not only as future hardware
platforms but also as tools for implementing quantum-inspired
algorithms. Numerical simulation of the time evolution of an
N-qubit quantum system requires 2N complex-number amplitudes. However, various phase-space techniques in quantum optics have been developed over the last four decades to simulate
quantum oscillator networks.[18–20] The complete description of a
network of quantum oscillators is now possible using N (or 2N)
sets of stochastic diﬀerential equations (SDEs) based on positiveP,[21] truncated Wigner,[22–24] or truncated Husimi[23,24] representations of the master equations. These SDEs can be used as
heuristic algorithms on modern digital platforms. To completely
describe a network of low-Q quantum oscillators, a discrete map
technique using a Gaussian quantum model, which is also computationally eﬃcient, is available.[25]
Similarly, a network of dissipation-less quantum oscillators
with adiabatic Hamiltonian modulation that can be described
using a set of N deterministic equations can also be used to implement a heuristic algorithm on a modern digital platform.[27–29]
Such heuristic algorithms are called simulated bifurcation machines (SBMs),[27,29] and a variant SBM will be studied in
Section 6. Although the original SBM was inspired by
dissipation-less adiabatic quantum computation, the version
of SBM discussed in this paper (dSBM) is not a true unitary
system, as dissipation is artiﬁcially added using inelastic walls to
improve the performance of the algorithm. As both algorithms
involve MVM as a computational bottleneck when simulated on
a digital computer, we use the number of MVMs as the metric
for performance comparison. We ﬁnd that both types of systems

Adv. Quantum Technol. 2021, 4, 2100077

2100077 (2 of 21)

have very similar performance in most cases except on graph
types with signiﬁcant variation in vertex degree, where the SBM
struggles consistently.

2. Semi-Classical Model for Error Correction
Feedback
In this section, we will describe several mutual coupling and
error correction feedback schemes for CIMs. To simplify our
argument, we consider a semi-classical deterministic picture.[10]
The semi-classical model treated in this section is an approximate theory for the following ﬁctitious machine. At an initial
time t = 0, each signal pulse ﬁeld is prepared in a vacuum state
(Figure 1a) and each error pulse ﬁeld is prepared in a weak
coherent state (Figure 1b). When the pump ﬁelds p and pi are
switched on at t ≥ 0, a vacuum ﬁeld incident on the extraction
beam splitter BSe from an open port is squeezed/anti-squeezed
by a phase-sensitive ampliﬁer (PSA) in the optical delay line
(ODL) CIM, as shown in Figure 1c. In other words, the vacuum ﬂuctuation in the in-phase component X̃ = 12 (̂a + â † ) is
deampliﬁed by a factor of 1/G whereas the vacuum ﬂuctuation
in the quadrature-phase component P̂ = 2i1 (̂a − â † ) is ampliﬁed
by a factor of G. Similarly, the vacuum ﬂuctuations incident on
the OPO pulse ﬁeld arising from linear loss in the cavity are
all squeezed by the respective PSA. The pump and feedback
injection ﬁeld ﬂuctuations along the in-phase component are
also deampliﬁed by the respective PSA (Figure 1c).
The truncated Wigner stochastic diﬀerential equation (WSDE) for such a quantum-optic CIM with squeezed reservoirs
has been derived and studied previously.[31] This particular CIM
achieves maximum quantum correlation among OPO pulse

© 2021 The Authors. Advanced Quantum Technologies published by Wiley-VCH GmbH

25119044, 2021, 11, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/qute.202100077 by Nat Prov Indonesia, Wiley Online Library on [12/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

www.advancedsciencenews.com

www.advquantumtech.com

ﬁelds along the in-phase component and maximum success
probability[31] because, in such systems, the quantum correlation
among the OPO pulse ﬁelds is formed by the mutual coupling of
the vacuum ﬂuctuations of these ﬁelds without the injection of
uncorrelated fresh reservoir noise. The following semi-classical
model is considered as an approximate theory of the W-SDE
described above in the limit of a large deampliﬁcation factor
(G ≫ 1); a full quantum description of a more realistic CIM with
optical error correction circuits (without reservoir engineering)
is given in Section 5.
To overcome the problem of amplitude heterogeneity in the
CIM,[10] the addition of an auxiliary variable for error detection
and correction has been proposed.[11,12] This system has been
studied as a modiﬁcation of the measurement feedback CIM.[31]
The spin variable (signal pulse amplitude) xi and auxiliary variable (error pulse amplitude) ei obey the following deterministic
equations[11]
∑
dxi
𝜉Jij xj
= −xi3 + (p − 1)xi − ei
dt
j

(1)

)
(
dei
= −𝛽ei xi2 − 𝛼
dt

(2)

where Jij is the Ising coupling matrix, 𝛼, 𝛽, and p are system parameters, and 𝜉 is a normalizing constant for Jij (see Appendix A
for parameter selection). In many cases, these parameters can be
modulated over time to achieve better performance (see Section 3
and Appendix C). To use this system as an Ising solver, we consider the spin conﬁguration 𝜎i = sign(xi ) as a possible solution to
the corresponding Ising problem. Even though noise is ignored
in Equations (1) and (2), the initial amplitude xi can be chosen
randomly to create a diverse set of possible trajectories.
In this paper, we refer to this system of equations as CIM with
chaotic amplitude control (CIM-CAC). The term “chaotic” is used
because CIM-CAC exhibits chaotic behavior (as discussed in Section 3). CIM-CAC can refer to either the above-described system
of deterministic diﬀerential equations when integrated as a digital algorithm or an optical CIM that emulates the corresponding equations.
To study the CIM-CAC equations, we have made the following
modiﬁcations
∑
𝜉Jij xj
(3)
zi = ei
j

dxi
= −xi3 + (p − 1)xi − zi
dt

(4)

)
(
dei
= −𝛽ei z2i − 𝛼
dt

(5)

which we refer to as CIM with chaotic feedback control (CIMCFC). The only diﬀerence between Equations (2) and (5) is that,
in the latter, the time evolution of the error variable ei monitors
the feedback signal zi rather than the internal amplitude xi . The
dynamics of this new equation are very similar to those of CIMCAC, as highlighted by the observation that CIM-CAC and CIMCFC have nearly identical ﬁxed points. Our motivation for studying CIM-CFC in addition to CIM-CAC is to gain a better under-

Adv. Quantum Technol. 2021, 4, 2100077

2100077 (3 of 21)

standing of how these systems work. In addition, CIM-CFC can
have slightly simpler dynamics, which in turn simpliﬁes its numerical integration.
The third system discussed in this paper has a very diﬀerent
equation
∑
𝜉Jij xj
(6)
zi =
j

( )
(
)
dxi
= −xi3 + (p − 1)xi − f czi − k zi − ei
dt

(7)

)
(
dei
= −𝛽 ei − zi
dt

(8)

where the non-linear function f is a sigmoid-like function such
as f (z) = tanh(z) and p, k, c, and 𝛽 are system parameters (see Appendix A for parameter selection). The signiﬁcance of this new
feedback system is that the diﬀerential equation for the error signal ei is now linear in the “mutual coupling signal” zi . In addition,
∑
zi is calculated simply as j 𝜉Jij xj without the additional factor
ei used in Equation (6). This means that the only nonlinear elements in the system are the gain saturation term −xi3 and the
nonlinear function f . To obtain the results reported in this paper,
we used f (z) = tanh(z); however, if a diﬀerent function with the
same properties is used, the system will have similar behavior.
In the system described above, the two essential aspects of
CIM-CAC and CIM-CFC are separated into two diﬀerent terms.
The term f (czi ) produces mutual coupling while passively addressing the problem of amplitude heterogeneity; the term k(zi −
ei ) introduces the error signal ei , which helps to destabilize local
minima. Therefore, we refer to this system as CIM with separated
feedback control (CIM-SFC) in the remainder of this paper.
Another signiﬁcant aspect diﬀerentiating CIM-SFC (Equations (6)–(8)) from CIM-CAC and CIM-CFC (Equations (1)–(5))
is that the auxiliary variables ei in CIM-SFC have very diﬀerent meanings. In CIM-CAC and CIM-CFC, ei is meant to be a
strictly positive number that varies exponentially and modulates
the mutual coupling term. In CIM-SFC, by contrast, ei is a variable that stores sign information and takes the same range of values as the mutual coupling signal zi . The error signal ei and the
term k(ei − zi ) can essentially be regarded, respectively, as lowand high-pass ﬁlters on zi (in other words, k(ei − zi ) only registers sharp changes in zi ). The similarities and diﬀerences among
CIM-SFC, CIM-CAC, and CIM-CFC can be ascertained by observing the ﬁxed points. In CIM-CAC and CIM-CFC, the ﬁxed
points are of the form[11]
xi = 𝜆1 𝜎i
e i = 𝜆2

1
hi 𝜎i

(9)
(10)

with
hi =

∑

𝜉Jij 𝜎j

(11)

j

where 𝜎i is a spin conﬁguration corresponding to a local minimum of the Ising Hamiltonian and 𝜆1 and 𝜆2 are constants that
depend on the system parameters. In CIM-SFC, the ﬁxed points

© 2021 The Authors. Advanced Quantum Technologies published by Wiley-VCH GmbH

25119044, 2021, 11, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/qute.202100077 by Nat Prov Indonesia, Wiley Online Library on [12/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

www.advancedsciencenews.com

www.advquantumtech.com

Figure 2. Trajectories of OPO amplitudes in CIMs with a) linear feedback, b) nonlinear ﬁltering feedback, and c) chaotic feedback control.

are generally very complicated and diﬃcult to express explicitly.
However, if we consider the limit of c ≫ 1, the ﬁxed points will
take the form
xi = 𝜆𝜎i

(12)

ei = 𝜆hi

(13)

where 𝜆 is a number such that −𝜆3 + (p − 1)𝜆 = −1 and 𝜎i is
again a spin conﬁguration corresponding to a local minimum.
This formula is only valid if f (cz) is an odd function that takes
the value of +1 for cz ≫ 1 and −1 for cz ≪ −1. Therefore, it is
important to choose an appropriate function f .
The important diﬀerence between the ﬁxed points of these two
types of systems is that, in CIM-CAC and CIM-CFC, the error
signal is
|e i | ∝ 1
| | |h |
| i|

(14)

whereas in CIM-SFC, the error signal is
|ei | ∝ |hi |
| | | |

(15)

In Section 5, we will see that this diﬀerence makes CIMSFC more robust to quantum noise from reservoirs and pump
sources. In the next section, we will investigate the similarities
and diﬀerences among these three systems using numerical simulation.

3. Numerical Simulation of CIM-CAC, CIM-CFC,
and CIM-SFC
The originally proposed CIM architecture employs simple linear
feedback without an error detection/correction mechanism.
In other words, the feedback term in Equation (1) is simply
∑
[10]
In this case, the Ising Hamiltonian cannot be
j 𝜉Jij xj .
properly mapped to the network loss owing to OPO amplitude

Adv. Quantum Technol. 2021, 4, 2100077

2100077 (4 of 21)

heterogeneity, particularly in frustrated spin systems, as shown
in Figure 2a. Such a CIM often does not ﬁnd a ground state of the
Ising Hamiltonian; instead, it selects the lowest-energy eigenstate of the coupling (Jacobian) matrix [Jij ].[10] This undesired
operation is caused by a system’s formation of heterogeneous
amplitudes.[10] This problem can be partially addressed by intro∑
ducing a nonlinear ﬁlter function such as tanh( j 𝜉Jij xj ) for the
feedback pulse to achieve homogeneous OPO amplitudes—at
least well above threshold—as shown in Figure 2b and satisfy
the proper mapping condition toward the end of the system’s
trajectory. However, such nonlinear ﬁltering alone is not sufﬁciently powerful to prevent the machine from being trapped
in numerous local minima. As the problem size N increases,
NP-hard Ising problems are expected to have exponentially
increasing numbers of local minima; thus, a system that is easily
trapped in these minima will be ineﬀective.
To destabilize the attractors caused by local minima and allow
the machine to continue searching for a true ground state, the
error detection/correction variable expressed by Equation (2) or
(5) can be introduced. As shown in Figure 2c, the trajectory of
a CIM with error correction variables will not reach equilibrium
but continue to explore many states. Conversely, the systems in
Figure 2a,b, which do not have the error correction variable (ei ),
will often converge rapidly on a ﬁxed point corresponding to a
high-energy excited state of the Ising Hamiltonian. Destabilizing
the local minima will inevitably make the ground state unstable
as well. Although this is undesirable, the machine can be simply
allowed to visit many local minima and subsequently determine
which has the lowest energy. Alternatively, we have found that
modulating the system parameters can give the system a high
probability of staying in a ground state toward the end of its trajectory (see Section 4 for further details).
The addition of another N degrees of freedom allows the machine to visit a local minimum, escape from it, and continue to explore nearby states; this is not possible with a conventional CIM
algorithm. In this section, we will discuss the dynamics of the
error correction schemes, CIM-CFC and CIM-SFC, proposed in
this paper.

© 2021 The Authors. Advanced Quantum Technologies published by Wiley-VCH GmbH

25119044, 2021, 11, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/qute.202100077 by Nat Prov Indonesia, Wiley Online Library on [12/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

www.advancedsciencenews.com

www.advquantumtech.com

Figure 3. Mutual coupling ﬁeld (blue) and injection feedback ﬁeld (red) in four diﬀerent feedback systems.

Even though CIM-CFC and CIM-SFC are described by very
diﬀerent equations, the two systems are derived from a similar
concept. To understand why CIM-CFC and CIM-SFC are similar,
we can consider systems in which the “mutual coupling signal”
∑
Mi (t) = j 𝜉Jij xj (t) and the “injection feedback signal” Ii (t) are introduced. We can then write both CIM-CFC and CIM-SFC in the
form
∑
𝜉Jij xj (t)
(16)
Mi (t) =
j

dxi
= −xi3 + (p − 1)xi − Ii (t)
dt

(17)

where Ii (t) depends on the time evolution of Mi (t). Figure 3 shows
how Ii (t) (red) varies with respect to a mutual coupling ﬁeld Mi (t)
(blue) for four diﬀerent feedback schemes.
CIM-CFC and CIM-SFC share the following similarities under these conditions. If the mutual coupling ﬁeld Mi (t) remains
constant for a certain period of time, the injection feedback ﬁeld
Ii (t) will converge on the value given by sign(Mi (t)). If, however,
Mi (t) varies sharply, Ii (t) will deviate from its steady state values
+1∕ − 1. This small deviation is eﬀective at triggering destabilization when the system is near a local minimum, which allows the
machine to explore new spin conﬁgurations.
Although CIM-CFC and CIM-SFC are derived from the same
principle, the dynamics of the two systems appear to diﬀer from
each other. In particular, CIM-CFC (and CIM-CAC) nearly always features chaotic dynamics, as the trajectory is highly sensitive to the initial conditions. In the case of CIM-SFC, the trajectory will often immediately fall into a stable periodic orbit

Adv. Quantum Technol. 2021, 4, 2100077

2100077 (5 of 21)

unless the parameters are dynamically modulated. At present,
we do not have an exact theoretical reason for this diﬀerence
in dynamics; this is purely an experimental observation. A
more theoretical analysis of the case of CIM-CAC can be found
elsewhere.[11]
To demonstrate this diﬀerence, Figure 4 shows the correlation
of pulse amplitudes between two initial conditions that are very
close to each other. The initial condition for the pulse amplitude
#1 (plotted on the x-axis) is chosen from a zero-mean Gaussian
with a standard deviation of 0.25; the initial condition for trajectory #2 (plotted in y-axis) is equal to that of trajectory #1 plus a
small amount of noise (standard deviation 0.01).
Figure 4 shows the correlation of all 100 pulse amplitudes
between the two initial conditions for a Sherrington–Kirkpatrick
(SK) spin glass instance of problem size N = 100. In CIM-SFC
(ﬁrst row), the correlation remains even after 4000 time-steps
(round trips), indicating that the two initial conditions follow
a nearly identical trajectory. However, in CIM-CFC (second
row), the xi variables become uncorrelated after around 100
time-steps even though the initial conditions of the two trajectories are very close. This indicates qualitatively that CIM-CFC
is highly sensitive to the initial condition whereas CIM-SFC
is not.
This pattern tends to hold when diﬀerent parameters and initial conditions are used. However, although CIM-SFC stays correlated in most cases, the two trajectories diverge under certain system parameters and initial conditions. This means that, although
CIM-SFC is less sensitive to the initial conditions than CIM-CFC,
some chaotic dynamics likely occur during the search, especially
when the parameters are modulated.

© 2021 The Authors. Advanced Quantum Technologies published by Wiley-VCH GmbH

25119044, 2021, 11, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/qute.202100077 by Nat Prov Indonesia, Wiley Online Library on [12/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

www.advancedsciencenews.com

www.advquantumtech.com

Figure 4. Signal pulse amplitude correlations at diﬀerent evolution times in CIM-SFC and CIM-CFC.

Figure 5. Signal pulse amplitude trajectories of CIM-SFC and CIM-CFC with ﬁxed and modulated system parameters.

Another way to qualitatively observe the diﬀerence in dynamics is to simply observe the trajectories. Figure 5 shows examples of trajectories of both systems (10 out of 100 xi variables
are shown) with ﬁxed and linearly modulated system parameters.
When the parameters are ﬁxed, the diﬀerence between the two
systems is evident: CIM-SFC will rapidly become trapped in a stable periodic attractor, whereas CIM-CFC will continue to search
in an unpredictable manner, allowing the parameters to be slowly
modulated so that the system can ﬁnd a ground state. Although
CIM-CFC and CIM-CAC can ﬁnd ground states with ﬁxed param-

Adv. Quantum Technol. 2021, 4, 2100077

2100077 (6 of 21)

eters, we have found that modulation of the system parameters
improves the performance of both considerably (see Appendix C
for details).
In the lower left panel of Figure 5, the parameters c and p
of CIM-SFC increase linearly from low to high values (p ranges
from −1 to +1 and c ranges from 1 to 3). We see that, as the parameters change, the system can jump from one attractor to another and eventually end up in a ﬁxed point/local minimum. By
linearly increasing the parameters c and p in CIM-SFC from low
to high values, we slowly transition the nonlinear term tanh(czi )

© 2021 The Authors. Advanced Quantum Technologies published by Wiley-VCH GmbH

25119044, 2021, 11, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/qute.202100077 by Nat Prov Indonesia, Wiley Online Library on [12/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

www.advancedsciencenews.com

www.advquantumtech.com

from a “soft spin” mode in which the nonlinear coupling term
has a continuous range of values between −1 and 1 to a “discrete” mode in which tanh(czi ) primarily assumes the values +1
or −1. This transition appears to be crucial for CIM-SFC to function properly.
For most ﬁxed parameters, CIM-SFC rapidly approaches a periodic or ﬁxed-point attractor, as shown in Figure 5; however, as
mentioned earlier, it is likely that for some speciﬁc values of c and
p CIM-SFC will feature chaotic dynamics similar to those of CIMCFC. It has been shown[11,13] that chaotic dynamics are observed
when solving hard optimization problems eﬃciently using a deterministic system. This trend is also observed in the SBM.[27,29]
Whether or not CIM-SFC utilizes chaotic dynamics, however, is
beyond the scope of this paper; to answer this question, we would
need to further analyze how the parameters of CIM-SFC aﬀect
its dynamics and gain a deeper understanding of how CIM-SFC
ﬁnds ground states.

4. Implementation of CIM with Optical Error
Correction Circuits
Figure 6, together with 1c, show the physical setup of a CIM-CAC
or CIM-CFC system with optical error correction circuits. In our
design, the main ring cavity stores signal pulses with normalized
amplitude, xi , and error pulses with normalized amplitude, ei ,
where i = 1, 2, … , N. The signal pulses start from vacuum states
|0⟩1 |0⟩2 ⋯ |0⟩N and are ampliﬁed (or deampliﬁed) along the Xcoordinate by a positive (or negative) pump rate p.
The error pulses start from a coherent state |𝛼⟩1 |𝛼⟩2 ⋯ |𝛼⟩N
with 𝛼 > 0 and are ampliﬁed (or deampliﬁed) along the Xcoordinate by the pump rate p′ as described below. The squared
amplitudes of the error pulses are kept small (e2i < 1) relative
to the saturation level of the main cavity OPO; thus, the error pulses are controlled within a linear ampliﬁer/deampliﬁer
regime whereas the signal pulses are controlled within both a
linear ampliﬁer/deampliﬁer (xi2 < 1) and a nonlinear oscillator
regime (xi2 > 1).
The extraction beamsplitter BSe in Figure 1c selects partial
waves of the signal and error pulses that are ampliﬁed by the
noise-free phase-sensitive ampliﬁer PSA0 , as shown in Figure 6a). PSA0 ampliﬁes the signal and error pulses to a classical
level without introducing additional noise. Although the extracted amplitudes x̃i and ẽi suﬀer from signal-to-noise ratio
(SNR) degradation owing to the vacuum noise incident on BSe ,
they are ampliﬁed by the high-gain noise-free PSA0 to classical
levels; therefore, no further SNR degradation occurs despite the
large linear losses in the optical error correction circuits.
A small part of the output of PSA0 is sent to an optical homodyne detector that measures the extracted signal and error pulses,
which have amplitudes x̃i and ẽi , respectively. The measurement
error of the homodyne detection is determined solely by the reﬂectivity of BSe and the vacuum ﬂuctuation incident on BSe (as
described above). Figure 6a shows the output of the fan-out circuit at diﬀerent times t = 𝜏, 3𝜏, 5𝜏, … separated by signal-pulseto-signal-pulse intervals of 2𝜏.
For instance, the signal pulse (x̃j ) is ﬁrst input to PSAj and
then sent to optical delay line DLj with a delay time of (2N − 2j +
√
1)𝜏. The phase-sensitive gain/loss of PSAj is set to Gj = 𝜉Jij so

Adv. Quantum Technol. 2021, 4, 2100077

2100077 (7 of 21)

that the ampliﬁed/deampliﬁed signal pulse that arrives in front
of the fan-in circuit at time t = 2N𝜏 is equal to 𝜉Jij x̃j . Therefore,
the fan-in circuit will output a pulse with the desired amplitude of
∑
j 𝜉Jij x̃j . If PSAj has a phase-sensitive linear gain/loss of 10dB,
we can implement an arbitrary Ising coupling of range 10−2 <
|𝜉Jij | < 1.
The output of the fan-in circuit is√then input to another PSA,
PSAe , that ampliﬁes with a factor of Ge = ẽi . This is achieved by
modulating the pump power to PSAe based on the measurement
result for ẽi . Finally, the output of PSAe is injected back into signal pulse (xi ) in the main cavity via BSi (see Figure 1c). The BSe
outputs not only signal pulses but also error pulses that are used
only for homodyne detection. Thus, the pump power to PSA0 is
switched oﬀ for the error pulses to deamplify the residual error
pulses by PSA1 , PSA2 , …, PSAN , PSAe . In this manner, spurious
injection of error pulses back into the main cavity is avoided, and
the error pulse dynamics are governed solely by the pump power
pi to the main cavity PSA, which is set to satisfy pi − 1 = 𝛽(𝛼 − x̃i 2 )
or pi − 1 = 𝛽(𝛼 − z̃i 2 ).
One advantage of this optical implementation of CIM-CAC
and CIM-CFC is that only one type of active device—a noisefree phase-sensitive (degenerate optical parametric) ampliﬁer
(PSA)—is needed, and all other elements are passive devices.
This allows for the potential on-chip monolithic integration of
the CIM system as well as low-energy dissipation in the computational unit, which will be discussed in Section 5.
A similar optical implementation of CIM-SFC is shown in Appendix F.
Figure 6b shows the pump pulse factory that provides the second harmonic generation (SHG) pulses to the main cavity PSA,
post-ampliﬁer PSA0 , delay line ampliﬁers PSA1 , PSA2 , ⋯ PSAN ,
and exit ampliﬁer PSAe . The purpose of this pump pulse factory is to reduce the use of EOM modulators, which consume
the bulk of the energy within the overall CIM. A soliton frequency comb generator produces a pulse train at a repetition
frequency of 100 GHz and wavelength of 1.56 𝜇m. Before it is
split into multiple branches, the pulse train is ampliﬁed by a
pump ampliﬁer PSAp . N storage ring cavities continuously produce pump pulses for PSA1 , PSA2 , ⋅ PSAN in order to imple∑
ment the MVM 𝜉Jij x̃ j . For this purpose, the pulses stored in
the ith ring cavity are
√ ampliﬁed to the appropriate amplitudes to
achieve a gain of

Gij = 𝜉Jij . The time needed to use N EOM

arrays is only one round trip of the ring cavity, that is, N × 10
(ps). The out-coupling loss of the storage ring cavities is compensated by the linear gain of the internal PSAs . The pump pulses for
PSAp , PSAs , and PSA0 have constant amplitudes and are therefore driven directly by the PSAp output. The pump pulses P and
Pi for the signal and error pulses in the main cavity, as well as
the exit PSAe , must be modulated over the entire computation
time.
Another factor that must be accounted for in an optical implementation is the calculation of the Ising energy. In our digital
simulation for generating the results presented in this paper,
the Ising energy was calculated at each time step (round trip)
and the smallest energy obtained was used as the result of the
computation. This means that, in an optical implementation,
it is necessary to measure the x̃i amplitude at every round trip
and calculate the Ising energy using, for instance, an external

© 2021 The Authors. Advanced Quantum Technologies published by Wiley-VCH GmbH

25119044, 2021, 11, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/qute.202100077 by Nat Prov Indonesia, Wiley Online Library on [12/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

www.advancedsciencenews.com

www.advquantumtech.com

Figure 6. a) Optical implementation of error correction circuits for CIM-CAC and CIM-CFC. b) Pump pulse factory providing SHG pulses to the main
cavity, and error correction circuits. The pump pulse factory carries N2 pulses spread over N optical cavities corresponding to the elements of the Ising
coupling matrix Jij .

ADC/FPGA circuit. This would defeat the purpose of using
optics, as the digital circuit in the ADC/FPGA would become a
bottleneck in terms of time and energy consumption.
However, we have found that, by applying proper parameter
modulation as shown in Figure 5, it is possible to use only
the ﬁnal state of the system for the result and still have a high
probability of success. To obtain the results for 800-spin Ising
instances (SK model) presented in Section 6, we calculated how
often a successful trajectory was in the ground spin conﬁguration
after the ﬁnal time step. For CIM-SFC, we found that in 100%
of the 7401 successful trajectories the ﬁnal spin conﬁguration
were in the ground state. In other words, if CIM-SFC visits the
ground state at any point during the trajectory, it will also be in

Adv. Quantum Technol. 2021, 4, 2100077

2100077 (8 of 21)

the ground state at the end of the trajectory. For CIM-CFC and
CIM-CAC, this was true only 75% and 48% of the time, respectively. We believe that this diﬀerence among the three systems
is a result of both the intrinsic dynamics and the parameters
used.
This suggests that, for a CIM with optical error correction, it is
possible to simply digitize the ﬁnal measured value of xi obtained
after many round trips to obtain a computational result and still
have a high probability of success. In the case of CIM-CFC and
CIM-CAC, it might be beneﬁcial to read the spin conﬁguration
multiple times during the last few round trips, as the machine
usually visits the ground state close to the end of the trajectory
even if it does not stay there.

© 2021 The Authors. Advanced Quantum Technologies published by Wiley-VCH GmbH

25119044, 2021, 11, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/qute.202100077 by Nat Prov Indonesia, Wiley Online Library on [12/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

www.advancedsciencenews.com

www.advquantumtech.com

5. Quantum Noise Analysis and Energy Cost to
Solution
As the proposed dynamical systems are to be implemented on
analog optical devices, it is important to investigate the extent to
which the noise from the physical system (in this case, quantum
noise from pump sources and external reservoirs) will degrade
their performance. In this section, we present quantum models
based on our optical implementation.
In our optical implementation for CIM-CAC, the real-number
signal pulse amplitude 𝜇i (in units of photon amplitude) obeys
the following truncated W-SDE[22,23]
∑
d
𝜇i = (p − 1)𝜇i − g 2 𝜇i3 + 𝜈̃i
𝜉Jij 𝜇̃ j + ni
dt
j

(18)

where p𝜇i and −𝜇i represent the parametric linear gain and the
linear loss rate, respectively; the latter term includes the cavity
background and extraction/injection beam splitter losses for mutual coupling and error correction. The nonlinear term −g 2 𝜇i3
represents gain saturation (or back-conversion from signal to
pump), where g is the saturation parameter. The saturation photon number is given by 1∕g 2 , which is equal to the average photon number of a solitary OPO at a pump rate of p = 2 (two times
above the threshold). Furthermore, Jij is the (i, j)th element of the
N × N Ising coupling matrix, as described in Section 2. As the
time t is normalized by a linear loss rate, the signal amplitude
decays by a factor of 1∕e at time t = 1. In addition, 𝜇̃ j = 𝜇j + Δ𝜇j
and 𝜈̃i = 𝜈i + Δ𝜈i are the inferred amplitudes for the signal and
error pulses, respectively, and Δ𝜇j and Δ𝜈i represent the additional noise terms governed by vacuum ﬂuctuations incident
on
√
the extraction beam splitter, which are characterized by

1−RB
w,
4RB

where RB is the reﬂectivity of the extraction beam splitter and w
is a zero-mean Gaussian random variable with a variance of one.
Finally, ni is the noise injected from external reservoirs and pump
sources[22,23] ; it is characterized by the two time correlation functions ⟨ni (t)ni (t′ )⟩ = ( 21 + g 2 𝜇i2 )𝛿(t − t′ ). We assume that the external reservoirs are in vacuum states and that the pump ﬁelds are
in coherent states.
The real number error pulse amplitude 𝜈i (in units of photon
amplitude) is governed by
(
)
d
𝜈 = p′i − 1 𝜈i + mi
dt i

(19)

where the correlation function for the noise term is given by
⟨mi (t)mi (t′ )⟩ = 12 𝛿(t − t′ ). The pump rate p′i for the error pulse is
determined by the inferred signal pulse amplitude x̃ i = g 𝜇̃ i normalized by the saturation parameter
(
)
p′i − 1 = 𝛽 𝛼 − x̃ i2

(20)

The error pulses start from coherent states |𝛾⟩1 |𝛾⟩2 ⋯ |𝛾⟩N , for
some positive real number 1∕g ≫ 𝛾 > 0. The absence of a gain
saturation term in Equation (19) implies that the error pulses are
always pumped at below the threshold. Nevertheless, the error
pulses represent exponentially varying amplitudes.
The parameter 𝛽 governs the time constant for the error correction dynamics, and 𝛼 is the squared target amplitude. This

Adv. Quantum Technol. 2021, 4, 2100077

2100077 (9 of 21)

feedback model stabilizes the squared signal pulse amplitude
x̃ i2 = g 2 𝜇̃ i2 to 𝛼 through an exponentially varying error pulse amplitude ei = g𝜈i . Equations (18) and (19) can be rewritten for the
normalized amplitudes xi and ei as
∑
d
𝜉Jij x̃ j + gni
x = (p − 1)xi − xi3 + ẽi
dt i
j

(21)

(
)
d
e = p′i − 1 ei + gmi
dt i

(22)

Except for the noise terms, these formulations are identical to
Equations (1) and (2).
The experimental setup shown in Figure 6 can also be used to
produce a CIM-CFC. In this case, the relevant truncated W-SDE
for the error pulse amplitude is still given by Equation (19) or (22)
but the pump rate p′ should be modiﬁed to
(
)
p′i − 1 = 𝛽 𝛼 − z̃ 2i

(23)

with
z̃ i =

∑

𝜉Jij x̃ j

(24)

j

Finally, a CIM-SFC can also be produced using the experimental setup shown in Appendix F (Figure F1). In this case, Equations (21) and (22) should be modiﬁed to
z̃ i =

∑

𝜉Jij x̃ j

(25)

j

(
)
( )
d
xi = (p − 1)xi − xi3 + k ẽi − z̃ i + tanh cz̃ i + gni
dt

(26)

(
)
d
ei = −𝛽 ei − z̃ i + gmi
dt

(27)

A comparison of the semi-classical nonlinear dynamical models of the CIM-CAC, CIM-CFC, and CIM-SFC represented by
Equations (1)–(8) with the quantum nonlinear dynamical models (truncated Wigner SDE) represented by Equations (21)–(27)
reveals that they diﬀer primarily in terms of the absence or presence of the vacuum and pump noise terms gni and gmi , respectively. The other important diﬀerence is that x̃i and ẽi are inferred
amplitudes of the vacuum noise contribution in the quantum
model, whereas in the semi-classical model the amplitudes xi and
ei can be reproduced without additional noise.
We next discuss the impact of quantum noise on the performance of a CIM. As indicated in Equations (21)–(27), the relative
magnitude of the quantum noise in the signal and error pulses
is governed by the saturation parameter g; when g increases, the
ratio between the normalized pulse (xi , ei ) and normalized quantum noise amplitudes (gni , gmi ) decreases. Therefore, CIM performance is expected to degrade as g increases. However, the
OPO threshold pump power decreases as g increases, (see Figure C1 in ref. [31]), which suggests that the OPO energy cost to
solution can be potentially reduced by increasing g.
Figure 7 shows the probability of success Ps for N = 100 Ising
problems (SK model) plotted against the saturation parameter g 2 .
The reﬂectivity of the extraction beam splitter RB is assumed to be
RB = 0.1. Ps is practically independent of g 2 as long as g 2 ≲ 10−4 .

© 2021 The Authors. Advanced Quantum Technologies published by Wiley-VCH GmbH

25119044, 2021, 11, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/qute.202100077 by Nat Prov Indonesia, Wiley Online Library on [12/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

www.advancedsciencenews.com

www.advquantumtech.com

Figure 7. Success probability Ps versus saturation parameter g2 for CIM-SFC and CIM-CFC at N = 100. The success probability is averaged over 100 SK
instances. CIM-CAC is not shown; however, the result is nearly identical to that for CIM-CFC.

Figure 8. Energy cost to solution in joules of CIM-SFC and CIM-CFC considering only pump power to main cavity PSA. The median ETS is plotted as a
function of g2 for N = 100 and N = 800 SK instances to show the optimal value of g2 in each case.

However, when g 2 exceeds 10−3 , the probability of success drops
rapidly owing to the decreased signal-to-quantum noise ratio, as
mentioned above.
Figure 8 shows the energy cost to solution for Ising problems
(SK model) with N = 100 and N = 800 with only the pump power
to the main cavity PSA, Emain = 2ℏ𝜔(MVM)NΔt∕g 2 , considered,
where MVM is the number of matrix-vector multiplication steps
to solution and Δt is a round-trip time normalized by the signal
lifetime (≈ 0.1).
It is seen from the ﬁgure that CIM-SFC is more robust than
CIM-CFC to quantum noise, allowing for the use of a potentially
larger value of g 2 . This is an expected result of the diﬀerent roles
played by the error variable ei in the respective systems. In CIMCFC, the feedback signal is calculated as
z̃i = ẽi

∑

𝜉Jij x̃j (t)

(28)

j

and is the primary cause of performance degradation when the
quantum noise is increased; this is because a large coherent exci∑
tation of ẽi will amplify small errors in j Jij 𝜉 x̃j (t) and, conversely,
∑
large coherent excitation of j 𝜉Jij x̃j (t) will amplify small errors
in ẽi . There are no such beat noise components in CIM-SFC,

Adv. Quantum Technol. 2021, 4, 2100077

2100077 (10 of 21)

making it more robust to quantum noise. Moreover, the nonlinear function tanh(cz̃i ) can help to suppress the quantum noise.
Although they are not shown, the results for CIM-CAC are
nearly identical to those for CIM-CFC.
If the energy cost in the optical error correction circuit and
pump pulse factory (as described in Figure 6) are included, the
energy cost is increased by several orders of magnitude, as shown
in Figure 9. Here, we assume that the pump pulse energy for a
small signal ampliﬁcation of (≈10 dB) in PSA1 , PSA2 , …, PSAN ,
and PSAe in the optical error correction circuit is 100 fJ per
pulse and that for a large signal ampliﬁcation of (≈50 dB) in
PSA0 is 1 pJ per pulse. These numbers correspond to the experimental values for a thin-ﬁlm LiNO3 ridge waveguide diodepumped OPO (DOPO) at a pump wavelength of 780 nm and a
pump pulse duration of 100 fs.[15] The pump energy consumed
in the optical error correction circuit is estimated to be Ecorrection =
[(N + 1) × 10−13 + 10−12 ]N(MVM)(J). The energy consumption of
the pump pulse factory can be attributed to three components:
the 100-GHz soliton frequency comb generator, EOM modulators, and phase-sensitive ampliﬁers (Figure 6b). The 100-GHz
soliton frequency comb generator requires an input power of
≈100 mW.[16] The 100-GHz EOM modulators require an electrical input power of ≈400 mW each.[17] The energy cost per pulse

© 2021 The Authors. Advanced Quantum Technologies published by Wiley-VCH GmbH

25119044, 2021, 11, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/qute.202100077 by Nat Prov Indonesia, Wiley Online Library on [12/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

www.advancedsciencenews.com

www.advquantumtech.com

Figure 9. Estimated energy cost to solution of optical and GPU implemen√
tations of CIM-CAC versus problem size N. The energy cost to solution
for the optical CIM is based on the results listed in Table 2. The energy
̃ W power consumption of the Nvidia
cost of the GPU is based on the 200
Tesla V100 GPU used.
Table 1. Operational power of active photonic devices in 100 GHz CIM.
Devices

Power consumption

Reference

Soliton frequency comb generator

100 mW

[16]

Phase sensitive ampliﬁer (PSA) 10 dB gain

10 mW

[15]

Phase sensitive ampliﬁer (PSA) 50 dB gain

100 mW

[15]

EOM modulator

400 mW

[17]

for PSAp is ≈1 pJ, whereas the cost of each of the N PSAs used in
the storage ring cavities is ≈100 fJ. Note that the N EOMs (EOM1 ,
EOM2 , … , EOMN ) need only be operated for one initial roundtrip time, 10−11 N (s). The operational powers of the active devices
in the 100-GHz CIM are summarized in Table 1. The energy cost
in the pump pulse factory is Efactory = [1.3 × 10−11 N(MVM) + 4 ×
10−12 N 2 + (10−12 + 10−13 N)(MVM)N](J). Table 2 summarizes the
energy costs in the three parts of the CIM.
Figure 9 shows the energy cost to solution if the CIM-CFC algorithm is implemented on a graphics processing unit (GPU).
A detailed description of this approach will be given in the next
section. Even though the optical implementation of the error correction circuit and pump pulse factory as described in Figure 6 is
technologically challenging, the energy cost can be decreased by
several orders of magnitude relative to a modern GPU.
Table 2. Energy cost to solution in three subsystems in CIM. MVM: matrixvector multiplication steps to solution, N: problem size, one round trip
time: 10−8 s, signal lifetime: 10−7 s.
Subsystem

Energy-to-solution

Main cavity

2.6 × 10−20 (MVM) N g−2

Optical error correction
circuit

[(N + 1)10−13 + 10−12 ](MVM)N ≃ 10−13 N2 (MVM)

Pump pulse factory

[N × 10−13 + 10−12 ](MVM)N + 1.3 ×
10−11 N(MVM) + 4 × 10−12 N2 ≃ 10−13 N2 (MVM)

Adv. Quantum Technol. 2021, 4, 2100077

2100077 (11 of 21)

Figure 10. (top) TTSs of CIM-CAC, CIM-CFC, and CIM-SFC vs. problem
√
size N. The shaded regions represent the 25th–75th-percentile TTS.
(bottom) The 75th and 90th-percentile TTS compared with the median
TTS as a function of problem size for all three systems.

6. CIM-Inspired Heuristic Algorithms
6.1. Scaling Performance of CIM-CAC, CIM-CFC, and CIM-SFC
To test whether the three classical nonlinear dynamics models
given by Equations (1)–(8) are good Ising solvers, we can numerically integrate them on a digital platform. In this section, we
will consider the numerical integration of these CIM-inspired algorithms using an Euler step. To ensure numerical stability, we
constrain the range of some variables; the details of this are presented in Appendix A.
The relevant performance metric is the time to solution, or
TTS (the number of integration time steps required to achieve
a success rate of 99%). In particular, we study how the median
TTS scales as a function of the problem size for randomly generated SK spin glass instances (the couplings are chosen randomly
from the range +1 to −1). The median TTS is computed on the
basis of a set of 100 randomly generated instances per problem
size; 3200 trajectories are used per instance to evaluate the TTS.
Figure 10 shows the median TTSs of the three CIM-inspired
algorithms (CIM-CAC, CIM-CFC, and CIM-SFC) with respect

© 2021 The Authors. Advanced Quantum Technologies published by Wiley-VCH GmbH

25119044, 2021, 11, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/qute.202100077 by Nat Prov Indonesia, Wiley Online Library on [12/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

www.advancedsciencenews.com

www.advquantumtech.com

to problem size. The shaded regions represent 25th–75th √
percentiles. The linear behavior of the TTS with respect to N
indicates that these algorithms have the same root exponential
scaling of TTS that is observed in physical CIMs with quantum noise from external reservoirs.[8,31] All three algorithms appear to have very similar scaling coeﬃcients
if the TTS is as√
sumed to be of the form TTS ≈ A ⋅ B n . In addition to the similar scaling, all three algorithms show a similar spread (25th–
75th percentile) in TTS, as indicated by the shaded region in the
top ﬁgure. Although CIM-SFC appears to have a slightly larger
spread in all cases, its spread does not appear to increase at larger
problem sizes.
6.2. Comparison with Noisy Mean Field Annealing
To demonstrate the importance of the auxiliary variable (error
pulse) in CIM-SFC, we compared its performance to that of
another CIM-inspired algorithm—noisy mean ﬁeld annealing
(NMFA).[26] Although NMFA also applies a hyperbolic tangent
function to the mutual coupling term, it does not have an auxiliary variable and relies on (artiﬁcial) quantum noise to escape
from local minima. Figure 11 compares the scaling of NMFA to
CIM-SFC with diﬀerent values of the feedback parameter k. As
k controls the strength of the destabilization force caused by the
auxiliary variable, we can measure the importance of the term
k(zi − ei ) to the scaling behavior. When k = 0, CIM-SFC is nearly
identical to NMFA. The fact that CIM-SFC performs slightly
worse at k = 0 indicates that the noise included in NMFA likely
has a small eﬀect and might help destabilize the local minima
(which can also be observed in Figure 7). The cases k = 0.15 and
k = 0.2 are shown as, respectively, an intermediate case and as
the (experimentally obtained) optimal value for k in CIM-SFC.
It is seen that the addition of the error correction feedback term
k(zi − ei ) to Equation (7) is eﬀective at improving both the scaling
and spread of TTS for the SK instances. This implies that the “correlated artiﬁcial noise” provided by the auxiliary variable is more
eﬀective at ﬁnding better solutions than the “random quantum
noise” from the reservoirs.
6.3. Comparison with Discrete Simulated Bifurcation Machine
We then compared the performance of the CIM-inspired algorithms with that of another heuristic Ising solver—the discrete
simulated bifurcation machine (dSBM).[27–29] Like CIM, dSBM
makes use of analog spins and continuous dynamics to solve
combinatorial optimization problems.
We are aware that the authors of ref. [29] seem to claim that
dSBM is algorithmically superior to CIM-CAC based on their
comparison of the required number of MVMs to solution. Although the authors of ref. [29] discussed the wall clock TTS of
their implementations on many problem sets, in making the
claim of algorithmic superiority they only used the median TTS
(in units of MVM) on SK instances with two problem sizes. In
this section, we will provide a more detailed comparison between
the three algorithms (CIM-CAC, CIM-CFC, and CIM-SFC) and
dSBM using MVM to solution (or equivalently, the number of
integration time steps to solution) as the performance metric. As

Adv. Quantum Technol. 2021, 4, 2100077

2100077 (12 of 21)

√
Figure 11. (top) TTSs of CIM-SFC and NMFA versus problem size N.
The shaded regions represent 25th–75th-percentile TTS. The results for
NMFA are from ref. [12]. (bottom) TTS for N = 400 SK instances for diﬀerent values of k. The 75th and 90th percentiles are not shown for smaller
values of k because they were too large to be computed.

mentioned before, this provides for eﬀective comparison because
all of the algorithms in question will have MVM as a computational bottleneck when implemented on a digital platform. As
discussed in Section 4, the computation of the Ising energy can
be left until the end of the trajectory in most cases; thus, for this
section we will only consider the MVM involved in the computation of the mutual coupling term when calculating the MVM
to solution.
The following problem instance sets were used in the comparison:
1) A set of 100 randomly generated 800-spin SK instances (available upon request from the authors). This instance set contains fully connected instances with weights of +1, −1.
2) The G-set instances that have been used as a benchmark
for max-cut performance (available at https://web.stanford.
edu/ yyye/yyye/Gset/). In this study, we considered 50 instances with problem sizes of 800–2000. These instances have

© 2021 The Authors. Advanced Quantum Technologies published by Wiley-VCH GmbH

25119044, 2021, 11, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/qute.202100077 by Nat Prov Indonesia, Wiley Online Library on [12/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

www.advancedsciencenews.com

www.advquantumtech.com

Figure 12. Required number of MVMs to solution for CIM-CAC, CIM-CFC, and CIM-SFC versus number of MVMs to solution for dSBM. The median
TTSs are indicated by red lines and the 25th–75th percentiles are indicated by shaded blue regions.

varying edge densities and include weights of either +1, 0 or
+1, 0, −1.
3) Another set of 1000 randomly generated 800- and 1200-spin
SK instances (available upon request from the authors) was
used to evaluate the worst-case performance.

To compare the performance on the 800-spin SK instances, the
dSBM algorithm was also implemented on a GPU. The parameters for dSBM were chosen on the basis of the parameters in ref.
[29] (see Appendix D).
Figure 12 compares the performance of the three algorithms
(CIM-CAC, CIM-CFC, and CIM-SFC) in each instance with
that of dSBM on the 800-spin SK instance set. The ground-state
energies used to evaluate the MVM to solution are the lowest
energies found by the four algorithms. As all four algorithms
found the same lowest energies, it is highly likely that these are
true ground-state energies. The parameters for all four systems
can be found in Appendix A. As shown in Figure 12, all four
systems performed in a remarkably similar manner on the
800-spin-instances case when the parameters were optimized.
It is important to note that, using the parameters shown in Figure 12, CIM-SFC did not ﬁnd the ground state in one instance.
However, if diﬀerent parameters are used, CIM-SFC will ﬁnd the
ground state for this particular instance as well. Thus, although

Adv. Quantum Technol. 2021, 4, 2100077

2100077 (13 of 21)

CIM-SFC can achieve high performance, it is highly sensitive to
parameter selection.
The median TTSs (in units of MVM) of CIM-CFC, CIM-SFC,
and dSBM were nearly the same at ≈ 2 × 105 each. Furthermore,
the spread in TTS was similar for all three algorithms. Although
CIM-CAC had a slightly worse median TTS (by less than a factor of two), it is worth noting that the instances in which CIMCAC performed better than dSBM tended to be the harder instances, indicating that, of the four algorithms, CIM-CAC might
show slightly better worst-case performance. We investigate this
further later in this section. This pattern was also seen on the
G-set.
Overall, all four algorithms performed similarly on the fully
connected instance set, and it was impossible to determine which
algorithm was the most eﬀective for this problem type. In addition to the similarities in terms of median TTS and spread, there
were high levels of correlation between the TTSs produced by the
four systems. This indicates either that instance diﬃculty is a universal property for all Ising heuristics or that there is something
fundamentally common to the four algorithms: see Appendix E
for a further discussion of the similarities and diﬀerences between the systems.
Although CIM-SFC performed well on fully connected problem instances, it struggled on many G-set instances. In Appendix D, we discuss a partial reason for this failure; however,

© 2021 The Authors. Advanced Quantum Technologies published by Wiley-VCH GmbH

25119044, 2021, 11, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/qute.202100077 by Nat Prov Indonesia, Wiley Online Library on [12/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

www.advancedsciencenews.com

www.advquantumtech.com

Figure 13. (left) TTS on G-set graphs for CIM-CAC, CIM-CFC, and dSBM. The best known cut values are found in ref. [29]. The TTS for dSBM is from ref.
[29]. In this plot, the instances are separated into groups depending on the graph type and size. The dots above the plot indicate where the best known
cut value was not found. (right) Histograms showing which algorithm achieves the slowest and fastest TTS, respectively. The column labeled “none”
indicates the two instances in which none of the three algorithms found the best known cut value. The parameters are chosen and optimized separately
for each instance type. An instance-by-instance comparison and the parameters used are presented in Appendix B.

the full reason is yet to be understood. In the future, we expect to
modify CIM-SFC or ﬁnd better parameters to enable it to solve
all problem types; for now, we will simply consider CIM-SFC to
be a fully connected (or densely connected) Ising solver and compare only the performances of CIM-CAC, CIM-CFC, and dSBM
on the G-set. For some of the results produced by CIM- SFC on
the G-set, see Appendix D.
The three algorithms (CIM-CAC, CIM-CFC, and dSBM) all
demonstrated fairly good performance on the G-set; however, we
argue that CIM-CAC is the most consistently eﬀective algorithm.
CIM-CAC and dSBM were able to ﬁnd the best known cut values
in 47 out of 50 instances; CIM-CFC found the best known cut
value in 45 out of 50 instances. It is worth noting that the simulation time used to calculate the TTS for dSBM[29] was much
longer than that used in this study. Given the same simulation
time, dSBM would most likely have solved only 45 out of 50 instances. As shown in Figure 13, CIM-CAC and CIM-CFC were
faster (in units of MVM) than dSBM in most instances. More importantly, among the instances in which dSBM was faster there
were no cases in which it signiﬁcantly faster than CIM-CAC other
than G37, in which CIM-CAC did not ﬁnd the best known cut
value. Meanwhile, CIM-CAC was more than an order of magnitude faster than dSBM in 13 out 50 instances. Based on this, we
believe that CIM-CAC is a more reliable algorithm when considering many problem types.
The diﬀerence between CIM-CAC and CIM-CFC is subtle,
which is to be expected given that the dynamics of the two systems are very similar. Although the performance of the two algorithms on the G-set was nearly identical in most cases, for some
of the harder instances there were some cases in which CIM-CFC
could not ﬁnd the best known cut value or CIM-CFC required a

Adv. Quantum Technol. 2021, 4, 2100077

2100077 (14 of 21)

signiﬁcantly longer TTS. This indicates either that CIM- CAC is
fundamentally a more promising algorithm or a precise parameter selection for CIM-CFC is required.
As noted in Figure 12, the worst-case performance of CIMCAC might have been slightly better than that of dSBM. To evaluate this further, we created new sets of 1000 800- and 1200spin SK instances. Figure 14 shows the number of instances
solved as a function of the number of MVMs required to achieve
a success probability of 99%. It is seen that, in both cases,
dSBM could solve the easier instances with fewer MVMs but,
for the hardest instances, CIM-CAC was faster; this can be ascertained by observing the intersection point of the two curves in
Figure 14.
In nearly all cases, the best Ising energy was the same for
both solvers when a similar number of MVMs was used (see Appendix A for the parameters). However, for two instances in the
N = 1200 set, the Ising energy found by CAC was not found by
dSBM. This remained true even when 50 000 dSBM trajectories
were used for these instances.
Our results suggest that dSBM might struggle considerably on
some harder SK instances. However, we acknowledge that this
could be a result of sub-optimal parameter selection for dSBM.
The parameters used (see Appendix A) were optimized manually
to achieve a good median TTS; however, they might not be the
best parameters for solving the hardest instances. By contrast, for
CIM-CAC the optimal parameters for the median TTS appear to
also perform well on the hardest instances.
To ensure that an Ising solver can ﬁnd the true ground state
of a given problem, it is very important that its worst-case performance is acceptable. For this purpose, we believe that CIM-CAC
is likely to be the most fundamentally superior algorithm, at least

© 2021 The Authors. Advanced Quantum Technologies published by Wiley-VCH GmbH

25119044, 2021, 11, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/qute.202100077 by Nat Prov Indonesia, Wiley Online Library on [12/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

www.advancedsciencenews.com

www.advquantumtech.com
posed optical CIM to surpass existing digital algorithms implemented on CMOS platforms in terms of both speed and energy
consumption.
The proposed CIM-inspired algorithms were shown to be
fast and accurate Ising solvers even when implemented on
an existing digital platform. In particular, we demonstrated
that their performance is very similar to that of other existing
analog-system-based algorithms such as dSBM. This again
brings up the question raised in ref. [11] as to whether the
simulation of analog spins on a digital computer can outperform
a purely discrete heuristic algorithm. Finally, whether chaotic
dynamics are necessary for a deterministic dynamical system
to be a good Ising solver is left as an open issue for future
research.[11,12,29]

Appendix A: Optimization of Simulation
Parameters
Here we summarize the simulation parameters used in our numerical experiments. The parameters are optimized empirically
and, therefore, do not necessarily reﬂect the true optimum values.

Parameters used in Figure 5

CIM-SFC (upper left panel)

Figure 14. Number of instances that remain unsolved (success probability under 99%) after a certain number of MVMs (time steps) for CIM-CAC
and dSBM. The dotted lines represent the assumption of a log-normal distribution for the TTS on randomly generated SK instances. The instance
sets used are 1000 randomly generated SK instances (diﬀerent from the
100 instances used in Figure 12) of problem sizes N = 800 (top) and N
= 1200 (bottom). The parameters for both systems can be found in Appendix A.

in the case of randomly generated SK instances. For the other
CIM modiﬁcations, this is likely not true; in particular, for CIMSFC the worst-case performance is signiﬁcantly worse than that
of dSBM and CIM-CAC (as shown in Figure 10). In the future, it
would be interesting to investigate the cause of this phenomenon
and also to examine the spread of TTS values over diﬀerent problem types.

7. Conclusion
The new coherent Ising machines presented in this paper (CIMCFC and CIM-SFC) have considerable potential as both digital heuristic algorithms and optically implemented physical devices. Rapid advances in thin-ﬁlm LiNbO3 platform[15–17] as a
photonic integrated circuit technology might enable the pro-

Adv. Quantum Technol. 2021, 4, 2100077

2100077 (15 of 21)

CIM-CFC (upper right panel)

N step

500

N step

ΔT

0.4

ΔT

0.4

p

−1.0

p

−1.0

1000

c

1.0

𝛼

1.0

𝛽

0.3

𝛽

0.2

k

0.2

CIM-SFC (lower left panel)

CIM-CFC (lower right panel)

N step

500

N step

ΔT

0.4

ΔT

0.4

p

−1.0 → 1.0

Tr

900

1000

c

1.0 → 3.0

Tp

100

𝛽

0.3 → 0.1

p

−1.0 → 1.0

k

0.2

𝛼

1.0

𝛽

0.2

Parameters used in Figures 10, 11, and 12
CIM-CAC: In the simulation
the xi variables
√ of CIM-CAC,
√
were restricted to the range [− 32 𝛼, 32 𝛼] at each time step. The
parameters p and 𝛼 were modulated linearly from their starting
to ending values during the Tr time steps and were kept at the
ﬁnal value for an additional Tp time steps. The initial value xi
was set to a random value chosen from a zero-mean Gaussian
distribution with a standard deviation of 10−4 and ei = 1. Furthermore, 3200 trajectories were computed per instance to evaluate
TTS. The actual parameters used for simulation are listed below:

© 2021 The Authors. Advanced Quantum Technologies published by Wiley-VCH GmbH

25119044, 2021, 11, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/qute.202100077 by Nat Prov Indonesia, Wiley Online Library on [12/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

www.advancedsciencenews.com

www.advquantumtech.com

N step

3200

ΔT

0.125

Tr

2880

Tp

320

p

−1.0 → 1.0

𝛼

1.0 → 2.5

𝛽

0.8

CIM-CFC: In the simulation of CIM-CFC, the xi variables
were restricted to the range [−1.5, 1.5] and ei was restricted to the
range [0.01, ∞]. The parameter p was modulated linearly from its
starting to ending values during the ﬁrst Tr time steps and kept
at the ﬁnal value for an additional Tp time steps. The initial value
xi was set to a random value chosen from a zero-mean Gaussian
distribution with a standard deviation of 0.1 and ei = 1. Furthermore, 3200 trajectories were computed per instance to evaluate
TTS. The actual parameters used for simulation are listed below:

Moreover, it is important to note that we used the same number of time steps for all problem sizes in Figures 10 and 11. As
it is likely that the optimal number of time steps is smaller for
smaller problem sizes, the scaling of TTS when the number of
time steps is optimized separately for each problem size might
be slightly worse than the reported scaling. However, we do not
believe that this diﬀerence would be very signiﬁcant. For a discussion of the scaling of TTS for CIM-CAC when diﬀerent parameters are chosen (see Appendix C).
dSBM: To obtain the results shown in Figure 12, dSBM was
implemented as described in ref. [29]. The following parameters
were used:
N step

2000

ΔT

1.25

c

0.5

Parameters used in Figure 14
N step

1000

ΔT

0.4

Tr

900

Tp

100

p

−1.0 → 1.0

𝛼

1.0

𝛽

0.2

The parameters for the N = 800 case were the same as those used
to obtain Figure 12. The parameters used for N = 1200 are listed
below. In most instances, 3200 trajectories were used for N =
1,200; however, to accurately evaluate the probability of success,
10 000–50 000 trajectories were computed for the ten hardest instances for both algorithms. Moreover, owing to the hardness in
the N = 1200 case, we are not very certain that the true ground
state was found.
CIM-CAC:

CIM-SFC: The xi and ei variables did not need to be restricted as this system is more numerically stable than CIM-CAC
or CIM-CFC. The parameters p, c, and 𝛽 were modulated linearly from their starting to ending values during simulation. The
initial value xi was set to a random value chosen from a zeromean Gaussian distribution with standard deviation of 0.1 and
ei = 0. 3200 trajectories were computed per instance to evaluate TTS. The actual parameters used for simulation are listed
below:

N step

500

ΔT

0.4

p

−1.0 → 1.0

c

1.0 → 3.0

𝛽

0.3 → 0.1

k

0.2

In addition to the parameters mentioned above, it is important
that the normalizing factor 𝜉 for the mutual coupling term be
chosen as[31]
√
𝜉=

2N
∑ 2
Jij

(A1)

This choice is crucial for the successful performance of CIMSFC but not for CIM-CAC or CIM-CFC.

Adv. Quantum Technol. 2021, 4, 2100077

2100077 (16 of 21)

N step

8000

ΔT

0.125

Tr

7200

Tp

800

p

−1.0 → 1.0

𝛼

1.0 → 2.5

𝛽

0.8

dSBM:
N step

4000

ΔT

1.25

c

0.5

Numerical Integration
An Euler step was used for integration in all cases except for
dSBM. As described above, we constrained the ranges of the xi
variables to ensure numerical stability. This was not necessary to
ensure performance, but it allowed us to increase the integration
time step by a factor of two or three without compromising the
probability 0f success. In Figure A1, we show the probability of
success of CIM-CAC with respect to the time step value for both
constrained and unconstrained systems.

© 2021 The Authors. Advanced Quantum Technologies published by Wiley-VCH GmbH

25119044, 2021, 11, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/qute.202100077 by Nat Prov Indonesia, Wiley Online Library on [12/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

www.advancedsciencenews.com

www.advquantumtech.com
CIM-CFC Parameters for G-Set
The variables were restricted as described in Appendix A and the
initial conditions were set in the same manner. The following
parameters were the same for all the G-set instances:
𝛼 1.0
𝛽 0.15

(B2)

The parameters p, ΔT, and the number of time steps used in
each phase were chosen by instance type as follows:

Figure A1. Probability of success of CIM-CAC with respect to time step
for both constrained and unconstrained systems. For the blue curve, the
√
√
xi amplitudes are restricted to the range [−1.5 𝛼, 1.5 𝛼].

Graph
type

Edge
weight

N

Instance
#

p

N step

ΔT

Tr

Tp

Random

{+1}

800

1–5

−1.0 → 1.0

4000

0.125

3600

400

Random

{+1, −1}

800

6–10

−1.0 → 1.0

2000

0.25

1800

200

The results in Section 5 for CIM-CFC do not reﬂect the use of
this numerical constraint; the CIM in this section was meant to
be a physical machine and, therefore, a time step of 0.2 was used.

Toroidal

{+1, −1}

800

11–13

−3.0 → −1.0

2000

0.25

1800

200

Planar

{+1}

800

14–17

−2.0 → 0.0

8000

0.125

7200

800

Planar

{+1, −1}

800

18–21

−2.0 → 0.0

4000

0.25

3600

400

Appendix B: Simulation Results for G-Set

Random

{+1}

1000

43–46

−1.0 → 1.0

5000

0.2

4500

500

Planar

{+1}

1000

51–54

−2.0 → 0.0

16 000 0.125 15 200 800

{+1}

The results in Figure 13 for dSBM are taken directly from the
GPU implementation of dSBM in ref. [29]. The unit for TTS in
Table B1 is TTS or, equivalently, MVM to solution. In our simulation, 3200, 10 000, or 32 000 trajectories were generated to evaluate the TTS depending on the instance diﬃculty. The numbers
in bold denote the best TTS among the three algorithms.
CIM-CAC Parameters for G-Set

𝛼 1.0 → 3.0
𝛽
0.3

(B1)

The parameters p, ΔT, and the number of time steps used in
each phase were chosen by instance type as follows:
Edge
weight

N

p

Instance
#

N step

ΔT

Tr

Tp

Random

{+1}

800

1–5

−0.5 → 1.0

6666

0.075

6000

666

Random

{+1, −1}

800

6–10

−0.5 → 1.0

6666

0.075

6000

666

4500

500

Toroidal

{+1, −1}

800

11–13

−4.0

5000

0.1

Planar

{+1}

800

14–17

−1.0

20 000

0.05 18 000 2000
0.05 18 000 2000

Planar

{+1, −1}

800

18–21

−1.0

20 000

Random

{+1}

1000

43–46

−0.5 → 1.0

10 000

0.1

Planar

{+1}

1000

51–54

−1.0

20 000

0.05 18 000 2000

{+1}

9000

1000

2000

22–26

−0.5 → 1.0

20 000

0.1

Random

{+1, −1} 2000

27–31

−0.5 → 1.0

20 000

0.1

19 000 1000

Toroidal

{+1, −1} 2000

32–34

−4.0 → −3.0 20 000

0.1

19 000 1000

Random

22–26

−1.0 → 1.0

10 000

0.2

9500

500

{+1, −1} 2000

27–31

−1.0 → 1.0

10 000

0.2

9500

500

Toroidal

{+1, −1} 2000

32–34

−3.0 → −1.0 40 000

0.1

39 000 1000

Planar

{+1}

2000

35–38

−2.0 → 0.0

80 000

0.05 78 000 2000

Planar

{+1}

2000

39–42

−2.0 → 0.0

40 000

0.1

39 000 1000

Appendix C: Reasoning for Parameter Selection

The variables were restricted as described in Appendix A and the
initial conditions were set in the same manner. The following
parameters were the same for all the G-set instances:

Graph
type

2000

Random

Random

19 000 1000

Planar

{+1}

2000

35–38

−1.0 → −0.5 80 000

0.05 78 000 2000

Planar

{+1}

2000

39–42

−1.0 → −0.5 80 000

0.05 78 000 2000

Adv. Quantum Technol. 2021, 4, 2100077

2100077 (17 of 21)

The parameters were generally selected numerically; however,
the choices of p, 𝛼, and 𝛽 can be understood as follows. It
is observed that the average residual energy visited by CIMCAC during the search process can be roughly estimated by the
formula[11]
ΔEavg ≈ K

1−p
𝛼𝛽

(C1)

where K is a constant depending only on the problem type
and size. This formula essentially predicts the eﬀective sampling temperature of the system (although the distribution might
not be an exact Boltzmann distribution). Based on this philosophy, we gradually reduced the “system temperature” to produce an annealing eﬀect. This was the motivation for increasing p and 𝛼. The diﬀerent choices for the range of p on different G-set instances reﬂect the vastly diﬀerent values for
the constant K depending on the structure of the max-cut
problem.
In a more general setting, the value of K can be predicted on
the basis of the problem type and the ranges for p and 𝛼 can be
chosen accordingly.
Although it has not been veriﬁed, a similar formula most likely
holds for CIM-CFC; thus, the parameters for CIM-CFC were chosen in the same manner.

© 2021 The Authors. Advanced Quantum Technologies published by Wiley-VCH GmbH

25119044, 2021, 11, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/qute.202100077 by Nat Prov Indonesia, Wiley Online Library on [12/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

www.advancedsciencenews.com

www.advquantumtech.com

Table B1. Probabilities of success and TTSs of CIM-CAC, CIM-CFC, and dSBM on G-set graphs. The probabilities of success for CIM-CAC and CIM-CFC
are for single trajectories with the parameters detailed in Appendix B. Note that Ps for dSBM taken from ref. [29] is the success probability for a batch of
1

160 trajectories. To calculate the Ps for a single dSBM trajectory, use 1 − (1 − Ps ) 160 .
Instance

CIM-CAC TTS

CIM-CAC Ps

CIM-CFC TTS

CIM-CFC Ps

G1

90 805

0.286875

60 078

0.264062

339 332

G2

920 217

0.0328125

1 330 454

0.01375

2 578 124

0.82

G3

169 551

0.165625

249 212

0.07125

400 343

0.996

dSBM TTS

dSBM Ps
0.987

G4

209 086

0.136563

239 389

0.0740625

361 673

0.983

G5

226 881

0.126562

226 449

0.078125

618 221

0.972
0.979

G6

188 908

0.15

104 083

0.0846875

190 728

G7

562 413

0.053125

146 490

0.0609375

201 889

0.974

G8

431 029

0.06875

399 118

0.0228125

358 947

0.954

G9

411 604

0.071875

223 836

0.0403125

1 095 704

0.867

G10

1 388 073

0.021875

622 470

0.0146875

1 410 031

0.407

G11

337 563

0.0659375

222 079

0.040625

282 524

0.98

G12

224 452

0.0975

78 562

0.110625

407 997

0.973
0.996

G13

391 011

0.0571875

373 236

0.024375

800 687

G14

17 291 018

0.0053125

13 080 721

0.0028125

1 469 967 245

0.005

G15

521 572

0.161875

462 528

0.0765625

6 782 113

0.804

G16

494 303

0.17

737 146

0.04875

9 156 329

0.992

G17

3 089 154

0.029375

3 256 332

0.01125

33 222 397

0.283

G18

556 635

0.1525

507 805

0.035625

14 375 986

0.074

G19

1 218 307

0.0728125

179 562

0.0975

417 204

0.995

G20

106 718

0.578125

42 428

0.352187

188 349

0.98

G21

3 991 180

0.0228125

574 365

0.0315625

10 080 921

0.136

G43

174 031

0.2325

145 625

0.14625

228 908

0.992

G44

244 188

0.171875

257 230

0.085625

263 171

0.985

G45

880 856

0.0509375

970 877

0.0234375

1 754 473

0.985

G46

1 528 073

0.0296875

717 957

0.0315625

610 421

0.992

G51

3 732 360

0.024375

2 189 016

0.0331

424 989 992

0.067

G52

3 122 871

0.0290625

382 0774

0.0191

92 285 270

0.213

G53

17 291 018

0.0053125

11 298 922

0.0065

1 676 440 469

0.043

G54

294 684 837

0.0003125

1 178 886 725

6.25e-05

49 107 077 298

0.0006

G22

2 516 544

0.0359375

2 718 081

0.0168

8 401 394

0.928

G23

N/A

0.0

N/A

0.0

N/A

0.0

G24

4 785 454

0.0190625

5 733 406

0.008

10 585 339

0.648

G25

17 291 018

0.0053125

15 327 529

0.003

43 414 254

0.399

G26

10 117 012

0.0090625

10 941 648

0.0042

10 730 290

0.643

G27

835 530

0.104375

649 972

0.0684

832 465

0.971
0.952

G28

2 389 444

0.0378125

2 413 498

0.0189

1 455 914

G29

4 164 219

0.021875

7 404 644

0.0062

5 516 820

0.737

G30

42 058 344

0.0021875

32 871 041

0.0014

11 002 259

0.738

G31

49 075 749

0.001875

92 080 375

0.0005

19 923 732

0.199

G32

70 802 710

0.0013

1 841 975 969

0.0001

150 969 342

0.093

G33

306 965 291

0.0003

N/A

0.0

2 204 950 868

0.005

G34

20 886 506

0.0044

32 801 883

0.0056

84 156 149

0.231

G35

N/A

0.0

N/A

0.0

N/A

0.0

G36

368 321 503

0.0005

3 683 951 938

0.0001

736 790 387 782

0.0001

G37

N/A

0.0

N/A

0.0

294 701 417 831

0.0002

G38

108 264 816

0.0017

147 181 162

0.0025

1 046 295 719

0.068

G39

4 065 368

0.0443

3 497 864

0.0513

651 087 484

0.107
0.154

G40

1 841 975 969

0.0001

N/A

0.0

264 354 894

G41

17 123 320

0.0107

7 916 531

0.023

222 414 431

0.282

G42

13 969 282

0.0131

18 328 423

0.01

N/A

0.0

Adv. Quantum Technol. 2021, 4, 2100077

2100077 (18 of 21)

© 2021 The Authors. Advanced Quantum Technologies published by Wiley-VCH GmbH

25119044, 2021, 11, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/qute.202100077 by Nat Prov Indonesia, Wiley Online Library on [12/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

www.advancedsciencenews.com

www.advquantumtech.com

Figure C1. Performance of CIM-CAC with respect to problem size for different parameters. The ﬁxed parameters are indicated in red and the parameter modulation is indicated in blue. The red and blue dotted lines are
ﬁts for the lower envelopes of the red and blue curves, respectively.

Optimal Parameters with Respect to Problem Size (CIM-CAC)
Figure C1 shows the diﬀerence in scaling when the parameters
are ﬁxed (red-shaded areas) compared to when the parameters
are modulated linearly (blue-shaded areas). In addition, the optimal annealing time (in other words, the optimal speed of modulation) will change with respect to the problem size, as long annealing times are required to obtain good results at large problem
sizes. This pattern was also used in choosing the parameters on
the G-set.
Although Figure C1 is based on the Gaussian quantum model
for CIM-CAC in MFB-CIM (see ref. [31]), the diﬀerence in performance between this model and the noiseless model discussed in
this paper is insigniﬁcant, as g 2 = 10−4 was used. It should also
be noted that a time step of 0.01 was used to produce the results
in Figure C1; as a result, the TTS in this ﬁgure is an order of magnitude longer than the results produced in this study, in which a
time step of 0.125 was used.

Appendix D: Results and Discussion for CIM-SFC
on G-Set
Based on our understanding of CIM-SFC, it is very important that
the term tanh(czi ) transitions from the “soft spin” mode, in which
czi ≈ 0 and tanh(czi ) ≈ czi , to the “discrete spin” mode, in which
|czi | >> 0 and tanh(czi ) ≈ sign(czi ). Therefore, we used the normalizing factor 𝜉 (as
√ deﬁned above) to ensure that zi would on
average be around 2 for a randomly chosen spin conﬁguration,
thereby allowing us to obtain similar results using the same value
for c in all of the cases. However, this only works for conditions
such as those for SK instances in which each node has equal connectivity; thus, we could expect zi to have roughly the same range
of values for all i.
On some G-set instances, in particular the planar graph instances, some nodes had a much larger degree; as a result, czi

Adv. Quantum Technol. 2021, 4, 2100077

2100077 (19 of 21)

was too large in some cases and too small in others regardless of the normalizing factor 𝜉 used. This might have been
one of the reasons why CIM-SFC struggled on many G-set instances, particularly planar graphs. It could also be the reason why dSBM struggled on planar graphs as well, as dSBM
relies on the same normalizing factor to obtain good results.
CIM-CAC and CIM-CFC did not need this normalizing factor, as they automatically compensate for diﬀerent values of
∑
j Jij 𝜎j ; this might have been why they performed well on planar
graphs.
∑
For toroidal graphs, the opposite is true, as j Jij 𝜎j can only
take on ﬁve diﬀerent values for such graphs. This could mean
that the transition from “soft spin” to “discrete spin” is rapid in
the case of CIM-SFC, indicating the need to carefully tune the
parameters to obtain good results on toroidal graphs.
Although this observation regarding the analog/discrete transition might partially explain the poor results on the G-set, it
is not a complete explanation. For example, CIM-SFC struggled on some random graphs (such as G9) that do not have
the above-mentioned property because each node has similar
connectivity.
The results for CIM-SFC on the G-set as well as the parameters
used are listed below (not all instances were tested):
Results for CIM-SFC on the G-Set

TTS

Ps

G1

28 470

0.194

G2

1 531 984

0.004

G3

130 388

0.046

G4

435 510

0.014

G5

380 685

0.016

G6

112 834

0.0202

G7

163 316

0.014

G8

125 360

0.0182

G9

4 604 018

0.0005

G10

395 845

0.0058

G11

195 461

0.0572

G12

128 184

0.0859

G13

311 368

0.0363

G43

1 702 012

0.0134375

Instance

G44

1 742 812

0.013125

G45

73 671 209

0.0003125

G46

1 927 483

0.011875

For instance, on G14–G21 (800-node planar graphs) and G51–
G54 (1,000-node planar graphs), CIM-SFC had a success probability of either zero or a very small nonzero value. Note that 2000node instances were not tested.
Parameters for CIM-SFC on G-Set
Common Parameters:
p| −1.0 → 1.0

(D1)

© 2021 The Authors. Advanced Quantum Technologies published by Wiley-VCH GmbH

25119044, 2021, 11, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/qute.202100077 by Nat Prov Indonesia, Wiley Online Library on [12/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

www.advancedsciencenews.com

www.advquantumtech.com

Parameters Selected by Problem Type:
Instance
#

c

𝛽

800

1–5

1.0 → 3.0

800

6–10

1.0 → 3.0

{+1, −1}

800

11–13

1.4

{+1}

1000

43–46

1.4 → 4.2

Edge
weight

N

Random

{+1}

Random

{+1, −1}

Toroidal
Random

Graph
type

k

N step

ΔT

0.3 → 0.0

0.2

2666

0.15

0.3 → 0.0

0.2

500

0.4

0.05 → 0.0 0.32

2500

0.4

0.2 → 0.0

5000

0.2

0.2

The parameters for CIM-SFC are chosen experimentally and
the understanding of how the parameters aﬀect the performance
and dynamics of the algorithm is therefore limited. Once this system is studied more thoroughly, we will propose a more systematic method of choosing parameters to ensure good performance
on many diﬀerent problem types.

Appendix E: Similarities and Diﬀerences Between
CIM and SBM Algorithms
Using continuous analog dynamics to solve discrete optimization problems is a somewhat new concept, and it is interesting
to compare the diﬀerent approaches.[11,13,29] In this appendix, we
will brieﬂy discuss some similarities and diﬀerences among the
three CIM-inspired algorithms and the SBM algorithms.
All four systems discussed in Section 6, namely CIM-CAC,
CIM-CAC, CIM-SFC, and dSBM, were originally inspired by the
same fundamental principle[10,27] :
The function
(
)
∑∑
∑ xi2 1 − p
Jij xi xj
(E1)
−
xi2 + c
H(x) =
4
2
i
i
j
can be used as a continuous approximation of the Ising cost function.
In the original CIM algorithm, gradient descent is used to ﬁnd
the local minima of H as it is deformed by increasing p. This
system has two signiﬁcant drawbacks[10] :
1) Local minima are stable;
2) Incorrect mapping of the Ising problem to the cost function
occurs as a result of amplitude heterogeneity.

All four algorithms discussed in Section 6 can be regarded as
modiﬁcations of the original CIM algorithm that attempt to overcome these two ﬂaws.[11,27–29] In each algorithm, the ﬁrst ﬂaw is
addressed by adding new degrees of freedom to the system, resulting in 2N (instead of only N) analog variables for N spins. In
SBM, this is done by including both a position vector, xi , and a
velocity/momentum vector, yi ; in the modiﬁed CIM algorithms,
by contrast, the auxiliary variable ei is added.
To address the second ﬂaw, the creators of dSBM added discretization and “inelastic walls,” whereas in CIM-CFC and CIMSFC this discretization is not necessary. Using diﬀerent mechanisms, all three algorithms ensure that the system only has ﬁxed
points at the local minima of the Ising Hamiltonian (during the
end of the trajectory), which is not true for the original CIM algorithm. Because these systems are fundamentally very similar, it
should not be surprising that they achieve similar performance.
We also note that, for dSBM to achieve good performance, it
is necessary to use discretization and inelastic walls, which make
the system discontinuous. This is particularly useful for implementation on a digital platform, in which discrete processes are
preferred; however, when implementing these algorithms on an
analog physical platform, it is not preferred. In the cases of CIMCAC, CIM-CFC, and CIM-SFC, the system evolves continuously,
making them much more suitable for analog implementation as
exempliﬁed by the optical CIM architecture proposed in this paper.
An interesting diﬀerence between the CIM and the original
bifurcation machine,[27] which was referred to as aSBM in ref.
[29], is that aSBM is a completely unitary dissipation-less system.
Because of this, aSBM relies on adiabatic evolution for computation (similar to quantum annealing); the dissipative CIM and
other Ising heuristics (such as simulated annealing or breakout
local search[14] ) , by contrast, rely on some sort of dissipative relaxation. However, the new SBM algorithms in ref. [29] deviate from
the concept of adiabatic evolution by adding inelastic walls, making the new bifurcation machine a dissipative system in which
information is lost over time. It would be interesting to attempt
to understand whether dissipation is in fact necessary for a system to achieve the high performance of the algorithms discussed
in this paper. For example, one could modify aSBM in a diﬀerent
manner that addresses the problem of amplitude heterogeneity
but retains the adiabatic nature. Whether this is possible is beyond the scope of this paper.

Figure F1. Optical implementation of CIM-SFC.

Adv. Quantum Technol. 2021, 4, 2100077

2100077 (20 of 21)

© 2021 The Authors. Advanced Quantum Technologies published by Wiley-VCH GmbH

25119044, 2021, 11, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/qute.202100077 by Nat Prov Indonesia, Wiley Online Library on [12/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

www.advancedsciencenews.com

www.advquantumtech.com

Appendix F: Optical Implementation of CIM-SFC
Figure F1 shows an optical implementation of CIM-SFC, which
is similar to that of CIM-CAC and CIM-CFC shown in Figure 6.
∑
The feedback signal z̃i = j Jij x̃j is deampliﬁed (rather than am̃ (m)

tanh(z )
pliﬁed) by PSAe with attenuation coeﬃcient z̃ (m)i , where z̃i (m)
i
is an optical homodyne measurement result of z̃i . This feedback
signal is then injected back into signal pulse xi in the main cavity
through BSi .
Part of the fan-in circuit output z̃i is delayed by a delay line
DLe with delay time N𝜏 and combined with the error pulse ei (inside the main cavity). This implements the term ei − z̃i in Equation (8). The term −𝛽(ei − z̃i ) on the right-hand side of Equation (8) is implemented by a phase-sensitive ampliﬁer PSAe in
the main cavity. This is also a deampliﬁcation process. Finally, the
error correction signal amplitude ei − z̃i is coupled to the signal
pulse xi inside the main cavity using a standard optical delay line.

Acknowledgements
The authors wish to thank R. Hamerly, M. G. Suh, M. Jankowski, E. Ng,
and Y. Inui for their valuable discussions.

Conﬂict of Interest
The authors declare no conﬂict of interest.

Data Availability Statement
Research data are not shared.

Keywords
coherent Ising machine, chaotic solution search, combinatorial optimization, matrix-vector multiplication, optical error correction
Received: June 6, 2021
Revised: August 17, 2021
Published online: September 7, 2021

[1] F. Barahona, J. Phys. A 1982, 15, 3241.
[2] M. W. Johnson, M. H. S. Amin, S. Gildert, T. Lanting, F. Hamze, N.
Dickson, R. Harris, A. J. Berkley, J. Johansson, P. Bunyk, E. M. Chapple, C. Enderud, J. P. Hilton, K. Karimi, E. Ladizinsky, N. Ladizinsky, T. Oh, I. Perminov, C. Rich, M. C. Thom, E. Tolkacheva, C. J. S.
Truncik, S. Uchaikin, J. Wang, B. Wilson, G. Rose, Nature 2011, 473,
194.

Adv. Quantum Technol. 2021, 4, 2100077

2100077 (21 of 21)

[3] S. Boixo, T. F. Rønnow, S. V. Isakov, Z. Wang, D. Wecker, D. A. Lidar,
J. M. Martinis, M. Troyer, Nat. Phys. 2014, 10, 218.
[4] A. Marandi, Z. Wang, K. Takata, R. L. Byer, Y. Yamamoto, Nat. Photonics 2014, 8, 937.
[5] T. Inagaki, K. Inaba, R. Hamerly, K. Inoue, Y. Yamamoto, H. Takesue,
Nat. Photonics 2016, 10, 415.
[6] P. L. McMahon, A. Marandi, Y. Haribara, R. Hamerly, C. Langrock,
S. Tamate, T. Inagaki, H. Takesue, S. Utsunomiya, K. Aihara, R. L.
Byer, M. M. Fejer, H. Mabuchi, Y. Yamamoto, Science 2016, 354,
614.
[7] T. Inagaki, Y. Haribara, K. Igarashi, T. Sonobe, S. Tamate, T. Honjo,
A. Marandi, P. L. McMahon, T. Umeki, K. Enbutsu, O. Tadanaga, H.
Takenouchi, K. Aihara, K. Kawarabayashi, K. Inoue, S. Utsunomiya,
H. Takesue, Science 2016, 354, 603.
[8] R. Hamerly, T. Inagaki, P. L. McMahon, D. Venturelli, A. Marandi,
T. Onodera, E. Ng, C. Langrock, K. Inaba, T. Honjo, K. Enbutsu, T.
Umeki, R. Kasahara, S. Utsunomiya, S. Kako, K. Kawarabayashi, R. L.
Byer, M. M. Fejer, H. Mabuchi, D. Englund, E. Rieﬀel, H. Takesue, Y.
Yamamoto, Sci. Adv. 2019, 5, eaau0823.
[9] K. Sankar, A. Scherer, S. Kako, S. Reifenstein, N. Ghadermarzy, W.
B. Krayenhoﬀ, Y. Inui, E. Ng, T. Onodera, P. Ronagh, Y. Yamamoto,
arXiv:2105.03528v1, 2021.
[10] Z. Wang, A. Marandi, K. Wen, R. L. Byer, Y. Yamamoto, Phys. Rev. A
2013, 88, 063853.
[11] T. Leleu, Y. Yamamoto, P. L. McMahon, K. Aihara, Phys. Rev. Lett. 2019,
122, 040607.
[12] T. Leleu, F. Khoyratee, T. Levi, R. Hamerly, T. Kohno, K. Aihara,
arXiv:2009.04084v3, 2020.
[13] M. Ercsey-Ravasz, Z. Toroczkai, Nat. Phys. 2011, 966, 970.
[14] U. Benlic, J. K. Hao, Eng. Appl. Artif. Intell. 2013, 26, 1162.
[15] C. Wang, C. Langrock, A. Marandi, M. Jankowski, M. Zhang, B. Desiatov, M. M. Fejer, M. Lončar, Optica 2018, 5, 1438.
[16] B. Stern, X. Ji, Y. Okawachi, A. L. Gaeta, M. Lipson, Nature 2018, 562,
401.
[17] C. Wang, M. Zhang, X. Chen, M. Bertrand, A. Shams-Ansari, S. Chandrasekhar, P. Winzer, M. Lončar, Nature 2018, 562, 101.
[18] P. D. Drummond, C W Gardiner, J. Phys. A 1980, 13, 2353.
[19] P. D. Drummond, C. W. Gardiner, D. F. Walls, Phys. Rev. A 1981, 24,
914.
[20] D. F. Walls, G. J. Milburn, Quantum Optics, Springer-Verlag, Berlin,
Heidelberg 2007.
[21] K. Takata, A. Marandi, Y. Yamamoto, Phys. Rev. A 2015, 92, 043821.
[22] D. Maruo, S. Utsunomiya, Y. Yamamoto, Phys. Scr. 2016, 91, 083010.
[23] Y. Inui, Y. Yamamoto, Phys. Rev. A 2020, 102, 062419.
[24] Y. Inui, Y. Yamamoto, Entropy 2021, 23, 624.
[25] E. Ng, T. Onodera, S. Kako, P. L. McMahon, H. Mabuchi, Y. Yamamoto, arXiv:2103.05629v1, 2021.
[26] A. D. King, W. Bernoudy, J. King, A. J. Berkley, T. Lanting,
arXiv:1806.08422v1, 2018.
[27] H. Goto, K. Tatsumura, A. R. Dixon, Sci. Adv. 2019, 5, eaav2372.
[28] K. Tatsumura, M. Yamasaki, H. Goto, Nat. Electron. 2021, 4, 208.
[29] H. Goto, K. Endo, M. Suzuki, Y. Sakai, T. Kanao, Y. Hamakawa, R.
Hidaka, M. Yamasaki, K. Tatsumura, Sci. Adv. 2021, 7, eabe795.
[30] Y. Inui, Y. Yamamoto, arXiv:2009.10328v1, 2020.
[31] S. Kako, T. Leleu, Y. Inui, F. Khoyratee, S. Reifenstein, Y. Yamamoto,
Adv. Quantum Technol. 2020, 3, 2000045.

© 2021 The Authors. Advanced Quantum Technologies published by Wiley-VCH GmbH

25119044, 2021, 11, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/qute.202100077 by Nat Prov Indonesia, Wiley Online Library on [12/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

www.advancedsciencenews.com

