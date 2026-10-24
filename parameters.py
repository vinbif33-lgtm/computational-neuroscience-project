"""
parameters.py
-------------
Electrophysiological parameter database for Canonical Neuronal Firing Pattern Library.
Maintains strictly source-separated, verified parameter sets for:
1. Izhikevich Model: Table S4
   Parameters: a, b, d, k, default current I, and internal reset c.
2. AdEx Model: Table S5 & Table 1
   Supported populations: Cerebellar Granule Cell, Cerebellar Golgi Cell,
   Cerebellar Purkinje Cell, Cholinergic Neuron, Deep Cerebellar Nuclei (DCN).
   (Cortico-cortical, Pyramidal, and Hippocampal Dentate Gyrus Granule are omitted for AdEx per instructions).
"""

from typing import Dict, Any, List, Tuple

# -------------------------------------------------------------------------
# Supported Populations per Model
# -------------------------------------------------------------------------
IZHIKEVICH_POPULATIONS = [
    "Cerebellar Granule Cell (GrC)",
    "Cerebellar Golgi Cell (GoC)",
    "Molecular Layer Interneuron (MLI)",
    "Cerebellar Purkinje Cell (PC)",
    "Cholinergic Neuron",
    "Cortico-cortical Neuron"
]

ADEX_POPULATIONS = [
    "Cerebellar Granule Cell (GrC)",
    "Cerebellar Golgi Cell (GoC)",
    "Cerebellar Purkinje Cell (PC)",
    "Inferior Olive Neuron (IO)",
    "Deep Cerebellar Nuclei Neuron (DCN)",
    "Hippocampal Dentate Gyrus Granule Cell",
    "Cholinergic Neuron",
    "Cortico-cortical Neuron"
]

# -------------------------------------------------------------------------
# 1. Table S4: Izhikevich Model Parameters (Exact Table from Reference Image)
# -------------------------------------------------------------------------
# dv/dt = k * v^2 + 5 * v + 140 - u + I
# du/dt = a * (b * v - u)
# If v >= 30 mV: v <- c, u <- u + d
# Displayed in GUI: a, b, c, d, k, I
IZHIKEVICH_TABLE_S4: Dict[str, Dict[str, Any]] = {
    "Cerebellar Granule Cell (GrC)": {
        "name": "Cerebellar Granule Cell (GrC)",
        "model": "Izhikevich",
        "source": "Table S4 (Optimized Parameters)",
        "a": 0.0725,
        "b": 0.0512,
        "c": -55.89,
        "d": 24.66,
        "k": 0.0408,
        "I": 20.0,
        "current_unit": "pA",
        "description": "High-frequency non-adapting granule cell."
    },
    "Cerebellar Golgi Cell (GoC)": {
        "name": "Cerebellar Golgi Cell (GoC)",
        "model": "Izhikevich",
        "source": "Table S4 (Optimized Parameters)",
        "a": 0.005695,
        "b": 0.3885,
        "c": -64.00,
        "d": 24.38,
        "k": 0.0443,
        "I": 0.0,
        "current_unit": "pA",
        "description": "Inhibitory interneuron of cerebellar granular layer."
    },
    "Molecular Layer Interneuron (MLI)": {
        "name": "Molecular Layer Interneuron (MLI)",
        "model": "Izhikevich",
        "source": "Table S4 & Jörntell & Ekerot (2003)",
        "a": 0.1,
        "b": 0.2,
        "c": -65.0,
        "d": 2.0,
        "k": 0.04,
        "I": 20.0,
        "current_unit": "pA",
        "description": "Cerebellar molecular layer interneuron (stellate/basket cell) providing feed-forward inhibition."
    },
    "Cerebellar Purkinje Cell (PC)": {
        "name": "Cerebellar Purkinje Cell (PC)",
        "model": "Izhikevich",
        "source": "Table S4 (Optimized Parameters)",
        "a": 0.0130,
        "b": 0.4347,
        "c": -55.30,
        "d": 15.83,
        "k": 0.0455,
        "I": 0.0,
        "current_unit": "pA",
        "description": "Principal inhibitory projection neuron of cerebellar cortex."
    },
    "Cholinergic Neuron": {
        "name": "Cholinergic Neuron",
        "model": "Izhikevich",
        "source": "Table S4 (Optimized Parameters)",
        "a": 0.002,
        "b": 0.183,
        "c": -70.634,
        "d": 21.091,
        "k": 0.062,
        "I": 0.0,
        "current_unit": "pA",
        "description": "Basal forebrain / brainstem cholinergic projection neuron."
    },
    "Cortico-cortical Neuron": {
        "name": "Cortico-cortical Neuron",
        "model": "Izhikevich",
        "source": "Table S4 (Optimized Parameters)",
        "a": 0.000946,
        "b": 0.222,
        "c": -54.729,
        "d": 7.709,
        "k": 0.034,
        "I": 200.0,
        "current_unit": "pA",
        "description": "Intracortical projection neuron."
    }
}

