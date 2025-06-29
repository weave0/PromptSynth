# components/piano_view.py

import streamlit as st

def render_piano_view():
    st.subheader("QWERTY Piano Mode 🎹")

    st.markdown("""
        This view will allow you to play musical notes using your computer keyboard (QWERTY layout).
        Future features:
        - Scale selection
        - Instrument selection
        - Real-time note playback
        - Loop recording
    """)

    st.info("🔧 This feature is under construction. Please check back soon!")
