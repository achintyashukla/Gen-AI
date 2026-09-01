# Task 5 - Using filter(): Filter Expensive Products

prices = [100, 250, 400, 1200, 50, 2000, 850]

# filter prices greater than 500
expensive = list(filter(lambda p: p > 500, prices))

# filter prices less than or equal to 500
cheap = list(filter(lambda p: p <= 500, prices))

print("Prices greater than 500:", expensive)
print("Prices less than or equal to 500:", cheap)
