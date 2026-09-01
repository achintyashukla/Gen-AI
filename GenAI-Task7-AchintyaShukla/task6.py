# Task 6: Magic Methods & Operator Overloading

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        
    def __str__(self):
        return f"Product({self.name}, {self.price}, {self.category})"
        
    def __add__(self, other):
        return self.price + other.price

# Test this with two product objects.
p1 = Product("Mouse", 25, "Accessories")
p2 = Product("Keyboard", 45, "Accessories")

print(str(p1))
print(f"Total combined price: ${p1 + p2}")
