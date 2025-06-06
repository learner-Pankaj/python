import numpy as np

arr = np.random.randint(1, 100, size=(10, 10))

min_val = np.min(arr)
max_val = np.max(arr)

print("Random 10x10 array :: ", arr)
print("Minimum value in the array :: ", min_val)
print("Maximum value in the array :: ", max_val)