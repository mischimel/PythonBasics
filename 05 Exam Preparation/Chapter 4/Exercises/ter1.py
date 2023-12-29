"""
ter1. Prime number
Write a program that reads an integer from the console and determines if the integer is a prime number or not.
"""

number = int(input("enter a number: "))

# 1 is not being a prime number, is ignored
if number > 1:
    for i in range(2, int(number / 2) + 1):
        if (number % i) == 0:
            print(number, "is NOT a prime number.")
            break
    else:
        print(number, "is a prime number.")

else:
    print(number, "is NOT a prime number.")