import numpy as np

arr = np.array(
    [np.nan, 1, 2, np.nan, 3, 4, 5]
)

print("Without removing NaN from the array : ", arr)

filterNaN = arr[~np.isnan(arr)]

print("After removing NaN from the Array")
print(filterNaN)