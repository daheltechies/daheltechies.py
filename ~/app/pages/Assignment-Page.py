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
col3.header("Dahel Techies Assignment App")
title_4 =  '<p style="font-family:sans-serif; color:Grey;">This Application allows you to submit your Assignment files.</p>'
col3.markdown(title_4, unsafe_allow_html=True)
title_5 = '<p style="font-family:sans-serif; color:Grey;">Kindly fill in your details correctly</p>'
col3.markdown(title_5, unsafe_allow_html=True)
title_6 = '<p style="font-family:sans-serif; color:Grey;">Choose the cohort you belong to correctly</p>'
col3.markdown(title_6, unsafe_allow_html=True)
col4.image(image)

col_3, col_4 = st.columns(2)

# Form
deta = Deta(st.secrets["deta_key1"])
db = deta.Base("assignment-Records")

with st.form("assignment app", clear_on_submit=True):
    name = col_3.text_input('Your Name')
    cohort = col_3.text_input('Write Your Cohort Month')
    excel = col_4.text_input('Enter Excel Google Drive Folder Link')
    sql = col_3.text_input('Enter Your SQL Google Drive Folder Link')
    tableau = col_4.text_input('Enter Your Tableau Google Drive Folder Link')
    powerbi = col_3.text_input('Enter Your Power BI Google Drive Folder Link')
    submit = st.form_submit_button("Submit")
    if submit:
           st.write("Submit Successful")
           db.put({"Name1":name, "Course":cohort, "Excel_Course":excel, "SQL_Course":sql, "Tableau_Course":tableau, "PowerBI_Course":powerbi})
            

