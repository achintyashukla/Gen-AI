# Task 1: Importing math_utils in two different ways
import math_utils
from math_utils import square

print("--- math_utils ---")
print("Add (5 + 3):", math_utils.add(5, 3))
print("Subtract (10 - 4):", math_utils.subtract(10, 4))
print("Square (6):", square(6))

# Task 2: Importing string_utils and testing
import string_utils

print("\n--- string_utils ---")
print("Capitalize:", string_utils.capitalize_words("python is fun"))
print("Reverse:", string_utils.reverse_string("hello"))
print("Word Count:", string_utils.word_count("This is a simple sentence."))

# Task 4: Importing shop_package
import shop_package.discount as disc
from shop_package.billing import calculate_total, apply_tax
# Also we can use the package level imports from __init__.py
import shop_package

print("\n--- shop_package ---")
# Using the alias 'disc'
print("Apply 10% discount to 1000:", disc.apply_discount(1000, 10))
print("Flat discount on 500:", disc.flat_discount(500))

# Using the directly imported functions
print("Calculate total for [100, 200, 300]:", calculate_total([100, 200, 300]))
print("Apply 5% tax to 1000:", apply_tax(1000))
