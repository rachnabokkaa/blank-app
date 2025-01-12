import streamlit as st
import google.generativeai as genai
import os
import json
st.set_page_config(page_title="My Streamlit Website", page_icon="🌐", layout="wide")

st.title("Taylored Tunes🎶")
st.markdown("""Not sure which Taylor Swift song fits your mood? Share how you're feeling, and we'll "Taylor" the perfect tune for you!

""")
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css?family=Your+Font+Name');
body {
    font-family: 'Your Font Name', mono-space;
}
</style>
""", unsafe_allow_html=True)
    # Title
st.title("Tell us the tale")

# Input text box
user_input = st.text_input("Enter your thoughts:")
# Display the input
genai.configure(api_key="AIzaSyBnUgN41vzt8lBQJJVnZ1Ug3GYIb___0K0")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(f"give me only the song name taylor swift song that is the most similar to the emotion in this paragraph: {user_input}")
response_description = model.generate_content(f"using the song {response}, tell me why this song applies to this : {user_input}")

if user_input:
    st.write(response.text)
    st.write(response_description.text)
