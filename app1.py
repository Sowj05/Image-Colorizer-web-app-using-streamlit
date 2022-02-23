import streamlit as st
import requests

#title
st.title("Image Colorizer")
st.subheader(" This app can convert Black & white images to Color")
st.markdown("This app is built by Sowjanya")

#file uploader to upload black and white images
file = st.file_uploader("choose an Image " )
if file:
    st.write(file)

#we need to send this image using API to backend  team
#for that we need to send requests

if st.button("Colorize your image"): #when this button will be pressed
    r = requests.post( # it'll sent one request to API
        "https://api.deepai.org/api/colorizer",
      files={
        'image': file #it
     },
      headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
    )
    print(r.json())
    st.write(r.json())#

#text to image
