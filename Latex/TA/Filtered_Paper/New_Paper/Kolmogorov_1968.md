International Journal of Computer Mathematics

ISSN: 0020-7160 (Print) 1029-0265 (Online) Journal homepage: https://www.tandfonline.com/loi/gcom20

Three approaches to the quantitative definition of
information
A. N. Kolmogorov
To cite this article: A. N. Kolmogorov (1968) Three approaches to the quantitative definition
of information , International Journal of Computer Mathematics, 2:1-4, 157-168, DOI:
10.1080/00207166808803030
To link to this article: https://doi.org/10.1080/00207166808803030

Published online: 21 Dec 2010.

Submit your article to this journal

Article views: 1089

Citing articles: 141 View citing articles

Full Terms & Conditions of access and use can be found at
https://www.tandfonline.com/action/journalInformation?journalCode=gcom20

International Jourml of Computer Mathematics, 1968, Vol. 2, pp. 157-168
@ 1968 Gordon and Breach Science Publishers

Three Approaches t o the Quantitative
Definition of Information*
By A. N. KOLMOGOROV
Problemy Peredachi Informatsii, Vol. 1 , No. 1, pp. 3-11,1365 (Problems of Information
Transmission)

There are two common approaches to the quantitative definition of
"information": combinatorial and probabilistic. The author briefly describes the major features of these approaches and introduces a new
algorithmic approach that uses the theory of recursive functions.
1. The Combinatorial Approach

Assume that a variable x is capable of taking values in a finite set X
containing N elements. We say that the "entropy" of the variable x is
H(x) = log2 N
By giving x a definite value
x = a

we "remove" this entropy and communicate "information"

I = log, N.
If the variables x , , x,, ..., x, are capable of independently taking values
in sets respectively containing N , , N2, ..., Nk members, then
Transmission of a quantity of information I requires
Here and in what follows f .w g indicates that the difference f - g is bounded,
while f N g indicates that the ratio f : g approaches one.
Reprinted with the publishers permission from Problems of Information Transmission, the Faraday Press, New York, 1001 1.
157

A. N. KOLMOGOROV

