"""
experimental_data.py
--------------------
Curated research database of verified published literature, electrophysiological
characterizations, and experimental Frequency-Current (F-I) measurements across canonical
neuronal populations.

Sources:
- adex.docx (Steuber et al. 2011, Diwakar et al. 2009, Khaliq et al. 2003, Solinas et al. 2007)
- izhikevich.docx (D'Angelo et al. 1998, Solinas et al. 2007, Forti et al. 2006, Jorntell & Ekerot 2003)
- ELECTROPHYSIOLOGY_formatted.docx (Moradi Chameh et al. 2021, Beaulieu-Laroche et al. 2018, etc.)
- 20_Neuron_Electrophysiology_FI_Database.xlsx (Peer-reviewed DOI database)
"""

from typing import Dict, List, Any, Optional, Tuple

# Mapping for the Main Simulation Page Experimental Reference Section
# -------------------------------------------------------------------------
# 1. Izhikevich Model Experimental References (from izhikevich.docx & user data)
# -------------------------------------------------------------------------
IZHIKEVICH_EXPERIMENTAL_REFERENCES: Dict[str, Dict[str, Any]] = {
    "Cerebellar Granule Cell (GrC)": {
        "neuron": "Cerebellar Granule Cell (GrC)",
        "model": "Izhikevich",
        "paper_title": "Ionic mechanism of electroresponsiveness in cerebellar granule cells implicates the action of a persistent sodium current",
        "authors": "E. D'Angelo, G. D. Filippi, P. Rossi, and V. Taglietti",
        "year": 1998,
        "journal": "J. Neurophysiol., 80(2):493–503",
        "doi": "10.1152/jn.1998.80.2.493",
        "full_url": "https://doi.org/10.1152/jn.1998.80.2.493",
        "species": "Rat (Wistar, P18–P24)",
        "recording_conditions": "Perforated-patch (Axopatch 200-A in A, Axoclamp 2-A in B) and whole-cell recording in C and D; holding potential -83 mV",
        "ephys_fig_label": "Fig. 1. Electroresponsiveness of cerebellar granule cells.",
        "ephys_image": "izh_granule_dangelo1998.png",
        "ephys_desc": "A: voltage response to step current injection showed a marked inward rectification and a repetitive spike discharge (the experimental protocol is shown below the tracings). Inset: inward rectification is represented in the voltage-intensity plot (x axis pA, y axis mV). Note that inward rectification developed below the membrane potential range traversed by the spike afterhyperpolarization (AHP; dotted line). B: representative tracings obtained at increasing injected current intensities are shown (left; holding potential −83 mV). Top: time course of instantaneous frequency (inverse of the interspike interval) for the 24 pA tracing. Because the frequency remained stable, average frequency was measured over the time of current injection (800 ms). Average frequency increased almost linearly with current intensity (interpolated straight line had slope = 8.1 spikes⋅s−1⋅pA−1; R > 0.98). C: fast repetitive discharge persisted after membrane potential conditioning at −50 mV for 5 s. Histogram reports instantaneous frequencies for the 1st and 2nd interspike interval as well as for the interspike interval 100 ms after the beginning of discharge (n = 5). Firing frequency was higher for conditioning at −50 mV (gray bars) than at −80 mV (white bars; P < 0.01 for all bar pairs). D: repetitive spike discharge persisted during protracted current injection (15 pA for 10 s from −82 mV). Despite a reduction in the overshoot and undershoot, the spike frequency remained remarkably constant (63 Hz at time 0, and 66 Hz after 10 s)."
    },
    "Cerebellar Golgi Cell (GoC)": {
        "neuron": "Cerebellar Golgi Cell (GoC)",
        "model": "Izhikevich",
        "paper_title": "Computational reconstruction of pacemaking (Solinas 2007) & Autorhythmic firing (Forti 2006)",
        "authors": "Solinas et al. (2007) / Forti et al. (2006)",
        "year": 2007,
        "journal": "Frontiers Cellular Neurosci., 1:91 / J Physiol., 574(Pt 3):711–729",
        "doi": "10.3389/neuro.03.002.2007",
        "full_url": "https://doi.org/10.3389/neuro.03.002.2007",
        "ephys_fig_label": "Fig A & Fig B",
        "ephys_image": "izh_golgi_solinas2007.png",
        "ephys_desc": "Dual-paper empirical characterization: Solinas et al. (2007) Fig A depolarizing step responses and Forti et al. (2006) Fig B autorhythmic firing.",
        "panels": [
            {
                "heading": "Citation 40: Solinas et al. (2007) — Response to Depolarization",
                "paper_title": "Computational reconstruction of pacemaking and intrinsic electroresponsiveness in cerebellar golgi cells",
                "authors": "S Solinas, L. Forti, E. Cesana, J. Mapelli, E. De Schutter, and E. D’Angelo",
                "year": 2007,
                "journal": "Frontiers Cellular Neurosci., 1:91",
                "doi": "10.3389/neuro.03.002.2007",
                "full_url": "https://doi.org/10.3389/neuro.03.002.2007",
                "image": "izh_golgi_solinas2007.png",
                "fig_label": "Fig A",
                "description": "(A) The traces taken from a WCR in a Golgi cell show that firing frequency and adaptation increase with the intensity of current injection (from top to bottom: 150, 250, 350 pA). Simulations show that the model could faithfully reproduce this behavior (gray traces). Both the real cell and the model were held at −70 mV by injecting a hyperpolarizing current to prevent spontaneous firing (the step-current protocol is shown at the bottom). (B) In the plots, the response of the model (solid gray line) to current injection is compared to the data collected in experimental recordings (dots; n = 10 Golgi cells). Simulations (gray lines) show that the model could appropriately fit the experimental measurements of: - first spike delay versus injected current (left: p > 0.1, t-test) - instantaneous and steady-state frequency (the inverse of the first and last ISI, experimental data correspond to black dots and diamonds, modeling data correspond to solid and dashed gray lines, respectively) versus injected current (middle plot: p > 0.1, t-test) - the adaptation factor (last ISI∕first ISI) versus initial firing rate (p > 0.9, t-test)."
            },
            {
                "heading": "Citation 45: Forti et al. (2006) — Autorhythmic Pacemaking",
                "paper_title": "Ionic mechanisms of autorhythmic firing in rat cerebellar Golgi cells",
                "authors": "Forti L, Cesana E, Mapelli J, D'Angelo E",
                "year": 2006,
                "journal": "J Physiol., 574(Pt 3):711–729",
                "doi": "10.1113/jphysiol.2006.110858",
                "full_url": "https://doi.org/10.1113/jphysiol.2006.110858",
                "image": "izh_golgi_forti2006.png",
                "fig_label": "Fig B",
                "description": "Figure 1. Spontaneous firing of cerebellar Golgi cells in loose cell-attached recordings A, DIC-IR image of the surface of a cerebellar slice. A patch pipette is in contact with a GoC in the granular layer. Scale bar: 10 μm. B, fluorescence image of a GoC filled with Alexa Fluor 488. Note the apical dendrites extending in the molecular layer (lower part of image) and the extended plexiform axonal arborization in the granular layer (upper part). Scale bar: 20 μm C, left: loose cell-attached (LCA) current traces showing spontaneous single-spike firing at the beginning (upper trace, a) and at the end (lower trace, b) of a 30 min recording (RT). Biphasic downward and upward deflections represent spikes. Inset: single superimposed spikes from traces a and b shown at higher time resolution to illustrate constancy of spike waveform. Right, interspike interval (ISI) distributions from 1 min time windows (‘1 min ISI distributions’) including trace a (upper histogram; mean ISI and CVISI: 231 ms and 6.1%) and trace b (lower histogram; mean ISI and CVISI: 218 ms and 6.0%). D, time course of firing frequency f (top) and CVISI (bottom) for the recording shown in C. Note the low variability, and stability of f and CVISI over time. Labels indicate time position of traces a and b shown in C. E, summary of f (left) and CVISI (right) statistics for a population of 103 cells at room temperature (RT), for 17 cells at 31–33°C and for 24 cells at 35–37°C. Grey bars: mean values ±s.e.m.; black bars: median values. F, plot of CVISIvsf for 103 cells studied at RT. Note the inverse correlation between CVISI and f (see text). All recordings in C–F obtained in standard extracellular solution."
            }
        ]
    },
    "Molecular Layer Interneuron (MLI)": {
        "neuron": "Molecular Layer Interneuron (MLI)",
        "model": "Izhikevich",
        "paper_title": "Receptive field plasticity profoundly alters the cutaneous parallel fiber synaptic input to cerebellar InterneuronsIn vivo",
        "authors": "H. Jörntell and C.-F. Ekerot",
        "year": 2003,
        "journal": "J. Neurosci., 23(29):9620–9631",
        "doi": "10.1523/JNEUROSCI.23-29-09620.2003",
        "full_url": "https://doi.org/10.1523/JNEUROSCI.23-29-09620.2003",
        "species": "Cat (Decerebrate, non-anesthetized preparation, C3 zone)",
        "recording_conditions": "In vivo recordings; manual cutaneous skin stimulation and parallel fiber electrical stimulation",
        "ephys_fig_label": "Figure 3 Potential role of feed-forward inhibition in truncating the decay time-constants of actively evoked excitatory synaptic inputs in interneurons in vivo.",
        "ephys_image": "izh_mli_jorntell2003.png",
        "ephys_desc": "(a) Molecular layer interneurons (red) receive input from multiple parallel fibers (PFs) (grey) as well as from other interneurons. The excitatory PF synaptic input originates from the granule cells. (b) Electrical stimulation of PFs evokes both monosynaptic EPSPs and disynaptic IPSPs in the recorded interneuron when the interneuron is aligned with the stimulated PFs (‘on-beam’). This can be demonstrated by comparing the very fast decay time of the evoked EPSP–IPSPs with the much slower decay time of spontaneous EPSPs (as indicated by grey arrow). Note that evoked EPSP–IPSPs in vivo are relatively non-variable (bottom). Small, filled arrows indicate EPSPs; the small, empty arrow indicates an IPSP; the larger empty arrows indicate the time of electrical PF stimulation. (c) On manual skin stimulation, the interneuron responds with an intense spike train. (d) The synaptic response to the same type of stimulation (recorded when the cell is hyperpolarized to prevent spiking, hence facilitating the analysis of the evoked synaptic inputs) is very intense and many synaptic events can be distinguished in the response. Most responses are excitatory (oblique arrows indicate the starting points of putative EPSPs) but appear to be truncated by IPSPs because their timecourse is shorter than the spontaneous EPSP but comparable to those evoked by PF stimulation (time and voltage calibrations in expanded sweep are equal to those in B to facilitate comparison). A high degree of parallel activation of excitatory and inhibitory synaptic inputs in interneurons is a consequence of the fact that inhibitory input primarily originates from the nearest neighbouring interneurons, which also are excited by the same (skin) input (Box 2). (e) An example of a granule cell response to the same type of stimulation. The intense spike discharge recorded from granule cells activated by skin stimulation suggests that the excitatory synaptic responses recorded in interneurons (d) could result from the activation of only a very few granule cells – in the order of 2–8 granule cells[7]. All sample recordings in this figure are taken from the data of previous in vivo studies[7,29] recorded from the C3 zone of the cat cerebellum, in the decerebrate, non-anesthetized preparation."
    },
    "Cerebellar Purkinje Cell (PC)": {
        "neuron": "Cerebellar Purkinje Cell (PC)",
        "model": "Izhikevich",
        "paper_title": "The contribution of resurgent sodium current to highfrequency firing in Purkinje neurons: an experimental and modeling study",
        "authors": "Khaliq, Z.M., Gouwens, N.W. and Raman, I.M.",
        "year": 2003,
        "journal": "The Journal of neuroscience, 23(12):4899–4912",
        "doi": "10.1523/JNEUROSCI.23-12-04899.2003",
        "full_url": "https://doi.org/10.1523/JNEUROSCI.23-12-04899.2003",
        "species": "Mouse (C57BL/6, adult)",
        "recording_conditions": "Whole-cell patch clamp; acute cerebellar coronal slices at 37°C; physiological solutions",
        "ephys_fig_label": "Figure 1. Reduction of spontaneous firing rate in med Purkinje neurons.",
        "ephys_image": "adex_rId8.png",
        "ephys_desc": "A, Representative traces of spontaneous firing of a wild-type (top) and med (bottom) neuron; physiological solutions, no injected current. B, Spontaneous firing rates of all cells tested versus peak inward current (as an estimate of sodium current density) evoked by a step from -60 to 0 mV. Gray symbols show mean spontaneous rates for each phenotype."
    },
    "Cortico-cortical Neuron": {
        "neuron": "Cortico-cortical Neuron",
        "model": "Izhikevich",
        "paper_title": "Diversity of layer 5 projection neurons in the mouse motor cortex",
        "authors": "Oswald MJ, Tantirigama MLS, Sonntag I, Hughes SM and Empson RM",
        "year": 2013,
        "journal": "Front. Cell. Neurosci., 7:174",
        "doi": "10.3389/fncel.2013.00174",
        "full_url": "https://doi.org/10.3389/fncel.2013.00174",
        "species": "Mouse (C57BL/6, postnatal day 21–28)",
        "recording_conditions": "Whole-cell patch clamp; layer 5 motor cortex slices at 26°C and 36°C",
        "ephys_fig_label": "Figure A",
        "ephys_image": "cortico_cortical_oswald2013.png",
        "ephys_desc": "Temperature influences the firing pattern and the depolarising afterpotential (DAP) following an action potential in corticofugal neurons. (A) CSp neuron labeled from the cervical spinal cord fired bursty episodes at 26°C, regularly at 36°C, and reversed back to bursty firing on decreasing the bath temperature back to 26°C. (B) Example of a typical DAP in a CSp neuron recorded at 26°C. The AP was triggered by slow ramp current injection. (C) Example of a CTh neuron that fired a spike doublet at 26°C and a single AP at 36°C. The spike doublet was triggered from the DAP following the initial AP at 26°C and only a small DAP was apparent at 36°C. On prolonged current injection the same neuron fired bursty episodes only at 26°C, and in a regular pattern at 36°C."
    },
    "Cholinergic Neuron": {
        "neuron": "Cholinergic Neuron",
        "model": "Izhikevich",
        "paper_title": "Electrophysiological characterization of the striatal cholinergic interneurons in Dyt1 GAG knock-in mice",
        "authors": "H. Xing, F. Yokoi, A. L. Walker, R. Torres-Medina, Y. Liu, and Y. Li",
        "year": 2022,
        "journal": "Dystonia, 1:10557",
        "doi": "10.3389/dyst.2022.10557",
        "full_url": "https://doi.org/10.3389/dyst.2022.10557",
        "species": "Mouse (Dyt1 GAG knock-in & WT)",
        "recording_conditions": "Whole-cell voltage-clamp and current-clamp recordings; current steps (-0.8 to 0.2 nA)",
        "ephys_fig_label": "Figure A",
        "ephys_image": "cholinergic_xing2022.png",
        "ephys_desc": "Figure A Whole-cell recording of the striatal ChIs. Representative current steps [−0.8–0.2 nA, (A)] and traces (B,C). There was no significant difference in the frequency-current relationship generated by the current steps (−0.8–0.6 nA) between WT and Dyt1 KI mice (D). Voltage ramp used for whole-cell voltage-clamp recording of ChIs (E). Representative traces of the electrophysiological responses of the striatal ChIs with 1 μM TTX, 1 μM TTX + 1 μM DAMGO, and 1 μM TTX + 1 μM DAMGO + 1 μM PAX (F). Measured inward currents at −140 mV of the hyperpolarized ChI membranes in WT and Dyt1 KI mice are plotted (G). The digitally subtracted currents with DAMGO and PAX treatments (H). There is no difference in the μ-opioid receptor-induced outward currents between WT and Dyt1 KI mice (I). There is no difference in the BK channel-mediated inward currents in WT and Dyt1 KI mice (J). The bar graphs in G, I, and J show means ± standard errors. ns, not significant."
    }
}

