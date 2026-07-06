import os
import re
from difflib import SequenceMatcher

bib_file = '/home/asus/Documents/DreamyTA/Latex/TA/Referensi.bib'
filtered_dir = '/home/asus/Documents/DreamyTA/Latex/TA/Filtered_Paper'

with open(bib_file, 'r') as f:
    content = f.read()

# Extract keys and titles
entries = re.findall(r'@\w+\{([^,]+),.*?title\s*=\s*[\{"](.*?)[^\\][\}"]', content, re.DOTALL | re.IGNORECASE)

titles = {k: v.replace('\n', ' ').strip() for k, v in entries}

# find all files in filtered_dir
file_to_folder = {}
for root, dirs, files in os.walk(filtered_dir):
    for file in files:
        if file.endswith('.md') or file.endswith('.pdf'):
            rel_path = os.path.relpath(root, filtered_dir)
            file_to_folder[file] = rel_path

print(f"Total entries in bib: {len(titles)}")
print(f"Total files in Filtered_Paper: {len(file_to_folder)}")
for file, folder in file_to_folder.items():
    print(f"{folder}/{file}")