# -------------------------------------------------------------------------
# 2. AdEx Parameter Sets (Table S5 & Table 1)
# -------------------------------------------------------------------------
ADEX_TABLE_S5: Dict[str, Dict[str, Any]] = {
    "Cerebellar Granule Cell (GrC)": {
        "name": "Cerebellar Granule Cell (GrC)",
        "model": "AdEx",
        "source": "Table S5 (Optimized Multi-Neuron Dataset)",
        "Cm": 198.94,
        "gL": 1.020,
        "EL": -73.97,
        "VT": -58.51,
        "Delta_T": 2.26,
        "tau_w": 111.07,
        "a": 0.0125,
        "b": 2.961,
        "Vr": -50.57,
        "Vcut": 27.52,
        "I": 20.0,
        "current_unit": "pA",
        "description": "Cerebellar granule cell with high input resistance."
    },
    "Cerebellar Golgi Cell (GoC)": {
        "name": "Cerebellar Golgi Cell (GoC)",
        "model": "AdEx",
        "source": "Table S5 (Optimized Multi-Neuron Dataset)",
        "Cm": 146.93,
        "gL": 2.148,
        "EL": -66.20,
        "VT": -57.19,
        "Delta_T": 3.29,
        "tau_w": 223.26,
        "a": 1.082,
        "b": 1.874,
        "Vr": -66.36,
        "Vcut": 31.07,
        "I": 0.0,
        "current_unit": "pA",
        "description": "Inhibitory interneuron of cerebellar granular layer."
    },
    "Cerebellar Purkinje Cell (PC)": {
        "name": "Cerebellar Purkinje Cell (PC)",
        "model": "AdEx",
        "source": "Table S5 (Optimized Multi-Neuron Dataset)",
        "Cm": 142.35,
        "gL": 9.218,
        "EL": -60.34,
        "VT": -59.90,
        "Delta_T": 4.14,
        "tau_w": 181.08,
        "a": 4.408,
        "b": 2.424,
        "Vr": -57.96,
        "Vcut": -8.52,
        "I": 10.0,
        "current_unit": "pA",
        "description": "Purkinje cell with low spike cutoff (-8.52 mV) and high conductance."
    },
    "Hippocampal Dentate Gyrus Granule Cell": {
        "name": "Hippocampal Dentate Gyrus Granule Cell",
        "model": "AdEx",
        "source": "Table S5 (Optimized Multi-Neuron Dataset)",
        "C": 145.595,
        "Cm": 145.595,
        "gL": 6.283,
        "EL": -65.020,
        "VT": -45.109,
        "Delta_T": 3.907,
        "tau_w": 340.584,
        "a": 1.791,
        "b": 13.169,
        "Vr": -55.531,
        "Vcut": 29.338,
        "I": 250.0,
        "current_unit": "pA",
        "default_duration_ms": 700.0,
        "description": "Hippocampal dentate gyrus granule cell with frequency-dependent adaptation (Mishra & Narayanan, 2020)."
    },
    "Cholinergic Neuron": {
        "name": "Cholinergic Neuron",
        "model": "AdEx",
        "source": "Table S5 (Optimized Multi-Neuron Dataset)",
        "C": 182.571,
        "Cm": 182.571,
        "gL": 9.753,
        "EL": -60.019,
        "VT": -59.355,
        "Delta_T": 3.919,
        "tau_w": 171.311,
        "a": 3.982,
        "b": 30.030,
        "Vr": -83.428,
        "Vcut": -15.964,
        "I": 0.0,
        "current_unit": "pA",
        "description": "Cholinergic neuron with deep reset (-83.43 mV) and cutoff (-15.96 mV)."
    },
    "Cortico-cortical Neuron": {
        "name": "Cortico-cortical Neuron",
        "model": "AdEx",
        "source": "Table S5 (Optimized Multi-Neuron Dataset)",
        "C": 117.91,
        "Cm": 117.91,
        "gL": 3.535,
        "EL": -65.74,
        "VT": -58.85,
        "Delta_T": 3.79,
        "tau_w": 341.49,
        "a": 1.276,
        "b": 22.79,
        "Vr": -53.42,
        "Vcut": 7.82,
        "I": 200.0,
        "current_unit": "pA",
        "default_duration_ms": 500.0,
        "description": "Layer 5 pyramidal / corticofugal projection neuron (Oswald et al., 2013)."
    }
}

