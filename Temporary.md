1. penurunan rumus pada pembahasan
2. penurunan rumus entropi pada lampiran A
3. entropi von neumann pada bab 2 dimulai dari entropi shannon saja
4. bab 2 proofread dari belakang aja

# Lampiran
1. Bukti bahwa log return tidak bisa digunakna pada expected return
2. bukti bahwa log return bisa digunakan sebagai standar deviasi matriks kovarians [[1_QuantFinance]]
3. penurunan rumus [[3_Markowitz]]
4. Penurunan rumus EPG [[4_EPG]]
5. Transformasi QUBO dalam bentuk matriks dalam [[5_QUBO]]
6. Bukti gradient descent memenuhi parameter shift rule egitu pula dengan spsa [[7_SPSA]]
7. matriks uniter
8. proses matematis ansatz dalam mencari nilai energi terendah
9. algoritma brute force oracle

$$

\begin{split}

E_{total}(\vec{x}) =& Q_{ii}\left(\frac{1-s_i}{2}\right) + \sum_{i\ne j} Q_{ij} \left(\frac{1-s_i}{2}\right)\left(\frac{1-s_j}{2}\right) -Ak \\

=& \sum_{i=1}^N Q_{ii} \frac{1-s_i}{2} + \sum_{i\ne j} Q_{ij} \frac{1-s_i-s_j+s_is_j}{4} - Ak \\

=& \sum_{i=1}^N \left(\frac{Q_{ii}}{2}\right) - \sum_{i=1}^N \left(\frac{Q_{ii}}{2}\right) (-s_i) + \sum_{i\ne j}\left(\frac{Q_{ij}}{4} \right) \left(1 - s_i - s_j + s_is_j\right) -Ak \\

=& \sum_{i=1}^N \left(\frac{Q_{ii}}{2}\right) + \sum_{i=1}^N \left(\frac{Q_{ii}}{2}\right) s_i + \sum_{i\ne j}\left(\frac{Q_{ij}}{4} \right) - \sum_{i\ne j}\left(\frac{Q_{ij}}{4} \right)s_i - \sum_{i\ne j}\left(\frac{Q_{ij}}{4} \right)s_j + \sum_{i\ne j}\left(\frac{Q_{ij}}{4} \right)s_is_j -Ak \\

=& \sum_{i=1}^N \left(\frac{Q_{ii}}{2} - \sum_{i\ne j}\frac{Q_{ij}}{2} \right)s_i + \sum_{i\ne j}\left(\frac{Q_{ij}}{4} \right)s_is_j + \sum_{i=1}^N \left(\frac{Q_{ii}}{2}\right) + \sum_{i\ne j}\left(\frac{Q_{ij}}{4} \right) - Ak \\

\end{split}

$$

$$
E = \sum_{i=1}^N \left(\frac{Q_{ii}}{2} - \sum_{i\ne j}\frac{Q_{ij}}{2} \right)s_i + \sum_{i\ne j}\left(\frac{Q_{ij}}{4} \right)s_is_j + \sum_{i=1}^N \left(\frac{Q_{ii}}{2}\right) + \sum_{i\ne j}\left(\frac{Q_{ij}}{4} \right) - Ak
$$

$$= \left(\sum_{i=1}^N\frac{\gamma \sigma_i^2}{2K^2} - \sum_{i=1}^N \frac{\mu_i}{K}\right)x_i + \sum_{i\ne j}\frac{\gamma \sigma_{ij}}{2K^2} x_ix_j
$$