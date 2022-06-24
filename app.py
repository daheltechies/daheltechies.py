import streamlit as st
import pandas as pd
from PIL import Image

col1, col2 = st.columns(2)
# Image For Page
image = Image.open('image1.png')

col1.header("Dahel Techies Internship App")
title_1 =  '<p style="font-family:sans-serif; color:Grey;">This Application allows you to submit your internship videos and files.</p>'
col1.markdown(title_1, unsafe_allow_html=True)
title_2 = '<p style="font-family:sans-serif; color:Grey;">Kindly fill in your details correctly</p>'
col1.markdown(title_2, unsafe_allow_html=True)
col2.image(image)

