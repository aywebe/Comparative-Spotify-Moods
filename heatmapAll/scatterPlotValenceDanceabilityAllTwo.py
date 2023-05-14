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

import pandas as pd

# Load the dataset from the csv file
df_genres_clean_2 = pd.read_csv("data/mergedStreaming/GenresMergedStreaming.csv")

# Remove "No genre information available"
df_genres_clean = df_genres_clean_2[df_genres_clean_2['artistGenres'] != 'No genre information available']

# Count the occurrences of each genre and get the top 10 most common genres
top_genres = df_genres_clean['artistGenres'].value_counts().nlargest(10).index.tolist()

# Filter the DataFrame to only include rows with one of the top 10 genres
df_genres_clean_10 = df_genres_clean[df_genres_clean['artistGenres'].isin(top_genres)]

source = df_genres_clean_10

zoom = alt.selection_interval(encodings=["x", "y"])

minimap = (
    alt.Chart(source)
    .mark_circle()
    .add_selection(zoom)
    .encode(
        x=alt.X("valenceScore:Q", axis=alt.Axis(title="Valence Score")),
        y=alt.Y("danceability:Q", axis=alt.Axis(title="Danceability")),
        color=alt.condition(zoom, alt.value("#6f82ac"), alt.value("lightgray")),
    )
    .properties(
        width=200,
        height=200,
        title="Minimap - click and drag to zoom",
    )
)

detail = (
    alt.Chart(source)
    .mark_circle(color="#6f82ac")
    .encode(
        x=alt.X(
            "valenceScore:Q", 
            scale=alt.Scale(domain={"selection": zoom.name, "encoding": "x"}),
            axis=alt.Axis(title="Valence Score")
        ),
        y=alt.Y(
            "danceability:Q",
            scale=alt.Scale(domain={"selection": zoom.name, "encoding": "y"}),
            axis=alt.Axis(title="Danceability")
        ),
        color=alt.Color(legend=None),
        tooltip=["trackName", "artistName", "valenceScore", "danceability"],
    )
    .properties(width=550, height=400)
)

scatter_plot_valence_danceability_all = (detail & minimap)



