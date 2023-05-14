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

df_genres_clean_2 = pd.read_csv("data/mergedStreaming/GenresMergedStreaming.csv")

# Remove "No genre information available"
df_genres_clean = df_genres_clean_2[df_genres_clean_2['artistGenres'] != 'No genre information available']

# Count the occurrences of each genre and get the top 40 most common genres
top_genres = df_genres_clean_2['artistGenres'].value_counts().nlargest(10).index.tolist()

# Filter the DataFrame to only include rows with one of the top 40 genres
df_genres_clean_40 = df_genres_clean_2[df_genres_clean_2['artistGenres'].isin(top_genres)]

# Create the strip plot using the filtered DataFrame
scatter_plot_valence_danceability_all = alt.Chart(df_genres_clean_40).mark_circle(size=30, color="#6f82ac").encode(
    y=alt.Y("danceability:Q", axis=alt.Axis(title="Danceability")),
    x=alt.X("valenceScore:Q", axis=alt.Axis(title="Valence Score")),
    tooltip=['trackName:N', "artistName:N", 'artistGenres:N','valenceScore:Q', 'danceability:Q', ],
    # color=alt.Color("valenceScore:Q", legend=None, scale=alt.Scale(scheme='greys'))
).properties(width=800, height=800)

zoom = alt.selection_interval(encodings=["x", "y"])

# Create the minimap using the entire dataset
minimap = (
    alt.Chart(df_genres_clean_2)
    .mark_circle()
    .add_selection(zoom)
    .encode(
        x="valenceScore:Q",
        y="danceability:Q",
        color=alt.condition(zoom, "Valence Score", alt.value("lightgray")),
    )
    .properties(
        width=200,
        height=200,
        title="Minimap -- click and drag to zoom in the detail view",
    )
)

# Combine the scatter plot and the minimap
scatter_plot_valence_danceability_all = scatter_plot_valence_danceability_all | minimap
