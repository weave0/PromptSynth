# components/mixer.py

import numpy as np

def apply_fx(waveform, params, global_fx=[], global_volume=1.0):
    if "distortion" in params.get("fx", []) + global_fx:
        waveform = np.tanh(waveform * 5)
    if "reverb" in params.get("fx", []) + global_fx:
        echo = np.pad(waveform, (5000, 0), mode='constant')[:-5000] * 0.3
        waveform = waveform + echo
    pan = params.get("pan", 0.5)
    volume = params.get("volume", 1.0) * global_volume
    left = waveform * (1 - pan) * volume
    right = waveform * pan * volume
    return np.vstack([left, right])

def render_mixer():
    import streamlit as st
    st.write("🔧 Mixer will go here soon!")
