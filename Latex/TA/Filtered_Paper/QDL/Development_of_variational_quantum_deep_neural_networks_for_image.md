Neurocomputing 501 (2022) 566–582

Contents lists available at ScienceDirect

Neurocomputing
journal homepage: www.elsevier.com/locate/neucom

Development of variational quantum deep neural networks for image
recognition
Yunqian Wang, Yufeng Wang, Chao Chen, Runcai Jiang, Wei Huang ⇑
School of Mathematics and Computer Sciences, Nanchang University, Nanchang 330031, China

a r t i c l e

i n f o

Article history:
Received 25 June 2021
Revised 8 December 2021
Accepted 6 June 2022
Available online 13 June 2022
Communicated by Zidong Wang
Keywords:
Quantum computation
Variational quantum algorithms
Parametrized quantum circuit
Quantum deep neural network
Quantum machine learning

a b s t r a c t
Parametrized quantum circuits are widely used for supervised learning tasks such as image classification
in the noisy intermediate scale quantum era. However, normally, it can only handle low-dimensional
data. This study presented a variational quantum deep neural network (VQDNN) model for various scale
image recognition tasks. Three classifiers were designed to verify the classification performance of the
proposed VQDNN model. In the first classifier, to accommodate the limitations of qubits in both simulation hardware and real quantum hardware – we adopted hybrid principal component analysis – VQDNN
architecture. Moreover, the amplitude encoding scheme and the rotation angle coding scheme were
employed in the subsequent two classifiers to handle large-size images. Finally, we used the classical
neural network and VQDNN model to conduct a comparative experiment of the ten-label classification
learning task on the same dataset. The quantum numerical experiment was implemented on two benchmark datasets: the MNIST and UCI databases of handwritten digits. The simulation results showed that
the proposed VQDNN classified the two datasets with an accuracy of 100% for the two-class classification
task, while the UCI dataset has an accuracy of 90.87% for the ten-label classification task. The proposed
VQDNN achieved better classification accuracy than the original classical neural network even under a
limited number of qubits available in current hardware, indicating the promising application potential
of VQDNN in image recognition.
Ó 2022 Elsevier B.V. All rights reserved.

1. Introduction
The field of quantum computing originated from the recognition that classical simulation of the quantum system is a challenging task [14]. Studying an alternative to the classical algorithm
based on the concept of quantum superposition and entanglement
has greatly. Additionally, the novel devices, called Noisy
Intermediate-Scale Quantum (NISQ) computers, have increasingly
attracted much attention [37]. It was shown that the state-ofthe-art NISQ outperforms the classical supercomputers in contrived mathematical tasks [1,48].
Variational quantum algorithms (VQAs) have emerged as a
promising approach to obtain a quantum advantage on NISQ
[10]. As a natural quantum analog of neural networks, VQAs adopt
an optimization-based method. The classical optimization toolbox

⇑ Corresponding author at: Department of Compute Science, Nanchang University, Nanchang 330031, China.
E-mail address: n060101@e.ntu.edu.sg (W. Huang).
https://doi.org/10.1016/j.neucom.2022.06.010
0925-2312/Ó 2022 Elsevier B.V. All rights reserved.

is used to run the parameterized quantum circuits on the quantum
computer, and then a classical optimizer is used to optimize the
parameters. In such a way, the quantum circuit depth can remain
shallow, mitigating noise, unlike quantum algorithms developed
for the fault-tolerant era. Due to this advantage, VQAs have been
used for various quantum computer applications, especially universal quantum computing [8], dynamical quantum simulation
[13,33,3], optimization [38,30,34], mathematical applications
[44,29,19], and quantum machine learning.
Quantum machine learning aims to learn patterns for predicting
unseen data accurately. An excellent review on variational or parametrized circuits in quantum machine learning can be found in Ref.
[6].
Expressiveness is the central topic of classical machine learning,
and it has aroused great interest in quantum machine learning.
Although parametrized quantum circuits (PQC) provides strong
evidence of quantum advantage, there are still two important
questions that have not been explored: (1) How can a high expressive PQC be designed? (2) Does PQC have any quantum advantages

Neurocomputing 501 (2022) 566–582

Y. Wang, Y. Wang, C. Chen et al.

VQDNN model, three VQDNN based classifiers used in different
variations for the experiments, and the comparative experiment
between VQDNN and the classical neural network. Section 4
describes the experimental setup and discusses the results. Final
conclusions and future works is recommended in Section 5.

that can be used to solve practical problems? The comparison of
expressive power between PQC and classical neural networks is
desirable and may be beneficial to the fields of physics and
machine learning. There have been some publications on this
aspect of research, such as the structure of variational quantum
neural networks[5,11,35], and quantum neural networks as classifiers [26,45].
A proof-of-principle experiment has proved that PQCs with a
simple structure already outperform any classical neural network
for learning tasks in Ref. [12]. However, the research mainly
focuses on generative learning tasks. Schuld et al. [42] investigated
how the strategy with which data are encoded into the model
influences the expressive power of parametrized quantum circuits
as function approximators. The results show that by repeating simple data-encoding gates multiple times, quantum models can
access increasingly rich frequency spectra. In Ref. [16], a parameterized tree-like quantum classifier was proposed. The classifier
can achieve decent performance for the Iris dataset and MNIST
with proper strategies. However, the research used dimension
reduction methods such as principal component analysis (PCA) to
reduce 784 dimensional data to an eight-dimensional vector,
which will inevitably cause some information loss. Schuld et al.
[39] proposed a parameterized circuit model with a circuit composed of variational single-qubit gates and two-qubit controlled
gates. This work provides several fresh angles to examine variational quantum classifiers. In addition to the above structures
and protocols of variational quantum classifiers, there are many
other works from different perspectives [9,25,47,22].
After careful analysis, it was determined that the previous
research still needs more in-depth evaluation in at least the following four aspects:

2. Preliminaries
2.1. Basic concepts
2.1.1. Quantum bit (Qubit)
The operational architecture of quantum computers is fundamentally different from that of classical computers. The quantum
computers adopt quantum bits (qubits) as an operating unit, unlike
classical computers adopting binary digits (bits: 0 or 1). Qubits can
be 1, 0, and a probabilistic mixture of 1 and 0, called superposition
[32]. Thanks to such a key principle, superposition, a quantum
computer can conduct specific tasks much faster than classical
computers. Generally, discussing a quantum framework via BraKet notation is trivial, where jwi and hwj represent vertical and horizontal quantum state vectors, respectively. A qubit is defined as a
linear combination of j0i and j1i which is defined as Eq. (1).

jwi ¼ aj0i þ bj1i ¼

 

a
b

; j0i ¼

 
 
1
0
; j1i ¼
0
1

ð1Þ

where a and b are the probability coefficients encoding qubit state
information, defined as the square root of the probability to be measured as j0i or j1i. Even though qubits can be in both j0i and j1i
simultaneously, they are determined as one of j0i or j1i when measured for a definite output.
The unit Bloch Sphere is used to represent a qubit. In the case of
j0i and j1i , the values are measured across the Z basis. Rotations
over the Bloch sphere surface are used to encode and manipulate
the data in a pure quantum state. In Eq. (1), the a and b can be considered as the states distances to the state vectors j0i and j1i,
where a high a indicates being relatively close to j0i. Quantum
computing can sample the output repeatedly to provide multiple
answers for one question.

 To process real datasets, most of the literature uses principal
component analysis (PCA) to preprocess the images and project
real data to low dimensions, which reduces the accuracy of the
algorithm.
 Most documents only use one coding method and do not compare the impact of different coding techniques on the accuracy
of the classification model.
 Most of the literature only performs a kind of binary classification, and there is no systematic comparison of model classification effects under different learning tasks.
 The implementation of some classifiers requires the help of
other quantum devices and does not support end-to-end learning from classical data to category labels.

