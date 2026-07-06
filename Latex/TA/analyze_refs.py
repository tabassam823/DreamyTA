import os
import re

bib_file = '/home/asus/Documents/DreamyTA/Latex/TA/Referensi.bib'
filtered_dir = '/home/asus/Documents/DreamyTA/Latex/TA/Filtered_Paper'

with open(bib_file, 'r') as f:
    content = f.read()

# find all citation keys
keys = re.findall(r'@\w+\{([^,]+),', content)

# find all pdf/md files in filtered_dir
file_to_folder = {}
for root, dirs, files in os.walk(filtered_dir):
    for file in files:
        if file.endswith('.pdf') or file.endswith('.md'):
            rel_path = os.path.relpath(root, filtered_dir)
            file_to_folder[file] = rel_path

print("Total keys in bib:", len(keys))
print("Total keys:", keys[:5])

# Also check how file names in bib map to files
files_in_bib = re.findall(r'file = \{[^:]*:([^:]+):', content)
print("Files mentioned in bib:", len(files_in_bib))

