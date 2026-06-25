import re
bib_file = '/home/asus/Documents/DreamyTA/Latex/TA/Referensi.bib'
with open(bib_file, 'r') as f:
    content = f.read()

entries = re.findall(r'@\w+\{([^,]+),.*?title\s*=\s*[\{"](.*?)[^\\][\}"]', content, re.DOTALL | re.IGNORECASE)
titles = {k: v.replace('\n', ' ').strip() for k, v in entries}
for k, v in titles.items():
    if "entanglement-induced" in v.lower() or "entanglement induced" in v.lower():
        print(k, v)
    if "information in black hole" in v.lower():
        print(k, v)
