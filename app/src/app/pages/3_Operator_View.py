import streamlit as st
import pandas as pd
import numpy as np
import datetime

st.set_page_config(page_title="Operator View", page_icon="🔧")

st.title("Operator View: Compliance Management")
st.sidebar.header("Operator View")

st.markdown("""
## For Water System Operators
This page helps you track notices and compliance tasks for your water system.

### What you can do here:
- Monitor upcoming compliance deadlines
- Track violation history and resolution status
- Manage public notice requirements
- View site visit reports and action items
""")

# System selector placeholder
st.subheader("Select Water System")
systems = ["Atlanta Water System", "Savannah Water System", "Augusta Water System"]  # Sample list
selected_system = st.selectbox("Select water system", systems)

# Tabs for different operator functions
tab1, tab2, tab3 = st.tabs(["Compliance Tasks", "Violations", "Site Visits"])

with tab1:
    st.header("Upcoming Compliance Tasks")
    
    # Sample compliance tasks for demonstration
    today = datetime.datetime.now()
    tasks = {
        'Task': ['Quarterly Sampling', 'Annual Report Submission', 'Filter Maintenance', 
                 'Lead & Copper Testing', 'Chemical Inventory'],
        'Deadline': [
            (today + datetime.timedelta(days=15)).strftime("%Y-%m-%d"),
            (today + datetime.timedelta(days=45)).strftime("%Y-%m-%d"),
            (today + datetime.timedelta(days=5)).strftime("%Y-%m-%d"),
            (today + datetime.timedelta(days=30)).strftime("%Y-%m-%d"),
            (today + datetime.timedelta(days=10)).strftime("%Y-%m-%d")
        ],
        'Status': ['Pending', 'Not Started', 'In Progress', 'Pending', 'Not Started']
    }
    
    tasks_df = pd.DataFrame(tasks)
    st.dataframe(tasks_df, use_container_width=True)
    
    # Task completion form
    st.subheader("Mark Task as Complete")
    with st.form("task_form"):
        task_select = st.selectbox("Select task", tasks_df['Task'].tolist())
        completion_date = st.date_input("Completion date", datetime.datetime.now())
        submit_button = st.form_submit_button(label="Submit")
        
        if submit_button:
            st.success(f"Task '{task_select}' marked as complete on {completion_date}")

with tab2:
    st.header("Violation History")
    
    # Sample violations for demonstration
    violations = {
        'Violation ID': ['V-2025-001', 'V-2025-002', 'V-2024-015', 'V-2024-009', 'V-2024-002'],
        'Type': ['Monitoring', 'MCL', 'Treatment Technique', 'Public Notification', 'Monitoring'],
        'Date Identified': ['2025-04-15', '2025-03-10', '2024-11-22', '2024-08-17', '2024-02-05'],
        'Status': ['Open', 'Open', 'Resolved', 'Resolved', 'Resolved'],
        'Due Date': ['2025-06-30', '2025-05-15', 'N/A', 'N/A', 'N/A']
    }
    
    violations_df = pd.DataFrame(violations)
    st.dataframe(violations_df, use_container_width=True)
    
    # Filter by status
    status_filter = st.multiselect("Filter by status", options=["Open", "Resolved"], default=["Open", "Resolved"])
    
    st.info("In the full implementation, the table above will be filtered based on your selection.")

with tab3:
    st.header("Recent Site Visits")
    
    # Sample site visits for demonstration
    site_visits = {
        'Visit ID': ['SV-2025-012', 'SV-2025-005', 'SV-2024-087', 'SV-2024-054'],
        'Visit Type': ['Sanitary Survey', 'Complaint Investigation', 'Follow-up', 'Routine Inspection'],
        'Visit Date': ['2025-05-20', '2025-02-12', '2024-12-08', '2024-08-15'],
        'Inspector': ['J. Smith', 'A. Johnson', 'R. Williams', 'T. Davis'],
        'Findings': ['1 Major, 2 Minor', 'No Findings', '3 Minor', 'No Findings']
    }
    
    site_visits_df = pd.DataFrame(site_visits)
    st.dataframe(site_visits_df, use_container_width=True)
    
    st.subheader("Action Items from Last Visit")
    st.markdown("""
    - Increase free chlorine residual at Entry Point A
    - Replace filter media in Filter #3
    - Update emergency response plan
    - Submit backflow prevention test results
    """)
