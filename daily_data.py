import pandas as pd
import yfinance as yf
import datetime 
from pandas.tseries.offsets import BDay


def ticker_info(): # ticker_symbol

    l = ["MCD", "PEP", "MSFT", "AAPL", "O", "KO"]

    df_list = []

    for t in l:
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
                            "targetHighPrice": "Target_High_Price"
                            })


    df["Current_Date"] = datetime.datetime.today() - BDay(0)
    df["Previous_Date"] = datetime.datetime.today() - BDay(1)

    # Create derived columns 
    df["Dividend_Yield"] = df["dividendYield"] * 100
    df["Daily_Change_Percent"] = (df["Current_Pricing"] - df["previousClose"]) / df["Current_Pricing"] * 100
    df["Fifty_Day_Avg_Percent"] = (df["Current_Pricing"] - df["fiftyDayAverage"]) / df["Current_Pricing"] * 100
    df["TwoHundred_Day_Avg_Percent"] = (df["Current_Pricing"] - df["twoHundredDayAverage"]) / df["Current_Pricing"] * 100
    df["Week_52_Low_Percent"] = (df["Current_Pricing"] - df["fiftyTwoWeekLow"]) / df["Current_Pricing"] * 100
    df["Week_52_High_Percent"] = (df["Current_Pricing"] - df["fiftyTwoWeekHigh"]) / df["Current_Pricing"] * 100

  

    # Adding percent or dollar symbols
    df["Current_Pricing"] = df["Current_Pricing"].map("${:,.2f}".format)
    df["Previous_Close_Pricing"] = df["previousClose"].map("${:,.2f}".format)
    df["Fifty_Day_Average_Pricing"] = df["fiftyDayAverage"].map("${:,.2f}".format)
    df["TwoHundred_Day_Avg_Pricing"] = df["twoHundredDayAverage"].map("${:,.2f}".format)
    df["Week_52_Low_Pricing"] = df["fiftyTwoWeekLow"].map("${:,.2f}".format)
    df["Week_52_High_Pricing"] = df["fiftyTwoWeekHigh"].map("${:,.2f}".format)
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