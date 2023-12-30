def add_numbers(a, b):
    result = a + b
    print("Sum:", result)

# Calling the function with arguments
add_numbers(5, 7)


def double(number):
    result = number * 2
    return result

x = 5
double(x) # no print, as the function only returns value, but not prints it
print("double(x):",double(x)) # this prints it
print("x: ", x) # check what the value of x is
x = double(x) # assign new value to x, so the original value of 5 is "lost"
print("x: ", x)