#list is a collection which is ordered and changeable.
#allows duplicate members

shoping_list=["soap","oil","maggie","tea","buiscuits",1024,"rice"]
print(shoping_list)

for i in shoping_list:
    print(i)

shoping_list.append("dalia")
print(shoping_list)

#list element is recognized by its index values
#first element shoping_list[0]

print(shoping_list[0])

#there is concept of negative indexing
print(shoping_list[-1])

#slicing
print(shoping_list[1:4])
print(shoping_list[:])
print(shoping_list[2:])
print(shoping_list[:5])

#reversing the list
print(shoping_list[::-1])
