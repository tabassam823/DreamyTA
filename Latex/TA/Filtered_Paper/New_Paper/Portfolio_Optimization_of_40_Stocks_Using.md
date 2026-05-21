arXiv:2007.01430v1 [q-fin.GN] 2 Jul 2020

Portfolio Optimization of 40 Stocks Using
DWaves Quantum Annealer
Chicago Quantum∗
email the authors
July 6, 2020

Contents
1 Introduction

2

2 Validity of the Formulation

3

3 Classical Methods
3.1 Brute Force . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.2 Genetic Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . .
3.3 Random Sampling . . . . . . . . . . . . . . . . . . . . . . . . . .
3.4 Heuristic Approach . . . . . . . . . . . . . . . . . . . . . . . . . .
3.5 Simulated Annealer as a Monte Carlo . . . . . . . . . . . . . . .

3
4
4
5
5
5

4 Using an Annealing Quantum Computer
4.1 The Optimal Portfolio . . . . . . . . . . . . . . . . . . . . . . . .
4.2 Developing the QUBO to Number of Assets in a Portfolio . . . .
4.3 Embedding, Scaling, and Hardware Considerations . . . . . . . .
4.4 Affine Transformations of the QUBO . . . . . . . . . . . . . . . .
4.5 Visualization . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

5
5
6
7
7
8

5 Results

9

6 Discussion and Conclusion

11

7 Thank You

16
Abstract

We investigate the use of quantum computers for building a portfolio
out of a universe of U.S. listed, liquid equities that contains an optimal set
∗ Jeffrey Cohen, Alex Khan, Clark Alexander

1

of stocks. Starting from historical market data, we look at various problem formulations on the D-Wave Systems Inc. D-Wave 2000QTM System
(hereafter called DWave) to find the optimal risk vs return portfolio; an
optimized portfolio based on the Markowitz formulation and the Sharpe
ratio, a simplified Chicago quantum ratio (CQR), then a new Chicago
quantum net score (CQNS). We approach this first classically, then by
our new method on DWave. Our results show that practitioners can use
a DWave to select attractive portfolios out of 40 U.S. liquid equities.

1

Introduction

The challenge we approach in financial portfolio optimization is to maximize
expected returns while minimizing variability of expected returns, or risk. This
is a buy and hold strategy and not a mid or high frequency trading strategy. It
relies on previous period risk, in our case one year of daily adjusted close data,
and the underlying variability and relationships of equities. We believe investors
can improve their chances by selecting the right combination of stocks.
Among the major challenges in financial portfolio optimization is “how does
an investor balance long term investments between expected return and volatility?” In this work we tackle this question from a variety of methods.This problem
is particularly well suited for an annealing solution, either classical simulated
thermal annealing, or quantum annealing since we wish to consider N equities in
which each equity may be included in a portfolio or not. This yields exactly 2N
possibilities. For a potential list of equities as small as 40, this becomes nearly
infeasible on a workstation. When we approach the entirety of the S&P 500, we
very quickly run into a solution space which is computationally infinite. That
is, we do not have enough memory in the observable universe to run through a
brute force solution.
This work is structured as follows: In §2 we begin our exploration with the
Sharpe ratio
wβE[Ra − Rb ] + Rb
Sa (w) =
(1)
σa
Where β is the ratio of Covariance of a portfolio with the market over the
variance of the entire market [3], Ra is the return of the collection of assets,
Rb is the risk free return, and σa is the standard deviation of the collection of
assets, and w is a vector of weights for assets in our portfolio.
We can also see the Sharpe ratio in matrix form as
Sa (w) =

wβE[Ra − Rb ] + Rb
1/2

[wt Covij w]

(2)

From here we develop the Chicago Quantum Ratio (CQR)
CQRa (w) =

2

w · Covim
σa

(3)

where Covim is the covariance of the ith asset against the entire market. This is
a slight improvement over the Sharpe ratio in terms of computation as we need
not consider nominal assets. Risk free investments have a near zero covariance
with the entire market.
We can also reformulate CQR in matrix form as
CQRa (w) =

