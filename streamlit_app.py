import streamlit as st
import requests

api_url = "https://link-grabber-backend.icecube1513.repl.co/scrape"
st.header("URL Grabber")
url_to_scrape = st.text_input("Enter the URL you want to fetch all webpages from")

if st.button("Scrape"):
    st.write("Scraping in progress. This may take a while.")
    if url_to_scrape:
        response = requests.post(api_url, json={"url": url_to_scrape})
        if response.status_code == 200:
            st.success("Scraping completed!")
            scraped_data = response.json()  # Adjusted this line

            for link in scraped_data:
                st.write(link)
        else:
            st.write(f"An error occurred: {response.content}")
    else:
        st.write("Please enter a URL.")
