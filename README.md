# 🎓 AI-Based Student Performance Predictor

A machine learning-powered web application that predicts student academic performance (Pass/Fail) based on various academic and personal factors. Built with Streamlit and deployed using modern cloud platforms.

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## ✨ Features

- 🤖 **Multiple ML Models**: Automatic comparison of Logistic Regression, Random Forest, and XGBoost
- 📊 **Real-time Predictions**: Get instant predictions with confidence scores
- 🎨 **Modern UI**: Beautiful, responsive web interface built with Streamlit
- 📈 **Data Visualization**: Interactive charts and probability distributions
- 🚀 **Easy Deployment**: Ready-to-deploy configuration for multiple platforms
- 🔒 **Robust**: Error handling, validation, and model caching

## 🎯 Demo

Try the live application:
- **Streamlit Cloud**: [Deploy on Streamlit Cloud](https://streamlit.io/cloud)
- **Render**: [Deploy on Render](https://render.com)
- **Heroku**: [Deploy on Heroku](https://heroku.com)

## 📋 Table of Contents

- [Features](#-features)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Usage](#-usage)
- [Model Details](#-model-details)
- [Deployment](#-deployment)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)
- [License](#-license)

## 🚀 Installation

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- Git (optional, for cloning)

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/AI_Student_Performance_Predictor.git
cd AI_Student_Performance_Predictor
```

### Step 2: Create Virtual Environment

```bash
python3 -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

## 🏃 Quick Start

### 1. Train the Model (First Time Only)

The app requires trained models to make predictions. Train them using:

```bash
python train_model.py
```

This will:
- Load the dataset from `data/student_data.csv`
- Train multiple ML models
- Select the best model based on F1-Score
- Save models to `models/` directory

### 2. Generate Dataset (If Needed)

If you need to regenerate the dataset:

```bash
cd data
python generate_dataset_standalone.py
cd ..
```

### 3. Run the Application

```bash
streamlit run app/app.py
```

The app will automatically open in your browser at `http://localhost:8501`

## 💻 Usage

### Making Predictions

1. **Navigate to Predictor Page**: Use the sidebar navigation
2. **Fill in Student Information**:
   - **Demographics**: Gender, Age
   - **Academic Metrics**: Attendance %, Previous Score, Internal Marks
   - **Study Habits**: Hours Studied/Week, Assignments Submitted
   - **Environmental**: Parent Education, Internet Access
3. **Click "Predict Performance"**: Get instant predictions
4. **View Results**: See predicted outcome, confidence scores, and probability distributions

### Understanding Results

- **Predicted Result**: Pass or Fail classification
- **Confidence Score**: Percentage confidence in the prediction
- **Probability Distribution**: Visual chart showing Pass/Fail probabilities
- **Input Summary**: Review all entered values

## 🔬 Model Details

### Input Features

| Feature | Type | Description |
|---------|------|-------------|
| Gender | Categorical | Male/Female |
| Age | Numerical | Student age (18-25) |
| Attendance % | Numerical | Class attendance percentage (0-100) |
| Hours Studied | Numerical | Weekly study hours (0-50) |
| Previous Score | Numerical | Previous academic score (0-100) |
| Parent Education | Categorical | Education level of parents |
| Internet Access | Categorical | Yes/No |
| Assignments Submitted | Numerical | Number of assignments (0-10) |
| Internal Marks | Numerical | Internal assessment marks (0-40) |

### ML Models

The system compares three models:

1. **Logistic Regression**: Fast, interpretable linear model
2. **Random Forest**: Robust ensemble method with 100 trees
3. **XGBoost**: Advanced gradient boosting (if available)

**Model Selection**: Best model chosen based on weighted F1-Score

### Preprocessing

- **Categorical Encoding**: Label encoding for text features
- **Feature Scaling**: StandardScaler for numerical features
- **Target Encoding**: Binary encoding for Pass/Fail classes

## 🌐 Deployment

### Option 1: Streamlit Cloud (Recommended)

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click "New app"
4. Select your repository and branch
5. Set Main file path: `app/app.py`
6. Click "Deploy"

**Note**: Ensure `requirements.txt` includes all dependencies.

### Option 2: Render

1. Create account at [render.com](https://render.com)
2. Connect GitHub repository
3. Create new Web Service
4. Settings:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run app/app.py --server.port $PORT --server.headless true`
   - **Environment**: Python 3
5. Deploy

### Option 3: Heroku

1. Install Heroku CLI
2. Login: `heroku login`
3. Create app: `heroku create your-app-name`
4. Deploy: `git push heroku main`

The `Procfile` is already configured for Heroku.

### Option 4: Docker

```bash
# Build the image
docker build -t student-predictor:latest .

# Run the container
docker run -p 8501:8501 student-predictor:latest
```

Access at `http://localhost:8501`

### Option 5: Local Server

For production deployment on a VPS:

```bash
# Install dependencies
pip install -r requirements.txt

# Train models
python train_model.py

# Run with production settings
streamlit run app/app.py --server.port 8501 --server.headless true
```

## 📁 Project Structure

```
AI_Student_Performance_Predictor/
├── app/
│   └── app.py                 # Main Streamlit application
├── data/
│   ├── student_data.csv       # Training dataset
│   └── generate_dataset_standalone.py
├── models/
│   ├── best_model.pkl         # Trained ML model
│   ├── scaler.pkl             # Feature scaler
│   ├── label_encoders.pkl     # Categorical encoders
│   └── target_encoder.pkl     # Target encoder
├── notebooks/                 # Jupyter notebooks (optional)
├── .streamlit/
│   └── config.toml            # Streamlit configuration
├── train_model.py             # Model training script
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Docker configuration
├── Procfile                   # Heroku configuration
├── .gitignore                 # Git ignore rules
└── README.md                  # This file
```

## 🛠️ Technologies Used

- **Python 3.11+**: Core language
- **Streamlit**: Web framework
- **Scikit-learn**: ML algorithms
- **XGBoost**: Gradient boosting
- **Pandas**: Data manipulation
- **NumPy**: Numerical computing
- **Matplotlib/Seaborn**: Visualization
- **Joblib**: Model serialization

## 📊 Dataset

The model is trained on a synthetic dataset containing 600+ student records. Each record includes:

- Demographics and personal information
- Academic performance metrics
- Study habits and attendance
- Environmental factors

**Note**: For production use, train on real-world data with proper validation.

## 🔧 Configuration

### Streamlit Configuration

Edit `.streamlit/config.toml` to customize:
- Theme colors
- Server settings
- Browser behavior

### Model Training

Edit `train_model.py` to:
- Change model hyperparameters
- Add new models
- Modify evaluation metrics

## 🐛 Troubleshooting

### Model Files Not Found
```bash
python train_model.py
```

### Module Not Found Error
```bash
pip install -r requirements.txt
```

### Port Already in Use
```bash
streamlit run app/app.py --server.port 8502
```

### XGBoost Installation Issues
The app will work with Logistic Regression and Random Forest even if XGBoost fails to install.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

Created with ❤️ for educational purposes.

## 🙏 Acknowledgments

- Streamlit team for the amazing framework
- Scikit-learn for ML algorithms
- Open source community for inspiration

## 📞 Support

For issues, questions, or contributions, please open an issue on GitHub.

---

**⭐ If you find this project helpful, please give it a star!**