2.1.2. Quantum data manipulation
To accomplish data transformation and data encoding, a qubit
and its quantum state must be manipulated to encapsulate information onto it. Qubits are manipulated through quantum gates,
which in turn manipulates the overall quantum state. These gates
can allow for complete manipulation over the Bloch sphere, and
more specifically complete manipulation of the quantum state vector, which can describe the state of a mixture of more than 1 qubit.
The few gates used in this paper are introduced in Eqs. (2)–(5).

Compared with the related works, the main contributions of
this study are summarized as follows:
 The quantum neural network (QNN) model was extended to the
facile and scalable variational quantum deep neural network
(VQDNN) model that allows an end-to-end training via data
preprocessing and a hybrid paradigm of a parametrized quantum circuit.
 Three quantum classifiers were designed based on the proposed
VQDNN model for various scales image recognition tasks.
 The angle encoding and amplitude encoding was trained and
evaluated, and then were combined in the proposed VQDNN
classifiers.
 A series of comparative binary and ten-label classification
experiments were conducted using full-size image samples
from the MNIST dataset[20] and UCI dataset[2] to demonstrate
quantum supremacy.

2

1 0 0
60 1 0
6
CNOT ¼ 6
40 0 0
0
"
RY ð h Þ ¼
"
RZ ð h Þ ¼
"
RX ð h Þ ¼

This paper is structured as follows: In Section 2 the preliminaries of the work are introduced. Section 3 describes the proposed
567

0

3
0


07
1 1 1
7
7; H ¼ pﬃﬃﬃ
15
2 1 1

1 0


 #
cos 2h  sin 2h
h
h
sin 2
cos 2
ih

ð2Þ

ð3Þ

#

e 2

0

0

e 2

ih


 #
cos 2h
i sin 2h


i sin 2h cos 2h

ð4Þ

ð5Þ

Y. Wang, Y. Wang, C. Chen et al.

Neurocomputing 501 (2022) 566–582

The accomplished task in Eq. (2) is to entangle two qubits. In
Eqs. (3)–(5) a single qubit is allowed to be placed to any position
on a Bloch sphere’s surface. These gates allow manipulating quantum states.

a log2 N qubits system with amplitude encoding. In this work, we
consider the input vector with dimension N ¼ 32  32 ¼

2.2. Classical data embedding

2.3. Parameterized quantum circuit

In the classification circuits, the data samples were first translated from the subject data domain D into the Hilbert space H
through a feature map f : D ! H . Various preprocessing methods
[41,40,27,15,42]can be integrated into f. In this study, two data
encoding patterns were presented, angle encoding and amplitude
encoding, adopted in the following parts, which are qubitefficient or amplitude-efficient for different data dimensions,
respectively.

Lewenstein first proposed the concept of quantum perception
to apply quantum computers to compute the neural network-like
structure [21]. PQC [6] is conceptually similar to a traditional neural network, having trainable parameters in circuits. Like having
many layers in a traditional neural network, there are many layers
realized by placing the unit layer multiple times in PQC. L times
repeated unit layer gives more flexibility to the circuit. Such a deep
neural network with multiple layers was proven to obtain outperforming results in many applications.
Let a PQC be denoted as a trainable unitary operation on the nqubit state, U h , applied to a reference state j/i, which generally
equals to j0in . The trained variable j/h i ¼ U h j/i, Where h is a vector of a polynomial number of circuit parameters. This circuit layout assumes a unit layer containing single-qubit operations
followed by entangling two-qubit operations.
Since an n-qubit quantum neural network encodes a 2n  2n
unitary mapping, the number of input qubits is the same as the
output qubits. Additionally, small and efficient local gates, such
as CNOT, CZ, and rotation gates, were utilized as a building block
of the overall unitary. The circuit parameters determined the
phases of the rotation gates.
This unit layer of the gate sequence was adopted as a circuit
template in this study, as shown in Fig. 2.

1024 ¼ 210 (for MNIST Dataset) or N ¼ 8  8 ¼ 64 ¼ 26 (for UCI
Digits Dataset) and n-qubit system with or respectively.

2.2.1. Angle encoding
Angle encoding, sometimes is called qubit encoding or tensor
product encoding. Such an employed encoding allows an efficient
operation since a constant number of operations in parallel processing is required regardless of the amount of data. However,
the number of qubits required depends on the amount of data:
one qubit per one component of the input vector. The state preparation scheme requires only a single-qubit to be rotated and thus
highly efficient. In contrast, the number of qubits for this encoding
is nonoptimal.
All data was normalized into the range ½0; 2p . Each values xi
was then represented by a single qubit as follows: The rotation
operator gates RX ðhÞ , RY ðhÞ and RZ ðhÞ were conducted. As a result,
the rotation angle was determined by the data value.
The most commonly used method in some literature is applying
 
 
the feature map xi ! cos x2i j0i þ sin x2i j1i using the RY ðhÞ rotation
operator as shown as Eq. (6),

RY ðxi Þj0i ¼ eðiYxi =2Þ j0i
"
 
  # 
1
cos x2i  sin x2i
xi 
xi 
¼
0
sin 2
cos 2
 
 
¼ cos x2i j0i þ sin x2i j1i

3. The proposed VQDNN model and VQDNN classifiers
An end-to-end variational quantum deep neural networks
model and the corresponding training algorithm are presented first
in this section. Then, three classifiers based on the proposed
VQDNN model were designed to perform binary classification
tasks. Finally, the classical neural network and VQDNN model
was used to perform a comparative experiment of the ten-label
classification learning task on the same dataset.

ð6Þ

To map the quantum states encoded from the data points to Hilbert space more dispersed, a slightly more complicated feature
map was used as shown in Eq. (7).


 
xi ! RZ arctan x2i RY ðarctan xi ÞHj0i

3.1. The end-to-end VQDNN model

ð7Þ

Here, PQC was applied as the core to develop a variational quantum model and to realize an end-to-end variational quantum deep

Given an n-dimensional vector x ¼ ðx0 ; x1 ;    ; xn1 Þ to be
encoded in an n qubit circuit, the encoding operation can be written as Eq. (8).


 
U ðxÞ ¼ RZ arctan x20 RY ðarctan x0 ÞH

 2 
RZ arctan x1 RY ðarctan x1 ÞH    

 
RZ arctan x2n RY ðarctan xn ÞH

ð8Þ

Fig. 1. Angle encoding circuit.

2.2.2. Amplitude encoding
Here, given a classical vector, x ¼ ðx0 ; x1 ;    ; x2n 1 Þ, the aim of
amplitude encoding was to encode the classical vector into an nqubit quantum state

jwi ¼ x0 j00    0i þ x1 j00    1i þ    þ x2n 1 j11    1i

ð9Þ

where the xi 2 R and the vector ðx0 ; x1 ;    ; x2n 1 Þ is a normalized
vector.
Amplitude encoding has the advantage that it only needs
n ¼ log ðN Þ qubit in encoding an input with N features, so the main
reason to choose this encoding scheme is to minimize the number
of qubits used, thereby reducing the number of circuit parameters.
For example, given a vector with size N, it can be represented with

Fig. 2. The unit layer of three qubits for VQDNN model.
568

Neurocomputing 501 (2022) 566–582

Y. Wang, Y. Wang, C. Chen et al.

 Compute @@hL using the hybrid quantum classical automatic dif-

neural network. The basic idea of VQDNN was to convert the performed learning task into a minimization problem over the param!
eters of a quantum circuit, h . The model had five major
components: data preparation, data encoding, unitary transformation, entangled state measurement, and classical postprocessing.
The first component describes the processing of input data to meet
the quantum requirements, using dimensionality reduction, padding, and data flattening methods. After this step, the classical data
can be encoded into a quantum state. The next component, data
encoding, delineates the skills needed to transform the classical
data point to a quantum state, using amplitude encoding or angle
encoding schemes. Unitary transformation, the third part of the
model, uses H gates, single-qubit rotation gates, and entanglement
gates to complete the transformation and entanglement of quantum states. After measuring the quantum state, the expected value
of some Hamiltonians is delivered into the postprocessing part. The
end-to-end VQDNN model is shown in Fig. 3.
The learning procedure of the VQDNN to solve real-world image
classification problems can be summarized as follows:

