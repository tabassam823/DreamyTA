import re
import os
import json

bib_file = '/home/asus/Documents/DreamyTA/Latex/TA/Referensi.bib'
filtered_dir = '/home/asus/Documents/DreamyTA/Latex/TA/Filtered_Paper'
sisa_file = '/home/asus/Documents/DreamyTA/Latex/TA/sisa_sitasi.md'

with open(bib_file, 'r') as f:
    bib_content = f.read()

entries = re.findall(r'@\w+\s*\{\s*([^,]+),.*?title\s*=\s*[\{"](.*?)[^\\][\}"]', bib_content, re.DOTALL | re.IGNORECASE)
titles = {k.strip(): v.replace('\n', ' ').strip() for k, v in entries}

file_to_folder = {}
for root, dirs, files in os.walk(filtered_dir):
    for file in files:
        if file.endswith('.md') or file.endswith('.pdf'):
            rel_path = os.path.relpath(root, filtered_dir)
            file_to_folder[file] = rel_path

with open(sisa_file, 'r') as f:
    sisa_content = f.read()

unused_keys = re.findall(r'`([^`]+)`', sisa_content)

mapped = {}
for key in unused_keys:
    title = titles.get(key, "NOT_FOUND")
    words = [w for w in re.findall(r'\w+', title) if len(w) > 3]
    
    found_folder = "Uncategorized"
    for file, folder in file_to_folder.items():
        if any(w.lower() in file.lower() for w in words):
            found_folder = folder
            break
            
    if found_folder not in mapped:
        mapped[found_folder] = []
    mapped[found_folder].append((key, title))

print(json.dumps(mapped, indent=2))
