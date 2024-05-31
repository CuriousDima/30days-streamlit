import streamlit as st

st.title("Check Box")
icecream = st.checkbox("Do you like ice cream?")
if icecream:
    st.write("You like ice cream!")

coffee = st.checkbox("Do you like coffee?")
if coffee:
    st.write("You like coffee!")

cola = st.checkbox("Do you like cola?")
if cola:
    st.write("You like cola!")
