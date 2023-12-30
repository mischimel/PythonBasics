# This program uses a loop to display a
# table showing the numbers.txt 1 through 10
# and their squares.

# Print the table headings.
print('Number\tSquare')
print('--------------')

# Print the numbers.txt 1 through 10
# and their squares.
for number in range(1, 11): # 1 is included, 11 is not included
    square = number**2 # ** is exponent
    print(f'{number}\t\t{square}') # for the format


# Print the numbers.txt 1 through 10, but only for odd numbers.txt
# and their squares.
for number in range(1, 11,2): # 1 is included, 11 is not included
    square = number**2 # ** is exponent
    print(f'{number}\t\t{square}') # for the format