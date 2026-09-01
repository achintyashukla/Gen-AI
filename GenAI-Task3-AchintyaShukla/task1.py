# Task 1 - Basic Function: Price After Discount

def apply_discount(price, discount_percent=5):
    # extra challenge: ensure discount never exceeds 60%
    if discount_percent > 60:
        discount_percent = 60
        
    discount_amount = (price * discount_percent) / 100
    final_price = price - discount_amount
    return final_price

print("Price with 10% discount:", apply_discount(1000, 10))
print("Price with default discount:", apply_discount(500))
print("Price with 70% discount (capped at 60%):", apply_discount(100, 70))
