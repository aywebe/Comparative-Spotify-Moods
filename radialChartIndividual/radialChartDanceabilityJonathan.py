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

# HOURLY DANCEABILITY CHART FOR ALL

df_hourly_danceability_average_jonathan = pd.read_csv("data/hourlyStreamingIndividual/dfHourlyDanceabilityAverageJonathan.csv")

# Extract values from df_hourly_valence_non_average
values = df_hourly_danceability_average_jonathan['averageDanceabilityScore'].tolist()

# Create a data frame with the values and index values
source = pd.DataFrame({'values': values, 'hour': range(0, len(values))})

# Define the chart
base = alt.Chart(source).encode(
    alt.Theta("hour:N", stack=True),
    alt.Radius("values:Q", scale=alt.Scale(type="sqrt", zero=True, rangeMin=20)),
    color=alt.Color("values:Q", legend=alt.Legend(title="Danceability"), scale=alt.Scale(scheme="tealblues"))
)

# Create the chart with index values as labels
c1 = base.mark_arc(innerRadius=20, stroke="#fff")
c2 = base.mark_text(radiusOffset=10).encode(text=alt.Text('hour:N'), angle=alt.value(0))

radial_chart_hourly_danceability_jonathan = (c1 + c2).properties(width=400, height=400)