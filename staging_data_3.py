import pandas as pd
from history_pull_1 import ticker_price_action
from daily_pull_2 import ticker_info
import os

pwd = os.getcwd()


# Assign function call to ticker for History
mcd_ticker = ticker_price_action("MCD")
pep_ticker = ticker_price_action("PEP")
msft_ticker = ticker_price_action("MSFT")
aapl_ticker = ticker_price_action("AAPL")
o_ticker = ticker_price_action("O")

# Call Daily function
daily_info = ticker_info()

# Export History Data to CSV
mcd_ticker.to_csv(pwd + "\\history.csv", mode ="w", header=True, index=False)
pep_ticker.to_csv(pwd + "\\history.csv", mode ="a", header=False, index=False)
msft_ticker.to_csv(pwd + "\\history.csv", mode ="a", header=False, index=False)
aapl_ticker.to_csv(pwd + "\\history.csv", mode ="a", header=False, index=False)
o_ticker.to_csv(pwd + "\\history.csv", mode ="a", header=False, index=False)

# Export Daily Data to CSV
daily_info.to_csv(pwd + "\\daily.csv", mode ="w", header=True, index=False)

# Create CSV data frame the import into Streamlit
df_hist = pd.read_csv(pwd + "\\history.csv")
df_daily = pd.read_csv(pwd + "\\daily.csv")

# Separate CSV History data by Ticker
mcd_df = df_hist[df_hist["Ticker"] == "MCD"]
pep_df = df_hist[df_hist["Ticker"] == "PEP"]
msft_df = df_hist[df_hist["Ticker"] == "MSFT"]
aapl_df = df_hist[df_hist["Ticker"] == "AAPL"]
o_df = df_hist[df_hist["Ticker"] == "O"]

