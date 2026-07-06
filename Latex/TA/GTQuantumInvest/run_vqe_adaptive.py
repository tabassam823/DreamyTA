import numpy as np
import pandas as pd
import os
import pennylane as qml
from compute_metrics import calculate_entanglement_entropy

def run_vqe_adaptive(H_obj, H_pen, n_qubits, curr_date, ne_bitstring=None, K=2, target_penalty=5.0,
                     max_depth=4, maxiter=100, max_total_iter=500,
                     batch_size=10, conv_window=4, conv_tol=1e-3,
                     best_a_base=0.1, seed=42, file_config=None):
    """
    Menjalankan VQE dengan Penalty Annealing.
    H_total(t) = H_obj + penalty(t) * H_pen
    """
    if file_config is None:
        file_config = {
            'riwayat_iterasi': 'riwayat_iterasi_vqe.csv',
            'theta_final': 'theta_final_all_depths.csv',
            'depth_vs_energi': 'hasil_depth_vs_energi.csv'
        }
        
    dev = qml.device("default.qubit", wires=n_qubits)
    rng = np.random.default_rng(seed)

    # --- RESET RIWAYAT ITERASI ---
    if os.path.exists(file_config['riwayat_iterasi']):
        os.remove(file_config['riwayat_iterasi'])

    def make_circuit(depth):
        def ansatz(params):
            w = params.reshape((depth + 1, n_qubits, 2))
            for layer in range(depth + 1):
                for q in range(n_qubits):
                    qml.RY(w[layer, q, 0], wires=q)
                    qml.RZ(w[layer, q, 1], wires=q)
                if layer < depth:
                    for q in range(n_qubits - 1):
                        qml.CNOT(wires=[q, q + 1])
                    qml.CNOT(wires=[n_qubits - 1, 0])

        @qml.qnode(dev)
        def cost_circuit(params, p_scale=1.0):
            ansatz(params)
            # H_total dinamis: H_obj + scale * H_pen
            return qml.expval(H_obj + p_scale * H_pen)

        @qml.qnode(dev)
        def prob_circuit(params):
            ansatz(params)
            return qml.probs(wires=range(n_qubits))
            
        @qml.qnode(dev)
        def state_circuit(params):
            ansatz(params)
            return qml.state()

        return cost_circuit, prob_circuit, state_circuit

    def run_spsa(cost_circuit, state_circuit, n_params, init_params=None, a_base=0.1, c_base=0.1, depth_label=1, target_p=5.0):
        a, c      = a_base, c_base
        A_coeff   = maxiter * 0.1
        alpha_exp = 0.602
        gamma_exp = 0.101

        if init_params is not None:
            params = init_params.copy()
        else:
            params = rng.uniform(0, 2 * np.pi, n_params)

        energy_history = []
        entropy_history = []
        grad_var_history = []
        total_iters    = 0
        
        while total_iters < max_total_iter:
            # --- PENALTY ANNEALING TERKALIBRASI ---
            # Pinalti mencapai 100% pada 70% total budget iterasi.
            # Sisa 30% digunakan untuk "fine-tuning" dengan pinalti konstan.
            anneal_progress = min(1.0, total_iters / (0.7 * max_total_iter))
            p_scale = target_p * (0.1 + 0.9 * anneal_progress)
            
            current_grad_vars = []
            for _ in range(batch_size):
                k     = total_iters
                a_k   = a / (A_coeff + k + 1) ** alpha_exp
                c_k   = c / (k + 1)           ** gamma_exp
                delta = 2 * rng.integers(0, 2, size=n_params) - 1
                
                cost_plus  = float(cost_circuit(params + c_k * delta, p_scale=p_scale))
                cost_minus = float(cost_circuit(params - c_k * delta, p_scale=p_scale))
                grad       = (cost_plus - cost_minus) / (2 * c_k * delta)
                
                # [Phase 3] Gradient Clipping
                grad       = np.clip(grad, -1.0, 1.0)
                
                params     = params - a_k * grad
                current_grad_vars.append(np.var(grad))
                total_iters += 1

            current_energy = float(cost_circuit(params, p_scale=p_scale))
            energy_history.append(current_energy)
            grad_var_history.append(np.mean(current_grad_vars))
            
            # Hitung Entropi
            try:
                current_psi = state_circuit(params)
                current_entropy = calculate_entanglement_entropy(current_psi)
                entropy_history.append(current_entropy)
            except:
                entropy_history.append(0.0)
            
            iter_df = pd.DataFrame({
                'Depth': [depth_label], 
                'Iteration': [total_iters], 
                'Energy': [current_energy],
                'Entropy': [entropy_history[-1]],
                'Grad_Var': [grad_var_history[-1]],
                'Penalty_Scale': [p_scale]
            })
            iter_df.to_csv(file_config['riwayat_iterasi'], mode='a', header=not os.path.exists(file_config['riwayat_iterasi']), index=False)

            if total_iters >= maxiter and len(energy_history) >= conv_window:
                # [Phase 4] Entropy Protection & Annealing Protection
                # Jangan berhenti jika:
                # 1. Entropi masih tinggi (mencegah superposisi macet)
                # 2. Annealing pinalti belum mencapai 100%
                if (n_qubits <= 4 and entropy_history[-1] > 0.1) or (anneal_progress < 1.0):
                    continue 

                E_old, E_now = energy_history[-conv_window], energy_history[-1]
                if abs(E_old - E_now) / (abs(E_old) + 1e-12) < conv_tol:
                    break
        return params, energy_history[-1], energy_history, entropy_history, grad_var_history, total_iters

    best_energy    = np.inf
    best_params, best_depth, best_history, best_ent_hist, best_grad_var_hist = None, 1, [], [], []
    depth_energies = []
    prev_params    = None
    all_theta_data = []
    
    saved_init_p = {}
    saved_a_base = {}

    for depth in range(1, max_depth + 1):
        n_params = n_qubits * 2 * (depth + 1)
        cost_fn, prob_fn, state_fn = make_circuit(depth)

        if prev_params is not None and len(prev_params) < n_params:
            # Warm-start yang diperbaiki: gunakan distribusi normal sangat kecil 
            # agar layer baru mendekati identitas, menjaga stabilitas energi.
            old_w = prev_params.reshape((depth, n_qubits, 2))     # (depth, n, 2)
            new_layer = rng.normal(0, 1e-4, (1, n_qubits, 2))    # layer baru (dekat identitas)
            # Sisipkan layer baru sebelum output layer terakhir
            new_w = np.concatenate([old_w[:-1], new_layer, old_w[-1:]], axis=0)  # (depth+1, n, 2)
            
            # [Phase 2] Asymmetric Jitter: Pemutus simetri agar tidak terjebak superposisi
            asymmetric_jitter = rng.normal(0, 1e-4, n_params) * np.linspace(1, 1.5, n_params)
            init_p = new_w.flatten() + asymmetric_jitter
        else:
            if ne_bitstring is not None:
                init_w = np.zeros((depth + 1, n_qubits, 2))
                for q in range(n_qubits):
                    init_w[0, q, 0] = np.pi if int(ne_bitstring[q]) == 1 else 0.0
                
                # [Phase 2] Asymmetric Jitter pada inisialisasi Nash
                asymmetric_jitter = rng.normal(0, 1e-3, n_params) * np.linspace(1, 1.5, n_params)
                init_p = init_w.flatten() + asymmetric_jitter
            else:
                init_p = rng.uniform(0, 2 * np.pi, n_params)

        # Skala learning rate dinamis: semakin dalam sirkuit, langkah semakin kecil (presisi)
        current_a_base = best_a_base / np.sqrt(depth)
        saved_init_p[depth] = init_p
        saved_a_base[depth] = current_a_base
        
        params, energy, e_hist, ent_hist, g_var_hist, n_iters = run_spsa(
            cost_fn, state_fn, n_params, init_params=init_p, 
            a_base=current_a_base, c_base=0.1/np.sqrt(depth), 
            depth_label=depth, target_p=target_penalty
        )
        print(f"    [Depth {depth}] Konvergen dalam {n_iters} iterasi | E = {energy:.6f}")
        depth_energies.append((depth, energy, n_iters))
        prev_params = params

        # --- KUMPULKAN THETA (Poin 1) ---
        for idx, val in enumerate(params):
            all_theta_data.append({'Depth': depth, 'Theta_Index': idx, 'Theta_Value': val})

        if energy < best_energy:
            best_energy, best_params, best_depth, best_history, best_ent_hist, best_grad_var_hist = energy, params, depth, e_hist, ent_hist, g_var_hist
            
    # --- 5 RUNS UNTUK DEPTH TERPILIH ---
    print(f"    -> Melakukan 5 iterasi SPSA untuk depth terpilih ({best_depth})...")
    cost_fn, prob_fn, state_fn = make_circuit(best_depth)
    n_params = n_qubits * 2 * (best_depth + 1)
    
    n_runs = 5
    runs_results = []
    for r_idx in range(n_runs):
        p, e, e_h, ent_h, gv_h, iters = run_spsa(
            cost_fn, state_fn, n_params, init_params=saved_init_p[best_depth], 
            a_base=saved_a_base[best_depth], c_base=0.1/np.sqrt(best_depth), 
            depth_label=best_depth, target_p=target_penalty
        )
        runs_results.append({
            'params': p, 'energy': e, 'e_hist': e_h, 'ent_hist': ent_h, 'g_var_hist': gv_h
        })
        
    best_history = [r['e_hist'] for r in runs_results]
    best_ent_hist = [r['ent_hist'] for r in runs_results]
    best_grad_var_hist = [r['g_var_hist'] for r in runs_results]
    
    # Pilih best_params dari 5 run ini
    best_run_idx = np.argmin([r['energy'] for r in runs_results])
    best_params = runs_results[best_run_idx]['params']
    best_energy = runs_results[best_run_idx]['energy']
    
    # Update all_theta_data untuk depth terpilih
    all_theta_data = [item for item in all_theta_data if item['Depth'] != best_depth]
    for idx, val in enumerate(best_params):
        all_theta_data.append({'Depth': best_depth, 'Theta_Index': idx, 'Theta_Value': val})

    # Update depth_energies agar plot vs depth pakai E dari best run terbaru (opsional, tapi disarankan)
    for i, (d, e, it) in enumerate(depth_energies):
        if d == best_depth:
            depth_energies[i] = (d, best_energy, it)

    # --- EKSPOR THETA GABUNGAN (Poin 1) ---
    pd.DataFrame(all_theta_data).to_csv(file_config['theta_final'], index=False)

    # --- EKSPOR DEPTH VS ENERGI (Poin 3) ---
    depth_df = pd.DataFrame(depth_energies, columns=['Depth', 'Energy', 'Iterations'])
    depth_df.insert(0, 'Date', curr_date.date())
    depth_df.to_csv(file_config['depth_vs_energi'], mode='a', header=not os.path.exists(file_config['depth_vs_energi']), index=False)

    _, prob_fn, _ = make_circuit(best_depth)
    probs = prob_fn(best_params)
    sorted_indices = np.argsort(probs)[::-1]
    best_bitstring = None
    for idx in sorted_indices:
        bs = format(idx, f'0{n_qubits}b')
        if bs.count('1') == K:
            best_bitstring = bs
            break
    if best_bitstring is None:
        top_k = np.argsort(probs)[-K:]
        bs_list = list('0' * n_qubits)
        for idx in top_k: bs_list[idx] = '1'
        best_bitstring = ''.join(bs_list)

    return [i for i, bit in enumerate(best_bitstring) if bit == '1'], best_depth, best_energy, best_history, best_ent_hist, best_grad_var_hist, depth_energies, probs, best_params
