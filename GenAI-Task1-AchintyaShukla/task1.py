# Task 1: Product Collections (Lists & Tuples)

# 1. Create a list named products containing at least 6 product names (strings).
products = ["Laptop", "Smartphone", "Tablet", "Monitor", "Keyboard", "Mouse"]

# 2. Create a tuple named sample_product that stores (product_name, price, category) for one product.
sample_product = ("Laptop", 1200.00, "Electronics")

# 3. Print the 2nd and last product from the products list.
print("2nd product:", products[1])
print("Last product:", products[-1])

# 4. Append two new product names to products and then print the updated list.
products.append("Headphones")
products.append("Webcam")
print("\nUpdated products list:")
print(products)

# Extra (optional): Convert sample_product into a list, change its price, and convert it back to a tuple.
sample_product_list = list(sample_product)
sample_product_list[1] = 1150.00
sample_product = tuple(sample_product_list)
print("\nUpdated sample_product:")
print(sample_product)
