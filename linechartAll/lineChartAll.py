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


# READING FILES FOR MERGED STREAMING
source = pd.read_csv("data/lineChartData/DfMonthlyAll.csv")
total_valence_df = pd.read_csv("data/lineChartData/DfMonthlyMeanAll.csv")

click = alt.selection_single(encodings=["color"])

base = alt.Chart(source).encode(
    x='endTime:T',
    y='valenceScore:Q',
    color='userID:N'
)

points = base.mark_circle().encode(
    opacity=alt.value(1)
).add_selection(
    click
).properties(
    width=600
)

lines = base.mark_line().encode(
    size=alt.condition(click, alt.value(3), alt.value(0.5))
)

bar = alt.Chart(total_valence_df).mark_bar().encode(
    x="valenceScore",
    y="userID:N",
    color=alt.condition(click, "userID:N",alt.value("grey")),
    tooltip=['valenceScore']  # Add tooltip encoding to display the score
).add_selection(
    click
).properties(height=200)

line_chart_all = bar | points + lines

