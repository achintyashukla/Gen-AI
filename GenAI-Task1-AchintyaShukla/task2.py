# Task 2: Categories (Sets)

# 1. From your products list, create a set of categories called categories_set.
# (If product names do not contain categories, create a short parallel list categories = [..] with matching length and use that.)
products = ["Laptop", "Smartphone", "Tablet", "Monitor", "Keyboard", "Mouse"]
categories = ["Electronics", "Electronics", "Electronics", "Electronics", "Accessories", "Accessories"]

categories_set = set(categories)
print("Initial categories_set:")
print(categories_set)

# 2. Demonstrate adding a new category to the set and show that duplicates are ignored.
categories_set.add("Software")
print("\nAfter adding 'Software':")
print(categories_set)

categories_set.add("Electronics") # This is a duplicate
print("\nAfter attempting to add 'Electronics' again (duplicate):")
print(categories_set)

# 3. Show how to check whether a category exists in the set (print a boolean result).
print("\nDoes 'Software' exist in the categories_set?")
print("Software" in categories_set)

print("\nDoes 'Clothing' exist in the categories_set?")
print("Clothing" in categories_set)

# Extra (optional): Show how to get the total number of unique categories using a set.
print("\nTotal number of unique categories:")
print(len(categories_set))
