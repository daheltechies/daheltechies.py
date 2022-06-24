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

# Setting Cohort Buttons
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

# Deta Detabase
deta = Deta(st.secrets["deta_key"])
db = deta.Base("January Cohort")

if january:
    assignment = st.selectbox("Choose:", ('Excel Internship', 'SQL Internship','Tableau Internship', 'PowerBI Internship'))
    # Excel Assignment
    if assignment == 'Excel Internship':
        st.subheader("January Cohort Excel Page")
        form = st.form("forms", clear_on_submit=True)
        name = form.text_input("Student Name")
        folder = form.text_input("Google Drive Link")
        submit = form.form_submit_button("Submit")
        if submit:
            st.success("Submitted Successfully")
            db.put({"Name": name,  "Folder Link": folder})

# Deta Detabase
deta = Deta(st.secrets["deta_key1"])
db = deta.Base("January Cohort")  

    if assignment == 'SQL Internship':
        st.subheader("January Cohort SQL Page")
        form1 = st.form("forms1", clear_on_submit=True)
        name1 = form1.text_input("Student Name")
        folder1 = form1.text_input("Google Drive Link")
        submit1 = form1.form_submit_button("Submit")
        if submit1:
            st.success("Submitted Successfully")
            db.put({"Name": name1, "Folder Link": folder1})
            





