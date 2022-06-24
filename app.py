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
    cohort = col_1.text_input('Write Your Cohort Month')
    excel = col_2.text_input('Enter Excel Google Drive Folder Link (If Null Skip)')
    sql = col_2.text_input('Enter Your SQL Google Drive Folder Link')
    tableau = col_2.text_input('Enter Your Tableau Google Drive Folder Link')
    powerbi = col_1.text_input('Enter Your Power BI Google Drive Folder Link')
    submit = st.form_submit_button("Submit")
    if submit:
           db.put({"Student_Name":name, "Cohort":cohort, "Excel":excel, "SQL":sql, "Tableau":tableau, "PowerBI":powerbi})
            
try:
    db_content = db.fetch().items
    st.write(db_content)
except:
    pass
                      
    
