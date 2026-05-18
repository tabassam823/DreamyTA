Chapter 15

ANOMALIES AND MARKET EFFICIENCY
G. WILLIAM SCHWERT °
University of Rochester, and NBER

Contents
Abstract
Keywords
1. Introduction
2. Selected empirical regularities
2.1. Predictable differences in returns across assets
2.1.1. Data snooping
2.1.2. The size effect
2.1.3. The turn-of-the-year effect
2.1.4. The weekend effect
2.1.5. The value effect
2.1.6. The momentum effect
2.2. Predictable differences in returns through time
2.2.1. Short-term interest rates, expected inﬂation, and stock returns
2.2.2. Dividend yields and stock returns

3. Returns to different types of investors
3.1. Individual investors
3.1.1. Closed-end funds
3.2. Institutional investors
3.2.1. Mutual funds
3.2.2. Hedge funds
3.2.3. Returns to IPOs
3.3. Limits to arbitrage

4. Long-run returns
4.1. Returns to ﬁrms issuing equity

°

939
939
940
941
941
941
942
943
944
945
947
949
950
952
954
954
955
956
956
956
957
959
959
960

The Bradley Policy Research Center, William E. Simon Graduate School of Business Administration,
University of Rochester, provided support for this research. I received helpful comments from Yakov
Amihud, Brad Barber, John Cochrane, Eugene Fama, Murray Frank, Ken French, David Hirshleifer,
Tim Loughran, Randall Mørck, Jeff Pontiff, Jay Ritter, René Stulz, A. Subrahmanyam, Sheridan Titman,
Janice Willett and Jerold Zimmerman. The views expressed herein are those of the author and do not
necessarily reﬂect the views of the National Bureau of Economic Research.
Handbook of the Economics of Finance, Edited by G.M. Constantinides, M. Harris and R. Stulz
© 2003 Elsevier Science B.V. All rights reserved

938

G.W. Schwert
4.2. Returns to bidder ﬁrms

5. Implications for asset pricing
5.1. The search for risk factors
5.2. Conditional asset pricing
5.3. Excess volatility
5.4. The role of behavioral ﬁnance

6. Implications for corporate ﬁnance
6.1. Firm size and liquidity
6.2. Book-to-market effects
6.3. Slow reaction to corporate ﬁnancial policy

7. Conclusions
References

962
964
964
965
965
965
966
966
966
967
968
968

Ch. 15:

Anomalies and Market Efﬁciency

939

Abstract
Anomalies are empirical results that seem to be inconsistent with maintained theories
of asset-pricing behavior. They indicate either market inefﬁciency (proﬁt opportunities)
or inadequacies in the underlying asset-pricing model. After they are documented and
analyzed in the academic literature, anomalies often seem to disappear, reverse, or
attenuate. This raises the question of whether proﬁt opportunities existed in the past,
but have since been arbitraged away, or whether the anomalies were simply statistical
aberrations that attracted the attention of academics and practitioners.
One of the interesting ﬁndings from the empirical work in this chapter is that many
of the well-known anomalies in the ﬁnance literature do not hold up in different sample
periods. In particular, the size effect and the value effect seem to have disappeared after
the papers that highlighted them were published. At about the same time, practitioners
began investment vehicles that implemented the strategies implied by the academic
papers.
The weekend effect and the dividend yield effect also seem to have lost their
predictive power after the papers that made them famous were published. In these
cases, however, I am not aware of any practitioners who have tried to use these
anomalies as a major basis of their investment strategy.
The small-ﬁrm turn-of-the-year effect became weaker in the years after it was ﬁrst
documented in the academic literature, although there is some evidence that it still
exists. Interestingly, however, it does not seem to exist in the portfolio returns of
practitioners who focus on small-capitalization ﬁrms.
Likewise, the evidence that stock market returns are predictable using variables such
as dividend yields or inﬂation is much weaker in the periods after the papers that
documented these ﬁndings were published.
All of these ﬁndings raise the possibility that anomalies are more apparent than
real. The notoriety associated with the ﬁndings of unusual evidence tempts authors
to further investigate puzzling anomalies and later to try to explain them. But even
if the anomalies existed in the sample period in which they were ﬁrst identiﬁed, the
activities of practitioners who implement strategies to take advantage of anomalous
behavior can cause the anomalies to disappear (as research ﬁndings cause the market
to become more efﬁcient).

Keywords
market efﬁciency, anomaly, size effect, value effect, selection bias, momentum
JEL classiﬁcation: G14, G12, G34, G32

940

G.W. Schwert

1. Introduction
Anomalies are empirical results that seem to be inconsistent with maintained theories
of asset-pricing behavior. They indicate either market inefﬁciency (proﬁt opportunities)
or inadequacies in the underlying asset-pricing model. After they are documented and
analyzed in the academic literature, anomalies often seem to disappear, reverse, or
attenuate. This raises the question of whether proﬁt opportunities existed in the past,
but have since been arbitraged away, or whether the anomalies were simply statistical
aberrations that attracted the attention of academics and practitioners.
Surveys of the efﬁcient markets literature date back at least to Fama (1970), and
there are several recent updates, including Fama (1991) and Keim and Ziemba (2000),
that stress particular areas of the ﬁnance literature. By their nature, surveys reﬂect
the views and perspectives of their authors, and this one will be no exception. My
goal is to highlight some interesting ﬁndings that have emerged from the research of
many people and to raise questions about the implications of these ﬁndings for the
way academics and practitioners use ﬁnancial theory 1 .
There are obvious connections between this chapter and other chapters by Ritter (5:
Investment Banking and Security Issuance), Stoll (9: Market Microstructure), Dybvig
and Ross (10: Arbitrage, State Prices and Portfolio Theory), Dufﬁe (11: Intertemporal
Asset Pricing Models), Ferson (12: Tests of Multi-Factor Pricing Models, Volatility,
and Portfolio Performance), Campbell (13: Equilibrium Asset Pricing Models), Easley
and O’Hara (17: Asset Prices Market Microstructure) and Barberis and Thaler (18:
Behavioral Issues in Asset Pricing). In fact, those chapters draw on some of the same
ﬁndings and papers that provide the basis for my conclusions.
At a fundamental level, anomalies can only be deﬁned relative to a model of
“normal” return behavior. Fama (1970) noted this fact early on, pointing out that
tests of market efﬁciency also jointly test a maintained hypothesis about equilibrium
expected asset returns. Thus, whenever someone concludes that a ﬁnding seems to
indicate market inefﬁciency, it may also be evidence that the underlying asset-pricing
model is inadequate.
It is also important to consider the economic relevance of a presumed anomaly.
Jensen (1978) stressed the importance of trading proﬁtability in assessing market
efﬁciency. In particular, if anomalous return behavior is not deﬁnitive enough for an
efﬁcient trader to make money trading on it, then it is not economically signiﬁcant.
This deﬁnition of market efﬁciency directly reﬂects the practical relevance of academic
research into return behavior. It also highlights the importance of transactions costs
and other market microstructure issues for deﬁning market efﬁciency.
The growth in the amount of data and computing power available to researchers,
along with the growth in the number of active empirical researchers in ﬁnance since

1

This chapter is not meant to be a survey of all of the literature on market efﬁciency or anomalies.
Failure to cite particular papers should not be taken as a reﬂection on those papers.

Ch. 15:

Anomalies and Market Efﬁciency

941

Fama’s (1970) survey article, has created an explosion of ﬁndings that raise questions
about the ﬁrst, simple models of efﬁcient capital markets. Many people have noted that
the normal tendency of researchers to focus on unusual ﬁndings (which could be a byproduct of the publication process, if there is a bias toward the publication of ﬁndings
that challenge existing theories) could lead to the over-discovery of “anomalies”. For
example, if a random process results in a particular sample that looks unusual, thereby
attracting the attention of researchers, this “sample selection bias” could lead to the
perception that the underlying model was not random. Of course, the key test is whether
the anomaly persists in new, independent samples.
Some interesting questions arise when perceived market inefﬁciencies or anomalies
seem to disappear after they are documented in the ﬁnance literature: Does their
disappearance reﬂect sample selection bias, so that there was never an anomaly in the
ﬁrst place? Or does it reﬂect the actions of practitioners who learn about the anomaly
and trade so that proﬁtable transactions vanish?
The remainder of this chapter is organized as follows. Section 2 discusses crosssectional and times-series regularities in asset returns, including the size, book-tomarket, momentum, and dividend yield effects. Section 3 discusses differences in
returns realized by different types of investors, including individual investors (through
closed-end funds and brokerage account trading data) and institutional investors
(through mutual fund performance and hedge fund performance). Section 4 evaluates
the role of measurement issues in many of the papers that study anomalies, including
the difﬁcult issues associated with long-horizon return performance. Section 5
discusses the implications of the anomalies literature for asset-pricing theories, and
Section 6 discusses the implications of the anomalies literature for corporate ﬁnance.
Section 7 contains brief concluding remarks.

2. Selected empirical regularities
2.1. Predictable differences in returns across assets
2.1.1. Data snooping
Many analysts have been concerned that the process of examining data and models
affects the likelihood of ﬁnding anomalies. Authors in search of an interesting research
paper are likely to focus attention on “surprising” results. To the extent that subsequent
authors reiterate or reﬁne the surprising results by examining the same or at least
positively correlated data, there is really no additional evidence in favor of the anomaly.
Lo and MacKinlay (1990) illustrate the data-snooping phenomenon and show how the
inferences drawn from such exercises are misleading.
One obvious solution to this problem is to test the anomaly on an independent
sample. Sometimes researchers use data from other countries, and sometimes they
use data from prior time periods. If sufﬁcient time elapses after the discovery of an

942

G.W. Schwert
Table 1
Size and value effects a , January 1982 – May 2002
Sample period

ai

t(ai = 0)

bi

t(bi = 1) b

DFA 9-10 Small company portfolio
1982–2002

0.0020

0.67

1.033

0.68

1982–1987

−0.0019

−0.44

1.000

0.00

1988–1993

0.0038

0.80

1.104

1.21

1994–2002

0.0035

0.66

1.013

0.15

−0.59

0.816

−2.14

DFA US 6-10 value portfolio
1994–2002

−0.0022

a Performance of DFA US 9-10 Small Company Portfolio relative
to the CRSP value-weighted portfolio of NYSE, Amex, and
Nasdaq stocks (Rm ) and the one-month Treasury bill yield (Rf ),
January 1982 – May 2002. The intercept in this regression, ai ,
is known as “Jensen’s alpha” (1968) and it measures the average
difference between the monthly return to the DFA fund and the
return predicted by the CAPM (see also Equation 1).
b The performance of the DFA US 6-10 Value Portfolio from
January 1994 – May 2002. Heteroskedasticity-consistent standard
errors are used to compute the t-statistics.

anomaly, the analysis of subsequent data also provides a test of the anomaly. I supply
some evidence below on the post-publication performance of several anomalies.
2.1.2. The size effect
Banz (1981) and Reinganum (1981) showed that small-capitalization ﬁrms on the New
York Stock Exchange (NYSE) earned higher average returns than is predicted by the
Sharpe (1964) – Lintner (1965) capital asset-pricing model (CAPM) from 1936–75.
This “small-ﬁrm effect” spawned many subsequent papers that extended and clariﬁed
the early papers. For example, a special issue of the Journal of Financial Economics
contained several papers that extended the size-effect literature 2 .
Interestingly, at least some members of the ﬁnancial community picked up on the
small-ﬁrm effect, since the ﬁrm Dimensional Fund Advisors (DFA) began in 1981 with
Eugene Fama as its Director of Research 3 . Table 1 shows the abnormal performance

