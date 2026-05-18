Dynami s of market

orrelations: Taxonomy and portfolio analysis

J.-P. Onnela, A. Chakraborti, K. Kaski

arXiv:cond-mat/0302546v1 [cond-mat.stat-mech] 26 Feb 2003

Laboratory of Computational Engineering, Helsinki University of Te hnology, P.O. Box 9203, FIN-02015 HUT, Finland
J. Kertész

Department of Theoreti al Physi s, Budapest University of Te hnology
& E onomi s, Budafoki út 8, H-1111, Budapest, Hungary and
Laboratory of Computational Engineering, Helsinki University of Te hnology, P.O. Box 9203, FIN-02015 HUT, Finland
A. Kanto

Department of Quantitative Methods in E onomi s and Management S ien e,
Helsinki S hool of E onomi s, P.O.Box 1210, FIN-00101 Helsinki, Finland
The time dependen e of the re ently introdu ed minimum spanning tree des ription of
between sto ks,

alled the asset tree have been studied to ree t the e onomi

orrelations

taxonomy. The

nodes of the tree are identied with sto ks and the distan e between them is a unique fun tion of the
orresponding element of the
as the most strongly
o

orrelation matrix. By using the

onne ted node of the tree, an important

upation layer (MOL). During

rashes the strong global

on ept of a
hara teristi

entral vertex,

hosen

is dened by the mean

orrelation in the market manifests itself

by a low value of MOL. The tree seems to have a s ale free stru ture where the s aling exponent of
the degree distribution is dierent for `business as usual' and ` rash' periods. The basi

stru ture

of the tree topology is very robust with respe t to time. We also point out that the diversi ation
aspe t of portfolio optimization results in the fa t that the assets of the

lassi

Markowitz portfolio

are always lo ated on the outer leaves of the tree. Te hni al aspe ts like the window size dependen e
of the investigated quantities are also dis ussed.

I.

exploring the asset tree

INTRODUCTION

dynami s

an provide us new in-

sights to the market. We believe that dynami
In spite of the traditional wisdom Money does not
grow on trees, here we wish to show that the

on ept

of trees (graphs) have potential appli ations in nan ial
market analysis. This on ept was re ently introdu ed by
Mantegna as a method for nding a hierar hi al arrangement of sto ks through studying the

lustering of

ompa-

