Physics Letters A 529 (2025) 130091

Contents lists available at ScienceDirect

Physics Letters A
journal homepage: www.elsevier.com/locate/pla

Letter

Family of quantum mutual information in multiparty quantum systems
Asutosh Kumar a,b,∗
a Department of Physics, Gaya College, Rampur, Gaya 823001, India
b P.G. Department of Physics, Magadh University, Bodh Gaya 824234, India

A R T I C L E

I N F O

Communicated by M.G.A. Paris

A B S T R A C T
The characterization of information within a multiparty system is both signiﬁcant and complex. This paper
presents the concept of generalized conditional mutual information, along with a family of multiparty quantum
mutual information measures. We provide interpretations and delineate the properties of these concepts, while
also pointing out certain unresolved issues. The generalized conditional mutual information serves to encapsulate
the interdependencies and correlations among various components of a multiparty quantum system. Additionally,
various formulations of multiparty quantum mutual information contribute to a deeper comprehension of
classical, quantum, and total correlations. These insights have the potential to propel fundamental research in
the ﬁeld of quantum information theory.

1. Introduction
In our information-driven universe, information is the cornerstone of
communication, computation, and knowledge. Shannon in 1948 introduced the concept of mutual information which provided a framework for
quantifying the amount of information shared between two systems, revolutionizing classical information theory. Classical mutual information
𝐼(𝑋 ∶ 𝑌 ) = 𝐻(𝑋) + 𝐻(𝑌 ) − 𝐻(𝑋, 𝑌 ), where 𝐻(𝑋) is the Shannon entropy, measures the amount of information obtained about one random
variable through another random variable. It quantiﬁes the reduction in
uncertainty about one variable given knowledge of the other. In classical information theory [1], mutual information has diverse applications
in data compression, error correction, and channel capacity, making it
a fundamental tool in communication systems and coding theory.
This concept has now transcended into the quantum domain, playing a crucial role in quantum information theory [2–4] in particular.
Quantum mutual information (QMI) is a generalization of classical mutual information to quantum systems. The QMI of a bipartite quantum
state 𝜌𝐴𝐵 given by 𝐼(𝐴 ∶ 𝐵) = 𝑆(𝜌𝐴 ) + 𝑆(𝜌𝐵 ) − 𝑆(𝜌𝐴𝐵 ), where 𝑆(𝜌) is
the von Neumann entropy, quantiﬁes the total correlation [5,6], both
classical and quantum, between subsystems 𝐴 and 𝐵 . It serves as a measure of correlation beyond entanglement. QMI is essential in multiple
areas of quantum information processing like quantum communication,
quantum computing, and quantum cryptography [2–4]. It is especially
important in quantifying quantum channel capacities [7,8]. In quantum
machine learning [9,10], it quantiﬁes the information exchanged be-

tween various representations of quantum datasets. It is also signiﬁcant
as a probe for many-body localization [11], and in quantifying quantum
objectivity [12].
Understanding various correlations [13–16] in systems involving
more than two parties becomes increasingly important. Quantum entanglement and correlations are resources which may be shared among
multiple parties but with certain restrictions. Thus, in measuring correlations of multipartite systems, some inequalities on distribution of
correlations arise naturally–say, the monogamy inequalities [17–19].
Although the problem of entanglement generation and detection in
multipartite systems has been well studied [20–22], there still exist
interesting problems. For example, the formalism to distinguish quantum correlation from classical correlation is not straightforward. In the
present study, we consider quantum mutual information in multiparty
systems, provide interpretations of their quantiﬁers, and present some
inequalities.
In classical information theory, mutual information between multiple random variables can be straightforwardly extended. In the quantum
realm, however, correlations are more complex due to the exotic quantum phenomena such as nonlocality, superposition and measurement
problem. Multiparty quantum mutual information (MQMI) extends the
concept of bipartite QMI to systems with multiple parties, oﬀering insights into the intricate correlations that arise in quantum states. It seeks
to quantify the total correlations among several subsystems within a
quantum state, and has implications for understanding and leveraging
the correlations in multiparty quantum systems. Mutual information

* Correspondence to: Department of Physics, Gaya College, Rampur, Gaya 823001, India.
E-mail address: asutoshk.phys@gmail.com.
https://doi.org/10.1016/j.physleta.2024.130091
Received 2 September 2024; Received in revised form 17 November 2024; Accepted 19 November 2024
Available online 22 November 2024
0375-9601/© 2024 Elsevier B.V. All rights are reserved, including those for text and data mining, AI training, and similar technologies.

Physics Letters A 529 (2025) 130091

A. Kumar

and related measures [5,6,23–29] are famed measures of multipartite
information and correlation. The journey of mutual information from
classical to quantum domains underscores its profound elegance and
signiﬁcance. As quantum technologies continue to advance, the significance of mutual information in both the realms becomes increasingly
evident. The two main contributions of this paper are:

eigenvalues [2]. The QRE is monotonic under partial trace, completelypositive and trace-preserving (CPTP) maps, and positive maps [31,32].
Let  = {𝑋1 , 𝑋2 , ⋯ , 𝑋𝑛 }, [𝑛] = {1, 2, ⋯ , 𝑛}, and 𝟏 = 1 such that 𝑆(𝟏) = 0
and for any system 𝑋 , 𝜌𝑋 𝟏 = 𝜌𝑋 = 𝟏𝜌𝑋 . [One can alternatively consider 𝟏 = diag{1, 1, ⋯ , 1} with the requirement that its dimension is
self-adjusting!]

1. Concept of generalized conditional mutual information which is an
extension of the conditional entropy 𝑆(𝐴|𝐵) = 𝑆(𝜌𝐴𝐵 ) − 𝑆(𝜌𝐵 ) and
conditional mutual information 𝐼(𝐴 ∶ 𝐵|𝐶) = 𝑆(𝜌𝐴𝐶 ) + 𝑆(𝜌𝐵𝐶 ) −
𝑆(𝜌𝐶 ) − 𝑆(𝜌𝐴𝐵𝐶 ). This quantity can encapsulate every possible interdependency and correlation of any subsystem of a multiparty
system.
2. Introduction of a family of multiparty quantum mutual information. There are at least 𝑛 − 1 MQMI for an 𝑛 (≥ 2)-party quantum
system. Moreover, any positive linear combination of these MQMIs
is another MQMI. Some linear combinations of these MQMIs can
yield negative values.

2.2. Correlations and monotones
Let us consider a function 𝑓 (𝜌𝑋1 ⋯𝑋𝑛 ) deﬁned on 𝜌𝑋1 ⋯𝑋𝑛 and mention below some plausible and useful properties.
(P1) Symmetry: 𝑓 (𝜌𝑋1 ⋯𝑋𝑛 ) is symmetric under the interchange of any
two parties 𝑋𝑗 and 𝑋𝑘 .
(P2) Semipositivity: 𝑓 (𝜌𝑋1 ⋯𝑋𝑛 ) ≥ 0.
(P3) Vanishing on product states: 𝑓 (𝜌𝑋1 ⊗ ⋯ ⊗ 𝜌𝑋𝑛 ) = 0.
(P4) Monotonicity under some local operations [local (completely) positive maps].
(P5) Monotonicity under classical communications (public announcement or communication over phone).
(
)
(P6) Additivity: 𝑓 (𝜌 ⊗ 𝜎) = 𝑓 (𝜌) + 𝑓 (𝜎) and 𝑓 𝜌⊗𝑛 = 𝑛𝑓 (𝜌).
(P7) Continuity: 𝑓 (𝜌) is a continuous (smooth) function of its argument 𝜌.

It is evident that multiple expressions of MQMI arise due to diﬀerent ways of deﬁning and quantifying correlations in complex quantum
systems. Each expression may capture unique aspects of these correlations, leading to diverse applications and insights. A straightforward
consequence of multiple expressions of MQMI would be enhanced understanding of classical, quantum and total correlations. By providing a
multifaceted understanding of correlations in multiparty quantum systems, multiple expressions of MQMI can drive fundamental research
in quantum information theory. By providing diﬀerent perspectives on
correlations and their operational interpretations, we can explore new
theoretical models and deepen our understanding of quantum systems.
This paper is organized as follows. In Sec. 2, we consider the preliminaries such as notation and deﬁnitions. The notion of generalized
conditional mutual information which is the generalization of conditional
entropy and conditional mutual information to multiparty systems is
introduced in Sec. 3. In Sec. 4, we introduce a family of multiparty quantum mutual information and provide their interpretations and properties. We also speculate them to be secrecy monotones which are useful in
cryptography. Finally, we conclude and discuss some unresolved issues
in Sec. 5.

