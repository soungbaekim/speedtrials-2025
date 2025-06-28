import streamlit as st
import pandas as pd
import numpy as np
import datetime

# st.set_page_config(page_title="Regulator View", page_icon="🔍")

st.title("Regulator View: Field Analysis Kit")
st.sidebar.header("Regulator View")

st.markdown("""
## For Water System Regulators
This page provides a field kit for understanding and monitoring water system status across Georgia.

### What you can do here:
- View statewide compliance metrics and trends
- Identify systems with recurring violations
- Track enforcement actions and outcomes
- Plan site visits based on risk assessment
""")

# Dashboard metrics
st.subheader("Statewide Compliance Dashboard")

# Create columns for metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Active Systems", value="1,542", delta="5 new")
    
with col2:
    st.metric(label="Open Violations", value="87", delta="-12")
    
with col3:
    st.metric(label="Site Visits (YTD)", value="623", delta="76%", delta_color="normal")
    
with col4:
    st.metric(label="Compliance Rate", value="94.3%", delta="1.2%")

# Risk assessment map
st.subheader("Risk Assessment Map")
st.markdown("*Map visualizing water systems by risk level across Georgia*")

# Placeholder for map
st.image("https://via.placeholder.com/800x400?text=Georgia+Water+Systems+Risk+Map", use_column_width=True)
st.caption("In the full implementation, this will be an interactive map showing water systems colored by risk level")

# Filters for data exploration
st.subheader("Filter Systems")
col1, col2, col3 = st.columns(3)

with col1:
    counties = ["All Counties", "Fulton", "DeKalb", "Cobb", "Gwinnett", "Clayton"]  # Sample list
    selected_county = st.selectbox("County", counties)

with col2:
    system_types = ["All Types", "Community", "Non-Community", "Transient Non-Community"]
    selected_type = st.selectbox("System Type", system_types)
    
with col3:
    violation_types = ["All Violations", "MCL", "Monitoring", "Treatment Technique", "Public Notice"]
    selected_violation = st.selectbox("Violation Type", violation_types)

# Systems table
st.subheader("Water Systems Overview")

# Sample data for demonstration
systems_data = {
    'PWSID': ['GA0010001', 'GA0020003', 'GA0030005', 'GA0040007', 'GA0050009'],
    'System Name': ['Atlanta City Water', 'Savannah Municipal', 'Augusta Water Works', 'Columbus Water', 'Athens Water Service'],
    'Type': ['Community', 'Community', 'Community', 'Non-Community', 'Transient Non-Community'],
    'Population': [450000, 145000, 95000, 65000, 35000],
    'Open Violations': [2, 0, 4, 1, 0],
    'Risk Score': ['Low', 'Low', 'High', 'Medium', 'Low']
}

systems_df = pd.DataFrame(systems_data)
st.dataframe(
    systems_df.style.apply(lambda x: ['background-color: #ffcccc' if x['Risk Score'] == 'High' else '' for i in x], axis=1),
    use_container_width=True
)

# Enforcement actions
st.subheader("Recent Enforcement Actions")
enforcement_data = {
    'PWSID': ['GA0030005', 'GA0060011', 'GA0040007', 'GA0070013'],
    'System Name': ['Augusta Water Works', 'Macon Water Authority', 'Columbus Water', 'Valdosta Utilities'],
    'Action Type': ['Administrative Order', 'Consent Order', 'Notice of Violation', 'Administrative Order'],
    'Issue Date': ['2025-05-12', '2025-04-03', '2025-03-22', '2025-02-14'],
    'Status': ['In Progress', 'Resolved', 'In Progress', 'In Progress']
}

enforcement_df = pd.DataFrame(enforcement_data)
st.dataframe(enforcement_df, use_container_width=True)

# Export functionality placeholder
st.subheader("Generate Reports")
report_type = st.selectbox(
    "Select Report Type", 
    ["Quarterly Compliance Summary", "Annual System Performance", "Violation Trends", "Site Visit Summary"]
)

col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input("Start Date", datetime.date(2025, 1, 1))
with col2:
    end_date = st.date_input("End Date", datetime.date.today())

if st.button("Generate Report"):
    st.success(f"{report_type} for period {start_date} to {end_date} would be generated here in the full implementation.")
