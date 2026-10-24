# Computational Neuronal Firing Pattern Library

A modular computational neuroscience platform and Streamlit graphical user interface (GUI) designed to simulate canonical neuronal firing dynamics, explore source-verified physiological parameters, and investigate empirical Frequency–Current (F–I) relationships from peer-reviewed electrophysiology literature.

---

## 1. Project Architecture

The codebase maintains a modular, decoupled architecture:

```text
neuron_library/
├── app.py                   # Streamlit GUI application (Frontend & Navigation)
├── models/
│   ├── __init__.py          # Models package export
│   ├── adex.py              # Adaptive Exponential Integrate-and-Fire simulation engine
│   └── izhikevich.py        # Dimensional Izhikevich neuron model simulation engine
├── models.py                # Backward-compatibility re-export wrapper
├── parameters.py            # Source-separated electrophysiological parameter databases
├── experimental_data.py     # Curated research database of verified publications & F–I data
├── plotting.py              # Publication-grade plotting for simulations & experimental curves
├── analysis.py              # Spike detection, ISI, and firing frequency analysis
├── data/
│   └── figures/             # High-resolution original published figure panels & traces
├── test_simulation.py       # Standalone backend validation test script
├── test_comprehensive.py    # 10-point automated test suite for all prompt specifications
├── requirements.txt         # Project dependencies
└── README.md                # Documentation and setup instructions
```

---

## 2. Models & Mathematical Formulations

### A. Izhikevich Model (Table S4)
Simulates canonical cortical and cerebellar neurons using Eugene Izhikevich's dimensional formulation:

$$\begin{aligned}
C \frac{dv}{dt} &= k(v - v_r)(v - v_t) - u + I \\[6pt]
\frac{du}{dt} &= a [ b(v - v_r) - u ]
\end{aligned}$$

**After-Spike Reset Rule:**
$$\text{If } v(t) \ge v_{\text{peak}} \implies v \leftarrow c, \quad u \leftarrow u + d$$

- **$a$**: Time scale of recovery variable $u$ ($\text{ms}^{-1}$)
- **$b$**: Subthreshold sensitivity ($\text{nS}$)
- **$c$**: Post-spike reset membrane potential ($\text{mV}$)
- **$d$**: Spike-triggered recovery increment ($\text{pA}$)
- **$k$**: Rheobase / subthreshold quadratic scaling factor ($\text{nS/mV}$)
- **$v_r, v_t, C$**: Configurable physical baseline defaults ($\text{mV}, \text{pF}$)

### B. Adaptive Exponential Integrate-and-Fire (AdEx) Model (Table S5 & Table 1)
Simulates subthreshold resonance, exponential spike initiation, and spike-frequency adaptation (Brette & Gerstner, 2005):

$$\begin{aligned}
C \frac{dV}{dt} &= -g_L (V - E_L) + g_L \Delta_T \exp\left( \min\left(\frac{V - V_T}{\Delta_T}, 20\right) \right) - w + I \\[6pt]
\tau_w \frac{dw}{dt} &= a (V - E_L) - w
\end{aligned}$$

**After-Spike Reset Rule:**
$$\text{If } V(t) \ge V_{\text{cut}} \implies V \leftarrow V_r, \quad w \leftarrow w + b$$

---

## 3. Parameter Databases & Literature Sources

The library explicitly separates source-specific parameter sets without mixing:
1. **Reference Table S4 (Izhikevich)**: Optimized parameters for Pyramidal, Granule, Golgi, Purkinje, Cholinergic, and Cortico-cortical neurons.
2. **Reference Table S5 (AdEx Multi-Neuron)**: Optimized parameters for Pyramidal, Granule, Golgi, Purkinje, Hippocampal Dentate Gyrus Granule, and Cholinergic neurons.
3. **Reference Table 1 (Canonical Cerebellar AdEx)**: Parameters for GrC, GoC, PC, IO, and DCN cerebellar neurons.

---

## 4. F–I Plot & Experimental Electrophysiology Hierarchy

The application includes a structured empirical research navigation menu:

```text
F–I Plot Hierarchy:
  └── Step 1: Select Neuron Type (20 curated neuronal types)
        └── Step 2: Select Experimental Paper (Verified literature records)
              ├── Step 3: View Experimental F–I Plot (Empirical points with error bars)
              ├── Step 4: View Experimental Electrophysiology (Published traces & conditions)
              └── Step 5: View Citation and Source Panel (Full APA citation & paper link)
```

- **Strict Empirical Integrity**: Simulated data and experimental data are clearly separated.
- **Graceful Handling of Missing Data**: Papers without an empirical F–I curve explicitly display:
  `No verified experimental F–I graph is available for this paper.`
- **Published Figure Panels**: Original figures extracted from the dossier (`ELECTROPHYSIOLOGY_formatted.docx`) are rendered directly alongside recording conditions and extraction methods.

---

## 5. Setup & Running Instructions

### Step 1: Install Dependencies
```bash
python -m pip install -r requirements.txt
```

### Step 2: Run Verification Test Suites
```bash
# Run baseline simulation check
python test_simulation.py

# Run comprehensive 10-point specification verification
python test_comprehensive.py
```

### Step 3: Launch the Streamlit Web Application
```bash
streamlit run app.py
```
