import streamlit as st

st.header("Multiselect")

options = ["Option 1", "Option 2", "Option 3"]
option_selected = st.multiselect("Select an option", options)

st.write("You selected: ", option_selected)
