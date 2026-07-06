arXiv:cond-mat/0208191v2 [cond-mat.soft] 11 Aug 2002

QUANTUM MECHANICS, PATH INTEGRALS AND
OPTION PRICING:
REDUCING THE COMPLEXITY OF FINANCE

BELAL E. BAAQUIE(1) , CLAUDIO CORIANÒ(2)
AND
MARAKANI SRIKANT(1)
(1)

National University of Singapore
Singapore 119260
phybeb@nus.edu.sg
srikant@srikant.org
(2)

Dipartimento di Fisica
Universita’ di Lecce
INFN Sezione di Lecce
Via Arnesano 73100, Lecce, Italy
claudio.coriano@le.infn.it

Quantum Finance represents the synthesis of the techniques of quantum theory
(quantum mechanics and quantum field theory) to theoretical and applied finance.
After a brief overview of the connection between these fields, we illustrate some
of the methods of lattice simulations of path integrals for the pricing of options.
The ideas are sketched out for simple models, such as the Black-Scholes model,
where analytical and numerical results are compared. Application of the method
to nonlinear systems is also briefly overviewed. More general models, for exotic or
path-dependent options are discussed.

1. Introduction
a

Financial markets have undergone a tremendous growth in the last
decades and in order to meet the need of customers new and complex
financial instruments have been developed. Risk assessment models and
the quantification of returns, given the huge amount of trading involved
worldwide, requires more sophisticated approaches than in the past. Nona Prep n.: UNILE-CBR-02-03. Talk presented by Claudio Corianò at the Intl. Workshop

“Nonlinear Physics: Theory and Experiment II”, Gallipoli, Lecce, Italy, June 28 - July
4, 2002
1

2

linearities play a key role in all of this, and, from this side, the field is
probably largely unexplored.
In general, intensive numerical simulations and fast algorithms are
needed to obtain useful results. Analytical results are limited, except for
simple models such as the Black-Sholes model and other similar models.
Use of a path integral formulation has some advantages. First, it is in
close relation to the lagrangean description of diffusion processes, second,
it opens the way to the use of quantum mechanical methods.
We will introduce the field at a non-expert level through a crash course
(next few sections). Then we will come to brefly illustrate where nonlinearities appear and review some of the simplest equations one can write down,
generalizing the Black-Scholes model. We will then proceed to discuss the
path integral formulation of the Black-Scholes and the model of barrier
options, resorting to a lagrangian path integral formulation. Strategies to
solve the path integral are then briefly presented, together with some results. Detailed simulations, algorithms of analysis and related applications
will be presented elsewhere 1 . The review sections are standard knowledge
in the field, and are based on 2 .
2. A view on Theoretical Finance
2.1. Simulating the Complexity of Finance
The simulation of financial markets can be modeled, from a theoretical
viewpoint, according to two separate approaches: a bottom up approach
and (or) a top down approach.
For instance, the modeling of financial markets starting from diffusion
equations and adding a noise term to the evolution of a function of a
stochastic variable is a top down approach. This type of description is,
effectively, a statistical one.
A bottom up approach, instead, is the modeling of artificial markets
using complex data structures (agent based simulations) using general updating rules to describe the collective state of the market. The number
of procedures implemented in the simulations can be quite large, although
the computational cost of the simulation becomes forbidding as the size
of each agent increases. Readers familiar with Sugarscape Models and the
computational strategies based on Growing of Artificial Societies 4 have
probably an idea of the enormous potentialities of the field. However, one
would expect that the bottom up description should become comparable to
the top down description for a very large number of simulated agents.
The bottom up approach should also provide a better description of ex-

3

