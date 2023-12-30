# This program demonstrates how numbers.txt
# must be converted to strings before they
# are written to a text file.

def main():
    # Open a file for writing.
    outfile = open('numbers.txt', 'w') # it does create a .txt file called numbers.txt (so no such file needs to exist)

    # Get three numbers.txt from the user.
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter another number: '))
    num3 = int(input('Enter another number: '))

    # Write the numbers.txt to the file.
    outfile.write(str(num1) + '\n')
    outfile.write(str(num2) + '\n')
    outfile.write(str(num3) + '\n')

    # Close the file.(close file handler)
    outfile.close()
    print('Data written to numbers.txt.txt')

# Call the main function.
if __name__ == '__main__':
    main()