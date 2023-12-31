"""
2. Sum of Digits in a String
Write a program that asks the user to enter a series of single-digit numbers with nothing separating them.
The program should display the sum of all the single digit numbers in the string.
For example, if the user enters 2514, the method should return 12, which is the sum of 2, 5, 1, and 4.
"""
def main():

    def sum_calc(str):
        total = 0
        for i in str:
            total += int(i)
        return total

    num_string = input("enter a series of single-digit numbers with nothing separating them: ")

    print(f"total is: {sum_calc(num_string)}")

if __name__ == '__main__':
    main()