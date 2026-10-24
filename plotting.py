"""
plotting.py
-----------
Plotting and visualization engine for the Computational Neuronal Firing Pattern Library.
Renders dark-theme optimized, publication-grade figures for:
- Simulated membrane potential V(t) and adaptation/recovery variable dynamics
- Experimental Frequency-Current (F-I) curves with verified data points and error bars
- Explicit differentiation between Empirical Data and Model Simulations
"""

from typing import Dict, Any, List, Optional
import matplotlib.pyplot as plt
import numpy as np


# Dark theme styling tokens
DARK_BG = "#0E1117"
PANEL_BG = "#161B22"
GRID_COLOR = "#30363D"
TEXT_COLOR = "#C9D1D9"
MUTED_TEXT = "#8B949E"
VOLTAGE_COLOR = "#FF5252"
ADAPTATION_COLOR = "#448AFF"
EXPERIMENTAL_COLOR = "#00E676"
SIMULATION_COLOR = "#FF9100"


def setup_matplotlib_dark_theme():
    """Apply consistent dark theme styling to matplotlib figures."""
    plt.rcParams["figure.facecolor"] = PANEL_BG
    plt.rcParams["axes.facecolor"] = DARK_BG
    plt.rcParams["axes.edgecolor"] = GRID_COLOR
    plt.rcParams["axes.labelcolor"] = TEXT_COLOR
    plt.rcParams["xtick.color"] = MUTED_TEXT
    plt.rcParams["ytick.color"] = MUTED_TEXT
    plt.rcParams["grid.color"] = GRID_COLOR
    plt.rcParams["grid.linestyle"] = ":"
    plt.rcParams["grid.alpha"] = 0.5
    plt.rcParams["font.sans-serif"] = "DejaVu Sans, Arial, sans-serif"
    plt.rcParams["legend.facecolor"] = PANEL_BG
    plt.rcParams["legend.edgecolor"] = GRID_COLOR


def plot_membrane_trace(
    time: np.ndarray,
    V: np.ndarray,
    w: np.ndarray,
    params: Dict[str, Any],
    model_name: str = "AdEx"
) -> plt.Figure:
    """
    Generate publication-grade dual-panel time series plot for membrane potential
    and adaptation/recovery variable.

    Parameters:
    -----------
    time : np.ndarray
        Simulation time points in ms.
    V : np.ndarray
        Membrane potential values in mV.
    w : np.ndarray
        Adaptation current (AdEx, pA) or recovery variable (Izhikevich, pA).
    params : dict
        Parameters used in simulation.
    model_name : str
        'AdEx' or 'Izhikevich'.

    Returns:
    --------
    matplotlib.figure.Figure
    """
    setup_matplotlib_dark_theme()
    fig, (ax1, ax2) = plt.subplots(
        2, 1, figsize=(11, 6), sharex=True, gridspec_kw={"height_ratios": [2.6, 1.1]}
    )

    # Subplot 1: Membrane Potential V(t)
    ax1.plot(time, V, color=VOLTAGE_COLOR, linewidth=1.2, label=f"V(t) Membrane Potential [{model_name}]")

    # Threshold markers
    vt_val = params.get("VT", params.get("vt", None))
    el_val = params.get("EL", params.get("vr", None))

    if vt_val is not None:
        ax1.axhline(float(vt_val), color="#FFD700", linestyle="--", linewidth=1.0, alpha=0.8, label=f"Threshold VT ({vt_val} mV)")
    if el_val is not None:
        ax1.axhline(float(el_val), color="#00E676", linestyle=":", linewidth=1.0, alpha=0.8, label=f"Reversal/Rest EL ({el_val} mV)")

    # Title & Labels
    neuron_title = params.get("name", "Neuron")
    injected_I = params.get("I", 0.0)
    current_unit = params.get("current_unit", "pA")
    ax1.set_ylabel("Membrane Potential (mV)", fontsize=11, fontweight="bold", color=TEXT_COLOR)
    ax1.set_title(
        f"Simulated Electrophysiological Firing Trace — {neuron_title} [{model_name} Model, I = {injected_I} {current_unit}]",
        fontsize=12, fontweight="bold", color=TEXT_COLOR, pad=10
    )
    ax1.grid(True)
    ax1.legend(loc="upper right", framealpha=0.85, labelcolor=TEXT_COLOR, fontsize=9)

    # Subplot 2: Adaptation current or recovery variable
    w_label = "Adaptation Current w(t) (pA)" if model_name.lower() == "adex" else "Recovery Variable u(t) (pA)"
    ax2.plot(time, w, color=ADAPTATION_COLOR, linewidth=1.2, label=w_label)
    ax2.set_xlabel("Time (ms)", fontsize=11, fontweight="bold", color=TEXT_COLOR)
    ax2.set_ylabel(w_label.split()[0] + " (pA)", fontsize=10, fontweight="bold", color=TEXT_COLOR)
    ax2.grid(True)
    ax2.legend(loc="upper right", framealpha=0.85, labelcolor=TEXT_COLOR, fontsize=9)

    plt.tight_layout()
    return fig


