Computational Economics
https://doi.org/10.1007/s10614-025-11061-5

Solving Multiple Discretization Portfolio Optimization
Problem with Quantum-Classical Hybrid Algorithms
Haijing Wei1 · Yanbo J. Wang2 · Haoxiang Yang3 · Xuan Yang2 · Mingming Cao3 ·
Qi Xu2 · Minglei Cai3 · Yiduo Wang2 · Zhichao Mao3 · Xiaofeng Cao2 ·
Quanxin Mei3 · Jie Wang2 · Xiaojun Zhou2 · Lin Yao3 · Wending Zhao3
Accepted: 11 July 2025
© The Author(s) 2025

Abstract
Portfolio optimization (PO) plays a central role in finance, encompassing both resource allocation and risk management. While numerous algorithms have been developed for continuous-variable PO, the inclusion of large, indivisible assets such
as real estate transforms the task into a combinatorial optimization problem, which
is NP-hard for classical computers. This study explores using quantum-classical hybrid algorithms for multi-discretized portfolio optimization, addressing the needs of
real-world applications. We propose a flexible theoretical model that can solve PO
problems with various types of discrete assets and constraints, which is compatible
with both quantum and classical computing paradigms. Then, we use the D-Wave
quantum processor and classical solver to determine optimal investment strategies.
Experimental results indicate that the hybrid quantum algorithm outperforms both
classical computing methods and quantum annealing algorithms in terms of return
and risk management. This research enhances quantum computing applications in
finance and provides insights into future algorithm design.
Keywords Portfolio optimization · Discrete combinatorial optimization problem ·
Quantum computing · Quantum-classical hybrid algorithms

Lin Yao
yaolin@hyqubit.com
Wending Zhao
zhaowending@hyqubit.com
1

College of Liberal Arts, Shanghai University, Shanghai 200444, China

2

Longying Zhida (Beijing) Technology Co., Ltd., Beijing 100020, China

3

Huayi Boao (Beijing) Quantum Technology Co., Ltd., Beijing 100176, China

13

H. Wei et al.

1 Introduction
Portfolio optimization (PO) is a critical financial task that focuses on finding the optimal balance between risk and return, with wide applications across various financial
sectors. This process often considers multiple constraints, such as risk thresholds,
investment proportions, diversification requirements, and regulatory compliance
(Lewis, 1988). The Markowitz model provides a framework for quantifying the
trade-off between risk and return (Markowitz, 1952). Typically, this model is effective when dealing with continuous variables. However, in real-world scenarios, the
independent variables consist of both continuous and discrete types. For example,
decisions such as whether to purchase a real estate property or a high-value NFT are
naturally modeled as binary variables, while the allocation of indivisible high-value
homogeneous goods (i.e., aircraft, servers, or heavy machinery) is best represented
using integer variables. These variables convert the optimization problem into a
Mixed-Integer Optimization problem or Discrete Optimization problem which is NPHard, thus challenging to solve classically (Vesselinova et al., 2020). Consequently,
there is a pressing need for advanced algorithms capable of effectively solving these
complex Combinatorial Optimization Problems (COPs), especially in the field of
financial computing (Orús et al., 2019; Lopez de Prado, 2015).
Given the complexity of combinatorial optimization algorithms, developing and
refining heuristic algorithms has emerged as a significant research focus in this field.
Some notable heuristic algorithms have been widely applied in portfolio optimization, option pricing, risk prediction and some other financial applications (Doğan et
al., 2024; Cura, 2021; He et al., 2023; Shinzato, 2018; De Moraes & Coelho, 2022).
These include algorithms such as Tabu Search (TS) (Glover, 1986, 1990), Simulated Annealing(SA) (Kirkpatrick et al., 1983), Steepest Descent(SD) (Bottou, 1998;
Ruder, 2016), and Genetic Algorithms (Goldberg et al., 1989). Particularly, some
nature-inspired algorithms have also demonstrated promising efficacy in addressing
some specific optimization problems, such as firefly algorithm (Yang, 2009; Abedi
& Gharehchopogh, 2020) and RIME optimization algorithm (Abdel-Salam et al.,
2024). With the rapid development of machine learning technologies, some machine
learning methods have gradually been used in portfolio optimization and other financial computing scenarios (Eraña-Díaz et al., 2020; Chen, 2021; Orra et al., 2025).
Quantum computing (QC), as a new computational paradigm, offers theoretically grounded advantages in solving prime factorization problem, a NP-hard
problem (Shor, 1994). Additionally, QC exhibits significant advantages in addressing Combinatorial Optimization Problems (COPs), which involve discrete variables (Nielsen & Chuang, 2011; Brandhofer et al., 2022; Lu & Yang, 2024; Woerner
& Egger, 2019; Orús et al., 2019). Recent advances in quantum hardware—including
increases in qubit count (Guo et al., 2024), gate fidelity (Ryan-Anderson et al., 2024),
and quantum volume (Jurcevic et al., 2021; Baldwin et al., 2022)—have significantly
improved the feasibility of applying quantum algorithms to real-world financial problems (Sofge, 2008; Orús et al., 2019; Lu & Yang, 2024; Buonaiuto et al., 2023). For
instance, IBM demonstrated a quantum algorithm based on amplitude estimation for
financial risk analysis that achieved faster convergence than classical Monte Carlo
simulations (Woerner & Egger, 2019). D-Wave’s superconducting quantum annealer

13

Solving Multiple Discretization Portfolio Optimization Problem with…

has been employed to solve discrete-time portfolio optimization problems, outperforming classical methods such as GEKKO (Beal, 2021) and quantum-inspired tensor
network optimizers (Orús, 2014, 2019; Mugel et al., 2022) in terms of computational
speed. Additional applications of quantum annealing include addressing multi-period
portfolio optimization (Rosenberg et al., 2015), asset correlation detection (Kalra et
al., 2018), and minimum holding period constraints in portfolio rebalancing (Mugel
et al., 2021). These developments demonstrate that even in the current Noisy Intermediate-Scale Quantum (NISQ) era, quantum computing is already being effectively
applied to practical financial optimization tasks.
In previous work, quantum algorithms were limited to handling portfolio optimization problems for a single asset type. Our model incorporates quantitative constraints
by including assets that must be acquired in indivisible units—such as aircraft, servers, or heavy machinery—aligning closely with real-world investment practices. It
also accommodates assets with multiple discrete valuations, such as real estate, art,
and private equity, thereby capturing the complexity of modern investment decisions.
Consequently, our model expands the applicability of quantum algorithms in solving
portfolio optimization problems to a broader range of asset types.
We then implemented this model by using the D-Wave quantum annealer alongside various classical solvers, conducting backtesting on two datasets. Results show
that the quantum-classical hybrid approach delivers superior performance in terms
of return and risk trade-offs. Furthermore, we analyzed the impact of increased qubit
counts on solution quality, demonstrating further potential for performance gains.
This work establishes a practical framework for applying quantum computing in
finance and outlines avenues for future improvement.
This paper is structured as follows: Firstly, we introduce our proposed theoretical
model aims at solving multiple discretization portfolio optimization problems. In the
Next, we introduce how to introduce linear constraints in the model and transform
it into a QUBO problem. Then, we outline the computational methods and datasets
containing multiple discretization assets. Subsequently, we execute this model on
D-Wave’s processor and compare the results with various classical algorithms for
solving PO problems. In the following section, the results are shown and the algorithmic complexity and effectiveness of these schemes are discussed. Finally, conclusions and future works are outlined.

2 Mathematical Modeling
2.1 QUBO Interpretation of Multiple Discretization PO Problem
This section elucidates the construction of a discrete portfolio optimization model
suitable for both quantum and classical computation. The input data include historical closing prices of selected assets, from which we compute return rates and the
covariance matrix to characterize expected performance and risk.
We formulate the problem using a QUBO-based framework to represent portfolio optimization with multiple discrete decision variables. Our approach builds on
the classical Markowitz mean-variance model (Markowitz, 1952), which balances

13

H. Wei et al.

expected return and risk via a risk preference parameter, λ. For a portfolio with up to
N assets, the objective function is given by:
(
)
min λω T Σω − ω T µ
ω

s.t.

N
∑

ωi = 1,(1)

i=1

where Σ is the covariance matrix, and ω depicts the investment strategy. ωi denotes
the weight assigned to the ith asset within the portfolio strategy. The covariance
matrix, Σ, depicts the interrelationships of daily returns among assets. The covariance between assets i and j, σij , is calculated as
σij =

Nt
1 ∑
(Rit − µi )(Rjt − µj ),
Nt − 1 t=1

(2)

