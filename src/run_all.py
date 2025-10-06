# -------------------------------------------------------
# File: run_all.py
# Description: Run the entire reproducible pipeline
# -------------------------------------------------------

import subprocess
import os

os.makedirs("outputs/tables", exist_ok=True)
os.makedirs("outputs/figures", exist_ok=True)

print(" Step 1: Downloading data with R...")
subprocess.run(["Rscript", "src/download_data.R"], check=True)

print(" Step 2: Cleaning data with Python...")
subprocess.run(["python", "src/clean_data.py"], check=True)

print(" Step 3: Computing volatility and visualizing results...")
subprocess.run(["python", "src/compute_and_visualize.py"], check=True)

