import streamlit as st
import pandas as pd
from PIL import Image
from deta import Deta
import json

# Column For Page
col3, col4 = st.columns(2)

# Image For Page
image = Image.open('image1.png')

# Page Header
col3.header("Dahel Techies Python Programming Assignment App")
title_4 =  '<p style="font-family:sans-serif; color:Grey;">This Application allows you to submit your Python Programming Assignment files.</p>'
col3.markdown(title_4, unsafe_allow_html=True)
title_5 = '<p style="font-family:sans-serif; color:Grey;">Kindly fill in your details correctly</p>'
col3.markdown(title_5, unsafe_allow_html=True)
title_6 = '<p style="font-family:sans-serif; color:Grey;">Choose the cohort you belong to correctly</p>'
col3.markdown(title_6, unsafe_allow_html=True)
col4.image(image)

col_3, col_4 = st.columns(2)

# Form
deta = Deta(st.secrets["deta_key3"])
db = deta.Base("python-Records")

with st.form("python app", clear_on_submit=True):
    name = col_3.text_input('Your Name')
    cohort = col_3.text_input('Write Your Cohort Month')
    assignment = col_4.text_input('Enter Your Assignment Google Drive Folder Link')
    link = col_4.text_input('Enter the link of your project if available')
    submit = st.form_submit_button("Submit")
    if submit:
           st.write("Submit Successful")
           db.put({"Name ":name, "Course":cohort, "Assignment":assignment, "Project Link":link})
