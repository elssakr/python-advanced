import streamlit as st

st.sidebar.header("Sidebar")

st.sidebar.write("This is the sidebar")

st.sidebar.selectbox("Chose an option", ["Option 1","Optiom2","Option 3"])

st.sidebar.radio("Go to",["Home","Data","Settings"])