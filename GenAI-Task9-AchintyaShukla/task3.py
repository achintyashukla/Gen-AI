# Task 3: Important NumPy Mathematical Formulas

import numpy as np

values = np.array([2, 4, 6, 8, 10])

print(f"Original Values: {values}\n")

# 1. Square root of each element
print(f"Square Root: {np.sqrt(values)}\n")

# 2. Exponential of each element
print(f"Exponential: {np.exp(values)}\n")

# 3. Natural logarithm of each element
print(f"Natural Logarithm: {np.log(values)}\n")

# 4. Sum of all elements
print(f"Sum of all elements: {np.sum(values)}\n")

# 5. Cumulative sum of elements
print(f"Cumulative Sum: {np.cumsum(values)}")
