# Task 1: Basic Class & Object Creation

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        
    def get_info(self):
        print(f"Product: {self.name}, Price: ${self.price}, Category: {self.category}")
        
    def apply_discount(self, percent):
        discount_amount = self.price * (percent / 100)
        return self.price - discount_amount

# Create two objects and call get_info()
p1 = Product("Laptop", 1200, "Electronics")
p2 = Product("Desk Chair", 150, "Furniture")

p1.get_info()
p2.get_info()

# Test extra method
print(f"Discounted price for {p1.name}: ${p1.apply_discount(10)}")