nies by using orrelations of asset returns [1℄. With an appropriate metri , based on the

orrelation matrix, a fully

onne ted graph was dened in whi h the nodes are

om-

panies, or sto ks, and the `distan es' between them are
obtained from the

orresponding

orrelation

oe ients.

The minimum spanning tree (MST) was generated from
the graph by sele ting the most important
and it is used to identify

lusters of

orrelations

all it a `dynami

asset

dan e of information. We aim to derive intuitively understandable measures, whi h

an be used to hara terize

the market taxonomy and its state. A further

distribution [6℄. We will also study the robustness of tree
topology and the

onsequen es of the market events on

its stru ture. The minimum spanning tree, as a strongly
pruned representative of asset

orrelations, is found to be

robust and des riptive of sto k market events.
Furthermore, we aim to apply dynami

entral problem from the

treatments, in luding spin glass type studies [8℄. In all

been made to obtain

orrelation

las-

si al approa h of Markowitz [7℄ to more sophisti ated

asset pri es play a

method [2℄,

asset trees in

the eld of portfolio optimization. Many attempts have

the attempts to solve this problem,

lustering from the huge

hara teri-

zation of the asset tree is obtained by studying its degree

tree'. It should be mentioned that several attempts have
matrix, like the Potts super paramagneti

asset trees

omplexity in order to grasp

the essen e of the market without drowning in the abun-

been made to solve this

ompanies.

In this paper, we study the time dependent properties
of the minimum spanning tree and

an be used to simplify this

fore, expe t a

orrelations between

ru ial role and one might, there-

onne tion between dynami

asset trees

a method based on the maximum likelihood [3℄ or the

and the Markowitz portfolio optimization s heme.

omparison of the eigenvalues with those given by the

demonstrate that although the topologi al stru ture of

random matrix theory [4℄.

the tree

We have

hosen the MST

hanges with time, the

We

ompanies of the mini-

The dierent

mum risk Markowitz portfolio are always lo ated on the

ompared in [3℄.

outer leaves of the tree. Consequently, asset trees in ad-

Finan ial markets are often

hara terized as evolving

dition to their ability to form e onomi ally meaningful

be ause of its uniqueness and simpli ity.
methods are

omplex systems [5℄.
the

The evolution is a ree tion of

hanging power stru ture in the market and it man-

lusters,

ould potentially

ontribute to the portfolio op-

timization problem. Then with a lighter key one

ould

ifests the passing of dierent produ ts and produ t gen-

perhaps say that some money may grow on trees, after

erations, new te hnologies, management teams, allian es

all.

and partnerships, among many other fa tors. This is why

The paper is organized as follows. In Se tion 2 we in-

2

h...i indi ates a time average over the

trodu e the data, dis uss some properties of asset return

where

orrelation distributions and

tive trading days in luded in the return ve tors. Due to

onstru t and

trees. Se tion 3 deals with tree o
vertex

hara terize

upation and

entral

onsiderations, followed with Se tion 4 whi h ad-

dresses the important question of e onomi
ness of tree

lusters.

meaningful-

Then Se tion 5 is devoted to the

study of the s ale free

Cau hy-S hwarz inequality, these

orrelation

asset trees to be dis ussed later.
Let us rst

hara terize the

orrelation

oe ient dis-

tion 6 deals with tree evolution through the

on epts of

tribution by its rst four moments and their

two dierent types of survival ratios, whi h

an be used

with one another. The rst moment is the

half-lives.

onne tions and determine tree

tion oe ient dened as

orrelations

mean orrela-

In the subsequent Se tion 7, we investigate

how asset trees

an

ontribute to the portfolio optimiza-

tion problem. Finally, in Se tion 8, we draw

on lusions

ρ̄(t) =

and summarize our ndings.

II.

oe ients

ondition −1 ≤ ρij ≤ 1 and form an N ×N ort
relation matrix C , whi h serves as the basis of dynami

fulll the

hara ter of the asset trees. Se -

to des ribe de aying of

onse u-

ASSET TREES

where we onsider only the non-diagonal (i 6= j) elements
ρtij of the upper (or lower) triangular matrix. We also
evaluate the higher order moments for the

The nan ial market, for the largest part in this paommer ially available from

X
1
(ρtij − ρ̄t )2 ,
N (N − 1)/2

(3)

X
1
3/2
(ρtij − ρ̄t )3 /λ2 (t),
N (N − 1)/2

(4)

λ2 (t) =

(i,j)

the University of Chi ago Graduate S hool of Business.
Here We will study the split-adjusted daily

losure pri es

= 477 sto ks traded at the New York

the skewness is

Sto k Ex hange (NYSE) over the period of 20 years,
from 02-Jan-1980 to 31-De -1999.

λ3 (t) =

This amounts a to-

(i,j)

tal of 5056 pri e quotes per sto k, indexed by time variable τ = 1, 2, . . . , 5056. For analysis and smoothing purposes, the data is divided time-wise into

t = 1, 2, ..., M of width T

M windows

and the kurtosis is

X
1
(ρtij − ρ̄t )4 /λ22 (t).
N (N − 1)/2

(5)

The mean, varian e, skewness and kurtosis of the

orrela-

orresponding to the number

of daily returns in luded in the window. Several

λ4 (t) =

onse u-

(i,j)

tive windows overlap with ea h other, the extent of whi h
is di tated by the window step length parameter δT , des ribing the displa ement of the window, measured also
in trading days. The hoi e of window width is a trade-o
between too noisy and too smoothed data for small and
large window widths, respe tively. The results presented
in this paper were

al ulated from monthly stepped four-

year windows, i.e.

δT ≈ 20.8 days and T = 1000 days.

We have explored a large s ale of dierent values for both
parameters, and the given values were found optimal [9℄.
With these

hoi es, the overall number of windows is

M = 195.
In order to investigate
rst denote the

orrelations between sto ks we

losure pri e of sto k i at time τ by Pi (τ )

(Note that τ refers to a date, not a time window). We
fo us our attention to the logarithmi

return of sto k

i, given by ri (τ ) = ln Pi (τ ) − ln Pi (τ − 1) whi h, for a
sequen e of

onse utive trading days, i.e. those en omt
passing the given window t, form the return ve tor r i .
In order to hara terize the syn hronous time evolution
of assets, we use the equal time

orrelation

oe ients

between assets i and j dened as

tion

oe ients are plotted as fun tions of time in Figure

1.
In this gure the ee t and reper ussions of Bla k Monday (O tober 19, 1987) are
of all these quantities.
tion

oe ient is

,
ρtij = q
2
2
[hr ti i − hr ti i2 ][hr tj i − hr tj i2 ]

learly visible in the behavior

For example, the mean

orrela-

learly higher than average on the in-

terval between 1986 and 1990. The length of this interval
orresponds to the window width T , and Bla k Monday
oin ides with the mid-point of the interval [10℄.
in reased value of the mean

orrelation is in a

with the observation by Drozdz et al.
that the maximum eigenvalue of the
whi h
market

arries most of the

The

ordan e

[11℄, who found

orrelation matrix,

orrelations, is very large during

rashes. We also investigated whether these four

dierent measures are

orrelated, as seems

lear from the

gure. For this we determined the Pearson's linear and
Spearman's rank-order

orrelation

oe ients, whi h be-

tween the mean and varian e turned out to be 0.97 and
0.90, and between skewness and kurtosis 0.93 and 0.96,
respe tively. Thus the rst two and the last two measures
are very strongly

hr ti rtj i − hr ti ihr tj i

orrelation

oe ients, so that the varian e is

the Center for Resear h in Se urity Pri es (CRSP) of

for a total of N

(2)

ρij ∈C

RETURN CORRELATIONS AND DYNAMIC

per, refers to a set of data

X
1
ρtij ,
N (N − 1)/2 t
t

orrelated.

We now move on to
(1)

onstru t an asset tree.
p For this we

use the non-linear transformation dij

= 2(1 − ρij ) to
obtain distan es with the property 2 ≥ dij ≥ 0, forming

mean correlation

3

mean

0.25
0.2
0.15

0.3

0.2

0.1
1984

1986

1988

1986

1988

1990

1992

1994

1996

1.2

1998

mean length

1984

time (year)

variance

0.12

1990

1992

1994

1996

1998

1992

1994

1996

1998

1992

1994

1996

1998

time (year)

0.1

1.1

1

0.1

1984

1986

1988

1990

time (year)

0.08
0.08

1984

1986

1988

1990

1992

1994

1996

risk

0.07

1998

0.06
0.05

time (year)

0.04

skewness

1.2

1984

1986

1988

1990

time (year)

1
0.8

Figure 2:

0.6

Plots of (a) the mean

orrelation

oe ient ρ̄(t),

(b) the normalized tree length L(t) and ( ) the risk of the

0.4

minimum risk portfolio, as fun tions of time.

0.2
1984

1986

1988

1990

1992

1994

1996

1998

time (year)

kurtosis

8

tionary steps of a single

dynami asset tree.

As a simple measure of the temporal state of the mar-

6

ket (the asset tree) we dene the

normalized tree length

as

4

1984

1986

1988

1990

1992

1994

1996

1998

time (year)
Figure 1:

L(t) =

oe ients as fun tions of time.

(6)

dij ∈T

The mean, varian e, skewness and kurtosis of the

orrelation

X
1
dtij ,
N −1 t
t

where t again denotes the time at whi h the tree is

on-

stru ted, and N − 1 is the number of edges present in the

t
an N × N distan e matrix D .

MST. The normalized tree length is depi ted in Figure
At this point an addi-

tional hypothesis about the topology of the metri

spa e

is required. The working hypothesis is that a useful spa e
for linking the sto ks is an

ultrametri spa e, i.e., a spa e

where all distan es are ultrametri .
motivated

This hypothesis is

a posteriori by the nding that the asso i-

ated taxonomy is meaningful from an e onomi
view.

The

point of

on ept of ultrametri ity is dis ussed in de-

tail by Mantegna [1℄, while the e onomi

meaningfulness

of the emerging taxonomy is addressed later in this paper. Out of the several possible ultrametri
subdominant ultrametri

2.
As expe ted and as the plots show, the mean
tion

orrela-

oe ient and the normalized tree length are very

strongly anti- orrelated. Pearson's linear
tween the mean

orrelation be-

oe ient ρ̄(t) and normal-

orrelation

ized tree length L(t) is -0.98, and Spearman's rank-order
orrelation

oe ient is -0.92, thus both indi ating very

strong anti- orrelation. Anti- orrelation is to be expe ted
in view of how the distan es dij are
orrelation

oe ients ρij .

onstru ted from

However, the extent of this

spa es, the

anti- orrelation is dierent for dierent input variables

is opted for due to its simpli -

and is lower if, say, daily transa tion volumes are studied

ity and remarkable properties. In pra ti e, it is obtained
t
by using the distan e matrix D to determine the min-

instead of daily

imum spanning tree (MST) of the distan es, a ording
t
to the methodology of [1℄, denoted T . This is a simply

spanning tree, we are ee tively redu ing the informa-

onne ted graph that

onne ts all N nodes of the graph

with N − 1 edges su h that the sum of all edge weights,
P
t
dt ∈Tt dij , is minimum. (Here time (window) depenij

losure pri es [12℄.

It should be noted that in

onstru ting the minimum

tion spa e from N (N − 1)/2 separate

orrelation

ients to N − 1 tree edges, in other words,

oe-

ompressing

the amount of information dramati ally. This follows bet
t
ause the orrelation matrix C and distan e matrix D

den e of the tree is emphasized by the addition of the

are both N × N dimensional, but due to their symmetry,

supers ript t to the notation.)

onstru ted

both have N (N − 1)/2 distin t upper (or lower) triangle

for dierent time windows are not independent from ea h

elements, while the spanning tree has only N − 1 edges.

other, but form a series through time. Consequently, this

So, in moving from

multitude of trees is interpreted as a sequen e of evolu-

asset tree, we have pruned the system from N (N − 1)/2

Asset trees

orrelation or distan e matrix to the

4
to N − 1 elements of information. This, of

ourse, raises

MER

the key question of information theory, whether essenexamination of the mean

orrelation

DIS

As the above

oe ient and nor-

malized tree length shows, the fa t that the two measures are strongly anti- orrelated testies to the su

vertex

tial information is lost in the redu tion.

DOW

CBS

ess

of the pruning pro ess. Consequently, one is justied to

GE

ontemplate the minimum spanning tree as a strongly
redu ed representative of the whole

1982

whi h bears the essential information about asset

1986

1988

1990

1992

1994

1996

1998

1994

1996

1998

1994

1996

1998

time (year)

orreMER

lations.

FNM

As further eviden e that the MST retains the salient
rash

an be quite a

urately seen in Figure 2.

The fa t that the market , during

rash, is moving to-

DUK

vertex

features of the sto k market, it is noted that the 1987
market

1984

orrelation matrix,

DIS
AEP
DOW

gether is thus manifested in two ways. First, the ridge in

BMY

the plot of the mean

CBS

orrelation

oe ient in Figure 2(a)

GE

indi ates that the whole market is ex eptionally strongly
orrelated. Se ond, the

1982

1984

1986

1988

1990

1992

time (year)

orresponding well in the plot of

the normalized tree length in Figure 2(b) shows how this
is ree ted in

WMT

onsiderably shorter than average length

MER

of the tree so that the tree, on average, is very tightly
sides of the ridge

onverge to a single date, whi h

oin-

ides with Bla k Monday [10℄.

FNM

vertex

pa ked. Upon letting the window width T → 0, the two

BK
MMM
PG
CBS
GE
KO

III.

TREE OCCUPATION AND CENTRAL

1982

1984

1986

Next we fo us on

hara terizing the spread of nodes on

the tree. In order to do so, we introdu e the quantity of

mean o upation layer as

(7)

onfused with the distan es dij between nodes,

entral
vertex vc , whose level is taken to be zero. Here the mean

are measured in natural numbers in relation to the

upation layer indi ates the layer on whi h the mass of

the tree, on average, is

on eived to be lo ated.

Let us now examine the

entral vertex in more de-

tail, as the understanding of the
for interpreting mean o
shortly.

The

on ept is a prerequisite

upation layer results, to follow

entral vertex is

1990

1992

Central verti es a

ording to (a) vertex degree

riterion, (b) weighted vertex degree
of mass

riterion and ( )

onsidered the parent of

enter

riterion.

ases, identi al out omes. The rst and se -

ond denitions of the

entral vertex are lo al in nature.

The idea here is to nd the node that is most strongly
onne ted to its nearest neighbors. A

where lev(vi ) denotes the level of vertex vi . The levels,

o

Figure 3:

and, in most

N

1 X
l(t, vc ) =
lev(vit ),
N i=1
not to be

1988

time (year)

VERTEX

ording to the the

vertex
degree, i.e. the number of edges whi h are in ident with

rst denition, this is the node with the highest

(neighbor of ) the vertex. The obtained results are shown
in Figure 3.
The

vertex degree riterion leads to General Ele tri

(GE) dominating 67.2% of the time, followed by Merrill
Lyn h (MER) at 20.5% and CBS at 8.2%.

The

om-

bined share of these three verti es is 95.9%. The se ond
denition, a modi ation of the rst, denes the

entral

vertex as the one with the highest sum of those

orre-

all other nodes in the tree, also known as the root of the

lation

tree. It is used as the referen e point in the tree, against

edges of the vertex.

whi h the lo ations of all other nodes are relative. Thus

nition weighs ea h departing node equally, the se ond

all other nodes in the tree are

gives more weight to short edges, sin e a high value of

hildren of the

tex. Although there is arbitrariness in the
entral vertex, we propose that it is
tant, in the sense that any

entral verhoi e of the

entral, or impor-

hange in its pri e strongly

ρij

oe ients that are asso iated with the in ident
Therefore, whereas the rst de-

orresponds to a low value of dij .

able, as short

This is reason-

onne tions link the vertex more tightly to

its neighborhood than long ones (the same prin iple em-

We propose three alternative denitions have emerged

onstru ting the spanning tree). This weighted
vertex degree riterion results in GE dominating 65.6% of

for the

the

ae ts the

ourse of events in the market on the whole.

entral vertex in our studies, all yielding similar

ployed in

ases, followed by MER at 20.0% and CBS at 8.7%,

5
10

the share of the top three being 94.3%. The third denition deals with the global quantity of
. In
t
onsidering a tree T at time t, the vertex vi that pro-

enter of mass

9

upation layer l(t, vi )

8

du es the lowest value for mean o

enter of mass, given that all nodes are assigned

an equal weight and

onse utive layers (levels) are at

equidistan e from one another, in a

ordan e with the

enter of mass riterion we

above denition. With this
nd that the most dominant

ompany, again, is GE, as

it is 52.8% of the time the

entre of mass, followed by

mean layer

is the

andidates

6

5

MER at 15.4% and Minnesota Mining & MFG at 14.9%.
These top three

7

4

onstitute 83.1% of the total.
3

Should the weight of the node be made proportional to
the size (e.g. revenue, prot et .) of the

ompany, it is

2

1984

obvious that GE's dominan e would in rease.

1986

1988

1990

1992

1994

1996

1998

time (year)

As Figure 3 shows, the three alternative denitions for
the

entral vertex lead to very similar results. The vertex

degree and the weighted vertex degree

riteria

91.8% of the time. In addition, the former

oin ide

Figure 4:

Plot of mean o

of time, with stati

upation layer l(t, vc ) as a fun tion

and dynami

entral verti es.

oin ides with

enter of mass 66.7% and the latter 64.6% of the time,
respe tively.

Overall, the three

entral vertex in 63.6% of the
able mutual agreement.

riteria yield the same

ases, indi ating

onsider-

The existen e of a meaningful

onne ted to market

enter in the tree is not a trivial issue, and neither is

that period as

oin iden e with the

500 index.

the

riteria applied, present a mixture of both lo al and

global approa hes, and the fa t that they

enter in the tree. The reason for the

iden e of the

riteria seems

entral vertex in

arries a lot of weight around it (the neigh-

boring nodes), whi h in turn may be highly
to others (to their

hildren) and so on.

onne ted

Two dierent

interpretations may be given to these results. One may
have either (i) stati

(xed at all times) or (ii) dynami

(updated at ea h time step)

entral vertex. If the rst

approa h is opted for, the above eviden e well substantiates the use of GE as the

entral vertex. In the se ond

approa h, the results will vary somewhat depending on
whi h of the three

riteria is used in determining the

en-

tral vertex.
upation layer l(t) is depi ted in Figure 4,

where also the ee t of dierent entral verti es is demonThe blue

vertex, i.e.

TREE CLUSTERS AND THEIR ECONOMIC
MEANINGFULNESS

As mentioned earlier, Mantegna's idea of linking sto ks
in an ultrametri

urve results from the stati

entral

GE, and the green one to dynami

entral

spa e was motivated

a posteriori by the

property of su h a spa e to provide a meaningful e onomi

taxonomy. We will now explore this issue further,

as the meaningfulness of the emerging e onomi

taxon-

omy is the key justi ation for the use of the

urrent

methodology. In [1℄, Mantegna examined the meaningfulness of the taxonomy by

omparing the grouping of

sto ks in the tree with a third party referen e grouping of
sto ks by their industry et .

lassi ations. In this

ase,

the referen e was provided by Forbes[14℄, whi h uses its
own

The mean o
strated.

IV.

oin-

lear, intuitively speaking.

A vertex with a high vertex degree, the
parti ular,

an be seen, for example, from the S&P

oin ide al-

most 2/3 of the time, does indi ate the existen e of a
well-dened

The ner stru ture may

result from general steady growth in asset pri es during

its

enter of mass. However, sin e

rashes, where the behavior of the

system is very homogeneous.

lassi ation system, assigning ea h sto k with a

se tor (higher level) and industry (lower level)

ategory..

In order to visualize the grouping of sto ks, we

on-

stru ted a sample asset tree for a smaller dataset, shown
in Figure 5. This was obtained by studying our previous

vertex evaluated using the vertex degree

riterion. The

dataset [13℄, whi h

two

urve is drawn.

tending from the beginning of 1982 to the end of 2000,

urves

oin ide where only the blue

onsists of 116 S&P 500 sto ks, ex-

entral ver-

resulting in a total of 4787 pri e quotes per sto k [15℄.

The two dips at

1986 and 1990, lo ated symmetri ally at half a window

The window width was set at T = 1000, and the shown
∗
sample tree is lo ated time-wise at t = t , orresponding

width from Bla k Monday,

to 1.1.1998. The sto ks in this dataset fall into 12

This is true most of the time, as the above
tex

onsiderations lead us to expe t.

orrespond to the topologi al

shrinking of the tree asso iated with the famous market

whi h are Basi

se tors,

Materials, Capital Goods, Conglomer-

rash of 1987 [10℄. Roughly between 1993 and 1997 l(t)

ates, Consumer/Cy li al, Consumer/Non-Cy li al, En-

rea hes very high values, whi h is in

ergy, Finan ial, Health are, Servi es, Te hnology, Trans-

on ordan e with

our earlier results obtained for a dierent set of data [13℄.

portation and Utilities. The se tors are indi ated in the

High values of l(t) are

tree with dierent markers, while the industry

onsidered to ree t a ner mar-

ket stru ture, whereas in the other extreme low dips are

tions are omitted for reasons of

larity.

lassi a-

6

outside the formed

luster are

onsidered outliers. (iii)

Only those edges that are required to

onne t the

luster

are in luded. Therefore, for example, in the Basi

Mate-

rials

luster, the edges DOW-IP and IP-GP are

ounted,

even though IP is not a Basi

Materials

is needed to render the

onne ted. (iv) If there are

nodes in a
not have

luster

ompany, but it

luster whi h do not belong there, and they do
hildren that belong to the

luster either, they

are not in luded. For example, again in the Basi

Mate-

rials

ounted

luster, edges DD-CSX-BNI-UNP are not

as they do not have

hildren that belong to the Basi

Materials se tor, although the parent DD is a member of
the

luster. Consequently, CSX, BNI and UNP are not

in luded in the Basi

Materials

luster.

Let us now examine some of the

lusters that have

omplete and in omplete to des ribe, in rather stri t terms,

been formed in the sample tree. We use the terms
asset tree

onne ting the

the su

examined 116 sto ks of the S&P 500 index.

The tree was

the

Figure 5:

Snapshot of a dynami

produ ed using four-year window width and it is

entered on

January 1, 1998. Business se tors are indi ated a

ording to

Forbes,

http://www.forbes. om. In this tree, General Ele tri

(GE) was used as the

entral vertex and eight layers

an be

identied.

Before

evaluating

the

e onomi

meaningfulness

of

grouping sto ks, we wish to establish some terminology.
We use the term se tor ex lusively to refer to the given
third party

lassi ation system of sto ks.

The term

bran h refers to a subset of the tree, to all the nodes
that share the spe ied

ommon parent. In addition to

the parent, we need to have a referen e point to indi ate

ess of

lustering. A

omplete

luster

ontains all

ompanies of the studied set belonging to the

or-

responding business se tor, so that none are left outside
the

luster. In pra ti e, however,

omplete,

lusters are mostly in-

ontaining most, but not all, of the

ompanies

of the given business se tor, and the rest are to be found
somewhere else in the tree. Only the Energy

luster was

found

lose, typi-

omplete, but many others

ome very

ally missing just one or two members of the
Building upon the normalized tree length
an hara terize the strength of

luster.
on ept, we

lusters in a similar man-

ner, as they are simply subsets of the tree. These
ters, whether
by the

omplete or in omplete, are

lus-

hara terized

normalized luster length, dened for a

luster c

as follows

the generational dire tion (i.e. who is who's parent) in
order for a bran h to be well dened. Without this refer-

Lc (t) =

en e there is absolutely no way to determine where one
bran h ends and the other begins. In our
eren e is the

ase, the ref-

1 X t
dij ,
Nc t

(8)

dij ∈c

entral node. There are some bran hes in

the tree, in whi h most of the sto ks belong to just one

where Nc is the number of sto ks in the

se tor, indi ating that the bran h is fairly homogeneous

be

with respe t to business se tors.

This nding is in a -

luster. This

an

ompared with the normalized tree length, whi h for
∗
∗
the sample tree in Figure 5 at time t is L(t ) ≈ 1.05.

ordan e with those of Mantegna [1℄, although there are

A full a

bran hes that are fairly heterogeneous, su h as the one

A, but as a short summary of results we state the follow-

ount of the results is to be found in Appendix

extending dire tly downwards from the

ing. The Energy

homogeneous as measured by the uniformity of their se -

ompanies form the most tightly pa ked
∗
luster resulting in LEnergy (t ) ≈ 0.92, followed by the
∗
Health- are luster with LHealth- are (t ) ≈ 0.98. For the
∗
Utilities luster we have LUtilities (t ) ≈ 1.01 and for the
∗
diverse Basi Materials luster LBasi materials (t ) ≈ 1.03.

tor

Even though the Te hnology

entral vertex,

see Figure 5.
Sin e the grouping of sto ks is not perfe t at the bran h
level, we dene a smaller subset whose members are more
lassi ations. The term

luster is dened, broadly

speaking, as a subset of a bran h, but a more a

urate

denition is based on the following four rules. (i) A

lus-

ter is named after the
in the

luster

luster parent, whi h is the node

losest to the

starting node of the

luster. The

the business se tor of the
for example, Utilities

entral vertex and it is the
luster is named after

luster parent.

This is why,

luster starts from PGL and not

from KO. (ii) If there are more than one potential
ter parent, the one resulting in the most
is

hosen as the

omplete

lus-

luster

luster parent. The nodes that are left

luster has the fewest num-

ber of members, its mean distan e is the highest of the
∗
examined groups of lusters being LTe hnology (t ) ≈ 1.07.
Thus, most

lusters seem to be more tightly pa ked than

the tree on average.
One

ould nd and examine several other

lusters in

the tree, but the ones that were identied are quite

on-

vin ing. The minimum spanning tree, indeed, seems to
provide a taxonomy that is well
se tor

ompatible with the

lassi ation provided by an outside institution,

Forbes in this

ase. This is a strong vote for the use of

7

the

urrent methodology in sto k market analysis. Some

further analysis of the identied

lusters is presented in

of external risks inuen es the sto k pri e of these
panies, in

oarse terms, leading to their more

lustering than that of

Appendix A.
There are, however, some observed deviations to the
lassi ation, whi h

all for an explanation.

the following points are raised.

For them

(i) Un ertainty in as-

set pri es in the minds of investors

om-

omplete

ompanies fa ing less uniform ex-

ternal risks. In

on lusion, regarding all the above listed

fa tors, the su

ess of the applied method in identifying

market taxonomy is remarkable.

auses some seem-

ingly random pri e u tuations to take pla e, and this
introdu es noise in the

orrelation matrix. Therefore,

V.

SCALE FREE STRUCTURE OF THE ASSET
TREE

it is not reasonable to expe t a one-to-one mapping between business se tors and MST

lusters. (ii) Business

se tor denitions are not unique, but vary by the orga-

So far we have

hara terized the asset tree as an im-

nization issuing them. In this work, we used the

lassi-

portant subgraph of the fully

onne ted graph derived

 ation system by Forbes [14℄, where the studied

om-

from all the elements of the

onne tivity matrix. Sin e

panies are divided into 12 business se tors and 51 industries.
on

Forbes has its own

the asset tree is expe ted to ree t some aspe ts of the

lassi ation prin iple, based

market and its state, it is therefore of interest to learn

ompany dynami s rather than size alone. Alterna-

more about its stru ture. During the last few years, mu h

tively, one

ould have used, say, the Global Industry

attention has been devoted to the degree distribution of

Classi ation Standard (GICS), released on January 2,

graphs. It has be ome

2001, by Standard & Poor's [16℄.

Within this frame-

graphs, where this distribution obeys a power law, are

ompanies are divided into 10 se tors, 23 industry

very frequent in many elds, ranging from human rela-

groups, 59 industries and 122 sub-industries. Therefore,

tionships through ell metabolism to the Internet [17, 18℄.

work,
the

lassi ation system

lear that the so

alled s ale free

learly makes a dieren e, and

S ale free trees have also been extensively studied (see

there are dis repan ies even at the topmost level of busi-

e.g., [19℄). Re ently, examples for s ale free networks in

ness se tors amongst dierent systems.

(iii) Histori al

e onomy and nan e have been found [6, 20, 21℄.

pri e time series is, by denition, old.

Therefore, one

Vandewalle et al. [6℄ found s ale free behavior for the

ontemporary denitions for business se tors

asset tree in a limited (one year, 1999) time window for

should use

et ., as those most a

urately

hara terize the

ompany.

Sin e these were not available to the authors, the
si ation s heme by Forbes was used. The error
by this approa h varies for dierent
many

lassi ation systems,

las-

aused

6358 sto ks traded at the NYSE, NASDAQ and AMEX.
They proposed the distribution of the vertex degrees f (n)
to follow a power law behavior:

ompanies. (iv) In

f (n) ∼ n−α ,

ompanies engaged in sub-

stantially dierent business a tivities are

lassied a -

(9)

ording to where the majority of revenues and prots

with the exponent α ≈ 2.2. This exponent implies that

omes from. For highly diversied

las-

the se ond moment of the distribution would diverge in

si ations are more ambiguous and, therefore, less infor-

the innite market limit, or in other words, the se ond

mative. As a

onsequen e,

ompanies, these

lassi ation of these types of

ompanies should be viewed with some skepti ism. This
problem has its roots in the desire to

ategorize

ompa-

moment of the distribution is always dominated by the
rare but extremely highly

onne ted verti es.

Our aim here is to study the property of s ale freeness

nies by a single label, and the approa h fails where this

in the light of asset tree dynami s.

division is unnatural. (v) Some

that the asset tree has, most of the time, s ale free prop-

plained through the MST
is based on

luster outliers

an be ex-

lustering me hanism, whi h

orrelations between asset returns.

There-

fore, one would expe t, for example, investment banks

First, we

on lude

erties with a rather robust exponent α ≈ −2.1 ± 0.1 for
normal topology (i.e. outside
as usual'), a result

rash periods of 'business

lose to that given in [6℄. For most of

to be grouped with their investments rather than with

the time the distribution behaves in a universal manner,

other similar institutions.

meaning that the exponent α is a

Through portfolio diversi-

onstant within the

ation, these banks distan e themselves from the pri e

error limits. However, when the behavior of the market

u tuations (risks) of a single business se tor.

is not 'business as usual' (i.e. within

Conse-

quently, it would be more surprising to nd a totally ho-

exponent also

mogeneous nan ial

of the tree is still maintained.

one

luster than a fairly heterogeneous

urrently observed.

(vi) The risks imposed on the

rash periods), the

hanges, although the s ale free

hara ter

For the Bla k Monday

period, we have α ≈ −1.8 ± 0.1.

This result is in full

ompanies by the external environment vary in their de-

agreement with the observation of the shrinking of the

gree of uniformity from one business se tor to another.

tree during market

For example,

in rease in the degree, thus explaining the higher value

ompanies in the Energy se tor (pri e of

rashes, whi h is a

ompanied by an

their sto ks) are prone to u tuations in the world mar-

of the exponent. The observation

ket pri e of oil, whereas it is di ult to think of one

in the value of the exponent for normal and

fa tor having equal inuen e on, say,

is exemplied in Figure 6.

ompanies in the

Consumer/Non- y li al business se tor. This uniformity

on erning the

When tting the data, in many

hange

rash period

ases we found one

8
0

10

−1

1

−1

0.9

−2

0.8

−2

10

−3

−3

10

10

−4

10

10

−4

0

1

10

2

10

10

10

0

1

10

k
Figure 6:

2

10

10

k

survival ratio / overlap

10

f(k)

10

f(k)

0

10

0.7

0.6

0.5

Typi al plots of vertex degree for normal (left) and

rash topology (right), for whi h the exponents and goodness
2
2
of t are α ≈ −2.15, R ≈ 0.96 and α ≈ −1.75, R ≈ 0.92,

0.4

respe tively. The plot on the left is

0.3

entered at 28.2.1994 and

the right one at 1.5.1989, and for both T = 1000.

1986

1988

1990

1992

1994

1996

1998

time (year)
Figure 7:

or two outliers, i.e.

1984

Single-step survival ratio σ(t) as a fun tion of time.

verti es whose degrees did not t

to the overall power law behavior sin e they were mu h
too high. In all
the highest

ases these sto ks

onne ted node (i.e.

orresponded either to
the

se utive trees at times t and t − 1 as

entral vertex) or

were nodes with very high degrees. This result suggest
that it
ial

ould be useful to handle these nodes with spe-

are, thus providing further support to the

of the

σ(t) =

on ept

1
|E(t) ∩ E(t − 1)|.
N −1

(10)

entral node. However, for the purpose of tting

the observed vertex degree data, su h nodes were

on-

sidered outliers. To give an overall measure of goodness
2
of the ts, we al ulated the R

oe ient of determination, whi h an be interpreted as the fra tion of the total

In this E(t) refers to the set of edges of the tree at time

t, ∩ is the interse tion operator and |...| gives the number of elements in the set. Under normal
the tree for two

ir umstan es,

onse utive time steps should look very

variation that is explained by the least-squares regression
2
≈ 0.86 for the
2
entire dataset with outliers in luded, and R ≈ 0.93 with

similar, at least for small values of window step length

outliers ex luded. Further, the ts for the normal market

the asset taxonomy, others may simply be due to noise.

period were better than those obtained for the

On letting δT

line. We obtained, on average, values of R

rash pe2

parameter δT .

With this measure it is expe ted that

while some of the dieren es

an ree t real

hanges in

→ 0, we nd that σ(t) → 1, indi ating

are stable in this limit [9℄.

riod as hara terized by the average values of R ≈ 0.89
2
and R ≈ 0.93, respe tively, with outliers ex luded. In

that the trees

addition to the market period based dependen e, the ex-

and δT

ponent α was also found to depend on the window width.

servations are made. (i) A large majority of

We examined a range of values for the window width T

survives from one time window to the next.

between 2 and 8 years and found, without ex luding the

two prominent dips indi ate a strong tree re onguration

outliers, the tted exponent to depend linearly on T .

taking pla e, and they are window width T apart, po-

In

on lusion, we have found the s aling exponent to

depend on the market period, i.e.

rash vs normal market

A sample plot of single-step survival ratio for T = 1000

≈ 20.8 is shown in Figure 7. The following obonne tions
(ii) The

sitioned symmetri ally around Bla k Monday, and thus
imply topologi al reorganization of the tree during the
rash[10℄. (iii) Single-step survival ratio σ(t) in-

ir umstan es and on the window width. These results

market

also raise the question of whether it is reasonable to as-

reases as the window width T in reases while δT is kept

sume that dierent markets share the s aling exponent.

onstant. Thus an in rease in window width renders the

In

trees more stable with respe t to single-step survival of

ase they do not, one should be

areful when pooling

sto ks together from dierent markets for the purpose of

onne tions. We also nd that the rate of

vertex degree analysis.

survival ratio de reases as the window width in reases

hange of the

and, in the limit, as the window width is in reased towards innity T → ∞,
VI.

σ(t) → 1 for all t. The survival

ratio seems to de rease very rapidly on e the window

ASSET TREE EVOLUTION

width is redu ed below roughly one year.

As the win-

dow width is de reased further towards zero, in the limit
In order to investigate the robustness of asset tree
topology, we dene the

single-step survival ratio of tree

edges as the fra tion of edges found

ommon in two

on-

as T → 0,

σ(t) → 0 for all t. (iv) Varian e of u tua-

tions around the mean is

onstant over time, ex ept for

the extreme events and the interim period, and it gets

9
0

1.5

1

half−life (year)

fraction of intact connections

10

−1

10

T=500
best fit
T=1000
best fit
T=1500
best fit

−2

10

0.5

0
0
−1

0

10

1

2

3

4

5

6

7

8

window width (year)

1

10

10

time (year)
Figure 9:
Figure 8:

Multi-step survival ratio σ(t, k) as a fun tion of

Plot of half-life t1/2 as a fun tion of window width

T.

values of T .

time for dierent parametri

short, as the time interval in whi h half the number of
less as the window width in reases.
In order to study the long term evolution of the trees,
we introdu e

σ(t, k) =

the multi-step survival ratio at time t as

1
|E(t) ∩ E(t − 1)...E(t − k + 1) ∩ E(t − k)|,
N −1
(11)

where only those
ount.

between two

A

is depi ted in Figure 9 and it is seen to follow a

ording to this formula, when a bond

ompanies breaks even on e in k steps and

then reappears, it is not

ounted as a survived

tion. It is found that many

onne -

onne tions in the asset trees

lean lin-

ear dependen e on for values of T being between 1 and 5
years, after whi h it begins to grow faster than a linear
fun tion. For the linear region, the tree half-life exhibits

t1/2 ≈ 0.12T dependen e.
This

onne tions that have persisted for the

whole time period without any interruptions are taken
into a

onne tions have de ayed, i.e., σ(t, t1/2 ) = 0.5.
The behavior of t1/2 as a fun tion of the window width
initial

an also be seen in Figure 8, where the dashed

horizontal line indi ates the level at whi h half of the
onne tions have de ayed. For the studied values of the
window width, tree half-life o

urs within the rst region

of the multi-step survival plot, where de aying was found
to depend on the window width. Consequently, the de-

evaporate quite rapidly in the early time horizon. How-

penden e of half-life on window width T does not

ever, this rate de reases signi antly with time, and even

di t the window width independent power law de aying

after several years there are some

onne tions that are

of

onne tions, as the two o

ontra-

ur in dierent regions. In

ompanies remain

general, the number of sto ks N , as well as the their

losely bonded for times longer that a de ade. The be-

type, is likely to ae t the half-lives. Earlier, for a set of

left inta t. This indi ates that some

havior of the multi-step survival ratio for three dierent
values of window width (2,4 and 6 years) is shown in

onsisting primarily of important industry giants, would

Figure 8, together with the asso iated ts.
In this gure the horizontal axis

an be divided into

two regions. Within the rst region, de aying of

N = 116 S&P 500 sto ks, half-life was found to depend
on the window width as t1/2 ≈ 0.20T [9℄. A smaller tree,

onne -

be expe ted to de ay more slowly than the larger set of
NYSE-traded sto ks studied in this paper.

tions is roughly exponential, and takes pla e at dierent
rates for dierent values of the window width.
within the se ond region, when most

Later,

onne tions have

VII.

PORTFOLIO ANALYSIS

de ayed and only some 20%-30% remain (for the shown
values of T ), there is a
ior.

ross-over to power law behav-

The exponents obtained for the window widths of

T = 500, T = 1000 and T = 1500 are -1.15, -1.19 and

Next, we apply the above dis ussed

on epts and mea-

sures to the portfolio optimization problem, a basi

prob-

lem of nan ial analysis. This is done in the hope that

-1.17, respe tively. Thus, interestingly, the power law de-

the asset tree

ay in the se ond region seems independent of the window

tive approa h to and/or visualization aid of the highly

width.
We

ould serve as another type of quantita-

inter- onne ted market, thus a ting as a tool support-

an also dene a

hara teristi

half-life of the survival ratio

time, the so

alled

t1/2 , or tree half-life for

We onsider a general Markowitz portfolio P(t) with the asset weights
ing the de ision making pro ess.

12
11
10
9
8
7
6
5
4
3
2

layer

layer

10

1984

1986

1988

1990

1992

1994

1996

12
11
10
9
8
7
6
5
4
3
2

1984

1998

1986

1988

layer

layer

12
11
10
9
8
7
6
5
4
3
2

1984

1986

1988

1990

1992

1994

1996

12
11
10
9
8
7
6
5
4
3
2

1984

1998

1986

1988

1992

1994

1996

1998

Plot of the weighted minimum risk portfolio layer

1990

1992

1994

1996

1998

time (year)

time (year)
Figure 10:

1990

time (year)

time (year)

Figure 11:

Plot of the weighted minimum risk portfolio layer

lP (t, θ = 0) with no short-selling and mean o upation layer
l(t, vc ) against time. Top: stati entral vertex, bottom: dy-

lP (t, θ = 0) with short-selling allowed and mean o upation
entral vertex, botlayer l(t, vc ) against time. Top: stati

nami

tom: dynami

entral vertex a

ording to the vertex degree

riterion.

entral vertex a

ording to the vertex degree

riterion.

w1 , w2 , . . . , wN . In the

lassi

Markowitz portfolio ophara terized by

lP (t, θ = 0). We nd that the portfolio layer is higher

their average risk and return, where the risk asso iated

than the mean layer at all times. The dieren e between

timization s heme, nan ial assets are

with an asset is measured by the standard deviation of returns. The Markowitz optimization is usually

arried out

the layers depends on the window width, here set at T =

1000, and the type of entral vertex used. The upper plot

by using histori al data. The aim is to optimize the asset

in Figure 10 is produ ed using the stati

weights so that the overall portfolio risk is minimized for

(GE), and the dieren e in layers is found to be 1.47. The

a given portfolio return rP [22℄.

In the dynami

asset

lower one is produ ed by using a dynami

tree framework, however, the task is to determine how

sele ted with the vertex degree

the assets are lo ated with respe t to the

the dieren e of 1.39 is found.

entral vertex.

Let rm and rM denote the returns of the minimum and

entral vertex
entral vertex,

riterion, in whi h

Above we assumed the no short-selling

ase

ondition.

maximum return portfolios, respe tively. The expe ted

However, it turns out that, in pra ti e, the weighted port-

portfolio return varies between these two extremes, and

folio layer never assumes negative values and the short-

an be expressed as rP,θ = (1 − θ)rm + θrM , where θ is

selling

a fra tion between 0 and 1. Hen e, when θ = 0, we have

peats the earlier plot, this time allowing for short-selling.

the minimum risk portfolio, and when θ = 1, we have the

The weighted portfolio layer is now 99.5% of the time

ondition, in fa t, is not ne essary. Figure 11 re-

maximum return (maximum risk) portfolio. The higher

higher than the mean o

the value of θ , the higher the expe ted portfolio return

same

rP,θ and,

en e between the two is 1.18 and 1.14 in the upper and

onsequently, the higher the risk the investor

is willing to absorb.

We dene a single measure, the

weighted portfolio layer as

entral vertex

upation layer and, with the

onguration as before, the dier-

lower plots, respe tively. Thus we

on lude that only mi-

nor dieren es are observed in the previous plots between
banning and allowing short-selling, although the dier-

lP (t, θ) =

X

wi lev(vit ),

en e between weighted portfolio layer and mean o
(12)

tion layer is somewhat larger in the rst

the dieren e in layers is also slightly larger for stati

i∈P(t,θ)

than dynami

PN

i=1 wi = 1 and further, as a starting point, the
onstraint wi ≥ 0 for all i, whi h is equivalent to assum-

where

ing that there is no short-selling.

upa-

ase. Further,

The purpose of this

entral vertex, although not by mu h.

As the sto ks of the minimum risk portfolio are found
on the outskirts of the tree, we expe t larger trees (higher

L) to have greater diversi ation potential, i.e., the s ope

onstraint is to prevent negative values for lP (t), whi h
would not have a meaningful interpretation in our frame-

mum risk portfolio. In order to look at this, we

work of trees with

the mean-varian e frontiers for the ensemble of 477 sto ks

entral vertex.

This restri tion will

risk of the minial ulated

using T = 1000 as the window width. In Figure 2, we plot

shortly be dis uss further.
Figure 10 shows the behavior of the mean o

of the sto k market to eliminate spe i

upation

layer l(t) and the weighted minimum risk portfolio layer

the level of portfolio risk as a fun tion of time, and nd
a similarity between the risk

urve and the

urves of the

11
12

in luded in these portfolios are lo ated

θ=0
θ = 1/4
θ = 1/2
θ = 3/4

11
10

tral vertex.

loser to the

en-

entral node is used, the av-

erage values of the weighted portfolio layer lP (t, θ) for

θ = 0, 1/2, 1/2, 3/4 are 6.03, 5.70, 5.11 and 4.72, respe tively. Similarly, for a dynami

9

entral node, we obtain

the values of 5.68, 5.34, 4.78 and 4.37. We have not in-

8

layer

When stati

luded the weighted portfolio layer for θ
7

not very informative.

maximum return portfolio

6

omprises only one asset (the

maximum return asset in the

5

= 1, as it is

This is due to the fa t that the
urrent time window) and,

therefore, lP (t, θ = 1) u tuates wildly as the maximum

4

return asset

hanges over time.

We believe these results to have potential for pra ti-

3

al appli ation. Due to the

2

1984

1986

1988

1990

1992

1994

1996

1998

time (year)
Figure 12:

lP (t, θ) for dierent values of θ.

seems plausible that
ment. These dynami

mean orrelation oe ient ρ̄ and normalized tree length
L. Earlier, when the smaller dataset of 116 sto ks - onsisting primarily important industry giants - was used,
orrelation

orrelation between the risk

oe ient ρ̄(t) to be 0.82, while

that between the risk and the normalized tree length L(t)
was −0.90. Therefore, for that dataset, the normalized
tree length was able to explain the diversi ation potential of the market better than the mean
oe ient. For the

orrelation

urrent set of 477 sto ks, whi h in-

ludes also less inuential

ompanies, the Pearson's linear

and Spearman's rank-order

orrelation

tween the risk and the mean

orrelation

oe ients beoe ient are

0.86 and 0.77, and those between the risk and the normalized tree length are -0.78 and -0.65, respe tively. It
should be noted again that the minimum spanning tree
with only N − 1 elements represents a pruned version
of the entire system of N (N − 1)/2 elements.

Further,

as N in reases, the proportion of elements in the tree
to the elements in the

ompanies of the same

luster fa e

similar risks, imposed by the external e onomi
the

and the mean

lusters with busi-

ness se tors as dened by a third party institution, it

Plots of the weighted minimum risk portfolio layer

we found Pearson's linear

lustering properties of the

MST, as well as the overlap of tree

ompanies, in

environ-

risks inuen e the sto k pri es of

oarse terms, leading to their

lustering

in the MST. In addition, the radial lo ation of sto ks depends on the

hosen portfolio risk level,

hara terized by

the value of θ . Sto ks in luded in low risk portfolios are
onsistently lo ated further away from the

entral node

than those in luded in high risk portfolios. Consequently,
the radial distan e of a node, i.e. its o
meaningful. Thus, it
of a

ompany

an be

upation layer, is

onje tured that the lo ation

within the luster ree ts its position with

regard to internal, or

luster spe i , risk. Chara teriza-

tion of sto ks by their bran h, as well as their lo ation
within the bran h, enables us to identify the degree of inter hangeability of dierent sto ks in the portfolio. For
example, in most

ases we

ferent asset tree

lusters, but from nearby layers, and in-

ould pi k two sto ks from dif-

ter hange them in the portfolio without
tering the
nami

onsiderably al-

hara teristi s of the portfolio. Therefore, dy-

asset trees provide an intuition-friendly approa h

to and fa ilitate

in orporation of subje tive judgment in

the portfolio optimization problem.

orrelation matrix gets less and,

onsequently, the tree is based on a smaller fra tion of
the available information. Therefore, although our ear-

VIII.

SUMMARY AND CONCLUSION

lier nding is not reprodu ed here to the same extent, the
result does indi ate the strength of pruning the applied
methodology is able to provide.

In summary, we have studied the distribution of
relation

So far, we have only examined the lo ation of sto ks in

or-

oe ients and found that the mean and the

varian e of the distribution are positively

orrelated, as

the minimum risk portfolio, for whi h θ = 0. As we in-

well as the skewness and the kurtosis. We have also stud-

rease θ towards unity, portfolio risk as a fun tion of time

ied the dynami s of asset trees and applied it to portfo-

soon starts behaving very dierently from the mean

or-

relation

oe ient and normalized tree length as shown

in Fig.

12.

Consequently, it is no longer useful in de-

lio analysis.

We have shown that the tree evolves over

time and have found that the normalized tree length dereases and remains low during a

rash, thus implying

s ribing diversi ation potential of the market. However,

the shrinking of the asset tree parti ularly strongly dur-

another interesting result emerges: The average weighted

ing a sto k market

portfolio layer lP (t, θ) de reases for in reasing values of

mean o

θ.

This means that out of all the possible Markowitz

risis. We have also found that the

upation layer u tuates as a fun tion of time,

and experien es a downfall at the time of market

risis

portfolios, the minimum risk portfolio sto ks are lo ated

due to topologi al

hanges in the asset tree. Further, our

furthest away from the

entral vertex, and as we move to-

studies of the s ale free stru ture of the MST show that

wards portfolios with higher expe ted return, the sto ks

this graph is not only hierar hi al in the sense of a tree

12

but there are spe ial, highly

onne ted nodes and the hi-

erar hi al stru ture is built up from these.

As for the

Only two

ompanies, Halliburton (HAL) and S hlum-

berger (SLB), are

portfolio analysis, it was found that the sto ks in luded

ment.

in the minimum risk portfolio tend to lie on the outskirts

Health- are

lassied as Oil Well Servi es & Equip-

luster :

of the asset tree: on average the weighted portfolio layer

omplete Health- are

an be almost one and a half levels higher, or further

wards the upper left

away from the

entral vertex, than the mean o

layer for window width of four years.

upation

are se tor

LHealth- are(t∗ ) ≈ 0.98. The inluster extends from the

enter to-

orner of the tree. All seven Health-

ompanies, Pzer (PFE), Eli Lilly (LLY),

Correlation be-

Mer k & Co. (MRK), Johnson & Johnson (JNJ), Bristol-

tween the risk and the normalized tree length was found

Myers Squibb (BMY), Ameri an Home Produ ts (AHP)

to be strong, though not as strong as the
tween the risk and the mean
we

orrelation

orrelation be-

oe ient. Thus

on lude that the diversi ation potential of the mar-

ket is very

losely related to the behavior of the normal-

ized tree length. Finally, the asset tree

an be viewed as

a highly graphi al tool, and even though it is strongly
pruned, it still retains all the essential information of the
market and

an be used to add subje tive judgment to

the portfolio optimization problem.

and Pharma ia (PHA), are
industry.

lassied in the Major Drugs

As the remaining four health

operate in dierent industries, this

are

ompanies

luster is

omplete

industry wise.

Utilities
teen

luster : LUtilities(t∗ ) ≈ 1.01. A total of thir-

ompanies belong to the Utilities business se tor,

represented by the blue asterisks. Twelve of them
found in the in omplete Utilities
diagonally from the

an be

luster, whi h extends

enter to the top right

orner of the

tree. Williams Companies (WMB) is the only

ompany

that is not part of it, but is lo ated in a sibling bran h

A knowledgments

instead. WMB along with Peoples Energy (PGL) are assigned to the Natural Gas Utilities industry, where as all

J.-P. O. is grateful to European S ien e Foundation for

other Utilities se tor

ompanies are assigned to Ele tri

REACTOR grant to visit Hungary, the Budapest Uni-

Utilities industry.

versity of Te hnology and E onomi s for the warm hos-

part of the main bran h in the tree.

pitality and Laszlo Kullmann for stimulating dis ussions.

Basi

Further, the role of Harri Toivonen at the Department of
A

ounting, Helsinki S hool of E onomi s, is a knowl-

edged for

arrying out CRSP database extra tions. J.-P.

O. is also grateful to the Graduate S hool in Computational Methods of Information Te hnology (ComMIT),
Finland.

The authors are also grateful to R. N. Man-

tegna for very useful dis ussions and suggestions. This
resear h was partially supported by the A ademy of Finland, Resear h Center for Computational S ien e and
Engineering, proje t no.

44897 (Finnish Center of Ex-

ellen e Programme 2000-2005) and OTKA (T029985).

Materials

There are thirteen

This

an explain why WMB is not

luster :

LBasi materials (t∗ ) ≈ 1.03.

ompanies in the Basi

Materials se -

tor, eleven of whi h are members of the bran h on the
right hand side of the tree. In the in omplete Basi

Ma-

terials

om-

luster, we

an identify a smaller sub-bran h

prising Al oa (AA), Phelps Dodge (PD), Homestake Mining (HM) and In o (N). AA, PD and N are in the Metal
Mining industry and HM in the Gold & Silver industry.
These are the only four

ompanies within the Basi

Ma-

terials se tor that provide mining raw materials. Another
interesting sub-bran h is that of Georgia-Pa i
(GP), Weyerhaeuser (WY), Louisiana-Pa i
Boise Cas ade (BCC). These

Group

(LPX) and

ompanies fun tion in the

strongly related industries of Paper & Paper Produ ts
Appendix A

and Forestry & Wood Produ ts.
more sub-bran h, namely the

The ve sample

We

an identify one

onne ted pair of DuPont

lusters that were identied in the asset
∗
tree of Figure 5 for t = t , orresponding to 1.1.1998,

lo ated at the beginning of the main Basi

are examined here in

bran h. Both

loser detail. It is emphasized that

for purposes of visualization, the tree was

onstru ted

from a smaller dataset of 116 S&P 500 sto ks. It is also

de Nemours (DD) and Dow Chemi al Company (DOW),
Materials

ompanies are in the Chemi als Plasti s&

Rubber industry. In the Basi

Materials

luster, the are

three

ompanies in luded that have a dierent business

important to bear in mind that the words business se tor

se tor

lassi ation from Basi

and industry are

Caterpillar (CAT) and Deere & Company (DE), belong

lassi ations assigned by a third party

institution, in this

ase Forbes [14℄. In

ontrast, the word

Materials. Two of them,

to the Capital Goods business se tor and Constru tion

luster is used to mean a bran h or part of a bran h in the

& Agri ultural Ma hinery industry.

tree, where most nodes are members of a single business

the bran h

se tor.

Energy

Their position in

an be substantiated by their relian e on this

luster for raw materials. The third ex eption in the Ba-

luster :

LEnergy(t∗ ) ≈ 0.92.

In the dataset

si

Materials se tor is International Paper (IP), whi h is

ompanies operating in the Energy se -

lo ated in front of the GP-WY-(LPX,BCC) sub-bran h.

tor, represented by red asterisks in Figure 5. They form a

IP belongs to the the Consumer/Non-Cy li al se tor and

there are eleven
omplete Energy
the

luster, whi h extends diagonally from

enter to the bottom left

dustry

orner of the tree. The in-

lassi ations are mainly Oil & Gas Operations.

within that to the O e Supplies industry.
seems natural that a paper
together with

Again, it

ompany should be lo ated

ompanies that provide its basi

materials.

13

Te hnology
ample of a

luster :

LTe hnology(t∗ ) ≈ 1.07.

learly in omplete

Te hnology business se tor

An ex-

luster is a group of ve

ompanies extending diago-

but they are mainly distributed around General Ele tri .

The ve

ompanies of the Te hnology

luster are

grouped together most probably be ause of their involve-

orner.

ment with semi ondu tor industry. Their industries are

These ve te hnology giants, IBM (IBM), Texas Instru-

either Semi ondu tors or Computer Hardware and Com-

ments (TXN), Hewlett-Pa kard (HWP), Computer S i-

puter Servi es. Motorola as one of the most important

nally from the

enter towards the bottom right

en es Corp. (CSC) and Motorola (MOT) form the Te h-

mobile phone manufa turers is

nology

Communi ations Equipment, a eld where similar

luster. There are eight other te hnology

nies (by business se tor) in the set of

ompa-

ompanies studied,

[2℄ L. Kullmann, J. Kertész and R. N. Mantegna, Physi a A
and

M.

Marsili,

preprint

available

at

Plerou et al., preprint available at

ond-mat/9902283

[14℄ Forbes at

http://www.forbes. om/, referen ed in Mar h-

April, 2002.
[15℄ Supplementary material on the dataset is available at

(1999).
[5℄ W. B. Arthur, S. N. Durlauf and D. A. Lane (eds.),
The e onomy as an evolving

omplex system II, Addison-

Wesley, Reading, Massa husetts (1997).
[6℄ N. Vandewalle, F. Brisbois and X. Tordoir, Quantitative

&

Poor's

500

http://www.standardandpoors. om/,

index

at

referen ed

in

June, 2002.
(2002).
[18℄ S. N. Dorogovtsev and J. F. F. Mendes, Advan es in

16, 45 (1989).

[8℄ S. Gallu io, J. -P. Bou haud and M. Potters, Physi a A
259, 449 (1998); A. Gabor and I. Kondor, Physi a A
274, 222 (1999); L. Bongini et al., Eur. Phys. J. B 27,

Taxonomy of Finan ial Assets, M. S . The-

sis, Helsinki University of Te hnology, Finland (2002).
[10℄ J.-P. Onnela, A. Chakraborti, K. Kaski and J. Kertész,

Physi s 51, 1079-1187 (2002).
[19℄ G. Szabó, M. Alava, and J. Kertész, Phys. Rev. E 66,
026101 (2002).
[20℄ M.

Marsili,

preprint

available

at

ond-mat/0207156

(2002).
[21℄ I. Yang, H. Jeong, B. Kahng and A.-L. Barabasi, preprint
available at

ond-mat/0301513 (2003).

Matlab

[22℄ Several software pa kages based on standard pro edures

Physi a A (in press, 2002).
[11℄ S. Drozdz et al., preprint available at

http://www.l e.hut./~jonnela/.

[16℄ Standard

[17℄ R. Albert and A.-L. Barabasi, Rev. Mod. Phys. 74, 47-97

Finan e 1, 372-374 (2001).
[7℄ G. Kim and H.M. Markowitz, J. Portfolio Management

[9℄ J.-P. Onnela,

[13℄ J.-P. Onnela, A. Chakraborti, K. Kaski and J. Kertész,
Eur. Phys. J. B 30, 285-288 (2002).

ond-mat/0204202 (2002).
[4℄ L. Laloux et al., Phys. Rev. Lett. 83, 1467 (1999); V.

263 (2002).

[12℄ J.-P. Onnela, A. Chakraborti, K. Kaski and J. Kertész,
in preparation (2003).

287, 412 (2000).

Giada

om-

peten ies are required as in the previous two.

(1999).

[1℄ R. N. Mantegna, Eur. Phys. J. B 11, 193 (1999).

[3℄ L.

lassied industry-wise as

ond-mat/9911168

are available. We used

with Finan ial Toolbox.

