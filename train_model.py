"""
Quick training script to train and save the model
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
try:
    import xgboost as xgb
    XGBOOST_AVAILABLE = True
except (ImportError, Exception) as e:
    XGBOOST_AVAILABLE = False
    print("⚠️  XGBoost not available, will use Logistic Regression and Random Forest only")
    print(f"   Error: {str(e)[:100]}")
import joblib
import os

print("🚀 Starting model training...")

# Load dataset
df = pd.read_csv('data/student_data.csv')
print(f"✅ Dataset loaded: {df.shape[0]} records")

# Preprocessing
df_processed = df.copy()
df_processed = df_processed.fillna(df_processed.mean(numeric_only=True))

# Encode categorical variables
label_encoders = {}
categorical_cols = ['gender', 'parent_education', 'internet_access']

for col in categorical_cols:
    le = LabelEncoder()
    df_processed[col] = le.fit_transform(df_processed[col])
    label_encoders[col] = le

# Encode target variable
target_encoder = LabelEncoder()
df_processed['final_result'] = target_encoder.fit_transform(df_processed['final_result'])

# Prepare features and target
X = df_processed.drop(['student_id', 'final_result'], axis=1)
y = df_processed['final_result']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
print(f"✅ Data split: Train={X_train.shape[0]}, Test={X_test.shape[0]}")

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train models
models = {
    'Logistic Regression': LogisticRegression(random_state=42, max_iter=1000),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42, max_depth=10),
}

if XGBOOST_AVAILABLE:
    try:
        models['XGBoost'] = xgb.XGBClassifier(random_state=42, eval_metric='logloss')
    except:
        print("⚠️  XGBoost failed to initialize, skipping...")

best_model = None
best_score = 0
best_name = ""

print("\n📊 Training models...")
for name, model in models.items():
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)
    f1 = f1_score(y_test, y_pred, average='weighted')
    acc = accuracy_score(y_test, y_pred)
    print(f"  {name}: Accuracy={acc:.4f}, F1-Score={f1:.4f}")
    
    if f1 > best_score:
        best_score = f1
        best_model = model
        best_name = name

print(f"\n🏆 Best Model: {best_name} (F1-Score: {best_score:.4f})")

# Save models
os.makedirs('models', exist_ok=True)
joblib.dump(best_model, 'models/best_model.pkl')
joblib.dump(scaler, 'models/scaler.pkl')
joblib.dump(label_encoders, 'models/label_encoders.pkl')
joblib.dump(target_encoder, 'models/target_encoder.pkl')

print("\n✅ Models saved successfully!")
print("   - models/best_model.pkl")
print("   - models/scaler.pkl")
print("   - models/label_encoders.pkl")
print("   - models/target_encoder.pkl")
print("\n🎉 Training complete! You can now start the app.")

