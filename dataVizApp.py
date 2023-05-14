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

# CSS
streamlit_style = """
			<style>
			@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap');

			html, body, [class*="css"]  {
			font-family: 'Roboto', sans-serif;
			}
            .picture-font {
            font-size:12px
            }
			</style>
			"""
st.markdown(streamlit_style, unsafe_allow_html=True)

# IMPORT CHART FROM PYTHON PATHS ALL
# from radialChartAll.radialChartAverageValenceAll import radial_chart_average_valence_all
from stripPlotAll.stripPlotTopTenGenresValenceAll import strip_plot_valence_artist_genres_all
from stripPlotAll.stripPlotTopTenGenresDanceabilityAll import strip_plot_danceability_artist_genres_all
from heatmapAll.heatmapValenceDanceabilityAll import heatmap_valence_danceability_all
from heatmapAll.scatterPlotValenceDanceabilityAllTwo import scatter_plot_valence_danceability_all 
from radialChartAll.radialChartCountSongsAll import radial_chart_songs_count_hour_all
from radialChartAll.radialChartAverageValenceHourAll import radial_chart_valence_average_all
from radialChartAll.radialChartAverageDanceabilityAll import hourly_danceability_all
from linechartAll.lineChartAll import line_chart_all
# from linechartAll.lineChartMeanAll import mean_total_valence_danceability_all

# IMPORT CHART FROM PYTHON PATHS INDIVIDUAL

# ANTON
from radialChartIndividual.radialChartCountSongsAnton import radial_chart_songs_count_hour_anton
from radialChartIndividual.radialChartAverageValenceAnton import radial_chart_average_valence_anton
from radialChartIndividual.radialChartDanceabilityAnton import radial_chart_hourly_danceability_anton
# from radarCharts.radarChartAnton import fig

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

# JONATHAN
from radialChartIndividual.radialChartCountSongsJonathan import radial_chart_songs_count_hour_jonathan
from radialChartIndividual.radialChartAverageValenceJonathan import radial_chart_average_valence_jonathan
from radialChartIndividual.radialChartDanceabilityJonathan import radial_chart_hourly_danceability_jonathan


####################################################################################################

# TITLE
st.title('Comparitive Moods Visualized with Spotify Data')
st.subheader('**Working with Valence Score and Danceability as variables for learning about our listening habits**')


st.write('Made by Anton Bentzon, Emil Engel, Freyja Viskum, Jonathan Wad Høgsbro, and Laura Amalie Augustinus')
st.write("MSC Digital Design and Interactive Technologies")
# Load ITU Logo
itu_logo_img = Image.open("images/ITU_logo_CPH_UK.jpg")
# Display ITU Logo
st.image(itu_logo_img, width=200)

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

############### ALL ###################

# LINE CHART ALL
st.subheader("1-Year Valence Score for All Group Members")
st.altair_chart(line_chart_all, use_container_width=True)
st.markdown("""<p class="picture-font">Line Chart: The line chart displays the valence score for different users 
            over a period of 12 months. There are a few anomalies in the valence \n score data that stands out.
            Laura has a significant drop in valence score towards the end of the year, with the lowest score in
            December. Freyja has an unusally low valence score in Januara. Aditionally, Anton has a significantly higher
            valence score in June than in other months.
            </p>""", unsafe_allow_html=True)

# LINE CHART MEAN ALL - DANCEABILITY + VALENCE

# st.subheader("1-Year Valence and Danceability Mean Score for All Group Members")
# st.altair_chart(mean_total_valence_danceability_all, use_container_width=True)
# st.markdown("""<p class="picture-font"> Line Chart Mean All: Awaiting text... 
#             </p>""", unsafe_allow_html=True)


st.subheader("24-Hour Valence Score and Danceability for All Group Members")
# COLUMNS STYLING
col1, col2, col3 = st.columns(3, gap="large")
with col1:
    # TOTAL COUNT OF SONGS HOURLY FOR ALL
    st.write("**Song Count by Hour for All**")
    st.altair_chart(radial_chart_songs_count_hour_all, use_container_width=True)
    st.markdown("""<p class="picture-font"> Radial Chart Song Count: The dataset shows a discernible pattern of higher 
                song activity
                during daytime hours and lower activity during nighttime hours, with an anomaly of a sharp drop
                in the number of songs played during 4 am
            </p>""", unsafe_allow_html=True)

