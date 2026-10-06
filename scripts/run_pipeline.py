import pandas as pd
import os
from datetime import datetime

def extract():
    print("[1/3] Extracting...")
    df = pd.read_csv("data/raw/students.csv")
    return df

def clean(df):
    print("[2/3] Cleaning...")
    df = df.dropna()
    df.columns = [c.strip().lower() for c in df.columns]
    return df

def load(df):
    print("[3/3] Loading...")
    os.makedirs("data/processed", exist_ok=True)
    os.makedirs("logs", exist_ok=True)
    
    df.to_csv("data/processed/clean_students.csv", index=False)
    
    with open("logs/pipeline.log", "a") as f:
        f.write(f"{datetime.now()} - Pipeline ran: {len(df)} rows cleaned\n")
    
    print(f"Done! {len(df)} rows saved to data/processed/clean_students.csv")

if __name__ == "__main__":
    raw = extract()
    cleaned = clean(raw)
    load(cleaned)