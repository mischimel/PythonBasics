def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        print("Error: Division by zero.")
        return None

# Function to display the menu
def display_menu():
    print("Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Quit")

# Function to get user input for menu choice
def get_menu_choice():
    return input("Enter your choice (1-5): ")

# Main program
while True:
    # Display the menu
    display_menu()

    # Get user choice
    choice = get_menu_choice()

    # Check user choice
    if choice == '1':
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        result = add(x, y)
        print("Result:", result)
    elif choice == '2':
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        result = subtract(x, y)
        print("Result:", result)
    elif choice == '3':
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        result = multiply(x, y)
        print("Result:", result)
    elif choice == '4':
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        result = divide(x, y)
        if result is not None:
            print("Result:", result)
    elif choice == '5':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
