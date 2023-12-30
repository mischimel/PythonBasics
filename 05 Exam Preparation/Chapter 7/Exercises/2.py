"""
2. Lottery Number Generator
Design a program that generates a seven-digit lottery number.
The program should generate seven random numbers, each in the range of 0 through 9,
and assign each number to a list element. (Random numbers were discussed in Chapter 5.)
Then write another loop that displays the contents of the list.
"""
import random
def main():

    # instantiate variables
    lottery_numbers = []

    for i in range(1,8,1):
        num = random.randint(0,9)
        lottery_numbers.append(num)

    for num in lottery_numbers:
        print(num,end="\t")

if __name__ == '__main__':
    main()