#WAP to check whether the number is palindrown or not

n=int(input("Enter a number: "))
temp=n
rev=0
while(n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
print("The reverse of a given number is",rev)


if rev==temp:
    print("The number is palindrown!")
else:
    print("The number is not palindrown!")
    