ADEX_TABLE_1: Dict[str, Dict[str, Any]] = {
    "Cerebellar Granule Cell (GrC)": {
        "name": "Cerebellar Granule Cell (GrC)",
        "model": "AdEx",
        "source": "Table 1 (Canonical Cerebellar Dataset)",
        "C": 1.0,
        "Cm": 1.0,
        "gL": 10.0,
        "EL": -70.0,
        "VT": -50.0,
        "Delta_T": 2.0,
        "tau_w": 0.71,
        "a": -10.0,
        "b": 265.0,
        "Vr": -60.0,
        "Vcut": 0.0,
        "I": 20.0,
        "current_unit": "pA",
        "default_duration_ms": 500.0,
        "description": "Small intrinsic excitatory granule cell of cerebellar cortex (Table 1 canonical parameters)."
    },
    "Cerebellar Golgi Cell (GoC)": {
        "name": "Cerebellar Golgi Cell (GoC)",
        "model": "AdEx",
        "source": "Table 1 (Canonical Cerebellar Dataset)",
        "C": 511.0,
        "Cm": 511.0,
        "gL": 13.1,
        "EL": -58.0,
        "VT": -60.0,
        "Delta_T": 7.0,
        "tau_w": 14.65,
        "a": -20.0,
        "b": 1033.0,
        "Vr": -50.0,
        "Vcut": 0.0,
        "I": 0.0,
        "current_unit": "pA",
        "default_duration_ms": 1000.0,
        "description": "Inhibitory interneuron of cerebellar granular layer exhibiting spontaneous pacemaking at resting potential."
    },
    "Cerebellar Purkinje Cell (PC)": {
        "name": "Cerebellar Purkinje Cell (PC)",
        "model": "AdEx",
        "source": "Table 1 (Canonical Cerebellar Dataset)",
        "C": 100.0,
        "Cm": 100.0,
        "gL": 10.0,
        "EL": -65.0,
        "VT": -50.0,
        "Delta_T": 2.0,
        "tau_w": 1.0,
        "a": -13.0,
        "b": 260.0,
        "Vr": -60.0,
        "Vcut": 0.0,
        "I": 10.0,
        "current_unit": "pA",
        "default_duration_ms": 1000.0,
        "description": "Principal inhibitory output neuron of cerebellar cortex exhibiting spontaneous pacemaking."
    },
    "Inferior Olive Neuron (IO)": {
        "name": "Inferior Olive Neuron (IO)",
        "model": "AdEx",
        "source": "Table 1 & Llinás & Yarom (1981)",
        "C": 350.0,
        "Cm": 350.0,
        "gL": 10.0,
        "EL": -65.0,
        "VT": -50.0,
        "Delta_T": 2.0,
        "tau_w": 1.0,
        "a": -13.0,
        "b": 1200.0,
        "Vr": -60.0,
        "Vcut": 0.0,
        "I": 2.0,
        "current_unit": "pA",
        "default_duration_ms": 500.0,
        "description": "Mammalian inferior olivary neuron exhibiting rhythmic oscillatory spiking (simulated with 2 pA step per literature protocol)."
    },
    "Deep Cerebellar Nuclei Neuron (DCN)": {
        "name": "Deep Cerebellar Nuclei Neuron (DCN)",
        "model": "AdEx",
        "source": "Table 1 & Steuber et al. (2011)",
        "C": 200.0,
        "Cm": 200.0,
        "gL": 10.0,
        "EL": -70.0,
        "VT": -50.0,
        "Delta_T": 2.0,
        "tau_w": 8.0,
        "a": -20.0,
        "b": 675.0,
        "Vr": -60.0,
        "Vcut": 0.0,
        "I": 20.0,
        "current_unit": "pA",
        "default_duration_ms": 500.0,
        "description": "Primary output neuron of the cerebellum exhibiting regular spiking under depolarizing current injection."
    }
}

