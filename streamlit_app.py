"""
Streamlit Deployment Wrapper
Run this file instead of app.py for Streamlit Cloud deployment
This ensures the model is ready before the main app starts
Your original app.py remains completely unchanged
"""

import streamlit as st
from model_handler import init_for_deployment

# Initialize model on app startup
if "model_initialized" not in st.session_state:
    st.session_state.model_initialized = False
    init_for_deployment()
    st.session_state.model_initialized = True

# Now run the original app
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from textSummarizer.pipeline.prediction import PredictionPipeline

# Configure page
st.set_page_config(
    page_title="Text Summarization",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("📝 Text Summarization Application")
st.markdown("---")

# Sidebar for navigation
with st.sidebar:
    st.header("Navigation")
    option = st.radio(
        "Select an option:",
        ["Home", "Prediction"],
        index=0
    )

# Home Page
if option == "Home":
    st.header("Welcome to Text Summarization")
    st.write("""
    This application uses advanced machine learning models to summarize text automatically.
    
    **Features:**
    - 📄 Summarize long texts into concise summaries
    - ⚡ Fast and accurate summarization
    - 🎯 Simple and intuitive interface
    
    Use the sidebar to navigate to the Prediction section.
    """)

# Prediction Page
elif option == "Prediction":
    st.header("Summarize Your Text")
    
    # Text area for input
    input_text = st.text_area(
        "Enter the text you want to summarize:",
        placeholder="Paste your text here...",
        height=200
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Generate Summary", type="primary", use_container_width=True):
            if input_text.strip():
                try:
                    with st.spinner("Generating summary..."):
                        obj = PredictionPipeline()
                        summary = obj.predict(input_text)
                    
                    st.success("Summary generated successfully!")
                    st.subheader("Original Text:")
                    st.write(input_text)
                    st.subheader("Summary:")
                    st.write(summary)
                    
                except Exception as e:
                    st.error(f"Error occurred: {str(e)}")
            else:
                st.warning("Please enter some text to summarize.")
    
    with col2:
        if st.button("Clear", use_container_width=True):
            st.rerun()
