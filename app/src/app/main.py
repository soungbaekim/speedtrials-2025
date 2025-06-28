import streamlit as st

st.set_page_config(
    page_title="Georgia Drinking Water Dashboard",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Georgia Drinking Water Dashboard")
st.sidebar.title("Navigation")

st.markdown("""
# Welcome to Georgia's Drinking Water Dashboard

This application provides insights into Georgia's drinking water systems using data from
the Safe Drinking Water Information System (SDWIS).

## Key Features

- **For the Public**: Understand if your drinking water is safe
- **For Operators**: Track notices and compliance tasks
- **For Regulators**: Field kit for understanding water system status

### Use the sidebar to navigate to different sections.
""")

st.info("Select a page from the sidebar to explore data specific to your needs.")
