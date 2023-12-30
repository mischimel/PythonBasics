# For loop

# Example of a count-controlled loop (for loop)
for i in [1,2,3]:
    print(f"Iteration {i}: Hello, World!")

# End of the program
print("End of the loop.")

# Example of a count-controlled loop (for loop)
for i in range(1, 4):  # Range generates a sequence of numbers.txt from 1 to 3
    print(f"Iteration {i}: Hello, World!")

# End of the program
print("End of the loop.")

import math  # Import the math module for the sqrt function

# Example using the target variable (= num) inside the loop
for num in range(2, 5): # Range generates a sequence of numbers.txt from 2 to 4
    square_root = math.sqrt(num)
    print(f"The square root of {num} is {square_root:.2f}")

# End of the program
print("End of the loop.")

# Example letting the user control the loop iterations
start = int(input("Enter the starting value: "))
end = int(input("Enter the ending value: "))

for num in range(start, (end+1)): # end +1, to have the ending value included
    square = num ** 2
    print(f"The square of {num} is {square}")

# End of the program
print("End of the loop.")

# Example generating an iterable sequence from highest to lowest
for i in range(3, 0, -1): # 0 is not included
    print(i)

# End of the program
print("End of the loop.")


# Example calculating a running total
# Initialize the accumulator variable
total = 0

# Loop to read each number in the series
for i in range(1, 4):
    print(f"current total is {total}, current i {i} gets now added")
    total += i

# Display the final total
print(f"The running total is: {total}")

# End of the program
print("End of the loop.")





