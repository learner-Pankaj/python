

binary_num = input("Enter comma saperated 4-digit Binary number : ").split(',')

divisible_by_5 = []

for binary in binary_num:
    decimal = int(binary, 2)
    if decimal%5==0:
        divisible_by_5.append(binary)

print(",".join(divisible_by_5))