If 𝑓 satisﬁes (P2) semipositivity and (P3) vanishing on product density matrices, it is a measure of the amount of correlation between the
parties. A nonnegative correlation function that observes (P4) monotonicity under local operations and (P5) monotonicity under classical
communications is called a monotone. A secrecy monotone, in addition
to (P2–P5), satisﬁes (P6) additivity and (P7) continuity. If the secrecy
monotone is expected to measure the amount of information (secrecy)
shared by the communicating parties {𝑋1 , 𝑋2 , ⋯ , 𝑋𝑛 } with the hostile
party Eve, then the following properties are natural [33,34]:
(P8) Monotonicity under local operations by Eve.
(P9) Monotonicity under classical (public) communication by Eve.
Whether the information in question is correlation, monotone or secrecy monotone should be clear from its properties and the context.

2. Setup

3. Generalized conditional mutual information

2.1. Preliminaries

In this section, we introduce the notion of generalized conditional
mutual information (GCMI). It is the multiparty extension of conditional
entropy 𝑆(𝐴|𝐵) = 𝑆(𝐴𝐵) − 𝑆(𝐵) and conditional mutual information
𝐼(𝐴 ∶ 𝐵|𝐶) = 𝑆(𝐴𝐶) + 𝑆(𝐵𝐶) − 𝑆(𝐶) − 𝑆(𝐴𝐵𝐶). It can encompass every possible interdependency or correlation (interaction information) of
any subsystem of a multiparty system. We deﬁne the GCMI as the information contained in subsystems 𝑋𝑘1 𝑋𝑘2 ⋯ 𝑋𝑘𝑚 of a multiparty system
𝑋1 𝑋2 ⋯ 𝑋𝑛 (𝑛 ≥ 𝑚) but not in 𝑌 , where 𝑌 (acting as a single system) is
either 𝟏 or one or more remaining subsystems,

We consider a multiparty quantum system 𝑋1 𝑋2 ⋯ 𝑋𝑛 represented
𝑑

𝑑

𝑑

by ﬁnite dimensional density matrix 𝜌𝑋1 𝑋2 ⋯𝑋𝑛 ∈ 1 1 ⊗2 2 ⊗⋯ ⊗𝑛 𝑛 .
The reduced density matrix of subsystem 𝑋 is obtained by partial tracing
over the remaining subsystems 𝑋 : 𝜌𝑋 = tr𝑋 (𝜌𝑋𝑋 ). The von Neumann
entropy (in bits) given by

𝑆(𝜌) ∶= −tr(𝜌 log2 𝜌) = −
∑

∑
𝑖

𝜆𝑖 log2 𝜆𝑖 ,

(1)

𝐼(𝑋𝑘1 ∶ 𝑋𝑘2 ∶ ⋯ ∶ 𝑋𝑘𝑚 |𝑌 ) ∶= −𝑆(𝑌 )

where 𝜆𝑖 ≥ 0 and 𝑖 𝜆𝑖 = 1, is the quantum counterpart of Shannon
entropy. Shannon entropy is the average information content of a probability distribution. The von Neumann entropy satisﬁes the inequalities
[30,31]: 𝑆(𝜌𝑋 ) − 𝑆(𝜌𝑌 ) ≤ 𝑆(𝜌𝑋𝑌 ) ≤ 𝑆(𝜌𝑋 ) + 𝑆(𝜌𝑌 ) ≤ 𝑆(𝜌𝑋𝑍 ) + 𝑆(𝜌𝑌 𝑍 )
and 𝑆(𝜌𝑌 ) + 𝑆(𝜌𝑋𝑌 𝑍 ) ≤ 𝑆(𝜌𝑋𝑌 ) + 𝑆(𝜌𝑌 𝑍 ). We denote the von Neumann
entropy of subsystem 𝑋𝑖 𝑋𝑗 as 𝑆(𝜌𝑋𝑖 𝑋𝑗 ) ≡ 𝑆(𝑋𝑖 𝑋𝑗 ) ≡ 𝑆𝑖𝑗 , and so on.
𝑆(𝜌) = 0 for a pure quantum state. Another important entropy for our
purpose is quantum relative entropy (QRE) which measures the closeness
of two density matrices. It is deﬁned as

𝐷(𝜏||𝜎) ∶= 𝑡𝑟(𝜏 log2 𝜏) − 𝑡𝑟(𝜏 log2 𝜎),

+

𝑚
∑
(−1)𝑗+1
𝑗=1

∑
𝑘1 <⋯<𝑘𝑗 ∈[𝑚]

𝑆(𝑋𝑘1 𝑋𝑘2 ⋯ 𝑋𝑘𝑗 𝑌 ).

(3)

A few remarkable points about 𝐼(𝑋𝑘1 ∶ 𝑋𝑘2 ∶ ⋯ ∶ 𝑋𝑘𝑚 |𝑌 ) are as follows.
1. 𝐼(𝑋𝑘1 ∶ 𝑋𝑘2 |𝑌 ) ≥ 0. This follows from the strong subadditivity of
von Neumann entropy.
2. 𝐼(𝑋𝑘1 𝑋𝑘2 ⋯ 𝑋𝑘𝑚 |𝟏) = 𝑆(𝑋𝑘1 𝑋𝑘2 ⋯ 𝑋𝑘𝑚 ).
3. 𝐼(𝑋1 ∶ 𝑋2 ∶ ⋯ ∶ 𝑋𝑛 |𝟏) is the information (correlation) common to
subsystems 𝑋1 , 𝑋2 , ⋯, and 𝑋𝑛 .
4. It can assume negative values [35–39].

(2)

if 𝑠𝑢𝑝𝑝(𝜏) ⊆ 𝑠𝑢𝑝𝑝(𝜎), and inﬁnity otherwise. The support of a Hermitian
matrix is the Hilbert space spanned by its eigenvectors with nonzero
2

Physics Letters A 529 (2025) 130091

A. Kumar

tems 𝐴 and 𝐵 [5,6], satisﬁes the Araki-Lieb inequality 𝐼(𝐴 ∶ 𝐵) ≤
2 min{𝑆(𝜌𝐴 ), 𝑆(𝜌𝐵 )} [30], is invariant under local unitary operations,
and is nonincreasing under tracing out a subsystem. Here we introduce
a family of entropic functions constructed on 𝜌𝑋1 ⋯𝑋𝑛 , and show below
that they serve as 𝑛-party quantum mutual information.
4.1. Deﬁnition
We deﬁne the 𝑘𝑡ℎ (1 ≤ 𝑘 ≤ 𝑛) multiparty quantum mutual information on 𝜌𝑋1 ⋯𝑋𝑛 as

𝑀𝑘(𝑛) (𝑋1 ∶ 𝑋2 ∶ ⋯ ∶ 𝑋𝑛 )

Fig. 1. (a) Two-variable and (b) three-variable Venn diagrams with possible intersecting regions and generalized conditional mutual information. Here
𝑆(𝑋) ≡ 𝐼(𝑋|𝟏) is the information content of subsystem 𝑋 , the information contained in subsystem 𝑋 but not in subsystem 𝑌 is given by the conditional entropy
𝑆(𝑋|𝑌 ) = 𝑆(𝑋𝑌 ) − 𝑆(𝑌 ) = 𝑆(𝑋) − 𝐼(𝑋 ∶ 𝑌 ) ≡ 𝐼(𝑋|𝑌 ), and 𝐼(𝑋 ∶ 𝑌 ) is the information between 𝑋 and 𝑌 .

∶=

∑

𝑗1 <⋯<𝑗𝑘 ∈[𝑛]

(

)
𝑛−1
𝑆(𝑋1 ⋯ 𝑋𝑛 ).
𝑘−1

𝑆(𝑋𝑗1 ⋯ 𝑋𝑗𝑘 ) −
(𝑛)

The superscript “𝑛” in 𝑀𝑘

(4)

denotes the number of subsystems (sin-

gle or composite) separated by colons, and the coeﬃcients

(𝑛−1)

for

𝑘−1
given 𝑛 constitute the 𝑛𝑡ℎ -row of the Pascal’s triangle. We posit a few

In the above, 𝐼(𝑋|𝟏) ≡ 𝐼(𝑋), 𝐼(𝑋1 ∶ 𝑋2 ∶ 𝑋3 |𝟏) ≡ 𝐼(𝑋1 ∶ 𝑋2 ∶ 𝑋3 ),
and so on. In multiparty systems, however, we prefer to keep the notation 𝐼(𝑋|𝟏) rather than 𝐼(𝑋) to remind us the fact that either 𝐼(𝑋) ≡
𝐼(𝑋|𝟏) = −𝑆(𝟏) + 𝑆(𝑋) is analogous to conditional information or 𝐼(𝑋)
is not a multiparty (total) correlation.
The nontriviality in characterization of information and correlations
begins to emerge with three-party system onwards. We illustrate the
idea of GCMI using the tripartite system 𝐴𝐵𝐶 represented by density
matrix 𝜌𝐴𝐵𝐶 [see Fig. 1(b)].

