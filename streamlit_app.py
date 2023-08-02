import streamlit as st
import requests

# Get parameters from the user
param1 = st.text_input('Enter the first parameter:')

if st.button('Scrape'):
    # Send a request to the Flask app
    response = requests.post('http://localhost:5000/scrape', json={'param1': param1, 'param2': param2})

    # Check if the request was successful
    if response.status_code == 200:
        # Display the scraped data
        st.write(response.json()['data'])
    else:
        # Display the error message
        st.error(response.json()['message'])
