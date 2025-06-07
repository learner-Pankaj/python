import numpy as np 

arr = np.random.randint(1, 21, size=(3,3))
print("Original array\n",arr)
print("\n==========\n")

#sort by 1st column
sort_by_col1 = arr[arr[:,0].argsort()]
print("Sort by 1st column\n",sort_by_col1)
print("\n==========\n")

#sort by 2nd column
sort_by_col2 = arr[arr[:,1].argsort()]
print("Sort by 2nd column\n", sort_by_col2)
print("\n==========\n")

#sort by 3rd column
sort_by_col3 = arr[arr[:,2].argsort()]
print("sort by 3rd column\n", sort_by_col3)