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

# Create the strip plot using the filtered DataFrame
scatter_plot_valence_danceability_all = alt.Chart(df_genres_clean_10).mark_circle(size=30, color="#6f82ac").encode(
    y=alt.Y("danceability:Q", axis=alt.Axis(title="Danceability")),
    x=alt.X("valenceScore:Q", axis=alt.Axis(title="Valence Score")),
    tooltip=['trackName:N', "artistName:N", 'artistGenres:N','valenceScore:Q', 'danceability:Q', ],
    # color=alt.Color("valenceScore:Q", legend=None, scale=alt.Scale(scheme='greys'))
).properties(width=800, height=800)



