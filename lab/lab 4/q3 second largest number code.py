l2 = [89, 67, 54, 65, 89, 78]

# Remove duplicates by converting the list to a set and back to a list
remove_dup = list(set(l2))
print("The final list is", remove_dup)

# Sort the list in ascending order
sorted_list = sorted(remove_dup)
print("Sorted List:", sorted_list)

# The second largest element is the second-to-last element in the sorted list
print("The second largest element is:", sorted_list[-2])
