# Task 2: Constructor & Encapsulation

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.__price = price  # private attribute
        self.category = category
        
    def get_info(self):
        print(f"Product: {self.name}, Price: ${self.__price}, Category: {self.category}")
        
    def get_price(self):
        return self.__price
        
    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
            print(f"Price updated to ${self.__price}")
        else:
            print("Invalid price. Price must be greater than 0.")

# Test modifying price using the setter
p = Product("Smartphone", 800, "Electronics")
p.get_info()

p.set_price(850)
p.get_info()

p.set_price(-50) # Should fail
