entropy
Article

Quantum Mutual Information, Fragile Systems and Emergence
Yasmín Navarrete 1, *,†

and Sergio Davis 2,3,†
1
2

3

*
†

Instituto de Filosofía y Ciencias de la Complejidad, Los Alerces 3024 Ñuñoa, Santiago 7780192, Chile
Research Center in the Intersection of Plasma Physics, Matter and Complexity (P2 mc), Comisión Chilena de
Energía Nuclear, Casilla 188-D, Santiago 8320000, Chile
Departamento de Física, Facultad de Ciencias Exactas, Universidad Andres Bello, Sazié 2212 piso 7,
Santiago 8370136, Chile
Correspondence: yasmin.navarrete@gmail.com
These authors contributed equally to this work.

Abstract: In this paper, we present an analytical description of emergence from the density matrix
framework as a state of knowledge of the system, and its generalized probability formulation.
This description is based on the idea of fragile systems, wherein the observer modifies the system
by the measurement (i.e., the observer effect) in order to detect possible emergent behavior. We
propose the use of a descriptor, based on quantum mutual information, to calculate if subsystems of
systems have inner correlations. This may contribute to a definition of emergent systems in terms of
emergent information.
Keywords: emergence; quantum theory; density matrix; subadditivity

1. Introduction

Citation: Navarrete, Y.; Davis, S.
Quantum Mutual Information,
Fragile Systems and Emergence.
Entropy 2022, 24, 1676. https://
doi.org/10.3390/e24111676
Academic Editor: Masahito Hayashi
Received: 12 September 2022
Accepted: 11 November 2022
Published: 17 November 2022
Publisher’s Note: MDPI stays neutral
with regard to jurisdictional claims in
published maps and institutional affiliations.

Copyright: © 2022 by the authors.
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed under the terms and
conditions of the Creative Commons
Attribution (CC BY) license (https://
creativecommons.org/licenses/by/

From quantum mechanics, it is well known that any separable state belongs to a
composite space that can be factored into individual states from separate subspaces. One
state is said to be correlated if it is not separable. As a matter of fact, to determine if a state
is separable or not is not trivial and the problem is classed as NP-hard from the theory of
complex systems [1].
A density operator, in quantum mechanics, is used to describe the statistical state of
a quantum system. The usual meaning of it is that the eigenvalues are the probabilities
of finding a system in one state corresponding to the eigenvectors. In a physical sense,
we can see its elements as relative frequencies corresponding to an appropriate ensemble
of N identical copies of the system that are in several possible states under a certain
setup or preparation protocol. Thus, we have a superposition of quantum states |vi i with
probabilities pi (real numbers) satisfying ∑ pi = 1. However, it can be shown that the
density operator formalism can be recovered in a Bayesian formalism for noncommutative
expectations, wherein the system depends on the order of the measurements. This is
not restricted just to a quantum mechanical system, and can be understood under the
framework of what we have called a fragile system [2]. This operator provides a convenient
mean for describing quantum systems whose state is not completely known, it being
mathematically equivalent to a state vector approach [3,4].
By applying the entropy to the density matrix, we can obtain the degree of disinformation of the state of the system. The systems can be composed of subsystems and, using
the subadditivity property (the probability of the whole is less than that of its parts) [5],
it is possible to quantify if the entropy of the whole is less than that of its parts. Holzer
and De Meer [6] make a comparison between the information at the system level with the
information at a lower level. As they state, “this measure gives a high value of emergence
for systems with many dependencies (interdependent components) and a low value of
emergence for systems with few dependencies (independent components)”; therefore, the

4.0/).

Entropy 2022, 24, 1676. https://doi.org/10.3390/e24111676

https://www.mdpi.com/journal/entropy

Entropy 2022, 24, 1676

2 of 10

