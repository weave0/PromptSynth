import os

def find_file(directory, filename):
    for root, dirs, files in os.walk(directory):
        if filename in files:
            return os.path.join(root, filename)
    return None

project_directory = "D:/PromptSynth"  # Update if needed
filename = "synth_trumpet.py"

file_path = find_file(project_directory, filename)

if file_path:
    print(f"✅ File found: {file_path}\n")
    with open(file_path, 'r') as file:
        synth_trumpet_code = file.read()
    print("📄 Contents of synth_trumpet.py:\n")
    print(synth_trumpet_code)
else:
    print("❌ synth_trumpet.py not found.")
