# Nested Loops

# Example of a nested loop to print a multiplication table
for i in range(1, 4):  # Outer loop for the rows
    for j in range(1, 6):  # Inner loop for the columns
        product = i * j
        print(f"{i}*{j}={product}", end="\t")  # Print in tab-separated format
    print()  # Move to the next line after completing inner loop

# End of the program
print("End of the loop.")
