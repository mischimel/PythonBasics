# Open a file for reading
file_name = "example.txt"
file_mode = "r"
file_object = open(file_name, file_mode)

# Read lines using a while loop
line = file_object.readline()
while line != '':
    print("Line:", line.strip())  # Remove newline characters
    line = file_object.readline()

# Close the file
file_object.close()

# Open a file for reading
file_name = "example.txt"
file_mode = "r"
file_object = open(file_name, file_mode)

# Read lines using a for loop
for line in file_object:
    print("Line:", line.strip())  # Remove newline characters

# Close the file
file_object.close()
