import re

files = ['Fase_Metodologi.qmd', 'Fase_LatarBelakang.qmd', 'Fase_Hasil.qmd']

for filepath in files:
    with open(filepath, 'r') as f:
        lines = f.readlines()
        
    new_lines = []
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # Match ANY line that starts with 3 or more colons (opening or closing)
        is_fence = re.match(r'^:{3,}', stripped)
        is_heading = re.match(r'^#+\s+', stripped)
        
        if is_fence or is_heading:
            # Ensure blank line before
            if len(new_lines) > 0 and new_lines[-1].strip() != '':
                new_lines.append('\n')
                
            new_lines.append(line)
            
            # Ensure blank line after
            if i + 1 < len(lines) and lines[i+1].strip() != '':
                new_lines.append('\n')
        else:
            new_lines.append(line)
            
    with open(filepath, 'w') as f:
        f.writelines(new_lines)

