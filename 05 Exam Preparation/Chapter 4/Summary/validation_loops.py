# Validation loops

# Example of input validation using a while loop
while True:
    try:
        user_input = float(input("Enter a positive number: "))

        if user_input > 0:
            break  # Break out of the loop if input is a positive number
        else:
            print("Invalid input. Please enter a positive number.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# Process the valid input
square_root = user_input ** 0.5
print(f"The square root of {user_input} is {square_root:.2f}")

# End of the program
print("End of the loop.")
