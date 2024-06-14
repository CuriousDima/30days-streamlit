# https://your_app.streamlit.app/?first_key=1&second_key=two&third_key=true
import streamlit as st

st.title("st.query_params")

st.write("Try <url>?param1=val1&param2=val2,etc.")
st.write(f"You params: {st.query_params}")
