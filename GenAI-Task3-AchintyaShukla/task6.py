# Task 6 - Combined Utility Function

def process_prices(prices):
    # apply 10% discount to everything using map
    discounted = list(map(lambda p: p * 0.90, prices))
    
    # keep only the ones above 300 using filter
    filtered = list(filter(lambda p: p > 300, discounted))
    
    return discounted, filtered

# testing the function
my_prices = [100, 500, 900, 50, 750]
res1, res2 = process_prices(my_prices)

print("Discounted prices:", res1)
print("Filtered prices (above 300):", res2)
