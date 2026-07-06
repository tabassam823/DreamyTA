import re
import os

allocations = {
    'Bab-2.1.tex': ['shaikh_feature_2025', 'ibrahim_bitcoin_2020', 'jiang_trend_2023', 'yang_abnormal_2024'],
    'Bab-2.2.tex': ['ahmed_international_2017', 'cohen_portfolio_2020', 'innan_quantum_2025'],
    'Bab-2.3.tex': ['ahmadi_dynamics_2023', 'freitas_game_2024', 'mukhopadhyay_analogies_2025'],
    'Bab-2.4.tex': ['kabelac_one-_2021', 'li_ising_2023', 'pagni_one-dimensional_2026', 'reifenstein_coherent_2021', 'datta_relationship_2015', 'schultz_two-dimensional_1964', 'suzuki_spin-_2025'],
    'Bab-2.5.tex': ['purwanto_fisika_2016', 'coyle_quantum_2021', 'feynman_simulating_1981', 'gong_quantum_2025', 'nakahara_quantum_2008', 'padilla_quantum_2025', 'rajak_quantum_2023'],
    'Bab-2.5.2.tex': ['anshu_sample-efficient_2020', 'benedetti_parameterized_2019', 'li_quantum_2025', 'revythi_quantum_2025', 'tomaz_quantum_2025', 'c_scoping_2025'],
    'Bab-2.6.tex': ['fontana_evaluating_2021', 'sharma_noise_2020', 'wierichs_general_2022'],
    'Bab-2.7.tex': ['fedorov_vqe_2022', 'dao_exploring_2025', 'regadio_exoplanet_2025', 'scursulim_multiclass_2026', 'wang_development_2022', 'dixit_variational_2025', 'tilly_variational_2022', 'wang_achieving_2025', 'wei_solving_2025'],
    'Bab-2.8.tex': ['crosato_shannon_2023', 'kumar_family_2025', 'ohya_fundamentals_1998', 'page_information_1993', 'shin_estimating_2024', 'barron_minimum_1991', 'ortiz_marrero_entanglement-induced_2021', 'serafini_symplectic_2003', 'shannon_mathematical_1948']
}

base_dir = '/home/asus/Documents/DreamyTA/Latex/TA/Contents/2_Daster'

for filename, keys in allocations.items():
    filepath = os.path.join(base_dir, filename)
    with open(filepath, 'r') as f:
        content = f.read()

    # Split into paragraphs
    paragraphs = re.split(r'\n\n+', content)
    new_paragraphs = []
    
    key_idx = 0
    for p in paragraphs:
        if key_idx >= len(keys):
            new_paragraphs.append(p)
            continue
            
        # Ignore equations, figures, tables, section headers
        if any(x in p for x in ['\\begin{', '\\end{', '\\[', '\\]', '\\section', '\\subsection', '\\caption']):
            new_paragraphs.append(p)
            continue
            
        # This is a safe text paragraph. Let's find sentences without \cite
        # We split the paragraph by sentences: anything ending in a word character + '.' + space or end of string
        # Let's use a regex to find sentence boundaries and their content.
        # It's easier to iterate over the string and find all '.' that have space/newline/EOF after them.
        
        # We can do this safely by regex matching chunks of text ending in '.'
        sentences = re.split(r'(?<=[a-zA-Z0-9>])\.(\s+|$)', p)
        # re.split with capturing group will return [sentence1, delimiter1, sentence2, delimiter2, ...]
        
        new_p = ""
        i = 0
        while i < len(sentences):
            sent = sentences[i]
            if i + 1 < len(sentences):
                delim = sentences[i+1]
                # Reconstruct
                # If sent does not contain \cite and has some minimum length
                if len(sent.strip()) > 20 and '\\cite' not in sent and key_idx < len(keys):
                    # inject citation
                    new_p += sent + f"~\\cite{{{keys[key_idx]}}}." + delim
                    key_idx += 1
                else:
                    new_p += sent + "." + delim
                i += 2
            else:
                new_p += sent
                i += 1
                
        new_paragraphs.append(new_p)
        
    # Write back
    with open(filepath, 'w') as f:
        f.write('\n\n'.join(new_paragraphs))
        
    print(f"{filename}: Injected {key_idx} out of {len(keys)}")