with col2:
    # 24-HOUR RADIAL VALENCE SCORE CHART FOR ALL
    st.write("**Average Valence Score by Hour for All**")
    st.altair_chart(radial_chart_valence_average_all, use_container_width=True)
    st.markdown("""<p class="picture-font"> Radial Chart Valence Score: Anomalies include the lowest average 
                valence score at midnight and a relatively low score at 11 pm. Trends show a downward trend in valence 
                score from early morning to mid-afternoon, with a low point at 2 pm, and an upward trend from 2 pm to 
                6 am, with a peak at 6 am
            </p>""", unsafe_allow_html=True)

with col3:
    # 24-HOUR RADIAL DANCEABILITY CHART FOR ALL
    st.write("**Average Danceability Score by Hour for All**")
    st.altair_chart(hourly_danceability_all, use_container_width=True)
    st.markdown("""<p class="picture-font"> Radial Chart Danceability: This data suggests an increasing trend in 
                danceability scores from midnight to early afternoon, peaking at 5 pm, followed by a slight decrease 
                until 10 pm and a significant decrease until midnight. The highest energy dance music is played in the 
                afternoon and early evening, while late night and early morning tend to have lower energy music.
            </p>""", unsafe_allow_html=True)

############### INDIVIDUAL DATA CHARTS ###################

st.subheader("Comparative Individual 24-Hour Radial Charts")

# MULTISELECT TOOL 
options = st.multiselect(
    'Choose to View Individual Group Members Data Like Above',
    ['Anton', 'Freyja', 'Laura', 'Emil', 'Jonathan'])

######## ANTON ##############

col4, col5, col6 = st.columns(3, gap="large")
if "Anton" in options:
    with col4:
        # 24-HOUR RADIAL DANCEABILITY CHART FOR ANTON
        st.write("**Count of Songs by 24-Hours for Anton**")
        st.altair_chart(radial_chart_songs_count_hour_anton, use_container_width=True)
        st.markdown("""<p class="picture-font"> Radial Chart Count of Songs for Anton: The track count varies 
                    greatly from as low as 2 tracks during the 8th hour to as high as 141 tracks during the 
                    16th hour. There also seems to be a trend of higher track counts during the later hours 
                    of the day (from 16th to 19th hour) with a sudden drop at the 22nd hour.
            </p>""", unsafe_allow_html=True)


    with col5:
        # 24-HOUR RADIAL VALENCE CHART FOR ANTON
        st.write("**Average Valence Score by 24-Hours for Anton**")
        st.altair_chart(radial_chart_average_valence_anton, use_container_width=True)
        st.markdown("""<p class="picture-font"> Radial Chart Valence Score for Anton: This data suggests 
                    that the average valence score of music played in a certain period is relatively stable 
                    between 0.47 and 0.54, with the highest scores occurring in the late evening from 9 pm 
                    to midnight, peaking at 10 pm. There is a significant drop in valence score after 
                    midnight, with the lowest score occurring at 11 am. The valence scores seem to 
                    follow a bimodal distribution, with peaks in the late evening and early afternoon.
            </p>""", unsafe_allow_html=True)

    with col6:
        # 24-HOUR RADIAL DANCEABILITY CHART FOR ANTON
        st.write("**Average Danceability Score by 24-Hours for Anton**")
        st.altair_chart(radial_chart_hourly_danceability_anton, use_container_width=True)
        st.markdown("""<p class="picture-font"> Radial Chart Danceability for Anton: The scores range from 
                    0.59 to 0.829, with the highest score occurring at 8am and the lowest score at 9am. 
                    There is a slight dip in the early afternoon before the scores rise again in the late 
                    afternoon and early evening, peaking at 11pm. The data suggests that songs played during
                    morning hours tend to be more danceable than those played in the afternoon or evening.
            </p>""", unsafe_allow_html=True)

######### FREYJA ###########