treme events, such as crashes, collectively conditioned behaviour and market incompleteness, this approach being of purely algorithmic nature. A
top down approach is, therefore, a model of reduced complexity and follows a statistical description of the dynamics of complex systems (for an
introduction see 5 ).
2.2. Forward, Futures Contracts and Options
Let the price at time t of a security be S(t). A specific good can be traded
at time t at the price S(t) between a buyer and a seller. The seller (short
position) agrees to sell the goods to the buyer (long position) at some time
T in the future at a price F(t,T) (the contract price). Notice that contract
prices have a 2-time dependence (actual time t and maturity time T). Their
difference τ = T − t is usually called time to maturity. Equivalently, the
actual price of the contract is determined by the prevailing actual prices
and interest rates and by the time to maturity.
Entering into a forward contract requires no money, and the value of the
contract for long position holders and strong position holders at maturity
T will be
(−1)p (S(T ) − F (t, T ))

(1)

where p = 0 for long positions and p = 1 for short positions. Futures
Contracts are similar, except that the after the contract is entered, any
changes in the market value of the contract are settled by the parties.
Hence, the cashflows occur all the way to expiry unlike in the case of the
forward where only one cashflow occurs. They are also highly regulated
and involve a third party (a clearing house). Forward, futures contracts
and, as we will see, options go under the name of derivative products, since
their contract price F(t, T) depend on the value of the underlying security
S(T ).
To complete this crash course on financial instruments we need to define
options. Options are derivatives that can be written on any security and
have a more complicated payoff function than the futures or forwards. For
example, a call option gives the buyer (long position) the right (but not the
obligation) to buy or sell the security at some predetermined strike-price at
maturity. A payoff function is the precise form of the price. Path dependent
options are derivative products whose value depends on the actual path
followed by the underlying security up to maturity. In the case of pathdependent options, since the payoff may not be directly linked to an explicit
right, they must be settled by cash. This is sometimes true for futures and
plain options as well as this is more efficient.

4

3. Langevin Evolution
In the top down description of theoretical finance, a security S(t) follows a
random walk described by a Ito-Weiner process (or Langevin equation) as
d S(t)
= φdt + σR(t)dt,
S(t)

(2)

where R(t) is a Gaussian white noise with zero mean and uncorrelated
values at time t and t′ hR(t)R(t′ )i = δ(t−t′ ). φ is the drift term or expected
return, while σ is a constant factor multiplying the random source R(t),
termed volatility.
As a consequence of Ito calculus, differentials of functions of random
variables, say f (S, t), do not satisfy Leibnitz’s rule, and for a Ito-Weiner
process with drift (2) one easily obtains for the time derivative of f (S, t)
∂f
∂f
1
∂2f
∂f
df
=
+ σ 2 S 2 2 + φS
+ σS
R.
dt
∂t
2
∂S
∂S
∂S

(3)

The Black-Scholes model is obtained by removing the randomness of the
stochastic process shown above by introducing a random process correlated
to (3). This operation, termed hedging, allows to remove the dependence on
the white noise function R(t), by constructing a portfolio Π, whose evolution
is given by the short-term risk free interest rate r
dΠ
= rΠ.
dt

(4)

∂f
S. This is a portfolio in which the
A possibility is to choose Π = f − ∂S
investor holds an option f and short sells b an amount of the underlying
∂f
. A combination of (3) and (4) yields the
security S proportional to ∂S
Black-Scholes equation

∂f
1
∂2f
∂f
+ σ 2 S 2 2 + rS
= rf.
∂t
2
∂S
∂S

(5)

There are some assumptions underlying this result. We have assumed absence of arbitrage, constant spot rate r, continuous balance of the portfolio,
no transaction costs and infinite divisibility of the stock.
The quantum mechanical version of this equation is obtained by a
change of variable S = ex , with x a real variable. This yields
∂f
= HBS f
∂t
b short selling of the stock should be possible

(6)

5

with an Hamiltonian HBS given by
HBS = −

σ2 ∂ 2
+
2 ∂x2



1 2
σ −r
2



∂
+ r.
∂x

(7)

