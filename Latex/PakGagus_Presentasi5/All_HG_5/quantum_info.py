# quantum_info.py
import numpy as np
import scipy.linalg as la

def von_neumann_entropy(rho):
    """Von Neumann entropy S(rho) = -Tr(rho log rho) untuk density matrix diagonal."""
    eig = np.real(la.eigvalsh(rho))
    eig = eig[eig > 1e-12]
    return -np.sum(eig * np.log(eig))


def calc_qmi(st_A, st_B):
    """
    Menghitung Quantum Mutual Information (QMI) antara dua aset:
        I(A:B) = S(rho_A) + S(rho_B) - S(rho_AB)
    
    Density matrix dibangun dari distribusi probabilitas joint biner
    dengan Laplace smoothing (pseudocount +1) untuk stabilitas numerik.
    Sesuai bab10.tex §4 dan Appendix QMI.
    """
    n_ij = np.zeros((2, 2))
    for t in range(len(st_A)):
        n_ij[int(st_A[t]), int(st_B[t])] += 1

    # Distribusi probabilitas joint dengan Laplace smoothing
    prob_joint = (n_ij + 1.0) / (len(st_A) + 4.0)

    # Density matrices marginal dan joint (diagonal → separable basis)
    rho_AB = np.diag(prob_joint.flatten())
    rho_A  = np.diag(prob_joint.sum(axis=1))
    rho_B  = np.diag(prob_joint.sum(axis=0))

    I_QMI = von_neumann_entropy(rho_A) + von_neumann_entropy(rho_B) - von_neumann_entropy(rho_AB)
    return max(I_QMI, 0.0)   # QMI ≥ 0 secara definisi


def compute_coupling_QMI(qmi_val, rho_corr, T_market, k_B=1.0):
    """
    Menghitung kopling informasional J_ij^QMI:
        alpha     = k_B * T_market   (k_B = 1 sesuai konvensi Econophysics)
        J_ij^QMI = alpha * sgn(rho_corr) * sqrt(I_QMI)

    Sesuai bab10.tex §4 (Kopling Informasi melalui Quantum Mutual Information).
    Tanda kopling ditentukan oleh korelasi Pearson empiris rho_corr.
    """
    alpha  = k_B * T_market
    sign   = np.sign(rho_corr) if not np.isnan(rho_corr) else 1.0
    return alpha * sign * np.sqrt(qmi_val)
