# Task 3: Inheritance (Single-Level)

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        
    def get_info(self):
        print(f"Product: {self.name}, Price: ${self.price}, Category: {self.category}")


class ElectronicProduct(Product):
    def __init__(self, name, price, category, warranty_years):
        super().__init__(name, price, category)
        self.warranty_years = warranty_years
        
    def get_info(self):
        print(f"Product: {self.name}, Price: ${self.price}, Category: {self.category}, Warranty: {self.warranty_years} years")

# Create an object and demonstrate inheritance + overriding
ep = ElectronicProduct("Monitor", 300, "Electronics", 2)
ep.get_info()
