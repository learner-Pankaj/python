
def factorial(num):
    if num == 0:
        return 1
    return num*factorial(num-1)

n = 8
print(f"factorial of the number {n} is {factorial(n)}")

