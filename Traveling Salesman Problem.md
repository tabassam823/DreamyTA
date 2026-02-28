Kita menggunakan rasio _Risk-Adjusted Return_ (mirip _Sharpe Ratio_ tanpa _risk-free rate_) yaitu $Z = \frac{\mu_{avg}}{\sigma_{avg}}$, lalu memasukkannya ke fungsi Sigmoid:

$$\lambda = \frac{1}{1 + e^{Z}} = \frac{1}{1 + \exp\left(\frac{\mu_{avg}}{\sigma_{avg}}\right)}$$

**Bagaimana ini menyelesaikan masalah?**

1. **Pasar Positif ($\mu > 0$):** Misal $\mu = 0.10, \sigma = 0.05 \rightarrow Z = 2$.
    
    $\lambda = \frac{1}{1 + e^2} \approx \frac{1}{1 + 7.38} \approx 0.12$.
    
    _(Investor menjadi agresif / risk-seeking karena pasar sedang menguntungkan)._
    
2. **Pasar Negatif ($\mu < 0$):** Misal $\mu = -0.10, \sigma = 0.05 \rightarrow Z = -2$.
    
    $\lambda = \frac{1}{1 + e^{-2}} \approx \frac{1}{1 + 0.135} \approx 0.88$.
    
    _(Investor menjadi sangat defensif / risk-averse karena pasar sedang rugi, namun nilai tetap di bawah 1)._
    
3. **Pasar Stagnan ($\mu = 0$):** $\lambda = \frac{1}{1 + 1} = 0.50$.
    
    _(Kondisi netral seimbang sempurna)._
    

### Solusi 2: Metode _Clipping_ (Asumsi Penghindaran Risiko Absolut)

Jika Anda ingin model yang lebih sederhana dan mencerminkan "Kepanikan Pasar" (_Market Panic_), kita bisa menggunakan fungsi `Max` untuk mencegah pembagi menjadi lebih kecil dari $\sigma$.

$$\lambda = \frac{\sigma_{avg}}{\max(0, \mu_{avg}) + \sigma_{avg}}$$

**Bagaimana ini bekerja?**

- Jika rata-rata return positif ($\mu > 0$), rumusnya beroperasi normal seperti ide awal kita: $\frac{\sigma}{\mu + \sigma}$. (Misal $\mu=0.05, \sigma=0.15 \rightarrow \lambda = 0.75$).
    
- Jika rata-rata return negatif ($\mu < 0$), fungsi $\max(0, \mu)$ akan mengubah nilai $\mu$ menjadi $0$. Rumusnya menjadi $\frac{\sigma}{0 + \sigma} = 1$.
    
- **Implikasi Fisis:** Ini berarti ketika ekspektasi keuntungan pasar bernilai negatif, algoritma mengasumsikan investor beralih ke mode **"Risk Aversion Maksimal" ($\lambda = 1$)**. Dalam matriks payoff, utilitas hanya akan dikalkulasi murni berdasarkan minimasi risiko ($U = -\sigma$), karena tidak ada harapan keuntungan yang bisa diharapkan dari pasar yang sedang anjlok.
    

**Saran Penerapan:**

Untuk tesis atau paper penelitian yang melibatkan komputasi kuantum dan _Game Theory_, **Solusi 1 (Fungsi Sigmoid)** akan terlihat jauh lebih kuat secara analitis. Ia memberikan gradasi _risk aversion_ yang mulus dan menangkap psikologi _loss aversion_ dengan formulasi fisika statistik yang solid.