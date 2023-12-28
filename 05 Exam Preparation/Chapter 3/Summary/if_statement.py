# if statement

# set condition to true by default
condition = True

if condition:
    print("condition = true") # will be printed

# set condition to false by default
condition = False

if condition:
    print("condition is true") # will not be printed

# Boolean Expressions and Relational Operators

x = 5
y = 10

# Using > relational operator
if x > y:
    print(f"{x} is greater than {y}")
else:
    print(f"{x} is not greater than {y}")

# Using == relational operator
if x == y:
    print(f"{x} and {y} are equal")
else:
    print(f"{x} and {y} are not equal")

# Using a block inside another block
# Outer block
if x > y:
    print(f"{x} is greater than {y}")
    # Inner block
    if x != y:
        print(f"{x} and {y} are not equal")

