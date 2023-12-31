"""
2. Capital Quiz
Write a program that creates a dictionary containing states as keys, and their capitals as values.
(Use the Internet to get a list of the states and their capitals.)
The program should then randomly quiz the user by displaying the name of a state and asking the user
to enter that state’s capital. The program should keep a count of the number of correct and incorrect responses.
"""

import random

def main():

    def capital_quiz(input_dict = {}):

        # Initialize counters for correct and incorrect responses
        correct_responses = 0
        incorrect_responses = 0

        # Get a list of states to use for quizzing
        keys_list = list(input_dict.keys())

        # Shuffle the list to randomize the order of questions
        random.shuffle(keys_list)

        # Quiz the user
        for key in keys_list:
            # Display the state and get user input for the capital
            user_input = input(f"What is the capital of {key}? (stop to finish quiz) ").strip()

            # Check if the user's input is correct
            if user_input.lower() == "stop":
                break
            elif user_input.lower() == input_dict[key].lower():
                print("Correct!\n")
                correct_responses += 1
            else:
                print(f"Incorrect. The capital of {key} is {input_dict[key]}.\n")
                incorrect_responses += 1

        # Display quiz results
        print("Quiz Results:")
        print(f"Correct Responses: {correct_responses}")
        print(f"Incorrect Responses: {incorrect_responses}")

    # create the dictionary to input to the function capital_quiz(input_dict = {}):
    states_capitals = {
            'Schweiz': 'Bern',
            'Luxembourg': 'Luxembourg',
            'Lichtenstein': 'Vaduz',
            'Belgien': 'Brüssel',
    }

    # input the dictionary to the function
    capital_quiz(states_capitals)

if __name__ == "__main__":
    main()
