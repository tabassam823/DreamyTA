## Iterasi 2 (k = 2)

### Langkah 1 — Hitung $a_k$ dan $c_k$

Karena $k = 2$, step size kini mengecil sesuai decay:

$$a_k = \frac{a}{k^\alpha} = \frac{0.1}{2^{0.602}} = \frac{0.1}{1.5178} = 0.0659$$

$$c_k = \frac{c}{k^\gamma} = \frac{0.1}{2^{0.101}} = \frac{0.1}{1.0725} = 0.0932$$

---

### Langkah 2 — Bangkitkan Vektor Perturbasi $\boldsymbol{\Delta}_2$

$$\boldsymbol{\Delta}_2 = [-1,\ -1]$$

---

### Langkah 3 — Evaluasi Titik Perturbasi

$$\boldsymbol{\theta}^+ = [1.1384,\ 0.4324] + 0.0932 \cdot [-1,\ -1] = [1.0451,\ 0.3392]$$

$$\boldsymbol{\theta}^- = [1.1384,\ 0.4324] - 0.0932 \cdot [-1,\ -1] = [1.2316,\ 0.5257]$$

$$E(\boldsymbol{\theta}^+) = 10\cos(1.0451) + 5\cos(0.3392) = 5.0179 + 4.7151 = 9.7331$$

$$E(\boldsymbol{\theta}^-) = 10\cos(1.2316) + 5\cos(0.5257) = 3.3273 + 4.3249 = 7.6522$$

---

### Langkah 4 — Estimasi Gradien SPSA

$$E^+ - E^- = 9.7331 - 7.6522 = 2.0808$$

$$\hat{g}_1 = \frac{2.0808}{2 \cdot 0.0932 \cdot (-1)} = \frac{2.0808}{-0.1865} = -11.1587$$

$$\hat{g}_2 = \frac{2.0808}{2 \cdot 0.0932 \cdot (-1)} = \frac{2.0808}{-0.1865} = -11.1587$$

> **Catatan:** Karena $\Delta_1 = \Delta_2 = -1$, kedua komponen $\hat{g}$ bernilai sama. Ini menunjukkan efek stokastik SPSA — ketika $\boldsymbol{\Delta}$ seragam, gradien tidak bisa membedakan kontribusi tiap parameter. Gradien analitik sejatinya: $\partial E/\partial\theta_1 = -9.0795$ dan $\partial E/\partial\theta_2 = -2.0954$, sangat berbeda.

---

### Langkah 5 — Update Parameter

$$\boldsymbol{\theta}^{(2)} = \boldsymbol{\theta}^{(1)} - a_k \cdot \hat{\boldsymbol{g}}$$

$$= [1.1384,\ 0.4324] - 0.0659 \cdot [-11.1587,\ -11.1587]$$

$$= [1.1384 + 0.7352,\ 0.4324 + 0.7352] = [1.8735,\ 1.1676]$$

---

## Ringkasan Konvergensi

|Iterasi|$\theta_1$|$\theta_2$|$E(\boldsymbol{\theta})$|Jarak ke −15|
|---|---|---|---|---|
|0|0.7854|0.7854|+10.6066|25.6066|
|1|1.1384|0.4324|+8.7306|23.7306|
|**2**|**1.8735**|**1.1676**|**−1.0197**|**13.9803**|

Energi turun cukup signifikan dari +8.73 ke −1.02, meski konvergensinya jauh lebih lambat dibanding parameter shift rule — ini konsekuensi wajar dari sifat stokastik SPSA yang estimasi gradiennya tidak selalu akurat per iterasi, namun unbiased secara rata-rata jangka panjang.