import numpy as np

data = np.genfromtxt("D:/Edureka-AWS-course/handsOnPython/datasets_v1.0/SalaryGender.csv", delimiter=',', skip_header=1, dtype=None, encoding='utf-8')

salary = np.array([row[0] for row in data])
gender = np.array([row[1] for row in data])
age = np.array([row[2] for row in data])
phd = np.array([row[3] for row in data])

print("salary :: ", salary)
print("gender :: ", gender)
print("age :: ", age)
print("phd :: ", phd)