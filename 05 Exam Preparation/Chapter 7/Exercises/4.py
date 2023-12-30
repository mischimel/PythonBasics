"""
4. Number Analysis Program
Design a program that asks the user to enter a series of 10 numbers.
The program should store the numbers in a list then display the following data:
• The lowest number in the list
• The highest number in the list
• The total of the numbers in the list
• The average of the numbers in the list
"""
def main():

    # instantiate variables
    numbers = []

    for i in range(1,11):
        num = int(input("enter a number: "))
        numbers.append(num)

    # instantiate variables
    total = 0
    for num in numbers:
        total += num

    average = total/(len(numbers))

    print("numbers entered:", numbers)
    print("min:", min(numbers))
    print("max:", max(numbers))
    print("total:", total)
    print("average:", average)

if __name__ == '__main__':
    main()