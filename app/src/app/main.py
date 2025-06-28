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
# Welcome to Georgia's Drinking Water Assistant

Meet your intelligent water data assistant powered by AI to help you analyze Georgia's Safe Drinking Water Information System (SDWIS) data.

## What Can Your Assistant Do?

- **Run Complex Queries**: Ask questions like "Which water systems had the most violations in 2024?"
- **Provide Data Insights**: Try "What's the relationship between system size and compliance rate?"
- **Generate Visualizations**: Ask "Show me a map of systems with lead exceedances"
- **Support All Stakeholders**: From helping residents check their water safety to assisting regulators with compliance monitoring

### Simply chat with your assistant or use the sidebar to navigate to specialized views.
""")

st.info("Select a page from the sidebar to explore data specific to your needs.")
