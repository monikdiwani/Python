t1=("Monik",78,"A grade",56000,"Badlapur")
print(t1)

#to checking type of tuple1
print(type(t1))

#slicing a tuple
print(t1[1:4])
print(t1[2:])
print(t1[:5])

#find length of the tuple
print("The length of the tuple is:",len(t1))

#negetive indexing
print(t1[-2])
print(t1[-1])

'''
List is collection which is orered and changeable.
List allows duplicate members.
Tuple is a collection which is ordered and unchangeable.
Tuple allows  duplicate members
'''

t2=list(t1)
print(t2)

t2[2]="A in sports"
print(t2)

for i in t2:
    print(i)
