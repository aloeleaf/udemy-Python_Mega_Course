import streamlit as st
from modules import functions

todos = functions.get_todos()

# create fix html elements in streamlit
st.title('My Todo App')
st.subheader('This is my todo app.')
st.write("This app is to increase your productivity")

# create dynamic html elements in streamlit 
for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Enter your todo")



# st.checkbox("Buy grocery")
# st.checkbox("Pay bills")