U NIVERSITY OF C ALIFORNIA
Los Angeles

Learning in Large–Scale Games
and Cooperative Control

A dissertation submitted in partial satisfaction
of the requirements for the degree
Doctor of Philosophy in Mechanical Engineering

by

Jason Robert Marden

2007

c Copyright by
Jason Robert Marden
2007

The dissertation of Jason Robert Marden is approved.

Gürdal Arslan

Robert M’Closkey

Jason L. Speyer

Jeff S. Shamma, Committee Chair

University of California, Los Angeles
2007

ii

To my family . . .
whose love and support have guided me through the years

iii

TABLE OF C ONTENTS

1

2

Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

1

1.1

Main Contributions of this Dissertation . . . . . . . . . . . . . . . .

6

Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

9

2.1

Finite Strategic-Form Games . . . . . . . . . . . . . . . . . . . . . .

9

2.2

Forms of Equilibrium . . . . . . . . . . . . . . . . . . . . . . . . . .

10

2.2.1

Nash Equilibrium . . . . . . . . . . . . . . . . . . . . . . . .

10

2.2.2

Correlated Equilibrium . . . . . . . . . . . . . . . . . . . . .

11

2.2.3

Coarse Correlated Equilibrium . . . . . . . . . . . . . . . . .

12

2.2.4

Equilibrium Comparison . . . . . . . . . . . . . . . . . . . .

14

Classes of Games . . . . . . . . . . . . . . . . . . . . . . . . . . . .

15

2.3.1

Identical Interest Games . . . . . . . . . . . . . . . . . . . .

16

2.3.2

Potential Games . . . . . . . . . . . . . . . . . . . . . . . .

16

2.3.3

Congestion Games . . . . . . . . . . . . . . . . . . . . . . .

17

2.3.4

Weakly Acyclic Games . . . . . . . . . . . . . . . . . . . . .

18

Repeated Games . . . . . . . . . . . . . . . . . . . . . . . . . . . .

19

2.4.1

Full Information Learning Algorithms . . . . . . . . . . . . .

20

2.4.2

Virtual Payoff Based Learning Algorithms . . . . . . . . . .

20

2.4.3

Payoff Based Learning Algorithms . . . . . . . . . . . . . . .

21

Joint Strategy Fictitious Play with Inertia for Potential Games . . . . .

22

3.1

23

2.3

2.4

3

Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

iv

3.2

4

Joint Strategy Fictitious Play with Inertia . . . . . . . . . . . . . . .

27

3.2.1

Fictitious Play . . . . . . . . . . . . . . . . . . . . . . . . .

27

3.2.2

Setup: Joint Strategy Fictitious Play . . . . . . . . . . . . . .

28

3.2.3

Convergence to Nash Equilibrium . . . . . . . . . . . . . . .

33

3.3

Fading Memory JSFP with Inertia . . . . . . . . . . . . . . . . . . .

34

3.4

Congestion Games and Distributed Traffic Routing . . . . . . . . . .

37

3.4.1

Distributed Traffic Routing . . . . . . . . . . . . . . . . . . .

38

3.4.2

Incorporating Tolls to Minimize the Total Congestion . . . . .

40

3.5

Concluding Remarks and Future Work . . . . . . . . . . . . . . . . .

43

3.6

Appendix to Chapter 3 . . . . . . . . . . . . . . . . . . . . . . . . .

45

3.6.1

Proof of Theorem 3.2.1 . . . . . . . . . . . . . . . . . . . . .

45

. . . . . . . . . . .

55

4.1

Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

55

4.2

Regret Matching . . . . . . . . . . . . . . . . . . . . . . . . . . . .

58

4.2.1

Coarse Correlated Equilibria and No-Regret . . . . . . . . . .

59

4.2.2

Illustrative Example . . . . . . . . . . . . . . . . . . . . . .

61

4.3

Regret Based Dynamics with Fading Memory and Inertia . . . . . . .

62

4.4

Simulations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

65

4.4.1

Three Player Identical Interest Game . . . . . . . . . . . . .

65

4.4.2

Distributed Traffic Routing . . . . . . . . . . . . . . . . . . .

66

4.5

Concluding Remarks and Future Work . . . . . . . . . . . . . . . . .

69

4.6

Appendix to Chapter 4 . . . . . . . . . . . . . . . . . . . . . . . . .

69

Regret Based Dynamics for Weakly Acyclic Games

v

4.6.1
5

Proof of Theorem 4.3.1 . . . . . . . . . . . . . . . . . . . . .

69

Payoff Based Dynamics for Weakly Acyclic Games . . . . . . . . . . . .

75

5.1

Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

76

5.2

Payoff Based Learning Algorithms . . . . . . . . . . . . . . . . . . .

79

5.2.1

Safe Experimentation Dynamics for Identical Interest Games .

79

5.2.2

Simple Experimentation Dynamics for Weakly Acyclic Games

82

5.2.3

Sample Experimentation Dynamics for Weakly Acyclic Games

5.3

with Noisy Utility Measurements . . . . . . . . . . . . . . .

89

Influencing Nash Equilibria in Resource Allocation Problems . . . . .

99

5.3.1

99

5.4

Illustrative Example – Braess’ Paradox . . . . . . . . . . . . . . . . . 102

5.5

Concluding Remarks and Future Work . . . . . . . . . . . . . . . . . 106

5.6

Appendix to Chapter 5 . . . . . . . . . . . . . . . . . . . . . . . . . 108
5.6.1

6

Congestion Game with Tolls Setup . . . . . . . . . . . . . . .

Background on Resistance Trees . . . . . . . . . . . . . . . . 108

Connections Between Cooperative Control and Potential Games . . . . 110
6.1

Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111

6.2

Cooperative Control Problems and Potential Games . . . . . . . . . . 113

6.3

Consensus Modeled as a Potential Game . . . . . . . . . . . . . . . . 116
6.3.1

Setup: Consensus Problem with a Time-Invariant and Undirected Interaction Graph . . . . . . . . . . . . . . . . . . . . 116

6.3.2

A Learning Algorithm for Potential Games with Suboptimal
Nash Equilibria . . . . . . . . . . . . . . . . . . . . . . . . . 119

vi

6.3.3

A Learning Algorithm for Potential Games with Suboptimal
Nash Equilibria and Restricted Action Sets . . . . . . . . . . 120

6.3.4

Example: Consensus in an Environment with Non-convex Obstructions . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123

6.4

6.5

Weakly Acyclic and Sometimes Weakly Acyclic Games . . . . . . . . 124
6.4.1

Weakly Acyclic Games . . . . . . . . . . . . . . . . . . . . . 125

6.4.2

Learning Dynamics for Weakly Acyclic Games . . . . . . . . 127

6.4.3

Sometimes Weakly Acyclic Games . . . . . . . . . . . . . . 128

6.4.4

Learning Dynamics for Sometimes Weakly Acyclic Games . . 128

Consensus Modeled as a Sometimes Weakly Acyclic Game . . . . . . 130
6.5.1

Setup: Consensus Problem with a Time-Varying and Directed
Interaction Graph . . . . . . . . . . . . . . . . . . . . . . . . 131

6.5.2
6.6

6.7

Extension to Multi-Dimensional Consensus . . . . . . . . . . 134

Group Based Decision Processes for Potential Games . . . . . . . . . 135
6.6.1

Spatial Adaptive Play with Group Based Decisions . . . . . . 135

6.6.2

Restricted Spatial Adaptive Play with Group Based Decisions

6.6.3

Constrained Action Sets . . . . . . . . . . . . . . . . . . . . 139

138

Functional Consensus . . . . . . . . . . . . . . . . . . . . . . . . . . 139
6.7.1

Setup: Functional Consensus Problem with Group Based Decisions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 140

6.7.2

Group Utility Function . . . . . . . . . . . . . . . . . . . . . 141

6.7.3

Group Selection Process and Action Constraints . . . . . . . 142

6.7.4

Illustration . . . . . . . . . . . . . . . . . . . . . . . . . . . 143

vii

6.8

6.9
7

Illustrative Examples . . . . . . . . . . . . . . . . . . . . . . . . . . 143
6.8.1

Dynamic Sensor Coverage Problem . . . . . . . . . . . . . . 143

6.8.2

Sudoku . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 147

Concluding Remarks . . . . . . . . . . . . . . . . . . . . . . . . . . 153

Conclusions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 155

References

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 159

viii

L IST OF F IGURES
2.1

Example of a Finite Strategic-Form Game . . . . . . . . . . . . . . .

2.2

Relationship Between Nash, Correlated, and Coarse Correlated Equi-

10

libria. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

14

2.3

Example of an Identical Interest Game . . . . . . . . . . . . . . . . .

15

2.4

Example of a Potential Game with Potential Function . . . . . . . . .

17

2.5

Example of a Weakly Acyclic Game . . . . . . . . . . . . . . . . . .

19

3.1

Fading Memory JSFP with Inertia: Congestion Game Example – Network Topology . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

3.2

Fading Memory JSFP with Inertia: Evolution of Number of Vehicles
on Each Route . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

3.3

38

39

Fading Memory JSFP with Inertia: Evolution of Congestion Cost on
Each Route . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

40

3.4

Example of a Driver Adjustment Process . . . . . . . . . . . . . . . .

41

3.5

Fading Memory JSFP with Inertia: Evolution of Total Congestion Experienced by All Drivers with and without Tolls. . . . . . . . . . . . .

44

4.1

A 3−player Identical Interest Game. . . . . . . . . . . . . . . . . . .

61

4.2

Evolution of the actions of players using RB. . . . . . . . . . . . . .

65

4.3

Regret Based Dynamics with Inertia: Congestion Game Example –
Network Topology . . . . . . . . . . . . . . . . . . . . . . . . . . .

4.4

66

Regret Based Dynamics with Inertia: Evolution of Number of Vehicles
on Each Route . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

ix

67

4.5

Regret Based Dynamics with Inertia: Evolution of Congestion Cost on
Each Route . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

68

5.1

Construction of alternative to tree rooted in X. . . . . . . . . . . . . .

87

5.2

Construction of alternative to tree rooted in D for Case (2). . . . . . .

88

5.3

Construction of alternative to tree rooted in D for Case (1). . . . . . .

89

5.4

Congestion Game Setup – Braess’ Paradox . . . . . . . . . . . . . . 102

5.5

Illustration of Nash Equilibrium in Braess’ Paradox. . . . . . . . . . . 103

5.6

Braess’ Paradox: Evolution of Number of Vehicles on Each Road Using Simple Experimentation Dynamics . . . . . . . . . . . . . . . . . 104

5.7

Braess’ Paradox: Congestion Game Setup with Tolls to Minimize Total Congestion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105

5.8

Braess’ Paradox: Evolution of Number of Vehicles on Each Road Using Simple Experimentation Dynamics with Optimal Tolls . . . . . . 106

5.9

Braess’ Paradox: Comparison of Evolution of Number of Vehicles on
Each Road Using Simple Experimentation Dynamics and Sample Experimentation Dynamics (baseline) with Noisy Utility Measurements . 107

6.1

Example: Setup of a Consensus Problem with Restricted Action Sets
and Non-convex Environmental Obstructions. . . . . . . . . . . . . . 124

6.2

Example: Evolution of the Action Path in the Consensus Problem with
Restricted Action Sets and Non-convex Environmental Obstructions. . 125

6.3

Evolution of Each Player’s Action in the Average Consensus Problem

6.4

Illustration of Reward Function Over Mission Space . . . . . . . . . . 145

x

144

6.5

Illustration of Sensor Coverage and Range Restricted Action Sets of a
Particular Sensor . . . . . . . . . . . . . . . . . . . . . . . . . . . . 146

6.6

Final Allocation of Sensors over Mission Space . . . . . . . . . . . . 148

6.7

Evolution of Potential Function over Mission . . . . . . . . . . . . . 148

6.8

Illustration of a Sudoku Puzzle . . . . . . . . . . . . . . . . . . . . . 149

6.9

Illustration of Neighbor Sets for a Player’s Utility Function in a Sudoku Puzzle . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 150

6.10 Evolution of Potential Function in Sudoku Puzzle Under the Learning
Algorithm Spatial Adaptive Play . . . . . . . . . . . . . . . . . . . . 152
6.11 The Completed Sudoku Puzzle . . . . . . . . . . . . . . . . . . . . . 152
6.12 Spatial Adaptive Play on a Sudoku Puzzle Classified as Very Hard . . 153

xi

L IST OF TABLES
2.1

Relationship Between Nash, Correlated, and Coarse Correlated Equilibria. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

xii

14

ACKNOWLEDGMENTS
Words cannot even begin to express the gratitude that I feel towards my family, friends,
colleagues and mentors for their unconditional support, encouragement and guidance
over the past six years. This thesis could not have been completed without all of you.
When I started graduate school at UCLA, I knew very little about my new advisor,
Jeff Shamma. All that I knew about Jeff was that I enjoyed talking to him and that he
promised me a free round of golf, which I am still waiting for to this day. Six years
later, I now realize how extremely fortunate I am to have had the opportunity to get to
work with Jeff. Jeff is one of the most sincere and caring individuals that I have ever
met in my life. Jeff took me under his wing like a father would do to his own son.
He guided, mentored, and provided me with a wealth of opportunities that ultimately
changed the direction of my life forever. I can never repay Jeff for all that he has done
for me. Thank you, Jeff. I am so proud to call you my academic father.
I was extremely fortunate to not have just one advisor, but rather two. My second
advisor, Gürdal Arslan, or “G” as the local Hawaiians call him, came into my life
about four years ago at a time when I began to question both life and my ambition for
research. Gürdal always made time for me, challenged me, and ultimately helped me
grow as both an individual and a researcher. Gürdal, through his “harnessed optimism”
and attention to detail, i.e., “first sentence, third paragraph... third sentence, third
paragraph...,” taught me discipline, patience, and precision in the research process.
Gürdal is now one of my best friends and will continue to be for the rest of my life.
Thank you for everything G. Andy’s on me!
During my graduate school experience, I became interested in the field of learning
in games largely due to the work of H. Peyton Young. While attending a game theory
conference in New York in July of 2006, Peyton agreed to meet with me to discuss

xiii

my research. We went on to have several interesting research conversations in addition
to writing a journal paper together. Thank you Peyton for making the time to work
with and mentor a non-economic graduate student. I have thoroughly enjoyed our
conversations and I hope that we can continue to work together for many more years
to come.
I have had the pleasure of learning from and interacting with several fantastic professors over the past six years, including but not limited to Munther Dahleh, Robert
M’Closkey, Jason Speyer, T.C. Tsao, and Web Marner. In addition to academia, I
have also had two fantastic mentors while working in industry, Greg Becker and John
Abedor. I want to thank all of you for your time and support. I would also like to
acknowledge the funding sources that made my research experience possible: NSF
grants #CMS–0339228 and #ECS-0501394, ARO Grant #W911NF–04–1–0316 and
AFOSR grant #FA9550-05-1-0239.
Sharing the graduate school experience with my lab mates and fellow colleagues
has given me a lifetime of fantastic memories. Our research conversations over boba
and coffee breaks have contributed significantly to this dissertation in addition to my
personal growth. To my main man George, or the “Algebra Guy” as the women call
him, your dedication and work ethic have inspired me tremendously over the past five
years. Ibrahim, you have definitely taught me valuable lessons in both life and the
art of debating. Whenever I hear the words, “well not exactly ...,” I will always think
of you. Shalom, you’ve always been there to offer me your “sound” advice, which
thankfully I have not followed. Talk about .... in a bag. Mike, you were always the
one person that I could always talk to about my graduate school experiences. I really
felt that we were on the same page with so many issues. To Li Na and Clay, as you
start your doctoral journey, you are a reminder that the academic life cycle continues
and the future is so bright. And lastly to Dr. Jonathan Wolfe, whose life ended all too

xiv

soon, your love for life and your optimism will be an inspiration to me for the rest of
my life. You will always be remembered.
My friends and family were the reason why I was able to persevere through the
six year grind of graduate school. I am so fortunate to be blessed with such a wonderful group of friends who have shared this experience with me over the years. To
Nick, my brother Brian, Big Boy, my cousins Jon and Michael, Annie, Tommy, Mark,
Steve, Jeff, Dustin, and Terri, thank you for always being there for me. Your support,
encouragement, and perpetual jokes about my lifelong student status will always be
remembered. I have thoroughly enjoyed sharing this experience with each one of you
and I am so grateful to have all of you in my life.
My family has been my pillar of strength for my entire life, especially during my
graduate studies. To Mom and Dad, you have given me so much over the years that I
do not even know where to begin. You have always been there for me, cared for me
and loved me. Both of you are the reason why I am here today. This dissertation is
truly a tribute to your dedication in raising me. You have inspired me to be a better
son, husband, and hopefully one day, a father. I love you with all my heart and I am so
proud to have you both as my parents. To my Grams, your warm heart and kindness
will live with me for the rest of my life. You are a constant reminder of the true essence
of life – love and happiness.
To my beloved wife Nancy, you are the love of my life. Thank you for standing
with me for the past five years as I pursued my dreams. Your unconditional love
and support has provided me with the strength to overcome each obstacle. You have
inspired me in so many ways by your kindness, generosity, compassion and sincerity.
You have opened my eyes and my heart to a more fulfilling and meaningful life. You
have truly been my guiding light. I have grown so much as person with you by my
side and I am so blessed to have you in my life.

xv

Lastly, I want to thank God for making all of this possible.

xvi

V ITA

May 1, 1978

Born, Panorama City, California

1997 – 2007

Multi-Disciplined Engineer, Raytheon Systems Corporation, El Segundo, California.

2001

B. S., Mechanical Engineering (Cum Laude), University of California, Los Angeles.

2001

Graduate Fellowship, Department of Mechanical and Aerospace
Engineering, University of California, Los Angeles.

2002 – 2007

Research Assistant, Department of Mechanical and Aerospace Engineering, University of California, Los Angeles.

2003 – 2006

Teaching Assistant, Department of Mechanical and Aerospace Engineering, University of California, Los Angeles.

2004

M. S., Mechanical Engineering, University of California, Los Angeles.

2004–2007

Engineering Consultant, InfoLenz Corporation, Cambridge, Massachusetts.

2006

Visiting Researcher, Department of Electrical Engineering, University of Hawaii at Manoa.

2007

Postdoctoral Fellowship, Social and Information Sciences Laboratory, California Institute of Technology, Pasadena, California.

xvii

P UBLICATIONS

J. R. Marden and G. Arslan and J. S. Shamma. “Joint Strategy Fictitious Play with
Inertia for Potential Games.” In Proceedings of the 44th IEEE Conference on Decision
and Control, pp. 6692–6697, December 2005.

J. R. Marden and G. Arslan and J. S. Shamma. “Regret based dynamics: Convergence
in Weakly Acyclic Games.” In Proceedings of the 2007 International Conference on
Autonomous Agents and Multiagent Systems (AAMAS), May 2007.

J. R. Marden and G. Arslan and J. S. Shamma. “Connections Between Cooperative
Control and Potential Games Illustrated on the Consensus Problem.” In Proceedings
of the 2007 European Control Conference (ECC ’07), July 2007.

G. Arslan, J. R. Marden, and J. S. Shamma. “Autonomous vehicle-target assignment:
a game theoretical formulation.” ASME Journal of Dynamic Systems, Measurement
and Control, 2007.

xviii

A BSTRACT OF THE D ISSERTATION

Learning in Large–Scale Games
and Cooperative Control
by

Jason Robert Marden
Doctor of Philosophy in Mechanical Engineering
University of California, Los Angeles, 2007
Professor Jeff S. Shamma, Chair

Many engineering systems can be characterized as a large scale collection of interacting subsystems each having access to local information, making local decisions,
having local interactions with neighbors, and seeking to optimize local objectives that
may well be in conflict with other subsystems. The analysis and design of such control systems falls under the broader framework of “complex and distributed systems”.
Other names include “multi-agent control,” “cooperative control,” “networked control,” as well as “team theory” or “swarming.” Regardless of the nomenclature, the
central challenge remains the same. That is to derive desirable collective behaviors
through the design of individual agent control algorithms. The potential benefits of
distributed decision architectures include the opportunity for real-time adaptation (or
self-organization) and robustness to dynamic uncertainties such as individual component failures, non-stationary environments, and adversarial elements. These benefits
come with significant challenges, such as the complexity associated with a potentially
large number of interacting agents and the analytical difficulties of dealing with overlapping and partial information.

xix

This dissertation focuses on dealing with the distributed nature of decision making and information processing through a non-cooperative game-theoretic formulation.
The interactions of a distributed/multi-agent control system are modeled as a noncooperative game among agents with the desired collective behavior being expressed
as a Nash equilibrium. In large scale multi-agent systems, agents are inherently limited in both their observational and computational capabilities. Therefore, this dissertation focuses on learning algorithms that can accommodate these limitations while
still guaranteeing convergence to a Nash equilibrium. Furthermore, in this dissertation
we illustrate a connection between the fields of game theory and cooperative control
and develop several suitable learning algorithms for a wide variety of cooperative control problems. This connection establishes a framework for designing and analyzing
multi-agent systems. We demonstrate the potential benefits of this framework on several cooperative control problems including dynamic sensor coverage, consensus, and
distributing routing over a network, as well as the mathematical puzzle Sudoku.

xx

CHAPTER 1
Overview
Many engineering systems can be characterized as a large scale collection of interacting subsystems each having access to local information, making local decisions,
having local interactions with neighbors, and seeking to optimize local objectives that
may well be in conflict with other subsystems. A representative sampling includes autonomous vehicle teams, cooperative robotics, distributed computing, electronic commerce, wireless networks, sensor networks, traffic control, social networks, and combat systems.
The analysis and design of such control systems falls under the broader framework
of “complex and distributed systems”. Other names include “multi-agent control,”
“cooperative control,” “networked control,” as well as “team theory” or “swarming.”
Regardless of the nomenclature, the central challenge remains the same. That is to
derive desirable collective behaviors through the design of individual agent control
algorithms. The potential benefits of distributed decision architectures include the
opportunity for real-time adaptation (or self-organization) and robustness to dynamic
uncertainties such as individual component failures, non-stationary environments, and
adversarial elements. These benefits come with significant challenges, such as the
complexity associated with a potentially large number of interacting agents and the
analytical difficulties of dealing with overlapping and partial information.
This dissertation focuses on dealing with the distributed nature of decision making and information processing through a non-cooperative game-theoretic formulation.

1

The interactions of a distributed/multi-agent control system are modeled as a noncooperative game among agents, with the desired collective behavior being expressed
as a Nash equilibrium. The emphasis is on simple learning algorithms that guarantee
convergence to a Nash equilibrium. Furthermore, the algorithms must have minimal
computational requirements to accommodate implementation in a wide variety of engineered systems.
The need for simple learning algorithms can be motivated by looking at the problem of distributed routing over a network. In such a problem, there is a large number
of self interested players seeking to utilize a common network. Since the available resources in the network are finite, players’ objectives are very much in conflict with one
another. The sheer quantity of available information makes centralized dissemination
or processing infeasible. When modeling the players’ interaction as a non-cooperative
game, the central issue involves how players make decisions. Or more precisely, what
information do players need to base their decisions on so as to guarantee some form of
a collective behavior? For example, does each player need to know the routing strategies of all other players or would some form of aggregate information be acceptable?
Motivated by the inherent information restrictions in the problem of distributed
routing over networks, in Chapter 3 we consider multi-player repeated games involving a large number of players with large strategy spaces and enmeshed utility structures. In these “large-scale” games, players are inherently faced with limitations in
both their observational and computational capabilities. Accordingly, players in largescale games need to make their decisions using algorithms that accommodate limitations in information gathering and processing. This disqualifies some of the well
known decision making models such as “Fictitious Play” (FP) [MS96a], in which each
player must monitor the individual actions of every other player and must optimize
over a high dimensional probability space.

2

In this chapter, we analyze the properties of the learning algorithm Joint Strategy
Fictitious Play (JSFP), a close variant of FP. We demonstrate that JSFP alleviates both
the informational and computational burden of FP. Furthermore, we introduce JSFP
with inertia, i.e., a probabilistic reluctance to change strategies, and establish the convergence to a pure Nash equilibrium in all generalized ordinal potential games in both
cases of averaged or exponentially discounted historical data. We illustrate JSFP with
inertia on the specific class of congestion games, a subset of generalized ordinal potential games. In particular, we illustrate the main results on a distributed traffic routing
problem.
In Chapter 4, we extend the results of JSFP by introducing an entire class of learning algorithms that can accommodate such observational and processing restrictions.
To that end, we build upon the idea of no-regret algorithms [HM00] to strengthen the
performance guarantees for implementation in multi-agent systems. No-regret algorithms have been proposed to control a wide variety of multi-agent systems. The appeal
of no-regret algorithms is that they are easily implementable in large scale multi-agent
systems because players make decisions using only regret based information. Furthermore, there are existing results proving that the collective behavior will asymptotically
converge to a set of points of “no-regret” in any game. We illustrate, through a simple example, that no-regret points need not reflect desirable operating conditions for a
multi-agent system.
Multi-agent systems often exhibit an additional structure, i.e., being weakly acyclic,
that has not been exploited in the context of no-regret algorithms. In this chapter, we
introduce a modification of the traditional no-regret algorithms by (i) exponentially
discounting the memory and (ii) bringing in a notion of inertia in players’ decision
process. We show how these modifications can lead to an entire class of regret based
algorithms that provide almost sure convergence to a pure Nash equilibrium in any

3

weakly acyclic game.
The last, and most informationally restrictive, class of learning algorithms that
we will consider in this dissertation are payoff based algorithms. In such a scenario,
players only have access to (i) the action they played and (ii) the utility (possibly
noisy) they received. In a transportation network, this translates to drivers only having
information about the congestion actually experienced. Drivers are now unaware of
the traffic conditions on any alternative routes, which was previously a requirement
for the implementation of either JSFP or any regret based learning algorithm.
In Chapter 5, we focus on payoff based learning algorithms on the specific class of
weakly acyclic games. We introduce three different payoff based processes for increasingly general scenarios and prove that after a sufficiently large number of stages, player
actions constitute a Nash equilibrium at any stage with arbitrarily high probability. The
first learning algorithm, called Safe Experimentation, guarantees convergence to an optimal Nash equilibrium in any identical interest game. Such an equilibrium is called
optimal because it maximizes the payoff to all players. The second learning algorithm,
called Simple Experimentation, guarantees convergence to a Nash equilibrium in any
weakly acyclic game. The third learning algorithm, called Sample Experimentation,
guarantees convergence to a Nash equilibrium in any weakly acyclic game even in the
presence of noisy utility functions.
The second topic of Chapter 5 is centered around the inefficiency of Nash equilibria in routing problems. It is well known that a Nash equilibrium may not represent
a desirable operating point in a routing problem as it typically does not minimize the
total congestion on the network. Motivated by this inefficiency concern, we derive an
approach for modifying player utility functions through tolls and incentives in congestion games, a special class of weakly acyclic games, to guarantee that a centralized
objective can be realized as a Nash equilibrium. We illustrate this equilibrium refine-

4

ment method on a well studied distributed routing problem known as Braess’ Paradox.
In the following chapter, the focus shifts from the development of suitable learning
algorithms to understanding how one would design a multi-agent systems for a cooperative control problem. In particular, how would a global planner design each agent’s
local utility function such that a central objective could be realized as the outcome
of a repeated non-cooperative game? We seek to answer this question by highlighting a connection between cooperative control problems and potential games. This
connection to potential games provides a structural framework with which to study
cooperative control problems and suggests an approach for utility design. However,
we would like to note that utility design for multi-agent systems is still very much an
open issue.
In Chapter 6, we present a view of cooperative control using the language of learning in games. We review the game theoretic concepts of potential games and weakly
acyclic games and demonstrate how several cooperative control problems such as consensus, dynamic sensor coverage, and even the mathematical puzzle Sudoku can be
formulated in these settings. Motivated by this connection, we build upon game theoretic concepts to better accommodate a broader class of cooperative control problems.
In particular, we introduce two extensions of the learning algorithm Spatial Adaptive
Play. The first extension called binary Restricted Spatial Adaptive Play accommodates
restricted action sets caused by limitations in agent capabilities. The second extension called Spatial Adaptive Play with Group Based Decisions accommodates group
based collaborations in the decision making process. Furthermore, we also introduce
a new class of games, called sometimes weakly acyclic games, for time-varying utility functions and action sets, and provide distributed algorithms for convergence to an
equilibrium.
Lastly, we illustrate the potential benefits of this connection on several cooper-

5

ative control problems. For the consensus problem, we demonstrate that consensus
can be reached even in an environment with non-convex obstructions. For the functional consensus problem, we demonstrate an approach that will allow agents to reach
consensus on a specific consensus point which is some function of the initial conditions. For the dynamic sensor coverage problem, we demonstrate how autonomous
sensors can distribute themselves using only local information in such a way as to
maximize the probability of detecting a particular event over a given mission space.
Lastly, we demonstrate how the popular mathematical game of Sudoku can be modeled as a noncooperative game and solved using the learning algorithms discussed in
this dissertation.

1.1

Main Contributions of this Dissertation

To summarize, we will now restate the main contributions of this dissertation.
• We introduce the learning algorithm Joint Strategy Fictitious Play with inertia
and establish almost sure convergence to a pure Nash equilibrium in all generalized ordinal potential games in both cases of averaged or exponentially discounted historical data.
• We introduce a modification of the traditional no-regret algorithms by (i) exponentially discounting the memory and (ii) bringing in a notion of inertia in
players’ decision process. We show how these modifications can lead to an entire class of regret based algorithms that provide almost sure convergence to a
pure Nash equilibrium in any weakly acyclic game.
• We introduce the payoff based algorithm Safe Experimentation and establish
almost sure convergence to an optimal Nash equilibrium in any identical interest
game.

6

• We introduce the payoff based algorithm Simple Experimentation and establish
almost sure convergence to a pure Nash equilibrium in any weakly acyclic game.
• We introduce the payoff based algorithm Sample Experimentation and establish
almost sure convergence to a pure Nash equilibrium in any weakly acyclic game
even in the presence of noisy utility functions.
• We derive an approach for modifying player utility functions through tolls and
incentives in congestion games to guarantee that a centralized objective can be
realized as a Nash equilibrium.
• We establish a connection between potential games and cooperative control and
demonstrate the potential benefits of this connection on several cooperative control problems including dynamic sensor coverage, consensus, and distributing
routing over a network, as well as the mathematical puzzle Sudoku.
• We derive an equivalent definition for weakly acyclic games that explicitly highlights the connection between weakly acyclic and potential games.
• We introduce an extension of the learning algorithm Spatial Adaptive Play, called
binary Restricted Spatial Adaptive Play, to accommodate restricted action sets
caused by agent limitations. We establish probabilistic convergence to an action
profile that maximizes the potential function in any potential game.
• We introduce an extension of the learning algorithm Spatial Adaptive Play, called
Spatial Adaptive Play with Group Based Decisions, to accommodate group based
collaborations in the decision making process. We establish probabilistic convergence to an action profile that maximizes the potential function in any potential
game.

7

• We introduce a new class of games, called sometimes weakly acyclic games, for
time-varying utility functions and action sets, and provide distributed algorithms
for almost sure convergence to a universal Nash equilibrium.

8

CHAPTER 2
Background
In this section, we will present a background of the game theoretic concepts used in this
dissertation. We refer the readers to [FT91, You98, You05] for a more comprehensive
review.

2.1

Finite Strategic-Form Games

We consider a finite strategic-form game with n-player set P := {P1 , ..., Pn } where
each player Pi ∈ P has an action set Ai and a utility function Ui : A → R where
A = A1 × · · · × An . We will refer to a finite strategic-form game as just a game and
we will sometimes use a single symbol, e.g., G, to represent the entire game, i.e., the
player set, P, action sets, Ai , and utility functions Ui .
An example of a two player game is illustrated in matrix form in Figure 2.1. In this
game, each player has two actions or strategies and a utility function represented by
the payoff matrix. Once each player has selected his action, both players receive their
associated reward. For example, if player 1 choose Top and player 2 choose Down,
player 1 would receive a reward of 2 while player 2 would receive a reward of 1.
For an action profile a = (a1 , a2 , ..., an ) ∈ A, let a−i denote the profile of player
actions other than player Pi , i.e.,
a−i = {a1 , . . . , ai−1 , ai+1 , . . . , an } .

9

Player 2
chooses Up

