# Sentinels

# Example using a sentinel value
sentinel = -1  # Define the sentinel value

# Initialize the total accumulator
total = 0

# Loop to read numbers until the sentinel is encountered
while True:
    value = float(input("Enter a number (or -1 to end): "))

    if value == sentinel:
        break  # Break out of the loop when the sentinel is encountered

    total += value  # Add the current value to the running total

# Display the final total
print(f"The running total is: {total}")

# End of the program
print("End of the loop.")
