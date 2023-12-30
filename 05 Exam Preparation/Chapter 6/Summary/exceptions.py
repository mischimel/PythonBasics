# Example 1: Preventing exceptions with input validation
print("Example 1: Preventing exceptions with input validation")
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid input. Please enter a valid integer for age.")

# Example 2: Handling multiple exceptions
print("Example 2: Handling multiple exceptions")
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Invalid input. Please enter a valid integer.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
except Exception as err:
    print(f"An unexpected error occurred: {err}")
else:
    print("No exceptions were raised.")

# Example 3: Using the else clause
# The else block is executed only if there are no exceptions
print("Example 3: Using the else clause")
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
except ValueError:
    print("Invalid input. Please enter valid integers.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print(f"The result of {num1} divided by {num2} is: {result}")


# Example 4: Using the finally clause
# The finally block is executed no matter what, whether an exception occurred or not.
print("Example 4: Using the finally clause")
"""
try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    print("Closing the file.")
    file.close()
"""

# Example 5: Displaying an exception's default error message
print("Example 5: Displaying an exception's default error message")
try:
    value = int("abc")
except ValueError as err:
    print(f"Error: {err}")

# Example 6: unhandled exception
print("Example 6: unhandled exception")
#result = 10 / 0