Player 2
chooses Down

Player 1
chooses Top

0,0

2,1

Player 1
chooses Bottom

1,2

0,0

Payoff Matrix

Figure 2.1: Example of a Finite Strategic-Form Game

With this notation, we will sometimes write a profile a of actions as (ai , a−i ). SimQ
ilarly, we may write Ui (a) as Ui (ai , a−i ). Furthermore, let A−i = Pj 6=Pi Ai denote the set of possible collective actions of all players other than player Pi and let
P−i = {P1 , . . . , Pi−1 , Pi+1 , . . . , Pn } denote the set of players other than player Pi .

2.2

Forms of Equilibrium

In this section we will introduce three forms of equilibrium that will be discussed in
this dissertation: Nash equilibrium, correlated equilibrium (CE), and coarse correlated
equilibrium (CCE).

2.2.1

Nash Equilibrium

The most well known form of an equilibrium is the Nash equilibrium.
Definition 2.2.1 (Pure Nash Equilibrium). An action profile a∗ ∈ A is called a pure
Nash equilibrium if for all players Pi ∈ P,
Ui (a∗i , a∗−i ) = max Ui (ai , a∗−i ).
ai ∈Ai

10

(2.1)

Furthermore, if the above condition is satisfied with a unique maximizer for every
player Pi ∈ P, then a∗ is called a strict Nash equilibrium.
A Nash equilibrium represents a scenario for which no player has an incentive to
unilaterally deviate.
The concept of Nash equilibrium also extends to mixed strategy spaces. Let the
strategy of player Pi be defined as pi ∈ ∆(Ai ), where ∆(Ai ) is the set of probability
distributions over the finite set of actions Ai . We will adopt the convention that pai i
P
represents the probability that player Pi will select action ai and ai ∈Ai pai i = 1. If all
players Pi ∈ P play independently according to their personal strategy pi ∈ ∆(Ai ),
then the expected utility of player Pi for strategy pi is defined as
Ui (pi , p−i ) =

X

Ui (a)pa11 pa22 . . . pann ,

a∈A

where p−i = {p1 , . . . , pi−1 , pi+1 , . . . , pn } denotes the collection of strategies of players
other than player Pi .
Definition 2.2.2 (Nash Equilibrium). A strategy profile p∗ = {p∗1 , . . . , p∗n } is called a
Nash equilibrium if for all players Pi ∈ P,
Ui (p∗i , p∗−i ) = max

pi ∈∆(Ai )

2.2.2

Ui (pi , p∗−i ).

(2.2)

Correlated Equilibrium

In this section we will define a broader class of equilibria for which there may be correlations among the players. To that end, let z ∈ ∆(A) denote a probability distribution
over the set of joint actions A. We will adopt the convention that z a is the probability
P
of the joint action a and a∈A z a = 1. In the special case that all players Pi ∈ P play
independently according to their personal strategy pi ∈ ∆(Ai ), as was the case in the

11

definition of the Nash equilibrium, then
z a = pa11 pa22 . . . pann ,
where a = (a1 , a2 , . . . , an ).
Definition 2.2.3 (Correlated Equilibrium). The probability distribution z is a correlated equilibrium if for all players Pi ∈ P and for all actions ai , a0i ∈ Ai ,
X

X

Ui (ai , a−i )z (ai ,a−i ) ≥

a−i ∈A−i

Ui (a0i , a−i )z (ai ,a−i ) .

(2.3)

a−i ∈A−i

To motivate this definition consider the following scenario. First, a joint action
a ∈ A is randomly drawn according to the probability distribution z ∈ ∆(A). Next,
each player is informed of only his particular action ai , but not the actions of the other
players. Finally, each player is given the opportunity to change his action. The condition for correlated equilibrium in (2.3) states that each player Pi ’s conditional expected
payoff for action ai is at least as good as his conditional expected payoff for any other
action a0i 6= ai . In other words, a probability distribution z is a correlated equilibrium
if and only if no player would seek to change their action from the outcome, randomly
drawn according to z, even after his part has been revealed.
Notice that all Nash equilibria are in fact correlated equilibria.

2.2.3

Coarse Correlated Equilibrium

We will now relax the requirements on correlated equilibrium. Before doing so, we
will discuss marginal distributions. Given the joint distribution z ∈ ∆(A), the marginal
distribution of all players other than player Pi is
a

z−i−i =

X

0

z (ai ,a−i ) .

a0i ∈Ai

Note that z−i is a well defined probability distribution in ∆(A−i ).

12

Definition 2.2.4 (Coarse Correlated Equilibrium). The probability distribution z is
a coarse correlated equilibrium if for all players Pi ∈ P and for all actions a0i ∈ Ai ,
X

X

Ui (a)z a ≥

a

Ui (a0i , a−i )z−i−i .

(2.4)

a−i ∈A−i

a∈A

To motivate this definition, consider the following scenario which differs slightly
from the correlated equilibrium scenario. Before the joint action a is drawn, each
player Pi is given the opportunity to opt out, in which case the player can select any
action ai ∈ Ai that he wishes. If the player does not opt out, he commits himself to
playing his part of the action-tuple a randomly drawn according to the distribution z.
In words, a distribution z is a coarse correlated equilibrium if under this scenario no
player would choose to opt out given that all other players opt to stay in.
If the joint distribution z is a correlated equilibrium, then we know that for any
action a0i ∈ Ai
X

X

Ui (ai , a−i )z (ai ,a−i ) ≥

ai ∈Ai a−i ∈A−i

X

X

Ui (a0i , a−i )z (ai ,a−i ) ,

ai ∈Ai a−i ∈A−i

X

=

Ui (a0i , a−i )

a−i ∈A−i

X

=

X

z (ai ,a−i ) ,

ai ∈Ai
a

Ui (a0i , a−i )z−i−i .

a−i ∈A−i

This implies that for any action a0i ∈ Ai
X
a∈A

Ui (a)z a ≥

X

a

Ui (a0i , a−i )z−i−i .

a−i ∈A−i

Therefore, all correlated equilibria, and hence Nash equilibria, are in fact coarse correlated equilibria as illustrated in Figure 2.2. Under the condition that all players select
their action independently, as was the case in the definition of the Nash equilibrium,
then the definition of correlated, coarse correlated, and Nash equilibria are all equivalent.

13

Nash

Correlated

Coarse
Correlated

Figure 2.2: Relationship Between Nash, Correlated, and Coarse Correlated Equilibria.

2.2.4

Equilibrium Comparison

The main difference between Nash, correlated, and coarse correlated equilibria is
whether a player is committed conditionally or unconditionally to a random draw of
a given joint distribution z ∈ ∆(A). Table 2.1, taken from [You05], summarizes the
main differences between the three forms of equilibria.
Conditional Participation

Unconditional Participation

Independent Probabilities

Nash

Nash

Correlated Probabilities

Correlated

Coarse Correlated

Table 2.1: Relationship Between Nash, Correlated, and Coarse Correlated Equilibria.

We will now present a simple two player example, from [You05], to highlight
the differences between the set of Nash equilibria and the set of correlated or coarse
correlated equilibria. Note that the set of correlated equilibria and the set of coarse
correlated equilibria are equivalent in two player games.
Consider the following two player game with payoff matrix as illustrated if Figure 2.3. For any joint action, the first entry is the payoff for player 1 and the second
entry is the payoff for player 2. For example, U1 (L, L) = 1 and U2 (L, L) = 1.
Let z = {z LL , z LR , z RL , z LL } be a probability distribution over the joint action space
A = {LL, LR, RL, RR}.

14

P2

P2
L

R

L

1,1

0,0

R

0,0

1,1

P1

L

R

L

zLL

zLR

R

zRL

zRR

P1

Payoff Matrix

Joint Distribution

Figure 2.3: Example of an Identical Interest Game

In this example, there are two strict Nash equilibria, (L, L) and (R, R). FurtherR
more, there is one mixed Nash equilibrium, pL1 = pL2 = 1/2 and pR
1 = p2 = 1/2. A

joint distribution z is a correlated equilibrium if and only if the off-diagonal probabilities do not exceed the diagonal probabilities, i.e.,
max{z LR , z RL } ≤ min{z LL , z RR }.
Therefore, the set of correlated equilibria is significantly larger than the set of Nash
equilibria.

2.3

Classes of Games

In this dissertation we will consider four classes of games: identical interest games,
potential games, congestion games, and weakly acyclic games. Each class of games
imposes a restriction on the admissible utility functions.

15

2.3.1

Identical Interest Games

The most restrictive class of games that we will review in this dissertation is identical
interest games. In such a game, the players’ utility functions {Ui }ni=1 are chosen to be
the same. That is, for some function φ : A → R,
Ui (a) = φ(a),
for every Pi ∈ P and for every a ∈ A. It is easy to verify that all identical interest games have at least one pure Nash equilibrium, namely any action profile a that
maximizes φ(a). An example of an identical interest game is illustrated in Figure 2.3.

2.3.2

Potential Games

A significant generalization of an identical interest game is a potential game. In a
potential game, the change in a player’s utility that results from a unilateral change
in strategy equals the change in the global utility. Specifically, there is a function
φ : A → R such that for every player Pi ∈ P, for every a−i ∈ A−i , and for every
a0i , a00i ∈ Ai ,
Ui (a0i , a−i ) − Ui (a00i , a−i ) = φ(a0i , a−i ) − φ(a00i , a−i ).

(2.5)

When this condition is satisfied, the game is called a potential game with the potential
function φ. It is easy to see that in potential games, any action profile maximizing the
potential function is a pure Nash equilibrium, hence every potential game possesses at
least one such equilibrium.
An example of a two player potential game with associated potential function is
illustrated if Figure 2.4.
We will also consider a more general class of potential games known as generalized
ordinal potential games. In generalized ordinal potential games there is a function

16

P2

P2
L

R

L

2,0

3,2

R

0,0

0,1

P1

L

R

L

2

4

R

0

1

P1

Payoff Matrix

Potential

Figure 2.4: Example of a Potential Game with Potential Function

φ : A → R such that for every player Pi ∈ P, for every a−i ∈ A−i , and for every
a0i , a00i ∈ Ai ,
Ui (a0i , a−i ) − Ui (a00i , a−i ) > 0 ⇒ φ(a0i , a−i ) − φ(a00i , a−i ) > 0.

2.3.3

Congestion Games

Congestion games are a specific class of games in which player utility functions have
a special structure.
In order to define a congestion game, we must specify the action set, Ai , and
utility function, Ui (·), of each player. Towards this end, let R denote a finite set of
“resources”. For each resource r ∈ R, there is an associated “congestion function”
cr : {0, 1, 2, ...} → R
that reflects the cost of using the resource as a function of the number of players using
that resource.
The action set, Ai , of each player, Pi , is defined as the set of resources available to

17

player Pi , i.e.,
Ai ⊂ 2R ,
where 2R denotes the set of subsets of R. Accordingly, an action, ai ∈ Ai , reflects a
selection of (multiple) resources, ai ⊂ R. A player is “using” resource r if r ∈ ai . For
an action profile a ∈ A, let σr (a) denote the total number of players using resource
r, i.e., |{i : r ∈ ai }|. In a congestion game, the utility of player Pi using resources
indicated by ai depends only on the total number of players using the same resources.
More precisely, the utility of player Pi is defined as
Ui (a) =

X

cr (σr (a)).

(2.6)

r∈ai

Any congestion game with utility functions as in (2.6) is a potential game [Ros73] with
potential function
φ(a) =

r (a)
X σX

cr (k).

(2.7)

r∈R k=1

In fact, every congestion game is a potential game and every finite potential game is
isomorphic to a congestion game [MS96b].

2.3.4

Weakly Acyclic Games

Consider any finite game G with a set A of action profiles. A better reply path is a
sequence of action profiles a1 , a2 , ..., aL such that, for every 1 ≤ ` ≤ L − 1, there
`+1
`
`
is exactly one player Pi` such that i) a`i` 6= a`+1
i` , ii) a−i` = a−i` , and iii) Ui` (a ) <

Ui` (a`+1 ). In other words, one player moves at a time, and each time a player moves
he increases his own utility.
Suppose now that G is a potential game with potential function φ. Starting from
an arbitrary action profile a ∈ A, construct a better reply path a = a1 , a2 , ..., aL until
it can no longer be extended. Note first that such a path cannot cycle back on itself,

18

because φ is strictly increasing along the path. Since A is finite, the path cannot be
extended indefinitely. Hence, the last element in a maximal better reply path from any
joint action, a, must be a Nash equilibrium of G.
This idea may be generalized as follows. The game G is weakly acyclic if for any
a ∈ A, there exists a better reply path starting at a and ending at some pure Nash
equilibrium of G [You98, You05]. Potential games are special cases of weakly acyclic
games.
An example of a two player weakly acyclic game is illustrated in Figure 2.5.

2,1

1,2

0,0

2,1

1,2

0,0

-1,2

2,1

0,0

1,2

2,1

0,0

0,0

0,0

1,1

0,0

0,0

1,1

Weakly Acyclic
Under Better Replies

Not Weakly Acyclic
Under Better Replies

Figure 2.5: Example of a Weakly Acyclic Game

2.4

Repeated Games

In a repeated game, at each time t ∈ {0, 1, 2, . . . }, each player Pi ∈ P simultaneously chooses an action ai (t) ∈ Ai and receives the utility Ui (a(t)) where a(t) :=
(a1 (t), . . . , an (t)). Each player Pi ∈ P chooses his action ai (t) at time t simultaneously according to a probability distribution pi (t), which we will refer to as the strategy

19

of player Pi at time t. A player’s strategy at time t can rely only on observations from
times {0, 1, 2, ..., t − 1}. Different learning algorithms are specified by both the assumptions on available information and the mechanism by which the strategies are
updated as information is gathered.
We will review three main classes of learning algorithms in this dissertation: full
information, virtual payoff based, and payoff based. For a detailed review of learning
in games we direct the reader to [FL98, You98, You05, HS98, Wei95, Sam97].

2.4.1

Full Information Learning Algorithms

The most informationally sophisticated class of learning algorithms is full information.
In full information learning algorithms, each player knows the functional form of his
utility function and is capable of observing the actions of all other players at every time
step. The strategy adjustment mechanism of player Pi can be written in the general
form

pi (t) = Fi a(0), ..., a(t − 1); Ui .
In this setting, players may develop probabilistic models for the actions of other
players using past observations. Based off these models, players may seek to maximize
some form of an expected utility. An example of a learning algorithm, or strategy
adjustment mechanism, of this form is the well known fictitious play [MS96a]. We
will review fictitious play in Section 3.2.1.

2.4.2

Virtual Payoff Based Learning Algorithms

We will now relax the requirements of full information learning algorithms. In virtual
payoff based algorithms, players are now unaware of the structural form of their utility
function. Furthermore, players also are not capable of observing the actions of all

20

players. However, players are endowed with the ability to assess the utility that they
would have received for alternative action choices. For example, suppose that the
action played at time t is a(t). In virtual payoff based dynamics, each player Pi with
|A |

action set Ai = {a1i , ..., ai i } has access to the following information:


Ui (a1i , a−i (t))




..
a(t) ⇒ 
,
.


|A |
Ui (ai i , a−i (t))
where |Ai | denotes the cardinality of the action set Ai .
The strategy adjustment mechanism of player Pi can be written in the general form

pi (t) = Fi {Ui (ai , a−i (0))}ai ∈Ai , . . . , {Ui (ai , a−i (t − 1))}ai ∈Ai .
An example of a learning algorithm, or strategy adjustment mechanism, of this form
is the well known regret matching [HM00]. We will review regret matching in Section 4.2. Virtual payoff based learning algorithms will be the focus of Chapters 3 and
4.

2.4.3

Payoff Based Learning Algorithms

Payoff based learning algorithms are the most informationally restrictive class of learning algorithms. Now, players only have access to (i) the action they played and (ii) the
utility (possibly noisy) they received. In this setting, the strategy adjustment mechanism of player Pi takes on the form

pi (t) = Fi {ai (0), Ui (a(0))}, ..., {ai (t − 1), Ui (a(t − 1))} .
We will discuss payoff based learning algorithms extensively in Chapter 5.

21

(2.8)

CHAPTER 3
Joint Strategy Fictitious Play with Inertia for Potential
Games
In this chapter we consider multi-player repeated games involving a large number of
players with large strategy spaces and enmeshed utility structures. In these “largescale” games, players are inherently faced with limitations in both their observational
and computational capabilities. Accordingly, players in large-scale games need to
make their decisions using algorithms that accommodate limitations in information
gathering and processing. This disqualifies some of the well known decision making
models such as “Fictitious Play” (FP), in which each player must monitor the individual actions of every other player and must optimize over a high dimensional probability
space. We will show that Joint Strategy Fictitious Play (JSFP), a close variant of FP,
alleviates both the informational and computational burden of FP. Furthermore, we
introduce JSFP with inertia, i.e., a probabilistic reluctance to change strategies, and
establish the convergence to a pure Nash equilibrium in all generalized ordinal potential games in both cases of averaged or exponentially discounted historical data.
We illustrate JSFP with inertia on the specific class of congestion games, a subset of
generalized ordinal potential games. In particular, we illustrate the main results on a
distributed traffic routing problem and derive tolling procedures that can lead to optimized total traffic congestion.

22

3.1

Introduction

We consider “large-scale” repeated games involving a large number of players, each of
whom selects a strategy from a possibly large strategy set. A player’s reward, or utility,
depends on the actions taken by all players. The game is repeated over multiple stages,
and this allows players to adapt their strategies in response to the available information
gathered over prior stages. This setup falls under the general subject of “learning
in games” [FL98, You05], and there are a variety of algorithms and accompanying
analysis that examine the long term behavior of these algorithms.
In large-scale games players are inherently faced with limitations in both their
observational and computational capabilities. Accordingly, players in such large-scale
games need to make their decisions using algorithms that accommodate limitations in
information gathering and processing. This limits the feasibility of different learning
algorithms. For example, the well-studied algorithm “Fictitious Play” (FP) requires
individual players to individually monitor the actions of other players and to optimize
their strategies according to a probability distribution function over the joint actions of
other players. Clearly, such information gathering and processing is not feasible in a
large-scale game.
The main objective of this chapter is to study a variant of FP called Joint Strategy
Fictitious Play (JSFP) [FL98, FK93, MS97]. We will argue that JSFP is a plausible
decision making model for certain large-scale games. We will introduce a modification
of JSFP to include inertia, in which there is a probabilistic reluctance of any player to
change strategies. We will establish that JSFP with inertia converges to a pure Nash
equilibrium for a class of games known as generalized ordinal potential games, which
includes so-called congestion games as a special case [Ros73].
Our motivating example for a large-scale congestion game is distributed traffic

23

routing [BL85], in which a large number of vehicles make daily routing decisions to
optimize their own objectives in response to their own observations. In this setting,
observing and responding to the individual actions of all vehicles on a daily basis
would be a formidable task for any individual driver. A more realistic measurement
on the information tracked and processed by an individual driver is the daily aggregate
congestion on the roads that are of interest to that driver [BPK91]. It turns out that
JSFP accommodates such information aggregation.
We will now review some of the well known decision making models and discuss
their limitations in large-scale games. See the monographs [FL98, You98, You05,
HS98, Wei95] and survey article [Har05] for a more comprehensive review.
The well known FP algorithm requires that each player views all other players
as independent decision makers [FL98]. In the FP framework, each player observes
the decisions made by all other players and computes the empirical frequencies (i.e.
running averages) of these observed decisions. Then, each player best responds to the
empirical frequencies of other players’ decisions by first computing the expected utility
for each strategy choice under the assumption that the other players will independently
make their decisions probabilistically according to the observed empirical frequencies.
FP is known to be convergent to a Nash equilibrium in potential games, but need not
converge for other classes of games. General convergence issues are discussed in
[HM03b, SA05, AS04].
The paper [LES05] introduces a version of FP, called “sampled FP”, that seeks to
avoid computing an expected utility based on the empirical frequencies, because for
large scale games, this expected utility computation can be prohibitively demanding.
In sampled FP, each player selects samples from the strategy space of every other
player according to the empirical frequencies of that player’s past decisions. A player
then computes an average utility for each strategy choice based off of these samples.

24

Each player still has to observe the decisions made by all other players to compute
the empirical frequencies of these observed decisions. Sampled FP is proved to be
convergent in identical interest games, but the number of samples needed to guarantee
convergence grows unboundedly.
There are convergent learning algorithms for a large class of coordination games
called “weakly acyclic” games [You98]. In adaptive play [You93] players have finite
recall and respond to the recent history of other players. Adaptive play requires each
player to track the individual behavior of all other players for recall window lengths
greater than one. Thus, as the size of player memory grows, adaptive play suffers from
the same computational setback as FP.
It turns out that there is a strong similarity between the JSFP discussed herein and
the regret matching algorithm [HM00]. A player’s regret for a particular choice is
defined as the difference between 1) the utility that would have been received if that
particular choice was played for all the previous stages and 2) the average utility actually received in the previous stages. A player using the regret matching algorithm
updates a regret vector for each possible choice, and selects actions according to a
probability proportional to positive regret. In JSFP, a player chooses an action by
myopically maximizing the anticipated utility based on past observations, which is effectively equivalent to regret modulo a bias term. A current open question is whether
player choices would converge in coordination-type games when all players use the
regret matching algorithm (except for the special case of two-player games [HM03a]).
There are finite memory versions of the regret matching algorithm and various generalizations [You05], such as playing best or better responses to regret over the last
m stages, that are proven to be convergent in weakly acyclic games when players use
some sort of inertia. These finite memory algorithms do not require each player to
track the behavior of other players individually. Rather, each player needs to remem-

25

ber the utilities actually received and the utilities that could have been received in the
last m stages. In contrast, a player using JSFP best responds according to accumulated experience over the entire history by using a simple recursion which can also
incorporate exponential discounting of the historical data.
There are also payoff based dynamics, where each player observes only the actual
utilities received and uses a Reinforcement Learning (RL) algorithm [SB98, BT96]
to make future choices. Convergence of player choices when all players use an RLlike algorithm is proved for identical interest games [LC03, LC05b, LC05a] assuming
that learning takes place at multiple time scales. Finally, the payoff based dynamics
with finite-memory presented in [HS04] leads to a Pareto-optimal outcome in generic
common interest games.
Regarding the distributed routing setting of Section 3.4, there are papers that analyze different routing strategies in congestion games with “infinitesimal” players, i.e.,
a continuum of players as opposed to a large, but finite, number of players. References [FV04, FV05, FRV06] analyze the convergence properties of a class of routing
strategies that is a variation of the replicator dynamics in congestion games, also referred to as symmetric games, under a variety of settings. Reference [BEL06] analyzes
the convergence properties of no-regret algorithms in such congestion games and also
considers congestion games with discrete players, as considered in this paper, but the
results hold only for a highly structured symmetric game.
The remainder of this chapter is organized as follows. Section 3.2, sets up JSFP
and goes on to establish convergence to a pure Nash equilibrium for JSFP with inertia in all generalized ordinal potential games. Section 3.3 presents a fading memory
variant of JSFP, and likewise establishes convergence to a pure Nash equilibrium. Section 3.4 presents an illustrative example for traffic congestion games. Section 3.4 goes
on to illustrate the use of tolls to achieve a socially optimal equilibrium and derives

26

conditions for this equilibrium to be unique.

3.2

Joint Strategy Fictitious Play with Inertia

Consider a finite game with n-player set P := {P1 , ..., Pn } where each player Pi ∈ P
has an action set Ai and a utility function Ui : A → R where A = A1 × ... × An .
In a repeated game as described in Section 2.4, at every stage t ∈ {0, 1, 2, ...}, each
player, Pi , simultaneously selects an action ai (t) ∈ Ai . This selection is a function of
the information available to player Pi up to stage t. Both the action selection function
and the available information depend on the underlying learning process.

3.2.1

Fictitious Play

We start with the well known Fictitious Play (FP) process [FL98]. Fictitious Play is an
example of a full information learning algorithm.
Define the empirical frequency, qiāi (t), as the percentage of stages at which player
Pi has chosen the action āi ∈ Ai up to time t − 1, i.e.,
t−1

qiāi (t) :=

1X
I{ai (τ ) = āi },
t τ =0

where ai (k) ∈ Ai is player Pi ’s action at time k and I{·} is the indicator function.
Now define the empirical frequency vector for player Pi as


ā1
q
 i 
 .. 
qi (t) :=  .  ,


ā|A |
i
qi
where |Ai | is the cardinality of the action set Ai .
The action of player Pi at time t is based on the (incorrect) presumption that other

27

players are playing randomly and independently according to their empirical frequencies. Under this presumption, the expected utility for the action āi ∈ Ai is
Ui (āi , q−i (t)) :=

X

Ui (āi , a−i )

a−i ∈A−i

Y

a

qj j (t),

(3.1)

aj ∈a−i

where q−i (t) := {q1 (t), ..., qi−1 (t), qi+1 (t), ..., qn (t)} and A−i := ×j6=i Aj . In the FP
process, player Pi uses this expected utility by selecting an action at time t from the
set
BRi (q−i (t)) := {ãi ∈ Ai : Ui (ãi , q−i (t)) = max Ui (ai , q−i (t))}.
ai ∈Ai

The set BRi (q−i (t)) is called player Pi ’s best response to q−i (t). In case of a nonunique best response, player Pi makes a random selection from BRi (q−i (t)).
It is known that the empirical frequencies generated by FP converge to a Nash
equilibrium in potential games [MS96b].
Note that FP as described above requires each player to observe the actions made
by every other individual player. Moreover, choosing an action based on the predictions (3.1) amounts to enumerating all possible joint actions in ×j Aj at every stage for
each player. Hence, FP is computationally prohibitive as a decision making model in
large-scale games.

3.2.2

Setup: Joint Strategy Fictitious Play

In JSFP, each player tracks the empirical frequencies of the joint actions of all other
players. In contrast to FP, the action of player Pi at time t is based on the (still incorrect) presumption that other players are playing randomly but jointly according to
their joint empirical frequencies, i.e., each player views all other players as a collective
group.
Let z a (t) be the percentage of stages at which all players chose the joint action

28

profile a ∈ A up to time t − 1, i.e.,
t−1

z ā (t) :=

1X
I{a(τ ) = ā}.
t τ =0

(3.2)

Let z(t) denote the empirical frequency vector formed by the components {z ā (t)}ā∈A .
Note that the dimension of z(t) is the cardinality |A|.
a

Similarly, let z−i−i (t) be the percentage of stages at which players other then player
Pi have chosen the joint action profile a−i ∈ A−i up to time t − 1, i.e.,
t−1

ā

z−i−i (t) :=

1X
I{a−i (τ ) = ā−i },
t τ =0

(3.3)

which, given z(t), can also be expressed as
ā

z−i−i (t) =

X

z (ai ,ā−i ) (t).

ai ∈Ai

Let z−i (t) denote the empirical frequency vector formed by the components
ā

{z−i−i (t)}ā−i ∈A−i . Note that the dimension of z−i (t) is the cardinality |×i6=j Aj |.
Similarly to FP, player Pi ’s action at time t is based on an expected utility for the
action āi ∈ Ai , but now based on the joint action model of opponents given by1
Ui (āi , z−i (t)) :=

X

a

Ui (āi , a−i )z−i−i (t).

(3.4)

a−i ∈A−i

In the JSFP process, player Pi uses this expected utility by selecting an action at time
t from the set
BRi (z−i (t)) := {ãi ∈ Ai : Ui (ãi , z−i (t)) = max Ui (ai , z−i (t))}.
ai ∈Ai

Note that the utility as expressed in (3.4) is linear in z−i (t).
When written in this form, JSFP appears to have a computational burden for each
player that is even higher than that of FP, since tracking the empirical frequencies
1

Note that we use the same notation for the related quantities U (ai , a−i ), U (ai , q−i ), and U (ai , z−i ),
where the latter two are derived from the first as defined in equations (3.1) and (3.4), respectively.

29

z−i (t) ∈ ∆(A−i ) of the joint actions of the other players is more demanding for player
Pi than tracking the empirical frequencies q−i (t) ∈ ×j6=i ∆(Aj ) of the actions of the
other players individually, where ∆(A) denotes the set of probability distributions
on a finite set A. However, it is possible to rewrite JSFP to significantly reduce the
computational burden on each player.
To choose an action at any time, t, player Pi using JSFP needs only the predicted
utilities Ui (āi , z−i (t)) for each āi ∈ Ai . Substituting (3.3) into (3.4) results in
t−1

Ui (āi , z−i (t)) =

1X
Ui (āi , a−i (τ )),
t τ =0

which is the average utility player Pi would have received if action āi had been chosen
at every stage up to time t − 1 and other players used the same actions. This average
utility, denoted by Viāi (t), admits the following simple recursion,
Viāi (t + 1) =

t
1
Viāi (t) +
Ui (āi , a−i (t)).
t+1
t+1

The important implication is that JSFP dynamics can be implemented without requiring each player to track the empirical frequencies of the joint actions of the other
players and without requiring each player to compute an expectation over the space of
the joint actions of all other players. Rather, each player using JSFP merely updates
the predicted utilities for each available action using the recursion above, and chooses
an action each stage with maximal predicted utility.
An interesting feature of JSFP is that each strict Nash equilibrium has an “absorption” property as summarized in Proposition 3.2.1.
Proposition 3.2.1. In any finite n-person game, if at any time t > 0, the joint action
a(t) generated by a JSFP process is a strict Nash equilibrium, then a(t + τ ) = a(t)
for all τ > 0.

30

Proof. For each player Pi ∈ P and for all actions ai ∈ Ai ,
Ui (ai (t), z−i (t)) ≥ Ui (ai , z−i (t)).
Since a(t) is a strict Nash equilibrium, we know that for all actions ai ∈ Ai \ai (t)
Ui (ai (t), a−i (t)) > Ui (ai , a−i (t)).
By writing z−i (t + 1) in terms of z−i (t) and a−i (t),
Ui (ai (t), z−i (t + 1)) =

t
1
Ui (ai (t), z−i (t)) +
Ui (ai (t), a−i (t)).
t+1
t+1

Therefore, ai (t) is the only best response to z−i (t + 1),
Ui (ai (t), z−i (t + 1)) > Ui (ai , z−i (t + 1)),

∀ai ∈ Ai \ai (t).

A strict Nash equilibrium need not possess this absorption property in general for
standard FP when there are more than two players.2
The convergence properties, even for potential games, of JSFP in the case of more
than two players is unresolved.3 We will establish convergence of JSFP in the case
where players use some sort of inertia, i.e., players are reluctant to switch to a better
action.
The JSFP with inertia process is defined as follows. Players choose their actions
according to the following rules:
2

To see this, consider the following 3 player identical interest game. For all Pi ∈ P, let Ai =
{a, b}. Let the utility be defined as follows: U (a, b, a) = U (b, a, a) = 1, U (a, a, a) = U (b, b, a) =
0, U (a, a, b) = U (b, b, b) = 1, U (a, b, b) = −1, U (b, a, b) = −100. Suppose the first action played
is a(1) = {a, a, a}. In the FP process each player will seek to deviate in the ensuing stage, a(2) =
{b, b, b}. The joint action {b, b, b} is a strict Nash equilibrium. One can easily verify that the ensuing
action in a FP process will be a(3) = {a, b, a}. Therefore, a strict Nash equilibrium is not absorbing in
the FP process with more than 2 players.
3
For two player games, JSFP and standard FP are equivalent, hence the convergence results for FP
hold for JSFP.

31

JSFP–1: If the action ai (t − 1) chosen by player Pi at time t − 1 belongs to
BRi (z−i (t)), then ai (t) = ai (t − 1).
JSFP–2: Otherwise, player Pi chooses an action, ai (t), at time t according to
the probability distribution
αi (t)βi (t) + (1 − αi (t))vai (t−1) ,
where αi (t) is a parameter representing player Pi ’s willingness to optimize at
time t, βi (t) ∈ ∆(Ai ) is any probability distribution whose support is contained
in the set BRi (z−i (t)), and vai (t−1) is the probability distribution with full support on the action ai (t − 1), i.e.,
 
0
.
 .. 
 
 
0
 
 
ai (t−1)

v
=
1
 
0
 
.
.
.
 
