import pandas as pd
import yfinance as yf
import streamlit as st

import os

pwd = os.getcwd()

# =======================================================================================================================================
#                                                    MCD
# =======================================================================================================================================

mcd = yf.Ticker("mcd")
mcd_history = mcd.history(period="max")

# Create Ticker Column
mcd_history["Ticker"] = "MCD"

# Create rolling weekly average column
mcd_history["weekly_avg_close"] = mcd_history["Close"].rolling(7).mean()

# Create weekly average close percent column
mcd_history["weekly_avg_close_percent"] = (mcd_history["Close"] - mcd_history["weekly_avg_close"]) / mcd_history["Close"] * 100

# Create rolling monthly average column
mcd_history["monthly_avg_close"] = mcd_history["Close"].rolling(30).mean()

# Create monthly average close percent column
mcd_history["monthly_avg_close_percent"] = (mcd_history["Close"] - mcd_history["monthly_avg_close"]) / mcd_history["Close"] * 100

# Create rolling semi_annual average column
mcd_history["semi_annual_avg_close"] = mcd_history["Close"].rolling(183).mean()

# Create semi_annual average close percent column
mcd_history["semi_annual_avg_close_percent"] = (mcd_history["Close"] - mcd_history["semi_annual_avg_close"]) / mcd_history["Close"] * 100

# Create rolling annual average column
mcd_history["annual_avg_close"] = mcd_history["Close"].rolling(365).mean()

# Create annual average close percent column
mcd_history["annual_avg_close_percent"] = (mcd_history["Close"] - mcd_history["annual_avg_close"]) / mcd_history["Close"] * 100


# Create rolling two_year average column
mcd_history["two_year_avg_close"] = mcd_history["Close"].rolling(730).mean()

# Create two_year average close percent column
mcd_history["two_year_avg_close_percent"] = (mcd_history["Close"] - mcd_history["two_year_avg_close"]) / mcd_history["Close"] * 100

# Drop NAs
mcd_history = mcd_history.dropna()

# Grab only needed columns
mcd_price_action = mcd_history[["Ticker", "Close", 
                                "weekly_avg_close_percent", "monthly_avg_close_percent",
                                "semi_annual_avg_close_percent", "annual_avg_close_percent", "two_year_avg_close_percent",
                                "weekly_avg_close", "monthly_avg_close", 
                                "semi_annual_avg_close", "annual_avg_close", "two_year_avg_close"
                                ]] \
                                .sort_values(by=["Date"], ascending=False) \
                                .head(5)
mcd_price_action = mcd_price_action.reset_index()

# Export to CSV
mcd_price_action.to_csv(pwd + "\\stocks.csv", mode ="w", header=True, index=False)


# =======================================================================================================================================
#                                                    PEP
# =======================================================================================================================================
pep = yf.Ticker("PEP")
pep_history = pep.history(period="max")

# Create Ticker Column
pep_history["Ticker"] = "PEP"

# Create rolling weekly average column
pep_history["weekly_avg_close"] = pep_history["Close"].rolling(7).mean()

# Create weekly average close percent column
pep_history["weekly_avg_close_percent"] = (pep_history["Close"] - pep_history["weekly_avg_close"]) / pep_history["Close"] * 100

# Create rolling monthly average column
pep_history["monthly_avg_close"] = pep_history["Close"].rolling(30).mean()

# Create monthly average close percent column
pep_history["monthly_avg_close_percent"] = (pep_history["Close"] - pep_history["monthly_avg_close"]) / pep_history["Close"] * 100

# Create rolling semi_annual average column
pep_history["semi_annual_avg_close"] = pep_history["Close"].rolling(183).mean()

# Create semi_annual average close percent column
pep_history["semi_annual_avg_close_percent"] = (pep_history["Close"] - pep_history["semi_annual_avg_close"]) / pep_history["Close"] * 100