def plot_experimental_fi(paper_info: Dict[str, Any]) -> Optional[plt.Figure]:
    """
    Render experimental Frequency-Current (F-I) curve from verified published data points.

    Parameters:
    -----------
    paper_info : dict
        Curated paper record containing 'fi_points', 'fi_fig', 'title', etc.

    Returns:
    --------
    matplotlib.figure.Figure or None if no F-I graph exists.
    """
    if not paper_info.get("has_fi_graph") or not paper_info.get("fi_points"):
        return None

    setup_matplotlib_dark_theme()
    fi_points = paper_info["fi_points"]

    currents = [p["current"] for p in fi_points]
    freqs = [p["freq"] for p in fi_points]
    errs = [p.get("err", 0.0) for p in fi_points]

    fig, ax = plt.subplots(figsize=(8, 4.8))

    has_error = any(e > 0 for e in errs)
    if has_error:
        ax.errorbar(
            currents, freqs, yerr=errs, fmt="o-", color=EXPERIMENTAL_COLOR,
            ecolor="#69F0AE", elinewidth=1.5, capsize=4, capthick=1.5,
            markersize=6, linewidth=1.8, label="Experimental Data (Mean ± SEM)"
        )
    else:
        ax.plot(
            currents, freqs, "o-", color=EXPERIMENTAL_COLOR,
            markersize=6, linewidth=1.8, label="Experimental Measurements"
        )

    ax.set_xlabel("Injected Current (pA)", fontsize=11, fontweight="bold", color=TEXT_COLOR)
    ax.set_ylabel("Firing Frequency (Hz)", fontsize=11, fontweight="bold", color=TEXT_COLOR)

    short_fig = paper_info.get("fi_fig", "F-I Plot")
    authors_short = paper_info.get("authors", "").split(",")[0]
    year = paper_info.get("year", "")
    ax.set_title(
        f"Verified Experimental F–I Curve — {authors_short} et al. ({year}), {short_fig}",
        fontsize=11, fontweight="bold", color=TEXT_COLOR, pad=10
    )

    ax.grid(True)
    ax.legend(loc="upper left", framealpha=0.9, labelcolor=TEXT_COLOR, fontsize=9)

    # Set appropriate limits
    if currents:
        x_min = min(currents)
        x_max = max(currents)
        pad_x = max((x_max - x_min) * 0.05, 5.0)
        ax.set_xlim(x_min - pad_x, x_max + pad_x)

    if freqs:
        y_max = max(freqs)
        err_max = max(errs) if has_error else 0.0
        ax.set_ylim(-2.0, (y_max + err_max) * 1.15 + 2.0)

    plt.tight_layout()
    return fig