col7, col8, col9 = st.columns(3, gap="large")
if "Freyja" in options:
    with col7:          
        # 24-HOUR RADIAL DANCEABILITY CHART FOR FREYJA
        st.write("**Songs by 24-Hours for Freyja**")
        st.altair_chart(radial_chart_songs_count_hour_freyja, use_container_width=True)
        st.markdown("""<p class="picture-font"> Radial Chart Count of Songs for Freyja: The number of tracks played ranges from
                    7 to 280, with the highest number of tracks played occurring at 13pm and the
                    lowest number of tracks played at 4am. There is a consistent increase in the
                    number of tracks played from the early morning to the late evening, peaking
                    between 12pm and 1pm and then again between 4pm and 6pm.    
            </p>""", unsafe_allow_html=True)

    with col8:
        # 24-HOUR RADIAL VALENCE CHART FOR FREYJA
        st.write("**Average Valence Score by 24-Hours for Freyja**")
        st.altair_chart(radial_chart_average_valence_freyja, use_container_width=True)
        st.markdown("""<p class="picture-font"> Radial Chart Valence Score for Freyja: 
                    The valence scores range from
                    0.07666956521739131 to 0.49439999999999995, with the highest score occurring at 5am and
                    the lowest score at 0am. There is a steady increase in valence scores from the early
                    morning to the late afternoon, peaking at 5am. Valence scores then begin to decrease
                    until reaching their lowest point at 0am. The data suggests that songs played in the early
                    morning tend to have a higher valence score than those played in the late evening or
                    early morning hours.
            </p>""", unsafe_allow_html=True)

    with col9:
        # 24-HOUR RADIAL DANCEABILITY CHART FOR FREYJA
        st.write("**Average Danceability Score by 24-Hours for Freyja**")
        st.altair_chart(radial_chart_hourly_danceability_freyja, use_container_width=True)
        st.markdown("""<p class="picture-font"> Radial Chart Danceability for Freyja: The danceability scores range from
                    0.152 to 0.626, with the highest score occurring at 5am and the lowest score at 3am.
                    There is a consistent increase in danceability scores from the early morning to the late
                    afternoon, with the highest scores occurring between 5pm and 7pm. The data suggests that
                    songs played in the late afternoon and early evening tend to be more danceable than those
                    played in the morning or late evening.
            </p>""", unsafe_allow_html=True)


######### LAURA ###########

col10, col11, col12 = st.columns(3, gap="large")
if "Laura" in options:
    with col10:
        # 24-HOUR RADIAL DANCEABILITY CHART FOR LAURA
        st.write("**Total Count of Songs by 24-Hours for Laura**")
        st.altair_chart(radial_chart_songs_count_hour_laura, use_container_width=True)
        st.markdown("""<p class="picture-font"> Radial Chart Count of Songs for Laura: The number of 
                    tracks played ranges from 1 to 523, with the highest number of tracks played occurring 
                    at 10am and the lowest number of tracks played at 2am and 23pm. There is a consistent 
                    increase in the number of tracks played from the early morning to the late evening, 
                    peaking between 9am and 11am and then again between 6pm and 7pm.
            </p>""", unsafe_allow_html=True)

    with col11:
        # 24-HOUR RADIAL VALENCE CHART FOR LAURA
        st.write("**Average Valence Score by 24-Hours for Laura**")
        st.altair_chart(radial_chart_average_valence_laura, use_container_width=True)
        st.markdown("""<p class="picture-font"> Radial Chart Valence Score for Laura: The valence scores 
                    range from 0.205 to 0.538, with the highest score occurring at 11pm and the lowest 
                    score at 2am. There is a slight increase in valence scores from the early morning to 
                    the late afternoon, with the highest scores occurring between 10pm and midnight. The 
                    data suggests that songs played in the late evening tend to have a higher valence score 
                    than those played in the early morning or late at night.
            </p>""", unsafe_allow_html=True)

    with col12:
        # 24-HOUR RADIAL DANCEABILITY CHART FOR Laura
        st.write("*Average Danceability Score by 24-Hours for Laura*")
        st.altair_chart(radial_chart_hourly_danceability_laura, use_container_width=True)
        st.markdown("""<p class="picture-font"> Radial Chart Danceability for Laura: The danceability 
                    scores range from 0.573 to 0.694, with the highest score occurring at 3am and the 
                    lowest score at 5am. There is a consistent increase in danceability scores from the 
                    early morning to the late afternoon, with the highest scores occurring between 11pm 
                    and midnight. The data suggests that songs played in the late evening and early morning 
                    tend to be more danceable than those played in the afternoon or late at night.
            </p>""", unsafe_allow_html=True)


