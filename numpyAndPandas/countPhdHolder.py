import pandas as pd

# Load the CSV file
df = pd.read_csv("D:/DevOps/Edureka-AWS-course/handsOnPython/datasets_v1.0/SalaryGender.csv")

total_phd = df[df['PhD'] == 1].shape[0]

print("Total number of person has phd degree = ",total_phd)