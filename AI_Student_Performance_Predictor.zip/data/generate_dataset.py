"""
Script to generate synthetic student performance dataset
"""
import pandas as pd
import numpy as np
from datetime import datetime

np.random.seed(42)

# Generate 500+ records
n_records = 600

# Generate student IDs
student_ids = [f'STU{i:04d}' for i in range(1, n_records + 1)]

# Generate gender
genders = np.random.choice(['Male', 'Female'], size=n_records, p=[0.52, 0.48])

# Generate age (typically 18-25 for college students)
ages = np.random.normal(21, 2, n_records).astype(int)
ages = np.clip(ages, 18, 25)

# Generate attendance percentage (0-100)
attendance_percentage = np.random.normal(75, 15, n_records)
attendance_percentage = np.clip(attendance_percentage, 0, 100).round(2)

# Generate hours studied per week
hours_studied = np.random.gamma(2, 5, n_records)
hours_studied = np.clip(hours_studied, 0, 50).round(2)

# Generate previous score (0-100)
previous_score = np.random.normal(65, 15, n_records)
previous_score = np.clip(previous_score, 0, 100).round(2)

# Generate parent education levels
parent_education = np.random.choice(
    ['High School', 'Some College', "Bachelor's", "Master's", 'PhD'],
    size=n_records,
    p=[0.25, 0.20, 0.30, 0.20, 0.05]
)

# Generate internet access
internet_access = np.random.choice(['Yes', 'No'], size=n_records, p=[0.85, 0.15])

# Generate assignments submitted (0-10)
assignments_submitted = np.random.poisson(8, n_records)
assignments_submitted = np.clip(assignments_submitted, 0, 10)

# Generate internal marks (0-40)
internal_marks = np.random.normal(28, 8, n_records)
internal_marks = np.clip(internal_marks, 0, 40).round(2)

# Generate final result based on features (with some randomness)
# Higher attendance, hours studied, previous score, and internal marks lead to better results
final_result = []
for i in range(n_records):
    score = (
        0.15 * (attendance_percentage[i] / 100) +
        0.20 * (hours_studied[i] / 50) +
        0.25 * (previous_score[i] / 100) +
        0.20 * (internal_marks[i] / 40) +
        0.10 * (assignments_submitted[i] / 10) +
        0.10 * np.random.random()  # Random factor
    )
    
    # Add bonus for internet access and higher parent education
    if internet_access[i] == 'Yes':
        score += 0.05
    if parent_education[i] in ["Master's", 'PhD']:
        score += 0.05
    
    # Determine result
    if score >= 0.6:
        final_result.append('Pass')
    else:
        final_result.append('Fail')

# Create DataFrame
df = pd.DataFrame({
    'student_id': student_ids,
    'gender': genders,
    'age': ages,
    'attendance_percentage': attendance_percentage,
    'hours_studied': hours_studied,
    'previous_score': previous_score,
    'parent_education': parent_education,
    'internet_access': internet_access,
    'assignments_submitted': assignments_submitted,
    'internal_marks': internal_marks,
    'final_result': final_result
})

# Save to CSV
df.to_csv('student_data.csv', index=False)
print(f"Dataset generated successfully with {len(df)} records!")
print(f"\nDataset shape: {df.shape}")
print(f"\nFirst few rows:")
print(df.head())
print(f"\nDataset statistics:")
print(df.describe())
print(f"\nFinal result distribution:")
print(df['final_result'].value_counts())

