import streamlit as st
import pandas as pd
from modules import send_mail



df = pd.read_csv("topics.csv")

st.header("Contact Us")

with st.form(key="contact_form"):
    user_email = st.text_input("Enter your name")
    topic = st.selectbox("Choose a topic", df['topic'])
    raw_message = st.text_area("Enter your message")
    message = f"""\
        Subject: New email from {user_email}
        Topic: {topic}

        {raw_message}  
    """ 
    submit_button = st.form_submit_button(label="Submit")

    if submit_button:
        send_mail.send_mail_smtp_ssl(message)
        st.info("Your email was sent successfully")
        

    