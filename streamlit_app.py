import streamlit as st
import requests

st.title("Web Scraper")

url_to_scrape = st.text_input("Enter the URL you want to scrape")

email_to_share = st.text_input("Enter your email to share the Google Sheet")

if st.button("Start Scraping"):
    response = requests.post("http://localhost:5000/scrape", json={"url": url_to_scrape, "email": email_to_share})
    st.write("Links are being extracted, this may take a while. Once they are completed, they will be shared with you via Google Sheets.")
