# ✅ Deployment Checklist

Use this checklist before deploying your AI Student Performance Predictor.

## Pre-Deployment Checklist

### 📋 Code Quality
- [ ] All code is tested locally
- [ ] No hardcoded paths or credentials
- [ ] Error handling is in place
- [ ] Models are trained and saved

### 📦 Dependencies
- [ ] `requirements.txt` is up to date
- [ ] All required packages are listed
- [ ] Version numbers are pinned (if needed)
- [ ] No unnecessary packages included

### 🔧 Configuration
- [ ] `.streamlit/config.toml` is configured
- [ ] `.gitignore` excludes sensitive files
- [ ] No secrets committed to repository
- [ ] Environment variables documented (if any)

### 📁 Files
- [ ] `models/` directory contains trained models
- [ ] `data/student_data.csv` exists (or will be generated)
- [ ] `app/app.py` is the main application file
- [ ] `Procfile` exists (for Heroku)
- [ ] `Dockerfile` exists (for Docker)

### 🧪 Testing
- [ ] App runs locally: `streamlit run app/app.py`
- [ ] Predictions work correctly
- [ ] UI displays properly
- [ ] All features functional

### 📚 Documentation
- [ ] `README.md` is complete
- [ ] Deployment instructions are clear
- [ ] Usage examples provided
- [ ] Troubleshooting section included

## Platform-Specific Checklist

### Streamlit Cloud
- [ ] Repository is on GitHub
- [ ] Main file path: `app/app.py`
- [ ] Branch is specified (usually `main`)
- [ ] `requirements.txt` is in root directory

### Render.com
- [ ] Build command: `pip install -r requirements.txt`
- [ ] Start command: `streamlit run app/app.py --server.port $PORT --server.headless true`
- [ ] Python version specified (3.11+)

### Heroku
- [ ] `Procfile` contains correct command
- [ ] Heroku account created
- [ ] Heroku CLI installed
- [ ] App created: `heroku create app-name`

### Docker
- [ ] Dockerfile is tested locally
- [ ] Image builds successfully: `docker build -t student-predictor .`
- [ ] Container runs: `docker run -p 8501:8501 student-predictor`

## Post-Deployment Checklist

### ✅ Verification
- [ ] App loads without errors
- [ ] All pages accessible
- [ ] Predictions work correctly
- [ ] Performance is acceptable
- [ ] Mobile responsive (if needed)

### 📊 Monitoring
- [ ] Logs are accessible
- [ ] Error tracking set up (optional)
- [ ] Performance monitoring (optional)

### 🔒 Security
- [ ] No sensitive data exposed
- [ ] HTTPS enabled (if applicable)
- [ ] API rate limiting (if applicable)

## Quick Test Commands

```bash
# Test locally
streamlit run app/app.py

# Test Docker
docker build -t student-predictor .
docker run -p 8501:8501 student-predictor

# Test requirements
pip install -r requirements.txt

# Test model loading
python -c "import joblib; joblib.load('models/best_model.pkl')"
```

## Common Issues

1. **Models not found**: Train models first with `python train_model.py`
2. **Import errors**: Check `requirements.txt` includes all packages
3. **Port conflicts**: Use different port or check what's using 8501
4. **Build fails**: Check logs for specific error messages

---

**Ready to deploy?** Choose your platform and follow the deployment guide!

