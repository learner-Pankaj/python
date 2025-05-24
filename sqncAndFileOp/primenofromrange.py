
# print prime number between a range

#range
lower = 900
upper = 1000

print("Search for prime numbers between 600 and 700")

for num in range(lower, upper):
    for i in range(2, num):
        if num%i==0:
            break
    else:
        print(num)
        
