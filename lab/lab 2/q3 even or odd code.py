#Q.3) WAP to check whether the number is even or not.

# Get a number from the user
number = int(input("Enter a number: "))

# Check if the number is divisible by 2
if number % 2 == 0:
# If true, the number is even else it is false number will be odd
    print("Number", number, "is even")
else:
    print("Number", number, "is odd")
