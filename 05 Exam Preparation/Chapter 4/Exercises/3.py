"""
3. Budget Analysis
Write a program that asks the user to enter the amount that he or she has budgeted for a month.
A loop should then prompt the user to enter each of his or her expenses for the month and keep a running total.
When the loop finishes, the program should display the amount that the user is over or under budget.
"""

budget = float(input("enter your budget in CHF: "))

# initialize variables
expense = 1
total = budget

while expense != 0:
    expense = float(input("enter your expense in CHF (0 to stop): "))
    total -= expense

if total == 0:
    print(f"Nothing left of budget of {budget}CHF, and no overspending.")
elif total > 0:
    print(f"You have {total}CHF left of your budget of {budget}CHF")
else:
    print(f"You have overspend you budget of {budget}CHF with this amount {(total*(-1))}CHF")

