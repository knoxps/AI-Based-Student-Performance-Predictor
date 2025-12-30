#!/bin/bash

cd /Users/knoxpratik/AI_Student_Performance_Predictor
source venv/bin/activate

echo "🚀 Starting Streamlit app..."
echo "📍 The app will be available at: http://localhost:8501"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

streamlit run app/app.py --server.headless true

