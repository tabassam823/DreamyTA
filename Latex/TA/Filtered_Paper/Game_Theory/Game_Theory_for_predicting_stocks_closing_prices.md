Article

Game Theory for predicting stocks’ closing prices
João Costa Freitas 1,∗ , Alberto Adrego Pinto 1,2,∗ and Óscar Felgueiras 1,3,∗
1
2
3

*

Citation: Freitas, J.C.; Pinto, A.A.;
Felgueiras, O. Game Theory for
predicting stocks’ closing prices.
Journal Not Specified 2022, 1, 0.
https://doi.org/
Received:
Accepted:
Published:
Publisher’s Note: MDPI stays neutral
with regard to jurisdictional claims in
published maps and institutional affiliations.
Copyright: © 2024 by the authors.
Submitted to Journal Not Specified
for possible open access publication
under the terms and conditions
of the Creative Commons Attribution (CC BY) license (https://
creativecommons.org/licenses/by/

Faculty of Sciences, University of Porto, R Campo Alegre, 4169-007 Porto, Portugal
LIAAD-INESC TEC, University of Porto, R Campo Alegre, 4169-007 Porto, Portugal
CMUP, University of Porto, R Campo Alegre, 4169-007 Porto, Portugal
Correspondence: joao.costafreitas@outlook.pt (J.F.); aapinto1@gmail.com (A.P.); olfelgue@fc.up.pt (O.F.)

Abstract: We model the financial markets as a game and make predictions using Markov chains
estimators. We extract the possible patterns displayed by the financial markets, define a game where
one of the players is the speculator, whose strategies depend on his/hers risk-to-reward preferences,
and the market is the other player, whose strategies are the previously observed patterns. Then we
estimate the market’s mixed probabilities by defining Markov chains and utilizing its transitions
matrices. Afterwards, we use these probabilities to determine which is the optimal strategy for the
speculator. Finally, we apply these models to real-time market data to determine its feasibility. After
all, we obtained a model for the financial markets that has a good performance in terms of accuracy
and profitability.

1

Keywords: Financial Markets; Games Against Nature; Markov Chains

10

1. Introduction

11

Due to the rise of automated systems that perform prediction tasks and posterior
execution, we thought it would be beneficial to create a theoretical framework for an automated system that outputs probabilities of different market states where traders can define
clear trading rules based on these probabilities and their risk tolerance, which can help
execute trades swiftly based on the model’s output. The presented methods can be utilized
as indicators to the purchase of certain financial assets, but would be optimal if they were
utilized as an automated system to purchase barrier options.
Thus, in this article, we will present and apply methods specifically designed to model
the financial market, but, before starting to discuss the models, we need to make a brief
introduction to the data that we will be working with.
Our data consists on financial asset prices from several stock exchanges, with special attention to the New York Stock Exchange, the London Stock Exchange and the Lisbon Stock
Exchange. Also, we focused on stock and forex (foreign exchange market) prices, because
these present higher volatility and volume (i.e., more trades), and the data related to these
assets is easier to obtain. Here, volatility is a statistical measure of the dispersion of returns
for a given financial asset. It is often measured as either the standard deviation or variance
between returns from that same asset.
Moving further we will often use the terms "stock exchange" and "financial market" interchangeably, but they slightly differ. The term "financial market" broadly refers to any
marketplace where the trading of securities occurs, including the stock market, bond market, forex market, and derivatives market, among others, whilst the "stock exchange" is a
facility where stockbrokers and traders can buy and sell securities, such as shares of stock,
bonds and other financial instruments. However, whenever we refer to the financial market
we will be referring to the stock exchange.
The data was retrieved from Yahoo Finance [1] and AlphaVantage [2], but it can be found at
the dataset related to the article [3].
We will study daily closing prices, that is, the price of the asset at the end of the day, and

12

4.0/).

Version August 20, 2024 submitted to Journal Not Specified

https://www.mdpi.com/journal/notspecified

2
3
4
5
6
7
8
9

13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38

Version August 20, 2024 submitted to Journal Not Specified

2 of 50

also intraday closing prices, i.e., the prices of the asset at the end of each minute. Also, we
will look into several assets within multiple stock exchanges. Specifically, we will analyze:

39

•
•

3 theoretical datasets with 1000 observations;
100 datasets with 1000 observations of stocks’ daily closing prices from several stock
exchanges;
100 datasets with 1000 observations of stocks’ intraday closing prices from several
stock exchanges.

41

Hence, we will obtain all kinds of data, with different characteristics and statistical properties. Moreover, since we cannot access the assets’ future prices, we will split the datasets
between training and test sets. All the analyzed datasets have 1000 observations and 20%
of these will be part of the test sets. This is done so that we can apply our models to the
training set and "compare" their predictions with the test set’s values.
To exemplify, consider the following datasets from the New York Stock Exchange (plots 1
and 2) and from the Lisbon Stock Exchange (plots 3 and 4):

46

•

200
100

150

Closing Price

250

300

AAPL Daily

2016−01−22

2017−05−17

2018−09−12

2020−01−10

Date

Figure 1. AAPL Daily Closing Price from 22/01/2016 to 10/01/2020

40

42
43
44
45

47
48
49
50
51
52

Version August 20, 2024 submitted to Journal Not Specified

3 of 50

315
305

310

Closing Price

320

325

AAPL Intraday

2020−02−03 09:31:00

2020−02−04 13:51:00

2020−02−06 11:40:00

2020−02−07 16:00:00

Date

Figure 2. AAPL Intraday Closing Price from 03/02/2020 09:31 to 07/02/2020 16:00

14
12

Closing Price

16

18

GALP Daily

2016−03−17

2017−07−04

2018−10−22

2020−02−13

Date

Figure 3. GALP Daily Closing Price from 17/03/2016 to 13/02/2020

Version August 20, 2024 submitted to Journal Not Specified

4 of 50

13.9
13.6

13.7

13.8

Closing Price

14.0

14.1

GALP Intraday

2020−02−11 04:00:00

2020−02−12 08:33:00

2020−02−14 04:38:00

2020−02−17 11:29:00

Date

Figure 4. GALP Intraday Closing Price from 11/02/2020 04:00 to 17/02/2020 11:29

Measuring past price changes to determine their dispersion should yield a probabilistic result. Additionally, price changes, in stock prices (or in any other financial instruments),
usually pattern themselves in a normal distribution (for further details see [4], [5], [6]
and/or [7]), which is the familiar bell-shaped curve (for further details see, for example,
[8]). There are numerous different ways to determine the probability function for a financial
instrument. Also, price changes can be measured and quantified empirically, either by the
percent change in the instrument’s value over specified time intervals or by the change in
the logarithm of the price over the time intervals.
Oftentimes when you’re thinking in terms of compounding percent changes, the mathematically cleaner concept is to think in terms of log differences. When you’re repeatedly
multiplying terms together, usually, it’s more convenient to work in logs and add terms
together. So, let’s say our wealth at time T is given by:
T

T

t =1

t =1

WT = ∏ (1 + Rt ) ⇐⇒ log WT = ∑ rt ,
where Rt is the (overall) return at time t and rt = log(1 + Rt ) = logWt − logWt−1 .
An idea from calculus is that you can approximate a smooth function with a line (for further
details see, for example, [9]). The linear approximation is simply the first two terms of a
Taylor Series. The first order Taylor Expansion of log( x ) around x = 1 is given by:
log( x ) ≈ log(1) +

d
log( x )| x=1 ( x − 1).
dx

The right hand side simplifies to 0 + 11 ( x − 1) hence:
log( x ) ≈ x − 1.
So for x in the neighborhood of 1, we can approximate log( x ) with the line y = x − 1.
Now consider two variables x1 and x2 such that xx2 ≈ 1. Then the log difference is
1

approximately the percent change xx2 − 1 = x2x− x1 :
1

1



x2
log x2 − log x1 = log
x1



≈

x2
− 1.
x1

Version August 20, 2024 submitted to Journal Not Specified

5 of 50

Note that for big percent changes, the log difference is not the same thing as the percent
change because approximating the curve y = log( x ) with the line y = x − 1 gets worse and
worse the further away you get from x = 1.
Thus we have the following:

53

•

The logarithmic method is well documented. The Black-Scholes formula for option
pricing assumes a lognormal dispersion of prices, and there is a theoretical lognormal
distribution than can be inferred from the Black-Scholes formula. However, the
discussion of the lognormal derivation of price changes is not necessary for this paper
(but, for further details, see [10] and/or [11]).
Measuring percentage price changes yields a nearly equivalent result to the lognormal
method, specially for price changes less than ≈ 15% (for further details see [7]). Also,
this method affords a fair approximation of the real world, while being fairly simple
to calculate.

57

However, if we simply analyzed the price change (between consecutive intervals) of a large
sample from some financial instrument, the analysis would be skewed by the change in the
price level, hence the need for measuring percentage changes in prices. Thus, any statistical
method used to analyze price changes has to be able to account for the increase in the price
level of the instrument. This can be taken care by looking at the prices’ percentage changes,
rather than the actual price changes. Also, there is the added property that percent price
changes should (theoretically) follow a normal distribution.
We have to note that he literature commonly uses the logarithmic returns for its statistical
properties, but we intend to use this model in a business setting, so the simple returns are
more intuitive and still hold the necessary statistical properties for our model (for further
details see [12] and/or [13]).
Nonetheless, most real world measurements vary from the standard normal distribution.
The theoretical lognormal distribution for stock prices has a slight skew to the positive
side, because there is an inherent upward bias in stock prices (for further details see [14]).
This is because, since the turn of the century, stocks have appreciated at approximately a
5% − 10% annual rate, this is partly due to inflation (or even to investor overconfidence),
but it is also due to increases in productivity, or the economic surplus society generates (for
further details see [15] and/or [16]). Thus, the skewing in the positive side of the theoretic
lognormal is understandable. Also note that, factors that have a bearing on assets’ prices,
such as wars, depression, peace, prosperity, oil shortages, foreign competition, market
crashes, pandemics, and so forth, are all contained in its data. So, henceforth, we will
consider that all the used data is transformed using the percentage change transformation,
X −X
i.e., we will apply the Percentage Returns’ transformation Ut = tX t−1 , so each entry on
t −1
the obtained datasets represents the percentage return from the previous iteration to the
present one. Thus, we will apply all of our models to this transformed data. For example,
the transformation applied to the previous datasets yields:

66

•

54
55
56

58
59
60
61
62
63
64
65

67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91

Version August 20, 2024 submitted to Journal Not Specified

6 of 50

0
−10

−5

Closing Price

5

Transformed AAPL Daily

2016−01−25

2017−05−18

2018−09−13

2020−01−10

Date

Figure 5. Transformed AAPL Daily Closing Price from 25/01/2016 to 10/01/2020

0.5
−1.0

−0.5

0.0

Closing Price

1.0

1.5

2.0

Transformed AAPL Intraday

2020−02−03 09:32:00

2020−02−04 13:51:00

2020−02−06 11:40:00

2020−02−07 16:00:00

Date

Figure 6. Transformed AAPL Intraday Closing Price from 03/02/2020 09:32 to 07/02/2020 16:00

Version August 20, 2024 submitted to Journal Not Specified

7 of 50

0
−4

−2

Closing Price

2

4

Transformed GALP Daily

2016−03−18

2017−07−05

2018−10−23

2020−02−13

Date

Figure 7. Transformed GALP Daily Closing Price from 18/03/2016 to 13/02/2020

−0.5

0.0

Closing Price

0.5

1.0

Transformed GALP Intraday

2020−02−11 04:01:00

2020−02−12 08:34:00

2020−02−14 04:39:00

2020−02−17 11:29:00

Date

Figure 8. Transformed GALP Intraday Closing Price from 11/02/2020 04:01 to 17/02/2020 11:29

Note that we can apply this transformation because all of our values represent asset
prices in a stock exchange, thus they are always strictly positive. Also, due to this transformation, we will "lose" one observation, but gain several important properties, which were
previously described.
and/or

92

2. Models

97

In this chapter we will make use of game theory (presented in [17], [18], [19], [20],
[21], [22], [23], [24], [25], [26], [27], [28], [29], [30] and [31]) to develop the game theoretical
model and Markov chains (presented in [32], [33], [34], [35], [36], [37], [38], [39], [40], [41],
[42] and [43]) to estimate the game’s probabilities in order to design suitable models for
financial data (specifically, for the data that was described in the previous chapter), then
we will describe how we applied our models using the R software.

98

93
94
95
96

99
100
101
102
103

Version August 20, 2024 submitted to Journal Not Specified

8 of 50

We sill also compare our results against classical time series theory (presented in [12], [44],
[45], [46], [47], [13], [48], [49], [50] and [51]), thus we need to explain how we will apply
these models and compare its outcomes.

104
105
106
107

2.1. The Game Theoretical Model

108

Since the focus of this article is to apply game theory to the financial markets, we will
start by presenting the game proposed in [31] and the subsequent decision model that
we developed from it. But, before constructing a game model for the market, we need to
understand how the market works, how can we model it and what our goals are. Thus, we
will start by identifying what kind of player in the market we will be, because there are
two kinds of participants in the financial markets:

109

Investors: these participants are interested in making a predictable rate of return from
their investments, through interest payments dividends and so on.
Speculators: these are interested in trying to profit from changes in the price of an asset.

115

Thus, since our goal is to predict prices and then act according to our predictions, henceforth we will take the part of a speculator. Also, to be a participant in the market, we must
accept some level of risk (high or low risk acceptance level) and we also must have a clear
profit objective in mind. Formally, the speculator needs to set a quantity for "Less Risk",
"high risk" and "profit objective", always assuming that the asset will be held until the price
reaches one of these targets. So, these targets must represent an individual’s actual risk
and reward appetites, because if they are set randomly, then it is possible that neither are
reached or that they are reached sooner than expected. Thus, these must have some basis
on reality and the asset should stand a chance of hitting one of them.
Once the decision has been made to take a position in the market (by buying or selling a
particular asset), the interaction between the asset’s price fluctuation and the speculator’s
risk acceptance level and profit objective will determine whether or not a profit will be
made.

118

•
•

110
111
112
113
114

116
117

119
120
121
122
123
124
125
126
127
128
129
130
131

Remark 1. Note that, this is consistent with game theory, where the outcome is determined
by the choices made by both players, not just one.

132
133
134

Thus, speculators take positions in markets and market prices fluctuate. As such, the
speculators’ strategies involve determining how much risk to accept, then the market will
fluctuate the prices. It is the interaction between the speculator’s and the market’s actions
that determine if a trade is profitable or not. Hence, after setting the profit objective and
risk acceptance levels, we have the following scenarios:

135

Zero Adversity: when there is no price fluctuation against the speculator’s position
severe enough to cause the trade to hit either risk acceptance levels. In this case, it
doesn’t matter how much risk is accepted, because the market movement is completely
favorable. We will term this pattern of price movement as Zero Adversity.
Minor (or Moderate) Adversity: when the market moves somewhat against the speculator’s position, which will cause the speculator to lose money if Less Risk were
accepted but would have resulted in a profit if More Risk were accepted. So, any
pattern of price movement that will cause a loss if Less Risk is accepted, yet still yield
a profit if More Risk is accepted falls into this category, which we will term as Minor
Adversity.
Major Adversity: when the market moves completely against both risk acceptance
positions, so the Less Risk acceptance position results in a small loss, and the large
risk acceptance position results in a large loss. Also, the profit objective was never
reached. We will term this pattern of price movement as Major Adversity.

140

•

•

•

136
137
138
139

141
142
143
144
145
146
147
148
149
150
151
152
153

Version August 20, 2024 submitted to Journal Not Specified

9 of 50

Note that, many different price movement patterns yield the same result and that
it is possible to classify all market price movements into these three categories. These
classifications are:

154

•

the speculator accepts Less Risk and then the prices move favorably, resulting in a
profit to the speculator;
the speculator accepts More Risk and then the prices move favorably, resulting in a
profit to the speculator;
the speculator accepts Less Risk and the prices move moderately against the position,
resulting in a small loss to the speculator;
the speculator accepts More Risk and the prices move moderately against the position,
resulting in a profit to the speculator;
the speculator accepts Less Risk and the prices move severely against the position,
resulting in a small loss to the speculator;
the speculator accepts More Risk and the prices move severely against the position,
resulting in a large loss to the speculator.

157

Thus, if we quantify our risk acceptance levels and profit objective, the pattern of
price fluctuation that subsequently occurs will result in one of the six outcomes previously
described. Also, there is no price line that can be drawn that will not yield one of the above
six results:

169

•
•
•
•
•

155
156

158
159
160
161
162
163
164
165
166
167
168

170
171
172

Figure 9. Visual representation of possible outcomes considering the speculator’s risk levels and the
market’s price movements.

However, even though there are six categories, there are only three possible outcomes
that can result from any trade, because the speculator must decide between accepting More
Risk or Less Risk on any particular trade, and there are three outcomes associated with
either of these actions. In other words, the speculator must decide on how much risk to take,
either take More Risk or take Less Risk, then the market decides on how to fluctuate the
prices, either fluctuate them so as to cause the speculator zero adversity, minor adversity or
major adversity. So, after the speculator’s decision, one of three possible states of nature
will prevail.
The previous discussion also holds true for short sales. A short sale is where the individual
sells a particular asset first, then buys it back at a later date. Typically, the shorted asset
is "borrowed" from the brokerage firm, and the broker will require a high margin against
the short. Intuitively, a short sale is the inverse of a long position (i.e., a buy-sell position
that we have been discussing so far), so short sellers make a profit when the value of an
asset declines and loses money when the prices rise. Thus, the risk acceptance levels are
set at prices higher than the price that initiated the trade. However, there is no significant
difference in the concepts of risk acceptance levels and profit objectives between being

173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188

Version August 20, 2024 submitted to Journal Not Specified

10 of 50

either long or short in the market. But, because of the added costs of being a short seller,
profit objectives generally have to be higher in order to recoup margin costs. Thus, henceforth, we will only concentrate on long positions, and its risk acceptance levels and profit
objectives.

189
190
191
192
193

2.1.1. The Financial Game

194

