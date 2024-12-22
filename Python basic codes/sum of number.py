# Get the sum of digits in a number

n = int(input("Enter a number: "))
sum1= 0
while n>0:
    rem=n%10
    sum1+=rem  
    n=n//10  
print("The sum of digits in the given number is", sum1)
