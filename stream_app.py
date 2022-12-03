import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff


st.title('DE Lab Dashboard')
ch=['query1','query2','query3','query4']
sel=st.sidebar.selectbox("choose query",ch)
a1=[i for i in range(20)]
a2=[j+5 for j in range(20)]
data = {"calories":a1,"duration":a2}
df = pd.DataFrame(data)

if sel=='query1':
  fig = ff.create_distplot(a1, 'q1')
  st.plotly_chart(fig, use_container_width=True)
  
if sel=='query2':
  fig = ff.create_distplot(a2, 'q2')
  st.plotly_chart(fig, use_container_width=True)
  
