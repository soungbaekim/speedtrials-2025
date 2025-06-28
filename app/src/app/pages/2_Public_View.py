import streamlit as st
import pandas as pd
import numpy as np

# st.set_page_config(page_title="Public View", page_icon="🏠")

st.title("Public View: Understanding Your Drinking Water")
st.sidebar.header("Public View")

st.markdown("""
## For Georgia Residents
This page helps you understand if your drinking water is safe and compliant with regulations.

### What you can do here:
- Search for your water system by name, county, or zip code
- View water quality information and compliance status
- Understand any active violations or notices
- Learn about your water source and treatment processes
""")

# County selector placeholder
st.subheader("Find Your Water System")
counties = ["Fulton", "DeKalb", "Cobb", "Gwinnett", "Clayton"]  # Sample list
selected_county = st.selectbox("Select your county", counties)

st.info(f"You selected {selected_county} County. In the full implementation, this will display water systems for this county.")

# Water system quality visualization placeholder
st.subheader("Water Quality Overview")

# Sample data for demonstration
data = {
    'Parameter': ['Lead', 'Copper', 'Nitrate', 'Bacteria', 'Chlorine'],
    'Status': ['Below Limit', 'Below Limit', 'Below Limit', 'Not Detected', 'Within Range'],
    'Value': ['0.005', '0.3', '2.1', '0', '1.2'],
    'Limit': ['0.015', '1.3', '10.0', '0', '0.5-4.0']
}

df = pd.DataFrame(data)
st.table(df)

st.markdown("""
### Understanding Water Quality Parameters
- **Lead and Copper**: EPA action level is 0.015 mg/L for lead and 1.3 mg/L for copper
- **Nitrate**: Maximum contaminant level is 10 mg/L
- **Bacteria**: No coliform bacteria should be present
- **Chlorine**: Should be maintained between 0.5 and 4.0 mg/L

### Active Notices
""")

# Placeholder for actual notices
st.warning("No active notices for your selected water system at this time.")
