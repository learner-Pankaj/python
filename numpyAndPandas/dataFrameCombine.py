import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv("D:/DevOps/Edureka-AWS-course/handsOnPython/datasets_v1.0/SalaryGender.csv")

# Select only 'Age' and 'PhD' columns
df_age_phd = df[['Age', 'PhD']]

# Delete data of people who don’t have a PhD (i.e., keep only 'Yes')
df_with_phd = df_age_phd[df_age_phd['PhD'] == 1]

# Print the resulting DataFrame
print(df_with_phd)
