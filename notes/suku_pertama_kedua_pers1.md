# 1. Definisi varians

Varians dari variabel acak (X) adalah

$$  
\text{Var}(X) = \mathbb{E}[(X - \mathbb{E}[X])^2]  
$$

Misalkan

$$  
X = x_1R_1 + x_2R_2  
$$

maka
$$
\text{Var}(x_1R_1 + x_2R_2)
=
\mathbb{E}  
\left[  
(x_1R_1 + x_2R_2 - \mathbb{E}[x_1R_1 + x_2R_2])^2  
\right]  
$$

---

# 2. Gunakan linearitas ekspektasi

Ekspektasi bersifat linear
$$
\mathbb{E}[x_1R_1 + x_2R_2]
=
x_1\mathbb{E}[R_1] + x_2\mathbb{E}[R_2]  
$$

misalkan

$$ 
\mu_1 = \mathbb{E}[R_1], \qquad \mu_2 = \mathbb{E}[R_2]  
$$
Di mana 
$$ \begin{split}
\mathbb{E}(R) &= \mathbb{E} \left[\frac{P_n(t) - P_n(t-1)}{P_n(t-1)}\right] \\\\
\mathbb{E}(R) &\approx \frac{1}{T}\sum_{t=1}^T \left[\frac{P_n(t) - P_n(t-1)}{P_n(t-1)}\right]
\end{split}
$$
maka

$$  
\text{Var}(x_1R_1 + x_2R_2)
=
\mathbb{E}  
\left[  
(x_1(R_1-\mu_1) + x_2(R_2-\mu_2))^2  
\right]  
$$

---

# 3. Kembangkan kuadrat

Gunakan identitas

$$  
(a+b)^2 = a^2 + b^2 + 2ab  
$$

maka

$$
(x_1(R_1-\mu_1) + x_2(R_2-\mu_2))^2  
$$

menjadi

$$  
x_1^2(R_1-\mu_1)^2  
+  
x_2^2(R_2-\mu_2)^2  
+  
2x_1x_2(R_1-\mu_1)(R_2-\mu_2)  
$$

---

# 4. Ambil ekspektasi

Sekarang kita ambil ekspektasi dari masing-masing suku

$$
\text{Var}(x_1R_1 + x_2R_2)
=
x_1^2\mathbb{E}[(R_1-\mu_1)^2]  
+  
x_2^2\mathbb{E}[(R_2-\mu_2)^2]  
+  
2x_1x_2\mathbb{E}[(R_1-\mu_1)(R_2-\mu_2)]  
$$

---

# 5. Gunakan definisi varians dan kovarians

### Varians

$$  
\sigma_1^2 = \text{Var}(R_1) = \mathbb{E}[(R_1-\mu_1)^2]  
$$

$$  
\sigma_2^2 = \text{Var}(R_2) = \mathbb{E}[(R_2-\mu_2)^2]  
$$

### Kovarians

$$ 
\sigma_{12} =  
\text{Cov}(R_1,R_2)
=
\mathbb{E}[(R_1-\mu_1)(R_2-\mu_2)]  
$$

---

# 6. Substitusi

Masukkan ke persamaan sebelumnya
$$  
\text{Var}(x_1R_1 + x_2R_2)
=
x_1^2\sigma_1^2  
+  
x_2^2\sigma_2^2  
+  
2x_1x_2\sigma_{12}  
$$

---

# 7. Interpretasi (sangat penting di finance)

Jika ($R_1$, $R_2$) adalah **return dua aset** dan ($x_1$, $x_2$) adalah **bobot portofolio**, maka

$$  
\text{Var}(R_p)  
$$

adalah **risiko portofolio**.

Komponennya:

1️⃣ **($x_1^2\sigma_1^2$)** → risiko aset 1  
2️⃣ **($x_2^2\sigma_2^2$)** → risiko aset 2  
3️⃣ **($2x_1x_2\sigma_{12}$)** → interaksi korelasi antar aset

Justru **term ketiga ini yang membuat diversifikasi bekerja**.

Jika

- kovarians negatif → risiko turun
    
- kovarians positif → risiko naik
    

---

# 8. Bentuk matriks (yang sering dipakai di portfolio theory)

Persamaan ini bisa ditulis lebih elegan:
$$  
\text{Var}(R_p)
=
\mathbf{x}^T  
\Sigma  
\mathbf{x}  
$$

dengan

$$
\mathbf{x} =  
\begin{bmatrix}  
x_1 \\  
x_2  
\end{bmatrix}  $$

dan matriks kovarians

$$
\Sigma =  
\begin{bmatrix}  
\sigma_1^2 & \sigma_{12} \\  
\sigma_{12} & \sigma_2^2  
\end{bmatrix}  
$$
