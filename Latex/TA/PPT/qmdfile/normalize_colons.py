import re

files = ['Fase_Metodologi.qmd', 'Fase_LatarBelakang.qmd', 'Fase_Hasil.qmd']

for filepath in files:
    with open(filepath, 'r') as f:
        lines = f.readlines()
        
    new_lines = []
    stack = []
    
    for line in lines:
        m_open = re.match(r'^(:{3,})\s*\{(.*)\}\s*$', line)
        if m_open:
            attrs = m_open.group(2)
            if '.columns' in attrs:
                new_colons = ':::::'
            elif '.column' in attrs:
                new_colons = '::::'
            elif '.panel-tabset' in attrs:
                new_colons = '::::'
            else:
                new_colons = ':::'
                
            stack.append(new_colons)
            new_lines.append(f"{new_colons} {{{attrs}}}\n")
            continue
            
        m_close = re.match(r'^(:{3,})\s*$', line)
        if m_close:
            if stack:
                new_colons = stack.pop()
                new_lines.append(f"{new_colons}\n")
            else:
                # If stack is empty, just drop the closing colons (they are floating)
                pass
            continue
            
        new_lines.append(line)
        
    with open(filepath, 'w') as f:
        f.writelines(new_lines)

