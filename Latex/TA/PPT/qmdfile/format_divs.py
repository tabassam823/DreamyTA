import re

with open('Fase_Metodologi.qmd', 'r') as f:
    text = f.read()

# First, convert all <div class="scrollable"...> to ::: {.scrollable ...}
# and all <div style="..."> to ::: {style="..."}
# and </div> to :::
# BUT wait! Doing this via regex is hard because of nested divs.
# I already have the Python script that did this (convert_divs.py)!
