#WAP to find factorial of a number
#5!=5*4*3*2*1=120

n=int(input("Enter a number "))
fact=1
for i in range(1,n+1):
    fact=fact*i
    print(fact)
print("Factorial of ",n," is ",fact)