information of the whole is more than the information of the parts. In that sense, the
entropy can be a good parameter to measure a type of emergence in systems.
This paper is organized as follows. In Section 2, we talk about emergent systems and
its current definitions. In Section 3, we define fragile systems as ones that are modified
by the act of measurement because of the change in internal variables. In Section 4, we
introduce the density matrix formalism. In Section 5, we depict a mathematical formulation
of emergent systems within the density matrix formalism. In Section 6, we show a concrete
example of a subadditive system. Finally, we provide some concluding remarks in Section 7.
2. Emergent Systems
Several definitions of emergence exist, taking into account different aspects of their
origin or behavior. For instance, Peter Checkland [7] defines emergence as “the principle
that entities exhibit properties which are meaningful only when attributed to the whole,
not to its parts”. Emergent systems are structured in such a way that their components
interact, allowing for the structure of global patterns, depicted as a consequence of interrelations/correlations between subsystem elements, them being the result of complex and
self-organizing processes. This process may be triggered by an external stimulus.
There are basically three types of emergence: simple, weak and strong ones, described
as follows:
Simple emergence is composed by the combination of certain properties and relationships between elements in a non-linear behavior. For instance, in order to achieve the
flight of an airplane, we cannot consider the motors, the propulsion system and their
wings separately; all of these properties must be considered together because they are
interconnected and they have interrelations through which flight emerges. This type of
emergence can be predicted from the functioning of its parts and it is referred to as the
concept of synergy, which means interacting or working together [8].
Weak emergence describes the emergence of properties of systems that may be predictable (not completely) and also reducible. They can be reduced to basic rules at an initial
time. After a while, the behavior can be unpredictable, as is mentioned in chaos theory [9];
nevertheless, it is possible to make computational simulations about such systems because
of the knowledge of the basic rules. Weak emergence is the product of complex system
dynamics (i.e., non-linear behavior, spontaneous order and adaptation); an example of the
latter is cellular automaton, known as Conway’s Game of Life [10–12].
Strong emergence is a case of non-expected emergence, as well as weak emergence.
The difference lies in its non-reducible behavior, which appears just when the system is
running. As it is systematically determined by low-level attributes, it is not possible to
deduce it from the components at lower levels. The consciousness phenomenon is one
example of this type of emergence, and appears as a construction process. There is likely
no algorithm from the bottom up because it is a dynamical process evolving along time at
the highest level, with non-linear relations at the lower ones.
Another way of conceptualizing emergence is the separation of levels of complexity of
the system at different spatial or temporal scales [13].
Some main characteristics of strong emergence to consider are the following:
Non-reducible phenomenon: the global state of the emergent system cannot be explainable, and neither is it reducible to its sub-system components.
Downward causation: emergent high-level properties appear from a non-obvious consequence of low-level properties, but, at the same time, all processes at the lower
level of hierarchy are constrained by and act in coherence with the laws of the higher
level [14].
Wholeness: a phenomenon wherein a complex, interesting high-level function appears as
a result of combining low-level mechanisms in straightforward ways.

Entropy 2022, 24, 1676

3 of 10