i

ferentiation framework [17,23]. Perform gradient descent:
hkþ1 ¼ hk  g @@hL

i

h¼hk

. This procedure was repeated until h con-

verges, and finally, the trained VQDNN can give the correct classification results.

3.2. Hybrid PCA-VQDNN classifier
In this section , a hybrid PCA-VQDNN classifier was designed
based on the above proposed VQDNN model. Principal component
analysis (PCA) was employed as the data preprocessing tool aimed
at to giving the VQDNN model the ability to tackle the common
image recognition tasks in high-dimensional space. The end-toend data flow diagram is shown in Fig. 4. As a baseline, the binary
classification tasks were first performed on the hybrid PCA-VQDNN
model using the MNIST dataset, where the PCA part serves as the
simple feature extractor and the PQC as the classifier.
The learning procedure of the hybrid PCA- VQDNN classifier
proceeded from reducing the dimension of the MNIST sample from
784 to 10 and encode it into a quantum state through the angle
encoding method, which is defined in Fig. 1. The core component
of the quantum classifier is shown in Fig. 2, which contains all
trainable parameters in the quantum circuit and can be stacked
in multiple layers. After the unitary evolution of PQC, mainly using
the Hadamard gate, single-qubit rotation gate (Ry and Rz ), and
entanglement gate (CNOT) to complete the transformation and
entanglement of quantum states, the output quantum state enters
the subsequent Pauli-Z measurement circuit. The classical postprocessing function, employing the cross-entropy loss function here in
this research, was applied to the measurement result to minimize
the loss function. The quantum circuit and the classical optimizer
work alternately until the optimal parameters were found.

 The input x of the data point ðx; yÞ was preprocessed and
encoded into the input state of the network either as
P
xi jii(amplitude encoding) or as j0i followed by a set of
jwi ¼
rotations n1
i¼0 Rðf ðxi ÞÞ (angle encoding), where f is a preprocessing function of x (arctan x in our research).
 The PQC, represented as U ðhÞ , was applied to the input quantum state of jwi to produce a new entangled state
jui ¼ U ðhÞjwi .
 The entangled state was observed using a measurement operator. The measurement expected value was used in the classical
computation part to produce the predicted label. Define a func!
!
tion, L h , such that the minimum value of the function, L h
 !
!
, or the circuit evaluated with the min, h ¼ argmin! L h
h
!
imized parameters, U h , corresponds to the solution to some
!
computational problem. The function F h can depend on the

3.3. Amplitude encoding based VQDNN classifier

parameterized circuit in a variety of ways, but the simplest
!
example is one might be where F h is the expected value of
!E
!E
D !
defined
some Hamiltonian, w h M w h , with w h

In the PCA-VQDNN classifier, to reduce the desired number of
qubits, classical principal component analysis was adopted to preprocess the data sample. However, here, how the proposed VQDNN
model performs on the original datasets was the objective. Fig. 5
shows that VQDNN uses the amplitude encoding method to encode
the MNIST or UCI handwritten digit sample to ten or 6-qubit quantum systems, respectively.
If the number of pixels in an original image was not exactly
equal to a n-th power of 2, the image can extend by padding the
input vector to reach 2n -dimensional.
For MNIST, the 784-dimensional input was padded into a 1024dimensional normalized vector x, which can be converted into an
amplitude-encoded 10-qubit state denoted by jui. The subsequent
classification circuit is shown in Fig. 5.

to be the state prepared by parameterized quantum circuit act!
ing on a fixed initial state. Then L h may be evaluated by
!E
and measuring M .
repeatedly preparing w h
 The predicted label b
y and the true label y were used to compute
a loss function via classical computation, e.g. the cross entropy
P
loss functionL ¼ N1 i  ½yi  log ðpi Þ þ ð1  yi Þ  log ð1  pi Þ,where
pi indicated the probability that the sample i is predicted to be
positive.

Fig. 3. The schematic diagram of end-to-end VQDNN model.
569

Y. Wang, Y. Wang, C. Chen et al.

Neurocomputing 501 (2022) 566–582

implemented using angle rotational encoding or amplitude encoding techniques, respectively. If the two architectures were mixed
together, is the proposed VQDNN model still effective? The first
part of the classifier uses amplitude encoding techniques to
achieve exponential coding supremacy, and the subsequent circuit

3.4. Hybrid encoding based VQDNN classifier
In the above two parts, classifiers were designed to explore the
performance of the proposed VQDNN model in low-dimensional
feature space and high-dimensional feature space, which were

Fig. 4. The diagram of the hybrid PCA-VQDNN classifier. The first part is data preprocessing. The middle part is the data encoding circuit. By going through one or more layers
of PQC, one measures all ten qubits, and ultimately takes the expected value for classic postprocessing.

Fig. 5. Diagram of the amplitude encoding-based VQDNN classifier. The first part is padding and flattening the input samples. U ðC Þ indicates amplitude encoding circuit.
Subsequently, N layers PQC is applied to the input state. At last measure all the ten qubits and take the expected value for classic post-processing.

Fig. 6. Diagram of the hybrid encoding-based VQDNN classifier. The first part is amplitude encoding. After passing through the first PQC and measuring, the expectations are
encoded into angles of qubits in the second PQC. The measurement results are used in classical postprocessing.
570

Neurocomputing 501 (2022) 566–582

Y. Wang, Y. Wang, C. Chen et al.

cessing. In the classical neural network, the simplest network
structure was used that contains just one hidden layer, as shown
in Fig. 8. In the comparative setting, we control the number of tunable parameters by adjusting the number of PQC layers and nodes
in the hidden layer in the classical network, and thus analyze the
relative performance of the VQDNN and classical neural network
on classification tasks.

uses angle encoding to span the data to the large Hilbert space.The
proposed VQDNN model’s performance in a sophisticated network
structure was the objective.
For large-size learning samples, amplitude encoding was used
to encode them. After passing through the first PQC and measuring,
the expectations were encoded into angles of qubits in the second
PQC. The measurement results were used in classical postprocessing. The whole process is shown in Fig. 6. Generally, the procedure
consists of the following six steps:

4. Numerical simulation & results discussion

 After padding and flattening the input samples, the classical
data can be encoded into a quantum state using the amplitude
encoding method.
 The input quantum state was transformed and entangled
through the first PQC, which can be stacked in multiple layers.
 All the qubits of the first PQC were measured in Pauli-Z before
passing the expected values into the second PQC using the angle
encoding method.
 Similar to the first PQC, the input quantum state was transformed and entangled in the second PQC, which can be stacked
in multiple layers.
 After measuring and passing the expected valuese, the loss
function can be calculated from the predicted value and the true
value.
 The tunable parameters in the two PQCs and the classical fully
connected layers were optimized using a classical optimizer.

In this section, four numerical simulation experiments are
implemented. The codes were written purely in Julia [7] and the
quantum circuit simulation was performed by the open-source
variational quantum circuit simulator VQC [24]. Adaptive moment
estimation (Adam) was used in the parameter updating.
4.1. VQDNN was effective in low feature spaces
VQDNN was first trained using hybrid PCA-VQDNN architecture
on the MNIST dataset. Each example of MNIST was described by
784 features, which required too many Qubits for some NISQ processors. Here, PCA was adopted to reduce the 784 features to 10
features. After the reduction, the 10 features were encoded into
the quantum states using rotational encoding and transformed
by shallow PQC. Finally, the measurement results were used to calculate the loss value and predict the class label.
In this numerical simulation, two binary datasets were
extracted including ‘0, 1’ and ‘3, 8’ samples only from the original

