import numpy as np

# Create a random vector (1D array) of size 30 with values between 0 and 1
vector = np.random.randint(1,30, size=30)

# Calculate the mean
mean_value = np.mean(vector)

# Print the vector and the mean
print("Random Vector:\n", vector)
print("\nMean Value:", mean_value)
