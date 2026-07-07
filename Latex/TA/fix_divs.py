import re

file = 'PPT/qmdfile/Fase_Metodologi.qmd'

with open(file, 'r') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    # Match `<div class="scrollable" style="...">`
    m1 = re.match(r'^<div\s+class="([^"]+)"\s+style="([^"]+)">', line.strip())
    # Match `<div style="...">`
    m2 = re.match(r'^<div\s+style="([^"]+)">', line.strip())
    # Match `</div>`
    m3 = re.match(r'^</div>', line.strip())
    
    if m1:
        cls = m1.group(1)
        style = m1.group(2)
        new_lines.append(f"::: {{.{cls} style=\"{style}\"}}\n")
    elif m2:
        style = m2.group(1)
        new_lines.append(f"::: {{style=\"{style}\"}}\n")
    elif m3:
        new_lines.append(":::\n")
    else:
        new_lines.append(line)

with open(file, 'w') as f:
    f.writelines(new_lines)

