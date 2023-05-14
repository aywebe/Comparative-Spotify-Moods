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

source = "dataframe"

horizontal_stripplot =  alt.Chart(source, width=600, height=100).mark_circle(size=12).encode(
    y=alt.Y(
        'jitter:Q',
        title=None,
        axis=alt.Axis(values=[0], ticks=True, grid=False, labels=False),
        scale=alt.Scale(),
    ),
    x=alt.X('lifeExp:Q', scale=alt.Scale(domain=(20, 85))),
    color=alt.Color('continent:N', legend=None),
    row=alt.Row(
        'continent:N',
        header=alt.Header(
            labelAngle=0,
            labelFontSize=16,
            titleOrient='top',
            labelOrient='left',
            labelAlign='left',
        ),
    ),
).transform_calculate(
    # Generate Gaussian jitter with a Box-Muller transform
    jitter='sqrt(-2*log(random()))*cos(2*PI*random())'
).configure_facet(
    spacing=0
).configure_view(
    stroke=None
).configure_axis(
    labelFontSize=16,
    titleFontSize=16
)