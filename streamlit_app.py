import streamlit as st
import requests

# Your Flask API URL
api_url = "https://link-grabber-backend.icecube1513.repl.co/scrape"

# Streamlit UI
url_to_scrape = st.text_input("Enter the URL you want to scrape:")
if st.button("Scrape"):
    if url_to_scrape:
        response = requests.post(api_url, json={"url": url_to_scrape})
        if response.status_code == 200:
            st.write("Scraping completed!")
            scraped_data = response.json()['data']

            # Display the scraped data
            for link in scraped_data:
                st.write(link)
        else:
            st.write(f"An error occurred: {response.content}")
    else:
        st.write("Please enter a URL.")