where Rit is the daily return on day t for asset i determined by the formula
P −Pi,t−1
Rit = itPi,t−1
. Pit is the closing price of asset i on day t. The expected daily return
∑
Nt
Rit , with Nt representing the number of trading days considered in
is µi = N1t t=1
the analysis. The covariance matrix, Σ, encapsulates the joint variability and correlation between the returns of multi-assets across time.
This mathematical model can be precisely solved when ω is a continuous variable,
but NP hard for discrete variable. However, this assumption is seldom encountered in
reality, especially in the context of non-fungible assets like estates and artworks. In
our model, we generally categorize assets into three types:
1. Fungible Continuous (FC): Fungible assets that offer a nearly continuous range
of values, such as individual funds. where each asset’s price is relatively small in
comparison to the total budget B.
2. Fungible Discrete (FD): Fungible assets offering discrete valuation options, like
aircraft, servers, or heavy machinery.
3. Non Fungible (NF): Non-fungible assets with a fixed value of either zero or a
specific amount V, such as private funds with minimum investment requirements, real estate, and artworks.
Therefore, according to the above classification, we rewrite a new objective function
as a function of vi :
(
)
∑
∑
min λ⃗v T
⃗v − B⃗
µT ⃗v
subject to
vi = B,(3)
v

Each asset value vi is drawn from a domain depending its type and represented using
binary variables:

13

Solving Multiple Discretization Portfolio Optimization Problem with…

vi ∈ [0, B],

vi =

K
∑

(t)

2−t B bi

for i ∈ F C,

t=0

{

vi ∈ npi | 0 ≤ n ≤

⌊ ⌋}
B
pi

⌊ ⌋
B
p

, vi =

i
∑



(t)

t=0
(0)
vi = p i b i

vi ∈ {0, pi },

(4)

for i ∈ F D,

p i bi

for i ∈ N F.

(t)

