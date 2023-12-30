# Open the file for reading
file_name = "example.txt"
file_mode = "r"
file_object = open(file_name, file_mode)

# Read the entire file contents
file_contents = file_object.read()
print("File Contents (with newline):\n" + file_contents)

# Remove exclamation marks using rstrip
# The rstrip method removes the characters at the right end of each line.
# As the line ends with \n, the \n must be with the ! in the method.
file_contents_stripped = file_contents.rstrip("!\n")
print("File Contents (stripped '!'):\n" + file_contents_stripped)
print("no space between this line and the line above, as '\ n' got removed")

# Close the file
file_object.close()


# Open the file for reading
file_name = "numbers.txt"
file_mode = "r"
file_object = open(file_name, file_mode)

numbers = []
# Read the entire file contents into a list of integers
for line in file_object:
    num = int(line.strip()) # convert into int and remove the \n
    numbers.append(num) # add number to list

print(numbers)

# print the type of the items of the list
for item in numbers:
    print(type(item))

# Close the file
file_object.close()