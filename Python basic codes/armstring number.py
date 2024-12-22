#WAP to check whether the number is armstring number or not
# for example n=153, 371

n = int(input("Enter a number: "))
temp = n  
sum1 = 0

while n > 0:
    rem = n % 10 
    sum1 = sum1 + (rem ** 3) 
    n = n // 10 

if sum1 == temp:
    print("The number is an Armstrong number.")
else:
    print("The number is not an Armstrong number.")
