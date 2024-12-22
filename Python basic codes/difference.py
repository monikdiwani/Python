#WAP to find intersection of difference in set
set_a={5,8,67,3,6}
print(set_a)

set_b={6,9,5,6}
print(set_b)

set_c=(6,5,9,10)
print(set_c)

result=set_a-set_b
print("the difference is",result)

result=set_a.difference(set_b)
print("the difference is",result)


#WAP to get synmetric difference (means the number are not present in bothh the set)
result=set_a ^ set_b
print("The synmetric difference is",result)

result = set_a.symmetric_difference(set_b)
print(result)
