import pandas as pd
import yfinance as yf
import datetime 
from pandas.tseries.offsets import BDay
from aristocrats_list import div_aristocrats
import os


def ticker_info(): # ticker_symbol

    df_list = []

    for t in div_aristocrats:
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



    df = df[["Symbol", "Company", "Sector", "Industry", 
             "Current_Pricing", "Trailing_PE", "Forward_PE",
             "Dividend_Yield", "Payout_Ratio", "PEG_Ratio",
             "Target_Low_Price", "Target_Median_Price", "Target_High_Price",
             "Week_52_Low_Pricing", "Week_52_High_Pricing", "Fifty_Day_Average_Pricing", "TwoHundred_Day_Avg_Pricing",
             "Current_Date", "Previous_Date",
             ]]

    return df

pwd = os.getcwd()

# Call Daily function
daily_info = ticker_info()


# Export Daily Data to CSV
daily_info.to_csv(pwd + "\\daily_aristocrat.csv", mode ="w", header=True, index=False)


# Create CSV data frame the import into Streamlit
# df_sl = pd.read_csv(pwd + "\\daily_aristocrat.csv")


# df_sl = df_sl[["Symbol", "Company", "Sector", "Industry", "Trailing_PE", "Forward_PE",
#                                "Dividend_Yield", "Payout_Ratio", "PEG_Ratio",
#                                "Current_Pricing", "Target_Low_Price", "Target_Median_Price", "Target_High_Price",
#                                "Week_52_Low_Pricing", "Week_52_High_Pricing", "Fifty_Day_Average_Pricing", "TwoHundred_Day_Avg_Pricing",
#                                "Current_Date", "Previous_Date"]]