# This program displays five random
# numbers.txt in the range of 1 through 100.
import random # random is a module

def main():
    for count in range(5):
        print(random.randint(1, 100))

# Call the main function.
main()
