# Risk Aversion Endogen: Lagrangian & Game Theory

Dokumen ini menjelaskan konsep **Risk Aversion Endogen** yang diturunkan dari *Lagrangian Multiplier* dan hubungannya dengan matriks payoff dalam *Game Theory*.

## 1. Konsep Dasar

Dalam teori keputusan dan ekonomi, **Risk Aversion** (keengganan terhadap risiko) biasanya dianggap sebagai parameter tetap ($\gamma$). Namun, dalam model **endogen**, tingkat keengganan ini ditentukan oleh kondisi pasar atau lingkungan permainan itu sendiri.

Formula yang digunakan untuk menentukan koefisien risiko pasar ($\lambda_{market}$) adalah:

$$\lambda_{market} = \frac{\sigma_{avg}}{\mu_{avg} + \sigma_{avg}}$$

Di mana:
- $\mu_{avg}$: Rata-rata ekspektasi pengembalian (mean payoff) dari seluruh kemungkinan dalam matriks.
- $\sigma_{avg}$: Rata-rata deviasi standar (volatilitas/risiko) dari matriks payoff.
- $\lambda_{market}$: Koefisien risk aversion yang terbentuk secara alami (endogen).

## 2. Derivasi dari Lagrangian Multiplier

Risk aversion dapat dipandang sebagai *shadow price* (harga bayangan) dari risiko dalam masalah optimasi. Misalkan seorang pemain ingin memaksimalkan utilitas $U$ yang merupakan fungsi dari return ($\mu$) dan risiko ($\sigma$).

### Optimasi Terkendala
Bayangkan masalah optimasi di mana kita ingin memaksimalkan pengembalian dengan batasan risiko tertentu:
$$	\text{Maximize } \mu$$
$$	\text{Subject to: } \sigma \le \sigma_{target}$$

Fungsi Lagrangiannya adalah:
$$L = \mu - \lambda (\sigma - \sigma_{target})$$

Di sini, **$\lambda$** adalah *Lagrangian Multiplier*. $\lambda$ menunjukkan berapa banyak kenaikan $\mu$ yang bersedia dikorbankan untuk menurunkan satu unit $\sigma$. 

### Penentuan Endogen
Dalam kondisi setimbang (equilibrium), $\lambda$ tidak lagi dipilih secara acak, melainkan ditentukan oleh rasio marginal antara risiko dan total potensi nilai ($\mu + \sigma$). 

Jika kita menganggap bahwa pasar menyeimbangkan bobot antara "harapan" ($\mu$) dan "ketidakpastian" ($\sigma$), maka $\lambda$ dapat didefinisikan sebagai proporsi risiko terhadap total nilai agregat:
$$\lambda = \frac{\partial 	\text{Risk}}{\partial (	\text{Return} + 	\text{Risk})} \approx \frac{\sigma_{avg}}{\mu_{avg} + \sigma_{avg}}$$

Interpretasi:
- Jika $\sigma_{avg} 	o 0$, maka $\lambda 	o 0$ (Market menjadi *Risk Neutral*).
- Jika $\sigma_{avg} \gg \mu_{avg}$, maka $\lambda 	o 1$ (Market menjadi sangat *Risk Averse*).

## 3. Implementasi pada Matriks Payoff Game Theory

Dalam *Game Theory*, payoff matrix $A$ merepresentasikan hasil dari strategi pemain.

### Menghitung Komponen
1. **$\mu_{avg}$**: Dihitung dari rata-rata seluruh elemen dalam matriks payoff $A$.
   $$\mu_{avg} = \frac{1}{n \cdot m} \sum_{i=1}^n \sum_{j=1}^m A_{ij}$$
2. **$\sigma_{avg}$**: Dihitung sebagai standar deviasi dari elemen-elemen tersebut, yang merepresentasikan variansi hasil jika strategi dipilih secara acak atau tidak pasti.

### Strategi Pemain
Dengan nilai $\lambda_{market}$ yang sudah diketahui, pemain tidak lagi menggunakan matriks payoff $A$ mentah, melainkan matriks yang sudah disesuaikan dengan risiko (*Risk-Adjusted Payoff*):
$$A'_{ij} = (1 - \lambda_{market}) A_{ij} - \lambda_{market} \sigma_{ij}$$

Atau dalam bentuk yang lebih sederhana, pemain menggunakan $\lambda$ sebagai bobot untuk mencari *Nash Equilibrium* dalam permainan yang memperhatikan volatilitas hasil.

## 4. Kesimpulan

Konsep **Risk Aversion Endogen** ini memberikan keunggulan karena:
1. **Objektif**: Tingkat ketakutan terhadap risiko dihitung langsung dari data (matriks payoff), bukan asumsi subjektif.
2. **Adaptif**: Jika variansi dalam matriks payoff meningkat, maka secara otomatis model akan meningkatkan sensitivitas terhadap risiko ($\lambda$ naik).
3. **Keseimbangan**: Menggunakan *Lagrangian Multiplier* memastikan bahwa trade-off antara return dan risiko berada pada titik optimal secara matematis.
