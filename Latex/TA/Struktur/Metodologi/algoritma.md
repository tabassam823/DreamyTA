# Algoritma Portofolio Kuantum HE-VQE (Kombinasi 4)

Dokumen ini menjelaskan alur logika sistem optimasi portofolio yang menggabungkan **Ekonofisika**, **Game Theory**, dan **Variational Quantum Eigensolver (VQE)**.

## 1. Pseudocode

```text
Algorithm 1: Portfolio Optimization via HE-VQE
1 function optimize_portfolio (Tickers, Capital, K, Window, Period);
  Input: Tickers LQ45, Initial Capital, Target assets K, Sliding Window size, Rebalance Frequency
  Output: Equity Curve and Performance Metrics
2 Unduh data historis harga penutupan P_t untuk semua Tickers;
3 Hitung Log Return R_t = ln(P_t / P_{t-1});
4 Diskretisasi status biner: |0⟩ jika R_t > 0, |1⟩ jika R_t ≤ 0;
5 for each rebalance period do
6 |   Hitung Probabilitas Gabungan P(s_i, s_j) dari data window;
7 |   for each asset pair (i, j) do
8 |   |   Hitung Matriks Payoff 2x2 dari return historis rata-rata;
9 |   |   Klasifikasi tipe permainan (Coordination/Anti-Coordination/Mixed);
10|   |   Hitung interaksi J_ij melalui Quantum Mutual Information (QMI);
11|   end
12|   Hitung bias h_i dari selisih expected payoff marginal;
13|   Konstruksi Hamiltonian Ising H = H_cost + H_penalty;
14|   Inisialisasi Hardware-Efficient Ansatz dengan parameter θ;
15|   while not converged or iter < maxiter do
16|   |   Estimasi gradien sirkuit menggunakan optimasi SPSA;
17|   |   Update parameter θ = θ - η∇E;
18|   end
19|   Ambil bitstring dengan probabilitas tertinggi yang memenuhi Hamming Weight = K;
20|   Eksekusi Rebalancing (Jual/Beli) dan hitung biaya transaksi;
21|   Update nilai ekuitas harian;
22 end
23 Hitung metrik performa (Sharpe Ratio, Max Drawdown, Total Return);
24 return Equity_Curve, Performance_Metrics
```

## 2. Diagram Alir (Mermaid)

```mermaid
graph TD
    subgraph "A. Tahap Data"
        A1[Data Saham LQ45] --> A2[Hitung Log Return]
        A2 --> A3[Binerisasi Status: 0=Naik, 1=Turun]
    end

    subgraph "B. Analisis Ekonofisika & Game Theory"
        A3 --> B1[Sliding Window 126 Hari]
        B1 --> B2[Hitung Probabilitas Gabungan P_ij]
        B2 --> B3[Matriks Payoff 2x2 (Return Historis)]
        B3 --> B4[Hitung Bias h_i & Klasifikasi Game]
        B1 --> B5[Hitung J_ij via Quantum Mutual Information]
    end

    subgraph "C. Optimasi Kuantum (HE-VQE)"
        B4 & B5 --> C1[Konstruksi Hamiltonian Ising]
        C1 --> C2[Hardware-Efficient Ansatz]
        C2 --> C3[Loop Optimasi SPSA]
        C3 --> C4{Konvergen?}
        C4 -- Tidak --> C3
        C4 -- Ya --> C5[Probabilistic Sampling]
        C5 --> C6[Seleksi Bitstring K-Aset]
    end

    subgraph "D. Rebalancing & Performa"
        C6 --> D1[Eksekusi Jual/Beli & Biaya Transaksi]
        D1 --> D2[Update Nilai Ekuitas Harian]
        D2 --> D3{Selesai Periode?}
        D3 -- Tidak --> B1
        D3 -- Ya --> D4[Hasil: Sharpe Ratio, MDD, Kurva Ekuitas]
    end
```
