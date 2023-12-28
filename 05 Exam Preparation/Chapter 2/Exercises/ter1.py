"""
ter1. Converting a decimal number into a binary number
Write a program that asks the user for an integer and converts this integer into a binary number.
Example: 10 -> 00001010
Hint: There exist different ways for implementation.
"""

# Get the decimal value
dec_number = int(input('Enter a decimal number: '))

binary_number = f'{dec_number:08b}'
print(binary_number)
binary_number = f'{dec_number:b}'
print(binary_number)