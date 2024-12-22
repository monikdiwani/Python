#WAP to reverse a given number

n=int(input("Enter a number: "))
rev=0
while(n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
print("The reverse of a given number is",rev)
