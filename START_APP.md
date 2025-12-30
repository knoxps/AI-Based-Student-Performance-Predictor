# 🚀 How to Start the App

## Quick Start (3 Steps)

### Step 1: Install Dependencies

```bash
# Navigate to project directory
cd /Users/knoxpratik/AI_Student_Performance_Predictor

# Option A: Use setup script (recommended)
./setup.sh

# Option B: Manual setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Step 2: Train the Model (Required First Time)

The app needs trained models to make predictions. Train them first:

```bash
# Activate virtual environment (if not already active)
source venv/bin/activate

# Start Jupyter notebook
jupyter notebook notebooks/model_training.ipynb
```

**In the notebook:**
- Run all cells (Cell → Run All)
- Wait for training to complete (~2-5 minutes)
- Models will be saved to `models/` directory

### Step 3: Start the Streamlit App

```bash
# Make sure virtual environment is activated
source venv/bin/activate

# Start the app
streamlit run app/app.py
```

The app will automatically open in your browser at `http://localhost:8501`

---

## Troubleshooting

### ❌ "Streamlit not found"
**Solution:** Install dependencies first:
```bash
source venv/bin/activate
pip install streamlit
```

### ❌ "Model files not found"
**Solution:** Train the model first by running the Jupyter notebook (Step 2 above)

### ❌ "ModuleNotFoundError"
**Solution:** Activate virtual environment and install requirements:
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### ❌ App won't open in browser
**Solution:** Manually open `http://localhost:8501` in your browser

---

## Complete Command Sequence

```bash
# 1. Navigate to project
cd /Users/knoxpratik/AI_Student_Performance_Predictor

# 2. Setup (first time only)
./setup.sh
# OR manually:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 3. Train model (first time only)
jupyter notebook notebooks/model_training.ipynb
# Run all cells in the notebook

# 4. Start app
source venv/bin/activate
streamlit run app/app.py
```

---

**Note:** After the first setup, you only need Step 3 to start the app (assuming models are already trained).

