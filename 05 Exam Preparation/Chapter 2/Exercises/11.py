"""
11. Male and Female Percentages
Write a program that asks the user for the number of males and the number of females registered in a class.
The program should display the percentage of males and females in the class.
Hint: Suppose there are 8 males and 12 females in a class. There are 20 students in the class.
The percentage of males can be calculated as 8 ÷ 20 = 0.4, or 40%.
The percentage of females can be calculated as 12 ÷ 20 = 0.6, or 60%.
"""

# Userinput
male = int(input("How many males are in your calss: "))
female = int(input("How many females are in your calss: "))

total_calss = male + female

male_percentage = male / total_calss
female_percentage = female / total_calss

print(f"In the class are total {total_calss} students, \n"
      f"{male} of them are male, what is {male_percentage*100}% and \n"
      f"{female} of them are female, what is {female_percentage:.2%}.")