2

Schwert (1983) discusses all of these papers in more detail.
Information about DFA comes from their web page: http://www.dfafunds.com and from the Center
for Research in Security Prices (CRSP) Mutual Fund database. Ken French maintains current data for
the Fama–French factors on his web site: http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/.

3

Ch. 15:

Anomalies and Market Efﬁciency

943

of the DFA US 9–10 Small Company Portfolio, which closely mimics the strategy
described by Banz (1981).
The measure of abnormal return ai in Table 1 is called Jensen’s (1968) alpha, from
the following familiar model:




Rit −Rft = ai + bi Rmt −Rft + eit ,
(1)
where Rit is the return on the DFA fund in month t, Rft is the yield on a one-month
Treasury bill, and Rmt is the return on the CRSP value-weighted market portfolio
of NYSE, Amex, and Nasdaq stocks. The intercept ai in (1) measures the average
difference between the monthly return to the DFA fund and the return predicted
by the CAPM. The market risk of the DFA fund, measured by bi , is insigniﬁcantly
different from 1.0 in the period January 1982–May 2002, as well as in each of the
three subperiods, 1982–1987, 1988–1993, and 1994–2002. The estimates of abnormal
monthly returns are between −0.2% and 0.4% per month, although none are reliably
below zero.
Thus, it seems that the small-ﬁrm anomaly has disappeared since the initial
publication of the papers that discovered it. Alternatively, the differential risk premium
for small-capitalization stocks has been much smaller since 1982 than it was during
the period 1926–1982.
2.1.3. The turn-of-the-year effect
Keim (1983) and Reinganum (1983) showed that much of the abnormal return to
small ﬁrms (measured relative to the CAPM) occurs during the ﬁrst two weeks in
January. This anomaly became known as the “turn-of-the-year effect”. Roll (1983)
hypothesized that the higher volatility of small-capitalization stocks caused more of
them to experience substantial short-term capital losses that investors might want to
realize for income tax purposes before the end of the year. This selling pressure might
reduce prices of small-cap stocks in December, leading to a rebound in early January
as investors repurchase these stocks to reestablish their investment positions 4 .
Table 2 shows estimates of the turn-of-the-year effect for the period 1962–2001, as
well as for the 1962–1979 period analyzed by Reinganum (1983), and the subsequent
1980–1989 and 1990–2001 sample periods. The dependent variable is the difference in
the daily return to the CRSP NYSE small-ﬁrm portfolio (decile 1) and the return to the
CRSP NYSE large-ﬁrm portfolio (decile 10), (R1t − R10t ). The independent variable,
January, equals one when the daily return occurs during the ﬁrst 15 calendar days of
January, and zero otherwise. Thus, the coefﬁcient aJ measures the difference between
the average daily return during the ﬁrst 15 calendar days of January and the rest of the
4

There are many mechanisms that could mitigate the size of such an effect, including the choice of
a tax year different from a calendar year, the incentive to establish short-term losses before December,
and the opportunities for other investors to earn higher returns by providing liquidity in December.

944

G.W. Schwert
Table 2
Small ﬁrm/turn-of-the-year effect a , daily returns, 1962–2001
Sample period

a0

t(a0 = 0)

aJ

t(aJ = 0)

1962–2001

−0.00007

−0.92

0.00641

9.87

1962–1979

0.00009

0.97

0.00815

7.14

1980–1989

−0.00014

−0.73

0.00433

4.55

1990–2001

−0.00026

−1.72

0.00565

5.37

a (R − R ) = a + a
Januaryt + et . R1t is the return to the CRSP NYSE small1t
10t
0
J
ﬁrm portfolio (decile 1) and R10t is the return to the CRSP NYSE large-ﬁrm portfolio
(decile 10). January = 1 when the daily return occurs during the ﬁrst 15 calendar days
of January, and zero otherwise. The coefﬁcient of January measures the difference in
average return between small- and large-ﬁrm portfolios during the ﬁrst two weeks of
the year versus other days in the year. Heteroskedasticity-consistent standard errors
are used to compute the t–statistics.

year. If small ﬁrms earn higher average returns than large ﬁrms during the ﬁrst half
of January, aJ should be reliably positive.
Unlike the results in Table 1, it does not seem that the turn-of-the-year anomaly has
completely disappeared since it was originally documented. The estimates of the turnof-the-year coefﬁcient aJ are around 0.4% per day over the periods 1980–1989 and
1990–2001, which is about half the size of the estimate over the 1962–1979 period of
0.8%. Thus, while the effect is smaller than observed by Keim (1983) and Reinganum
(1983), it is still reliably positive.
Interestingly, Booth and Keim (2000) have shown that the turn-of-the-year anomaly
is not reliably different from zero in the returns to the DFA 9–10 portfolio over
the period 1982–1995. They conclude that the restrictions placed on the DFA fund
(no stocks trading at less than $2 per share or with less than $10 million in equity
capitalization, and no stocks whose IPO was less than one year ago) explain the
difference between the behavior of the CRSP small-ﬁrm portfolio and the DFA
portfolio. Thus, it is the lowest-priced and least-liquid stocks that apparently explain the
turn-of-the-year anomaly. This raises the possibility that market microstructure effects,
especially the costs of illiquidity, play an important role in explaining some anomalies
(see chapters 9 and 17 by Stoll and Easley and O’Hara, respectively).
2.1.4. The weekend effect
French (1980) observed another calendar anomaly. He noted that the average return
to the Standard and Poor’s (S&P) composite portfolio was reliably negative over
weekends in the period 1953–1977. Table 3 shows estimates of the weekend effect
from February 1885 to May 2002, as well as for the 1953–1977 period analyzed
by French (1980) and the 1885–1927, 1928–1952, and 1978–2002 sample periods
not included in French’s study. The dependent variable is the daily return to a broad

Ch. 15:

Anomalies and Market Efﬁciency

945

Table 3
Day-of-the-week effects in the U.S. stock returns a , February 1885−May 2002
Sample period

a0

t(a0 = 0)

aW

t(aW = 0)

1885–2002

0.0005

8.52

−0.0017

−10.13

1885–1927

0.0004

4.46

−0.0013

−4.96

1928–1952

0.0007

3.64

−0.0030

−6.45

1953–1977

0.0007

6.80

−0.0023

−8.86

1978–2002

0.0005

4.00

−0.0005

−1.37

a R

Weekend t + et . Weekend = 1 when the return spans Sunday (e.g.,
t = a0 + a W
Friday to Monday), and zero otherwise. The coefﬁcient of Weekend measures the
difference in average return over the weekend versus other days of the week. From
1885–1927, Dow Jones portfolios are used [see Schwert (1990)]. From 1928–May
2002, the Standard & Poor’s composite portfolio is used. Heteroskedasticity-consistent
standard errors are used to compute the t-statistics.

portfolio of U.S. stocks. For the 1885–1927 period, the Schwert (1990) portfolio based
on Dow Jones indexes is used. For 1928–2002, the S&P composite portfolio is used.
The independent variable, Weekend, equals one when the daily return spans a weekend
(e.g., Friday to Monday), and zero otherwise. Thus, the coefﬁcient aW measures the
difference between the average daily return over weekends and the other days of the
week. If weekend returns are reliably lower than returns on other days of the week,
aW should be reliably negative (and the sum of a0 + aW should be reliably negative
to conﬁrm French’s (1980) results). The results for 1953–1977 replicate the results
in French (1980). The estimate of the weekend effect for 1928–1952 is even more
negative, as previously noted by Keim and Stambaugh (1984). The estimate of the
weekend effect from 1885–1927 is smaller, about half the size for 1953–1977 and
about one-third the size for 1928–1952, but still reliably negative. Interestingly, the
estimate of the weekend effect since 1978 is not reliably different from the other days
of the week. While the point estimate of aW is negative from 1978–2002, it is about
one-quarter as large as the estimate for 1953–1977, and it is not reliably less than
zero. The estimate of the average return over weekends is the sum a0 + aW , which is
essentially zero for 1978–2002.
Thus, like the size effect, the weekend effect seems to have disappeared, or at least
substantially attenuated, since it was ﬁrst documented in 1980.
2.1.5. The value effect
Around the same time as early size-effect papers, Basu (1977, 1983) noted that ﬁrms
with high earnings-to-price (E/P) ratios earn positive abnormal returns relative to the
CAPM. Many subsequent papers have noted that positive abnormal returns seem to
accrue to portfolios of stocks with high dividend yields (D/P) or to stocks with high
book-to-market (B/M) values.

946

G.W. Schwert

Ball (1978) made the important observation that such evidence was likely to indicate
a fault in the CAPM rather than market inefﬁciency, because the characteristics that
would cause a trader following this strategy to add a ﬁrm to his or her portfolio would
be stable over time and easy to observe. In other words, turnover and transactions
costs would be low and information collection costs would be low. If such a strategy
earned reliable “abnormal” returns, it would be available to a large number of potential
arbitrageurs at a very low cost.
More recently, Fama and French (1992, 1993) have argued that size and value (as
measured by the book-to-market value of common stock) represent two risk factors
that are missing from the CAPM. In particular, they suggest using regressions of the
form:





Rit −Rft = ai + bi Rmt −Rft + si SMBt + hi HMLt + eit ,

(2)

to measure abnormal performance, ai . In Equation (2), SMB represents the difference
between the returns to portfolios of small- and large-capitalization ﬁrms, holding
constant the B/M ratios for these stocks, and HML represents the difference between
the returns to portfolios of high and low B/M ratio ﬁrms, holding constant the
capitalization for these stocks. Thus, the regression coefﬁcients si and hi represent
exposures to size and value risk in much the same way that bi measures the exposure
to market risk.
Fama and French (1993) used their three-factor model to explore several of the
anomalies that have been identiﬁed in earlier literature, where the test of abnormal
returns is based on whether ai = 0 in Equation (2). They found that abnormal returns
from the three-factor model in Equation (2) are not reliably different from zero for
portfolios of stocks sorted by: equity capitalization, B/M ratios, dividend yield, or
earnings-to-price ratios. The largest deviations from their three-factor model occur in
the portfolio of low B/M (i.e., growth) stocks, where small-capitalization stocks have
returns that are too low and large-capitalization stocks have returns that are too high
(ai > 0).
Fama and French (1996) extended the use of their three-factor model to explain the
anomalies studied by Lakonishok, Shleifer and Vishny (1994). They found no estimates
of abnormal performance in Equation (2) that are reliably different from zero based
on variables such as B/M, E/P, cash ﬂow over price (C/P), and the rank of past sales
growth rates.
In 1993, Dimensional Fund Advisors (DFA) began a mutual fund that focuses on
small ﬁrms with high B/M ratios (the DFA US 6–10 Value Portfolio). Based on the
results in Fama and French (1993), this portfolio would have earned signiﬁcantly
positive “abnormal” returns of about 0.5% per month over the period 1963–1991
relative to the CAPM. The estimate of the abnormal return to the DFA Value portfolio
from 1994–2002 in the last row of Table 1 is −0.2% per month, with a t-statistic of
−0.59. Thus, as with the DFA US 9–10 Small Company Portfolio, the apparent anomaly
that motivated the fund’s creation seems to have disappeared, or at least attenuated.

