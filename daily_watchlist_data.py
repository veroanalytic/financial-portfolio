import pandas as pd
import yfinance as yf
import datetime 
from pandas.tseries.offsets import BDay


def ticker_info(): # ticker_symbol

    watchlist = ["PEP", "MSFT", "AAPL", "O", "JNJ", "PG"]
    
    df_list = []

    for t in watchlist:
        df_list.append(pd.DataFrame([yf.Ticker(t).info]))
    
    df = pd.concat(df_list)

      # Rename columns
    df = df.rename(columns={
                            "symbol": "Symbol",
                            "shortName": "Company", 
                            "industry": "Industry",
                            "payoutRatio": "Payout_Ratio",
                            "pegRatio": "PEG_Ratio",
                            "trailingPE": "Trailing_PE",
                            "forwardPE": "Forward_PE",
                            "sector": "Sector",
                            "lastDividendDate": "Last_Dividend_Date",
                            "currentPrice": "Current_Pricing",
                            "targetLowPrice": "Target_Low_Price",
                            "targetMedianPrice": "Target_Median_Price",
                            "targetHighPrice": "Target_High_Price",
                            "fiftyTwoWeekLow":  "Week_52_Low_Pricing",
                            "fiftyTwoWeekHigh": "Week_52_High_Pricing",
                            "fiftyDayAverage": "Fifty_Day_Average_Pricing",
                            "twoHundredDayAverage": "TwoHundred_Day_Avg_Pricing"
                            })


    df["Current_Date"] = datetime.datetime.today() - BDay(0)
    df["Previous_Date"] = datetime.datetime.today() - BDay(1)

    # Create derived columns 
    df["Dividend_Yield"] = df["dividendYield"] * 100
    df["Daily_Change_Percent"] = (df["Current_Pricing"] - df["previousClose"]) / df["Current_Pricing"] * 100
    df["Fifty_Day_Avg_Percent"] = (df["Current_Pricing"] - df["Fifty_Day_Average_Pricing"]) / df["Current_Pricing"] * 100
    df["TwoHundred_Day_Avg_Percent"] = (df["Current_Pricing"] - df["TwoHundred_Day_Avg_Pricing"]) / df["Current_Pricing"] * 100
    df["Week_52_Low_Percent"] = (df["Current_Pricing"] - df["Week_52_Low_Pricing"]) / df["Current_Pricing"] * 100
    df["Week_52_High_Percent"] = (df["Current_Pricing"] - df["Week_52_High_Pricing"]) / df["Current_Pricing"] * 100

  

    # Adding percent or dollar symbols
    df["Current_Pricing"] = df["Current_Pricing"].map("${:,.2f}".format)
    df["Previous_Close_Pricing"] = df["previousClose"].map("${:,.2f}".format)
    df["Fifty_Day_Average_Pricing"] = df["Fifty_Day_Average_Pricing"].map("${:,.2f}".format)
    df["TwoHundred_Day_Avg_Pricing"] = df["TwoHundred_Day_Avg_Pricing"].map("${:,.2f}".format)
    df["Week_52_Low_Pricing"] = df["Week_52_Low_Pricing"].map("${:,.2f}".format)
    df["Week_52_High_Pricing"] = df["Week_52_High_Pricing"].map("${:,.2f}".format)
    df["Target_Low_Price"] = df["Target_Low_Price"].map("${:,.2f}".format)
    df["Target_Median_Price"] = df["Target_Median_Price"].map("${:,.2f}".format)
    df["Target_High_Price"] = df["Target_High_Price"].map("${:,.2f}".format)


    df = df[["Symbol", "Company", "Sector", "Industry", "Trailing_PE", "Forward_PE",
             "Dividend_Yield", "Payout_Ratio", "PEG_Ratio",
             "Current_Date", "Previous_Date", "Last_Dividend_Date",
             "Current_Pricing", "Previous_Close_Pricing", 
             "Fifty_Day_Average_Pricing", "TwoHundred_Day_Avg_Pricing", 
             "Week_52_Low_Pricing", "Week_52_High_Pricing", 
             "Daily_Change_Percent", "Fifty_Day_Avg_Percent", "TwoHundred_Day_Avg_Percent", 
             "Week_52_Low_Percent", "Week_52_High_Percent",
             "Target_Low_Price", "Target_Median_Price", "Target_High_Price"


    ]]

    return df