Radical novelty emergence: a phenomenon wherein a system is designed according to
certain principles. Interesting unexpected properties arise from the behavior of
sub-system elements [15].
In general, emergent systems are common in nature and technology. One example of
the latter is the speed of a vehicle affected by the center of gravity, the driver skills, weather
and friction, among other attributes (in this case, we can predict the emergent property of
the speed from the relation between components, it being the case of weak emergence). It is
possible to find strong emergent properties in the consciousness phenomenon [16], human
body and social phenomena, among others. One important example is ’self-awareness’,
which is a result of the interconnection of neurons in the brain [17].
In the case of biological systems (as well as in the case of social phenomena), emergent
models are appropriate for describing those situations. We can observe the characteristics
mentioned regarding strong emergence: non-reducibility, radical novelty, wholeness and
downward causation.
The main aspect of biological emergent systems is that they may be observed from
inside them by the system (“from internal control of a system which might be fully controlled by an observer/controller architecture that is part of the system” [18]); this is in
concordance with the autopoiesis theory proposed by the Chilean biologists H. Maturana
and F. Varela [19] to define the self-maintaining chemistry of any living cell, which is under
the perspective of chemical organization theory used to formalize autopoietic structures,
“providing a basis to operationalize goals as an emergent process” [20]. When the measurement is affected by the observer, it is the case of what we will call a fragile system. In the
next section, we will go deeper into the concept.
3. Fragile Systems
In simple terms, a fragile system is one that is affected by the measurement [21]. This
distinguishes it from a non-fragile (classical) system, which is not modified upon observation.
Because any system (being fragile or not) possesses information, we will think of
a system as a “black box” that can be found in different internal states, which is to be
denoted by λ. In general, λ contains many degrees of freedom, but we will not make use of
that inner structure here. The internal state λ contains all of the information necessary to
describe any aspect of the system.
The crucial difference between a fragile system and a non-fragile one is that, in a fragile
system, access to the internal state λ is impossible, because it is precisely this internal state
that is modified by the measurement. As the modification of the state λ depends on the
details of the environment when carrying out the measurement (which we do not know
or control with accuracy), the outcome of a measurement is unavoidably stochastic, and a
mathematical formulation requires probability theory [22].
4. The Density Operator
In this section, we formulate the density matrix operator, as a previous concept, in
order to define emergent systems using the calculation of entropies.
The density operator is a positive semi-definite Hermitian operator of trace one. If A
is the matrix representation of an arbitrary observable Â, we can write


A =


a1
 a2 

 
 ..  a1 a2 · · · a N .
 . 
aN

(1)

Entropy 2022, 24, 1676

4 of 10

Hence, we have

···
···
..
.



A =

a1 a1
 a2 a1

 ..
 .


a1 a N
a2 a N 

.. 
. 

· · · aN aN

a N a1

where ai is the conjugate of the element ai , and, in the case of real numbers, the same
element. We can take the average of different measurements represented by different
matrices A of the same observable, and then normalize and diagonalize it; finally, we obtain
the density matrix of a mixture as below:
N

ρ̂ = ∑ pi |vihv|

(2)

i

where pi = P(λi | I ) and λi is obtained from the eigen-value problem λi |vi i = λi Â [21].
We can formulate the density matrix operator by the use of a complex Hilbert space
just as in Von Neumann’s formulation of quantum theory [23]. For this, we consider an
arbitrary orthonormal basis set |ni (n = 1, . . . , N) with hi | ji = δ(i, j), and define the density
operator [24] ρ̂ as
N

N

ρ̂ := ∑ ∑ ρij |i ih j|,

(3)

i =1 j =1

with ρij complex numbers. Imposing that ρ̂ is Hermitian, we see that the diagonal elements
ρii must be real and ρij = ρ ji . It is always possible to make a choice of such complex matrix
elements ρij so that they are proportional to the elements pij ; these are given by
ρij = hei |ρ̂ e j =


1 
[ pij + p ji ] + i [ pij − p ji ] ,
2η

(4)

where η = ∑i pii is a normalization factor that imposes Tr(ρ̂) = 1.
Pure and Mixed States
Consider an ensemble of measurements {|vi i}iN=1 . If the state vector is known [25],
the ensemble represents a pure state. Assuming that the system is in the state |vi, we can
expand it with respect to the eigenvector of a Hermitian operator Â as follows:

|vi =

∑ λ n | v n i,

(5)

n

Â|vi

= λ n | v i.

(6)

Finally, we can define a pure state by the following term [25]:
ρ̂ = |vihv|.

(7)

Because ρ̂2 = (|vihv|)(|vihv|) = |vi(hv|vi)hv| = ρ̂, we can distinguish a density
operator of a pure state by tracing; then, we have
 
Tr(ρ̂) = Tr ρ̂2 = 1.
(8)
When we cannot repeat exactly the same initial condition, because of the noise of the
system, we represent this situation in a mathematical formulation in terms of an operator
called a density matrix for mixed states. This is a superposition of pure states [26]:
ρ̂ = ∑ pi |vihv|,
i

(9)

Entropy 2022, 24, 1676

5 of 10

where the weights of each measurement satisfy the normalization condition ∑i pi = 1 .
Each pi is the probability of finding a system in a given pure state.
In contrast to a pure state, when we have a mixed-density matrix, the trace of the
square density matrix is given by the inequality
 
