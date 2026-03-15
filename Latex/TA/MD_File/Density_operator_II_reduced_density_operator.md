# Reduced Density Operator

**Masatsugu Sei Suzuki**  
Department of Physics, SUNY at Binghamton  
_(Date: October 29, 2020)_

Here we discuss the density operator for the two and three-particles system. The concept of the reduced density operator is significant. The reduced density operator enables one to obtain expectation values of one subsystem 1's observables without bothering about the states of the other subsystem 2. It is formed from the density operator of the entire system by taking the partial trace over the states of subsystem 2.

---

## 1. Kronecker Product

A classical bit of information is represented by a system that can be in either of two states, 0, 1. At the quantum mechanical level, the most natural candidate for replacing a classical bit is the state of a two-level system, whose basic components may be written as:

$$|0\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \quad |1\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$$

This is the so-called quantum bit of information, or, in short, a **qubit**. We define the combined state of two qubits as:

$$|\psi_1\rangle \otimes |\psi_2\rangle = \text{KroneckerProduct}[|\psi_1\rangle, |\psi_2\rangle]$$

Then we have:

$$|0\rangle|0\rangle = \begin{pmatrix}1\\0\\0\\0\end{pmatrix}, \quad |0\rangle|1\rangle = \begin{pmatrix}0\\1\\0\\0\end{pmatrix}, \quad |1\rangle|0\rangle = \begin{pmatrix}0\\0\\1\\0\end{pmatrix}, \quad |1\rangle|1\rangle = \begin{pmatrix}0\\0\\0\\1\end{pmatrix}$$

And the outer products:

$$|0\rangle\langle0| \otimes |0\rangle\langle0| = \begin{pmatrix}1&0&0&0\\0&0&0&0\\0&0&0&0\\0&0&0&0\end{pmatrix}, \quad |0\rangle\langle0| \otimes |1\rangle\langle1| = \begin{pmatrix}0&0&0&0\\0&1&0&0\\0&0&0&0\\0&0&0&0\end{pmatrix}$$

$$|1\rangle\langle1| \otimes |0\rangle\langle0| = \begin{pmatrix}0&0&0&0\\0&0&0&0\\0&0&1&0\\0&0&0&0\end{pmatrix}, \quad |1\rangle\langle1| \otimes |1\rangle\langle1| = \begin{pmatrix}0&0&0&0\\0&0&0&0\\0&0&0&0\\0&0&0&1\end{pmatrix}$$

---

## 2. Calculation of Density Operator by Mathematica

A classical bit of information is represented by a system that can be in either of two states, 0, 1. At the quantum mechanical level, the most natural candidate for replacing a classical bit is the state of a two-level system, whose basic components may be written as:

$$|0\rangle = \begin{pmatrix} 1 \ 0 \end{pmatrix}, \quad |1\rangle = \begin{pmatrix} 0 \ 1 \end{pmatrix}$$

This is the so-called quantum bit of information, or, in short, a **qubit**.

The Kronecker product:

$$|\psi_1\rangle \otimes |\psi_2\rangle = \text{KroneckerProduct}[|\psi_1\rangle, |\psi_2\rangle]$$

Then we have (same results as Section 1 above).

---

## 3. Density Operators for Two-Particle System

We consider the two-particle system. A typical example is the two-spin system with spin 1/2. There are four states:

$$|\uparrow_z, \uparrow_z\rangle_{12} = |\uparrow_z\rangle_1 \otimes |\uparrow_z\rangle_2, \quad |\uparrow_z, \downarrow_z\rangle_{12} = |\uparrow_z\rangle_1 \otimes |\downarrow_z\rangle_2$$

$$|\downarrow_z, \uparrow_z\rangle_{12} = |\downarrow_z\rangle_1 \otimes |\uparrow_z\rangle_2, \quad |\downarrow_z, \downarrow_z\rangle_{12} = |\downarrow_z\rangle_1 \otimes |\downarrow_z\rangle_2$$

In general, the density operator for a two-particle system can be expressed by:

$$\hat{\rho} = \sum_{i,j,k,l} \langle i,j|\hat{\rho}|k,l\rangle , (|\phi_i\rangle\langle\phi_k|) \otimes (|\chi_j\rangle\langle\chi_l|)$$

where $|\phi_i\rangle$ is the eigenket of particle 1 and $|\chi_j\rangle$ is the eigenket of particle 2. Here we use the formula:

$$\text{Tr}_1[(|\phi_i\rangle\langle\phi_k|) \otimes (|\chi_j\rangle\langle\chi_l|)] = \langle\phi_k|\phi_i\rangle , |\chi_j\rangle\langle\chi_l| = \delta_{ki} , |\chi_j\rangle\langle\chi_l|$$

$$\text{Tr}_2[(|\phi_i\rangle\langle\phi_k|) \otimes (|\chi_j\rangle\langle\chi_l|)] = \langle\chi_l|\chi_j\rangle , |\phi_i\rangle\langle\phi_k| = \delta_{lj} , |\phi_i\rangle\langle\phi_k|$$

---

## 4. Reduced Density Operator $\hat{\rho}_1$

The reduced density operator $\hat{\rho}_1$ describes completely all the properties/outcomes of measurements of the system 1, given that system 2 is left unobserved ("tracing out" system 2). This represents the maximum information which is available about the particle 1 alone, irrespective of the state of particle 2.

The reduced density operator $\hat{\rho}_1$ is defined as:

$$\hat{\rho}_1 = \text{Tr}_2[\hat{\rho}_{12}] = \sum_{i,k} \langle i|\hat{\rho}|k\rangle , |\phi_i\rangle\langle\phi_k|$$

where we use the formula $\text{Tr}_2[(|\chi_j\rangle\langle\chi_l|)] = \langle\chi_l|\chi_j\rangle = \delta_{jl}$.

For the two-particle system, using the shorthand notation $|1,1\rangle \equiv 1$, $|1,2\rangle \equiv 2$, $|2,1\rangle \equiv 3$, $|2,2\rangle \equiv 4$:

$$\hat{\rho}_1 = \text{Tr}_2[\hat{\rho}] = \begin{pmatrix} \hat{\rho}_{11} & \hat{\rho}_{13} \ \hat{\rho}_{31} & \hat{\rho}_{33} \end{pmatrix} + \begin{pmatrix} \hat{\rho}_{22} & \hat{\rho}_{24} \ \hat{\rho}_{42} & \hat{\rho}_{44} \end{pmatrix}$$

---

## 5. Reduced Density Operator $\hat{\rho}_2$

