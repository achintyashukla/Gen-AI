# Task 5: Statistical Operations (Core Focus)

import numpy as np

marks = np.array([78, 85, 90, 66, 72, 88, 95, 60])

print(f"Marks: {marks}\n")

# 1. Mean
print(f"Mean: {np.mean(marks)}")

# 2. Median
print(f"Median: {np.median(marks)}")

# 3. Variance
print(f"Variance: {np.var(marks)}")

# 4. Standard Deviation
print(f"Standard Deviation: {np.std(marks)}")

# 5. Minimum & Maximum
min_mark = np.min(marks)
max_mark = np.max(marks)
print(f"Minimum: {min_mark}, Maximum: {max_mark}")

# 6. Range (max - min)
print(f"Range: {np.ptp(marks)}") # Or max_mark - min_mark
