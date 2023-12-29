"""
8. Sum of Numbers
Write a program with a loop that asks the user to enter a series of positive numbers.
The user should enter a negative number to signal the end of the series.
After all the positive numbers have been entered; the program should display their sum.
"""

num = int(input("please enter a number: "))

# initialize variables
sum = 0

while num >= 0:
    sum += num
    num = int(input("please enter a number (negative number to stop): "))

print(f"The sum of all the entered numbers is {sum}")