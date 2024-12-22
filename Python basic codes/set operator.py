'''
a set in python programming is an unordered collection data type that
is iterable and has no duplicate element. while sets are mutable,
meaning you can add or remove elements after their creation
'''

set_a={5,8,73,3}
print(set_a)

set_b={6,9,5,6}
print(set_b)

set_c={7,9,78,4}
print(set_c)

#set union opertion
set_d=set_a.union(set_b)
print("The union of both the sets are:",set_d)

set_e=set_a.union(set_b,set_c)
print("The union of all the sets are",set_e)

#using union operation |

result=set_a | set_b | set_c
print("The union of all is ",result)
