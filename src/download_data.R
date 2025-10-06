# src/download_data.R
# Purpose: download raw stock data for AAPL, MSFT, GOOGL from Yahoo Finance

# ---- load package ----
if(!require(quantmod)) install.packages("quantmod", repos="https://cloud.r-project.org")
library(quantmod)

# ---- Stocks ----
tickers <- c("AAPL", "MSFT", "GOOGL")
start_date <- "2022-01-01"
end_date <- Sys.Date()

# ---- download and save ----
dir.create("data/raw", recursive = TRUE, showWarnings = FALSE)

for (t in tickers) {
  cat("Downloading:", t, "\n")
  getSymbols(t, src = "yahoo", from = start_date, to = end_date, auto.assign = TRUE)
  df <- get(t)
  df <- data.frame(date = index(df), coredata(df))
  out_path <- file.path("data", "raw", paste0(t, ".csv"))
  write.csv(df, out_path, row.names = FALSE)
}

cat("All data downloaded to data/raw/\n")
