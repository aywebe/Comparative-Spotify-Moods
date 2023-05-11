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


# RADIAL CHART
# SHOWS EACH PERSONS AVERAGE VALENCE SCORE

# Create a dictionary to store the data frames
dfs = {}

# Load data frames into dictionary
dfs['Anton'] = pd.read_csv("data/mergedStreaming/AntonMergedStreamingClean.csv")
dfs['Freyja'] = pd.read_csv("data/mergedStreaming/FreyjaMergedStreamingClean.csv")
dfs['Laura'] = pd.read_csv("data/mergedStreaming/LauraMergedStreamingClean.csv")
dfs['Emil'] = pd.read_csv("data/mergedStreaming/EmilMergedStreamingClean.csv")


# Calculate the average valenceScore
values = [dfs['Anton']['valenceScore'].sum()/len(dfs['Anton']),
          dfs['Freyja']['valenceScore'].sum()/len(dfs['Freyja']),
          dfs['Laura']['valenceScore'].sum()/len(dfs['Laura']),
          dfs['Emil']['valenceScore'].sum()/len(dfs['Emil'])]

# Create a data frame with the values and labels
source = pd.DataFrame({
    'person': ['Anton', 'Freyja', 'Laura', 'Emil'],
    'values': values})

# Define the chart
base = alt.Chart(source).encode(
    alt.Theta("values:Q", stack=True),
    alt.Radius("values:Q", scale=alt.Scale(type="sqrt", zero=True, rangeMin=20)),
    color=alt.Color("values:Q", scale=alt.Scale(scheme="greys"))
)

# Create the chart with labels
c1 = base.mark_arc(innerRadius=20, stroke="#fff")
c2 = base.mark_text(radiusOffset=70).encode(text="person:N") 
c3 = base.mark_text(radiusOffset=40).encode(text="values:Q")

radial_chart_average_valence_all=(c1 + c2 + c3)