Ch. 15:

Anomalies and Market Efﬁciency

947

Davis, Fama and French (2000) collected and analyzed B/M data from 1929 through
1963 to study a sample that does not overlap the data studied in Fama and French
(1993). They found that the apparent premium associated with value stocks is similar
in the pre-1963 data to the post-1963 evidence. They also found that the size effect
is subsumed by the value effect in the earlier sample period. Fama and French (1998)
have shown that the value effect exists in a sample covering 13 countries (including
the USA) over the period 1975–1995. Thus, in samples that pre-date the publication
of the original Fama and French (1993) paper, the evidence supports the existence of
a value effect.
Daniel and Titman (1997) have argued that size and M/B characteristics dominate
the Fama–French size and B/M risk factors in explaining the cross-sectional pattern
of average returns. They conclude that size and M/B are not risk factors in an
equilibrium pricing model. However, Davis, Fama and French (2000) found that Daniel
and Titman’s results do not hold up outside their sample period.
2.1.6. The momentum effect
Fama and French (1996) have also tested two versions of momentum strategies.
DeBondt and Thaler (1985) found an anomaly whereby past losers (stocks with low
returns in the past three to ﬁve years) have higher average returns than past winners
(stocks with high returns in the past three to ﬁve years), which is a “contrarian”
effect. On the other hand, Jegadeesh and Titman (1993) found that recent past winners
(portfolios formed on the last year of past returns) out-perform recent past losers,
which is a “continuation” or “momentum” effect. Using their three-factor model in
Equation (2), Fama and French found no estimates of abnormal performance that are
reliably different from zero based on the long-term reversal strategy of DeBondt and
Thaler (1985), which they attribute to the similarity of past losers and small distressed
ﬁrms. On the other hand, Fama and French are not able to explain the short-term
momentum effects found by Jegadeesh and Titman (1993) using their three-factor
model. The estimates of abnormal returns are strongly positive for short-term winners.
Table 4 shows estimates of the momentum effect using both the CAPM benchmark
in Equation (1) and the Fama–French three-factor benchmark in Equation (2). The
measure of momentum is the difference between the returns to portfolios of high and
low prior return ﬁrms, UMD, where prior returns are measured over months −2 to −13
relative to the month in question 5 . The sample periods shown are the 1965–1989
period used by Jegadeesh and Titman (1993), the 1927–1964 period that preceded their
sample, the 1990–2001 period that occurred after their paper was published, and the
overall 1927–2001 period. Compared with the CAPM benchmark in the top panel of
Table 4, the momentum effect seems quite large and reliable. The intercept a is about

5

This Fama–French momentum factor for the period 1927–2001 is available from Ken French’s web
site, http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Momentum_Factor.zip.

Sample size (T )

456
300
756
144

1926–1964

1965–1989

1926–1989

1990–2001

0.0107

0.0091

0.0082

0.0100

0.0095

a

456
300
756
144

1926–1964

1965–1989

1926–1989

1990–2001

0.0123

0.0107

0.0100

0.0103

0.0110

2.95

7.77

4.61

5.72

8.25

2.71

6.37

4.00

5.33

6.98

t(a = 0)

−0.201

−0.170

−0.010

−0.204

−0.193

−0.063

−0.303

0.016

−0.415

−0.280

b

−1.83

−3.27

−0.13

−3.45

−3.75

−0.56

−3.50

0.22

−4.06

−3.48

t( b = 0)

0.093

−0.128

−0.132

−0.137

−0.102

s

0.54

−1.25

−1.17

−0.95

−1.14

t(s = 0)

−0.245

−0.519

−0.276

−0.525

−0.484

h

−1.35

−4.50

−2.08

−3.67

−4.65

t(h = 0)

a UMD = a + b(R −R ) + sSMB + hHML + e . UMD is the return to a portfolio that is long stocks with high returns and short stocks with low
t
mt
ft
t
t
t
t
returns in recent months (months −13 through −2). The market risk premium is measured as the difference in return between the CRSP value-weighted
portfolio of NYSE, Amex and Nasdaq stocks (Rm ) and the one-month Treasury bill yield (Rf ). SMBt is the difference between the returns to portfolios
of small- and large-capitalization ﬁrms, holding constant the B/M ratios for these stocks, and HMLt is the difference between the returns to portfolios of
high and low B/M ratio ﬁrms, holding constant the capitalization for these stocks. Heteroskedasticity-consistent standard errors are used to compute the
t-statistics.

900

1926–2001

Three-factor Fama–French benchmark

900

1926–2001

Single-factor CAPM benchmark

Sample period

Table 4
Momentum effects a , 1927–2001

948
G.W. Schwert

Ch. 15:

Anomalies and Market Efﬁciency

949

1% per month, with t-statistics between 2.7 and 7.0. In fact, the smallest estimate
of abnormal returns occurs in the 1965–1989 period used by Jegadeesh and Titman
(1993) and the largest estimate occurs in the 1990–2001 sample after their paper was
published 6 .
Fama and French (1996) noted that their three-factor model does not explain the
momentum effect, since the intercepts in the bottom panel of Table 4 are all reliably
positive. In fact, the intercepts from the three-factor models are larger than from the
single-factor CAPM model in the upper panel.
Lewellen (2002) has presented evidence that portfolios of stocks sorted on size and
B/M characteristics have similar momentum effects as those seen by Jegadeesh and
Titman (1993, 2001) and Fama and French (1996). He argues that the existence of
momentum in large diversiﬁed portfolios makes it unlikely that behavioral biases in
information processing are likely to explain the evidence on momentum.
Brennan, Chordia and Subrahmanyam (1998) found that size and B/M characteristics do not explain differences in average returns, given the Fama and French
three-factor model. Like Fama and French (1996), they found that the Fama–French
model does not explain the momentum effect. Finally, they found a negative relation
between average returns and recent past dollar trading volume. They argue that this
reﬂects a relation between expected returns and liquidity as suggested by Amihud and
Mendelson (1986) and Brennan and Subrahmanyam (1996).
Thus, while many of the systematic differences in average returns across stocks
can be explained by the three-factor characterization of Fama and French (1993),
momentum cannot. Interestingly, the average returns to index funds that were created
to mimic the size and value strategies discussed above have not matched up to the
historical estimates, as shown in Table 1. The evidence on the momentum effect seems
to persist, but may reﬂect predictable variation in risk premiums that are not yet
understood.
2.2. Predictable differences in returns through time
In the early years of the efﬁcient markets literature, the random walk model, in
which returns should not be autocorrelated, was often confused with the hypothesis
of market efﬁciency [see, for example, Black (1971)]. Fama (1970, 1976) made clear
that the assumption of constant equilibrium expected returns over time is not a part
of the efﬁcient markets hypothesis, although that assumption worked well as a rough
approximation in many of the early efﬁcient markets tests.
Since then, many papers have documented a small degree of predictability in stock
returns based on prior information. Examples include Fama and Schwert (1977) [shortterm interest rates], Keim and Stambaugh (1986) [spreads between high-risk corporate
6

Jegadeesh and Titman (2001) also show that the momentum effect remains large in the post
1989 period. They tentatively conclude that momentum effects may be related to behavioral biases
of investors.

950

G.W. Schwert

bond yields and short-term interest rates], Campbell (1987) [spreads between long- and
short-term interest rates], French, Schwert and Stambaugh (1987) [stock volatility],
Fama and French (1988) [dividend yields on aggregate stock portfolios], and Kothari
and Shanken (1997) [book-to-market ratios on aggregate stock portfolios]. Recently,
Baker and Wurgler (2000) have shown that the proportion of new securities issues
that are equity issues is a negative predictor of future equity returns over the period
1928–1997.
An obvious question given evidence of the time-series predictability of returns is
whether this is evidence of market inefﬁciency, or simply evidence of time-varying
equilibrium expected returns. Fama and Schwert (1977) found weak evidence that
excess returns to the CRSP value-weighted portfolio of NYSE stocks (in excess of the
one-month Treasury bill yield) are predictably negative. Many subsequent papers have
used similar metrics to judge whether the evidence of time variation in expected returns
seems to imply proﬁtable trading strategies. I am not aware of a paper that claims to
ﬁnd strong evidence that excess stock returns have been predictably negative, although
that may be an extreme standard for deﬁning market inefﬁciency since it ignores risk.
2.2.1. Short-term interest rates, expected inﬂation, and stock returns
Using data from 1953–1971, Fama and Schwert (1977) documented a reliable negative
relation between aggregate stock returns and short-term interest rates. Since Fama
(1975) had shown that most of the variation in short-term interest rates was due to
variation in expected inﬂation rates during this period, Fama and Schwert concluded
that expected stock returns are negatively related to expected inﬂation.
Table 5 shows estimates of the relation between stock returns and short-term interest
rates or expected inﬂation rates for the period January 1831–May 2002, as well as
for the 1953–1971 period analyzed by Fama and Schwert (1977). The dependent
variable Rmt is the monthly return to an aggregate stock portfolio [based on the Schwert
(1990) data for 1831–1925 and the CRSP value-weighted portfolio for 1926–2001, and
the Standard and Poor’s composite for 2002],
Rmt = a + gRft + et ,

(3)

where Rft is the yield on a short-term low-risk security (commercial paper yields from
1831–1925 and Treasury yields from 1926–2002) 7 . The negative relation between
expected stock returns and short-term interest rates is strongest for the 1953–1971
period, but the estimate is negative in all of the sample periods in Table 5, and it is
reliably different from zero over 1831–1925. The t-statistic for 1972–2002 is −1.08.
It is common to use the average difference between the return from a large portfolio
of stocks and the yield on a short-term bond (Rmt −Rft ) as an estimate of the market risk

7

Schwert (1989) describes the sources and methods used to derive the short-term interest rate series.

Ch. 15:

Anomalies and Market Efﬁciency

951

Table 5
Relation between stock market returns and short-term interest rates or expected
inﬂation a , January 1831 – May 2002
Sample period b

Rft

E(PPIt ) c

E(CPIt ) d

1831–2002 [2,053]

−2.073 (−3.50)

0.139 (0.93)

−0.591 (−0.68)

1831–1925 [1,136]

−3.958 (−4.58)

0.223 (1.53)

1926–1952 [324]

0.114 (0.03)

−0.056 (−0.10)

−0.580 (−0.46)

1953–1971 [228]

−5.559 (−2.57)

−0.412 (−0.43)

−2.448 (−1.13)

1972–2002 [357]

−1.140 (−1.08)

−0.612 (−0.95)

−1.258 (−1.29)

a R

