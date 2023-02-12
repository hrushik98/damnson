import requests
import json
import streamlit as st

response = requests.get('https://meme-api.com/gimme/PublicFlashing')

if response.status_code == 200:
    content = response.content.decode('utf-8')
    data = json.loads(content)
    img_url = data['url']
else:
    print('Failed to retrieve data')

st.set_page_config(page_title="Random Imgur Image", page_icon=":guardsman:", layout="wide")

st.header("Random Imgur Image")
if st.button("r/sexybutnotporn"):

    st.image(img_url, width=300)


