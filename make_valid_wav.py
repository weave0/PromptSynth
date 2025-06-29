import wave
import struct
import math

filename = "valid_test.wav"
sample_rate = 44100
duration = 1.0  # seconds
frequency = 440.0  # Hz

n_frames = int(sample_rate * duration)
amplitude = 32767  # Max for 16-bit audio

with wave.open(filename, 'w') as wav_file:
    wav_file.setnchannels(1)       # mono
    wav_file.setsampwidth(2)       # 2 bytes (16-bit)
    wav_file.setframerate(sample_rate)

    for i in range(n_frames):
        sample = amplitude * math.sin(2 * math.pi * frequency * i / sample_rate)
        sample = max(min(int(sample), 32767), -32768)  # Clamp value
        wav_file.writeframes(struct.pack('<h', sample))
