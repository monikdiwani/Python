# Function to find the maximum of two numbers
def maximum(a, b):
    if a > b:
        return a
    else:
        return b

# Taking two numbers as input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Displaying the maximum number
print(f"The maximum number between {num1} and {num2} is {maximum(num1, num2)}")
