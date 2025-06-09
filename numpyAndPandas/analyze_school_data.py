import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# PHASE 1 – Read and Describe the Data
file_path = "D:\DevOps\Edureka-AWS-course\handsOnPython\datasets_v1.0\middle_tn_schools.csv" 
df = pd.read_csv(file_path)

print("First 5 rows of the dataset:")
print(df.head())
print("\nSummary statistics:")
print(df.describe())
print("\nMissing values in each column:")
print(df.isnull().sum())

# PHASE 2 – Group by School Rating
print("\nGrouped description of 'reduced_lunch' by 'school_rating':")
grouped = df[['school_rating', 'reduced_lunch']].groupby('school_rating')
print(grouped.describe())

# PHASE 3 – Correlation between reduced_lunch and school_rating
correlation = df['reduced_lunch'].corr(df['school_rating'])
print(f"\nCorrelation between reduced_lunch and school_rating: {correlation:.2f}")

# PHASE 4 – Scatter Plot
plt.figure(figsize=(8,6))
plt.scatter(df['reduced_lunch'], df['school_rating'], color='blue', alpha=0.6)
plt.title("Reduced Lunch % vs School Rating")
plt.xlabel("Reduced Lunch (%)")
plt.ylabel("School Rating")
plt.grid(True)
plt.tight_layout()
plt.show()

# PHASE 5 – Correlation Matrix Heatmap
# Select relevant columns (you can add/remove depending on your dataset)
columns_to_check = ['school_rating', 'reduced_lunch', 'stu_teach_ratio', 'size']
selected_df = df[columns_to_check]

corr_matrix = selected_df.corr()

plt.figure(figsize=(8,6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
plt.title("Correlation Matrix")
plt.tight_layout()
plt.show()
