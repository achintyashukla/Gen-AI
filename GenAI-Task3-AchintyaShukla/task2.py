# Task 2 - Recursive Function: Factorial Utility

def factorial(n):
    if n < 0:
        print("Error: cannot calculate factorial for negative numbers")
        return None
    
    # handle the edge cases
    if n == 0 or n == 1:
        return 1
        
    # recursive call
    return n * factorial(n - 1)

print("factorial(5) is", factorial(5))
print("factorial(0) is", factorial(0))
print("factorial(-3) result:")
factorial(-3)
