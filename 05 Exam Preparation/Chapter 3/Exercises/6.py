"""
6. Magic Dates
The date June 10, 1960, is special because when it is written in the following format,
the month times the day equals the year: 6/10/60
Design a program that asks the user to enter a month (in numeric form), a day, and a two-digit year.
The program should then determine whether the month times the day equals the year.
If so, it should display a message saying the date is magic.
Otherwise, it should display a message saying the date is not magic.
"""

month = int(input("enter a month: "))
day = int(input("enter a day: "))
year = int(input("enter a two digit year: "))

# Check date isvalid
if month > 12 or month < 1:
    print('Error: invalid month input')
elif day > 31 or day < 1:
    print('Error: invalid day input')
elif year > 99 or year < 0:
    print('Error: invalid year input')
# date is valid
else:
    if month*day == year:
        print(f"the date {month}/{day}/{year} is a magic date")
    else:
        print(f"the date {month}/{day}/{year} is not a magic date")
