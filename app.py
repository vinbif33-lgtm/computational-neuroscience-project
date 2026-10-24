"""
app.py
------
Computational Neuronal Firing Pattern Library
Streamlit Graphical User Interface.

Features:
- Dual-Mode Navigation:
    1. Simulation Controls & Main Dashboard (Izhikevich & AdEx Models)
    2. F–I Plot & Literature Electrophysiology Navigation
- Izhikevich Model:
    dv/dt = k * v^2 + 5 * v + 140 - u + I(t)
    du/dt = a * (bv - u)
    If v >= 30 mV: v <- c, u <- u + d
    Simplified visible parameter table (a, b, d, k, I) with c managed internally.
- AdEx Model:
    Cm * dV/dt = -gL*(V - EL) + gL*Delta_T*exp((V - VT)/Delta_T) - w + I(t)
    tau_w * dw/dt = a*(V - EL) - w
    If V >= Vcut: V <- Vr, w <- w + b
    Specific populations (GrC, GoC, PC, Cholinergic, DCN with 20 A current).
- Main Simulation Page Order:
    1. Title & Subtitle
    2. Selected population & model information
    3. Source-specific parameter table & model notes
    4. Simulation settings & Generate Firing Pattern
    5. Membrane potential & recovery/adaptation plots
    6. CSV download button
    7. Experimental electrophysiology figure
    8. Experimental F–I curve
    9. Full paper citation, figure identifiers, and source links
- Cleaned F-I Plot page:
    Step 3 removed, genuine figure panel captions, no internal filenames, no standalone PMC button.
"""

import os
from typing import Dict, Any, List
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

# Backend imports
from parameters import (
    IZHIKEVICH_POPULATIONS,
    ADEX_POPULATIONS,
    PARAM_METADATA,
    get_supported_populations,
    is_population_supported,
    get_available_datasets_for_population,
    get_neuron_parameters
)
from models import simulate_adex, simulate_izhikevich
from analysis import analyze_firing_pattern
from experimental_data import (
    get_experimental_reference,
    list_fi_plot_neuron_types,
    get_fi_plot_neuron_record
)
from plotting import plot_membrane_trace