The reduced density operator $\hat{\rho}_2$ describes completely all the properties/outcomes of measurements of the system 2, given that system 1 is left unobserved ("tracing out" system 1). This represents the maximum information which is available about the particle 2 alone, irrespective of the state of particle 1.

The reduced density operator $\hat{\rho}_2$ is defined by:

$$\hat{\rho}_2 = \text{Tr}_1[\hat{\rho}_{12}] = \sum_{i,j,l} \langle i,j|\hat{\rho}|i,l\rangle , |\chi_j\rangle\langle\chi_l|$$

For the two-particle system:

$$\hat{\rho}_2 = \text{Tr}_1[\hat{\rho}] = \begin{pmatrix} \hat{\rho}_{11} & \hat{\rho}_{12} \ \hat{\rho}_{21} & \hat{\rho}_{22} \end{pmatrix} + \begin{pmatrix} \hat{\rho}_{33} & \hat{\rho}_{34} \ \hat{\rho}_{43} & \hat{\rho}_{44} \end{pmatrix}$$

---

## 6. Example 1: Two Spins (Independent Subsystems)

We consider the state of the composite system 1-2 consisting of independent subsystems:

$$|\psi_{12}\rangle = \frac{1}{\sqrt{2}}\left(|{+z},1\rangle + |{-z},1\rangle\right) \otimes |{+z},2\rangle = |{+x},1\rangle \otimes |{+z},2\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix}1\\0\\1\\0\end{pmatrix}$$

The density operator is:

$$\hat{\rho}_{12} = |\psi_{12}\rangle\langle\psi_{12}| = (|{+x},1\rangle \otimes |{+z},2\rangle)(\langle{+x},1| \otimes \langle{+z},2|) = \hat{\rho}_A \otimes \hat{\rho}_B$$

The matrix form of $\hat{\rho}_{12}$ is:

$$\hat{\rho}_{12} = \frac{1}{2}\begin{pmatrix}1&0&1&0\\0&0&0&0\\1&0&1&0\\0&0&0&0\end{pmatrix}$$

The reduced density operators are:

$$\hat{\rho}_1 = \text{Tr}_2[\hat{\rho}_{12}] = \frac{1}{2}\begin{pmatrix}1&1\\1&1\end{pmatrix} = \hat{\rho}_A$$

$$\hat{\rho}_2 = \text{Tr}_1[\hat{\rho}_{12}] = \frac{1}{2}\begin{pmatrix}1&0\\0&1\end{pmatrix} \cdot 2 \cdot \frac{1}{2} = \begin{pmatrix}1&0\\0&0\end{pmatrix} = \hat{\rho}_B$$

Note that $\hat{\rho}_1 = \text{Tr}_2[\hat{\rho}_A \otimes \hat{\rho}_B] = \hat{\rho}_A \text{Tr}[\hat{\rho}_B] = \hat{\rho}_A$ and $\hat{\rho}_2 = \hat{\rho}_B$.

---

## 7. Example 2: Two Spins — Independent Subsystems

We start with the two-particle pure state $|\psi_{12}\rangle = |\uparrow_z,1\rangle|\uparrow_z,2\rangle$. The density operator is:

$$\hat{\rho}_{12} = |\uparrow_z,1;\uparrow_z,2\rangle\langle\uparrow_z,1;\uparrow_z,2| = \hat{\rho}_A \otimes \hat{\rho}_B = \begin{pmatrix}1&0&0&0\\0&0&0&0\\0&0&0&0\\0&0&0&0\end{pmatrix}$$

where $\hat{\rho}_A = \begin{pmatrix}1&0\\0&0\end{pmatrix}$, $\hat{\rho}_B = \begin{pmatrix}1&0\\0&0\end{pmatrix}$.

The reduced density operators (under the basis ${|\uparrow\rangle, |\downarrow\rangle}$):

$$\hat{\rho}_1 = \text{Tr}_2[\hat{\rho}_{12}] = \begin{pmatrix}1&0\\0&0\end{pmatrix} = \hat{\rho}_A, \quad \hat{\rho}_2 = \text{Tr}_1[\hat{\rho}_{12}] = \begin{pmatrix}1&0\\0&0\end{pmatrix} = \hat{\rho}_B$$

---

## 8. Example 3: Bell's Two-Particle Entangled State

The Bell's entangled state is given by:

$$|\psi_{12}^{(-)}\rangle = \frac{1}{\sqrt{2}}\left(|\uparrow_z,1;\downarrow_z,2\rangle - |\downarrow_z,1;\uparrow_z,2\rangle\right)$$

The density operator (pure state) is:

$$\hat{\rho}_{12}^{(-)} = |\psi_{12}^{(-)}\rangle\langle\psi_{12}^{(-)}| = \frac{1}{2}\begin{pmatrix}0&0&0&0\\0&1&-1&0\\0&-1&1&0\\0&0&0&0\end{pmatrix}$$

The reduced density operators are:

$$\hat{\rho}_1 = \text{Tr}_2[\hat{\rho}_{12}^{(-)}] = \frac{1}{2}\begin{pmatrix}1&0\\0&1\end{pmatrix}, \quad \hat{\rho}_2 = \text{Tr}_1[\hat{\rho}_{12}^{(-)}] = \frac{1}{2}\begin{pmatrix}1&0\\0&1\end{pmatrix}$$

under the basis ${|\uparrow_z\rangle, |\downarrow_z\rangle}$. Thus for measurements of particle 1 (or 2), the Bell's state behaves like the mixed state of a completely un-polarized ensemble.

> **Note (Nielsen & Chuang):** The state $\hat{\rho}_1$ (or $\hat{\rho}_2$) is a mixed state. This is a quite remarkable result. The state of the joint system of two qubits is a pure state — it is known exactly — however, the first qubit is in a mixed state, about which we apparently do not have maximal knowledge. This strange property, that the joint state of a system can be completely known, yet a subsystem be in the mixed state, is another hallmark of **quantum entanglement**.

---

## 9. Density Operator for Three-Spins System

In general, the density operator for a three-particle system can be expressed by:

$$\hat{\rho}_{123} = \sum_{i,j,k,l,m,n} \langle i,j,k|\hat{\rho}|l,m,n\rangle , (|\phi_i\rangle\langle\phi_l|) \otimes (|\chi_j\rangle\langle\chi_m|) \otimes (|\xi_k\rangle\langle\xi_n|)$$

where $|\phi_i\rangle$ is the eigenket of particle 1, $|\chi_j\rangle$ is the eigenket of particle 2, and $|\xi_k\rangle$ is the eigenket of particle 3.

The density matrix for the three-spins system (spin-1/2) is an $8 \times 8$ matrix:

