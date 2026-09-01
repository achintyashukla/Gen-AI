# Task 3: Custom Exception: Age Validator

def check_age(age):
    if age < 1 or age > 120:
        raise ValueError("Age must be between 1 and 120")
    print("Age is valid.")

try:
    user_age_str = input("Enter your age: ")
    user_age = int(user_age_str)
    check_age(user_age)
except ValueError as e:
    # This will catch both the int() conversion error and our custom raise ValueError
    print(f"Error: {e}")
