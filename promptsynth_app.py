# promptsynth_app.py

import streamlit as st
from components.sequencer_grid import render_sequencer_grid
from components.mixer import render_mixer
from utils.file_manager import export_project

st.set_page_config(layout="wide")
st.title("🎛 PromptSynth Studio")

tabs = st.tabs(["Sequencer", "Mixer", "Export"])

with tabs[0]:
    st.header("🧱 Sequencer Grid")
    render_sequencer_grid()

with tabs[1]:
    st.header("🎚 Mixer")
    render_mixer()

with tabs[2]:
    st.header("📦 Export")
    export_project()
