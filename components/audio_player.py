import os
import simpleaudio as sa

class AudioPlayer:
    def __init__(self):
        self.play_objects = []

    def play_sample(self, filepath):
        if not os.path.exists(filepath):
            print(f"[AudioPlayer] File not found: {filepath}")
            return

        try:
            wave_obj = sa.WaveObject.from_wave_file(filepath)
            play_obj = wave_obj.play()
            self.play_objects.append(play_obj)
        except Exception as e:
            print(f"[AudioPlayer] Error playing {filepath}: {e}")

    def stop_all(self):
        for play_obj in self.play_objects:
            play_obj.stop()
        self.play_objects = []
