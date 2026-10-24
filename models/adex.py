"""
models/adex.py
--------------
Numerical integration engine for the Adaptive Exponential Integrate-and-Fire (AdEx) model
(Brette & Gerstner, 2005).

Differential Equations:
  C * dV/dt = -gL * (V - EL) + gL * Delta_T * exp((V - VT) / Delta_T) - w + I
  tau_w * dw/dt = a * (V - EL) - w

Spike Reset Rule:
  If V >= V_peak (or Vcut):
      Spike timestamp recorded
      V -> V_reset (or Vr)
      w -> w + b

Unit Consistency:
  - C (or Cm): Membrane capacitance in pF
  - gL: Leak conductance in nS
  - EL: Leak / reversal potential in mV
  - VT: Spike-initiation threshold in mV
  - Delta_T: Exponential slope factor in mV
  - tau_w: Adaptation time constant in ms
  - a: Subthreshold adaptation conductance in nS
  - b: Spike-triggered adaptation increment in pA
  - I: Injected / applied current in pA
  - V_peak (Vcut): Spike cutoff / peak threshold in mV
  - V_reset (Vr): Post-spike reset membrane potential in mV

Dimensional Check:
  (I [pA] - gL [nS] * Delta_V [mV]) / C [pF]
  = (10^-12 A) / (10^-12 F) = 1 V/s = 1 mV/ms.
  dV/dt is in mV/ms, and dw/dt is in pA/ms.
"""

from typing import Tuple, Dict, Any
import numpy as np


def adex_derivatives(V: float, w: float, params: Dict[str, Any]) -> Tuple[float, float]:
    """
    Compute derivatives dV/dt (mV/ms) and dw/dt (pA/ms) for the AdEx model.

    Parameters:
    -----------
    V : float
        Current membrane potential (mV).
    w : float
        Current adaptation current (pA).
    params : dict
        Neuron parameter dictionary containing C/Cm, gL, EL, Delta_T, VT, tau_w, a, I.

    Returns:
    --------
    tuple (dV_dt, dw_dt)
    """
    C = float(params.get("Cm", params.get("C", 100.0)))
    gL = float(params.get("gL", 10.0))
    EL = float(params.get("EL", -65.0))
    Delta_T = float(params.get("Delta_T", 2.0))
    VT = float(params.get("VT", -50.0))
    tau_w = float(params.get("tau_w", 1.0))
    a = float(params.get("a", 0.0))
    I = float(params.get("I", 0.0))

    if Delta_T <= 0:
        Delta_T = 1e-4

    # Prevent exponential numerical overflow by clipping the exponent
    exponent = (V - VT) / Delta_T
    exponent_clipped = np.clip(exponent, -50.0, 20.0)

    # Exponential current term
    exp_term = gL * Delta_T * np.exp(exponent_clipped)

    # Membrane voltage derivative: dV/dt = ( -I_leak + I_exp - w + I_injected ) / C
    dV_dt = (-gL * (V - EL) + exp_term - w + I) / C

    # Adaptation current derivative: dw/dt = ( a * (V - EL) - w ) / tau_w
    dw_dt = (a * (V - EL) - w) / max(tau_w, 1e-4)

    return dV_dt, dw_dt


