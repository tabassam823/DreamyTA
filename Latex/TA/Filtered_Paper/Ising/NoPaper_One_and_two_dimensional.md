One- and two-dimensional
Ising model
Statistical Physics Seminar by Prof. Wolschin

Anton Kabelac
08.11.2021

Abstract
The Ising model is one of the most important models in statistical physics. It is analytically
exactly solvable in one and two dimensions. In this extended summary of a seminar
presentation, the one- and two-dimensional Ising models are presented and main aspects
such as phase transitions are discussed. Further the historical background and modern
applications of the Ising model are outlined.

1

1

Basic idea of the model

The Ising model is a theoretical model in statistical physics that was originally developed
to describe ferromagnetism. A system of magnetic particles can be modeled as a linear
chain in one dimension or a lattice in two dimension, with one molecule or atom at each
lattice site i. To each molecule or atom a magnetic moment is assigned that is represented
in the model by a discrete variable

i.

Each ’spin’

The two possible values indicate whether two spins
( i·

j = +1) or anti-parallel ( i ·

j =

can only have a value of
i and

i = ±1.

j are align and thus parallel

1).

A system of two spins is considered to be in a lower energetic state if the two magnetic
moments are aligned. If the magnetic moments points in opposite directions they are
consider to be in a higher energetic state. Due to this interaction the system tends to
align all magnetic moments in one direction in order to minimise energy. If nearly all
magnetic moments point in the same direction the arrangement of molecules behaves like
a macroscopic magnet.
A phase transition in the context of the Ising model is a transition from an ordered state
to a disordered state. A ferromagnet above the critical temperature TC is in a disordered
state. In the Ising model this corresponds to a random distribution of the spin values.
Below the critical temperature TC (nearly) all spins are aligned, even in the absence of an
external applied magnetic field H. If we heat up a cooled ferromagnet, the magnetization
vanishes at TC and the ferromagnet switches from an ordered to a disordered state. This
is a phase transition of second order.

2

Historical Background

The Ising model was invented in 1920 by Wilhelm Lenz, which is why its also referred
to as the Lenz-Ising or Ising-Lenz model. Lenz was a German physicist, also notable for
his application of the Laplace–Runge–Lenz vector. He was at Rostock University in 1920,
but the following year he was appointed ordinary professor at Hamburg. One of his first
students was Ernst Ising.

2

Ising started his dissertation on the investigation of ferromagnetism, summarized in a short paper written in
1924 and published [1] in 1925. Ising carried out an exact calculation for the special case of a one-dimensional
lattice. His analysis showed that there was no phase
transition to a ferromagnetic ordered state at any finite temperature. Ising wrongly predicted, that a phase
transition also does not occur in higher dimensions.
This lead to initial rejection of the Lenz-Ising model
form the physical community, including Ising himself.
Figure 1: Ernst Ising
When Werner Heisenberg proposed his own theory of
ferromagnetism in 1928, he said:
”Ising succeeded in showing that also the assumption of directed sufficiently
great forces between two neighboring atoms of a chain is not sufficient to explain
ferromagnetism.”
[2]
The Lenz-Ising model became more relevant in 1936, when Rudolf Peierl showed that the
2d version must have a phase transition at finite temperature [3]. Finally in 1944 the twodimensional Ising model without an external field was solved analytically by Lars Onsager
by a transfer-matrix method.

3

One dimensional Ising model

The one-dimensional Ising model is an chain of spins. Each spin
value of

can only have a discrete

i = ±1. The index i marks the position of the spin in the chain.

3

Figure 2: Ising chain
Like Ising did in 1924 [1] we will take a look at the simplest possible case of the onedimensional Ising model. Our goal is to investigate if a phase transition occures, explaining
spontaneous magnetisation and thus ferromagnetism. We will introduce two conditions.
• No external magnetic field H
• Each spin can only interact with its neighboring spin.
We will later refer to the second condition as only nears neighboring interactions (NN).
The interaction strength between two spins

i and

i+1 is characterised by the coupling

