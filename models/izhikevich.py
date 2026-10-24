"""
models/izhikevich.py
--------------------
Exact numerical integration engine for the Izhikevich neuron model
matching the reference specification:

Differential Equations:
  dv/dt = k * v^2 + 5 * v + 140 - u + I(t)
  du/dt = a * (b * v - u)

Spike Reset Rule:
  If v >= 30 mV:
      Spike timestamp recorded
      v -> c
      u -> u + d

Units & Conventions:
  - v: Membrane potential (mV)
  - u: Recovery variable (pA)
  - a: Time scale of recovery variable u (ms^-1)
  - b: Sensitivity of recovery variable to subthreshold fluctuations (dimensionless / nS)
  - c: Post-spike membrane potential reset (mV) [internal reset parameter]
  - d: After-spike recovery increment (pA)
  - k: Quadratic non-linear scaling parameter (mV^-1 * ms^-1)
  - I: Injected / applied depolarizing current (pA)
  - Spike detection threshold: Strictly 30.0 mV
"""

from typing import Tuple, Dict, Any
import numpy as np


def izhikevich_derivatives(v: float, u: float, params: Dict[str, Any]) -> Tuple[float, float]:
    """
    Compute derivatives dv/dt (mV/ms) and du/dt (pA/ms) for the Izhikevich model.

    Exact Equations:
      dv/dt = k * v^2 + 5 * v + 140 - u + I
      du/dt = a * (b * v - u)
    """
    k = float(params.get("k", 0.04))
    a = float(params.get("a", 0.02))
    b = float(params.get("b", 0.2))
    I = float(params.get("I", 0.0))

    dv_dt = k * (v ** 2) + 5.0 * v + 140.0 - u + I
    du_dt = a * (b * v - u)

    return dv_dt, du_dt


def simulate_izhikevich(
    params: Dict[str, Any],
    duration_ms: float,
    dt: float = 0.01,
    V_peak: float = 30.0,
    V_reset: float = None,
    method: str = "euler"
) -> Dict[str, Any]:
    """
    Simulate membrane potential v(t) and recovery variable u(t) using the exact
    Izhikevich equations.

    Parameters:
    -----------
    params : dict
        Parameter dictionary containing a, b, c, d, k, and I.
    duration_ms : float
        Total duration of simulation in milliseconds (ms).
    dt : float, optional
        Integration time step in milliseconds (ms). Default is 0.01 ms.
    V_peak : float, optional
        Action potential peak threshold. Fixed at strictly 30.0 mV per model definition.
    V_reset : float, optional
        Post-spike reset voltage (mV). If None, uses params['c'].
    method : str, optional
        Integration method: 'euler' (Forward Euler) or 'rk4'.

    Returns:
    --------
    dict containing:
        'time'       : 1D np.ndarray of time points (ms)
        'V'          : 1D np.ndarray of membrane potentials (mV)
        'w'          : 1D np.ndarray of recovery variable u (pA)
        'spike_times': 1D np.ndarray of float (ms when spikes occurred)
        'spike_count': int (total detected spikes)
    """
    if duration_ms <= 0:
        raise ValueError("Simulation duration must be strictly positive (> 0 ms).")
    if dt <= 0 or dt > 1.0:
        raise ValueError("Time step dt must be strictly positive and <= 1.0 ms.")

    # Strictly 30.0 mV threshold
    peak_v = 30.0

    # Internal reset voltage c
    c = float(V_reset if V_reset is not None else params.get("c", -55.0))
    d = float(params.get("d", 8.0))
    b = float(params.get("b", 0.2))

    # Initialize time array
    n_steps = int(np.round(duration_ms / dt)) + 1
    t_array = np.linspace(0.0, duration_ms, n_steps)

    # Initialize state variables
    v_array = np.zeros(n_steps)
    u_array = np.zeros(n_steps)

    # Initial conditions: start at reset voltage c
    v_curr = c
    u_curr = b * c

    v_array[0] = v_curr
    u_array[0] = u_curr

    spike_times = []

    # Numerical integration loop
    for i in range(n_steps - 1):
        # Check spike reset condition: if v >= 30 mV
        if v_curr >= peak_v:
            spike_times.append(t_array[i])
            v_array[i] = peak_v  # Visually mark peak at 30 mV
            v_next = c
            u_next = u_curr + d
        else:
            if method.lower() == "rk4":
                k1_v, k1_u = izhikevich_derivatives(v_curr, u_curr, params)
                k2_v, k2_u = izhikevich_derivatives(v_curr + 0.5 * dt * k1_v, u_curr + 0.5 * dt * k1_u, params)
                k3_v, k3_u = izhikevich_derivatives(v_curr + 0.5 * dt * k2_v, u_curr + 0.5 * dt * k2_u, params)
                k4_v, k4_u = izhikevich_derivatives(v_curr + dt * k3_v, u_curr + dt * k3_u, params)

                v_next = v_curr + (dt / 6.0) * (k1_v + 2 * k2_v + 2 * k3_v + k4_v)
                u_next = u_curr + (dt / 6.0) * (k1_u + 2 * k2_u + 2 * k3_u + k4_u)
            else:
                # Forward Euler
                dv_dt, du_dt = izhikevich_derivatives(v_curr, u_curr, params)
                v_next = v_curr + dv_dt * dt
                u_next = u_curr + du_dt * dt

        # Numerical boundary limits to prevent overflow
        if v_next > 80.0:
            v_next = peak_v
        elif v_next < -150.0:
            v_next = -150.0

        if not (np.isfinite(v_next) and np.isfinite(u_next)):
            raise ArithmeticError(
                f"Izhikevich simulation diverged at t = {t_array[i]:.2f} ms (v={v_next}, u={u_next}). "
                "Check injected current I or reduce dt."
            )

        v_curr = v_next
        u_curr = u_next

        v_array[i + 1] = v_curr
        u_array[i + 1] = u_curr

    return {
        "time": t_array,
        "V": v_array,
        "w": u_array,
        "spike_times": np.array(spike_times),
        "spike_count": len(spike_times),
    }
