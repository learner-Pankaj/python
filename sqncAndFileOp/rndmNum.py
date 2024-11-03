import random

flag = True
lst = []
while flag:
    num = random.randint(1, 1000)
    if num%5==0 and num%7==0:
        lst.append(num)
    if len(lst)==5:
        flag = False

print(lst)
