from datetime import time, date
import streamlit as st

st.title("Day 8: Slider")

st.header("Slider")
values_1 = st.slider("How old are you?", 0, 130, 25)

st.header("Range Slider")
values_2 = st.slider("Select a range of values", 0.0, 100.0, (25.0, 75.0))

st.header("Range time Slider")
values_3 = st.slider(
    "Select a range of time",
    min_value=time(0, 0),  # start of the day
    max_value=time(23, 59),  # end of the day
    value=(time(9, 0), time(17, 0)),  # default value
)

st.header("Datetime Slider")
values_4 = st.slider(
    "Select a range of dates",
    date(2019, 1, 1),
    date(2024, 12, 31),
    date(2021, 1, 1),
)

# st.select_slider displays a slider widget to select items from a list.
color = st.select_slider(
    "Select a color of the rainbow",
    options=["red", "orange", "yellow", "green", "blue", "indigo", "violet"],
)
st.write("My favorite color is", color)

start_color, end_color = st.select_slider(
    "Select a range of color wavelength",
    options=["red", "orange", "yellow", "green", "blue", "indigo", "violet"],
    value=("red", "blue"),
)
st.write("You selected wavelengths between", start_color, "and", end_color)

print_button = st.button("Print values")
if print_button:
    st.write(f"Values 1: {values_1}")
    st.write(f"Values 2: {values_2}")
    st.write(f"Values 3: {values_3}")
    st.write(f"Values 4: {values_4}")
    st.write(f"Color: {color}")
    st.write(f"Start color: {start_color}, End color: {end_color}")