######### EMIL ###########

col13, col14, col15 = st.columns(3, gap="large")
if "Emil" in options: 
    with col13:
        # 24-HOUR RADIAL DANCEABILITY CHART FOR EMIL
        st.write("**Total Count of Songs by 24-Hours for Emil**")
        st.altair_chart(radial_chart_songs_count_hour_emil, use_container_width=True)
        st.markdown("""<p class="picture-font"> Radial Chart Count of Songs for Emil: The chart 
                    indicates that the fewest tracks were played during the early morning hours, 
                    with the lowest count recorded at hour 4. The track count then gradually 
                    increased throughout the day, with the highest count recorded during the late 
                    afternoon and early evening hours from 6 PM to 9 PM. The count then decreases 
                    from 9 PM to 4 AM
            </p>""", unsafe_allow_html=True)

    with col14: 
        # 24-HOUR RADIAL VALENCE CHART FOR EMIL
        st.write("**Average Valence Score by 24-Hours for Emil**")
        st.altair_chart(radial_chart_average_valence_emil, use_container_width=True)
        st.markdown("""<p class="picture-font"> Radial Chart Valence Score for Emil: The chart indicates 
                    that the highest valence scores are recorded during the late afternoon and early 
                    evening hours, with a peak at hour 21. The lowest valence scores are recorded during 
                    the early morning hours.
            </p>""", unsafe_allow_html=True)


    with col15:
        # 24-HOUR RADIAL DANCEABILITY CHART FOR EMIL
        st.write("**Average Danceability Score by 24-Hours for Emil**")
        st.altair_chart(radial_chart_hourly_danceability_emil, use_container_width=True)
        st.markdown("""<p class="picture-font"> Radial Chart Danceability for Emil: The danceability 
                    score is relatively high during the early morning hours from 3 AM to 7 AM. However, 
                    there is a slight dip in danceability from 7 AM to 10 AM, with a low at hour 10. 
                    The score then gradually increases from 10 AM to 8 PM, with the highest score 
                    recorded at hour 21. The danceability score then decreases from 8 PM to 3 AM, with 
                    the lowest score recorded at hour 2
            </p>""", unsafe_allow_html=True)

######### JONATHAN ###########

col16, col17, col18 = st.columns(3, gap="large")
if "Jonathan" in options: 
    with col16:
        # 24-HOUR RADIAL DANCEABILITY CHART FOR EMIL
        st.write("**Total Count of Songs by 24-Hours for Jonathan**")
        st.altair_chart(radial_chart_songs_count_hour_jonathan, use_container_width=True)
        st.markdown("""<p class="picture-font"> Radial Chart Count of Songs for Emil: This data shows 
                    the number of tracks played at different hours of the day, presented as a radial 
                    chart. The chart shows that the number of tracks played is lowest during the early
                    morning hours from 0 to 2. There is a gradual increase in the number of tracks 
                    played from 2 to 7, with a steep increase from 7 to 10. The highest number of 
                    tracks played is recorded at hour 17, after which the number decreases. The lowest 
                    number of tracks played is recorded at hour 23.
            </p>""", unsafe_allow_html=True)

    with col17: 
        # 24-HOUR RADIAL VALENCE CHART FOR EMIL
        st.write("**Average Valence Score by 24-Hours for Jonathan**")
        st.altair_chart(radial_chart_average_valence_jonathan, use_container_width=True)
        st.markdown("""<p class="picture-font"> Radial Chart Valence Score for Jonathan: This data 
                    shows the average valence score of music tracks across the day, visualized on a 
                    radial chart. The chart shows that valence scores are relatively low during the 
                    early morning hours from 0 to 2, with a slight increase from 2 to 6. There is a 
                    gradual increase in valence scores from 6 to 17, with the highest score recorded 
                    at hour 17. Scores then decrease from 17 to 23, with the lowest score recorded at 
                    hour 2.
            </p>""", unsafe_allow_html=True)

    with col18:
        # 24-HOUR RADIAL DANCEABILITY CHART FOR EMIL
        st.write("**Average Danceability Score by 24-Hours for Jonathan**")
        st.altair_chart(radial_chart_hourly_danceability_jonathan, use_container_width=True)
        st.markdown("""<p class="picture-font"> Radial Chart Danceability for Jonathan: The chart shows 
                    that the danceability score is relatively low during the early morning hours, from 
                    0 to 3. However, there is a gradual increase in danceability from 3 to 8, with a peak 
                    at hour 15. The danceability score remains relatively high from 15 to 19, with a 
                    slight dip at hour 18. The score then decreases from 19 to 23, with the lowest score 
                    recorded at hour 3.
            </p>""", unsafe_allow_html=True)

