# Task 1: Creating NumPy Arrays

import numpy as np

# 1. A 1D array of integers from 1 to 10
array_1d = np.arange(1, 11)

# 2. A 2D array of shape (3, 3) with values from 1 to 9
array_2d = np.arange(1, 10).reshape(3, 3)

# 3. A NumPy array from the list: [10, 20, 30, 40, 50]
array_list = np.array([10, 20, 30, 40, 50])

# Print Shape and Data Type of each array
print("1D Array:")
print(array_1d)
print(f"Shape: {array_1d.shape}, Data Type: {array_1d.dtype}\n")

print("2D Array:")
print(array_2d)
print(f"Shape: {array_2d.shape}, Data Type: {array_2d.dtype}\n")

print("List Array:")
print(array_list)
print(f"Shape: {array_list.shape}, Data Type: {array_list.dtype}")
