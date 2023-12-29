"""
6. Celsius to Fahrenheit Table
Write a program that displays a table of the Celsius temperatures 0 through 20 and their Fahrenheit equivalents.
The formula for converting a temperature from Celsius to Fahrenheit is
F = 9/5*C + 32
where F is the Fahrenheit temperature, and C is the Celsius temperature.
Your program must use a loop to display the table.
"""

# table header
print("Celsius \tFahrenheit")
print("---------------------------------------")

for celcius in range(0,21,1):
    fahrenheit = 9/5 * celcius + 32
    print(f"{celcius:.1f} \t\t{fahrenheit:.1f}")