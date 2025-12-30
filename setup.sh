#!/bin/bash

# Setup script for AI Student Performance Predictor
# This script sets up the project environment

set -e  # Exit on error

echo "🚀 Setting up AI Student Performance Predictor..."
echo ""

# Check Python version
echo "📋 Checking Python version..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
required_version="3.11"

if ! python3 -c "import sys; exit(0 if sys.version_info >= (3, 11) else 1)" 2>/dev/null; then
    echo "❌ Python 3.11+ is required. Found: $python_version"
    exit 1
fi
echo "✅ Python $python_version detected"

# Create virtual environment
echo ""
echo "📦 Creating virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✅ Virtual environment created"
else
    echo "ℹ️  Virtual environment already exists"
fi

# Activate virtual environment
echo ""
echo "🔌 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo ""
echo "⬆️  Upgrading pip..."
pip install --upgrade pip > /dev/null 2>&1
echo "✅ pip upgraded"

# Install requirements
echo ""
echo "📥 Installing dependencies..."
pip install -r requirements.txt
echo "✅ Dependencies installed"

# Check if models exist
echo ""
if [ ! -f "models/best_model.pkl" ]; then
    echo "⚠️  Model files not found. Training models..."
    echo ""
    python train_model.py
else
    echo "✅ Model files found"
fi

# Check if data exists
echo ""
if [ ! -f "data/student_data.csv" ]; then
    echo "⚠️  Dataset not found. Generating dataset..."
    cd data
    python generate_dataset_standalone.py
    cd ..
    echo "✅ Dataset generated"
else
    echo "✅ Dataset found"
fi

echo ""
echo "🎉 Setup complete!"
echo ""
echo "To start the app, run:"
echo "  source venv/bin/activate"
echo "  streamlit run app/app.py"
echo ""

