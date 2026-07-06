---
name: quantum-curriculum-generator
description: Membangun modul pembelajaran akademik mendalam (Fisika/Ekonofisika) untuk mahasiswa mid-year berdasarkan kurikulum di kurikulum.md. Skill ini mensintesis implementasi kode di GT_Ising_SBR.ipynb dan teori di MD_File/ menjadi draf materi ajar yang formal, matematis, dan sesuai standar publikasi ilmiah.
---

# Quantum Curriculum Module Generator

Skill ini bertugas untuk mengembangkan butir-butir kurikulum di `kurikulum.md` menjadi materi pembelajaran yang komprehensif (Modul). Output yang dihasilkan wajib mengikuti standar penulisan di `GEMINI.md` (Persona: Penulis Jurnal Ilmiah Senior).

## Workflow Inti

1. **Topik Selection**: Identifikasi modul mana dari `kurikulum.md` yang akan dibuat (misal: Modul 5: VQE).
2. **Code Mapping**: Cari implementasi teknis terkait di `GT_Ising_SBR.ipynb`. Perhatikan label komentar seperti `[Tugas 1]`, `[Tugas 5]`, dll.
3. **Theory Search**: Cari file referensi pendukung di direktori `MD_File/` yang relevan dengan topik tersebut (misal: `SPSA.md`, `Variational_Principle.md`).
4. **Synthesis & Writing**:
    - **Persona**: Tulis dengan gaya akademis yang lugas, objektif, dan teknis.
    - **Struktur**: Minimal 2 paragraf per subbab, 4-5 kalimat per paragraf.
    - **Matematika**: Sertakan derivasi LaTeX yang bersih dengan indeks nomor persamaan (1), (2), dst.
    - **Bahasa**: Gunakan Bahasa Indonesia formal, dengan istilah teknis (*technical terms*) dalam Bahasa Inggris yang dicetak *italic*.

## Standar Konten Per Modul

Setiap modul harus mencakup komponen berikut:

### 1. Urgensi & Konteks Fisika
Jelaskan mengapa algoritma/konsep tersebut penting dalam sistem portofolio kuantum. Gunakan logika deduktif untuk konsep baru atau induktif untuk hal yang umum.

### 2. Formalisme Matematis & Algoritma
Turunkan persamaan utama dengan rigoritas tinggi. Hubungkan variabel fisik (misal: Hamiltonian Ising) dengan variabel finansial (misal: Risk-Return Markowitz). Gunakan `MD_File/` sebagai rujukan utama kedalaman matematis.

**Mandat Penurunan Rumus:**
- **Eksplisit & Berurutan**: Jangan melompati langkah aljabar. Mahasiswa diasumsikan memerlukan bantuan penuh dalam transisi antar baris persamaan.
- **Justifikasi Matematis**: Setiap transisi variabel (misal: substitusi, integrasi, atau transformasi Pauli) wajib diberikan penjelasan logis/fisik di antara baris-baris rumus.
- **Pembuktian Validitas**: Sertakan pembuktian singkat mengapa model tersebut valid (misal: membuktikan ekuivalensi fungsi objektif dengan energi Hamiltonian, atau membuktikan normalisasi state).
- **Indeks Persamaan**: Gunakan format `$$ ... $$` dengan nomor persamaan di kanan, misal: `(1)`, `(2)`, dst.

### 3. Implementasi Teknis (Code Breakdown)
Jelaskan logika fungsi di `GT_Ising_SBR.ipynb`. Contoh: bagaimana fungsi `run_vqe_adaptive` bekerja atau bagaimana `NMI` dihitung secara numerik. Sertakan saran visualisasi/grafik yang relevan (Gambar).

### 4. Analisis Konvergensi & Hasil
Berikan panduan cara menginterpretasi output (misal: grafik energi vs iterasi SPSA).

## Referensi File Penting
- `kurikulum.md`: Struktur silabus.
- `GT_Ising_SBR.ipynb`: Source code dan data simulasi.
- `MD_File/*.md`: Dasar teori (SPSA, Variational, Hamiltonian, dll).
- `GEMINI.md`: Mandat gaya bahasa dan tipografi.

## Contoh Trigger
- "Buatkan materi lengkap untuk Modul 2 berdasarkan kurikulum."
- "Jelaskan bab VQE (Modul 5) dengan merujuk pada kode dan file SPSA.md."
- "Kembangkan draf Modul 1 dengan gaya bahasa jurnal ilmiah."
