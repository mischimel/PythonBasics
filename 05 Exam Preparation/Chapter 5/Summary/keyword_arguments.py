def print_info(name, age, city):
    print("Name:", name)
    print("Age:", age)
    print("City:", city)

# Using positional arguments
print_info("Alice", 25, "Wonderland")

# Using keyword arguments (order is not important)
print_info(age=30, city="Bobsville", name="Bob")

# Mixing positional and keyword arguments
print_info("Charlie", city="Charlottetown", age=35)
