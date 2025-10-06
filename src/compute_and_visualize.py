# ---------------------------------------------------------
# File: compute_and_visualize.py
# Author: Shirin Dehghannezhad
# Description:
#   Compute stock returns, volatility, and visualizations
#   using cleaned data from data/processed/.
# Outputs:
#     - volatility_summary.csv (table)
#     - line, return, and heat map charts in outputs/figures/
# ---------------------------------------------------------

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Make sure output folders exist
os.makedirs("outputs/tables", exist_ok=True)
os.makedirs("outputs/figures", exist_ok=True)

# List of tickers
tickers = ["AAPL", "MSFT", "GOOGL"]

# Read cleaned data

data = {}
for ticker in tickers:
    path = f"data/processed/{ticker}_clean.csv"
    df = pd.read_csv(path, parse_dates=["date"])
    df["return"] = np.log(df["adjusted_close"] / df["adjusted_close"].shift(1))
    df.dropna(subset=["return"], inplace=True)
    data[ticker] = df

# -----------------------------
# 1. Summary table of volatility
# -----------------------------

summary = []
for ticker, df in data.items():
    daily_sd = df["return"].std()
    annual_vol = daily_sd * np.sqrt(252)
    summary.append({
        "Ticker": ticker,
        "Start_Date": df["date"].min().date(),
        "End_Date": df["date"].max().date(),
        "Obs": len(df),
        "Daily_SD": round(daily_sd, 5),
        "Annualized_Volatility": round(annual_vol, 5)
    })

summary_df = pd.DataFrame(summary)
summary_df.to_csv("outputs/tables/volatility_summary.csv", index=False)
print(" Saved summary table to outputs/tables/volatility_summary.csv")

# -----------------------------
# 2. Price line chart
# -----------------------------

plt.figure(figsize=(10, 5))
for ticker, df in data.items():
    plt.plot(df["date"], df["adjusted_close"], label=ticker)
plt.title("Stock Prices (Adjusted Close)")
plt.xlabel("Date")
plt.ylabel("Price ($)")
plt.legend()
plt.tight_layout()
plt.savefig("outputs/figures/price_lines.png", dpi=300)
plt.close()
print("Saved price line chart")

# -----------------------------
# 3. Daily return line chart
# -----------------------------
plt.figure(figsize=(10, 5))
for ticker, df in data.items():
    plt.plot(df["date"], df["return"], label=ticker, alpha=0.8)
plt.title("Daily Log Returns")
plt.xlabel("Date")
plt.ylabel("Return")
plt.legend()
plt.tight_layout()
plt.savefig("outputs/figures/return_lines.png", dpi=300)
plt.close()
print("Saved daily return line chart")

# -----------------------------
# 4. Correlation heat map
# -----------------------------
# Build a single DataFrame of returns

returns_df = pd.DataFrame({t: data[t]["return"].values for t in tickers})
corr = returns_df.corr()

plt.figure(figsize=(6, 5))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation of Daily Returns")
plt.tight_layout()
plt.savefig("outputs/figures/returns_correlation_heatmap.png", dpi=300)
plt.close()
print(" Saved correlation heat map")

# -----------------------------
# 5. Volatility bar chart
# -----------------------------
plt.figure(figsize=(6, 4))
sns.barplot(data=summary_df, x="Ticker", y="Annualized_Volatility", palette="viridis")
plt.title("Annualized Volatility (2022–present)")
plt.ylabel("Volatility")
plt.xlabel("")
plt.tight_layout()
plt.savefig("outputs/figures/volatility_bar.png", dpi=300)
plt.close()
print(" Saved volatility bar chart")
# -----------------------------

print("\n All analysis completed. Check outputs/tables and outputs/figures folders.")
