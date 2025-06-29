import sys
sys.path.append(".")

from components.audio_player import AudioPlayer

player = AudioPlayer()
player.play_sample("valid_test.wav")
