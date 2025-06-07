import numpy as np

arr = np.random.randint(1,10,size=(2,3,4,5))
print("original shape of the matrix",arr.shape)
print("\n",arr)

result = np.sum(arr, axis=(-2,-1))
print("\n Result \n",result)
print("\nshape after sum", result.shape)