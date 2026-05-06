Available online at https://journal.rescollacomm.com/index.php/ijrcs/index

International Journal of Research in Community
Service

e-ISSN: 2746-3281
p-ISSN: 2746-3273

Vol. 1, No. 3, pp. 14-18, 2020

Markowitz Model Investment Portfolio Optimization: a Review
Theory
Nurfadhlina Abdul Halima*, Ari Yuliatib
b

a
Faculty of Science and Technology, Universiti Sains Islam Malaysia, MALAYSIA
Department of Electrical Engineering, Universitas Muhammadiyah Tasikmalaya, INDONESIA

.
*

Corresponding author email: nurfadhlina@usim.edu.my

Abstract
In the face of investment risk, investors generally diversify and form an investment portfolio consisting of several
assets. The problem is the fiery proportion of funds that must be allocated to each asset in the formation of
investment portfolios. This paper aims to study the optimization of the Markowitz investment portfolio. In this
study, the Markowitz model discussed is that which considers risk tolerance. Optimization is done by using the
Lagrangean Multiplier method. From the study, an equation is obtained to determine the proportion (weight) of
fund allocation for each asset in the formation of investment portfolios. So by using these equations, the
determination of investment portfolio weights can be determined by capital.
Keywords: Investment risk, diversification, portfolio, the weight of fund allocation, optimization, Lagrange
multiplier.

1. Introduction
Investment Portfolio is a group of investments owned by an institution or individual. The form can
vary, such as bonds, mutual funds, property, stocks, and other investment instruments. For people who
invest in shares, there is also the term Stock Portfolio, which is a collection of investment assets in the
form of shares. In a portfolio, an investor can diversify into various investment products to produce
optimal returns & minimize risk (Ardia and Boudt, 2013). This is by the advice to not put all eggs in one
basket so that all eggs do not break if the basket falls. With diversification, the risk borne in an
investment can be reduced because all money is not put into one investment instrument. The more assets
(basket), the lower the risk (Bjork et al., 2011).
Refer to Panjer et al. (1998) and Ruppert (2004), Markowitz’s in 1952 had popularized efficient
portfolio selection methods. For example, given p portfolio with w weight vector, investors have two
objectives (objective), namely: (i) Maximizing the expected value  p of portfolio returns, and (ii)

Nurfadhlina Abdul Halim. / International Journal of Research in Community Service, Vol. 1, No. 3, pp. 14-18, 2020

15

Minimizing portfolio risk, which is measured by  2p or  p . Based on individual preferences, an
investor puts weight on these two different goals, and maximizes them. Refer to Garcia et al. (2015),
Harry Markowitz explained that to minimize risk and still get a sizeable return, it can be done by forming
a portfolio. This statement is supported by research by Mangram (2013) and Parmar (2014). According to
Kamil et al. (2006) and Sirucek & Lukas (2015), the determination of the optimal portfolio can be done
in several ways, one of them with the Markowitz model. The Markowitz model assumes that investors
choose two considerations when building an investment portfolio, namely expected returns and risks in
return.
Based on the description above, this paper intends to conduct a theoretical study of the optimization of
the Markowitz investment portfolio. The aim is to obtain an equation form that can be used to determine
the weight value of the allocation of funds for each asset in the formation of investment portfolios. The
resulting equation is very useful for investors to determine the weight of fund allocation easily.

2. Materials and Methods
The material used in this study is Markowitz's investment portfolio model, which considers investor
risk tolerance. The study methods used include the formation of mean vectors, the formation of
covariance matrices, formation of average equations and variance of portfolios, the formation of
investment portfolio models in the form of Markowitz mean variants, where the optimization process
used is Lagrangean multiplier, and Kuhn-Tucker's theorem.

3. Results and Discussion
Suppose there are N risk assets (ordinary shares or stock indexes, and the like) with a return r1,..., rN .
It is assumed that the first and second moments of the r1,..., rN exist (Panjer et al., 1998). Then the return
expectation value vector is given by

μT  (1,...,  N ) , with i  E[ri ] , i  1,..., N
and the covariance matrix is given by

Σ  ( ij )i , j 1,..., N , with  ij  Cov(ri , rj ) , i, j  1,..., N

T
As explained earlier, portfolio returns with a weight vector of w  ( w1,..., wN ) , where

N

 wi  1 is
i 1

required, are given by equation (4.2.1). Expectations of portfolio returns in equation (4.2.2) can be
expressed using vector equations as

 p  E[rp ]  μT w ,

(1)

 2p  Var (rp )  wT Σw .

(2)

and the variance equation (4.2.3) becomes
In the Mean-Variance optimization, an efficient portfolio is defined as follows.
Definition 1. A p * portfolio is called (Mean-Variance) efficient if there is no p portfolio with

 p   p* and  2p   2p* (Panjer et al., 1998; Rupert, 2004).
To get an efficient portfolio, usually using objective functions to maximize

2 p   2p ,   0

(3)

16

Nurfadhlina Abdul Halim. / International Journal of Research in Community Service, Vol. 1, No. 3, pp. 14-18, 2020

where is the risk tolerance parameter  of the investor, means, for investors with risk tolerance 
(  0) must resolve portfolio problems
N

Maximize
{2 p   2p } with the provision of  wi  1 ,
N

(4)

Maximize{2
 μT w  wT Σw} with the provision of eT w  1
N

(5)

w

i 1

or
w

by eT  (1, 1, ...,1) N . It is important to note that settlement (5), for all  [0, ) , forms a
complete set of efficient portfolios. The set of all points in the diagram- (  p ,  2p ) relating to an efficient
portfolio is called an efficient surface, as given by Figure 1.

