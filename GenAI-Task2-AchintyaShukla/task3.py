# Task 3: User Menu (while loop + break/continue)

orders_list = []

while True:
    print("\n--- Menu ---")
    print("1 - Add order amount to a running list")
    print("2 - Show all orders and totals after applying discounts")
    print("q - Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == 'q':
        print("Exiting program.")
        break
    elif choice == '1':
        order_input = input("Enter order amount: ")
        # Basic check for positive integer values
        if order_input.isdigit():
            order_amount = int(order_input)
            orders_list.append(order_amount)
            print("Order added successfully.")
        else:
            print("Invalid input. Please enter a positive number.")
            continue
    elif choice == '2':
        if not orders_list:
            print("No orders in the list yet.")
            continue
            
        print("\nOrder Amount -> Discount% -> Final Amount")
        total_revenue = 0
        for order_amount in orders_list:
            if order_amount >= 2000:
                discount_rate = 0.15
            elif order_amount >= 1500:
                discount_rate = 0.10
            elif order_amount >= 1000:
                discount_rate = 0.07
            else:
                discount_rate = 0.00
                
            final_amount = order_amount - (order_amount * discount_rate)
            total_revenue += final_amount
            print(f"${order_amount:<11} -> {discount_rate*100:>2.0f}%      -> ${final_amount:.2f}")
            
        print(f"Total Revenue: ${total_revenue:.2f}")
    else:
        print("Invalid choice. Please try again.")
        continue
