import re
import os

files = ['Fase_Metodologi.qmd', 'Fase_LatarBelakang.qmd', 'Fase_Hasil.qmd']

for filepath in files:
    with open(filepath, 'r') as f:
        lines = f.readlines()
        
    new_lines = []
    div_stack = []
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # Check for block-level opening <div ...>
        m_open = re.match(r'^<div\s+([^>]+)>$', stripped)
        if m_open:
            attrs = m_open.group(1)
            # Convert class="xyz" style="abc" into .xyz style="abc"
            # Extract classes
            classes = []
            m_class = re.search(r'class="([^"]+)"', attrs)
            if m_class:
                classes = ['.' + c for c in m_class.group(1).split()]
                attrs = re.sub(r'class="[^"]+"\s*', '', attrs)
            
            attr_str = ' '.join(classes + [attrs.strip()]).strip()
            new_lines.append(f"::: {{{attr_str}}}\n")
            div_stack.append(True)
            continue
            
        # Check for block-level closing </div>
        if stripped == '</div>':
            if div_stack:
                div_stack.pop()
                new_lines.append(":::\n")
                continue
            
        new_lines.append(line)
        
    with open(filepath, 'w') as f:
        f.writelines(new_lines)

