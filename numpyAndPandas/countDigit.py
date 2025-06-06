# Input list of integers
numbers = [0, 5, 4, 0, 4, 4, 3, 0, 0, 5, 2, 1, 1, 9]

# Create a list of 10 zeros (to count from 0 to 9)
count = [0] * 10

# Loop through each number in the list
for num in numbers:
    count[num] += 1  # Increase count at that index

# Print the result
print(count)
