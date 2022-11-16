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

    df["Current_Date"] = datetime.datetime.today() - BDay(0)
    df["Previous_Date"] = datetime.datetime.today() - BDay(1)

    # Create derived columns
    df["Symbol"] = df["symbol"]
    df["Daily_Change_Percent"] = (df["currentPrice"] - df["previousClose"]) / df["currentPrice"] * 100
    df["Fifty_Day_Avg_Percent"] = (df["currentPrice"] - df["fiftyDayAverage"]) / df["currentPrice"] * 100
    df["TwoHundred_Day_Avg_Percent"] = (df["currentPrice"] - df["twoHundredDayAverage"]) / df["currentPrice"] * 100
    df["Week_52_Low_Avg_Percent"] = (df["currentPrice"] - df["fiftyTwoWeekLow"]) / df["currentPrice"] * 100
    df["Week_52_High_Avg_Percent"] = (df["currentPrice"] - df["fiftyTwoWeekHigh"]) / df["currentPrice"] * 100

    # Adding percent or dollar symbols
    df["Current_Pricing"] = df["currentPrice"].map("${:,.2f}".format)
    df["Previous_Close_Pricing"] = df["previousClose"].map("${:,.2f}".format)
    df["Fifty_Day_Average_Pricing"] = df["fiftyDayAverage"].map("${:,.2f}".format)
    df["TwoHundred_Day_Avg_Pricing"] = df["twoHundredDayAverage"].map("${:,.2f}".format)
    df["Week_52_Low_Avg_Pricing"] = df["fiftyTwoWeekLow"].map("${:,.2f}".format)
    df["Week_52_High_Avg_Pricing"] = df["fiftyTwoWeekHigh"].map("${:,.2f}".format)

    # Reorder columns in df

    df = df[["Current_Date", "Symbol", 
            "Current_Pricing", "Daily_Change_Percent",
            "Fifty_Day_Avg_Percent", "TwoHundred_Day_Avg_Percent", "Week_52_Low_Avg_Percent", "Week_52_High_Avg_Percent",
            "Previous_Date", 
            "Previous_Close_Pricing", "Fifty_Day_Average_Pricing", "TwoHundred_Day_Avg_Pricing", 
            "Week_52_Low_Avg_Pricing", "Week_52_High_Avg_Pricing"

    ]]

    return df