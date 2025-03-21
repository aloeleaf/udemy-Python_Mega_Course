import streamlit as st

st.header("Contuct Me")

with st.form(key="contact_form"):
    user_email = st.text_input("Your email address")
    message = st.text_area("Your message")
    submit_button = st.form_submit_button()
    if submit_button:
        print("pressed")
    
    
    