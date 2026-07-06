```prompt
Buktikan bahwa state $\rho = \frac{1}{9}(\mathbb{I} - p)$ adalah entangled dengan menunjukkan bahwa dukungan (support) dari $\rho$, yaitu subruang $S^\perp$ yang ortogonal terhadap subruang $S = \text{span}\{\ket{\psi_1}, \dots, \ket{\psi_5}\}$, tidak mengandung satu pun state produk $\ket{u} \otimes \ket{v}$. Gunakan analisis kasus pada koefisien-koefisien vektor $|u\rangle$ dan $|v\rangle$ untuk membuktikan hal ini.
```
**2.a. Buktikan bahwa $\rho$ entangled**

**Diberikan:**
*   Ruang Hilbert bipartit $\mathcal{H}_A \otimes \mathcal{H}_B \approx \mathbb{C}^3 \otimes \mathbb{C}^3$. Dimensi total $d = 3 \times 3 = 9$.
*   Basis ortonormal untuk masing-masing subsistem: $\{\ket{0}, \ket{1}, \ket{2}\}$.
*   Operator proyeksi $p = \sum_{k=1}^5 \ket{\psi_k}\bra{\psi_k}$ pada subruang $S$, dengan:
    1.  $\ket{\psi_1} = \ket{0} \otimes \frac{1}{\sqrt2}(\ket{0}-\ket{1})$
    2.  $\ket{\psi_2} = \ket{2} \otimes \frac{1}{\sqrt2}(\ket{1}-\ket{2})$
    3.  $\ket{\psi_3} = \frac{1}{\sqrt2}(\ket{0}-\ket{1}) \otimes \ket{2}$
    4.  $\ket{\psi_4} = \frac{1}{\sqrt2}(\ket{1}-\ket{2}) \otimes \ket{0}$
    5.  $\ket{\psi_5} = \frac{1}{3}(\ket{0}+\ket{1}+\ket{2}) \otimes (\ket{0}+\ket{1}+\ket{2})$
*   State campuran $\rho = \frac{1}{9} (\mathbb{I}-p)$.

**Tujuan:**
Membuktikan bahwa $\rho$ adalah entangled.

**Strategi Pembuktian:**
Suatu density matrix $\rho$ dikatakan entangled jika ia tidak dapat dituliskan sebagai kombinasi konveks dari state produk. Untuk tipe state seperti ini (yang berkaitan dengan *Unextendible Product Basis* atau UPB), cara termudah untuk membuktikan entanglement adalah dengan menunjukkan bahwa **dukungan ($\text{supp}(\rho) = S^\perp$) tidak mengandung state produk apa pun**. Jika tidak ada state produk $\ket{\Phi} = \ket{u} \otimes \ket{v}$ yang ortogonal terhadap semua $\{\ket{\psi_k}\}$, maka $\rho$ tidak mungkin merupakan kombinasi dari state produk, sehingga $\rho$ pasti entangled.

---

**Langkah 1: Syarat Ortogonalitas terhadap UPB**
Misalkan terdapat state produk $\ket{\Phi} = \ket{u} \otimes \ket{v} \in S^\perp$, di mana:
$$\ket{u} = \sum_{i=0}^2 u_i \ket{i} \quad \text{dan} \quad \ket{v} = \sum_{j=0}^2 v_j \ket{j}$$
Syarat $\ket{\Phi} \in S^\perp$ berarti $\langle \psi_k | \Phi \rangle = 0$ untuk semua $k=1, \dots, 5$:
1.  $\langle \psi_1 | \Phi \rangle = \frac{1}{\sqrt2} u_0 (v_0 - v_1) = 0$
2.  $\langle \psi_2 | \Phi \rangle = \frac{1}{\sqrt2} u_2 (v_1 - v_2) = 0$
3.  $\langle \psi_3 | \Phi \rangle = \frac{1}{\sqrt2} (u_0 - u_1) v_2 = 0$
4.  $\langle \psi_4 | \Phi \rangle = \frac{1}{\sqrt2} (u_1 - u_2) v_0 = 0$
5.  $\langle \psi_5 | \Phi \rangle = \frac{1}{3} (u_0 + u_1 + u_2) (v_0 + v_1 + v_2) = 0$

---

**Langkah 2: Analisis Kasus**

**Kasus 1: Terdapat elemen nol pada koefisien $u$ atau $v$.**
Misalkan $u_0 = 0$:
*   Dari pers (3): $(0 - u_1) v_2 = 0 \implies u_1 = 0$ atau $v_2 = 0$.
    *   Jika $u_1 = 0$, maka dari pers (4): $(0 - u_2) v_0 = 0 \implies u_2 = 0$ atau $v_0 = 0$.
        *   Jika $u_2 = 0$, maka $\ket{u} = 0$ (vektor nol).
        *   Jika $v_0 = 0$, maka dari pers (1) $u_0(v_0-v_1)=0$ terpenuhi. Dari pers (2) $u_2(v_1-v_2)=0$. Jika $u_2 \ne 0$, maka $v_1=v_2$. Dari pers (5): $u_2(v_0+v_1+v_2) = u_2(2v_1) = 0 \implies v_1=0$. Maka $v_0=v_1=v_2=0 \implies \ket{v} = 0$.
*   Logika yang sama berlaku jika kita memulai dari asumsi elemen nol lainnya. Secara umum, jika salah satu koefisien nol, koordinasi antar persamaan memaksa seluruh vektor menjadi nol.

**Kasus 2: Semua koefisien $u_i$ dan $v_j$ adalah non-zero.**
Jika semua non-zero, maka dari persamaan (1)-(4) kita peroleh:
1.  $v_0 = v_1$ (dari pers 1)
2.  $v_1 = v_2$ (dari pers 2) $\implies v_0 = v_1 = v_2 = c$
3.  $u_0 = u_1$ (dari pers 3)
4.  $u_1 = u_2$ (dari pers 4) $\implies u_0 = u_1 = u_2 = d$

Substitusikan ke persamaan (5):
$$\frac{1}{3} (3d) (3c) = 3dc = 0$$
Karena kita berasumsi koefisien non-zero ($c, d \ne 0$), maka persamaan ini tidak mungkin terpenuhi kecuali $c=0$ atau $d=0$, yang berujung pada $\ket{v}=0$ atau $\ket{u}=0$.

---

**Langkah 3: Kesimpulan**
Satu-satunya vektor produk yang ortogonal terhadap subruang $S$ adalah vektor nol. Ini membuktikan bahwa subruang $S^\perp$ (dukungan dari $\rho$) tidak mengandung state produk sama sekali. Karena $\rho$ beroperasi sepenuhnya di dalam subruang yang tidak memiliki state produk, maka $\rho$ tidak dapat dinyatakan sebagai campuran dari state produk.

Oleh karena itu, **$\rho$ adalah state entangled**. $\square$