Notice that one can introduce a quantum mechanical formalism and interpret the option price as a ket |f i in the basis of |xi, the underlying security
price. Using Dirac notation, we can formally reinterpret f (x, t) = hx|f (t)i,
as a projection of an abstract quantum state |f (t)i on the chosen basis.
In this notation, the evolution of the option price can be formally written
as |f, ti = etH |f, 0i, for an appropriate Hamiltonian H.
In the presence of a stochastic volatility, the description is more involved,
but also more interesting.
In general, the description of these processes is driven by two correlated
white noise functions R1 and R2
dV
= λ + µV + ζV α R1
dt
√
dV
= φS + σ V + µV + ζV α R2
dt

(8)

√
with V = σ and hR1 (t)R2 (t′ )i = 1/ρ δ(t − t′ ), ρ being the correlation parameter. However, since volatility is not traded in the market (the market
is said to be incomplete), perfect hedging is not possible, and an additional
term, the market price of volatility risk β(S, V, t, r), is in this case introduced. β can be modeled appropriately. In some models 3 , a redefinition
of the drift term µ in (8) in the evolution of the volatility is sufficient to
hedge such more complex portfolios, which amounts to an implicit choice of
β(S, V, t, r). We just quote the result for the evolution of an option price in
the presence of stochastic volatility, which, in the Hamiltonian formulation
are given by
∂f
= HMG f
∂t

(9)

with




ey ∂
ζ 2 2y(α−1) ∂
ey ∂ 2
−y
HMG = − r −
− λe + µ − e
−
2 ∂x
2
∂y
2 ∂x2
−ρζey(α−1/2)

e2y(α−1) ∂ 2
∂2
+ r.
− ζ2
∂x∂y
2
∂y 2

(10)

which is nonlinear in the variables x = log(S) and y = log(V ). For general
values of the parameters, the best way to obtain the pricing of the options
in this model is by a simulation of the path integral.

6

4. Monte Carlo Simulations of option pricing
Simulations of the functional integral are rather straightforward and we
should omit any detail about them since they have been known ever since
by the high energy physics community. However, to reach out to a less
specialized audience, we will provide a simple illustration of the method.
Once the model is given, one determines the underlying lagrangean. We
assume a discretization of the time to maturity τ in intervals ǫ = τ /N , with
N an arbitrary (large) integer.
For instance, for the Black Scholes model one gets the action
SBS = ǫ

N
X

LBS (i)

(11)

i=1

with
LBS (i) = −

1
2σ 2



xi − xi−1
σ2
+r−
ǫ
2

2

(12)

where we have introduced discretized positions (xi ) for the variable x =
log(S) which identifies the quantum mechanical state of the system. We
will refer to it as to the stock price. The propagator for the stock price is
given by the pricing kernel
Z
′
pBS (x, x , τ ) = DXBS eSBS
= hx|e−τ HBS |x′ i

(13)

with
Z

DXBS = Πτt=0

Z ∞

dx(t).

(14)

−∞

For barrier options there is an analogous procedure, except that now we
need to introduce a generic potential V (x) in the corresponding Hamiltonian


1 2
∂
σ2 ∂ 2
+
σ − V (x)
+ V (x).
(15)
HV = −
2
2 ∂x
2
∂x
The pricing kernel is the fundamental quantity to compute using the functional integral. Related attempts can be found in the literature 7 .
For this purposes, we have used a standard Metropolis algorithm. If
thermalization is slow, it is possible to resort to use sequentially Metropolis
updates and cluster updates. The latter is an update for the embedded Ising
dynamics in the lattice variables xi /|xi | (Swendsen-Wang, Wolff), and is

7

included in for a faster generation of the thermalized paths of the stock
price x(t).
For processes involving a stochastic volatility (y = log(V )) the expression of the path integral is more complicated and can be found in 6 . From
now on we will just consider the case of a constant volatility.
If we denote by g(x, K) the payoff function, with a strike price K, in
this case the value of the option (its price) is given by the Feynman-Kac
formula

f (t, x) =

Z ∞

−∞

d x′ hx|e−(T −t)HBS |x′ ig(x′ , K).

(16)