# Metadata dictionary for symbols, descriptions, units, and sources
PARAM_METADATA: Dict[str, Dict[str, str]] = {
    # AdEx Parameters (Table 1 & Table S5)
    "C": {"unit": "pF", "name": "Membrane Capacitance", "category": "AdEx", "source": "Table 1 / Table S5"},
    "Cm": {"unit": "pF", "name": "Membrane Capacitance", "category": "AdEx", "source": "Table 1 / Table S5"},
    "gL": {"unit": "nS", "name": "Leak Conductance", "category": "AdEx", "source": "Table 1 / Table S5"},
    "EL": {"unit": "mV", "name": "Leak Reversal Potential", "category": "AdEx", "source": "Table 1 / Table S5"},
    "VT": {"unit": "mV", "name": "Threshold Voltage", "category": "AdEx", "source": "Table 1 / Table S5"},
    "Delta_T": {"unit": "mV", "name": "Slope Factor", "category": "AdEx", "source": "Table 1 / Table S5"},
    "tau_w": {"unit": "ms", "name": "Adaptation Time Constant", "category": "AdEx", "source": "Table 1 / Table S5"},
    "a": {"unit": "nS", "name": "Subthreshold Adaptation Coupling", "category": "AdEx", "source": "Table 1 / Table S5"},
    "b": {"unit": "pA", "name": "Spike-Triggered Adaptation Increment", "category": "AdEx", "source": "Table 1 / Table S5"},
    "Vr": {"unit": "mV", "name": "Post-Spike Reset Potential", "category": "AdEx", "source": "Table 1 / Table S5"},
    "Vcut": {"unit": "mV", "name": "Spike Cutoff Threshold", "category": "AdEx", "source": "Table 1 / Table S5"},
    "I": {"unit": "pA", "name": "Injected Current", "category": "Common", "source": "Table Protocol"},

    # Izhikevich Parameters (Table S4)
    "izh_a": {"unit": "ms^-1", "name": "Recovery Time Scale (a)", "category": "Izhikevich", "source": "Table S4"},
    "izh_b": {"unit": "dimensionless", "name": "Subthreshold Sensitivity (b)", "category": "Izhikevich", "source": "Table S4"},
    "izh_c": {"unit": "mV", "name": "Post-Spike Reset Potential (c)", "category": "Izhikevich", "source": "Table S4"},
    "izh_d": {"unit": "pA", "name": "After-Spike Recovery Increment (d)", "category": "Izhikevich", "source": "Table S4"},
    "izh_k": {"unit": "mV^-1 * ms^-1", "name": "Quadratic Coefficient (k)", "category": "Izhikevich", "source": "Table S4"},
    "izh_I": {"unit": "pA", "name": "Injected Current (I)", "category": "Izhikevich", "source": "Table S4"}
}


