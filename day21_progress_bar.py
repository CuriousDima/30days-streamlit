import streamlit as st
import time

st.title("st.progress")

my_bar = st.progress(0)

for percent_complete in range(100):
    time.sleep(0.05)
    my_bar.progress(percent_complete + 1)

st.toast("We are done ;)")
