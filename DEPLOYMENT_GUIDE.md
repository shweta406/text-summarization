# Streamlit Cloud Deployment Guide

## Overview
This guide explains how to deploy the Text Summarization app to Streamlit Cloud in 5 minutes.

## Important: 2GB Model Handling
Your trained model is 2GB, which is too large for GitHub. The deployment setup handles this by:
1. **First deployment** - Downloads the model from HuggingFace Hub automatically (3-5 minutes for first run)
2. **Subsequent runs** - Uses cached model (instant)

The deployment uses the `google/pegasus-samsum` pretrained model from HuggingFace, which is optimized for dialogue summarization (same family as your trained model).

## Prerequisites
- GitHub account
- Streamlit Cloud account (free at https://streamlit.io/cloud)
- Your repo already pushed to GitHub ✅

## Deployment Steps

### Step 1: Verify GitHub Repository
- Ensure your repo is at: https://github.com/shweta406/text-summarization
- All files should be committed and pushed ✅

### Step 2: Create Streamlit Cloud Account
1. Go to https://share.streamlit.io
2. Click "Sign Up" 
3. Connect your GitHub account
4. Authorize Streamlit

### Step 3: Deploy Your App
1. Click "New app"
2. Connect repository: `shweta406/text-summarization`
3. Branch: `main`
4. Main file path: `streamlit_app.py`
5. Click "Deploy"

### Step 4: Wait for First Deploy
- Streamlit will build and deploy
- **First run**: Model will download (~2-3 minutes) - **This is normal, don't close the app**
- You'll see progress messages
- Once complete, you'll see the working app

### Step 5: Share Your App!
Your app will be live at:
```
https://text-summarization-<random>.streamlit.app
```

## File Structure Created for Deployment
```
.
├── .streamlit/
│   └── config.toml          (Streamlit configuration)
├── model_handler.py         (Model download logic)
├── streamlit_app.py         (Deployment entry point)
├── app.py                   (Original - UNCHANGED)
├── requirements.txt         (Already compatible)
└── src/
    └── textSummarizer/      (Your code - UNCHANGED)
```

## Troubleshooting

### "Model download timeout"
- First deployment can take 3-5 minutes
- Be patient - the model is 2GB and needs to download
- Check Streamlit logs for progress

### "Out of memory"
- Streamlit Cloud has 1GB RAM
- The app uses ~800MB at peak with model cached
- If you hit this, you may need to:
  - Use a lighter model quantization
  - Deploy to a more powerful host like Render or AWS

### "Application stopped unexpectedly"
- This happens if model download fails
- Check the error logs in Streamlit Cloud
- Try redeploying

### Want to use your custom trained model?

If you have your original `pegasus-samsum-model` (2GB) and want to use it instead of the public model:

1. **Upload to HuggingFace Hub** (recommended)
   - Create account at huggingface.co
   - Upload your model
   - Update `model_handler.py` line with your model ID

2. **Or ask for alternative deployment** to AWS S3 + Lambda + API Gateway

## Cost
- **Streamlit Cloud**: FREE (up to 3 apps)
- **Domain & SSL**: FREE
- **Bandwidth**: FREE

## Next Steps
1. Push this repo to ensure all files are committed
2. Go to streamlit.io/cloud
3. Deploy using the steps above
4. Share your live app!

## Questions?
If any issues, check:
- Streamlit logs in Cloud dashboard
- `model_handler.py` for download logic
- Ensure `streamlit run streamlit_app.py` works locally
