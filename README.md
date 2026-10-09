# DE-101 Pipeline - Production ETL Pipeline

> From 0 to Production in 10 Days | Built by jazzy (https://github.com/sirjazzyy)

A production-ready ETL pipeline built with Python & Pandas. Scaled from material site data to 3 real-world datasets (students 184B, real_tips 7.8K, ecommerce 65K) with production logging and data quality gates.

---

### 🚀 Live Production Run - Day 10

2026-10-09 14:49:02 | INFO | ===== ETL JOB STARTED =====
2026-10-09 14:49:02 | INFO | Input file: students.csv
2026-10-09 14:49:02 | INFO | [1/4] Extracting... 2 rows extracted
2026-10-09 14:49:02 | INFO | [2/4] Validating data...
2026-10-09 14:49:02 | INFO | [VALIDATION] Row count check passed
2026-10-09 14:49:02 | INFO | [VALIDATION] No duplicates found
2026-10-09 14:49:02 | INFO | [VALIDATION] Critical columns check passed
2026-10-09 14:49:02 | INFO | [VALIDATION] All checks passed!
2026-10-09 14:49:02 | INFO | [3/4] Cleaning data... Found 0 nulls
2026-10-09 14:49:02 | INFO | [4/4] Loading to data/processed/cleaned_data.csv
2026-10-09 14:49:02 | INFO | ===== ETL JOB COMPLETED SUCCESSFULLY =====

### 📁 Project Structure
de-101-pipeline/
├── scripts/
│   ├── run_pipeline.py   # Main orchestrator (Extract -> Validate -> Clean -> Load)
│   ├── logger.py         # Day 9 - Production logger (file + console)
│   ├── validate.py       # Day 10 - 4 data quality checks
│   └── pipeline.py       # Day 3 - legacy
├── data/
│   ├── raw/              # Raw inputs
│   └── processed/
│       └── cleaned_data.csv
├── logs/
│   └── etl_20261009.log
├── students.csv          # Dataset 1 - students
├── real_tips.csv         # Dataset 2 - 7.8K tips (main)
├── tips.csv              # Dataset 2 - alias for testing
├── ecommerce.csv         # Dataset 3 - 65K ecommerce
├── quantity_per_site.png # Day 2 viz
├── deliveries.png        # Day 2 viz
├── .gitignore
└── README.md

### 📅 10-Day Build Journey

| Day | Milestone |
|-----|-----------|
| Day 1 | First ETL - cleaned NaN to 0, summary by site |
| Day 2 | Visualizations - quantity_per_site.png + deliveries chart |
| Day 3 | Complete ETL pipeline end-to-end |
| Day 4 | Pro pipeline with logging + real materials data |
| Day 5-6 | Tested with real data: real_tips.csv (7.8K) + ecommerce.csv (65K) |
| Day 7 | Scaled to 3 datasets: students.csv, real_tips.csv, ecommerce.csv |
| Day 8 | Fixed argparse, parameterized --input, organized data/raw & data/processed |
| Day 9 | Production logging - logger.py with FileHandler + StreamHandler |
| Day 10 | Data validation - validate.py with 4 gates |

### ▶️ How To Run

Parameters:
- --input: Input CSV filename (required) - supports any dataset
pip install pandas matplotlib
python3 scripts/run_pipeline.py --input students.csv
python3 scripts/run_pipeline.py --input real_tips.csv
python3 scripts/run_pipeline.py --input ecommerce.csv
cat logs/etl_*.log
ls -lh data/processed/

ETL Steps Inside run_pipeline.py:
1. [1/4] Extract - pd.read_csv(args.input)
2. [2/4] Validate - validate.py -> 4 checks
3. [3/4] Clean - handle nulls, duplicates
4. [4/4] Load - to data/processed/cleaned_data.csv

### 🛠 Tech Stack

| Layer | Tools |
|-------|-------|
| Language | Python 3.10+ |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib |
| Production | Logging (File + Console), Argparse (--input), OS, Datetime |
| Data Quality | validate.py - Row Count, Duplicates, Critical Columns, Nulls |
| Datasets | students.csv, real_tips.csv / tips.csv, ecommerce.csv |
| Architecture | Modular Scripts, Parameterized CLI, Raw -> Processed |

Stack: Python | Pandas | Matplotlib | Logging | Argparse | Data Validation | Git

---
Status: DE-101 COMPLETED ✅ 10/10 Days

Author: sirjazzyy — Data Engineer in progress