import streamlit as st
import asyncio
from sqlalchemy import create_engine
from typing import List, Dict, Any

# Import the agent graph
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from agents.graph import create_graph

st.set_page_config(
    page_title="Water Quality Data Agent Chat",
    page_icon="💧",
    layout="wide"
)

st.title("💧 Water Quality Data Assistant")
st.markdown("Ask questions about Georgia's Safe Drinking Water Information System (SDWIS) data")

# Initialize session state for storing chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

if "agent" not in st.session_state:
    try:
        # Create database engine
        engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
        # Initialize the agent
        st.session_state.agent = create_graph(engine)
        st.session_state.db_connected = True
    except Exception as e:
        st.session_state.db_connected = False
        st.error(f"Could not connect to database. Error: {str(e)}")
        st.session_state.agent = None

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask a question about water quality data..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Check if agent is available (database connected)
    if not st.session_state.get("db_connected", False) or st.session_state.agent is None:
        error_message = "Sorry, I'm unable to answer your question as I cannot connect to the database. Please check your database connection and try again."
        
        # Display error message
        with st.chat_message("assistant"):
            st.markdown(error_message)
        
        # Add assistant error response to chat history
        st.session_state.messages.append({"role": "assistant", "content": error_message})
    else:
        # Display assistant response with a spinner while processing
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            with st.spinner("Thinking..."):
                try:
                    # Call the agent with the user's message
                    # Using invoke directly since it appears to not be a coroutine
                    response = st.session_state.agent.invoke(
                        {"messages": [{"role": "user", "content": prompt}]},
                        {"recursion_limit": 100},
                        debug=True
                    )
                    
                    # Extract the last AI message
                    last_ai_message = None
                    for msg in reversed(response["messages"]):
                        if getattr(msg, "role", None) == "assistant" or type(msg).__name__ == "AIMessage":
                            last_ai_message = msg.content if hasattr(msg, "content") else msg.get("content")
                            break
                    
                    # Display the response
                    message_placeholder.markdown(last_ai_message)
                    
                    # Add assistant response to chat history
                    st.session_state.messages.append({"role": "assistant", "content": last_ai_message})
                except Exception as e:
                    error_message = f"An error occurred while processing your request: {str(e)}"
                    message_placeholder.markdown(error_message)
                    st.session_state.messages.append({"role": "assistant", "content": error_message})

# Add a sidebar with information about the data
with st.sidebar:
    st.header("About the Data")
    st.markdown("""
    This chat interface allows you to query information about Georgia's Safe Drinking Water Information System (SDWIS).
    
    **Available Data Tables:**
    - Public Water Systems
    - Violations
    - Facilities
    - Site Visits
    - Lead and Copper Samples
    - Geographic Areas
    - Events and Milestones
    - Public Notice Violations
    - Service Areas
    - Reference tables
    
    Ask questions about water quality, violations, or specific public water systems.
    """)