I.={

I for integral I

[a + 1 for fractional I

binary digits. F example, the number of different "words " consisting
of k zeros and ones and one two is
2'(k

+ 1).

Hence, the information content of such a message is

I =k

+ log,(k + l),

i.e., the "coding" of such words in a purely binary system requires*

+

I' x k log, k
zeros and ones.
Discussions of information theory do not usually go into this combinatorial approach at any length, but I consider it important to emphasize
its logical independence of probabilistic assumptions. Suppose, for
example, that we are faced with the problem of coding a message written
in an alphabet consisting of s letters, it being known that the frequencies

of occurrence of individual letters in a message of length n satisfy the
inequality
s

It is easy to see that for large n, the binary logarithm of the number of
messages satisfying requirement (2) has the asymptotic estimate
H = log, N - nh.

In transmitting such messages, therefore, it is sufficient to use ayproximately nh binary digits.
A universal coding method that permits the transmission of any sufficiently long message in an alphabet of s letters with no more than nh
binary digits is not necessarily excessively complex; in particular, it is
not essential to begin by determining the frequencies pr for the entire
message. In order to make this clear, it is sufficient to note that by splitting

THREE APPROACHES TO THE QUANTITATIVE DEFINILION

159

the message S into m segments S , , S,, ..., S,, we obtain the inequality.

However, I will not go into the details of this special problem here. It is
only important for me to show that the mathematical problems associated with a purely combinatorial approach to the measure of information are not limited to trivialities.
It is perfectly natural to take a purely combinatorial approach to the
notion of the "entropy of language" if we have in mind an estimate
of its "flexibility," an index of the diversity of the possibilities for
developing a language with a given dictionary and given rules for the
construction of sentences. M. Ratner and N. Svetlova obtained the following estimate for the binary logarithm of the number N of Russian
texts of length n, expressed as the "number of symbols including spaces," composed of words in S. I. Ozhegov's Russian dictionary and
subject only to the requirements of "grammatical correctness"

This is considerably larger than the upper estimate for the "entropy of
literary texts" that can be obtained by various methods of "guessing
continuations." This discrepancy is quite natural, since literary texts
must meet many requirements beyond simple "grammatical correctness."
It is more difficult to estimate the combinatorial entropy of texts
subject to definite, more elaborate constraints. It would, for example,
be of interest to estimate the entropy of Russian texts that could be
regarded as sufficiently accurate (in terms of content) translations of a
given foreign-language text. It is only "residual entropy" that makes it
possible to translate poetry, where the "entropy cost" of adhering to a
given meter and rhyme scheme can be calculated rather accurately. It can
be shown that the classical rhyming iambic tetrameter, with certain
natural restraints on the frequency of syllables, etc., requires a freedom
in handling verbal material characterized by a "residual entropy" of the
order of 0.4 (this estimate is based on the above method of measuring
the length of a text in terms of the "number of symbols, including
spaces"). On the other hand, if we take into account the fact that the
stylistic limitations of a particular genre probably reduce the above

160

A. N. KOLMOGOROV

estimate of the "total" entropy from 1.9 to no more than 1.1 - 1.2, the
situation becomes remarkable both in the case of translation and in the
case of original poetry.
I trust the reader of a utilitarain bent will forgive me this example,
but it should be noted that the broader problem of measuring the information connected wit% creative human endeavor is of the utmost
significance.
At this point, let us turn to a discussion of the extent to which a purely
combinatorial approach permits one to estimate the information conveyed by a variable x with respect to a related variable y. The relation
between the variables x and y, which respectively take values in the sets
X and Y, consists in that not all pairs (x, y) belonging to the Cartesian
product X x Y are "possible." The set U of possible pairs determines
the set Ya of y such that for a given a E X

It is natural to define the conditional entropy by the equation

(where N(YJ is the number of members of Y,) and the information
conveyed by x with respect to y by the formula

For the case shown in the table, for example, we have

Clearly, HCylx) and I(x :y) are functions of x (whereas y takes the form
of a "bound variable ").
It is not difficult to introduce in a purely combinatorial conception
the notion of the "quantity of information necessary to designate an
object x with given requirements imposed on the accuracy of the de-

THREE APPROACHES TO THE QUANTITATIVE DEFINITION

161

signation." (Apropos of this see theextensiveliteratureonthe "&-entropy"
of sets in metric spaces.)
It is obvious that

2. The Probabilistic Approach

The possible advantages of further developing information theory on
the basis of definitions (5) and (6) have been overshadowed by the fact
that if we make the variables x and y "random variables" with given
joint probability distributions, we can obtain a considerably richer system
of concepts and relationships. Paralleling the quantities introduced in
$1, here we have
Hw(x) =

- C ~ ( log2
4 P(x),

(8)

X

As before, H&/x) and Iw(x: y) are functions of x, and we have the
inequalities
H w (x) 6 H(x) HwCvIx) S HOtIx),
(11)
where the equality holds when the corresponding distributions (on both
X and Y,) are uniform. The quantities IW(x:y) and Z(x: y) are not
related by an inequality of a particular direction. As in 1,

The difference lies in the fact that we can form the mathematical
expectations
MHw (Ylx), MZw (x : Y),
while the quantity

Zw (x, y) = MIw (x :y) =MIw (y : x)

(13)

symmetrically characterizes the "closeness of the relation" between
x and y.
However, it should be noted that the probabilistic approach gives
rise to a paradox: In the combinatorial approach, Z(x: y) is always

162

A. N. KOLMOGOROV

content, but Zw(x : y ) may be negative. Now only the averaged quantity
Z,(x, y) is a true measure of the information content.
The probabilistic approach is natural in the theory of information
transmission over communications channels carrying "bulk" information consisting of a large number of unrelated or weakly related messages
obeying definite probabilistic laws. In this type of problem there is a
harmless and (in applied work) deep-rooted tendency to mix up probabilities and frequencies within a sufficiently long time sequence (which
is rigorously justified if it is assumed that "mixing" is sufficiently rapid).
In practice, for example, it can be assumed that the problem of finding
the "entropy" of a flow of congratulatory telegrams and the channel
"capacity" required for timely and undistorted transmission is validly
represented by a probabilistic treatment even with the usual substitution
of empirical frequencies for probabilities. If something goes wrong here,
the problem lies in the vagueness of our ideas of the relationship between
mathematical probability theory and real random events in general.
But what real meaning is there, for example, in asking how much
information is contained in "War and Peace"? Is it reasonable to include
this novel in the set of "possible novels," or even to postulate some
probability distribution for this set? Or, on the other hand, must we
assume that the individual scenes in this book form a random sequence
with "stochastic relations" that damp out quite rapidly over a distance
of several pages?
Actually, we are just as much in the dark over the fashionable question
of the "quantity of hereditary information" necessary, say, for the reproduction of particular form of roach. Still, within the limits of the probabilistic approach, two variants are possible. In the first variant, we must
consider the set of "possible forms" with a probability distribution of
uncertain origin in this set.* In the second variant, the characteristics
of the form are assumed to be a set of weakly dependent random variables. The real nature of the mechanism of mutation provides arguments
favoring the second variant, but these arguments are undermined if we
assume that natural selection causes a system of consistent characteristics
to appear.
Even a purely combiiatorial calculation of the number of possible forms extant
(or once extant) on the earth would give a ridiculously low upper limit (something
like < 100 bits).

