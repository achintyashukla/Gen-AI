# Task 1: Discount Rules (if / elif / else)

user_input = input("Enter the order amount: ")

# 3. Ensure you convert input to a number and handle non-numeric input
# We use .isdigit() to check if it's an integer.
if not (user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit())):
    print("Error: Please enter a valid integer.")
else:
    order_amount = int(user_input)
    
    if order_amount < 0:
        print("Error: Order amount cannot be negative.")
    else:
        # 2. Apply discount rules
        if order_amount >= 2000:
            discount_rate = 0.15
        elif order_amount >= 1500:
            discount_rate = 0.10
        elif order_amount >= 1000:
            discount_rate = 0.07
        else:
            discount_rate = 0.00
            
        discount_amount = order_amount * discount_rate
        subtotal = order_amount - discount_amount
        
        print(f"Original amount: ${order_amount:.2f}")
        print(f"Discount applied: {discount_rate*100:.0f}%")
        print(f"Subtotal after discount: ${subtotal:.2f}")
        
        # Extra (optional): Add tax (fixed 5%) after discount
        tax_rate = 0.05
        tax_amount = subtotal * tax_rate
        final_total = subtotal + tax_amount
        
        print(f"Tax (5%): ${tax_amount:.2f}")
        print(f"Final total: ${final_total:.2f}")
