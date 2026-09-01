# Task 4 - Using map(): Apply GST to List of Prices

prices = [100, 250, 400, 1200, 50]

gst = lambda price: price + (0.18 * price)

# using map to apply gst to all prices
prices_with_gst = list(map(gst, prices))

print("Original prices:", prices)
print("Prices after GST:", prices_with_gst)
