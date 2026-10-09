import pandas as pd
from logger import get_logger

logger = get_logger("validator")

def validate_data(df: pd.DataFrame):
    logger.info("[VALIDATION] Starting data quality checks...")

    # Check 1: File is not empty
    if df.empty:
        logger.error("[VALIDATION FAILED] DataFrame is empty!")
        raise ValueError("Empty file - no data to process")
    logger.info(f"[VALIDATION] Row count check passed: {len(df)} rows")

    # Check 2: No duplicate rows
    dupes = df.duplicated().sum()
    if dupes > 0:
        logger.warning(f"[VALIDATION] Found {dupes} duplicate rows - removing them")
        df = df.drop_duplicates()
    else:
        logger.info("[VALIDATION] No duplicates found")

    # Check 3: Critical columns must not have nulls (adjust to your csv)
    # For students.csv, let's say 'name' is critical
    critical_cols = [col for col in ['name', 'student_name', 'id'] if col in df.columns]
    for col in critical_cols:
        nulls = df[col].isnull().sum()
        if nulls > 0:
            logger.error(f"[VALIDATION FAILED] Critical column '{col}' has {nulls} nulls")
            raise ValueError(f"Critical column {col} has nulls")
    logger.info("[VALIDATION] Critical columns check passed")

    # Check 4: Log overall nulls
    total_nulls = df.isnull().sum().sum()
    logger.info(f"[VALIDATION] Total null values in file: {total_nulls}")

    logger.info("[VALIDATION] All checks passed!")
    return df