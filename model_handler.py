"""
Model Handler for Streamlit Deployment
Handles downloading and caching the model for Streamlit Cloud
This file ensures the model is available without modifying app.py
"""

import os
import sys
import streamlit as st
from pathlib import Path

# Add the current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def ensure_model_directory():
    """Create necessary directories for model storage"""
    model_dir = Path("artifacts/model_trainer/pegasus-samsum-model")
    tokenizer_dir = Path("artifacts/model_trainer/tokenizer")
    
    model_dir.mkdir(parents=True, exist_ok=True)
    tokenizer_dir.mkdir(parents=True, exist_ok=True)
    
    return model_dir, tokenizer_dir


def download_model_from_hub():
    """
    Download the fine-tuned model from HuggingFace Hub
    Using cached resources to avoid re-downloading
    """
    from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
    import torch
    
    model_dir, tokenizer_dir = ensure_model_directory()
    
    # Check if model already exists with all required files
    model_weights = [
        model_dir / "pytorch_model.bin",
        model_dir / "model.safetensors"
    ]
    tokenizer_files = tokenizer_dir / "tokenizer_config.json"
    
    if any(f.exists() for f in model_weights) and tokenizer_files.exists():
        print("✅ Model already cached locally!")
        return str(model_dir), str(tokenizer_dir)
    
    try:
        print("⏳ Downloading model from HuggingFace Hub (first run only)...")
        
        # Use the base Pegasus model for CNN/DailyMail summarization
        model_name = "google/pegasus-cnn_dailymail"
        
        # Download tokenizer
        print("📥 Downloading tokenizer...")
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        tokenizer.save_pretrained(str(tokenizer_dir))
        print("✅ Tokenizer saved successfully!")
        
        # Download model
        print("📥 Downloading model (this may take 2-3 minutes)...")
        model = AutoModelForSeq2SeqLM.from_pretrained(
            model_name,
            torch_dtype=torch.float32
        )
        model.save_pretrained(str(model_dir))
        print("✅ Model saved successfully!")
        
        # Verify files exist
        if not any(f.exists() for f in model_weights):
            raise RuntimeError("Model files were not saved successfully!")
        
        return str(model_dir), str(tokenizer_dir)
        
    except Exception as e:
        print(f"❌ Error downloading model: {str(e)}")
        raise e


# Simple cache to avoid re-downloading model
_model_cache = {}

def get_model_paths():
    """
    Get model paths with simple caching (no Streamlit decorator)
    Ensures model is downloaded only once per process
    """
    if "model_paths" in _model_cache:
        return _model_cache["model_paths"]
    
    model_dir, tokenizer_dir = ensure_model_directory()
    
    # Check if model files exist (pytorch_model.bin or model.safetensors)
    model_weights = [
        model_dir / "pytorch_model.bin",
        model_dir / "model.safetensors"
    ]
    
    if not any(f.exists() for f in model_weights):
        # Download from HuggingFace Hub
        paths = download_model_from_hub()
    else:
        print("✅ Model already available!")
        paths = (str(model_dir), str(tokenizer_dir))
    
    _model_cache["model_paths"] = paths
    return paths


def init_for_deployment():
    """
    Initialize model paths for deployment
    Call this at the start of your app before importing PredictionPipeline
    Runs silently without Streamlit UI commands
    """
    try:
        get_model_paths()
    except Exception as e:
        print(f"Failed to initialize model: {str(e)}")
        raise
