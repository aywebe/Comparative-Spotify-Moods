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

zoom = alt.selection_interval(encodings=["x", "y"])

# Create the minimap using the entire dataset
minimap = (
    alt.Chart(df_genres_clean_2)
    .mark_circle()
    .add_selection(zoom)
    .encode(
        x="valenceScore:Q",
        y="danceability:Q",
        color=alt.condition(zoom, "weather", alt.value("lightgray")),
    )
    .properties(
        width=200,
        height=200,
        title="Minimap -- click and drag to zoom in the detail view",
    )
)

# Create the strip plot using the filtered DataFrame
scatter_plot_valence_danceability_all = (
    alt.Chart(df_genres_clean_40)
    .mark_circle(size=30)
    .encode(
        x=alt.X(
            "valenceScore:Q", scale=alt.Scale(domain={"selection": zoom.name, "encoding": "x"})
        ),
        y=alt.Y(
            "danceability:Q",
            scale=alt.Scale(domain={"selection": zoom.name, "encoding": "y"})
        ),
        color="#6f82ac",
    )
    .properties(width=800, height=800)
)

# Combine the scatter plot and the minimap
scatter_plot_valence_danceability_all = scatter_plot_valence_danceability_all | minimap