$$\hat{\rho}_{123} = \begin{pmatrix} \rho_{11} & \rho_{12} & \cdots & \rho_{18} \ \rho_{21} & \rho_{22} & \cdots & \rho_{28} \ \vdots & & \ddots & \vdots \ \rho_{81} & \rho_{82} & \cdots & \rho_{88} \end{pmatrix}$$

where the basis labeling is: $|{+++}\rangle \equiv 1$, $|{++-}\rangle \equiv 2$, $|{+-+}\rangle \equiv 3$, $|{+--}\rangle \equiv 4$, $|{-++}\rangle \equiv 5$, $|{-+-}\rangle \equiv 6$, $|{--+}\rangle \equiv 7$, $|{---}\rangle \equiv 8$.

---

## 10. Reduced Density Operators (Three-Particle System)

**Reduced density operator $\hat{\rho}_{23}$** (trace over particle 1):

$$\hat{\rho}_{23} = \text{Tr}_1[\hat{\rho}_{123}] = \begin{pmatrix}\rho_{11}&\rho_{12}&\rho_{13}&\rho_{14}\\rho_{21}&\rho_{22}&\rho_{23}&\rho_{24}\\rho_{31}&\rho_{32}&\rho_{33}&\rho_{34}\\rho_{41}&\rho_{42}&\rho_{43}&\rho_{44}\end{pmatrix} + \begin{pmatrix}\rho_{55}&\rho_{56}&\rho_{57}&\rho_{58}\\rho_{65}&\rho_{66}&\rho_{67}&\rho_{68}\\rho_{75}&\rho_{76}&\rho_{77}&\rho_{78}\\rho_{85}&\rho_{86}&\rho_{87}&\rho_{88}\end{pmatrix}$$

**Reduced density operator $\hat{\rho}_{13}$** (trace over particle 2):

$$\hat{\rho}_{13} = \text{Tr}_2[\hat{\rho}_{123}] = \begin{pmatrix}\rho_{11}&\rho_{12}&\rho_{15}&\rho_{16}\\rho_{21}&\rho_{22}&\rho_{25}&\rho_{26}\\rho_{51}&\rho_{52}&\rho_{55}&\rho_{56}\\rho_{61}&\rho_{62}&\rho_{65}&\rho_{66}\end{pmatrix} + \begin{pmatrix}\rho_{33}&\rho_{34}&\rho_{37}&\rho_{38}\\rho_{43}&\rho_{44}&\rho_{47}&\rho_{48}\\rho_{73}&\rho_{74}&\rho_{77}&\rho_{78}\\rho_{83}&\rho_{84}&\rho_{87}&\rho_{88}\end{pmatrix}$$

**Reduced density operator $\hat{\rho}_{12}$** (trace over particle 3):

$$\hat{\rho}_{12} = \text{Tr}_3[\hat{\rho}_{123}] = \begin{pmatrix}\rho_{11}&\rho_{13}&\rho_{15}&\rho_{17}\\rho_{31}&\rho_{33}&\rho_{35}&\rho_{37}\\rho_{51}&\rho_{53}&\rho_{55}&\rho_{57}\\rho_{71}&\rho_{73}&\rho_{75}&\rho_{77}\end{pmatrix} + \begin{pmatrix}\rho_{22}&\rho_{24}&\rho_{26}&\rho_{28}\\rho_{42}&\rho_{44}&\rho_{46}&\rho_{48}\\rho_{62}&\rho_{64}&\rho_{66}&\rho_{68}\\rho_{82}&\rho_{84}&\rho_{86}&\rho_{88}\end{pmatrix}$$

**Reduced density operator $\hat{\rho}_3$** (trace over particles 1 and 2):

$$\hat{\rho}_3 = \text{Tr}_{12}[\hat{\rho}_{123}] = \text{Tr}_2[\hat{\rho}_{23}] = \begin{pmatrix}\rho_{11}+\rho_{22}\\\rho_{33}+\rho_{44}\end{pmatrix} \to \frac{1}{2}\begin{pmatrix}1&0\\0&1\end{pmatrix} \quad \text{(for GHZ)}$$

---

## 11. Example 1: Entangled GHZ State

$$|\psi_{GHZ}^{(+)}\rangle = \frac{1}{\sqrt{2}}\left[|{+++}\rangle + |{---}\rangle\right]$$

The density operator is defined by $\hat{\rho}_{123} = |\psi_{GHZ}^{(+)}\rangle\langle\psi_{GHZ}^{(+)}|$, which gives an $8\times8$ matrix with $\frac{1}{2}$ in the $(1,1)$, $(1,8)$, $(8,1)$, and $(8,8)$ positions, and zeros elsewhere.

The reduced density operators are:

$$\hat{\rho}_{23} = \text{Tr}_1[\hat{\rho}_{123}] = \frac{1}{2}\begin{pmatrix}1&0&0&0\\0&0&0&0\\0&0&0&0\\0&0&0&1\end{pmatrix}$$

$$\hat{\rho}_3 = \text{Tr}_{12}[\hat{\rho}_{123}] = \frac{1}{2}\begin{pmatrix}1&0\\0&1\end{pmatrix}$$

which is equivalent to a completely un-polarized state.

---

## 12. Example 2: Another Entangled GHZ State

$$|\psi_{GHZ}^{(-)}\rangle = \frac{1}{\sqrt{2}}\left[|{+++}\rangle - |{---}\rangle\right]$$

The density operator is $\hat{\rho}_{123} = |\psi_{GHZ}^{(-)}\rangle\langle\psi_{GHZ}^{(-)}|$, which gives an $8 \times 8$ matrix with $\frac{1}{2}$ at $(1,1)$, $-\frac{1}{2}$ at $(1,8)$, $-\frac{1}{2}$ at $(8,1)$, and $\frac{1}{2}$ at $(8,8)$.

The reduced density operators are:

$$\hat{\rho}_{23} = \text{Tr}_1[\hat{\rho}_{123}] = \frac{1}{2}\begin{pmatrix}1&0&0&0\\0&0&0&0\\0&0&0&0\\0&0&0&1\end{pmatrix}$$

$$\hat{\rho}_3 = \text{Tr}_{12}[\rho_{123}] = \frac{1}{2}\begin{pmatrix}1&0\\0&1\end{pmatrix}$$

which is equivalent to a completely un-polarized state.

---

## 13. Origin of the Collapse of the State Vector

The collapse postulate states that upon measurement a system evolves from a pure state to a mixed state.

If we are in a state $|\psi\rangle$ and we measure $A$, we end up in an eigenstate $|a\rangle$ with probability $|\langle a|\psi\rangle|^2$. That is, the pure state $|\psi\rangle$ evolves to a mixed state:

