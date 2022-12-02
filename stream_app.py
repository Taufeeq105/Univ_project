import streamlit as st
import pandas as pd
import numpy as np

st.title('DE Lab Dashboard')


@st.cache
option = st.sidebar.selectbox(
    'Select Query you want to run?',
    ('Q1', 'Q2', 'Q3','Q4','Q5'))

st.write('You selected:', option)
