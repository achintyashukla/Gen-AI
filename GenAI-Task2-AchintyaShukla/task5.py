# Task 5: Loop Control with Conditions (break & continue)

daily = [200, 150, 0, 400, 50, -1, 300]

total_sales = 0

for sale in daily:
    if sale == -1:
        print("Corrupted data encountered (-1). Stopping processing.")
        break
    elif sale == 0:
        print("No sales for this day. Skipping.")
        continue
    elif sale > 0:
        total_sales += sale
        print(f"Added ${sale}. Running total: ${total_sales}")
    else:
        # In case of other negative values
        print(f"Invalid sale amount: {sale}. Skipping.")
        continue

print(f"\nFinal total sales processed: ${total_sales}")
