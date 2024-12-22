#WAP to print even number in tuple

tup1=(68,54,44,18,93,7)

for i in tup1:
    if i%2==0:
        print(i)

tup2=(45,[35,89],80,36,15,6,90,45)
print(tup2[0])
print(tup2[1])
print(tup2[1][0])
print(tup2[1][1])

tup2[1][0]=45
print(tup2)

