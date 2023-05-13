# IMPORT LIBRARIES

import streamlit as st
import pandas as pd
import numpy as np
import time 
import requests
import csv
import altair as alt
import numpy as np
from datetime import datetime
alt.data_transformers.disable_max_rows()

# # Read files for Valence Score
# anton_total_valence_monthly = pd.read_csv("data/lineChartData/AntonDfMonthly.csv")
# emil_total_valence_monthly = pd.read_csv("data/lineChartData/EmilDfMonthly.csv")
# freyja_total_valence_monthly = pd.read_csv("data/lineChartData/FreyjaDfMonthly.csv")
# laura_total_valence_monthly = pd.read_csv("data/lineChartData/LauraDfMonthly.csv")
# jonathan_total_valence_monthly = pd.read_csv("data/lineChartData/JonathanDfMonthly.csv")

# # Read files for Danceability


# # Concatenate the dataframes vertically
# merged_total_df = pd.concat([
#     anton_total_valence_monthly, 
#     emil_total_valence_monthly, 
#     freyja_total_valence_monthly, 
#     laura_total_valence_monthly, 
#     jonathan_total_valence_monthly,
#     ])

merged_total_df = pd.read_csv("data/lineChartData/DfMonthlyAll.csv")

# # Convert index to datetime index
# merged_total_df['endTime'] = pd.to_datetime(merged_total_df['endTime'])
# # set the 'date' column as the index of the dataframe
# merged_total_df.set_index('endTime', inplace=True)

# mean_total_valence = merged_total_df.groupby(pd.Grouper(key='endTime', freq='M'))['valenceScore'].mean().reset_index()

# # # Insert featureID
# # mean_total_valence['feature'] = 'valenceScore'

# # Create a line chart using Altair with a title
# mean_total_valence_all = alt.Chart(mean_total_valence, height=200).mark_line(color='blue').encode(
#     x='endTime:N',
#     y='valenceScore:Q',
#     size=alt.value(3)
# ).properties(
#     title='Group total valence score mean'  # Add a title to the chart
# )

# mean_total_valence_danceability_all = mean_total_valence_all 