def simulate_adex(
    params: Dict[str, Any],
    duration_ms: float,
    dt: float = 0.01,
    V_peak: float = None,
    V_reset: float = None,
    method: str = "euler"
) -> Dict[str, Any]:
    """
    Simulate membrane potential V(t) and adaptation current w(t) using the AdEx model.

    Parameters:
    -----------
    params : dict
        Dictionary of neuron parameters.
    duration_ms : float
        Total duration of simulation in milliseconds (ms).
    dt : float, optional
        Integration time step in milliseconds (ms). Default is 0.01 ms.
    V_peak : float, optional
        Threshold voltage for spike detection (mV). If None, uses params['Vcut'] or params['V_peak'].
    V_reset : float, optional
        Reset voltage post-spike (mV). If None, uses params['Vr'] or params['V_reset'].
    method : str, optional
        Integration method: 'euler' (Forward Euler) or 'rk4' (4th Order Runge-Kutta).

    Returns:
    --------
    dict containing:
        'time'       : 1D np.ndarray of time points (ms)
        'V'          : 1D np.ndarray of membrane potentials (mV)
        'w'          : 1D np.ndarray of adaptation currents (pA)
        'spike_times': 1D np.ndarray of float (ms when spikes occurred)
        'spike_count': int (total detected spikes)
    """
    if duration_ms <= 0:
        raise ValueError("Simulation duration must be strictly positive (> 0 ms).")
    if dt <= 0 or dt > 1.0:
        raise ValueError("Time step dt must be strictly positive and <= 1.0 ms.")

    # Determine spike threshold and reset potential
    if V_peak is not None:
        peak_v = float(V_peak)
    else:
        peak_v = float(params.get("Vcut", params.get("V_peak", 0.0)))

    if V_reset is not None:
        reset_v = float(V_reset)
    else:
        reset_v = float(params.get("Vr", params.get("V_reset", -60.0)))

    # Initialize time array
    n_steps = int(np.round(duration_ms / dt)) + 1
    t_array = np.linspace(0.0, duration_ms, n_steps)

    # Initialize state variables
    V_array = np.zeros(n_steps)
    w_array = np.zeros(n_steps)

    # Initial conditions: V starts at resting leak potential EL, w starts at 0
    EL = float(params.get("EL", -65.0))
    V_array[0] = EL
    w_array[0] = 0.0

    b = float(params.get("b", 0.0))
    spike_times = []

    # Time integration loop
    for i in range(n_steps - 1):
        V_curr = V_array[i]
        w_curr = w_array[i]

        # Check for spike occurrence
        if V_curr >= peak_v:
            # Record spike time
            spike_times.append(t_array[i])

            # For visualization, visually set spike peak on trace
            V_array[i] = peak_v

            # Apply AdEx reset rules for next step
            V_next = reset_v
            w_next = w_curr + b
        else:
            if method.lower() == "rk4":
                # 4th Order Runge-Kutta step
                k1_V, k1_w = adex_derivatives(V_curr, w_curr, params)
                k2_V, k2_w = adex_derivatives(V_curr + 0.5 * dt * k1_V, w_curr + 0.5 * dt * k1_w, params)
                k3_V, k3_w = adex_derivatives(V_curr + 0.5 * dt * k2_V, w_curr + 0.5 * dt * k2_w, params)
                k4_V, k4_w = adex_derivatives(V_curr + dt * k3_V, w_curr + dt * k3_w, params)

                V_next = V_curr + (dt / 6.0) * (k1_V + 2 * k2_V + 2 * k3_V + k4_V)
                w_next = w_curr + (dt / 6.0) * (k1_w + 2 * k2_w + 2 * k3_w + k4_w)
            else:
                # Forward Euler step
                dV_dt, dw_dt = adex_derivatives(V_curr, w_curr, params)
                V_next = V_curr + dV_dt * dt
                w_next = w_curr + dw_dt * dt

        # Biological safety clamp against runaways
        if V_next < -150.0:
            V_next = -150.0
        elif V_next > 80.0:
            V_next = peak_v

        # Numerical stability sanity check
        if not (np.isfinite(V_next) and np.isfinite(w_next)):
            raise ArithmeticError(
                f"Simulation became unstable at t = {t_array[i]:.2f} ms (V={V_next}, w={w_next}). "
                "Check parameters or reduce integration step dt."
            )

        V_array[i + 1] = V_next
        w_array[i + 1] = w_next

    return {
        "time": t_array,
        "V": V_array,
        "w": w_array,
        "spike_times": np.array(spike_times),
        "spike_count": len(spike_times),
    }
