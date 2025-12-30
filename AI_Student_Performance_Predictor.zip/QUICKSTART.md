# 🚀 Quick Start Guide

Get up and running with the AI-Based Student Performance Predictor in minutes!

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Installation

### Option 1: Automated Setup (Recommended)

```bash
./setup.sh
```

This will:
- Create a virtual environment
- Install all dependencies
- Set up the project

### Option 2: Manual Setup

1. **Create virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Generate dataset** (if not already present)
   ```bash
   cd data
   python3 generate_dataset_standalone.py
   cd ..
   ```

## Usage

### Step 1: Train the Model

Open the Jupyter notebook and run all cells:

```bash
jupyter notebook notebooks/model_training.ipynb
```

This will:
- Load and preprocess the data
- Train 3 ML models (Logistic Regression, Random Forest, XGBoost)
- Compare their performance
- Save the best model to `models/best_model.pkl`

**Expected time**: 2-5 minutes

### Step 2: Run the Web Application

Start the Streamlit app:

```bash
streamlit run app/app.py
```

The app will automatically open in your browser at `http://localhost:8501`

### Step 3: Make Predictions

1. Fill in the student information in the web form
2. Click "Predict Performance"
3. View the predicted result and confidence scores

## Project Structure Overview

```
AI_Student_Performance_Predictor/
├── data/                    # Dataset files
│   ├── student_data.csv     # Main dataset (600 records)
│   └── generate_dataset*.py # Dataset generation scripts
├── notebooks/               # Jupyter notebooks
│   └── model_training.ipynb # Complete ML pipeline
├── app/                     # Web application
│   └── app.py              # Streamlit app
├── models/                  # Saved models (created after training)
│   ├── best_model.pkl
│   ├── scaler.pkl
│   └── ...
├── requirements.txt         # Python dependencies
└── README.md               # Full documentation
```

## Troubleshooting

### Issue: "ModuleNotFoundError"
**Solution**: Make sure you've activated the virtual environment and installed dependencies:
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### Issue: "Model files not found"
**Solution**: Train the model first by running the Jupyter notebook:
```bash
jupyter notebook notebooks/model_training.ipynb
```

### Issue: "Dataset not found"
**Solution**: Generate the dataset:
```bash
cd data
python3 generate_dataset_standalone.py
cd ..
```

### Issue: Streamlit not opening
**Solution**: Manually open `http://localhost:8501` in your browser

## Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Check [report.md](report.md) for project analysis and results
- Experiment with different models and hyperparameters
- Add your own features to improve predictions

## Need Help?

Refer to the main [README.md](README.md) for comprehensive documentation.

---

**Happy Predicting! 🎓✨**

