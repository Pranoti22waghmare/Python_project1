
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

df=pd.read_csv("heart.csv")
df

st.title("Pranoti Waghmare")
st.header("Python")
st.write("MSC DSAI")
st.write(df.head())

fig=px.bar(x=df["chol"],y=df['age'])
st.plotly_chart(fig)

fig=px.line(x=df["chol"],y=df['age'])
st.plotly_chart(fig)

fig=px.scatter(df["thalach"])
st.plotly_chart(fig)

fig=px.histogram(x=df["chol"])
st.plotly_chart(fig)