def get_supported_populations(model: str) -> List[str]:
    """Return strictly supported populations for the chosen model."""
    if model.lower() == "izhikevich":
        return IZHIKEVICH_POPULATIONS.copy()
    elif model.lower() == "adex":
        return ADEX_POPULATIONS.copy()
    return []


def is_population_supported(model: str, population: str) -> Tuple[bool, str]:
    """Check if population is supported by model."""
    if model.lower() == "izhikevich":
        if population in IZHIKEVICH_TABLE_S4:
            return True, f"'{population}' is supported in Izhikevich Table S4."
        return False, f"Neuron '{population}' is not supported by the Izhikevich model."
    elif model.lower() == "adex":
        if population in ADEX_POPULATIONS:
            return True, f"'{population}' is supported in the AdEx model database."
        return False, f"Neuron '{population}' is not supported by the AdEx model."
    return False, f"Unknown model '{model}'."


def get_available_datasets_for_population(model: str, population: str) -> List[str]:
    """Return available source datasets for a given model and population, with Table 1 prioritized."""
    if model.lower() == "izhikevich":
        return ["Table S4 (Optimized Parameters)"]
    elif model.lower() == "adex":
        datasets = []
        if population in ADEX_TABLE_1:
            datasets.append("Table 1 (Canonical Cerebellar Dataset)")
        if population in ADEX_TABLE_S5:
            datasets.append("Table S5 (Optimized Multi-Neuron Dataset)")
        return datasets
    return []


def get_neuron_parameters(model: str, population: str, dataset_source: str = None) -> Dict[str, Any]:
    """Retrieve parameter dictionary for model and population, defaulting to Table 1 for AdEx."""
    if model.lower() == "izhikevich":
        if population not in IZHIKEVICH_TABLE_S4:
            raise KeyError(f"Neuron '{population}' not found in Izhikevich Table S4.")
        return IZHIKEVICH_TABLE_S4[population].copy()

    elif model.lower() == "adex":
        if dataset_source == "Table 1 (Canonical Cerebellar Dataset)" and population in ADEX_TABLE_1:
            return ADEX_TABLE_1[population].copy()
        if dataset_source == "Table S5 (Optimized Multi-Neuron Dataset)" and population in ADEX_TABLE_S5:
            return ADEX_TABLE_S5[population].copy()

        # Defaults: prioritize Table 1, then check Table S5
        if population in ADEX_TABLE_1:
            return ADEX_TABLE_1[population].copy()
        elif population in ADEX_TABLE_S5:
            return ADEX_TABLE_S5[population].copy()
        raise KeyError(f"Neuron '{population}' not found in AdEx tables.")

    raise ValueError(f"Unknown model: {model}")


# Backward-compatible alias
NEURON_DATABASE = ADEX_TABLE_1

def list_available_neurons() -> List[str]:
    return list(ADEX_TABLE_1.keys())

def get_neuron_params(neuron_key: str) -> Dict[str, Any]:
    if neuron_key in ADEX_TABLE_1:
        return ADEX_TABLE_1[neuron_key].copy()
    # Flexible alias lookup (e.g. 'GrC - Cerebellar Granule Cell' -> 'Cerebellar Granule Cell (GrC)')
    clean_k = neuron_key.lower().replace("-", " ").replace("(", " ").replace(")", " ")
    words = [w for w in clean_k.split() if len(w) > 2]
    for k in ADEX_TABLE_1:
        if any(w in k.lower() for w in words):
            return ADEX_TABLE_1[k].copy()
    raise KeyError(f"Neuron key '{neuron_key}' not found.")
