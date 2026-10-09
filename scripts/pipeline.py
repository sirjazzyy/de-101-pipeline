import subprocess
import logging
import os
from datetime import datetime
import sys

# Setup logging - file + console
os.makedirs("logs", exist_ok=True)
log_file = f"logs/pipeline_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)-8s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler(sys.stdout)
    ]
)

def run_step(script_name):
    try:
        logging.info(f"Starting {script_name}...")
        result = subprocess.run([sys.executable, f"scripts/{script_name}"], check=True)
        logging.info(f"Completed {script_name} successfully!")
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"FAILED at {script_name}: {e}")
        return False

if __name__ == "__main__":
    logging.info("===== PIPELINE STARTED =====")
    start = datetime.now()

    if not run_step("extract_clean.py"):
        logging.error("Pipeline stopped - cleaning failed")
        sys.exit(1)

    if not run_step("visualize_materials.py"):
        logging.error("Pipeline stopped - visualization failed")
        sys.exit(1)

    end = datetime.now()
    logging.info(f"===== PIPELINE COMPLETE in {end - start} | Logs saved to {log_file} =====")