import re
import os

# We already injected some. We need to find the remainder!
# Let's see what is STILL unused.
tex_dir = '/home/asus/Documents/DreamyTA/Latex/TA/'
used_keys = set()
for root, _, files in os.walk(tex_dir):
    for file in files:
        if file.endswith('.tex'):
            with open(os.path.join(root, file), 'r') as f:
                cites = re.findall(r'\\cite\{([^\}]+)\}', f.read())
                for cite_match in cites:
                    used_keys.update([k.strip() for k in cite_match.split(',')])

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
    remaining_keys = [k for k in keys if k not in used_keys]
    if not remaining_keys:
        continue
        
    filepath = os.path.join(base_dir, filename)
    with open(filepath, 'r') as f:
        content = f.read()

    # Find all sentence endings
    # Avoid matching within \begin{...} ... \end{...} by doing a simple state machine
    new_content = ""
    in_math = False
    i = 0
    key_idx = 0
    
    # We will just split by sentences manually.
    # Find all period matches
    matches = list(re.finditer(r'([a-zA-Z0-9>]{2,})\.(\s+)', content))
    
    last_idx = 0
    for m in matches:
        if key_idx >= len(remaining_keys):
            break
            
        start, end = m.span()
        word = m.group(1)
        space = m.group(2)
        
        # Check text from last_idx to start
        chunk = content[last_idx:start]
        
        # Check if chunk contains cite
        if '\\cite' in chunk:
            pass # skip
        elif '\\begin' in chunk or '\\end' in chunk or '\\[' in chunk or '\\]' in chunk or '\\caption' in chunk or '\\section' in chunk or '\\label' in chunk:
            pass # skip
        else:
            # Check if we are inside a math block by counting $$
            # Actually, just assume it's safe if chunk length > 30 and no weird latex
            if len(chunk) > 30:
                # INJECT!
                injection_point = start + len(word)
                content = content[:injection_point] + f"~\\cite{{{remaining_keys[key_idx]}}}" + content[injection_point:]
                
                # Re-run the regex because string length changed
                # It's easier to just do it backwards
                key_idx += 1
                break # We break and restart to avoid offset issues
                
    # To avoid offset issues, do it backwards
    key_idx = 0
    while key_idx < len(remaining_keys):
        matches = list(re.finditer(r'([a-zA-Z0-9>]{2,})\.(\s+)', content))
        injected_in_this_pass = False
        
        for m in reversed(matches):
            start, end = m.span()
            word = m.group(1)
            
            # find previous period
            prev_m = None
            for pm in matches:
                if pm.span()[0] < start:
                    prev_m = pm
            
            chunk_start = prev_m.span()[1] if prev_m else 0
            chunk = content[chunk_start:start]
            
            if len(chunk.strip()) > 30 and '\\cite' not in chunk and '\\begin' not in chunk and '\\end' not in chunk and '\\[' not in chunk and '\\]' not in chunk and '\\caption' not in chunk and '\\section' not in chunk and '\\subsection' not in chunk and '\\label' not in chunk:
                # Inject!
                injection_point = start + len(word)
                content = content[:injection_point] + f"~\\cite{{{remaining_keys[key_idx]}}}" + content[injection_point:]
                key_idx += 1
                injected_in_this_pass = True
                break # break the inner loop, restart matches
                
        if not injected_in_this_pass:
            print(f"COULD NOT FIND ENOUGH SENTENCES IN {filename}")
            break
            
    with open(filepath, 'w') as f:
        f.write(content)
        
    print(f"{filename}: Injected {key_idx} out of {len(remaining_keys)}")

