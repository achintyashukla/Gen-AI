# Task 5: Mini Program: Safe Shopping Cart

cart = []

print("--- Safe Shopping Cart ---")

while True:
    user_input = input("> Enter a price (or 'q' to quit): ")
    
    if user_input.lower() == 'q':
        break
        
    try:
        price = float(user_input)
        
        if price < 0:
            raise ValueError("Price cannot be negative")
            
        cart.append(price)
        print("Item added.")
        
    except ValueError as e:
        # Catch both the float conversion error and our custom negative check error
        print(f"Invalid input: {e}")

print("\n--- Checkout ---")
print(f"Total items: {len(cart)}")
print(f"Total bill: {sum(cart)}")
