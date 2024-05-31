import streamlit as st

st.header("Select Box")

options = ["Option 1", "Option 2", "Option 3"]
option_selected = st.selectbox("Select an option", options)

st.write("You selected: ", option_selected)
