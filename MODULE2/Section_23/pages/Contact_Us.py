import streamlit as st
from send_email import send_mail


st.header("Contuct Me")

with st.form(key="contact_form"):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your message")
    message = f"""\
    Subject: New email from {user_email}
    
    from: {user_email}    
    {raw_message}
    """
    submit_button = st.form_submit_button("Submit")
    if submit_button:
        send_mail(message)
        st.info("Your email was sent successfully")
        
    
    
    