"""
8. Tip, Tax, and Total
Write a program that calculates the total amount of a meal purchased at a restaurant.
The program should ask the user to enter the charge for the food, then calculate the amounts of a 18 percent tip
and 7 percent sales tax. Display each of these amounts and the total.
"""

# input from customer
food_costs = float(input("Please enter the charge in CHF for the food: "))

TIP = 0.18
SALES_TAX = 0.07

print(f"When the food costs {food_costs} CHF \n"
      f"then the 18% tip should be {food_costs*TIP:.2f} CHF \n"
      f"and the 7% sales tax is {food_costs*SALES_TAX:.2f} CHF \n"
      f"the total is the {food_costs+(food_costs*TIP)+(food_costs*SALES_TAX):.2f} CHF.")