To create the game that mimics the financial markets, we need to meet game theory’s
requirement to have at least two players and that their identities are known, in our case the
players are the speculator and the market. However, the market is an abstract entity, thus
we enter the subclass of games (developed in [19], [20], [27] and [30]), called games against
nature, where one of the players is an abstract entity.
In spite of this being a standard game against nature, we must make some important
observations and assumptions:

195

•

The market does not come up with prices in a vacuum, rather the prices are the net
result of the buying and selling decisions of all the individual participants in the
market.
Generally, an individual has no influence on nature, yet in the financial markets a
participant may have an effect on the price movements due to his/hers own actions.
Of course that this depends on the individual and on the market. For instance, if the
market is small and thinly traded, a large order will tend to move the prices either up
or down, or if a person making the order is known (to other participants) to be astute,
then his/hers actions may also influence the prices. However, since the majority of the
individuals cannot affect "large" markets (such as in the USA, EU, UK markets), we
will assume that we are working on a large market and that the effect of any individual
is negligible.
Since the payoffs of each individual are unrelated, then we will assume that the
market plays the same game against all participants. This also guarantees that all the
individuals are playing against the market separately.
We will also assume that the goal of the speculator is to make a profit and that the goal
of the market is to try and make the speculator lose money.

202

Note that with the previous assumptions, we have a game against nature where we assume
the Wald’s (max-min) Criterion (for more details check [19], [20], [27] and/or [30]). That
is we apply Wald’s (max-min) Criterion to model the interaction between the speculator
and the market within a game against nature framework, where we assume the market
acts adversarially, aiming to minimize the speculator’s gains while the speculator aims to
maximize their profit under the worst-case scenario of market behavior. This approach
helps determine a strategy that guarantees the best possible outcome for the speculator,
even in the face of unpredictable market fluctuations.
Here the market "tries" to make the speculator lose money by attempting to fluctuate the
prices in such a manner so as to make it impossible to find a good combination of risk
acceptance levels and profit objectives. Also, because we are using a theory that will enable
an individual to find a way to beat the market, assuming that the market is also trying to
beat the individual is the most conservative approach. So, ascribing a motive to the market
allows us to analyze the market’s strategies as if it is a rational player in the game.
In order to have a game theoretic construction, we need to be able to draw a game matrix
outlining the strategies of each player as well as the payoffs. Also, this should be done
from the perspective of the individual speculator, because the point of this analysis is
to find a set of strategies that will enable an individual to beat the market. Thus, the
possible strategies for the speculator are accepting More Risk or relatively Less Risk. And
the market’s strategies are price movements relative to the speculator’s position, i.e., the
market can "choose" between three price movements: Zero Adversity, Minor Adversity or
Major Adversity.
With this, we have that there are two possible strategies that the speculator can play and

219

•

•

•

196
197
198
199
200
201

203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218

220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241

Version August 20, 2024 submitted to Journal Not Specified

11 of 50

three possible strategies the market can play, resulting in six possible outcomes from the
interaction between price movements and risk acceptance levels, all of which results in the
following game table:

242
243
244

Table 1. The game table for the financial market game.

Market

\
Zero Adversity (0 A )
Minor Adversity (m A )
Major Adversity (M A )

Speculator
More Risk (R+ )
Profit
Profit
Large Loss

Less Risk (R− )
Profit
Small Loss
Small Loss
245

Remark 2. Note that, in the game table, we added between parenarticle some notation so that we
can refer to those strategies in a simpler manner.

246
247
248

Looking at the game table suggests that we should play the strategy of Less Risk,
because this column has a minimum of a small loss, which is larger than the minimum in
the More Risk column, which is a large loss. Similarly the market will "look" at the payoff
table and "decide" to play a strategy that leaves us with the smallest minimum, i.e., the
market will choose to play the Major Adversity strategy, because this row’s maximum is
a small loss, which is the smallest maximum available. Hence the most likely outcome is
that the speculator will lose money, which makes this game rather unattractive. However,
in the real world a lot of people play the markets and some of them make money (at least
some of the time).
Note that the solution Major Adversity, Less Risk is based on the concept of pure strategies.
So this solution requires that the speculator always plays the strategy of Less Risk, and the
market always plays the strategy of Major Adversity. Thus, this renders the game entirely
pointless from the speculator’s point of view. But there are some caveats, the market is
simultaneously playing against a myriad of players and, as such, it does not know all of the
risk acceptance levels, the profit objectives and how many are short sellers or long traders.
So, the market has to make its decision on which strategy to play under conditions of both
risk and uncertainty.
Given the multitude of players and their strategies, the market will try to fluctuate prices
in such a manner so that as many people as possible lose money. Also, from the point of
view of any individual speculator, these fluctuations will make it look as if the market is
varying its strategy each different time the game is played. All of this (and considering the
theory so far) implies that playing each different strategy with some probability is called
playing mixed strategies (for further details see [18], [21], [22], [26], [29] and/or [28]).
The speculator may also play mixed strategies, if they vary their risk and reward amounts
each time they play the game. Also, they do not know how advantageous it is to play either
strategy with any regularity, due to the market’s continually changing mixed strategies.
But, in the financial markets, the players do not usually change their strategies, i.e., they
pick the risk acceptance levels and then wait the assets’ prices to hit the corresponding
thresholds. So, with this in mind, we will only consider pure strategies for the speculator
to play in the financial game.
Now we need to be able to calculate the payoffs to the speculator for any set of strategies
he/she plays against any set of mixed strategies that the market may play, in order to determine the merits of playing any one strategy at any particular point in time. Furthermore,
this has to be done in the general case, because to have a coherent theory, the solutions
must hold true for each and every individual speculator, no matter what strategy they play.
The market will play one of three strategies: fluctuate the prices in a way that causes major
adversity to the speculator, fluctuate the prices in a manner that causes minor adversity
to the speculator, or fluctuate the prices in a manner favorable to the speculator. Also, the
market will choose one of the strategies in an unknown manner to the speculator, so each

249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
287

Version August 20, 2024 submitted to Journal Not Specified

12 of 50

strategy will have a certain probability of being played. Thus we will use the following
notation:
•
•
•

p1 := the probability the market plays Minor Adversity;
p2 := the probability the market plays Major Adversity;
p0 := the probability the market plays Zero Adversity.

This notation is in terms of the probability that either event will occur and, because the
market is playing mixed strategies, the sum of the probabilities of playing all of the
strategies must equal 1. Therefore, if the market plays Minor Adversity with a probability
of p1 and Major Adversity with probability p2 , then it follows that Zero Adversity occurs
with a probability of p0 = 1 − p1 − p2 .
Regarding the speculator, theoretically, he/she may play two different strategies: More
Risk or Less Risk. Analogously to the market, the speculator may play the More Risk
strategy with some probability and the Less Risk strategy with some probability. Thus, the
speculator is playing mixed strategies, just as the market is. With this, we can define the
probabilities of playing the two strategies as follows:
•
•

q = the probability the speculator plays More Risk;
1 − q = the probability the speculator plays Less Risk.

288
289
290
291
292
293
294
295
296
297
298
299
300
301
302
303
304

Once again, the sum of the probabilities of playing both strategies must equal one.
Next we need to make a representation of the payoffs. Recall that there are three different
results for this game, a speculator may: make a profit, lose money equal to the Less Risk
amount, or lose money equal to the More Risk amount. We will denote this as follows:

305

w := profit to the speculator (this corresponds to a "win" to the speculator);
− x := loss equal to the "Less Risk" amount (this corresponds to a "small loss" to the
speculator);
−y := loss equal to the "More Risk" amount (this corresponds to a "large loss" to the
speculator).

309

•
•
•

Here, w, x, y ∈ R+ and w ≥ y > x.

So, with this notation we do not need to specify
monetary amounts associated with a profit, a small loss, or a large loss, because we have
the relative magnitude of these variables. Thus, putting together the above ideas into a
game table, we obtain the following:

306
307
308

310
311
312
313
314
315
316
317

Table 2. The "updated" game table for the financial market game.

Market

p0
p1
p2

Speculator
q
1−q
+
R
R−
0A
w
w
mA
w
−x
M A −y
−x

Note that the previous table 2 is the game’s decision matrix (also known as payoff
matrix), however it only presents the payoffs for the speculator since the market’s payoffs
can’t be quantifiable.
Now, to determine when it is advantageous to play one strategy or the other, we need to
start by isolating the pure strategies in terms of their expected profitability, and each of the
speculator’s strategies must be compared with each of the market’s strategies, also all the
results must be quantified.

318
319
320
321
322
323
324
325

Remark 3. Even though we presented the probabilities associated with the speculator’s strategies,
we will not consider them for our model.

326
327
328

Version August 20, 2024 submitted to Journal Not Specified

13 of 50

We know that there are three outcomes that can happen after the speculator takes a
position in the market: a profit (equal to the profit objective), a small loss (equal to the
Less Risk amount) or a large loss (equal to the More Risk amount). And, each of these
three outcomes happens with some unknown probability. Also, these events are mutually
exclusive, i.e., only one of them can happen at any one point in time (or trade). This is
because, if the speculator gets stopped out of the market, he/she made a profit or suffered a
loss (large or relatively small), and the highest probability that any event can occur is 100%.
Given this, it is possible (although unlikely) that one of the three outcomes happens with
100% probability, but since we want to develop our model in terms of the speculator getting
stopped out for either a large loss or a small loss, we will construct a diagram (specifically,
a probability triangle) which will reflect these two possibilities.

329
330
331
332
333
334
335
336
337
338
339
340

Remark 4. The diagram that we will be constructing goes along with the algebraic exposition, in order to make the model much easier to interpret.

341
342
343

2.1.2. The Probability Triangle

344

For the diagram, consider the market’s probability of playing Major Adversity on the
vertical axis, and the market’s probability of playing Minor Adversity on the horizontal axis.
Also, since the highest value either axis can have is 100% (because neither condition can
prevail more than 100% of the time), this implies that all combinations of Major Adversity
and Minor Adversity can never sum to more than 100%. This being the case, a diagonal
line must be drawn between the 100% mark on both axis, which will contain all possible
combinations of the market’s strategies of Major Adversity and Minor Adversity. Thus,
with all of this, we obtain the following probability triangle:

345
346
347
348
349
350
351
352

Probability
of Major
Adversity
1

Probability of Minor Adversity

0
1

Probability
of Minor
Adversity

Figure 10. The probability triangle showing the likelihood of loss.

We will divide this probability triangle into several regions, which will reflect when it
is more advantageous to accept More or Less Risk, or even when it is advantageous not to
play the game at all. Furthermore, since game theory gives us methods to determine when

353
354
355

Version August 20, 2024 submitted to Journal Not Specified

14 of 50

a player is guaranteed a certain payoff, we can solve for when it is optimal to accept either
More or Less Risk.
So far, we have concentrated on the speculator’s strategies which involve taking a position
in the market. However, in reality, if we know when to take a position (i.e., when to play
the game), we also know when not to take a position in the market (i.e., when not to play
the game). So we will develop this model in order to determine when it is advantageous to
take a position, along with when it is disadvantageous to do so. Thus, conditions where it
is disadvantageous to take a position will correspond to the "Do Not Play" region of the
probability triangle.
Now, we can determine, with the aid of the game table 2, the expected payoffs from playing
each of the speculator’s strategies:
•

356
357
358
359
360
361
362
363
364
365
366

The Expected Payoff from playing Less Risk (R− ):
ES ( R− ) = (1 − p1 − p2 )w + p1 (− x ) + p2 (− x ) = w − ( p1 + p2 )(w + x )

(1)
367

•

The Expected Payoff from playing More Risk (R+ ):
ES ( R+ ) = (1 − p1 − p2 )w + p1 w + p2 (−y) = w − p2 (w + y)

(2)

Equation (1) represents the expected payoff from playing the pure strategy Less Risk (R− )
and is written with several variables: the amount that can be won (w), the amount that can
be lost due to a small stop (x), and the probability that the market will either give us minor
adversity (p1 ) or major adversity (p2 ). Note that the speculator determines the values of w
and x by his/hers risk-to-reward appetite, but the market determines the probabilities p1
and p2 .
If the equation 1 is greater than zero, the speculator expects a profit, but if it is less than
zero, the speculator expects to lose money. Also, because the speculator is only in control
of the variables x and w, we need to express the equation as strict inequality, and solve it in
terms of p1 and p2 . In other words, we need to find out for which market conditions it is
always advantageous to accept Less Risk by finding out when the expected payoff from
playing Less Risk is greater than zero. Thus we obtain the following:
ES ( R− ) > 0 ⇐⇒ w − ( p1 + p2 )(w + x ) > 0 ⇐⇒ p1 + p2 <

w
w+x

368
369
370
371
372
373
374
375
376
377
378
379

(3)

Note that we are considering a strict inequality because if ES ( R− ) = 0 it is not profitable to
play the Less Risk strategy, because its expected payoff is zero.
With all of this, we can incorporate equation 3 into the probability triangle yielding the
following:

380
381
382
383

Version August 20, 2024 submitted to Journal Not Specified

15 of 50

Figure 11. The probability triangle divided into two regions: "Play Less Risk" and "Do not Play".
384

Remark 5. Note that, by definition of w and x:
w < w + x ⇐⇒

385

w
<1
w+x

(4)
386
387

The "Play Less Risk" area contains the points where it is profitable to play the strategy
of Less Risk, and the "Do Not Play" region contains money-losing strategies. Also, because
equation 3 was developed as a strict inequality, the line diving the two regions is not
included in the "Play Less Risk" area, so the points on the line (ES ( R− ) = 0) are included in
the area of loss.
Again, the line dividing these areas is determined exclusively by the parameters set by
the speculator, so this line will vary from individual to individual, always based on each
individual’s risk-to-reward appetites, also the value yielded by w/(w + x ) is not a constant
that holds true for all players in the market. But, since we are developing a model in the
general case, it must hold true for each and every person, no matter what their individual
circumstances are.
Moving forward, we can now focus on determining when it is advantageous to accept
More Risk, however it is not as straightforward as it was for Less Risk, because it is only
advantageous to accept More Risk when the market is playing Minor Adversity. And,
under this condition, a strategy of Less Risk will cause a small loss, but a strategy of More
Risk results in a profit.
Looking back at the game table 2:

388

•

405

•

under market conditions of Zero Adversity, both strategies yield a profit, so the
speculator is indifferent between the strategies;
under market conditions of Minor Adversity, a strategy of More Risk generates a
profit, and the strategy of Less Risk causes a loss, so it is advantageous to utilize the
More Risk strategy;

389
390
391
392
393
394
395
396
397
398
399
400
401
402
403
404

406
407
408
409

Version August 20, 2024 submitted to Journal Not Specified

•

16 of 50

if the market conditions correspond to Major Adversity, both the speculator’s strategies
are unprofitable, but the Less Risk strategy causes a smaller loss than does the More
Risk strategy, so it is less advantageous to play More Risk.

410

We know that, by equations 1 and 3, if the expected payoff from the Less Risk strategy is
positive, then we are "guaranteed" a positive payoff when Less Risk is played. So, to find
out when the strategy of More Risk yields a positive payoff when the strategy of Less Risk
does not, we need to analyze equation 2 while 1 is negative.
So, we need to to find out for which market conditions it is always advantageous to accept
More Risk by finding out when the Expected Payoff from playing More Risk (R+ ) is greater
than zero, assuming that ES ( R− ) < 0. Thus we obtain the following:

413

ES ( R+ ) > 0 ⇐⇒ w − p2 (w + y) > 0 ⇐⇒ p2 <

w
w+y

411
412

414
415
416
417
418
419

(5)

Note that we are considering a strict inequality because if ES ( R+ ) = 0 it is not profitable to
play the More Risk strategy, since its expected payoff is zero. Also, observe that equation
5 is only in terms of Major Adversity (p2 ) and it implies that if the probability of Major
is greater than w/(w + y) then the trade will lose money, otherwise the trade will make
money. In terms of game theory, if the probability of Major Adversity is greater than
w/(w + y), then we will not play the game, and if the probability of Major Adversity is
less than w/(w + y), then we play the pure strategy of More Risk. Additionally, if the
probability of Major Adversity is equal to w/(w + y), then the trade will result in a profit
of zero, thus we will also not play the game.
With all of this, we can incorporate equation 5 into the probability triangle yielding the
following:

420
421
422
423
424
425
426
427
428
429
430

Probability
of Major
Adversity

1

DO NOT PLAY

PLAY MORE RISK

Probability of Minor Adversity

0

1

Probability
of Minor
Adversity

Figure 12. The probability triangle divided into two regions: "Play More Risk" and "Do not Play".
431

Remark 6. Regarding the previous probability triangle, note that:
•
•

w
w+y < 1;

