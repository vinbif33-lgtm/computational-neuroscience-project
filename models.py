"""
models.py
---------
Backward-compatible wrapper re-exporting model simulations:
- simulate_adex, adex_derivatives (from models.adex)
- simulate_izhikevich, izhikevich_derivatives (from models.izhikevich)
"""

from models.adex import simulate_adex, adex_derivatives
from models.izhikevich import simulate_izhikevich, izhikevich_derivatives

__all__ = [
    "simulate_adex",
    "adex_derivatives",
    "simulate_izhikevich",
    "izhikevich_derivatives",
]
