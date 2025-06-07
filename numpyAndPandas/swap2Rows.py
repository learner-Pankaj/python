import numpy as np

arr = np.random.randint(1, 101, size=(3,3))
print("Original Array\n",arr)
arr[[0,2]] = arr[[2,0]]
print("\n Array after swapping row 1 and row 3: \n", arr)
