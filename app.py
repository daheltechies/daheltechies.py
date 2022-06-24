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

# Deta Detabase
deta = Deta(st.secrets["deta_key"])
db = deta.Base("CRM-Records")

col_1, col_2 = st.columns(2)

january = col_1.checkbox('January Cohort')
february = col_2.checkbox('February Cohort')
march = col_1.checkbox('March Cohort')
april = col_2.checkbox('April Cohort')
may = col_1.checkbox('May Cohort')
june = col_2.checkbox('June Cohort')
july = col_1.checkbox('July Cohort')
august = col_2.checkbox('August Cohort')
september = col_1.checkbox('September Cohort')
october = col_2.checkbox('October Cohort')
november = col_1.checkbox('November Cohort')
december = col_2.checkbox('December Cohort')

if january:
    assignment = st.selectbox("Choose:", ('Excel Internship', 'SQL Internship','Tableau Internship', 'PowerBI Internship'))





