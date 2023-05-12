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

# ANTON
# 24-HOUR RADIAL CHART 
# SHOWS THE AVERAGE VALENCE SCORE FOR ALL BASED ON HOUR OF DAY
# SHOWS A BIAS = HOUR 5 + 6 IS NOT HOURS THAT HAVE A LOT OF PLAYS

df_hourly_valence_average_freyja = pd.read_csv("data/hourlyStreamingIndividual/dfHourlyValenceAverageFreyja.csv")

# Extract values from df_hourly_valence_avereage
values = df_hourly_valence_average_freyja['averageValenceScore'].tolist()

# Create a data frame with the values and index values
source = pd.DataFrame({'values': values, 'hour': range(0, len(values))})

# Define the chart
base = alt.Chart(source).encode(
    alt.Theta("hour:N", stack=True),
    alt.Radius("values:Q", scale=alt.Scale(type="sqrt", zero=True, rangeMin=20)),
    color=alt.Color("values:Q", scale=alt.Scale(scheme="purples"))
)

# Create the chart with index values as labels
c1 = base.mark_arc(innerRadius=20, stroke="#fff")
c2 = base.mark_text(radiusOffset=10).encode(text=alt.Text('hour:N'), angle=alt.value(0))

radial_chart_average_valence_freyja = (c1 + c2).properties(width=400, height=400)