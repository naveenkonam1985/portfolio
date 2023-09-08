# Streamlit app for Portfolio
import streamlit as st

col1,col2 = st.columns([0.3,0.7])

with col1:
  st.title("Hey, I'm Naveen Kumar Konam")
  st.header("Data Engineer")

  st.markdown("#### Skills")
  st.write("Python")
  st.write("SQL")
  st.write("Hadoop")
  

with col2:
  st.markdown("## About Me")
  st.write("These are my projects")

  st.markdown("## Projects")

