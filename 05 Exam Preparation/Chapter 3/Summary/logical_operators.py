# Logical Operators

# and operator
# Example using the and operator
income = float(input("Enter your annual income: "))
years_employed = int(input("Enter the number of years employed: "))

# Using the and operator to determine loan eligibility
if income >= 30000 and years_employed >= 2:
    print("Congratulations! You qualify for a loan.")
else:
    print("Sorry, you do not qualify for a loan.")




# or operator

# Example using the or operator
age = int(input("Enter your age: "))
income = float(input("Enter your annual income: "))

# Using the or operator to determine eligibility for a discount
if age <= 18 or income <= 50000:
    print("You qualify for a discount.")
else:
    print("Sorry, you do not qualify for a discount.")

# not operator
has_credit_card = input("Do you have a credit card? (yes/no): ").lower() == 'yes'

# Using the not operator to check if the user does not have a credit card
if not has_credit_card:
    print("You are eligible for a special offer if you apply for a credit card.")
else:
    print("Thank you for being our valued customer.")

# Another example with parentheses for clarity
is_student = input("Are you a student? (yes/no): ").lower() == 'yes'
has_discount = input("Do you have a discount code? (yes/no): ").lower() == 'yes'

# Using the not operator with parentheses for clarity
if not (is_student and has_discount):
    print("You are not eligible for the student discount with a discount code.")
else:
    print("You qualify for the student discount with a discount code.")

# Checking Numeric Ranges with Logical Operators

# Example checking if a numeric value is within a specific range
x = int(input("Enter a number: "))

# Checking if x is within the range [10, 20]
if x >= 10 and x <= 20:
    print(f"{x} is within the range of 10 to 20.")
else:
    print(f"{x} is outside the range of 10 to 20.")


# Checking if x is outside the range [10, 20]
if x < 10 or x > 20:
    print(f"{x} is outside the range of 10 to 20.")
else:
    print(f"{x} is within the range of 10 to 20.")

# End of the program
print("Thank you for using the program.")

