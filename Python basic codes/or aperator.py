#WAP to accept a number from a user and check wheather it is divisible by 3 or 5

num=int(input("Enter number :"))

if num%3==0 or num%5==0:
    print("the number is divisible by 3 or 5")
else:
    print("the number not divisible by 3 or 5")
