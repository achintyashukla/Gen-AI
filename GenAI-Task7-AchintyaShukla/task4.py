# Task 4: Polymorphism

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def get_info(self):
        print(f"Product: {self.name}, Price: ${self.price}")

class Laptop(Product):
    def get_info(self):
        print(f"[LAPTOP] Model: {self.name} | Cost: ${self.price}")

class Mobile(Product):
    def get_info(self):
        print(f"[MOBILE] Device: {self.name} | Price Tag: ${self.price}")

# Write a loop that iterates over objects of Laptop and Mobile and calls get_info()
devices = [
    Laptop("MacBook Pro", 2000),
    Mobile("iPhone 14", 999),
    Laptop("Dell XPS", 1500)
]

for device in devices:
    device.get_info()
