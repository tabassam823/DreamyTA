import re

with open('Fase_Metodologi.qmd', 'r') as f:
    lines = f.readlines()

stack = []
for i, line in enumerate(lines):
    line_num = i + 1
    m = re.match(r'^(:{3,})\s*(.*)', line)
    if m:
        colons = m.group(1)
        attrs = m.group(2).strip()
        if attrs:  # It's an opening div
            stack.append((colons, attrs, line_num))
            print(f"[{line_num}] OPEN  {colons} {attrs} (Stack: {[s[0] for s in stack]})")
        else:      # It's a closing div
            if stack and stack[-1][0] == colons:
                opened = stack.pop()
                print(f"[{line_num}] CLOSE {colons} (Matched with {opened[2]}) (Stack: {[s[0] for s in stack]})")
            else:
                print(f"[{line_num}] ERROR: Found {colons} but expected {stack[-1][0] if stack else 'NONE'}! (Stack: {[s[0] for s in stack]})")
                if stack:
                    # Try to find a match deeper in the stack
                    for j in range(len(stack)-1, -1, -1):
                        if stack[j][0] == colons:
                            print(f"    -> WARNING: Force closing down to {stack[j][2]}")
                            stack = stack[:j]
                            break
