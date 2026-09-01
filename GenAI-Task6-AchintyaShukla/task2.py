# Task 2: Bill Calculator with Error Handling

prices = [120, 350, 'abc', 500, -200, 800]
total = 0

for price in prices:
    try:
        # Check if the price is a number
        if not isinstance(price, (int, float)):
            raise TypeError("Value is not a number")
        
        # Check if the price is negative
        if price < 0:
            raise ValueError("Negative price not allowed")
            
        total += price
        
    except TypeError as e:
        print(f"Skipping invalid item: {e}")
    except ValueError as e:
        print(f"Skipping invalid price: {e}")

print(f"\nFinal Total: {total}")