w · Covim
1/2

[wt Covij w]

(4)

We explore these formulations by a variety of classical methods which one
will find in §3. Both formulations are ratios and thus neither is properly suitable
for a quantum annealing solution, as DWave requires a linear quadratic form.
We attempt to rectify this by exploring
ln(Sa ) = ln(E[Ra − Rb ]) − ln(σa )

(5)

This, however causes a different set of mathematical problems in formulating
a consistent quadratic form. Finally we settle on the Chicago Quantum Net
Score (CQNS) which is given by
CQNS(w; α) = V ar(Rw ) − E[Rw ]2+α

(6)

Where Rw is a weighted portfolio and α ∈ R In most experiments we choose
an equal weighting i.e. wi = 1/n where n is the number of assets included,
and we choose α near 1. These are not requirements, but they do make the
computations on DWave slightly easier. There is a wide open question as to
finding optimal weighting and optimal α.
We explain how to formulate a quadratic form for use on DWave in §4.
Finally in §5 and 6 we give our results visually and mathematically, and
discuss our future work.

2

Validity of the Formulation

In its current capacity DWave solves problems which are formulated in terms
of an Ising model. Thus our practical challenge is to provide for Dwave an acceptable model on which it may begin its computations. Consider the following
image 1
Our formulation has a propensity toward conservative side in investment
terms, however, is also demonstrates that the present formulations are near the
efficient frontier of investment portfolios. Thus from an empirical perspective
this formulation passes muster. We develop the method in more detail in §4.

3

Classical Methods

In this section we wish to give various formulations which we run on digital
computers. These methods are meant as benchmarking measures so that we
3

Figure 1: Comparison of CQR and CQNS scores against the Sharpe Ratio
may check whether the computations from the annealing quantum computer
are legitimate or if the annealing computer lands on local minima which are not
particularly deep.

3.1

Brute Force

For a smaller asset universe we are able to simply loop through all binary solutions. If given enough time one can brute force roughly 40 assets. This however
is best approached by an in-place in-time algorithm. If one attempts to build
all 2N portfolios first and simply loop through a list, one will run out of memory. An in-place algorithm eliminates the memory excess. An in-time algorithm
allows us to write out solutions in case of interruption. With brute force methods we can explicitly know the minimum possible energy level and thus verify
whether our formulation for an annealing quantum computer is valid.

3.2

Genetic Algorithm

Our genetic algorithm solution gets to a local minimum deeper than our Monte
Carlo method with 950M samples, and does so very quickly. Our difficulty is in
tuning the parameters for number of evolutionary steps, probability of elitism,
4

and size of initial population. Even with essentially random guesses at these
parameters, our genetic algorithm reaches a low enough energy level so that we
can determine whether the quantum annealing solutions are legitimate.

3.3

Random Sampling

As mentioned earlier §3.1 a 40 asset portfolio is slightly more than a workstation
can handle without an in-place algorithm. Thus we randomly sample as much
as we can. We are able to sample roughly 229 portfolios of a potential
240 This
√
means most of our effort is spent around portfolios of size 40 ± 40. Percentage
wise this doesn’t cover much of the entire spectrum, but we approach 0.4% of
the mid sized portfolio. Specifically by Stirlong’s approximation we know.
 
1 40
1
P (|X| = 20) = 40
≈√
≈ 0.12
20
2
20π
On the other hand 229 /240 ≈ 0.0005. So we get about an 8 fold lift around the
middle portfolios.

3.4

Heuristic Approach

After running a number of the previous classical methodologies we notice that
certain stocks appear most often within the best performing portfolios. We
name these stocks “All stars.” Similarly we notice several stocks which appear
most often in the worst performing portfolios. We name these “Dog stars.” The
heuristic approach is to attempt building portfolios of mostly All stars with the
addition of a few extra items. This works well as a seeding algorithm for other
probabilistic methods and will inform our approach when we attempt to solve
the portfolio optimization problem on quantum circuit and trapped ion models.

3.5

Simulated Annealer as a Monte Carlo

