lst = [12,24,35,70,88,120,155]  
#0th,4th,5th indexes will be not there in new list
lst1 = [num for i, num in enumerate(lst) if i not in (0, 4 ,5)]   

'''
for i in range(len(lst)):
    if i not in (0, 4, 5):
        lst1.append(lst[i])
'''

print(lst1)    