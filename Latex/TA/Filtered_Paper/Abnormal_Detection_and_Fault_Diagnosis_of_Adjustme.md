machines
Article

Abnormal Detection and Fault Diagnosis of Adjustment
Hydraulic Servomotor Based on Genetic Algorithm to Optimize
Support Vector Data Description with Negative Samples and
One-Dimensional Convolutional Neural Network
Xukang Yang 1,2 , Anqi Jiang 3 , Wanlu Jiang 1,2, *, Yonghui Zhao 1,2 , Enyu Tang 1,2 and Shangteng Chang 1,2
1

2

3

*

Citation: Yang, X.; Jiang, A.; Jiang, W.;
Zhao, Y.; Tang, E.; Chang, S.
Abnormal Detection and Fault
Diagnosis of Adjustment Hydraulic
Servomotor Based on Genetic
Algorithm to Optimize Support Vector
Data Description with Negative
Samples and One-Dimensional
Convolutional Neural Network.
Machines 2024, 12, 368. https://
doi.org/10.3390/machines12060368
Academic Editor: Alexios
Papacharalampopoulos
Received: 29 April 2024

Hebei Provincial Key Laboratory of Heavy Machinery Fluid Power Transmission and Control, Yanshan
University, Qinhuangdao 066004, China; qibaoer_zongwu@163.com (X.Y.); ysuzyh1996@163.com (Y.Z.);
ysyytey@163.com (E.T.); ysucst@163.com (S.C.)
Key Laboratory of Advanced Forging & Stamping Technology and Science, Yanshan University, Ministry of
Education of China, Qinhuangdao 066004, China
School of Electrical Engineering, Yanshan University, Qinhuangdao 066004, China; anqi_jiang@163.com
Correspondence: wljiang@ysu.edu.cn

Abstract: Because of the difficulty in fault detection for and diagnosing the adjustment hydraulic
servomotor, this paper uses feature extraction technology to extract the time domain and frequency
domain features of the pressure signal of the adjustment hydraulic servomotor and splice the features
of multiple pressure signals through the Multi-source Information Fusion (MSIF) method. The
comprehensive expression of device status information is obtained. After that, this paper proposes a
fault detection Algorithm GA-SVDD-neg, which uses Genetic Algorithm (GA) to optimize Support
Vector Data Description with negative examples (SVDD-neg). Through joint optimization with the
Mutual Information (MI) feature selection algorithm, the features that are most sensitive to the state
deterioration of the adjustment hydraulic servomotor are selected. Experiments show that the MI
algorithm has a better performance than other feature dimensionality reduction algorithms in the field
of the abnormal detection of adjustment hydraulic servomotors, and the GA-SVDD-neg algorithm has
a stronger robustness and generality than other anomaly detection algorithms. In addition, to make
full use of the advantages of deep learning in automatic feature extraction and classification, this
paper realizes the fault diagnosis of the adjustment hydraulic servomotor based on 1D Convolutional
Neural Network (1DCNN). The experimental results show that this algorithm has the same superior
performance as the traditional algorithm in feature extraction and can accurately diagnose the known
faults of the adjustment hydraulic servomotor. This research is of great significance for the intelligent
transformation of adjustment hydraulic servomotors and can also provide a reference for the fault
warning and diagnosis of the Electro-Hydraulic (EH) system of the same type of steam turbine.
Keywords: adjustment hydraulic servomotor; fault detection; fault diagnosis; genetic algorithm;
support vector data description; one-dimensional convolutional neural networks

Revised: 16 May 2024
Accepted: 20 May 2024
Published: 24 May 2024

1. Introduction
Copyright: © 2024 by the authors.
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed under the terms and
conditions of the Creative Commons
Attribution (CC BY) license (https://
creativecommons.org/licenses/by/
4.0/).

A high-pressure adjustment hydraulic servomotor is an electromechanical hydraulic
integrated system with a servo valve as its core. Its task is to provide the power source for
the steam turbine valve mechanism, which plays a key role in ensuring the safe and stable
operation of the steam turbine. However, due to the complex structure and harsh working
environment of the high-pressure adjustment hydraulic servomotor, its key components,
such as springs and seals, are prone to wear and tear, resulting in abnormal operation.
Moreover, due to the strong nonlinearity of the high-pressure adjustment hydraulic servomotor system, it is difficult to diagnose it through the traditional regular maintenance
program and overhaul method, which seriously affects the safe operation of the turbine.

Machines 2024, 12, 368. https://doi.org/10.3390/machines12060368

https://www.mdpi.com/journal/machines

Machines 2024, 12, 368

2 of 21

Therefore, the effective abnormal detection and fault diagnosis of the adjustment hydraulic
servomotor is the key to ensuring the stable operation of the turbine unit [1].
Numerous scholars have conducted a lot of research in the field of electro-hydraulic
servomotor system troubleshooting for high-pressure adjustment hydraulic servomotors.
Yu et al. studied the valve stem jamming problem using orthogonal decomposition and
simulation methods [2]. Li et al. proposed a method for detecting various slide valve faults
as well as electro-hydraulic converter jamming faults by introducing an expert system [3].
Wang et al. combined a particle swarm optimization algorithm with a back propagation
neural network to effectively diagnose servo valve faults [4]. Xu et al. verified that the
Genetic Algorithm (GA) can be applied to the adjustment hydraulic servomotor jamming
fault diagnosis by simulation means [5]. Zhang et al. combined a system identification
method with a genetic algorithm to realize the diagnosis of hydraulic servomotor jamming
faults [6]. However, the above research focuses on piston rod jamming and servo valve
jamming, two types of faults, and the research method is only “simulation” based; there
are fewer types of faults and limitations in the research methods. With the advent of
the Industry 4.0 era, a diagnostic system that relies on knowledge and simulation can no
longer meet the requirements of modern intelligent fault diagnosis [7], and the data-driven
Prognostics and Health Management (PHM) system has become increasingly prominent in
the field of intelligent manufacturing [8].
Given that the vibration signal is easily interfered with by factors such as the inherent mechanical vibration of the hydraulic servomotor and the strong noise background,
and the fact that pressure signals play an increasingly important role in the field of the
intelligent operation and maintenance of hydraulic systems [9], a specific description of
the characteristics of the pressure signal can be formed through the extraction of multiple
time-domain and frequency-domain features of the pressure signal that are of good physical
significance and interpretability. However, the characteristic information obtained only
from a single pressure signal is incomplete in describing the overall operating state of
the adjustment hydraulic servomotor, and the Multi-source Information Fusion (MSIF)
method can combine the complementary information in space. Then, the completeness
of the feature information is greatly improved. The concept of MSIF was first proposed
by Professor Y. Bar-Shalom, a famous system scientist, in the 1970s [10]. In recent years,
the theory and technology of MSIF have rapidly developed into an independent discipline and have been widely used in wireless communication, fault diagnosis, and other
fields [11]. In this paper, the “feature level” information fusion technology in MSIF is used
to concatenate the features from different pressure signals into a comprehensive feature,
which provides a more comprehensive and in-depth data perspective for the subsequent
anomaly detection model training. In addition, to solve the problem of data sparsity in
the high-dimensional feature space after feature fusion, the dimensionality of feature fusion needs to be approximated. Currently, the mainstream data dimensionality reduction
methods include unsupervised dimensionality reduction algorithms and feature selection
algorithms; compared to the former, the latter only filters the existing features, which has
the advantage of strong interpretability [12]. Mutual information (MI) has been widely
used as a simple and efficient feature selection algorithm [13–15]. For example, Jiang et al.
proposed a multi-block principal component analysis method based on MI and utilized
SVDD to comprehensively evaluate the monitoring results of all sub-blocks to achieve
anomaly detection in industrial process monitoring [16].
The main task of fault detection for mechanical equipment is that the model can
identify the abnormal behavior of the equipment through real-time data. However, the
fault state of the equipment in the industrial field is highly accidental, so it is quite difficult
to collect the abnormal state data, compared with the normal state data that can be easily
obtained. Moreover, even if a small amount of fault data is obtained, it is difficult to fully
describe all fault states [17,18]. Therefore, the Anomaly Detection (AD) algorithm, that only
needs normal data to complete the modeling process, has become the key to solving this
problem [19,20]. Moreover, compared with the classification model, the AD algorithm also

Machines 2024, 12, 368

3 of 21

has great advantages in detecting unknown faults [21]. For example, Yu et al. used MoniNet,
an innovative network architecture and analysis methodology, to improve the accuracy
and efficiency of industrial process monitoring and control [22]. As a classic algorithm
in the AD field, Support Vector Data Description (SVDD) was proposed by Tax et al. [23]
in 1999 and has been widely used in biochemistry, cloud computing, fault diagnosis, and
other fields [24–26]. Since the performance of SVDD is deeply affected by the selection
of hyperparameters, various meta-heuristic methods have been used to optimize SVDD
hyperparameters [27,28]. However, because SVDD only establishes decision boundaries
for normal data, it easily leads to the overfitting of the model and a high false positive
rate. For this reason, Tax et al., the creators of SVDD, pointed out in 2004 that adding
abnormal data to the training set is expected to strengthen the description of normal data
on the decision boundary, and proposed the SVDD with negative examples (SVDD-neg)
algorithm [29]. Like SVDD, SVDD-neg relies heavily on hyperparameter tuning. Ni et al.
used PSO to optimize the hyperparameters of SVDD-neg and significantly reduced the
false positive rate in Foreign Object Damage (FOD) target detection under strong ground
clutter [30]. However, the PSO Algorithm is prone to fall into the local optimal solution
in the optimization process [31]. Therefore, in this paper, a GA-SVDD-neg algorithm is
proposed to optimize the SVDD-neg using GA, which has strong global searching ability,
to achieve the abnormal monitoring of hydraulic servomotors.
Finally, based on the principle of warning-then-diagnosis, when the anomaly detection
model gives a fault prediction, the classification model realizes the diagnosis of existing
faults. In recent years, with the improvement in computing power, deep learning, and
especially Convolutional Neural Networks (CNNs), has become a research focus in the field
of fault diagnosis [32]. CNNs can automatically extract features, and the feature extraction
process is directly oriented to fault classification. This end-to-end joint optimization is
conducive to improving the generalization ability of the model. Since Krizhevsky et al.
used a CNN to obtain the best classification in the ImageNet Large-scale Visual Recognition
Challenge in 2012 [33], CNNs have been widely used in the field of image recognition.
Therefore, many scholars have combined the time–frequency transform method with
2DCNN. It is applied for the intelligent fault diagnosis of equipment [34,35]. However,
the state signal during machine operation is usually a one-dimensional vector and the
time–frequency conversion of the original signal will cause a certain degree of information
distortion. 1DCNN directly processes the original one-dimensional time series signal,
which not only avoids input information loss but also simplifies the network structure,
which is conducive to the application of the model in the real-time diagnosis of equipment.
The main contributions of this research are as follows:
(1)

(2)

(3)