The original test of our problem comes in the form of a simulated (thermal)
annealing solution. Using statistics of random matrices we are able to tune the
parameters of our simulated annealing solution to deliver very deep local minima. Additionally, this style solution only covers minimizing risk in a portfolio.
Based on the cooling rate of the thermal annealing and the number of attempts
per solution we use simple statistics from sampling theory to provide a measure
of goodness.

4

Using an Annealing Quantum Computer

4.1

The Optimal Portfolio

The optimal portfolio in our case is one which maximizes the Sharpe ratio.
However, as presented the Sharpe ratio of a portfolio is not computable as a

5

QUBO. The main thrust of this research is, in fact, how to formulate a QUBO
which, when presented to DWave produces similar results to the classical Sharpe
ratio. Consider the following, The Sharpe ratio is defined above in 1
Sa =

βE[Ra − Rb ] + Rb
σa

The numerator can be expressed as a simple dot product, i.e.
X
µi wi
where µi and wi are the expected return and the relative weight of the ith
asset, respectively. The denominator can be expressed as the square root of a
quadratic form, i.e.
1/2
X
X
 1
v i qi + 2
covij qi qj 
|U|2
i<j


Where qi ∈ {0, 1} is a binary classifying whether the ith asset is in the
portfolio or not, vi is the variance, and covij is the covariance term between
asset i and j. One will immediately recognize this as σa as in the initial formula.
One will also recognize that the Sharpe ratio is not a proper quadratic form, and
thus not suitable for DWave in its current iteration. We find that the Chicago
Quantum Net Score (CQNS) solves this problem and can be presented as a
quadratic form.

4.2

Developing the QUBO to Number of Assets in a Portfolio

Consider a universe U of N assets. When dealing with a single asset portfolio,
we only consider the linear terms in a QUBO. In particular when we have a
lower triangular matrix or a zero diagonal matrix, products of the form
eti Qei = 0
Thus we pick off only the linear terms. In this case, we concisely model the
inverse Sharpe Ratio on qubits and use a penalty on the couplers. DWave finds
one-asset portfolios with the highest ratios.
Moving to two or more assets we have substantially more work to do. Looking at a single asset, there are no covariance terms to deal with, and we can
embed the inverse Sharpe ratio directly onto the qubits. We create a unique
QUBO for each size portfolio evaluated {2, . . . , N } by applying the weights directly toPthe matrix, so qi and qj can remain binary. We divide the linear terms
by N ( wi = 1) and apply the linear affine transformation. We divide the
variance terms (the diagonal entries) by N 2 ∗ (N − 1) to avoid duplication, and
divide the covariance terms (off diagonal entries) by N 2 to avoid duplication.
6

We then apply the quadratic affine transformation. Then we assemble the matrix and reverse the sign on the linear terms. Finally, we apply a scale factor
(−1, 1) to the QUBO and write it into our N × N × N matrix for processing by
DWave

4.3

Embedding, Scaling, and Hardware Considerations

We embed the CQNS on DWave by writing the expected returns onto the linear
terms, both variance (diagonal) and covariance (off diagonal) onto the quadratic
terms. From here the DWave inspector shows how the system encodes and
embeds assets onto physical qubits. An attempt at changing the formulation
by manually embedding terms to respect a reordering of assets does not yield
substantial improvements in performance thus we use DWaves automated embedding functions.
As we increase our asset size, we see that for a fully connected QUBO DWave
requires multiple qubits in chains to leverage the available connections in other
groups of the chimera structure. Increasing our portfolio size above 40 would
result in increasing qubit counts utilized to support multiple chains, and the
potential for increased chain breaks. We see consistent results with 40 assets
when we tune the “Chain Strength and scale factors.
We attempt to reduce our resource cost by removing links between assets that
are thought to be insignificant due to low correlation values in our calculations.
However, we create inaccurate results in this formulation and from this point
we shall avoid this method of reducing our resource cost.
We adjust DWaves chain strength parameter to see adequate results with low
volume of chain breaks. DWave defaults to a chain strength of 1, and we found
we could reduce chain breaks by setting chain strength to values as high as 15.
However, a chain strength of 1 provides more valid answers to our particular
QUBO.
We control the qubit value scaling to avoid unequal scaling of linear and
quadratic terms. Dwave’s native scaling, if left untouched would reduce the
accuracy of our scores. We scale the values we send to DWave within the
QUBO. The process of scaling naturally moves us toward scaling our values by
a hyperbolic tangent. In particular, we find the original scale of our values has
some very small values owing to covariance matrices having a zero eigenvalue.
The hyperbolic tangent scales our values to the range (−1, 1) we cutoff at ±0.99.
The original scaling produced results which are difficult to read and slightly
inconsistent. The newer scaling gives more reliable and consistent results.