In actual simulations, it is convenient to compute directly the option price
rather than the propagator itself. The simulation is done by taking the
initial point x fixed, and letting the final point evolve according to its
quantum dynamics. In this way a path (x, x′ ) is generated. After the first
thermalization, x′ is allowed to undergo quantum fluctuations, at fixed
x. Each x′ is then convoluted with the payoff function and an average is
performed. Finally, this procedure is repeated for several x values, so to
obtaint the option price at time to maturity τ .
Figs. 1, 2 and 3, illustrate some simple results obtained by the monte
carlo mehtod. For illustrative purposes, we show the behaviour of the
Black-Scholes model. Fig. 1 shows a typical thermalized path, generated
from a given initial value x (at current time t = τ ) assuming a maturity of
300 days, while in Fig. 2 we have plotted several path for different starting
values x of the stock at current time τ . We have chosen an interest rate
r = 0.05 and a 12 percent volatility σ. Finally, in Fig. 3 we compare the
analytical and the numerical evaluation of the Black-Scholes option price
with a low resolution for (16), in order to separate the two curves, which
otherwise would overlap completely, in order to illustrate the convergence
of the Metropolis algorithm.
Barrier options can be analized similarly, equivalently, by this method
or by the Langevin method. We show in Fig. 4 the evaluation of the price
of the option using the Langevin method in the presence of a step potential
sitting at a value of the stock price given by x0 = log(So ), with S0 = 100.
Compared to the Black-Scholes now the price has been discounted.
Applications of the method to the determination of various pricing kernels is underway. More details will be given elsewhere 1 .

8

1.01

Log(S)

1.00

0.99

0.98
0.0

100.0

200.0

300.0

days

Figure 1. An example of thermalized path obtained from the simulation of the path
integral (Black-Scholes) with r=0.05 and σ = 0.12

5. Acknowledgements
C.C. thanks R. Parwani for hospitality; the National Univ. of Singapore,
University Scholars Program, for financial support and L. Cosmai for previous discussions.

References
1. B.E. Baaquie, C. Corianò and S. Marakani, to appear.
2. B.E. Baaquie, Quantum Finance, to be published.
3. R. C. Merton, Bell Journal of Economics and Management Science 4 (Spring
1973), 141; M. Garman, A General theory of Asset Valuation under Diffusion
State Processes. Working Paper No 50, Univ. of California, Berkeley, 1976.
4. J. Epstein and R. Axtell, Growing Artificial Societies: Social Science from
the Bottom up, Brookings, MIT Press, 1996. See also the link:www.swarm.org
(Santa Fe Istitute, New Mexico).
5. R. Parwani, physics/0201055 and links therein.
6. B. E. Baaquie, L. C. Kwek and S. Marakani, cond-mat/008327

9

1.8

1.6

Log(S)

1.4

1.2

1.0

0.8

0

100

200

300

days
Figure 2.

Several thermalized paths for (Black-Scholes) with r=0.05 and σ = 0.12

7. G. Montagna, O. Nicrosini and N. Moreni, Physica A310 (2002) 450; G.
Montagna, O. Nicrosini Eur. Phys. J. B27 (2002) 249.

10
5
MC-BS
AN-BS

call option price

4

3

2

1

0

1

1.2

1.4

1.8

1.6

2

x0 = log(S0)

Figure 3. Call option price for strike price 3 versus the logarithm of the initial value of
the stock x0 = log(S0 ). the parameters are fixed as in figs 1. Shown is the analytical
result vs the monte carlo result, with a low resolution of 10,000 configurations

Result for Potential -0.95 for x>x0 and 0.05 for x<x0 (S0=100)
t=1 year, volatility = 0.25/year, 50,000 configurations, 128 time steps
40
Price with potential
Black-Scholes Price

Call option price

30

20

10

0
70

80

90

100

110
Strike price

120

130

140

150

Figure 4. Plot of the option price versus the stock price obtained by a Langevin simulation of the path integral, with a potential step