0
where the “1” occurs in the coordinate of ∆(Ai ) associated with ai (t − 1).
According to these rules, player Pi will stay with the previous action ai (t − 1)
with probability 1 − αi (t) even when there is a perceived opportunity for utility improvement. We make the following standing assumption on the players’ willingness to
optimize.
Assumption 3.2.1. There exist constants ε and ε̄ such that for all time t ≥ 0 and for
all players Pi ∈ P,
0 < ε < αi (t) < ε̄ < 1.

32

This assumption implies that players are always willing to optimize with some
nonzero inertia4 .
The following result shows a similar absorption property of pure Nash equilibria
in a JSFP with inertia process.
Proposition 3.2.2. In any finite n-person game, if at any time t > 0 the joint action
a(t) generated by a JSFP with inertia process is 1) a pure Nash equilibrium and 2) the
action ai (t) ∈ BRi (z−i (t)) for all players Pi ∈ P, then a(t + τ ) = a(t) for all τ > 0.
Proof. For each player Pi ∈ P and for all actions ai ∈ Ai ,
Ui (ai (t), z−i (t)) ≥ Ui (ai , z−i (t)).
Since a(t) is a pure Nash equilibrium, we know that for all actions ai ∈ Ai
Ui (ai (t), a−i (t)) ≥ Ui (ai , a−i (t)).
By writing z−i (t + 1) in terms of z−i (t) and a−i (t),
Ui (ai (t), z−i (t + 1)) =

t
1
Ui (ai (t), z−i (t)) +
Ui (ai (t), a−i (t)).
t+1
t+1

Therefore, ai (t) is also a best response to z−i (t + 1),
Ui (ai (t), z−i (t + 1)) ≥ Ui (ai , z−i (t + 1)),

∀ai ∈ Ai .

Since ai (t) ∈ BRi (z−i (t + 1)) for all players, then a(t + 1) = a(t).

3.2.3

Convergence to Nash Equilibrium

The following establishes the main result regarding the convergence of JSFP with inertia.
We will assume that no player is indifferent between distinct strategies5 .
4
5

This assumption can be relaxed to holding for sufficiently large t, as opposed to all t.
One could alternatively assume that all pure equilibria are strict.

33

Assumption 3.2.2. Player utilities satisfy
Ui (a1i , a−i ) 6= Ui (a2i , a−i ), ∀ a1i , a2i ∈ Ai , a1i 6= a2i , ∀ a−i ∈ A−i , ∀ i ∈ {1, ..., n}.
(3.5)
Theorem 3.2.1. In any finite generalized ordinal potential game in which no player
is indifferent between distinct strategies as in Assumption 3.2.2, the action profiles
a(t) generated by JSFP with inertia under Assumption 3.2.1 converge to a pure Nash
equilibrium almost surely.
We provide a complete proof of Theorem 3.2.1 in the Appendix of this chapter. We
encourage the reader to first review the proof of fading memory JSFP with inertia in
Theorem 3.3.1 of the following section.

3.3

Fading Memory JSFP with Inertia

We now analyze the case where players view recent information as more important.
In fading memory JSFP with inertia, players replace true empirical frequencies with
weighted empirical frequencies defined by the recursion
ā

z̃−i−i (0) := I{a−i (0) = ā−i },
ā

ā

z̃−i−i (t) := (1 − ρ)z̃−i−i (t − 1) + ρI{a−i (t − 1) = ā−i }, ∀t ≥ 1,
where 0 < ρ ≤ 1 is a parameter with (1−ρ) being the discount factor. Let z̃−i (t) denote
ā

the weighted empirical frequency vector formed by the components {z̃−i−i (t)}ā−i ∈A−i .
Note that the dimension of z̃−i (t) is the cardinality |A−i |.
One can identify the limiting cases of the discount factor. When ρ = 1 we have
“Cournot” beliefs, where only the most recent information matters. In the case when
ρ is not a constant, but rather ρ(t) = 1/(t + 1), all past information is given equal
importance as analyzed in Section 3.2.

34

Utility prediction and action selection with fading memory are done in the same
way as in Section 3.2, and in particular, in accordance with rules JSFP-1 and JSFP-2.
To make a decision, player Pi needs only the weighted average utility that would have
been received for each action, which is defined for action āi ∈ Ai as
X

Ṽiāi (t) := Ui (āi , z̃−i (t)) =

a

Ui (āi , a−i )z̃−i−i (t).

a−i ∈A−i

One can easily verify that the weighted average utility Ṽiāi (t) for action āi ∈ Ai admits
the recursion
Ṽiāi (t) = ρUi (āi , a−i (t − 1)) + (1 − ρ)Ṽiāi (t − 1).
Once again, player Pi is not required to track the weighted empirical frequency vector
z̃−i (t) or required to compute expectations over A−i .
As before, pure Nash equilibria have an absorption property under fading memory
JSFP with inertia.
Proposition 3.3.1. In any finite n-person game, if at any time t > 0 the joint action
a(t) generated by a fading memory JSFP with inertia process is 1) a pure Nash equilibrium and 2) the action ai (t) ∈ BRi (z̃−i (t)) for all players Pi ∈ P, then a(t+ t̃) = a(t)
for all t̃ > 0.
Proof. For each player Pi ∈ P and for all actions ai ∈ Ai ,
Ui (ai (t), z̃−i (t)) ≥ Ui (ai , z̃−i (t)).
Since a(t) is a pure Nash equilibrium, we know that for all actions ai ∈ Ai
Ui (ai (t), a−i (t)) ≥ Ui (ai , a−i (t)).
By writing z̃−i (t + 1) in terms of z̃−i (t) and a−i (t),
Ui (ai (t), z̃−i (t + 1)) = (1 − ρ)Ui (ai (t), z̃−i (t)) + ρUi (ai (t), a−i (t)).

35

Therefore, ai (t) is also a best response to z̃−i (t + 1),
Ui (ai (t), z̃−i (t + 1)) ≥ Ui (ai , z̃−i (t + 1)),

∀ai ∈ Ai .

Since ai (t) ∈ BRi (z̃−i (t + 1)) for all players, then a(t + 1) = a(t).
The following theorem establishes convergence to Nash equilibrium for fading
memory JSFP with inertia.
Theorem 3.3.1. In any finite generalized ordinal potential game in which no player is
indifferent between distinct strategies as in Assumption 3.2.2, the action profiles a(t)
generated by a fading memory JSFP with inertia process satisfying Assumption 3.2.1
converge to a pure Nash equilibrium almost surely.
Proof. The proof follows a similar structure to the proof of Theorem 6.2 in [You05].
At time t, let a0 := a(t). There exists a positive constant T , independent of t, such
that if the current action a0 is repeated T consecutive stages, i.e. a(t) = ... = a(t +
T − 1) = a0 , then BRi (z̃−i (t + T )) = BRi (a0−i ) 6 for all players. The probability
of such an event is at least (1 − ε)n(T −1) , where n is the number of players. If the
joint action a0 is an equilibrium, then by Proposition 3.3.1 we are done. Otherwise,
there must be at least one player Pi(1) ∈ P such that a0i(1) 6∈ BRi(1) (a0−i(1) ) and hence
a0i(1) 6∈ BRi(1) (z̃−i(1) (t + T )).
Consider now the event that, at time t + T , exactly one player switches to a different action, i.e., a1 := a(t + T ) = (a∗i(1) , a0−i(1) ) for some player Pi(1) ∈ P where
Ui(1) (a1 ) > Ui(1) (a0 ). This event happens with probability at least ε(1 − ε)n−1 . Note
that if φ(·) is a generalized ordinal potential function for the game, then φ(a0 ) < φ(a1 ).
Continuing along the same lines, if the current action a1 is repeated T consecutive
stages, i.e. a(t + T ) = ... = a(t + 2T − 1) = a1 , then BRi (z̃−i (t + 2T )) = BRi (a1−i )
6

Since no player is indifferent between distinct strategies, the best response to the current action
profile, BRi (a0−i ), is a singleton.

36

for all players. The probability of such an event is at least (1 − ε)n(T −1) . If the joint
action a1 is an equilibrium, then by Proposition 3.3.1, we are done. Otherwise, there
must be at least one player Pi(2) ∈ P such that a1i(2) 6∈ BRi(2) (a1−i(2) ) and hence
a1i(2) 6∈ BRi(2) (z̃−i(2) (t + 2T )).
One can repeat the arguments above to construct a sequence of profiles
a0 , a1 , a2 , ..., am , where ak = (a∗i(k) , ak−1
−i(k) ) for all k ≥ 1, with the property that
φ(a0 ) < φ(a1 ) < ... < φ(am ),
and am is an equilibrium. This means that given {z̃−i (t)}ni=1 , there exist constants
T̃ = (|A| + 1)T > 0,
|A|
|A|+1
ε̃ = ε(1 − ε)n−1
(1 − ε)n(T −1)
> 0,
both of which are independent of t, such that the following event happens with probability at least ε̃: a(t + T̃ ) is an equilibrium and ai (t + T̃ ) ∈ BRi (z̃−i (t + T̃ )) for
all players Pi ∈ P. This implies that a(t) converges to a pure equilibrium almost
surely.

3.4

Congestion Games and Distributed Traffic Routing

In this section, we illustrate the main results on congestion games, as defined in Section 2.3.3, which are a special case of the generalized ordinal potential games addressed in Theorems 3.2.1 and 3.3.1. We illustrate these results on a simulation of
distributed traffic routing. We go on to discuss how to modify player utilities in distributed traffic routing to allow a centralized planner to achieve a desired collective
objective through distributed learning.

37

3.4.1

Distributed Traffic Routing

We consider a congestion game, as defined in Section 2.3.3, with 100 players, or
drivers, seeking to traverse from node A to node B along 10 different parallel roads
as illustrated in Figure 3.1. Each driver can select any road as a possible route. In
r

1

r

2

A

B

r

10

Figure 3.1: Fading Memory JSFP with Inertia: Congestion Game Example – Network Topology

terms of congestion games, the set of resources is the set of roads, R, and each player
can select one road, i.e., Ai = R.
Each road has a quadratic cost function with positive (randomly chosen) coefficients,
cri (k) = ai k 2 + bi k + ci , i = 1, ..., 10,
where k represent the number of vehicles on that particular road. The actual coefficients are unimportant as we are just using this example as an opportunity to illustrate
the convergence properties of the algorithm fading memory JSFP with inertia. This
cost function may represent the delay incurred by a driver as a function of the number
of other drivers sharing the same road.
We simulated a case where drivers choose their initial routes randomly, and every

38

day thereafter, adjusted their routes using fading memory JSFP with inertia. The parameters αi (t) are chosen as 0.5 for all days and all players, and the fading memory
parameter ρ is chosen as 0.03. The number of vehicles on each road fluctuates initially
and then stabilizes as illustrated in Figure 3.2. Figure 3.3 illustrates the evolution of the
congestion cost on each road. One can observe that the congestion cost on each road
converges approximately to the same value, which is consistent with a Nash equilibrium with large number of drivers. This behavior resembles an approximate “Wardrop
equilibrium” [War52], which represents a steady-state situation in which the congestion cost on each road is equal due to the fact that, as the number of drivers increases,
the effect of an individual driver on the traffic conditions becomes negligible.

Number of Vehicles on Each Route

20

15

10

5

0

20

40

60

80

100
120
Day Number

140

160

180

200

Figure 3.2: Fading Memory JSFP with Inertia: Evolution of Number of Vehicles on Each
Route

Note that FP could not be implemented even on this very simple congestion game.
A driver using FP would need to track the empirical frequencies of the choices of the
99 other drivers and compute an expected utility evaluated over a probability space of

39

4

3.5

Congestion Cost on Each Route

3

2.5

2

1.5

1

0.5

0

0

20

40

60

80

100
120
Day Number

140

160

180

200

Figure 3.3: Fading Memory JSFP with Inertia: Evolution of Congestion Cost on Each Route

dimension 1099 .
It turns out that JSFP, fading memory JSFP, or other virtual payoff based learning
algorithms are strongly connected to actual driver behavioral models. Consider the
driver adjustment process considered in [BPK91] which is illustrated in Figure 3.4.
The adjustment process highlighted is precisely JSFP with Inertia.

3.4.2

Incorporating Tolls to Minimize the Total Congestion

It is well known that a Nash equilibrium may not minimize the total congestion experienced by all drivers [Rou03]. In this section, we show how a global planner can
minimize the total congestion by implementing tolls on the network. The results are
applicable to general congestion games, but we present the approach in the language
of distributed traffic routing.

40

Figure 3.4: Example of a Driver Adjustment Process

The total congestion experienced by all drivers on the network is
Tc (a) :=

X

σr (a)cr (σr (a)).

r∈R

Define a new congestion game where each driver’s utility takes the form
Ui (a) = −

X


cr (σr (a)) + tr (σr (a)) ,

r∈ai

where tr (·) is the toll imposed on road r which is a function of the number of users of
road r.
The following proposition, which is a special case of Proposition 5.3.1, outlines
how to incorporate tolls so that the minimum congestion solution is a Nash equilibrium. The approach is similar to the taxation approaches for nonatomic congestion
games proposed in [Mil04, San02].

41

Proposition 3.4.1. Consider a congestion game of any network topology. If the imposed tolls are set as
tr (k) = (k − 1)[cr (k) − cr (k − 1)], ∀k ≥ 1,
then the total negative congestion experienced by all drivers, φc (a) := −Tc (a), is a
potential function for the congestion game with tolls.
By implementing the tolling scheme set forth in Proposition 3.4.1, we guarantee
that all action profiles that minimize the total congestion experienced on the network
are equilibria of the congestion game with tolls. However, there may be addition equilibria at which an inefficient operating condition can still occur. The following proposition establishes the uniqueness of a strict Nash equilibrium for congestion games of
parallel network topologies such as the one considered in this example.
Proposition 3.4.2. Consider a congestion game with nondecreasing congestion functions where each driver is allowed to select any one road, i.e. Ai = R for all drivers.
If the congestion game has at least one strict equilibrium, then all equilibria have the
same aggregate vehicle distribution over the network. Furthermore, all equilibria are
strict.
Proof. Suppose action profiles a1 and a2 are equilibria with a1 being a strict equi1

librium. We will use the shorthand notation σra to represent σr (a1 ). Let σ(a1 ) :=
1

1

2

2

(σra1 , ..., σran ) and σ(a2 ) := (σra1 , ..., σran ) be the aggregate vehicle distribution over the
network for equilibrium a1 and a2 . If σ(a1 ) 6= σ(a2 ), there exists a road a such that
1

2

1

2

σaa > σaa and a road b such that σba < σba . Therefore, we know that
1

2

2

1

ca (σaa ) ≥ ca (σaa + 1),
cb (σba ) ≥ cb (σba + 1).

42

Since a1 and a2 are equilibrium with a1 being strict,
1

1

2

2

ca (σaa ) < cri (σrai + 1), ∀ri ∈ R,
cb (σba ) ≤ cri (σrai + 1), ∀ri ∈ R.
Using the above inequalities, we can show that
1

2

2

1

1

ca (σaa ) ≥ ca (σaa + 1) ≥ cb (σba ) ≥ cb (σba + 1) > ca (σaa ),
which gives us a contradiction. Therefore σ(a1 ) = σ(a2 ). Since a1 is a strict equilibrium, then a2 must be a strict equilibrium as well.
When the tolling scheme set forth in Proposition 3.4.1 is applied to the congestion
game example considered previously, the resulting congestion game with tolls is a potential game in which no player is indifferent between distinct strategies. Proposition
3.4.1 guarantees us that the action profiles that minimize the total congestion experienced by all drivers on the network are in fact strict equilibria of the congestion game
with tolls. Furthermore, if the new congestion functions are nondecreasing7 , then by
Proposition 3.4.2, all strict equilibria must have the same aggregate vehicle distribution over the network, and therefore must minimize the total congestion experienced
by all drivers on the network. Therefore, the action profiles generated by fading memory JSFP with inertia converge to an equilibrium that minimizes the total congestion
experienced by all users, as shown in Figure 3.5.

3.5

Concluding Remarks and Future Work

We have analyzed the long-term behavior of a large number of players in large-scale
games where players are limited in both their observational and computational capabilities. In particular, we analyzed a version of JSFP and showed that it accommodates
7

Simple conditions on the original congestion functions can be established to guarantee that the new
congestion functions, i.e congestion plus tolls, are nondecreasing.

43

160

Total Congestion Experienced by all Drivers

150

140
Congestion Game without Tolls
Congestion Game With Tolls

130

120

110

100

90

0

20

40

60

80

100
120
Day Number

140

160

180

200

Figure 3.5: Fading Memory JSFP with Inertia: Evolution of Total Congestion Experienced by
All Drivers with and without Tolls.

inherent player limitations in information gathering and processing. Furthermore, we
showed that JSFP has guaranteed convergence to a pure Nash equilibrium in all generalized ordinal potential games, which includes but is not limited to all congestion
games, when players use some inertia either with or without exponential discounting
of the historical data. The methods were illustrated on a transportation congestion
game, in which a large number of vehicles make daily routing decisions to optimize
their own objectives in response to the aggregate congestion on each road of interest.
An interesting continuation of this research would be the case where players observe
only the actual utilities they receive. This situation will be the focus of Chapter 5.
The method of proof of Theorems 3.2.1 and 3.3.1 relies on inertia to derive a positive probability of a single player seeking to make an utility improvement, thereby
increasing the potential function. This suggests a convergence rate that is exponential
in the game size, i.e., number of players and actions. It should be noted that inertia

44

is simply a proof device that assures convergence for generic potential games. The
proof provides just one out of multiple paths to convergence. The simulations reflect
that convergence can be much faster. Indeed, simulations suggest that convergence
is possible even in the absence of inertia but not necessarily for all potential games.
Furthermore, recent work [HM06] suggests that convergence rates of a broad class
of distributed learning processes can be exponential in the game size as well, and so
this seems to be a limitation in the framework of distributed learning rather than any
specific learning process (as opposed to centralized algorithms for computing an equilibrium).

3.6

Appendix to Chapter 3

3.6.1

Proof of Theorem 3.2.1

This section is devoted to the proof of Theorem 3.2.1. It will be helpful to note the
following simple observations:
1. The expression for Ui (āi , z−i (t)) in equation (3.4) is linear in z−i (t).
2. If an action profile, a0 ∈ A, is repeated over the interval [t, t + N − 1], i.e.,
a(t) = a(t + 1) = ... = a(t + N − 1) = a0 ,
then z(t + N ) can be written as
z(t + N ) =

t
N
0
z(t) +
va ,
t+N
t+N

and likewise z−i (t + N ) can be written as
z−i (t + N ) =

N
t
0
z−i (t) +
va−i .
t+N
t+N

45

We begin by defining the quantities δi (t), Mu , mu , and γ as follows. Assume that
player Pi played a best response at least one time in the period [0, t], where t ∈ [0, ∞).
Define
δi (t) := min{0 ≤ τ ≤ t : ai (t − τ ) ∈ BRi (zi (t − τ ))}.
In other words, t − δi (t) is the last time in the period [0, t] at which player Pi played
a best response. If player Pi never played a best response in the period [0, t], then we
adopt the convention δi (t) = ∞. Note that
ai (t − τ ) = ai (t), ∀τ ∈ {0, 1, ..., min{δi (t), t}}.
Now define
Mu := max{|Ui (a1 ) − Ui (a2 )| : a1 , a2 ∈ A, Pi ∈ P},
mu := min{|Ui (a1 ) − Ui (a2 )| : |Ui (a1 ) − Ui (a2 )| > 0, a1 , a2 ∈ A, Pi ∈ P},
γ := dMu /mu e,
where d·e denotes integer ceiling.
The proof of fading memory JSFP with inertia relied on a notion of memory dominance. This means that if the current action profile is repeated a sufficient number of
times (finite and independent of time) then a best response to the weighted empirical
frequencies is equivalent to a best response to the current action profile and hence will
increase the potential provided that there is only a unique deviator. This will always
happen with at least a fixed (time independent) probability because of the players’
inertia.
In the non-discounted case the memory dominance approach will not work for the
reason that the probability of dominating the memory because of the players’ inertia
diminishes with time. However, the following claims show that one does not need to
dominate the entire memory, but rather just the portion of time for which the player

46

was playing a suboptimal action. By dominating this portion of the memory, one can
guarantee that a unilateral best response to the empirical frequencies will increase the
potential. This is the fundamental idea in the proof of Theorem 3.2.1.
Claim 3.6.1. Consider a player Pi with δi (t) < ∞. Let t1 be any finite integer satisfying
t1 ≥ γδi (t).
If an action profile, a0 ∈ A, is repeated over the interval [t, t + t1 ], i.e.,
a(t) = a(t + 1) = · · · = a(t + t1 ) = a0 ,
then
âi ∈ BRi (z−i (t + t1 + 1)) ⇒ Ui (âi , a0−i ) ≥ Ui (a0i , a0−i ),
i.e., player Pi ’s best response at time t + t1 + 1 cannot be a worse response to a0−i than
a0i .
Proof. Since âi ∈ BRi (z−i (t + t1 + 1)),
Ui (âi , z−i (t + t1 + 1)) − Ui (a0i , z−i (t + t1 + 1)) ≥ 0.
Expressing z−i (t + t1 + 1) as a summation over the intervals [0, t − δi (t) − 1], [t −
δi (t), t − 1], and [t, t + t1 ] and using the definition (3.4) leads to


(t1 + 1) Ui (âi , a0−i ) − Ui (a0i , a0−i )
+

t−1
X



Ui (âi , a−i (τ )) − Ui (a0i , a−i (τ ))

τ =t−δi (t)



+(t − δi (t)) Ui (âi , z−i (t − δi (t))) − Ui (a0i , z−i (t − δi (t))) ≥ 0.
Now, since
ai (t − δi (t)) = ai (t − δi (t) + 1) = · · · = ai (t) = a0i ∈ BRi (z−i (t − δi (t))),

47

meaning that the third term above is negative, and so


(t1 + 1) Ui (âi , a0−i ) − Ui (a0i , a0−i )
t−1
X

+



Ui (âi , a−i (τ )) − Ui (a0i , a−i (τ )) ≥ 0.

τ =t−δi (t)

This implies that


Mu δi (t)
Ui (âi , a0−i ) − Ui (a0i , a0−i ) ≥ −
> −mu ,
t1 + 1
or, alternatively,


Ui (a0i , a0−i ) − Ui (âi , a0−i ) < mu .
If the quantity in brackets were positive, this would violate the definition of mu —
unless âi = a0i . In either case,
Ui (âi , a0−i ) − Ui (a0i , a0−i ) ≥ 0.

There are certain action profile/empirical frequency values where the next play is
“forced”. Define the time-dependent (forced-move) set F(t) ⊂ A × ∆(A) as
(ā, z̄) ∈ F(t)
⇔

āi ∈ BRi


1 ā−i
t
z̄−i +
v
,
t+1
t+1

∀i ∈ {1, ..., n} .

So the condition (a(t), z(t)) ∈ F(t), implies that for all i, “today’s” action necessarily
lies in “tomorrow’s” best response, i.e.,
ai (t) ∈ BRi (z−i (t + 1)).
By the rule JSFP-1, the next play ai (t + 1) = ai (t) is forced for all i ∈ {1, ..., N }.

48

Now define
π(t; a(t), z(t)) := min {τ ≥ 0 : (a(t + τ ), z(t + τ )) 6∈ F(t + τ )} .

(3.6)

If this is never satisfied, then set π(t; a(t), z(t)) = ∞.
For the sake of notational simplicity, we will drop the explicit dependence on a(t)
and z(t) and simply write π(t) instead of π(t; a(t), z(t)).
A consequence of the definition of π(t) is that for a given a(t) and z(t), 1) a(t)
must be repeated over the interval [t, t + π(t)]. Furthermore, at time t + π(t) + 1, at
least one player can improve (over yet another repeated play of a(t)) by playing a best
response at time t + π(t) + 1. Furthermore, the probability that exactly one player will
switch to a best response action at time t + π(t) + 1 is at least ε(1 − ε)n−1 .
The following claim shows that this improvement opportunity remains even if a(t)
is repeated for longer than π(t) (because of inertia).
Claim 3.6.2. Let a(t) and z(t) be such that π(t) < ∞. Let t1 be any integer satisfying
π(t) ≤ t1 < ∞. If
a(t) = a(t + 1) = · · · = a(t + π(t)) = · · · = a(t + t1 ),
then
ai (t) 6∈ BRi (z−i (t + t1 + 1)), for some i ∈ {1, ..., n}.
Proof. Let i ∈ {1, ..., n} be such that
ai (t) 6∈ BRi (z−i (t + π(t) + 1))
and
ai (t) ∈ BRi (z−i (t + π(t))).

49

The existence of such an i is assured by the definition of π(t). Pick âi ∈ BRi (z−i (t +
π(t) + 1)). We have
Ui (âi , z−i (t + π(t) + 1)) − Ui (ai (t), z−i (t + π(t) + 1))
= [Ui (âi , z−i (t + π(t))) − Ui (ai (t), z−i (t + π(t)))]
+ [Ui (âi , a−i (t)) − Ui (ai (t), a−i (t))]

t + π(t)
t + π(t) + 1

1
> 0.
t + π(t) + 1

Since ai (t) ∈ BRi (z−i (t + π(t))), we must have
Ui (âi , a−i (t)) − Ui (ai (t), a−i (t)) > 0.
This implies
Ui (âi , z−i (t + t1 + 1)) − Ui (ai (t), z−i (t + t1 + 1))
= [Ui (âi , z−i (t + π(t) + 1)) − Ui (ai (t), z−i (t + π(t) + 1))]
+ [Ui (âi , a−i (t)) − Ui (ai (t), a−i (t))]

t + π(t) + 1
t + t1 + 1

t1 − π(t)
> 0.
t + t1 + 1

Claim 3.6.3. If, at any time, a(t) is not an equilibrium, then π(t) ≤ γt.
Proof. Let a0 := a(t). Since a0 is not an equilibrium,
a0i 6∈ BRi (a0−i ), for some i ∈ {1, ..., n}.
Pick âi ∈ BRi (a0−i ) so that Ui (âi , a0−i ) − Ui (a0i , a0−i ) > mu . If
a(t) = a(t + 1) = · · · = a(t + γt) = a0 ,
then
Ui (âi , z−i (t + γt + 1)) − Ui (a0i , z−i (t + γt + 1))
t[Ui (âi , z−i (t)) − Ui (a0i , z−i (t))] + (γt + 1)[Ui (âi , a0−i ) − Ui (a0i , a0−i )]
=
t + γt + 1
−tMu + (γt + 1)mu
≥
t + γt + 1
> 0.

50

Claim 3.6.4. Consider a finite generalized ordinal potential game with a potential
function φ(·) with player utilities satisfying Assumption 3.2.2. For any time t ≥ 0,
suppose that
1. a(t) is not an equilibrium; and
2. max1≤i≤n δi (t) ≤ δ̄ for some δ̄ ≤ t.
Define

ψ(t) := 1 + max π(t), γ δ̄ .
Then ψ(t) ≤ 1 + γt and
Pr [φ(a(t + ψ(t))) > φ(a(t)) | a(t), z(t)] ≥ ε(1 − ε)n(1+γ δ̄)−1 ,
and
max δi (t + ψ(t)) ≤ 1 + (1 + γ)δ̄.

1≤i≤n

Proof. Since a(t) is not an equilibrium, Claim 3.6.3 implies that π(t) ≤ γt, which in
turn implies the above upper bound on ψ(t).
First consider the case where π(t) ≥ γ δ̄, i.e., ψ(t) = 1 + π(t). According to the
definition of π(t) in equation (3.6), a(t) must be repeated as a best response in the
period [t, t + π(t)]. Furthermore, we must have
max δi (t + ψ(t)) ≤ 1

1≤i≤n

and ai (t) 6∈ BRi (z−i (t + ψ(t))) for at least one player Pi . The probability that exactly
one such player Pi will switch to a choice different than ai (t) at time t + ψ(t) is at
least ε(1 − ε)n−1 . But, by Claim 3.6.1 and no-indifference Assumption 3.2.2, such an
event would cause
Ui (a(t + π(t) + 1)) > Ui (a(t)) ⇒ φ(a(t + π(t) + 1)) > φ(a(t)).

51

Now consider the case where π(t) < γ δ̄, i.e., ψ(t) = 1 + γ δ̄. In this case,
max δi (t + ψ(t)) ≤ 1 + γ δ̄ + δ̄.

1≤i≤n

Moreover, the event
a(t) = · · · = a(t + γ δ̄)
will occur with probability at least8 (1 − ε)nγ δ̄ . Conditioned on this event, Claim 3.6.2
provides that exactly one player Pi will switch to a choice different than ai (t) at time
t + ψ(t) with probability at least ε(1 − ε)n−1 . By Claim 3.6.1 and no-indifference
Assumption 3.5, this would cause
Ui (a(t + ψ(t))) > Ui (a(t)) ⇒ φ(a(t + ψ(t))) > φ(a(t)).

Proof of Theorem 3.2.1
It suffices to show that there exists a non-zero probability, ε∗ > 0, such that the following statement holds. For any t ≥ 0, a(t) ∈ A, and z(t) ∈ ∆(A), there exists a finite
time t∗ ≥ t such that, for some equilibrium a∗ ,
Pr [a(τ ) = a∗ , ∀τ ≥ t∗ | a(t), {z−i (t)}ni=1 ] ≥ ε∗ .

(3.7)

In other words, the probability of convergence to an equilibrium by time t∗ is at least
ε∗ . Since ε∗ does not depend on t, a(t), or z(t), this will imply that the action profile
converges to an equilibrium almost surely.
We will construct a series of events that can occur with positive probability to
establish the bound in equation (3.7).
8

In fact, a tighter bound can be derived by exploiting the forced moves for a duration of π(t).

52

Let t0 = t + 1. All players will play a best response at time t0 with probability at
least εn . Therefore, we have


n
Pr max δi (t0 ) = 0 | a(t), {z−i (t)}i=1 ≥ εn .
1≤i≤n

(3.8)

Assume that a(t0 ) is not an equilibrium. Otherwise, according to Proposition 3.2.2,
a(τ ) = a(t0 ) for all τ ≥ t0 .
From Claim 3.6.4, define t1 and δ1 as
δ1 := 1 + (1 + γ)δ0 ,
t1 := t0 + 1 + max{π(t0 ), γδ0 },
≤ t0 + 1 + γt0 = 1 + (1 + γ)t0 ,
where δ0 := 0. By Claim 3.6.4,
Pr [φ(a(t1 )) > φ(a(t0 )) | a(t0 ), {z−i (t0 )}ni=1 ] ≥ ε(1 − ε)n(1+γδ0 )−1
and
max δi (t1 ) ≤ δ1 .

1≤i≤n

Similarly, for k > 0 we can recursively define
δk := 1 + (1 + γ)δk−1 ,
k−1
X
k
= (1 + γ) δ0 +
(1 + γ)j ,
j=0

=

k−1
X

(1 + γ)j ,

j=0

and
tk := tk−1 + 1 + max{π(tk−1 ), γδk−1 },
≤ 1 + (1 + γ)tk−1
k−1
X
k
≤ (1 + γ) t0 +
(1 + γ)j ,
j=0

53

where
Pr [φ(a(tk )) > φ(a(tk−1 )) | a(tk−1 ), {z−i (tk−1 )}ni=1 ] ≥ ε(1 − ε)n(1+γδk−1 )−1
and
max δi (tk ) ≤ δk ,

1≤i≤n

as long as a(tk−1 ) is not an equilibrium.
Therefore, one can construct a sequence of profiles a(t0 ), a(t1 ), ..., a(tk ) with the
property that φ(a(t0 )) < φ(a(t1 )) < ... < φ(a(tk )). Since in a finite generalized
ordinal potential game, φ(a(tk )) cannot increase indefinitely as k increases, we must
have
|A|−1

Y

Pr [a(tk ) is an equilibrium for some tk ∈ [t, ∞) | a(t), {z−i (t)}ni=1 ] ≥ εn

ε(1 − ε)n(1+γδk )−1 ,

k=0

where εn comes from (3.8). Finally, from Claim 3.6.1 and Assumption 3.2.2, the
above inequality together with
Pr [a(tk ) = · · · = a(tk + γδk ) | a(tk ), {z−i (tk )}ni=1 ] ≥ (1 − ε)nγδk ≥ (1 − ε)nγδ|A|
implies that for some equilibrium, a∗ ,
Pr [a(τ ) = a∗ , ∀τ ≥ t∗ | a(t), {z−i (t)}ni=1 ] ≥ ε∗ ,
where
∗

