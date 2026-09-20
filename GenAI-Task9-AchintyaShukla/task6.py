# Task 6: Percentiles & Sorting

import numpy as np

marks = np.array([78, 85, 90, 66, 72, 88, 95, 60])
print(f"Original Marks: {marks}")

# 1. Sort the array
sorted_marks = np.sort(marks)
print(f"Sorted Marks: {sorted_marks}\n")

# 2. Find Percentiles
print(f"25th Percentile: {np.percentile(marks, 25)}")
print(f"50th Percentile (Median): {np.percentile(marks, 50)}")
print(f"75th Percentile: {np.percentile(marks, 75)}\n")

# 3. Count how many students scored above the average marks
average = np.mean(marks)
above_average_count = np.sum(marks > average)
print(f"Average Mark: {average}")
print(f"Students scoring above average: {above_average_count}")