4.4

Affine Transformations of the QUBO

When exploring portfolios of different sizes, we present a different matrix to
Dwave for each desired size of portfolio. We add a penalty for exploring portfolios of different sizes, while maintaining accurate values for the desired portfolio
size. The intuition for this follows closely from converting a QUBO into an
Ising model. In order to convert a QUBO into an Ising model we consider the
7

transformation on the binary vector x:
z = 2x − 1
This transforms xt Qx into z t Jz + c · z + k where c is a vector of matching
length and k is a constant which we can remove from consideration. Since we’re
only looking for the location of the lowest energy level in z coordinates, we
convert back to x and find the actual lowest energy. Thus our intution leads us
to consider affine transformations in x:
z

=

ax + b

=⇒

xt Qx

=

z t Jz + c · z + k

(7)
(8)

where J = Q/a2 , c = −2J · b and again k is a constant about which we
care none. Our goal at this point is to find a shift which we can apply to the
quadratic form. This corresponds to a translation and is thus closely related
to the term b above. In our formulation we do not use balance although our
mathematics takes it into consideration. In this case balance will correspond to
a boost in our coordinate system.
In order to make things easier from the point of view of computation we do
not give explicit formulations of shift and balance in terms of a and b above,
but rather explain what we actually compute.
Definition 1. Given a universe U of assets from which to choose, we define the
shift factor sn for exactly n > 1 assets from U as
sn =

−2gnm
|U|

(9)

where g is the best score derived from a classical simulation in this case a genetic
algorithm, 1.5 < m < 20 is a multiplier which we derive empirically.
Our multiplier m is generally around 5. Intuitively, errors can be multiplicative
√ and so we consider values close the geometric average of 1.5 and 20 i.e.
30 ≈ 5.4
As mentioned we skip the algebraic coordinate transformation and simply
add our shift factor to both linear and quadratic terms, but we do so as follows:
1. to linear terms add sn /n that is −gm/|U|
2. to quadratic terms add 2sn /(n − 1)

4.5

Visualization

Visualization of the energy landscape is critical in learning how DWave finds a
solution. It also aids our understanding of how matrix transformations adjust
the landscape to improve the probability of sampling “correct” asset values. For
8

Figure 2: CQNS scores raw vs computed with a shifted matrix
example, we can place a penalty on smaller portfolios by adding a shift term
while subtracting a shift term places a penalty on larger portfolios. Consider
the following image:
The values in both of these graphs are computed energy values and the x-axis
is the set of assets sorted by number of assets in a portfolio. We see an unevenly
shifted matrix where we have chosen exactly half the possible assets. We achieve
a nice “U”-shaped curve where the minimal values are clustered around |U|/2
assets. Furthermore, around |U|/2 our shifted matrix gives us lower values than
the raw CQNS. We repeat this for each number of assets n > 1, while holding
the raw CQNS scores for the desired portfolio size constant. We ‘tilt the curve
toward or away from smaller portfolios, with the opposite impact on larger ones,
to ensure DWave finds the desired portfolio sizes in that QUBO.

5

Results

Our experimental workflow is as follows:
1. Download 1-year of daily market data for a specific set of N assets and
indices.
· Current as of that moment
· Hold that data for all experiments
2. Calculate covariance of each asset with the market, and β,[3] based on log
returns
3. Calculate covariance terms between assets
9

