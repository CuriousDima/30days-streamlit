import streamlit as st

# Whenever a user interacts with a widget, the Streamlit app is rerun.
# A form is a container that visually groups other elements and widgets
# together, and contains a Submit button. Herein, a user can interacts
# with one or more widgets for as many times as they like without causing
#  a rerun.

st.title("Example Form")

with st.form("coffee_order_form"):
    st.subheader("**Order your coffee**")

    # Input widgets
    coffee_bean_val = st.selectbox("Coffee bean", ["Arabica", "Robusta"])
    coffee_roast_val = st.selectbox("Coffee roast", ["Light", "Medium", "Dark"])
    brewing_val = st.selectbox(
        "Brewing method", ["Aeropress", "Drip", "French press", "Moka pot", "Siphon"]
    )
    serving_type_val = st.selectbox("Serving format", ["Hot", "Iced", "Frappe"])
    milk_val = st.select_slider("Milk intensity", ["None", "Low", "Medium", "High"])
    owncup_val = st.checkbox("Bring own cup")

    # Every form must have a submit button
    submitted = st.form_submit_button("Order coffee!")

if submitted:
    st.markdown(
        f"""
        ☕ You have ordered:
        - Coffee bean: `{coffee_bean_val}`
        - Coffee roast: `{coffee_roast_val}`
        - Brewing: `{brewing_val}`
        - Serving type: `{serving_type_val}`
        - Milk: `{milk_val}`
        - Bring own cup: `{owncup_val}`
        """
    )
