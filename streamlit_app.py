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

df_merged = pd.concat([df_hist, df_daily], axis=1)

df_merged = df_merged[[
            "Current_Date", "symbol", 
            "currentPrice", "Daily_Percent_Change",
            "Wkly_Avg_Close_Percent", "Monthly_Avg_Close_Percent",
            "Fifty_Day_Avg_%", "TwoHundred_Day_Avg_%", "Week_52_Low_Avg_%", "Week_52_High_Avg_%",
            "Previous_Date", 
            "previousClose", "Wkly_Avg_Close", "Monthly_Avg_Close", 
            "fiftyDayAverage", "twoHundredDayAverage", 
            "fiftyTwoWeekLow", "fiftyTwoWeekHigh"]]

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

st.header("Daily Data:")
# st.write(df_daily)
st.dataframe(df_merged.style.applymap(percent_variance, subset=["Daily_Percent_Change", "Wkly_Avg_Close_Percent", "Monthly_Avg_Close_Percent",
                                                                "Fifty_Day_Avg_%", "TwoHundred_Day_Avg_%", 
                                                                "Week_52_Low_Avg_%", "Week_52_High_Avg_%"]))

st.markdown("""---""")

st.header("Historical Data:")

st.dataframe(df_hist.style.applymap(percent_variance, subset=["Wkly_Avg_Close_Percent", "Monthly_Avg_Close_Percent",
                                                             "Semi_Annual_Avg_Close_Percent", "Annual_Avg_Close_Percent", "Two_Year_Avg_Close_Percent"
                                                             ]))

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