4. Calculate underlying and summary values, including Sharpe Ratio and
Chicago Quantum Net Score, for an all asset portfolio (i.e. hold all 40
assets for an equal investment amount)
5. Derive a QUBO for each portfolio size (2 to |U|).
· Visualize minimum CQNS values on multiple QUBO matrices.
· Shift each QUBO to increase likelihood of choosing a portfolio with
fixed number of assets.
6. Run a classical probabilistic algorithm, in our case a genetic algorithm, to
see one “best” portfolio and its values.
7. Execute DWave using appropriate range of portfolio sizes.
8. Use the Dwave results the seed the genetic algorithm
9. Compare values to classical methods.
The following figures 34 give some idea of how well the Quantum computer
performs using the CQNS against the Sharpe ratio. We see that in this sample,
DWave approaches the efficient frontier in a few cases (highest return for that
level of risk). Most points achieve relative parity with random sampling results,
and in some cases DWave suggests lower performing portfolios. These results
vary by sample, sample size, and market conditions. One will also notice that
toward the lower left of the efficient frontier, there is a higher density of solutions
which shows us that the CQNS formulation lands on the efficient frontier, but
is somewhat more conservative. In reality, the CQNS tends to favor portfolios
with lower risk.
We further give results of the CQNS by method. One will notice that DWave
performs well, in fact obtaining better results than Monte Carlo methods, but
underperforming the genetic algorithms. Using DWave as a seed guarantees the
genetic algorithm will perform better, as we disallow anything “worse” than
the seed to propagate through generations of solutions. Interestingly, the two
genetic algorithms give the same answers. We were lucky, however to be able
to run the genetic algorithms through many generations. We expect that if our
universe were to have ∼ 1024 assets the genetic algorithm with DWave seeds
would be the top performer, with the simple genetic algorithm performing close
to DWave.
We see that DWave outperforms classical random sampling on average, for
all portfolios n ∈ {3 − 25, 27, 28, 33}, which is where most of our portfolios were
run. This shows that DWave is not picking randomly or average solutions, but
good ones. The under performance for larger portfolios gives us food for thought
in future experiments.

10

Figure 3: DWave solutions; expected return vs standard deviation. We also plot
Expected return vs Market Momentum, which is a covariance with the market
without adjusting for nominal returns as in the Sharpe Ratio.

(a) CQR vs DWave

(b) CQNS vs DWave

Figure 4: Some plots of Classical vs Quantum annealer computations

6

Discussion and Conclusion

Positive Semi-Definite Considerations Practitioners of numpy will know
well that numpy is prone to rounding errors. In particular we find that numpy
computes covariance matrices with slightly negative eigenvalues ∼ −1e − 8.
While this is not a particularly large negative value, it does open the possibility
of a “minimum risk portfolio” by having a negative overall variance, then the
computed Sharpe ratio will be several orders of magnitude too large. In order to
mitigate this we first test our covariance with a Cholesky decomposition.Second
we can simply modify our matrix by computing the standard eigendecomposition
11

(a) CQNS by Method

(b) Completion Time by Method

Figure 5: Some plots of Classical vs Quantum annealer computations

Figure 6: CQNS by asset size
and setting all eigenvalues below some absolute threshold at exactly zero.
Considerations of Weighting Assets In order to maintain a weighting of
assets which sums to 1, we restrict from negative values. In principle one can
short assets, but designing a quadratic form to account for this is a separate
problem. In particular if we short one asset then the sum of positive investments
will be greater than one and incurs questions about over and under leveraging.
This is out of the scope of our present research. The second problem is that we
will not have a QUBO as we must consider values {−1, 0, 1}. This requires a
tertiary optimizer, not a binary one. For this research we have chosen an even
positive weighting of assets to reduce computation space. When we have |U|
assets, our search space with even weightings is 2|U | . Were we to allow a continuous weighting, we would have to approach this with a different optimization
scheme. If we were to allow assets to have a discrete weighting, e.g. 0 to 1 by
0.01, our search space becomes 101|U | which is approximately 7 order of magnitude larger. This brings our ability to search for an optimal portfolio down to
only 32. We demonstrated that a 32 asset portfolio can be optimized reasonably
well with classical methods. Specifically, we have enough solution space to line
up eigenvectors much more easily.

