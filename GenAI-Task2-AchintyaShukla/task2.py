# Task 2: Process Multiple Orders (for loop)

orders = [1200, 2500, 800, 1750, 3000]

total_revenue = 0
discounted_orders_count = 0

print("Summary Table:")
print("Order Amount -> Discount% -> Final Amount")
print("-" * 45)

for order_amount in orders:
    # Apply discount rules
    if order_amount >= 2000:
        discount_rate = 0.15
    elif order_amount >= 1500:
        discount_rate = 0.10
    elif order_amount >= 1000:
        discount_rate = 0.07
    else:
        discount_rate = 0.00
        
    discount_amount = order_amount * discount_rate
    final_amount = order_amount - discount_amount
    
    total_revenue += final_amount
    
    if discount_rate > 0:
        discounted_orders_count += 1
        
    print(f"${order_amount:<11} -> {discount_rate*100:>2.0f}%      -> ${final_amount:.2f}")

print("-" * 45)
print(f"Total revenue after discounts: ${total_revenue:.2f}")

# Extra (optional): Print the number of orders that received a discount
print(f"Number of orders that received a discount: {discounted_orders_count}")