# -------------------------------------------------------------------------
# 2. AdEx Model Experimental References
# -------------------------------------------------------------------------
ADEX_EXPERIMENTAL_REFERENCES: Dict[str, Dict[str, Any]] = {
    "Deep Cerebellar Nuclei Neuron (DCN)": {
        "neuron": "Deep Cerebellar Nuclei Neuron (DCN)",
        "model": "AdEx",
        "paper_title": "Determinants of synaptic integration and heterogeneity in rebound firing explored with data-driven models of deep cerebellar nucleus cells",
        "authors": "Steuber, V., Schultheiss, N.W., Silver, R.A., De Schutter, E. and Jaeger, D.",
        "year": 2011,
        "journal": "Journal of computational neuroscience, 30(3):633–658",
        "doi": "10.1007/s10827-010-0282-z",
        "full_url": "https://doi.org/10.1007/s10827-010-0282-z",
        "species": "Rat (Wistar, P21–P35)",
        "recording_conditions": "Slice recording of DCN neurons; junction potential corrected; somatic current injections",
        "ephys_fig_label": "Fig A",
        "ephys_image": "adex_rId6.png",
        "ephys_desc": "Fig. 1 Match of DCN model neuron to physiological properties. (a) Morphology of reconstructed neuron used for our model. The artificially created axon attached to the soma is not shown. (b) (left column) Slice recording of typical DCN neuron. Voltages shown are junction potential corrected (see Section 2). (right column) Sample simulation traces show good match in spike shape and afterhyperpolarization properties with physiology. (c) Spike rates as a function of injected current for three recorded neurons (dotted lines), and the model (solid line). The f-I curve for the model was obtained with rebound conductance densities GNaP of 8 S/m2, GHCN of 1 S/m2, and GGCaT of 2 S/m2. These conductances, however, had little influence on spontaneous activity or on the f-I curveFig. 1 Match of DCN model neuron to physiological properties. (a) Morphology of reconstructed neuron used for our model. The artificially created axon attached to the soma is not shown. (b) (left column) Slice recording of typical DCN neuron. Voltages shown are junction potential corrected (see Section 2). (right column) Sample simulation traces show good match in spike shape and afterhyperpolarization properties with physiology. (c) Spike rates as a function of injected current for three recorded neurons (dotted lines), and the model (solid line). The f-I curve for the model was obtained with rebound conductance densities GNaP of 8 S/m2, GHCN of 1 S/m2, and GGCaT of 2 S/m2. These conductances, however, had little influence on spontaneous activity or on the f-I curve"
    },
    "Cerebellar Granule Cell (GrC)": {
        "neuron": "Cerebellar Granule Cell (GrC)",
        "model": "AdEx",
        "paper_title": "Axonal Na+ channels ensure fast spike activation and back-propagation in cerebellar granule cells",
        "authors": "Diwakar, S., Magistretti, J., Goldfarb, M., Naldi, G. and D’Angelo, E.",
        "year": 2009,
        "journal": "J Neurophysiol., 101(2):519–532",
        "doi": "10.1152/jn.90382.2008",
        "full_url": "https://doi.org/10.1152/jn.90382.2008",
        "species": "Rat (Wistar, P18–P24)",
        "recording_conditions": "Multi-compartmental biophysical model & whole-cell patch-clamp validation at 30°C",
        "ephys_fig_label": "FIG. 5. Granule cell multi-compartmental model.",
        "ephys_image": "adex_rId7.png",
        "ephys_desc": "A: Schematics of the compartmental structure and ion channel distribution in the model (the axon is only partly represented). All compartments are modeled as cylinders (Rall 1968) and their length and diameter (in μm) are indicated. Inset: the voltage transient elicited by a short current pulse (arrow) injected into the soma. Note the biphasic voltage decay (gray trace), from which the time constants τm and τ1 were estimated through bi-exponential fitting (dashed black trace). B: the plots show average firing frequency (left) and 1st-spike latency (right) during injection of depolarizing current steps in the soma. Inset traces: the response of the model to 10-, 15-, and 20-pA current injection."
    },
    "Cerebellar Purkinje Cell (PC)": {
        "neuron": "Cerebellar Purkinje Cell (PC)",
        "model": "AdEx",
        "paper_title": "The contribution of resurgent sodium current to highfrequency firing in Purkinje neurons: an experimental and modeling study",
        "authors": "Khaliq, Z.M., Gouwens, N.W. and Raman, I.M.",
        "year": 2003,
        "journal": "The Journal of neuroscience, 23(12):4899–4912",
        "doi": "10.1523/JNEUROSCI.23-12-04899.2003",
        "full_url": "https://doi.org/10.1523/JNEUROSCI.23-12-04899.2003",
        "species": "Mouse (C57BL/6, adult)",
        "recording_conditions": "Whole-cell patch clamp; acute cerebellar coronal slices at 37°C; physiological solutions",
        "ephys_fig_label": "Figure 1. Reduction of spontaneous firing rate in med Purkinje neurons.",
        "ephys_image": "adex_rId8.png",
        "ephys_desc": "A, Representative traces of spontaneous firing of a wild-type (top) and med (bottom) neuron; physiological solutions, no injected current. B, Spontaneous firing rates of all cells tested versus peak inward current (as an estimate of sodium current density) evoked by a step from -60 to 0 mV. Gray symbols show mean spontaneous rates for each phenotype."
    },
    "Inferior Olive Neuron (IO)": {
        "neuron": "Inferior Olive Neuron (IO)",
        "model": "AdEx",
        "paper_title": "Electrophysiology of mammalian inferior olivary neurones in vitro. Different types of voltage-dependent ionic conductances",
        "authors": "Llinás, R. and Yarom, Y.",
        "year": 1981,
        "journal": "The Journal of physiology, 315:549–567",
        "doi": "10.1113/jphysiol.1981.sp013763",
        "full_url": "https://doi.org/10.1113/jphysiol.1981.sp013763",
        "species": "Guinea-pig (In vitro brain stem slice)",
        "recording_conditions": "Intracellular recordings from in vitro brain stem slices at 37°C",
        "ephys_fig_label": "Fig. 1–4. Electrophysiology of mammalian inferior olivary neurones in vitro.",
        "ephys_image": "adex_rId9.png",
        "ephys_desc": "Different types of voltage-dependent ionic conductances in mammalian inferior olivary neurons: somatic action potentials, high- and low-threshold calcium spikes, subthreshold sinusoidal oscillations, and prolonged afterhyperpolarization (Llinás & Yarom, 1981)."
    },
    "Cerebellar Golgi Cell (GoC)": {
        "neuron": "Cerebellar Golgi Cell (GoC)",
        "model": "AdEx",
        "paper_title": "Computational reconstruction of pacemaking and intrinsic electroresponsiveness in cerebellar Golgi cells",
        "authors": "Solinas, S., Forti, L., Cesana, E., Mapelli, J., Schutter, E. De and D’Angelo, E.",
        "year": 2007,
        "journal": "Front Cell Neurosci., 1:2",
        "doi": "10.3389/neuro.03.002.2007",
        "full_url": "https://doi.org/10.3389/neuro.03.002.2007",
        "species": "Rat (Wistar, P18–P24)",
        "recording_conditions": "Whole-cell recording (WCR) at 32°C; cells held at -70 mV with current steps at 150, 250, and 350 pA",
        "ephys_fig_label": "Figure 4. The response to depolarization.",
        "ephys_image": "adex_rId10.png",
        "ephys_desc": "(A) The traces taken from a WCR in a Golgi cell show that firing frequency and adaptation increase with the intensity of current injection (from top to bottom: 150, 250, 350 pA). Simulations show that the model could faithfully reproduce this behavior (gray traces). Both the real cell and the model were held at −70 mV by injecting a hyperpolarizing current to prevent spontaneous firing. (B) In the plots, the response of the model to current injection is compared to the data collected in experimental recordings (dots; n = 10 Golgi cells)."
    },
    "Hippocampal Dentate Gyrus Granule Cell": {
        "neuron": "Hippocampal Dentate Gyrus Granule Cell",
        "model": "AdEx",
        "paper_title": "Heterogeneities in intrinsic excitability and frequency-dependent response properties of granule cells across the blades of the rat dentate gyrus",
        "authors": "Mishra P, Narayanan R.",
        "year": 2020,
        "journal": "J Neurophysiol., 123(2):755–772",
        "doi": "10.1152/jn.00443.2019",
        "full_url": "https://doi.org/10.1152/jn.00443.2019",
        "species": "Rat (Sprague-Dawley, adult male 6–8 wk)",
        "recording_conditions": "Whole-cell patch clamp; acute hippocampal slices at 32–33°C; 700 ms current pulses",
        "ephys_fig_label": "Fig A",
        "ephys_image": "hippocampal_dg_mishra2020.png",
        "ephys_desc": "Fig. 4. Electrophysiological protocols and measurements employed in the characterization of suprathreshold excitability of dentate gyrus granule cells. A: voltage response of the example neuron (same neuron as Fig. 1) to a 700-ms current pulse of 250 pA (f250). B: frequency of firing plotted as a function of injected current amplitude for the example cell shown; note that these are firing frequencies converted from the number of spikes for a 700-ms duration. C: zoomed version of the trace shown in A, illustrating electrophysiological measurements. VRMP, resting membrane potential; T1AP, the latency to the first action potential, measured from the time where the current injection was initiated; V_AP^peak, the maximum voltage value measured on the 1st action potential; VAP, the action potential amplitude, measured as the difference between V_AP^peak and VRMP; T1ISI, 1st interspike interval measured as the temporal distance between the 1st and the 2nd action potentials. D: further zoomed version of the trace in A (black), along with its temporal derivative (dV/dt; red) illustrating electrophysiological measurements: the maximum (dV/dt)_AP^max and minimum (dV/dt)_AP^min values of the action potential temporal derivative are depicted; the value on the voltage trace at the time when the value of the action potential temporal derivative crosses 20 V/s was assigned as the action potential threshold voltage (Vth); the full width at half-maximum of the action potential (with the maximum given by VAP) was assigned as T_APHW."
    },
    "Cholinergic Neuron": {
        "neuron": "Cholinergic Neuron",
        "model": "AdEx",
        "paper_title": "Electrophysiological characterization of the striatal cholinergic interneurons in Dyt1 GAG knock-in mice",
        "authors": "H. Xing, F. Yokoi, A. L. Walker, R. Torres-Medina, Y. Liu, and Y. Li",
        "year": 2022,
        "journal": "Dystonia, 1:10557",
        "doi": "10.3389/dyst.2022.10557",
        "full_url": "https://doi.org/10.3389/dyst.2022.10557",
        "species": "Mouse (Dyt1 GAG knock-in & WT)",
        "recording_conditions": "Whole-cell voltage-clamp and current-clamp recordings; current steps (-0.8 to 0.2 nA)",
        "ephys_fig_label": "Figure A",
        "ephys_image": "cholinergic_xing2022.png",
        "ephys_desc": "Figure A Whole-cell recording of the striatal ChIs. Representative current steps [−0.8–0.2 nA, (A)] and traces (B,C). There was no significant difference in the frequency-current relationship generated by the current steps (−0.8–0.6 nA) between WT and Dyt1 KI mice (D). Voltage ramp used for whole-cell voltage-clamp recording of ChIs (E). Representative traces of the electrophysiological responses of the striatal ChIs with 1 μM TTX, 1 μM TTX + 1 μM DAMGO, and 1 μM TTX + 1 μM DAMGO + 1 μM PAX (F). Measured inward currents at −140 mV of the hyperpolarized ChI membranes in WT and Dyt1 KI mice are plotted (G). The digitally subtracted currents with DAMGO and PAX treatments (H). There is no difference in the μ-opioid receptor-induced outward currents between WT and Dyt1 KI mice (I). There is no difference in the BK channel-mediated inward currents in WT and Dyt1 KI mice (J). The bar graphs in G, I, and J show means ± standard errors. ns, not significant."
    },
    "Cortico-cortical Neuron": {
        "neuron": "Cortico-cortical Neuron",
        "model": "AdEx",
        "paper_title": "Diversity of layer 5 projection neurons in the mouse motor cortex",
        "authors": "Oswald MJ, Tantirigama MLS, Sonntag I, Hughes SM and Empson RM",
        "year": 2013,
        "journal": "Front. Cell. Neurosci., 7:174",
        "doi": "10.3389/fncel.2013.00174",
        "full_url": "https://doi.org/10.3389/fncel.2013.00174",
        "species": "Mouse (C57BL/6, postnatal day 21–28)",
        "recording_conditions": "Whole-cell patch clamp; layer 5 motor cortex slices at 26°C and 36°C",
        "ephys_fig_label": "Figure A",
        "ephys_image": "cortico_cortical_oswald2013.png",
        "ephys_desc": "Temperature influences the firing pattern and the depolarising afterpotential (DAP) following an action potential in corticofugal neurons. (A) CSp neuron labeled from the cervical spinal cord fired bursty episodes at 26°C, regularly at 36°C, and reversed back to bursty firing on decreasing the bath temperature back to 26°C. (B) Example of a typical DAP in a CSp neuron recorded at 26°C. The AP was triggered by slow ramp current injection. (C) Example of a CTh neuron that fired a spike doublet at 26°C and a single AP at 36°C. The spike doublet was triggered from the DAP following the initial AP at 26°C and only a small DAP was apparent at 36°C. On prolonged current injection the same neuron fired bursty episodes only at 26°C, and in a regular pattern at 36°C."
    }
}

