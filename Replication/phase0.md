# Phase 0: Theoretical Derivation for Portfolio Optimization VQE

## 1. QUBO to Ising Hamiltonian Mapping

### Objective Function Formulation

The portfolio optimization problem is formulated as a Quadratic Unconstrained Binary Optimization (QUBO) problem. The objective function $C(x)$ is given by Equation (12) in the reference paper:

$$ C(x) = -λ \sum_{i=1}^{N} \mu_i x_i + (1-\lambda) \sum_{i=1}^{N} \sum_{j=i+1}^{N} \sigma_{ij} x_i x_j + p \left( \sum_{i=1}^{N} x_i - \frac{N}{2} \right)^2 $$

Where:
*   $x_i \in \{0, 1\}$ are binary decision variables ($1$ if asset $i$ is selected, $0$ otherwise).
*   $N$ is the total number of assets.
*   $μ_i$ is the expected return of asset $i$.
*   $σ_{ij}$ is the covariance between assets $i$ and $j$.
*   $λ$ is the risk aversion parameter ($0 \le λ \le 1$).
*   $p$ is the penalty coefficient for the cardinality constraint ($\sum x_i = N/2$).

### Expansion of the Constraint Term

First, let us expand the squared penalty term:

$$ \left( \sum_{i=1}^{N} x_i - \frac{N}{2} \right)^2 = \left( \sum_{i=1}^{N} x_i \right)^2 - N \sum_{i=1}^{N} x_i + \frac{N^2}{4} $$

Recall that for binary variables $x_i^2 = x_i$. Thus:
$$ \left( \sum_{i=1}^{N} x_i \right)^2 = \sum_{i=1}^{N} x_i^2 + 2 \sum_{i=1}^{N} \sum_{j=i+1}^{N} x_i x_j = \sum_{i=1}^{N} x_i + 2 \sum_{i=1}^{N} \sum_{j=i+1}^{N} x_i x_j $$

Substituting this back into the penalty term:
$$ p \left( \sum_{i=1}^{N} x_i - \frac{N}{2} \right)^2 = p \left( \sum_{i=1}^{N} x_i + 2 \sum_{i<j} x_i x_j - N \sum_{i=1}^{N} x_i \right) + \text{const} $$
$$ = p \sum_{i=1}^{N} (1 - N) x_i + 2p \sum_{i<j} x_i x_j + \text{const} $$

### Grouping Coefficients in $C(x)$

Now, we rewrite $C(x)$ by grouping linear and quadratic terms. Let $Q_i$ be the coefficient for $x_i$ and $Q_{ij}$ be the coefficient for $x_i x_j$:

$$ C(x) = \sum_{i=1}^{N} Q_i x_i + \sum_{i=1}^{N} \sum_{j=i+1}^{N} Q_{ij} x_i x_j + \text{const} $$

Comparing with the original equation and the expanded penalty:
*   **Linear Coefficient ($Q_i$):**
    $$ Q_i = -λ \mu_i + p(1 - N) $$
*   **Quadratic Coefficient ($Q_{ij}$):**
    $$ Q_{ij} = (1-\lambda) \sigma_{ij} + 2p $$

### Transformation to Ising Hamiltonian

To map to the Ising model, we use the change of variable:
$$ x_i = \frac{1 - Z_i}{2} $$
where $Z_i \in \{1, -1\}$ are the Pauli-Z operators (eigenvalues).

**1. Transforming the Linear Term:**
$$ \sum_{i} Q_i x_i = \sum_{i} Q_i \left( \frac{1 - Z_i}{2} \right) = \sum_{i} \frac{Q_i}{2} - \sum_{i} \frac{Q_i}{2} Z_i $$

