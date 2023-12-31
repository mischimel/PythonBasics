"""
8. Sentence Capitalizer
Write a program with a function that accepts a string as an argument and returns a copy
of the string with the first character of each sentence capitalized. For instance,
if the argument is “hello. my name is Joe. what is your name?”
the function should return the string “Hello. My name is Joe. What is your name?”
The program should let the user enter a string and then pass it to the function.
The modified string should be displayed.
"""
def main():

    # Define a function that capitalizes the first character of each sentence
    def cap_string(text):
        # Initialize an empty list to store modified sentences
        new_sentence_list = []

        # Split the input text into sentences using '.' as the delimiter
        sentence_list = text.split('.')

        # Remove the last element, which is an empty string due to the trailing '.' in the input
        sentence_list = sentence_list[:-1]

        # Iterate through each sentence in the list
        for sentence in sentence_list:
            # Strip leading and trailing whitespaces from the sentence and capitalize the first character
            new_sentence = sentence.strip().capitalize()

            # Append the modified sentence to the new_sentence_list
            new_sentence_list.append(new_sentence)

        # Return the list of modified sentences
        return new_sentence_list

    # Get input from the user
    text = input('Enter an arbitrary text: ')

    # Call the cap_string function with the user input
    new_text = cap_string(text)

    # Print each modified sentence, ending with a '.'
    for item in new_text:
        print(item, end='. ')

if __name__ == '__main__':
    main()

