import os
import re

bib_file = '/home/asus/Documents/DreamyTA/Latex/TA/Referensi.bib'
filtered_dir = '/home/asus/Documents/DreamyTA/Latex/TA/Filtered_Paper'

with open(bib_file, 'r') as f:
    content = f.read()

keys_to_check = ['fedorov_vqe_2022', 'hidalgo_quantum_2006', 'kumar_family_2025', 'sim_expressibility_2019', 'cohen_portfolio_2020', 'wang_achieving_2025', 'li_ising_2023', 'datta_relationship_2015', 'wang_variational_2025']

entries = re.findall(r'@\w+\{([^,]+),.*?title\s*=\s*[\{"](.*?)[^\\][\}"]', content, re.DOTALL | re.IGNORECASE)
titles = {k: v.replace('\n', ' ').strip() for k, v in entries}

file_to_folder = {}
for root, dirs, files in os.walk(filtered_dir):
    for file in files:
        if file.endswith('.md') or file.endswith('.pdf'):
            rel_path = os.path.relpath(root, filtered_dir)
            file_to_folder[file] = rel_path

for key in keys_to_check:
    title = titles.get(key, "NOT_FOUND_IN_BIB")
    print(f"Key: {key}, Title: {title}")
    words = [w for w in re.findall(r'\w+', title) if len(w) > 3]
    found = False
    for file, folder in file_to_folder.items():
        if any(w.lower() in file.lower() for w in words):
            print(f"  -> Found in: {folder}/{file}")
            found = True
            break
    if not found:
        print("  -> No matching file found")
