import streamlit as st
# from staging_data import df_merged, df_hist #, mcd_df, pep_df, msft_df, aapl_df, o_df, df_daily 
import pandas as pd
from history_data import ticker_price_action
from daily_data import ticker_info
import os

pwd = os.getcwd()


# Assign function call to ticker for History
mcd_ticker = ticker_price_action("MCD")
pep_ticker = ticker_price_action("PEP")
msft_ticker = ticker_price_action("MSFT")
aapl_ticker = ticker_price_action("AAPL")
o_ticker = ticker_price_action("O")
ko_ticker = ticker_price_action("KO")
# pg_ticker = ticker_price_action("PG")
# # jnj_ticker = ticker_price_action("JNJ")
# abbv_ticker = ticker_price_action("ABBV")

# Call Daily function
daily_info = ticker_info()

# Export History Data to CSV
mcd_ticker.to_csv(pwd + "\\history.csv", mode ="w", header=True, index=False)
pep_ticker.to_csv(pwd + "\\history.csv", mode ="a", header=False, index=False)
msft_ticker.to_csv(pwd + "\\history.csv", mode ="a", header=False, index=False)
aapl_ticker.to_csv(pwd + "\\history.csv", mode ="a", header=False, index=False)
o_ticker.to_csv(pwd + "\\history.csv", mode ="a", header=False, index=False)
ko_ticker.to_csv(pwd + "\\history.csv", mode ="a", header=False, index=False)
# pg_ticker.to_csv(pwd + "\\history.csv", mode ="a", header=False, index=False)
# jnj_ticker.to_csv(pwd + "\\history.csv", mode ="a", header=False, index=False)
# abbv_ticker.to_csv(pwd + "\\history.csv", mode ="a", header=False, index=False)

# Export Daily Data to CSV
daily_info.to_csv(pwd + "\\daily.csv", mode ="w", header=True, index=False)

# Create CSV data frame the import into Streamlit
df_hist = pd.read_csv(pwd + "\\history.csv")
df_daily = pd.read_csv(pwd + "\\daily.csv")

df_merged = pd.concat([df_hist, df_daily], axis=1)

df_date_check = df_merged.copy()
df_percent = df_merged.copy()
df_dollar_price = df_merged.copy()