3.5. Benchmark design of VQDNN model
In the above four parts, an end-to-end VQDNN model was proposed and three classifiers were designed to explore the performance of VQDNN in low-dimensional feature space, highdimensional feature space and sophisticated network structure,
which were implemented using PCA, amplitude encoding and
hybrid encoding technology, respectively. All three classifiers performed well on the learning task. The next question naturally was
how the performance of the VQDNN model-based classifier compared with the classical original neural network. Under the limitation of the same number of trainable parameters in the classical
classifier, does the VQDNN classifier still have satisfactory classification performance?.
Here, a ten-label classification task benchmark was conducted
on the UCI digits dataset. In the quantum setting, shown in
Fig. 7, the UCI digits image was first flattened. After normalization,
the vector was encoded into a 6-qubit quantum state using the
amplitude encoding method. Then, a multilayer PQC was applied
to the input state. After measurement, the expected values were
injected into a 6  10 fully connected layers for classical postpro-

Fig. 8. Ten-label classification learning task of the classical neural network.

Fig. 7. Ten-label classification learning task of VQDNN.
571

Y. Wang, Y. Wang, C. Chen et al.

Neurocomputing 501 (2022) 566–582

fication learning task of number ‘0, 1’ and ‘3, 8’ on UCI handwritten
digits dataset and MNIST dataset, respectively.

data. For each class, 1000 samples were used as the training data
and 200 samples were set as to the test to verify the accuracy of
the algorithm. A stochastic gradient optimizer called adaptive
moment estimation (Adam) was used with a learning rate of
0.01. To reduce the randomness of the experiment, Each experiment was conducted 10 times, and the average of 10 times was
taken in each iteration as the accuracy value and loss value of this
iteration. The test accuracy and loss curves of single-layer PQC,
double-layer PQC and triple-layer PQC with 80, 110, and 140
parameters in the 0, 1 classification and 3, 8 classification are
shown in Fig. 9. It can be seen that the VQDNN model had achieved
better classification accuracy on the 0 and 1 binary classification
tasks than on the 3 and 8 binary classification tasks. Observing
the same classification task, as the number of PQC layers increases,
the classification performance of the VQDNN model was significantly improved. The test accuracies of single-layer PQC, doublelayer PQC, and three-layer PQC all reached 99% under the twoclass classification task of 0 and 1. However, it is worth noting that
as the number of PQC layers increased, the classifier required fewer
iterations to achieve 99% classification accuracy. Single-layer PQC
and double-layer PQC can achieve 99% classification accuracy after
60 iterations, which was significantly better than single-layer PQC
after 90 iterations.
To visualize the training performance, the training loss is shown
on the right side of Fig. 9. As the number of training iterations
increased, the losses of the three PQCs will gradually decrease
under the two classification tasks. However, after carefully checking the loss curve, it was found that the two-layer and three-layer
PQCs decreased significantly faster on the 0 and 1 classification
tasks, and finally reached approximately 0.01. In summary, it can
be seen that the hybrid PCA-VQDNN algorithm exhibits excellent
performance in the low-dimensional feature space with limited
quantum computing resources. By increasing the number of trainable parameters (increasing the number of PQC layers), the model
will converge faster, and the training loss can be reduced to a minimum faster.

4.2.1. UCI hand-written digit data
A: ‘0, 1’ vs. ‘3, 8’ classification.
First, we trained VQDNN on the UCI hand-written digit dataset.
Filtering out the digits ‘0, 1’ and ‘3, 8’ in the UCI handwritten digits
dataset, there were 765 training samples and 360 testing samples
left for ‘0, 1’. The numbers ‘3’ and ‘8’ were also screened out, and
769 training samples and 357 test samples were obtained. In this
experiment, we first flattened the 8  8 images to the 64  1 column vector. After normalization, the vector was encoded into a
6-qubit quantum state using the amplitude encoding method.
Then, a multilayer PQC is applied to the input state.
Depending on the number of layers included in the PQC, each
VQDNN contains a different number of trainable parameters. The
number of different parameters determines the learning performance of the quantum classifier. In this numerical simulation
experiment, we set the number of layer to 1–5 to explore the performance of the VQDNN under different circuit depths. Adam was
used as the optimizer with a learning rate of 0.01. To reduce the
randomness of the experiment, we repeated each quantum experiment 10 times, and took the average of 10 values as the value of
the current iteration. We trained each classifier in the 0, 1 and 3,
8 binary classification tasks 100 times, and the results are shown
in Fig. 10 and Fig. 11.
In Fig. 10, when the quantum classifier takes a single layer,
there were 48 trainable parameters in the quantum neural network (6  3 þ 6  3 þ 6  2). At the end of the training process,
the average test accuracy for 10 runs was approximately 0.9747.
This means that for 360 test samples, the quantum classifier made
9 errors. As the number of PQC layers increased to 5, the number of
trainable parameters reached 120. At the end of the training process, the average test accuracy of 10 runs is approximately
0.9989, and the quantum classifier can almost completely classify
correctly. It can also be seen from Fig. 10 that as the depth of the
quantum circuit increases, the classifier can achieve better classification accuracy, and it can also converge faster. However, from the
fact that the second half of the accuracy curves at depths 4 and 5
almost overlap, it can be seen that the classification accuracy and
convergence speed cannot be improved all the time. With the
increase in trainable parameters, the network has been saturated.

4.2. VQDNN was effective in high-dimensional spaces
To explore the classification performance of VQDNN in highdimensional feature spaces, here we implement the binary classi-

Fig. 9. Illustration of hybrid PCA-VQDNN architecture single-layer PQC, two-layer PQC and three-layer PQC on the 0, 1, and 3, 8 binary classification tasks test accuracy and
training loss curve with the number of iterations. As the number of training iterations increases, the accuracy of PQC with more layers is higher than that of single-layer PQC,
and the loss also drops faster.
572

Neurocomputing 501 (2022) 566–582

Y. Wang, Y. Wang, C. Chen et al.

Fig. 10. The test accuracy and training loss of the 1–5 layer PQC using the VQDNN architecture on the 0, 1 classification task vary with the number of iterations.

Fig. 11. The test accuracy and training loss of the 1–5 layer PQC using the VQDNN architecture on the 3 and 8 classification task vary with the number of iterations.

B: quantum vs. classical classification.
To compare with the classic neural network, we used a single
hidden layer classic fully connected neural network to perform
the same two-class learning task. The classic neural network uses
the same 64 pixel values as input, was set as a single hidden layer,
the output layer had 2 nodes, and the hyperparameter settings
were exactly the same as VQDNN. This classic benchmark was
designed to limit the number of parameters to make a fair comparison with the quantum model. The experimental results are shown
in Fig. 13 and Fig. 14. It can be seen from the two figures that the
classification performance of VQDNN was significantly better than
that of the classic neural network under the limitation of the number of similar parameters, regardless of whether it was a 0, 1 classification or a 3, 8 classification.

It can be seen from the loss curve on the right side of Fig. 10 that as
the depth of the quantum circuit increases, the training loss converges faster and faster.
Fig. 11 shows the test accuracy and training loss of PQC on 3 and
8 classification tasks as a function of the number of iterations. Similar to the 0, 1 classification task, in this experiment, as the depth of
the quantum circuit increases, the classifier can achieve better
classification accuracy and converge faster. This was consistent
with the performance on the 0, 1 classification task.
To compare the performance difference of the VQDNN model on
different classification tasks, we took the change curves of the PQC
with depths 1, 3, and 5 on the two classification tasks of ‘0, 1’ and
‘3, 8’ to draw Fig. 12. It can be seen from the figure that the PQC of
the same depth can achieve better accuracy on 0 and 1 classification tasks and converge faster. This was because 3 and 8 classification tasks were more complicated than 0 and 1, and achieving
similar classification accuracy requires more trainable parameters
and more iterations.

4.2.2. MNIST
To fully explore the classification performance of VQDNN in
high-dimensional spaces, we trained VQDNN on the MNIST dataset
573

