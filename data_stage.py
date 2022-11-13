# Import Libraries
import pandas as pd
import yfinance as yf
import streamlit as st
import os
from time import sleep

pwd = os.getcwd()


def ticker_history(ticker_symbol):

    # Call yfinance ticker info
    ticker = yf.Ticker(ticker_symbol)

    # Assign variable for ticker history
    ticker_history = ticker.history(period="max")

    return ticker_history

def ticker_price_action(ticker_symbol):
    
    ticker_price_action = ticker_history(ticker_symbol)

    # Number of rows displayed
    rows_returned = 5

    # Create derived columns
    ticker_price_action["Ticker"] = ticker_symbol
    ticker_price_action["Wkly_Avg_Close"] = ticker_price_action["Close"].rolling(7).mean()
    ticker_price_action["Wkly_Avg_Close_Percent"] = (ticker_price_action["Close"] - ticker_price_action["Wkly_Avg_Close"]) / ticker_price_action["Close"] * 100
    ticker_price_action["Monthly_Avg_Close"] = ticker_price_action["Close"].rolling(30).mean()
    ticker_price_action["Monthly_Avg_Close_Percent"] = (ticker_price_action["Close"] - ticker_price_action["Monthly_Avg_Close"]) / ticker_price_action["Close"] * 100
    ticker_price_action["Semi_Annual_Avg_Close"] = ticker_price_action["Close"].rolling(183).mean()
    ticker_price_action["Semi_Annual_Avg_Close_Percent"] = (ticker_price_action["Close"] - ticker_price_action["Semi_Annual_Avg_Close"]) / ticker_price_action["Close"] * 100
    ticker_price_action["Annual_Avg_Close"] = ticker_price_action["Close"].rolling(365).mean()
    ticker_price_action["Annual_Avg_Close_Percent"] = (ticker_price_action["Close"] - ticker_price_action["Annual_Avg_Close"]) / ticker_price_action["Close"] * 100
    ticker_price_action["Two_Year_Avg_Close"] = ticker_price_action["Close"].rolling(730).mean()
    ticker_price_action["Two_Year_Avg_Close_Percent"] = (ticker_price_action["Close"] - ticker_price_action["Two_Year_Avg_Close"]) / ticker_price_action["Close"] * 100

    # Drop NAs
    ticker_price_action = ticker_price_action.dropna()

    # Create new DF of only needed columns
    ticker_price_action = ticker_price_action[["Ticker", "Close", 
                                    "Wkly_Avg_Close_Percent", "Monthly_Avg_Close_Percent",
                                    "Semi_Annual_Avg_Close_Percent", "Annual_Avg_Close_Percent", "Two_Year_Avg_Close_Percent",
                                    "Wkly_Avg_Close", "Monthly_Avg_Close", 
                                    "Semi_Annual_Avg_Close", "Annual_Avg_Close", "Two_Year_Avg_Close"
                                    ]] \
                                    .sort_values(by=["Date"], ascending=False) \
                                    .head(rows_returned)
    ticker_price_action = ticker_price_action.reset_index()

    ticker_price_action["Date"] = ticker_price_action["Date"].dt.date

    return ticker_price_action

# Assign function call to ticker
mcd_ticker = ticker_price_action("MCD")
pep_ticker = ticker_price_action("PEP")
msft_ticker = ticker_price_action("MSFT")
o_ticker = ticker_price_action("O")

# Export to CSV
mcd_ticker.to_csv(pwd + "\\stocks.csv", mode ="w", header=True, index=False)
pep_ticker.to_csv(pwd + "\\stocks.csv", mode ="a", header=False, index=False)
msft_ticker.to_csv(pwd + "\\stocks.csv", mode ="a", header=False, index=False)
o_ticker.to_csv(pwd + "\\stocks.csv", mode ="a", header=False, index=False)

# Create CSV data frame the import into Streamlit
mcd_df = pd.read_csv(pwd + "\\stocks.csv")
mcd_df = mcd_df[mcd_df["Ticker"] == "MCD"]

pep_df = pd.read_csv(pwd + "\\stocks.csv")
pep_df = pep_df[pep_df["Ticker"] == "PEP"]

msft_df = pd.read_csv(pwd + "\\stocks.csv")
msft_df = msft_df[msft_df["Ticker"] == "MSFT"]

o_df = pd.read_csv(pwd + "\\stocks.csv")
o_df = o_df[o_df["Ticker"] == "MSFT"]