12

Selecting our Economic Values We use three market equity indices to
derive our one-year market returns (Wilshire 5000, S&P 500, Russell 2000),
along with the average return over the past year of 13 week US Treasury Bills.
We apply floors to each index to avoid negative market returns. We remove
stocks with β < 0 or β > 10, and those without continuous trade data over the
past year i.e. 253 days, in order to avoid market anomalies. We select one-year
data because we lose too much variability with five-year historical market data
≈ 2/3. We believe this is due to the market reverting to means.
Model adjustments during time of market turbulence: Our model for stock
selection requires mathematical adjustment in times of market declines when our
indices move into negative territory over a year or when interest rates approach
or drop below zero. This impacts the signs of our scoring models.
Discussion of Quantum Advantage We optimize a reasonably sized portfolio using DWaves 2,041 qubit quantum annealer through a repeatable research
and business process. We pick 40 assets, which creates a solution space of 240 ,
or 1.1 trillion portfolios from which to select.
As practitioners, our research indicates potential for quantum advantage at
a higher number of assets. At lower asset levels there are efficient classical
algorithms that do better. We cannot solve this problem using brute force on
our equipment at 40 assets. We find an equivalent portfolio with a random
sampling of 500M portfolios that takes hours to run. One portfolio with 3 out
of 40 assets appears optimal via a genetic algorithm seeded with 1,028 random
portfolios. We improve on that timing by seeding the genetic algorithm with
the DWave solutions.
If we repeat the process of 36 experiments with 60 assets, we expect we
might beat the genetic algorithm...but we would also use a classical simulated
annealer which could outperform the genetic algorithm...so the race for quantum
advantage continues.
Next Steps In the future we intend to evaluate reverse annealing, simulated
annealing (both thermal and quantum), use of the DWave Hybrid solver, and to
optimize larger and more diverse portfolios. We also intend to further optimize
the DWave runs and the QUBO build process.
From an economics perspective, we intend to add different types of financial
assets, including bonds, commodities, real estate investment trusts, and currencies (including Bitcoin - USD). We intend to evaluate additional economic
factors such as financial health, growth, dividend payouts, and liquidity, which
today we include implicitly.
Finally, we saw unique behavior when actual market returns over one year
became negative (which it did during our research), and when individual stocks
behaved erratically (e.g., β < 0 and β > 5.0). We intend to explore how these
impact the portfolio optimization solutions from the Chicago Quantum Net
Score.

13

References
[1] N.Bekkers, R.Doeswijk, T.Lam, Strategic Asset Allocation: Determining
the Optimal Portfolio with Ten Asset Classes https://papers.ssrn.com/
sol3/papers.cfm?abstract_id=1368689 Oct 20 09
[2] StackExchange, Comparing Portfolio Volatility with Index Volatility seems a wrong method?, Jan 2015, AltTabsen, QuantK,
and
Ric,
https://quant.stackexchange.com/questions/16223/
comparing-portfolio-volatility-with-index-volatility-seems-a-wrong-method
[3] BETA, Investopedia https://www.investopedia.com/terms/b/beta.
asp
[4] G. Brinson, L.R. Hood, G. Beebower, Determinants of Portfolio Performance, June 1986, Financial Analysts Journal 42(4):39-44, DOI: 10.2469/
faj.v42.n4.39
[5] G. Brinson, B. Singer, G. Beebower, Determinants of Portfolio Performance
II: An Update, May/June 1991, Financial Analysts Journal pp.40
[6] Ahmed Fasih, StackOverflow:
Python:
convert matrix to positive semi-definite, https://stackoverflow.com/questions/43238173/
python-convert-matrix-to-positive-semi-definite/43244194
[7] V. Divakar, Calculating the Covariance Matrix and Portfolio
Variance,
December 27,
2018,
https://blog.quantinsti.com/
calculating-covariance-matrix-portfolio-variance
[8] DWave Systems Documentation,https://www.docs.dwavesys.com
[9] DWave Systems Application Development Resources, https://cloud.
dwavesys.com/leap/resources
[10] Efficient Frontier at Wikipedia https://en.wikipedia.org/wiki/
Efficient_frontierEfficientFrontierWiki
[11] Harry Markowitz, Portfolio Selection, The Journal of Finance, 7,1 (1952),
77-91
[12] Michael Marzec. Portfolio Optimization: Applications in Quantum Computing. SSRN Electronic Journal, 2013 https://papers.ssrn.com/sol3/
papers.cfm?abstract_id=2278729
[13] Marcos Lopez de Prado, Ph.D., Machine Learning Asset Allocation, https:
//ssrn.com/abstract=3469964, Advanced in Financial Machine Learning, ORIE 5256
[14] Nada Elsokkary, Faisal Shah Khan, Davide La Torre, Travis S. Humble,
Joel Gottlieb. Financial Portfolio Management using D-Waves Quantum
Optimizer: The Case of Abu Dhabi Securities Exchange. IEEE High Performance Extreme Computing Conference, 2017 (edited)
14

