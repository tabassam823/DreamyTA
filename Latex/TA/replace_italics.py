import re

files = [
    "Contents/2_Daster/Bab-2.5.tex", 
    "Contents/2_Daster/Bab-2.6.tex", 
    "Contents/2_Daster/Bab-2.8.tex"
]

pattern = re.compile(r'(^|[\s\(\-])\*([A-Za-z][A-Za-z0-9\s\-]*)\*(?=$|[\s\)\,\.\:\;\-\?])')

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()
    
    # We might need to run it twice if there are overlapping matches, 
    # but the lookahead prevents overlap consumption.
    new_content = pattern.sub(r'\1\\textit{\2}', content)
    
    with open(filepath, 'w') as f:
        f.write(new_content)
        
print("Replacement complete.")
