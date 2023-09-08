# Streamlit app for Portfolio
import streamlit as st

col1,col2 = st.columns(2)

with col1:
  st.title("Hey, I'm Naveen Kumar Konam")
  st.header("Python Developer")

with col2:
  st.header("I am analyst turned Developer")
  st.write("These are my projects")

