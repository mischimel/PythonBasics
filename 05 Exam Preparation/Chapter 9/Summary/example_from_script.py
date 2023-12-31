# create a dictionary in which the keys are the integers 1 through 4 and the values are the squares of the keys

# Using a for loop
numbers = [1, 2, 3, 4]
squares = {}

for item in numbers:
    squares[item] = item ** 2

print(squares)

# Using a dictionary comprehension
numbers = [1, 2, 3, 4]
squares = { item:item**2 for item in numbers}
print(squares)

# You have an existing list of strings. Create a dictionary in which the keys are the stings in the list, and the values are the lengths of the strings
names = ['Jeremy', 'Kate', 'Peg']
str_lengths = {item:len(item) for item in names}
print(str_lengths)

# making a copy of a dictionary
dict1 = {'A':1, 'B':2, 'C':3}
dict2 = {keys:values for keys,values in dict1.items()}
print(dict2)
dict3 = dict1
print(dict3)

# A dictionary contains cities and their populations as key-value pairs. Select only the cities with a population greater than 2 million
populations = {'New York': 8398748, 'Los Angeles': 3990456,
               'Chicago': 2705994, 'Houston': 2325502,
               'Phoenix': 1660272, 'Philadelphia': 1584138}
largest = {keys:values for keys,values in populations.items() if values > 2000000}
print(largest)

# making a copy of a se
set1 = set([1, 2, 3, 4, 5])
set2 = {item for item in set1}
print(set2)

# creating a set that contains the squares of the numbers stored in another set
set1 = set([1, 2, 3, 4, 5])
set2 = {item**2 for item in set1}
print(set2)

# copying the numbers in a set that are less than 10
set1 = set([1, 20, 2, 40, 3, 50])
set2 = {item for item in set1 if item < 10}
print(set2)