remarks here. First, the choice of deﬁnition in Eq. (4) is motivated by
the fact that the two well-established MQMI [28,33] in the literature are
members of this family. Second, this multiparty quantum mutual information contains all two and more parties interactions, as described in
[28], and not just the 𝑛-party interaction 𝐼(𝑋1 ∶ 𝑋2 ∶ ⋯ ∶ 𝑋𝑛 |𝟏). Third,
𝑀1(2) (𝑋 ∶ 𝑌 ) = 𝐼(𝑋 ∶ 𝑌 ) = 𝐼(𝑋 ∶ 𝑌 |𝟏).
For 𝑝 + 𝑞 = 𝑛, one can consider 𝑝-party versus 𝑞 -party partitions of
 such that

1. Information in 𝐴 is [𝑎 + 𝑎𝑏 + 𝑎𝑐 + 𝑎𝑏𝑐] = 𝑆(𝜌𝐴 ) ≡ 𝐼(𝐴|𝟏).
2. Information in 𝐴 but neither in 𝐵 nor in 𝐶 (i.e., information strictly
contained in 𝐴) is [𝑎] = −𝑆(𝜌𝐵𝐶 ) + 𝑆(𝜌𝐴𝐵𝐶 ) ≡ 𝐼(𝐴|𝐵𝐶).
3. Information in 𝐴 (and possibly in 𝐵 ) but not in 𝐶 is [𝑎 + 𝑎𝑏] =
−𝑆(𝜌𝐶 ) + 𝑆(𝜌𝐴𝐶 ) ≡ 𝐼(𝐴|𝐶).
4. Information common to 𝐴 and 𝐵 (and possibly in 𝐶 ) is [𝑎𝑏 + 𝑎𝑏𝑐] =
𝑆(𝜌𝐴 ) + 𝑆(𝜌𝐵 ) − 𝑆(𝜌𝐴𝐵 ) ≡ 𝐼(𝐴 ∶ 𝐵|𝟏).
5. Information common to 𝐴 and 𝐵 but not in 𝐶 is [𝑎𝑏] = −𝑆(𝜌𝐶 ) +
𝑆(𝜌𝐴𝐶 ) + 𝑆(𝜌𝐵𝐶 ) − 𝑆(𝜌𝐴𝐵𝐶 ) ≡ 𝐼(𝐴 ∶ 𝐵|𝐶).
6. Information common to 𝐴, 𝐵 and 𝐶 is [𝑎𝑏𝑐] = 𝑆(𝜌𝐴 ) + 𝑆(𝜌𝐵 ) +
𝑆(𝜌𝐶 ) − 𝑆(𝜌𝐴𝐵 ) − 𝑆(𝜌𝐴𝐶 ) − 𝑆(𝜌𝐵𝐶 ) + 𝑆(𝜌𝐴𝐵𝐶 ) ≡ 𝐼(𝐴 ∶ 𝐵 ∶ 𝐶|𝟏).
7. Information in 𝐴𝐵𝐶 (as a single system) is 𝑆(𝜌𝐴𝐵𝐶 ) ≡ 𝐼(𝐴𝐵𝐶|𝟏).

∑

𝑀𝑝(𝑛) + 𝑀𝑞(𝑛) =

(
)
𝐼 𝜌𝑘 ∶ 𝜌 𝑘 .

(5)

𝑘𝑘∈{𝑝|𝑞 𝑝𝑎𝑟𝑡𝑖𝑡𝑖𝑜𝑛𝑠 𝑜𝑓 }
(𝑛)

See Appendix A for more relations between 𝑀𝑘 .
The existence of several expressions for multiparty quantum mutual
information can have profound consequences and diverse applications
in quantum information theory and technology. As research in this area
continues to evolve, the insights gained from multiple MQMI measures
will be instrumental in unlocking the full potential of quantum information science. The following observations, for instance, merit attention.
(𝑛)

1. 𝑀𝑘 are independent multiparty quantum mutual information. As
these yield distinct values for an arbitrary state, the parties must
make a priori choice about which multiparty correlation they want
to consider. This a priori choice should be obvious (self-revealing)
once their interpretations are known.
2. To maximize their correlation, parties should consider the quantity
𝑀𝑘(𝑛) where 𝑘 = 𝑛∕2 (for even 𝑛) or 𝑘 = (𝑛 ± 1)∕2 (for odd 𝑛). For

Indeed, there are several possibilities. Diﬀerent arrangements or conﬁgurations of subsystems yield, in general, diﬀerent values of information or correlation.
8. Three-party total correlations amongst 𝐴, 𝐵 and 𝐶 are given by

(𝑛)

(𝑛)

minimal correlation, 𝑀1 and 𝑀𝑛−1 are good candidates.
3. Corresponding to this family of multiparty quantum mutual information, one can introduce a family of multiparty quantum discord.
Discord is the diﬀerence between unmeasured total correlation and
measured total correlation present in a quantum state.
4. Information deviation due to a map or channel Φ (this may include
noise) acting on a multiparty quantum state 𝜌 is |(Φ(𝜌)) − (𝜌)|,
(𝑛)
where  is either 𝑀𝑘 , 𝑀 (𝑛) , 𝐶 (𝑛) , or generalized conditional mutual information.
5. Suppose the eavesdropper 𝐸 interacts with the system 𝜌𝐴𝐵 . Then,
the desirable condition for the secure secret sharing of information
between 𝐴 and 𝐵 is that the sum of correlations of 𝐸 with 𝐴 and
𝐵 should be minimal (refer to Fig. 1(b) with 𝐸 in place of 𝐶 ). That
is,

𝑇3 (𝐴 ∶ 𝐵 ∶ 𝐶) = 𝑆(𝜌𝐴 ) + 𝑆(𝜌𝐵 ) + 𝑆(𝜌𝐶 ) − 𝑆(𝜌𝐴𝐵𝐶 )
=𝐷(𝜌𝐴𝐵𝐶 ∥ 𝜌𝐴 ⊗ 𝜌𝐵 ⊗ 𝜌𝐶 )
=𝐼(𝐴 ∶ 𝐵𝐶) + 𝐼(𝐵 ∶ 𝐶)
=𝐼(𝐴 ∶ 𝐵|𝐶) + 𝐼(𝐴 ∶ 𝐶|𝐵) + 𝐼(𝐵 ∶ 𝐶|𝐴) + 2𝐼(𝐴 ∶ 𝐵 ∶ 𝐶|𝟏),
and

𝑆3 (𝐴 ∶ 𝐵 ∶ 𝐶) = 𝑆(𝜌𝐴𝐵 ) + 𝑆(𝜌𝐴𝐶 ) + 𝑆(𝜌𝐵𝐶 ) − 2𝑆(𝜌𝐴𝐵𝐶 )
=𝐼(𝐴 ∶ 𝐵𝐶) + 𝐼(𝐵 ∶ 𝐶|𝐴)
=𝐼(𝐴 ∶ 𝐵|𝐶) + 𝐼(𝐴 ∶ 𝐶|𝐵) + 𝐼(𝐵 ∶ 𝐶|𝐴) + 𝐼(𝐴 ∶ 𝐵 ∶ 𝐶|𝟏)
=𝑆(𝜌𝐴𝐵𝐶 ) − 𝐼(𝐴|𝐵𝐶) − 𝐼(𝐵|𝐴𝐶) − 𝐼(𝐶|𝐴𝐵).

𝐼(𝐴 ∶ 𝐸|𝐵) + 𝐼(𝐵 ∶ 𝐸|𝐴) + 𝐼(𝐴 ∶ 𝐵 ∶ 𝐸)

4. Family of MQMI

=𝑀2(3) (𝐴 ∶ 𝐵 ∶ 𝐸) − 𝐼(𝐴 ∶ 𝐵|𝐸)

The bipartite QMI 𝐼(𝐴 ∶ 𝐵) = 𝑆(𝐴) + 𝑆(𝐵) − 𝑆(𝐴𝐵) is the measure of total correlation (classical and quantum) between subsys-

=𝐼(𝐴𝐵 ∶ 𝐸) → 0.
3

(6)

Physics Letters A 529 (2025) 130091

A. Kumar

A more stringent condition would be that each of 𝐼(𝐴 ∶ 𝐸|𝐵), 𝐼(𝐵 ∶
𝐸|𝐴), and 𝐼(𝐴 ∶ 𝐵 ∶ 𝐸) is either zero or tends to zero.
∑
(𝑛)
(𝑛)
6. 𝑀𝑘 together with 𝑘 𝑐𝑘 𝑀𝑘 can be used to distinguish quantum
states.

