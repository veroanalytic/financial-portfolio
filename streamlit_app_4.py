import streamlit as st
from staging_data_3 import mcd_df, pep_df, msft_df, aapl_df, o_df, df_daily

# Run Streamlit

# Streamlit conditional function
def percent_variance(val):
    color = "red" if val < 0 else "green" # if val > 0 else "green"
    return f"background-color: {color}"


st.set_page_config(layout="wide")
st.title("Weekly DCA Assessment")

st.header("Daily Data:")
# st.write(df_daily)
st.dataframe(df_daily.style.applymap(percent_variance, subset=["Daily_Percent_Change"]))


st.header("Historical Data:")
st.subheader("McDonald's Corp")
# st.write(mcd_df)
st.dataframe(mcd_df.style.applymap(percent_variance, subset=["Wkly_Avg_Close_Percent", "Monthly_Avg_Close_Percent",
                                                             "Semi_Annual_Avg_Close_Percent", "Annual_Avg_Close_Percent", "Two_Year_Avg_Close_Percent"
                                                             ]))

st.subheader("PepsiCo, Inc.")
# st.write(pep_df)
st.dataframe(pep_df.style.applymap(percent_variance, subset=["Wkly_Avg_Close_Percent", "Monthly_Avg_Close_Percent",
                                                             "Semi_Annual_Avg_Close_Percent", "Annual_Avg_Close_Percent", "Two_Year_Avg_Close_Percent"
                                                             ]))

st.subheader("Microsoft Corp")
# st.write(msft_df)
st.dataframe(msft_df.style.applymap(percent_variance, subset=["Wkly_Avg_Close_Percent", "Monthly_Avg_Close_Percent",
                                                             "Semi_Annual_Avg_Close_Percent", "Annual_Avg_Close_Percent", "Two_Year_Avg_Close_Percent"
                                                             ]))

st.subheader("Apple Inc")
# st.write(aapl_df)
st.dataframe(aapl_df.style.applymap(percent_variance, subset=["Wkly_Avg_Close_Percent", "Monthly_Avg_Close_Percent",
                                                             "Semi_Annual_Avg_Close_Percent", "Annual_Avg_Close_Percent", "Two_Year_Avg_Close_Percent"
                                                             ]))                                                             

st.subheader("Realty Income Corp")
# st.write(o_df)
st.dataframe(o_df.style.applymap(percent_variance, subset=["Wkly_Avg_Close_Percent", "Monthly_Avg_Close_Percent",
                                                             "Semi_Annual_Avg_Close_Percent", "Annual_Avg_Close_Percent", "Two_Year_Avg_Close_Percent"
                                                             ]))

# add_sidebar = st.sidebar.selectbox("Test Side Bar Title", ("Test 1", "Test 2"))
