def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2] #this is list comprehension
    '''
    lst3=[]
    for value in lst1:
        if value in lst2:
            lst3.append(value)
    '''
    return lst3

lst1 = [1,3,6,78,35,55]
lst2 = [12,24,35,24,88,120,155]

print(intersection(lst1, lst2))