Table 1
(𝑛)
Values of multiparty quantum mutual information 𝑀𝑘 and common infor(𝑛)
of generalized Greenberger-Horne-Zeilinger states |𝑔𝐺𝐻𝑍𝑛 ⟩ =
mation 𝐶
√
√
∑
⊗𝑛−𝑟
𝑝 |0⟩⊗𝑛 + 𝑒𝑖𝜙 1 − 𝑝 |1⟩⊗𝑛 , Dicke states |𝐷𝑛𝑟 ⟩ = √1 𝑛
|1⟩⊗𝑟 ],
 [|0⟩

(𝑟)

1

three-qutrit totally antisymmetric state |𝜓𝑎𝑠 ⟩ = √ (|123⟩ − |132⟩ + |231⟩ −

The various equivalent expressions of two eminent MQMIs [28,33]
are:

𝑇𝑛 (𝑋1 ∶ 𝑋2 ∶ ⋯ ∶ 𝑋𝑛 ) ≡ 𝑀1(𝑛) (𝑋1 ∶ 𝑋2 ∶ ⋯ ∶ 𝑋𝑛 )
𝑛
∑

|1100⟩ − |1111⟩), and |𝐻𝑆4 ⟩ = √1 (|0011⟩ + |1100⟩ + 𝜔(|1010⟩ + |0101⟩) +
6

𝜔2 (|1001⟩ + |0110⟩)). Here ℎ(𝑝) ∶= −𝑝 log2 𝑝 − (1 − 𝑝) log2 (1 − 𝑝) is the binary
2𝜋𝑖

𝑆(𝜌𝑋𝑘 ) − 𝑆(𝜌𝑋1 ⋯𝑋𝑛 )

(7)

=𝐷(𝜌𝑋1 ⋯𝑋𝑛 ∥ 𝜌𝑋1 ⊗ ⋯ ⊗ 𝜌𝑋𝑛 )

(8)

=

𝑘=1

=

=

𝑛−1
∑
𝑘=1
𝑛
∑

𝐼(𝑋𝑘 ∶ 𝑋𝑘+1 ⋯ 𝑋𝑛 )
∑

(𝑗 − 1)

𝑗=2

𝑘1 <⋯𝑘𝑗 ∈[𝑛]

6

|213⟩ + |312⟩ − |321⟩), four-qubit cluster state |𝐶4 ⟩ = 12 (|0000⟩ + |0011⟩ +

entropy, 𝜔 = 𝑒 3 , and “×” stands for not applicable. Note that 𝐶 (𝑛) can be negative and 𝐶 (𝑛=𝑜𝑑𝑑) vanishes for pure states.

(9)

𝐼(𝑋𝑘1 ∶ ⋯ ∶ 𝑋𝑘𝑗 |𝑋𝑘𝑗+1 ⋯ 𝑋𝑘𝑛 ),

(10)

and
(𝑛)
𝑆𝑛 (𝑋1 ∶ 𝑋2 ∶ ⋯ ∶ 𝑋𝑛 ) ≡ 𝑀𝑛−1
(𝑋1 ∶ 𝑋2 ∶ ⋯ ∶ 𝑋𝑛 )

=

𝑛
∑
𝑘=1

𝑆(𝜌𝑋1 ⋯𝑋𝑘−1 𝑋𝑘+1 ⋯𝑋𝑛 ) − (𝑛 − 1)𝑆(𝜌𝑋1 ⋯𝑋𝑛 )

=𝐼(𝑋1 ∶ 𝑋2 ⋯ 𝑋𝑛 ) +
=

𝑛
∑

∑

𝑗=2 𝑘1 <⋯𝑘𝑗 ∈[𝑛]

=𝑆(𝜌𝑋1 ⋯𝑋𝑛 ) −

𝑛−1
∑
𝑘=2

𝐼(𝑋𝑘 ∶ 𝑋𝑘+1 ⋯ 𝑋𝑛 |𝑋1 ⋯ 𝑋𝑘−1 )

𝐼(𝑋𝑘1 ∶ ⋯ ∶ 𝑋𝑘𝑗 |𝑋𝑘𝑗+1 ⋯ 𝑋𝑘𝑛 )

𝑛
∑
𝑘=1

(11)

State

𝑀1(𝑛)

𝑀2(𝑛)

𝑀3(𝑛)

𝑀4(𝑛)

𝐶 (𝑛)

|𝑔𝐺𝐻𝑍2 ⟩

2 ℎ(𝑝)

|𝑔𝐺𝐻𝑍3 ⟩
|𝐷31 ⟩
|𝜓𝑎𝑠 ⟩

3 ℎ(𝑝)
2.75489
4.75489

0

×

×

2 ℎ(𝑝)

3 ℎ(𝑝)
2.75489
4.75489

0
0
0

×
×
×

0
0
0

|𝑔𝐺𝐻𝑍4 ⟩
|𝐷41 ⟩
|𝐷42 ⟩
|𝐶4 ⟩
|𝐻𝑆4 ⟩

4 ℎ(𝑝)
3.24511
4
4
4

6 ℎ(𝑝)
6
7.50978
10
10.75489

4 ℎ(𝑝)
3.24511
4
4
4

0
0
0
0
0

2 ℎ(𝑝)
0.490225
0.490225
-2
-2.75489

|𝑔𝐺𝐻𝑍5 ⟩
|𝐷51 ⟩
|𝐷52 ⟩

5 ℎ(𝑝)
3.60964
4.85475

10 ℎ(𝑝)
9.70951
12.95462

10 ℎ(𝑝)
9.70951
12.95462

5 ℎ(𝑝)
3.60964
4.85475

0
0
0

(𝑛)

(𝑛)

(12)

or operational meaning like 𝑀1 and 𝑀𝑛−1 . Therefore, any operational
interpretation of these mutual information would be appreciated.

(13)

4.3. Properties
(𝑛)

𝐼(𝑋𝑘 |𝑋𝑘 ).

Here we discuss a number of useful properties that 𝑀𝑘 satisfy.

(14)

(𝑛)

1. 𝑀𝑘 is invariant under local unitary operations because von Neumann entropy is invariant under unitary operations.
(𝑛)
(𝑛)
2. 𝑀1 = 𝑇𝑛 and 𝑀𝑛−1 = 𝑆𝑛 satisfy the following properties [28,
33]: (P1–P9) above, (P10) 𝑆𝑛 = 𝑇𝑛 for pure states, and (P11)
𝑆𝑛 (𝜌𝑋1 𝑋2 ⋯𝑋𝑛 ) ≤ 𝑇𝑛 (𝜌𝑋1 𝑋2 ⋯𝑋𝑛 ) + 2𝑆(𝜌𝑋1 𝑋2 ⋯𝑋𝑛 ).

Both 𝑇𝑛 and 𝑆𝑛 measure both the classical and the quantum correlations.
𝑇𝑛 and 𝑆𝑛 are referred to as “total correlation” [5,23] and “dual total correlation” [24,25] respectively, quantum secrecy monotones [33],
and multiparty quantum mutual information [28] from the informationtheoretic point of view.
(𝑛)
We further ﬁnd that 𝑀𝑘 , for ﬁxed 𝑘 (1 ≤ 𝑘 < 𝑛), is nondecreasing
under discarding of any one party or grouping together any two parties
(see Appendix B). That is,

𝑀𝑘(𝑛) (𝑋1 ∶ ⋯ ∶ 𝑋𝑛 ) ≥ 𝑀𝑘(𝑛−1) (𝑋1 ∶ ⋯ ∶ 𝑋𝑛−1 ),

(15)

𝑀𝑘(𝑛) (𝑋1 ∶ ⋯ ∶ 𝑋𝑛 ) ≥ 𝑀𝑘(𝑛−1) (𝑋1 ∶ ⋯ ∶ 𝑋𝑛−1 𝑋𝑛 ).

(16)

(𝑛)

3. 𝑀𝑛 = 0 (as expected) because (𝑋1 𝑋2 ⋯ 𝑋𝑛 ) as a single system has
no mutual information.
(𝑛)
4. Suppose 1 ≤ 𝑝, 𝑞 ≤ 𝑛 − 1 such that 𝑝 ≠ 𝑞 and 𝑝 + 𝑞 = 𝑛. Then 𝑀𝑝 =

𝑀𝑞(𝑛) for pure states and hence can be called “dual” to each other.
(𝑛)

We envisage from Table 1 that for pure states the proﬁle of 𝑀𝑘
versus 𝑘 is analogous to a truncated Gaussian (a point or a straight
line being the particular case).
(𝑛)
5. 𝑀𝑘 satisfy (P1) symmetry, (P3) vanishing on product states, (P6)
additivity and (P7) continuity. These properties are also satisﬁed by
(𝑛)
any quantity which is a linear combination of 𝑀𝑘 . In particular,

4.2. Interpretations
(𝑛)

Interpretations of 𝑇𝑛 = 𝑀1 .– From Eq. (8), 𝑇𝑛 is interpreted as the
minimal relative entropy between 𝜌𝑋1 ⋯𝑋𝑛 and a product density matrix
𝜎𝑋1 ⊗ ⋯ ⊗ 𝜎𝑋𝑛 (the minimum being attained when 𝜎𝑋𝑘 = 𝜌𝑋𝑘 ). From
Eq. (9), 𝑇𝑛 is the sum of decorrelation costs when the parties decorrelate
themselves locally one by one from the rest using 𝐼(𝑋𝑘 ∶ 𝑋𝑘+1 ⋯ 𝑋𝑛 )
bits of randomness [5]. From Eq. (10), 𝑇𝑛 is the sum of (𝑗 − 1)-times all
(𝑗 ≥ 2)-party interactions.
(𝑛)
Interpretations of 𝑆𝑛 = 𝑀𝑛−1 .– 𝑆𝑛 like 𝑇𝑛 , from Eq. (12), can be
interpreted as the sum of decorrelation costs when the parties decorrelate themselves locally one by one from the rest using 𝐼(𝑋𝑘 ∶
𝑋𝑘+1 ⋯ 𝑋𝑛 |𝑋1 ⋯ 𝑋𝑘−1 ) bits of randomness. 𝑆𝑛 , using Eq. (13), is the
sum of all interactions of two and more parties only once [28]. Equivalently, from Eq. (14), it is the entropy of the whole system less the sum
of information in nonintersecting regions.
(𝑛)
Nevertheless, while all 𝑀𝑘 can be viewed as the sum of two and
more parties interactions, not all of them have straightforward physical

𝑀 (𝑛) (𝑋1 ∶ 𝑋2 ∶ ⋯ ∶ 𝑋𝑛 )
=

𝑛
∑
𝑘=1

𝜆𝑘 𝑀𝑘(𝑛) (𝑋1 ∶ 𝑋2 ∶ ⋯ ∶ 𝑋𝑛 ),
∑

(17)
(𝑛)

where 𝜆𝑘 ≥ 0 and 𝑘 𝜆𝑘 = 1. We conjecture below that 𝑀𝑘 and
𝑀 (𝑛) are plausible candidates for secrecy monotones. Another im(𝑛)
portant linear combination of 𝑀𝑘 is

𝐶 (𝑛) (𝑋1 ∶ 𝑋2 ∶ ⋯ ∶ 𝑋𝑛 )
=

𝑛
∑

(−1)𝑘+1 𝑀𝑘(𝑛) (𝑋1 ∶ 𝑋2 ∶ ⋯ ∶ 𝑋𝑛 ),

𝑘=1

=𝐼(𝑋1 ∶ 𝑋2 ∶ ⋯ ∶ 𝑋𝑛 |𝟏).
4

(18)

Physics Letters A 529 (2025) 130091

A. Kumar

(𝑛)
(𝑛)
and 𝑀𝑛−1 , the inter(𝑛)
pretation of other measures 𝑀𝑘 remains unclear. Therefore, some op-

𝐶 (𝑛) is the information (correlation) common to all 𝑋𝑘 s. It can, however, be negative (see Table 1). Moreover, it vanishes identically for
pure odd-party quantum states:
𝐶

(𝑛=odd)

∑

=

𝑘=odd

𝑀𝑘(𝑛) −

∑
𝑘=even

𝑀𝑘(𝑛) = 0.

(𝑛)

While various interpretations exist for 𝑀1

erational interpretations of these mutual information measures would
be beneﬁcial. Additionally, we conjecture that the remaining measures
∑
∑
𝑀𝑘(𝑛) and 𝑀 (𝑛) = 𝑘 𝜆𝑘 𝑀𝑘(𝑛) , where 𝜆𝑘 ≥ 0 and 𝑘 𝜆𝑘 = 1, will exhibit monotonicity under local operations and classical communication,
thereby qualifying as secrecy monotones. We also posit that our formalism will be instrumental in characterizing measures of multiparty
nonclassical correlations.

(19)

(𝑛)

6. For pure states, 𝐶 (𝑛) ≤ 𝑀𝑘 = 𝑀𝑛−𝑘 . For mixed states, we expect
them to obey the inequality:

)
(
(𝑛)
𝐶 (𝑛) ≤ 𝑀1(𝑛) ≈ 𝑀𝑛−1
)
(
(𝑛)
(𝑛)
< ⋯ < 𝑀𝑛∕2
.
< 𝑀2(𝑛) ≈ 𝑀𝑛−2
We also surmise that for 𝑘1 < 𝑘2 ≤ 𝑛∕2 and 𝑐 ≥ 𝑐𝑘2 ,𝑘1 =

𝑐𝑀𝑘(𝑛) ≥ 𝑀𝑘(𝑛) .
1

2

CRediT authorship contribution statement
(20)
Asutosh Kumar: Writing – review & editing, Writing – original draft,
Investigation, Formal analysis, Conceptualization.

𝑘2 (𝑘𝑛 )

2
,
𝑘1 (𝑘𝑛 )
1

Declaration of competing interest

(21)

The authors declare that they have no known competing ﬁnancial
interests or personal relationships that could have appeared to inﬂuence
the work reported in this paper.

(𝑛)

7. 𝑀𝑘 (𝑋1 ∶ 𝑋2 ∶ ⋯ ∶ 𝑋𝑛 ) in Eq. (4) is semipositive.
Proof. It is obvious for pure states because 𝑆(𝑋1 𝑋2 ⋯ 𝑋𝑛 ) vanishes
(𝑛)
(𝑛)
identically. For mixed states, the semipositivity of 𝑀1 , 𝑀𝑛−1 , and

(𝒏)
𝒌

Appendix A. Relations between 𝑴

(𝑛)
𝑀𝑘=𝑛∕2
(for even 𝑛) follows from Eqs. (8), (9), Eq. (12), and Eq. (5)
(𝑛)
respectively. In general, 𝑀𝑘 is semipositive because it is nondecreas(𝑛)
(𝑛−1)
ing under discarding a subsystem: 𝑀𝑘 ≥ 𝑀𝑘
≥ ⋯ ≥ 𝑀𝑘(𝑘) = 0 [see
(𝑛)
Eq. (15)]. 𝑀𝑘 can also be shown nonnegative using the subadditivity

1. The recurrence relation(s) for 𝑇𝑛 and 𝑆𝑛 are as follows:

𝑇𝑛 (𝑋1 ∶ 𝑋2 ∶ ⋯ ∶ 𝑋𝑛 )
=𝑇𝑛−1 (𝑋𝑘1 ∶ 𝑋𝑘2 ∶ ⋯ ∶ 𝑋𝑘𝑛−1 ) + 𝐼(𝑋𝑘1 ⋯ 𝑋𝑘𝑛−1 ∶ 𝑋𝑘𝑛 ),

and the strong subadditivity of von Neumann entropy (see Appendix C).
The idea is to eliminate 𝑆(𝑋1 𝑋2 ⋯ 𝑋𝑛 ) terms. This can be achieved by
grouping together (repeatedly) two appropriate entropy terms of small
number of parties to obtain an entropy term having greater number of
parties. One should, however, take care that while grouping no entropy
term, except 𝑆(𝑋1 𝑋2 ⋯ 𝑋𝑛 ), appears twice or more. ■

(A.1)

𝑇𝑛 (𝑋1 ∶ 𝑋2 ∶ ⋯ ∶ 𝑋𝑛 )
=𝑇𝑛−1 (𝑋𝑘1 𝑋𝑘2 ∶ 𝑋𝑘3 ∶ ⋯ ∶ 𝑋𝑘𝑛 ) + 𝐼(𝑋𝑘1 ∶ 𝑋𝑘2 ),

(A.2)

and

𝑆𝑛 (𝑋1 ∶ 𝑋2 ∶ ⋯ ∶ 𝑋𝑛 )
=𝑆𝑛−1 (𝑋𝑘1 𝑋𝑘2 ∶ 𝑋𝑘3 ∶ ⋯ ∶ 𝑋𝑘𝑛 )

(𝑛)
Thus, 𝑀𝑘 in Eq. (4) and 𝑀 (𝑛) in Eq. (17) satisfy a number of useful

properties: symmetry, semipositivity, vanishing on product states, additivity, and continuity. Hence, they constitute a family of multiparty
quantum mutual information.

+ 𝐼(𝑋𝑘1 ∶ 𝑋𝑘2 |𝑋𝑘3 ⋯ 𝑋𝑘𝑛 ),

(A.3)

where 𝑋𝑘𝑗 belongs to and exhaust the set  . It is evident that
the recurrence relation is not unique. For the choice of {𝑋𝑘𝑛−𝑗 =
, Eq. (A.1) and Eq. (A.2) separately yields Eq. (9), and
𝑋𝑗+1 }𝑛−1
𝑗=0

4.4. Conjecture and remark

Eq. (A.3) yields Eq. (12).
(𝑛 )
(𝑛2 )
2. Relations between 𝑀𝑘 1 and 𝑀𝑘+1
.

Secrecy monotones quantify the amount of secret correlation shared
by the parties of a multipartite system. They are useful in the study of
(𝑛)
(𝑛)
quantum (as well as classical) cryptography. 𝑀1 = 𝑇𝑛 and 𝑀𝑛−1 = 𝑆𝑛
satisfy properties (P4, P5) and (P8, P9), and qualify for secrecy mono(𝑛)
tones [33]. We speculate (see Appendix D for argument) that 𝑀𝑘 (𝑘 =
2, 3, ⋯ , 𝑛 − 2) in Eq. (4) and 𝑀 (𝑛) in Eq. (17) also meet the criteria (P4,
P5) and (P8, P9) for being considered as measures of secrecy monotone.
In addition to these 𝑛-party symmetric monotones, we also have
(𝑚)
other monotones 𝑀𝑘 (1 ≤ 𝑘 ≤ 𝑚 < 𝑛) on 𝑛-party quantum states
𝜌𝑋1 ⋯𝑋𝑛 which can be obtained by grouping together any two or more
of the 𝑛-parties. All these monotones, however, are not all linearly independent.

𝑀2(𝑛) +

∑

𝑗<𝑘∈[𝑛]

𝐼(𝑋𝑗 ∶ 𝑋𝑘 ) = (𝑛 − 1)𝑀1(𝑛) ,

(𝑛)
(𝑘 + 1)𝑀𝑘+1
+

=(𝑛 − 𝑘)𝑀𝑘(𝑛) +

∑

∑

𝑗1 <⋯<𝑗𝑘 ∈[𝑛] 𝑖(≠𝑗1 ≠⋯≠𝑗𝑘 )

(

1−

𝑘
𝑛

(A.4)

)
(
𝐼 𝑋 𝑗1 ⋯ 𝑋 𝑗𝑘 ∶ 𝑋 𝑖

)( )
𝑛
𝑀1(𝑛) ,
𝑘

(A.5)

(𝑛)
𝑀𝑛−1
(𝑋1 ∶ ⋯ ∶ 𝑋𝑛 )
(𝑛−1)
=𝑀𝑛−2
(𝑋1 ∶ ⋯ ∶ 𝑋𝑛−1 )

5. Conclusions

+

𝑛−1 (
∑
𝑘=1

In this study, we have conducted a comprehensive analysis of
entropy-based information within multiparty systems. Firstly, we introduced the concept of generalized conditional mutual information.
Next, we presented a family of multiparty quantum mutual information, which is anticipated to signiﬁcantly contribute to fundamental
research in quantum information theory. This advancement is expected
to enhance our comprehension of classical, quantum, and total correlations, and consequences thereof. Notably, this framework includes the
two well-established multiparty quantum mutual information measures.

𝑆𝑋 + 𝑆𝑋 − 𝑆𝑋1 ⋯𝑋𝑛 − 𝑆𝑋 𝑋
𝑘

𝑛

𝑘

𝑛

)

.

(A.6)

Appendix B. Proof of Eqs. (15), (16)
(𝑛)

Here we show that 𝑀𝑘 , for ﬁxed 𝑘 (1 ≤ 𝑘 < 𝑛), is nondecreasing
under discarding of any one party or grouping together any two parties.
That is,

5

𝑀𝑘(𝑛) (𝑋1 ∶ 𝑋2 ∶ ⋯ ∶ 𝑋𝑛 ) ≥ 𝑀𝑘(𝑛−1) (𝑋1 ∶ 𝑋2 ∶ ⋯ ∶ 𝑋𝑛−1 ),

(B.1)

𝑀𝑘(𝑛) (𝑋1 ∶ 𝑋2 ∶ ⋯ ∶ 𝑋𝑛 ) ≥ 𝑀𝑘(𝑛−1) (𝑋1 ∶ 𝑋2 ∶ ⋯ ∶ 𝑋𝑛−1 𝑋𝑛 ).

(B.2)

Physics Letters A 529 (2025) 130091

A. Kumar
(𝑛)

≥𝑀2(3) (𝑋1 ∶ 𝑋2 ∶ 𝑋3 𝑋4 ) + (𝑆1 + 𝑆2 + 𝑆34 − 𝑆1234 ),

Above inequalities follow from the deﬁnition of 𝑀𝑘 and the entropic inequalities 𝑆(𝑋) + 𝑆(𝑌 ) ≥ 𝑆(𝑋𝑌 ) (subadditivity) and 𝑆(𝑋𝑌 ) +
𝑆(𝑌 𝑍) ≥ 𝑆(𝑌 ) + 𝑆(𝑋𝑌 𝑍) (strong subadditivity), as shown below. First,
(𝑛)
we show that 𝑀𝑘 is nondecreasing under discarding a subsystem.

=𝑀2(3) (𝑋1 ∶ 𝑋2 ∶ 𝑋3 𝑋4 ) + 𝑀1(3) (𝑋1 ∶ 𝑋2 ∶ 𝑋3 𝑋4 ),
≥𝑀2(3) (𝑋1 ∶ 𝑋2 ∶ 𝑋3 𝑋4 ),

𝑀1(𝑛) (𝑋1 ∶ 𝑋2 ∶ ⋯ ∶ 𝑋𝑛 )
=

𝑛
∑
𝑘=1

=

𝑛−1
∑

𝑀3(4) (𝑋1 ∶ 𝑋2 ∶ 𝑋3 ∶ 𝑋4 ) = 𝑆123 + 𝑆124 + 𝑆134 + 𝑆234 − 3𝑆1234
≥ 0 = 𝑀3(3) (𝑋1 ∶ 𝑋2 ∶ 𝑋3 𝑋4 ). ■

𝑆𝑘 − 𝑆12⋯𝑛

(𝒏)
𝒌

Appendix C. Semipositivity of 𝑴

(
)
𝑆𝑘 − 𝑆12⋯(𝑛−1) + 𝑆12⋯(𝑛−1) + 𝑆𝑛 − 𝑆12⋯𝑛

𝑘=1
=𝑀1(𝑛−1) (𝑋1 ∶ 𝑋2 ∶ ⋯ ∶ 𝑋𝑛−1 ) + 𝐼(𝑋1 𝑋2 ⋯ 𝑋𝑛−1 ∶ 𝑋𝑛 |𝟏)
=𝑀1(𝑛−1) (𝑋1 ∶ 𝑋2 ∶ ⋯ ∶ 𝑋𝑛−1 ) + 𝑀1(2) (𝑋1 𝑋2 ⋯ 𝑋𝑛−1 ∶ 𝑋𝑛 ),
≥𝑀1(𝑛−1) (𝑋1 ∶ 𝑋2 ∶ ⋯ ∶ 𝑋𝑛−1 ),
𝑀2(𝑛) (𝑋1 ∶ 𝑋2 ∶ ⋯ ∶ 𝑋𝑛 )

=

∑

𝑗<𝑘∈[𝑛]

𝑗<𝑘∈[𝑛−1]

+

𝑀1(5) = (𝑆1 + 𝑆2 + 𝑆3 + 𝑆4 + 𝑆5 ) − 𝑆12345 ≥ 𝑆12345 − 𝑆12345 = 0.
𝑀2(5) = 𝑆12 + 𝑆13 + 𝑆14 + 𝑆15 + 𝑆23 + 𝑆24 + 𝑆25 + 𝑆34
+𝑆35 + 𝑆45 − 4𝑆12345

𝑆𝑗𝑘 − (𝑛 − 1)𝑆12⋯𝑛

∑

=

(𝑛)

Here we illustrate the nonnegativity of 𝑀𝑘 for 𝑛 = 5.

(𝑛−1
∑
𝑗=1

= (𝑆12 + 𝑆34 ) + 𝑆15 + (𝑆13 + 𝑆45 ) + 𝑆24 + (𝑆14 + 𝑆23 )
+𝑆25 + 𝑆35 − 4𝑆12345

𝑆𝑗𝑘 − (𝑛 − 2)𝑆12⋯(𝑛−1)

≥ (𝑆1234 + 𝑆15 ) + (𝑆1345 + 𝑆24 ) + (𝑆1234 + 𝑆25 ) + 𝑆35 − 4𝑆12345

)

≥ (𝑆12345 + 𝑆1 ) + (𝑆12345 + 𝑆4 ) + (𝑆12345 + 𝑆2 ) + 𝑆35 − 4𝑆12345

𝑆𝑗𝑛 + (𝑛 − 2)𝑆12⋯(𝑛−1) − (𝑛 − 1)𝑆12⋯𝑛

≥𝑀2(𝑛−1) (𝑋1 ∶ 𝑋2 ∶ ⋯ ∶ 𝑋𝑛−1 ) +

(𝑛−2
∑
𝑗=1

= (𝑆1 + 𝑆2 + 𝑆4 ) + 𝑆35 − 𝑆12345

)
𝑆𝑗 + 𝑆(𝑛−1)𝑛 − 𝑆12⋯𝑛

≥ (𝑆124 + 𝑆35 ) − 𝑆12345
≥ 𝑆12345 − 𝑆12345 = 0.

≥𝑀2(𝑛−1) (𝑋1 ∶ 𝑋2 ∶ ⋯ ∶ 𝑋𝑛−1 )

𝑀3(5) = 𝑆123 + 𝑆124 + 𝑆125 + 𝑆134 + 𝑆135 + 𝑆145 + 𝑆234 + 𝑆235

+ 𝑀1(𝑛−1) (𝑋1 ∶ 𝑋2 ∶ ⋯ 𝑋𝑛−2 ∶ 𝑋𝑛−1 𝑋𝑛 ),

+𝑆245 + 𝑆345 − 6𝑆12345

≥𝑀2(𝑛−1) (𝑋1 ∶ 𝑋2 ∶ ⋯ ∶ 𝑋𝑛−1 ),

= (𝑆123 + 𝑆145 ) + (𝑆124 + 𝑆235 ) + (𝑆135 + 𝑆234 ) + (𝑆134 + 𝑆245 )

𝑀3(𝑛) (𝑋1 ∶ 𝑋2 ∶ ⋯ ∶ 𝑋𝑛 )
(
)
∑
𝑛−1
𝑆𝑖𝑗𝑘 −
𝑆12⋯𝑛
=
2
𝑖<𝑗<𝑘∈[𝑛]
(
)
∑
𝑛−2
=
𝑆𝑖𝑗𝑘 −
𝑆12⋯(𝑛−1)
2
𝑖<𝑗<𝑘∈[𝑛−1]
)
(
(
)
(
)
∑
𝑛−2
𝑛−1
+
𝑆𝑖𝑗𝑛 +
𝑆12⋯(𝑛−1) −
𝑆12⋯𝑛
2
2
𝑖<𝑗∈[𝑛−1]

+(𝑆125 + 𝑆345 ) − 6𝑆12345
≥ (𝑆1 + 𝑆12345 ) + (𝑆2 + 𝑆12345 ) + (𝑆3 + 𝑆12345 ) + (𝑆4 + 𝑆12345 )
+(𝑆5 + 𝑆12345 ) − 6𝑆12345
= (𝑆1 + 𝑆2 + 𝑆3 + 𝑆4 + 𝑆5 ) − 𝑆12345 ≥ 0.
𝑀4(5) = (𝑆1234 + 𝑆1235 ) + (𝑆1245 + 𝑆1345 ) + 𝑆2345 − 4𝑆12345

≥𝑀3(𝑛−1) (𝑋1 ∶ 𝑋2 ∶ ⋯ ∶ 𝑋𝑛−1 )
)
(𝑛−1
𝑛−2 ∑
𝑛−1
∑
∑
𝑆1𝑗𝑛 +
𝑆𝑖𝑗 − (𝑛 − 2)𝑆12⋯𝑛
+

≥ (𝑆123 + 𝑆12345 ) + (𝑆145 + 𝑆12345 ) + 𝑆2345 − 4𝑆12345

≥𝑀3(𝑛−1) (𝑋1 ∶ 𝑋2 ∶ ⋯ ∶ 𝑋𝑛−1 ).

= (𝑆1 + 𝑆2345 ) − 𝑆12345

(𝑛)
(𝑛−1)
Similarly, one can show that 𝑀𝑘>3 (𝑋1 ∶ 𝑋2 ∶ ⋯ ∶ 𝑋𝑛 ) ≥ 𝑀𝑘>3 (𝑋1 ∶
(𝑛)
𝑋2 ∶ ⋯ ∶ 𝑋𝑛−1 ). Next, we show that 𝑀𝑘 is nondecreasing under group-

≥ 𝑆12345 − 𝑆12345 = 0.

𝑗=2

≥ (𝑆123 + 𝑆145 ) + 𝑆2345 − 2𝑆12345
≥ (𝑆1 + 𝑆12345 ) + 𝑆2345 − 2𝑆12345

𝑖=2 𝑗=𝑖+1

Alternatively, one can also endeavor to obtain a recurrence relation
(𝑛)
for 𝑀𝑘 which expresses it as a positive sum of bipartite mutual information 𝐼(𝐴 ∶ 𝐵) and conditional mutual information 𝐼(𝐴 ∶ 𝐵|𝐶). Then,
(𝑛)
the semipositivity of 𝑀𝑘 is trivial. We, however, note that obtaining
the recurrence relation is neither unique [see Eqs. (A.1), (A.2), (A.3)]
nor easy. For example,

ing together two parties, speciﬁcally for 𝑛 = 4.

𝑀1(4) (𝑋1 ∶ 𝑋2 ∶ 𝑋3 ∶ 𝑋4 ) = (𝑆1 + 𝑆2 + 𝑆3 + 𝑆4 ) − 𝑆1234
= (𝑆1 + 𝑆2 + 𝑆34 − 𝑆1234 ) + (𝑆3 + 𝑆4 − 𝑆34 )
= 𝑀1(3) (𝑋1 ∶ 𝑋2 ∶ 𝑋3 𝑋4 ) + 𝑀1(2) (𝑋3 ∶ 𝑋4 ),

𝑀2(𝑛) (𝑋1 ∶ 𝑋2 ∶ ⋯ ∶ 𝑋𝑛 )

≥ 𝑀1(3) (𝑋1 ∶ 𝑋2 ∶ 𝑋3 𝑋4 ),
𝑀2(4) (𝑋1 ∶ 𝑋2 ∶ 𝑋3 ∶ 𝑋4 )

=𝑀2(𝑛−1) (𝑋1 ∶ 𝑋2 ∶ ⋯ ∶ 𝑋𝑛−1 ) + 𝑀1(𝑛−1) (𝑋1 ∶ 𝑋2 ∶ ⋯ ∶ 𝑋𝑛−1 )

=𝑆12 + 𝑆13 + 𝑆14 + 𝑆23 + 𝑆24 + 𝑆34 − 3𝑆1234

+ 𝐼(𝑋𝑛 ∶ 𝑋2 ⋯ 𝑋𝑛−1 |𝑋1 )

=(𝑆12 + 𝑆134 + 𝑆234 − 2𝑆1234 )
+

+ (𝑆13 + 𝑆14 + 𝑆23 + 𝑆24 + 𝑆34 − 𝑆134 − 𝑆234 − 𝑆1234 )

𝑛−1
∑
𝑗=2

6

𝐼(𝑋𝑛 ∶ 𝑋1 ⋯ 𝑋𝑗−1 𝑋𝑗+1 ⋯ 𝑋𝑛−1 |𝑋𝑗 ). ■

(C.1)

Physics Letters A 529 (2025) 130091

A. Kumar
(𝒏)
𝒌

Appendix D. Argument for secrecy monotones of 𝑴

[6] N. Li, S. Luo, Total versus quantum corrrelations in quantum states, Phys. Rev. A 76
(2007) 032327.
[7] C.H. Bennett, P.W. Shor, Quantum channel capacities, Science 303 (2004)
1784–1787.
[8] A.S. Holevo, Quantum channel capacities, Quantum Electron. 50 (2020) 440.
[9] J. Biamonte, P. Wittek, N. Pancotti, P. Rebentrost, N. Wiebe, S. Lloyd, Quantum
machine learning, Nature 549 (2017) 195–202.
[10] G. Carleo, I. Cirac, K. Cranmer, L. Daudet, M. Schuld, N. Tishby, L. Vogt-Maranto, L.
Zdeborová, Machine learning and the physical sciences, Rev. Mod. Phys. 91 (2019)
045002.
[11] G.D. Tomasi, S. Bera, J.H. Bardarson, F. Pollmann, Quantum mutual information as
a probe for many-body localization, Phys. Rev. Lett. 118 (2017) 016804.
[12] D.A. Chisholm, L. Innocenti, G.M. Palma, Importance of using the averaged mutual information when quantifying quantum objectivity, Phys. Rev. A 110 (2024)
012218.
[13] I. Bengtsson, K. Życzkowski, Geometry of Quantum States: An Introduction to Quantum Entanglement, Cambridge University Press, 2006.
[14] R. Horodecki, P. Horodecki, M. Horodecki, K. Horodecki, Quantum entanglement,
Rev. Mod. Phys. 81 (2009) 865.
[15] K. Modi, A. Brodutch, H. Cable, T. Paterek, V. Vedral, The classical-quantum boundary for correlations: discord and related measures, Rev. Mod. Phys. 84 (2012) 1655.
[16] A. Bera, T. Das, D. Sadhukhan, S.S. Roy, A. Sen(De), U. Sen, Quantum discord and
its allies: a review of recent progress, Rep. Prog. Phys. 81 (2018) 024001.
[17] S.-Y. Liu, Y.-R. Zhang, L.-M. Zhao, W.-L. Yang, H. Fan, General monogamy property
of global quantum discord and the application, Ann. Phys. 348 (2014) 256–269.
[18] A. Kumar, Conditions for monogamy of quantum correlations in multipartite systems, Phys. Lett. A 380 (38) (2016) 3044–3050.
[19] H.S. Dhar, A.K. Pal, D. Rakshit, A. Sen(De), U. Sen, Monogamy of quantum correlations – a review, in: Lectures on General Quantum Correlations and Their Applications, in: Part of the Series Quantum Science and Technology, Springer International
Publishing, 2017, pp. 23–64.
[20] C. Song, et al., Generation of multicomponent atomic Schrödinger cat states of up to
20 qubits, Science 365 (6453) (2019) 574–577.
[21] C.-T. Chen, et al., ScQ cloud quantum computation for generating GreenbergerHorne-Zeilinger states of up to 10 qubits, Sci. China, Phys. Mech. Astron. 65 (2022)
110362.
[22] K. Xu, et al., Metrological characterization of non-Gaussian entangled states of superconducting qubits, Phys. Rev. Lett. 128 (2022) 150501.
[23] S. Watanabe, Information theoretical analysis of multivariate correlation, IBM J. Res.
Dev. 4 (1) (1960) 66–81.
[24] T.S. Han, Linear dependence structure of the entropy space, Inf. Control 29 (1975)
337–368.
[25] T.S. Han, Nonnegative entropy measures of multivariate symmetric correlations, Inf.
Control 36 (1978) 133–156.
[26] Z. Walczak, Total correlations and mutual information, Phys. Lett. A 373 (2009)
1818–1822.
[27] G.L. Giorgi, B. Bellomo, F. Galve, R. Zambrini, Genuine quantum and classical correlations in multipartite systems, Phys. Rev. Lett. 107 (2011) 190501.
[28] A. Kumar, Multiparty quantum mutual information: an alternative deﬁnition, Phys.
Rev. A 96 (2017) 012332.
[29] Sk Sazim, P. Agrawal, Quantum mutual information and quantumness vectors for
multiqubit systems, Quantum Inf. Process. 19 (2020) 216.
[30] A. Wehrl, General properties of entropy, Rev. Mod. Phys. 50 (1978) 221.
[31] M.B. Ruskai, Inequalities for quantum entropy: a review with conditions for equality,
J. Math. Phys. 43 (2002) 4358–4375.
[32] A. M̈uller-Hermes, D. Reeb, Monotonicity of the quantum relative entropy under
positive maps, Ann. Henri Poincaré 18 (2017) 1777–1788.
[33] N.J. Cerf, S. Massar, S. Schneider, Multipartite classical and quantum secrecy monotones, Phys. Rev. A 66 (2002) 042309.
[34] M. Horodecki, P. Horodecki, R. Horodecki, Limits for entanglement measures, Phys.
Rev. Lett. 84 (2000) 2014.
[35] N.J. Cerf, C. Adami, Negative entropy and information in quantum mechanics, Phys.
Rev. Lett. 79 (1997) 5194–5197.
[36] M. Horodecki, J. Oppenheim, A. Winter, Partial quantum information, Nature 436
(2005) 673–676.
[37] M. Horodecki, J. Oppenheim, A. Winter, Quantum state merging and negative information, Commun. Math. Phys. 269 (2007) 107–136.
[38] L. del Rio, J. Aberg, R. Renner, O. Dahlsten, V. Vedral, The thermodynamic meaning
of negative entropy, Nature 474 (2011) 61–63.
[39] G. Gour, M.M. Wilde, S. Brandsen, I.J. Geng, Inevitability of knowing less than nothing, arXiv:2208.14424 [quant-ph].

(𝑛)

Our argument for the speculation that 𝑀𝑘 meet the criteria of secrecy monotones is as follows. Consider a ﬁve-party quantum system
 = {𝑋1 , ⋯ , 𝑋5 }, for example. We know that the von Neumann entropy
is invariant under unitary transformations including the permutation or
particle exchange operator. That is, 𝑆12345 = 𝑆13245 = 𝑆23145 , etc. Then

𝑀2(5) (𝑋1 ∶ 𝑋2 ∶ ⋯ ∶ 𝑋5 )
=𝑆12 + 𝑆13 + 𝑆14 + 𝑆15 + 𝑆23 + 𝑆24 + 𝑆25 + 𝑆34 + 𝑆35
+ 𝑆45 − 4𝑆12345
(
)
= 𝑆12 + log2 (𝑑3 𝑑4 𝑑5 ) − 𝑆12345
(
)
+ 𝑆13 + log2 (𝑑2 𝑑4 𝑑5 ) − 𝑆13245 + ⋯
(
)
+ 𝑆45 + log2 (𝑑1 𝑑2 𝑑3 ) − 𝑆12345 + 6𝑆12345 − log2 (𝑑1 𝑑2 𝑑3 𝑑4 𝑑5 )6
=𝐷(𝜌12345 ||𝜌12 ⊗ 𝐼345 ) + 𝐷(𝜌13245 ||𝜌13 ⊗ 𝐼245 ) + ⋯
+ 𝐷(𝜌12345 ||𝐼123 ⊗ 𝜌45 ) + 6𝑆12345 − log2 (𝑑1 𝑑2 𝑑3 𝑑4 𝑑5 )6 ,
and

𝑀3(5) (𝑋1 ∶ 𝑋2 ∶ ⋯ ∶ 𝑋5 )
=𝑆123 + 𝑆124 + 𝑆125 + 𝑆134 + 𝑆135 + 𝑆145 + 𝑆234 + 𝑆235
+ 𝑆245 + 𝑆345 − 6𝑆12345
(
) (
)
= 𝑆123 + log2 (𝑑4 𝑑5 ) − 𝑆12345 + 𝑆124 + log2 (𝑑3 𝑑5 ) − 𝑆12435 + ⋯
(
)
+ 𝑆345 + log2 (𝑑1 𝑑2 ) − 𝑆12345 + 4𝑆12345 − log2 (𝑑1 𝑑2 𝑑3 𝑑4 𝑑5 )4
=𝐷(𝜌12345 ||𝜌123 ⊗ 𝐼45 ) + 𝐷(𝜌12435 ||𝜌124 ⊗ 𝐼35 ) + ⋯
+ 𝐷(𝜌12345 ||𝐼12 ⊗ 𝜌345 ) + 4𝑆12345 − log2 (𝑑1 𝑑2 𝑑3 𝑑4 𝑑5 )4 .
In the last steps above, the multiplicative factor of( total )entropy
( )
∏
𝑆12⋯𝑛 or the exponent of 𝑛𝑖=1 𝑑𝑖 can be obtained as 𝑘𝑛 1 − 𝑘𝑛 . While
𝐷(𝜌𝐴𝐵 ||𝜌𝐴 ⊗ 𝜌𝐵 ) is always well-behaved, 𝐷(𝜌𝐴𝐵 ||𝜌𝐵 ⊗ 𝜌𝐴 ) is not in
general due to the support condition. Therefore, in the second steps
above, the parties (subsystems) have been rearranged beforehand to resolve the support condition of QRE. Note that the operations such as
local quantum operations and local measurements and public classical
communication can be regarded as local positive maps [33]. Because
𝐷(𝜌||𝜎) ≥ 𝐷(Φ(𝜌)||Φ(𝜎)) for any local positive map Φ, it implies that
𝑀𝑘(𝑛) are monotonic under local quantum operations and classical communications. ■
Data availability
No data was used for the research described in the article.
References
[1] T. Cover, J. Thomas, Elements of Information Theory, John Wiley & Sons, 1991.
[2] M.A. Nielsen, I.L. Chuang, Quantum Computation and Quantum Information, Cambridge University Press, 2000.
[3] M.M. Wilde, Quantum Information Theory, Cambridge University Press, 2013.
[4] J. Preskill, Lecture Notes for Physics 229: Quantum Information and Computation,
CreateSpace Independent Publishing Platform, 2015.
[5] B. Groisman, S. Popescu, A. Winter, Quantum, classical, and total amount of correlations in a quantum state, Phys. Rev. A 72 (2005) 032317.

7

