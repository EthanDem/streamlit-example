import streamlit as st
import requests

st.header("Link Grabber")
api_url = "https://link-grabber-backend.icecube1513.repl.co/scrape"


url_to_scrape = st.text_input("Enter the main domain of the pages you would like to scrape")
email_to_share = st.text_input("Enter your email to share to Google Sheets")

if st.button("Scrape"):
    if url_to_scrape and email_to_share:
        st.write("Results will be shared via Google Sheets. You can close this tab now.")

        response = requests.post(api_url, json={"url": url_to_scrape, "email": email_to_share})
        if response.status_code == 200:
            st.write("Scraping completed!")
            scraped_data = response.json()  # Adjusted this line

            for link in scraped_data:
                st.write(link)
        else:
            st.write(f"An error occurred: {response.content}")
    elif not url_to_scrape:
        st.write("Please enter a URL.")
    elif not email_to_share:
        st.write("Please enter an email.")
