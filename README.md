# DE-101: Materials Data Pipeline 🏗️

A production-style ETL pipeline for processing construction materials data (Cement, Reinforcement Bars, Sand) - built with Python, Pandas & Logging.

> Day 1-8 Project by Jazzy | Aspiring Data Engineer

### 📊 Architecture
Raw CSV -> Extract & Clean -> Cleaned CSV -> Visualize -> Logs

### 📁 Folder Structure
de-101-pipeline/
├── data/
│   ├── raw/materials.csv
│   └── processed/cleaned.csv
├── logs/
│   └── pipeline.log
├── extract_clean.py
├── visualize_materials.py
├── pipeline.py
└── README.md

### 🛠️ Tech Stack
- Python 3
- Pandas for ETL
- Matplotlib for charts
- Logging for monitoring
- Git & GitHub

### 🚀 How to Run
git clone https://github.com/sirjazzyy/de-101-pipeline.git
cd de-101-pipeline
pip install pandas matplotlib
python3 pipeline.py

### 📝 Sample Log
2026-10-06 - INFO - Starting extract_clean.py...
2026-10-06 - INFO - Completed successfully!
2026-10-06 - INFO - PIPELINE COMPLETE in 0:00:05

### 📈 What it Does
- Cleans missing values (NaN -> 0)
- Processes real factory materials
- Generates delivery charts
- Full audit trail via logs

### 🗓️ Roadmap
- Day 1: Basic ETL
- Day 2: Visualizations
- Day 3: Pipeline Automation
- Day 4: Pro Logging + Real Data
- Day 5: Professional README
- Day 6-7: Multi-Dataset + Logging
- Day 8: Parameterized ETL (TODAY)

### Day 6-7 - Multi-Dataset
- Added 3 real datasets: students, real_tips, ecommerce
- Added full audit trail via logs/pipeline.log

### Day 8 - Parameterized ETL (Current)
- Fixed critical bug: hardcoded `clean_ecommerce.csv` → now uses args
- Added argparse for --input / --output (pipeline reusable for any CSV)
- Outputs: clean_students.csv (3 rows), clean_real_tips.csv (244 rows), clean_ecommerce.csv (500 rows)

#### How to Run Day 8
```bash
python scripts/run_pipeline.py --input data/raw/students.csv --output data/processed/clean_students.csv
python scripts/run_pipeline.py --input data/raw/real_tips.csv --output data/processed/clean_real_tips.csv
python scripts/run_pipeline.py --input data/raw/ecommerce.csv --output data/processed/clean_ecommerce.csv
```

'Author: sirjazzyy | Data Engineer in progress'