THREE APPROACHES TO THE QUANTITATIVE DEFINITION

163

3. An Algorithmic Approach

Actually, it is most fruitful to discuss the quantity of information
"conveyed by an object" (x) "about an object" 0).It is not an accident,
that in the probabilistic approach this has led to a generalization to the
case of continuous variables, for which the entropy is infinite but, in a
large numbers of cases,

is finite. The real objects that we study are very (infinitely) complex, but
the relationships between two separate objects diminish as the schemes
used to describe them become simpler. While a map yields a considerable
amount of information about a region of the earth's surface, the microstrncture of the paper and the ink of the paper have no relation to the
microstructure of the area shown on the map.
In practice, we are most frequently interested in the quantity of information "conveyed by an individual object x about an individual object y."
It is true, as we have already noted, that such an individual quantitative
estimate of information is meaningful only when the quantity of information is sufficiently large. It is, for example, meaningless to ask about
the quantity of information conveyed by the sequence
0 1 1 0

about the sequence
1100.

But if we take a perfectly specific table of random numbers of the sort
commonly used in statistical practice, and for each of its digits we write
the unit's digit of the units of square according to the scheme

the new table will contain approximately

164

A. N. KOLMOGOROV

bits of information about the initial sequence (where n is the number of
digits in the tables). .
Accordingly, below we propose to define
IA(X:Y)
so that some indeterminacy remains. Different equivalent variants of this
definition will lead to values equivalent only in the sense that I,, % I,,,
lee.,
IC, - I AS~C A
~, A ~ ,
where the constant CAIAl
depends on the two basic ways of defining the
universal methods of programming At and A 2 .
Consider an "index domain of objects," i.e., a countable set

x = {XI,
with a finite sequence n(x) of zeros and ones, beginning with a one,
associated with each element as its index. Denote the length of the sesequence n ( ~ by
) I(x), and assume that:
1) the correspondence between X and the set D of binary sequences
of the form described above is one-to-one;
2) D c X, the function n(x) on D is generally recursive [I], and for
XED
W 4 ) 6 Kx) + C,
where C is a constant;

3) together with x and y, the set X contains the ordered pair (x, y),
whose index is a generally recursive function of the indices of x and y
and
G , Y ) s c x -4- ICY),
where C, depends only on x.
Not all of these requirements are essential, but they do simplify the
discussion. The end result of the construdtion is invariant under transition to a new indexing nl(x) that has the same properties as the old
system, and can be generally recursively expressed in termsofit; moreover, .
Xretains its properties when embedded in a larger system X'(provided
that, for the members of the initial system, the index n' in the expanded
system can be generally recursively expressed in terms of the initial

THREE APPROACHES TO THE QUANTITATIVE DEFINITION

165

index n). The new "complexity" K and quantity of information remain
equivalent under these transformations in the sense of x .
As the "relative complexity" of an object y with a given x, we will
take the minimal length i(p) of the "program" p for obtaining y from x.
The definition thus formulated depends on the "programming method,"
which is nothing other than the function

that associates on object y with a program p and an object x.
In accordance with the views now universally accepted in modern
mathematical logic, we must assume that the function g, is partially
recursive. For any such function we have
rnin

l(p)

CQ if there is no p such that g,@,

x) = y,

In this case a function
v = g,W

of u E X with range v B X is said to be partially recursive if it generates
a partially recursive function of the index transformation

