import streamlit as st
import pandas as pd
# from daily_aristocrats_data import df_sl
import os
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode



pwd = os.getcwd()

# # Call Daily function
# daily_info = ticker_info()


# # Export Daily Data to CSV
# daily_info.to_csv(pwd + "\\daily_aristocrat.csv", mode ="w", header=True, index=False)


# Create CSV data frame the import into Streamlit
df_sl = pd.read_csv(pwd + "\\daily_aristocrat.csv")



st.set_page_config(layout="wide")



st.title("Company Assessment")

st.markdown("""---""")

st.header("Daily Data")
# st.write(df_daily)

st.subheader("Company Info:")
# st.dataframe(df_sl)                       


# AgGrid(df_sl)

gb = GridOptionsBuilder.from_dataframe(df_sl)
# gb.configure_pagination(paginationAutoPageSize=True)
gb.configure_default_column(enablePivot=True, enableValue=True, enableRowGroup=True)
gb.configure_side_bar()
gb.configure_selection(selection_mode="multiple", use_checkbox=True)
gridOptions = gb.build()

grid_response = AgGrid(
    df_sl,
    gridOptions=gridOptions,
    update_mode=GridUpdateMode.MODEL_CHANGED,
    data_return_mode=DataReturnMode.FILTERED_AND_SORTED,
    fit_columns_on_grid_load=True,
    # theme="streamlit",
    enable_enterprise_modules=True,
    height=300,
    width="100%",
    header_checkbox_selection_filtered_only=True,
    use_checkbox=True,
    # reload_data=True
)


data = grid_response["data"]
selected = grid_response["selected_rows"]

if selected:
    st.subheader("Company Comparison:")
    dfs = pd.DataFrame(selected)
    dfs = dfs.drop(["_selectedRowNodeInfo", "Current_Date", "Previous_Date"], axis=1)

    AgGrid(dfs, fit_columns_on_grid_load=True)


    # dfs_chart = dfs.copy()
    # dfs_chart = dfs_chart[["Current_Date", "Current_Pricing", "Target_Low_Price", "Target_Median_Price", "Target_High_Price"]]
    # st.bar_chart(data=dfs_chart)

