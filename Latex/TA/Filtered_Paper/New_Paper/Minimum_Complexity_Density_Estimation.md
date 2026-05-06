1034

IEEE

TRANSACTIONS

ON INFORMATION

THEORY,

VOL.

37, NO. 4, JULY

1991

Minimum Complexity Density Estimation
Andrew R. Barron, Member, IEEE and Thomas M. Cover, Fellow, IEEE

Abstract -The
minimum
complexity or minimum
description-length
criterion
developed by Kolmogorov,
Rissanen,
Wallace, So&in, and others leads to consistent probability density estimators. These density estimators are defined to achieve
the best compromise between likelihood and simplicity. A related issue is the compromise between accuracy of approximations and complexity relative to the sample size. An index of
resolvability is studied which is shown to bound the statistical
accuracy of the density estimators, as well as the informationtheoretic redundancy.
Index Terms -Kolmogorov
complexity,
minimum
description-length criterion, universal data compression, bounds on
redundancy, resolvability of functions, model selection, density
estimation, discovery of probability laws, consistency, statistical
convergence rates.

by the choice of a description length for each of these
distributions, subject to information-theoretic requirements. An idealized form of the minimum complexity
criterion is obtained when Kolmogorov’s theory of complexity is used to assessthe description length of probability laws; however, our results are not restricted to this
idealistic framework.
For independent random variables X,, X,, * * *, X,,
drawn from an unknown probability density function p,
the minimum complexity density estimator 6, is defined
as a density achieving the following minimization

min L(q)+log
4
1

II
irpi)

1
(l-1)
I’

