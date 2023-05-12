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

# 2D HISTOGRAM HEATMAP
# CONVEYS THE LINK BETWEEN VALENCE SCORE AND DANCEABILITY
# HOW IS VALENCE SCORE DEFINED BY: HAPPY, SAD, AND SUCH
# HOW IS DANCEABILITY DEFINED BY: TEMPO, etc...
# CORRELATION ANALYSIS

# Load and merge data
df = pd.read_csv("data/mergedStreaming/AllMergedStreaming.csv")

# Drop unnecessary columns and rename columns
df = df.drop(['msPlayed', 'minutesPlayed', 'trackName'], axis=1)
df = df.rename(columns={'Danceability': 'danceability', 'Valence': 'valenceScore'})

# Group data by danceability and valence score
df_grouped = df.groupby(['danceability', 'valenceScore']).count()

# Reset index
df_grouped = df_grouped.reset_index()

# Define chart
heatmap_valence_danceability_all = alt.Chart(df_grouped).mark_rect().encode(
    alt.X('valenceScore:Q', bin=True),
    alt.Y('danceability:Q', bin=True),
    alt.Color('count():Q', scale=alt.Scale(scheme='hello'))
).properties(
    width=800,
    height=400,
)


heatmap_valence_danceability_all