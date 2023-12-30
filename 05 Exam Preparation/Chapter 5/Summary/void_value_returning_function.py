# void function
def greet_user_void(name):
    """Prints a greeting message."""
    print(f"Hello, {name}!")

# Call the void function
greet_user_void("Alice")

#value-returning function
def generate_greeting_value(name):
    """Generates a greeting message and returns it."""
    greeting_message = f"Hello, {name}!"
    return greeting_message

# Call the value-returning function
greeting_result = generate_greeting_value("Bob")

# Now you can use the returned value
print(greeting_result)
