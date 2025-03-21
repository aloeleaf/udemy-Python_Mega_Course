import streamlit as st
import pandas as pd

# Configures the default settings of the page.
st.set_page_config(layout="wide")

df = pd.read_csv("data.csv", sep=",")



#Display text in header formatting.
st.header("Our Team")

content_h1 ="""
The Best Company
"""
st.header(content_h1)

content_p1 = """
lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""
st.write(content_p1)


# Create three columns.
# Insert containers laid out as side-by-side columns.
col_1, col_2, col_3 = st.columns(3)

with col_1:
    for index, row in df[:4].iterrows():
        st.subheader(f"{row["first name"].title()} {row["last name"].title()}")
        st.write(row["role"])
        st.image("images/" + row["image"])

with col_2:
    for index, row in df[4:8].iterrows():
        st.subheader(f"{row["first name"].title()} {row["last name"].title()}")
        st.write(row["role"])
        st.image("images/" + row["image"])

with col_3:
   for index, row in df[8:].iterrows():
        st.subheader(f"{row["first name"].title()} {row["last name"].title()}")
        st.write(row["role"])
        st.image("images/" + row["image"])
   