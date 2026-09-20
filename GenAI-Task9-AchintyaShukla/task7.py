# Task 7: Mini Use Case: Sales Analysis

import numpy as np

sales = np.array([1200, 1500, 900, 2000, 1800, 1700, 1600])
print(f"Daily Sales Data: {sales}\n")

# 1. Total weekly sales
total_sales = np.sum(sales)
print(f"Total weekly sales: {total_sales}")

# 2. Average daily sales
average_sales = np.mean(sales)
print(f"Average daily sales: {average_sales:.2f}")

# 3. Highest and lowest sales day (value)
highest_sales = np.max(sales)
lowest_sales = np.min(sales)
print(f"Highest sales day value: {highest_sales}")
print(f"Lowest sales day value: {lowest_sales}")

# 4. Standard deviation of sales
std_dev = np.std(sales)
print(f"Standard deviation of sales: {std_dev:.2f}")

# 5. Identify days where sales were above average
days = np.array(['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7'])
above_avg_mask = sales > average_sales

print("\nDays where sales were above average:")
for day, sale in zip(days[above_avg_mask], sales[above_avg_mask]):
    print(f"{day}: {sale}")

# Alternatively, just outputing the boolean mask or filtered sales
print(f"\nFiltered sales (above average): {sales[above_avg_mask]}")
