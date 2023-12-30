import random

# Example 1: Random numbers.txt without specifying a seed
print("Example 1: Random numbers.txt without specifying a seed")
for _ in range(5):
    print(random.randint(1, 100), end=' ')
print("\n")

# Example 2: Random numbers.txt with a specified seed
print("Example 2: Random numbers.txt with a specified seed")
# Setting the seed to a specific value (e.g., 42)
random.seed(42)
for _ in range(5):
    print(random.randint(1, 100), end=' ')
print()

# As long as the seed remains the same,
# the sequence of random numbers.txt will be the same every time you run the program
random.seed(42)
for _ in range(5):
    print(random.randint(1, 100), end=' ')
