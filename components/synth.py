# components/synth.py

import numpy as np

SAMPLE_RATE = 44100

def generate_tone(freq, duration, volume=1.0):
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration))
    waveform = np.sin(2 * np.pi * freq * t)
    return waveform * volume

def apply_fx(waveform, volume=1.0, pan=0.5, fx=[]):
    waveform = waveform * volume
    if "distortion" in fx:
        waveform = np.tanh(waveform * 5)
    if "reverb" in fx:
        echo = np.pad(waveform, (4000, 0), mode='constant')[:-4000] * 0.4
        waveform = waveform + echo
    # Pan logic: left/right stereo
    left = waveform * (1 - pan)
    right = waveform * pan
    return np.vstack([left, right])

def generate_kick(params):
    t = np.linspace(0, params['duration'], int(SAMPLE_RATE * params['duration']))
    freq = np.linspace(params['pitch'] * 2, params['pitch'], t.shape[0])
    waveform = np.sin(2 * np.pi * freq * t)
    envelope = np.exp(-t * 10)
    return apply_fx(waveform * envelope, params['volume'], params['pan'], params['fx'])

def generate_snare(params):
    t = np.linspace(0, params['duration'], int(SAMPLE_RATE * params['duration']))
    noise = np.random.randn(len(t))
    envelope = np.exp(-t * 20)
    return apply_fx(noise * envelope, params['volume'], params['pan'], params['fx'])

def generate_sub_bass(params):
    t = np.linspace(0, params['duration'], int(SAMPLE_RATE * params['duration']))
    waveform = np.sin(2 * np.pi * params['pitch'] * t)
    return apply_fx(waveform, params['volume'], params['pan'], params['fx'])

def generate_pad(params):
    t = np.linspace(0, params['duration'], int(SAMPLE_RATE * params['duration']))
    waveform = np.sin(2 * np.pi * params['pitch'] * t)
    envelope = np.sin(np.pi * t / params['duration'])
    return apply_fx(waveform * envelope, params['volume'], params['pan'], params['fx'])

INSTRUMENT_GENERATORS = {
    "kick": generate_kick,
    "snare": generate_snare,
    "sub_bass": generate_sub_bass,
    "pad": generate_pad
}
