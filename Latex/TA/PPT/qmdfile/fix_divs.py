import re

files = ['Fase_Metodologi.qmd', 'Fase_LatarBelakang.qmd', 'Fase_Hasil.qmd']

for filepath in files:
    with open(filepath, 'r') as f:
        lines = f.readlines()
        
    new_lines = []
    for i, line in enumerate(lines):
        # If the line is only colons (e.g., :::, ::::, etc.)
        if re.match(r'^:+\s*$', line):
            # Check if previous line in new_lines is not empty
            if len(new_lines) > 0 and new_lines[-1].strip() != '':
                new_lines.append('\n')
        new_lines.append(line)
        
    with open(filepath, 'w') as f:
        f.writelines(new_lines)