Y. Wang, Y. Wang, C. Chen et al.

Neurocomputing 501 (2022) 566–582

Fig. 12. Comparison of the test accuracy and training loss with the number of iterations on the 0, 1 and 3, 8 classification tasks of the 1–5 layer PQC using the VQDNN
architecture.

Fig. 13. The test accuracy and training loss of the quantum classifier and the single hidden layer classical neural network classifier on the 0, 1 classification task are compared
with the change curve of the number of iterations.

mizer with a learning rate of 0.05. It can also be seen from
Fig. 15 that in the two classification tasks, as the depth of the quantum circuit increased, the classifier can achieve better classification
accuracy and converge faster. It can also be observed that the PQC
of the same depth can achieve better accuracy on 0 and 1 classification tasks and converge faster. This was because 3 and 8 classification tasks were more complicated than 0 and 1, and
achieving similar classification accuracy requires more trainable
parameters and more iterations.
According to the results of two numerical simulation experiments, it can be concluded that the proposed VQDNN could also
complete the two-class learning task well in the highdimensional feature spaces.

which was more difficult for the currently available quantum computing resources. Because the 784-dimensional MNIST sample was
still too large for the current quantum processor, the previous
research literature mostly downsampled the 28  28 digital image
to 8  8 or 4  4 . However here, we padded the 28  28 images to
32  32 , taking zero for the outermost pixels of the image and
adopt amplitude encoding method. Therefore, the 1024dimensional pixel value was encoded into a 10-qubits quantum
system. We extracted two binary datasets including ‘0, 1’ and ‘3,
8’ samples only from the original dataset. For each class, we used
1000 samples as the training data and 200 samples as the test
set to verify the accuracy of the classifier. We trained each classifier
in the 0, 1 and 3, 8 binary classification tasks 10 times to take the
average. The result is shown in Fig. 15.
For a one-layer quantum classifier, there were 80 trainable
parameters in the VQDNN (10  3  1 þ 10  3 þ 10  2). As the
PQC depth increases to 2, 3, and 5 layers, the trainable parameters
were 110, 140, and 200 respectively. Adam was used as the opti-

4.3. VQDNN was effective in sophisticated network structure
According to the two research results above, we know that
VQDNN can complete the two-class learning task well in both
574

Neurocomputing 501 (2022) 566–582

Y. Wang, Y. Wang, C. Chen et al.

Fig. 14. The test accuracy and training loss of the quantum classifier and the single hidden layer classical neural network classifier on the 3, 8 classification task are compared
with the change curve of the number of iterations.

Fig. 15. The binary classification accuracy and loss curve of the multilayer PQC using the VQDNN architecture varies with the number of iterations.

the optimizer with a learning rate of 0.05. At the end of 100 training epochs, the test accuracy was approximately 0.9975. This
means for 360 testing samples, the quantum classifier made one
mistake. As increase the quantum classifier depth to 2, the trainable parameters reached 120. As shown in Fig. 16, almost from
the 30th epoch, the test accuracy had been stable at 1.00. It can
also be seen that as the depth of the quantum circuit increased,
the training loss converged quickly.
Model performances of test accuracy (left) and training loss
(right) modified VQDNN depth. In both figures, the curve depth
takes 2 and parameters takes 120 is the better one.
B: Amplitude encoding versus Hybrid encoding
To analyze the classification performance of the VQDNN model
under amplitude encoding and hybrid encoding, we conducted
benchmark experiments, and the results are shown in Fig. 17 and
Fig. 18.
It can be seen in Fig. 17 that the classification performance of
the VQDNN model in the case of amplitude encoding and hybrid
encoding in the 0, 1 classification task is significantly better than
the classical neural network. Comparing Amplitude coding (Ex2)

low-dimensional feature spaces and high-dimensional feature
spaces. If we mixed the two architectures above together, does
the proposed VQDNN model still be effective? Below, we will verify
the binary classification performance of the model on the two
datasets.
4.3.1. UCI hand-written digit data
We first encoded the 64-feature digit image into a 6 qubits
quantum system using the amplitude encoding method. After the
unitary transformation of the first PQC, we measured all 6 qubits.
Passed the measured expected values into the second PQC, using
the rotational encoding method. After unitary transformation, 6
qubits were measured to obtain 6 expected values, followed by a
6  2 fully connected neural network, and finally the classification
value is given.
A: 0, 1 binary classification task
For the depth = 1 quantum classifier, where the first PQC and
the second PQC all take one-layer circuit, there are 84 trainable
parameters
in
the
quantum
neural
network
(6  3  1 þ 6  3 þ 6  3  1 þ 6  3 þ 6  2). Adam was used as
575

Y. Wang, Y. Wang, C. Chen et al.

Neurocomputing 501 (2022) 566–582

Fig. 16. Model performances of test accuracy (left) and training loss (right) modified VQDNN depth. In both figures, the curve depth is 2 and parameters takes 120 is the
better one.

Fig. 17. The accuracy and loss of the VQDNN model based on amplitude encoding and hybrid encoding and the classical neural network on the 0, 1 binary classification
learning tasks vary with the number of iterations.

For each class, we took 1000 samples as the training data and
200 samples as the testing data to train the quantum classifier.
For the depth = 1 quantum classifier, where the first PQC and the
second PQC all take a one-layer circuit, there were 140 trainable
parameters
in
the
quantum
neural
network
(10  3  1 þ 10  3 þ 10  3  1 þ 10  3 þ 10  2). Adam was
used as the optimizer with a learning rate of 0.05. At the end of
100 training epochs, the test accuracy was approximately 0.9975.
This means that for 400 testing samples, the quantum classifier
made one mistake. by increasing the quantum classifier depth to
2, the trainable parameters reached 200. A seen from Fig. 19,
almost from the 48th epoch, the test accuracy was stable at 1.00.
It can also be seen that as the depth of the quantum circuit
increases, the training loss converged quickly.
Model performances of test accuracy (left) and training loss
(right) modified VQDNN depth. In both figures, the curve depth
takes 2 and parameters takes 120 is the better one.
B: quantum vs. classical classification

and hybrid coding (Ex3), it can be seen that under the same number of trainable parameters, the classification performance of
VQDNN in complex networks was not worse than the simple network structure under Amplitude encoding in the previous section.
The VQDNN model in the 3 and 8 classification tasks in Fig. 18 also
had a similar performance. This shows that our proposed VQDNN
model was effective in complex network structures.
4.3.2. MNIST
A: 0, 1 binary classification task.
After padding the 28  28 MNIST images to 32  32 and encoding the 1024-dimensional pixel value into a 10-qubits quantum
system, we applied the unitary transformation formed by the first
PQC. After measuring and taking the expected value of 10 qubits,
we used the rotation encoding method to transport the expected
value to the second PQC. After unitary transformation, all qubits
were measured, and the expected value was used for binary
classification.
576

Neurocomputing 501 (2022) 566–582

Y. Wang, Y. Wang, C. Chen et al.

Fig. 18. The accuracy and loss of the VQDNN model based on amplitude encoding and hybrid encoding and the classical neural network on the 3, 8 binary classification
learning tasks vary with the number of iterations.

Fig. 19. Model performances of test accuracy (left) and training loss (right) modified VQDNN depth. In both figures, the curve depth takes 2 and parameters takes 200 is the
better one.

complex network was slightly better than that of the pure amplitude coding classifier, as shown in the blue and red curves. For 3
and 8 classification tasks, the classification performance of the
pure amplitude coding classifier was slightly better than the classification performance of the complex network. It can also be seen
that it was not possible to simply judge which of these two network structures was better or worse. In actual use, you should
make careful judgments for different learning tasks. However, it
can be seen in Fig. 21 that although the trainable parameters of
the two classifiers were an order of magnitude worse than the classic fully connected network, the performance was similar.