**2. Transforming the Quadratic Term:**
$$ \sum_{i<j} Q_{ij} x_i x_j = \sum_{i<j} Q_{ij} \left( \frac{1 - Z_i}{2} \right) \left( \frac{1 - Z_j}{2} \right) $$
$$ = \sum_{i<j} \frac{Q_{ij}}{4} (1 - Z_i - Z_j + Z_i Z_j) $$
$$ = \sum_{i<j} \frac{Q_{ij}}{4} - \sum_{i<j} \frac{Q_{ij}}{4} Z_i - \sum_{i<j} \frac{Q_{ij}}{4} Z_j + \sum_{i<j} \frac{Q_{ij}}{4} Z_i Z_j $$

### Deriving $h_k$ and $J_{ij}$

We seek the Hamiltonian in the form $H = \underbrace{\sum_{k} h_k Z_k}_{\text{external factor}} + \sum_{i<j} \underbrace{J_{ij}}_{\text{brdr}} \underbrace{Z_i Z_j}_{\text{inter}}$.

**Coupling Coefficients ($J_{ij}$):**
From the quadratic expansion term $\sum_{i<j} \frac{Q_{ij}}{4} Z_i Z_j$, we directly identify:
$$ J_{ij} = \frac{Q_{ij}}{4} = \frac{(1-\lambda) \sigma_{ij} + 2p}{4} $$

**Local Field Coefficients ($h_k$):**
For a specific spin $Z_k$, contributions come from:
1.  The linear term: $-\frac{Q_k}{2} Z_k$
2.  The quadratic term where $i=k$ (sum over $j>k$): $-\sum_{j>k} \frac{Q_{kj}}{4} Z_k$
3.  The quadratic term where $j=k$ (sum over $i<k$): $-\sum_{i<k} \frac{Q_{ik}}{4} Z_k$

Thus:
$$ h_k = -\frac{Q_k}{2} - \sum_{j>k} \frac{Q_{kj}}{4} - \sum_{i<k} \frac{Q_{ik}}{4} $$

Substituting $Q_k$ and $Q_{ij}$:
$$ h_k = -\frac{-λ \mu_k + p(1-N)}{2} - \frac{1}{4} \sum_{j \neq k} \left( (1-\lambda)\sigma_{kj} + 2p \right) $$
*(Note: $σ_{ij} = σ_{ji}$ is symmetric)*

Simplifying $h_k$:
$$ h_k = \frac{λ \mu_k}{2} - \frac{p(1-N)}{2} - \frac{1}{4} \sum_{j \neq k} (1-\lambda)\sigma_{kj} - \frac{1}{4} \sum_{j \neq k} 2p $$
The last term is $-\frac{2p}{4}(N-1) = -\frac{p}{2}(N-1) = \frac{p(1-N)}{2}$.

Canceling the penalty terms:
$$ h_k = \frac{λ \mu_k}{2} - \frac{p(1-N)}{2} + \frac{p(1-N)}{2} - \frac{1-\lambda}{4} \sum_{j \neq k} σ_{kj} $$
$$ h_k = \frac{λ \mu_k}{2} - \frac{1-\lambda}{4} \sum_{j \neq k} σ_{kj} $$

### Final Expressions

For the Hamiltonian $H = \sum_{i} h_i Z_i + \sum_{i<j} J_{ij} Z_i Z_j$:

$$ h_i = \frac{λ \mu_i}{2} - \frac{1-\lambda}{4} \sum_{j \neq i}^N σ_{ij} $$

$$ J_{ij} = \frac{(1-\lambda) σ_{ij} + 2p}{4} $$

### General Ising Form and VQE Background

The paper notes that the objective function can be written in the classical Ising form (Eq. 13):
$$ E(s) = -\sum_{i=1} h_i s_i - \sum_{i<j} J_{ij} s_i s_j $$
where $s_i \in \{+1, -1\}$.

The corresponding Quantum Hamiltonian is (Eq. 14):
$$ \hat{H} = -\sum_{i=1} h_i \hat{Z}_i - \sum_{i<j} J_{ij} \hat{Z}_i \hat{Z}_j $$

