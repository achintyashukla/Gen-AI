# Task 7 - Mini Problem: Menu Using Functions

def add_price(prices_list, price):
    prices_list.append(price)

def get_average_price(prices_list):
    if len(prices_list) == 0:
        return 0
    total = sum(prices_list)
    return total / len(prices_list)

def get_max_price(prices_list):
    if len(prices_list) == 0:
        return 0
    return max(prices_list)

# starting with an empty list
prices_list = []

while True:
    print("\n--- Menu ---")
    print("1 -> Add price")
    print("2 -> Show average price")
    print("3 -> Show highest price")
    print("q -> Quit")
    
    choice = input("Enter choice: ")
    
    if choice == 'q':
        print("Goodbye!")
        break
    elif choice == '1':
        new_price = float(input("Enter a new price: "))
        add_price(prices_list, new_price)
        print("Price added.")
    elif choice == '2':
        avg = get_average_price(prices_list)
        print("Average price is:", avg)
    elif choice == '3':
        highest = get_max_price(prices_list)
        print("Highest price is:", highest)
    else:
        print("Invalid choice, please try again.")
