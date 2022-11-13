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
mcd_ticker.to_csv(pwd + "\\mcd_stocks.csv", mode ="w", header=True, index=False)
pep_ticker.to_csv(pwd + "\\pep_stocks.csv", mode ="w", header=True, index=False)
msft_ticker.to_csv(pwd + "\\msft_stocks.csv", mode ="w", header=True, index=False)
o_ticker.to_csv(pwd + "\\o_stocks.csv", mode ="w", header=True, index=False)

# Create CSV data frame the import into Streamlit
mcd_df = pd.read_csv(pwd + "\\mcd_stocks.csv")
pep_df = pd.read_csv(pwd + "\\pep_stocks.csv")
msft_df = pd.read_csv(pwd + "\\msft_stocks.csv")
o_df = pd.read_csv(pwd + "\\o_stocks.csv")


# Run Streamlit

# Streamlit conditional function
def percent_variance(val):
    color = "red" if val < 0 else "green" # if val > 0 else "green"
    return f"background-color: {color}"


st.set_page_config(layout="wide")
st.title("Weekly DCA Assessment")

st.subheader("McDonald's Corp")
# st.write(mcd_df)
st.dataframe(mcd_df.style.applymap(percent_variance, subset=["Wkly_Avg_Close_Percent", "Monthly_Avg_Close_Percent",
                                                             "Semi_Annual_Avg_Close_Percent", "Annual_Avg_Close_Percent", "Two_Year_Avg_Close_Percent"
                                                             ]))

st.subheader("PepsiCo, Inc.")
# st.write(pep_df)
st.dataframe(pep_df.style.applymap(percent_variance, subset=["Wkly_Avg_Close_Percent", "Monthly_Avg_Close_Percent",
                                                             "Semi_Annual_Avg_Close_Percent", "Annual_Avg_Close_Percent", "Two_Year_Avg_Close_Percent"
                                                             ]))

st.subheader("Microsoft Corp")
# st.write(msft_df)
st.dataframe(msft_df.style.applymap(percent_variance, subset=["Wkly_Avg_Close_Percent", "Monthly_Avg_Close_Percent",
                                                             "Semi_Annual_Avg_Close_Percent", "Annual_Avg_Close_Percent", "Two_Year_Avg_Close_Percent"
                                                             ]))

st.subheader("Realty Income Corp")
# st.write(o_df)
st.dataframe(o_df.style.applymap(percent_variance, subset=["Wkly_Avg_Close_Percent", "Monthly_Avg_Close_Percent",
                                                             "Semi_Annual_Avg_Close_Percent", "Annual_Avg_Close_Percent", "Two_Year_Avg_Close_Percent"
                                                             ]))

# add_sidebar = st.sidebar.selectbox("Test Side Bar Title", ("Test 1", "Test 2"))
