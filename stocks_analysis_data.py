import pandas as pd
import yfinance as yf
import datetime 
from pandas.tseries.offsets import BDay
from overall_stocks_list import stocks_analysis
import os


def ticker_info(): # ticker_symbol

    df_list = []

    for t in stocks_analysis:
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
    df["Dividend_Yield"] = round(df["dividendYield"] * 100, 2)
    df["Payout_Ratio"] = round(df["Payout_Ratio"], 2)
    df["PEG_Ratio"] = round(df["PEG_Ratio"], 2)
    df["Trailing_PE"] = round(df["Trailing_PE"], 2)
    df["Forward_PE"] = round(df["Forward_PE"], 2)
    df["PEG_Ratio"] = round(df["PEG_Ratio"], 2)
    df["Current_Pricing"] = round(df["Current_Pricing"], 2)
    df["Week_52_Low_Pricing"] = round(df["Week_52_Low_Pricing"], 2)
    df["Week_52_High_Pricing"] = round(df["Week_52_High_Pricing"], 2)
    df["Fifty_Day_Average_Pricing"] = round(df["Fifty_Day_Average_Pricing"], 2)
    df["TwoHundred_Day_Avg_Pricing"] = round(df["TwoHundred_Day_Avg_Pricing"], 2)



    df = df[["Symbol", "Company", "Sector", "Industry", 
             "Current_Pricing", "Trailing_PE", "Forward_PE",
             "Dividend_Yield", "Payout_Ratio", "PEG_Ratio",
            #  "Target_Low_Price", "Target_Median_Price", "Target_High_Price",
             "Week_52_Low_Pricing", "Week_52_High_Pricing", "Fifty_Day_Average_Pricing", "TwoHundred_Day_Avg_Pricing",
             "Current_Date", "Previous_Date",
             ]]

    return df

pwd = os.getcwd()

# Call Daily function
daily_info = ticker_info()


# Export Daily Data to CSV
daily_info.to_csv(pwd + "\\stocks_analysis.csv", mode ="w", header=True, index=False)


# Create CSV data frame the import into Streamlit
# df_sl = pd.read_csv(pwd + "\\daily_aristocrat.csv")


# df_sl = df_sl[["Symbol", "Company", "Sector", "Industry", "Trailing_PE", "Forward_PE",
#                                "Dividend_Yield", "Payout_Ratio", "PEG_Ratio",
#                                "Current_Pricing", "Target_Low_Price", "Target_Median_Price", "Target_High_Price",
#                                "Week_52_Low_Pricing", "Week_52_High_Pricing", "Fifty_Day_Average_Pricing", "TwoHundred_Day_Avg_Pricing",
#                                "Current_Date", "Previous_Date"]]