In order to understand the definition, it is important to not that, in
general, partially recursive functions are not defined everywhere, and
there is no fixed method for determining whether application of the
program p to an object k will lead to a result or not. As a result, the
function K,O,/x) cannot be effectively calculated (generally recursive)
even if it is known to be finite for all x and y.
Fundamental theorem. There exists a partially recursive function A(p, x)
such that for any other partially recursive function q(p7x) we have the
inequality
K h l x ) 5 &Dlx) + Cp7
where the constant C, does not depend on x or y.
The proof is based on the existence of a universal partially recursive
function
@(n,
4

9

166

A. N. KOLMOGOROV

which has the property that by fixing an appropriate index n, we can
use the formula
~ ( =4@(n, u)
to obtain any other partially recursive function. The function A@, x)
we require, is given by the formula*

We will call functions A(p, x) that satisfy the requirements of the
fundamental theorem (and the programming methods defined by them)
asymptotically optimal. It is clear that the corresponding "complexity"
KA(y/x)is finite for all x and y. For two such functions A , and A,

s

I ~ * , w x >- &,Cylx)l
CA,,,,
where CA,,,does not depend on x and y, i.e., KA,blx) - K~,blx).
Finally,
KAO = KAb/l)
can be taken for the "complexity of y" and we can define the "quantity
of information conveyed by x about y" by the formula
It is easy to show** that this quantity is always essentially positive,
which means that IA(x:y) is no less than some negative constant C
that depends only on the characteristics of the selected programming
method. As we have already noted, the theorem was designed for appliis
cation to a quantity of information so large that, in comparison,
negligibly small.
Note, finally, that KA(x/x)x 0,I,(x : x) x KA(x).

Ic(

q n , u) is defined only when n E D, and A(p, x) is defined only when p is of the
form (n, q) n E D.
** By choosing a "comparison function" of the form p(p, x) = A(p, I), we obtain
K~b'lx)5 %(Y/X) Cw = KA(Y) Cp

+

+

THREE APPROACHES TO THE QUANTITATIVE DEFINITION

167

Of course, one can avoid the indeterminacies associated with the constant C,, etc., by considering particular domains of the objects X, indexing, and the function A, but it is doubtful that this can be done
without explicit arbitrariness. One must, however, suppose that the
different "reasonable " variants presented here will lead to "complexity
estimates" that will converge on hundreds of bits instead of tens of thousands. Hence, such quantities as the "complexity" of the text of "War
and Peace" can be assumed to be defined with what amounts to uniqueness. Experiments on guessing continuations of literary texts make it
possible to obtain an upper estimate for the conditional complexity in
the presence of a given consumption of "a priori information" (about
language, style, textual content) available to the guesser. In tests conducted at the Moscow State University Department of Probability Theory,
such upper estimates fluctuated between 0.9 and 1.4. The estimates of
the order of 0.9-1.1 obtained by N. G. Rychkov have led less successful
guessers to suggest that the telepathically communicated with the authors
of the texts.
I believe that the approach proposed here yields, in principle, a correct
definition of the "quantity of hereditary information," although it would
be difficult to obtain a reliable estimate of this quantity.
4. Conclusion

The concepts discussed in $ 3 have one important disadvantage: They
do not allow for the "difficulty" of preparing a program p for passing
from an object x to an object y. By introducing appropriate definitions,
it is possible to prove rigorously formulated mathematical propositions
that can be legitimately interpreted as an indication of the existence of
cases in which an object permitting a very simple program, i.e., with a
very small complexity K(x), can be restored by short programs only as
the result of computations of a thoroughly unreal duration. Sometime
in the future, I intend to study the relationship between the necessary
complexity of a program
Kt(4
and its permissible difficulty t. The complexity K(x) that was obtained
in $ 3 , is, in this case, the minimum 6f Kt(x) on the removal of constraints
on r.

168

A. N. KOLMOGOROV

It is beyond the scope of this article to consider the use of the constructions of $ 3in providing a new basis for probability theory. Roughly
speaking, the situation is as follows: If a finite set M, containing a very
large number of membersN, admits determination by means of a program
of length negligibly small in comparison with logz N, then almost all
members'of M have complexity K(x) close to log, N. The elements
x E M of this complexity are also treated as "random" members of the
set M. An incomplete discussion of this idea may be found in [2].

References
1.V. A. Uspenskii, Lectures on Computable Functions [in Russian], Fizmatgiz,
Moscow, 1960.
2. A.N.Kolmogorov, "On tables of random numbers," Sankhya. Indian J. of
Statisti&,Series A, 25,4, 369-376, (1963).

