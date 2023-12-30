"""
7. Random Number File Writer
Write a program that writes a series of random numbers to a file.
Each random number should be in the range of 1 through 500.
The application should let the user specify how many random numbers the file will hold.
"""

import random

def main():

    file = open("random_numbers.txt", "w")

    how_many_numbers = int(input("How many random numbers should we create? "))

    count = 1
    # loop to create as many random numbers as user said
    while count <= how_many_numbers:
        random_num = random.randint(1,500) # create random number
        as_string = str(random_num) + "\n" # convert to string and add newline
        file.write(as_string) #add to the file
        count +=1 # increase count

    file.close()


if __name__ == '__main__':
    main()