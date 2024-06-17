import streamlit as st

st.title("Percentage Calculator")

st.latex(
    r"""
    \begin{aligned}
    \text{whole} & \quad \xrightarrow{is} \quad 100\% \\
    \text{part}  & \quad \xrightarrow{is} \quad x\%
    \end{aligned}
"""
)


def percent_of_whole():
    st.session_state.part = st.session_state.whole * (st.session_state.percent / 100.0)


def whole_from_part():
    st.session_state.whole = (st.session_state.part / st.session_state.percent) * 100


col1, col2, col3 = st.columns([2, 1, 2])
with col1:
    part = st.number_input("Whole:", key="whole", on_change=percent_of_whole)
with col2:
    percent = st.number_input("Percent:", key="percent", on_change=percent_of_whole)
with col3:
    kilogram = st.number_input("Part:", key="part", on_change=whole_from_part)

st.latex(
    r"\text{whole} + \text{part} = %s"
    % str(st.session_state.whole + st.session_state.part)
)
