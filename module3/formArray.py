

X, Y =  map(int, input("Enter two comma separated numbers : ").split(","))

array = []

for i in range(X):
    row = []
    for j in range(Y):
        row.append(i*j)
    array.append(row)

print(array)