$$\hat{\rho} = \sum_a |\langle a|\psi\rangle|^2 |a\rangle\langle a|$$

This puzzle is resolved if we keep track of entanglements. Let:

- $|\psi\rangle$ = the state of the system
- $|E\rangle$ = the state of the measuring apparatus

Measurement: $|a\rangle|E\rangle \to |a\rangle|E_a\rangle$, where $|E_a\rangle$ is the state of the apparatus after measuring $a$.

If $|\psi\rangle = \sum_a \alpha_a |a\rangle$, then by linearity:

$$|\psi\rangle|E\rangle \to \sum_a \alpha_a |a\rangle|E_a\rangle$$

If we do not wish to study the state of our apparatus, we trace over $\mathcal{H}_E$:

$$\hat{\rho} = \text{Tr}_E\left[\sum_{a,a'} \alpha_a \alpha_{a'}^* |a\rangle\langle a'| \otimes |E_a\rangle\langle E_{a'}|\right] = \sum_a |\alpha_a|^2 |a\rangle\langle a|$$

using $\langle E_{a'}|E_a\rangle = \delta_{aa'}$. The state vector appears to collapse through a purely unitary mechanism. The assumption $\langle E_a|E_{a'}\rangle = \delta_{aa'}$ is the statement that $E$ is classical.

---

## 14. Schrödinger's Cat

### 14.1 Bipartite Quantum System

We consider the state vector in the $A \otimes B$ system. System $A$ is accessible, while system $B$ is inaccessible:

$$|\psi_{AB}\rangle = a|0\rangle_A|0\rangle_B + b|1\rangle_A|1\rangle_B = \begin{pmatrix}a\\0\\0\\b\end{pmatrix}$$

where $|a|^2 + |b|^2 = 1$.

With probability $|a|^2$, measuring system $A$ gives $|0\rangle_A$, collapsing to $|0\rangle_A|0\rangle_B$. With probability $|b|^2$, the outcome is $|1\rangle_A$, collapsing to $|1\rangle_A|1\rangle_B$.

The density operator for the combined system $AB$ is:

$$\hat{\rho}_{AB} = |\psi_{AB}\rangle\langle\psi_{AB}| = |a|^2|0\rangle_A\langle0|\otimes|0\rangle_B\langle0| + ab^*|0\rangle_A\langle1|\otimes|0\rangle_B\langle1| + a^*b|1\rangle_A\langle0|\otimes|1\rangle_B\langle0| + |b|^2|1\rangle_A\langle1|\otimes|1\rangle_B\langle1|$$

### 14.2 Reduced Operator

The reduced density operator $\hat{\rho}_A$ is obtained by tracing over subsystem $B$:

$$\hat{\rho}_A = \text{Tr}_B[|\psi_{AB}\rangle\langle\psi_{AB}|] = |a|^2|0\rangle_A\langle0| + |b|^2|1\rangle_A\langle1| = \begin{pmatrix}|a|^2&0\\0&|b|^2\end{pmatrix}$$

We can verify that $\hat{\rho}_A = \hat{\rho}_B$.

The entanglement destroys the coherence of a superposition of states of $A$, so that some of the phase in the superposition becomes inaccessible if we look at $A$ alone.

### 14.3 Gedanken Experiment (Schrödinger's Cat)

The Schrödinger cat paradox is a _gedanken_ experiment designed by Schrödinger to illustrate problems of quantum measurement. The apparatus consists of a radioactive nucleus, a Geiger counter, a hammer, a bottle of cyanide gas, a cat, and a box. The nucleus has a 50% probability of decaying in one hour.

**(Schrödinger, 1935):** One can even set up quite ridiculous cases. A cat is penned up in a steel chamber, along with the following device (which must be secured against direct interference by the cat): in a Geiger counter there is a tiny bit of radioactive substance, so small, that perhaps in the course of the hour one of the atoms decays, but also, with equal probability, perhaps none; if it happens, the counter tube discharges and through a relay releases a hammer which shatters a small flask of hydrocyanic acid. [...] The psi-function of the entire system would express this by having in it the living and dead cat (pardon the expression) mixed or smeared out in equal parts. _(E. Schrödinger, November 1935)_

The quantum state of the combined system after one hour:

$$|\psi_{AB}\rangle = \frac{1}{\sqrt{2}}\left[|0\rangle_A|0\rangle_B + |1\rangle_A|1\rangle_B\right]$$

where $|0\rangle_A = |\text{cat alive}\rangle$, $|1\rangle_A = |\text{cat dead}\rangle$, $|0\rangle_B = |\text{no decay}\rangle$, $|1\rangle_B = |\text{decay}\rangle$.

The reduced density operator for the cat (system $A$) is:

$$\hat{\rho}_A = \text{Tr}_B[|\psi_{AB}\rangle\langle\psi_{AB}|] = \frac{1}{2}\begin{pmatrix}1&0\\0&1\end{pmatrix} = \frac{1}{2}\hat{I}_A$$

**Maximally entangled state:** When $\hat{\rho}_A = \frac{1}{2}\hat{I}$, measuring spin $A$ along any axis gives a completely random result (up or down each with probability 1/2).

---

## 15. Quantum Teleportation

We consider the pure particle state $|\psi_{123}\rangle$ related to quantum teleportation. The density operator is $\hat{\rho}_{123} = |\psi_{123}\rangle\langle\psi_{123}|$, where:

$$|\psi_{123}\rangle = \frac{1}{2}|\psi_{12}^{(-)}\rangle[-a|{+z}\rangle_3 - b|{-z}\rangle_3] + \frac{1}{2}|\psi_{12}^{(+)}\rangle[-a|{+z}\rangle_3 + b|{-z}\rangle_3]$$ $$+ \frac{1}{2}|\Phi_{12}^{(-)}\rangle[a|{-z}\rangle_3 + b|{+z}\rangle_3] + \frac{1}{2}|\Phi_{12}^{(+)}\rangle[a|{-z}\rangle_3 - b|{+z}\rangle_3]$$

with:

$$|\psi_{12}^{(\pm)}\rangle = \frac{1}{\sqrt{2}}\left[|{+z}\rangle_1|{-z}\rangle_2 \pm |{-z}\rangle_1|{+z}\rangle_2\right] = \frac{1}{\sqrt{2}}\begin{pmatrix}0\\1\\\pm1\\0\end{pmatrix}$$

$$|\Phi_{12}^{(\pm)}\rangle = \frac{1}{\sqrt{2}}\left[|{+z}\rangle_1|{+z}\rangle_2 \pm |{-z}\rangle_1|{-z}\rangle_2\right] = \frac{1}{\sqrt{2}}\begin{pmatrix}1\\0\\0\\\pm1\end{pmatrix}$$

