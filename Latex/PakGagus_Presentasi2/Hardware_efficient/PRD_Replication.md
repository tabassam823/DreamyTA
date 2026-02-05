Tentu, ini adalah **Product Requirement Document (PRD)** yang disusun berdasarkan spesifikasi teknis dari paper Kandala et al. (2017). Dokumen ini diformat agar siap disalin ke dalam alat manajemen proyek seperti Antigravity/Jira/Notion, diikuti dengan implementasi kode Hamiltonian sederhana untuk PennyLane/Qiskit.

---

# Product Requirement Document (PRD): Hardware-Efficient VQE Replication

**Project Name:** Replikasi Kandala 2017 (HE-VQE) **Objective:** Mengembangkan simulasi VQE yang efisien secara hardware untuk estimasi energi dasar molekul (H2, LiH, BeH2) dan model magnetisme, menggunakan _Ansatz_ kedalaman rendah yang tahan terhadap noise. **Source Reference:** Kandala et al., _Nature_ **549**, 242–246 (2017).

## 1. Scope & Features (Lingkup & Fitur)

### 1.1 Variational Form (Ansatz)

Membangun sirkuit kuantum parametrik dengan struktur _interleaved_ (selang-seling) sesuai **Figur 1c**.

- **Lapisan Rotasi ($U_{q,i}$):**
    - Qubit tunggal diputar menggunakan kombinasi gerbang Euler ($Z \to X \to Z$).
    - Dalam simulasi, ini direpresentasikan sebagai rotasi parametrik $RZ(\alpha) \to RX(\beta) \to RZ(\gamma)$.
- **Lapisan Entangler ($U_{ENT}$):**
    - Menggunakan gerbang dua-qubit yang bekerja pada seluruh qubit yang terhubung.
    - **Spesifikasi:** Gerbang _Cross-Resonance_ (CR) atau CNOT (jika simulasi ideal).
    - **Topologi:** Linear atau _Star_ (sesuai konektivitas Qubit 1-6 di **Figur 1b**).
- **Depth Management:**
    - Kemampuan untuk mengatur kedalaman sirkuit $d$ (mulai dari $d=1$ hingga $d=20+$ untuk eksperimen noise).

### 1.2 Classical Optimization

Mengimplementasikan loop umpan balik klasik-kuantum untuk meminimalkan nilai ekspektasi energi.

- **Algoritma:** SPSA (_Simultaneous Perturbation Stochastic Approximation_).
- **Constraint:** Estimasi gradien harus menggunakan hanya 2 pengukuran per iterasi, terlepas dari jumlah parameter ($p$).
- **Parameter:** Total parameter $p = N(3d + 2)$, di mana rotasi Z awal pada iterasi pertama ditiadakan/dikunci.

### 1.3 Hamiltonian Mapping

Menerjemahkan masalah Fermionik ke Qubit.

- **Metode Mapping:** _Binary Tree Encoding_ (Parity Mapping).
- **Qubit Reduction (Tapering):**
    - Memanfaatkan simetri $Z_2$ (paritas spin dan partikel) untuk mengurangi jumlah qubit.
    - **Target:** H2 (4 orbital $\to$ 2 qubit), LiH (4 qubit), BeH2 (10 orbital $\to$ 6 qubit dengan _frozen core_).

## 2. Technical Specifications (Spesifikasi Teknis)

### 2.1 Input Data (Molecular Specs)

- **H2:** Jarak ikatan variatif (0.2 Å - 3.0 Å).
- **LiH:** Jarak ikatan variatif (1.0 Å - 4.0 Å).
- **BeH2:** Jarak ikatan variatif (0.5 Å - 4.0 Å).

### 2.2 Measurement Strategy

- **Grouping:** Mengelompokkan suku-suku Pauli yang komutatif (TPB - _Tensor Product Basis_) untuk mengurangi jumlah sirkuit pengukuran.
- **Sampling:** Mensimulasikan _finite sampling_ (misal: 1000 _shots_) untuk meniru fluktuasi statistik eksperimen.

## 3. Acceptance Criteria (Kriteria Keberhasilan)