t

|A|

= t|A| + γδ|A| + 1 = (1 + γ)

t0 +

|A|
X

(1 + γ)j ,

j=0

ε

∗

|A|−1


=

ε

n

Y

n(1+γδk )−1



ε(1 − ε)

k=0

Since ε∗ does not depend on t this concludes the proof.

54

nγδ|A|

(1 − ε)


.

CHAPTER 4
Regret Based Dynamics for Weakly Acyclic Games
No-regret algorithms have been proposed to control a wide variety of multi-agent systems. The appeal of no-regret algorithms is that they are easily implementable in large
scale multi-agent systems because players make decisions using only retrospective or
“regret based” information. Furthermore, there are existing results proving that the collective behavior will asymptotically converge to a set of points of “no-regret” in any
game. We illustrate, through a simple example, that no-regret points need not reflect
desirable operating conditions for a multi-agent system. Multi-agent systems often exhibit an additional structure (i.e. being “weakly acyclic”) that has not been exploited
in the context of no-regret algorithms. In this chapter, we introduce a modification of
the traditional no-regret algorithms by (i) exponentially discounting the memory and
(ii) bringing in a notion of inertia in players’ decision process. We show how these
modifications can lead to an entire class of regret based algorithms that provide almost
sure convergence to a pure Nash equilibrium in any weakly acyclic game.

4.1

Introduction

The applicability of regret based algorithms for multi-agent learning has been studied in several papers [Gor05, Bow04, KV05, BP05, GJ03, AMS07]. The appeal of
regret based algorithms is two fold. First of all, regret based algorithms are easily
implementable in large scale multi-agent systems when compared with other learning

55

algorithms such as fictitious play [MS96a, JGD01]. Secondly, there is a wide range of
algorithms, called “no-regret” algorithms, that guarantee that the collective behavior
will asymptotically converge to a set of points of no-regret (also referred to as coarse
correlated equilibrium) in any game [You05]. A point of no-regret characterizes a situation for which the average utility that a player actually received is as high as the
average utility that the player “would have” received had that player used a different
fixed strategy at all previous time steps. No-regret algorithms have been proposed in
a variety of settings ranging from network routing problems [BEL06] to structured
prediction problems [Gor05].
In the more general regret based algorithms, each player makes a decision using
only information regarding the regret for each of his possible actions. If an algorithm
guarantees that a player’s maximum regret asymptotically approaches zero then the algorithm is referred to as a no-regret algorithm. The most common no-regret algorithm
is regret matching [HM00]. In regret matching, at each time step, each player plays a
strategy where the probability of playing an action is proportional to the positive part
of his regret for that action. In a multi-agent system, if all players adhere to a no-regret
learning algorithm, such as regret matching, then the group behavior will converge
asymptotically to a set of points of no-regret [HM00]. Traditionally, a point of noregret has been viewed as a desirable or efficient operating condition because each
player’s average utility is as good as the average utility that any other action would
have yielded [KV05]. However, a point of no-regret says little about the performance;
hence knowing that the collective behavior of a multi-agent system will converge to a
set of points of no-regret in general does not guarantee an efficient operation.
There have been attempts to further strengthen the convergence results of no-regret
algorithms for special classes of games. For example, in [JGD01], Jafari et al. showed
through simulations that no-regret algorithms provide convergence to a Nash equilib-

56

rium in dominance solvable, constant-sum, and general sum 2 × 2 games. In [Bow04],
Bowling introduced a gradient based regret algorithm that guarantees that players’
strategies converge to a Nash equilibrium in any 2 player 2 action repeated game.
In [BEL06], Blum et al. analyzed the convergence of no-regret algorithms in routing
games and proved that behavior will approach a Nash equilibrium in various settings.
However, the classes of games considered here cannot fully model a wide variety of
multi-agent systems.
It turns out that weakly acyclic games, which generalize potential games [MS96b],
are closely related to multi-agent systems [MAS07a]. The connection can be seen by
recognizing that in any multi-agent system there is a global objective. Each player
is assigned a local utility function that is appropriately aligned with the global objective. It is precisely this alignment that connects the realms of multi-agent systems and
weakly acyclic games.
An open question is whether no-regret algorithms converge to a Nash equilibrium
in n-player weakly acyclic games. In this chapter, we introduce a modification of the
traditional no-regret algorithms that (i) exponentially discounts the memory and (ii)
brings in a notion of inertia in players’ decision process. We show how these modifications can lead to an entire class of regret based algorithms that provide almost sure
convergence to a pure Nash equilibrium in any weakly acyclic game. It is important
to note that convergence to a Nash equilibrium also implies convergence to a no-regret
point.
In Section 4.2 we discuss the no-regret algorithm, “regret matching,” and illustrate
the performance issues involved with no-regret points in a simple 3 player identical
interest game. In Section 4.3 we introduce a new class of learning dynamics referred
to as regret based dynamics with fading memory and inertia. In Section 4.4 we present
some simulation results. Section 4.5 presents some concluding remarks.

57

4.2

Regret Matching

We consider a repeated matrix game with n-player set P := {P1 , ..., Pn }, a finite
action set Ai for each player Pi ∈ P, and a utility function Ui : A → R for each
player Pi ∈ P, where A := A1 × · · · × An .
We introduce regret matching, from [HM00], in which players choose their actions
based on their regret for not choosing particular actions in the past steps.
Define the average regret of player Pi for an action ai ∈ Ai at time t as
1
Riai (t) :=

t−1
X

t τ =0

(Ui (ai , a−i (τ )) − Ui (a(τ ))) .

(4.1)

In other words, player Pi ’s average regret for ai ∈ Ai would represent the average
improvement in his utility if he had chosen ai ∈ Ai in all past steps and all other
players’ actions had remained unaltered.
Each player Pi using regret matching computes Riai (t) for every action ai ∈ Ai
using the recursion
Riai (t) =

t − 1 ai
1
Ri (t − 1) + (Ui (ai , a−i (t)) − Ui (a(t))) .
t
t

Note that, at every step t > 0, player Pi updates all entries in his average regret


vector Ri (t) := Riai (t) ai ∈Ai . To update his average regret vector at time t, it is
sufficient for player Pi to observe (in addition to the actual utility received at time
t − 1, Ui (a(t − 1))) his hypothetical utilities Ui (ai , a−i (t − 1)), for all ai ∈ Ai , that
would have been received if he had chosen ai (instead of ai (t − 1)) and all other player
actions a−i (t − 1) had remained unchanged at step t − 1.
In regret matching, once player Pi computes his average regret vector, Ri (t), he
chooses an action ai (t), t > 0, according to the probability distribution pi (t) defined
as
[Riai (t)]+
ai
pi (t) = Pr [ai (t) = ai ] = P
 ãi + ,
ãi ∈Ai Ri (t)

58

for any ai ∈ Ai , provided that the denominator above is positive; otherwise, pi (t) is the
uniform distribution over Ai (pi (0) ∈ ∆(Ai ) is always arbitrary). Roughly speaking,
a player using regret matching chooses a particular action at any step with probability
proportional to the average regret for not choosing that particular action in the past
steps. If all players use regret matching, the empirical distribution of the joint actions
converge almost surely to the set of coarse correlated equilibria (similar results hold
for different regret based adaptive dynamics); see [HM00, HM01, HM03a]. Note that
this does not mean that the action profiles a(t) will converge, nor does it mean that the
empirical frequencies of a(t) will converge to a point in ∆(A).

4.2.1

Coarse Correlated Equilibria and No-Regret

The set of coarse correlated equilibrium has a strong connection to the notion of regret.
We will restate the definitions of the joint and marginal empirical frequencies originally defined in Section 3.2. Define the empirical frequency of the joint actions, z a (t),
as the percentage of stages at which all players chose the joint action profile a ∈ A up
to time t − 1, i.e.,
t−1

1X
z (t) :=
I{a(τ ) = a}.
t τ =0
a

Let z(t) denote the empirical frequency vector formed by the components
{z a (t)}a∈A . Note that the dimension of z(t) is the cardinality of the set A, i.e., |A|,
and z(t) ∈ ∆(A).
a

Similarly, let z−i−i (t) be the percentage of stages at which players other then player
Pi have chosen the joint action profile a−i ∈ A−i up to time t − 1, i.e.,
t−1

a

z−i−i (t) :=

1X
I{a−i (τ ) = a−i },
t τ =0

59

(4.2)

which, given z(t), can also be expressed as
X

a

z−i−i (t) =

z (ai ,a−i ) (t).

ai ∈Ai
a

Let z−i (t) denote the empirical frequency vector formed by the components {z−i−i (t)}a−i ∈A−i .
Note that the dimension of z−i (t) is the cardinality |A−i | and z−i (t) ∈ ∆(A−i ).
Given a joint distribution z(t), the expected utility of player Pi is
Ui (z(t)) =

X

Ui (a)z a (t),

a∈A
t−1

1X
=
Ui (a(τ )),
t τ =0
which is precisely the average utility that player Pi has received up to time t − 1. The
expected utility of player Pi for any action ai ∈ Ai is
Ui (ai , z−i (t)) =

X

a

Ui (ai , a−i )z−i−i (t),

a−i ∈A−i
t−1

=

1X
Ui (ai , a−i (τ )),
t τ =0

which is precisely the average utility that player Pi would have received up to time
t − 1 if player Pi had played action ai all previous time periods provided that the other
players actions remained unchanged. Therefore, the regret of player Pi for action
ai ∈ Ai at time t can be expressed as
Riai (t) = Ui (ai , z−i (t)) − Ui (z(t)).
If all players use regret matching, then we know that the empirical frequency z(t)
of the joint actions converges almost surely to the set of coarse correlated equilibria. If
z(t) is a coarse correlated equilibrium, then we know that for any player Pi ∈ P and
any action ai ∈ Ai ,
Ui (ai , z−i (t)) ≤ Ui (z(t)) ⇒ Riai (t) ≤ 0.

60

Therefore, stating that the empirical frequency of the joint actions converge to the set
of coarse correlated equilibria is equivalent to saying that a player’s average regret for
any action will asymptotically vanish.

4.2.2

Illustrative Example

In general, the set of Nash equilibria is a proper subset of the set of coarse correlated
equilibria. Consider for example the following 3−player identical interest game characterized by the player utilities shown in Figure 4.1.

L

R

U

2

-1

D

1

-2
M1

L

R

U

0

0

D

0

0
M2

L

R

U

-2

1

D

-1

2
M3

Figure 4.1: A 3−player Identical Interest Game.

Player P1 chooses a row U or D, Player P2 chooses a column L or R, Player P3
chooses a matrix M1 , or M2 , or M3 . There are two pure Nash equilibria (U, L, M1 )
and (D, R, M3 ) both of which yield maximum utility 2 to all players. The set of coarse
correlated equilibria contains these two pure Nash equilibria as the extremum points
of ∆(A) as well as many other probability distributions in ∆(A). In particular, the set
of coarse correlated equilibria contains the following


X
a
U LM2
DRM2
U RM2
DLM2
z ∈ ∆(A) :
z = 1, z
=z
, z
=z
.
a∈A:a3 =M2

Any coarse correlated equilibrium of this form yields an expected utility of 0 to all
players. Clearly, one of the two pure Nash equilibria would be more desirable to all

61

players then any other outcome including the above coarse correlated equilibria. However, the existing results at the time of writing this dissertation such as Theorem 3.1 in
[You05] only guarantee that regret matching will lead players to the set of coarse correlated equilibria and not necessarily to a pure Nash equilibrium. While this example
is simplistic in nature, one must believe that situations like this could easily arise in
more general weakly acyclic games.
We should emphasize that regret matching could indeed be convergent to a pure
Nash equilibrium in weakly acyclic games; however, to the best of authors’ knowledge,
no proof for such a statement exists. The existing results characterize the long-term
behavior of regret matching in general games as convergence to the set of coarse correlated equilibria, whereas we are interested in proving that the action profiles, a(k),
generated by regret matching will converge to a pure Nash equilibrium when player
utilities constitute a weakly acyclic game, an objective which we will pursue in the
next section.

4.3

Regret Based Dynamics with Fading Memory and Inertia

To enable convergence to a pure Nash equilibrium in weakly acyclic games, we will
modify the conventional regret based dynamics in two ways. First, we will assume
that each player has a fading memory, that is, each player exponentially discounts
the influence of its past regret in the computation of its average regret vector. More
precisely, each player computes a discounted average regret vector according to the
recursion
R̃iāi (t + 1) = (1 − ρ)R̃iāi (t) + ρ (Ui (āi , a−i (t)) − Ui (a(t))) ,
for all āi ∈ Ai , where ρ ∈ (0, 1] is a parameter with 1 − ρ being the discount factor,
and R̃iāi (1) = 0.

62

Second, we will assume that each player chooses an action based on its discounted
average regret using some inertia. Therefore, each player Pi chooses an action ai (t),
at step t > 1, according to the probability distribution
αi (t)RBi (R̃i (t)) + (1 − αi (t))vai (t−1) ,
where αi (t) is a parameter representing player Pi ’s willingness to optimize at time
t, vai (t−1) is the vertex of ∆(Ai ) corresponding to the action ai (t − 1) chosen by
player Pi at step t − 1, and RBi : R|Ai | → ∆(Ai ) is any continuous function (on
{x ∈ R|Ai | : [x]+ 6= 0}) satisfying
x` > 0 ⇔ RBi` (x) > 0
and

(4.3)

[x]+ = 0 ⇒ RBi` (x) = |A1i | , ∀`,
where x` and RBi` (x) are the `-th components of x and RBi (x) respectively.
We will call the above dynamics regret based dynamics (RB) with fading memory
and inertia. One particular choice for the function RBi is
 ` +
