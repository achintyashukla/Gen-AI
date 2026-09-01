# Task 4: File Reader with Exception Handling

filename = input("Enter a filename to open: ")

try:
    with open(filename, 'r') as f:
        print(f"--- First 3 lines of {filename} ---")
        for _ in range(3):
            line = f.readline()
            if not line:
                break
            print(line.strip())
            
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")
finally:
    print("File operation attempted.")
