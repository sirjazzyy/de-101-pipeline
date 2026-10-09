import pandas as pd
import argparse
import sys
import os

# Make sure we can import from scripts folder
sys.path.append(os.path.dirname(__file__))

from logger import get_logger
from validate import validate_data

logger = get_logger("etl_pipeline")

def main():
    parser = argparse.ArgumentParser(description="DE-101 ETL Pipeline")
    parser.add_argument('--input', required=True, help='Input CSV file')
    args = parser.parse_args()

    try:
        logger.info("===== ETL JOB STARTED =====")
        logger.info(f"Input file: {args.input}")

        # [1/4] EXTRACT
        logger.info(f"[1/4] Extracting {args.input}...")
        df = pd.read_csv(args.input)
        logger.info(f"Extracted {len(df)} rows")

        # [2/4] VALIDATE (Day 10 - NEW)
        logger.info(f"[2/4] Validating data...")
        df = validate_data(df)

        # [3/4] CLEAN
        logger.info(f"[3/4] Cleaning...")
        nulls = df.isnull().sum().sum()
        logger.info(f"Found {nulls} null values")
        # Your existing cleaning logic here
        # df = df.dropna() etc.

        # [4/4] LOAD
        logger.info(f"[4/4] Loading...")
        # Your existing load logic here
        # For now, just save to processed
        os.makedirs("data/processed", exist_ok=True)
        df.to_csv("data/processed/cleaned_data.csv", index=False)
        
        logger.info("===== ETL JOB COMPLETED SUCCESSFULLY =====")

    except Exception as e:
        logger.error(f"===== ETL JOB FAILED: {e} =====")
        raise

if __name__ == "__main__":
    main()