import pandas as pd
import yfinance as yf
import datetime 
from pandas.tseries.offsets import BDay


def ticker_info(): # ticker_symbol

    l = ["MCD", "PEP", "MSFT", "AAPL", "O"]

    df_list = []

    for t in l:
        df_list.append(pd.DataFrame([yf.Ticker(t).info]))
    
    df = pd.concat(df_list)

    df["Current_Date"] = datetime.date.today() - BDay(0)
    df["Previous_Date"] = datetime.date.today() - BDay(1)

    # Create derived columns
    df["Daily_Percent_Change"] = (df["currentPrice"] - df["previousClose"]) / df["currentPrice"] * 100
    df["Fifty_Day_Avg_%"] = (df["currentPrice"] - df["fiftyDayAverage"]) / df["currentPrice"] * 100
    df["TwoHundred_Day_Avg_%"] = (df["currentPrice"] - df["twoHundredDayAverage"]) / df["currentPrice"] * 100
    df["Week_52_Low_Avg_%"] = (df["currentPrice"] - df["fiftyTwoWeekLow"]) / df["currentPrice"] * 100
    df["Week_52_High_Avg_%"] = (df["currentPrice"] - df["fiftyTwoWeekHigh"]) / df["currentPrice"] * 100

    # Adding percent or dollar symbols
    df["currentPrice"] = df["currentPrice"].map("${:,.2f}".format)
    df["previousClose"] = df["previousClose"].map("${:,.2f}".format)
    df["fiftyDayAverage"] = df["fiftyDayAverage"].map("${:,.2f}".format)
    df["twoHundredDayAverage"] = df["twoHundredDayAverage"].map("${:,.2f}".format)
    df["fiftyTwoWeekLow"] = df["fiftyTwoWeekLow"].map("${:,.2f}".format)
    df["fiftyTwoWeekHigh"] = df["fiftyTwoWeekHigh"].map("${:,.2f}".format)

    # Reorder columns in df

    df = df[["symbol", "Current_Date", 
            "currentPrice", "Daily_Percent_Change",
            "Fifty_Day_Avg_%", "TwoHundred_Day_Avg_%", "Week_52_Low_Avg_%", "Week_52_High_Avg_%",
            "Previous_Date", 
            "previousClose", "fiftyDayAverage", "twoHundredDayAverage", 
            "fiftyTwoWeekLow", "fiftyTwoWeekHigh"

    ]]

    return df