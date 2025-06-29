import sys
import os
import keyboard  # Requires: pip install keyboard
from components.audio_player import AudioPlayer

sys.path.append(".")

# Pad mappings to sample files
PAD_MAP = {
    'a': 'assets/samples/Organ/DS_BitOrgan140D-01.wav',
    's': 'assets/samples/Synth/DS_JenSyn140D-01.wav',
    'w': 'assets/samples/Bass/DS_BassA140D-01.wav',
    'e': 'assets/samples/FX/Delay_Feedback01.wav',
    'd': 'assets/samples/Guitar/Nylon Guitar a3.wav'
}

player = AudioPlayer()

print("\n🎹 Live Pad Performer Ready")
print("Press mapped keys to trigger samples. ESC = Exit.\n")
for k, v in PAD_MAP.items():
    print(f"🎵 {k.upper()} → {os.path.basename(v)}")

try:
    while True:
        for key, path in PAD_MAP.items():
            if keyboard.is_pressed(key):
                print(f"🔊 Playing: {os.path.basename(path)}")
                player.play_sample(path)
                while keyboard.is_pressed(key):
                    pass  # wait until key is released

        if keyboard.is_pressed('esc'):
            print("Exiting performer.")
            break

except KeyboardInterrupt:
    print("Exited via Ctrl+C")
