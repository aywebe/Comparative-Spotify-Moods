# DATA VIZ APP

# LIBRARIES
import streamlit as st
import pandas as pd
import numpy as np
import time 
import requests
import csv
import altair as alt
import numpy as np
from datetime import datetime
from PIL import Image

# DISABLES MAX ROWS FOR ALTAIR
alt.data_transformers.disable_max_rows()

# PAGE CONFIGURATION
st.set_page_config(
    page_title='Comparative Moods',
    layout="wide",
    # initial_sidebar_state="expanded",
)

# Link to your CSS file
st.markdown(
    """
    <style>
    body {
    font-family: 'Times New Roman', Times, serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# IMPORT CHART FROM PYTHON PATHS ALL
from radialChartAll.radialChartAverageValenceAll import radial_chart_average_valence_all
from stripPlotAll.stripPlotTopTenGenresValenceAll import strip_plot_valence_artist_genres_all
from stripPlotAll.stripPlotTopTenGenresDanceabilityAll import strip_plot_danceability_artist_genres_all
from heatmapAll.heatmapValenceDanceabilityAll import heatmap_valence_danceability_all
from heatmapAll.scatterPlotValenceDanceabilityAllTwo import scatter_plot_valence_danceability_all 
from radialChartAll.radialChartCountSongsAll import radial_chart_songs_count_hour_all
from radialChartAll.radialChartAverageValenceHourAll import radial_chart_valence_average_all
from radialChartAll.radialChartAverageDanceabilityAll import hourly_danceability_all
from linechartAll.lineChartAll import line_chart_all

# IMPORT CHART FROM PYTHON PATHS INDIVIDUAL

# ANTON
from radialChartIndividual.radialChartCountSongsAnton import radial_chart_songs_count_hour_anton
from radialChartIndividual.radialChartAverageValenceAnton import radial_chart_average_valence_anton
from radialChartIndividual.radialChartDanceabilityAnton import radial_chart_hourly_danceability_anton

# FREYJA
from radialChartIndividual.radialChartCountSongsFreyja import radial_chart_songs_count_hour_freyja
from radialChartIndividual.radialChartAverageValenceFreyja import radial_chart_average_valence_freyja
from radialChartIndividual.radialChartDanceabilityFreyja import radial_chart_hourly_danceability_freyja

# LAURA
from radialChartIndividual.radialChartCountSongsLaura import radial_chart_songs_count_hour_laura
from radialChartIndividual.radialChartAverageValenceLaura import radial_chart_average_valence_laura
from radialChartIndividual.radialChartDanceabilityLaura import radial_chart_hourly_danceability_laura

# EMIL
from radialChartIndividual.radialChartCountSongsEmil import radial_chart_songs_count_hour_emil
from radialChartIndividual.radialChartAverageValenceEmil import radial_chart_average_valence_emil
from radialChartIndividual.radialChartDanceabilityEmil import radial_chart_hourly_danceability_emil

# TITLE
st.title('Comparitive Moods Visualized with Spotify Data')
st.subheader('**Working with Valence Score and Danceability as variables for learning about our listening habits**')

# Load ITU Logo
itu_logo_img = Image.open("images/ITU_logo_CPH_UK.jpg")
# Display ITU Logo
st.image(itu_logo_img, width=200)
st.write('*Made by Anton Bentzon, Emil Engel, Freyja Viskum, Jonathan Wad Høgsbro, and Laura Amalie Augustinus*')
st.write("*MSC Digital Design and Interactive Technologies*")

st.write("**How does Spotify define valence?**")
st.write("""
         Spotify describes valence as a measure of the musical positivity conveyed by a track. It is represented 
         as a numerical value between 0.0 and 1.0, with higher values indicating a more positive or happy mood, 
         and lower values indicating a more negative or sad mood. \n Spotify calculates valence scores based on a 
         combination of musical features, such as tempo, rhythm, and harmony, as well as lyrics and other contextual 
         information. Valence scores are used by Spotify's recommendation algorithms to suggest songs that match a 
         user's mood or preferences.
         """)
st.write("**How does Spotify define danceability?**")
st.write("""
         Spotify describes danceability as a measure of how suitable a track is for dancing based on its tempo, rhythm 
         stability, beat strength, and overall regularity. It is represented as a numerical value between 0.0 and 1.0, 
         with higher values indicating that a track is more danceable. \n Danceability is calculated by analyzing various 
         musical features, such as the track's BPM (beats per minute), the regularity of the rhythm, and the presence of a 
         strong and consistent beat. Other factors, such as the track's time signature and the presence of vocals, can also 
         affect the danceability score. \n Spotify uses danceability scores as part of its recommendation system to suggest 
         songs that are suitable for dancing or to create playlists tailored to users' workout routines or dance parties.
         """
         )

# SIDEBAR
# with st.sidebar:
# 	st.write("Sidebar Hello")

############### ALL ###################

# LINE CHART ALL
st.subheader("1-Year Valence Score for All Group Members")
st.altair_chart(line_chart_all, use_container_width=True)
st.write("""*LINE CHART: The line chart displays the valence score for different users 
        over a period of 12 months. \n There are a few anomalies in the valence 
        score data that stand out. Laura has a significant drop in 
        valence score towards the end of the year, with the lowest score in 
        December. Freyja has an unusually low valence score in 
        January. Additionally, Anton has a significantly higher valence score in 
        June than in other months. These anomalies may indicate changes in music 
        preferences or external factors affecting the users' moods.*
        """)

st.subheader("24-Hour Valence Score and Danceability for All Group Members")
# COLUMNS STYLING
col1, col2, col3 = st.columns(3, gap="large")
with col1:
    # TOTAL COUNT OF SONGS HOURLY FOR ALL
    st.write("**Song Count by Hour for All**")
    st.altair_chart(radial_chart_songs_count_hour_all, use_container_width=True)
    st.write("""*RADIAL CHART: 
            The dataset shows a discernible pattern of higher song activity during daytime hours and lower 
            activity during nighttime hours, with an anomaly of a sharp drop in the number of songs played 
            during 4 am*""")

with col2:
    # 24-HOUR RADIAL VALENCE SCORE CHART FOR ALL
    st.write("**Valence Score by Hour for All**")
    st.altair_chart(radial_chart_valence_average_all, use_container_width=True)
    st.write("*RADIAL CHART: This data shows...*")

with col3:
    # 24-HOUR RADIAL DANCEABILITY CHART FOR ALL
    st.write("**Danceability Score by Hour for All**")
    st.altair_chart(hourly_danceability_all, use_container_width=True)
    st.write("*RADIAL CHART: This data shows...*")

############### INDIVIDUAL DATA CHARTS ###################

st.write("To conclude this...")

# MULTISELECT TOOL 
options = st.multiselect(
    'Choose to View Individual Data',
    ['Anton', 'Freyja', 'Laura', 'Emil', 'Jonathan'],
    ['Anton'])

######## ANTON ##############

col4, col5, col6 = st.columns(3)
if "Anton" in options:
    with col4:
        # 24-HOUR RADIAL DANCEABILITY CHART FOR ANTON
        st.write("**Count of Songs by Hour for Anton**")
        st.altair_chart(radial_chart_songs_count_hour_anton, use_container_width=True)
        st.write("*RADIAL CHART: This chart shows...*")

    with col5:
        # 24-HOUR RADIAL VALENCE CHART FOR ANTON
        st.write("**Valence Score by Hour for Anton**")
        st.altair_chart(radial_chart_average_valence_anton, use_container_width=True)
        st.write("*RADIAL CHART: This chart shows...*")

    with col6:
        # 24-HOUR RADIAL DANCEABILITY CHART FOR ANTON
        st.write("**Danceability Score for Hour for Anton**")
        st.altair_chart(radial_chart_hourly_danceability_anton, use_container_width=True)
        st.write("*RADIAL CHART: This chart shows...*")

######### FREYJA ###########

col7, col8, col9 = st.columns(3)
if "Freyja" in options:
    with col7:          
        # 24-HOUR RADIAL DANCEABILITY CHART FOR FREYJA
        st.write("**Songs by Hour for Freyja**")
        st.altair_chart(radial_chart_songs_count_hour_freyja, use_container_width=True)
        st.write("*RADIAL CHART: This chart shows...*")

    with col8:
        # 24-HOUR RADIAL VALENCE CHART FOR FREYJA
        st.write("**Valence Score for Hour for Freyja**")
        st.altair_chart(radial_chart_average_valence_freyja, use_container_width=True)
        st.write("*RADIAL CHART: This data shows...*")

    with col9:
        # 24-HOUR RADIAL DANCEABILITY CHART FOR FREYJA
        st.write("**Danceability Score for Hour for Freyja**")
        st.altair_chart(radial_chart_hourly_danceability_freyja, use_container_width=True)
        st.write("*RADIAL CHART: This data shows...*")


######### LAURA ###########

col10, col11, col12 = st.columns(3)
if "Laura" in options:
    with col10:
        # 24-HOUR RADIAL DANCEABILITY CHART FOR LAURA
        st.write("**24-Hour Total Count of Songs by Hour for Laura**")
        st.altair_chart(radial_chart_songs_count_hour_laura, use_container_width=True)
        st.write("*RADIAL CHART: This data shows...*")

    with col11:
        # 24-HOUR RADIAL VALENCE CHART FOR LAURA
        st.write("**24-Hour Valence Score for Hour for Laura**")
        st.altair_chart(radial_chart_average_valence_laura, use_container_width=True)
        st.write("*RADIAL CHART: This data shows...*")


    with col12:
        # 24-HOUR RADIAL DANCEABILITY CHART FOR Laura
        st.write("*24-Hour Danceability Score for Hour for Laura*")
        st.altair_chart(radial_chart_hourly_danceability_laura, use_container_width=True)
        st.write("*RADIAL CHART: This data shows...*")


######### EMIL ###########

col13, col14, col15 = st.columns(3)
if "Emil" in options: 
    with col13:
        # 24-HOUR RADIAL DANCEABILITY CHART FOR EMIL
        st.write("**24-Hour Total Count of Songs by Hour for Emil**")
        st.altair_chart(radial_chart_songs_count_hour_emil, use_container_width=True)
        st.write("*RADIAL CHART: This data shows...*")

    with col14: 
        # 24-HOUR RADIAL VALENCE CHART FOR EMIL
        st.write("**24-Hour Valence Score for Hour for Emil**")
        st.altair_chart(radial_chart_average_valence_emil, use_container_width=True)
        st.write("*RADIAL CHART: This data shows...*")


    with col15:
        # 24-HOUR RADIAL DANCEABILITY CHART FOR EMIL
        st.write("**24-Hour Danceability Score for Hour for Emil**")
        st.altair_chart(radial_chart_hourly_danceability_emil, use_container_width=True)
        st.write("*RADIAL CHART: This data shows...*")


############### CHARTS THAT ARE WORKING ON ALL OF OUR DATA ###################

col16, col17 = st.columns(2, gap="large")
with col16:
    # HEATMAP
    st.subheader("Interconectedness of Valence Score and Danceability")
    st.altair_chart(heatmap_valence_danceability_all, use_container_width=True)
    st.write("*HEATMAP: This data shows...*")


with col17:
    # SCATTERPLOT / HEATMAP VERS 2
    st.subheader("Track Interconectedness of Valence Score and Danceability")
    st.altair_chart(scatter_plot_valence_danceability_all, use_container_width=True)
    st.write("*SCATTERPLOT: This data shows...*")


col18, col19 = st.columns(2, gap="Large")
with col18:
    # STRIP PLOT TOP 10 ARTIST GENRES VALENCE
    st.subheader("Valence Score by Top 10 Artist Genres")
    st.altair_chart(strip_plot_valence_artist_genres_all, use_container_width=True)
    st.write("*STRIP PLOT: This data shows...*")

with col19:
    # STRIP PLOT TOP 10 ARTIST GENRES DANCEABILITY
    st.subheader("Danceability by Top 10 Artist Genres")
    st.altair_chart(strip_plot_danceability_artist_genres_all, use_container_width=True)
    st.write("*STRIP PLOT: This data shows...*")






