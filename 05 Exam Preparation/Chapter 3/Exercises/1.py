"""
1. Day of the Week
Write a program that asks the user for a number in the range of 1 through 7.
The program should display the corresponding day of the week,
where 1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday,
5 = Friday, 6 = Saturday, and 7 = Sunday.
The program should display an error message if the user enters a number that is outside the range of 1 through 7.
"""

# User input
num = int(input("Enter a number in the range of 1 through 7: "))

if num < 1 or num > 7:
    print(f"{num} is a number that is outside the range of 1 through 7.")
elif num == 1:
    print("Monday")
elif num == 2:
    print("Tuesday")
elif num == 3:
    print("Wednesday")
elif num == 4:
    print("Thursday")
elif num == 5:
    print("Friday")
elif num == 6:
    print("Saturday")
else:                   # num == 7
    print("Sunday")