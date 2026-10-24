"""
models package
--------------
Numerical simulation models for computational electrophysiology:
- adex: Adaptive Exponential Integrate-and-Fire model (Brette & Gerstner, 2005)
- izhikevich: Generalized / Dimensional Izhikevich model (Izhikevich, 2003, 2007)
"""

from .adex import simulate_adex, adex_derivatives
from .izhikevich import simulate_izhikevich, izhikevich_derivatives

__all__ = [
    "simulate_adex",
    "adex_derivatives",
    "simulate_izhikevich",
    "izhikevich_derivatives",
]
