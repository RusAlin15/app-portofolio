import streamlit as st
from send_email import send_email

st.title("Contact me!")

with st.form("email_forms"):
    user_email = st.text_input("Enter yout email adress!", key="user_email")
    subject = f"Subject: New email from  {user_email}"
    message = st.text_area("Your message")
    message = subject + "\n" + message + "\n" + user_email
    submit = st.form_submit_button("Submit")
    if submit:
        send_email(message)
        st.info("Your email was successfully sent!")
