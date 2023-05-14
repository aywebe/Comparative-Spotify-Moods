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
    y=alt.Y("artistGenres:N", axis=alt.Axis(title="Artist Genres"), sort=alt.EncodingSortField(field="count", order='descending')),    
    x=alt.X("valenceScore:Q", axis=alt.Axis(title="Valence Score")),
    href='url:N',
    tooltip=['trackName:N', "artistName:N", "artistGenres:N", "valenceScore:Q", "url:N"],
    # yOffset="jitter:Q",
    # color=alt.Color("valenceScore:Q", legend=None, scale=alt.Scale(scheme='purples'))
).transform_calculate(
    # Generate an url to let people search for the tracks
    url = alt.condition(
    alt.datum.artistName.notnull() & (alt.datum.artistName != ""),
    alt.expr("https://www.google.com/search?q=" + alt.datum.artistName.replace(' ', '+')),
    alt.value("")),
    # Generate Gaussian jitter with a Box-Muller transform
    jitter="sqrt(-2*log(random()))*sin(2*PI*random())"
).properties(width=800, height=800)

strip_plot_valence_artist_genres_all