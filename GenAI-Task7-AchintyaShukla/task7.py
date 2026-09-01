# Task 7: Mini Project: Simple Inventory System (OOP Only)

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        
    def __str__(self):
        return f"{self.name} (${self.price})"
        
    def __add__(self, other):
        return self.price + other.price


class Inventory:
    def __init__(self):
        self.products = []
        
    def add_product(self, product):
        self.products.append(product)
        
    def remove_product(self, name):
        for p in self.products:
            if p.name == name:
                self.products.remove(p)
                print(f"Removed {name} from inventory.")
                return
        print(f"{name} not found in inventory.")
        
    def get_total_value(self):
        total = 0
        for p in self.products:
            total += p.price
        return total
        
    def show_all_products(self):
        for p in self.products:
            print(f"- {p.name} (${p.price}) [{p.category}]")


class Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self.inventory = Inventory()
        
    def add_new_product(self):
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        category = input("Enter product category: ")
        
        new_product = Product(name, price, category)
        self.inventory.add_product(new_product)
        print(f"Added {name} to {self.store_name}.")
        
    def show_summary(self):
        print(f"\n--- {self.store_name} Summary ---")
        print(f"Total Items: {len(self.inventory.products)}")
        print(f"Total Inventory Value: ${self.inventory.get_total_value()}")
        print("Products in stock:")
        self.inventory.show_all_products()


# Test the system by:
# 1. Creating a Store object
my_store = Store("TechHub")

# 2. Adding 3 products
p1 = Product("Laptop", 1200, "Electronics")
p2 = Product("Mouse", 25, "Accessories")
my_store.inventory.add_product(p1)
my_store.inventory.add_product(p2)
# Adding 3rd product via the store's add_new_product method
my_store.add_new_product()

# 3. Showing summary
my_store.show_summary()

# 4. Using __add__ to combine prices of two products
print(f"\nCombined price of {p1.name} and {p2.name}: ${p1 + p2}")
