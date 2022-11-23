import streamlit as st
import pandas as pd
from history_data import ticker_price_action
from daily_watchlist_data import ticker_info
import os

pwd = os.getcwd()


# Assign function call to ticker for History
pep_ticker = ticker_price_action("PEP")
msft_ticker = ticker_price_action("MSFT")
aapl_ticker = ticker_price_action("AAPL")
o_ticker = ticker_price_action("O")
pg_ticker = ticker_price_action("PG")
jnj_ticker = ticker_price_action("JNJ")



# Call Daily function
daily_info = ticker_info()

# Export History Data to CSV
pep_ticker.to_csv(pwd + "\\history.csv", mode ="w", header=True, index=False)
msft_ticker.to_csv(pwd + "\\history.csv", mode ="a", header=False, index=False)
aapl_ticker.to_csv(pwd + "\\history.csv", mode ="a", header=False, index=False)
o_ticker.to_csv(pwd + "\\history.csv", mode ="a", header=False, index=False)
pg_ticker.to_csv(pwd + "\\history.csv", mode ="a", header=False, index=False)
jnj_ticker.to_csv(pwd + "\\history.csv", mode ="a", header=False, index=False)



# Export Daily Data to CSV
daily_info.to_csv(pwd + "\\daily.csv", mode ="w", header=True, index=False)

# Create CSV data frame the import into Streamlit
df_hist = pd.read_csv(pwd + "\\history.csv")
df_daily = pd.read_csv(pwd + "\\daily.csv")

df_merged = pd.concat([df_hist, df_daily], axis=1)

df_date_check = df_merged.copy()
df_percent = df_merged.copy()
df_dollar_price = df_merged.copy()
df_low_median_high = df_merged.copy()

df_date_check = df_date_check[["Symbol", "Company", "Sector", "Industry", "Trailing_PE", "Forward_PE",
                               "Dividend_Yield", "Payout_Ratio", "PEG_Ratio",
                               "Current_Date", "Date", "Previous_Date"]] 

df_dollar_price = df_dollar_price[["Symbol", "Current_Pricing",
                    "Previous_Close_Pricing", "Wkly_Avg_Close_Pricing", "Monthly_Avg_Close_Pricing", 
                    "Fifty_Day_Average_Pricing", "TwoHundred_Day_Avg_Pricing", 
                    "Week_52_Low_Pricing", "Week_52_High_Pricing"]]                                       

df_percent = df_percent[[
            "Symbol", "Current_Pricing",
            "Daily_Change_Percent",
            "Wkly_Avg_Close_Percent", "Monthly_Avg_Close_Percent",
            "Fifty_Day_Avg_Percent", "TwoHundred_Day_Avg_Percent", "Week_52_Low_Percent", "Week_52_High_Percent",
            ]]

df_low_median_high = df_low_median_high[[
            "Symbol", "Current_Pricing",
            "Target_Low_Price", "Target_Median_Price", "Target_High_Price"
            ]]



# Run Streamlit

# Streamlit conditional function
def percent_variance(val):
    if val < -10:
        color = "red"
    elif val < 0:
        color = "#FF6A6A"
    elif val > 10:
        color = "#00CD00"
    elif val > 0:
        color = "#3CB371"

    # color = "#FF6A6A" if val < 0 else "green" # if val > 0 else "green"
    return f"background-color: {color}"


st.set_page_config(layout="wide")
st.title("Weekly DCA Assessment")

st.markdown("""---""")

st.header("Daily Data")
# st.write(df_daily)

st.subheader("Company Info:")
st.dataframe(df_date_check)

st.subheader("Percent Difference:")
st.dataframe(df_percent)
# st.dataframe(df_percent.style.applymap(percent_variance, subset=["Daily_Change_Percent", "Wkly_Avg_Close_Percent", "Monthly_Avg_Close_Percent",
#                                                                 "Fifty_Day_Avg_Percent", "TwoHundred_Day_Avg_Percent", 
#                                                                 "Week_52_Low_Percent", "Week_52_High_Percent"]))

st.subheader("Pricing:")
st.dataframe(df_dollar_price)


st.subheader("Targets:")
st.dataframe(df_low_median_high)


st.markdown("""---""")

# st.header("Historical Data:")

# st.dataframe(df_hist.style.applymap(percent_variance, subset=["Wkly_Avg_Close_Percent", "Monthly_Avg_Close_Percent",
#                                                              "Semi_Annual_Avg_Close_Percent", "Annual_Avg_Close_Percent", "Two_Year_Avg_Close_Percent"
#                                                              ]))

# # st.subheader("McDonald's Corp")
# # st.write(mcd_df)
# st.dataframe(mcd_df.style.applymap(percent_variance, subset=["Wkly_Avg_Close_Percent", "Monthly_Avg_Close_Percent",
#                                                              "Semi_Annual_Avg_Close_Percent", "Annual_Avg_Close_Percent", "Two_Year_Avg_Close_Percent"
#                                                              ]))

# # st.subheader("PepsiCo, Inc.")
# # st.write(pep_df)
# st.dataframe(pep_df.style.applymap(percent_variance, subset=["Wkly_Avg_Close_Percent", "Monthly_Avg_Close_Percent",
#                                                              "Semi_Annual_Avg_Close_Percent", "Annual_Avg_Close_Percent", "Two_Year_Avg_Close_Percent"
#                                                              ]))

# # st.subheader("Microsoft Corp")
# # st.write(msft_df)
# st.dataframe(msft_df.style.applymap(percent_variance, subset=["Wkly_Avg_Close_Percent", "Monthly_Avg_Close_Percent",
#                                                              "Semi_Annual_Avg_Close_Percent", "Annual_Avg_Close_Percent", "Two_Year_Avg_Close_Percent"
#                                                              ]))

# # st.subheader("Apple Inc")
# # st.write(aapl_df)
# st.dataframe(aapl_df.style.applymap(percent_variance, subset=["Wkly_Avg_Close_Percent", "Monthly_Avg_Close_Percent",
#                                                              "Semi_Annual_Avg_Close_Percent", "Annual_Avg_Close_Percent", "Two_Year_Avg_Close_Percent"
#                                                              ]))                                                             

# # st.subheader("Realty Income Corp")
# # st.write(o_df)
# st.dataframe(o_df.style.applymap(percent_variance, subset=["Wkly_Avg_Close_Percent", "Monthly_Avg_Close_Percent",
#                                                              "Semi_Annual_Avg_Close_Percent", "Annual_Avg_Close_Percent", "Two_Year_Avg_Close_Percent"
#                                                              ]))

# add_sidebar = st.sidebar.selectbox("Test Side Bar Title", ("Test 1", "Test 2"))
