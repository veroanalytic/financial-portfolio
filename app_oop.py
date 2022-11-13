# Import Libraries
import pandas as pd
import yfinance as yf
import streamlit as st
import os

pwd = os.getcwd()


def ticker_function(ticker_symbol):

    # Call yfinance ticker info
    ticker = yf.Ticker(ticker_symbol)

    # Assign variable for ticker history
    ticker_history = ticker.history(period="max")

    # Create derived columns
    ticker_history["Ticker"] = ticker_symbol
    ticker_history["Wkly_Avg_Close"] = ticker_history["Close"].rolling(7).mean()
    ticker_history["Wkly_Avg_Close_Percent"] = (ticker_history["Close"] - ticker_history["Wkly_Avg_Close"]) / ticker_history["Close"] * 100
    ticker_history["Monthly_Avg_Close"] = ticker_history["Close"].rolling(30).mean()
    ticker_history["Monthly_Avg_Close_Percent"] = (ticker_history["Close"] - ticker_history["Monthly_Avg_Close"]) / ticker_history["Close"] * 100
    ticker_history["Semi_Annual_Avg_Close"] = ticker_history["Close"].rolling(183).mean()
    ticker_history["Semi_Annual_Avg_Close_Percent"] = (ticker_history["Close"] - ticker_history["Semi_Annual_Avg_Close"]) / ticker_history["Close"] * 100
    ticker_history["Annual_Avg_Close"] = ticker_history["Close"].rolling(365).mean()
    ticker_history["Annual_Avg_Close_Percent"] = (ticker_history["Close"] - ticker_history["Annual_Avg_Close"]) / ticker_history["Close"] * 100
    ticker_history["Two_Year_Avg_Close"] = ticker_history["Close"].rolling(730).mean()
    ticker_history["Two_Year_Avg_Close_Percent"] = (ticker_history["Close"] - ticker_history["Two_Year_Avg_Close"]) / ticker_history["Close"] * 100

    # Drop NAs
    ticker_history = ticker_history.dropna()

    # Create new DF of only needed columns
    ticker_price_action = ticker_history[["Ticker", "Close", 
                                    "Wkly_Avg_Close_Percent", "Monthly_Avg_Close_Percent",
                                    "Semi_Annual_Avg_Close_Percent", "Annual_Avg_Close_Percent", "Two_Year_Avg_Close_Percent",
                                    "Wkly_Avg_Close", "Monthly_Avg_Close", 
                                    "Semi_Annual_Avg_Close", "Annual_Avg_Close", "Two_Year_Avg_Close"
                                    ]] \
                                    .sort_values(by=["Date"], ascending=False) \
                                    .head(5)
    ticker_price_action = ticker_price_action.reset_index()

    # ticker_price_action["Date"] = ticker_price_action["Date"].dt.date

    return ticker_price_action

# Assign function call to ticker
mcd_ticker = ticker_function("MCD")
pep_ticker = ticker_function("PEP")
msft_ticker = ticker_function("MSFT")

# Export to CSV
mcd_ticker.to_csv(pwd + "\\stocks.csv", mode ="w", header=True, index=False)
pep_ticker.to_csv(pwd + "\\stocks.csv", mode ="a", header=False, index=False)
msft_ticker.to_csv(pwd + "\\stocks.csv", mode ="a", header=False, index=False)

# Create CSV data frame the import into Streamlit
df = pd.read_csv(pwd + "\\stocks.csv")

# Run Streamlit
st.title("Weekly DCA Assessment")
st.write(df)

add_sidebar = st.sidebar.selectbox("Test Side Bar Title", ("Test 1", "Test 2"))