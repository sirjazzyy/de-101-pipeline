import subprocess

print("Step 1: Cleaning data...")
subprocess.run(["python", "scripts/extract_clean.py"])

print("Step 2: Visualizing...")
subprocess.run(["python", "scripts/visualize_materials.py"])

print("✅ Pipeline Complete!")