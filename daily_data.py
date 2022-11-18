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
    df["Last_Dividend_Date"] = df["lastDividendDate"]
#     df["Last_Dividend_Date"] = pd.to_datetime(df["lastDividendDate"])

    # Create derived columns / rename columns
    df["Symbol"] = df["symbol"]
    df["Company"] = df["shortName"]
    df["Industry"] = df["industry"]
    df["Payout_Ratio"]= df["payoutRatio"]
    df["Dividend_Yield"] = df["dividendYield"] * 100
    df = df.rename(columns={"pegRatio": "PEG_Ratio"})
    df = df.rename(columns={"trailingPE": "Trailing_PE"})
    df = df.rename(columns={"forwardPE": "Forward_PE"})
    
    df["Daily_Change_Percent"] = (df["currentPrice"] - df["previousClose"]) / df["currentPrice"] * 100
    df["Fifty_Day_Avg_Percent"] = (df["currentPrice"] - df["fiftyDayAverage"]) / df["currentPrice"] * 100
    df["TwoHundred_Day_Avg_Percent"] = (df["currentPrice"] - df["twoHundredDayAverage"]) / df["currentPrice"] * 100
    df["Week_52_Low_Percent"] = (df["currentPrice"] - df["fiftyTwoWeekLow"]) / df["currentPrice"] * 100
    df["Week_52_High_Percent"] = (df["currentPrice"] - df["fiftyTwoWeekHigh"]) / df["currentPrice"] * 100

    # Adding percent or dollar symbols
    df["Current_Pricing"] = df["currentPrice"].map("${:,.2f}".format)
    df["Previous_Close_Pricing"] = df["previousClose"].map("${:,.2f}".format)
    df["Fifty_Day_Average_Pricing"] = df["fiftyDayAverage"].map("${:,.2f}".format)
    df["TwoHundred_Day_Avg_Pricing"] = df["twoHundredDayAverage"].map("${:,.2f}".format)
    df["Week_52_Low_Pricing"] = df["fiftyTwoWeekLow"].map("${:,.2f}".format)
    df["Week_52_High_Pricing"] = df["fiftyTwoWeekHigh"].map("${:,.2f}".format)

    return df