To explore the performance difference of VQDNN-based classifiers for classification tasks of different degrees of difficulty under
complex networks, we further extracted a binary classification
data set containing ‘3’ and ‘8’ samples from the original dataset.
Similarly, for each category, we used 1000 samples as the training
data and 200 samples as the test set to verify the performance of
the classifier. To more accurately reflect the performance of the
classifier, we iteratively trained each classifier in the 0, 1, 3, and
8 binary classification tasks, and ran it 10 times to average. The
results are the four curves identified by Ex3 in Fig. 4.20 Shown.
To compare the performance differences of the classifier based
on the VQDNN model in the case of amplitude coding and hybrid
coding, we also plotted the VQDNN classifier data based on the
amplitude coding in the previous section in Fig. 20, that is, the
three curves identified by Ex2.
Regardless of 0, 1 classification or 3, 8 classification, with the
increase of PQC depth, the classification performance was
improved. For the 0, 1 classification task, when the PQC contains
140 trainable parameters, the classification performance of the

4.4. Compared with the classical neural network, VQDNN has better
performance on ten-label classification tasks
4.4.1. quantum vs. classical classification task on UCI datasets
Here we conducted a ten-label classification learning task comparative benchmark experiment on the UCI digit dataset. The
577

Y. Wang, Y. Wang, C. Chen et al.

Neurocomputing 501 (2022) 566–582

Fig. 20. The accuracy and loss of the binary classification of multilayer PQC under the amplitude encoding and hybrid encoding of the VQDNN architecture vary with the
number of iterations.

Fig. 21. The binary classification accuracy and loss curve of the hybrid encoding classifier using the VQDNN architecture and the classical fully connected neural network vary
with the number of iterations.

only half (exactly 54.19%) of the number of parameters associated
with the analogous classical neural network (Fig. 8) were used for
the same classification task. However, the test accuracy that the
two models can achieve after 200 epochs of training was basically
the same. To be more precise, VQDNN had a slight advantage.
The same phenomenon can also be seen in the comparison
between the left and the middle of Fig. 22. In the left figure, when
the trainable parameter is approximately 90, the classification
accuracy of VQDNN far exceeds the classification accuracy of the
classic neural network. The middle figure shows the change in
accuracy when the trainable parameter is approximately 160. It
can also be seen from the figure that the classification accuracy
of the classic neural network was still quite large compared to
VQDNN.
It can be seen in Fig. 23 that whether it as classical or quantum,
as the depth (the number of hidden layer nodes) increased, the faster the loss decreased.

VQDNN classifier used amplitude encoding to compress the 64dimensional vectors into a 6-qubit quantum system.
The classical neural network used the same 64 pixels as an
input. The hidden layer has only one node and the output layer
had ten nodes. The design for this classical benchmark aims to
limit the number of parameters for a fair comparison to the quantum model.
The PQC had 6 qubits input, one layer of unitary transform, and
6 qubits output (Fig. 7). Each qubit had a tunable unitary transform
per layer, so there were 96 parameters (6  3  1 þ 6  3 þ 6  10)
in the circuit. Adam was used as the optimizer with a learning rate
of 0.05.
Fig. 22 shows the variation curve of test accuracy and training
loss with the number of iterations during the training process. Look
at the right of the figure first.
When the hidden layer has 4 nodes, the classical classifier had
310 parameters. The VQDNN classifier had 168 parameters when
the PQC had 5 layers of unitary transform. Importantly, roughly
578

Neurocomputing 501 (2022) 566–582

Y. Wang, Y. Wang, C. Chen et al.

Fig. 22. Model performances of test accuracy of VQDNN and Classical Neural Network modified the model depth. In the left figure, the layer depth is set to 1 and both the
number of parameters is about 90. VQDNN significantly excels classical networks. In the middle figure, VQDNN’s leading advantage can still be maintained as the depth
increases. In the right figure, VQDNN can achieve better classification accuracy using only 54.19% of the parameters in the classical network.

Fig. 23. Model performances of training loss of VQDNN (left) and classical neural networks(right) modified VQDNN depth. In both figures, with increasing depth, the loss
declines faster.

the classifier can achieve better classification accuracy, and it can
also converge faster. When the line depth was set to 10, the test
accuracy can reach approximately 0.8. For a classic fully connected
network with a single hidden layer, set the number of hidden layer
nodes to 1, 2, 3, and 5, and the number of corresponding parameters to 1045, 2080, 3115, and 5185. Observing the experimental
data, it can be seen that compared with the classical network with
four-digit parameter number, the quantum classifier based on
VQDNN still maintains significantly better classification performance under the number of trainable parameters that differ by
an order of magnitude.

4.4.2. quantum vs. classical classification task on MNIST datasets
Here we still padded the 28  28 images to 32  32, take zero
for the outermost pixels of the image and adopt the amplitude
encoding method. Therefore, the 1024-dimensional pixel value is
encoded into a 10 qubit quantum system. Considering that a tenqubit simulation system was time-consuming, for each category,
we used 200 samples as training data and 100 samples as a test
set to verify the performance of the classifier. We train each classifier iteratively 500 times. For the classic fully connected network,
because the number of nodes in the hidden layer was small, the
difference between each training of the classifier was large. To
make the results more representative, we took the average of ten
runs, as shown in Fig. 24.
For a single-layer quantum classifier, there were 160 trainable
parameters in the VQDNN. As the PQC line depth increased to 10
layers, the number of trainable parameters reached 430. Using
the Adam optimizer, the learning rate was set to 0.1. It can be seen
from the figure that as the depth of the quantum circuit increased,

4.5. Comparison of VQDNN with other quantum neural network
models
VQDNN experiments were conducted on the UCI and MNIST
datasets, using three different procedures, i.e., VQDNN in low feature spaces, VQDNN in high feature spaces, and VQDNN in a
579

Y. Wang, Y. Wang, C. Chen et al.

Neurocomputing 501 (2022) 566–582

Fig. 24. VQDNN (left) and classical neural network (right) training loss curve. In these two figures, as the depth (the number of hidden layer nodes) increases, the faster the
loss decreases.

very limited model classes that can be expressed by variational circuits. Repeating encoding can help to increase the frequency spectrum, and thereby the expressivity of a quantum neural network
model. Then, as additional layers are added to variational quantum
circuits, the expressibility will increase under certain circumstances, but does not always continue to improve. The observation
that different PQCs saturate at different layer numbers can inform
the choice of PQC used in practice. Finally, to compare the classification performance (expressibility and entangling capability of the
model), we concluded that if one is trying to design a PQC to
increase expressibility, it is better to insert two-qubit gates such
as Rz and Ry in pairs.

sophisticated network structure. Finally, a comparative experiment was conducted on the UCI hand-written digit datasets for
ten-label classification tasks. These experiments revealed that the
proposed VQDNN had excellent classification performance and
show that the VQDNN is superior to classical neural networks in
some specific learning tasks under the limitation of the same number of trainable parameters. In this section, we first compared and
analyzed the proposed model with other quantum neural network
models, focusing on the performance of different quantum models
on classification learning tasks. Then, theoretically analyzed the
validity of the model.
Skolik et al. [43] proposed a quantum neural network model,
using qubit encoding in combination with principal component
analysis (PCA), which means that each image in MNIST is represented by a vector with the 10 components. They obtained an accuracy of approximately 0.73 in the binary classification task. Wei
et al. [46] proposed a quantum convolutional neural network on
NISQ devices. In their two-class (‘0’ and ‘8’) and ten-class (‘0’ ‘9’)
image recognition experiments, the noise-free qcnn model
obtained 0.963 and 0.743 classification accuracies, respectively.
In Ref. [36] Potempa et al. achieved an accuracy of approximately
0.7. Johri et al. [18] designed a quantum nearest centroid classifier,
and experimentally demonstrated it on an 11-qubit trapped-ion
quantum machine. Finally, they achieved an accuracy of approximately 87.5% for the case of ‘2’ vs. ‘7’. For the 10 different digits,
they obtained an accuracy of approximately 77.5%. Lu et al. [28]
downsampled ‘3’ and ‘6’ images into 8  8 images to fit the QCNN
model with 6 qubits, and they obtained 0.9665 for the binary classification task.
Compared with the above five quantum neural network models,
our experimental classification accuracy did have certain advantages, which depend on the different data encoding technologies,
neural network structures, types of quantum gates, and model
training technologies. Specifically, we believe that the following
four practical implications were very important for the design of
quantum neural network classifiers.
First, for high-dimensional data, in addition to using PCA,
amplitude encoding can also be used to exponentially reduce the
dimensionality, and then other data encoding methods can be
selectively used according to the number of qubits available. Second, data encoding controls the expressiveness of quantum models. If the encoding is not ”rich” enough, we may end up with

