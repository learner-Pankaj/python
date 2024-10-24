lst = [12,24,35,24,88,120,155,88,120,155]

lst1 = []
for value in lst:
    
    if value in lst1:
        continue
    else :
        lst1.append(value)

print(lst1)
    
