import re

files = ['Fase_Metodologi.qmd', 'Fase_LatarBelakang.qmd', 'Fase_Hasil.qmd']

for filepath in files:
    with open(filepath, 'r') as f:
        lines = f.readlines()
        
    new_lines = []
    stack = []
    
    for i, line in enumerate(lines):
        m_open = re.match(r'^(:{3,})\s*\{(.*)\}\s*$', line)
        if m_open:
            colons = m_open.group(1)
            attrs = m_open.group(2).strip()
            
            # Check if this should be a HTML div (it has style or .scrollable but NOT .columns, .column, .panel-tabset, .r-stack, .fragment)
            if 'style=' in attrs or '.scrollable' in attrs:
                if '.columns' not in attrs and '.column' not in attrs and '.panel-tabset' not in attrs and '.r-stack' not in attrs and '.fragment' not in attrs:
                    # Convert to HTML div
                    html_attrs = attrs
                    # Convert .class to class="class"
                    classes = re.findall(r'\.([\w-]+)', attrs)
                    if classes:
                        html_attrs = re.sub(r'\.[\w-]+\s*', '', html_attrs)
                        html_attrs = f'class="{" ".join(classes)}" ' + html_attrs
                    
                    new_lines.append(f"<div {html_attrs.strip()}>\n")
                    stack.append((colons, True)) # True means it's an HTML div
                    continue
            
            new_lines.append(line)
            stack.append((colons, False))
            continue
            
        m_close = re.match(r'^(:{3,})\s*$', line)
        if m_close:
            colons = m_close.group(1)
            if stack and stack[-1][0] == colons:
                opened_colons, is_html = stack.pop()
                if is_html:
                    new_lines.append("</div>\n")
                else:
                    new_lines.append(line)
            else:
                new_lines.append(line)
            continue
            
        new_lines.append(line)
        
    with open(filepath, 'w') as f:
        f.writelines(new_lines)