Tr ρ̂2 < 1.
(10)

Hence, Tr ρ̂2 , known as the degree of purity [25], can be used to distinguish between
pure and mixed states in a basis-independent manner.
5. Density Operator Formalism and Emergent Systems
Earlier work by Prokopenko et al. [13] has set the basis for a discussion of complexity,
self-organization and the emergence of classical systems in information-theoretical terms,
particularly in terms of Shannon entropy and mutual information.
Taking all of this into account, we will rephrase the earlier arguments in terms of the
(von Neumann) entropy of density matrices. However, first, let us review the behavior of
the information entropy (or Shannon entropy) for classical, correlated systems.
We adopt the Bayesian view by Jaynes [27] and others of the Shannon entropy related
to the information content of a model based on, in principle, subjective probabilities, but
consistent with known facts. Shannon entropy is then a measure of missing information in
a probabilistic model about some aspect of reality, and is therefore dependent of the state
of knowledge used to construct said model. For a state of knowledge I , where we ask an
arbitrary question with N possible answers, denoted by the proposition A1 , A2 , . . . , A N ,
the Shannon entropy is defined as
N

S(I) := − ∑ pi ln pi

(11)

i =1

where pi is the probability P( Ai |I) of the answer Ai being true under I . Please note that,
for two ‘observers’ with different states of knowledge I1 and I2 , the Shannon entropies
S(I1 ) and S(I2 ) that they assign to an unknown question will, in general, be different.
For instance, if the first observer knows that A1 is true, whereas the second only knows
that either A1 or A2 is true, then S(I1 ) = 0 because P( Ak |I1 ) = δ1k , but S(I2 ) > 0 because
0 < P( A1 |I2 ) < 1 and P( A2 |I2 ) = 1 − P( A1 |I2 ) > 0.
In the case where the question involves the unknown value of one or more variable,
the information entropy directly translates in terms of the probability distribution. For instance, for the joint probability distribution P( X, Y |I) of the variables X and Y under the
state of knowledge I , we have
SXY (I) := − ∑ ∑ P( x, y|I) ln P( x, y|I).
x

(12)

y

Using the product rule of probability,
P( x, y|I) = P(y| x, I) P( x |I),

(13)

this entropy can always be separated into two terms [28],
D
E
SXY (I) = SX (I) + SY | X ,
I

(14)

where the first term is the entropy of the variable X, and the second term,
D

SY | X

E
I

:= − ∑ P( x |I) ∑ P(y| x, I) ln P(y| x, I)
x

y

(15)

Entropy 2022, 24, 1676

6 of 10

is the expected value of the conditional entropy of Y given X. This conditional entropy
cannot be negative, it being the expected value of a non-negative quantity.
It is possible to extend the Bayesian idea of probabilities as degrees of belief constrained
on the available information to quantum systems [29,30]. Let ρ12 = ρ1 ⊗ ρ2 . We can obtain
the eigenvalues of ρ1 ai = {ρ1 }ii and ρ2 b j = {ρ2 }ii . Hence, the diagonal elements of ρ12
are given by all products of the form ai b j , where i = 1, ..., n1 and j = 1, ..., n2 . Here, n1 and
n2 are the dimensions of ρ1 and ρ2 , respectively; then:
S(ρ12 )

= − Tr(ρ12 ln ρ12 )

(16)

n1 n2


= − ∑ ∑ ( ai b j ) ln ai b j .
i =1 j =1

On the other hand, the sum of the entropy of each system is given by
n1
n2

S(ρ1 ) + S(ρ2 ) = − ∑ ai ln( ai ) − ∑ b j ln b j .

(17)

j =1

i =1

