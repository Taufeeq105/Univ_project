import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


st.title('DE Lab Dashboard')
ch=['query1','query2','query3','query4']
sel=st.sidebar.selectbox("choose query",ch)
a1=[i for i in range(20)]
a2=[j+5 for j in range(20)]
data = {
  "calories":a1,
  "duration":a2
}
df = pd.DataFrame(data)

if sel=='query1':
  fig, ax = plt.subplots()
  ax.hist(df['duration'])
  st.pyplot(fig)
  
if sel=='query2':
  fig, ax = plt.subplots()
  ax.hist(df['calories'])
  st.pyplot(fig)
  
