@echo off
echo Launching PromptSynth...
cd /d %~dp0
streamlit run main.py
pause
