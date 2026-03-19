# hamiltonian.py
import pennylane as qml

def build_hamiltonian_total(h_total, J_total, n_assets):
    """
    Membangun operator Hamiltonian Ising dari parameter TOTAL yang sudah
    menggabungkan kontribusi Game Theory dan Penalty:
        H = sum_i h_total[i] * Z_i + sum_{i<j} J_total[i,j] * Z_i Z_j

    Parameter h_total dan J_total sudah mengandung:
        h_total[i]   = h_i^GT   + h_i^pen
        J_total[i,j] = J_ij^QMI + J_ij^pen

    Sesuai bab10.tex §5 (Sintesis Hamiltonian Akhir).
    """
    coeffs = []
    obs    = []

    # Suku linear: h_i * Z_i
    for i in range(n_assets):
        if abs(h_total[i]) > 1e-10:
            coeffs.append(float(h_total[i]))
            obs.append(qml.PauliZ(i))

    # Suku kuadratik: J_ij * Z_i Z_j
    for i in range(n_assets):
        for j in range(i + 1, n_assets):
            if abs(J_total[i, j]) > 1e-10:
                coeffs.append(float(J_total[i, j]))
                obs.append(qml.PauliZ(i) @ qml.PauliZ(j))

    # Fallback agar Hamiltonian tidak kosong
    if len(coeffs) == 0:
        coeffs.append(0.0)
        obs.append(qml.Identity(0))

    return qml.Hamiltonian(coeffs, obs)
