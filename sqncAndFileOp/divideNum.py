num = [12,24,35,70,88,120,155]
lst = [val for val in num if val%5 != 0 or val%7 != 0]
print(lst)

'''
result = []
for val in num:
    if ((val%5!=0) or (val%7!=0)):
        result.append(val)

print(result)
'''