The MSIF “feature-level” information fusion technique is adopted to stitch the features
from different pressure signals into a comprehensive feature, which provides a more
comprehensive and in-depth data perspective for the subsequent training of the
anomaly detection model. The MI algorithm is also used to remove redundant
features in the fused high-dimensional features, which enhances the robustness and
generalizability of the subsequent model.
A GA-SVDD-neg algorithm is proposed by optimizing SVDD-neg using GA with
strong global search capability, and the accuracy of the GA-SVDD-neg model is
directly used as a quantitative index to evaluate the performance of the feature selection algorithm, which implements the MI-GA-SVDD-neg joint optimization. The
superiority of MI-GA-SVDD-neg is verified by combining and co-optimizing four
feature dimensionality reduction methods with GA-SVDD-neg, which are Principal
Components Analysis (PCA), minimum Redundancy–Maximum Relevance (mRMR),
Analysis of Variance (ANOVA), and Random Forest-based Recursive Feature Elimination (RFE).
The superiority of GA-SVDD-neg compared to PSO-SVDD and GA-SVDD is verified
based on the feature set screened by MI.

Machines 2024, 12, 368

Analysis of Variance (ANOVA), and Random Forest-based Recursive Feature Elimination (RFE).
(3) The superiority of GA-SVDD-neg compared to PSO-SVDD and GA-SVDD is verified
4 of 21
based on the feature set screened by MI.
(4) 1DCNN was employed for pattern recognition of the hydraulic servomotor and the
eﬀectiveness of the algorithm in the fault diagnosis of the hydraulic servomotor was
(4) verified.
1DCNN was employed for pattern recognition of the hydraulic servomotor and the
effectiveness of the algorithm in the fault diagnosis of the hydraulic servomotor was
The rest of the paper is organized as follows. Section 2 summarizes the basic princiverified.
ples of MI and SVDD-neg algorithms. Section 3 analyzes in detail the process of collecting
The rest ofdata
the paper
is organizedfeature
as follows.
the basic principles
experimental
and constructing
sets.Section
Section2 4summarizes
conducts comparative
experiof
MI
and
SVDD-neg
algorithms.
Section
3
analyzes
in
detail
the
process
of collecting
exments and analyzes the main results. Section 5 analyzes the results of the
1DCNN test.
perimental
data
and
constructing
feature
sets.
Section
4
conducts
comparative
experiments
Finally, the conclusions are summarized and future research is envisioned in Section 6.
and analyzes the main results. Section 5 analyzes the results of the 1DCNN test. Finally,
the
conclusions
are summarized
and future research is envisioned in Section 6.
2. Related
Technologies
and Theories
2.1.
MutualTechnologies
Information and Theories
2.
Related
2.1. Mutual
MI is a Information
measure of the degree of interdependence between random variables, X and
Y . ItMI
X is reduced
Y isXknown,
indicates
the extent
whichofthe
uncertainty inbetween
is a measure
of thetodegree
interdependence
randomwhen
variables,
and Y.
and
is giventhe
by extent
the following
formula:
It
indicates
to which
the uncertainty in X is reduced when Y is known, and is
given by the following formula:
p ( x, y )
I ( X ; Y ) =   p ( x, y ) log
(1)
x∈ X y∈Y
p (px()x,p (yy))
I ( X; Y ) = ∑ ∑ p( x, y) log
(1)
( x ) p(y)
X y ∈Y
The relationship and diﬀerencex∈between
MI and pinformation
entropy are shown in
Figure 1. The correlation of the two random variables increases with the increase in their
Theinformation
relationshipvalue,
and difference
MIaand
information
entropyofare
shown in
mutual
so MI canbetween
be used as
measure
of the amount
information
Figure
1.
The
correlation
of
the
two
random
variables
increases
with
the
increase
in their
shared by two random variables. The specific expression of MI is as follows:
mutual information value, so MI can be used as a measure of the amount of information
I ( X ;expression
Y) =
shared by two random variables. The specific
of MI is as follows:
H ( X ) − H ( X∣Y ) =
(2)
) −YH)(=
H (IY( X;
Y∣X ) =
H (X) − H (X | Y) =
(2)
H ( X ) + H (Y ) − H ( X , Y )
H (Y ) − H (Y | X ) =
H ( Xentropies
) + H (Y ) −
( X, Y ) variables X and Y , respecwhere H ( X ) and H (Y ) are the
of Hrandom
tively. H ( X , Y ) is the joint entropy, which represents the joint distribution of two ranwhere H ( X ) and H (Y ) are the entropies of random variables X and Y, respectively. H ( X, Y )
X which
dom
and Y represents
. Conditional
entropy
H ( X | Y )ofrepresents
thevariables
uncertainty
of
is
the variables
joint entropy,
the joint
distribution
two random
X and
X
when
random
variable
Y
is
known.
In
machine
learning
tasks,
MI
random
variable
Y. Conditional entropy H ( X |Y ) represents the uncertainty of random variable X when
is used as
a measure
the correlation
between
features
labels
used to screen
random
variable
Y is of
known.
In machine
learning
tasks,and
MI is
usedand
as aismeasure
of the
out featuresbetween
with a strong
correlation
with
to achieve
the
purpose
ofwith
feature
seleccorrelation
features
and labels
andlabels
is used
to screen
out
features
a strong
tion.
correlation
with labels to achieve the purpose of feature selection.
H(X )

H (Y )

H ( X | Y ) I ( X ; Y ) H (Y | X )

H ( X ,Y )

Figure 1.
1. Mutual information
information Venn
Venn diagram.
diagram.
Figure

2.2. Principle of SVDD-neg Algorithm
2.2. Principle of SVDD-neg Algorithm
Figure 2 shows the basic classification of SVDD. In the figure, the solid circles are
Figure 2 shows the basic classification of SVDD. In the figure, the solid circles are the
the target class samples that need to be described, and the cross symbols are the anomaly
target class samples that need to be described, and the cross symbols are the anomaly
samples that need to be rejected; S is the spherical boundary of the described region. SVDD
samples that need to be rejected; S is the spherical boundary of the described region.
is the coverage area determined by defining the center a and radius R of the sphere, and
SVDD is the coverage area determined by defining the center a and radius R of the
rejecting the abnormal class sample as much as possible while completely covering the
sphere, and rejecting the abnormal class sample as much as possible while completely
target class sample, and the relaxation variable ξ i is used to reduce the influence of outliers
on SVDD. However, the decision boundary of SVDD is often not tight enough, and some
abnormal samples are easily misjudged as normal samples, so the generalization of the
model is low. To make up for this deficiency, Tax et al. introduced abnormal samples into
the training process of the model and proposed the SVDD-neg algorithm. The mathematical
model of SVDD-neg can be expressed as follows:

Machines 2024, 12, 368

fluence of outliers on SVDD. However, the decision boundary of SVDD is often not tight
enough, and some abnormal samples are easily misjudged as normal samples, so the generalization of the model is low. To make up for this deficiency, Tax et al. introduced abnormal samples into the training process of the model and proposed the SVDD-neg algorithm. The mathematical model of SVDD-neg can be expressed as follows:
5 of 21
n

m

n i =1

l =1

min R 2 + c1 ξi + c2 ξ l , ξ i , ξ l ≥ 0
R,a

m

2
2
min R
s.t.+
φ (c1x )∑− aξ i +≤cR2 2∑+ ξξ l,, ξyi , ξ=l 1≥ 0
R,a

i i =1

l =1 i

22

(3)
(3)

i

2 2 + ξ i , yi = 1
s.t.∥ϕφ( x( xi ) )−− aa∥ ≥≤RR
− ξl , yl = −1
l
2
2
∥ ϕ ( x l ) − a ∥ ≥ R − ξ l , y l = −1

n
m
where { x , y } =1 is the target class sample set, yi = +1 is the label of xi , { xl , yl }ml =1 is the
where { xi i, yii}ini=
is
the
target
class
sample
set,
y
=
+
1
is
the
label
of
x
,
x
,
y
{
}
i
i
l l l =1 is the
1
the
classification
identifier
of of
xl ,x ,c1c and
c are
sample set
sample
set of
ofexception
exceptionclass,
class, yyll ==−1−1isis
the
classification
identifier
l 1 and c22 are
penalty factors,
factors,and
andξ i ξand
ξl relaxation
are relaxation
factors.
Using
the Lagrange
principle
to
penalty
ξ l are
factors.
Using
the Lagrange
principle
to solve
i and
the
above
optimization
problems,
there
are
solve the above optimization problems, there are

n

m m

n
n

m

i =1

l =1l =1

=1
ii=
1

l =1

n

m

βi ,Rβ2l )+=cR
+ cξ1i 
 β∑l ξlβ l ξ l
L( R, a, ξLi (, ξRl,,aα,iξ, iα, ξl ,l β, αi ,i β, αl )l ,=
+ξic2+ c∑2 ξξl l−− 
∑ββiξiiξ−
1 ∑
i−
2

i =1

n

l =1

mm
n



2 2
− ∑ α−i Rα2i −Rϕ2 (−xφi )( −
 −∑ααll φϕ(( xll )) −−aa22−−RR
xi )a−2 a+2 ξ+iξi−
++
ξl ξ l
i =1

i =1

(4)

l =11
l=

≥ 0 , αl ≥0,0 ,β iβ≥
0 and
, andβ l β≥
0 .The
Thefinal
finaldistance
distancefrom
fromany
any
test
sample
to
where αα
where
test
sample
z toz the
i ≥0,
l ≥0.
i i≥ 0, αl ≥
center
of the
D is obtained
as follows:
the center
ofsphere
the sphere
D is obtained
as follows:
v
n
n
n
u
n
n n ′
′
Du
=
K
z
,
z
−
2
α
K
z
,
x
+
αi α
K x ,x 
(
)
(
)
′


D = tK (z, z) − 2 ∑
α iK (z, xi )i + ∑
αi′ αjj K ( xii , x jj )
i =1 i
i =1 j∑
=1
i =1

(5)
(5)

i =1 j =1

where α ′i = yiα i and x j are of the same class as xi . If D ≤ R , this means that the test
where αi′ = yi αi and x j are of the same class as xi . If D ≤ R, this means that the test sample
sample is on or inside the hypersphere and belongs to the normal sample, ( y = +1) ; if
is on or inside the hypersphere and belongs to the normal sample, (y = +1); if D > R, the
D >sample
R , the test
sample
belongs
to thesample,
abnormal
test
belongs
to the
abnormal
(y =sample,
−1). ( y = −1) .
Support vector
ξi

a

R

S

Figure 2.
2. SVDD anomaly detection
detection diagram.
diagram.
Figure

Based
Based on
on the
the optimal
optimal set
set of
of special
special features
features screened
screened by
by MI,
MI, and
and also
also to
to obtain
obtain the
the
SVDD
model
with
a
better
generalization
performance,
this
paper
utilizes
the
SVDD-neg
SVDD model with a better generalization performance, this paper utilizes the SVDD-neg
algorithm
algorithm to
to achieve
achieve the
the anomaly
anomaly detection
detection of
of an
an adjustment
adjustment hydraulic
hydraulic servomotor.
servomotor.
3. Experiment Settings
3. Experiment Settings
This paper designs and conducts relevant tests using the high-pressure adjustment
This paper designs and conducts relevant tests using the high-pressure adjustment
hydraulic servomotor fault simulation test bench, as depicted in Figure 3. The structure of
hydraulic servomotor fault simulation test bench, as depicted in Figure 3. The structure of
the high-pressure adjustment hydraulic servomotor is a symmetrical cylinder with onethe high-pressure adjustment hydraulic servomotor is a symmetrical cylinder with onesided action. It is composed of a spring, cylinder, electro-hydraulic servo valve, throttle
sided action. It is composed of a spring, cylinder, electro-hydraulic servo valve, throttle
hole, oil filter, displacement, pressure sensor, electrical junction box, and valve block for
hole, oil filter, displacement, pressure sensor, electrical junction box, and valve block for
installing a quick-closing solenoid valve and inserted one-way valve. A pressure sensor
M3 is installed between the non-working chamber of the adjustment hydraulic servomotor
and the port B of the cartridge valve, pressure sensor M4 is installed between the throttle
hole C0 and the working chamber of the adjustment hydraulic servomotor, and pressure
sensor M5 is installed between the throttle hole D0 and the port A of the cartridge valve.
All three are installed by threaded holes.
Since the original three pressure sensors M3–M5 and one displacement sensor LVDT
cannot fully obtain system state information, this paper optimizes the layout of the measuring points by adding 5 new measuring points P5–P9 for pressure measurement based

Machines 2024, 12, 368

6 of 21

on the original measuring points. P5 is installed at the oil inlet of the system, P6 is installed at the working port of electro-magnetic directional valve 1 (left), P7 is installed
at the working port of electromagnetic directional valve 2 (right), P8 is installed at the
oil inlet of electromagnetic directional valve 1 (left), and P9 is installed at the oil inlet of
electromagnetic directional valve 2 (right). After that, this study realized the fault implantation of the adjustment hydraulic servomotor by replacing the faulty components
or artificially destroying the normal parts. A total of six fault states were set, including
in-cylinder leakage, spring breakage, solenoid valve throttle orifice blocked, spool zero
position internal leakage, solenoid valve internal leakage, and C0 throttle orifice clogged.
Machines 2024, 12, x FOR PEER REVIEW
6 of 22
The sensors’ layout design and the six fault settings are shown in Figure 4. Among them,
the leakage in the normal servo valve is 0.70 L/min, and the leakage in the worn servo valve
is 12.32 L/min. The solenoid valve internal leakage is simulated by replacing the internal
installing
a quick-closing
solenoid
and inserted
one-way
valve.
A pressure
sensor
leakage
solenoid
valve. The
normalvalve
diameter
of the solenoid
valve
front
throttle hole
is
M3
is
installed
between
the
non-working
chamber
of
the
adjustment
hydraulic
servomoφ = 0.8 mm, processing and replacing the smaller throttle hole diameter of φ = 0.5 mm; the
C0
diametervalve,
is φ =pressure
3 mm, processing
replacing
the throttle
hole
tor throttle
and thehole’s
port Bnormal
of the cartridge
sensor M4and
is installed
between
the throtdiameter
of and
φ = the
1 mm.
The in-cylinder
leakage
fault is simulated
byservomotor,
wearing theand
seal presring.
tle hole C0
working
chamber of
the adjustment
hydraulic
The
fault is simulated
by artificially
destroying
small
or
surespring
sensorbreakage
M5 is installed
between the
throttle hole
D0 and the internal
port A of
the spring
cartridge
cutting
a part
of are
theinstalled
spring. by threaded holes.
valve. All
three
1

2

3

4

5

6

7

8

9

10

Figure 3.
3. High-pressure
servomotor
fault
simulation
testtest
bench:
1: quick-closFigure
High-pressureadjustment
adjustmenthydraulic
hydraulic
servomotor
fault
simulation
bench:
1: quicking solenoid
valve;
2: M5
pressure
sensor;
3:3:M4
5: LVDT
LVDT
closing
solenoid
valve;
2: M5
pressure
sensor;
M4pressure
pressuresensor;
sensor;4:4:M3
M3 pressure
pressure sensor;
sensor; 5:
of 22 9: filter; and 10:
displacement sensor;
sensor; 6:
6: return
return pipe;
pipe; 7:
7: inlet
inlet pipe;
pipe; 8:
8: electro-hydraulic
electro-hydraulic servo
servo7 valve;
valve;
displacement
9: filter; and 10:
spring box.
spring box.

s 2024, 12, x FOR PEER REVIEW

Normal

Internal leakage

Since the
original
pressure sensors M3–M5 and one displacement sensor LVDT
Solenoid
valve internal three
leakage
P7
cannot fully obtain system stateP6information, this paper optimizes
the layout of the measuring points by adding 5 new measuring points P5–P9 for pressure measurement based
on the original measuring points.P8 P5 is installed at the oil inlet
of the system, P6 is installed
P9
at the working port of electro-magnetic directional valve
1
(left), P7 is installed at the
Solenoid valve throttle orifice blocked
working port of electromagnetic directional valve 2 (right), P8 is installed at the oil inlet
andBP9 is installed at the oil inlet of electroM3 of electromagnetic directional valve 1 (left),
B
magnetic directional valve 2 (right).AAfter that,
A this study realized the fault implantation
of
the
adjustment
hydraulic
servomotor
by
replacing
the faulty components or artificially
2mm
M5
destroying the normal parts. A total of six fault states were set, including in-cylinder leak1mm
A throttle
B
C0
D0
age,
spring
breakage, solenoid valve
orifice blocked, spool zero position internal
leakage, solenoid valve internal leakage, and C0 throttle orifice clogged. The sensors’ layP T
Spool zero position internal leakage
out design and the six fault settings are shown in Figure 4. Among them, the leakage in
theM4 normal servo valve is 0.70 L/min, and the leakage in the worn servo valve is 12.32
L/min. The solenoid valve internal leakage is simulated by replacing the internal leakage
solenoid valve. The normal diameter of the solenoid valve front throttle hole is φ = 0.8
LVDT
mm, processing and replacing the smaller throttle hole diameter of φ = 0.5 mm; the C0
throttle hole’s normal diameter is φ = 3P5 mm, processing and replacing the throttle hole
In-cylinder leakageof φ = 1 mm. The in-cylinder leakage fault is simulated by wearing the seal ring.
diameter
LVDT-Displacement
Sensor
The
spring breakage fault is simulated by artificially destroying the internal small spring
P 、M-Pressure sensors
P
T
or cutting a part of the spring.
C0 throttle orifice
clogged

Spring
breakage

Figure 4. Adjustment
hydraulic
servomotor
hydraulic
systemhydraulic
principles
and fault
settings.
Figure
4. Adjustment
hydraulic
servomotor
system
principles
and fault settings.

Finally, according to the above six fault states and normal states, the pressure of the
EH oil supply system is adjusted to 15 MPa; then, the adjustment hydraulic servomotor is
controlled by LabVIEW under the working condition of a frequency of 0.1 Hz and amplitude of 5%. The Machine Condition Monitoring (MCM_2.1.2.0) software was used to set
the sampling frequency to 12.5 kHz, each sampling time to 30 s, and each state to be sam-

Machines 2024, 12, 368

7 of 21

Finally, according to the above six fault states and normal states, the pressure of the
EH oil supply system is adjusted to 15 MPa; then, the adjustment hydraulic servomotor
is controlled by LabVIEW under the working condition of a frequency of 0.1 Hz and
amplitude of 5%. The Machine Condition Monitoring (MCM_2.1.2.0) software was used to
set the sampling frequency to 12.5 kHz, each sampling time to 30 s, and each state to be
sampled three times.
4. Abnormal Detection of Adjustment Hydraulic Servomotor
4.1. Feature Extraction and Feature Fusion
In this paper, a total of 17 time-domain characteristic parameters, such as mean value
and absolute mean value, were extracted to represent the amplitude fluctuation, power
fluctuation, and waveform distribution of the signal, respectively. At the same time,
this paper also extracted 13 frequency-domain characteristic parameters, such as the mean
value of frequency domain amplitude and frequency variance, to characterize the frequency
distribution of signals in the frequency domain and the degree of spectrum concentration.
In addition, the sensor information of each spatial position of the equipment is consistent and complementary, and the accuracy and generalization ability of the anomaly
detection model can be improved by using multi-sensor fusion technology to synthesize,
refine, and optimize the sensor information. According to the different resolutions of
data and processing processes, multi-sensor fusion technology can be divided into three
categories: data layer fusion, feature layer fusion, and decision layer fusion. The feature
layer fusion in the middle layer is to compress the information of the original data through
feature extraction, and then fuse it into a comprehensive feature through sequential splicing,
which is conducive to online real-time processing. This study pays attention to the effect of
the model in practical applications and has high requirements for real-time 8performance,
of 22
so “feature layer fusion” is chosen as the information fusion method. The specific process
of feature selection and fusion is shown in Figure 5.

OR PEER REVIEW

Same process for each state
State 1
Sequential
stitching of
3 csv files
(1125k×8)
State 7

Pressure Signal1
(1125k x 1)

Pressure Signal8
(1125k x 1)

Sample
Segmentation
(801×125k)

Feature extraction
(801×30)

Sample
Segmentation
(801×125k)

Feature extraction
(801×30)

Validation
(±1)
set
feature fusion
(801×240)

Stratified
sampling
divisions and
combinations

Training
(±1)
set
Test set (±1)

Figure 5. Flow chart ofFigure
feature
extraction
and feature
fusion.
5. Flow
chart of feature
extraction
and feature fusion.
Each step in the flow chart is described as follows:
Step 1: Longitudinally concatenate three consecutive data files in seven states, respectively, to concatenate
obtain seven data
files
with the shape
of (1125k
8). Then,
the data
files of the
Step 1: Longitudinally
three
consecutive
data
files in×seven
states,
respecseven
states
are
combined
to
obtain
three-dimensional
data
with
the
shape
of
(7
× 1125k
tively, to obtain seven data files with the shape of (1125k × 8). Then, the data files of the
× 8).
seven states are combined to obtain three-dimensional data with the shape of (7 × 1125k ×
Step 2: Separate samples of each state and signal by sliding window. To ensure that
8).
the sample contains at least one cycle of device operation data, the window and window
Step 2: Separatestack
samples
each
state
by sliding window.
To ensure that data
lengthsofare
set to
125kand
andsignal
1250, respectively.
Thus, the three-dimensional
× 1125k
8) areofconverted
to the four-dimensional
data of (7and
× 8window
× 800 × 125k).
the sample containsofat(7least
one×cycle
device operation
data, the window
That
is,
there
are
seven
states,
each
state
contains
eight
signals,
and
each
signal
stack lengths are set to 125k and 1250, respectively. Thus, the three-dimensional data ofgenerates
(7
800 samples, respectively, and the length of each sample is 125k.
× 1125k × 8) are converted
to the four-dimensional data of (7 × 8 × 800 × 125k). That is,
Step 3: Perform feature extraction on the samples obtained in step 2 based on the
there are seven states,
each 30
state
contains
eight domain
signals,features
and each
800 sam- from
selected
time
and frequency
andsignal
reduce generates
the feature dimension
125kthe
to 30
to obtain
an initial
feature
ples, respectively, and
length
of each
sample
issample
125k. set (7 × 8 × 800 × 30).
Step 4: extraction
Adopting ‘feature
level
fusion’ technology,
samples
Step 3: Perform feature
on the
samples
obtainedthe
in30-dimensional
step 2 basedfeature
on the
of eight pressure signals are spliced horizontally head to tail, resulting in a comprehensive

Each step in the flow chart is described as follows:

selected 30 time and frequency domain features and reduce the feature dimension from
125k to 30 to obtain an initial feature sample set (7 × 8 × 800 × 30).
Step 4: Adopting ‘feature level fusion’ technology, the 30-dimensional feature samples of eight pressure signals are spliced horizontally head to tail, resulting in a comprehensive feature sample with a dimensionality of 240, denoted as (7 × 800 × 240) 3-dimen-

Machines 2024, 12, 368

8 of 21

feature sample with a dimensionality of 240, denoted as (7 × 800 × 240) 3-dimensional
data. The “normal state” samples were separated, while the six “fault state” samples
were combined.
Step 5: Designate the “normal state” sample as the target for the SVDD-neg model
with the label set as ‘1’. Divide it into a positive example training set, positive example
verification set, and positive example test set using a ratio of ‘3:1:1’ through random
sampling division. The number of samples in the positive example training set is 480, the
positive example verification set is 160, and the positive example test set is 161.
Step 6: Set integer labels for the six “fault state” samples and divide them into a
counter-example training set, counter-example verification set, and counter-example test
set using hierarchical sampling division. The number of samples in the counter-example
training set is 479, the counter-example verification set is 160, and the counter-example test
set is 161. Then, set all counter-example sample labels as ‘−1’.
Step 7: Combine the positive example training set and negative example training set
into a mixed training set (label contains both ‘1’ and ‘−l’), combine the positive example
verification set and negative example verification set into a mixed verification set, and
combine the positive example test set and negative example test set into a mixed test set.
The results of the data set are shown in Table 1. In the training set, verification set, and
test set, not only is the number of positive and negative samples relatively balanced, but
the number of abnormal state samples in the negative samples is also balanced. In this way,
the SVDD-neg model can be ensured to tighten the decision boundary as much as possible
while paying attention to the positive samples and establishing its boundary description.
Table 1. SVDD experimental data arrangement.
State Type

Tag

Training Set

Verification Set

Test Set

Length of Sample

Normal
In-cylinder leakage
Spring breakage
Solenoid valve throttle orifice blocked
Spool zero position internal leakage
Solenoid valve internal leakage
C0 throttle orifice clogged

1
−1
−1
−1
−1
−1
−1

480
79
80
80
80
80
80

160
27
26
27
27
26
27

161
27
27
27
27
27
26

240
240
240
240
240
240
240

4.2. Wrapper-Type Feature Selection Based on MI and GA-SVDD-neg
4.2.1. Combined Optimization of MI-GA-SVDD-neg
The high-dimensional data after feature fusion will make the model computation grow
exponentially and easily lead to problems of high model complexity and low generalization
ability, so it is necessary to reduce the dimensionality of the feature set. By using the
feature selection algorithm, we can gain insight into the signal channels and feature names
that are sensitive to the state of the device, which is conducive to reducing the number
of sensors in the later stage and the promotion of this study to real-world applications.
Therefore, in this study, the MI feature selection algorithm is utilized to perform feature
screening on the 240-dimensional comprehensive feature set and is combined with the
GA-SVDD-neg algorithm as a wrapper-style feature selection algorithm to jointly optimize
the MI-GA-SVDD-neg.
Firstly, dimension reduction was performed on the training set, verification set, and
test set using the MI algorithm. It is assumed that, after dimensionality reduction, all three
data sets have a reduced dimensionality denoted as “m” (m ∈ A, A = {n|1 ≤ n ≤ 240}).
Subsequently, training, validation, and hyperparameter optimization were conducted
using the GA-SVDD-neg model on m-dimensional training sets and verification sets. The
accuracy value of the optimal model on m-dimensional test sets was then calculated as
a quantitative indicator “b” for evaluating compatibility between “the m-dimensional
feature set proposed by MI” and “GA-SVDD-neg”. The specific process of optimizing the
SVDD-neg hyperparameter by GA is described. The hyperparameters of the SVDD-neg

Machines 2024, 12, 368

sequently, training, validation, and hyperparameter optimization were conducted using
the GA-SVDD-neg model on m -dimensional training sets and verification sets. The accuracy value of the optimal model on m -dimensional test sets was then calculated as a
quantitative indicator “ b ” for evaluating compatibility between “the m -dimensional fea9 of 21

ture set proposed by MI” and “GA-SVDD-neg”. The specific process of optimizing the
SVDD-neg hyperparameter by GA is described. The hyperparameters of the SVDD-neg
algorithm consist of the positive case penalty factor ( c ) and the negative case penalty
algorithm consist of the positive case penalty factor (c11) and the negative case penalty
factor (c
( c22).).Additionally,
Additionally,aaradial
radialbasis
basiskernel
kernelfunction
function isis utilized
utilized to
to address
address the
the issue
issue of
of
factor
linearindivisibility
indivisibilityininthe
thedata.
data.Therefore,
Therefore,the
the
GA
needs
optimize
three
hyperparamelinear
GA
needs
to to
optimize
three
hyperparameters
including
the radial
basis basis
kernelkernel
function
parameter
γ at the γsame
time.
Thetime.
implementation
at the
same
The impleters including
the radial
function
parameter
of
the
GA-SVDD-neg
algorithm
proposed
in
this
study
is
shown
in
Figure
6:
mentation of the GA-SVDD-neg algorithm proposed in this study is shown in Figure 6:
Define the
fitness
function

Generating
the initial
population

Calculate the
fitness of each
chromosome in
the population

No

Selection of
the most
Yes
adapted
chromosome

Selection

Crossover

Schematic diagram of crossovervariation
cross-cutting point
Crossover

Is the number
of iterations
maxed out?

Variation

Variation

Renewal and
generation of
new stocks

Figure 6.
6. Genetic
Genetic algorithm
algorithm optimization
optimization flow
flow chart.
chart.
Figure

Step
Step 1:
1: Define
Define the
the fitness
fitness function
function of
of the
the GA
GA algorithm.
algorithm. Assume
Assume that
that the
the accuracy
accuracy of
of
the
SVDD-neg
model
on
m-dimensional
verification
set
is
a,
then
define
the
fitness
value
of
the SVDD-neg model on m -dimensional verification set is a , then define the fitness
the GA algorithm as (1 − a), and the iterative goal of the GA algorithm is to minimize the
fitness value of chromosomes in the m-dimensional verification set.
Step 2: Binary code a hyperparameter combination (c1 ,c2 ,γ) into a chromosome,
where c1 , c2 , γ all have values in the range [0.001, 1]. Then, the initial population with
50 chromosomes is randomly generated, and the maximum number of iterations is set to
10, and the mutation probability is set to 0.001.
Step 3: Initialize the SVDD-neg model based on the chromosomes in the population;
then, train the model on the m-dimensional training set and obtain the fitness value of each
chromosome on the m-dimensional validation set.
Step 4: Select chromosomes to enter the next generation population according to the
fitness value of chromosomes; at the same time, cross and mutate chromosomes according
to certain strategies and add the newly generated chromosomes to the next generation
population. Then, renew and create new populations.
Step 5: Determine whether the maximum number of iterations has been reached. If
no, return to Step 3. If yes, proceed to Step 6.
Step 6: Calculate and select the chromosome with the highest fitness value in the
new population and initialize the SVDD-neg model after decoding it into a combination
of hyperparameters. Finally, the model was retrained on the m-dimensional training set +
validation set, and the accuracy value of the model was calculated on the test set.
4.2.2. Comparative Study of Feature Selection Algorithms
To highlight the superiority of the MI-GA-SVDD-neg joint optimization algorithm, this
study adopts the same wrapper feature selection idea to combine and similarly co-optimize
the GA-SVDD-neg with the four dimensionality reduction methods of ANOVA, MRMR,
RFE, and PCA, respectively, to conduct a comparative study.
The specific comparative research process is shown in Figure 7:
Step 1: Select a dimensionality reduction method from five dimensionality reduction
algorithms.
Step 2: Use the selected method to reduce the feature dimension to m and calculate
the evaluation indicator b.

Machines 2024, 12, 368

optimize the GA-SVDD-neg with the four dimensionality reduction methods of ANOVA,
MRMR, RFE, and PCA, respectively, to conduct a comparative study.
The specific comparative research process is shown in Figure 7:
Step 1: Select a dimensionality reduction method from five dimensionality reduction
10 of 21
algorithms.
Step 2: Use the selected method to reduce the feature dimension to m and calculate
the evaluation indicator b .
Step
1 to
240240
and
repeat
step
2 until
m =m240.
Step 3:
3: Increase mmfrom
from
1 to
and
repeat
step
2 until
= 240.
Step
Step 4:
4: Repeat steps 1 to 3 until all feature dimensionality reduction
reduction algorithms
algorithms have
have
been
been traversed.
traversed.
Step
Figure
8. 8.
Step 5:
5: Summarize and plot
plot an
an analysis
analysis of
of b,bas
, asshown
showninin
Figure
240-dimensional
(±1)
validation set
240-dimensional
(±1)
training set
240-dimensional
(±1)
test set

Choose a feature
selection or feature
dimensionality
reduction algorithm

GA iterates and
optimises SVDD_neg
on the training,
validation sets with
feature dimensions of m

Get training set,
validation set, test set
with feature dimension m
(initial value of m is 1)

Yes

m+1

Gets the precision
value b of SVDD on
the test set with the
feature dimension m

m<240
No

Yes
Summary of
results and
mapping analyses

No

There are other
algorithms?

Save the 240 precision values
b corresponding to this feature
selection or dimensionality
reduction algorithm

Figure 7.
7. Flow chart
chart of
of comparative
comparative study
study of
of feature
feature selection
selection algorithms.
algorithms.
Figure

From
From Figure
Figure 8,
8, itit can
can be
be seen
seen that
that the
the effect
eﬀect of
of the
the GA-SVDD-neg
GA-SVDD-neg model
model begins
begins to
to
deteriorate
the feature
featuredimension
dimensionrises
risesand
and
shows
increasingly
violent
oscillations,
deteriorate as the
shows
increasingly
violent
oscillations,
inMachines 2024, 12, x FOR PEER REVIEW
11 ofthe
22
indicating
that
high-dimensional
features
contain
redundant
features.
dicating that
thethe
high-dimensional
features
do do
contain
redundant
features.
For For
the
disdistance-based
SVDD-neg
model,
the existence
of redundant
features
will to
lead
the
tance-based SVDD-neg
model,
the existence
of redundant
features
will lead
theto
probproblem
of
data
sparsity
in
the
high-dimensional
feature
space,
which
increases
the
risk
lem of data sparsity in the high-dimensional feature space, which increases the risk of
of
model
thus
reducing
model overfitting
overfitting and
and makes
makesthe
themodel
modelmore
moresensitive
sensitivetotosmall
smalldata
datachanges,
changes,
thus
reducthe the
stability
of the
model,
which
reflects
the necessity
of “feature
selection”.
ing
stability
of the
model,
which
reflects
the necessity
of “feature
selection”.

Comparison of
of the eﬀect
effect of each feature selection algorithm.
Figure 8. Comparison

For aa certain
i, ifithe
dimension
is reduced
For
certain feature
featuredimension
dimensionreduction
reductionmethod
method
, if feature
the feature
dimension
is reto
m
by
the
i
method
and
the
evaluation
indicator
b
=
100%,
then
the
current
m
is
identified
m
duced to
by the i method and the evaluation indicator b = 100% , then the current
as
feature
anddimension
defined asand
mi .defined
Assuming
all mi of the i method
m aisgood
identified
as adimension
good feature
as mthat
i . Assuming that all mi of
constitute a good dimension set B (B ⊆ A), then the higher number of elements in set B
the i method constitute a good dimension set B ( B ⊆ A ), then the higher number of
represents the higher robustness of the GA-SVDD-neg model to the i algorithm. Further, a
elements in set B represents the higher robustness of the GA-SVDD-neg model to the
comparative study of these dimensionality reduction methods allows the selection of the
i algorithm. Further, a comparative study of these dimensionality reduction methods almost robust feature reduction algorithm and its corresponding optimal feature dimension
lows the selection of the most robust feature reduction algorithm and its corresponding
k, k = Bmin . Accordingly, it can be seen from the analysis of Figure 8 that, on the one hand,
optimal
dimension
. Accordingly,
be seen
from
analysis
of
k , k = Bminincreases
when thefeature
number
of feature selections
from 8 it
tocan
47, the
feature
setthe
selected
based
Figure
8
that,
on
the
one
hand,
when
the
number
of
feature
selections
increases
from
8
to
on MI algorithm can make the accuracy of GA-SVDD-neg model reach 100%, indicating
47, the feature set selected based on MI algorithm can make the accuracy of GA-SVDDneg model reach 100%, indicating that the GA-SVDD-neg model has the strongest robustness to the MI algorithm; on the other hand, the MI algorithm only needs to select six
features to make the accuracy of the GA-SVDD-neg reach 100%, indicating that, compared
with other algorithms, the MI algorithm preferentially selects the features most suitable
for the GA-SVDD-neg model.

Machines 2024, 12, 368

11 of 21

that the GA-SVDD-neg model has the strongest robustness to the MI algorithm; on the
other hand, the MI algorithm only needs to select six features to make the accuracy of
the GA-SVDD-neg reach 100%, indicating that, compared with other algorithms, the MI
algorithm preferentially selects the features most suitable for the GA-SVDD-neg model.
To further verify the effectiveness of the six features proposed by “mutual information”
and the applicability of this feature set with GA-SVDD-neg, on the one hand, this paper uses
the t-Distributed Stochastic Neighbor Embedding (t-SNE) dimension reduction algorithm
to reduce and visually analyze the original 240-dimensional features and the 6-dimensional
features proposed by MI, respectively. Figure 9a shows a obvious overlap phenomenon
between normal and abnormal samples in the spatial distribution of the 240 dimensional
feature set, while Figure 9b shows a significant difference in the spatial distribution of
normal and abnormal samples in the 6-dimensional feature set. On the other hand, this
paper uses the GA algorithm to optimize SVDD-neg 30 times in the 6-dimensional feature
set and 240-dimensional feature set, respectively, and the optimization process each time
is the same as the calculation process of GA-SVDD-neg described in Section 4.2.1. Finally,
the 30 accuracy values corresponding to the two feature sets are plotted in Figure 9c. The
accuracy of GA-SVDD-neg is above 99.5% in 30 tests based on a six-dimensional feature
set, and most of them can reach 100%. However, the accuracy of GA-SVDD-neg fluctuates
Machines 2024, 12, x FOR PEER REVIEW
12 of 22
greatly in 30 tests for 240-dimensional features, only reaching 100% five times, and even
only 92.857% in the 20th test. The above results are consistent with the conclusion in
Figure 8 that “the existence of redundant features in high-dimensional features will lead
also
that the six
features
selected
by MI have strong
applicability
and that
robustness
to
theprove
deterioration
of the
stability
of GA-SVDD-neg
model”,
and also prove
the six
with
the
GA-SVDD-neg
algorithm.
Based
on
this,
this
paper
finally
selects
the
MI
method
features selected by MI have strong applicability and robustness with the GA-SVDD-neg
for feature Based
selection
and this
selects
sixfinally
sensitive
features
ofmethod
the P9 pressure
such
as
algorithm.
on this,
paper
selects
the MI
for featuresignal,
selection
and
variation
frequency
variance,
peak
value,
square root
selects
sixrate,
sensitive
features
of the waveform
P9 pressureindex,
signal,
such
as variation
rate,amplitude,
frequency
and eﬀective
value. index, peak value, square root amplitude, and effective value.
variance,
waveform

overlapping

(a)

(b)

(c)

Figure 9.
9. Comparative
(a)(a)
visualization
of the
original
feature
t-SNE;
(b)
Figure
Comparativestudy
studyofoftwo
twofeature
featuresets:
sets:
visualization
of the
original
feature
t-SNE;
visualization of 6-dimensional features t-SNE filtered by MI algorithm; and (c) comparison of ro(b) visualization of 6-dimensional features t-SNE filtered by MI algorithm; and (c) comparison of
bustness and applicability.
robustness and applicability.

4.2.3.
4.2.3. Comparison of Model Training
Training and
and Testing
TestingTime
Time
In addition,
addition, “feature
“feature selection”
selection” can
can not
not only
only improve
improve the
the generalization
generalization of
of the
the model
but also
also reduce
reduce the
the training
training and
and testing
testing time
time of
of the
the model,
model, which
which is
is of
of great
great significance
significance
for the
the application
application of
of the
the SVDD-neg
SVDD-neg model.
model. In this paper,
paper, the
the model
model of
of GA-SVDD-neg
GA-SVDD-neg
algorithm 30 times
times optimization
optimizationisisanalyzed.
analyzed.The
The
training
time
on the
“training
+
training
time
on the
“training
set +set
ververification
set”
and
the
test
time
on
the
“test
set”
are
summarized,
as
shown
in
Figure
10.
ification set” and the test time on the “test set” are summarized, as shown in Figure
Compared
Compared with
with the
the 240-dimensional
240-dimensional feature,
feature, the
the training
training time
time and
and test
test time
time of SVDD-neg
on
the
6-dimensional
feature
are
both
reduced,
and
the
reduction
in
the
on the 6-dimensional feature are both reduced, and the reduction in the test
test time
time is
is more
more
obvious.
of of
thethe
model
in real-time
fault
detection.
obvious. This
Thisisisvery
veryconducive
conducivetotothe
thedeployment
deployment
model
in real-time
fault
detecThe
minimum,
andand
maximum
values
of of
thethe
training
and
tion.average,
The average,
minimum,
maximum
values
training
andtesting
testingtimes
timesof
of the
the
statistical model are shown in Table 2. According to the statistical indicator of “average”,
the training time is reduced by about 8.1%, 76 ms, and the test time is reduced by about
28.5%, 3 ms. Considering that the order of training and testing time of the model is small,
this degree of reduction eﬀect is already incredibly significant. The experimental analysis
of this study was completed on the same computer, which was configured as Intel Core

Machines 2024, 12, 368

12 of 21

x FOR PEER REVIEW

13 of 22

statistical model are shown in Table 2. According to the statistical indicator of “average”,
the training time is reduced by about 8.1%, 76 ms, and the test time is reduced by about
28.5%, 3 ms. Considering that the order of training and testing time of the model is small,
this degree of reduction effect is already incredibly significant. The experimental analysis
of this study was completed on the same computer, which was configured as Intel Core i5Machines 2024, 12, x FOR PEER REVIEW
12400F (2.50 GHz), 32 GRAM, and NVIDIA GeForce RTX 3060Ti (8 GB). The development
environment was scikit-learn 0.24.2+python 3.6.2 and tensorflow-gpu2.10.0+python 3.8.18.

(a)

(b)

Figure 10. Training time and test time comparison: (a) comparison of training time; (b) test time
comparison.
(a)
(b)
Table 2. Comparison of training time and test time for two feature sets.

c

ns

Figure
and test time
comparison:of(a)
comparison
of training
Figure 10. Training
time 10.
andTraining
test timetime
comparison:
(a) comparison
training
time; (b)
test timetime; (b) t
comparison.
comparison.
Training Time (s)
Test Time (s)

Training + Verifica- Test
Mean Table
Minimum
Maximum
Mean
Maximum
Table 2. Comparison
of training
time
and
timetime
for
two
sets.
2. Comparison
of test
training
andfeature
testMinimum
time
for two feature
sets.
tion Set
Set
Value
Value
Value
Value
Value
Value Test Time (s)
Training Time (s)Test Time (s)
Training Time (s)
Characteristic
Training
+
VerificaTest
Test
Training
+
Characteristic
1
640
161Label
Mean
Minimum Mean
Maximum
MeanMaximum
MinimumMean
Maximum
Label
Minimum
Minimum Max
Set
Verification Set
Dimension
0.93304
0.86917
1.09226
0.0115
0.01
0.013 Value
tion
Set
Dimension
ValueSet
Value
Value
Value
Value
−1
639
161
Value
Value
Value
Value
Value
V
1
640
161
240
0.93304
0.86917
1.09226
0.0115
0.01
0.013
1
640
161
1 dimensions
640
−
1 dimensions
639 161
161
240
0.93304
0.86917 0.007
1.09226 0.01157
0.0115
0.01
0
0.85739
0.75157
1.06117
0.00822
−1
639
161
−1
639
1
640 161
161

Label

6 dimensions

−1

639

6 dimensions

1
−1

0.85739

0.75157

1.06117
0.00822
0.007
0.01157
161
0.85739 0.75157
1.06117
0.00822
0.007
161

640
639

161

4.3. GA-SVDD-neg Analysis of Abnormal Detection Results

0.0

4.3. GA-SVDD-neg Analysis of Abnormal Detection Results

The GA-SVDD-neg fault detection
process is
shown
in FigureDetection
11. In this
paper, for
4.3. GA-SVDD-neg
Analysis
of Abnormal
Results
The GA-SVDD-neg fault detection process is shown in Figure 11. In this paper, for the
the six-dimensional
training,
validation,
and
test
sets
obtained
from
MI,
the
three
datasets
The validation,
GA-SVDD-neg
faultsets
detection
process
is shown
in Figure
11.are
In this pap
six-dimensional training,
and test
obtained
from MI,
the three
datasets
are firstly pre-processed
in
a
standardized
way,
and
the
SVDD-neg
is
trained,
optimized,
the
six-dimensional
training,
validation,
and
test
sets
obtained
from
MI,
the
firstly pre-processed in a standardized way, and the SVDD-neg is trained, optimized, and three d
are
firstly
pre-processed
in process
a standardized
way,
and
the
SVDD-neg
is The
trained, opti
and tested according
to the
GA-SVDD-neg
optimization
described
in Section
4.2.1.
tested
according
to the
GA-SVDD-neg
optimization
process
described
in Section
4.2.1.
and
tested
according
to
the
GA-SVDD-neg
optimization
process
described
in Sectio
hyperparameters
the final SVDD-neg
model
are shown
in Table
The hyperparameters
of the final of
SVDD-neg
model are
shown
in Table
3. 3.
The hyperparameters of the final SVDD-neg model are shown in Table 3.

6-dimensional
(±1)
validation set
6-dimensional
(±1)
training set
6-dimensional
(±1)
test set

GA-SVDD_neg
6-dimensional
(±1)
training,
validation set validation,

GA-SVDD_neg
Optimal
decision surface
training,
forvalidation,
hyperspheres
optimisation

optimisation
Standardised
Standardised 6-dimensional(±1)
training
set
pre-processing
pre-processing
SVDD_neg anomaly
6-dimensional
(±1)
detection model
test set
(a, R )

Optimal decision su
for hypersphere

SVDD_neg anomaly
Normal
detection
model
(a, R )

Abnormal

No

Abn

Figure 11. GA-SVDD-neg fault detection flow.

Figure 11. GA-SVDD-neg
detection flow.
Figure fault
11. GA-SVDD-neg
fault detection flow.
Table 3. Final SVDD-neg model hyperparameter.

Table 3. Final SVDD-neg
model hyperparameter.
Radial Kernel Support Vector
Parameter Penalty FacPercentage of
Penalty Factor c2
Parameters
γ
tor
c
Name
Count Hypersphere
Support Vectors
Penalty FacRadial1 Kernel Support Vector
Percentage of
Penalty Factor
c2
Parameter
Parameters
γ 0.72095632
tor c 1
Count 0.97008421
Support Vectors
Radius
0.93561615
3
0.2346%
value

0.93561615

0.72095632

0.97008421

3

0.2346%

0.400601

Hypers
Radi

0.400

To visually display the “decision boundary” formed by the SVDD-neg mod

Machines 2024, 12, 368

13 of 21

Table 3. Final SVDD-neg model hyperparameter.
Parameter
Name

Penalty Factor
c1

Penalty Factor
c2

Radial Kernel
Parameters γ

Support Vector
Count

Percentage of
Support Vectors

Hypersphere
Radius

Parameter
value

0.93561615

0.72095632

0.97008421

3

0.2346%

0.400601

Machines 2024, 12, x FOR PEER REVIEW

To visually display the “decision boundary” formed by the SVDD-neg model after the
training process, the PCA algorithm was used in this paper to reduce the six-dimensional
model
can
not dimensions
only correctly
distinguish
normal
abnormalmodel,
samples,
but also
collection
to two
and then
train and optimize
theand
GA-SVDD-neg
and the
decision boundary
of thetypes
modelon
wasthe
finally
drawn, as scale,
shown which
in Figureverifies
12a. Thethe
model
can
distinguish
six fault
“distance”
applicability
not only correctly
distinguish
normal
samples,
but also
distinguish hydraulic
six
SVDD-neg
model
in the field
of and
theabnormal
abnormal
detection
of clearly
an adjustment
fault types on the “distance” scale, which verifies the applicability of the SVDD-neg model
motor.
Figure 12b shows the ROC curve of the current SVDD-neg model on the t
in the field of the abnormal detection of an adjustment hydraulic servomotor. Figure 12b
An
AUC
of 1 curve
indicates
that the
eﬀect of
theoncurrent
SVDD-neg
has reach
shows
the ROC
of the current
SVDD-neg
model
the test set.
An AUC ofmodel
1 indicates
that the effect
the there
currentisSVDD-neg
has reached
the optimal
level which
and there
is
optimal
levelofand
no need model
to further
optimize
the model,
verifies
the
no
need
to
further
optimize
the
model,
which
verifies
the
superiority
of
GA
in
optimizing
riority of GA in optimizing SVDD-neg hyperparameters.
SVDD-neg hyperparameters.

(a)

(b)

Figure 12.
boundary
and ROC
training(a)
settraining
decision boundary;
(b) ROC
graph for (b) ROC
Figure
12.Decision
Decision
boundary
andcurve:
ROC(a)curve:
set decision
boundary;
SVDD-neg.
for SVDD-neg.

4.4. A Comparative Study of Anomaly Detection Algorithms

4.4. AToComparative
Study ofofAnomaly
Detection
Algorithms
verify the superiority
the GA-SVDD-neg
algorithm
proposed in this paper in the

field To
of the
abnormal
detection of an
hydraulic servomotor,
it was
compared
verify
the superiority
ofadjustment
the GA-SVDD-neg
algorithm
proposed
in this pa
with GA-SVDD and PSO-SVDD. According to the six features mentioned in Section 4.2.2,
the field of the abnormal detection of an adjustment hydraulic servomotor, it wa
the MI algorithm was used in this study to reduce the normal sample training set and
pared
with set
GA-SVDD
According
to the sixrespectively,
features mentioned
in S
verification
divided inand
StepPSO-SVDD.
5 of Section 4.1
to six dimensions,
for the
4.2.2,
theand
MIoptimization
algorithmofwas
used and
in this
study models.
to reduce
normal
sample
training
GA-SVDD
PSO-SVDD
The the
test set
remained
the train
same
as
GA-SVDD-neg.
After
several
iterations
of
optimization,
this
paper
presents
the
and verification set divided in Step 5 of Section 4.1 to six dimensions, respectively,
optimal test
of the threeof
algorithms,
as shown
in Figure 13. models. The test set remain
training
andresults
optimization
GA-SVDD
and PSO-SVDD

same as GA-SVDD-neg. After several iterations of optimization, this paper prese
optimal test results of the three algorithms, as shown in Figure 13.

Machines 2024, 12, 368

the field of the abnormal detection of an adjustment hydraulic servomotor, it was compared with GA-SVDD and PSO-SVDD. According to the six features mentioned in Section
4.2.2, the MI algorithm was used in this study to reduce the normal sample training set
and verification set divided in Step 5 of Section 4.1 to six dimensions, respectively, for the
training and optimization of GA-SVDD and PSO-SVDD models. The test set remained the
same as GA-SVDD-neg. After several iterations of optimization, this paper presents the 14 of 21
optimal test results of the three algorithms, as shown in Figure 13.

Machines 2024, 12, x FOR PEER REVIEW

15 of 22

(a)

(b)

Judgment error

(c)

(d)

(e)

(f)

Judgment error

Figure 13.
13. Comparison
results
of three
algorithms:
(a) GA-SVDD-neg
sample
distance–radius;
Figure
Comparisonofoftest
test
results
of three
algorithms:
(a) GA-SVDD-neg
sample
distance–radius;
(b) GA-SVDD-neg confusion matrix; (c) GA-SVDD sample distance–radius; (d) GA-SVDD confu(b)
GA-SVDD-neg
confusion
matrix;
(c)
GA-SVDD
sample
distance–radius;
(d)
GA-SVDD
confusion
sion matrix; (e) PSO-SVDD sample distance–radius; and (f) PSO-SVDD confusion matrix.
matrix; (e) PSO-SVDD sample distance–radius; and (f) PSO-SVDD confusion matrix.

It can be seen from Figure 13a that the distance from the normal samples to the center
can be seen is
from
Figure
that thethat
distance
from the normal
samples
to the center
of theIthypersphere
all less
than13a
the radius;
is, the GA-SVDD-neg
model
determines
of
the
hypersphere
is
all
less
than
the
radius;
that
is,
the
GA-SVDD-neg
model
determines
all normal samples as normal. The distance from the abnormal samples to the center
of
all
normal
samples
as
normal.
The
distance
from
the
abnormal
samples
to
the
center of
the hypersphere is much larger than the radius; that is, the GA-SVDD-neg model not only
the
hypersphere
is muchsamples
larger than
the radius;
GA-SVDD-neg
not only
determines
all abnormal
as abnormal
but that
also is,
hasthe
a strong
diﬀerencemodel
between
determines
all abnormal
abnormal
but also
has a strong
difference
between
the distance distribution
of samples
abnormalas
samples
and normal
samples.
The confusion
matrix
in Figure
13bdistribution
shows that the
and
recall indicator
values
of the model
on the testmatrix
the
distance
of accuracy
abnormal
samples
and normal
samples.
The confusion
setFigure
both reach
100%, which
reflects
the powerful
generalization
abilityof
ofthe
the model
GA-SVDDin
13b shows
that the
accuracy
and recall
indicator values
on the test
negboth
algorithm.
Figure which
13c,d show
that,the
in powerful
GA-SVDD,generalization
all abnormal samples
correctly
set
reach 100%,
reflects
abilityare
of the
GA-SVDDidentified,
but one
normal
sample
misjudged
as abnormal.
Figure 13e,f
show that,
in
neg
algorithm.
Figure
13c,d
showisthat,
in GA-SVDD,
all abnormal
samples
are correctly
PSO-SVDD,
all
abnormal
samples
are
correctly
classified,
but
two
normal
samples
are
identified, but one normal sample is misjudged as abnormal. Figure 13e,f show that, in
misjudged as abnormal samples. The results show that GA-SVDD-neg has a stronger generalization ability than GA-SVDD and PSO-SVDD, and GA is more suitable for the optimization of SVDD hyperparameters than PSO. In this paper, the accuracy rate, recall rate,
F1 score, and overall accuracy indicator statistics of the three models on the test set are
shown in Table 4:

Machines 2024, 12, 368

15 of 21

EER REVIEW

100

16 of 22
PSO-SVDD, all abnormal samples are correctly classified, but two normal samples are
misjudged as abnormal samples. The results show that GA-SVDD-neg has a stronger
generalization ability than GA-SVDD and PSO-SVDD, and GA is more suitable for the
99.38 of100
99.69
98.77
100 the99.38
optimization
SVDD hyperparameters
than PSO.
In this paper,
accuracy rate, recall
rate, F1 score, and overall accuracy indicator statistics of the three models on the test set
are shown in Table 4:

100

It can be seen from the above table that GA-SVDD-neg is superior to GA-SVDD and
Table
4. The
results of the
three algorithms.
PSO-SVDD in terms of
each
indicator
value.
The results show that, when there are negative
examples, the
GA-SVDD-neg algorithm GA-SVDD
can be used for anomaly detection
Method
GA-SVDD-neg
PSO-SVDD to obtain
F1F1F1Precision
Recall
Accuracy
Precision
Recall
Accuracy
Precision
Recall
Indicators/%
a model with
stronger
generalization
and robustness,
falseAccuracy
posScore
Score and eﬀectively reduce the
Score
Normal
100
100
100
100
99.38
99.69
100
98.76
99.38
itive
rate of100the model.
It is of100great significance
to99.69
the application
and popularization
of
99.69
99.38
Abnormal
100
100
99.38
100
98.77
100
99.38
the model in the industrial scene.

It can be seen from the above table that GA-SVDD-neg is superior to GA-SVDD and

5. Fault Diagnosis of PSO-SVDD
Adjustment
Hydraulic
Servomotor
Basedshow
on that,
1DCNN
in terms
of each indicator
value. The results
when there are negative

examples, the GA-SVDD-neg algorithm can be used for anomaly detection to obtain a

5.1. DCNN Structure Design
model with stronger generalization and robustness, and effectively reduce the false positive

rate ofhydraulic
the model. Itservomotor
is of great significance
to the
of the
After the adjustment
is judged
toapplication
be faultyand
bypopularization
the GA-SVDDmodel in the industrial scene.
neg model, it is necessary to determine the fault location and fault type. In this paper,
Fault Diagnosis of
Servomotor
Based on 1DCNN
based on 1DCNN, the5.characteristics
ofAdjustment
pressure Hydraulic
signals were
automatically
extracted and
5.1.
DCNN
Structure
Design
classified, and an end-to-end fault diagnosis model for the adjustment hydraulic servoAfter the adjustment
hydraulic
servomotor and
is judged
to be
faulty by theof
GA-SVDD-neg
motor was constructed. Finally,
the pattern
recognition
fault
diagnosis
six fault
model, it is necessary to determine the fault location and fault type. In this paper, based on
states and normal states
of the
hydraulic
servomotor
are realized.
1DCNN,
theadjustment
characteristics of
pressure signals
were automatically
extracted and classified,
an end-to-end
fordesigned
the adjustment
hydraulic
was
The structure andand
parameters
offault
the diagnosis
1DCNNmodel
model
in this
paperservomotor
are shown
constructed.
Finally,
the
pattern
recognition
and
fault
diagnosis
of
six
fault
states
and
in Figure 14, which includes three parts: the input layer, feature extraction layer, and clasnormal states of the adjustment hydraulic servomotor are realized.
sification layer. First, the original
signal
is segmented
and transmitted
directly
to theareinput
The structure
and parameters
of the 1DCNN
model designed
in this paper
shown
in Figure 14,layers
which includes
three
parts: theininput
layer, feature
extraction
layer, and
layer. The three convolutional
are then
arranged
alternating
rows
with each
of
classification
layer.
First,
the
original
signal
is
segmented
and
transmitted
directly
to
the
the three pooling layers, which together constitute the feature extraction layer. Among
input layer. The three convolutional layers are then arranged in alternating rows with each
them, the convolutionoflayer
uses
multiple
the original
the three
pooling
layers,convolution
which together kernels
constitute to
theextract
feature extraction
layer. presAmong
them,
the convolution
layer uses
multiple
convolution
kernels to extract
original
sure signal of the input
layer,
and the pooling
layer
reduces
the dimension
of thethe
feature
pressure
signal
of the input
layer,making
and the these
poolingfeatures
layer reduces
the dimension
of the
vector by the maximum
pooling
operator
while
insensitive
to transfeature vector by the maximum pooling operator while making these features insensitive
lation, oﬀset, and small
distortion.
After
featureAfter
vectors
are
reorganized
oneto translation,
offset,
andthat,
smallall
distortion.
that, all
feature
vectors areinto
reorganized
dimensional vectors by
adding
the Flatten
layer
layer,
andpooling
Dropout
into
one-dimensional
vectors
by after
addingthe
thethird
Flattenpooling
layer after
the third
layer,
and
Dropout
is
added
to
prevent
overfitting.
Finally,
a
classification
layer
composed
is added to prevent overfitting. Finally, a classification layer composed of three fully con-of
three fully connected layers is added, and the classification output is performed by the
nected layers is added,Softmax
and the
classification output is performed by the Softmax classifier.
classifier.
1024

1020×128

340×128

336×256

67×256

63×512

12×512

6144

6144

512

512

7

Samples

Sample Input

Conv1D

MaxPooling1D

Conv1D

MaxPooling1D

Conv1D

MaxPooling1D Flatten

Dropout Dense1 Dense2 Output

Figure
14. CNN structure chart.
Figure 14. CNN structure
chart.

5.2. Data Acquisition and Parameter Setting
According to the results of the MI feature selection algorithm in Section 4.2.2, the P9

Machines 2024, 12, 368

16 of 21

5.2. Data Acquisition and Parameter Setting
According to the results of the MI feature selection algorithm in Section 4.2.2, the P9
pressure signal containing the most sensitive features is selected as the data source of the
1DCNN model. In this paper, a window of 1024 length is used to slice the P9 signals of
each state, and it is marked with integer labels. A total of 7000 samples were obtained for
seven states, of which 1000 samples were obtained for each state and the sample dimension
was 1024. Finally, according to the ratio of 3:1:1, 7000 samples are divided into training sets,
verification sets, and test sets via “stratified sampling division”. The details of the 1DCNN
experimental data set are shown in Table 5.
Table 5. 1DCNN experimental data arrangement.
Categories

Labels

Training Set Size

Validation Set Size

Test Set Size

Normal
In-cylinder leakage
Spring breakage
Solenoid valve throttle orifice blocked
Spool zero position internal leakage
Solenoid valve internal leakage
C0 throttle orifice clogged

0
1
2
3
4
5
6

600
600
600
600
600
600
600

200
200
200
200
200
200
200

200
200
200
200
200
200
200

After adjusting the model parameters several times and comparing and analyzing the
training effect, the relevant settings and parameters of the model were finally determined,
as shown in Table 6. In this paper, the ReLU activation function and the Dropout technique
are used to prevent model overfitting and enhance the robustness of the model. After that,
to reduce the dependence on the learning rate scheduler, we chose the RMSprop optimizer
that can adaptively adjust the learning rate to update the parameters of the model, and,
at the same time, to make the model converge as soon as possible in the early stage of the
training period, the initial learning rate was set to 0.002 and the number of batches was set
to 20. Finally, the Epochs were set to 250 to ensure that the model could be fully trained.
Table 6. 1DCNN hyperparameter settings.
Parameter
Name
Parameter
value

Name

Optimiser
Learning Rate

Decay Rate

Loss Function

Indicator

Epochs

Batch Size

Dropout

RMSProp

0.002

0.9

categorical_crossentropy

accuracy

250

20

0.5

5.3. Result Analysis
The 1DCNN hyperparameter values shown in Table 6 were used to initialize the
model, and then the partitioned training and validation sets were passed to the model
for training and iteration. In this paper, the accuracy and loss values of the model on the
training set and the verification set in the iterative process were, respectively, drawn, as
shown in Figure 15a,b. As can be seen from the figure, with the continuous optimization of
parameters in 1DCNN, the accuracy rate of the model on the training set and verification
set rapidly increased to 100% and gradually became stable, and the loss of the model on the
training set and verification set rapidly decreased to 0 and gradually became stable. The
results show that the RMSProp optimizer selected in this paper and its related parameter
settings can instantly search the location of the optimal solution in the parameter space
and converge.

Machines 2024, 12, 368

of parameters in 1DCNN, the accuracy rate of the model on the training set and verification set rapidly increased to 100% and gradually became stable, and the loss of the model
on the training set and verification set rapidly decreased to 0 and gradually became stable.
The results show that the RMSProp optimizer selected in this paper and its related parameter settings can instantly search the location of the optimal solution in the parameter
17 of 21
space and converge.

Machines 2024, 12, x FOR PEER REVIEW

18 of 22

Figure 15. 1DCNN training curve: (a) accuracy curve; (b) loss curve.
(a)
(b)
Figure
15. consistent
1DCNN training
(a) accuracyincurve;
loss curve.
The
“blackcurve:
box problem”
deep(b)
learning
makes it diﬃcult for us to understand and explain the inner workings of convolutional neural networks. To explore the
The mode
consistent
problem”
in deep
learningthis
makes
it difficult
us to
learning
and “black
featurebox
extraction
ability
of 1DCNN,
paper
uses thefor
trained
understand
and
explain
the
inner
workings
of
convolutional
neural
networks.
To
explore
1DCNN model to predict the test set, extracts the feature data output from the penultithe learning
mode and
feature
ability of 1DCNN,
paper
uses the trained
mate
fully connected
layer
in theextraction
forward propagation
process this
of the
convolutional
neural
1DCNN
model
to
predict
the
test
set,
extracts
the
feature
data
output
from
thevisualize
penultimate
network, and uses the t-SNE algorithm to reduce the dimensionality and
the
fully connected layer in the forward propagation process of the convolutional neural
feature data, as shown in Figure 16a. Meanwhile, at the same time, t-SNE was used to
network, and uses the t-SNE algorithm to reduce the dimensionality and visualize the
perform the same dimensionality reduction and visualization for test set samples, as
feature data, as shown in Figure 16a. Meanwhile, at the same time, t-SNE was used
shown in Figure 16b. By comparing the two, it can be found that samples of various cateto perform the same dimensionality reduction and visualization for test set samples, as
gories of the original data are initially mixed, but after 1DCNN convolution and full conshown in Figure 16b. By comparing the two, it can be found that samples of various
nection calculation, the clustering eﬀect of various samples is obvious and can be clearly
categories of the original data are initially mixed, but after 1DCNN convolution and full
distinguished. The 1DCNN model can automatically extract high-quality feature data
connection calculation, the clustering effect of various samples is obvious and can be clearly
from the original pressure data of the adjustment hydraulic servomotor.
distinguished. The 1DCNN model can automatically extract high-quality feature data from
the original pressure data of the adjustment hydraulic servomotor.

(a)

(b)

Figure 16. 1DCNN
1DCNN feature
feature map
map visualization
visualization analysis:
analysis: (a)
(a) 1DCNN
1DCNN feature
feature map
map t-SNE
t-SNE visualization;
visualization;
(b)
original
sample
t-SNE
visualization.
(b) original sample t-SNE visualization.

To test the generalization ability of the model and the eﬀectiveness of the selected P9
signal relative to other signals, this paper adopts the same processing flow, uses the hyperparameters in Table 6 to train and test IDCNN on each signal, respectively, and takes
the recall rate of a single fault type as an indicator to draw the confusion matrix, as shown
in Figure 17.

Machines 2024, 12, 368

18 of 21

To test the generalization ability of the model and the effectiveness of the selected
P9 signal relative to other signals, this paper adopts the same processing flow, uses the
hyperparameters in Table 6 to train and test IDCNN on each signal, respectively, and takes
Machines 2024, 12, x FOR PEER REVIEW
of 22
the recall rate of a single fault type as an indicator to draw the confusion matrix, as 19
shown
in Figure 17.

Accuracy=0.9993

Accuracy=0.9993

Accuracy=0.9993

(a)

(b)

Accuracy=0.9971

(c)

Accuracy=0.9993

(d)

Accuracy=0.9971

(e)

(f)

Accuracy=0.975

Accuracy=0.9964

(g)

(h)

Figure 17.
17. 1DCNN
1DCNNconfusion
confusionmatrix
matrixon
oneach
eachsignal:
signal:
(e) P5;
(f) M5;
(g)
Figure
(a)(a)
P9;P9;
(b)(b)
P8;P8;
(c) (c)
P7;P7;
(d) (d)
P6; P6;
(e) P5;
(f) M5;
(g) M4;
M4;
and
(h)
M3.
and (h) M3.

Figure 17a
exceedingly
small
number
of
Figure
17a shows
shows that
that the
the1DCNN
1DCNNmodel
modelonly
onlyhas
hasanan
exceedingly
small
number
identification
errors
in the
faultfault
category
of spring
break,break,
whichwhich
has a recall
of rate
99.5%,
of
identification
errors
in the
category
of spring
has a rate
recall
of
and theand
identification
accuracy
of other
faults
is 100%.
In addition,
the test
accu99.5%,
the identification
accuracy
oftypes
other of
types
of faults
is 100%.
In addition,
the
test
racy of the
on allon
samples
is as high
99.93%.
The 1DCNN
model model
trainedtrained
in this
accuracy
ofmodel
the model
all samples
is as as
high
as 99.93%.
The 1DCNN
paper
strong
ability and
robustness
and hasand
constituted
a good demonin
this has
paper
has generalization
strong generalization
ability
and robustness
has constituted
a good
stration of the application
of deep
in theinfault
diagnosis
of the
hydemonstration
of the application
of learning
deep learning
the fault
diagnosis
of adjustment
the adjustment
draulic servomotor.
hydraulic
servomotor.
In addition, comparing Figure 17a–h, it can be found that 1DCNN performs best on
the overall
overall test accuracy reaches 99.93% except for the distinct types
P8, P7, and P5, and the
of misjudgment, which is the same as the
the performance
performance of
of the
the model
model on
on P9.
P9. At the same
time, it also shows that P9, P8, P7, and P5 pressure signals contain more information than
P6, M5, M4, and M3, which can represent the state change of the adjustment hydraulic
servomotor. This conclusion coincides with the above results of “mutual information feature selection preferentially selects P9, P8 and P7 signals”, and the superiority of the several pressure sensors added in this paper in obtaining adjustment hydraulic servomotor

Machines 2024, 12, 368

19 of 21

time, it also shows that P9, P8, P7, and P5 pressure signals contain more information than
P6, M5, M4, and M3, which can represent the state change of the adjustment hydraulic
servomotor. This conclusion coincides with the above results of “mutual information
feature selection preferentially selects P9, P8 and P7 signals”, and the superiority of the
several pressure sensors added in this paper in obtaining adjustment hydraulic servomotor
status information is demonstrated.
6. Conclusions and Future Prospects
In this paper, an anomaly detection model based on GA-SVDD-neg was proposed
to detect the known and unknown faults of the equipment, aiming at the problems of
the difficult and limited maintenance efficiency of the adjustment hydraulic servomotor.
The superiority of the algorithm compared with other anomaly detection algorithms was
verified by experiments. At the same time, a fault diagnosis model based on 1DCNN was
designed to classify and diagnose known faults. The experimental results show that the
model has high precision and a strong generalization performance. The specific conclusions
are as follows:
(1)

(2)

(3)

In this paper, time and frequency domain feature extraction and multi-feature fusion
technology were used to achieve a comprehensive characterization of the state information of the adjustment hydraulic servomotor. Moreover, the effectiveness of MI in
the feature selection field of the adjustment hydraulic servomotor and its applicability
with the GA-SVDD-neg algorithm were verified by the comparative study of multiple
dimensionality reduction methods.
Through comparative study with GA-SVDD and PSO-SVDD algorithms, the superiority of the GA-SVDD-neg algorithm proposed in this paper was verified in the field of
the abnormal detection of adjustment hydraulic servomotors.
The 1DCNN was successfully applied to the fault diagnosis of an adjustment hydraulic
servomotor, achieving satisfactory results.

The method proposed in this paper can be further explored as an intelligent fault
diagnosis method for other types of hydraulic servomotors. The shortcomings of this study
and future exploration work are as follows:
(1)

(2)

Considering the complexity of manual feature extraction for the anomaly detection of
hydraulic servomotors using MI-GA-SVDD-neg, automatic feature extraction using
deep learning, such as a convolutional autoencoder, will be investigated in the future.
In this paper, 1DCNN and other convolutional neural network algorithms were
not comparatively studied when the fault diagnosis of a hydraulic servomotor was
performed, and the application of a lightweight convolutional neural network based
on an attention mechanism in the field of the fault diagnosis of a hydraulic servomotor
will be studied in the future.

Author Contributions: Conceptualization, X.Y.; methodology, X.Y.; software, X.Y. and Y.Z.; validation,
E.T. and S.C.; formal analysis, A.J.; resources, W.J.; data curation, X.Y. and E.T.; writing—original draft
preparation, X.Y.; writing—review and editing, W.J.; visualization, Y.Z.; supervision, W.J.; project
administration, W.J. All authors have read and agreed to the published version of the manuscript.
Funding: This research was supported by the National Natural Science Foundation of China (Grant
No. 52275067) and the Province Natural Science Foundation of Hebei, China (Grant No. E2023203030).
Informed Consent Statement: Informed consent was obtained from all subjects involved in the study.
Data Availability Statement: The data presented in this study are available on request from the
corresponding author due to privacy.
Conflicts of Interest: The authors declare no conflicts of interest.

Machines 2024, 12, 368

20 of 21

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

Yang, X. Research on State Monitoring and Fault Prediction and Diagnosis System of Adjustment Hydraulic Servomotor Based
on 1D-CNN and SVDD. Master’s Thesis, Yanshan University, Qinhuangdao, China, 2021.
Yu, D.; Xiang, Q.-H.; Sui, Y.-F. Online Detection of Valve Stem Sticking Faults in Turbine Regulation System. Chin. J. Electr. Eng.
2001, 21, 59–62. [CrossRef]
Li, W.; Yang, K.; Yu, D. Research on Networked Fault Diagnosis System for Turbine Regulation System. Master’s Thesis, North
China Electric Power University, Beijing, China, 2000.
Wang, X.; Li, X.; Li, F. Analysis on Oscillation in Electro-Hydraulic Regulating System of Steam Turbine and Fault Diagnosis
Based on PSOBP. Expert Syst. Appl. 2010, 37, 3887–3892. [CrossRef]
Xu, P. Model-Based Fault Diagnosis Research on Turbine Regulation System. Master’s Thesis, Harbin Institute of Technology,
Harbin, China, 2011.
Zhang, Z. Development of Turbine Oil Supply Control System and Hydraulic Servomotor Fault Diagnosis. Master’s Thesis,
Dalian University of Technology, Dalian, China, 2019.
Gawde, S.; Patil, S.; Kumar, S.; Kamat, P.; Kotecha, K.; Abraham, A. Multi-Fault Diagnosis of Industrial Rotating Machines Using
Data-Driven Approach: A Review of Two Decades of Research. Eng. Appl. Artif. Intell. 2023, 123, 106139. [CrossRef]
Vrignat, P.; Kratz, F.; Avila, M. Sustainable Manufacturing, Maintenance Policies, Prognostics and Health Management: A
Literature Review. Reliab. Eng. Syst. Saf. 2022, 218, 108140. [CrossRef]
Orošnjak, M.; Brkljač, N.; Šević, D.; Čavić, M.; Oros, D.; Penčić, M. From Predictive to Energy-Based Maintenance Paradigm:
Achieving Cleaner Production through Functional-Productiveness. J. Clean. Prod. 2023, 408, 137177. [CrossRef]
He, X.; Dong, H.; Yang, W.; Li, W. Multi-Source Information Fusion Technology and Its Application in Smart Distribution Power
System. Sustainability 2023, 15, 6170. [CrossRef]
Shanshan, Z. Multi-Source Information Fusion Technology and Its Engineering Application. Res. Health Sci. 2020, 4, p408.
[CrossRef]
Cai, J.; Luo, J.; Wang, S.; Yang, S. Feature Selection in Machine Learning: A New Perspective. Neurocomputing 2018, 300, 70–79.
[CrossRef]
Ma, J.; Wang, Y.; Niu, X.; Jiang, S.; Liu, Z. A Comparative Study of Mutual Information-Based Input Variable Selection Strategies
for the Displacement Prediction of Seepage-Driven Landslides Using Optimized Support Vector Regression. Stoch. Environ. Res.
Risk Assess. 2022, 36, 3109–3129. [CrossRef]
Song, X.; Zhang, Y.; Gong, D.; Sun, X. Feature Selection Using Bare-Bones Particle Swarm Optimization with Mutual Information.
Pattern Recognit. 2021, 112, 107804. [CrossRef]
Lei, X.; Xia, Y.; Wang, A.; Jian, X.; Zhong, H.; Sun, L. Mutual Information Based Anomaly Detection of Monitoring Data with
Attention Mechanism and Residual Learning. Mech. Syst. Signal Process. 2023, 182, 109607. [CrossRef]
Jiang, Q.; Yan, X. Plant-Wide Process Monitoring Based on Mutual Information–Multiblock Principal Component Analysis. ISA
Trans. 2014, 53, 1516–1527. [CrossRef] [PubMed]
Pan, H.; Xu, H.; Zheng, J.; Tong, J.; Cheng, J. Twin Robust Matrix Machine for Intelligent Fault Identification of Outlier Samples in
Roller Bearing. Knowl. Based Syst. 2022, 252, 109391. [CrossRef]
Pan, H.; Sheng, L.; Xu, H.; Tong, J.; Zheng, J.; Liu, Q. Pinball Transfer Support Matrix Machine for Roller Bearing Fault Diagnosis
under Limited Annotation Data. Appl. Soft Comput. 2022, 125, 109209. [CrossRef]
Moya, M.M.; Koch, M.W.; Hostetler, L.D. One-Class Classifier Networks for Target Recognition Applications. NASA Sti/Recon
Tech. Rep. N 1993, 93, 24043.
Bishop, C.M. Novelty Detection and Neural Network Validation. In Proceedings of the ICANN ′ 93; Gielen, S., Kappen, B., Eds.;
Springer: London, UK, 1993; pp. 789–794.
Cabral, G.G.; Oliveira, A.L.I. One-Class Classification Based on Searching for the Problem Features Limits. Expert Syst. Appl. 2014,
41, 7182–7199. [CrossRef]
Yu, W.; Zhao, C.; Huang, B. MoniNet With Concurrent Analytics of Temporal and Spatial Information for Fault Detection in
Industrial Processes. IEEE Trans. Cybern. 2022, 52, 8340–8351. [CrossRef]
Tax, D.M.; Duin, R.P. Support Vector Domain Description. Pattern Recognit. Lett. 1999, 20, 1191–1199. [CrossRef]
Zou, Y.; Wu, H.; Guo, X.; Peng, L.; Ding, Y.; Tang, J.; Guo, F. MK-FSVM-SVDD: A Multiple Kernel-Based Fuzzy SVM Model for
Predicting DNA-Binding Proteins via Support Vector Data Description. Curr. Bioinf. 2021, 16, 274–283. [CrossRef]
Huang, C.; Min, G.; Wu, Y.; Ying, Y.; Pei, K.; Xiang, Z. Time Series Anomaly Detection for Trustworthy Services in Cloud
Computing Systems. IEEE Trans. Big Data 2022, 8, 60–72. [CrossRef]
He, Z.; Zeng, Y.; Shao, H.; Hu, H.; Xu, X. Novel Motor Fault Detection Scheme Based on One-Class Tensor Hyperdisk. Knowl.
Based Syst. 2023, 262, 110259. [CrossRef]
Xu, E.; Li, Y.; Peng, L.; Yang, M.; Liu, Y. An Unknown Fault Identification Method Based on PSO-SVDD in the IoT Environment.
Alex. Eng. J. 2021, 60, 4047–4056. [CrossRef]
Navarro-Acosta, J.A.; García-Calvillo, I.D.; Reséndiz-Flores, E.O. Fault Detection Based on Squirrel Search Algorithm and Support
Vector Data Description for Industrial Processes. Soft Comput. 2022, 26, 13639–13650. [CrossRef]
Tax, D.M.; Duin, R.P. Support Vector Data Description. Mach. Learn. 2004, 54, 45–66. [CrossRef]

Machines 2024, 12, 368

30.
31.
32.
33.
34.
35.

21 of 21

Ni, P.; Miao, C.; Tang, H.; Jiang, M.; Wu, W. Small Foreign Object Debris Detection for Millimeter-Wave Radar Based on Power
Spectrum Features. Sensors 2020, 20, 2316. [CrossRef] [PubMed]
Qinghai, B. Analysis of Particle Swarm Optimization Algorithm. Stud. Comp. Intell. 2010, 3, 180. [CrossRef]
Jiang, W.L.; Zhao, Y.H.; Zang, Y.; Qi, Z.Q.; Zhang, S.Q. Feature Extraction and Diagnosis of Periodic Transient Impact Faults
Based on a Fast Average Kurtogram–GhostNet Method. Processes 2024, 12, 287. [CrossRef]
Krizhevsky, A.; Sutskever, I.; Hinton, G.E. ImageNet Classification with Deep Convolutional Neural Networks. Commun. ACM
2017, 60, 84–90. [CrossRef]
Guo, S.; Yang, T.; Gao, W.; Zhang, C. A Novel Fault Diagnosis Method for Rotating Machinery Based on a Convolutional Neural
Network. Sensors 2018, 18, 1429. [CrossRef] [PubMed]
Wang, L.-H.; Zhao, X.-P.; Wu, J.-X.; Xie, Y.-Y.; Zhang, Y.-H. Motor Fault Diagnosis Based on Short-Time Fourier Transform and
Convolutional Neural Network. Chin. J. Mech. Eng. 2017, 30, 1357–1368. [CrossRef]

Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.

