import pandas as pd
import os
import argparse
import logging
from datetime import datetime
import sys

# Setup proper logger
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)-8s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler(f"logs/etl_{datetime.now().strftime('%Y%m%d')}.log"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

def extract(input_path):
    logger.info(f"[1/3] Extracting {input_path}...")
    try:
        df = pd.read_csv(input_path)
        logger.info(f"Extracted {len(df)} rows from {input_path}")
        return df
    except FileNotFoundError:
        logger.error(f"Input file not found: {input_path}")
        raise

def clean(df):
    logger.info("[2/3] Cleaning...")
    initial = len(df)
    nulls_before = df.isnull().sum().sum()
    logger.info(f"Found {nulls_before} null values")
    
    df = df.dropna()
    df.columns = [c.strip().lower().replace(" ", "_").replace(".", "") for c in df.columns]
    
    logger.info(f"Cleaned: {initial} -> {len(df)} rows (dropped {initial - len(df)})")
    return df

def load(df, output_path):
    logger.info(f"[3/3] Loading to {output_path}...")
    os.makedirs("data/processed", exist_ok=True)
    df.to_csv(output_path, index=False)
    logger.info(f"Successfully saved {len(df)} rows to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="DE-101 ETL Pipeline")
    parser.add_argument("--input", required=True, help="Input CSV path")
    parser.add_argument("--output", required=False, help="Output CSV path")
    args = parser.parse_args()

    if not args.output:
        base = os.path.basename(args.input)
        args.output = f"data/processed/clean_{base}"

    logger.info("===== ETL JOB STARTED =====")
    try:
        df = extract(args.input)
        df = clean(df)
        load(df, args.output)
        logger.info("===== ETL JOB COMPLETED SUCCESSFULLY =====")
    except Exception as e:
        logger.error(f"ETL JOB FAILED: {e}", exc_info=True)
        sys.exit(1)