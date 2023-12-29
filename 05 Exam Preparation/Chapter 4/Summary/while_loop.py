# While loop

# Example of a while loop
count = 1

while count <= 3:
    print(f"Count is {count}")
    count += 1  # Incrementing the count variable

print("End of the program, while loop finished before this line got executed.")

# Example of a while loop (pretest loop)
target_number = 7
guess = 0
attempts = 0

while guess != target_number: # test -> when user got the correct number, while loop will not be executed again
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < target_number:
        print("Too low! Try again.")
    elif guess > target_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the correct number {target_number} in {attempts} attempts.")

print("End of the program.")

# Example of an infinite loop (without break loop would never end)
while True:
    user_input = input("Enter a value (type 'exit' to end): ")

    if user_input.lower() == 'exit':
        break  # Break out of the infinite loop if the user enters 'exit'

    # Perform some operation with the input
    processed_value = user_input.upper()
    print(f"Processed value: {processed_value}")

# This statement will be reached only after breaking out of the loop
print("End of the program.")


