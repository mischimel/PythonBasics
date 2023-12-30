"""
1. Total Sales
Design a program that asks the user to enter a store’s sales for each day of the week.
The amounts should be stored in a list. Use a loop to calculate the total sales for the week and display the result.
"""
def main():

    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # instantiate variables
    sales = []
    total = 0

    # receive user input
    for day in week:
        daily_sale = float(input(f"Please enter the sales in CHF for {day}: "))
        total += daily_sale

    print(f"total of sales for this week is {total} CHF")

if __name__ == '__main__':
    main()