import glob
import re

files = ["Fase_0.qmd", "Fase_1.qmd", "Fase_2.qmd", "Fase_LatarBelakang.qmd", "Fase_3.qmd", "Fase_4.qmd", "Fase_5.qmd", "Fase_6.qmd", "Fase_Metodologi.qmd", "Fase_7.qmd", "Fase_8.qmd", "Fase_9.qmd", "Fase_Hasil.qmd"]

for file in files:
    try:
        with open("PPT/qmdfile/" + file, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        continue
        
    stack = []
    print(f"--- Checking {file} ---")
    for i, line in enumerate(lines):
        line = line.strip()
        m = re.match(r'^(:{3,})(.*)', line)
        if m:
            colons = m.group(1)
            attrs = m.group(2).strip()
            
            # If it has attributes, it's an opening div
            if '{' in attrs:
                stack.append((len(colons), i+1, attrs))
                # print(f"Open {len(colons)} at {i+1}")
            else:
                # Without attributes, it's a closing div (if it matches something in the stack)
                if stack and stack[-1][0] == len(colons):
                    stack.pop()
                    # print(f"Close {len(colons)} at {i+1}")
                elif len(colons) >= 3:
                    print(f"Line {i+1}: Found {len(colons)} colons, but expected {stack[-1][0] if stack else 'none'}")
    
    if stack:
        for length, line_num, attrs in stack:
            print(f"ERROR in {file}: Unclosed div from line {line_num} with {length} colons ({attrs})")
        print()
