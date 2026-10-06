import pandas as pd
import os

print('Pipeline started... Extracting & Cleaning...')

# Check if real raw data exists, else use dummy for demo
raw_path = 'data/raw/materials.csv'
if os.path.exists(raw_path):
    df = pd.read_csv(raw_path)
    print(f"Loaded real data from {raw_path}")
    # Clean: fill NaN with 0
    df = df.fillna(0)
else:
    print("No raw file found, using demo data")
    data = {'name': ['Jazzy', 'Tobi', 'Sola'], 'score': [90, 85, None]}
    df = pd.DataFrame(data)
    df['score'] = df['score'].fillna(0)

print('Raw:')
print(df)
print('Cleaned:')

# Ensure folder exists
os.makedirs('data/processed', exist_ok=True)
df.to_csv('data/processed/cleaned.csv', index=False)
print('Saved to data/processed/cleaned.csv - Done!')