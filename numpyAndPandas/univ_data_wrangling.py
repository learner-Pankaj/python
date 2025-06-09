import pandas as pd
import numpy as np

mathFile = "D:\DevOps\Edureka-AWS-course\handsOnPython\datasets_v1.0\MathScoreTerm1.csv"
physicsFile = "D:\DevOps\Edureka-AWS-course\handsOnPython\datasets_v1.0\PhysicsScoreTerm1.csv"
dsFile = "D:\DevOps\Edureka-AWS-course\handsOnPython\datasets_v1.0\DSScoreTerm1.csv"

# STEP 1: Read all 3 CSV files
math_df = pd.read_csv(mathFile)
ds_df = pd.read_csv(dsFile)
physics_df = pd.read_csv(physicsFile)

# STEP 2: Remove 'Name' and 'Ethnicity' columns
cols_to_remove = ['Name', 'Ethnicity']
math_df.drop(columns=cols_to_remove, inplace=True, errors='ignore')
ds_df.drop(columns=cols_to_remove, inplace=True, errors='ignore')
physics_df.drop(columns=cols_to_remove, inplace=True, errors='ignore')

# STEP 3: Fill missing score data with zero
math_df.fillna(0, inplace=True)
ds_df.fillna(0, inplace=True)
physics_df.fillna(0, inplace=True)

# STEP 4: Merge the three files on 'Student ID' (or 'ID')
# Ensure consistent column name
for df in [math_df, ds_df, physics_df]:
    if 'ID' in df.columns:
        df.rename(columns={'ID': 'StudentID'}, inplace=True)

# Merging all on 'StudentID'
merged_df = pd.merge(math_df, ds_df, on='StudentID')
merged_df = pd.merge(merged_df, physics_df, on='StudentID')

# STEP 5: Convert 'Sex' column M/F to 1/2
merged_df['Sex'] = merged_df['Sex'].map({'M': 1, 'F': 2})

# STEP 6: Store the final DataFrame into ScoreFinal.csv
merged_df.to_csv("ScoreFinal.csv", index=False)
print("✔ ScoreFinal.csv file has been created successfully.")


