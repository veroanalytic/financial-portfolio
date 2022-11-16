# Import Libraries
import yfinance as yf
import streamlit as st

def ticker_history(ticker_symbol):

    # Call yfinance ticker info
    ticker = yf.Ticker(ticker_symbol)

    # Assign variable for ticker history
    ticker_history = ticker.history(period="max")

    return ticker_history

def ticker_price_action(ticker_symbol):
    
    df = ticker_history(ticker_symbol)

    # Number of rows displayed
    rows_returned = 1

    # Create derived columns
    df["Ticker"] = ticker_symbol
    df["Wkly_Avg_Close"] = df["Close"].rolling(7).mean()
    df["Wkly_Avg_Close_Percent"] = (df["Close"] - df["Wkly_Avg_Close"]) / df["Close"] * 100
    df["Monthly_Avg_Close"] = df["Close"].rolling(30).mean()
    df["Monthly_Avg_Close_Percent"] = (df["Close"] - df["Monthly_Avg_Close"]) / df["Close"] * 100
    df["Semi_Annual_Avg_Close"] = df["Close"].rolling(183).mean()
    df["Semi_Annual_Avg_Close_Percent"] = (df["Close"] - df["Semi_Annual_Avg_Close"]) / df["Close"] * 100
    df["Annual_Avg_Close"] = df["Close"].rolling(365).mean()
    df["Annual_Avg_Close_Percent"] = (df["Close"] - df["Annual_Avg_Close"]) / df["Close"] * 100
    df["Two_Year_Avg_Close"] = df["Close"].rolling(730).mean()
    df["Two_Year_Avg_Close_Percent"] = (df["Close"] - df["Two_Year_Avg_Close"]) / df["Close"] * 100

    # Drop NAs
    df = df.dropna()


    df["Monthly_Avg_Close_Pricing"] = df["Monthly_Avg_Close"].map("${:,.2f}".format)
    df["Wkly_Avg_Close_Pricing"] = df["Wkly_Avg_Close"].map("${:,.2f}".format)

    # Create new DF of only needed columns
    df = df[["Ticker", "Close", 
            "Wkly_Avg_Close_Percent", "Monthly_Avg_Close_Percent",
            "Semi_Annual_Avg_Close_Percent", "Annual_Avg_Close_Percent", "Two_Year_Avg_Close_Percent",
            "Wkly_Avg_Close_Pricing", "Monthly_Avg_Close_Pricing", 
            "Semi_Annual_Avg_Close", "Annual_Avg_Close", "Two_Year_Avg_Close"
            ]] \
            .sort_values(by=["Date"], ascending=False) \
            .head(rows_returned)
    df = df.reset_index()

     # Adding percent or dollar symbols
    

    # df["Date"] = df["Date"].dt.date.sort_values(ascending=False)


    return df

