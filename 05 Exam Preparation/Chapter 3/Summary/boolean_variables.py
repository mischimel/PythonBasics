# Boolean Variables

# Example using boolean variables as flags
has_credit_card = False  # Initializing a boolean variable as a flag

# Asking the user if they have a credit card
user_response = input("Do you have a credit card? (yes/no): ").lower()

# Updating the boolean variable based on user input
if user_response == 'yes':
    has_credit_card = True  # Setting the flag to True

# Checking the flag and displaying a message accordingly
if has_credit_card:
    print("Thank you for having a credit card.")
else:
    print("Consider applying for a credit card to enjoy exclusive benefits.")

# Another example using a boolean variable as a flag
is_authenticated = False  # Initializing another boolean variable as a flag

# Simulating a login process
user_name = input("Enter your username: ")
password = input("Enter your password: ")

# Checking login credentials and updating the flag
if user_name == 'user123' and password == 'pass456':
    is_authenticated = True  # Setting the flag to True

# Displaying a message based on authentication status
if is_authenticated:
    print("Welcome! You are now logged in.")
else:
    print("Invalid credentials. Please try again.")

# End of the program
print("Thank you for using the program.")