with $|a|^2 + |b|^2 = 1$.

Tracing out particle 1, then particle 2:

$$\hat{\rho}_3 = \text{Tr}_{12}[\hat{\rho}_{123}] = \frac{1}{2}\begin{pmatrix}1&0\\0&1\end{pmatrix}$$

This is equivalent to a completely un-polarized state, so Bob (particle 3) has no information about Alice's state before receiving the result of the Bell state measurement.

---

## 16. Average $\langle\hat{X}_1\rangle$

We consider the average value of an operator $\hat{X}_1$ that acts only on system 1 in a global density operator $\hat{\rho}$ for particles 1 and 2:

$$\langle\hat{X}_1\rangle = \text{Tr}_{12}[(\hat{X}_1 \otimes \hat{I}_2)\hat{\rho}_{12}] = \text{Tr}_1[\hat{X}_1 \text{Tr}_2 \hat{\rho}_{12}] = \text{Tr}_1[\hat{X}_1\hat{\rho}_1]$$

where $\hat{\rho}_1 = \text{Tr}_2\hat{\rho}$.

Since $\hat{\rho}_{12} = \hat{\rho}_1 \otimes \hat{\rho}_2$:

$$\langle\hat{X}_1\rangle = \text{Tr}[\hat{X}_1\hat{\rho}_1\hat{I}_2\hat{\rho}_2] = \text{Tr}_1[\hat{X}_1\hat{\rho}_1]\text{Tr}_2[\hat{I}_2\hat{\rho}_2] = \text{Tr}_1[\hat{X}_1\hat{\rho}_1]$$

and $\hat{\rho}_1 = \text{Tr}_2[\hat{\rho}_1 \otimes \hat{\rho}_2] = \hat{\rho}_1 \text{Tr}_2[\hat{\rho}_2] = \hat{\rho}_1$.

---

## 17. Schmidt Decomposition

**Theorem:** Suppose $|\psi\rangle$ is a pure state of a bipartite composite system $A \otimes B$. Then there exist orthonormal states $|i\rangle_A$ for system $A$, and $|i\rangle_B$ for system $B$, such that:

$$|\psi\rangle = \sum_i \sqrt{p_i}, |i\rangle_A|i\rangle_B$$

where $\sqrt{p_i}$ are the **Schmidt coefficients** (non-negative real numbers) satisfying $\sum_i p_i = 1$. Note that $\text{Tr}[\hat{\rho}^2] = \sum_i p_i^2$.

The state is a pure state if and only if there is only one nonzero Schmidt coefficient ($p_i = 1$ for exactly one $i$).

For a two-qubit state $|\psi\rangle = \sum_{i,j} C_{ij}|a_i\rangle|b_j\rangle$, the Schmidt coefficients are the eigenvalues of $\hat{C}\hat{C}^\dagger$.

**Examples:**

|State|$\hat{C}$|Eigenvalues of $\hat{C}\hat{C}^\dagger$|Type|
|---|---|---|---|
|$\frac{1}{\sqrt{2}}(\|00\rangle + \|01\rangle)$|$\frac{1}{\sqrt{2}}\begin{pmatrix}1&1\\0&0\end{pmatrix}$|$p_1=1, p_2=0$|**Product state**|
|$\frac{1}{\sqrt{2}}(\|00\rangle + \|11\rangle)$|$\frac{1}{\sqrt{2}}\begin{pmatrix}1&0\\0&1\end{pmatrix}$|$p_1=p_2=\frac{1}{2}$|**Entangled**|
|$\frac{1}{\sqrt{2}}(\|01\rangle + \|10\rangle)$|$\frac{1}{\sqrt{2}}\begin{pmatrix}0&1\\1&0\end{pmatrix}$|$p_1=p_2=\frac{1}{2}$|**Entangled**|
|$\frac{1}{\sqrt{3}}(\|00\rangle+\|01\rangle+\|11\rangle)$|$\frac{1}{\sqrt{3}}\begin{pmatrix}1&1\\0&1\end{pmatrix}$|$p_1\approx0.873$, $p_2\approx0.127$|**Entangled**|
|$\frac{1}{2}(\|00\rangle+\|01\rangle+\|10\rangle+\|11\rangle)$|$\frac{1}{2}\begin{pmatrix}1&1\\1&1\end{pmatrix}$|$p_1=1, p_2=0$|**Product state**|

---

## 18. Schmidt Decomposition Application

Given the Schmidt decomposition $|\psi\rangle = \sum_i \sqrt{p_i},|i\rangle_A|i\rangle_B$, the density operator is:

$$\hat{\rho} = \sum_{i,j} \sqrt{p_i p_j},|i\rangle_A\langle j|\otimes|i\rangle_B\langle j|$$

The reduced density operators are:

$$\text{Tr}_B(\hat{\rho}) = \sum_i p_i |i\rangle_A\langle i|, \quad \text{Tr}_A(\hat{\rho}) = \sum_i p_i |i\rangle_B\langle i|$$

The spectrum (set of eigenvalues) of both reduced density operators is the same.

---

## 19. Purification

Suppose we are given a state $\hat{\rho}_A$ of a quantum system $A$. It is possible to introduce an additional (fictitious reference) system $R$ (same dimension as $A$) and define a pure state $|AR\rangle$ for the joint system $AR$ such that:

$$\hat{\rho}_A = \text{Tr}_R\left[|AR\rangle\langle AR|\right]$$

**Construction:** If $\hat{\rho}_A = \sum_i p_i |i\rangle_A\langle i|$ (mixed state), define:

$$|AR\rangle = \sum_i \sqrt{p_i},|i\rangle_A|i\rangle_R \quad \text{(pure state)}$$

Then $\text{Tr}_R[|AR\rangle\langle AR|] = \sum_i p_i |i\rangle_A\langle i| = \hat{\rho}_A$.

The Schmidt basis for system $A$ in the purification is the basis in which the mixed state is diagonal, with Schmidt coefficients being the square roots of the eigenvalues.

---

## 20. Example 1

Given the density operator:

$$\hat{\rho} = \frac{1}{2}\left[|\uparrow_z\rangle\langle\uparrow_z| + |\uparrow_z\rangle\langle\downarrow_z| + |\downarrow_z\rangle\langle\uparrow_z| + |\downarrow_z\rangle\langle\downarrow_z|\right] = \frac{1}{2}\begin{pmatrix}1&1\\1&1\end{pmatrix}$$

We have:

$$\text{Tr}[\hat{\rho}^2] = \text{Tr}\left[\frac{1}{4}\begin{pmatrix}2&2\\2&2\end{pmatrix}\right] = 1 \quad \Rightarrow \text{pure state}$$

