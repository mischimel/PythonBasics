# Write a program that asks the user to enter a series of single-digit numbers.txt with nothing separating them.
# The program should display the sum of all the single digit numbers.txt in the string.
# For example, if the user enters 2514, the method should return 12, which is the sum of 2, 5, 1, and 4.

def main():
    numbers = input("Please enter a series of single-digit numbers.txt with nothing separating them: ")

    print(f"The total of yeach number of {numbers} is {total_of_numbers(numbers)}")

def total_of_numbers (string):
    number = 0
    total = 0
    for i in range(len(string)):
        number = int(string[i])
        total += number

    return total

if __name__ == "__main__":
    main()