"""
10. Most Frequent Character
Write a program that lets the user enter a string and displays the character that appears most frequently in the string.
"""
def main():

    def most_frequent_char(str):
        # create variables
        letter_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        index = 0
        frequency = 0

        # making all chars capitalizes
        for ch in str:
            ch = ch.upper()

            # find the current letter in the letters = 'ABCDEF...
            index = letters.find(ch)

            # make sure the current char is in the list
            if index >= 0:

                # count the occurence and increase the letter_count at matching index
                letter_count[index] += 1

        # looking for the highest frequency and setting the index of highest letter count = frequency
        for i in range(len(letter_count)):
            if letter_count[i] > letter_count[frequency]:
                frequency = i

        return print(f'The character that appears most frequently '
          f'in the string is {letters[frequency]}.')

    # get string from user
    user_string = input('Enter a string: ')
    most_frequent_char(user_string)


if __name__ == '__main__':
    main()

