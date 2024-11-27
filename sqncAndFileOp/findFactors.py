
#find the factors of a number

number = int(input("Enter a number so we can see the factorial of it. :: "))
n = number
for num in range(1, number+1):
    if n%num==0:
        print(num)
    else:
        continue
