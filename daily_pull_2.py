import pandas as pd
import yfinance as yf
import streamlit as st
import os
import datetime
from pandas.tseries.offsets import BDay

pwd = os.getcwd()

def ticker_info(): # ticker_symbol

    l = ["MCD", "PEP", "MSFT", "AAPL", "O"]

    df_list = []

    for t in l:
        df_list.append(pd.DataFrame([yf.Ticker(t).info]))
    
    df = pd.concat(df_list)

    df["Current_Date"] = datetime.datetime.today() - BDay(0)
    df["Previous_Date"] = datetime.datetime.today() - BDay(1)

    df = df[["symbol", "shortName",
            "currentPrice", "previousClose",      
            "dividendRate", "dividendYield",
            "Current_Date", "Previous_Date",

    ]]

    # Create derived columns
    df["Daily_Percent_Change"] = (df["currentPrice"] - df["previousClose"]) / df["currentPrice"] * 100
    df["dividendYield"] = df["dividendYield"] * 100

    # Adding percent or dollar symbols
    df["currentPrice"] = df["currentPrice"].map("${:,.2f}".format)
    df["previousClose"] = df["previousClose"].map("${:,.2f}".format)
    # df["Daily_Percent_Change"] = df["Daily_Percent_Change"].map("{:,.2f}%".format)
    df["dividendRate"] = df["dividendRate"].map("${:,.2f}".format)
    df["dividendYield"] = df["dividendYield"].map("{:,.2f}%".format)

    # Reorder columns in df

    df = df[["symbol", "shortName", "Daily_Percent_Change",
            "currentPrice", "previousClose", 
            "dividendRate", "dividendYield",
            "Current_Date", "Previous_Date",
    ]]

    return df