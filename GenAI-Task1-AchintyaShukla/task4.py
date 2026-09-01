# Task 4: Combined Operations

# Let's redefine the lists and dictionaries from previous tasks for this script
products = ["Laptop", "Smartphone", "Tablet", "Monitor", "Keyboard", "Mouse"]
categories = ["Electronics", "Electronics", "Electronics", "Electronics", "Accessories", "Accessories"]
price_dict = {
    "Laptop": 1200.0,
    "Smartphone": 800.0,
    "Tablet": 400.0,
    "Monitor": 250.0,
    "Keyboard": 50.0,
    "Mouse": 30.0
}

# 1. Using the products list and price_dict, create a list of tuples named catalog 
# where each tuple is (product_name, price, category).
catalog = []
for i in range(len(products)):
    product_name = products[i]
    category = categories[i]
    # Fetching price from price_dict (using 0.0 as default if not found)
    price = price_dict.get(product_name, 0.0) 
    catalog.append((product_name, price, category))

print("Catalog:")
for item in catalog:
    print(item)

# 2. From catalog, create a new dictionary category_to_products that maps 
# each category to a list of product names in that category.
category_to_products = {}
for product_name, price, category in catalog:
    if category not in category_to_products:
        category_to_products[category] = []
    category_to_products[category].append(product_name)

print("\nDictionary category_to_products:")
print(category_to_products)

# 3. Print all products that belong to the category that has the maximum number of products.
max_category = None
max_count = 0

for category, product_list in category_to_products.items():
    if len(product_list) > max_count:
        max_count = len(product_list)
        max_category = category

print(f"\nThe category with the maximum number of products is: '{max_category}' with {max_count} products.")
print(f"Products in this category: {category_to_products[max_category]}")
