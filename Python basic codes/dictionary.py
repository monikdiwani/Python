'''
a dictionary is a bult-in data structure in python
that allows you to stour a collection of key-value pairs.

dictionary is mutable it is unordered
'''

my_dict={
    "std_id":1024,
    "std_name":"Monik",
    "course":"BCA"
}

print(my_dict)

x=my_dict["course"]
print("The course selected is ",x)

x=my_dict.get("std_id")
print(x)

#find all the keys present in the dictionary

y=my_dict.keys()
print("the keys present are:",y)

# to update dictionary element
my_dict.update({"std_name":"Diwani"})
print(my_dict)

#to add new element in the dictionary
my_dict["fees"]=34000
print(my_dict)

my_dict["address"]="Badlapur"
print(my_dict)

#to remove certain element form the dictionary
my_dict.popitem()
print(my_dict)

#looping over dictionary

for i in my_dict:
    print(i)

#to get keys from the dictionary
for i in my_dict.keys():
    print(i)


#to get values from the dictionary
for i in my_dict.values():
    print(i)

#to grt both keys and values from the dictionary
for x,y in my_dict.items():
    print(x,y)

my_dict.pop("std_name")
print(my_dict)