# -----------------------------------------------------------------------------
# Streamlit Page Configuration & Dark Styling
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Computational Neuronal Firing Pattern Library",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for rich dark aesthetics
st.markdown("""
<style>
    /* Metric Cards */
    div[data-testid="stMetricValue"] {
        font-size: 1.35rem !important;
        font-weight: 700;
        color: #58A6FF !important;
    }
    div[data-testid="stMetricLabel"] {
        font-size: 0.85rem !important;
        color: #8B949E !important;
    }
    .badge {
        display: inline-block;
        padding: 0.22rem 0.55rem;
        font-size: 0.75rem;
        font-weight: 600;
        border-radius: 9999px;
        margin-right: 0.35rem;
        margin-bottom: 0.25rem;
    }
    .badge-blue { background-color: #1F6FEB22; color: #58A6FF; border: 1px solid #1F6FEB66; }
    .badge-green { background-color: #23863622; color: #3FB950; border: 1px solid #23863666; }
    .badge-purple { background-color: #8957E522; color: #BC8CFF; border: 1px solid #8957E566; }
    .badge-amber { background-color: #D2992222; color: #D29922; border: 1px solid #D2992266; }
    .citation-box {
        background-color: #161B22;
        border: 1px solid #30363D;
        border-radius: 8px;
        padding: 1.2rem;
        margin-top: 1rem;
    }
    .figure-caption-tag {
        background-color: #0D1117;
        border-left: 3px solid #58A6FF;
        padding: 0.5rem 0.8rem;
        font-size: 0.85rem;
        color: #C9D1D9;
        margin-top: 0.4rem;
        border-radius: 0 4px 4px 0;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# Session State Initialization
# -----------------------------------------------------------------------------
if "nav_mode" not in st.session_state:
    st.session_state["nav_mode"] = "Simulation Controls"
if "selected_model" not in st.session_state:
    st.session_state["selected_model"] = "Izhikevich"
if "selected_pop" not in st.session_state:
    st.session_state["selected_pop"] = "Cerebellar Granule Cell (GrC)"

# -----------------------------------------------------------------------------
# 1. Application Title and Subtitle
# -----------------------------------------------------------------------------
st.title("Computational Neuronal Firing Pattern Library")
st.caption("Canonical Electrophysiological Characterization using the Adaptive Exponential Integrate-and-Fire (AdEx) and Izhikevich Models")

st.markdown("""
Welcome to the computational electrophysiology platform. This library enables interactive simulation
of canonical neuronal firing patterns, inspection of source-verified physiological parameters, and direct
exploration of empirical frequency–current (F–I) relationships and electrophysiology literature.
""")

# Top Navigation Mode Selector
nav_choice = st.radio(
    "Navigation Mode",
    options=["Simulation Controls", "F–I Plot"],
    horizontal=True,
    index=0 if st.session_state["nav_mode"] == "Simulation Controls" else 1,
    label_visibility="collapsed"
)
st.session_state["nav_mode"] = nav_choice

st.divider()

# Figures directory
FIGURES_DIR = os.path.join(os.path.dirname(__file__), "data", "figures")


# =============================================================================
# VIEW 1: MAIN SIMULATION CONTROLS & DYNAMICS
# =============================================================================
if st.session_state["nav_mode"] == "Simulation Controls":
    # -------------------------------------------------------------------------
    # Sidebar: Simulation Controls
    # -------------------------------------------------------------------------
    st.sidebar.header("Simulation Controls")

    # Select Neuron Model
    model_options = ["Izhikevich", "AdEx"]
    m_idx = model_options.index(st.session_state["selected_model"]) if st.session_state["selected_model"] in model_options else 0
    selected_model = st.sidebar.selectbox(
        "Select Neuron Model",
        options=model_options,
        index=m_idx,
        help="Select model equations: Izhikevich (Table S4) or AdEx (Table 1 & Table S5)."
    )

    if selected_model != st.session_state["selected_model"]:
        st.session_state["selected_model"] = selected_model
        # Reset population to default of new model
        supported_for_model = get_supported_populations(selected_model)
        st.session_state["selected_pop"] = supported_for_model[0]

    # Select Neuronal Population (Filtered strictly per model)
    allowed_populations = get_supported_populations(selected_model)
    current_pop_idx = (
        allowed_populations.index(st.session_state["selected_pop"])
        if st.session_state["selected_pop"] in allowed_populations
        else 0
    )

    selected_population = st.sidebar.selectbox(
        "Select Neuronal Population",
        options=allowed_populations,
        index=current_pop_idx,
        help=f"Supported neuronal populations for the {selected_model} model."
    )
    st.session_state["selected_pop"] = selected_population

    # AdEx dataset source selection if multiple available (e.g. Table 1 vs Table S5)
    dataset_source = None
    if selected_model == "AdEx":
        avail_datasets = get_available_datasets_for_population(selected_model, selected_population)
        if len(avail_datasets) > 1:
            dataset_source = st.sidebar.selectbox(
                "Parameter Table Source:",
                options=avail_datasets,
                index=0,
                help="Select between Reference Table 1 (Canonical Cerebellar) or Table S5."
            )
        elif avail_datasets:
            dataset_source = avail_datasets[0]

    # Load baseline parameters
    base_params = get_neuron_parameters(selected_model, selected_population, dataset_source)

    st.sidebar.subheader("Simulation Parameters")

    # Population-specific widget keys to ensure proper parameter initialization
    pop_key = f"{selected_model}_{selected_population}_{dataset_source}"

    # Simulation Duration
    default_dur = float(base_params.get("default_duration_ms", 500.0))
    duration_ms = st.sidebar.number_input(
        "Simulation Duration (ms):",
        min_value=10.0,
        max_value=5000.0,
        value=default_dur,
        step=50.0,
        key=f"dur_{pop_key}",
        help="Total simulation time window in milliseconds."
    )

    # Integration Time Step dt
    dt_ms = st.sidebar.number_input(
        "Integration Time Step dt (ms):",
        min_value=0.001,
        max_value=0.5,
        value=0.010,
        step=0.005,
        format="%.3f",
        key=f"dt_{pop_key}",
        help="Time step for numerical integration."
    )

    # Injected Current handling
    default_I = float(base_params.get("I", 0.0))
    current_unit = base_params.get("current_unit", "pA")

    custom_I = st.sidebar.number_input(
        f"Injected Current I ({current_unit}):",
        min_value=-500.0,
        max_value=3000.0,
        value=default_I,
        step=10.0,
        key=f"I_{pop_key}",
        help=f"Applied current step in {current_unit}."
    )

    # Spike Reset Parameters
    st.sidebar.subheader("Spike Reset Parameters")

    if selected_model == "AdEx":
        default_vpeak = float(base_params.get("Vcut", 0.0))
        default_vreset = float(base_params.get("Vr", -60.0))

        V_peak = st.sidebar.number_input(
            "Spike Cutoff Threshold V_cut (mV):",
            min_value=-40.0,
            max_value=80.0,
            value=default_vpeak,
            step=1.0,
            key=f"vpeak_{pop_key}",
            help="Membrane potential cutoff threshold triggering spike reset."
        )
        V_reset = st.sidebar.number_input(
            "Post-Spike Reset Voltage V_r (mV):",
            min_value=-120.0,
            max_value=-20.0,
            value=default_vreset,
            step=1.0,
            key=f"vreset_{pop_key}",
            help="Membrane voltage to which cell resets after spike."
        )
    else:
        # Izhikevich model: threshold is strictly 30.0 mV per model definition
        st.sidebar.markdown("**Spike Threshold (V_peak):** Fixed at `30.0 mV`")
        st.sidebar.caption("The exact Izhikevich equation requires spike reset when v >= 30 mV.")
        V_peak = 30.0
        default_c = float(base_params.get("c", -55.0))
        V_reset = st.sidebar.number_input(
            "Post-Spike Reset Potential c (mV):",
            min_value=-100.0,
            max_value=-30.0,
            value=default_c,
            step=0.5,
            key=f"c_{pop_key}",
            help="Post-spike membrane potential reset value c from Table S4."
        )

    # Reset to Source Defaults button
    if st.sidebar.button("Reset to Source Defaults", use_container_width=True):
        st.rerun()

    st.sidebar.divider()
    generate_btn = st.sidebar.button("Generate Firing Pattern", type="primary", use_container_width=True)

    # -------------------------------------------------------------------------
    # 2. Selected Neuronal Population & Model Information
    # -------------------------------------------------------------------------
    active_params = base_params.copy()
    active_params["I"] = custom_I
    if selected_model == "AdEx":
        active_params["Vcut"] = V_peak
        active_params["Vr"] = V_reset
    else:
        active_params["V_peak"] = 30.0
        active_params["c"] = V_reset

    # -------------------------------------------------------------------------
    # 3. Source-Specific Parameter Table and Model Notes
    # -------------------------------------------------------------------------
    col_tbl, col_nts = st.columns([1.25, 0.75])

    with col_tbl:
        st.subheader(f"Parameter Table: {selected_population}")
        st.markdown(f"**Model:** `{selected_model}` &nbsp;|&nbsp; **Source:** `{active_params.get('source', '')}`")
        st.write(f"**Description:** {active_params.get('description', '')}")

        # Construct visible parameter table
        table_rows = []
        if selected_model == "Izhikevich":
            # Display all Table S4 parameters: a, b, c, d, k, Injected current I
            izh_keys = ["a", "b", "c", "d", "k"]
            for k in izh_keys:
                meta = PARAM_METADATA.get(f"izh_{k}", {})
                table_rows.append({
                    "Parameter Symbol": k,
                    "Description": meta.get("name", k),
                    "Value": active_params[k],
                    "Unit": meta.get("unit", "-"),
                    "Source": "Table S4 (Optimized Parameters)"
                })
            # Add Injected Current I
            table_rows.append({
                "Parameter Symbol": "I",
                "Description": "Injected / Applied Current Step",
                "Value": active_params["I"],
                "Unit": active_params.get("current_unit", "pA"),
                "Source": "Table S4 Protocol"
            })
        else:
            # AdEx parameters: C, gL, EL, VT, Delta_T, tau_w, a, b, Vr, Vcut, I
            adex_keys = ["C", "gL", "EL", "VT", "Delta_T", "tau_w", "a", "b", "Vr", "Vcut"]
            for k in adex_keys:
                meta = PARAM_METADATA.get(k, {})
                val = active_params.get(k)
                if val is None and k == "C":
                    val = active_params.get("Cm")
                table_rows.append({
                    "Parameter Symbol": k,
                    "Description": meta.get("name", k),
                    "Value": val,
                    "Unit": meta.get("unit", "-"),
                    "Source": active_params.get("source", "Table 1 / Table S5")
                })
            # Injected current
            table_rows.append({
                "Parameter Symbol": "I",
                "Description": "Injected Current Step",
                "Value": active_params["I"],
                "Unit": active_params.get("current_unit", "pA"),
                "Source": "Table Protocol"
            })

        df_params = pd.DataFrame(table_rows)
        st.dataframe(df_params, use_container_width=True, hide_index=True)

    with col_nts:
        st.subheader("Model & Parameter Notes")
        if selected_model == "Izhikevich":
            st.info(
                f"**Izhikevich Model Equations:**\n\n"
                r"$$\frac{dv}{dt} = kv^2 + 5v + 140 - u + I(t)$$" + "\n\n"
                r"$$\frac{du}{dt} = a(bv - u)$$" + "\n\n"
                f"**Spike Reset Condition:**\n"
                r"$$\text{If } v \ge 30\text{ mV} \implies v \leftarrow c,\quad u \leftarrow u + d$$" + "\n\n"
                f"• **Spike Detection Threshold:** Strictly **30.0 mV**.\n"
                f"• **Post-Spike Reset Potential (c):** **{active_params.get('c')} mV** (Table S4 parameter).\n"
                f"• **Recovery Variable Increment (d):** **{active_params.get('d')} pA**."
            )
        else:
            st.info(
                f"**AdEx Model Equations:**\n\n"
                r"$$C\frac{dV}{dt} = -g_L(V - E_L) + g_L\Delta_T\exp\left(\frac{V - V_T}{\Delta_T}\right) - w + I(t)$$" + "\n\n"
                r"$$\tau_w\frac{dw}{dt} = a(V - E_L) - w$$" + "\n\n"
                f"**Reset Condition:**\n"
                r"$$\text{If } V \ge V_{\text{cut}} \implies V \leftarrow V_r,\quad w \leftarrow w + b$$" + "\n\n"
                f"• **Spike Cutoff (Vcut):** **{active_params.get('Vcut')} mV**\n"
                f"• **Reset Potential (Vr):** **{active_params.get('Vr')} mV**"
            )

    st.divider()

    # -------------------------------------------------------------------------
    # 4 & 5. Simulation Execution & Plots
    # -------------------------------------------------------------------------
    if generate_btn or "sim_executed" in st.session_state:
        st.session_state["sim_executed"] = True

        try:
            sim_params = active_params.copy()

            if selected_model == "AdEx":
                sim_data = simulate_adex(
                    params=sim_params,
                    duration_ms=duration_ms,
                    dt=dt_ms,
                    V_peak=V_peak,
                    V_reset=V_reset
                )
            else:
                sim_data = simulate_izhikevich(
                    params=sim_params,
                    duration_ms=duration_ms,
                    dt=dt_ms,
                    V_peak=30.0,
                    V_reset=sim_params.get("c")
                )

            time = sim_data["time"]
            V = sim_data["V"]
            w_or_u = sim_data["w"]
            spike_times = sim_data["spike_times"]

            # Analysis metrics
            metrics = analyze_firing_pattern(spike_times, duration_ms)

            st.subheader("Simulation & Firing Pattern Analysis")
            m1, m2, m3, m4, m5 = st.columns(5)
            m1.metric("Detected Spikes", metrics["num_spikes"])
            m2.metric("Mean Frequency", f"{metrics['mean_frequency_hz']} Hz")
            m3.metric("Mean ISI", f"{metrics['mean_isi_ms'] if metrics['mean_isi_ms'] else 'N/A'} ms")
            m4.metric("ISI CV", metrics["cv_isi"] if metrics["cv_isi"] is not None else "N/A")
            m5.metric("Firing Mode", metrics["firing_mode"])

            st.divider()

            # Plot membrane potential and recovery/adaptation variable
            st.subheader(f"Membrane Potential & State Variable Traces — {selected_model}")
            fig_trace = plot_membrane_trace(time, V, w_or_u, active_params, selected_model)
            st.pyplot(fig_trace)

            # -----------------------------------------------------------------
            # 6. CSV Download Button
            # -----------------------------------------------------------------
            var_name = "AdaptationCurrent_w_pA" if selected_model == "AdEx" else "RecoveryVariable_u_pA"
            df_export = pd.DataFrame({
                "Time_ms": np.round(time, 3),
                "MembranePotential_V_mV": np.round(V, 3),
                var_name: np.round(w_or_u, 3)
            })
            csv_bytes = df_export.to_csv(index=False).encode("utf-8")
            st.download_button(
                label=f"Download {selected_model} Simulation Data (CSV)",
                data=csv_bytes,
                file_name=f"{selected_population.split()[0]}_{selected_model}_simulation.csv",
                mime="text/csv",
                use_container_width=True
            )

        except Exception as e:
            st.error(f"Simulation Error: {str(e)}")
            st.exception(e)
    else:
        st.info("Configure simulation parameters in the sidebar and click **Generate Firing Pattern** to visualize membrane dynamics.")

    st.divider()

    # -------------------------------------------------------------------------
    # 7, 8, 9. Experimental Reference: Electrophysiology and F–I Curve
    # (Directly below CSV download button on Main Simulation Page)
    # -------------------------------------------------------------------------
    st.subheader("Experimental Reference: Published Electrophysiology")
    st.caption("Empirical electrophysiology figures, experimental response traces, and peer-reviewed citations for the currently selected neuronal population.")

    exp_ref = get_experimental_reference(selected_population, selected_model)

    if not exp_ref:
        st.info(f"No dedicated empirical reference figures are currently indexed for {selected_population}.")
    elif "panels" in exp_ref:
        # Multi-panel reference (e.g., Cerebellar Golgi Cell with Solinas 2007 + Forti 2006)
        cols = st.columns(len(exp_ref["panels"]))
        for i, panel in enumerate(exp_ref["panels"]):
            with cols[i]:
                st.markdown(f"#### {panel.get('heading', f'Citation {i+1}')}")
                img_name = panel.get("image")
                img_path = os.path.join(FIGURES_DIR, img_name) if img_name else None
                if img_path and os.path.exists(img_path):
                    img = Image.open(img_path)
                    st.image(img, caption=panel.get("fig_label", "Published Panel"), use_container_width=True)
                else:
                    st.info(f"Published panel: {panel.get('fig_label', '')}")

                st.markdown(f"""
                <div class="figure-caption-tag" style="margin-bottom: 0.8rem;">
                    <b>Description:</b> {panel.get('description', '')}
                </div>
                """, unsafe_allow_html=True)

                st.markdown(f"""
                <div class="citation-box">
                    <h5 style="margin-top:0; color: #58A6FF; margin-bottom: 0.3rem;">{panel.get('paper_title', '')}</h5>
                    <p style="margin-bottom:0.3rem; color: #C9D1D9; font-size: 0.9rem;"><b>Authors:</b> {panel.get('authors', '')} ({panel.get('year', '')})</p>
                    <p style="margin-bottom:0.3rem; color: #C9D1D9; font-size: 0.85rem;"><b>Journal:</b> <i>{panel.get('journal', '')}</i></p>
                    <p style="margin-bottom:0.6rem; color: #C9D1D9; font-size: 0.85rem;"><b>DOI:</b> <a href="{panel.get('full_url', '#')}" target="_blank" style="color: #58A6FF;">{panel.get('doi', '')}</a></p>
                    <a href="{panel.get('full_url', '#')}" target="_blank" style="text-decoration: none;">
                        <button style="background-color: #238636; color: white; border: none; padding: 0.45rem 1rem; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 0.85rem;">
                            🔗 Open Original Paper
                        </button>
                    </a>
                </div>
                """, unsafe_allow_html=True)
    else:
        # Single-panel reference (e.g. Granule Cell D'Angelo 1998, MLI Jörntell 2003, AdEx papers)
        col_fig, col_info = st.columns([1.15, 0.85])
        with col_fig:
            st.markdown(f"#### {exp_ref.get('ephys_fig_label', 'Experimental Electrophysiology')}")
            img_name = exp_ref.get("ephys_image")
            img_path = os.path.join(FIGURES_DIR, img_name) if img_name else None
            if img_path and os.path.exists(img_path):
                img_ephys = Image.open(img_path)
                st.image(img_ephys, caption=exp_ref.get("ephys_fig_label", "Published Electrophysiology"), use_container_width=True)
            else:
                st.info(f"Published panel: {exp_ref.get('ephys_fig_label', '')}")

        with col_info:
            st.markdown("#### Figure Description & Citation")
            rec_cond = exp_ref.get("recording_conditions")
            rec_str = f"<br><br><b>Recording Conditions:</b> {rec_cond}" if rec_cond else ""
            species = exp_ref.get("species")
            species_str = f"<br><b>Species:</b> {species}" if species else ""

            st.markdown(f"""
            <div class="figure-caption-tag" style="margin-bottom: 0.8rem;">
                <b>Description:</b> {exp_ref.get('ephys_desc', '')}{rec_str}{species_str}
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div class="citation-box">
                <h5 style="margin-top:0; color: #58A6FF; margin-bottom: 0.3rem;">{exp_ref.get('paper_title', '')}</h5>
                <p style="margin-bottom:0.3rem; color: #C9D1D9; font-size: 0.9rem;"><b>Authors:</b> {exp_ref.get('authors', '')} ({exp_ref.get('year', '')})</p>
                <p style="margin-bottom:0.3rem; color: #C9D1D9; font-size: 0.85rem;"><b>Journal:</b> <i>{exp_ref.get('journal', '')}</i></p>
                <p style="margin-bottom:0.6rem; color: #C9D1D9; font-size: 0.85rem;"><b>DOI:</b> <a href="{exp_ref.get('full_url', '#')}" target="_blank" style="color: #58A6FF;">{exp_ref.get('doi', '')}</a></p>
                <a href="{exp_ref.get('full_url', '#')}" target="_blank" style="text-decoration: none;">
                    <button style="background-color: #238636; color: white; border: none; padding: 0.45rem 1rem; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 0.85rem;">
                        🔗 Open Original Paper
                    </button>
                </a>
            </div>
            """, unsafe_allow_html=True)


# =============================================================================
# VIEW 2: CLEANED F–I PLOT NAVIGATION HIERARCHY
# =============================================================================
elif st.session_state["nav_mode"] == "F–I Plot":
    st.header("Experimental Electrophysiology Literature Navigation")
    st.markdown("""
    Explore curated peer-reviewed publications and verified experimental electrophysiological figures.
    """)

    # Hierarchy Breadcrumb
    st.markdown("""
    <div style="background-color: #161B22; padding: 0.65rem 1rem; border-radius: 6px; border: 1px solid #30363D; margin-bottom: 1.5rem;">
        <span class="badge badge-blue">Hierarchy</span>
        <b>F–I Plot</b> &rarr;
        <span style="color:#58A6FF;">Step 1: Select Neuron Type</span> &rarr;
        <span style="color:#3FB950;">Step 2: Select Experimental Paper</span> &rarr;
        <span style="color:#BC8CFF;">View Electrophysiology & Figures</span> &rarr;
        <span style="color:#D29922;">Citation & Source</span>
    </div>
    """, unsafe_allow_html=True)

    # -------------------------------------------------------------------------
    # STEP 1: Select Neuron Type
    # -------------------------------------------------------------------------
    st.subheader("Step 1: Select Neuron Type")
    fi_types = list_fi_plot_neuron_types()

    col_t1, col_t2 = st.columns([1.2, 0.8])
    with col_t1:
        selected_fi_type = st.selectbox(
            "Curated Neuronal Population:",
            options=fi_types,
            index=1,
            help="Select cell type to inspect literature records."
        )

    fi_rec = get_fi_plot_neuron_record(selected_fi_type)

    with col_t2:
        st.markdown(f"**Brain Region:** `{fi_rec.get('region', 'N/A')}`")

    st.divider()

    # -------------------------------------------------------------------------
    # STEP 2: Select Experimental Paper
    # -------------------------------------------------------------------------
    st.subheader("Step 2: Select Experimental Paper")
    papers = fi_rec.get("papers", [])

    if not papers:
        st.warning("No papers currently indexed for this neuron type.")
    else:
        paper_titles = [f"{p['authors'].split(',')[0]} et al. ({p['year']}) — {p['title']}" for p in papers]
        selected_paper_idx = 0
        if len(papers) > 1:
            selected_paper_idx = st.selectbox(
                "Associated Publication:",
                options=range(len(papers)),
                format_func=lambda i: paper_titles[i]
            )

        paper = papers[selected_paper_idx]

        # Publication Summary Card
        st.markdown(f"""
        <div class="citation-box" style="margin-top: 0.5rem; margin-bottom: 1rem;">
            <h4 style="margin-top:0; color: #58A6FF;">{paper['title']}</h4>
            <p style="margin-bottom: 0.4rem; color: #C9D1D9;"><b>Authors:</b> {paper['authors']} ({paper['year']})</p>
            <p style="margin-bottom: 0.4rem; color: #C9D1D9;"><b>Journal:</b> <i>{paper['journal']}</i> &nbsp;|&nbsp; <b>DOI:</b> <a href="{paper['full_url']}" target="_blank" style="color: #58A6FF;">{paper['doi']}</a></p>
            <p style="margin-bottom: 0; color: #C9D1D9;"><b>Species:</b> {paper.get('species', 'N/A')} &nbsp;|&nbsp; <b>Method:</b> {paper.get('method', 'N/A')}</p>
        </div>
        """, unsafe_allow_html=True)

        st.divider()

        # -------------------------------------------------------------------------
        # Display Experimental Figures (Step 3 removed per instructions)
        # Genuine captions used; no internal filenames like rId5.png!
        # -------------------------------------------------------------------------
        st.subheader("Experimental Electrophysiology Figures")

        img_name = paper.get("ephys_image")
        img_path = os.path.join(FIGURES_DIR, img_name) if img_name else None

        if img_path and os.path.exists(img_path):
            img = Image.open(img_path)
            # Genuine source figure identification without internal filenames
            caption_text = paper.get("ephys_fig_label", "Experimental Figure Panel")
            st.image(img, caption=caption_text, use_container_width=True)
        else:
            st.info(f"Figure reference: {paper.get('ephys_fig_label', 'Published figure panel')}")

        st.divider()

        # -------------------------------------------------------------------------
        # Citation & Source Panel (No separate PubMed Central button per instructions)
        # -------------------------------------------------------------------------
        st.subheader("Citation & Source")
        st.markdown(f"""
        **Full Citation (APA 7th Edition):**
        > {paper['authors']} ({paper['year']}). {paper['title']}. *{paper['journal']}*. https://doi.org/{paper['doi']}

        - **DOI:** `{paper['doi']}`
        - **Figure Panel:** `{paper.get('ephys_fig_label', '')}`
        """)

        st.link_button(
            "🔗 Open Original Paper",
            paper["full_url"],
            use_container_width=False,
            type="primary"
        )
