# Write a program that uses nested loops to draw this pattern:
"""
##
# #
#  #
#   #
#    #
#     #
"""

# Define the number of rows for the pattern
num_rows = 6

# Outer loop for rows
for i in range(num_rows):
    # Print #
    print("#", end="")  # prints the first # and end="" tells the program next print statement is on the same line
    # Inner loop for spaces between the #
    for j in range(i):
        print(" ", end="")
    # Print #
    print("#") # prints the last # and then tells the program to go to a new line