by definition of w and y: w < w + y ⇐⇒
(
(
p2 = ww+y
p2 = ww+y
⇐⇒
.
p1 = 1 − ww+y
p1 + p2 = 1

432
433

434

Version August 20, 2024 submitted to Journal Not Specified

17 of 50

435
436

Here, the lower region contains the conditions where it is advantageous to play the
pure strategy of More Risk, and the upper region is where it is disadvantageous to play
More Risk. Also, once again, the points in the separating line (ES ( R+ ) = 0) are included in
the Do Not Play area.
The same reasoning used to understand the implications of playing the pure strategy of
Less Risk hold true for the strategy of More Risk, i.e., points within the "Play More Risk"
area represent profitable trades and points within the "Do Not Play" area represent losses.
Also, once again, the solutions must be interpreted in a probabilistic sense.
Now that we know when it is advantageous to play More Risk (assuming that the result of
playing Less Risk is negative), we need determine when it is advantageous to play More
Risk despite the result of playing Less Risk, because there is a region of the probability
triangle where the two strategies overlap. So we still need to determine when it is advantageous to play More Risk, irrespective of the merit of playing Less Risk. Thus we need to
solve the following equations:
•
•

ES ( R+ ) > 0 ⇐⇒ w − p2 (w + y) > 0 ⇐⇒ p2 < ww+y ;
ES ( R− ) < ES ( R+ ) ⇐⇒ w − ( p1 + p2 )(w + x ) < w − p2 (w + y)

(6)

⇐⇒

y− x
p1 > p2 w + x .

(7)
Consider that equation 7 was developed as an equality, then if the probability of Minor
Adversity is equal to zero (i.e., p1 = 0), then the probability of Major Adversity has to equal
to zero as well (i.e., p2 = 0). However, in the inequality, if p1 were zero, then p2 would
have to be less than zero, but this is in conflict with the variables’ definitions, because
probabilities can only take values between zero and one, thus they cannot be negative. Also,
the probability of Major Adversity occurring in the real world is not less than zero, because,
if this were true, all the players in the market would always win. Moreover, since the
formula that expresses the slope of the line ((y − x )/(w + x )) is always a positive number
(as the variables x, y and w are all positive numbers), whenever p1 is zero, then p2 has to
be zero, and vice versa. Also, the line itself represents the boundary where it is equally
advantageous to play the pure risk strategies of either Less Risk or More Risk, and the area
above the line defines where it is advantageous to play Less Risk.
All of these results are combined in the following probability triangle:

437
438
439
440
441
442
443
444
445
446
447
448
449
450
451
452
453
454
455
456
457
458
459
460
461
462
463
464
465
466

Version August 20, 2024 submitted to Journal Not Specified

18 of 50

Probability
of Major
Adversity

1

PLAY LESS RISK

PLAY MORE RISK

Probability of Minor Adversity

Probability
0

1

of Minor
Adversity

Figure 13. The probability triangle with all the analyzes done so far, which is divided into three
regions: "Play Less Risk", "Play More Risk" and "Do Not Play".
467

Remark 7. Regarding the previous probability triangle, note that:
•
•

2 + wx + wy
w(w+y)+w(w+ x )
w
w
2
> 1 ⇐⇒ w2w
2 + wy + wx + xy > 1 ⇐⇒ 2w + wx +
w+ x > 1 − w+y ⇐⇒
(w+ x )(w+y)
wy > w2 + wy + wx + xy ⇐⇒ w2 > xy, which is true because, by definition, w ≥ y > x;

w(y− x )
1 − ww+y > (w+ x)(w+y)

(
•

p2 = ww+y
(

•

y− x

p1 = p2 w + x
p1 + p2 = ww
+x

(
•

y− x

p1 = p2 w + x

p1 + p2 = ww
+x
p2 = ww+y

⇐⇒

⇐⇒ 1 > ww+ x ⇐⇒ x > 0, which is true by definition of x;

 p = w(y− x )
1
(w+ x )(w+y)
;
 p2 = w
w+y


 p = w(y− x )
1
(w+ x )(w+y)
⇐⇒
 p2 = w
w+y

 p = w(y− x )
1
(w+ x )(w+y)
⇐⇒
 p2 = w

468
469
470
471

472

;

473

.

474

w+y

475
476
477

In the previous probability triangle, there are three regions: the Do Not Play region,
the Less Risk region, and the More Risk region. Also the dotted lines show the location of
the original regions, as well some relevant intersection points. Note that all of the interior
lines intersect at one point (p1 = (w(y − x ))/((w + x )(w + y)), p2 = w/(w + y)), and
that we included the separation line between the Less Risk and More Risk regions (i.e.,
y− x
p1 = p2 w+ x ) in the Less Risk region, but the intersection point between all the interior lines
is considered a part of the Do Not Play region.
Finally, observe that, in all of the obtained probability triangles, a "Do Not Play" region has
appeared which is not related to any possible strategy (on the presented financial game)
that the speculator can choose from. However, the "Do Not Play" strategy is implicit in the
game tables 1 and 2. To see this consider the game table 2 and that the speculator has an

478
479
480
481
482
483
484
485
486
487
488

Version August 20, 2024 submitted to Journal Not Specified

19 of 50

additional "Do Not Play" strategy. So, if the speculator chooses this strategy, then he/she
will not enter the trade, and thus will not lose or win with the trade. Hence, the payoffs
from this strategy are always zero independently of the market’s strategy. So, the game
table 2 becomes:

489
490
491
492

Table 3. The game table for the financial market game including the "Do Not Play" (D) strategy.

Market

p0
p1
p2

0A
mA
MA

q1
R+
w
w
−y

Speculator
q2
1 − q1 − q2
R−
D
w
0
−x
0
−x
0

However, the payoffs from adding this strategy do not change any of the calculations
that we made to determine the several probability triangles, also these would only be
relevant if we wanted to determine the best mixed strategy for the speculator to play
(specifically, the probabilities q1 , q2 and 1 − q1 − q2 would be important). But, since we
only want to determine the best pure strategy that the speculator should play (i.e., one of
the speculator’s probabilities will be equal to one) by taking into account the market’s probabilities (p0 , p1 and p2 ), the "Do Not Play" strategy being explicit or not in the game table is
not relevant, but this strategy is still important to the overall, because it complements the
speculator’s other two strategies (Play More Risk and Play Less Risk).
So, the complete model, which incorporates all of the previous calculations and graphic
representations, has the general form shown by the probability triangle in Figure 13. Also,
this probability triangle represents the situation a speculator faces in a financial market,
because it takes into account the speculator accepting either More Risk or Less Risk, and the
market generating conditions of either Zero Adversity, Minor Adversity, or Major Adversity
(always with respect to the speculator’s position). Additionally, the probability triangle has
Minor Adversity and Major Adversity as its axes, yet it also shows the condition of Zero
Adversity, which is the complete absence of both Major Adversity and Minor Adversity,
which is represented by the origin point on the probability triangle.
Always have in mind that the model has to be interpreted in terms of "if these certain
probabilities exist, then we should play a specific strategy". So the model cannot tell us
what the probabilities are, it only tells us that if certain probabilities exist, then a particular
strategy should be employed. Thus, if we play the financial game repeatedly, under some
predetermined circumstances, the wins will outweigh the losses, and the net result of
our successive plays will be profitable, this is because we need to interpret the model
in the probabilistic sense rather than in an absolute sense. For instance, the model does
not suggest that each and every trade that falls within the parameters of w/(w + x ) will
necessarily be profitable, only that over time the amount won will be greater than the lost.
Now that we have the complete model, we need to estimate the probabilities of the market
playing the strategies of Major Adversity and Minor Adversity. Furthermore, we need to
make these estimates as accurate as possible, because if they are not, the model will lose its
predictive value. And we will accomplish this in the next section, with the aid of Markov
Chains.

493
494
495
496
497
498
499
500
501
502
503
504
505
506
507
508
509
510
511
512
513
514
515
516
517
518
519
520
521
522
523
524
525

2.1.3. Parallel to Barrier Options

526

As it was mentioned before, the presented methods would be optimal if they were
utilized as an automated system to purchase barrier options. Thus, we will briefly present
barrier options an their parallelism to our financial game.
Barrier options are a type of exotic financial derivative where the payoff depends on
whether the underlying asset reaches or exceeds a predetermined price, known as the
barrier. They are more complex than standard options and are considered path-dependent

527
528
529
530
531
532

Version August 20, 2024 submitted to Journal Not Specified

20 of 50

because their value changes based on the underlying asset’s price movements during the
option’s term.
There are two main types of barrier options:

533

•

Knock-in Options: These options only become active if the underlying asset’s price
reaches a specified barrier. They can be further classified into:

536

Up-and-In Call: Activated when the asset’s price rises above the barrier.
Down-and-In Put: Activated when the asset’s price falls below the barrier.

538

Knock-out Options: These options become void if the underlying asset’s price reaches
a specified barrier. They can be further classified into:

540

Up-and-Out Call: Ceases to exist when the asset’s price rises above the barrier.
Down-and-Out Put: Ceases to exist when the asset’s price falls below the barrier.

542

Barrier options are often used for hedging or speculative purposes and typically have lower
premiums compared to standard options due to the added complexity and conditions (for
further details on barrier options see [52]).
In the previous section 2.1.1, for the financial game, we defined the speculator’s possible
strategies and to each strategy will be associated a threshold related to the speculator
possible profits or losses (Less Risk, More Risk and Profit thresholds), in the next sections
(2.2, 2.4) we will specifically define these thresholds for each strategy.
Each threshold will be link to the asset’s own value, which will result in a profit/loss to
the speculator when it is achieved by the asset’s price. So, these thresholds can be directly
linked to the barriers on the barrier options, that is:

544

•

when the model predicts Zero Adversity or Minor Adversity, the speculator can
purchase an Up-and-In Call Option with the a barrier of More Risk, which will yield a
profit associated with the More Risk threshold.
when the model predicts Major Adversity, the speculator can purchase a Down-and-In
Put Option with the barrier of More Risk, which will yield a profit associated with the
More Risk threshold.

554

These are the straightforward strategies using barrier options than can be considered using
the predicted strategies.

560

2.2. The Markov Chains Model

562

As we have seen in the previous section, playing the markets is an iterated game, so
the next important task that we have to address is the (probabilistic) method that we will
use to estimate the probabilities of the market playing Zero Adversity, Minor Adversity
and Major Adversity (p0 , p1 and p2 respectively).

563

–
–
•

–
–

•

534
535

537

539

541

543

545
546
547
548
549
550
551
552
553

555
556
557
558
559

561

564
565
566
567

Remark 8. Here we need to note that the Bayes’ Theorem [53] will not be the primary method used
because we will use Markov Chains to model market behavior. Markov Chains excel at capturing
sequences of events where the probability of the next event depends solely on the current state, not
the entire history, which does not allow us to directly apply Baye’s theorem. Instead, we focus
on estimating transition probabilities within the Markov Chain. These probabilities represent the
likelihood of the market shifting from one strategy (e.g., "Minor Adversity") to another (e.g., "Major
Adversity") in a single time step.

568
569
570
571
572
573
574
575

The financial assets’ prices fluctuate from a variety of ranges (but always strictly
positive). Thus we need to split the data into classes in order for us to make some kind of
probabilistic analysis. For this, consider the standard deviation (α) of a dataset transformed
with the percentage change transformation, and define the strategies’ thresholds as:

576

•

580

•

the Less Risk threshold corresponds to minus two times the standard deviation of the
data (−2α);
the More Risk threshold corresponds to minus three times the standard deviation of
the data (−3α);

577
578
579

581
582
583

Version August 20, 2024 submitted to Journal Not Specified

•

21 of 50

the profit threshold corresponds to three times the standard deviation of the data
(3 · α).

584

Since different assets from the stock market have different price ranges and levels of
volatility, then by defining the thresholds in this manner, we will maintain a certain
coherence across all the datasets. Also, note that the less and More Risk thresholds have to
be negative, because they correspond to possible losses. Additionally, since the datasets’
unit of measure is the percentage change, the standard deviation’s unit of measure is also
the percentage change.
After defining the thresholds, we can formally say what is the relationship between the
market’s chosen strategies with an asset’s price. Thus, to accomplish this, we will assume
that:

586

the asset’s price drops further than the Less Risk threshold if and only if the market
chooses to play the Minor Adversity strategy;
the asset’s price drops further than the More Risk threshold if and only if the market
chooses to play the Major Adversity strategy;
the asset’s price increases further than the profit threshold if and only if the market
chooses to play the Zero Adversity strategy.

595

Now, consider that we observed the asset’s percentage price change for N successive
and mutually independent financial market games, and that we want to determine the
mentioned probabilities for the next (N + 1) game. Also, the percentage price change of
game i is denoted by Xi , i = 1, . . . , N + 1. Additionally, assume that if the thresholds of
Major Adversity or Zero Adversity are reached in a game, suppose that it was on game
k ∈ {1, . . . , N }, then the speculator will not play on the following games, k + 1, . . . , N,
otherwise the speculator will continue to play. We need to assume this because, if the
speculator loses or wins on a game, then we will not continue playing, due to the trade
being closed, and if the price does not reach one of the thresholds, the speculator will not
win nor lose the game, so he/she needs to keep playing, because the trade is still open.

601

•
•
•

585

587
588
589
590
591
592
593
594

596
597
598
599
600

602
603
604
605
606
607
608
609
610
611

Remark 9. Note that if the market chooses to play Minor Adversity, the speculator only has to stop
playing if he/she played the Less Risk strategy.

612
613
614

With all of this, we can start estimating the desired probabilities for the ( N + 1)th
game, knowing that the probability of the market playing a certain strategy at game N + 1
is related to the probabilities of the market’s choices on the N previous games, i.e., we want
to determine
p 0 = P ( X N + 1 ≥ 3 · α | X1 , . . . , X N ) ,
p 2 = P ( X N + 1 ≤ − 3 · α | X1 , . . . , X N ) ,
p1 = 1 − p0 − p2 .
615
616

Remark 10. Note that we will not directly estimate p1 , because it is simpler to estimate p0 and p2 ,
due to the way we defined these probabilities. Also, we can do this because p0 + p1 + p2 = 1. So,
moving forward, we will not reference the estimator of p1 unless we see fit to do so.

617
618
619
620

Firstly, suppose that we only consider one game to determine our probabilities, i.e.,
we will start by considering N = 1, so we have the following:
•
•

p 2 = P ( X2 ≤ − 3 · α | X1 ) = P ( X1 ≤ − 3 · α ) ;
p 0 = P ( X2 ≥ 3 · α | X1 ) = P ( X1 ≥ 3 · α ) .

621
622

(8)
(9)

623

We can interpret equation 8 for the probability of the market playing Major Adversity as
follows: if the percentage price change reaches the More Risk threshold in game 1, then
the speculator stops playing. So, the probability of the price change reaching the More
Risk threshold is obtained by simply calculating the probability of the percentage change

625

624

626
627
628

Version August 20, 2024 submitted to Journal Not Specified

22 of 50

reaching the More Risk threshold in the previous game, i.e., P( X1 ≤ −3 · α).
Similarly, the probability of the market playing the Zero Adversity strategy is obtained by
calculating the probability of the percentage change reaching the profit objective threshold
in the previous game, i.e., P( X1 ≥ 3 · α).
However, since we have access to more historical data of the asset’s price, we can determine
these probabilities more accurately by taking into account more games. Now, consider
that we will use the results of two past games to determine our probabilities, i.e., we will
consider N = 2, thus we obtain:
p 2 = P ( X3 ≤ − 3 · α | X2 , X1 ) =

= P( X1 ≤ −3 · α) + P(−3 · α < X1 ≤ 3 · α ∧ X2 ≤ −3 · α);
p 0 = P ( X3 ≥ 3 · α | X2 , X1 ) = P ( X1 ≥ 3 · α ) + P ( X1 < 3 · α ∧ X2 ≥ 3 · α ) .

629
630
631
632
633
634
635
636

(10)
(11)
(12)

Thus we can can interpret the new equation 10 for the probability of the market playing
Major Adversity as follows: the speculator stops playing, if the percentage price change
reaches the More Risk threshold in game 1 or if the threshold is only reached in game 2
(implying that, in game 1, no threshold was reached). So, the probability of the price change
reaching the More Risk threshold is obtained by adding the probability of the percentage
change reaching the More Risk threshold in game 1 to the probability of the percentage
change reaching the More Risk threshold in game 2 without reaching it in game 1. And, a
similar interpretation can be given to equation 11.
Finally, we can obtain even more accurate probabilities if we consider the results of all
the played games (i.e., by considering all the historical price data). Thus, considering the
results of N games, the equations for the desired probabilities are:

637
638
639
640
641
642
643
644
645
646
647

p 2 = P ( X N + 1 ≤ − 3 · α | X N , . . . , X1 ) =

= P( X1 ≤ −3 · α) + P(−3 · α < X1 < 3 · α ∧ X2 ≤ −3 · α)+
+ P(−3 · α < X1 < 3 · α ∧ −3 · α < X2 < 3 · α ∧ X3 ≤ −3 · α) + · · · +
+ P(−3 · α < X1 < 3 · α ∧ −3 · α < X2 < 3 · α ∧ −3 · α < X3 < 3 · α∧
∧ · · · ∧ −3 · X N ≤ −3 · α ).

(13)

p0 = P( X N +1 ≥ 3 · α| X N , . . . , X1 ) = P( X1 ≥ 3 · α) + P( X1 < 3 · α ∧ X2 ≥ 3 · α)+

+ P ( X1 < 3 · α ∧ X2 < 3 · α ∧ X3 ≥ 3 · α ) + · · · +
+ P ( X1 < 3 · α ∧ X2 < 3 · α ∧ X3 < 3 · α ∧ · · · ∧ X N ≥ 3 · α ) ;

(14)

The intuition behind the obtained equations 14 and 13 is similar to the one that we used to
obtain the equations 8 and 9. Also, because the N games are mutually independent, from
basic probability theory we have that the equations 14 and 13 are equivalent to:

648
649
650

p 2 = P ( X N + 1 ≤ − 3 · α | X N , . . . , X1 ) =

= P( X1 ≤ −3 · α) + P(−3 · α < X1 < 3 · α) P( X2 ≤ −3 · α)+
+ P(−3 · α < X1 < 3 · α) P(−3 · α < X2 < 3 · α) P( X3 ≤ −3 · α) + · · · +
+ P(−3 · α < X1 < 3 · α) P(−3 · α < X2 < 3 · α) P(−3 · α < X3 < 3 · α) · · ·
· · · P(−3 · X N ≤ −3 · α)

(15)

p0 = P( X N +1 ≥ 3 · α| X N , . . . , X1 ) = P( X1 ≥ 3 · α) + P( X1 < 3 · α) P( X2 ≥ 3 · α)+

+ P ( X1 < 3 · α ) P ( X2 < 3 · α ) P ( X3 ≥ 3 · α ) + · · · +
+ P ( X1 < 3 · α ) P ( X2 < 3 · α ) P ( X3 < 3 · α ) · · · P ( X N ≥ 3 · α ) ;

(16)

From these equations we can see that, for example, to estimate p0 (and p2 ), we would have
to estimate ( N ( N + 1))/2 probabilities, which would be computationally inefficient and
the error from the final estimate would increase due to the large number of individual

651
652
653

Version August 20, 2024 submitted to Journal Not Specified

23 of 50

estimates. So, to overcome these problems we will use Markov chains to estimate the
probabilities p0 , p1 and p2 .
Thus, using the same assumptions and notations as before:

654
655
656

the asset’s percentage price change for N successive financial market games is known;
the percentage price change of game i is denoted by Xi , i = 1, . . . , N + 1;
we want to determine the mentioned probabilities the N + 1th game;
if any of thresholds is reached in a game, suppose that it was on game k ∈ {1, . . . , N },
then the speculator will not play on the following games, k + 1, . . . , N, otherwise the
speculator will continue to play.

657

Now, because we will use Markov Chains, we need to assume that the probabilities
associated with each game are related through the Markov property (for further details see
[33]):

663

•
•
•
•

658
659
660
661
662

664
665

Definition 1 (Markov Property). A stochastic process { xt , t = 0, 1, 2, . . . } with a discrete and
finite (or countable) state space S is said to be a Markov chain if for all states i0 , i1 , . . . , it−1 , i, j and
(steps) t ≥ 0:
P( xt+1 = j| x0 = i0 , . . . , xt−1 = it−1 , xt = i ) = P( xt+1 = j| xt = i ) = pijt,t+1 .
So, we obtain the following estimators for p0 and p2 :
•
•

p 0 = P ( X N + 1 ≥ 3 · α | X N , . . . , X1 ) = P ( X N + 1 ≥ 3 · α | X N ) ;
p 2 = P ( X N + 1 ≤ − 3 · α | X N , . . . , X1 ) = P ( X N + 1 ≤ − 3 · α | X N ) .

666

(17)
(18)

667

In order for us to be able to use the percentage price change (of a given asset) at game
i (i.e., to use Xi ) as the underlying stochastic process of the Markov chain, we need to split
the data into classes (or states). Also, by defining the Markov chain we will obtain its
probability matrix, which will allow us to estimate p0 and p2 .
Before moving further, we need to note that, for instance, if the price is (at a certain time)
on a lower price class (relative to the initial price), then it will have a higher probability of
transitioning to a higher price class, due to the nature of the data that we are utilizing, and
a similar argument can be made if the price is on a higher class (as we have seen in Chapter
1). However, this is represented by the Markov property, because the probability of the
Markov chain being in a certain state at time t only depends on which state the chain was
at time t − 1, so this probability may change according to which states the chain encounters
itself in time t − 1. And this fact will also affect on how we will define the chain’s classes.
To define the classes we can utilize the standard deviation (which we previously denoted
by α) of the dataset, and since we defined (and used) the strategies’ thresholds, we will split
the data "around" these thresholds values, also the classes’ ranges and distance between
them will be α.
Additionally, due to the mentioned volatility and wide range of the assets’ prices, they may
reach one of the thresholds in the first game (or iteration), or they may not reach them at
all. So, for these reasons we will define some intermediate classes between the the classes
associated with the thresholds (or market strategies). Thus, with all of this, we obtain that
the classes (or states) are:

669

•
•
•

the Major Adversity class is s M = { Xt : Xt ≤ −2.5 · α};
(19)
the Minor Adversity class is sm = { Xt : −2.5 · α < Xt ≤ −1.5 · α};
(20)
the intermediate classes between Minor Adversity and the Zero Adversity classes are:
–
–
–
–

•

s1 = { Xt : −1.5 · α < Xt ≤ −0.5 · α};
s2 = { Xt : −0.5 · α < Xt ≤ 0.5 · α};
s3 = { Xt : 0.5 · α < Xt ≤ 1.5 · α};
s4 = { Xt : 1.5 · α < Xt ≤ 2.5 · α}.

the Zero Adversity (or Profit) class is s Z = { Xt : Xt > 2.5 · α}.

(21)
(22)
(23)
(24)
(25)

668

670
671
672
673
674
675
676
677
678
679
680
681
682
683
684
685
686
687
688
689
690
691
692
693
694
695
696
697

Version August 20, 2024 submitted to Journal Not Specified

24 of 50

698

Remark 11. Note that, instead of using the previously defined threshold to limit the classes, we
chose to define the classes around these thresholds, in order to include them. However, if all the
classes maintain a certain coherence according to the thresholds and have the same range (excluding
the s M and s Z classes), then we will obtain similar results after applying our models.

699
700
701
702
703

As an example, consider the dataset

{45.00, 44.49, 43.44, 40.17, 41.05, 41.53, 41.36, 40.68, 40.46, 38.42}

704

(26)

to be the prices of some financial asset for ten consecutive days, then its percentage change
transformed dataset (rounded to two decimal cases) is:

{−1.13, −2.36, −7.53, 2.19, 1.17, −0.41, −1.64, −0.54, −5.04},

706

(27)

which was obtained by applying the percentage changes transformation. So, the standard
deviation of this transformed dataset is 3.00 (which also is a percentage), i.e., α = 3.00.
Hence the classes, for this example, are:
•
•
•
•
•
•
•

705

s M = { Xt : Xt ≤ −2.5 · α} = { Xt : Xt ≤ −7.5};
sm = { Xt : −2.5 · α < Xt ≤ −1.5 · α} = { Xt : −7.5 < Xt ≤ −4.5};
s1 = { Xt : −1.5 · α < Xt ≤ −0.5 · α} = { Xt : −4.5 < Xt ≤ −1.5};
s2 = { Xt : −0.5 · α < Xt ≤ 0.5 · α} = { Xt : −1.5 < Xt ≤ 1.5};
s3 = { Xt : 0.5 · α < Xt ≤ 1.5 · α} = { Xt : 1.5 < Xt ≤ 4.5};
s4 = { Xt : 1.5 · α < Xt ≤ 2.5 · α} = { Xt : 4.5 < Xt ≤ 7.5};
s Z = { Xt : Xt > 2.5 · α} = { Xt : Xt > 7.5}.

707
708
709
710
711
712
713
714
715
716

2.2.1. Defining the Markov Chains

717

Before formally defining the necessary Markov Chains, we need to make some observations about the described classes. According to our assumptions, if the market chooses
to play Major Adversity or Zero Adversity, the speculator will have to stop playing (which
will result in a major a loss or in a profit, respectively) independently of the speculator’s
chosen strategy, but if the market chooses to play Minor Adversity, the speculator only has
to stop playing if he/she chose the Less Risk strategy.
Also, with the aid of game table 2 (from the previous section (2.1)), we can see that the
results of the market playing the Major Adversity strategy are only noticeable if the speculator chooses to play the More Risk strategy, because if the speculator chooses the Less Risk
strategy he/she will stop playing the game immediately after the Less Risk threshold is
reached, thus he/she will not know if the price further increased or decreased.
Thus, assuming that the speculator chose the More Risk strategy, we can determine the
probability of the market playing the Major Adversity strategy. Also, if we assume that the
speculator chose to play the Less Risk strategy, then we can determine the probability of
the market playing the Zero Adversity strategy, this is because, in this case, the speculator
only has a profit if the market chooses this strategy.
So, for these reasons we will define two Markov Chains, one where we consider that the
speculator chose the Less Risk strategy and another where he/she chose to play the More
Risk strategy. However, we will always use the same assumptions, strategies’ thresholds and data for both the Markov Chains, so that we can utilize the probability matrices from each to estimate the probabilities p0 , p1 and p2 . Also, we will assume that
s2 = { Xt : 0.5 · α < Xt ≤ 0.5 · α} is the initial state for both the Markov chains, because
when the speculator enters for trade of a certain asset, then the asset’s initial percentage
price change will be 0% which is an element of the s2 class.
Regarding the Markov Chain where we assume that the speculator chose to play the More
Risk strategy, we have the following observations about its states (or classes):

718

•

The classes s M , sm , s1 , . . . , s4 , s Z will retain the same definitions as before

719
720
721
722
723
724
725
726
727
728
729
730
731
732
733
734
735
736
737
738
739
740
741
742
743
744

Version August 20, 2024 submitted to Journal Not Specified

•

•

25 of 50

To represent the fact that the speculator only stops playing if the price enters the Major
Adversity class (s M ) or the Zero Adversity class (s Z ) in the Markov Chain, we simply
must define these classes as absorbing states, i.e., if the price enters one of these classes,
then it will never exit them (for more details see [32], [33] and/or [36]).
Since the speculator does not stop playing if the price is in one of the remaining classes,
the price may go to any class (including staying in the same class). And, to represent
this in terms of Markov Chains, we simply define these classes as transient (for more
details see [32], [33], [36] and/or[37]). Also, these states (sm , s1 , . . . , s4 ) communicate
between themselves, thus they form a communicating class in the Markov Chain.

745
746
747
748
749
750
751
752
753

In the terms of Markov Chains, for this Markov Chain, we are considering the stochastic process { Xt , t = 1, 2, . . . , N }, where Xt is the percentage price change at game t,
with a discrete and finite state space S = {s M , sm , s1 , . . . , s4 , s Z }, where for all states
S0 , S1 , . . . , St−1 , Si , S j ∈ S and steps (or games) t ∈ {1, . . . , N }:
P( Xt+1 = S j | X1 = S0 , . . . , Xt−1 = St−1 , Xt = Si ) = P( Xt+1 = S j | Xt = Si ) =: pijt,t+1 .
Here, the steps of the Markov Chain represent each successive game from 1 up until N, and
Si represents a state from the state space S = {s M , sm , s Z , s1 , . . . , s4 }, which is composed by
the classes that we previously defined, thus they have the mentioned properties. Also, the
7 × 7 transition matrix PM associated with this chain will be defined as:
sM

sm

s1

···

s4

sZ

p11
sm  p21

s1  p31

PM = .  .
..  ..

s4  p

p12
p22
p32
..
.

p13
p23
p33
..
.

···
···
···
..
.

p16
p26
p36
..
.

p62
p72

p63
p73

···
···

p66
p76


p17
p27 

p37 

.. 
. 

p67 
p77

sM



61

sZ

p71

754
755
756
757

(28)

To visualize this Markov Chain we can use the following diagram:

Figure 14. The Markov Chain where we assume that the speculator chose to play the More Risk
strategy.

758

Version August 20, 2024 submitted to Journal Not Specified

26 of 50

Note that we could have simplified the previous diagram by joining the states sm , s1 , . . . , s4759
in the same communicating class. However, it is useful for us to present the Markov chain 760
in this manner, because it allow us to take more conclusions on how the chain develops as 761
we move forward in time.
762
So, assuming that the initial state is s2 (i.e., assuming that π = (0, 0, 0, 1, 0, 0, 0) T ) and that 763
the transition matrix PM related to the Markov chain is well defined, the probability of the 764
market playing the Major Adversity strategy (p2 ) at time (or game) t is given by the first 765
t .
element of πPM
766
Now, regarding the Markov Chain where we assume that the speculator chose to play the 767
Less Risk strategy, we can make similar observations as before, but with some modifications: 768
•

•
•

•

The Major Adversity class is not necessary for this Markov chain, because the speculator will stop playing if the price reaches the Minor Adversity class. So the s M class
will be "included" in the sm class, thus sm is altered to sm = { Xt : Xt ≤ −1.5 · α}
(considering Example 26, this class becomes sm = { Xt : Xt ≤ −4.5}).
The classes s Z , s1 , . . . , s4 are defined as before.
To represent the fact that the speculator stops playing if the price enters the Minor
Adversity class (sm ) or the Zero Adversity class (s Z ) in the Markov Chain, we simply
must define these classes as absorbing states, i.e., if the price enters one of these classes,
then it will never exit them (for more details see [32], [33] and/or [36]).
Since the speculator does not stop playing if the price is in one of the remaining classes,
the price may go to any class (including staying in the same class). And, to represent
this in terms of Markov Chains, we simply define these classes as transient (for more
details see [32], [33], [36] and/or[37]).

769
770
771
772
773
774
775
776
777
778
779
780
781

As before, in the terms of Markov Chains, we are considering the same stochastic process
{ Xt , t = 1, 2, . . . , N }, where Xt is the percentage price change at game t, with a discrete and
finite state space S = {sm , s Z , s1 , . . . , s4 }, where for all states S0 , S1 , . . . , St−1 , Si , S j ∈ S and
steps (or games) t ∈ {1, . . . , N }:
P( Xt+1 = S j | X1 = S0 , . . . , Xt−1 = St−1 , Xt = Si ) = P( Xt+1 = S j | Xt = Si ) =: pijt,t+1 .
Here, the steps of the Markov Chain represent each successive game from 1 up until N,
and Si represents a state from the state space S = {sm , s Z , s1 , . . . , s4 }, which is composed by
the classes that we previously defined, thus they have the mentioned properties. Also, the
6 × 6 transition matrix PL associated with this chain will be defined as:
sm

s1

···

s4

sZ

p11
s1  p21


PL = ...  ...

s4  p51

p12
p22
..
.

p13
p23
..
.

···
···
..
.

p16
p26
..
.

p52
p62

p53
p63

···
···

p56
p66

sm

sZ



p61


p16
p26 

.. 
. 

p56 

782
783
784
785

(29)

p66

To visualize this Markov Chain we can use the following diagram:

786

Version August 20, 2024 submitted to Journal Not Specified

27 of 50

Figure 15. The Markov Chain where we assume that the speculator chose to play the Less Risk
strategy.

Regarding this diagram, note that is its similar to the previous one (14), however, in
this one, the state s M is included in the state sm . Additionally, we could have simplified the
diagram by joining the states s1 , . . . , s4 in the same communicating class. But again, it is
useful for us to present the Markov chain in this manner, for the same reasons as before.
So, assuming that the initial state is s2 (i.e., assuming that π = (0, 0, 1, 0, 0, 0) T ) and that
the transition matrix PL related to the Markov chain is well defined, the probability of the
market playing the Zero Adversity strategy (p0 ) at time/game t is given by the last element
of πPLt .
With all of this, we have the necessary methods to estimate the probabilities of the market
playing Zero Adversity, Minor Adversity and Major Adversity, thus we also have a method
on how to choose the best strategy for a certain dataset. However, the estimation method for
the market’s probabilities is not complete, because we still have to estimate the transition
probability matrix for each of the defined Markov chains. So, this is what we will focus on
until the end of this section. But, before moving further, note that:
•
•

•
•

we will always use the same (percentage change transformed) dataset for all of the
estimations;
since the s Z state is absorbing in both of the chains, then we do not need to estimate
its transition probabilities, i.e., the last row of both the transition matrices (28 and 29)
is of the form (0, . . . , 0, 1);
the state s M in the Markov chain related to the More Risk strategy, like the s Z state, is
absorbing, thus the first row of the transition matrix 28 is of the form (1, 0, . . . , 0);
the state sm in the Markov chain related to the Less Risk strategy, like the s Z state, is
absorbing, thus the first row of the transition matrix 29 is of the form (1, 0, . . . , 0).

787
788
789
790
791
792
793
794
795
796
797
798
799
800
801
802
803
804
805
806
807
808
809

2.2.2. Estimation of the Transition Probabilities

810

To estimate the transition probabilities for each of the Markov chains, lets start by
considering the one where we assume that the speculator chose to play the More Risk

811
812

Version August 20, 2024 submitted to Journal Not Specified

28 of 50

strategy, represented by the following transition matrix (similar to the previously presented
matrix 28):
sM

sm

s1

···

s4

sZ

1
sm  p21

s1  p31

PM = .  .
..  ..

s4  p

0
p22
p32
..
.

0
p23
p33
..
.

···
···
···
..
.

0
p26
p36
..
.

p62
0

p63
0

···
···

p66
0


0
p27 

p37 

.. .
. 

p67 

sM



61

0

sZ

813
814

(30)

1

Now, lets consider that we are departing from state s2 = { Xt : 0.5 · α < Xt ≤ 0.5 ·
α} (the assumed initial state of the chain), so to estimate the transition probabilities
{ p41 , p42 , p43 , · · · , p47 }, we will just determine the relative frequency of each of the sates
using the dataset, and we will use these frequencies on the corresponding row of the
transition matrix.
Utilizing the Example 26, the relative frequencies for the transformed dataset for these
classes are:

815
816
817
818
819
820
821

Table 4. Relative frequencies table considering that the starting state is s2 .

sM

sm

1
9

1
9

s1
2
9

s2
4
9

s3

s4

1
9

sZ

0
9

0
9

And, replacing in the transition matrix (related to Example 26’s Markov chain), we
obtain:
sM

sm

s1

s2

s3

s4

sZ

1
sm  p21

s1  p31

PM = s2 
 1/9
s3 
 p51
s4  p61
sZ
0

0
p22
p32
1/9
p52
p62
0

0
p23
p33
2/9
p53
p63
0

0
p24
p34
4/9
p54
p64
0

0
p25
p35
1/9
p55
p65
0

0
p26
p36
0
p56
p66
0


0
p27 

p37 

0 
.
p57 

p67 
1

sM



822
823

(31)

As it was previously observed, the probabilities of transitioning from state s2 (to any other
state) are not the same as if we considered that we started from a different state. Thus, in
order to take this into account and to still use the relative frequency "method" to estimate
the transition probabilities, we need to slightly alter the classes on which we will determine
the relative frequencies.
For example, consider the classes obtained from Example 26, if the price increased 3% (of
its initial price) at the first iteration of the chain, i.e., the price went from 100% to 103% of
its (initial) value (which translates in a ((103 − 100)/100) ∗ 100 = 3% percentage change in
price), then the chain moved from state s2 to the state s3 . However, if the price is now at the
state s3 and it further increased 3% (comparing to the initial price), the chain will not move
from the s3 state to the s4 state, because , in this case, the price went from 103% to 106%
of its (initial) value, so the percentage change in price is ((106 − 103)/103) ∗ 100 ≈ 2.91%,
which is not a member of the s4 state, thus the chain will remain in the s3 state. So, the
transition from the s3 state to all of the other states is not the same (in terms of percentage
change) as the transition from s2 to all of the other states. And, a similar argument can be
made if we considered that we started from any state different from s2 .
With this in mind, if we want to use the relative frequencies of the dataset to estimate the
transitions from any state to any other, then we need to "re-calculate" the classes in order
for the estimation to be coherent with what we assumed and defined. So, to accomplish
this, we need to consider the percentage change of price regarding the previous iteration of
the chain, and not the percentage change regarding the initial price.

824
825
826
827
828
829
830
831
832
833
834
835
836
837
838
839
840
841
842
843
844

Version August 20, 2024 submitted to Journal Not Specified

29 of 50

Again, for example, to estimate the transition from the s3 state to the s4 state, we need to
assume that the initial state is the s3 state and that we want to transition to the s4 state,
i.e., we need to assume the percentage price change (relative to the s2 ) is at 103% and
that we want to know what is the percentage price change if the percentage price change
transitioned to 106% (relative to the s2 ), which would be ((106 − 103)/103) ∗ 100 ≈ 2.91%.
Also, because we are dealing with classes, this obtained percentage change between classes
will be used as the "new" α to determine the limits (and ranges) of the classes, this is because
s3 and s4 are consecutive classes in terms of their range of values (as s2 and s3 were in the
base classes). Thus, in this case, the s4 state (or class) becomes s4 = { Xt : 1.46 < Xt ≤ 4.37}.
So, we need to use these "re-calculated" classes to obtain the relative frequencies table,
which will be the estimation for the transition probabilities if we consider that we started
from state s3 .
To generally define the classes which we will use in the relative frequencies table, we need
to consider the direct correspondence f : {sm , s1 , s2 , s3 , s4 } → {2, 1, 0, −1, −2} defined as:

845
846
847
848
849
850
851
852
853
854
855
856
857
858

f (sm ) = 2
f ( s1 ) = 1
f ( s2 ) = 0
f ( s3 ) = −1
f ( s4 ) = −2
So, the "altered" classes (or states) obtained considering that we started from state s ∈
{sm , s1 , s2 , s3 , s4 } are:
s M = { Xt : Xt ≤ (−2.5 + f (s)) · α};
sm = { Xt : (−2.5 + f (s)) · α < Xt ≤ (−1.5 + f (s)) · α};
s1 = { Xt : (−1.5 + f (s)) · α < Xt ≤ (−0.5 + f (s)) · α};
s2 = { Xt : (−0.5 + f (s)) · α < Xt ≤ (0.5 + f (s)) · α};
s3 = { Xt : (0.5 + f (s)) · α < Xt ≤ (1.5 + f (s)) · α};
s4 = { Xt : (1.5 + f (s)) · α < Xt ≤ (2.5 + f (s)) · α};
s Z = { Xt : Xt > (2.5 + f (s)) · α}.

•
•
•
•
•
•
•

(32)
(33)
(34)
(35)
(36)
(37)
(38)

Note that, the value of α used in the equations of the new classes, also needs to be recalculated, which we will see how to do so after determining the "re-calculated" classes for
the Example 26 considering that we started from the s3 state and with α = 2.91, which are:
s M = { Xt : Xt ≤ −10.185};
sm = { Xt : −10.185 < Xt ≤ −7.275};
s1 = { Xt : −7.275 < Xt ≤ −4.365};
s2 = { Xt : −4.365 < Xt ≤ −1.455};
s3 = { Xt : −1.455 < Xt ≤ 1.455};
s4 = { Xt : 1.455 < Xt ≤ 4.365};
s Z = { Xt : Xt > 4.365}.

•
•
•
•
•
•
•

Utilizing the dataset from Example 26, we have the following relative frequencies table for
these classes:
Table 5. Relative frequencies table considering that the starting state is s3 .

sM

sm

0
9

1
9

s1
1
9

s2
2
9

s3
4
9

s4
1
9

sZ
0
9

859
860
861
862
863
864
865
866
867
868
869
870
871
872
873
874
875
876
877
878
879

Version August 20, 2024 submitted to Journal Not Specified

30 of 50

Replacing in the transition matrix 31 (related to Example 26’s Markov chain), we
obtain:
sM

1
sm  p21

s1  p31

PM = s2 
 1/9
s3 
 0
s4  p61
sZ
0
sM



sm

s1

s2

s3

0
0
0
0
p22 p23 p24 p25
p32 p33 p34 p35
1/9 2/9 4/9 1/9
1/9 1/9 2/9 4/9
p62 p63 p64 p65
0
0
0
0

s4

sZ

0
p26
p36
0
1/9
p66
0


0
p27 

p37 

0 
.
0 

p 

880
881

(39)

67

1

Now, for the general case, consider that we want to determine the relative frequencies
assuming that we are departing from the si ∈ {sm , s1 , . . . , s4 } state, then we need to
determine the range of each class, i.e., we need to determine the α that we will use in
the previously presented formulas 32-38. For this, we need to consider si ’s consecutive
class, which is the class that contains the values immediately before the lower limit of si
or after the upper limit of si , and we will denote it as s j . Also, it is not relevant which
of the two that we choose. For instance, if si = sm , then its consecutive classes are s M
and s1 , so s j can be either s M or sm ; likewise, the (only) consecutive class of si = s M is
s j = sm . Thus, after obtaining the consecutive class, consider mi and m j to be the midpoints
of si and s j , respectively. But, if s j is s M or s Z , m j will be the mi + (in f (si ) − sup(si )) or
mi + (sup(si ) − in f (si )), respectively.
So, the α value is obtained by:
m j − mi
(40)
100 .
α=
mi + 100

882
883
884
885
886
887
888
889
890
891
892
893

894

Remark 12. Note that we did not include s M and s Z into the set of possible states that si can be,
this is because the probabilities of departing from these states are fixed, as we saw when we built the
transition matrix 30. Also, in the calculation of the α, we need to consider the absolute value, in
case s j is related to lower limit of si .

895
896
897
898
899

Afterwards, we simply have to determine the classes by replacing the obtained α in all
of the equations 32-38, which we will use to calculate the relative frequencies table of the
(same transformed) dataset. Finally, we just replace the obtained relative frequencies in the
row of the transition matrix related to the si state (or class).
Applying all of this to example 26, we obtain the following transition matrix:
sM

sm

s1

s2

s3

s4

1
0
0
0
0
0

sm
0
0
0
 4/9 4/9 1/9
s1  2/9 2/9 4/9 1/9
0
0

PM = s2 
0
 1/9 1/9 2/9 4/9 1/9
s3 
0
1/9
1/9
2/9
4/9
1/9

0
1/9 1/9 2/9 4/9
s4  0
sZ
0
0
0
0
0
0
sM



900
901
902
903
904

sZ


0
0 

0 

0 
.
0 

1/9 
1

(41)

All the presented estimators and examples are related to the Markov Chain where we
assume that the speculator chose to play the More Risk strategy. So, to estimate the
transition probabilities for the Markov Chain where we assume that the speculator chose to

905
906
907

Version August 20, 2024 submitted to Journal Not Specified

31 of 50

play the Less Risk strategy, which is represented by the following transition matrix (similar
to the previously presented matrix 29):
sm

s1

···

s4

sZ

1
s1  p21


PL = ...  ...

s4  p51

0
p22
..
.

0
p23
..
.

···
···
..
.

0
p25
..
.

p52
0

p53
0

···
···

p55
0

sm

sZ



0


0
p26 

.. .
. 

p56 

908
909

(42)

1

And, like in the PM case, we will determine the relative frequency tables considering that
the chain started from each of the sates s1 , . . . , s4 . So, again assume that we are departing
from the si ∈ {s1 , . . . , s4 } state, then we need to determine the range of each class, i.e., we
need to determine the α that we will use in formulas similar to the previously presented
ones (32-38). So, as before, consider a consecutive class to si , denoted as s j . For instance, if
si = s1 , then its consecutive classes are sm and s2 , so s j can be either sm or s2 ; likewise, the
(only) consecutive class of si = sm is s j = s1 . After obtaining the consecutive class, consider
mi and m j to be the midpoints of si and s j , respectively. But, if s j is sm or s Z , m j will be the
mi + (in f (si ) − sup(si )) or mi + (sup(si ) − in f (si )), respectively.
So, the α value is obtained by:
m j − mi
α=
(43)
100 .
mi + 100

910
911
912
913
914
915
916
917
918
919

920

Remark 13. Note that the equation to obtain α in the PL case is the same as the previous equation
40. Also, we did not include sm and s Z into the set of possible states that si can be, this is because
the probabilities of departing from these states are fixed, as we observed when we built the transition
matrix 29.

921
922
923
924
925

As in the PM case, the transition probabilities are not the same as if we considered
that the chain started from different states. Thus, in order to take this into account and to
still use the relative frequency "method" to estimate the transition probabilities we need
to slightly alter the classes on which we will determine the relative frequencies. So, again
consider the direct correspondence f : {s1 , . . . , s4 } → {2, 1, 0, −1, −2} defined as:

926
927
928
929
930

f ( s1 ) = 1
f ( s2 ) = 0
f ( s3 ) = −1
f ( s4 ) = −2
So, the "altered" classes (or states) for the PL matrix considering that we started from a state
s ∈ {s1 , . . . , s4 } are:
•
•
•
•
•
•

sm = { Xt : Xt ≤ (−1.5 + f (s)) · α};
s1 = { Xt : (−1.5 + f (s)) · α < Xt ≤ (−0.5 + f (s)) · α};
s2 = { Xt : (−0.5 + f (s)) · α < Xt ≤ (0.5 + f (s)) · α};
s3 = { Xt : (0.5 + f (s)) · α < Xt ≤ (1.5 + f (s)) · α};
s4 = { Xt : (1.5 + f (s)) · α < Xt ≤ (2.5 + f (s)) · α}.
s Z = { Xt : Xt > (2.5 + f (s)) · α}.

Now, we will estimate the PL matrix for the same dataset

{45.00, 44.49, 43.44, 40.17, 41.05, 41.53, 41.36, 40.68, 40.46, 38.42}
from Example 26, which resulted into the transformed dataset

{−1.13, −2.36, −7.53, 2.19, 1.17, −0.41, −1.64, −0.54, −5.04}.

(44)
(45)
(46)
(47)
(48)
(49)

931
932
933
934
935
936
937
938

Version August 20, 2024 submitted to Journal Not Specified

32 of 50

Considering that we started from the s3 state (with the consecutive state s4 ), i.e., considering
that:
m j − mi
6−3
α=
100 =
100 ≈ 2.91.
mi + 100
3 + 100
We obtain the classes
•
•
•
•
•
•

939

sm = { Xt : Xt ≤ −7.275};
s1 = { Xt : −7.275 < Xt ≤ −4.365};
s2 = { Xt : −4.365 < Xt ≤ −1.455};
s3 = { Xt : −1.455 < Xt ≤ 1.455};
s4 = { Xt : 1.455 < Xt ≤ 4.365};
s Z = { Xt : Xt > 4.365}.

940
941
942
943
944
945

And, by replacing the relative frequencies, PL is:
sm

1
s1  4/9

s  2/9
PL = 2 
s3 
 1/9
s4  0
sZ
0
sm



s1

946

s2

s3

s4

sZ

0
0
0
0
4/9 1/9
0
0
2/9 4/9 1/9
0
1/9 2/9 4/9 1/9
1/9 1/9 2/9 4/9
0
0
0
0


0
0 

0 
.
0 

1/9 
1

(50)

2.2.3. Estimating the Market’s Probabilities

947

Now, we have everything that we need to estimate the probabilities of the market
playing Zero Adversity (p0 ), Minor Adversity (p1 ) and Major Adversity (p2 ). And, to
accomplish this, we will use two Markov chains to estimate p2 and p0 , as it was previously
explained.
To estimate p2 we will make the use of the Markov Chain where we assumed that the
speculator chose to play the More Risk strategy, which is represented by the transition
matrix 30:

948

sM

sm

s1

···

sZ

1
sm  p21

s1  p31

PM = .  .
..  ..

s4  p

0
p22
p32
..
.

0
p23
p33
..
.

···
···
···
..
.

p62
0

p63
0

···
···


0
p27 

p37 

.. .
. 

p67 

sM



61

sZ

0

950
951
952
953
954

(51)

1

Also, as before, we will assume that the initial state of the chain is s2 , i.e., the probability
distribution of X0 (the first percentage price change of the chain) is given by the π0M =
(0, 0, 0, 1, 0, 0, 0)T .
Since we want to predict what will happen to an asset’s price after we buy it, that is,
we want to know if we will have a profit or a loss (according to the financial game that
we established) after we enter a trade, then it is sensible to consider what will happen
immediately after we buy the asset and/or what is the asset’s price tending to. So, to this
end, we will consider two separate estimators and analyze the obtained results. Thus, p2
will be estimated by:
•
•

949

the probability of the chain reaching the s M state after one iteration;
the long-run probability of the chain being at state s M .

955
956
957
958
959
960
961
962
963
964
965

Version August 20, 2024 submitted to Journal Not Specified

33 of 50

Regarding the first estimator, we will just compute the probability of the chain being at
state s M after one iteration of the chain, so we will compute:
1
 p21


 p31
0 
 p41
 p51

p
61
0


π1M = π0M PM = 0



=

0

0

1

0

0

sM

sm

s1

s2

s3

s4

p41

p42

p43

p44

p45

p46

0
p22
p32
p42
p52
p62
0

0
p23
p33
p43
p53
p63
0

0
p24
p34
p44
p54
p64
0

0
p25
p35
p45
p55
p65
0

0
p26
p36
p46
p56
p66
0

s

Z

p47 .

1
 p21


 p31
0 
 p41
 p51

p
61
0

0
p22
p32
p42
p52
p62
0
Z

πn7 .



=



0

0

1

0

0

sM

sm

s1

s2

s3

s4

πn1

πn2

πn3

πn4

πn5

πn6

967


0
p27 

p37 

p47 
=
p57 

p67 
1

Where, after the matrix multiplication, we obtained a 1 × 7 vector π1M , which is the probability distribution of the chain after one iteration. Here, note that π1M is simply the transition
probabilities starting from the s2 state, which makes sense considering that the initial state
is s2 and we only want to know the probability distribution after one iteration of the chain.
Thus, the first entry of π1M is the probability of the chain being in state s M after one iteration
and our estimator for p2 is: p2 ≈ p41 .
As we can see, this estimator is fairly simple, both in theoretical and in practical terms.
So, to try to understand how the percentage price will evolve, we will also consider a
estimator related to the long term distribution of the chain. However, we need to note that
this probability distribution may not exist, because our chain is not irreducible. So, we
cannot use Theorem II.C.3 from [33] to guarantee that such distribution exists. Also, if such
distribution is to exist, we know (from [32] and [36]) that the chain will tend to its absorbing
states, thus, in our case, the long run probability distribution would be a 1 × 7 vector π
where one of the absorbing states (s M or s Z ) has a probability of one. But, we do not know
when this will happen or which state will have probability one. Hence, to overcome these
issues, we will compute the probability distribution of the chain after n < ∞ iterations:

n
πnM = π0M PM
= 0

966

0
p23
p33
p43
p53
p63
0

0
p24
p34
p44
p54
p64
0

0
p25
p35
p45
p55
p65
0

0
p26
p36
p46
p56
p66
0

968
969
970
971
972
973
974
975
976
977
978
979
980
981
982
983

n
0
p27 

p37 

p47 
 = (52)
p57 

p 
67

1

s

(53)

Thus, after the matrix multiplication, we obtain a 1 × 7 vector πnM , and its first entry is
the probability of the chain being in state s M after n iterations, so our estimator for p2 is:
p2 ≈ πn1 .
Observe that we cannot apply the Theorem II.C.3 from [33] to determine the long-run
probability distribution π of the chain, because it is not irreducible. So, we do need to
compute the n matrix multiplications.
Now, similarly to the estimator of p2 , we will estimate p0 using the Markov Chain where

984
985
986
987
988
989
990

Version August 20, 2024 submitted to Journal Not Specified

34 of 50

we assumed that the speculator chose to play the Less Risk strategy, which is represented
by the transition matrix 42:
sm

s1

···

s4

sZ

1
s1  p21


PL = ...  ...

s4  p51

0
p22
..
.

0
p23
..
.

···
···
..
.

p52
0

p53
0

···
···


0
p27 

.. .
. 

p57 

sm



0

sZ

1

the probability of the chain reaching the s Z state after one iteration;
the long-run probability of the chain being at state s Z .

1
 p21

 p31
0 
 p41

 p51
0

π1L = π0L PL = 0

=



0

1

0

0

0
p22
p32
p42
p52
0

sm

s1

s2

s3

s4

sZ

p41

p42

p43

p44

p45


p46 .

0
p23
p33
p43
p53
0

0
p24
p34
p44
p54
0

0
p25
p35
p45
p55
0

996

1
 p21

 p31
0 
 p41

 p51
0

πnL = π0L PLn = 0

=



0

1

0

0

0
p22
p32
p42
p52
0

sm

s1

s2

s3

s4

sZ

pn1

pn2

pn3

pn4

pn5


pn6 ,

0
p23
p33
p43
p53
0

0
p24
p34
p44
p54
0

0
p25
p35
p45
p55
0

997
998


0
p26 

p36 
=
p46 

p56 
1

Where, after the matrix multiplication, we obtain a 1 × 6 vector π1L . And, again, note that
π1 is simply the transition probabilities starting from the s2 state. Also, the last entry of π1L
is the probability of the chain being in state s Z after one iteration, so our estimator for p0 is:
p0 ≈ p46 .
As before, this estimator is fairly simple, and because this chain is also not irreducible, we
will compute the probability distribution (πnL ) of the chain again after n < ∞ iterations:


993
994
995

Regarding the first estimator, we will just compute the probability of the chain being at
state s Z after one iteration of the chain, i.e. we will compute:


992

(54)

As before, we will assume that the initial state of the chain is s2 , i.e., we will assume
that π0L = (0, 0, 1, 0, 0, 0) T . So, for the same reasons as before, p0 will be estimated by:
•
•

991

999
1000
1001
1002
1003
1004

n
0
p26 

p36 
 =
p46 

p56 
1

which, after the matrix multiplication, yields a 1 × 6 vector πn . And, its last entry is
the probability of the chain being in state s Z after n iterations, so our estimator for p0 is:
p0 ≈ pn6 .
Observe that we had the same issues in both estimators, because the chains were not
irreducible, also we used the same number of iterations n (to determine the long-run
estimator) in both chains, so that we can compare the obtained results from the different
chains. Finally, we need to note that these estimators (for p0 and p2 ) sum up to a value
≤ 1, because, by Section 2.2, the theoretical probabilities that we are estimating have this
property, and by the fact that we are under-estimating the market’s probabilities, since
theoretically we should determine the long-run estimator by using infinite iterations (and
not only n).

1005
1006
1007
1008
1009
1010
1011
1012
1013
1014
1015

Version August 20, 2024 submitted to Journal Not Specified

35 of 50

1016

Remark 14. Even though the used notations for both estimators are similar, the obtained estimated
probabilities result from (n iterations of) different chains, so they represent different probabilities.
Additionally, the estimator for p1 is simply p1 = 1 − p0 − p2 , for both cases.

1017

So, with all of this, we can estimate the probabilities of the market playing a certain
strategy and thus choose the speculator’s optimal strategy according to the previously
presented financial game.
To finalize this section we will just pick up the dataset from the Example 26 (from the
previous section) and compute the estimators for the market’s probabilities. For this, recall
that the obtained transition matrix related to the chain where we assumed the More Risk
strategy is:

1021

1018
1019
1020

sM

sm

s1

s2

s3

s4

1
0
0
0
0
0
sm  4/9 4/9 1/9
0
0
0

s1  2/9 2/9 4/9 1/9
0
0

PM = s2 
1/9
1/9
2/9
4/9
1/9
0

s3 
1/9 1/9 2/9 4/9 1/9
 0
s4  0
0
1/9 1/9 2/9 4/9
sZ
0
0
0
0
0
0


0
0 

0 

0 
.
0 

1/9 
1

s1

1
s1  4/9

s2 
 2/9
PL =
s3 
 1/9
s4  0
sZ
0
sm

s2

s3

s4

0
0
0
0
4/9 1/9
0
0
2/9 4/9 1/9
0
1/9 2/9 4/9 1/9
1/9 1/9 2/9 4/9
0
0
0
0



0

1
4/9


2/9
0 
1/9
 0

 0
0

π1M = π0M PM = 0

=



0

0

1

0

sM

sm

s1

s2

s3

s4

sZ

1/9

1/9

2/9

4/9

1/9

0

0


0
0 

0 
.
0 

1/9 
1

=



1

0

0

1028
1029


0
0 

0 

0 
=
0 

1/9
1

.
1031

1
4/9

2/9
0 
1/9

 0
0

0
0
0
0
4/9 1/9
0
0
2/9 4/9 1/9
0
1/9 2/9 4/9 1/9
1/9 1/9 2/9 4/9
0
0
0
0



0

1027

1030

And with π0M = (0, 0, 0, 1, 0, 0, 0) T we have:

π1L = π0L PL = 0

1026

(56)

0
0
0
0
0
4/9 1/9
0
0
0
2/9 4/9 1/9
0
0
1/9 2/9 4/9 1/9
0
1/9 1/9 2/9 4/9 1/9
0
1/9 1/9 2/9 4/9
0
0
0
0
0


1025

sZ

So, assuming π0M = (0, 0, 0, 1, 0, 0, 0) T , we have that:


1024

(55)

The obtained transition matrix related to the chain where we assumed the Less Risk
strategy is:
sm

1023

sZ



sM

1022

sm

s1

s2

s3

s4

sZ

2/9

2/9

4/9

1/9

0

0



.


0
0 

0 
=
0 

1/9
1

Version August 20, 2024 submitted to Journal Not Specified

36 of 50

So the one iteration estimators for the market’s probabilities, for this example, are:

1032

p0 = 0
p1 = 8/9 ≈ 0.89
p2 = 1/9 ≈ 0.11
Regarding the long run estimator with n = 10 iterations, we have that:

1033

1
0
0
0
0
0
4/9 4/9 1/9
0
0
0

2/9 2/9 4/9 1/9
0
0

0
0 
1/9 1/9 2/9 4/9 1/9
 0
1/9
1/9
2/9
4/9
1/9

 0
0
1/9 1/9 2/9 4/9
0
0
0
0
0
0


n
πnM = π0M PM
= 0

=



0

0

1

0

0

sM

sm

s1

s2

s3

s4

0.9

0.03

0.03

0.02

0.01

0.01

0

1
4/9

2/9
0 
1/9

 0
0

n
0
0 

0 

0 
 =
0 

1/9
1

sZ


1034

0
0
0
0
4/9 1/9
0
0
2/9 4/9 1/9
0
1/9 2/9 4/9 1/9
1/9 1/9 2/9 4/9
0
0
0
0



πnL = π0L PLn = 0

=



0

1

0

sm

s1

s2

s3

s4

0.95

0.02

0.01

0.01

0.01

n

0
0 

0 
 =
0 

1/9
1

sZ


1035

Remark 15. Note that the presented values are rounded with two decimal cases.

1036
1037

So the long-run estimators for the market’s probabilities, for this example, are:

1038

p0 = 0.01
p1 = 0.09
p2 = 0.9
Note that the estimated probabilities, in this example, change drastically from one estimator
to the other, also they suggest that the market (as the iterations of the chain increase) is
increasing its probability of choosing the Major Adversity strategy.
To finalize, the previously presented game table 2 related to the financial game, for this
example, becomes:
Table 6. Example 26’s game table for the financial market game.

Market

p0
p1
p2

Speculator
q
1−q
+
R
R−
0A
9
9
mA
9
−6
M A −9
−6

1039
1040
1041
1042
1043

Version August 20, 2024 submitted to Journal Not Specified

37 of 50

These payoffs (or strategy thresholds) were obtained by applying the theory on Section
2.1 and considering the standard deviation of the transformed dataset (i.e., considering
α = 3), where we obtained w = 9, x = 6 and y = 9.
Now, with the one iteration estimators and considering the probability triangle (also
presented in Section 2.1, but considering these new values), for this case, the speculator
should choose to play the More Risk strategy, because:
p2 = 0.11 <

p
w
y−x
= 0.5 and 1 ≈ 8.09 >
= 0.2.
w+y
p2
w+x

w
w
= 0.5 and p2 = 0.9 >
= 0.5.
w+y
w+y

1045
1046
1047
1048
1049

(57)

And, considering the long run estimator and the same probability triangle, the speculator
should choose not to play, because:
p1 + p2 = 0.99 >=

1044

1050
1051

(58)

Thus, as we can see the two estimators yield different strategies for the speculator to choose.
All of this because the market "changes" its behavior as the iterations increase.

1052
1053
1054

2.3. The SARIMA and GARCH Models

1055

Now that we have discussed the specific game theoretical and Markov chains models
that we will use, it is time to describe how we will use the SARIMA and GARCH models to
predict the market’s behavior, and then compare the accuracy of the three approaches.
However, we need to note that we use Markov chains as an auxiliary model to determine the probabilities for the game’s strategies, so we will also consider the SARIMA and
GARCH models as auxiliary to the base game model. Moreover, we cannot simply apply
the time series models to the raw dataset and make a prediction for the future value of the
time series, because, in order to make the comparison of the models possible, we need to
apply all the models to the same dataset and try to predict the same objects, which in our
case means predicting the strategies that the market will choose. All of this because we can’t
directly compare traditional econometrics models, because these models are deterministic
and our model is probabilistic.
Thus, we will apply the time series models to the same percentage change transformed
datasets that we have been using on the previous sections. So, if we make predictions based
on these models, we obtain percentage change transformed predictions of the asset’s price
(which is useful, but it is not our ultimate goal).
To obtain a prediction of the market’s strategy, firstly we will estimate the optimal time
series models for the dataset. Then, using these estimated models, we will perform K simulations each with N observations, thus obtaining K simulations of percentage change prices
for each of the models and each one starting on the last observation of the transformed
dataset.

1056
1057
1058
1059
1060
1061
1062
1063
1064
1065
1066
1067
1068
1069
1070
1071
1072
1073
1074
1075
1076
1077

Remark 16. All of this will be done with the aid of the R software, which we will elaborate
further on Section 2.4.

1078
1079
1080

Now, as in the previous sections, consider the speculator’s More Risk strategy thresholds in terms of the dataset’s standard deviation α:
•
•

the Profit Objective threshold: s P ≥ 3 · α;
the More Risk threshold: s R ≤ −3 · α.

Finally, for each of the K simulations, we need to check which of the thresholds was reached
first, because the speculator will exit the trade (or the game) when one of these is reached.
And with this we obtain the absolute frequencies of each of the thresholds, and also its
relative frequencies if we divide by K.

1081
1082
1083
1084
1085
1086
1087
1088
1089

Version August 20, 2024 submitted to Journal Not Specified

38 of 50

Remark 17. Note that, as we are performing simulations involving a model which includes
a probability distribution, if we ran the same code several times, we would obtain different results
after each run. However, these results will not have major differences between them.

1090
1091
1092
1093

Hence, we will estimate the probability of the market playing the Major Adversity
strategy (p2 ) with the relative frequency related to the More Risk threshold, and similarly
the probability of the market playing the Zero Adversity strategy (p0 ) with the relative
frequency related to the Profit Objective threshold. Also, by default, the estimation for
probability of the market playing the Minor Adversity strategy (p1 ) is simply 1 − p2 − p0 .
Additionally, since we have the market’s probabilities, then we can choose the speculator’s
optimal strategy according to the probability triangle presented in Section 2.1.2. But, before
moving on, note that we need to determine these probabilities for both the SARIMA and
the GARCH models, so we need to make an estimation for each of these models (but always
using the same dataset), i.e., we need to perform K simulations for each model estimation
and then determine the probabilities for each set of estimations. So, we will obtain two
optimal strategies, one for each of the models.
Thus, for all the models presented so far (specifically, Markov Chain, SARIMA and
GARCH), the speculator will obtain a optimal strategy for each of them, which is done by
estimating the market’s probabilities (which may differ for each model) and then we will
apply the same probability triangle for each set of probabilities.

1094
1095
1096
1097
1098
1099
1100
1101
1102
1103
1104
1105
1106
1107
1108
1109
1110

2.4. Procedures

1111

Now that we have all the necessary models and estimators, it is time to describe how
we will use each model to choose the optimal strategy for a certain dataset. Also, we need
to explain how we will check if the predictions were accurate and how accurate.
Consider an abstract dataset composed by strictly positive values, which will represent the
price of a certain financial asset for n + 1 consecutive iterations (it can be n + 1 consecutive
minutes, days,...). Since we worked with percentage change data in the game theoretical
model, then we will apply the percentage change transformation to the dataset, obtaining
a transformed dataset C = {c1 , . . . , cn } composed with percentage changes of n + 1 consecutive iterations. So, we will apply all of our models to this dataset C. Also, in order
to check the accuracy of our models, we will split the dataset into training (C1 ) and test
(C2 ) sets, where the training set will be composed by the first 80% of the observations and
the remaining will belong to the test set. Thus, considering the set C = {c1 , . . . , cn }, the
training set will be C1 = {c1 , . . . , ck } and the test set C2 = {ck+1 , . . . , cn }, for k < n.
The general procedure applied to a (transformed and divided) dataset C, consists on estimating the market’s probabilities for each of the models (Markov chains, SARIMA and
GARCH), thus obtaining three "pairs" of probabilities, then we will use them to determine
the speculator’s optimal strategy, also obtaining three optimal strategies. Afterwards, we
will use the test set to check if the obtained strategies were accurate predictions for the
current training set.
To accomplish this, consider the speculator’s More Risk strategy thresholds (as we did in
the previous section) in terms of the dataset’s standard deviation α:

1112

•
•

the Profit Objective threshold: s P = 3α;
the More Risk threshold: s R = −3α.

1113
1114
1115
1116
1117
1118
1119
1120
1121
1122
1123
1124
1125
1126
1127
1128
1129
1130
1131
1132
1133
1134

Then, using the test set, we will check which of the thresholds was reached first. So,
this information together with the chosen optimal strategies, gives us the accuracy of the
predictions, specifically:

1135

•

1138

considering that optimal chosen strategy was the More Risk strategy, then we will
consider that strategy to be accurate if the first threshold to be reached in the test set
was the Profit Objective threshold, otherwise the strategy will be considered to be not
accurate;

1136
1137

1139
1140
1141

Version August 20, 2024 submitted to Journal Not Specified

•

39 of 50

considering that optimal chosen strategy was the Less Risk strategy, then we will
consider that strategy to be accurate if the first threshold to be reached in the test set
was the Profit Objective threshold, otherwise the strategy will be considered to be not
accurate;
considering that optimal chosen strategy was the Do Not Play strategy, then we will
consider that strategy to be accurate if the first threshold to be reached in the test
set was the More Risk threshold, otherwise the strategy will be considered to be not
accurate.

1142

Note that the Less Risk threshold was not necessary to determine the accuracy of the
strategies. Also, due the nature of the data, none of the thresholds may be reached, so, in
this case, we will not consider the strategy to be accurate nor inaccurate. Hence, in this
situation, we can decrease the thresholds and recalculate the optimal strategies, or we can
just consider that the accuracy cannot be determined due to the nature of the data.
Finally, in order to have more samples to analyze, we will increase the training set by
one observation and decrease the test set by one observation, thus obtaining the sets
C1 = {c1 , . . . , ck , ck+1 } and C2 = {ck+2 , . . . , cn }. Then we will redo what we described
before, but considering these new sets as training and test sets, respectively. Thus, we will
obtain new accuracy data for the new optimal strategies.
To summarize, consider the transformed dataset C = {c1 , . . . , cn } split between a training
set C1 = {c1 , . . . , ck } and a test set C2 = {ck+1 , . . . , cn }, then the procedure to be applied is:

1150

•

1.

1146
1147
1148
1149

1151
1152
1153
1154
1155
1156
1157
1158
1159
1160
1161

•

1163

estimate the market’s probabilities using the Markov chains model and determine
the optimal strategy for speculator using the game theoretical model;
estimate the optimal SARIMA model, estimate the market’s probabilities using
the model’s simulations and determine the optimal strategy for the speculator
using the game theoretical model;
estimate the optimal GARCH model, estimate the market’s probabilities using
the model’s simulations and determine the optimal strategy for the speculator
using the game theoretical model.

1164
1165
1166
1167
1168
1169
1170

Considering the test set C2 :

1171

•

1172

•

4.

1145

1162

•

3.

1144

Considering the training set C1 :

•

2.

1143

check the accuracy of the three obtained optimal strategies, using the previously
described method;
store the accuracy results for each of the models.

Increase the training set C1 by one observation and shorten the test set C2 also by one
observation, thus we will now consider the training set to be C1 = {c1 , . . . , ck , ck+1 }
and the test set to be C2 = {ck+2 , . . . , cn }.
Perform all of the previous steps considering the "new" training and test sets, but end
the procedure when the test set only has one observation remaining.

1173
1174
1175
1176
1177
1178
1179

After applying this procedure, we need to analyze the obtained results, which we will do
next.

1180

3. Results

1182

Now, we can put what was presented into practice with some real-time data from the
financial markets, compare the models’ accuracy results and thus derive some conclusions
from them.
Firstly, we will make our analysis for some controlled datasets, with the objective to check
how the models perform in "well-behaved" scenarios, and then move on to datasets with
daily and intraday data. But, before moving further, let us recall that a model is said to
be accurate if the speculator’s obtained optimal strategies were the correct ones (when
comparing to the test set) after the procedure described in Section 2.4 (from Chapter 2)
ended. Likewise, the model is said to be inaccurate if the speculator’s obtained optimal
strategies were the incorrect ones (when comparing to the test set) after the same procedure
ended. However, if a model’s accuracy could not be determined (at a certain time) then it is

1183

1181

1184
1185
1186
1187
1188
1189
1190
1191
1192
1193

Version August 20, 2024 submitted to Journal Not Specified

40 of 50

said to have null accuracy. Additionally, we will also present (and analyze) the following
characteristics obtained from applying the described procedures:

1194

•

The percentage of times that the several models obtained the same strategies. This was
done in order to check how often different approaches would lead to the same optimal
strategies. Also, we will present these results regarding pairs of models, for instance
we will present the percentage of times that the Markov chains and the SARIMA
models obtained the same strategies.
The average time (in the same units as the corresponding dataset) that it took for
the trade to close (in the test set), after a strategy was given. This average time was
obtained by determining the number necessary iterations for the several test sets to
reach one of the speculator’s thresholds.
The percentage of the speculator’s obtained strategies that were "Play Less Risk", "Play
More Risk" and/or "Do Not Play".
In order to show the potential of investing, we used the obtained strategies and entered
a fictional market with an initial monetary value of $10.000, where we only bought
one item of each financial asset. This was done in order to see the profit that we would
obtain if we entered a financial market and used the speculator’s obtained strategies
(for each of the models) to enter (and then exit) a trade. We will not consider the barrier
options strategy presented in section 2.1.3 because our objective is to evaluate the
accuracy of the model in a statistical way and by considering the value of a portfolio
with $10.000 of simple financial assets.

1196

We won’t use different performance metrics to compare the stocks’ predicted values against
the actual values since our objective is to prioritize metrics directly related to profitability
and trading success, rather than general statistical forecasting accuracy. Other metrics are
valuable for evaluating how close predictions are to actual values, but they don’t always
translate directly to trading profits.
To facilitate the presentation, we will round all of the results up to two decimal cases, but,
if needed to, we will display some results in scientific notation. Thus, the values that will
be presented are approximations of the actual results.

1215

•

•
•

1195

1197
1198
1199
1200
1201
1202
1203
1204
1205
1206
1207
1208
1209
1210
1211
1212
1213
1214

1216
1217
1218
1219
1220
1221
1222
1223

Remark 18. In order to make the text lighter, we will refer to the Markov chains model considering
the one iteration estimator as the MC1 model, and to the Markov chains model considering the
long-run estimator as the MCn model.

1224
1225
1226
1227

Finally, the following sections will be structured in the same manner, that is, a brief explanation of the dataset(s), followed by the presentation of each model’s obtained accuracy
results (and related conclusions), ending with the analysis of some characteristics resultant
from the models’ appliance.

1228

3.1. Controlled Datasets

1232

Since the models tend to behave differently due to extreme events we created the
Controlled Datasets which represent extreme behaviors. Thus, for this section, we will
start by explaining how we constructed each dataset and make an overall analysis of the
obtained results.
The first dataset was constructed with the purpose to check how the models perform in a
"mild" Major Adversity scenario, i.e., the price of the asset will not always be decreasing
but its trend will. And to obtain such a dataset we followed the presented steps until we
obtained 1000 observations:

1233

1.
2.
3.
4.
5.

1241

defined the first value of the dataset as 1000;
the second value of the dataset is just an increase of 3% of the previous one;
the third value of the dataset is a decrease of 9% of the previous one;
the even observations are obtained with an increase of 3% of the previous value;
the odd observations are obtained with a decrease of 9% of the previous value.

1229
1230
1231

1234
1235
1236
1237
1238
1239
1240

1242
1243
1244
1245

Version August 20, 2024 submitted to Journal Not Specified

41 of 50

We constructed the dataset in this manner in order to mimic an event of Major Adversity, so
for the models to "perform well" in this dataset, the speculator’s obtained optimal strategy
must always be "Do Not Play", because the market, ultimately, is choosing to decrease the
asset’s price in the long-run.
The second dataset was constructed with the purpose to check how the models perform in
an "extreme" Major Adversity scenario, i.e., the price of the asset will always be decreasing.
To obtain such a dataset, we just defined it as 1000 observations starting from 1000, always
decreasing by 3% of the previous value and adding a random value from a standard normal
distribution. We constructed the dataset in this manner in order to mimic an extreme event
of Major Adversity. So, for the models to "perform well" in this dataset, the speculator’s
obtained optimal strategy must always be "Do Not Play", because the market will always
choose the Major Adversity strategy.
The third dataset was constructed with the purpose to check how the models perform in
a "mild" Zero Adversity scenario, i.e., the price of the asset will not always be increasing
but its trend will. And to obtain such a dataset we followed the presented steps until we
obtained 1000 observations:

1246

1.
2.
3.
4.
5.

defined the first value of the dataset as 1000;
the second value of the dataset is just an decrease of 3% of the previous one;
the third value of the dataset is a increase of 9% of the previous one;
the even observations are obtained with a decrease of 3% of the previous value;
the odd observations are obtained with an increase of 9% of the previous value.

1262

We constructed the dataset in this manner in order to mimic an event of Zero Adversity, so
for the models to "perform well" in this dataset, the speculator’s obtained optimal strategy
must either be "Play Less Risk" or "Play More Risk", because the market, ultimately, is
choosing to increase the asset’s price in the long-run.

1267

1247
1248
1249
1250
1251
1252
1253
1254
1255
1256
1257
1258
1259
1260
1261

1263
1264
1265
1266

1268
1269
1270
1271

The last dataset was constructed with the purpose to check how the models perform
in an "extreme" Zero Adversity scenario, i.e., the price of the asset will always be increasing.
To obtain such a dataset, we just defined it as 1000 observations starting from 1000, always
increasing by 3% of the previous value and adding a random value from a standard normal
distribution. We constructed the dataset in this manner in order to mimic an extreme event
of Zero Adversity. So, for the models to "perform well" in this dataset, the speculator’s
obtained optimal strategy must always be "Play Less Risk" (or even "Play More Risk"),
because the market will always choose the Zero Adversity strategy.

1272
1273
1274
1275
1276
1277
1278
1279
1280

Now that we have explained how each dataset was constructed, we will make a global
analysis of the obtained results for the controlled datasets (considering that 20% of the data
belongs to the test set), obtaining:
•
•

•

The highest standard deviation of the transformed datasets was α ≈ 3 (obtained in
Datasets 1 and 3) and the lowest was α ≈ 0 (in Dataset 2).
The MC1 model was 75% more accurate then the other models, i.e., on 3 datasets
this model had higher (or equal) accuracy results than all the other models. Also, the
highest accuracy result was 100% (obtained in Datasets 2 and 4), while the lowest was
0% (on Dataset 1).
The MCn, SARIMA and GARCH models were 100% more accurate then the other
models. Additionally, the highest accuracy result was 100% (obtained in Datasets 2
and 4), while the lowest was 98.5% (on Dataset 3).

From these results we can see that the MCn, SARIMA and GARCH models are the models
with the best accuracy results, which means that if the speculator used these models (for
these datasets), he/she would obtain more strategies that would result in a profit (or at
least a smaller loss). Consequently, the MC1 model obtained the worst accuracy results.
Also we need to note that the lowest accuracy results were always obtained in the same
datasets, while the highest was almost always in the same one.

1281
1282
1283
1284
1285
1286
1287
1288
1289
1290
1291
1292
1293
1294
1295
1296
1297
1298

Version August 20, 2024 submitted to Journal Not Specified

42 of 50

Finally, 50% of the datasets presented no null accuracy results for all the models, meaning
that the thresholds were always reached in all of the test sets. In Dataset 1, 0.5% of the
models resulted in null accuracy results, which was the same for all the models. While this
percentage was 1.5% for Dataset 3.
Moving to the obtained characteristics (which resulted from the explained procedures) for
these controlled datasets were:

1299

•

1305

The percentage of times that the several models obtained the same strategies:

1303
1304

The average time (in iterations) for all of the datasets was the same across all of the
models. Also, the highest average time was 3.475 iterations (in Dataset 3) and the
lowest was 1 iteration (on Datasets 2 and 4).
The percentage of the speculator’s obtained strategies for each of the models was:

1310

1307
1308
1309

1311
1312
1313

–

For the MC1 model:

1314
1315

–

in 50% of the datasets always chose the More Risk strategy;
*
in 25% of the datasets always chose the Less Risk strategy;
*
in 25% of the datasets always chose the Not Play strategy.
*
For the MCn, SARIMA and GARCH models:
*
*

•

1302

1306

–

•

1301

The MCn model fully coincided in all the datasets with the time series models,
i.e., in all the dataset these models always resulted in the same strategies
The MC1 model fully coincided in 50% of the datasets with all the other models,
but on the other hand, it never coincided with any model in the other datasets.

–

•

1300

in 50% of the datasets always chose the Less Risk strategy;
in 50% of the datasets always chose the Not Play strategy.

The obtained possible profits using each model were:
–

For the MC1 model:
*

–

negative in 25% of the datasets, null in 25% and positive in the remaining
ones;
the lowest profit (or highest loss) was in Dataset 1;
the highest profit was in Dataset 3.

*
*
For the MCn, SARIMA and GARCH models:
*
*
*

null in 50% of the datasets and positive in the remaining datasets;
the lowest profit (or highest loss) was in Datasets 1 and 2;
the highest profit was in Dataset 3.

As it was said before, the MCn, SARIMA and GARCH models fully coincided between
them, in terms of accuracy results and chosen strategies. But, on the other hand, the MC1
model never coincided with all the other models in 50% of the datasets.
The MC1 model in 50% of the datasets always chose the More Risk strategy, and then
switched between all the strategies in the remaining datasets. Meanwhile, the other models
always chose the Less Risk strategy in 50% of the datasets, and then the Not play strategy
on the other datasets.
In terms of possible profits, the MCn, SARIMA and GARCH models obtained positive
profits in 50% of the datasets and null profits on the other ones, while the MC1 model
obtained negative profits in 25% of the datasets, null profits in 25% and the remaining were
positive.
From all of these results, we can see that the MCn, SARIMA and GARCH models obtained
better accuracy and profits results, because they chose the expected optimal strategies for
each of the datasets. While the MC1 model was the worst in all of the same aspects.
Finally, the average time it took the models to reach a threshold always coincided between
models and its range was approximately from 1 to 3 iterations. Also, we need to note that
both the highest and lowest profits were always obtained in the same datasets.

1316
1317
1318
1319
1320
1321
1322
1323
1324
1325
1326
1327
1328
1329
1330
1331
1332
1333
1334
1335
1336
1337
1338
1339
1340
1341
1342
1343
1344
1345
1346
1347
1348

Version August 20, 2024 submitted to Journal Not Specified

43 of 50

3.2. Daily Datasets

1349

For this section, we will analyze datasets which are only composed with daily closing
prices of several financial assets, this means that we are going to analyze the assets’ prices
at the end of each day (specifically, at the closing of the financial market).
We applied our models to 100 different datasets, but we will not analyze each of them,
rather we will make a global analysis of the results. Also, note that whenever we refer to a
specific dataset, we are actually referring to the price data that we obtained for a certain
financial asset. Additionally, all the datasets have exactly 1000 observations of the closing
price at the end of the day.
Thus, after applying our models to these datasets, considering that 20% of the data belongs
to the test set, we obtained that:

1350

•
•

•

•

•

The highest standard deviation of the transformed datasets was α ≈ 3.44 (obtained in
dataset TNXP) and the lowest was α ≈ 0 (in dataset PSON).
The MC1 model was 41% more accurate then the other models, i.e., on 41 datasets
this model had higher (or equal) accuracy results than all the other models. Also, the
highest accuracy result was 66.5% (obtained in dataset AAPL), while the lowest was
33.5% (on dataset TNXP).
The MCn model was 50% more accurate then the other models. And, the highest
accuracy result was 66.5% (obtained in datasets AAPL and TNXP), while the lowest
was 34.5% (on dataset NOS).
The SARIMA model was 42% more accurate then the other models. And, the highest
accuracy result was 66.5% (obtained in dataset AAPL), while the lowest was 35% (on
dataset GFS).
The GARCH model was 40% more accurate then the other models. And, the highest
accuracy result was 66.5% (obtained in dataset AAPL), while the lowest was 35.5%
(on dataset NOS).

1351
1352
1353
1354
1355
1356
1357
1358
1359
1360
1361
1362
1363
1364
1365
1366
1367
1368
1369
1370
1371
1372
1373
1374

From these results we can see that the MCn model is the one with the best accuracy results,
which means that if the speculator used this model (for these datasets), he/she would
obtain more strategies that would result in a profit (or at least a smaller loss). Additionally,
the MC1, SARIMA and GARCH models obtained very similar accuracy results.
Regarding the time series models, the SARIMA model obtained slightly higher accuracy
results than the GARCH model, which is the opposite of what was expected, since the
GARCH models were specifically developed for this kind of data, as such it would be
expected for them to perform better in terms of accuracy.
Finally, the obtained null accuracy results were the same across all the models and were
almost always zero, also the highest percentage of null models was 6% (obtained in dataset
TWTR). Additionally, we need to note that the highest accuracy results were always
obtained in the same dataset.
The obtained characteristics (which resulted from the explained procedures) for these
datasets were:

1375

•

1389

The percentage of times that the several models obtained the same strategies:
–

–
–

–

The Markov chains models fully coincided between them in 81% of the datasets,
i.e., in 81 datasets these two models always resulted in the same strategies. Also
they never coincided in 5% of the datasets and, on the other datasets, the percentage of coinciding models ranged from 2% to 99%.
The MC1 model never coincided (in all the datasets) with the time series models.
The MCn model never coincided in 81% of the datasets with the SARIMA model
and, on the other datasets, the percentage of coinciding models ranged from 1%
to 98%.
The MCn model never coincided in 82% of the datasets with the GARCH model
and, on the other datasets, the percentage of coinciding models ranged from 0.5%
to 98.5%.

1376
1377
1378
1379
1380
1381
1382
1383
1384
1385
1386
1387
1388

1390
1391
1392
1393
1394
1395
1396
1397
1398
1399
1400

Version August 20, 2024 submitted to Journal Not Specified

The SARIMA model fully coincided with the GARCH model in 6% of the datasets
and, on the other datasets, the percentage of coinciding models ranged from
51.5% to 99.5%.

1401

The average time (in days) for all the datasets was the same across all the models.
Also, the highest average time was 9.35 days (in dataset GFS) and the lowest was 1.015
days (on dataset PSON).
The percentage of the speculator’s obtained strategies for each of the models was:

1404

The MC1 model always chose to play the More Risk strategy on all of the datasets.
For the MCn model:

1408

in 81% of the datasets always chose the More Risk strategy;
in 1% of the datasets always chose the Less Risk strategy;
in 4% of the datasets always chose the Not Play strategy;
in 1% of the datasets chose between the play More Risk and Less Risk strategies;
in 13% of the datasets only chose between the More Risk and Not Play
strategies.

1410

–

•

•

–
–

*
*
*
*
*
–

For the SARIMA model:
*
*
*

–

in 5% of the datasets always chose the Less Risk strategy;
in none of the datasets always chose the More Risk and Not Play strategies;
in the remaining datasets only chose between the Less Risk and Not Play
strategies. Also, the percentage of times the Less Risk strategy was chosen
(instead of the Not Play strategy) is less than 50% in only 3% of all the
datasets.

For the GARCH model:
*
*
*

•

44 of 50

in 26% of the datasets always chose the Less Risk strategy;
in none of the datasets always chose the More Risk and Not Play strategies;
in the remaining datasets only chose between the Less Risk and Not Play
strategies. Also, the percentage of times the Less Risk strategy was chosen
(instead of the Not Play strategy) is less than 50% in only 1% of all the
datasets.

The obtained possible profits using each model were:

1402
1403

1405
1406
1407

1409

1411
1412
1413
1414
1415
1416
1417
1418
1419
1420
1421
1422
1423
1424
1425
1426
1427
1428
1429
1430
1431

–

For the MC1 model:

1432
1433

–

negative in 18% of the datasets and positive in the remaining datasets;
*
the lowest profit (or highest loss) was in dataset CCL;
*
the highest profit was in dataset AZN.
*
For the MCn model:
*

negative in 16% of the datasets, null in 4% of the datasets and positive in the
remaining datasets;
the lowest profit (or highest loss) was in dataset CCL;
the highest profit was in dataset AZN.

1434
1435
1436
1437
1438
1439

–

*
*
For the SARIMA model:

1442

–

negative in 25% of the datasets and positive in the remaining datasets;
*
the lowest profit (or highest loss) was in dataset CCL;
*
the highest profit was in dataset AVV.
*
For the GARCH model:
negative in 19% of the datasets and positive in the remaining datasets;
the lowest profit (or highest loss) was in dataset CCL;
the highest profit was in dataset AZN.

1446

*
*
*

From the first item we can see that no model fully coincided in terms of chosen strategies
with another one, but, on the other hand, the MC1 model never coincided with the time

1440
1441

1443
1444
1445

1447
1448
1449
1450

Version August 20, 2024 submitted to Journal Not Specified

45 of 50

series models (SARIMA and GARCH), similarly the MCn model almost never coincided
with the time series models. Also, the Markov chains models almost always coincided
between them. Regarding the time series models, they almost always coincided between
them, even though they only fully coincided in 6% of the datasets.
The MC1 model always chose the More Risk strategy across all of the datasets, while this
only happened in 81% of the datasets for the MCn model. But, unlike the Markov chains
models, the time series models never chose the More Risk strategy.
From all of these results, we can see that the MCn model performed better both in terms of
accuracy results and of possible profits. Meanwhile, the MC1 model performed similarly
to the time series models, both in terms of accuracy results and of possible profits. Also,
regarding the time series models, the SARIMA model had slightly higher accuracy results
than the GARCH model, however it had the highest percentage of unprofitable datasets.
Finally, the average time it took the models to reach a threshold always coincided between
models and its range was from approximately a day to two weeks (each week in the financial markets is composed by five days). Also, we need to note that the lowest profit was
always obtained in the same dataset, while the highest one was almost always obtained in
the same one.

1451
1452
1453
1454
1455
1456
1457
1458
1459
1460
1461
1462
1463
1464
1465
1466
1467
1468

3.3. Intraday Datasets

1469

For this section, we will analyze datasets which are only composed with 1000 observations of intraday closing prices of several financial assets, this means that we are going to
analyze the assets’ prices at the end of each minute for several days. Also, we applied our
models to 100 different datasets, but we will not analyze each of them, rather we will make
a global analysis of the results. Also, note that whenever we refer to a specific dataset, we
are actually referring to the price data that we obtained for a certain financial asset.
Thus, after applying our models to these datasets, considering that 20% of the data belongs
to the test set, we obtained that:

1470

•

•

•

•

•

The highest standard deviation of the transformed datasets was α ≈ 2.13 (obtained in
dataset TNXP), also this value was the only value for the standard deviation greater
than 1. Furthermore, all the other values for the standard deviation were smaller than
0.4, where the lowest was α ≈ 0 (in dataset Z).
The MC1 was 27% more accurate then the other models, i.e., on 27 datasets this model
had higher (or equal) accuracy results than all the other models. Also, the highest
accuracy result was 68.5% (obtained in dataset NOS), while the lowest was 0.5% (on
dataset TWTR).
The MCn model was 43% more accurate then the other models. And, the highest
accuracy result was 78.5% (obtained in dataset FCX), while the lowest was 0.5% (on
dataset TWTR).
The SARIMA model was 43% more accurate then the other models. And, the highest
accuracy result was 74% (obtained in dataset BCP), while the lowest was 2.5% (on
dataset TWTR).
The GARCH model was 33% more accurate then the other models. And, the highest
accuracy result was 67.5% (obtained in dataset O), while the lowest was 14% (on
dataset TWTR).

From these results we can see that the MCn and SARIMA models were the ones with the
best accuracy results, which means that if the speculator used one of these models (for
these datasets), he/she would obtain more strategies that would result in a profit (or at
least a smaller loss). Meanwhile, the MC1 model was the one with the lowest accuracy
results.
Regarding the time series models, the SARIMA model obtained higher accuracy results
than the GARCH model, which is the opposite of what was expected, since the GARCH
models were specifically developed for this kind of data.
Finally, the obtained null accuracy results were the same across all the models and were

1471
1472
1473
1474
1475
1476
1477
1478
1479
1480
1481
1482
1483
1484
1485
1486
1487
1488
1489
1490
1491
1492
1493
1494
1495
1496
1497
1498
1499
1500
1501
1502
1503

Version August 20, 2024 submitted to Journal Not Specified

46 of 50

almost always zero, where the highest percentage of null models was 12.5% (obtained
in dataset TWTR). Also, we need to note that the smallest accuracy results were always
obtained in the same dataset.
The obtained characteristics (which resulted from the explained procedures) for these
controlled datasets were:

1504

•

1509

The percentage of times that the several models obtained the same strategies:

1508

The average time (in minutes) for all the datasets was the same across all the models.
And, the highest average time was 52.56 minutes (in dataset TWTR), while the lowest
was 1.035 minutes (on dataset Z).
The percentage of the speculator’s obtained strategies for each of the models was:

1524

The MC1 model always chose to play the More Risk strategy on all of the datasets.
For the MCn model:

1528

in 61% of the datasets always chose the More Risk strategy;
in 1% of the datasets always chose the Less Risk strategy;
in 16% of the datasets always chose the Not Play strategy;
in 22% of the datasets only chose between the More Risk and Not Play
strategies.

1530

–

–

–
–

*
*
*
*
–

For the SARIMA model:
*
*
*

–

in 5% of the datasets always chose the Less Risk strategy;
in none of the datasets always chose the More Risk and Not Play strategies;
in the remaining datasets only chose between the Less Risk and Not Play
strategies. Also, the percentage of times the Less Risk strategy was chosen
(instead of the Not Play strategy) is less than 50% in only 7% of all the
datasets.

For the GARCH model:
*
*
*

•

1507

1510

–
–

•

1506

The Markov chains models fully coincided between them in 61% of the datasets,
i.e., in 61 datasets these two models always resulted in the same strategies. Also,
they never coincided in 17% of the datasets and, on the other datasets, the percentage of coinciding models ranged from 1% to 98.5%.
The MC1 model never coincided in all the datasets with the time series models.
The MCn model fully coincided with the SARIMA model in 1% of the datasets,
never coincided in 67% of the datasets and, on the other datasets, the percentage
of coinciding models ranged from 1% to 87.5%.
The MCn model never coincided with the GARCH model in 76% of the datasets
and, on the other datasets, the percentage of coinciding models ranged from 0.5%
to 95.5%.
The SARIMA model fully coincided with the GARCH model in 4% of the datasets
and, on the other datasets, the percentage of coinciding models ranged from
12.5% to 99.5%.

–

•

1505

in 27% of the datasets always chose the Less Risk strategy;
in none of the datasets always chose the More Risk;
in the remaining datasets, only chose between the Less Risk and Not Play
strategies. Also, the percentage of times the Less Risk strategy was chosen
(instead of the Not Play strategy) is less than 50% in only 3% of all the
datasets.

The obtained profits using each model were:

1511
1512
1513
1514
1515
1516
1517
1518
1519
1520
1521
1522
1523

1525
1526
1527

1529

1531
1532
1533
1534
1535
1536
1537
1538
1539
1540
1541
1542
1543
1544
1545
1546
1547
1548
1549

–

For the MC1 model:

1550
1551

–

negative in 41% of the datasets and positive in the remaining datasets;
*
the lowest profit (or highest loss) was in dataset RB;
*
the highest profit was in dataset AZN.
*
For the MCn model:

1552
1553
1554

Version August 20, 2024 submitted to Journal Not Specified

*

47 of 50

negative in 37% of the datasets, null in 16% and positive in the remaining
datasets;
the lowest profit (or highest loss) was in dataset RB;
the highest profit was in dataset AHT.

1555
1556
1557

–

*
*
For the SARIMA model:

1560

–

negative in 40% of the datasets and positive in the remaining datasets;
*
the lowest profit (or highest loss) was in dataset RB;
*
the highest profit was in dataset AZN.
*
For the GARCH model:

negative in 43% of the datasets and positive in the remaining datasets;
*
the lowest profit (or highest loss) was in dataset RB;
*
the highest profit was in dataset AZN.
*
From the first item we can see that no model fully coincided in terms of chosen strategies
with another one, but the MC1 model never coincided with the time series models (SARIMA
and GARCH), and the MCn model almost never coincided with the time series models.
Also, the Markov chains models almost always coincided between them. Similarly, the
time series models almost always coincided between them, even though they only fully
coincided in 4% of the datasets.
The MC1 model always chose the More Risk strategy across all the datasets, while this only
happened in 61% of the datasets for the MCn model. But, unlike the Markov chains models,
the time series models never chose the More Risk strategy.
The average time it took the models to reach a threshold always coincided between models
and its range was from approximately 1 to 53 minutes. Also, the lowest profit was always
obtained in the same dataset, while the highest was almost always obtained in the same
one.
Finally, from all of these results, we can see that the MCn and SARIMA models were the
ones with the best accuracy results, however, the MCn model had the lowest percentage of
unprofitable datasets and was a model which resulted in all kinds of strategies. Additionally,
regarding the time series models, the SARIMA model had better accuracy and profit results
than the GARCH model.

1558
1559

1561
1562
1563
1564
1565
1566
1567
1568
1569
1570
1571
1572
1573
1574
1575
1576
1577
1578
1579
1580
1581
1582
1583
1584

4. Conclusions

1585

Now that we have all the results for all the datasets, we can make a summary of what
we obtained and then withdraw some conclusions from it.
Firstly, from all the obtained results, we can note that the lowest standard deviation of the
transformed datasets was α ≈ 0, while the highest was α ≈ 3. Also, we need to note that,
in the Intraday datasets, 99% of the transformed datasets had a standard deviation lower
than 0.4.
Regarding the obtained accuracy results for the models, we can see that the MCn model
obtained the best accuracy results for each type of datasets (Controlled, Daily and Intraday),
but on the Controlled datasets it tied with the time series models, while this happened with
the SARIMA model in the Intraday datasets. About the maximum and minimum accuracy
results, we obtained that:

1586

•

for the Controlled datasets, the lowest accuracy result was almost always obtained in
the same dataset, while the highest was always obtained in the same one;
for the Daily datasets, only the highest accuracy result was always obtained in the
same dataset;
for the Intraday datasets, only the lowest accuracy result was always obtained in the
same dataset.

1597

Additionally, in all of the datasets both the null accuracy results and the average closing
times were the same across the models. However, we need to note that, in terms of
maximum results, the intraday datasets resulted in higher null results and higher average

1603

•
•

1587
1588
1589
1590
1591
1592
1593
1594
1595
1596

1598
1599
1600
1601
1602

1604
1605

Version August 20, 2024 submitted to Journal Not Specified

48 of 50

closing times.
For the percentage of equal strategies across the models we obtained that:

1606

•

For the controlled datasets, the MCn model always coincided with the time series
models. Meanwhile, the MC1 model fully coincided with the other models in 50% of
the datasets, whilst it never coincided in the other datasets.
For both the daily and intraday datasets, the Markov chains models almost always
coincided between them. But the MC1 model never coincided with the time series
models, and, consequently, the MCn model almost never coincided with the time series
models. Regarding the time series models, they almost always had a high percentage
of coinciding strategies between them, but they almost never fully coincided between
them.

1608

Now, regarding the percentage of chosen strategies for each of the models we obtained
that:

1617

•

For the controlled datasets, the MC1 model almost always chose the More Risk strategy
(sometimes switching to the other strategies), while the other models chose between
the Less Risk and Not Play strategies.
For both the daily and intraday datasets: the MC1 model always chose the More Risk
strategy; the MCn model almost always chose the More Risk strategy, but it also chose
between the other strategies; the time series models chose between the Less Risk and
Not Play strategies.

1619

Regarding the obtained possible profits resulting from applying the different models we
can see that the MCn model obtained the least percentage of unprofitable datasets for each
type of datasets, but on the Controlled datasets it tied with the time series models, on the
other hand, the MC1 model obtained the highest percentage of strictly positive profits in
the Daily datasets, while the same happened for the Intraday datasets with the SARIMA
model. About the maximum and minimum obtained possible profits, we have that:

1626

•

for the Controlled datasets, the lowest and highest possible profits were always
obtained in the same datasets;
for both the Daily and Intraday datasets, the lowest possible profit was always obtained in the same dataset (CCL and RB, respectively) and the highest was almost
always obtained in the same one (AZN for both types).

1632

Thus, gathering all these results, we can see that the Markov chains model (considering
the long-run estimator) behaved better both in terms of accuracy and possible profits, than
the other models, additionally, this model resulted in all kinds of strategies, unlike all the
other models. So, with the Markov chains model (considering the long-run estimator), we
obtained better results than all the other presented models.
Finally, the game theoretical model that we used as the decision model to make predictions
(and to buy and sell financial assets) is a useful and accurate tool (both for the Markov
chains models and the time series models), because it gives us an optimal strategy chosen
in terms of these market probabilities, also these strategies are the same as the ones commonly used by the markets’ investors (and speculators). So, instead of directly predicting a
financial asset’s price (and then acting upon this predictions), we can obtain a probabilistic
model that lets us see how the financial markets behaved and where they may be going in
terms of the assets’ prices.

1637

•

•

•

1607

1609
1610
1611
1612
1613
1614
1615
1616

1618

1620
1621
1622
1623
1624
1625

1627
1628
1629
1630
1631

1633
1634
1635
1636

1638
1639
1640
1641
1642
1643
1644
1645
1646
1647
1648
1649
1650

4.1. Future Work

1651

From the presented theory and subsequently results, a number of possible extensions
can be made, such as:

1652

•

1654

•

create a new decision model that incorporates both the Markov chains and time series
models;
add more classes to the Markov chains model, add more strategies to the game
theoretical model and/or alter the existing classes/strategies;

1653

1655
1656
1657

Version August 20, 2024 submitted to Journal Not Specified

•
•

49 of 50

study on how these models can be adapted to all kinds of data;
incorporate data regarding news sentiment, social media trends, and economic indicators to improve the model’s accuracy, since this would allow for a more dynamic and
responsive approach to stock market prediction;
develop a model for extreme events when the time series change directions, such as
the Great Recession or the 2008 financial crisis;
consider bigger forecasting horizons in order to make long-term predictions;
consider other models instead of the Markov chains to predict the game’s probabilities
such as VAR, ECM, Kalman Filter, Decision Trees based models, Neural Networks.

1658

Also, we can study the possible relationships between the volatility, type and/or length of
the datasets to:

1667

•
•
•

the obtained optimal model (both in terms of accuracy and possible profit results);
the obtained values for the accuracy and possible profit results;
the standard deviations, the average closing time and the percentage of null models.

1669

All of this should be studied in order to better model that predicts the financial markets so
as to increase the potential profits, and then extend to all kinds of data.

1672

Funding: This work is financed by: National Funds through the Portuguese funding agency, FCT
- Fundação para a Ciência e a Tecnologia, within project LA/P/0063/2020; CMUP - Centro de
Matemática da Universidade do Porto.

1674

Institutional Review Board Statement: Not applicable.

1677

Informed Consent Statement: Not applicable.

1678

Data Availability Statement: The data presented in this study are openly available in https://www.
kaggle.com/jfcf0802/daily-and-intraday-stock-data.

1679

Conflicts of Interest: The authors declare no conflict of interest.

1681

•
•
•

1659
1660
1661
1662
1663
1664
1665
1666

1668

1670
1671

1673

1675
1676

1680

References

1682

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

1683

22.
23.
24.
25.
26.
27.

Yahoo Finance. [Online; accessed 23-January-2020].
AlphaVantage. [Online; accessed 14-February-2020].
Freitas, J. KAGGLE Dataset - Daily and Intraday Stock Data. [Online; accessed 4-May-2020].
McDonald, J.B. Probability Distributions for Financial Models. Handbook of Statistics 1996, 14, 427–461.
Jackwerth, J.C.; Rubinstein, M. Recovering Probability Distributions from Option Prices. The Journal of Finance 1996, 51, 1661.
Errunza, V.R.; Losq, E. The Behavior of Stock Prices on LDC Markets. Journal of Banking and Finance 1985, 9, 561–575.
Mandelbrot, B.; Taylor, H.M. On the Distribution of Stock Price Differences. Operations Research 1967, 15, 1057–1062.
Pishro-Nik, H. Introduction to Probability, Statistics, and Random Processes; Kappa Research, 2014.
Stewart, J. Calculus, 8 ed.; Cengage Learning, 2016.
McMillan, L.G. Options as a Strategic Investment, 4 ed.; Prentice Hall Press, 2001.
Murphy, J.E. Stock Market Probability: How to Improve the Odds of Making Better Investment Decisions; Probus Publishing, 1988.
Box, G.; Jenkins, G. Time Series Analysis, Forecasting and Control; Holden-Day, 1970.
Hipel, K.; McLeod, A. Time Series Modelling of Water Resources and Environmental Systems; Elsevier, 1994.
Gottlieb, G.; Kalay, A. Implications of the Discreteness of Observed Stock Prices. The Journal of Finance 1965, 11, 135–153.
Scott, J.; Stumpp, M.; Xu, P. Overconfidence Bias in International Stock Prices. The Journal of Portfolio Management 2003, pp. 80–89.
Royal, J.; Arielle, O. What is the Average Stock Market Return?, 2020. [Online; accessed 24-April-2020].
Cournot, A. Researches into the Mathematical Principles of the Theory of Wealth; 1897.
Nash, J. Equilibrium Points in n-Person Games. Proceedings of the National Academy of Sciences 1950, 36, 48–49.
Wald, A. Statistical Decision Functions; John Wiley & Sons, 1950.
Luce, R.D.; Raiffa, H. Games and Decisions; John Wiley & Sons, 1957.
Harsanyi, J. Games with Randomly Distributed Payoffs: A New Rationale for Mixed Strategy Equilibrium Points. International
Journal of Game Theory 1973, 2, 1–23.
Aumann, R. Subjectivity and Correlation in Randomized Strategies. Journal of Mathematical Economics 1974, 1, 67–96.
Aumann, R. Agreeing to Disagree. Annals of Statistics 1976, 4, 1236–1239.
Farber, H. An Analysis of Final-Offer Arbitration. Journal of Conflict Resolution 1980, 35, 683–705.
Bertrand, J. Théorie Mathématique de la Richesse Sociale. Journal des Savants 1883, pp. 499–508.
Pearce, D. Rationalize Strategic Behavior and the Problem of Perfection. Econometrica 1984, 52, 1029–50.
Szép, J.; Forgó, F. Introduction to the Theory of Games; D. Reidel Publishing Company, 1985.

1684
1685
1686
1687
1688
1689
1690
1691
1692
1693
1694
1695
1696
1697
1698
1699
1700
1701
1702
1703
1704
1705
1706
1707
1708
1709
1710

Version August 20, 2024 submitted to Journal Not Specified

28.
29.
30.
31.
32.
33.
34.
35.
36.
37.
38.
39.
40.
41.
42.
43.
44.
45.
46.
47.
48.
49.
50.
51.
52.
53.

50 of 50

Fudenberg, D.; Tirole, J. Game Theory; The MIT Press, 1991.
Gibbons, R. A Primer in Game Theory; Pearson Education, 1992.
Biswas, T. Decision-Making Under Uncertainty; MAcMillan Press Ltd, 1997.
Shelton, R.B. Gaming the Market; Wiley Trading Advantage, John Wiley & Sons, 1997.
Kemeny, J.; Shell, J. Finite Markov Chains; Van Nostrand Company, 1960.
Bowerman, B.L. Nonstationary Markov decision processes and related topics in nonstationary Markov chains. Retrospective
theses and dissertations. 6327, Iowa State University, Iowa, USA, 1974.
Fismen, M. Exact Simulation Using Markov Chains. Diploma-thesis (master-thesis) in statistics, Department of Mathematical
Sciences, The Norwegian University of Science and Technology, Trondheim, Norway, 1997.
Welton, N.; Ades, A. Estimation of Markov Chain Transition Probabilities and Rates from Fully and Partially Observed Data:
Uncertainty Propagation, Evidence Synthesis, and Model Calibration. MRC Health Services Research Collaboration 2005.
Fette, B. Cognitive Radio Technology, 2 ed.; Academic Press, 2009.
Stewart, W.J. Probability, Markov chains, queues and simulation, 1 ed.; Princeton University Press, 2009.
Himmelmann, S.; www.linhi.com. HMM: HMM - Hidden Markov Models. R package version 1.0 2010.
Jackson, C.H. Multi-State Models for Panel Data: The msm Package for R. Journal of Statistical Software 2011, 38, 1–29.
Wreede, L.; Fiocco, M.; Putter, H. mstate: An R Package for the Analysis of Competing Risks and Multi-State Models. Journal of
Statistical Software 2011, 38, 1–30.
Kobayashi, H.; Mark, B.L.; Turin, W. Probability, Random Processes and Statistical Analysis; Cambridge University Press, 2012.
Geyer, C.J.; Johnson, L..T. mcmc: Markov Chain Monte Carlo. R package version 0.9-2 2013.
Spedicato, G.A.; Kang, T.S.; Yalamanchi, S.B.; Yadav, D.; Cordón, I. The markovchain Package: A Package for Easily Handling
Discrete Markov Chains in R. The R Journal 2017.
Box, G.; Jenkins, G. Time Series Analysis, Forecasting and Control; Holden-Day, 1976.
Engle, R.F. Autoregressive conditional heteroscedasticity with estimates of the variance of United Kingdom inflation. Econometrica
1982, 50, 987–1007.
Bollerslev, T. Generalized autoregressive conditional heteroscedasticity. J. Econ. 1986, 31, 307–327.
Hamilton, J.D. Time Series Analysis; Princeton University Press, 1994.
Box, G.; G.Jenkins.; Reinsel, G. Time Series Analysis, Forecasting and Control; Wiley, 2008.
Hyndman, R.; Khandakar, Y. Automatic time series forecasting: The forecast package for R. Journal of Statistical Software 2008,
27, 1–22.
Shumway, R.H.; Stoffer, D.S. Time Series Analysis and Its Applications, 3 ed.; Springer Texts in Statistics, Springer, 2011.
Brockwell, P.; Davis, R. Introduction to Time Series and Forecasting, 3 ed.; Springer Texts in Statistics, Springer, 2016.
Wilmott, P.; Howison, S.; Dewynne, J. The Mathematics of Financial Derivatives: A Student Introduction; Cambridge University Press,
1995.
Stuart, A.; Ord, K. Kendall’s Advanced Theory of Statistics: Volume I – Distribution Theory; Edward Arnold, 1994.

1711
1712
1713
1714
1715
1716
1717
1718
1719
1720
1721
1722
1723
1724
1725
1726
1727
1728
1729
1730
1731
1732
1733
1734
1735
1736
1737
1738
1739
1740
1741
1742
1743
1744

