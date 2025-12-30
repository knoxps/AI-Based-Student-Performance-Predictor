# ⚡ 5-Minute Deployment Guide

Get your AI Student Performance Predictor up and running in **5 minutes**!

## 🚀 Quick Start (Local)

### Option 1: Automated Script (Fastest - 2 minutes)

```bash
chmod +x QUICK_START.sh
./QUICK_START.sh
```

That's it! The script will:
- ✅ Set up virtual environment
- ✅ Install all dependencies
- ✅ Train models (if needed)
- ✅ Start the web app

**Your app will be live at: http://localhost:8501**

---

## 📦 Manual Setup (3-5 minutes)

### Step 1: Install Dependencies (1 min)
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Step 2: Train Models (2 min)
```bash
python train_model.py
```

### Step 3: Run App (30 sec)
```bash
streamlit run app/app.py
```

---

## 🌐 Deploy to Cloud (5 minutes)

### Streamlit Cloud (Recommended - Easiest)

#### 1. Push to GitHub (2 min)
```bash
git init
git add .
git commit -m "AI Student Performance Predictor"
git remote add origin YOUR_GITHUB_REPO_URL
git push -u origin main
```

#### 2. Deploy (3 min)
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click "New app"
3. Select your repository
4. Set Main file: `app/app.py`
5. Click "Deploy"

**Done! Your app is live! 🎉**

---

## 🐳 Docker Deployment (3 minutes)

```bash
# Build (2 min)
docker build -t student-predictor .

# Run (30 sec)
docker run -p 8501:8501 student-predictor
```

Access at: http://localhost:8501

---

## ✅ Pre-Deployment Checklist

Quick check before deploying:

- [ ] All files committed to Git
- [ ] `requirements.txt` is up to date
- [ ] Models are trained (`models/best_model.pkl` exists)
- [ ] App runs locally without errors
- [ ] `.gitignore` excludes `venv/` and sensitive files

---

## 🎯 Project Status

### ✅ Ready for Deployment
- ✅ Streamlit web app (`app/app.py`)
- ✅ Trained ML models (`models/`)
- ✅ Dataset (`data/student_data.csv`)
- ✅ Requirements file (`requirements.txt`)
- ✅ Dockerfile for containerization
- ✅ Procfile for Heroku
- ✅ Configuration files (`.streamlit/config.toml`)
- ✅ Documentation (README.md, deployment guides)

### 📁 Project Structure
```
AI_Student_Performance_Predictor/
├── app/
│   └── app.py              # ✅ Main Streamlit app
├── models/                 # ✅ Trained models
├── data/                   # ✅ Dataset
├── requirements.txt        # ✅ Dependencies
├── Dockerfile              # ✅ Docker config
├── Procfile                # ✅ Heroku config
├── QUICK_START.sh          # ✅ Quick setup script
└── README.md               # ✅ Full documentation
```

---

## 🆘 Troubleshooting

### Issue: Module not found
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### Issue: Models not found
```bash
python train_model.py
```

### Issue: Port already in use
```bash
streamlit run app/app.py --server.port 8502
```

### Issue: Permission denied (scripts)
```bash
chmod +x QUICK_START.sh setup.sh deploy.sh
```

---

## 🎉 Success!

Your AI Student Performance Predictor is now ready to:
- ✅ Make predictions locally
- ✅ Deploy to Streamlit Cloud
- ✅ Deploy to Render/Heroku
- ✅ Run in Docker containers
- ✅ Scale to production

**Next Steps:**
1. Test predictions locally
2. Push to GitHub
3. Deploy to Streamlit Cloud
4. Share your app! 🚀

---

**Need help?** Check the detailed guides:
- `README.md` - Full documentation
- `STREAMLIT_DEPLOY.md` - Streamlit Cloud guide
- `DEPLOYMENT.md` - All deployment options

