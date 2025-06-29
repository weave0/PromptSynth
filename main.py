# main.py – Launches PromptSynth App UI

import streamlit as st
from components.sequencer_grid import render_sequencer
from components.piano_view import render_piano_view
from components.mixer import render_mixer

# Set full layout
st.set_page_config(page_title="PromptSynth", layout="wide")

# Tabs across top
tabs = st.tabs(["🎛 Sequencer", "🎹 Piano", "🎚 Mixer"])

# Grid tab
with tabs[0]:
    st.title("🧱 Modular Sequencer Grid")
    render_sequencer()

# Piano tab
with tabs[1]:
    st.title("🎹 QWERTY Piano View")
    render_piano_view()

# Mixer tab
with tabs[2]:
    st.title("🎚 Track Mixer")
    render_mixer()