$$\langle S_x \rangle = \text{Tr}[\hat{S}_x\hat{\rho}] = \frac{\hbar}{2}$$

---

## 21. Example 2

Show that:

$$\frac{1}{2}\left[|\uparrow_n\rangle\langle\uparrow_n| + |\downarrow_n\rangle\langle\downarrow_n|\right] = \frac{1}{2}\left[|\uparrow_z\rangle\langle\uparrow_z| + |\downarrow_z\rangle\langle\downarrow_z|\right]$$

where:

$$|\uparrow_n\rangle = \begin{pmatrix}\cos(\theta/2)\\sin(\theta/2)e^{i\phi}\end{pmatrix}, \quad |\downarrow_n\rangle = \begin{pmatrix}-\sin(\theta/2)\\ \cos(\theta/2)e^{i\phi}\end{pmatrix}$$

**(Solution):**

$$\hat{\rho}_z = \frac{1}{2}\begin{pmatrix}0&1\\1&0\end{pmatrix} = \frac{1}{2}\hat{I}, \quad \hat{\rho}_n = \frac{1}{2}\begin{pmatrix}1&0\\0&1\end{pmatrix} = \frac{1}{2}\hat{I}$$

Then $\hat{\rho}_z = \hat{\rho}_n$, and $\text{Tr}[\hat{\rho}^2] = \frac{1}{2}$ (mixed state).

---

## 22. Example 3

Find states $|\psi_1\rangle$ and $|\psi_2\rangle$ for which the density operator:

$$\hat{\rho} = \frac{3}{4}|\uparrow_z\rangle\langle\uparrow_z| + \frac{1}{4}|\downarrow_z\rangle\langle\downarrow_z| = \frac{1}{2}|\psi_1\rangle\langle\psi_1| + \frac{1}{2}|\psi_2\rangle\langle\psi_2|$$

**(Solution):** Assume:

$$|\psi_1\rangle = \sqrt{\frac{3}{2}}|\uparrow_z\rangle + \sqrt{\frac{1}{2}}|\downarrow_z\rangle \cdot \frac{1}{\sqrt{2}}, \quad |\psi_2\rangle = \sqrt{\frac{3}{2}}|\uparrow_z\rangle - \sqrt{\frac{1}{2}}|\downarrow_z\rangle \cdot \frac{1}{\sqrt{2}}$$

Then $\hat{\rho} = \begin{pmatrix}3/4&0\\0&1/4\end{pmatrix}$, and $\text{Tr}[\hat{\rho}^2] = \frac{9+1}{16} + \text{...} = \frac{5}{8}$ (mixed state).

---

## 23. Example 4

An attempt at a Bell-state measurement produces a mixed state: the two photons are in the entangled state $\frac{1}{\sqrt{2}}[|x,x\rangle - |y,y\rangle]$ with probability $p$, and with probability $\frac{1-p}{2}$ each in $|x,x\rangle$ and $|y,y\rangle$.

**(Solution):**

$$|\psi_1\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix}1\\0\\0\\1\end{pmatrix}, \quad |\psi_2\rangle = \begin{pmatrix}1\\0\\0\\0\end{pmatrix}, \quad |\psi_3\rangle = \begin{pmatrix}0\\0\\0\\1\end{pmatrix}$$

$$\hat{\rho} = p|\psi_1\rangle\langle\psi_1| + \frac{1-p}{2}|\psi_2\rangle\langle\psi_2| + \frac{1-p}{2}|\psi_3\rangle\langle\psi_3| = \begin{pmatrix}1/2&0&0&p/2\\0&0&0&0\\0&0&0&0\\p/2&0&0&1/2\end{pmatrix}$$

with $\text{Tr}[\hat{\rho}^2] = \frac{1+p^2}{2}$.

---

## 24. Example 5

Using the density operator formalism, show that the probability a measurement finds two spin-1/2 particles in state $|x,x\rangle$ differs for the pure Bell state $|\psi^{(-)}\rangle$ versus the mixed state $\hat{\rho}_2 = \frac{1}{2}|\uparrow_z\uparrow_z\rangle\langle\uparrow_z\uparrow_z| + \frac{1}{2}|\downarrow_z\downarrow_z\rangle\langle\downarrow_z\downarrow_z|$.

**(Solution):**

For the Bell state $|\psi^{(-)}\rangle$:

$$\hat{\rho}_1 = \frac{1}{2}\begin{pmatrix}1&0&0&1\\0&0&0&0\\0&0&0&0\\1&0&0&1\end{pmatrix}, \quad \text{Tr}[\hat{\rho}_1^2] = 1 \text{ (pure state)}$$

$$P(x,x) = \text{Tr}[\hat{P}_{xx}\hat{\rho}_1] = \frac{1}{2}$$

For the mixed state $\hat{\rho}_2$:

$$\hat{\rho}_2 = \frac{1}{2}\begin{pmatrix}1&0&0&0\\0&0&0&0\\0&0&0&0\\0&0&0&1\end{pmatrix}, \quad \text{Tr}[\hat{\rho}_2^2] = \frac{1}{2} \text{ (mixed state)}$$

$$P(x,x) = \text{Tr}[\hat{P}_{xx}\hat{\rho}_2] = \frac{1}{4}$$

The disagreement between quantum predictions for the entangled state versus a local realist view is apparent without resorting to Bell inequalities.

---

## 25. Example 6

Prove that states of the form:

$$|\psi_{12}\rangle = C_{xy}|x\rangle|y\rangle + C_{yx}|y\rangle|x\rangle$$

with $|C_{xy}|^2 + |C_{yx}|^2 = 1$ and both coefficients non-zero, **cannot** be written as a Kronecker product state $|\psi_{12}\rangle = |\psi'\rangle_1 \otimes |\psi'\rangle_2$.

**(Solution):** Suppose $|\psi_{12}\rangle = |\psi'\rangle_1 \otimes |\psi'\rangle_2$. Then the components satisfy $\rho_{xx} = 0$, $\rho_{yy} = 0$, and $C_{xy} = \alpha_x \beta_y$, $C_{yx} = \alpha_y \beta_x$. This gives $C_{xy}C_{yx} = (\alpha_x\beta_y)(\alpha_y\beta_x) = \rho_{xx}\rho_{yy} = 0$, which contradicts both coefficients being non-zero. $\square$

---

## 26. Example (Townsend)

Consider the state vector:

$$|\psi_{12}\rangle = \frac{1}{2}\left[|x\rangle_1|x\rangle_2 + |x\rangle_1|y\rangle_2 + |y\rangle_1|x\rangle_2 + |y\rangle_1|y\rangle_2\right]$$

