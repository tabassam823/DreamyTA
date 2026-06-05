dates = [
    '2021-01-04', '2021-02-02', '2021-03-04', '2021-04-06', '2021-05-05',
    '2021-06-10', '2021-07-09', '2021-08-10', '2021-09-10', '2021-10-11',
    '2021-11-10', '2021-12-09', '2022-01-10', '2022-02-09', '2022-03-14',
    '2022-04-12', '2022-05-23', '2022-06-23', '2022-07-22', '2022-08-23',
    '2022-09-21', '2022-10-20', '2022-11-18', '2022-12-19', '2023-01-17',
    '2023-02-16', '2023-03-17', '2023-04-27', '2023-05-30', '2023-07-05',
    '2023-08-04', '2023-09-05', '2023-10-05', '2023-11-03', '2023-12-04'
]

content_h = [
    r'\chapter{Visualisasi Perbandingan Alokasi Portofolio N=4 (GT vs No-GT)}',
    r'\label{appendix:window_analysis_n4}',
    '',
    r'Penampil grafik alokasi aset pada setiap jendela waktu (\textit{rolling window}) untuk sistem dengan $N=4$ aset, membandingkan pengaruh model \textit{Game Theory} terhadap keputusan investasi.',
    ''
]

for date in dates:
    fig_str = (
        r'\begin{figure}[!htbp]' + '\n' +
        r'    \centering' + '\n' +
        r'    \begin{subfigure}[b]{0.48\textwidth}' + '\n' +
        r'        \centering' + '\n' +
        r'        \includegraphics[width=\textwidth]{GTQuantumInvest/Hasil_N4_GT/Analisis_Window_N4/' + date + r'_window.png}' + '\n' +
        r'        \caption{Dengan \textit{Game Theory}}' + '\n' +
        r'    \end{subfigure}' + '\n' +
        r'    \hfill' + '\n' +
        r'    \begin{subfigure}[b]{0.48\textwidth}' + '\n' +
        r'        \centering' + '\n' +
        r'        \includegraphics[width=\textwidth]{GTQuantumInvest/Hasil_N4_NoGT/Analisis_Window_N4/' + date + r'_window.png}' + '\n' +
        r'        \caption{Tanpa \textit{Game Theory}}' + '\n' +
        r'    \end{subfigure}' + '\n' +
        r'    \caption{Perbandingan Alokasi Portofolio N=4 Jendela Waktu ' + date + '}' + '\n' +
        r'    \label{fig:window_n4_' + date.replace('-', '_') + '}' + '\n' +
        r'\end{figure}' + '\n'
    )
    content_h.append(fig_str)

with open('Contents/Lampiran/Lampiran-H.tex', 'w') as f:
    f.write('\n'.join(content_h))

print("Lampiran-H generated successfully.")
