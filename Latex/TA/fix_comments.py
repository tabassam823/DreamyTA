import sys

files = {
    'Contents/Lampiran/Lampiran-E.tex': ['2021-01-04', '2022-02-09', '2022-09-21', '2022-12-19', '2023-02-16', '2023-03-17', '2023-07-05', '2023-12-04'],
    'Contents/Lampiran/Lampiran-H.tex': ['2021-04-06', '2021-07-09', '2021-10-11', '2021-11-10', '2022-01-10', '2022-03-14', '2022-04-12', '2022-05-23', '2022-06-23', '2022-08-23', '2022-12-19', '2023-08-04', '2023-09-05', '2023-11-03']
}

for fpath, uncommented_dates in files.items():
    with open(fpath, 'r') as f:
        lines = f.read().splitlines()
        
    new_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        
        if line.startswith(r'\begin{figure}'):
            # scan ahead to find the date
            date_found = None
            temp_i = i
            while temp_i < len(lines) and not lines[temp_i].startswith(r'\end{figure}'):
                if 'caption{Perbandingan Alokasi Portofolio' in lines[temp_i]:
                    date_found = lines[temp_i].split('Jendela Waktu ')[1].split('}')[0].strip()
                    break
                temp_i += 1
                
            # now we know if this figure should be commented
            should_comment = date_found is not None and date_found not in uncommented_dates
            
            # process the figure block
            while i < len(lines):
                l = lines[i]
                if should_comment:
                    if not l.startswith('%'):
                        new_lines.append('% ' + l)
                    else:
                        new_lines.append(l)
                else:
                    new_lines.append(l)
                    
                if l.startswith(r'\end{figure}'):
                    break
                i += 1
        else:
            new_lines.append(line)
            
        i += 1
        
    with open(fpath, 'w') as f:
        f.write('\n'.join(new_lines) + '\n')
        
    print(f'Processed {fpath}')