Thus, the entropy for an ensemble (ρ12 ) for which the subsystems are uncorrelated is
just equal to the sum of the entropies of the reduced ensembles for the subsystems. When
there are correlations, we should expect an inequality instead (called the subadditivity
property of entropy [5,31,32]), since, in this case, ρ12 contains additional information
concerning the correlations, which is not present in ρ1 and in ρ2 (those are the partial traces
of ρ12 , respectively), as in
S(ρ12 ) ≤ S(ρ1 ) + S(ρ2 ).
(18)
Given this inequality, we can use the mutual information formulation
I := S(ρ1 ) + S(ρ2 ) − S(ρ12 ),

(19)

such that I > 0 whenever there is subadditive behavior and I = 0 for additivity.
From Equation (19), we obtain a descriptor of weak emergency in systems that are
correlated. In these types of systems, new information emerges from the relation of its parts
in terms of correlations.
6. An Example of a Subadditive System
As is depicted in Equation (4), we can write the density matrix as follows:
ρij = hei |ρ̂ e j =


1 
[ pij + p ji ] + i [ pij − p ji ] .
2η

(20)

but where we now interpret pij as
pij = P(ei , e0j | I ),

(21)

η = ∑ pii

(22)

i

where primed states are states after a measurement.
Because of the marginalization rule, it must hold that

∑ pij = P(e0j | I )

for all j = 1, . . . , N,

(23)

∑ pij = P(ei | I )

for all i = 1, . . . , N

(24)

i

while, simultaneously,

j

Entropy 2022, 24, 1676

7 of 10

must be true. As an example, consider an abstract system composed of two integers, a and
b, such that a ∈ {1, 2, 3, 4} and b ∈ {1, 2, 3, 4}. Let us set the constraint I that a and b are
either both even or both odd; then, there are eight allowed states, namely
Γ1 : a = 1, b = 1,
Γ2 : a = 1, b = 3,
Γ3 : a = 3, b = 1,
Γ4 : a = 3, b = 3,

(25)

Γ5 : a = 2, b = 2,
Γ6 : a = 2, b = 4,
Γ7 : a = 4, b = 2,
Γ8 : a = 4, b = 4.
Let us now define the measurement M ( a, b) by


1 if a = b,



M ( a, b) := 2, if a > b,




3 if a < b.

(26)

such that the system undergoes the following transitions: Γ1 ↔ Γ4 , Γ5 ↔ Γ8 , Γ2 ↔ Γ6 and
Γ3 ↔ Γ7 . In this way, if the system has a = 3 and b = 1, that is, it is in the state Γ3 , and we
perform the measurement M, we will obtain a value M = 2 and the state will change to a0
= 4 and b0 = 2, that is, to Γ7 . This makes the system fragile regarding the measurement M,
with the integers a and b being the hidden variables of the system. Lastly, we will define the
parity of each integer as 0 if the number is odd, and 1 if it is even. In this way, there are
only four observable states, namely
s1 = (0, 0),
s2 = (0, 1),

(27)

s3 = (1, 0),
s4 = (1, 1),

where the first and second position of the tuple represent the parity bit of a and b, respectively. Of these states, only s1 and s4 are consistent with the constraint I . Considering the
allowed transitions, we have that

 1 if s ∈ {s1 , s4 } and s0 ∈ {s1 , s4 },
4
P(s, s0 |I) =
(28)
0 otherwise.
The matrix elements pij = P(s = si , s0 = s j |I) are given in Table 1, together with the
density matrix elements ρij . The latter are simply
ρij =


pij
1
pij + p ji + i [ pij − p ji ] =
= 2pij ,
2η
η

(29)

because η = ∑4i=1 pii = 21 . The states given by Equation (27) are equivalent to the ket
notation (|00i, |11i, |01i, |10i). The density matrix elements ρij correspond to the density
operator of a pure, but entangled state,
ρ̂ AB =


1
|00ih00| + |00ih11| + |11ih00| + |11ih11| = Φ+
2

Φ+

(30)

Entropy 2022, 24, 1676

8 of 10

with |Φ+ i as one of the Bell states,

1 
Φ+ := √ |00i + h11| .
2

(31)

Table 1. The set of joint probabilities pij = P(s = si , s0 = s j |I) (third column) for the fragile system
arising from the two-integer example described in Section 6. The fourth column shows the values of
the elements of the corresponding density matrix.