strength J. The Hamiltonian H of such a system is than given by
X
(1) H = J
i j
<ij>

with the nears neighboring sum < ij >. For a system with Ntot lattice sites and two
possible

i -values at each lattice site, a total number of 2

Ntot

possible configurations of the

arrangement of particles exists. Summing over all possible configurations i then yields the
partition sum Z:
X
(2) Z =
e H
{i}

=

X

X

1 =±1

2 =±1

...

X

e J( 1 2 + 2 3 + 3 4 ...)

N =±1

In order to simplify eq. (2) we introduce a new variable µi :=

i·

i+1 , describing whether

two neighbouring spins are parallel or anti-parallel. The Hamiltonian (1) and the partition
sum (2) can now be rewritten without a NN sum:
(3)

H=

J

X
i

µi

)

Z =2·

X
{µ}

e

J

N
P

i=1

µi

4

The factor of 2 in the partition function arises from the two possible configurations for the
first spin in the chain.
In the thermodynamic limit (N >> 1) we can simplify the partition function:
(4)

Z =2·
=2·
=2·

X

e

{µ}

X

J

NP1

µi

i=1

X

µ1 =±1 µ2 =±1

X

X

...

X

µN

µ1 =±1 µ2 =±1

1 =±1

X

...

µN

e J(µ1 +µ2 +...+µN 1 )
e J(µ1 +µ2 +...+µN 2 )

2 =±1

X

µN

|

e JµN 1

1 =±1

{z

(e J +e

J

With the relation e J + e J = 2cosh( J) it follows:
X X
X
(5) Z = 2 ·
...
e J(µ1 +µ2 +...+µN 2 ) 2 cosh ( J)
µ1 =±1 µ2 =±1

µN

)

}

2 =±1

= 2 [2 cosh ( J)]N 1
N

1

⇡ [2 cosh ( J)]N

This is our final result for the partition function of the one-dimensional Ising model without
an external field.
Newt we want to show that in this simple case no phase transition at a finite temperature
occurs. The average spin in the chain is given by:
1X
H
(6) < i > =
ie
Z
{ }

The more interesting case is to average alignment of two spins
necessarily have to be neighbors.
1 X
(7) < i i+j > =
i i+j e
Z

i and

i+j , that don not

H

{ }

In order to simplefy eq. (7) we introduce a di↵erent coupling constant Ji for each spin
pair.
(8)

<

i i+j > =

1 X
Z

i

i+j e

{ }

=

X
1 X
...
Z =±1
=±1
1

i

H

X

i+1 =±1

...

X

N =±1

i i+j e

(J1 1 2 +J2 2 3 +J3 3 4 ...)

5

Next we rewrite the product

i ·

i+j in terms of bonds rather than spins.

product of any spin with itself ( i ·
(9)

i·

i+j =

=

i · 1 · ... · 1 ·
i · ( i+1 ·

i = 1) is always equal to one.

i+j

i+1 ) · ( i+2 · ... ·

i+j 2 ) · ( i+j 1 ·

i+j 1 ) ·

= ( i · i+1 ) · ( i+1 · i+2 ) ·... · ( i+j 2 · i+j 1 ) · ( i+j 1 ·
| {z } |
{z
}
|
{z
} |
{z
µi

µi+1

µi+j

µi+j

2

i+j
i+j )
1

Combining eq. (8) and eq. (9) yields:
(10) <

i i+j > =

1 X
Z

i

Note that the

i+j e

}

H

{ }

=

1
[2 cosh ( J1 ) · ... · 2 sinh ( Ji ) · ... · 2 sinh ( Ji+j 1 ) · ... · 2 cosh ( JN 1 )]
Z

The partition function Z for di↵erent coupling constant Ji for each spin pair can be calculated analogue to eq.(1-5):
(11) ) <

i i+j >

cosh ( J1 ) · ... · sinh ( Ji ) · ... · sinh ( Ji+j 1 ) · ... · cosh ( JN 1 )
cosh ( J1 ) · ... · cosh ( Ji ) · ... · cosh ( Ji+j 1 ) · ... · cosh ( JN 1 )
j
Y
=
tanh ( Ji+m 1 )
=

