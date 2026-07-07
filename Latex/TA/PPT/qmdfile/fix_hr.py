import re

with open('Fase_Metodologi.qmd', 'r') as f:
    lines = f.readlines()

new_lines = []
in_scrollable = False

for line in lines:
    if '<div class="scrollable"' in line:
        in_scrollable = True
    elif '</div>' in line and in_scrollable:
        in_scrollable = False
        
    if in_scrollable and line.strip() == '---':
        new_lines.append('<hr>\n')
    else:
        new_lines.append(line)

with open('Fase_Metodologi.qmd', 'w') as f:
    f.writelines(new_lines)