5. Conclusions
It is important to understand that, driven by the real dilemma of
machine learning and the recent limitations of quantum computing, variational circuits have profoundly changed the research
goals of quantum machine learning. They are not aimed at the
acceleration of known models, but have produced a series of new
models. Currently, their usefulness is still largely unknown and
requires in-depth research. This shift in perspective has created
many new research questions. Such as what type of model is a
quantum circuit? How to choose an encoding method? Are their
quantum properties such as superposition and entanglement useful? How can we best train them in practice? What is their generalization ability? This study will focus on some important
preliminary answers to these questions.
We proposed a variational quantum deep neural network classification model and evaluate its classification performance using
three VQDNN classifiers on two general datasets. The main findings
of this study and the advantages of the model are as follows:
 Such a hybrid VQDNN architecture enabled us to build quantum
machine learning algorithms capable of dealing with lowdimensional or high-dimensional inputs and potentially to
implement these QML algorithms on NISQ devices with a limited number of qubits and shallow circuit depth.
 Numerical simulation results show that the proposed VQDNN
models can achieve excellent classification accuracy and have
better performance on the ten-label classification task than
580

Neurocomputing 501 (2022) 566–582

Y. Wang, Y. Wang, C. Chen et al.

their classical counterparts, which have the same tunable
parameters, confirming that the VQDNN classifier can provide
excellent classification ability.
 Additionally, we explored the way to build a more sophisticated
classifier by stacking multiple PQC layers and mixing the encoding method together. This shows that stacking more layers in
the VQDNN can obviously increase the model performance.
 The proposed VQDNN model can be applied in different quantum machine learning scenarios and potentially be implemented on NISQ devices, given the suitable encoding methods.

[11] I. Cong, S. Choi, M.D. Lukin, Quantum convolutional neural networks, Nat.
Phys. 15 (2019) 1273–1278.
[12] Y. Du, M.H. Hsieh, T. Liu, D. Tao, Expressive power of parametrized quantum
circuits, Phys. Rev. Res. 2 (2020) 033125.
[13] S. Endo, J. Sun, Y. Li, S.C. Benjamin, X. Yuan, Variational quantum simulation of
general processes, Phys. Rev. Lett. 125 (2020) 010501.
[14] R.P. Feynman, Simulating physics with computers, Feynman and computation,
CRC Press (2018) 133–153.
[15] F.J. Gil Vidal, D.O. Theis, Input redundancy for parameterized quantum circuits,
Front. Phys. 8 (2020) 297.
[16] E. Grant, M. Benedetti, S. Cao, A. Hallam, J. Lockhart, V. Stojevic, A.G. Green, S.
Severini, Hierarchical quantum classifiers, NPJ Quantum Inf. 4 (2018) 1–8.
[17] C. Guo, D. Poletti, Scheme for automatic differentiation of complex loss
functions with applications in quantum physics, Phys. Rev. E 103 (2021)
013309.
[18] S. Johri, S. Debnath, A. Mocherla, A. Singk, A. Prakash, J. Kim, I. Kerenidis,
Nearest centroid classification on a trapped ion quantum computer, NPJ
Quantum Inf. 7 (2021) 1–11.
[19] R. LaRose, A. Tikku, É. O’Neel-Judy, L. Cincio, P.J. Coles, Variational quantum
state diagonalization, NPJ Quantum Inf. 5 (2019) 1–10.
[20] Y. LeCun, L. Bottou, Y. Bengio, P. Haffner, Gradient-based learning applied to
document recognition, Proc. IEEE 86 (1998) 2278–2324.
[21] M. Lewenstein, Quantum perceptrons, J. Modern Opt. 41 (1994) 2491–2501.
[22] Y. Li, R.G. Zhou, R. Xu, J. Luo, W. Hu, A quantum deep convolutional neural
network for image recognition, Quantum Sci. Technol. 5 (2020) 044003.
[23] J. Liu, K.H. Lim, K.L. Wood, W. Huang, C. Guo, H.L. Huang, Hybrid quantumclassical
convolutional
neural
networks,
2019.
arXiv
preprint
arXiv:1911.02998..
[24] J. Liu, K.H. Lim, K.L. Wood, W. Huang, C. Guo, H.L. Huang, Hybrid quantumclassical
convolutional
neural
networks,
2019.
arXiv
preprint
arXiv:1911.02998..
[25] J. Liu, K.H. Lim, K.L. Wood, W. Huang, C. Guo, H.L. Huang, Hybrid quantumclassical convolutional neural networks, Sci. China Phys. Mech. Astron. 64
(2021) 1–8.
[26] S. Lloyd, Quantum machine learning for data classification, Physics 14 (2021)
79.
[27] S. Lloyd, M. Schuld, A. Ijaz, J. Izaac, N. Killoran, Quantum embeddings for
machine learning, 2020. arXiv preprint arXiv:2001.03622..
[28] Y. Lu, Q. Gao, J. Lu, M. Ogorzałek, J. Zheng, A quantum convolutional neural
network for image classification, in: 2021 40th Chinese Control Conference
(CCC), IEEE, 2021, pp. 6329–6334.
[29] M. Lubasch, J. Joo, P. Moinier, M. Kiffner, D. Jaksch, Variational quantum
algorithms for nonlinear problems, Phys. Rev. A 101 (2020) 010301.
[30] F.B. Maciejewski, F. Baccari, Z. Zimborás, M. Oszmaniec, Modeling and
mitigation of cross-talk effects in readout noise with applications to the
quantum approximate optimization algorithm, Quantum 5 (2021) 464.
[31] C. Miles, A. Bohrdt, R. Wu, C. Chiu, M. Xu, G. Ji, M. Greiner, K.Q. Weinberger, E.
Demler, E.A. Kim, Correlator convolutional neural networks as an interpretable
architecture for image-like quantum matter data, Nat. Commun. 12 (2021) 1–
7.
[32] M.A. Nielson, I.L. Chuang, Quantum computing and quantum information, in:
Cambridge University Press, Cambridge, 2000, pp. 13–28..
[33] H. Nishi, T. Kosugi, Y.i. Matsushita, Implementation of quantum imaginarytime evolution method on nisq devices by introducing nonlocal
approximation, NPJ Quantum Inf. 7 (2021) 1–7.
[34] P. Palittapongarnpim, P. Wittek, E. Zahedinejad, S. Vedaie, B.C. Sanders,
Learning in quantum control: High-dimensional global optimization for noisy
quantum dynamics, Neurocomputing 268 (2017) 116–126.
[35] A. Pesah, M. Cerezo, S. Wang, T. Volkoff, A.T. Sornborger, P.J. Coles, Absence of
barren plateaus in quantum convolutional neural networks, Phys. Rev. X 11
(2021) 041011.
[36] Potempa, R., Porebski, S., 2021. Comparing concepts of quantum and classical
neural network models for image classification task, in: Progress in Image
Processing, Pattern Recognition and Communication Systems. Springer, pp.
61–71..
[37] J. Preskill, Quantum computing in the nisq era and beyond, Quantum 2 (2018)
79.
[38] J. Romero, R. Babbush, J.R. McClean, C. Hempel, P.J. Love, A. Aspuru-Guzik,
Strategies for quantum computing molecular energies using the unitary
coupled cluster ansatz, Quantum Sci. Technol. 4 (2018) 014008.
[39] M. Schuld, A. Bocharov, K.M. Svore, N. Wiebe, Circuit-centric quantum
classifiers, Phys. Rev. A 101 (2020) 032308.
[40] M. Schuld, F. Petruccione, Information encoding, Supervised Learning with
Quantum Computers. Springer (2018) 139–171.
[41] M. Schuld, F. Petruccione, Representing data on a quantum computer, Machine
Learning with Quantum Computers. Springer (2021) 147–176.
[42] M. Schuld, R. Sweke, J.J. Meyer, Effect of data encoding on the expressive power
of variational quantum-machine-learning models, Phys. Rev. A 103 (2021)
032430.
[43] A. Skolik, J.R. McClean, M. Mohseni, P. van der Smagt, M. Leib, Layerwise
learning for quantum neural networks, Quantum Mach. Intell. 3 (2021) 1–11.
[44] Y. Subasßi, R.D. Somma, D. Orsucci, Quantum algorithms for systems of linear
equations inspired by adiabatic quantum computing, Phys. Rev. Lett. 122
(2019) 060504.

