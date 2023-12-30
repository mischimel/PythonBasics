"""
11. Math Quiz
Write a program that gives simple math quizzes. The program should display two random numbers.txt that are to be added, such as:
247 + 129
The program should allow the student to enter the answer. If the answer is correct, a message of congratulations should be displayed.
If the answer is incorrect, a message showing the correct answer should be displayed.
"""
import random

def main():
    # Local variables
    QUESTIONS = 5
    LIMIT = 10

    # Repeat QUESTIONS times.
    for i in range(QUESTIONS):
        # Print the question number.
        print('Question', (i + 1))

        # Call generate_question and get the result.
        question = generate_question(LIMIT)

        # Display the question to the user.
        print(question)

        # Get the user's answer.
        user_answer = get_user_answer()

        # Check if the answer is correct and display a message.
        check_answer(question, user_answer)


# The generate_question function accepts max_number
# and returns a string of an addition question of
# two numbers.txt between 1 and max_number in the format
# "num1 + num2 = _____".
def generate_question(max_number):
    num1 = random.randint(1, max_number)
    num2 = random.randint(1, max_number)
    question = f"{num1} + {num2} = _____"
    return question

# The get_user_answer function prompts the user for an answer
# and returns the user's input as an integer.
def get_user_answer():
    while True:
        try:
            user_input = input("Enter your answer: ")
            user_answer = int(user_input)
            return user_answer
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# The check_answer function checks if the user's answer is correct
# and displays an appropriate message.
def check_answer(question, user_answer):
    # Extract the correct answer from the question.
    correct_answer = eval(question.split('=')[0].strip())

    if user_answer == correct_answer:
        print("Congratulations! Your answer is correct.\n")
    else:
        print(f"Sorry, the correct answer is {correct_answer}.\n")

if __name__ == '__main__':
    main()