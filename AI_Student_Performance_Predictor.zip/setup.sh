#!/bin/bash

# Setup script for AI-Based Student Performance Predictor

echo "🎓 AI-Based Student Performance Predictor - Setup"
echo "=================================================="
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"
echo ""

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    echo "✅ Virtual environment created"
else
    echo "✅ Virtual environment already exists"
fi

echo ""
echo "🔧 Activating virtual environment..."
source venv/bin/activate

echo ""
echo "📥 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "✅ Setup complete!"
echo ""
echo "📝 Next steps:"
echo "1. Activate virtual environment: source venv/bin/activate"
echo "2. Generate dataset (if needed): cd data && python3 generate_dataset_standalone.py"
echo "3. Train models: jupyter notebook notebooks/model_training.ipynb"
echo "4. Run web app: streamlit run app/app.py"
echo ""
echo "Happy predicting! 🎓✨"