# Create rolling annual average column
pep_history["annual_avg_close"] = pep_history["Close"].rolling(365).mean()

# Create annual average close percent column
pep_history["annual_avg_close_percent"] = (pep_history["Close"] - pep_history["annual_avg_close"]) / pep_history["Close"] * 100

# Create rolling two_year average column
pep_history["two_year_avg_close"] = pep_history["Close"].rolling(730).mean()

# Create two_year average close percent column
pep_history["two_year_avg_close_percent"] = (pep_history["Close"] - pep_history["two_year_avg_close"]) / pep_history["Close"] * 100


# Drop NAs
pep_history = pep_history.dropna()

# Grab only needed columns
pep_price_action = pep_history[["Ticker", "Close", 
                                "weekly_avg_close_percent", "monthly_avg_close_percent",
                                "semi_annual_avg_close_percent", "annual_avg_close_percent", "two_year_avg_close_percent",
                                "weekly_avg_close", "monthly_avg_close", 
                                "semi_annual_avg_close", "annual_avg_close", "two_year_avg_close"
                                ]] \
                                .sort_values(by=["Date"], ascending=False) \
                                .head(5)
pep_price_action = pep_price_action.reset_index()


# Export to CSV
pep_price_action.to_csv(pwd + "\\stocks.csv", mode ="a", header=False, index=False)

# =======================================================================================================================================
#                                                    MSFT
# =======================================================================================================================================

msft = yf.Ticker("MSFT")
msft_history = msft.history(period="max")

msft_history["Ticker"] = "MSFT"

# Create rolling weekly average column
msft_history["weekly_avg_close"] = msft_history["Close"].rolling(7).mean()

# Create weekly average close percent column
msft_history["weekly_avg_close_percent"] = (msft_history["Close"] - msft_history["weekly_avg_close"]) / msft_history["Close"] * 100

# Create rolling monthly average column
msft_history["monthly_avg_close"] = msft_history["Close"].rolling(30).mean()

# Create monthly average close percent column
msft_history["monthly_avg_close_percent"] = (msft_history["Close"] - msft_history["monthly_avg_close"]) / msft_history["Close"] * 100

# Create rolling semi_annual average column
msft_history["semi_annual_avg_close"] = msft_history["Close"].rolling(183).mean()

# Create semi_annual average close percent column
msft_history["semi_annual_avg_close_percent"] = (msft_history["Close"] - msft_history["semi_annual_avg_close"]) / msft_history["Close"] * 100

# Create rolling annual average column
msft_history["annual_avg_close"] = msft_history["Close"].rolling(365).mean()

# Create annual average close percent column
msft_history["annual_avg_close_percent"] = (msft_history["Close"] - msft_history["annual_avg_close"]) / msft_history["Close"] * 100

# Create rolling two_year average column
msft_history["two_year_avg_close"] = msft_history["Close"].rolling(730).mean()

# Create two_year average close percent column
msft_history["two_year_avg_close_percent"] = (msft_history["Close"] - msft_history["two_year_avg_close"]) / msft_history["Close"] * 100


# Drop NAs
msft_history = msft_history.dropna()

# Grab only needed columns
msft_price_action = msft_history[["Ticker", "Close", 
                                "weekly_avg_close_percent", "monthly_avg_close_percent",
                                "semi_annual_avg_close_percent", "annual_avg_close_percent", "two_year_avg_close_percent",
                                "weekly_avg_close", "monthly_avg_close", 
                                "semi_annual_avg_close", "annual_avg_close", "two_year_avg_close"
                                ]] \
                                .sort_values(by=["Date"], ascending=False) \
                                .head(5)
msft_price_action = msft_price_action.reset_index()

# Export to CSV
msft_price_action.to_csv(pwd + "\\stocks.csv", mode ="a", header=False, index=False)


df = pd.read_csv(pwd + "\\stocks.csv")

st.title("Hello world!")
st.write(df)