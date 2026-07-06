from sympy import symbols, pi, pprint, sqrt, Matrix, exp, I, cos, sin
from sympy.physics.quantum import qapply, represent
from sympy.physics.quantum.qubit import Qubit
from sympy.physics.quantum.gate import CNOT, UGate

def RY(target, theta):
    """Mendefinisikan gerbang rotasi Y menggunakan UGate."""
    return UGate((target,), Matrix([
        [cos(theta/2), -sin(theta/2)],
        [sin(theta/2), cos(theta/2)]
    ]))

def RZ(target, theta):
    """Mendefinisikan gerbang rotasi Z menggunakan UGate."""
    return UGate((target,), Matrix([
        [exp(-I*theta/2), 0],
        [0, exp(I*theta/2)]
    ]))

# 0. Inisialisasi State Awal
# State awal |00>
psi_00 = Qubit(0, 0)

def show_gate(gate, label):
    print(f"\n[Gate: {label}]")
    # Representasikan gate sebagai matriks (4x4 untuk 2 qubit)
    mat = represent(gate, nqubits=2)
    pprint(mat.evalf(3))

def apply_yz_rotations(state, theta_y0, theta_z0, theta_y1, theta_z1):
    """
    Menerapkan rotasi RY dan RZ pada qubit 0 dan qubit 1 secara berurutan.
    Serta menampilkan matriks masing-masing gate.
    """
    # Qubit 0
    g_y0 = RY(0, theta_y0)
    show_gate(g_y0, f"RY(q0, theta={theta_y0})")
    state = qapply(g_y0 * state)
    
    g_z0 = RZ(0, theta_z0)
    show_gate(g_z0, f"RZ(q0, theta={theta_z0})")
    state = qapply(g_z0 * state)

    # Qubit 1
    g_y1 = RY(1, theta_y1)
    show_gate(g_y1, f"RY(q1, theta={theta_y1})")
    state = qapply(g_y1 * state)

    g_z1 = RZ(1, theta_z1)
    show_gate(g_z1, f"RZ(q1, theta={theta_z1})")
    state = qapply(g_z1 * state)

    return state

def apply_cnot(state, control, target):
    """
    Menerapkan gerbang CNOT pada state yang diberikan dan menampilkan matriksnya.
    """
    gate_cnot = CNOT(control, target)
    show_gate(gate_cnot, f"CNOT(control={control}, target={target})")
    return qapply(gate_cnot * state)

def show_state(state, label):
    print(f"\n--- {label} ---")
    print("Simbolik:")
    pprint(state)
    print("Vektor State (Numeric):")
    # Representasikan state dalam basis Z (standar)
    try:
        vec = represent(state)
        pprint(vec.evalf(3)) # Tampilkan dengan 3 angka desimal
    except Exception as e:
        print(f"Error dalam representasi: {e}")

show_state(psi_00, "State Awal |00>")

# 2. Contoh: Membuat Bell State |Phi+> 
theta_y0 = pi/2
psi_rotated = apply_yz_rotations(psi_00, theta_y0, 0, 0, 0)
show_state(psi_rotated, "Tahap 1: Rotasi YZ (RY pi/2 pada Q0)")

psi_bell = apply_cnot(psi_rotated, 0, 1)
show_state(psi_bell, "Tahap 2: CNOT(control=0, target=1)")

# 3. Eksperimen: YZ + CNOT lagi pada Bell State
psi_experiment_rotated = apply_yz_rotations(psi_bell, pi, 0, 0, 0)
psi_final = apply_cnot(psi_experiment_rotated, 0, 1)
show_state(psi_final, "Eksperimen: YZ + CNOT lagi pada Bell State")