i

j

pij

ρij

1
1
1
1

1
2
3
4

1

⁄4
0
0
1
⁄4

1

2
2
2
2

1
2
3
4

0
0
0
0

0
0
0
0

3
3
3
3

1
2
3
4

0
0
0
0

0
0
0
0

4
4
4
4

1
2
3
4

1

⁄4
0
0
1
⁄4

1

⁄2
0
0
1
⁄2

⁄2
0
0
1
⁄2

The reduced density matrices are

1 1
ρA =
2 0

1 1
ρB =
2 0


0
,
1

0
.
1

Hence, ρ̂ AB 6= ρ̂ A ⊗ ρ̂ B , and the operator ρ̂ AB is not separable. The values of the von
Neumann entropy are S A = SB = ln 2 and S AB = 0, the latter being a pure state; therefore,
the system is subadditive. With this example, we have found a density operator that is not
only correlated but could describe an emergent system, since the entropy of the whole is
less than that of its parts.
7. Concluding Remarks
In this work, we reviewed the idea of emergence in the context of quantum mechanics
and fragile systems in order to detect emergent behavior in systems under the framework
of the density matrix theory. We proposed the mutual information as a descriptor of
emergence in fragile systems [21]. When the parameter I > 0, there is more information in
the whole than its parts; therefore, new information emerges as a result of the interaction of
the subsystems as correlations. We have presented a concrete example of an operator that
could describe a subadditive system.
We believe that this formulation may give some insights about adaptative, selfsustainable and interconnected models. In particular, we aim to describe how, in an
entangled system, the observer is part of the observation by being an inseparable element
of it; for instance, by considering the side effect that produces the act of measurement (i.e.,
the observer effect [33–35]).

Entropy 2022, 24, 1676

9 of 10

Author Contributions: Conceptualization, Y.N.; methodology, Y.N. and S.D.; software, S.D.; validation, Y.N. and S.D.; formal analysis, Y.N. and S.D.; writing—original draft preparation, Y.N. and
S.D.; writing—review and editing, Y.N. and S.D. All authors have read and agreed to the published
version of the manuscript.
Funding: This research was funded by ANID FONDECYT 1220651 grant.
Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: Not applicable.
Conflicts of Interest: The authors declare no conflict of interest.

References
1.
2.
3.
4.
5.
6.
7.
8.
9.
10.
11.
12.
13.
14.
15.
16.
17.
18.
19.
20.
21.
22.
23.
24.
25.
26.
27.
28.
29.
30.
31.
32.
33.

