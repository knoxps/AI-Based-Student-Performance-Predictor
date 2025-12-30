#!/bin/bash

# 🚀 QUICK START - Get everything running in 5 minutes
# This script sets up and runs the AI Student Performance Predictor

set -e

echo "╔══════════════════════════════════════════════════════════╗"
echo "║  🎓 AI Student Performance Predictor - Quick Start      ║"
echo "║  Get your app running in 5 minutes!                     ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Step 1: Check Python
echo -e "${BLUE}📋 Step 1/5: Checking Python...${NC}"
if ! python3 --version &> /dev/null; then
    echo -e "${RED}❌ Python 3 is not installed${NC}"
    exit 1
fi
echo -e "${GREEN}✅ Python $(python3 --version) found${NC}"
echo ""

# Step 2: Setup Virtual Environment
echo -e "${BLUE}📦 Step 2/5: Setting up virtual environment...${NC}"
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo -e "${GREEN}✅ Virtual environment created${NC}"
else
    echo -e "${YELLOW}ℹ️  Virtual environment already exists${NC}"
fi

source venv/bin/activate
pip install --upgrade pip --quiet
echo -e "${GREEN}✅ Virtual environment activated${NC}"
echo ""

# Step 3: Install Dependencies
echo -e "${BLUE}📥 Step 3/5: Installing dependencies...${NC}"
pip install -r requirements.txt --quiet
echo -e "${GREEN}✅ All dependencies installed${NC}"
echo ""

# Step 4: Check/Create Models
echo -e "${BLUE}🤖 Step 4/5: Checking models...${NC}"
if [ ! -f "models/best_model.pkl" ]; then
    echo -e "${YELLOW}⚠️  Models not found. Training models...${NC}"
    python train_model.py
    echo -e "${GREEN}✅ Models trained and saved${NC}"
else
    echo -e "${GREEN}✅ Models already exist${NC}"
fi
echo ""

# Step 5: Check Data
echo -e "${BLUE}📊 Step 5/5: Checking dataset...${NC}"
if [ ! -f "data/student_data.csv" ]; then
    echo -e "${YELLOW}⚠️  Dataset not found. Generating dataset...${NC}"
    cd data
    python generate_dataset_standalone.py
    cd ..
    echo -e "${GREEN}✅ Dataset generated${NC}"
else
    echo -e "${GREEN}✅ Dataset exists${NC}"
fi
echo ""

# Final Step: Start the app
echo "╔══════════════════════════════════════════════════════════╗"
echo "║                    🎉 Setup Complete!                    ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""
echo -e "${GREEN}✅ Everything is ready!${NC}"
echo ""
echo -e "${BLUE}🚀 Starting Streamlit app...${NC}"
echo ""
echo -e "${YELLOW}📍 Your app will open at: http://localhost:8501${NC}"
echo -e "${YELLOW}   Press Ctrl+C to stop the server${NC}"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Start Streamlit
streamlit run app/app.py --server.headless true

