"""
1. File Display
Assume a file containing a series of integers is named numbers.txt and exists on the computer’s disk.
Write a program that displays all of the numbers in the file.
"""
def main():

    # open file
    file = open("numbers.txt","r")

    # read whole file
    file_content = file.read()
    print(file_content)


    # close file
    file.close()

if __name__ == '__main__':
    main()