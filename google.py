import streamlit as st
import pandas as pd
import os

# File path for storing user data
CSV_FILE = 'user_data.csv'

# Function to save user data to CSV
def save_to_csv(username, email, password):
    # Check if the CSV file already exists
    if os.path.isfile(CSV_FILE):
        # Append data to the existing CSV file
        data = pd.DataFrame({
            'Username': [username],
            'Email': [email],
            'Password': [password]
        })
        data.to_csv(CSV_FILE, mode='a', header=False, index=False)
    else:
        # Create a new CSV file with a header
        data = pd.DataFrame({
            'Username': [username],
            'Email': [email],
            'Password': [password]
        })
        data.to_csv(CSV_FILE, mode='w', header=True, index=False)

# Title of the sign-up page
st.title("Sign-Up Page")

# Collect user input
with st.form(key='signup_form'):
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type='password')
    submit_button = st.form_submit_button(label='Sign Up')

    if submit_button:
        if username and email and password:
            save_to_csv(username, email, password)
            st.success("You have successfully signed up!")
        else:
            st.error("Please fill out all fields.")
