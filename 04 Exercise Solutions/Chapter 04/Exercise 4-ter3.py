# Not a real infinite loop
# for i in range(10**100):
#   print(i)

# Real infinite loop
import itertools # the itertools.count() function generates an infinite sequence of numbers
for i in itertools.count():
    print("Value of i: ", i)
