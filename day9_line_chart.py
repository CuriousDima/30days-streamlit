import pandas as pd
import numpy as np
import streamlit as st

# st.line_chart displays a line chart. It is syntax sugar for st.altair_chart.
# if really want to customize the graph, use st.altair_chart instead.

st.header("Line Chart")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.line_chart(chart_data)

st.header("Scutter Chart")
normal_data = np.random.normal(loc=0.0, scale=1.0, size=1000)
st.scatter_chart(normal_data)
