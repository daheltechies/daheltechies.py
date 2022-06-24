import streamlit as st
import pandas as pd
from PIL import Image
from deta import Deta
import json

# Column For Page
col1, col2 = st.columns(2)

# Image For Page
image = Image.open('image1.png')

# Page Header
col1.header("Dahel Techies Internship App")
title_1 =  '<p style="font-family:sans-serif; color:Grey;">This Application allows you to submit your internship videos and files.</p>'
col1.markdown(title_1, unsafe_allow_html=True)
title_2 = '<p style="font-family:sans-serif; color:Grey;">Kindly fill in your details correctly</p>'
col1.markdown(title_2, unsafe_allow_html=True)
title_3 = '<p style="font-family:sans-serif; color:Grey;">Choose the cohort you belong to correctly</p>'
col1.markdown(title_3, unsafe_allow_html=True)
col2.image(image)

col_1, col_2 = st.columns(2)

# Form
deta = Deta(st.secrets["deta_key"])

with st.form("internship app"):
    name = col_1.text_input('Your Name')
    cohort = col_1.selectbox('Select Your Cohort', ('Select One','January Cohort', 'February Cohort', 'March Cohort', 'April Cohort', 'May Cohort',
                                             'June Cohort', 'July Cohort', 'August Cohort', 'September Cohort',
                                             'October Cohort', 'November Cohort', 'December Cohort'))
    course = col_2.multiselect('Select Your Internship Course',('Excel', 'SQL', 'Tableau', 'PowerBI'))
    link = col_2.text_input('Your Google Drive Link')
    submit = st.form_submit_button("Submit")
    if submit:
           db.put({"Student Name":name, "Cohort":cohort, "Course":course, "Google Drive Link":link})
                      
    
