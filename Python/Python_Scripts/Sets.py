# Creating a set
my_set = {1, 2, 3, 4, 5}

# Adding elements to the set
my_set.add(6)
my_set.update({7, 8, 9})
print("Updated set:", my_set)

# Removing elements from the set
my_set.remove(3)
print("Set after removing 3:", my_set)

# Checking membership
print("Is 5 in the set?", 5 in my_set)

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union
union_set = set1.union(set2)
print("Union of sets:", union_set)

# Intersection
intersection_set = set1.intersection(set2)
print("Intersection of sets:", intersection_set)

# Difference
difference_set = set1.difference(set2)
print("Difference of sets:", difference_set)

my_set.discard(2)
print("Set after discarding 2:", my_set)