Let x denote the vector of all binary variables bi , which is a linear transformation of
v. The QUBO objective becomes:
)
(
min xT Σ̃x − µ̃T x

subject to

∑

p̃i xi = B.(5)

To include the linear constraint in the objective function, we adopt a squared penalty
method with penalty term and corresponding penalty coefficient ξ , resulting in the
QUBO format:
(
(∑
)2 )
.
min xT Σ̃x − µ̃T x + ξ
p̃i xi − B
(6)
2.2 Constraints of the Number of Assets
To enhance portfolio diversification, it is often necessary to constrain the number of
selected assets within a specified range [L, U]. Such constraints require the inclusion
of auxiliary binary variables yi , indicating whether asset i is included in our portfolio.
These constraints can be mathematically expressed as:
L⩽

i<N
∑

yi ⩽ U,

yi ⩽

i=0

k<K
∑

(k)

bi

⩽ Kyi ,

for

k=0

i ∈ [0, N − 1].

(7)

To convert Eq. 7 into equalities, slack variables are introduced along with penalty
terms. Specifically, the slack variables, sL and sU , are introduced for each constraint
respectively. Then, Eq. 7 is transformed into equalities as follows:
N
−1
∑
i=0

yi −

K−1
∑
k=0

(k)

bi

yi − L + sL = 0,

+ sLi = 0,

K−1
∑
k=0

(k)

bi

N
−1
∑
i=0

yi − U − sU = 0, (8)

− Kyi − sU i = 0,

for

i ∈ [0, N − 1], (9)

13

H. Wei et al.

∑m

∑m

where sL = j=0 2j sLj and sU = j=0 2j sU j are the binary decomposition of
slack variables. Here, m is the maximum number of binary bits required, which is
determined based on the maximum value that each slack variable might attain. It is
essential to note that the coefficients in the above formula including the slack variables are all integers. It enables their representation in a binary format to align with
the binary essence of the problem. This approach guarantees that the integrity of
slack variables as integer (specifically binary) components is maintained in optimization problems dominated by binary decisions.
The penalty terms for constraints on the number of assets are included in the final
objective function by introducing the expression:
( N −1
)
N
−1
∑
∑
2
2
ξ (
yi − L + sL ) + (
yi − U − sU )
i=0

+

N
−1
∑
i=0

(

i=0

K−1
∑

K−1
∑ (k)
(k)
ξ(yi −
bi + sLi )2 + ξ(
bi − Kyi − sU i )2
k=0
k=0

) 

(10)

.

By adding these penalty terms Eq. 10 to the original objective function described in
Eq. 6, the comprehensive objective function for this optimization problem is formulated. This approach enables the application of optimization techniques to identify
solutions that adhere to the initial constraints with maximal accuracy. The parameter
ξ is adjusted to maintain a balance between the degree of constraint breaches and
other optimization objectives.

3 Methods and Dataset
3.1 Dataset of Preselect Assets
In this paper, we prepare two distinct datasets of financial assets to validate our
model’s effectiveness in portfolio optimization problems. Dataset-1 only contains
publicly tradable stocks from the Shanghai and Shenzhen Stock Exchanges, covering over a four-month period from September 1, 2021, to December 31, 2021.
Dataset-2 includes three asset types, private equity, mutual funds, and stocks, with
five instances of each asset type. The time window of Dataset-2 ranges from January
1, 2024, to April 18, 2024, encompassing 57 trading days. Stocks are categorized as
Fungible Continuous (FC), requiring investments in 100-share increments. Mutual
funds are considered Fungible Discrete (FD) due to the lack of similar restrictions.
Private equities are labeled Non-Fungible (NF), where interpolation methods are
used to calculate the value of assets for ensuring data consistency across asset types.
All pre-selected assets were obtained through random selection, in consideration of
industry diversity and fundamental assessment of assets. (See Appendix A for more
details about data.)

13

Solving Multiple Discretization Portfolio Optimization Problem with…

3.2 Computational Methods and Algorithms
In this work, we employ various methods and hardware implementations to solve the
portfolio optimization problem, which are shown below:
1. Quantum-Classical hybrid algorithm: Quantum-Classical Hybrid Annealing
(QCHA) implemented on D-Wave quantum annealing machine (King et al.,
2022; McGeoch, 2020).
2. Quantum algorithm: Quantum Annealing (QA) implemented on D-Wave quantum annealing machine (King et al., 2022; McGeoch, 2020).
3. Classical commercial software: Gurobi (Gurobi, 2018).
4. Classical inspired algorithm: Simulated Annealing (SA) (Kirkpatrick et al.,
1983).
5. Classical algorithm: Tabu Search (TS) (Glover, 1986, 1990).
6. Classical algorithm: Steepest Descent (SD) (Bottou, 1998; Ruder, 2016).
QCHA and QA are executed on the D-Wave Advantage system4.1 via the D-Wave
cloud and software (DWAVE, 2023). Compared to QA, QCHA leverages the advantages of quantum algorithms without being limited by the number of qubits by
decomposing the master problem into several sub-problems with fewer independent
variables. These sub-problems are solved by using quantum annealing algorithms,
and their optimal solutions are recombined to update the global solution. Consequently, QCHA is capable of solving larger-scale optimization problems while maintaining a solution quality compared to QA.
In this paper, these four classical algorithms are implemented on PC served as
benchmarks for quantum algorithms. These classical algorithms represent some of
the most common and effective methods for solving optimization problems. Gurobi
(Gurobi, 2018) is a widely recognized commercial software package that specializes
in solving combinatorial optimization issues. The other three algorithms are similarly
effective in solving combinatorial mathematical optimization and are extensively utilized in various fields, including finance (Rubio-García et al., 2024; Karakalidis &
Sifaleras, 2016; Mansouri & Moghadam, 2021; Doğan et al., 2024), job scheduling (Ma et al., 2023; Xie et al., 2023; Mahjoubi et al., 2022), path planning (AitSaadi et al., 2022; Sheikh-Hosseini & Hashemi, 2022), and machine learning (Araya,
2021; Song & Yang, 2023; Ganie & Dadvandipour, 2023). (See Appendix C for more
details of the Computational methods.)
3.3 Evaluation Indicators of Portfolio Optimization
In this work, we use the objective function value—analogous to the expectation
value of the cost Hamiltonian in quantum algorithms—to determine convergence.
However, relying solely on this metric to evaluate portfolio optimization neglects
the risk aspect of portfolio. Instead, we assess performance using Net Asset Value
(NAV) (Williams, 1938) to compute daily returns over shorter horizons. We further
incorporate standard financial metrics such as the rate of return (RET) (Cartea et al.,
2015; Markowits, 1952), the accumulated return (ACC) (Cartea et al., 2015), the

13

H. Wei et al.

Sharpe ratio (Sharpe, 1966), and the Sortino ratio (Sortino & Van Der Meer, 1991) to
provide a more robust and comprehensive evaluation. (See Appendix B for details.)

4 Experimental Results
In this section, we perform the results of portfolio optimization achieved through
the implementation of various algorithms and parameter configurations. Our study
includes classical algorithms and quantum algorithms running on D-Wave quantum annealing machines. We detail the performance of these algorithms using two
datasets, Dataset-1 and Dataset-2, and discuss how well the theoretical models align
with practical applications. Then, we present the performance of quantum algorithms
when introducing constraints and compare it to classical algorithms. Finally, we discussed the advantages of quantum algorithms in portfolio optimization problems, and
the effectiveness of our theoretical model and propose possible future optimizations
based on the results from the actual datasets.
4.1 Performance of Multiple Algorithms
Firstly, we compute the covariance matrices and corresponding objective functions of
pre-selected assets in both Dataset-1 and Dataset-2, respectively. Secondly, six different algorithms are employed to solve the portfolio optimization problem and obtained
the optimal investment strategies. Notably, the Quantum Annealing Algorithm (QA)
is not applicable to Dataset-2 due to the hardware limitations of the D-Wave system,
as the required number of qubits exceeded its capacity. In the next, we back-test these
strategies by the five evaluation indexes. The backtesting rule involves opening positions based on the optimization results from different algorithms at the start of the
trading period, with the assumption that no trading occurs during this period.
Figure 1(a) illustrates the daily return, NAV, over the trading period calculated
by six different algorithms in Dataset-1. For each stock, we assign five binary dis-

Fig. 1 The daily return of portfolio optimization strategies in Dataset-1 and Dataset-2. (a) For Dataset-1, the daily fluctuation of the NAV is illustrated using curves in different colors, representing six
algorithms, QCHA, QA, TS, SA, and SD. In this case, five binary variables are used to discretize the
investment proportions for each stock. The x-axis represents trading days, excluding non-trading days.
(b) For Dataset-2, five algorithms are used for portfolio optimization, where 128 binary independent
variables are assigned to discretize the investment ratios for 15 assets

13

Solving Multiple Discretization Portfolio Optimization Problem with…

crete independent variables to represent investment proportions, which is equivalent
to using 50 quantum bits in all. The analysis of Fig. 1(a) reveals that while the investment strategies generated by the six algorithms differ, the yield variation trends over
time exhibit a considerable degree of consistency. Notably, CHA algorithm, depicted
by the solid red line, outperforms the other algorithms consistently over the entire
duration, showcasing a superior end-of-period yield assessment. The same calculations were replicated on Dataset-2, as shown in Fig. 1(b). It is evident that both
QCHA (solid red line) and Gurobi (dashed blue line) algorithms maintain advantages
throughout the entire time period, compared to the other three algorithms. Analysis
of these two datasets underscores the superiority of QCHA in backtesting concerning
daily NAV. (See Appendix D for specific allocation proportions of investment strategies and more details.)
From the perspective of financial investment practitioners, the values of returns
and risks at end-of-period are of primary concern. Figure 2(a1-a3) display (a1)ACC,
(a2)Sharpe ratio, and (a3)Sortino ratio obtained by six algorithms at the end of the
period respectively. These calculations are based on Dataset-1, utilizing 50 discrete
variables. It is evident that the QCHA algorithm exhibits advantages in both ACC
and Sharpe ratio. Although it may not exhibit the best performance in Sortino ratio,
the difference compared to the best-performing is marginal. This result indicates that
QCHA is able to deliver high overall returns with strong risk-adjusted performance,
making it an appealing choice for practitioners focused on maximizing utility.
Similarly, we conducted similar experiments in Dataset-2, as depicted in Fig. 2(b1b3). Notably, Fig. 2(b3) highlights that the strategy produced by the QCHA algorithm
excels in the Sortino ratio. While in terms of ACC and Sharpe ratio, QCHA may not
be the optimal as indicated in Fig. 2(b1) and (b2). This suggests that QCHA maintains

Fig. 2 The end-of-perioid evaluation of portfolio strategies provided by different algorithms based on
(a) Dataset-1 and (b) Dataset-2 respectivily. The evaluations are presented by three indexes: (1) ACC
values, (2) Sharpe ratio, and (3) Sortino Ratio. The number of discretized independent variables is 50
for Dataset-1 and 128 for Dataset-2. In each set of numerical experiments, the algorithm with the best
performance is especially marked as a red box with black stars

13

H. Wei et al.

robust downside protection while offering competitive returns, thereby providing a
conservative yet efficient investment strategy in risk-sensitive environments.
Through the comparison of experiments illustrated in Figs. 1 and 2, QCHA demonstrates the most outstanding performance in both two datasets, showcasing its
adeptness in balancing returns and risks. Additionally, the Gurobi algorithm delivers
notable results, serving as a benchmark for subsequent experiments.
4.2 Effect of the Number of Qubits on Optimizers
The number of qubits constraints the resolution of Fungible Continuous(FC) assets’ proportion in the portfolio. One requires more qubits to encode a high precision float number. On the other hand, more qubits poses challenge to the current quantum hardware
and more hard to converge. In this section, we analyze the number of qubits’ impact on
the financial indicators.
In Fig. 3, we adjust the number of qubits in using QCHA. For Dataset-1, we vary
the qubit number from 20 to 50 and evaluate performance via backtesting. The Gurobi
algorithm with 50 discrete variables serves as a classical benchmark (red dashed
line). The QCHA algorithm with 40 qubits already surpasses Gurobi, underscoring

Fig. 3 Portfolio optimization results obtained by the QCHA algorithm with varying numbers of qubits
across two datasets. Subfigures (a) and (b) show the ACC values and Sharpe ratios of portfolio schemes
solved by QCHA based on Dataset-1, when the number of qubits increases from 20 to 50. The red
dashed line represents results from the Gurobi algorithm using 50 discrete variables as a benchmark.
Subfigures (c) and (d) present the results using 45, 91, and 128 qubits on Dataset-2, benchmarked
against Gurobi with 128 variables

13

Solving Multiple Discretization Portfolio Optimization Problem with…

the potential advantage of quantum algorithms. As the number of qubits increases,
the precision in investment allocation improves, leading to better outcomes. Financially, this allows for more accurate portfolio weights, enhancing return potential
while keeping risk in check.
For Dataset-2, we test QCHA with 45, 91, and 128 qubits, respectivily. Results
are shown in subfigures (c) and (d), where performance is evaluated by ACC and
Sharpe ratio. With 128 variables, QCHA achieves a higher Sharpe ratio than Gurobi
at the same scale. Although its ACC is slightly lower, the trend from 45 to 128 qubits
is approximately linear. This indicates steady financial improvement with hardware
scaling, supporting finer risk-return tradeoffs.
To summarize, in portfolio optimization, quantum-classical hybrid algorithms
already demonstrate superior performance at equivalent problem scales, compared
to other four classical solver. With the continued development of quantum hardware
and the natural suitability of quantum algorithms for COPs, quantum computing represent a highly promising direction for solviong financial optimization tasks in the
future. Quantum computing offer scalable, high-quality solutions for solving multiple
discretization portfolio optimization problem.
4.3 Portfolio Optimization with Constraints on the Number of Invested Assets
For solving practical PO problems, incorporating real-world constraints into the
theoretical model is a key task to build a robust and efficiency model. For instance,
risk-aware investors often diversify across multiple stocks or industries. Imposing
minimum or maximum thresholds on the number of investment assets enhances
diversification and improves risk management. Our portfolio optimization model
integrates constraints on the number of invested assets, as formulated in Eq. 10, using
transformations defined in Eqs. 7 and 8. With growing investment universes, incorporating such constraints is crucial for maintaining tractability and relevance.
Figure 4 presents results generated by three solvers—TS, Gurobi, and QCHA—
under both constrained and unconstrained settings. For Dataset-1, we assign 4 and 5
binary variables per asset, which equals to 40 and 50 qubits used and corresponds to
configurations labeled 40Q and 50Q on the X-axis. The constraint on the number of
invested assets is set to 3 < N < 8. When this constraint is applied, the total number
of discrete variables increases to 87 and 97, respectively.
All four evaluation metrics show a slight decline when constraints are imposed.
This can be attributed to the increased complexity of the solution space due to more
variables and the structural limitations introduced by the constraints, which can hinder the algorithm’s ability to escape local minima. However, the performance drop in
QCHA is significantly smaller than TS and Gurobi. This suggests that QCHA maintains high solution quality regardless of constraint inclusion or problem size.
In summary, the introduction of constraints imposes additional challenges on
both modeling and algorithmic performance, requiring efficient search strategies and
robustness against local optima. Our results demonstrate that the quantum-classical
hybrid QCHA algorithm is well-suited for solving constrained portfolio optimization
problems in large, discrete solution spaces.

13

H. Wei et al.

Fig. 4 Portfolio optimization results with and without constraints on the number of invested assets
based on Dataset-1. Evaluation metrics include: (a) End-of-period return (RET value), (b) ACC value,
(c) Sharpe ratio, and (d) Sortino ratio. Results are generated using three algorithms: QCHA, Gurobi
and TS. The number of used discrete variables, equal to qubits in quantum algorithm, is labeled on the
X-axis

5 Conclusion and Further Work
In this work, we present a hybrid quantum algorithm designed for multiple-discretization portfolio optimization. This framework allows for the inclusion of non-fungible and
high-value indivisible assets, addressing practical challenges often encountered in realworld investment scenarios. The algorithm builds on a QUBO formulation of the Markowitz model and is readily extensible to accommodate various real-world constraints.
We evaluate its performance on D-Wave’s quantum computing platform and find that,
compared to both classical and alternative quantum methods, our approach achieves
superior returns while maintaining robust risk resistance. Notably, its advantages become
increasingly evident as the number of discrete independent variables (qubits) scales up.
Looking ahead, the integration of real-time market data for dynamic portfolio optimization represents a promising extension. This would require the development of a
time-series modeling framework tailored to multiple discretization levels. As quantum hardware continues to evolve, optimizing larger and more complex portfolios
becomes feasible. More broadly, the prevalence of binary and integer decision variables across microeconomic models highlights the potential of quantum algorithms
in solving combinatorial optimization problems. In order to address larger-scale port-

13

Solving Multiple Discretization Portfolio Optimization Problem with…

folio optimization challenges, quantum computing hardware, particularly in terms of
gate fidelity and qubit count, requires further enhancement to satisfy the demands of
practical applications. Moreover, combining machine learning with quantum computing in this domain offers a compelling avenue for future research and application.

Appendix

A Description to Dataset Selections
In this paper, we prepare two sets of assets, Dataset-1, which includes only normal tradable stocks, and Dataset-2, which comprises private offering funds, public offering funds, and stocks. Both of them exhibit relatively short time windows
characterized by short-term unpredictability and volatility. The fluctuations inherent
in these short time frames pose significant challenges. This volatility necessitates
a more robust strategy, as traditional reliance on broader, long-term trends proves
insufficient. These factors highlight the complexity and nuanced nature of formulating short-term financial investment strategies. Consequently, we aim to develop
a new algorithm capable of efficiently calculating the optimal solution to mitigate
investment risk.
A.1 Dataset-1: Only Stocks
The stocks in Dataset-1 are selected from the Shanghai and Shenzhen stock
exchanges for the period spanning September 1, 2021, to December 31, 2021. The
dataset comprises 10 stocks and covers a four-month analysis period. Daily closing
stock prices are collected from the official websites of the Shanghai and Shenzhen
stock exchanges. These two market indices do not exhibit static or monotonic behavior during the designated trading period.
Considering the randomness of the selection of data sampling and the dispersion of
asset matching, the selected stocks represent a diverse range of industries, including
shipping ports, gaming, power grid equipment, electricity, diversified finance, medical services, and alcoholic beverages. Approximately 50 stocks were chosen from
each industry to form a stock pool based on the department’s focus. Due to the current limitations in the number of available qubits, sampling methods were employed
to select 10 stocks from this pool. Stocks 1 to 10 represent: Rizhao Port (600017.
SH), Tianzhou Culture (300148.SZ), Moen Electric (002451.SZ), COSCO Shipping
Holdings (601919.SH), and Guangdong Electric Power A (000539.SZ), Xiangyi
Rongtong (600830.SH), Tongce Medical (600763.SH), Lianyungang (601008.SH),
Kweichow Moutai (600519.SH) and Wuliangye (000858.SZ) respectively.

13

H. Wei et al.

Fig. 5 The Net Asset Value (NAV) over time when the investment amount is equally divided among the
pre-selected assets in (a)Dataset-1 and (b)Dataset-2 respectively

As illustrated in Fig. 5(a), we present the daily NAV resulting from an equal investment in 10 stocks from Dataset-1. Backtesting this equal-weighted strategy yields
the following end-of-period evaluation metrics: RET = 0.172, ACC = 1.052,
Sharpe = 0.639, and Sortino = 1.245, with net income close to zero. These results
suggest that the selected assets in Dataset-1 display a high degree of randomness and
volatility. Compared to the outcomes achieved using various algorithms discussed in
the main text, the equal investment strategy appears to be less effective, indicating
that the portfolio optimization methods may offer performance improvements over
naive diversification in this context.
A.2 Dataset-2: Stocks, Private Equities and Mutual Funds
Dataset-2 comprises 15 financial assets, categorized into five stocks, five public
funds, and five private equity funds. The data are sourced from the Wind Database
and the stock exchange, covering the period from January 19, 2024, to April 9, 2024.
These assets span a broad range of industries, including medical equipment, port
operations, cultural entertainment, the low-carbon economy, new energy vehicles,
and biomedicine. The method of selecting pre-selected assets is similar to that of
Dataset-1, which is random selection from high-quality asset pools across diverse
industries.
The selected assets in Dataset-2 are listed as follows:
–
–
–
–
–

Stocks:Kweichow Moutai Co., Ltd (600519.SH)
Jiangxi Guoke Defence Group Co., Ltd (688543.SH)
NINGBO OCEAN SHIPPING Co., Ltd (601022.SH)
Well Lead Medical Co., Ltd (603309.SH)
Shanghai International Port (600018.SH)

– Public Funds:CICC Science and Technology Innovation Theme (501080.
OF)
– China Merchants CSI Baijiu (161725.OF)
– Yi Fangda CSI Mainland Low Carbon Economy ETF (516070.OF)
– Huitianfu CSI New Energy Automobile Industry C (501058.OF)

13

Solving Multiple Discretization Portfolio Optimization Problem with…

– Huaan Guozheng Bio-Pharmaceutical ETF (159508.OF)
–
–
–
–
–

Private Equity Funds:Barrow Steady No. 1 (XT1613496.XT)
Baqisuo Endurance Steady No. 1 (XT1519228.XT)
Haiwei Quantitative No. 1 (XT1623529.XT)
Hanxin No. 1 (XT1410420.XT)
Yitong Growth (XT1510216.XT)Similarly, we conducted a backtest of Dataset-2 under the equal investment strategy. The corresponding results are
RET = 0.005, ACC = 1.001, Sharpe = −0.159, and Sortino = 0.051.
The backtesting indicates that the equal investment strategy has a slight probability of negative returns, approaching 0. This also suggests that dataset-2
exhibits randomness and volatility.

All data were sourced from the public database WIND.These two data selections
reflect a real-world situations where assets of discrete choices of buy-in amount are
present in our candidate for portfolio optimization. These two datasets highlight
the complexity and volatility of formulating short-term trading strategies. Unlike
long-term studies, macro trends fail to give an excellent trading strategy. Developing short-term trading strategies with significant fluctuations and randomness poses
greater challenges, emphasizing the complexity.

B Introduction to the Evaluation Indicators of Backtest Portfolio
Optimization Strategy
The rate of return is a fundamental metric for assessing investment performance,
representing the value growth of an investment over a specific period. It is typically
expressed as a ratio over time and calculated as follows (Cartea et al., 2015; Jordan
et al., 2003):
R(t) =

P (t) − P (t − 1) + D(t)
,(11)
P (t − 1)

where P(t) denotes the end-of-period price at time t, and D(t) represents any dividends or interest received at t. The rate of return R(t) serves as a core indicator for
evaluating investment performance.
Net Asset Value (NAV) (Williams, 1938) is a commonly employed measure for
assessing the value of an investment portfolio. It is calculated by subtracting total
liabilities from total assets. The formula for NAV is:
N AV (t) = N AV (t − 1) × (1 + R(t)),

(12)

where NAV(t) represents the net asset value at time t, and R(t) is the rate of return. In
practical applications, NAV is widely used in fund valuation to compute daily returns
per share or per fund, making it particularly suitable for evaluating the daily performance of multi-asset portfolios.

13

H. Wei et al.

The rate of return (RET) (Cartea et al., 2015; Markowits, 1952) standardizes the
cumulative return over a specific investment period, Nt , into an equivalent annualized rate. It is calculated using:
RET =

[N
∏t

] 252
Nt

(1 + R(t))

t=1

− 1,(13)

where Nt is the total number of trading days in the investment period. Notably, in this
study, RET represents the end-of-period return rather than daily returns (e.g., Fig. 4).
Accumulated return (ACC) (Cartea et al., 2015) reflects the total return of an
investment over a period, incorporating the effects of compounding and reinvestment. It is computed as:
ACC =

Nt
∏

t=1

(1 + R(t)) − 1,

(14)

where R(t) is the return at time t. ACC is particularly effective for evaluating longterm investment performance.
The Sharpe ratio, introduced by William Sharpe, is a widely-used metric for assessing risk-adjusted returns (Sharpe, 1966). It compares the excess return—defined as
the return above a risk-free rate—to the total investment risk, measured by return
volatility:
Sharpe =

RET − Rf
,(15)
σRET

where RET is the value from Eq. 13, Rf is the risk-free rate, and σRET is the standard
deviation of returns. A higher Sharpe ratio indicates more favorable risk-adjusted performance. In this analysis, we set Rf = 0.03 to reflect a realistic long-term estimate
of the risk-free rate in developed markets.
The Sortino ratio refines the Sharpe ratio by focusing solely on downside risk (Sortino & Van Der Meer, 1991). Downside risk, σD , is the standard deviation of negative
returns and is defined as:


N
1 
2
σD = 
(min(RETi , 0)) ,
N i=1

(16)

where N is the number of periods and RETi is the return for period i. The Sortino
ratio is then calculated as:
Sortino =

13

RET − Rf
.
σD

(17)

Solving Multiple Discretization Portfolio Optimization Problem with…

To emphasize the penalization of losses alone, we adopt a conservative assumption
of Rf = 0 when computing the Sortino ratio. This convention is commonly used in
practice to isolate downside volatility without attributing any baseline reward to riskfree investment.
In this study, NAV is used to monitor real-time portfolio changes and evaluate performance over short time horizons. The four metrics—RET, ACC, Sharpe,
and Sortino—are employed to assess portfolio optimization strategies at the end of
the investment period. This comprehensive evaluation framework supports more
informed and effective investment decision-making.
B.1 Framework of the Quantum–Classical Hybrid Algorithm (QCHA)
The goal of this study is to design an investment strategy that remains effective across
a wide spectrum of assets and realistic investment constraints. We cast the multiplediscrete portfolio-selection problem as a quadratic-unconstrained binary optimization (QUBO) task. After collecting the closing-price data of the chosen assets, we
compute their return vectors and covariance matrices, then embed the portfolio
objective and its constraints into the QUBO matrix Q. Because today’s quantum processors offer only a limited number of physical qubits, we adopt a quantum–classical hybrid approach that partitions the large QUBO into smaller sub-problems, each
small enough to run accurately on quantum hardware. The overall workflow is summarized in Algorithm 1.
Algorithm 1 HybridQUBOSolve: quantum–classical algorithm for large QUBOs

Within each iteration, the impact index

(
)
Ii (x; Q) = f x1 , . . . , xi ⊕ 1, . . . , xN ; Q − f (x; Q),(18)

13

H. Wei et al.

measures the change in objective value when bit xi is flipped (Booth et al., 2017;
Atobe et al., 2021). Variables with similar impact indices are deemed highly correlated and grouped together, which yields sub-problems capturing the most influential interactions. Each sub-matrix subQ is then solved on D-Wave’s Advantage 4.1
annealer via the D-Wave cloud, following the partition-and-iterate strategy of Booth
et al. (2017). After the sub-solutions are stitched back into a global vector, a classical local search—such as tabu search or greedy descent—refines the result, updates
the incumbent best solution, and the process repeats until convergence. All classical
computations were run on a quad-core Intel i5-8265U laptop under 64-bit Windows
11, and all code was written in Python 3.10.13. This hybrid scheme therefore leverages quantum hardware where it is most effective—on tightly scoped, high-fidelity
sub-tasks—while retaining the scalability and flexibility of classical optimization for
global coordination and convergence.

C Classical Computational Methods
C.1 Introduction to Classical Optimization Solution Algorithms
In this study, four classical algorithms are utilized as benchmarks for evaluating quantum algorithms: Gurobi, Simulated Annealing (SA), Tabu Search (TS), and Steepest
Descent (SD). These algorithms are frequently used to address combinatorial mathematical optimization and operations research problems, known for their universality
and efficiency. Additionally, they have significant applicability in the financial sector,
offering significant practical relevance. Subsequently, we will discuss the fundamental principles and financial application scenarios of these four classical algorithms.
Firstly, the Gurobi optimizer, as a well-known commercial solver, can efficiently
handle various combinatorial optimization problems with both discrete and continuous
variables. Gurobi’s solvers and cloud platform are capable of efficiently solving combinatorial optimization mathematical models. The QUBO-based multi-discretized asset
portfolio optimization model proposed in this article is fully compatible with Gurobi.
As a non-open-source commercial software, Gurobi integrates various algorithms to
solve optimization problems, but its internal algorithmic processes and methods remain
proprietary. Nevertheless, available literature indicates that Gurobi demonstrates excellent solver performance and is widely utilized in the field of finance (Karakalidis &
Sifaleras, 2016; Min et al., 2023; Pouzada, 2019). In addition, Gurobi solvers are widely
used in other field, such as biomedical (Muley, 2021; Yevseyeva et al., 2019), production scheduling (Cortés et al., 2024), power dispatching (Germscheid et al., 2023).
Simulated Annealing (SA) is a probabilistic technique used to approximate the
global optimum of a given function. SA is effective in locating the global optimum,
particularly when the search space is discrete. In 1983, Kirkpatrick et al. (1983) applied
this technique to solve the traveling salesman problem, subsequently coining the term
”simulated annealing.” Tabu search (TS) is a metaheuristic search method employing
local search methods used for mathematical optimization. Tabu search enhances the
performance of local search by relaxing its basic rule, which discourages revisiting

13

Solving Multiple Discretization Portfolio Optimization Problem with…

previously-visited solutions. It was created by Fred W. Glover in 1986 Glover (1986).
Gradient descent is a method for unconstrained mathematical optimization, which is a
first-order iterative algorithm for minimizing a differentiable multivariate function. In
this work, we utilize the stochastic gradient descent (SGD) algorithm (Bottou, 1998) as
a solver for solving portfolio optimization problems, which is also a widely employed
tool in contemporary machine learning. The above three classic algorithms for solving optimization problems are also widely applied across various industries, such as
finance(Doğan et al., 2024), industrial task optimization, and flight optimization.
C.2 Experimental Results of Classical Algorithms
For classical algorithms used to solve COPs, particularly heuristic approaches, the
quality of solutions is highly sensitive to hyperparameter settings and the compatibility between the algorithm and the specific problem instance. Consequently, careful
tuning of hyperparameters is crucial for achieving high-quality results and should be
tailored to the characteristics of each problem.
In Section 4, we utilize four classical algorithms as benchmarks to evaluate the
performance of our proposed quantum algorithm. In the main text, hyperparameters
are selected to reflect the optimal performance of each classical solver. This appendix subsection provides a detailed account of classical algorithm performance under
varying hyperparameter configurations.
Figures 6 and 7 display the results of solving a portfolio optimization problem
on Dataset-1 and Dataset-2, respectively, using classical algorithms under different
hyperparameter configurations. Each scatter point in the figures corresponds to an
outcome under a specific parameter setting. Due to visualization constraints, only 2–3
hyperparameters are shown. Based on the initial scatter results, we performed further
fine-tuning to identify the best-performing solution, indicated by the red triangle.
These optimal solutions are reported in the main text as representative benchmarks
for each algorithm. For comparison, the QCHA algorithm’s results are overlaid as a
light-blue plane in each figure. The legend also summarizes the best metric values
achieved by both QCHA and the classical solvers.
The alphabetical labels (a)–(d) correspond to the four classical solvers: (a) Gurobi,
(b) TS, (c) SA, and (d) SD, with each solver displayed in a separate row of the figure.
For the Gurobi solver, we tune two hyperparameters: Time_limit, which specifies the
maximum runtime in seconds (higher values allow more time to prove optimality
but may increase computation costs), and cuts, which controls the aggressiveness of
cutting-plane strategies used to tighten the LP relaxation. Disabling cuts can yield
faster approximate solutions, while enabling stronger cuts may lead to faster convergence on harder problems.
For TS, SA, and SD algorithms, common hyperparameters include initial_states
and num_reads. The initial_states parameter sets the number of distinct starting
points used to initialize the solver, promoting diversity in the search and reducing
sensitivity to poor initial guesses. The num_reads parameter determines how many
times the solver independently attempts to find a solution; each run is performed from
scratch, and the best result is retained. Increasing this value improves robustness and
solution quality but scales linearly with computational time.

13

H. Wei et al.
(a1)

(a2)

(a3)

(a4)

(b1)

(b2)

(b3)

(b4)

(c1)

(c2)

(c3)

(c4)

(d1)

(d2)

(d3)

(d4)

Fig. 6 Scatter plot illustrating the results of hyperparameter tuning for classical algorithms on Dataset-1. Blue points represent investment portfolio strategies and their corresponding back-testing metrics under different parameter configurations. The red triangle denotes the best-performing solution
identified by the current classical algorithm. The light blue plane indicates the optimal results achieved
by the QCHA algorithm. The X and Y axes represent tunable hyperparameters, while the Z axis shows
the value of the back-testing metric. Numerical indices correspond to evaluation metrics: (1) RET, (2)
ACC, (3) SHARPE, and (4) Sortino. Alphabetical indices denote classical solvers: (a) Gurobi, (b) TS,
(c) SA, and (d) SD

Specifically for the SA algorithm, we additionally tune the annealing schedule by
varying the inverse-temperature range, denoted as beta_range = (βmin , βmax ). The
lower bound βmin (corresponding to a high temperature) allows more frequent acceptance of worse solutions at the start, enabling global exploration, while the upper
bound βmax (low temperature) enforces greedy descent toward a local minimum in
later stages. The tested schedules include: (0.1, 4.2), (0.2, 3.8), (0.2, 3.8), (0.3, 3.5),
(0.4, 3.2), and (0.5, 3.0). These schedules balance exploration and exploitation and
help prevent premature convergence. A rule of thumb in tuning βrange is to begin

13

Solving Multiple Discretization Portfolio Optimization Problem with…
(a1)

(a2)

(a3)

(a4)

(b1)

(b2)

(b3)

(b4)

(c1)

(c2)

(c3)

(c4)

(d1)

(d2)

(d3)

(d4)

Fig. 7 Scatter figure by adjusting hyper-parameters of the classical algorithms on Dataset-2

with an initial acceptance rate around 80% and cool down until the acceptance rate
drops below 1%.

D Supplementary Materials for Experimental Results
In this section, we present detailed experimental results, including the allocation proportions of the optimal strategies and the back-testing results. Additionally, we offer
further analysis and discussions.
D.1 Using Six Algorithms to Solve PO Problem on Dataset-1
In this study, we present the results of portfolio optimization conducted using six
distinct algorithms on Dataset-1. Here, we present the portfolio allocations resulting
from each algorithm, as illustrated in Table 1. The corresponding back-test index

13

Table 1 The allocation proportion of the optimal portfolio strategies on Database-1
Algorithms
600017SH
300148SZ
002451SZ
601919SH
000539SZ
600830SH
600763SH
601008SH
600519SH
000858SZ
QCHA
0.0
0.097
0.0
0.0
0.258
0.032
0.258
0.323
0.0
0.032
Gurobi
0.0
0.129
0.0
0.0
0.258
0.0
0.194
0.29
0.0
0.129
QA
0.0
0.161
0.0
0.0
0.161
0.065
0.29
0.194
0.032
0.097
TS
0.0
0.065
0.0
0.0
0.225
0.0
0.258
0.323
0.032
0.097
SA
0.0
0.065
0.032
0.0
0.258
0.097
0.161
0.129
0.0
0.258
SD
0.065
0.097
0.0
0.0
0.194
0.032
0.194
0.225
0.0
0.193
These strategies are calculated by six different algorithms, such as QCHA, Gurobi, QA, TS, SA, and SD, when the total number of discrete independent variables used
in constructing model is 50

H. Wei et al.

13

Solving Multiple Discretization Portfolio Optimization Problem with…
Table 2 Performance of portfolio optimization given by six
algorithms based on Dataset-1

Algorithms Hamiltonian
RET
ACC
Sharpe Sortino
QCHA
-9.999647587 0.890 1.227 3.130
6.242
Gurobi
-9.9997203
0.812 1.211
2.974
6.028
QA
-9.999394085 0.781 1.204 2.728
6.246
TS
-9.999600907 0.843 1.217 2.988
6.491
SA
-9.999503829 0.715 1.189 2.608
5.098
SD
-9.99957352
0.690 1.184 2.574
5.440
There are five columns in the table, and each column is a
measurement index, including Hamiltonian, RET, ACC, Sharpe
Ratio, and Sortino Ratio. Each row represents the numerical results
calculated using six different algorithms, respectively

results for the schemes generated by the different algorithms are displayed in Table
2. According to Table 1, several poorly performing stocks, such as 600017SH and
002451SZ, were excluded from investment when applying the QCHA, Gurobi, and
QA algorithms. In contrast, the other classical algorithms failed to identify and avoid
these poorly performing stocks. The solution provided by the QCHA algorithm
exhibits minor variations in allocation proportions compared to Gurobi’s results.
Consequently, the QCHA algorithm ultimately yields superior outcomes, underscoring the advantages of quantum computing, as evidenced in Table 2.
The QCHA algorithm outperforms all other algorithms across every metric. It
achieves the highest results in three metrics: RET = 0.890, ACC = 1.227, and
Sharpe = 3.13, suggesting that it is the most effective algorithm for portfolio optimization among those tested. The Sortino ratio provided by QCHA ranks second,
slightly lower than that of the TS algorithm. The classical algorithms, TS and Gurobi,
demonstrate moderate performance, which is slightly inferior to that of QCHA, indicating a less favorable risk-adjusted return. The remaining three algorithms exhibit
significant disadvantages across these indicators. Regarding the QA algorithm implemented by D-Wave’s quantum annealing machine, its performance surpasses that of
the SD SA algorithm, though the margin is modest. In summary, the QCHA algorithm
emerges as an effective method for portfolio optimization, outperforming two commonly used classical algorithms: TS and Gurobi. Additionally, QCHA is a significantly more robust hybrid algorithm compared to simple quantum annealing.
D.2 Using 5 Algorithms to Solve PO Problem in Dataset-2
The allocation ratios of the portfolio optimization strategy on Dataset-2 are presented
in Table 3. A comparison reveals that the strategies generated by each algorithm are
not entirely identical. Nevertheless, the top three performing algorithms, QCHA, TS,
and Gurobi, exhibit a shared tendency to avoid investing in certain underperforming stocks. This observation suggests that our model possesses strong capabilities in
addressing practical financial investment challenges.
According to Table 4, the Sortino ratio obtained by QCHA is the best. Moreover,
the QCHA algorithm ranks second in terms of ACC value and Sharpe ratio, trailing
the best by only 0.45% and 0.2%, respectively. Therefore, QCHA remains the best
algorithm. Overall, Gurobi, QCHA, and TS are still significantly better than the others according to the results of backtesting, each with its strengths and weaknesses.

13

Table 3 The allocation proportions of the optimal portfolio strategies are derived from five different algorithms, utilizing a total of 128 discrete independent variables
Algorithms 6005
6885
6010
6033
6000
5010
1617
5160
5010
1595
XT1613 XT1519 XT1623 XT1410 XT1510
19.SH 43.SH 22.SH 09.SH 18.SH 80.OF 25.OF 70.OF 58.OF 08.OF 496.XT
228.XT
529.XT
420.XT
216.XT
QCHA
0.016
0.348
0.021
0.001
0.0
0.044
0.454
0.016
0.0
0.0
0.0
0.0
0.0
0.0
0.1
Gourbi
0.0
0.409
0.007
0.0
0.0
0.001
0.371
0.052
0.06
0.0
0.0
0.0
0.0
0.0
0.1
TS
0.0
0.0
0.0
0.0
0.0
0.063
0.36
0.034
0.228
0.015
0.1
0.0
0.0
0.1
0.1
SA
0.049
0.094
0.033
0.002
0.003
0.048
0.323
0.113
0.135
0.0
0.0
0.0
0.1
0.0
0.1
SD
0.033
0.464
0.049
0.014
0.013
0.004
0.108
0.108
0.001
0.006
0.1
0.0
0.0
0.1
0.0
This analysis is based on Dataset-2, which includes three types of assets with varying degrees of dispersion

H. Wei et al.

13

Solving Multiple Discretization Portfolio Optimization Problem with…
Table 4 The performance
indicators for portfolio optimization, calculated using five
algorithms in Dataset-1, are
summarized in the table

Algorithms Hamiltonian
RET
ACC
Sharpe Sortino
QCHA
-1000.017372 0.460 1.089 1.976
4.253
Gurobi
-1000.01746
0.487 1.094 1.912
4.051
TS
-1000.016794 0.279 1.057 1.980
3.096
SA
-1000.016798 0.280 1.057 1.986
3.833
SD
-1000.017077 0.336 1.068 1.062
2.022
This table consists of five columns, each representing a measurement
index: Hamiltonian, RET, ACC, Sharpe Ratio, and Sortino Ratio.
Each row displays the numerical results obtained from the five
different algorithms

Fig. 8 The allocation ratios of the investment strategy following portfolio optimization using the
QCHA algorithm are presented in this section. The experiments were conducted on Database-1, where
the stock codes of ten assets are labeled on the x-axis. The number of independent variables is set at (a,
b) N = 40 and (c, d)N = 50, respectively. Information regarding whether constraints are considered
in the model is indicated in the titles above each figure

13

H. Wei et al.

In this case, due to the number of independent variables exceeding hardware limitations, traditional quantum annealing algorithms cannot be executed. In summary,
QCHA is a very effective method for solving portfolio optimization problems.
D.3 Results of Portfolio Optimization with and Without Constraints
In the main paper, we compared the backtesting results of various algorithms under
two scenarios: considering and not considering constraints, with the number of independent variables set at 40 and 50, respectively. Due to the reduced solution space
and variations in boundary conditions, all evaluation indicators show a decrease of
approximately 10% compared to the results without constraints. Figure 8 illustrates
the optimal investment strategies provided by the QCHA algorithm under different
conditions.
As shown in Fig. 8, the number of stocks available for investment decreases,
while the concentration of investments increases after considering the constraints.
Additionally, as the number of qubits increases, the changes in the allocation pattern of investment proportions become more subtle when comparing allocations with
different numbers of qubits used. This finding demonstrates that the QCHA algorithm possesses strong capabilities. Assuming we have obtained an optimal solution
without considering constraints, introducing additional constraints and relaxation
variables does not yield significant differences from it. Typically, the introduction
of extra constraints leads to a deterioration in the optimal solution as the number of
qubits increases, particularly because the problem size grows exponentially with the
increase in qubits. Therefore, it is significant that the QCHA algorithm can still maintain equivalent capabilities in solving portfolio optimization problems. In summary,
QCHA outperforms other classical algorithms.

Acknowledgements We are very grateful for the financial support provided by Beijing Science and Technology Plan, Quantum Financial Cloud Platform Key Technology Research and Development and Demonstration Application (Z231100001323001). We thank Gaoxiang Tang for the help in discussions. We
thank D-Wave’s technical team for providing cloud platform computing resources.
Author Contributions Haijing Wei, Wending Zhao, and Lin Yao conceived the experiments and theory.
Yanbo J. Wang and Qi Xu conducted the experiments. Haijing Wei and Wending Zhao analysed the results.
Wending Zhao, and Lin Yao wrote this manuscript. All authors reviewed the manuscript.
Data and code availability All of the data are available upon request. Source codes covered in this paper
can be made available upon request.

Declarations
Competing interests All of the authors declare on behalf of all authors that there are no competing interests.

13

Solving Multiple Discretization Portfolio Optimization Problem with…
Open Access This article is licensed under a Creative Commons Attribution-NonCommercialNoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution
and reproduction in any medium or format, as long as you give appropriate credit to the original author(s)
and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed
material. You do not have permission under this licence to share adapted material derived from this article
or parts of it. The images or other third party material in this article are included in the article’s Creative
Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in
the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or
exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view
a copy of this licence, visit ​h​t​t​p​:​/​​/​c​r​e​a​​t​i​v​e​c​o​​m​m​o​n​​s​.​o​r​g​​/​l​i​c​e​​n​s​e​s​/​b​​y​-​n​c​​-​n​d​/​4​.​0​/.

References
Abdel-Salam, M., Hu, G., Çelik, E., Gharehchopogh, F. S., & El-Hasnony, I. M. (2024). Chaotic rime
optimization algorithm with adaptive mutualism for feature selection problems. Computers in Biology and Medicine, 179, Article 108803.
Abedi, M., & Gharehchopogh, F. S. (2020). An improved opposition based learning firefly algorithm with
dragonfly algorithm for solving continuous optimization problems. Intelligent Data Analysis, 24(2),
309–338.
Ait-Saadi, A., Meraihi, Y., Soukane, A., Ramdane-Cherif, A., & Gabis, A. B. (2022). A novel hybrid chaotic aquila optimization algorithm with simulated annealing for unmanned aerial vehicles path planning. Computers and Electrical Engineering, 104, Article 108461.
Araya, R. (2021). Enriching elementary school mathematical learning with the steepest descent algorithm.
Mathematics, 9(11), 1197.
Atobe, Y., Tawada, M., & Togawa, N. (2021). Hybrid annealing method based on subqubo model extraction with multiple solution instances. IEEE Transactions on Computers, 71(10), 2606–2619.
Baldwin, C. H., Mayer, K., Brown, N. C., Ryan-Anderson, C., & Hayes, D. (2022). Re-examining the
quantum volume test: Ideal distributions, compiler optimizations, confidence intervals, and scalable
resource estimations. Quantum, 6, 707.
Beal, L. (2021). GEKKO Optimization Suite. Accessed: 2024-07-16. ​h​t​t​p​s​:​/​/​g​e​k​k​o​.​r​e​a​d​t​h​e​d​o​c​s​.​i​o​/​e​n​/​l​a​
t​es​ ​t/​​​​​
Booth, M., Reinhardt, S. P., & Roy, A. (2017). Partitioning optimization problems for hybrid classical.
quantum execution. Technical Report, 01–09
Bottou, L. (1998). Online algorithms and stochastic approximations. Online learning in neural networks
Brandhofer, S., Braun, D., Dehn, V., Hellstern, G., Huls, M., Ji, Y., Polian, I., Bhatia, A. S., & Wellens, T.
(2022). Benchmarking the performance of portfolio optimization with QAOA. Quantum Information
Processing. https://doi.org/10.1007/s11128-022-03766-5
Buonaiuto, G., Gargiulo, F., De Pietro, G., Esposito, M., & Pota, M. (2023). Best practices for portfolio optimization by quantum computing, experimented on real quantum devices. Scientific Reports,
13(1), 19434.
Cartea, Á., Jaimungal, S., & Penalva, J. (2015). Algorithmic and High-frequency Trading. Cambridge
University Press,???
Chen, Y. (2021). [retracted] BP neural network based on simulated annealing algorithm optimization for
financial crisis dynamic early warning model. Computational Intelligence and Neuroscience,2021(1),
4034903.
Cortés, P., Escudero-Santana, A., Barbadilla-Martin, E., & Guadix, J. (2024). A production-inventory
model to optimize the operation of distributed energy resource networks in a rolling horizon. Heliyon.​
h​t​t​p​s​:​​/​/​d​o​i​​.​o​r​g​/​1​​0​.​1​0​​1​6​/​j​.​​h​e​l​i​y​​o​n​.​2​0​2​​4​.​e​3​​9​9​0​0
Cura, T. (2021). A rapidly converging artificial bee colony algorithm for portfolio optimization. Knowledge-Based Systems, 233, Article 107505.
De Moraes, M. B., & Coelho, G. P. (2022). A diversity preservation method for expensive multi-objective
combinatorial optimization problems using novel-first tabu search and moea/d. Expert systems with
applications, 202, Article 117251.
Doğan, S., Bezgin, M. S., & Karaçayır, E. (2024). The portfolio optimization with simulated annealing
algorithm: An application of Borsa Istanbul. Gazi İktisat ve İşletme Dergisi,10(1), 1–15.

13

H. Wei et al.
DWAVE. (2023). Software development kit: Dwaver-sampler. ​h​t​t​p​s​:​​/​/​g​i​t​​h​u​b​.​c​o​​m​/​d​w​​a​v​e​s​y​​s​t​e​m​s​​/​d​w​a​v​e​​-​s​
a​m​​p​l​e​r​s
Eraña-Díaz, M. L., Cruz-Chávez, M. A., Rivera-López, R., Martínez-Bahena, B., Cruz-Rosales, M. H.,
et al. (2020). Optimization for risk decision-making through simulated annealing. IEEE Access,8,
117063–117079.
Ganie, A. G., & Dadvandipour, S. (2023). From big data to smart data: A sample gradient descent approach
for machine learning. Journal of Big Data,10(1), 162.
Germscheid, S. H., Röben, F. T., Sun, H., Bardow, A., Mitsos, A., & Dahmen, M. (2023). Demand response
scheduling of copper production under short-term electricity price uncertainty. Computers & Chemical Engineering,178, Article Article 108394.
Glover, F. (1986). Future paths for integer programming and links to artificial intelligence. Computers &
Operations Research,13(5), 533–549.
Glover, F. (1990). Tabu search: A tutorial. Interfaces, 20(4), 74–94.
Goldberg, D. E., Korb, B., & Deb, K. (1989). Messy genetic algorithms: Motivation, analysis, and first
results. Complex Systems,3(5), 493–530.
Guo, S. A., Wu, Y. K., Ye, J., Zhang, L., Lian, W. Q., Yao, R., Wang, Y., Yan, R. Y., Yi, Y. J., & Xu,
Y. L. (2024). A site-resolved two-dimensional quantum simulator with hundreds of trapped ions.
Nature,630(8017), 613–618.
Gurobi. (2018). Gurobi Optimization. https://github.com/Gurobi
He, Y., Jia, T., & Zheng, W. (2023). Tabu search for dedicated resource-constrained multiproject scheduling to minimise the maximal cash flow gap under uncertainty. European Journal of Operational
Research, 310(1), 34–52.
Jordan, B. D., Ross, S. A., & Westerfield, R. W. (2003). Fundamentals of corporate finance
Jurcevic, P., Javadi-Abhari, A., Bishop, L. S., Lauer, I., Bogorin, D. F., Brink, M., Capelluto, L., Günlük,
O., Itoko, T., Kanazawa, N., Kandala, A., Keefe, G. A., Krsulich, K., Landers, W., Lewandowski, E.
P., McClure, D. T., Nannicini, G., Narasgond, A., Nayfeh, H. M.,… Gambetta, J. M. (2021). Demonstration of quantum volume 64 on a superconducting quantum computing system. Quantum Science
and Technology, 6(2), Article 025020. https://doi.org/10.1088/2058-9565/abe519
Kalra, A., Qureshi, F. I., & Tisi, M. (2018). Portfolio asset identification using graph algorithms on a quantum annealer. Machine Learning eJournal
Karakalidis, A., & Sifaleras, A. (2016). Solving portfolio optimization problems using ampl. In: Operational Research in Business and Economics: 4th International Symposium and 26th National Conference on Operational Research, Chania, Greece, June 2015, pp. 167–184. Springer
King, A. D., Suzuki, S., Raymond, J., Zucca, A., Lanting, T., Altomare, F., Berkley, A. J., Ejtemaee, S.,
Hoskinson, E., & Huang, S. (2022). Coherent quantum annealing in a programmable 2000-qubit
Ising chain. Nature Physics,18, 1324–1328. https://doi.org/10.1038/s41567-022-01741-6
Kirkpatrick, S., Gelatt, C. D., Jr., & Vecchi, M. P. (1983). Optimization by simulated annealing. science,
220(4598), 671–680.
Lewis, A. L. (1988). A simple algorithm for the portfolio selection problem. Journal of Finance,43(1),
71–82.
Lu, Y., & Yang, J. (2024). Quantum financing system: A survey on quantum algorithms, potential scenarios
and open research issues. Journal of Industrial Information Integration. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​1​6​/​j​.​j​i​
i​.​2​0​2​4​.​1​0​0​6​6​3​​​​
Ma, Y., He, Z., Wang, N., & Demeulemeester, E. (2023). Tabu search for proactive project scheduling
problem with flexible resources. Computers & Operations Research,153, Article 106185.
Mahjoubi, A., Grinnemo, K.-J., & Taheri, J. (2022). An efficient simulated annealing-based task scheduling technique for task offloading in a mobile edge architecture. In: 2022 IEEE 11th International
Conference on Cloud Networking (CloudNet), pp. 159–167. IEEE
Mansouri, T., & Moghadam, M. R. S. (2021). Markowitz-based cardinality constrained portfolio selection
using asexual reproduction optimization (aro). arXiv:2101.03312
Markowits, H. M. (1952). Portfolio selection. Journal of finance,7(1), 71–91.
Markowitz, H. (1952). Portfolio selection*. The Journal of Finance,7(1), 77–91. ​h​t​t​p​s​:​​/​/​d​o​i​​.​o​r​g​/​1​​0​.​1​1​​1​1​/​j​
.​​1​5​4​0​-​​6​2​6​1​.​1​​9​5​2​.​​t​b​0​1​5​2​5​.​x
McGeoch, C. C. (2020). Theory versus practice in annealing-based quantum computing. Theoretical Computer Science,816, 169–183. https://doi.org/10.1016/j.tcs.2020.01.024
Min, L., Han, Y., Xiang, Y. (2023). A two-stage robust omega portfolio optimization with cardinality constraints. IAENG International Journal of Applied Mathematics,53(1)

13

Solving Multiple Discretization Portfolio Optimization Problem with…
Mugel, S., Abad, M., Bermejo, M., Sánchez, J., Lizaso, E., & Orús, R. (2021). Hybrid quantum investment
optimization with minimal holding period. Scientific Reports,11, Article 19587. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​
0​3​8​/​s​4​1​5​9​8​-​0​2​1​-​9​8​2​9​7​-​x​​​​
Mugel, S., Kuchkovsky, C., Sánchez, E., Fernández-Lorenzo, S., Luis-Hita, J., Lizaso, E., & Orús, R.
(2022). Dynamic portfolio optimization with real datasets using quantum processors and quantuminspired tensor networks. Physical Review Research,4, Article 013006. ​h​t​t​p​s​:​​​/​​/​d​o​​i​.​o​r​​g​/​​1​0​.​​1​1​​0​3​/​​P​h​y​s​
R​​e​v​R​e​s​e​​a​​r​c​​​h​.​4​.​0​1​3​0​0​6
Muley, V. Y. (2021). Mathematical programming for modeling expression of a gene using gurobi optimizer
to identify its transcriptional regulators. In: Modeling Transcriptional Regulation: Methods and Protocols, pp. 99–113. Springer,???
Nielsen, M. A., & Chuang, I. L. (2011). Quantum Computation and Quantum Information: 10th Anniversary Edition, pp. 171–352. Quantum Computation and Quantum Information: 10th Anniversary
Edition,???
Orra, A., Bhambu, A., Choudhary, H., Thakur, M., & Natarajan, S. (2025). Deep reinforcement learning
for investor-specific portfolio optimization: A volatility-guided asset selection approach. Technical
report
Orús, R., Mugel, S., & Lizaso, E. (2019). Quantum computing for finance: Overview and prospects.
Reviews in Physics,4, Article 100028. https://doi.org/10.1016/j.revip.2019.100028
Orús, R. (2014). A practical introduction to tensor networks: Matrix product states and projected entangled
pair states. Annals of Physics, 349, 117–158.
Orús, R. (2019). Tensor networks for complex quantum systems. Nature Reviews Physics, 1(9), 538–550.
Orús, R., Mugel, S., & Lizaso, E. (2019). Quantum computing for finance: Overview and prospects.
Reviews in Physics, 4, Article 100028.
Pouzada, M. A. T. B. V. (2019). Design of a supply chain network with financial considerations. PhD
thesis, Universidade do Porto (Portugal)
Prado, M. (2015). Generalized optimal trading trajectories: A financial quantum computing application.
Available at SSRN 2575184
Rosenberg, G., Haghnegahdar, P., Goddard, P., Carr, P. P., Wu, K., & Prado, M. L. (2015). Solving the
optimal trading trajectory problem using a quantum annealer. IEEE Journal of Selected Topics in
Signal Processing,10, 1053–1060.
Rubio-García, Á., Fernández-Lorenzo, S., García-Ripoll, J. J., & Porras, D. (2024). Accurate solution
of the index tracking problem with a hybrid simulated annealing algorithm. Physica A: Statistical
Mechanics and Its Applications,639, Article Article 129637.
Ruder, S. (2016). An overview of gradient descent optimization algorithms. arXiv:1609.04747
Ryan-Anderson, C., Brown, N., Baldwin, C., Dreiling, J., Foltz, C., Gaebler, J., Gatterman, T., Hewitt, N.,
Holliman, C., Horst, C., et al. (2024). High-fidelity and fault-tolerant teleportation of a logical qubit
using transversal gates and lattice surgery on a trapped-ion quantum computer. arXiv:2404.16728
Sharpe, W. F. (1966). Mutual fund performance. The Journal of business,39(1), 119–138.
Sheikh-Hosseini, M., & Hashemi, S. R. S. (2022). Connectivity and coverage constrained wireless sensor
nodes deployment using steepest descent and genetic algorithms. Expert Systems with Applications,
190, Article 116164.
Shinzato, T. (2018). Maximizing and minimizing investment concentration with constraints of budget and
investment risk. Physica A: Statistical Mechanics and Its Applications,490, 986–993.
Shor, P. W. (1994). Algorithms for quantum computation: discrete logarithms and factoring. In: Proceedings 35th Annual Symposium on Foundations of Computer Science, pp. 124–134. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​
.​1​1​0​9​/​S​F​C​S​.​1​9​9​4​.​3​6​5​7​0​0​​​​
Sofge, D. A. (2008). A survey of quantum programming languages: History, methods, and tools. Second
International Conference on Quantum, Nano and Micro Technologies (ICQNM 2008), 66–71
Song, Z., & Yang, C. (2023). An automatic learning rate schedule algorithm for achieving faster convergence and steeper descent. arXiv:2310.11291
Sortino, F. A., & Van Der Meer, R. (1991). Downside risk. The Journal of Portfolio Management,17(4),
27.
Vesselinova, N., Steinert, R., Perez-Ramirez, D. F., & Boman, M. (2020). Learning combinatorial optimization on graphs: A survey with applications to networking. IEEE Access,PP(99), 1–1
Williams, J. B. (1938). The theory of investment value. (No Title)
Woerner, S., & Egger, D. J. (2019). Quantum risk analysis. npj Quantum. Information,5(1), Article 15.
Xie, J., Li, X., Gao, L., & Gui, L. (2023). A hybrid genetic tabu search algorithm for distributed flexible
job shop scheduling problems. Journal of Manufacturing Systems, 71, 82–94.

13

H. Wei et al.
Yang, X.-S. (2009). Firefly algorithm, levy flights and global optimization. In: Research and Development
in Intelligent Systems XXVI: Incorporating Applications and Innovations in Intelligent Systems
XVII, pp. 209–218. Springer,???
Yevseyeva, I., Lenselink, E. B., Vries, A., IJzerman, A. P., Deutz, A. H., & Emmerich, M. T. (2019). Application of portfolio optimization to drug discovery. Information Sciences,475, 29–43.
Publisher's Note Springer Nature remains neutral with regard to jurisdictional claims in published maps
and institutional affiliations.

13

