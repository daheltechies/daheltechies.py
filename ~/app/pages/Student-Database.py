import streamlit as st
import pandas as pd
from PIL import Image
from deta import Deta
import json

# Column For Page
col5, col6 = st.columns(2)

# Image For Page
image = Image.open('image1.png')

# Page Header
col5.header("Dahel Techies Student Database App")
title_5 =  '<p style="font-family:sans-serif; color:Grey;">This Application allows you to submit your student details.</p>'
col1.markdown(title_1, unsafe_allow_html=True)
title_6 = '<p style="font-family:sans-serif; color:Grey;">Kindly fill in your details correctly</p>'
col5.markdown(title_2, unsafe_allow_html=True)
col6.image(image)

col_5, col_6 = st.columns(2)

# Form
deta = Deta(st.secrets["deta_key2"])
db = deta.Base("student-Records")

with st.form("assignment app", clear_on_submit=True):
    name = col_5.text_input('Your Name')
    phone = col_6.text_input('Enter Your Phone Number')
    cohort = col_5.text_input('Enter Your Cohort Month')
    certificate = col_6.text_input('Enter Your Course Stack')
    email = col_5.text_input('Enter Your Email Address')
    folder = col_6.text_input('Enter Your Google Drive Folder Link')
    submit = st.form_submit_button("Submit")
    if submit:
           st.write("Submit Successful")
           db.put({"Student_Name":name, "Phone_Number":phone, "Email_Address":email, "Cohort Month": cohort, 
                   "Certification": certificate,"Folder Link":folder})

