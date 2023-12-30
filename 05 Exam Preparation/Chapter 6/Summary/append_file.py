# Open a file for appending
file_name = "example.txt"
file_mode = "a"
file_object = open(file_name, file_mode)

# Append data to the file
data_to_append = "This is additional data.\n"
file_object.write(data_to_append)

# Close the file
file_object.close()