Gharibian, S. Strong NP-hardness of the quantum separability problem. Quantum Inf. Comput. 2010, 10, 343–360. [CrossRef]
Navarrete, Y.; Davis, S. Noncommutative Bayesian expectation and its connection to quantum theory. AIP Conf. Proc. 2022,
in press.
Warmuth, M.K.; Kuzmin, D. Bayesian generalized probability calculus for density matrices. Mach. Learn. 2010, 78, 63–101.
[CrossRef]
Warmuth, M.K.; Kuzmin, D. A Bayesian probability calculus for density matrices. arXiv 2014, arXiv:1408.3100.
Bhatia, R. Positive Definite Matrices; Princeton University Press: Princeton, NJ, USA, 2015.
Holzer, R.; de Meer, H. Methods for Approximations of Quantitative Measures in Self-Organizing Systems; Springer: Berlin/Heidelberg,
Germany, 2011; pp. 1–15.
Checkland, P. Systems Thinking, Systems Practice; John Wiley: Hoboken, NJ, USA, 1999.
Hitchins, D.K. Systems Engineering: A 21st Century Systems Methodology; John Wiley & Sons: Hoboken, NJ, USA, 2008.
Alligood, K.T.; Sauer, T.; Yorke, J.A.; Crawford, J.D. Chaos: An Introduction to Dynamical Systems; Springer: Berlin/Heidelberg,
Germany, 1997.
Hanson, J.E.; Crutchfield, J.P. Computational mechanics of cellular automata: An example. Physica D 1997, 103, 169–189.
[CrossRef]
Bak, P.; Chen, K.; Creutz, M. Self-organized criticality in the Game of Life. Nature 1989, 342, 780–782. [CrossRef]
Wolfram, S. A New Kind of Science; Wolfram Media Champaign: Champaign, IL, USA, 2002.
Prokopenko, M.; Boschetti, F.; Ryan, A.J. An information-theoretic primer on complexity, self-organization, and emergence.
Complexity 2009, 15, 11–28. [CrossRef]
Campbell, D.T. ‘Downward causation’ in hierarchically organised biological systems. In Studies in the Philosophy of Biology;
Springer: Berlin/Heidelberg, Germany, 1974; pp. 179–186.
Chalmers, D.J. The Conscious Mind: In Search of a Fundamental Theory; Oxford Paperbacks: Oxford, UK, 1996.
Varela, F.J. Neurophenomenology: A Methodological Remedy for the Hard Problem; Imprint Academic: Exeter, UK, 1996; Volume 3,
pp. 330–349.
Jackson, S.; Hitchins, D.; Eisner, H. What is the systems approach? Insight 2010, 13, 41–43. [CrossRef]
Schmeck, H.; Müller-Schloer, C.; Çakar, E.; Mnif, M.; Richter, U. Adaptivity and self-organization in organic computing systems.
ACM Trans. Auton. Adapt. Syst. 2010, 5, 1–32. [CrossRef]
Maturana, H.; Varela, E.G. De Máquinas y Seres Vivos; Editorial Universitaria: Santiago, Chile, 1973.
Veloz, T. Goals as Emergent Autopoietic Processes. Front. Bioeng. Biotechnol. 2021, 9, 720652. [CrossRef] [PubMed]
Navarrete, Y.; Davis, S. Fragile Systems. arXiv 2016, arXiv:1609.01972.
Paul, W.; Baschnagel, J. Stochastic Processes: From Physics to Finance; Springer International Publishing: Berlin/Heidelberg,
Germany, 2013.
Von Neumann, J. Mathematical Foundations of Quantum Mechanics; Princeton University Press: Princeton, NJ, USA, 1955.
Cohen-Tannoudji, C.; Diu, B.; Laloë, F. Quantum Mechanics; Wiley: Hoboken, NJ, USA, 2005.
Barnett, S.M. Quantum Information; OUP Oxford: Oxford, UK, 2009.
Nielsen, M.A.; Chuang, I.L. Quantum Computation and Quantum Information; Cambridge University Press: Cambridge, UK, 2000.
Jaynes, E.T. Probability Theory: The Logic of Science; Cambridge University Press: Cambridge, UK, 2003.
Cover, T.M.; Thomas, J.A. Elements of Information Theory; John Wiley and Sons: Hoboken, NJ, USA, 2006.
Schack, R.; Brun, T.A.; Caves, C.M. Quantum Bayes rule. Phys. Rev. A 2001, 64, 014305. [CrossRef]
Caves, C.M.; Fuchs, C.A.; Schack, R. Quantum probabilities as Bayesian probabilities. Phys. Rev. A 2002, 65, 22305. [CrossRef]
Hayashi, M. Quantum Information: An Introduction; Springer: Berlin/Heidelberg, Germany, 2006.
Wilde, M.M. Quantum Information Theory; Cambridge University Press: Cambridge, UK, 2013.
Dirac, P.A.M. The Principles of Quantum Mechanics; Clarendon Press: Oxford, UK, 1930.

Entropy 2022, 24, 1676

34.
35.

10 of 10

de Bianchi, M.S. The Observer Effect. Found. Sci. 2013, 18, 213–243. [CrossRef]
Rogala, M.; Dabrowski, P.; Kowalczyk, P.J.; Wlasny, I.; Kozlowski, W.; Busiakiewicz, A.; Karaduman, I.; Lipinska, L.; Baranowski,
J.M.; Klusek, Z. The observer effect in graphene oxide—How the standard measurements affect the chemical and electronic
structure. Carbon 2016, 103, 235–241. [CrossRef]

