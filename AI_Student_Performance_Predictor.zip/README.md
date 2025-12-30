# 🎓 AI-Based Student Performance Predictor

A comprehensive machine learning project that predicts student academic performance (Pass/Fail) based on various academic and personal factors.

## 📋 Table of Contents

- [Objective](#objective)
- [Project Structure](#project-structure)
- [Dataset Description](#dataset-description)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Model Performance](#model-performance)
- [Results](#results)

## 🎯 Objective

This project aims to:
- Predict student academic performance using machine learning algorithms
- Identify key factors that influence student success
- Provide an interactive web interface for easy predictions
- Compare multiple ML models to select the best performer

## 📁 Project Structure

```
AI_Student_Performance_Predictor/
├── data/
│   ├── student_data.csv          # Synthetic dataset (600+ records)
│   └── generate_dataset.py       # Script to generate dataset
├── notebooks/
│   └── model_training.ipynb       # Complete ML pipeline notebook
├── app/
│   └── app.py                     # Streamlit web application
├── models/
│   ├── best_model.pkl            # Trained best model
│   ├── scaler.pkl                # Feature scaler
│   ├── label_encoders.pkl        # Categorical encoders
│   └── target_encoder.pkl        # Target encoder
├── requirements.txt              # Python dependencies
├── README.md                     # This file
└── report.docx                   # Project report
```

## 📊 Dataset Description

The synthetic dataset contains **600 student records** with the following features:

| Feature | Description | Type |
|---------|-------------|------|
| `student_id` | Unique student identifier | String |
| `gender` | Student gender (Male/Female) | Categorical |
| `age` | Student age (18-25) | Numerical |
| `attendance_percentage` | Class attendance percentage (0-100) | Numerical |
| `hours_studied` | Hours studied per week (0-50) | Numerical |
| `previous_score` | Previous academic score (0-100) | Numerical |
| `parent_education` | Parent education level | Categorical |
| `internet_access` | Internet access availability (Yes/No) | Categorical |
| `assignments_submitted` | Number of assignments submitted (0-10) | Numerical |
| `internal_marks` | Internal assessment marks (0-40) | Numerical |
| `final_result` | Target variable (Pass/Fail) | Categorical |

### Dataset Generation

To regenerate the dataset, run:
```bash
cd data
python3 generate_dataset.py
```

## ✨ Features

### 1. Data Preprocessing
- Missing value handling
- Categorical variable encoding (Label Encoding)
- Feature normalization (StandardScaler)
- Train-test split (80/20)

### 2. Model Training
- **Logistic Regression**: Baseline linear model
- **Random Forest**: Ensemble tree-based model
- **XGBoost**: Gradient boosting model

### 3. Model Evaluation
- Accuracy, Precision, Recall, F1-Score
- Confusion Matrix
- Classification Report
- Feature Importance Analysis

### 4. Data Visualization
- Correlation heatmap
- Feature distribution plots
- Model performance comparison charts
- Confusion matrix visualization

### 5. Web Interface
- Interactive Streamlit application
- Real-time predictions
- Probability visualization
- User-friendly input forms

## 🛠️ Technologies Used

- **Python 3.8+**: Core programming language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations
- **Scikit-learn**: Machine learning algorithms and utilities
- **XGBoost**: Gradient boosting framework
- **Matplotlib**: Static plotting
- **Seaborn**: Statistical data visualization
- **Streamlit**: Web application framework
- **Joblib**: Model serialization
- **Jupyter Notebook**: Interactive development environment

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Steps

1. **Clone or download the project**
   ```bash
   cd AI_Student_Performance_Predictor
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Generate dataset (if not already present)**
   ```bash
   cd data
   python3 generate_dataset.py
   cd ..
   ```

## 🚀 Usage

### Step 1: Train the Model

Open and run the Jupyter notebook to train the models:

```bash
jupyter notebook notebooks/model_training.ipynb
```

Or run it programmatically:
```bash
jupyter nbconvert --to notebook --execute notebooks/model_training.ipynb
```

This will:
- Load and preprocess the data
- Train multiple ML models
- Compare their performance
- Save the best model and preprocessing objects

### Step 2: Run the Web Application

Start the Streamlit app:

```bash
streamlit run app/app.py
```

The application will open in your default web browser at `http://localhost:8501`

### Step 3: Make Predictions

1. Navigate to the **Predictor** page
2. Fill in the student information:
   - Demographics (Gender, Age)
   - Academic metrics (Attendance, Previous Score, Internal Marks)
   - Study habits (Hours Studied, Assignments Submitted)
   - Environmental factors (Parent Education, Internet Access)
3. Click **Predict Performance**
4. View the predicted result and confidence scores

## 📈 Model Performance

The system compares three models and selects the best one based on F1-Score:

| Model | Accuracy | Precision | Recall | F1-Score |
|-------|----------|-----------|--------|----------|
| Logistic Regression | ~0.85 | ~0.85 | ~0.85 | ~0.85 |
| Random Forest | ~0.90 | ~0.90 | ~0.90 | ~0.90 |
| XGBoost | ~0.92 | ~0.92 | ~0.92 | ~0.92 |

*Note: Actual values may vary based on the dataset and random seed.*

## 📊 Sample Outputs

### Prediction Example
- **Input**: Student with 85% attendance, 20 hours/week study time, 75 previous score
- **Output**: ✅ **Pass** (95% confidence)

### Visualization Examples
- Correlation heatmap showing relationships between features
- Feature distribution plots comparing Pass vs Fail students
- Model performance comparison bar charts
- Confusion matrix for the best model

## 🔍 Key Insights

Based on the model analysis:
1. **Previous Score** and **Internal Marks** are strong predictors
2. **Attendance Percentage** significantly impacts performance
3. **Hours Studied** shows positive correlation with success
4. **Internet Access** provides a slight advantage
5. **Parent Education** level has moderate influence

## 📝 Notes

- This project uses **synthetic data** for demonstration purposes
- For production use, train on real student data
- Model performance may vary with different datasets
- Regular retraining is recommended as new data becomes available

## 🤝 Contributing

Feel free to:
- Improve model accuracy
- Add more features
- Enhance the web interface
- Optimize the code

## 📄 License

This project is for educational purposes.

## 👨‍💻 Author

AI-Based Student Performance Predictor Project

---

**Happy Predicting! 🎓✨**

