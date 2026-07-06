import re
import os

bib_file = '/home/asus/Documents/DreamyTA/Latex/TA/Referensi.bib'
aux_file = '/home/asus/Documents/DreamyTA/Latex/TA/main.aux'

# Get all keys from .bib
with open(bib_file, 'r') as f:
    bib_content = f.read()

bib_keys = set()
# find @type{key,
matches = re.findall(r'@\w+\s*\{\s*([^,]+),', bib_content)
for m in matches:
    bib_keys.add(m.strip())

# Get used keys from .aux
# we need to search main.aux and all included .aux files!
# but actually LaTeX merges \citation into main.aux if they are sub-aux, wait... 
# Actually, \include produces its own .aux, but \input doesn't. 
# main.aux will contain \@input{Contents/.../xxx.aux} which we can follow.
# Instead of doing that, let's just grep \cite{...} from all .tex files!
tex_dir = '/home/asus/Documents/DreamyTA/Latex/TA/'
used_keys = set()

for root, _, files in os.walk(tex_dir):
    for file in files:
        if file.endswith('.tex'):
            with open(os.path.join(root, file), 'r') as f:
                content = f.read()
                cites = re.findall(r'\\cite\{([^\}]+)\}', content)
                for cite_match in cites:
                    # handle multiple keys like \cite{a,b,c}
                    keys = [k.strip() for k in cite_match.split(',')]
                    used_keys.update(keys)

unused_keys = sorted(list(bib_keys - used_keys))

with open('/home/asus/Documents/DreamyTA/Latex/TA/sisa_sitasi.md', 'w') as f:
    f.write("# Daftar Sitasi yang Belum Digunakan\n\n")
    f.write(f"Total sitasi di Referensi.bib: {len(bib_keys)}\n")
    f.write(f"Total sitasi yang digunakan: {len(used_keys.intersection(bib_keys))}\n")
    f.write(f"Sisa sitasi yang belum digunakan: {len(unused_keys)}\n\n")
    
    f.write("Berikut adalah *cite keys* dari `Referensi.bib` yang belum dipanggil di dalam file `.tex` manapun:\n\n")
    for i, key in enumerate(unused_keys, 1):
        f.write(f"{i}. `{key}`\n")

print(f"Total bib keys: {len(bib_keys)}")
print(f"Total used keys: {len(used_keys.intersection(bib_keys))}")
print(f"Unused keys written: {len(unused_keys)}")