The density operator:

$$\hat{\rho}_{12} = \frac{1}{4}\begin{pmatrix}1&1&1&1\\1&1&1&1\\1&1&1&1\\1&1&1&1\end{pmatrix}$$

The reduced density operators:

$$\hat{\rho}_1 = \text{Tr}_2[\hat{\rho}_{12}] = \frac{1}{2}\begin{pmatrix}1&1\\1&1\end{pmatrix}, \quad \hat{\rho}_2 = \text{Tr}_1[\hat{\rho}_{12}] = \frac{1}{2}\begin{pmatrix}1&1\\1&1\end{pmatrix}$$

Since $\hat{\rho}_1^2 = \hat{\rho}_1$ and $\hat{\rho}_2^2 = \hat{\rho}_2$, both reduced density operators describe **pure states**.

---

## 27. Werner State

We consider the density operator (4×4 matrix):

$$\hat{\rho} = \lambda|\psi^{(-)}\rangle\langle\psi^{(-)}| + \frac{1-\lambda}{4}\hat{I}_4$$

where $\lambda$ is a real parameter ($0 < \lambda < 1$). This gives:

$$\text{Tr}[\hat{\rho}^2] = \frac{1+3\lambda^2}{4}$$

For $0 < \lambda < 1$, $\frac{1}{4} < \text{Tr}[\hat{\rho}^2] < 1$, which means the system is **mixed**.

---

## 28. Two-Photon System

In order to describe the polarization state of the two-photon system, the polarization state is:

$$|x,x\rangle = |x_s\rangle \otimes |x_i\rangle = \begin{pmatrix}1\\0\end{pmatrix} \otimes \begin{pmatrix}1\\0\end{pmatrix} = \begin{pmatrix}1\\0\\0\\0\end{pmatrix}$$

We also have:

$$|45°, x\rangle = \frac{1}{\sqrt{2}}(|x,x\rangle + |y,x\rangle), \quad |R, R\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix}1\\i\end{pmatrix} \otimes \frac{1}{\sqrt{2}}\begin{pmatrix}1\\i\end{pmatrix}$$

The entangled Bell state:

$$|\psi^{(-)}\rangle = \frac{1}{\sqrt{2}}(|x,y\rangle - |y,x\rangle) = \frac{1}{\sqrt{2}}\begin{pmatrix}0\\1\\-1\\0\end{pmatrix}$$

can be expressed in various bases:

- In the ${|x'\rangle, |y'\rangle}$ basis: same form $\frac{1}{\sqrt{2}}(|x',y'\rangle - |y',x'\rangle)$
- In the ${|45°\rangle, |{-45°}\rangle}$ basis: also the same form
- In circular polarization: $\frac{1}{\sqrt{2}}(|R,L\rangle - |L,R\rangle)$

---

## 29. HV Polarization Operator

$$\hat{P}_{HV} = |x\rangle\langle x| - |y\rangle\langle y| = \begin{pmatrix}1&0\\0&-1\end{pmatrix}$$

**Example:** Acting on state $|y, 45°\rangle$:

$$\hat{P}_{HV}^{(s)} \otimes \hat{I}^{(i)} = \begin{pmatrix}0&1\\1&0\end{pmatrix}^{(s)}, \quad \hat{I}^{(s)} \otimes \hat{P}_{HV}^{(i)} = \begin{pmatrix}0&1\\1&0\end{pmatrix}^{(i)}$$

---

## 30. Problem: Pure State vs. Mixed State

Compare the density operators corresponding to:

**(a)** A **superposition** of equal parts $|x,x\rangle$ and $|y,y\rangle$ (relative phase zero):

$$|\psi\rangle = \frac{1}{\sqrt{2}}(|x,x\rangle + |y,y\rangle) = \frac{1}{\sqrt{2}}\begin{pmatrix}1\\0\\0\\1\end{pmatrix}$$

$$\hat{\rho}_{\text{pure}} = \frac{1}{2}\begin{pmatrix}1&0&0&1\\0&0&0&0\\0&0&0&0\\1&0&0&1\end{pmatrix}$$

**(b)** A **mixture** of equal parts $|x,x\rangle$ and $|y,y\rangle$:

$$\hat{\rho}_{\text{mixed}} = \frac{1}{2}\begin{pmatrix}1&0&0&0\\0&0&0&0\\0&0&0&0\\0&0&0&1\end{pmatrix}$$

The pure-state density operator has additional off-diagonal terms that encode the coherence (entanglement) between the states.

---

## 31. Problem: Conditional Probability

For a two-photon system prepared as an equal mixture of $|x,x\rangle$ and $|y,y\rangle$, find $P(45°_s | 45°_i)$.

$$\hat{\rho} = \frac{1}{2}\begin{pmatrix}1&0&0&0\\0&0&0&0\\0&0&0&0\\0&0&0&1\end{pmatrix}$$

**Solution:**

$$P(45°_s, 45°_i) = \text{Tr}[\hat{P}_{45,45}\hat{\rho}] = \frac{1}{4}$$

$$P(45°_i) = \text{Tr}[(\hat{I} \otimes |{45°}\rangle\langle{45°}|)\hat{\rho}] = \frac{1}{2}$$

$$P(45°_s | 45°_i) = \frac{P(45°_s, 45°_i)}{P(45°_i)} = \frac{1/4}{1/2} = \frac{1}{2}$$

using **Bayes' theorem**: $P(a|b) = \frac{P(a,b)}{P(b)}$.

---

## References

- L.D. Landau and E.M. Lifshitz, _Quantum Mechanics_ (Pergamon Press, Oxford, 1977).
- L.I. Schiff, _Quantum Mechanics_, 3rd ed. (McGraw-Hill, New York, 1968).
- J.J. Sakurai and J. Napolitano, _Modern Quantum Mechanics_, 2nd ed. (Addison-Wesley, 2011).
- J.S. Townsend, _A Modern Approach to Quantum Mechanics_, 2nd ed. (University Science Books, 2012).
- K. Blum, _Density Matrix Theory and Applications_, 2nd ed. (Plenum Press, NY, 1996).
- M.A. Nielsen and I.L. Chuang, _Quantum Computation and Quantum Information_, 10th Anniversary Edition (Cambridge, 2010).
- A. Graham, _Kronecker Products and Matrix Calculus with Applications_ (Ellis Horwood, 1981).
- U. Leonhardt, _Essential Quantum Optics_ (Cambridge, 2010).
- M. Beck, _Quantum Mechanics: Theory and Experiment_ (Oxford, 2012).
- J. Binney and D. Skinner, _The Physics of Quantum Mechanics_ (Oxford, 2014).
- J. Preskill, _Lecture Notes for Phys. 229: Quantum Information and Computation_ (September, 1998).

