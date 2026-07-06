# Deep Dive: The Chain Store Paradox (Bab 8)
*Berdasarkan referensi dari "Bayesian Games: Games of Incomplete Information" oleh Meryl Seah.*

---

## 1. Masalah Chain Store (The Chain Store Problem)

**Skenario:**
- **Pemain:** 
  1. Satu **Monopolist** (Penguasa Pasar).
  2. Sejumlah $T$ **Entrants** (Penantang) yang akan memutuskan untuk masuk pasar satu per satu secara berurutan.
- **Tipe Monopolist:**
  - **Strong (S):** Monopolist Kuat.
  - **Weak (W):** Monopolist Lemah.
- **Informasi:** 
  - Hanya Monopolist yang tahu tipenya sendiri (Private Information).
  - Entrant hanya tahu probabilitas awal ($q > 0$) bahwa Monopolist adalah tipe **Strong**.

### Payoff (Imbalan)
Jika Entrant memutuskan masuk (*Enter*), Monopolist bisa memilih:
- **Fight (Lawan):** Perang harga.
- **Yield (Menyerah):** Biarkan masuk.

**Struktur Payoff:**
- Jika Entrant **Stay Out (Tidak Masuk):**
  - Entrant: 0
  - Monopolist: $a > 1$
- Jika Entrant **Enter** dan Monopolist **Yield**:
  - Entrant: $\beta$ (dimana $0 < \beta < 1$)
  - Monopolist (Strong): -1
  - Monopolist (Weak): 0
- Jika Entrant **Enter** dan Monopolist **Fight**:
  - Entrant: $\beta - 1$
  - Monopolist (Strong): 0
  - Monopolist (Weak): -1

> **Catatan:** Monopolist Kuat *lebih suka* bertarung (0) daripada menyerah (-1). Monopolist Lemah *lebih suka* menyerah (0) daripada bertarung (-1).

---

## 2. Dinamika Belief (Kepercayaan $q_t$)

Setiap Entrant ke-$t$ memiliki keyakinan $q_t(h_{t-1})$ bahwa Monopolist adalah tipe **Strong** berdasarkan sejarah kejadian sebelumnya ($h_{t-1}$).

**Aturan Update Belief ($q_t$):**

1. **Jika tidak ada yang masuk pada $t-1$:**
   Tidak ada informasi baru, belief tetap: $q_t = q_{t-1}$.

2. **Jika ada yang masuk, dan Monopolist Melawan (Fight):**
   - Jika $q_{t-1} > 0$, maka belief diupdate menjadi:
     $$ q_t = \max\{\beta^{T-t+1}, q_{t-1}\} $$
   *Logika: Melihat perlawanan meningkatkan atau mempertahankan keyakinan bahwa Monopolist kuat.*

3. **Jika ada yang masuk, dan Monopolist Menyerah (Yield):**
   - Maka $q_t = 0$.
   *Logika: Monopolist Kuat tidak akan pernah menyerah (karena payoff yield = -1, fight = 0). Jadi jika menyerah, pasti dia Lemah.*

---

## 3. Strategi Pemain

### Strategi Monopolist
1. **Tipe Strong:** Selalu **Fight** (Lawan) jika ada yang masuk.
2. **Tipe Weak:**
   - Jika $t = T$ (ronde terakhir): **Yield**.
   - Jika $t < T$ dan belief Entrant tinggi ($q_t > \beta^{T-t}$): **Fight**.
   - Jika $t < T$ dan belief Entrant rendah ($q_t < \beta^{T-t}$): **Fight** dengan probabilitas campuran (mixing strategy):
     $$ \frac{(1 - \beta^{T-t})q_t}{(1-q_t)\beta^{T-t}} $$

### Strategi Entrant (Penantang ke-$t$)
Keputusan bergantung pada belief $q_t$ dibandingkan dengan threshold $\beta^{T-t+1}$:
1. **Jika $q_t > \beta^{T-t+1}$:** **Stay Out** (Takut dilawan).
2. **Jika $q_t < \beta^{T-t+1}$:** **Enter** (Berani masuk).
3. **Jika $q_t = \beta^{T-t+1}$:** **Stay Out** dengan probabilitas $1/\alpha$ (indifferent).

---

## 4. Pembuktian Sequential Equilibrium

Bagian ini membuktikan bahwa strategi dan belief di atas membentuk *Sequential Equilibrium*.

### Lemma 8.2 (Induksi Mundur / Backwards Induction)
Untuk setiap periode $t \in \{1, ..., T\}$:
1. Jika $q_t < \beta^{T-t+1}$: Total *expected payoff* Monopolist Lemah dari titik ini adalah 0.
2. Jika $q_t \ge \beta^{T-t+1}$: Total *expected payoff* Monopolist Lemah dari titik ini adalah 1.

*Bukti dilakukan dengan induksi mundur mulai dari $t=T$ hingga $t=1$.*

### Theorem 8.3
Strategi di atas membentuk **Sequential Equilibrium**.

**Bukti Konsistensi (Consistency):**
- Menggunakan **Bayes' Rule** untuk mengupdate belief di jalur permainan yang mungkin terjadi (*on-path*).
- Rumus update belief (Persamaan 8.5) menunjukkan bagaimana probabilitas dihitung saat Monopolist Lemah melakukan *bluffing* (menggertak/melawan).
  $$ q_{t+1} = \frac{q_t}{q_t + (1-q_t)\sigma_W(Fight)} $$

**Penanganan "Off-path" Beliefs:**
- Situasi di mana Bayes' Rule tidak berlaku (misal: probabilitas kejadian 0).
- Contoh: Jika $q_t$ sudah 0 (yakin lemah), tapi tiba-tiba Monopolist melawan.
- Makalah ini menangani hal tersebut dengan mendefinisikan "kesalahan" (*trembling hand*) yang konvergen ke 0, memastikan belief tetap terdefinisi secara konsisten.

**Bukti Rasionalitas Sekuensial (Sequential Rationality):**
- Menunjukkan bahwa di setiap titik keputusan, strategi yang dipilih adalah *Best Response* terhadap strategi lawan dan belief saat ini.
- Entrant masuk hanya jika *expected payoff* positif (risiko dilawan cukup kecil).
- Monopolist Lemah melawan di awal permainan untuk membangun reputasi ("Saya Kuat") agar Entrant masa depan takut masuk, sehingga ia bisa mendapatkan payoff monopoli ($a$) di masa depan.