[15] Bernard Pfaff, Financial Risk Modelling and Portfolio Optimization with
R, second edition, Wiley, 2016. ISBN : 9781119119661
[16] Michael Jensen, The Pricing of Capital Assets and the Evaluation of Investment Portfolios, The Journal of Business, Vol. 42, No.2, (Apr., 1969),
pp. 167 - 247
[17] An Introduction to Information Geometry, https://arxiv.org/pdf/
1808.08271.pdf
[18] Ors, Romn, Samuel Mugel, and Enrique Lizaso. Quantum computing for finance: overview and prospects. Reviews in Physics 4 (2019)
(arXiv:1807.03890 [quant-ph])
[19] ReSolve Asset Management Whitepaper, A General Framework for Portfolio Choice, 27 pages, undated
[20] M. Rubenstein, Markowitz’s Portfolio Selection: a Fifty-Year Retrospective, The Journal of Finance, Vol LVII, Num 3, June 2002,
DOI:10.1.1.404.4279
[21] Sharpe Ratio at Wikipedia https://en.wikipedia.org/wiki/Sharpe_
ratio
[22] William F. Sharpe, Stanford University, The Sharpe Ratio, The Journal of
Portfolio Management, Fall 1994 http://web.stanford.edu/~wfsharpe/
art/sr/sr.htm
[23] Standard & Poor, formerly CapitalIQ company database, Highland Park
Public Library access to data screening tools, https://hplibrary.org/
databases-5317
[24] William F. Sharpe, Mutual Fund Performance, The Journal of B business,
Vol 39, No.1, Part 2, Supplement on Security Prices. (Jan 1966), pp. 119 138 http://www.jstor.org/stable/2351741
[25] Scot
Stockton,
What’s
The
Difference
Between
45
and
28 Percent Return?
The Efficient Frontier,
August 20,
2018,
Seeking
Alpha,
https://seekingalpha.com/article/
4200744-difference-45-return-and-28-efficient-frontier
[26] D.Venturelli, A.Kondratyev, Reverse Quantum Annealing Approach to
Portfolio Optimization Problems, arXiv:1810.08584, 2018
[27] X.Ye, L.Ning, J.Yang, D.Yao, Y.Hong, Research on three different Portfolio Models with singular Covariance Matrix IOSR Journal of Mathematics
(IOSR-JM) Volume 14, Issue 5 Ver. II (Sep - Oct 2018), PP 33-39
[28] YFinance python module, maintained by Ran Aroussi, Thank you https:
//pypi.org/project/yfinance/
[29] Yahoo Finance provides all historical data used in these experiments,
Thank you, https://finance.yahoo.com/
15

7

Thank You

We acknowledge and thank the writers, maintainers and community contributors for Python, Numpy, Pandas, Matplotlib, Scipy, and DWave Ocean, Julia,
and R. We also thank DWave Systems, Google, Slack, Anaconda, and Jupyter
for use of their tools in this research effort.

16

