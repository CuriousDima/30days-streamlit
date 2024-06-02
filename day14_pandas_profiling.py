import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

st.header("Pandas Profiler on Streamlit")

# Create a sample DataFrame
data = {
    "ID": [23, 43, 12, 13, 67, 89, 90, 56, 34],
    "Name": [
        "Ram",
        "Deep",
        "Yash",
        "Aman",
        "Arjun",
        "Aditya",
        "Divya",
        "Chalsea",
        "Akash",
    ],
    "Marks": [89, 97, 45, 78, 56, 76, 100, 87, 81],
    "Grade": ["B", "A", "F", "C", "E", "C", "A", "B", "B"],
}
df = pd.DataFrame(data)

# Generate the profile report
profile = ProfileReport(df, title="Pandas Profiling Report")
st_profile_report(profile)