Figure 1: Efficient portfolio set

An efficient portfolio that matches   0 is called the minimum variance of the w Min portfolio
(Kheirollah & Bjarnbo, 2007; Panjer et al., 1998).
The mathematical nature of the optimization problem (4.4.5), because the covariance matrix Σ is
semi-definite positive, the objective function is quadratic convex. Thus, (5) is a matter of quadratic
convective optimization (Panjer et al., 1998). The Lagrange multiplier function of the problem of
portfolio optimization is given by
(6)
L (w,  )  2 μT w  wT Σw   (wT e  1) .
Based on the Kuhn-Tucker theorem, the optimality condition of equation (6) is

L
 2 μ  2Σw  e  0
w
L
 wT e  1  0


(7)
(8)

Nurfadhlina Abdul Halim. / International Journal of Research in Community Service, Vol. 1, No. 3, pp. 14-18, 2020

17

Equations (7) and (8) are necessary and sufficient conditions for global optimum. In addition, it is also
linear in weight portfolio w and in the Lagrange multiplier  (Kheirullah & Bjarnbo, 2007; Rupert,
2004; Panjer, 1998).
To calculate the set of efficient portfolios it is assumed: (i) Σ is a positive definite matrix, and (ii)
vectors e and μ are linearly free.
Efficient Portfolio Set. Let   0 is determined, solving equations (7) and (8) results in a minimum
portfolio of variances with a weight vector

1
w Min  T 1 Σ1e
e Σ e
After going through several calculations, to   0 obtained


1
eT Σ1μ
w*  T 1 Σ1e    Σ1μ  T 1 Σ1e 
e Σ e
e Σ e



(9)

or

eT Σ1μ
w*  w Min   z * , with z*  Σ1μ  T 1 Σ1e
e Σ e

(10)

To summarize, all efficient portfolios have the same form

w*  w Min   z * ,   0

(11)

Min

where w
is the minimum variance portfolio, which depends on the Σ covariance matrix but not on
the μ vector, while w * depends on Σ and μ , and has properties
N

 zi  0
i 1

Therefore, w * is a portfolio of self-financing in the sense that long positions are cashed in by short
positions (Panjer, 1998).
Efficient surface. Formula (11) can be used to determine the surface efficiently, using

Cov(rpMin , rz* )  zT Σw Min  0
obtained

 p*   pMin   z* ,

and

 2p*   2pMin   2 z2* .
Therefore, the efficient surface is parabolic in the (  p ,  2p ) -diagram if the risk is measured with  2p ,
and hyperbolic in the (  p ,  p ) -diagram if the risk is measured with  p (Panjer, 1998).

4. Conclusion
In this paper, a study has been carried out on optimizing the investment portfolio of the Markowitz
model. From the results of the study, it can be concluded that the portfolio optimization discussed
considers risk tolerance, and an equation form has been obtained to determine the weight of the fund

18

Nurfadhlina Abdul Halim. / International Journal of Research in Community Service, Vol. 1, No. 3, pp. 14-18, 2020

allocation for each asset in the investment portfolio. Besides, the discussion also obtained an efficient
surface curve which is a set of points of the mean and variance pairs for each risk tolerance value formed.

References
Ardia, D. & Boudt, K. (2013). Implied Expected Returns and the Choice of a Mean-Variance Efficient Portfolio
Proxy. Working Paper. A D´epartement de Finance, Assurance et Immobilier, Universite Laval, Quebec City
(Quebec), Canada.
Bjork, T., Murgoci, A. & Zhou, X.Y. (2011). Mean-Variance Portfolio Optimization with State-Dependent Risk
Aversion. Working Paper. Department of Finance, StockholmSchool of Economics, Box 6501, SE-113 83
Stockholm, SWEDEN. E-mail: tomas.bjork@hhs.se.
Garcia, Fernando, Jairo, A., & Javier, O. (2015). Mean-Variance Investment Strategy Applied in Emerging
Financial Markets: Evidence From the Colombian Stock Market. Jurnal Mykolo Romerio Universitetas, 9 (2),
22-29.
Kamil, Anton, A., Chin, Y. F., & Kin, K. (2006). Portfolio Analysis Based On Markowitz Model. Journal of
Statistics and Management Systems University Sains Malaysia, 9 (3), 519-536.
Kheirollah, A. & Bjarnbo, O., (2007), A Quantitative Risk Optimization of Markowitz Model: An Empirical
Investigation on Swedish Large Cap List. Master Thesis, in Mathematics/Applied Mathematics, University
Sweden, Department of Mathematics and Physics, www.mdh.se/polopoly_fs/ 1.16205!MasterTheses.pdf
Mangram, M. (2013). A Simplified Perspective of the Markowitz Portfolio Theory. Global Journal of Business
Research SMC University Switzerland,7 (1), 59-70.
Panjer, H.H., Boyle, D.D., Cox, S.H., Dufresne, D., Gerber, H.U., Mueller, H.H., Pedersen, H.W., & Pliska, S.R.
(1998). Financial Economics. With Applications to Investments, Insurance, and Pensions. Schaumberg,
Illinois: the Actuarial Foundation.
Parmar, Chetna. (2014). Portfolio Selection using Min-Max Approach; Selected Bank in India: Markowitz Model.
International Journal of Advanced Research in Computer Science and Management Studies RK University, 2
(1), 11-17.
Ruppert, D. (2004). Statistics and Finance: An Introduction. Springer-Verlag, New York.
Sirucek, Martin & Lukas Kren. (2015). Application of Markowitz Portfolio Theory by Building Optimal Portfolio
on the Us Stock Market. Jurnal Mendel University, 63 (4), 1375-1386.

