#  Stock Volatility Comparison — Apple, Microsoft, and Google

**Author:** **Shirin Dehghannezhad**
**Date:** October 2025  
**Course:** Data Science 1

---

##  Project Goal

This project compares the **stock price volatility** of **Apple (AAPL)**, **Microsoft (MSFT)**, and **Alphabet (GOOGL)** using daily historical data from **Yahoo Finance**.

It demonstrates a reproducible data science workflow combining **R (for data collection)** and **Python (for cleaning, analysis, and visualization)**.

---

##  Reproducibility

The project follows reproducibility best practices:
- **All raw and processed data included**
- **Environment requirements saved**
- **Scripts organized by step**
- **Outputs automatically created**
- **Results reproducible with one command**

---

## Folder Structure

Stock_volatility_comparison
├── README.md
├── LICENSE
├── environment
│   └── requirements.txt
├── data
│   ├── raw
│   │   ├── AAPL.csv
│   │   ├── MSFT.csv
│   │   └── GOOGL.csv
│   └── processed
│       ├── AAPL_clean.csv
│       ├── MSFT_clean.csv
│       └── GOOGL_clean.csv
├── src
│   ├── download_data.R
│   ├── clean_data.py
│   ├── compute_and_visualize.py
│   └── run_all.py
└── outputs
    ├── tables
    │   └── volatility_summary.csv
    └── figures
        ├── price_lines.png
        ├── return_lines.png
        ├── returns_correlation_heatmap.png
        └── volatility_bar.png



---

##  Environment Setup

###  1. Clone the repository
```bash
git clone https://github.com/shirind76/stock-volatility-comparison.git
cd Stock_volatility_comparison
```
### 2. Set up Python environment
``` bash
python -m venv .venv
```
### 3. Activate environment:
##### macOS/Linux
``` bash 
source .venv/bin/activate 
```
###### Windows
```bash
.venv\Scripts\Activate
```
### 4. Install dependencies
```bash 
pip install -r environment/requirements.txt
```
---
## Analysis Workflow

###   1. Download Data (R)
- Uses the **`quantmod`** package to fetch daily stock prices for:
  - Apple (AAPL)
  - Microsoft (MSFT)
  - Alphabet (GOOGL)
- Saves the data as CSV files in the `data/raw/` folder.

###   2. Clean Data (Python)
- Reads each raw CSV from `data/raw/`
- Keeps only the relevant columns: `date` and `adjusted_close`
- Removes duplicate and missing rows
- Sorts the data by date
- Saves the cleaned datasets to `data/processed/`

###  3. Analyze and Visualize (Python)
- Computes **daily log returns**
- Calculates **annualized volatility** using  
  \[
  \sigma_{\text{annual}} = \text{sd}(r_t) \times \sqrt{252}
  \]
- Creates and saves the following visualizations:
  - **Line chart** of adjusted closing prices (`price_lines.png`)
  - **Line chart** of daily log returns (`return_lines.png`)
  - **Heatmap** of correlation between returns (`returns_correlation_heatmap.png`)
  -  **Bar chart** comparing annualized volatility (`volatility_bar.png`)
- Exports a summary table:
  - `outputs/tables/volatility_summary.csv`

---

 **End Result:**  
After running the full workflow, the project will contain:
- Cleaned and reproducible stock data  
- Volatility summary table  
- Four professional visualizations stored in `outputs/figures/`  


