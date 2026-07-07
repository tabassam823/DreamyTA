import glob

qmd_files = glob.glob('PPT/qmdfile/*.qmd')

def check_file(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    
    div_stack = []
    issues = []
    
    for i, line in enumerate(lines):
        line = line.strip()
        if line.startswith(':::'):
            colon_count = len(line) - len(line.lstrip(':'))
            has_attr = '{' in line
            
            if has_attr:
                div_stack.append((colon_count, i+1))
            else:
                # closing div
                if div_stack and div_stack[-1][0] == colon_count:
                    div_stack.pop()
                elif colon_count > 0:
                    issues.append(f"Line {i+1}: Closing div with {colon_count} colons, but stack is {div_stack}")
                    
    if div_stack:
        for colon_count, line_num in div_stack:
            issues.append(f"Line {line_num}: Unclosed opening div with {colon_count} colons")
            
    if issues:
        print(f"--- {file} ---")
        for issue in issues:
            print(issue)

for f in sorted(qmd_files):
    if "merged.qmd" in f or "test" in f or "main.qmd" in f:
        continue
    check_file(f)
