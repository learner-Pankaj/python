import math

C, H = 50, 30
D = input("Enter number in a comma separated sequence ").split(",")

result = []

for val in D:
    d = int(val)
    Q = math.sqrt((2*C*d)/H)
    result.append(round(Q))

print(",".join(map(str, result)))