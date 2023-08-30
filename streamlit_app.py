import streamlit as st
import requests


replit_url = "https://selenium-backend.icecube1513.repl.co/scrape"


url_to_scrape = st.text_input("Enter the URL you want to scrape:")
if st.button("Scrape"):
    if url_to_scrape:
        response = requests.post(replit_url, json={"url": url_to_scrape})
        if response.status_code == 200:
            st.write("Scraping completed!")
            st.write(response.json())
        else:
            st.write(f"An error occurred: {response.content}")
    else:
        st.write("Please enter a URL.")
