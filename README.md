# Text Summarization

Web-based NLP application that trains and serves a Pegasus-based abstractive summarizer, with a Streamlit UI for inference.

## Key Features
- Pegasus-CNN/DailyMail model fine-tuned on SAMSum for dialogue summarization.
- End-to-end pipeline: data ingestion → validation → transformation → training → evaluation.
- Streamlit UI for interactive summarization.
- Config-driven via YAML; artifacts stored under `artifacts/`.
- Includes pre-downloaded model/tokenizer artifacts for offline use.

## Tech Stack
- Python, Hugging Face Transformers, Datasets, Evaluate/ROUGE, PyTorch
- Streamlit for UI
- YAML-driven configs

## Repository Structure
- app.py: Streamlit UI (Home + Prediction).
- main.py: Runs full training pipeline (all stages).
- config/config.yaml: Paths and model/data settings.
- src/textSummarizer: Package code (components, pipeline, utils).
- artifacts/: Data, processed datasets, trained model (`pegasus-samsum-model`), tokenizer, metrics.
- requirements.txt: Python deps.
- research/: Notebooks for experimentation.

## Quickstart (Inference via Streamlit)
1) Clone and create a venv:
```bash
git clone https://github.com/shweta406/text-summarization.git
cd text-summarization
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install --upgrade pip
pip install -r requirements.txt
```

2) Ensure model file name is correct:
If `artifacts/model_trainer/pegasus-samsum-model/model-002.safetensors` exists but `model.safetensors` does not, rename:
```bash
cd artifacts/model_trainer/pegasus-samsum-model
ren model-002.safetensors model.safetensors
cd ../../..
```

3) Run the UI:
```bash
streamlit run app.py
```
Use the **Prediction** tab, paste text, click **Generate Summary**.

## Training Pipeline (Reproduce Model)
Run all stages end-to-end:
```bash
python main.py
```
Stages (in order):
1. Data Ingestion
2. Data Validation
3. Data Transformation (tokenization)
4. Model Training
5. Model Evaluation (writes metrics to `artifacts/model_evaluation/metrics.csv`)

Configs for each stage are in `config/config.yaml`.

## Configuration
- Data + artifact roots: see `config/config.yaml`.
- Model checkpoint used for fine-tuning: `google/pegasus-cnn_dailymail`.
- Tokenizer path and model path for inference come from the `model_evaluation` section.

## Notes on Artifacts
- `artifacts/model_trainer/pegasus-samsum-model/` (~2GB) and tokenizer files are checked in so the app can run offline.
- `artifacts/data_ingestion` and `artifacts/data_transformation` contain SAMSum splits and processed datasets.
- For a lighter repo, remove large artifacts and re-run the pipeline to regenerate.

## Tests
- No automated tests are included. To validate, run `python main.py` and confirm `metrics.csv` is produced, then exercise the Streamlit app.

## Troubleshooting
- Model file warning in UI: rename `model-002.safetensors` to `model.safetensors` as above.
- Slow startup: first run downloads Pegasus weights if artifacts are missing.
- Memory: Pegasus can be memory-intensive; use CPU with enough RAM or a GPU-enabled environment.

