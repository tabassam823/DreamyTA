import re

file = 'PPT/qmdfile/Fase_Metodologi.qmd'
with open(file, 'r') as f:
    text = f.read()

# Replace <hr> with <hr/>
text = re.sub(r'<hr\s*>', '<hr/>', text)
# Replace <hr style="..."> with <hr style="..."/>
text = re.sub(r'<hr\s+([^>]+?)(?<!/)>', r'<hr \1/>', text)

with open(file, 'w') as f:
    f.write(text)

