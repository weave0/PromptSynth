import numpy as np
import sounddevice as sd

class SynthTrumpet:
    def __init__(self, sample_rate=44100):
        self.sample_rate = sample_rate

    def _generate_wave(self, freq, duration, vibrato_rate=5, vibrato_extent=0.5):
        t = np.linspace(0, duration, int(self.sample_rate * duration), endpoint=False)
        # Vibrato LFO modulating frequency
        vibrato = np.sin(2 * np.pi * vibrato_rate * t) * vibrato_extent

        # Harmonic-rich tone modulated by vibrato
        wave = (
            0.6 * np.sin(2 * np.pi * (freq + vibrato) * t) +
            0.3 * np.sin(2 * np.pi * 2 * (freq + vibrato) * t) +
            0.1 * np.sin(2 * np.pi * 3 * (freq + vibrato) * t)
        )

        envelope = np.exp(-3 * t)
        return wave * envelope

    def play_note(self, freq, duration=1.0, volume=0.8):
        waveform = self._generate_wave(freq, duration) * volume
        sd.play(waveform.astype(np.float32), self.sample_rate)
        sd.wait()

    def play_notes(self, freqs, duration=1.0, volume=0.8):
        voices = [self._generate_wave(f, duration) for f in freqs]
        mix = np.sum(voices, axis=0)
        mix *= volume / len(freqs)  # prevent clipping
        sd.play(mix.astype(np.float32), self.sample_rate)
        sd.wait()