############### CHARTS THAT ARE WORKING ON ALL OF OUR DATA ###################


#with col17:
    # HEATMAP
st.subheader("Interconectedness of Valence Score and Danceability")
st.altair_chart(heatmap_valence_danceability_all, use_container_width=False)
st.markdown("""<p class="picture-font"> Heatmap of Valence vs. Danceability: This 2D histogram heatmap 
                illustrates the 
                correlation between the valence score and danceability of songs in a given dataset.
            The central area of the chart exhibits a dense cluster of songs with moderate valence scores 
            and danceability ratings. Showing a high concentration of songs with similar valence and 
            danceability ratings in the middle range of the two variables. 
            </p>""", unsafe_allow_html=True)

# col16, col17 = st.columns(2, gap="large")
# with col16:
    # SCATTERPLOT / HEATMAP VERS 2
st.subheader("Track Interconectedness of Valence Score and Danceability by Top 10 Artist Genres")
st.altair_chart(scatter_plot_valence_danceability_all, use_container_width=True)
st.markdown("""<p class="picture-font"> Scatter Plot Valence vs Danceability: The scatter plot represents 
                the relationship between the valence score and danceability of songs across the top 10 most 
                common genres in the dataset. The y-axis shows the danceability rating, while the x-axis 
                shows the valence score. Each circle represents a song, and its color indicates the valence 
                score of the song. The tooltip shows additional information about each song, such as 
                its name, artist, genre, valence score, and danceability rating. By examining the scatter 
                plot, we can see how the valence score and danceability of songs tend to vary across 
                different genres. Some genres, such as pop and rock, have a wider range of valence scores 
                and danceability ratings, while others, such as hip-hop and R&B, tend to have higher 
                danceability ratings but lower valence scores
            </p>""", unsafe_allow_html=True)

col18, col19 = st.columns(2, gap="large")
with col18:
    # STRIP PLOT TOP 10 ARTIST GENRES VALENCE
    st.subheader("Valence Score by Top 10 Artist Genres")
    st.altair_chart(strip_plot_valence_artist_genres_all, use_container_width=True)
    st.markdown("""<p class="picture-font"> Valence Score by top 10 Artist Genres: This strip plot shows 
                the valence score for the top 10 most common genres of artists. The plot is created using 
                data from a merged dataset of streaming information on various songs and artists. Each 
                circle represents a song, and the position of the circle along the x-axis indicates the 
                valence score of the song. The y-axis shows the artist genre. Hover over a circle to see 
                the song name, artist name, artist genre, valence score, and danceability score. The color 
                of the circles indicates the valence score of the song, with warmer colors representing 
                higher scores. The chart helps to visualize the distribution of valence scores across 
                different genres of music.
            </p>""", unsafe_allow_html=True)
with col19:
    # STRIP PLOT TOP 10 ARTIST GENRES DANCEABILITY
    st.subheader("Danceability by Top 10 Artist Genres")
    st.altair_chart(strip_plot_danceability_artist_genres_all, use_container_width=True)
    st.markdown("""<p class="picture-font"> Danceability by Top 10 Artist Genres: This chart shows a 
                strip plot of danceability scores for the top 10 artist genres found in a dataset of 
                merged streaming information. The y-axis displays the artist genres while the x-axis 
                displays the danceability scores ranging from 0 to 1. Each circle represents a track, 
                with its associated track name, artist name, artist genres, and a URL for searching the 
                track. 
            </p>""", unsafe_allow_html=True)
    