However, our research still has some shortcomings, as well as
some work that can be carried out in the future.
 Extension of our model to more complicated datasets such as
the Fashion-MNIST dataset and CIFAR-10 needs further indepth research in the future to test its robustness and
capability.
 Trying VQDNN with novel VQC architectures such as the quantum convolutional neural networks [31] to improve the performance of the current model is another further investigation.
 There is a fast growth in the number of qubits available in quantum computers [4], so it is necessary to implement this model
on quantum hardware in the future.
CRediT authorship contribution statement
Yunqian Wang: Conceptualization, Methodology, Software,
Writing – original draft. Wei Huang: Writing – review & editing.
Declaration of Competing Interest
The authors declare that they have no known competing financial interests or personal relationships that could have appeared
to influence the work reported in this paper.
Acknowledgement
This work is supported by the National Natural Science Foundation of China under Grant 62061029 and 61862043, and Natural
Science Foundation of Jiangxi Province under Grant
20204BCJ22011.
References
[1] F. Arute, K. Arya, R. Babbush, D. Bacon, J.C. Bardin, R. Barends, R. Biswas, S.
Boixo, F.G. Brandao, D.A. Buell, et al., Quantum supremacy using a
programmable superconducting processor, Nature 574 (2019) 505–510.
[2] A. Asuncion, D. Newman, Uci machine learning repository, 2007..
[3] A.B. de Avila, R.H. Reiser, M.L. Pilla, A.C. Yamin, State-of-the-art quantum
computing simulators: Features, optimizations, and improvements for d-gm,
Neurocomputing 393 (2020) 223–233.
[4] E. Bäumer, N. Gisin, A. Tavakoli, Demonstrating the power of quantum
computers, certification of highly entangled measurements and scalable
quantum nonlocality, NPJ Quantum Inf. 7 (2021) 1–6.
[5] K. Beer, D. Bondarenko, T. Farrelly, T.J. Osborne, R. Salzmann, D. Scheiermann,
R. Wolf, Training deep quantum neural networks, Nat. Commun. 11 (2020) 1–
6.
[6] M. Benedetti, E. Lloyd, S. Sack, M. Fiorentini, Parameterized quantum circuits
as machine learning models, Quantum Sci. Technol. 4 (2019) 043001.
[7] J. Bezanson, S. Karpinski, V.B. Shah, A. Edelman, Julia: A fast dynamic language
for technical computing, 2012. arXiv preprint arXiv:1209.5145..
[8] J. Biamonte, Universal variational quantum computation, Phys. Rev. A 103
(2021) L030401.
[9] A. Blance, M. Spannowsky, Quantum machine learning for particle physics
using a variational quantum classifier, J. High Energy Phys. 2021 (2021) 1–20.
[10] M. Cerezo, A. Arrasmith, R. Babbush, S.C. Benjamin, S. Endo, K. Fujii, J.R.
McClean, K. Mitarai, X. Yuan, L. Cincio, et al., Variational quantum algorithms,
2020. arXiv preprint arXiv:2012.09265..

581

Y. Wang, Y. Wang, C. Chen et al.

Neurocomputing 501 (2022) 566–582
Runcai Jiang received his bachelor’s degree in Information Management and Information System from
Northeastern University, China, in 2018. He is currently
pursuing a M.S. degree in Software Engineer at Nanchang University, China. His current research interests
are quantum machine learning algorithms, deep learning, and their applications in image processing, computer vision.

[45] M. Watabe, K. Shiba, C.C. Chen, M. Sogabe, K. Sakamoto, T. Sogabe, Quantum
circuit learning with error backpropagation algorithm and experimental
implementation, Quantum Rep. 3 (2021) 333–349.
[46] S. Wei, Y. Chen, Z. Zhou, G. Long, A quantum convolutional neural network on
nisq devices, 2021. arXiv preprint arXiv:2104.06918..
[47] H. Yano, Y. Suzuki, R. Raymond, N. Yamamoto, Efficient discrete feature
encoding for variational quantum classifier, in: 2020 IEEE International
Conference on Quantum Computing and Engineering (QCE), IEEE, 2020, pp.
11–21.
[48] H.S. Zhong, H. Wang, Y.H. Deng, M.C. Chen, L.C. Peng, Y.H. Luo, J. Qin, D. Wu, X.
Ding, Y. Hu, et al., Quantum computational advantage using photons, Science
370 (2020) 1460–1463.

Yunqian Wang received his M.S. degree in Computer
Applied Technology from the University of Science and
Technology of China (USTC), China, in 2010. He is currently pursuing a Ph.D. degree at Nanchang University,
China. Since 2010, he has been working in Nanchang
University, Nanchang, P. R. China, where he is currently
an Assistant Professor. His current research interests are
quantum computation, quantum machine learning
algorithms deep learning, and their applications in
pattern recognition, image processing and computer
vision.

Wei Huang obtained his B.Eng. and M.Eng. degrees from
the Harbin Institute of Technology, China. He obtained
his Ph.D. degree from the Nanyang Technological
University, Singapore. He then worked in the University
of California San Diego, USA, as well as the Agency for
Science Technology and Research, Singapore as Postdoctoral Research Fellows. He is now a Full Professor
with the Department of Compute Science and acts as
the Head at the Informatization Office in the Nanchang
University, China. Dr. Huang’s main research interests
include machine learning, pattern recognition, medical
image processing, and multimedia. He has published
over 100 academic journal/ conference papers, including IEEE Transactions on
Medical Imaging, IEEE Transactions on Multimedia, IEEE Transactions on Circuits
and Systems for Video Technology, MICCAI, ACM Multimedia, etc. He has been
acting as the principal investigator/ co-PI in nearly 20 national/ provincial grants,
including 5 NSF-China projects and 2 NSF key projects in Jiangxi Province, China. He
received the Jiangxi Provincial Natural Science Award, the best paper award of
MICCAI-MLMI, the most interesting paper award of ICME-ASMMC, etc. He has also
been entitled the provincial academic leader of the Jiangxi Province in 2020.

Yufeng Wang received his bachelor’s degree in Software Engineering from Shandong Jianzhu University,
China, in 2021.He is currently pursuing a M.S. degree in
Computer Technology at Nanchang University, China.
His current research interests are quantum machine
learning algorithms,deep learning, and their applications in image processing, computer vision.

Chao Chen received his bachelor’s degree in Software
Engineering from Jiangxi Normal University, China, in
2021. He is currently pursuing a M.S. degree in Computer technology at Nanchang University, China. His
current research interests are quantum machine learning algorithms, deep learning, and their applications in
data processing, image processing, computer vision.

582

