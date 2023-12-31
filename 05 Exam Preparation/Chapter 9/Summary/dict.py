# Creating a Dictionary
# Using curly braces
my_dict = {'key1': 'value1', 'key2': 'value2'}

# Using the dict() function
another_dict = dict(key1='value1', key2='value2')

# Retrieving a Value from a Dictionary:
# Accessing a value using a key
value = my_dict['key1']
print(value)
# Using the get method with a default value
value = my_dict.get('key3', 'Default')
print(value)

my_dict = {'key1': 'value1', 'key2': 'value2'}
# Adding a new key-value pair
my_dict['key3'] = 'value3'
# Deleting a key-value pair
del my_dict['key2']
print(my_dict)


my_dict = {'key1': 'value1', 'key2': 'value2'}
# Using a for loop to iterate over keys
for key in my_dict:
    print(key, my_dict[key])

# Using items method to iterate over key-value pairs
for key, value in my_dict.items():
    print(key, value)

