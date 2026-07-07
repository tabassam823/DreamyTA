import re

def process_file(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
        
    new_lines = []
    # We will build a stack of (original_colons, new_colons)
    stack = []
    
    # We will start at depth 0 using 7 colons.
    # Depth 1 will use 6, depth 2 will use 5, etc.
    # We just need: new_colons = max(3, 7 - len(stack))
    
    for line in lines:
        m_open = re.match(r'^(:{3,})\s*\{(.*)\}\s*$', line)
        if m_open:
            original_colons = m_open.group(1)
            attrs = m_open.group(2)
            
            new_colons_count = max(3, 8 - len(stack))
            new_colons = ':' * new_colons_count
            
            stack.append(original_colons)
            new_lines.append(f"{new_colons} {{{attrs}}}\n")
            continue
            
        m_close = re.match(r'^(:{3,})\s*$', line)
        if m_close:
            original_colons = m_close.group(1)
            # Find the matching original_colons in the stack.
            # Assuming perfectly matched in terms of our previous stack logic!
            if stack and stack[-1] == original_colons:
                stack.pop()
                new_colons_count = max(3, 8 - len(stack))
                new_colons = ':' * new_colons_count
                new_lines.append(f"{new_colons}\n")
            else:
                # Fallback, just use 3 colons or whatever
                new_lines.append(line)
            continue
            
        new_lines.append(line)
        
    with open(filepath, 'w') as f:
        f.writelines(new_lines)

for filepath in ['Fase_Metodologi.qmd', 'Fase_LatarBelakang.qmd', 'Fase_Hasil.qmd']:
    process_file(filepath)

