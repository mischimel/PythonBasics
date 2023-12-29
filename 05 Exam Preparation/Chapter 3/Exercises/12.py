"""
12. Software Sales
A software company sells a package that retails for $99. Quantity discounts are given according to the following table:
Quantity        Discount
10–19           10%
20–49           20%
50–99           30%
100 or more     40%
Write a program that asks the user to enter the number of packages purchased.
The program should then display the amount of the discount (if any) and the total amount of the purchase after the discount.
"""

# Named constants
RETAIL_PRICE = 99

# Variables
quantity = 0
fullPrice = 0.0
discountRate = 0.0
discountAmount = 0.0
totalAmount = 0.0

# Get number
quantity = int(input('Enter the number of packages purchased: '))

# Calculate the discount rate
if quantity >= 100:
    discountRate = 0.40
elif quantity >= 50:
    discountRate = 0.30
elif quantity >= 20:
    discountRate = 0.20
elif quantity >= 10:
    discountRate = 0.10
else:
    discountRate = 0

# Calculate the full price
fullPrice = quantity * RETAIL_PRICE

# Calculate the discount amount
discountAmount = fullPrice * discountRate

# Calculate the total amount
totalAmount = fullPrice - discountAmount

# Print results
print (f'Discount received: {discountRate:.2%}')
print (f'Discount Amount: ${discountAmount:,.2f}')
print (f'Total Amount: ${totalAmount:,.2f}')
