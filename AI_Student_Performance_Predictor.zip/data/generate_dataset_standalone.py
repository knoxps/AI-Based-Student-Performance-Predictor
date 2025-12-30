"""
Standalone script to generate synthetic student performance dataset
Uses only standard library (no external dependencies)
"""
import csv
import random

random.seed(42)

# Generate 600 records
n_records = 600

# Education levels
education_levels = ['High School', 'Some College', "Bachelor's", "Master's", 'PhD']
education_weights = [0.25, 0.20, 0.30, 0.20, 0.05]

def generate_student(i):
    """Generate a single student record"""
    student_id = f'STU{i:04d}'
    gender = random.choice(['Male', 'Female'])
    age = max(18, min(25, int(random.gauss(21, 2))))
    
    # Attendance (normal distribution, clipped to 0-100)
    attendance = max(0, min(100, round(random.gauss(75, 15), 2)))
    
    # Hours studied (gamma-like distribution, clipped to 0-50)
    hours_studied = max(0, min(50, round(random.gammavariate(2, 5), 2)))
    
    # Previous score (normal distribution, clipped to 0-100)
    previous_score = max(0, min(100, round(random.gauss(65, 15), 2)))
    
    # Parent education
    parent_education = random.choices(education_levels, weights=education_weights)[0]
    
    # Internet access
    internet_access = random.choices(['Yes', 'No'], weights=[0.85, 0.15])[0]
    
    # Assignments submitted (Poisson-like, clipped to 0-10)
    assignments_submitted = max(0, min(10, int(random.expovariate(0.125) * 8)))
    
    # Internal marks (normal distribution, clipped to 0-40)
    internal_marks = max(0, min(40, round(random.gauss(28, 8), 2)))
    
    # Calculate final result based on features
    score = (
        0.15 * (attendance / 100) +
        0.20 * (hours_studied / 50) +
        0.25 * (previous_score / 100) +
        0.20 * (internal_marks / 40) +
        0.10 * (assignments_submitted / 10) +
        0.10 * random.random()
    )
    
    # Add bonus for internet access and higher parent education
    if internet_access == 'Yes':
        score += 0.05
    if parent_education in ["Master's", 'PhD']:
        score += 0.05
    
    # Determine result
    final_result = 'Pass' if score >= 0.6 else 'Fail'
    
    return [
        student_id, gender, age, attendance, hours_studied, previous_score,
        parent_education, internet_access, assignments_submitted, internal_marks, final_result
    ]

# Generate data
data = []
data.append([
    'student_id', 'gender', 'age', 'attendance_percentage', 'hours_studied',
    'previous_score', 'parent_education', 'internet_access', 'assignments_submitted',
    'internal_marks', 'final_result'
])

for i in range(1, n_records + 1):
    data.append(generate_student(i))

# Write to CSV
with open('student_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)

print(f"Dataset generated successfully with {n_records} records!")
print(f"File saved as: student_data.csv")

