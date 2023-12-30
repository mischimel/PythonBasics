# Open a file for writing
file_name = "example.txt"
file_mode = "w"
file_object = open(file_name, file_mode)

# Write data to the file
data_to_write = "Hello, World!\n"
file_object.write(data_to_write)

# Close the file
file_object.close()

# Open a file for writing
file_name = "numbers.txt"
file_mode = "w"
file_object = open(file_name, file_mode)

# Write data to the file
numbers = [1, 2, 3, 4]
numbers_as_string = []
# loop through list, convert in string, and add to list
for num in numbers:
    numbers_as_string.append(str(num))

# loop through string list to add data to the file with a new line
for num_str in numbers_as_string:
    file_object.write(num_str + '\n')

# Close the file
file_object.close()
