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

# Count the occurrences of each genre and get the top 40 most common genres
top_genres = df_genres_clean['artistGenres'].value_counts().nlargest(10).index.tolist()

# Filter the DataFrame to only include rows with one of the top 40 genres
df_genres_clean_40 = df_genres_clean[df_genres_clean['artistGenres'].isin(top_genres)]

# Create the strip plot using the filtered DataFrame
strip_plot_valence_artist_genres_all = alt.Chart(df_genres_clean_40).mark_circle(size=8).encode(
    y=alt.Y("artistGenres:N", axis=alt.Axis(title="Artist Genres")),
    x=alt.X("valenceScore:Q", axis=alt.Axis(title="Valence Score")),
    href='url:N',
    tooltip=['trackName:N', "artistName:N", "valenceScore:Q", "danceability:Q"],
    yOffset="jitter:Q",
    color=alt.Color("valenceScore:Q", legend=None, scale=alt.Scale(scheme='plasma'))
).transform_calculate(
    # Generate an url to let people search for the tracks
    url='https://www.google.com/search?q=' + alt.datum.Name,
    # Generate Gaussian jitter with a Box-Muller transform
    jitter="sqrt(-2*log(random()))*cos(2*PI*random())"
).properties(width=800, height=800)

strip_plot_valence_artist_genres_all