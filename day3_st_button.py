import streamlit as st

# The header function is used to create a title for the app.
st.header("Button Example")

button = st.button("Click me")
if button:
    st.write("Button clicked")
else:
    st.write("Button not clicked")
