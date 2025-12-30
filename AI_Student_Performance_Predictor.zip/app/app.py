"""
Streamlit Web Application for Student Performance Prediction
"""
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# Set page config
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="wide"
)

# Load model and preprocessing objects
@st.cache_resource
def load_model():
    """Load the trained model and preprocessing objects"""
    try:
        model_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'best_model.pkl')
        scaler_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'scaler.pkl')
        label_encoders_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'label_encoders.pkl')
        target_encoder_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'target_encoder.pkl')
        
        model = joblib.load(model_path)
        scaler = joblib.load(scaler_path)
        label_encoders = joblib.load(label_encoders_path)
        target_encoder = joblib.load(target_encoder_path)
        
        return model, scaler, label_encoders, target_encoder
    except FileNotFoundError as e:
        st.error(f"Model files not found. Please run the model training notebook first. Error: {e}")
        return None, None, None, None

# Load model
model, scaler, label_encoders, target_encoder = load_model()

# Main title
st.title("🎓 AI-Based Student Performance Predictor")
st.markdown("---")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Predictor", "About"])

if page == "Predictor":
    if model is None:
        st.warning("⚠️ Please train the model first by running the Jupyter notebook.")
    else:
        st.header("Enter Student Information")
        st.markdown("Fill in the details below to predict student performance.")
        
        # Create two columns for input fields
        col1, col2 = st.columns(2)
        
        with col1:
            gender = st.selectbox("Gender", ["Male", "Female"])
            age = st.number_input("Age", min_value=18, max_value=25, value=21, step=1)
            attendance_percentage = st.slider("Attendance Percentage", min_value=0.0, max_value=100.0, value=75.0, step=0.1)
            hours_studied = st.number_input("Hours Studied per Week", min_value=0.0, max_value=50.0, value=15.0, step=0.5)
            previous_score = st.slider("Previous Score", min_value=0.0, max_value=100.0, value=65.0, step=0.1)
        
        with col2:
            parent_education = st.selectbox(
                "Parent Education Level",
                ["High School", "Some College", "Bachelor's", "Master's", "PhD"]
            )
            internet_access = st.selectbox("Internet Access", ["Yes", "No"])
            assignments_submitted = st.number_input("Assignments Submitted", min_value=0, max_value=10, value=8, step=1)
            internal_marks = st.slider("Internal Marks (out of 40)", min_value=0.0, max_value=40.0, value=28.0, step=0.1)
        
        # Predict button
        if st.button("🔮 Predict Performance", type="primary"):
            try:
                # Prepare input data
                input_data = {
                    'gender': gender,
                    'age': age,
                    'attendance_percentage': attendance_percentage,
                    'hours_studied': hours_studied,
                    'previous_score': previous_score,
                    'parent_education': parent_education,
                    'internet_access': internet_access,
                    'assignments_submitted': assignments_submitted,
                    'internal_marks': internal_marks
                }
                
                # Create DataFrame
                df_input = pd.DataFrame([input_data])
                
                # Encode categorical variables
                for col, encoder in label_encoders.items():
                    if col in df_input.columns:
                        df_input[col] = encoder.transform(df_input[col])
                
                # Scale features
                df_scaled = scaler.transform(df_input)
                
                # Make prediction
                prediction = model.predict(df_scaled)[0]
                prediction_proba = model.predict_proba(df_scaled)[0]
                
                # Decode prediction
                predicted_class = target_encoder.inverse_transform([prediction])[0]
                
                # Display results
                st.markdown("---")
                st.header("📊 Prediction Results")
                
                result_col1, result_col2 = st.columns(2)
                
                with result_col1:
                    st.subheader("Predicted Result")
                    if predicted_class == "Pass":
                        st.success(f"✅ {predicted_class}")
                    else:
                        st.error(f"❌ {predicted_class}")
                
                with result_col2:
                    st.subheader("Prediction Confidence")
                    pass_prob = prediction_proba[target_encoder.transform(['Pass'])[0]] * 100
                    fail_prob = prediction_proba[target_encoder.transform(['Fail'])[0]] * 100
                    
                    st.metric("Pass Probability", f"{pass_prob:.2f}%")
                    st.metric("Fail Probability", f"{fail_prob:.2f}%")
                
                # Probability bar chart
                st.subheader("Probability Distribution")
                prob_df = pd.DataFrame({
                    'Result': ['Pass', 'Fail'],
                    'Probability': [pass_prob, fail_prob]
                })
                st.bar_chart(prob_df.set_index('Result'))
                
                # Show input summary
                with st.expander("📋 View Input Summary"):
                    st.json(input_data)
                    
            except Exception as e:
                st.error(f"An error occurred during prediction: {str(e)}")
                st.info("Please ensure all fields are filled correctly.")

elif page == "About":
    st.header("About This Project")
    st.markdown("""
    ### 🎯 Objective
    This AI-Based Student Performance Predictor uses machine learning to forecast student academic 
    performance based on various academic and personal factors.
    
    ### 📊 Features
    - **Multiple ML Models**: Logistic Regression, Random Forest, and XGBoost
    - **Comprehensive Evaluation**: Accuracy, Precision, Recall, and F1-Score metrics
    - **Data Visualization**: Correlation heatmaps, feature distributions, and model comparisons
    - **Interactive Web Interface**: Easy-to-use Streamlit application for predictions
    
    ### 🔬 Model Details
    The system trains multiple machine learning models and selects the best-performing one based on 
    F1-Score. The models are trained on features including:
    - Demographics (Gender, Age)
    - Academic Performance (Attendance, Previous Scores, Internal Marks)
    - Study Habits (Hours Studied, Assignments Submitted)
    - Environmental Factors (Parent Education, Internet Access)
    
    ### 📈 Dataset
    The model is trained on a synthetic dataset containing 600+ student records with various 
    features that influence academic performance.
    
    ### 🚀 How to Use
    1. Navigate to the **Predictor** page
    2. Fill in the student information
    3. Click **Predict Performance** to get the result
    4. View the prediction confidence and probability distribution
    
    ### 🛠️ Technologies Used
    - **Python**: Core programming language
    - **Scikit-learn**: Machine learning algorithms
    - **XGBoost**: Gradient boosting framework
    - **Pandas & NumPy**: Data manipulation
    - **Matplotlib & Seaborn**: Data visualization
    - **Streamlit**: Web application framework
    - **Joblib**: Model serialization
    
    ### 📝 Note
    This is a demonstration project using synthetic data. For real-world applications, 
    the model should be trained on actual student data and validated thoroughly.
    """)

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "AI-Based Student Performance Predictor | Built with Streamlit"
    "</div>",
    unsafe_allow_html=True
)

