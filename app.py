import requests
import json
import streamlit as st
st.title("Subreddit Image viewer")
st.text("")
st.text("Created by @Hrush1k")
st.text("")

sub_reddit_name = st.text_input("Enter subreddit name:")
st.text("Example: wholesomememes for r/wholesomememes")

if st.button("Go!"):
    try:
        response = requests.get(f'https://meme-api.com/gimme/{sub_reddit_name}')

        if response.status_code == 200:
            content = response.content.decode('utf-8')
            data = json.loads(content)
            img_url = data['url']
            st.image(img_url, width=300)
        else:
            st.warning("Failed to retrive data. Check if the subreddit exists.")


      

       
    except:
        st.warning("Enter a valid subreddit name!")
