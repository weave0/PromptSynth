import sys
import os
import keyboard
from components.audio_player import AudioPlayer

sys.path.append(".")

SAMPLE_DIR = "."
KEY_BINDINGS = ['1', '2', '3', '4', '5']
SAMPLE_MAP = {}
player = AudioPlayer()

def find_wav_files(directory):
    wavs = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(".wav") and is_valid_wav(os.path.join(root, file)):
                wavs.append(os.path.join(root, file))
    return wavs

def is_valid_wav(path):
    try:
        with open(path, 'rb') as f:
            return f.read(4) == b'RIFF'
    except:
        return False

def assign_samples():
    wav_files = find_wav_files(SAMPLE_DIR)
    if not wav_files:
        print("No valid WAV files found.")
        sys.exit(1)

    print("\nAssign samples to keys 1–5:")
    for i, key in enumerate(KEY_BINDINGS):
        chosen = None
        while not chosen:
            print(f"\nFiles:")
            for idx, file in enumerate(wav_files):
                print(f"  [{idx}] {file}")
            try:
                choice = input(f"Choose file index for key [{key}]: ")
                idx = int(choice)
                if 0 <= idx < len(wav_files):
                    SAMPLE_MAP[key] = wav_files[idx]
                    chosen = True
                else:
                    print("Invalid index.")
            except:
                print("Please enter a number.")

def run_sampler():
    print("\nPress 1–5 to play samples.")
    pr
