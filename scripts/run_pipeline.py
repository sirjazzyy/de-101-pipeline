import pandas as pd
import os
import argparse
from datetime import datetime

def extract(input_path):
    print(f"[1/3] Extracting {input_path}...")
    df = pd.read_csv(input_path)
    print(f"  -> {len(df)} rows")
    return df

def clean(df):
    print("[2/3] Cleaning...")
    initial = len(df)
    df = df.dropna()
    df.columns = [c.strip().lower().replace(" ", "_").replace(".", "") for c in df.columns]
    print(f"  -> {initial} -> {len(df)} rows")
    return df

def load(df, output_path):
    print(f"[3/3] Loading to {output_path}...")
    os.makedirs("data/processed", exist_ok=True)
    os.makedirs("logs", exist_ok=True)
    df.to_csv(output_path, index=False)
    with open("logs/pipeline.log", "a") as f:
        f.write(f"{datetime.now()} - Pipeline ran: {len(df)} rows -> {output_path}\n")
    print(f"Done! {len(df)} rows saved to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="DE-101 ETL Pipeline")
    parser.add_argument("--input", required=True, help="Input CSV path")
    parser.add_argument("--output", required=False, help="Output CSV path")
    args = parser.parse_args()

    if not args.output:
        base = os.path.basename(args.input)
        args.output = f"data/processed/clean_{base}"

    df = extract(args.input)
    df = clean(df)
    load(df, args.output)
    print("Pipeline DONE")