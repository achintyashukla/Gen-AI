# Task 1: Safe Division Utility

try:
    numerator = float(input("Enter numerator: "))
    denominator = float(input("Enter denominator: "))
    
    result = numerator / denominator
except ValueError:
    print("Invalid input: Please enter numerical values.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
    print(f"Result: {result}")
finally:
    print("Operation Complete")
