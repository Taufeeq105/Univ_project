import streamlit as st
import pandas as pd
import numpy as np

st.title('DE Lab Dashboard')
ch=['query1','query2','query3','query4']
sel=st.sidebar.selectbox("choose query",ch)
