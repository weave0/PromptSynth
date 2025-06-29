# components/sample_loader.py

import os

# Automatically resolve to: /assets/samples relative to this file
SAMPLE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "assets", "samples"))

def list_sample_categories():
    """Return a list of top-level sample categories (folder names)"""
    if not os.path.exists(SAMPLE_ROOT):
        return []
    return sorted([d for d in os.listdir(SAMPLE_ROOT) if os.path.isdir(os.path.join(SAMPLE_ROOT, d))])

def list_samples_in_category(category):
    """List all .wav files in a given sample subfolder (e.g., 'Kick', 'Snare')"""
    category_path = os.path.join(SAMPLE_ROOT, category)
    if not os.path.exists(category_path):
        return []
    return sorted([
        f for f in os.listdir(category_path)
        if f.lower().endswith(".wav")
    ])

def get_sample_path(category, filename):
    """Return full absolute path to a selected sample file"""
    path = os.path.join(SAMPLE_ROOT, category, filename)
    return path if os.path.exists(path) else None

def list_all_samples():
    """Return a dict of all samples by category, with full paths"""
    sample_dict = {}
    for root, dirs, files in os.walk(SAMPLE_ROOT):
        for file in files:
            if file.lower().endswith(".wav"):
                category = os.path.basename(root)
                path = os.path.join(root, file)
                sample_dict.setdefault(category, []).append(path)
    return sample_dict
