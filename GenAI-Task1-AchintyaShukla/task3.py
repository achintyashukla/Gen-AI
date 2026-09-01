# Task 3: Product Pricing (Dictionaries)

# 1. Create a dictionary price_dict where keys are product names and values are prices (integers or floats). Include at least 6 entries.
price_dict = {
    "Laptop": 1200.0,
    "Smartphone": 800.0,
    "Tablet": 400.0,
    "Monitor": 250.0,
    "Keyboard": 50.0,
    "Mouse": 30.0
}
print("Initial price_dict:")
print(price_dict)

# 2. Write small code blocks to:
# - Add a new product with price to price_dict.
price_dict["Headphones"] = 150.0
print("\nAfter adding a new product (Headphones):")
print(price_dict)

# - Update the price of an existing product.
price_dict["Smartphone"] = 750.0
print("\nAfter updating the price of Smartphone:")
print(price_dict)

# - Remove a product by name (handle the case when the product does not exist).
product_to_remove = "Tablet"
if product_to_remove in price_dict:
    del price_dict[product_to_remove]
    print(f"\nAfter removing {product_to_remove}:")
    print(price_dict)

# Handling a non-existent product
non_existent_product = "Smartwatch"
if non_existent_product in price_dict:
    del price_dict[non_existent_product]
else:
    print(f"\nCould not remove '{non_existent_product}' as it does not exist in the dictionary.")

# 3. Print the average price of all products (use only dictionary operations and basic arithmetic).
total_price = sum(price_dict.values())
number_of_products = len(price_dict)
average_price = total_price / number_of_products
print("\nAverage price of all products:")
print(f"${average_price:.2f}")

# Extra (optional): Print the product with both the maximum and minimum prices.
product_max_price = max(price_dict, key=price_dict.get)
product_min_price = min(price_dict, key=price_dict.get)

print(f"\nProduct with maximum price: {product_max_price} (${price_dict[product_max_price]})")
print(f"Product with minimum price: {product_min_price} (${price_dict[product_min_price]})")
