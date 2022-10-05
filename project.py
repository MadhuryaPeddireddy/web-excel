import streamlit as st
import pandas as pd
import os
import cv2
st.set_page_config(page_title='SRM EXCEL')
st.sidebar.title("Pick the type of file")
file = st.sidebar.radio("The options available",options=("None", "CSV(.csv) FILE", "EXCEL(.xlsx) FILE"))
if file=="None":
  st.title("DISPLAYING THE EXCEL FILE IN TABLE FORMAT")
  img = cv2.imread("excel.webp")
  st.image(img, channels='RGB')
  st.header("Go to sidebar and select the type of file to upload...")
if file == "CSV(.csv) FILE":
  uploaded_file = st.file_uploader("Upload the CSV file",type=['csv'],accept_multiple_files=False,key="fileUploader")
  if uploaded_file is not None:
    st.write(f'The file name is {uploaded_file.name}.')
    file_name, file_extension = os.path.splitext(uploaded_file.name)
    st.write(file_extension)
    df=pd.read_csv(uploaded_file)
    df
  else:
    st.warning("You should upload a .csv file!")
if file=="EXCEL(.xlsx) FILE":
  uploaded_file = st.file_uploader("Upload the EXCEL file",type=['xlsx'],accept_multiple_files=False,key="fileUploader")
  if uploaded_file is not None:
    st.write(f'The file name is {uploaded_file.name}.')
    file_name, file_extension = os.path.splitext(uploaded_file.name)
    st.write("The extension of the file is ",file_extension)
    df=pd.read_excel(uploaded_file)
    df
  else:
    st.warning("You should upload a .xlsx file!")

