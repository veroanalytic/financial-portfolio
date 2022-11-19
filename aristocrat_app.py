import streamlit as st
import pandas as pd
from history_data import ticker_price_action
from daily_data import ticker_info
import os


# Call Daily function
daily_info = ticker_info()