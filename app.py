import streamlit as st
from url_shortner import URLShortener

# Initialize the URL shortener
url_shortener = URLShortener()

st.title('URL Shortener')

tab1, tab2 = st.tabs(["Shorten URL", "Decode URL"])

with tab1:
    st.header("Create Short URL")
    long_url = st.text_input("Enter the URL to shorten")
    if st.button("Shorten"):
        if long_url:
            short_url = url_shortener.encode_url(long_url)
            st.success(f"Your shortened URL: {short_url}")
        else:
            st.error("Please enter a URL")

with tab2:
    st.header("Get Original URL")
    short_url = st.text_input("Enter the shortened URL")
    if st.button("Decode"):
        if short_url:
            original_url = url_shortener.decode_url(short_url)
            if original_url:
                st.success(f"Original URL: {original_url}")
            else:
                st.error("URL not found")
        else:
            st.error("Please enter a shortened URL")