# Local Testing Guide (Before Streamlit Cloud Deployment)

## Test the Deployment Setup Locally

Before pushing to GitHub and deploying to Streamlit Cloud, test it locally to ensure everything works:

### Step 1: Test with Your Original app.py
```bash
# Still works as before
streamlit run app.py
```

### Step 2: Test the Deployment Version
```bash
# Test the version that will run on Streamlit Cloud
streamlit run streamlit_app.py
```

**Expected behavior:**
1. App starts
2. First run: "Downloading model from HuggingFace Hub" message appears
3. Progress messages show download status (2-3 minutes for 2GB)
4. App fully loads with UI
5. Can summarize text successfully
6. Subsequent runs: Skips download (model cached)

### Step 3: Verify Model Download
Check that model files are created:
```bash
ls artifacts/model_trainer/pegasus-samsum-model/
# Should show: config.json, generation_config.json, pytorch_model.bin (or model.safetensors)

ls artifacts/model_trainer/tokenizer/
# Should show: tokenizer_config.json, spiece.model, etc.
```

### Troubleshooting Local Testing

**Issue: "ModuleNotFoundError"**
```bash
# Ensure you're in the project directory and have installed requirements
pip install -r requirements.txt
# or
conda env create -f environment.yml  # if you have this
```

**Issue: "CUDA out of memory"**
- This is fine! Model will use CPU (slower but works)
- Streamlit Cloud also uses CPU

**Issue: "Connection timeout downloading model"**
- Check internet connection
- HuggingFace Hub might be temporarily down
- Try again later

## What Changed vs Original?
✅ **NOT Changed:**
- app.py (your original code)
- main.py (your training pipeline)
- requirements.txt (compatible as-is)
- src/textSummarizer/ (all your components)

✅ **NEW Files Created:**
- `streamlit_app.py` - Deployment entry point
- `model_handler.py` - Handles model download for cloud
- `.streamlit/config.toml` - Streamlit settings
- `DEPLOYMENT_GUIDE.md` - This guide
- `LOCAL_TESTING_GUIDE.md` - You're reading this!

## Next: Ready to Deploy?
Once local testing works:
1. `git add .`
2. `git commit -m "Add Streamlit Cloud deployment setup"`
3. `git push origin main`
4. Follow steps in `DEPLOYMENT_GUIDE.md`
