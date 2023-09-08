# Streamlit app for Portfolio
import streamlit as st

col1,col2 = st.columns([0.4,0.6])

with col1:
  st.title("Hey, I'm Naveen Kumar Konam")
  st.header("Data Engineer")

  st.markdown("#### Skills")
  st.write("Python")
  st.write("SQL")
  st.write("Hadoop")
  

with col2:
  st.markdown("## About Me")
  st.write("Myself an aspiring data engineer, interested in building paltforms which can help the customers achieve their tasks effortlessly and efficiently")

  st.markdown("## Projects")
  st.markdown("### Table Crawler")
  st.write("Table Crawler is a simple project to scrape the tables from webpages without writing code")
  st.markdown("![Table Crawler]https://tablecrawler.streamlit.app/")