mt = a + gXt + et ; Xt = Rft , E(PPIt ), or E(CPIt ). Rft is the yield on a one-month
security (commercial paper from 1831–1925 and Treasury securities from 1926–2002).
E(PPIt ) is the one-month-ahead forecast from a predictive model for PPI inﬂation:
PPIt = a0 + g0 Rft + [(1 − qL)/ [(1 − ÷L)] et , which is a regression of PPI inﬂation on the
short-term interest rate with ARMA(1,1) errors estimated with the prior 120 months
of data. Similarly, E(CPIt ) is the one-month-ahead forecast from a predictive model
for CPI inﬂation. Heteroskedasticity-consistent t-statistics are in parentheses next to
the coefﬁcient estimates.
b Sample size between brackets.
c 120 PPI observations are used to create the forecasting model, so the sample size
from 1831–2002 is 1,932 and from 1831–1925 it is 1,015.
d CPI data are available from 1931–2002, and 120 observations are used to create the
forecasting model, so the sample size from 1831–2002 is 952.

premium [e.g., Ibbotson Associates (1998) and Brealey and Myers (2000)]. This model
of the market risk premium implies that the coefﬁcient of Rft in Equation (3) should be
1.0, so that the negative estimates are even more surprising. For example, the t-statistic
for the hypothesis that the coefﬁcient of Rft equals 1.0 for 1972–2002 is −2.03.
Table 5 also shows estimates of the relation between stock returns and two measures
of the expected inﬂation rate, using the Consumer Price Index (CPI) and the Producer
Price Index (PPI). The model for expected inﬂation uses a regression of the inﬂation
rate on the short-term interest rate with ARMA(1,1) errors,
PPIt = a0 + g0 TBt +

(1 − qL)
et ,
(1 − ÷L)

(4)

where L is the lag operator, Lk Xt = Xt − k , estimated using the most recent 120 months
of data to forecast inﬂation in month t + 1 8 . It is notable that the negative relation
with stock returns is stronger for the interest rate Rft than for either measure of the
expected inﬂation rate, even though Rft is a part of the prediction model for inﬂation.
8

This model is similar the model used by Nelson and Schwert (1977) to model the CPI inﬂation rate
from 1953–1977. It is a ﬂexible model that is capable of representing a wide variety of persistence in
the inﬂation data.

952

G.W. Schwert

This shows that the interest rate is not a close proxy for the expected inﬂation rate
outside the 1953–1971 period. It also shows that the negative relation between stock
returns and short-term interest rates is not always due to expected inﬂation.
Thus, the apparent ability of short-term interest rates to predict stock returns is
strongest in the period used by Fama and Schwert (1977). Nevertheless, it does seem
that excess returns on stocks are negatively related to interest rates, suggesting a
slowly time-varying market risk premium. If the market risk premium varies because of
underlying economic fundamentals, this is not an anomaly that would allow investors
to trade to make abnormal proﬁts.
2.2.2. Dividend yields and stock returns
Using CRSP data for the period 1927–1986, Fama and French (1988) showed that
aggregate dividend yields predict subsequent stock returns. Many subsequent papers
have ampliﬁed this ﬁnding and several have questioned aspects of the statistical
procedures used, including Goyal and Welch (1999). Table 6 reproduces some of the
main results from Fama and French (1988), but also uses the Cowles (1939) data for
1872–1926 and additional CRSP data for 1987–2000. The equation estimated by Fama
and French is,
r(t, t + T ) = a + dY (t) + e(t, t + T ),

(5)

where Y (t) = D(t)/P(t − 1), P(t) is the price at time t, D(t) is the dividend for the
year preceding t, and r(t, t + T ) is the continuously compounded nominal return from
t to t + T .
What is clear from Table 6 is that the incremental data both before and after the
1927–1986 period studied by Fama and French shows a much weaker relation between
aggregate dividend yields and subsequent stock returns. None of the t-statistics for
the slope coefﬁcient d are larger than 2.0, even for the 1872–2000 sample which
includes the 1927–1986 data used by Fama and French (about half of the sample).
This occurs because the slope estimates are much smaller and the explanatory power
of the models (R2 ) is negligible.
Figure 1 illustrates the limitations of the dividend yield model for predicting stock
returns. Figure 1a shows the predictions of stock returns from the model based on
lagged dividend yield, D(t)/P(t − 1), for a one-year horizon based on estimates for
1927–1986 (the top row in the right-hand panel of Table 6). It also shows the one-year
return to short-term commercial paper and Treasury securities. The model for 1927–
1986 is used to predict stock returns both before and after the estimation sample, for
the 1872–2000 period. Until 1961, the predicted stock return is always higher than the
interest rate. However, starting in 1990, the predicted stock return is always below the
interest rate 9 .
9

Campbell and Shiller (1998) also stress the pessimistic implications of low aggregate dividend yields
and apparently followed the advice of their model (Wall Street Journal, January 13, 1997).

Ch. 15:

Anomalies and Market Efﬁciency

953

Table 6
Relation between stock market returns and aggregate dividend yields a , 1872–2000
Return horizon, T

Y (t) = D(t)/P(t − 1)

Y (t) = D(t)/P(t)
d

t(d)

R2

S(e)

d

t(d)

R2

S(e)

1

2.21

1.00

0.01

0.21

5.25

3.03

0.07

0.20

2

6.88

2.78

0.08

0.30

8.85

3.53

0.09

0.29

3

9.28

3.23

0.12

0.33

11.25

3.82

0.12

0.33

4

12.05

4.00

0.16

0.36

12.55

4.54

0.12

0.37

1

0.53

0.52

−0.01

0.18

1.27

1.16

0.00

0.18

2

2.03

1.44

0.01

0.26

1.11

0.66

−0.01

0.26

3

2.30

1.33

0.00

0.30

2.17

1.04

0.00

0.30

4

3.87

1.83

0.02

0.34

3.40

1.42

0.01

0.34

1

0.84

0.64

−0.01

0.16

0.55

0.29

−0.02

0.16

2

2.29

1.20

0.00

0.22

−1.14

−0.47

−0.02

0.22

3

1.49

0.70

−0.01

0.24

1.16

0.42

−0.02

0.24

4

3.51

1.40

0.01

0.28

4.48

1.39

0.01

0.28

1927–1986, N = 60

1872–2000, N = 129

1872–1926, N = 55

a r(t, t + T ) = a + dY (t) + e(t, t + T ). P(t) is the price at time t. Y (t) equals either D(t)/P(t)

or D(t)/P(t − 1), where D(t) is the dividend for the year preceding t. r(t, t + T ) is the
continuously compounded nominal return from t to t + T to the CRSP value-weighted
portfolio from 1926–2000 and to the Cowles portfolio from 1872–1925. The regressions
for two-, three- and four-year returns use overlapping annual observations. The t-statistics
t(d) use heteroskedasticity- and autocorrelation-consistent standard error estimates. R2 is
the coefﬁcient of determination, adjusted for degrees of freedom, and S(e) is the standard
error of the regression.

Figure 1b shows the investment results that would have occurred from following a
strategy of investing in short-term bonds, rather than stocks, when the dividend yield
model in Table 6 predicts stock returns lower than interest rates. Both that strategy and
a benchmark buy-and-hold strategy start with a $1000 investment in 1872. By the end
of 1999, the buy-and-hold strategy is worth almost $6.7 million, whereas the dividend
yield asset allocation strategy is worth just over $2.2 million. This large difference
reﬂects the high stock returns during the 1990s when the dividend yield model would
have predicted low stock returns. In short, the out-of-sample prediction performance
of this model would have been disastrous 10 .
10 Of course, it is possible that a less extreme asset-allocation model that reduced exposure to stocks
when dividend yields were low relative to interest rates would perform better.

954

G.W. Schwert
35%
30%
25%
20%
15%
10%
5%
0%
-5%
2001

1991

1981

1971

1961

1951

1941

1931

1921

1911

1901

1891

1881

1871

-10%

Fig. 1a. Predictions of stock returns based on lagged dividend yields, D(t)/P(t − 1), and the regression
sample from 1927–1986 versus interest rates, 1872–2000. Solid line, interest rate; dashed line, predicted
stock return.
$10,000,000

$1,000,000

$100,000

$10,000

$1,000

2001

1991

1981

1971

1961

1951

1941

1931

1921

1911

1901

1891

1881

1871

$100

Fig. 1b. Value of $1 invested in stocks (“buy-and-hold”) versus a strategy based on predictions of stock
returns from a regression on lagged dividend yields, D(t)/P(t − 1), from 1927–1986. When predicted
stock returns exceed interest rates, invest in stocks for that year. When predicted stock returns are below
interest rates, invest in short-term money market instruments, 1872–2000. Solid line, buy-and-hold;
dashed line, dividend yield strategy.

3. Returns to different types of investors
3.1. Individual investors
One simple corollary of the efﬁcient markets hypothesis is that uninformed investors
should be able to earn “normal” rates of return. It should be just as hard to select
stocks that will under-perform as to select stocks that will out-perform the market,
otherwise, a strategy of short-selling or similarly taking opposite positions would earn
above-normal returns. Of course, investors who trade too much and incur unnecessary

Ch. 15:

Anomalies and Market Efﬁciency

955

and unproductive transactions costs should earn below-normal returns net of these
costs.
Odean (1999) examined data from 10 000 individual accounts randomly selected
from a large national discount brokerage ﬁrm for the period 1987–1993. This sample
covers over 160 000 trades. Because the data source is a discount brokerage ﬁrm,
recommendations from a retail broker are presumably not the source of information
used by investors to make trading decisions. Odean found that traders lower their
returns through trading, even ignoring transactions costs, because the stocks they sell
earn higher subsequent returns than the stocks they purchase.
Barber and Odean (2000, 2001) used different data from the same discount
brokerage ﬁrm and found that active trading accounts earn lower risk-adjusted net
returns than less-active accounts. They have also found that men trade more actively
than women and thus earn lower risk-adjusted net returns and that the stocks that
individual investors buy subsequently under-perform the stocks that they sell.
The results in these papers are anomalies, but not because trading costs reduce net
returns, or because men trade more often than women. They are anomalies because
it seems that these individual investors can identify stocks that will systematically
under-perform the Fama–French three-factor model in Equation (2). One potential clue
in Odean (1999) is that these investors tend to sell stocks that have risen rapidly in
the recent weeks, suggesting that the subsequent good performance of these stocks
is due to the momentum effect described earlier. By going against momentum, these
individual investors may be earning lower returns.

3.1.1. Closed-end funds
The closed-end fund puzzle has been recognized for many years. Closed-end funds
generally trade in organized secondary trading markets, such as the NYSE. Since
marketable securities of other ﬁrms constitute most of the assets of closed-end funds, it
is relatively easy to observe both the value of the stock of the closed-end fund and the
value of its assets. On average, in most periods, the fund trades at less than the value
of its underlying assets, which leads to the “closed-end fund discount” anomaly.
Thompson (1978) was one of the ﬁrst to carefully show that closed-end fund
discounts could be used to predict above-normal returns to the shares of closed-end
funds. Lee, Shleifer and Thaler (1991) argued that the time-series behavior of closedend fund discounts is driven by investor sentiment, with discounts shrinking when
individual investors are optimistic. They found that discounts shrink at the same time
that returns to small-capitalization stocks are relatively high.
Pontiff (1995) updated and extended Thompson’s tests and found that the abnormal
returns to closed-end funds are due to mean reversion in the discount, not to unusual
returns to the assets held by the funds. In other words, when the prices of closedend fund shares depart too much from their asset values, the difference tends to grow
smaller, leading to higher-than-average returns to these shares.

956

G.W. Schwert

Since the anomaly here pertains to the prices of the closed-end fund shares, not to the
underlying investment portfolios, and since closed-end fund shares are predominantly
held by individual investors, this evidence sheds light on the investment performance
of some individual investors.

3.2. Institutional investors
Studies of the investment performance of institutional investors date back at least
to Cowles (1933). Cowles concluded that professional money managers did not
systematically outperform a passive index fund strategy (although he did not use
the term “index fund”). There is an extensive literature studying the returns to large
samples of open-end mutual funds and, more recently, to private hedge funds.
3.2.1. Mutual funds
Hendricks, Patel and Zeckhauser (1993) have found short-run persistence in mutual
fund performance, although the strongest evidence is of a “cold-hands” phenomenon
whereby poor performance seems more likely to persist than would be true by random
chance.
Malkiel (1995) studied a database from Lipper that includes all open-end equity
funds that existed in each year of the period 1971–1991. Unlike many mutual fund
databases that retroactively omit funds that go out of business or merge, Malkiel’s
data do not suffer from the survivorship bias stressed by Brown, Goetzmann, Ibbotson
and Ross (1992). Malkiel found that mutual funds earn gross returns that are consistent
with the CAPM in Equation (1) and net returns that are inferior because of the expenses
of active management. He also found evidence of performance persistence for the
1970s, but not for the 1980s.
Carhart (1997) also used a mutual-fund database that is free of survivorship bias
and found that the persistence identiﬁed by Hendricks, Patel and Zeckhauser (1993)
is explainable by the momentum effect for individual stocks described earlier. After
taking this into account, the only evidence of persistent performance of open-end funds
is that poorly performing managers have “cold hands”.
3.2.2. Hedge funds
The problem of assessing performance for hedge funds is complicated by the unusual
strategies used by many of these funds. Fung and Hsieh (1997) showed that hedge
fund returns are not well characterized as ﬁxed linear combinations of traditional
asset classes, similar to the Fama–French three-factor model. Because of changing
leverage, contingent claims, and frequent changes in investment positions, traditional
fund performance measures are of dubious value.

Ch. 15:

Anomalies and Market Efﬁciency

957

3.2.3. Returns to IPOs
The large returns available to investors who can purchase stocks in underwritten ﬁrmcommitment initial public offerings (IPOs) at the offering price have been the subject
of many papers, dating at least to Ibbotson (1975). Most of the literature on high
average initial returns to IPOs focuses on the implied underpricing of the IPO stock
and the effects on the issuing ﬁrm, but this evidence has equivalent implications for
abnormal proﬁts to IPO investors. Several theories have been developed to explain
the systematic underpricing of IPO stocks (see chapter 5 in this Handbook by Ritter).
Many of these theories point to the difﬁculty of individual investors in acquiring the
most underpriced of IPOs, which is why I include this discussion in the section under
returns to institutional investors.
How large are the returns to IPO investing? Figure 2a shows the cumulative value
of a strategy of investing $1000 starting in January 1960 in a random sample of IPOs,
selling after one month, and then re-investing in a new set of IPOs in the next month.
The returns to IPOs are from Ibbotson, Sindelar and Ritter (1994) and are updated on
Jay Ritter’s website [http://bear.cba.uﬂ.edu/ritter/ipoall.htm]. For comparison, Figure 2a
also shows the value of investing in the CRSP value-weighted portfolio over the same
period. By December 2001, the CRSP portfolio is worth about $74, 000. On the other
hand, the IPO portfolio strategy is worth over $533 × 1033 . Clearly, no one has been
able to follow this strategy, or people like Bill Gates and Warren Buffet would be
viewed as rank amateurs in the wealth-creation business!

$1.E+36

IPO strategy

Value of $1,000 Investment in 1960

$1.E+33
$1.E+30
$1.E+27
$1.E+24
$1.E+21
$1.E+18
$1.E+15

CRSP market strategy

$1.E+12
$1.E+9
$1.E+6
$1.E+3

2000

1998

1996

1994

1992

1990

1988

1986

1984

1982

1980

1978

1976

1974

1972

1970

1968

1966

1964

1962

1960

$1.E+0

Fig. 2a. Value each month of $1000 invested in January 1960 in a random sample of IPOs. At the end
of each month, the IPO stocks are sold and the proceeds invested in a new sample of IPOs in the next
month. The scale is logarithmic and the December 2001 value of the IPO strategy is over $533×1033 .
For comparison, the strategy of investing $1000 in the CRSP value-weighted market portfolio in January
1960 is worth almost $74, 000 by December 2001.

958

G.W. Schwert

What are the impediments to IPO investing as a strategy for earning abnormal
returns? First, it is difﬁcult to be included in the allocations made by the underwriters.
Investment banks usually allocate shares ﬁrst to large institutional customers (see, e.g.,
Wall Street Journal, January 27, 2000). If the institutional customers can distinguish
between deals that are more underpriced and those that are less underpriced, then the
shares available to individual investors are likely to offer lower initial returns. It has
also been alleged that in exchange for potential favors (“spinning”), investment banks
allocate shares to preferred individual clients such as politicians, including House
Speaker Thomas Foley (Wall Street Journal, July 20, 1993) and Senator Alphonse
D’Amato, a prominent member of the Senate Banking Committee (Wall Street Journal,
June 6, 1996), or to the executives of private ﬁrms that are considering going public
in the near future (see, e.g., Wall Street Journal, November 12, 1997). Thus, a typical
individual investor would have difﬁculty acquiring shares in the IPOs that are most
underpriced.
Second, many investment banks discourage the practice of buying shares in an IPO
and then selling the shares in the secondary market (“ﬂipping”). Forcing IPO investors
to hold shares for more than a month, for example, would increase the risk and costs
of pursuing the IPO strategy outlined above (although it would still seem extremely
proﬁtable). To the extent that underwriters sometimes provide informal price support
in the after-market by buying shares at a price close to the IPO price, it is clear
why they would want to discourage ﬂipping when initial returns are negative. On the
other hand, when the after-market price rises dramatically and volume is high, ﬂipping
is beneﬁcial to the underwriter by increasing market-maker proﬁts. It is necessary
for some investors who purchased shares in the IPO to sell their shares to create a
public ﬂoat and therefore liquidity. Indeed, there has been recent acknowledgement
that ﬂipping is useful in helping to create liquidity (see, e.g., Wall Street Journal,
February 2, 2000).
Another unusual feature of IPO returns is their apparent persistence, shown in
Figure 2b. While average IPO returns are positive in almost every month from 1960
to 2001, there seem to be very noticeable cycles in these returns, with high returns
following high returns and vice versa. According to Lowry and Schwert (2002), these
cycles are explained by two important factors. First, the types of ﬁrms that go public
tend to be clustered in time, so that cross-sectional differences in IPO returns that
may be due to information asymmetry, for example, show up in average returns across
IPOs. Second, the learning that occurs during the registration period (as underwriters
talk to potential investors) affects IPO prices and subsequent returns for the similartype ﬁrms that are in the IPO process at the same time, and this process usually lasts
more than one month. Lowry and Schwert argue that ﬁrms cannot use the persistence
in IPO returns shown in Figure 2b to optimally time their IPOs (trying to minimize
initial returns). By analogy, investors cannot time their participation in the IPO market
(trying to maximize their returns).

Ch. 15:

Anomalies and Market Efﬁciency

959

Monthly Percentage Return to IPOs

125%
100%
75%
50%
25%
0%
-25%

2000

1998

1996

1994

1992

1990

1988

1986

1984

1982

1980

1978

1976

1974

1972

1970

1968

1966

1964

1962

1960

-50%

Fig. 2b. Ibbotson, Sindelar and Ritter’s (1994) monthly data on the average initial returns to IPO investors,
January 1960 to December 2001.

Thus, while IPOs seem to offer large abnormal returns to investors who can obtain
shares in the IPO allocation, it is not clear that this is an anomaly that can beneﬁt most
investors.
3.3. Limits to arbitrage
It has long been recognized that transactions costs can limit the ability of traders to
proﬁt from mispricing [e.g., Jensen (1978)]. The question of how market frictions
affect asset prices and allow apparent anomalies to persist has received increasing
attention in recent years.
Shleifer and Vishny (1997) have argued that agency problems associated with
professional money managers, along with transactions costs, can cause mispricing
to persist and that many anomalies are a result of such market frictions. Pontiff
(1996) has shown that the absolute value of closed-end fund discounts and premiums
are correlated with various measures of the costs of trying to arbitrage mispricing,
including the composition of the funds’ portfolios and the level of interest rates.
Table 7 lists nine papers that appeared in a special issue of the Journal of Financial
Economics, all of which study the effects on asset prices of various kinds of frictions.
Several of these papers contain evidence similar to Pontiff ’s in that the extent of
apparent pricing anomalies is correlated with the size of transactions costs.

4. Long-run returns
DeBondt and Thaler (1985) tracked the returns to “winner” and “loser” portfolios for
36 months after portfolio formation and noted a slow drift upward in the cumulative
abnormal returns (CARs) of loser stocks that had performed poorly in the recent

960

G.W. Schwert

Table 7
Contents of the Special Issue of the Journal of Financial Economics on the Limits to Arbitrage,
Vol. 66(2–3), November/December 2002
Authors

Paper title

Joseph Chen, Harrison Hong
and Jeremy C. Stein

Breadth of ownership and stock returns

Charles M. Jones and
Owen A. Lamont

Short sale constraints and stock returns

Christopher C. Geczy,
David K. Musto and
Adam V. Reed

Stocks are special too: An analysis of the equity lending market

Gene D’Avolio

The market for borrowing risk

Darrell Dufﬁe,
Nicolae Garleanu and
Lasse Heje Pedersen

Securities lending, shorting, and pricing

Dilip Abreu and
Markus K. Brunnermeier

Synchronization risk and delayed arbitrage

Denis Gromb and
Dimitri Vayanos

Equilibrium and welfare in markets with ﬁnancially constrained
arbitrageurs

Randolph B. Cohen,
Paul A. Gompers and
Tuomo Vuolteenaho

Who underreacts to cash-ﬂow news? Evidence from trading
between individuals and institutions

Arvind Krishnamurthy

The bond/old-bond spread

past. They interpret this result as evidence of excessive pessimism following poor
performance, making the stocks of loser ﬁrms proﬁtable investments.
Ball, Kothari and Shanken (1995) have argued that poor stock return performance
will generally lead to higher leverage, because the value of the stock drops more than
the value of the ﬁrm’s debt. The increase in leverage should lead to higher risk and
higher expected returns than would be reﬂected in risk estimates from a period before
the drop in stock price. They have also pointed out that many of the stocks earning
the highest returns have very low prices, so that microstructure effects, such as a large
proportional bid–ask spread, can reduce subsequent performance by large amounts.
4.1. Returns to ﬁrms issuing equity
Using both CARs and buy-and-hold abnormal returns (BHARs), Ritter (1991)
measured post-IPO stock performance and concluded that IPO stocks yield belownormal returns in the 36 months following the IPO. He interpreted this result as
evidence that investors become too optimistic about IPO ﬁrms, inﬂating the initial
IPO return (from the IPO price to the secondary market trading price), and lowering

Ch. 15:

Anomalies and Market Efﬁciency

961

subsequent returns. Loughran and Ritter (1995) extended Ritter’s analysis using a
sample of IPOs from 1970–1990.
Brav and Gompers (1997) and Brav, Geczy and Gompers (2000) have studied the
returns to IPO ﬁrms for the period 1975–1992 and found that underperformance is
concentrated primarily in small ﬁrms with low book-to-market ratios. They argue that
this is the same behavior as seen by Fama and French (1993) in their tests of their threefactor model and that the IPO anomaly is thus a manifestation of a general problem in
pricing small ﬁrms with low book-to-market ratios. Brav, Geczy and Gompers (2000)
also studied seasoned equity offerings (SEOs) and found that momentum, in addition
to the Fama–French three-factor model, helps explain the behavior of returns after
SEOs. Eckbo, Masulis and Norli (2000) have shown that the reduction in leverage
that occurs when new equity is issued reduces subsequent equity risk exposure and
thus contributes to the apparent unusual behavior of returns following SEOs.
Schultz (2003) used simulations to study the behavior of abnormal return measures
after events that are triggered by prior stock price performance. For example, if a ﬁrm
chooses to issue stock after its price has risen in the recent past, even if the stock
price is fully rational, many of the popular measures of long-run abnormal returns
will falsely reveal subsequent poor performance (he refers to this as “pseudo-market
timing”). The driving force behind his result is that the covariance between current
excess returns and the number of future offerings is positive.
Many papers have analyzed long-run stock returns following a variety of events and
a large number of papers have also analyzed the properties of these long-run stock
return tests and alternative hypotheses to explain these types of results.
Fama (1998) has argued that the problem of measuring normal returns is particularly
important when measuring long-run returns, because model problems that may be
small in a day or a month can be compounded into larger apparent effects over three or
ﬁve years. He has also argued that most papers that attribute apparent abnormal stock
returns to behavioral effects are not testing a speciﬁc alternative model. Recent papers
by Barberis, Shleifer and Vishny (1998), Daniel, Hirshleifer and Subrahmanyam (1998,
2001) and Barberis and Shleifer (2003) are examples of models that make predictions
for short- and long-run stock returns from irrational investor behavior. At this point,
however, it is unclear whether these models have refutable predictions that differ from
tests that have already been performed.
Several papers have studied the statistical properties of long-run CARs and BHARs,
including Barber and Lyon (1997), Kothari and Warner (1997) and Mitchell and
Stafford (2000). All of these papers conclude that it is difﬁcult to ﬁnd long-run
abnormal return measures that have well-speciﬁed statistical properties and reasonable
power. Mitchell and Stafford (2000) argue that the calendar-time regression approach
originally used by Jaffe (1974) and Mandelker (1974), and advocated by Fama (1998),
provides more reliable inferences than long-run CARs or BHARs.

962

G.W. Schwert

4.2. Returns to bidder ﬁrms
The returns to bidder ﬁrms’ stocks provide another example of potentially anomalous
post-event behavior. Since at least Asquith (1983), researchers have noted that there
is a pronounced downward drift in the cumulative abnormal returns to the stocks of
ﬁrms that are bidders in mergers. One interpretation of this evidence is that bidders
overpay and that it takes the market some time to gradually learn about this mistake.
Schwert (1996) analyzed the returns to 790 NYSE and Amex-listed bidders for the
period 1975–1991 and found a negative drift of about 7% in the year following the
announcement of the bid. He concluded, however, that the explanation for this drift is
the unusually good stock return performance of the bidder ﬁrms in the period prior to
the bid. To measure abnormal performance, he used a market model regression,
Rit = ai + bi Rmt + eit ,

(6)

where Rit is the return to the bidder ﬁrm and Rmt is the return to the CRSP valueweighted portfolio in period t, based on 253 daily returns in the year before the event
analysis (which starts six months before the ﬁrst bid is announced). Using the estimates
of ai and bi , abnormal returns are estimated, averaged, and cumulated for the period
from 127 trading days before the bid announcement to 253 trading days after the bid
announcement,
eik = Rik − ai − bi Rmk
790

AR k =
eik
(7)

i=1

CAR J =

J


AR k .

k = −127

The dashed line in Figure 3 represents the CAR to the bidder ﬁrms in Equation (7). It
drifts downward after the ﬁrst bid announcement to about −8% a year afterwards. The
solid line in Figure 3 represents a simple adjustment to the calculation of abnormal
returns to bidders’ stocks: the intercept ai is set equal to zero. This adjusted cumulative
abnormal return does not have a noticeable drift in Figure 3, which is consistent with
the efﬁcient markets hypothesis.
The adjustment eliminates the negative drift in abnormal returns because the
estimated intercepts in the market model are systematically positive for bidder stocks
in the year and a half before the bid, reﬂecting the fact that bidder ﬁrms are more
likely to have recently experienced good performance, at least in terms of their stock
prices. This abnormally good performance vanishes after the ﬁrst bid (as it should in
an efﬁcient market).
Note that this does not mean that the bid somehow caused something bad to happen
to the bidder ﬁrm; it simply means that bidders’ stock returns were normal in the period

Ch. 15:

Anomalies and Market Efﬁciency

963

Cumulative Average Abnormal Returns

2%

0%

-2%

-4%

-6%

-8%

252

231

210

189

168

147

126

105

84

63

42

0

21

-21

-42

-63

-84

-105

-126

-10%

Event Date Relative to First Bid

Fig. 3. Cumulative average abnormal returns to bidder ﬁrms’ stocks from trading day −126 to +253
relative to the ﬁrst bid for NYSE- and AMEX-listed target ﬁrms for the period 1975–1991. Market model
parameters used to deﬁne abnormal returns are estimated using the CRSP value-weighted portfolio for
days −379 to −127. The solid line shows the effect of setting the intercepts to zero, since the bidder
ﬁrms seem to have abnormally high stock returns during the estimation period (shown by the dotted
line that drifts downward from day −126 to day +253). There are 790 NYSE- or Amex-listed bidder
ﬁrms that made the ﬁrst bid for exchange-listed target ﬁrms in this period. Solid line, ﬁrst bidder CAR
(intercept = 0); dotted line, ﬁrst bidder CAR.

following the announcement of the bid. The unusually positive performance of bidders’
stocks before the bid is an example of sample selection bias: the decisions of bidder
ﬁrms to pursue acquisitions is correlated with their past stock price performance.
It is important to note that it is not necessary to adjust the CAR for the sample
of target ﬁrms. The CAR for target ﬁrms rises gradually before the ﬁrst bid
announcement, reﬂecting bid anticipation, and jumps on the day of the announcement.
After that, it remains ﬂat for the next year. In contrast with the bidder ﬁrms, the target
ﬁrms’ intercepts from the estimated market models are not unusually large, reﬂecting
neither positive nor negative stock price performance in the year and half before they
become targets.
Mitchell and Stafford (2000) used the calendar-time portfolio method suggested by
Fama (1998) to measure abnormal returns to acquiring ﬁrms. They concluded that an
equal-weighted portfolio of acquirers seems to earn negative abnormal returns over a
three-year window following an acquisition, but that a value-weighted portfolio does
not, using the Fama–French three-factor model in Equation (2) as a benchmark. This
method of measuring the size and signiﬁcance of abnormal returns is not affected by
unusual prior performance in the same way as the CARs in Figure 3.
Loughran and Vijh (1997) compared buy-and-hold returns to bidders’ stocks
measured ﬁve years after acquisitions with returns to control ﬁrms that are matched on
size and book-to-market characteristics. They found that stock mergers are followed

964

G.W. Schwert

by negative excess returns and cash tender offers are followed by positive excess
returns. Since the choice of payment by the bidder is similar to a choice concerning
equity ﬁnancing, the sample selection issues raised by Schultz (2003) might affect the
Loughran and Vijh (1997) results.

5. Implications for asset pricing
Consistent with Fama’s observation (1970, 1976, 1998) that tests of market efﬁciency
are necessarily joint tests of a model of expected returns, evidence of anomalies is also
potentially evidence of a short-coming in the implied asset-pricing model used for the
test. One example of this phenomenon that has created much activity in the ﬁnance
literature in recent years is the Fama and French (1993) three-factor model, which
incorporates the size and book-to-market anomalies into the asset-pricing model.
5.1. The search for risk factors
An obvious question that arises from empirically motivated adjustments of assetpricing models is whether the new, extended model accurately describes equilibrium
behavior, or is just a convenient offshoot of the anomalous ﬁndings that motivated the
extension. For example, the simple two-parameter CAPM of Sharpe (1964) and Lintner
(1965) was motivated by portfolio theory. Many people have developed extensions
of theoretical asset-pricing models that include multiple factors (see, for example,
chapters 10, 11 and 12 in this Handbook by Dybvig and Ross, Dufﬁe, and Ferson,
respectively), although none of these models match closely with the empirical Fama–
French model.
On the other hand, as Fama and French (1993) have pointed out, some versions of
multifactor models are vague about the risk factors that might lead to differences in
expected returns across assets, so that their empirical proxies (size and book-to-market)
may be reﬂecting equilibrium trade-offs between risk and expected return. The Fama
and French (1993, 1996) tests are consistent with their three-factor model being an
adequate asset-pricing model, in the sense that the intercepts in their regression tests
(measuring average abnormal returns to different portfolio strategies) are not reliably
different from zero 11 .
There is at least one other issue that must be addressed, however, before concluding
that the three-factor model is an accurate equilibrium-pricing model. As noted by
MacKinlay (1995), the estimates of factor risk premiums from the Fama–French
model seem very high, particularly for the book-to-market factor. In some ways,

11

An exception is that the Fama–French (1993) portfolio of the smallest ﬁrms with the lowest book-tomarket ratios has a reliably negative intercept. Also, as mentioned above, the Fama–French model does
not seem to explain the momentum evidence.

Ch. 15:

Anomalies and Market Efﬁciency

965

this is analogous to the “equity premium puzzle” that has been frequently discussed
in the macro-ﬁnance literature (see chapter 13 in this Handbook by Campbell). If
the estimates of risk premiums are too high (or too low) to be consistent with the
underlying economic theory that motivates the model, the fact that average returns
are linearly related to the risk factors is not sufﬁcient to conclude that the market is
efﬁcient. If the book-to-market premium is too high, as argued by MacKinlay, then
returns vary too much with this risk factor. From this perspective, the evidence that
the three-factor model provides a good linear model of risk and return may be just a
fortuitous description of an anomaly.
5.2. Conditional asset pricing
The evidence on time-varying expected returns has obvious implications for the
growing literature on conditional asset-pricing models. On the other hand, the poor
out-of-sample performance of some of the predictor variables raises questions about
their role in asset prices.
5.3. Excess volatility
I have not addressed the question raised by Shiller (1981a,b) of whether stock market
volatility is “too high”. His provocative papers on “excess volatility” stimulated many
rebuttals, including Kleidon (1986) and Marsh and Merton (1986), that raised questions
about the validity and robustness of his statistical methods. While I have written many
papers on the behavior of stock volatility, some of which raise questions about why
volatility varies over time as much as it does [e.g., Schwert (1989)], I do not believe that
this literature is closely linked with the literature on anomalies and market efﬁciency.
In my 1991 review of Shiller (1989), I argue that Shiller’s research on excess volatility
is really a test of a particular valuation model and provides no guidance on how to
identify or proﬁt from mispricing.
5.4. The role of behavioral ﬁnance
Finally, there is the issue of whether the ﬁndings in the anomalies literature can
be combined with behavioral theories from the psychology literature to create new
asset-pricing theories that combine economic equilibrium concepts with psychological
concepts to create an improved asset-pricing model (see chapter 18 by Barberis and
Thaler). My impression, to date, is that the attempts to proceed in this direction have
produced models that might explain some of the existing anomalies, but they make no
predictions for observable behavior that have not already been tested extensively 12 .
In other words, the new behavioral theories have not yet made predictions that are

12

Fama (1998) is less sympathetic to the ability of these new models to explain existing anomalies.

966

G.W. Schwert

refutable with new tests. Going beyond the stage of building theories to explain the
“stylized facts” that already exist will be a signiﬁcant challenge.

6. Implications for corporate ﬁnance
What implications do market efﬁciency and anomalies have for corporate ﬁnance? The
standard textbook treatment of corporate ﬁnance in an efﬁcient market [for example,
Brealey and Myers (2000)] tells ﬁrms to choose projects that maximize value, and
perhaps choose capital structures or dividend policies that create value, but to take the
market prices of their stocks and bonds as given and more or less correct.
6.1. Firm size and liquidity
How would the kinds of anomalies discussed above change this advice, if at all? To
the extent that the small-ﬁrm effect is real, ﬁrms that merge and become larger would
have a lower cost of capital, and therefore a higher value. But this kind of ﬁnancial
synergy is hard to believe. In fact, it raises the question of whether ﬁrm size somehow
proxies for a more fundamental source of risk or value.
Amihud and Mendelson (1986) have argued that ﬁrm size proxies for the illiquidity
of the stock and that higher transactions costs for small ﬁrms raise the required gross
return so that net expected returns are equalized, given the risk of the stock. In their
empirical work, they found that the cross-sectional dispersion in average returns across
portfolios of NYSE stocks sorted on bid–ask spreads is similar to the dispersion in
average returns across portfolios sorted on risk estimates. From this perspective, size
is not a risk factor, but rather a proxy for differential transactions costs 13 . Thus,
actions that increase the liquidity of a ﬁrm’s stock would reduce required returns
and increase the stock price if such actions were costless. Decisions on whether the
ﬁrm should undertake policies that increase liquidity depend on whether the beneﬁts
exceed the costs. There has been much recent work on the linkages between market
microstructure, asset pricing, and corporate ﬁnance (see chapter 17 in this Handbook
by Easley and O’Hara).
6.2. Book-to-market effects
Fama and French interpret the book-to-market ratio as an indicator of “value” versus
“growth” stocks, and the HML risk factor as reﬂecting “distress risk”. In their tests,
ﬁrms with high book-to-market ratios or risk sensitivities are often ﬁrms whose value

13

The apparent disappearance of the size effect discussed in Section 2.1, if true, would be problematic
for the liquidity effect unless small-capitalization stocks have relatively low transactions costs in recent
years.

Ch. 15:

Anomalies and Market Efﬁciency

967

has fallen recently because of bad performance. These ﬁrms are more likely to suffer
ﬁnancial distress costs in future periods if further bad news hits.
To the extent that Fama and French (1993) are correct that SMB and HML reﬂect
priced risk factors, then reducing a ﬁrm’s exposure to these types of risk would lower
the expected return on its stock, and therefore, its cost of capital. Such a change would
not increase the value of the ﬁrm, however, so there is no obvious prescription for
managerial behavior.
If Daniel and Titman (1997) are correct that ﬁrms with lower book-to-market ratios
have lower expected returns, holding risk constant, then corporate ﬁnancial policies
designed to lower B/M would improve ﬁrm value by lowering the cost of capital. Of
course, holding book value constant, this is equivalent to increasing the market value
of the stock, which is generally good for shareholders (and not a new insight).
In the corporate ﬁnance literature, the book-to-market ratio has been interpreted
as a measure of the type of investment opportunities that are available to the ﬁrm.
For example, Smith and Watts (1992) have interpreted high book-to-market ﬁrms as
those with “assets-in-place” and low book-to-market ﬁrms as those with relatively more
“growth options”. From this perspective, the fact that accounting book values make no
attempt to measure the value of growth options drives the cross-sectional dispersion
in book-to-market ratios. Interpreted this way, the book-to-market ratio is exogenous
and reﬂects the investment opportunity set facing the ﬁrm. It would not make sense,
for example, to advise ﬁrms to sell assets in place and invest in growth options just
to lower book-to-market and, from the perspective of Daniel and Titman, to lower the
cost of capital.
There has also been a substantial literature using Tobin’s Q-ratio (a close relative
of book-to-market) as a proxy for the efﬁciency with which managers use corporate
assets. Dating back at least to Mørck, Shleifer and Vishny (1988), high book-to-market
ratios have been interpreted as indicating poor performance and possibly the existence
of agency problems between stockholders and managers.
The fact that the same empirical proxy has been used in three quite different ways
raises serious questions about interpreting any of this evidence in a normative way to
give ﬁrms or managers advice about corporate ﬁnancial policy.
6.3. Slow reaction to corporate ﬁnancial policy
Much of the literature studying long-horizon returns focuses on corporate ﬁnancial
policy decisions such as IPOs, seasoned equity offerings, share repurchases, merger
bids, and so forth. A common theme in this literature is that there is a slow drift in
the stock price of the ﬁrm after the event, apparently reﬂecting a gradual process of
learning the good or bad news associated with the event. A slow reaction is inconsistent
with the efﬁcient markets hypothesis.
As mentioned above, the papers that have systematically studied the behavior of
long-horizon performance measures found that they have low power and unreliable
statistical properties in most situations. Even if one were to accept the premise that

968

G.W. Schwert

the market learns very slowly about the implications of changes in corporate ﬁnancial
policy, the uncertainty associated with the future price performance for an individual
ﬁrm over a period of one to ﬁve years is so great that it would be senseless to advise
that ﬁrms choose their ﬁnancial policies so as to take advantage of market mispricing
that is only corrected after ﬁve years.
7. Conclusions
This chapter highlights some interesting ﬁndings that have emerged from empirical
research on the behavior of asset prices and discusses the implications of these
ﬁndings for the way academics and practitioners use ﬁnancial theory. In the process,
I have replicated and extended some puzzling ﬁndings that have been called anomalies
because they do not conform with the predictions of accepted models of asset pricing.
One of the interesting ﬁndings from the empirical work in this chapter is that many
of the well-known anomalies in the ﬁnance literature do not hold up in different sample
periods. In particular, the size effect and the value effect seem to have disappeared after
the papers that highlighted them were published. At about the same time, practitioners
began investment vehicles that implemented the strategies implied by the academic
papers.
The weekend effect and the dividend yield effect also seem to have lost their
predictive power after the papers that made them famous were published. In these
cases, however, I am not aware of any practitioners who have tried to use these
anomalies as a major basis of their investment strategy.
The small-ﬁrm turn-of-the-year effect became weaker in the years after it was ﬁrst
documented in the academic literature, although there is some evidence that it still
exists. Interestingly, however, it does not seem to exist in the portfolio returns of
practitioners who focus on small-capitalization ﬁrms.
Likewise, the evidence that stock market returns are predictable using variables such
as dividend yields or inﬂation is much weaker in the periods after the papers that
documented these ﬁndings were published.
All of these ﬁndings raise the possibility that anomalies are more apparent than
real. The notoriety associated with the ﬁndings of unusual evidence tempts authors
to further investigate puzzling anomalies and later to try to explain them. But even
if the anomalies existed in the sample period in which they were ﬁrst identiﬁed, the
activities of practitioners who implement strategies to take advantage of anomalous
behavior can cause the anomalies to disappear (as research ﬁndings cause the market
to become more efﬁcient).
References
Abreu, D., and M.K. Brunnermeier (2002), “Synchronization risk and delayed arbitrage”, Journal of
Financial Economics 66:341−360.

Ch. 15:

Anomalies and Market Efﬁciency

969

Amihud, Y., and H. Mendelson (1986), “Asset pricing and the bid-ask spread”, Journal of Financial
Economics 17:223−249.
Asquith, P. (1983), “Merger bids, uncertainty, and stockholder returns”, Journal of Financial Economics
11:51−83.
Baker, M., and J. Wurgler (2000), “The equity share in new issues and aggregate stock returns”, Journal
of Finance 55:2219−2257.
Ball, R. (1978), “Anomalies in relationships between securities’ yields and yield-surrogates”, Journal of
Financial Economics 6:103−126.
Ball, R., S.P. Kothari and J. Shanken (1995), “Problems in measuring portfolio performance: an application
to contrarian investment strategies”, Journal of Financial Economics 38:79−107.
Banz, R. (1981), “The relationship between return and market value of common stock”, Journal of
Financial Economics 9:3−18.
Barber, B.M., and J.D. Lyon (1997), “Detecting long-run abnormal stock returns: empirical power and
speciﬁcation of test statistics”, Journal of Financial Economics 43:341−372.
Barber, B.M., and T. Odean (2000), “Trading is hazardous to your wealth: the common stock investment
performance of individual investors”, Journal of Finance 55:773−806.
Barber, B.M., and T. Odean (2001), “Boys will be boys: gender, overconﬁdence, and common stock
investment”, Quarterly Journal of Economics 116:261−292.
Barberis, N., and A. Shleifer (2003), “Style investing”, Journal of Financial Economics 68:161−199.
Barberis, N., A. Shleifer and R. Vishny (1998), “A Model of investor sentiment”, Journal of Financial
Economics 49:307−343.
Basu, S. (1977), “Investment performance of common stocks in relation to their price-earning ratios: a
test of the efﬁcient market hypothesis”, Journal of Finance 32:663−682.
Basu, S. (1983), “The relationship between earnings’ yield, market value and return for NYSE common
stocks: further evidence”, Journal of Financial Economics 12:129−156.
Black, F. (1971), “Random walk and portfolio management”, Financial Analyst Journal 27:16−22.
Booth, D.G., and D.B. Keim (2000), “Is there still a January effect?” in: D.B. Keim and W.T. Ziemba,
eds., Security Market Imperfections in Worldwide Equity Markets (Cambridge University Press,
Cambridge) pp. 169–178.
Brav, A., and P.A. Gompers (1997), “Myth or reality? The long-run underperformance of initial public
offerings: evidence from venture and nonventure capital-backed companies”, Journal of Finance
52:1791−1821.
Brav, A., C. Geczy and P.A. Gompers (2000), “Is the abnormal return following equity issuances
anomalous?”, Journal of Financial Economics 56:209−249.
Brealey, R.A., and S.C. Myers (2000), Principles of Corporate Finance, 6th Edition (McGraw-Hill, New
York).
Brennan, M.J., and A. Subrahmanyam (1996), “Market microstructure and asset pricing: on the
compensation for illiquidity in stock returns”, Journal of Financial Economics 41:441−464.
Brennan, M.J., T. Chordia and A. Subrahmanyam (1998), “Alternative factor speciﬁcations, security
characteristics, and the cross-section of expected stock returns”, Journal of Financial Economics
49:345−373.
Brown, S.J., W. Goetzmann, R.G. Ibbotson and S.A. Ross (1992), “Survivorship bias in performance
studies”, Review of Financial Studies 5:679−698.
Campbell, J.Y. (1987), “Stock returns and the term structure”, Journal of Financial Economics 18:
373−400.
Campbell, J.Y., and R.J. Shiller (1998), “Valuation ratios and the long-run stock market outlook”, Journal
of Portfolio Management 24:11−26.
Carhart, M.M. (1997), “On the persistence in mutual fund performance”, Journal of Finance 52:57−82.
Chen, J., H. Hong and J.C. Stein (2002), “Breadth of ownership and stock returns”, Journal of Financial
Economics 66:171−205.

970

G.W. Schwert

Cohen, R.B., P.A. Gompers and T. Vuolteenaho (2002), “Who underreacts to cash-ﬂow news? Evidence
from trading between individuals and institutions”, Journal of Financial Economics 66:409−462.
Cowles, A. (1933), “Can stock market forecasters forecast?” Econometrica 1:309−324.
Cowles, A. (1939), Common Stock Indexes, 2nd Edition, Cowles Commission Monograph 3 (Principia
Press, Inc., Bloomington, IN).
Daniel, K., and S. Titman (1997), “Evidence on the characteristics of cross-sectional variation in stock
returns”, Journal of Finance 52:1−33.
Daniel, K., D. Hirshleifer and A. Subrahmanyam (1998), “Investor psychology and security market
under- and overreactions”, Journal of Finance 53:1839−1885.
Daniel, K., D. Hirshleifer and A. Subrahmanyam (2001), “Overconﬁdence, arbitrage, and equilibrium
asset pricing”, Journal of Finance 56:921−965.
Davis, J.L., E.F. Fama and K.R. French (2000), “Characteristics, covariances and average returns”, Journal
of Finance 55:389−406.
D’Avolio, G. (2002), “The market for borrowing stock”, Journal of Financial Economics 66:271−306.
DeBondt, W.F.M., and R. Thaler (1985), “Does the stock market overreact?” Journal of Finance 40:
793−805.
Dufﬁe, D., N. Garleanu and L.H. Pedersen (2002), “Securities lending, shorting, and pricing”, Journal
of Financial Economics 66:307−339.
Eckbo, B.E., R.W. Masulis and Ø. Norli (2000), “Seasoned public offerings: resolution of the ‘new
issues puzzle’ ”, Journal of Financial Economics 56:251−291.
Fama, E.F. (1970), “Efﬁcient capital markets: a review of theory and empirical work”, Journal of Finance
25:383−417.
Fama, E.F. (1975), “Short-term interest rates as predictors of inﬂation”, American Economic Review
65:269−282.
Fama, E.F. (1976), Foundations of Finance (Basic Books, New York).
Fama, E.F. (1991), “Efﬁcient capital markets II”, Journal of Finance 46:1575−1617.
Fama, E.F. (1998), “Market efﬁciency, long-term returns, and behavioral ﬁnance”, Journal of Financial
Economics 49:283−306.
Fama, E.F., and K.R. French (1988), “Dividend yields and expected stock returns”, Journal of Financial
Economics 22:3−25.
Fama, E.F., and K.R. French (1992), “The Cross-section of expected returns”, Journal of Finance
47:427−465.
Fama, E.F., and K.R. French (1993), “Common risk factors in the returns on stocks and bonds”, Journal
of Financial Economics 33:3−56.
Fama, E.F., and K.R. French (1996), “Multifactor explanations of asset pricing anomalies”, Journal of
Finance 51:55−84.
Fama, E.F., and K.R. French (1998), “Value versus growth: the international evidence”, Journal of
Finance 53:1975−1999.
Fama, E.F., and G.W. Schwert (1977), “Asset returns and inﬂation”, Journal of Financial Economics
5:115−146.
French, K.R. (1980), “Stock returns and the weekend effect”, Journal of Financial Economics 8:55−69.
French, K.R., G.W. Schwert and R.F. Stambaugh (1987), “Expected stock returns and volatility”, Journal
of Financial Economics 19:3−29.
Fung, W., and D.A. Hsieh (1997), “Empirical characteristics of dynamic trading strategies: the case of
hedge funds”, Review of Financial Studies 10:275−302.
Geczy, C.C., D.K. Musto and A.V. Reed (2002), “Stocks are special too: an analysis of the equity lending
market”, Journal of Financial Economics 66:241−269.
Goyal, A., and I. Welch (1999), “Predicting the equity premium with dividend ratios”, manuscript (Yale
University).
Gromb, D., and D. Vayanos (2002), “Equilibrium and welfare in markets with ﬁnancially constrained
arbitrageurs”, Journal of Financial Economics 66:361−407.

Ch. 15:

Anomalies and Market Efﬁciency

971

Hendricks, D., J. Patel and R. Zeckhauser (1993), “Hot hands in mutual funds: short-run persistence of
relative performance”, Journal of Finance 48:93−130.
Ibbotson, R. (1975), “Price performance of common stock new issues”, Journal of Financial Economics
2:235−272.
Ibbotson, R., J. Ritter and J. Sindelar (1994), “The market’s problem with the pricing of initial public
offerings”, Journal of Applied Corporate Finance 7:66−74.
Ibbotson Associates (1998), Stocks, Bonds, Bills, and Inﬂation: 1998 Yearbook (Ibbotson Associates,
Chicago).
Jaffe, J. (1974), “Special information and insider trading”, Journal of Business 47:411–428.
Jegadeesh, N., and S. Titman (1993), “Returns to buying winners and selling losers: implications for
stock market efﬁciency”, Journal of Finance 48:65−91.
Jegadeesh, N., and S. Titman (2001), “Proﬁtability of momentum strategies: an evaluation of alternative
explanations”, Journal of Finance 56:699−720.
Jensen, M.C. (1968), “The performance of mutual funds in the period 1945–64”, Journal of Finance
23:389−416.
Jensen, M.C. (1978), “Some anomalous evidence regarding market efﬁciency”, Journal of Financial
Economics 6:95−102.
Jones, C.M., and O.A. Lamont (2002), “Short sale constraints and stock returns”, Journal of Financial
Economics 66:207−239.
Keim, D.B. (1983), “Size-related anomalies and stock return seasonality: further empirical evidence”,
Journal of Financial Economics 12:13−32.
Keim, D.B., and R.F. Stambaugh (1984), “A further investigation of the weekend effect in stock returns”,
Journal of Finance 39:819−835.
Keim, D.B., and R.F. Stambaugh (1986), “Predicting returns in the stock and bond markets”, Journal of
Financial Economics 17:357−390.
Keim, D.B., and W.T. Ziemba (2000), “Security market imperfections: an overview”, in: D.B. Keim
and W.T. Ziemba, eds., Security Market Imperfections in Worldwide Equity Markets (Cambridge
University Press, Cambridge) pp. xv–xxvii.
Kleidon, A.W. (1986), “Variance bounds tests and stock price valuation models”, Journal of Political
Economy 94:953−1001.
Kothari, S.P., and J. Shanken (1997), “Book-to-market, dividend yield, and expected market returns: a
time series analysis”, Journal of Financial Economics 44:169−203.
Kothari, S.P., and J.B. Warner (1997), “Measuring long-horizon security price performance”, Journal of
Financial Economics 43:301−339.
Krishnamurthy, A. (2002), “The bond/old-bond spread”, Journal of Financial Economics 66:463−506.
Lakonishok, J., A. Shleifer and R.W. Vishny (1994), “Contrarian investment, extrapolation, and risk”,
Journal of Finance 49:1541−1578.
Lee, C.M.C., A. Shleifer and R.H. Thaler (1991), “Investor sentiment and the closed-end fund puzzle”,
Journal of Finance 46:75−110.
Lewellen, J. (2002), “Momentum and autocorrelation in stock returns”, Review of Financial Studies
15:533−563.
Lintner, J. (1965), “The valuation of risk assets and the selection of risky investment in stock portfolios
and capital budgets”, Review of Economics and Statistics 47:13−37.
Lo, A.W., and A.C. MacKinlay (1990), “Data-snooping biases in tests of ﬁnancial asset pricing models”,
Review of Financial Studies 3:431−467.
Loughran, T., and J.R. Ritter (1995), “The new issues puzzle”, Journal of Finance 50:23−51.
Loughran, T., and A.M. Vijh (1997), “Do long-term shareholders beneﬁt from corporate acquisitions?”
Journal of Finance 52:1765−1790.
Lowry, M., and G.W. Schwert (2002), “IPO market cycles: bubbles or sequential learning?” Journal of
Finance 57:1171−1200.

972

G.W. Schwert

MacKinlay, A.C. (1995), “Multifactor models do not explain deviations from the CAPM”, Journal of
Financial Economics 38:3−28.
Malkiel, B.G. (1995), “Returns from investing in equity mutual funds, 1971 to 1991”, Journal of Finance
50:549−572.
Mandelker, G. (1974), “Risk and return: the case of merging ﬁrms”, Journal of Financial Economics
1:303−335.
Marsh, T.A., and R.C. Merton (1986), “Dividend variability and variance bounds tests for the rationality
of stock market prices”, American Economic Review 76:483−498.
Mitchell, M.L., and E. Stafford (2000), “Managerial decisions and long-term stock price performance”,
Journal of Business 73:287−320.
Mørck, R., A. Shleifer and R.W. Vishny (1988), “Management ownership and market valuation: an
empirical analysis”, Journal of Financial Economics 20:293−315.
Nelson, C.R., and G.W. Schwert (1977), “On testing the hypothesis that the real rate of interest is
constant”, American Economic Review 67:478−486.
Odean, T. (1999), “Do investors trade too much?” American Economic Review 89:1279−1298.
Pontiff, J. (1995), “Closed-end fund premia and returns: implications for ﬁnancial market equilibrium”,
Journal of Financial Economics 37:341−370.
Pontiff, J. (1996), “Costly arbitrage: evidence from closed-end funds”, Quarterly Journal of Economics
111:1135−1151.
Reinganum, M.R. (1981), “Misspeciﬁcation of capital asset pricing: empirical anomalies based on
earnings’ yields and market values”, Journal of Financial Economics 9:19−46.
Reinganum, M.R. (1983), “The anomalous stock market behavior of small ﬁrms in january: empirical
tests for tax-loss selling effects”, Journal of Financial Economics 12:89−104.
Ritter, J.R. (1991), “The long-run performance of initial public offerings”, Journal of Finance 46:3−27.
Roll, R. (1983), “Vas ist das? The turn-of-the-year effect and the return premia of small ﬁrms”, Journal
of Portfolio Management 9:18−28.
Schultz, P. (2003), “Pseudo market timing and the long-run underperformance of IPOs”, Journal of
Finance 58:483−517.
Schwert, G.W. (1983), “Size and stock returns, and other empirical regularities”, Journal of Financial
Economics 12:3−12.
Schwert, G.W. (1989), “Why does stock market volatility change over time?” Journal of Finance
44:1115−1153.
Schwert, G.W. (1990), “Indexes of United States stock prices from 1802 to 1987”, Journal of Business
63:399−426.
Schwert, G.W. (1991), “Review of market volatility by R. Shiller: Much ado about . . . very little”,
Journal of Portfolio Management 17:74−78.
Schwert, G.W. (1996), “Markup pricing in mergers & acquisitions”, Journal of Financial Economics
41:153−192.
Sharpe, W.F. (1964), “Capital asset prices: a theory of market equilibrium under conditions of risk”,
Journal of Finance 19:425−442.
Shiller, R.J. (1981a), “Do stock prices move too much to be justiﬁed by subsequent changes in dividends?”
American Economic Review 75:421−436.
Shiller, R.J. (1981b), “The use of volatility measures in assessing market efﬁciency”, Journal of Finance
36:291−304.
Shiller, R.J. (1989), Market Volatility (MIT Press, Cambridge, MA).
Shleifer, A., and R.W. Vishny (1997), “The limits of arbitrage”, Journal of Finance 52:35−55.
Smith, C.W., and R.L. Watts (1992), “The investment opportunity set and corporate ﬁnancing, dividend,
and compensation policies”, Journal of Financial Economics 32:263−292.
Thompson, R. (1978), “The information content of discounts and premiums on closed-end fund shares”,
Journal of Financial Economics 6:151−186.

