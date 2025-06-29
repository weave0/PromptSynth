import sys
import keyboard  # Requires `pip install keyboard`
from components.audio_player import AudioPlayer

sys.path.append(".")

SAMPLE_MAP = {
    '1': 'valid_test.wav',
    '2': 'valid_test.wav',
    '3': 'valid_test.wav',
    '4': 'valid_test.wav',
    '5': 'valid_test.wav',
}

player = AudioPlayer()

print("Press keys 1–5 to play samples. Press ESC to quit.")

try:
    while True:
        for key in SAMPLE_MAP:
            if keyboard.is_pressed(key):
                print(f"Playing: {SAMPLE_MAP[key]}")
                player.play_sample(SAMPLE_MAP[key])
                while keyboard.is_pressed(key):
                    pass  # Wait for key release

        if keyboard.is_pressed('esc'):
            print("Exiting...")
            break

except KeyboardInterrupt:
    print("Exited via Ctrl+C")
