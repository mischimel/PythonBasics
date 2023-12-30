global_variable = 100

def access_global():
    # Accessing the global variable
    print("Global variable inside function:", global_variable)

# Calling the function
access_global()

print("Global variable outside function:", global_variable)

# Define global constant
TAX_RATE = 0.08

def calculate_total_cost(price):
    # Use global constant within the function
    tax_amount = price * TAX_RATE
    total_cost = price + tax_amount
    return total_cost

# Example usage
item_price = 100
total = calculate_total_cost(item_price)

print(f"The total cost including tax is: {total:.2f} CHF")
