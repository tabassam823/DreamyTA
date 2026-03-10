import re
import os
import subprocess

appendix_map = {
    'Markowitz': 'Appendix A',
    'risk_aversion_endogen': 'Appendix B',
    'Lagrange_Multiplier': 'Appendix C',
    'Teorema_Reyleigh_Ritz': 'Appendix D',
    'Dekomposisi_Hamiltonian': 'Appendix E',
    'Parameter_Shift_Rule': 'Appendix F',
    'ekspansi_state': 'Appendix G',
    'Born_Rule': 'Appendix H',
    'suku_pertama_kedua': 'suku pertama kedua',
    'SPSA': 'SPSA'
}

def replace_links(content):
    def repl(match):
        link = match.group(1)
        return appendix_map.get(link, link)
    return re.sub(r'\[\[(.*?)\]\]', repl, content)

files_to_convert = [
    ('Markowitz_QUBO_TA.md', 'main.tex'),
    ('Markowitz.md', 'appendix_A.tex'),
    ('risk_aversion_endogen.md', 'appendix_B.tex'),
    ('Lagrange_Multiplier.md', 'appendix_C.tex'),
    ('Teorema_Reyleigh_Ritz.md', 'appendix_D.tex'),
    ('Dekomposisi_Hamiltonian.md', 'appendix_E.tex'),
    ('Parameter_Shift_Rule.md', 'appendix_F.tex'),
    ('ekspansi_state.md', 'appendix_G.tex'),
    ('Born_Rule.md', 'appendix_H.tex')
]

for md_file, tex_file in files_to_convert:
    if os.path.exists(md_file):
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        content = replace_links(content)
        
        tmp_md = f"tmp_{md_file}"
        with open(tmp_md, 'w', encoding='utf-8') as f:
            f.write(content)
        
        # Run pandoc to convert to latex
        # --no-highlight to avoid requiring verbatim packages
        # We don't want a standalone document for each appendix yet, just snippets,
        # but for main.tex maybe just snippets too so it can be \input{}ed.
        # Actually user just wants "kode latex ke dalam file baru". Snippets are fine.
        subprocess.run(['pandoc', tmp_md, '-o', tex_file, '--to=latex', '--wrap=none'])
        os.remove(tmp_md)
        print(f"Converted {md_file} to {tex_file}")