I. INTRODUCTION
HE KOLMOGOROV
theory of complexity
(Kolmogorov [l]) leads to the notion of a universal where the minimization is over a list I of candidate
minimal sufficient statistic for the optimal compression of probability density functions 9, and the logarithm is base
data as discussed in V’Yugin [2], Cover [3], [4], and Cover, 2. As discussed in Section III, this criterion corresponds
Gacs, and Gray [5]. The Kolmogorov theory is applicable to the minimization of the total length of a two-stage
to arbitrary, possibly nonrandom, data sequences.Related description of the data. The nonnegative numbers L(q)
notions of complexity or description length, that are are assumed to satisfy Kraft’s inequality Cq2PL(q)I 1 and
specifically appropriate for making inferences from ran- are interpreted to be codelengths for the descriptions of
dom data, arise in the work of Rissanen [6]-[ll], Wallace the densities. Although not needed for the informationet al. [12], [13], Sorkin [14], Barron [15]-[17], Cover [31, [4], theoretic interpretation, there is also a Bayesian interpre[18], and V’Yugin [2] and in the context of universal tation of the numbers 2--L(q)as prior probabilities. In the
source coding as in Davisson [19]. The goal shared by Kolmogorov complexity framework, L(q) is equal to the
these complexity-based principles of inference is to obtain length of the shortest computer code for q as explained in
accurate and parsimonious estimates of the probability Section IV, and the best data compression and the best
distribution. The idea is to estimate the simplest density bounds on rates of convergence are obtained in this case.
The list I of candidate probability densities is often
that has high likelihood by minimizing the total length of
specified
from a given sequence of parametric models of
the description of the data. The estimated density should
dimension
d = 1,2; . ., with the parameter values resummarize the data in the sense that, given the minimal
stricted
to
a prescribed number of bits accuracy. The
description of the estimated density, the remaining deminimum
complexity
criterion is then used to select the
scription length should be close to the length of the best
model
and
to
estimate
the parameters. Larger lists I
description that could be achieved if the true density were
provide
better
flexibility
to
discover accurate yet parsimoknown.
nious
models
in
the
absence
of true knowledge of the
Minimum complexity estimators are treated in a gencorrect
parametric
family.
In
the
idealistic case, I consists
eral form that can be specialized to various cases by the
of
all
computable
probability
distributions.
choice of a set of candidate probability distributions and
The minimum complexity criterion can discover the
true distribution. Indeed, it is shown that if the true
Manuscript received February 3, 1989; revised January 25, 1991. A. R.
distribution happens to be on the countable list I, then
Barron’s work was supported by ONR Contracts N00014-86-K-0670 and
the estimator is exactly correct,
N00014-89-J-1811. T. M. Cover’s work was supported in part by the

T

National Science Foundation under Contract NCR-89-14538.
A. R. Barron is with the Department of Statistics and the Department
of Electrical and Computer Engineering, University of Illinois, 101 Illini
Hall, 725 S. Wright St., Champaign, IL 61820.
T. M. Cover is with Information Systems Laboratory, 121 Durand,
Stanford University, Stanford, CA 94305.
IEEE Log Number 9144768.

6,-p,

(1.2)

for all sufficiently large sample sizes, with probability one
(Theorem 1). Consequently, the probability of error based

0018-9448/91/0700-1034$01.00

01991 IEEE

BARRON

AND

COVER:

MINIMUM

COMPLEXITY

DENSITY

ESTIMATION

on n samples tends to zero as y1--)00.The result is most
dramatic in the Kolmogorov complexity framework: if the
data are governed by a computable probability law, then,
with probability one, this law eventually will be discovered
and thereafter never be refuted. Although the law is
eventually discovered, one cannot be certain that the
estimate is exactly correct for any given IZ. You know, but
you do not know you know.
Consistency of the minimum complexity estimator is
shown to hold even if the true density is not on the given
countable list, provided the true density is approximated
by sequences of densities on the list in the relative entropy sense. Theorems 2 and 3, respectively, establish
almost sure consistency of the estimated distribution and
(under somewhat stronger assumptions) L1 consistency of
the estimated density. These results, which were announced in [151, [161, are the first general consistency
results for the minimum description-length principle in a
setting that does not require the true distribution to be a
member of a finite-dimensional parametric family.
The main contribution of this paper is the introduction
of an index of resolvability,
R,(p)

= min
4 ( n +“D’;;,I’lj)

(1.3)

1035

practical. (In contrast, the method of maximum likelihood
density estimation fails without constraints on the class of
densities.) The minimum complexity estimator converges
to the true density nearly as fast as an estimator based on
prior knowledge of the true subclass of densities.
The minimum complexity estimator may also be defined for lists of joint densities q(X,, X,; . .,X,1 that
allow for dependent random variables, instead of independence rI:=,q(X,)
as required in (1.1). Indeed, the
assumption of stationarity and ergodicity is sufficient for
the result on the discovery of the true distribution in the
computable case, as shown in [16]. The assumption of
independence, however, appears to be critical to our
method of obtaining bounds on the rate of convergence of
the density estimators in terms of the index of resolvability.
In some regression and classification contexts, a complexity penalty may be added to a squared error or other
distortion criterion that does not correspond to the length
of an efficient description of the data. Bounds on the
statistical risk in those contexts have recently been developed in Barron [17] using inequalities of Bernstein and
Hoeffding instead of the Chernoff inequalities used here.
Interpretations and basic properties of minimum complexity estimators are discussed in Sections II-IV. Motivation for the index of resolvability is given in Section V
followed by examples of the resolvability for various models in Section VI. The main statistical convergence results
are given in Section VII followed by the proofs in Section
VIII. Some regression and classification problems that
can be examined from the minimum description-length
framework are discussed in Section IX.

that is proved to bound the rate of convergence of minimum complexity density estimators as well as the information-theoretic redundancy of the corresponding total
description length. Here D(pJlq) denotes the relative
entropy. The resolvability of a density function is determined by how accurately it can be approximated in the
relative entropy sense by densities of moderate complexity relative to the sample size. Theorem 4 and its corollary
II. AN INFORMAL
EXAMPLE
state conditions under which the minimum complexity
The minimum description-length criterion for density
density estimator converges in squared Hellinger distance
d?ir(r?,&) = /(& - KJ’ with rate bounded by the in- estimation is illustrated by the following example. Let
dex of resolvability, i.e.,
x1,x2,. . ., X,, .be independent and identically distributed
according to an unknown probability density p(x). Supin probability. (1.4)
di$( PA)
5 O(%P))
pose it happens that this density is normal with mean F
Also the complexity of the estimate relative to the sample and variance a2 = fi. In this example, p is some fixed
size, L,($,>/n is shown to be not greater than OCR,(p))
uncomputable real number, whereas v!% is computable.
in probability.
(Computability means that a fixed-length program exists
The results on the index of resolvability demonstrate that can take any integer b as an input and compute the
the statistical effectiveness of the minimum description- number to accuracy 2-“.)
length principle as a method of inference. Indeed, with
The minimum description-length idea is to choose a
high probability, the estimation error d$(p,$,)
plus the simple density q that yields high likelihood on the data. If
complexity per sample size L,( fi,>/n, which are achieved L(q) is the number of bits needed to describe q and
by the minimum complexity estimator, are as small as can logl/q(X,;
. .) X,) is the number of bits in the Shannon
be expected from an examination of the optimal tradeoff code (relative to q) for the data, then
between the approximation error D(pllq) and the com1
plexity L(q)/n,
as achieved by the index of resolvability.
min L(q) +log
(2.1)
9 i
9(X,,...>X,)
I
It is shown that the index of resolvability R,(p) is of
order l/n if the density is on the list; order (log n)/n in is the minimum two-stage description length of the data.
parametric cases; order (l/nP’ or ((logn)/n)Y in some (The actual Shannon code has length equal to the integer
nonparametric cases, with 0 < y < 1; and order o(1) in part of the logarithm of the reciprocal of the probability
of discretized values of the data; the use of the density is
general, provided inf, ET D(p(lq) = 0.
It need not be known in advance which class of densi- a convenient simplification.)
ties is correct. With minimum complexity estimation, we
For the Gaussian example, we may expect the proceare free to consider as many models as are plausible and dure to work as follows. For small sample sizes compared

1036

IEEE TRANSACTIONS

to the complexity of the normal family (say y1I lo), we
would estimate 8, to be one of a few very simple densities, such as a uniform density over a simple range that
includes the sample. For moderate sample sizes (perhaps
IZ= 100) we begin to use the normal family. Parameter
estimates and associated description lengths that achieve
approximately the best tradeoff between complexity and
likelihood are derived in [7], 1121,[131and [16, Section 4.21
(see also Section VI where related description lengths are
given that optimize the index of resolvability in parametric cases>.In particular, we take the maximum likelihood
estimates <x, = (l/n)CX,
and S,’= (l/n)C(X, - xn12)
rounded off to the simplest numbers fi and (i2 in the
confidence intervals xn + l/G
and S,’f l/G.
These numbers are described using roughly (1/2)log lzci
and (1/2)log y1c2bits. Here ci = l/S: and c2 = 1/(2S,4)
are the empirical Fisher informations, for p and c2
respectively, evaluated at the maximum likelihood.’ See
[7], [12], [13] for relevant discussion on the appropriate
constants. In the present example, for which the variance
is a relatively simple number, the enumeration of the bits
of the estimate is preferred only for sample sizes with
(1/2)log ylcZ less than the length of the description of fi.
Then when we have enough data to determine the first
10 or so bits of the unknown variance (n = 1 OOOOOO),
we
begin to believe that the density estimate is normal with
variance equal to 6. We have guessed correctly that
u2 = fi, and this guess results in a shorter description.
The estimated mean ,&, is x, rounded to an accuracy of
a/&;
this requires roughly (1/2)log ylci bits where ci =
1,‘~~. For any constant c, no simple number is found in
the interval x f c/h
for large ,y1. We must content
ourselves with $,, = normal (fi,, 6).
Note that the complexity of the best density estimate fi,,
grows at first like ~1,then like (1/2)log ylcr +(1/2)log rzc2,
and finally like (1/2)log nc,. For large n, we have discovered that the true density function is Gaussian, that its
variance is exactly fi, and that its mean is approximately
x,5 a/&.
From the data alone, it becomes apparent
that the structure of the underlying probability law consists of its Gaussian shape and its special variance. Its
mean, however, has no special properties.
Even if the true density is not a member of any of the
usual parametric families, the minimum description-length
criterion may select a family to provide an adequate
approximation for a certain range of sample sizes. Additional samples will then throw doubt on the tentative
choice. With the aid of the criterion, we are then free to
rIt happens in this Gaussian example that the Fisher information
matrix is diagonal. For parametric families with nondiagonal information matrices, approximately the best tradeoff is achieved with an
estimated parameter vector in an elliptical confidence region centered at
the MLE. Such estimates are described in a locally rotated and scaled
coordinate system, using about (1/21log nc, +
+(1/21log ltcd bits,
which reduces to (1/2)logdet(&
where cr, ., cd are the eigenvalues
of the empirical Fisher information i and d is the dimension of the
parameter-space, see [16, Sect. 4.21. Thus (d/2llog n is the dominant
term in the description of the parameters and the (1/2)logdet(!)
term
accounts for the local curvature of likelihood function.

ON INFORMATION

THEORY,

VOL. 37, NO. 4, JULY 1991

jump to some other family (and proceed with the estimation of any parameters in this family). The question is
whether this disorderly jumping around from procedure
to procedure on the basis of some peeking at the data will
still allow convergence. We show that indeed convergence
does occur for densities estimated by the minimum complexity or minimum description-length criterion.
The formulation of the minimum description-length
principle as in [6], [7], [12], [13] leads to a restriction on
the parameter estimates in each family to a grid of points
spaced at width of order l/G
and the optimization of a
criterion for which the dominant terms are
f logn +logl,p;(Xn),

(2.2)

where d is the number of parameters and 6 is the
maximum likelihood estimate of the parameter vector
OERd, truncated to (1/2)logn
bits per parameter.
Rissanen 181,[9] shows that for most parameter points this
criterion yields asymptotically the best data compression.
Indeed, he shows in [9] that the redundancy of order
(d /2)log n cannot be beaten except for a set of parameter points of measure zero. The theory we develop shows
that the minimum description-length criterion for model
selection is also justified on the grounds that it produces
statistically accurate estimates of the density.
The Gaussian example illustrates an advantage of deviating in some cases from the minimum description-length
criterion in the form (2.2), by not necessarily restricting
the parameter estimates to a grid of preassigned widths of
order l/G.
By allowing the search to include simpler
parameter values, in particular to include maximum likelihood estimates truncated to fewer than (1/2)log IZ bits
and nearby numbers of low complexity (such as fi in the
previous example), we allow for the possibility of discovery of density functions with special parameter points,
which in some cases may govern the distribution of the
observed data.
Other departures from the minimum description-length
criterion in the form (2.2) are justified when it is not
assumed that the density is in a finite-dimensional family.
See Case 4 in Section VI for one such example. Nevertheless, it will be seen (Case 3 in Section VI> that criteria of
the form (2.21, using sequences of parametric families,
continue to be effective for both data compression and
inference in an infinite-dimensional context.
III. SOME PRELIMINARIES
In this section we set up some notation, define minimum complexity density estimation, and discuss some
specializations of the general method.
Let Xi, X,; . .,X,, . . . be independent random variables drawn from a (possibly unknown) probability density
function p(n). The random variables are assumed to take
values in a measurable space X and the density function
is taken with respect to a known sigma-finite dominating
measure v(h). The joint density function for X” =

BARRON

AND

COVER:

MINIMUM

COMPLEXITY

DENSITY

al,x2,~-, X,) is denoted by p(X”)= nyZ,p(Xi> for
n=1,2;..;
the probability distribution for the process is
denoted by P.
For each y1=1,2;*., let I, be a countable collection
of probability density functions q(x) (each taken with
respect to the same measure Y(A)). For each q in I,, we
let q( X”) = ll:= lq( X,) denote the corresponding product
density and we let Q denote the corresponding probability distribution (which would make the Xi independent
with density q).
We need a notion of the length of a description of q.
For each n, let L,(q) be nonnegative numbers defined
for each q in I?,. (For convenience, we also define
L,(q) =QZ if q is not in I’,.) The following summability
requirement,

(3.1)
9 t L

is the essential condition assumed of the numbers L,(q).
The complexity of the data and the minimum complexity density estimate are now defined relative to the lengths
L,(q), q E I,. The sample size n is assumed to be given.
Definition: The complexity B(X”) of the data X” relative to L, and I, is defined by
L,(q)+log-

(3.2)

The minimum complexity estimator j?, of the density relative to L, and I’, is defined by
6, = argmin L,(q)
4 E r, i

+log-

1
4(Xn) 1 ’

1037

ESTIMATION

(3.3)

where, in the case of ties, the density J?, is chosen for
which L,(b,) is shortest (and any further ties are broken
by selecting the density with least index in I,). It will be
seen that a minimizing 6, exists with probability one.
There are two fundamental interpretations of the minimum complexity criterion: one from the theory of data
compression, the other from Bayesian statistics.

necessary and sufficient conditions for the existence of
instantaneous binary codes of the prescribed lengths (see
120,pp. 45-49, 5141).
To explain the second stage of the code, observe that if
q is given, then by rounding logl/q(X”)
up to the
nearest integer, lengths L,(Xn) = [logl/q( Xn)l are obtained that satisfy Kraft’s inequality, CX,ZL@“) 4 1.
Hence, as discovered by Shannon, if q is given, then
[logl/q(X”)j
is the length of an instantaneous code
that describes the sequence X”.
On .the other hand, when the density is estimated from
the data, then in order for the Shannon code based on an
estimate $, to be uniquely decodable, the density 6, must
first be encoded. The overall length of the code for the
data is then (within one bit of)
L,(A)

+lwl/&(Xn).

(3.4)

Thus any density estimator corresponds to a code for the
data. The minimum complexity criterion simply chooses
the estimator yielding the best compression.
Coding Interpretation in the Continuous Case: If the
space X is not discrete, then no finite-length uniquely
decodable codes can exist. Nevertheless, quantization of
X does lead to outcomes that are finitely describable. In
the case of fine quantization, density functions are approximated by ratios of measures. Indeed, if [xl denotes
the quantization region that contains x, then q(x) =
f or almost every x (where the limit is
lim Q([xI>/v([~l)
taken for a refining sequence of quantization regions that
generates X). Consequently, log l/q(X”)
= log l/
where [Xn] denotes the
Q<[Xnl> + log v([X”I)
coordinate-wise quantization of X”. If this approximation
were valid uniformly for q E I,, then the minimization as
in (3.3) would amount to choosing a density that minimizes the two-stage codelength for the quantized data,

L(Q>+log1/

Q(Wl).

(3.5)

For simplicity of exposition in this paper, we restrict
attention to the minimization involving densities as in
(3.3). Discrete random variables are then a special case
A. Coding Interpretation
with v equal to counting measure. Barron [161 treats the
The complexity defined in (3.2) is interpreted as a case in which the distribution is estimated by minimizing
minimal two-stage description length for X”, for a given (3.5); in the theory developed there, the quantization
sample size n. The terms L,(q) and logl/q(X”)
corre- regions are allowed to, shrink as the sample size n +m. [It
spond, respectively, to the length of a description of q is seen that the estimators based on uniformly quantized
and the length of a description of X” based on q.
data on the real line behave in a manner essentially
To give the precise coding interpretation, assume that analogous to the continuous case when the width h of the
X is discrete and that each q is a probability mass quantization intervals are of smaller order than l/n, and
function (i.e., q is a density with respect to v = counting in a manner analogous to the discrete case when nh is
measure). If the numbers L,(q), q E I, are positive inte- large. New techniques are also developed there to handle
gers satisfying (3.1), then L,(q) is the length of an instan- the case when nh is constant.]
taneously decodable binary code for q E I,. The instantaneous decodability property states that no codeword is B. Bayesian Inference Interpretation
the prefix of any other codeword. Since the second-stage
Let w,(q) be a prior probability mass function on
description of X” follows the code for q, the prefix
condition is essential for decoding the two stages. The q E I,, and set L,(q) = log l/ w,(q) (with the convention
condition (3.1) in this context is Kraft’s inequality giving that if w,(q) = 0 then L,(q) =a). Then the summability

IEEE TRANSACTIONS

1038

condition (3.1) is satisfied since
L-

LAq)= Cw,(q)

9

= 1.

(3.6)

9

The minimization in (3.3) is seen to be the same as the
maximization of
2-L,‘4’q(

X”))

(3.7)

which is proportional (as a function of q E I?,> to the
Bayes posterior probability of q given X”.
Consequently, the estimator fi, defined in (3.3) is the
Bayes estimator minimizing the probability of error,
C,w,(q>Q{b, # q} for a density in I’, drawn according to
w,(q).
The connection between the Bayesian and coding interpretations is that if w,(q) is a prior probability function
concentrated on a countable set of densities q, then
logl/ w,(q) is the length (rounded to an integer) of a
Shannon code for q based on w,. Conversely, if L,(q) is a
codelength for a uniquely decodable code, then w,(q) =
2-Ln(q)/cn d ef mes a proper prior probability (where c, =
C2PLn(4)5 1 is the normalizing constant).
Thus the minimum description-length principle provides an information-theoretic justification of Bayes’rule.
A Bayesian with a discrete prior w,(q), q E r, chooses
the estimate that achieves the minimum total description
length L,(j,) + log l/fi,(Xn>. Of course, Bayesian estimation also has decision-theoretic justification.
We emphasize the necessity of the term L,(fi,) that
involves the prior probability. Indeed, in the absence of
this term, if 3, depends on X”, then, in general,
logl/$,(X”)
will not satisfy Kraft’s inequality and hence
there does not exist a code for X” with lengths
logl/fi,(X”).
A consequence is that the maximum likelihood rule that selects a density to achieve the minimum
value of log l/sn(Xn> does not admit a description-length
interpretation of this value.
Some basic results for the minimum complexity estimator are a straightforward consequence of the Bayesian
interpretation. Define
m( Xn) = C 2-Ln’q’q( Xn).
9

(3.8)

ON INFORMATION

THEORY,

VOL. 37, NO. 4, JULY 1991

estimators based on the data X,, X2; . .,X,,. By definition, an estimator b,, is inadmissible if there is another
estimator $3 such that P@L2) f p} 5 P{bn # p} for all
p E I,, with strict inequality for some p E r,. If no such
uniformly better estimator exists, then b,, is said to be
admissible. The following proposition is a consequence of
the admissibility of Bayes rules.
Proposition 2: The minimum complexity estimator fi,, is
admissible for the estimation of a density in the countable
set r,.
IV.

IDEALIZED

CODELENGTHS

AND KOLMOGOROV

COMPLEXITY

Clearly, a practical requirement on the candidate probability distributions Q is that finite length descriptions
exist, i.e., Q must be computable.2 Subject to this restriction, an idealized form of the minimum complexity criterion is obtained by choosing the descriptions of the probabilities Q to be as short as possible.
Let U be a fixed universal computer with a domain
consisting of finite length binary programs 4 that satisfy
the prefix property. Specifically, no acceptable program is
a prefix of another, so that the set of binary programs
constitutes an instantaneous code and consequently the
program lengths satisfy the Kraft inequality. Let I* be
the set of all computable probability measures on X. For
each Q E I*, let L*(Q) = L:(Q) be the minimum length
of programs that recursively enumerate Q,

L*(Q) = uc~;n(!lemth(4).

(4-l)

This L*(Q) is the Kolmogorov-Solomonoff-Chaitin algorithmic complexity of Q. This measure was independently
posed, in different levels of detail, by Kolmogorov [l],
Solomonoff [21], and Chaitin [22]. For fundamental properties of L*, see Chaitin [23] and Levin [24], [25].
We mention that for any two universal computers U
and I/ there exists a finite constant c = cU,” such that
IL;(Q)-L$(Q)IIc,

forall QEI’*.

(4.2)

Moreover, for any computable function L(Q), Q E I? (on
a domain I c I*> that satisfies the Kraft inequality, there
exists a constant c = cL such that

In the Bayesian interpretation, m(X”) is the marginal
density function for X”. It is seen that m(X”> is finite for
for all Q E I?.
L*(Q) I L(Q) + c,
(4.3)
almost every X” (indeed it has integral not greater than
In
the
same
way,
for
any
computable
prior
w(Q),
Q
E
I c
one). Thus for almost every X”, the quantities in (3.7) are
I*
with
&w(Q)
=
1,
there
is
an
constant
c
=
c,
such
that
summable for q E I, and, consequently, the maximum is
for all Q E I, (4.4)
achieved. (Indeed, let v >. 0 be the value in (3.7) for some
L*(Q) 5 bl/w(Q>
+ c,
q; by summability there must be a finite set of q such that whence
outside this set the value of 2-Ln(q) q(X”) is less than v,
2-L*(9) 2 w( Q)2-“,
forall QEI.
and hence the overall maximum occurs on this finite set.)
(4.5)
Thus the following proposition is proved.
It is these basic facts about the algorithmic complexity
Proposition 1: There almost surely exists at least one L*(Q) that provide its appeal as a notion of idealized
and no more than finitely many densities achieving the
maximum in (3.7). Thus the minimum complexity density
‘A probability measure Q on X is computable, relative to a countable
collection of sets A,, A,,
that generates the measurable space X, if
estimator 3, exists with probability one.
the set {(r,,~*,k):
it < Q(Ak) < Ye for Y~,Y~ rational and k = 1,2,.
Next we show admissibility of the minimum complexity is recursively enumerable. Thus Q(A,) can be calculated to any preas-}
estimator of a density in the countable set I,, among signed degree of accuracy.

BARRON

AND

COVER:

MINIMUM

COMPLEXITY

DENSITY

1039

ESTIMATION

codelength for the minimum complexity estimation princi- remains one). Then, for sample sizes n much less than
ple. In particular, (4.5) gives a sense in which 2-L*(Q) is a 1000, it is unlikely for a normal density to have observauniversal prior, giving (essentially) at least as much mass tions in the perturbed segment. The true density and the
to distributions as would any computable prior.
normal density are indistinguishable in this case. Indeed,
the relative entropy distance between the true density and
V. AN INDEX OF RESOLVABILITY
the standard normal is log1.001, which is approximately
Minimum complexity density estimation chooses a den- equal to 0.001log e. If L(p) and L(4) are the description
lengths of the true density and the normal density, respecsity that minimizes the quantity
tively, then from definition (5.3), the normal density has
better resolvability for n < lOOO(L(p) - L(+))/log e.
(5-l)
The density 3, is a theoretical analog of the samplebased minimum complexity estimator fi,. In our analysis
This quantity is a random variable depending on Xi, of $,, we regard it as being more directly an estimator of
i= 1,2;. .) n, which are assumed to be independent with 5, than an estimator of p. The total error between fi,, and
unknown density p. In order to help explain the behavior p involves contributions from the estimation of ji, by fi,,
of this minimization, we replace (5.1) by its expected and from the approximation of p by 6,.
value and investigate the corresponding minimization.
Observe that in general the resolvability can be imThis expectation is
proved by increasing n, enlarging I,, or decreasing the
lengths L,(q).
1
In the limit as n --f~, the index of resolvability R,(p)
Cl(X)
converges to zero if and only if there is a sequence of
densities qn in I, such that D(plJq,) + 0 and L,(q,)/

;L&)+qilog- I
= j&(q)

+ qdlq)

+ fw,

(5.2)

where H(p) = - /p(x)log p(x>v(dx) is the entropy (of p
with respect to v) and D(pllq) = Jp(x) log(p(x)/
q(x))v(dx)
is the relative entropy or Kullback-Leibler
distance between p and q.
Since by the law of large numbers, the quantities in
(5.1) are close to the expected value for large ~1, we
anticipate that the behavior of the minimization of (5.1)
will be largely determined by the minimization of (5.2).
Definition: The index of resolvability of p (relative to a
list I’,,, codelengths L,, and sample size n) is defined by
.

(5.3)

An interpretation of the index of resolvability is the
following. If we know p, then nH(p) bits are required to
describe X” on the average. If we do not know p, then
n(H(p)+
R,(p)) bits suffice to describe X” on the average. This is proved shortly in Proposition 4. The index of
resolvability may be interpreted as the minimum description-length principle applied on the average. The index of
resolvability is used (in the proof of Theorem 4) to bound
the rate of convergence of the density estimator fin that
minimizes (5.1) in terms of a density J?, that achieves the
minimum in (5.3).
The density fi,, minimizing L,(q) among those that
achieve the minimum in (5.3) is regarded as the density
that best resolves p for sample size n. A compromise is
achieved between densities that closely approximate p
and densities with logical simplicity.
For example, suppose the true density p is a standard
normal perturbed by having zero density in a small segment accounting for about 0.001 of the mass of the
normal curve and having density scaled up by a factor of
1.001 on the rest of the line (so that the total area

12+ 0.
Definition:

The information closure of I, denoted by I?,
is the set of all probability densities p for which
inf qErD(pllq>=O.
In the case of all computable probability measures on
the real line, it is shown in Barron [16] that the information closure T* consists of all densities p for which
D(pllq) is finite for some computable measure Q . Moreover, r* includes all bounded densities with finite support
and all densities with tails or peaks bounded by a computable integrable function.
Here we show that the information closure is the set of
all distributions for which the resolvability tends to zero
as n + co.A condition is required to force regular behavior of the numbers L,(q) as a function of n. Let I = lJ .I,
be the union of the lists of densities I,.
Growth restriction:
L,(q)

= O(n),

for each q E r.

(5.4)

Note that this condition requires that each q E l7 is in I,
for all large n. The growth restriction is automatically
satisfied for a constant <I, = I) or increasing <I, t I’)
sequence of sets of densities with a constant (L,(q) =
L(q)) or convergent (lima L,(q)= L(q)) sequence of
codelengths.
Proposition 3: If the numbers L,(q) satisfy the growth
restriction (5.4), then
lim R,(p)

n-m

= 0,

(5.5)

if and only if p is in i;, the information closure of I.
Proof of Proposition 3: Clearly R,(p) + 0 implies
D(p(( 6,) -+ 0 and hence p is in r. Suppose conversely
that inf, ~ r D(p(lq) = 0. G iven any E > 0, choose q in I

IEEE

1040

such that D(pllq)
(5.41,

TRANSACTIONS

< E. Then by the growth restriction

limR,(p)~~~~~L,(q)+D(pllq)<E.
(5.6)
n+Q=
0
Now E > 0 is arbitrary, so lim R,(p) = 0 as desired.
The redundancy A,(p) of a code is defined to be the
expected value of the difference between the actual and
ideal codelengths divided by the sample size. For the
minimum two-stage codelengths B(X”) defined as in
(3.2) we have
A,(p) = $E(B(Xn)-logl,p(X’)).

(5.7)

Here logl/p(X”)
is interpreted as the ideal codelength:
it can only be achieved with true knowledge of the distribution p. Its expected length is the entropy of p. When
the entropy is finite, the redundancy measures the excess
average description length beyond the entropy. The redundancy, which plays a role similar to that of a risk
function in statistical decision theory, is the basis for
information-theoretic notions of the efficiency of a code,
as developed in Davisson [1913
Proposition 4: The redundancy of the minimum twostage code is less than or equal to the index of resolvability, i.e.,
4

P> 2 u

P>.

(5J)

Proof: We have
;(n(xn)

-logl,P(xn))

= min ~L,(q)++Iog-q=r, i n

P(X?

. (5.9)
d-v
I
Taking the expected value with respect to P, we have
A,,(p)=Em~(.)<m~E(.)=R,(p),
as desired.

0

Remarks: In nondiscrete cases, B(X”) and logl/p(Xn)
are not actually codelengths. Nevertheless, the log density
ratio logp(X”)/q(Xn)
in (5.9) does represent the limit,
as the quantization regions become vanishingly small, of
the log probability ratio log P([ Xn])/ Q<[Xn]>. Ignoring
the necessary rounding to integer lengths, this log probability ratio is the difference between the codelength
log l/Q<[ X”]) and the ideal codelength log l/P([ Xn]>.
For quantized data, the redundancy of the minimum
two-stage code is the expected value of (L3([Xnl) n where B([X’l) is the minimum of the
logl/P([X”I))/
codelengths from expression (3.5). In this case, the redundancy is bounded by R;](p) = min, (L,(q)/n
+
D[‘](pllq)).
Here D[‘](pllq) = CAP(A)
P(A)/Q(A)
is
3A referee has suggested another relevant notion of redundancy,
namely, E,(B(X”)logl/m(X”)),
where m(X”) = II:4 ZPLC4)q(X”)
and the expectation E, is taken with respect to m(xn). This measures
the average deficiency of the minimal two-stage description compared to
the code that is optimal for minimizing the Bayes average description
length with prior w(q) = 2mL(4).

ON INFORMATIONTHEORY,

VOL.

37, NO. 4, JULY

1991

the discrete relative entropy obtained by summing over
sets in the partition formed by the quantization regions.
As a consequence of familiar inequality D[‘](pllq) I
D(pllq), we have R;](p) I R,(p) uniformly for all quantizations. Consequently, the index of resolvability
R,(p) = min(L,(q)/n
+ D(p(lq)) provides a bound on
the redundancy that holds uniformly over all quantizations.
The key role of the resolvability for estimation by the
minimum description length criterion will be given in
Section VII. There it will be shown that R,(p) bounds
the rate of convergence of the density estimator.
VI. EXAMPLES OF RESOLVABILITY
In this section we present bounds on the index of
resolvability for various classes of densities. In each case
the list I is chosen to have information closure which
includes the desired class of densities. The bounds on
resolvability are obtained with specific choices of L,(q).
Nevertheless, in each case these.bounds lead to bounds
on the resolvability using L*(q) (the algorithmic complexity of q). With L*, the best rates of convergence of the
resolvability hold without prior knowledge of the class of
densities.
We show that the resolvability R,(p) is 0(1/n> in
computable cases, O((log n)/ n) in smooth parametric
cases, and O(l/nY’ or O(((log n)/n)Y) in some nonparametric cases, where 0 < y < 1.
The bounds on resolvability in these examples are derived in anticipation of the consequencesfor the rates of
convergence of the density estimator (Section VII). We
intersperse the examples and resolvability calculations
with remarks on the implications for parametric model
selection. There is also opportunity to compare some
choices of two stage codes in the parametric case using
average and minimax criteria involving .the index of resolvability.
Case 1) P is computable: R,(p) = L(p)/n
for all
large n.
Suppose L,(q) = L(q) does not depend on n. Let 5,
be the density that achieves the best resolution in (5.3). If
the density p is on the list I, then, for all sufficiently
large’n,
5, = P

(6.1)

and
R,(P)

L(P)
= ~
12 f

(6.2)

If there is more than one density on the list that is a.e.
equal to p, then in (6.1) and (6.2) we take the one for
which L(p) is shortest.
To verify (6.1) and (6.2) we first note that for all n,
0 < L(g,) 4 L(p) (because any q with L(q) > L(p) results in a higher value of L(q)/n + D(pllq) than the
value L(p)/ n that is achieved at q = p). Now for small n
compared to L(p), densities q that are simpler than p
may be preferred. However, for all n r L(p)/D,,,,
it

BARRON

AND

COVER:

MINIMUM

COMPLEXITY

DENSITY

must be that j,, = p and R,(p) = L(p)/n

where

Dmin=m~(D(plIq):

L(q)

<L(P)].

ESTIMATION

(6.3)

Indeed for such n, we observe that for each q with
L(q) < L(p), the value of L(q)/n + D(p11q) is greater
than Dmin and hence greater than L(p)/n,
which is the
value at p, whence $,, = p.
Case 2) P is in a d-dimensional parametric family
R,(P)

N (d/z)(logn)/n.

For sufficiently regular parametric families {pe: 19E O},
0 c Rd, there exists I,,, L, and constants c, such that for
every 8
(d/2)logn+c,+o(l)
Rn( Pe) 5

(6.4)

n

Moreover, for every I, and L, and for all 8 except in a
set of Lebesgue measure zero,

(dP)logn
R?z(P,)3l--(l))

n

.

(6.5)

The lower bound (6.5) is a consequence of a bound on
redundancy proved in Rissanen [9, Theorem 11, and the
regularity conditions stated there are required. The upper
bound (6.4) is closely related to a result in Rissanen [8,
Theorem lb)] for the redundancy of two-stage codes.
Here we derive (6.4) requiring only that 0 be an open set
and that for each 0 the relative entropy D(p,llp6) is twice
continuously differentiable as a function of 6 (so that the
second order Taylor expansion (6.7) holds). For compact
subsets of the parameter space, bounds on the minimax
resolvability are also obtained.
First to establish (6.4), we let I, be the set of densities
ps for which the binary expansions of the parameters
terminate in (1/2)logn bits to the right of the decimal
point and we set the corresponding description length to
be

1041

where Je is the nonnegative definite matrix of second
partial derivatives (with respect to e’> of E ln(p,(X)/
p,$X>> evaluated at 0 = 0. Although we do not need a
further characterization of JB here, it is known that under
additional regularity conditions Je is the Fisher information matrix with entries - E(d2 In p,,(X>/Nj80,>.
To optimize the constant c, in (6.4) according to average or minimax resolvability criteria, I, should correspond to a nonuniform grid of points to account for the
curvature and scaling reflected in Je. Assume that JB is
positive definite. In the Appendix, it is shown that, given
E > 0, the best covering of the parameter space (such that
for every 0 there is a 6 in the net with (0 - ejTJ,(fI - 6) I
.?> is achieved by a net having an asymptotic density of
hd(l/ ejd det ( JOI1/’ points per unit volume in neighborhoods of 0, where h, is a constant (equal to the optimum
density for the coverage of Rd by balls of unit radius). We
set E = Jd/n, which optimizes the bound on the resolvability. We need a code for the points in the net. It is
shown in the Appendix, that if w(0) is a continuous and
strictly positive prior density on 0, then the points in the
net can be described using lengths L,(p& ps E r,, such
that for any given 8,
L,( pe) = 4 log n + k logdet ( Je)

1
+log--w(e)

d

2 l”gc,+O(l),

(6.8)

where 6 is the point in the net that best approximates e
and o(l) * 0 as n -+ ~0.Here cd = d/(Ad>2/d is a constant
which is close to 2rre for large d. In (6.8) the term
log l/ w(0) may be regarded as the description length per
unit volume, for a small set that contains 8, and the
remaining terms account for the log of the number of
points per unit volume in this set. Sets I, and codelengths
L, with properties similar to (6.8) are derived in Barron
d
[16] and Wallace and Freeman [13]. The principle differL,( PO) = lLel + 2 log n,
ence is that here the codelengths are designed to optimize
the resolvability, which involves the expected value of the
for pe E I, where Zleldenotes the length of a code for the
log-likelihood, whereas in [16] the codelengths are devector of integer parts of the components of 19.Thus I,
signed to optimize the total description-length based on
corresponds to a rectangular grid of parameter values
the sample value. (This accounts for the use of the Fisher
with cells of equal width 6 = l/h.
The choice of 6 of
information .$ in (6.8) instead of the empirical Fisher
order l/G
is seen to optimize the resolvability, which is
information J.)
of order ( - log s>/n + 6 2. For 0 E 0, the truncation of
With the given choice of L, and I, and using R,(p,) I
the binary expansion of the coordinates to (1/2)log n bits
L,(p&/n
+ D(p,llp&
we obtain the following bound on
yields an approximation to the density with relative enthe resolvability,
tropy distance of order l/n and a codelength of ZLel+
(d /2> log n. Consequently, the redundancy satisfies
det ( Jo)“*
R,( ps> I ((d /2)log n + O(l>>/n. This verifies (6.4).
w(e)
This derivation uses the fact that the relative entropy
satisfies D(p,/pi,) = O(ll0 - &12> as e + 0 for any given 8.
Indeed, since D( psllp~) achieves a minimum at e = 8, it
-~logc,/e+o(l)
. (6.9)
follows that the gradient with respect to 6 is zero at 0 and
the second order Taylor expansion is
Moreover, it is seen that this bound holds uniformly on
compact subsets of the parameter space. For any compact
D(p~IJPR)=~(e-~~l..I,(B-~ij)lOge+O(lje-~llz),
set B c 0, the asymptotic minimax value of the right side
(6.7) of (6.9) is obtained by choosing the prior w(0) such that

1042

IEEE

TRANSACTIONS

ON INFORMATION

THEORY,

VOL.

37, NO. 4, JULY

1991

the bound is asymptotically independent of 8, i.e., we set

contains the density q. Here L(k) is chosen to satisfy
Ck2-L(k) 5 1 so that it is interpretable as a codelength for
det(J@)“*
k.
If k* is the index of the family that contains the true
w(e) =
(6.10)
2
density, then without prior knowledge that this is the right
'J,B
family, we obtain an index of resolvability that differs by
where c~,~ = lB det (J,>l/* de. With this choice, it is seen
only L( k*)/n
when compared to the resolvability atthat the minimax resolvability is bounded by
tained with true knowledge of the family. Consequently,
the index of resolvability remains of order (log n>/n,
R, _<$ ; logn +logjRdet(J,)“*de
when the true density is in one of the parametric families,
even though the true family is unknown to us.
A related criterion for the selection of parametric mod-;log;+o(l)
(6.11)
els was introduced by Schwarz [30], with a Bayesian
Corresponding to this bound is the choice of a constant interpretation, and by Barron [16] and Rissanen [lo],
with a minimum two-stage description-length interpretacodelength
tion. In this method the index l, of the family is
d
where
L,(~~)=~logn+logc,,~+logc,+6,,
(6.12) chosen to minimize L(k) + log l/mk(Xn>,
m,(X”> = lpik)(X”)w,(0) de is the marginal density of
which is equal to the log of the minimum cardinality of X” obtained by integrating with respect to a given prior
nets that cover B in such a way that for every 0 E B there density w,(e) for the kth family. Schwarz 1301 and
is a 6 in the net with (0 - G>TJ,(O-6) I (d/n).
Here Rissanen [lo] have obtained approximations to the criterion showing that it amounts to the minimization of
lim 6, = 0.
Similar lower bounds on minimax resolvability can be (d, /2)log n + log l/pek’(X”) as in the minimum descripobtained from known lower bounds on minimax redun- tion-length criterion. Here d, is the dimension of the kth
dancy. Indeed, it is shown in Barron and Clarke [26] (with family. A more detailed analysis as in [16], applying
uniformity on compact sets B shown in Clark [27]) that, Laplace’s method to approximate the integral defining
under suitable regularity conditions, the code that opti- m,(X”), yields exact asymptotics, including terms involvmizes the average redundancy, i.e., the code based on the ing the prior density and the determinant of the empirical
density m(X”> = lpe(Xn)w(O> de, has asymptotic redun- Fisher information matrix. This analysis is the basis for
(6.13) as derived in [26]. Moreover, examination of the
dancy given by
approximation to the criterion shows that it is very similar
to minimum complexity estimation with codelengths
L n(pik’) approximated as in (6 .8) .
Case 3) Sequences of parametric families:

- ; log2%-e+ o(1) . (6.13)
1
Consequently the prior in (6.10) yields the asymptotically
minimax redundancy as well as bounds on the minimax
resolvability. (A similar role for this prior is given in
Krichevsky and Trofimov [281 for the special case of the
redundancy of codes for the multinomial family.) Note
that the expression (6.13) for the redundancy and the
bound (6.9) for the resolvability differ in the constant
term, but otherwise they are the same. The prior in (6.101,
which is defined to be proportional to the square-root of
the determinant of the Fisher information matrix, was
introduced by Jeffreys [29, pp. 180-1811 in another statistical context.
Remarks: Consider the index of resolvability in a model
selection context. We are given a list of parametric families from which one is to be selected from the data by the
minimum description-length criterion. The previous analysis applies (with slight modification) to bound the index
of resolvability in this case. Indeed, let {pek)}, k = 1,2, * * *
be a list of families, with corresponding sets I,‘“’ and
codelengths L’,k)(s), each of which is designed to satisfy
(6.4). In this case I,, = lJ kI(k) is taken to be the union of
the sets of candidate densities and L;(q) = L’,k)(s> + L(k)
for q in I’, where k is the index of the family that

*r/m+

1)

What if the true density is not in any of the finitedimensional families? We show that for a large nonparametric class of densities, a sequences of parametric
families continues to yield a resolvability of order
(d, /2)(log n>/n, except that now the best dimension d,
grows with the sample size.
Consider the class of all densities p(x) with 0 < x < 1
for which the smoothness condition
j&$logp(x-))Zdu

<w

is satisfied for some r 2 1. We find sequences of parametric families with the property that for every such density,
the resolvability satisfies
2r/(2r+l)

(6.14)

Moreover, this rate is achieved by minimum complexity
density estimation without prior knowledge of the degree
of smoothness r.

BARRON

AND

COVER:

MINIMUM

COMPLEXITY

DENSITY

ESTIMATION

Consider sequencesof exponential families of the form

pid)(x) = ew 5

ejcbj(X>

-

@d(e)

j=l

,

depend on the density p or the dimension d) such that

D(pllp$?) I~~(O’lW

(6.15)

I

where ed(0) = log 10’exp(C,d_lOj$ji(x)) dx, 0 E Rd, and
l,&(x);.
., 4d(~) are orthonormal functions on L2[0, 11
that are chosen to form a basis for polynomials (of degree
d), splines (of order s 2 1 with m equally spaced knots
and d = m + s - l), or trigonometric series (with a maximal frequency of d/2). We focus on the polynomial and
spline cases,since the trigonometric case requires that the
periodic extension of log p(x) must also be r-times differentiable for (6.17) below to hold.
In Barron and Sheu, bounds are determined for the
relative entropy distances DC pII ~$9 and D(p$?ll pid’),
where 0” in Rd is chosen to minimize D(pllp~d’). There
the bounds are used to determine the rate at which
D(pllp,(dn’) converges to zero in probability, where e^ is
the maximum likelihood estimator of the parameter and
d, is a prescribed sequence of dimensions. Here we use
the bounds on the relative entropy from Barron and Sheu
[31] to derive bounds on the index of resolvability. This
bound on the resolvability will lead to the conclusion that,
with a sequence of dimensions d, estimated by the minimum description-length criterion, the density estimator
converges at rate bounded by ((log n)/n)2”/(2’+‘).
Let I, consist of the union for all d 2 1 of the sets of
densities pe(d) for which the binary expansion of the
coordinates of 6’terminate in (1/2)log n bits to the right
of the binary point. Also let wd(kl; . ., kd) = lJIfSlw(kj)
be a prior for vectors of integers that makes the coordinates independent with a probability mass function w(k),
k=0,*1,*2;+..
Assume, for convenience, that w(h) is
symmetric and decreasing in Ikl. (Assume other choices
for the prior distribution can also be shown to lead to
bounds of the desired form.) Then set the codelengths for
pid) in r, to equal
L~(p~d))=~l~gn+logl/wd([O])+210gd+c.

1043

PI”.

(6.17)

Moreover, there exists a constant y* depending on y such
that max, Ilog 1)$)(x)1 I y* for all large d. For simplicity
we assume that y* is an integer. By [31, (5.311we have for
any parameter vector 0 that
D( p$Qlpid))

I ~ey*e”JB*PBiiilO* - Oll*‘log e, (6.18)

where ad is a sequence of order O(d) in the polynomial
case and O(a) in the spline and trigonometric cases.
Now let 0 be chosen to equal f3* with each coordinate
truncated to (1/2)log n bits accuracy (to the right of the
binary point). As a consequence of the inequality
(eTj2+ . . . + (0,*)2 I /(log p$)j2 5 (Y”>~, it is seen that
the integers [ ej] are bounded by y *. Consequently, from
(6.16) the description length for this density is bounded by
L,(pid’)~(d/2)logn+dlog1/w(y*)+210gd+c.
(6.19)
With the given choice of 0 we have ]]f3*- 0]]* I d/n.
Now we combine the bounds from (6.17) and (6.18). It
is seen that for any constant co, there exist constants cl
and c2, such that for all d satisfying a$d/n SC,, the
relative entropy distance satisfies

D( PIIPid’) = D( PIIP$q + q P$‘ll Pid’)
2r

d
+c,-.

(6.20)

n

The first identity in (6.20) is a Pythagorean-like identity
from [31, Lemma 31 that is valid when the family is of the
exponential form. As a consequence of this bound, if a
sequenceof dimensions d = d, is chosen such that azd /n
is bounded, then the index of resolvability satisfies
R,(P)

~~L,,(pl”‘)+U(~llp~~‘)

(6.16)
<O(flogn)+O($)2’-t.0($).

Here logl/wd([8]) is the codelength for the integer part
of the parameter vector and 210gd + c is a codelength for
the dimension d where c = Cz=ld-2. (In the spline case,
if the order s is not fixed, then we add an additional log d
bits for the description of s _<d.)
Note that in this set up, the minimum complexity
criterion is used to automatically select a sequence of
dimensions d^, that provide parsimonious yet accurate
density estimates.
In order to verify (6.14) we proceed as follows. Let 0*
in Rd be chosen to minimize D(pplJpid)), i.e., p$? is that
member of the family that provides the best approximation to p in the relative entropy sense. Set y =
max, llog p(x)1 (which is finite as a consequence of the
integrability of the derivative). It is shown in [311 that in
the polynomial case and in the spline case (with r I s 5 d),
there exists a constant c (that depends on r, but does not

(6.21)

This bound is optimized with d = O(n/log n)1/(2r+1) (for
which the condition aid/n I O(1) will be satisfied in the
polynomial, spline and trigonometric cases for all r 2 l),
which yields
2r/(2r

+ 1)

(6.22)
Remarks: As a consequence of this bound, using the
results of Section VII, it is seen that the minimum complexity density estimator converges in squared Hellinger
distance at rate ((log n)/n)*‘/(*‘+‘).
Moreover, as previously noted, the minimum complexity criterion automatically chooses an appropriate sequence of dimensions d
from the data without knowledge of the degree of
smoothness r. In contrast, the rates of convergence of
order np2r/(2r+1) obtained in [31] are for density estima-

1044

IEEE

TR ANSACTIONS

tors in families with a sequence of dimensions d of order
n1/(2r+1), is preselected with knowledge of the degree of
smoothness r.

ON INFORMATION

THEORY,

VOL.

37, NO. 4, JULY

1991

gence rate of order n-*i3 is possible for the relative
entropy and the redundancy, as shown in [31], [36], and
[.54] using other histogram-based methods with a predeTherefore, with minimum complexity estimation, we termined sequence of number of bins. Yu and Speed [36,
converge at a rate within a logarithmic factor of the rate Theorem 3.11 demonstrate that np213 is the optimal reobtainable with knowledge of the smoothness class of the dundancy in a minimax setting involving first derivative
density. This remains true whether the true density is in a assumptions on the density function.
finite- or infinite-dimensional class.
Minimum complexity criteria may also be used to select
In related contexts of model selection (in particular in the boundaries of the cells (or more generally to select
the context of selecting the order of a polynomial regres- the locations of the knots for the spline models), leading
sion), Shibata [32] and Li [33] have shown that criteria to improved resolvability in some cases. Nevertheless,
closely related to criteria proposed by Akaike [34] are equal-spaced boundaries are sufficient to obtain the indiasymptotically optimal (in the sense that the risk of the cated bounds on the index of resolvability.
estimated model is asymptotically equivalent to the risk
Case 4) Fully nonparametric:
achievable by knowledge of the sequence of model dimenR,(p) = O( n-2r/(2r+1))f
sions that minimize the risk), provided the true distribution is not in any of the finite-dimensional families;
We show that by a special selection of the set I,, that
whereas this asymptotic optimality fails for other criteria
including the minimum description-length criterion. How- does not involve the use of a sequence of smooth parainever, to achieve this optimality property in infinite-dimen- metric families, a resolvability of O((l/n)2’/(2’+1))
can be attained using assional cases, the criteria used by Shibata and Li sacrifices stead of O((logn)/n)2’/(2’+1)
strong consistency in finite-dimensional cases. It is sumptions on derivatives of the density up to order r.
reasonable to conjecture that results similar to those Moreover, it is shown that O(n-2r/(2’+1)) is asymptotiobtained by Shibata carry over to the case of density cally the minimax resolvability as well as being the miniestimation with sequencesof exponential families. Unfor- max rate of convergence of density estimators.
First consider the class of density functions p on the
tunately, the methodology used by Shibata and Li relies
heavily on linearity properties of the models that limit the unit interval for which the log-density f(x) = log p(x) is
in the Sobolev ball,
validity of the criteria.
In contrast, the minimum complexity criterion does not
require the candidate parametric models to be approximately linear. We are free to add to the list densities
having arbitrary and possibly irregular form, in hopes of
obtaining better estimates in some cases, without hurting
the bounds on the rates of convergence in the best understood cases.
Concerning splines, we remark that ideally the mini- where y is an arbitrary positive constant.
The Kolmogorov c-entropy H, of a set of functions W
mum description-length criterion should be used to select
the order s. If instead we fix s, then the above analysis is the log of the cardinality of the smallest net of funcholds only for r _<s. With splines of a fixed order, it is not tions f such that for every function f in W there is an f
possible to take advantage of smoothness of order r > s with If(x) - f(x)] < E for all x (Kolmogorov and
to get the faster rates of convergence that are possible Tihomirov [37]). In Birman and Solomjak [38], it is shown
that for all sufficiently small E, the e-entropy of the
with polynomials or variable-order splines.
Histograms, which are piecewise constant density esti- Sobolev ball is bounded by c(l/~)‘/’ where c is a conmators, are a special case of spline models in which the stant depending only on y and r.
Fix an e-net with log-cardinality satisfying H, I
order of the spline is fixed at s = 1. Therefore, the results
of this section apply to histograms in the case that the C(l/$) ‘jr . We let I, consist of the densities proportional
minimum description-length criterion is used to select the to ef@) for f’ in the net. (Here E will be chosen as a
number of cells. The index of resolvability converges to function of n.) Thus each q in I,, is of the form q(x) =
zero at rate ((log n>/n> 2/3 for log-densities with at least efcxjPcf where cf = log liefiX)&. Now by [31, Lemma 11,
one square-integrable derivative. O ther results that in- if II. II denotes the supremum norm, we have
volve the stochastic complexity and the relative entropy in
the histogram setting may be found in Hall and Hannon
D( pllq) 5 +/11
/p(x)(f(x)
-fix))‘&
[3.5],Yu and Speed [36], and Barron, Gyorfi, and van der
Meulen [42]. In particular, Yu and Speed [36] demonstrate that the redundancy is c((log n)/n)2/3(1 + o(l))
_< ;&ll,l
f - fl12,
(6.23)
and explicitly identify the constant c, for a class of universal codes that (as they point out) are closely related to the
two-part codes we consider here. A slightly faster conver- which is less than (1/2)e’E* by the choice of J? Setting

BARRON

AND

COVER:

MINIMUM

COMPLEXITY

DENSITY

ESTIMATION

1045

integrated squared error at rate n-2r/(2ri1) uniformly for
densities in the Sobolev class. Now this rate is known to
be
asymptotically minimax for the integrated squared
1
1
error
for densities in W,l+ (see Bretagnolle and Huber
R,(p) I -HE + ?e’e*
n
[40], Efroimovich and Pinsker [41]); also, it is the minimax
rate for the redundancy (formulated as a cumulative
(6.24) relative entropy) as recently shown in Yu and Speed [36].
It follows therefore that n-2’/(2’+1) is also the minimax
which holds uniformly for all log-densities in the Sobolev rate for the index of resolvability of densities in this
ball. Noting that eB tends to one for small E, it is readily space. (Indeed, any faster uniform convergence of the
seen that choosing E, = O(n-‘/(2r+1)) gives the best rate resolvability would yield a faster convergence of the denin (6.24). With such a choice we have resolvability bounded sity estimator resulting in a contradiction.)
O ther classesof functions may be considered for which
by
if
the density functions in the class are bounded away
R,(p) = O( n-2r/(2r+1)),
(6.25)
from zero by an amount y, then the metric entropy H, is
uniformly for all log-densities in the Sobolev ball, for all known. By the same argument, the resolvability of densilarge n.
ties in the class by densities in the E-net automatically
By adding description-length terms for r and for y, we satisfies
may use the minimum complexity criterion to automatiK
1
R,(p) I ; + ye’E*.
(6.26)
cally select a suitable Sobolev ball from the data. The
indicated rate on the index of resolvability will hold
For each such class of functions, optimization of the
without prior knowledge of the best smoothness class.
Similar results for the index of resolvability can be choice E leads to a rate of convergence for the index of
obtained in the case of Sobolev conditions imposed on the resolvability.
Minimum complexity estimation with the e-net of funcdensity itself (instead. of the log-density), assuming that
tions
is analogous to Grenander’s method of sieve estimathe density function is bounded away from zero. Indeed,
tion
[39].
The important difference is that with minimum
let W<+ ={f E Wl: f(x) 2 l/y], y > 1, for which the
complexity
estimation we can automatically estimate the
E-entropy must have the same bound H, I c(l/~)~/‘, let
sieve
of
the
best granularity. Moreover, with the index of
I,, be the set of probability density functions proportional
resolvability
we have bounds on the rate of convergence
to f(x) for f’ in the E-net of Wi+, and let L,(q) be the
of
the
sieve
estimator.
log of the cardinality of this net. Each q in I, is of the
The Kolmogorov metric entropy has also been used by
form q(x)= f”(x)/cf where now cf= lJf”x)& I y and
Yatracos
[42] to obtain rates of convergence in L1 for a
q(x) 2 l/y*. Using inequalities between the relative endifferent
class of density estimators. However, it is not
tropy and Chi-square distance (D(pllq) I l(p - q>*/q I
known
to
us whether the metric entropy has previously
l(p - cq>*/q for c > 01, which may be deduced as in [31,
been
used
to give bounds on redundancy for universal
Section 31, it follows that for probability density functions
codes.
The
new ideas here are the relationships between
p(x>=f(x) in W{+, we have D(pllq) I y*/,‘< f(x)redundancy,
resolvability, and rates of convergence of
f(x>>*dx, which is less than yap* by suitable choice of f
minimum
complexity
estimators.
in the e-net. As in the previous case it follows that the
Remarks:
In
the
Examples
2, 3, and 4, we permitted
index of resolvability satisfies
the lengths L,(q) to depend on the given sample size.
1
Nevertheless, by paying a price of order (loglogn)/n,
R,(P) s ,H’ + Y*E*,
comparable resolvability can be achieved using lengths
L’(q) which do not depend on n. The advantage is that
and optimizing the choice of Eyields R,( p) = O(n -2r/(2r+ I)>
the growth and domination conditions (7.31, (7.41, and
as before.
(7.6) which are used in Theorems 1, 2, and 3 will then be
As a consequence of this bound on the index of resolvsatisfied. To construct such an assignment of description
ability (and by application of Theorem 4, Section VII), we
lengths L’(q), we first note that positive integers k can be
see that the minimum complexity density estimator, speencoded using 210gk + c bits where c is a constant.
cialized to the current case, converges to the true density
G iven I, and L,(q) for n = 1,2,. . ., define a new list
in squared Hellinger distance at rate n-2’/(2r+1), uniI’= lJ k12k to be the union of the sets for indices equal
formly for all densities in the Sobolev class Wi +. Now
to powers of two and define, for q E I?,
when both p and q are bounded and bounded away from
(6.27)
L’(q) =Lnk(q)+21wlognk
+c,
zero (here l/y <p(x)<
y and l/y* I q(x)< y*> the
squared Hellinger distance, the relative entropy and the with nk = 2k, where k is the first index such that q E r2k.
integrated squared error are equivalent to within a con- It is seen that L’ satisfies Kraft’s inequality on I’. With L’
stant factor: indeed, /‘(fi - fi)” I D(pllq) I j(p - qj2/
in place of L, we achieve resolvability satisfying R’,(p) I
q I y*/(p - qj2 I 4y4/(& - &)*.
It follows that the ((d /2) log n + 2 log log n + O(l>>/n in the parametric
density estimator also converges in relative entropy and case. In general, since between the powers of two the
L,(q) = H,, we obtain the following bound on the resolv-

ability

IEEE

1046

TRANSACTIONS

resolvability R’,(p) = min(L’(q)/n + D(pllq))
is never
more than twice the resolvability at the next power of two,
we conclude that R’,(p) 2 O(RJp) + (log log n’>/n’),
where n’ = 2[‘ognl. In particular, when R,(p) is of larger
order than (log log n>/n, the overall rate is unaffected by
the addition of the (loglogn)/n term, so it follows that
R’,(P) = O(r,dp)).

For practical estimation of a density function, we are
more inclined to use sequences of parametric families as
in Case 3, instead of using the “fully nonparametric”
estimators as in Case 4, despite the fact that for a large
class of functions the index resolvability tends to zero at a
slightly faster rate in Case 3. There are two reasons for
this. Firstly, the metric entropy theory does not provide
an explicit choice for the net of density functions with
which we can compute. Secondly, with sequencesof parametric families, while converging at a nearly optimal rate
even in the infinite-dimensional case, we retain the possibility of delight in the discovery of the correct family in
the finite-dimensional case.
RESULTS
VII. THECONVERGENCE
In this section we present our main theorems establishing convergence of the sequence of minimum complexity
density estimators. The first three theorems concern the
statistical consistency of the estimators. Bounds on rates
of convergence are given in Theorem 4 and its corollary.
Conditions: For each of the results, one or more of the
following conditions are assumed. G iven a sequence of
lists I,, and numbers L,(q) for densities q in I,,, let
r = LJ.r,. Set L,(q) =oo for g not in r,.

There exists a constant b > 0 such that
for all n.
c 2--Ln(q)5 b,
(7.1)

Summability:

g E r,
Light tails: There exist constants 0 < cr < 1 and b’ such

that
x2-

~&t(q)-< b’,

for all 12.

(7.2)

= 0,

foreveryqEr.

(7.3)

<co,

for every q E r.

(7.4)

4 E r,
Growth restriction:
&z(q)

limsup n
n
Nondivergence:

limsupL,(q)

n

Nondegeneracy:

for all q E I, and all n,
Domination:

such that
L(q) I L,(q)

for some constant I > 0.

There exists L(q),‘q

(7.5)

E I and a constant c

+ c, for all q and all n and c 2-L(q) I 1.
4
(7.6)

ON INFORMATION

THEORY,

VOL.

37, NO. 4, JULY

1991

Remarks Concerning the Conditions: The main condition for all of our results is the summability condition
(7.1). It is implied by Kraft’s inequality in the data compression framework or it is implied by the requirement of
a proper prior in the Bayesian framework. This condition
(or the closely related condition (7.6)) is used to obtain
the results of Theorems 1 and 2 on the consistency of the
estimator of the distribution. The somewhat more stringent assumption (7.2) is used to get the rate of convergence results for the estimator of the density. The
Corollary to Theorem 4 shows how this more stringent
condition can be circumvented by restricting the minimization to densities that are not excessively complex.
Either the growth restriction (7.3) or the boundedness
(7.4) is used with the almost sure results (Theorems 1, 2,
3), but they are not needed for the main result (Theorem
4) on the rate of convergence in probability. For condition
(7.5), the constant 1 can be taken to equal 1 when the
lengths L,(q) are positive integers.
For given L(q) and I that do not depend on n, if
Cq2-L(q) 2 1 and if I contains more than one point, then
all of these conditions are satisfied except perhaps for the
tail condition (7.2). A modified criterion with AL(q) used
in place of L(q), where A > 1 is a constant, is seen to
satisfy all of the conditions, provided Cq2-L(q) I 1. In
particular (7.2) will hold with (Y= l/h. Note that this
modification will not increase the index of resolvability by
more than the factor h. In particular R,(p) will have the
same rates of convergence.
For the case of complexity constrained maximum likelihood estimators in Cover [Ml, the density estimate fi,, is
selected by maximizing the likelihood in I,, where
5, r,, . . . is an increasing sequence of collections of
densities. This is a special case of minimum complexity
density estimation with L,(q) set to a constant on I,,. We
impose the cardinality restriction log IllY,ll= o(n). In this
case we set L,(q) = 210g IllY,llfor q E I, and 00otherwise.
Then conditions (7.1), (7.2), (7.3), and (7.5) are satisfied,
so all of the convergence results except Theorem 1 hold
in this case. Even if the collections I’,, are not increasing,
the conditions are still satisfied for Theorem 4. The
proofs of the theorems are in Section VIII.
Let X,, X2, . * * be independent and identically distributed with probability density function p(x). Let fi, be
the minimum complexity density estimate defined by (3.3).
Thus B,, achieves

min (L,(q)
4 E r,

+lwl/q(X”)).

(7.7)

Theorem 1 (Discovery of the true density): Assume L,
satisfies the nondivergence condition (7.4) and the domination condition (7.6). If
Per,
(7.8)
then
A-P,
for all sufficiently large n, with probability one.

(7.9)

Thus, in the important case that I = I”, if the data are
governed by a computable law then this law eventually

BARRON

AND

COVER:

MINIMUM

COMPLEXITY

DENSITY

will be discovered and thereafter never be refuted. However, although the estimator eventually will be precisely
correct, it is never known for any given sample size
whether the true density has been discovered.
Next we present convergence properties that do not
require that the true density be in I. It is assumed to be
an information limit of such densities. The next result
establishes convergence of the estimated distributions.
Theorem 2 (Consistency of the minimum complexity estimator of the distribution): Assume L, satisfies the

summability condition (7.1) and the growth restriction
(7.3). If p E I, then for each measurable set S,
with probability one. (7.10)
lim PJ S) = P(S)
n-m
Assuming that X is a separable Bore1 space, it follows
that, with probability one,
A

(7.11)

P, * P

1047

ESTIMATION

E > 0, there is a c > 0, such that P{Yn /R, > c} I E for all
large n.
The following result relates the accuracy of the density
estimator to the information-theoretic resolvability. It is
this result that demonstrates the importance of the index
of resolvability for statistical estimation by the minimumdescription length principle.
Theorem 4 (Convergence rates bounded by the index of
resoluability): Assume L, satisfies the tail condition (7.2)
and the nondegeneracy condition (7.5). If lim R,(p) = 0,
then b,, converges to p in Hellinger distance with rate
bounded by the resolvability R,,(p), i.e.,
d$( p,B,)

,< R,(P)

in probability.

(7.16)

in probability.

(7.17)

Moreover,

L( A>

------RR,(p)
n

Remarks: The conclusion (7.16) has recently been
strengthened in [17] (building on the proof technique
In Barron [43] a technique is developed that shows developed here in Section VIII), to yield that for all n 2 1,
convergence of a sequence of distance functions stronger
than distances corresponding to weak convergence but
not as strong as convergence in total variation. See the where c is a constant. A bound on the constant obtained
in [17] is (2+4(1+(b + e-‘>/l>/(la))/loge.
remark following the proof in Section VIII.
A consequence of Theorem 4 for the classes of densiThe next two results show convergence of the density
estimates in L’ and hence convergence of the distribu- ties considered in Section VI, is that the minimum comtions in total variation. However, the stronger summabil- plexity density estimators converge at rate l/n, (log n)/n,
((log n)/n)2r/(2r+‘)
or n-2r’(2r+‘), respectively. To obtain
ity condition (7.2) is required.
these rates, the lengths L,(q) used in Section VI are
Theorem 3 (Consistency of the minimum complexity estireplaced by AL,(q) where A > 1, so that the tail condition
mator of the density): Assume L, satisfies the tail condi(7.2) is satisfied, or we use the modification indicated
tion (7.2) and the growth restriction (7.3). If p E I!, then
below.
with probability one,
If weights 2--Ln(q)are summable but do not satisfy the
tail
condition, we show how a slight modification results
lim lp-@,I=0
(7.12)
n-m /
in a convergent density estimator. Fix A > 1 (in particular,
and
we suggest h = 21, and let L’,^) be the value of L,(q) for a
density that achieves min, (h L,(q) + log l/q(X”)).
Now
(7.13)
~
I
define
$,
to
be
the
density
that
achieves
the
minimum
of
n
n-tm
L,(q) + log l/q(X”)
subject to the constraint that
Let d$(p, 4) = /(fi - 6)” denote the Hellinger disL,(q) 5 2i’,“‘. Thus
tance. Convergence of densities in L’ distance and conj, = arg 4: L ~f~2ir”i(l,(q~
vergence in the Hellinger distance are equivalent as is
+lowq(Xn))~
(7.18)
n - n
evident from the following equalities (Pitman [44, p. 71)
where ties are broken in the same way as for 6, (by
(7.14)
choosing a minimizing density with least L,(q)). Here the
constant 2 could be replaced by any constant c > 1.
The Hellinger distance is also related to the entropy
Observe that if the minimum complexity density estidistance. Indeed d$(p, s> I /p In p/q and if p(x)/q(x)
mate fi, has length L,(p,) less than 2~?‘,“‘,then the
* 1 in sup norm, then
resulting estimate is unchanged, i.e., fi, = 8,. The intention of the modification is to change the estimate only
(7.15)
when unconstrained use of the criterion would result in a
density with complexity L,(p,) much larger than the
in the sense that the ratio of the two sides converges to
complexity of densities that optimize the resolvability.
one.
Corollary to Theorem 4: Suppose L, satisfies the
For sequences of positive random variables Y,, the
summability.condition (7.1) and the nondegeneracycondinotation Y, < R, in probability is used to denote convertion (7.5). Let 8, be defined by (7.18). Then
gence in probability at the indicated rate. This means that
in probability.
(7.19)
the ratio Y, /R, is bounded in probability, i.e., for every
d?&dn)
<R,(P)

in the sense of weak convergence.

lim

L(hJ
-=

o

di%p>q)~
jlp-qk2d,(p,q).

IEEE

1048

TRANSACTIONS

Moreover,

ON INFORMATION

THEORY,

VOL.

37, NO. 4, JULY

1991

of events bound,
P{$,#pforsomen>k}

L( ii)

in probability.

-<R,(P)
n

(7.20)

VIII. PROOFS
The minimization of L,(q)+log l/q(X”)
is the same
as the maximization of q(Xn)2-Ln’q’. We shall find it
mathematically convenient to treat the problems from the
perspective of maximizing q(X”)2-Ln’q’.
A tool we will use repeatedly in the proofs is Markov’s
inequality applied as in Chernoff [45] to yield the following inequalities:
P{ p( Xn) I cq( X”) and X” E B}

I cQ( p( X’) 2 cq( Xn) and X” E B},

(8.1)

for any measurable set B in X” and any constant c > 0,
in particular
P( p( xy

5 cq( X”)}

I c,

(8.2)

I q( X”)2-Ln(q)

for some n 2 k}

= iP(A$J)),
4

(8.7)

where the sum is for q in I with q # p. Here A(k4)is the
event that Q(X”)~-~,(~) I q(X”)2-Ln’q’ for some n 2 k.
We will show that the probabilities P(Ap’) are dominated by a summable bound 2--L(q)+c+cgand that they
converge to zero as k + ~0 for each q.
First we show the domination. To exclude small n for
which L,(p) may be infinite, we use condition (7.4) to
assert that given p there exists c0 and k, such that
L,(p) I c0 for all n 2 k,. Consider k 2 k,. Momentarily
fix q. The event A$$ is a disjoint union of the events
occurs for the
A n,k, that p( X”)2-Ln(p) I q(X”)2-Lx(q)
first time at n (i.e., the opposite inequality obtains for
k, 4 n’ < n). Then, by inequality (8.1) and condition (7.61,
P( A(k4)) I P( Ap;)

and, in the same manner,
PI P(X”)

I C P{p( X”)2-Ln(P)

S cq(X”)J

= jlk

= P{(p(X”))1’2~c1~*(q(x~))1’2}
<

5 pw*

fvn,k,>
0

co
c Q( An,ko)2-Ln(q)+L”(P)
n = k,

I 2-~&wW*&‘*

where p = /(pq)*/* and d(p,q)
ple of the Hellinger distance
d*(p,q)

,

(8.3)

I

is defined to be a multi-

=j(fi-\l;;)*loge.

f

Q( An,k0)2~L(q)+c+c~

n = k,
<- 2-Ud2c+c,*

(8.4)

(8.8)

This bound is summable for q in I, so it gives the desired
domination.
Now we show convergence of the probabilities P(A’,4’)
to zero as k + ~0. By inequality (8.3), the event
I q( Xn)2-Ln(q)} has probability bounded
{p(x”)2-LJp)
by 2-nd2(p,q)2Cu/2that is exponentially small. Whence by
the Borel-Cantelli Lemma, P(A’,4)> tends to zero for
each q # p.
By the dominated convergence theorem, as k +m, the
limit of the sum in (8.7) is the same as the sum of the
limits. Consequently,

The inequality log p< -d*/2 follows from (l/2)/(&
&>” = 1 - p and log p I (p - 1)log e. The factor of log e
in (8.4) is chosen for convenience so that all exponents in
(8.3) are base 2.
We note here that these inequalities are applied in
each case with c proportional to 2--Ln(q).The summability
of the resulting bounds in (8.1) and (8.21, summing over q
in I,, is key to the proof of consistency of the minimum
complexity estimator. The presence of the fractional power
of c in the bound (8.3) forces more stringent summability
P{ @ , # p infinitely often} = 0.
hypotheses to be imposed to get the rate of convergence This completes the proof of Theorem 1.
q
results.
Remark: Two other proofs of this theorem can be
Proof of Theorem 1: We are to show that
found in Barron [16], based on martingale convergence
P{ b, f p infinitely often} = 0.
(8.5) theory. The present proof shares the greatest commonality with the developments forthcoming.
For a decreasing sequence of sets, the probability of the
For the proofs of Theorems 2 and 3 we will use the
limit is the limit of the probabilities. Thus
following.
Lemma I: Suppose L, satisfies the growth restriction
P{ fi, # p infinitely often}
(7.3). If p E r then for any E > 0, if fi E I satisfies
= ,llmP{ fi, # p for some n 2 k} . (8.6)
D(pllfi)
< E, then
For 8, to not equal p, it is necessarythat P(X”)~-~,‘~) 5
q(X”)2-Ln’q’ for some q # p. Consequently, by the union

for all large n , (8.9)
with probability one. Moreover, for any positive sequence
2-LJJj)j(

X”)

2 p( x,)2-,,,

BARRON

AND

COVER:

MINIMUM

COMPLEXITY

DENSITY

1049

ESTIMATION

c, for which lim c, /n = 0, the left side of (8.9) exceeds events bound and (8.1) to obtain
the right side by at least the factor 2”n, for all large n,
P( A,) I P( A, n B,) + P( B:)
with probability one.
Proof of Lemma 1: Taking the logarithm and dividing
by n, the desired inequality (8.9) is seen to be the same as

-ua + -1log ~P(X”>
~
n

n

Jqxy

<E,

for all large n, (8.10)

with probability one. This is true by application of (7.3)
and the strong law of large numbers. The second claim
0
follows in the same way.
Remark: We note that the left side of (8.10) is an upper
bound to the pointwise redundancy per sample defined by
n ( cornPare with 5.7). Thus a
(B(X”) - log l/PW>>/
consequenceof the Lemma is the following.
Corollary to Lemma 1: If (7.3) is satisfied and if p E ?,
then the pointwise redundancy per sample (B(Xn)logl/p(X”))/n
converges to zero with probability one.
Proof of Theorem 2: We are to show that if p E !?,

then
with probability one,
lim PJ S) = P(S)
n-a
for arbitrary measurable subsets S in X. Toward this end,
given any 6 > 0, choose 0 < E < S/2 and choose- j E I
such that D(pllfi) <(l/2)6* loge. Then /P(S)- P(S)/ <
(1/2)jlp - fit< (1/2)~. From Lemma 1 we have
2-L,qj(

x7

> p( Xn)e-&*,

for all large n ,
(8.11)

I CP(A$%

B,)+

P(B;)

I c2- Ln(q)ene2/2Q( A’,4’f~ Bn) + P( B,‘)
4

<x2- LGi)ene=/*e- nt6-e)‘/2 + p( B;)
4
5 be-“’ + e-“&*,
(8.15)
where the sum is for all q in I?, with IQ(S)- P(S)1 2 6.
Here r = ((6 - cl2 - ~*>/2, which is strictly positive by
the choice of E. Thus P(A,) is exponentially small. Using
the Borel-Cantelli lemma and combining (8.11) with (8.13)
we have
2-Lnta)g( X’) > max q( Xn)2-Ln(q),

for all large n,

4

(8.16)
with probability one, where the maximum is for all q in I,
with IQ(S)- P(S)1 2 6. Thus there exists densities in I’,
with IQ(S)- P(S)/ < 6 that have a larger value for
q(X”)2-Ln(q)
than all q with IQ(S)- P(S)/ 2 6. Consequently, the minimum complexity estimator, which is defined to achieve the overall maximum, must satisfy
for all large n, (8.17)
I~n(s)-P(s)l<s,
with probability one. Since 6 > 0 is arbitrary, it follows
that, with probability one,

lim PJS) = P(S),
n-t’=
with probability one.
Let N(S, Xn) = Cr= ilIx, E sJ be the number of observa- for any measurable set S in X. Consequently, for any
tions in S. Then N(S, X”) has a binomial (n, P(S)) distri- countable collection G of sets, we have
bution when the Xi are independent with distribution P,
P limPn(S)=P(S),forallSEG
=l. (8.18)
whereas it ,would have a binomial (n, Q(S)> distribution if
1
i n+m
the Xi were independent with distribution Q . Define the
Assuming that X is a separable Bore1 space (e.g., the real
set
line), it follows that there exists a countable collection of
B =
WS,X”)
sets
that generates the Bore1 sigma-field. Applying (8.18)
(8.12)
n
n
to this countable collection, it follows that
Then the Hoeffding [46] or by standard type-counting
arguments in information theory, P(B,“) I 2ehn2” and
Q(B,)
5 e-ntS-d2/2 uniformly for all Q with IQ(S)PWI 2 6, where B,’ denotes the complement of the event
B,. (Thus (8.12) defines the acceptance region of a test
for P versus {Q: IQ(S)- P(S)1 2 6) that has uniformly
exponentially small probabilities of error, [43].)
We want to show that with high probability
(8.13)
4
where the maximum is for all q in I, with IQ(S)P(S)1 2 6. Let A, be the event that (8.13) does not occur:
this is a union of the events A$) defined by
p( Xn)e-ne2/2

> max q( Xn)2-Lff(q),

A~)={p(X”)e-“‘*/2sq(Xn)2-Lncq)}.

(8.14)

To bound the orobabilitv of A.. we use the union of

P{& - P} = 1,
where =j denotes weak convergence.

(8.19)
0

Remark: A similar proof using more elaborate hypothesis tests, as in Barron [43], shows that

lim C jPJS)n+m.sE.rr,

P(S)I=O

with probability one,
(8.20)

for any sequence of partitions r,, of X for which the
effective cardinality is of order O(n).
Proof of Theorem 3: Here we show almost sure convergence of the minimum complexity density estimate, in
Hellinger distance, and almost sure convergence of
L,(b,)/n,
for weights 2 -Ln(q) that satisfy the tail condition (7.2).

IEEE

1050

TRANSACTIONS

Note that since C2-cuLn(q)is decreasing in (Y, condition
(7.2) is unchanged if it is assumed that l/2 5 cy< 1. G iven
S>O and 1/21cu<l,
set O<e<S(l--(Y).
For PET
there exists a density ~5E I with D(pIIj) < E so that
d*(p,fi) < E < 6. Then by Lemma 1,
for all large n, ‘(8.21)
with probability one. Consequently, to show that
d*(p, b,> < 6 and L,(fi,) < nS, it is enough to show that
for all large n ,
p( X,)2-,’ > maxq( Xn)2PLJq),
2-L+?(

xn> > p( x,)2-,,,

4

(8.22)

with probability one, where the maximum is for all q with
d*(q, p) 2 6 or L,(q) 2 nS. Using the Bore&Cantelli
lemma and the union of events bound, it is enough to
show that the following sum is exponentially small:
~P{p(X”)2-“‘<q(X”)2-“L~,Cq’},
9

(8.23)

ON INFORMATION

VOL.

37, NO. 4, JULY

1991

The following result will be useful in the proof of
Theorem 4.
Lemma 2: Let p and q be any two probability density
functions on X and let Xi, * . ., X,, be independent random variables with density p or q. Then

D( pIIs> + 1 log e

P{X”EB}SQ{X~EB}~“‘+

r

nr

e ’
(8.28)

for all measurable subsets B of X”, all r > 0 and all n.
Proof: The inequality is trivial if D(pllq) is infinite.
Now suppose D(pllq)
is finite. Let A, ={p(X”><
q(X”)2”‘}
and B, = {X” E B}, then as in (8.1),
P(B,)

2 P(A,n

B,)+

< Q( BJ2”’

P(A’,)

+ P( A”,).

(8.29)

Now by Markov’s inequality,
P(A”,)

where the sum is for all q with d*(q,p> 2 6 or L,(q) 2 nS.
For the terms in the sum with L,(q) 2 nS we use the
upper bound from (8.2):
2-Ll(q)2n~ 5 2- aL,Go-n(S(l -al-t).
(8.24)
These terms have a sum less than b2-“(‘(l-“)-“),
which is
exponentially small by the choice of E. For the terms in
the sum with d*(p, q) r 6 we use (8.2) and (8.3) to obtain
the upper bound:
min { 2-Ln(q)2ne,2-L,,(q)/*2-n(S-E)/* 1

THEORY,

= P{logp(Xn)/q(Xn)

>nr}

~,(l~gp(x”)/q(x”))
nr

+

I

I nD(pllq) +(lwe)/e
nr

(8.30)

>

where we have used the fact that the expectation with
respect to P of the negative part of logp(X”)/q(X”)
is
the expectation with respect to Q of (p(X”)/q(X”))
.(log p(X”)/q(X”))that is bounded by (l/e>log e. Together (8.29) and (8.30) prove the lemma.
0

4 (2-L,(q)2~e)*“-‘(2-L,(q)/22-n(6-c)/*)*(’-o)

Proof of Theorem 4: We show that if the weights
2-Ln(q)
satisfy the tail condition (7.2) and if the resolvabil>
ity
R,(p)
tends to zero, then the minimum complexity
where we have used the fact that min{c,, c2} 5 c~c:~” for
density
estimate
fi, converges in squared Hellinger dis0 I p 2 1 and any positive ci, c2. This bound also has a
tance
with
rate
bounded
by R,(p) in probability. Also
sum less than b’2-“(“(‘-“)-‘I
that is exponentially small.
L,(
fin>/n
converges
with
rate
bounded by R,(p).
Therefore, (8.22) is established. From (8.21) and (8.22)
Choose
fi,,
to
achieve
the
best resolution R,(p) =
we deduce that all maximizers 6, of q(X”)2-Ln(q) must
L,(3,)/n
+
D(pllfi,>.
Let
l/2
5
a < 1 be such that consatisfy
dition
(7.2)
is
satisfied.
For
c
>
1,
let
‘Lmz) < s
for all large n,
d2(j?,,p)
<S and ~
>
= 2--cuL,(q)2--n(S(l--a)--tu)

(8.25)

n

B, = {d*( p,B,)

(8.26)

with probability one. Here 6 > 0 is arbitrary. Consequently,
lim d*(fi,,p)=O
n+m
with probability one.

and

lim UAJ
p=
n
n+m

o’
,
0

(8.27)

If c, > 0 is any sequence with lim c, /n = 0,
then by the same reasoning, with the second claim of
Lemma 1 used in place of (8.21), it is seen that the value
of q(X”)2- L~(q)at fi will exceed the maximum value for
all q with d*(q,p) 2 6 or L,(q) 2 nS by at least the
factor 2”n for all large n, with probability one. Consequently, every density that achieves within c, of the
minimum two-stage description, will simultaneously satisfy (8.26) for all large ~1,with probability one. That is,
they are all close to the true density p, and none of them
has complexity larger than nS.
Remark:

> 4cR,,( p)/(lL(

&J/n

a) or

> cR,( p)/(l-

a)}.

(8.31)

The factor of l- (Y in the denominators is for convenience in the proof. G iven E > 0, we show that P(B,) has
limit less than E,for c sufficiently large. Applying Lemma
2 with r = (c - l)R,(p)/2
and Q = p, and using R,(p) 2
NPII~,),

we

have

P( B,) I pn( B,)2(C-1)“Rn(p)‘2 + &
2
+ (c-l)nR,(p)

log e
e

’ (8’32)

Next we bound the p,, probability of the event B,. Using
the triangle inequality d(p, fi,,) 5 d(fi,, fi,)+ d(p, fi,> and
d(p,j,)
I ,/m
I Juno),
it is seen that B, is a
subset of the event
in = {d*(&,A)

> cR,(p)/(lL,(b,)/n

a) or
> cR,(p)/(l-

u)}.

(8.33)

1051

BARRONANDCOVER:MINIMUMCOMPLEXITYDENSITYESTlMATION

For the event L?, to occur there must be some q with
d2(S,, q) > cR,(p)/(la> or L,(q)/n > cR,(p)/(la>
for which the value of 2-Ltl(q)q(X”) is at least as large as
the value achieved at fi,. Thus by the union of events
bound

event of probability less than b’2-(c~1-co)1/2 +
(2/(c - 1 - c,))(l + (log e>/el>, for c - 1 > ca 2 0.
Consequently, except in this event of small probability, all densities that achieve values of L,(q)+
logl/q(X”)
that are within c,nR,(p) of the minimum will satisfy d2(p, q) I 4cR,(p)/(l(u) and
L,(q)/n

(8.34)
where the sum is for q with d2($,,q)>
cL?,(p)/(l- a)
or L,(q)/n > cR,(p)/(la). As in the proof of Theorem 3, the terms in this sum are not greater than
min {2- L,,(q)+L,(b,,)
>2-(L,~(q)+Ln(6,,)-ndZ(~~,q))/2
I
2 2-“L,‘4’2- c%(P)2UD,)~

(8.35)

Summing this bound, using (7.2) and L,(fi,J 5 nR,(p),
yields
p,l( in) I b’2-‘“p WL(P).
(8.36)
Plugging this result into (8.32) and using L,(fi,) 2 1 by
condition (7.5), we obtain
log e
2
p( B,) _<b’2-‘“- 1)~~R,(p)/2
+ -& +
(c - l)nR,( P) e
2
2
log e
~
5 b’2-(C-l)‘/2 + __
(8.37)
c-l + (c-1)1
e ’

a) From (8.37) we have a bound on the probability of
interest that holds uniformly for all densities p, for
all sample sizes IZ, for all L,, and for all l/2 < a < 1
I b’ and L,(q) 2 I, namely,
satisfying C,2- olLn(q)
P(d”( p,A)

> 4cR,(~)/(l-

a> or

L,(fi,)/n>cR,(~)/(l-cu)}
2
2
___
< ),‘2-(-1)‘/‘2 + c-l + (c-1)1

a>.

Proof of the Corollary to Theorem 4: Assuming only
that C2~L~~(q)
I 1, we are to show that the density j,, that
minimizes L,(q)+ log l/q(X”)
subject to L,(q) I 2L,
will converge in squared Hellinger distance at rate
bounded by R,(p) in probability. Here i,, is the length
L,(B,) for a density p^, that achieves the minimum of
A L,(q) + log l/q(Xn)
where A > 1.
First we verify that $, achieves a value of AL,(q)+
logl/q(X”)
that is within (A - l>L, of the minimum.
Indeed, AL,(j,) + log l/jn(Xn) is equai to (A - l)L,(j,)
+min{L,(q)+logl/q(X~“):
L,(q) < 2L,), which is less
than or equal to (A - 1)2L, + L,($,) + log l/fi,(X”).
This
last expression reduces to (A - l>L, + AL,($,) +
log l/$JXn)
as desired.
Now, setting c,, = (c - 1)/2, we have
P(d2(d,)

> CR,(P)}

5 P(d2(p,$,,)

> C&(P)

and

Taking c sufficiently large yields P(B,) 5 E. This com0
pletes the proof of Theorem 4.
Remarks:

I cR,(p)/(l-

(8.39)
The first event on the right is included in the event that
CR,(~) for some density that achieves within
of the minimum of AL,(q)+logl/q(X’);
by
Remark d), this event has a probability that is made
arbitrarily small by the choice of c sufficiently large. Also,
the second event on the right has small probability for c
large, by direct application of Theorem 4. This completes
0
the proof of the corollary.
d2(p,q)>
c,nR,(p)

AND CLASSIFICATION
IX. REMARKS ON REGRESSION
log e
The results in this paper have been developed in the
e ’
context
of density estimation. Nevertheless, it is possible
(8.38)
to apply the convergence results to problems in nonparaI b’ holds for some metric regression and classification. For instance, in reb) If the tail condition C2-“~~‘-~~(q)
sequence (Y, = 1- l/c,, where c, + ~0,and c,R,(p)
gression it might be assumed that the data is of the form
+ 0, then d2(p,j3,) and L,($,)/n
converge in xi=<q,y),
~1, where the input random varii=l;..,
probability at rate bounded by c,R,(p).
ables U, are drawn from a design density p(u) and the
cl A consequence of the previous remark is that if output random variables Y, are conditionally distributed
2-Ln(q) are weights that satisfy the summability con- as Normal( f (u>,g2> given that Ui = U. Suppose the error
dition (7.1) but not the tail condition (7.2), then by variance cr2 is known. The conditional mean f(u) is the
replacing L,(q) with (l+ l/c,)L,(q),
new weights unknown function that we wish to estimate. Assigning
are obtained for which the minimum complexity complexities L(g) to a countable set of candidate funcestimator will converge at rate bounded by c, R,(p).
tions g, we select fz, to minimize
d) With a slight modification of the proof of Theorem
4, it is seen that the value of 2-Lfl(q)q(X”) at $, will
(9.1)
L(g) + & ,C (Y,- g(Q))21we.
exceed the maximum value for all densities with
1=1

d2G,, q) > cR,(p)/(l-

(l-

a> or L,(q)/n

> CR,,(P)/

a) by at least the factor 2’(~“~*(~),except in an

This f: is the minimum complexity regression estimator.

IEEETRANSACTIONSONINFORMATIONTHEORY,VOL.37,NO.4,JULY1991

1052

The index of resolvability in this context equals

L(g)
+1
Rn(f)
=m:(~
n

ZaZIlf - Al2 loge , (9.2)
1

where IIf - g112= /(f(u)g(u>j2p(u) du (here the relative entropy reduces to a multiple of the L2 distance).
Using results for the L2 approximation rates for smooth
functions, as in Cox [47], bounds on the index of resolvability can be obtained that yield the same rates of
convergence as we have given for density estimation. For
instance, consider least squarespolynomial regression with
the degree of the polynomial automatically determined by
the minimum complexity criterion. If p(u) is bounded and
has bounded support on the real line and if the rth
derivative of f is square integrable then R,(f) I
O(((log n)/n)2”(2” “1.
By Theorem 4, the squared Hellinger distance be!ween
the densities that have conditional mean functions f,, and
f converges to zero in probability with rate bounded by
R,(f)
(provided L(q) is chosen such that C2--“lL(g) is
finite for some 0 < (Y< 1). The squared AHellingerdistance
in this context is seen to equal /cl- e(f~(U)-f(U))Z’8u2)p(~)
from which it is straightforward to obtain the lower bound
clmin((fn(u)f(u>>2,8u2>p(u)du,
where c = (1; e-l>/
8a2. Consequently, the squared distance / min(( f, - f j2,
8a2) converges to zero in probability with rate bounded
by the index of resolvability.
Similar results hold for classification problems. Consider for instance the two-class case with class labels
Y E {O,1). Here (ul,,Y), i = 1,2; . ., y1 are independent
copies of .the random pair (U, Y >. The conditional probability f(u) = P{Y = 1lU = u} denotes the optimal discriminant function that we wish to estimate. Suppose complexities L(g) are assigned to a countable set of functions
g(u) each with range restricted to 0 5 g 2 1. (For instance, these functions may be obtained by logistic
transformations of linear models, g(u) = l/(1 +
exp( - CO,+=
l+j(u>>, where the +j are polynomial or spline
basis functions and the ej are restricted to (1/2)log IZ bits
accuracy. The dimension d is automatically selected by
the minimum complexity criterion.) It is seen that the
minimum complexity estimator selects f: to minimize
1
t (l-yi)log.
L(g)+- 5 r, log &+
I

i=l

i=l

l-&+4>

The index of resolvability in this classification context is
R,(f)

L(g)

= min n
g

f(u)
-+(I-f(u))b
g(u)

log (1 - f(u)> are square integrable, then R,(f > 5
O(((log n)/nP”Q ’+ “I.
By Theorem 4, the square of the Hellinger distance,
and hence also the square of the L1 distance /p(u)1 f(u) fi(u)l, converges at rate bounded by the index of resolvability R,( f ). From accurate estimates of the discriminate
function, good classification rules are obtained. Indeed,
let P, be the Bayes optimal probability of error, which
corresponds to the classification rule that decides class 1
if and only if f(u) 2 l/2, and let P:“) be the probability
of error for the rule that decides class 1 if and only if
h(U) 2 l/2. It can be shown that IPJ”) - P,l I
2/p(u)l&u)f(u>l. Consequently, P,‘“) converges to the
optimal probability of error at rate bounded by vlR,cf,.
The convergence results for minimum complexity regression and classification estimators are particularly useful for problems involving complicated multidimensional
models, such as multilayered artificial neural networks,
see [17], [48], [49]. The minimum complexity criterion is
used to automatically select a network structure of appropriate complexity.
X. CONCLUSION
The minimum complexity or minimum descriptionlength principle, which is motivated by information-theoretic considerations, provides a versatile criterion for statistical estimation and model selection. If the true density
is finitely complex, then it is exactly discovered for all
sufficiently large sample sizes. For large classes of infinitely complex densities, the sequence of minimum complexity estimators is strongly consistent. An index of
resolvability has been introduced and characterized in
parametric and nonparametric settings. It has been shown
that the rate of convergence of minimum complexity
density estimators is bounded by the index of resolvability.
APPENGIX
DETAILS

ON RESOLVABILITY

INTHE~ARAMETRIC

CASE

Here we verify bounds on the optimum resolvability in
parametric cases that are stated in Section VI.
Let w(0) be a continuous and positive prior density
function on the parameter space and suppose that the
matrix JB (obtained from second-order derivatives of the
relative entropy) is continuous and positive definite. We
are to establish the existence of I, and L, satisfying the
properties indicated in Section VI (Case 2). In particular
I, is to correspond to a net of points, such that for every
f3 there is a 6 in the net satisfying
(e-6)‘Jo(e-e)~

d + o(l)
n

Rates of convergence for R,(f) can be obtained in the
same manner as for density estimation. For instance, in and
the case of the logistic models with polynomial basis L,( pe) = log(/id(n/d)d’2det(J,)1’2)
functions, if p(u) is bounded and has bounded support on
+logl/w(0)
the real line and if the rth derivatives of log f(u) and

+ o(1).

(A.2)

BARRON

AND

COVER:

MINIMUM

COMPLEXITY

DENSITY

The set I, is obtained in the following way. First, the
parameter space is ‘partitioned into disjoint rectangles A
within which the prior density w(0) and the matrix Je are
nearly constant. Then in each set A, an E-net of points e
is chosen such that for every 8 in A, there is a 6 with
(e - eyJ,(e - e;)5 E2. The minimal such net requires
N,(A) points, where for small E,
N,(A) w h,(1/E)dvol(A)(detJ,)!‘2

1053

ESTIMATION

(A.3)

uniformly for all 0 E B, where 6 is the point in the net
that minimizes the left side of (A.6).
Now let 6, be a sequence decreasing to zero and let B,
be a sequence of compact sets increasing to 0. Without
loss of generality IZ*,,~, is an increasing sequence diverging to infinity as k + cc. For each n 2 1, let k, be the last
index such that n 6,,B, I II. Then lim k, = CQ.Setting I, =
l?6%,Bkfl)and L,(q)= Lfkn,Bkn)(q) we have that for all n,
&5)-(A.7) are satisfied with 6, in place of 6, uniformly
on Bkn. Since any compact subset of 0 is eventually
contained in Bkn, this establishes the existence of a single
set I, and length function L, for which (A.11 and (A.2)
are satisfied uniformly on compacts.
Finally, from (A.5) and (A.7) it follows that the index of
resolvability satisfies

and A, is a constant (see Lorentz [50, p. 1531). This
amounts to taking the rotated and scaled parameter vectors < = JAI”0 and finding economical coverings of the
parallelograms {JA1/28.. 8 E A}, using Euclidean balls of
radius E. The constant A, is the optimal density (in points
per unit volume) for the coverage of Rd using balls of
unit radius. Now for large d, it is seen that Ayd/d 1/2rre. [This asymptotic density is found by combining.
R,,(Pn)-<~L,,(P~)+D(PHIIPB)
the bounds of Rogers [51] and Coxeter, Few, and Rogers
4
[52] for the thickness of the optimal covering with the
~~((d/2)logn/cd+log(det(J,)1’2/w(B))
Stirling approximation to the volume of the unit ball, see
Conway and Sloane [53, ch. 1, (18) and ch. 2, (2) and (19)l.
+(d/2)loge+o(l)).
(A.81
Consequently, the constants cd = d/hyd are bounded
independently of d.
where o(1) tends to zero uniformly on compacts.
We let I” consist of the densities pi for 6 in the E-nets
The minimax bound on resolvability now follows as in
of the rectangles. The bound on resolvability will depend Section VI, upon taking w(0) to be proportional to
on E through the terms -(d/n)log~
+(1/2)~~loge for det ( Jo)l12. In particular, for each compact set B c 0,
which the optimum E is seen to .equal Jd7/n, so we now
set E = m
accordingly.
infsup Rn(pn)<i
~logn+log/Bdet(J,)“‘dB
Now we define the codelengths L,(p,). Let W(A)
L,, Lo E B
denote the prior probability of the rectangles A. For
pi E I?, set
-;log~+o(l)
(A.91
i,(P,)

=logl/W(A)+lwN,(A),

(A-4)

for e’in A, for each A in the partition. Clearly,
= 1.
c2- J%PS)
The matrices JA are chosen such that JA is positive
definite and det JA /det Jo is arbitrarily close to one for
all 0 in A. This can be done by a choice of sufficiently small rectangles A because of the assumed continuity
and positive definiteness of Jo. In the same way
w(e)vol(A>/ W(A) is arbitrarily close to one, uniformly
for 0 in A. Moreover, by uniform continuity, these approximations are valid uniformly for all rectangles in a
compact subset of the parameter space. Then from (A.3),
(A.4), and the Taylor expansion of D, we have that for
any given 6 > 0 and any compact set B c 0, there exists
set I(‘,“), codelengths L’,fi,@(q) and n6,B such that for all
n 2 n&B,
IL,(Ps)-log(A,(n/d)d’2(detJ~)1’2/w(e))1<fi,
(A.51
(A.61
and
q

PollPit) 5 yogc

(1+2c?),

(A.71

In this analysis, we used a minimal net of points for
covering the parameter space to a prescribed covering
radius for a locally specified metric, so as to bound the
minimax resolvability. If nets based on other coverings are
used (such as cubes in the locally transformed parameter
&), similar terms still appear involving the Fisher information and the prior density, but somewhat worse constants
are obtained in the minimax bound.
As pointed out by a referee, a different net can yield
improved bounds for the average resolvability,
I wte>u

PO) de.

To bound the average resolvability, it is suggested that
optimal quantization regions (with centroids e> be selected subject to a constraint on the average value for
(f3 - 6>‘J,(f3 - 6) (instead of a constraint on the maximum
value). Indeed, suppose we constrain the averagevalue to
equal e2. Using optimum quantization results as in [531,it
is seen by an analysis similar to that previously given that
the minimum number of quantization points in each set
A is the same as in (A.3) but with (dGd)d/2 in place of
A,, where G , is the coefficient of optimum mean-square
quantization as characterized in [53, pp. 58-591. In particular, lrom a result of Zador, G , N 1/2re for large d.
This yields codelengths L,(pg,) that are the same as

IEEE TRANSACTIONS

1054

ON INFORMATION

THEORY, VOL. 37, NO. 4, JULY 1991

before, but with c> = l/G , in place of cd. Both cd and c> 1271B. S. Clarke, “Asymptotic cumulative risk and Bayes risk under
entropy loss, with applications.” Ph.D. dissertation, Dept. Statist.,
are close to 2re, for large d. Thus for large dimensions,
Univ. of Illinois. Urbana, IL. Julv 1989.
there is not much difference in the codelengths designed 1281R. E. Krichevsky and V. K. Trofimov, “The performance of universal encodings,” IEEE Trans. Inform. Theory, vol. 27, pp. 199-207,
from optimum covering and optimal quantization considMar. 1981.
erations.
Dl H. Jeffreys, Theory of Probability. Oxford: Oxford Univ. Press,
REFERENCES

Ul A. N. Kolmogorov,

“Three approaches to the quantitative definition of information,” Probl. Pereduch. Inform., vol. 1, pp. 3-11,
1965.
121V. V. V’Yugin, “On the defect of randomness of a finite object with
respect to measures with given complexity bounds,” Theory Probab.
Appl., vol. 32, pp. 508-512, 1987.
[31 T. M. Cover, “Generalization on patterns using Kolmogorov complexity,” in Proc. First Int. Joint Conf. Pattern Recog., Washington,
DC, Oct. 1973.
“Kolmogorov complexity, data compression, and inference,”
141 ->
in The Impact of Processing Techniques on Communications, J. K.
Skwirzynski, Ed. Boston, MA: Martinus Nijhoff Pub]., 1985, pp.
23-34.
El T. M. Cover, P. Gacs, and R. M. Gray, “Kolmogorov’s contributions to information theory and algorithmic complexity,” Ann.
Probab.. vol. 17. no. 840-865. Julv 1989.
[61 J. Rissaien, “%deling by &or&t data description,” Automatica,
vol. 14, pp. 465-471, 1978.
“A universal prior for integers and estimation by minimum
[71
description length,” Ann. Statist., vol. 11, pp. 416-431, June 1983.
“Universal coding, information, prediction, and estimation,”
RI
Is
Trans. Inform. Theorv, vol. 30, DD. 629-636, Julv 1984.
“Stochasiic complexit; and moheling,” Ann. St&t., vol. 14,
[91
pp. 1080-1100, Sept. 1986.
“Stochastic complexity and sufficient statistics,” J. Roy.
[lO I
Statis;. Sot. B, vol. 49, pp. 223-239, 1987.
Stochastic Complexity in Statistical Inquiry. Teaneck, NJ:
[ill
fi&
Scientific Pub]., 1989.
[=I C. S. Wallace and D. M. Boulton, “An information measure for
classification,” Comput. J., vol. 11, pp. 185-194, 1968.
1131 C. S. Wallace and P. R. Freeman, “Estimation and inference by
compact coding,,” 1. Roy. Statist. Sot. B, vol. 49, pp. 240-265, 1987.
[141 R. Sorkin, “A quantitative Occam’s razor,” Int. J. Theoretic Phys.,
vol. 22, pp. 1091-1103, 1983.
[I51A. R. Barron, “Convergence of logically simple estimates of unknown probability densities,” presented at IEEE Int. Symp. Inform. Theory, St. Jovite, Canada, Sept. 26-30, 1983.
“Logically smooth density estimation,” Ph.D. dissertation,
Ml
Depth Elect. Eng., Stanford Univ., Stanford, CA, Aug. 1985.
“Complexity regularization,” in Proceedings NATO Advanced
1171 ->
Study Institute on Nonparametric
Functional Estimation,
G.
Roussas, Ed. Dordrecht, The Netherlands: Kluwer Academic
Publ., 1991.
H81 T. M. Cover, “A hierarchy of probability density function estimates,”
in Frontiers in Pattern Recognition. New York: Academic Press,
1972, pp. 83-98.
D91 L. D. Davisson, “Universal noiseless coding,” IEEE Truns. Inform.
Theory, vol. 19, pp. 783-795, Nov. 1973.
DO1R. G. Gallager, Information Theory and Reliable Communication.
New York: Wiley, 1968.
Ml R. J. Solomonoff, “A formal theory of inductive inference,” Inform.
Contr., vol. 7, pp. 224-254, 1964.
Dl G. J. Chaitin, “On the length of programs for computing finite
binary sequences,” .I. Assoc. Comput. Machine, vol. 13, pp. 547-569,
1966.
“A theory of program size formally identical to information
[231
theory, J. Assoc. Comput. Machine, vol. 22, pp. 329-340, 1975.
WI L. A. Levin, “On the notion of a random sequence,” Souiet Math.
Dokl., vol. 14, pp. 1413-1416, 1973.
“Laws of information conservation and aspects of the founDl -1
dations of probability theories,” Probl. Inform. Transm., vol. 10, pp.
206-210, 1974.
D-4 B. S. Clarke and A. R. Barron, “Information theoretic asymptotics
of Bayes methods,” IEEE Trans. Inform. Theory, vol. 36, no. 3, pp.
453-471, May 1990.
-3

1967.
[301 G. Schwarz, “Estimating the dimension of a model,” Ann. Statist.,
vol. 6, pp. 461-464, 1978.
of density functions by
1311 A. R. Barron and C. She”, “Approximation
sequences of exponential families,” Ann. Statist., vol. 19, no. 3,
Sept. 1991.
[321 R. Shibata, “An optimal selection of regression variables,”
Biometrika, vol. 68, pp. 45-54, 1981.
[331 K. C. Li, “Asymptotic optimality for C,, C,, cross-validation, and
generalized cross-validation: Discrete index set,” Ann. Statist., vol.
15, pp. 958-975, Sept. 1987.
theory and an extension of the maximum
1341 H. Akaike, “Information
likelihood principle,” in Proc. 2nd Int. Symp. Inform. Theory, P. N.
Petrov and F. Csaki, Eds. Budapest: Akademia Kiado, 1983, pp.
267-281.
1351 P. Hall and E. J. Hannan, “On stochastic complexity and nonparametric density estimation,” Biometrika, vol. 75, pp. 705-714, 1988.
WJI B. Yu and T. P. Speed, “Stochastic complexity and model selection
II: Histograms,” Tech. rep. no. 241, Dept. of Statist. Univ. of
California, Berkeley, Mar. 1990.
[371 A. N. Kolmogorov and V. M. Tihomirov, “c-entropy and e-capacity
of sets in function spaces,” Uspehi, vol. 3, pp. 3-86, 1959.
[381M. S. Birman and M. Z. Solomjak, “Piecewise-polynomial approximations of functions of the classes W,“,” Mat. USSR-Sbornik, vol. 2,
pp. 295-317, 1967.
[391 U. Granander, Abstract Inference. New York: Wiley, 1981.
[401 J. Bretagnolle and C. Huber, “Estimation des densit&: Risque
minimax”, Z. Wahrscheninlichkeitstheorie venu. Gebiete, vol. 47, pp.’
119-137, 1979.
[411 S. Y. Efroimovich and M. S. Pinsker, “Estimation of square-integrable probability density of a random variable,” Probl. Inform.
Transm., vol. 18, pp. 175-189, 1983.
[421 Y. G. Yatracos, “Rates of convergence of minimum distance estimators and Kolmogorov’s entropy,‘: Ann. Statist., vol. 13, pp.
768-774, June 1985.
powerful goodness of fit tests,” Ann.
1431 A. R. Barron, “Uniformly
Statist., vol. 17, no. 1, Mar. 1989.
[441 E. J. G. Pitman, Some Basic Theory for Statistical Inference. London: Chapman and Hall, 1979.
1451 H. Chernoff, “A measure of asymptotic efficiency for tests of a
hypothesis based on the sum of observations,” Ann. Math. Statist,.,
vol. 23, pp. 493-507, 1952.
[461 W. Hoeffding, “Probability inequalities for sums of bounded random variables,” J. Amer. Statist. Assoc., vol. 58, pp. 13-30, Mar.
1963.
of least squares regression on nested
[471 D. D. Cox, “Approximation
subspaces,” Ann. Statist., vol. 16, pp. 713-732, June 1988.
[481A. R. Barron and R. L. Barron, “Statistical learning networks: A
unifying view,” Computing Science and Statistics: Proceedings of the
20th Symposium on the Interface. Fairfax, Virginia, April 21-23,
1988, E. Wegman, D. T. Gantz, and J. J. Miller, Eds. Alexandria,
VA: Amer. Statist. Assoc., 1988.
[491 A. R. Barron, “Statistical properties of artificial neural networks,”
presented at Proc. 28th IEEE Conf. Decision Contr., Tampa,
Florida, Dec. 1989.
[501 G. G. Lorentz, Approximation of Functions. New York: Holt,
Rinehart, and Winstdn, 1966.
[511 C. A. Rogers, “Lattice coverings of space,” Mathematika, vol. 6, pp.
33-39, 1959.
[521 H. S. M. Coxeter, L. Few, and C. A. Rogers, “Covering space with
equal spheres,” Mathematika, vol. 6, pp. 147-157, 1959.
[531 J. H. Conway and N. J. A. Sloane, Sphere Packings, Lattices, and
Groups. New York: Springer-Verlag, 1988.
[541 A. R. Barron, L. GyGrfi, and E. C. van der Meulen, “Distribution
estimation convergent in total variation and in informational divergence,” to appear in IEEE Trans. Inform. Theory.

