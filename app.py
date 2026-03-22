import streamlit as st
import os
import sys

# Add the current directory to the path so we can import textSummarizer
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
    
    # Check if model files exist
    model_path = os.path.join(os.path.dirname(__file__), "artifacts/model_trainer/pegasus-samsum-model")
    model_file = os.path.join(model_path, "model.safetensors")
    model_file_002 = os.path.join(model_path, "model-002.safetensors")
    
    if not os.path.exists(model_file) and os.path.exists(model_file_002):
        st.warning("⚠️ Model file needs to be renamed. Please run this command:")
        st.code("cd artifacts/model_trainer/pegasus-samsum-model && ren model-002.safetensors model.safetensors", language="bash")
        st.info("After running the command above, refresh this page.")
    elif not os.path.exists(model_file) and not os.path.exists(model_file_002):
        st.error("❌ Model files not found. Please ensure the model is downloaded in artifacts/model_trainer/pegasus-samsum-model/")
    else:
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