x
`
, (when [x]+ 6= 0)
RBi (x) = P|Ai |
+
m
m=1 [x ]

(4.4)

which leads to regret matching with fading memory and inertia. Another particular
choice is

1 `
eτ x
`
`
+
RBi (x) = P
6= 0),
1 m I{x > 0}, (when [x]
x
τ
e
m
x >0

where τ > 0 is a parameter. Note that, for small values of τ , player Pi would choose,
with high probability, the action corresponding to the maximum regret. This choice
leads to a stochastic variant of an algorithm called Joint Strategy Fictitious Play with
fading memory and inertia; see Section 3.3. Also, note that, for large values of τ ,
player Pi would choose any action having positive regret with equal probability.

63

According to these rules, player Pi will stay with his previous action ai (t − 1)
with probability 1 − αi (t) regardless of his regret. We make the following standing
assumption on the players’ willingness to optimize.
Assumption 4.3.1. There exist constants ε and ε̄ such that
0 < ε < αi (t) < ε̄ < 1
for all steps t > 1 and for all i ∈ {1, ..., n}.
This assumption implies that players are always willing to optimize with some
nonzero inertia1 . A motivation for the use of inertia is to instill a degree of hesitation
into the decision making process to ensure that players do not overreact to various
situations. We will assume that no player is indifferent between distinct strategies 2 .
Assumption 4.3.2. Player utilities satisfy
Ui (a1i , a−i ) 6= Ui (a2i , a−i ), ∀ a1i , a2i ∈ Ai , a1i 6= a2i , ∀ a−i ∈ A−i , ∀ i ∈ {1, ..., n}.
The following theorem establishes the convergence of regret based dynamics with
fading memory and inertia to a pure Nash equilibrium.
Theorem 4.3.1. In any weakly acyclic game satisfying Assumption 4.3.2, the action
profiles a(t) generated by regret based dynamics with fading memory and inertia satisfying Assumption 4.3.1 converge to a pure Nash equilibrium almost surely.
We provide a complete proof for the above result in the Appendix of this chapter.
We note that, in contrast to the existing weak convergence results for regret matching
in general games, the above result characterizes the long-term behavior of regret based
dynamics with fading memory and inertia, in a strong sense, albeit in a restricted class
of games. We next numerically verify our theoretical result through some simulations.
1
2

This assumption can be relaxed to holding for sufficiently large t, as opposed to all t.
One could alternatively assume that all pure Nash equilibrium are strict.

64

4.4

Simulations

4.4.1

Three Player Identical Interest Game

We extensively simulated the RB iterations for the game considered in Figure 4.1. We
used the RBi function given in (4.4) with inertia factor α = 0.5 and discount factor
ρ = 0.1. In all cases, player action profiles a(t) converged to one of the pure Nash
equilibria as predicted by our main theoretical result. A typical simulation run shown
in Figure 4.2 illustrates the convergence of RB iterations to the pure Nash equilibrium
(D, R, M3 ).

D

ay 1(k):
(t)
1

U
0

50

100

150

200

250

300

200

250

300

200

250

300

step
k
time
step:
t

R
(k):
ay 2
(t)
2
L
0

50

100

150
step
k
time
step:
t

M
3

ay 3(k):
(t) M
3

2

M
1

0

50

100

150
step
k
time
step:
t

Figure 4.2: Evolution of the actions of players using RB.

65

4.4.2

Distributed Traffic Routing

We consider a simple congestion game, as defined in Section 2.3.3, with 100 players
seeking to traverse from node A to node B along 5 different parallel roads as illustrated
in Figure 4.3. Each player can select any road as a possible route. In terms of congesRoad 1
Road 2

A

Road 3

B

Road 4
Road 5

Figure 4.3: Regret Based Dynamics with Inertia: Congestion Game Example – Network Topology

tion games, the set of resources is the set of roads, R, and each player can select one
road, i.e., Ai = R.
We will assume that each road has a linear cost function with positive (randomly
chosen) coefficients,
cri (k) = ai k + bi , i = 1, ..., 5,
where k represent the number of vehicles on that particular road. This cost function
may represent the delay incurred by a driver as a function of the number of other drivers
sharing the same road. The actual coefficients or structural form of the cost function
are unimportant as we are just using this example as an opportunity to illustrate the
convergence properties of the proposed regret based algorithms.
We simulated a case where drivers choose their initial routes randomly, and every
day thereafter, adjusted their routes using the regret based dynamics with the RBi
function given in (4.4) with inertia factor α = 0.85 and discount factor ρ = 0.1. The

66

number of vehicles on each road fluctuates initially and then stabilizes as illustrated in
Figure 4.4. Figure 4.5 illustrates the evolution of the congestion cost on each road. One
can observe that the congestion cost on each road converges approximately to the same
value, which is consistent with a Nash equilibrium with large number of drivers. This
behavior resembles an approximate “Wardrop equilibrium” [War52], which represents
a steady-state situation in which the congestion cost on each road is equal due to the
fact that, as the number of drivers increases, the effect of an individual driver on the
traffic conditions becomes negligible.
40
Road 1
Road 2
Road 3
Road 4
Road 5

35

Number of Drivers on Each Road

30

25

20

15

10

5
0

50

100

150

200

250

Iteration Number

Figure 4.4: Regret Based Dynamics with Inertia: Evolution of Number of Vehicles on Each
Route

We would like to note that the simplistic nature of this example was solely for
illustrative purposes. Regret based dynamics could be employed on any congestion
game with arbitrary network topology and congestion functions. Furthermore, well
known learning algorithms such as fictitious play [MS96a] could not be implemented
even on this very simple congestion game. A driver using fictitious play would need

67

60
Road 1
Road 2
Road 3
Road 4
Road 5

55

50

Congestion Cost on Each Road

45

40

35

30

25

20

15

10
0

50

100

150

200

250

Iteration Number

Figure 4.5: Regret Based Dynamics with Inertia: Evolution of Congestion Cost on Each Route

to track the empirical frequencies of the choices of the 99 other drivers and compute
an expected utility evaluated over a probability space of dimension 599 .
We would also like to note that in a congestion game, it may be unrealistic to
assume that players are aware of the congestion function on each road. This implies
that each driver is unaware of his own utility function. However, even in this setting,
regret based dynamics can be effectively employed under the condition that each player
can evaluate congestion levels on alternative routes. On the other hand, if a player
is only aware of the congestion experienced, then one would need to examine the
applicability of payoff based algorithms [MYA07] which will be discussed in detail in
the following chapter.

68

4.5

Concluding Remarks and Future Work

In this chapter we analyzed the applicability of regret based algorithms on multi-agent
systems. We demonstrated that a point of no-regret may not necessarily be a desirable
operating condition. Furthermore, the existing results on regret based algorithms do
not preclude these inferior operating points. Therefore, we introduced a modification
of the traditional no-regret algorithms that (i) exponentially discounts the memory and
(ii) brings in a notion of inertia in players’ decision process. We showed how these
modifications can lead to an entire class of regret based algorithms that provide convergence to a pure Nash equilibrium in any weakly acyclic game. We believe that
similar results hold for no-regret algorithms without fading memory and inertia but
thus far the proofs have been elusive.

4.6

Appendix to Chapter 4

4.6.1

Proof of Theorem 4.3.1

We will first state and prove a series of claims. The first claim states that if at any time
a player plays an action with positive regret, then the player will play an action with
positive regret at all subsequent time steps.
Claim 4.6.1. Fix any t0 > 1. Then,
a (t )

a (t)

R̃i i 0 (t0 ) > 0 ⇒ R̃i i (t) > 0
for all t > t0 .
a (t )

Proof. Suppose R̃i i 0 (t0 ) > 0. We have
a (t )

a (t )

R̃i i 0 (t0 + 1) = (1 − ρ)R̃i i 0 (t0 ) > 0.

69

If ai (t0 + 1) = ai (t0 ), then
a (t +1)

R̃i i 0

a (t )

(t0 + 1) = R̃i i 0 (t0 + 1) > 0.

If ai (t0 + 1) 6= ai (t0 ), then
a (t +1)

R̃i i 0

(t0 + 1) > 0.
a (t)

The argument can be repeated to show that R̃i i (t) > 0, for all t > t0 .
Define
Mu := max{Ui (a) : a ∈ A, Pi ∈ P},
mu := min{Ui (a) : a ∈ A, Pi ∈ P},
δ := min{|Ui (a1 ) − Ui (a2 )| > 0 :
a1 , a2 ∈ A, a1−i = a2−i , Pi ∈ P},
N := min{n ∈ {1, 2, ...} :
(1 − (1 − ρ)n )δ − (1 − ρ)n (Mu − mu ) > δ/2},
f := min{RBim (x) : |x` | ≤ Mu − mu , ∀`,
xm ≥ δ/2, for one m, ∀Pi ∈ P}.
Note that δ, f > 0, and |R̃iai (t)| ≤ Mu − mu , for all Pi ∈ P, ai ∈ Ai , t > 1.
The second claim states a condition describing the absorptive properties of a strict
Nash equilibrium.
Claim 4.6.2. Fix t0 > 1. Assume
1. a(t0 ) is a strict Nash equilibrium, and
a (t )

2. R̃i i 0 (t0 ) > 0 for all Pi ∈ P, and
3. a(t0 ) = a(t0 + 1) = ... = a(t0 + N − 1).

70

Then, a(t) = a(t0 ), for all t ≥ t0 .
Proof. For any Pi ∈ P and any ai ∈ Ai , we have
R̃iai (t0 + N ) = (1 − ρ)N R̃iai (t0 )

+ 1 − (1 − ρ)N Ui (ai , a−i (t0 ))

−Ui (ai (t0 ), a−i (t0 )) .
Since a(t0 ) is a strict Nash equilibrium, for any Pi ∈ P and any ai ∈ Ai , ai 6= ai (t0 ),
we have
Ui (ai , a−i (t0 )) − Ui (ai (t0 ), a−i (t0 )) ≤ −δ.
Therefore, for any Pi ∈ P and any ai ∈ Ai , ai 6= ai (t0 ),
R̃iai (t0 + N ) ≤ (1 − ρ)N (Mu − mu ) − (1 − (1 − ρ)N )δ
< −δ/2 < 0.
We also know that, for all Pi ∈ P,
a (t )

a (t )

R̃i i 0 (t0 + N ) = (1 − ρ)N R̃i i 0 (t0 ) > 0.
This proves the claim.
The third claim states an event, and associated probability, where the ensuing joint
action is a better response to the current joint action profile.
Claim 4.6.3. Fix t0 > 1. Assume
1. a(t0 ) is not a Nash equilibrium, and
2. a(t0 ) = a(t0 + 1) = ... = a(t0 + N − 1)

71

Let a∗ = (a∗i , a−i (t0 )) be such that
Ui (a∗i , a−i (t0 )) > Ui (ai (t0 ), a−i (t0 )),
a∗

for some Pi ∈ P and some a∗i ∈ Ai . Then, R̃i i (t0 + N ) > δ/2, and a∗ will be chosen
at step t0 + N with at least probability γ := (1 − )n−1 f .
Proof. We have
a∗

R̃i i (t0 + N ) ≥ −(1 − ρ)N (Mu − mu ) + (1 − (1 − ρ)N )δ
> δ/2.
Therefore, the probability of player Pi choosing a∗i at step t0 + N is at least f . Because of players’ inertia, all other players will repeat their actions at step t0 + N with
probability at least (1 − )n−1 . This means that the action profile a∗ will be chosen at
step t0 + N with probability at least (1 − )n−1 f .
The fourth claim identifies a particular event, and associated probability, guaranteeing that each player will only play actions with positive regret as discussed in
Claim 4.6.1.
a (t)

Claim 4.6.4. Fix t0 > 1. We have R̃i i (t) > 0 for all t ≥ t0 + 2N n and for all
Pi ∈ P with probability at least
n
Y
1
γ(1 − )2N n .
|Ai |
i=1
a0

Proof. Let a0 := a(t0 ). Suppose R̃i i (t0 ) ≤ 0. Furthermore, suppose that a0 is repeated N consecutive times, i.e. a(t0 ) = ... = a(t0 + N − 1) = a0 , which occurs with
at least probability at least (1 − )n(N −1) .
If there exists a a∗ = (a∗i , a0−i ) such that Ui (a∗ ) > Ui (a0 ), then, by Claim 4.6.3,
a∗

R̃i i (t0 + N ) > δ/2 and a∗ will be chosen at step t0 + N with at least probability γ.
a (t)

Conditioned on this, we know from Claim 4.6.1 that R̃i i (t) > 0 for all t ≥ t0 + N .

72

If there does not exist such an action a∗ , then R̃iai (t0 + N ) ≤ 0 for all ai ∈ Ai . An
0
0
w
0
action profile (aw
i , a−i ) with Ui (ai , a−i ) < Ui (a ) will be chosen at step t0 + N with at
0
w
0
least probability |A1i | (1−)n−1 . If a(t0 +N ) = (aw
i , a−i ), and if furthermore (ai , a−i ) is

repeated N consecutive times, i.e., a(t0 + N ) = ... = a(t0 + 2N − 1), which happens
a0

with probability at least (1 − )n(N −1) , then, by Claim 4.6.3, R̃i i (t0 + 2N ) > δ/2
and the action profile a0 will be chosen at step (t0 + 2N ) with at least probability γ.
a (t)

Conditioned on this, we know from Claim 4.6.1 that R̃i i (t) > 0 for all t ≥ t0 + 2N .
a (t)

In summary, R̃i i (t) > 0 for all t ≥ t0 + 2N with at least probability
1
γ(1 − )2N n .
|Ai |
a (t)

We can repeat this argument for each player to show that R̃i i (t) > 0 for all times
t ≥ t0 + 2N n and for all Pi ∈ P with probability at least
n
Y
1
γ(1 − )2N n .
|Ai |
i=1

FINAL STEP: Establishing convergence to a strict Nash equilibrium:
Proof. Fix t0 > 1. Define t1 := t0 + 2N n. Let a1 , a2 , . . . , aL be a finite sequence of
action profiles satisfying the conditions given in Subsection 2.3.4 with a1 := a(t1 ).
a (t)

Suppose R̃i i (t) > 0 for all t ≥ t1 and for all Pi ∈ P, which, by Claim 4.6.4,
occurs with probability at least
n
Y
1
γ(1 − )2N n .
|A
|
i
i=1

Suppose further that a(t1 ) = ... = a(t1 + N − 1) = a1 which occurs with at least
probability (1 − )n(N −1) . According to Claim 4.6.3 the action profile a2 will be played
at step t2 := t1 + N with at least probability γ. Suppose now a(t2 ) = ... = a(t2 +

73

N − 1) = a2 , which occurs with at least probability (1 − )n(N −1) . According to
Claim 4.6.3, the action profile a3 will be played at step t3 := t2 + N with at least
probability γ.
We can repeat the above arguments until we reach the strict Nash equilibrium aL
at step tL (recursively defined as above) and stay at aL for N consecutive steps. From
Claim 2, this would mean that the action profile would stay at aL for all t ≥ tL .
Therefore, given t0 > 1, there exists constants ˜ > 0 and T̃ > 0, both of which are
independent of t0 , and a strict Nash equilibrium a∗ , such that the following event happens with at least probability ˜: a(t) = a∗ for all t ≥ t0 + T̃ . This proves Theorem 4.1.

74

CHAPTER 5
Payoff Based Dynamics for Weakly Acyclic Games
We consider repeated multi-player games in which players repeatedly and simultaneously choose strategies from a finite set of available strategies according to some
strategy adjustment process. We focus on the specific class of weakly acyclic games,
which is particularly relevant for multi-agent cooperative control problems. A strategy adjustment process determines how players select their strategies at any stage as
a function of the information gathered over previous stages. Of particular interest
are “payoff based” processes, in which at any stage, players only know their own actions and (noise corrupted) payoffs from previous stages. In particular, players do not
know the actions taken by other players and do not know the structural form of payoff
functions. We introduce three different payoff based processes for increasingly general scenarios and prove that after a sufficiently large number of stages, player actions
constitute a Nash equilibrium at any stage with arbitrarily high probability. We also
show how to modify player utility functions through tolls and incentives in so-called
congestion games, a special class of weakly acyclic games, to guarantee that a centralized objective can be realized as a Nash equilibrium. We illustrate the methods with a
simulation of distributed routing over a network.

75

5.1

Introduction

The objective in distributed cooperative control for multi-agent systems is to enable
a collection of “self-interested” agents to achieve a desirable “collective” objective.
There are two overriding challenges to achieving this objective. The first is complexity:
finding an optimal solution by a centralized algorithm may be prohibitively difficult
when there are large numbers of interacting agents. This motivates the use of adaptive
methods that enable agents to “self organize” into suitable, if not optimal, collective
solutions.
The second challenge is limited information. Agents may have limited knowledge
about the status of other agents, except perhaps for a small subset of “neighboring”
agents. An example is collective motion control for mobile sensor platforms (e.g.,
[GSM05]). In these problems, mobile sensors seek to position themselves to achieve
various collective objectives such as rendezvous or area coverage. Sensors can communicate with neighboring sensors, but otherwise do not have global knowledge of the
domain of operation or the status and locations of non-neighboring sensors.
A typical assumption is that agents are endowed with a reward or utility function
that depends on their own strategies and the strategies of other agents. In motion
coordination problems, for example, an agent’s utility function typically depends on
its position relative to other agents or environmental targets, and knowledge of this
function guides local motion adjustments.
In other situations, agents may know nothing about the structure of their utility
functions, and how their own utility depends on the actions of other agents (whether local or far away). In this case the only thing they can do is observe rewards based on experience and “optimize” on a trial and error basis. The situation is further complicated
because all agents are trying simultaneously to optimize their own strategies. There-

76

fore, even in the absence of noise, an agent trying the same strategy twice may see
different results because of the non-stationary nature of the strategies of other agents.
There are several examples of multi-agent systems that illustrate this situation. In
distributed routing for ad hoc data networks (e.g., [BK03]), routing nodes seek to route
packets to neighboring nodes based on packet destinations without knowledge of the
overall network structure. The objective is to minimize the delay of packets to their
destinations. This delay must be realized through trial and error, since the functional
dependence of delay on routing strategies is not known. A similar problem is automotive traffic routing, in which drives seek to minimize the congestion experienced to get
to a desired destination. Drivers can experience the congestion on selected routes as a
function of the routes selected by other drivers, but drivers do not know the structure of
the congestion function. Finally, in a multi-agent approach to designing manufacturing
systems (e.g., [Ger94]), it may not be known in advance how performance measures
(such as throughput) depend on manufacturing policy. Rather performance can only
be measured once a policy is implemented.
Our interest in this chapter is to develop algorithms that enable coordination in
multi-agent systems for precisely this “payoff based” scenario, in which agents only
have access to (possibly noisy) measurements of the rewards received through repeated
interactions with other agents. We adopt the framework of “learning in games” (see
[FL98, Har05, You98, You05] for an extensive overview). Unlike most of the learning
rules in this literature, which assume that agents adjust their behavior based on the
observed behavior of other agents, we shall assume that agents know only their own
past actions and the payoffs that resulted. It is far from obvious that Nash equilibrium
can be achieved under such a restriction, but in fact it has recently been shown that such
“payoff based” learning rules can be constructed that work in any game [FY06, GL].
In this chapter we show that there are simpler and more intuitive adjustment rules

77

that achieve this objective for a large class of multi-player games known as “weakly
acyclic” games. This class captures many problems of interest in cooperative control
[MAS07a, MAS07b]. It includes the very special case of “identical interest” games,
where each agent receives the same reward. However, weakly acyclic games (and the
related concept of potential games) capture other scenarios such as congestion games
[Ros73] and similar problems such as distributed routing in networks, weapon target assignment, consensus, and area coverage. See [MAS05, AMS07] and referenced
therein for a discussion of a learning in games approach to cooperative control problems, but under less stringent assumptions on informational constraints considered in
this chapter.
For many multi-agent problems, operation at a pure Nash equilibrium may reflect
optimization of a collective objective.1 We will derive payoff based dynamics that
guarantee asymptotically that agent strategies will constitute a pure Nash equilibrium
with arbitrarily high probability. It need not always be the case that at least one Nash
equilibrium optimizes a collective objective. Motivated by this consideration, we also
discuss the introduction of incentives or tolls in a player’s payoff function to assure
that there is at least one Nash equilibrium that optimizes a collective objective. Even
in this case, however, there may still be suboptimal Nash equilibria.
The remainder of this chapter is organized as follows. Section 5.2 introduces three
types of payoff based dynamics in for increasingly general problems. Section 5.2.1
presents “Safe Experimentation Dynamics” which is restricted to identical interest
games. Section 5.2.2 presents “Simple Experimentation Dynamics” for the more general class of weakly acyclic games but with noise free payoff measurements. Section 5.2.3 presents “Sample Experimentation Dynamics” for weakly acyclic games
with noisy payoff measurements. Section 5.3 discusses how to introduce tolls and
1

Nonetheless, there are varied viewpoints on the role of Nash equilibrium as a solution concept for
multi-agent systems. See [SPG07] and [MS07].

78

incentives in payoffs so that a Nash equilibrium optimizes a collective objective. Section 5.4 presents an illustrative example of a traffic congestion game. Finally, Section 5.5 contains some concluding remarks. An important analytical tool throughout is
the method of resistance trees for perturbed Markov chains [You93], which is reviewed
in the appendix of this chapter.

5.2

Payoff Based Learning Algorithms

In this section, we will introduce three simple payoff based learning algorithms. The
first, called Safe Experimentation, guarantees convergence to a pure optimal Nash
equilibrium in any identical interest game. Such an equilibrium is optimal because
each player’s utility is maximized. The second learning algorithm, called Simple
Experimentation, guarantees convergence to a pure Nash equilibrium in any weakly
acyclic game. The third learning algorithm, called Sample Experimentation, guarantees convergence to a pure Nash equilibrium in any weakly acyclic game even when
utility measurements are corrupted with noise.
For each learning algorithm, we consider a repeated strategic form game, as described in Section 2.4, with n-player set P := {P1 , ..., Pn }, a finite action set Ai for
each player Pi ∈ P, and a utility function Ui : A → R for each player Pi ∈ P, where
A := A1 × · · · × An .

5.2.1
5.2.1.1

Safe Experimentation Dynamics for Identical Interest Games
Constant Exploration Rates

Before introducing the learning dynamics, we introduce the following function. Let
Uimax (t) := max Ui (a(τ ))
0≤τ ≤t−1

79

be the maximum utility that player Pi has received up to time t − 1.
We will now introduce the Safe Experimentation dynamics for identical interest
games; see Section 2.3.1 for a review of identical interest games.
1. Initialization: At time t = 0, each player randomly selects and plays any action,
ai (0). This action will be initially set as the player’s baseline action at time t = 1
and is denoted by abi (1) = ai (0).
2. Action Selection: At each subsequent time step, each player selects his baseline
action with probability (1 − ) or experiments with a new random action with
probability , i.e.:
• ai (t) = abi (t) with probability (1 − )
• ai (t) is chosen randomly (uniformly) over ai with probability 
The variable  will be referred to as the player’s exploration rate.
3. Baseline Strategy Update: Each player compares the actual utility received,
Ui (a(t)), with the maximum received utility Uimax (t) and updates his baseline
action as follows:
abi (t + 1) =



ai (t),

Ui (a(t)) > Uimax (t);


ab (t),
i

Ui (a(t)) ≤ Uimax (t).

This step is performed whether or not Step 2 involved exploration.
4. Return to Step 2 and repeat.
The reason that this learning algorithm is called “Safe” Experimentation is that
the utility evaluated at the baseline action, U (ab (t)), is non-decreasing with respect to
time.

80

Theorem 5.2.1. Let G be a finite n-player identical interest game in which all players
use the Safe Experimentation dynamics. Given any probability p < 1, if the exploration
rate  > 0 is sufficiently small, then for all sufficiently large times t, a(t) is an optimal
Nash equilibrium of G with at least probability p.
Proof. Since G is an identical interest game, let the utility of each player be expressed
as U : A → R and let A∗ be the set of “optimal” Nash equilibrium of G, i.e.,
A∗ = {a∗ ∈ A : U (a∗ ) = max U (a)}.
a∈A

For any joint action, a(t), the ensuing joint action will constitute an optimal Nash
equilibrium with at least probability








···
,
|A1 |
|A2 |
|An |
where |Ai | denotes the cardinality of the action set of player Pi . Therefore, an optimal
Nash equilibrium will eventually be played with probability 1 for any  > 0.
Suppose an optimal Nash equilibrium is first played at time t∗ , i.e., a(t∗ ) ∈ A∗ and
a(t∗ − 1) ∈
/ A∗ . Then the baseline joint action must remain constant from that time
onwards, i.e., ab (t) = a(t∗ ) for all t > t∗ . An optimal Nash equilibrium will then be
played at any time t > t∗ with at least probability (1 − )n . Since  > 0 can be chosen
arbitrarily small, and in particular such that (1 − )n > p this completes the proof.

5.2.1.2

Diminishing Exploration Rates

In the Safe Experimentation dynamics, the exploration rate  was defined as a constant.
Alternatively, one could let the exploration rate vary to induce desirable behavior. One
example would be to let the exploration rate decay, such as t = (1/t)1/n . This would
induce exploration at early stages and reduce exploration at later stages of the game.

81

The theorem and proof hold under the following conditions for the exploration rate:
lim t = 0,





t 
Y
τ
τ
τ
lim
1−
···
= 0.
t→∞
|A1 |
|A2 |
|An |
τ =1
t→∞

5.2.2

Simple Experimentation Dynamics for Weakly Acyclic Games

We will now introduce the Simple Experimentation dynamics for weakly acyclic games;
see Section 2.3.4 for a review of weakly acyclic games. These dynamics will allow us
to relax the assumption of identical interest games.
1. Initialization: At time t = 0, each player randomly selects and plays any action,
ai (0). This action will be initially set as the player’s baseline action at time 1,
i.e., abi (1) = ai (0). Likewise, the player’s baseline utility at time 1 is initialized
as ubi (1) = Ui (a(0)).
2. Action Selection: At each subsequent time step, each player selects his baseline
action with probability (1 − ) or experiments with a new random action with
probability .
• ai (t) = abi (t) with probability (1 − )
• ai (t) is chosen randomly (uniformly) over ai with probability 
The variable  will be referred to as the player’s exploration rate. Whenever
ai (t) 6= abi (t), we will say that player Pi experimented.
3. Baseline Action and Baseline Utility Update: Each player compares the utility
received, Ui (a(t)), with his baseline utility, ubi (t), and updates his baseline action
and utility as follows:
• If player Pi experimented (i.e., ai (t) 6= abi (t)) and if Ui (a(t)) > ubi (t) then

82

abi (t + 1) = ai (t),
ubi (t + 1) = Ui (a(t)).
• If player Pi experimented and if Ui (a(t)) ≤ ubi (t) then
abi (t + 1) = abi (t),
ubi (t + 1) = ubi (t).
• If player Pi did not experiment (i.e., ai (t) = abi (t)) then
abi (t + 1) = abi (t),
ubi (t + 1) = Ui (a(t)).
4. Return to Step 2 and repeat.
As before, these dynamics require only utility measurements, and hence almost no
information regarding the structure of the game.
Theorem 5.2.2. Let G be a finite n-player weakly acyclic game in which all players
use the Simple Experimentation dynamics. Given any probability p < 1, if the exploration rate  > 0 is sufficiently small, then for all sufficiently large times t, a(t) is a
Nash equilibrium of G with at least probability p.
The remainder of this subsection is devoted to the proof of Theorem 5.2.2. The
proof rely on the theory of resistance trees for perturbed Markov chains (see the appendix of this chapter for a brief review).
Define the state of the dynamics to be the pair [a, u], where a is the baseline joint
action and u is the baseline utility vector. We will omit the superscript b to avoid
cumbersome notation.
Partition the state space into the following three sets. First, let X be the set of states
[a, u] such that ui 6= Ui (a) for at least one player Pi . Let E be the set of states [a, u]
such that ui = Ui (a) for all players Pi and a is a Nash equilibrium. Let D be the set

83

of states [a, u] such that ui = Ui (a) for all players Pi and a is a disequilibrium (not a
Nash equilibrium). These are all the states.
Claim 5.2.1.

a. Any state [a, u] ∈ X transitions to a state in E ∪ D in one period

with probability O(1).
b. Any state [a, u] ∈ E ∪ D transitions to a different state [a0 , u0 ] with probability
at most O(ε).
Proof. For any [a, u0 ] ∈ X, there exists at least one player Pi such that u0i 6= Ui (a). If
all players repeat their part of the joint action profile a which occurs with probability
(1 − )n , then [a, u0 ] transitions to [a, u], where ui = Ui (a) for all players Pi . Thus
the process moves to [a, u] ∈ E ∪ D with prob O(1). This proves statement (a). As
for statement (b), any state in E ∪ D transitions back to itself whenever no player
experiments, which occurs with probability at least O(1).
Claim 5.2.2. For any state [a, u] ∈ D, there is a finite sequence of transitions to a
state [a∗ , u∗ ] ∈ E, where the transitions have the form2 :
[a, u] → [a1 , u1 ] → ... → [a∗ , u∗ ]
O()

O()

O()

where uki = Ui (ak ) for all i and for all k > 0, and each transition occurs with probability O().
Proof. Such a sequence is guaranteed by weak acyclicity. Since a is not an equilibrium, there is a better reply path from a to some equilibrium a∗ , say a, a1 , a2 , ..., a∗ .
At [a, u] the appropriate player Pi experiments with probability , chooses the appropriate better reply with probability 1/|Ai |, and no one else experiments. Thus the
process moves to [a1 , u1 ] where u1i = Ui (a1 ) for all players Pi with probability O().
2

We will use the notation z → z 0 to denote the transition from state z to state z 0 . We use z → z 0 to
O()

emphasize that this transition occurs with probability of order .

84

Notice that for the deviator Pi , Ui (a1 ) > Ui (a), therefore u1i = Ui (a1 ). For the nondeviator, say player Pj , u1j = Uj (a1 ) since a1j = aj . Thus [a1 , u1 ] ∈ D ∪ E. In the next
period, the appropriate player deviates and so forth.

Claim 5.2.3. For any equilibrium [a∗ , u∗ ] ∈ E, any path from [a∗ , u∗ ] to another state
[a, u] ∈ E ∪ D, a 6= a∗ , that does not loop back to [a∗ , u∗ ] must be of one of the
following two forms:
1. [a∗ , u∗ ] → [a∗ , u0 ] → [a0 , u00 ] → ... → [a, u], where k ≥ 2;
O()

O(k )

2. [a∗ , u∗ ] → [a0 , u00 ] → ... → [a, u], where k ≥ 2.
O(k )

Proof. The path must begin by either one player experimenting or more that one player
experimenting. Case (2) results if more than one player experiments. Case (1) results
if exactly one agent, say agent Pi , experiments with an action a0i 6= a∗i and all other
players continue to play their part of a∗ . This happens with probability |Ai | (1 − )n−1 .
In this situation, player Pi cannot be better off, meaning that Ui (a0i , a∗−i ) ≤ Ui (a∗ ),
since by assumption a∗ is an equilibrium. Hence the baseline action next period remains a∗ for all players, though their baseline utilities may change. Denote the next
state by [a∗ , u0 ]. If in the subsequent period all players continue to play their part of
the action a∗ again, which occurs with probability (1 − )n , then the state reverts back
to [a∗ , u∗ ] and we have a loop. Hence the only way the path can continue without a
loop is for one or more players to experiment in the next stage, which has probability
O(k ), k ≥ 1. This is exactly what case (1) alleges.

Proof of Theorem 5.2.2. This is a finite aperiodic Markov process on the state space
A × Ū , where Ū denotes the finite set of baseline utility vectors. Furthermore, from

85

every state there exists a positive probability path to a Nash equilibrium. Hence, every
recurrent class has at least one Nash equilibrium. We will now show that within any
recurrent class, the trees (see the appendix of this chapter) rooted at the Nash equilibrium will have the lowest resistance. Therefore, according to Theorem 5.6.1, the
a priori probability that the state will be a Nash equilibrium can be made arbitrarily
close to 1.
In order to apply Theorem 5.6.1, we will construct minimum resistance trees with
vertices consisting of every possible state (within a recurrence class). Each edge will
have resistance 0, 1, 2, ... associated with the transition probabilities
O(1), O(), O(2 ), ..., respectively.
Our analysis will deviate slightly from the presentation in the appendix. In the discussion in the appendix, the vertices of minimum resistance trees are recurrence classes
of an associated unperturbed Markov chain. In this case, the unperturbed Markov chain
corresponds to Simple Experimentation dynamics with  = 0, and so the recurrence
classes are all states in E ∪ D. Nonetheless, we will construct resistance trees with the
vertices being all possible states, i.e., E ∪ D ∪ X. The resulting conclusions remain the
same. Since the states in X are transient with probability O(1), the resistance to leave
a node corresponding to a state in X is zero. Therefore, the presence of such states
does not affect the conclusions determining which states are stochastically stable.
Suppose a minimum resistance tree T is rooted at a vertex v that is not in E.
If v ∈ X, it is easy to construct a new tree that has lower resistance. Namely, by
Claim 5.2.1a, there is a 0-resistance one-hop path P from v to some state [a, u] ∈
E ∪ D. Add the edge of P to T and subtract the edge in T that exits from the vertex
[a, u]. This results in a [a, u]-tree T 0 . It has lower resistance than T because the added
edge has zero resistance while the subtracted edge has resistance greater than or equal
to 1 because of Claim 5.2.1b. This argument is illustrated in Figure 5.1, where the red

86

edge of strictly positive resistance is removed and replaced with the blue edge of zero
resistance.
Original Tree T (Rooted in X)

Revised Tree T' (Rooted in D or E)
[a, u'']

[a, u'']
R>1

[a, u']

[a, u']

[a, u]

[a, u]
R=0

[a', u']

[a', u']

[a', u]

[a', u]

Figure 5.1: Construction of alternative to tree rooted in X.

Suppose next that v = [a, u] ∈ D but not in E. Construct a path P as in Claim 5.2.2
from [a, u] to some state [a∗ , u∗ ] ∈ E. As above, construct a new tree T 0 rooted at
[a∗ , u∗ ] by adding the edges of P to T and taking out the redundant edges (the edges
in T that exit from the vertices in P ). The nature of the path P guarantees that the
edges taken out have total resistance at least as high as the resistances of the edges put
in. This is because the entire path P lies in E ∪ D, each transition on the path has
resistance 1, and, from Claim 5.2.2b, the resistance to leave any state in E ∪ D is at
least 1.
To construct a new tree that has strictly lower resistance, we will inspect the effect
of removing the exiting edge from [a∗ , u∗ ] in T . Note that this edge must fit either case
(1) or case (2) of Claim 5.2.3.
In case (2), the resistance of the exiting edge is at least 2, which is larger than
any edge in P . Hence the new tree has strictly lower resistance than T , which is a
contradiction. This argument is illustrated in Figure 5.2. A new path is created from
the original root [a, u] ∈ D to the equilibrium [a∗ , u∗ ] ∈ E (blue edges). Redundant

87

(red) edges emanating from the new path are removed. In case (2), the redundant edge
emanating from [a∗ , u∗ ] has a resistance of at least 2.
Original Tree T (Rooted in D - Case 2)

Revised Tree T' (Rooted in E)

[a, u'']

[a, u]

[a, u]

[a, u'']
R=1

R>1
[a, u']

[a', u']

[a', u'']

[a, u']

[a', u']

[a', u'']

R=1
R>1
[a'', u'']

[a*, u']

[a'', u'']
R>2

[a*, u']

R=1

[a*, u*]

[a*, u*]

Figure 5.2: Construction of alternative to tree rooted in D for Case (2).

In case (1), the exiting edge has the form [a∗ , u∗ ] → [a∗ , u0 ] which has resistance 1
where u∗ 6= u0 . The next edge in T , say [a∗ , u0 ] → [a0 , u00 ], also has at least resistance
1. Remove the edge [a∗ , u0 ] → [a0 , u00 ] from T , and put in the edge [a∗ , u0 ] → [a∗ , u∗ ].
The latter has resistance 0 since [a∗ , u0 ] ∈ X. This results in a tree T 00 that is rooted
at [a∗ , u∗ ] and has strictly lower resistance than does T , which is a contradiction. This
argument is illustrated in Figure 5.3. As in Figure 5.2, a new (blue) path is constructed
and redundant (red) edges are removed. The difference is that the edge [a∗ , u0 ] →
[a0 , u00 ] is removed and replaced with [a∗ , u0 ] → [a∗ , u∗ ].
To recap, a minimum resistant tree cannot be rooted at any state in X or D, and
therefore can only be rooted in E. Therefore, when  is sufficiently small, the long-run
probability on E can be made arbitrarily close to 1, and in particular larger than any
specified probability p.

88

Original Tree T (Rooted in D - Case 1)

Revised Tree T' (Rooted in E)

[a, u'']

[a, u]

[a, u]

[a, u'']
R=1

R>1
[a, u']

[a', u']

[a', u'']

[a, u']

[a', u']

[a', u'']

R=1

R>1
R>1
[a'', u'']

[a*, u']

[a'', u'']

R=1

R=1

[a*, u*]

[a*, u']
R=0

[a*, u*]

Figure 5.3: Construction of alternative to tree rooted in D for Case (1).

5.2.3

Sample Experimentation Dynamics for Weakly Acyclic Games with Noisy
Utility Measurements

5.2.3.1

Noise-free Utility Measurements

In this section we will focus on developing payoff based dynamics for which the limiting behavior exhibits that of a pure Nash equilibrium with arbitrarily high probability
in any finite weakly acyclic game even in the presence of utility noise. We will show
that a variant of the so-called Regret Testing algorithm [FY06] accomplishes this objective for weakly acyclic games with noisy utility measurements.
We now introduce Sample Experimentation dynamics.
1. Initialization: At time t = 0, each player randomly selects and plays any action,
ai (0) ∈ Ai . This action will be initially set as the player’s baseline action,
abi (1) = ai (0).
2. Exploration Phase: After the baseline action is set, each player engages in an

89

exploration phase over the next m periods. The length of the exploration phase
need not be the same or synchronized for each player, but we will assume that
they are for the proof. For convenience, we will double index the time of the
actions played as
ǎ(t1 , t2 ) = a(m t1 + t2 )
where t1 indexes the number of the exploration phase and t2 indexes the actions
played in that exploration phase. We will refer to t1 as the exploration phase
time and t2 as the exploration action time. By construction, the exploration
phase time and exploration action time satisfy t1 ≥ 1 and m ≥ t2 ≥ 1. The
baseline action will only be updated at the end of the exploration phase and will
therefore only be indexed by the exploration phase time.
During the exploration phase, each player selects his baseline action with probability (1 − ) or experiments with a new random action with probability . That
is, for any exploration phase time t1 ≥ 1 and for any exploration action time
satisfying m ≥ t2 ≥ 1,
• ǎi (t1 , t2 ) = abi (t1 ) with probability (1 − ),
• ǎi (t1 , t2 ) is chosen randomly (uniformly) over (Ai \abi (t1 )) with probability
.
Again, the variable  will be referred to as the player’s exploration rate.
3. Action Assessment: After the exploration phase, each player evaluates the average utility received when playing each of his actions during the exploration
phase. Let nai i (t1 ) be the number of times that player Pi played action ai during the exploration phase at time t1 . The average utility for action ai during the

90

exploration phase at time t1 is

Pm

 ai1
t2 =1 I{ai = ǎi (t1 , t2 )}Ui (ǎ(t1 , t2 )),
n
(t
)
1
i
V̂iai (t1 ) =

U ,
min

nai i (t1 ) > 0;
nai i (t1 ) = 0,

where I{·} is the usual indicator function and Umin satisfies
Umin < min min Ui (a).
i

a∈A

In words, Umin is less than the smallest payoff any agent can receive.
4. Evaluation of Better Response Set: Each player compares the average utility
ab (t)

received when playing his baseline action, V̂i i (t1 ), with the average utility
received for each of his other actions, V̂iai (t1 ), and finds all played actions which
performed δ better than the baseline action. The term δ will be referred to as the
players’ tolerance level. Define A∗i (t1 ) to be the set of actions that outperformed
the baseline action as follows:
o
n
ab (t )
A∗i (t1 ) := ai ∈ Ai : V̂iai (t1 ) ≥ V̂i i 1 (t1 ) + δ .

(5.1)

5. Baseline Strategy Update: Each player updates his baseline action as follows:
• If A∗i (t1 ) = ∅, then abi (t1 + 1) = abi (t1 ).
• If A∗i (t1 ) 6= ∅, then
– With probability ω, set abi (t1 + 1) = abi (t1 ). (We will refer to ω as the
player’s inertia.)
– With probability 1 − ω, randomly select abi (t1 + 1) ∈ A∗i (t1 ) with
uniform probability.
6. Return to Step 2 and repeat.

91

For simplicity, we will first state and prove the desired convergence properties
using noiseless utility measurements. The setup for the noisy utility measurements
will be stated afterwards.
Before stating the following theorem, we define the constant α > 0 as follows.
If Ui (a1 ) 6= Ui (a2 ) for any joint actions a1 , a2 ∈ A and any player Pi ∈ P, then
|Ui (a1 ) − Ui (a2 )| > α. In words, if any two joint actions result in different utilities at
all, then the difference would be at least α.
Theorem 5.2.3. Let G be a finite n-player weakly acyclic game in which all players
use the Sample Experimentation dynamics. For any
• probability p < 1,
• tolerance level δ ∈ (0, α),
• inertia ω ∈ (0, 1), and
• exploration rate  satisfying min{(α − δ)/4, δ/4, 1 − p} > (1 − (1 − )n ) > 0,
if the exploration phase length m is sufficiently large, then for all sufficiently large
times t > 0, a(t) is a Nash equilibrium of G with at least probability p.
The remainder of this subsection is devoted to the proof of Theorem 5.2.3.
We will assume for simplicity that utilities are between -1/2 and 1/2, i.e., |Ui (a)| ≤
1/2 for any player Pi ∈ P and any joint action a ∈ A.
We begin with a series of useful claims. The first claim states that for any player
Pi the average utility for an action ai ∈ Ai during the exploration phase can be made
arbitrarily close (with high probability) to the actual utility the player would have received provided that all other players never experimented. This can be accomplished

92

if the experimentation rate is sufficiently small and the exploration phase length is
sufficiently large.
Claim 5.2.4. Let ab be the joint baseline action at the start of an exploration phase of
length m. For
• any probability p < 1,
• any δ ∗ > 0, and
• any exploration rate  > 0 satisfying δ ∗ /2 ≥ (1 − (1 − )n−1 ) > 0,
if the exploration phase length m is sufficiently large then
h
i
Pr V̂iai − Ui (ai , ab−i ) > δ ∗ < 1 − p.
Proof. Let ni (ai ) represent the number of times player Pi played action ai during the
exploration phase. In the following discussion, all probabilities and expectations are
conditioned on ni (ai ) > 0. We omit making this explicit for the sake of notational
simplicity. The event ni (ai ) = 0 has diminishing probability as the exploration phase
length m increases, and so this case will not affect the desired conclusions for increasing phase lengths.
For an arbitrary δ ∗ > 0,
h
i
Pr V̂iai − Ui (ai , ab−i ) > δ ∗
i
h
≤ Pr V̂iai − E{V̂iai } + E{V̂iai } − Ui (ai , ab−i ) > δ ∗
i
h
h
i
ai
ai
ai
∗
b
∗
≤ Pr V̂i − E{V̂i } > δ /2 + Pr E{V̂i } − Ui (ai , a−i ) > δ /2 .
|
{z
} |
{z
}
(∗)

(∗∗)

First, let us focus on (∗∗). We have
h
i
E{V̂iai } − Ui (ai , ab−i ) = [1 − (1 − )n−1 ] E{Ui (ai , a−i (t))|a−i (t) 6= ab−i } − Ui (ai , ab ) ,

93

which approaches 0 as  ↓ 0. Therefore, for any exploration rate  satisfying δ ∗ /2 >
(1 − (1 − )n−1 ) > 0, we know that
h
i
ai
b
∗
Pr E{V̂i } − Ui (ai , a−i ) > δ /2 = 0.
Now we will focus on (∗). By the weak law of large numbers, (∗) approaches 0 as
ni (ai ) ↑ ∞. This implies that for any probability p̄ < 1 and any exploration rate  > 0,
there exists a sample size n∗i (ai ) such that if ni (ai ) > n∗i (ai ) then
h
i
ai
ai
Pr V̂i − E{V̂i } > ρ/2 < 1 − p̄.
Lastly, for any probability p̄ < 1 and any fixed exploration rate, there exists a minimum
exploration length m > 0 such that for any exploration length m > m,
Pr [ni (ai ) ≥ n∗i (ai )] ≥ p̄.
In summary, for any fixed exploration rate  satisfying δ ∗ /2 ≥ (1 − (1 − )n−1 ) > 0,
(∗) + (∗∗) can be made arbitrarily close to 0, provided that the exploration length m is
sufficiently large.
Claim 5.2.5. Let ab be the joint baseline action at the start of an exploration phase of
length m. For any
• probability p < 1,
• tolerance level δ ∈ (0, α), and
• exploration rate  > 0 satisfying min{(α − δ)/4, δ/4} ≥ (1 − (1 − )n−1 ) > 0,
if the exploration length m is sufficiently large, then each player’s better response set
a∗i will contain only and all actions that are a better response to the joint baseline
action, i.e.,
a∗i ∈ A∗i ⇔ Ui (a∗i , ab−i ) > Ui (ab )
with at least probability p.

94

Proof. Suppose ab is not a Nash equilibrium. For some player Pi ∈ P, let a∗i be a
strict better reply to the baseline joint action, i.e. Ui (a∗i , ab−i ) > Ui (ab ) and let aw
i be a
b
b
non-better reply to the baseline joint action, i.e. Ui (aw
i , a−i ) ≤ Ui (a ).

Using Claim 5.2.4, for any probability p̄ < 1 and any exploration rate  > 0
satisfying min{(α − δ)/4, δ/4} ≥ (1 − (1 − )n−1 ) > 0 there exists a minimum
exploration length m > 0 such that for any exploration length m > m the following
expressions are true:
h b
i
a
Pr |V̂i i − Ui (abi , ab−i )| < δ ∗ ≥ p̄,
h ∗
i
ai
∗ b
∗
Pr |V̂i − Ui (ai , a−i )| < δ
≥ p̄,
h w
i
a
b
∗
Pr |V̂i i − Ui (aw
≥ p̄,
i , a−i )| < δ

(5.2)
(5.3)
(5.4)

where δ ∗ = min{(α − δ)/2, δ/2}. Rewriting equation 5.2 we obtain
h b
i
h b
i
a
a
Pr |V̂i i − Ui (abi , ab−i )| < δ ∗ ≤ Pr V̂i i − Ui (abi , ab−i ) < (α − δ)/2 ,
and rewriting equation 5.3 we obtain
h ∗
i
h ∗
i
ai
ai
∗ b
∗
∗ b
Pr |V̂i − Ui (ai , a−i )| < δ
≤ Pr V̂i − Ui (ai , a−i ) > −(α − δ)/2 ,
h ∗
i
a
≤ Pr V̂i i − (Ui (abi , ab−i ) + α) > −(α − δ)/2 ,
h ∗
i
a
= Pr V̂i i − Ui (abi , ab−i ) > (α + δ)/2 ,
meaning that
Pr [a∗i ∈ A∗i ] ≥ p̄2 .
Similarly, rewriting equation 5.2 we obtain
h b
i
h b
i
a
a
Pr |V̂i i − Ui (abi , ab−i )| < δ ∗ ≤ Pr V̂i i − Ui (abi , ab−i ) > −δ/2 ,
and rewriting equation 5.4 we obtain
h w
i
h w
i
a
ai
b
∗
w
b
≤
Pr
V̂
,
a
)
<
δ/2
,
Pr |V̂i i − Ui (aw
,
a
)|
<
δ
−
U
(a
i i
−i
i
−i
i
h w
i
a
≤ Pr V̂i i − Ui (abi , ab−i ) < δ/2 ,

95

meaning that
Pr [aw
/ A∗i ] ≥ p̄2 .
i ∈
Since p̄ can be chosen arbitrarily close to 1, the proof is complete.
Theorem 5.2.3. The evolution of the baseline actions from phase to phase is a finite
aperiodic Markov process on the state space of joint actions, A. Furthermore, since G
is weakly acyclic, from every state there exists a better reply path to a Nash equilibrium. Hence, every recurrent class has at least one Nash equilibrium. We will show that
these dynamics can be viewed as a perturbation of a certain a Markov chain whose recurrent classes are restricted to Nash equilibria. We will then appeal to Theorem 5.6.1
to derive the desired result.
We begin by defining an “unperturbed” process on baseline actions. For any ab ∈
A, define the true better reply set as

Ā∗i (ab ) := ai : Ui (ai , ab−i ) > Ui (ab ) .
Now define the transition process from ab (t1 ) to ab (t1 + 1) as follows:
• If Ā∗i (ab (t1 )) = ∅, then abi (t1 + 1) = abi (t1 ).
• If Ā∗i (ab (t1 )) 6= ∅, then
– With probability ω, set abi (t1 + 1) = abi (t1 ).
– With probability 1 − ω, randomly select abi (t1 + 1) ∈ Ā∗i (t1 ) with uniform
probability.
This is a special case of a so-called “better reply process with finite memory and inertia”. From [You05, Theorem 6.2], the joint actions of this process converge to a Nash
equilibrium with probability 1 in any weakly acyclic game. Therefore, the recurrence
classes of this unperturbed are precisely the set of pure Nash equilibria.

96

The above unperturbed process closely resembles the Baseline Strategy Update
process described in Step 5 of Sample Experimentation Dynamics. The difference
is that the above process uses the true better reply set, whereas Step 5 uses a better
reply set constructed from experimentation over a phase. However, by Claim 5.2.5, for
any probability p̄ < 1, acceptable tolerance level δ, and acceptable exploration rate ,
there exists a minimum exploration phase length m such that for any exploration phase
length m > m, each player’s better response set will contain only and all actions that
are a strict better response with at least probability p̄.
With parameters selected according to Claim 5.2.5, the transitions of the baseline
joint actions in Sample Experimentation Dynamics follow that of the above unperturbed better reply process with probability p̄ arbitrarily close to 1. Since the recurrence classes of the unperturbed process are only Nash equilibria, we can conclude
from Theorem 5.6.1 that as p̄ approaches 1, the probability that the baseline action for
sufficiently large t1 will be a (pure) Nash equilibrium can be made arbitrarily close to
1. By selecting the exploration probability  sufficiently small, we can also conclude
that the joint action during exploration phases, i.e., a(mt1 + t2 ), will also be a Nash
equilibrium with probability arbitrarily close to 1.

5.2.3.2

Noisy Utility Measurements

Suppose that each player receives a noisy measurement of his true utility, i.e.,
Ũi (ai , a−i ) = Ui (ai , a−i ) + νi ,
where νi is an i.i.d. random variable with zero mean. In the regret testing algorithm
with noisy utility measurements, the average utility for action ai during the exploration

97

phase at time t1 is now

Pm

 ai1
t2 =1 I{ai = ǎi (t1 , t2 )}Ũi (ǎ(t1 , t2 )),
n
(t
)
1
i
V̂iai (t1 ) =

U ,
min

nai i (t1 ) > 0;
nai i (t1 ) = 0.

A straightforward modification of the proof of Theorem 5.2.3 leads to the following
theorem.
Theorem 5.2.4. Let G be a finite n-player weakly acyclic game where players’ utilities
are corrupted with a zero mean noise process. If all players use the regret testing
dynamics, then for any
• probability p < 1,
• tolerance level δ ∈ (0, α),
• inertia ω ∈ (0, 1), and
• exploration rate  satisfying min{(α − δ)/4, δ/4, 1 − p} > (1 − (1 − )n ) > 0,
if the exploration phase length m is sufficiently large, then for all sufficiently large
times t > 0, a(t) is a Nash equilibrium of G with at least probability p.

5.2.3.3

Comment on Length and Synchronization of Players’ Exploration Phases

In the proof of Theorem 5.2.3, we assumed that all players’ exploration phases were
synchronized and of the same length. This assumption was used to ensure that the
baseline action of the other players remained constant when a player assessed the performance of a particular action. Because of the players’ inertia this assumption is
unnecessary. The general idea is as follows: a player will repeat his baseline action
regardless of his better response set with positive probability because of his inertia.
Therefore, if all players repeat their baseline action a sufficient number of times, which

98

happens with positive probability, then the joint baseline action would remain constant
long enough for any player to evaluate an accurate better response set for that particular
joint baseline action.

5.3

Influencing Nash Equilibria in Resource Allocation Problems

In this section we will derive an approach for influencing the Nash equilibria of a
resource allocation problem using the idea of marginal cost pricing. We will illustrate
the setup and our approach on a congestion game which is an example of a resource
allocation problem.

5.3.1

Congestion Game with Tolls Setup

We consider a congestion game, as defined in Section 2.3.3, with a player set P =
{P1 , . . . , Pn }, a set of resources R, and a congestion cr : {0, 1, 2, ...} → R for each
resource r ∈ R.
One approach for equilibrium manipulation is to influence drivers’ utilities with
tolls [San02], as introduced in Section 3.4.2. In a congestion game with tolls, a driver’s
utility takes on the form
Ui (a) = −

X

cr (σr (a)) + tr (σr (a)),

r∈Ai

where tr (k) is the toll imposed on route r if there are k users.
In Section 3.4.2, we analyzed the situation in which a global planner was interested
in minimizing the total congestion experienced by all drivers on the network, which
can be evaluated
Tc (a) :=

X

σr (a)cr (σr (a)).

r∈R

Now suppose that the global planner is interested in minimizing a more general

99

measure3 ,
φ(a) :=

X

fr (σr (a))cr (σr (a)).

(5.5)

r∈R

An example of an objective function that fits within this framework and may be practical for general resource allocation problems is
φ(a) =

X

cr (σr (a)).

r∈R

We will now show that there exists a set of tolls, tr (·), such that the potential
function associated with the congestion game with tolls will be aligned with the global
planner’s objective function of the form given in equation (5.5).
Proposition 5.3.1. Consider a congestion game of any network topology. If the imposed tolls are set as
tr (k) = (fr (k) − 1)cr (k) − fr (k − 1)cr (k − 1), ∀k ≥ 1,
then the global planners objective, φc (a) = −φ(a), is a potential function for the
congestion game with tolls.
Proof. Let a1 = {a1i , a−i } and a2 = {a2i , a−i }. We will use the shorthand notation σra

1

to represent σr (a1 ). The change in utility incurred by driver di in changing from route
a2i to route a1i is
Ui (a1 ) − Ui (a2 ) = −
= −

X

X
1
1 
2
2 
cr (σra ) + tr (σra ) +
cr (σra ) + tr (σra ) ,

r∈A1i

r∈A2i

X

X
1
1 
cr (σra ) + tr (σra ) +
r∈A2i \a1i

r∈A1i \a2i
3

2
2 
cr (σra ) + tr (σra ) .

In fact, if cr (σr (a)) 6= 0 for all a, then (5.5) is equivalent to

˜ (σr (a))
.
fr (σr (a)) = fcrr (σ
r (a))

100

P

˜

r∈R fr (σr (a)) where

The change in the total negative congestion from the joint action a2 to a1 is
2
2 
1
1
fr (σra )cr (σra ) − fr (σra )cr (σra ) .

X

φc (a1 ) − φc (a2 ) = −

r∈(a1i ∪a2i )

Since
X

2 
2
1
1
fr (σra )cr (σra ) − fr (σra )cr (σra ) = 0,

r∈(a1i ∩a2i )

the change in the total negative congestion is
X

φc (a1 ) − φc (a2 ) = −

2 
2
1
1
fr (σra )cr (σra ) − fr (σra )cr (σra )

r∈A1i \a2i

X

−

1
1
2
2 
fr (σra )cr (σra ) − fr (σra )cr (σra ) .

r∈A2i \a1i

Expanding the first term, we obtain
X

1
1
2
2 
fr (σra )cr (σra ) − fr (σra )cr (σra )

r∈A1i \a2i

=


1
1
1
1
fr (σra )cr (σra ) − (fr (σra − 1))cr (σra − 1) ,

X
r∈A1i \a2i

=


1
1
1
1
1
fr (σra )cr (σra ) − ((fr (σra ) − 1)cr (σra ) − tr (σra )) ,

X
r∈A1i \a2i

=

1
1 
cr (σra ) + tr (σra ) .

X
r∈A1i \a2i

Therefore,
φc (a1 ) − φc (a2 ) = −

X

X
1
1 
cr (σra ) + tr (σra ) +
r∈A2i \a1i

r∈A1i \a2i

= Ui (a1 ) − Ui (a2 ).

101

2
2 
cr (σra ) + tr (σra ) ,

By implementing the tolling scheme set forth in Proposition 5.3.1, we guarantee
that all action profiles that minimize the global planner’s objective are equilibrium of
the congestion game with tolls.
In the special case that fr (σr (a)) = σr (a), then Proposition 5.3.1 produces the
same tolls as in Proposition 3.4.1

5.4

Illustrative Example – Braess’ Paradox

We will consider a discrete representation of the congestion game setup considered in
Braess’ Paradox [Bra68]. In our setting, there are 1000 vehicles that need to traverse
through the network. The network topology and associated congestion functions are
illustrated in Figure 5.4. Each vehicle can select one of the four possible paths to
traverse across the network.

c(k) = k / 1000

c(k) = 1

c(k) = 0

Start

c(k) = 1

Finish

c(k) = k / 1000

Figure 5.4: Congestion Game Setup – Braess’ Paradox

The reason for using this setup as an illustration of the learning algorithms and
equilibrium manipulation approach developed in this chapter is that the Nash equilibrium of this particular congestion game is easily identifiable. The unique Nash equi-

102

librium is when all vehicles take the route as highlighted in Figure 5.5. At this Nash
equilibrium each vehicle has a utility of 2 and the total congestion is 2000.

c(k) = k / 1000

c(k) = 1

c(k) = 0

c(k) = 1

c(k) = k / 1000

Figure 5.5: Illustration of Nash Equilibrium in Braess’ Paradox.

Since a potential game is weakly acyclic, the payoff based learning dynamics in this
chapter are applicable learning algorithms for this congestion game. In a congestion
game, a payoff based learning algorithms means that drivers have access only to the
actual congestion experienced. Drivers are unaware of the congestion level on any
alternative routes. Figure 5.6 shows the evolution of drivers on routes when using the
Simple Experimentation dynamics. This simulation used an experimentation rate of
 = 0.25%. The colors on the plots are consistent with the colors of each route as
indicated in Figure 5.4. One can observe that the vehicles’ collective behavior does
indeed approach that of the Nash equilibrium.
In this congestion game, it is also easy to verify that this vehicle distribution does
not minimize the total congestion experience by all drivers over the network. The distribution that minimizes the total congestion over the network is when half the vehicles
occupy the top two roads and the other half occupy the bottom two roads. The middle
road (pink) is irrelevant.

103

1000

900

800

Number of Vehicles on Each Road

700

600

500

400

300

200

100

0
0

1000

2000

3000

4000
5000
6000
Iteration Number

7000

8000

9000

10000

Figure 5.6: Braess’ Paradox: Evolution of Number of Vehicles on Each Road Using Simple
Experimentation Dynamics

One can employ the tolling scheme developed in the previous section to locally
influence vehicle behavior to achieve this objective. In this setting, the new cost functions, i.e. congestion plus tolls, are illustrated in Figure 5.7.
Figure 5.8 shows the evolution of drivers on routes when using the Simple Experimentation dynamics. This simulation used an experimentation rate of  = 0.25%.
When using this tolling scheme, the vehicles’ collective behavior approaches the refined Nash equilibrium which now minimizes the total congestion experienced on the
network. The total congestion experienced on the network is now approximately 1500.

There are other tolling schemes that would have resulted in the desired allocation.
One approach is to assign an infinite cost to the middle road, which is equivalent to
removing it from the network. Under this scenario, the unique Nash equilibrium is for
half the vehicles to occupy the top route and half the bottom, which would minimize

104

c(k) = k / 1000 +
(k-1) / 1000

c(k) = 1

c(k) = 0

c(k) = 1

c(k) = k / 1000 +
(k-1) / 1000

Figure 5.7: Braess’ Paradox: Congestion Game Setup with Tolls to Minimize Total Congestion

the total congestion on the network. Therefore, the existence of this extra road, even
though it has zero cost, resulted in the unique Nash equilibrium having a higher total
congestion. This is Braess’ Paradox [Bra68].
The advantage of the tolling scheme set forth in this chapter is that it gives a systematic method for influencing the Nash equilibria of any congestion game. We would
like to highlight that this tolling scheme only guarantees that the action profiles that
maximize the desired objective function are Nash equilibria of the new congestion
game with tolls. However, it does not guarantee the lack of suboptimal Nash equilibria.
In many applications, players may not have access to their true utility, but do have
access to a noisy measurement of their utility. For example, in the traffic setting, this
noisy measurement could be the result of accidents or weather conditions. We will
revisit the original congestion game (without tolls) as illustrated in Figure 5.4. We will
now assume that a driver’s utility measurement takes on the form
Ũi (a) = −

X

cr (σr (a)) + νi ,

r∈Ai

where νi is a random variable with zero mean and variance of 0.1. We will assume that

105

1000

900

800

Number of Vehicles on Each Road

700

600

500

400

300

200

100

0
0

1000

2000

3000

4000
5000
6000
Iteration Number

7000

8000

9000

10000

Figure 5.8: Braess’ Paradox: Evolution of Number of Vehicles on Each Road Using Simple
Experimentation Dynamics with Optimal Tolls

the noise is driver specific rather than road specific.
Figure 5.9 shows a comparison of the evolution of drivers on routes when using the
Simple and Sample Experimentation dynamics. The Simple Experimentation dynamics simulation used an experimentation rate  = 0.25%. The Sample Experimentation
dynamics simulation used an exploration rate  = 0.25%, a tolerance level δ = 0.002,
an exploration phase length m = 500000, and inertia ω = 0.85. As expected, the noisy
utility measurements influenced vehicle behavior more in the Simple Experimentation
dynamics than the Sample Experimentation dynamics.

5.5

Concluding Remarks and Future Work

We have introduced Safe Experimentation dynamics for identical interest games, Simple Experimentation dynamics for weakly acyclic games with noise-free utility mea-

106

Sample Experimentation Dynamics

Simple Experimentation Dynamics
1000

Number of Vehicles on Each Road (Baseline)

1000

800

700

600

500

Number of Vehicles on Each Road (Baseline)

Number of Vehicles on Each Road

Number of Vehicles of Each Road

900

400

300

200

100

900

800

700

600

500

400

300

200

100

0

0
0

1000

2000

3000

4000

5000

6000

7000

8000

9000

10000

Iteration Number
Iteration
Number

0

10

20

30
Iteration Number

40

50

60

Exploration Phase Time

Figure 5.9: Braess’ Paradox: Comparison of Evolution of Number of Vehicles on Each Road
Using Simple Experimentation Dynamics and Sample Experimentation Dynamics (baseline)
with Noisy Utility Measurements

surements, and Sample Experimentation dynamics for weakly acyclic games with
noisy utility measurements. For all three settings, we have shown that for sufficiently
large times, the joint action taken by players will constitute a Nash equilibrium. Furthermore, we have shown how to guarantee that a collective objective in a congestion
game is a (non-unique) Nash equilibrium.
Our motivation has been that in many engineered systems, the functional forms of
utility functions are not available, and so players must adjust their strategies through an
adaptive process using only payoff measurements. In the dynamic processes defined
here, there is no explicit cooperation or communication between players. One the one
hand, this lack of explicit coordination offers an element of robustness to a variety of
uncertainties in the strategy adjustment processes. Nonetheless, an interesting future
direction would be to investigate to what degree explicit coordination through limited
communications could be beneficial.

107

5.6

Appendix to Chapter 5

5.6.1

Background on Resistance Trees

For a detailed review of the theory of resistance trees, please see [You93]. Let P 0
denote the probability transition matrix for a finite state Markov chain over the state
space Z. Consider a “perturbed” process such that the size of the perturbations can
be indexed by a scalar  > 0, and let P  be the associated transition probability matrix. The process P  is called a regular perturbed Markov process if P  is ergodic
for all sufficiently small  > 0 and P  approaches P 0 at an exponentially smooth rate
[You93]. Specifically, the latter condition means that ∀z, z 0 ∈ Z,

0
lim Pzz
0 = Pzz 0 ,

→0+

and

Pzz
0 > 0 for some  > 0 ⇒ 0 < lim
+
→0


Pzz
0

r(z→z0 )

< ∞,

for some nonnegative real number r(z → z 0 ), which is called the resistance of the
0
0
transition z → z 0 . (Note in particular that if Pzz
0 > 0 then r(z → z ) = 0.)

Let the recurrence classes of P 0 be denoted by E1 , E2 , ..., EN . For each pair of
distinct recurrence classes Ei and Ej , i 6= j, an ij-path is defined to be a sequence
of distinct states ζ = (z1 → z2 → ... → zn ) such that z1 ∈ Ei and zn ∈ Ej . The
resistance of this path is the sum of the resistances of its edges, that is, r(ζ) = r(z1 →
z2 ) + r(z2 → z3 ) + ... + r(zn−1 → zn ). Let ρij = min r(ζ) be the least resistance
over all ij-paths ζ. Note that ρij must be positive for all distinct i and j, because there
exists no path of zero resistance between distinct recurrence classes.
Now construct a complete directed graph with N vertices, one for each recurrence
class. The vertex corresponding to class Ej will be called j. The weight on the directed
edge i → j is ρij . A tree, T , rooted at vertex j, or j-tree, is a set of N −1 directed edges

108

such that, from every vertex different from j, there is a unique directed path in the tree
to j. The resistance of a rooted tree, T , is the sum of the resistances ρij on the N − 1
edges that compose it. The stochastic potential, γj , of the recurrence class Ej is defined
to be the minimum resistance over all trees rooted at j. The following theorem gives a
simple criterion for determining the stochastically stable states ([You93], Theorem 4).
Theorem 5.6.1. Let P  be a regular perturbed Markov process, and for each  > 0 let
µ be the unique stationary distribution of P  . Then lim→0 µ exists and the limiting
distribution µ0 is a stationary distribution of P 0 . The stochastically stable states (i.e.,
the support of µ0 ) are precisely those states contained in the recurrence classes with
minimum stochastic potential.

109

CHAPTER 6
Connections Between Cooperative Control and
Potential Games
In this chapter, we present a view of cooperative control using the language of learning in games. We review the game theoretic concepts of potential games and weakly
acyclic games and demonstrate how several cooperative control problems such as consensus and dynamic sensor coverage can be formulated in these settings. Motivated
by this connection, we build upon game theoretic concepts to better accommodate a
broader class of cooperative control problems. In particular, we extend existing learning algorithms to accommodate restricted action sets caused by limitations in agent
capabilities. Furthermore, we also introduce a new class of games, called sometimes
weakly acyclic games, for time-varying objective functions and action sets, and provide distributed algorithms for convergence to an equilibrium. Lastly, we illustrate the
potential benefits of this connection on several cooperative control problems. For the
consensus problem, we demonstrate that consensus can be reached even in an environment with non-convex obstructions. For the functional consensus problem, we demonstrate an approach that will allow agents to reach consensus on a specific consensus
point. For the dynamic sensor coverage problem, we demonstrate how autonomous
sensors can distribute themselves using only local information in such a way as to
maximize the probability of detecting an event over a given mission space. Lastly,
we demonstrate how the popular mathematical game of Sudoku can be modeled as a

110

potential game and solved using the learning algorithms discussed in this chapter.

6.1

Introduction

Our goals in this chapter are to establish a relationship between cooperative control
problems, such as the consensus problem, and game theoretic methods, and to demonstrate the effectiveness of utilizing game theoretic approaches for controlling multiagent systems. The results presented here are of independent interest in terms of their
applicability to a large class of games. However, we will focus on the consensus problem as the main illustration of the approach.
We consider a discrete time version of the consensus problem initiated in [TBA86]
in which a group of players P = {P1 , . . . , Pn } seek to come to an agreement, or
consensus, upon a common scalar value1 by repeatedly interacting with one another.
By reaching consensus, we mean converging to the agreement space characterized by
a1 = a2 = · · · = an ,
where ai is referred to as the state of player Pi . Several papers study different interaction models and analyze the conditions under whether these interactions lead to
consensus [BHO05, XB04, XB05, OM03, OFM07, Mor04, JLM03, KBS06].
A well studied protocol, referred to here as the “consensus algorithm”, can be
described as follows. At each time step t ∈ {0, 1, . . . }, each player Pi is allowed to
interact with a group of other players, who are referred to as the neighbors of player Pi
and denoted as Ni (t). During an interaction, each player Pi is informed of the current
(or possibly delayed) state of all his neighbors. Player Pi then updates his state by
forming a convex combination of his state along with the state of all his neighbors.
1

The forthcoming results will hold for multi-dimensional consensus as well.

111

The consensus algorithm takes on the general form
ai (t + 1) =

X

ωij (t)aj (t),

(6.1)

Pj ∈Ni (t)

where ωij (t) is the relative weight that player Pi places on the state of player Pj at
time t. The interaction topology is described in terms of a time varying directed graph
G(V, E(t)) with the set of nodes V = P and the set of edges E(t) ⊂ P × P at time t.
The set of edges is directly related to the neighbor sets as follows: (Pi , Pj ) ∈ E(t) if
and only if Pj ∈ Ni (t). We will refer to G(V, E(t)) as the interaction graph at time t.
There has been extensive research centered on understanding the conditions necessary for guaranteeing the convergence of all states, i.e. limt→∞ ai (t) → a∗ , for
all players Pi ∈ P. The convergence properties of the consensus algorithm have
been studied under several interaction models encompassing delays in information exchange, connectivity issues, varying topologies and noisy measurements.
Surprisingly, there has been relatively little research that links cooperative control
problems to a branch of the learning in games literature [You98] that emphasizes coordination games. The goal of this chapter is to better establish this link and to develop
new algorithms for broader classes of cooperative control problems as well as games.
In Section 6.2 we establish a connection between cooperative control problems
and potential games. In Section 6.3 we model the consensus problem as a potential
game and present suitable learning algorithms that guarantee that players will come
to a consensus even in an environment filled with non-convex obstructions. In Section 6.4 we introduce a new class of games called sometimes weakly acyclic games,
which generalize potential games, and present simple learning dynamics with desirable convergence properties. In Section 6.5 we show that the consensus problem can
be modeled as a sometimes weakly acyclic game. In Section 6.6 we develop learning
algorithms that can accommodate group based decisions. In Section 6.7 we model the

112

functional consensus problem as a potential game with group based decisions. In Section 6.8 we illustrate the connection between cooperative control and potential games
on the dynamic sensor allocation problem and also the mathematical puzzle of Sudoku.
Section 6.9 presents some final remarks.

6.2

Cooperative Control Problems and Potential Games

Cooperative control problems entail several autonomous players seeking to collectively accomplish a global objective. The consensus problem is one example of a
cooperative control problem, where the global objective is for all players to reach consensus upon a given state. The challenge in cooperative control problems is designing
local control laws and/or local objective functions for each of the individual players so
that collectively they accomplish the desired global objective.
One approach for cooperative control problems is to assign each individual player
a fixed protocol or policy. This protocol specifies precisely what each player should
do under any environmental condition. The consensus algorithm set forth in Equation
(6.1) is an example of such a policy based approach. One challenge in this approach
is to incorporate dynamic or evolving constraints on player policies. For example,
suppose a global planner desires a group of autonomous players to physically converge to a central location in an environment containing obstructions. The standard
consensus algorithm may not be applicable to this problem since limitations in control
capabilities caused by environmental obstructions are not considered. Variations of the
consensus algorithm could possibly be designed to accommodate obstructions, but the
analysis and control design would be more challenging.
An alternative, game theoretic approach to cooperative control problems, and our
main interest in this chapter, is to assign each individual player a local objective func-

113

tion. In this setting, each player Pi ∈ P is assigned an action set Ai and a local
Q
objective function Ui : A → R, where A = Pi ∈P Ai is the set of joint actions. An
example of an objective function that will be studied in the following section is
X
Ui (ai , a−i ) := −
kai − aj k,
Pj ∈Ni

where k · k is any norm, Ni is the neighbor set of player Pi , and
a−i = {a1 , . . . , ai−i , ai+1 , . . . , an } denotes the collection of actions of players other
than player Pi . With this notation, we will frequently express the joint action a as
(ai , a−i ).
We are interested in analyzing the long term behavior when players are repeatedly
allowed to interact with one another in a competitive environment where each player
seeks to selfishly maximize his own objective function. These interactions will be
modeled as a repeated game, in which a one stage game is repeated each time step t ∈
{0, 1, 2, . . . }. At every time step t > 0, each player Pi ∈ P selects an action ai ∈ Ai
seeking to myopically maximize his expected utility. Since a player’s utility may be
adversely affected by the actions of other players, the player can use his observations
from the games played at times {0, 1, . . . , t − 1} to develop a behavioral model of the
other players.
At any time t > 0, the learning dynamics specify how any player Pi processes past
observations from the interactions at times {0, 1, . . . , t − 1} to generate a model of the
behavior of the other players. The learning dynamics that will be used throughout this
chapter are referred to as single stage memory dynamics which have a structural form
similar to that of the consensus algorithm; namely, that the decision of any player Pi
at time t is made using only observations from the game played at time t − 1. The
learning dynamics need not be restricted to single stage memory. A follow up study
could analyze the benefit of using additional memory in learning dynamics for the
consensus problem.

114

The challenge of the control design for a game theoretic approach lies in designing the objective functions and the learning dynamics such that, when players selfishly pursue their own objectives, they also collectively accomplish the objective of
the global planner. Suppose that the objective of the global planner is captured by a
potential function φ : A → R. In any successful multi-agent system each player’s
objective function should be appropriately “aligned” with the objective of the global
planner. This notion of utility alignment in multi-agent systems has a strong connection to potential games [MS96b]. For convenience, we will restate the definition of
potential games originally defined in Section 2.3.2.
Definition 6.2.1 (Potential Games). Player action sets {Ai }ni=1 together with player
objective functions {Ui : A → R}ni=1 constitute a potential game if, for some potential
function φ : A → R,
Ui (a00i , a−i ) − Ui (a0i , a−i ) = φ(a00i , a−i ) − φ(a0i , a−i ),
for every player Pi ∈ P, for every a0i , a00i ∈ Ai , and for every a−i ∈ ×j6=i Aj .
A potential game, as defined above, requires perfect alignment between the global
objective and the players’ local objective functions, meaning that if a player unilaterally changed his action, the change in his objective function would be equal to the
change in the potential function. There are weaker notions of potential games, called
weakly acyclic games, which will be discussed later. The connection between cooperative control problems and potential games is important because learning algorithms for potential games have been studied extensively in the game theory literature
[MS96a, MS96b, MS97, MAS07b, MAS05]. Accordingly, if it is shown that a cooperative control problem can be modeled as a potential game, established learning
algorithms with guaranteed asymptotic results could be used to tackle the cooperative
control problem at hand.

115

In the following section we will illustrate this opportunity by showing that the
consensus problem can be modeled as a potential game by defining players’ utilities
appropriately.

6.3

Consensus Modeled as a Potential Game

In this section we will formulate the consensus problem as a potential game. First,
we establish a global objective function that captures the notion of consensus. Next,
we show that local objective functions can be assigned to each player so that the resulting game is in fact a potential game. Finally, we present a learning algorithm that
guarantees consensus even in an environment containing non-convex obstructions.
It turns out that the potential game formulation of the consensus problem discussed
in this section requires the interaction graph to be time-invariant and undirected. In
Section 6.5 we relax these requirements by formulating the consensus problem as a
sometimes weakly acyclic game.

6.3.1

Setup: Consensus Problem with a Time-Invariant and Undirected Interaction Graph

Consider a consensus problem with n-player set P where each player Pi ∈ P has a
finite action set Ai . A player’s action set could represent the finite set of locations that
a player could select.
We will consider the following potential function for the consensus problem
φ(a) := −

X X kai − aj k
Pi ∈P Pj ∈Ni

2

,

(6.2)

where Ni ⊂ P is player Pi ’s time-invariant neighbor set. In the case where the interac-

116

tion graph induced by the neighbor sets {Ni }ni=1 is connected2 , the potential function
above achieves the value of 0 if and only if the action profile a ∈ A constitutes a
consensus, i.e.,
φ(a) = 0 ⇔ a1 = · · · = an .
The goal is to assign each player an objective function that it is perfectly aligned
with the global objective in (6.2). One approach would be to assign each player the
following objective function:
Ui (a) = φ(a).
This assignment would require each player to observe the decision of all players in
order to evaluate his payoff for a particular action choice, which may be infeasible. An
alternative approach would be to assign each player an objective function that captures
the player’s marginal contribution to the potential function. For the consensus problem,
this translates to each player being assigned the objective function
X

Ui (ai , a−i ) = −

kai − aj k.

(6.3)

Pj ∈Ni

Now, each player’s objective function is only dependent on the actions of his neighbors. An objective function of this form is referred to as Wonderful Life Utility; see
[AMS07, WT99]. It is known that assigning each agent a Wonderful Life Utility leads
to a potential game [AMS07, WT99]; however, we will explicitly show this for the
consensus problem in the following claim.
Claim 6.3.1. Player objective functions (6.3) constitute a potential game with the potential function (6.2) provided that the time-invariant interaction graph induced by the
neighbor sets {Ni }ni=1 is undirected, i.e.,
Pj ∈ Ni ⇔ Pi ∈ Nj .
2

A graph is connected if there exists a path from any node to any other node.

117

Proof. Since the interaction graph is time-invariant and undirected, the potential function can be expressed as

φ(a) = −

X

kai − aj k −

Pj ∈Ni

X

X

Pj 6=Pi Pk ∈Nj \Pi

kaj − ak k
.
2

The change in objective of player Pi by switching from action a1i to action a2i provided
that all other players collectively play a−i is

Ui (a2i , a−i ) − Ui (a1i , a−i ) =

X

−ka2i − aj k + ka1i − aj k,

Pj ∈Ni

= φ(a2i , a−i ) − φ(a1i , a−i ).

Note that the above claim does not require the interaction graph to be connected. There
may exist other potential functions and subsequent player objective functions that can
accommodate more general setups. For a detailed discussion on possible player objective functions derived from a given potential function, see [AMS07].
We now assume that the above game is repeatedly played at discrete time steps
t ∈ {0, 1, 2, . . . }. We are interested in determining the limiting behavior of the players,
in particular whether or not they reach a consensus, under various interaction models.
Since the consensus problem is modeled as a potential game, there are a large number of learning algorithms available with guaranteed results [You98, You05, AMS07,
MS96b, MAS07b, MAS05]. Most of the learning algorithms for potential games guarantee that the player behavior converges to a Nash equilibrium.
It is straightforward to see that any consensus point is a Nash equilibrium of the
game characterized by the player objective functions (6.3). This is because a consensus

118

point maximizes the potential function as well as the player objective functions (6.3).
However, the converse statement is not true. Let A∗ denote the set of Nash equilibria
and Ac denote the set of consensus points. We know that Ac ⊂ A∗ where the inclusion
can be proper. In other words, a Nash equilibrium, say a∗ ∈ A∗ , can be suboptimal,
i.e., φ(a∗ ) < 0, and hence fail to be a consensus point.

6.3.2

A Learning Algorithm for Potential Games with Suboptimal Nash Equilibria

Before stating the learning algorithm, we start with some notation. Let the strategy
of player Pi at time t be denoted by the probability distribution pi (t) ∈ ∆(Ai ) where
∆(Ai ) denotes the set of probability distributions over the set Ai . Using this strategy,
player Pi randomly selects an action from Ai at time t according to pi (t).
Consider the following learning algorithm known as spatial adaptive play (SAP)
[You98]. At each time t > 0, one player Pi ∈ P is randomly chosen (with equal
probability for each player) and allowed to update his action. All other players must
repeat their actions, i.e. a−i (t) = a−i (t − 1). At time t, the updating player Pi
randomly selects an action from Ai according to his strategy pi (t) ∈ ∆(Ai ) where the
ai −th component pai i (t) of his strategy is given as
exp{β Ui (ai , a−i (t − 1))}
,
āi ∈Ai exp{β Ui (āi , a−i (t − 1))}

pai i (t) = P

for some exploration parameter β ≥ 0. The constant β determines how likely player Pi
is to select a suboptimal action. If β = 0, player Pi will select any action ai ∈ Ai with
equal probability. As β → ∞, player Pi will select an action from his best response
set
{ai ∈ Ai : Ui (ai , a−i (t − 1)) = max
Ui (a0i , a−i (t − 1))}
0
ai ∈Ai

with arbitrarily high probability.

119

In a repeated potential game in which all players adhere to SAP, the stationary
distribution µ ∈ ∆(A) of the joint action profiles is given in [You98] as
exp{β φ(a)}
.
ā∈A exp{β φ(ā)}

µ(a) = P

One can interpret the stationary distribution µ as follows: for sufficiently large times
t > 0, µ(a) equals the probability that a(t) = a. As β ↑ ∞, all the weight of the
stationary distribution µ is on the joint actions that maximize the potential function.
In the potential game formulation of the consensus problem, the joint actions that
maximize the potential function (6.2) are precisely the consensus points provided that
the interaction graph is connected. Therefore, if all players update their actions using
the learning algorithm SAP with sufficiently large β, then the players will reach a
consensus asymptotically with arbitrarily high probability.

6.3.3

A Learning Algorithm for Potential Games with Suboptimal Nash Equilibria and Restricted Action Sets

One issue with the applicability of the learning algorithm SAP for the consensus problem is that it permits any player to select any action in his action set. Because of player
mobility limitations, this may not be possible. For example, a player may only be able
to move to a position within a fixed radius of his current position. Therefore, we seek
to modify SAP by conditioning a player’s action set on his previous action. Let a(t−1)
be the joint action at time t − 1. With restricted action sets, the set of actions available
to player Pi at time t is a function of his action at time t − 1 and will be denoted as
Ri (ai (t − 1)) ⊂ Ai . We will adopt the convention that ai ∈ Ri (ai ) for any action
ai ∈ Ai , i.e., a player is always allowed to stay with his previous action.
We will introduce a variant of SAP called binary Restrictive Spatial Adaptive Play
(RSAP) to accommodate the notion of restricted action sets. RSAP can be described
as follows: At each time step t > 0, one player Pi ∈ P is randomly chosen (with equal

120

probability for each player) and allowed to update his action. All other players must
repeat their actions, i.e. a−i (t) = a−i (t − 1). At time t, the updating player Pi selects
one trial action âi randomly from his allowable set Ri (ai (t − 1)) with the following
probability:
• Pr [âi = ai ] = N1i for any ai ∈ Ri (ai (t − 1)) \ ai (t − 1),
• Pr [âi = ai (t − 1)] = 1 − |Ri (ai (t−1))|−1
,
Ni
where Ni denotes the maximum number of actions in any restricted action set for
player Pi , i.e., Ni := maxai ∈Ai |Ri (ai )|. After player Pi selects a trial action âi , he
chooses his action at time t as follows:
exp{β Ui (âi , a−i (t − 1))}
,
exp{β Ui (âi , a−i (t − 1))} + exp{β Ui (a(t − 1))}
exp{β Ui (a(t − 1))}
Pr [ai (t) = ai (t − 1)] =
,
exp{β Ui (âi , a−i (t − 1))} + exp{β Ui (a(t − 1))}
Pr [ai (t) = âi ] =

where β ≥ 0 is an exploration parameter. Note that if âi is selected as ai (t − 1) then
Pr [ai (t) = ai (t − 1)] = 1.
We make the following assumptions regarding the restricted action sets.

Assumption 6.3.1 (Reversibility). For any player Pi ∈ P and any action pair a1i , a2i ∈
Ai ,
a2i ∈ Ri (a1i ) ⇔ a1i ∈ Ri (a2i ).

Assumption 6.3.2 (Feasibility). For any player Pi ∈ P and any action pair a0i , ani ∈
Ai , there exists a sequence of actions a0i → a1i → · · · → ani satisfying aki ∈ Ri (ak−1
)
i
for all k ∈ {1, 2, . . . , n}.
Theorem 6.3.1. Consider a finite n-player potential game with potential function φ(·).
If the restricted action sets satisfy Assumptions 6.3.1 and 6.3.2, then RSAP induces

121

a Markov process over the state space A where the unique stationary distribution
µ ∈ ∆(A) is given as
exp{β φ(a)}
, for any a ∈ A.
ā∈A exp{β φ(ā)}

µ(a) = P

(6.4)

Proof. The proof follows along the lines of the proof of Theorem 6.2 in [You98]. By
Assumptions 6.3.1 and 6.3.2 we know that the Markov process induced by RSAP is
irreducible and aperiodic; therefore, the process has a unique stationary distribution.
Below, we show that this unique distribution must be (6.4) by verifying that the distribution (6.4) satisfies the detailed balanced equations
µ(a)Pab = µ(b)Pba ,
for any a, b ∈ A, where
Pab := Pr [a(t) = b|a(t − 1) = a] .
Note that the only nontrivial case is the one where a and b differ by exactly one player
Pi , that is, a−i = b−i but ai 6= bi where ai ∈ Ri (bi ) which also implies that bi ∈ Ri (ai ).
Since player Pi has probability 1/n of being chosen in any given period and any trial
action bi ∈ Ri (ai ), bi 6= ai , has probability of 1/Ni of being chosen, it follows that

 

exp{β φ(a)}
exp{β Ui (b)}
µ(a)Pab = P
× (1/n)(1/Ni )
.
exp{β Ui (a)} + exp{β Ui (b)}
z∈A exp{β φ(z)}
Letting

λ=

1
P
z∈A exp{β φ(z)}




×


(1/n)(1/Ni )
,
exp{β Ui (a)} + exp{β Ui (b)}

we obtain
µ(a)Pab = λ exp{βφ(a) + βUi (b)}.
Since Ui (b) − Ui (a) = φ(b) − φ(a), we have
µ(a)Pab = λ exp{βφ(b) + βUi (a)},

122

which leads us to
µ(a)Pab = µ(b)Pba .

Note that if all players adhere to the learning dynamics RSAP in a consensus problem where the interaction graph is time-invariant and undirected, the restricted action
sets satisfy Assumptions 6.3.1 and 6.3.2, and players are assigned the utilities (6.3),
then, at sufficiently large times t, the players’ collective behavior will maximize the
potential function (6.2) with arbitrarily high probability provided that β is sufficiently
large. Furthermore, if the interaction graph is connected and consensus is possible,
meaning (A1 ∩ A2 ∩ · · · ∩ An ) 6= ∅, then, at sufficiently large times t > 0, the
players’ actions will constitute a consensus with arbitrarily high probability even in an
environment filled with non-convex obstructions.

6.3.4

Example: Consensus in an Environment with Non-convex Obstructions

Consider the 2-D consensus problem with player set P = {P1 , P2 , P3 , P4 }. Each
player Pi has an action set Ai = {1, 2, . . . , 10} × {1, 2, .., 10} as illustrated in Figure
6.1. The arrows represent the time-invariant and undirected edges of the connected
interaction graph. The restricted action sets are highlighted for players P2 and P4 . At
any given time, any player can have at most 9 possible actions; therefore, Ni = 9 for
all players Pi ∈ P.
We simulated RSAP on the consensus problem with the interaction graph, environmental obstruction, and the initial conditions shown in Figure 6.1. We increase the
exploration parameter β as t/200 during player interactions. The complete action path
of all players reaching a consensus is shown in Figure 6.2.

123

10

9

Player 3

8

7

Player 2

Obstruction
6

5

Player 1
4

3

2

Restricted
Action Sets

1

Player 4
0
0

1

2

3

4

5

6

7

8

9

10

Figure 6.1: Example: Setup of a Consensus Problem with Restricted Action Sets and
Non-convex Environmental Obstructions.

6.4

Weakly Acyclic and Sometimes Weakly Acyclic Games

In potential games, players’ objective functions must be perfectly aligned with the potential of the game. In the potential game formulation of the consensus problem, this
alignment condition required that the interaction graph be time-invariant and undirected. In this section we will seek to relax this alignment requirement by allowing
player objective functions to be “somewhat” aligned with the potential of the game.
We will review a weaker form of potential games called weakly acyclic games and
introduce a new class of games called sometimes weakly acyclic games. We will also
present simple learning dynamics that guarantee convergence to a universal Nash equilibrium, to be defined later, in any sometimes weakly acyclic game.

124

10
9
8
7
6
5
4
3
2
1
0

Consensus Reached

0

1

2

3

4

5

6

7

8

9

10

Figure 6.2: Example: Evolution of the Action Path in the Consensus Problem with Restricted
Action Sets and Non-convex Environmental Obstructions.

6.4.1

Weakly Acyclic Games

Recall the definition of a weakly acyclic game from Section 2.3.4. A game is weakly
acyclic if, for any a ∈ A, there exists a better reply path starting at a and ending at
some Nash equilibrium [You98, You05].
The above definition does not clearly identify the similarities between potential
games and weakly acyclic games. Furthermore, using this definition to show that a
given game G, i.e., the players, objective functions, and action sets, is weakly acyclic
would be problematic. With these issues in mind, we will now derive an equivalent
definition for weakly acyclic games that utilizes potential functions.
Lemma 6.4.1. A game is weakly acyclic if and only if there exists a potential function
φ : A → R such that for any action a ∈ A that is not a Nash equilibrium, there

125

exists a player Pi ∈ P with an action a∗i ∈ Ai such that Ui (a∗i , a−i ) > Ui (ai , a−i ) and
φ(a∗i , a−i ) > φ(ai , a−i ).
Proof. (⇐) Select any action a0 ∈ A. If a0 is not a Nash equilibrium, there exists a
player Pi ∈ P with an action a∗i ∈ Ai such that Ui (a1 ) > Ui (a0 ) and φ(a1 ) > φ(a0 )
where a1 = (a∗i , a0−i ).
Repeat this process and construct a path a0 , a1 , . . . , an until it can no longer be
extended. Note first that such a path cannot cycle back on itself, because φ is strictly
increasing along the path. Since A is finite, the path cannot be extended indefinitely.
Hence, the last element in this path must be a Nash equilibrium.
(⇒) We will construct a potential function φ : A → R recursively. Select any
action a0 ∈ A. Since the game is weakly acyclic, there exists a better reply path
a0 , a1 , . . . , an where an is a Nash equilibrium. Let A0 = {a0 , a1 , . . . , an }. Define the
(finite) potential function φ over the set A0 satisfying the following conditions:
φ(a0 ) < φ(a1 ) < · · · < φ(an ).
Now select any action ã0 ∈ A \ A0 . There exists a better reply path ã0 , ã1 , . . . , ãm
where ãm is a Nash equilibrium. Let A1 = {ã0 , ã1 , . . . , ãm }. If A1 ∩ A0 = ∅ then
define the potential function φ over the set A1 satisfying the following conditions:
φ(ã0 ) < φ(ã1 ) < · · · < φ(ãm ).
If A1 ∩ A0 6= ∅, then let k ∗ = min{k ∈ {1, 2, . . . , m} : ãk ∈ A0 }. Define the potential
∗

function φ over the truncated (redefined) set A1 = {ã0 , ã1 , . . . , ãk −1 } satisfying the
following conditions:
∗

φ(ã0 ) < φ(ã1 ) < · · · < φ(ãk ).
Now select any action â0 ∈ A \ (A0 ∪ A1 ) and repeat until no such action exists.

126

The construction of the potential function φ guarantees that for any action a ∈ A
that is not a Nash equilibrium, there exists a player Pi ∈ P with an action a∗i ∈ Ai
such that Ui (a∗i , a−i ) > Ui (ai , a−i ) and φ(a∗i , a−i ) > φ(ai , a−i ).

6.4.2

Learning Dynamics for Weakly Acyclic Games

We will consider the better reply with inertia dynamics for weakly acyclic games analyzed in [You93, You05]. Before stating the learning dynamics, we define a player’s
strict better reply set for any action profile a0 ∈ A as
Bi (a0 ) := {ai ∈ Ai : Ui (ai , a0−i ) > Ui (a0 )}.
The better reply with inertia dynamics can be described as follows. At each time
t > 0, each player Pi presumes that all other players will continue to play their previous actions a−i (t − 1). Under this presumption, each player Pi ∈ P selects an action
according to the following strategy at time t:
Bi (a(t − 1)) = ∅ ⇒ ai (t) = ai (t − 1),

 Pr [ai (t) = ai (t − 1)] = α(t),
Bi (a(t − 1)) 6= ∅ ⇒
 Pr [a (t) = a∗ ] = 1−α(t) ,
i

i

|Bi (a(t−1))|

for any action a∗i ∈ Bi (a(t−1)) where α(t) ∈ (0, 1) is referred to as the player’s inertia
at time t. According to these rules, player Pi will stay with the previous action ai (t−1)
with probability α(t) even when there is a perceived opportunity for improvement. We
make the following standing assumption on the players’ willingness to optimize.
Assumption 6.4.1. There exist constants ε and ε̄ such that for all time t ≥ 0 and for
all players Pi ∈ P,
0 < ε < αi (t) < ε̄ < 1.
This assumption implies that players are always willing to optimize with some
nonzero inertia.

127

If all players adhere to the better reply with inertia dynamics satisfying Assumption 6.4.1, then the joint action profiles will converge to a Nash equilibrium almost
surely in any weakly acyclic game [You93, You05].

6.4.3

Sometimes Weakly Acyclic Games

In the potential game formulation of the consensus problem, each player was assigned
a time-invariant objective function of the form (6.3). However, in the case of a timevarying interaction topology, we would like to allow player objective functions to be
time-varying. In this framework, each player Pi is now assigned a local objective
function Ui : A × {0, 1, 2, . . . } → R. We will denote the objective function of player
Pi at time t as Ui (a(t), t) where a(t) is the action profile at time t.
We will call an action profile a∗ a universal Nash equilibrium if
Ui (a∗ , t) = max Ui (ai , a∗−i , t)
ai ∈Ai

for all times t ≥ 0.
We will call a game sometimes weakly acyclic if there exists a potential function
φ : A → R and a finite time constant T such that for any time t0 > 0 and any action
profile a0 that is not a universal Nash equilibrium, there exists a time t1 ∈ [t0 , t0 + T ],
a player Pi ∈ P, and an action a∗i ∈ Ai such that Ui (a∗i , a0−i , t1 ) > Ui (a0 , t1 ) and
φ(a∗i , a0−i ) > φ(a0 ).
Note that a sometimes weakly acyclic game has at least one universal Nash equilibrium: namely, an action profile that maximizes the potential function phi.

6.4.4

Learning Dynamics for Sometimes Weakly Acyclic Games

We will consider the better reply with inertia dynamics for games involving timevarying objective functions. Before stating the learning dynamics, we redefine a player’s

128

strict better reply set for any action profile a0 ∈ A and time t > 0 as
Bi (a0 , t) := {ai ∈ Ai : Ui (ai , a0−i , t) > Ui (a0 , t)}.
The better reply with inertia dynamics can be described as follows. At each time t > 0,
each player Pi presumes that all other players will continue to play their previous
actions a−i (t − 1). Under this presumption, each player Pi ∈ P selects an action
according to the following strategy at time t:
Bi (a(t − 1), t) = ∅ ⇒ ai (t) = ai (t − 1),

 Pr [ai (t) = ai (t − 1)] = α(t),
Bi (a(t − 1), t) 6= ∅ ⇒
 Pr [a (t) = a∗ ] = (1−α(t)) ,
i

i

|Bi (a(t−1),t)|

for any action a∗i ∈ Bi (a(t − 1), t) where α(t) ∈ (0, 1) is the player’s inertia at time t.
Theorem 6.4.1. Consider an n-player sometimes weakly acyclic game with finite action sets. If all players adhere to the better reply with inertia dynamics satisfying
Assumption 6.4.1, then the joint action profiles will converge to a universal Nash equilibrium almost surely.
Proof. Let φ : A → R and T be the potential function and time constant for the
sometimes weakly acyclic game. Let a(t0 ) = a0 be the action profile at time t0 . If
a0 is a universal Nash equilibrium, then a(t) = a0 for all times t ≥ t0 and we are
done. Otherwise, there exists a time t1 satisfying (t0 + T ) ≥ t1 > t0 , a player Pi ∈ P,
and an action a∗i ∈ Ai such that Ui (a∗i , a0−i , t1 ) > Ui (a0 , t1 ) and φ(a∗i , a0−i ) > φ(a0 ).
Because of players’ inertia, the action a1 = (a∗i , a0−i ) will be played at time t1 with at
) nT
least probability n−1 (1−¯
 .
|A|

One can repeat this argument to show that for any time t0 > 0 and any action
profile a(t0 ) there exists a joint action a∗ such that
Pr [a(t) = a∗ , ∀t ≥ t∗ ] ≥ ∗

129

where
t∗ = t0 + T |A|,

|A|
¯) n T
n−1 (1 − 
∗
 =


.
|A|

6.5

Consensus Modeled as a Sometimes Weakly Acyclic Game

Two main problems arose in the potential game formulation of the consensus problem.
The first problem was that a Nash equilibrium was not necessarily a consensus point
even when the interaction graph was connected and the environment was obstruction
free. Therefore, we needed to employ a stochastic learning algorithm like SAP or
RSAP to guarantee that the collective behavior of the players would be a consensus
point with arbitrarily high probability. SAP or RSAP led to consensus by introducing
noise into the decision making process, meaning that a player would occasionally make
a suboptimal choice. The second problem was that the interaction graph needed to be
time-invariant, undirected, and connected in order to guarantee consensus.
In this section, we will illustrate that by modeling the consensus problem as a
sometimes weakly acyclic game one can effectively alleviate both problems. For
brevity, we will show that the 1-dimensional consensus problem with appropriately
designed player objective functions is a sometimes weakly acyclic game. However,
one can easily extend this to the multi-dimensional case.

130

6.5.1

Setup: Consensus Problem with a Time-Varying and Directed Interaction
Graph

Consider a consensus problem with a n-player set P and a time-varying and directed
interaction graph. Each player has a finite action set Ai ⊂ R and without loss of
generalities, we will assume that A1 = A2 = · · · = An . Each player Pi ∈ P is
assigned an objective function Ui : A × {0, 1, 2, ...} → R. We make the following
standard assumption on players’ neighbor sets.
Assumption 6.5.1. Players’ neighbor sets satisfy
Pi ∈ Ni (t), ∀Pi ∈ P, t > 0.
Before introducing the player objective functions, we define the following measure
D(a, P 0 ) :=

max (ai − aj ),

Pi ,Pj ∈P 0

(6.5)

where P 0 ⊆ P, and extreme player sets
P u (a) := {Pi ∈ P : ai = max aj },
Pj ∈P

l

P (a) := {Pi ∈ P : ai = min aj },
Pj ∈P

u

n(a) := min{|P (a)|, |P l (a)|}.
We also define the constant δA > 0 as follows. For any a1 , a2 ∈ A and any player sets
P 1 , P 2 ⊂ P such that D(a1 , P 1 ) 6= D(a2 , P 2 ), the following inequality is satisfied:
|D(a1 , P 1 ) − D(a2 , P 2 )| > δA .
Consider the following potential function φ : A → R
φ(a) = −D(a, P) + δA (1 − n(a)/n).

131

(6.6)

Note that the potential function is a non-positive function that achieves the value of
0 if and only if the action profile constitutes a consensus. Furthermore, note that the
potential function is independent of the interaction topology.
Rather than specifying a particular objective functions as in (6.3), we will introduce
a class of admissible objective functions. To that end, we define the set of reasonable
actions for player Pi at time t given any action profile a0 ∈ A as
Si (a0 , t) := {ai ∈ Ai : max a0j ≥ ai ≥ min a0k }.
Pj ∈Ni (t)

Pk ∈Ni (t)

Note that
ai ∈ Si (a0 , t) ⇒ D(ai , a0−i , Ni (t)) ≤ D(a0 , Ni (t)).
We will define a general class of reasonable objective functions. An objective function
for player Pi is called a reasonable objective function if, for any time t > 0, and any
action profile a ∈ A, the better response set satisfies the following two conditions:
1. Bi (a, t) ⊂ {Si (a, t), ∅},
2. |Si (a, t)| > 1 ⇒ Bi (a, t) 6= ∅.
Roughly speaking, these conditions ensure that a player will not value moving further
away from his belief about the location of his neighbors.
We will now relax our requirements on the connectivity and time-invariance of the
interaction graph in the consensus problem. A common assumption on the interaction
graph is connectedness over intervals.
Assumption 6.5.2 (Connectedness Over Intervals). There exists a constant T > 0
such that for any time t > 0, the interaction graph with nodes P and edges E =
E(t) ∪ · · · ∪ E(t + T ) is connected.
Claim 6.5.1. Reasonable objective functions introduced above constitute a sometimes
weakly acyclic game with the potential function (6.6) provided that the interaction

132

graph satisfies Assumption 6.5.2. Furthermore, every universal Nash equilibrium constitutes consensus.

Proof. It is easy to see that any consensus point is a universal Nash equilibrium. We
will show that if an action profile is not a consensus point, then there exists a player
who can increase his objective function as well as the potential function at some time in
a fixed time window. This implies that every universal Nash equilibrium is a consensus
point and furthermore that the game is sometime weakly acyclic.
Let a0 = a(t0 ) be any joint action that is not a consensus point. We will show
that for some time t1 ∈ [t0 , t0 + T ] there exists a player Pi ∈ P with an action
a∗i ∈ Ai such that Ui (a∗i , a0−i , t1 ) > Ui (a0 , t1 ) and φ(a∗i , a0−i ) > φ(a0 ). To see this
let P ∗ be the extreme player set with the least number of players, i.e., P ∗ = P u (a0 )
if |P u (a0 )| ≤ |P l (a0 )| or P ∗ = P l (a0 ) if |P u (a0 )| > |P l (a0 )|. Since the interaction
graph satisfies Assumption 6.5.23 , for some t1 ∈ [t0 , t0 + T ] there exists at least one
player Pi ∈ P ∗ with a neighbor Pj ∈ Ni (t1 ) such that Pj ∈
/ P ∗ . Therefore,
|Si (a0 , t1 )| > 1 ⇒ |Bi (a0 , t1 )| =
6 ∅.
Let a∗i ∈ Bi (a0 , t1 ) and for notional convenience let a1 = (a∗i , a0−i ). We know that
D(a1 , P) ≤ D(a0 , P). If D(a1 , P) < D(a0 , P), then
φ(a1 ) = −D(a1 , P) + δA (1 − n(a1 )/n),
> −D(a0 , P) + δA + δA (1 − n(a1 )/n),
> −D(a0 , P) + δA + δA (1 − (n(a0 ) + n)/n),
= φ(a0 ).
3

Note that assumption 6.5.2 is stronger than necessary for this proof.

133

If D(a1 , P) = D(a0 , P), then
φ(a1 ) = −D(a0 , P) + δA (1 − n(a1 )/n),
> −D(a0 , P) + δA (1 − (n(a1 ) + 1)/n),
≥ −D(a0 , P) + δA (1 − n(a0 )/n),
= φ(a0 ).
Therefore, a0 is not a universal Nash equilibrium.
If all players adhere to the better reply with inertia dynamics in a consensus problem where the interaction graph satisfies Assumption 6.5.2 and the players are assigned
reasonable objective functions then the joint action profile will converge almost surely
to a consensus point.
These results can easily be extended to a multi-dimensional consensus problem
with bounded observational delays.

6.5.2

Extension to Multi-Dimensional Consensus

One can easily extend the arguments above to show that any k-dimensional consensus
game is a sometimes weakly acyclic game by generalizing the measure and choosing
the extreme player sets appropriately. An example of an acceptable measure is
0

D(a, P ) :=

n
X
k=1

max 0 dTk (ai − aj ).

Pi ,Pj ∈P

where P 0 ⊆ P and d1 , d2 , ..., dn ∈ Rk is a set of measure vectors which span the complete space of Rk . The term maxPi ,Pj ∈P 0 dTk (ai − aj ) captures the maximum distance
between the action of any two agents in the nonempty player set P 0 relative to the measure direction dk . In the 1-D consensus problem, where d1 = 1, the measure reverts
back to (6.5).

134

The set of reasonable actions for player Pi at time t given the joint action profile a
is now
Si (a, t) = {a0i ∈ Ai : ∀k, max dTk aj ≥ dTk a0i ≥
Pj ∈Ni (t)

min

Pj ∈Ni (t)

dTk aj }.

The consensus algorithm in (6.1) corresponds to a specific reasonable utility function.
In particular, the set of reasonable actions is the convex hull of the previous actions of
his neighbors, i.e.,
Si (a, t) = {a0i ∈ Ai : a0i =

X
Pj ∈Ni (t)

ωij aj ,

X

ωij = 1, ωij > 0 ∀ Pj ∈ Ni (t)}.

Pj ∈Ni (t)

In the present setting, a player’s future action need not be in the convex hull of his
neighbors’ actions.

6.6

Group Based Decision Processes for Potential Games

In this section, we analyze the situation where players are allowed to collaborate with
a group of other players when making a decision. In particular we extend the results
of SAP to accommodate such a grouping structure.

6.6.1

Spatial Adaptive Play with Group Based Decisions

Consider a potential game with potential function φ : A → R. We will now introduce
a variant of SAP to accommodate group based decisions. At each time t > 0, a group
of players G ⊆ P is randomly chosen according to a fixed probability distribution
P ∈ ∆(2P ) where 2P denotes the set of subsets of P. We will refer to PG as the
probability that group G will be chosen. We make the following assumption on the
group probability distribution.
Assumption 6.6.1 (Completeness). For any player Pi ∈ P there exists a group G ⊆
P such that Pi ∈ G and PG > 0.

135

Once a group is selected, the group is unilaterally allowed to alter it’s collective
strategy. All players not in the group must repeat their action, i.e., a−G (t) = a−G (t−1),
where aG is the action-tuple of all players in the group G, and a−G is the action-tuple
of all players not in the group G. The group will be modeled as a single entity with a
Q
group utility function UG : A → R and a collective action set AG = Pi ∈G Ai . At
time t, the updating group G randomly selects a collective action from AG according
to the collective strategy pG (t) ∈ ∆(AG ) where the aG −th component paGG (t) of the
collective strategy is given as
exp{β Ui (aG , a−G (t − 1))}
,
āG ∈AG exp{β Ui (āG , a−G (t − 1))}

paGG (t) = P

for some exploration parameter β ≥ 0.
We make the following assumption on the admissible group utility functions:
Assumption 6.6.2 (Group Utility Functions). Group utility functions must preserve
the potential structure of the game, meaning that for any group G ⊆ P, collective
Q
group actions a0G , a00G ∈ AG , and a−G ∈ Pi ∈G
/ Ai ,
UG (a00G , a−G ) − UG (a0G , a−G ) = φ(a00G , a−G ) − φ(a0G , a−G ).
.
In general, group utility functions need to preserve this condition. However, one
can always assign each group a utility that captures the group’s marginal contribution
to the potential function, i.e., a wonderful life utility as discussed in Section 6.3. This
utility assignment guarantees preservation of the potential structure of the game.
We will now show that the convergence properties of the learning algorithm SAP
still hold with group based decisions.
Theorem 6.6.1. Consider a finite n-player potential game with potential function φ(·),
a group probability distribution P satisfying Assumption 6.6.1, and group utility func-

136

tions satisfying Assumption 6.6.2. SAP with group based decisions induces a Markov
process over the state space A where the unique stationary distribution µ ∈ ∆(A) is
given as
exp{β φ(a)}
, for any a ∈ A.
ā∈A exp{β φ(ā)}

µ(a) = P

(6.7)

Proof. The proof follows along the lines of the proof of Theorem 6.2 in [You98]. By
Assumption 6.6.1, the Markov process induced by SAP with group based decisions
is irreducible and aperiodic; therefore, the process has a unique stationary distribution. Below, we show that this unique distribution must be (6.7) by verifying that the
distribution (6.7) satisfies the detailed balanced equations
µ(a)Pab = µ(b)Pba ,
for any a, b ∈ A, where
Pab := Pr [a(t) = b|a(t − 1) = a] .
Note that there are now several ways to transition from a and b when incorporating
group based decisions. Let Ḡ(a, b) represent the group of players with different actions
in a and b, i.e.,
Ḡ(a, b) := {Pi ∈ P : ai 6= bi }.
Let G(a, b) ⊆ 2P be the complete set of player groups for which the transition from a
to b is possible, i.e.,
G(a, b) := {G ∈ 2P : Ḡ(a, b) ⊆ G}.
Since a group G ∈ G(a, b) has probability PG of being chosen in any given period,
it follows that

  X

exp{β φ(a)}
exp{β UG (b)}
µ(a)Pab = P
×
PG P
.
z∈A exp{β φ(z)}
āG ∈AG exp{β UG (āG , a−G )}
G∈G(a,b)

137

Letting

λG :=

1
P
z∈A exp{β φ(z)}




×


PG
P
,
āG ∈AG exp{β UG (āG , a−G )}

we obtain
µ(a)Pab =

X

λG exp{βφ(a) + βUG (b)}.

G∈G(a,b)

Since UG (b) − UG (a) = φ(b) − φ(a) and G(a, b) = G(b, a), we have
µ(a)Pab =

X

λG exp{βφ(b) + βUG (a)},

G∈G(b,a)

which leads us to
µ(a)Pab = µ(b)Pba .

6.6.2

Restricted Spatial Adaptive Play with Group Based Decisions

Extending these results to accommodate restricted action sets is straightforward. Let
a(t − 1) be the action profile at time t − 1. In this case, the restricted action set for
Q
any group G ⊆ P at time t will be AG (t) = Pi ∈G Ri (ai (t − 1)). We will state the
following theorem without proof to avoid redundancy.
Theorem 6.6.2. Consider a finite n-player potential game with potential function φ(·),
a group probability distribution P satisfying Assumption 6.6.1, and group utility functions satisfying Assumption 6.6.2. If the restricted action sets satisfy Assumptions 6.3.1
and 6.3.2, then RSAP induces a Markov process over the state space A where the
unique stationary distribution µ ∈ ∆(A) is given as
exp{β φ(a)}
, for any a ∈ A.
ā∈A exp{β φ(ā)}

µ(a) = P

138

6.6.3

Constrained Action Sets

The learning algorithms SAP or RSAP with group based decisions induced a Markov
process over the entire set A. We will now consider the situation in which each group’s
Q
action set is constrained, i.e., AG ⊂ Pi ∈G Ai . We will assume that the collective
action set of each group is time invariant.
Under this framework, the learning algorithms SAP or RSAP with group based
decisions induces a Markov process over the constrained set Ā ⊆ A which can be
characterized as follows: Let a(0) be the initial actions of all players. If ā ∈ Ā then
there exists a sequence of action profiles a(0) = a0 , a1 , ..., an = ā with the condition
that for all k ∈ {1, 2, ..., n}, ak = (akGk , ak−1
−Gk ) for a group Gk ⊆ P, where PGk > 0
and akGk ∈ AGk . The unique stationary distribution µ ∈ ∆(Ā) is given as
exp{β φ(a)}
, for any a ∈ Ā.
ā∈Ā exp{β φ(ā)}

µ(a) = P

6.7

(6.8)

Functional Consensus

In the consensus problem, as described in Section 6.3, the global objective was for all
agents to reach consensus. In this section, we will analyze the functional consensus
problem where the goal is for all players to reach a specific consensus point which is
typically dependent on the initial action of all players, i.e.,
lim ai (t) = f (a(0)), ∀Pi ∈ P,

t→∞

where a(0) ∈ A is the initial action of all players and f : A → R is the desired
function. An example of such a function for an n-player consensus problem is
1 X
f (a(0)) =
ai (0),
n P ∈P
i

for which the goal would be for all players to agree upon the average of the initial
actions of all players. We will refer to this specific functional consensus problem as

139

average consensus.
The consensus algorithm of (6.1) achieves the objective of average consensus under the condition that the interaction graph is connected and the associated weighting
matrix, Ω = {ωij }Pi ,Pj ∈P , is doubly stochastic. A doubly stochastic matrix is any
matrix where all coefficients are nonnegative and all column sums and rows sums are
equal to 1. The consensus algorithm takes on the following matrix form
a(t + 1) = Ω a(t).
If Ω is a doubly stochastic matrix, then for any time t > 0,
1T a(t + 1) = 1T Ω a(t) = 1T a(t).
Therefore, the sum of the actions of all players is invariant. Hence, if the players
achieve consensus, they must agree upon the average.
In order to achieve any form of functional consensus it is imperative that there exist
cooperation amongst the players. Players must agree on how to alter their action each
iteration. In the consensus algorithm, this cooperation is induced by the weighting matrix which specifies precisely how a player should change his action each iteration. If
a player acted selfishly and unilaterally altered his action, the invariance of the desired
function would not be preserved.

6.7.1

Setup: Functional Consensus Problem with Group Based Decisions

Consider the consensus problem with a time invariant undirected interaction graph as
described in Section 6.3. To apply the learning algorithm SAP or RSAP with group
based decisions to the functional consensus problem one needs to define both the group
utility functions and the group selection process.

140

6.7.2

Group Utility Function

Recall the potential function used for the consensus problem with a time invariant and
undirected interaction graph analyzed in Section 6.3,
X X
φ(a) = −(1/2)
kai − aj k.
Pi ∈P Pj ∈Ni

We will assign any group G ⊆ P the following local group utility function
X X
X X
UG (a) = −(1/2)
kai − aj k −
kai − aj k.
Pi ∈G Pj ∈Ni ∩G

(6.9)

Pi ∈G Pj ∈Ni \G

An explanation for the (1/2) is to avoid double counting since the interaction graph
is undirected. We will now show that this group utility function satisfies Assumption 6.6.2. Before showing this, let NG denote the neighbors of group G, i.e., NG =
S
Pi ∈G Ni . The change in the potential function by switching from a = (aG , a−G ) to
a0 = (a0G , a−G ) is
φ(a0 ) − φ(a) = −(1/2)

X X


ka0i − a0j k − kai − aj k .

Pi ∈P Pj ∈Ni

For simplicity of notation let δij = −(1/2)(ka0i − a0j k − kai − aj k). The change in the
potential can be expressed as
X X
δij ,
φ(a0 ) − φ(a) =
Pi ∈P Pj ∈Ni

=

X X

δij ,

Pi ∈NG Pj ∈Ni

=

X

X

δij +

Pi ∈G Pj ∈Ni ∩G

=

X

X

Pi ∈G Pj ∈Ni ∩G

X

X

δij +

Pi ∈G Pj ∈Ni \G

δij +

X

X

δij +

Pi ∈G Pj ∈Ni \G

Pi ∈NG \G Pj ∈Ni ∩G

141

X

δij ,

Pi ∈NG \G Pj ∈Ni

Since the interaction graph is undirected, we know that
X X
X
X
δij =
δij ,
Pi ∈G Pj ∈Ni \G

X
X

X

Pi ∈NG \G Pj ∈Ni ∩G

δij .

therefore, we can conclude that
X

X

φ(a0 ) − φ(a) =

Pi ∈G

X

δij + 2

Pj ∈Ni ∩G

δij



Pj ∈Ni \G

0

= UG (a ) − UG (a).

6.7.3

Group Selection Process and Action Constraints

Let a(t − 1) be the action profile at time t − 1. At time t, one player Pi is randomly
(uniformly) chosen. Rather that updating his action unilaterally, player Pi first selects
a group of players G ⊆ P which we will assume is the neighbors of player Pi , i.e.,
G = Ni . The group is assigned a group utility function as in (6.9) and a constrained
Q
action set AG ⊂ Pi ∈G Ai .
A central question is how can one constrain the group action set, using only location information, such as to preserve the invariance of the desired function f . In this
case, we will restrict our attention only to functions where “local” preservation equates
to “global” preservation. This means that for each group G ⊆ P there exists a function
fG : AG → R such that for any group actions a0G , a00G ∈ AG
fG (a0G ) = fG (a00G ) ⇒ f (a0G , a−G ) = f (a00G , a−G ), ∀a−G ∈

Y

Ai .

Pi ∈G
/

Examples of functions that satisfy this constraint are
fG (a) =

1 X
1 X
ai ⇒ f (a) =
ai ,
|G| P ∈G
|P| P ∈P
i

i

fG (a) = max ai ⇒ f (a) = max ai ,
Pi ∈G

Pi ∈P

fG (a) = min ai ⇒ f (a) = min ai .
Pi ∈G

Pi ∈P

In each of these examples, the structural form of f and fG is equivalent. There may
exist alternative functions where this is not required.

142

6.7.4

Illustration

We will illustrate this approach by solving the average consensus problem on the example developed in Section 6.3.4. Given the initial configuration, all players should
agree upon the action (5, 5). We will solve this average consensus problem using the
learning algorithm binary RSAP with group based decisions. However, we will omit
the non-convex obstruction in this illustration. This omission is not necessary, but
rather convenient for not having to verify the properties of the constrained action set,
i.e., is consensus even possible, and Assumption 6.3.2 for the group action sets.
Figure 6.3 illustrates the evolution of each player’s actions using the stochastic
learning algorithm binary RSAP with group based decisions and an increasing β coefficient, β(t) = 1.5 + t(2/1000).

6.8

Illustrative Examples

In this section we will develop two examples to further illustrate the wide range applicability of the theory developed in this chapter. The first problem we will consider is
the dynamic sensor allocation problem. Lastly, we will demonstrate how this theory
can be used to solve a popular mathematical puzzle called Sudoku.

6.8.1

Dynamic Sensor Coverage Problem

We consider the dynamic sensor coverage problem described in [LC05c] and references therein. The goal of the sensor coverage problem is to allocate a fixed number
of sensors across a given “mission space” to maximize the probability of detecting a
particular event.
We will divide the mission space into a finite set of sectors denoted as S. There

143

Player 1

Player 2

10

10
x state
y state

x state
y state

9

8

8

7

7

6

6
State

State

9

5

5

4

4

3

3

2

2

1

1

0

0
0

200

400
600
Iteration

800

1000

0

200

Player 3

800

1000

Player 4

10

10
x state
y state

9

x state
y state

9

8

8

7

7

6

6
State

State

400
600
Iteration

5

5

4

4

3

3

2

2

1

1

0

0
0

200

400
600
Iteration

800

1000

0

200

400
600
Iteration

800

1000

Figure 6.3: Evolution of Each Player’s Action in the Average Consensus Problem

exists an events density function, or relative reward function, R(s), defined over S. We
P
will assume that R(s) ≥ 0, ∀s ∈ S and s∈S R(s) = 1. In the application of enemy
submarine tracking, R(s) could be defined as the a priori probability that an enemy
submarine is situated in sector s. The mission space and associated reward function
that we will use in this section is illustrated in Figure 6.4.
There are a finite number of autonomous sensors denoted as P = {P1 , ..., Pn }
allocated to the mission space. Each sensor Pi can position itself in any particular

144

Reward Function over Mission Space

x 10

-3

Reward

4

2

0
0
20
40
60

100
80
60

80

40
20
100
0

Figure 6.4: Illustration of Reward Function Over Mission Space

sector, i.e., the action set of sensor Pi is Ai = S. Furthermore, each sensor has limited
sensing and moving capabilities. If an event occurs in sector s, the probability of sensor
Pi detecting the event given his current location ai is denoted as pi (s, ai ). Typically,
each sensor has a finite sensing radius, ri , where the probability of detection obeys the
following:
ks − ai k < ri ⇔ pi (s, ai ) > 0.
An example of the sensing and moving capabilities of a particular sensor is illustrated
in Figure 6.5.
For a given joint action profile a = {a1 , ..., an }, the joint probability of detecting
an event in sector s is given by
P (s, a) = 1 −

Y

[1 − pi (s, ai )].

Pi ∈P

In general a global planner would like the sensors to allocate themselves in such a
fashion as to maximize the following potential function
X
φ(a) =
R(s)P (s, a).
s∈S

145

Pi

Sensor
Coverage

Range Restricted
Action Sets

Pj

Figure 6.5: Illustration of Sensor Coverage and Range Restricted Action Sets of a Particular
Sensor

One way to accomplish such an objective is to assign each sensor a utility function
that is appropriately aligned with the global objective function as was the case in the
consensus problem. One option is to just assign each sensor the global objective, i.e.,
Ui (a) = φ(a).
Under this scenario, we have a potential game and one could use a learning algorithm
like SAP or RSAP to guarantee that the sensors allocate themselves in a configuration
that maximizes the global objective. However, this particular choice of utility functions
require each sensor to be knowledgable of the locations and capabilities of all other
sensors. To avoid this requirement, we will assign each sensor a Wonderful Life Utility
[AMS07, WT99]. The utility of sensor Pi given any action profile a ∈ A is now
Ui (a) = φ(ai , a−i ) − φ(a0i , a−i ),

(6.10)

where the action a0i is defined as the null action, which is equivalent to sensor Pi
turning off all sensing capabilities. The term φ(a0i , a−i ) captures the value of the allocation of all sensors other than sensor Pi . Therefore, the utility of sensor Pi for an

146

action profile a is defined as his marginal contribution to the global objective. This
means that a sensor now can evaluate his utility using only local information. Furthermore, the Wonderful Life Utility assignment preserves the potential game structure
[AMS07, WT99], meaning that SAP or RSAP can now be implemented with the sensors using only local information to guarantee that the sensors allocate themselves in
a desirable configuration.
In the following simulation we have the mission space and reward function as illustrated in Figure 6.4. The mission space is S = {1, 2, ..., 100} × {1, 2, ..., 100} and the
P
reward function satisfies s∈S R(s) = 1. We have 18 different autonomous sensors, 6
with a sensing radius of 6, 6 with a sensing radius of 12, and 6 with a sensing radius of
18. For simplicity, each sensor will have prefect sensing capabilities within its sensing
radius, namely for any sector s satisfying ks − ai k < ri , then pi (s, ai ) = 1. Each sensor is endowed with the WLU as expressed in (6.10). All 18 sensors originally started
at the location (1, 1) and each sensor has range restricted action sets as illustrated in
Figure 6.5. We ran the binary RSAP with β = 0.6. Figure 6.6 illustrates a snapshot
of the sensors configuration at the final iteration. Figure 6.7 illustrates the evolution of
the potential function over the mission.

6.8.2

Sudoku

Our final illustration of the broad applicability of potential games is the well known
mathematical puzzle of Sudoku. An example of a Sudoku puzzle is shown in Figure 6.8. The objective is to fill a 9x9 grid so that each column, each row, and each
of the nine 3x3 boxes contains the digits from 1 to 9. The puzzle setter provides a
partially completed grid (blue boxes) which cannot be changed.
We will now illustrate that Sudoku is exactly a potential game when the players,
action sets, and utility functions are designed appropriately. We will view each of the

147

100
90
80
70
60
50
40
30
20
10
0
0

20

40

60

80

100

Figure 6.6: Final Allocation of Sensors over Mission Space

Evolution of Objective Function over Mission
0.8

0.7

Objective Function

0.6

0.5

0.4

0.3

0.2

0.1

0
0

100

200
300
Iteration Number

400

500

Figure 6.7: Evolution of Potential Function over Mission

148

5
4

1

8

7

6

3

9

6

9

8

3

5
8

2
7

3

4

7

5

5

3

6

1

1

2

6

3

Figure 6.8: Illustration of a Sudoku Puzzle

empty boxes as a self interested player Pi with action set Ai = {1, 2, ..., 9}. Each
player will be assigned the utility function
Ui (a) :=

X

X

I{ai = aj } +

I{ai = aj } +

Pj ∈NiC

Pj ∈NiR

X

I{ai = aj },

Pj ∈NiB

where NiR , NiC , and NiB are the row, column and box neighbors of player Pi and I{·}
is the usual indication function. An illustration of the neighbor sets of player P1 is
highlighted in Figure 6.9, where the the green boxes indicate the row neighbors, red
boxes indicate the column neighbors, and yellow boxes indicate the box neighbors.
Note that in this framework, unlike with the consensus problem, each player Pi is not
a neighbor of himself.
To simplify the notation, we define the following function: for each player Pi and
for any player set P̄ ⊆ P, let
ni (a, P̄) :=

X

I{ai = aj }.

Pj ∈P̄

This function computes the number of players with the same action as player Pi in the

149

P1

5

4

1

8

7

6

3

9

6

9

8

3

5
8

2
7

3

4

7

5

5

3

6

1

1

2

6

3

Figure 6.9: Illustration of Neighbor Sets for a Player’s Utility Function in a Sudoku Puzzle

set P̄. Using this function, we will express the utility of player Pi as
Ui (a) = ni (a, NiR ) + ni (a, NiC ) + ni (a, NiB ).
We will now show that the Sudoku game with utilities defined as above is a potential game with potential function
X

φ(a) = 1/2

Ui (a).

Pi ∈P

To simplify the analysis, we will break up the potential function as
φ(a) = φR (a) + φC (a) + φB (a),
where
φR (a) = 1/2

X

ni (a, NiR ),

Pi ∈P
C

φ (a) = 1/2

X

ni (a, NiC ),

Pi ∈P
B

φ (a) = 1/2

X
Pi ∈P

150

ni (a, NiB ).

Let a0 , a00 ∈ Y be any two action profiles that differ by a unilateral deviation, i.e.,
a0i 6= a00i and a0−i = a00−i for some player Pi ∈ P. The change in φR (·) is
X

2(φR (a0 ) − φR (a00 )) =

ni (a0 , NiR ) − ni (a00 , NiR ),

Pi ∈P

X

= ni (a0 , NiR ) − ni (a00 , NiR ) +

nj (a0 , NjR ) − nj (a00 , NjR ),

Pj ∈NiR

X

= ni (a0 , NiR ) − ni (a00 , NiR ) +

nj (a0 , Pi ) − nj (a00 , Pi ),

Pj ∈NiR

X

= ni (a0 , NiR ) − ni (a00 , NiR ) +

ni (a0 , Pj ) − ni (a00 , Pj ),

Pj ∈NiR

= ni (a0 , NiR ) − ni (a00 , NiR ) + ni (a0 , NiR ) − ni (a00 , NiR ),
= 2(ni (a0 , NiR ) − ni (a00 , NiR )).
One could repeat this analysis for φC (·) and φB (·) to show that
φ(a0 ) − φ(a00 ) = Ui (a0 ) − Ui (a00 ).
Therefore the Sudoku game is in fact a potential game. Furthermore, the potential
function is always nonnegative, and achieves the value of 0 if and only if the Sudoku
puzzle has been solved. Therefore, all solutions to the Sudoku puzzles are in fact Nash
equilibria of the Sudoku game. However, much like the consensus problem, there may
exist suboptimal Nash equilibria.
To solve the Sudoku puzzle we will use the learning algorithm SAP as described in
Section 6.3.2. We let the β coefficient increase as β(t) = t/5000. Figure 6.10 shows
the evolution of the potential function during the SAP learning process. One can see
that the potential function achieves the value of 0 after approximately 17,000 iterations
which means that the puzzle has been solved. To verify, the final joint action profile is
illustrated in Figure 6.11.
To further illustrate the applicability of SAP, we simulated SAP on a Sudoku puzzle

151

Evolution of Potential Function for Sudoku Game using Spatial Adaptive Play
120

Value of Potential Function

100

80

60

Sudoku Solved!
40

20

0
0

2000

4000

6000

8000
10000
Iteration Number

12000

14000

16000

18000

Figure 6.10: Evolution of Potential Function in Sudoku Puzzle Under the Learning Algorithm
Spatial Adaptive Play

3

6

8

7

2

9

4

5

1

4

9

2

1

8

5

7

6

3

5

1

7

6

4

3

9

8

2

1

7

6

9

5

8

3

2

4

9

5

4

2

3

1

6

7

8

2

8

3

4

6

7

5

1

9

8

2

5

3

9

6

1

4

7

7

4

9

5

1

2

8

3

6

6

3

1

8

7

4

2

9

5

Figure 6.11: The Completed Sudoku Puzzle

152

classified as very hard. Once again, a solution to the puzzle was found as illustrated in
Figure 6.12.
1
6

5

7

9

2

Evolution of Potential Function for Sudoku Game using Spatial Adaptive Play

6
7
9

4

9

7

2

3
8

6

1

6

4
7
3

3

1

8

6

9

1

3

5

8

7

4

6

2

120

5

4

6

9

3

2

7

8

1

7

8

2

1

6

4

3

5

9

1

5

4

6

7

3

9

2

8

2

6

9

4

5

8

1

7

3

3

7

8

2

1

9

6

4

5

6

9

1

7

2

5

8

3

4

8

2

7

3

4

1

5

9

6

4

3

5

8

9

6

2

1

7

100
Value of Potential Function

7

140

80

Sudoku Solved!

60

40

20

5
1

0
0

1

2

3
4
Iteration Number

5

6

7
x 10

5

Figure 6.12: Spatial Adaptive Play on a Sudoku Puzzle Classified as Very Hard

It is important to note that while it took many iterations to solve the Sudoku puzzles, the algorithm of SAP was applied in its original form. We firmly believe that the
algorithm could be modified to decrease computation time. For example, a player’s
action set could be reduced with knowledge of the board. In particular, the action set
of player P1 in Figure 6.9 could initially have been set as A1 = {1, 2, 3, 6, 7, 8, 9}.

6.9

Concluding Remarks

We have proposed a game theoretic approach to cooperative control by highlighting a
connection between cooperative control problems and potential games. We introduced
a new class of games and enhanced existing learning algorithms to broaden the applicability of game theoretic methods in cooperative control setting. We demonstrated
that one could successfully implement game theoretic methods on the cooperative control problem of consensus in a variety of settings. While the main example used was
the consensus problem, the results in Theorems 6.3.1, 6.4.1, and 6.6.1 and the notion
of a sometimes weakly acyclic game is applicable to a broader class of games as well

153

as other cooperative control problems.

154

CHAPTER 7
Conclusions
This dissertation focused on dealing with the distributed nature of decision making and
information processing through a non-cooperative game-theoretic formulation. The
emphasis was on simple learning algorithms that guarantee convergence to a Nash
equilibrium.
We analyzed the long-term behavior of a large number of players in large-scale
games where players are limited in both their observational and computational capabilities. In particular, we analyzed a version of JSFP and showed that it accommodates
inherent player limitations in information gathering and processing. Furthermore, we
showed that JSFP has guaranteed convergence to a pure Nash equilibrium in all generalized ordinal potential games, which includes but is not limited to all congestion
games, when players use some inertia either with or without exponential discounting
of the historical data. Furthermore, we introduced a modification of the traditional
no-regret algorithms that (i) exponentially discounts the memory and (ii) brings in a
notion of inertia in players’ decision process. We showed how these modifications can
lead to an entire class of regret based algorithms that provide convergence to a pure
Nash equilibrium in any weakly acyclic game.
The method of proof used for JSFP and the regret based dynamics relies on inertia to derive a positive probability of a single player seeking to make an utility improvement, thereby increasing the potential function. This suggests a convergence rate
that is exponential in the game size, i.e., number of players and actions. It should be

155

noted that inertia is simply a proof device that assures convergence for generic potential games. The proof provides just one out of multiple paths to convergence. The
simulations reflect that convergence can be much faster. Indeed, simulations suggest
that convergence is possible even in the absence of inertia. Furthermore, recent work
[HM06] suggests that convergence rates of a broad class of distributed learning processes can be exponential in the game size as well, and so this seems to be a limitation
in the framework of distributed learning rather than any specific learning process (as
opposed to centralized algorithms for computing an equilibrium).
We also analyzed the long-term behavior of a large number of players in large-scale
games where players only have access to the action they played and the utility they
received. Our motivation for this information restriction is that in many engineered
systems, the functional forms of utility functions are not available, and so players must
adjust their strategies through an adaptive process using only payoff measurements. In
the dynamic processes defined here, there is no explicit cooperation or communication
between players. One the one hand, this lack of explicit coordination offers an element of robustness to a variety of uncertainties in the strategy adjustment processes.
Nonetheless, an interesting future direction would be to investigate to what degree
explicit coordination through limited communications could be beneficial.
In this payoff based setting, players are no longer capable of analyzing the utility they would have received for alternative action choices as required in the regret
based algorithms and JSFP. We introduced Safe Experimentation dynamics for identical interest games, Simple Experimentation dynamics for weakly acyclic games with
noise-free utility measurements, and Sample Experimentation dynamics for weakly
acyclic games with noisy utility measurements. For all three settings, we have shown
that for sufficiently large times, the joint action taken by players will constitute a Nash
equilibrium. Furthermore, we have shown how to guarantee that a collective objective

156

in a congestion game is a (non-unique) Nash equilibrium.
Lastly, we proposed a game theoretic approach to cooperative control by highlighting a connection between cooperative control problems and potential games. We
introduced a new class of games and enhanced existing learning algorithms to broaden
the applicability of game theoretic methods in the cooperative control setting. We
demonstrated that one could successfully implement game theoretic methods on several cooperative control problems including consensus, dynamic sensor allocation, and
distributing routing over a network. Furthermore, we even demonstrated how the
mathematical puzzle of Sudoku can be modeled as a potential game and solved in
a distributed fashion using the learning algorithms discussed in this dissertation.
In summary, this dissertation illustrated a connection between the fields of learning
in games and cooperative control and developed several suitable learning algorithms
for a wide variety of cooperative control problems. There remains several interesting
and challenging directions for future research.
Equilibrium Selection and Utility Design:
One problem regarding a game theoretic formulation of a multi-agent system is the
existence of multiple Nash equilibria, not all of which are desirable operating conditions. Is it possible to develop a methodology for designing agent utilities/objectives
and to derive implementable learning algorithms that guarantee the agents’ collective
behavior converges to a desirable Nash equilibrium? For example, the potential game
formulation of the consensus problem had suboptimal Nash equilibria, i.e., Nash equilibria that did not represent consensus points. The existence of these suboptimal Nash
equilibria required the use of a stochastic learning algorithm such as SAP or RSAP
to guarantee reaching a desirable Nash equilibrium. However, when we modeled the
consensus problem as a sometimes weakly acyclic game and properly designed the
utilities we were able to effectively eliminate these suboptimal Nash equilibria. Can

157

this be accomplished for more general cooperative control problems?
Learning Algorithms for Stochastic Games:
In many cooperative control problems players are inherently faced with a notion of
state dependent action sets and objectives. Stochastic games, which generalize Markov
decision processes to multiple decision makers, emerge as the most natural framework
to study such cooperative systems. An important research direction is understand to
applicability of Markov games for cooperative control problems and to develop simple
computational learning algorithms for stochastic games with guaranteed convergence
results. We believe that the notion of sometimes weakly acyclic game is an initial step
in the direction or Markov games.
Learning Algorithms with Time Guarantees:
One open issue with regarding the applicability of the learning algorithms discussed in this paper is time complexity. Roughly speaking, how long will it take the
agents to reach some form of a desirable operating condition? One question that has
relevance is whether non-stochastic learning algorithms, such as JSFP and regret based
algorithms, have computational advantage over stochastic learning algorithms, such as
SAP or RSAP. If the answer to this question is an affirmative, than the notion of utility
design plays an even more important role in the applicability of these learning algorithms for controlling multi-agent systems.

158

R EFERENCES
[AMS07] G. Arslan, J. R. Marden, and J. S. Shamma. “Autonomous Vehicle-Target
Assignment: A Game Theoretical Formulation.” ASME Journal of Dynamic Systems, Measurement and Control, 2007. to appear.
[AS04]

G. Arslan and J. S. Shamma. “Distributed convergence to Nash equilibria
with local utility measurements.” In 43rd IEEE Conference on Decision
and Control, pp. 1538–1543, 2004.

[BEL06]

A. Blum, E. Evan-Dar, and K. Ligett. “On Convergence to Nash Equilibria
of Regret-Minimizing Algorithms in Routing Games.” In Symposium on
Principles of Distributed Computing (PODC), 2006.

[BHO05]

V. D. Blondel, J. M. Hendrickx, A. Olshevsky, and J. N. Tsitsiklis. “Convergence in multiagent coordination, consensus, and flocking.” In IEEE
Conference on Decision and Control, 2005.

[BK03]

V. S. Borkar and P. R. Kumar. “Dynamic Cesaro-Wardrop equilibration
in networks.” IEEE Transactions on Automatic Control, 48(3):382–396,
2003.

[BL85]

M. Ben-Akiva and S. Lerman. Discrete-Choice Analysis: Theory and
Application to Travel Demand. MIT Press, Cambridge, MA, 1985.

[Bow04]

M. Bowling. “Convergence and No-Regret in Multiagent Learning.” In
Neural Information Processing Systems Conference (NIPS), 2004.

[BP05]

B. Banerjee and J. Peng. “Efficient No-regret Multiagent Learning.” In
The 20th National Conference on Artificial Intelligence (AAAI-05), 2005.

[BPK91]

M. Ben-Akiva, A. de Palma, and I. Kaysi. “Dynamic network models and
driver information systems.” Transportation Research A, 25A:251–266,
1991.

[Bra68]

D. Braess.
“Uber ein Paradoxen der Verkehrsplanning.”
ternehmensforschung, 12:258–268, 1968.

[BT96]

D. P. Bertsekas and J. N. Tsitsiklis.
Athena Scientific, Belmont, MA, 1996.

[FK93]

D. Fudenberg and D. Kreps. “Learning mixed equilibria.” Games and
Economic Behavior, 5:320–367, 1993.

159

Un-

Neuro-Dynamic Programming.

[FL98]

D. Fudenberg and D. K. Levine. The Theory of Learning in Games. MIT
Press, Cambridge, MA, 1998.

[FRV06]

S. Fischer, H. Raecke, and B. Voecking. “Fast convergence to Wardrop
equilibria by adaptive sampling methods.” In Proceedings of the 38th Annual ACM Symposium on Theory of Computing, pp. 653–662, 2006.

[FT91]

D. Fudenberg and J. Tirole. Game Theory. MIT Press, Cambridge, MA,
1991.

[FV04]

S. Fischer and B. Vocking. “The evolution of selfish routing.” In Proceedings of the 12th European Symposium on Algorithms (ESA ’04), pp.
323–334, 2004.

[FV05]

S. Fischer and B. Voecking. “Adaptive routing with stale information.”
In Proceedings of the 24th Annual ACM Symposium on Principles of Distributed Computing, pp. 276–283, 2005.

[FY06]

D. P. Foster and H. P. Young. “Regret testing: Learning to play Nash equilibrium without knowing you have an opponent.” Theoretical Economics,
1:341–367, 2006.

[Ger94]

S. B. Gershwin. Manufacturing Systems Engineering. Prentice-Hall,
1994.

[GJ03]

A. Greenwald and A. Jafari. “A General Class of No-Regret Learning
Algorithms and Game-Theoretic Equilibria.” In Conference on Learning
Theory (COLT), pp. 2–12, 2003.

[GL]

F. Germano and G. Lugosi. “Global convergence of Foster and Young’s
regret testing.” Games and Economic Behavior. forthcoming.

[Gor05]

G. J. Gordon. “No-regret algorithms for structured prediction problems.”
Technical Report CMU-CALD-05-112, Department of Machine Learning
at Carnegie Mellon, 2005.

[GSM05] A. Ganguli, S. Susca, S. Martinez, F. Bullo, and J. Cortes. “On collective
motion in sensor networks: sample problems and distributed algorithms.”
In Proceedings of the 44th IEEE Conference on Decision and Control, pp.
4239–4244, Seville, Spain, December 2005.
[Har05]

S. Hart. “Adaptive Heuristics.” Econometrica, 73(5):1401–1430, 2005.

[HM00]

S. Hart and A. Mas-Colell. “A simple adaptive procedure leading to correlated equilibrium.” Econometrica, 68:1127–1150, 2000.

160

[HM01]

S. Hart and A. Mas-Colell. “A general class of adaptative strategies.”
Journal of Economic Theory, 98:26–54, 2001.

[HM03a]

S. Hart and A. Mas-Colell. “Regret based continuous-time dynamics.”
Games and Economic Behavior, 45:375–394, 2003.

[HM03b]

S. Hart and A. Mas-Colell. “Uncoupled dynamics do not lead to Nash
equilibrium.” American Economic Review, 93(5):1830–1836, 2003.

[HM06]

S. Hart and Y. Mansour. “The communication complexity of uncoupled
nash equilibrium procedures.” Technical Report DP-419, The Hebrew
University of Jerusalem, Center for Rationality, April 2006.

[HS98]

J. Hofbauer and K. Sigmund. Evolutionary Games and Population Dynamics. Cambridge University Press, Cambridge, UK, 1998.

[HS04]

S. Huck and R. Sarin. “Players with limited memory.” Contributions to
Theoretical Economics, 4(1), 2004.

[JGD01]

A. Jafari, A. Greenwald, D., and G. Ercal. “On No-Regret Learning, Fictitious Play, and Nash Equilibrium.” In Proceedings of the Eighteenth International Conference on Machine Learning (ICML), pp. 226–233, 2001.

[JLM03]

A. Jadbabaie, J. Lin, and A. S. Morse. “Coordination of groups of mobile
autonomous agents using nearest neighbor rules.” IEEE Transaction on
Automatic Control, 48(6):988–1001, June 2003.

[KBS06]

A. Kashyap, T. Basar, and R. Srikant. “Consensus with Quantized Information Updates.” In 45th IEEE Conference on Decision and Control, pp.
2728–2733, 2006.

[KV05]

A. Kalai and S. Vempala. “Efficient algorithms for online decision problems.” Journal of Computer and System Sciences, 71(3):291–307, 2005.

[LC03]

D. Leslie and E. Collins. “Convergent multiple-timescales reinforcement
learning algorithms in normal form games.” Annals of Applied Probability, 13:1231–1251, 2003.

[LC05a]

D. Leslie and E. Collins. “Generalised weakened fictitious play.” Games
and Economic Behavior, 56:285–298, 2005.

[LC05b]

D. Leslie and E. Collins. “Individual Q-learning in normal form games.”
SIAM Journal on Control and Optimization, 44(2), 2005.

[LC05c]

W. Li and C. G. Cassandras. “Sensor Networks and Cooperative Control.”
European Journal of Control, 2005. to appear.

161

[LES05]

T. Lambert, M. Epelman, and R. Smith. “A Fictitious Play Approach to
Large-Scale Optimization.” Operations Research, 53(3):477–489, 2005.

[MAS05] J. R. Marden, G. Arslan, and J. S. Shamma. “Joint Strategy Fictitious
Play with Inertia for Potential Games.” In Proceedings of the 44th IEEE
Conference on Decision and Control, pp. 6692–6697, December 2005.
Submitted to IEEE Transactions on Automatic Control.
[MAS07a] J. R. Marden, G. Arslan, and J. S. Shamma. “Connections Between Cooperative Control and Potential Games Illustrated on the Consensus Problem.” In Proceedings of the 2007 European Control Conference (ECC
’07), July 2007. to appear.
[MAS07b] J. R. Marden, G. Arslan, and J. S. Shamma. “Regret Based Dynamics:
Convergence in Weakly Acyclic Games.” In Proceedings of the 2007 International Conference on Autonomous Agents and Multiagent Systems
(AAMAS), Honolulu, Hawaii, May 2007.
[Mil04]

I. Milchtaich. “Social optimality and cooperation in nonatomic congestion
games.” Journal of Economic Theory, 114(1):56–87, 2004.

[Mor04]

L. Moreau. “Stability of Continuous-Time Distributed Consensus Algorithms.” In 43rd IEEE Conference on Decision and Control, pp. 3998–
4003, 2004.

[MS96a]

D. Monderer and L. S. Shapley. “Fictitious play property for games with
identical interests.” Journal of Economic Theory, 68:258–265, 1996.

[MS96b]

D. Monderer and L. S. Shapley. “Potential Games.” Games and Economic
Behavior, 14:124–143, 1996.

[MS97]

D. Monderer and A. Sela. “Fictitious play and no-cycling conditions.”
Technical report, 1997.

[MS07]

S. Mannor and J.S. Shamma. “Multi-agent Learning for Engineers.” 2007.
forthcoming special issue in Artificial Intelligence.

[MYA07] J. R. Marden, H. P. Young, G. Arslan, and J. S. Shamma. “Payoff Based
Dynamics for Multi-Player Weakly Acyclic Games.” SIAM Journal of
Control and Optimization, 2007. submitted to.
[OFM07] R. Olfati-Saber, J. A. Fax, and R. M. Murray. “Consensus and Cooperation
in Networked Multi-Agent Systems.” In Proceedings of the IEEE, January
2007. to appear.

162

[OM03]

R. Olfati-Saber and R. M. Murray. “Consensus Problems in Networks of
Agents with Switching Topology and Time-Delays.” IEEE Transaction on
Automatic Control, 49(6), June 2003.

[Ros73]

R. W. Rosenthal. “A Class of Games Possessing Pure-Strategy Nash Equilibria.” Int. J. Game Theory, 2:65–67, 1973.

[Rou03]

Tim Roughgarden. “The price of anarchy is independent of the network
topology.” Journal of Computer and System Sciences, 67(2):341–364,
2003.

[SA05]

J. S. Shamma and G. Arslan. “Dynamic fictitious play, dynamic gradient
play, and distributed convergence to Nash equilibria.” IEEE Transactions
on Automatic Control, 50(3):312–327, 2005.

[Sam97]

L. Samuelson. Evolutionary Games and Equilibrium Selection. MIT
Press, Cambridge, MA, 1997.

[San02]

W. Sandholm. “Evolutionary Implementation and Congestion Pricing.”
Review of Economic Studies, 69(3):667–689, 2002.

[SB98]

R. S. Sutton and A. G. Barto. Reinforcement Learning: An Introduction.
MIT Press, MA, 1998.

[SPG07]

Y. Shoham, R. Powers, and T. Grenager. “If multi-agent learning is the
answer, what is the question?” forthcoming special issue in Artificial
Intelligence, 2007.

[TBA86]

J. N. Tsitsiklis, D. P. Bertsekas, and M. Athans. “Distributed Asynchronous Deterministic and Stochastic Gradient Optimization Algorithms.” IEEE Transactions on Automatic Control, 35(9):803–812, 1986.

[War52]

J. G. Wardrop. “Some theoretical aspects of road traffic research.” In
Proceedings of the Institute of Civil Engineers, volume I, pt. II, pp. 325–
378, London, Dec. 1952.

[Wei95]

J.W. Weibull. Evolutionary Game Theory. MIT Press, Cambridge, MA,
1995.

[WT99]

D. Wolpert and K. Tumor. “An overview of collective intelligence.” In
J. M. Bradshaw, editor, Handbook of Agent Technology. AAAI Press/MIT
Press, 1999.

[XB04]

L. Xiao and S. Boyd. “Fast linear iterations for distributed averaging.”
Systems and Control Letters, 2004.

163

[XB05]

L. Xiao and S. Boyd. “A scheme for robust distributed sensor fusion based
on average consensus.” In Information processing in sensor networks,
2005.

[You93]

H. P. Young. “The Evolution of Conventions.” Econometrica, 61(1):57–
84, January 1993.

[You98]

H. P. Young. Individual Strategy and Social Structure. Princeton University Press, Princeton, NJ, 1998.

[You05]

H. P. Young. Strategic Learning and its Limits. Oxford University Press,
2005.

164

