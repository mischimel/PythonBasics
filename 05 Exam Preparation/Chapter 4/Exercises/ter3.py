"""
ter3. Infinite for loop
Write a program with a for loop that never stops execution (infinite loop)
"""
# Not a real infinite loop (range ends after (10**100)-1)
for i in range(10**100):
    print(i)

# Real infinite loop
import itertools

for i in itertools.count(): # the itertools.count() function generates an infinite sequence of numbers
    print("Value of i: ", i)
