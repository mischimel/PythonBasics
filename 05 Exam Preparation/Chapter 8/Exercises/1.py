"""
1. Initials
Write a program that gets a string containing a person’s first, middle, and last names,
and displays their first, middle, and last initials.
For example, if the user enters John William Smith, the program should display J. W. S.
"""
def main():

    full_name= str(input("Your full name: "))
    # tokenize string
    name_tokens = full_name.split()

    # loop through list name, get first char and capitalize it
    for name in name_tokens:
        print(name[0].upper(), sep="", end=". ")

if __name__ == '__main__':
    main()