string1 = "Hello"
string2 = "World"
result = string1 + ", " + string2
print(result)


# change the string with concatenation
string1 = "Hello"
print("before changing:", string1)
string2 = "World"
string1 += ", " + string2 # -> string1 = string 1 + ", " + string2
print("after changing:", string1)

# Strings are immutable
my_string = "Hello"
# This will raise an exception
# my_string[0] = 'J'

