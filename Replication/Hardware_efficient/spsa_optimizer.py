"""
SPSA (Simultaneous Perturbation Stochastic Approximation) Optimizer
Based on Kandala et al., Nature 549, 242-246 (2017)

Key feature: Only 2 function evaluations per iteration, regardless of 
parameter dimension (unlike gradient-based methods which need O(p) evaluations).

Reference: Spall, J.C. (1992). "Multivariate stochastic approximation using 
a simultaneous perturbation gradient approximation"
"""

import numpy as np
from typing import Callable, Optional, Tuple, List


class SPSA:
    """
    SPSA Optimizer for VQE.
    
    The gradient is approximated using only 2 measurements per iteration:
        g_k ≈ [f(θ + c_k⋅Δ) - f(θ - c_k⋅Δ)] / (2⋅c_k) ⋅ Δ^(-1)
        
    Where Δ is a random perturbation vector with ±1 entries.
    
    Gain sequences (standard form):
        a_k = a / (A + k + 1)^α
        c_k = c / (k + 1)^γ
        
    Recommended: α = 0.602, γ = 0.101 (theoretically optimal)
    """
    
    def __init__(
        self,
        maxiter: int = 100,
        a: float = 0.1,
        c: float = 0.1,
        A: float = 10.0,
        alpha: float = 0.602,
        gamma: float = 0.101,
        seed: Optional[int] = None
    ):
        """
        Initialize SPSA optimizer.
        
        Args:
            maxiter: Maximum iterations
            a: Initial step size for parameter update
            c: Initial perturbation magnitude
            A: Stability constant (typically ~10% of maxiter)
            alpha: Decay exponent for step size
            gamma: Decay exponent for perturbation
            seed: Random seed for reproducibility
        """
        self.maxiter = maxiter
        self.a = a
        self.c = c
        self.A = A
        self.alpha = alpha
        self.gamma = gamma
        
        self.rng = np.random.default_rng(seed)
        
        # Tracking
        self.history = []
        self.nfev = 0  # Number of function evaluations
    
    def _get_gains(self, k: int) -> Tuple[float, float]:
        """Calculate gain sequences at iteration k."""
        a_k = self.a / (self.A + k + 1) ** self.alpha
        c_k = self.c / (k + 1) ** self.gamma
        return a_k, c_k
    
    def _get_perturbation(self, p: int) -> np.ndarray:
        """Generate random ±1 perturbation vector."""
        return 2 * self.rng.integers(0, 2, size=p) - 1
    
    def step(
        self,
        cost_fn: Callable[[np.ndarray], float],
        params: np.ndarray,
        k: int
    ) -> Tuple[np.ndarray, float, float]:
        """
        Perform single SPSA step.
        
        Args:
            cost_fn: Objective function to minimize
            params: Current parameter values
            k: Current iteration number
            
        Returns:
            new_params: Updated parameters
            grad_approx_norm: Norm of gradient approximation
            cost_mid: Cost at current parameters (estimated)
        """
        p = len(params)
        a_k, c_k = self._get_gains(k)
        
        # Generate perturbation
        delta = self._get_perturbation(p)
        
        # Evaluate at perturbed points (core of SPSA - only 2 evaluations!)
        params_plus = params + c_k * delta
        params_minus = params - c_k * delta
        
        f_plus = cost_fn(params_plus)
        f_minus = cost_fn(params_minus)
        self.nfev += 2
        
        # Approximate gradient
        # g_k ≈ (f+ - f-) / (2⋅c_k) ⋅ (1/Δ)
        # Element-wise: g_k[i] ≈ (f+ - f-) / (2⋅c_k⋅Δ[i])
        grad_approx = (f_plus - f_minus) / (2 * c_k * delta)
        
        # Update parameters
        new_params = params - a_k * grad_approx
        
        # Estimate cost at current point
        cost_mid = (f_plus + f_minus) / 2
        
        return new_params, np.linalg.norm(grad_approx), cost_mid
    
    def optimize(
        self,
        cost_fn: Callable[[np.ndarray], float],
        initial_params: np.ndarray,
        callback: Optional[Callable[[int, np.ndarray, float], None]] = None
    ) -> Tuple[np.ndarray, float, List[float]]:
        """
        Run full SPSA optimization.
        
        Args:
            cost_fn: Objective function to minimize
            initial_params: Starting parameter values
            callback: Optional callback(iteration, params, cost)
            
        Returns:
            best_params: Optimal parameters found
            best_cost: Minimum cost achieved
            history: List of costs at each iteration
        """
        params = initial_params.copy()
        self.history = []
        self.nfev = 0
        
        best_params = params.copy()
        best_cost = float('inf')
        
        for k in range(self.maxiter):
            params, grad_norm, cost = self.step(cost_fn, params, k)
            
            self.history.append(cost)
            
            if cost < best_cost:
                best_cost = cost
                best_params = params.copy()
            
            if callback is not None:
                callback(k, params, cost)
        
        return best_params, best_cost, self.history


def create_spsa_optimizer(maxiter=100, calibrate=True, initial_cost=None):
    """
    Factory function to create SPSA optimizer with sensible defaults.
    
    Args:
        maxiter: Maximum iterations
        calibrate: Whether to auto-calibrate a and c based on initial_cost
        initial_cost: Initial cost value for calibration
        
    Returns:
        SPSA optimizer instance
    """
    # Default parameters (can be tuned)
    if calibrate and initial_cost is not None:
        # Simple heuristic: scale by initial cost
        a = 0.1 * abs(initial_cost) if initial_cost != 0 else 0.1
        c = 0.1
    else:
        a = 0.1
        c = 0.1
    
    return SPSA(
        maxiter=maxiter,
        a=a,
        c=c,
        A=maxiter * 0.1,  # 10% of total iterations
        alpha=0.602,
        gamma=0.101
    )


# ============================================================
# Testing / Demonstration
# ============================================================
if __name__ == "__main__":
    print("SPSA Optimizer Test")
    print("=" * 60)
    
    # Test on simple quadratic: f(x) = sum(x^2)
    # Minimum at x = 0
    def quadratic(x):
        return np.sum(x ** 2)
    
    # Initialize
    n_params = 10
    x0 = np.random.randn(n_params)
    
    print(f"Number of parameters: {n_params}")
    print(f"Initial cost: {quadratic(x0):.6f}")
    print(f"Initial params (first 3): {x0[:3]}")
    
    # Run SPSA
    optimizer = SPSA(maxiter=200, a=0.5, c=0.1, seed=42)
    
    best_params, best_cost, history = optimizer.optimize(quadratic, x0)
    
    print(f"\nResults after {optimizer.maxiter} iterations:")
    print(f"Best cost: {best_cost:.6f}")
    print(f"Best params (first 3): {best_params[:3]}")
    print(f"Total function evaluations: {optimizer.nfev}")
    print(f"Expected: 2 × {optimizer.maxiter} = {2 * optimizer.maxiter}")
    
    # Verify 2 evaluations per iteration
    assert optimizer.nfev == 2 * optimizer.maxiter, "SPSA should use exactly 2 evals per iter!"
    print("\n✓ Verified: 2 function evaluations per iteration")
