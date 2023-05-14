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


# RADIAL CHART SHOWING THE NUMBER OF SONGS PLAYED IN EACH HOUR

# Load the file 
df_hourly_track_count_laura = pd.read_csv("data/hourlyStreamingIndividual/dfTrackCountLaura.csv")

# Extract values from df_hourly_valence_avereage
values = df_hourly_track_count_laura['trackCount'].tolist()

# Create a data frame with the values and index values
source = pd.DataFrame({'values': values, 'hour': range(0, len(values))})

# Define the chart
base = alt.Chart(source).encode(
    alt.Theta("hour:N", stack=True),
    alt.Radius("values:Q", scale=alt.Scale(type="sqrt", zero=True, rangeMin=20)),
    color=alt.Color("values:Q", legend=alt.Legend(title="Count of Songs"), scale=alt.Scale(scheme="greys"))
)

# Create the chart with index values as labels
c1 = base.mark_arc(innerRadius=20, stroke="#fff")
c2 = base.mark_text(radiusOffset=10).encode(text=alt.Text('hour:N'), angle=alt.value(0))

radial_chart_songs_count_hour_laura = (c1 + c2)
