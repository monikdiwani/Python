'''
ordered
when we say that tuples are ordered,it means that the item have a
defined order, and that order will not change.
Unchangeable:tuple are unchangeable,meaning that we cannot change,add or romove
item sfter the tuple has been created.
since tuple are indexed, they can have items with the same value:
'''
thistuple=("apple","banana","cherry","apple","cherry")
print(thistuple)

#find the length of the tuple
print(len(thistuple))

#tuple is also recognized by its index no.
print(thistuple[0])
print(thistuple[3])
print(thistuple[2:4])
