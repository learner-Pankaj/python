

arr = list(range(11))
for num in range(len(arr)):
    if 3 <= arr[num] <= 9:
        arr[num] = -arr[num]

print("modified array :: ", arr)