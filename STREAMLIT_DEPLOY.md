# 🚀 Quick Deployment Guide - Streamlit Cloud

## Step-by-Step Deployment to Streamlit Cloud

### Prerequisites
1. GitHub account
2. Code pushed to GitHub repository

### Deployment Steps

#### 1. Push to GitHub
```bash
# Initialize git (if not already)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: AI Student Performance Predictor"

# Add remote (replace with your repo URL)
git remote add origin https://github.com/yourusername/AI_Student_Performance_Predictor.git

# Push to GitHub
git push -u origin main
```

#### 2. Deploy on Streamlit Cloud

1. **Go to Streamlit Cloud**
   - Visit: https://share.streamlit.io
   - Sign in with your GitHub account

2. **Create New App**
   - Click "New app" button
   - Authorize Streamlit to access your GitHub (if first time)

3. **Configure App**
   - **Repository**: Select your repository
   - **Branch**: Select `main` (or your default branch)
   - **Main file path**: Enter `app/app.py`
   - **App URL**: Choose a unique URL (optional)

4. **Advanced Settings** (Optional)
   - **Python version**: 3.11 (default should work)
   - **Secrets**: Add any environment variables if needed

5. **Deploy**
   - Click "Deploy" button
   - Wait for build to complete (~2-5 minutes)

6. **Access Your App**
   - Your app will be live at: `https://your-app-name.streamlit.app`

### Troubleshooting

#### Build Fails - Missing Dependencies
**Solution**: Ensure `requirements.txt` includes all packages:
```bash
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Update requirements"
git push
```

#### Model Files Not Found
**Solution**: Ensure model files are in the repository:
```bash
# Train models locally
python train_model.py

# Commit models (if small enough)
git add models/
git commit -m "Add trained models"
git push
```

**Alternative**: Train models in Streamlit Cloud by adding a setup script or training on first run.

#### App Crashes on Load
**Solution**: Check logs in Streamlit Cloud dashboard:
- Go to app settings
- Click "Manage app" → "Logs"
- Look for error messages

#### Port Already in Use
**Solution**: Not needed for Streamlit Cloud (handled automatically)

### Best Practices

1. **Keep Requirements Updated**
   - Pin major versions in `requirements.txt`
   - Test locally before deploying

2. **Model File Size**
   - If models are large (>100MB), consider:
     - Using Git LFS
     - Training on first app load
     - Using external storage

3. **Environment Variables**
   - Use Streamlit Secrets for sensitive data
   - Create `.streamlit/secrets.toml` (not committed)

4. **Performance**
   - Use `@st.cache_resource` for model loading
   - Already implemented in `app.py`

5. **Version Control**
   - Use meaningful commit messages
   - Tag releases

### Custom Domain (Optional)

Streamlit Cloud supports custom domains:
1. Go to app settings
2. Click "Manage app"
3. Add custom domain in settings

---

**Need Help?**
- Streamlit Cloud Docs: https://docs.streamlit.io/streamlit-community-cloud
- Community Forum: https://discuss.streamlit.io

