list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [9, 2, 8, 3, 0, 6, 10]
print(list1)
print(list2)

# Find the intersection of the two lists using set operations
intersection = list(set(list1) & set(list2))

print("The intersection of both lists is:", intersection)
