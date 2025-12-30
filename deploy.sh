#!/bin/bash

# Deployment script for AI Student Performance Predictor
# This script helps prepare and deploy the application

set -e

echo "🚀 AI Student Performance Predictor - Deployment Helper"
echo "========================================================"
echo ""

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check prerequisites
echo "📋 Checking prerequisites..."

if ! command_exists python3; then
    echo "❌ Python 3 is not installed"
    exit 1
fi
echo "✅ Python 3 found"

if ! command_exists git; then
    echo "⚠️  Git is not installed (optional but recommended)"
else
    echo "✅ Git found"
fi

# Activate venv if exists
if [ -d "venv" ]; then
    source venv/bin/activate
    echo "✅ Virtual environment activated"
fi

# Check if models are trained
if [ ! -f "models/best_model.pkl" ]; then
    echo ""
    echo "⚠️  Models not found. Training models..."
    python train_model.py
fi

# Check dependencies
echo ""
echo "📦 Checking dependencies..."
pip install -r requirements.txt --quiet
echo "✅ Dependencies up to date"

# Run tests (if test file exists)
if [ -f "test_app.py" ]; then
    echo ""
    echo "🧪 Running tests..."
    python -m pytest test_app.py -v || echo "⚠️  Tests failed, but continuing..."
fi

echo ""
echo "✅ Deployment preparation complete!"
echo ""
echo "📝 Deployment Options:"
echo ""
echo "1. Streamlit Cloud:"
echo "   - Push to GitHub: git push origin main"
echo "   - Go to https://share.streamlit.io"
echo "   - Deploy with main file: app/app.py"
echo ""
echo "2. Render.com:"
echo "   - Connect GitHub repo"
echo "   - Build: pip install -r requirements.txt"
echo "   - Start: streamlit run app/app.py --server.port \$PORT --server.headless true"
echo ""
echo "3. Heroku:"
echo "   - heroku create your-app-name"
echo "   - git push heroku main"
echo ""
echo "4. Docker:"
echo "   - docker build -t student-predictor ."
echo "   - docker run -p 8501:8501 student-predictor"
echo ""
echo "5. Local Production:"
echo "   - streamlit run app/app.py --server.port 8501 --server.headless true"
echo ""