---

## Appendix I: Definition of the Kronecker Product

**(a)** For vectors:

$$\hat{A} = \begin{pmatrix}a_1\\a_2\end{pmatrix}, \quad \hat{B} = \begin{pmatrix}b_1\\b_2\end{pmatrix}$$

$$\hat{A} \otimes \hat{B} = \begin{pmatrix}a_1\hat{B}\\a_2\hat{B}\end{pmatrix} = \begin{pmatrix}a_1 b_1\\a_1 b_2\\a_2 b_1\\a_2 b_2\end{pmatrix}$$

**(b)** For matrices:

$$\hat{A} = \begin{pmatrix}a_{11}&a_{12}\\a_{21}&a_{22}\end{pmatrix}, \quad \hat{B} = \begin{pmatrix}b_{11}&b_{12}\\b_{21}&b_{22}\end{pmatrix}$$

$$\hat{A} \otimes \hat{B} = \begin{pmatrix}a_{11}\hat{B}&a_{12}\hat{B}\\a_{21}\hat{B}&a_{22}\hat{B}\end{pmatrix} = \begin{pmatrix}a_{11}b_{11}&a_{11}b_{12}&a_{12}b_{11}&a_{12}b_{12}\\a_{11}b_{21}&a_{11}b_{22}&a_{12}b_{21}&a_{12}b_{22}\\a_{21}b_{11}&a_{21}b_{12}&a_{22}b_{11}&a_{22}b_{12}\\a_{21}b_{21}&a_{21}b_{22}&a_{22}b_{21}&a_{22}b_{22}\end{pmatrix}$$

---

## Appendix II: Formulas Related to the Kronecker Product

|#|Formula|
|---|---|
|(1)|$\text{Tr}(\hat{A}\otimes\hat{B}) = \text{Tr}(\hat{A})\text{Tr}(\hat{B})$|
|(2)|$\text{Tr}(\hat{A}\hat{B}\hat{C}) = \text{Tr}(\hat{C}\hat{A}\hat{B}) = \text{Tr}(\hat{B}\hat{C}\hat{A})$|
|(3)|$\text{Tr}[|
|(4)|$\text{Tr}[\hat{A}\otimes\hat{B}] = \text{Tr}[\hat{A}],\text{Tr}[\hat{B}]$|
|(5)|$(|
|(6)|$\text{Tr}[\hat{A}\otimes\hat{B}] = \text{Tr}[\hat{B}],\hat{A}$|
|(7)|$\text{Tr}_2(\hat{A}_1\otimes\hat{B}_2) = \hat{A}_1,\text{Tr}_2(\hat{B}_2)$|
|(8)|$\text{Tr}_1(\hat{A}_1\otimes\hat{B}_2) = \hat{B}_2,\text{Tr}_1(\hat{A}_1)$|
|(9)|$\text{Tr}_1[\hat{A}_1\hat{\rho}_{12}] = \hat{A}_1,\text{Tr}_{12}[(\hat{A}_1\otimes\hat{1}_2)\hat{\rho}_{12}]$|
|(10)|$\text{Tr}_2[\hat{A}_2\hat{\rho}_{12}] = \hat{A}_2,\text{Tr}_{12}[(\hat{1}_1\otimes\hat{A}_2)\hat{\rho}_{12}]$|
|(11)|$(|

### Partial Trace and Kronecker Product

$$\text{Tr}[|a\rangle\langle b|] = \langle b|a\rangle$$

$$\text{Tr}[\hat{A}\otimes\hat{B}] = \text{Tr}[\hat{A}],\text{Tr}[\hat{B}]$$

$$\text{Tr}_2[\hat{A}_1\otimes\hat{B}_2] = \hat{A}_1,\text{Tr}[\hat{B}_2]$$

$$\text{Tr}_1[\hat{A}_1\otimes\hat{B}_2] = \hat{B}_2,\text{Tr}[\hat{A}_1]$$

### Useful Kronecker Product Identities

$$(\hat{A}\otimes\hat{B})(\hat{C}\otimes\hat{D}) = (\hat{A}\hat{C})\otimes(\hat{B}\hat{D})$$

$$(\hat{A}\otimes\hat{B})^\dagger = \hat{A}^\dagger\otimes\hat{B}^\dagger$$

$$(\hat{A}\otimes\hat{B})^T = \hat{A}^T\otimes\hat{B}^T$$

$$(\hat{A}\otimes\hat{B})^{-1} = \hat{A}^{-1}\otimes\hat{B}^{-1}$$

$$\det(\hat{A}\otimes\hat{B}) = \det(\hat{A})^n\det(\hat{B})^m \quad (A: m\times m,\ B: n\times n)$$

$$\hat{A}\otimes\hat{B} \neq \hat{B}\otimes\hat{A} \quad \text{(in general)}$$

---

## Appendix: Mathematica Programs for Partial Trace

Programs for the partial trace of $8\times8$ and $4\times4$ matrices.

**For $4\times4$ matrices** (`PartialTr41`, `PartialTr42`), computing $\text{Tr}_1[\rho_{12}]$ and $\text{Tr}_2[\rho_{12}]$:

```mathematica
PartialTr41[ρ1_] := Module[{A1, K1, K2, K12}, A1 = ρ1;
  K1 = A1[[{1, 2}, {1, 2}]]; K2 = A1[[{3, 4}, {3, 4}]];
  K12 = K1 + K2];

PartialTr42[ρ1_] := Module[{A1, K1, K2, K12}, A1 = ρ1;
  A1[[All, {2, 3}]] = A1[[All, {3, 2}]];
  A1[[{2, 3}]] = A1[[{3, 2}]];
  K1 = A1[[{1, 2}, {1, 2}]]; K2 = A1[[{3, 4}, {3, 4}]];
  K12 = K1 + K2];
```

**For $8\times8$ matrices** (`PartialTr81`, `PartialTr82`, `PartialTr83`), computing $\rho_{23} = \text{Tr}_1[\rho_{123}]$, $\rho_{13} = \text{Tr}_2[\rho_{123}]$, $\rho_{12} = \text{Tr}_3[\rho_{123}]$:

```mathematica
PartialTr81[ρ1_] := Module[{A1, K1, K2, K12}, A1 = ρ1;
  K1 = A1[[{1, 2, 3, 4}, {1, 2, 3, 4}]];
  K2 = A1[[{5, 6, 7, 8}, {5, 6, 7, 8}]]; K12 = K1 + K2];
```

_(See document for full `PartialTr82` and `PartialTr83` implementations.)_