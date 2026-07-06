import os

with open("main.tex", "r") as f:
    main_content = f.read()

preamble = r"""\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{amsmath,amssymb,amsfonts}
\usepackage{hyperref}
\usepackage{bookmark}
\usepackage{graphicx}
\usepackage[indonesian]{babel}
\usepackage{geometry}
\geometry{a4paper, margin=1in}

\title{Penurunan Model Markowitz ke Ising Hamiltonian}
\author{}
\date{}

\begin{document}
\maketitle
\tableofcontents
\newpage

"""

postamble = r"""

\newpage
\appendix
\section{Markowitz}\label{appendix-a}
\input{appendix_A.tex}

\newpage
\section{Risk Aversion Endogen}\label{appendix-b}
\input{appendix_B.tex}

\newpage
\section{Lagrange Multiplier}\label{appendix-c}
\input{appendix_C.tex}

\newpage
\section{Teorema Rayleigh-Ritz}\label{appendix-d}
\input{appendix_D.tex}

\newpage
\section{Dekomposisi Hamiltonian}\label{appendix-e}
\input{appendix_E.tex}

\newpage
\section{Parameter Shift Rule}\label{appendix-f}
\input{appendix_F.tex}

\newpage
\section{Ekspansi State}\label{appendix-g}
\input{appendix_G.tex}

\newpage
\section{Born Rule}\label{appendix-h}
\input{appendix_H.tex}

\end{document}
"""

with open("main_compiled.tex", "w") as f:
    f.write(preamble + main_content + postamble)