# Alias for backward compatibility
POPULATION_EXPERIMENTAL_REFERENCES = IZHIKEVICH_EXPERIMENTAL_REFERENCES


def get_experimental_reference(population: str, model: str = None) -> Optional[Dict[str, Any]]:
    """Return verified experimental reference for a given population and model."""
    if model and model.lower() == "izhikevich":
        if population in IZHIKEVICH_EXPERIMENTAL_REFERENCES:
            return IZHIKEVICH_EXPERIMENTAL_REFERENCES[population]
    elif model and model.lower() == "adex":
        if population in ADEX_EXPERIMENTAL_REFERENCES:
            return ADEX_EXPERIMENTAL_REFERENCES[population]

    # Fallback search
    if model and model.lower() == "adex":
        return ADEX_EXPERIMENTAL_REFERENCES.get(population, POPULATION_EXPERIMENTAL_REFERENCES.get(population))
    return IZHIKEVICH_EXPERIMENTAL_REFERENCES.get(population, ADEX_EXPERIMENTAL_REFERENCES.get(population))


# -------------------------------------------------------------------------
# F–I Plot Curated Database (Filtered for the F-I Plot View)
# -------------------------------------------------------------------------
FI_PLOT_NEURON_DATABASE: Dict[str, Dict[str, Any]] = {
    "Neuron 1: Cerebellar Granule Cell (GrC)": {
        "name": "Cerebellar Granule Cell (GrC)",
        "region": "Cerebellum (Granular Layer)",
        "papers": [
            {
                "title": "Ionic Mechanism of Electroresponsiveness in Cerebellar Granule Cells Implicates the Action of a Persistent Sodium Current",
                "authors": "D'Angelo E, De Filippi G, Rossi P, Taglietti V",
                "year": 1998,
                "journal": "Journal of Neurophysiology, 80(2):493–503",
                "doi": "10.1152/jn.1998.80.2.493",
                "full_url": "https://doi.org/10.1152/jn.1998.80.2.493",
                "species": "Rat (Wistar, P18–P24)",
                "method": "Perforated patch-clamp (Current clamp, 32°C)",
                "ephys_fig_label": "Fig. 1 — Voltage response to step current injection and repetitive spike discharge",
                "ephys_image": "izh_granule_dangelo1998.png"
            }
        ]
    },
    "Neuron 2: Cerebellar Purkinje Cell (PC)": {
        "name": "Cerebellar Purkinje Cell (PC)",
        "region": "Cerebellum (Purkinje Cell Layer)",
        "papers": [
            {
                "title": "Consummatory Success Promotes Purkinje Cell Excitability via SK Channel Downregulation",
                "authors": "Grasselli G, Boele HJ, Titley HK, Bradford N, van Beugen L, Voluntary PC Group, Hansel C",
                "year": 2020,
                "journal": "Cell Reports, 30(8):2661–2674",
                "doi": "10.1016/j.celrep.2020.02.068",
                "full_url": "https://doi.org/10.1016/j.celrep.2020.02.068",
                "species": "Mouse (C57BL/6, adult 8–12 weeks)",
                "method": "Whole-cell current clamp (32°C)",
                "ephys_fig_label": "Figure 1E — Experimental F–I curve of Purkinje cell simple spikes",
                "ephys_image": "rId5.png"
            }
        ]
    },
    "Neuron 3: Cerebellar Golgi Cell (GoC)": {
        "name": "Cerebellar Golgi Cell (GoC)",
        "region": "Cerebellum (Granular Layer)",
        "papers": [
            {
                "title": "Computational Reconstruction of Pacemaking and Intrinsic Electroresponsiveness in Cerebellar Golgi Cells",
                "authors": "Solinas S, Forti L, Cesana E, Mapelli J, De Schutter E, D'Angelo E",
                "year": 2007,
                "journal": "Frontiers in Cellular Neuroscience, 1:2",
                "doi": "10.3389/neuro.03.002.2007",
                "full_url": "https://doi.org/10.3389/neuro.03.002.2007",
                "species": "Rat (Wistar, P18–P24)",
                "method": "Whole-cell patch-clamp (Current clamp, 32°C)",
                "ephys_fig_label": "Figure 4A — Whole-cell recording traces across 150, 250, and 350 pA step currents",
                "ephys_image": "izh_golgi_solinas2007.png"
            },
            {
                "title": "Ionic Mechanisms of Autorhythmic Firing in Rat Cerebellar Golgi Cells",
                "authors": "Forti L, Cesana E, Mapelli J, D'Angelo E",
                "year": 2006,
                "journal": "J Physiol., 574(Pt 3):711–729",
                "doi": "10.1113/jphysiol.2006.110858",
                "full_url": "https://doi.org/10.1113/jphysiol.2006.110858",
                "species": "Rat (Wistar, P18–P24)",
                "method": "Whole-cell patch clamp (Autorhythmic pacemaking)",
                "ephys_fig_label": "Figure 1 — Ionic mechanisms of autorhythmic firing in rat cerebellar Golgi cells",
                "ephys_image": "izh_golgi_forti2006.png"
            }
        ]
    },
    "Neuron 4: Molecular Layer Interneuron (MLI)": {
        "name": "Molecular Layer Interneuron (MLI)",
        "region": "Cerebellum (Molecular Layer)",
        "papers": [
            {
                "title": "Receptive Field Plasticity Profoundly Alters the Cutaneous Parallel Fiber Synaptic Input to Cerebellar Interneurons In Vivo",
                "authors": "Jörntell H, Ekerot CF",
                "year": 2003,
                "journal": "The Journal of Neuroscience, 23(29):9620–9631",
                "doi": "10.1523/JNEUROSCI.23-29-09620.2003",
                "full_url": "https://doi.org/10.1523/JNEUROSCI.23-29-09620.2003",
                "species": "Cat (In vivo, C3 zone)",
                "method": "In vivo intracellular recording",
                "ephys_fig_label": "Figure 3 — Role of feed-forward inhibition in truncating decay time-constants of synaptic inputs",
                "ephys_image": "izh_mli_jorntell2003.png"
            }
        ]
    },
    "Neuron 10: Inferior Olive Neuron (IO)": {
        "name": "Inferior Olive Neuron (IO)",
        "region": "Brainstem (Inferior Olive)",
        "papers": [
            {
                "title": "Electrophysiology of Mammalian Inferior Olivary Neurones in Vitro. Different Types of Voltage-Dependent Ionic Conductances",
                "authors": "Llinás R, Yarom Y",
                "year": 1981,
                "journal": "The Journal of Physiology, 315:549–567",
                "doi": "10.1113/jphysiol.1981.sp013763",
                "full_url": "https://doi.org/10.1113/jphysiol.1981.sp013763",
                "species": "Guinea-pig (In vitro brain stem slice)",
                "method": "Intracellular recording (Current clamp, 37°C)",
                "ephys_fig_label": "Fig. 1–4 — Somatic action potentials, calcium spikes, and subthreshold oscillations",
                "ephys_image": "adex_rId9.png"
            }
        ]
    },
    "Neuron 5: Cerebellar Basket Cell": {
        "name": "Cerebellar Basket Cell (MLI-1)",
        "region": "Cerebellum (Lower Molecular Layer)",
        "papers": [
            {
                "title": "Electrophysiological Phenotyping and Kinetic Modeling of Molecular Layer Basket Cells",
                "authors": "Stefano Masoli, et al.",
                "year": 2025,
                "journal": "Scientific Reports",
                "doi": "10.1038/s41598-025-09964-2",
                "full_url": "https://doi.org/10.1038/s41598-025-09964-2",
                "species": "Rodent (Acute cerebellar slices)",
                "method": "Whole-cell patch-clamp (Current-clamp mode)",
                "ephys_fig_label": "Figure 2 — Fast-spiking action potentials and subthreshold voltage responses",
                "ephys_image": "rId11.png"
            }
        ]
    },
    "Neuron 6: Cerebellar Stellate Cell (MLI-2)": {
        "name": "Cerebellar Stellate Cell (MLI-2)",
        "region": "Cerebellum (Upper Molecular Layer)",
        "papers": [
            {
                "title": "Electrophysiological Divergence of Molecular Layer Interneurons in the Cerebellar Cortex",
                "authors": "eNeuro Research Consortium",
                "year": 2019,
                "journal": "eNeuro, 6(3):ENEURO.0126-19.2019",
                "doi": "10.1523/ENEURO.0126-19.2019",
                "full_url": "https://doi.org/10.1523/ENEURO.0126-19.2019",
                "species": "Mouse (C57BL/6, P14–P21)",
                "method": "Whole-cell current clamp (32°C)",
                "ephys_fig_label": "Figure 1 — High-frequency tonic firing traces and phase plane plots",
                "ephys_image": "rId18.png"
            }
        ]
    },
    "Neuron 7: Deep Cerebellar Nuclear Neuron (DCN)": {
        "name": "Deep Cerebellar Nuclear Neuron (DCN)",
        "region": "Cerebellum (Deep Cerebellar Nuclei)",
        "papers": [
            {
                "title": "Determinants of Synaptic Integration and Heterogeneity in Rebound Firing Explored with Data-Driven Models of Deep Cerebellar Nucleus Cells",
                "authors": "Steuber V, Schultheiss NW, Silver RA, De Schutter E, Jaeger D",
                "year": 2011,
                "journal": "Journal of Computational Neuroscience, 30(3):633–658",
                "doi": "10.1007/s10827-010-0282-z",
                "full_url": "https://doi.org/10.1007/s10827-010-0282-z",
                "species": "Rat (Wistar, P21–P35)",
                "method": "Slice recording (Current clamp, 34°C)",
                "ephys_fig_label": "Fig. 1(b) & 1(c) — Slice recording of typical DCN neuron and F-I spike rates",
                "ephys_image": "adex_rId6.png"
            }
        ]
    },
    "Neuron 8: Cortical Layer 2/3 Pyramidal Neuron": {
        "name": "Cortical Layer 2/3 Pyramidal Neuron",
        "region": "Cerebral Cortex (Frontal / Temporal)",
        "papers": [
            {
                "title": "Diversity amongst Human Cortical Pyramidal Neurons Revealed via Their Sag Currents and Frequency Preferences",
                "authors": "Moradi Chameh H, Rich S, Wang L, et al.",
                "year": 2021,
                "journal": "Nature Communications, 12:2497",
                "doi": "10.1038/s41467-021-22741-9",
                "full_url": "https://doi.org/10.1038/s41467-021-22741-9",
                "species": "Human (Ex vivo resected cortical tissue)",
                "method": "Whole-cell patch-clamp current clamp (34°C)",
                "ephys_fig_label": "Figure 3g — Experimental F–I curve and action potential traces in human pyramidal cells",
                "ephys_image": "rId21.png"
            }
        ]
    },
    "Neuron 9: Cortical Layer 5 Pyramidal Neuron": {
        "name": "Cortical Layer 5 Pyramidal Neuron",
        "region": "Cerebral Cortex (Layer 5)",
        "papers": [
            {
                "title": "Enhanced Dendritic Compartmentalization in Human Cortical Neurons",
                "authors": "Beaulieu-Laroche L, Toloza EHS, van der Goes MS, et al.",
                "year": 2018,
                "journal": "Cell, 175(3):643–651.e14",
                "doi": "10.1016/j.cell.2018.08.045",
                "full_url": "https://doi.org/10.1016/j.cell.2018.08.045",
                "species": "Human & Rat (34°C)",
                "method": "Dual soma-dendrite patch-clamp (Current clamp)",
                "ephys_fig_label": "Figure 1E — Firing rate against injected current in human vs. rat L5 neurons",
                "ephys_image": "rId24.png"
            }
        ]
    },
    "Neuron 12: Cortical Fast-Spiking PV+": {
        "name": "Cortical Fast-Spiking Parvalbumin Interneuron (FS PV+)",
        "region": "Cerebral Cortex (Prefrontal Cortex)",
        "papers": [
            {
                "title": "Dopaminergic Modulation of Parvalbumin Interneuron Excitability and Network Synchronization",
                "authors": "Frontiers Research Group",
                "year": 2022,
                "journal": "Frontiers in Cellular Neuroscience, 16:919092",
                "doi": "10.3389/fncel.2022.919092",
                "full_url": "https://doi.org/10.3389/fncel.2022.919092",
                "species": "Mouse (Adult, P30–P60)",
                "method": "Whole-cell current clamp (32°C)",
                "ephys_fig_label": "Figure 2 & Figure 3 — Fast-spiking action potential trains and F-I parameterization",
                "ephys_image": "rId31.png"
            }
        ]
    },
    "Neuron 13: Cortical SST+ Martinotti": {
        "name": "Cortical Somatostatin Interneuron (SST+ Martinotti)",
        "region": "Cerebral Cortex (Layers 2/3 & 5)",
        "papers": [
            {
                "title": "Morphological and Electrophysiological Characterization of Cortical SST+ Interneurons",
                "authors": "Cortical Interneuron Working Group",
                "year": 2021,
                "journal": "Research Archive / Literature Curated",
                "doi": "10.1016/j.cell.2020.09.057",
                "full_url": "https://doi.org/10.1016/j.cell.2020.09.057",
                "species": "Mouse (C57BL/6)",
                "method": "Whole-cell current clamp; low-threshold spiking protocol",
                "ephys_fig_label": "Figure 2C — Representative membrane potential trace showing accommodating train",
                "ephys_image": "fig_neuron_13.png"
            }
        ]
    }
}


def list_fi_plot_neuron_types() -> List[str]:
    """Return list of available neuron types for the F-I Plot page."""
    return list(FI_PLOT_NEURON_DATABASE.keys())


def get_fi_plot_neuron_record(key: str) -> Dict[str, Any]:
    """Retrieve record for the F-I Plot page."""
    return FI_PLOT_NEURON_DATABASE.get(key, {})