m=1

If we go back to a constant coupling constant Ji = J the result becomes:
(12) <

i i+j > = [tanh (

J)]j

All that’s left to do is to look at the temperature dependent magnetisation M of the system
(13) M = m N <
M 2 = m2 N 2 <

>
>2 = m2 N 2 lim <
j!1

i i+j > =

0

8T >0

with the magnetic moment of each spin m, the number of spins in the system N and the
average spin <

>.

Because tanh ( J)  1 the expression in eq. (12) becomes zero for large j. The only
exception is at T = 0, where the tanh ( J) diverges. So to be precise one have to say
that a phase transition in the one-dimensional Ising model does not occur at a finite
temperature.

6

4

Transfer Matrix

The next question we are going to answer is what happens to our system if we apply an
external magnetic field H that can interact with the magnetic moment m of each spin. The
Hamiltonian of such a system becomes:
(14) H =

X

J

i

j

mH

<ij>

X

i

i

It is helpful to assume periodic boundary conditions ( N +1 = 1), closing the one-dimensional
Ising chain to a ring. We define a transfer matrix in the following way:
H( 1 , 2 , 3 ,...)

(15) e

E( N , 1 )
N 1, N )
= e| E({z1 , 2}) e| E({z2 , 3}) ... e| E( {z
} e| {z }
T1,2

T2,3

So each transfer matrix is given by:
✓
1
(16) Ti,i+1 = exp
J i i+1 + H ( i +
2

TN

i+1 )

1,N

TN,1

◆

Every spin can have two possible values so our transfer matric becomes a 2⇥2 matrix.
!
!
T+1,+1 T+1, 1
e J+H e J
(17) Ti,i+1 =
=
T 1,+1 T 1, 1
e J e J H
Now we can write down the partition function in terms of the transfer matrices
(18) Z =

X

e

H

{i}

=

X

Ti,i+1

{i}

=

X

1 =±1

X

2 =±1

...

X

T1,2 T2,3 ...TN 1,N TN,1

N =±1

Remember that matrix multiplication is defined as (AB)ik =

P

j Aij Bjk . If we zoom in on

the multiplication between the 1-2 transfer matrix and the 2-3 transfer matrix, we see that
the transfer matrices are being multiplied by each other when we sum over their shared
index
(19)

2:

X
2

T1,2 T2,3 = (T · T ) 1 3

7

So when we sum over

2 , those two transfer matrices ”collapse” together and we’re left

with a squared transfer matrix between spin

1 and spin

3.

If we repeat this process of

”collapsing” all the transfer matrices together, we end up with
(20) Z =

X
1

(T
T · ... · T}) 1 1 ,
| · T · {z
N times

which we recognize as the formula for the trace of T N ,
⇥ ⇤
(21) Z = tr T N =

N
1 +

N
2

The two eigenvalues of the transfer matrix (eq. 17) are
h
i
p
J
2
2
J
(22) 1,2 = e
cosh(H) ± cosh (H) 2 e
sinh(2 J) .

In the thermodynamic limit the partition function simplifies even further. Only the larger
eigenvalues

1 is relevant.

(23) Z = lim

N !1

N
1

1+

✓

2
1

◆N !

=

N
1

Thus we have arrived at an exact solution for the one dimension Ising model with external
field.

5

Two Dimensional Ising Model and Peirls Proof

The two-dimensional Ising model is defined on a two dimensional lattice. The Hamiltonian
of the system is:
(24) H =

J

X

<ij>

i

j

mH

X

i

i

One of the main di↵erences between the one- and two-dimensional is the amount of nears
neighbours. In the two-dimensional case each spin has four NN.

8

5.1

Proof of Peirls Theorem

In contrast to the one-dimensional Ising model, the two-dimensional case does show a
phase transition, or to be more precise a phase transitions at a finite temperature. A phase
transition means, that our system of spins shows magnetisation without any external field.

Figure 3: Schematic plot of a phase transition in a system of magnets.
In fig. 3 the magnetisation M is plotted against an outer magnetic field. On the left the
temperature T is above a critical temperature Tc and on the right temperature T is below
a critical temperature Tc . The existence of a phase transition is means that this critical
temperature exists.

To proof the existence of a phase transition we have
to show that the system tends to be magnetised, even
without or with a small external field. Magnetisation
means the alignment of spin states. A small, external
magnetic field is implemented by fixing all spins on the
outer layer into on spin state, lets say to plus spins
( 1 = +1). The idea is visualized in fig. (4). The idea
behind Peirls proof is now to look at the spin in the
center of our system. If a phase transition occurs and
the system tends to magnetise, the probability of the
spin in the center of our system being anti-parallel to
the outer spins should become zero.

Figure 4: Arrangement of spins

9

We define ⌫ as a configuration of spins in our system. Further we define two sets of spin
configurations. ⌦ is the set of all configuration, where the outer spins are all spin up. The
subset ⌦0 includes all configurations ⌫, where the outer spins are spin up (+) and the spin
in the center of the system is spin down (-). In order to proof the existence of a phase
transition we have to show that the probability of any configuration ⌫ lying in ⌦0 diverges
to zero in the thermodynamic limit.

Figure 5: di↵erent sets of spin configurations
If we take a closer look into any configuration ⌫ 2 ⌦, we can see islands of minus spins
in a sea of plus spins. As we can see in fig. 6 the island of minus spins can include lakes
of plus spins. Note the red lines that separate the lake of plus spins from the islands of
minus spins. Those are so called ”shorelines”. If two spins
shoreline, their product

i·

j is always equal to

i and

j are seperated by a

1.

Figure 6: Schematic zoom in a spin configuration
With the definition of a shoreline in mind we define a third set of spin configurations ⌦S ,
where the outer spins are all plus spins, the spin in the center of the system is a minus
spin, and we have any fixed shoreline surrounding the spin in the center. Because it is

10

rather hard to estimate the probability of a spin configuration ⌫ lying in ⌦0 directly, we
estimate the probability for ⌫ 2 ⌦S first. To get the probability of ⌫ 2 ⌦0 we than sum
over all di↵erent shoreline arrangements.

The probability of ⌫ 2 ⌦S can be obtained by simple counting.
(25) Prob (⌫ 2 ⌦S ) =

1 X
e
Z⌦ ⌫2⌦

H⌫

S

1 X
=
exp
Z⌦ ⌫2⌦
S

"

J

X

<ij>

i j

#

Next we separate the NN sum in the exponential function into spin pairs that are separated
by the shoreline in the center and into those who are not. The number of spin pairs that
are separated by the shoreline is nothing else than just the length of the shoreline n(S).
2
3
X
X
1
5
(26) Prob (⌫ 2 ⌦S ) =
exp [
J n(S)] exp 4 J
i j
Z⌦ ⌫2⌦
<ij>2S
/

S

However the last term is rather hard to calculate. So we need to estimate an more explicit
expression. For this we look at a spin configuration ⌫ 2 ⌦S and flip all spins inside the
shoreline surrounding the centering spin. We note this system as ⌦0S .

Figure 7: Flipping spins

11
The NN sum of two neighboring spins in the flipped system ⌦0S can be split into spin pairs
that are separated by the shoreline and those who are not:
(27) 8 ⌫ 0 2 ⌦0S :

X

0
i

X

0
j =

<ij>

0
i

0
j

+

X

<ij>2S

<ij>2S
/

|

{z

n(S)

0
i

0
j

}

Using the property of the shoreline discussed above ( i ·

j

=

1, if the two spins are

separated by S), we see that the fallowing statement holds true :
X

(28)

0
i

0
j =

<ij>2S
/

X

i

j

<ij>2S
/

Rearranging eq. 27 and using the that the length of the shoreline n(S) is always positive
yields:
(29)

X

<ij>2S
/

i

j =

X

0
i

0
j

<ij>

n(S) <

X

0
i

0
j

<ij>

Now that we found a expression for the sum we can plug eq. 29 in eq. 26.
2
3
X
X
1
5
(30) Prob (⌫ 2 ⌦S ) =
exp [
J n(S)] exp 4 J
i j
Z⌦ ⌫2⌦
<ij>2S
/
S
"
#
X
1 X
0 0
<
exp [
J n(S)] exp
J
i j
Z⌦ 0 0
<ij>
⌫ 2⌦S
"
#
X
X
1
0 0
= e J n(S)
exp
J
i j
Z⌦ 0 0
<ij>
⌫ 2⌦S
"
#
X
X
1
= e J n(S)
exp
J
i j
Z⌦ ⌫2⌦
<ij>
S
"
#
X
X
1
< e J n(S)
exp
J
i j
Z⌦ ⌫2⌦
<ij>
=e

J n(S)

So far we have obtained the probability of a spin configuration ⌫ laying in the set ⌦S . To
get the wanted probability of a spin configuration ⌫ laying in the set ⌦0 we need to sum

12

over the set of all possible arrangements of shorelines ⌘.
X
(31) Prob (⌫ 2 ⌦0 ) =
Prob (⌦S )
S2⌘

<

X

e

J n(S)

S2⌘

Because the notation of the sum is vague we replace the sum over the set of all possible
arrangements of shorelines ⌘ by a sum over all shorelines of a certain length s(n).
(32) Prob (⌫ 2 ⌦0 ) <

1
X

s(n) e

J n(S)

n=1

The factor s(n) gives the amount of di↵erent shoreline configurations for any length n. It
can by obtained by looking at closed random walks:
1
(33) s (n) < n 4n
2
Combining eq. 32 and 33 yields our final result.
(34) Prob (⌫ 2 ⌦0 ) <
<

1
X

s(n) e

J n(S)

n=1

1
X
1

2
n=1

n 4n e

J n(S)

1

1X
n
=
n 4| e{z J}
2 n=1
x

Because x < 1 this geometric series converges to (1 xx)2 . To the probability that the spin
in the center is a minus spin in a system where the outer spins are all plus spins is given
by:
(35) Prob (⌫ 2 ⌦0 ) <

1
4e J
2 (1 4 e J )2

!1

!

0

Thus have proven that for sufficiently low temperatures all spins in the systems tend to
align even without an external magnetic field.

6

Applications

Due to its rather simple concept and the existence of analytical solutions the Ising model
has been successfully applied in many field of science. One example is the description of

13

DNA structures in polymer biology like done in [4].
A recently relevant application of the one-dimensional Ising model is the spread of diseases.
In [5] it has been used to model the speed of contamination. The ”spin” in this context
are infected or non infected people.
In its almost 100 year old history the Ising model has been applied to a vast number of
di↵erent systems making it to one of the most important models in statistical physics.

References
[1] E. Ising. “Beitrag zur Theorie des Ferromagnetismus”. In: Z. Physik 31, 253 (1925).
[2] S.G. Brush. “History of the Lenz-Ising model”. In: Rev. Mod. Phys. 36, 856 (1967).
[3] R. Peierls. “Ising’s model of ferromagnetism”. In: Proc. Cambridge Phil. Soc. 32, 477
(1936).
[4] M. Leung, F. Choo, and B. Tong. “Application of modified Ising model to the helix-coil
transition of DNA molecules”. In: Biopolymers. 16(6):1233-44 (1977).
[5] I. Mello et al. “Epidemics, the Ising-model and percolation theory: a comprehensive
review focussed on Covid-19”. In: Physica A p. 125963 (2021).
[6] U. Schwarz. “Theoretical statistical physics”. University Lecture. Winter term 2019/20.
[7] T. Fließbach. Statistische Physik : Lehrbuch zur Theoretischen Physik IV. Berlin:
Springer Spektrum, (2018).
[8] T.D. Schultz, E. Lieb, and D.C. Mattis. “Two dimensional Ising model as a soluble
model of many fermions”. In: Rev. Mod. Phys. 36, 856 (1964).

