"""
1. Kilometer Converter
Write a program that asks the user to enter a distance in kilometers,
then converts that distance to miles. The conversion formula is as follows:
Miles = Kilometers * 0.6214
"""

# only executed when running this file!
def main():
    km = float(input("Enter a distance in km: "))

    if km != 0 and km > 0:
        print(f"{km:.2f} km are {covert_to_miles(km):.2f} miles")

# could be used in other modules
def covert_to_miles (kilometers):
    miles = kilometers * 0.6214
    return miles

# Conditionally execute main only if this module is run as the main program
if __name__ == '__main__':
    main()
