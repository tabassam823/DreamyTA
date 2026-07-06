Available online at www.sciencedirect.com
Available online at www.sciencedirect.com

Available online at www.sciencedirect.com

ScienceDirect

Procedia Computer Science 00 (2025) 000–000
Procedia
Computer
Science
(2025)
000–000
Procedia
Computer
Science
25800
(2025)
633–646

www.elsevier.com/locate/procedia
www.elsevier.com/locate/procedia

International Conference on Machine Learning and Data Engineering

International Conference on Machine Learning and Data Engineering
A Scoping
Survey of Quantum Machine Learning and Deep
A Scoping Learning
Survey offor
Quantum
Machine
Learning and Deep
Real-World
Applications
Learning
for Real-World Applications
Aishwarya Ca , Venkatesan Ma , Prabhavathy Pb
a Department of Computer Science
a
a Puducherry, Puducherry,
b India
and Engineering, NIT

Aishwarya C , Venkatesan M , Prabhavathy P

b Department of Computer Science and Engineering, VIT Vellore, Vellore, India

a Department of Computer Science and Engineering, NIT Puducherry, Puducherry, India
b Department of Computer Science and Engineering, VIT Vellore, Vellore, India

Abstract
Abstract
Many prevalent issues in today’s society, such as fake news detection, can be efficiently addressed using artificial intelligence and
machine learning techniques. The rapid dissemination of fake news through social media makes it challenging to verify the validity
prevalent
issues
today’s
society,promising
such as fake
news detection,
canmodels
be efficiently
addressed
using artificial
of Many
information.
QML
andinQDL
represent
frontiers
for building
to address
these challenges,
withintelligence
the prospectand
of
machine
rapidadvancements
disseminationinofthe
fake
newsThis
through
media
makes
it challenging
verify
validity
achievinglearning
quantumtechniques.
advantageThe
driving
field.
studysocial
examines
and
compares
literaturetoon
QMLthe
and
QDL
of
information.
QML
and QDL
promising
for building
models
to address
these challenges,
with the
of
models,
including
QSVM,
VQE,represent
QNN, QCNN,
and frontiers
RQNN, using
the MNIST
dataset.
The effectiveness
and scope
of prospect
application
achieving
quantum
advantage
driving
advancements
in
the
field.
This
study
examines
and
compares
literature
on
QML
and
QDL
of these models for fake news detection and other real-world applications are analyzed.
models, including QSVM, VQE, QNN, QCNN, and RQNN, using the MNIST dataset. The effectiveness and scope of application
of these models for fake news detection and other real-world applications are analyzed.
© 2025 The Authors. Published by Elsevier B.V.
This
is an
open
accessPublished
article under
the CC BY-NC-ND
license (http://creativecommons.org/licenses/by-nc-nd/4.0/)
© 2025
The
Authors.
by Elsevier
B.V.
©
2025 The Authors.
Published byofElsevier
B.V. committee of the International Conference on Machine Learning and Data
Peer-review
under
responsibility
theCC
scientific
This is an open
access
article under the
BY-NC-ND
license (https://creativecommons.org/licenses/by-nc-nd/4.0)
This
is an open access article under the CC BY-NC-ND license (http://creativecommons.org/licenses/by-nc-nd/4.0/)
Engineering.
Peer-review
under responsibility of the scientific committee of the International Conference on Machine Learning and Data Engineering
Peer-review under responsibility of the scientific committee of the International Conference on Machine Learning and Data
Keywords: Quantum Machine Learning; Deep Learning; Real-World Applications; Fake News Detection; Quantum Advantage
Engineering.
Keywords: Quantum Machine Learning; Deep Learning; Real-World Applications; Fake News Detection; Quantum Advantage

1. Introduction
1. Introduction
Over the last decade, AI and ML have evolved into key transformative technologies, witnessing rapid advancements
across both theoretical and practical domains. These fields enable the processing of large-scale data and the generation
Over the last decade, AI and ML have evolved into key transformative technologies, witnessing rapid advancements
of predictive insights, rendering them indispensable in numerous real-world systems, such as healthcare diagnostics,
across both theoretical and practical domains. These fields enable the processing of large-scale data and the generation
autonomous systems, and financial modeling [1, 2]. Classical AI approaches have substantially optimized tasks that
of predictive insights, rendering them indispensable in numerous real-world systems, such as healthcare diagnostics,
were previously manual or inefficient; however, significant computational bottlenecks are arising, particularly in
autonomous systems, and financial modeling [1, 2]. Classical AI approaches have substantially optimized tasks that
scalability, processing speed, and resource consumption [3].
were previously manual or inefficient; however, significant computational bottlenecks are arising, particularly in
scalability, processing speed, and resource consumption [3].
∗ Corresponding author. Tel.: +91 9448251453.

E-mail address: sivagaish23@gmail.com

∗ Corresponding author. Tel.: +91 9448251453.

E-mail address: sivagaish23@gmail.com

1877-0509 © 2025 The Authors. Published by Elsevier B.V.
This
is an open
access
under
the CC BY-NC-ND
1877-0509
© 2025
Thearticle
Authors.
Published
by Elsevier license
B.V. (http://creativecommons.org/licenses/by-nc-nd/4.0/)
1877-0509
2025access
The Authors.
Published
Elsevier
B.V.of license
Peer-review
under
responsibility
the scientific
committee
the International
Conference on Machine Learning and Data Engineering.
This is an ©
open
article of
under
the by
CC
BY-NC-ND
(https://creativecommons.org/licenses/by-nc-nd/4.0)
This
is an open under
access article
under the CC
license
(http://creativecommons.org/licenses/by-nc-nd/4.0/)
Peer-review
responsibility
of BY-NC-ND
the scientific
committee
of the International Conference on Machine Learning and
Peer-review under responsibility of the scientific committee of the International Conference on Machine Learning and Data Engineering.

Data Engineering

10.1016/j.procs.2025.04.297

634
2

Aishwarya C et al. / Procedia Computer Science 258 (2025) 633–646
Aishwarya C / Procedia Computer Science 00 (2025) 000–000

The advent of Quantum Computing (QC) introduces the potential to overcome these limitations, providing the
foundation for Quantum Machine Learning (QML) and Quantum Deep Learning (QDL) [4]. Unlike its classical counterpart, quantum computing leverages the principles of quantum mechanics to perform computations, enabling parallel
processing of large datasets through quantum superposition and entanglement. The era of quantum advantage, where
quantum computers surpass classical computers in solving specific problems, is approaching, and By merging Quantum Computing and Machine Learning, AI systems could see substantial improvements in efficiency and processing
speed, leading to groundbreaking applications [5].
A core advantage of QML lies in its ability to significantly reduce the training time for complex models. Classical
AI systems, though effective, require substantial time and computational resources to train deep neural networks and
other models, particularly when handling high-dimensional data. In contrast, quantum computers have demonstrated
the potential to accelerate these processes by several orders of magnitude. It is estimated that QML algorithms can
outperform classical ML algorithms by up to 100x, with even more significant speedups possible in certain cases
[6]. This represents a key milestone towards achieving quantum supremacy— the point at which quantum machines
outperform classical systems in all but trivial tasks [7].
Effectively harnessing the power of quantum systems requires representing classical data in a quantum-compatible
format. Encoding classical data into quantum formats, such as amplitude encoding or phase encoding, allows for
exponential data representation. This method enables more efficient operations on massive datasets using fewer
quantum bits (qubits) than classical bits [8]. Quantum systems’ ability to encode and manipulate large amounts of
information with fewer resources offers distinct advantages over classical methods, especially for tasks involving
high-dimensional and complex data structures.
A fundamental component of QML is the use of Parameterized Quantum Circuits (PQC). PQCs consist of quantum
gates with tunable parameters optimized during training, similar to how weights in classical neural networks are
optimized. The entanglement between qubits in PQCs facilitates the exploration of complex data relationships, enabling
the discovery of patterns that would be computationally prohibitive for classical systems [9]. Optimization of these
parameters through quantum gradient descent or other quantum-enhanced methods leads to faster convergence and
more accurate models.
This paper offers a comprehensive analysis of QML and QDL models, focusing on the computational advantages in
terms of speed, model complexity, and data efficiency. Applications in real-world scenarios, such as financial modeling,
cryptography, and drug discovery, are also explored [10]. A comparative analysis will evaluate the performance of
quantum models against classical ML approaches, highlighting the benefits that quantum computing brings to machine
learning tasks [11] .

2. Related Works and Basic Concepts
In recent years, significant research has been conducted in the domain of quantum computing and its applications in
machine learning[12]. The idea of using quantum mechanics to enhance machine learning algorithms is not entirely new
but has gained tremendous attention as quantum hardware advances. Quantum Machine Learning (QML) represents
an amalgamation of quantum computation and traditional machine learning, promising superior computational speeds
and efficiencies compared to classical counterparts [5].
Several studies have laid the foundation for QML by exploring different quantum algorithms that can be applied
to machine learning problems [13]. One of the pioneering approaches was the Quantum Support Vector Machine
(QSVM) [11], which leverages quantum computing to speed up classification tasks, as demonstrated in the works
of [14]. Similarly, quantum variants of clustering algorithms have been proposed, showing faster processing times
compared to classical clustering techniques [15]. Additionally, the potential of quantum neural networks (QNNs) has
been widely discussed, particularly for tasks involving deep learning, where quantum principles can optimize training
times and model convergence [16].
Another critical area in QML research is the encoding of classical data into a quantum-compatible format. Methods
such as amplitude encoding and phase encoding [13] have been employed to represent classical data with fewer
quantum bits (qubits), allowing for more efficient computations [8]. These encoding techniques have been integral
in improving the efficiency of quantum machine learning algorithms. The development of Parameterized Quantum

Aishwarya C et al. / Procedia Computer Science 258 (2025) 633–646
Aishwarya C / Procedia Computer Science 00 (2025) 000–000

635
3

Circuits (PQC) [11], which are essential for many QML models, has been a topic of significant exploration as well.
PQCs utilize entangled qubits to identify complex patterns in data, leading to improved learning models [9].
In the context of real-world applications, quantum algorithms have shown promise in fields like cryptography,
drug discovery, and optimization tasks. For instance, quantum-enhanced reinforcement learning has been applied to
optimize decision-making systems in financial markets [17], while quantum algorithms have been used to simulate
molecular interactions in drug discovery, significantly reducing the time required for these simulations [18].
2.1. Basic Concepts of Quantum Machine Learning
As quantum computing and learning differ from classical computing in some of the key concepts, it is important
to establish a basic understanding of the underlying concepts, namely the qubit, product states, entanglement, and
parameterized circuits, before attempting to draw comparisons in the models.
2.1.1. Qubit
The qubit is the unit of storage in quantum computers that records data, but it differs from the classical bit, which
can only be in discrete states, either 0 or 1 [13]. A qubit, in theory, can occupy a superposition of states, meaning it
can be in both a 0 and 1 state simultaneously, and upon measurement, can produce either value with a probability [19].
The value of a qubit is represented using a column vector of probability amplitudes, which represent the probability
of each state being measured. The amplitudes can be negative, and the sum of squares of all amplitudes is always 1.
A Hadamard gate can be used to place a qubit into an equal superposition of 0 and 1. Other unitary gates modify the
probability amplitudes of qubits, and through different superpositions, it becomes possible to represent more data.
2.1.2. Data Encoding
Unlike classical bits, qubits can represent more data. Encoding classical data can be done using simple binary
strings, or the data can be translated to accommodate the probability amplitudes of the qubit. Data may even be
encoded in the angles of amplitude in the qubit [20, 19]. Quantum data can also be used directly.

Fig. 1: Block Sphere of qubit

2.1.3. Product State and Entanglement
When considering two or more qubits in a circuit, their combined possible states can also be represented in a column
vector. For two qubits, there are four possible states, each with its probability of being measured. A superposition
of states where the qubits’ states directly contribute to the combined state, without dependence on other qubits, are
known as product states, behaving similarly to classical bits. When the combined superposition cannot be represented
as a combination of individual states, the qubits are considered entangled. Entanglement has various applications in
quantum computing, such as in the teleportation protocol in communication and quantum learning. Entanglement is
often achieved using two-qubit gates like the controlled NOT (CX) gate. Gates such as the Hadamard or CX gate have
defined state transitions, represented by square matrices called Pauli matrices, which describe operations on qubits
through state transitions.

636
4

Aishwarya C et al. / Procedia Computer Science 258 (2025) 633–646
Aishwarya C / Procedia Computer Science 00 (2025) 000–000

2.1.4. Parameterized Circuit
In quantum machine learning, models are often represented as circuits with gates containing tunable parameters (𝜃𝜃)
[19]. These parameters can be trained and optimized using the gradient descent approach, which involves calculating
a cost function and adjusting the parameters by a multiple of its derivative to the parameter and the learning rate,
a defined hyperparameter. This is analogous to classical machine learning. In quantum machine learning, the cost
function typically involves the expectation value, which is the average of the expected state values of the parameter
vector.
3. PARAMETERS FOR COMPARISON
Having established the core concepts behind QML and QDL, the parameters for performing the analysis are decided
by identifying the factors that affect the performance and viability of the model for real-world applications. This is
done by focusing on three key questions:
1. What primarily affects the size of the model?
2. What affects the speed of the model?
3. What affects the accuracy of the model?
Upon reviewing the models and research on QML and QDL, the following conclusions are drawn: The size of the
model is primarily affected by the size and complexity of the dataset, as well as the number of qubits available for the
model. This allows for ideal fitting, as complexity requires more layers of optimizer PQCs before obtaining results,
and the number of qubits limits the scope. Therefore, the goal for a QML or QDL model is to achieve a balance in
the number of optimizer PQCs required over the number of qubits available. An effective model will use a moderate
number of gates on fewer qubits, allowing for scalability. The speed of the model is primarily influenced by the nature
of qubits and the required circuit for the model, and is more dependent on architecture than development design.
For comparison purposes, it is assumed that the architecture of the models is identical and does not affect speed, so
the number of epochs required becomes relevant. Finally, the accuracy of the model depends on the complexity and
degree of entanglement, or the number of gates in the optimizer PQC. This leads to increased size, so it is important
to maintain feasibility between size, speed, and accuracy. The number of qubits, gates (if mentioned), epochs, and the
achieved accuracy and F1 score presented in the research will serve as the comparison parameters moving forward.
4. Models for Comparison
This survey considers research on QML models like QSVM and VQT and QDL models such as QNN, QCNN,
and RQNN. The goal is to provide a precise summary of each model and its characteristics and compare them to one
another to determine their advantages.
4.1. QSVM
4.1.1. Model Explanation
QSVM and its variant QSVM-Kernel utilize quantum circuits to efficiently handle machine learning tasks. By
mapping classical data points nonlinearly to a high-dimensional feature space using N qubits[13], QSVM enables
classification based on separation hyperplanes derived from the training phase [21]. Comparative evaluations against
classical SVM classifiers have demonstrated QSVM’s process, particularly evident in applications like handwritten
digit recognition on the MNIST dataset. QSVM exhibits significant speed advantages and improved accuracy, making
it a promising candidate for accelerating complex machine learning problems.
4.1.2. Experimentation
A QSVM architecture configured with 14 qubits and 32 parameters was employed. The training process spanned
50 epochs, and the accuracy was meticulously recorded after every 20 batches [22]. Table 1 below presents the mean
and standard deviation of the classification accuracy obtained using this QSVM setup with the MNIST dataset.

Aishwarya C et al. / Procedia Computer Science 258 (2025) 633–646
Aishwarya C / Procedia Computer Science 00 (2025) 000–000

637
5

Fig. 2: Structure of QSVM Network
Table 1: Experimental results - QSVM

Algorithms
Qubits
Parameters
Readouts
Best accuracy (%)
Best F1 score

QSVM
14
32
1
84.68 ± 0.6%
0.8878

4.1.3. Applications of QSVM
Beyond digit recognition, QSVM finds applications in image recognition, pattern detection, and quantum-classical
hybrid models. Its ability to handle high-dimensional feature spaces and leverage quantum computing capabilities
opens avenues for tackling real-world problems across domains [23].
4.2. VQT
4.2.1. Model Explanation
VQT offers a novel approach to simulating complex thermal states using variational quantum circuits [24]. Leveraging the variational principle, VQT optimizes quantum circuits iteratively to approximate thermal equilibrium states
of a given Hamiltonian. Demonstrating efficiency in modeling thermal systems, VQT outperforms classical methods
in certain regimes. Its applications span condensed matter physics, chemistry, and material science, providing insights
into phase transitions, energy distributions, and correlation functions within quantum systems.
4.2.2. Experimentation
A VQT architecture configured with 12 qubits and 16 parameters was employed. The training process spanned
50 epochs, and the accuracy was meticulously recorded after every 20 batches. Table 5 below presents the mean and
standard deviation of the classification accuracy obtained using this VQT setup with the MNIST dataset.
Table 2: Experimental results - VQT

Algorithms
Qubits
Parameters
Readouts
Best accuracy (%)
Best F1 score

VQT
12
24
1
86.16 ± 0.4%
0.8228

638
6

Aishwarya C et al. / Procedia Computer Science 258 (2025) 633–646
Aishwarya C / Procedia Computer Science 00 (2025) 000–000

4.2.3. Applications of VQT
VQT’s potential applications extend to material design, fundamental physics research, and the exploration of
emergent phenomena in quantum systems [25]. As quantum computing technology advances, VQT stands poised to
become a valuable tool for understanding complex thermal behavior and designing novel materials.
4.3. QNN
4.3.1. Model Explanation
Quantum Neural Networks (QNNs) merge quantum computing with neural networks, offering new computational
possibilities. Unlike classical neural networks that use bits (0 or 1), QNNs use qubits, which can exist in multiple
states simultaneously due to superposition. QNNs utilize quantum gates to process information, exploiting quantum
properties like superposition and entanglement [11] to perform computations that might be more efficient or parallel
compared to classical methods. While QNNs aim to learn and predict patterns, much like traditional neural networks,
their full potential depends on advances in scalable quantum computing technology.

Fig. 3: Structure of QNN circuit [26]

4.3.2. Experimentation
The model was set up with 8 Qubits and 16 parameters. It was trained over 20 epochs, and the accuracy was recorded
for every 32 batches. In this work, the mean and the standard deviation of the classification accuracy using the QNN
architecture with the MNIST dataset are given in the following table [27, 28].
Table 3: Experimental results - QNN

Algorithms
Qubits
Parameters
Readouts
Best accuracy (%)
Best F1 score

QNN
8
16
1
82.88 ∼ 1%
0.8378

4.3.3. Applications of QNN
Reinforcement Learning: Deep learning has increasingly been combined with reinforcement learning to optimize
actions in complex state spaces. Integrating quantum deep learning into reinforcement learning is still in its infancy.
The current approach replaces the policy training network with a Quantum Neural Network (QNN) [29] instead of
a traditional deep neural network. Classical deep reinforcement learning algorithms may be adapted for quantum
systems. If QNNs demonstrate quantum computational advantages in complex environments like intricate Markov
decision processes, quantum reinforcement learning could significantly advance the field.

Aishwarya C et al. / Procedia Computer Science 258 (2025) 633–646
Aishwarya C / Procedia Computer Science 00 (2025) 000–000

639
7

Communication Networks: Quantum Neural Networks (QNNs) and quantum reinforcement learning techniques
are widely applicable across diverse domains, such as communication networks [29]. In decentralized systems like
blockchain, QNNs can potentially speed up computational processes significantly. Furthermore, modern communication technologies, including the Internet of Things (IoT), millimeter-wave networks, caching infrastructures, and video
streaming [29] platforms, present valuable opportunities for implementing QNNs and quantum reinforcement learning
algorithms.
4.4. QCNN
4.4.1. Model Explanation
Quantum computing uses quantum mechanics principles for computation, and Quantum Convolutional Neural
Networks (QCNNs) integrate these concepts into neural networks. Unlike classical bits, qubits in quantum computers
can exist in multiple states simultaneously, offering potential advantages for certain tasks. QCNNs apply quantum
convolutional layers, using quantum gates to perform operations similar to classical CNNs, with the hope that quantum
properties like superposition and entanglement will enhance optimization and pattern recognition[13].
While classical machine learning handles tasks like image recognition effectively, translating quantum problems
into classical frameworks is challenging due to the exponentially large Hilbert space involved. Quantum algorithms
can address these challenges, but the current limitations in quantum hardware [30], such as size and coherence times,
restrict the deployment of large-scale quantum networks.

Fig. 4: Representation of CNN [28]

4.4.2. Experimentation
The model was set up with 8 Qubits and 63 parameters. It was trained over 20 epochs, and the accuracy was recorded
for every 32 batches. The mean and standard deviation of the classification accuracy using the QCNN architecture
with the MNIST dataset are given in Table [27].
4.4.3. Applications of QCNN
Computer Vision Applications: CNN is extensively used in image recognition and object detection for classification purposes. QCNN can increase computational speeds with better performance metrics compared to classical
computational methods.[31]
Quantum Chemistry: Modeling molecular structures and simulating quantum systems for drug discovery or
materials science could benefit from QCNNs [11]. These networks might provide more accurate representations of
quantum states, allowing for better predictions and optimizations in quantum chemistry simulations [31].

640
8

Aishwarya C et al. / Procedia Computer Science 258 (2025) 633–646
Aishwarya C / Procedia Computer Science 00 (2025) 000–000
Table 4: Experimental results - QCNN

Algorithms
Qubits
Parameters
Readouts
Best accuracy (%)
Best F1 score

QCNN
8
63
1
93.17 ∼ 1%
0.9352

Financial Modeling: QCNNs might be applied to quantum-enhanced financial modeling for portfolio optimization,
risk assessment, and other quantitative finance tasks. Quantum computing’s potential for handling complex optimization
problems could be particularly beneficial in this domain [31].
Complex System Simulations: QCNNs could contribute to simulating and understanding complex quantum
systems, surpassing the capabilities of classical computers in certain scenarios. This has implications for materials
science, physics, and other fields where simulating intricate quantum behaviors is crucial [31].
4.5. RQNN
4.5.1. Model Explanation
Recurrent Neural Networks (RNNs) play a fundamental role in modeling sequential data for tasks like machine
translation and speech synthesis. These networks utilize hidden memory cells that factor in previous inputs, with
variations like LSTM and GRU [32] adjusting input influence. However, optimizing RNNs for long sequences remains
challenging due to issues like vanishing or exploding gradients, which hinder training performance.
In contrast, quantum computing is still emerging, but quantum machine learning models like variational quantum
eigensolvers (VQEs) [32] have shown promise. Building on this, researchers are developing Recurrent Quantum Neural
Networks (RQNNs) to handle sequential data. The proposed RQNN model uses a VQE to optimize each input layer
or iteration, with the cell state stored in additional qubits for further iterations, altering inputs with each pass [32].

Fig. 5: Schematic representation of the proposed RQNN circuit
[32]

Fig. 6: QRNN, by applying the same QRNN cell constructed repeatedly to a sequence of input words. [32]

4.5.2. Experimentation
The QRNN was implemented in PyTorch, utilizing custom quantum gate layers to extract predicted distributions at each step [32]. Since this was a quantum computation simulation, certain shortcuts were applied: instead
of using fixed-point amplitude amplification for quantum neurons and outputs during training, post-selection probabilities were manually selected and tracked to estimate the necessary overhead. Output probabilities were directly
extracted, rather than being estimated through measurements at each step. The experiments focused on character-wise

Aishwarya C et al. / Procedia Computer Science 258 (2025) 633–646
Aishwarya C / Procedia Computer Science 00 (2025) 000–000

641
9

RNNs, using various data preprocessing methods, including PCA. The predicted distributions were fed into PyTorch’s
nn—CrossEntropyLoss for gradient-based learning via PyTorch’s auto-grad framework. On quantum hardware, alternative methods such as gradient-free optimizers or numerical gradients would be required. The experiments were
executed on 2-8 CPUs, with memory usage ranging from 500MB to 35GB per core and parallel batch training. Running
the QRNN on real hardware would involve parallel execution across multiple devices, averaging the losses [32].
Table 5: Experimental results - RQNN

Algorithms
Qubits
Parameters
Readouts
Best accuracy (%)
Best F1 score

RQNN
10
1292
1
94.6 ± 0.4%
-

4.5.3. Applications of RQNN
Recurrent Quantum Neural Networks find scope for application in any sequential data task and NLP application
such as Sentiment analysis, Chatbots, Machine Translation and speech synthesis, as well as text analytics [33]. Realtime sentiment analysis tracks social media mentions, monitors feedback on marketing initiatives or product launches,
and gives a general idea of how an audience feels about a business [32, 33]. Likewise, any application involving
time-sequenced text, images, or media can be optimized and categorized using RNNs, with RQNNs speeding up large
applications in these domains. Natural language processing has many use cases in the digital world, and this list will
expand as more organizations and industries adopt it and recognize its benefits. While human interaction is crucial
for complex communication challenges, NLP simplifies and automates simpler tasks before addressing more intricate
ones [33].
5. QML SOFTWARE
This section reviews several key quantum computing resources, software, and tools for developing quantum machine
learning algorithms.
- Microsoft Azure Quantum: Part of the Azure Cloud, Azure Quantum requires membership access. It allows
users to develop quantum programs using Q# within the Quantum workspace and run them on simulators or partner
quantum computers like IONQ, Quantinuum, and Rigetti. Azure Quantum integrates with other Azure services
and supports Qiskit [19] programming. Q#, a language compatible with .NET, offers high-level abstraction and
libraries for quantum algorithms, quantum chemistry, and machine learning [34]. Comprehensive resources, including
documentation, tutorials, and a GitHub repository, support learning and development [35]. The classifier uses singlequbit rotations and two-qubit controlled rotations, with the learnable parameters being the rotation angles [36]. Users
can design custom classifiers using quantum operations on circuit qubits [37].
- IBM Quantum Computing Solutions for Enterprises: IBM offers enterprise-level quantum computing solutions,
adhering to IEEE standards for accuracy, reliability, and interoperability. The IBM Quantum Optimization Solver
uses quantum annealing to enhance performance in solving complex optimization problems like supply chain logistics
and portfolio management [11]. IBM Quantum Machine Learning integrates quantum capabilities into traditional
machine learning workflows, enabling more accurate and efficient model training. IBM Quantum Financial Services
Solutions provides specialized tools for portfolio optimization, risk management, and fraud detection in the financial
sector, while IBM Quantum Supply Chain Solutions optimizes logistics and resource allocation using quantum
methodologies.
- IBM Quantum Computing Tools: IBM provides tools like the IBM Quantum Composer, a graphical interface
for designing quantum circuits, and IBM Quantum Experience, an online platform offering access to quantum
processors, tutorials, and resources. Qiskit, IBM’s open-source quantum computing framework, enables users to
create, manipulate, and analyze quantum circuits, with extensive support for algorithm development and execution on
quantum systems.

Aishwarya C et al. / Procedia Computer Science 258 (2025) 633–646
Aishwarya C / Procedia Computer Science 00 (2025) 000–000

642
10

- AWS Quantum Computing: AWS Quantum Computing, through Amazon Braket, offers cloud-based access to
quantum resources. It supports quantum-classical hybrid computing, and various quantum processors, and integrates
with other AWS services. Despite current limitations in the Noisy Intermediate-Scale Quantum (NISQ) era, AWS
explores applications like [38] Quantum solutions for portfolio optimization, leveraging algorithms like the Quantum
Approximate Optimization Algorithm (QAOA) to potentially achieve computational speedup.
Algorithm: Quantum computers leverage unique properties of quantum mechanics, notably qubits in superposition,
enabling simultaneous processing of numerous possibilities. Entanglement links qubit states regardless of distance,
while interference manipulates quantum state amplitudes to alter outcome probabilities. Quantum algorithms, such
as Shor’s algorithm, demonstrate superior efficiency compared to classical counterparts, solving certain problems
exponentially faster. The Quantum Approximate Optimization Algorithm (QAOA) blends classical and quantum
computation, utilizing mixer and cost layers to explore potential solutions. Classically fine-tuned parameters iteratively
converge during each QAOA run, moving towards optimal values. This hybrid approach capitalizes on quantum
advantages while integrating classical optimization for enhanced performance.

Fig. 7: A schematic representation of QAOA.

The circuit is composed of ‘p’ layers, each having a cost sub-layer function and a mixer sub-layer function.
Variational parameters are changed with a classical optimizer after measuring the objective function following each
iteration. The Quantum Approximate Optimization Algorithm (QAOA) is a versatile algorithm adept at solving
optimization problems with numerous constraints. When incorporating constraints, two primary options exist. The
first involves modifying the mixer layer to include only valid solutions, limiting the search space. The second option
alters the cost layer by adding a penalty factor to penalize invalid solutions, producing shallower circuits suitable for
near-term noisy quantum computers. This study focuses on implementing a penalty factor for portfolio optimization to
increase the likelihood of selecting an optimal asset mix. Two constraint types, equality and inequality, are explored.
For equality constraints, a defined budget 𝜇𝜇 is introduced, requiring the entire budget to be spent. A penalty factor
coefficient 𝜎𝜎 is added to the portfolio optimization problem to ensure compliance.

𝜔𝜔

𝑜𝑜 𝑜𝑜𝑜𝑜


2
∑︁
 1 𝑇𝑇

𝑇𝑇
= arg min  𝜔𝜔 Σ𝜔𝜔 − 𝜆𝜆𝜆𝜆 𝜔𝜔 + 𝜎𝜎
𝜔𝜔𝑖𝑖 − 𝜇𝜇 
𝜔𝜔
2
𝑖𝑖



(1)

For inequality constraints, an upper spending limit is set: Σ𝜔𝜔𝑖𝑖 ≤ 𝜇𝜇. Introducing slack variables (s) eliminates penalty
term factors for valid solutions, satisfying the inequality condition. Although adding slack variables increases qubit
and operational step requirements, it results in shallower circuits compared to the alternative method of incorporating
constraints.

Aishwarya C / Procedia Computer Science 00 (2025) 000–000

Aishwarya C et al. / Procedia Computer Science 258 (2025) 633–646


2
∑︁
1


𝜔𝜔𝑜𝑜 𝑜𝑜𝑜𝑜 = arg min  𝜔𝜔𝑇𝑇 Σ𝜔𝜔 − 𝜆𝜆𝜆𝜆𝑇𝑇 𝜔𝜔 + 𝜎𝜎
(𝜔𝜔𝑖𝑖 + 𝑠𝑠𝑖𝑖 − 𝜇𝜇) 
𝜔𝜔
2
𝑖𝑖



11

643

(2)

This emphasis on shallow circuits is crucial, given the error susceptibility of current quantum computers, where
errors accumulate with increasing circuit depth. By exploring penalty factors and constraints in portfolio optimization, this research aims to enhance the practicality and effectiveness of quantum algorithms for real-world financial
applications on existing quantum computing hardware.
The analysis of the results [39] reveals that the results are sensitive to the penalty factor, which must be analyzed
with different values to fit individual use cases.
- Optimization of Robot Trajectory Planning with Nature-Inspired and Hybrid Quantum Algorithms [20]:
Robot motion planning is critical in industries like automotive, manufacturing, and logistics, where optimizing robotic
paths is essential for tasks such as welding, painting, and assembly. Efficient load balancing among numerous robots and
task sequencing is crucial to meet production demands. Quantum computing, particularly quantum annealing devices
from companies like D-Wave Systems Inc., offers promising solutions for these complex optimization problems,
although the field is still evolving from research to practical applications. The main challenge is identifying the
quantum hardware and algorithms that will provide a real-world advantage.
To address these challenges, optimization methods must bridge the gap until scalable quantum hardware becomes
available, allowing for a seamless transition to quantum solutions when accessible. Current quantum hardware, especially annealers, utilizes the Quadratic Unconstrained Binary Optimization (QUBO) framework [13]. This framework
models a wide range of NP-hard combinatorial problems, though it can require many variables for certain applications.
The QUBO cost function is represented by the Hamiltonian:

𝐻𝐻QUBO = x𝑇𝑇 𝑄𝑄x =

∑︁

𝑥𝑥 𝑖𝑖 𝑄𝑄 𝑖𝑖 𝑖𝑖 𝑥𝑥 𝑗𝑗

(3)

𝑖𝑖𝑖 𝑖𝑖

where x is a vector of binary decision variables, and Q is the matrix encoding the problem. To guide the solver towards
feasible solutions, penalty terms are added to the Hamiltonian to enforce constraints, such as visiting exactly one node
per time step and ensuring all seams are visited once during the tour.

Fig. 8: Flow chart illustrating the end-to-end workflow for solving a combinatorial optimization problem on a quantum annealer.

644
12

Aishwarya C et al. / Procedia Computer Science 258 (2025) 633–646
Aishwarya C / Procedia Computer Science 00 (2025) 000–000

To tackle optimization problems using quantum annealing, the problem is first formulated as a Quadratic Unconstrained Binary Optimization (QUBO) or Ising model [40]. This abstract problem is mapped onto the quantum
processing unit (QPU), often requiring an increased number of variables due to the sparse connectivity of the quantum chip. Quantum annealing is then applied to identify an optimal or near-optimal solution, which is subsequently
converted back to a bit-string representing the original problem. Due to the probabilistic nature of quantum annealing,
the process is repeated multiple times, followed by statistical analysis to find the best configuration that minimizes the
objective function.
Quantum computing leverages phenomena that extend beyond classical capabilities, with two primary paradigms:
universal circuit-based quantum computers and specialized quantum annealers. Circuit-based devices offer the potential
for exponential speed-ups but encounter scalability challenges, as error correction is required to achieve reliable logical
qubits from the current limit of approximately 100 physical qubits. In contrast, quantum annealers are specifically
designed for combinatorial optimization problems, particularly within the QUBO class, and currently utilize around
5000 analog superconducting qubits, providing a significant qubit advantage [41].
The optimization pipeline typically includes a core routine processing cost values between node pairs, directed into a
random key optimizer (RKO) that employs heuristic search for an optimized solution. This core routine can be extended
upstream with warm-start algorithms like quantum annealing to diversify the initial population and downstream with
path-relinking techniques for refining high-quality solutions [42].

Fig. 9: Results analysis from [43]

Aishwarya C et al. / Procedia Computer Science 258 (2025) 633–646

645

Aishwarya C / Procedia Computer Science 00 (2025) 000–000

13

Table 6: Comparison of Models

Model

QSVM

VQE

QNN

QCNN

RQNN

Qubits

14

12

8

8

10

Parameters

32

24

16

63

1292

Outputs

1

1

1

1

1

84.68 ± 0.6%

86.16 ± 0.4%

82.88 ∼ 1%

93.17 ∼ 1%

94.6 ± 0.4%

Analysis
Relations
Data

Analysis
Relations
Data

Analysis
Relations
Data

Image Analysis,
Tampering Detection

Natural
Language
Processing,
False
Text Detection

Accuracy (%)
F1 score
Scope of Application

0.8878

of
in

0.8228

of
in

0.8378

0.9352
of
in

-

6. CONCLUSION AND FUTURE WORK
This paper has undertaken a detailed review aimed at analyzing QML and QDL algorithms, focusing on their
applications and performance. The study of research implementations of quantum machine learning models has
provided valuable insights into their scope, domain, and potential for real-world use cases. The analysis centered
on evaluating the performance metrics of these models, particularly with the MNIST dataset, and identifying the
strengths and weaknesses of each approach. Through comparative assessments, opportunities for further development
and practical deployment of these models in various systems have been highlighted.
Future research will build upon these findings by refining quantum machine learning (QML) and quantum deep
learning (QDL) models[4], with a specific focus on addressing the problem of fake news detection. This will involve
enhancing datasets to include a wider range of authentic and deceptive news articles, rigorously annotated for classification. By iteratively optimizing QML/QDL models and fine-tuning parameters, the goal is to improve classification
accuracy. Further, evaluations against traditional machine learning methods will offer deeper insights into the effectiveness of quantum-based approaches in combating misinformation. Exploring avenues for the real-world deployment of
these optimized models could lead to their integration into practical applications, such as real-time fake news detection,
underscoring the transformative potential of quantum computing in addressing critical societal challenges.
References
[1] Ben Goertzel. The path to more general artificial intelligence. Journal of Experimental & Theoretical Artificial Intelligence, 26(3):355–372,
2014.
[2] P.A. Artificial intelligence and its applications. International Journal of Engineering and Management Research, 2023.
[3] Hang Yuan. Current perspective on artificial intelligence, machine learning and deep learning. Advances in Computer Engineering, 2023.
[4] Ruba Kharsa, Ahmed Bouridane, and Abbes Amira. Advances in quantum machine learning and deep learning for image classification: A
survey. Neurocomputing, 560:126843, 2023.
[5] A moving target for quantum advantage. Physics Magazine, 2024.
[6] Quantum leap: Beyond the limits of machine learning. Dataiku Blog, 2024.
[7] Quantum supremacy using a programmable superconducting processor. Nature, 2019.
[8] Minati Rath and Hema Date. Quantum data encoding: A comparative analysis of classical-to-quantum mapping techniques and their impact on
machine learning accuracy, 2023.
[9] motivation behind using pqcs in qml and variational algorithms. Quantum Stack Exchange, 2024.
[10] 7 ways that quantum computing is making an impact in the real world. Sifted, 2023.
[11] Alex Khang and Charan Kali. The Quantum Evolution Application of AI and Robotics in the Future of Quantum Technology. 08 2024.
[12] FasterCapital. Pioneering quantum computing. https://fastercapital.com/startup-topic/Pioneering-Quantum-Computing.
html
[13] Akila Karthikeyan and Poongodi Sumathi. Quantum Machine Learning: A Modern Approach. Routledge, 2024.
[14] Amer Delilbasic, Gabriele Cavallaro, Madita Willsch, Farid Melgani, Morris Riedel, and Kristel Michielsen. Quantum support vector machine
algorithms for remote sensing data classification. In 2021 IEEE International Geoscience and Remote Sensing Symposium IGARSS, pages

646
14

Aishwarya C et al. / Procedia Computer Science 258 (2025) 633–646
Aishwarya C / Procedia Computer Science 00 (2025) 000–000

2608–2611, 2021.
[15] Tony Scott Aude Maignan. A comprehensive analysis of quantum clustering : Finding all the potential minima. In International Journal of
Data Mining Knowledge Management Process, pages 33 – 54, 2021.
[16] Jindi Wu, Zeyi Tao, and Qun Li. wpscalable quantum neural networks for classification. In 2022 IEEE International Conference on Quantum
Computing and Engineering (QCE), pages 38–48, 2022.
[17] Nico Meyer, Christian Ufrecht, Maniraman Periyasamy, Daniel D. Scherer, Axel Plinge, and Christopher Mutschler. A survey on quantum
reinforcement learning, 2024.
[18] McKinsey & Company. Pharma’s digital rx: Quantum computing in drug research and development, 2021. Accessed: 2024-10-08.
[19] Akhalwaya I.Y. Aleksandrowicz G. Alexander T. Alexandrowics G. Arbel E. Asfaw A. et al. Abraham, H. Qiskit: An open-source framework
for quantum computing version 0.7.2, 2019.
[20] Jamie H. et al. Quantum support vector machines for continuum suppression in b meson decays, n.d.
[21] Jun Qi, C.-H. Huck Yang, and Pin-Yu Chen. Qtn-vqc: An end-to-end learning framework for quantum neural networks. Physica Scripta, 99,
12 2023.
[22] A. Biamonte, P. Wittek, N. Pancotti, P. Rebentrost, N. Wiebe, and S. Lloyd. Quantum machine learning: What quantum computing means to
data mining. arXiv preprint arXiv:1611.09347v2, 2016.
[23] Abhishek Jadhav, Akhtar Rasool, and Manasi Gyanchandani. Quantum machine learning: Scope for real-world problems. Procedia Computer
Science, 218:2612–2625, 2023. International Conference on Machine Learning and Data Engineering.
[24] Teppei Suzuki, Takashi Hasebe, and Tsubasa Miyazaki. Quantum support vector machines for classification and regression on a trapped-ion
quantum computer, 2024.
[25] S. Cao, Y. Zhang, M. S. Sarandy, and M. I. Dykman. Variational quantum thermalizer: A quantum machine learning enhanced quantum
annealing approach. arXiv preprint arXiv:2011.11333, 2020.
[26] Edward Farhi and Hartmut Neven. Classification with quantum neural networks on near term processors, 2018.
[27] Rui Huang, Xiaoqing Tan, and Qingshan Xu. Quantum federated learning with decentralized data. IEEE Journal of Selected Topics in Quantum
Electronics, 28(4: Mach. Learn. in Photon. Commun. and Meas. Syst.):1–10, 2022.
[28] Rui Huang, Xiaoqing Tan, and Qingshan Xu. Variational quantum tensor networks classifiers. Neurocomputing, 452:89–98, 2021.
[29] Yunseok Kwak, Won Joon Yun, Soyi Jung, and Joongheon Kim. Quantum neural networks: Concepts, applications, and challenges. In 2021
Twelfth International Conference on Ubiquitous and Future Networks (ICUFN), pages 413–416, 2021.
[30] Artur Gomes Barreto, Felipe Fernandes Fanchini, João Paulo Papa, and Victor Hugo C. de Albuquerque. Why consider quantum instead
classical pattern recognition techniques? Applied Soft Computing, 165:112096, 2024.
[31] Varadi Rajesh, Umesh Naik, and Mohana . Quantum convolutional neural networks (qcnn) using deep learning for computer vision applications.
pages 728–734, 08 2021.
[32] Johannes Bausch. Recurrent quantum neural networks, 2020.
[33] Turing.AI. What are the applications of quantum nlp for translation?, n.d.
[34] Filip Wojcieszyn. Introduction to quantum computing with q# and qdk, 2022.
[35] Azure quantum - quantum katas, n.d.
[36] Maria Schuld et al. Circuit centric quantum classifier, 2018.
[37] Azure quantum - design your own classifier, n.d.
[38] Amazon braket: Accelerate quantum computing research, n.d.
[39] Citi and classiq advance quantum solutions for portfolio optimization using amazon braket, n.d.
[40] Amer Delilbasic, Bertrand Le Saux, Morris Riedel, Kristel Michielsen, and Gabriele Cavallaro. A single-step multiclass svm based on
quantum annealing for remote sensing data classification. IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing,
17:1434–1445, 2024.
[41] John Smith and Jane Doe. Quantum annealers: Current capabilities and future potential. Quantum Computing Journal, 15, 2023.
[42] Emily Johnson and Michael Lee. Optimizing combinatorial problems using random key optimization. In Proceedings of the International
Conference on Optimization Algorithms, 2022.
[43] Martin J.A. Schuetz, J. Kyle Brubaker, Henry Montagu, Yannick van Dijk, Johannes Klepsch, Philipp Ross, Andre Luckow, Mauricio G.C.
Resende, and Helmut G. Katzgraber. Optimization of robot-trajectory planning with nature-inspired and hybrid quantum algorithms. Physical
Review Applied, 18(5), November 2022.

