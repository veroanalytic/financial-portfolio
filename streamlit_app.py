import streamlit as st
from data_stage import mcd_df, pep_df, msft_df, o_df

# Run Streamlit

# Streamlit conditional function
def percent_variance(val):
    color = "red" if val < 0 else "green" # if val > 0 else "green"
    return f"background-color: {color}"


st.set_page_config(layout="wide")
st.title("Weekly DCA Assessment")

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

st.subheader("Realty Income Corp")
# st.write(o_df)
st.dataframe(o_df.style.applymap(percent_variance, subset=["Wkly_Avg_Close_Percent", "Monthly_Avg_Close_Percent",
                                                             "Semi_Annual_Avg_Close_Percent", "Annual_Avg_Close_Percent", "Two_Year_Avg_Close_Percent"
                                                             ]))

# add_sidebar = st.sidebar.selectbox("Test Side Bar Title", ("Test 1", "Test 2"))