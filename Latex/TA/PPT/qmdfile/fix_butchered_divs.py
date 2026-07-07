import re

files = ['Fase_Metodologi.qmd', 'Fase_LatarBelakang.qmd', 'Fase_Hasil.qmd']

replacements = {
    '6em': '0.6em',
    '7em': '0.7em',
    '75em': '0.75em'
}

for filepath in files:
    with open(filepath, 'r') as f:
        text = f.read()
        
    for bad_cls, right_val in replacements.items():
        # Case 1: class="bad_cls" style="...font-size: 0;..."
        # We need to remove class="bad_cls" and replace font-size: 0; with font-size: right_val;
        text = re.sub(rf'class="{bad_cls}"([^>]+)font-size:\s*0;', rf'\1font-size: {right_val};', text)
        
        # Case 2: class="scrollable bad_cls" style="...font-size: 0;..."
        text = re.sub(rf'class="scrollable\s+{bad_cls}"([^>]+)font-size:\s*0;', rf'class="scrollable"\1font-size: {right_val};', text)

    # Some might be class="6em" (with no other classes left) which we just turned into <div style="...">
    # but there might be an extra space: <div  style="...">
    text = re.sub(r'<div\s+style=', '<div style=', text)

    with open(filepath, 'w') as f:
        f.write(text)

