import re
import os

appendix_files = [
    'appendix_A.tex',
    'appendix_B.tex',
    'appendix_C.tex',
    'appendix_D.tex',
    'appendix_E.tex',
    'appendix_F.tex',
    'appendix_G.tex',
    'appendix_H.tex'
]

# 1. Remove \section from appendices and remove intro paragraphs "Dokumen ini menjelaskan..."
for file in appendix_files:
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove the \section commands, maintaining the content
        content = re.sub(r'\\section\{[^}]*\}\s*\\label\{[^}]*\}', '', content)
        
        # Remove introductory paragraphs containing "Dokumen ini menjelaskan"
        content = re.sub(r'Dokumen ini menjelaskan.*?\n\n', '', content, flags=re.DOTALL)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content.strip() + '\n')
        print(f"Formatted {file}")

# 2. Make appendix references in main.tex as links "(lihat appendix X)"
with open('main.tex', 'r', encoding='utf-8') as f:
    main_content = f.read()

# Replace plain text "Appendix X" with "\hyperref[appendix-x]{(lihat Appendix X)}"
def replace_appendix_ref(match):
    app_letter = match.group(1)
    label = f"appendix-{app_letter.lower()}"
    return f"\\hyperref[{label}]{{(lihat Appendix {app_letter})}}"

main_content = re.sub(r'Appendix ([A-H])', replace_appendix_ref, main_content)

with open('main.tex', 'w', encoding='utf-8') as f:
    f.write(main_content)
print("Formatted main.tex with links")