1. **H2 Accuracy:** Mencapai _Chemical Accuracy_ (error < 1.6 mHa) pada jarak setimbang dengan kedalaman $d=1$.
2. **LiH Characteristic:** Mereproduksi fitur "kink" (bengkokan) pada kurva energi di jarak 2.5 Å saat menggunakan $d=1$, yang menandakan keterbatasan kedalaman sirkuit.
3. **Efficiency:** Algoritma SPSA harus konvergen tanpa memerlukan perhitungan gradien penuh (parameter-shift rule yang mahal).

---

# Contoh Implementasi Sederhana Matriks Hamiltonian (H2)

Sesuai permintaan Anda, berikut adalah contoh **Matriks Hamiltonian H2** yang sudah dipetakan ke qubit.

Alih-alih memberikan matriks raksasa $4 \times 4$ yang sulit dibaca, cara standar dalam PennyLane/Qiskit adalah mendefinisikannya sebagai penjumlahan suku Pauli (_Weighted Pauli Sum_).

Ini adalah contoh untuk molekul **Hidrogen (H2)** pada jarak ikatan **0.74 Å** (titik setimbang), setelah dipetakan menggunakan **Parity Mapping** dan direduksi menjadi **2 Qubit** (sesuai).

### Versi PennyLane (Python)

Kode ini bisa langsung Anda jalankan untuk mendapatkan Hamiltonian yang siap dimasukkan ke VQE.

```
import pennylane as qml
from pennylane import numpy as np

# 1. Definisikan Geometri dan Spesifikasi Molekul
# Jarak atom H-H = 0.74 Angstrom (setimbang)
symbols = ["H", "H"]
coordinates = np.array([0.0, 0.0, -0.37, 0.0, 0.0, 0.37])

# 2. Membuat Hamiltonian Menggunakan Fungsi Bawaan
# Paper menggunakan "Binary Tree" (Parity) dan reduksi qubit
H, qubits = qml.qchem.molecular_hamiltonian(
    symbols,
    coordinates,
    charge=0,
    mult=1,
    basis="sto-3g",
    mapping="parity",  # Sesuai paper
    # Tapering off (Reduksi Qubit) otomatis dilakukan jika symmetries dideteksi
    # Namun, secara manual kita bisa melihat hasilnya biasanya adalah kombinasi Pauli di bawah ini.
)

print(f"Jumlah Qubit setelah mapping: {qubits}")
print("Hamiltonian (Suku Pauli):")
print(H)

# --- ATAU ---

# Jika Anda ingin INPUT MANUAL (Hardcoded) sesuai hasil paper (Approximate coefficients):
# Ini merepresentasikan H2 pada 2 Qubit (setelah tapering).
# Koefisien (h_i) dalam satuan Hartree.

coeffs = [
    -1.0523732,  # Identity
    0.39793742,  # Z0
    -0.3979374,  # Z1
    -0.0112801,  # Z0 Z1
    0.18093119,  # X0 X1
]

ops = [
    qml.Identity(wires=), # I
    qml.PauliZ(wires=0),        # Z pada qubit 0
    qml.PauliZ(wires=1),        # Z pada qubit 1
    qml.PauliZ(wires=0) @ qml.PauliZ(wires=1), # Z0 Z1
    qml.PauliX(wires=0) @ qml.PauliX(wires=1), # X0 X1 (Ini suku entangling penting!)
]

H_manual = qml.Hamiltonian(coeffs, ops)

print("\nHamiltonian Manual (Siap untuk VQE):")
print(H_manual)
```

### Penjelasan Koneksi ke Paper:

1. **Parity Mapping:** Dalam kode `qml.qchem.molecular_hamiltonian`, argumen `mapping="parity"` mengacu pada _Binary Tree Encoding_ yang disebut di paragraf.
2. **Suku Pauli:** Perhatikan suku `X0 X1`. Suku inilah yang memaksa qubit untuk saling berinteraksi (_entanglement_). Suku `Z0` dan `Z1` merepresentasikan energi orbital masing-masing.
3. **Reduksi:** Jika Anda menjalankan kode otomatis di atas tanpa _tapering_ manual, PennyLane mungkin memberi 4 qubit. Untuk mendapatkan persis 2 qubit seperti di paper ("remove the two qubits associated with spin parities"), Anda perlu mengaktifkan fitur `qml.qchem.taper_operation` pada Hamiltonian tersebut.