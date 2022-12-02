import streamlit as st
import pandas as pd
import numpy as np

st.title('DE Lab Dashboard')


@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


st.subheader('Number of pickups by hour')
option = st.selectbox(
    'How would you like to be contacted?',
    ('Q1', 'Q2', 'Q3','Q4','Q5'))

st.write('You selected:', option)
