
import numpy as np

#Load numerical data only from the column
data = np.genfromtxt("D:/DevOps/Edureka-AWS-course/handsOnPython/datasets_v1.0/SalaryGender.csv", delimiter=',', skip_header=1, dtype=None, encoding='utf-8')

#type of the data
print(type(data))

salary = np.array([row[0] for row in data])
gender = np.array([row[1] for row in data])
age = np.array([row[2] for row in data])
phd = np.array([row[3] for row in data])

men_with_phd = 0
women_with_phd = 0

for i in range(len(gender)):
    if gender[i] == 1 and phd[i] == 1:
        men_with_phd += 1
    elif gender[i] == 0 and phd[i] == 1:
        women_with_phd += 1

print("Number of men with PhD:", men_with_phd)
print("Number of women with PhD:", women_with_phd)