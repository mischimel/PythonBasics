# Creating a list
my_list = [1, 2, 3]
print("my_list:", my_list)

# Using repetition operator
new_list = my_list * 3
print("new_list:", new_list)

print("my_list with for loop:")
# Iterating over a list
for item in my_list:
    print(item)

# Creating a list
my_list = [1, 2, 3]

# Indexing
print(my_list[0])  # Access the first element
print(my_list[-1])  # Access the last element

# Creating a list
my_list = [1, 2, 3]

# Using len function
list_length = len(my_list)
print("Length of the list:", list_length)

# Creating a list
my_list = [1, 2, 3]

my_list.append(6)
print(my_list)

# Creating a list
my_list = [1, 2, 3]
list2 = [4,5]

# Concatenate two lists into a new list
new_list = my_list + list2
print(new_list)

# Creating a list
my_list = [1, 2, 3, 4]

# Slicing
subset = my_list[1:3] # from index 1 to index 2 (3 ist not included)
print(subset)

# Creating a list
my_list = [1, 2, 3, 4]

# Using in operator
if 3 in my_list:
    print("3 is in the list")

# Creating a list
my_list = [1, 2, 3, 4]

my_list.reverse()
print("reverse order:", my_list)
my_list.insert(0, 8)
print("insert at index:", my_list)
my_list.sort()
print("sort list:", my_list)
my_list.remove(8)
print("remove 8:", my_list)
print(my_list)

# Creating a list
my_list = [1, 2, 3, 4]

# List comprehension to create a new list
squared_list = [x**2 for x in my_list]
print(squared_list)

# List comprehension with condition
filtered_list = [x for x in my_list if x % 2 == 0]
print(filtered_list)