# Creating a Set
# Using curly braces
my_set = {1, 2, 3}

# Using the set() function
another_set = set([3, 4, 5])


my_set = {1, 2, 3}
# Adding an element
my_set.add(4)

# Removing an element
my_set.remove(2)
print(my_set)

my_set = {1, 2, 3}
# Using a for loop to iterate over elements
for item in my_set:
    print(item)

print("set Operations")
# Set Operations
my_set = {1, 2, 3}
another_set = set([3, 4, 5])

# Union of two sets
union_set = my_set.union(another_set)
union_set2 = my_set | another_set
print(union_set)
print(union_set2)

# Intersection of two sets
intersection_set = my_set.intersection(another_set)
intersection_set2 = my_set & another_set
print(intersection_set)
print(intersection_set2)

# Difference of two sets
difference_set = my_set.difference(another_set)
difference_set2 = my_set - another_set
print(difference_set)
print(difference_set2)

print("set Operations2")
# Set Operations
my_set = {1, 2, 3}
another_set = set([3, 4, 5])

# Symmetric difference of two sets
symmetric_difference_set = my_set.symmetric_difference(another_set)
symmetric_difference_set2 = my_set ^ another_set
print(symmetric_difference_set)
print(symmetric_difference_set2)

my_set = {1, 2, 3}
another_set = set([1, 2, 3, 4, 5])
# Set A is subset of set B
subset = my_set.issubset(another_set)
subset2 = my_set <= another_set
print(subset)
print(subset2)

# Set A is superset of set B
superset = my_set.issuperset(another_set)
superset2 = my_set >= another_set
print(superset)
print(superset2)