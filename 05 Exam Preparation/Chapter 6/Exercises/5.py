"""
5. Sum of Numbers
Assume a file containing a series of integers is named numbers.txt and exists on the computer’s disk.
Write a program that reads all of the numbers stored in the file and calculates their total.
"""
def main():

    file = open("numbers.txt", "r")

    file_content_lines = file.readlines() # read each line seperately

    sum = 0
    # loop through all the lines, convert them into int and add to sum
    for line in file_content_lines:
        num = int(line)
        sum += num

    print(sum)

if __name__ == '__main__':
    main()