# The if-elif-else Statement
# Example of a nested decision structure
income = float(input("Enter your annual income: "))
years_employed = int(input("Enter the number of years employed: "))

# Nested if statements to determine loan eligibility
if income >= 30000:
    if years_employed >= 2:
        print("Congratulations! You qualify for a loan.")
    else:
        print("Sorry, you need to be employed for at least two years.")
else:
    print("Sorry, your income is below the required threshold.")


# Example of the if-elif-else statement
score = int(input("Enter your exam score (max is 100): "))

# if-elif-else statement to determine the grade
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

# Displaying the grade
print(f"Your grade is {grade}")



