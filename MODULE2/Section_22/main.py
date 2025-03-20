import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)


with col1:
    st.image("images/photo.png")

with col2:
    st.header("Ardit Sulce" )
    content= """
    I am a software engineer with a passion for data science and machine learning. I have experience in building web applications, data pipelines, and machine learning models. I am always looking for new challenges and opportunities to learn and grow."""
    st.info(content)

content2 = """Bellow you ca find some of the apps I have buit in Python. Fell free to contact me!"""
st.write(content2)



col3, col4 = st.columns(2)
content = pd.read_csv("data.csv", sep=";")
with col3:    
    for index, row in content[:10].iterrows():
        st.header(row["title"])
with col4:
    for index, row in content[10:].iterrows():
        st.header(row["title"])
  