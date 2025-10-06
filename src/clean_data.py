# -------------------------------
# File: clean_data.py
# Author: Shirin Dehghannezhad
# Description:
#   This script cleans the raw Yahoo Finance stock data
#   downloaded with R (AAPL, MSFT, GOOGL).
#   Steps:
#     1. Read raw CSVs from data/raw/
#     2. Keep only 'date' and 'Adjusted Close' columns
#     3. Drop missing and duplicate rows
#     4. Sort by date and save to data/processed/
# -------------------------------

import os
import pandas as pd

# Make sure the output folder exists
os.makedirs("data/processed", exist_ok=True)

# List of stock tickers
tickers = ["AAPL", "MSFT", "GOOGL"]

# Loop through each ticker
for ticker in tickers:
    raw_path = f"data/raw/{ticker}.csv"
    clean_path = f"data/processed/{ticker}_clean.csv"

    # Check if the file exists
    if not os.path.exists(raw_path):
        print(f" File not found: {raw_path}")
        continue

    # Read the raw CSV file
    df = pd.read_csv(raw_path)

    # Find the Adjusted Close column automatically
    adj_col = [col for col in df.columns if "Adj" in col or "Adjusted" in col][0]

    # Keep only the relevant columns
    df = df[["date", adj_col]].rename(columns={adj_col: "adjusted_close"})

    # Clean the data
    df = (
        df.drop_duplicates(subset="date")  # remove duplicates
          .dropna()                        # remove missing values
          .sort_values("date")             # sort by date ascending
    )

    # Save the cleaned data
    df.to_csv(clean_path, index=False)

    print(f" Cleaned data saved to {clean_path}")

print("\n All cleaned files are saved in 'data/processed/' folder.")
