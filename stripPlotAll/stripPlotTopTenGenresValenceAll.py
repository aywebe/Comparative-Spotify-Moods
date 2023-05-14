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

# Load dataframe

df_genres_clean = pd.read_csv("data/mergedStreaming/GenresMergedStreaming.csv")

# Filter out "No genre information available" genre
df_genres_clean = df_genres_clean[df_genres_clean['artistGenres'] != 'No genre information available']

# Count the occurrences of each genre and get the top 40 most common genres
top_genres = df_genres_clean['artistGenres'].value_counts().nlargest(10).index.tolist()

# Filter the DataFrame to only include rows with one of the top 40 genres
df_genres_clean_40 = df_genres_clean[df_genres_clean['artistGenres'].isin(top_genres)]

# Create the strip plot using the filtered DataFrame
strip_plot_valence_artist_genres_all = alt.Chart(df_genres_clean_40).mark_circle(size=30, color="#5c3a94" , opacity=1.0).encode(
    y=alt.Y(
        "jitter:Q",
        title=None,
        axis=alt.Axis(values=[0], ticks=True, grid=False, labels=False), 
        scale=alt.Scale(),
        # sort=alt.EncodingSortField(field="count", order='descending')
    ),    
    x=alt.X("valenceScore:Q", scale=alt.Scale(domain=(0,1)),
        color=alt.Color("valenceScore:Q", legend=None),
        row=alt.Row(
            "artistGenres:N",
            # header=alt.Header(
            #     labelAngle=0,
            #     labelFontSize=16,
            #     titleOrient='top',
            #     labelOrient='lef',
            #     labelAlign='left',
            # )
        ),
    ),
).transform_calculate(
    jitter="sqrt(-2*log(random()))*cos(2*PI*random())"
).properties(width=800, height=800)

strip_plot_valence_artist_genres_all