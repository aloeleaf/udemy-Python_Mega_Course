import streamlit as st
import send_email


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
        send_email.send_mail_smtp_ssl(message)
        st.info("Your email was sent successfully")