**VQE Algorithm Basics:**
The Variational Quantum Eigensolver minimizes the expectation value (Eq. 15):
$$ E(\boldsymbol{\theta}) = \frac{\langle \psi(\boldsymbol{\theta}) | \hat{H} | \psi(\boldsymbol{\theta}) \rangle}{\langle \psi(\boldsymbol{\theta}) | \psi(\boldsymbol{\theta}) \rangle} $$

Expanding the variational state in the computational basis $|\psi(\boldsymbol{\theta}^*)\rangle = \sum_n c_n(\boldsymbol{\theta}^*)|n\rangle$ (Eq. 17), the energy is (Eq. 18):
$$ E(\boldsymbol{\theta}^*) = \sum_n |c_n(\boldsymbol{\theta}^*)|^2 E_n $$

**Standard CVaR (Conditional Value-at-Risk):**
Instead of the mean energy, Barkoutsos et al. proposed using CVaR. Given ordered sampled energies $E_{(1)} \le E_{(2)} \le \dots \le E_{(K)}$ from $K$ shots (Eq. 19):
$$ CVaR_\alpha(E) = \frac{1}{\lceil \alpha K \rceil} \sum_{k=1}^{\lceil \alpha K \rceil} E_{(k)} $$

When $\alpha = 1$, this reduces to the standard mean energy (Eq. 20):
$$ \bar{E} = \frac{1}{K} \sum_{k=1}^{K} E_k $$

---

## 2. Weighted CVaR (WCVaR) Analysis

### Definition
The Weighted Conditional Value-at-Risk (WCVaR) is defined in Equation (21) as:
$$ WCVaR_\alpha(E) = \sum_{k=1}^{\lceil \alpha K \rceil} w_k E_{(k)} $$

Where:
*   $K$ is the total number of samples (shots).
*   $α \in (0, 1]$ is the confidence level fraction.
*   $E_{(k)}$ are the sampled energies sorted in ascending order ($E_{(1)} \le E_{(2)} \le \dots \le E_{(K)}$).
*   $w_k$ are normalized weights such that $\sum_{k=1}^{\lceil \alpha K \rceil} w_k = 1$.

### Difference from Standard CVaR
Standard CVaR (or Expected Shortfall) assigns **uniform weights** to the tail:
$$ w_k^{CVaR} = \frac{1}{\lceil \alpha K \rceil} \quad \text{for } k \le \lceil \alpha K \rceil, \quad 0 \text{ otherwise.} $$
It simply averages the best $\alpha$-fraction of samples.

**WCVaR** introduces non-uniform weighting within this tail. The paper (Appendix A) suggests a **Piecewise Exponential Weighting**:
$$ w_k \propto \begin{cases} \exp(-\beta_1 k) & k < N_1 \ \exp(-\beta_2 (k-N_1)) & N_1 \le k < N_2 \ \dots \end{cases} $$
This assigns significantly higher weight to the lowest energies ($E_{(1)}, E_{(2)}, \dots$) compared to those at the edge of the cutoff ($E_{(\lceil \alpha K \rceil)}$).

### Theoretical Benefit for VQE Convergence
1.  **Smoother Landscape vs. Min-Energy:** Purely minimizing the minimum sampled energy (equivalent to $\alpha \to 0$) creates a discontinuous, jagged landscape that is hard for classical optimizers (like COBYLA or CMA-ES) to traverse.
2.  **Focus vs. Mean:** Minimizing the full expectation value ($\alpha=1$) often leads to "barren plateaus" or getting stuck in local minima because high-energy states wash out the gradients of the ground state path.
3.  **WCVaR Advantage:** By using a weighted tail, WCVaR provides a middle ground. It heavily prioritizes the ground state (like min-energy) but retains enough contribution from slightly higher energy states (the "tail") to provide a smoother, differentiable gradient slope towards the minimum. The exponential decay ensures that as the optimizer improves, it is driven more aggressively towards the true ground state $E_{(1)}$ rather than just the average of the tail.
