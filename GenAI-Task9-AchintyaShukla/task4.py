# Task 4: Aggregation Operations

import numpy as np

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Data Array:")
print(data)
print()

# 1. Row-wise sum
print(f"Row-wise sum: {np.sum(data, axis=1)}")

# 2. Column-wise sum
print(f"Column-wise sum: {np.sum(data, axis=0)}")

# 3. Minimum value
print(f"Minimum value: {np.min(data)}")

# 4. Maximum value
print(f"Maximum value: {np.max(data)}")

# 5. Overall mean
print(f"Overall mean: {np.mean(data)}")
